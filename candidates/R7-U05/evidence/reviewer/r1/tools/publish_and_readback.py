"""Ordinary push to the sole authorized branch, then exact immutable remote readback."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote
from urllib.request import urlopen

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--commit',required=True)
ap.add_argument('--expected-tip',default='ABSENT')
ap.add_argument('--output',type=Path,required=True)
ap.add_argument('--print-full',action='store_true')
args=ap.parse_args()
assert re.fullmatch('[0-9a-f]{40}',args.commit)
assert args.expected_tip=='ABSENT' or re.fullmatch('[0-9a-f]{40}',args.expected_tip)
OUT=Path(__file__).resolve().parents[1];REPO=Path(__file__).resolve().parents[6]
BOOT=Path('/workspace/r7-review-bootstrap/R7-U05')
destination=args.output.resolve()
assert destination.is_relative_to(OUT) or destination.is_relative_to(BOOT)
assert not destination.exists()
BRANCH='codex/r7-u05-reviewer-20261015-r1';PREFIX='candidates/R7-U05/evidence/reviewer/r1/'
B='e646432c644dec04d306842cc5a559a29c718fbc'
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(data):
 return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())
result=dict(schema='r7.u05.reviewer-ordinary-push-and-full-remote-readback.v1',start_utc=utc(),branch=BRANCH,
            commit=args.commit,expected_previous_remote_tip=args.expected_tip,commands=[],files=[],semantic_or_execution_credit=False)
def command(*argv):
 start=utc();p=subprocess.Popen(argv,cwd=REPO,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 stdout,stderr=p.communicate()
 result['commands'].append(dict(argv=list(argv),cwd=str(REPO),start_utc=start,end_utc=utc(),command_pid=p.pid,
                                exit_code=p.returncode,stdout=stdout.decode(),stderr=stderr.decode()))
 if p.returncode: raise RuntimeError('command failed: '+str(argv))
 return stdout
try:
 assert command('git','branch','--show-current').decode().strip()==BRANCH
 assert command('git','rev-parse','HEAD').decode().strip()==args.commit
 check_tip=command('git','ls-remote','--heads','origin','refs/heads/'+BRANCH).decode().strip()
 assert check_tip==('' if args.expected_tip=='ABSENT' else args.expected_tip+'\trefs/heads/'+BRANCH),'Remote branch collision; protect existing result'
 diff=command('git','diff','--name-only',B,args.commit).decode().splitlines()
 assert diff and all(path.startswith(PREFIX) for path in diff)
 assert not command('git','diff','--name-only',args.commit,'--')
 assert not command('git','ls-files','--others','--exclude-standard')
 command('git','push','origin',args.commit+':refs/heads/'+BRANCH)
 assert command('git','ls-remote','--heads','origin','refs/heads/'+BRANCH).decode().strip()==args.commit+'\trefs/heads/'+BRANCH
 command('git','fetch','--no-tags','origin','refs/heads/'+BRANCH)
 assert command('git','rev-parse','FETCH_HEAD').decode().strip()==args.commit
 result['tree']=command('git','rev-parse',args.commit+'^{tree}').decode().strip()
 result['formal_tree']=command('git','rev-parse',args.commit+':deliverables/final-specification-set').decode().strip()
 assert result['formal_tree']=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
 listing=command('git','ls-tree','-r',args.commit,'--',PREFIX).decode().splitlines()
 rows=[]
 for line in listing:
  metadata,path=line.split('\t');mode,kind,blob=metadata.split()
  assert mode=='100644' and kind=='blob'
  data=subprocess.check_output(['git','show',args.commit+':'+path],cwd=REPO)
  assert (REPO/path).read_bytes()==data
  rows.append((path,blob,data))
 assert sorted(diff)==sorted(row[0] for row in rows)
 def fetch(row):
  path,blob,local=row;url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+args.commit+'/'+quote(path)
  start=utc()
  with urlopen(url,timeout=40) as response: remote=response.read(len(local)+1);status=response.status
  actual=identity(remote)
  assert remote==local and actual['git_blob']==blob
  return dict(path=path,url=url,start_utc=start,end_utc=utc(),http_status=status,git_mode='100644',
              **actual,full_remote_bytes_equal_git_blob_and_local=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: result['files']=list(pool.map(fetch,rows))
 result.update(status='ORDINARY_PUSH_AND_ALL_REMOTE_REVIEWER_BYTES_VERIFIED',files_verified=len(rows),
               bytes_verified=sum(r['bytes'] for r in result['files']),only_authorized_reviewer_paths=True)
except BaseException as error:
 result.update(status='FAILED_REAL_EVIDENCE_PRESERVED',error=str(error))
 raise
finally:
 result['end_utc']=utc();destination.parent.mkdir(parents=True,exist_ok=True)
 with destination.open('x') as stream: json.dump(result,stream,ensure_ascii=False,indent=2);stream.write('\n')
 if args.print_full: print(json.dumps(result,ensure_ascii=False,indent=2))
 else: print(json.dumps({k:result[k] for k in ['status','commit','tree','files_verified','bytes_verified'] if k in result},indent=2))
