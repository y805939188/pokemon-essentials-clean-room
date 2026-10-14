# Hand-authored fresh semantic bindings; this is analytical data, not framework code.
CORE='001_Pokemon.rb'
DAY='reference/pokemon-essentials/Data/Scripts/012_Overworld/007_Overworld_DayCare.rb'
ROAM='reference/pokemon-essentials/Data/Scripts/012_Overworld/002_Battle triggering/005_Overworld_RoamingPokemon.rb'
TRIAD='reference/pokemon-essentials/Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb'
add('wp18-creature-identity-species-ownership.md',1,134,'Identity, fields and content layers',
    'Species strict/loose base+form lookup and constructor fields distinguish content record from individual state. Individual metadata defaults, names, body size, owner and saved caches are not derived from current battle copies.',('008_Species.rb:1:455','001_Pokemon.rb:1:1227','005_Pokemon_Owner.rb:1:73'))
add('wp18-creature-identity-species-ownership.md',135,161,'Species and form commits',
    'Species assignment and normal/form-simple/prompted commits have different cache/stat/Dex actions. Dynamic form only submits a differing truthy result; explicit normal and prompted setters still act at the same numeric form.',('001_Pokemon.rb:113:188','001_FormHandlers.rb:1:792'),('005_Player_Pokedex.rb:195:219','009_Species_files.rb:92:139'))
add('wp18-creature-identity-species-ownership.md',162,224,'Creature creation and ordinary trainer overrides',
    'Creation resolves species/level/owner, generates six IVs and32bit ID, resets moves conditionally, then optional creation-form callback and stats. Normal Trainer conversion applies specified defaults/deterministic overwrites in its own ordering.',('001_Pokemon.rb:1159:1227','015_Trainer.rb:71:213','002_Trainer_LoadAndNew.rb:1:124'),('003_Pokemon_ShadowPokemon.rb:114:140'))
add('wp18-creature-identity-species-ownership.md',225,242,'Clone bounded independence',
    'Base clone copies move objects and selected maps/lists, owner record and fused/shadow boundaries differ; shadow extension retains shared savedEV hash and independently cloned move-record list.',('001_Pokemon.rb:1135:1157','003_Pokemon_ShadowPokemon.rb:213:221'))
add('wp18-creature-identity-species-ownership.md',243,300,'Owner, foreign and provenance fields',
    'Owner is an explicit value record; foreignness compares trainer ID andnonzero differentlanguage. Owner assignment accepts a valid Owner record without rechecking its fields and retains prior shiny caches; names empty/long setter and time integers have their individual semantics.',('005_Pokemon_Owner.rb:1:73','001_Pokemon.rb:840:914'))
add('wp18-creature-identity-species-ownership.md',301,341,'Millimeter size math and invariants',
    'All eight size-piece ranges and high/low ID/IV terms were newly read; size returns millimeters from species height independently of current battle weight. Attribute storage expectations remain valid domain definitions.',('002_Utilities_Pokemon.rb:243:276','001_Pokemon.rb:899:914'))
add('wp18-creature-identity-species-ownership.md',342,345,'Failure scope before owner clause',
    'Strict species/level resolution errors are source-supported, while validation is a helper rather than an unconditional guarantee for all argument fields.',('001_Pokemon.rb:1159:1207','004_Validation.rb:1:31'))
add('wp18-creature-identity-species-ownership.md',346,346,'Equal-valued owner constructor arguments',
    'GR6-K-002: value-keyed validation collapses equal values; id0/name0/gender0/language2 accepts an integer name. Single-field name setter rejects0. Field type expectations and existence of validation are retained, only unconditional constructor-error claim is proposed for narrowing.',('005_Pokemon_Owner.rb:19:28','005_Pokemon_Owner.rb:51:55','004_Validation.rb:12:30'),('001_Pokemon.rb:1198:1205',),status='GR6-K-002_PROPOSAL_COUNTER_SUPPORTED')
endunits('wp18-creature-identity-species-ownership.md',347,('001_Pokemon.rb:1:1227','005_Pokemon_Owner.rb:1:73'))
add('wp20-hp-status-moves-helditem.md',1,120,'HP and persistent statuses',
    'HP setter clips to total, zero clears evolution readiness and hyper extension; heal methods distinguish eggs and full cure. Status validation/count defaults differ from battle temporary effects. Recalculation can revive a fainted creature when maxHP increases.',('001_Pokemon.rb:246:312','003_Pokemon_ShadowPokemon.rb:23:26','010_Status.rb:1:76','001_Pokemon.rb:1099:1133'))
add('wp20-hp-status-moves-helditem.md',121,161,'Known moves, first records and PP',
    'Learning existing moves reorders, first moves are separate orderedID records, compatibility/relearn gates use species data. Move ID changes and PPUp writes clip PP; malformed negative PPUp can commit counter before an inverted clamp fails.',('001_Pokemon.rb:606:727','004_Pokemon_Move.rb:1:77','008_Species.rb:207:246'))
