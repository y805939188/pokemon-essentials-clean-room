"""Task-local review metadata, not target execution. Assertions are hand-authored TSV rows."""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import json
import subprocess

BASE = Path(__file__).resolve().parent
FORMAL_ROOT = Path('/workspace/pokemon-essentials-clean-room')
R = Path('/workspace/pokemon-essentials')
FORMAL = 'deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
ME = '/root/kernel_atomic_reception'
TIME = 'Data/Scripts/012_Overworld/003_Overworld_Time.rb'
STATS = 'Data/Scripts/004_Game classes/012_Game_Stats.rb'
START = 'Data/Scripts/003_Game processing/001_StartGame.rb'
UTIL = 'Data/Scripts/019_Utilities/001_Utilities.rb'
PHONE = 'Data/Scripts/013_Items/004_Item_Phone.rb'
GP = 'Data/Scripts/004_Game classes/008_Game_Player.rb'
GC = 'Data/Scripts/004_Game classes/006_Game_Character.rb'
DUN = 'Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb'
REC = 'Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb'
GLOBAL = 'Data/Scripts/012_Overworld/002_Overworld_Metadata.rb'
VALUES = 'Data/Scripts/002_Save data/004_Game_SaveValues.rb'
units = {
 'wallclock': [(TIME,4,6)], 'stats-playtime': [(STATS,173,180)],
 'stats-derived': [(STATS,173,192)], 'stats-derived-all': [(STATS,150,163)],
 'start-new': [(START,39,58)], 'game-load': [(START,63,74)],
 'scene-main': [('Data/Scripts/003_Game processing/002_Scene_Map.rb',231,252)],
 'stats-default-start': [(STATS,64,148),(START,39,58),(VALUES,120,127)],
 'phone-refresh': [(PHONE,118,134)], 'phone-frame': [(PHONE,543,560)],
 'global-phone': [(GLOBAL,5,126),(PHONE,4,15),(VALUES,76,81)],
 'tone-cache': [(TIME,82,90)], 'tone-internal': [(TIME,92,110)],
 'tone-render': [(TIME,116,124)], 'time-periods': [(TIME,44,72)],
 'weekday': [(TIME,129,149)], 'month': [(TIME,154,197)],
 'season': [(TIME,201,232)], 'moon': [(TIME,246,269)], 'zodiac': [(TIME,273,309)],
 'timer-seconds': [(UTIL,157,164)], 'timer-days': [(UTIL,166,175)],
 'timer-valid': [(UTIL,177,192)], 'timer-all': [(UTIL,157,192)],
 'step-dispatch': [('Data/Scripts/012_Overworld/001_Overworld.rb',172,186)],
 'gameplayer-distance': [(GP,130,177)], 'gameplayer-jump': [(GP,188,195),(GC,767,787)],
 'gameplayer-diagonal': [(GC,584,638)],
 'gameplayer-step-completion': [(GC,397,404),(GC,893,910),(GC,935,992),(GP,543,558)],
 'stats-inventory': [(STATS,4,148)], 'stats-constructor': [(STATS,64,148)],
 'kernel-rand': [('Data/Scripts/001_Technical/002_RubyUtilities.rb',366,389)],
 'dungeon-generate': [(DUN,428,450)],
 'record-dump': [(REC,70,72)], 'record-random': [(REC,129,133)],
 'playback-random': [(REC,188,192)], 'record-properties': [(REC,46,67)],
 'recorded-battle-file': [(REC,1,287)], 'antirandom': [(UTIL,77,98)],
 'save-wholeobjects': [(VALUES,76,81),(VALUES,120,127)],
 'encounter-version': [(GLOBAL,5,126)],
 'dungeon-save-interface': [(DUN,1047,1058),(DUN,428,450),(VALUES,76,81)],
}
ledger_path = BASE / 'reading-ledger.json'
ledger = json.loads(ledger_path.read_text())
for path, ranges, mode, evidence in [
 (REC, [[1,287]], 'FULL_READ', ['io/wp06-recorded-battle-full.json']),
 (PHONE, [[1,18],[118,164],[215,280],[318,389],[447,540],[543,600]], 'PARTIAL_READ_COMPLETE_NAMED_UNITS', ['io/wp06-phone-time-complete-units.json','io/wp03-necessary-consumer-complete-methods.json']),
 (DUN, [[320,383],[428,451],[1047,1061]], 'PARTIAL_READ_COMPLETE_NAMED_UNITS', ['io/wp06-phone-time-complete-units.json','io/wp06-pending-seed-registration.json']),
 (GLOBAL, [[1,145]], 'PARTIAL_READ_COMPLETE_NAMED_UNITS', ['io/wp06-scene-title-clock-complete-unit.json']),
 ('Data/Scripts/003_Game processing/002_Scene_Map.rb', [[201,252]], 'PARTIAL_READ_COMPLETE_NAMED_UNITS', ['io/wp06-scene-title-clock-complete-unit.json']),
]:
 found = next((v for v in ledger['records'] if v.get('path') == path), None)
 if found and found.get('status') == 'FULL_READ':
  continue
 raw = (R/path).read_bytes()
 record = {'repo':'R','path':path,'status':mode,'reader':ME,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'actual_read_ranges':ranges,'reading_evidence':evidence,'whole_file_read':mode=='FULL_READ','credit':'ACTUAL_SOURCE_READ; methods outside recorded ranges remain unread; no domain semantic PASS'}
 if mode == 'FULL_READ': record['range'] = [1,287]
 if found: found.update(record)
 else: ledger['records'].append(record)
