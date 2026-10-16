import json,pathlib,hashlib,datetime,subprocess
rr=pathlib.Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e')
p=rr/'tasks/pbs_world_record_audit'; dst=p/'received-final-v2';dst.mkdir(exist_ok=True)
now=datetime.datetime.now(datetime.timezone.utc).isoformat();R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';B='fd1df570cad987dc3852a3b958f03916e317f7fe'
def load(path):return json.loads((rr/path).read_text())
def save(path,obj):(p/path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def bind(path):
 b=(rr/path).read_bytes();return dict(path=path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
# Exact report reception is distinct from primary source or formal reading.
full=[
 'adjudication/root-primary-task-final-registry.v1.json',
 'adjudication/root-world-primary-task-final-acceptance.v1.json',
 'adjudication/root-ui-primary-task-final-acceptance.v1.json',
 'adjudication/root-kernel-task-final-acceptance.v1.json',
 'adjudication/root-facility-task-final-acceptance.v1.json',
 'adjudication/root-item-task-final-acceptance.v1.json',
 'adjudication/root-creature-d-task-final-acceptance.v1.json',
 'adjudication/root-creature-e-task-final-acceptance.v1.json',
 'adjudication/root-pbs-current-task-final-acceptance.v1.json',
 'adjudication/root-readable-binary-resource-task-final-acceptance.v1.json',
 'tasks/world_full/interfaces.json','tasks/world_full/review.md',
 'tasks/ui_full/interfaces.json','tasks/ui_full/review.md',
 'tasks/kernel_atomic_reception/interfaces.json',
 'tasks/facility_atomic_completion_cloud/v2/review.md',
 'tasks/creature_b/interfaces.json',
 'tasks/pbs_creature_current_cloud/remaining-necessary-interfaces.v1.json',
 'evidence/external-recovered/receive_external_creature_d/173c822a14d2fccb28083c24da03bee6b500e7b2/finite-receptions.json'
]
receipts=[]
for path in full:
 b=(rr/path).read_bytes();name=path.replace('/','__');(dst/name).write_bytes(b)
 receipts.append({**bind(path),'report_read_status':'FULL_CURRENT_ARTIFACT_READ','snapshot':'received-final-v2/'+name,'source_FULL_credit_transferred':False,'formal_FULL_credit_transferred':False})
facpath='tasks/facility_atomic_completion_cloud/v2/interfaces.json';fd=load(facpath)
facids=['FAC-I01','FAC-I02','FAC-I07','FAC-I08','FAC-I09','FAC-I12'];selected=[x for x in fd['interfaces'] if x['id'] in facids]
assert len(selected)==6
save('received-final-v2/facility-interfaces-selected.json',{'original':bind(facpath),'selected_complete_objects':selected,'reading_scope':'Only these six complete objects actual read; other seven interface objects only mechanically indexed, not FULL semantic credit here.'})
receipts.append({**bind(facpath),'report_read_status':'SIX_COMPLETE_SELECTED_INTERFACE_OBJECTS_READ','ids':facids,'snapshot':'received-final-v2/facility-interfaces-selected.json','source_FULL_credit_transferred':False,'formal_FULL_credit_transferred':False})
old=load('tasks/pbs_world_record_audit/interfaces.json')
closing=[
('PBSW-I01','KERNEL schema / parser / compile / registration / save / reverse writer',
 ['KAR-I-PBS','KAR-I-WORLD-GEN','KAR-I-INTL-MEDIA','SFR01–31 root-qualified definition scope'],
 ['adjudication/root-kernel-task-final-acceptance.v1.json','tasks/kernel_atomic_reception/interfaces.json'],
 'Own complete world schemas and necessary compiler/write ranges retained. Root-qualified kernel current necessary definitions and direct special facility paths received; explicit backups remain alternative author inputs, no recursive autoactivation. Ordinary SaveData retains object references; native archive execution is not inferred.',
 'Whole kernel clauses beyond these field/identity/compiler/persistence contacts and all other PBS raw paths remain original-owner credit, not a local unresolved interface.'),
('PBSW-I02','TownMap / MapPosition / MapSize → RegionMap / Area / fly UI',
 ['UIFULL-I11','UIFULL-I16','WI-FIELD-UI','original UI-I04/UI-I14'],
 ['adjudication/root-ui-primary-task-final-acceptance.v1.json','tasks/ui_full/interfaces.json','tasks/ui_full/review.md'],
 'All27 points/two regions remain own raw reading; actual UI primary now includes MapMetadata138/PBS398 full and area24 plus69 complete record notes, RegionMap/Area/query/first-match/visibility/fly/cancel/return and persistence intent. Source compile permits MapSize width0 and does not validate shape length/binary content; no such invalid value is invented for supplied records.',
 'Entire UI or all native fly outputs/compiled populations not granted. Missing compiled map_metadata remains a separate exact material boundary.'),
('PBSW-I03','connections / map metadata / global-player metadata → topology / transfer / weather / audio / save',
 ['WI-TOPOLOGY','WI-WEATHER','WI-PERSISTENCE','WI-FIELD-UI','WI-PLAYER-STEP','WI-TIME-CONSUMERS','W01–W06/W19–W21/W27–W31'],
 ['adjudication/root-world-primary-task-final-acceptance.v1.json','tasks/world_full/interfaces.json','tasks/world_full/review.md'],
 'All19 connections,69 map sections and3 global/player sections remain own producer facts. Actual world primary current root-qualified receiver binds zero-size filtering, anchors, temporary setup/resident reuse, lifecycle/transfer/blackout, weather/audio request and save/load/name paths under their normal/cancel/failure prefixes. Default PBS051 marker known; actual Map051 body/bindings/load/runtime remain unknown. Map flags are finite predicates at actual receivers, not guarantees of all events.',
 'Original whole-world/formal approval, arbitrary event/plugin configurations, actual physical maps/media and global history remain foreign/global, not a required local source reread.'),
('PBSW-I04','1888 cup row records → explicit facility lists / parser / creation / TrainerNos / predicates / cached traits / session',
 ['FAC-I01','FAC-I02','FAC-I07','FAC-I08','FAC-I09','FAC-I12'],
 ['adjudication/root-facility-task-final-acceptance.v1.json','tasks/facility_atomic_completion_cloud/v2/review.md','tasks/facility_atomic_completion_cloud/v2/interfaces.json'],
 'Actual facility v2 complete raw1888 five-field literal reception, all1600 trainers72 TrainerType, raw649 equivalence classes2732 provenances and typed453 defaults2727 profiles648 bodies join necessary compiler/default/inheritance/create/cache/rule/pool/restoration contracts. This closes the previously concrete field/TrainerNos/rule consumer reception. Own cup order/empty slots/EV codes/literal spelling and unreferenced618 remain unchanged. Previous conditional graph/eligibility mathematical evidence retains original provenance; no new checker, arithmetic recomputation, generated-team or loop-termination claim.',
 'Whole facility source/formal FULL is retained by its actual readers. All templates legal, all reachable, runtime battles and unrestricted callback behavior are not asserted. Optional debug RNG root is not a new PBSW proposal.'),
('PBSW-I05','80 ribbons → GameData registration / Pokemon ordered holder operations / Summary / finite purification / save',
 ['own Ribbon48/Pokemon726–785/Summary835–900','UIFULL-I07','UIFULL-I14','RX-CD-J09','KAR finite SaveData'],
 ['adjudication/root-ui-primary-task-final-acceptance.v1.json','tasks/ui_full/interfaces.json','adjudication/root-creature-d-task-final-acceptance.v1.json','evidence/external-recovered/receive_external_creature_d/173c822a14d2fccb28083c24da03bee6b500e7b2/finite-receptions.json'],
 'All80 IDs/Name/Description/IconPosition and existing own getter/grant/remove/list and crop consumers retained. UI Summary/Party/lifecycle actual necessary source is complete; CD finite Purify/Chamber and save object boundaries received. Award wording remains display text and cannot establish a contest/facility default award event. A census of arbitrary ordinary/debug award callers was an overbroad foreign-domain request, not an unverified field meaning in these80 records.',
 'All award/gameplay events, whole Shadow and physical save/reload are outside this record partition; source/runtime FULL is not transferred.'),
('PBSW-I06','332 versioned berry records → constructor / planting / watering / mulch / harvest / item/bag / time / weather / conversion',
 ['WI-PBS-WORLD','WI-WEATHER','WI-TIME-CONSUMERS','IF-DATA','IF-INVENTORY','IF-SAVE','RX-CD-J05/J06/J07','KAR current save/compile definitions'],
 ['adjudication/root-world-primary-task-final-acceptance.v1.json','tasks/world_full/interfaces.json','adjudication/root-item-task-final-acceptance.v1.json','tasks/creature_b/interfaces.json','adjudication/root-kernel-task-final-acceptance.v1.json','evidence/external-recovered/receive_external_creature_d/173c822a14d2fccb28083c24da03bee6b500e7b2/finite-receptions.json'],
 'Own BerryPlant45/BerryPlants471 and all explicit hours/drying/yield tuples, mechanisms and interaction prefixes retained. Current actual world whole berry/weather/time receiver, actual item schema/identity/bag finite receipt and complete save/conversion receiver supply the necessary field→lookup→message/receipt→object-save contacts. Gen6–8 association with default remains exact-byte factoring; Gen5 remains64 explicit records; no generation switch inferred.',
 'All held-item battle callbacks, all clock behavior and all historical save/native compatibility are foreign/runtime qualifications, not unfinished berry-field reading.'),
('PBSW-I07','2 parameters ×2 tilesets / Dungeon flag → constructor / seed / layout / tile writes / placement / temporary map caller',
 ['GEN01–GEN10','WI-PBS-WORLD','WI-TOPOLOGY','WI-MAINCATALOG','KAR-I-WORLD-GEN'],
 ['adjudication/root-world-primary-task-final-acceptance.v1.json','tasks/world_full/interfaces.json','tasks/world_full/review.md','tasks/kernel_atomic_reception/interfaces.json'],
 'All four current finite parameter×tileset field combinations and whole own generator1107/WP14 retained; actual world receiver explicitly accepts complete GEN01–10 and outer Map/Factory/caller facts plus complete current WP14 data tables/vectors. Constructor-before-seed, parameter/S/system seed priority, clearS/global reseed, redraw continuing random prefix, negative area, empty antiring, each density0 interruption, original-map write order and event versus player failure prefixes remain exact.',
 'Actual Map051 tileset/area/events/compiled activation, seed-to-pixel outcome, native RNG, arbitrary termination and all plugin inputs are not proved; this is no remaining named producer/consumer reception.'),
('PBSW-I08','3 phone sets /41 fields → whole-set fallback / dialogue choice / contact/UI / TP-TE / time / rematch / persistence',
 ['IF-PHONE','IF-SAVE','RX-CD-J04','UIFULL-I11/I12','KAR current Time/source/save definitions'],
 ['tasks/creature_b/interfaces.json','evidence/external-recovered/receive_external_creature_d/173c822a14d2fccb28083c24da03bee6b500e7b2/finite-receptions.json','adjudication/root-ui-primary-task-final-acceptance.v1.json','tasks/ui_full/interfaces.json','adjudication/root-kernel-task-final-acceptance.v1.json'],
 'Own Phone706/PhoneMessage100/phone48/WP63 whole reading and all41 ordered field bodies retained. Actual full PhoneUI/current lifecycle and finite encounter producer reception bind Contact-passing UI versus missing Phone.get identifier wrapper, eager TP/TE before token inspection, Land→Cave→Water first nonempty and firstmin(4,n) equal slot choice, whole-set current→start→default fallback, time predicates, normal End and rematch flag1→2-before-play prefix. Old unsupported DayCare phone-notification assertion is explicitly rejected.',
 'Authored concrete TrainerBattle/common events/maps/NPC reachability, every possible data version, actual clock/media/call/save execution and whole WP63 other domains are not inferred.')
]
rows=[]
for id,chain,units,paths,meaning,excluded in closing:
 prev=next(x for x in old['interfaces'] if x['id']==id)
 rows.append({'id':id,'chain':chain,'status':'COMPLETE_CURRENT_ASSIGNED_NECESSARY_FINITE_RECORD_INTERFACE','original_status':prev['status'],'original_snapshot':'interfaces.json#'+id,'original_primary_reader':'/root/pbs_world_record_audit','actual_receiver_units':units,'qualified_receipts':[bind(x) for x in paths],'current_accepted_complete_finite_meaning':meaning,'foreign_or_runtime_qualification':excluded,'current_necessary_available_unread':[],'current_necessary_consumer_unreceived':[],'source_FULL_credit_added':0,'formal_FULL_credit_added':0,'behavior':'NOT_EXECUTED'})
material=[];repo=pathlib.Path('/workspace/pokemon-essentials')
for id,path,meaning in [
 ('PBSW-MAT-01','Data/map_metadata.dat','Compiled effective MapMetadata population/load is not supplied. All69 raw PBS sections including051 Dungeon=true were actually read; raw known does not prove compiled loaded state.'),
 ('PBSW-MAT-02','Data/Map051.rxdata','Actual map dimensions, tileset ID, events and playable default binding unavailable. Do not derive them from Dungeon flag or dungeon author tables.'),
 ('PBSW-MAT-03','Data/System.rxdata','Actual serialized System project data not supplied; no actual project-start/tileset/engine activation inferred from Ruby/PBS declarations.')]:
  proc=subprocess.run(['git','cat-file','-e',R+':'+path],cwd=repo,capture_output=True)
  assert proc.returncode!=0 and not (repo/path).exists()
  material.append({'id':id,'path':path,'fixed_R_git_object_exists':False,'working_file_exists':False,'status':'EXACT_MATERIAL_ABSENT_NOT_AVAILABLE_UNREAD','meaning':meaning,'tool_evidence':'Read-only filesystem existence and fixed git cat-file lookup; no data load/compile executed.','utc':now})
remaining={'schema':'gr8-pbs-world-final-remaining/v2','utc':now,'status':'CURRENT_ASSIGNED_NECESSARY_AVAILABLE_READING_AND_FINITE_RECEPTION_COMPLETE','necessary_available_unread':[],'necessary_producer_consumer_unreceived':[],'material_absent':material,'retained_available_partial_or_unread_outside_this_primary':[
 {'id':'PBSW-FOREIGN-01','scope':'Own partial WP11/WP03/WP04/WP21/WP66 and partial compiler/other consumers retain original ledger ranges; actual complete necessary peer contributions received above.','disposition':'NO_PERSONAL_FULL_PROMOTION; not a local producer/consumer blocker'},
 {'id':'PBSW-FOREIGN-02','scope':'Whole Facility/Kernel/World/UI/Creature/Item formal/source domains beyond these eight finite contacts and all other raw PBS/backup populations','disposition':'ORIGINAL_OWNER_PRIMARY; no inherited FULL; no new unbounded literal/graph audit'},
 {'id':'PBSW-FOREIGN-03','scope':'All ordinary/debug ribbon award events, arbitrary event/plugin callers and unrestricted data combinations','disposition':'NOT_PROMISED_BY_FIELD_CONTRACT; no false default event/reachability guarantee'}],
 'global_owner_qualifications':[{'id':'PBSW-GLOBAL-01','scope':'Global historical equivalence, alias/root deduplication, all-current-domain final seal and final whole-review count','owner':'/root and original history/domain owners','disposition':'NOT_LOCAL_AVAILABLE_UNREAD; not granted by this completion'}],
 'execution_qualifications':[{'id':'PBSW-EXEC-01','scope':'Reference Ruby/game/native/model/physical input/media/clock/random/save-reload/project reachability','status':'NOT_EXECUTED','new_runs':0},{'id':'PBSW-EXEC-02','scope':'Previous facility conditional pure mathematical/graph tool results keep original provenance; no new recomputation or loop termination proof','status':'ORIGINAL_QUALIFICATION_RETAINED'}],
 'required_change_handoff':['GR8-PBSW-001','GR8-PBSW-002'],'UPDATE_NOT_STARTED':True,'new_actual_contexts':0,'new_independent_votes':0}
save('interfaces.final.v2.json',{'schema':'gr8-pbs-world-current-final-interfaces/v2','utc':now,'fixed_B8':B,'fixed_R':R,'original_snapshot_retained':'interfaces.json','interfaces':rows,'necessary_interface_count':8,'current_necessary_unreceived':0,'no_foreign_whole_domain_FULL':True,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})
save('remaining.final.v2.json',remaining)
save('final-reception.v2.json',{'schema':'gr8-pbs-world-current-primary-final-reception/v2','utc':now,'actual_reader':'/root/pbs_world_record_audit','continuation_of_original_context':True,'continuation_start_utc':'2026-10-16T14:23:58Z','new_actual_contexts':0,'new_independent_votes':0,'new_primary_source_or_formal_read_credit':0,'report_artifacts_actual_read':receipts,'accepted_interface_ids':[x['id'] for x in rows],'source_and_formal_reading_credit':'All original FULL vs PARTIAL and exact-byte Gen6–8 association remain unchanged in reading-ledger.json. This continuation receives qualified complete finite peer meanings, not their whole source/formal FULL.','scope_correction':'Original foreign-domain/global requests are explicitly separated from the exact18-record-input partition. Resolved concrete consumers are closed only through named actual existing reader receipts, never by a status count alone.','failure_and_truncation_qualification':'First combined root E/PCR receipt output was globally truncated; both complete artifacts re-read individually. Earlier global file listing was truncated and earns inventory-only navigation, not semantic credit. No original PBS/source was re-read solely to invent a new vote.','actual_configuration':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','Fast':'UNVERIFIED','opaque_agent_UUID':'UNVERIFIED','opaque_session_ID':'UNVERIFIED'},'logical_task_ID':'/root/pbs_world_record_audit','business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})
oldreview=load('tasks/pbs_world_record_audit/review.json')
review={'schema':'gr8-pbs-world-final-primary-signature/v2','utc':now,'status':'REVIEW_COMPLETE_WITH_REQUIRED_CHANGE_HANDOFF_AND_RETAINED_MATERIAL_NATIVE_GLOBAL_QUALIFICATIONS_UPDATE_NOT_STARTED','actual_primary_reader':'/root/pbs_world_record_audit','fixed_B8':B,'fixed_R':R,'primary_files':18,'primary_records':2400,'forward_field_occurrences':24980,'finite_reverse_rows_retained':25,'primary_unread':0,'necessary_available_unread':0,'necessary_consumer_unreceived':0,'original_reading_qualification':'Gen6–8 berry exact same bytes as default, complete semantics identity factored without new independent text read; all other original scope and source/formal ranges unchanged.','current_required_handoff':['GR8-PBSW-001','GR8-PBSW-002'],'classification':'Existing root requiredP3 finite contracts only; no new findings/classification/count increments.','original_root_reception':'root-decision-reception.json','new_required':0,'new_optional':0,'new_actual_contexts':0,'new_independent_votes':0,'business_runs':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'whole_review_complete':False,'B8_formal_compliance_or_global_PASS':False,'actual_configuration':'Each model/effort/tier/speed/Fast/opaque UUID/session field UNVERIFIED; requested values not certification.','operative_report':'review.final.v2.md','operative_interfaces':'interfaces.final.v2.json','remaining':'remaining.final.v2.json','reception':'final-reception.v2.json','manifest':'delivery-manifest.final.v2.json','original_snapshots_retained':['review.md','review.json','interfaces.json','reading-ledger.json','proposals.json','forward.json','reverse.json']}
save('review.final.v2.json',review)
print('Written v2 scoped reception only at',now)
