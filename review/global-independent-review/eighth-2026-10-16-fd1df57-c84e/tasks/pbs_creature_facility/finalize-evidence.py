"""Record already-performed reading and manual assertions; metadata only."""
from pathlib import Path
import datetime, hashlib, json, re, subprocess

HERE = Path(__file__).parent
SPEC = Path('/workspace/pokemon-essentials-clean-room')
REF = Path('/workspace/pokemon-essentials')
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(n): return json.loads((HERE/n).read_text())
def put(n,d): (HERE/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def ident(repo, commit, path):
    data=(repo/path).read_bytes()
    tree=subprocess.check_output(['git','rev-parse',commit+'^{tree}'],cwd=repo,text=True).strip()
    blob=subprocess.check_output(['git','rev-parse',commit+':'+path],cwd=repo,text=True).strip()
    actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    return dict(repo=str(repo),commit=commit,tree=tree,path=path,blob=blob,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),matches_frozen_blob=actual==blob,lines=len(data.splitlines()))

F='Data/Scripts/018_Alternate battle modes/001_Battle Frontier/'
Q='Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/'
C='Data/Scripts/021_Compiler/'
G='Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/'
units=[]
def unit(id,path,ranges,claims,formal,mode='FULL_READ_SELECTED_UNITS'):
    units.append(dict(id=id,path=path,ranges=ranges,reviewer='/root/pbs_creature_facility',read_mode=mode,
                      fact_subassertions=claims,formal=formal,evidence='SOURCE_STATIC',execution='NOT_EXECUTED'))
unit('PBF-S01',F+'001_Challenge_BattleChallenge.rb',[[1,429]],[
 'All challenge getters/config/register branches, missing Type config writes and conditional mode generation',
 'CurrentID assignment/start partial state, unique trainer loop, counters and nextTrainer',
 'Party reference snapshot/submission/cancel/end asymmetry; six record counters, retained state after cancel',
 'Pause/resume/save-location writes and noensure; FactoryData full rental prepare/choose/swap commits'],['WP55§2/4','WP57§3–5'],'FULL_READ')
unit('PBF-S02',F+'002_Challenge_Data.rb',[[1,219]],[
 'Lazy global challenge, separate first matching nondefault then first default lookups; load failure rescue',
 'Entry nil/empty truthiness, graphic fallback and message intro actual receiver',
 'All template parse/initialize/fromPokemon/inspect/unusedcompact/RETURN/create branches; ID absence not alias',
 'Every template gets normal constructor, no automatic moves, item/PID/nature/happiness/moves/EV/IV/stats writes in order'],['WP55§2.5/2.7','WP76§8'],'FULL_READ')
unit('PBF-S03',F+'003_Challenge_ChooseFoes.rb',[[1,164]],[
 'All15 trainer threshold rows, floor scaling, negativewins and zero-rand branch; all8 IV bands',
 'Short list preserves all order/duplicates without validation; long list samples withreplacement and no cap',
 'Factory2 complete8row tables, inclusive881 scaling, swap6thresholds, IV8rows, temporary numbers and normal-only restoration'],['WP55§2.5/4','WP57§2'],'FULL_READ')
unit('PBF-S04',F+'004_Challenge_Battles.rb',[[1,144]],[
 'All4 battle creators, debugskip and ordinary heal→EXP-adjust→itemsnapshot→create→noninternal→prepare→battle',
 'Normal indexed EXP then heal/unmega/unprimal/item restore; recorddecisions1/2/5 and stats; noensure',
 'Record move+clear, Marshal playback dispatch, directfile/debugfile paths'],['WP54§4.2','WP55§3/4','WP58 boundary'],'FULL_READ')
unit('PBF-S05',F+'005_UI_BattleSwap.rb',[[1,247]],[
 'All rental/swap menus and bothscreen state loops; rental cannotcancel, exactly3 and rejectlastselection',
 'Swap cancel/reselect/confirm paths; accepted slot reference replaced with opponentobject and boolean returned',
 'Summary invocation and whole UI show/hide/dispose flow; UI actual runtime untouched'],['WP57§3/4'],'FULL_READ')
unit('PBF-S06',Q+'001_Challenge_ChallengeRules.rb',[[1,382]],[
 'Container shallowcopy and resets/shared lists, ordered battlerules, exactbilateral type predicate',
 'All10 active factories with member/team/number/layout/adjustment/clauses parameters; all inactive examples read as inactive'],['WP54§2/4/5','WP54data§1/2'],'FULL_READ')
