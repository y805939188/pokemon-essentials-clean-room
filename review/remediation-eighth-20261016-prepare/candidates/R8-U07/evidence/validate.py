"""Static metadata/identity validation only. Does not execute a behavioral vector."""
import json,pathlib,subprocess,hashlib,datetime
ROOT=pathlib.Path(__file__).resolve().parents[5]
C='review/remediation-eighth-20261016-prepare/candidates/R8-U07'
E=ROOT/C/'evidence'; BASE='4575e80d041ab0c74a42e2e36399d05791dbaa5b'
TARGET='review/remediation-eighth-20261016-prepare/navigation/current-r7-metadata-qualification.json'
R7='review/remediation-seventh-20261015-prepare';B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
checks=[]
def check(label,value):
 assert value,label
 checks.append(label)
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def load(path,commit=B8):return json.loads(git('show',commit+':'+path))
def resolve(doc,pointer):
 if pointer=='':return doc
 for part in pointer.split('/')[1:]:
  part=part.replace('~1','/').replace('~0','~');doc=doc[int(part)] if isinstance(doc,list) else doc[part]
 return doc
p=ROOT/C/'mirror'/TARGET;o=json.loads(p.read_text());r=load(R7+'/delegation/task-registry/current.json');l=load(R7+'/ledger.json');pbl=load(R7+'/completion/current-public-reception.json');cl=load(R7+'/closure/final/decision.json')
for key,s in o['sources'].items():
 b=git('show',s['commit']+':'+s['path']);mode,typ,sha=git('ls-tree',s['commit'],'--',s['path']).decode().split('\t')[0].split()
 check('fixed_source:'+key,len(b)==s['bytes'] and hashlib.sha256(b).hexdigest()==s['sha256'] and sha==s['blob'] and mode==s['mode'] and typ=='blob')
 check('protected_local_source:'+key,(ROOT/s['path']).read_bytes()==b)
ref_count=0
def walk(v):
 global ref_count
 if isinstance(v,dict):
  if 'source' in v and isinstance(v['source'],str) and v['source'] in o['sources']:
   s=o['sources'][v['source']];b=git('show',s['commit']+':'+s['path']);
   if 'pointer' in v:resolve(json.loads(b),v['pointer'])
   ref_count+=1
  for x in v.values():walk(x)
 elif isinstance(v,list):
  for x in v:walk(x)
walk(o)
check('historical_counters_exact',o['stage_counts']['historical_projection']['values']==r['semantic_stage_counters'])
check('historical_counter_generation_unknown',o['stage_counts']['historical_projection']['field_generation_utc']=='UNVERIFIED')
check('current_four_stages_exact',o['stage_counts']['current_at_B8']['counters']==l['counters']=={s:27 if s.endswith('_items') else 13 for s in l['counters']})
check('public_final_counts_exact',all(pbl[x]==27 for x in ['candidate_PASS_items','actual_applied_items','actual_independent_PASS_items','ACCEPTED_items','CLOSED_items']) and pbl['batches']==13)
check('closure_27_records_retained',len(cl['records'])==27 and all(x['formal_ACCEPTED'] and x['CLOSED'] for x in cl['records']))
check('42_unique_task_IDs',len(r['entries'])==len({x['task_id'] for x in r['entries']})==42)
check('population_original_counts',o['task_population']['unique_task_ids']==42 and o['task_population']['actual_review_contexts']==12 and o['task_population']['reviewer_result_versions']==32 and o['task_population']['actual_review_result_versions']==15)
for b,index in zip(o['candidate_r2_bindings'],[2,6,9]):
 old=l['batches'][index];new=b['current_r2'];hist=b['historical_initial_r1_dispatch'];rr=load(o['sources'][new['reception']['source']]['path'])['parent_receipt']
 check(b['batch_id']+':exact_r2_pair',new['result_commit']==rr['result_commit']==old['candidate_review_commit'] and new['result_tree']==rr['result_tree'] and new['reviewer_task_id']==rr['reviewer_task_id']==old['reviewer_context'])
 check(b['batch_id']+':distinct_excluded_r1',hist['reviewer_task_id']==old['reviewer_task_id']!=new['reviewer_task_id'] and hist['reviewer_prompt_path']==old['reviewer_prompt_path'] and hist['r1_root_eligibility']=='WAIT_INPUT_OR_INDEPENDENCE' and hist['field_generation_utc']=='UNVERIFIED')
 entry=resolve(r,new['registry_entry']['pointer']);check(b['batch_id']+':registry_pair',entry['result_commit']==new['result_commit'] and entry['task_id']==new['reviewer_task_id'])
