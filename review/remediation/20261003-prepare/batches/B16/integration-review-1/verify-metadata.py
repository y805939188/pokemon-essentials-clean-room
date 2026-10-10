#!/usr/bin/env python3
"""Fresh exact ACT Git/text/JSON/TSV metadata checks; no historical program execution."""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
PREFIX = 'review/remediation/20261003-prepare/batches/B16/'
PUBLIC = 'review/remediation/20261003-prepare/'
C = '27185563f307e16d2612fa86e83b2c9bd772c79e'
NEW = '356b46b320884e57e71a1cab8413e13594524a7d'
ACT = '29b21fe188cce4e76f5a2f566f9144f1c3f53239'
PACKET = '7372479c763b90271f0bf8fbab68a15862739ba0'
CANDIDATE_REPORT = 'da58ab3e8ce5e508b2ed55928c6f334cb64a2445'
CONTROL_PACKET = '8e2753430ccb4bad8098048c814576aa386a09ef'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF_GIT = '/tmp/b16-reference.git'
checks, inputs = [], []
cache = {}


def git(*args, reference=False):
    cmd = ['git', '-c', 'core.hooksPath=/dev/null']
    cmd += ['--git-dir=' + REF_GIT] if reference else ['-C', str(ROOT)]
    return subprocess.check_output(cmd + list(args))


def blob(commit, path, reference=False):
    key = (commit, path, reference)
    if key not in cache:
        cache[key] = git('show', commit + ':' + path, reference=reference)
    return cache[key]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def check(name, passed, detail=None):
    checks.append({'check': name, 'pass': bool(passed), 'detail': detail})


def load(commit, path):
    return json.loads(blob(commit, path))


def identity(commit, path, reference=False):
    data = blob(commit, path, reference)
    return {'commit': commit, 'path': path, 'bytes': len(data), 'sha256': digest(data),
            'git_blob': git('rev-parse', commit + ':' + path, reference=reference).decode().strip()}


def verify(binding, label):
    actual = identity(binding['commit'], binding['path'])
    check(label, all(actual[k] == binding[k] for k in ('git_blob', 'sha256', 'bytes') if k in binding))
    inputs.append({'label': label, **actual})
    return blob(binding['commit'], binding['path'])


def tree(commit):
    result = {}
    for entry in git('ls-tree', '-r', '-z', commit).split(b'\0'):
        if entry:
            meta, path = entry.split(b'\t', 1)
            result[path.decode()] = meta.decode()
    return result


d = load(PACKET, PREFIX + 'actual-freeze-1/full-actual-dispatch.json')
for key in ('candidate_FULL_report', 'original_qualified_controls', 'approved_acceptance',
            'complete_case_constraints', 'inherited_source_limits', 'G_registration',
            'accepted_preservation', 'scope3', 'scope4'):
    verify(d[key], 'dispatch/' + key)
for key, binding in d['complete_control_bindings'].items():
    verify(binding, 'dispatch/complete-controls/' + key)
for binding in d['public_pending_registration']:
    verify(binding, 'dispatch/public/' + binding['path'])
check('ACT/exact-tree', git('rev-parse', ACT + '^{tree}').decode().strip() == d['reviewed_ACT_tree'])
check('NEW/exact-tree', git('rev-parse', NEW + '^{tree}').decode().strip() == d['reviewed_candidate_NEW_tree'])
check('C/exact-tree', git('rev-parse', C + '^{tree}').decode().strip() == d['formal_accepted_input_C_tree'])
check('target/explicit-ACT', d['reviewed_ACT'] == ACT and d['formal_accepted_input_C'] == C and d['reviewed_candidate_NEW'] == NEW)
check('AGENTS/same', blob(C, 'AGENTS.md') == blob(NEW, 'AGENTS.md') == blob(ACT, 'AGENTS.md') == blob(PACKET, 'AGENTS.md'))
candidate_manifest = load(CANDIDATE_REPORT, PREFIX + 'candidate-review-2/artifact-manifest.json')
for binding in candidate_manifest['files']:
    verify({'commit': CANDIDATE_REPORT, **binding}, 'own-published-candidate-proof/' + binding['path'])
