"""Check original member bindings and author evidence declarations independently."""
import datetime,hashlib,json,pathlib,re,subprocess
out=pathlib.Path(__file__).resolve().parents[1];ctx=pathlib.Path('/workspace/r7-context/R7-U02-reviewer');cand=pathlib.Path('/workspace/r7-review-input/R7-U02-r1-84e2cca132ada38405657f19cbbd3d6891d4794f/candidate');contract=json.loads((ctx/'dispatch/delegation/contracts/R7-U02.json').read_bytes())
rawroot=ctx/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs';validated=[]
def ptr(x,p):
 for k in p.strip('/').split('/'):
  k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
 return x
def walk(x):
 if isinstance(x,dict):
  if 'raw_member_byte_offsets' in x:
   d=(rawroot/(x['input_sha256']+'.raw')).read_bytes();a,b=x['raw_member_byte_offsets'];part=d[a:b]
   assert len(part)==x['raw_member_bytes'] and hashlib.sha256(part).hexdigest()==x['raw_member_sha256']
   v=ptr(json.loads(d),x['json_pointer']);assert json.loads(part)==v
   canonical=json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode();assert hashlib.sha256(canonical).hexdigest()==x['canonical_sha256']
   validated.append({'input_sha256':x['input_sha256'],'json_pointer':x['json_pointer'],'byte_range':[a,b],'raw_sha256':x['raw_member_sha256'],'pointer_and_canonical_match':True})
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(contract)
manifest=json.loads((cand/'candidates/R7-U02/evidence/author/artifact-manifest.json').read_bytes());files=[]
for row in manifest['files']:
 d=(cand/row['path']).read_bytes();e=row.get('candidate',row)
 assert len(d)==e['bytes'] and hashlib.sha256(d).hexdigest()==e['sha256']
 assert hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()==e['git_blob_content_id']
 if row.get('base_path'):
  base=subprocess.check_output(['git','show','e646432c644dec04d306842cc5a559a29c718fbc:'+row['base_path']]);assert hashlib.sha256(base).hexdigest()==row['base']['sha256']
 files.append(row['path'])
per=json.loads((cand/'candidates/R7-U02/evidence/author/per-id.json').read_bytes());cat=(cand/'candidates/R7-U02/deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md').read_text();v=[]
for row in per['records']:
 assert row['conditional_write_set']==[]
 for vector in row['candidate_vectors']:
  assert vector['execution']=='NOT_EXECUTED' and vector['host_result']=='NOT_OBSERVED'
  lines=[s for s in cat.splitlines() if s.startswith('| '+vector['id']+' |')];assert len(lines)==1
  for cell in vector['catalog_cells']:assert cell in lines[0]
  v.append({'id':vector['id'],'execution':'NOT_EXECUTED','catalog_matches_author_evidence':True})
assert len(v)==51
r={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'raw_bindings':validated,'author_declared_files_verified':files,'author_manifest_self_binding':'own identity bound by candidate commit/tree and independently checked exhaustive 63-file table','vectors':v,'semantic_credit':False,'qualification':'TOOL_VALIDATION; manual content verdict is separate.'}
(out/'binding-validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'raw_bindings_verified':len(validated),'author_declared_files_verified':len(files),'catalog_vector_rows_verified':len(v),'conditional_targets':0,'semantic_credit':False}))
