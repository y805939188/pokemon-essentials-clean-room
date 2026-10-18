raise SystemExit('Superseded at checkpoint25: use current explicit root state; this historical generator must not overwrite new actual contexts/classifications.')
from pathlib import Path
import json,hashlib,datetime,shutil,subprocess
root=Path(__file__).resolve().parents[1];repo=root.parents[2]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(p,x):
 f=root/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def load(p):return json.loads((root/p).read_text())
h=root/'tasks/history_current';hist=json.loads((h/'subshards.json').read_text())
write('delegation/history-subshards.snapshot.json',hist)
shutil.copyfile(h/'recover_transport.py',root/'delegation/helpers/recover_transport.py')
jobs=[]
for s in hist['shards']:
 name=s['id'].lower().replace('-','_');read=json.loads(Path(s['readset_path']).read_text())
 read.update(primary_task=name,write_root=str(root/'tasks'/name),recovery_tool=str(root/'delegation/helpers/recover_transport.py'))
 read['recovery_tool_write_note']='Read whole helper; copy into this task own write root (TASK is __file__ parent); restore only into fresh absent directory. Restored evidence is never executed.'
 write('delegation/readsets/'+name+'.json',read)
 prompt=Path(s['prompt_path']).read_text().replace(str(h/'contract.md'),str(root/'inputs/eighth-global-review-prompt.md')).replace(s['readset_path'],str(root/'delegation/readsets'/f'{name}.json'))
 prompt+='\n正式独占写集已赋为 `'+str(root/'tasks'/name)+'`。实际平台ID由真实启动回显填写，未知UNVERIFIED。技能在 `'+str(root/'inputs/review-SKILL.md')+'`。恢复helper在 `'+str(root/'delegation/helpers/recover_transport.py')+'`，先全文读懂，再复制到任务独占目录；TASK自动取自身父目录。所有7个原历史commit与15份关键原载荷已由history_current在隔离bare成功fetch并核身份，旧LOCAL_MISSING已解除，不把本地缓存条件冒作材料limit。新的环境可按精确SHA在自身隔离bare普通fetch。原文件/proposal/证据只读，UPDATE_NOT_STARTED。\n'
 (root/'delegation/prompts'/f'{name}.md').write_text(prompt)
 jobs.append({'id':name,'scope':s['scope'],'prompt':'delegation/prompts/'+name+'.md','readset':'delegation/readsets/'+name+'.json','write_set':'tasks/'+name+'/','input_rows':len(read['files']),'input_bytes_with_versions':s['input_decoded_bytes_with_versions'],'state':'NO_ACTUAL_START_RECEIPT_IN_COORDINATOR','requested':s['requested_configuration']})
write('delegation/third-wave.json',{'schema':'gr8-third-wave/v2','utc':now,'additional_jobs':jobs,'additional_count':4,'previous_dispatchable_count':21,'all_dispatchable_count':25,'input_availability_validation':'tasks/history_current/dispatch-validation.json','semantic_status':'Only actual read ledgers grant semantic credit; dispatch is not completion','update_started':False})
snap=root/'evidence/proposal-snapshots';snap.mkdir(parents=True,exist_ok=True)
proposals=[]
for name in ['kernel_review','combat_review','history_current','world_topology_audit','ui_navigation_audit','pbs_world_record_audit','com_ai','binary_controller_strings_review','world_full','world_interpreter','ui_full','binary_remaining_texts','binary_ruby_zlib_remaining']:
 p=root/'tasks'/name/('findings.json' if name in ['kernel_review','combat_review','history_current'] else 'proposals.json')
 if not p.exists():continue
 raw=p.read_bytes();x=json.loads(raw);sha=hashlib.sha256(raw).hexdigest();target=snap/(name+'-'+sha+'.json');target.write_bytes(raw)
 items=x if isinstance(x,list) else x.get('records',x.get('proposals',x.get('findings',[])))+x.get('discoveries',[])+x.get('new_program_discoveries',[])
 for item in items:proposals.append({'origin_task':name,'immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':item,'root_status':'WAIT_ROOT_FINAL_CANONICAL_ADJUDICATION'})
cp=root/'tasks/creature_review/proposals/GR8-CRE-001.v2.json'
if cp.exists():
 raw=cp.read_bytes();sha=hashlib.sha256(raw).hexdigest();target=snap/('creature_review-'+sha+'.json');target.write_bytes(raw)
 proposals.append({'origin_task':'creature_review','immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':json.loads(raw),'root_status':'INDEPENDENT_RECOMMENDATION_RECEIVED_WAIT_ROOT_CANONICAL_ADJUDICATION','independent_review':'tasks/combat_review/adjudications-creature.json'})
