"""U04 actual identity/integration/cache validation only; no behavior execution."""
import hashlib
import json
import os
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/workspace/r4-u04-independent-actual-review')
OUT = Path(__file__).resolve().parent
A = 'ede6a0714d29843c2ca896af6187ae1dc97a9d8a'
P = 'cfc19190f6596896524f2fc9577471577a3306de'
Q = '0cf49785b67baa911deb4ff8acfa9cc64395ce8a'
C = '1c2cdcbe6509839a19fd3c48c8a412a6c19e161a'
V = 'c10aaea975c0b0e87a88de9d536e2ab2afb45f0b'
E = '53edd67b69d3641de3d748ceb1bfeb847f621f6a'
B = '1f36475d22120a0d1175967d5b17d71fe8311d88'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
S = 'd305ba47f31ecfde747b763682e87f32abe54888'
PREP = 'review/remediation-fourth-20261012-prepare/'
TASK = PREP + 'registration/R4-U04/'
AUTHOR = PREP + 'batches/R4-U04/author/'
CANDIDATE = PREP + 'batches/R4-U04/review/candidate-v1/'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def read(commit, path):
    return git('show', commit + ':' + path)


def paths(commit, prefix):
    return git('ls-tree', '-r', '--name-only', commit, prefix).decode().splitlines()


def identity(commit, path, data=None):
    data = read(commit, path) if data is None else data
    return {'commit': commit, 'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': git('rev-parse', commit + ':' + path).decode().strip(),
            'full_bytes_loaded': True}


def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


start = datetime.now(timezone.utc).isoformat()
assert git('rev-parse', A + '^{tree}').decode().strip() == '21b917b2f5267ec4b9f3a0d69b135b0011e43f49'
assert git('rev-parse', P + '^{tree}').decode().strip() == 'ff8f0730a6eee0cb0966d5f3e06c90557b883b8d'
assert git('show', '-s', '--format=%P', A).decode().strip() == Q
handoff = json.loads(read(P, TASK + 'actual-review-handoff.json'))
assert handoff['actual_commit'] == A and handoff['candidate']['commit'] == C
assert handoff['same_independent_reviewer_thread_id'] == '01a130d5-fcbe-7506-9573-e758528ad023'
formal = handoff['formal_read_paths']
assert set(git('diff', '--name-only', Q, A, '--', 'deliverables').decode().splitlines()) == set(formal)
assert git('diff', '--name-only', A, P, '--', 'deliverables').decode().strip() == ''
git('diff', '--check', Q, A)
task_paths = paths(P, TASK)
task_ids = [identity(P, p) for p in task_paths]
for p in task_paths:
    if p.endswith('.json'):
        json.loads(read(P, p))

partition = {'U04_exact_candidate': [], 'U01_U02_U03_exact_accepted': [], 'unchanged_B': []}
manifest = handoff['formal_files_131']
assert len(manifest) == 131 and set(f['path'] for f in manifest) == set(paths(A, 'deliverables/final-specification-set'))
full_identities = []
for f in manifest:
    p = f['path']
    data = read(A, p)
    item = identity(A, p, data)
    assert all(item[k] == f[k] for k in ['bytes', 'sha256', 'git_blob'])
    assert data == read(P, p)
    if p in formal:
        assert data == read(C, p)
        group = 'U04_exact_candidate'
    elif f['qualification'] == 'U01_U02_U03_accepted_exact_bytes':
        assert data == read(Q, p)
        group = 'U01_U02_U03_exact_accepted'
    else:
        assert f['qualification'] == 'unchanged_B_exact_bytes'
        assert data == read(B, p) == read(Q, p)
        group = 'unchanged_B'
    partition[group].append(p)
    full_identities.append(item)
assert [len(partition[g]) for g in partition] == [2, 24, 105]
consumers = []
for f in handoff['required_shared_consumers']:
    item = identity(A, f['path'])
    assert all(item[k] == f[k] for k in ['bytes', 'sha256', 'git_blob'])
    consumers.append(dict(item, scope=f['range_scope']))
for p in [f['path'] for f in consumers if '/wp67-a-' in f['path'] or '/wp17-messages-' in f['path']]:
    assert read(A, p) == read('5dd6789b22e03b85bb81ae73b9c65a1fab585186', p)
wp67 = next(f['path'] for f in consumers if '/wp67-a-' in f['path'])
actual_text, base_text = read(A, wp67).decode(), read(B, wp67).decode()
section = lambda text: text[text.index('## 5. γ：'):text.index('## 6. δ：')]
assert section(actual_text) == section(base_text)

