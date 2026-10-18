"""Serialize manually reviewed finite facts; inspect Git bytes, never execute game code."""
import datetime, hashlib, json, re, subprocess
from pathlib import Path

ROOT=Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e')
OUT=ROOT/'tasks/creature_e_factory_completion_cloud'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B='fd1df570cad987dc3852a3b958f03916e317f7fe'
RT='7589c800b61ba13a13040ed0d686979b80a84fd0'
BT='751dfde81048c81390f89a65ca1d1a565ba8e1ca'
FT='f292698cdd4a8e725525a9be6dc34b75faaf151e'
READER='/root/creature_e_factory_completion_cloud'
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
PREFIX='Data/Scripts/018_Alternate battle modes/'
paths={
 'S1':PREFIX+'001_Battle Frontier/001_Challenge_BattleChallenge.rb',
 'S2':PREFIX+'001_Battle Frontier/002_Challenge_Data.rb',
 'S3':PREFIX+'001_Battle Frontier/003_Challenge_ChooseFoes.rb',
 'S4':PREFIX+'001_Battle Frontier/004_Challenge_Battles.rb',
 'S5':PREFIX+'001_Battle Frontier/005_UI_BattleSwap.rb',
 'S6':PREFIX+'003_Battle Frontier generator/001_ChallengeGenerator_Data.rb',
 'S7':PREFIX+'003_Battle Frontier generator/002_ChallengeGenerator_Pokemon.rb',
 'S8':PREFIX+'002_Battle Frontier rules/001_Challenge_ChallengeRules.rb',
 'S9':PREFIX+'002_Battle Frontier rules/002_Challenge_Rulesets.rb',
 'S10':'Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb',
 'S11':'Data/Scripts/015_Trainers and player/001_Trainer.rb',
 'S12':'Data/Scripts/014_Pokemon/004_Pokemon_Move.rb',
 'S13':PREFIX+'003_Battle Frontier generator/003_ChallengeGenerator_Trainers.rb',
 'S14':'Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb',
 'D1':PREFIX+'002_Battle Frontier rules/003_Challenge_EntryRestrictions.rb',
 'D2':PREFIX+'002_Battle Frontier rules/004_Challenge_LevelAdjustment.rb',
 'D3':'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',
 'D4':'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb',
 'D5':'Data/Scripts/014_Pokemon/001_Pokemon.rb',
 'D6':'Data/Scripts/002_Save data/004_Game_SaveValues.rb',
 'D7':'Data/Scripts/012_Overworld/002_Overworld_Metadata.rb',
 'D8':'Data/Scripts/003_Game processing/001_StartGame.rb',
 'D9':'Data/Scripts/016_UI/018_UI_ItemStorage.rb',
 'D10':'Data/Scripts/016_UI/006_UI_Summary.rb',
 'D11':'Data/Scripts/013_Items/001_Item_Utilities.rb',
 'D12':'Data/Scripts/007_Objects and windows/002_MessageConfig.rb',
 'D13':'Data/Scripts/001_Settings.rb',
 'D14':'Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb',
 'D15':'Data/Scripts/010_Data/001_GameData.rb',
 'D16':'Data/Scripts/001_Technical/002_RubyUtilities.rb',
 'D17':'Data/Scripts/001_Technical/003_Intl_Messages.rb',
 'P1':'PBS/battle_facility_lists.txt','P2':'PBS/battle_tower_pokemon.txt',
 'P3':'PBS/battle_tower_trainers.txt','P4':'PBS/trainer_types.txt',
 'F1':'deliverables/final-specification-set/creature-rpg/wp57-factory-rentals-and-swaps.md',
 'F2':'deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md',
 'F3':'deliverables/final-specification-set/combat-requirements/wp55-facility-session-and-restoration.md',
 'F4':'deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md',
 'F5':'deliverables/final-specification-set/combat-requirements/wp54-entry-rules-and-cup-data.md',
 'F6':'deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md',
}
def git(repo,*args):return subprocess.check_output(['git','-C',repo,*args])
def source(k):
 formal=k.startswith('F');repo='/workspace/pokemon-essentials-clean-room' if formal else '/workspace/pokemon-essentials'
 commit=B if formal else R
 return git(repo,'show',commit+':'+paths[k])
