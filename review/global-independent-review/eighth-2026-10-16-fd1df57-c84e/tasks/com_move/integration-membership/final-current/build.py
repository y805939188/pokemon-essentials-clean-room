"""Thin successor pointer table. Metadata only; no source/record semantic rereading."""
from pathlib import Path
import collections,datetime,hashlib,json
OUT=Path(__file__).resolve().parent;BASE=OUT.parent;RR=BASE.parents[2]
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
START=datetime.datetime.now(datetime.timezone.utc).isoformat();cache={};inputs={};pointer_checks=[];unknown=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def put(n,d):
 with (OUT/n).open('w') as f:json.dump(d,f,ensure_ascii=False,separators=(',',':'));f.write('\n')
def read(n):
 if n not in cache:
  p=RR/n;raw=p.read_bytes();cache[n]=json.loads(raw);inputs[n]={'path':n,'bytes':len(raw),'sha256':sha(raw),'role':'STRUCTURED_METADATA_POINTER_ONLY_NO_NEW_SEMANTIC_CREDIT'}
 return cache[n]
def resolve(d,p):
 for k in p.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');d=d[int(k)] if isinstance(d,list) else d[k]
 return d
def bind(n,p):
 v=resolve(read(n),p);pointer_checks.append({'artifact':n,'pointer':p,'value_sha256_canonical_JSON':sha(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())});return v
def fref(n,p):return {'artifact':n,'pointer':p}
def field(n,p):return {**fref(n,p),'original_value':bind(n,p)}
def entry(n,p):
 d=bind(n,p);out={'artifact':n,'record_pointer':p,'original_fields':[]}
 names={'reader','reviewer','actual_reader','actual_full_reader','actual_context','reviewer_context','receiver','status','semantic_status','read_status','file_status','reading','reading_scope','kind','qualification','credit','own_full_read','whole_read','range','ranges','read_ranges','read_intervals','continuous_read_ranges','continuous_intervals','actual_read_ranges','own_read_range','unread_ranges','unread_intervals','total_lines','complete_file_lines','lines','path','payload','identity_path','repo','commit','bytes','sha256','blob','git_blob','associate_from','all_record_field_semantics','generation_reading_credit'}
 if isinstance(d,dict):
  for k,v in d.items():
   if k in names:out['original_fields'].append(field(n,p+'/'+k))
  if isinstance(d.get('identity'),dict):
   for k,v in d['identity'].items():
    if k in names:out['original_fields'].append(field(n,p+'/identity/'+k))
  if isinstance(d.get('continuous_displays'),list):
   for i,x in enumerate(d['continuous_displays']):
    for k in ['range','stdout','began_utc','ended_utc','exit_code']:
     if k in x:out['original_fields'].append(field(n,p+'/continuous_displays/'+str(i)+'/'+k))
 return out
def check_identity(d,fixed):
 mapping={'path':'path','bytes':'bytes','sha256':'sha256','blob':'git_blob','git_blob':'git_blob','commit':'commit'}
 for k,dst in mapping.items():
  if k in d:assert d[k]==fixed[dst],(k,d[k],fixed[dst])

# The original fifty payloads remain immutable, including frozen23 index and old remaining states.
original_manifest=read('tasks/com_move/integration-membership/delivery-manifest.json')
assert original_manifest['file_count']==50
for x in original_manifest['files']:
 p=BASE/x['path'];raw=p.read_bytes();assert len(raw)==x['bytes'] and sha(raw)==x['sha256'],x['path']
basepath='tasks/com_move/integration-membership/index.json';base=read(basepath)
assert len(base['rows'])==563
fixed={}
for kind,n in [('reference','reference-inventory.json'),('formal','formal-inventory.json')]:
 for i,x in enumerate(read('tasks/inventory_denominator/'+n)):
  fixed[(kind,x['path'])]=(x,fref('tasks/inventory_denominator/'+n,'/'+str(i)))
assert len(fixed)==563