prior = load(CANDIDATE_REPORT, PREFIX + 'candidate-review-2/review.json')
prior_meta = load(CANDIDATE_REPORT, PREFIX + 'candidate-review-2/metadata-verification.json')
check('candidate/own-339-checks-valid', prior_meta['check_count'] == 339 and not prior_meta['failed_checks'] and all(c['pass'] for c in prior_meta['checks']))
check('candidate/exact-target-not-ACT-verdict', prior['reviewed_NEW'] == NEW and prior['verdict'] == 'PASS_SCOPED' and not prior['blockers'])

frozen = load(PACKET, d['frozen_output_manifest']['path'])
payload = [x['path'] for x in frozen['outputs']]
check('payload/eleven-six-five', len(payload) == 11 and frozen['formal_outputs'] == 6 and frozen['authorized_original_outputs'] == 5)
outputs = []
for entry in frozen['outputs']:
    for key in ('accepted_C_before', 'reviewed_NEW', 'frozen_ACT'):
        verify(entry[key], 'payload/' + key + '/' + entry['path'])
    check('payload/NEW-to-ACT-full-bytes/' + entry['path'], blob(NEW, entry['path']) == blob(ACT, entry['path']))
    outputs.append({'path': entry['path'], 'C': identity(C, entry['path']), 'NEW': identity(NEW, entry['path']), 'ACT': identity(ACT, entry['path']), 'same_NEW_ACT_bytes': True})

streams = []
for entry in d['complete_unfiltered_streams']:
    data = git(*entry['command'][1:])
    name = Path(entry['path']).name
    (OUT / name).write_bytes(data)
    check(name + '/exact-packet-copy', data == blob(PACKET, entry['path']))
    check(name + '/full-hash-byte-count', len(data) == entry['bytes'] and digest(data) == entry['sha256'])
    parts = git('diff', '--no-renames', '--name-status', '-z', entry['from'], ACT).decode().split('\0')[:-1]
    statuses = [{'status': s, 'path': p} for s, p in zip(parts[::2], parts[1::2])]
    check(name + '/all-name-status', statuses == entry['complete_name_status'] and len(statuses) == entry['file_count'])
    blocks = re.split(rb'(?=^diff --git )', data, flags=re.M)[1:]
    check(name + '/all-top-level-blocks', len(blocks) == len(statuses))
    inventory = []
    for status, block in zip(statuses, blocks):
        path = status['path']
        record = {**status, **identity(ACT, path), 'block_bytes': len(block), 'block_sha256': digest(block),
                  'role': 'payload' if path in payload else 'public-registration' if path in [x['path'] for x in d['public_pending_registration']] else 'copied-evidence-or-private-preparation-or-G-metadata'}
        if path.endswith('.json'):
            obj = load(ACT, path)
            record['full_JSON_parsed'] = True
            record['top_level_keys'] = list(obj)
        inventory.append(record)
    streams.append({'from': entry['from'], 'to': ACT, 'command': entry['command'], 'unfiltered': True,
                    'bytes': len(data), 'sha256': digest(data), 'file_count': len(statuses), 'inventory': inventory})

