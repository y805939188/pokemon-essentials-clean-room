#!/usr/bin/env python3
"""Full fixed-commit raw readback of every newly changed payload, no R execution."""
import json,subprocess,sys,urllib.request,urllib.parse,hashlib,datetime,time,concurrent.futures
from pathlib import Path
E=Path(__file__).resolve().parent; REPO=E.parents[4]
commit,base,out=sys.argv[1:4]
branch='codex/remediation-sixth-r6-u05-author-20261014'
def git(*args): return subprocess.check_output(['git',*args],cwd=REPO)
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
remote=git('ls-remote','origin','refs/heads/'+branch).decode().strip()
assert remote.split()[0]==commit,remote
paths=git('diff','--name-only',base,commit).decode().splitlines()
allowed=E.parent.relative_to(REPO).as_posix()+'/'
assert paths and all(p.startswith(allowed+'mirror/') or p.startswith(allowed+'evidence/') for p in paths)
def read(path):
 line=git('ls-tree',commit,'--',path).decode().strip(); mode,kind,blob_name=line.split('\t')[0].split()
 assert kind=='blob' and mode=='100644'
 expected=git('cat-file','blob',commit+':'+path); expected_identity=identity(expected)
 assert blob_name==expected_identity['git_blob']
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/')
 attempts=[]
 for n in range(1,4):
  try:
   with urllib.request.urlopen(url,timeout=45) as r:got=r.read();status=r.status
   actual=identity(got);assert got==expected and actual==expected_identity
   return {'commit':commit,'path':path,'mode':mode,'type':'text','git_object_type':kind,'expected':expected_identity,'remote':actual,'raw_http_status':status,'complete_original_bytes_equal':True,'url':url,'failed_attempts':attempts}
  except Exception as ex:
   attempts.append({'attempt':n,'error':str(ex),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
   if n==3: return {'path':path,'failed_attempts':attempts,'result':'FAILED_READBACK'}
   time.sleep(min(n,2))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:records=list(pool.map(read,paths))
result={'started_utc':start,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'base_commit':base,'workspace_tree':git('rev-parse',commit+'^{tree}').decode().strip(),'candidate_directory_tree':git('rev-parse',commit+':'+E.parent.relative_to(REPO).as_posix()).decode().strip(),'mirror_directory_tree':git('rev-parse',commit+':'+(E.parent/'mirror').relative_to(REPO).as_posix()).decode().strip(),'remote_branch':branch,'ls_remote':remote,'listing_basis':'Exact base..commit changed path list; every path mode/type/blob bound by immutable commit SHA echoed by remote branch and full matching raw bytes','paths_count':len(paths),'undeclared_paths':[],'payloads':records,'result':'FULL_REMOTE_READBACK_CONFIRMED' if all(x.get('complete_original_bytes_equal') for x in records) else 'FAILED'}
Path(out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='payloads'},ensure_ascii=False))
sys.exit(0 if result['result']=='FULL_REMOTE_READBACK_CONFIRMED' else 1)
