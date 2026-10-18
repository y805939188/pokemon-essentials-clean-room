"""Assemble locators for already personally read units. This script is NOT a semantic reviewer.
The human notes and explicit topic joins below are the decisions; text splitting only gives
stable paragraph/table-cell denominators, not independent proof or execution credit.
"""
import json,re,hashlib,datetime,subprocess
from pathlib import Path
B=Path(__file__).parent
I=json.loads((B/'identities.json').read_text()); IDS={f['id']:f for f in I['files']}
L=json.loads((B/'reading-ledger.json').read_text()); now=datetime.datetime.now(datetime.timezone.utc).isoformat()
# Manually chosen source-topic joins from the actual complete reading. Ranges are inclusive.
T={
'entry': [('R12',1,425),('R13',1,264)],
'world': [('R13',1,264),('R14',1,227)],
'daycare':[('R14',229,376)], 'roam':[('R14',378,548),('R13',266,543)],
'player':[('R13',839,1143)],'party':[('R13',545,767),('R18',1091,1151)],'bag':[('R13',769,837)],
'pokemon':[('R18',1,1151)],'battle_test':[('R13',266,543),('R14',741,869)],
'battle_observe':[('R12',181,406),('R15',1,226)],'battle_edit':[('R16',1,876)],
'effects':[('R17',1,452),('R15',423,490)],'environment':[('R15',228,421)],
'logging':[('R13',266,543)],'tools':[('R13',1145,1496)],
'properties':[('R11',1,1706),('R05',1,14),('R05',64,410),('R20',1,647)],
'trainer_type':[('R01',342,443)],'trainer':[('R01',445,687)],'item':[('R01',819,921)],
'species':[('R01',923,987)],'metadata':[('R01',689,817)],'dex':[('R01',989,1247)],
'connections':[('R03',1,578)],'terrain':[('R02',1,263)],'encounter':[('R01',1,340)],
'metrics':[('R04',1,411)],'tiles':[('R14',665,739)],
'anim_entry':[('R10',928,1170)],'canvas':[('R06',1,1012)],'controls':[('R07',1,942)],
'anim_props':[('R10',185,371)],'anim_frames':[('R06',513,694),('R10',68,183),('R10',679,752)],
'anim_list':[('R10',1,183)],'anim_paths':[('R08',1,436)],'anim_tween':[('R10',754,927)],
'anim_timing':[('R10',373,677)],'anim_preview':[('R06',451,511)],
'anim_single':[('R09',1,84)],'anim_organizer':[('R01',1249,1324)],
'anim_batch':[('R14',550,663),('R05',16,62)],'anim_old':[('R09',86,147)],
'animmaker':[('R21',1,26)], 'extendtext':[('R22',1,4)],
'compiler':[], 'rename':[('R19',1,89)],'scripts':[('R23',1,183),('R24',1,183)],'townmap':[('R25',1,414)],
'generator':[], 'demo':[]}
# Dependency facts below were read personally unless a finite received packet names its original reader.
D={
'entry':['003_Game processing/002_Scene_Map.rb','016_UI/001_UI_PauseMenu.rb','016_UI/013_UI_Load.rb','011_Battle/004_Scene/003_Scene_ChooseCommands.rb'],
'world':['004_Game classes/004_Game_Map.rb','004_Game classes/001_Switches and Variables/003_Game_Variables.rb','019_Utilities/001_Utilities.rb'],
'daycare':['012_Overworld/007_Overworld_DayCare.rb','016_UI/005_UI_Party.rb','019_Utilities/001_Utilities.rb'],
'roam':[], 'player':['015_Trainers and player/004_Player.rb','015_Trainers and player/005_Player_Pokedex.rb'],
'party':['014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb','019_Utilities/002_Utilities_Pokemon.rb','014_Pokemon/001_Pokemon.rb'],
'bag':['013_Items/008_PokemonBag.rb'], 'pokemon':['014_Pokemon/001_Pokemon.rb','014_Pokemon/003_Pokemon_ShadowPokemon.rb','014_Pokemon/004_Pokemon_Move.rb','014_Pokemon/005_Pokemon_Owner.rb','015_Trainers and player/005_Player_Pokedex.rb','013_Items/001_Item_Utilities.rb'],
'battle_test':['015_Trainers and player/001_Trainer.rb','015_Trainers and player/002_Trainer_LoadAndNew.rb'],
'battle_observe':[], 'battle_edit':['011_Battle/002_Battler/001_Battle_Battler.rb','011_Battle/002_Battler/002_Battler_Initialize.rb','011_Battle/002_Battler/003_Battler_ChangeSelf.rb','014_Pokemon/001_Pokemon.rb','015_Trainers and player/005_Player_Pokedex.rb'],
'effects':['007_Objects and windows/011_Messages.rb'], 'environment':['007_Objects and windows/011_Messages.rb'],
'logging':['001_Technical/001_Debugging/001_PBDebug.rb','001_Technical/001_Debugging/003_Errors.rb'],
'properties':['007_Objects and windows/011_Messages.rb','010_Data/001_GameData.rb'],
'trainer_type':['010_Data/002_PBS data/014_TrainerType.rb','021_Compiler/003_Compiler_WritePBS.rb'],
'trainer':['010_Data/002_PBS data/015_Trainer.rb','021_Compiler/002_Compiler_CompilePBS.rb','021_Compiler/003_Compiler_WritePBS.rb'],
'item':['010_Data/002_PBS data/006_Item.rb','021_Compiler/003_Compiler_WritePBS.rb'],
'species':['010_Data/002_PBS data/008_Species.rb','021_Compiler/002_Compiler_CompilePBS.rb','021_Compiler/003_Compiler_WritePBS.rb'],
'metadata':['010_Data/002_PBS data/016_Metadata.rb','010_Data/002_PBS data/017_PlayerMetadata.rb','010_Data/002_PBS data/018_MapMetadata.rb','021_Compiler/003_Compiler_WritePBS.rb'],
'dex':['010_Data/002_PBS data/008_Species.rb','010_Data/002_PBS data/001_MiscPBSData.rb','021_Compiler/002_Compiler_CompilePBS.rb','021_Compiler/003_Compiler_WritePBS.rb'],
'connections':['021_Compiler/002_Compiler_CompilePBS.rb','021_Compiler/003_Compiler_WritePBS.rb'],
'encounter':['010_Data/002_PBS data/013_Encounter.rb','010_Data/001_Hardcoded data/013_EncounterType.rb','021_Compiler/002_Compiler_CompilePBS.rb','021_Compiler/003_Compiler_WritePBS.rb','012_Overworld/002_Overworld_Metadata.rb'],
'metrics':['010_Data/002_PBS data/010_SpeciesMetrics.rb','010_Data/001_GameData.rb','021_Compiler/003_Compiler_WritePBS.rb'],
'anim_preview':['011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb'],
'anim_old':['011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb'],
'compiler':['021_Compiler/001_Compiler.rb','021_Compiler/002_Compiler_CompilePBS.rb','021_Compiler/003_Compiler_WritePBS.rb','021_Compiler/004_Compiler_MapsAndEvents.rb','004_Game classes/011_Game_FollowerFactory.rb','012_Overworld/001_Overworld.rb','004_Game classes/005_Game_MapFactory.rb','004_Game classes/006_Game_Character.rb','003_Game processing/003_Interpreter.rb','003_Game processing/004_Interpreter_Commands.rb'],
'rename':['021_Compiler/004_Compiler_MapsAndEvents.rb','001_Technical/002_RubyUtilities.rb'],
'generator':['018_Alternate battle modes/003_Battle Frontier generator/','018_Alternate battle modes/002_Battle Frontier rules/','018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb','018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb','011_Battle/004_Scene/009_Battle_DebugScene.rb','019_Utilities/001_Utilities.rb','014_Pokemon/001_Pokemon.rb'],
'demo':['PBS/metadata.txt','PBS/map_metadata.txt','PBS/map_connections.txt','PBS/encounters.txt','PBS/trainers.txt','PBS/battle_facility_lists.txt','PBS/dungeon_parameters.txt','PBS/town_map.txt','PBS/phone.txt','PBS/pokemon.txt','010_Data/002_PBS data/020_DungeonParameters.rb','010_Data/001_Hardcoded data/007_Evolution.rb','013_Items/004_Item_Phone.rb','016_UI/009_UI_RegionMap.rb','019_Utilities/002_Utilities_Pokemon.rb','012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb']}
# Every formal section was read in full. These are hand-selected topic contexts, not keyword inference.
S={
'F01':[(1,26,['entry']),(27,53,['entry']),(54,62,['world']),(63,68,['world']),(69,75,['world']),(76,82,['daycare']),(83,88,['roam']),(89,97,['roam','logging','encounter']),(98,111,['player']),(112,121,['party']),(122,127,['bag']),(128,176,['pokemon']),(177,188,['battle_test']),(189,195,['battle_observe']),(196,211,['battle_edit']),(212,218,['effects']),(219,230,['environment','battle_observe']),(231,240,['logging']),(241,246,['pokemon','battle_edit','properties']),(247,276,['tools']),(277,306,['entry','properties','pokemon','battle_edit','tools']),(307,451,['effects'])],
'F02':[(1,35,['properties']),(36,46,['properties']),(47,54,['properties']),(55,62,['properties']),(63,76,['properties']),(77,85,['trainer_type']),(86,109,['trainer']),(110,132,['item']),(133,152,['species']),(153,157,['metadata']),(158,169,['dex']),(170,176,['properties']),(177,192,['trainer','item','species','metadata','dex']),(193,198,['tools']),(199,225,['properties','trainer','item','species','metadata','dex'])],
'F03':[(1,27,['connections','terrain','encounter','metrics']),(28,50,['connections']),(51,56,['metadata']),(57,66,['terrain']),(67,119,['encounter']),(120,147,['metrics']),(148,168,['metrics']),(169,175,['tiles']),(176,220,['connections','terrain','encounter','metrics','tiles'])],
'F04':[(1,76,['anim_entry','canvas','anim_single','anim_batch']),(77,134,['canvas']),(135,159,['anim_props']),(160,202,['anim_frames','canvas']),(203,222,['anim_list']),(223,232,['canvas']),(233,244,['anim_frames']),(245,276,['anim_tween']),(277,296,['anim_paths']),(297,322,['anim_timing']),(323,355,['anim_preview','anim_timing']),(356,367,['anim_single']),(368,374,['anim_organizer']),(375,402,['anim_batch']),(403,416,['anim_old']),(417,423,['compiler']),(424,447,['anim_entry','anim_single','anim_batch','compiler']),(448,459,['controls']),(460,489,['animmaker']),(490,521,['canvas','anim_frames','anim_paths','anim_timing','anim_single','anim_batch','animmaker'])],
'F05':[(1,32,['compiler','rename','scripts','townmap','extendtext']),(33,55,['compiler','scripts','townmap']),(56,299,['compiler']),(300,308,['rename']),(309,360,['scripts']),(361,388,['townmap']),(389,409,['extendtext']),(410,437,['compiler']),(438,460,['compiler','rename','scripts','townmap','extendtext'])],
'F06':[(1,279,['generator'])], 'F07':[(1,230,['demo'])],
'F08':[(1,76,['entry','world','daycare','roam','player','party','bag','pokemon','battle_test','battle_observe','battle_edit','effects','environment','logging','tools']),(77,116,['properties','trainer_type','trainer','item','species','metadata','dex']),(117,153,['connections','terrain','encounter','metrics','tiles']),(154,193,['canvas','anim_props','anim_frames','anim_list','anim_paths','anim_tween','anim_timing','anim_preview','anim_single','anim_organizer','anim_batch','anim_old','controls','compiler']),(194,230,['compiler','rename','scripts','townmap','extendtext']),(231,261,['generator']),(262,284,['demo']),(285,294,['generator']),(295,317,['entry','daycare','battle_edit','pokemon','properties','trainer','item','species','metrics','encounter','effects']),(318,344,['canvas','anim_frames','anim_preview','anim_paths','anim_timing','anim_batch','anim_organizer','compiler','scripts','demo','pokemon']),(345,356,['scripts','compiler']),(357,359,['trainer_type','trainer','item']),(360,361,['item']),(362,364,['pokemon','battle_edit']),(365,376,['dex']),(377,390,['compiler','dex','connections','anim_entry']),(391,410,['extendtext']),(411,433,['animmaker'])]}
# More exact cross-owner vector joins, personally rechecked by ID, including all conditions/counters on that line.
VS={291:['generator'],292:['pokemon'],293:['generator'],301:['entry','party'],302:['daycare'],303:['battle_edit'],304:['battle_edit','pokemon'],305:['player'],306:['properties'],307:['properties'],308:['properties','metadata'],309:['properties','trainer'],310:['species'],311:['trainer','properties'],312:['encounter'],313:['encounter'],314:['metrics'],315:['effects'],316:['item','properties'],317:['properties'],325:['canvas'],326:['anim_batch','compiler','demo'],327:['compiler'],328:['anim_single','anim_batch','anim_list','anim_timing'],329:['scripts'],330:['canvas','anim_frames','anim_old'],331:['anim_preview','anim_timing'],332:['compiler'],333:['demo'],334:['pokemon'],335:['compiler'],336:['anim_organizer'],337:['anim_paths','canvas'],338:['canvas'],339:['compiler'],340:['compiler'],341:['demo'],342:['anim_paths'],343:['compiler']}

