"""Read every result file at a real published commit from immutable raw HTTPS."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request

repo=Path('/workspace/r7-ir-R7-U12/checkout')
prefix='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U12/r1/'
branch='codex/r7-ir-u12-20261015-r1'
commit,destination=sys.argv[1:]
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args):return subprocess.check_output(['git','-C',str(repo),*args])
def ident(data):return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
start=utc()
tip=git('ls-remote','origin','refs/heads/'+branch).decode().strip()
assert tip.split()[0]==commit
tree=git('rev-parse',commit+'^{tree}').decode().strip()
changed=git('diff','--name-only','e646432c644dec04d306842cc5a559a29c718fbc',commit).decode().splitlines()
assert changed and all(path.startswith(prefix) for path in changed)
entries=[]
for item in git('ls-tree','-r','-z',commit,prefix).split(b'\0'):
    if not item:continue
    meta,path=item.split(b'\t');mode,kind,blob=meta.decode().split()
    assert mode=='100644' and kind=='blob'
    entries.append((path.decode(),blob))
assert set(changed)==set(path for path,_ in entries)
def read(row):
    path,blob=row;local=git('show',commit+':'+path)
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
    attempts=[]
    for attempt in range(1,4):
        before=utc()
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R7-U12-actual-IR-readback'}),timeout=40) as response:
                remote=response.read(len(local)+1);status=response.status
            assert remote==local,path
            got=ident(remote);assert got['git_blob']==blob
            attempts.append(dict(attempt=attempt,start_utc=before,end_utc=utc(),http_status=status,complete_byte_match=True))
            return dict(path=path,**got,git_mode='100644',url=url,attempts=attempts)
        except Exception as error:
            attempts.append(dict(attempt=attempt,start_utc=before,end_utc=utc(),error=str(error)))
            if attempt==3:raise RuntimeError(json.dumps(dict(path=path,attempts=attempts))) from error
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    rows=list(pool.map(read,entries))
assert git('ls-remote','origin','refs/heads/'+branch).decode().strip()==tip
result=dict(schema='r7.u12.full-remote-readback.v1',start_utc=start,end_utc=utc(),audit_pid=os.getpid(),
    branch=branch,remote_ref=tip,commit=commit,tree=tree,files=rows,count=len(rows),bytes=sum(r['bytes'] for r in rows),
    complete_exhaustive_tree=True,full_remote_bytes_match=True,all_changes_inside_allowed_prefix=True,
    semantic_PASS=False,behavior_execution='NOT_EXECUTED',configuration='UNVERIFIED',
    self_qualification='This actual readback is produced after its target commit; it never asserts a recursive self hash.')
target=Path(destination);target.parent.mkdir(parents=True,exist_ok=True)
with target.open('x') as stream:json.dump(result,stream,ensure_ascii=False,indent=2);stream.write('\n')
print(json.dumps({k:result[k] for k in ['branch','commit','tree','count','bytes','full_remote_bytes_match','all_changes_inside_allowed_prefix']}))
