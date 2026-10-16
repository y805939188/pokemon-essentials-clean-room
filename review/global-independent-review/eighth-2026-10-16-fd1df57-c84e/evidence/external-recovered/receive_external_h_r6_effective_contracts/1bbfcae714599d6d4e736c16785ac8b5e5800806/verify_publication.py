"""Ordinary remote fetch/readback with an explicit verified unchanged-input cache.
The new publication commit must be absent from the cache before fetch.
No recovered scripts or game content are executed.
"""
import datetime,gzip,hashlib,io,json,pathlib,subprocess,sys
T=pathlib.Path(__file__).resolve().parent
repo=T.parents[4]
commit,stage=sys.argv[1:3]
assert len(commit)==40 and all(c in '0123456789abcdef' for c in commit)
assert stage in ['core','final']
J=T/'runtime'/('readback-'+stage+'.git');assert not J.exists()
S=T/'runtime/remote.git'
G=['git','--git-dir='+str(J)];events=[]
receipt=T/('publication/'+stage+'-readback.json') if stage=='core' else T/'runtime/final-readback.json'
receipt.parent.mkdir(exist_ok=True)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def call(a,ok=0):
 t=now();p=subprocess.run(a,capture_output=True)
 events.append(dict(args=a,start_utc=t,end_utc=now(),exit=p.returncode,stdout=p.stdout.decode('utf-8','backslashreplace'),stderr=p.stderr.decode('utf-8','backslashreplace')))
 (T/'runtime'/('readback-'+stage+'-events.json')).write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
 assert p.returncode==ok,(a,p.stderr.decode(errors='replace'))
 return p.stdout
# Full pack-file identities bind the read-only cache from this run's prior remote recovery.
seed=[]
for p in sorted((S/'objects/pack').iterdir()):
 if p.suffix not in ['.pack','.idx','.rev']:continue
 h=hashlib.sha256();n=0
 with p.open('rb') as f:
  while b:=f.read(1024*1024):h.update(b);n+=len(b)
 seed.append(dict(path=str(p),bytes=n,sha256=h.hexdigest()))
assert subprocess.run(['git','--git-dir='+str(S),'cat-file','-e',commit+'^{commit}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode!=0
call(['git','init','--bare',str(J)])
for x in seed:
 p=pathlib.Path(x['path']);(J/'objects/pack'/p.name).symlink_to(p.resolve())
if (S/'shallow').exists():(J/'shallow').write_bytes((S/'shallow').read_bytes())
call(G+['update-ref','refs/inputs/verified-external-target','a96ec67a948e3fc86b25ad407cd977b6752e2d77'])
assert subprocess.run(G+['cat-file','-e',commit+'^{commit}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode!=0
call(G+['fetch','--no-tags','--depth=1','https://github.com/y805939188/pokemon-essentials-clean-room.git',commit])
local=['git','-C',str(repo)]
prefix=str(T.relative_to(repo))+'/'
checkout=call(G+['rev-parse',commit+'^{tree}']).decode().strip()
assert checkout==subprocess.check_output(local+['rev-parse',commit+'^{tree}']).decode().strip()
tasktree=call(G+['rev-parse',commit+':'+prefix.rstrip('/')]).decode().strip()
assert tasktree==subprocess.check_output(local+['rev-parse',commit+':'+prefix.rstrip('/')]).decode().strip()
assert call(G+['rev-parse',commit+':deliverables/final-specification-set']).decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
a=call(G+['ls-tree','-r','-z',commit,'--',prefix])
b=subprocess.check_output(local+['ls-tree','-r','-z',commit,'--',prefix]);assert a==b
rows=[]
for line in a.split(b'\0'):
 if not line:continue
 meta,path=line.split(b'\t',1);mode,typ,oid=meta.decode().split();assert typ=='blob' and mode in ['100644','100755']
 path=path.decode();assert path.startswith(prefix)
 data=subprocess.check_output(G+['cat-file','blob',oid]);expected=subprocess.check_output(local+['cat-file','blob',oid]);assert data==expected
 q=identity(data);assert q['git_blob']==oid
 rows.append(dict(path=path,mode=mode,**q))
index=json.loads(subprocess.check_output(G+['show',commit+':'+prefix+'decoded-index.json']))
decoded=[];seen=set()
for r in index['roles']:
 i=r['input'];sha=i['sha256']
 if sha in seen:continue
 seen.add(sha)
 comp=subprocess.check_output(G+['show',commit+':'+prefix+'recovered/payload-objects/'+sha+'.gz'])
 with gzip.GzipFile(fileobj=io.BytesIO(comp)) as f:data=f.read(i['bytes']+1)
 q=identity(data);assert all(q[k]==i[k] for k in ['bytes','sha256','git_blob'])
 raw=subprocess.check_output(G+['show',commit+':'+prefix+r['decoded_path']]);assert raw==data
 decoded.append(dict(decoded=sha,**q))
assert len(decoded)==52
out=dict(schema='r8-reception-publication-readback/v1',status='VERIFIED',commit=commit,checkout_tree=checkout,task_tree=tasktree,prefix=prefix,file_count=len(rows),bytes=sum(x['bytes'] for x in rows),files=rows,decoded_objects=decoded,seed=dict(scope='Exact unchanged inputs previously independently fetched as target a96ec67a; no publication commit existed before this ordinary remote fetch',recovery='recovery-manifest.json',pack_bindings=seed),events=events,utc_end=now(),semantic_status='INCOMPLETE',semantic_credit_from_readback=0,protected_formal_tree='f292698cdd4a8e725525a9be6dc34b75faaf151e')
receipt.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','commit','checkout_tree','task_tree','file_count','bytes','semantic_status']},ensure_ascii=False))