def topics(fid,n):
 if fid=='F08' and n in VS:return VS[n]
 for a,b,t in S[fid]:
  if a<=n<=b:return t
 raise ValueError((fid,n))
# Source facts preserve the human notes already written at actual first-reading time.
facts=[]
for e in L['entries']:
 if not e['file_id'].startswith('R'):continue
 fid=e['file_id'];a,b=e['lines'];ft=[]
 for topic,spans in T.items():
  if any(x==fid and not (b<lo or a>hi) for x,lo,hi in spans):ft.append(topic)
 fact={'id':f'DEV-SRC-{len(facts)+1:03d}','source':{'file_id':fid,'lines':[a,b],'identity':e['source_identity']},'actual_reader':'/root/developer_full_cloud','original_read_utc':e['utc'],'fact':e['semantic_note'],'topics':ft,'evidence_level':'SOURCE_STATIC','disposition':'SUPPORTED_SCOPE_JOIN' if ft else 'READ_INTERNAL_OR_UNUSED_HELPER','premise':'The stated branch is reached with its explicit legal arguments and preceding steps normal. No source bug is silently repaired; No/BACK and exceptional exits stay separate.','runtime':'NOT_EXECUTED'}
 if fid=='R01' and a==1204:fact['disposition']='UNUSED_DIAGNOSTIC_HELPERS_READ';fact['scope_reason']='Complete helper definitions read; actual regional editor uses GameData::Species.get_evolutions family graph. No default caller of these legacy helper definitions is inferred, and no future API requirement follows.'
 facts.append(fact)
