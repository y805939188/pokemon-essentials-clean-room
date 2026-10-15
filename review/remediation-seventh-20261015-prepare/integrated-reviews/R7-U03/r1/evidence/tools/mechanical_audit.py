import json, hashlib, subprocess, datetime, os, difflib, gzip
from pathlib import Path
root=Path('/workspace/r7-ir-R7-U03-final'); repo=Path('/workspace/pokemon-essentials-clean-room')
B='e646432c644dec04d306842cc5a559a29c718fbc'; MI='94d5eb73f4508b8a8a54319040faa9aea5752059'; FI='6a02773d62e36a295e9701a8d0ba5b5cb6441614'
def git(*a): return subprocess.check_output(['git',*a],cwd=repo)
def ident(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest())
def check(b,d):
 a=ident(b)
 for k in a:
  if k in d: assert a[k]==d[k],(k,a[k],d[k])
 return a
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'qualification':'TOOL_VALIDATION only; no behavior execution','commits':{},'restored':[]}
for c in [B,MI,FI,'5325e8046f4d625b855e3c216abaa650805fab5e','11bff8e7912a98de09691ad7d7b7a2d3194e2757','a8a65bc4f29e2b19c8b63fd59c9c2a0941be6520']:
 out['commits'][c]=git('rev-parse',c+'^{tree}').decode().strip()
for directory,plans in [('original','original-plans'),('actual-input','actual-plans')]:
 plan=json.loads(next((root/plans).glob('*.json')).read_text())
 for row in plan['artifacts']:
  # Some plans group artifacts by role; all concrete rows are walked below.
  pass
 def walk(v):
  if isinstance(v,dict):
   if 'local_path' in v and ('sha256' in v or 'expected_sha256' in v):yield v
   else:
    for x in v.values():yield from walk(x)
  elif isinstance(v,list):
   for x in v:yield from walk(x)
 rows=list(walk(plan))
 for r in rows:
  p=root/directory/r['local_path']; b=p.read_bytes();a=check(b,r)
  if 'git_blob_content_id' in r:assert a['git_blob']==r['git_blob_content_id']
  if r.get('repository')=='y805939188/pokemon-essentials-clean-room':
   stored=git('show',r['commit']+':'+r['path'])
   if 'encoded_identity' in r:
    enc=ident(stored);ei=r['encoded_identity'];assert enc['bytes']==ei['bytes'] and enc['git_blob']==ei['git_blob_content_id'];stored=gzip.decompress(stored)
   assert b==stored,(directory,r['local_path'],'Git bytes')
   mode=git('ls-tree',r['commit'],'--',r['path']).decode().split()[0];assert mode=='100644'
  out['restored'].append(dict(path=str(p.relative_to(root)),**a))
out['restored_count']=len(out['restored'])
fi=json.loads((root/'supplement/integration/wave4/v1/integrated-input.json').read_text())
formal=[]
for r in fi['all_formal_file_identities']:
 p=r['path'];bb=git('show',B+':'+p);mb=git('show',MI+':'+p);check(bb,r['base_B_identity']);check(mb,r)
 assert (bb!=mb)==r['changed_against_B']
 formal.append(dict(path=p,changed=bb!=mb,baseline=ident(bb),actual=ident(mb)))
out['formal131']=formal;out['formal_changed']=sum(x['changed'] for x in formal);out['formal_unchanged']=len(formal)-out['formal_changed']
assert len(formal)==131 and out['formal_changed']==33
out['formal_tree']=git('rev-parse',MI+':deliverables/final-specification-set').decode().strip()
assert out['formal_tree']=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
j=json.loads((root/'actual-input/integration/applied-clauses.json').read_text());checks=[]
allfiles=j['cumulative_files'];out['hunks']=[]
for f in allfiles:
 p=f['path']; exists=bool(git('ls-tree',B,'--',p));bb=git('show',B+':'+p) if exists else b'';check(bb,f['baseline_identity']);mb=git('show',MI+':'+p);bl=bb.decode().splitlines(keepends=True); rebuilt=[];cursor=0
 for h in f['hunks']:
  a,z=h['base_line_indices_half_open'];ca,cz=h['candidate_line_indices_half_open'];added=h['added_text'];removed=h['removed_text']
  assert ''.join(bl[a:z])==removed,(p,a,z,'base')
  cb=git('show',h['candidate_commit']+':'+h['candidate_path']);cl=cb.decode().splitlines(keepends=True)
  assert ''.join(cl[ca:cz])==added,(p,'candidate slice')
  assert a>=cursor,(p,'overlap',a,cursor)
  rebuilt.extend(bl[cursor:a]);rebuilt.append(added);cursor=z
  check(removed.encode(),h['removed_identity']);check(added.encode(),h['added_identity'])
  if 'actual_final_line_indices_half_open' in h and not p.endswith('current-navigation-errata.json'):
   ma,mz=h['actual_final_line_indices_half_open'];assert ''.join(mb.decode().splitlines(keepends=True)[ma:mz])==added,(p,'actual position')
  out['hunks'].append(dict(path=p,batch=h['batch_id'],base_lines=[a,z],candidate_commit=h['candidate_commit'],candidate_path=h['candidate_path'],candidate_lines=[ca,cz],added=ident(added.encode()),removed=ident(removed.encode())))
 rebuilt.extend(bl[cursor:]);assembled=''.join(rebuilt).encode();expected=f.get('assembled_candidate_clauses_identity',f.get('actual_final_identity'))
 if expected:check(assembled,expected)
 if assembled!=mb and p.endswith('current-navigation-errata.json'):
  before=json.loads(assembled);after=json.loads(mb);changes=[]
  for keys in [('status',),('reception','candidate_review'),('reception','shared_integration')]:
   v=before;w=after
   for k in keys[:-1]:v=v[k];w=w[k]
   changes.append(dict(pointer='/'+'/'.join(keys),before=v[keys[-1]],after=w[keys[-1]]));v[keys[-1]]=w[keys[-1]]
  assert before==after and after['reception']['ACCEPTED'] is False and after['reception']['CLOSED'] is False
  out['errata_phase_adjustments']=changes
 elif assembled!=mb:
  adjustments=[a for a in j['root_administrative_adjustments'] if a['path']==p];assert len(adjustments)==1,(p,'unexpected difference')
  adj=adjustments[0];assert assembled+adj['added_text'].encode()==mb,(p,'root pointer')
 checks.append(dict(path=p,hunks=len(f['hunks']),contributors=sorted(set(h['batch_id'] for h in f['hunks'])),actual=ident(mb)))
