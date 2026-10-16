"""Bind hand-authored case meanings; identity/navigation never grants a case PASS."""
from pathlib import Path
import csv,datetime,hashlib,json
BASE=Path(__file__).resolve().parent
B=Path('/workspace/pokemon-essentials-clean-room'); R=Path('/workspace/pokemon-essentials')
RR=BASE.parent.parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F='deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md'
lines=(B/F).read_text().splitlines()
def read(n):return json.loads((BASE/n).read_text())
def write(n,obj):(BASE/n).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
rows=list(csv.DictReader((BASE/'catalog020304-manual-cases.tsv').open(),delimiter='\t'))
assert len(rows)==181 and len({x['id'] for x in rows})==181
case_lines={line.split('|')[1].strip():i for i,line in enumerate(lines,1) if line.startswith('| ')}
ledger=read('reading-ledger.json')
partials=[
 ('PBS/pokemon.txt',[[1,29]],['complete BULBASAUR record1–29 only; other actual PBS records not read by this partial'],['io/catalog-kc06-complete-debug-extraction-handler-and-bulbasaur-record.json']),
 ('Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb',[[1,344],[926,1225],[1200,1285]],['pbEncountersEditor6–129','pbEncounterMapVersionEditor133–252','pbEncounterTypeEditor256–340','pbPokemonEditor926–987','pbRegionalDexEditor992–1097','pbRegionalDexEditorMain1099–1202','pbAppendEvoToFamilyArray1204–1216','pbGetEvoFamilies1218–1229','pbEvoFamiliesToStrings1231–1246; pbAnimationsOrganiser tail is PARTIAL'],['io/catalog-encounter-editor-complete-outer-unit-first.json','io/catalog-encounter-type-editor-complete-unit.json','io/catalog-regional-family-complete-tail-definitions.json','io/catalog-regional-editor-main-complete-tail.json']),
 ('Data/Scripts/020_Debug/002_Editor_DataTypes.rb',[[1340,1570],[1624,1706]],['EvolutionsProperty complete1340–1570','pbPropertyList complete1624–1706'],['io/catalog-evolutions-property-complete-class.json']),
 ('Data/Scripts/014_Pokemon/001_Pokemon.rb',[[490,542],[965,1054]],['nature497–503, nature_id505–507, nature=511–515, nature_for_stats520–523, nature_for_stats_id525–527, nature_for_stats=531–535 complete','check_evolution_on_level_up976–981/use_item986–991/trade996–1001/after_battle1005–1010/by_event1015–1020/action_after_evolution1026–1030/check_evolution_internal1035–1045 complete; trigger_event_evolution tail PARTIAL'],['io/catalog-nature-current-pid-complete-getters.json','io/catalog-evolution-first-eligible-complete-methods.json']),
 ('Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb',[[247,270]],['complete hatch_eggs event registration252–269'],['io/catalog-nature-current-pid-complete-getters.json']),
 ('Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb',[[50,72],[675,714],[746,790]],['pbCheckHiddenMoveBadge56–64 and direct Surf/startSurf complete within675–714; SURF CanUseMove/UseMove registrations754–788 complete'],['io/catalog-kc03-badge-helper-and-surf-complete-consumers.json']),
 ('Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb',[[1,47]],['shadow_data32–34/max_gauge_size36–39 complete; later change_heart_gauge PARTIAL'],['io/catalog-schema-shadow-maxgauge-complete-getters.json']),
 ('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',[[1423,1460]],['complete extract_text registration1423–1455; following compilehandlerPARTIAL'],['io/catalog-kc06-complete-debug-extraction-handler-and-bulbasaur-record.json'])
]
for path,ranges,units,ios in partials:
 found=next((x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==path),None)
 if not found:found={'repo':'R','path':path,'status':'PARTIAL_READ_COMPLETE_NAMED_UNITS','reader':'/root/kernel_atomic_reception','whole_file_read':False};ledger['records'].append(found)
 if found.get('status')!='FULL_READ':
  found['actual_read_ranges']=sorted(set(tuple(x) for x in found.get('actual_read_ranges',[]))|set(tuple(x) for x in ranges))
  found['complete_units']=sorted(set(found.get('complete_units',[])+units)); found['later_read_evidence']=sorted(set(found.get('later_read_evidence',[])+ios))
