"""Fetch an exact published commit, then read every task blob in full.

Uses the isolated task-owned bare repository, never local alternates or a local
origin. This validates transport/identity only, not semantic reading or behavior.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, subprocess

TASK=Path(__file__).resolve().parent
REPO=next(p for p in TASK.parents if (p/'.git').exists())
REL=TASK.relative_to(REPO).as_posix()
BARE=TASK/'remote-verification.git'/'bare'
ORIGIN='https://github.com/y805939188/pokemon-essentials-clean-room.git'
BRANCH='codex/r8-external-h-early-qualifications-20261016'

def run(args, **kwargs):
    return subprocess.check_output(args, **kwargs)

def git(*args):
    return run(['git',*args],cwd=REPO)

def remote(*args):
    return run(['git','--git-dir='+str(BARE),*args])

ap=argparse.ArgumentParser()
ap.add_argument('--commit',required=True)
ap.add_argument('--output',required=True)
a=ap.parse_args()
out=(TASK/a.output).resolve()
assert out.is_relative_to(TASK) and not out.is_symlink()
assert len(a.commit)==40 and all(c in '0123456789abcdef' for c in a.commit)
if not BARE.exists():
    subprocess.run(['git','init','--bare',str(BARE)],check=True,capture_output=True)
assert not (BARE/'objects/info/alternates').exists()
fetch=subprocess.run(['git','--git-dir='+str(BARE),'fetch','--no-tags','--depth=1',ORIGIN,a.commit],capture_output=True,text=True,check=True)
assert remote('rev-parse','FETCH_HEAD').decode().strip()==a.commit
branch=git('ls-remote',ORIGIN,'refs/heads/'+BRANCH).decode().strip()
assert branch.split()[0]==a.commit
raw=remote('ls-tree','-rz',a.commit,'--',REL)
assert raw==git('ls-tree','-rz',a.commit,'--',REL)
files=[]
for row in raw.split(b'\0'):
    if not row:continue
    meta,path=row.split(b'\t',1)
    mode,kind,blob=meta.decode().split()
    assert kind=='blob' and mode in {'100644','100755'}
    data=remote('cat-file','blob',blob)
    local=git('cat-file','blob',blob)
    assert data==local
    calculated=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert calculated==blob
    files.append(dict(path=path.decode(),mode=mode,git_blob=blob,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),full_remote_body_read=True))
workspace_tree=remote('rev-parse',a.commit+'^{tree}').decode().strip()
task_tree=remote('rev-parse',a.commit+':'+REL).decode().strip()
assert workspace_tree==git('rev-parse',a.commit+'^{tree}').decode().strip()
assert task_tree==git('rev-parse',a.commit+':'+REL).decode().strip()
protected=git('ls-remote',ORIGIN,'refs/heads/main','refs/tags/delivery/seventh-round-closed-final-20261016').decode().strip()
assert len(protected.splitlines())==2
assert all(x.split()[0]=='fd1df570cad987dc3852a3b958f03916e317f7fe' for x in protected.splitlines())
record=dict(schema='r8.external-h.remote-full-body-readback.v1',utc=datetime.now(timezone.utc).isoformat(),
    commit=a.commit,workspace_tree=workspace_tree,task_tree=task_tree,branch=branch,
    remote=ORIGIN,isolated_bare=str(BARE),alternates=False,
    fetch={'exit':fetch.returncode,'stdout':fetch.stdout,'stderr':fetch.stderr},
    files_total=len(files),files_fully_read=len(files),bytes_total=sum(f['bytes'] for f in files),
    files=files,protected_refs=protected,all_identities_match=True,
    semantic_credit=False,new_behavior_execution=0,final_state='UPDATE_NOT_STARTED')
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['commit','workspace_tree','task_tree','files_total','files_fully_read','bytes_total','all_identities_match','protected_refs']},ensure_ascii=False))
