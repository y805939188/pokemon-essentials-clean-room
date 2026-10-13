from record import *
import re
S='Data/Scripts/'
A={
 'values':('002_Save data/002_SaveData_Value.rb',1,284,'all value registration/loading/validation/compile entries'),
 'default_values':('002_Save data/004_Game_SaveValues.rb',1,127,'all 17 registrations'),
 'savefile':('002_Save data/001_SaveData.rb',1,82,'path/existence/read/save/delete/old format'),
 'convert':('002_Save data/003_SaveData_Conversion.rb',1,223,'conversion definition/selection/ordering/run/single'),
 'conversion_data':('002_Save data/005_Game_SaveConversions.rb',1,420,'all 14 registered conversion bodies'),
 'start':('003_Game processing/001_StartGame.rb',1,126,'initialize/setup/start_new/load/map/save'),
 'save':('003_Game processing/001_StartGame.rb',106,126,'save'),
 'load_ui':('016_UI/013_UI_Load.rb',216,356,'read/validate/backup/delete/continue/new/menu'),
 'emergency':('016_UI/014_UI_Save.rb',1,24,'pbEmergencySave'),
 'save_ui':('016_UI/014_UI_Save.rb',100,139,'save confirmation/overwrite and caller'),
 'main':('999_Main/999_Main.rb',1,60,'mainFunction/mainFunctionDebug/title/top-level loop'),
 'events':('003_Game processing/005_Event_Handlers.rb',1,91,'Event/NamedEvent'),
 'handlers':('003_Game processing/005_Event_Handlers.rb',93,298,'HandlerHash/Symbol/Enum/content specializations'),
 'condition':('003_Game processing/005_Event_Handlers.rb',148,197,'symbol lookup/addIf/copy/remove/clear/trigger'),
 'collections':('003_Game processing/006_Event_HandlerCollections.rb',1,123,'EventHandlers/MenuHandlers'),
 'menus':('003_Game processing/006_Event_HandlerCollections.rb',80,123,'menu registration/enumeration/call'),
 'plugin_reg':('001_Technical/005_PluginManager.rb',106,366,'register/error/queries/version comparator'),
 'plugin_meta':('001_Technical/005_PluginManager.rb',405,551,'readMeta/discovery/dependency/order'),
 'plugin_load':('001_Technical/005_PluginManager.rb',553,664,'compile decision/compile/run/findDirectory'),
 'plugin_error':('001_Technical/005_PluginManager.rb',368,403,'pluginErrorMsg'),
 'steps':('012_Overworld/001_Overworld.rb',70,187,'step notifications, soot, normal/forced step dispatch'),
 'movement_stats':('004_Game classes/008_Game_Player.rb',121,166,'bump/distance/waterfall-crest'),
 'stats':('004_Game classes/012_Game_Stats.rb',1,200,'74 defaults, derived readers, playtime/time markers'),
 'playtime':('004_Game classes/012_Game_Stats.rb',165,200,'time setters/play_time/session average/last-save'),
 'scene_title':('003_Game processing/002_Scene_Map.rb',232,252,'map scene main, clear playtime anchor on title'),
 'calendar':('012_Overworld/003_Overworld_Time.rb',1,309,'clock/day-period/tone/date/season/moon/zodiac'),
 'phone_time':('013_Items/004_Item_Phone.rb',118,134,'refresh_ready_trainers'),
 'phone_frame':('013_Items/004_Item_Phone.rb',543,560,'phone_call_counter'),
 'timers':('019_Utilities/001_Utilities.rb',154,192,'pbTimeEvent/pbTimeEventDays/pbTimeEventValid'),
 'anti':('019_Utilities/001_Utilities.rb',73,98,'AntiRandom'),
 'rand':('001_Technical/002_RubyUtilities.rb',363,388,'global/Kernel rand normalization'),
 'dungeon':('012_Overworld/008_Overworld_RandomDungeons.rb',428,450,'generate seed selection/consumption/early return'),
 'lottery':('017_Minigames/005_Minigame_Lottery.rb',1,46,'date seed/random/reset and variable consumers'),
 'record':('011_Battle/008_Other battle types/005_RecordedBattle.rb',15,192,'recording initial attributes/random output and playback index'),
 'metadata':('012_Overworld/002_Overworld_Metadata.rb',1,183,'persistent global/map metadata, encounter version, clear/updateMap'),
 'world_entry':('012_Overworld/001_Overworld.rb',224,238,'on_enter_map setup_new_map'),
 'mapfactory':('004_Game classes/005_Game_MapFactory.rb',17,38,'setup/current-map read'),
 'mapnotify':('004_Game classes/005_Game_MapFactory.rb',142,153,'leave/enter/spriteset notification'),
 'directories':('001_Technical/002_Files/001_FileTests.rb',1,107,'Dir helpers/safe wrappers/safeGlob'),
 'resources':('001_Technical/002_Files/001_FileTests.rb',109,273,'canonicalize/RTP/resource extensions'),
 'file':('001_Technical/002_Files/001_FileTests.rb',275,361,'archive-aware exists/open/first/full reads'),
 'stream':('001_Technical/002_Files/001_FileTests.rb',366,484,'StringInput stateful operations'),
 'binary':('001_Technical/002_Files/002_FileMixins.rb',1,149,'small integer and indexed-entry read/write integration'),
 'copy_move':('001_Technical/002_RubyUtilities.rb',141,171,'File.copy/move'),
 'http':('001_Technical/002_Files/003_HTTP_Utilities.rb',1,83,'GET/POST and convenience wrappers'),
 'errors':('001_Technical/001_Debugging/003_Errors.rb',1,94,'exception presentation and critical wrapper'),
 'critical':('001_Technical/001_Debugging/003_Errors.rb',76,94,'pbCriticalCode completion/propagation'),
 'debug':('001_Technical/001_Debugging/001_PBDebug.rb',1,77,'ordinary-exception wrapper/log/flush/dump'),
 'console':('001_Technical/001_Debugging/002_DebugConsole.rb',1,233,'output gates/input/formatting'),
 'validation':('001_Technical/001_Debugging/004_Validation.rb',1,31,'class/any-class/responds-to validation'),
 'deprecation':('001_Technical/001_Debugging/005_Deprecation.rb',1,52,'warn/alias creation and dispatch'),
 'variables':('004_Game classes/001_Switches and Variables/003_Game_Variables.rb',1,25,'variable defaults/read/write'),
 'switches':('004_Game classes/001_Switches and Variables/002_Game_Switches.rb',1,25,'switch defaults/read/write'),
 'selfswitches':('004_Game classes/001_Switches and Variables/004_Game_SelfSwitches.rb',1,24,'self-switch defaults/read/write'),
 'varhelpers':('019_Utilities/001_Utilities.rb',509,520,'pbGet/pbSet'),
 'system':('004_Game classes/002_Game_System.rb',1,40,'system persistent field defaults'),
 'timer':('004_Game classes/002_Game_System.rb',274,287,'timer and update'),
 'temp':('004_Game classes/001_Switches and Variables/001_Game_Temp.rb',1,94,'temporary field defaults and mart-price reset'),
 'berry':('012_Overworld/006_Overworld_BerryPlants.rb',437,471,'pick berry stats'),
 'trade':('016_UI/001_Non-interactive UI/005_UI_Trading.rb',217,243,'trade counter before target validation'),
 'mart':('016_UI/020_UI_PokeMart.rb',598,715,'buy/sell/bonus item statistics'),
 'bp':('016_UI/021_UI_BattlePointShop.rb',453,504,'buy statistics'),
 'hall':('016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb',244,261,'read-only time display'),
 'phone_add':('013_Items/004_Item_Phone.rb',17,210,'contact lookup/add and class-level wrappers'),
 'daycare':('012_Overworld/007_Overworld_DayCare.rb',259,342,'slot defaults/filled/MAX_SLOTS=2'),
 'berry_init':('012_Overworld/006_Overworld_BerryPlants.rb',1,33,'berry default fields'),
}
def anchors(keys):
 if isinstance(keys,str):keys=keys.split()
 return [{'path':S+A[k][0],'version':RV,'lines':[A[k][1],A[k][2]],'entry':A[k][3]} for k in keys]