regpath='adjudication/root-primary-task-final-registry.v1.json';reg=read(regpath);assert len(reg['accepted'])==reg['count']==29
receipts={}
for i,x in enumerate(reg['accepted']):
 n=x['receipt']['path'];d=read(n);assert inputs[n]['bytes']==x['receipt']['bytes'] and inputs[n]['sha256']==x['receipt']['sha256']
 assert d.get('task_final_accepted') is True
 receipts[x['task']]={'registry_pointer':'/accepted/'+str(i),'identity':x['receipt'],'declared_status_original':x['status'],'task_final_field':fref(n,'/task_final_accepted'),'qualification':'Existing root acceptance only; this successor grants no personal FULL or semantic PASS.'}
assert receipts['com_ability_item']['identity']['bytes']==15834 and receipts['com_ability_item']['identity']['sha256']=='8e7fe16c8ebee3fbb6c0a6bd4e9c9dbbb49e29320654c238197c62a6b7d842ab'
assert receipts['formal_shared']['identity']['bytes']==79903 and receipts['formal_shared']['identity']['sha256']=='08a971e15bfaaf97bd665d7ff3ed5deb393f6f09d5bd8022a2323b8136112ce7'

overrides=[]
def override(kind,path,coverage,tasks,bindings,qualification):
 f,fr=fixed[(kind,path)]
 x={'id':'O'+str(len(overrides)+1).zfill(2),'kind':kind,'path':path,'fixed_commit':f['commit'],'fixed_identity':{k:f[k]for k in ['bytes','sha256','git_blob']},'fixed_identity_pointer':fr,'coverage_kind_original_qualification':coverage,'actual_reader_bindings':bindings,'current_root_receipt_tasks':tasks,'qualification':qualification,'new_source_reading_credit':0,'personal_FULL_granted_here':False,'semantic_PASS_granted_here':False}
 overrides.append(x);return x

# Eighteen localization files: collective actual original readers, preserving individual partitions.
ELR='evidence/external-recovered/receive_external_localization_records/3f7971a430ec87af7decd149b0b32caad53a5884'
el=read(ELR+'/reading-ledger.json');pa=read(ELR+'/continuation/received-parts/parent-acceptance.json')
assert len(el['literal_record_reads'])==433 and len(pa['records'])==10264
def runs(ns):
 out=[]
 for n in sorted(set(ns)):
  if out and n==out[-1][1]+1:out[-1][1]=n
  else:out.append([n,n])
 return out
textkeys=[(k,f)for k,(f,_)in fixed.items()if k[0]=='reference' and f['payload_kind']=='localization_records'];assert len(textkeys)==18
for (kind,path),f in textkeys:
 domain=Path(path).stem;bindings=[]
 direct=[i for i,x in enumerate(el['literal_record_reads'])if x['domain']==domain]
 if direct:bindings.append({'actor_original':el['reviewer_context'],'actor_pointer':fref(ELR+'/reading-ledger.json','/reviewer_context'),'reading_array_pointer':fref(ELR+'/reading-ledger.json','/literal_record_reads'),'exact_array_index_runs':runs(direct),'navigation_pair_count_not_atoms':len(direct),'coverage':'Original receiver actual personal pair fields only, not all18files personal FULL.'})
 by=collections.defaultdict(list)
 for i,x in enumerate(pa['records']):
  if x['domain']==domain:by[(x['reader_context'],x['part'])].append(i)
 for (actor,part),ns in sorted(by.items()):
  ri=next(i for i,x in enumerate(pa['receipts'])if x['part']==part)
  assert pa['receipts'][ri]['reader_context']==actor
  bindings.append({'actor_original':actor,'part':part,'actor_pointer':fref(ELR+'/continuation/received-parts/parent-acceptance.json','/receipts/'+str(ri)+'/reader_context'),'reading_array_pointer':fref(ELR+'/continuation/received-parts/parent-acceptance.json','/records'),'exact_array_index_runs':runs(ns),'navigation_pair_count_not_atoms':len(ns),'original_reader_ledger':ELR+'/continuation/received-parts/'+part+'/reading-ledger.json','coverage':'Existing actual nonauthor original literal fields; parent reception does not transfer source FULL. Original C-selfUUID qualification remains preserved in parent receipt.'})
 assert bindings
 o=override(kind,path,'QUALIFIED_COMPLETE_LITERAL_PAIR_FIELDS_COLLECTIVELY_READ',['localization_records'],bindings,'All current key/value fields are split among the actual original actors above; no one is assigned personal FULL of all18. Descriptive texts do not establish described game mechanics or execution. Original failed/truncated/partial snapshots remain unchanged.')
 o['header_scope_qualification']={'root_receipt':'adjudication/root-localization-records-task-final-acceptance.v1.json','pointer':'/qualified_primary_typed_populations/headers','declared_headers':bind('adjudication/root-localization-records-task-final-acceptance.v1.json','/qualified_primary_typed_populations/headers'),'qualification':'Root accepts18headers in qualified complete corpus; no invented per-header personal actor.'}
 o['navigation_pair_count_not_atoms']=sum(x['navigation_pair_count_not_atoms']for x in bindings)
