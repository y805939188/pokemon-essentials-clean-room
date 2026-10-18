"""Read back only this receiver's published increment in a fresh isolated bare.

Usage: python verify_publication.py CORE_COMMIT NEW_EMPTY_BARE_PATH
Writes publication.json next to this file. No remote mutations or game execution.
"""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

OUT = Path(__file__).resolve().parent
REPO = next(p for p in OUT.parents if (p / '.git').is_dir())
PREFIX = OUT.relative_to(REPO).as_posix()
CORE, bare_argument = sys.argv[1:]
BARE = Path(bare_argument)
assert not BARE.exists()
BRANCH = 'codex/r8-cp-reception-05-20261016'
BASE = '35d85e4484b892ebc32542346861440638d2183c'
ORIGIN = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
commands = []


def run(args, log_output=True):
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    commands.append(dict(args=args, exit=proc.returncode,
                         stderr=proc.stderr.decode(errors='replace'),
                         stdout=proc.stdout.decode(errors='replace') if log_output else '<binary payload hashed separately>'))
    assert proc.returncode == 0, commands[-1]
    return proc.stdout


def local(*args):
    return run(['git','-C',str(REPO),*args], False)


def remote(*args):
    return run(['git','--git-dir='+str(BARE),*args], False)


run(['git','init','--bare',str(BARE)])
run(['git','--git-dir='+str(BARE),'remote','add','origin',ORIGIN])
run(['git','--git-dir='+str(BARE),'fetch','--no-tags','--depth=1','--filter=blob:none','origin','refs/heads/'+BRANCH])
remote_head = remote('rev-parse','FETCH_HEAD').decode().strip()
assert remote_head == CORE, (CORE,remote_head)
local_tree = local('rev-parse',CORE+'^{tree}').decode().strip()
remote_tree = remote('rev-parse',CORE+'^{tree}').decode().strip()
assert local_tree == remote_tree
task_tree = local('rev-parse',CORE+':'+PREFIX).decode().strip()
assert task_tree == remote('rev-parse',CORE+':'+PREFIX).decode().strip()
left = local('ls-tree','-r',CORE,'--',PREFIX)
right = remote('ls-tree','-r',CORE,'--',PREFIX)
assert left == right
changed = local('diff','--name-only',BASE,CORE).decode().splitlines()
assert changed and all(x.startswith(PREFIX+'/') for x in changed)
rows=[]
for line in left.decode().splitlines():
    metadata,path = line.split('\t',1)
    mode,kind,blob = metadata.split()
    assert kind == 'blob'
    expected = local('cat-file','blob',blob)
    actual = remote('cat-file','blob',blob)
    assert expected == actual
    rows.append(dict(path=path,mode=mode,git_blob=blob,bytes=len(actual),
                     sha256=hashlib.sha256(actual).hexdigest(),complete_readback=True))
assert {x['path'] for x in rows} == set(changed)
receipt=dict(schema='r8-cp05-publication/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    status='ALL_OWN_CORE_INCREMENT_READ_BACK',branch=BRANCH,core_commit=CORE,
    core_tree=local_tree,core_task_tree=task_tree,base_commit=BASE,
    remote_head_at_read=remote_head,isolated_bare=str(BARE),
    all_files=rows,file_count=len(rows),total_bytes=sum(x['bytes'] for x in rows),
    file_set_mode_blob_bytes_sha256_and_trees_match=True,
    upstream_inputs='Reused fixed contract cache; not downloaded again or given semantic credit.',
    command_receipts=commands,semantic_credit=0,business_executions=0,
    final_receipt_self_binding='This successor file binds core only. Its own final commit/blob is verified separately without recursive self-hash.',
    UPDATE_NOT_STARTED=True)
(OUT/'publication.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ('status','core_commit','core_tree','core_task_tree','file_count','total_bytes')},ensure_ascii=False))