unit('PBF-S07',Q+'002_Challenge_Rulesets.rb',[[1,323]],[
 'Defaults/publicnegative max6/raw0/min1, copyminreset, addSubset actually team, suggestednumber/level',
 'All canRegister/hasRegistrable/hasValid/isValid distinct guards, full combination enumeration and errors',
 'StandardRules and5direct cup sample constructors preserve min1 and differing restrictions'],['WP54§2/5','WP54data§2/4.1'],'FULL_READ')
unit('PBF-S08',Q+'003_Challenge_EntryRestrictions.rb',[[1,392]],[
 'All25 restrictions: ordinaryability priority/named whitelist/ban/BST, height/weight and species-key caches',
 'All count/totallevel/species/item/nickname methods and actual nil/failure behavior, strictlittle item/move/species lists',
 'Unused negative extension lacks true return; module nickname helper and preceding-only loops separately retained'],['WP54§3','WP54data§3/4.2'],'FULL_READ')
unit('PBF-S09',Q+'004_Challenge_LevelAdjustment.rb',[[1,229]],[
 'All9 adjustment definitions; firstsave both EXP, side types, clamping or unclamped open/balance cases',
 'Normal restore indexed conditional EXP/calcstats; missing instance nullhelper; noensure; combinations ignore nestedtypes'],['WP54§4','WP54data§4.3'],'FULL_READ')
unit('PBF-S10',Q+'005_Challenge_BattleRules.rb',[[1,103]],[
 'All14 setter definitions; single/double layout and exactdictionarykeys',
 'draw/modifiedselfdestruct/suddendeath are receiveronly keys with no convenience setter here'],['WP54§6','WP54data§4.4'],'FULL_READ')
unit('PBF-S11',C+'002_Compiler_CompilePBS.rb',[[857,1073]],[
 'Incidental ordinarytrainer compile validation context857–948 separately not wholefile credit',
 'Whole facilities compiler949–1070: missinglist writes default, valid sections, requiredtwofilenames, missingfiles empty',
 'All6 trainer schema fields order and unknownkeys ignored; sectionnames unconstrained, names/speeches hash accumulation',
 'Templates use commentedline parser and full fromInspected; messageclears before compile; save .dat only after loops'],['WP55§2.5','WP04§4.2'])
unit('PBF-S12',C+'003_Compiler_WritePBS.rb',[[511,621]],[
 'Whole3 facility writers: datareadrescue, list metadata/default and indirecttrainer/template writes',
 'Trainer numeric section order, nilfields omitted, PokemonNos rawjoin; others CSVwriter',
 'Template canonical IDs, itemexistence, EVbrief order and4slot moves; no transactionalrollback'],['WP55§2.5','WP76§8.4','WP04§5'])
unit('PBF-S13',C+'001_Compiler.rb',[[1,220],[255,312],[384,510],[650,795],[840,1135]],[
 'Line/file/header/comment preprocessing; partial unrelatedfunc at220 not fullunitcredit',
 'Full split_csv_line255–293: oddquotes recombine, literalbackslashquote stripping conditional onposition/count; unrelatedunused csvfield partial',
 'Full cast/checkenum relevanttypes and get_csv_record690–736/writer and quoting relevantunits',
 'Whole edit/rewrite+modify-before-compile onlyVictoryME/BaseDamage rewrites, file discovery/compile order',
 'Compile_all and main complete to actual EOF: registrycompile before facilities, deletion/exception cleanup and no runtime invocation'],['WP04§3–5','WP55§2.5'])
unit('PBF-S14','PBS/battle_facility_lists.txt',[[1,25]],[
 'All5 sections: defaultTower; Poke/Little/Pika single+double; Fancy both variants selectsingle254, alternative618 unselected'],['WP54data§1','WP55§2.5'],'FULL_READ')
unit('PBF-S15','PBS/trainer_types.txt',[[1,999999]],[
 'All72 type records and all fields read; all44 referenced types exist. Defaults and actualmoney/skill/gender/flags/music inherited through trainer registry'],['WP55§2.5/2.7','trainer domain'],'FULL_READ')
unit('PBF-S16','Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb',[[1,134]],[
 'Whole schema/defaults/name/gender/flag/PBSwriter; all charset/front/back/icon filename handlers and bitmapresolution fallback'],['WP55§2.7','trainer domain'],'FULL_READ')
unit('PBF-S17','Data/Scripts/015_Trainers and player/001_Trainer.rb',[[1,194]],[
 'Whole Trainer/NPC: registered type identity, name/ID/language/empty party and no NPC inventory/speeches bydefault',
 'Type name/skill/money/gender/flag forwarding, fullname NoName branch, heal and party methods'],['WP55§2.5/3','WP57§2.4'],'FULL_READ')
