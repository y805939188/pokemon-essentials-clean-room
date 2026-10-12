"""Independent document/object validation only. Executes no reference or model."""
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
PACK = '08a57fb55118914a74ac1ffaf617647c01df8938'
BASE = '1f36475d22120a0d1175967d5b17d71fe8311d88'
CAND = 'db879d9034acf2fa3a3721ad3b94614827922ec4'
AUTHOR = 'c1e5c8a780426aef1611a5b139375de15e6cd468'
PUB = '2b60c7bd0dce8d972e34a9d86a8f6cf6a3b1dd65'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
R_GIT = Path('/workspace/r4-u01-reference.git')
TASK = 'review/remediation-fourth-20261012-prepare/tasks/R4-U01/'
AUTHOR_ROOT = 'review/remediation-fourth-20261012-prepare/batches/R4-U01/author/'
REPORT_ROOT = 'review/global-independent-review/fourth-2026-10-12-1f36475-c92e/'


def git(*args, reference=False):
    prefix = ['git', '--git-dir=' + str(R_GIT)] if reference else ['git', '-C', str(ROOT)]
    return subprocess.check_output(prefix + list(args))


def read(commit, path, reference=False):
    return git('show', commit + ':' + path, reference=reference)


def decoded(commit, path):
    return json.loads(read(commit, path))


def ident(commit, path, reference=False):
    data = read(commit, path, reference)
    return {'commit': commit, 'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': git('rev-parse', commit + ':' + path, reference=reference).decode().strip()}


def verify(expected, commit, path, reference=False):
    observed = ident(commit, path, reference)
    for key in ('bytes', 'sha256', 'git_blob'):
        assert expected[key] == observed[key], (commit, path, key)
    return observed


contract = decoded(PACK, TASK + 'batch-contract.json')
formal = contract['allowed_formal_write_paths']
scope = decoded(PACK, TASK + 'read-scope.json')
trees = {}
for c, expected, reference in [
    (BASE, 'd696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a', False),
    (PACK, '8fc388710e3433890416f6d01247fd09df9d2ea8', False),
    (CAND, 'f47c43195a60b8edb2922f40d38582874a675cc5', False),
    (R, '7589c800b61ba13a13040ed0d686979b80a84fd0', True),
]:
    observed = git('rev-parse', c + '^{tree}', reference=reference).decode().strip()
    assert observed == expected, (c, observed)
    trees[c] = observed
trees[AUTHOR] = git('rev-parse', AUTHOR + '^{tree}').decode().strip()
assert git('rev-parse', CAND + '^').decode().strip() == PACK
assert git('rev-parse', AUTHOR + '^').decode().strip() == CAND
assert git('diff', '--name-only', BASE, PACK, '--', 'deliverables/final-specification-set') == b''
changed = git('diff', '--name-only', PACK, CAND).decode().splitlines()
assert set(p for p in changed if not p.startswith(AUTHOR_ROOT)) == set(formal)
assert len(changed) == 11
assert git('diff', '--name-only', CAND, AUTHOR).decode().splitlines() == [AUTHOR_ROOT + 'candidate-publication.json']
assert git('diff', '--binary', PACK, CAND, '--', *formal) == read(CAND, AUTHOR_ROOT + 'formal-diff.patch')
raw_diff_check = subprocess.run(['git', '-C', str(ROOT), 'diff', '--check', PACK, CAND],
                                capture_output=True, text=True)
assert raw_diff_check.returncode in (0, 2)
assert all(line.startswith(AUTHOR_ROOT + 'formal-diff.patch:')
           for line in raw_diff_check.stdout.splitlines() if line and not line.startswith('+'))
git('diff', '--check', PACK, CAND, '--', *formal)

all_formal = git('ls-tree', '-r', '--name-only', BASE, 'deliverables/final-specification-set').decode().splitlines()
assert len(all_formal) == 131
unchanged = [p for p in all_formal if p not in formal]
assert all(read(BASE, p) == read(CAND, p) for p in unchanged)
formal_ids = decoded(CAND, AUTHOR_ROOT + 'formal-file-identities.json')
formal_verified = []
for item in formal_ids['files']:
    expected = item['candidate_bytes']
    path = expected['path']
    formal_verified.append(verify(expected, CAND, path))
    data = read(CAND, path)
    assert data == (ROOT / path).read_bytes()
    text = data.decode('utf-8')
    assert b'\r' not in data and data.endswith(b'\n')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            assert (ROOT / path).parent.joinpath(target.split('#')[0]).exists(), (path, target)
assert {x['path'] for x in formal_verified} == set(formal)

catalog = formal[-1]
def rows(commit):
    matches = re.findall(r'^\| ([A-Z][A-Z0-9-]*\d+) \|.*$', read(commit, catalog).decode(), re.M)
    lines = re.findall(r'^\| [A-Z][A-Z0-9-]*\d+ \|.*$', read(commit, catalog).decode(), re.M)
    assert len(matches) == len(set(matches))
    return dict(zip(matches, lines))
before, after = rows(BASE), rows(CAND)
assert len(before) == 121
assert all(after[k] == v for k, v in before.items())
new = {f'TM{i:02}' for i in range(15, 24)} | {f'IO{i:02}' for i in range(16, 21)} | {f'LZ{i:02}' for i in range(26, 36)}
assert set(after) - set(before) == new and len(new) == 24

