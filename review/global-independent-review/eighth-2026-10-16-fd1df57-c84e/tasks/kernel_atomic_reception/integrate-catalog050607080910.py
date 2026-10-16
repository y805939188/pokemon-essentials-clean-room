"""Bind 206 manually reconstructed cases with explicit source and reception boundaries."""
from pathlib import Path
import ast,csv,datetime,hashlib,json
BASE=Path(__file__).resolve().parent; RR=BASE.parent.parent
R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F='deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md';text=(B/F).read_text().splitlines()
def read(n):return json.loads((BASE/n).read_text())
def write(n,obj):(BASE/n).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
rows=list(csv.DictReader((BASE/'catalog050607080910-manual-cases.tsv').open(),delimiter='\t'))
assert len(rows)==206 and len({x['id'] for x in rows})==206
case_lines={line.split('|')[1].strip():i for i,line in enumerate(text,1) if line.startswith('| ')}
assert all(x['id'] in case_lines for x in rows)
ledger=read('reading-ledger.json')
for path,ranges,units,ios in [
 ('Data/Scripts/016_UI/007_UI_Bag.rb',[[1,580]],['Window_PokemonBag completeclass4–127','PokemonBag_Scene completeclass133–453, especially full pbStartScene145–224 and pbChooseItem351–452','PokemonBagScreen initialize459–462/pbStartScreen464–580 complete; later choosing/storage methods not read'],['io/catalog-bag-complete-start-and-navigation-definitions.json','io/catalog-bag-complete-normal-screen-caller.json','io/catalog-bag-complete-item-window-and-class-headers.json']),
 ('Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb',[[318,451],[982,1010],[1040,len((R/'Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb').read_text().splitlines())]],['Dungeon.initialize347–382 and generate428–450 complete; adjacent full accessors/local predicates within318–451','generateMapInPlace982–1005 complete','PokemonGlobalMetadata dungeon getters1047–1058 complete','complete random_dungeon event registration1063–EOF; other maze/paint/room-placement implementations not accepted'],['io/catalog-dungeon-complete-seed-constructor-and-generate.json','io/catalog-dungeon-complete-map-create-receiver.json'])
]:
 found=next((x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==path),None)
 if not found:found={'repo':'R','path':path,'status':'PARTIAL_READ_COMPLETE_NAMED_UNITS','reader':'/root/kernel_atomic_reception','whole_file_read':False};ledger['records'].append(found)
 if found.get('status')!='FULL_READ':
  found['actual_read_ranges']=sorted(set(tuple(x) for x in found.get('actual_read_ranges',[]))|set(tuple(x) for x in ranges));found['complete_units']=sorted(set(found.get('complete_units',[])+units));found['later_read_evidence']=sorted(set(found.get('later_read_evidence',[])+ios))
