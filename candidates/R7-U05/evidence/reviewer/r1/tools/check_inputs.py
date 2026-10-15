"""Independent byte, scope and provenance checks, with no game/reference execution."""
import datetime
import difflib
import hashlib
import json
import os
from pathlib import Path
import subprocess

REPO = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parents[1]
BOOT = Path('/workspace/r7-review-bootstrap/R7-U05')
CONTEXT = Path('/workspace/r7-context/R7-U05-reviewer')
CANDIDATE = Path('/workspace/r7-review-input/R7-U05-3acf3e23fd79c3bed1b98d23873bc1f2fd25cafa/candidate')
PREFIX = 'candidates/R7-U05/'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
C = '3acf3e23fd79c3bed1b98d23873bc1f2fd25cafa'
F = '58c6427f2ba48aa7dd3b59d4ab1e40c54394fd3a'
D = '6ec1d09e9c470954964d72761c83a760ef4f0364'
PREP = 'review/remediation-seventh-20261015-prepare/'

def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest())

def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)

def read_json(path):
    return json.loads(path.read_bytes())

checks = []
def check(label, condition):
    if not condition:
        raise AssertionError(label)
    checks.append(label)

start = datetime.datetime.now(datetime.timezone.utc).isoformat()
freeze = read_json(BOOT / 'candidate-input.json')
gate = read_json(BOOT / 'candidate-freeze-requirements.json')
check('complete_freeze_fields', all(k in freeze for k in gate['required_fields']))
check('fixed_freeze_tree', git('rev-parse', F+'^{tree}').decode().strip() == '41849a965da575666d2b8363125ba14eb46bd6ec')
check('fixed_candidate_tree', git('rev-parse', C+'^{tree}').decode().strip() == freeze['candidate_tree'])
check('baseline_tree', git('rev-parse', B+'^{tree}').decode().strip() == freeze['fixed_B_tree'])
check('different_actual_context', os.environ['CODEX_THREAD_ID'] != freeze['author_task_id'])
check('unique_reviewer_branch', git('branch', '--show-current').decode().strip() == 'codex/r7-u05-reviewer-20261015-r1')
check('reviewer_started_from_exact_B', git('rev-parse', 'HEAD').decode().strip() == B)
check('candidate_is_descendant_of_B', subprocess.run(['git','merge-base','--is-ancestor',B,C],cwd=REPO).returncode == 0)

bindings = [(D, PREP+'candidate-freezes/R7-U05/reviewer-dispatch.md', BOOT/'reviewer-dispatch.md'),
            (D, PREP+'delegation/parallel-dispatch/candidate-freeze-requirements.json', BOOT/'candidate-freeze-requirements.json')]
for name in ['candidate-input.json','candidate-restore/R7-U05.json','mirror-diffs.patch','remote-readback.json']:
    bindings.append((F, PREP+'candidate-freezes/R7-U05/'+name, BOOT/name))
base_boot = Path('/workspace/r7-bootstrap/R7-U05-reviewer')
for name in ['tools/restore_container_context.py','recovery/batches/R7-U05.json','recovery/independent-containers.md']:
    local = base_boot / ('independent-containers.md' if name.endswith('independent-containers.md') else name)
    bindings.append(('658488c81f1f3181a488298ab27850c8af951d73',PREP+name,local))
bindings.append(('f622356f3beb9e84ea8cff9db07c7fb382565d3f',PREP+'delegation/contracts/R7-U05.json',base_boot/'R7-U05-contract.json'))
verified_bindings = []
for commit, path, local in bindings:
    data = local.read_bytes()
    check('fixed_git_bytes:'+path, git('show', commit+':'+path) == data)
    verified_bindings.append(dict(commit=commit,path=path,**identity(data)))
check('dispatch_declared_candidate_input_identity',identity((BOOT/'candidate-input.json').read_bytes()) == dict(bytes=11407,sha256='e82a75216fe339ec5897bd8aa943c3d3fe98ecdaaad8220333a48632142c3b42',git_blob='e69439e5f0e4cf2e12b5a023fbb468b9b22a65c0'))
check('dispatch_declared_candidate_plan_identity',identity((BOOT/'candidate-restore/R7-U05.json').read_bytes()) == dict(bytes=7384,sha256='7a862503d7d6042b933080e14245f3b20aec482882aa0c2b88d31e2a0452e1ea',git_blob='57dd52e3577c8e79353d9a128e9660120f4b679b'))