ledger['updated_utc']=NOW;write('reading-ledger.json',ledger)
sources={
 'settings':'Data/Scripts/001_Settings.rb','battleSettings':'Data/Scripts/002_BattleSettings.rb','c1':'Data/Scripts/021_Compiler/001_Compiler.rb','c2':'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb','c3':'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb','c4':'Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb',
 'generic':'Data/Scripts/010_Data/001_GameData.rb','enc':'Data/Scripts/010_Data/002_PBS data/013_Encounter.rb','terrain':'Data/Scripts/010_Data/001_Hardcoded data/011_TerrainTag.rb','nature':'Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb','stat':'Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb','meta':'Data/Scripts/010_Data/002_PBS data/016_Metadata.rb','playerMeta':'Data/Scripts/010_Data/002_PBS data/017_PlayerMetadata.rb','mapMeta':'Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb','metrics':'Data/Scripts/010_Data/002_PBS data/010_SpeciesMetrics.rb','shadow':'Data/Scripts/010_Data/002_PBS data/011_ShadowPokemon.rb','phoneData':'Data/Scripts/010_Data/002_PBS data/021_PhoneMessage.rb','trainerData':'Data/Scripts/010_Data/002_PBS data/015_Trainer.rb','trainerType':'Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb','species':'Data/Scripts/010_Data/002_PBS data/008_Species.rb','speciesFiles':'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb','type':'Data/Scripts/010_Data/002_PBS data/003_Type.rb','move':'Data/Scripts/010_Data/002_PBS data/005_Move.rb','item':'Data/Scripts/010_Data/002_PBS data/006_Item.rb','ability':'Data/Scripts/010_Data/002_PBS data/004_Ability.rb','ribbon':'Data/Scripts/010_Data/002_PBS data/012_Ribbon.rb','town':'Data/Scripts/010_Data/002_PBS data/002_TownMap.rb','tiles':'Data/Scripts/010_Data/002_PBS data/019_DungeonTileset.rb','params':'Data/Scripts/010_Data/002_PBS data/020_DungeonParameters.rb','shape':'Data/Scripts/010_Data/001_Hardcoded data/004_BodyShape.rb','color':'Data/Scripts/010_Data/001_Hardcoded data/005_BodyColor.rb','habitat':'Data/Scripts/010_Data/001_Hardcoded data/006_Habitat.rb',
 'intl':'Data/Scripts/001_Technical/003_Intl_Messages.rb','phone':'Data/Scripts/013_Items/004_Item_Phone.rb','pokemon':'Data/Scripts/014_Pokemon/001_Pokemon.rb','shadowConsumer':'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb','egg':'Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb','load':'Data/Scripts/016_UI/013_UI_Load.rb','start':'Data/Scripts/003_Game processing/001_StartGame.rb','main':'Data/Scripts/999_Main/999_Main.rb','field':'Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb','debug':'Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb','editor':'Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb','props':'Data/Scripts/020_Debug/002_Editor_DataTypes.rb','position':'Data/Scripts/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb','misc':'Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb','temp':'Data/Scripts/004_Game classes/001_Switches and Variables/001_Game_Temp.rb','factory':'Data/Scripts/004_Game classes/005_Game_MapFactory.rb','player':'Data/Scripts/015_Trainers and player/004_Player.rb','bulba':'PBS/pokemon.txt','dungeon':'Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb'
}
bindings={}
def assign(ids,keys):
 for ident in ids.split():bindings[ident]=keys.split()