cache_ids = []
for origin, prefix in [(E, AUTHOR), (V, CANDIDATE)]:
    for p in paths(origin, prefix):
        assert read(A, p) == read(origin, p) == read(P, p)
        cache_ids.append({'path': p, 'origin_commit': origin,
                          'actual_git_blob': git('rev-parse', A + ':' + p).decode().strip(),
                          'complete_bytes_equal': True,
                          'reuse': 'exact unchanged candidate evidence; no new behavior PASS'})
all_changes = git('diff', '--name-only', Q, A).decode().splitlines()
allowed_extra = {TASK + 'integration-check.json', TASK + 'shared-consumer-check.json', PREP + 'registration/status-ledger.json'}
assert all(p in formal or p.startswith(AUTHOR) or p.startswith(CANDIDATE) or p in allowed_extra for p in all_changes)
delivery_paths = git('diff', '--name-only', S, P).decode().splitlines()
assert all(p.startswith(PREP) or p in formal for p in delivery_paths)
cached_source = json.loads(read(V, CANDIDATE + 'read-ledger.json'))['source_reads']
for f in cached_source:
    source_blob = subprocess.check_output(['git', '-C', '/workspace/r4-u04-reference', 'rev-parse', R + ':' + f['path']]).decode().strip()
    assert source_blob == f['git_blob']

save('identity.json', {
    'review_kind': 'INDEPENDENT_ACTUAL_REVIEW',
    'reviewer_task': '/root', 'reviewer_thread_id': os.environ.get('CODEX_THREAD_ID', 'UNVERIFIED'),
    'same_reviewer_as_candidate': True,
    'model_request': dict(handoff['model_request'], actual_echo='UNVERIFIED'),
    'actual': {'commit': A, 'tree': '21b917b2f5267ec4b9f3a0d69b135b0011e43f49', 'parent': Q},
    'task_publication': {'commit': P, 'tree': 'ff8f0730a6eee0cb0966d5f3e06c90557b883b8d'},
    'candidate': handoff['candidate'], 'candidate_review_publication': V,
    'formal_base': B, 'source_commit': R,
    'actual_formal_files': [f for f in full_identities if f['path'] in formal],
    'current_shared_consumers': consumers, 'task_files': task_ids,
    'formal_partition': partition,
    'formal_identity_manifest_sha256': hashlib.sha256(json.dumps(full_identities, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
    'candidate_evidence_reuse': cache_ids,
    'source_cache': {'exact_commit': R, 'file_blob_identities_verified': len(cached_source),
                     'source_record_origin': V + ':' + CANDIDATE + 'read-ledger.json',
                     'all_source_or_history_download_repeated': False},
    'report_branch': 'review/r4-u04-independent-actual-20261012',
    'report_branch_parent': P, 'formal_write_paths': [], 'global_write_paths': [],
    'formal_acceptance_registered': False, 'closure_registered': False})
save('validation.json', {
    'evidence_level': 'TOOL_VALIDATION', 'status': 'PASS_ACTUAL_IDENTITY_PARTITION_AND_SCOPE_ONLY',
    'command': 'python3 ' + PREP + 'batches/R4-U04/review/actual-v1/validate-actual.py',
    'versions': {'python': platform.python_version(), 'git': git('--version').decode().strip()},
    'started_at': start, 'finished_at': datetime.now(timezone.utc).isoformat(), 'exit_code': 0,
    'actual_commit': A, 'task_publication_commit': P,
    'formal_partition_counts': {k: len(v) for k, v in partition.items()},
    'current_shared_consumer_complete_identities': len(consumers),
    'U03_current_WP67_A_and_WP17_equal_accepted_bytes': True, 'current_WP67_A_section5_equal_B': True,
    'copied_candidate_evidence_exact_complete_bytes': len(cache_ids),
    'actual_integration_changed_paths': all_changes, 'outside_actual_integration_scope': [],
    'new_delivery_checkpoint': S, 'task_publication_new_delivery_paths': delivery_paths,
    'formal_actual_to_task_publication_delta': [],
    'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE', 'behavior_executions': 0,
    'limits': 'Identity and preservation checks do not sign semantics or evaluate vectors. Actual semantics is a separate bounded current-consumer check.',
    'side_effects': 'Only own actual-v1/identity.json and validation.json written.'})
print(json.dumps({'status': 'PASS_ACTUAL_IDENTITY_PARTITION_AND_SCOPE_ONLY',
                  'partition': {k: len(v) for k, v in partition.items()},
                  'current_consumers': len(consumers), 'new_delivery_paths': len(delivery_paths),
                  'unchanged_candidate_evidence': len(cache_ids), 'behavior_executions': 0}))
