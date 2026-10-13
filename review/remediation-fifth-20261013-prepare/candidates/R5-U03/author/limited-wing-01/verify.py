#!/usr/bin/env python3
"""Verify a bounded document delta; no reference, model, or host behavior runs."""
import difflib
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=ROOT, text=True).strip())
REL = ROOT.relative_to(REPO).as_posix()
BASE = 'd84bf0dd0eac4605c98d8ba4ae3f8502117fc5a7'
PROPOSAL = '9fab9d7d2995cf0402920f3bf94d8473579e31b8'
ACTUAL_REVIEW = '1eda123e3bcd4b1aa99e2ba57c6de02d56414716'
PROPOSAL_ROOT = 'review/remediation-fifth-20261013-prepare/integration/R5-U03/limited-revision-proposal-01/'
REVIEW_ROOT = 'review/remediation-fifth-20261013-prepare/reviews/R5-U03/actual/round-01/'
TARGET = 'deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md'

def blob(ref, path):
    return subprocess.check_output(['git', 'show', ref + ':' + path], cwd=REPO)

def old(path):
    return blob(BASE, REL + '/' + path)

def current(path):
    return (ROOT / path).read_bytes()

def identity(raw):
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
                git_blob=hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest())

def project(data):
    baseline = {p: blob(data['base_commit'], p).decode() for p in {o['target_path'] for o in data['operations']}}
    projected = dict(baseline)
    for op in data['operations']:
        p = op['target_path']
        assert identity(baseline[p].encode())['git_blob'] == op['B5_anchor']['git_blob']
        if op['operation'] == 'append':
            projected[p] += op['new_text']
        else:
            assert projected[p].count(op['old_text']) == 1, op['label']
            projected[p] = projected[p].replace(op['old_text'], op['new_text'], 1)
    return baseline, projected

def patch_check(baseline, projected, patch):
    with tempfile.TemporaryDirectory(prefix='u03-wing-prose-') as td:
        d = Path(td)
        for p, text in baseline.items():
            q = d / p
            q.parent.mkdir(parents=True, exist_ok=True)
            q.write_text(text)
        patch_path = d / 'input.patch'
        patch_path.write_bytes(patch)
        subprocess.run(['git', 'apply', '--check', str(patch_path)], cwd=d, check=True, capture_output=True)
        subprocess.run(['git', 'apply', str(patch_path)], cwd=d, check=True, capture_output=True)
        assert all((d / p).read_text() == text for p, text in projected.items())