assign('KC01 KC02','settings battleSettings')
assign('KC03','settings field');assign('KC04','c1 c2');assign('KC05','settings start load');assign('KC06','debug load intl')
for n in [1,2]:assign('KR%02d'%n,'enc generic')
assign('KR03','terrain generic item');assign('KR04','meta playerMeta');assign('KR05','metrics');assign('KR06','trainerData phoneData c2');assign('KR07 KR16','generic c1 c2 item');assign('KR08','c2 trainerData');assign('KR09 KR10','c1 c2');assign('KR11','c1');assign('KR12','shadow');assign('KR13','nature pokemon');assign('KR14','c2 phoneData phone intl');assign('KR15','c2 phoneData')
for n in range(1,51):bindings['KL%02d'%n]=['c1','c2','c3','generic']
for n,keys in {1:'main c1',2:'c1',3:'c1',4:'c1',5:'c1 c3',7:'item c1',8:'item c1',9:'item c1',10:'c1',18:'c3 c4',22:'editor enc c2 c3',23:'metrics position c3',24:'metrics c3',25:'metrics c3',26:'metrics c3',27:'species speciesFiles editor props',28:'species speciesFiles editor props c3',29:'speciesFiles c3 editor',30:'enc c2',31:'enc c2',32:'enc c2',33:'species c1 c2',34:'species c1',35:'speciesFiles c1 c2 c3',36:'c1 c2 item phoneData',37:'c1 c2 move',38:'c1 c2 c4',39:'c1 c2 c4 intl',40:'misc temp c2 c3',41:'misc temp',42:'editor misc temp c3',43:'temp misc c2',44:'factory c2',45:'c2',46:'c1 c2 type',47:'c1 c2 type',48:'c1 c2 type',49:'c1 c2 type',50:'c2 trainerData'}.items():bindings['KL%02d'%n]=keys.split()
for row in rows:
 ident=row['id']
 if ident.startswith('U01-M01-'):
  group=int(ident.split('-')[2]);bindings[ident]={1:'species c1 c2',4:'stat species c1 c2 trainerData bulba',21:'params tiles',22:'tiles c1 c2',23:'phoneData c1 c2 c3',24:'shape color habitat species c1 c2',25:'species c2 pokemon',26:'species c2',27:'c2 c3 factory',28:'c1 c2 misc',29:'c1 c2 trainerData',30:'item c3',31:'species editor'}[group].split()
 elif ident.startswith('C01F-'):
  group=int(ident.split('-')[1]);bindings[ident]={10:'c1 c2 item',11:'c1 c2 item trainerType trainerData move',12:'c1 c2 meta playerMeta trainerData',13:'c2 move',15:'c2 meta playerMeta',16:'ability ribbon meta player item mapMeta town trainerType move intl',17:'species speciesFiles c2 c3',18:'enc c2 c3'}[group].split()
 elif ident.startswith('R6-U14-'):bindings[ident]=('c1 c2 ability egg player' if 'FLAGS' in ident else 'c1 c2 metrics species' if '-C06-' in ident else 'c1 c2 item move type intl').split()
 elif ident.startswith('GR7-M01-001-'):bindings[ident]='generic town meta playerMeta mapMeta tiles terrain item'.split()
 elif ident.startswith('J01-'):bindings[ident]='c1 c2 generic params metrics shadow species tiles position c3 shadowConsumer'.split()
 elif ident.startswith('R1-J01-'):bindings[ident]='shadow shadowConsumer c1 c2'.split()
assert set(bindings)=={x['id'] for x in rows}
bindings['U01-M01-021-01']+=['dungeon','mapMeta']

lib=json.loads((RR/'tasks/coverage_acceptance_incremental/dispatch/kernel_atomic_reception.readset.json').read_text())['all_fixed_R432_F131_identity_library']
identities={}
for key,path in sources.items():
 fixed=next(x for x in lib if x['repo']=='R' and x['path']==path);raw=(R/path).read_bytes();assert len(raw)==fixed['bytes'] and hashlib.sha256(raw).hexdigest()==fixed['sha256']
 current=next((x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==path),None)
 assert current is not None, ('Missing actual reading ledger, identity alone is not reading',path)
 identities[key]={'fixed':fixed,'raw_bytes_sha_equal':True,'actual_reader':'/root/kernel_atomic_reception','whole_file_actually_read':bool(current and current.get('status')=='FULL_READ'),'complete_named_unit_credit':current if current and current.get('status')!='FULL_READ' else 'Explicit row unit label; full source personally read, not automatic row or whole-domain acceptance.'}
