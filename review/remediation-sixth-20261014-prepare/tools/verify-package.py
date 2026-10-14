#!/usr/bin/env python3
"""Verify finite preparation identities and state; never attest semantic PASS."""
import collections
import hashlib
import json
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
repo = root.parents[1]
main = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
final = '76038a81fbb376ab318159e24268bd369cdec2ba'
report = 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=repo)


def read(name):
    return json.loads((root / name).read_text())


def identity(data):
    return {'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


manifest = json.loads(git('cat-file','blob',final + ':' + report + '/cloud-sixth-update-handoff-manifest.json'))
ledger = read('ledger.json')
register = read('task-register.json')
rows = ledger['required']
assert len(rows) == len({x['id'] for x in rows}) == 56
assert collections.Counter(x['severity'] for x in rows) == {'P2':39,'P3':17}
assert {x['id']:x['primary_batch'] for x in rows} == manifest['batch_contracts']['unique_primary_batch']
assert ledger['totals'] == {'candidate_pass':0,'integrated_pass':0,'accepted':0,'closed':0,'open':56}
assert not ledger['formal_remediation_started']
assert all(x['state']=='OPEN_NOT_UPDATED' and x['candidate_state']=='BASELINE_ONLY' and not x['closed'] for x in rows)
assert all(x['candidate_pass'] is None and x['integrated_pass'] is None and x['formal_acceptance'] is None for x in rows)
assert register['actual_author_reviewer_launch_count'] == 0
assert len(register['tasks']) == len({t['logical_id'] for t in register['tasks']}) == 28
for task in register['tasks']:
    assert task['launch_count'] == 0 and task['platform_task_id'] is None and task['pid'] is None
    assert task['requested_model']=='gpt-6.1-sol' and task['requested_tier']==task['requested_speed']=='default'
    assert task['requested_effort'] == ('xhigh' if task['role']=='author' else 'ultra')
    data=(root/task['prompt']).read_bytes()
    assert identity(data) == task['prompt_identity']
    original=git('cat-file','blob',final+':'+task['original_entry']['git_full_path'])
    assert data.endswith(original)
    for key,value in identity(original).items():
        assert task['original_entry'][key]==value
    contract=read('contracts/'+task['batch']+'.json')
    assert contract==next(b for b in manifest['batch_contracts']['batches'] if b['id']==task['batch'])
    assert task['required_ids']==contract['required_ids']
    if task['role']=='author':
        expected=[str(root/'candidates'/task['batch']/'mirror'/p) for p in contract['candidate_formal_paths']]
        expected.append(str(root/'candidates'/task['batch']/'evidence')+'/')
    else:
        expected=[str(root/'reviews'/task['logical_id'])+'/']
    assert task['write_allowlist']==expected
baseline_files=0
for batch in manifest['batch_contracts']['batches']:
    expected={str(root/'candidates'/batch['id']/'mirror'/p) for p in batch['candidate_formal_paths']}
    actual={str(p) for p in (root/'candidates'/batch['id']/'mirror').rglob('*') if p.is_file()}
    assert actual==expected
    for path in batch['candidate_formal_paths']:
        assert (root/'candidates'/batch['id']/'mirror'/path).read_bytes()==git('cat-file','blob',main+':'+path)
        baseline_files+=1
for key,row in read('inputs/evidence/index.json').items():
    assert key in manifest['evidence_binding_index']
    data=(root/row['local_path']).read_bytes()
    assert all(identity(data)[k]==row[k] for k in identity(data))
    assert not row['new_semantic_review']
for name in ['dependency_graph','file_conflict_graph','policy_records','limit_records','optional_records','no_required_revision_records','optional_facets','historical_qualification','execution_phases']:
    assert read('inputs/'+name.replace('_','-')+'.json')==manifest[name]
assert read('verification/reading-coverage.json')['semantic_full_read_of_all_65_records_by_new_authors_or_reviewers'] is False
capability=read('verification/runtime-capability.json')
assert capability['author_reviewer_actual_launch_count']==0 and not capability['model_turn_started']
assert capability['probe']['exit_code']==1 and not (root/'verification/runtime-probe/stdout.jsonl').read_bytes()
assert git('rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='1046fbb657882e84b3dfc6d017943a9edf7782e5'
for path in git('diff','--name-only',main).decode().splitlines():
    assert path.startswith(str(root.relative_to(repo))+'/'), 'Existing protected tracked content changed: '+path
for path in git('ls-files','--others','--exclude-standard').decode().splitlines():
    assert path.startswith(str(root.relative_to(repo))+'/'), 'Unexpected new path outside owned root: '+path
assert not (repo/'build_review.py').exists() and not (repo/'forward-matrix.jsonl').exists()
print(json.dumps({'state':'PREPARATION_IDENTITY_AND_STATE_VERIFIED','required_open':56,'baseline_files':baseline_files,
                  'unique_formal_candidate_paths':54,'entries':28,'source_evidence_files':115,
                  'actual_author_reviewer_launch_count':0,'formal_tree_unchanged':True,'tracked_history_unchanged':True,
                  'semantic_full_read':'PENDING_NEW_ENTRY_READS','new_reference_execution':0,
                  'candidate_PASS':0,'integrated_PASS':0,'accepted':0,'CLOSED':0},ensure_ascii=False))