ledger['updated_utc']=NOW;write('reading-ledger.json',ledger)
tree=ast.parse((BASE/'integrate-catalog020304.py').read_text())
sources=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='sources' for t in n.targets))
sources.update({
 'events':'Data/Scripts/003_Game processing/005_Event_Handlers.rb','collections':'Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb','plugin':'Data/Scripts/001_Technical/005_PluginManager.rb','overworld':'Data/Scripts/012_Overworld/001_Overworld.rb','time':'Data/Scripts/012_Overworld/003_Overworld_Time.rb','stats':'Data/Scripts/004_Game classes/012_Game_Stats.rb','recorded':'Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb','map':'Data/Scripts/004_Game classes/004_Game_Map.rb','vars':'Data/Scripts/004_Game classes/001_Switches and Variables/003_Game_Variables.rb','switches':'Data/Scripts/004_Game classes/001_Switches and Variables/002_Game_Switches.rb','selfswitches':'Data/Scripts/004_Game classes/001_Switches and Variables/004_Game_SelfSwitches.rb','utils':'Data/Scripts/019_Utilities/001_Utilities.rb','filetest':'Data/Scripts/001_Technical/002_Files/001_FileTests.rb','mixins':'Data/Scripts/001_Technical/002_Files/002_FileMixins.rb','http':'Data/Scripts/001_Technical/002_Files/003_HTTP_Utilities.rb','ruby':'Data/Scripts/001_Technical/002_RubyUtilities.rb','deprecation':'Data/Scripts/001_Technical/001_Debugging/005_Deprecation.rb','errors':'Data/Scripts/001_Technical/001_Debugging/003_Errors.rb','value':'Data/Scripts/002_Save data/002_SaveData_Value.rb','savefile':'Data/Scripts/002_Save data/001_SaveData.rb','registrations':'Data/Scripts/002_Save data/004_Game_SaveValues.rb','convert':'Data/Scripts/002_Save data/003_SaveData_Conversion.rb','all14':'Data/Scripts/002_Save data/005_Game_SaveConversions.rb','saveui':'Data/Scripts/016_UI/014_UI_Save.rb','bag':'Data/Scripts/013_Items/008_PokemonBag.rb','bagui':'Data/Scripts/016_UI/007_UI_Bag.rb','berry':'Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb','dungeon':'Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb'
})
bindings={};named={}
for row in rows:
 ident=row['id'];keys=[]
 if ident.startswith('EP'):
  n=int(ident[2:]);keys=('events collections' if n<=5 or 22<=n<=25 else 'events collections overworld' if n>=26 else 'plugin').split()
 elif ident.startswith('TM'):
  n=int(ident[2:]);keys={1:'time',2:'phone',3:'phone',4:'stats start',5:'',6:'dungeon params tiles',7:'recorded',8:'stats start registrations',9:'berry bag',10:'stats',11:'stats',12:'overworld',13:'stats',14:'time settings',15:'utils vars map',16:'utils vars map',17:'utils vars map',18:'utils vars map',19:'utils vars map registrations',20:'ruby',21:'ruby',22:'ruby',23:'ruby'}[n].split()
  if n==5:named[ident]=['received/root-lottery-finite-reception.v1.json']
  if n in [10,11,13]:named[ident]=['received/ui-complete-finite-reception.json','received/ui-correction-dex-reception.json']
 elif ident.startswith('IO'):
  n=int(ident[2:]);keys=('http' if n<=5 or n>=16 else 'filetest' if n in [6,7] else 'filetest' if 13<=n<=15 else 'errors main plugin c1' if n==11 else 'errors main').split()
 elif ident.startswith('DP'):keys=['deprecation']
 elif ident.startswith('LZ'):
  n=int(ident[2:]);keys=('intl load' if n in [13,14] else 'intl debug' if n in [15,16] else 'intl overworld berry bag' if n in [36,37,38] else 'intl' ).split()
  if n in [39,40,41]:named[ident]=['received/ui-complete-finite-reception.json','received/ui-correction-dex-reception.json']
 elif ident.startswith('SV'):keys='value savefile registrations start load stats factory map'.split()
 elif ident.startswith('MG'):
  n=int(ident[2:]);keys=('plugin convert' if n==1 else 'convert savefile registrations all14' if n<=5 else 'saveui start' if 6<=n<=8 else 'convert all14' if n in [9,10] else 'start load factory map' if n in [11,12] else 'convert all14 stats' if 13<=n<=16 else 'convert all14 bag bagui').split()
  if n==9:keys+=['daycare']
  if n==10:keys+=['phone']
 elif ident.startswith('U02-SV-WORLD'):keys='start factory map events collections'.split()
 elif ident.startswith('U01-M01-') or ident.startswith('C01F-'):keys='intl debug'.split()
 elif ident.startswith('U01-M02-'):
  n=int(ident.split('-')[2]);keys={1:'vars switches selfswitches utils map',2:'collections',3:'mixins',4:'all14 convert berry',5:'errors main saveui',6:'stats',7:'utils',8:'mixins'}[n].split()
 else:raise AssertionError(ident)
 bindings[ident]=keys
sources['daycare']='Data/Scripts/012_Overworld/007_Overworld_DayCare.rb'
lib=json.loads((RR/'tasks/coverage_acceptance_incremental/dispatch/kernel_atomic_reception.readset.json').read_text())['all_fixed_R432_F131_identity_library']
identities={}
for key in sorted(set(k for v in bindings.values() for k in v)):
 path=sources[key];fixed=next(x for x in lib if x['repo']=='R' and x['path']==path);raw=(R/path).read_bytes();assert len(raw)==fixed['bytes'] and hashlib.sha256(raw).hexdigest()==fixed['sha256']
 current=next(x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==path)
 identities[key]={'fixed':fixed,'raw_bytes_sha_equal':True,'actual_reader':'/root/kernel_atomic_reception','whole_file_actually_read':current.get('status')=='FULL_READ','complete_named_credit':current if current.get('status')!='FULL_READ' else 'Full source actually personally read; explicit named method/conditional row meaning only, no mechanical whole-file acceptance.'}
receipt_ids={}
for name in sorted(set(p for arr in named.values() for p in arr)):
 raw=(BASE/name).read_bytes();receipt_ids[name]={'path':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'reception':'Actual whole selected finite contribution previously read; original sourceFULL/reader retained inside complete receipt. Package has excess other units, only actual named case unit contributes here.'}