unit('PBF-S18','Data/Scripts/011_Battle/005_AI/009_AITrainer.rb',[[1,108]],[
 'Whole AITrainer skillsetup/typeflags/defaultskillbands/sanitize Anti flags; exactcase inclusion and medium32/high48/best100'],['WP55 type consumer','WP51 boundary'],'FULL_READ')
unit('PBF-S19','Data/Scripts/001_Technical/003_Intl_Messages.rb',[[475,490],[500,630],[638,681],[750,785]],[
 'Whole stringToKey/load message/default/getFromHash/hashbuilder/wrappers relevantunits; selected ranges only',
 'Localizedgame then core then originaltext; nil/emptyoriginal short circuit; key whitespace normalization doesnotremove literalquotes',
 'Facilitycompile hash accumulator/set difference and defaultmessage save/load are actual source consumers'],['WP55§2.5/2.7','WP04 messages boundary'])
unit('PBF-S20','Data/Scripts/002_Save data/001_SaveData.rb',[[1,999999]],[
 'Whole SaveData container read; registration/value save/load orchestrates actual global reference serialization'],['WP55globalpersistence','WP09boundary'],'FULL_READ')
unit('PBF-S21','Data/Scripts/002_Save data/002_SaveData_Value.rb',[[1,292]],[
 'Whole Value default/load/newgame/validation/save optionalcondition fields and callbacks, no automatic challenge revalidation'],['WP55globalpersistence','WP09boundary'],'FULL_READ')
unit('PBF-S22','Data/Scripts/002_Save data/004_Game_SaveValues.rb',[[1,999999]],[
 'Whole actual registration list read, PokemonGlobal saved and loaded by reference to data; classgate retained'],['WP55globalpersistence','WP09boundary'],'FULL_READ')
unit('PBF-S23','Data/Scripts/003_Game processing/001_StartGame.rb',[[63,149]],[
 'Game.load/map/save complete relevantunit: safesave counters/version/metadata and IO/SystemCall rescue false; other exceptions propagate'],['WP55§2.4/4','WP09boundary'])
unit('PBF-S24','Data/Scripts/012_Overworld/002_Overworld_Metadata.rb',[[1,104]],[
 'Global metadata challenge attr33 and constructornil88; partial remainingmetadata not granted fullfile credit'],['WP55globalpersistence'])
unit('PBF-S25','Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb',[[330,547]],[
 'Money win/loss internalguard and full EndOfBattle404–514 reads NPC lose/win text bydecision; prize not awarded by noninternal facility',
 'Postbattle refunds/cleanup and scene outputs; partialjudging after514 separately incidental'],['WP55§3/4','WP50 boundary'])
unit('PBF-S26','Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb',[[1,999999]],[
 'All25 nature registrations, property schema, default changes and message names; table order default selection input'],['WP55§2.5'],'FULL_READ')
unit('PBF-S27','Data/Scripts/014_Pokemon/001_Pokemon.rb',[[535,585]],[
 'Full actualitem getter/item_id/setter/hasItem? definitions including unknownleavesold, nilclear and typedcomparison'],['PBF-ITEM','WP55§3'])
unit('PBF-S28',G+'003_ChallengeGenerator_Trainers.rb',[[1,211]],[
 'All200attempts emptybranch, type/name weights, repeated species and refill boundaries, originalvalidity and final save/write lists',
 'Allmatching listdefault flag computed from beforewrites, .dat saved then PBS writes, no transaction; Generator invocation NOT_EXECUTED'],['WP76§8/9'],'FULL_READ')
unit('PBF-S29','Data/Scripts/019_Utilities/003_Utilities_BattleAudio.rb',[[1,152]],[
 'All wild/trainer music functions incl typeintro memorize, array lastspecified type precedence, globaloverride/map/global/fallback',
 'Trainer victory returns BGM-relativeME path and fromtype function retains stringcase; host playback/resource bytes not interpreted'],['WP55typeaudio','WP58boundary'],'FULL_READ')
unit('PBF-S30','Data/Scripts/011_Battle/004_Scene/002_Scene_Initialize.rb',[[150,210]],[
 'Whole trainerback/front sprite creation selectedunits; front bitmapabsence returns after pbAddSprite; placement actualconsumer'],['WP55§2.7'])
unit('PBF-S31','Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb',[[1,90],[245,285]],[
 'Full trainer tuple serialization and18 metadata start fields, fivepartdump; later registertarget partial not grantedallrecordcommands',
 'Playbackhelper receiver recreates trainer/class tuple/name/ID/win/lose, recorded party is Marshal data; full replayeffects not claimed'],['WP55§3 recordjoin','WP58boundary'])

