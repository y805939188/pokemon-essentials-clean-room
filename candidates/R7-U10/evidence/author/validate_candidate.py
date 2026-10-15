"""Bounded identity/scope/arithmetic audit only. Does not execute any reference/host/model."""
from pathlib import Path
import json,hashlib,subprocess,difflib,re,sys
ROOT=Path(__file__).resolve().parents[4]
CONTEXT=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/workspace/r7-context/R7-U10-author')
BOOT=Path('/workspace/r7-bootstrap/R7-U10-author')
B='e646432c644dec04d306842cc5a559a29c718fbc'
def ident(b):
 return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
def eq(b,row):
 a=ident(b)
 for k in a:
  if k in row:assert a[k]==row[k],(k,row.get('local_path'),a[k],row[k])
 return a
plan=json.loads((BOOT/'recovery/batches/R7-U10.json').read_text())
contract=json.loads((BOOT/'contracts/R7-U10.json').read_text())
verified=[]
for row in plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']:
 p=CONTEXT/row['local_path'];verified.append({'path':row['local_path'],**eq(p.read_bytes(),row)})
assert len(verified)==39
# Fixed input binding verification, including exact raw byte spans and canonical JSON pointers.
rawroot=CONTEXT/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'
raws={row['sha256']:(CONTEXT/row['local_path']).read_bytes() for row in plan['evidence']};checked={}
supp=Path('/workspace/r7-context/R7-U10-author-supplement')
sr=json.loads((supp/'receipt.json').read_text())
raws.update({row['sha256']:(supp/row['logical_path']).read_bytes() for row in sr['files'] if row['logical_path'].endswith('.raw')})
def pointer(obj,path):
 for k in path.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');obj=obj[int(k)] if isinstance(obj,list) else obj[k]
 return obj
def checkrefs(x):
 if isinstance(x,dict):
  if all(k in x for k in ('input_sha256','json_pointer','raw_member_byte_offsets')):
   key=(x['input_sha256'],x['json_pointer']);raw=raws[x['input_sha256']]
   assert hashlib.sha256(raw).hexdigest()==x['input_sha256']
   start,end=x['raw_member_byte_offsets'];part=raw[start:end]
   assert len(part)==x['raw_member_bytes'] and hashlib.sha256(part).hexdigest()==x['raw_member_sha256'],key
   obj=pointer(json.loads(raw),x['json_pointer'])
   canon=json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
   assert hashlib.sha256(canon).hexdigest()==x['canonical_sha256'],key
   checked[key]={'binding_id':x['binding_id'],'pointer':x['json_pointer'],'raw_sha256':x['input_sha256']}
  for v in x.values():checkrefs(v)
 elif isinstance(x,list):
  for v in x:checkrefs(v)
checkrefs(contract)
norm=json.loads((CONTEXT/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_text())
for idx in (19,27,21):checkrefs(norm['records'][idx])
supp=Path('/workspace/r7-context/R7-U10-author-supplement')
sr=json.loads((supp/'receipt.json').read_text())
for row in sr['files']:eq((supp/row['logical_path']).read_bytes(),row)
# These are restored prior decoder outputs, not a new decoder execution.
displays=[(supp/'tasks/R7-C06/logs'/name).read_text() for name in ('038-cil-decode.stdout','039-cil-helpers.stdout')]
assert sorted(int(x) for s in displays for x in re.findall(r'^METHOD (\d+) ',s,re.M))==list(range(1,16))
assert sum(len(re.findall(r'^EH_CLAUSE ',s,re.M)) for s in displays)==11
allowed=[r for r in contract['paths'] if r['classification']=='required']
hunks=[];mirrors=[]
allowed_old_ranges={
'audit/source-traceability.md':[(1473,1473)],
'planning/feature-matrix.md':[(258,258)],
'deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md':[(140,140),(164,164)],
'deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md':[(14,14),(17,17),(19,19),(460,464),(495,495)],
'deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md':[(139,139),(168,168),(391,391)]}
for row in allowed:
 old=git('show',B+':'+row['path']);new=(ROOT/row['candidate_path']).read_bytes()
 assert old==(CONTEXT/'inputs/project'/row['path']).read_bytes()
 oldlines=old.decode().splitlines(keepends=True);newlines=new.decode().splitlines(keepends=True)
 changes=[]
 for tag,a,b,c,d in difflib.SequenceMatcher(None,oldlines,newlines,autojunk=False).get_opcodes():
  if tag=='equal':continue
  # Insertions occur before old line a+1; replacements cover a+1..b.
  low=a+1;high=max(low,b)
  assert any(low>=l and high<=h for l,h in allowed_old_ranges[row['path']]),(row['path'],tag,low,high)
  changes.append({'kind':tag,'base_lines':[low,high],'candidate_lines':[c+1,max(c+1,d)]})
 mirrors.append({'original_path':row['path'],'candidate_path':row['candidate_path'],'base':ident(old),'new':ident(new),'changes':changes})
 hunks.append(''.join(difflib.unified_diff(oldlines,newlines,fromfile='B/'+row['path'],tofile=row['candidate_path'],n=3)))
cat=next(r for r in allowed if '/test-catalog/' in r['path'])
old=git('show',B+':'+cat['path']).decode();new=(ROOT/cat['candidate_path']).read_text()
for line in old.splitlines():
 if re.match(r'^\| (AN-M\d+|CV-M\d+) \|',line) and not line.startswith('| AN-M09 |'):
  assert line in new
for token in ('| AN-M09 |','| WE-M17 |'):assert old.count(token)==new.count(token)==1
assert len(re.findall(r'^\| TOOL-AN-\d+ \|',new,re.M))==17
# Meaningful independent arithmetic audit, not an executable editor/XML-tool behavior model.
arith={'n0':[960,192],'n6':[960,192*((6+4)//5)],'cell5':[192*(5%5),192*(5//5)],'slot0-56x68':[96-56,96-68,2*56,2*68],'slot1-56x68':[192+96-56,96-68,112,136]}
assert arith=={'n0':[960,192],'n6':[960,384],'cell5':[0,192],'slot0-56x68':[40,28,112,136],'slot1-56x68':[232,28,112,136]}
# The formal tree and all baseline tracked worktree files remain unchanged.
assert git('rev-parse',B+':deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
assert git('diff','--name-only',B,'--',':(exclude)candidates/R7-U10/').strip()==b''
extra=git('ls-files','--others','--exclude-standard','-z').split(b'\0')
assert all(not p or p.decode().startswith('candidates/R7-U10/') for p in extra)
assert not (ROOT/'candidates/R7-U10/specs').exists()
e=ROOT/'candidates/R7-U10/evidence/author'
result={'status':'TOOL_VALIDATION_OK_ONLY','restored_files':len(verified),'restored_bytes':sum(x['bytes'] for x in verified),'unique_raw_member_bindings':len(checked),'supplement_files':len(sr['files']),'restored_prior_methods':15,'restored_prior_EH_clauses':11,'mirror_count':len(mirrors),'mirrors':mirrors,'arithmetic':arith,'scope_check':'only authorized clauses in five complete mirrors; formal unchanged; conditional old source not activated','reference_or_host_execution':0,'behavior_vectors':'NOT_EXECUTED','independent_review':'NOT_PERFORMED'}
(e/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(e/'clause-diff.patch').write_text('\n'.join(hunks))
print(json.dumps({k:v for k,v in result.items() if k not in ('mirrors',)},ensure_ascii=False,indent=2))