ct, nt, at, pt = tree(C), tree(NEW), tree(ACT), tree(PACKET)
administrative = d['administrative_predecessor']
adt = tree(administrative)
public_paths = [x['path'] for x in d['public_pending_registration']]
changed_C = [p for p, v in ct.items() if at.get(p) != v]
changed_NEW = [p for p, v in nt.items() if at.get(p) != v]
check('preservation/C-existing-only-eleven-and-three', set(changed_C) == set(payload + public_paths) and len(changed_C) == 14)
check('preservation/NEW-existing-only-public-three', set(changed_NEW) == set(public_paths))
check('preservation/no-existing-deletion', set(ct) <= set(at) and set(nt) <= set(at))
check('G/ordinary-parent-is-administrative-predecessor', git('rev-parse', ACT + '^').decode().strip() == administrative)
check('preservation/all-administrative-existing-outside-eleven-and-three', all(at.get(p) == value for p, value in adt.items() if p not in payload + public_paths))
check('management/does-not-change-ACT-existing-paths', all(pt.get(p) == v for p, v in at.items()))
copies = load(ACT, PREFIX + 'integration-stage-1/published-artifact-copies.json')
for entry in copies['copied_artifacts']:
    data = verify(entry['source'], 'copy/source/' + entry['target'])
    check('copy/ACT-byte-and-mode/' + entry['target'], data == blob(ACT, entry['target']) and at[entry['target']].split()[0] == entry['mode'])
check('copy/all-161', len(copies['copied_artifacts']) == 161 and copies['author_candidate_files'] == 113 and copies['FULL_report_files'] == 9 and copies['affected_report_files'] == 39)
candidate_gates = load(ACT, PREFIX + 'integration-stage-1/candidate-gate-receipts.json')
candidate_owner_records = []
for owner in candidate_gates['owners']:
    verdict = json.loads(verify(owner['receipt'], 'candidate-gate/source/' + owner['owner']))
    check('candidate-gate/exact-copied-target-and-scope/' + owner['owner'], verdict['owner'] == owner['owner'] and verdict['reviewed_commit'] == NEW and verdict['reviewed_tree'] == d['reviewed_candidate_NEW_tree'] and verdict['verdict'] == owner['candidate_verdict'] and not verdict['blockers'] and owner['actual_verdict'] is None and blob(ACT, owner['receipt']['path']) == blob(owner['receipt']['commit'], owner['receipt']['path']))
    candidate_owner_records.append({'owner': owner['owner'], 'candidate_verdict': verdict['verdict'], 'reviewed_NEW': NEW, 'receipt': owner['receipt'], 'actual_verdict': None})
check('candidate-gate/14-with-nine-PASS-five-NA-no-ACT-signature', len(candidate_owner_records) == 14 and sum(x['candidate_verdict'] == 'PASS_SCOPED' for x in candidate_owner_records) == 9 and sum(x['candidate_verdict'] == 'NOT_AFFECTED' for x in candidate_owner_records) == 5)
for path in set(at) - set(nt):
    if path.startswith(PUBLIC + 'batches/B17/preparation-dispatch-after-B13-C-1/') or path.startswith(PUBLIC + 'batches/B18/preparation-dispatch-after-B13-C-1/') or path.startswith(PREFIX + 'refreeze-after-B13-C-1/'):
        source = CONTROL_PACKET if path.startswith(PREFIX + 'refreeze-after-B13-C-1/') else administrative
        check('administrative-copy/exact-frozen/' + path, blob(ACT, path) == blob(source, path))

