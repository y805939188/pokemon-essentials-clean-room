"""Serialize manually completed static review notes; never executes reference code."""
from pathlib import Path
import json, hashlib, difflib, re, subprocess
P=Path(__file__).parent
W=Path.cwd()
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
RV='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BV='9366d9d17aaeac3b4414236468affa650fb3dd27'
FT='d5a462b4c6f8b78c3264a25d6b5495230fa265e2'
F=Path('deliverables/final-specification-set')
base=dict(schema_version='gr5.review.v1',module='M12',reviewer='M12B',source_baseline=RV,specification_baseline=BV,formal_tree=FT)
def save(name,obj): (P/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def lines(p): return p.read_text(encoding='utf-8-sig').splitlines()
def merge(ranges):
 out=[]
 for a,b in sorted(ranges):
  if out and a<=out[-1][1]+1:out[-1][1]=max(b,out[-1][1])
  else:out.append([a,b])
 return out
def gaps(ranges,n):
 out=[]; at=1
 for a,b in merge(ranges):
  if a>at:out.append([at,a-1])
  at=max(at,b+1)
 if at<=n:out.append([at,n])
 return out
def identity(p):
 b=p.read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
rc=json.loads((P/'reading-coverage.json').read_text())
rc['records']=[x for x in rc['records'] if x.get('assigned_role')=='primary']
rc.pop('specification_records',None)
# Existing primary entries contain the firsthand rule-by-rule semantic notes.
for row in rc['records']:
 if row.get('assigned_role')=='primary':
  row['review_extent']='full';row['remaining_review']='none within assigned static source body and necessary consumer scope';row['reviewer']='M12B'
  row['content_read_ranges']=[[1,row['total_lines']]];row['unreviewed_ranges']=[]
  for s in row['semantic_ranges']:
   s['comparison_result']='Compared to current complete main contract, all corresponding Demo/DX vectors, current original and applicable supplements; see linked capability and reverse-map units for result.'
 row.update(identity(R/row['path']))
secondary=[]
def add(p,rr,entry,rules,contracts,full=False,role='necessary_dependency'):
 p='Data/Scripts/'+p if not p.startswith(('Data/','PBS/')) else p
 n=len(lines(R/p));rr=merge([[a,min(b,n)] for a,b in rr]);g=gaps(rr,n)
 secondary.append(dict(path=p,version=RV,total_lines=n,reviewer='M12B',review_extent='full' if not g else 'partial',assigned_role=role,material_availability='available_text',evidence_level=['SOURCE_STATIC','SPEC_STATIC'],content_read_ranges=rr,semantic_ranges=[dict(lines=r,entry=entry,rules=rules,spec_anchors=contracts,comparison_result='Direct static read and behavioral comparison; no reference execution') for r in rr],unreviewed_ranges=g,unreviewed_scope='Unrelated body outside the stated dependency/counterevidence slice' if g else None,remaining_review='none within stated dependency slice',**identity(R/p)))
# Previous and current direct reads. A partial record never claims the omitted body was read.
add('010_Data/001_GameData.rb',[(1,260)],'register/query/default/PBS/save/load','Registration directly constructs records; required/optional lookup; no adapter for stale creation text fields; persistence serializes current table','WP73-A §§2/4/6; WP03/04; GR5-M12-101/102')
for p,n,e,rule in [
 ('014_TrainerType.rb',134,'Trainer type schema/default/resource/export','Text default Unnamed; skill default base money; nullable skill property preserves default; image fallback returns nil'),
 ('016_Metadata.rb',81,'Global metadata schema/properties/defaults','Global identity0/start money3000/item seed/home/audio eleven editor properties'),
 ('017_PlayerMetadata.rb',95,'Player metadata schema/properties/fallback','ID fallback1; seven movement images and cascading getters; no constructor normalization of absent images'),
 ('018_MapMetadata.rb',138,'Map metadata schema/properties/defaults','All map editor fields, flags/weather/coordinates and PBS projection inspected'),
 ('010_SpeciesMetrics.rb',101,'Species metrics schema/query/defaults','Five groups; missing form lazily registers inherited metrics with empty suffix; save path selection is independent')]:
 add('010_Data/002_PBS data/'+p,[(1,n)],e,rule,'WP73-A/B; WP77')
add('010_Data/002_PBS data/006_Item.rb',[(1,210),(245,270)],'Item schema/all editor properties/constructor/PBS projection','All 16 properties; creation defaults Unnamed/Unnamed/???; BP1 projects empty then numeric0; nullable sell price is a negative control','WP73-A §4.3; WP29 §5; GR5-M12-101/102')
add('010_Data/002_PBS data/008_Species.rb',[(1,220),(380,455)],'Species schema/editor fields/defaults/export','All33 editor fields; old plural evolution projection empty, singular export mutates parameters; height/weight scaling and form omission','WP73-A §§2/4.4/6; B21 CHAIN-6')
add('010_Data/002_PBS data/013_Encounter.rb',[(1,71)],'Encounter identities/query/enumeration/defaults','Exact pair existence versus version0 lookup fallback; version enumerator key mismatch; constructor default0/suffix','WP73-B §6; WP03/04; WP77')
add('010_Data/002_PBS data/015_Trainer.rb',[(1,213)],'Trainer schema/constructor/to_trainer/export','Complete member schema; absent IV/EV versus present partial map0; move dedup and normal load order; data keys/name mapping','WP73-A §4.2; WP18/24; WP77')
add('010_Data/002_PBS data/003_Type.rb',[(73,141)],'Effectiveness','Six multiplier categories; product by component; generator Levitate and Wonder Guard consume modified inputs','WP76 §7.3')
add('010_Data/001_Hardcoded data/011_TerrainTag.rb',[(1,204)],'Terrain tag definitions','All18 numericIDs0..17 and flags; missing tag fallback None; editor sparse/custom-ID caveat separate','WP73-B §5')
add('010_Data/001_Hardcoded data/013_EncounterType.rb',[(1,178)],'Encounter type definitions','All type registrations; land21/cave5/water2/radar20/rock50/fishing0/contest21; no per-type slot count enforced by editor','WP73-B §6; WP77')
add('010_Data/001_Hardcoded data/007_Evolution.rb',[(480,505)],'Location and LocationFlag','LocationFlag registered text parameter and map flag check; editor parameter dispatch still numeric','WP73-A §3.5; WP77 §7')
add('010_Data/002_PBS data/020_DungeonParameters.rb',[(1,121)],'Dungeon parameter selection/defaults','Area/version lookup and defaults; no binding from RandomDungeon flag to cave data','WP77 §7.1')
add('015_Trainers and player/002_Trainer_LoadAndNew.rb',[(1,124)],'load/new/check/missing trainer','First member mandatory; later repeated prompts; free version0..255; save false construction; conversion writes both PBS; missing public entry nondebug raises','WP73-A §4.2; WP75 §5.3; WP24')
add('007_Objects and windows/011_Messages.rb',[(55,158),(166,206),(711,790),(821,859)],'Number parameters/number choice/commands/free text','Default clamping precedes cancellation fallback; explicit -1 differs; command cursor versus cancel parameter; text ESC returns old','WP72/73A/76; B21 CASE-DISPATCH')
add('021_Compiler/003_Compiler_WritePBS.rb',[(1,225),(285,355),(403,644)],'Generic PBS writer and named data writers','New default text emitted from registered real fields; archive then PBS; encountered step chance0 omitted; metric paths from nonzero suffixes; trainer-list partial writes','WP73-A/B/74/76; B21 CHAIN-6; B19-C016')
add('021_Compiler/002_Compiler_CompilePBS.rb',[(289,365),(658,773),(951,1063),(1274,1321)],'Species validation/encounters/facility lists/animations','Species normalization, encounter duplicate/type/probability defaults, facility required filename keys and missing files; animation active-prefix mapping with nonempty write gate','WP73-A/B/74/76; WP04')
add('021_Compiler/001_Compiler.rb',[(990,1043)],'compile ordering','Facility lists compiled from available PBS; PBS→animations→trainer events; compilation not current encounter snapshot reset','WP76/77; WP73-B')
add('011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb',[(1,844)],'Animation container/cels/timings/player','All25 cel attributes, all five timing types and shared capture state; 20fps visited-frame behavior; slot60 exclusion; legacy conversion inactive; collection resize selection=len','WP74 §§2/7/10/14/17; all AN vectors')
add('011_Battle/004_Scene/004_Scene_PlayAnimations.rb',[(405,485),(509,529),(568,579)],'Move/common animation consumers','Side-specific fallback, hit offset, type table fallback; common exact concatenation; no trimming','WP74 §15; WP67-A shared consumer')
add('011_Battle/004_Scene/001_Battle_Scene.rb',[(19,30)],'Animation focal constants','User128,224 and target384,96 independent coordinate input','WP74 §10')
add('007_Objects and windows/008_AnimatedBitmap.rb',[(1,228)],'Bitmap loading variants','Ordinary protected load yields32-square placeholder; framed PNG errors propagate to editor rescue; native frame iterator differs','WP74 §3.3; WP15')
add('007_Objects and windows/001_RPG_Cache.rb',[(1,144)],'Bitmap cache','Empty name placeholder, path/hue cache with reference count; source copy behavior; host pixels not verified','WP74 §3.3; WP15')
add('007_Objects and windows/005_SpriteWindow_text.rb',[(764,798),(858,997),(1194,1223)],'Command window index/commands/navigation','No index clamp on assignment or commands replacement; navigation modulo can restore; no idle repair','WP73-A §5; WP74 §7.1')
add('010_Data/002_PBS data/001_MiscPBSData.rb',[(1,64)],'Animation/dex/map caches and clear','Cache priority, no-file nil; editor temporary object not automatically cached; explicit clearing triggers subsequent reload','WP73-A/B/74')
add('018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb',[(1,219)],'Facility query and compact templates','Full templates parse/serialize/create; first default fallback; EV denominator includes repetitions; no252 clamp','WP76 §§4/5.7/8; B17 PA040')
add('018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb',[(1,45)],'Challenge setup','Always invokes generation wrapper after challenge registration; wrapper DEBUG gate independent','WP76 §3')
add('018_Alternate battle modes/002_Battle Frontier rules/001_Challenge_ChallengeRules.rb',[(1,202)],'Rule wrapper and cup recipes','Rule copying, levels, battle factory and concrete cup family inputs; generated team-size2 does not bind final original rules','WP76 §§3/5/6/8')
add('018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb',[(1,232)],'Ruleset copy and validation','Complete ruleset1..224: copy minimum resets1; suggested level/number, individual/team/subset rules, team validity and clears','WP76 §§5/6/8')
add('011_Battle/004_Scene/009_Battle_DebugScene.rb',[(1,106)],'No-visual scene','Logging opt-in; auxiliary menu conditional probabilities; singular move accessor failure does not prove active AI path fails','WP72 §8; WP76 §7.2')
add('011_Battle/002_Battler/001_Battle_Battler.rb',[(1,175)],'Battler write-through','HP/status/item/level/form write original; form invokes ordinary submission; Wonder Room swaps defense access','WP72 §7.4; GR5-M12-103; WP76')
add('011_Battle/002_Battler/002_Battler_Initialize.rb',[(275,322)],'Battler update','Readback/full change controls; no unconditional reset of all debug fields','WP72 §7.4')
add('011_Battle/001_Battle/009_Battle_CommandPhase.rb',[(154,265)],'Debug command branch and AI control','Return-2 debug refresh invokes weather/terrain/form refresh; controlPlayer leads AI choice; no random menu use by generator','WP72 §7.6; WP76 §7.2')
add('014_Pokemon/001_Pokemon.rb',[(85,100),(136,217),(274,309),(1080,1127)],'Form/level/heal/stats','Ordinary form commits register regardless setup/egg; simple does not; level setter no explicit stat calc; heal clearsPP/status/evolutionready; statcalc does not clamp EV','WP72/76; WP18/21; GR5-M12-103')
add('015_Trainers and player/005_Player_Pokedex.rb',[(1,225)],'Pokedex register/seen/owned','Register no egg or debug gate; reads effective species, gender and shiny; sets seen/forms/firstlast only, not owned; conditional refresh','WP72 §6; WP62 §§3/4; GR5-M12-103')
add('019_Utilities/001_Utilities.rb',[(220,390)],'Trainer suggested/random names','System user-name fallback and full syllable tables/grammar; random up to50 then truncates; generated facility names uppercase/max12','WP72 §5; WP76 §9.2; WP24')
add('013_Items/004_Item_Phone.rb',[(148,210),(249,314),(410,446),(506,544)],'Phone contact/debug consumers','Hide resets timers/rematch/selfA/request refresh; trainer and encounter message substitutions; version and encounter sampling distinct','WP72 §5.1; WP77 §6')
add('014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',[(253,281)],'Giratina dynamic form','Orb OR DistortionWorld flag→1 else0; no Shellos handler found in full-source name search','WP77 §7; GR5-M12-103 fixture boundary')
add('012_Overworld/008_Overworld_RandomDungeons.rb',[(1044,1097)],'Dungeon generation entry parameters','Map flag enables generation; area none/version0 defaults vs explicit cave input','WP77 §7.1')
add('003_Game processing/006_Event_HandlerCollections.rb',[(80,123)],'Menu handlers','Order/default registration sequence, conditional/name resolution, effect lookup; no automatic debug condition','WP72 §§2/3')
add('003_Game processing/005_Event_Handlers.rb',[(66,175)],'Handler registrations','Replacement/iteration and shared handler copies; menu uses HandlerHash with no fallback exception handling','WP72 §2')
add('003_Game processing/002_Scene_Map.rb',[(100,121),(190,214)],'Map debug caller','F9 DEBUG gating and pending-call consumption; debug opens through fade','WP72 §3')
add('016_UI/001_UI_PauseMenu.rb',[(289,299)],'Pause debug caller','Menu condition DEBUG order80; normal return refreshes pause menu','WP72 §3')
add('016_UI/005_UI_Party.rb',[(1325,1340),(1504,1554)],'Party debug and event selector','Debug order20/gate; chosen index and name variables written even cancel→-1/empty','WP72 §§3/4')
add('016_UI/017_UI_PokemonStorage.rb',[(1539,1581)],'Storage debug caller','DEBUG command; passes held target/position/held state to mixin','WP72 §3')
add('011_Battle/004_Scene/003_Scene_ChooseCommands.rb',[(40,64)],'Battle F9 caller','F9 DEBUG returns-2; ordinary selection/cancel separate','WP72 §3')
add('016_UI/013_UI_Load.rb',[(270,310),(335,350)],'Load debug caller','DEBUG skip-continue uses encryption and config; otherwise Debug gate onlyDEBUG; calls restricted false','WP72 §§3/9')
for p in ['002_Game_Switches.rb','003_Game_Variables.rb']:
 add('004_Game classes/001_Switches and Variables/'+p,[(1,25)],'Raw slots','Upper5000; switches false fallback, variables0 onlynil; no automatic map refresh','WP72 §4.2')
add('001_Technical/001_Debugging/001_PBDebug.rb',[(1,77)],'Logs','Full logging gates DEBUG+INTERNAL; flush clears outside gate; exception print unconditional; immediate append','WP72 §8.1')
add('001_Technical/001_Debugging/003_Errors.rb',[(1,94)],'Exception boundaries','Report file append no guard; trace length10/25; critical wrapper reset/systemexit rethrow and hangup reset','WP72 §8.1; root OBS001 boundary')
add('999_Main/999_Main.rb',[(1,45)],'Main debug boundary','DEBUG alone chooses critical wrapper; loader precedes main; no universal later catch promise','WP72 §8; root OBS001')
add('013_Items/001_Item_Utilities.rb',[(401,425),(582,650)],'EV raising and learn move','Training EV clamp distinct from facility raw template EV; normal learning rejects Shadow, egg only when nondebug; PP replacement/machine option','WP72 §6.3; WP76 §5.7; B17 PA040')
add('012_Overworld/002_Overworld_Metadata.rb',[(111,122)],'Encounter version assignment','Same-value early return; changed valid version sets current map snapshot only if both objects exist','WP73-A §6; WP73-B §6.1')
add('012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb',[(1,51)],'Encounter snapshot setup','Copies chances and deep-copies slot tables; no automatic live link to registry','WP73-B §6.1')
add('014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb',[(134,167)],'Relic stone selector','Purifiable guard then selection variables1/2; only >=0 enters purification','WP72 §4.6')
add('004_Game classes/005_Game_MapFactory.rb',[(383,475)],'Connection cache/dimensions','Load validates both dimensions; normalize cardinal edge coordinates; dimensions read errors cached[0,0]; clear invalidates both caches','WP73-B §3')
add('006_Map renderer/004_TileDrawingHelper.rb',[(164,202)],'Minimap','4px/tile, 3layers and blackborder; absent map32placeholder; absent tileset blank','WP73-B §3; WP73-A map selector')
add('003_Game processing/001_StartGame.rb',[(1,65)],'Start/new game','System start map/position source distinct from Home; missing media/system not universal empty fallback','WP77 §§2/3')
add('016_UI/009_UI_RegionMap.rb',[(175,232)],'Region point/details/fly consumers','Switch/wallmap gates for all three projections; first matchingpoint and editor display distinctions','WP77 §4')
add('012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb',[(1,73)],'Wild modifiers','Map ScaleWildEncounterLevels balanced−4+0..4 then clamp/recalc/reset; prior modifiers separate','WP77 §7.2')
add('016_UI/023_UI_PurifyChamber.rb',[(1,30),(1280,1296)],'Purification access/lazy creation','Access marks seen; chamber lazily constructs; no menu access check added','WP72 §4.6')
add('004_Game classes/004_Game_Map.rb',[(45,66)],'Map reconstruction','Uses current global tilesets; terrain editor saved alias survives later No','WP73-B §5')
add('001_Technical/002_Files/001_FileTests.rb',[(175,252)],'Resource resolved comparison paths','Current directory only; literal-first then extension resolution; absolute input unchanged; no match returns input','WP74 §13.3; optional GR5-M12-104')
add('021_Compiler/004_Compiler_MapsAndEvents.rb',[(88,249),(440,699),(815,913),(979,1133),(1391,1578),(1683,1751)],'Independent root observations counterevidence','Direct anchors for trainer annotation latch/consumption, exact generated doors/transfer, six line-anchored old calls and TrainerBattle-only empty repair, distinct map/common driver','WP75; root OBS002..007',role='independent_counterevidence')
add('020_Debug/003_Debug menus/008_Debug_FilenameUpdater.rb',[(1,89)],'Independent filename counterevidence','Prefix eligibility then every token occurrence replacement; special stage basename gate; map references match same transformation','WP75 §11; root OBS006',role='independent_counterevidence')
# Remove the parent-inherited inventory entry when replacing it with a direct independent read.
rc['records']=[x for x in rc['records'] if x['path']!='Data/Scripts/020_Debug/003_Debug menus/008_Debug_FilenameUpdater.rb']+secondary
rc.update(base)
rc['method']='Full primary source bodies were read in segments and manually analyzed before mappings. Dependency slices are direct reads, not full-module claims. Hashing/serialization is bookkeeping, not semantic evidence.'
rc['execution_status']='STATIC_ONLY_NO_REFERENCE_OR_MODEL_EXECUTION'
rc['parent_ownership']={'reviewer':'root','record':'../M12/reading-coverage.json','reused_identity_only':True,'scope':'Full Compiler_MapsAndEvents, root tools and media remain root-owned; M12B direct counterevidence slices separately recorded, never inherited as independent full signoff.'}
# Complete configuration bodies already read directly, plus bounded literal fixture data.
for p,rr,entry,rule in [
 ('PBS/metadata.txt',[(1,33)],'Global and player metadata','Every supplied field and both player records compared; Home is recovery, not game start'),
 ('PBS/map_metadata.txt',[(1,398)],'All map metadata records','69 sections; locations/flags/weather/healing/authoring examples compared one by one'),
 ('PBS/map_connections.txt',[(1,40)],'All19 connections','All endpoints/edge offsets matched WP77; Route8–Lappet directedge retained'),
 ('PBS/town_map.txt',[(1,36)],'All town map points','26 point rows, six flight rows/five destinations/four matching healing points; switches51/52'),
 ('PBS/dungeon_parameters.txt',[(1,30)],'Both dungeon parameter records','cave and forest distinct area/size/corridor offset; not default none'),
 ('PBS/battle_facility_lists.txt',[(1,25)],'All five facility lists','Default plus4 explicit cups; fancy single-named input also referenced by doubles'),
 ('PBS/phone.txt',[(1,48)],'All phone messages','Default intro5 plus time3 separate; Jeff/Susie text and variants'),
 ('PBS/encounters.txt',[(1,311)],'All root encounter rows','19 sections, all slots/form variants/levels; Safari counts distinguish rows and species'),
 ('PBS/trainers.txt',[(1,118)],'All20 trainer records','Brock all fields, twoShadow entries, rival variants/champion, contacts versions'),
 ('PBS/trainer_types.txt',[(18,27),(38,42),(79,83),(95,99),(171,180),(191,200),(239,244),(269,274),(297,306),(312,318),(396,401)],'All15 types used by demo trainer rows','IDs and numeric/default/BGM fields verified; YOUNGSTER shortcut qualified'),
 ('PBS/battle_tower_pokemon.txt',[(1,8)],'Fixed B17 PA040 and leading template controls','CATERPIE FOCUSBAND QUIRKY HP/ATK TACKLE/STRINGSHOT; twoEV255 each and duplicate denominator counterexample'),
 ('PBS/battle_tower_trainers.txt',[(1,18)],'Facility template shape controls','Two concrete valid training records and assigned zero-based candidate IDs'),
 ('PBS/moves.txt',[(2990,3000),(5141,5151),(6395,6403)],'Generator pruning and Sketch fixtures','AERIALACE/SWIFT accuracy0 power60 None; SKETCH effect andPP1'),
 ('PBS/pokemon.txt',[(6191,6206),(11113,11140)],'SMEARGLE and SHELLOS fixtures','Smeargle onlySketch weighted repetitions; Shellos base named WestSea andgender'),
 ('PBS/pokemon_forms.txt',[(1117,1134)],'SHELLOS form1','Named EastSea form with inherited fields, no getForm handler')]:
 add(p,rr,entry,rule,'WP77/WP76; GR5-M12-103 fixture',role='configuration_or_fixture')
rc['records']+=secondary[len(rc['records'])-23:] if False else []
# secondary appended by add() after rc copied the initial list: append just data entries.
rc['records'] += [x for x in secondary if x['assigned_role']=='configuration_or_fixture']
loader=dict(path='Data/Scripts.rxdata',version=RV,reviewer='M12B',review_extent='partial',material_availability='available_binary_safe_zlib_decode',evidence_level=['SOURCE_STATIC'],assigned_role='independent_counterevidence',semantic_ranges=[dict(lines=[1,49],coordinate_system='decoded Main text',entry='external script loader',rules='Files before subdirectories, separately sorted; dot directories skipped but dot .rb files included; .RB accepted; unbounded recursion; read outside protected evaluation; ScriptError replacement and StandardError report/900-char log boundary; all other exceptions propagate')],content_read_ranges=[[1,49]],unreviewed_ranges=[],unreviewed_scope='Binary archive container not executed or deserialized; only exact compressed text member safely decoded',decoded_sha256='da24a2220936c6d44ddc60f180aed37beede022012d7addc99b5562ed07c52e1',decoded_bytes=1197,compressed_member_offset=29,**identity(R/'Data/Scripts.rxdata'))
rc['records'].append(loader)
# Formal/original and effective supplement reading records added separately below.
save('reading-coverage.json',rc)
print('source records',len(rc['records']))
# Last bounded dependency/data reads.
extra_before=len(secondary)
add('019_Utilities/002_Utilities_Pokemon.rb',[(186,238)],'Balanced level','All members incl eggs/fainted; population deviation; separate weight bounds; round→lower1→+2→upperM; empty/sum0 direct1','WP77 §7.1; WP36 §6.2')
add('019_Utilities/001_Utilities.rb',[(510,526)],'Event variable write wrapper','Negative/absent ID guard; writes variable if wrapper exists and separately requests map refresh','WP72 §4')
add('001_Settings.rb',[(44,54),(215,224),(264,288)],'Author-tool consumed configuration','Money/BP/party/boxes/pocket names/capacity/order/slot maximum; not a full configuration-domain audit','WP72/73A/76')
add('PBS/pokemon.txt',[(2173,2180),(3533,3540),(7913,7919),(19063,19069),(19113,19119)],'All six LocationFlag rows','Both evolution conditions and map flags; no assertion of reachability','WP77 §6.5/§8')
rc['records']+=secondary[extra_before:]
# Merge repeated reads of the same source while retaining all semantic notes.
by={}
for r in rc['records']:
 k=(r['path'],r.get('version'))
 if k not in by:by[k]=r;continue
 z=by[k];z['semantic_ranges']+=r['semantic_ranges'];z['content_read_ranges']=merge(z['content_read_ranges']+r['content_read_ranges'])
 if 'total_lines' in z:
  z['unreviewed_ranges']=gaps(z['content_read_ranges'],z['total_lines']);z['review_extent']='partial' if z['unreviewed_ranges'] else 'full'
rc['records']=list(by.values())
# All main formal and original bodies were read; exact matching spans need not be read twice.
main_files={p.name.split('-')[0]+('-a' if p.name.startswith('wp73-a') else '-b' if p.name.startswith('wp73-b') else ''):p for p in (F/'demo-dx').glob('wp7[234567]*')}
def doc_record(p,rr,entry,rule,version=BV,kind='specification'):
 n=len(lines(W/p)); rr=merge(rr)
 return dict(path=str(p),version=version,total_lines=n,reviewer='M12B',assigned_role=kind,material_availability='available_text',review_extent='partial' if gaps(rr,n) else 'full',evidence_level=['SPEC_STATIC'] if kind!='original' else ['ORIGINAL_COMPARISON'],content_read_ranges=rr,semantic_ranges=[dict(lines=q,entry=entry,rules=rule,comparison_result='Manually compared; line mapping only serializes the comparison') for q in rr],unreviewed_ranges=gaps(rr,n),**identity(W/p))
for k,p in main_files.items():
 rc['records'].append(doc_record(p,[(1,len(lines(p)))],'Complete '+k+' contract','Every section, paragraph, parameter/default table and named example read; linked vectors and applicable supplements compared; source ownership and exceptions in reverse mapping'))
orig=[]
for k,p in main_files.items():
 o=Path('specs/demo')/p.name; a=lines(o);b=lines(p);matcher=difflib.SequenceMatcher(None,a,b,autojunk=False)
 rr=[dict(kind=t,original_lines=[i+1,j] if i<j else [],formal_lines=[x+1,y] if x<y else []) for t,i,j,x,y in matcher.get_opcodes()]
 orig.append(dict(original=str(o),formal=str(p),version=BV,review_extent='full',material_availability='available_text',method='Full semantic comparison. Original differing spans read directly; exact equal spans reuse the independently read full formal body. Source-first evidence, not diff counts, determines disposition.',ranges=rr,unique_fact_disposition='No uncarried valid independent behavioral fact identified in the complete original main body. Trace/source identifiers and historical administrative status correctly excluded; vector tables moved into current catalog. Superseded assertions separately listed below.',original_identity=identity(o),formal_identity=identity(p)))
 rc['records'].append(doc_record(o,[(1,len(a))],'Complete original '+k,'All original facts compared against current main body plus test catalog; same-line reuse explicitly distinguished from differing-line direct reads',kind='original'))
supps=[
 ('review/wp72-delivery-2026-10-02/revision-v2/battle-effects-catalog.md','All120 exact effect identities/default/range/sentinel rows, mapped in order to current E001–E120; current table also separates ACTION reset'),
 ('review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md','All capability rows compared; current formal expression-switch behavior supersedes stale blanket display-does-not-change; form registration gate still candidate103'),
 ('review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md','All property/editor/lister rows; old EV can-not-leave, form0–999 and evolution read mutation claims judged against source/current refined contract, not carried as authority'),
 ('review/wp73b-delivery-2026-10-02/revision-v4/entry-coverage-table.md','All world editor rows; current changed-only positioning and runtime snapshot/write-path refinements preserved'),
 ('review/wp74-delivery-2026-10-02/revision-v4/entry-coverage-table.md','All42 capability rows and inactive appendix; full current cel ranges, timing gradients and directory failures extend these rows'),
 ('review/wp75-delivery-2026-10-02/revision-v4/entry-coverage-table.md','All44 rows read for independent negative evidence only; no exact door defaults, duplicate Boolean rule or decoded loader contract; explicitly TrainerBattle-only empty repair rebuts broad complaint'),
 ('review/wp76-delivery-2026-10-02/revision-v4/entry-coverage-table.md','All29 rows and inactive appendix; current match-history settlement and pause/iteration equations take precedence over old mistaken ordering'),
 ('review/wp77-delivery-2026-10-03/revision-v2/evidence-coverage-table.md','All16 rows inspected; config/static/chain/runtime tiers remain separated'),
 ('review/wp77-delivery-2026-10-03/revision-v2/gap-register.md','All12 gap rows; suggested future verification preserved in current gap responsibility and source availability limitations')]
for p,note in supps:rc['records'].append(doc_record(Path(p),[(1,len(lines(Path(p))))],'Applicable original attachment',note,kind='supplement'))
# B5 current cross-contracts read completely or in the precise bounded slices below.
related=[
 ('generic-kernel/wp03-content-identity-and-schema.md',[(1,240)]),('generic-kernel/wp04-pbs-lifecycle.md',[(1,227)]),
 ('generic-kernel/wp05-events-extensions-plugins.md',[(1,141)]),('generic-kernel/wp07-diagnostics-files-http.md',[(1,143)]),('generic-kernel/wp09-save-startup-continue.md',[(1,163)]),
 ('creature-rpg/wp24-player-trainers-partners.md',[(1,289)]),('creature-rpg/wp27-bag-and-item-storage.md',[(1,174)]),('creature-rpg/wp29-shops-and-exchanges.md',[(1,210)]),
 ('creature-rpg/wp18-creature-identity-species-ownership.md',[(131,155)]),('pokemon-rules/wp21-dynamic-forms-and-display.md',[(1,327)]),('pokemon-rules/wp62-pokedex-records-regions-and-content.md',[(1,118)]),
 ('engine-overworld/wp13-map-events-npc-followers.md',[(1,190)]),('engine-overworld/wp13-move-route-matrix.md',[(1,81)]),('engine-overworld/wp13-interpreter-command-matrix.md',[(1,84),(123,159)]),
 ('engine-overworld/wp15-resource-matching-and-audio.md',[(17,46),(117,162)]),('engine-overworld/wp16-world-rendering-and-visual-transitions.md',[(203,229)]),('creature-rpg/wp36-wild-encounters-and-modifiers.md',[(199,206)]),
 ('test-catalog/demo-dx-wp72-73-74-75-76-77.md',[(1,295)]),('test-catalog/generic-kernel-wp02-03-04.md',[(1,81)]),
 ('test-catalog/generic-kernel-wp05-06-07-08-09-10.md',[(1,35),(70,98),(155,175)]),
 ('test-catalog/creature-rpg-wp18-20-24-25-26.md',[(5,40),(91,125)]),('test-catalog/pokemon-rules-wp19-21-22-23-34.md',[(84,131)]),('test-catalog/creature-rpg-wp27-28-29-30-33.md',[(122,157)])]
for p,rr in related:
 q=F/p;n=len(lines(q));rr=[(a,min(b,n)) for a,b in rr]
 rc['records'].append(doc_record(q,rr,'Current related contract/negative evidence','Read the stated entire related section/body; shared generic contracts do not replace concrete author-tool entry behavior; no full-domain audit implied for a bounded slice'))
# Exact accepted archive objects, with actual semantic read scope. No old execution is claimed as this review's execution.
archives=[
 ('e58486178e746273fb6fab55df00722807f1dc44','review/remediation/20261003-prepare/batches/B21/author-draft-1/static-cases.json','all CASE-DISPATCH records','full','Number default5 BACK5; nullable clear; pocket old0 BACK0 versus confirmfirst→1'),
 ('e58486178e746273fb6fab55df00722807f1dc44','review/remediation/20261003-prepare/batches/B21/author-draft-1/eight-chains.json','CHAIN-6 behavioral fields and linked contracts/vectors','partial','Edit→archive→PBS→compile→snapshot; plural Evolution projection versus singular write; stale reverse relationships; excludes administrative receipts'),
 ('e58486178e746273fb6fab55df00722807f1dc44','review/remediation/20261003-prepare/batches/B17/author-draft-1/traceability.json','whole object','full','Version and exact PA040 source binding'),
 ('e58486178e746273fb6fab55df00722807f1dc44','review/remediation/20261003-prepare/batches/B17/author-draft-1/static-cases.json','PA040 double/training/duplicate objects','partial','CATERPIE normal two emphasizes255 each, repeated denominator170 each, normal training250→252 distinct'),
 ('3f521e6dea0b442e4bb174a9715c458416386b37','review/remediation/20261003-prepare/batches/B20/author-draft-1/six-family-fixtures.json','all18 objects','full','Each six-family core/default/canLose fixture inspected; empty_branch_revisit is visit label, not assertion all wild branches insert exit')]
for v,p,scope,extent,note in archives:
 b=subprocess.check_output(['git','show',v+':'+p])
 rc['records'].append(dict(path=p,version=v,material_availability='available_fixed_archive_object',review_extent=extent,reviewer='M12B',assigned_role='effective_supplement',evidence_level=['SPEC_STATIC','SUPPLEMENT_STATIC'],semantic_ranges=[dict(json_pointer_scope=scope,rules=note)],unreviewed_ranges=[] if extent=='full' else ['Other unrelated objects and administrative receipt fields'],bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),execution_status='NOT_EXECUTED_THIS_REVIEW'))
