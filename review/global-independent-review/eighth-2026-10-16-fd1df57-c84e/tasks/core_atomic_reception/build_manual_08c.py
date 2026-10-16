import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_08b.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(450,[
 'EORSwitch has two pre-Judge gates: existing decision>0 returns when !favorDraws; existing decision5 returns when favorDraws. Only if these allow does Judge execute.',
 'Judge reads both persistent participating-side all-fainted results: both→DecisionOnDraw, onlyplayer→2, onlyopponent→1; if neither, it doesnot clear an existing decision.',
 'After Judge, any positive decision returns before replacement scan. Default draw5 and actual selfkoclause lastMoveUser-based draw override are separate; favorDraws doesnot generally erase existing positive results or force a replacement.'
],['switching','startendfull','clauses','battlefull'],'preexistingdecision/favor gates→actual persistentparty Judge→positive return→only undecided scan.')
row(451,[
 'EORSwitch allocates switched[], clears it each loop, and scans @battlers in array order, skipping nil and actors not currently fainted.',
 'It reads each actual actor.index at visit, not its former partyindex. Replacement occurs immediately per selected slot, while entry notifications are postponed until the entire scan finishes.',
 'After a scan, zero actual replacement breaks; otherwise entry receives that scan list and the loop rescans from the first array slot. No fixed one-pass bound or automatic sort by speed applies to choosing replacements.'
],['switching','battlerfull'],'array-order faintscan→immediatebind/list append→one entry dispatch→rescan until no appended replacement.')
row(452,[
 'Before owner/wild/UI branch, CanChooseNonActive scans all participating party indices and returns true on first CanSwitchIn success.',
 'The in-only query excludes out-of-range/nil/egg/wrong-owner/persistentfaint/currently-active candidates; it doesnot use duplicate registeredSwitchOut or currentactor trapping gates.',
 'No qualifying candidate means next for that slot without replacement error/message generated here. Other callbacks or a later choice error are not covered by that benign empty-candidate skip.'
],['switching','battlefull','ai_finite'],'per-slot current in-only candidate existence→skip or owner-specific producer, distinct from combined voluntary switching.')
row(453,[
 'Non-player-owned slot includes opponents and own-side partners. Wild actor in this branch skips replacement; a partner is not wild merely because currentbattle is wild.',
 'Otherwise SwitchInBetween chooses playerUI only for actuallyplayerowned&&!controlPlayer; this nonowned branch delegates AI.DefaultChooseNewEnemy, receiving a party-array index without registering SwitchOut.',
 'Only the full switchStyle prompt conjunction triggers the optional player exchange: internalBattle, switchStyle, trainerBattle, playersideSize1, currentreplacementopposes, player0living/notalreadyinthisscanlist/haseligiblebench/Outrage0.',
 'Prompt candidate name uses real enemy party chosen index, optionally same-owner LastInTeam name for rawILLUSION with no globalNG. That name-query can fail before either optional player replacement or foe replacement; it doesnot repair partyorder.',
 'After player confirms, SwitchInBetween(0,false,true) is strict combined qualification and cancelable; nonnegative result gives recallmessage→RecallAndReplace0→append0. Negative cancel skips only optional player exchange.',
 'Then the originally chosen nonowned slot is recalled/replaced and appended. The player exchange occurs before that foe binding; entry notifications wait for scan end, so neither optionalplayer nor foe immediately gets fullentry here.'
],['switching','teams','battlefull','ai_finite','scene_party'],'nonowned/nonwild→AIcandidate→bounded style/name prompt→optional cancelable player replacement→foe replacement→scanend entry.')
row(454,[
 'Actuallyplayerowned fainted slot in trainerBattle uses GetReplacementPokemonIndex(random=false)→SwitchInBetween(checkLaxOnly=true,canCancel=false).',
 'PlayerUI route is in-only noncancelable replacement selection without RegisterSwitch; controlPlayer instead uses actual AI candidate producer.',
 'After returned candidate, it directly RecallAndReplace then appends slot; no new voluntary CanSwitchOut/duplicate guard or separate registered SwitchOut action is inserted at executor.'
],['switching','ai_finite','scene_party','command'],'owned trainerfaint→mandatory lax producer/UI-or-AI→direct replacement→entry-list append.')
row(455,[
 'Actuallyplayerowned fainted slot in wildBattle first asks Use next Pokemon?; yes sets switchtrue without running escape.',
 'No invokes Run(slot,true); return<=0 sets switchtrue, return>0 leaves this slot unfilled. Thus a failed escape−1 and impossibleattempt0 both lead to replacement, while debugcancel−1 also does; this is not plainmenu cancel semantics.',
 'Run duringBattle still performs opponent/debug/trainer/canRun early layers but skips Ghost/certainability/certainitem/aggregate/opposingtrap group. It uses existingrunCommand without increment.',
 'When switchtrue, mandatory in-only noncancelable replacement producer then RecallAndReplace/list append is reached. A positive ordinary run sets decision3 but this local owner branch merely leaves its slot unchanged.'
],['switching','running','scene_party','ai_finite','battlefull'],'wild nextquestion→yes or duringBattle runreturn comparison→mandatory replacement or skipthisslot; no inferred immediate global return.')
row(456,[
 'Each scan with appended replacements invokes one Entry(switched) for all actual appended field indices after the scan completes; zero appends exits with no entry invocation.',
 'Entry own cached speed-order filtering, position recovery/hazards/faint/otherhooks use actual earlier C0438–C0446 children, not original scan order or a fresh unsorted sequential call per replacement.',
 'New entrants fainted by hazards can be eligible in the next complete scan; immediate binding means later choices see newly occupied partyindices. No assumed fixed number of repeats or rollback on later loop error.'
],['switching','priority','b_init'],'immediate binding affects later candidate census→scanend grouped speed-entry→hazard result→next faintscan.')
row(457,[
 'Reached RecallAndReplace order is old not-fainted recallanimation→switchout cleanup→single-side lineup→nonrandom replacementmessage→Replace binding/orderexchange→SendOut. Grouped EOR entry is later.',
 'Fainted old actors skip recallanimation only; randomReplacement suppresses replacementmessage only. Optional switchStyle playerexchange separately emits MessageOnRecall before its recall/replace.',
 'An exception stops the current method suffix and preserves prior recall/status/form/local-disable/order/Pokedex/used flags actually written; this sequence is not a combined transaction or unconditional completed message promise.'
],['switching','ability_item','peer','b_init'],'actual guarded oldcleanup/newbinding presentation chain→separate deferred fullentry; guard/failure prefixes retained.')
row(458,[
 'The optional opponent-sendout prompt requires all eight actual gates in C0453; no conjunction factor alone authorizes the prompt.',
 'Playerside declaredsize1 is the actual size gate; replacing slot must opposeplayer, so an own-side partner doesnot trigger the prompt even though it entered the same nonowned branch.',
 'Both player0living and HasEligibleBench0 are required, plus player0 not already in current scan switchedlist and Outrage==0. This is per scan list, not a battle-long already-switched prohibition.',
 'Doubles/triples on player side skip; no assertion that an asymmetric battle with player1/opponent2 is categorically excluded beyond the actual stated conjunction.'
],['switching','battlefull','teams'],'actual owner/declaredsize/internal/style/liveness/bench/current-scan/Outrage conjunction→prompt; no broadened symmetric-layout assumption.')
row(459,[
 'Within the fainted-slot scan, successful owned wild Run(true) can set decision3 and returnpositive, making only that slot switchfalse. EORSwitch has no inside-scan positive-decision break after that call.',
 'Later fainted eligible ownslots in the same array scan can still prompt, select, bind, exchange partyorder and SendOut; completed list then receives entry even with decision3.',
 'Under all normalcallbacks/nootherdecisionwriter and nonlethal entry fixture, later position healing and nonlethal hazards may commit while decision stays3. Existing positive decision doesnot itself gate generic entry at its start.',
 'On the following EORSwitch loop scan, all stillfainted slots are reconsidered by the same actual branches; finite intended control chooses no further replacement or exits with emptylist. No global eventualtermination promise is inferred for unconstrained repeated userchoices.',
 'After EORSwitch returns, ordinary EOR master explicitly tests decision>0 and returns before distantShift/continualchecks/tailcleanup; clauses wrapper suddenDeath additionally requires decision0, so it doesnot replace this unchanged3.',
 'One eligible waiting slot and no other replacement can produce no secondprompt/entry. Existing positive decision on ordinary initialcall returns at entry. Firstslot acceptingreplacement never wrote escape3. Correct existing paragraph is preserved.'
],['switching','running','eor','clauses','ability_item','peer'],'successfulrun earlyslot→continued same-scan later replacement/entry prefixes→normalreturn→EOR explicit positive checkpoint, bounded nonlethal controls.')
row(460,[
 'Choosing No to Use next Pokemon? launches an escapeattempt, not cancellation of the entire EOR call. Its return is consumed by <=0 switch predicate.',
 'The subsequent required replacement UI has canCancel=false; Scene negativechoice repeats rather than returning. Optional switchStyle player replacement separately allows cancel.',
 'Run sound/display precede ordinary decision3 write; replacement selection precedes binding/order/sendout; entryposition/HP/item flags commit only on reached paths. Later exceptions preserve completed prefixes and do not guarantee decision remains3.',
 'This paragraph deliberately limits successful continuation evidence to nonlethal case. Hazards causing genuine faint/Judge/end callbacks require their own exact result path; no lethal-result extrapolation.'
],['switching','running','scene_party','b_change','eor','errors'],'distinct no-next escape / mandatory choice / optional promptcancel→specific commit points→no transactional restoration.')
row(461,[
 'Per array visit only currently fainted nonnil actor with current in-only candidate exists is processed; prior scan membership doesnot reserve a second unused field object.',
 'Simultaneous fainted slots are selected/replaced by @battlers order, and only after scan does grouped entry use speed order. These two different orders cannot be collapsed.',
 'Switchedlist clears every loop and newly hazard-fainted entrant is revisited if eligiblebench remains; no automatically successful entry or explicit artificial iteration cap.'
],['switching','priority','battlerfull'],'array selectionorder versus grouped speedentry order; live qualifications reread next pass.')
row(462,[
 'Nonowned wild Battler is explicitly skipped even when CanChooseNonActive found an eligible same-owner candidate. Declared side-size doesnot create a wild replacement permission.',
 'Owned player faint in a wildBattle still takes its nextquestion/run/replacement branch, so wildbattle category is not a blanket ban on all participants switching.'
],['switching','battlefull','battlerfull'],'nonowned + actualwildactor→skip, while owned wildbattleplayer follows ownbranch; no size-based exception.')
row(463,[
 'Partner belongs player side but pbOwnedByPlayer? false; it therefore takes nonowned replacement path and actual AI.DefaultChooseNewEnemy, not the players own mandatory PartyScreen branch.',
 'It doesnot satisfy opposes? required for optional switchStyle opponent announcement, so it cannot itself trigger that player offer.',
 'Ownership remains current trainer segment through candidate qualification/binding/sceneownername; original individual Owner data or sideparity alone cannot select the branch.'
],['switching','teams','battlefull','ai_finite'],'same-side nonplayerowner→AI partycandidate→no opponent offer→normal deferred entry; originalOwner not selector.')
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_08c.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children'])for x in rows)})
