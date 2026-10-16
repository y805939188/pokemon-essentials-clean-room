"""Fresh-bare exact publication byte readback; no recovered content executed."""
from pathlib import Path
import subprocess,datetime,json,hashlib,sys
T=Path(__file__).resolve().parent;REPO=Path('/workspace/pokemon-essentials-clean-room');PREFIX=str(T.relative_to(REPO))
C=sys.argv[1];ATT=sys.argv[2];OUT=Path(sys.argv[3]);assert len(C)==40 and all(x in '0123456789abcdef'for x in C)
G=Path('/tmp')/('r8-cp-publication-'+ATT+'.git');assert not G.exists();events=[]
def call(args,save=True):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(args,capture_output=True)
 events.append({'args':args,'utc_start':start,'utc_end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':p.returncode,'stdout':p.stdout.decode('utf8','backslashreplace')if save else'Full bytes compared and identified below','stderr':p.stderr.decode('utf8','backslashreplace')});assert p.returncode==0,(args,p.stderr);return p.stdout
call(['git','init','--bare',str(G)])
call(['git','--git-dir='+str(G),'remote','add','origin','https://github.com/y805939188/pokemon-essentials-clean-room.git'])
call(['git','--git-dir='+str(G),'config','remote.origin.promisor','true'])
call(['git','--git-dir='+str(G),'config','remote.origin.partialclonefilter','blob:none'])
call(['git','--git-dir='+str(G),'fetch','--filter=blob:none','--depth=1','--no-tags','origin',C])
tree=call(['git','--git-dir='+str(G),'rev-parse',C+'^{tree}']).decode().strip();localtree=call(['git','rev-parse',C+'^{tree}']).decode().strip();assert tree==localtree
tasktree=call(['git','--git-dir='+str(G),'rev-parse',C+':'+PREFIX]).decode().strip();assert tasktree==call(['git','rev-parse',C+':'+PREFIX]).decode().strip()
remote=call(['git','--git-dir='+str(G),'ls-tree','-rz',C,'--',PREFIX+'/']);local=call(['git','ls-tree','-rz',C,'--',PREFIX+'/']);assert remote==local
rows=[];oids=[]
for row in remote.split(b'\0'):
 if not row:continue
 meta,path=row.split(b'\t',1);mode,typ,oid=meta.decode().split();assert mode=='100644'and typ=='blob';rows.append((mode,oid,path.decode()));oids.append(oid)
# Download missing blobs from remote together, then compare every complete byte stream.
# Each SHA is already bound by exact fetched tree. No local target cache or alternates.
call(['git','--git-dir='+str(G),'fetch','--no-tags','origin',*sorted(set(oids))],save=False)
files=[]
for mode,oid,path in rows:
 remote_raw=call(['git','--git-dir='+str(G),'cat-file','blob',oid],False)
 local_raw=subprocess.check_output(['git','cat-file','blob',oid]);assert remote_raw==local_raw
 assert hashlib.sha1(b'blob '+str(len(remote_raw)).encode()+b'\0'+remote_raw).hexdigest()==oid
 files.append({'path':path,'mode':mode,'blob':oid,'bytes':len(remote_raw),'sha256':hashlib.sha256(remote_raw).hexdigest(),'full_remote_bytes_equal_local':True})
changes=call(['git','diff','--name-only','40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',C]).decode().splitlines();assert all(x.startswith(PREFIX+'/')for x in changes)
result={'schema':'gr8-cp-publication-readback/v1','status':'VERIFIED_REMOTE_FULL_BYTES_SEMANTIC_TASK_INCOMPLETE','commit':C,'checkout_tree':tree,'task_tree':tasktree,'prefix':PREFIX,'file_count':len(files),'bytes':sum(x['bytes']for x in files),'files':files,'remote':'https://github.com/y805939188/pokemon-essentials-clean-room.git','isolated_bare':str(G),'seed_or_alternates':False,'collection_identical':True,'only_own_write_set_changed':True,'events':events,'semantic_credit':0,'task_final':'OPEN_INCOMPLETE','UPDATE_NOT_STARTED':True}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k]for k in ['status','commit','checkout_tree','task_tree','file_count','bytes']}))
