"""Complete immutable HTTP readback of every result file, bound to remote Git."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request

REPO = Path(__file__).resolve().parents[6]
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH = 'codex/r7-u03-reviewer-20261015-r2'
PREFIX = 'candidates/R7-U03/evidence/reviewer/r2/'

def git(*args):
    return subprocess.check_output(['git','-C',str(REPO),*args])

def identity(d):
    return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest())

commit = sys.argv[1]
output = Path(sys.argv[2])
tree = git('rev-parse',commit+'^{tree}').decode().strip()
remote = git('ls-remote','origin','refs/heads/'+BRANCH).decode().strip()
assert remote.split()[0] == commit, remote
assert git('fetch','--filter=blob:none','--depth=1','--no-tags','origin',commit) == b''
assert git('rev-parse','FETCH_HEAD').decode().strip() == commit
rows=[]
for line in git('diff','--name-status',B,commit).decode().splitlines():
    status,path=line.split('\t')
    assert status=='A' and path.startswith(PREFIX),line
    rows.append(path)

def read(path):
    local=git('show',commit+':'+path)
    expected=identity(local)
    tracked=git('ls-tree',commit,path).decode().split()
    assert tracked[:3]==['100644','blob',expected['git_blob']],tracked
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    with urllib.request.urlopen(url,timeout=40) as response:
        actual=response.read(len(local)+1);status=response.status
    assert status==200 and actual==local,(path,status)
    assert identity(actual)==expected
    return dict(path=path,url=url,http_status=status,start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),complete_response_matches_local_git_bytes=True,**expected)

start=datetime.datetime.now(datetime.timezone.utc).isoformat()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    files=list(pool.map(read,rows))
result=dict(schema='r7-u03-r2.full-remote-readback.v1',commit=commit,tree=tree,branch=BRANCH,
            remote_ref=remote,fetch_head_verified=True,start_utc=start,
            end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            files=files,files_verified=len(files),bytes_verified=sum(r['bytes'] for r in files),
            scope='All additions against fixed B; all ordinary 100644 blobs under r2 only',
            stage='TOOL_VALIDATION',semantic_credit=False,
            qualification='Commit/tree and complete bytes only. Final self-binding is reported outside this Git commit.')
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['commit','tree','branch','files_verified','bytes_verified','stage']}))
