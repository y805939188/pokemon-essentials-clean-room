"""Read-only identity/association checks; writes only this authorized packet's metadata."""
from pathlib import Path
import datetime,hashlib,json
HERE=Path(__file__).resolve().parent
RR=HERE.parents[2]
REPO=RR.parents[2]
def read(p):return json.loads(Path(p).read_bytes())
def sha(b):return hashlib.sha256(b).hexdigest()
def at(x,pointer):
    for k in pointer.lstrip('/').split('/'):
        if k:x=x[int(k)] if isinstance(x,list) else x[k]
    return x
began=datetime.datetime.now(datetime.timezone.utc).isoformat()
old=read(HERE.parent/'delivery-manifest.current.json')
for x in old['files']:
    b=(HERE.parent/x['path']).read_bytes()
    assert len(b)==x['bytes'] and sha(b)==x['sha256'],x['path']
assert len(old['files'])==335
for p in HERE.rglob('*.json'):read(p)
for n in ['current-egggroup-handoff.json','current-wp31-handoff.json']:
    q=read(HERE/'inputs'/n);p=RR/q['parent']['path'];b=p.read_bytes()
    assert len(b)==q['parent']['bytes'] and sha(b)==q['parent']['sha256']
    data=json.loads(b)
    for s in q['selections']:assert s['complete_object']==at(data,s['pointer'])
h12=read(RR/'tasks/receive_external_h_early_qualifications/receivers/fanout-v1/early_r1_r4/inputs-recovered-1/decoded-25')
for q in read(HERE/'inputs/r1-complete-domain-qualifications.json')['records']:
    assert q['complete_effective_record']==at(h12,q['pointer'])
r2=read(REPO/'review/remediation-20261003-prepare/finding-acceptance.json')
for p in (HERE/'inputs').glob('r2-GIR-FD82-*.json'):
    q=read(p);assert q['complete_effective_business_object']==r2[q['complete_effective_business_object']['id']]
for q in read(HERE/'inputs/r2-complete-selected-status-qualifications.json')['records']:
    assert q['complete_qualification']==at(h12,q['pointer'])
for q in read(HERE/'inputs/r3-r4-complete-nearby-objects.json')['complete_records']:
    assert q['object']==at(h12,q['pointer'])
values=h12['R5']['original_and_current_percheck_value_dictionary']
def resolve(x):
    if isinstance(x,str) and x in values:return resolve(values[x])
    if isinstance(x,list):return [resolve(a) for a in x]
    if isinstance(x,dict):return {k:resolve(v) for k,v in x.items()}
    return x
native=0;criteria=0
for p in (HERE/'inputs').glob('r5-GR5-M01-*.json'):
    q=read(p);s=at(h12,q['full_scope_pointer']);c=at(h12,q['current_root_pointer'])
    assert q['complete_original_scope_and_effective_override']['original_scope_qualification']==s['original_scope_qualification']
    assert q['complete_original_scope_and_effective_override']['effective_qualification_override']==s['effective_qualification_override']
    assert q['complete_effective_current_record']['current_scope_qualification']==c['current_scope_qualification']
    native+=len(s['original_scope_qualification']['acceptance_criteria']['static'])
    assert len(q['all_criteria_complete_business_fields'])==len(c['schema_units'])
    for got,unit in zip(q['all_criteria_complete_business_fields'],c['schema_units']):
        orig=resolve(unit['original_fields']);cur=resolve(unit['current_fields'])
        assert all(orig[k]==v for k,v in got['original_complete_semantics'].items())
        if 'shared_complete_semantics' in got['current_complete_semantics']:
            assert all(cur[k]==v for k,v in q['shared_current_criterion_qualification'].items())
        else:assert all(cur[k]==v for k,v in got['current_complete_semantics'].items())
        assert resolve(unit['accepted_fields'])==got['accepted_complete_semantics']
        criteria+=1
assert native==25 and criteria==38
for n,field,pointer in [('c2-complete-wurmple-object.json','complete_record','/records/8'),('r6-retained-util11-complete.json','complete_record','/complete_legacy_contribution/10')]:
    q=read(HERE/'inputs'/n);assert q[field]==at(read(REPO/q['binding']['path']),pointer)
q=read(HERE/'inputs/r6-complete-species-consumer-facts.json');parent=read(REPO/q['binding']['path'])
assert q['records']==[parent['contracts'][2],parent['contracts'][54]]
q=read(HERE/'inputs/qualified-r7-two-comparisons.json');parent=read(REPO/q['binding']['path'])
assert q['records']==[parent['records'][32],parent['records'][33]]
for k,v in read(HERE/'source-bindings.json')['bindings'].items():
    b=(REPO/v['path']).read_bytes();assert len(b)==v['bytes'] and sha(b)==v['sha256'],k
comp=read(HERE/'comparison.json');rem=read(HERE/'remaining.json')
assert [x['id'] for x in comp['comparisons']]==['GR8-PBS-EGGGROUP-DOMAIN-001','GR8-CRE-WP31-UNKNOWN-001']
assert len(comp['comparisons'][0]['complete_domain_in_definition_order'])==15
assert not rem['necessary_available_unreceived'] and not rem['unavailable_required_materials']
assert all(x['actually_read_complete_business_object'] for x in read(HERE/'reading-ledger.json')['inputs'])
result={'schema':'creb-history-delivery-identity-validation/v1','began_utc':began,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'PASS_METADATA_IDENTITY_AND_ASSOCIATION_ONLY','original335_files_unchanged':True,'original335_bytes':old['total_bytes'],'original_manifest_sha256':sha((HERE.parent/'delivery-manifest.current.json').read_bytes()),'selected_r5_native_conditions':native,'selected_r5_schema_criteria':criteria,'all22_selected_packets_business_text_read_and_bound':True,'source_FULL_credit':0,'semantic_review_or_behavior_from_script':False,'behavior':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
(HERE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
