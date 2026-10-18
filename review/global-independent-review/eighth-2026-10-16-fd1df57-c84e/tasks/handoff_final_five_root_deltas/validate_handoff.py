"""Check bounded document composition; never executes a game or changes Git."""
from pathlib import Path
from collections import Counter
import hashlib
import json

TASK = Path(__file__).resolve().parent
RR = TASK.parent.parent
REPO = RR.parents[2]
H = TASK/'handoff'
def read(p): return json.loads(p.read_text())
root = read(RR/'adjudication/root-decisions.partial.json')
index = read(H/'records-index.json')
contracts = read(H/'contracts.delta.zh.json')
manifest = read(H/'cloud-eighth-update-handoff-manifest.json')
batches = read(H/'batch-assignment.json')['batches']
graph = read(H/'dependency-graph.json')
conflicts = read(H/'file-conflict-graph.json')
checks = {}
checks['exact_38_current_classification_severity'] = [(x['id'],x['classification'],x.get('severity')) for x in index['records']] == [(x['id'],x['classification'],x.get('severity')) for x in root['records']]
checks['exact_root_counts'] = manifest['bounded_counts'] == root['bounded_counts'] == {'required':29,'required_P2':2,'required_P3':27,'optional':9}
required = [x['id'] for x in root['records'] if x['classification']=='required']
assigned = [rid for b in batches for rid in b['required_ids']]
checks['29_unique_required_primary_batches'] = Counter(assigned) == Counter(required) and all(n==1 for n in Counter(assigned).values())
checks['nine_batches_and_zero_current_launch'] = len(batches)==9 and graph['currently_startable_count']==0 and manifest['currently_startable_count']==0
checks['nine_optionals_unselected'] = len([x for x in index['records'] if x['classification']=='optional'])==9 and all(b['selected_optional_ids']==[] for b in batches)
checks['independent_policy_unselected_empty_write'] = graph['independent_policy']['selection']=='UNSELECTED' and graph['independent_policy']['required_write_set']==[] and manifest['policy_count']==1
checks['no_new_semantic_or_transitive_edges'] = graph['semantic_edit_edges']==[] and graph['transitive_closure_edit_edges']==[]
checks['source_spec_identity_carriers_no_copied_source'] = read(H/'source-spec-readset.delta.json')['source_code_copied'] is False
checks['future_core_and_enclosing_commit_not_fabricated'] = manifest['R8_core']['commit'] is None and manifest['R8_core']['tree'] is None and manifest['enclosing_report_commit'] is None
checks['no_update_or_business_execution'] = manifest['update_started'] is False and manifest['execution']['new_business_runs']==0
checks['new_five_records_exact_ids'] = [x['id'] for x in contracts['records']]==[x['id'] for x in root['records'][33:]]
checks['WP31_corrected_64_and_52'] = '64' in contracts['records'][0]['complete_contract']['minimal_revision_contract']['preserve'][0] and '52不是注册身份数量' in contracts['records'][0]['complete_contract']['minimal_revision_contract']['preserve'][0]
checks['MG32_exact_targets_and_32_preserved'] = len(contracts['records'][4]['operation']['mandatory_target_write_set'])==2 and manifest['shared_catalog']['vector_count']==32 and '别名前缀' in manifest['shared_catalog']['preserve']
checks['all_actual_file_writers_unique_integrator'] = len({x['path'] for x in conflicts['actual_file_writers']})==len(conflicts['actual_file_writers']) and all(x['actual_writer']=='R8-INTEGRATOR' for x in conflicts['actual_file_writers'])
checks['nine_full_original_prompt_section_dedup_proofs'] = len(read(TASK/'verification/original-prompt-dedup.json')['proofs'])==9
identity_failures=[]
for item in manifest['input_payloads']:
    p=REPO/item['path']; b=p.read_bytes()
    if len(b)!=item['bytes'] or hashlib.sha256(b).hexdigest()!=item['sha256'] or hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()!=item['blob']:
        identity_failures.append(item['path'])
checks['all_bound_input_payloads_still_exact'] = not identity_failures
for batch in batches:
    prompt=(H/f"batches/{batch['id']}/prompt.md").read_text()
    assert batch['inherited_complete_prompt']['sha256'] in prompt
    assert all(rid in prompt for rid in batch['required_ids'])
    assert 'UPDATE_NOT_STARTED' in prompt
checks['all_nine_prompts_bind_full_original_and_exact_ids'] = True
result={'schema':'r8-bounded-handoff-composition-validation/v1','checks':checks,'passed':all(checks.values()),
        'failed_input_identities':identity_failures,'scope':'TOOL_VALIDATION only; no source semantic/adjudication/actual remediation acceptance credit',
        'records':38,'new_contracts':5,'required':29,'optional':9,'independent_policy':1,'new_business_runs':0,'update_started':False}
(TASK/'verification/validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
assert result['passed']