assert sum(x['navigation_pair_count_not_atoms']for x in overrides)==10697

# Complete ItemSprites source unit, actual157 lines; old164 claim is not propagated.
item='Data/Scripts/013_Items/007_Item_Sprites.rb';n=ELR+'/continuation/direct-source-reception-2.json';x=bind(n,'/rows/14');assert x['path']==item and x['actual_read_ranges']==[[1,157]] and x['whole_read'] is True;check_identity(x,fixed[('reference',item)][0])
override('reference',item,'EXISTING_COMPLETE_SOURCE_FILE157_NECESSARY_DEFINITIONS',['localization_records'],[entry(n,'/rows/14'),{'actor_original':el['reviewer_context'],'actor_pointer':fref(ELR+'/reading-ledger.json','/reviewer_context')}],'Original actual ELR receiver source read1–157. Original164 locator mistake remains historical, not a fictitious suffix; generated source-copy credit0 remains0.')

# Four identical metrics paths: actual complete literal reception is one alias group, not four new whole readers.
PB='evidence/external-recovered/receive_external_pbs_creature_backups/96ee9a69e24d5e2063be7ebcf8de0fdb2e019510';pb=read(PB+'/reading-ledger.json');lr=bind(PB+'/reading-ledger.json','/literal_readings/1');assert lr['ids']==['P04','P08','P12','P16'] and lr['range']==[1,4045] and lr['rows']==[1,674]
for generation,oldrow in [(5,3),(6,7),(7,11),(8,15)]:
 path=f'PBS/Gen {generation} backup/pokemon_metrics.txt';old=bind(PB+'/recovered-target/reading-ledger.json','/primary/'+str(oldrow));assert old['path']==path and old['total_bytes']==fixed[('reference',path)][0]['bytes']
 prior_fields={k:old[k]for k in ['identity_id','path','file_status','representation','read_ranges','unread_ranges','attestation_pointer']}
 o=override('reference',path,'QUALIFIED_COMPLETE_LITERAL_FIELD_ALIAS_GROUP_READ',['pbs_creature_backups'],[{'actor_original':pb['receiver'],'actor_pointer':fref(PB+'/reading-ledger.json','/receiver'),'reading':entry(PB+'/reading-ledger.json','/literal_readings/1'),'original_raw_attestation':{'artifact':PB+'/recovered-target/reading-ledger.json','record_pointer':'/primary/'+str(oldrow),'fields_original':prior_fields},'current_necessary_metrics_chain_pointer':fref(PB+'/reading-ledger.json','/final_four_generation_integration/complete_finite_interfaces/IF03')}],'Four exact same72120B/SHA payloads carry674ordered metrics rows/all4raw fields read by existing receiver, aliases deduped; original raw FULL_READ is reading only and old section READ_NOT_ACCEPTED/PENDING_MAIN_REVIEWER remains at original time. Not PBSWORLD ownership, not four added reads/votes. Root-backups accepts current IF03 finite schema/compiler/consumer scope; no arbitrary native pixel/audio behavior.')
 o['alias_group_fixed_SHA256']=fixed[('reference',path)][0]['sha256']

