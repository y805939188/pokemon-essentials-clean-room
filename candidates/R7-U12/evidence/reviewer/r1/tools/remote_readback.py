"""Read back one actual pushed reviewer commit; compare every full result file.

Write the receipt outside the commit under review to avoid a recursive self hash.
"""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request

OUT=Path(__file__).resolve().parents[1]
REPO=OUT.parents[4]
BRANCH='codex/r7-u12-reviewer-20261015-r1'
B='e646432c644dec04d306842cc5a559a29c718fbc'
PREFIX='candidates/R7-U12/evidence/reviewer/r1/'
commit,receipt_path=sys.argv[1:]
assert len(commit)==40 and all(c in '0123456789abcdef' for c in commit)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
commands=[]
def run(argv,cwd):
    start=now();p=subprocess.run(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    commands.append({'argv':argv,'cwd':str(cwd),'start_utc':start,'end_utc':now(),'exit_code':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()})
    if p.returncode:raise RuntimeError(commands[-1])
    return p.stdout
def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args])
start=now()
tip=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH],REPO)
assert tip.decode().split()[0]==commit
remote_repo=Path('/workspace/r7-remote-readback/R7-U12-r1-'+commit)
assert not remote_repo.exists(), 'Preserve existing receipt directory; do not overwrite'
remote_repo.parent.mkdir(exist_ok=True)
run(['git','init','--bare',str(remote_repo)],REPO)
run(['git','-C',str(remote_repo),'fetch','--filter=blob:none','--no-tags','--depth=1',
     'https://github.com/y805939188/pokemon-essentials-clean-room.git',commit],REPO)
remote_tree=run(['git','-C',str(remote_repo),'rev-parse','FETCH_HEAD^{tree}'],REPO).decode().strip()
local_tree=git('rev-parse',commit+'^{tree}').decode().strip()
assert remote_tree==local_tree
remote_files=run(['git','-C',str(remote_repo),'ls-tree','-r',commit,PREFIX],REPO)
assert remote_files==git('ls-tree','-r',commit,PREFIX)
diff=git('diff','--name-status',B,commit).decode().splitlines()
assert all(s.startswith('A\t'+PREFIX) for s in diff)
paths=[s.split('\t',1)[1] for s in diff]
assert len(paths)==len(remote_files.decode().splitlines())
def get(path):
    a=now();expected=git('show',commit+':'+path)
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
    with urllib.request.urlopen(url,timeout=40) as response:
        data=response.read(len(expected)+1);status=response.status
    assert data==expected, path
    return {'path':path,'url':url,'start_utc':a,'end_utc':now(),'http_status':status,**ident(data),'full_byte_for_byte_match':True}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(get,paths))
tip_after=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH],REPO)
assert tip_after==tip
result={'schema':'r7.u12.reviewer-full-remote-readback.v1','start_utc':start,'end_utc':now(),'branch':BRANCH,
        'commit':commit,'tree':remote_tree,'remote_tip_before_after_match':True,'files':rows,'file_count':len(rows),
        'bytes_verified':sum(r['bytes'] for r in rows),'complete_scope_against_B':diff,'commands':commands,
        'status':'COMPLETE_REMOTE_BYTES_VERIFIED','stage':'TOOL_VALIDATION','semantic_verdict':'See fixed report; no integration/acceptance/closure certificate'}
target=Path(receipt_path);target.parent.mkdir(parents=True,exist_ok=True)
with target.open('x') as stream:json.dump(result,stream,ensure_ascii=False,indent=2);stream.write('\n')
print(json.dumps({k:result[k] for k in ['status','branch','commit','tree','file_count','bytes_verified','remote_tip_before_after_match']},ensure_ascii=False))
print(json.dumps({'receipt':str(target),**ident(target.read_bytes())},ensure_ascii=False))
