"""Independent byte, scope and binding audit. No domain behavior is executed."""
from pathlib import Path
import datetime, difflib, gzip, hashlib, json, re, subprocess
REPO=Path('/workspace/r7-ir-result')
OUT=Path(__file__).parent
P='review/remediation-seventh-20261015-prepare/'
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='b0eea808887a688d52d28390ac8886fed9c10bcf'
FI='d9021aa2d704476f644ef15f1a3b8291653ff8f1'
D='95c260d8f3fb4a171675dde877137fcd4c2f1c8d'
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def get(c,p):return git('show',f'{c}:{p}')
def ident(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
def check(data,row):
 a=ident(data)
 for k,v in a.items():
  key='git_blob_content_id' if k=='git_blob' and 'git_blob_content_id' in row else k
  if key in row:assert v==row[key],(key,v,row[key])
 return a
def dump(name,obj):(OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
inputs=json.loads(get(FI,P+'integration/U04-U05/v1/integrated-input.json'))
assert git('rev-parse',MI+'^{tree}').decode().strip()==inputs['actual_integration_tree']
assert git('rev-parse',MI+':deliverables/final-specification-set').decode().strip()==inputs['actual_formal_subtree']
assert git('rev-parse',FI+'^{tree}').decode().strip()=='7efe118d11965ea842b5522cfa9dd7a8c7842d2d'
checks=[]
for kind in ['original','actual']:
 for b in ['U04','U05']:
  plan_path=Path('/workspace/r7-ir-bootstrap')/(kind+'-plans')/('R7-'+b+'.json')
  plan=json.loads(plan_path.read_bytes())
  c='658488c81f1f3181a488298ab27850c8af951d73' if kind=='original' else FI
  p=P+('recovery/batches/' if kind=='original' else 'integration/U04-U05/v1/integrated-restore/')+('R7-'+b+'.json')
  assert plan_path.read_bytes()==get(c,p)
  root=Path('/workspace/r7-ir-'+('context' if kind=='original' else 'actual'))/b
  rows=plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']
  for row in rows:
   data=(root/row['local_path']).read_bytes();check(data,row)
   # All project locators are checked against actual immutable Git objects too.
   if row['repository']=='y805939188/pokemon-essentials-clean-room':assert data==get(row['commit'],row['path']) if row not in plan['evidence'] else True
   if row in plan['evidence']:
    encoded=(root/'transport'/row['transport_path']).read_bytes();check(encoded,row['encoded_identity']);assert gzip.decompress(encoded)==data
  receipts=list(root.glob('recovery-receipt-*.json'));assert len(receipts)==1
  receipt=json.loads(receipts[0].read_bytes());assert receipt['status']=='BOUNDED_RESTORE_BYTES_VERIFIED' and receipt['files_verified']==len(rows)
  (OUT/f'{kind}-{b}-recovery-receipt.json').write_bytes(receipts[0].read_bytes())
  checks.append({'plan':str(plan_path),'plan_identity':ident(plan_path.read_bytes()),'files':len(rows),'bytes':sum(r['bytes'] for r in rows),'all_exact':True,'encoded_objects_checked':len(plan['evidence'])})
# Verify every original seven-group raw span and canonical JSON binding.
bindings=[]
for b in ['U04','U05']:
 root=Path('/workspace/r7-ir-context')/b
 contract=json.loads((root/f'dispatch/delegation/contracts/R7-{b}.json').read_bytes())
 refs=[]
 def walk(x):
  if isinstance(x,dict):
   if all(k in x for k in ['input_sha256','json_pointer','canonical_sha256','raw_member_byte_offsets','raw_member_bytes','raw_member_sha256']):refs.append(x)
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(contract);seen=set()
 for r in refs:
  key=(r['input_sha256'],r['json_pointer'])
  if key in seen:continue
  seen.add(key)
  raw=next((root/'evidence').rglob(r['input_sha256']+'.raw')).read_bytes()
  lo,hi=r['raw_member_byte_offsets'];span=raw[lo:hi]
  assert len(span)==r['raw_member_bytes'] and hashlib.sha256(span).hexdigest()==r['raw_member_sha256']
  v=json.loads(raw)
  for token in r['json_pointer'].split('/')[1:]:
   token=token.replace('~1','/').replace('~0','~');v=v[int(token)] if isinstance(v,list) else v[token]
  assert json.loads(span)==v
  assert hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()==r['canonical_sha256']
  bindings.append({'batch':b,'pointer':r['json_pointer'],'input_sha256':r['input_sha256'],'span_and_canonical_match':True})
# Independently reconstruct the exact resulting bytes from the 11 named contributions.
journal=json.loads(get(MI,P+'integration/U04-U05/v1/applied-clauses.json'))
segments=[];expected_patch=[]
for op in journal['operations']:
 path=op['path'];base=get(B,path);actual=get(MI,path);candidate=get(op['source_candidate_commit'],op['source_candidate_path'])
 assert actual==candidate
 check(base,op['before']);check(actual,op['after'])
 b=base.splitlines(keepends=True);a=actual.splitlines(keepends=True);rebuilt=list(b)
 previous_b=previous_a=0
 for h in op['hunks']:
  s,e=h['base_lines_zero_half_open'];u,v=h['candidate_lines_zero_half_open']
  assert b[previous_b:s]==a[previous_a:u]
  check(b''.join(b[s:e]),h['removed_identity']);check(b''.join(a[u:v]),h['inserted_identity'])
  previous_b,previous_a=e,v
  segments.append({'id':h['hunk_id'],'path':path,'base_lines_zero_half_open':[s,e],'actual_lines_zero_half_open':[u,v],'outside_complement_before_equal':True,'removed':ident(b''.join(b[s:e])),'inserted':ident(b''.join(a[u:v]))})
 assert b[previous_b:]==a[previous_a:]
 for h in reversed(op['hunks']):
  s,e=h['base_lines_zero_half_open'];u,v=h['candidate_lines_zero_half_open'];rebuilt[s:e]=a[u:v]
 assert b''.join(rebuilt)==actual
 expected_patch.extend(difflib.unified_diff(base.decode().splitlines(True),actual.decode().splitlines(True),fromfile='a/'+path,tofile='b/'+path))
assert len(segments)==11
assert ''.join(expected_patch).encode()==get(MI,P+'integration/U04-U05/v1/actual-changes.patch')
formal='deliverables/final-specification-set'
formal_paths=git('ls-tree','-r','--name-only',MI,'--',formal).decode().splitlines();assert len(formal_paths)==131
paths=git('diff','--name-only',B,MI,'--',formal).decode().splitlines()
assert paths==sorted(inputs['all_cumulative_formal_diff_paths_against_B'])
assert paths==sorted(op['path'] for op in journal['operations'])
actual_identities=[]
for row in inputs['actual_integrated_files']:
 data=get(MI,row['path']);check(data,row);actual_identities.append({'path':row['path'],**ident(data)})
for row in inputs['unchanged_consumers']:
 data=get(MI,row['path']);assert data==get(B,row['path']);check(data,row)
# Full old evidence and all files outside the R7 preparation/candidate additions retain B bytes.
full=git('diff','--name-status',B,MI).decode().splitlines()
unexpected=[line for line in full if line.split('\t')[-1] not in paths and not line.split('\t')[-1].startswith((P,'candidates/R7-','review/global-independent-review/seventh-2026-10-14-e646432-7a91/'))]
assert not unexpected,{'unexpected_count':len(unexpected),'sample':unexpected[:5]}
assert all(line.startswith('A\t') or line.split('\t')[-1] in paths for line in full)
# Check every pre-existing table row survives byte-exactly in order, not just IDs.
rows_audit=[]
for op in journal['operations']:
 if '/test-catalog/' not in op['path']:continue
 old=[l for l in get(B,op['path']).splitlines(True) if l.startswith(b'|')];new=get(MI,op['path']).splitlines(True);pos=0
 for l in old:
  ix=new.index(l,pos);pos=ix+1
 rows_audit.append({'path':op['path'],'old_rows_retained_in_order':len(old),'exact':True})
combat=get(MI,paths[3]).decode() if 'combat-requirements-wp39' in paths[3] else get(MI,next(p for p in paths if 'combat-requirements-wp39' in p)).decode()
for prefix,n in [('BC',31),('SW',35)]:
 ids=re.findall(r'^\| ('+prefix+r'-\d+) \|',combat,re.M);assert ids==[f'{prefix}-{i:02}' for i in range(1,n+1)]
# Candidate and independent-review commits/trees and full directory manifests.
prior=[]
for binding in inputs['source_bindings']:
 for role,ck,tk,category,suffix in [('author','candidate_commit','candidate_tree','candidate','author'),('candidate-review','candidate_review_commit','candidate_review_tree','candidate-review','reviewer/r1')]:
  c=binding[ck];assert git('rev-parse',c+'^{tree}').decode().strip()==binding[tk]
  batch=binding['batch_id'];b=batch[-3:];scope=f'candidates/{batch}/'
  changed=git('diff','--name-only',B,c).decode().splitlines();assert all(p.startswith(scope) for p in changed)
  if role=='candidate-review':scope+=f'evidence/{suffix}/'
  listed=git('ls-tree','-r','--name-only',c,'--',scope).decode().splitlines()
  local=Path('/workspace/r7-ir-actual')/b/category
  for p in listed:assert (local/p).read_bytes()==get(c,p)
  manifest_path=next(local.rglob('artifact-manifest.json'));manifest=json.loads(manifest_path.read_bytes())
  manifest_rows=[]
  if 'evidence_inventory' in manifest:
   manifest_rows.extend({'path':p,**r} for p,r in manifest['evidence_inventory'].items())
   manifest_rows.extend({'path':r['path'],**r['candidate_identity']} for r in manifest['mirrors'])
  else:
   manifest_rows.extend({'path':r['path'],**r.get('new_identity',r)} for r in manifest['files'])
  for r in manifest_rows:check((local/r['path']).read_bytes(),r)
  assert len(manifest_rows)==len(listed)-1
  prior.append({'manifest_nonself_entries_verified':len(manifest_rows),'batch':batch,'role':role,'commit':c,'tree':binding[tk],'files_checked':len(listed),'entire_result_diff_within_candidate_scope':True,'all_local_restored_bytes_equal_actual_git_blobs':True})
for c in [B,MI,D]:assert not git('ls-tree','-r','--name-only',c,'--','.agents','.codex').strip()
result={'schema':'r7.ir-independent-byte-audit.v1','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_commit':D,'MI':MI,'MI_tree':inputs['actual_integration_tree'],'formal_subtree':inputs['actual_formal_subtree'],'FI':FI,'formal_count':131,'formal_changed_files':paths,'unchanged_formal_files':126,'restoration':checks,'original_binding_checks':bindings,'changed_segments':segments,'exact_patch_match':True,'prior_evidence':prior,'actual_file_identities':actual_identities,'unchanged_consumers_byte_match':inputs['unchanged_consumers'],'catalog_old_rows':rows_audit,'old_non_R7_evidence_bytes_preserved':True,'skills_in_fixed_trees':[],'scope':'TOOL_VALIDATION_ONLY; no semantic PASS or behavior execution','behavior_vectors':'NOT_EXECUTED','source_execution':0}
dump('input-audit.json',result)
(OUT/'frozen-integrated-input.json').write_bytes(get(FI,P+'integration/U04-U05/v1/integrated-input.json'))
print(json.dumps({'result':'BYTE_AND_SCOPE_CHECKS_PASS','restored_files':sum(x['files'] for x in checks),'original_bindings':len(bindings),'formal_files':131,'changed_files':len(paths),'segments':len(segments),'old_rows':rows_audit,'semantic_credit':False}))