# Gen8moves: exact association to default already read by actual PBS battle reader.
n='tasks/pbs_battle/reading-ledger.json';d=read(n);x=bind(n,'/primary/14');base_moves=bind(n,'/primary/19');path='PBS/Gen 8 backup/moves.txt';assert x['associate_from']=='PBS/moves.txt' and x['identity']['sha256']==base_moves['identity']['sha256'];check_identity(x['identity'],fixed[('reference',path)][0]);check_identity(base_moves['identity'],fixed[('reference','PBS/moves.txt')][0])
override('reference',path,'EXACT_BYTE_ASSOCIATION_TO_ACTUAL_DEFAULT_WHOLE_FIELD_READER',['pbs_battle'],[entry(n,'/primary/14'),entry(n,'/primary/19')],'Original status OWN_READ_THEN_EXACT_BYTE_PATH_ASSOCIATION; actual default whole-field reader /root/pbs_battle. Does not invent Gen8 independent rereading or turn associated bytes into a new reader.')

# Tower Pokemon actual raw whole source; trainer files complete lossless field views, no raw-display FULL claim.
n='tasks/facility_atomic_completion_cloud/v2/reading-ledger.json';x=bind(n,'/supplemental/17');path='PBS/battle_tower_pokemon.txt';check_identity(x,fixed[('reference',path)][0]);assert x['read_ranges']==[[1,884]]
override('reference',path,'EXISTING_ACTUAL_RAW_WHOLE882_RECORD_READ',['com_facility'],[entry(n,'/supplemental/17')],'Actual original FAC parent raw884lines/882records; F04/F05/F06 source program readers are separate actual actors, not presumed raw PBS readers. Current constructor/compiler/default joins covered by qualified FAC reception, no runtime execution.')
n='tasks/facility_atomic_completion_cloud/v2/trainer-view-reception.current.json';d=read(n);assert len(d['actual_read'])==6
for i,x in enumerate(d['actual_read']):
 rawpath=bind(n,'/structure_object/metadata/'+str(i)+'/file');assert rawpath in {p for k,p in fixed if k=='reference'}
 assert x['reader']=='/root/facility_atomic_completion_cloud'
 o=override('reference',rawpath,'EXISTING_COMPLETE_LOSSLESS_TRAINER_FIELD_VIEW_READ',['com_facility'],[{'actor_original':x['reader'],'actor_pointer':fref(n,'/actual_read/'+str(i)+'/reader'),'view_reading_pointer':fref(n,'/actual_read/'+str(i)),'raw_path_pointer':fref(n,'/structure_object/metadata/'+str(i)+'/file'),'view_fields_original':{k:x[k]for k in ['path','bytes','sha256','actual_read_windows','records','reader','reading']},'complete_equivalence_pointer':fref(n,'/all_five_literal_fields_and_ordered_integer_pools_equal')}],'All complete literal business fields, ordered pool membership and exact metadata/dictionary bindings received in actual lossless views. Original explicitly says raw PBS full-file display is not claimed; old partial receipt is preserved. Do not assign personal raw FULL to F04/F05/F06 or manufacture blanket FULL label.')
 o['source_path_binding_scope']='Exact raw file name in current fixedR trainer structure metadata; original view equivalence proof is qualified provider contribution, not a new field/source reread here.'

# CRE-B original four formal reads: correct nested identity status and continuous I/O, two requested overrides.
n='tasks/creature_b/reading-ledger.json'
for i in [6,8]:
 x=bind(n,'/initial/'+str(i));path=x['identity']['path'];check_identity(x['identity'],fixed[('formal',path)][0]);assert x['own_full_read'] is True
 override('formal',path,'EXISTING_ACTUAL_FULL_CONTINUOUS_FORMAL_TEXT_READ',['creature_b'],[entry(n,'/initial/'+str(i))],'Original /root/creature_b continuous source/formal text read, with nested identity.read_status and actual displays. Root CRE-B335manifest/current qualified reception remains separate; source whole reading never equals semantic/global PASS.')
assert len(overrides)==33 and len({(x['kind'],x['path'])for x in overrides})==33
assert sum(x['kind']=='reference'for x in overrides)==31