add('wp20-hp-status-moves-helditem.md',162,171,'Battle PP synchronization interface',
    'Persistent PP and battle-copy writes are different layers; active same-ID/nonTransform synchronization consumers must be bound by combat owner rather than inferred from persistent Move setters.',('004_Pokemon_Move.rb:15:47','001_Item_Utilities.rb:1:917'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-C')
add('wp20-hp-status-moves-helditem.md',172,191,'Held item and mail consistency',
    'Item assignment normalizes legal identity, mail getter clears mismatched attachment then returnsnil; mail assignment validates class but does not assign held item. This consumer explains WP64 PCGive failure while ordinary giving writes matching held item.',('001_Pokemon.rb:552:603','001_Item_Utilities.rb:1:917'),('006_Item_Mail.rb:1:125',))
add('wp20-hp-status-moves-helditem.md',192,205,'Battle item restoration consumers',
    'Initial item records may change under real effects, and partner merged lists can diverge from changed player lists. Core getters alone do not establish combat restoration ordering; this named join awaits C.',('001_Pokemon.rb:552:603',),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-C')
endunits('wp20-hp-status-moves-helditem.md',206,('001_Pokemon.rb:246:312','001_Pokemon.rb:552:727','004_Pokemon_Move.rb:1:77'))
add('wp24-player-trainers-partners.md',1,135,'Trainer/player identity, resources and flags',
    'Trainer and Player constructor defaults and per-resource setters differ: initial StartMoney bypasses money setter, later zero-price write clamps. Badges/featureflags and metadata fallback are separate from actual UI unlock/caller existence.',('001_Trainer.rb:1:194','004_Player.rb:1:123','017_PlayerMetadata.rb:1:95','001_Utilities.rb:227:280'))
add('wp24-player-trainers-partners.md',136,172,'Combat money and NPC loading',
    'NPC content to creature conversion is independently read in full; missing trainer feedback distinguishes Debug fallback from normal failure. Battle result money has separate combat callers and requires its direct write ordering.',('015_Trainer.rb:1:213','002_Trainer_LoadAndNew.rb:1:124'),status='PARTIAL_SUPPORTED_COMBAT_WRITER_BINDING_PENDING',owner='R6-C')
add('wp24-player-trainers-partners.md',173,199,'Logical battle audio and remembered intro',
    'All149 battleaudio lines define request precedence for wild/trainer/victory/capture and nextbattle overrides; metadata versus data fallback and trainer-intro memory remain separate from asset presence or playback.',('003_Utilities_BattleAudio.rb:1:149','014_TrainerType.rb:1:134','003_Trainer_Sprites.rb:1:68'))
add('wp24-player-trainers-partners.md',200,239,'Partner registration and cross consumers',
    'Player/trainer objects establish identity and party queries, but partner registration event writes, battle participation and field blocking require current O/C consumer binding.',('001_Trainer.rb:1:194','004_Player.rb:1:123'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-O/R6-C')
endunits('wp24-player-trainers-partners.md',240,('001_Trainer.rb:1:194','004_Player.rb:1:123','003_Utilities_BattleAudio.rb:1:149'))
add('wp25-party-and-storage.md',1,120,'Party/storage addressing and domain moves',
    'Party queries distinguish occupied, nonEgg and able; basic storage preserves member identity on copy/move, party deletion compresses, box deletion does not. Regional storage is an isolated per-region container and wallpaper identity/unlock do not imply media.',('001_Trainer.rb:1:194','004_Player.rb:1:123','004_PokemonStorage.rb:1:400','002_Utilities_Pokemon.rb:1:180'))
add('wp25-party-and-storage.md',121,168,'UI guards and stored-member cure',
    'Domain containers do not enforce every last-able/egg/mail/release guard. UI and PC paths are separate and must be joined to actual caller conditions; preserve ready-to-evolve around designated storage healing is a caller contract.',('004_PokemonStorage.rb:1:400','001_Pokemon.rb:274:312'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-UI')
endunits('wp25-party-and-storage.md',169,('004_PokemonStorage.rb:1:400','001_Trainer.rb:1:194'))
add('wp26-acquisition-gifts-and-script-trade.md',1,92,'Acquisition entries and prefix writes',
    'Ordinary/silent/party-only/foreign/egg entrances have distinct capacity and Dex/name/owner orders. Storage tool returns earlier than some outer callbacks; data writes and normalfalse do not promise rollback of prefix effects.',('002_Utilities_Pokemon.rb:1:180','005_Player_Pokedex.rb:195:219','001_Pokemon.rb:840:889'))
add('wp26-acquisition-gifts-and-script-trade.md',93,121,'Trade presentation and final replacement',
    'Core owner fields and trade-evolution predicates are newly read. Actual trade scene prefix Dex and double cleanup presentation must be imported from UI before signing the full normal chain.',('001_Pokemon.rb:996:1003','007_Evolution.rb:1:676','005_Pokemon_Owner.rb:1:73'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-UI')
endunits('wp26-acquisition-gifts-and-script-trade.md',122,('002_Utilities_Pokemon.rb:1:180','001_Pokemon.rb:840:889'))
add('wp27-bag-and-item-storage.md',1,70,'Item default and display inputs',
    'Full item270 content file defines defaultPocket1/price0/use0, quantity semantics and important-item consumption override. Flags drive handler eligibility separately from direct registration and per-row displayed count.',('006_Item.rb:1:270','007_Item_Sprites.rb:1:157','008_PokemonBag.rb:1:301'))
add('wp27-bag-and-item-storage.md',71,112,'Bag/PC helper storage and partial commits',
    'Quantity sums sameID slots, unlimited pockets scan occupied+1 slots for a single call; capacity probe is pure, add/remove may partially commit, atomic wrappers precheck. Replace leaves multiple sameID slots, clear keeps registration and lastpocket; PC fixedcapacity/initial item lookup differs.',('008_PokemonBag.rb:1:301',))
add('wp27-bag-and-item-storage.md',113,135,'PC quantity flow and browser restoration',
    'Basic container count is owned; actual PC transfer/remove/order and bag filter cursor restore are UI consumers and require imported current review evidence.',('008_PokemonBag.rb:170:301',),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-UI')
add('wp27-bag-and-item-storage.md',136,156,'Author item choice and paired conversion',
    'Three bag choices return identity/nil and write NONE only at permitted variable conditions; list filtering preserves given order/duplicates. Pair conversion skips trailing orphan, firstmatch returns original item target or strict species target; clearing can precede target failure.',('001_Item_Utilities.rb:691:917','001_Utilities.rb:489:523'))
add('wp27-bag-and-item-storage.md',157,178,'Registration three gates and migration',
    'Direct registration deduplicates legal identities without requiring field handler; UI registration eligibility and quickcollection are distinct. Registered-item migration fields are correct despite separate lastpocket case error in WP10.',('008_PokemonBag.rb:139:160','005_Game_SaveConversions.rb:207:240','001_Item_Utilities.rb:1:142'),status='PARTIAL_SUPPORTED_UI_BINDING_PENDING',owner='R6-UI')
endunits('wp27-bag-and-item-storage.md',179,('008_PokemonBag.rb:1:301','006_Item.rb:1:270'))
add('wp28-item-use-and-training.md',1,111,'Active item dispatch and ordinary contexts',
    'Ten registries, conditional precedence and copied handlers are read. Field family inner−1/0/1 differs from outerfalse/true; bag session lastresult can be0 after previous consumption. Field tools/HP/learn and itemfinder all have full owned source; UI selection consumes these contracts.',('001_Item_Utilities.rb:1:917','002_Item_Effects.rb:1:381','005_Event_Handlers.rb:148:204'),status='PARTIAL_SUPPORTED_UI_BINDING_PENDING',owner='R6-UI')
add('wp28-item-use-and-training.md',112,140,'Battle registration and refund residue',
    'The full712 battle item handlers are read; eligibility checks and effects are separately registered. Registration debit, qualifyingrefund, residual choice and same-round terminal secondrefund require combat consumer chain; parser/serialized consumption overrides require DX.',('003_Item_BattleEffects.rb:1:712','001_Item_Utilities.rb:1:917','006_Item.rb:1:270'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-C/R6-DX')
add('wp28-item-use-and-training.md',141,226,'Item families, HP and active PP',
    'Full field and battle handler sets provide the healing configuration amounts, floor-ratioSitrus, fullheal confusion only battle, revivehalfmin1, PPUp cap, and PPrestore fieldfainted versus battleable. Only normal successful entry consumption is asserted.',('002_Item_Effects.rb:382:718','003_Item_BattleEffects.rb:66:212','003_Item_BattleEffects.rb:333:531','001_Item_Utilities.rb:1:230','004_Pokemon_Move.rb:1:47'))
add('wp28-item-use-and-training.md',227,275,'Cultivation, candies and teaching entries',
    'All six vitamin/feather/wing/berry families and21mints are fullread. Quantity helper clamps selection separately from per-share application and bool result; successfulpartial uses consume requestedquantity. Capsule/patch candidate2message can differ from eventual abilityresolve; TR firstrecord only tutorial wrapper.',('002_Item_Effects.rb:719:1120','001_Item_Utilities.rb:231:486','001_Item_Utilities.rb:590:766','001_Utilities.rb:429:487','001_Pokemon.rb:428:550'))
add('wp28-item-use-and-training.md',276,320,'Battle utilities and form/fusion effects',
    'Xstat stage amounts, DireHitthreshold/assign2,2,3, GuardSpecMist5 and mushroom five main stats are explicit. Complete form/fusion family guards and setter callback/party removal/toolreplacement ordering are owned; last-able removalfalse is not checked.',('003_Item_BattleEffects.rb:214:327','003_Item_BattleEffects.rb:537:712','002_Item_Effects.rb:1122:1524','004_Player.rb:1:123','001_Pokemon.rb:159:179'))
add('wp28-item-use-and-training.md',321,342,'HOOPA refresh reentry and nested BoxLink',
    'Owned HOOPA/form handler and ordinary icon setter demonstrate dynamic read nested within prompted formcommit before original-formtime hook; underlying fusion removefalse is confirmed. Normal UI reentry/BoxLink persistence needs UI’s actual route, not only modeled setters.',('002_Item_Effects.rb:1216:1349','001_FormHandlers.rb:1:792','001_Pokemon.rb:147:188','003_Pokemon_Sprites.rb:124:140','009_Species_files.rb:123:139','004_Player.rb:1:123'),status='PARTIAL_SUPPORTED_UI_BINDING_PENDING',owner='R6-UI')
endunits('wp28-item-use-and-training.md',343,('001_Item_Utilities.rb:1:917','002_Item_Effects.rb:1:1524','003_Item_BattleEffects.rb:1:712'))
add('wp29-shops-and-exchanges.md',1,109,'Purchase/sale/BP UI control flow',
    'Money setters and bag partial add/remove are owned. UI stock same-reference filters, buyrollback, gift, saleorder and BP halfdisplay require actual PokeMart consumers, so full UI proof is explicitly pending.',('008_PokemonBag.rb:1:301','004_Player.rb:1:123'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-UI')
add('wp29-shops-and-exchanges.md',110,151,'Price defaults and resource clamping',
    'Item constructor price/salehalf/BP defaults differ from editor bounds; Player money/BP setters clip but initial StartMoney does not. Conditional event priceoverride and two shop writer orders still require direct UI evidence.',('006_Item.rb:1:270','004_Player.rb:1:123','017_PlayerMetadata.rb:1:95'),status='PARTIAL_SUPPORTED_UI_BINDING_PENDING',owner='R6-UI')
endunits('wp29-shops-and-exchanges.md',152,('006_Item.rb:1:270','008_PokemonBag.rb:1:301','004_Player.rb:1:123'))
add('wp30-growth-learning-and-friendship.md',1,78,'Growth curves and bounded lookup',
    'All188 growth definitions newly read,600 tableentries statically parsed and independently calculated. Curves use table to100 and formula above; invalidlevel returns errorobject whereas negativeexp diagnostic has another failure. No original curve execution claimed.',('001_GrowthRate.rb:1:188','001_Pokemon.rb:191:243'))
add('wp30-growth-learning-and-friendship.md',79,125,'Combat experience/EV consumers',
    'Persistent level/EV fields and shadow staging are owned; participation/experience sequential floors and battle learn/statistics require current combat implementation binding.',('001_Pokemon.rb:191:243','003_Pokemon_ShadowPokemon.rb:14:21','003_Pokemon_ShadowPokemon.rb:200:211'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-C')
add('wp30-growth-learning-and-friendship.md',126,153,'Level/experience tools and candy wrappers',
    'Helpers clamp requested level/exp, message before write, same-level returns after recalculation, candy quantities combine exp and friendship before one flow. Rare candy maxlevel can consume after cancelled evolution; actual evolution scene remains UI binding.',('001_Item_Utilities.rb:143:380','002_Item_Effects.rb:918:993','001_Pokemon.rb:191:243'),status='PARTIAL_SUPPORTED_EVOLUTION_UI_BINDING_PENDING',owner='R6-UI')
add('wp30-growth-learning-and-friendship.md',154,181,'Learning and relearning collection',
    'Core known/first move records and general learning/forget tools are fullread; tutor wrapper appends firstTR record only here. Relearn empty-list initialdetail failure and modal loops need UI chain, distinct from candidate calculation.',('001_Pokemon.rb:606:727','001_Item_Utilities.rb:590:690','001_Utilities.rb:429:487'),status='PARTIAL_SUPPORTED_UI_COMBAT_BINDING_PENDING',owner='R6-UI/R6-C')
add('wp30-growth-learning-and-friendship.md',182,243,'Friendship and affection tables',
    'Full method×threefriendshipbands table and map/luxurybell/softcap modifiers are owned. Shadow phase>=4 blocks both signs before ordinaryhelper; direct assignment and captureball writes do not inherit that guard. Peruse cultivation and EV caps are entry-limited.',('001_Pokemon.rb:916:973','003_Pokemon_ShadowPokemon.rb:109:112','001_Item_Utilities.rb:231:486','002_Item_Effects.rb:995:1077'))
endunits('wp30-growth-learning-and-friendship.md',244,('001_GrowthRate.rb:1:188','001_Pokemon.rb:916:973','001_Item_Utilities.rb:1:917'))
add('wp33-daycare-and-breeding-session.md',1,213,'Daycare session, counters and consumer interface',
    'Fresh O full564 Daycare input: deposit stats before invalidindex/space, receive generates beforecapacity without eggflag/compatibility,256step eggcheck then sharingRNG thenXP, finallevel-only silentlearning afterlargejump. Generator own1–255 and saveconversion are joined; compiler event parameter rewrites remain DX pending.',(f'{DAY}:1:564','005_Game_SaveConversions.rb:1:420','001_Pokemon.rb:191:243','012_Game_Stats.rb:1:149'),owner='R6-O',status='IMPORTED_SUPPORTED_COMPILER_BINDING_PENDING')
add('wp35-eggs-and-hatching.md',1,66,'Egg field, content default and source entries',
    'Egg query is steps>0 with directfield/no nilfallback; constructor0 differs from species HatchSteps default1 and textpositive/editorlimit. Own gift/Daycare generator assigns hatchsteps. UIsummary/debug creator limits require current UI/DX.',('001_Pokemon.rb:215:219','001_Pokemon.rb:1159:1227','008_Species.rb:1:207','002_Utilities_Pokemon.rb:162:180',f'{DAY}:21:90'),status='PARTIAL_SUPPORTED_UI_DX_BINDING_PENDING',owner='R6-UI/R6-DX')
add('wp35-eggs-and-hatching.md',67,132,'Step scan, hatch submit and presentation',
    'Hatchstep handler/submit actual chain belongs UI: critical nonegg scan is after first decrement, and submit does not itself clearsteps. Owner/form/Dex dependencies are owned, including ownerassignment retaining shinycache and dynamic formstat/Dex commits before standard owned/egg flags.',('001_Pokemon.rb:147:188','001_Pokemon.rb:390:426','001_Pokemon.rb:840:845','005_Player_Pokedex.rb:195:219'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-UI')
endunits('wp35-eggs-and-hatching.md',133,('001_Pokemon.rb:215:219','001_Pokemon.rb:840:845','001_FormHandlers.rb:1:792'))
add('wp36-wild-encounters-and-modifiers.md',1,99,'Encounter content and registered snapshot distinction',
    'Encounter71 and26type178 definitions newly read: exact existence differs from versionfallback and byversion enumeration can duplicatebase; slots and step chances rawdata are separate. Parsing/writer0-loss and current map snapshot copy/reload require DX/O.',('013_Encounter.rb:1:71','013_EncounterType.rb:1:178'),status='PARTIAL_SUPPORTED_O_DX_BINDING_PENDING',owner='R6-O/R6-DX')
add('wp36-wild-encounters-and-modifiers.md',100,198,'World encounter probability, selection and generation',
    'Owned typecategories/settings/playerqueries/ID anditemhelper contracts feed world selector. All type,time,integeraccumulator,preferredfilter,doubleprecedence,generatedhelditem/shiny/virus/gender and notification effects require O’s current exact sourcejoin; not inferred from dataalone.',('013_EncounterType.rb:1:178','001_Settings.rb:1:524','001_Trainer.rb:1:194','001_Pokemon.rb:313:550'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-O')
add('wp36-wild-encounters-and-modifiers.md',199,206,'Balanced party level math',
    'Helper uses all supplied members, populationdeviation and weightedfraction then positive rounding+2; [5,5]→7 and[10,50]→52. Empty/zerototal return1. Formula does not promise world encounter happens.',('002_Utilities_Pokemon.rb:194:241',))
endunits('wp36-wild-encounters-and-modifiers.md',207,('013_Encounter.rb:1:71','013_EncounterType.rb:1:178','002_Utilities_Pokemon.rb:194:241'))
add('wp57-factory-rentals-and-swaps.md',1,110,'Factory numerical generation and same-reference swap',
    'Owned base creation with blanktrainer yields owner[0,empty,unknown2,language2], and resource/party contracts establish boundary. Sourceinclusive scaledtemplate/IVthresholds/tempcount/no retrybound and cancelstillcommit require C; full formalclauses are freshly read.',('001_Pokemon.rb:1159:1227','005_Pokemon_Owner.rb:1:73','001_Trainer.rb:1:194'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-C')
endunits('wp57-factory-rentals-and-swaps.md',111,('001_Pokemon.rb:1159:1227','005_Pokemon_Owner.rb:1:73'))
add('wp64-mail-and-mystery-gift.md',1,55,'Mail object, snapshot and reading inputs',
    'Mail stores rawmessage/sender and immutablefieldtuples from currentparty k+2/k+1/actualrecipient, independent of actualrecipient container. Emptywrite cancellation createsnomail, cap10 lazybox; reading UI consumes savedtuples and requestsbitmap rather than repickingmembers.',('006_Item_Mail.rb:1:125','001_Pokemon.rb:586:603','001_Item_Utilities.rb:767:917'))
add('wp64-mail-and-mystery-gift.md',56,83,'Mail take and cancellation prefixes',
    'Take prechecks bagcapacity before PC intention. Ordinary swapgiving can addolditem before cancelledmail and retainsolditem member; originalmail removal can persist before later cancellation. PCGive attachesMail then getterselfclears mismatch, but actualPC consumer source is pending.',('001_Item_Utilities.rb:767:917','001_Pokemon.rb:586:603','006_Item_Mail.rb:1:125'),status='PARTIAL_SUPPORTED_PC_UI_BINDING_PENDING',owner='R6-UI')
add('wp64-mail-and-mystery-gift.md',84,161,'Gift queues, codec, authoring and delivery',
    'HTTP transport contract is owned and deliberately distinct from unsafe/nonempty decoding failures. Full MysteryGift UI source is delegated: IDduplicates, queue/delivery mutation, sessionalias/authorcancel/CreateExport fileownership need current UI facts, not presumed from oldreports.',('003_HTTP_Utilities.rb:1:83','002_Utilities_Pokemon.rb:78:95','004_Player.rb:1:123'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-UI')
endunits('wp64-mail-and-mystery-gift.md',162,('006_Item_Mail.rb:1:125','001_Item_Utilities.rb:767:917','003_HTTP_Utilities.rb:1:83'))
add('wp68-triple-triad.md',1,34,'Species-card numbers and price',
    'Fresh O full1300 triad: fourdirection basevalues, bucketcutoffs andprice strictnextstep are matched to owned species/statdata, distinct from individual stats. TypefirstNormal usessecond, no usualeffectivenessmultiplier.',(f'{TRIAD}:13:86','008_Species.rb:1:455','008_Stat.rb:1:119'),owner='R6-O',status='IMPORTED_SOURCE_STATIC_SUPPORTED')
add('wp68-triple-triad.md',35,70,'Card storage, copied hand and selection domain',
    'Occupied+1 helper partialadd aligns card999 limit. Fresh O source715–726 prepares an emptycopy by repeatedadd, merging nonfull sameID slots; randomhand samples remaining slots uniformly, not cardcounts. Permanentstock changes only later.',(f'{TRIAD}:700:806',f'{TRIAD}:987:1046','008_PokemonBag.rb:237:301'),owner='R6-O',status='IMPORTED_SOURCE_STATIC_SUPPORTED')
add('wp68-triple-triad.md',71,112,'Ordered flip, preview and input loops',
    'Fresh O loop/flip facts: initial elements bonus only, samewins recurses afterownershipwrite; preview rejects occupiedrecursivepositions so directonly. openhand range is playerhand count and can have extraemptycursor. Nativepixels/keys/1.5srealwait are unexecuted.',(f'{TRIAD}:371:406',f'{TRIAD}:522:541',f'{TRIAD}:647:699'),owner='R6-O',status='IMPORTED_SOURCE_STATIC_SUPPORTED')
add('wp68-triple-triad.md',113,136,'Result transfers and buy/sell resource consumers',
    'Fresh O result807–949 preserves directloss residualcandidateidentity and trueprizeoverride; transfers follow resultmessage. Buy precheck-add-debit; sell clampedcredit thenremove, so fullwallet doesnot protectcard. No crosssteptransaction.',(f'{TRIAD}:807:949',f'{TRIAD}:1048:1245','004_Player.rb:1:123'),owner='R6-O',status='IMPORTED_SOURCE_STATIC_SUPPORTED')
endunits('wp68-triple-triad.md',137,(f'{TRIAD}:1:1300','008_PokemonBag.rb:237:301'),owner='R6-O')

add('wp19-attributes-ability-and-stats.md',1,116,'Derived identity caches, ability and nature',
    'Owned core full1227: typespecieslist can have3; genderlow8, ordinary/supershiny independentcaches, abilityindexfallback versus candidateenumeration, complete25Nature table and computedoverride with no automatic clear by IDassignment. AbilityPatch messagecandidate2 canresolvefallback.',('001_Pokemon.rb:313:550','002_GenderRatio.rb:1:83','009_Nature.rb:1:173','002_Item_Effects.rb:1079:1120'))
add('wp19-attributes-ability-and-stats.md',117,175,'Experience, IV, EV storage versus consumer limits',
    'Levelvalidates1..max while rawexperience canstoreoutofrange. IV capflags affectcalculation only; cultivationperstat252/total510 do notnormalize allstoredEVs. Facilitytemplate255 double allocation must be joined to C source; its numericdata is independentlyreadformal.',('001_Pokemon.rb:191:243','001_Pokemon.rb:1066:1133','001_GrowthRate.rb:1:188','003_Pokemon_ShadowPokemon.rb:200:211','001_Item_Utilities.rb:231:486'),status='PARTIAL_SUPPORTED_FACILITY_BINDING_PENDING',owner='R6-C')
add('wp19-attributes-ability-and-stats.md',176,240,'Six stat equations and HP recalculation',
    'Separate integer divisions are respected; HP1 specialbase and nonscaledNatureHP; eachNature modifies two nonHP stats except5 neutral. Newmax-currentHP difference canrevive0 whenincrease, preventsfaint ifdecrease fromalive, clipsmax; doesnot preserveHPpercentage.',('001_Pokemon.rb:1066:1133','008_Stat.rb:1:119','009_Nature.rb:1:173','001_Pokemon.rb:246:252'))
endunits('wp19-attributes-ability-and-stats.md',241,('001_Pokemon.rb:313:550','001_Pokemon.rb:1066:1133','009_Nature.rb:1:173'))
add('wp21-dynamic-forms-and-display.md',1,130,'Form registry and all registered families',
    'All792 formhandler lines and species455 newlyread. All triggerfamilies, regional17 targets, plate/memory/type maps and timedFurfrou/Hoopa forms are individuallydeclared. Copyregistration preserves resultattime; defaulttarget data requires dataowner joins ratherthan officialseries substitutions.',('001_FormHandlers.rb:1:792','005_Event_Handlers.rb:148:204','001_Pokemon.rb:113:188'),status='PARTIAL_SUPPORTED_PBS_BINDING_PENDING',owner='R6-D')
add('wp21-dynamic-forms-and-display.md',131,164,'Spinda finite shape and pixel request math',
    'All four hardcoded logical pointmasks and PIDnibbles are read; eachmark alters2×2block fromlefttopRGBA, overlappingmasks applyagain. Individualimageentry copies the resource theniteratesframes; nativeanimationpixelcoverage unknown, separated fromenumerablePNGframes.',('001_FormHandlers.rb:1:792','009_Species_files.rb:92:121'))
add('wp21-dynamic-forms-and-display.md',165,197,'Condition input, timed form and commit order',
    'Forcedform returnswithoutcommit. Dynamicformdifferenttruthy only thennormalsetter; explicitsamevalue normal/prompted stillcacheclear/hook/stat/Dex. Promptedsetter invokescallback between storagewrite and formhook; HOOPA refresh canreenternormal0beforeoutertimehook.',('001_Pokemon.rb:113:188','001_FormHandlers.rb:1:792','003_Pokemon_Sprites.rb:124:140'),('005_Player_Pokedex.rb:195:219','009_Species_files.rb:123:139','002_Item_Effects.rb:1216:1229'))
add('wp21-dynamic-forms-and-display.md',198,235,'Handler move identities and partial failures',
    'ROTOMdirectoldslotchange retainsPPclips; samevaluebarecommit candeletealreadyknownsoleformmove. KYUREM removal compressesduringiteration and canskipshifteditem, CALYREX compactsafterloop. Missingtarget existenceguards differ fromstrictlearn failures; no minimumone-move promise.',('001_FormHandlers.rb:1:792','001_Pokemon.rb:606:727','004_Pokemon_Move.rb:15:47','001_Item_Utilities.rb:590:690'))
add('wp21-dynamic-forms-and-display.md',236,278,'Battle triggers and markings/ribbons/display fields',
    'Owned markingarrays/ribbons canretain malformed orduplicateidentities by distinctwriters; unknown removal differs frommissingvalidribbon. Battle start/leave/Transform calls and UI action-key cancellation/empty-mark comparison need direct C/UI binding.',('001_Pokemon.rb:730:788','001_Pokemon.rb:1:98','001_FormHandlers.rb:1:792'),status='PARTIAL_SUPPORTED_UI_COMBAT_BINDING_PENDING',owner='R6-UI/R6-C')
endunits('wp21-dynamic-forms-and-display.md',279,('001_FormHandlers.rb:1:792','001_Pokemon.rb:113:188','001_Pokemon.rb:730:788'))
add('wp22-mega-and-primal-reversion.md',1,36,'Individual special-form predicates',
    'Mega target scans ordered speciesrecords forstone OR knownmove, simplifiedcurrentform andunmega defaults. Stoneflag alone isnot a binding andknownmovePP0 stillcounts. Primal isseparatehandler+orb contract; individualqueries do notimposeallbattle guards.',('002_Pokemon_MegaEvolution.rb:1:83','008_Species.rb:1:455','001_FormHandlers.rb:1:792'))
add('wp22-mega-and-primal-reversion.md',37,98,'Battle registration, execution and restore scopes',
    'Individualform operations are owned; ownerquota/ring/debug/Transform/SkyDrop/registrationcancel/priority/Primalentry/normalterminal restoration require C’s actualbattleconsumer facts. World/Facility explicitrestore are separate consumers.',('002_Pokemon_MegaEvolution.rb:1:83','001_Pokemon.rb:159:188'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-C/R6-O')
endunits('wp22-mega-and-primal-reversion.md',99,('002_Pokemon_MegaEvolution.rb:1:83',))
add('wp22-transformation-data.md',1,68,'Complete default Mega/Primal literal data',
    '48 targettuples/47stoneconditions+DRAGONASCENT,2Primaldata,ring+stoneflags were freshlyreadformal. Matching fullPBS evidence is required fromdataowner; own Species constructor defaults andPrimalhandler provide semanticsbutnot tupleliteralproof.',('008_Species.rb:1:455','006_Item.rb:1:270','002_Pokemon_MegaEvolution.rb:1:83','001_FormHandlers.rb:1:792'),status='FOREIGN_PBS_BINDING_PENDING',owner='R6-D/root')
add('wp22-transformation-data.md',69,77,'Historical METAGROSS HP and independent vector',
    'Given literalMegaHP95 instead ofbase80, L50IV0EV0max140→155andcurrent70→85, reverse140/70; formula independentlyverified. Literaldata proofpendingdoesnotlicense substitutingofficialstats.',('001_Pokemon.rb:1086:1133',),status='PARTIAL_SUPPORTED_PBS_BINDING_PENDING',owner='R6-D/root')
add('wp23-shadow-hyper-and-purification.md',1,59,'Shadow establishment, gauge and move staging',
    'Allshadow221+Other460 newlyread. No idempotentestablish guard; savedExp/EV reset, gaugeM, movesstage suffix andPPpreserving currentorder. Clone savedEVhashshared. PreparationcheckcanrepeatG0message, doesnotuseLugia exclusion; heartgaugesnapshotmoves require C.',('003_Pokemon_ShadowPokemon.rb:1:221','002_ShadowPokemon_Other.rb:1:460','001_Pokemon.rb:1135:1157'),status='PARTIAL_SUPPORTED_SNAPSHOT_CONSUMER_BINDING_PENDING',owner='R6-C')
add('wp23-shadow-hyper-and-purification.md',60,85,'Hyper and growth staging',
    'OriginalHyper enter usesinclusive quarterthreshold andnormalrandom0 returnsfloat; G0stillwritesstoredHyper andrequestsmessage thoughqueryfalse. CoreHP0explicitclear andfullhealnotclear. Shadowphase>=4 friendshipblock, phase<=3savedgrowth; EOR/obedience/experienceconsumersneed C.',('002_ShadowPokemon_Other.rb:1:230','003_Pokemon_ShadowPokemon.rb:14:112','002_RubyUtilities.rb:366:388','001_Pokemon.rb:274:312'),status='PARTIAL_SUPPORTED_COMBAT_BINDING_PENDING',owner='R6-C')
add('wp23-shadow-hyper-and-purification.md',86,111,'Purification submit ordered prefix',
    'Purify guardshadow+exactG0, stat+flags+ribbon+moves+firstrecord thenEV+savedclears and80%exp, thenleveltool beforeexactexp. Samelevelcalcneeds Sexists even0. Chamberupdatecallbackfailure vsrelicemptycallback requiresUIboundfirstwindowconsumer.',('002_ShadowPokemon_Other.rb:1:82','001_Item_Utilities.rb:143:380','003_Pokemon_ShadowPokemon.rb:200:211'),status='PARTIAL_SUPPORTED_CHAMBER_UI_BINDING_PENDING',owner='R6-UI')
add('wp23-shadow-hyper-and-purification.md',112,129,'Relic, scents and TimeFlute gates',
    'RelicouterpurifiableexcludesLugia butselectionableShadowG0doesnot; mixedparty opensLugia. Scent checks h255+G0, friendshipbeforegauge; Hyperordinary gate basedScentflag differs threebattleIDs. TimeFlute permitspositiveG thenpurifyearlyreturns andeffecttrue consumes.',('002_ShadowPokemon_Other.rb:83:282','003_Pokemon_ShadowPokemon.rb:188:198','001_Item_Utilities.rb:1:917','006_Item.rb:1:270'),status='PARTIAL_SUPPORTED_OPTIONAL_PBS_BINDING_PENDING',owner='R6-D/root')
add('wp23-shadow-hyper-and-purification.md',130,185,'Purification chamber full consumer domain',
    'Chamber编成/math/rawShadowresultcomparison/negativepositionleak/withdrawboxfull/receivecapacity andcrosslevelmissingupdate are freshlyreadformal, andare delegatedtoUIfull1308 source. Core objects establish alias/grade/EV/exp dependencies only; bindingexplicitlypending.',('003_Pokemon_ShadowPokemon.rb:1:221','001_Pokemon.rb:191:243','004_PokemonStorage.rb:1:400'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-UI')
endunits('wp23-shadow-hyper-and-purification.md',186,('003_Pokemon_ShadowPokemon.rb:1:221','002_ShadowPokemon_Other.rb:1:460'))
add('wp23-shadow-data-and-vectors.md',1,36,'Full25 stored-nature gauge table',
    'Full25×4 table checkedagainst originalhearthelper. Unknownnaturedefaults100/300/100/100; scentonlymultipliers1,2,3; computedNatureoverride isnot input.',('003_Pokemon_ShadowPokemon.rb:46:98',))
add('wp23-shadow-data-and-vectors.md',37,60,'Independent scalar vectors and cross consumers',
    '80%expfloor andEVheadroom/gaugephases are independentlycheckable fromownfunctions. Chambertriangleflow andcrosslevelWindowfailure needUI; allvectors remainDERIVED/NOTEXECUTED, nohost equivalence.',('002_ShadowPokemon_Other.rb:1:82','003_Pokemon_ShadowPokemon.rb:93:112','003_Pokemon_ShadowPokemon.rb:200:211'),status='PARTIAL_SUPPORTED_UI_BINDING_PENDING',owner='R6-UI')
add('wp23-shadow-data-and-vectors.md',61,241,'131 optional species/18moves/4items/1type',
    'Completeformal literalcatalogread. Optionalbackupcontent isexplicitlynot defaultcompiled/enabled; rawtable/count/absence/mismatch sourceproofrequestedfromdatareviewer. OwnShadowcontent70/effects460 onlyestablish consumers,notinstallation orallliteralfields.',('011_ShadowPokemon.rb:1:70','002_ShadowPokemon_Other.rb:231:460','006_Item.rb:1:270'),status='FOREIGN_PBS_BINDING_PENDING',owner='R6-D/root')
add('wp31-basic-evolution.md',1,127,'All evolution condition families and author joins',
    'Complete676 registeredmethod file newlyread: fivecheckcontexts, samevariable/postactioncondition, TradeSpecies comparesreceiveritselfthenoldmemberEverstone, highhalfPIDmod10branch, forwardevolutiondepth-first/prevolutionlastsource andPBSextractionsharedparameter-mutationalready KL29. CompilerformcopypriorityneedsDX.',('007_Evolution.rb:1:676','008_Species.rb:250:455'),status='PARTIAL_SUPPORTED_COMPILER_BINDING_PENDING',owner='R6-DX')
add('wp31-basic-evolution.md',128,155,'Shared guards and first target',
    'All fivepersistentindividualcheckentries feedcommon egg/shadow/Everstone/BattleBond guard; afterfirsttruthymethod target returns, noalltargetscollection. Levelentrydoesnotimpose universaljustleveledupsourceprecondition.',('001_Pokemon.rb:976:1045','007_Evolution.rb:1:676'))
add('wp31-basic-evolution.md',156,208,'Evolution scene submission and cancellation',
    'Core Species/cache/HP andpostactionhandlers establish changedfieldrules andShedinja conditionalcopy. Actualanimationcancel, successfulstat/message/consume/clone/species/Dex/learn ordering is UI sourceconsumer; stoneuncancellable andmaxcandycancelstilltrue areowneditemcallers.',('001_Pokemon.rb:123:140','001_Pokemon.rb:1025:1059','007_Evolution.rb:1:676','002_Item_Effects.rb:382:404','002_Item_Effects.rb:918:948'),status='PARTIAL_SUPPORTED_UI_BINDING_PENDING',owner='R6-UI')
endunits('wp31-basic-evolution.md',209,('001_Pokemon.rb:976:1059','007_Evolution.rb:1:676'))
add('wp32-contextual-trade-and-post-battle-evolution.md',1,33,'Context predicate sources and read timing',
    'Full evolutionmethod source usescurrentworldmap/time/weather/globalvehicle/nonEggparty andreceivedmember; shortcircuit avoidslatersourceswhenearlygatefails, targetselectiondoesnotrecheckallconditionsafteranimation. Worldclock/weatherbindingsrequireO.',('007_Evolution.rb:1:676','001_Pokemon.rb:976:1045','001_Trainer.rb:1:194'),status='PARTIAL_SUPPORTED_WORLD_BINDING_PENDING',owner='R6-O')
add('wp32-contextual-trade-and-post-battle-evolution.md',34,97,'Battle K/D records, scan and capture replacement',
    'Ownedreadyfield andevolutionmethods give thresholds/guards andHP0clear. Critical/damagerecord domains, reset/notify, captureindexshift andpartnerhelditemalias need current C fullconsumer; formulasalone donotprove broadbattle rules.',('007_Evolution.rb:1:676','001_Pokemon.rb:246:252','001_Pokemon.rb:1005:1045'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-C')
add('wp32-contextual-trade-and-post-battle-evolution.md',98,109,'Trade receive predicate and doublecleanup interface',
    'TradeSpeciesdefaulttwocrossparameterrows cannotmatchreceiveritself; owncallbackstrictoldobjectitemquery failifnilafterfirstbranch. Actualscene1/2cleanup andfinalpartyreplacement requireUI, includingunknownhostdoubledispose beforesecondcheck.',('007_Evolution.rb:1:676','001_Pokemon.rb:996:1003'),status='PARTIAL_SUPPORTED_UI_BINDING_PENDING',owner='R6-UI')
add('wp32-contextual-trade-and-post-battle-evolution.md',110,128,'Event hit, readiness and cancellation',
    'Singleeventchecks thenstartsnormalcancellableevolution andreturnstrueafterregardlesscancel; wholepartyselectsablelist first. EventIDhasnoglobalconsumption, readinesspersistsuntilexplicitclear orsuccessfulsubmit; prepareddata remains separatefromsubmittedspecies.',('001_Pokemon.rb:1015:1059','007_Evolution.rb:1:676','001_Pokemon.rb:246:312'),status='PARTIAL_SUPPORTED_WHOLEPARTY_UI_BINDING_PENDING',owner='R6-O/R6-UI')
endunits('wp32-contextual-trade-and-post-battle-evolution.md',129,('007_Evolution.rb:1:676','001_Pokemon.rb:976:1059'))
add('wp32-context-inputs-and-scenarios.md',1,46,'35 contextual registered identities',
    'Complete676methods establishes35 contextualidentities; tablecounts57/17samplefamilies belongliteralPBSvalidation ratherthancodeexistence. All zerocounts remainabsenceofliterals not absenceoffeature.',('007_Evolution.rb:1:676',),status='PARTIAL_SUPPORTED_PBS_BINDING_PENDING',owner='R6-D/root')
add('wp32-context-inputs-and-scenarios.md',47,123,'57 default records and map/weather data',
    'Everyformalrowread withparameter identity preserved; ownMapMetadata/Weatherdefinitions setfieldcategories butdonotprovespecificPBSmapliteral. FullPBSsourcejoin requested, noevent/mapruntimeinferred.',('018_MapMetadata.rb:1:138','012_Weather.rb:1:165','007_Evolution.rb:1:676'),status='FOREIGN_PBS_BINDING_PENDING',owner='R6-D/root')
endunits('wp32-context-inputs-and-scenarios.md',124,('007_Evolution.rb:1:676','001_Pokemon.rb:976:1059'),'Fixed K/D/record/cancel vectors preserve stated currentcombat/world prerequisites; they are not reference execution and await current consumer bindings.',owner='R6-C/R6-UI')
add('wp34-inheritance-and-offspring.md',1,160,'Complete offspring generator and ordered inheritance',
    'OwnDayCare1–255fullread: normalizedparentroles/speciesfamily/offspringmapping andform→nature→ability→moves→IV→ball→shiny→pokerus→stats. Completepoweritemaccountingwithoneinheritanceperstat,ballmastercherishreplace andMasuda/ShinyCharmrethrows. Core setter/Dexsameformsideeffect isjoined explicitly.',(f'{DAY}:1:255','008_Species.rb:250:328','001_FormHandlers.rb:1:792','001_Pokemon.rb:159:166'),('005_Player_Pokedex.rb:195:219',))
add('wp34-inheritance-and-offspring.md',161,174,'Inheritance invariants before samevalue clause',
    'Finalindividualvalues andfirstrecord/RNGstatus remain entrylimited; generationnotcapacitytransaction. Same numeric form canstill havecommit effects, andlater recalculationdoesnotprovepriorcallback absent.',(f'{DAY}:1:255','001_Pokemon.rb:159:166'))
add('wp34-inheritance-and-offspring.md',175,182,'Maternal base0 sameform is still commit',
    'GR6-K-003: defaultSHELLOSmother0flag inheritance directlysubmits eggform0, no equality guard; settercache/hook/stat/Dexregister runs andDex hasno eggguard. KeptWP21commitcontract andWP62generalregistration correct; proposed narrow this no-operation summary.',(f'{DAY}:21:90','001_Pokemon.rb:159:166','005_Player_Pokedex.rb:195:219'),status='GR6-K-003_PROPOSAL_COUNTER_SUPPORTED')
endunits('wp34-inheritance-and-offspring.md',183,(f'{DAY}:1:255','008_Species.rb:250:328','001_Pokemon.rb:159:166'))
add('wp37-roaming-and-poke-radar.md',1,80,'Roam config, advance and identity consumers',
    'CurrentO61full228 confirms terminal-andcaughtreset; mapskeys emptiness earlyreturn, missingneighbor nilreturn, empty[] canreceive extra1/32candidate beforefinalguard. Oldrawname vsnewdisplayname gatematches. Normalwrapper doublegeneration, notifyoriginalarg andcombatcontinuation requireO/Cconsumerjoin.',(f'{ROAM}:1:228','001_Settings.rb:1:524'),status='IMPORTED_SUPPORTED_COMBAT_INTERFACE_PENDING',owner='R6-O/R6-C')
add('wp37-roaming-and-poke-radar.md',81,133,'FullRadar geometry, random and cancellation',
    'Owned267 entireRadar: terrain/table/bike beforedebugbattery, initpreserveschain/resetcapture50;fourringcandidateuniform geometry, validitybefore25%/shiny. Exactintegerfloor/realceilshiny, continuationintegerchainquarter,100tries speciesstopversusfinalpair-equality, nilreadfails. Eightcancelcallsincludeexternalbikecaller O.',('005_Item_PokeRadar.rb:1:267','013_EncounterType.rb:1:178','002_RubyUtilities.rb:366:388'),status='PARTIAL_SUPPORTED_BICYCLE_CONSUMER_BINDING_PENDING',owner='R6-O')
add('wp37-roaming-and-poke-radar.md',134,158,'Notification sequence, persistence and debug',
    'Eventorderedregistration andcurrentRoam/Radarfullsources arejoined; migrationskeepterminalplaceholdermarkfailure. FullDebugtool branchrequiresDX ratherthanoldreview; real save/hostnotexecuted. Persistedsourcefield doesnotmeanalreadylandedonfile.',('005_Item_PokeRadar.rb:161:255',f'{ROAM}:1:228','005_Game_SaveConversions.rb:1:420','005_Event_Handlers.rb:66:96'),status='IMPORTED_SUPPORTED_DEBUG_BINDING_PENDING',owner='R6-O/R6-DX')
endunits('wp37-roaming-and-poke-radar.md',159,('005_Item_PokeRadar.rb:1:267',f'{ROAM}:64:103'),'Configuration and unknown clauses remain bounded. WP37:169 no candidate is interpreted after the already specified extra-candidate phase; an empty base adjacency can move if the extra gate hits. No required contradiction established.',owner='R6-O')

# Test catalog rows are each mapped to the freshly read source units for their
# named primary document; foreign consumer dependencies remain visible.
catalog_bindings={
 'creature-rpg-wp18-20-24-25-26.md':[
  (1,37,['wp18-creature-identity-species-ownership.md']),(38,87,['wp20-hp-status-moves-helditem.md']),(88,161,['wp24-player-trainers-partners.md']),(162,208,['wp25-party-and-storage.md']),(209,249,['wp26-acquisition-gifts-and-script-trade.md']),(250,283,['wp18-creature-identity-species-ownership.md']),(284,308,['wp18-creature-identity-species-ownership.md','wp24-player-trainers-partners.md','wp26-acquisition-gifts-and-script-trade.md'])],
 'creature-rpg-wp27-28-29-30-33.md':[
  (1,40,['wp27-bag-and-item-storage.md']),(41,121,['wp28-item-use-and-training.md']),
  (122,155,['wp29-shops-and-exchanges.md']),(156,214,['wp30-growth-learning-and-friendship.md']),
  (215,239,['wp33-daycare-and-breeding-session.md']),(240,257,['wp28-item-use-and-training.md']),
  (258,269,['wp30-growth-learning-and-friendship.md']),(270,314,['wp24-player-trainers-partners.md','wp27-bag-and-item-storage.md','wp28-item-use-and-training.md','wp21-dynamic-forms-and-display.md'])],
 'creature-rpg-wp35-36-57-64-68.md':[
  (1,31,['wp35-eggs-and-hatching.md']),(32,69,['wp36-wild-encounters-and-modifiers.md']),
  (70,91,['wp57-factory-rentals-and-swaps.md']),(92,128,['wp64-mail-and-mystery-gift.md']),
  (129,167,['wp68-triple-triad.md']),(168,183,['wp64-mail-and-mystery-gift.md'])],
 'generic-kernel-wp02-03-04.md':[(1,15,['wp02-rule-configuration-and-data-variants.md']),(16,36,['wp03-content-identity-and-schema.md']),(37,82,['wp03-content-identity-and-schema.md']),(83,165,['wp03-content-identity-and-schema.md'])],
 'generic-kernel-wp05-06-07-08-09-10.md':[
  (1,36,['wp05-events-extensions-plugins.md']),(37,69,['wp06-time-random-steps-stats.md']),
  (70,99,['wp07-diagnostics-files-http.md']),(100,109,['wp07-deprecation-appendix.md']),
  (110,154,['wp08-localization.md']),(155,177,['wp09-save-startup-continue.md']),
  (178,207,['wp10-migration-failure-recovery.md','wp09-save-startup-continue.md']),
  (208,230,['wp08-localization.md']),(231,234,['wp09-save-startup-continue.md']),
  (235,238,['wp05-events-extensions-plugins.md']),(239,243,['wp07-diagnostics-files-http.md']),
  (244,248,['wp10-migration-failure-recovery.md']),(249,252,['wp07-diagnostics-files-http.md']),
  (253,260,['wp06-time-random-steps-stats.md']),(261,265,['wp07-diagnostics-files-http.md'])],
 'pokemon-rules-wp19-21-22-23-34.md':[
  (1,83,['wp19-attributes-ability-and-stats.md']),(84,131,['wp21-dynamic-forms-and-display.md']),
  (132,162,['wp22-mega-and-primal-reversion.md']),(163,220,['wp23-shadow-hyper-and-purification.md']),
  (221,261,['wp34-inheritance-and-offspring.md']),(262,293,['wp21-dynamic-forms-and-display.md']),
  (294,305,['wp19-attributes-ability-and-stats.md','wp28-item-use-and-training.md']),
  (306,312,['wp21-dynamic-forms-and-display.md','wp28-item-use-and-training.md'])],
 'pokemon-rules-wp31-32-37-38.md':[
  (1,47,['wp31-basic-evolution.md']),(48,95,['wp32-contextual-trade-and-post-battle-evolution.md']),
  (96,137,['wp37-roaming-and-poke-radar.md']),(138,165,['wp28-item-use-and-training.md','wp20-hp-status-moves-helditem.md'])]
}
for doc, bands in catalog_bindings.items():
 for first,last,names in bands:
  parents=[u for u in UNITS if u['formal_path'] in {SPEC[x]['path'] for x in names}]
  sr=[]
  for u in parents:
   for s in u['source_refs']:
    ref=f"{s['path']}:{s['start_line']}:{s['end_line']}"
    if ref not in sr:sr.append(ref)
  add(doc,first,last,'Catalog bounded vectors '+','.join(n.split('-')[0] for n in names),
      'Each displayed vector was freshly read with its stated input and dependent entry. It is DERIVED_VECTOR/NOT_EXECUTED. Numeric computations are independently checkable; current foreign source/consumer bindings inherit the parent unit limitations. Cross-file catalog headings are editorial only. Wurmple10000/10005 examples denote the named high-half16-bit input, not full32-bitID.',tuple(sr),
      status='DERIVED_VECTOR_PARENT_BINDINGS_RETAINED')
  UNITS[-1]['primary_unit_ids']=[u['id'] for u in parents]

# Compiler catalog inherited units do not replace delegated WP04 source proof.
for u in UNITS:
 if u['formal_path'].endswith('test-catalog/generic-kernel-wp02-03-04.md') and u['start_line']>=37:
  u['status']='DERIVED_VECTOR_DX_COMPILER_BINDING_PENDING'
  u['imported_owner']='R6-DX'
  u['new_fact']+=' PBS lifecycle/extract/recompile writers and six-column/enum grammar are explicitly delegated; own registry/schema facts are prerequisites only.'