candidate_files = []
for row in freeze['candidate_and_author_evidence_file_identities']:
    data = (CANDIDATE/row['path']).read_bytes()
    actual = identity(data)
    check('candidate_identity:'+row['path'],all(actual[k]==row[k] for k in actual))
    check('candidate_git_bytes:'+row['path'],git('show',C+':'+row['path']) == data)
    mode, kind, blob = git('ls-tree',C,'--',row['path']).decode().split('\t')[0].split()
    check('regular_mode:'+row['path'],mode=='100644' and kind=='blob' and blob==actual['git_blob'])
    candidate_files.append(dict(path=row['path'],**actual,git_mode=mode,full_byte_match=True))
actual_diff = [{'status':line.split('\t')[0],'path':line.split('\t')[1]} for line in git('diff','--name-status',B,C).decode().splitlines()]
check('complete_candidate_diff',actual_diff == freeze['complete_diff_against_B'])
check('candidate_diff_scoped',all(r['path'].startswith(PREFIX) and r['status']=='A' for r in actual_diff))
check('candidate_file_set',set(git('ls-tree','-r','--name-only',C,'--',PREFIX).decode().splitlines()) == {r['path'] for r in candidate_files})
manifest=read_json(CANDIDATE/PREFIX/'evidence/author/artifact-manifest.json')
for row in manifest['files']:
    actual=identity((CANDIDATE/row['path']).read_bytes())
    expected=dict(row['new_identity']); expected['git_blob']=expected.pop('git_blob_content_id')
    check('author_manifest:'+row['path'],actual==expected)
check('author_manifest_complete_except_explicit_self',{r['path'] for r in candidate_files} == {r['path'] for r in manifest['files']}|{manifest['self_exclusion']['path']})

wp='deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md'
cat='deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md'
old_wp=git('show',B+':'+wp); new_wp=(CANDIDATE/PREFIX/wp).read_bytes()
old_cat=git('show',B+':'+cat); new_cat=(CANDIDATE/PREFIX/cat).read_bytes()
old_lines=old_wp.splitlines(keepends=True); new_lines=new_wp.splitlines(keepends=True)
changed_lines=[i+1 for i,(a,b) in enumerate(zip(old_lines,new_lines)) if a!=b]
check('WP34_only_line188',len(old_lines)==len(new_lines) and changed_lines==[188])
lo=new_cat.index('### R7-U05-PF：'.encode()); hi=new_cat.index('## R4-IV：'.encode(),lo)
check('catalog_all_B_bytes_preserved',new_cat[:lo]+new_cat[hi:]==old_cat)
check('only_approved_mirrors',{r['formal_target'] for r in freeze['candidate_and_author_evidence_file_identities'] if r['role']=='candidate_mirror'}=={wp,cat})
anchors=[]
for path,data in [(wp,new_wp),(cat,new_cat)]:
    offset=0
    for line_num,line in enumerate(data.splitlines(keepends=True),1):
        if (path==wp and line_num==188) or (path==cat and (line.startswith(b'| R7-U05-PF') or line.startswith('共同前提：**仅作者数据变体**'.encode()))):
            anchors.append(dict(path=PREFIX+path,line=line_num,byte_offsets=[offset,offset+len(line)],sha256=hashlib.sha256(line).hexdigest()))
        offset+=len(line)

plan=read_json(base_boot/'recovery/batches/R7-U05.json')
context_files=[]
for row in plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']:
    data=(CONTEXT/row['local_path']).read_bytes();actual=identity(data)
    expected=dict(bytes=row['bytes'],sha256=row['sha256'],git_blob=row['git_blob_content_id'])
    check('context_file:'+row['local_path'],actual==expected)
    context_files.append(dict(local_path=row['local_path'],**actual))
for row in plan['evidence']:
    actual=identity((CONTEXT/'transport'/row['transport_path']).read_bytes())
    check('encoded_object:'+row['transport_path'],actual['bytes']==row['encoded_identity']['bytes'] and actual['git_blob']==row['encoded_identity']['git_blob_content_id'])
