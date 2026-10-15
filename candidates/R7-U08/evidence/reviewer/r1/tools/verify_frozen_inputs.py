"""Independent byte/scope checks only; never execute source or author programs."""
import datetime,difflib,hashlib,json,os,pathlib,subprocess
W=pathlib.Path('/workspace/r7-u08-reviewer');O=W/'candidates/R7-U08/evidence/reviewer/r1'
P=pathlib.Path('/workspace/pokemon-essentials-clean-room');X=pathlib.Path('/workspace/r7-context/R7-U08-reviewer')
D=pathlib.Path('/workspace/r7-review-input/R7-U08-r1-d6e07340aa14eb8b45728020cad018a22d7559b2');C=D/'candidate'
F=pathlib.Path('/workspace/r7-review-bootstrap/R7-U08-r1/freeze')
B='e646432c644dec04d306842cc5a559a29c718fbc';A='d6e07340aa14eb8b45728020cad018a22d7559b2';Z='aa369555b0e8b6c8b077f964b54ed63d3b924f26';H='95c260d8f3fb4a171675dde877137fcd4c2f1c8d'
def git(*a):return subprocess.check_output(['git','-C',str(P),*a])
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def match(b,row):
 d=ident(b)
 for k,v in d.items():
  key='git_blob_content_id' if k=='git_blob' and 'git_blob_content_id' in row else k
  if key in row: assert v==row[key],(k,row)
 return d
