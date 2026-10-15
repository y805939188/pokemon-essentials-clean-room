"""Bind shared candidate approvals to journal slices; no peer semantic verdict."""
import hashlib
import json
import os
import re
import subprocess
import datetime
from pathlib import Path

ROOT = Path('/workspace/r7-ir-R7-U11')
INP = ROOT / 'actual-input'
OUT = Path(__file__).resolve().parent.parent
def read(p): return json.loads(p.read_bytes())
def git(*args): return subprocess.check_output(['git', *args])
def identity(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(b)}\0'.encode() + b).hexdigest()}
journal = read(INP / 'integration/applied-clauses.json')
plan = read(ROOT / 'actual-plans/R7-U11.json')
rows = []
def dicts(v):
    if isinstance(v, dict):
        yield v
        for child in v.values(): yield from dicts(child)
    elif isinstance(v, list):
        for child in v: yield from dicts(child)
for rule in plan['shared_preservation_checks']:
    batch = rule['other_batch']
    source = next(x for x in journal['source_bindings'] if x['id'] == batch)
    assert source['candidate_commit'] == rule['candidate_commit']
    assert source['candidate_review_commit'] == rule['candidate_review_commit']
    eligibility = read(INP / 'shared-root-reception' / batch / 'eligibility.json')
    assert eligibility['root_eligibility'] == 'PASS_SCOPED_CANDIDATE'
    assert eligibility['eligible_for_next_gate'] is True
    assert eligibility['task']['result_commit'] == source['candidate_review_commit']
    assert eligibility['task']['reviewer_task_id'] == source['reviewer_context']
    assert git('rev-parse', source['candidate_commit']+'^{tree}').decode().strip() == source['candidate_tree']
    assert git('rev-parse', source['candidate_review_commit']+'^{tree}').decode().strip() == source['candidate_review_tree']
    per_id = read(INP / 'shared-candidate-review' / batch / 'per-id.json')
    receipt = read(INP / 'shared-candidate-review' / batch / 'review-input-receipt.json')
    for rec in per_id['records']:
        assert rec.get('verdict', rec.get('conclusion')) == 'PASS_SCOPED_CANDIDATE'
        assert rec.get('candidate_commit', per_id.get('candidate_commit')) == source['candidate_commit']
    candidate_path = 'candidates/' + batch + '/' + rule['path']
    candidate = (INP / 'shared-candidate' / batch / rule['path']).read_bytes()
    assert candidate == git('show', source['candidate_commit'] + ':' + candidate_path)
    ident = identity(candidate)
    declarations = [x for x in dicts(receipt) if x.get('path', x.get('candidate_path')) == candidate_path and 'sha256' in x]
    assert declarations, (batch, candidate_path, 'missing reviewer input identity')
    for declaration in declarations:
        assert declaration['sha256'] == ident['sha256']
        assert declaration['bytes'] == ident['bytes']
        assert declaration.get('git_blob', declaration.get('git_blob_content_id')) == ident['git_blob']
    file_row = next(x for x in journal['files'] if x['path'] == rule['path'])
    hunks = [x for x in file_row['hunks'] if x['batch_id'] == batch]
    assert hunks
    for h in hunks:
        a, b = h['candidate_line_indices_half_open']
        assert b''.join(candidate.splitlines(keepends=True)[a:b]) == h['added_text'].encode()
    rows.append({**rule, 'candidate_identity': ident,
                 'candidate_review_tree': source['candidate_review_tree'],
                 'reviewer_context': source['reviewer_context'],
                 'root_eligibility': eligibility['root_eligibility'],
                 'reviewer_input_identity_matches': True,
                 'actual_hunks': [{k: h[k] for k in ('batch_id','base_line_indices_half_open','actual_final_line_indices_half_open','added_identity')} for h in hunks],
                 'receiver': 'R7-I sole integrator',
                 'this_review': 'Exact shared contribution preserved and compatible with U11 scope; no new peer semantic PASS'})
public = read(INP / 'integration/public-reception.json')
assert public['source_bindings'] == journal['source_bindings']
assert public['three_procedural_waits'] == ['R7-U03', 'R7-U07', 'R7-U10']
assert public['ACCEPTED_items'] == 3 and public['CLOSED_items'] == 0
assert public['denominators'] == {'required_items':27, 'batches':13}
dispatch = git('show', 'c64774c60d91e522cb515ef71e3e9d4ea6b4712c:review/remediation-seventh-20261015-prepare/integration/wave2/v1/dispatch/R7-U11-R7IR.md').decode()
excluded = sorted(set(re.findall(r'01a[0-9a-f]{5}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', dispatch)))
thread = os.environ.get('CODEX_THREAD_ID')
assert thread and thread not in excluded
context = {'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'thread_id':thread, 'session_id':os.environ.get('CODEX_SESSION_ID','NOT_EXPOSED'),
           'source_thread_id':'01a13f49-a154-7054-9b04-ce31f924d01c',
           'instruction_context':'/root', 'excluded_visible_ids':excluded,
           'different_from_all_excluded_visible_ids':True, 'AI_auxiliary_tasks_created':0,
           'opaque_platform_task_context_id':'NOT_EXPOSED_UNVERIFIED',
           'effective_configuration':dict.fromkeys(['model','effort','tier','speed'],'UNVERIFIED'),
           'qualification':'Thread/session read from selected execution environment; tool PID is not model identity or configuration proof'}
(OUT / 'context-observation.json').write_text(json.dumps(context,ensure_ascii=False,indent=2)+'\n')
(OUT / 'shared-approval-audit.json').write_text(json.dumps({
    'rows':rows, 'same_boundary_insertions':journal['same_boundary_insertions'],
    'public_phase_counts':{k:public[k] for k in ('candidate_PASS_items','actual_integration_applied_items','actual_independent_PASS_items','ACCEPTED_items','CLOSED_items','denominators')},
    'root_adjustments':journal['root_administrative_reception_adjustments'],
    'qualification':'TOOL_VALIDATION plus separately reported finite compatibility assessment; no other-ID semantic reapproval'
},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'shared_approval_pairs':len(rows),'visible_thread':thread,'excluded_visible_ids':len(excluded),'all_matches':True}))