formal=[
 ('combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md',[[1,156]],'FULL_READ'),
 ('combat-requirements/wp54-entry-rules-and-cup-data.md',[[1,109]],'FULL_READ'),
 ('combat-requirements/wp55-facility-session-and-restoration.md',[[1,152]],'FULL_READ'),
 ('creature-rpg/wp57-factory-rentals-and-swaps.md',[[1,116]],'FULL_READ'),
 ('demo-dx/wp76-facility-content-generation-and-simulation.md',[[1,279]],'FULL_READ'),
 ('test-catalog/combat-requirements-wp54-55-56-58.md',[[1,190]],'FULL_READ'),
 ('test-catalog/creature-rpg-wp35-36-57-64-68.md',[[70,90]],'FULL_READ_FC_SECTION_ONLY'),
 ('test-catalog/demo-dx-wp72-73-74-75-76-77.md',[[231,260],[285,294]],'FULL_READ_GN_AND_B17_SECTIONS_ONLY'),
 ('generic-kernel/wp04-pbs-lifecycle.md',[[70,128]],'FULL_READ_SELECTED_SECTION_ONLY')]
formal=[dict(path='deliverables/final-specification-set/'+p,ranges=r,credit=m,reviewer='/root/pbs_creature_facility') for p,r,m in formal]
identities=load('identities.json')
for row in identities['primary']:
 row.pop('semantic_status',None)
 row['inventory_semantic_status_at_freeze']='UNREAD (original frozen inventory, not current reading status)'
 row['semantic_status']='FULL_PRIMARY_BUSINESS_FIELDS_READ'
 row['evidence_level']='SOURCE_STATIC'
 row['actual_reviewer']='/root/pbs_creature_facility'
identities['supplemental_reference']=[ident(REF,R,p) for p in dict.fromkeys(x['path'] for x in units)]
for x in units:
 n=next(z['lines'] for z in identities['supplemental_reference'] if z['path']==x['path'])
 x['ranges']=[[a,min(b,n)] for a,b in x['ranges']]
identities['formal']=[ident(SPEC,B8,x['path']) for x in formal]
identities['supplemental_identity_matches']=all(x['matches_frozen_blob'] for x in identities['supplemental_reference']+identities['formal'])
identities['updated_utc']=NOW
put('identities.json',identities)
ledger=load('reading-ledger.json')
ledger['supplemental']=units
ledger['formal']=formal
ledger['primary_unread_records']=0
for x in ledger['primary']:
 x['unreceived_consumers']=[]
 x['bounded_join']='Own full actual receiver units and bounded peer receipts; battle-effects/host/event composition independently scoped in interfaces and review'
ledger['receipts']=[
 dict(id='RC-FAC',reviewer='/root/com_facility',accepted_facts=['FAC-R07','FAC-R08','FAC-R09','FAC-R10','FAC-R13','FAC-R14','FAC-R15','FAC-R16','FAC-R17','FAC-R19','FAC-R20','FAC-R21','FAC-R22'],payloads=['tasks/com_facility/review.md','tasks/com_facility/interfaces.json','tasks/com_facility/forward-mapping.json selected complete logicalfacts'],scope='SOURCE_STATIC finite producer/receiver facts, own related receivers independently read; no wholefacility PASS'),
 dict(id='RC-CUP',reviewer='/root/pbs_world_record_audit',payloads=['tasks/pbs_world_record_audit/review.md','tasks/pbs_world_record_audit/field-contracts.json#/contracts/CUP','tasks/pbs_world_record_audit/interfaces.json'],accepted='All1888 template records/fields by original full reader; parent actual parser/create/select/generation/rules join read',not_claimed='Parent raw reread of1888 or receipt of remaining worldgroups'),
 dict(id='RC-ITEM',reviewer='/root/creature_b',payloads=['tasks/creature_b/facility-item-interface.json','tasks/creature_b/pbs-record-reception.json'],accepted='FITEM1–4 identity/getter/setter/equality and3154path item records default+conditionalprofiles; finite exact ID inventory receiver join',not_claimed='Wholeheld battleeffect execution or actual live registry'),
 dict(id='RC-TRAIT',reviewer='/root/pbs_creature_facility/trait_eligibility',payloads=['subreviews/trait_eligibility/review.md','subreviews/trait_eligibility/interfaces.json','subreviews/trait_eligibility/creation-domain.json','subreviews/trait_eligibility/finite-traits.json'],accepted='All453 template species relevant fields2732provenances649classes, allreachablecreatedforms predicates and allfactories/direct/modes; parent read proof/contract and independently uses all records in finite inventory, no parent raw reread',cache_premise='Cold or consistent caches for numeric certificates; complete actualstate predicate otherwise')]
