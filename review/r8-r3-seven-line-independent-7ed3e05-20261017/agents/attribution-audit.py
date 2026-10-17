import ast
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path('/workspace/r8-r3-seven-line-review')
OUT = ROOT / 'review/r8-r3-seven-line-independent-7ed3e05-20261017/agents'
BASE = 'planning/implementation-routing/r8-20261017/'
CANDIDATE = '7ed3e0554ac24339a7e61cab152f628037111644'
PARENT = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
CURRENT = '5f87743293290de2e219ecdd6c19e88280f60c9a'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
PRIOR = '34202eb7accfee48bb8761db88b340bd77f54a42'
PRIOR_DIR = 'review/r8-disposition-r3-independent-c0f62d9-20261017/'
PRIOR_PHYSICAL = pathlib.Path('/workspace/r8-disposition-r3-review')
IDS = ['FR-000173', 'FR-000227', 'FR-000596']


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def show(commit, path):
    return git('show', commit + ':' + path)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(commit, path):
    return json.loads(show(commit, path))


def diff_values(old, new, pointer=''):
    if type(old) is not type(new):
        return [pointer]
    if isinstance(old, dict):
        return sum((diff_values(old[k], new[k], pointer + '/' + k)
                    if k in old and k in new else [pointer + '/' + k]
                    for k in sorted(set(old) | set(new))), [])
    if isinstance(old, list):
        if len(old) != len(new):
            return [pointer]
        return sum((diff_values(a, b, pointer + '/' + str(i))
                    for i, (a, b) in enumerate(zip(old, new))), [])
    return [] if old == new else [pointer]


old = load(PARENT, BASE + 'routing-manifest.json')
new = load(CANDIDATE, BASE + 'routing-manifest.json')
oldfs = {f['feature_id']: f for f in old['features']}
newfs = {f['feature_id']: f for f in new['features']}
changed = diff_values(old, new)
assert changed == [
    '/features/28/differences/1', '/features/31/differences/1',
    '/features/161/differences/1', '/features/192/differences/1',
    '/features/215/differences/1', '/features/433/differences/1',
    '/features/566/differences/1']

input_identities = []
for path in ['AGENTS.md', BASE + 'review-prompt.md',
             BASE + 'revisions/r3-calibration-repair/review-prompt.md',
             BASE + 'revisions/r3-calibration-repair/README.md',
             BASE + 'revisions/r3-calibration-repair/correction-record.json',
             BASE + 'revisions/r3-calibration-repair/repair-proof.json',
             BASE + 'revisions/r3-calibration-repair/command-io.json',
             BASE + 'revisions/r3-calibration-repair/manifest-from-c0.diff',
             BASE + 'routing-manifest.json',
             BASE + 'revisions/r3/feature-source-deltas.json',
             BASE + 'revisions/r3/source-file-reassessment.json',
             BASE + 'revisions/r3/source-refinement-patch.json',
             BASE + 'revisions/r3/facet-inheritance.json',
             BASE + 'revisions/r3/feature-resolution.json',
             BASE + 'revisions/r3/build-author-evidence.py',
             BASE + 'views/creature-rpg.md', BASE + 'views/pokemon-rules.md']:
    b = show(CANDIDATE, path)
    assert (ROOT / path).read_bytes() == b
    input_identities.append({'commit': CANDIDATE, 'path': path,
                             'git_blob': git('rev-parse', CANDIDATE + ':' + path).decode().strip(),
                             'bytes': len(b), 'sha256': sha(b), 'worktree_equals_fixed_git': True})

prior_identity = []
for name in ['REPORT.md', 'findings.json', 'feature-results.json',
             'agents/source-report.md', 'agents/creature-report.md',
             'agents/pokemon-world-report.md']:
    path = PRIOR_DIR + name
    b = show(PRIOR, path)
    assert (PRIOR_PHYSICAL / path).read_bytes() == b
    prior_identity.append({'commit': PRIOR, 'path': path, 'bytes': len(b),
                           'sha256': sha(b), 'physical_equals_fixed_git': True})

