"""Independent R4-U04 fixed-input integrity checks; no behavior execution."""
import hashlib
import json
import os
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/workspace/r4-u04-independent-review')
SOURCE = Path('/workspace/r4-u04-reference')
OUT = Path(__file__).resolve().parent
PREP = 'review/remediation-fourth-20261012-prepare/'
B = '1f36475d22120a0d1175967d5b17d71fe8311d88'
T = '08a57fb55118914a74ac1ffaf617647c01df8938'
C = '1c2cdcbe6509839a19fd3c48c8a412a6c19e161a'
E = '53edd67b69d3641de3d748ceb1bfeb847f621f6a'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
H = '130452d902530140331c21064a3188b7887f72ae'
P = '2b60c7bd0dce8d972e34a9d86a8f6cf6a3b1dd65'
REVIEW_ROOT = PREP + 'batches/R4-U04/review/'
AUTHOR_ROOT = PREP + 'batches/R4-U04/author/'


def git(*args, source=False):
    return subprocess.check_output(['git', '-C', str(SOURCE if source else ROOT), *args])


def read(commit, path, source=False):
    return git('show', commit + ':' + path, source=source)


def identity(commit, path, source=False):
    data = read(commit, path, source)
    return {'commit': commit, 'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': git('rev-parse', commit + ':' + path, source=source).decode().strip(),
            'full_bytes_loaded': True}


def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


started = datetime.now(timezone.utc).isoformat()
contract = json.loads(read(T, PREP + 'tasks/R4-U04/batch-contract.json'))
scope = json.loads(read(T, PREP + 'tasks/R4-U04/read-scope.json'))
finding_input = json.loads(read(T, PREP + 'tasks/R4-U04/findings-input.json'))
receipt_path = PREP + 'freeze-and-publication.json'
receipt = json.loads(read(P, receipt_path))
publication = json.loads(read(E, AUTHOR_ROOT + 'candidate-publication.json'))
allowed = set(contract['allowed_formal_write_paths'])
expected_trees = {B: 'd696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a',
                  T: '8fc388710e3433890416f6d01247fd09df9d2ea8',
                  C: 'fcd0cff8a0830b7e3a8860f8e84c55c5bb793ec3',
                  E: '69d4088db4c03b490d8e0dcd1a19b76dd91d86a1',
                  R: '7589c800b61ba13a13040ed0d686979b80a84fd0',
                  H: 'b2677e819a85422c353bd3eac3ff55409698d5d8'}
for commit, tree in expected_trees.items():
    assert git('rev-parse', commit + '^{tree}', source=commit == R).decode().strip() == tree
assert git('show', '-s', '--format=%P', C).decode().strip() == T
assert git('show', '-s', '--format=%P', E).decode().strip() == C
assert receipt['task_package_commit'] == receipt['author_start_commit'] == T
assert receipt['task_package_tree'] == expected_trees[T]
assert publication['candidate_commit'] == C and publication['candidate_tree'] == expected_trees[C]

input_paths = [PREP + 'tasks/R4-U04/' + f for f in
               ['reviewer.md', 'author.md', 'batch-contract.json', 'read-scope.json',
                'findings-input.json', 'handoff-findings.md', 'launch-contract.json', 'legacy-navigation.json']]
input_paths += [PREP + f for f in ['input-verification.json', 'resource-scope.json', 'dispatch-plan.json']]
receipt_files = {f['path']: f for f in receipt['task_pack_readback']['file_identities']}
task_ids = []
for path in input_paths:
    item = identity(T, path)
    assert all(item[k] == receipt_files[path][k] for k in ['bytes', 'sha256', 'git_blob'])
    assert read(T, path) == read(C, path) == read(E, path)
    if path.endswith('.json'):
        json.loads(read(T, path))
    task_ids.append(item)
canonical = json.loads(read(H, 'review/global-independent-review/fourth-2026-10-12-1f36475-c92e/findings.json'))
assert finding_input['canonical_root_records'][0] == next(f for f in canonical['findings'] if f['id'] == 'GR4-M05-001')

source_ids = []
for anchor in scope['source']:
    item = identity(R, anchor['path'], source=True)
    assert all(item[k] == v for k, v in anchor['identity'].items())
    source_ids.append(item)
supplemental_source = identity(R, 'Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb', source=True)
changes = git('diff', '--name-only', '-z', T, C).decode().strip('\0').split('\0')
assert len(changes) == 12
assert all(p in allowed or p.startswith(AUTHOR_ROOT) for p in changes)
assert set(git('diff', '--name-only', T, C, '--', 'deliverables').decode().splitlines()) == allowed
assert git('diff', '--name-only', C, E).decode().splitlines() == [AUTHOR_ROOT + 'candidate-publication.json']
git('diff', '--check', T, C)
candidate_ids = [identity(C, p) for p in changes]
claimed = {f['path']: f for f in publication['readback']['file_identities']}
for item in candidate_ids:
    assert all(item[k] == claimed[item['path']][k] for k in ['bytes', 'sha256', 'git_blob'])
    assert read(C, item['path']) == read(E, item['path'])
    if item['path'].endswith('.json'):
        json.loads(read(C, item['path']))

formal_paths = git('ls-tree', '-r', '--name-only', B, 'deliverables/final-specification-set').decode().splitlines()
assert len(formal_paths) == 131
for p in formal_paths:
    assert read(B, p) == read(T, p)
    if p not in allowed:
        assert read(B, p) == read(C, p) == read(E, p)