controls = json.loads(verify(d['complete_control_bindings']['whole_original_approved_current_controls'], 'controls/full-original-approved-current'))
effective = json.loads(verify(d['complete_control_bindings']['whole_effective_constraints'], 'controls/full-twelve-effective'))
g = json.loads(verify(d['G_registration'], 'G/records'))
entries = d['per_ID_actual_entrances']
check('coverage/all-24-20', len(entries) == len(controls['controls']) == len(g['records']) == 24 and sum(x['primary'] for x in entries) == 20)
check('controls/twelve-entire-effective-unchanged', effective['full_exact_values'] == prior_meta['effective_cases'] and len(effective['full_exact_values']) == 12)
registration = []
for i, (entry, c, gr, oldproof, candidate) in enumerate(zip(entries, controls['controls'], g['records'], prior_meta['controls'], prior['per_ID_results'])):
    check(c['id'] + '/order-and-primary', entry['id'] == c['id'] == gr['id'] == candidate['id'] and entry['primary'] == c['primary'] == gr['primary'] == candidate['primary'])
    check(c['id'] + '/complete-original-approved-reused', digest(canonical(c['whole_original_object'])) == oldproof['original_object_sha256'] and digest(canonical(c['whole_approved_acceptance_object'])) == oldproof['approved_object_sha256'])
    check(c['id'] + '/entire-current-fields-G-and-prior', gr['complete_current_control_fields'] == c['complete_current_control_fields'] and digest(canonical(c['complete_current_control_fields'])) == oldproof['complete_fields_canonical_sha256'])
    check(c['id'] + '/bindings-preserved', gr['whole_original_object_binding'] == c['whole_original_object_binding'] and gr['whole_approved_acceptance_binding'] == c['whole_approved_acceptance_binding'] and gr['whole_original_object_sha256'] == c['whole_original_object_sha256'] and gr['whole_acceptance_object_sha256'] == c['whole_acceptance_object_sha256'])
    check(c['id'] + '/not-accepted-not-actual-approved', gr['canonical_state'] == 'OPEN' and gr['accepted_B16_contributions'] == 0 and gr['actual_full_and_affected_receipts'] is None and not gr['final_closure'])
    check(c['id'] + '/candidate-minimum-primary-only', gr['candidate_primary_minimum_satisfied'] == gr['primary'] and gr['candidate_FULL_disposition'] == candidate['verdict'])
    check(c['id'] + '/scope-and-candidate-pointer', gr['candidate_scope_and_minimum'] == candidate['scope'] and gr['candidate_FULL_record']['pointer'] == '/per_ID_results/' + str(i) and gr['candidate_FULL_record']['commit'] == CANDIDATE_REPORT)
    check(c['id'] + '/nonlocal-contributors-exact', gr['all_contributors'] == c['all_contributor_batches'] and gr['accepted_contributors'] == c['accepted_contributors'] and gr['remaining_contributors'] == c['pending_contributors'])
    for locus in entry['exact_ACT_formal_locators']:
        verify(locus['binding'], c['id'] + '/actual-body/' + locus['path'])
        check(c['id'] + '/body-line/' + str(locus['line']), locus['heading'] in blob(ACT, locus['path']).decode().splitlines()[locus['line'] - 1])
    catalog = entry['exact_ACT_catalog']
    verify(catalog['binding'], c['id'] + '/actual-catalog')
    row = blob(ACT, catalog['path']).decode().splitlines()[catalog['line'] - 1]
    check(c['id'] + '/actual-row-ID', row.startswith('| ' + catalog['id'] + ' |'))
    registration.append({'id': c['id'], 'primary': c['primary'], 'G_pointer': '/records/' + str(i),
                         'complete_control_canonical_sha256': digest(canonical(c)),
                         'current_fields_canonical_sha256': digest(canonical(c['complete_current_control_fields'])),
                         'actual_catalog': catalog, 'actual_catalog_row': row,
                         'all_contributors': gr['all_contributors'], 'accepted_contributors': gr['accepted_contributors'],
                         'pending_contributors': gr['remaining_contributors'], 'candidate_record': gr['candidate_FULL_record'],
                         'actual_receipts_at_ACT': None, 'accepted_B16_at_ACT': 0, 'canonical_at_ACT': 'OPEN'})

