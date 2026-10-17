#!/usr/bin/env python3
"""Static identity/propagation audit for the four EV recovery cases only."""
import ast
import copy
import hashlib
import json
import pathlib
import subprocess

REPO = pathlib.Path('/workspace/r8-r3-seven-line-review')
OUT = REPO / 'review/r8-r3-seven-line-independent-7ed3e05-20261017/agents'
P = 'planning/implementation-routing/r8-20261017/'
C = '7ed3e0554ac24339a7e61cab152f628037111644'
OLD = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
CUR = '5f87743293290de2e219ecdd6c19e88280f60c9a'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
PRIOR = '34202eb7accfee48bb8761db88b340bd77f54a42'
PR = 'review/r8-disposition-r3-independent-c0f62d9-20261017/'
IDS = ['FR-000029', 'FR-000032', 'FR-000204', 'FR-000456']
inputs = []

def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def read(commit, path):
    data = git('show', commit + ':' + path)
    identity = {'commit': commit, 'path': path, 'bytes': len(data),
                'sha256': sha(data), 'git_blob': git('rev-parse', commit + ':' + path).decode().strip()}
    if identity not in inputs:
        inputs.append(identity)
    return data

def obj(commit, path):
    return json.loads(read(commit, path))

def changes(a, b, path=''):
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        if set(a) != set(b):
            return [path]
        return sum((changes(a[k], b[k], path + '/' + k) for k in a), [])
    if isinstance(a, list):
        if len(a) != len(b):
            return [path]
        return sum((changes(x, y, path + '/' + str(i)) for i, (x, y) in enumerate(zip(a, b))), [])
    return [] if a == b else [path]

manifest = obj(C, P + 'routing-manifest.json')
before = obj(OLD, P + 'routing-manifest.json')
features = {x['feature_id']: x for x in manifest['features']}
old_features = {x['feature_id']: x for x in before['features']}
prior_results = obj(PRIOR, PR + 'feature-results.json')
prior_features = {x['feature_id']: x for x in prior_results['active_feature_results']}
prior_findings = obj(PRIOR, PR + 'findings.json')
prior_ev = next(x for x in prior_findings['findings'] if x['id'] == 'R3-EV-BOUNDARY-001')
assert [x['feature_id'] for x in prior_ev['cases']] == IDS
deltas = obj(C, P + 'revisions/r3/feature-source-deltas.json')
files = obj(C, P + 'revisions/r3/source-file-reassessment.json')
patch = obj(C, P + 'revisions/r3/source-refinement-patch.json')
old_patch = obj(OLD, P + 'revisions/r3/source-refinement-patch.json')
resolution = obj(C, P + 'revisions/r3/feature-resolution.json')
facets = obj(C, P + 'revisions/r3/facet-inheritance.json')
correction = obj(C, P + 'revisions/r3-calibration-repair/correction-record.json')
for path in ['revisions/r3-calibration-repair/repair-proof.json',
             'revisions/r3-calibration-repair/command-io.json',
             'revisions/r3/tools/actual-command-io.json',
             'revisions/r3-calibration-repair/README.md',
             'revisions/r3-calibration-repair/review-prompt.md',
             'review-prompt.md', 'revisions/r3-calibration-repair/manifest-from-c0.diff']:
    read(C, P + path)
generator_bytes = read(C, P + 'revisions/r3/build-author-evidence.py')
old_generator = read(OLD, P + 'revisions/r3/build-author-evidence.py')
assert generator_bytes.splitlines(keepends=True)[:6] == old_generator.splitlines(keepends=True)[:6]
literal_dicts = {}
for node in ast.parse(generator_bytes).body:
    if isinstance(node, ast.Assign):
        try:
            value = ast.literal_eval(node.value)
        except (ValueError, TypeError):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and isinstance(value, dict):
                literal_dicts[target.id] = value
