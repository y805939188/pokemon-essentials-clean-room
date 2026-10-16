"""Read-only Git/blob and reversible presentation validation; semantic credit is zero."""
from pathlib import Path
import subprocess,json,gzip,hashlib,re,collections,datetime,os
W=Path(__file__).resolve().parents[1];T=W.parents[2];F=T/'delegation/fanout-v1';P=T.parents[3];G=['git','--git-dir='+str(W/'.local/input.git')]
C='9abf7bfc87274fb37f08d9f77a1bcb53f53d3ecd';TARGET='11c057d9aed330c16312470f80f13d180f8e1e65';PREV='ab44ee8c5ffd53ded7d5bc37ae6f15e6ed3ba8d8'
def dump(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
def git(*a):return subprocess.check_output(G+list(a))
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ptr(x,p):
 for k in p.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');x=x[int(k)]if isinstance(x,list)else x[k]
 return x
assert git('rev-parse',TARGET+'^{tree}').decode().strip()=='2fcef25ee9903bd7e28dec21f6fc2d970c221f77'
prefix='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/external_h_early_qualifications'
assert git('rev-parse',TARGET+':'+prefix).decode().strip()=='bb0cb15506d2abc9e6b84abe1391048776de6997'
contract=json.loads((T/'contract/receive_external_h_early_qualifications.complete.json').read_text());rows=contract['files'];listing={}
for l in git('ls-tree','-r','-z',TARGET,'--',prefix).split(b'\0'):
 if l:
  meta,path=l.split(b'\t');mode,typ,oid=meta.decode().split();listing[path.decode()]=(mode,oid)
assert set(listing)=={r['remote_path_at_target_commit']for r in rows}
missing=[]
for r in rows:
 q=subprocess.run(G+['cat-file','-e',r['git_blob']],env=dict(os.environ,GIT_NO_LAZY_FETCH='1'),capture_output=True)
 if q.returncode:missing.append(r['git_blob'])
if missing:subprocess.run(G+['fetch','--no-tags','origin']+missing,check=True,capture_output=True)
verified=[]
for r in rows:
 assert listing[r['remote_path_at_target_commit']]==(r['mode'],r['git_blob']);actual=ident(git('cat-file','blob',r['git_blob']));assert all(actual[k]==r[k]for k in actual);verified.append({'path':r['remote_path_at_target_commit'],'mode':r['mode'],**actual})
assert len(verified)==357 and sum(x['bytes']for x in verified)==12034301
readset=json.loads((F/'shards/r5_u01_u02/readset.json').read_text());recovery=json.loads((W/'input-recovery.json').read_text());bysha={}
for row in recovery['files']:
 p=W/row.get('decoded_local_path',row['encoded_local_path']);bysha[row.get('actual_decoded',row['actual_encoded'])['sha256']]=p
H=json.loads(bysha['cf92051ba805dbb59d80cd6e12c27c920d7b0b6915308f0c0c4bb41a2dd9ee8c'].read_text());view=json.loads(bysha['5451b628b51540b6a93aac894fc22c6c35d672c18f1dd3a3ada0d5c14e817f2a'].read_text());D=H['R5']['original_and_current_percheck_value_dictionary'];assert all(D[k]==v for k,v in view['dictionary_entries_for_own_occurrences'].items())
bindings=[]
def expand(x,p,stack=()):
 if isinstance(x,str)and x in D:
  assert x not in stack;bindings.append({'occurrence':p,'dictionary_pointer':'/R5/original_and_current_percheck_value_dictionary/'+x,'original_reference':x,'resolved_value_sha256':ident(dump(D[x]))['sha256']});return expand(D[x],p,stack+(x,))
 if isinstance(x,dict):return {k:expand(v,p+'/'+k.replace('~','~0').replace('/','~1'),stack)for k,v in x.items()}
 if isinstance(x,list):return [expand(v,p+'/'+str(i),stack)for i,v in enumerate(x)]
 return x
originals={(x['source']['original_identity']['commit'],x['source']['original_identity']['path']):json.loads((W/x['decoded_local_path']).read_text())for x in recovery['files']if 'original_identity'in x['source']}
objects=[]
for i,o in enumerate(view['owned_complete_objects']):
 raw=o['raw_complete_object'];p=o['pointer']
 if 'source_logical_path'in o:assert ptr(H,p)==raw;assert expand(raw,p)==o['expanded_complete_object']
 else:
  origin=originals[(o['source_commit'],o['source_path'])]
  expect={k:v for k,v in origin.items()if k not in ('findings','criteria','records')}if p.startswith('/ (')else ptr(origin,p)
  assert expect==raw and raw==o['expanded_complete_object']
 objects.append({'index':i,**{k:v for k,v in o.items()if k not in ('raw_complete_object','expanded_complete_object')},'raw_identity':ident(dump(raw)),'expanded_identity':ident(dump(o['expanded_complete_object']))})
assert collections.Counter(dump(x)for x in bindings)==collections.Counter(dump(x)for x in view['dictionary_bindings'])
criteria=[u['criterion_id']for o in view['owned_complete_objects']if o['pointer'].startswith('/R5/current_root/records/')for u in o['expanded_complete_object']['schema_units']]
assert criteria==readset['primary_semantic_population']['R5_criteria'] and len(criteria)==294
write(W/'evidence/input-validation.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'contract_commit':C,'target':TARGET,'checkout_tree':'2fcef25ee9903bd7e28dec21f6fc2d970c221f77','target_task_tree':'bb0cb15506d2abc9e6b84abe1391048776de6997','collection':{'files':357,'bytes':12034301,'all_mode_blob_bytes_sha_match':True,'exact_set_match':True,'source_readset_identity':ident((T/'contract/receive_external_h_early_qualifications.complete.json').read_bytes())},'owned_objects':len(objects),'dictionary_bindings':len(bindings),'dictionary_entries':len(view['dictionary_entries_for_own_occurrences']),'criteria':len(criteria),'semantic_credit':0,'behavior_execution':0,'initial_recovery_failure':{'cause':'bare alternates supplied trees but partial-clone promisor missing for bed27f15 blob','exit':1,'preserved':True,'resolution':'configured the bare origin as promisor, reran the read and exact identities succeeded'}})
write(W/'.local/object-identities.json',objects)
# Reversible map: every scalar is retained with all object/path contexts. Presentation
# only coalesces equal values, and excludes exact navigation scalars by TYPE, never
# by business field names such as original_actual_text.
values=collections.OrderedDict()
def walk(x,p,oi,primary):
 if isinstance(x,dict):
  for k,v in x.items():walk(v,p+'/'+k,oi,primary)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,p+'/'+str(i),oi,primary)
 else:
  key=json.dumps(x,ensure_ascii=False);values.setdefault(key,{'value':x,'contexts':[]})['contexts'].append([oi,primary,p])
for i,o in enumerate(view['owned_complete_objects']):walk(o['expanded_complete_object'],'',i,o.get('primary_id','CONTEXT_ONLY'))
write(W/'.local/scalar-map.json',list(values.values()))
print(json.dumps({'verified_collection':357,'owned_objects':len(objects),'dictionary_bindings':len(bindings),'criteria':len(criteria),'scalar_groups_for_presentation_not_acceptance':len(values),'semantic_credit':0}))
