"""Verify actual remote C0 using the already fully read C1 byte cache."""
import argparse,datetime,hashlib,json,os,subprocess
from pathlib import Path
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--receipt',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
 src=Path(a.receipt);out=Path(a.output);assert not out.exists();r=json.loads(src.read_bytes());assert r['status']=='FULL_REMOTE_READBACK_VERIFIED'
 bare=r['isolated_bare_repository'];rr=r['report_root'];core='28e0d9df6ca4f75de9773a502ebdaa177cc0752c';logs=out.parent/(out.name+'.commands');logs.mkdir();commands=[]
 env=dict(os.environ)
 for k in list(env):
  if k in ('GIT_DIR','GIT_WORK_TREE','GIT_COMMON_DIR','GIT_OBJECT_DIRECTORY','GIT_ALTERNATE_OBJECT_DIRECTORIES','GIT_INDEX_FILE','GIT_CONFIG','GIT_CONFIG_COUNT','GIT_CONFIG_PARAMETERS') or k.startswith(('GIT_CONFIG_KEY_','GIT_CONFIG_VALUE_')):env.pop(k)
 env['GIT_OPTIONAL_LOCKS']='0'
 def run(args):
  argv=['git','-C',bare,*args];start=utc();p=subprocess.run(argv,capture_output=True,env=env);stem=logs/str(len(commands));stdout=Path(str(stem)+'.stdout');stderr=Path(str(stem)+'.stderr');stdout.write_bytes(p.stdout);stderr.write_bytes(p.stderr);commands.append({'argv':argv,'start_utc':start,'end_utc':utc(),'exit_code':p.returncode,'stdout':str(stdout),'stderr':str(stderr)});assert p.returncode==0,p.stderr;return p.stdout
 run(['fetch','--no-tags','--depth=2',r['remote'],'refs/heads/'+r['branch']]);assert not (Path(bare)/'objects/info/alternates').exists()
 workspace=run(['rev-parse',core+'^{tree}']).decode().strip();tree=run(['rev-parse',core+':'+rr]).decode().strip();assert workspace=='a2e8143f5f514ac8db5fcc36e8cbdaaaaf428133' and tree=='3583466aef215439358c9578f956871afa1f98af'
 listing=run(['ls-tree','-r','-z',core,'--',rr]);cache={x['path']:x for x in r['physical_members']};members=[];direct=0
 for line in listing.split(b'\0'):
  if not line:continue
  meta,path=line.split(b'\t',1);mode,kind,oid=meta.decode().split();path=path.decode();assert kind=='blob'
  old=cache.get(path)
  if old and old['git_blob']==oid:members.append({**old,'verification':'FULL_REMOTE_C1_BYTES_REUSED_EXACT_UNCHANGED_GIT_BLOB'})
  else:
   b=run(['show',core+':'+path]);v=ident(b);assert v['git_blob']==oid;members.append({'path':path,'mode':mode,**v,'verification':'FULL_REMOTE_C0_BYTES_READ_SEPARATELY'});direct+=1
 result={'schema':'r7.remote-core-byte-verification.v1','status':'FULL_REMOTE_CORE_VERIFIED','at_utc':utc(),'core_commit':core,'workspace_tree':workspace,'report_tree':tree,'report_root':rr,'C1_receipt':{'path':str(src),**ident(src.read_bytes())},'members':members,'counts':{'core_files':len(members),'direct_C0_reads':direct,'exact_C1_byte_cache_reuse':len(members)-direct},'commands':commands,'qualification':'Immutable remote C0 tree plus exact full remote byte evidence; reuse does not add semantic reading. No source checkout or alternate object store.'}
 out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result['counts']))
if __name__=='__main__':main()
