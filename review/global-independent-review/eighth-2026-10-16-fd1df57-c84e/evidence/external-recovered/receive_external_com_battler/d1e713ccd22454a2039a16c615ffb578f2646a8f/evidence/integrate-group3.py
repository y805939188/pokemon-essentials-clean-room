"""Bind actually read group-3 contributions into the existing parent ledgers.

This is a reception/integrity tool, not a source reviewer. Its semantic basis is
the receiver's prior literal reading of all 183 assertions/reasons, all 36 reverse
contributions, all 27 compound qualifications and the required interface evidence.
It never executes the recovered group validator or any source/game code.
"""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

TASK=Path(__file__).resolve().parent.parent
ROOT=TASK.parent.parent
REPO=ROOT.parents[2]
BASE='02c8206651676effe40ff9a33dbb70998b79c1b1'
FIXED='faba225d554f0a4718f8d92bcf21f69d19c0614e'
GROUP_CONTEXT='01a14493-c641-76d5-98fd-8c075a60b028'
IDS=['P07','P08','P09','P10']
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p): return json.loads(p.read_text())
def write(p,x):
    assert p.is_relative_to(TASK)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def git(*args): return subprocess.check_output(['git','-C',str(REPO),*args])
assert git('rev-parse','HEAD').decode().strip()==BASE
files=[]
for row in git('diff','--name-status',BASE,FIXED).decode().splitlines():
    status,path=row.split('\t')
    assert status=='A' and any(path.startswith(str((TASK/'splits'/s/'result').relative_to(REPO))+'/') for s in IDS)
    raw=git('show',FIXED+':'+path)
    assert (REPO/path).read_bytes()==raw
    mode,kind,blob=git('ls-tree',FIXED,path).decode().split('\t')[0].split()
    assert mode=='100644' and kind=='blob'
    files.append({'path':path,'mode':mode,'blob':blob,'bytes':len(raw),
                  'sha256':hashlib.sha256(raw).hexdigest()})
assert len(files)==33
original=read(TASK/'inputs/target-5cf9503a/forward-mapping.json')
original_compounds={x['id']:x for x in original['compounds']}
original_children={x['id']:x for c in original_compounds.values() for x in c['children']}
original_reverse={x['id']:x for g in read(TASK/'inputs/target-5cf9503a/reverse-mapping.json')['clause_groups'] for x in g['subassertions']}
source={}; reverse={}; compounds={}; contribution_files={}; originals_interfaces=read(TASK/'interfaces.json')['four_full_original_interfaces']
for s in IDS:
    result=TASK/'splits'/s/'result'
    d=read(result/'reception-ledger.json'); request=read(TASK/'splits'/s/'readset.json')
    assert [x['original'] for x in d['compounds']]==request['primary_compounds']
    assert {x['id'] for x in d['source_children']}==set(request['primary_child_ids'])
    assert {x['id'] for x in d['assigned_reverse_children']}==set(request['assigned_reverse_child_ids'])
    for n,c in enumerate(d['compounds']):
        assert c['original']==original_compounds[c['id']]
        assert c['id'] not in compounds; compounds[c['id']]=(s,n,c)
    for n,c in enumerate(d['source_children']):
        assert c['original']==original_children[c['id']]
        assert c['id'] not in source; source[c['id']]=(s,n,c)
    for n,c in enumerate(d['assigned_reverse_children']):
        assert c['original']==original_reverse[c['id']]
        assert c['id'] not in reverse; reverse[c['id']]=(s,n,c)
    for c in read(result/'interfaces.json')['interfaces']:
        assert c['original']==next(x for x in originals_interfaces if x['id']==c['original']['id'])
    assert d['new_required']==[] and d['new_optional']==[] and d['unresolved_local_semantic_objects']==[]
    contribution_files[s]=next(x for x in files if x['path']==str((result/'reception-ledger.json').relative_to(REPO)))
assert len(compounds)==27 and len(source)==183 and len(reverse)==36