active_candidate=root/'tasks/core_atomic_reception/candidate-skip-parenthesis.v1.json'
if active_candidate.exists():
 raw=active_candidate.read_bytes();sha=hashlib.sha256(raw).hexdigest();target=snap/('core_atomic_reception-'+sha+'.json');target.write_bytes(raw)
 proposals.append({'origin_task':'core_atomic_reception','immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':json.loads(raw),'root_status':'BOUNDED_REQUIRED_P3_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION','canonical_id':'GR8-COM-004','independent_review':'adjudication/root-com004-counterreview.json'})
active_candidate=root/'tasks/core_atomic_reception/candidate-straighten-facing.v1.json'
if active_candidate.exists():
 raw=active_candidate.read_bytes();sha=hashlib.sha256(raw).hexdigest();target=snap/('core_atomic_reception-'+sha+'.json');target.write_bytes(raw)
 proposals.append({'origin_task':'core_atomic_reception','immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':json.loads(raw),'root_status':'BOUNDED_REQUIRED_P3_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION','canonical_id':'GR8-COM-005','independent_review':'adjudication/root-com005-counterreview.json'})
active_candidate=root/'tasks/core_atomic_reception/candidate-powder-damage-gates.v1.json'
if active_candidate.exists():
 raw=active_candidate.read_bytes();sha=hashlib.sha256(raw).hexdigest();target=snap/('core_atomic_reception-'+sha+'.json');target.write_bytes(raw)
 proposals.append({'origin_task':'core_atomic_reception','immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':json.loads(raw),'root_status':'WAIT_ACTUAL_DIFFERENT_CONTEXT_COMPLETE_COUNTERREVIEW_AND_ROOT_CLASSIFICATION','canonical_id':None,'independent_review':None})
active_candidate=root/'tasks/core_atomic_reception/candidate-after-all-hits-wording.v1.json'
if active_candidate.exists():
 raw=active_candidate.read_bytes();sha=hashlib.sha256(raw).hexdigest();target=snap/('core_atomic_reception-'+sha+'.json');target.write_bytes(raw)
 proposals.append({'origin_task':'core_atomic_reception','immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':json.loads(raw),'root_status':'WAIT_ACTUAL_DIFFERENT_CONTEXT_COMPLETE_COUNTERREVIEW_AND_ROOT_CLASSIFICATION','canonical_id':None,'independent_review':'delegation/prompts/after-all-hits-existing-kernel-counterreview.md'})
# Preserve complete newlyavailable active candidates without manufacturing reception.
for task in ['core_atomic_reception','kernel_atomic_reception','facility_atomic_completion_cloud']:
 for candidate in sorted((root/'tasks'/task).glob('candidate-*.json')):
  raw=candidate.read_bytes();sha=hashlib.sha256(raw).hexdigest()
  if any(x.get('snapshot_sha256')==sha for x in proposals):continue
  target=snap/(task+'-'+sha+'.json');target.write_bytes(raw)
  proposals.append({'origin_task':task,'immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':json.loads(raw),'root_status':'WAIT_ACTUAL_COMPLETE_NONPROPOSER_COUNTERREVIEW_AND_ROOT_CLASSIFICATION','canonical_id':None,'independent_review':None,'root_semantic_read_credit_from_snapshot':0})
active_facility=root/'tasks/facility_atomic_completion_cloud/proposals.json'
if active_facility.exists():
 raw=active_facility.read_bytes();sha=hashlib.sha256(raw).hexdigest();target=snap/('facility_atomic_completion_cloud-'+sha+'.json');target.write_bytes(raw)
 for record in json.loads(raw).get('records',[]):
  proposals.append({'origin_task':'facility_atomic_completion_cloud','immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':record,'root_status':'WAIT_ACTUAL_DIFFERENT_CONTEXT_COMPLETE_COUNTERREVIEW_AND_ROOT_CLASSIFICATION','canonical_id':None,'independent_review':'delegation/prompts/recorded-scalar-existing-core-counterreview.md','root_semantic_read_credit_from_snapshot':0})