out['assembled_files']=checks;out['hunk_count']=len(out['hunks']);assert out['hunk_count']==86
out['new_u03_hunks']=sum(h['batch']=='R7-U03' for h in out['hunks']);assert out['new_u03_hunks']==14
out['previous72_preserved']=len(out['hunks'])-out['new_u03_hunks']==72
prev='b0eea808887a688d52d28390ac8886fed9c10bcf';protected=[p.decode().split('\t')[1] for p in git('ls-tree','-r',prev,'--','deliverables/final-specification-set').splitlines() if p.decode().split('\t')[1] in j['older_U04_U05_11_hunks_preserved'].get('paths',[])] if isinstance(j['older_U04_U05_11_hunks_preserved'],dict) else ['deliverables/final-specification-set/'+p for p in ['combat-requirements/wp39-battle-context-and-participants.md','combat-requirements/wp41-switching-positioning-and-escape.md','pokemon-rules/wp34-inheritance-and-offspring.md','test-catalog/combat-requirements-wp39-40-41-42-45.md','test-catalog/pokemon-rules-wp19-21-22-23-34.md']]
out['protected_U04_U05']=[]
for p in protected:
 b=git('show',MI+':'+p);assert b==git('show',prev+':'+p);out['protected_U04_U05'].append(dict(path=p,**ident(b)))
norm=json.loads((root/'original/evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_text());bindings=json.loads((root/'original/evidence/tasks/R7-C13/raw-binding-manifest.json').read_text());by={r['binding_id']:r for r in bindings}
refs={}
def refs_walk(v):
 if isinstance(v,dict):
  if all(k in v for k in ['binding_id','json_pointer','raw_member_byte_offsets','canonical_sha256']):refs[(v['binding_id'],v['json_pointer'])]=v
  for x in v.values():refs_walk(x)
 elif isinstance(v,list):
  for x in v:refs_walk(x)
for r in norm['records'][6:8]:refs_walk(r)
out['raw_members']=[]
for (binding,pointer),r in refs.items():
 br=by[binding];p=root/'original/evidence/tasks/R7-C13'/br['c13_snapshot']
 if not p.exists():p=root/'supplement/original-bound'/br['report_relative_path']
 b=p.read_bytes();assert ident(b)['sha256']==r['input_sha256'];check(b,br);a,z=r['raw_member_byte_offsets'];slice_=b[a:z]
 assert len(slice_)==r['raw_member_bytes'] and hashlib.sha256(slice_).hexdigest()==r['raw_member_sha256']
 value=json.loads(b)
 for part in pointer.strip('/').split('/'):value=value[int(part)] if isinstance(value,list) else value[part.replace('~1','/').replace('~0','~')]
 assert json.loads(slice_)==value
 canonical=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
 assert hashlib.sha256(canonical).hexdigest()==r['canonical_sha256'],(binding,pointer,'canonical')
 out['raw_members'].append(dict(binding_id=binding,json_pointer=pointer,offsets=[a,z],bytes=len(slice_),sha256=r['raw_member_sha256'],canonical_sha256=r['canonical_sha256'],input_identity=ident(b),local_path=str(p.relative_to(root))))
out['raw_member_count']=len(out['raw_members']);assert out['raw_member_count']==149
(root/'audit/mechanical-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k in ['commits','restored_count','formal_changed','formal_unchanged','formal_tree','hunk_count','new_u03_hunks','previous72_preserved','raw_member_count']},indent=2))
