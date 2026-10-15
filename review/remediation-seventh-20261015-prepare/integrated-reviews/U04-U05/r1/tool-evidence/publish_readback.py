"""Ordinary commit/push of the single authorized scope, then full remote readback."""
from pathlib import Path
import argparse,concurrent.futures,datetime,hashlib,json,subprocess,urllib.request,urllib.parse
parser=argparse.ArgumentParser();parser.add_argument('--previous',default='');parser.add_argument('--output',required=True);parser.add_argument('--message',required=True);args=parser.parse_args()
BRANCH='codex/r7-ir-u04-u05-20261015-r1';BASE='e646432c644dec04d306842cc5a559a29c718fbc'
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/U04-U05/r1/'
receipt={'schema':'r7.ir-publication-full-readback.v1','start_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'branch':BRANCH,'base':BASE,'expected_previous_remote_tip':args.previous,'commands':[],'files':[],'semantic_or_behavior_credit':False}
def run(argv):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE);out,err=p.communicate()
 receipt['commands'].append({'argv':argv,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command_pid':p.pid,'exit_code':p.returncode,'stdout':out.decode(),'stderr':err.decode()})
 assert p.returncode==0,(argv,p.returncode,err.decode());return out
try:
 assert run(['git','branch','--show-current']).decode().strip()==BRANCH
 status=run(['git','status','--porcelain','--untracked-files=all']).decode().splitlines();assert all(l[3:].startswith(PREFIX) for l in status)
 before=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH]).decode().strip();assert (before.split()[0] if before else '')==args.previous
 run(['git','add','--',PREFIX]);run(['git','diff','--cached','--check'])
 staged=run(['git','diff','--cached','--name-only']).decode().splitlines();assert staged and all(p.startswith(PREFIX) for p in staged)
 run(['git','commit','-m',args.message]);commit=run(['git','rev-parse','HEAD']).decode().strip();tree=run(['git','rev-parse','HEAD^{tree}']).decode().strip();receipt.update(commit=commit,tree=tree)
 changed=run(['git','diff','--name-only',BASE,commit]).decode().splitlines();assert changed and all(p.startswith(PREFIX) for p in changed)
 run(['git','push','origin','HEAD:refs/heads/'+BRANCH])
 remote1=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH]).decode().split()[0];assert remote1==commit
 run(['git','fetch','--no-tags','origin','refs/heads/'+BRANCH]);assert run(['git','rev-parse','FETCH_HEAD']).decode().strip()==commit
 assert run(['git','rev-parse','FETCH_HEAD^{tree}']).decode().strip()==tree
 listed=run(['git','ls-tree','-r',commit,'--',PREFIX]).decode().splitlines();paths=[]
 for line in listed:
  header,path=line.split('\t');mode,typ,blob=header.split();assert mode=='100644' and typ=='blob';paths.append((path,blob))
 assert {p for p,_ in paths}==set(changed)
 def read(row):
  path,blob=row;expected=subprocess.check_output(['git','show',commit+':'+path]);start=datetime.datetime.now(datetime.timezone.utc).isoformat()
  url=f'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/{commit}/'+urllib.parse.quote(path)
  with urllib.request.urlopen(url,timeout=40) as response:data=response.read();status=response.status
  assert data==expected and data==Path(path).read_bytes();computed=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest();assert computed==blob
  return {'path':path,'url':url,'http_status':status,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':blob,'full_response_body_equals_git_and_local':True}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:receipt['files']=list(pool.map(read,paths))
 remote2=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH]).decode().split()[0];assert remote2==commit
 receipt.update(status='ORDINARY_PUSH_AND_FULL_REMOTE_READBACK_VERIFIED',remote_before_read=remote1,remote_after_read=remote2,file_count=len(paths),bytes=sum(f['bytes'] for f in receipt['files']),worktree_status=run(['git','status','--porcelain','--untracked-files=all']).decode());assert receipt['worktree_status']==''
except Exception as e:
 receipt.update(status='FAILED_PRESERVE_STATE',error=str(e));raise
finally:
 receipt['end_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();Path(args.output).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['status','commit','tree','file_count','bytes','remote_before_read','remote_after_read']}))