# Seventeen family catalogs: exact original actual whole-text reader, distinct from normative/identity extra tables.
catalog_defs=[('combat-requirements-wp39-40-41-42-45.md','tasks/core_atomic_reception/reading-ledger.json','/entries/5','com_core'),('combat-requirements-wp47-ab.md','tasks/com_move/reading-ledger.json','/primary_payloads/24','com_move'),('combat-requirements-wp49-51-52.md','tasks/com_ai/reading-ledger.json','/files/28','com_ai'),('combat-requirements-wp54-55-56-58.md','tasks/facility_atomic_completion_cloud/v2/reading-ledger.json','/original_inputs/28','com_facility'),('creature-rpg-wp18-20-24-25-26.md','tasks/creature_a_atomic_reception/reading-ledger.json','/own_full_reads/7','creature_a_and_c'),('creature-rpg-wp27-28-29-30-33.md','tasks/creature_b/reading-ledger.json','/initial/9','creature_b'),('creature-rpg-wp35-36-57-64-68.md','tasks/creature_a_atomic_reception/reading-ledger.json','/own_full_reads/91','creature_a_and_c'),('demo-dx-wp72-73-74-75-76-77.md','tasks/developer_full_cloud/reading-ledger.json','/inventory/32','developer_full_cloud'),('engine-overworld-wp11-15-59-60.md','tasks/world_full/reading-ledger.json','/entries/67','world_full'),('engine-overworld-wp16.md','tasks/world_full/receptions/resources-final-reading-ledger.json','/files/31','world_full'),('generic-kernel-wp02-03-04.md','tasks/kernel_atomic_reception/reading-ledger.json','/records/17','kernel'),('generic-kernel-wp05-06-07-08-09-10.md','tasks/kernel_atomic_reception/reading-ledger.json','/records/18','kernel'),('pokemon-rules-wp19-21-22-23-34.md','tasks/creature_a_atomic_reception/reading-ledger.json','/own_full_reads/8','creature_a_and_c'),('pokemon-rules-wp31-32-37-38.md','tasks/creature_a_atomic_reception/reading-ledger.json','/own_full_reads/90','creature_a_and_c'),('pokemon-rules-wp43-44-46-48-50.md','tasks/com_move/reading-ledger.json','/primary_payloads/25','com_move'),('pokemon-rules-wp53-60-61-62-69-70.md','tasks/facility_atomic_completion_cloud/v2/reading-ledger.json','/original_inputs/29','com_facility'),('user-interface-wp17-63-65-66-67-68-69-70-71.md','tasks/ui_full/reading-ledger.v3.json','/records/51','ui_full')]
catalogs=[]
for name,n,p,task in catalog_defs:
 path='deliverables/final-specification-set/test-catalog/'+name;f,fp=fixed[('formal',path)];x=bind(n,p);actualpath=x.get('path',x.get('payload',x.get('identity_path',x.get('identity',{}).get('path'))));assert actualpath==path,(n,p,actualpath,path)
 rootdoc=read(n);reader_fields=[]
 for location,record in [(p,x),('',rootdoc)]:
  for key in ['reader','reviewer','actual_reader']:
   if isinstance(record.get(key),str):reader_fields.append(field(n,location+'/'+key))
 assert reader_fields,(name,n,p)
 c={'id':'C'+str(len(catalogs)+1).zfill(2),'path':path,'fixed_B8':f['commit'],'fixed_identity':{k:f[k]for k in ['bytes','sha256','git_blob']},'fixed_identity_pointer':fp,'actual_original_text_reading':entry(n,p),'reader_fields_original':reader_fields,'current_root_receipt_task':task,'qualification':'Existing actual whole text reading is an original reader attribution only; normative/mapping/current finite interface acceptance is distinct. No new personal FULL or catalog semantic PASS from this pointer table.'}
 if name in ['engine-overworld-wp16.md','generic-kernel-wp05-06-07-08-09-10.md']:c['two_identity_layers']='Fixed B8 inventory identity and original actual FULL ledger are distinct layers; optional extra identity tables do not erase actual whole reading. Engine original actor remains world_resources_rendering, not parent world_full FULL transfer.'
 catalogs.append(c)
assert len(catalogs)==17

