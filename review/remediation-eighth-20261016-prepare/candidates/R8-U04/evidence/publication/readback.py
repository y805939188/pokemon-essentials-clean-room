from pathlib import Path
import subprocess,sys,json,datetime,hashlib
root=Path('/workspace/pokemon-essentials-clean-room');work=Path('/tmp/r8u04-publication');remote=work/'remote.git';rev=sys.argv[1];label=sys.argv[2];prefix='review/remediation-eighth-20261016-prepare/candidates/R8-U04/';ops=[]
def run(name,args,data=None):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(args,input=data,stdout=subprocess.PIPE,stderr=subprocess.PIPE);end=datetime.datetime.now(datetime.timezone.utc).isoformat();(work/(label+'-'+name+'.stdout')).write_bytes(r.stdout);(work/(label+'-'+name+'.stderr')).write_bytes(r.stderr);ops.append({'name':name,'argv':args,'start_utc':start,'end_utc':end,'exit':r.returncode,'stdout_bytes':len(r.stdout),'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr':r.stderr.decode()});print(name,r.returncode,len(r.stdout),r.stderr.decode()[:500],flush=True);assert r.returncode==0;return r.stdout
if not remote.exists():
 run('init',['git','init','--bare','--initial-branch=r8-readback',str(remote)])
 run('origin',['git','-C',str(remote),'remote','add','origin','https://github.com/y805939188/pokemon-essentials-clean-room.git'])
 run('promisor',['git','-C',str(remote),'config','remote.origin.promisor','true'])
 run('filter',['git','-C',str(remote),'config','remote.origin.partialclonefilter','blob:none'])
assert not (remote/'objects/info/alternates').exists()
run('fetch',['git','-c','gc.auto=0','-c','maintenance.auto=false','-C',str(remote),'fetch','--no-tags','--filter=blob:none','--depth=1','origin',rev])
listing=run('tree',['git','-C',str(remote),'ls-tree','-r','-z',rev,'--',prefix]);entries=[]
for entry in listing.split(b'\0'):
 if not entry:continue
 identity,path=entry.split(b'\t',1);mode,typ,blob=identity.decode().split();assert typ=='blob';entries.append((mode,blob,path.decode()))
assert entries
missing=[]
# cat-file --batch-check with lazy-fetch disabled identifies which full objects still need remote transfer.
bids=sorted(set(b for _,b,_ in entries))
r=subprocess.run(['git','-C',str(remote),'--no-lazy-fetch','cat-file','--batch-check'],input=('\n'.join(bids)+'\n').encode(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
assert r.returncode==0,r.stderr
for line in r.stdout.decode().splitlines():
 if line.endswith(' missing'):missing.append(line.split()[0])
if missing:
 run('fetch-new-full-blobs',['git','-c','gc.auto=0','-c','maintenance.auto=false','-C',str(remote),'fetch','--no-tags','--no-write-fetch-head','--filter=blob:none','--stdin','origin'],data=('\n'.join(missing)+'\n').encode())
files=[]
for mode,blob,path in entries:
 b=run('blob-'+blob,['git','-C',str(remote),'--no-lazy-fetch','cat-file','blob',blob]);local=(root/path).read_bytes();assert b==local,path
 calculated=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();assert calculated==blob
 files.append({'path':path,'mode':mode,'blob':blob,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'full_remote_bytes_equal_local':True})
actual=run('advertised-head',['git','-C',str(remote),'ls-remote','--heads','origin','refs/heads/revise/r8-u04-20261017']).decode().split()[0];assert actual==rev
out={'schema':'r8-u04-fresh-remote-full-bytes/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':rev,'branch':'revise/r8-u04-20261017','remote':'https://github.com/y805939188/pokemon-essentials-clean-room.git','status':'VERIFIED_REMOTE_FULL_BYTES','fresh_bare':str(remote),'local_object_alternates':False,'local_repository_used_as_object_source':False,'strategy':'remote partial fetch for trees, explicit remote fetch of every missing candidate blob, complete cat-file bytes SHA256/blob comparison','files':files,'file_count':len(files),'bytes':sum(x['bytes'] for x in files),'operations':ops,'semantic_review_credit':'NONE','business_execution':'NOT_EXECUTED','candidate_independent_PASS':'PENDING_NONAUTHOR'}
(work/(label+'-readback.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('VERIFIED',rev,len(files),out['bytes'],flush=True)
