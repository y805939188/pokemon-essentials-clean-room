"""Bind manually written WP09 meanings and individually checked registration values."""
import csv
import datetime
import hashlib
import json
import subprocess
from pathlib import Path
BASE=Path(__file__).resolve().parent
B=Path('/workspace/pokemon-essentials-clean-room')
R=Path('/workspace/pokemon-essentials')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
FORMAL='deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md'
TEXT=(B/FORMAL).read_text().splitlines()
FILES={
 'value':'Data/Scripts/002_Save data/002_SaveData_Value.rb',
 'registration':'Data/Scripts/002_Save data/004_Game_SaveValues.rb',
 'file':'Data/Scripts/002_Save data/001_SaveData.rb',
 'start':'Data/Scripts/003_Game processing/001_StartGame.rb',
 'scene':'Data/Scripts/003_Game processing/002_Scene_Map.rb',
 'loadui':'Data/Scripts/016_UI/013_UI_Load.rb',
 'saveui':'Data/Scripts/016_UI/014_UI_Save.rb',
 'stats':'Data/Scripts/004_Game classes/012_Game_Stats.rb',
 'vars':'Data/Scripts/004_Game classes/001_Switches and Variables/003_Game_Variables.rb',
 'switch':'Data/Scripts/004_Game classes/001_Switches and Variables/002_Game_Switches.rb',
 'selfswitch':'Data/Scripts/004_Game classes/001_Switches and Variables/004_Game_SelfSwitches.rb',
 'utils':'Data/Scripts/019_Utilities/001_Utilities.rb',
 'mapfactory':'Data/Scripts/004_Game classes/005_Game_MapFactory.rb',
 'metadata':'Data/Scripts/012_Overworld/002_Overworld_Metadata.rb',
 'overworld':'Data/Scripts/012_Overworld/001_Overworld.rb',
 'warp':'Data/Scripts/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb',
 'main':'Data/Scripts/999_Main/999_Main.rb',
 'errors':'Data/Scripts/001_Technical/001_Debugging/003_Errors.rb',
 'settings':'Data/Scripts/001_Settings.rb',
 'conversions':'Data/Scripts/002_Save data/005_Game_SaveConversions.rb'}
ledger=json.loads((BASE/'reading-ledger.json').read_text())
full={x['path'] for x in ledger['records'] if x.get('repo')=='R' and x.get('status')=='FULL_READ'}
identity=[]
for k,path in FILES.items():
 raw=(R/path).read_bytes();fixed=subprocess.check_output(['git','show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+path],cwd=R);assert raw==fixed
 identity.append({'key':k,'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'blob':subprocess.check_output(['git','rev-parse','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+path],cwd=R,text=True).strip(),'actual_reader':'/root/kernel_atomic_reception','whole_source_actually_read':path in full,'complete_unit_scope':('pbDefaultMap4–8 and pbWarpToMap10–39 only; actualread1–79; other Debug methods uncredited' if k=='warp' else 'Whole source actually read; only named current assertion is semantically adopted')})
def sources(unit):
 if unit.startswith('formal-') or unit=='catalog-forward':return []
 keys=set()
 for token,key in [('Value','value'),('valid?','value'),('load_values','value'),('load_all_values','value'),('load_bootup_values','value'),('load_new_game_values','value'),('mark_values_as_unloaded','value'),('initialize_bootup_values','value'),('compile_save_hash','value'),('register','value'),('default17','registration'),('save_to_file','file'),('read_from_file','file'),('delete_file','file'),('SaveData.FILE_PATH','file'),('Scene_Map','scene'),('Game.start_new','start'),('Game.load','start'),('Game.save','start'),('Game.initialize','start'),('Game.set_up_system','start'),('PokemonLoadScreen','loadui'),('pbStartLoadScreen','loadui'),('load_save_file','loadui'),('prompt_save_deletion','loadui'),('delete_save_data','loadui'),('GameStats','stats'),('Game_Variables','vars'),('Game_Switches','switch'),('Game_SelfSwitches','selfswitch'),('pbSet','utils'),('PokemonMapFactory','mapfactory'),('PokemonMapMetadata','metadata'),('on_enter_map','overworld'),('pbWarpToMap','warp'),('mainFunction','main'),('pbCriticalCode','errors'),('Settings','settings'),('Game_SaveConversions','conversions')]:
  if token in unit:keys.add(key)
 if 'default17' in unit:keys.add('value')
 assert keys,unit
 return [{'path':FILES[k],'complete_named_unit':unit,'actual_reader':'/root/kernel_atomic_reception','whole_file_actually_read':FILES[k] in full,'identity_ref':k,'credit':'Exact complete named definition/fact; no mechanical full-file semantic range'} for k in sorted(keys)]
