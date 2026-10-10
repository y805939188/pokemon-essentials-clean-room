"""Finite independent actual Git/JSON/hash/TSV/text checks; no historical program execution."""
import collections
import csv
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path

ACT = 'a46d6c457ff0a01181f22a80af25419370f86149'
BASE = '1d06c45cc0a744fca181ac80ee573cc9ebb9b862'
CAND = '8ddba850af71f24e7bd77a80b7605c456c31dc7a'
MGMT = '9ad5539f38544fef6037356018015fe418021514'
PACKET = 'aa90d3988b410b4bec447f4f80d1b63ab97c46c9'
OWN_REPORT = 'e94ed84d5118f3fc53091f8055db00aab20b62fb'
FULL_REPORT = '76a49b3829fa8193107851b6816ab317ff94c815'
ROOT = 'review/remediation/20261003-prepare/batches/B12/'
OUT = Path(ROOT + 'affected-actual-review-1/B02')
OWNERS = ['B02', 'B03', 'B04', 'B07', 'B08', 'B09', 'B10', 'B11', 'B14', 'B15']
checks, cache = [], {}

def git(*args):
    return subprocess.check_output(['git', *args])

def blob(commit, path):
    if (commit, path) not in cache:
        raw = git('show', commit + ':' + path)
        ident = {'commit': commit, 'path': path,
                 'git_blob': git('rev-parse', commit + ':' + path).decode().strip(),
                 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
        cache[commit, path] = raw, ident
    return cache[commit, path]

def obj(path, commit=ACT):
    return json.loads(blob(commit, path)[0])

def check(label, passed, **detail):
    checks.append({'check': label, 'pass': bool(passed), **detail})

def exact(binding):
    raw, identity = blob(binding['commit'], binding['path'])
    check('exact finite input binding', all(identity[k] == binding[k]
          for k in ['git_blob', 'sha256', 'bytes']), identity=identity)
    return raw

def tree(commit):
    result = {}
    for row in git('ls-tree', '-rz', commit).split(b'\0'):
        if row:
            meta, path = row.split(b'\t', 1)
            result[path.decode()] = meta.decode()
    return result

def rows(raw):
    return list(csv.DictReader(io.StringIO(raw.decode()), delimiter='\t'))

def logical_hash(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(',', ':')).encode()).hexdigest()

freeze = obj(ROOT + 'actual-freeze-1/actual-freeze.json', PACKET)
request = obj(ROOT + 'integration-stage-1/actual-review-request.json')
check('frozen ACT tree', git('rev-parse', ACT + '^{tree}').decode().strip()
      == freeze['reviewed_actual_tree'] == '1d1c3ea7b217463b88146c7640ae4a6821c25c54')
check('formal predecessor distinct from management successor', freeze['current_formal_accepted_predecessor']
      == BASE and freeze['reviewed_actual_commit'] == ACT and PACKET != ACT)
check('all ten exact role scopes', [r['gate'] for r in request['required_roles'] if r['gate'] != 'FULL'] == OWNERS)
for owner in OWNERS:
    role = next(r for r in request['required_roles'] if r['gate'] == owner)
    check('allowed actual output path', role['output_directory'] == ROOT + 'affected-actual-review-1/' + owner + '/', owner=owner)

trees = {c: tree(c) for c in [BASE, CAND, MGMT, ACT, OWN_REPORT, FULL_REPORT]}
formal = request['formal_scope']
public = ['review/remediation/20261003-prepare/' + p for p in
          ['approval-ledger.tsv', 'traceability-successor.tsv', 'final-integration-review.md']]
check('precise 11 final and five original boundary', len(formal) == 16 and
      sum(p.startswith('deliverables/') for p in formal) == 11 and
      sum(p.startswith('specs/') for p in formal) == 5)
for p in formal:
    check('ACT payload exactly candidate', blob(ACT, p)[0] == blob(CAND, p)[0],
          candidate=blob(CAND, p)[1], actual=blob(ACT, p)[1])
check('all prior tracked paths retained', set(trees[BASE]) <= set(trees[ACT]))
old_changed = [p for p in trees[BASE] if trees[BASE][p] != trees[ACT].get(p)]
check('all old accepted content outside authorized 16 and public3 byte identity', set(old_changed) == set(formal + public),
      old_tracked_paths=len(trees[BASE]), authorized_old_changes=old_changed)
for p in trees[MGMT]:
    if p not in formal + public and p not in trees[BASE]:
        check('frozen management metadata exact', trees[MGMT][p] == trees[ACT].get(p), path=p)
