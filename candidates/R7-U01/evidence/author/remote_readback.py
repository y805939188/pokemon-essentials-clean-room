"""Read fixed remote candidate bytes; no mutation except optional local receipt."""
import argparse,concurrent.futures,datetime,hashlib,json,subprocess,urllib.request,urllib.parse
from pathlib import Path
REPOSITORY='y805939188/pokemon-essentials-clean-room'
BASE='e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH='codex/r7-u01-author-20261015-pilot1'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--commit',required=True);p.add_argument('--output',type=Path);a=p.parse_args();logs=[]
 def run(args):
  start=now();cmd=['git',*args];r=subprocess.run(cmd,cwd=a.repo,capture_output=True,text=True);logs.append({'command':cmd,'start_utc':start,'end_utc':now(),'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr});assert r.returncode==0,logs[-1];return r.stdout.strip()
 expected=a.commit;start=now();assert run(['rev-parse','HEAD'])==expected
 tree=run(['rev-parse',expected+'^{tree}']);before=run(['ls-remote','--heads','origin',BRANCH]);assert before.split()[0]==expected
 run(['fetch','--no-tags','origin',BRANCH]);assert run(['rev-parse','FETCH_HEAD'])==expected;assert run(['rev-parse','FETCH_HEAD^{tree}'])==tree
 paths=run(['diff','--name-only',BASE,'FETCH_HEAD']).splitlines();assert paths and all(x.startswith('candidates/R7-U01/') for x in paths)
 run(['merge-base','--is-ancestor',BASE,expected])
 def read(path):
  local=subprocess.check_output(['git','show',expected+':'+path],cwd=a.repo)
  url='https://raw.githubusercontent.com/'+REPOSITORY+'/'+expected+'/'+urllib.parse.quote(path)
  began=now();request=urllib.request.Request(url,headers={'User-Agent':'R7-U01-exact-remote-readback'})
  with urllib.request.urlopen(request,timeout=40) as resp:data=resp.read(len(local)+1);status=resp.status
  assert status==200 and data==local,(path,status)
  return {'path':path,'url':url,'start_utc':began,'end_utc':now(),'http_status':status,'complete_byte_match':True,**identity(data)}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:files=list(pool.map(read,paths))
 after=run(['ls-remote','--heads','origin',BRANCH]);assert after==before
 result={'schema':'r7.u01-exact-remote-readback.v1','status':'REMOTE_COMPLETE_BYTES_VERIFIED','start_utc':start,'end_utc':now(),'commit':expected,'tree':tree,'branch':BRANCH,'remote_tip_before_and_after':expected,'base':BASE,'base_relative_diff_scope':'candidates/R7-U01/ only','files_verified':len(files),'bytes_verified':sum(x['bytes'] for x in files),'files':files,'commands':logs,'semantic_review':'NOT_ASSERTED','independent_candidate_review':'NOT_REACHED'}
 if a.output:a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['status','commit','tree','branch','files_verified','bytes_verified','base_relative_diff_scope','independent_candidate_review']},ensure_ascii=False))
if __name__=='__main__':main()