def validate(check_manifest=True):
    proposal = json.loads(blob(PROPOSAL, PROPOSAL_ROOT + 'author-revision-proposal.json'))
    change = proposal['proposed_formal_change']
    assert change['path'] == TARGET
    v0 = json.loads(old('static-vectors.json'))
    v1 = json.loads(current('static-vectors.json'))
    assert len(v0['vectors']) == len(v1['vectors']) == 69
    assert {k: v for k, v in v0.items() if k != 'vectors'} == {k: v for k, v in v1.items() if k != 'vectors'}
    assert v0['vectors'][45] == proposal['author_sync_edits'][0]['old_value']
    assert v1['vectors'][45] == proposal['author_sync_edits'][0]['proposed_value']
    assert [i for i, (a, b) in enumerate(zip(v0['vectors'], v1['vectors'])) if a != b] == [45]
    assert {k: v for k, v in v0['vectors'][45].items() if k != 'input'} == {k: v for k, v in v1['vectors'][45].items() if k != 'input'}
    assert all(v['execution_status'] == 'NOT_EXECUTED' and v['evidence_level'] == 'DERIVED_VECTOR' for v in v1['vectors'])
    o0 = json.loads(old('operations.json'))
    o1 = json.loads(current('operations.json'))
    assert len(o0['operations']) == len(o1['operations']) == 52
    assert {k: v for k, v in o0.items() if k != 'operations'} == {k: v for k, v in o1.items() if k != 'operations'}
    assert [i for i, (a, b) in enumerate(zip(o0['operations'], o1['operations'])) if a != b] == [49]
    a, b = o0['operations'][49], o1['operations'][49]
    assert a['target_path'] == b['target_path'] == TARGET and a['label'] == b['label'] == 'R5U03-vectors'
    assert {k: v for k, v in a.items() if k != 'new_text'} == {k: v for k, v in b.items() if k != 'new_text'}
    assert a['new_text'].count(change['old_input']) == 1
    assert b['new_text'] == a['new_text'].replace(change['old_input'], change['new_input'], 1)
    baseline, p0 = project(o0)
    baseline1, p1 = project(o1)
    assert baseline == baseline1 and len(p0) == len(p1) == 16
    assert [p for p in p0 if p0[p] != p1[p]] == [TARGET]
    assert p1[TARGET] == p0[TARGET].replace(change['old_input'], change['new_input'], 1)
    assert identity(p1[TARGET].encode()) == {k: change['new_identity_after_author_approval'][k] for k in ['bytes', 'sha256', 'git_blob']}
    assert current('formal/' + TARGET) == p1[TARGET].encode()
    assert blob(change['old_actual_commit'], TARGET) == p0[TARGET].encode()
    rows0 = [(p, s) for p, text in p0.items() if '/test-catalog/' in p for s in text.splitlines() if s.startswith('| R5U03-')]
    rows1 = [(p, s) for p, text in p1.items() if '/test-catalog/' in p for s in text.splitlines() if s.startswith('| R5U03-')]
    assert len(rows0) == len(rows1) == 81
    assert [(a, b) for a, b in zip(rows0, rows1) if a != b] == [((TARGET, change['old_row'].rstrip('\n')), (TARGET, change['new_row'].rstrip('\n')))]
    delta = ''.join(difflib.unified_diff(p0[TARGET].splitlines(keepends=True), p1[TARGET].splitlines(keepends=True), fromfile='a/' + TARGET, tofile='b/' + TARGET)).encode()
    assert delta == current('limited-wing-01/formal-diff.patch') == blob(PROPOSAL, PROPOSAL_ROOT + 'proposed-formal-diff.patch')
    cumulative = ''.join(''.join(difflib.unified_diff(baseline[p].splitlines(keepends=True), p1[p].splitlines(keepends=True), fromfile='a/' + p, tofile='b/' + p)) for p in sorted(p1)).encode()
    assert cumulative == current('formal-diff.patch')
    patch_check(baseline, p0, old('formal-diff.patch'))
    patch_check(baseline, p1, cumulative)
    patch_check(p0, p1, delta)
    assert current('fragment-manifest.json') == old('fragment-manifest.json')
    fragments = json.loads(current('fragment-manifest.json'))['fragments']
    assert len(fragments) == 31
    previous_manifest = json.loads(old('candidate-manifest.json'))
    required_changed = {'static-vectors.json', 'operations.json', 'formal/' + TARGET, 'formal-diff.patch', 'candidate-manifest.json'}
    old_files = [p for p in subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE, '--', REL], cwd=REPO, text=True).splitlines()]
    assert len(old_files) == 33
    changed_old = []
    for p in old_files:
        name = p[len(REL) + 1:]
        if current(name) != old(name):
            changed_old.append(name)
    assert set(changed_old) == required_changed
    assert current('finding-responses.json') == old('finding-responses.json')
    assert len(json.loads(current('finding-responses.json'))['findings']) == 11
    criteria_raw = blob(ACTUAL_REVIEW, REVIEW_ROOT + 'criterion-results.json')
    assert hashlib.sha256(criteria_raw).hexdigest() == '48ce3aba76cba99e44b0cf0023e01214de623287719a5097acfe4f6305947201'
    criteria = json.loads(criteria_raw)
    assert criteria['explicit_static_criteria']['count'] == 60 and criteria['explicit_static_criteria']['PASS'] == 59 and criteria['explicit_static_criteria']['FAIL'] == 1
    assert len(criteria['scoped_PASS_findings']) == 10
    assert criteria['findings'][8]['finding_id'] == 'GR5-M05-004' and criteria['findings'][8]['actual_verdict'] == 'FAIL'
    assert criteria['gates']['U01_required_upstream'] == 'SATISFIED_EXACT_U01_OWNER_SCOPE_AT_7bd8102'
    response = json.loads(current('limited-wing-01/response.json'))
    assert [r['finding_id'] for r in response['finding_status']] == previous_manifest['required_ids']
    assert len(response['unchanged_prior_static_PASS']) == 59
    for i, record in enumerate(response['finding_status']):
        assert record['prior_actual_pointer'] == '/findings/' + str(i)
        assert record['prior_actual_verdict'] == criteria['findings'][i]['actual_verdict']
        assert record['current_independent_recheck'] == ('WAIT_ORIGINAL_REVIEWER' if i == 8 else 'REUSE_EXACT_UNCHANGED_SCOPE_ONLY')
    assert response['new_reference_model_host_execution'] == 0 and not response['self_signature']
    if check_manifest:
        manifest = json.loads(current('candidate-manifest.json'))
        names = sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p.name != 'candidate-manifest.json')
        assert sorted(x['path'] for x in manifest['artifacts']) == names
        for artifact in manifest['artifacts']:
            assert identity(current(artifact['path'])) == {k: artifact[k] for k in ['bytes', 'sha256', 'git_blob']}, artifact['path']
        for receiver in manifest['synchronized_receivers']:
            assert identity(p1[receiver['target_path']].encode()) == receiver['projected_B5_replay_identity']
        assert manifest['limited_wing_01']['supersedes_current_validation_for'] == 'GR5-M05-004/static/04'
    return dict(schema='r5.u03.wing-limited-tool-validation.v1', evidence_level='TOOL_VALIDATION', status='PASS',
                author_base_commit=BASE, bounded_vector_index=45, changed_vector_fields=['input'], vector_count=69,
                unchanged_vector_objects=68, operation_count=52, changed_operation_index=49, unchanged_operation_objects=51,
                catalogue_row_count=81, unchanged_catalogue_rows=80, projected_files=16, unchanged_projected_files=15,
                fragments_unchanged=31, preserved_existing_payload_files=28, changed_existing_payload_files=5,
                prior_actual_scope_PASS_reused=10, prior_static_PASS_reused=59, prior_static_FAIL_retained=1,
                cumulative_old_and_new_patch_replay='PASS', one_row_incremental_patch_replay='PASS',
                expected_and_premises_unchanged=True, old_two_advisory_MISMATCH='RETAINED_NOT_CERTIFIED',
                U01_upstream='SATISFIED_EXACT_OWNER_SCOPE_7bd8102', U03_independent_recheck='WAIT_ORIGINAL_REVIEWER',
                actual02_frozen=False, new_reference_model_host_execution=0, formal_acceptance=0, CLOSED=0, public_registration=0,
                actual_model_echo='UNVERIFIED', self_signature=False)

if __name__ == '__main__':
    print(json.dumps(validate(), ensure_ascii=False, indent=2))