external = load(PACKET, PREFIX + 'actual-freeze-1/public-registration-actual-binding.json')
check('public/external-binding-exact-ACT', external['ACT'] == ACT and external['ACT_tree'] == d['reviewed_ACT_tree'] and not external['C'])
public_rows = {}
for path in public_paths[:2]:
    before, after = blob(C, path), blob(ACT, path)
    check('public/raw-240-prefix/' + path, after.startswith(before))
    old = list(csv.DictReader(io.StringIO(before.decode()), delimiter='\t'))
    rows = list(csv.DictReader(io.StringIO(after.decode()), delimiter='\t'))
    check('public/240-plus-24/' + path, len(old) == 240 and len(rows) == 264 and rows[:240] == old)
    for i, (row, gr, bound) in enumerate(zip(rows[240:], g['records'], external['records'])):
        obligations = json.loads(row['remaining_obligations'])
        check('public/' + Path(path).name + '/' + gr['id'] + '/identity-pending', row['finding_id'] == gr['id'] and row['canonical_state'] == 'OPEN' and row['candidate_commit'] == NEW and row['candidate_review_commit'] == CANDIDATE_REPORT and 'PENDING' in row.get('integration_gate', row.get('integration_verdict', '')))
        check('public/' + Path(path).name + '/' + gr['id'] + '/all-nonlocal-obligations', obligations['record_key'] == gr['record_key'] and obligations['all_contributors'] == gr['all_contributors'] and obligations['accepted_contributors'] == gr['accepted_contributors'] and obligations['remaining_contributors'] == gr['remaining_contributors'] and obligations['C'] == 'NOT_PERFORMED' and obligations['canonical_final_closure'] == 'NOT_PERFORMED')
        check('public/' + Path(path).name + '/' + gr['id'] + '/ACT-placeholder-external-resolved', bound['id'] == gr['id'] and bound['record_key'] == gr['record_key'] and bound['actual_commit_external_binding'] == ACT and bound['actual_tree'] == d['reviewed_ACT_tree'] and bound['actual_review_receipts'] is None and bound['accepted_B16_contributions'] == 0)
    public_rows[path] = {'C': identity(C, path), 'ACT': identity(ACT, path), 'physical_records': len(rows),
                         'accepted_old_raw_prefix_records': len(old), 'new_pending_records': rows[240:]}
final_path = public_paths[2]
check('public/old-final-review-whole-suffix', blob(ACT, final_path).endswith(blob(C, final_path)))
stats_path = PUBLIC + 'batches/B13/acceptance-stage-1/completion-statistics-successor.json'
ledger_path = PUBLIC + 'finding-ledger.tsv'
check('accepted/full-statistics-byte-preserved', blob(C, stats_path) == blob(ACT, stats_path))
check('canonical/full-ledger-byte-preserved', blob(C, ledger_path) == blob(ACT, ledger_path))
canonical_rows = list(csv.DictReader(io.StringIO(blob(ACT, ledger_path).decode()), delimiter='\t'))
check('canonical/229-OPEN-zero-CLOSED', len(canonical_rows) == 229 and all(row['canonical_state'] == 'OPEN' for row in canonical_rows))
check('accepted/240-version-matched-owned-proof', len(prior_meta['accepted240']) == len({(x['batch'], x['id']) for x in prior_meta['accepted240']}) == 240 and all(x['verdict'] == 'PASS_SCOPED' for x in prior_meta['accepted240']))
manifest = load(ACT, PREFIX + 'integration-stage-1/integration-manifest.json')
check('G/no-C-no-premature-downstream-release', manifest['accepted_batches'] == 15 and manifest['accepted_contributions'] == 240 and manifest['new_pending_contributions'] == 24 and manifest['canonical_OPEN'] == 229 and manifest['canonical_CLOSED'] == 0 and manifest['B17_B18_formal_held_until_B16_C'] and not manifest['C'])
scope = load(ACT, PREFIX + 'integration-stage-1/original-scope-application.json')
for record in scope['records']:
    data = verify(record['exact_current_scope_after'], 'scope/exact-current-after/' + record['path'])
    check('scope/ACT-authorized-after/' + record['path'], data == blob(ACT, record['path']) == blob(NEW, record['path']))