formal_before = [identity(B, p) for p in sorted(allowed)]
wp, cat = contract['allowed_formal_write_paths']
old, new = read(B, wp).decode(), read(C, wp).decode()
old_pp = old[old.index('### 5.2 PP 与 PP 成长'):old.index('### 5.3 EV 与培养')]
new_pp = new[new.index('### 5.2 PP 与 PP 成长'):new.index('### 5.3 EV 与培养')]
assert old_pp[old_pp.index('- PPUP/PPMAX：'):] == new_pp[new_pp.index('- PPUP/PPMAX：'):]
restored = new.replace(new_pp, old_pp, 1).replace(
    '| PP | ETHER/MAXETHER/ELIXIR/MAXELIXIR/LEPPABERRY |',
    '| PP | ETHER/MAXETHER/ELIXIR/MAXELIXIR/LEPPA |', 1)
assert restored.encode() == read(B, wp)
old, new = read(B, cat).decode(), read(C, cat).decode()
addition = new[new.index('### R4-U04 主动 PP 补给'):new.index('## SH：')]
old_iu = next(l for l in old.splitlines() if l.startswith('| IU-07 |'))
new_iu = next(l for l in new.splitlines() if l.startswith('| IU-07 |'))
assert new.replace(addition, '', 1).replace(new_iu, old_iu, 1).encode() == read(B, cat)
vector_ids = [l.split('|')[1].strip() for l in addition.splitlines() if l.startswith('| R4-U04-PP')]
assert vector_ids == ['R4-U04-PP' + str(i).zfill(2) for i in range(1, 8)]
for text, cols in [(new_pp, 6), (addition, 5)]:
    assert all(len(l.split('|')) == cols for l in text.splitlines() if l.startswith('|'))

save('identity.json', {
    'task': 'R4-U04 independent candidate-v1', 'reviewer_task': '/root',
    'reviewer_thread_id': os.environ.get('CODEX_THREAD_ID', 'UNVERIFIED'),
    'source_parent_thread_id': '01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',
    'requested_model_contract': {'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra',
                                 'service_tier': 'default', 'fast': False, 'actual_echo': 'UNVERIFIED'},
    'independence': 'New reviewer thread; did not author this candidate or execute author validation script.',
    'candidate': {'commit': C, 'tree': expected_trees[C], 'parent': T},
    'author_evidence_successor': {'commit': E, 'tree': expected_trees[E], 'role': 'receipt only, not reviewed candidate'},
    'report_branch': 'review/r4-u04-independent-candidate-20261012',
    'report_branch_parent': E, 'report_write_root': REVIEW_ROOT,
    'contract_commit': T, 'formal_base': B, 'reference': {'commit': R, 'tree': expected_trees[R]},
    'preparation_receipt': identity(P, receipt_path), 'task_input_files': task_ids,
    'candidate_changed_files': candidate_ids, 'author_publication_receipt': identity(E, AUTHOR_ROOT + 'candidate-publication.json'),
    'source_full_byte_identities': source_ids, 'supplemental_source': supplemental_source,
    'formal_before': formal_before, 'actual_integration_review': 'NOT_PERFORMED',
    'formal_acceptance_registered': False, 'closure_registered': False})
save('validation.json', {
    'evidence_level': 'TOOL_VALIDATION', 'status': 'PASS_INTEGRITY_SCOPE_AND_PRESERVATION_ONLY',
    'started_at': started, 'finished_at': datetime.now(timezone.utc).isoformat(),
    'versions': {'python': platform.python_version(), 'git': git('--version').decode().strip()},
    'command': 'python3 ' + REVIEW_ROOT + 'candidate-v1/validate-inputs.py',
    'candidate_commit': C, 'candidate_tree': expected_trees[C],
    'all_changed_paths': changes, 'outside_author_scope': [],
    'source_identities_checked': len(source_ids), 'canonical_finding_matches_fixed_review': True,
    'frozen_task_full_bytes_match_preparation_receipt': True,
    'formal_baseline_drift_in_contract': 'NONE', 'other_formal_files_unchanged_complete_bytes': 129,
    'WP28_reverts_to_B_after_only_PP_section_and_identity_row_removed': True,
    'catalog_reverts_to_B_after_only_IU07_and_new_vector_section_removed': True,
    'PPUP_PPMAX_sync_and_all_other_old_clauses_preserved': True,
    'candidate_publication_claims_independently_verified_against_complete_blobs': True,
    'vector_ids_and_columns_checked': vector_ids,
    'new_reference_or_model_or_host_execution_count': 0,
    'execution_status': 'NOT_EXECUTED_THIS_UPDATE',
    'limits': 'Byte/JSON/table/scope checks do not evaluate vectors or prove behavior; semantic verdict is separately reasoned from source and specs.',
    'side_effects': 'Only own candidate-v1/identity.json and validation.json written; all inputs read-only.'})
print(json.dumps({'status': 'PASS_INTEGRITY_SCOPE_AND_PRESERVATION_ONLY',
                  'candidate': C, 'source_files': len(source_ids),
                  'candidate_changed_files': len(changes), 'other_formal_files': 129,
                  'execution_status': 'NOT_EXECUTED_THIS_UPDATE'}))