management_new = set(trees[MGMT]) - set(trees[BASE])
check('exact28 management files, no B16 private prep import', len(management_new) == 28 and
      all('/refreeze-after-B15-C-1/' in p or '/B15/acceptance-stage-1/downstream-dispatch-1/' in p for p in management_new))
archive_sources = {}
for p in trees[CAND]:
    if p.startswith(ROOT + 'author-draft-1/') or p.startswith(ROOT + 'candidate-1/'):
        archive_sources[p] = CAND
for source, prefix in [(OWN_REPORT, ROOT + 'affected-candidate-review-1/'),
                       (FULL_REPORT, ROOT + 'candidate-review-1/')]:
    for p in trees[source]:
        if p.startswith(prefix): archive_sources[p] = source
check('27 author and45 candidate independent archives', len(archive_sources) == 72 and
      sum(c == CAND for c in archive_sources.values()) == 27)
for p, source in sorted(archive_sources.items()):
    check('exact frozen archive, never executed', blob(source, p)[0] == blob(ACT, p)[0],
          source=blob(source, p)[1], actual=blob(ACT, p)[1])
g_paths = [p for p in trees[ACT] if p.startswith(ROOT + 'integration-stage-1/')]
check('exact11 new G files', len(g_paths) == 11)
for p in g_paths:
    if p.endswith('.json'):
        obj(p)
        check('G JSON parse', True, path=p)
expected_additions = set(archive_sources) | management_new | set(g_paths)
check('all actual new paths within explicit integration scopes', set(trees[ACT]) - set(trees[BASE]) == expected_additions)
for binding in freeze['publication_receipt']['identities']:
    exact(binding)

def category(path):
    if path in formal: return 'approved-formal-or-original-payload'
    if path in public: return 'public-pending-registration'
    if path in archive_sources: return 'exact-static-archive'
    if path in management_new: return 'exact-frozen-management'
    if path in g_paths: return 'new-G-bookkeeping'
    return 'UNEXPECTED'

diffs = []
for frozen in freeze['complete_unfiltered_differences']:
    cmd = ['diff', '--no-ext-diff', '--no-textconv', '--binary', '--full-index', frozen['from'], ACT]
    raw = git(*cmd)
    changed = git('diff', '--name-status', frozen['from'], ACT).decode().splitlines()
    chunks = re.split(b'(?=^diff --git )', raw, flags=re.M)
    chunks = [c for c in chunks if c]
    entries = []
    for line, chunk in zip(changed, chunks):
        status, path = line.split('\t')
        check('complete all-path diff scoped consumption', category(path) != 'UNEXPECTED', path=path, category=category(path))
        entries.append({'status': status, 'path': path, 'scope': category(path),
                        'full_diff_chunk_sha256': hashlib.sha256(chunk).hexdigest(), 'chunk_bytes': len(chunk)})
    check('complete unfiltered full-index diff identity', hashlib.sha256(raw).hexdigest() == frozen['sha256']
          and len(raw) == frozen['bytes'] and len(changed) == frozen['changed_path_count'] == len(chunks), name=frozen['name'])
    diffs.append({'name': frozen['name'], 'command': ['git'] + cmd, 'sha256': hashlib.sha256(raw).hexdigest(),
                  'bytes': len(raw), 'changed_paths': len(changed), 'all_chunks_consumed': True,
                  'path_filter': None, 'duplicate_7MB_artifact_committed': False, 'entries': entries})

copy_doc = obj(ROOT + 'integration-stage-1/formal-copy-identities.json')
for item in copy_doc['identities']:
    exact(item['candidate'])
    exact(item['accepted_before'])
scope = obj(ROOT + 'author-draft-1/scope-amendment-1.json')
originals = []
for item in scope['proposals']:
    p = item['path']
    b, bi = blob(BASE, p)
    a, ai = blob(ACT, p)
    check('authorized original exact before and approved after',
          bi['git_blob'] == item['before_git_blob'] and bi['sha256'] == item['before_sha256'] and
          ai['sha256'] == item['approved_after_sha256'] == item['actual_after_sha256'] and
          ai['git_blob'] == item['actual_after_git_blob'] and ai['bytes'] == item['actual_after_bytes'], path=p)
    check('approved patch archive identity retained', blob(ACT, item['approved_patch_path'])[1]['git_blob']
          == item['approved_patch_blob'] and blob(ACT, item['approved_patch_path'])[1]['sha256'] == item['approved_patch_sha256'], path=p)
    originals.append({'path': p, 'before': bi, 'actual': ai, 'proposal_number': item['proposal_number'],
                      'effective_clause_labels': item['effective_clause_labels'],
                      'prior_exact_patch_reconstruction_reused': True})
