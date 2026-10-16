"""Bind personally checked WP10 clauses and explicit historical mappings."""
import csv,datetime,hashlib,json,re,subprocess
from pathlib import Path
BASE=Path(__file__).resolve().parent
B=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F='deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md'
T=(B/F).read_text().splitlines()
def read(n):return json.loads((BASE/n).read_text())
def write(n,v):(BASE/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
ledger=read('reading-ledger.json')
for path,ranges,units,io in [
 ('Data/Scripts/013_Items/004_Item_Phone.rb',[[1,214]],['complete outer Phone class4–210, including initializer/get/add/sort and singleton actual receivers'],['io/wp10-phone-conversion-actual-receiver-complete-units.json']),
 ('Data/Scripts/012_Overworld/007_Overworld_DayCare.rb',[[1,115],[172,213],[261,347]],['generate/determine species/basic egg/inherit_form complete definitions within1–115; get_moves_to_inherit onlyPARTIAL','inherit_IVs173–212 complete','DayCareSlot261–317 complete','MAX_SLOTS327/initialize329–335/reset_egg_counters341–344 complete; count at346–347PARTIAL'],['io/wp10-phone-conversion-actual-receiver-complete-units.json','io/wp10-daycare-slot-conversion-complete-state-definitions.json'])]:
 found=next((x for x in ledger['records'] if x.get('path')==path),None)
 if not found:found={'repo':'R','path':path,'status':'PARTIAL_READ_COMPLETE_NAMED_UNITS','reader':'/root/kernel_atomic_reception'};ledger['records'].append(found)
 assert found.get('status')!='FULL_READ'
 found['actual_read_ranges']=sorted({tuple(x) for x in found.get('actual_read_ranges',[])}|{tuple(x) for x in ranges})
 found.setdefault('complete_units',[]);found['complete_units']+=units;found.setdefault('later_read_evidence',[]);found['later_read_evidence']+=io;found['whole_file_read']=False
ledger['updated_utc']=NOW;write('reading-ledger.json',ledger)
full={x['path'] for x in ledger['records'] if x.get('repo')=='R' and x.get('status')=='FULL_READ'}
FILES={
 'engine':'Data/Scripts/002_Save data/003_SaveData_Conversion.rb',
 'all14':'Data/Scripts/002_Save data/005_Game_SaveConversions.rb',
 'value':'Data/Scripts/002_Save data/002_SaveData_Value.rb',
 'registration':'Data/Scripts/002_Save data/004_Game_SaveValues.rb',
 'file':'Data/Scripts/002_Save data/001_SaveData.rb',
 'start':'Data/Scripts/003_Game processing/001_StartGame.rb',
 'loadui':'Data/Scripts/016_UI/013_UI_Load.rb',
 'saveui':'Data/Scripts/016_UI/014_UI_Save.rb',
 'main':'Data/Scripts/999_Main/999_Main.rb',
 'errors':'Data/Scripts/001_Technical/001_Debugging/003_Errors.rb',
 'plugin':'Data/Scripts/001_Technical/005_PluginManager.rb',
 'stats':'Data/Scripts/004_Game classes/012_Game_Stats.rb',
 'bag':'Data/Scripts/013_Items/008_PokemonBag.rb',
 'plant':'Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb',
 'phone':'Data/Scripts/013_Items/004_Item_Phone.rb',
 'daycare':'Data/Scripts/012_Overworld/007_Overworld_DayCare.rb',
 'warp':'Data/Scripts/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb',
 'settings':'Data/Scripts/001_Settings.rb'}
identities=[]
for k,path in FILES.items():
 raw=(R/path).read_bytes();assert raw==subprocess.check_output(['git','show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+path],cwd=R)
 identities.append({'key':k,'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'blob':subprocess.check_output(['git','rev-parse','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+path],cwd=R,text=True).strip(),'reader':'/root/kernel_atomic_reception','whole_source_actually_read':path in full,'credit':'Identity check adds no semantic reading; exact complete named unit and own full/partial ledger govern.'})
index={x['id']:x for x in read('facility-save-conversion-contribution.v1.json')['all14_actual_default_conversions']}
def source_units(unit):
 if unit.startswith('formal-') or unit=='catalog-forward':return []
 keys=set();entries=[]
 for ident,meta in index.items():
  if ident in unit:entries.append({'path':FILES['all14'],'complete_named_unit':ident,'range':meta['complete_range'],'actual_reader':'/root/kernel_atomic_reception','whole_file_actually_read':True})
 if entries:keys.add('engine')
 for token,key in [('Conversion','engine'),('run_conversions','engine'),('get_conversions','engine'),('register_conversion','engine'),('run_single_conversions','engine'),('all14-default','all14'),('default17','registration'),('to_hash_format','file'),('read_from_file','file'),('get_data_from_file','file'),('delete_file','file'),('Game.','start'),('load_save_file','loadui'),('prompt_save_deletion','loadui'),('delete_save_data','loadui'),('PokemonLoadScreen','loadui'),('pbStartLoadScreen','loadui'),('pbEmergencySave','saveui'),('mainFunction','main'),('pbCriticalCode','errors'),('PluginManager','plugin'),('GameStats','stats'),('BerryPlantData','plant'),('Phone.','phone'),('DayCare','daycare'),('pbWarpToMap','warp'),('Settings','settings')]:
  if token in unit:keys.add(key)
 if unit=='daycare-conversion':return source_units('v20_refactor_day_care_variables/DayCareSlot.filled?')
 if unit=='phone-conversion':return source_units('v21_replace_phone_data/Phone.add_silent')
 if unit=='v20_rename_bag_variables/UI_Bag':keys.add('bag')
 assert keys or entries,unit
 for k in sorted(keys):entries.append({'path':FILES[k],'complete_named_unit':unit,'actual_reader':'/root/kernel_atomic_reception','whole_file_actually_read':FILES[k] in full,'identity_ref':k,'scope':'Exact actually read named complete definitions; no mechanical fullrange or whole-domain approval'})
 return entries
records=[]
for name in ['wp10-manual-core.tsv','wp10-manual-conversions.tsv']:
 for row in csv.DictReader((BASE/name).open(),delimiter='\t'):
  line=int(row['formal_line']);records.append({'id':'KAR-WP10-'+row['id'],'formal':{'path':F,'lines':[line],'exact_text':T[line-1]},'assertion':row['assertion'],'source_complete_units':source_units(row['source_unit']),'source_status':row['status'],'reception_status':row['status'],'premise':'Unmodified fixedB8/R and named finite input/caller state. Definitions/conditional source vectors are distinct from business reachability, native load/run or whole-domain compatibility.','normal_failure_cancel_partial':row['premise_and_failure_boundary'],'original_fact_refs':[row['original_fact']] if row['original_fact'] else [],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED','update_started':False})
maps=list(csv.DictReader((BASE/'wp10-historical-item-identities.manual.tsv').open(),delimiter='\t'))
assert len(maps)==68 and sum(x['kind']=='berry' for x in maps)==64
raw=(R/FILES['all14']).read_text()
for row in maps:
 old=int(row['old_id']);line=int(row['formal_line']);symbol=row['identity']
 assert re.search(r'\b'+str(old)+r'\s*=>\s*:'+symbol+r'\b',raw)
 assert f'| {old} | {symbol} |'==T[line-1]
 records.append({'id':'KAR-WP10-ID-'+row['kind']+'-'+str(old),'formal':{'path':F,'lines':[line],'exact_text':T[line-1]},'assertion':f"Historical {row['kind']} numeric identity {old} maps to :{symbol} in the explicit default conversion table.",'source_complete_units':source_units('v20_fix_planted_berry_numerical_ids'),'source_status':'PERSONALLY_READ_EXACT_HISTORICAL_ID_MAPPING','reception_status':'RECEIVED_LOCAL_STATIC_MAPPING','premise':'Actual eligible old Array entry under selected converter; later symbol/current record lookup and native data load are separate. All68 actual source/formal mapping entries were personally read, not accepted by regex alone.','normal_failure_cancel_partial':'Eligible field assignment follows lookup. Berry unknown usesORAN; mulch unknown can becomenil. This row establishes exact named table entry only, not all objects/legacy/native compatibility.','original_fact_refs':['KER-F128'],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED'})
for row in csv.DictReader((BASE/'wp10-plant-slot-edges.manual.tsv').open(),delimiter='\t'):
 line=int(row['formal_line']);records.append({'id':'KAR-WP10-SLOT-'+row['id'],'formal':{'path':F,'lines':[line],'exact_text':T[line-1]},'assertion':f"For {row['layout']}-slot plant layout, one-based position {row['position']} has edge: {row['write']}.",'source_complete_units':source_units('v20_refactor_planted_berries_data/BerryPlantData.initialize'),'source_status':'PERSONALLY_READ_EXACT_POSITION_WRITE_EDGE','reception_status':'RECEIVED_LOCAL_STATIC_MAPPING','premise':row['premise'],'normal_failure_cancel_partial':'Constructor first, symbol-gated field writes, replacement only at reached tail. Failure can preserve earlier field/entry effects and prevent later fields/replacement. No implicit validation/coercion or rollback.','original_fact_refs':['KER-F129'],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED'})
assert len({r['id'] for r in records})==len(records)
write('wp10-manual-atoms.json',{'schema':'kernel-wp10-hand-authored-semantic-children-v1','utc':NOW,'working_children':len(records),'identities':identities,'records':records,'manual_basis':'90 general/recovery and63 conversion/vector assertions plus68 individually read identity entries and17 exact slot edges. Working refinement count, not frozen final unique denominator.','remaining':'Exact pending UI bag complete unit, Phone later named dispatch, all declared native/history/inner-domain boundaries are explicit per record; no whole-WP10 or global PASS.'})
main=read('manual-atomic-clauses.json');ids={r['id'] for r in records};main['records']=[r for r in main['records'] if r['id'] not in ids]+records;write('manual-atomic-clauses.json',main)
old=read('old-locator-disposition.json')
for item in old['records']:
 if item['path']!=F:continue
 children=[r for r in records if item['range'][0]<=r['formal']['lines'][0]<=item['range'][1]]
 if children:
  item['manual_child_assertions']=sorted(set(item.get('manual_child_assertions',[])+[r['id'] for r in children]));item['disposition']='EXPLICIT_MANUAL_MEANINGS_WITH_PER_CHILD_BOUNDED_STATUS';item['semantic_acceptance']='Only named meanings and full specific premises; no inherited oldPASS or full-locator execution claim.'
  item['pending']=[{'id':r['id'],'boundary':r['normal_failure_cancel_partial']} for r in children if 'OPEN' in r['source_status'] or 'PENDING' in r['source_status'] or 'KNOWN_REQUIRED' in r['source_status']]
  if not item['pending']:item['pending']='No extra local meaning claimed beyond exact named children; native/inner-domain scope remains as explicitly limited in those children.'
 if item['range'][0] in [27,42,61,71,82,117,186,196,221]:item.update(disposition='TABLE_COLUMN_LABELS_NOT_DATA_OR_RUNTIME_ASSERTION',purpose='Complete column vocabulary read, actual body mappings/branches individually reconciled.',semantic_acceptance='LAYOUT_ONLY_NO_ADJACENT_APPROVAL',pending='No standalone runtime assertion in column labels.')
write('old-locator-disposition.json',old)
sf=read('sourcefact-consumer-receptions.json')
for item in sf['records']:
 links=[r['id'] for r in records if item['fact_id'] in r['original_fact_refs']]
 if links:item['manual_atom_links']=sorted(set(item.get('manual_atom_links',[])+links));item['named_child_reception']='Exact WP10 per-child source/caller/normal-failure-prefix support, not wholesale old context or execution credit.'
 if item['fact_id'] in ['KER-F134','KER-F135']:
  item['status']='SOURCE_FACT_LOCALLY_CONFIRMED_ORIGINAL_FORMAL_NAVIGATION_NOT_ACCEPTED'
  item['exception']='Original WP10:256–265 navigation contains boundary/failure section rather than FilenameUpdater; preserved original range is not semantic support. No current WP10 requirement to import developer tool is inferred.'
  item['actual_source_evidence']=['io/wp10-filename-updater-complete-reread.json','io/wp10-filename-move-whole-file-extension-complete.json','io/wp10-mapdata-whole-complete-class-reread.json']
  item['pending_exact_consumer_records']='WP75 actual developer_full_cloud complete finite formal-unit reception requested. MapData triage remains nonrequired; no alias to KER003.'
sf['updated_utc']=NOW;write('sourcefact-consumer-receptions.json',sf)
progress=read('progress.json');progress.update(updated_utc=NOW,explicit_manual_atom_subset=len(main['records']),wp10_explicit_manual_subset=len(records),old_locators_with_explicit_partial_child_binding=sum(bool(x.get('manual_child_assertions') or x.get('explicit_manual_child_ids')) for x in old['records']));write('progress.json',progress)
print(json.dumps({'utc':NOW,'new_WP10_working_children':len(records),'working_total':len(main['records']),'old_locator_named_bindings':progress['old_locators_with_explicit_partial_child_binding'],'original_F134_F135_navigation_correction':True}))