full = {x['path'] for x in ledger['records'] if x.get('status')=='FULL_READ' and x.get('repo')=='R' and not x['path'].startswith('PBS/')}
def source_identity(path):
 raw=(R/path).read_bytes()
 return {'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'blob':subprocess.check_output(['git','rev-parse','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+path],cwd=R,text=True).strip(),'file_lines':len(raw.decode('utf-8-sig').splitlines()),'identity_only':True}
identities={path:source_identity(path) for path,_,_ in sum(units.values(),[])}
formal_lines=(FORMAL_ROOT/FORMAL).read_text().splitlines()
records=[]
with (BASE/'wp06-time-manual-atoms.tsv').open() as stream:
 for row in csv.DictReader(stream,delimiter='\t'):
  line=int(row['formal_line']); alias=row['source_unit']; source=[]
  for path,start,end in units.get(alias,[]):
   assert end<=identities[path]['file_lines'], (path,end)
   source.append({'path':path,'navigation_range':[start,end],'complete_named_unit':alias,'actual_reader':ME,'whole_file_read':path in full,'unit_read_is_not_whole_file_credit':path not in full,'identity_ref':path})
  if alias=='root-lottery-LT01':
   source=[{'reception_path':'received/root-lottery-finite-reception.v1.json','unit':'RWA-LT01','actual_source_reader':'/root','receiver':ME,'receiver_source_FULL_added':0}]
  records.append({'id':'KAR-WP06-'+row['id'],'formal':{'path':FORMAL,'lines':[line],'exact_text':formal_lines[line-1]},'assertion':row['assertion'],'source_complete_units':source,'source_status':row['status'],'reception_status':row['status'],'source_alias':alias,'premise':'Fixed B8/R; complete stated static unit plus specific premise below; no target/native execution.','normal_failure_cancel_partial':row['premise_and_failure_boundary'],'original_fact_refs':[row['original_fact']] if row['original_fact'] else [],'receiver':ME,'target_behavior':'NOT_EXECUTED','update_started':False,'additional_dependencies':'No acceptance outside each named complete unit/contribution. Declarative scope/history/search atoms grant no unseen source semantics.'})
assert len(records)==131 and len({r['id'] for r in records})==131
out={'schema':'kernel-wp06-time-hand-authored-subassertions-v1','utc':NOW,'manual_working_subset':131,'final_chapter_atomic_denominator_frozen':False,'source_identities':list(identities.values()),'records':records,'remaining':'Physical-line binding is navigation only; scope families and remaining update-consumer composites still need exact closure. No global PASS.'}
(BASE/'wp06-time-manual-atoms.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
main_path=BASE/'manual-atomic-clauses.json';main=json.loads(main_path.read_text()); old_ids={r['id'] for r in records};main['records']=[r for r in main['records'] if r['id'] not in old_ids]+records;main['manual_atomic_denominator']='NOT_FROZEN_WORKING_SUBSET_ONLY';main_path.write_text(json.dumps(main,ensure_ascii=False,indent=2)+'\n')
old_path=BASE/'old-locator-disposition.json';old=json.loads(old_path.read_text())
for oldrow in old['records']:
 if oldrow['path']!=FORMAL: continue
 children=[r['id'] for r in records if oldrow['range'][0]<=r['formal']['lines'][0]<=oldrow['range'][1]]
 if children:
  oldrow['manual_child_assertions']=children;oldrow['disposition']='PARTIAL_EXPLICIT_MANUAL_CHILD_ASSERTIONS_RECONCILED';oldrow['semantic_acceptance']='ONLY_NAMED_CHILD_CONTENT_AND_ITS_QUALIFIED_STATUS; NO_LOCATOR_WIDE_PASS';oldrow['pending']='Remaining meanings/history/negative premises and foreign consumers continue; child count is not the line semantic denominator.'
old_path.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
sf_path=BASE/'sourcefact-consumer-receptions.json';sf=json.loads(sf_path.read_text())
for item in sf['records']:
 links=[r['id'] for r in records if item['fact_id'] in r['original_fact_refs']]
 if links:item['manual_atom_links']=sorted(set(item.get('manual_atom_links',[])+links));item['reception_status']='NAMED_CHILD_FACTS_ACCEPTED_ONLY_WITH_EXPLICIT_CHILD_STATUS; all-consumer semantic closure NOT_GRANTED'
sf['updated_utc']=NOW;sf_path.write_text(json.dumps(sf,ensure_ascii=False,indent=2)+'\n')
ledger['own_reference_full_read_non_PBS']=len(full);ledger['updated_utc']=NOW;ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
progress_path=BASE/'progress.json';progress=json.loads(progress_path.read_text());progress.update(updated_utc=NOW,explicit_manual_atom_subset=len(main['records']),own_reference_full_read_non_PBS=len(full),wp06_time_explicit_manual_subset=131,old_locators_with_explicit_partial_child_binding=sum(bool(r.get('explicit_manual_child_ids') or r.get('manual_child_assertions')) for r in old['records']))
cc=json.loads((BASE/'consumer-candidate-dispositions.json').read_text());progress['consumer_candidate_dispositions']=cc['summary'];progress['own_full_source_reference_occurrences']=cc['own_full_source_reference_occurrences'];progress_path.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':NOW,'new_atoms':len(records),'working_total':len(main['records']),'full_non_PBS':len(full),'partial_locator_bindings':progress['old_locators_with_explicit_partial_child_binding'],'statuses':dict(collections.Counter(r['reception_status'] for r in records))}))