# Personally written dependency statements; identities are captured independently from their semantic reading.
for dep in json.loads((B/'manual-dependency-facts.json').read_text())['facts']:
 facts.append({'id':'DEV-DEP-'+dep['key'],'source':{'file_id':None,'path':dep['path'],'lines':dep['range'],'identity':dep['source_identity']},'actual_reader':dep['actual_reader'],'fact':dep['fact'],'topics':dep['topics'],'evidence_level':'SOURCE_STATIC','disposition':'PERSONALLY_READ_COMPLETE_CITED_UNITS','premise':dep['premise'],'failure_boundary':dep['failure_boundary'],'runtime':'NOT_EXECUTED'})
# Embedded payload and native evidence have their own bounded provenance; do not call original reader ourselves.
extra=[('DEV-LOADER','received/loader-Main.rb',['scripts'],'/root','Whole49-line decodedloader read; sortedfilesbeforefolders,caseinsensitive.rb,hiddenfileseligible/hiddendirsrejected;readoutsideevalrescue;ScriptErrornewclass;ordinarymessageattemptactual900threshold/logoverwrite;priorloadedprefixnotrolledback.'),('DEV-POSITIONS','received/tasks__core_atomic_reception__debug-position-producers.v1.json',['effects'],'/root/core_atomic_reception','Eight complete producer units; legal1v2 nil hole in both arrays at2 is skipped by R15 next if !position. No normal existing position with nil battler follows.'),('DEV-RECORDED','received/core_atomic_reception__recorded-command-consumers.v1.json',['generator'],'/root/core_atomic_reception','Complete Recorded287/baseCommand265/Start247–317; Recording inherits main loop/menu; controlPlayer sends both sides to AI; Playback loop is a separate consumer.'),('DEV-AN-CIL','received/preflight_resources__evidence__current-animmaker-cil.stdout',['animmaker'],'/root/preflight_resources','All15 CIL method bodies read personally with full metadata; full XML input stage before output, original pattern indices, n0 minimum canvas, per-file existence vs load failure, weak cache, no96 cap, Save(name) and finally prefixes.'),('DEV-EXT-TEXT','received/preflight_resources__current-programs-v2__extendtext-text-disassembly.txt',['extendtext'],'/root/preflight_resources','Entire native .text read with aligned40129c and imports/data; duplicate mutex0 vs failure−1; case-sensitive marker; four independent dialogs; unchecked geometry requests;150ms polling; no restoration.'),('DEV-NATIVE-FACTS','received/preflight-tools-selected-complete-objects.json',['animmaker','extendtext'],'/root/preflight_resources','All18 complete RES-AN/RES-EXT finite objects and premises/failure boundaries read; accepted only together with actual decoded body and identities, not the entire original729728B forward map.')]
for id,path,ts,orig,note in extra:
 raw=(B/path).read_bytes();facts.append({'id':id,'source':{'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},'actual_receiver':'/root/developer_full_cloud','original_reader':orig,'fact':note,'topics':ts,'evidence_level':'SOURCE_STATIC','disposition':'FINITE_RECEIVED_AND_RECHECKED','runtime':'NOT_EXECUTED'})
# Textual clauses: every nonempty semantic paragraph or table cell is a stable atom. Markdown headings/separators are typed context.
rev=[]
for fid,f in IDS.items():
 if not fid.startswith('F'):continue
 text=(Path(f['repo'])/f['path']).read_text().splitlines();heading='';tabhead=[]
 for n,line in enumerate(text,1):
  s=line.strip()
  if not s:continue
  typ='CLAUSE'
  if s.startswith('#'):heading=s;typ='STRUCTURAL_HEADING'
  elif re.match(r'^\|[\s|:\-]+\|$',s):typ='TABLE_SEPARATOR'
  elif s=='---':typ='FRONT_MATTER_SEPARATOR'
  ts=topics(fid,n)
  refs=[x['id'] for x in facts if set(x['topics'])&set(ts)]
  if s.startswith('|') and typ=='CLAUSE':
   cells=[x.strip() for x in s.strip('|').split('|')]
   if not tabhead or cells[0] in ['ID','条款','ID／所属发现','向量','前态／条件','ID／所属发现'] or n>1 and text[n-2].strip()=='':tabhead=cells;typ='TABLE_COLUMN_CONTEXT'
   atoms=[{'cell':i+1,'text':v,'subassertions':[p for p in re.split(r'[；。]',v) if p]} for i,v in enumerate(cells)]
  else:atoms=[{'text':s,'subassertions':[p for p in re.split(r'[；。]',s) if p]}]
  rev.append({'id':f'DEV-{fid}-L{n:03d}','file_id':fid,'lines':[n,n],'formal_identity':{'commit':f['commit'],'path':f['path'],'sha256':f['sha256'],'git_blob':f['git_blob']},'heading':heading,'kind':typ,'assertions':atoms,'topics':ts,'source_fact_ids':refs,'dependency_topics':ts,'status':'CONTEXT_READ' if typ!='CLAUSE' else 'READ_AND_STATICALLY_COMPARED','actual_reviewer':'/root/developer_full_cloud','premise':'Apply the full section premise and this row/paragraph explicit gates, normal/cancel/error/partial-prefix qualifications together. Legal data/resources and preceding operations normal are conditional premises, not observations.','evidence_level':'DERIVED_VECTOR' if fid=='F08' else 'SOURCE_STATIC','execution':'NOT_EXECUTED','comparison_note':'Read the whole containing document and complete primary source units; compared actual branch, defaults, write ordering, cancel/error exits and owner boundary. Source/dependency pointers are locators, not execution or independent approval.'})
# Exact 120 parameter rows: pair sequential registry rows only after actual manual layer/type/default/range/reset comparison.
r17=(Path(IDS['R17']['repo'])/IDS['R17']['path']).read_text().splitlines(); regs=[(i,s.strip()) for i,s in enumerate(r17,1) if re.match(r'^\s+PBEffects::\w+\s*=>',s)]
effects=[e for e in rev if e['file_id']=='F01' and re.match(r'^E\d{3}$',e['assertions'][0].get('text',''))] # table cells have first text
if len(effects)!=120 or len(regs)!=120:raise ValueError(('effects',len(effects),len(regs)))
for e,(ln,s) in zip(effects,regs):
 e['exact_registry_locator']={'file_id':'R17','lines':[ln,ln],'key':re.search(r'PBEffects::(\w+)',s).group(1)}
 e['checked_fields']=['layer','behavior','input kind','registered default','input bounds','ACTION reset']
 e['comparison_note']='All six fields personally compared, including omitted registry exclusions; defaults are interpreted by the complete editor. LastRoundFainted registered−2 is normalized to integer minimum/reset−1, not a battler reference.'
for fact in facts:
 fact['formal_clause_ids']=[e['id'] for e in rev if e['kind']=='CLAUSE' and set(e['topics'])&set(fact['topics'])]
 fact['consumer_dependency_topics']=fact['topics']
# Source syntax inventory is only a mechanical denominator. Each complete unit remains tied to the already-read parent fact.
units=[]
for fid,f in IDS.items():
 if not fid.startswith('R'):continue
 lines=(Path(f['repo'])/f['path']).read_text().splitlines();starts=[]
 for i,s in enumerate(lines,1):
  if re.match(r'^\s*(?:def |class |module |MenuHandlers\.add\(|[A-Z][A-Z_]+\s*=)',s):starts.append((i,s))
 if not starts:starts=[(1,'Entire text/document/browser program')]
 if fid=='R25':starts += [(i,s) for i,s in enumerate(lines,1) if re.match(r'^\s*(?:function |attachEvent\()',s)]
 for i,s in starts:
  indent=len(s)-len(s.lstrip());end=(len(lines) if s=='Entire text/document/browser program' else i)
  if fid=='R25' and s!='Entire text/document/browser program':end=next((j-1 for j,t in starts if j>i),len(lines))
  if s.lstrip().startswith(('def ','class ','module ')) and not re.search(r';.*\bend\s*$',s):
   end=next((j for j in range(i+1,len(lines)+1) if re.match(r'^'+' '*indent+r'end\s*$',lines[j-1])),len(lines))
  elif s.startswith('MenuHandlers.add('):end=next((j for j in range(i+1,len(lines)+1) if lines[j-1]=='})'),len(lines))
  elif re.match(r'^\s*[A-Z][A-Z_]+\s*=',s):end=next((j-1 for j,t in starts if j>i and len(t)-len(t.lstrip())<=indent),len(lines))
  parents=[fct['id'] for fct in facts if fct.get('source',{}).get('file_id')==fid and not(end<fct['source']['lines'][0] or i>fct['source']['lines'][1])]
  units.append({'id':f'DEV-UNIT-{fid}-{i:04d}','file_id':fid,'range':[i,end],'declaration':s.strip(),'denominator_only':True,'read':'FULL_READ_WITH_CONTAINING_PRIMARY','actual_reader':'/root/developer_full_cloud','manual_fact_ids':parents,'semantic_disposition':'See complete parent human facts and their clause joins. This inventory is not an independent semantic assertion.'})
(B/'forward-mapping.json').write_text(json.dumps({'schema':'gr8-forward/v2','reviewer':'/root/developer_full_cloud','recorded_utc':now,'method':'Actual human complete reading + explicit topic joins; script only assembles stable locators and denominators.','entries':facts,'syntax_units':units,'dependency_topics':D,'qualification':'All clauses are conditional static comparisons; host execution0. Every primary source line is covered by full-file reading; syntax units may overlap their enclosing class/module. No unit count certifies behavior.'},ensure_ascii=False,indent=2)+'\n')
(B/'reverse-mapping.json').write_text(json.dumps({'schema':'gr8-reverse/v2','reviewer':'/root/developer_full_cloud','recorded_utc':now,'entries':rev,'summary':{'nonempty_lines':len(rev),'semantic_clauses':sum(e['kind']=='CLAUSE' for e in rev),'table_cells':sum(len(e['assertions']) for e in rev if len(e['assertions'])>1),'subassertions':sum(len(a['subassertions']) for e in rev for a in e['assertions']),'effect_rows':len(effects)},'qualification':'Line/cell/subassertion enumeration is a bookkeeping denominator; complete manual reading and finite facts supply semantics. Cross-owner references grant only the named interface; no whole referenced specification approval.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'recorded_utc':now,'facts':len(facts),'syntax_units':len(units),'reverse':len(rev),'effect_rows':len(effects)}))
