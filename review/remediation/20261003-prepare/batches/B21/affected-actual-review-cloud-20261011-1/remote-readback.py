#!/usr/bin/env python3
"""Fresh independent Git remote byte readback of this actual review's outputs."""
import argparse,hashlib,json,pathlib,subprocess
ap=argparse.ArgumentParser();ap.add_argument('--commit',required=True);ap.add_argument('--tree',required=True);ap.add_argument('--branch',required=True);ap.add_argument('--report-dir',required=True);ap.add_argument('--baseline',required=True);ap.add_argument('--bare',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
repo='/workspace/b21-review';remote='https://github.com/y805939188/pokemon-essentials-clean-room.git'
def run(*cmd):return subprocess.check_output(cmd)
def local(*args):return run('git','-C',repo,*args)
bare=pathlib.Path(a.bare)
if not bare.exists():run('git','init','--bare',str(bare));run('git','-C',str(bare),'remote','add','origin',remote)
def fetched(*args):return run('git','-C',str(bare),*args)
assert not (bare/'objects/info/alternates').exists(), 'independent store must not use local alternates'
assert fetched('config','--get','remote.origin.url').decode().strip()==remote
advertised=run('git','ls-remote',remote,'refs/heads/'+a.branch).decode().split()
assert advertised[0]==a.commit, 'advertised branch must identify exact published commit'
fetched('fetch','--depth=1','--filter=blob:none','origin',a.commit)
assert fetched('rev-parse',a.commit+'^{tree}').decode().strip()==a.tree
files=local('ls-tree','-r','--name-only',a.commit,'--',a.report_dir).decode().splitlines()
assert files, 'outputs required'
outputs=[]
for p in files:
    remote_bytes=fetched('show',a.commit+':'+p);local_bytes=local('show',a.commit+':'+p)
    blob=hashlib.sha1(b'blob '+str(len(remote_bytes)).encode()+b'\0'+remote_bytes).hexdigest()
    expected=fetched('rev-parse',a.commit+':'+p).decode().strip()
    assert remote_bytes==local_bytes and blob==expected, p
    outputs.append(dict(path=p,git_blob=blob,sha256=hashlib.sha256(remote_bytes).hexdigest(),bytes=len(remote_bytes),full_remote_bytes_match=True))
delta=local('diff','--no-renames','--name-status',a.baseline,a.commit).decode().splitlines()
assert all(x.startswith('A\t'+a.report_dir+'/') for x in delta), 'only new report paths authorized'
assert len(delta)==len(files)
result=dict(kind='INDEPENDENT_REMOTE_FULL_BYTE_REPORT_READBACK',published_commit=a.commit,published_tree=a.tree,branch=a.branch,remote=remote,base_management=a.baseline,independent_bare_store=str(bare),no_local_alternates=True,remote_advertised_branch_matches=True,output_count=len(outputs),outputs=outputs,all_outputs_match=True,only_new_report_paths=True,changed_paths=delta,no_recursive_diff_copy=True,reference_program_execution=0,static_cases_executed=False)
pathlib.Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(commit=a.commit,tree=a.tree,output_count=len(outputs),all_outputs_match=True,only_new_report_paths=True)))
