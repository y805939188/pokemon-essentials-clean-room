"""Check exact input and disjoint split coverage. Tool validation only."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import subprocess

task=Path(__file__).resolve().parent.parent
root=task.parent.parent
repo=root.parents[2]
def read(p): return json.loads(p.read_text())
def git(*args): return subprocess.check_output(['git','-C',str(repo),*args]).decode().strip()
dispatch=read(task/'split-dispatch.json')
original=task/'inputs/target-5cf9503a'
f=read(original/'forward-mapping.json')
r=read(original/'reverse-mapping.json')
rs=read(root/'delegation/readsets/receive_external_com_battler.complete.json')
for row in rs['files']:
    data=(original/row['relative_to_target_task']).read_bytes()
    assert len(data)==row['bytes']
    assert hashlib.sha256(data).hexdigest()==row['sha256']
    assert hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()==row['git_blob']
compound_ids=[]; children=[]; reverse_ids=[]; fact_ids=[]
all_compounds={x['id']:x for x in f['compounds']}
primary=[]
for entry in dispatch['jobs']:
    pack=read(repo/entry['readset']['path'])
    assert entry['status']=='PLANNED_CONTEXT_NOT_CREATED'
    for item in pack['primary_compounds']:
        assert item==all_compounds[item['id']]
        compound_ids.append(item['id'])
        children.extend(c['id'] for c in item['children'])
    reverse_ids.extend(pack['assigned_reverse_child_ids'])
    fact_ids.extend(pack['consumer_primary_ids'])
    for key in ['prompt','readset']:
        data=(repo/entry[key]['path']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==entry[key]['sha256']
        assert len(data)==entry[key]['bytes']
    assert str(task.relative_to(root))+'/splits/'+entry['id']+'/result/' == entry['exclusive_write_set']
assert set(compound_ids)==set(all_compounds) and len(compound_ids)==289
assert len(children)==len(set(children))==810
assert set(children)=={c['id'] for x in f['compounds'] for c in x['children']}
assert len(reverse_ids)==len(set(reverse_ids))==160
assert set(reverse_ids)=={c['id'] for x in r['clause_groups'] for c in x['subassertions']}
assert len(fact_ids)==len(set(fact_ids))==24
assert set(fact_ids)=={x['id'] for x in f['consumer_facts']}
for row in read(original/'identities.json')['files']:
    if row['purpose']!='primary_reference': continue
    data=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',row['commit']+':'+row['path']])
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
    assert len(data.splitlines())==row['line_count']
    primary.append({'evidence_id':row['evidence_id'],'path':row['path'],'bytes':len(data),
      'lines':len(data.splitlines()),'sha256':row['sha256'],'credit':'IDENTITY_ONLY'})
assert len(primary)==10 and sum(x['lines'] for x in primary)==4646
assert sum(x['bytes'] for x in primary)==183690
json_count=0
for p in task.rglob('*.json'):
    if any(x.endswith('.git') for x in p.parts): continue
    read(p); json_count+=1
assert read(task/'reception-ledger.json')['status']=='INCOMPLETE'
assert read(task/'reception-ledger.json')['complete_producer_children_received']==0
assert read(task/'reception-ledger.json')['complete_selected_formal_children_received']==0
assert git('rev-parse','HEAD')=='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'
result={'schema':'r8-com-battler-delivery-integrity/v1',
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'result':'PASS_TOOL_VALIDATION_ONLY_TASK_INCOMPLETE','target_inputs':10,
 'target_bytes':2576539,'split_jobs':15,'compound_partition':289,'source_child_partition':810,
 'reverse_child_partition':160,'consumer_primary_partition':24,'partition_overlap':0,
 'parsed_json_files':json_count,'primary_parent_identities':primary,
 'B8_formal_tree':git('rev-parse','HEAD:deliverables/final-specification-set'),
 'R_commit':subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse','HEAD']).decode().strip(),
 'semantic_credit':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
(task/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='primary_parent_identities'}))
