"""Independent identity/scope/binding checks. No author/reference code execution."""
import datetime, difflib, gzip, hashlib, json, pathlib, re, subprocess

SESSION = pathlib.Path('/workspace/r7-review-session')
REPO = pathlib.Path('/workspace/r7-u01-reviewer-checkout')
CTX = pathlib.Path('/workspace/r7-context/R7-U01-reviewer')
INPUT = pathlib.Path('/workspace/r7-review-input/R7-U01-de550bb9fe5d2b80312b1a4f6f166d2a6aa5fc67')
BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'
CAND = 'de550bb9fe5d2b80312b1a4f6f166d2a6aa5fc67'
FREEZE = '58c6427f2ba48aa7dd3b59d4ab1e40c54394fd3a'
DISPATCH = '6ec1d09e9c470954964d72761c83a760ef4f0364'

def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def verify(data, row):
    actual=identity(data)
    for key, value in actual.items():
        ek='git_blob_content_id' if key=='git_blob' and 'git_blob_content_id' in row else key
        if ek in row: assert value==row[ek], (ek,value,row[ek])
    return actual

def git(*args):
    target=REPO if args[0]=='rev-parse' and args[-1].startswith(BASE) else pathlib.Path('/workspace/r7-review-metadata')
    if args[0]=='show' and args[-1].startswith(BASE): target=REPO
    if args[0]=='ls-tree' and BASE in args: target=REPO
    return subprocess.check_output(['git',*args],cwd=target)

def pointer(data, ptr):
    for key in ptr.split('/')[1:]:
        key=key.replace('~1','/').replace('~0','~')
        data=data[int(key)] if isinstance(data,list) else data[key]
    return data

def walk(data):
    if isinstance(data,dict):
        yield data
        for v in data.values(): yield from walk(v)
    elif isinstance(data,list):
        for v in data: yield from walk(v)

