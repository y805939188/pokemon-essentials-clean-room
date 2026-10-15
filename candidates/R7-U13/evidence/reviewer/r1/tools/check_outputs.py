"""Check review evidence consistency and exact output scope; no behavior execution."""
import json
from pathlib import Path
import subprocess

root=Path(__file__).resolve().parents[1]
repo=Path('/workspace/r7-u13-reviewer-checkout')
prefix='candidates/R7-U13/evidence/reviewer/r1/'
per=json.loads((root/'per-id.json').read_bytes())
receipt=json.loads((root/'review-input-receipt.json').read_bytes())
record=per['records'][0]
assert record['verdict']=='PASS_SCOPED_CANDIDATE'
assert len(record['vectors'])==15 and len(record['acceptance_checks'])==7
assert all(x['behavior_result']=='NOT_EXECUTED' and x['documentary_review']=='PASS' for x in record['vectors'])
assert receipt['candidate_files_received']==len(receipt['candidate_files'])==24
assert sum(x['bytes'] for x in receipt['candidate_files'])==receipt['candidate_bytes_received']==862370
assert per['candidate_commit']==receipt['candidate_commit']=='5635c73ea14adc278961da0e3917c2d00d580a25'
assert per['candidate_tree']==receipt['candidate_tree']=='e2c261a77a7268a5eb07e7e364ac257d9fed3e31'
assert all(x=='UNVERIFIED' for x in per['effective_configuration'].values())
assert all(per[k] is False for k in ['integrated_PASS','ACCEPTED','CLOSED'])
assert all(x['status'] in ['OPEN','UNCHANGED_NOT_REATTESTED'] for x in record['unmet_dependencies'])
for path in root.rglob('*.json'): json.loads(path.read_bytes())
for path in root.rglob('*.jsonl'):
    for line in path.read_text().splitlines(): json.loads(line)
changed=subprocess.check_output(['git','diff','--name-only','e646432c644dec04d306842cc5a559a29c718fbc'],cwd=repo).decode().splitlines()
untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=repo).decode().splitlines()
assert all(x.startswith(prefix) for x in changed+untracked),changed+untracked
assert subprocess.check_output(['git','branch','--show-current'],cwd=repo).decode().strip()=='codex/r7-u13-reviewer-20261015-r1'
assert not any('__pycache__' in x for x in changed+untracked)
print(json.dumps(dict(status='OUTPUT_CONSISTENCY_AND_SCOPE_PASS',required_records=1,vectors=15,all_behavior_NOT_EXECUTED=True,only_reviewer_r1=True,formal_or_author_mirrors_changed=False)))