ledger['updated_utc']=NOW
put('reading-ledger.json',ledger)

forward=[]
raw=load('trainer-structure.json')
for i,x in enumerate(raw['source_records']):
 forward.append(dict(id='PBF-TRAINER-%04d'%i,path=x['file'],record_order=i,source_section=x['section'],source_start=x['start'],
  fields={k:dict(line=v['line'],value=v['value'],semantic_unit={'Type':'PBF-S11/PBF-S16/PBF-S17/PBF-S18/PBF-S25/PBF-S29/PBF-S30','Name':'PBF-S11/PBF-S19/PBF-S03/PBF-S17/PBF-S31','BeginSpeech':'PBF-S11/PBF-S19/PBF-S02','EndSpeechWin':'PBF-S11/PBF-S19/PBF-S01/PBF-S25/PBF-S31','EndSpeechLose':'PBF-S11/PBF-S19/PBF-S01/PBF-S25/PBF-S31','PokemonNos':'PBF-S11/PBF-S03/PBF-S02/PBF-S08/PBF-S01'}[k]) for k,v in x['fields'].items()},
  formal=['WP55§2.5/2.7/3','WP54§2/3/5','WP57§2'],pool_certificate='finite-pool-certificates.json record matching samefile and source_range',status='SOURCE_STATIC_FULL_RECORD_FIELDS'))
templates=[]
for i,line in enumerate((REF/'PBS/battle_tower_pokemon.txt').read_text(encoding='utf-8-sig').splitlines(),1):
 if not line or line.startswith('#'): continue
 fields=line.split(';')
 templates.append(dict(id='PBF-TOWER-%03d'%len(templates),path='PBS/battle_tower_pokemon.txt',line=i,index=len(templates),
  source_fields=dict(zip(['species','item','nature','EV_emphasis','ordered_moves'],fields)),
  subassertions=['Positionalcompiledidentity and actual default ID normalization PBF-S02/S11','Species/form/cache qualification PBF-S06/S07/S08 and TE01–05','Item identity setter/clause/snapshotrestore PBF-ITEM','Nature/table/PID/IV/EV exact creation PBF-S02/S26','Moves first4/filter/RETURN/currentstrict ban PBF-MOVE','Ordered source index referenced by each complete trainerpool, session/rental reference and save consumers PBF-S01/S03/S20–24/S31'],
  formal=['WP55§2.5','WP54§3/5','WP57§2'],status='SOURCE_STATIC_FULL_RAW_RECORD_FIELDS'))
put('forward-mapping.json',dict(schema='gr8.pbs-facility.forward/v1',reviewer='/root/pbs_creature_facility',source_units=units,trainer_records=forward,tower_records=templates,cup_peer_records='RC-CUP with all1888, not duplicated primary',dispositions={'BOM_and_wiki_firstline':'Nonruntime navigation comment; line parser skips, identity retained','separators':'No semantic rule in comment; source row order retained','trainer_section_labels':'Parsed but not trainer identity; all appearance order used, including300 repeated Trainer sections in alternativeFancy'},behavior='NOT_EXECUTED'))

rev=[]
def claim(id,doc,section,assertions,sources,status='SUPPORTED_BOUNDED_SOURCE_STATIC'):
 rev.append(dict(id=id,path='deliverables/final-specification-set/'+doc,section=section,subassertions=assertions,support_units=sources,status=status,behavior='NOT_EXECUTED'))
w54=formal[0]['path'].split('final-specification-set/')[1]; data54=formal[1]['path'].split('final-specification-set/')[1]
w55=formal[2]['path'].split('final-specification-set/')[1]; w57=formal[3]['path'].split('final-specification-set/')[1]; w76=formal[4]['path'].split('final-specification-set/')[1]
claim('REV54-COUNT',w54,'§2.1',['min1/rawmax0/negativepublic6','setNumber exactvs range','copy resets min and shares refs','subsetadd writes team','suggestedlastmin/max excludes teamtotal'],['PBF-S06','PBF-S07'])
claim('REV54-QUERIES',w54,'§2.2',['memberonly','registrableall team/max6','hasregistrable filteredcounts','hasvalid enumerates combos','final min/max→members→team→real subset order','errors and emptyinput boundaries'],['PBF-S07','PBF-S08'])
claim('REV54-ENTRY',w54,'§2.3',['realpartymultiselect consumer source accepted fromFAC','entry nilvs emptycommit','active submit reference write'],['PBF-S02','PBF-S01','RC-FAC'])
for name in ['Standard ordinaryability/namedpriority/BST','Height/Weight tenthsrounded limits','Baby sharedspecieskey cache','Unevolved validforward notNone cache','Species identicalbaseidentity','Item onlynonemptyidentity','StrictLittle exactitem/move/species lists','levelmin/max/total','otherall25definitions incl unused negative/nickname failure']:
 claim('REV54-PRED-%02d'%len(rev),w54,'§3',[name,'default andalternate data/createdform/inputstate premises retained'],['PBF-S08','PBF-ITEM','RC-TRAIT'])