freeze=json.loads((F/'candidate-input.json').read_bytes())
assert freeze['candidate_commit']==A and freeze['fixed_B']==B
assert git('rev-parse',A+'^{tree}').decode().strip()==freeze['candidate_tree']=='ed37cf1d27414f8f7411f079f1f717e55f3213a3'
assert git('rev-parse',Z+'^{tree}').decode().strip()=='08bd0f362c74ef7645b5bbd70b557489c122ae29'
assert git('rev-parse',B+':deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
assert git('rev-parse',A+':deliverables/final-specification-set')==git('rev-parse',B+':deliverables/final-specification-set')
frozen_meta=[]
for f in ['candidate-input.json','remote-readback.json','mirror-diffs.patch']:
 b=(F/f).read_bytes();loc='review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U08/'+f
 assert ident(b)['git_blob']==git('rev-parse',Z+':'+loc).decode().strip()
 frozen_meta.append({'commit':Z,'path':loc,**ident(b)})
tree={}
for row in git('ls-tree','-rz',A,'--','candidates/R7-U08').split(b'\0'):
 if row:
  meta,p=row.split(b'\t');mode,typ,blob=meta.decode().split();assert typ=='blob' and mode=='100644';tree[p.decode()]={'mode':mode,'blob':blob}
rows=freeze['candidate_and_author_evidence_file_identities'];expected={r['path'] for r in rows}
assert set(tree)==expected and len(rows)==113
changes=[]
for row in git('diff','--no-renames','--name-status','-z',B,A).split(b'\0'):
 if row:changes.append(row.decode())
actual_diff=[{'status':changes[i],'path':changes[i+1]} for i in range(0,len(changes),2)]
assert actual_diff==freeze['complete_diff_against_B'] and all(r['status']=='A' for r in actual_diff)
files=[]
for row in rows:
 p=C/row['path'];b=p.read_bytes();d=match(b,row);assert tree[row['path']]['blob']==d['git_blob']
 files.append({'path':row['path'],'mode':'100644',**d,'role':row['role']})
assert sum(r['bytes'] for r in files)==1198309
assert {str(p.relative_to(C)) for p in (C/'candidates/R7-U08').rglob('*') if p.is_file()}==expected
plans=[(pathlib.Path('/workspace/r7-bootstrap/R7-U08-reviewer/recovery/batches/R7-U08.json'),X),(pathlib.Path('/workspace/r7-review-bootstrap/R7-U08-r1/candidate-restore/R7-U08.json'),D)]
restores=[]
for plan,dest in plans:
 d=json.loads(plan.read_bytes());rr=[]
 for row in d['artifacts']+d['evidence']+d['fixed_read_inputs']:
  p=dest/row['local_path'];rr.append({'path':str(p),**match(p.read_bytes(),row)});p.chmod(p.stat().st_mode & ~0o222)
 restores.append({'plan':str(plan),'plan_identity':ident(plan.read_bytes()),'files':len(rr),'bytes':sum(x['bytes'] for x in rr),'identities':rr})
cs=json.loads((X/'dispatch/delegation/contracts/R7-U08.json').read_bytes());match((X/'dispatch/delegation/contracts/R7-U08.json').read_bytes(),freeze['original_contract_commit_path_identity'])
assert freeze['author_task_id']=='01a13f7f-ac68-740b-922a-7bf690ebb024'
assert os.environ['CODEX_THREAD_ID']!=freeze['author_task_id']
mirrors=[]
for row in rows:
 if row['role']!='candidate_mirror':continue
 p=row['formal_target'];base=(X/'inputs/project'/p).read_bytes();candidate=(C/row['path']).read_bytes();match(base,row['base_B_identity_or_explicit_new_file'])
 assert ident(base)['git_blob']==git('rev-parse',B+':'+p).decode().strip()
 old=base.decode().splitlines(keepends=True);new=candidate.decode().splitlines(keepends=True)
 operations=[{'kind':t,'base_lines':[i+1,j],'candidate_lines':[k+1,l]} for t,i,j,k,l in difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes() if t!='equal']
 if p.endswith('wp67-a-battle-interaction-and-presentation.md'):
  assert len(old)==len(new)==348 and {i+1 for i,(a,b) in enumerate(zip(old,new)) if a!=b}=={196,247,248}
  for i in [196,248]:assert new[i-1]==old[i-1].replace('闪白','闪光')
 elif p.endswith('wp67-b-lifecycle-presentations-and-history.md'):
  assert len(old)==len(new)==213 and {i+1 for i,(a,b) in enumerate(zip(old,new)) if a!=b}=={141}
 else:
  assert len(old)==1026 and len(new)==1030
  assert [x.split('|')[1].strip() for x in new[398:402]]==['R7-U08-HP01','R7-U08-HP02','R7-U08-HP03','R7-U08-HP04']
  reduced=new[:398]+new[402:];assert {i+1 for i,(a,b) in enumerate(zip(old,reduced)) if a!=b}=={440}
 mirrors.append({'path':row['path'],'formal_target':p,'base_identity':ident(base),'candidate_identity':ident(candidate),'operations':operations,'all_other_bytes_preserved':True})
manifest=json.loads((C/'candidates/R7-U08/evidence/author/artifact-manifest.json').read_bytes())
for row in manifest['supporting_evidence']:match((C/row['path']).read_bytes(),row)
for row in manifest['mirrors']:
 match((C/row['candidate_path']).read_bytes(),row['candidate']);match((X/'inputs/project'/row['base_path']).read_bytes(),row['base'])
# Validate original raw spans referenced by all four complete seven-group contracts.
raws={}
for p in (X/'evidence').rglob('*'):
 if p.is_file() and p.suffix!='gz':raws[hashlib.sha256(p.read_bytes()).hexdigest()]=p
spans=[]
def walk(x):
 if isinstance(x,dict):
  if all(k in x for k in ['input_sha256','raw_member_byte_offsets','raw_member_bytes','raw_member_sha256']):
   p=raws[x['input_sha256']];a,b=x['raw_member_byte_offsets'];bb=p.read_bytes()[a:b]
   assert len(bb)==x['raw_member_bytes'] and hashlib.sha256(bb).hexdigest()==x['raw_member_sha256']
   spans.append({'path':str(p),'offsets':[a,b],'bytes':len(bb),'sha256':x['raw_member_sha256'],'pointer':x.get('json_pointer')})
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(cs)
author=json.loads((C/'candidates/R7-U08/evidence/author/per-id.json').read_bytes())
checks=[]
for a,c in zip(author['records'],cs['original_full_contracts']):
 g=c['complete_seven_groups'];assert a['id']==c['record_id']
 for key,gkey in [('full_premises_and_paths','二_证据_前提_反例_四路径'),('minimum_contract_and_preserved_scope','三_最小修订_正确保留'),('historical_and_dependency_qualification','五_独立裁决及历史')]:assert a[key]==g[gkey]
 assert a['read_set']==g['六_依赖接收_精确读写集']['读取义务']['items'] and a['optional_changes_adopted']==[]
 assert all(v['execution']=='NOT_EXECUTED' for v in a['vectors'])
 checks.append({'id':a['id'],'contract_fields_equal':True,'optional_adoption':[],'vectors':[v['id'] for v in a['vectors']]})
receipt={'schema':'r7.u08.reviewer-input-receipt.v1','observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer_thread_id':os.environ['CODEX_THREAD_ID'],'reviewer_context':'/root','author_external_task':freeze['author_task_id'],'author_internal_task':'NOT_EXPOSED_TO_AUTHOR_CONTEXT; retained','distinct_visible_ids':True,'dispatch_commit':H,'dispatch_tree':git('rev-parse',H+'^{tree}').decode().strip(),'freeze_commit':Z,'freeze_tree':git('rev-parse',Z+'^{tree}').decode().strip(),'candidate_commit':A,'candidate_tree':freeze['candidate_tree'],'B':B,'frozen_metadata':frozen_meta,'candidate_files':files,'candidate_counts':freeze['counts'],'complete_diff':actual_diff,'restorations':restores,'raw_span_checks':spans,'mirror_scope_checks':mirrors,'author_manifest_declared_evidence_checked':len(manifest['supporting_evidence']),'author_contract_copy_checks':checks,'status':'ALL_BYTES_TREE_MODE_SCOPE_MATCH','semantic_credit_from_this_tool':False,'execution':'TOOL_VALIDATION_ONLY; no author/reference/native program executed'}
(O/'review-input-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['status','dispatch_tree','freeze_tree','candidate_tree','candidate_counts','mirror_scope_checks']},ensure_ascii=False,indent=2))