allowed = {'/features/' + str(i) + '/differences/1' for i, x in enumerate(manifest['features'])
           if x['feature_id'] in IDS + ['FR-000173', 'FR-000227', 'FR-000596']}
assert set(changes(before, manifest)) == allowed
evidence = []
readset = []
for fid in IDS:
    f = features[fid]
    i = manifest['features'].index(f)
    assert changes(old_features[fid], f) == ['/differences/1']
    assert prior_features[fid]['normalized_facets'] == {
        'classification': 'PASS', 'responsibility': 'PASS', 'scope': 'PASS',
        'dependency': 'PASS', 'current_calibration': 'FAIL'}
    loc = f['current_applicability']['locator']
    doc = f['source']['document']
    raw = read(CUR, doc)
    ls = raw.decode().splitlines(keepends=True)
    effective = ''.join(''.join(ls[a - 1:b]) for a, b in loc['line_ranges']).encode()
    assert sha(effective) == loc['unit_sha256']
    assert sha(raw) == loc['file_sha256']
    assert git('rev-parse', CUR + ':' + doc).decode().strip() == loc['file_git_blob']
    assert prior_features[fid]['current_applicability'] == f['current_applicability']
    baseline = read(B8, doc)
    assert sha(baseline) == f['source']['file_sha256']
    dr_i, dr = next((i, x) for i, x in enumerate(deltas['records']) if x['feature_id'] == fid)
    fr_i, fr = next((i, x) for i, x in enumerate(files['records']) if x['document'] == doc)
    pa_i, pa = next((i, x) for i, x in enumerate(patch['records']) if x['feature_id'] == fid)
    cor = next(x for x in correction['records'] if x['feature_id'] == fid)
    assert dr['immutable_source'] == f['source']
    assert dr['current_source'] == {'commit': CUR, 'document': doc, **loc}
    assert cor['after'] == f['differences'][1]
    assert cor['before'] == old_features[fid]['differences'][1]
    assert cor['fixed_source'] == dr['current_source']
    assert pa['current_source_evidence'] == dr['current_source']
    assert pa['field_changes'][0]['after'] == f['differences']
    old_pa = next(x for x in old_patch['records'] if x['feature_id'] == fid)
    assert changes(old_pa, pa) == ['/field_changes/0/after/1']
    assert dr['source_fact_delta'] in f['differences'][1]
    assert literal_dicts['manual'][pathlib.Path(doc).name] == (
        fr['source_fact_reassessment'], fr['future_plan_reassessment'])
    assert dr['future_boundary_reassessment'] == fr['future_plan_reassessment']
    if fid in ['FR-000029', 'FR-000032']:
        assert literal_dicts['unit_narratives'][fid] == dr['source_fact_delta']
        assert dr['source_fact_delta'] in fr['source_fact_reassessment']
    else:
        assert dr['source_fact_delta'] == fr['source_fact_reassessment']
    view = {'FR-000029': 'combat-requirements', 'FR-000032': 'combat-requirements',
            'FR-000204': 'creature-rpg', 'FR-000456': 'pokemon-rules'}[fid]
    view_path = P + 'views/' + view + '.md'
    vls = read(C, view_path).decode().splitlines()
    view_i, view_row = next((i, x) for i, x in enumerate(vls, 1) if x.startswith('| ' + fid + ' /'))
    assert f['differences'][1] in view_row
    assert old_features[fid]['differences'][1] not in view_row
    rr = next(x for x in resolution['active_feature_results'] if x['feature_id'] == fid)
    fa = next(x for x in facets['records'] if x['feature_id'] == fid)
    repair = {'fixed_review': PRIOR, 'received_facet_verdict': 'FAIL',
              'received_other_four_facets': 'PASS', 'finding_id': 'R3-EV-BOUNDARY-001',
              'author_status': 'CORRECTED_AWAITING_INDEPENDENT_REVIEW',
              'evidence': '../r3-calibration-repair/correction-record.json#' + fid}
    assert rr['current_calibration_repair'] == fa['current_calibration_repair'] == repair
    assert rr['whole_feature_or_compatibility_PASS_granted_by_author'] is False
    assert f['destination_verification']['status'] == '待验证'
    assert f['future_plan']['stage_approval'] == '未批准'
    assert f['implementation'] == {'status': '未实现', 'acceptance_status': '未验收', 'evidence': []}
    evidence.append({'feature_id': fid, 'candidate_pointer': '/features/' + str(i) + '/differences/1',
                     'source_effective_proof': {'commit': CUR, 'document': doc, **loc},
                     'changed_manifest_fields': ['/differences/1'],
                     'source_unit_pointer': '/records/' + str(dr_i),
                     'source_file_pointer': '/records/' + str(fr_i),
                     'patch_pointer': '/records/' + str(pa_i) + '/field_changes/0/after/1',
                     'view': {'path': view_path, 'line': view_i},
                     'dependency_feature_refs': f['dependencies']['feature_refs'],
                     'all_non_narrative_feature_fields_identical_to_parent': True,
                     'current_source_same_as_fixed_prior_review': True,
                     'source_unit_and_file_fact_and_future_boundary_coherent': True,
                     'patch_generator_facet_resolution_and_view_coherent': True})
    readset.append('CURRENT ' + fid + ' ' + doc + '\n' + '\n'.join(
        str(j) + ': ' + ls[j - 1].rstrip('\n') for a, b in loc['line_ranges'] for j in range(a, b + 1)))

