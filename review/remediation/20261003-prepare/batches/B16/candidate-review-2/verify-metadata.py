#!/usr/bin/env python3
"""Fresh incremental Git/text/JSON metadata checks. No behavioral execution."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
PREFIX = 'review/remediation/20261003-prepare/batches/B16/'
OLD = 'ae223d7bfb9ff6ed8a1ac153debb986115345957'
NEW = '356b46b320884e57e71a1cab8413e13594524a7d'
PUB = '7585b16a65338392af8ff78e7d8a8cb23cd19901'
BASE = '27185563f307e16d2612fa86e83b2c9bd772c79e'
PRIOR = '458f4f207266154021340c09d949f7863c358df2'
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


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':')).encode()


def check(name, passed, detail=None):
    checks.append({'check': name, 'pass': bool(passed), 'detail': detail})


def identity(commit, path, reference=False):
    data = blob(commit, path, reference)
    return {'commit': commit, 'path': path,
            'git_blob': git('rev-parse', commit + ':' + path,
                            reference=reference).decode().strip(),
            'bytes': len(data), 'sha256': sha(data)}


def verify(binding, label):
    actual = identity(binding['commit'], binding['path'])
    check(label, all(actual[k] == binding[k]
                     for k in ('git_blob', 'bytes', 'sha256') if k in binding))
    inputs.append({'label': label, **actual})
    return blob(binding['commit'], binding['path'])


def load(commit, path):
    return json.loads(blob(commit, path))


def tree(commit):
    result = {}
    for entry in git('ls-tree', '-r', '-z', commit).split(b'\0'):
        if entry:
            meta, path = entry.split(b'\t', 1)
            result[path.decode()] = meta.decode()
    return result


dispatch = load(PUB, PREFIX + 'author-draft-1/original-sync-4/incremental-review-dispatch.json')
prior_manifest = load(PRIOR, PREFIX + 'candidate-review-1/artifact-manifest.json')
for entry in prior_manifest['files']:
    verify({'commit': PRIOR, **entry}, 'prior-report/' + entry['path'])
prior = load(PRIOR, PREFIX + 'candidate-review-1/review.json')
prior_meta = load(PRIOR, PREFIX + 'candidate-review-1/metadata-verification.json')
for key, value in dispatch.items():
    if isinstance(value, dict) and all(k in value for k in ('commit', 'path', 'git_blob', 'sha256', 'bytes')):
        verify(value, 'dispatch/' + key)
check('identity/OLD', git('rev-parse', OLD + '^{tree}').decode().strip() == dispatch['OLD_tree'])
check('identity/NEW', git('rev-parse', NEW + '^{tree}').decode().strip() == dispatch['NEW_tree'])
check('identity/BASE', git('rev-parse', BASE + '^{tree}').decode().strip() == dispatch['formal_input_tree'])
check('identity/publication-parent', git('rev-parse', PUB + '^').decode().strip() == NEW)
check('identity/AGENTS', blob(OLD, 'AGENTS.md') == blob(NEW, 'AGENTS.md') == blob(PUB, 'AGENTS.md'))
check('identity/prior-reviewed-OLD', prior['reviewed_commit'] == OLD and prior['reviewed_tree'] == dispatch['OLD_tree'])
check('reuse/prior-checks-valid', prior_meta['check_count'] == 586 and not prior_meta['failed_checks'] and all(x['pass'] for x in prior_meta['checks']))

controls = json.loads(verify(dispatch['whole_original_approved_current_controls'], 'complete-controls'))
effective = json.loads(verify(dispatch['whole_effective_constraints'], 'complete-effective'))
check('controls/all-24-20', len(controls['controls']) == 24 and sum(c['primary'] for c in controls['controls']) == 20)
check('controls/exact-ordered-IDs', [c['id'] for c in controls['controls']] == dispatch['contribution_ids'] == [c['id'] for c in prior['per_ID_results']])
check('controls/exact-primary', [c['id'] for c in controls['controls'] if c['primary']] == dispatch['primary_ids'])
control_reuse = []
for c, oldproof in zip(controls['controls'], prior_meta['controls']):
    original_hash = sha(canonical(c['whole_original_object']))
    approved_hash = sha(canonical(c['whole_approved_acceptance_object']))
    current_hash = sha(canonical(c['complete_current_control_fields']))
    check(c['id'] + '/complete-original-unchanged', original_hash == c['whole_original_object_sha256'] == oldproof['original_object_sha256'])
    check(c['id'] + '/complete-approved-unchanged', approved_hash == c['whole_acceptance_object_sha256'] == oldproof['approved_object_sha256'])
    check(c['id'] + '/all-current-fields-unchanged', current_hash == oldproof['complete_fields_canonical_sha256'])
    control_reuse.append({**oldproof, 'reused_from_report': PRIOR,
                          'whole_control_complete_canonical_sha256': sha(canonical(c)),
                          'NEW_controls_identical': True})
check('effective/full-12-unchanged', effective['full_exact_values'] == prior_meta['effective_cases'] and len(effective['full_exact_values']) == 12)

payload = [x['path'] for x in dispatch['current_payload_outputs']]
check('payload/eleven', len(payload) == 11 and len(set(payload)) == 11)
outputs = []
for entry in dispatch['current_payload_outputs']:
    p = entry['path']
    verify(entry['FIX_BASE_before'], 'payload/BASE/' + p)
    verify(entry['reviewed_OLD_before'], 'payload/OLD/' + p)
    after = identity(NEW, p)
    check('payload/NEW/' + p, all(after[k] == entry['after'][k] for k in ('git_blob', 'bytes', 'sha256')))
    check('payload/preserved-declaration/' + p, (blob(OLD, p) == blob(NEW, p)) == entry['unchanged_from_reviewed_OLD'])
    outputs.append({'path': p, 'kind': entry['kind'], 'before_OLD': identity(OLD, p), 'after_NEW': after,
                    'unchanged_from_OLD': blob(OLD, p) == blob(NEW, p)})

streams = {}
for label, start in [('OLD_to_NEW', OLD), ('FIX_BASE_to_NEW', BASE)]:
    data = git('diff', '--binary', start, NEW)
    (OUT / ('complete-' + label.replace('_to_', '-to-') + '.diff')).write_bytes(data)
    claimed = dispatch['complete_unfiltered_streams'][label]
    check(label + '/exact-publication-copy', data == blob(PUB, claimed['path']))
    check(label + '/full-bytes-hash', len(data) == claimed['bytes'] and sha(data) == claimed['sha256'])
    names = git('diff', '--name-only', '-z', start, NEW).decode().split('\0')[:-1]
    check(label + '/full-path-list', names == claimed['changed_paths'])
    blocks = re.split(rb'(?=^diff --git )', data, flags=re.M)[1:]
    check(label + '/all-top-level-blocks', len(blocks) == len(names))
    inventory = []
    for path, block in zip(names, blocks):
        record = {**identity(NEW, path), 'diff_block_bytes': len(block), 'diff_block_sha256': sha(block),
                  'role': 'payload' if path in payload else 'B16-own-evidence',
                  'hunks': re.findall(r'^@@.*$', block.decode(), re.M)}
        if path.endswith('.json'):
            doc = load(NEW, path)
            record['complete_JSON_parsed'] = True
            record['top_level_keys'] = list(doc)
        if label == 'OLD_to_NEW':
            check('delta/path-authorized/' + path, path in payload or path.startswith(PREFIX + 'author-draft-1/') or path.startswith(PREFIX + 'candidate-1/'))
        inventory.append(record)
    streams[label] = {'command': ['git', 'diff', '--binary', start, NEW], 'bytes': len(data),
                      'sha256': sha(data), 'unfiltered': True, 'file_count': len(names), 'inventory': inventory}

oldtree, newtree, basetree = tree(OLD), tree(NEW), tree(BASE)
changed_old = [p for p in oldtree if oldtree[p] != newtree.get(p)]
protection = json.loads(verify(dispatch['protection'], 'protection/author-binding'))
check('protection/all-OLD-existing', len(oldtree) == 36417 and changed_old == protection['OLD_existing_paths_changed'])
check('protection/36414-mode-type-blob', len(oldtree) - len(changed_old) == 36414)
check('protection/old-no-deletion', set(oldtree) <= set(newtree))
check('protection/BASE-existing-outside-11', all(newtree.get(p) == v for p, v in basetree.items() if p not in payload))
check('protection/8-other-output-bytes', sum(x['unchanged_from_OLD'] for x in outputs) == 8)
pubtree = tree(PUB)
check('protection/publication-existing-same-candidate', all(pubtree.get(p) == v for p, v in newtree.items()))
catalog = payload[0]
needle = b'\xe4\xb8\x8a\xe9\x99\x9050\xe5\xaf\xb9\xe7\x85\xa7\xe5\xae\x9e\xe9\x99\x8520\xe6\x9d\xa5\xe6\xba\x9030\xe7\x9b\xae\xe6\xa0\x8750'
fixed = needle.replace(b'30', b'26')
check('C003/exact-whole-catalog-only-replacement', blob(OLD, catalog).count(needle) == 1 and blob(OLD, catalog).replace(needle, fixed) == blob(NEW, catalog))
line_changes = []
for p in changed_old:
    a, b = blob(OLD, p).decode().splitlines(), blob(NEW, p).decode().splitlines()
    differences = [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y]
    check('delta/single-line/' + p, len(a) == len(b) and len(differences) == 1)
    line_changes.append({'path': p, 'line': differences[0], 'before': a[differences[0] - 1], 'after': b[differences[0] - 1]})
check('delta/exact-590-217-217', [x['line'] for x in line_changes] == [590, 217, 217])
body_changes = line_changes[1:]
check('C120/original-sanitized-wallpaper-identical', body_changes[0]['after'].split('另有查看盒子的背景刷新写入：')[1] == body_changes[1]['after'].split('另有查看盒子的背景刷新写入：')[1])
for x in body_changes:
    check('C120/non-wallpaper-prefix-suffix-retained/' + x['path'], x['before'].split('另有查看盒子的背景刷新写入：')[0] == x['after'].split('另有查看盒子的背景刷新写入：')[0] and x['before'].split('盒号5（零基）')[1] == x['after'].split('盒号5（零基）')[1])

scope = json.loads(verify(dispatch['scope4_receipt'], 'scope4/permission-only'))
check('scope4/one-file-one-clause', scope['grant_file_count'] == scope['grant_control_count'] == scope['grant_replacement_count'] == 1)
grant = scope['granted_files'][0]
before = verify(grant['before_artifact'], 'scope4/before-snapshot')
check('scope4/before-is-OLD', before == blob(OLD, grant['path']))
patch = verify(grant['whole_combined_patch'], 'scope4/whole-patch').decode().splitlines(keepends=True)
after = verify(grant['complete_proposed_after'], 'scope4/whole-after')
lines = before.decode().splitlines(keepends=True)
cursor, result, hunk_count = 0, [], 0
i = 0
while i < len(patch):
    if not patch[i].startswith('@@ '):
        i += 1
        continue
    match = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', patch[i])
    start = int(match[1]) - 1
    result.extend(lines[cursor:start])
    cursor = start
    hunk_count += 1
    i += 1
    while i < len(patch) and not patch[i].startswith('@@ '):
        sign, text = patch[i][0], patch[i][1:]
        if sign in ' -':
            assert lines[cursor] == text
            cursor += 1
        if sign in ' +':
            result.append(text)
        i += 1
result.extend(lines[cursor:])
check('scope4/fresh-in-memory-single-application', hunk_count == 1 and ''.join(result).encode() == after == blob(NEW, grant['path']))

manifest = json.loads(verify(dispatch['candidate_manifest'], 'NEW/complete-manifest'))
trace = json.loads(verify(dispatch['traceability_completion'], 'NEW/complete-trace'))
check('NEW/manifest-24-20', manifest['contribution_ids'] == dispatch['contribution_ids'] and manifest['primary_ids'] == dispatch['primary_ids'])
check('NEW/manifest-all-eleven-output-paths', [e['path'] for e in manifest['outputs']] == payload)
for entry in manifest['outputs']:
    actual = identity(NEW, entry['path'])
    check('NEW/manifest-output/' + entry['path'], all(actual[k] == entry['after'][k] for k in ('git_blob', 'sha256', 'bytes')))
check('NEW/trace-24-20', [r['id'] for r in trace['rows']] == dispatch['contribution_ids'] and sum(r['primary'] for r in trace['rows']) == 20)
for row, c in zip(trace['rows'], controls['controls']):
    check(row['id'] + '/trace-original-approved-binding', row['whole_original_object'] == c['whole_original_object_binding'] and row['whole_approved_acceptance_object'] == c['whole_approved_acceptance_binding'])
current_C003 = trace['rows'][10]['corrected_C003_evidence']['catalog']
check('C003/current-trace-row', current_C003['full_static_row'] == blob(NEW, catalog).decode().splitlines()[589])
row_edits = load(NEW, PREFIX + 'author-draft-1/remediation-R-B16-F01-1/catalog-row-edits.json')
catalog_preservation = load(NEW, PREFIX + 'author-draft-1/remediation-R-B16-F01-1/catalog-preservation.json')
for index, row in enumerate(catalog_preservation['added_rows']):
    check('NEW/catalog-preservation-row/' + str(index), row['text'] in blob(NEW, catalog).decode().splitlines())
check('C003/current-row-edit-expected', row_edits['new_rows'][10]['expected_static'] in current_C003['full_static_row'])
for entry in trace['current_original_whole_results']:
    actual = identity(NEW, entry['path'])
    check('NEW/current-original-whole-result/' + entry['path'], all(actual[k] == entry['after'][k] for k in ('git_blob', 'sha256', 'bytes')))
for key in ('C120_current_sanitized_clause', 'C120_original_current_clause'):
    locus = trace['rows'][16][key]
    check('C120/current-trace/' + key, locus['text'] == blob(NEW, locus['path']).decode().splitlines()[locus['line'] - 1])
hunks = json.loads(verify(dispatch['current_complete_hunks'], 'NEW/complete-original-sanitized-hunks'))
for edit in hunks['edits'] + hunks['current_original_payload_hunks']:
    actual = git('diff', BASE, NEW, '--', edit['path']).decode()
    check('NEW/full-hunk/' + edit['path'], actual.rstrip('\n') == edit['complete_baseline_to_final_text_hunks'].rstrip('\n'))

receipt_path = 'review/remediation/20261003-prepare/batches/B13/acceptance-stage-1/completion-statistics-successor.json'
receipt = blob(BASE, receipt_path)
check('accepted240/full-frozen-file', receipt == blob(OLD, receipt_path) == blob(NEW, receipt_path))
check('accepted240/full-unique-records-reused', len(prior_meta['accepted240']) == len({(r['batch'], r['id']) for r in prior_meta['accepted240']}) == 240 and all(r['verdict'] == 'PASS_SCOPED' for r in prior_meta['accepted240']))
source_limits = json.loads(verify(dispatch['source_limits'], 'NEW/exact-source-limits'))
prior_limits_identity = identity(**prior['retained_source_limits']['binding'])
check('limits/same-byte-identity-as-original-FULL', all(dispatch['source_limits'][k] == prior_limits_identity[k] for k in ('git_blob', 'sha256', 'bytes')))
check('limits/complete-inherited-values-retained', source_limits['complete_inherited_limits'] == prior['retained_source_limits']['complete_inherited_limits'])
sources = []
for e in prior['blockers'][0]['direct_evidence']:
    actual = identity(REF, e['path'], reference=True)
    check('source/C003-exact-prior/' + e['path'], all(actual[k] == e[k] for k in ('git_blob', 'sha256', 'bytes')))
    lines = blob(REF, e['path'], True).splitlines(keepends=True)
    for r in e['ranges']:
        a, b = map(int, r['lines'].split('-'))
        data = b''.join(lines[a - 1:b])
        check('source/C003-range/' + r['lines'], len(data) == r['bytes'] and sha(data) == r['sha256'])
    sources.append({**actual, 'ranges': e['ranges'], 'method': 'Version-matched own prior static source proof reused; no behavioral execution.'})
source_addition = load(NEW, PREFIX + 'author-draft-1/remediation-C120-1/source-reading-supplement.json')
for e in source_addition['ranges']:
    actual = identity(REF, e['path'], reference=True)
    check('source/C120-fixed-blob/' + e['path'], all(actual[k] == e[k] for k in ('git_blob', 'sha256', 'bytes')))
    r = e['range']
    data = b''.join(blob(REF, e['path'], True).splitlines(keepends=True)[r['start'] - 1:r['end']])
    check('source/C120-bounded-range/' + e['path'], len(data) == r['bytes'] and sha(data) == r['sha256'])
    sources.append({**actual, 'ranges': [r], 'method': 'Independent bounded static source inspection; no Ruby/game/vector execution.'})
wp25 = verify(source_addition['accepted_WP25'], 'C120/accepted-WP25')
check('C120/accepted-WP25-full-preserved', wp25 == blob(OLD, source_addition['accepted_WP25']['path']) == blob(NEW, source_addition['accepted_WP25']['path']))
check('sources/fixed-reference-tree', git('rev-parse', REF + '^{tree}', reference=True).decode().strip() == dispatch['read_only_static_reference']['tree'])
for name in ('affected-review-dispatch.json', 'affected-review-dispatch.md', 'full-review-dispatch.json', 'full-review-dispatch.md', 'publication-receipt.json'):
    path = PREFIX + 'author-draft-1/original-sync-3/' + name
    check('reuse/previous-publication-evidence/' + name, blob(NEW, path) == blob('5c70c6945ede498f1d7d59592da1d37a96c07a98', path))

failed = [c for c in checks if not c['pass']]
record = {'role': 'Independent FULL24/20 fresh incremental metadata verification only',
          'reviewed_OLD': OLD, 'reviewed_NEW': NEW, 'reviewed_NEW_tree': dispatch['NEW_tree'],
          'publication_read_only': PUB, 'FIX_BASE': BASE, 'prior_FULL_report': PRIOR,
          'check_count': len(checks), 'failed_checks': failed, 'checks': checks, 'inputs': inputs,
          'complete_unfiltered_streams': streams, 'outputs': outputs, 'controls': control_reuse,
          'effective_cases': effective['full_exact_values'], 'exact_three_line_changes': line_changes,
          'protection': {'OLD_existing_paths': len(oldtree), 'OLD_changed_existing_paths': changed_old,
                         'OLD_identical_other_mode_type_blob': len(oldtree) - len(changed_old),
                         'NEW_added_paths': len(set(newtree) - set(oldtree)), 'eight_other_outputs_exact': True,
                         'BASE_outside_11_exact': True, 'old_catalog': prior_meta['catalog'],
                         'catalog_only_single_C003_replacement': True,
                         'scope3_27_other_replacements_and_every_other_original_byte_preserved': True,
                         'scope4_exact_after_independent_one_application': True},
          'accepted240': prior_meta['accepted240'], 'accepted240_frozen_file': identity(NEW, receipt_path),
          'source_proofs': sources, 'accepted_WP25': identity(NEW, source_addition['accepted_WP25']['path']),
          'execution_boundary': {'reference_game_Ruby': False, 'behavior_vectors': False,
                                 'historical_programs': False, 'fresh_metadata_checks': True,
                                 'runtime_observations': 0, 'proven_Demo_chains': 0},
          'metadata_is_not_quality_PASS': True}
(OUT / 'metadata-verification.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'checks': len(checks), 'failed': failed,
                  'streams': {k: {a: v[a] for a in ('bytes', 'sha256', 'file_count')} for k, v in streams.items()},
                  'OLD_existing_protected': len(oldtree) - len(changed_old)}, ensure_ascii=False))
raise SystemExit(bool(failed))