check('scope/no-new-scope-no-saved-execution', not scope['new_scope_amendment_by_G'] and not scope['saved_author_patch_programs_reexecuted'] and scope['scope_permission_not_independent_quality'])
limits = json.loads(verify(d['inherited_source_limits'], 'ACT/inherited-limits'))
verify(limits['inherited_complete_candidate_source_limits'], 'limits/full-candidate-value')
verify(limits['complete_contract_limits'], 'limits/full-contract-value')
source_proofs = []
for proof in prior_meta['source_proofs']:
    current = identity(REF, proof['path'], reference=True)
    check('source/exact-fixed-reuse/' + proof['path'], all(current[k] == proof[k] for k in ('git_blob', 'sha256', 'bytes')))
    for r in proof['ranges']:
        a, b = map(int, r['lines'].split('-')) if 'lines' in r else (r['start'], r['end'])
        data = b''.join(blob(REF, proof['path'], True).splitlines(keepends=True)[a - 1:b])
        check('source/range-identity/' + proof['path'], len(data) == r['bytes'] and digest(data) == r['sha256'])
    source_proofs.append({**proof, 'actual_method': 'Own exact candidate source semantics reused after full actual delta. Fresh hash/range identity read only; no new reference semantic reread or execution.'})
check('source/fixed-reference-tree', git('rev-parse', REF + '^{tree}', reference=True).decode().strip() == d['reference']['tree'])
catalog_path = payload[0]
check('catalog/full-NEW-body-preserved', blob(NEW, catalog_path) == blob(ACT, catalog_path))
check('C003/correct-target-capped-row', '上限50对照实际20来源26目标50' in blob(ACT, catalog_path).decode().splitlines()[589])
for path in ('deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md', 'specs/ui/wp66-b-storage-and-pokedex-ui.md'):
    check('C120/correct-complete-clause/' + path, blob(ACT, path).decode().splitlines()[216] == blob(NEW, path).decode().splitlines()[216])

failed = [x for x in checks if not x['pass']]
result = {'role': 'Original independent FULL exact ACT fresh metadata verification only', 'reviewed_ACT': ACT,
          'reviewed_ACT_tree': d['reviewed_ACT_tree'], 'C': C, 'NEW': NEW, 'packet_read_only': PACKET,
          'candidate_evidence_report': CANDIDATE_REPORT, 'checks': checks, 'check_count': len(checks), 'failed_checks': failed,
          'inputs': inputs, 'complete_unfiltered_streams': streams, 'outputs': outputs,
          'protection': {'C_existing_paths': len(ct), 'C_changed_existing_paths': changed_C,
                         'C_mode_type_blob_protected_other_paths': len(ct) - len(changed_C),
                         'NEW_existing_paths': len(nt), 'NEW_changed_existing_paths': changed_NEW,
                         'NEW_mode_type_blob_protected_other_paths': len(nt) - len(changed_NEW),
                         'ACT_added_paths_from_C': len(set(at) - set(ct)), 'ACT_added_paths_from_NEW': len(set(at) - set(nt)),
                         'accepted240_frozen_statistics': identity(ACT, stats_path), 'canonical_ledger': identity(ACT, ledger_path),
                         'old_catalog_protection_reused': prior_meta['protection']['old_catalog'],
                         'public_old_raw_prefixes_and_old_review_suffix': True, 'B16_pending': 24, 'accepted_batches': 15,
                         'accepted_contributions': 240, 'canonical_OPEN': 229, 'canonical_CLOSED': 0},
          'actual_registration_per_ID': registration, 'complete_12_effective_constraints': effective['full_exact_values'],
          'public_records': public_rows, 'published_artifact_copies': copies, 'source_proofs': source_proofs,
          'candidate_owner_prerequisites_only': candidate_owner_records,
          'accepted240': prior_meta['accepted240'], 'historical_programs_executed': False,
          'reference_game_Ruby_behavior_vectors_executed': False, 'runtime_observations': 0, 'proven_Demo_chains': 0,
          'metadata_is_not_ACT_quality_PASS': True}
(OUT / 'metadata-verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'checks': len(checks), 'failed': failed,
                  'streams': [{k: x[k] for k in ('from', 'bytes', 'sha256', 'file_count')} for x in streams],
                  'C_protected_existing_other': len(ct) - len(changed_C),
                  'NEW_protected_existing_other': len(nt) - len(changed_NEW)}, ensure_ascii=False))
raise SystemExit(bool(failed))