# Inventory-only material is deliberately excluded from semantic completion count.
for p in sorted(R.glob('PBS/Gen * backup/encounters.txt')):
 rc['records'].append(dict(path=str(p.relative_to(R)),version=RV,review_extent='inventory_only',material_availability='available_text',assigned_role='outside_root_demo_data_scope',evidence_level=['INVENTORY_ONLY'],semantic_ranges=[],unreviewed_ranges=[[1,len(lines(p))]],boundary='WP77 explicitly bounds full slot audit to root encounters.txt; backup tables are alternative datasets, not default active demo records',**identity(p)))
for p in ['Data/MapInfos.rxdata','Data/System.rxdata','Data/Tilesets.rxdata','Data/CommonEvents.rxdata','Data/Animations.rxdata','Data/PkmnAnimations.rxdata','Data/move2anim.dat','Data/trainer_lists.dat','Graphics','Audio','Plugins','Game.ini','Game.rxproj']:
 exists=(R/p).exists()
 rc['records'].append(dict(path=p,version=RV,review_extent='unreadable' if not exists else 'inventory_only',material_availability='missing_material' if not exists else 'available_inventory',assigned_role='demo_material_boundary',evidence_level=['INVENTORY_ONLY'],semantic_ranges=[],unreviewed_ranges=['No file body available' if not exists else 'Not part of this behavioral source assignment'],boundary='Existence result only; missing material neither disproves a feature nor verifies a runtime fallback'))
