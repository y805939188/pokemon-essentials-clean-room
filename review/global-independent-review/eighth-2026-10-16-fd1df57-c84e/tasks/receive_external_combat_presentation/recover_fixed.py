"""Exact-commit remote recovery. Restored text and scripts are inert, never executed."""
from pathlib import Path
import subprocess,json,hashlib,datetime
TASK=Path(__file__).resolve().parent
ROOT=TASK.parents[1]
READSET=ROOT/'delegation/readsets/receive_external_combat_presentation.complete.json'
D=json.loads(READSET.read_text()); C=D['target_commit']; PREFIX=str(Path(D['files'][0]['remote_path_at_target_commit']).parent)+'/'
G=Path('/tmp/r8-cp-reception-target-01.git')
assert not G.exists()
E=[]
def run(args,check=True):
 s=datetime.datetime.now(datetime.timezone.utc).isoformat(); p=subprocess.run(args,capture_output=True)
 E.append({'args':args,'start_utc':s,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':p.returncode,'stdout':p.stdout.decode('utf8','backslashreplace') if len(p.stdout)<30000 else '[binary/large output retained by identity]','stderr':p.stderr.decode('utf8','backslashreplace')})
 if check: assert p.returncode==0,(args,p.stderr)
 return p.stdout
run(['git','init','--bare',str(G)])
run(['git','--git-dir='+str(G),'remote','add','origin','https://github.com/y805939188/pokemon-essentials-clean-room.git'])
run(['git','--git-dir='+str(G),'config','remote.origin.promisor','true'])
run(['git','--git-dir='+str(G),'config','remote.origin.partialclonefilter','blob:none'])
run(['git','--git-dir='+str(G),'fetch','--no-tags','--filter=blob:none','--depth=1','origin',C])
tree=run(['git','--git-dir='+str(G),'rev-parse',C+'^{tree}']).decode().strip(); assert tree==D['target_checkout_tree']
listing=run(['git','--git-dir='+str(G),'ls-tree','-rz',C,'--',PREFIX])
rows={}
for row in listing.split(b'\0'):
 if not row:continue
 meta,path=row.split(b'\t',1); mode,typ,oid=meta.decode().split();assert typ=='blob';rows[path.decode()]=(mode,oid)
assert set(rows)=={r['remote_path_at_target_commit'] for r in D['files']}
dest=TASK/'recovered'/C;assert not dest.exists();dest.mkdir(parents=True)
out=[]
for r in D['files']:
 mode,oid=rows[r['remote_path_at_target_commit']];assert mode==r['mode'] and oid==r['git_blob']
 raw=run(['git','--git-dir='+str(G),'cat-file','blob',oid]); assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256']
 assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==oid
 p=dest/r['relative_to_target_task'];p.parent.mkdir(exist_ok=True,parents=True);p.write_bytes(raw)
 out.append({**r,'local_path':str(p.relative_to(TASK)),'verified':True})
tasktree=run(['git','--git-dir='+str(G),'rev-parse',C+':'+PREFIX.rstrip('/')]).decode().strip();assert tasktree==D['target_task_tree_observed_from_fixed_commit']
receipt={'schema':'gr8-cp-exact-recovery/v1','status':'VERIFIED_IDENTITY_ONLY','commit':C,'checkout_tree':tree,'task_tree':tasktree,'remote_independent_bare':str(G),'no_seed_no_alternates':True,'fetch_shallow_blob_filter':'blob:none; each target payload subsequently fetched and read in full','files':out,'count':len(out),'bytes':sum(r['bytes']for r in out),'events':E,'semantic_credit':0,'recovered_code_executed':False,'UPDATE_NOT_STARTED':True}
(TASK/'recovery.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k]for k in ['status','commit','checkout_tree','task_tree','count','bytes']}))