author_validation = decoded(CAND, AUTHOR_ROOT + 'validation-result.json')
def section(commit, path, heading):
    text = read(commit, path).decode()
    start = text.index(heading)
    level = len(heading.split(' ')[0])
    following = re.search(r'^#{1,' + str(level) + r'} ', text[start + len(heading):], re.M)
    end = start + len(heading) + following.start() if following else len(text)
    return text[start:end].strip()
preserved_sections = author_validation['preserved_sections']
assert len(preserved_sections) == 27
for item in preserved_sections:
    assert section(BASE, item['path'], item['section']) == section(CAND, item['path'], item['section']), item

source_anchors = [verify(x['identity'], R, x['path'], True) for x in scope['source']]
spec_anchors = [verify(x['identity'], BASE, x['path']) for x in scope['formal_anchors']]
author_reads = decoded(CAND, AUTHOR_ROOT + 'input-and-read-evidence.json')
source_claims = [verify(x, R, x['path'], True) for x in author_reads['source_read']]
historical_claims = [verify(x, x['commit'], x['path']) for x in author_reads['historical_probes_read_not_run']]
assert author_reads['new_reference_execution'] == author_reads['new_model_execution'] == author_reads['new_host_or_demo_execution'] == 0
assert author_reads['historical_fourth_review_reference_execution_records'] == 4
pack_records = decoded(PACK, TASK + 'findings-input.json')['canonical_root_records']
root_records = decoded('130452d902530140331c21064a3188b7887f72ae', REPORT_ROOT + 'findings.json')['findings']
root_by_id = {x['id']: x for x in root_records}
assert all(f == root_by_id[f['id']] for f in pack_records)
mapping = decoded(CAND, AUTHOR_ROOT + 'acceptance-and-regression.json')
assert [x['finding'] for x in mapping['records']] == contract['finding_ids']
assert not mapping['accepted_or_closed_registered']
for x in mapping['records']:
    for criterion in x['criteria']:
        assert criterion['independent_verdict'] == 'PENDING_PARENT_REVIEWER'
        assert set(criterion['vectors']) <= set(after)

freeze = decoded(PUB, 'review/remediation-fourth-20261012-prepare/freeze-and-publication.json')
assert freeze['author_start_commit'] == PACK and freeze['task_package_tree'] == trees[PACK]
assert freeze['formal_input_commit'] == BASE and freeze['reference_commit'] == R
for x in freeze['task_pack_readback']['file_identities']:
    if x['path'].startswith(TASK) or x['path'].endswith(('resource-scope.json', 'input-verification.json', 'dispatch-plan.json')):
        verify(x, PACK, x['path'])

nav = decoded(PACK, TASK + 'legacy-navigation.json')
legacy_verified = []
for group in ('selected_original229', 'selected_exact341'):
    for record in nav[group]:
        binding = record.get('immutable_scope', record.get('qualified_scope_binding'))
        file_id = binding['file_identity']
        verified = verify(file_id, file_id['commit'], file_id['path'])
        obj = decoded(file_id['commit'], file_id['path'])
        for token in binding['pointer'].strip('/').split('/'):
            obj = obj[int(token)] if isinstance(obj, list) else obj[token]
        h = hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        assert h == binding['object_sha256']
        author_scope = next(x for x in author_reads['bounded_legacy_scopes_read'] if x['group'] == group)
        assert obj == author_scope['qualified_scope']
        legacy_verified.append({'group': group, 'id': record.get('id', record.get('record_key')),
                                'exact_tuple': record.get('exact_tuple'), 'file': verified,
                                'pointer': binding['pointer'], 'qualified_scope_sha256': h,
                                'execution_status': 'not_reexecuted', 'scope_expanded': False})

result = {
    'batch': 'R4-U01', 'status': 'PASS_TOOL_VALIDATION', 'evidence_level': 'TOOL_VALIDATION',
    'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'commit_trees': trees, 'candidate_changed_paths': changed,
    'four_formal_file_identities': formal_verified, 'unchanged_formal_file_count': len(unchanged),
    'existing_vector_rows_retained_verbatim': len(before), 'new_static_vector_ids': sorted(new),
    'existing_sections_independently_compared': preserved_sections,
    'read_scope_source_anchor_checks': source_anchors, 'read_scope_spec_anchor_checks': spec_anchors,
    'author_claimed_source_identities_checked': source_claims,
    'historical_receipt_identities_checked_not_run': historical_claims,
    'root_findings_equal_frozen_task_records': True, 'freeze_receipt_binding_verified': True,
    'author_formal_diff_equal_actual_diff': True, 'legacy_exact_scopes_verified': legacy_verified,
    'formal_diff_check': 'PASS',
    'whole_candidate_diff_check': {
        'exit_code': raw_diff_check.returncode,
        'diagnostic_count': sum(line.startswith(AUTHOR_ROOT) for line in raw_diff_check.stdout.splitlines()),
        'interpretation': 'Only required single-space blank context lines inside the exact saved patch; no formal-file whitespace defect and no revision requested.'},
    'new_reference_execution': 0, 'new_model_execution': 0, 'new_host_or_demo_execution': 0,
    'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE',
    'historical_fourth_review_reference_execution_records': 4,
    'limitations': 'Document/object checks do not replace the independent semantic review or grant actual/host/runtime acceptance.'
}
(OUT / 'validation-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'formal_files': len(formal_verified),
                  'unchanged_formal': len(unchanged), 'old_rows': len(before), 'new_vectors': len(new),
                  'source_anchors': len(source_anchors), 'legacy_scopes': len(legacy_verified)}, ensure_ascii=False))
