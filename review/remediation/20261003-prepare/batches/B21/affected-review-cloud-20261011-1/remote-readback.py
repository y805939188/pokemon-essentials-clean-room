#!/usr/bin/env python3
"""Fresh remote Git object store; verify every independent report output."""
import hashlib, json, pathlib, subprocess, sys
S=sys.argv[1]
OUT=sys.argv[2]
repo='https://github.com/y805939188/pokemon-essentials-clean-room.git'
branch='codex/cloud-B21-affected-independent-20261011'
R='review/remediation/20261003-prepare/batches/B21/affected-review-cloud-20261011-1'
bare=pathlib.Path('/tmp/b21-independent-remote-readback.git')
def run(*args): return subprocess.check_output(args)
if not bare.exists():
    subprocess.check_call(['git','init','--bare','--quiet',str(bare)])
    subprocess.check_call(['git','--git-dir='+str(bare),'remote','add','origin',repo])
subprocess.check_call(['git','--git-dir='+str(bare),'config','remote.origin.promisor','true'])
subprocess.check_call(['git','--git-dir='+str(bare),'config','remote.origin.partialclonefilter','blob:none'])
subprocess.check_call(['git','--git-dir='+str(bare),'-c','remote.origin.promisor=true','-c','remote.origin.partialclonefilter=blob:none','fetch','--depth=1','--filter=blob:none','--no-tags','origin','refs/heads/'+branch])
def remote(*args): return run('git','--git-dir='+str(bare),*args)
tip=remote('rev-parse','FETCH_HEAD').decode().strip()
if tip!=S: raise RuntimeError('Remote report tip mismatch: '+tip+' versus '+S)
metadata=remote('show','-s','--format=%H %T %P',S).decode().split()
paths=remote('ls-tree','-r','--name-only',S,R).decode().splitlines()
outputs=[]
for p in paths:
    r=remote('show',S+':'+p)
    local=run('git','show',S+':'+p)
    oid=hashlib.sha1(('blob '+str(len(r))+'\0').encode()+r).hexdigest()
    outputs.append(dict(commit=S,path=p,git_blob=oid,sha256=hashlib.sha256(r).hexdigest(),bytes=len(r),remote_equals_committed_local=r==local))
    if r!=local: raise RuntimeError('Remote file bytes mismatch: '+p)
old_changes=run('git','diff','--name-status','fa5e1d876c9082797d6eb71f1590f3d8d9a19b0a',S).decode().splitlines()
if not all(line.startswith('A\t'+R+'/') for line in old_changes): raise RuntimeError('Report commit changes an old or unapproved path')
result=dict(stage='INDEPENDENT_REPORT_REMOTE_READBACK_ONLY',repository='y805939188/pokemon-essentials-clean-room',report_branch=branch,report_commit=S,report_tree=metadata[1],report_parents=metadata[2:],source_remote_url=repo,remote_tip=tip,independent_object_store=str(bare),local_object_alternates_used=False,readback_method='fresh remote fetch depth1/filter blob:none then remote Git read of every report output; byte comparison and independently recomputed SHA256/Git blob',outputs=outputs,output_count=len(outputs),all_outputs_match=True,all_report_changes_new_only=old_changes,reference_or_project_program_execution=False,static_cases_executed=False,gate_signed='REPORT_PUBLICATION_ONLY_NO_CANDIDATE_ACCEPTANCE_ACTUAL_OR_FINAL')
pathlib.Path(OUT).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(report_commit=S,report_tree=metadata[1],output_count=len(outputs),all_outputs_match=True,only_new_report_paths=True),ensure_ascii=False))