# Manually selected source groups for every current formal section; splitting into units below is formatting only.
M={
 'wp05-events-extensions-plugins.md':[(1,20,'events handlers menus plugin_reg plugin_meta plugin_load'),(22,33,'events handlers'),(34,39,'collections steps'),(41,47,'events collections steps errors main'),(49,54,'menus'),(56,80,'plugin_reg plugin_meta directories'),(82,103,'plugin_meta plugin_load main'),(105,118,'events plugin_reg plugin_error plugin_load errors'),(120,141,'plugin_reg plugin_load events collections')],
 'wp06-time-random-steps-stats.md':[(1,21,'calendar playtime steps rand record'),(23,50,'calendar phone_time phone_frame playtime start scene_title'),(52,72,'timers variables default_values'),(74,87,'steps movement_stats'),(89,99,'stats default_values'),(101,111,'rand phone_time dungeon lottery'),(113,123,'dungeon metadata default_values'),(125,129,'record'),(131,142,'anti rand'),(144,158,'metadata default_values start calendar'),(159,174,'calendar stats steps timers anti dungeon record')],
 'wp07-diagnostics-files-http.md':[(1,19,'file http errors debug'),(21,27,'directories'),(29,39,'file resources stream'),(41,46,'resources'),(48,52,'savefile plugin_load errors debug http'),(54,65,'http'),(67,81,'http'),(83,90,'errors plugin_error'),(92,96,'debug console'),(98,105,'main errors emergency'),(107,119,'file http errors plugin_reg debug'),(121,143,'file http errors debug deprecation')],
 'wp07-deprecation-appendix.md':[(1,15,'deprecation console validation'),(17,26,'deprecation console'),(28,33,'deprecation validation'),(35,44,'deprecation console validation'),(46,54,'deprecation validation')],
 'wp09-save-startup-continue.md':[(1,19,'values default_values start'),(21,42,'values'),(44,57,'values'),(59,81,'default_values'),(83,94,'main start load_ui'),(96,96,'start world_entry metadata mapfactory mapnotify'),(98,103,'values default_values start'),(105,117,'save savefile playtime'),(119,128,'savefile convert load_ui'),(130,145,'start savefile values load_ui'),(147,163,'values default_values start savefile convert')],
 'wp10-migration-failure-recovery.md':[(1,19,'convert conversion_data savefile emergency'),(21,32,'convert'),(34,38,'convert plugin_reg'),(40,47,'savefile values default_values'),(49,76,'convert savefile'),(78,99,'conversion_data'),(101,109,'conversion_data playtime'),(111,122,'start load_ui savefile'),(124,128,'emergency save'),(130,135,'main errors emergency plugin_load'),(137,140,'start'),(142,158,'convert conversion_data emergency start'),(160,175,'convert conversion_data savefile start')]
}
CONV={
 'v20_fix_planted_berry_numerical_ids':(6,97),'v20_refactor_planted_berries_data':(101,141),'v20_refactor_follower_data':(145,165),'v20_refactor_day_care_variables':(169,203),'v20_rename_bag_variables':(207,230),'v20_increment_player_character_id':(234,240),'v20_add_pokedex_records':(244,259),'v20_add_new_default_options':(263,270),'v20_fix_default_weather_type':(274,282),'v20_add_stats':(286,297),'v20_convert_pokemon_markings':(301,351),'v21_replace_phone_data':(355,381),'v21_replace_flute_booleans':(385,408),'v21_add_bump_stat':(412,420)}
