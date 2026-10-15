"""Independent byte/scope audit only; no semantic PASS and no reference execution."""
import datetime
import difflib
import hashlib
import json
import os
from pathlib import Path
import subprocess

REPO = Path('/workspace/pokemon-essentials-clean-room')
OUT = Path(__file__).resolve().parent
BOOT = Path('/workspace/r7-review-bootstrap/R7-U13-r1')
ORIGBOOT = Path('/workspace/r7-bootstrap/R7-U13-reviewer')
ORIG = Path('/workspace/r7-context/R7-U13-reviewer')
CAND = Path('/workspace/r7-review-input/R7-U13-r1-5635c73ea14adc278961da0e3917c2d00d580a25')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
DISPATCH = '95c260d8f3fb4a171675dde877137fcd4c2f1c8d'
FREEZE = 'aa369555b0e8b6c8b077f964b54ed63d3b924f26'
COMMIT = '5635c73ea14adc278961da0e3917c2d00d580a25'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)

def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def verify(data, expected):
    actual = identity(data)
    expected = dict(expected)
    if 'git_blob' in expected:
        expected['git_blob_content_id'] = expected['git_blob']
    for key, value in actual.items():
        if key in expected:
            assert value == expected[key], (key, value, expected[key])
    return actual

frozen = []
for local, commit, path in [
    (ORIGBOOT/'reviewer-dispatch.md', DISPATCH, 'review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U13/reviewer-dispatch.md'),
    (ORIGBOOT/'tools/restore_container_context.py', '658488c81f1f3181a488298ab27850c8af951d73', 'review/remediation-seventh-20261015-prepare/tools/restore_container_context.py'),
    (ORIGBOOT/'recovery/batches/R7-U13.json', '658488c81f1f3181a488298ab27850c8af951d73', 'review/remediation-seventh-20261015-prepare/recovery/batches/R7-U13.json'),
    (ORIGBOOT/'recovery/independent-containers.md', '658488c81f1f3181a488298ab27850c8af951d73', 'review/remediation-seventh-20261015-prepare/recovery/independent-containers.md'),
    *[(BOOT/name, FREEZE, 'review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U13/'+name) for name in ['candidate-restore/R7-U13.json','candidate-input.json','mirror-diffs.patch','remote-readback.json']]
]:
    data = local.read_bytes()
    assert data == git('show', commit+':'+path), str(local)
    frozen.append(dict(commit=commit, path=path, **identity(data)))

plans = [(ORIGBOOT/'recovery/batches/R7-U13.json', ORIG), (BOOT/'candidate-restore/R7-U13.json', CAND)]
restored = []
for plan_path, destination in plans:
    plan = json.loads(plan_path.read_bytes())
    rows = plan['artifacts'] + plan['evidence'] + plan['fixed_read_inputs']
    actuals = []
    for row in rows:
        p = destination/row['local_path']
        data = p.read_bytes()
        actuals.append(dict(local_path=str(p), repository=row['repository'], commit=row['commit'],
                            remote_path=row['path'], **verify(data, row)))
    restored.append(dict(plan=str(plan_path), files=len(actuals), bytes=sum(x['bytes'] for x in actuals), identities=actuals))