units = load(CANDIDATE, BASE + 'revisions/r3/feature-source-deltas.json')['records']
files = load(CANDIDATE, BASE + 'revisions/r3/source-file-reassessment.json')['records']
patch = load(CANDIDATE, BASE + 'revisions/r3/source-refinement-patch.json')['records']
facets = load(CANDIDATE, BASE + 'revisions/r3/facet-inheritance.json')['records']
resolution = load(CANDIDATE, BASE + 'revisions/r3/feature-resolution.json')['active_feature_results']
prior_result = load(PRIOR, PRIOR_DIR + 'feature-results.json')
findings = load(PRIOR, PRIOR_DIR + 'findings.json')
prior_cases = findings['findings'][0]['cases']

manual = None
unit_overrides = None
generator_path = BASE + 'revisions/r3/build-author-evidence.py'
for node in ast.parse(show(CANDIDATE, generator_path)).body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'manual' for t in node.targets):
        manual = ast.literal_eval(node.value)
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'unit_narratives' for t in node.targets):
        unit_overrides = ast.literal_eval(node.value)
assert manual is not None
assert unit_overrides is not None
assert show(CANDIDATE, generator_path).splitlines()[:6] == show(PARENT, generator_path).splitlines()[:6]

records = []
for feature_id in IDS:
    f = newfs[feature_id]
    idx = new['features'].index(f)
    assert diff_values(oldfs[feature_id], f) == ['/differences/1']
    path = f['source']['document']
    b = show(CURRENT, path)
    lines = b.decode().splitlines(keepends=True)
    ranges = f['functional_scope']['line_ranges']
    unit_bytes = ''.join(''.join(lines[a-1:z]) for a, z in ranges).encode()
    loc = f['current_applicability']['locator']
    assert sha(b) == loc['file_sha256']
    assert sha(unit_bytes) == loc['unit_sha256']
    assert git('rev-parse', CURRENT + ':' + path).decode().strip() == loc['file_git_blob']
    uidx, u = next((i, r) for i, r in enumerate(units) if r['feature_id'] == feature_id)
    didx, d = next((i, r) for i, r in enumerate(files) if r['document'] == path)
    pidx, p = next((i, r) for i, r in enumerate(patch) if r['feature_id'] == feature_id)
    assert u['current_source'] == {'commit': CURRENT, 'document': path, **loc}
    assert u['source_fact_delta'] == d['source_fact_reassessment'] == manual[path.split('/')[-1]][0]
    assert unit_overrides.get(feature_id, manual[path.split('/')[-1]][0]) == u['source_fact_delta']
    assert u['future_boundary_reassessment'] == d['future_plan_reassessment'] == manual[path.split('/')[-1]][1]
    assert f['differences'][1].startswith(u['source_fact_delta'])
    changes = p['field_changes']
    after = next(c['after'] for c in changes if c['pointer'] == '/differences')
    assert after == f['differences']
    complete_patch = git('diff', '--no-ext-diff', '--unified=3', B8, CURRENT, '--', path)
    assert sha(complete_patch) == d['complete_diff_identity']['sha256']
    assert len(complete_patch) == d['complete_diff_identity']['bytes']
    facet_idx, facet = next((i, r) for i, r in enumerate(facets) if r['feature_id'] == feature_id)
    resolution_idx, res = next((i, r) for i, r in enumerate(resolution) if r['feature_id'] == feature_id)
    for r in [facet, res]:
        assert r['current_calibration_repair']['received_facet_verdict'] == 'FAIL'
        assert r['current_calibration_repair']['received_other_four_facets'] == 'PASS'
        assert r['current_calibration_repair']['author_status'] == 'CORRECTED_AWAITING_INDEPENDENT_REVIEW'
        assert r['whole_feature_or_compatibility_PASS_granted_by_author'] is False
    view = 'views/pokemon-rules.md' if feature_id == 'FR-000596' else 'views/creature-rpg.md'
    before_line = next(s for s in show(PARENT, BASE + view).decode().splitlines() if s.startswith('| ' + feature_id + ' /'))
    new_lines = show(CANDIDATE, BASE + view).decode().splitlines()
    after_line = next(s for s in new_lines if s.startswith('| ' + feature_id + ' /'))
    assert after_line == before_line.replace(oldfs[feature_id]['differences'][1], f['differences'][1])
    prior_case = next(c for c in prior_cases if c['feature_id'] == feature_id)
    prior_feature = next(r for r in prior_result['active_feature_results'] if r['feature_id'] == feature_id)
    assert prior_feature['normalized_facets'] == {
        'classification': 'PASS', 'responsibility': 'PASS', 'scope': 'PASS',
        'dependency': 'PASS', 'current_calibration': 'FAIL'}
    assert prior_feature['functional_scope'] == f['functional_scope']
    assert prior_feature['current_applicability'] == f['current_applicability']
    assert prior_feature['fixed_source'] == f['source']
    assert prior_case['candidate_pointer'] == f'/features/{idx}/differences/1'
    assert prior_case['candidate_claim'] == oldfs[feature_id]['differences'][1]
    assert prior_case['source_identity'] == loc
    records.append({'feature_id': feature_id, 'candidate_pointer': f'/features/{idx}/differences/1',
                    'document': path, 'current_source': {'commit': CURRENT, **loc},
                    'full_b8_to_5f_patch_bytes': len(complete_patch),
                    'full_b8_to_5f_patch_sha256': sha(complete_patch),
                    'changed_hunks': [s for s in complete_patch.decode().splitlines() if s.startswith('@@')],
                    'source_unit_record': uidx, 'source_file_record': didx, 'patch_record': pidx,
                    'facet_record': facet_idx, 'resolution_record': resolution_idx,
                    'view_path': BASE + view, 'view_line': new_lines.index(after_line) + 1,
                    'view_exact_old_row_with_only_narrative_replacement': True,
                    'all_non_narrative_manifest_fields_equal_to_prior_candidate': True,
                    'generator_file_and_unit_facts_consistent': True,
                    'old_finding_case_and_source_identity_match_fixed_prior': True,
                    'fixed_prior_four_PASS_facets_and_full_source_scope_current_identity_matched': True,
                    'source_and_unit_hashes_independently_recomputed': True})

