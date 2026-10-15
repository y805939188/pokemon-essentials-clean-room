"""Validate evidence packaging and scope, not content acceptance."""
from pathlib import Path
import json
import subprocess

root=Path(__file__).resolve().parent.parent
repo=Path('/workspace/r7-ir-R7-U12/checkout')
prefix='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U12/r1/'
def git(*args):return subprocess.check_output(['git','-C',str(repo),*args]).decode()
assert git('rev-parse','HEAD').strip()=='e646432c644dec04d306842cc5a559a29c718fbc'
assert git('branch','--show-current').strip()=='codex/r7-ir-u12-20261015-r1'
tracked=git('diff','--name-only','HEAD').splitlines()
untracked=git('ls-files','--others','--exclude-standard').splitlines()
assert all(p.startswith(prefix) for p in tracked+untracked)
assert not any(p.is_symlink() for p in root.rglob('*'))
assert not any('__pycache__' in p.parts for p in root.rglob('*'))
for p in root.rglob('*.json'):json.loads(p.read_bytes())
records=json.loads((root/'per-id.json').read_bytes())['records']
assert [(r['record_id'],r['verdict']) for r in records]==[('GR7-M19-001','WAIT'),('GR7-H08-001','WAIT')]
assert all(not r['ACCEPTED'] and not r['CLOSED'] for r in records)
assert all(v['behavior_execution']=='NOT_EXECUTED' for r in records for v in r['vectors'])
assert all(r['unmet_review_gates'] for r in records)
assert not (root/'tool-evidence/inputs/additional').exists()
check=subprocess.run(['git','-C',str(repo),'diff','--no-index','--check','/dev/null',str(root/'report.md')],capture_output=True)
assert check.returncode in (0,1),(check.returncode,check.stdout,check.stderr)
print(json.dumps(dict(scope_only=True,branch='codex/r7-ir-u12-20261015-r1',verdicts=['WAIT','WAIT'],
    files_before_manifest=sum(p.is_file() for p in root.rglob('*')),new_behavior_executions=0,
    semantic_review_complete=False,qualification='Packaging checks only; remaining readable content review gates explicit.')))