docs = sorted({features[x]['source']['document'] for x in IDS})
diffs = []
for doc in docs:
    data = git('diff', B8, CUR, '--', doc)
    diffs.append(data)
    inputs.append({'old_commit': B8, 'new_commit': CUR, 'path': doc,
                   'reading': 'FRESH_COMPLETE_PER_FILE_DIFF', 'bytes': len(data), 'sha256': sha(data)})
for fid in ['FR-000487', 'FR-000681', 'FR-000739', 'FR-000754', 'FR-000755']:
    f = features[fid]
    raw = read(CUR, f['source']['document']).decode().splitlines()
    ranges = f['current_applicability']['locator']['line_ranges']
    readset.append('CONSUMER ' + fid + '\n' + '\n'.join(
        str(j) + ': ' + raw[j - 1] for a, b in ranges for j in range(a, b + 1)))
for name, a, b in [('combat-requirements-wp39-40-41-42-45.md', 299, 317),
                   ('pokemon-rules-wp19-21-22-23-34.md', 344, 356)]:
    doc = 'deliverables/final-specification-set/test-catalog/' + name
    raw = read(CUR, doc).decode().splitlines()
    readset.append('CATALOG ' + doc + '\n' + '\n'.join(str(j) + ': ' + raw[j - 1] for j in range(a, b + 1)))
assert git('diff', '--name-only', C).decode() == ''
(OUT / 'ev-effective-readset.txt').write_text('\n\n'.join(readset) + '\n')
(OUT / 'ev-three-file-B8-to-5f.diff').write_bytes(b''.join(diffs))
result = {'schema': 'r3-seven-line-ev-static-evidence.v1', 'candidate_commit': C,
          'exact_parent_commit': OLD, 'current_source_commit': CUR, 'fixed_prior_review_commit': PRIOR,
          'all_checks_passed': True, 'manifest_changed_pointers': sorted(allowed),
          'feature_evidence': evidence, 'input_identities': inputs,
          'historical_writer_first_six_guard_lines_byte_preserved': True,
          'tracked_worktree_diff_empty': True, 'business_execution': False,
          'scope': 'Four EV recovery cases; identity checks do not substitute for semantic judgment.'}
(OUT / 'ev-static-evidence.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'all_checks_passed': True, 'four_cases': IDS, 'source_files': len(docs),
                  'input_identities': len(inputs), 'author_changes': 0}, ensure_ascii=False))
