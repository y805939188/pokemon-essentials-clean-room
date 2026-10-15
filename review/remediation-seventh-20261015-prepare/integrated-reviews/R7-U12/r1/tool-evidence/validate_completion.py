"""Validate the completed evidence package without executing domain behavior."""
from pathlib import Path
import hashlib
import json
import subprocess

repo = Path('/workspace/r7-ir-R7-U12/checkout')
root = Path(__file__).resolve().parent.parent
prefix = root.relative_to(repo).as_posix()+'/'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
old = '38ea9afb84395d7c20d3beed322281dd50a688e4'
def git(*args):
    return subprocess.check_output(['git','-C',str(repo),*args])

assert git('branch','--show-current').decode().strip() == 'codex/r7-ir-u12-20261015-r1'
subprocess.run(['git','-C',str(repo),'merge-base','--is-ancestor',B,'HEAD'],check=True)
subprocess.run(['git','-C',str(repo),'merge-base','--is-ancestor',old,'HEAD'],check=True)
changed = git('diff','--name-only',B).decode().splitlines()
untracked = git('ls-files','--others','--exclude-standard').decode().splitlines()
assert all(x.startswith(prefix) for x in changed+untracked)
assert not any(x.is_symlink() for x in root.rglob('*'))
assert not any('__pycache__' in x.parts for x in root.rglob('*'))
for path in root.rglob('*.json'):
    json.loads(path.read_bytes())
rows = json.loads((root/'per-id.json').read_text())['records']
assert [(x['record_id'],x['verdict']) for x in rows] == [
    ('GR7-M19-001','PASS_SCOPED_ACTUAL_INTEGRATION'),
    ('GR7-H08-001','PASS_SCOPED_ACTUAL_INTEGRATION')]
for row in rows:
    assert row['unmet_review_gates'] == []
    assert row['unmet_independence_gate'] == []
    assert not row['ACCEPTED'] and not row['CLOSED']
    assert all(v['behavior_execution']=='NOT_EXECUTED' for v in row['vectors'])
assert [len(x['vectors']) for x in rows] == [8,16]
coverage = json.loads((root/'tool-evidence/content-review-coverage.json').read_text())
assert coverage['complete_actual_full_text_semantic_review'] is True
assert coverage['missing'] == []
shared = json.loads((root/'tool-evidence/shared-contribution-receipt.json').read_text())
assert len(shared['checks']) == 8
assert all(x['semantic_compatibility'].startswith('COMPATIBLE_WITH_U12') for x in shared['checks'])
for name in ['report.md','per-id.json','review-input-receipt.json',
             'tool-evidence/content-review-coverage.json',
             'tool-evidence/shared-contribution-receipt.json']:
    assert (root/'tool-evidence/history'/old/name).read_bytes() == git('show',old+':'+prefix+name)
assert json.loads((root/'tool-evidence/history'/old/'per-id.json').read_text())['records'][0]['verdict']=='WAIT'
subprocess.run(['git','-C',str(repo),'diff','--check',old,'--',prefix],check=True)
print(json.dumps(dict(package_scope_only=True, complete_review_records=2,
    vectors=[8,16], all_vectors='NOT_EXECUTED', shared_compatibility_records=8,
    historical_WAIT_exactly_preserved=True, remaining_reviewer_gates=0,
    root_acceptance_or_closure_granted=False,
    qualification='Packaging consistency checks only; static content judgment is separately stated.')))
