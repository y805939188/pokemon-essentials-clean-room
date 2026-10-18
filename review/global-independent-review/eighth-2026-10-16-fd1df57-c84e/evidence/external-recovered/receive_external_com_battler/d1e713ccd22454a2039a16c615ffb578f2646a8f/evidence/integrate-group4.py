"""Integrate actually read group4 finite contributions; no source/game execution.

Semantic basis: all24 qualified records and controls, both complete eight-section
counters,37 exact ledger qualification groups, ten envelopes, four prior reports
and all group limits were literally read before invoking this integrity writer.
Primary810/160 are never granted credit by this script.
"""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

TASK=Path(__file__).resolve().parent.parent
ROOT=TASK.parent.parent
REPO=ROOT.parents[2]
BASE='8e87f63a01ae7d20717150d0859ae47fde2c0e7f'
FIXED='9e210cc9d118a54a01612a469f1f869db75a8aff'
GROUP='01a14490-29b6-7509-9531-dc647c10f001'
CONTRACT='02c8206651676effe40ff9a33dbb70998b79c1b1'
IDS=['R01','R02','R03','H01']
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads(p.read_text())
def write(p,x):
    assert p.is_relative_to(TASK)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def git(*a):return subprocess.check_output(['git','-C',str(REPO),*a])