check('ordinary_U02_control_unchanged',l['batches'][1]['reviewer_task_id']==l['batches'][1]['reviewer_context']=='01a13ff0-0f85-70d4-b48e-b15a4ba68038' and all(x['batch_id']!='R7-U02' for x in o['candidate_r2_bindings']))
u=o['u06_continuation'];cur=u['completed_continuation'];proc=load(o['sources'][u['process_decision']['source']['source']]['path']);rec=load(o['sources'][cur['parent_reception']['source']]['path']);report=git('show',B8+':'+o['sources'][cur['signed_report']['source']]['path']).decode()
check('U06_exact_result_and_context',cur['result_commit']==rec['parent_receipt']['result_commit']=='55a843b3ab01d26442f604770f30932e120f923b' and cur['result_tree']==rec['parent_receipt']['result_tree'] and cur['reviewer_task_id']==rec['parent_receipt']['reviewer_task_id']==r['continuations']['R7-U06']['same_thread'])
check('U06_exact_turn',cur['continuation_turn_id']==r['continuations']['R7-U06']['turn_id'])
check('U06_process_does_not_grant_PASS',u['process_decision']['PASS_granted_by_this_decision']==proc['PASS_granted_by_this_decision']==False and u['old_WAIT']['result_commit']==proc['original_WAIT_commit'])
check('U06_old_start_exact',u['historical_start_projection']['value']==l['batches'][5]['actual_integration_continuation_state']=='PARENT_CONTINUATION_STARTED_WAIT_RESULT' and u['historical_start_projection']['field_generation_utc']=='UNVERIFIED')
check('U06_completion_time_is_signed_report_fact',cur['signed_completion_utc'] in report and cur['parent_reception_utc']==rec['utc'])
check('U06_continuation_adds_no_context',cur['new_contexts']==cur['new_independent_votes']==0 and cur['new_independent_reviewer']==False and cur['state']==r['continuations']['R7-U06']['status'])
u=o['u12_input_receipt_scope'];h=u['historical_input_receipt'];n=u['current_content_result'];inp=load(o['sources'][h['source']['source']]['path']);oldinp=load(o['sources'][h['old_input_receipt']['source']]['path']);rec=load(o['sources'][n['parent_reception']['source']]['path'])['parent_receipt'];per=load(o['sources'][n['per_id']['source']]['path']);elig=load(o['sources'][n['eligibility']['source']]['path'])
check('U12_original_input_time_and_WAIT_scope_exact',h['retained_input_utc']==inp['utc']==oldinp['utc'] and h['retained_result_scope']==inp['result_scope']==oldinp['result_scope'] and inp['full_semantic_review_complete'] and not oldinp['full_semantic_review_complete'])
check('U12_exact_completed_pair',n['result_commit']==rec['result_commit']=='fd112431b76e39980364e1177cbb3109b34b5a33' and n['result_tree']==rec['result_tree'] and n['reviewer_task_id']==rec['reviewer_task_id']==elig['task']['reviewer_task_id'])
check('U12_current_two_PASS_exact',n['verdicts']=={x['record_id']:x['verdict'] for x in per['records']}=={'GR7-M19-001':'PASS_SCOPED_ACTUAL_INTEGRATION','GR7-H08-001':'PASS_SCOPED_ACTUAL_INTEGRATION'})
check('U12_not_completion_backfill','signed_completion_utc' not in n and n['new_contexts']==n['new_independent_votes']==0)
for row in json.loads((E/'source-identities.json').read_text())['source_spec_and_optional_files']:
 b=git('show',row['commit']+':'+row['path']);check('full_source_identity:'+str(row['index']),len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'])
check('formal_target_absent_unmodified',not (ROOT/TARGET).exists())
changed=git('diff','--name-only',BASE).decode().splitlines();untracked=git('ls-files','--others','--exclude-standard').decode().splitlines();paths=sorted(set(changed+untracked));check('exclusive_batch_write_set',all(x==str(pathlib.Path(C)/'mirror'/TARGET) or x.startswith(C+'/evidence/') for x in paths))
check('reference_fixed_identity',subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse','HEAD'],text=True).strip()=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b')
check('independent_branch',git('branch','--show-current').decode().strip()=='codex/r8-u07-revision-20261017')
for f in (ROOT/C).rglob('*.json'):json.loads(f.read_text())
result={'schema':'r8-u07-author-static-validation.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'classification':'TOOL_VALIDATION_STATIC_METADATA_ONLY','checks_satisfied':len(checks),'checks':checks,'all_source_references_resolve':ref_count,'source_bytes_verified':sum(s['bytes'] for s in o['sources'].values()),'derived_scenarios':'dispositions.json; NOT_EXECUTED behavior','new_Ruby_game_native_host_media_save_replay_runs':0,'candidate_independent_PASS':'NOT_GRANTED_BY_AUTHOR','actual_integrated_PASS':'PENDING','ACCEPTED':False,'CLOSED':False}
(E/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False))