orig_result={**base,'records':orig,'attachments':[dict(path=p,version=BV,result=n) for p,n in supps], 'superseded_or_correctly_excluded':[
 {'path':'specs/demo/wp73-a-content-editors.md','scope':'§2/§3.5 plus v4 attachment','result':'Old mutation attributed to opening plural Evolutions is superseded by current exact empty-projection/singular-export contract; not a lost valid fact.'},
 {'path':'review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md','scope':'IV/EV row and TrainerPokemon row','result':'Old cannot-leave excess-EV and form0–999 shorthand not copied as authority; actual child loop and form0–99 are already specified in current body. Numeric-key storage representation is correctly excluded from clean-room behavior, while missing named-stat0 remains.'},
 {'path':'specs/demo/wp73-b-world-editors.md','scope':'M17 positioning','result':'Old blanket changed flag revised to actual confirmed-operation condition in current WE-M17; source supports current qualification.'},
 {'path':'specs/demo/wp76-facility-content-generation-and-simulation.md','scope':'§7.4 and M18/M20; corresponding attachment','result':'Current §7.4a disambiguates history settlement and cumulative count; stale original statement cannot overwrite source-correct current chain.'},
 {'path':'specs/demo/wp72-debug-contexts-and-controls.md','scope':'§7.5 + effect catalog','result':'All120 data rows explicitly carried to current E001–E120 including LastRoundFainted default−2/reset−1 and PayDay cap; no unique effect row lost.'},
 {'path':'specs/demo/wp77-demo-evidence-and-capability-coverage.md','scope':'§9/G01–G12 and attachments','result':'Future evidence to collect is represented by same12 current gaps; administrative counts do not prove semantic coverage or runtime availability.'}], 'conclusion':'No additional substantive loss unique to B5 original bodies or these attachments was found; new findings arise from source-first behavior, and occur in both original and current descriptions.'}
save('original-comparison.json',orig_result)
save('reading-coverage.json',rc)
