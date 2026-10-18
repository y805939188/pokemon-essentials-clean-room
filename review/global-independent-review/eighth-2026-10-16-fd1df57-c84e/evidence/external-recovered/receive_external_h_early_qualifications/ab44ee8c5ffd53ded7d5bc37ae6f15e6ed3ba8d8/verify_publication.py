"""Exact ordinary remote commit readback in a fresh bare; identity only."""
from pathlib import Path
import subprocess,json,hashlib,datetime,sys,gzip
T=Path(__file__).resolve().parent
REPO=T.parents[4]
C,attempt=sys.argv[1:3]
assert len(C)==40 and all(x in '0123456789abcdef'for x in C)
assert attempt.isalnum() or all(x.isalnum()or x=='-'for x in attempt)
W=T/'.transport'/('publication-'+attempt);assert not W.exists();W.mkdir(parents=True)
G=W/'remote.git';P=T/'.transport'/(attempt+'-remote-readback.json');events=[]
proof={'commit':C,'attempt':attempt,'utc_start':datetime.datetime.now(datetime.timezone.utc).isoformat(),'events':events,'semantic_credit':0,'status':'RUNNING'}
def save():P.write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
def run(args,check=True):
 p=subprocess.run(list(map(str,args)),capture_output=True)
 events.append({'args':list(map(str,args)),'exit':p.returncode,'stdout':p.stdout.decode('utf8','backslashreplace'),'stderr':p.stderr.decode('utf8','backslashreplace')});save()
 if check:assert p.returncode==0,(args,p.stderr)
 return p.stdout
def local(*args):return subprocess.check_output(['git','-C',str(REPO),*args])
try:
 run(['git','init','--bare',G]);pack=G/'objects/pack';bindings=[]
 seed=T/'.transport/target-1/remote.git/objects/pack'
 for p in sorted(seed.iterdir()):
  if p.suffix not in ('.pack','.idx','.rev'):continue
  bindings.append({'source':str(p),'resolved_source':str(p.resolve()),'bytes':p.stat().st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest()});(pack/p.name).symlink_to(p.resolve())
 proof['seed']={'scope':'Explicit frozen contract/B8/target/5historical identity cache; no own report commit; cache is not a full fresh network download','packs':bindings,'alternates_created':False};save()
 before=run(['git','--git-dir='+str(G),'cat-file','-e',C+'^{commit}'],False);assert events[-1]['exit']!=0,'Report already in seed; require a genuinely absent own commit'
 run(['git','--git-dir='+str(G),'update-ref','refs/inputs/fixed-contract','40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'])
 run(['git','--git-dir='+str(G),'remote','add','origin','https://github.com/y805939188/pokemon-essentials-clean-room.git'])
 run(['git','-c','gc.auto=0','--git-dir='+str(G),'fetch','--no-tags','origin',C])
 tree=run(['git','--git-dir='+str(G),'rev-parse',C+'^{tree}']).decode().strip();assert tree==local('rev-parse',C+'^{tree}').decode().strip()
 prefix=str(T.relative_to(REPO))
 tasktree=run(['git','--git-dir='+str(G),'rev-parse',C+':'+prefix]).decode().strip();assert tasktree==local('rev-parse',C+':'+prefix).decode().strip()
 l=local('ls-tree','-r','-z',C,'--',prefix);r=run(['git','--git-dir='+str(G),'ls-tree','-r','-z',C,'--',prefix]);assert l==r
 diff=local('diff','--name-only','-z','40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',C).decode().split('\0');assert all(not p or p.startswith(prefix+'/')for p in diff)
 files=[];data={}
 for row in r.split(b'\0'):
  if not row:continue
  meta,path=row.split(b'\t',1);mode,typ,oid=meta.decode().split();path=path.decode();assert typ=='blob' and mode=='100644';assert '/.transport/'not in path
  b=subprocess.check_output(['git','--git-dir='+str(G),'cat-file','blob',oid]);lb=local('cat-file','blob',oid);assert b==lb
  assert hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==oid
  rel=path[len(prefix)+1:];data[rel]=b
  files.append({'path':path,'relative_path':rel,'mode':mode,'blob':oid,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
 decoded=[]
 for f in files:
  rel=f['relative_path']
  if not rel.endswith('.gz'):continue
  b=gzip.decompress(data[rel]);expected=None
  if rel=='inputs/target/semantic-atlas/associations.json.gz':expected=json.loads(data['inputs/target/semantic-atlas/association-transport.json'])['decoded_identity']
  elif rel=='evidence/frozen-semantic-objects.json.gz':expected=json.loads(data['frozen-denominator.json'])['semantic_object_register']['decoded']
  elif rel.startswith('inputs/original-transport/'):
   for x in json.loads(data['evidence/original-recovery.json'])['files']:
    if x['transport_local_path']==rel:expected=x['input'];break
  assert expected is not None,rel
  sha=hashlib.sha256(b).hexdigest();oid=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest();assert len(b)==expected['bytes']and sha==expected['sha256']and oid==expected.get('git_blob',expected.get('git_blob_content_id'))
  decoded.append({'path':rel,'decoded_bytes':len(b),'decoded_sha256':sha,'decoded_blob':oid,'status':'VERIFIED'})
 proof.update(status='VERIFIED_FULL_TASK_REMOTE_READBACK',checkout_tree=tree,task_tree=tasktree,file_count=len(files),bytes=sum(x['bytes']for x in files),files=files,gzip_decoded_identities=decoded,protected_path_diff_outside_exclusive_task=[],utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat());save()
 print(json.dumps({k:proof[k]for k in ['commit','checkout_tree','task_tree','status','file_count','bytes']}))
except BaseException as e:
 proof.update(status='FAILED',error=repr(e));save();raise
