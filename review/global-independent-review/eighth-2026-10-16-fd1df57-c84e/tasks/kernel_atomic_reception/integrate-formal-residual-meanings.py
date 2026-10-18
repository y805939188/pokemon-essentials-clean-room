"""Integrate explicitly hand-written residual meanings; never classify prose by regex alone."""
from pathlib import Path
import ast,csv,datetime,hashlib,json
BASE=Path(__file__).resolve().parent;RR=BASE.parent.parent
B=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(n):return json.loads((BASE/n).read_text())
def write(n,d):(BASE/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
paths={
 'WP02':'generic-kernel/wp02-rule-configuration-and-data-variants.md','WP03':'generic-kernel/wp03-content-identity-and-schema.md','WP04':'generic-kernel/wp04-pbs-lifecycle.md','WP05':'generic-kernel/wp05-events-extensions-plugins.md','STATS':'generic-kernel/wp06-stats-directory.md','TIME':'generic-kernel/wp06-time-random-steps-stats.md','DP':'generic-kernel/wp07-deprecation-appendix.md','IO':'generic-kernel/wp07-diagnostics-files-http.md','LZ':'generic-kernel/wp08-localization.md','SAVE':'generic-kernel/wp09-save-startup-continue.md','MIG':'generic-kernel/wp10-migration-failure-recovery.md'}
paths={k:'deliverables/final-specification-set/'+v for k,v in paths.items()}
rows=list(csv.DictReader((BASE/'formal-residual-meanings.manual.tsv').open(),delimiter='\t'))
tree=ast.parse((BASE/'integrate-catalog020304.py').read_text())
sources=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='sources' for t in n.targets))
sources.update({'facility_lists':'PBS/battle_facility_lists.txt','plugin':'Data/Scripts/001_Technical/005_PluginManager.rb','dungeon':'Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb'})
sources.update({'berryData':'Data/Scripts/010_Data/002_PBS data/007_BerryPlant.rb','growth':'Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb','gender':'Data/Scripts/010_Data/001_Hardcoded data/002_GenderRatio.rb','eggGroup':'Data/Scripts/010_Data/001_Hardcoded data/003_EggGroup.rb','evolution':'Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb','status':'Data/Scripts/010_Data/001_Hardcoded data/010_Status.rb','weather':'Data/Scripts/010_Data/001_Hardcoded data/012_Weather.rb','encounterType':'Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb','environment':'Data/Scripts/010_Data/001_Hardcoded data/014_Environment.rb','battleWeather':'Data/Scripts/010_Data/001_Hardcoded data/015_BattleWeather.rb','battleTerrain':'Data/Scripts/010_Data/001_Hardcoded data/016_BattleTerrain.rb','target':'Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb'})
sources.update({'events':'Data/Scripts/003_Game processing/005_Event_Handlers.rb','collections':'Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb','stats':'Data/Scripts/004_Game classes/012_Game_Stats.rb','system':'Data/Scripts/004_Game classes/002_Game_System.rb','registrations':'Data/Scripts/002_Save data/004_Game_SaveValues.rb','deprecation':'Data/Scripts/001_Technical/001_Debugging/005_Deprecation.rb','console':'Data/Scripts/001_Technical/001_Debugging/002_DebugConsole.rb','validation':'Data/Scripts/001_Technical/001_Debugging/004_Validation.rb','pokedex':'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb'})
sources.update({'clock':'Data/Scripts/012_Overworld/003_Overworld_Time.rb','lottery':'Data/Scripts/017_Minigames/005_Minigame_Lottery.rb','fishing':'Data/Scripts/012_Overworld/005_Overworld_Fishing.rb','contest':'Data/Scripts/018_Alternate battle modes/002_BugContest.rb','sprite':'Data/Scripts/001_Technical/006_RPG_Sprite.rb','ruby':'Data/Scripts/001_Technical/002_RubyUtilities.rb','recorded':'Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb'})
sources.update({'files':'Data/Scripts/001_Technical/002_Files/001_FileTests.rb','filemixins':'Data/Scripts/001_Technical/002_Files/002_FileMixins.rb','http':'Data/Scripts/001_Technical/002_Files/003_HTTP_Utilities.rb','errors':'Data/Scripts/001_Technical/001_Debugging/003_Errors.rb','pbd':'Data/Scripts/001_Technical/001_Debugging/001_PBDebug.rb'})
ledger=read('reading-ledger.json')
px=next((x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==sources['pokedex']),None)
if not px:px={'repo':'R','path':sources['pokedex'],'status':'PARTIAL_READ_COMPLETE_NAMED_UNITS','reader':'/root/kernel_atomic_reception','whole_file_read':False};ledger['records'].append(px)
if px['status']!='FULL_READ':
 px['actual_read_ranges']=sorted(set(tuple(x) for x in px.get('actual_read_ranges',[]))|{(1,35),(110,207),(345,len((R/sources['pokedex']).read_text().splitlines()))})
 px['complete_units']=sorted(set(px.get('complete_units',[])+['initialize/clear complete15–35; refresh_accessible_dexes implementation not read','owned?164–169/owned_shadow_pokemon?173–178/owned_count183–186 complete','count_species351–359 complete, defaultnationalbranch enumeratesregisteredbaseSpecies andtruthy ownedHash values','register starts195 but tailcut207, no complete registration credit']))
 px.setdefault('later_read_evidence',[]).extend(['io/stats-derived-caught-complete-pokedex-owned-count.json','io/stats-derived-caught-complete-count-species-and-initializer.json','directtool f61117 complete110–165 output'])
