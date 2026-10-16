"""Read only this review's changed blobs from a fresh filtered remote object store.

Usage: python verify_remote.py COMMIT [RECEIPT_NAME]
RECEIPT_NAME, when given, must be a basename under this script directory.
Without a receipt name verification prints its result only (no recursive self-hash).
Git fetch is authenticated using the existing environment; no credential is printed.
No recovered script/reference program is executed.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=next(p for p in OUT.parents if (p/'AGENTS.md').is_file())
PREFIX=OUT.relative_to(ROOT).as_posix()
BASE='35d85e4484b892ebc32542346861440638d2183c'
BRANCH='codex/r8-cp-reception-03-20261016'
COMMIT=sys.argv[1]
assert len(COMMIT)==40 and all(c in '0123456789abcdef' for c in COMMIT)
DEST=sys.argv[2] if len(sys.argv)>2 else None
assert DEST is None or (Path(DEST).name==DEST and DEST.endswith('.json'))
BARE=OUT/'.remote-readback.git'
assert not BARE.exists(), 'Do not overwrite an earlier failed remote readback store'
LOG=[]


def run(args, binary=False):
    start=datetime.now(timezone.utc).isoformat()
    p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    LOG.append(dict(args=args,utc_start=start,utc_end=datetime.now(timezone.utc).isoformat(),
                    exit=p.returncode,stdout_bytes=len(p.stdout),
                    stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),
                    stdout=None if binary else p.stdout.decode(errors='replace'),
                    stderr=p.stderr.decode(errors='replace'),
                    scope='TRANSPORT_OR_IDENTITY_ONLY'))
    if p.returncode:
        print(json.dumps(dict(status='FAILED',commands=LOG),ensure_ascii=False))
        raise SystemExit(p.returncode)
    return p.stdout


local=lambda *a: run(['git','-C',str(ROOT),*a])
remote=lambda *a: run(['git','--git-dir='+str(BARE),*a])
url=local('remote','get-url','origin').decode().strip()
assert url=='https://github.com/y805939188/pokemon-essentials-clean-room.git'
head=local('ls-remote','origin','refs/heads/'+BRANCH).decode().strip().split()
assert head and head[0]==COMMIT, ('remote head differs',head)
changed=local('diff','--name-only',BASE,COMMIT).decode().splitlines()
assert changed and all(p.startswith(PREFIX+'/') for p in changed)
local_tree=local('ls-tree','-r',COMMIT,'--',PREFIX).decode()
local_subtree=local('rev-parse',COMMIT+':'+PREFIX).decode().strip()
run(['git','init','--bare',str(BARE)])
remote('remote','add','origin',url)
remote('fetch','--depth=1','--filter=blob:none','origin',COMMIT)
assert remote('rev-parse','FETCH_HEAD').decode().strip()==COMMIT
remote_tree=remote('ls-tree','-r',COMMIT,'--',PREFIX).decode()
remote_subtree=remote('rev-parse',COMMIT+':'+PREFIX).decode().strip()
assert remote_tree==local_tree and remote_subtree==local_subtree
rows=[]
for line in remote_tree.splitlines():
    left,path=line.split('\t',1)
    mode,typ,blob=left.split()
    assert typ=='blob' and mode=='100644'
    raw=run(['git','--git-dir='+str(BARE),'show',COMMIT+':'+path],binary=True)
    expected=(ROOT/path).read_bytes()
    assert raw==expected, path
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==blob
    rows.append(dict(path=path,mode=mode,git_blob=blob,bytes=len(raw),
                     sha256=hashlib.sha256(raw).hexdigest(),full_remote_bytes_read=True,
                     equals_local_exact_bytes=True))
assert {x['path'] for x in rows}==set(changed)
result=dict(schema='r8-cp03-remote-readback/v1',status='VERIFIED_ALL_OWN_CHANGED_FILES',
            utc=datetime.now(timezone.utc).isoformat(),commit=COMMIT,
            checkout_tree=remote('rev-parse',COMMIT+'^{tree}').decode().strip(),
            task_subtree=remote_subtree,branch=BRANCH,files_count=len(rows),
            files=rows,commands=LOG,
            provenance='Fresh isolated filtered Git remote fetch; shared local object cache not used',
            scope='Only this continuation own changed payloads; global trees are transport metadata, no semantic credit',
            business_executions=0,UPDATE_NOT_STARTED=True)
shutil.rmtree(BARE)
if DEST:
    (OUT/DEST).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='commands'},ensure_ascii=False))