assert git('rev-parse','HEAD').decode().strip()==BASE
files=[]
for row in git('diff','--name-status',CONTRACT,FIXED).decode().splitlines():
    status,path=row.split('\t')
    assert status=='A' and any(path.startswith(str((TASK/'splits'/s/'result').relative_to(REPO))+'/') for s in IDS)
    raw=git('show',FIXED+':'+path);assert (REPO/path).read_bytes()==raw
    mode,kind,blob=git('ls-tree',FIXED,path).decode().split('\t')[0].split()
    assert mode=='100644' and kind=='blob'
    files.append({'path':path,'mode':mode,'blob':blob,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
assert len(files)==48
SOURCE=TASK/'inputs/target-5cf9503a'
forward=read(SOURCE/'forward-mapping.json')
original_facts={x['id']:x for x in forward['consumer_facts']}
facts={};refs={}
for s in IDS:
    d=read(TASK/'splits'/s/'result/reception-ledger.json')
    request=read(TASK/'splits'/s/'readset.json')
    assert set(x['id'] for x in d['records'])==set(request['consumer_primary_ids'])
    for n,x in enumerate(d['records']):
        assert x['original_complete_object']==original_facts[x['id']]
        assert x['id'] not in facts;facts[x['id']]=x
        f=next(f for f in files if f['path']==str((TASK/'splits'/s/'result/reception-ledger.json').relative_to(REPO)))
        refs[x['id']]={'commit':FIXED,'path':f['path'],'blob':f['blob'],'sha256':f['sha256'],'json_pointer':f'/records/{n}'}
assert len(facts)==24
shared=TASK/'splits/H01/result/evidence'
assert read(shared/'mandatory-exact-inputs.json')==read(ROOT/'adjudication/root-battler-eight-facts-exact-inputs.v1.json')
assert read(shared/'mandatory-eight-facts-reception.json')==read(ROOT/'adjudication/root-battler-eight-consumer-facts-reception.v1.json')
for p in (TASK/'splits/H01/result/recovered').iterdir():assert p.read_bytes()==(SOURCE/p.name).read_bytes()
counter_hashes=['d3ecbfde37326955fe37e431ebf8ce84d9598fb9eadbb5850049a93c36a05a62',
                '4665d22e08e734745090e45548c10cdb4188c658a53c5cd6648c7dfb9dcd468c']
for name,sha in zip(['ecb-001-complete-counter.json','ecb-002-complete-counter.json'],counter_hashes):
    assert hashlib.sha256((shared/name).read_bytes()).hexdigest()==sha
    assert len(read(shared/name)['sections'])==8

metadata=read(shared/'metadata-audit.json')
assert metadata['original_184_rows']==read(SOURCE/'reading-ledger.json')['files']
identity={x['evidence_id']:x for x in read(SOURCE/'identities.json')['files']}
rows={x['evidence_id']:x for x in metadata['original_184_rows']}
count=0
for group in metadata['lossless_semantic_groups']:
    for eid in group['ids']:
        x=rows[eid]
        assert group['fields']=={k:v for k,v in x.items() if k not in ['evidence_id','path','commit','read_ranges','unread_ranges']}
        count+=1
assert count==184 and len(metadata['lossless_semantic_groups'])==37
for p in metadata['line_partitions']:
    x=rows[p['id']];a=[n for lo,hi in x['read_ranges'] for n in range(lo,hi+1)]
    b=[n for lo,hi in x['unread_ranges'] for n in range(lo,hi+1)]
    assert sorted(a+b)==list(range(1,p['lines']+1)) and len(a+b)==len(set(a+b))
assert len(metadata['legacy_aliases'])==88
for a,b in zip(metadata['legacy_aliases'],forward['legacy_fact_id_crosswalk']):
    assert a['id']==b['id'] and a['actual']==a['expected']==b['replacement_compounds']
assert len(metadata['envelopes'])==10
for a,b in zip(metadata['envelopes'],forward['load_envelopes']):
    assert a['original']==b and a['match']
    i=identity[a['id']]
    raw=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',i['commit']+':'+i['path']]).decode().splitlines()
    assert all(raw[x['line']-1]==x['text'] for x in a['actual_non_unit_lines'])
bindings=read(shared/'input-bindings.json')
for x in bindings['source_fetch_bindings']:
    cwd='/workspace/pokemon-essentials' if x['commit']=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' else str(REPO)
    raw=subprocess.check_output(['git','-C',cwd,'show',x['commit']+':'+x['path']])
    assert len(raw)==x['bytes'] and hashlib.sha256(raw).hexdigest()==x['sha256']
    assert hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()==x['observed_blob']

binding={'source_commit':FIXED,'source_workspace_tree':git('rev-parse',FIXED+'^{tree}').decode().strip(),
 'actual_group_context_from_parent_dispatch':GROUP,
 'author_context':'01a143b2-64d2-72d2-ae62-0058869a3010','files':files,
 'publication_observation':'Group4 used GitHub Git Data API and full immutable-object API readback; its own isolated bare NOT_EXECUTED_ENVIRONMENT_FAILED. Parent imported exact fixed objects and performs its own cumulative bare readback; no retrospective claim that group4 ran shell or bare.',
 'opaque_self_echo':'UNVERIFIED; actual route binding is parent dispatch, not role name/source_thread',
 'new_contexts_or_review_layers_created_here':0}
ledger=read(TASK/'reception-ledger.json')
received={x['id'] for x in ledger['source_child_statuses'] if x['status']!='OPEN'}
join_rows=[]
for x in ledger['facts']:
    fact=facts[x['id']]
    producers=[c for c in forward['compounds'] if x['id'] in c['necessary_consumers']]
    missing=[c['id'] for c in producers if any(z['id'] not in received for z in c['children'])]
    assert missing
    x['finite_definition_reception']={
       'status':'COMPLETE_FINITE_DEFINITION_COMPARISON_RECEIVED',
       'actual_complete_meaning':fact['actual_complete_meaning'],'premises':fact['premises'],
       'finite_control':fact['finite_control'],'normal_cancel_failure_partial_commit':fact['normal_cancel_failure_partial_commit'],
       'strongest_no_required':fact['strongest_no_required'],'source_definitions':fact['source_definitions_and_necessary_producers'],
       'current_formal':fact['formal_counterparts'],'source_reader':GROUP,'contribution':refs[x['id']],
       'execution':'NOT_EXECUTED'}
    x['source_support']='COMPLETE_QUALIFIED_FINITE_DEFINITION_COMPARISON_FROM_ACTUAL_GROUP4'
    x['final_consumer_join']='OPEN_EXACT_MISSING_PRODUCER_CONTRIBUTIONS'
    x['remaining_producer_compound_ids']=missing
    join_rows.append({'id':x['id'],'definition':refs[x['id']],
       'all_producer_compound_ids':[c['id'] for c in producers],
       'received_producer_compound_ids':[c['id'] for c in producers if c['id'] not in missing],
       'missing_producer_compound_ids':missing,'status':'FINITE_RECEIVER_COMPLETE_CUMULATIVE_PRODUCER_JOIN_OPEN'})
ledger['finite_definition_comparisons_received']=24
ledger['received_groups']['group4']=binding
ledger['metadata_reception']={'original_ledger_rows':184,'complete_qualification_groups':37,'legacy_aliases':88,'envelopes':10,
 'contribution_commit':FIXED,'source_credit':'Identity/range/qualification reception only; does not transfer old SOURCE_FULL or count810/160.'}
ledger['complete_counter_packages_received']=2
ledger['status']='INCOMPLETE_GROUP3_GROUP4_RECEIVED_WAIT_GROUP1_GROUP2'
write(TASK/'reception-ledger.json',ledger)

interfaces=read(TASK/'interfaces.json')
interfaces['cumulative_finite_fact_joins']=join_rows
for edge in interfaces['cumulative_group3_edges']:
    edge['actual_group4_receiver_bindings']={rx:refs[rx] for rx in edge['necessary_context_ids']}
    edge['status']='GROUP3_PRODUCER_AND_GROUP4_RECEIVER_EDGES_JOINED_OTHER_PRODUCERS_OPEN'
interfaces['cross_group_pending']['RX-CORE-ENTRY_evidence_binding']={
 'status':'RESOLVED_BY_ACTUAL_R01_FINITE_CONTRIBUTION',
 'definition':['E039',316,423],'contribution':refs['RX-CORE-ENTRY'],
 'reader':GROUP,'claim':'Entry hazard/ability/item order and per-member item-before-ability firsttrue stop received; no allCORE/global interface closure.'}
interfaces['cross_group_pending']['full_consumer_primary_facts']='All24 finite definition comparisons received. Exact missing producer compound IDs per fact remain in cumulative_finite_fact_joins; no final full interface closed.'
interfaces['status']='GROUP3_GROUP4_BOUNDED_EDGES_JOINED_FULL_INTERFACES_OPEN'
write(TASK/'interfaces.json',interfaces)

reading=read(TASK/'reading-ledger.json')
reading['cumulative_group4_reception']={
 'binding':binding,'actual_business_objects_read':{'qualified_complete_fact_records':24,'complete_eight_section_counters':2,
 'ledger_qualification_groups':37,'envelopes':10,'prior_provider_full_reports':4},
 'exact_aliases_reused':'Eight H01 actual_complete_meaning lists equal the mandatory already-read complete meaning lists; original24 objects equal fixed target. No semantic values suppressed as identity fields.',
 'metadata_boundary':'184 rows/88 map sets are exact identity and range indexes; all37 remaining semantic/qualification field groups literally read. Old FULL remains old reader; no new810/160 credit.',
 'repairs':['Initial report output omitted R03 middle; its complete five records then read.','Combined prior-provider output omitted E181 tail/E182 prefix; repaired complete E181 tail and E182 whole.','Combined span output truncated only repeated locator fields; repaired all tuples compact and verified they exactly match source/formal lists in already-read records.'],
 'business_execution':'NOT_EXECUTED'}
write(TASK/'reading-ledger.json',reading)
counters=read(TASK/'proposal-counters.json')
counters['receipt_read']='Both root bounded receipts and both complete eight-section original counter packages fully received. Original source sidecars and whole global historical negative proof not inherited.'
counters['final_state']='BOUNDED_COUNTERS_FULLY_RECEIVED_PRESERVE_NO_REQUIRED_GLOBAL_HISTORY_QUALIFIED'
for item in counters['independent_assessment']:
    item['open']='完整八节反证现已实读接收；原反证所有源sidecar/全域FULL不转移。全局canonical/optional等价与重开资格未作普遍声称，不阻塞现有有限NO_REQUIRED且不新建ID。'
counters['complete_original_counter_reception']={
 'status':'BOTH_COMPLETE_EIGHT_SECTION_ORIGINALS_RECEIVED',
 'evidence_commit':FIXED,'evidence_paths':['splits/H01/result/evidence/ecb-001-complete-counter.json','splits/H01/result/evidence/ecb-002-complete-counter.json'],
 'sha256':counter_hashes,'reader':'current parent receiver literal full section reading; original counter source reader remains original nonauthor',
 'classification':'PRESERVE_BOTH_EXISTING_NO_REQUIRED_BOUNDED_SCOPE','new_required':0,'new_optional':0,'new_votes':0,
 'qualification':'Full counter meanings/controls/prefixes received, not original counter entire source sidecars or whole global historical absence. No newcanonical or reopening of R7_27.'}
write(TASK/'proposal-counters.json',counters)
progress=read(TASK/'progress.json');progress['utc']=NOW
progress['status']='INCOMPLETE_GROUP3_GROUP4_RECEIVED_WAIT_GROUP1_GROUP2'
progress['completed']['finite_source_comparisons']=24
progress['completed']['complete_original_counter_packages_received']=2
progress['completed']['ledger_qualification_groups_received']=37
progress['completed']['original_ledger_rows_audited']=184
progress['completed']['legacy_aliases_received']=88
progress['completed']['envelopes_received']=10
progress['remaining']['complete_original_counter_packages']=0
progress['remaining']['consumer_definition_comparisons']=0
progress['remaining']['cumulative_consumer_joins']=24
progress['remaining']['RX-CORE-ENTRY_E039_binding']=0
progress['actual_group4_delivery']=binding
progress['next']='Receive actual group1/group2 outputs, join exact missing producer IDs with already-complete finite receiver records, then reconcile all formal/foreign/history boundaries and root final.'
write(TASK/'progress.json',progress)
publication=read(TASK/'publication.json')
publication['current_cumulative_reception']='GROUP3_GROUP4_RECEIVED_PARENT_TASK_INCOMPLETE'
publication['group4_source_commit']=FIXED;publication['group4_source_file_count']=48
publication['group4_transport_qualification']=binding['publication_observation']
publication['completed_scope']='27/183/36 group3 contributions plus all24 finite group4 definitions, both full counters,184 ledger/37 qualification groups,88 map sets and10 envelopes received. Source read credit stays actual readers.'
publication['remaining_scope']='627 source children/124 other reverse primary facets and complete cumulative interfaces await group1/group2; existing explicit foreign/history scope remains qualified.'
write(TASK/'publication.json',publication)
validation=read(TASK/'validation.json')
validation['cumulative_group4_validation']={'utc':NOW,'source_commit':FIXED,'fixed_import_files':48,
 'fact_objects_exact':24,'counter_exact_hashes':2,'original_ledger_rows_exact':184,
 'qualification_groups_losslessly_equal':37,'legacy_sets_equal':88,'envelopes_equal':10,
 'source_identity_bindings':len(bindings['source_fetch_bindings']),
 'result':'PASS_IDENTITY_STRUCTURE_ONLY','semantic_credit_from_checks':0,'task_status':'INCOMPLETE'}
write(TASK/'validation.json',validation)
print(json.dumps({'received_finite_definitions':24,'complete_counter_packages':2,'metadata_qualification_groups':37,
 'E039_binding':'RESOLVED_BY_R01','source_children_received':183,'reverse_primary_facets_received':36,
 'remaining_source_children':627,'remaining_reverse_primary_facets':124,'full_central_interfaces_complete':0,
 'new_required':0,'new_optional':0,'task_status':'INCOMPLETE'}))