frozen=json.loads((SESSION/'candidate-input.json').read_text())
contract=json.loads((CTX/'dispatch/delegation/contracts/R7-U01.json').read_text())
assert git('rev-parse',BASE+'^{tree}').decode().strip()=='84f79ec6e772aacbf3a464fde68cdc5a280e2950'
assert git('rev-parse',BASE+':deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
assert git('rev-parse',CAND+'^{tree}').decode().strip()==frozen['candidate_tree']
assert git('rev-parse',FREEZE+'^{tree}').decode().strip()=='41849a965da575666d2b8363125ba14eb46bd6ec'
freeze_path='review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U01/'
for commit, path, local in [
 (FREEZE, freeze_path+'candidate-input.json', SESSION/'candidate-input.json'),
 (FREEZE, freeze_path+'candidate-restore/R7-U01.json', pathlib.Path('/workspace/r7-review-bootstrap/R7-U01/candidate-restore/R7-U01.json')),
 (DISPATCH, freeze_path+'reviewer-dispatch.md', SESSION/'reviewer-dispatch.md'),
 ('658488c81f1f3181a488298ab27850c8af951d73','review/remediation-seventh-20261015-prepare/tools/restore_container_context.py',pathlib.Path('/workspace/r7-bootstrap/R7-U01-reviewer/tools/restore_container_context.py')),
 ('658488c81f1f3181a488298ab27850c8af951d73','review/remediation-seventh-20261015-prepare/recovery/batches/R7-U01.json',pathlib.Path('/workspace/r7-bootstrap/R7-U01-reviewer/recovery/batches/R7-U01.json'))]:
    assert git('show',commit+':'+path)==local.read_bytes(), path
verify((CTX/'dispatch/delegation/contracts/R7-U01.json').read_bytes(),frozen['original_contract_commit_path_identity'])
files=[]
for row in frozen['candidate_and_author_evidence_file_identities']:
    data=(INPUT/'candidate'/row['path']).read_bytes()
    ident=verify(data,row)
    assert data==git('show',CAND+':'+row['path'])
    assert git('ls-tree',CAND,'--',row['path']).decode().startswith('100644 blob '+ident['git_blob'])
    files.append(dict(path=row['path'],**ident,git_mode='100644',full_git_object_match=True))
actual=git('diff','--name-status',BASE,CAND).decode().splitlines()
assert actual==[row['status']+'\t'+row['path'] for row in frozen['complete_diff_against_B']]
assert all(x.startswith('A\tcandidates/R7-U01/') for x in actual)
for row in json.loads((INPUT/'candidate/candidates/R7-U01/evidence/author/artifact-manifest.json').read_text())['files']:
    verify((INPUT/'candidate'/row['path']).read_bytes(),row)
restored=[]
for root, plan_path in [(CTX,pathlib.Path('/workspace/r7-bootstrap/R7-U01-reviewer/recovery/batches/R7-U01.json')),
                       (INPUT,pathlib.Path('/workspace/r7-review-bootstrap/R7-U01/candidate-restore/R7-U01.json'))]:
    plan=json.loads(plan_path.read_text())
    for category in ['artifacts','evidence','fixed_read_inputs']:
        for row in plan[category]:
            data=(root/row['local_path']).read_bytes(); verify(data,row)
            assert not (root/row['local_path']).stat().st_mode & 0o222
            if category=='evidence':
                encoded=(root/'transport'/row['transport_path']).read_bytes()
                verify(encoded,row['encoded_identity']); assert gzip.decompress(encoded)==data
            restored.append(dict(local_path=str(root/row['local_path']),**identity(data)))
known={hashlib.sha256(p.read_bytes()).hexdigest():p.read_bytes() for p in (CTX/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs').glob('*.raw')}
seen=set();bindings=[]
for row in walk(contract):
    if row.get('input_sha256') not in known or 'raw_member_byte_offsets' not in row:continue
    key=(row['input_sha256'],row['json_pointer'],tuple(row['raw_member_byte_offsets']))
    if key in seen:continue
    seen.add(key);data=known[key[0]];lo,hi=key[2];part=data[lo:hi]
    assert len(part)==row['raw_member_bytes'] and hashlib.sha256(part).hexdigest()==row['raw_member_sha256']
    value=pointer(json.loads(data),row['json_pointer'])
    canonical=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(canonical).hexdigest()==row['canonical_sha256']
    bindings.append(dict(binding_id=row.get('binding_id'),json_pointer=row['json_pointer'],input_sha256=key[0],exact_raw_and_canonical_match=True))
contrib=json.loads((INPUT/'candidate/candidates/R7-U01/evidence/author/contributions.json').read_text())
mirror_checks=[]
patch=[]
for row in contrib['files']:
    old=git('show',BASE+':'+row['formal_target']); new=(INPUT/'candidate'/row['candidate_path']).read_bytes()
    verify(old,row['base']); verify(new,row['candidate'])
    opcodes=difflib.SequenceMatcher(None,old.decode().splitlines(),new.decode().splitlines(),autojunk=False).get_opcodes()
    hunks=[dict(operation=op,base_lines=[a+1,b],candidate_lines=[c+1,d]) for op,a,b,c,d in opcodes if op!='equal']
    assert hunks==row['hunks']
    mirror_checks.append(dict(path=row['candidate_path'],base_identity=identity(old),candidate_identity=identity(new),hunks=hunks))
    patch.extend(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile='a/'+row['formal_target'],tofile='b/'+row['formal_target']))
    if row['formal_target'].startswith(('audit/','planning/','deliverables/final-specification-set/test-catalog/')):assert new.startswith(old)
assert ''.join(patch).encode()==(SESSION/'integrator-mirror-diffs.patch').read_bytes()
integrator=json.loads((SESSION/'integrator-remote-readback.json').read_text())
assert integrator['candidate_commit']==CAND and integrator['candidate_tree']==frozen['candidate_tree']
for row in integrator['files']:verify((INPUT/'candidate'/row['path']).read_bytes(),row)
catalog=(INPUT/'candidate/candidates/R7-U01/deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md').read_text()
new=catalog.split('## R7-U01：',1)[1]
vectors=['GR7-M01-001-V'+str(i) for i in range(1,4)]+['J01-V'+str(i).zfill(2) for i in range(1,14)]
for v in vectors:assert new.count('| '+v+' |')==1
assert 'NOT_EXECUTED' in new
assert not git('ls-tree','-r','--name-only',BASE,'.agents').strip()
assert not git('ls-tree','-r','--name-only',DISPATCH,'.agents').strip()
result=dict(schema='r7.u01-independent-mechanical-audit.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            status='PASS_TOOL_VALIDATION_ONLY',candidate_files=files,restored_files_verified=len(restored),
            restored_bytes_verified=sum(x['bytes'] for x in restored),raw_bindings=bindings,mirrors=mirror_checks,
            exact_candidate_diff=actual,vectors_present=vectors,
            independent_recomputed_patch_matches_integrator_patch=True,
            unchanged_catalog_prefixes=True,reference_execution='NOT_EXECUTED',semantic_credit=False,
            source_scripts_executed=0,author_programs_executed=0)
(SESSION/'mechanical-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','restored_files_verified','restored_bytes_verified','source_scripts_executed','author_programs_executed']}))