wp36 = newfs['FR-000227']['source']['document']
old36 = show(B8, wp36).decode().splitlines(keepends=True)
new36 = show(CURRENT, wp36).decode().splitlines(keepends=True)
assert old36[139:146] == new36[139:146]
assert oldfs['FR-000244'] == newfs['FR-000244']
assert oldfs['FR-000762'] == newfs['FR-000762']

io = load(CANDIDATE, BASE + 'revisions/r3-calibration-repair/command-io.json')
io_summary = []
for c in io['unchanged_ten_command_suite']['commands'] + io['commands']:
    io_summary.append({k: c[k] for k in ['argv', 'started_utc', 'ended_utc', 'exit_code']})

evidence = {'candidate_commit': CANDIDATE, 'parent_candidate_commit': PARENT,
            'current_source_commit': CURRENT, 'baseline_source_commit': B8,
            'fixed_prior_review_commit': PRIOR,
            'manifest_changed_pointers': changed,
            'input_identities': input_identities, 'fixed_prior_identities': prior_identity,
            'allocated_feature_checks': records,
            'retained_controls': {'FR-000244_entire_manifest_record_unchanged': True,
                                  'FR-000762_entire_manifest_record_unchanged': True,
                                  'WP36_4_3_L140_146_equal_B8_and_5f': True,
                                  'historical_writer_first_six_lines_equal_parent': True},
            'author_command_io_parsed_only_not_replayed_by_this_agent': io_summary,
            'all_allocated_structural_checks_passed': True}
(OUT / 'attribution-evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'all_allocated_structural_checks_passed': True,
                  'features': IDS, 'manifest_changed_leaves': len(changed),
                  'input_identities': len(input_identities), 'prior_identities': len(prior_identity)}, indent=2))
