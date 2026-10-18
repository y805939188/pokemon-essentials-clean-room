"""Read-only independent remote checkpoint recovery; never executes recovered inputs."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
commit,group,expected_tree=sys.argv[1:4]
assert len(commit)==40 and all(x in '0123456789abcdef'for x in commit)
assert group and all(x.islower()or x.isdigit()or x=='_'for x in group)
work=Path('/workspace/scratch')/('r8-external-'+group+'-'+commit[:8]+'-recovery1')
assert not work.exists(), 'Use a fresh explicitly named attempt; never delete existing evidence'
work.mkdir();gitdir=work/'remote.git';events=[]
remote='https://github.com/y805939188/pokemon-essentials-clean-room.git'
seed=Path('/workspace/scratch/r8-com006-nine-dispatch-readback-17/remote.git')
proof=json.loads((ROOT/'publication/r8-com006-nine-dispatch-readback-17.json').read_text())
assert proof['status']=='VERIFIED'and proof['commit']=='6c31240ade5c761b1f405958583a81ed140d4682'
result={'schema':'gr8-external-independent-recovery/v1','commit':commit,'logical_primary':group,'remote':remote,'expected_checkout_tree':expected_tree,'utc_start':datetime.datetime.now(datetime.timezone.utc).isoformat(),'events':events,'status':'IN_PROGRESS','semantic_credit':'NONE transport/identity only; recovered files inert','UPDATE_NOT_STARTED':True}
receipt=ROOT/'publication'/('external-'+group+'-'+commit[:8]+'-recovery.json')
def save():receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
def run(args,expected=0,timeout=55):
 st=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(args,capture_output=True,timeout=timeout)
 events.append({'args':list(map(str,args)),'start_utc':st,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':p.returncode,'stdout':p.stdout.decode('utf-8','backslashreplace'),'stderr':p.stderr.decode('utf-8','backslashreplace')})
 if expected is not None:assert p.returncode==expected,(args,p.stderr)
 return p
try:
 assert not(seed/'objects/info/alternates').exists()
 before=run(['git','--git-dir='+str(seed),'cat-file','-e',commit+'^{commit}'],expected=None)
 assert before.returncode!=0, 'Target already in seed: no independent recovery credit'
 run(['git','init','--bare',str(gitdir)])
 pack=gitdir/'objects/pack';pack.mkdir(exist_ok=True);bindings=[]
 for p in sorted((seed/'objects/pack').iterdir()):
  if p.suffix not in ['.pack','.idx','.rev']:continue
  raw=p.read_bytes();bindings.append({'path':str(p),'resolved_path':str(p.resolve()),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()});(pack/p.name).symlink_to(p.resolve())
 result['seed']={'scope':'Independently full-byte verified17 report ancestry + exactB8 input packs; no externaltarget present before fetch. Read-only pack symlinks; noalternates. This seed is intentionally broader than B8-only ordinary publication verifier, explicitly named.','proof':'publication/r8-com006-nine-dispatch-readback-17.json','pack_bindings':bindings}
 run(['git','--git-dir='+str(gitdir),'update-ref','refs/inputs/verified-report17','6c31240ade5c761b1f405958583a81ed140d4682'])
 run(['git','--git-dir='+str(gitdir),'remote','add','origin',remote])
 before=run(['git','--git-dir='+str(gitdir),'cat-file','-e',commit+'^{commit}'],expected=None);assert before.returncode!=0
 run(['git','-c','gc.auto=0','--git-dir='+str(gitdir),'fetch','--no-tags','origin',commit])
 tree=run(['git','--git-dir='+str(gitdir),'rev-parse',commit+'^{tree}']).stdout.decode().strip();assert tree==expected_tree,(tree,expected_tree)
 formal=run(['git','--git-dir='+str(gitdir),'rev-parse',commit+':deliverables/final-specification-set']).stdout.decode().strip();assert formal=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
 base='fd1df570cad987dc3852a3b958f03916e317f7fe';diff=run(['git','--git-dir='+str(gitdir),'diff','--name-only','-z',base,commit]).stdout.split(b'\0');report_prefix='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/'
 assert all(not x or x.decode().startswith(report_prefix)for x in diff),'Protected source/formal or other path changed'
 prefix=report_prefix+'tasks/external_'+group+'/'
 listing=run(['git','--git-dir='+str(gitdir),'ls-tree','-r','-z',commit,'--',prefix]).stdout.split(b'\0')
 entries=[];dest=ROOT/'evidence/external-recovered'/group/commit;assert not dest.exists();dest.mkdir(parents=True)
 for row in listing:
  if not row:continue
  meta,path=row.split(b'\t',1);mode,typ,oid=meta.decode().split();path=path.decode();assert path.startswith(prefix)and typ=='blob';rel=Path(path[len(prefix):]);assert not rel.is_absolute()and '..'not in rel.parts
  p=subprocess.run(['git','--git-dir='+str(gitdir),'cat-file','blob',oid],capture_output=True);assert p.returncode==0
  blob=p.stdout;assert hashlib.sha1(b'blob '+str(len(blob)).encode()+b'\0'+blob).hexdigest()==oid
  target=dest/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(blob)
  entries.append({'remote_path':path,'recovered':str(target.relative_to(ROOT)),'git_blob':oid,'mode':mode,'bytes':len(blob),'sha256':hashlib.sha256(blob).hexdigest(),'materialization':'Inertregularfile; originalmode recorded, noexecutepermissionorlinkcreated'})
 assert entries, 'Expected exclusive delivery folder not found; do not claim delivery recovered'
 result.update(status='VERIFIED_REMOTE_CHECKPOINT_BYTES_RECOVERED',checkout_tree=tree,protected_formal_tree=formal,exclusive_delivery_prefix=prefix,files=entries,count=len(entries),bytes=sum(x['bytes']for x in entries),utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat(),task_final_acceptance='OPEN_NOT_SIGNED')
 save();print(json.dumps({k:result[k]for k in ['commit','checkout_tree','count','bytes','status']},ensure_ascii=False))
except BaseException as error:
 result.update(status='FAILED_ZERO_TRANSPORT_ACCEPTANCE',error_type=type(error).__name__,error=str(error),utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat());save();raise
