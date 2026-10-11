#!/usr/bin/env python3
"""NEW2 report-only independent remote Git readback; no project/reference execution."""
import hashlib, json, pathlib, subprocess, sys
S, destination = sys.argv[1:3]
repo='https://github.com/y805939188/pokemon-essentials-clean-room.git'
branch='codex/cloud-B21-NEW2-affected-independent-20261011'
base='9b6d16e34daf59e205f8a3df20e24930175064ed'
root='review/remediation/20261003-prepare/batches/B21/affected-review-cloud-20261011-2'
bare=pathlib.Path('/tmp/b21-new2-independent-remote-readback.git')
def run(*args): return subprocess.check_output(args)
if not bare.exists():
    subprocess.check_call(['git','init','--bare','--quiet',str(bare)])
    subprocess.check_call(['git','--git-dir='+str(bare),'remote','add','origin',repo])
assert not (bare/'objects/info/alternates').exists(), 'Local object alternates forbidden'
subprocess.check_call(['git','--git-dir='+str(bare),'config','remote.origin.promisor','true'])
subprocess.check_call(['git','--git-dir='+str(bare),'config','remote.origin.partialclonefilter','blob:none'])
subprocess.check_call(['git','--git-dir='+str(bare),'fetch','--depth=1','--filter=blob:none','--no-tags','origin','refs/heads/'+branch])
def remote(*args):return run('git','--git-dir='+str(bare),*args)
tip=remote('rev-parse','FETCH_HEAD').decode().strip()
assert tip==S, 'Remote tip does not equal requested exact report commit'
fields=remote('show','-s','--format=%H %T %P',S).decode().split()
paths=remote('ls-tree','-r','--name-only',S,root).decode().splitlines()
assert paths, 'No report outputs found'
outputs=[]
for p in paths:
    data=remote('show',S+':'+p)
    local=run('git','show',S+':'+p)
    assert data==local, 'Remote committed bytes mismatch: '+p
    outputs.append(dict(commit=S,path=p,git_blob=hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest(),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),remote_equals_local_committed=True))
delta=run('git','diff','--name-status',base,S).decode().splitlines()
assert all(x.startswith('A\t'+root+'/') for x in delta), 'Old or unapproved paths changed'
result=dict(kind='INDEPENDENT_NEW2_REPORT_REMOTE_READBACK_ONLY',repository='y805939188/pokemon-essentials-clean-room',reviewed_NEW2='e58486178e746273fb6fab55df00722807f1dc44',report_branch=branch,report_commit=S,report_tree=fields[1],report_parents=fields[2:],remote_tip=tip,source_remote_url=repo,independent_remote_object_store=str(bare),local_object_alternates_used=False,method='Remote fetch into independently initialized bare object store; every report path read from remote objects and independently SHA256/Git-blob hashed; byte compared with local committed objects',output_count=len(outputs),outputs=outputs,all_outputs_match=True,all_delta_paths_new_report_only=delta,actual_or_B21_C_or_closure_or_FINAL_signed=False,reference_or_project_program_execution=0,static_cases_executed=False)
pathlib.Path(destination).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(report_commit=S,report_tree=fields[1],output_count=len(outputs),all_outputs_match=True,only_new_report_paths=True)))
