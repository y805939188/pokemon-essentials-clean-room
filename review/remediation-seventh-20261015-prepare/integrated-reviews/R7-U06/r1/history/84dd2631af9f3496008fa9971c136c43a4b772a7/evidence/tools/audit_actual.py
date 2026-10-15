import datetime,hashlib,json,os,pathlib,subprocess
ROOT=pathlib.Path('/workspace/r7-ir-R7-U06'); REPO=ROOT/'result'
B='e646432c644dec04d306842cc5a559a29c718fbc';MI='45c80832a41c1b56dcd7e9d93497758cbb7721de';FI='13d76ba61838b13925ba9d41f58a6b047564d926'
def git(*args):return subprocess.check_output(['git','-c','credential.helper=','-c','http.extraHeader=',*args],cwd=REPO)
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def verify(b,row):
 i=identity(b)
 for k,v in i.items():
  if k in row:assert row[k]==v,(k,row.get(k),v)
  if k=='git_blob' and 'git_blob_content_id' in row:assert row['git_blob_content_id']==v
 return i
def read_json(p):return json.loads(p.read_bytes())
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'kind':'TOOL_VALIDATION_ONLY','behavior_execution':'NOT_EXECUTED'}
plans=[]
for plan_name,dest in [('original-plans','original'),('actual-plans','actual-input'),('supplement-plans','supplement')]:
 p=read_json(ROOT/plan_name/'R7-U06.json');rows=p['artifacts']+p['evidence']+p['fixed_read_inputs'];out=[]
 for row in rows:out.append({'path':row['local_path'],**verify((ROOT/dest/row['local_path']).read_bytes(),row),'commit':row['commit']})
 plans.append({'plan':plan_name,'members':len(out),'bytes':sum(x['bytes'] for x in out),'rows':out})
receipt['restored']=plans
receipt['git']={c:git('rev-parse',c+'^{tree}').decode().strip() for c in [B,MI,FI,'c64774c60d91e522cb515ef71e3e9d4ea6b4712c']}
assert receipt['git'][MI]=='6480ffe3df49bd9776c719f3c9be1c13618fdb0a'
assert receipt['git'][FI]=='6747a584b91c86acd4771c1a6dee93260602106f'
receipt['formal_subtree']=git('rev-parse',MI+':deliverables/final-specification-set').decode().strip()
assert receipt['formal_subtree']=='8403869aaeb4726518414b409b3808c3c0780e65'
fi=read_json(ROOT/'bootstrap-evidence/integrated-input.json')
def tree(c):
 out={}
 for line in git('ls-tree','-r',c,'deliverables/final-specification-set').decode().splitlines():
  meta,path=line.split('\t');mode,typ,blob=meta.split();out[path]={'git_mode':mode,'git_blob':blob}
 return out
bt,mt=tree(B),tree(MI);assert set(bt)==set(mt) and len(mt)==131
formal=[]
for row in fi['all_formal_file_identities']:
 path=row['path'];assert mt[path]['git_blob']==row['git_blob'] and mt[path]['git_mode']==row['git_mode'];assert bt[path]['git_blob']==row['base_B_identity']['git_blob']
 changed=mt[path]!=bt[path];assert changed==row['changed_against_B'];formal.append({**row,'git_tree_matched':True})
assert sum(x['changed_against_B'] for x in formal)==26
receipt['formal131']=formal
receipt['formal_counts']={'all':131,'changed':26,'unchanged':105}
receipt['skills']={c:git('ls-tree','-r','--name-only',c,'.agents','.codex').decode().splitlines() for c in [B,MI]}
assert receipt['skills'][MI]==[]
j=read_json(ROOT/'actual-input/integration/applied-clauses.json');own=[]
for f in j['files']:
 if 'R7-U06' not in f['contributors']:continue
 path=f['path'];base=(ROOT/'actual-input/baseline'/path).read_bytes();actual=(ROOT/'actual-input/actual'/path).read_bytes();candidate=(ROOT/'actual-input/candidate/candidates/R7-U06'/path).read_bytes()
 assert actual==candidate;verify(base,f['baseline_identity']);verify(actual,f['assembled_candidate_clauses_identity']);assert identity(actual)['git_blob']==mt[path]['git_blob']
 before=base.decode().splitlines(keepends=True);after=actual.decode().splitlines(keepends=True);rebuilt=[];cursor=0;hunks=[]
 for h in f['hunks']:
  a,b=h['base_line_indices_half_open'];c,d=h['candidate_line_indices_half_open'];e,g=h['actual_final_line_indices_half_open']
  assert a>=cursor;removed=''.join(before[a:b]);added=''.join(after[e:g]);assert removed==h['removed_text'] and added==h['added_text'];verify(removed.encode(),h['removed_identity']);verify(added.encode(),h['added_identity']);assert ''.join(candidate.decode().splitlines(keepends=True)[c:d])==added
  rebuilt+=before[cursor:a]+[added];cursor=b
  offsets=[sum(len(s.encode()) for s in after[:e]),sum(len(s.encode()) for s in after[:g])]
  hunks.append({'base_lines_zero_based_half_open':[a,b],'MI_lines_one_based':[e+1,g],'MI_byte_offsets_half_open':offsets,'added_identity':identity(added.encode()),'removed_identity':identity(removed.encode())})
 rebuilt+=before[cursor:];assert ''.join(rebuilt).encode()==actual
 own.append({'path':path,'contributors':f['contributors'],'baseline':identity(base),'actual_MI':identity(actual),'equals_author_candidate':True,'hunks':hunks,'outside_hunks_exact_B':True})