debug_partial=next(x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==sources['debug'])
assert debug_partial['status']!='FULL_READ'
debug_partial['actual_read_ranges']=sorted(set(tuple(x) for x in debug_partial.get('actual_read_ranges',[]))|{(1328,1496)})
debug_partial['complete_units']=sorted(set(debug_partial.get('complete_units',[])+['complete files_menu/compile_data/create_pbs_files/rename_files/extract_text/compile_text/mystery_gift/reload_system_cache registrations1328–EOF1496']))
debug_partial.setdefault('later_read_evidence',[]).extend(['io/wp04-debug-complete-compile-and-writers-handlers.json','io/wp04-debug-complete-pbs-compile-export-handlers.json'])
if not any(x.get('repo')=='R' and x.get('path')==sources['facility_lists'] for x in ledger['records']):ledger['records'].append({'repo':'R','path':sources['facility_lists'],'status':'FULL_READ','reader':'/root/kernel_atomic_reception','range':[1,25],'reading_evidence':['io/wp02-complete-facility-list-five-records.json'],'scope':'All5 complete records/allfields read. Referenced10 innerfiles not semantically received by filename existence.'})
ledger['updated_utc']=NOW;write('reading-ledger.json',ledger)
groups={
 'compiler':['c1','c2','c3','c4'],
 'fixed_catalogs':'growth gender eggGroup shape color habitat evolution stat nature status terrain weather encounterType environment battleWeather battleTerrain target'.split(),
 'author_classes':'town type ability move item berryData species metrics shadow ribbon enc trainerType trainerData meta playerMeta mapMeta tiles params phoneData'.split(),
 'formal_scope':[], 'creator_consumer':[], 'consumer_inventory':[], 'material_inventory':[], 'search_backup':[], 'search_seed':[], 'ui_contribution':[], 'media_contribution':[], 'catalog_first':[], 'catalog_second':[]
}
finite_refs={
 'creator_consumer':['received/creature-a-kernel-consumer-reception.json','received/core-kernel-reception.json','received/ui-complete-finite-reception.json'],
 'ui_contribution':['received/ui-complete-finite-reception.json','received/ui-correction-dex-reception.json'],
 'consumer_inventory':['consumer-candidate-dispositions.json'],
 'catalog_first':['catalog020304-manual-atoms.json'],
 'catalog_second':['catalog050607080910-manual-atoms.json'],
 'material_inventory':['input-identities.json'],
 'search_backup':['wp02-residual-static-presence-proof.v1.json']
}
finite_refs['search_seed']=['time-actual-consumer-reading-addendum.v1.json']
finite_refs['media_contribution']=['received/media-messages-finite-reception.json','received/media-serialized-encoding-87f3db06-reception.json']
lib=json.loads((RR/'tasks/coverage_acceptance_incremental/dispatch/kernel_atomic_reception.readset.json').read_text())['all_fixed_R432_F131_identity_library']
# Current input identities/presence for literal material statements only: no body-reading credit.
material=[]
for x in lib:
 if x['repo']=='R' and (x['path'].startswith('PBS/Gen ') or x['path'].startswith('PBS/Shadow Pokémon backup/')):
  p=R/x['path'];material.append({'fixed':x,'current_exists':p.is_file(),'body_read_credit':'NONE_FROM_PRESENCE_OR_IDENTITY'})
