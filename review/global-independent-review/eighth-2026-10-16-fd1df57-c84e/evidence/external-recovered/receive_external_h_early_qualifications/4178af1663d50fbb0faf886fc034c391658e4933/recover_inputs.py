"""Recover exact fixed task from fresh isolated bare fetch; never execute inputs."""
from pathlib import Path
import datetime,hashlib,json,subprocess
TASK=Path(__file__).resolve().parent
REPO=TASK.parents[4]
ROOT=TASK.parents[1]
C='11c057d9aed330c16312470f80f13d180f8e1e65'
rows=json.loads((ROOT/'delegation/readsets/receive_external_h_early_qualifications.complete.json').read_text())
work=TASK/'.transport/target-1'; assert not work.exists();work.mkdir(parents=True)
gitdir=work/'remote.git';events=[]
proof={'utc_start':datetime.datetime.now(datetime.timezone.utc).isoformat(),'target':C,'events':events,'semantic_credit':0,'recovered_code_executed':False,'status':'RUNNING'}
def save(): (TASK/'input-recovery.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
def run(args,check=True):
 p=subprocess.run(list(map(str,args)),capture_output=True)
 events.append({'args':list(map(str,args)),'exit':p.returncode,'stdout':p.stdout.decode('utf8','backslashreplace'),'stderr':p.stderr.decode('utf8','backslashreplace')});save()
 if check: assert p.returncode==0,(args,p.stderr)
 return p
try:
 run(['git','init','--bare',gitdir])
 # Freeze seed packs by path, bytes and SHA256. The target commit is absent.
 # Seed is explicitly the inherited B8 workspace plus exact contract-fetch packs;
 # not claimed to be the coordinator's B8-only cache or a fresh network download.
 pack=gitdir/'objects/pack';seed=REPO/'.git/objects/pack';bindings=[]
 for p in sorted(seed.iterdir()):
  if p.suffix not in ('.pack','.idx','.rev'):continue
  bindings.append({'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest()})
  (pack/p.name).symlink_to(p.resolve())
 proof['seed']={'qualification':'Inherited B8 + fixed contract packs, explicit immutable-content identity cache, not remote semantic credit','files':bindings,'alternates_created':False};save()
 before=run(['git','--git-dir='+str(gitdir),'cat-file','-e',C+'^{commit}'],False);assert before.returncode!=0
 run(['git','--git-dir='+str(gitdir),'update-ref','refs/inputs/fixed-contract','40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'])
 run(['git','--git-dir='+str(gitdir),'remote','add','origin','https://github.com/y805939188/pokemon-essentials-clean-room.git'])
 run(['git','-c','gc.auto=0','--git-dir='+str(gitdir),'fetch','--no-tags','origin',C])
 tree=run(['git','--git-dir='+str(gitdir),'rev-parse',C+'^{tree}']).stdout.decode().strip();assert tree==rows['target_checkout_tree']
 prefix='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/external_h_early_qualifications'
 tt=run(['git','--git-dir='+str(gitdir),'rev-parse',C+':'+prefix]).stdout.decode().strip();assert tt==rows['target_task_tree_observed_from_fixed_commit']
 listing=run(['git','--git-dir='+str(gitdir),'ls-tree','-r','-z',C,'--',prefix]).stdout.split(b'\0');observed={}
 for row in listing:
  if not row:continue
  m,path=row.split(b'\t',1);mode,typ,oid=m.decode().split();assert typ=='blob';observed[path.decode()]=(mode,oid)
 assert set(observed)=={r['remote_path_at_target_commit']for r in rows['files']}
 dest=TASK/'inputs/target';assert not dest.exists();dest.mkdir(parents=True)
 files=[]
 for r in rows['files']:
  assert observed[r['remote_path_at_target_commit']]==(r['mode'],r['git_blob'])
  rel=Path(r['relative_to_target_task']);assert not rel.is_absolute() and '..'not in rel.parts
  p=subprocess.run(['git','--git-dir='+str(gitdir),'cat-file','blob',r['git_blob']],capture_output=True);assert p.returncode==0
  b=p.stdout;assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'] and hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['git_blob']
  out=dest/rel;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(b)
  files.append(dict(r,local_path=str(out.relative_to(TASK)),credit='IDENTITY_ONLY'))
 proof.update(status='VERIFIED_TARGET_BYTES',checkout_tree=tree,task_tree=tt,files=files,file_count=len(files),bytes=sum(x['bytes']for x in files),utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat());save()
 print(json.dumps({k:proof[k]for k in ['status','checkout_tree','task_tree','file_count','bytes']}))
except BaseException as e:
 proof.update(status='FAILED',error=repr(e));save();raise