def ident(k):
 b=source(k); formal=k.startswith('F');repo='/workspace/pokemon-essentials-clean-room' if formal else '/workspace/pokemon-essentials';commit=B if formal else R
 return {'id':k,'repo':repo,'commit':commit,'tree':BT if formal else RT,'formal_subtree':FT if formal else None,'path':paths[k],'mode':'100644','git_blob':git(repo,'rev-parse',commit+':'+paths[k]).decode().strip(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(b.splitlines())}
IDENTS={k:ident(k) for k in paths}
def pointer(p,selection=None):
 b=(ROOT/p).read_bytes();x={'path':p,'mode':'100644','bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'publication_commit':'ROOT_SOLE_PUBLISHER_PENDING'}
 if selection:x['complete_object_selection']=selection
 return x
def dump(n,d):(OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

COMMON={'reader':READER,'evidence':'SOURCE_STATIC','business':'NOT_EXECUTED','premise':'Fixed R/B8, normal nonnegative session counters and valid dependencies returning normally through the named observation, no later override. Failure prefixes are retained; no claim of native output, every template constructability, rejection-loop termination or Demo reachability.'}
units=[]
def u(k,a,b,label,facts,receivers,disposition='FACTORY_PRIMARY_OR_NECESSARY_INTERFACE'):
 units.append({'id':f'FF-U{len(units)+1:03}', 'source':k,'range':[a,b],'structure':label,'facts':[{'id':f'FF-F{sum(len(z["facts"]) for z in units)+i+1:03}','meaning':f} for i,f in enumerate(facts)],'formal_receivers':receivers,'disposition':disposition,**COMMON})

u('S1',4,77,'BattleChallenge identity, initialize/set/register/rules/modeToRules',[
 'A fresh challenge owns reset session data, current identity -1 and empty per-identity records. Set stores identity, rounds and supplied rules before register; double substring/factory prefix/open suffix provide immediate registration arguments, then debug cup writer is requested.',
 'Factory registration installs fresh extra data, forces the immediate missing-rules count to3 and battle type to Tower; already supplied rules are retained. It does not rewrite the type record readers or force an already supplied double ruleset from4 to3.',
 'Absent rules are generated from mode and immediate arguments. Arena forces single; other/Factory battle type is Tower. Mode1/2/default use Standard max100/100/50 and opponent-only Open lower30/60/50, distinct from the explicit Factory rule helper.',
 'A missing type is lazily created; six counters initialize zero, but layout/count/battle-type/mode reader fields are not assigned here.'
],['F1:17,108','F3:19-24','F4:105-113','F5:22,39-47'])
u('S1',79,176,'BattleChallenge outer start/end/battle, query and forwarding methods',[
 'Start resolves type and writes current identity before inner start. End recovers active-type counters before clearing identity and invoking inner end.',
 'Battle dispatches to extra Factory data when present; otherwise builds a normal trainer from its own candidate-number list. These are different individual-owner paths.',
 'Forwarders expose inProgress/resting/counts/nextTrainer and pass explicit progression/cancellation/party submissions to session data. Battle result does not itself advance wins or write decision.',
 'Data query inactive returns nil; active string current identity fails numeric comparison before its clone expression. The six direct historical-count queries access the live type record.'
],['F1:13,89-94','F3:26-57'])
u('S1',181,229,'BattleChallengeData initialization, extra-data/party setters and complete start',[
 'setParty immediately writes player.party only while inProgress, then stores exactly the supplied list reference; outside progress it only updates registration.',
 'Start writes active/resting=false/decision0/current swaps/current wins/battleNumber1/trainers[] before rejecting nonpositive rounds; rejection does not reach location/original-party capture or save.',
 'Positive rounds are stored; trainer indices use wins+filled length, rejecting duplicate equal indices until full, without bound. Location and original party reference are captured only after this finishes.',
 'A stored truthy party, including an empty list, replaces player.party; safe save is requested afterward while decision0. False save return does not undo state.'
],['F1:17,69,81,89,91','F3:26-65'])
u('S1',231,286,'GoToStart, add-win/add-swap, match-over, rest/continue/cancel/end/nextTrainer',[
 'Add-win changes wins and battleNumber together only while active; add-swap changes swaps only while active. Match-over is inactive/nonzero-decision/battleNumber beyond rounds.',
 'Rest and continue change resting only while active and call the start-position save helper; neither clears inProgress.',
 'Cancel restores original party when its reference exists then resets immediate session state, without save or refresh. End writes oldParty unconditionally before the active guard, and active end resets/refreshes then saves only a prior nonzero decision.',
 'nextTrainer reads trainers[battleNumber-1]. GoToStart transfers only in Scene_Map, faces up and dismounts; missing maps/events do not prove playable reception.'
],['F1:89-94','F3:44-65'])
u('S1',292,362,'reset, pbSaveInProgress and BattleChallengeType initialize/saveWins',[
 'Reset clears active/resting/start/decision/wins/swaps/battleNumber/trainers/oldParty/party/extra, retaining inner numRounds and outer identity/rules/type records.',
 'The save helper captures live map/x/y/direction, temporarily writes the saved start/up state, calls safe save, then restores on normal return including false. Propagated exceptions skip the tail; no local ensure restores position.',
 'Type counters all start zero. Undecided end zeros only current wins/swaps; winning end keeps current session counts; other nonzero decisions zero current. Decided endings update previous and maxima.',
 'Cancel then end is not an all-object no-op: outer retained identity can still recover zero current counters and inner cleared oldParty can write nil before returning inactive.'
],['F1:89,91,93','F3:50-65,123-134'])
u('S1',368,386,'Factory initialize and pbPrepareRentals',[
 'Factory data stores its associated session reference. Initial generation saves all six rentals before reading next trainer and building the new NPC.',
 'The selected trainer record supplies name/type and loss/win message keys; Factory does not use its PokemonNos field to generate the opponent.',
 'The full rental candidates are exclusions for opponent generation; the returned opponent candidates are sampled for3 object references and assigned as NPC.party.',
 'Failures keep the reached prefix: rentals may already be replaced, opponent allocated or message fields assigned before candidate generation fails.'
],['F1:17,57,83','F3:97-105'])
u('S1',388,395,'pbChooseRentals',[
 'The fade block creates the rental UI, replaces rentals with its successful returned object-reference list, asks active counter to add1, then submits that same list.',
 'The normal UI returns3; inactive direct use still updates registration but add-swap does not change count or active player.party.',
 'There is no transactional rollback for an exception after UI return or after count increment. External fade cleanup does not reverse business writes.'
],['F1:63-69,89-94'])
u('S1',398,412,'pbPrepareSwaps',[
 'Previous opponent.party is captured by reference before replacing the opponent trainer object.',
 'New trainer wrapper uses its own selected name/type/lose/win fields; exclusions are a new concatenation of current rentals followed by old opponent members.',
 'New candidates are sampled for3; generating the new opponent does not replace the retained old-opponent party reference.',
 'An exception can leave oldopponent assigned and a new incomplete opponent; no save/party restore is implied by this preparation.'
],['F1:57,83,94'])
u('S1',414,429,'pbChooseSwaps and Factory pbBattle',[
 'Swap UI receives the current rental list and old-opponent list. A true return adds a swap through the active-only counter; false does not.',
 'setParty(rentals) runs for either normal Boolean return, including quit. The wrapper returns the UI Boolean only after the fade block completes.',
 'A completed accepted swap edits the same rental list before the wrapper count and submission; active player.party/registration can already share it.',
 'Factory battle delegates the prepared opponent and current challenge rules to the ordinary organized-battle wrapper; no automatic preparation/progression is added.'
],['F1:75-94','F3:103-121'])
u('S2',4,50,'Lazy challenge, battle/eligibility entrypoints, two independent list loaders, entry screen',[
 'Global challenge is created lazily and reused. Convenience battle/eligibility use current challenge rules and active player.party.',
 'Trainer and Pokemon loads are independent: load exceptions become[], first nondefault matching challenge wins, else first default wins, else[]. Matching entry content can itself be empty; no fallback based on its emptiness.',
 'Entry UI cancellation nil does not submit. Truthy list results including[] submit; return then tests length>0. This is separate from Factory rental UI.'
],['F1:49,57,69,81,89','F3:52,97-105'])
u('S2',55,96,'moveto2, event status, opponent graphic and begin speech',[
 'The start-location helper writes tile/real coordinates and prelock direction directly. Event in-challenge exposes global active state.',
 'Opponent graphic uses selected trainer type charset, then NPC01 on absent/empty or protected bitmap branch exception; exceptions before begin or in fallback are not guaranteed caught.',
 'Intro speech returns ellipsis inactive or absent trainer; otherwise translates record BeginSpeech. Graphic/text requests are not host display observations.'
],['F1:57,108-114','F3:107-114'])
u('S2',101,164,'PBPokemon attributes, fromInspected, fromPokemon and initialize',[
 'Template parsing trims, splits semicolon fields, recognizes species/item/nature through their registries (unknown becomes nil), maps HP/ATK/DEF/SA or SPATK/SD or SPDEF/SPD emphasis tokens, ignores other stat spellings.',
 'Only first MAX_MOVES input move slots are considered; unknown moves are omitted in order, and zero accepted moves uses first registry key. Ordered/repeated EV entries remain.',
 'fromPokemon keeps species/current item/nature, up to four move IDs and those main EV entries strictly>60. Template initializer normalizes recognized item or nil and retains other inputs.',
 'Missing field strings can fail at split; parser existence is not a claim all fixed raw spellings are current registered/constructible.'
],['F1:49,53,100,108','F3:99-101'])
u('S2',166,219,'Template inspect/tocompact, disabled serialization samples, convertMove/createPokemon',[
 'Inspect emits canonical recognized identities and ordered EV/move representation; unused compact text and commented dump/load are authoring/navigation, not an active alternate loader.',
 'createPokemon first invokes normal constructor with default move filling disabled, then template item, rerolled32bit PID, nature and happiness0; moves are fresh records, RETURN changes to FRUSTRATION only if that identity exists.',
 'Every listed EV slot gets integer EV_LIMIT/entry count (repeated entries affect divisor); all main IVs get supplied value; final stats recalculate. Empty emphasis does not add EV writes.',
 'Passing nil trainer produces constructor default Owner0/empty/2/2; later NPC.party assignment and swapping do not rewrite it. Construction may have normal constructor/form-hook effects and can fail before final validation.'
],['F1:49,53,79,83,93','F3:101'])
u('S3',6,83,'Trainer selector and ordinary opponent path',[
 'Trainer selection uses the highest satisfied win lower bound among0,6,7,13,14,20,21,27,28,34,35,41,42,48,49; respective starts/lengths are0/100,80/40,80/40,120/20,100/40,140/20,120/40,160/20,140/40,180/20,160/40,200/20,180/40,220/40,200/100.',
 'Start and length independently scale by trainer count integer-divided300; result is scaled start+rand(length). Negative wins return0; zero random argument is a distinct host/native return-type boundary, not Factory empty-pool random-bound1.',
 'Ordinary opponent path uses selected PokemonNos, suggested count/level, trainer-index IV stair and actual NPC owner. Short candidate-number list constructs all without fill/final team check; long samples with replacement until valid without bound.',
 'Factory uses the same trainer selector for schedule but bypasses this normal PokemonNos generation path.'
],['F1:53,57,108','F3:67-101'])
u('S3',88,124,'Factory pool selection and all sixteen endpoint table rows',[
 'Pool uses current challenge list loader; suggested level is read before temporary count changes. Group=min(wins integer-divided7,7). Open table is chosen by suggested level exactly equal to configured maximum, not by challenge-name suffix alone.',
 'Ordinary endpoints by groups0..7 are[0,173],[174,272],[273,371],[372,491],[492,610],[611,729],[730,849],[372,881]. Open endpoints are[372,491],[492,610],[611,729],[730,849] then[372,881] four times.',
 'Both endpoints multiply actual template count and integer-divide881 separately. Fixed default pool contains882 raw templates; the881 divisor is a source constant, not its actual record count.',
 'The vector pool sizes881/100/0 are explicit independent fixtures; they do not silently replace the actual default882.'
],['F1:30-41','F2:FC-01..04,FC-16..17'])
u('S3',125,164,'Factory IVs, swap thresholds, temporary rule count, draw/validate/retry/restore',[
 'IV table[3,6,9,12,15,21,31,31] supplies current group and next group capped7. Lower-IV threshold starts6 and becomes5/4/3/2/1 at swaps15/22/29/36/43; position before appending selects IV.',
 'Original min/max are retained. No exclusions sets exact count6 and constructs6; nonempty exclusions sets count old_max+exclusions.length and constructs old_max. Final validation receives fresh new-party+exclusion concatenation.',
 'Each draw includes both endpoints with positive integer span=end-start+1, does not remove prior choices, constructs fresh individuals with nil trainer, and appends; duplicate species/items are rejected only by the complete team predicates.',
 'Validation failure clears attempt and repeats without bound. Normal success restores original bounds. Selecting endpointN or empty pool index0 yields missing template and creation failure before final validation/restoration; no local ensure.'
],['F1:45-53,90-94','F2:FC-05..08,FC-13..17'])
u('S4',4,35,'BattleType/Tower/Palace/Arena constructors',[
 'Tower creates recorded battle using actual trainer party references; basic/Palace/Arena constructors are other facility types read for dispatch distinction.',
 'Factory extra delegates organized wrapper whose rule battle type normally remains Tower; no assumption of clone or owner change is introduced.'
],['F1:89,93,108','F3:118-121'],'NECESSARY_DISPATCH; NONFACTORY_VARIANTS_OTHER_FAC_OWNER')
u('S4',40,97,'Complete organized battle wrapper',[
 'Debug+CTRL branch displays skip/win/opponent lose messages, then clears temp record/stopsME/returns true; it precedes healing and adjustment.',
 'Normal path heals player first, adjusts levels (retaining both sides oldEXP), then stores current held-item identities, creates battle, sets internalBattle=false, prepares and runs it.',
 'Normal return unadjusts EXP by current position, then each player before opponent heals/unmega/unprimal/restores item by saved position; missing item position writesnil. Uncaught failures skip all remaining tail, not a rollback.',
 'Only after cleanup temp record is cleared, optionally replaced for decision1/2/5; wins stat for1, losses for2/3/5; only1 returns true. Session wins/decision/swaps are untouched by this wrapper.'
],['F1:13,17,89,93,108-114','F3:116-134','F4:72-103'])
u('S4',102,144,'record/play/debug-play/file entrypoints',[
 'RecordLastBattle copies temp record to global lastbattle and clears temp; replay chooses mode from restored record, uses abortable scene and battle animation.',
 'Debug choose/file replay definitions are fully read but belong to WP58; WP57 explicitly excludes replay and does not inherit execution or native-load success from their presence.'
],['F1:21-22,109-116'],'OTHER_OWNER_WP58; WP57_SCOPE_DISPOSITION')
u('S5',4,82,'BattleSwapScene rent/swap construction, init/end, command/confirm adapters',[
 'Rental/swap modes use their respective retained object lists, titles/backgrounds/list/help/message windows, initialized hidden message window, deactivate/fade-in and update callbacks.',
 'Initial swap commands are current members+CANCEL, focus0, mode1. Normal end fades out/disposes sprite hash then viewport; no scene-local ensure promises cleanup after failure.',
 'Command and confirmation use UIHelper with scene-update callback; confirmation false includes explicitNo or BACK after text finishes. Native graphics/input/selection timing are unobserved.'
],['F1:63-81'])
u('S5',83,158,'commands/choose/choices/swapChosen/canceled/summary/update',[
 'Labels use speciesName/category and selected red text. Rental help is first/second/third from chosen count. Rental choose(false) ignores BACK; swap choose(true) maps final CANCEL to-1 and penultimate mode2 rechoose to-2.',
 'Second swap screen lists old-opponent members, PKMN FOR SWAP and CANCEL; rechoose resets first screen. Choosing indexes is not an independent ruleset revalidation.',
 'Summary fades surrounding sprites, passes the same list/index to default nonbattle PokemonSummaryScreen, sets list cursor to its returned index, then restores visibility. That shared Summary contract can mutate held items/move order/marks; no Factory read-only guarantee follows.',
 'Update delegates sprite hash updates. Unknown malformed index or host failure has no local all-state rollback.'
],['F1:63-83','F6:136,168,172-190'])
u('S5',163,206,'BattleSwapScreen initialize and complete rental state machine',[
 'Chosen indices startempty; each selected row offers Summary, Rent or Deselect, Others. Summary returns to selection; Others/menu BACK have no rent action.',
 'Deselect removes that index and refreshes chosen clone. New choice appends in selection order and refreshes; exactly3 opens confirmation.',
 'Yes constructs a new3-element list of the selected original object references and ends scene before returning it. No removes only the just-added third index, refreshes and loops.',
 'There is no normal cancellation exit. This normal-return guarantee assumes valid list/input/UI dependencies; it does not assert every malformed/exceptional call returns.'
],['F1:63-69','F2:FC-07,FC-09'])
u('S5',208,247,'Complete two-screen swap state machine',[
 'First screen Summary returns; Rechoose/no command returns to list. Swap records current member slot then enters acceptance loop.',
 'AcceptNo stays second screen. AcceptYes first ends scene, then assigns current[slot]=oldOpponent[selection] by reference and returnstrue; no field copying/owner reassignment/local level or item reset.',
 'Second rechoose(-2) returns to first screen; either screen cancel(-1) asks Quit, withNo staying its own loop andYes ending scene and returningfalse.',
 'False does not assign a rental slot in this method; it does not roll back preceding shared Summary mutations, nor prevent the wrapper unconditional setParty.'
],['F1:75-94','F2:FC-10..12,FC-15'])
u('S6',4,108,'Tier restriction classes, withRestr and pbArrangeByTier',[
 'BST inclusive restriction; nonlegendary allows gendered first, rejects genderless Undiscovered; inverse negates. withRestr constructs fresh restrictions and ignores its _rule parameter except outer filtering.',
 'Nine tier bands are0..500nonlegendary,380..500nonlegendary, four400..555nonlegendary,580..680legendary,500..680nonlegendary,580..680any. Original rule filters first; eligible tier is selected proportionally to original list position.',
 'Each tier sorts BST ascending then species, concatenating. This is authoring rank order that can become Factory pool order, not the runtime eight-group table itself.'
],['F1:100,109,113'],'WP76_NECESSARY_AUTHORING_INTERFACE; FULL_LOCAL_DEFINITIONS_READ')
u('S6',113,166,'replenish/duplicate/removeDuplicates',[
 'Replenish requests random legal candidates until party20, rejecting duplicates without bound.',
 'Duplicate requires same species, then same move arrays in their original slots (compact/sort expressions are unused), or same item/nature/all main EVs. Padding to MAX_MOVES means the four-slot comparison includesnil.',
 'Remove duplicates retains order, drops an exact duplicate, and when a species already appears10times deletes its first prior row before appending. WP76 owns these pool-building meanings; no runtime Factory dedup substitute is introduced.'
],['F1:100,109,113'],'OTHER_OWNER_WP76_POOL_AUTHORING_READ')
u('S6',171,271,'Complete pbGenerateChallenge local control flow',[
 'Generator copies rule and sets2, loads cached party/teams with[]fallback; fewer10teams seeds party from current content templates at suggested level/IV31/nil trainer, filtering individuals, then deduplicates.',
 'Eleven iterations use maxteams600, cutoff65, low40: saves party/teams at named stages, replenishes20, replaces weak/short/retired teams, deletes beyondmax only in its ordered elsif branch, fills teams and simulates.',
 'Simulation other draw performs five assignments with next applying only inside that inner loop; final self-match is skipped. Local rounds continue until mean games>=12, then ratings update/sort/save.',
 'Final teams ascending rating contribute only>65, dedup then tier-arrange, then pbTrainerInfo writes trainer/pool output. External rating/battle internals are WP76 owner; not necessary to approve all combat to state Factory consumes ordered output.'
],['F1:21-22,109,113-116'],'WP76_LOCAL_ALGORITHM_FULL_READ; NO_FULL_TRANSITIVE_GENERATOR_APPROVAL')
u('S6',276,338,'Complete debug cup writer',[
 'No debug returns before prompts. Missing list offers yes/no; existing list offersNo/useExisting/useNew. No returns; choose-existing cancellation returns without routing writes.',
 'Choosing existing removes id from every nondefault challenge list, adds it only to selected nondefault list, saves trainer_lists then exports PBS. Choosing default relies on fallback rather than addingid.',
 'New generation requires confirmation, runs callback UI updates and local generator, then disposes message window and announces complete only on normal path. Errors retain preceding writes; this does not turn arbitrary future content into fixed current inputs.'
],['F1:109,113-116','F3:21,99','F4:113'])
u('S7',1,139,'Generator caches, BST/baby/minimum/evolution helpers, random/legal/add/power move definitions',[
 'Global caches retain BST/baby/minlevel/evolutions by species; legal moves cache resets on level change, TM move catalog is lazy. Random Sketch move excludes Struggle and Sketch-function identities and repeats withoutbound.',
 'Legal moves add eligible level moves, machine-backed tutor moves and baby egg moves with weights; exclusions/pruning compare function/type/power/accuracy/PP; Bubble/BubbleBeam never add.',
 'Weights use ordered overrides: base+1, low-power base,>=60/protection base+2,>=80Normal or listed utility base+3. Stronger move query compares same type and larger positive power.',
 'These definitions are fully read as WP76 pool authoring and do not alter runtime Factory sampling once the ordered template pool is loaded.'
],['F1:100,109,113'],'OTHER_OWNER_WP76_CANDIDATE_AUTHORING_READ')
u('S7',144,359,'Complete random-rule candidate creation',[
 'Outer attempts alternate strength bias, sample only form0 species, reject minimumlevel and probabilistic BST/baby/evolution conditions, choose each EV emphasis by50%, and repeatedly choose nature with its specifiedneutral/Lax/Gentle andEV emphasis gates.',
 'Forty-one item literals plus forced Leftovers branch apply species/BST/item gates; berries can addEV emphasis, low/highlevel Oran/Sitrus substitutions, then move sampling/Sketch replacement and compatibility retries operate.',
 'Four-move sampling rejects weaker same-type50%, Stockpile/SpitUp/Swallow mismatch, SleepTalk/Snore withoutRest except conditional20%, emphasis mismatch80%, totalpower gates, then updatesEV emphasis and item compatibility.',
 'Final held-item replacements cover SilkScarf/LightClay/BlackSludge/HeatRock/DampRock and Rest berries; creates template then individual IV31 with supplied trainer; only individual rule success ends. Caches can be mutated and retries unbounded. Complete caller success is not asserted.'
],['F1:100,109,113'],'OTHER_OWNER_WP76_CANDIDATE_AUTHORING_READ')
u('S8',4,118,'Complete challenge rule container and wrappers',[
 'Container defaults new ruleset/Tower/no adjustment/empty battle rules. Copy clones ruleset lists but retains rule/adjustment/battle-type references.',
 'Count/layout setters forward; double sets4, single3 and adds a layout rule. Setting an additional count later does not remove layout.',
 'Adjust/unadjust dispatch only if strategy/records exist; create battle delegates type then applies battle rules in order. Entry/team/level adders use their actual ruleset paths.'
],['F1:49,53,90,92,108','F4:17-27,72-113'])
u('S8',123,382,'All active cup helpers, explicit Factory helper and dormant block examples',[
 'Explicit Factory open uses fixed100+max100, otherwise fixed50+max50, bansUNOWN, adds different-species/items and SoulDew battle clause, then single3/double4. It does not add standard/nonegg/able restrictions.',
 'Ten active helpers and dormant commented historical examples are read; nonFactory cup restrictions remain WP54/FAC owner. Explicit Factory helper differs from modeToRules and from register immediate forced3.',
 'The historical block is nonexecuting authoring material, not extra current default rules.'
],['F1:17,53,90-92,108','F4:105-113','F5:7-47'])
u('S9',4,224,'Complete ruleset methods',[
 'New ruleset min1/rawmax0; max<0 exposes MAX_PARTY_SIZE; input maximum is max(partyconfig,max). setNumber/Range clamp eachendpoint>=1 without ordered-range or6cap guarantee. Copy resetsmin1 and shares rule objects.',
 'Suggested level uses last min/max restrictions and separate subset total; normal addSubsetRule actually appends team rules. Final team validity checks length then individuals then allteam then subset in order.',
 'Species duplicates and held-item duplicates are complete-team predicates, not draw-level filters. Exclusion members participate in the same concatenated final check.',
 'Full registration/existence/copy/clear helpers are read as upstreamWP54 behavior; Factory consumes exactcounts/suggestedLevel/isValid and does not gain a stronger invariance/termination promise from them.'
],['F1:49,53,90-94,108','F4:15-49'])
u('S9',229,323,'Standard and direct cup samples',[
 'Standard initializesnumber and standard/species/item restrictions plusoptionalmaximum; min remains1 unless count set later. Five direct cup sample constructors are fully read and belongWP54.',
 'These are separate from explicit Factory helper; default-mode generation uses Standard, so fixedFactory-clause claims are conditional on suppliedFactory rules.'
],['F1:108','F4:105-113','F5:26-47'],'OTHER_OWNER_WP54_EXCEPT_MODE_DEFAULT_INTERFACE')
u('S10',4,73,'Complete owner object definition',[
 'Owner validates id/name/gender/language and retains those values; trainer conversion builds a new record from trainer fields, foreignID helper is separate.',
 'All four setters validate and assign; public id is lower16bits. Factory passesnil and constructor suppliesOwner(0,empty,2,2), so it is not the NPCtrainerrecord nor absenceofowner.'
],['F1:53,79,83,93','F2:FC-15'])
u('S11',4,194,'Complete Trainer/NPCTrainer definitions',[
 'Trainer normalizes trainerType, retainsname, draws32bitid, getslanguage and initializesparty[]; NPC adds version0/items[]/nilwin/losetext. party is a direct writable attribute, so assignment does not traverse/reown members.',
 'Fullname/type/gender/resource-related readers delegate type data. heal_party calls eachmember.heal in order. Collection queries filter egg/HP as defined, removal has its separatelastable guard.',
 'Factory uses constructor and party assignment only; permanent collection helpers do not run simply because rentals become activeparty.'
],['F1:53,57,79,83,89,93','F3:101,118'])
u('S12',4,77,'Complete Pokemon::Move definition',[
 'Move constructor strictly resolvesidentity, initializesPPUp0 and fullPP; id/PP/PPUp writers clamp currentPP to currentmaximum; totalPP usesbase+base*ups/5.',
 'Data/display methods delegate currentMove registry; freshtemplate move records do not imply effect execution. None of these writers changesOwner.'
],['F1:53,79,108','F3:101'])
u('S13',4,211,'getTypes and complete trainer allocation/writer',[
 'getTypes clonescurrent species types. Existingtrainer/template listsload separately; no trainer data triggers200generation, whose nonYoungster retry branch lacks a break and can fail toterminate.',
 'Candidate levels normalizedtosuggested; validity andtypes captured; trainerexistingPokemonNos define species/types preference. Weightedrank/type selection and fallback fill update orderedindices, dedupthen sort.',
 'Every outputtrainer keeps type/name/intro/win/lose and newlyassignedindices. Creaturelist converts throughfromPokemon, retainingliteral identity/EV/moves conversion behavior.',
 'Output searches routingentries includingchallenge, replacesmatchingrecords and defaultflag basedonpriorDefault, otherwise appendsnamedtrainer/pokemonfiles; save_data precedesPBSexports. Prefixes surviveexceptions. Fullrating/simulationcallerapproval remainsWP76.'
],['F1:100,109,113-116'],'NECESSARY_DYNAMIC_AUTHORING_ROUTE; NOT_DEFAULT_RUNTIME_DATA_CHANGE')
u('S14',1,134,'Complete TrainerType registry data definition/resource resolvers',[
 'Schema providesid/name/gender/baseMoney/skill/flags/BGMs; missingname=Unnamed,gender2,baseMoney30,skill=baseMoney,flags[]. Type lookupsarestrict atTrainerconstructor.',
 'Resourcecheck returnsnil invalidtype or unresolvedbitmap; charsetbrief strips pathprefixonly aftersuccessfulresolve. Filename requests donotproveassetsavailable.',
 'Factorydefaulttrainers use38actualtypePBSrecords readwithfullfields; noflags/BGMs intheserecords,skilldefaults tobaseMoney except explicitGambler32/Lady72/Swimmer32/Tuber16.'
],['F1:57,108-114','F3:111'])
u('D1',180,373,'Complete required species/maxlevel/item restriction definitions',[
 'Blacklists compare speciesidentity; different-species rejects repeatnonempty species; maxlevel accepts<=L. ItemClause ignoresempty/noitem and rejects repeatedheldidentity.',
 'FactoryUNOWN/50or100/differentitemspecies consumeactualconstructedmembers. Other intervening restrictiondefinitions were read onlyincidentally; noallrestrictionsscope credit.'
],['F1:53,92,108','F4:60-65'])
u('D2',4,95,'Complete base and FixedLevelAdjustment',[
 'Adjustment retainsbothsidesEXP beforetargetcalculations andwrite; fixedstrategy clampsL1..max andtargets bothteams.',
 'Normal unadjust restoresbycurrentindex onlywhenoldEXPpresentanddifferent, thenrecalculates. NoidentitymatchingorHP/PP/item snapshotrollback.'
],['F1:89,93,108','F3:118','F4:72-103'])
u('D3',951,1063,'Complete list and trainer compilers',[
 'MissinglistfilewritesBOMdefaulttowerfilenames. OnlyDefaultTrainerList/TrainerListrecognized; requiredtrainer/pokemonfilenames checked,defaultChallengesignored; actualfilenamefields retained.',
 'Presenttrainerfilescompile ordered sections/recognizedType/Name/Begin/Win/Lose/PokemonNos; missingfilesbecome[]. PokemoncommentedlinesparsewithPBPokemon; challengesdefault[]thenremoveempty/nil.',
 'Messagehashesare reset/added atnamedstages; sectionsfinallysave totrainer_lists. Noatomicallfilesrollback oractualcompiledfile/nativeavailabilityclaimed.'
],['F1:100,108-114','F3:97-101'])
u('D4',511,619,'Complete list/trainer/Pokemon exporters',[
 'Loadfailure/nilreturns; listfileopenedwb andeachrecordwritesdefault/listheader,names,nondefaultChallenges thenexportsbothexternalfiles; exceptioncanleavepartialoutput.',
 'Trainerexport skipsnilrecords, writesordinalheaders andrecognizednonnilfields. Pokemonexport emits canonicalregisteredidentities, recognizeditemornone, fixedstatabbreviations andfourslots. Thisisnotrawbyteidentityroundtrip.'
],['F1:100,109,113','F3:99'])
u('D5',191,1226,'Required complete constructor/level/nature/item/heal/stat units (disjoint ranges in ledger)',[
 'ConstructorstrictSpecieslookup normalizesbasespecies/form, writeslevel/EXP beforelaterfields, initializesnonEggstatus/emptyhelditem/moves/owner/PID/statfields andmayinvokecreationformhook; withMoves=false suppressesdefaultmovefill.',
 'Ownernil=>default0/empty/2/2; thisremains throughFactoryparty/swap. Itemsetterrecognizesnewidentity ornil; invalidnonnull leavesoldvalue. Naturevalidwrite canrecalculatebeforefinaltemplateIV/EVwrites.',
 'Levelsetterrejectsoutside1..max andusesgrowthminimumEXP; EXPsetterinvalidateslevelcache. HealnonEgg restoresHP/status/PP andclearsreadyToEvolve.',
 'Finalstatcalc readsactualforms/baseStats/IV/EV/nature, doesnotvalidatealltemplateeligibility. Constructor/formhooks/nativeRNGandfullyqualifiedallrecords remainseparatescope, notassumedbyliteralcontent.'
],['F1:49,53,79,83,93,108','F3:101'])
u('D6',76,81,'Complete global_metadata save registration',[
 'Globalmetadata savevalue returnswhole $PokemonGlobal andloadassignswholevalue withclassvalidation/new-gameconstructor. Factorynestedchallengeispartofthisgraph, notaseparatefactoryserializer.',
 'Noactualserialization/diskreadback/nativealiaspreservationproved bythisregistration.'
],['F1:89,93,108','F3:15'])
u('D7',30,89,'Global metadata challenge declaration and initialization fragment',[
 'challenge andlastbattlearewritableglobalfields initializednil; lazychallengegetterfillswhenneeded. Declaration/initializationareactualsourcejoins, notproofallmetadatahasbeenreviewedhere.'
],['F1:89,93','F3:15'])
u('D8',111,125,'Complete Game.save',[
 'Validatefirst,thenwritesafesave/saveCount/magic/timeprefix; protectedsaveandframeResetcatchIOError/SystemCallError, decrementcount andreturnfalse, otherexceptionspropagate.',
 'Factorysessioncallerignoresfalseforrollback. Thisisrequest/returnbehavioronly; livegraphnativewriteandloadremainhostlimits.'
],['F1:89,93,108-116','F3:59-65,131'])
u('D9',240,375,'Complete UIHelper confirm/commands units',[
 'Yes/No confirmationdefaultsYes andonlyreturns trueonUSEatindex0 aftertextready;BACKorNo false. Normalcleanupdisposescommands andrestoresmessagevisibility.',
 'MenucommandBACK returns-1,USEcurrentindex;commandwindowdisposehasensurebutvisibilitytail canbeskippedbyexception. Othernumber/displayhelpersinrangearenotFactoryconsumers.'
],['F1:65-81'])
u('D10',117,1352,'Complete necessary Summary opening/options/scene/move reorder/wrapper units',[
 'Summarywrapperdefaultinbattle=false; openingretainssameparty/memberreference andbeginsINFO. Factorycallusesdefaultfalsewithrentaloroldopponentobjects.',
 'NonbattleoptionsofferGive/Take/Dex/Mark understatedgates;TakeactualhelditemcanenterBagandclearsharedtemporarymember. Move-page reorderimmediatelyswapssameMoveobjects; noFactory-specificread-onlyguard.',
 'OnnormalBACKscene returnsfinalindex,wrapperendsSceneandreturnsindex. Factoryresumeswithsameobjectchanges anddoesnorequalification atUIconfirmation; originalgenerationallegalitydoesnotguaranteeimmutabilityafterSummary.',
 'ThisisalreadycoveredbyWP66-AsharedSummarycontract; WP57localcancel/noncopy/slotreplacementstatements do not promise wholechainreadonly/rollback.'
],['F1:65,75,79,81,92','F6:136,168,174,188-190'])
u('D11',781,854,'Complete actual Give/Take item helpers',[
 'GivehasEgg/Mail/oldheld gatesandorderedBagold/newitemwrites;mailcanceldoesnotgloballyrollback. Takewithoutitem/fullBagrejects; nonmailnormalbranchaddshelditem,showsmessage,clearsitemthenreturnstrue.',
 'FactorySummarycanreachthesehelpers ontemporary sharedmembers;successpremisepreservesBagchangesafterlocalrent/swapcancel. Noordinarypermanentcapture/ownertransferisrequired.'
],['F1:65,75,81','F6:100-102,188-190'])
u('D12',559,591,'Complete outer fade block helper',[
 'Fade-out/nativeupdatesbeforeblock,thenpushfade; ensure pops andnormalfade-back/dispose evenwhenblockraises, conditionalnofadeout. Cleanupisvisualstate, notgameplaytransactionrollback.'
],['F1:69,81,94,114-116'])
u('D13',130,220,'Needed Settings constants',[
 'CurrentMAXIMUM_LEVEL100,DISABLE_IVS_AND_EVSfalse,MAX_PARTY_SIZE6. These arefiniteconfigurationvalues; unspecifiedfutureoverridecombinationsremainL11.'
],['F1:30,53,90,108','F4:11','F5:62'])
u('D14',23,25,'Complete GrowthRate.max_level',[
 'ConfiguredmaximumlevelisreadthroughSettings::MAXIMUM_LEVEL, currently100. TheFactoryopen/tablebranchtestisexactequalitytosuggestedlevel.'
],['F1:30-41','F2:FC-03'])
u('D15',8,145,'Complete common registry access modules',[
 'Stringidentitiesbecomesymbolwithoutcasefolding;exists nilfalse,try_get nilnil,getstrictlyvalidatesandunknownraises. Keyorderissymbolregistrydefinitionorder; firstfallbackmoveisthatfirstkey.',
 'Registryaccessdefinitionsareactualread;notall species/move/itemserializedregistrationorcreationqualification.'
],['F1:49,53,100','F3:99-101'])
u('D16',366,388,'Complete global and Kernel random wrappers',[
 'GlobalranddelegatesKernel; numericargumentforwardsoldRand(a),range/twonumbersuseinclusiveoffsetformula. NativeintegerRNG/sampleimplementationnotexecutedordisassembled.',
 'Factoryspanispositivefornonnegativevalidgroupsincludingemptypoolspan1; trainerzero-lengthusesnumeric0 andkeepsseparatehostreturntypequalification.'
],['F1:49','F2:FC-02..04,FC-13..17','F3:89'])
u('D17',600,770,'Complete required message-hash lookup and wrapper units',[
 'Lookupdelaysmessageload,normalizestranslationkey,returnsoriginaltextforemptykey/nooverride, prefersgamethencorelookup. GlobalwrapperdelegatesMessageTypes object.',
 'Actual300trainerliteraltextsareinputkeys,notclaimslocalizedrenderedstringsareidentical. Hostfont/audio/displayandmessagefileloadremainunobserved.'
],['F1:57,63-79,114','F3:111-112'])

fwd={'schema':'gr8-finite-factory-forward/v1','fixed_R':R,'fixed_B8':B,'units':units,'population_note':'Manually authored semantic groups/facts, not line-count or parser-derived proof. Provider facts below remain a distinct reception population; duplicate agreement adds no independent vote. Disjoint exact ranges are in ledger, broad group ranges are navigation only.','new_source_execution':0,'UPDATE_NOT_STARTED':True}
dump('forward-mapping.json',fwd)

clauses=[]
def c(a,b,label,assertions,src):
 clauses.append({'id':f'FF-C{len(clauses)+1:03}','formal':'F1','range':[a,b],'clause':label,'assertions':assertions,'source_units':src,'judgment':'SUPPORTED_WITH_STATED_SCOPE_AND_PREMISES','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':READER})
c(1,5,'Title, classification and static/sanitized status',['Factorytemporaryteamdomain isimplementation-independent; sourcepathsarekeptinaudit.','Allcurrentclaimsarestatic; noUI/runtimeconfirmation.'],['FF-U023','FF-U024'])
c(9,13,'Purpose and allocations',['Candidatepool/group/IV,rental/swapcommit andoriginalpartyrelation areprimary.','CreationnumericruleWP55,FactorypredicatesWP54,sessionrestoreWP55 remainactualseparateinterfaces.'],['FF-U001','FF-U013','FF-U016','FF-U017','FF-U020'])
c(15,17,'End-to-end visible workflow',['Factoryregister installs extra andimmediatecount3; preexistingrulesretained.','Prepare6 andopponent;rent3confirmaddsactivecounter1 andsubmits.','Laterpreparecapturesoldopponent beforefreshopponent;true swapadds1,normalfalse stillsubmits; explicitexternalprogression/ending controlsloop.'],['FF-U001','FF-U006','FF-U007','FF-U008','FF-U009'])
c(19,22,'Non-goals',['Wholefacility/restoration/qualifier/creationcontractsretaintheirprimary.','Generator/replay/reception/hostbusinessarenotexecutedhere.'],['FF-U020','FF-U027','FF-U028','FF-U029'])
c(28,30,'Group/mode/scaling',['Groupmin(wins//7,7) inordinarynonnegativecounterdomain.','Maxsuggestedlevelchoosesopen;bothendpointsfloor(template*N/881) independently.'],['FF-U015','FF-U045','FF-U046'])
for row,(normal,op) in enumerate(zip([[0,173],[174,272],[273,371],[372,491],[492,610],[611,729],[730,849],[372,881]],[[372,491],[492,610],[611,729],[730,849],[372,881],[372,881],[372,881],[372,881]])):
 c(34+row,34+row,f'Group{row} table',['Ordinary inclusive template endpoints '+str(normal),'Open inclusive template endpoints '+str(op)],['FF-U015'])
c(43,45,'IV table and allthresholds',['IVtable3,6,9,12,15,21,31,31; paircurrent/nextcapped7.','Lower-IVcount6/5/4/3/2/1 forswaplowerbounds0/15/22/29/36/43;highestfulfilledrow.'],['FF-U016'])
c(47,49,'All quantity/retry/failure clauses',['Retainoriginalmin/max;emptyexclusions=>exact6/new6/selfcheck.','Nonempty=>exactoldmax+excludedcount/newoldmax/checknew+excluded.','Inclusivedraw,lower/higherIVbybatchposition,niltrainer,newobjects.','EndpointN orpool0 yieldsniltemplatefailurebeforevalidation/restoration.','Invalidwholeteamretriesfromemptywithoutbound;onlynormalsuccessrestorebounds.'],['FF-U015','FF-U016','FF-U032','FF-U037'])
c(51,53,'Candidate objects and identity',['Newtemporaryindividualusesliteraltemplatefields/level;niltrainerbecomesOwner0/empty/2/2.','NPCparty/swapdoesnotreown. OrdinarytrainerpathhasNPCowner.','Duplicatescanbedrawn;wholepredicatesdetermineacceptance.'],['FF-U012','FF-U013','FF-U014','FF-U016','FF-U033','FF-U034','FF-U038'])
c(55,57,'Opponent preparation',['Sixinitialrentalsareexcludedbeforeopponentgeneration;sample3.','Laterexclusionscurrentrentals+oldopponent;sample3.','NPCname/type/texteventsbelongactualwrapperandWP55;noPokemonNosFactorygeneration.'],['FF-U006','FF-U008','FF-U011','FF-U014'])
c(61,63,'Rental display',['Rental title/name-categorylabels,selectedred/helpbycount.'],['FF-U021','FF-U022'])
c(65,65,'Rental row menu',['Summary/Rent-or-Deselect/Others;Othershasnoaction.'],['FF-U022','FF-U023','FF-U042'])
c(66,66,'Third choice confirmation',['Yesreturnsnewlistofthreeselectedoriginalobjects;Noonlyremovesjustaddedthird.'],['FF-U023'])
c(67,67,'No rental cancellation',['Normalrentalchoose(false)hasnoback/cancelexit;normalreturnhas3objects.','Thisisnotaguaranteeformalformedhost/exceptioninputs.'],['FF-U022','FF-U023'])
c(69,69,'Rental submit',['Returnedrentalsstored,activecounter+1,thenpartycommit.'],['FF-U007','FF-U003','FF-U004'])
c(73,75,'Swap screens and menus',['Currentrentals+CANCEL;rowSummary/Swap/Rechoose;secondoldopponent+rechoose+CANCEL.'],['FF-U021','FF-U022','FF-U024'])
c(77,78,'All cancel and rechoose branches',['Eitherfirst/secondcancelasksQuit;Yesfalse/normalend;Nostayssameloop.','Secondrechoosegoesfirstscreen;rowRechoosenoprogrammedspecialaction.'],['FF-U024'])
c(79,79,'Accept commit ordering',['AcceptYesendsscenebeforereferenceassignment;replacechosenrentalwithchosenoldopponentobjectandreturntrue.','Localassignmentdoesnotcopyfields/reown/changelevel/EXP/moves/helditem. SharedSummaryactionsareseparatecalleecontract.'],['FF-U024','FF-U042'])
c(81,81,'Unconditional wrapper submission',['Trueasksactivecounter+1;falsecancelleavescounterandslotunchangedbySwap.','BothnormalresultscommitR;activeP!=R showsactivepartywrite, inactiveonlyregistration.','NoglobalrollbackofearlierSummarywritespromised.'],['FF-U009','FF-U003','FF-U004','FF-U024','FF-U042','FF-U043'])
c(83,83,'Old opponent reference and defaultowner',['Capturepreviouspartybeforefreshopponent;notdeepclone.','Factoryallcandidatesniltrainer/Ownerdefault;noNPCownershiptransfer.'],['FF-U006','FF-U008','FF-U013','FF-U033','FF-U038'])
c(87,89,'Original party invariant',['Originalpartyreferencewrittenonlyatstart,restoredcancel/end;FactoryUI/generationdoesnotassigntheoldPartyfield.','Registration/rentals/playerpartyshareafteractivecommit;noallfields-copystrategy.'],['FF-U003','FF-U004','FF-U005','FF-U007','FF-U009'])
c(90,90,'Capacity/predicate temporary counts',['Temporary6/oldmax+exclusions affectgeneration/check;normalreturnrestores.','Formalcapacity/entrycountcontractremainsWP25/WP54,notatemplatecountoverride.'],['FF-U016','FF-U032'])
c(91,91,'Count',['OnlyrentconfirmationandacceptedSwap calladdswap,whichwritesonlyactive.','Cancel/rechoosedonotaddswap.'],['FF-U004','FF-U007','FF-U009','FF-U023','FF-U024'])
c(92,92,'Legality',['GenerationusescompletecheckswithFactorymember/teamconstraints.','Unsatisfiable/repeatedrejectloopsneednotterminate;malformedpoolconstructioncanraise.','Summarymutationdoesnotrewriteclaimthatgenerationvalidatedtheoriginalcandidatebatch.'],['FF-U016','FF-U031','FF-U032','FF-U037','FF-U042'])
c(93,93,'References and crosssession',['Swapkeepsindividualreference/defaultOwner;permanentacquisitionisnotthisoperation.','Sessionretainscurrentlistorrestoresoriginalonappropriatecancel/end;saveiswholegraphrequest,notnativeproof.'],['FF-U005','FF-U009','FF-U024','FF-U033','FF-U039','FF-U041'])
c(94,94,'Partial rule-set side effects',['Temporaryboundsrestoreonlysuccess;constructionexceptionsornonterminatingretrycanleavetemporarycounts.','Noensuretransactionaddedbyvisualfadehelper.'],['FF-U016','FF-U044'])
c(98,100,'Configuration anddata',['Templatepool/source881divisor/bothtables/IV8/threshold6/countargumentsareactualconstants.','Actualdefault882literalrecordsand300trainerfieldsarereviewedseparatelyfromallconstructor/terminationqualification.'],['FF-U012','FF-U015','FF-U016','FF-U037','FF-U038'])
c(102,104,'Examples/catalog binding',['AllFC01..17effectivevectorscheckedasindependentderivedfixtures.'],['FF-U015','FF-U016','FF-U023','FF-U024'])
c(106,109,'Dependencies',['Creation/sessionWP55,eligibilityWP54,partyWP25/ownerWP18/growthWP30/itemsWP50 remainprimaryseparations.','GeneratorWP76/defaultvsdynamicroute/receptionWP77aretiedtoactualcalls,notassumedexecuted.'],['FF-U001','FF-U013','FF-U017','FF-U020','FF-U028','FF-U029','FF-U036','FF-U037','FF-U042'])
c(111,116,'All unverified/excluded declarations',['PBScontentgeneration/replay/fullfacility/reception/host/pluginsretainnamedownersandlimits.','NoUI/generator/simulation/game/saveconversionexecuted;WP57doesnotclaimWP54/WP55/globalcompletion.'],['FF-U020','FF-U027','FF-U028','FF-U029','FF-U036','FF-U039','FF-U041'])

# Explicit final semantic joins, checked against the final group census. IDs are
# navigation only; the meanings above are the substantive review contribution.
clause_joins=[
 [19,26,27], [1,13,16,18], [1,6,7,8,9], [19,26,27,28,29],
 [15,51,52], *([[15]]*8), [16], [15,16,32,39,43,54],
 [12,13,14,16,34,35,43], [6,8,11,14,35,55], [20,21],
 [21,22,48], [22], [21,22], [7,3,4,50], [20,21,23], [23],
 [23,48], [9,3,4,23,48,49], [6,8,13,34,43],
 [3,4,5,7,9,44,45,46], [16,32], [4,7,9,22,23],
 [16,31,32,39,43,48], [5,9,23,34,35,43,44,45,46], [16,50],
 [12,15,16,41,42,51,52], [15,16,22,23],
 [1,13,17,18,19,27,30,31,32,34,37,41,42,43,48],
 [19,26,27,28,29,37,42,44,45,46,50,54,55],
]
assert len(clause_joins)==len(clauses)
for row,joins in zip(clauses,clause_joins):row['source_units']=[f'FF-U{i:03}' for i in joins]

catalog=source('F2').decode('utf-8-sig').splitlines();vectors=[]
for line_no,line in enumerate(catalog,1):
 if re.match(r'\| FC-\d+',line):
  parts=[p.strip() for p in line.split('|')[1:-1]]
  vectors.append({'id':parts[0],'formal':'F2','line':line_no,'complete_input_premise':parts[1],'complete_derived_expected':parts[2],'source_units':['FF-U015','FF-U016'] if int(parts[0][-2:]) in [1,2,3,4,5,6,8,13,14,16,17] else ['FF-U006','FF-U007','FF-U008','FF-U009','FF-U022','FF-U023','FF-U034','FF-U043'],'judgment':'SUPPORTED_DERIVED_NOT_EXECUTED','reader':READER})
dump('reverse-mapping.json',{'schema':'gr8-finite-factory-reverse/v1','clauses':clauses,'vectors':vectors,'pure_navigation_disposition':[{'formal':'F1','line':26,'meaning':'Section 2 heading identifies candidate generation; operative clauses follow.'},{'formal':'F1','line':32,'meaning':'Column headings identify group, ordinary template interval and open template interval; all eight rows are mapped separately.'},{'formal':'F1','line':33,'meaning':'Markdown table alignment delimiter; no independent business assertion.'}],'shared_catalog_full_read':{'formal':'F2','range':[1,183],'Factory':[70,90],'other_owner_dispositions':[{'range':[1,6],'purpose':'Shared header, static and history qualifications; root/history owner retains global history reception.'},{'range':[7,31],'purpose':'EG other Creature owner; full text read for consistency, no new EG acceptance.'},{'range':[32,68],'purpose':'EN other Creature owner; full text read for consistency, no new EN acceptance.'},{'range':[92,127],'purpose':'MG root primary; full catalog text read, no Mail/MG sign-off.'},{'range':[129,166],'purpose':'TT accepted finite primary/root receipt; no renamed vote.'},{'range':[168,183],'purpose':'R5U03 Mail vectors root primary; full text read, no whole history acceptance.'}]},'formal_dependencies_read':['F3','F4','F5'],'partial_required_summary_formal':{'formal':'F6','ranges':[[100,220]],'purpose':'Complete relevant §4.4 rows and §5–6 shared Summary contract; no own whole WP66 credit.'},'UPDATE_NOT_STARTED':True})

fullscripts=['S'+str(i) for i in range(1,15)]
partials={
 'D1':[[174,309],[352,384]],'D2':[[1,110]],'D3':[[947,1080]],'D4':[[500,635]],
 'D5':[[180,215],[267,310],[490,580],[1070,1128],[1130,1227]],
 'D6':[[1,110]],'D7':[[1,110]],'D8':[[105,125]],'D9':[[198,376]],
 'D10':[[117,190],[925,1005],[1130,1410]],'D11':[[777,877]],'D12':[[553,591]],
 'D13':[[123,151],[211,224]],'D14':[[1,125]],'D15':[[1,145]],'D16':[[45,80],[356,392]],'D17':[[575,625],[739,780]],'F6':[[100,220]],
}
ledger=[]
for k in fullscripts+['F1','F2','F3','F4','F5','P1','P2']:
 ledger.append({'identity':k,'status':'OWN_FULL_TEXT_READ','ranges':[[1,IDENTS[k]['lines']]],'reader':READER,'semantic_credit':'Factoryprimary/necessaryjoins;nonFactoryunitsaremappedorotherownerpurpose-disposed','whole_source_credit_from_foreign_receipt':False})
for k,rs in partials.items():ledger.append({'identity':k,'status':'OWN_NECESSARY_COMPLETE_DEFINITIONS_READ_WITH_INCIDENTAL_CONTEXT','actual_read_ranges':[[a,min(b,IDENTS[k]['lines'])] for a,b in rs],'whole_file_FULL':False,'reader':READER})
ledger.append({'identity':'D5','status':'QUALIFIED_COMPLETE_UNIT_RECEIVED','range':[625,642],'unit':'pokemon:reset_moves:0','producer_packet':pointer('tasks/facility_atomic_completion_cloud/v2/individual-producer-source.exact.json','#/whole_source_units[id=pokemon:reset_moves:0]'),'necessary':'Constructor withMovesfalse bypassesit;receivedcompletefornormalconstructoralternativewithoutclaimallPokemonFULL'})
ledger.append({'identity':'P3','status':'OWN_ALL_FACTORY_CONSUMED_FIELDS_READ','records':300,'record_indices':[0,299],'header_line_formula':'3+8*i','fields':['Type','Name','BeginSpeech','EndSpeechWin','EndSpeechLose'],'field_values':1500,'unused_field_disposition':'All300PokemonNosarraysarenotreadbyFactorygeneration;ordinaryopponentandWP76originalFACownerretainswhole1600trainerrecordcoverage. NotownwholeP3FULL.','reader':READER})
ledger.append({'identity':'P4','status':'OWN_ALL38_REQUIRED_COMPLETE_RECORDS_READ','selection':'alltypesappearinginP3Typefields','records':38,'defaults_received':'NoFlags/BGMsinthe38;GameDataTrainerType defaultsflags[]/BGMs nil. MissingSkillLevel fallsbacktoBaseMoney;GAMBLER32/LADY72/SWIMMER_M,F32/TUBER_M,F16explicit.','reader':READER})

provider_names=['factory-76-facts-selected-producer.v2.json','factory-creation-session-restoration-selected.v2.json']
providers=[]
for fn in provider_names:
 p='tasks/facility_atomic_completion_cloud/v2/'+fn;d=json.loads((ROOT/p).read_text());field='complete_fact_objects' if '76-' in fn else 'complete_facts_with_lossless_shared_premise'
 providers.append({'identity':pointer(p,'#/'+field+' ALL '+str(len(d[field]))+' completeobjects with allsharedpremises/sourceidentities/limits'),'actual_receiver':READER,'actual_producer':'/root/facility_atomic_completion_cloud','received_ids':[x['id'] for x in d[field]],'facts':len(d[field]),'received':'Alloperativeassertion/locator/receiver/pendingdependencyfieldsread;repeatedtypedstatus/evidence/execution/premisefieldsreadwithcompletefinitecommonvalues. Exactoriginalobjectsremainbound,notrecopied.','no_source_FULL_transfer':True,'qualifications':d.get('important_limits',d.get('unaccepted'))})
dump('reading-ledger.json',{'schema':'gr8-finite-factory-reading/v1','contracts':{'original_prompt':pointer('inputs/eighth-global-review-prompt.md'),'delegated_prompt':pointer('delegation/prompts/creature_e_factory_completion_cloud.md'),'readset':pointer('delegation/readsets/creature_e.json'),'skill':pointer('inputs/review-SKILL.md'),'AGENTS':'/workspace/pokemon-essentials-clean-room/AGENTS.md whole; /workspace/.agents contains no files; project .agents absent; clean-document-revision excludes auditreport exceptfuturehandofffinalprose'},'ledger':ledger,'provider_facts':providers,'raw_PBS_templates':{'own_full':882,'fivefield_records':882,'records_are_not_facts_or_clauses':True,'original_complete_objects':pointer('tasks/pbs_creature_facility/forward-mapping.json','#/tower_records ALL882; rawfixedGitP2preferredforthisreading'),'row_binding':'rawrecordi=GitP2linei+3;allfivefields/orderread1..884withcontiguous1-224,225-444,445-664,665-884'},'excluded_original_readset_domains':[{'paths':['WP64','WP68','Item_Mail','UI_MysteryGift','allunrelatedsharedcatalogs'],'reason':'Root/acceptedTriadotherprimary;currentreadsetoldUNREADorFULLisnotthiscontexttruth;notmycoverageclaim'},{'paths':['PBScup1888Pokemon','nondefaultCuptrainerrecords','unreferencedcup_fancy_pkmn/trainers'],'reason':'FixedP1assignsPoke/Little/Pika/Fancyids,noneprefixFactory. CompleteoriginalFAC/WP76qualifiedobjectsretained;nonepartofdefaultFactoryselection. Debugreroutingalgorithmreviewedbutdoesnotmakearbitraryfuturedatafixedcurrentinput.'}], 'business_execution':{'Ruby':0,'TypeScript':0,'UI':0,'generator':0,'simulation':0,'media':0,'save':0,'runtime':0},'UPDATE_NOT_STARTED':True})

interfaces=[
 {'id':'FF-I01','edge':'listPBS→compile→independentloaders→currentFactorypool/trainer','source_units':['FF-U010','FF-U012','FF-U015','FF-U037','FF-U038'],'meaning':'FixedlistoneDefaulttowerandfourcupblocks;noneFactoryid,sofixedprefixFactorygetsdefault882templates/300trainers. Firstmatchednondefaultemptydoesnotfallthrough;separateloadscanobservealternativecontent. Missingfiles/loadfailureandpartialcompileprefixareexplicit.','state':'COMPLETE_FINITE_STATIC','data':'P1full25;P2full884/882fivefieldrecords;P3all300Factoryfivefields;P4all38neededrecords'},
 {'id':'FF-I02','edge':'set/register/rules/defaults/explicitFactoryRule→extra/session/generator','source_units':['FF-U001','FF-U002','FF-U025','FF-U030','FF-U031','FF-U032','FF-U033','FF-U037'],'meaning':'Existingrulesretained;Factoryregisteronlyforcesimmediatefallback3/Tower. ExplicitFactoryhelperhas50/100max/fixed,UNOWN/species/itemclauses,single3/double4. Suggestedlevelandoldmaxareactualruntimeinputs;cannotinferallfromid.','state':'COMPLETE_FINITE_STATIC'},
 {'id':'FF-I03','edge':'template→Pokemonconstructor/Owner/moves/EV/IV/form→candidate→wholepredicate','source_units':['FF-U012','FF-U013','FF-U016','FF-U033','FF-U035','FF-U037','FF-U038'],'meaning':'Nils/unknowns/orderedfields/RETURNfallback/EVdivisor andconstructorOwnerdefaultresolved;allrawdefaultrecordsread,notallconstructibilitytheorem. Statsandformhooksqualifiedbyactualdependencies;nofulltypedtraitscreationproofinherited.','state':'COMPLETE_FINITE_REQUIRED_INTERFACE; ALL_RECORD_CONSTRUCTABILITY_NOT_CLAIMED','provider_objects':providers},
 {'id':'FF-I04','edge':'rentalandoldopponentUI→confirmation/cancel→count→registration/playerparty','source_units':['FF-U003','FF-U004','FF-U006','FF-U007','FF-U008','FF-U009','FF-U021','FF-U022','FF-U023','FF-U024','FF-U040','FF-U044'],'meaning':'Sameobjectlist/slotreplacement,oldopponentcapture,sample3,allconfirmation/cancelbranches,unconditionalnormalreturnsetPartyandactive-onlycountarejoined. Failuresretaintheiractualprefix;fadeensureisnotbusinessrollback.','state':'COMPLETE_FINITE_STATIC'},
 {'id':'FF-I05','edge':'FactorySummary→sharedSummary/Itemhelpers→samecandidate/current/oldopponent/Bag→return','source_units':['FF-U022','FF-U042','FF-U043'],'meaning':'DefaultnonbattleSummarywithsameobjectsallowsnormalGive/Take/moveorder/mark/Dexoperations. Localcanceldoesnotrewindthese;FactorydoesnotrecheckatUIconfirmation. ExistingWP66-AspecifiesmutabilityandWP57doesnotpromiseglobalreadonly/rollback.','state':'COMPLETE_FINITE_STATIC; NO_REQUIRED_REVISION','strongest_case':'ValidnormalnonmailtemporarymemberXholdingLAXINCENSE,bagcanacceptandaddnormal;SummaryINFO→Take→BACK;Bag+1,X.itemnil. ThenQuitswapfalse leavescounter/swap-slotunchangedandstillsetParty,earlierBagchangeholds. NativeUI/DemoNOT_EXECUTED.'},
 {'id':'FF-I06','edge':'preparedFactoryNPC/currentrentalparty→organizedbattle→normalrestore→oldopponent','source_units':['FF-U006','FF-U008','FF-U009','FF-U017','FF-U018','FF-U035','FF-U037'],'meaning':'NPCpartyassignmentdoesnotreown;organizedwrapperusespartylists,heal/adjust/itemrecords/create/prepare/normalindexedrestoreandprefixfailure. Wrapperdoesnotsetdecisions/progresswins;earlieritemsnapshotiscurrentSummarymodifieditem.','state':'COMPLETE_FINITE_STATIC; BATTLE_ENGINE_END_TO_END_NOT_CLAIMED'},
 {'id':'FF-I07','edge':'sessionparty/originalparty/typecounters→rest/cancel/end→wholeglobalmetadatasaverequest','source_units':['FF-U003','FF-U004','FF-U005','FF-U039','FF-U040','FF-U041'],'meaning':'Snapshotisreference;activecommitwritesplayer;cancel/endrestoreconditional/unconditionalasdefined;stagedcounters/resets/safesavefalse/exceptionprefixreceived. Savecontainerincludeschallenge,notguaranteednativegraphroundtrip.','state':'COMPLETE_FINITE_STATIC; NATIVE_DISK_RELOAD_UNVERIFIED'},
 {'id':'FF-I08','edge':'debugwriter/generator/tier/allocation/export→futureroutedpool','source_units':['FF-U025','FF-U026','FF-U027','FF-U028','FF-U029','FF-U036','FF-U038'],'meaning':'Fullrequiredlocalgeneratordefinitionsread,existinglistassociationwrite/newlistwriter/partialprefixandfuturepoolorderhandedtoWP76. Simulatedcombat/ratinginternalsaretheirprimary,notpreconditiontoapprove881runtimeformula. Noarbitrarycuprecord/allfutureconfigurationqualification.','state':'COMPLETE_FINITE_AUTHORING_INTERFACE; WP76_WHOLE_PRIMARY_OTHER_OWNER'},
 {'id':'FF-I09','edge':'labels/trainerrecord/message/resource/inputrequests→nativehost','source_units':['FF-U011','FF-U021','FF-U022','FF-U034','FF-U047','FF-U048'],'meaning':'Type/name/speechinputvalues/readorder,localizedlookup/fallbackandnormalinputrequestscomplete. Font/pixel/audio/nativeRNG/sample/disk/backendandactualNPCreachabilityboundedbyL01-04/L08/L10-L12/L14.','state':'COMPLETE_AVAILABLE_STATIC; HOST_LIMITS_RETAINED'},
]
interface_joins=[
 [10,12,15,41,42,53,55], [1,2,30,31,32,33,39,51,52],
 [12,13,16,34,35,36,39,43,53], [3,4,6,7,8,9,20,21,22,23,47,50],
 [21,48,49], [6,8,9,17,18,35,36,40,43], [3,4,5,44,45,46],
 [24,25,26,27,28,29,37,41,42], [11,20,21,38,47,54,55],
]
for row,joins in zip(interfaces,interface_joins):row['source_units']=[f'FF-U{i:03}' for i in joins]
dump('interfaces.json',{'schema':'gr8-finite-factory-interfaces/v1','interfaces':interfaces,'no_receiving_of_receiving_layer':True,'remaining_necessary_finite_gameplay_interfaces':[],'other_owner_exclusions':['AcceptedTriad','RootMail/MysteryGift','FullFAC/Combatcallbacks','FullWP76','Allcuprecordconstructibility/termination','Sevenroundglobalhistoryacceptance'],'UPDATE_NOT_STARTED':True})

# A typed structure census is separate from fact/clause populations. It locates
# every definition/declaration in the fourteen files actually read in full and
# gives its manually reviewed containing group; it supplies no reading credit.
structure_rows=[]
for k in fullscripts:
 for line_no,line in enumerate(source(k).decode('utf-8-sig').splitlines(),1):
  if re.match(r'^\s*(?:class |module |def |attr_(?:reader|writer|accessor)\b)',line):
   matched=[x for x in units if x['source']==k and x['range'][0]<=line_no<=x['range'][1]]
   structure_rows.append({'source':k,'line':line_no,'declaration':line.strip(),'semantic_group':[x['id'] for x in matched],'disposition':[x['disposition'] for x in matched]})
dump('evidence/structure-dispositions.json',{'schema':'gr8-finite-factory-structure-dispositions/v1','classification':'TOOL_VALIDATION_NAVIGATION_ONLY','actual_full_reader':READER,'fixed_R':R,'rows':structure_rows,'unassigned':[x for x in structure_rows if not x['semantic_group']],'business_execution':0})

def parse_sections(k):
 rows=[];cur=None
 for n,line in enumerate(source(k).decode('utf-8-sig').splitlines(),1):
  if line.startswith('['):
   if cur:cur['range'][1]=n-1
   cur={'header':line,'range':[n,IDENTS[k]['lines']],'fields':{}};rows.append(cur)
  elif cur and '=' in line:
   field,val=line.split('=',1);cur['fields'][field.strip()]={'line':n,'value':val.strip()}
 return rows
trainer_rows=parse_sections('P3')
needed_types={x['fields']['Type']['value'] for x in trainer_rows}
type_rows=[x for x in parse_sections('P4') if x['header'].strip('[]') in needed_types]
dump('evidence/data-domain-bindings.json',{'schema':'gr8-finite-factory-data-domains/v1','fixed_R':R,'actual_reader':READER,'literal_reading_and_constructability_are_distinct':True,'template_domain':{'identity':'P2','git_blob':IDENTS['P2']['git_blob'],'complete_object_pointer':R+':'+paths['P2'],'records':882,'raw_record_to_line':'i (zero based) -> i+3','all_five_fields_actually_read':True,'individual_records_not_recopied':'Exact immutable Git blob preserves every value and order; this context read all 884 lines.'},'trainer_domain':{'identity':'P3','git_blob':IDENTS['P3']['git_blob'],'complete_object_pointer':R+':'+paths['P3'],'records':300,'consumed_fields':['Type','Name','BeginSpeech','EndSpeechWin','EndSpeechLose'],'field_values_read':1500,'record_header_formula':'3+8*i','PokemonNos_disposition':'Not consumed by Factory generation. The ordinary opponent and authoring paths are separate; their full raw record review remains the original FAC/PBS primary.'},'needed_type_records':{'identity':'P4','records':type_rows,'defaults':'Name fallback Unnamed, gender2, base money30, skill=base money, flags[], BGM fields nil; all required record values below are actual fixed PBS fields.'},'fixed_alternatives':{'identity':'P1','whole_object_pointer':R+':'+paths['P1'],'actual_default':'battle_tower_trainers.txt / battle_tower_pokemon.txt','nondefault_ids':['pokecupsingle','pokecupdouble','littlecupsingle','littlecupdouble','pikacupsingle','pikacupdouble','fancycupsingle','fancycupdouble'],'Factory_matches':[],'current_Factory_cup_rows_needed':0,'conditional_debug_reroute':'Source algorithms are reviewed. This does not adopt arbitrary future routing/content as current fixed data, or guarantee construction/termination for alternate arrays.'},'business_execution':0})

discussion={
 'id':'FF-NR-SUMMARY-INTERFACE','kind':'FINITE_NO_REQUIRED_DISCUSSION_NOT_NEW_CANONICAL_FINDING','proposer':READER,
 'sections':{
 '1_exact_current_clause':'F1lines65,75allowSummary;79describeslocalacceptedreferenceassignment;81statescancelnotcount/notreplaceslotandunconditionalsetParty;92describesgenerationvalidation. F6§5–6lines136,174,188-190alreadydescribessharedreference/nonbattleitemandmoveedit.',
 '2_complete_source_facts':'S5pbSummary147-153constructsdefaultnonbattleSummarywithsameparty;Summaryinitialize1343-1352/start117-182/scene1270-1335/options1193-1229 andMoveSelection929-992joinactualitemhelper781-854. ConditionalTakeaddsnormalnonmailhelditemtoBagthenmessageanditemnil;FactoryUIhasnoadditionalread-onlyguardorfinalrevalidation.',
 '3_falsifiable_case':'ValidnonEgg/nonShadownonmailcandidateXwithLAXINCENSE,normalSummaryresources/messagesandBagcanaccept/addnormal:takeitemfromSummarythenBACKandquitswap. BagLAXINCENSE+1andX.itemnil;falseSwapdoesnotrewindthem,doesnotaddcounterorassignswapslot,butwrapperstillsetParty. AdjacentnopreviousSummarycanceldoesnotmakeBagchange. AllSOURCE_STATIC/NOT_EXECUTED,notclaimeddefaultDemoaccessible.',
 '4_required_vs_optional':'Underlyingmutabilitymustbepreservedinanalysis;missingduplicateWP57listingisnotrequiredrevisionbecauseitscalleecontractalreadycontainsactualmutabilityanditslocalcancelassertionsdonotpromiseall-chainreadonly/rollback. AnextraSummarycross-linkcouldbeeditorialoptionalbutnonewoptionalrootisproposed.',
 '5_strongest_no_required':'ReadingWP57aslocalselection/commitcontractandWP66-AasSummaryprimarymakesbothsourceandformaltrue. RequiringWP57repeatallSummary/Bag/marking/Dexeffectsviolatesprimarycontractdedup. QualifiedgenerationlegalitydoesnotclaimcandidatesremainimmutableafterseparateUIactions.',
 '6_history_and_same_root':'NoexistingFactoryproposalfoundincurrentproposals/rootadjudicationsearch;thisisafiniteinterfacecheck. Seven-roundclosedfindings/statusesremainoriginalhistoricalqualificationonly;noneborrowedasaB8PASS. RootprovidedstrongestNO_REQUIREDinterpretationwhichthiscontextcheckedagainstactualcurrentbytes;notanindependentrequiredissuevote.',
 '7_bounded_chinese_handoff':'保留WP57当前局部租借/换位/计数/提交合同；接合WP66-A摘要同引用且非战斗可写的主规则。后续实现不得从“取消不换槽”推成摘要期间背包/持物/招式操作全回滚；不新增工厂只读或最终复验策略。无必修整改、无自动改稿。',
 '8_remaining_unknown_execution':'NativeUIinput/media/BagexternaloverridesandDemoeventsequenceNOT_EXECUTED/UNVERIFIED. NobusinessrunornewTS,scopewholeCreatureE/globalstillroot. Contextconfigmodel/effort/tier/speed/FastnoauthoritativeechoUNVERIFIED.'}}
dump('proposals.json',{'schema':'gr8-finite-factory-proposals/v1','new_required_proposals':[],'new_optional_proposals':[],'unresolved_candidates':[],'finite_no_required_discussions':[discussion],'root_independent_adjudication':'No newly proposed required issue to accept; coordinator may inspect full finite discussion. This context does not accept its own mandatory finding.','global_history_status':'Root/historyowners retain full seven-round original currentqualification. Existing Factoryendpoint/Owner/cancel clauses rechecked fromcurrentR/B8;nooldPASSsubstitute.','UPDATE_NOT_STARTED':True})

summary={'source_full_scripts':len(fullscripts),'source_full_script_lines':sum(IDENTS[k]['lines'] for k in fullscripts),'source_groups':len(units),'source_manual_fact_assertions':sum(len(u['facts']) for u in units),'formal_full_files':5,'formal_full_lines':sum(IDENTS[k]['lines'] for k in ['F1','F2','F3','F4','F5']),'WP57_lines':116,'WP57_clause_groups':len(clauses),'WP57_manual_assertions':sum(len(c['assertions']) for c in clauses),'catalog_Factory_vectors':len(vectors),'default_template_records':882,'default_trainer_records_required_fields':300,'default_trainer_field_values':1500,'required_trainer_type_records':38,'provider_fact_objects':sum(x['facts'] for x in providers),'necessary_interfaces':len(interfaces),'unread_primary_text':0,'unmapped_WP57_effective_clauses':0,'unreceived_necessary_finite_interfaces':0,'new_required':0,'new_optional':0}
dump('identities.json',{'schema':'gr8-finite-factory-identities/v1','actual_context':READER,'logical_primary':'creature_e finiteFactoryWP57','requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','Fast':'off'},'actual_authoritative_echo':dict.fromkeys(['model','effort','tier','speed','Fast','session_UUID'],'UNVERIFIED'),'parallel_support_attempt':'Spawnfactory_countercheckrejectedagentthreadlimit;nochildcontextstarted/noindependentvotecreated','fixed_B8':{'commit':B,'tree':BT,'formal_subtree':FT},'fixed_R':{'commit':R,'tree':RT},'source_and_formal':list(IDENTS.values()),'provider_payloads':providers,'summary':summary,'write_scope':str(OUT),'publication':'Rootsolepublisher;noindex/add/commit/push/branchswitch','actual_reader_does_not_sign':['Triadacceptedprimary','RootMail/MysteryGift','wholeCreatureE','globalreview','allFACorWP76'],'UPDATE_NOT_STARTED':True})
dump('progress.json',{'schema':'gr8-finite-factory-progress/v1','utc':UTC,'actual_context':READER,'logical_primary':'creature_e finiteFactoryWP57','process':'COMPLETED','status':'READY_FOR_COORDINATOR_CONSOLIDATION','completion_scope':'CompletefiniteFactorysource/formal/vector/necessaryinterfaceprimaryonly.WholeCreatureE/globalfinalrootdecision.','counts':summary,'blockers':[],'scope_limits':['Noall-templateconstructability/typedtraits/proofqualification/terminationclaim','NativeRNG/sample/graphics/input/audio/disk/reload/DemoNOT_EXECUTEDorUNVERIFIED','WholeFAC/WP76/acceptedTriad/rootMail-MGandglobalhistoryremaintheiroriginalowners'],'new_business_execution':0,'UPDATE_NOT_STARTED':True})

review=f'''# R8 finite Factory primary completion

`READY_FOR_COORDINATOR_CONSOLIDATION` — fixed B8 `{B}` / R `{R}`. Actual reader `{READER}`. UPDATE_NOT_STARTED.

Whole WP57 (116 lines), the whole shared catalog (183 lines, including all 17 FC vectors), and the necessary complete WP54/WP55 formal files were actually read. {summary['source_full_scripts']} complete source files ({summary['source_full_script_lines']} lines), required complete dependency definitions, all 882 default template records, all 300 default trainer records’ five Factory-consumed fields, and all 38 referenced trainer-type records were read. Their exact Git bindings and ranges are in identities/reading-ledger. {summary['source_groups']} manually authored source/interface groups contain {summary['source_manual_fact_assertions']} fact assertions; {summary['WP57_clause_groups']} WP57 groups contain {summary['WP57_manual_assertions']} assertions. These populations are separate from 17 vectors, PBS records, 267 qualified producer facts and 9 interfaces.

Factory grouping, both endpoint tables, scaling, IVs and thresholds agree with the current clauses. The fixed pool has 882 raw records; 881 is the scaling divisor. Endpoint N and empty pool failures occur at missing-template creation before validation and bound restoration. Rejection has no retry limit. Successful-generation legality is distinct from every record constructing successfully or every loop terminating.

Renting returns three references, counts through the active-session guard and then submits. Accepted swapping ends its scene before slot assignment; only a true UI return asks for the counter increment. Both normal Boolean returns submit the rental list. The original party and old opponent are retained references; Factory candidates get default Owner id0/empty name/gender2/language2 from the nil-trainer constructor path. Full source joins confirm active versus inactive submissions, indexed battle restoration, save-false behavior and partial failures.

The required mutable Summary handoff was checked. Factory passes the same objects to the default nonbattle Summary. Taking an item, rearranging moves and the other Summary operations follow WP66-A. A later local swap cancellation does not undo preceding Summary writes. WP57 does not claim Summary is read-only or all-chain rollback; WP66-A already supplies the primary mutable contract, so no new required or optional finding is proposed. The complete eight-part discussion is in proposals.json.

FAC’s exact 76-fact and 191-fact selected producer packets were read with their full operative meanings, common premises, object identities and limitations. They remain immutable pointers, do not transfer source FULL, and do not grant all-FAC/typed-trait/constructability or termination approval. The five constructor units required by FIP-F01 were read directly or received as complete units. The incorrect tentative FactoryData 341–429 locator was corrected to the actual 368–429; PBS list is actually 25 lines. Exact original packets are preserved.

The fixed list has one Tower default and four named cup lists. No cup challenge identity is Factory-prefixed, so default Factory routes to Tower. Debug reassociation and new generation/export were followed as conditional authoring paths, including failure prefixes. Other cup literal corpora remain with their qualified FAC/WP76 owner; an arbitrary future debug reroute is not part of fixed current data. No actual current Factory path required a cup record. Every necessary finite interface is mapped in interfaces.json; this does not create an additional receiving-of-receiving review layer.

The accepted Triad contribution, root’s Mail/MysteryGift reading, unrelated shared-catalog domains and the global seven-round historical reception are excluded from this context’s sign-off. NonFactory portions of the whole files were read and purpose-disposed to their actual WP54/55/58/76 owners. Historical PASS and file identity were not substituted for current reading.

All Ruby/TypeScript/UI/generator/simulation/media/save/runtime behavior is NOT_EXECUTED. Graphics, input, audio, native RNG/sample and serialization/disk/reload/Demo reachability remain the original bounded host/material limits; available unread gameplay definitions are not hidden as limits. Model, effort, tier, speed, Fast and session UUID have no authoritative echo and remain UNVERIFIED. The visible canonical context identity is recorded. A parallel countercheck spawn was rejected by the platform thread limit; no extra reviewer or vote exists.

No formal specification or reference source was edited; no Git index/commit/push/branch action was taken. Root alone publishes and decides whole Creature-E/global completion. Manifest and mechanical validation bind the final finite packet without self-hash recursion. UPDATE_NOT_STARTED.
'''
(OUT/'review.md').write_text(review)

validation={'schema':'gr8-finite-factory-mechanical-validation/v1','utc':UTC,'scope':'Identity/path/count/range/reference validation only; no semanticreadingcredit or business execution','checks':[]}
def check(n,ok,detail):validation['checks'].append({'check':n,'ok':bool(ok),'detail':detail})
check('frozenB8tree',git('/workspace/pokemon-essentials-clean-room','rev-parse',B+'^{tree}').decode().strip()==BT,BT)
check('frozenFormalTree',git('/workspace/pokemon-essentials-clean-room','rev-parse',B+':deliverables/final-specification-set').decode().strip()==FT,FT)
check('frozenRtree',git('/workspace/pokemon-essentials','rev-parse',R+'^{tree}').decode().strip()==RT,RT)
check('originalContract',pointer('inputs/eighth-global-review-prompt.md')['sha256']=='63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b','36653-byte fixed prompt')
check('Factoryvectors',set(x['id'] for x in vectors)=={f'FC-{i:02}' for i in range(1,18)},len(vectors))
allunit={x['id'] for x in units};bad=[(x['id'],y) for x in clauses for y in x['source_units'] if y not in allunit]
check('clauseUnitReferences',not bad,bad)
check('groupSourcePaths',all(x['source'] in IDENTS for x in units),len(units))
check('allFullFileStructuresDisposed',all(x['semantic_group'] for x in structure_rows),{'structures':len(structure_rows),'unassigned':[x for x in structure_rows if not x['semantic_group']]})
check('dataDomains',len(trainer_rows)==300 and len(type_rows)==38,{'trainer_records':len(trainer_rows),'complete_needed_type_records':len(type_rows)})
provider_fact_ids=[z for p in providers for z in p['received_ids']]
check('providerFactsDistinct',len(provider_fact_ids)==len(set(provider_fact_ids)),len(provider_fact_ids))
check('actualReadRangesInsideFiles',all(1<=a<=b<=IDENTS[x['identity']]['lines'] for x in ledger for a,b in x.get('actual_read_ranges',x.get('ranges',[]))),len(ledger))
check('factIdsUnique',len({f['id'] for x in units for f in x['facts']})==summary['source_manual_fact_assertions'],summary['source_manual_fact_assertions'])
coverage={i:0 for i in range(1,117)}
for x in clauses:
 for n in range(x['range'][0],x['range'][1]+1):coverage[n]+=1
uncovered=[n for n in coverage if coverage[n]==0 and n not in [26,32,33] and source('F1').decode().splitlines()[n-1].strip() not in ['', '---']]
check('WP57AllNonemptyLinesDisposed',not uncovered,uncovered)
check('allProviderSourceFixed',all(json.loads((ROOT/x['identity']['path']).read_text()).get('fixed_R')==R for x in providers),len(providers))
check('ownFullScriptsExact',sum(IDENTS[k]['lines'] for k in fullscripts)==3294,summary['source_full_script_lines'])
check('noSelfHash',True,'manifest excludes ownfutureidentity; rootlaterbindsmanifest')
validation['all_checks_pass']=all(x['ok'] for x in validation['checks'])
dump('evidence/mechanical-check.json',validation)
manifest_files=[]
for p in sorted(OUT.rglob('*')):
 if p.is_file() and p.name!='delivery-manifest.json':manifest_files.append(pointer(str(p.relative_to(ROOT))))
dump('delivery-manifest.json',{'schema':'gr8-finite-factory-delivery/v1','utc':UTC,'actual_context':READER,'fixed_R':R,'fixed_B8':B,'status':'READY_FOR_COORDINATOR_CONSOLIDATION','files':manifest_files,'summary':summary,'validation':{'path':'evidence/mechanical-check.json','all_checks_pass':validation['all_checks_pass']},'manifest_identity':'Externalrootpublicationbindsthismannifest;noselffuturehash','root_sole_publisher':True,'UPDATE_NOT_STARTED':True})
print(json.dumps({'counts':summary,'validation':validation,'file_count_excluding_manifest':len(manifest_files)},ensure_ascii=False,indent=2))