# Verify parent/slice identities mechanically without rereading primary bodies.
a=read(TASK/'splits/P07/result/evidence/actual-reading-evidence.json')
identity_rows=[]
for x in a['actual_source_and_formal_reading']:
    i=x['identity']
    cwd='/workspace/pokemon-essentials' if i['commit']=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' else str(REPO)
    raw=subprocess.check_output(['git','-C',cwd,'show',i['commit']+':'+i['path']])
    assert hashlib.sha256(raw).hexdigest()==i['sha256'] and len(raw)==i['bytes']
    assert len(raw.splitlines())==i['line_count']
    assert hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()==i['blob']
    identity_rows.append({'id':x['evidence_id'],'path':i['path'],'commit':i['commit'],
      'sha256':i['sha256'],'status':'IDENTITY_ONLY_VERIFIED'})
mandatory=read(ROOT/'adjudication/root-battler-eight-facts-exact-inputs.v1.json')['complete_necessary_units']
for entry,unit in zip(a['mandatory_units'],mandatory):
    assert hashlib.sha256(unit['text'].encode()).hexdigest()==entry['sha256_of_text']
assert len(a['mandatory_units'])==31

binding={'source_commit':FIXED,'source_workspace_tree':git('rev-parse',FIXED+'^{tree}').decode().strip(),
 'actual_group_context_from_parent_dispatch':GROUP_CONTEXT,
 'context_binding_source':'Parent dispatch explicitly reported group3 successful actual start; child self echo remains UNVERIFIED',
 'forbidden_original_author_context':'01a143b2-64d2-72d2-ae62-0058869a3010',
 'no_new_context_or_review_layer_created_here':True,'unchanged_original_files':files}
def pointer(s,n,collection):
    return {'commit':FIXED,'path':contribution_files[s]['path'],
            'blob':contribution_files[s]['blob'],'sha256':contribution_files[s]['sha256'],
            'json_pointer':f'/{collection}/{n}'}

ledger=read(TASK/'reception-ledger.json')
for x in ledger['source_child_statuses']:
    if x['id'] not in source: continue
    s,n,c=source[x['id']]
    x.update(status='RECEIVED_SUPPORTED_UNDER_RETAINED_PREMISES',
      meaning=c['original']['assertion'],qualification=c['original']['premises'],
      receiver_reason=c['receiver_rationale'],contribution=pointer(s,n,'source_children'),
      source_reader=GROUP_CONTEXT,source_not_runtime='NOT_EXECUTED')
foreign_open=[]
for x in ledger['reverse_child_statuses']:
    if x['id'] not in reverse: continue
    s,n,c=reverse[x['id']]
    foreign=c['foreign_facet']
    status='PRIMARY_FACET_RECEIVED_FOREIGN_JOIN_OPEN' if foreign else 'RECEIVED_ASSIGNED_SOURCE_SUPPORT'
    if foreign: foreign_open.append(x['id'])
    x.update(status=status,meaning=c['original']['assertion'],qualification=c['original']['premise'],
      receiver_reason=c['receiver_rationale'],foreign_facet=foreign,
      contribution=pointer(s,n,'assigned_reverse_children'),source_reader=GROUP_CONTEXT,
      source_not_runtime='NOT_EXECUTED')
assert foreign_open==['FC40-TURN.01']
ledger['complete_producer_children_received']=183
ledger['assigned_reverse_primary_facets_received']=36
ledger['complete_selected_formal_children_received']=35
ledger['reverse_count_qualification']='36 complete assigned primary-facet contributions received; FC40-TURN.01 explicitly retains foreign CORE command-producer join. 35 have no explicit foreign facet. No assertion that full formal parents/global interfaces are closed.'
ledger['received_groups']={'group3':binding}
ledger['status']='INCOMPLETE_WAIT_OTHER_GROUP_DELIVERIES'
contexts=read(TASK/'splits/P07/result/evidence/necessary-consumers.json')
context_map={x['original']['id']:x for x in contexts['objects']}
for fact in ledger['facts']:
    if fact['id'] in context_map:
        fact['group3_bounded_necessary_context']={
          'source_commit':FIXED,'source_reader':GROUP_CONTEXT,
          'assessment':context_map[fact['id']]['receiver_assessment'],
          'source_evidence':'splits/P07/result/evidence/actual-reading-evidence.json',
          'full_fact_primary_reception':'AWAIT_ASSIGNED_R01_R02_R03_H01',
          'execution':'NOT_EXECUTED'}
