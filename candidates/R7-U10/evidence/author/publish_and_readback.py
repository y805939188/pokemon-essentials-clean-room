"""Publish only authorized U10 branch, read every new path in full from immutable remote URLs.
Run only after candidate commit. Receipts live outside the frozen candidate to avoid self-reference.
"""
from pathlib import Path
import subprocess,json,hashlib,datetime,urllib.request,urllib.parse,time,sys,concurrent.futures
ROOT=Path(__file__).resolve().parents[4]
B='e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH='codex/r7-u10-author-20261015-wave1'
DEST=Path('/workspace/r7-bootstrap/R7-U10-author/remote-readback-final')
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
DEST.mkdir(parents=True,exist_ok=False)
operations=[]
def run(argv):
 start=utc();p=subprocess.Popen(argv,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE);out,err=p.communicate()
 row={'argv':argv,'cwd':str(ROOT),'start_utc':start,'end_utc':utc(),'tool_pid':p.pid,'exit_code':p.returncode,'stdout':out.decode(errors='replace'),'stderr':err.decode(errors='replace')}
 operations.append(row)
 (DEST/'operations.json').write_text(json.dumps(operations,ensure_ascii=False,indent=2)+'\n')
 if p.returncode:raise RuntimeError(row)
 return out
assert run(['git','branch','--show-current']).decode().strip()==BRANCH
assert run(['git','status','--porcelain=v1'])==b''
commit=run(['git','rev-parse','HEAD']).decode().strip()
tree=run(['git','rev-parse','HEAD^{tree}']).decode().strip()
assert run(['git','rev-parse','HEAD^']).decode().strip()==B
assert run(['git','remote','get-url','origin']).decode().strip()=='https://github.com/y805939188/pokemon-essentials-clean-room.git'
paths=run(['git','diff','--name-only',B,commit]).decode().splitlines()
assert paths and all(p.startswith('candidates/R7-U10/') for p in paths)
assert not run(['git','diff','--name-only','--diff-filter=DMRT',B,commit])
# New branch must still be absent. Never overwrite an unrelated author's existing branch.
assert not run(['git','ls-remote','origin','refs/heads/'+BRANCH]).strip()
run(['git','push','origin','HEAD:refs/heads/'+BRANCH])
ref=run(['git','ls-remote','origin','refs/heads/'+BRANCH]).decode().strip()
assert ref==commit+'\trefs/heads/'+BRANCH
run(['git','fetch','origin',BRANCH])
assert run(['git','rev-parse','FETCH_HEAD']).decode().strip()==commit
assert run(['git','rev-parse','FETCH_HEAD^{tree}']).decode().strip()==tree
def read_one(path):
 local=(ROOT/path).read_bytes()
 expected=identity(local)
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
 attempts=[]
 for attempt in range(1,4):
  start=utc()
  try:
   request=urllib.request.Request(url,headers={'User-Agent':'R7-U10-fixed-candidate-readback'})
   with urllib.request.urlopen(request,timeout=40) as response:
    data=response.read(len(local)+1);status=response.status
   assert data==local,(path,identity(data),expected)
   target=DEST/'files'/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
   attempts.append({'attempt':attempt,'start_utc':start,'end_utc':utc(),'http_status':status,'complete_bytes_equal':True})
   return {'path':path,'url':url,'local':expected,'remote':identity(data),'attempts':attempts}
  except Exception as error:
   attempts.append({'attempt':attempt,'start_utc':start,'end_utc':utc(),'error':str(error)})
   if attempt==3:raise RuntimeError({'path':path,'attempts':attempts}) from error
   time.sleep(attempt)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 results=list(pool.map(read_one,paths))
assert run(['git','status','--porcelain=v1'])==b''
final_ref=run(['git','ls-remote','origin','refs/heads/'+BRANCH]).decode().strip()
assert final_ref==ref
receipt={'status':'CANDIDATE_READY_NOT_REVIEWED','at_utc':utc(),'branch':BRANCH,'base':B,'commit':commit,'tree':tree,'ordinary_push':True,'remote_ref':ref,'new_files_verified':len(results),'bytes_verified':sum(x['remote']['bytes'] for x in results),'remote_full_byte_readback':results,'operations_file':'operations.json','all_files_complete_remote_match':True,'working_tree_clean':True,'frozen_stop_writes':True,'independent_review':'WAIT_R7-I_FROZEN_INPUT_AND_DIFFERENT_ULTRA_CONTEXT','root_accepted_or_closed':False}
(DEST/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='remote_full_byte_readback'},ensure_ascii=False,indent=2))