common={
 3:['All expected results are static derived cases, not executed tests.','Asset/native/host/run status remains scope-qualified.','EP/TM/IO/DP/LZ/SV/MG owner links are navigation and have no automatic whole-owner acceptance.'],
 56:['TM15–23 derived/unexecuted; valid slot1/no main override/given clocks except TM19 explicit invalid controls.','Existing map/normal refresh/no slot rewrite; independent subcases except continuousTM16.','Refresh counts are requests; original controlled receipts are stub calls, not real event pages/save roundtrips.'],
 90:['IO16–20 precise errors/stub counts refer to original Ruby2.6.10p210 controlled original-function receipt, not this execution.','Independent requests/no filetarget/http example.invalid/fake200OK host; no real networking.','Target Ruby3.1 game host remainsUNVERIFIED.','Current static source proves constructor before localhostcatch and convenience entire-call catch only.','Source placement plus historical controlled runtime cannot become target-host execution proof.'],
 140:['LZ26–35 legal readable single nonmapdomain24 file/nonempty noncomment contents/no overrides/physicalorder fixed.','Subcases independent; prior singlefile receipt did not execute whole menu/crossfile/binary writes.','Repeated-key examples do not prove default corpus duplicates.','Replacement controls use original when all currentlanguage layers miss and observe before window processing.','Codepoint pairs are notU+0001; additional escapes/native presentation remain unverified.'],
 201:['MG17–19 fixed converters/validbag/version context/no override or concurrentwrite.','Target branch/object accesses normal; only bounded memorystate derived.','Ordinary UI additionally assumes its own dependencies normal; no legacyread/backup/writeback/hostUI executed.'],
 211:['U02 two rows are finite normalrestore/failure-prefix projections of WP11§6.1–6.2/WP13§3.3.','They do not change default17/save duplicate-registration/type/missing-map/nil-versus-empty-event/notification contracts.','Conditional cross-map projections are not default oldrecord load path.','Prior GR3 identifiers are historical/owner navigation, not full original-history execution received here.'],
 220:['Author-input vectors fixed legal dependencies/no overrides/normal preceding calls.','Reference game/independent behavior model/fileIO/nativehost/Demo not executed.','Subcases reset independently unless explicitly continuous.'],
 279:['LZ36–41 currentlanguage game/core valid/no lookup orconsumer overrides/normal priorsteps.','String identity observed after lookup before window control processing.','Image identity observed at resource delivery, not actualmedia/host/pixels.','WP08/WP15/WP65 ControlHelp links are bounded named consumers, not all_UI localization permission.']
}
records=[]
for row in rows:
 ident=row['id'];line=case_lines[ident];group_premise=[3]
 for a,b,qualifier in [(60,68,56),(94,98,90),(144,153,140),(205,207,201),(215,216,211),(224,275,220),(283,288,279)]:
  if a<=line<=b:group_premise.append(qualifier)
 for number,assertion in enumerate(row['manual_subassertions'].split('||'),1):
  status='LOCALLY_RECONSTRUCTED_FINITE_SOURCE_VECTOR'
  if ident in named:status='NAMED_COMPLETE_FINITE_CONTRIBUTION_PLUS_EXACT_LOCAL_DEFINITIONS'
  if ident=='TM11':status='LOCAL_SETTER_NAMED_UI_DISPLAY_ACCEPTED_ACTUAL_EVENT_CALLER_OPEN'
  if ident in ['IO16','IO17','IO18','IO19','IO20','LZ30']:status='CURRENT_STATIC_PLACEMENT_AND_ORIGINAL_COMPLETE_CRITERIA_RECEIVED_RAW_PROBE_OPEN'
  if ident.startswith('U02-SV-WORLD'):status='LOCAL_COMPLETE_SOURCE_FINITE_WORLD_PROJECTION_NOT_WHOLE_WORLD_OWNER_ACCEPTANCE'
  boundary=row['failure_and_scope']
  if ident=='MG18':boundary='UI_Bag actual complete Window/Scene classes and normalcaller1–580 now personally read; oldfield not cleared by this ordinary navigation. Adapter and Bag accessor source complete. Finite normal-dependency premise only, not whole714L UI or default startup repeat.'
  records.append({'id':'KAR-CAT050607080910-'+ident+'-S%02d'%number,'case_id':ident,'formal':{'path':F,'lines':[line],'exact_text':text[line-1]},'assertion':assertion,'manual_source_unit_label':row['source_units'],'source_complete_units':[{'path':sources[k],'identity_ref':k,'whole_file_actually_read':identities[k]['whole_file_actually_read'],'actual_credit':identities[k]['complete_named_credit']} for k in bindings[ident]],'named_complete_contribution_refs':[receipt_ids[n] for n in named.get(ident,[])],'source_status':status,'reception_status':status,'premise':'All complete formal row input qualifiers preserved verbatim; shared exact qualification lines listed below remain effective. Inputs independent unless case explicitly continuous.','shared_qualification_lines':group_premise,'normal_failure_cancel_partial':boundary,'original_fact_refs':[],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED','update_started':False,'count_status':'WORKING_REFINEMENT_OR_CONTROL_NOT_FROZEN_UNIQUE_ATOM_DENOMINATOR'})
for line,assertions in common.items():
 for number,assertion in enumerate(assertions,1):records.append({'id':'KAR-CAT050607080910-COMMON-L%03d-S%02d'%(line,number),'formal':{'path':F,'lines':[line],'exact_text':text[line-1]},'assertion':assertion,'source_status':'CATALOG_SHARED_QUALIFICATION_AND_OWNER_NAVIGATION_PERSONALLY_RECONCILED','reception_status':'FINITE_SCOPE_ACCEPTED_OR_EXACT_HISTORY_OPEN_AS_STATED','premise':'Applies only to its explicitly named group; histories and linked owners not automatically inherited.','normal_failure_cancel_partial':'Qualification/action boundary; actual source branch and prefix stated per case. No new runtime execution or compatibility policy.','original_fact_refs':[],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED','count_status':'WORKING_SHARED_PREMISE_NOT_FROZEN_UNIQUE_DENOMINATOR'})
out={'schema':'kernel-second-catalog-hand-derived-meanings-v1','utc':NOW,'case_count':206,'case_children':782,'working_child_count':len(records),'case_tsv_sha256':hashlib.sha256((BASE/'catalog050607080910-manual-cases.tsv').read_bytes()).hexdigest(),'source_identities':identities,'named_contributions':receipt_ids,'records':records,'remaining':'All206 case rows and8 shared qualification paragraphs personally meaning-disposed. Exact raw historical probes, HallOfFame actual event caller, fullworld/maze/native outcomes remain bounded, not generic all-row OPEN. Composite/repeated controls need final unique denominator reconciliation.'}
write('catalog050607080910-manual-atoms.json',out)
main=read('manual-atomic-clauses.json');main['records']=[x for x in main['records'] if not x['id'].startswith('KAR-CAT050607080910-')]+records;write('manual-atomic-clauses.json',main)
old=read('old-locator-disposition.json')
for item in old['records']:
 if item['path']!=F:continue
 children=[x for x in records if item['range'][0]<=x['formal']['lines'][0]<=item['range'][1]]
 if children:item.update(manual_child_assertions=sorted(set(item.get('manual_child_assertions',[])+[x['id'] for x in children])),disposition='EXPLICIT_MANUAL_MEANINGS_WITH_PER_CHILD_BOUNDED_STATUS',semantic_acceptance='Only full actual conditional meanings, exact source/reader/normal-failure/history premises per child; no inherited PASS or whole-case universal approval.',pending='Final unique child denominator reconciliation plus exact per-child history/native/actual-event-caller boundaries.')
 elif text[item['range'][0]-1].startswith('|'):item.update(disposition='TABLE_LAYOUT_COLUMN_OR_SEPARATOR_NO_RUNTIME_ASSERTION',purpose='Actual column names or separators read; data meanings handled individually.',semantic_acceptance='LAYOUT_ONLY',pending='No standalone runtime assertion in these labels.')
 elif text[item['range'][0]-1].startswith('#'):item.update(disposition='LAYOUT_HEADING_EXACT_BODY_JOIN',purpose='Actual group name/count/range points to individually reconstructed EP27/TM23/IO20/DP5/LZ35+6/SV17/MG19 and author/world vectors; no extra runtime behavior.',semantic_acceptance='NAVIGATION_ONLY_BODY_CHILD_STATUS_CONTROLS',pending='No unexamined runtime rule inferred from heading.')
 else:raise AssertionError(('Undisposed old locator',item))
write('old-locator-disposition.json',old)
progress=read('progress.json');progress.update(updated_utc=NOW,catalog050607080910_cases_manual=206,catalog050607080910_working_children=len(records),explicit_manual_atom_subset=len(main['records']),old_locators_with_explicit_partial_child_binding=sum(bool(x.get('manual_child_assertions') or x.get('explicit_manual_child_ids')) for x in old['records']));write('progress.json',progress)
print(json.dumps({'utc':NOW,'cases':206,'case_children':782,'with_shared_children':len(records),'working_total':len(main['records']),'old_named':progress['old_locators_with_explicit_partial_child_binding']}))
