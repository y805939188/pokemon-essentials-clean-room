"""Read every new candidate file fully from immutable remote commit URLs."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parents[4]
B='e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH='codex/r7-u03-author-20261015-wave1'
commit=sys.argv[1]
destination=Path(sys.argv[2])
assert len(commit)==40 and all(c in '0123456789abcdef' for c in commit)
assert str(destination.resolve()).startswith('/workspace/r7-bootstrap/R7-U03-author/')
destination.mkdir(parents=True,exist_ok=True)

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(data):return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
    git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())
def command(argv):
    start=utc();p=subprocess.Popen(argv,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE);out,err=p.communicate()
    result=dict(argv=argv,pid=p.pid,start_utc=start,end_utc=utc(),stdout=out.decode(),stderr=err.decode(),exit_code=p.returncode)
    assert p.returncode==0,result
    return result

start=utc()
remote=command(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH])
assert remote['stdout'].strip()==commit+'\trefs/heads/'+BRANCH,remote
fetch=command(['git','fetch','--no-tags','origin','refs/heads/'+BRANCH])
fetched=subprocess.check_output(['git','rev-parse','FETCH_HEAD'],cwd=ROOT).decode().strip();assert fetched==commit
tree=subprocess.check_output(['git','rev-parse',commit+'^{tree}'],cwd=ROOT).decode().strip()
paths=subprocess.check_output(['git','diff','--name-only',B,commit],cwd=ROOT).decode().splitlines()
assert paths and all(p.startswith('candidates/R7-U03/') for p in paths)

def read_one(path):
    expected=subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
    began=utc()
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'R7-U03-author-fixed-commit-readback'})
        with urllib.request.urlopen(request,timeout=40) as response:
            data=response.read(len(expected)+1);status=response.status
        assert status==200 and data==expected,(path,status,identity(data),identity(expected))
        output=destination/'files'/path;output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(data)
        return dict(path=path,url=url,start_utc=began,end_utc=utc(),http_status=status,full_bytes_equal=True,
            **identity(data),qualification='Actual complete HTTP read; identity only, no semantic acceptance.')
    except Exception as error:
        return dict(path=path,url=url,start_utc=began,end_utc=utc(),error=str(error),full_bytes_equal=False)

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    files=list(pool.map(read_one,paths))
ok=all(row['full_bytes_equal'] for row in files)
receipt=dict(schema='r7-u03-full-remote-readback.v1',start_utc=start,end_utc=utc(),commit=commit,tree=tree,branch=BRANCH,
    remote_branch_command=remote,remote_fetch_command=fetch,fetch_head=fetched,files=files,new_file_count=len(paths),
    all_complete_remote_bytes_equal=ok,stage='TOOL_VALIDATION',semantic_PASS=False,reference_host_execution=0)
target=destination/'receipt.json';target.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(commit=commit,tree=tree,new_file_count=len(paths),all_complete_remote_bytes_equal=ok,
    receipt=str(target),receipt_identity=identity(target.read_bytes()),semantic_PASS=False)))
sys.exit(0 if ok else 1)
