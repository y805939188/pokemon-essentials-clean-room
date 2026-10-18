"""Read complete published task blobs from an independent bare remote store.

Call with a commit already ordinary-pushed and a receipt path below this task.
Uses no alternates/local object cache. Its own final receipt is bound externally.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess

task=Path(__file__).resolve().parent.parent
root=task.parent.parent
repo=root.parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('commit')
parser.add_argument('receipt')
args=parser.parse_args()
assert len(args.commit)==40 and all(c in '0123456789abcdef' for c in args.commit)
receipt=(task/args.receipt).resolve()
assert receipt.is_relative_to(task)
branch='codex/r8-receive-com-battler-20261016'
url='https://github.com/y805939188/pokemon-essentials-clean-room.git'
bare=task/'evidence/readback.git'
def cmd(*argv): return subprocess.check_output(argv,stderr=subprocess.PIPE)
if not bare.exists():
    cmd('git','init','--bare',str(bare))
    cmd('git',f'--git-dir={bare}','remote','add','origin',url)
    cmd('git',f'--git-dir={bare}','config','remote.origin.promisor','true')
    cmd('git',f'--git-dir={bare}','config','remote.origin.partialclonefilter','blob:none')
cmd('git',f'--git-dir={bare}','fetch','--depth=1','--filter=blob:none','--no-tags','origin',branch)
def remote(*argv): return cmd('git',f'--git-dir={bare}',*argv)
actual=remote('rev-parse','FETCH_HEAD').decode().strip()
assert actual==args.commit,(actual,args.commit)
assert not (bare/'objects/info/alternates').exists()
task_path=str(task.relative_to(repo))
entries=remote('ls-tree','-r',args.commit,task_path).decode().splitlines()
local_entries=cmd('git','-C',str(repo),'ls-tree','-r',args.commit,task_path).decode().splitlines()
assert entries==local_entries
files=[]
for entry in entries:
    meta,path=entry.split('\t'); mode,kind,blob=meta.split()
    assert kind=='blob' and mode=='100644',(path,kind,mode)
    data=remote('cat-file','blob',blob)
    local=cmd('git','-C',str(repo),'cat-file','blob',blob)
    assert data==local
    assert data==(repo/path).read_bytes()
    if path.endswith('.json'): json.loads(data)
    files.append({'path':path,'mode':mode,'blob':blob,'bytes':len(data),
      'sha256':hashlib.sha256(data).hexdigest(),'complete_remote_bytes_equal':True})
tree=remote('rev-parse',args.commit+'^{tree}').decode().strip()
task_tree=remote('rev-parse',args.commit+':'+task_path).decode().strip()
assert tree==cmd('git','-C',str(repo),'rev-parse',args.commit+'^{tree}').decode().strip()
assert task_tree==cmd('git','-C',str(repo),'rev-parse',args.commit+':'+task_path).decode().strip()
refs=cmd('git','ls-remote',url,'refs/heads/'+branch,'refs/heads/main',
         'refs/tags/delivery/seventh-round-closed-final-20261016').decode()
assert args.commit+'\trefs/heads/'+branch in refs
assert 'fd1df570cad987dc3852a3b958f03916e317f7fe\trefs/heads/main' in refs
assert 'fd1df570cad987dc3852a3b958f03916e317f7fe\trefs/tags/delivery/seventh-round-closed-final-20261016' in refs
changed=cmd('git','-C',str(repo),'diff','--name-only',
 '40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',args.commit).decode().splitlines()
assert all(p.startswith(task_path+'/') for p in changed)
result={'schema':'r8-com-battler-full-remote-readback/v1',
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'branch':branch,'commit':args.commit,
 'workspace_tree':tree,'task_tree':task_tree,'file_count':len(files),
 'total_bytes':sum(x['bytes'] for x in files),'files':files,
 'isolated_bare':str(bare),'alternates':False,'fetch':'remote depth1 blob:none, then complete remote blob reads',
 'remote_refs':refs.splitlines(),'changed_paths_from_contract':changed,
 'file_set_mode_blob_bytes_sha256_tree':'ALL_MATCH','task_status':'INCOMPLETE',
 'semantic_credit':0,'behavior_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['files','changed_paths_from_contract','remote_refs']}))