check('proposal4 corrected effective section4, no patch identity revision', scope['label_correction']['effective_label']
      == '§4 宝石比较参数' and scope['label_correction']['patch_content_or_identity_changed'] is False)

previous_shared = obj(ROOT + 'affected-candidate-review-1/B02/shared-metadata.json', OWN_REPORT)
check('prior shared evidence exactly versioned, no failures', not previous_shared['failures']
      and previous_shared['reviewed_sha'] == CAND and previous_shared['behavior_executions'] == 0)
owner_versions = {}
for owner in OWNERS:
    old = obj(ROOT + 'affected-candidate-review-1/' + owner + '/result.json', OWN_REPORT)
    exact(old['version_basis']['accepted_receipts_binding'])
    preserved = []
    for body in old['version_basis']['unchanged_owner_body_identities']:
        p = body['after']['path']
        check('current accepted owner body protection', blob(ACT, p)[0] == blob(BASE, p)[0] == blob(CAND, p)[0], owner=owner, path=p)
        preserved.append(blob(ACT, p)[1])
    owner_versions[owner] = {'prior_report': blob(OWN_REPORT, ROOT + 'affected-candidate-review-1/' + owner + '/result.json')[1],
                             'qualified_receipts': old['version_basis']['prior_scoped_receipts'], 'current_owner_bodies': preserved}

catalogs = []
for old in previous_shared['catalogs']:
    p = old['path']
    def catalog_rows(commit):
        return [line for line in blob(commit, p)[0].splitlines(keepends=True)
                if re.match(rb'^\| [A-Z]+[0-9]+[a-z]? \|', line)]
    before, after = catalog_rows(BASE), catalog_rows(ACT)
    cursor, inserted = 0, []
    for row in after:
        if cursor < len(before) and row == before[cursor]: cursor += 1
        else: inserted.append(row.decode().rstrip('\n'))
    check('catalog all old raw rows, order and multiplicity', cursor == len(before)
          and len(before) == old['old_rows'] and len(after) == old['new_rows'], path=p)
    catalogs.append({'path': p, 'before': blob(BASE, p)[1], 'actual': blob(ACT, p)[1],
                     'old_rows': len(before), 'actual_rows': len(after), 'all_old_rows_preserved': cursor == len(before),
                     'added_unexecuted_designs': inserted})
check('both changed catalogs387 old rows plus15 designs', sum(c['old_rows'] for c in catalogs[:2]) == 387
      and sum(len(c['added_unexecuted_designs']) for c in catalogs[:2]) == 15)

registration = obj(ROOT + 'integration-stage-1/finding-registration.json')
qualified = obj(ROOT + 'refreeze-after-B15-C-1/B12-downstream-contract.json')
stats_path = 'review/remediation/20261003-prepare/batches/B15/acceptance-stage-1/completion-statistics-successor.json'
stats = obj(stats_path)
check('B15 accepted statistics exact current', blob(ACT, stats_path)[0] == blob(BASE, stats_path)[0])
check('accepted13/21,223,175,143,strict133/10 retained', len(stats['accepted_batches']) == 13 and
      stats['contribution_records'] == 223 and stats['distinct_touched_IDs'] == 175 and stats['primary_denominator'] == 143
      and stats['strict_all_planned_contribution_counts'] == {'all_contributor_batches_accepted': 133, 'pending': 10})
registration_protections = []
for record, control in zip(registration['records'], qualified['contribution_controls']):
    check('complete qualified fields and whole object identities retained', record['id'] == control['id']
          and record['complete_current_control_fields'] == control['complete_current_control_fields']
          and record['whole_original_object_sha256'] == control['whole_original_object_sha256']
          and record['whole_acceptance_object_sha256'] == control['whole_acceptance_object_sha256'], finding=record['id'])
    accepted = sorted({x['batch'] for x in stats['accepted_contribution_receipts'] if x['id'] == record['id']})
    contributors = sorted(control['all_contributor_batches'])
    remaining = sorted(set(contributors) - set(accepted))
    check('accepted contributor receipts and remaining obligations', sorted(record['accepted_contributors']) == accepted
          and sorted(record['all_contributors']) == contributors and sorted(record['remaining_contributors']) == remaining,
          finding=record['id'])
    check('new record remains pending, canonical open', record['canonical_state'] == 'OPEN'
          and record['current_status'] == 'INTEGRATED_PENDING_EXACT_ACTUAL; NOT_ACCEPTED', finding=record['id'])
    registration_protections.append({'id': record['id'], 'qualified_field_logical_sha256': logical_hash(record['complete_current_control_fields']),
                                    'all_contributors': contributors, 'accepted_contributors': accepted,
                                    'remaining_contributors': remaining, 'actual_status': record['current_status']})
