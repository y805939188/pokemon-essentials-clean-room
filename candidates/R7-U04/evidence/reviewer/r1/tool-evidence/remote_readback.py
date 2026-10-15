"""Reviewer-owned full immutable HTTP readback, bound to one authorized branch."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import urllib.parse
import urllib.request

OUT=Path(__file__).resolve().parent
REPO=OUT.parents[5]
BRANCH='codex/r7-u04-reviewer-20261015-r1'
PREFIX='candidates/R7-U04/evidence/reviewer/r1/'
BASE='e646432c644dec04d306842cc5a559a29c718fbc'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--commit',required=True)
parser.add_argument('--receipt',type=Path)
args=parser.parse_args()
assert re.fullmatch('[a-f0-9]{40}',args.commit)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*argv):return subprocess.check_output(['git',*argv],cwd=REPO)
def head():
    value=git('ls-remote','--exit-code','--heads','origin',BRANCH).decode()
    assert value==args.commit+'\trefs/heads/'+BRANCH+'\n',value
    return value
started=now()
before=head()
tree=git('rev-parse',args.commit+'^{tree}').decode().strip()
paths=git('diff','--name-only',BASE,args.commit).decode().splitlines()
assert paths and all(p.startswith(PREFIX) for p in paths)
entries=git('ls-tree','-r',args.commit,'--',PREFIX).decode().splitlines()
expected={}
for row in entries:
    header,path=row.split('\t'); mode,kind,blob=header.split()
    assert mode=='100644' and kind=='blob'
    expected[path]=blob
assert sorted(paths)==sorted(expected)
def read(path):
    original=git('show',args.commit+':'+path)
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+args.commit+'/'+urllib.parse.quote(path)
    start=now()
    request=urllib.request.Request(url,headers={'User-Agent':'R7-U04-independent-reviewer-r1-full-readback'})
    with urllib.request.urlopen(request,timeout=40) as response:
        data=response.read(len(original)+1);status=response.status
    assert data==original and status==200,path
    blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
    assert blob==expected[path]
    return dict(path=path,url=url,git_mode='100644',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=blob,start_utc=start,end_utc=now(),http_status=status,full_response_body_equal=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:files=list(pool.map(read,paths))
after=head()
result=dict(schema='r7.u04.r1.remote-readback.v1',status='REMOTE_COMPLETE_BYTES_MATCH',start_utc=started,end_utc=now(),branch=BRANCH,commit=args.commit,tree=tree,ls_remote_before=before,ls_remote_after=after,file_count=len(files),total_bytes=sum(x['bytes'] for x in files),files=files,all_changes_within_authorized_prefix=True,semantic_credit_from_transport=0,formal_ACCEPTED=False,CLOSED=False)
if args.receipt:
    dest=args.receipt.resolve()
    assert dest.parent==OUT
    with dest.open('x') as stream:stream.write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
