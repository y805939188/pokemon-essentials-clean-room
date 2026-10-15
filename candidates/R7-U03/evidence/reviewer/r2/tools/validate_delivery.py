"""Verify reviewer evidence consistency and the sole authorized write set."""
import hashlib
import json
from pathlib import Path
import subprocess

root=Path(__file__).resolve().parents[1]
repo=root.parents[4]
prefix='candidates/R7-U03/evidence/reviewer/r2/'
for p in root.rglob('*.json'):json.loads(p.read_bytes())
receipt=json.loads((root/'review-input-receipt.json').read_bytes())
per=json.loads((root/'per-id.json').read_bytes())
assert len(receipt['candidate_files'])==84
assert sum(r['bytes'] for r in receipt['candidate_files'])==774948
assert {r['id'] for r in per['records']}=={'GR7-M05-001','GR7-M06-001'}
assert all(r['verdict']=='PASS_SCOPED_CANDIDATE' for r in per['records'])
assert not any(per[k] for k in ['integrated_PASS','ACCEPTED','CLOSED'])
assert receipt['reviewer']['child_AI_tasks_created_total']==0
assert receipt['prior_r1']['R7_I_final_process_qualification']=='WAIT_INPUT_OR_INDEPENDENCE'
assert receipt['configuration']['effective']=={k:'UNVERIFIED' for k in ['model','reasoning_effort','service_tier','speed']}
manifest=root/'artifact-manifest.json'
if manifest.exists():
    m=json.loads(manifest.read_bytes())
    for r in m['files']:
        d=(repo/r['path']).read_bytes()
        assert len(d)==r['bytes'] and hashlib.sha256(d).hexdigest()==r['sha256'],r['path']
        assert hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()==r['git_blob'],r['path']
status=subprocess.check_output(['git','-C',str(repo),'status','--porcelain','--untracked-files=all']).decode().splitlines()
assert all(line[3:].startswith(prefix) for line in status),status
assert subprocess.check_output(['git','-C',str(repo),'branch','--show-current']).decode().strip()=='codex/r7-u03-reviewer-20261015-r2'
print(json.dumps(dict(json_parsed=True,verdicts_consistent=True,current_changes_only_authorized_r2=True,configuration_and_old_WAIT_preserved=True,behavior_executions=0)))