ledger['remaining_source_child_ids']=[x['id'] for x in ledger['source_child_statuses'] if x['id'] not in source]
ledger['remaining_reverse_primary_child_ids']=[x['id'] for x in ledger['reverse_child_statuses'] if x['id'] not in reverse]
assert len(ledger['remaining_source_child_ids'])==627 and len(ledger['remaining_reverse_primary_child_ids'])==124
write(TASK/'reception-ledger.json',ledger)

interface=read(TASK/'interfaces.json')
joined=[]
consumer_manifest=read(TASK/'splits/P07/result/evidence/necessary-consumers.json')
available_consumers={x['original']['id']:x for x in consumer_manifest['objects']}
for i in interface['four_full_original_interfaces']:
    owned=[(cid,s,n,c) for cid,(s,n,c) in compounds.items() if i['id'] in c['original']['finite_interfaces']]
    all_producer_ids=[x['id'] for cid,s,n,c in owned for x in c['original']['children']]
    needed=sorted({rx for cid,s,n,c in owned for rx in c['original']['necessary_consumers']})
    joined.append({'id':i['id'],'received_compound_ids':[cid for cid,s,n,c in owned],
      'received_source_child_ids':all_producer_ids,
      'complete_compound_contributions':[pointer(s,n,'compounds') for cid,s,n,c in owned],
      'necessary_context_ids':needed,
      'group3_context_assessments':{rx:available_consumers[rx]['receiver_assessment'] for rx in needed if rx in available_consumers},
      'status':'GROUP3_EDGES_RECEIVED_OTHER_PRODUCERS_AND_CUMULATIVE_RECEIVERS_OPEN',
      'scope':'Actual received group3 producer/necessary context only; full original interface not closed.'})
interface['cumulative_group3_edges']=joined
interface['shortcut_index_qualification']='Original group3 receiver_local_source_child_ids arrays are empty; retained unchanged. Cumulative edges are reconstructed from the fully received compound children, not from empty advisory arrays. This is an index repair for integration, not a new finding or rereview.'
interface['cross_group_pending']={
 'source_primary_ids':ledger['remaining_source_child_ids'],
 'reverse_primary_ids':ledger['remaining_reverse_primary_child_ids'],
 'explicit_group3_foreign_facet':{'id':'FC40-TURN.01','route':'CORE/R01','meaning':reverse['FC40-TURN.01'][2]['foreign_facet']},
 'RX-CORE-ENTRY_evidence_binding':'Group3 preserves a bounded entering-callback assessment, but its53-row actual-reading manifest has no E039 row. Preserve that source-read claim without assigning a fabricated IO; bind exact E039 complete entry unit through actual R01 receipt when delivered. This does not reopen P10 primary or add a finding.',
 'full_consumer_primary_facts':'R01/R02/R03/H01 actual deliverables still awaited; context receipts do not sign all24 whole facts.'}
interface['status']='GROUP3_CONTRIBUTIONS_JOINED_FULL_INTERFACES_OPEN'
write(TASK/'interfaces.json',interface)

reading=read(TASK/'reading-ledger.json')
reading['cumulative_group3_reception']={
 'binding':binding,'actual_business_objects_read':{'compounds':27,'source_child_assertions_and_reasons':183,'assigned_reverse_objects_and_reasons':36,
 'unique_complete_formal_relation_objects':33,'necessary_consumer_objects':13,'mandatory_handler_object':1},
 'read_method':'Read full actual contribution values and limits, not all primary source again. Repeated original objects verified equal fixed parent then their complete business values read; exact repeated fields/identity indexes de-duplicated explicitly. Unique receiver rationales all literally presented.',
 'reading_repairs':['Combined schema/report and compound outputs truncated; omitted P09 report and compound269–273 reread.','Reverse combined output middle truncated; P07 last6 business contributions repaired, CLEAN01/02 then reread compact.','No omitted/truncated value counted before repair.'],
 'source_read_credit':'Primary source reading stays with actual group3; this parent receives contribution semantics. No new parent SOURCE_FULL claim.',
 'identity_only_checks':identity_rows,'business_execution':'NOT_EXECUTED'}
write(TASK/'reading-ledger.json',reading)