records=[]
for row in csv.DictReader((BASE/'wp09-manual-atoms.tsv').open(),delimiter='\t'):
 line=int(row['formal_line']);records.append({'id':'KAR-WP09-'+row['id'],'formal':{'path':FORMAL,'lines':[line],'exact_text':TEXT[line-1]},'assertion':row['assertion'],'source_complete_units':sources(row['source_unit']),'source_status':row['status'],'reception_status':row['status'],'premise':'Fixed B8/R and exact named local branch; only current complete assertion, not whole paragraph/source/domain. Runtime/native behavior NOT_EXECUTED.','normal_failure_cancel_partial':row['premise_and_failure_boundary'],'original_fact_refs':[row['original_fact']] if row['original_fact'] else [],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED','update_started':False})
registration_rows=list(csv.DictReader((BASE/'wp09-registration-manual-values.tsv').open(),delimiter='\t'))
assert len(registration_rows)==17 and len({x['id'] for x in registration_rows})==17
for row in registration_rows:
 ident=row['id'];line=int(row['formal_line']);start,end=map(int,row['source_range'].split('-'))
 facts={
  'TYPE':f"Registration {ident} has ensured class {row['class']}; this is the outer type predicate, not its fields.",
  'BOOT':f"Registration {ident} load_in_bootup is {row['boot']}; boot traversal additionally requires its independent loaded flag false.",
  'SUPPLIER':f"Registration {ident} new-game supplier is {row['new_supplier']}; ABSENT means no supplier is called, not an implicit value.",
  'RESET':f"Registration {ident} reset_on_new_game is {row['reset']}; its supplier still requires existence and unloaded-or-reset predicate.",
  'SAVE':f"Registration {ident} save callback reads {row['save_getter']}, then Value.save validates its result before compile assignment under identity {ident}.",
  'LOAD':f"Registration {ident} validated restore callback assigns to {row['load_receiver']}; its own loaded flag becomes true only after callback returns."}
 for facet,claim in facts.items():
  records.append({'id':'KAR-WP09-REG-'+ident+'-'+facet,'formal':{'path':FORMAL,'lines':[line],'exact_text':TEXT[line-1]},'assertion':claim,'source_complete_units':[{'path':FILES['registration'],'unit':'entire individually read registration block','range':[start,end],'actual_reader':'/root/kernel_atomic_reception','whole_file_actually_read':True},{'path':FILES['value'],'unit':'complete Value definition and corresponding boot/new/load/save traversal','actual_reader':'/root/kernel_atomic_reception','whole_file_actually_read':True}],'source_status':'SOURCE_STATIC_PERSONALLY_CHECKED','reception_status':'RECEIVED_LOCAL_REGISTRATION_FACET','premise':'Unmodified exact17 default blocks, ordinary declaration/registration order and available referenced class/constants. Supplier invocation is not a claim all nested constructors/data/host calls succeed.','normal_failure_cancel_partial':'Noninteractive declaration/callback mechanism. Each actual callback/value validation can fail and preserve earlier effects; no direct file operation in this individual block. Full compile/save/read and loaded gates are separate named manual children. Inner domain/persistence encoding is outside this outer facet.','original_fact_refs':['KER-F116'],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED','update_started':False,'manual_basis':'Each actual value was personally checked against complete127-line source. Template enumerates six distinct manually entered facts, not a generated semantic PASS or frozen atomic denominator.'})
assert len({r['id'] for r in records})==len(records)
out={'schema':'kernel-wp09-hand-authored-semantic-children-v1','utc':NOW,'working_children':len(records),'source_identities':identity,'actual_reads':['io/wp09-complete-formal-for-manual-children.json','io/wp09-save-value-and-registration-complete-reread-for-children.json','io/wp09-startgame-load-ui-complete-reread-for-children.json','io/wp09-main-save-ui-and-slot-definitions-complete-reread.json','io/wp09-slot-convenience-complete-helper.json','io/wp09-map-selector-and-reentry-complete-units.json'],'records':records,'denominator':'Working semantic refinements/aliases; not frozen final unique atomic denominator','remaining':'Exact GR3-M03 historical qualification, complete catalog scenario receipt and remaining declared interfaces/runtime unknowns; no whole-WP09/global PASS.'}
(BASE/'wp09-manual-atoms.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
mainp=BASE/'manual-atomic-clauses.json';main=json.loads(mainp.read_text());ids={r['id'] for r in records};main['records']=[r for r in main['records'] if r['id'] not in ids]+records;mainp.write_text(json.dumps(main,ensure_ascii=False,indent=2)+'\n')
oldp=BASE/'old-locator-disposition.json';old=json.loads(oldp.read_text())
for item in old['records']:
 if item['path']!=FORMAL:continue
 children=[r for r in records if item['range'][0]<=r['formal']['lines'][0]<=item['range'][1]]
 if children:
  item['manual_child_assertions']=sorted(set(item.get('manual_child_assertions',[])+[r['id'] for r in children]));item['disposition']='EXPLICIT_MANUAL_MEANINGS_WITH_PER_CHILD_BOUNDED_STATUS';item['semantic_acceptance']='ONLY_LISTED_MEANINGS_AND_EXPLICIT_PREMISES; final unique atomic denominator not frozen';item['pending']=[{'id':r['id'],'boundary':r['normal_failure_cancel_partial']} for r in children if 'OPEN' in r['source_status'] or 'PENDING' in r['source_status'] or 'KNOWN_REQUIRED' in r['source_status']]
  if not item['pending']:item['pending']='No additional local meaning claimed beyond exact listed children. Chapter-wide historical/catalog and explicitly non-goal domains are separate, not generic hidden source approval.'
 if item['range'][0] in [27,48,61,87,99,125]:item.update(disposition='TABLE_COLUMN_LABELS_NOT_DATA_OR_RUNTIME_ASSERTION',purpose='Actual complete formal table columns read; body data/logic individually reconciled in named children.',semantic_acceptance='LAYOUT_ONLY_NO_ADJACENT_APPROVAL',pending='No standalone runtime assertion in these labels.')
oldp.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
sfp=BASE/'sourcefact-consumer-receptions.json';sf=json.loads(sfp.read_text())
for item in sf['records']:
 links=[r['id'] for r in records if item['fact_id'] in r['original_fact_refs']]
 if links:item['manual_atom_links']=sorted(set(item.get('manual_atom_links',[])+links));item['named_child_reception']='Exact WP09 per-child support/consumer/failure premises; no adoption of all historical original context as current PASS.'
sf['updated_utc']=NOW;sfp.write_text(json.dumps(sf,ensure_ascii=False,indent=2)+'\n')
wp=BASE/'progress.json';p=json.loads(wp.read_text());p.update(updated_utc=NOW,explicit_manual_atom_subset=len(main['records']),wp09_explicit_manual_subset=len(records),old_locators_with_explicit_partial_child_binding=sum(bool(x.get('manual_child_assertions') or x.get('explicit_manual_child_ids')) for x in old['records']));wp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':NOW,'WP09_manual_general':len(records)-102,'individual_registration_facets':102,'working_new_children':len(records),'working_total':len(main['records']),'partial_old_bindings':p['old_locators_with_explicit_partial_child_binding']}))