def units(lines):
 out=[];buf=[];start=0;section='preamble'
 def flush():
  nonlocal buf
  if buf:out.append((start,start+len(buf)-1,section,'paragraph','\n'.join(buf)));buf=[]
 for i,line in enumerate(lines,1):
  if not line.strip():flush();continue
  if line.startswith('#'):
   flush();section=line.lstrip('# ').strip();out.append((i,i,section,'section_heading',line));continue
  if line.startswith('|'):
   flush()
   if not re.fullmatch(r'[| :\-]+',line):out.append((i,i,section,'table_row',line))
   continue
  if line.startswith(('- ','1. ','2. ','3. ','4. ','5. ','6. ','7. ','8. ','9. ')):
   flush();out.append((i,i,section,'clause',line));continue
  if not buf:start=i
  buf.append(line)
 flush();return out
# All writer statements were located, then their control ranges were read manually and entered in reading-coverage.
source_rows=json.loads((P/'reading-coverage.json').read_text())['sources']
field_sources={}
stats_path=R/S/'004_Game classes/012_Game_Stats.rb'
stats_lines=stats_path.read_text().splitlines()
for i,line in enumerate(stats_lines,1):
 if i>193:break
 for field in re.findall(r':([a-z_]+)',line.split('#')[0]) if re.search(r'attr_(?:accessor|writer)',line) else []:
  field_sources[field]=[{'path':S+'004_Game classes/012_Game_Stats.rb','version':RV,'lines':[i,i],'entry':'field declaration '+field}]
