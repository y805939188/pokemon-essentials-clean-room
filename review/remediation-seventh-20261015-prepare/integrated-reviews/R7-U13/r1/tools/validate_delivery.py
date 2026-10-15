"""Validate review evidence and authorized write scope, never behavioral tests."""
from pathlib import Path
import json,subprocess,datetime,os,sys
from run_logged import identity
W=Path('/workspace/r7-ir-R7-U13');E=Path(__file__).resolve().parent.parent;T=E/'tools';repo=W/'checkout';prefix=str(E.relative_to(repo))+'/'
def git(*a):return subprocess.check_output(['git','-C',str(repo),*a])
def js(p):return json.loads(p.read_bytes())
assert git('branch','--show-current').decode().strip()=='codex/r7-ir-u13-20261015-r1'
assert git('merge-base','HEAD','e646432c644dec04d306842cc5a559a29c718fbc').decode().strip()=='e646432c644dec04d306842cc5a559a29c718fbc'
changed=git('status','--porcelain=v1','--untracked-files=all','-z').decode().split('\0')
paths=[x[3:] for x in changed if x];assert all(p.startswith(prefix) for p in paths),paths
tracked_changed=git('diff','--name-only','e646432c644dec04d306842cc5a559a29c718fbc','HEAD').decode().splitlines();assert all(p.startswith(prefix) for p in tracked_changed)
assert git('rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
json_files=0;jsonl_rows=0;files=[]
for p in sorted(E.rglob('*')):
    if not p.is_file():continue
    assert not p.is_symlink() and '__pycache__' not in p.parts,p
    if p.suffix=='.json':json.loads(p.read_bytes());json_files+=1
    if p.suffix=='.jsonl':
        for l in p.read_text().splitlines():json.loads(l);jsonl_rows+=1
    files.append(p)
per=js(E/'per-id.json');records=per['records'];assert len(records)==1 and records[0]['id']=='GR7-D07-001'
rec=records[0];assert rec['verdict']=='PASS_SCOPED_ACTUAL_INTEGRATION' and not per['ACCEPTED'] and not per['CLOSED']
assert len(rec['vectors'])==15 and len({v['id'] for v in rec['vectors']})==15
assert all(v['behavior_result']=='NOT_EXECUTED' for v in rec['vectors'])
assert not rec['blocking_content_findings'] and not rec['other_ID_new_semantic_PASS']
receipt=js(E/'review-input-receipt.json');assert len(receipt['mandatory_ten_full_read_coverage'])==10 and all(r['literal_read_full'] for r in receipt['mandatory_ten_full_read_coverage'])
assert git('show','45c80832a41c1b56dcd7e9d93497758cbb7721de:AGENTS.md').decode() in (T/'controls-corrected.stdout').read_text()
for k in ['REFERENCE_OBSERVATION','independent_full_behavior_model','reference_program','reference_Ruby','game_host','Demo','native_media','synthesis','sound','real_save_replay']:assert per['execution'][k]==0
assert all(v=='UNVERIFIED' for v in per['effective_configuration'].values())
summary=js(T/'clause-byte-audit.json')['summary'];assert summary=={'reconstructed_files':24,'hunks':56,'shared_preservation_checks':9,'candidate_slices_checked':56,'root_admin_adjustments':3}
for r in js(T/'evidence-relocations.json')['relocations']:assert identity(Path(r['actual_full_stdout_local_path']).read_bytes())==r['identity']
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'branch':git('branch','--show-current').decode().strip(),'authorized_prefix':prefix,'changed_paths_within_prefix':len(paths),'changed_outside_prefix':[],'formal_tree_on_result_branch_is_B':True,'json_files_valid':json_files,'jsonl_rows_valid':jsonl_rows,'mandated_full_read_documents':10,'per_id_records':1,'vectors':15,'behavior_execution':0,'mechanical_summary':summary,'qualifications':'Evidence/schema/authorization checks only; no behavior or model configuration credit.'}
(T/'delivery-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
