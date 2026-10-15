"""Ordinary push to the sole authorized reviewer branch and full pinned HTTP readback.

The receipt is detached outside the checkout. No author or reference code runs.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT=Path('/workspace/r7-u13-reviewer-checkout')
SCOPE='candidates/R7-U13/evidence/reviewer/r1/'
BRANCH='codex/r7-u13-reviewer-20261015-r1'
B='e646432c644dec04d306842cc5a559a29c718fbc'
THREAD='01a13ff1-4e91-74b4-ac83-5838dbb59018'
parser=argparse.ArgumentParser()
parser.add_argument('--phase',choices=['initial','final'],required=True)
parser.add_argument('--receipt',type=Path,required=True)
args=parser.parse_args()
assert args.receipt.parent==Path('/workspace/r7-review-bootstrap/R7-U13-r1')
assert not args.receipt.exists()
assert os.environ['CODEX_THREAD_ID']==THREAD
operations=[]
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def run(argv):
    start=utc();process=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True)
    operations.append(dict(start_utc=start,end_utc=utc(),argv=argv,stdout=process.stdout,stderr=process.stderr,exit_code=process.returncode))
    assert process.returncode==0,operations[-1]
    return process.stdout.strip()
def identity(data): return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

start=utc()
assert run(['git','branch','--show-current'])==BRANCH
assert run(['git','remote','get-url','origin'])=='https://github.com/y805939188/pokemon-essentials-clean-room.git'
assert run(['git','status','--porcelain=v1'])==''
commit=run(['git','rev-parse','HEAD']);tree=run(['git','rev-parse','HEAD^{tree}']);parent=run(['git','rev-parse','HEAD^'])
changes=[line.split('\t') for line in run(['git','diff','--name-status',B,commit]).splitlines()]
assert changes and all(status=='A' and path.startswith(SCOPE) for status,path in changes)
before=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH])
if args.phase=='initial':
    assert parent==B
    assert not before, 'Existing reviewer branch protected; ownership is not inferred.'
else:
    first=json.loads((ROOT/SCOPE/'tools/first-push-readback.json').read_bytes())
    assert first['reviewer_thread']==THREAD and parent==first['commit']
    assert before.split()[0]==parent, 'Unexpected remote state protected; no force or alternate branch.'
run(['git','push','origin','HEAD:refs/heads/'+BRANCH])
run(['git','fetch','--no-tags','origin','refs/heads/'+BRANCH])
assert run(['git','rev-parse','FETCH_HEAD'])==commit
assert run(['git','rev-parse','FETCH_HEAD^{tree}'])==tree
after=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH])
assert after.split()[0]==commit
entries=[]
for raw in subprocess.check_output(['git','ls-tree','-rz',commit,SCOPE],cwd=ROOT).split(b'\0'):
    if not raw: continue
    metadata,path=raw.split(b'\t');mode,kind,blob=metadata.decode().split();path=path.decode()
    assert mode=='100644' and kind=='blob' and path.startswith(SCOPE)
    entries.append((path,blob))
assert {x[1] for x in changes}=={path for path,blob in entries}

def readback(item):
    path,blob=item
    local=subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
    attempts=[]
    for attempt in range(1,4):
        begin=utc()
        try:
            request=urllib.request.Request(url,headers={'User-Agent':'R7-U13-independent-reviewer-pinned-byte-readback','Cache-Control':'no-cache'})
            with urllib.request.urlopen(request,timeout=40) as response:
                data=response.read(len(local)+1);status=response.status
            actual=identity(data)
            assert data==local and actual['git_blob_content_id']==blob
            attempts.append(dict(attempt=attempt,start_utc=begin,end_utc=utc(),http_status=status,full_bytes_read=True))
            return dict(path=path,url=url,expected_mode='100644',expected_blob_from_tree=blob,remote=actual,full_byte_equal=True,attempts=attempts)
        except (urllib.error.URLError,TimeoutError) as error:
            attempts.append(dict(attempt=attempt,start_utc=begin,end_utc=utc(),error=str(error)))
            if isinstance(error,urllib.error.HTTPError) and error.code not in [429,500,502,503,504]: raise
            if attempt==3: raise
            time.sleep(attempt)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    files=list(pool.map(readback,entries))
assert run(['git','status','--porcelain=v1'])==''
receipt=dict(schema='r7-u13-reviewer-full-remote-readback.v1',phase=args.phase,start_utc=start,end_utc=utc(),
    reviewer_thread=THREAD,tool_pid=os.getpid(),tool_parent_pid=os.getppid(),model_process_pid='NOT_EXPOSED',
    branch=BRANCH,base=B,commit=commit,tree=tree,parent=parent,ordinary_push_only=True,
    remote_before=before,remote_after=after,git_operations=operations,files=files,
    files_read_back=len(files),bytes_read_back=sum(x['remote']['bytes'] for x in files),
    all_full_remote_bytes_sha256_blob_equal=True,worktree_clean=True,verdict='PASS_SCOPED_CANDIDATE',
    configuration='UNVERIFIED',behavior='NOT_EXECUTED',reference_host_Demo_native_media_real_save_replay=0,
    integrated_PASS=False,ACCEPTED=False,CLOSED=False,qualification='Full Git/HTTP byte readback only. Semantic candidate judgment is in the independently authored report. Final receipt remains detached to avoid recursive self-binding.')
with args.receipt.open('x') as stream: stream.write(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