records=[]
for row in rows:
 line=case_lines[row['id']]
 for number,assertion in enumerate(row['manual_subassertions'].split('||'),1):
  status='LOCALLY_RECONSTRUCTED_FINITE_SOURCE_VECTOR'
  if row['id']=='U01-M01-024-03':status='COMPLETE_FINITE_NAMED_UI_CONSUMER_PLUS_OWN_DEFINITIONS'
  if row['id']=='U01-M01-021-01':status='LOCAL_COMPLETE_QUERY_AND_ACTUAL_MAP_SETUP_RECEIVER_FINITE_FAILURE'
  records.append({'id':'KAR-CAT020304-'+row['id']+'-S%02d'%number,'case_id':row['id'],'formal':{'path':F,'lines':[line],'exact_text':lines[line-1]},'assertion':assertion,'manual_source_unit_label':row['source_units'],'source_complete_units':[{'path':sources[k],'identity_ref':k,'actual_credit':identities[k]['complete_named_unit_credit'],'whole_file_actually_read':identities[k]['whole_file_actually_read']} for k in bindings[row['id']]],'source_status':status,'reception_status':status,'premise':'All complete formal row input qualifiers preserved verbatim above; common static/unmodified/normal preceding dependencies and per-row failure boundary below. Case subinputs independent unless explicitly continuous.','normal_failure_cancel_partial':row['failure_and_scope'],'original_fact_refs':[],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED','update_started':False,'count_status':'WORKING_REFINEMENT_OR_CONTROL_NOT_FROZEN_UNIQUE_ATOM_DENOMINATOR'})
common={
 3:['All case expectations are static derived vectors rather than engine executions.','Catalog points to actual WP02/WP03/WP04 behavioral owners; links are navigation, not acceptance of their whole scope.'],
 94:['Actual assets/native/host prerequisites need their own validation before executed-test claims.'],
 95:['A conflict requires primary behavioral specification revision and a recorded issue; catalog alone must not silently override its owner.'],
 99:['All author-input cases use fixed inputs/legal dependencies/no overrides/normal preceding steps.','Reference game, independent behavior model, file I/O, native host and Demo were not executed for these declared vectors.','Subcases reset independently except where continuous observation explicitly stated.'],
 183:['R6 finite records use unique legal new identities and no schema/query override.','Other fields/references/terminal dependencies normal.','Observe raw registration or direct query; name examples exclude language hits or inspect raw fields.','No full-table disk/UI/native success follows.','WP27/WP43/WP73-B are named consumer navigation, not inherited domain approval.'],
 202:['R7 equality/schema/register/query extensions fixed and subinputs reset independently.','Inputs readable and preceding attributes/dependencies normal.','Save-can-reach additionally requires final checks and I/O; registration alone does not prove save.','Engine-overworld R7 pointer is consumer navigation; exact necessary generator reception remains explicit.'],
 223:['Earlier KR03–08/KR12/KR14–16/KL02–06/KL15–16/KL23–26/KL36–39 and R6 metrics controls remain required regressions with their complete original premises.','New vectors do not certify cache refresh.','No byte-identical roundtrip/default Shadow/general game failure/host or Demo reachability granted.'],
 227:['R1 source vector is NOT_EXECUTED, fixed schema/register/query/consumer, Species RATTATA registered and optional Shadow input explicitly enabled.','Query form0 with RATTATA_0 absent.','First three examples have exactly one legal base RATTATA section and omit remaining fields.','Fourth case is explicit current no-hit state, not inferred from optional input absence.','Exact prior GR7-J01 canonical qualification is historical navigation, not re-executed or fully reaccepted by current example.'],
 236:['Four r1 normal value-source queries have no own UI cancel/save/partial commit.','Earlier J01-V12 editor and V13 direct/startup failure prefixes remain separately effective.','Output4000 cannot distinguish present record from no record.','Output4000 cannot distinguish omitted from explicit field.','Correct Shadow field-default rule remains; no new compatibility policy.']}
for line,assertions in common.items():
 for n,assertion in enumerate(assertions,1):records.append({'id':'KAR-CAT020304-COMMON-L%03d-S%02d'%(line,n),'formal':{'path':F,'lines':[line],'exact_text':lines[line-1]},'assertion':assertion,'source_status':'CATALOG_QUALIFICATION_SCOPE_AND_CROSS_REFERENCE_PERSONALLY_READ','reception_status':'FINITE_QUALIFICATION_RECONCILED_WITH_ALL181_MANUAL_CASES','premise':'Exact text and all per-case qualifiers remain effective; historical/consumer links are not unreceived sourceFULL or global approval.','normal_failure_cancel_partial':'This statement qualifies the particular vectors, not a new runtime action; each actual branch/prefix stays in the named child records.','original_fact_refs':[],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED','count_status':'WORKING_SHARED_PREMISE_NOT_FROZEN_UNIQUE_ATOM_DENOMINATOR'})
out={'schema':'kernel-first-catalog-hand-derived-meanings-v1','utc':NOW,'case_count':181,'case_children':596,'working_child_count':len(records),'case_tsv_sha256':hashlib.sha256((BASE/'catalog020304-manual-cases.tsv').read_bytes()).hexdigest(),'source_identities':identities,'records':records,'remaining':'All181 case rows and shared scope qualifiers have manual meanings; composite and repeated controls still require final unique denominator reconciliation. Exact histories/native and U01-021 generator necessary entry kept explicit, not generic all-row OPEN or global PASS.'}
write('catalog020304-manual-atoms.json',out)
main=read('manual-atomic-clauses.json');main['records']=[x for x in main['records'] if not x['id'].startswith('KAR-CAT020304-')]+records;write('manual-atomic-clauses.json',main)
old=read('old-locator-disposition.json')
for item in old['records']:
 if item['path']!=F:continue
 children=[x for x in records if item['range'][0]<=x['formal']['lines'][0]<=item['range'][1]]
 if children:
  item['manual_child_assertions']=sorted(set(item.get('manual_child_assertions',[])+[x['id'] for x in children]));item['disposition']='EXPLICIT_MANUAL_MEANINGS_WITH_PER_CHILD_BOUNDED_STATUS';item['semantic_acceptance']='Actual complete conditional static vectors, reader/source identity retained per child; no inherited oldPASS, native or whole-case universal approval.';item['pending']='Final unique child denominator reconciliation and exact per-child explicit remaining boundaries; all whole-case qualifiers preserved, not generic OPEN.'
 elif lines[item['range'][0]-1].startswith('|'):
  item.update(disposition='TABLE_LAYOUT_COLUMN_OR_SEPARATOR_NO_RUNTIME_ASSERTION',purpose='Actually read ID/input-premise/expected columns or separator; no implicit approval of neighboring data rows.',semantic_acceptance='LAYOUT_ONLY',pending='No standalone semantic runtime branch in these table labels.')
 elif lines[item['range'][0]-1].startswith('#'):
  item.update(disposition='LAYOUT_HEADING_EXACT_BODY_JOIN',purpose='Actual heading names the case group. KC6/KR16/KL50, R6/R7/r1 content individually read and bound above; heading itself adds no independent runtime behavior.',semantic_acceptance='Navigation/count naming only, body child statuses control.',pending='No standalone unexamined rule inferred from heading.')
write('old-locator-disposition.json',old)
progress=read('progress.json');progress.update(updated_utc=NOW,catalog020304_cases_manual=181,catalog020304_working_children=len(records),explicit_manual_atom_subset=len(main['records']),old_locators_with_explicit_partial_child_binding=sum(bool(x.get('manual_child_assertions') or x.get('explicit_manual_child_ids')) for x in old['records']));write('progress.json',progress)
print(json.dumps({'utc':NOW,'cases':181,'new_children':len(records),'working_total':len(main['records']),'old_named':progress['old_locators_with_explicit_partial_child_binding']}))