# Thin563 successor: all original detailed pointers remain hash-bound, no15MB regeneration.
om={(x['kind'],x['path']):x['id']for x in overrides};cm={x['path']:x['id']for x in catalogs};primary={}
for task in ['com_battler','com_ability_item','formal_shared']:
 n='delegation/readsets/'+task+'.json'
 def w(v,p=''):
  if isinstance(v,dict):
   for k,y in v.items():w(y,p+'/'+k)
  elif isinstance(v,list):
   for i,y in enumerate(v):w(y,p+'/'+str(i))
  elif isinstance(v,str):
   for kind in ['reference','formal']:
    if (kind,v)in fixed:primary.setdefault((kind,v),[]).append({'task':task,'readset_pointer':fref(n,p),'qualification':'Exact original readset member linked to existing current root task receipt; source reader stays original.'})
 w(read(n))
thin=[]
for i,row in enumerate(base['rows']):
 k=(row['kind'],row['path']);f,fp=fixed[k];assert f['sha256']==row['fixed_identity']['sha256'] and f['git_blob']==row['fixed_identity']['git_blob']
 original_tasks=sorted({t for c in row['candidate_groups']for t in c['root_receipt_tasks']if t in receipts})
 x={'i':i,'kind':k[0],'path':k[1],'fixed_commit':f['commit'],'bytes':f['bytes'],'sha256':f['sha256'],'blob':f['git_blob'],'original_index_row_pointer':'/rows/'+str(i),'original_root_receipt_pointer_candidates_preserved':original_tasks,'new_current_named_primary_receipt_links':primary.get(k,[]),'semantic_PASS':None,'personal_FULL_added':False}
 if k in om:x['exact_override_id']=om[k]
 if k[1]in cm:x['catalog_reader_id']=cm[k[1]]
 if 'resource_root_guard'in row:x['resource_scope']={'current_root_receipt_task':'resource_media_serialized','original_index_guard_pointer':'/rows/'+str(i)+'/resource_root_guard','qualification':'Existing required readable resource/program/data completeness only; named AVAILABLE_OPAQUE_NATIVE unreviewed machinecode/host remains. Never whole binary/machinecode FULL.'}
 if 'parent_requested_primary_qualification'in row:x['shared_formal_current_qualification']={'original_whole_text_reading':'../three-shared-formal-priority.json','current_root_receipt_task':'formal_shared','current_task_final_accepted_declared_by_root':True,'qualification':'Original451lines/6chunks/18groups preserved; original3OPEN interfaces and NOT_SIGNED snapshots are historical, current root29 acceptance separately bound. No UNREAD backfill or global PASS.'}
 thin.append(x)
assert len(thin)==563 and sum('resource_scope'in x for x in thin)==18

put('paths-563.json',{'schema':'gr8-thin-final-current-fixed-member-pointers/v1','scope':'MECHANICAL_SUCCESSOR_ONLY','original_index_identity':inputs[basepath],'original_index_frozen_current_root_receipts':23,'current_root_registry_identity':inputs[regpath],'current_root_task_receipts':len(receipts),'reference_commit':R,'formal_commit':B8,'overrides':'overrides-33.json','catalogs':'catalog-readers-17.json','root_receipts':'root-receipts-current.json','rows':thin,'new_contexts':0,'new_votes':0,'new_semantic_credit':0,'global_PASS_granted':False,'global_denominator_frozen':False,'UPDATE_NOT_STARTED':True})
put('overrides-33.json',{'schema':'gr8-exact-existing-33-reader-pointer-overrides/v1','qualification':'Correct existing qualified producer/actual reader/alias/field-view pointers only; not new source reading or template FULL. Old partial and generated PENDING states remain immutable.','rows':overrides})
put('catalog-readers-17.json',{'schema':'gr8-seventeen-original-catalog-text-readers/v1','rows':catalogs,'qualification':'Whole text reading and exact fixed B8 identity are separate from semantic acceptance of every vector/premise/consumer. Identity extra tables do not negate actual original reading.'})
put('root-receipts-current.json',{'schema':'gr8-current29-root-task-receipt-pointer-bindings/v1','registry_identity':inputs[regpath],'count':len(receipts),'receipts':receipts,'qualification':'These are existing root decisions, not new reviewer votes/source reading credit.'})
put('inputs.json',{'schema':'gr8-thin-successor-input-identities/v1','inputs':list(inputs.values()),'old_50_payloads_unchanged':True,'new_source_body_reads':0,'metadata_only':True})
put('unknown.json',{'schema':'gr8-thin-successor-exact-unmatched/v1','unknown':unknown,'qualification':'No inferred unknown→limit or task receipt→personal FULL. Complete trainer lossless view reading is explicitly not raw PBS full-file display. Source/consumer semantic sufficiency is retained solely within the already root-qualified scope.'})
put('pointer-bindings.json',{'schema':'gr8-thin-successor-metadata-pointer-checks/v1','bindings':pointer_checks,'qualification':'Canonical JSON hashes are pointer integrity checks only, not reading-credit or behavioral truth.'})
for n,d in cache.items():
 raw=(RR/n).read_bytes();assert len(raw)==inputs[n]['bytes'] and sha(raw)==inputs[n]['sha256'],('concurrent_input_change',n)