faclist=(R/sources['facility_lists']).read_text().splitlines();facnames=[line.split('=',1)[1].strip() for line in faclist if line.startswith(('Trainers =','Pokemon ='))]
assert len(facnames)==10 and len(set(facnames))==10
for name in facnames:assert (R/'PBS'/name).is_file()
write('wp02-residual-static-presence-proof.v1.json',{'captured_utc':NOW,'actual_read_FacilityList':'io/wp02-complete-facility-list-five-records.json','all5_records_full_read':True,'exact10_referenced_paths':facnames,'all10_current_files_exist':True,'inner_file_body_read_credit':'NONE_FROM_EXISTENCE','material_paths':material,'backup_bounded_search':{'actual_tool_output':'aa4fee','query':'rg -n -i backup Data/Scripts','exit':0,'matches':['Data/Scripts/002_Save data/003_SaveData_Conversion.rb:192','Data/Scripts/016_UI/013_UI_Load.rb:232','Data/Scripts/002_Save data/001_SaveData.rb:63'],'scope':'Only searched forms; all3 save-related, no universal no-dynamic-reference claim.','direct_command_start_end_utc':'UNVERIFIED_NOT_CAPTURED'},'plugin_fixed_library_paths':['Data/Scripts/001_Technical/005_PluginManager.rb'],'manual47_threshold_proof':'wp02-manual-47-threshold-group-proof.v1.json','business':'NOT_EXECUTED'})
identities={}
for row in rows:
 for token in row['source_units'].split():
  for key in groups.get(token,[token]):
   if key in identities:continue
   path=sources[key];fixed=next(x for x in lib if x['repo']=='R' and x['path']==path);raw=(R/path).read_bytes();assert len(raw)==fixed['bytes'] and hashlib.sha256(raw).hexdigest()==fixed['sha256']
   actual=next(x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==path)
   identities[key]={'fixed':fixed,'raw_bytes_sha_equal':True,'actual_reader':'/root/kernel_atomic_reception','actual_reading':actual,'credit':'Exact personally read definition and manually stated conditional fact only; no wholeblob semantic acceptance.'}