counters=read(TASK/'proposal-counters.json')
counters['group3_received_qualification']={
 'commit':FIXED,'platform_binding':GROUP_CONTEXT,
 'actual_complete_business_object':read(TASK/'splits/P07/result/proposal-counters.json'),
 'GR8-ECB-001':'Receive group3 finite source/counter conclusion preserving existing bounded NO_REQUIRED. Root direct whole original counter-package reception remains H01-owned; do not invent a new independent final vote.',
 'GR8-ECB-002':'Group3 explicitly did not read full counter; retain H01 ownership.',
 'GR8-COM-001':'Existing required/P3 corroboration only: STALL order bracket differs from TRUANT action gate. Preserve original canonical root and pending global history, newrequired0/newoptional0.',
 'new_required':0,'new_optional':0,'new_independent_final_votes':0}
write(TASK/'proposal-counters.json',counters)

progress=read(TASK/'progress.json')
progress['utc']=NOW; progress['status']='INCOMPLETE_GROUP3_RECEIVED_WAIT_OTHER_ACTUAL_RESULTS'
progress['completed']['received_source_children']=183
progress['completed']['received_compounds']=27
progress['completed']['received_reverse_primary_facets']=36
progress['completed']['reverse_without_explicit_foreign_facet']=35
progress['remaining']['source_children']=627
progress['remaining']['formal_children']=124
progress['remaining']['explicit_group3_foreign_join']='FC40-TURN.01 CORE/R01'
progress['capacity_handoff']='Four groups were actually dispatched by parent. Frozen split-dispatch.json preserves generation-time plans; current receipt is group3 actual contribution only. No new dispatch record/context/review layer.'
progress['next']='Wait for other actual group deliveries, receive their exact contributions, join cumulative interfaces/history, then root final decision.'
progress['actual_group3_delivery']=binding
failure={'action':'Group3 identity-only integration validation',
 'actual':'First run raised KeyError workspace_tree on X-* identity aliases, before any ledger write.',
 'correction':'X aliases bind exact commit/path/blob without workspace_tree; choose repository by fixed R commit, verify full bytes/blob/line count, rerun successfully. No semantic inference from failed run.'}
if failure not in progress['failure_and_correction_log']:
    progress['failure_and_correction_log'].append(failure)
write(TASK/'progress.json',progress)

publication=read(TASK/'publication.json')
publication['current_cumulative_reception']='GROUP3_RECEIVED_PARENT_TASK_INCOMPLETE'
publication['group3_source_commit']=FIXED
publication['group3_source_file_count']=33
publication['group3_scope']='27 methods/183 source assertions/36 reverse primary facets; same-byte import only. Other groups not yet received.'
publication['completed_scope']='Initial31 units and eight finite comparisons retained; actual group3 full contribution business received without rereading its whole primary source.'
publication['remaining_scope']='627 source children,124 other reverse primary facets,FC40-TURN.01 foreign join,whole central/consumer/history reception await actual other groups.'
publication['final_binding']='Initial core receipt remains historical. This cumulative commit is ordinary-pushed and independently read back; its actual commit/tree are bound by tool result and final reply, without recursive self hashes.'
write(TASK/'publication.json',publication)

validation=read(TASK/'validation.json')
validation['cumulative_group3_validation']={'utc':NOW,'source_commit':FIXED,'source_file_count':33,
 'exact_original_compounds':27,'exact_source_child_objects':183,'exact_reverse_child_objects':36,
 'disjoint_from_unreceived_primary_ids':True,'source_identity_rows_checked':53,'mandatory_unit_hashes':31,
 'all_original_group_payloads_unchanged':True,'semantic_credit_from_checks':0,
 'result':'PASS_INTEGRITY_ONLY_PARENT_TASK_INCOMPLETE'}
write(TASK/'validation.json',validation)
print(json.dumps({'source_commit':FIXED,'received_compounds':27,'received_source_children':183,
 'received_reverse_primary_facets':36,'explicit_foreign_open':foreign_open,
 'remaining_source_children':627,'remaining_reverse_primary_facets':124,
 'original_group_files_imported':33,'new_required':0,'new_optional':0,'status':'INCOMPLETE'}))