check('new nine records six primary, zero new acceptance', len(registration['records']) == 9 and
      sum(r['primary'] for r in registration['records']) == 6 and registration['new_B12_accepted_contributions'] == 0)
table_evidence = []
for p in public[:2]:
    before, after = blob(BASE, p)[0], blob(ACT, p)[0]
    old_rows, all_rows = rows(before), rows(after)
    new = all_rows[len(old_rows):]
    check('old223 public entire raw prefix retained', after.startswith(before) and len(old_rows) == 223 and len(all_rows) == 232, path=p)
    check('nine new public pending, no closure or automatic actual', len(new) == 9 and
          {r['finding_id'] for r in new} == {r['id'] for r in registration['records']} and
          all(r['canonical_state'] == 'OPEN' and 'PENDING' in r.get('integration_disposition', r.get('integration_gate', '')) for r in new), path=p)
    for row in new:
        obligations = json.loads(row['remaining_obligations'])
        record = next(r for r in registration['records'] if r['id'] == row['finding_id'])
        check('public complete control and contributor obligations exact', obligations['record_key'] == record['record_key']
              and sorted(obligations['remaining_contributors']) == sorted(record['remaining_contributors'])
              and sorted(obligations['accepted_contributors']) == sorted(record['accepted_contributors'])
              and obligations['canonical_final_closure'] == 'NOT_PERFORMED', finding=row['finding_id'], path=p)
    table_evidence.append({'path': p, 'before': blob(BASE, p)[1], 'actual': blob(ACT, p)[1],
                           'old_accepted_raw_prefix_preserved': True, 'old_rows': len(old_rows), 'physical_rows': len(all_rows),
                           'new_pending_rows': len(new)})
final_old, final_new = blob(BASE, public[2])[0], blob(ACT, public[2])[0]
check('old final integration body exact suffix, new header pending only', final_new.endswith(final_old)
      and '待精确实际复审'.encode() in final_new[:len(final_new)-len(final_old)])
canonical_path = 'review/remediation/20261003-prepare/finding-ledger.tsv'
canonical = rows(blob(ACT, canonical_path)[0])
check('canonical exact ledger229OPEN0CLOSED', blob(ACT, canonical_path)[0] == blob(BASE, canonical_path)[0]
      and len(canonical) == 229 and all(r.get('canonical_state', r.get('state')) == 'OPEN' for r in canonical))

limits = obj(ROOT + 'integration-stage-1/source-limits.json')
check('all static execution limits zero', all(limits[k] == 0 for k in ['reference_execution', 'behavior_vectors_executed',
      'runtime_observations', 'proven_Demo_chains', 'historical_author_reviewer_program_execution']))
check('conditional67 and nonlocal obligations retained', limits['conditional_67_berry_rows_retained'] and
      limits['nonlocal_shared_findings_and_all_other_batches_remain_open'])
failures = [c for c in checks if not c['pass']]
result = {'role': 'INDEPENDENT_AFFECTED_ACTUAL_REVIEWER', 'reviewed_sha': ACT, 'reviewed_tree': freeze['reviewed_actual_tree'],
          'accepted_predecessor': BASE, 'candidate': CAND, 'packet': PACKET, 'prior_independent_report': OWN_REPORT,
          'checks': checks, 'passed': len(checks) - len(failures), 'failures': failures, 'complete_diffs': diffs,
          'original_scope': originals, 'catalogs': catalogs, 'owner_versions': owner_versions,
          'public_tables': table_evidence, 'qualified_registration_protections': registration_protections,
          'finite_input_identities': [identity for raw, identity in cache.values()],
          'historical_programs_executed': 0, 'reference_game_ruby_behavior_executions': 0,
          'actual_quality_inferred_from_metadata': False, 'formal_C': False, 'subtasks_spawned': 0}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'shared-actual-metadata.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'checks': len(checks), 'passed': result['passed'], 'failures': failures}, ensure_ascii=False))
if failures: raise SystemExit(1)