for x in original_manifest['files']:
 raw=(BASE/x['path']).read_bytes();assert len(raw)==x['bytes'] and sha(raw)==x['sha256']
validation={'schema':'gr8-thin-successor-mechanical-validation/v1','start_utc':START,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'fixed_unique_paths':563,'reference':432,'formal':131,'root_receipts_exact':29,'exact_overrides':33,'override_reference':31,'override_formal':2,'catalogs':17,'binary_readable_opaque_guards':18,'localization_collective_pairs_navigation':10697,'metadata_pointer_checks':len(pointer_checks),'unknown':len(unknown),'old50payloads_exact_unchanged':True,'all_563_no_source_FULL_or_semantic_PASS_added':all(x['semantic_PASS'] is None and not x['personal_FULL_added']for x in thin),'new_contexts':0,'new_votes':0,'new_source_reading_or_semantic_credit':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'actual_model_effort_tier_speed_Fast_UUID':'UNVERIFIED','global_semantic_denominators_frozen':False,'global_PASS_granted':False}
put('validation.json',validation)
report='''563路径机械后继薄表已绑定当前root29份exact收据；原冻结23索引及原50payload全部保持，未重建15MB索引、未再读全源或原记录语义。\n\npaths-563.json引用原index/hash/row，overrides-33.json给31R/2F真实原reader/原账指针及whole/alias/完整字段视图资格，catalog-readers-17.json给17catalog的原实际全文读者。metrics归PBSbackups的既有完整literal alias组，不归PBSWORLD；6trainer为FAC完整无损字段视图，不冒raw PBS逐行全文；TowerPokemon为FAC原884行完整raw。F04/F05/F06程序来源读者与这些raw/view读者分开。Gen8moves只精确同byte关联default原whole reader。18Text由原receiver433对与A/B/C/D具名10264对集体承接，不造某人个人18全文。ItemSprites实际157行，旧164资格不扩。CREB WP27/WP29保原连续I/O及嵌套身份状态。\n\nshared formal451行原root全文/18有限组保留；旧3OPEN/NOT_SIGNED为原时点，新root29的formal_shared收据单独接合，不回退UNREAD。ABI原2R4F与Battler10R原source个人资格保留，当前root相应task-final分别绑定；root-item不替代ABI整域。\n\nengine-wp16实际world_resources_rendering见resources-final-reading-ledger/files/31；kernel05–10见kernel reading-ledger/records/18。固定B8 identity和额外identity表是不同层，不造缺读或父个人FULL。18binary仍保原resource可读范围与AVAILABLE_OPAQUE_NATIVE边界。\n\n全部仅机械metadata/成员/身份/指针核对；0新增context/票/sourceFULL/语义信用，NOT_EXECUTED，UPDATE_NOT_STARTED，实际配置与UUID UNVERIFIED，不签全局或冻结全局语义分母。\n'''
(OUT/'report.md').write_text(report)
print(json.dumps(validation,ensure_ascii=False))
