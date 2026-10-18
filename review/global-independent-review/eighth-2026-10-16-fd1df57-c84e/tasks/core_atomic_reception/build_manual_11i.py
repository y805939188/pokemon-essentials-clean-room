import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11h.json').read_text());d=base['source_dictionary'];rows=[dict(number=898,layout_reason='E table column heading only; normal terminal/world vectors separately preserve old/current decision and actual object identities.')]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(899,[
 'E01 enters normal EndOfBattle with old decision1, wild battle and nonempty caughtPokemon.',
 'It saves oldDecision1 then writes current decision4, but case dispatch still uses oldDecision1.',
 'That old win branch skips its early GainMoney because currentdecision==4.',
 'The common tail records/stores caught Pokemon first and only afterward calls GainMoney for currentdecision4.',
 'World SetOutcome counts4 in wild battles won and the ordinary wild wrapper returns true for4.',
 'This is normal-return flow, distinct from an AbortException rescue; capture/Box/callback failures can prevent the later reward/stat/result handoff.'
],['normal_end','catch_full','capture','wild','after','root_set'],'old1 saved -> current4 -> oldwin branch/no earlymoney -> caught store -> current4money -> outer winstat/wildtrue.')
row(900,[
 'E02 supplies internal trainer loss, canLose=true, moneyGain enabled, no-loss switch false, highest player-own level20, badge_count0 and money1000.',
 'LoseMoney uses only player owner0 team max level, not partner max.',
 'Badge index0 selects multiplier8, giving nominal loss160; available1000 is sufficient and money becomes840.',
 'Statistics increase by actual old-minus-new160 and positive-loss feedback reports160.',
 'canLose suppresses blackout feedback/startover logic where checked, but is not a LoseMoney exemption.',
 'Later world after_battle loss+canLose heals the player party; a registered partner would add its separate existence-based healing branch, absent in the stated no-partner control.',
 'Money/stat writes precede later feedback/healing errors and have no general rollback.'
],['money','playerfull','money_cap_config','teams','config','after','pokemon_heal'],'max ownlevel20*badge0mult8 -> money1000to840/stat160 -> later canLose healing, no money exemption.')
row(901,[
 'E03 has nominal trainer reward100 and both stored AmuletCoin/HappyHour flags true, with player money only50 below the cap.',
 'GainMoney doubles twice to nominal400, then Player.money= clamps the attempted balance to the configured upper limit.',
 'Actual moneyGained is measured after assignment, yielding50 rather than400.',
 'Only actual positive50 is added to battle_money_gained and shown in the winner reward message.',
 'The PayDay branch then separately doubles its stored amount as applicable, attempts another money assignment and measures that later actual increase; it cannot bypass the money cap.',
 'At an already full cap that later branch gives no positive money/stat/message increment, while its earlier stored PayDay multiplication may still have occurred.',
 'These are two sequential actual-delta operations, not one nominal400-plus-PayDay statistic.'
],['money','playerfull','money_cap_config','activefield_full'],'nominal100*2*2 -> clampedbalance actual+50 -> stat/message50 -> separate PayDay actual-delta/cap.')
row(902,[
 'E04 enters normal terminal flow with decision3, internal battle and an unused registered item choice.',
 'The case has no3-specific win/loss/capture reward branch, but the common caught-record/store and internal Pokerus propagation paths are still reached.',
 'Scene EndBattle precedes per-battler CancelChoice, which can refund the still-identified consumable under actual ownership/capacity rules and then clear choice.',
 'The common party leave/item-restoration loop follows, independent of winning or losing.',
 'World SetOutcome counts3 as a lost battle; ordinary wild wrapper returns true while ordinary trainer wrapper returns false.',
 'Normal callback/scene/refund success is required to reach later cleanup; this is not a guarantee an abort or arbitrary exception runs the common tail.'
],['normal_end','items','priority','pokemon_pokerus','peer','pokemon_item_exact','wild','trainer','after'],'decision3 no dedicatedcase -> commonstore/pokerus/sceneEnd -> cancel/refund -> restore -> outerloststat/wildtrue/trainerfalse.')
row(903,[
 'E05 has ordinary result2 or5 with canLose=false and a normally returning on_end_battle default callback.',
 'That callback checks evolution first under CHECK_EVOLUTION_AFTER_ALL_BATTLES or not-loss/draw logic; loss/draw therefore evolves here only when the all-battles setting permits.',
 'It then clears level/critical/direct-damage before-battle records.',
 'In the loss/draw !canLose branch it unpauses BGM and BGS before calling StartOver.',
 'StartOver itself has contest/recovery/home/map conditions, so the call is not proof every case transfers the actual player map.',
 'A failure before or inside return/recovery preserves reached record/audio/world prefixes; native transfer/resource execution remains untested.'
],['events','event_dispatch','startover','after','audio_path'],'onEnd -> configured evolution -> recordsnil -> BGM/BGS unpause -> conditional StartOver; actual transfer separate.')
row(904,[
 'E06 uses result3 with a registered PokemonGlobal.partner, regardless of whether partner_can_participate allowed this battle.',
 'World after_battle first regularizes player poison count and explicitly removes Mega/Primal forms.',
 'The partner-existence branch heals the current player party and each registered partner Pokemon, then removes partner Mega/Primal forms.',
 'It does not require the actual battle trainer array to include that partner or a win/loss result.',
 'Without a registered partner and without the separate loss/draw+canLose branch, this common code does not uniformly heal all player HP/PP.',
 'The actual registered-partner array and merged battle party are distinct identities; only normal reached helper writes are established.'
],['after','partner_array_producer','pokemon_heal','pokemon_mega_full','shadow_main'],'after common resets -> registeredpartner existence -> player/partner heals/resets, independent participation and result3.')
row(905,[
 'E07b preserves the complete GR013 fixture: ordinary single/no partner/no capture reshuffle/plugin/flag override, originalPikachu party0, preconstructed live Burmy form0 party1, Cave environment, sequential send-outs to slot0 and normal common terminal cleanup.',
 'Both SendOut calls set usedInBattle[0][slot0/2] namely index0 true, not the currently sent Pokemon party index1.',
 'The resulting player used flags are[true,false].',
 'Normal common terminal loop enumerates party indices and supplies usedInBattle[0][1]==false to Burmy Peer leave.',
 'Burmy handler requires endBattle AND usedInBattle; the false input leaves stored form0 and does not create a new form1 seen entry via this handler.',
 'Burmy was explicitly constructed earlier and not recreated in Cave, excluding the separate getFormOnCreation Cave choice1.',
 'Actual prior participation does not repair the slot-versus-party-index mismatch; this is already captured GR013 and no new finding is added.'
],['send','normal_end','peer','burmy_leave','crec_form_join','b_init'],'two slot0send writes flag0only -> terminal partyindex1 readsfalse -> Burmy leave guard -> form0/no newform1dex.')
row(906,[
 'E08b independently puts the same preconstructed Burmy at party0 and initially sends it to slot0.',
 'SendOut records flag0true and terminal partyindex0 therefore passes used=true with endBattle=true.',
 'The Cave branch returns form1; Peer commits that form through Pokemon.form= when it differs.',
 'The actual form setter recalculation/global-player seen-form registration follows the finite complete form reception, so this normal control can register form1.',
 'It is not a correction making all send-out records party-indexed or a claim every storage/native persistence path executed.'
],['send','normal_end','peer','burmy_leave','crec_form_join'],'Burmy party0/slot0 flagtrue -> Cave leave1 -> real form setter/recalc/dex; isolated control.')
row(907,[
 'E09b directly supplies Burmy leave-handler inputs usedInBattle=true,endBattle=true in Cave.',
 'The complete handler returns form1 under those explicit inputs, consistent with WP21.',
 'It does not discover actual participation or validate the producer record itself; the caller controls the supplied flags.',
 'The producer mismatch in E07b therefore does not make the handler rule wrong or require changing its correct standalone contract.'
],['burmy_leave','peer','crec_form_join'],'explicit true/true Cave -> handler1; caller record provenance separate, correct handler preserved.')
row(908,[
 'E07 propagation starts by collecting the original player-party indices whose PokerusStage==1.',
 'Each original source reads its strain and conditionally infects its currently uninfected immediate left then right neighbor on rand(3)==0.',
 'With only the middle originally infected and the two stated draws0, both adjacent uninfected members receive the same valid strain.',
 'The collected infected index list is not enlarged after those writes, so a newly infected neighbor does not become a fresh source and propagate farther in that pass.',
 'Existing other original infected sources can still act in their own turn; the no-chain statement is this snapshot-source rule, not a general future-round immunity.',
 'Each givePokerus writes the persistent individual; current save/reload remains the bounded serialization contract, not an executed save.'
],['normal_end','pokemon_pokerus','playerfull'],'snapshot stage1indices -> each original strain -> left/right rand0 -> writes without extending source list.')
row(909,[
 'E08 reaches debug battle-loop turnCount>=100 with time-decision computed1 before explicit pbAbort.',
 'Abort raises the dedicated Exception subclass, bypassing the remaining normal loop/EndOfBattle call.',
 'The public StartBattle dedicated rescue catches it, overwrites decision0, calls only Scene.EndBattle0 and returns0.',
 'Normal capture/common Pokerus/choice-refund/party item restore from EndOfBattle are not supplied by this rescue.',
 'If the world core receives this normal rescued return, it can still run after_battle and SetOutcome0, with the ordinary wild wrapper true for0.',
 'No game execution or universal handling of unknown exceptions is inferred from the dedicated abort catch.'
],['battle_loop_complete','abort_raise','startendfull','wild','after','root_set','pbdebug'],'debug100 decision1 -> AbortException -> dedicatedrescue decision0/SceneEnd -> world after/set0/wildtrue, no normalEnd.')
row(910,[
 'E09 gives a registered consumed Bag item not yet used when explicit abort happens.',
 'Registration consumption is an earlier actual Bag write, independent of later terminal cleanup.',
 'The dedicated abort path skips normal EndOfBattle CancelChoice refund, so that refund is not guaranteed.',
 'World after_battle heals/resets/notifies under its own predicates and does not implement a replacement Bag refund loop.',
 'An arbitrary exception is even less reason to assume a universal restore; exact reached write/rescue/callback boundaries must be retained.'
],['items','priority','abort_raise','startendfull','normal_end','after','bag'],'registered Bag decrement -> abort skips normal cancel/refund -> outerafter no substitute refund.')
row(911,[
 'E10 uses outcome0 with CHECK_EVOLUTION_AFTER_ALL_BATTLES=false and an existing before-level record showing a real increase.',
 'The on_end condition still invokes EvolutionCheck because0 is neither2 nor5.',
 'For a nonEgg eligible individual, EvolutionCheck can use the existing recorded lower level to test level-up evolution, then separately after-battle evolution if no species found.',
 'If a skipped start did not establish a level record, that branch cannot invent an old level or infer a level-up from absence.',
 'The separate after-battle evolution test may still be called; absence of the old record is not a blanket no-evolution claim.',
 'Actual scene evolution/species-form mutations are limited to received finite consumers; this is callback reachability and prerequisite handling.'
],['events','record_start','after','event_dispatch'],'result0 !=2/5 -> EvolutionCheck -> existingoldlevel comparison OR skipmissing -> separate afterbattle check.')
row(912,[
 'E11 supplies a nonEgg Pickup-ability Pokemon with no held item and first draw9, then explicitly filtered common/rare arrays shorter than18/11.',
 'Draw9 passes the strict rand100<10 entry gate.',
 'The source then checks filtered list lengths before building the level window or drawing the weighted item.',
 'If either declared threshold is short it returns without setting a held item; it does not insert a default fallback ID.',
 'Independent draw10 fails the earlier probability gate before list selection, rather than reaching the same short-array return.',
 'Unknown item/native registry handling outside the explicitly filtered-array fixture remains separate, not a hidden all-default-data assumption.'
],['events','pokemon_ability_queries','pokemon_item_exact','itemdata'],'eligiblePickup -> draw9 -> filtered lengths18/11 gate -> return noitem; draw10 earlierreturn.')
row(913,[
 'E12 keeps every default common/rare identity defined, eligible Pickup/nonEgg/emptyitem, first draw9 and level1.',
 'The start index formula clamps level to<=100 and gives0 for level1, selecting common positions1–9 and rare1–2.',
 'The concatenated integer weights total100; common entries occupy draws0–97 and the two rare windows98/99.',
 'Independent second draw98 selects rare1 HYPERPOTION, while99 selects rare2 NUGGET.',
 'Pokemon.item= writes the registered selected item to the same persistent individual on the normal branch.',
 'This is two controlled second-draw cases after the first10-percent gate, not an empirically measured chance or automatically independent runtime sample.'
],['events','pokemon_ability_queries','pokemon_item_exact','itemdata'],'level1index0 -> common1..9/rare1..2 -> integerweighted98/99 -> registered HyperPotion/Nugget setter.')
row(914,[
 'E13 keeps E12 eligibility/all-ID premises but changes level to91.',
 'The computed start_index9 selects common positions10–18 and rare10–11.',
 'Independent second draws98/99 therefore select LEFTOVERS/DESTINYKNOT respectively.',
 'The rare table preserves its duplicate entries at positions7/9/11 rather than deduplicating and shifting these windows.',
 'Normal registered setter behavior and the unexecuted RNG/data boundary remain as in E12.'
],['events','pokemon_ability_queries','pokemon_item_exact','itemdata'],'level91index9 -> common10..18/rare10..11 ->98Leftovers/99DestinyKnot; duplicate positions retained.')
row(915,[
 'E14 retains its complete identity fixture: full playerA..F, initial/currentA=X,B=Y, othersnil, legal inertitems, actual partner participation, ordinary two-wild battle firstdefeat then lastcapture, caughtnoitem, sendToBoxes0 and legal BoxA selection/space, no extra party/item callbacks.',
 'Actual partner participation makes set_up_player_trainers allocate a distinct merged battle array holding originalA..F references plus partner, while Player.party remains its own six-element array.',
 'Catch Store selectingA first runs its leave/poison/form cleanup and stores that same A object in the box, then deletesA from Player.party.',
 'Its remembered initialItems player indices shift left, giving[Y,nil,nil,nil,nil,nil] after the no-item capture is appended to current Player.party B..F,caught.',
 'The old merged battle party still holdsA..F,partner because this selected capture path does not rebuild it from current Player.party.',
 'Normal EndOfBattle enumerates that old merged array and assigns initialItems by its current numeric index via Pokemon.item=, not Battler.item=.',
 'Consequently boxedA is later changed fromX toY, oldB is setnil, and any later missing remembered entries clear their bound Pokemon items under the actual nil setter contract.',
 'Without partner participation, battle party aliases Player.party, so removingA removes it from the restoration enumeration; boxedA staysX and currentB restoresY.',
 'The stated inert current/initial items and no-other-callback premise prevent unrelated item moves/consumption from obscuring this identity control.',
 'This exact existing CP22-linked static anomaly is preserved without a new finding; storage/native/save/reload behavior beyond the actually received finite reference chain remains unexecuted.'
],['partner_array_producer','constructor','catch_full','capture','peer','normal_end','pokemon_item_exact','bag'],'distinct mergedparty refs -> Player deleteA/appendcapture +initialItemshift -> oldmerged terminalrestore -> boxedA=Y/B=nil; alias no-partner control A=X/B=Y.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11i.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
