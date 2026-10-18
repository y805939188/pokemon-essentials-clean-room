"""Package reviewer-authored finite conclusions; never run reference/game code."""
from pathlib import Path
import collections, datetime, hashlib, json, subprocess

T = Path(__file__).resolve().parent
RR = T.parent.parent
R = Path('/workspace/pokemon-essentials')
UTC = datetime.datetime.now(datetime.timezone.utc).isoformat()
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BC = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
def read(p): return json.loads((T/p).read_text())
def write(p, v): (T/p).write_text(json.dumps(v, ensure_ascii=False, indent=2)+'\n')
def binding(p):
    p=Path(p); b=p.read_bytes()
    try: name=str(p.relative_to(RR))
    except ValueError: name=str(p)
    return {'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

# Preserve the real earlier delivery as a dated snapshot, not a new review layer.
if not (T/'prior-delivery.v1.json').exists():
    write('prior-delivery.v1.json', {'schema':'gr8-creb-prior-delivery-snapshot/v1',
        'captured_utc':UTC,'qualification':'Original04:16 delivery state, superseded only by actual same-context necessary reception. No retrospective PASS.',
        'complete_prior_objects':{n:read(n) for n in ['progress.json','interfaces.json']},
        'complete_prior_report':(T/'review.md').read_text(),
        'prior_reverse_scope_flags':{k:read('reverse-mapping.json')[k] for k in ['complete_semantic_acceptance','reason','all_transitive_interfaces_received']}})

baseline=read('prior-delivery.v1.json')['complete_prior_objects']['progress.json']
all_io=[json.loads(x) for x in (T/'read-io/index.jsonl').read_text().splitlines()]
io=[x for x in all_io if x['began_utc']>='2026-10-16T14:00:00']
groups=collections.defaultdict(list)
for x in io: groups[(x['path'],x['sha256'],x['bytes'],x['file_lines'])].append(x)
new_full_R=[
 'Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',
 'Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb',
 'Data/Scripts/010_Data/002_PBS data/007_BerryPlant.rb',
 'Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb',
 'Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb',
 'Data/Scripts/010_Data/002_PBS data/015_Trainer.rb',
 'Data/Scripts/001_Technical/001_Debugging/004_Validation.rb',
 'PBS/berry_plants.txt','PBS/trainers.txt','PBS/trainer_types.txt','PBS/map_metadata.txt']
old_ledger=read('reading-ledger.json')
prior_full={str(Path(x['identity']['repo'])/x['identity']['path']) for x in old_ledger['initial'] if x['own_full_read']}
prior_full.update(x['path'] for x in old_ledger['extra_full_reads'] if x['own_full_read'])
continuation=[]
for (path,sha,n,lines),rows in groups.items():
    merged=[]
    for a,b in sorted(x['range'] for x in rows):
        if merged and a<=merged[-1][1]+1: merged[-1][1]=max(b,merged[-1][1])
        else: merged.append([a,b])
    unread=[];cursor=1
    for a,b in merged:
        if cursor<a:unread.append([cursor,a-1])
        cursor=b+1
    if cursor<=lines:unread.append([cursor,lines])
    full=not unread
    isR=path.startswith(str(R)+'/')
    rel=str(Path(path).relative_to(R)) if isR else None
    actual_new_full=isR and rel in new_full_R
    if actual_new_full: assert full
    continuation.append({'identity':{'path':path,'bytes':n,'sha256':sha,'lines':lines},
       'displayed_ranges':merged,'undisplayed_ranges_for_this_identity':unread,
       'continuous_displays':[{k:x[k] for k in ['range','stdout','began_utc','ended_utc','exit_code']} for x in rows],
       'display_full_for_exact_bytes':full,
       'source_reading_credit':('NEW_OWN_COMPLETE_FILE_READ_SAME_CONTEXT' if actual_new_full else 'PRIOR_OWN_FULL_REUSED_NO_INCREMENT' if path in prior_full else 'OWN_EXACT_UNITS_ONLY_NO_WHOLE_SOURCE_FULL' if isR else 'COMPLETE_OR_SELECTED_RECEIPT_ARTIFACT_DISPLAY_NOT_UNDERLYING_SOURCE_FULL'),
       'semantic_acceptance':'Explicit manual units/interfaces below only; display unions alone grant no semantic credit.'})
write('continuation-reading-ledger.current.json',{'schema':'gr8-creb-exact-identity-continuation-reading/v1','utc':UTC,
 'actual_context':'/root/creature_b','new_contexts':0,'new_votes':0,
 'original_denominators_unchanged':{'primary':10,'R_primary':6,'F_primary':4,'dependencies':37,'dependency_own_FULL':36,'dependency_byte_association':1,'initial_own_FULL':46},
 'original_extra_full_payloads':46,'original_three_partial_PBS_paths_and_twelve_records_unchanged':True,
 'new_own_complete_R_files':new_full_R,'new_own_complete_R_count':len(new_full_R),
 'read_identity_groups':continuation,
 'truncation_repairs':['Mega companion739 lines: initial giant-line178 display repaired174–180 before full credit.','C backup34119B operative: combined tool output cut329–370, actual320–375 repair read; whole725 lines then accepted.'],
 'failed_range_requests':'Three211/59/102-line root receipts were initially requested1..1000 and asserted before display (exit1); corrected complete ranges read. No credit for failed requests. Actual platform outputs preserved; unavailable UTC not fabricated.',
 'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})

def unit(id, sources, fact, ordinary, controls, joins, credit='OWN_SOURCE_OR_EXPLICIT_NAMED_FINITE_RECEIPT'):
 return {'id':id,'sources':sources,'complete_finite_meaning':fact,'ordinary':ordinary,'negative_cancel_failure':controls,
         'producer_consumer_and_formal_join':joins,'reading_credit':credit,
         'common_premises':'FixedB8/R; legal ordinary objects and exact registered dependencies unless a specific boundary is stated; earlier callbacks/UI return normally up to the stated point; no plugin/redefinition/concurrent mutation. Alternative files require explicit valid selection and compilation. Native/game/save/reload/render execution is not inferred.',
         'execution':'NOT_EXECUTED'}
units=[
 unit('CRN-W01',['Game_Character815–888','Game_Player179–186','own ItemUtilities/Effects'],
 'turn_generic returns immediately under direction_fix; otherwise writes direction,stop_count0 and only changed direction calls turn hook. Right90 mapping is2→4→8→6→2. Player override only changed direction with no forcedroute/interpreter triggers direction event and clears encounter indicator unless keep flag.',
 'Unlocked cardinal direction can turn; Itemfinder retains its actually read item-side loop/order.',
 'Direction locked keeps direction and does not trigger changed-direction notification. No guarantee of event-free wait, host input or loop termination is added.',
 ['IF-WORLD-TRANSITIVE','U09/E02','WP28 field-item definitions']),
 unit('CRN-W02',['Game_Player38–48','MapMetadata138','PBS/map_metadata.txt398','own Bicycle/Escape/FieldMoves'],
 'Both transfer-with-follower and vehicle-with-follower require followers.length==0. Map metadata stores absent boolean/scalar asnil and flags default[]; all69 current records read. Bicycle flags, outdoor and always-bicycle are separate fields consumed by already-read item gates.',
 'Maps29/34/46/49/50/51/74 explicitly Bicycletrue;40/41/45 BicycleAlways true;10/37/38/56/59/61/63/64/65 DisableBoxLink. These are authored values conditional on valid loading.',
 'Follower present blocks named predicate. Missing boolean is not automatically true; raw metadata does not establish a reachable event, current compiled file or actual map transfer.',
 ['IF-WORLD-TRANSITIVE','IF-PARTY-FORM','IF-WORLD-ITEM','WP28/WP27 finite map gates']),
 unit('CRN-W03',['tasks/world_full/world-cre-interface-facts.json WFS080–086/088/089/099','PBS backup interfaces IF05/IF09','PCR current frontier row encounters'],
 'Encounter setup clears steps/chances/tables but retains accumulator; reset clears both. Invalid/disabled/no player/debug/zerochance/no table gates precede radar. Repel chooses configured lead rule; weighted species selection and time/terrain fallback remain ordered. A successful trigger predicate never implies reset. pbEncounter writes type before selection, keeps reached prefix onnil, and clears after normal Battle.start return without interpreting its return value.',
 'Valid loaded table with legal normal rate selects and constructs through the named ordinary chain; data19 current and76 backup sections remain original actual-reader qualified contributions.',
 'Nil/no table/no eligible candidate returns through precise early branch; current negative-chance CD002 remains its root-owned existing required handoff. Explicit backup activation and later reset callers remain separate.',
 ['IF-WORLD-TRANSITIVE','SweetScent/Honey/Fishing source-side return contracts','WP36 existing bounded contract; no new finding'], '/root/world_full and original qualified PBS readers; no own whole WildEncounters claim'),
 unit('CRN-W04',['world WFS085/087','PBS_BATTLE PB10/necessary wild constructor','backup IF09','Pokemon552–583'],
 'Wild constructor draws one rarityrand100 before equal-three-array branch. Equal pools usecommon.sample, all-empty yieldsnil. Otherwise ordinary50/5/1 and CompoundEyes or configuredSuperLuck60/20/5; raw lead ability matters. Setter validates truthy item identity without can_hold. Species all-three-omitted form inheritance differs independent array defaults.',
 'A selected valid ID becomes rawitem_id; nil empties. Current and explicitly selected variant wild-item fields feed exactly these rules.',
 'No generated creature held item is guaranteed from empty pools. Later Shiny/Pokerus/CuteCharm/Synch/form and species callback failures keep earlier prefix; no transaction or effective-battle-ability substitution.',
 ['IF-WORLD-TRANSITIVE','IF-DATA','IF-FACILITY-ITEM','WP27 identity and WP36 generator'], '/root/world_full,/root/pbs_battle,qualified current/backup raw readers + ownPokemon/item data'),
 unit('CRN-E01',['EOR entire781','BattlerChangeSelf64–99','StartEnd322–347/557–567','ActionSwitching142–204','Battle303–305/329–350','own Command/Attack/ActionUseItem full'],
 'Poison damage loops current priority: skip fainted/nonpoison; ordinary poison H/8, Toxic separately increments/caps16 and usesH*Toxic/16; PoisonHeal branch separate. Damage→HP item check→damage ability→formal faint. Faint clears only its own choice directly and resets local status; persistentPokemon HP0 status guard stays distinct. EOR later pbEORSwitch calls judge, uses able counts and sets win1 when only opposing party has no able member. Battle loop then normal end visits retained other choices.',
 'Exact WP28§3.5.1 2v1 no partner, both item users always alive; T missing1HP, POTION2: register0,first heals1 and clears own identity,second fullHP recheck refunds1 but keepsidentity. Unique ordinary poisonedwildHP1 with stated exclusions faints; judgement1 then normal ending refunds retained second choice1→2.',
 'If wild survives/no other result, nextcommand directclear keeps1; if second user faints first, its directclear keeps1. Capacity refusal errors at that refund and retains earlier committed prefix. All callbacks/evolution/reward/media need normal returns before later points. No universal choice reset or idempotence. Any adopted halfHP wild flee claim must separately reject opposingwild with current same-side living>1 and still require CanRun for soleliving; not used by the poison control.',
 ['IF-EOR-COMPOSITION','IF-BATTLE-ACTIVE','WP28§3.5.1 U04-RF01–06','CORE root-qualified necessary source scope']),
 unit('CRN-X01',['BerryPlants entire471','BerryPlant entire45','CompilePBS268–278 (priorwhole1321)','PBS/berry_plants.txt all336/67records','own all item records/Bag/UI/save'],
 'All67 plant records explicitly supply hours,drying,yield. Schema positivehours/nonnegative dry/min and positive max; defaults3/15/[2,5] only for omission and initializer reverses yield if reversed; generic Berry validators empty, no automatic Item/Berry reference assertion. Every supplied plant ID is the corresponding own-read registered current berry record. Mulch selection tests exact Mulch flag, writes mulch beforeremove; planting stats→plant/reset(true)→remove→message. Maturepick confirms, prechecks can_add, stats→add→messages→selfswitchA then true; outer reset only after true.',
 'Default CHERIBERRY3/15/[2,5],ORAN4/15/[2,5],SITRUS8/7/[2,5]; raw all67 other exact tuples actually read, not default copied. GROWTH×.75stage/ceil1.5dry,DAMP×1.25stage/integerhalf dry,GOOEYceil1.5replants,STABLEceil1.5maturestages. Ordered watering-cans Sprayduck/Squirtbottle/Wailmerpail/Sprinklotad first held prompt, no consumption.',
 'Cancel mulch/berry prevents its later write, but earlier appliedmulch remains; reject/fullbagpick noouterreset oradd. Message-time independent newplant updates may still commit. Empty/invalid customplant ID may fail later GameData lookup; no arbitrary flaggedberry guarantee. reset freezes current NEW_BERRY_PLANTS; old objects ordinary sprite path do not update because noinitialtrue. Clock/media not executed.',
 ['IF-EXTERNAL-ITEM-CONSUMERS','WFS057–059 actually received','WP27 add/remove/wholeglobal save and WP28 flag/quantity boundary','WP60 owner remains external']),
 unit('CRN-X02',['received-current/mining-lottery.json complete MG-MN01–10/MG-LT01–03','Mining144–227 complete61candidate/13iron rows','own all current item records/Bag301/save'],
 'Mining data everyrow ID/weight/crop/geometry/mask read:61rows48itemIDs,totalweight2370;7fossils and16plates each exclusive,HEARTSCALE repeat. Ordered local revealed wonIDs are appended only after flash normalreturn. Ordinary collapse/allfound/giveup all call GiveItems; each won ID directly add1 in order, independent false capacity continues, earlier additions remain, wonlist notcleared. Wrapper calls once. Lottery only writes draw/match variables and no local inventory/money/prize writer.',
 'All48 Mining IDs are own-read default registered Items; direct ordered awards join Bag.add/current pocket rules and wholebag save value. Repeated geometric rows do not create different item identities.',
 'No batchcapacity promise; partial award, later name-query failure and repeat direct call prefix remain. No miningtool admission inferred; arbitrary NPC crafting/lottery prize/event rewards remain authored caller scope. Searchfor craft/hiddenitem is navigation-only and not proof of absence of plugins or dynamically authored Ruby.',
 ['IF-EXTERNAL-ITEM-CONSUMERS','WP27 direct partial addition','UI minigame primary qualified root receipt'], '/root/ui_minigames fullsource facts retained; own complete candidate/iron tables only, not wholeMining645'),
 unit('CRN-X03',['Summary184–215/1232–1268/1342–1400','received-current/learning.json complete4records20atoms17sourceunits6rawrecords','own ItemUtilities917/Pokemon1227/Party1560/Utilities624'],
 'Full-slot chooser constructs optional newmove; initialslot0; BACK chooses max slot and returns−1, USE chooses current; UP/DOWN ordered and skips unavailable existing slots. Screen loops HM refusal unlessDEBUG; negativecancel returns without replacement. Bag machine handler passes bymachine and is_TR to Tutor; successful learning writes stats then first_moves onlyforTR, before sceneend and outer consumption. Party machine branch directLearn lacks TRfirstmove/stat writer.',
 'Default TM57 is FieldUseTR/CHARGEBEAM, notTM byname; legal Magnemite level5 with currentTACKLE/firstTACKLE and free slot can learn. Bag appendsCHARGEBEAM tofirst, Party doesnot. Existing selected raw fixtures and PP definitions remain actual original readers.',
 'Cancel/HM refusal prevents downstream learning/consumption; prior independent commits and later callback errors not rolledback. No wholeSummary1400 or universal rendering approval. Relearn empty list and extrafirst setting gates retain exact received facts and original owners.',
 ['IF-EXTERNAL-ITEM-CONSUMERS','IF-EVOLUTION','WP28 teaching entry lifecycle','WP30 qualified field/consumer receipts']),
 unit('CRN-X04',['GameDataTrainer213','TrainerType134','PBS/trainers118 all20','PBS/trainer_types401 all72','own Phone706/PhoneMessage100/phonePBS48/Compiler1117/CompilePBS1321/WritePBS821/Trainer194/Owner73'],
 'Trainer key is[type.to_sym,rawname,version]; missingversion0,items[],loss"...",pokemon[]. Strictget unknown raises, try_get/existence validate type+name and use exactkey. TrainerType name/gender/money/skill/flags defaults and actual72 rows read, skill defaults base_money, separatemediafields. All20 current trainer records/member fields read; heldSITRUSBERRY and FULLRESTORE list use actual item identities. to_trainer clones items, owner/currentRNG/orderedmember setters, Shadowmake then shininessfalse, recalculates.',
 'CAMPER Jeff versions0/1, PICNICKER Susie0/1 and RIVAL1 Blue0/1/2 exist; TEAMROCKET male/femaleGrunt onlyversion1. These inputs join Phone current exact ID/version lookup, not a promise that buggy versions_count/reveal callers normalize them.',
 'No unknown getter invented: WP63 prior four/18legacy facts remain. No real globalcontact/event installation, variant activation, trainer battle or Phone substitution rendering executed. Explicit valid runtimeglobal needed before later migrationPhone.get failure; defaultcoldstart earlieradd_silent remains WP10.',
 ['IF-EXTERNAL-ITEM-CONSUMERS','IF-PHONE','WP63/WP10 already fullread','PCR all20/72 qualified primary scope']),
 unit('CRN-S01',['PCR remaining-necessary301/rootfinal126','PBSbackup interfaces766/necessaryprovider528/rootfinal168','A/C interfaces371/qualifications155/backupCBV725/rootfinal113'],
 'Current2178 and6712backup record contributions remain original actual field readers, not new ownrawFULL. Necessary base/form numeric/growth/learning/breeding/evolution/wilditem/identity/default/order joins accepted under same-generation anchor and explicitactivation rules. Typescompile uniq only; Tutor duplicates retained; reset_moves latest eligible levelMove occurrence thenlast4. Mega matchingstone OR knownmove, arbitrary otherMegaStone no extra exclusion.',
 'Already own-read item-use source/selected complete default fixtures meet finite item-relevant shared GR/DC/SH/PP vectors; qualified CBV05/06/09/11/12 + IF02/08/09 supply exact producer rules and boundaries.',
 'No global numerical/daycare/fusion/allmoves domain or whole foreign formal approved here. Parent102/A6939/C659 populations remain original readers; final-interface navigation doesnot make their source bodies personally FULL. Old acceptedfalse/OPEN snapshots preserved, later rootqualification explicit.',
 ['IF-SHARED-CATALOGS','IF-PARTY-FORM','IF-EVOLUTION','item-relevant GR/DC/R6GR finite meanings only'], 'Named original A/C/current/fourbackup actual readers; exact operative fullreceipts here'),
 unit('CRN-H01',['root readable-resource223','root H-C2 128/H-R6 137/H-R7 99/kernel116/developer116/UI102/World120/Item107/CORE106'],
 'Receive root ownership and exact current historical/opaque qualification, not their whole original bodies. No oldPASS used to prove current item behavior. Readable resource primary signed with native dispatch, physical device, fonts/audio/pixels/Marshal/realprocess qualifications retained. R6 old18 attempts and R7 oneprocess are historical scopes, not current runs; globaldedup and wholeReview remain rootwork.',
 'All own source-static item save callbacks, actual UI requests and normal return prefixes are independently read; qualified producer receipts close concrete data/message/source inputs where claimed.',
 'Actual compiled tables, binary authored eventstock/reward/contact branches, native disk restart/reload/media outcomes remain unobserved; no claim of those outcomes depends on missing real execution. Opaque available native remains unreviewed ratherthan materialmissing. Wholeforeign approval or allhistoryfinal is not an additional local prerequisite.',
 ['IF-HISTORY-BINARY-HOST','IF-SAVE','all originalNOT_EXECUTED vectors'], 'Exact root qualification received, no sourceFULL/historybody transfer'),
 unit('CRN-P01',['PBS_BATTLE20facts/necessary337/interfaces194/remaining61/rootfinal89','COM-MOVE interfaces108/receipt629/remaining36','own PBS reception149+6path identities'],
 'Two-way Item source/data reception complete. Own full independent raw paths five plus Gen8 exactbyteassociation still3154path-records; PBS_BATTLE21paths7704 records retain its own11/association5/namedraw4/namedassociation1. Fling andNaturalGift current-item/prefix/fullnumeric/firstmatch/typefallback/berrypermission/laterconsumption remain received finite actual callers; Gen5 power60/70/80 differs later80/90/100 onlyifselected.',
 'COM-MOVE OUT-PBS receipt9937fabc actually read completely and its consumer states acceptedfinite; PBSB actual Item schema/fullrecord producer references preserve ourreadingcredit.',
 'No secondraw reader from projection/receipt; no unsupported Gen7type difference or automatic backups. Old quotedFITEM1 nonnilwording must bind final-evidence-corrections below; ordinary validID/nil ItemClause/material inputs unaffected.',
 ['IF-FLING-NATURALGIFT','IF-DATA','IF-FACILITY-ITEM','PBS-FIELDS/FLAGS/PATHS'], 'Two-way named producer/consumer; own raw credit unchanged')
]

closures=[
 {'id':'IF-WORLD-TRANSITIVE','current':'ACCEPTED_FINITE_NECESSARY_CHAIN','units':['CRN-W01','CRN-W02','CRN-W03','CRN-W04'],
  'retained':'Full world/native/map event domains not approved by CRE-B. Necessary definitions/table/version/constructor/follower/direction/map metadata now concretely received; no missing local fact.'},
 {'id':'IF-EOR-COMPOSITION','current':'ACCEPTED_FINITE_NECESSARY_CHAIN','units':['CRN-E01'],
  'retained':'Existing poison2v1 vector only, all six controls static NOT_EXECUTED; no allEOR/combat formal approval.'},
 {'id':'IF-SHARED-CATALOGS','current':'NECESSARY_ITEM_FACETS_ACCEPTED_FOREIGN_PRIMARY_APPROVAL_RETAINED','units':['CRN-S01','CRN-X03'],
  'retained':'Whole numerical/state/daycare/A/C/formal/globalhistory approval remains actual external owner/root. Sharedcatalog ownfullread never becomes wholeforeign approval.'},
 {'id':'IF-EXTERNAL-ITEM-CONSUMERS','current':'ACCEPTED_FINITE_NECESSARY_CHAIN','units':['CRN-X01','CRN-X02','CRN-X03','CRN-X04','CRN-W02','CRN-P01'],
  'retained':'Arbitrary authored event/plugin/crafting/reward future combinations and whole UI/minigame/PBS domains not approved; original generic labels are not particular missing local predicates.'},
 {'id':'IF-HISTORY-BINARY-HOST','current':'DISPOSED_RETAINED_GLOBAL_AND_UNEXECUTED_QUALIFICATION_NOT_LOCAL_BLOCKER','units':['CRN-H01'],
  'retained':'Global history, true native/disk/media observations and foreign wholebody reading remain unapproved here. No real game/host outcome claimed or oldPASS credited.'}]
accepted_artifacts=[]
for e in continuation:
    path=e['identity']['path']
    if not path.startswith(str(R)+'/') and e['display_full_for_exact_bytes'] and not path.startswith(str(T)+'/'):
        accepted_artifacts.append({**e['identity'],'read_displays':e['continuous_displays'],
            'scope':'Complete operative text received; only named finite meanings/qualifications in this receipt adopted. No originalsource FULL transfer.'})
for entry in accepted_artifacts:
    if entry['path'].endswith('/root-primary-task-final-registry.v1.json'):
        snapshot=T/'received-current/root-primary-task-final-registry.at-reception.json'
        if snapshot.exists() and hashlib.sha256(snapshot.read_bytes()).hexdigest()==entry['sha256']:
            entry['volatile_original_parent_at_reception']={'path':entry['path'],'bytes':entry['bytes'],'sha256':entry['sha256'],
                'qualification':'Original complete actual display restored byte-exactly; volatile parent later changed. Original snapshot only, no current registry claim.'}
            entry['path']=str(snapshot.relative_to(RR))
write('necessary-reception.current.json',{'schema':'gr8-creb-necessary-final-reception/v1','utc':UTC,'actual_receiver':'/root/creature_b',
 'same_original_context':True,'new_contexts':0,'new_votes':0,'new_required':0,'new_optional':0,
 'original_scope':'6R4formal primary;37dependencies(36ownFULL+1exactbyteassociation) unchanged; original50source+42dependency facts and125vectors retained.',
 'manual_finite_units':units,'former_five_interfaces':closures,'complete_operative_artifact_receptions':accepted_artifacts,
 'mandatory_companion':'final-evidence-corrections.current.json','necessary_available_unread':[],'necessary_consumer_unreceived':[],
 'foreign_whole_approval_granted':False,'whole_review_complete':False,'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})

# Concrete correction: full source units and the original complete wrong objects.
def source_unit(path,a,b,name):
    p=R/path; lines=p.read_text(encoding='utf-8-sig').splitlines(keepends=True)
    return {'id':name,'identity':binding(p),'R_commit':RC,'complete_unit_range':[a,b],
            'complete_text':''.join(lines[a-1:b]),'source_reading':'Own prior full read or exact complete reread in continuation ledger; no execution.'}
corr=read('evidence-corrections.current.json')
corr['schema']='gr8-creb-final-evidence-corrections/v1';corr['finalized_utc']=UTC
corr['complete_source_units']=[
 source_unit('Data/Scripts/014_Pokemon/001_Pokemon.rb',552,554,'Pokemon.item'),
 source_unit('Data/Scripts/014_Pokemon/001_Pokemon.rb',556,558,'Pokemon.item_id'),
 source_unit('Data/Scripts/014_Pokemon/001_Pokemon.rb',563,566,'Pokemon.item='),
 source_unit('Data/Scripts/014_Pokemon/001_Pokemon.rb',573,577,'Pokemon.hasItem?'),
 source_unit('Data/Scripts/014_Pokemon/001_Pokemon.rb',586,589,'Pokemon.mail'),
 source_unit('Data/Scripts/014_Pokemon/001_Pokemon.rb',594,599,'Pokemon.mail='),
 source_unit('Data/Scripts/010_Data/001_GameData.rb',89,95,'Symbols.exists?'),
 source_unit('Data/Scripts/010_Data/001_GameData.rb',99,105,'Symbols.get'),
 source_unit('Data/Scripts/010_Data/001_GameData.rb',109,115,'Symbols.try_get'),
 source_unit('Data/Scripts/010_Data/001_GameData.rb',220,233,'InstanceMethods.=='),
 source_unit('Data/Scripts/001_Technical/001_Debugging/004_Validation.rb',12,30,'Kernel.validate'),
 source_unit('Data/Scripts/016_UI/005_UI_Party.rb',938,956,'Party.pbPokemonGiveMailScreen')]
corr['common_premises']='FixedR/B8; ordinary registered GameData::Item, String/Symbol/nil controls versus explicit literalfalse boundary; original validate/no redefinition/no plugin. All static derived controls NOT_EXECUTED. No assertion false naturally enters ordinary facility/template/AI input.'
corr['finite_false_boundary_controls']=[
 {'input':'registered :POTION / "POTION" / current Item object','effect':'normalizes rawitem to :POTION; typed getter returns Item; ordinary facility/AI/move predicates unchanged'},
 {'input':'unknown valid Symbol/String token with oldvalidheld','effect':'exists?false causes earlyreturn withoutwrite; olditem remains'},
 {'input':'nil','effect':'skips truthyguard and storesnil; getter nil; noarg hasItem?false'},
 {'input':'literal false','effect':'skips truthyguard and storesrawfalse; item_id false; noarg hasItem?true; item getter and any specified hasItem? reach try_get(false) then validate and raise ArgumentError before equality'},
 {'input':'other unsupported truthy primitive','effect':'exists?validate raises beforeassignment; not unknown-ID nil fallback'},
 {'input':'registered ID held plus check_item=false','effect':'getter returns Item, InstanceMethods.==(false) returnsfalse; differs rawfalse getterfailure'}]
corr['affected_current_objects_and_consumers']=[
 {'object':'dependency-semantic-facts.json ITEM-DATA/MAIL/PC-MAIL/DATA-IDENTITY','disposition':'Corrected own original42facts; full rejected oldobjects retained above. PC-MAIL locator remains PC237 dispatcher plus exact Party938–956 unit.'},
 {'object':'facility-item-interface.json FITEM1/FITEM2','disposition':'Corrected explicitfalse/nil/types; PBF-ITEM parser yields valid83IDs ornil(STICK), so ordinary ItemClause semantics not changed; no allfacility review reopened.'},
 {'object':'tasks/com_move/pbs-consumer-reception.current.json#/facility_identity_scope/0:2','disposition':'Frozen oldcomplete objects bound above; must not apply broad nonnilsetter tofalse. Original GameData trueID/nil Fling/NG/ItemClause receipt retained; no peer oldbyte/status mutation.'},
 {'object':'WORLD/CORE/AI/MOVE any copied generic item identity phrase','disposition':'Only when adopting same exact false/nil facet, use these complete source units. This doesnot independently reapprove theirwhole primary. Root can issue own mandatory companion; source/runtime/domain status not backfilled.'},
 {'object':'MAIL frozen005locator copies and PColdassignment-order phrase','disposition':'006 sourceactualFULL125 unchanged; emptyholder mail first write→getter selfclear→nil.item failure beforeitemsetter/mailboxdelete; matchingheld and cancellation guards separate; no newformalrequired.'}]
mandatory_paths=[
 'adjudication/mandatory-creb-mail-source-path-clarification.v1.json',
 'adjudication/mandatory-item-showquantity-schema-meaning-qualification.v1.json',
 'adjudication/mandatory-item-pinch-false-gluttony-meaning-qualification.v1.json',
 'tasks/pbs_creature_current_cloud/mandatory-primary-token-type-clarification.v1.json',
 'tasks/pbs_creature_current_cloud/mandatory-species-mega-branch-clarification.v1.json',
 'tasks/pbs_creature_current_cloud/mandatory-encounter-trigger-counter-clarification.v1.json',
 'tasks/creature_a_atomic_reception/final-evidence-qualifications.v1.json',
 'tasks/creature_c_existing_crea/backup-producer-qualified-final-reception.v1.json']
corr['actual_complete_mandatory_companions']=[binding(RR/x) for x in mandatory_paths]
corr['mandatory_effective_meanings']={
 'ShowQuantity':'storedtrue OR !important, independentConsumable; ordinary explicitfalse stilltrue; important omission/falsefalse, explicittruetrue.',
 'pinch':'Afterindependent berrypermission, hp<=quarter admitted. quarter<hp<=half withcheck_gluttony=false bypasses predicate forbothactiveandinactiveGluttony; true requiresactive. Abovehalf rejected; othergates remain.',
 'typed':'SevenOnPokemon enums compileInteger1, TIMEFLUTE omittedBattleUse0; SHADOW IconPositionInteger19 andIsSpecialTypebooleantrue; audit JSON lexeme is not Ruby scalar dump.',
 'Mega':'matchingrequiredstone OR knownrequiredmove; otherMegaStone notbaremove-path block; actual battle ring/Transform/Shadow/quota gates separate.',
 'Tutor':'OnlyTypescompileuniq; repeatedTutor DOUBLETEAM/TRICKROOM remain; TWISTER levelMoves+oneTutor isnotduplicateTutor; reset_moves independentlylatesteligible levelMoves thenlast4.',
 'Encounter':'Successfultrigger returntrue notreset; grace may incrementsteps beforetrue; explicitresetcallers ownreachedprefix separately.',
 'MAIL':'Actual006; mailassignment precedes item getter; current corrected order required whenever using old PC-MAIL object.',
 'faint':'BattlerlocalNONE clear is distinct from persistentPokemon HP0 statussetterguard; no broad persistentstatusclear.'}
corr['counts']='Evidence wording/locator corrections only; no new proposal/required/optional/context/vote or formal/source update.'
write('final-evidence-corrections.current.json',corr)

a=read('interfaces.json')
for row in a['interfaces']:
    row.setdefault('prior_0416_status',row['status'])
    c=next((c for c in closures if c['id']==row['id']),None)
    if c:
        row.setdefault('prior_0416_received_contract',row['received_contract']); row.setdefault('prior_0416_remaining',row['remaining'])
        row['status']=c['current'];row['received_contract']='Complete necessary same-context finite reception: '+','.join(c['units'])+' in necessary-reception.current.json.'
        row['remaining']=c['retained'];row['necessary_unreceived']=[]
    if row['id']=='IF-WORLD-ITEM':row['remaining']='Necessarytransitive chain now received in IF-WORLD-TRANSITIVE; host/event/global qualifiers retained.'
    if row['id']=='IF-BATTLE-ACTIVE':row['remaining']='Exact EOR poison-vector and controls now independently sourcejoined in CRN-E01; all businessNOT_EXECUTED.'
    if row['id'] in ['IF-DATA','IF-FACILITY-ITEM','IF-FLING-NATURALGIFT','IF-HELD-ITEMS','IF-PHONE']:
        row['mandatory_companion']='final-evidence-corrections.current.json'
a.update(utc=UTC,finite_accepted=20,open_actual_receipt=0,
 prior_snapshot={'utc':'2026-10-16T04:16:50.503629+00:00','denominator':20,'finite_accepted':15,'open_actual_receipt':5,'complete_original_objects':'prior-delivery.v1.json'},
 current_necessary_available_unread=0,current_necessary_consumer_unreceived=0,
 current_reception='necessary-reception.current.json',mandatory_companion='final-evidence-corrections.current.json',
 note='20 finite interface facets disposed for exact task necessity; foreignwhole/history/native qualifications retained, not20whole-domain approvals. No sourceFULL transferred.',
 new_contexts=0,new_votes=0,new_required=0,whole_review_complete=False)
write('interfaces.json',a)
write('remaining.json',{'schema':'gr8-creb-final-remaining/v1','utc':UTC,'primary_unread':0,
 'necessary_available_unread':[],'necessary_producer_unreceived':[],'necessary_consumer_unreceived':[],
 'material_unavailable':[],'former_five_complete_dispositions':closures,
 'retained_not_local_blockers':[
  'Original 37dependency reading36ownFULL+1byteassociation and3partialPBSpaths/12records preserve actual personalextent. Foreign original raw/fullsource reading stays original reader.',
  'Wholeforeign formal/PBS/Combat/UI/World/history approval not granted by CRE-B. Root taskfinals received with their exact qualifications, not inherited allbodies.',
  'Global dedup/whole-review/current formalcompliance stillrootowned; CRE001 existingfiniteP3 handoff unimplemented. No newrequired.',
  'Actual disk save/restart/reload, compiled table availability, arbitrary authored maps/CommonEvents/reward/plugin/contact permutations, media/native/device/input/render outcomes unexecuted/unapproved.',
  'Available opaque native machinecode retains explicit unread scope, not materialmissing or sourceFULL. No claim of its execution made.'
 ],'mandatory_companion':'final-evidence-corrections.current.json','same_context':True,'new_contexts':0,'new_votes':0,
 'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','actual_configuration':'UNVERIFIED'})

for n in ['forward-mapping.json','reverse-mapping.json','vector-mapping.json']:
 a=read(n);a['necessary_current_receipt']='necessary-reception.current.json';a['mandatory_evidence_companion']='final-evidence-corrections.current.json'
 if n=='reverse-mapping.json':
  a.update(complete_semantic_acceptance=True,all_transitive_interfaces_received=True,
   reason='Exact6R4F primary and necessary finite producer/consumer chains complete; original50/42facts/47clausegroups/125vectors retained. This flag covers task necessaryinterfaces only, not allforeign formal/globaldomains or runtimePASS.',
   whole_foreign_or_global_approval=False)
 if n=='vector-mapping.json':a['EOR_current_finite_join']='CRN-E01; WP28§3.5.1 U04-RF01–06 all staticNOT_EXECUTED; no new vector denominator.'
 write(n,a)

old_ledger.update(updated_utc=UTC,status='PRIMARY_AND_NECESSARY_FINITE_INTERFACES_COMPLETE_WITH_RETAINED_GLOBAL_QUALIFICATIONS',
 semantic_acceptance='PRIMARY_FULL_AND20FINITE_INTERFACES_DISPOSED_FOR_NECESSITY_NO_GLOBAL_PASS',
 continuation='continuation-reading-ledger.current.json',
 original_0416_extra_counts={'full_payloads':46,'partial_PBS_paths':3,'complete_selected_records':12},
 new_same_context_complete_R_files=new_full_R,new_same_context_complete_R_count=len(new_full_R),
 necessary_reception='necessary-reception.current.json')
write('reading-ledger.json',old_ledger)
a=read('identities.json');a.update(updated_utc=UTC,current_receipt_identity_ledger='continuation-reading-ledger.current.json',
 mandatory_companion='final-evidence-corrections.current.json');write('identities.json',a)
p=read('progress.json');p.update(updated_utc=UTC,ended_utc=UTC,
 status='REVIEW_COMPLETE_FOR_ORIGINAL_PRIMARY_AND_NECESSARY_FINITE_INTERFACES_WITH_RETAINED_GLOBAL_QUALIFICATIONS',
 unreceived_interfaces=0,finite_accepted_interfaces=20,necessary_available_unread=0,necessary_consumer_unreceived=0,
 phase='CURRENT_NECESSARY_RECEPTION_COMPLETE',semantic_acceptance='FINITE_SOURCE_STATIC_TASK_COMPLETE_NO_GLOBAL_PASS',
 prior_0416_interface_snapshot={'finite_accepted':15,'open_actual_receipt':5},
 same_context_new_complete_R_count=len(new_full_R),new_contexts=0,new_votes=0,
 necessary_receipt='necessary-reception.current.json',remaining='remaining.json',
 mandatory_companion='final-evidence-corrections.current.json',current_exact_manifest='delivery-manifest.current.json')
write('progress.json',p)

report=f'''CRE-B 原6R/4F主责和必要有限接口已完成；当前必要可得未读0、必要producer/consumer未接收0、材料不可得0。原20接口全部按本片必要范围处置，原04:16时点15已接/5开放完整保存在prior-delivery.v1.json；没有据此批准20个外域整体。新增required/optional/context/独立票均0，CRE001仅保留root既有有限P3交接，UPDATE_NOT_STARTED。

B8={BC}，tree751dfde81048c81390f89a65ca1d1a565ba8e1ca，formal tree f292698cdd4a8e725525a9be6dc34b75faaf151e；R={RC}，tree7589c800b61ba13a13040ed0d686979b80a84fd0。原47载荷46本人全文+1Gen8/default同byte路径关联；10primary、37dependency中36本人全文+1关联均保原资格。五独立raw Items全文及Gen8关联合3154路径记录；原50源单元/42依赖事实/47正式组/125逐向量保持，不用新接口计数替代原意义审读。原额外46完整载荷、3个PBS部分路径12完整记录保原时点；续审11个新增完整R文件与精确局部源/真实接收输出分别列continuation-reading-ledger.current.json，不给他人raw/source个人FULL。

necessary-reception.current.json逐项载明五旧接口的真正producer、consumer、缺省/显式启用及普通/取消/失败前提。World实际37单元162事实完整接收，另本人补读转向/方向锁、玩家follower谓词、MapMetadata138及69条默认地图记录。EOR781本人全文及正式毒伤2v1向量的失能/裁判/终局撤选择链已读：第二次失败退款身份保留、唯一野生毒倒后正常终局再退；次轮直接清/使用者先失能/容量失败各自边界明确。所有向量仍NOT_EXECUTED。

其他道具consumer已接树果完整471+定义45+67条原记录、完整67字段意义及覆盖物/水壶/采摘入包前缀；挖矿61候选/13铁表本人全结构读，实际ui_minigames十完整源事实及Lottery三单元有限接收，逐件Bag.add/失败/重复入口前缀保持原reader。Summary完整选槽/取消/HM拒绝方法、学习4记录20子断言17源单元6原记录接收；默认20trainer/72TrainerType原记录及213/134定义本人全文，接电话准确身份/version键。任意作者新增craft/reward/event/plugin和宿主像素不在这些有限结论内。

PBS_CURRENT2178与backup6712的原真实字段读者、同代base/form、激活/编译/重载/对象查询/save共同前提有限接收，不重读或声称个人6712FULL。PBS_BATTLE20事实/接口与COM-MOVE当前629行双向接收完整，NG/Fling当前item/旗/数值/消费分层不扩为全战斗。A/C完整必要12族及强制限定接收，仅item相关GR/DC/SH/PP意义闭合，整体外域正文批准归原owner/root。H-C2/R6/R7、KERNEL/Developer/UI/World/Item/CORE/readable-resource根限定实际读完；无旧PASS作本轮语义证据，全史总final/native/真实存档和二进制事件执行资格继续单列，非本片精确必要缺口。

final-evidence-corrections.current.json是必须同用伴件：MAIL实际006；邮箱先mail赋值、getter自清导致nil.item在持物设置/邮箱删除前失败；ShowQuantity storedtrue OR !important而非Consumable；pinch check_gluttony=false对active/inactive均跳谓词；GameData参数类型与JSON词面分开；item=false可写rawfalse、noarg hasItem?true、typed getter失败，完整旧对象与12完整源单位/普通nil/有效ID对照均保留；Mega正确石OR已知招、不加任意其它石排除；只有Types编译uniq、Tutor重复保留；Encounter成功不等reset。证据纠正不造新正式必改，冻结外域包不回填。源FULL/原定义归属不变。

所有业务/参考Ruby/game/native/状态模型执行0、NOT_EXECUTED，更新UPDATE_NOT_STARTED。只写原tasks/creature_b；没有安装、commit、push、正式/R/其它任务/历史修改或自动整改。实际model/effort/tier/speed/Fast/opaqueID无回显，逐项UNVERIFIED。真实UTC/exit/stdout见read-io/index.jsonl和continuation ledger；失败/截断与实际补读单列，不造追溯时间。current精确交付绑定见delivery-manifest.current.json。打包UTC{UTC}。
'''
(T/'review.md').write_text(report)
print(json.dumps({'utc':UTC,'necessary_unread':0,'necessary_unreceived':0,'interfaces':20,'new_contexts':0,'new_votes':0,'new_required':0,'new_complete_R_files':len(new_full_R),'business':'NOT_EXECUTED'}))
