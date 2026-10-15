"""Independent frozen byte, Git-tree, exact-scope and original-binding audit."""
import datetime, difflib, hashlib, json, pathlib, re, subprocess
OUT = pathlib.Path(__file__).parent
ROOT = pathlib.Path.cwd()
CONTEXT = pathlib.Path('/workspace/r7-context/R7-U10-reviewer')
BOOT = pathlib.Path('/workspace/r7-review-bootstrap/R7-U10-r1')
INPUT = pathlib.Path('/workspace/r7-review-input/R7-U10-r1-583330fb69935ff6b2eb32ca11ede6c23bde5ecd/candidate')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'

def identity(b):
    return {'bytes':len(b), 'sha256':hashlib.sha256(b).hexdigest(), 'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}

def verify(b, expected):
    actual=identity(b)
    for key, value in actual.items():
        ex=expected.get(key,expected.get('git_blob_content_id') if key=='git_blob' else None)
        if ex is not None: assert value==ex,(key,value,ex)
    return actual

def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT)
def load(path): return json.loads(pathlib.Path(path).read_bytes())
def endpoint(name): return json.loads(load(OUT/'tool-evidence'/name)['structuredContent']['content'])

original=load('/workspace/r7-bootstrap/R7-U10-reviewer/recovery/batches/R7-U10.json')
contract=load(CONTEXT/'dispatch/delegation/contracts/R7-U10.json')
freeze=load(BOOT/'candidate-input.json')
candidate_plan=load(BOOT/'candidate-restore/R7-U10.json')
verified_original=[{'path':r['local_path'],**verify((CONTEXT/r['local_path']).read_bytes(),r)} for k in ('artifacts','evidence','fixed_read_inputs') for r in original[k]]
assert len(verified_original)==39
ctree=endpoint('candidate-u10-tree.json')
assert not ctree['truncated']
tree_files={'candidates/R7-U10/'+r['path']:r for r in ctree['tree'] if r['type']=='blob'}
expected={r['path']:r for r in freeze['candidate_and_author_evidence_file_identities']}
assert set(tree_files)==set(expected)=={r['path'] for r in candidate_plan['artifacts']}
verified_candidate=[]
for path, row in sorted(expected.items()):
    actual=verify((INPUT/path).read_bytes(),row)
    t=tree_files[path]
    assert t['mode']==row['git_mode']=='100644' and t['sha']==actual['git_blob'] and t['size']==actual['bytes']
    verified_candidate.append({'path':path,**actual,'mode':t['mode']})
assert len(verified_candidate)==61 and sum(x['bytes'] for x in verified_candidate)==1050546
# Root tree equality outside the sole new candidates/ member proves the full diff scope.
base={}
for raw in git('ls-tree','-z',B).split(b'\0'):
    if raw:
        meta,path=raw.split(b'\t');mode,kind,sha=meta.decode().split();base[path.decode()]={'mode':mode,'type':kind,'sha':sha}
remote=endpoint('candidate-root.json')
assert not remote['truncated']
remote_map={r['path']:{k:r[k] for k in ('mode','type','sha')} for r in remote['tree']}
assert {k:v for k,v in remote_map.items() if k!='candidates'}==base
assert set(remote_map)-set(base)=={'candidates'}

def tree_id(entries):
    data=b''
    for path,row in sorted(entries.items(), key=lambda kv:(kv[0]+('/' if kv[1]['type']=='tree' else '')).encode()):
        mode=row['mode'].lstrip('0')
        data+=mode.encode()+b' '+path.encode()+b'\0'+bytes.fromhex(row['sha'])
    return hashlib.sha1(b'tree '+str(len(data)).encode()+b'\0'+data).hexdigest()

assert tree_id(remote_map)==freeze['candidate_tree']=='7a81a11b22d771fe79f165a265fa108c4a85502c'
assert tree_id(base)==git('rev-parse',B+'^{tree}').decode().strip()=='84f79ec6e772aacbf3a464fde68cdc5a280e2950'
manifest=load(INPUT/'candidates/R7-U10/evidence/author/artifact-manifest.json')
manifest_checked=[]
for row in manifest['files']:
    path=row['path'];verify((INPUT/path).read_bytes(),row.get('new',row.get('new_identity',row.get('identity',row))))
    if isinstance(row.get('base'),dict): verify(git('show',B+':'+row['original_path']),row['base'])
    manifest_checked.append(path)
# Resolve each exact original member reference independently, including nested bindings.
raws={r['sha256']:(CONTEXT/r['local_path']).read_bytes() for r in original['evidence']}
supp=load(OUT/'supplement-reception.json')
for row in supp['files']:
    data=pathlib.Path(row['local_path']).read_bytes();verify(data,row);raws[row['sha256']]=data
seen={}
def pointer(obj,p):
    for key in p.split('/')[1:]:
        key=key.replace('~1','/').replace('~0','~');obj=obj[int(key)] if isinstance(obj,list) else obj[key]
    return obj
