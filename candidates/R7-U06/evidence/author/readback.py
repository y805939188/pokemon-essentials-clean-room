"""Full-byte immutable GitHub readback of every file changed from B; no push."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import urllib.error

B='e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH='codex/r7-u06-author-20261015-wave1'
REPO='y805939188/pokemon-essentials-clean-room'
def git(*args):return subprocess.check_output(['git',*args])
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
        git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())
commit=git('rev-parse','HEAD').decode().strip()
tree=git('rev-parse','HEAD^{tree}').decode().strip()
remote=git('ls-remote','--heads','origin','refs/heads/'+BRANCH).decode()
assert remote.split()[0]==commit,remote
paths=git('diff','--name-only',B,commit).decode().splitlines()
assert paths and all(p.startswith('candidates/R7-U06/') for p in paths)
def one(path):
    expected=git('show',commit+':'+path)
    url=f'https://raw.githubusercontent.com/{REPO}/{commit}/'+urllib.parse.quote(path)
    attempts=[]
    for attempt in range(1,4):
        start=utc()
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R7-U06-full-readback'}),timeout=40) as response:
                actual=response.read(len(expected)+1)
                status=response.status
            assert actual==expected,path
            row=dict(path=path,url=url,**identity(actual),expected_git_blob=git('rev-parse',commit+':'+path).decode().strip(),
                start_utc=start,end_utc=utc(),http_status=status,complete_byte_match=True,attempt=attempt)
            assert row['git_blob_content_id']==row['expected_git_blob']
            return row
        except (urllib.error.URLError,TimeoutError) as error:
            attempts.append(dict(attempt=attempt,start_utc=start,end_utc=utc(),error=str(error)))
            if attempt==3:raise
            time.sleep(attempt)
    raise AssertionError(path)
receipt=dict(schema='r7.u06.full-remote-readback.v1',commit=commit,tree=tree,branch=BRANCH,
    remote_ref_stdout=remote,start_utc=utc(),files=[],semantic_acceptance=False)
try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        receipt['files']=list(pool.map(one,paths))
    receipt['status']='ALL_NEW_FILES_FULL_REMOTE_BYTES_VERIFIED'
except Exception as error:
    receipt['status']='READBACK_INCOMPLETE'
    receipt['error']=str(error)
    raise
finally:
    receipt['end_utc']=utc()
    target=Path(sys.argv[1]);target.parent.mkdir(parents=True,exist_ok=True)
    assert not target.exists()
    target.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':receipt['status'],'commit':commit,'tree':tree,'files':len(receipt['files']),
    'bytes':sum(r['bytes'] for r in receipt['files']),'receipt':str(target)}))