# External full proposal inputs are frozen for actual independent reception; snapshots are not verdicts.
for group,sha in [('localization_records','90b9e27ef03feb2c018bb2f258b5e0d5aaed012b'),('com_battler','5cf9503a99a855c06a8ac9c932e6778b57e71049'),('combat_presentation','18d21310bdc360c87d7ffd886df7d06aef8604a7'),('pbs_creature_backups','b6f12ecfbe006ef0f2ea463d6689d78094915e75'),('creature_d','8434e69e1cc278a514c41f11335ba20d89a95419'),('h_c2_current_records','967b90fac83a6b0c3313087d8871312b4eac18b9'),('legacy_manifest_currentness','93d7df7f66adcaa25811fd6ff09352b754577af0')]:
 candidate=root/'evidence/external-recovered'/group/sha/('findings.json' if group=='h_c2_current_records' else 'proposals.json')
 raw=candidate.read_bytes();digest=hashlib.sha256(raw).hexdigest();target=snap/('external_'+group+'-'+digest+'.json');target.write_bytes(raw);obj=json.loads(raw)
 items=obj.get('records',obj.get('proposals',obj.get('items',obj.get('findings',[]))))
 for item in items:
  proposals.append({'origin_task':'external_'+group,'immutable_external_commit':sha,'immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':digest,'record':item,'root_status':'WAIT_ACTUAL_ROOT_FULL_NONPROPOSER_RECEPTION_OR_CANONICAL_HISTORY_QUALIFICATION','root_semantic_read_credit_from_snapshot':0})