for field,arr in field_sources.items():
 for i,line in enumerate(stats_lines,1):
  if re.search('@'+re.escape(field)+r'\s*=',line):arr.append({'path':S+'004_Game classes/012_Game_Stats.rb','version':RV,'lines':[i,i],'entry':'initialization/setter '+field})
 for src in source_rows:
  path=R/src['path']
  if not path.is_file():continue
  for i,line in enumerate(path.read_text().splitlines(),1):
   if re.search(r'\$stats\.'+re.escape(field)+r'\s*(?:\+=|-=|=(?!=))',line):
    reviewed=next((x for x in src['segments'] if x['lines'][0]<=i<=x['lines'][1]),None)
    if reviewed:arr.append({'path':src['path'],'version':RV,'lines':reviewed['lines'],'entry':field+' writer at line '+str(i),'rule':reviewed['semantic_rules']})
# statistics time methods/source conversions are indirect writes rather than $stats setters
for field in ('play_time','time_last_saved','play_sessions'):
 field_sources[field]+=anchors('playtime start')
for field in ('times_to_get_badges','time_to_enter_hall_of_fame'):
 field_sources[field]+=anchors('playtime')
FIND_BY_FILE={'wp09-save-startup-continue.md':['GR5-M02-001'],'wp05-events-extensions-plugins.md':['GR5-M02-002'],'wp07-diagnostics-files-http.md':['GR5-M02-003','GR5-M02-005'],'wp10-migration-failure-recovery.md':['GR5-M02-004']}
for file,maps in M.items():
 path=F+'generic-kernel/'+file;lines=Path(path).read_text().splitlines();clauses=[]
 for lo,hi,section,kind,txt in units(lines):
  row=next((x for x in maps if x[0]<=lo<=x[1]),maps[-1]);aa=anchors(row[2]);result='supported_static: current stated behavior within conditions; no execution or host guarantee'
  finding_ids=[]
  for key,span in CONV.items():
   if key in txt:
    aa=[{'path':S+'002_Save data/005_Game_SaveConversions.rb','version':RV,'lines':list(span),'entry':key}]
    if key in list(CONV)[:2]:result='partial: summary supported_static; compatibility data/shape detail candidate GR5-M02-004';finding_ids=['GR5-M02-004']
  if file=='wp05-events-extensions-plugins.md' and lo==31:result='partial: selection and identity normalization supported_static; removal/clear distinction candidate GR5-M02-002';finding_ids=['GR5-M02-002']
  if file=='wp07-diagnostics-files-http.md' and lo==36:result='partial: stated open/path behavior supported_static; returned stream contract candidate GR5-M02-003';finding_ids=['GR5-M02-003']
  if file=='wp07-diagnostics-files-http.md' and lo in [90,102]:result='partial: exception/signals supported_static; completion outcome candidate GR5-M02-005';finding_ids=['GR5-M02-005']
  if kind=='section_heading' or lo<5:result='scope/organization/evidence-boundary; not an independent behavior claim'
  clauses.append({'section_or_vector':section,'lines':[lo,hi],'unit_kind':kind,'current_unit':txt,'source_anchors':aa,'result':result,'related_findings':finding_ids})
 entry={'path':path,'version':B,'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'review_extent':'full','material_availability':'available_text','evidence_level':'static_semantic_comparison','clauses':clauses,'effective_supplements':[],'unreviewed_intervals':[],'whole_module_runtime_signed':False}
 if file in ['wp06-time-random-steps-stats.md','wp07-diagnostics-files-http.md']:
  entry['effective_supplements'].append({'path':'review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M02/evidence/probe-result-v2.json','version':'130452d902530140331c21064a3188b7887f72ae','role':'historical bounded isolated receipt only; read, not rerun; not evidence of GR5 execution or host behavior'})
 if file=='wp06-time-random-steps-stats.md':entry['effective_supplements'] += [{'path':F+'generic-kernel/wp06-stats-directory.md','version':B,'role':'current 74-field appendix'},{'path':F+'engine-overworld/wp59-world-time-weather-field-moves.md','version':B,'lines':[22,99],'role':'complete calendar/tone data projection'}]
 if file=='wp07-deprecation-appendix.md':entry['effective_supplements'] += [{'path':'audit/source-traceability.md','version':B,'lines':[419,430],'role':'source navigation; old PASS not reused'},{'path':F+'user-interface/wp63-pokegear-map-music-and-phone.md','version':B,'lines':[93,125],'role':'18 concrete deprecated phone consumers, distinct from alias constructor'}]
 if file=='wp09-save-startup-continue.md':entry['effective_supplements'] += [{'path':F+'engine-overworld/wp11-map-topology-transfer.md','version':B,'lines':[101,138],'role':'world recovery projection'},{'path':F+'engine-overworld/wp13-map-events-npc-followers.md','version':B,'lines':[48,64],'role':'event instance vs persistent local records'}]
 mutate('spec-to-source','specifications',entry,'path')
# Current stats directory: every field row receives actual declaration/default/writer anchors.
for path in [F+'generic-kernel/wp06-stats-directory.md','specs/kernel/wp06-stats-directory.md']:
 lines=Path(path).read_text().splitlines();cs=[]
 for lo,hi,section,kind,txt in units(lines):
  field=next((f for f in field_sources if re.match(r'\|\s*'+re.escape(f)+r'\s*\|',txt)),None)
  aa=field_sources[field] if field else anchors('stats default_values')
  result='supported_static field initialization, persistence, and stated update category; finite writer control ranges read'
  if field in ['poke_center_count','revived_fossil_count','lottery_prize_count','drinks_bought','drinks_won','gym_leader_attempts','elite_four_attempts','hall_of_fame_entry_count']:result='unresolved: declaration/default/comment supported_static; absent NPC/map event writer remains material gap U01'
  if field=='battle_points_won':result='unresolved: declaration/default known; writer not located, not inferred absent or necessarily event-owned'
  if field in ['times_to_get_badges','time_to_enter_hall_of_fame']:result='supported_static setter rule only; caller/demo reachability unresolved'
  cs.append({'section_or_vector':field or section,'lines':[lo,hi],'unit_kind':kind,'current_unit':txt,'source_anchors':aa,'result':result})
 mutate('spec-to-source','specifications',{'path':path,'version':B,'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'review_extent':'full','material_availability':'available_text','evidence_level':'static_semantic_comparison','clauses':cs,'effective_supplements':[{'path':F+'generic-kernel/wp10-migration-failure-recovery.md','version':B,'lines':[101,109],'role':'old frame-count conversion time boundary'},{'path':'audit/source-traceability.md','version':B,'lines':[393,404],'role':'navigation only; field count not semantic proof'}],'unreviewed_intervals':[]},'path')
# Every owned test ID, with no WP08/LZ sign-off.
test_groups={
 'EP':[(1,2,'events'),(3,3,'events handlers menus'),(4,5,'handlers'),(6,7,'plugin_meta directories'),(8,8,'plugin_reg'),(9,11,'plugin_reg plugin_meta'),(12,12,'plugin_reg'),(13,15,'plugin_reg plugin_load'),(16,17,'plugin_load'),(18,21,'plugin_meta directories plugin_load'),(22,25,'events collections errors'),(26,27,'events collections steps')],
 'TM':[(1,1,'calendar'),(2,3,'phone_time phone_frame'),(4,4,'playtime start scene_title'),(5,5,'lottery rand'),(6,6,'dungeon metadata'),(7,7,'record'),(8,8,'stats start'),(9,9,'berry'),(10,10,'mart bp'),(11,11,'playtime hall'),(12,12,'steps'),(13,13,'trade'),(14,14,'calendar'),(15,19,'timers variables'),(20,23,'anti rand')],
 'IO':[(1,5,'http'),(6,7,'file'),(8,8,'errors main'),(9,9,'main'),(10,10,'main emergency'),(11,11,'errors plugin_load'),(12,12,'errors plugin_error'),(13,15,'directories'),(16,20,'http')],
 'DP':[(1,2,'deprecation console'),(3,5,'deprecation validation')],
 'SV':[(1,2,'load_ui start'),(3,6,'start mapfactory mapnotify'),(7,7,'values default_values start'),(8,9,'values'),(10,11,'save savefile'),(12,17,'values save savefile')],
 'MG':[(1,1,'plugin_reg convert'),(2,2,'convert'),(3,3,'savefile values default_values'),(4,5,'convert savefile'),(6,8,'emergency save'),(9,9,'conversion_data daycare'),(10,10,'conversion_data phone_add start'),(11,12,'start'),(13,16,'conversion_data playtime')]
}
tp=F+'test-catalog/generic-kernel-wp05-06-07-08-09-10.md';cs=[]
for i,line in enumerate(Path(tp).read_text().splitlines(),1):
 m=re.match(r'\|\s*(EP|TM|IO|DP|SV|MG)(\d+)\s*\|',line)
 if m:
  family,num=m[1],int(m[2]);g=next(x for x in test_groups[family] if x[0]<=num<=x[1])
  item={'section_or_vector':family+m[2],'lines':[i,i],'unit_kind':'test_vector','current_unit':line,'source_anchors':anchors(g[2]),'result':'supported_static for explicitly stated preconditions; NOT_EXECUTED_THIS_REVIEW','execution_status':'NOT_EXECUTED_THIS_REVIEW'}
  if family=='IO' and num>=16:item['historical_evidence_boundary']='R4 Ruby 2.6.10p210 isolated receipt read; exact host behavior UNVERIFIED; supplementary static controls separated'
  cs.append(item)
 elif '| U02-SV-WORLD' in line:
  cs.append({'section_or_vector':line.split('|')[1].strip(),'lines':[i,i],'unit_kind':'test_vector','current_unit':line,'source_anchors':anchors('start metadata world_entry mapfactory mapnotify events'),'result':'supported_static bounded M02 projection only; M03 owns world lifecycle','execution_status':'NOT_EXECUTED_THIS_REVIEW'})
mutate('spec-to-source','specifications',{'path':tp,'version':B,'sha256':hashlib.sha256(Path(tp).read_bytes()).hexdigest(),'review_extent':'partial','material_availability':'available_text','evidence_level':'static_semantic_comparison','clauses':cs,'owned_vectors':len(cs),'effective_supplements':[],'unreviewed_intervals':[[110,154]],'boundary':'WP08/LZ01–LZ35 belongs to M01; no full shared catalog signoff. Preamble and family notes read as evidence boundaries.'},'path')
# Companion extraction texts: every section/paragraph/table unit read; old status/earlier vectors do not overrule final formal text.
for file in M:
 path='specs/kernel/'+file
 if not Path(path).exists():continue
 cs=[]
 for lo,hi,sec,kind,txt in units(Path(path).read_text().splitlines()):
  if 'wp05' in file:
   keys='events handlers collections' if '3.' in sec else 'menus' if '4.' in sec else 'plugin_reg plugin_meta' if '5.' in sec else 'plugin_load main' if '6.' in sec else 'events handlers menus plugin_reg plugin_meta plugin_load'
  elif 'wp06' in file:keys='calendar playtime phone_time phone_frame' if '3.' in sec else 'stats steps movement_stats' if '4.' in sec else 'rand dungeon lottery record' if '5.' in sec else 'stats start default_values calendar'
  elif 'deprecation' in file:keys='deprecation validation console'
  elif 'wp07' in file:keys='directories file resources' if '3.' in sec else 'http' if '4.' in sec else 'errors debug console main'
  elif 'wp09' in file:keys='values default_values' if '3.' in sec else 'main start load_ui' if '4.' in sec else 'savefile save playtime' if '5.' in sec else 'values default_values start savefile load_ui'
  else:keys='convert savefile plugin_reg' if '3.' in sec else 'conversion_data' if '4.' in sec else 'start load_ui emergency errors main' if '5.' in sec else 'convert conversion_data start savefile'
  aa=anchors(keys)
  for key,span in CONV.items():
   if key in txt:aa=[{'path':S+'002_Save data/005_Game_SaveConversions.rb','version':RV,'lines':list(span),'entry':key}]
  cs.append({'section_or_vector':sec,'lines':[lo,hi],'unit_kind':kind,'current_unit':txt,'source_anchors':aa,'result':'companion extraction read and compared; current final formal clauses control; historical PASS/status not reused','formal_counterpart':F+'generic-kernel/'+file})
 mutate('spec-to-source','specifications',{'path':path,'version':B,'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'review_extent':'full','material_availability':'available_text','evidence_level':'static_semantic_comparison_of_companion','clauses':cs,'effective_supplements':[],'unreviewed_intervals':[],'role':'companion source-traceability text; no reopening based solely on old management status or superseded vectors'},'path')
print('Formal and companion documents mapped; owned shared-catalog vectors',len(next(x for x in json.loads((P/'spec-to-source.json').read_text())['specifications'] if x['path']==tp)['clauses']))
