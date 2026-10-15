"""Independent byte/scope/binding checks; this is not a behavior executor."""
import datetime,difflib,hashlib,json,pathlib,subprocess
repo=pathlib.Path('/workspace/pokemon-essentials-clean-room');out=pathlib.Path(__file__).resolve().parents[1]
context=pathlib.Path('/workspace/r7-context/R7-U11-reviewer');bootstrap=pathlib.Path('/workspace/r7-review-bootstrap/R7-U11-r1');candidate=pathlib.Path('/workspace/r7-review-input/R7-U11-r1-f151a507bb43e8c936845c7408ab4bc14138caf0/candidate')
B='e646432c644dec04d306842cc5a559a29c718fbc';C='f151a507bb43e8c936845c7408ab4bc14138caf0'
def git(*a):return subprocess.check_output(['git','-C',str(repo),*a])
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def save(name,d):(out/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
freeze=json.loads((bootstrap/'candidate-input.json').read_bytes());plan=json.loads((bootstrap/'candidate-restore/R7-U11.json').read_bytes())
assert git('rev-parse',C+'^{tree}').decode().strip()==freeze['candidate_tree']
rows=[]
for r in freeze['candidate_and_author_evidence_file_identities']:
 p=r['path'];b=(candidate/p).read_bytes();actual=ident(b)
 assert actual=={k:r[k] for k in actual},p
 assert git('show',C+':'+p)==b,p
 mode,typ,blob,path=git('ls-tree',C,'--',p).decode().strip().split(maxsplit=3);assert (mode,typ,blob,path)==('100644','blob',actual['git_blob'],p)
 rows.append({'path':p,**actual,'mode':mode})
assert len(rows)==57 and sum(r['bytes'] for r in rows)==1112365
changes=[x.split('\t') for x in git('diff','--name-status',B,C).decode().splitlines()]
assert changes==[[r['status'],r['path']] for r in freeze['complete_diff_against_B']]
assert all(s=='A' and p.startswith('candidates/R7-U11/') for s,p in changes)
assert sorted(r['path'] for r in rows)==sorted(p for s,p in changes)
assert {r['path']:r['bytes'] for r in rows}=={r['path']:r['bytes'] for r in plan['artifacts']}
mirrors=[];patch=''
for r in freeze['candidate_and_author_evidence_file_identities']:
 if r['role']!='candidate_mirror':continue
 p=r['formal_target'];b=git('show',B+':'+p);c=(candidate/r['path']).read_bytes();assert ident(b)==r['base_B_identity_or_explicit_new_file'];assert b==(context/'inputs/project'/p).read_bytes()
 a=b.decode().splitlines(keepends=True);z=c.decode().splitlines(keepends=True);ops=[{'kind':tag,'B_lines':[i+1,j],'candidate_lines':[k+1,l]} for tag,i,j,k,l in difflib.SequenceMatcher(a=a,b=z,autojunk=False).get_opcodes() if tag!='equal']
 patch+=''.join(difflib.unified_diff(a,z,fromfile='a/'+p,tofile='b/'+p))
 mirrors.append({'formal_target':p,'candidate_path':r['path'],'B_identity':ident(b),'candidate_identity':ident(c),'changes':ops})
assert patch.encode()==(bootstrap/'mirror-diffs.patch').read_bytes()
wp='deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md';b=git('show',B+':'+wp).decode();c=(candidate/('candidates/R7-U11/'+wp)).read_text()
def section(t,start,end):return t.split(start,1)[1].split(end,1)[0]
for s,e in [('### 12.4','## 13.'),('## 18.','__END__')]:assert section(b,s,e)==section(c,s,e)
tc='deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md';assert (candidate/('candidates/R7-U11/'+tc)).read_bytes().startswith(git('show',B+':'+tc))
mat=[r for r in mirrors if r['formal_target']=='planning/feature-matrix.md'][0];assert mat['changes']==[{'kind':'replace','B_lines':[259,259],'candidate_lines':[259,259]}]
# Validate original pointers against independently restored source payloads.
rawroot=context/'evidence/tasks/R7-C13';bindings={r['binding_id']:r for r in json.loads((rawroot/'raw-binding-manifest.json').read_bytes())}
files={p.stem:p.read_bytes() for p in (rawroot/'inputs/tasks/R7-P02/evidence/inputs').glob('*.raw')};files.update({p.stem:p.read_bytes() for p in pathlib.Path('/workspace/r7-review-supplement/R7-U11-r1').glob('*.raw')})
norm=json.loads((rawroot/'inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes());checks=[]
def pointer(d,p):
 for v in p.split('/')[1:]:
  v=v.replace('~1','/').replace('~0','~');d=d[int(v)] if isinstance(d,list) else d[v]
 return d

def walk(d,loc):
 if isinstance(d,dict):
  if all(k in d for k in ('binding_id','json_pointer','input_sha256')):
   data=files[d['input_sha256']];r=bindings[d['binding_id']];assert r['sha256']==d['input_sha256'];assert ident(data)=={'bytes':r['bytes'],'sha256':r['sha256'],'git_blob':r['content_git_blob']}
   v=pointer(json.loads(data),d['json_pointer']);canonical=json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode();assert hashlib.sha256(canonical).hexdigest()==d['canonical_sha256'],loc
   if 'raw_member_byte_offsets' in d:
    lo,hi=d['raw_member_byte_offsets'];fragment=data[lo:hi];assert len(fragment)==d['raw_member_bytes'];assert hashlib.sha256(fragment).hexdigest()==d['raw_member_sha256'];assert json.loads(fragment)==v
   checks.append({'location':loc,'binding_id':d['binding_id'],'json_pointer':d['json_pointer'],'canonical_sha256':d['canonical_sha256'],'matched':True})
  for k,v in d.items():walk(v,loc+'/'+k)
 elif isinstance(d,list):
  for i,v in enumerate(d):walk(v,loc+'/'+str(i))
for i in (20,22):walk(norm['records'][i],'/records/'+str(i))
save('input-byte-audit.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate_commit':C,'candidate_tree':freeze['candidate_tree'],'files':rows,'files_verified':len(rows),'bytes_verified':sum(r['bytes'] for r in rows),'complete_B_diff':changes,'mirror_diff_exact':True,'mirror_changes':mirrors,'WP75_12_4_and_18_unchanged':True,'catalog_B_full_prefix_unchanged':True,'matrix_only_F18_04_note':True,'qualification':'TOOL_VALIDATION_ONLY'})
save('original-binding-audit.json',{'checks':checks,'count':len(checks),'qualification':'Original byte span/canonical JSON binding checks; not inherited semantic PASS.'})
print(json.dumps({'candidate_files':len(rows),'bytes':sum(r['bytes'] for r in rows),'mirrors':len(mirrors),'bound_original_references':len(checks),'scope':'EXACT','behavior_vectors':'NOT_EXECUTED'}))