claim('REV54-ADJ',w54,'§4.1',['All9adjustment classes','savecompleteEXP bothsides beforewrite','sidekind exact gating','targetperstrategy clamps andprefixdistributions','nestedadjustmenttypeignored','missingnullhelper defined failure'],['PBF-S06','PBF-S09'])
claim('REV54-RESTORE',w54,'§4.2',['heal first','adjust thenitem snapshot','noninternal andprepare','normalrestore bycurrentposition','equalEXPskipcalc','niloldEXPskip/itemclear','allpartialexceptionprefixes noensure'],['PBF-S04','PBF-S09','PBF-S27'])
for name in ['Pika','Poke','Prime','Fancy','Little','StrictLittle','Tower','Palace','Arena','Factory','StandardRules','StandardCup','DoubleCup','FancyCup','LittleCup','LightCup','mode1','mode2','othermode']:
 claim('REV54-FACTORY-'+name,w54,'§5',[name+' complete numbers/member/team/adjust/layout/battleflag configuration','factory vs directsample vs mode predicates not conflated','suggestedlevel totalcap contradiction retained where applicable'],['PBF-S06','PBF-S07','PBF-S01','RC-TRAIT','PBF-POOLS'])
claim('REV54-FLAGS',w54,'§6',['All14 setters exactkeys/layout','threeconsumeronlykeys no setter','effects not established by flagsetting alone'],['PBF-S10','RC-FAC'],'SETTERS_SUPPORTED_EFFECT_CONSUMERS_ROOT_COMBAT_REVERSE')
for sect,claims in [('§1',['All5listsections/currentFancyselection','alternativeFancy unselected but allrecordsread']),('§2',['All10factory+5sample rows exact fieldvalues','rawmin/max andsuggested distinctions']),('§3',['Complete finite fields species/form/ability/BST/high/weight/evolution inputs andall25restriction definitions']),('§4',['full ruleset/entry/adjustment/setter groups','inactiveexamples not active']),('§5',['source-staticscope/unknownhostandworld','dataexistence not runtime qualification'])]:
 claim('REV54-DATA-'+sect,data54,sect,claims,['PBF-S06','PBF-S07','PBF-S08','PBF-S09','PBF-S10','PBF-S14','RC-TRAIT'])
