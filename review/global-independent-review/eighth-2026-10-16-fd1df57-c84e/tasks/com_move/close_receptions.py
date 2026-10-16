from pathlib import Path
import json,hashlib,datetime,subprocess,shutil

P=Path(__file__).resolve().parent;RR=P.parents[1]
W=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials')
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(p):return json.loads(p.read_text())
def save(n,v):(P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def meta(p):return {'path':str(p.relative_to(RR)) if p.is_relative_to(RR) else str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
stamp=now()
old=P/'prior-deliveries/20261016T040203'
if not old.exists():
 old.mkdir(parents=True)
 for n in ['progress.json','identities.json','reading-ledger.json','forward-mapping.json','reverse-mapping.json','interfaces.json','proposals.json','review.md','delivery-files.json','validation.json']:
  shutil.copyfile(P/n,old/n)

creb=RR/'tasks/creature_b';pbs=load(creb/'pbs-record-reception.json')
facility=load(creb/'facility-item-interface.json')
creb_ledger=load(creb/'reading-ledger.json')
pbs_reads=[r for r in creb_ledger['initial'] if r['identity']['path'].startswith('PBS/')]
assert len(pbs_reads)==6
for r in pbs_reads:
 f=R/r['identity']['path'];assert meta(f)['sha256']==r['identity']['sha256']
assert sum(r['own_full_read'] for r in pbs_reads)==5
root_files=['mandatory-stage-kind-evidence-reception.v1.json','root-after-all-hits-reception.v1.json','root-f054-clarification-reception.v1.json','mandatory-item-pinch-false-gluttony-meaning-qualification.v1.json','root-battler-three-schema-facts-reception.v1.json']
root_inputs={n:load(RR/'adjudication'/n) for n in root_files}
stage=root_inputs[root_files[0]]
stage_qualifiers=[{'id':x['id'],'original_record_index':x['record_index'],'original_kind_pointer':x['kind_pointer'],'old_kind_preserved':x['old_kind_preserved'],'effective_kind':'Ordinary target-stage requests as stated in behavior/step_detail; constructor constant list is absent, requests are not absent.','actual_behavior':x['behavior'],'formal':x['formal'],'premise':x['premise']} for x in stage['ten_complete_raw_objects_and_exact_fields']]
assert len(stage_qualifiers)==10
mandatory=[meta(RR/'adjudication'/n) for n in root_files]
mandatory += [meta(RR/'tasks/core_atomic_reception/core-f054-mandatory-straighten-clarification.v1.json'),meta(RR/'tasks/pbs_creature_current_cloud/battler-finite-reception.v1.json')]
save('mandatory-qualifications.current.json',{
 'schema':'gr8-com-move-mandatory-current-qualifications/v1','utc':stamp,'actual_receiver':'/root/com_move','same_context_followup':True,'new_contexts':0,'new_independent_votes':0,
 'read_basis':'Complete mandatory Stage472 lines (single embedded line437 reread after output truncation), after-all-hits136, F054root73 plus207-line full clarification, Pinch91, typed-schema33 plus275-line full finite packet actually read. Original MOVE full source/11formal and exact needed definitions retained, not reread denominators.',
 'input_bindings':mandatory,
 'stage_ten':stage_qualifiers,
 'stage_common':'Keep original493602-byte stage table immutable. All ten actual behavior/request amounts/order/gates were correct and remain accepted. The old no-direct-ordinary-request kind label is inaccurate for these ten only and must always be consumed with this companion. 114/65+49 and67+47 are different partitions; no extra atoms or new formal issue.',
 'after_all_hits':{'effective_fact':'Master pbUseMove calls after-all-hits outside the hit loop once per original target entry after reached post-loop processing. It is distinct from per-hit pbProcessMoveHit callbacks. Delivery is not necessarily a successful effect: each family and central qualification controls changes.','controls':'Scale Shot ordinary two-hit fixture yields one Defense−1 then Speed+1 request, not two. A miss can leave zero successful hits yet still reach post-loop delivery; unaffected can suppress effect. Earlier whole-use return never reaches it. Prefix writes survive a later failure; no all-callback shared-guard claim.','root_disposition':'GR8-CAR-CAND-004 NO_REQUIRED_BOUNDED_SCOPE; correct combined WP40/WP46 retained; no new required/optional/vote.'},
 'F054':{'effective_fact':'Old CORE-F054 再通知/朝向 is not proof of a direction write. Reached default Game_Character#straighten conditionally resets pattern when walk_anime or step_anime, always resets anime_count/prelock_direction; no direction assignment or turn_* call.','preserved':'Earlier poison-count/form/partner/canlose-heal/wait/event and separate result-record facts retain normal-callback/reached-tail scope. No whole-battle direction invariant or transactional cleanup.','root_disposition':'Existing GR8-COM-005 required/P3 limited upstream WP39 phrase; count/classification unchanged. Original old source fact and raw bytes preserved.'},
 'Pinch':{'effective_fact':'After canConsumeBerry permission, HP<=floor(H/4) passes. Above quarter through half, check_gluttony=false does not require Gluttony and accepts both active and inactive Gluttony. True/default requires active Gluttony. Neither admits above half.','preserved':'Ordinary itemActive/canHeal/stat gates and forced-specific bypasses stay separate. No absence-of-Gluttony predicate and no new formal defect.'},
 'typed_data':{'effective_fact':'For ClassMethodsSymbols, get/try_get validate Symbol/String/same-class; same-class instance returns directly before registered membership. Unknown valid key strict get raises/try_get nil; nil try_get nil; invalid primitive fails validate. Raw array membership does not normalize each entry.','own_exact_definitions':'GameData1–283 and Kernel validate1–31 now actually complete source-read in this same context; original Item270 and Battler001 full source retained. No foreign-source FULL transfer.','name_qualification':'Actual Item#unlosable?(species,ability) is distinct from Battler#unlosableItem?; earlier descriptive unlosable_by_species? is no new method.','activation_representation':'Record/schema/constructor/JSON token are distinct from compiled Ruby scalar representation, registry activation, effect-handler registration, cache replacement and existing live object state. No automatic conversion, activation, whole4.2MB typed-record receipt or native/save-load proof from a serialized packet.'},
 'scope':'All these are necessary current evidence meanings, not approval of whole outside domains. No source/formal fix, new business run or new review layer.',
 'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})

received={'schema':'gr8-com-move-pbs-scoped-final-reception/v1','utc':stamp,'actual_receiver':'/root/com_move','producer':'/root/creature_b','received_source_artifact':meta(creb/'pbs-record-reception.json'),'actual_full_artifact_read':True,
 'accepted_policy_ids':['PBS-FIELDS','PBS-FLAGS','PBS-FLING-NG','PBS-PATHS'],'complete_policy_objects':[x for x in pbs['record_policy_facts'] if x['id'] in ['PBS-FIELDS','PBS-FLAGS','PBS-FLING-NG','PBS-PATHS']],
 'actual_source_readers':pbs_reads,'record_denominators':pbs['record_denominators'],'reader_credit':'Five full raw paths remain CRE-B credit; Gen8 is proven byte path association only, not a separate full display. COM-MOVE retains its own578Fling fields and namedchild1900 relevant-field projection; reception transfers exact finite facts, not personal rawFULL of3154 path-record instances.',
 'consumer_join':'NaturalGift current active Berry/prefix admission, first complete type+numeric flag and registered-type fallback, per-hit current item identity/power, existing malformed flag versus nil identity failure; Fling active/losable/prefix/berry permission, numeric minimum/default, substitute/ShieldDust named effects, current-item suffix consumption all match locally fully read R008/R011 and complete Battler/item reaction definitions.',
 'generation_boundary':'Gen5 NaturalGift60/70/80 versus later80/90/100 are conditional data inputs; no unsupported Gen7/default type difference, and backups not concurrently activated. No inventory/compiled/runtime proof from field receipt.',
 'facility_identity_scope':facility['facts'],'facility_boundary':facility['accepted_scope'],'state':'ACCEPTED_FINITE_TWO_WAY_CONSUMER_JOIN','necessary_remaining':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
save('pbs-consumer-reception.current.json',received)

ints=load(P/'interfaces.json')
for x in ints['interfaces']:
 if x['id'] in ['COM-MOVE-IN-BATTLER','COM-MOVE-IN-ABILITY-ITEM']:
  x['state']='NECESSARY_SOURCE_FACTS_AND_CONSUMERS_RECEIVED'
  x['remaining']='No exact necessary COM-MOVE fact is missing. Entire outside formal-domain task-final is separate root-owned work, not a local prerequisite. No personal FULL or unreceived factual credit is inferred.'
  x['whole_external_formal_task_final']='OUTSIDE_THIS_FINITE_TASK_ROOT_OWNS'
 if x['id']=='COM-MOVE-OUT-PBS':
  x['state']='ACCEPTED_FINITE_BY_NAMED_RECEIVER';x['receiver_evidence']='../creature_b/pbs-record-reception.json PBS-FLING-NG';x['actual_reception']='Complete producer policy artifact, six exact identities and true five-full/one-associated ledger entries read; finite two-way consumer relation accepted in pbs-consumer-reception.current.json.';x['remaining']='No necessary finite binding remains. Entire PBS/domain approval and runtime activation not implied.'
ints.update({'updated_utc':stamp,'local_primary_unreceived_semantic_units':0,'assigned_necessary_consumer_unreceived':0,'assigned_available_unread':0,'outbound_receiver_binding_open':0,'whole_domain_final_receptions_open':0,'whole_domain_qualification':'The earlier2 represented entire external-domain approvals, not2 exact missing COM-MOVE facts. Reclassified without granting those approvals; root external Battler/Ability continuation remains independently owned.','not_material_limits':'No local necessary unread/unreceived item is hidden as limit or discharged by whole-domain role approval. Exact facts actually read/received and current mandatory companions are bound.','mandatory_companion':'mandatory-qualifications.current.json'})
save('interfaces.json',ints)
remaining={'schema':'gr8-com-move-remaining-necessary/v2','utc':stamp,'assigned_available_unread':0,'assigned_necessary_producer_unreceived':0,'assigned_necessary_consumer_unreceived':0,'outbound_binding_pending':0,'exact_local_remaining':[],
 'outside_task_not_local_approval_gate':[{'scope':'COM-BATTLER complete formal domain / root group1–2 continuation','owner':'/root','status':'ROOT_OWNED_OUTSIDE_SCOPE_NOT_GRANTED','local_fact_basis':'All ten exact sources and actual needed facts already read/received; full outside formal approval does not add a missing local producer fact.'},{'scope':'COM-ABILITY-ITEM complete formal domain / CONT01 continuation','owner':'/root','status':'ROOT_OWNED_OUTSIDE_SCOPE_NOT_GRANTED','local_fact_basis':'Both complete handler files and necessary callers read, exact finite callback/data meanings received; entire foreign formal domain not granted.'},{'scope':'Global history/equivalent dedup/native host/whole review and source remediation','owner':'/root','status':'OUTSIDE_FINITE_TASK_NO_APPROVAL_GRANTED'}],
 'new_contexts':0,'new_votes':0,'new_findings':0,'new_required':0,'new_optional':0,'actual_configuration_and_UUID':'UNVERIFIED','business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
save('remaining.json',remaining)
pr=load(P/'progress.json');pr.update({'status':'REVIEW_COMPLETE_NECESSARY_JOINS_CLOSED_ROOT_TASK_FINAL_PENDING','updated_utc':stamp,'end_utc':stamp,'dependencies_unreceived':[],'outbound_receiver_binding_pending':[],'outside_whole_domain_qualification':'See remaining.json: external whole formal approvals kept root-owned, not counted as local missing definitions/facts.','same_context_followup':True,'new_contexts':0,'new_independent_votes':0,'necessary_available_unread':0,'necessary_consumer_unreceived':0,'preflight':'READY_WITH_UNVERIFIED_CONFIGURATION','mandatory_companions':'mandatory-qualifications.current.json'});save('progress.json',pr)

dep=load(P/'dependency-facts.json')
dep['GameDataCurrent']={'path':'Data/Scripts/010_Data/001_GameData.rb','intervals':[[1,283]],'status':'FULL_READ_DEPENDENCY','reviewer':'/root/com_move','facts':["All three mixins distinguish allowed argument classes, nil try_get and unknown-key failure. Same-class get/try_get returns directly without membership. ClassMethodsSymbols raw DATA replacement, ordered enumeration, equality Symbol/String/sameclass/integer-id_number branch and PBS export omission semantics read. load_all/candidate file enumeration do not themselves prove compiled/native success."],'mandatory':'mandatory-qualifications.current.json:typed_data'}
dep['ValidationCurrent']={'path':'Data/Scripts/001_Technical/001_Debugging/004_Validation.rb','intervals':[[1,31]],'status':'FULL_READ_DEPENDENCY','reviewer':'/root/com_move','facts':['validate requiresHash; arraycondition accepts any is_a?, Symbolcondition requiresrespond_to?, othercondition is_a?; errors collected and ArgumentError raised unlessnone. Invalid primitives are not treated as unknown legal data IDs.']}
dep['CORE-F054-current-qualification']={'producer':'/root/core_atomic_reception','receiver':'/root/com_move','status':'FINITE_COMPLETE_CLARIFICATION_RECEIVED','artifact':'../core_atomic_reception/core-f054-mandatory-straighten-clarification.v1.json','effective':'Reached defaultstraighten changesanimation bookkeeping/conditionalpattern, notdirection; old朝向shorthand remains originalevidence requiringcurrentcompanion. Normaltail/earlierpartyforms/status/partner/canlose-heal/event/resultsequence qualified separately.','mandatory':'mandatory-qualifications.current.json:F054'}
save('dependency-facts.json',dep)
fw=load(P/'forward-mapping.json');fw['dependency_facts']=dep;fw['mandatory_current_qualifications']='mandatory-qualifications.current.json';fw['finite_pbs_final_reception']='pbs-consumer-reception.current.json';save('forward-mapping.json',fw)
rv=load(P/'reverse-mapping.json');rv['global_domain_receptions_not_claimed']=['Whole external Battler andAbility formal domains remain root-owned outside this finite task; not local unread/unreceived facts.'];rv['mandatory_current_qualifications']='mandatory-qualifications.current.json';rv['necessary_remaining']='remaining.json';save('reverse-mapping.json',rv)
sr=load(P/'subreview-receptions.json');sr['current_required_companion']='mandatory-qualifications.current.json:stage_ten';sr['rows']['stage_table']['current_qualification']='All10 old no-direct-request kind labels require the current companion; empty constructor parameter lists are not zero requests. Original behavior/order/gates and114 count remain retained.';save('subreview-receptions.json',sr)
bl=load(P/'battler-reception.json');bl['necessary_COM_MOVE_reception']='CLOSED exact needed facts/callers; whole external formal-domain approval remains outside scope, not local pending.';bl['mandatory_current_qualification']='mandatory-qualifications.current.json:typed_data';save('battler-reception.json',bl)
al=load(P/'ability-item-source-reception.json');al['necessary_COM_MOVE_reception']='CLOSED exact needed callback/data/caller facts; foreign whole-domain approval not implied or required as local gate.';al['mandatory_current_qualification']='mandatory-qualifications.current.json:Pinch';save('ability-item-source-reception.json',al)
ledger=load(P/'reading-ledger.json');ledger['final_necessary_reception']={'artifact':'remaining.json','available_unread':0,'consumer_unreceived':0,'same_actual_context_no_new_review_layer':True};ledger['mandatory_current_qualifications']='mandatory-qualifications.current.json';ledger['named_PBS_receiver']='pbs-consumer-reception.current.json'
for path,total,key in [('Data/Scripts/010_Data/001_GameData.rb',283,'GameDataCurrent'),('Data/Scripts/001_Technical/001_Debugging/004_Validation.rb',31,'ValidationCurrent')]:
 f=R/path;io=[]
 for p in (P/'io').glob('read-*.json'):
  j=load(p)
  if j.get('path')==str(f):io.append(str(p.relative_to(P)))
 row={'payload':path,'reviewer':'/root/com_move','sha256':meta(f)['sha256'],'bytes':f.stat().st_size,'total_lines':total,'continuous_intervals':[[1,total]],'unread_intervals':[],'status':'FULL_READ_DEPENDENCY','facts_key':key,'original_io':io}
 ledger['dependencies']=[x for x in ledger['dependencies'] if x['payload']!=path]+[row]
save('reading-ledger.json',ledger)
ident=load(P/'identities.json');ident['same_context_final_reception_utc']=stamp;ident['new_contexts_or_votes']=0;ident['current_mandatory_companions']=mandatory;save('identities.json',ident)

ops=[]
for args,cwd in [(['git','diff','--quiet','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','--'],R),(['git','diff','--stat','fd1df570cad987dc3852a3b958f03916e317f7fe','--','deliverables/final-specification-set'],W)]:
 start=now();z=subprocess.run(args,cwd=cwd,text=True,capture_output=True);ops.append({'args':args,'cwd':str(cwd),'start_utc':start,'end_utc':now(),'stdout':z.stdout,'stderr':z.stderr,'exit':z.returncode})
save('final-reception-operations.json',{'utc':stamp,'operations':ops,'behavior_runs':0,'no_Ruby_or_game_execution':True})
checks={'primary_frozen_26_identities':all(hashlib.sha256((Path(x['repo'])/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in ident['readset_files']),'primary_15R_11F_retained':ledger['primary_full_reference']==15 and ledger['primary_full_formal']==11,'331_actual_vector_judgments_retained':len(load(P/'vector-review.json')['rows'])==331 and not load(P/'vector-review.json')['actual_semantic_proof_missing'],'old_stage_payload_immutable':meta(P/'subreviews/attributes_calling/stage-table-reception.json')['sha256']=='0cd8abd0f58a5facac244b2363f881e30327b092e8995621074647fd2ae2fa0a','ten_kind_qualifications':len(stage_qualifiers)==10,'PBS_six_true_reader_qualifications':len(pbs_reads)==6 and sum(x['own_full_read'] for x in pbs_reads)==5,'local_necessary_remaining_zero':not remaining['exact_local_remaining'] and ints['outbound_receiver_binding_open']==0,'source_diff_zero':ops[0]['exit']==0,'formal_diff_empty':ops[1]['exit']==0 and not ops[1]['stdout'],'new_review_layers_zero':pr['new_contexts']==0 and pr['new_independent_votes']==0}
save('final-reception-validation.json',{'utc':now(),'type':'DELIVERY_AND_IDENTITY_STATIC_VALIDATION','checks':checks,'status':'PASS' if all(checks.values()) else 'FAIL','business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})
print(json.dumps({'status':'PASS' if all(checks.values()) else 'FAIL','necessary_unread':0,'necessary_unreceived':0,'new_contexts':0,'new_votes':0,'PBS_receipt':meta(P/'pbs-consumer-reception.current.json')},ensure_ascii=False))
