"""Seed immutable pre-R6 Git objects for differential remote transport checking.
This scratch repository is never a replacement project input or checkout.
"""
import datetime, json, os, pathlib, re, subprocess
root=pathlib.Path(__file__).resolve().parents[1];base=root.parents[2]
def git(*a):return subprocess.check_output(['git','-C',str(base),*a],text=True).strip()
assert git('rev-parse','HEAD')=='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
assert not git('diff','--cached','--name-only')
src=pathlib.Path(git('rev-parse','--git-path','objects'))
if not src.is_absolute():src=base/src
dst=root/'temporary/remote-readback.git';dst.parent.mkdir(exist_ok=True)
assert not dst.exists(),'Do not overwrite a previous transport cache'
subprocess.run(['git','init','--bare',str(dst)],check=True,capture_output=True)
count=total=0
for p in src.rglob('*'):
    if not p.is_file():continue
    rel=p.relative_to(src)
    if not ((len(rel.parts)==2 and re.fullmatch('[0-9a-f]{2}',rel.parts[0]) and re.fullmatch('[0-9a-f]{38}',rel.parts[1])) or (rel.parts[0]=='pack' and p.suffix in {'.pack','.idx','.rev'})):continue
    q=dst/'objects'/rel;q.parent.mkdir(parents=True,exist_ok=True)
    os.link(p,q);count+=1;total+=p.stat().st_size
subprocess.run(['git','--git-dir='+str(dst),'update-ref','refs/heads/seed-input-main','8ea169fbd0f33f378b5d732fd6bea59e854e04a6'],check=True)
subprocess.run(['git','--git-dir='+str(dst),'cat-file','-e','8ea169fbd0f33f378b5d732fd6bea59e854e04a6^{tree}'],check=True)
o={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scratch_git_dir':str(dst),'pre_report_HEAD':git('rev-parse','HEAD'),'source_object_store':str(src),'linked_immutable_files':count,'linked_bytes':total,'new_R6_commits_present_at_seed':False,'purpose':'Reuse only pre-existing unchanged input/old-object transfer cache; fetch report branch later into this separate object database and fully hash each remote report blob. Never reset/switch/replace actual project.'}
(root/'control/remote-cache-seed.json').write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n');print(json.dumps(o))
