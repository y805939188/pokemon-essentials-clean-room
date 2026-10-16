"""Full HTTPS object readback; metadata is separately fetched through GitHub connector."""
from pathlib import Path
import concurrent.futures,datetime,gzip,hashlib,json,subprocess,sys,time,urllib.parse,urllib.request
T=Path(__file__).resolve().parents[1];C=T.parents[4];P=str(T.relative_to(C))
sha,tree,tasktree,out=sys.argv[1:]
for v in [sha,tree,tasktree]:assert len(v)==40 and all(c in '0123456789abcdef' for c in v)
assert subprocess.check_output(['git','rev-parse',sha+'^{tree}'],cwd=C,text=True).strip()==tree
assert subprocess.check_output(['git','rev-parse',sha+':'+P],cwd=C,text=True).strip()==tasktree
raw=subprocess.check_output(['git','ls-tree','-r','-z',sha,'--',P],cwd=C);entries=[]
for line in raw.split(b'\0'):
 if not line:continue
 head,path=line.decode().split('\t');mode,kind,blob=head.split();assert kind=='blob'
 entries.append((path,mode,blob))
def digest(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
cat=json.loads((T/'payload-catalog.json').read_text())['rows'];decoded={}
for r in cat:decoded[P+'/'+r['decoded_object']]={k:r['input'][k] for k in ['bytes','sha256','git_blob']}
errors=[]
def verify(e):
 path,mode,blob=e;url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+sha+'/'+urllib.parse.quote(path,safe='/')
 b=None
 for attempt in range(3):
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'r8-external-review-full-readback'}),timeout=45) as r:b=r.read()
   break
  except Exception as ex:
   errors.append({'path':path,'attempt':attempt+1,'error':type(ex).__name__+': '+str(ex)})
   if attempt==2:raise
 d=digest(b);assert d['git_blob']==blob
 local=subprocess.check_output(['git','show',sha+':'+path],cwd=C);assert b==local
 row={'path':path,'mode':mode,**d,'complete_remote_bytes_match':True,'url':url}
 if path in decoded:
  dd=digest(gzip.decompress(b));assert dd==decoded[path];row['decoded_identity']=dd
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(verify,entries))
r={'schema':'r8.external-r6-published-task-readback.v2','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':sha,'workspace_tree':tree,'task_tree':tasktree,'payloads':len(rows),'remote_bytes':sum(r['bytes'] for r in rows),'decoded_readset_objects_verified':sum('decoded_identity'in r for r in rows),'all_paths_modes_blobs_bytes_sha256_match':True,'metadata_boundary':'GitHub connector independently read commit/tree chain and exact task recursive tree; SHA matched local complete tree. Metadata receipt is recorded externally or in sibling receipt. No remote-tracking-only inference.','semantic_credit_from_transport':False,'attempt_errors_retained':errors,'status':'FULL_TASK_REMOTE_READBACK_VERIFIED','rows':rows}
if out!='-':
 q=T/'publication'/out;assert q.parent==T/'publication' and not q.exists();q.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k!='rows'},ensure_ascii=False))
