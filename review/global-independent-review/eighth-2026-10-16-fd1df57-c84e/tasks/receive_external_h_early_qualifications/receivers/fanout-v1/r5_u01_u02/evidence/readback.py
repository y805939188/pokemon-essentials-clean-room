"""Read back exactly one published commit and this shard, without a checkout.

The isolated bare has no alternates. Blob-filtered fetch reuses its own already
verified cache on the successor pass, fetching only required shard payloads.
"""
from pathlib import Path
import subprocess,sys,json,hashlib,datetime
W=Path(__file__).resolve().parents[1];P=Path('/workspace/pokemon-essentials-clean-room');G=W/'.local/remote-readback.git';prefix=str(W.relative_to(P));branch='codex/r8-final-early-r5-u01-u02-20261016';remote='https://github.com/y805939188/pokemon-essentials-clean-room.git'
commit=sys.argv[1]
assert len(commit)==40 and all(c in '0123456789abcdef'for c in commit)
def run(*a):return subprocess.check_output(list(a),stderr=subprocess.PIPE)
def local(*a):return run('git','-C',str(P),*a)
def git(*a):return run('git','--git-dir='+str(G),*a)
if not G.exists():
 run('git','init','--bare',str(G));git('remote','add','origin',remote)
assert not (G/'objects/info/alternates').exists()
head=git('ls-remote','--heads','origin','refs/heads/'+branch).decode().split()
assert head==[commit,'refs/heads/'+branch],head
git('fetch','--no-tags','--depth=1','--filter=blob:none','origin',commit)
assert git('rev-parse','FETCH_HEAD').decode().strip()==commit
def listing(f):
 ret={}
 for line in f('ls-tree','-r','-z',commit,'--',prefix).split(b'\0'):
  if not line:continue
  meta,path=line.split(b'\t');mode,typ,oid=meta.decode().split();p=path.decode();assert p.startswith(prefix+'/')and typ=='blob';ret[p]=(mode,oid)
 return ret
rows=listing(git);assert rows==listing(local)
files=[]
for path,(mode,oid)in sorted(rows.items()):
 b=git('cat-file','blob',oid);expected=local('cat-file','blob',oid);assert b==expected
 assert hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==oid
 assert mode=='100644'
 files.append({'path':path,'mode':mode,'git_blob':oid,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
tree=git('rev-parse',commit+'^{tree}').decode().strip();task_tree=git('rev-parse',commit+':'+prefix).decode().strip()
assert tree==local('rev-parse',commit+'^{tree}').decode().strip()
assert task_tree==local('rev-parse',commit+':'+prefix).decode().strip()
result={'schema':'gr8.r5-u01-u02.remote-readback/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'branch':branch,'remote':remote,'checkout_tree':tree,'shard_tree':task_tree,'ordinary_fetch':True,'isolated_bare_no_alternates':True,'exact_file_set_mode_blob_bytes_sha_match':True,'file_count':len(files),'bytes':sum(x['bytes']for x in files),'files':files,'semantic_credit':0,'new_behavior_execution':0,'UPDATE_NOT_STARTED':True}
out=W/'.local'/('readback-'+commit+'.json');out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k!='files'}))