write('findings.json',{'schema':'gr8-findings/v3','utc':now,'proposals':proposals,'adjudicated_required':[],'required_count':None,'required_count_reason':'Whole review and root final canonical adjudication are incomplete; no NO_REQUIRED_UPDATE conclusion','independent_receptions':['tasks/counter_kernel_first/adjudications.json','tasks/combat_review/adjudications-creature.json'],'root_partial_counterreview':'coverage/root-counterreview-notes.json','update_started':False})
scope=load('publication/checkpoint-scope.json')
completed=scope['completed'];running=scope['running']
state=load('progress.json');state.update(utc=now,status='RUNNING',semantic_completion='INCOMPLETE_NO_GLOBAL_PASS',pending_original_dispatch_jobs_without_actual_start_here=scope['original_dispatch_jobs']-len(scope['original_jobs_started_here']),actual_spawned_child_contexts=scope['actual_descendant_contexts_started'],actual_contexts_including_root=scope['actual_descendant_contexts_started']+1,actual_active_collaboration_contexts_including_root=scope['active_including_root'])
state.pop('pending_external_dispatchable_jobs',None)
state['tasks']={n:{'platform_entry':'/root/'+n,'process_status':'COMPLETED' if n in completed else 'RUNNING','semantic_status':'SCOPED_OUTPUT_WITH_OPEN_JOINS' if n in completed else 'IN_PROGRESS','outputs':'tasks/'+n,'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'Fast off'},'actual':dict.fromkeys(['model','effort','tier','speed'],'UNVERIFIED')} for n in completed+running}
for n in scope.get('exited_unpublished',[]):
 state['tasks'][n]={'platform_entry':'/root/'+n,'process_status':'COMPLETED','semantic_status':'SCOPED_OUTPUT_PENDING_PUBLICATION_AND_TASK_FINAL_RECEPTION','outputs':'tasks/'+n,'actual_configuration':'UNVERIFIED'}
state['external_cloud_start_receipts']='delegation/external-starts.current.json:9actualparentrelayedthreadIDs; externalcurrentprocessstatesUNVERIFIED'
state['global_actual_contexts_with_external_receipts']=52
state['global_logical_primary_not_started']=0
state['additional_existing_context_running_tasks']=scope.get('additional_existing_context_running_tasks',[])
state['nested_running_contexts']=scope['nested_running']
state['nested_completed_contexts']=scope['nested_completed']
state['original_dispatch_actual_mapping']=scope['original_jobs_started_here']
state['original_dispatch_scoped_overlaps']=scope['original_jobs_with_scoped_overlaps']
state['proposal_count_at_snapshot']=len(proposals);state['behavior_executions']={'reference_observation':0,'host_demo':0,'native_media':0,'independent_numeric_model_exploration_processes':1,'numeric_model_verification_credit':0,'static_PBS_eligibility_math_audit_processes':1,'root_binary_static_python_processes':2,'root_binary_static_objdump_processes':6,'ruby_primitive_attempt_not_spawned':1,'root_metadata_loader_byte_validation_processes':1}
state['report_metadata_corrections_pending']=[]
state['report_metadata_corrections_completed']=[{'task':'counter_kernel_first','path':'reading-ledger.json','original_requested_range':[595,633],'actual_read_range':[595,624],'actual_source_EOF':624,'evidence':'tasks/counter_kernel_first/correction.json','reading_credit_added':0}]
decisions=load('adjudication/root-decisions.partial.json')
state['bounded_root_decisions']={'path':'adjudication/root-decisions.partial.json','counts':decisions['bounded_counts'],'qualification':decisions['counts_qualification'],'whole_review_required_count':None}
state['declared_coverage_cutpoint']={'input':'tasks/coverage_acceptance_audit/review.md','utc':'2026-10-16T03:20:52.642310+00:00','R_text_full':175,'R_text_partial':43,'R_text_no_ranges':196,'R_binary_separate':18,'formal_full':46,'formal_partial':14,'formal_no_ranges':71,'qualification':'Actual declared read ranges at this cutpoint only; no independent business acceptance. Later running contributions await increment.'}
state['published_dispatch_checkpoint']='a5e395756060501de34824f02f18446b3508fa5d'
state['dispatch_remote_readback']={'files':9475,'bytes':1092732133,'status':'VERIFIED','evidence':'publication/r8-finite-reception-and-handoff-prep-readback-23.json','semantic_credit':'NONE'}
state['current_dispatch_plan']={'path':'delegation/current-plan.json','execution_leaf_plans_including_support':41,'current_primary_leaf_plans':31,'binary_supplement_and_child_plans':2,'actual_supporting_plans':8,'retired_never_started_ui_plans':2,'original_parent_routes_without_receipt':17,'logical_primary_groups_without_local_context':9,'global_logical_primary_groups_not_started':0,'actual_external_primary_contexts':9,'new_semantic_completion_contracts':'3ATOMIC_FROZEN_3ACTUAL_PLUS_FONT_ACTUAL1','supplemental_queue':'delegation/queued-followups.json','planned_is_not_started':True}
state['cloud_input_package']={'library_file_id':'libfile_4b51216024e48191b2cf3166a331583d','bytes':16531493,'sha256':'6a2b23bd78ba13effe19dd00fc26c268edb9ac53a4927eb1ea13412db6e2511e','status':'NOT_MATERIALIZED_DNS_FAILURE','needed':'Exact same ZIP on independent Git branch fixed commit/path, or a working supported Library workspace transfer','cloud_prompt_status':'UNREAD; original full contract read; publisher states section4-end identical'}
state['new_additional_completion_plans']={'count':2,'status':'READY_NOT_STARTED_NO_ACTUAL_CREATION_RECEIPT','manifest':'delegation/handler-atomic-completion-parent-dispatch.json','actual_contexts_started':0,'requested':'gpt-6.1-sol ultra default normal Fastoff'}
state['current_dispatch_plan']['execution_leaf_plans_including_support']=43
state['current_dispatch_plan']['original41_actual_routes']=41
state['current_dispatch_plan']['new_additional_completion_plans_not_started']=2
write('progress.json',state)
status=(root/'publication/checkpoint-status.md').read_text()
(root/'status-report.md').write_text(status)
findings=load('findings.json')
findings['bounded_root_decisions']={'path':'adjudication/root-decisions.partial.json','counts':decisions['bounded_counts'],'whole_review_required_count':None,'qualification':decisions['counts_qualification']}
findings['bounded_canonical_records']=decisions['records']
decision_map={r['id']:r for r in decisions['records']}
for entry in findings['proposals']:
 rid=entry['record'].get('id')
 if rid in decision_map:
  entry['root_status']='BOUNDED_'+decision_map[rid]['classification'].upper()+'_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION_PENDING'
  entry['root_decision_path']='adjudication/root-decisions.partial.json'
  entry['root_decision_version_qualification']='Only exact frozen contract binding in bounded root decision was received; evolving later proposal versions do not inherit full-payload read credit.'
 elif rid == 'GR8-CAR-CAND-001':
  entry['root_status']='BOUNDED_REQUIRED_P3_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION'
  entry['canonical_id']='GR8-COM-004'
  entry['root_decision_path']='adjudication/root-com004-counterreview.json'
 elif rid == 'GR8-CAR-CAND-002':
  entry['root_status']='BOUNDED_REQUIRED_P3_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION'
  entry['canonical_id']='GR8-COM-005'
  entry['root_decision_path']='adjudication/root-com005-counterreview.json'
 elif rid == 'GR8-CAR-CAND-003':
  entry['root_status']='BOUNDED_REQUIRED_P3_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION'
  entry['canonical_id']='GR8-COM-006'
  entry['root_decision_path']='adjudication/root-com006-counterreview.json'
 elif rid == 'GR8-CAR-CAND-005':
  entry['root_status']='BOUNDED_REQUIRED_P3_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION'
  entry['canonical_id']='GR8-COM-007'
  entry['root_decision_path']='adjudication/root-com007-generation-identity-counterreview.json'
 elif rid == 'GR8-CAR-CAND-006':
  entry['root_status']='BOUNDED_REQUIRED_P3_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION'
  entry['canonical_id']='GR8-COM-008'
  entry['root_decision_path']='adjudication/root-com008-switch-order-counterreview.v1.json'
 elif rid == 'GR8-FAC-001':
  entry['root_status']='NO_REQUIRED_BOUNDED_SCOPE_SOURCE_FACT_RETAINED'
  entry['root_decision_path']='adjudication/root-recorded-scalar-reception.v1.json'
 elif rid == 'GR8-CAR-CAND-004':
  entry['root_status']='NO_REQUIRED_BOUNDED_SCOPE_SOURCE_FACT_RETAINED'
  entry['root_decision_path']='adjudication/root-after-all-hits-reception.v1.json'
 elif rid == 'GR8-KAR-001':
  entry['root_status']='NO_REQUIRED_BOUNDED_NIL_LOOKUP_INPUT_SCOPE_SOURCE_FACT_RETAINED'
  entry['root_decision_path']='adjudication/root-hash-default-scope-counterreview.v1.json'
 elif rid in ['GR8-ECB-001','GR8-ECB-002']:
  entry['root_status']='NO_REQUIRED_BOUNDED_SCOPE_SOURCE_FACT_RETAINED'
  entry['root_decision_path']='adjudication/root-'+rid.lower()+'-reception.v1.json'
 elif rid in ['GR8-XPCB-001','GR8-EXT-CD-001']:
  entry['root_status']='NO_REQUIRED_BOUNDED_SCOPE_SOURCE_FACT_RETAINED'
  entry['root_decision_path']='adjudication/root-xpcb001-already-documented-counterreview.v1.json' if rid=='GR8-XPCB-001' else 'adjudication/root-cd001-nonpositive-selector-counterreview.v1.json'
 elif rid == 'GR8-UI-002':
  entry['root_status']='REJECTED_ORIGINAL_EXCEPTION_CANDIDATE_ONLY'
  entry['root_decision_path']='adjudication/root-ui002-reception.json'
 elif rid == 'GR8-RZ-YARB-001':
  entry['root_status']='EXACT_FINITE_DISCOVERY_AND_DIFFERENT_CONTEXT_RECEPTION_ACCEPTED_NO_NORMATIVE_CLAIM'
  entry['root_decision_path']='adjudication/root-ruby-yarb-reception.json'
 else:entry['root_status']='WAIT_ROOT_CANONICAL_CLASSIFICATION_AND_NONPROPOSER_RECEPTION'
findings['independent_receptions']+=['tasks/counter_combat_first/adjudications.json','tasks/counter_world_first/adjudications.json','tasks/world_topology_audit/refutation-ui001.json','tasks/world_topology_audit/refutation-pbsw002.json','coverage/root-pbsw-001-counterreview.json']
findings['independent_receptions']+=['tasks/com_facility/adjudications-ai.json','adjudication/root-hist-001-counterreview.json','adjudication/root-history-facets-counterreview.json']
findings['independent_receptions']+=['adjudication/root-u12-receipt-scope-counterreview.json','adjudication/root-binary-bounded-receptions.json','adjudication/root-world003-counterreview.json','adjudication/root-world004-counterreview.json','adjudication/root-world-int001-reception.json','adjudication/root-world-int002-counterreview.json','adjudication/root-ui002-reception.json','adjudication/root-ui003-counterreview.json','adjudication/root-com004-counterreview.json','adjudication/root-com005-counterreview.json','adjudication/root-com006-counterreview.json','adjudication/root-com007-generation-identity-counterreview.json','adjudication/root-recorded-scalar-reception.v1.json','adjudication/root-com005-wp42-propagation-reception.v1.json','adjudication/root-elr001-counter-reception.v1.json','adjudication/root-gr8-ecb-001-reception.v1.json','adjudication/root-gr8-ecb-002-reception.v1.json']
findings['separate_rejected_proposals']={'path':'adjudication/root-ui002-reception.json','ids':['GR8-UI-002'],'qualification':'Rejected original exception counterexample only; no whole-UI approval.'}
findings['bounded_no_required_reception']={'path':'adjudication/root-binary-bounded-receptions.json','count':4,'qualification':'Only four finite negative claims; no full controller/resource/binary-domain or whole-review NO_REQUIRED_UPDATE.'}
findings['separate_bounded_no_required_candidates']={'ids':['GR8-KAR-001','GR8-CAR-CAND-004','GR8-FAC-001','GR8-ECB-001','GR8-ECB-002'],'receipts':['adjudication/root-hash-default-scope-counterreview.v1.json','adjudication/root-after-all-hits-reception.v1.json','adjudication/root-recorded-scalar-reception.v1.json','adjudication/root-gr8-ecb-001-reception.v1.json','adjudication/root-gr8-ecb-002-reception.v1.json'],'required_added':0,'optional_added':0,'global_qualification':'No whole-review NO_REQUIRED_UPDATE'}
findings['separate_bounded_no_required_candidates']['ids'] += ['GR8-XPCB-001','GR8-EXT-CD-001']
findings['separate_bounded_no_required_candidates']['ids'].append('CREC-WP30-CANCEL-DYNAMIC-READ-SCOPE')
findings['separate_bounded_no_required_candidates']['receipts'] += ['adjudication/root-xpcb001-already-documented-counterreview.v1.json','adjudication/root-cd001-nonpositive-selector-counterreview.v1.json']
findings['separate_bounded_no_required_candidates']['receipts'].append('adjudication/root-wp30-cancel-dynamic-read-scope-reception.v1.json')
findings['independent_receptions'] += ['adjudication/root-com008-switch-order-counterreview.v1.json','adjudication/root-cd001-nonpositive-selector-counterreview.v1.json','adjudication/root-cd002-negative-probability-counterreview.v1.json','adjudication/root-cd003-recording-attribution-reception.v1.json','adjudication/root-cd004-navigation-reception.v1.json','adjudication/root-xpcb001-already-documented-counterreview.v1.json']
write('findings.json',findings)
packed=load('publication/compressed-artifacts.json')
packed_paths={r['original_path'] for r in packed['artifacts']}
selected=[];local_only=[]
for f in root.rglob('*'):
 if not f.is_file() or f.is_symlink():continue
 rel=f.relative_to(root);parts=rel.parts
 if '__pycache__' in parts:continue
 if str(rel) in packed_paths:continue
 if parts[0] in ['inputs','delegation','publication','adjudication'] or len(parts)==1 or rel.as_posix().startswith('coverage/root-') or parts[:2] in [('evidence','proposal-snapshots'),('evidence','adjudication-inputs'),('evidence','compressed'),('evidence','root-binary-counterreview')]:
  if f.name=='checkpoint-selection.json':continue
  selected.append(f);continue
 if len(parts)>2 and parts[0]=='tasks' and parts[1] in completed+['reference_metadata']:
  if any(s=='object-cache.git' or s.startswith(('recovered-','readset-materialized-')) or s=='__pycache__' for s in parts[2:-1]):
   local_only.append(str(rel));continue
  selected.append(f)
for f in selected:
 if f.suffix=='.json':json.loads(f.read_bytes())
rows=[{'path':str(f.relative_to(repo)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(selected)]
write('publication/checkpoint-selection.json',{'schema':'gr8-checkpoint-selection/v1','utc':now,'selected_files_except_this_selection':rows,'count':len(rows),'bytes':sum(x['bytes'] for x in rows),'local_only_cached_inputs':local_only,'exclusion_reason':'Nested bare repository and exact historical input byte caches are reproducible from fixed objects/transport and excluded; recovery receipts preserve identities. No local source/caches removed.','semantic_core_status':'NOT_FROZEN','update_started':False})
selected.append(root/'publication/checkpoint-selection.json')
subprocess.run(['git','-C',str(repo),'add','--']+[str(f.relative_to(repo)) for f in selected],check=True)
staged=subprocess.check_output(['git','-C',str(repo),'diff','--cached','--name-only','-z']).split(b'\0')
prefix=str(root.relative_to(repo))+'/'
assert all(not p or p.decode().startswith(prefix) for p in staged)
print(json.dumps({'selected_report_files':len(selected),'bytes':sum(f.stat().st_size for f in selected),'proposals_at_snapshot':len(proposals),'dispatchable_planned':25,'local_only_cached_input_files':len(local_only),'all_selected_json_valid':True},ensure_ascii=False))