for row in plan['fixed_read_inputs']:
    if row['repository']=='y805939188/pokemon-essentials-clean-room':
        check('B_snapshot_git_bytes:'+row['path'],git('show',row['commit']+':'+row['path'])==(CONTEXT/row['local_path']).read_bytes())

raw_dir=CONTEXT/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'
raws={p.stem:p.read_bytes() for p in raw_dir.glob('*.raw')}
documents={s:json.loads(data) for s,data in raws.items()}
members={}
def pointer(obj,p):
    for part in p.strip('/').split('/'):
        part=part.replace('~1','/').replace('~0','~')
        obj=obj[int(part)] if isinstance(obj,list) else obj[part]
    return obj
def visit(obj):
    if isinstance(obj,dict):
        s=obj.get('input_sha256')
        if s in raws and 'raw_member_byte_offsets' in obj:
            a,b=obj['raw_member_byte_offsets']; data=raws[s][a:b]
            key=s+'#'+obj['json_pointer']
            check('raw_member:'+key,len(data)==obj['raw_member_bytes'] and hashlib.sha256(data).hexdigest()==obj['raw_member_sha256'])
            value=pointer(documents[s],obj['json_pointer'])
            canonical=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
            check('canonical_member:'+key,hashlib.sha256(canonical).hexdigest()==obj['canonical_sha256'])
            members[key]=dict(byte_offsets=[a,b],raw_sha256=obj['raw_member_sha256'],canonical_sha256=obj['canonical_sha256'])
        for value in obj.values(): visit(value)
    elif isinstance(obj,list):
        for value in obj: visit(value)
visit(read_json(base_boot/'R7-U05-contract.json'))
challenge=documents['bcf3539beb2c1c24c44f3cd426dd4b4a49752b1a39d30925effb32a36b6329d6']['challenges'][1]
root=documents['e0c5ebb227169d6a24ca470630bdc0c22f4ea8f8a70a89951fae64546dde22ae']['records'][10]
check('root_decision_exact_C05_member',root['independent_adjudication']['decision_record']==challenge)
check('formal_tree_unchanged',git('rev-parse',C+':deliverables/final-specification-set')==git('rev-parse',B+':deliverables/final-specification-set'))
check('no_project_skills_at_B_or_dispatch',not git('ls-tree','-r','--name-only',B,'--','.agents','.codex') and not git('ls-tree','-r','--name-only',D,'--','.agents','.codex'))
for root_path in [CONTEXT,CANDIDATE.parent]:
    for path in root_path.rglob('*'):
        if path.is_file(): path.chmod(0o444)

result=dict(schema='r7.u05.reviewer-independent-input-check.v1',start_utc=start,
            end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            status='INPUT_BYTES_SCOPE_AND_PROVENANCE_VERIFIED',semantic_PASS=False,
            checks=checks,fixed_bindings=verified_bindings,candidate_files=candidate_files,
            candidate_files_count=len(candidate_files),candidate_bytes=sum(r['bytes'] for r in candidate_files),
            complete_candidate_diff=actual_diff,WP34_changed_lines=changed_lines,
            catalog_insert_byte_offsets=[lo,hi],candidate_anchors=anchors,
            context_files=context_files,context_bytes=sum(r['bytes'] for r in context_files),raw_members=members,
            task_context=dict(actual_thread_id=os.environ['CODEX_THREAD_ID'],actual_session_id=os.environ.get('CODEX_SESSION_ID'),
                              container_session_id=os.environ.get('CODEX_CAAS_SESSION_ID'),probe_pid=os.getpid(),
                              platform_task_id='UNVERIFIED_NO_EXPLICIT_TASK_ID_RETURN'),
            effective_configuration={k:'UNVERIFIED' for k in ['model','effort','tier','speed']},
            reference_behavior_model_host_Demo_native_save_replay='NOT_EXECUTED',new_subtasks=0)
with (OUT/'tools/input-validation.json').open('x') as stream:
    json.dump(result,stream,ensure_ascii=False,indent=2);stream.write('\n')
print(json.dumps(dict(status=result['status'],checks=len(checks),candidate_files=len(candidate_files),
                      candidate_bytes=result['candidate_bytes'],context_files=len(context_files),
                      context_bytes=result['context_bytes'],raw_members=len(members),semantic_PASS=False),indent=2))
