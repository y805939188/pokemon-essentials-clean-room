"""Read every published result byte from immutable remote URLs and compare Git blobs."""
from pathlib import Path
import datetime, hashlib, json, os, subprocess, sys, urllib.parse, urllib.request

ROOT=Path('/workspace/r7-ir-R7-U09/checkout')
B='e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH='codex/r7-ir-u09-20261015-r1'
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U09/r1/'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def identity(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest())
commit=git('rev-parse','HEAD').decode().strip();tree=git('rev-parse','HEAD^{tree}').decode().strip()
start=utc();before=git('ls-remote','--heads','origin','refs/heads/'+BRANCH).decode().strip();assert before.split()[0]==commit
files=git('diff','--name-only','-z',B,commit).decode().strip('\0').split('\0');rows=[]
for p in files:
    assert p.startswith(PREFIX)
    blob=git('show',commit+':'+p); expected=identity(blob)
    url=f'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/{commit}/'+urllib.parse.quote(p)
    s=utc()
    with urllib.request.urlopen(url,timeout=40) as r:data=r.read(expected['bytes']+1);status=r.status
    assert data==blob,p
    mode,kind,sha=git('ls-tree',commit,'--',p).decode().split('\t')[0].split();assert mode=='100644' and kind=='blob' and sha==expected['git_blob']
    rows.append(dict(path=p,url=url,http_status=status,start_utc=s,end_utc=utc(),**expected,complete_remote_bytes_equal_git_blob=True))
after=git('ls-remote','--heads','origin','refs/heads/'+BRANCH).decode().strip();assert before==after
result=dict(schema='r7.u09.actual-review-complete-remote-readback.v1',start_utc=start,end_utc=utc(),pid=os.getpid(),branch=BRANCH,commit=commit,tree=tree,fixed_B=B,remote_ref_before=before,remote_ref_after=after,files=rows,files_verified=len(rows),bytes_verified=sum(x['bytes'] for x in rows),all_complete_remote_bytes_matched=True,qualification='Immutable full-byte transport and exact Git tree/blob validation only; no semantic/model/runtime certificate.')
Path(sys.argv[1]).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