assert len(own)==4 and sum(len(f['hunks']) for f in own)==6
receipt['own_exact_hunks']=own
prior=[]
for p in (ROOT/'actual-input/prior-accepted/actual-at-accepted-MI').rglob('*.md'):
 path=str(p.relative_to(ROOT/'actual-input/prior-accepted/actual-at-accepted-MI'));b=p.read_bytes();a=(ROOT/'actual-input/actual'/path).read_bytes();assert a==b and identity(a)['git_blob']==mt[path]['git_blob'];prior.append({'path':path,**identity(a),'same_as_prior_accepted_MI':True})
assert len(prior)==5;receipt['prior_five']=prior
receipt['own_shared_preservation_checks']=read_json(ROOT/'actual-plans/R7-U06.json')['shared_preservation_checks']
assert not receipt['own_shared_preservation_checks'];assert all(f['contributors']==['R7-U06'] for f in own)
receipt['journal_scope']={'batches':j['ordered_batches'],'items':len(j['required_ids']),'hunks':sum(len(x['hunks']) for x in j['files']),'targets':len(j['files']),'same_boundary':j['same_boundary_insertions'],'root_adjustments':j['root_administrative_reception_adjustments'],'qualification':'U06 four complete shared target files have no other current batch contributor. Other batches not granted new semantic PASS.'}
assert receipt['journal_scope']['hunks']==56 and len(j['files'])==24
# Verify original member locators, byte slices and canonical JSON independently.
contract=read_json(ROOT/'original/dispatch/delegation/contracts/R7-U06.json')
normalized=read_json(ROOT/'original/evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json')
raws={p.stem:p.read_bytes() for d in ['original','supplement'] for p in (ROOT/d/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs').glob('*.raw')}
def pointer(doc,path):
 for k in path.lstrip('/').split('/'):
  k=k.replace('~1','/').replace('~0','~');doc=doc[int(k)] if isinstance(doc,list) else doc[k]
 return doc
refs=[]
def walk(x):
 if isinstance(x,dict):
  if all(k in x for k in ['input_sha256','json_pointer','canonical_sha256']):refs.append(x)
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(contract)
for i in [12,13]:walk(normalized['records'][i])
checked=[];missing=[]
for ref in refs:
 sha=ref['input_sha256']
 if sha not in raws:missing.append(ref);continue
 data=raws[sha];assert hashlib.sha256(data).hexdigest()==sha
 obj=pointer(json.loads(data),ref['json_pointer']);canon=json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode();assert hashlib.sha256(canon).hexdigest()==ref['canonical_sha256'],ref
 if 'raw_member_byte_offsets' in ref:
  a,b=ref['raw_member_byte_offsets'];part=data[a:b];assert len(part)==ref['raw_member_bytes'] and hashlib.sha256(part).hexdigest()==ref['raw_member_sha256']
 checked.append({'input_sha256':sha,'pointer':ref['json_pointer'],'canonical_sha256':ref['canonical_sha256'],'raw_slice_verified':'raw_member_byte_offsets' in ref})
receipt['original_bindings']={'checked':checked,'missing':missing};assert not missing
receipt['constant_arithmetic']={'BU_bases':[5+95//10,5+10//10],'TK_evaluation_bases':[10,20,30],'water_level_factor':2*20//5+2,'water_base':((2*20//5+2)*40*33//55)//50+2,'water_damage':18,'HP':82,'PP':4,'speed_stage2':35*4//2,'speed_stage6':35*8//2,'speed_requests':{'-4':2,'0':6,'5':6,'6':'NO_RISE'},'kind':'Independent constants only; no battle/reference model or vector execution'}
out=ROOT/'bootstrap-evidence/actual-byte-audit.json';out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'formal_counts':receipt['formal_counts'],'own_files':len(own),'own_hunks':6,'prior_preserved':len(prior),'original_bindings_checked':len(checked),'missing_bindings':len(missing),'result':'BYTE_SCOPE_BINDING_CHECKS_COMPLETE_NO_SEMANTIC_CREDIT'},ensure_ascii=False))