freeze = json.loads((BOOT/'candidate-input.json').read_bytes())
assert git('rev-parse', FREEZE+'^{tree}').decode().strip() == '08bd0f362c74ef7645b5bbd70b557489c122ae29'
assert git('rev-parse', COMMIT+'^{tree}').decode().strip() == freeze['candidate_tree']
assert git('rev-parse', B+'^{tree}').decode().strip() == '84f79ec6e772aacbf3a464fde68cdc5a280e2950'
assert git('rev-parse', B+':deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
diff = [dict(zip(['status','path'], line.split('\t'))) for line in git('diff','--name-status',B,COMMIT).decode().splitlines()]
assert diff == freeze['complete_diff_against_B']
assert len(diff) == 24 and all(x['status']=='A' and x['path'].startswith('candidates/R7-U13/') for x in diff)
file_table = []
mirror_diffs = []
mirror_ops = []
for row in freeze['candidate_and_author_evidence_file_identities']:
    path = row['path']
    data = (CAND/'candidate'/path).read_bytes()
    actual = verify(data, row)
    assert git('show', COMMIT+':'+path) == data
    tree_line = git('ls-tree', COMMIT, '--', path).decode().strip()
    mode, kind, rest = tree_line.split(' ', 2)
    blob, tree_path = rest.split('\t')
    assert mode == row['git_mode'] == '100644' and kind == 'blob'
    assert tree_path == path and blob == actual['git_blob_content_id']
    file_table.append(dict(path=path, git_mode=mode, **actual))
    if row['role'] == 'candidate_mirror':
        target = row['formal_target']
        base = git('show', B+':'+target)
        verify(base, row['base_B_identity_or_explicit_new_file'])
        assert base == (ORIG/'inputs/project'/target).read_bytes()
        before, after = base.decode().splitlines(True), data.decode().splitlines(True)
        mirror_diffs.extend(difflib.unified_diff(before, after, fromfile='a/'+target, tofile='b/'+target))
        changes=[]
        for tag,i,j,k,l in difflib.SequenceMatcher(None,before,after,autojunk=False).get_opcodes():
            if tag != 'equal':
                allowed = {
                    'audit/source-traceability.md': [(313,326)],
                    'deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md': [(191,196),(212,214)],
                    'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md': [(400,436)],
                    'planning/feature-matrix.md': [(174,174)],
                }
                assert any(lo <= i+1 <= hi and j <= hi for lo,hi in allowed[target]), (target,tag,i,j)
                assert tag == 'insert' or (target == 'planning/feature-matrix.md' and tag == 'replace' and j-i == l-k == 1)
                changes.append(dict(operation=tag,base_interval_half_open_zero_based=[i,j],candidate_interval_half_open_zero_based=[k,l],base_anchor_line=i+1))
        mirror_ops.append(dict(path=target,changes=changes))
assert ''.join(mirror_diffs).encode() == (BOOT/'mirror-diffs.patch').read_bytes()
author = CAND/'candidate/candidates/R7-U13/evidence/author'
manifest = json.loads((author/'artifact-manifest.json').read_bytes())
assert len(manifest['artifacts']) == 4
for row in manifest['artifacts']:
    verify((CAND/'candidate'/row['candidate_path']).read_bytes(), row['candidate'])
    verify(git('show',B+':'+row['original_path']), row['base'])
counter = json.loads((ORIG/'evidence/tasks/R7-C13/inputs/evidence/received-final-proposals/GR7-D07-001/counter-review.json').read_bytes())['findings'][0]
proposal = json.loads((BOOT/'supplemental/tasks/R7-D07/findings.json').read_bytes())['findings'][0]
vectors = json.loads((author/'per-id.json').read_bytes())['records'][0]['vectors']
for original in counter['regression_vectors']+proposal['regression_vectors']:
    matches = [v for v in vectors if v['id']==original['id']]
    assert len(matches)==1
    for key in ['id','input','expected','execution']:
        assert matches[0][key] == original[key], (original['id'], key)
    assert matches[0]['behavior_result'] == 'NOT_EXECUTED'

catalog_path = 'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'
base_catalog = git('show',B+':'+catalog_path).decode()
new_catalog = (CAND/'candidate/candidates/R7-U13'/catalog_path).read_text()
old_rows=[s for s in base_catalog.splitlines() if s.startswith('| B04-R')]
new_rows=[s for s in new_catalog.splitlines() if s.startswith('| B04-R')]
assert old_rows == new_rows and len(old_rows)==28
body='deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md'
before=git('show',B+':'+body).decode();after=(CAND/'candidate/candidates/R7-U13'/body).read_text()
assert before.split('## 11.')[1] == after.split('## 11.')[1]
matrix='planning/feature-matrix.md'
before=git('show',B+':'+matrix).decode();after=(CAND/'candidate/candidates/R7-U13'/matrix).read_text()
assert next(x for x in before.splitlines() if x.startswith('| F05-01 |')) == next(x for x in after.splitlines() if x.startswith('| F05-01 |'))

context=json.loads((author/'execution-context.json').read_bytes())
thread=os.environ.get('CODEX_THREAD_ID')
assert thread and thread != context['actual_thread_id'] == freeze['author_task_id']
for commit in [B, DISPATCH]:
    assert git('ls-tree','-r','--name-only',commit,'.agents/skills') == b''
summary=dict(schema='r7-u13-reviewer-independent-byte-audit.v1', observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    status='TOOL_VALIDATION_PASS_ONLY', semantic_PASS=False, dispatch_commit=DISPATCH,
    dispatch_tree=git('rev-parse',DISPATCH+'^{tree}').decode().strip(), freeze_commit=FREEZE,freeze_tree='08bd0f362c74ef7645b5bbd70b557489c122ae29',
    candidate_commit=COMMIT,candidate_tree=freeze['candidate_tree'], fixed_B=B,
    reviewer_thread=thread,author_thread=context['actual_thread_id'], different_actual_thread=True,
    effective_configuration=dict(model='UNVERIFIED',reasoning_effort='UNVERIFIED',service_tier='UNVERIFIED',speed='UNVERIFIED'),
    frozen_controls=frozen,restored=restored,candidate_files=file_table,candidate_file_count=len(file_table),candidate_bytes=sum(x['bytes'] for x in file_table),
    complete_diff_against_B=diff,mirror_changes=mirror_ops,root_mirror_diff_exact=True,author_manifest_mirrors=4,
    author_evidence_manifest_nonself_unlisted=19,original_14_vector_fields_exact=True,B04_R_28_rows_exact=True,
    WP15_section11_exact=True,F05_01_exact=True,skills_found_in_B_or_dispatch=[],
    source_execution=0,host_Demo_native_media_save_replay=0)
(OUT/'byte-audit.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:summary[k] for k in ['status','candidate_file_count','candidate_bytes','different_actual_thread','original_14_vector_fields_exact','B04_R_28_rows_exact','WP15_section11_exact','F05_01_exact']},ensure_ascii=False))