def references(obj):
    if isinstance(obj,dict):
        if all(k in obj for k in ('input_sha256','json_pointer','raw_member_byte_offsets')):
            raw=raws[obj['input_sha256']];start,end=obj['raw_member_byte_offsets'];part=raw[start:end]
            assert len(part)==obj['raw_member_bytes'] and hashlib.sha256(part).hexdigest()==obj['raw_member_sha256']
            v=pointer(json.loads(raw),obj['json_pointer'])
            canonical=json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
            assert hashlib.sha256(canonical).hexdigest()==obj['canonical_sha256']
            seen[(obj['input_sha256'],obj['json_pointer'])]={'input_sha256':obj['input_sha256'],'pointer':obj['json_pointer'],'raw_member_sha256':obj['raw_member_sha256']}
        for value in obj.values():references(value)
    elif isinstance(obj,list):
        for value in obj:references(value)
references(contract)
norm=load(CONTEXT/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json')
for i in (19,27,21):references(norm['records'][i])
changes=[];diffs=[]
for row in contract['paths']:
    if row['classification']!='required':continue
    old=git('show',B+':'+row['path'])
    assert old==(CONTEXT/'inputs/project'/row['path']).read_bytes()
    new=(INPUT/row['candidate_path']).read_bytes()
    a,b=old.decode().splitlines(True),new.decode().splitlines(True)
    spans=[{'kind':tag,'old_halfopen_lines0':[i,j],'new_halfopen_lines0':[k,l]} for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes() if tag!='equal']
    changes.append({'path':row['path'],'old':identity(old),'new':identity(new),'spans':spans})
    diffs.append(''.join(difflib.unified_diff(a,b,fromfile='B/'+row['path'],tofile=row['candidate_path'])))
# Every original catalog row is identical except AN-M09 replacement and WE-M17 suffix.
catalog='deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md'
old=git('show',B+':'+catalog).decode().splitlines()
new=(INPUT/'candidates/R7-U10'/catalog).read_text().splitlines()
old_rows={r.split('|')[1].strip():r for r in old if re.match(r'^\| [A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+ \|',r)}
new_rows={r.split('|')[1].strip():r for r in new if re.match(r'^\| [A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+ \|',r)}
for key,line in old_rows.items():
    if key=='AN-M09':continue
    if key=='WE-M17':assert new_rows[key].startswith(line[:-2])
    else:assert new_rows[key]==line,key
assert sum(r.startswith('| TOOL-AN-') for r in new)==17
wp74='deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md'
old74=git('show',B+':'+wp74).decode();new74=(INPUT/'candidates/R7-U10'/wp74).read_text()
for start,end in [('## 2.','## 18.'),('## 19.','## 21.')]:
    assert old74[old74.index(start):old74.index(end)]==new74[new74.index(start):new74.index(end)]
# Arithmetic only; no executable behavioral model or reference calls.
arithmetic={'n0':[960,192], 'n6':[960,192*((6+4)//5)], 'cell5':[192*(5%5),192*(5//5)], 'slot0':[96-56,96-68,2*56,2*68], 'slot1':[192+96-56,96-68,2*56,2*68]}
assert arithmetic=={'n0':[960,192],'n6':[960,384],'cell5':[0,192],'slot0':[40,28,112,136],'slot1':[232,28,112,136]}
all_cil=(OUT/'logs/001-cil-all.stdout').read_text()
assert len(re.findall('^METHOD ',all_cil,re.M))==15 and len(re.findall('^EH_CLAUSE ',all_cil,re.M))==11
for name in ['038-cil-decode.stdout','039-cil-helpers.stdout']:
    prior=(CONTEXT/'supplements/tasks/R7-C06/logs'/name).read_text()
    assert all(chunk in all_cil for chunk in re.findall(r'METHOD .*?(?=METHOD |\Z)',prior,re.S))
assert not git('diff','--name-only',B,'--',':(exclude)candidates/R7-U10/evidence/reviewer/r1/').strip()
result={'schema':'r7.u10.reviewer.independent-tool-validation.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'TOOL_VALIDATION_ONLY','original_files':verified_original,'candidate_files':verified_candidate,'candidate_root_tree':tree_id(remote_map),'full_diff_scope':'Only new candidates/R7-U10/ subtree; all other root entries exactly equal B','manifest_declared_files_checked':manifest_checked,'exact_original_bindings':list(seen.values()),'changes':changes,'preserved_catalog_rows':len(old_rows)-2,'tool_vectors':17,'arithmetic_only':arithmetic,'static_decode':{'methods':15,'EH_clauses':11,'old_displays_match':True,'target_program_executed':False},'behavior_vectors':'NOT_EXECUTED','semantic_PASS_from_tool':False}
(OUT/'independent-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'independent-mirror-diff.patch').write_text('\n'.join(diffs))
print(json.dumps({'original_files':len(verified_original),'candidate_files':len(verified_candidate),'candidate_bytes':sum(r['bytes'] for r in verified_candidate),'original_bindings':len(seen),'manifest_declarations':len(manifest_checked),'preserved_catalog_rows':len(old_rows)-2,'candidate_tree':tree_id(remote_map),'semantic_credit':False}))