for sect,claims,src in [
 ('§2.1',['setup immediateparameters not Typefields','lazy6zerocounters','optional rules mode/setup unreachabletent','Factory extra+num3'],['PBF-S01']),
 ('§2.2',['all11tablefield write/read points','decision/endedquery','stringID<0 exception','explicitcounter progression','unique list fill','stateinvariants'],['PBF-S01','PBF-S03']),
 ('§2.3',['nil/empty/nonempty entry','originalreference snapshot','active submission','cancelretainedfields','endunconditionalpartywrite','recordrecover decisionbranches and cancel→end'],['PBF-S01','PBF-S02']),
 ('§2.4',['start/save regardlessdecision0','pause andresume both active','temporarylocation restore onfalse','unhandledexception skipsrestore','endonlynonzero save'],['PBF-S01','PBF-S20','PBF-S21','PBF-S22','PBF-S23','PBF-S24']),
 ('§2.5.a',['all15threshold rows/floorandnegative','IV8bands','N200unreachable199','emptytable/rand0 deferredfailure'],['PBF-S03','PBF-DOMAIN']),
 ('§2.5.b',['shortnofinalvalidation/longreplacement/no cap','all1600poolrecordjoins','completefinite eligibility andmatching vs runtimeevent input'],['PBF-S03','PBF-POOLS','RC-TRAIT']),
 ('§2.5.c',['firstmatchingnondefault/default/none','completecompiler6field+templateparse/data schema','allcurrentrecordIDvalues','ordinaryquote andobsoleteID cases'],['PBF-S02','PBF-S11','PBF-S12','PBF-S13','PBF-CSV','PBF-MOVE','PBF-ITEM']),
 ('§2.5.d',['normal NPCowner vs Factory defaultOwner','PID/nature/EVdivision/IVall/movetransform/happiness0/stats','dynamic creationform finitepremises'],['PBF-S02','PBF-S26','RC-TRAIT']),
 ('§2.6',['rentals6/selection3 andcounter','prepareswap previousparty','cancelunconditionalcommit'],['PBF-S01','PBF-S05']),
 ('§2.7',['intro/name/winlose exactmessage keys','typegraphicfallback','quickcheck/entrynil','mapteleportscenecondition'],['PBF-S01','PBF-S02','PBF-S16','PBF-S19','PBF-S25','PBF-S30']),
 ('§3',['organizednormal/debug','positionalrestore','localboolean vs noautosessionprogress','recordtransfer5tuple andtrainer metadata'],['PBF-S04','PBF-S09','PBF-S25','PBF-S31']),
 ('§4',['round0partialstate','missingtemplate andemptycandidate deferredreceiver failure','selectionandresamplingnontermination','savefalse vs propagate','cancel/endbeforestart','nohypotheticalaward'],['PBF-S01','PBF-S02','PBF-S03','PBF-S04','PBF-S23']),
 ('§5–7',['WS36 actualvectors andsixnewrows read','configuration references recorded','event/reward/host unknown separated fromavailablereadable source'],['PBF-S01','PBF-S14','PBF-S15','RC-FAC'])]:
 claim('REV55-'+sect,w55,sect,claims,src)
for sect,claims,src in [
 ('§2.1',['all2×8domains inclscaledinclusiveN','wins groups0..7 given nonnegative premise'],['PBF-S03','PBF-DOMAIN']),
 ('§2.2',['all8IV values','all6swapthresholds and perposition choice'],['PBF-S03']),
 ('§2.3',['rental6 vs oldmax+excludedlength','wholeconcatenatedvalidation','no cap','Nfailbeforevalidateandnumberrestore','successfulonlyrestore'],['PBF-S03','PBF-POOLS']),
 ('§2.4–2.5',['newnormalobjects/defaultOwner unchanged','allheld/moves/template writes','prepareorderandrandom3subset'],['PBF-S01','PBF-S02','PBF-ITEM','RC-TRAIT']),
 ('§3',['fullrentalloop noexit','confirm3/rejectthird','counter+1 andcommit'],['PBF-S01','PBF-S05']),
 ('§4',['bothscreen cancel/reselect/accept','reference slotreplace','successfulcounteronly','unconditionalcurrentrentalcommit','oldopponent sourcesnapshot'],['PBF-S01','PBF-S05']),
 ('§5–9',['allreference/owner/capacity/counter invariants','failure temporarynumbers','17FCvector rows read','host/replay/gen actualexecution unverified'],['PBF-S01','PBF-S03','PBF-S05','RC-FAC'])]:
 claim('REV57-'+sect,w57,sect,claims,src)
claim('REV76-TRAINERS',w76,'§8/9.3',['fullgeneratortrainerdefinition211lines','allpositional/typeweights andrefillinvalidstop','fromPokemon/writeoutput andallmatchingflags','checkpoint .dat thenPBS no transaction'],['PBF-S28','PBF-S11','PBF-S12'])
claim('REV76-OTHER',w76,'§3–7/9–10',['source all4generator facts received from actualFAC reader','parentfullformaltextread','no parent claim own3othergenerator fullsource','330moveeffects/whole species primary independently scoped'],['RC-FAC'],'FINITE_PEER_SOURCE_RECEIPT_PARENT_SOURCE_REREAD_NOT_CLAIMED')
claim('REV04-CSV','generic-kernel/wp04-pbs-lifecycle.md','§4.2',['oddquoterecombination','literalbackslashdoublequote+position stripping','ordinaryouterquotesretained','getCSVschema singlevsrepeat behavior','quotes do not protectcomments'],['PBF-S11','PBF-S13','PBF-CSV'])
catalogs=[('test-catalog/combat-requirements-wp54-55-56-58.md',{'QC':'PBF-S06/S07/S08/S09/S10 andFAC fullbattleclause primary','WS':'PBF-S01/S02/S03/S04/S19/S23 andcomplete pools','PA':'FAC originalPalace/Arena source reception, not ownfullsource','RC':'FAC originalRecord source reception; ownmetadata/transfer receiveronly'}),('test-catalog/creature-rpg-wp35-36-57-64-68.md',{'FC':'PBF-S01/S03/S05'}),('test-catalog/demo-dx-wp72-73-74-75-76-77.md',{'GN':'FAC-R19/R20/R21/R22 plusownS28','B17':'SOURCE_STATIC vector only; no reference/modelexecution'})]
catalog_rows=[]
for path,families in catalogs:
 family=None
 for line_no,line in enumerate((SPEC/'deliverables/final-specification-set'/path).read_text().splitlines(),1):
  if line.startswith('## '):
   family=next((k for k in families if line[3:].startswith(k)),family)
  if not line.startswith('|'): continue
  key=line.split('|')[1].strip()
  active = key.startswith(tuple(families)) or ('GR7-M12-001' in key and 'combat-requirements' in path)
  if 'combat-requirements' in path and family in families:
   active = active or bool(re.fullmatch('[QWAP][0-9]+[a-z]?', key))
  if active:
   fam=next((k for k in families if key.startswith(k)),family or 'WS')
   catalog_rows.append(dict(path='deliverables/final-specification-set/'+path,line=line_no,claim_id=key,whole_row=line,support=families[fam],reading='Fullactualrowread; rowcapture is navigation notsemantic substitute',behavior='NOT_EXECUTED',status='SOURCE_STATIC_BOUNDED_INTERFACE' if fam not in ['PA','RC'] else 'RECEIVED_FAC_SOURCE_NOT_OWN_FULLSOURCE'))
