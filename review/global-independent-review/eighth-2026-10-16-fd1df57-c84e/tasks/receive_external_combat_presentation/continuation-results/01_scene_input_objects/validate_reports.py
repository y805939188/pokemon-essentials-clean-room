"""Validate report consistency only; not a behavioral test or semantic proof."""
import json
from check_inputs import REPO, TASK, OUT, CONTRACT, git

d=json.loads((TASK/'continuation/01_scene_input_objects/readset.complete.json').read_text())
documents={p.name:json.loads(p.read_text()) for p in OUT.glob('*.json')}
r=documents['reception-ledger.json']
i=documents['interfaces.json']
n=documents['assessment-notes.json']
read=documents['reading-ledger.json']
assert r['contract_commit']==CONTRACT
assert r['denominator']==r['received_facts']==len(r['records'])==166
assert r['source_groups']==d['source_groups']
assert len(n)==32 and sum(map(len,n.values()))==166
assert [x['id'] for x in r['records']]==[x['id'] for x in d['primary_objects']]
for got, original in zip(r['records'],d['primary_objects']):
    assert got['original_complete_object']==original
for g in d['source_groups']:
    xs=[x for x in r['records'] if x['original_complete_object']['group']==g['id']]
    assert [x['current_complete_meaning_and_reason'] for x in xs]==n[g['id']]
assert sum(x['disposition']=='RECEIVED_WITH_MANDATORY_QUALIFICATION' for x in r['records'])==16
assert r['necessary_unread']==i['necessary_unread']==read['necessary_unread']==[]
assert r['new_candidates_pending_parent_adjudication']==i['new_candidates_pending_parent_adjudication']==1
assert len(i['reverse_records'])==59 and len(i['selected_reverse_interfaces'])==2
expected=[(g,s) for g in d['reverse_current_contribution_objects'] for s in g['subassertions']]
for got,(g,s) in zip(i['reverse_records'],expected):
    assert got['original_complete_assertion']==s and got['original_reverse_group']==g
assert [x['original_complete_interface'] for x in i['selected_reverse_interfaces']]==d['selected_reverse_interfaces']
assert len(read['units'])==55
for unit in read['units'][:5]:
    assert unit['read_intervals']==[[1,unit['line_count']]]
    assert unit['whole_file']
assert sum(x['bytes'] for x in read['units'][:5])==80222
assert sum(x['line_count'] for x in read['units'][:5])==2333
assert documents['findings.json']['required_final_count']==0
formal=REPO/'deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md'
assert documents['findings.json']['candidates'][0]['original_complete_clause'] in formal.read_text()
changed=git(REPO,'diff','--name-only',CONTRACT).decode().splitlines()
new=git(REPO,'ls-files','--others','--exclude-standard').decode().splitlines()
prefix=str(OUT.relative_to(REPO))+'/'
assert all(p.startswith(prefix) for p in changed+new),changed+new
assert git(REPO,'branch','--show-current').decode().strip()=='codex/r8-cp-reception-01-20261016'
assert not list(OUT.rglob('__pycache__'))
print(json.dumps(dict(status='PASS_REPORT_CONSISTENCY_ONLY',primary=166,qualified=16,reverse=59,
                      selected_interfaces=2,read_units=55,new_candidate=1,necessary_unread=0,
                      scope_paths=len(set(changed+new)),restored_code_executed=False)))
