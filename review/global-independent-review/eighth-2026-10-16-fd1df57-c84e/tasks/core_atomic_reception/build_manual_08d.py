import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_08c.json').read_text());d=base['source_dictionary'];rows=[]
d['scene_fight']={'path':'Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb','range':[68,133],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_FIGHTMENU_METHOD_ACTUALLY_READ; no nativewindow execution'}
d['escape_handlers']={'actual_reader':'/root/core_atomic_reception','complete_units':[{'path':'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','range':[2553,2569]},{'path':'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','range':[3204,3208]},{'path':'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb','range':[1944,1948]}],'reading':'OwnFULL effectparents plus actualcomplete specific defaulttrapping/escape registrations reread; itemtrapping group is empty in fixed ownFULL1948/default facts, not plugin guarantee'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(464,[
 'CanShift first rejects only when BOTH declared side sizes<=2. Thus ordinarydouble/single rejects, but ownside2 against opposing3 can reach its own2-seat destination branch.',
 'Then ownside1 rejects; ownside3 actor in central field2/3 rejects; ownside2 destination=(index+2)%4; outer triple actor destination2 ifeven else3.',
 'Current owner index at actor and computed destination must match. The query has no explicit missing/fainted-target guard; actual Swap later separately rejects missing actors/opposition/differentowner.',
 'SceneFightMenu computes shiftMode1/0 from CanShift once on opening and only SPECIAL input with positive shiftMode yields−3; command callback unregisters Mega then bare RegisterShift. Native rendering/input execution remainsNOT_EXECUTED.'
],['other','battlefull','owners','scene_fight','command','ui_command'],'global sizes→ownside/destination→owner equality→scene permission→Megaunregister/barechoice; executor has separate guards.')
row(465,[
 'Shift registration only writes actionShift/index0/movenil; it doesnot swap during command selection or repeat CanShift internally.',
 'Attack move scanner accepts currently living actors with UseMove or Shift and not movedThisRound, respecting forcednext/quash and ordinarypriority. Shift executes through ProcessTurn, not move PP/use algorithm.'
],['other','attack','use','command'],'bare register→later actual live/unmoved priorityscanner→ProcessTurn Shift branch.')
row(466,[
 'ProcessTurn computes destination from current declared ownside size:2→(index+2)%4;3→outer to parity central2/3; central or othercase remains−1.',
 'Only nonnegative destination calls Swap; the execution branch doesnot rerun selection CanShift. A directly forced malformed/unqualified Shift can therefore reach different no-swap/cost behavior.',
 'Swap itself rejects absent actor at either index, opposite sides, or current owner-index mismatch before objectwrites; no liveness rejection for the other actor is added.'
],['use','swap','other','battlefull'],'current size/destination→optional Swap with own existence/ownerguards; directregistration not qualificationcertificate.')
row(467,[
 'Successful Swap first exchanges @battlers references, then their index fields, then choices arrays, then invokes scene.SwapBattlerSprites.',
 'It subsequently remaps specified cross-target effect indices on current living allBattlers. Same Pokemon/battler objects move; no InitPokemon, partyorder exchange, scene.SendOut or entry chain.',
 'Scene failure can occur after object/index/choices exchange but before reference remap; returnfalse from an earlier guard is distinct from exception and ProcessTurn doesnot test that boolean before its later message/cost.'
],['swap','use','battlefull'],'objects→indices→choices→sprites→specifiedrefs; nontransactional source order and ignoredboolean retained.')
row(468,[
 'For each current living actor, Swap remaps Attract,BideTarget,CounterTarget,MirrorCoatTarget,LockOnPos,MeanLook,JawLock,Octolock,SkyDrop,TrappingUser only when value equals either exchanged field index.',
 'Each matching value becomes the other index; unrelated indices and all other effect entries remain untouched by this remap routine.',
 'LeechSeed deliberately remains position-based because recipient HP goes to current savedposition occupant; PerishSongUser only side matters and same-side Swap preserves it.',
 'Counter damage amount is not swapped/reset by target-index remap. No all index-valued fields identity-follow guarantee or remapping of currently fainted/nonliving recipients is inferred.'
],['swap','battlerfull','use'],'fixed ten targetidentity fields A↔B on livecollection; explicit positional/side exceptions and unmodified damage data.')
row(469,[
 'When destination>=0, ProcessTurn calls Swap then emits moved across for ownsize2 or moved to center for ownsize3, based on its current side after any successful indexchange.',
 'It doesnot inspect Swap return value, so guarded refusal can still produce the movement message. A scene exception prevents reaching that message; normalqualified fixture has actualsameowneractors and succeeds.'
],['use','swap','other'],'computed destination→Swapcall→size-specificmessage irrespective boolean, subject actual normalreturn.')
row(470,[
 'After Shift optionalswap/message, ProcessTurn calls BeginTurn(choice), CancelMoves, then writes self.lastRoundMoved=current turnCount and returnstrue.',
 'BeginTurn clears DestinyBond/Grudge/MoveNext/Quash and staleEncore fields per exact source; CancelMoves handles finalOutrage confusion and clears TwoTurnAttack/Rollout/Outrage/Uproar/Bide/currentMove conditionalHyperBeam/FuryCutter, not HyperBeam itself.',
 'Neither routine clears Counter damage amount. CounterTarget follows earlier ten-field remap; normal complete EOR tail later separately resets Counter/CounterTarget.',
 'No move PP reduction occurs through this Shift branch, and the other moved Battler keeps its object/choice/moved history rather than spending an additional action automatically.',
 'Acting object moved stamp makes its newly occupied field slot skip later scanner attempts, provided no later reset/reentry. Failure before stamp can leave swap/cleanup prefixes without markingdone; no atomic movement-and-cost promise.'
],['use','swap','attack','eor','battlerfull'],'swap/message→BeginTurn→CancelMoves→actingobject movedstamp→scanner filter; no secondactor actioncharge or PPwriter.')
row(471,[
 'Swap requires same side and same current owner. Pokemon partyindex/ownerobject/participatingarray references stay on the moved object; exchanging field indices doesnot reassign trainersegments.',
 'Adjacency remains exact position-table relation, not persistent relation between the two Pokemon identities. After indexexchange, later target eligibility recomputes proximity using current indices.',
 'No new targettable policy or complete replay of already resolved targets is implied; previously stored specific effectindices follow only the explicit remap set.'
],['swap','battlefull','teams','targetresolve','targetdata'],'sameowner activeindex exchange→later position-based adjacency; identity and targetdomain distinguished.')
row(472,[
 'Shift source has no SwitchOut ability/Peerleave, new InitPokemon, SendOut, entry hazards, entryability or entryitem invocation. It moves existing on-field objects and their choices.',
 'Actual replacement chain performs those separate oldcleanup/newbinding/entry stages under exact earliergates; no equality between Shift and replacement induced by both changing positions.',
 'Selection CanShift and actualpriority/unmoved/living ProcessTurn gates still apply; bare RegisterShift alone doesnot certify successful swap or normal presentation.'
],['use','swap','other','switching','ability_item','peer','attack'],'positionmovement without leave/entry versus actual replacement callbacks; keep WP40 qualification/timing.')
row(473,[
 'CanRun query first rejects trainerBattle, then rejects !canRun only for nonopposing actor. Wild opposing query bypasses that configuration refusal but still evaluates its other actual gates.',
 'Then Ghost withMORE_TYPE_EFFECTS, activeCertainEscape ability, activeCertainEscape item each returntrue before aggregate trap. Fixed RUNAWAY and SMOKEBALL complete handlers simplytrue when reached.',
 'Then aggregate trapped state refuses; each current living opposingbearer is visited with active abilitytrap then active itemtrap in the same perbearer loop.',
 'Default ArenaTrap refuses grounded switcher, MagnetPull Steel switcher, ShadowTag switcher without activeShadowTag; itemtrap registry empty under fixeddefaults. These queries write no runCommand/choice/decision themselves.',
 'Source callback/getter errors and malformed missing actor are not certified harmless; querytrue is permission for caller, not probability success or the same guards as Run execution.'
],['running','escape_handlers','battlerfull','ability_item','b_settings'],'trainer/config→Ghost/activecertainescape→aggregate→perbearerabilitythenitem→true; no executioncommit.')
row(474,[
 'Run execution first handles opposingactor: trainer returns0; wild writes choices[actionRun,index0,movenil] then returns−1, before Debug/config/trap/probability. No player-style calculation or decision3 here.',
 'Own-side then DebugRun; any nonzero return is returned immediately. Next trainerBattle: internal displays cannotrun and0; external mayconfirmforfeit, sound/message,decision3 and1, else0.',
 'Next !canRun displayscannotescape and0. Only !duringBattle then checks Ghost, activeCertainEscape ability, activeCertainEscape item, aggregate trap, all-opponent abilitytrap loop, then all-opponent itemtrap loop.',
 'Deterministic success branches display/sound before writingdecision3 andreturn1; trap refusal message names actual bearer/abilityoritem andreturns0. If all pass, calculation is reached.',
 'Unlike CanRun perbearer interleaving, this execution exhausts abilitytrap loop before itemtrap loop. No query call wraps or normalizes these different source branches.'
],['running','escape_handlers','battlerfull','battlefull'],'opposingearlyregistration→debug→trainerforfeit→canRun→ordinarycertainescape/traps→calculation; distinct branch writes/refusals.')
row(475,[
 'duringBattle=true keeps earlier opposing/debug/trainer/canRun gates but skips entire !duringBattle group, including Ghost/RunAway/SmokeBall and aggregate/opposing trapping checks.',
 'It reaches rawspeed calculation even if ordinaryquery would report Ghost-guaranteedescape or traprefusal. It doesnot incrementrunCommand and uses the preexistingcount.',
 'EORSwitch consumes return<=0 as replacement requested, return>0 as thisslot not replaced; ordinary RunMenu instead consumes !=0 as stopcurrentplayerselection. Same integer return can therefore cause different caller action.'
],['running','switching','command','ai_finite'],'duringBattle flag→group skipped→existingcounter probability→caller-specific comparator, not sharedeligibility.')
row(476,[
 'TrappedInBattle aggregate tests positiveTrapping, MeanLook>=0, ownJawLock>=0, anycurrentlivingBattler JawLock==self.index, Octolock>=0, Ingrain, NoRetreat, positive fieldFairyLock in that order.',
 'It doesnot itself evaluate Ghost/certainescape/opposingtrap handlers. Ordinaryquery/run/canswitch callers can bypass aggregate through earlier own exceptions; duringBattle Run omits aggregate entirely.',
 'Concrete Bind/MeanLook/JawLock/Octolock/Ingrain/NoRetreat/FairyLock producers have distinct field/source/duration semantics; no claim all trapping shares a single timer or direct damage source.',
 'Run item success text names fleeing Pokemon and actual item; opposingtrap text names preventingbearer and actual ability/item. Optional switching PartyScene feedback is a separate UIreceiver.'
],['battlerfull','running','switching','switch_effects_full','escape_handlers'],'actualaggregatefields→callerorder/bypass→specificfeedback; identity/source/duration not collapsed.',open=['All nonselected concrete Ingrain/FairyLock/NoRetreat producer class→expiry consumers beyond existing precise primary/reset and Move-note receptions remain individually OPEN; aggregate and caller gates are complete.'])
row(477,[
 'DebugRun only opens commands for $DEBUG && Ctrlpressed. Choices win/loss/draw/run/capture(wildonly)/cancel set exactdecisions1/2/5/3/4 or return−1 withoutchange; ordinarynondebugreturns0.',
 'Run executes Debug before trainer/canRun and returns its nonzero value. Cancel−1 therefore never reaches ordinaryprobability or incrementsattemptcount.',
 'RunMenu returns Run()!=0. PlayerCommandLoop interprets thistrue as commandsEnd and breaks remaining player selection even on debugcancel; decision still0 then permits later AI loop.',
 'This differs from a fight/party menu cancel. It doesnot imply Debugcancel wrote :Run choice, decision3, PP consumption or a new movedstamp.'
],['running','command','battlefull'],'debugInput→exactreturn/decision→RunMenu nonzero→commandsEnd→possiblyAI continuation; no invented ordinaryattempt.')
row(478,[
 'CanRun query, Run(false), Run(true) have genuinely different source guard ordering/sets and side behavior as C0473–C0475; none is implemented simply by calling another.',
 'Run and CanSwitchOut share rawaggregate and namedtrap handlers, but CanSwitchOut owncertainSwitching/ShedShell gate differs from RunCertainEscape/SmokeBall and trainer/config/probability behavior.',
 'Neither escape path contains switchStyle opponent-next-name confirmation or replacement binding. EORSwitch owns its own nextquestion and consumes Run return as a later caller.'
],['running','switching','escape_handlers','battlerfull'],'shared predicates with distinct callercontracts; no three-entrycommon-guard equivalence or run-induced replacementself.')
row(479,[
 'runCommand starts0 in constructor; only reached calculation increments by1 and only !duringBattle. Early opposing/debug/trainer/canRun/certainescape/trap returns leave it unchanged.',
 'The increment precedes speed reads/rate/RNG/feedback and persists even if those later operations error. duringBattle reads existing accumulatedcount withoutincrement.',
 'Earlier Ghost/RunAway/SmokeBall deterministic successes skip calculation/count; speedPlayer>speedEnemy yields rate256 inside calculation and normalordinaryattempt has ALREADYincremented. The complete paragraph first condition governs this distinction.'
],['battlefull','running'],'constructorcounter→reachedcalc conditionalincrement→speed/rate/RNG/feedback; deterministicearlygates versus calc-speedcertainty separate.')
row(480,[
 'Escape calculation reads Battler.speed rawcachedvalue for actor and currentlivingopponents, never pbSpeed stage/ability/item/weather computation.',
 'This rawcache can be changed by actual Transform/refresh/init; it is not immutable original Pokemon speed. Opposing maximum begins1, so no currentlivingopponent leaves denominator1.',
 'Static formula below assumes ordinaryvalid positiveinteger cachedspeeds. No guarantee arbitrarydebug/customvalue or missingactor cannot raise, and no universaloriginalspeciesstat equality.'
],['running','battlerfull','b_change','b_init'],'current rawcache→maxopponents(min1)→formula; speedmodifiers versus cachewriters distinguished.')
row(481,[
 'If rawactor speed strictly greater than maximum opponentrawspeed, rate256; equality instead enters floor(actorSpeed*128/enemySpeed)+runCommand*30.',
 'For ordinary firstattempt speed64 vs128 with constructorcount0, increment makescount1 and rate64+30=94; duringBattle at priorcount0 insteadrate64. No floating quotient or implicit minimumchance adjustment.',
 'Counter coefficient is30 regardless of party size/individualoriginalspeed; rate is not clamped before comparison. speedfaster branch ignorescount inrate but countwrite already occurred whenordinary.'
],['running','battlefull'],'rawspeed strictcomparison→integerdivision+existing/incrementedcounter30; explicit static numericcontrols.')
row(482,[
 'rate>=256 succeeds without RNG call due short-circuit; otherwise AI.pbAIRandom(256) supplies0…255 globalrand under finite received AIutility contract, success only when draw<rate.',
 'Rate94 control succeeds draw93 and fails94. Onsuccess sound→pausedmessage→decision3→return1; failure pausedmessage→return−1 withoutdecisionwrite.',
 'Feedback/RNG exceptions can preserve priorcounterincrement and preventdecisionwrite; sourceproof is not proof native sound/text or observed random behavior ran.'
],['running','ai_finite'],'rate threshold→optionalAIglobalrand strictcomparison→sound/message beforedecision orfailurefeedback, no rollback.')
row(483,[
 'Ordinary computed failure−1 makes RunMenutrue and ends remaining player choices, representing roundactionopportunity cost through its caller. Bare Run doesnot write self.movedround or ordinaryplayerRunchoice in that branch.',
 '0 ordinarily means impossible/noattempt and RunMenufalse permits choice loop continue; 1 means reachedterminal/debugsuccess and stopsplayerselection. Debugcanwrite outcomesotherthan3.',
 'Opposingwild−1 is registeredRun rather than computedfailure, Debugcancel−1 is noattempt/no decision, and EOR−1 causes replacement. Full§7.1 exceptions prevent treating −1 as one globallyuniformeffect.',
 'Later attack scanner/AI/decision checks decide what proceeds; no PPcost or guarantee all alreadyforced playeractions canceled is inferred from stopping newplayerchoices.'
],['running','command','attack','switching','ai_finite'],'exactreturn→actualcaller comparison→selectioncontinuation/terminal/replacement, context-sensitive cost.')
row(484,[
 'Ordinary flee/forfeit success records decision3 after actual reached sound/message; it doesnot itself call full EndOfBattle or overworldcleanup.',
 'Caller-specific decision checkpoints determine when normal ending reaches reward/item/form/Peer/scene/worldafter hooks. Existing sourceprefixcounter/choice/UI writes remain; decisiononly shorthand here doesnot mean literally no other fields/messages changed.',
 'Facility externalforfeit uses its reached confirmation/sound/message/decision3/return1 path; complete facility battlewrapper may prepare/restore persistent objects separately, not infer it ran from this setter.'
],['running','command','switching','startendfull','after','wrappers'],'flee/forfeit terminalintent→actualouterdecision checkpoint→separate ending/world/facility consumers, no cleanupfrominteger alone.')
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_08d.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children'])for x in rows),'open_rows':sum(bool(x.get('open'))for x in rows)})