records=[]
for row in rows:
 key=row['file_key'];path=paths[key];line=int(row['line']);formal=(B/path).read_text().splitlines()[line-1]
 actualsources=[];receipts=[]
 for token in row['source_units'].split():
  actualsources.extend(groups.get(token,[token]))
  for ref in finite_refs.get(token,[]):
   raw=(BASE/ref).read_bytes();receipts.append({'path':ref,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'credit':'Previously actually read complete finite named payload or explicit current audit inventory; each has own exact qualification, not all-domain acceptance.'})
 for n,assertion in enumerate(row['manual_subassertions'].split('||'),1):records.append({'id':'KAR-RESIDUAL-'+key+'-'+row['id']+'-S%02d'%n,'formal':{'path':path,'lines':[line],'exact_text':formal},'assertion':assertion,'source_identity_refs':sorted(set(actualsources)),'specific_contribution_refs':receipts,'source_status':row['status'],'reception_status':row['status'],'premise':'Exact complete formal sentence, personally reconstructed child meaning and finite boundary retained; scope/policy/navigation facts are not runtime claims.','normal_failure_cancel_partial':row['boundary'],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED','count_status':'WORKING_CHILD_REFINEMENT_NOT_FROZEN_UNIQUE_DENOMINATOR','original_fact_refs':[]})
assert len({x['id'] for x in records})==len(records)
write('formal-residual-meanings.json',{'schema':'kernel-personally-reconstructed-residual-meanings/v1','utc':NOW,'rows':len(rows),'working_children':len(records),'source_identities':identities,'records':records,'remaining':'All scope/default/qualifications remain their actual purposes; no full-domain acceptance from identifiers or layout.'})
main=read('manual-atomic-clauses.json');main['records']=[x for x in main['records'] if not x['id'].startswith('KAR-RESIDUAL-')]+records;write('manual-atomic-clauses.json',main)
old=read('old-locator-disposition.json')
for item in old['records']:
 children=[x for x in records if x['formal']['path']==item['path'] and item['range'][0]<=x['formal']['lines'][0]<=item['range'][1]]
 if children:item.update(manual_child_assertions=sorted(set(item.get('manual_child_assertions',[])+[x['id'] for x in children])),disposition='EXPLICIT_MANUAL_MEANINGS_WITH_PER_CHILD_BOUNDED_STATUS',semantic_acceptance='Only complete personally expressed meanings/premises and exact purpose; not inherited sourcefact links/PASS or generic OPEN.',pending='Final denominator reconciliation and exact named boundary per child.')
 # Only these personally inspected residual layout outputs are disposed here.
 elif item['path'] in [paths['WP02'],paths['WP03'],paths['WP04'],paths['WP05'],paths['STATS'],paths['DP'],paths['TIME'],paths['IO'],paths['LZ']] and not(item.get('manual_child_assertions') or item.get('explicit_manual_child_ids')):
  exact=(B/item['path']).read_text().splitlines()[item['range'][0]-1]
  column_words=['设置','事实','候选材料','组合','身份类','类/操作','情形','内容与省略字段','省略字段','模式','字段种类','内容','合法独立输入及查询','入口','校验','独立作者输入','维度','位置','类（身份类）','触发条件','异常类别/阶段','合法材料中的单行','边','层次','类别（含省略）','写出时状态','入口与已登记状态','已预载内容','阶段','交界','原语','失败/边界','字段','输入','来源','消费者','独立输入／观察点','首参/次参','参数种子 A','条件','操作','输入/操作','层','输入与入口（各例独立）','分支','模式/入口','入口形态','指定消费者','入口与原文','默认输入（彼此独立）','桶前提与选择','已有译文／对照','有序输入（均为合法24号节）','步骤']
  if exact.startswith('|') and (set(exact.replace('|','').strip())<=set('- :') or exact.split('|')[1].strip() in column_words):item.update(disposition='TABLE_LAYOUT_COLUMNS_OR_SEPARATOR_ACTUALLY_READ',purpose='Exact column vocabulary/separator only; substantive data rows have their own named children.',semantic_acceptance='NO_NEIGHBOR_APPROVAL',pending='No standalone runtime behavior in these column labels.')
  elif exact.startswith('**') or exact.startswith('#'):item.update(disposition='LAYOUT_HEADING_EXACT_BODY_PURPOSE',purpose='Actually inspected category/section heading; any named counts are joined to explicit individually reconstructed declarations/body facts.',semantic_acceptance='NAVIGATION_OR_CATEGORY_ONLY',pending='No extra runtime branch asserted by heading.')
  else:raise AssertionError(('WP02 unresolved meaning',item['old_locator_id'],exact))
write('old-locator-disposition.json',old)
progress=read('progress.json');progress.update(updated_utc=NOW,explicit_manual_atom_subset=len(main['records']),residual_manual_children=len(records),old_locators_with_explicit_partial_child_binding=sum(bool(x.get('manual_child_assertions') or x.get('explicit_manual_child_ids')) for x in old['records']),own_PBS_full_read_paths=[x['path'] for x in ledger['records'] if x.get('repo')=='R' and x.get('status')=='FULL_READ' and x['path'].startswith('PBS/')]);write('progress.json',progress)
print(json.dumps({'utc':NOW,'rows':len(rows),'residual_children':len(records),'working_total':len(main['records']),'old_named':progress['old_locators_with_explicit_partial_child_binding'],'ownPBSfull':len(progress['own_PBS_full_read_paths'])}))