put('reverse-mapping.json',dict(schema='gr8.pbs-facility.reverse/v1',formal_reading=formal,manual_claim_groups=rev,catalog_rows=catalog_rows,scope='All manual subassertions remain bounded; not punctuationsplit inventedglobalclausecensus. WP54 battle effect clauses/fullAI/move primary independent reverse under root, own installedkeys/eligibility proved.',unreceived_external=['Independent global formal reverse acceptance by differentcontext/root','Battleprimary complete330rawmove-ID semantic effects and linked held triggers, beyondqualification/reference identity','Actualhost compiled registry/save/media/event sequence NOT_EXECUTED; source material not reclassified limit'],behavior='NOT_EXECUTED'))
put('proposals.json',dict(schema='gr8.pbs-facility.proposals/v1',proposals=[],new_required_candidates=0,reason='All finite edgecases here already supported by currentWP04/WP54/WP55/WP57/WP76 general contracts; supplemental data-specific evidence is not itself a formal defect.',examined=[dict(id='PBF-OBS-LEGACY',observation='Tower STICK→nil andVICEGRIPdrop under currentdefaultIDs',disposition='Existing unknownIDparse contract; no universal source-data invariant contradicted'),dict(id='PBF-OBS-CSV',observation='Ordinaryquotedcomma speech completebutliteralquotes; source stripping requiresbackslashquote/position',disposition='WP04§4.2 alreadyaccurate; no newrequired'),dict(id='PBF-OBS-POOL',observation='Pika/Poke/Fancy fixed suggestedlevels vs totalcap rejectall3draws',disposition='Existing suggestedlevel/teamtotal/retry contracts compose; proofevidence, no claim formal guaranteestermination'),dict(id='PBF-OBS-CACHE',observation='Priorforme.gPICHU2 can changeLittlemembership',disposition='WP54 sharedspeciescache alreadyexplicit; coldpremisepreserved')],independent_review='Child actual differentcontext mathematicalcheck; not masquerading as nonauthorproposalacceptance; no requiredsent fordecision',behavior='NOT_EXECUTED',update='UPDATE_NOT_STARTED'))
progress=load('progress.json')
progress.update(updated_utc=NOW,state='STATIC_REVIEW_DELIVERED_BOUNDED_RECEPTIONS',source_read_cursor='Primary7 allrecords/fields0unread;31 own supplementalunits fullorselected exactranges; finitepeer joins accepted with outerglobal boundaries explicit',unreceived='Global independent formal reverse/battle effects/host event composition remain root scoped; no local primary unread',local_primary_unread_records=0,local_receiver_semantic_unread_units=0,supplemental_source_paths=len(identities['supplemental_reference']),formal_paths=len(formal),manual_reverse_groups=len(rev),catalog_rows=len(catalog_rows),end_utc=NOW)
put('progress.json',progress)
print(json.dumps(dict(primary_files=7,primary_bytes=535742,trainer_records=len(forward),tower_records=len(templates),supplemental_paths=len(units),formal_paths=len(formal),manual_reverse_groups=len(rev),catalog_rows=len(catalog_rows),identity_matches=identities['supplemental_identity_matches'],recorded_utc=NOW)))
