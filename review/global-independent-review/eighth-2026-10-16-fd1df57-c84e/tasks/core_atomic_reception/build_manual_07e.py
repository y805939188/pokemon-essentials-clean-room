import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_07d.json').read_text());d=base['source_dictionary'];rows=[]
d['primal_producers']={'path':'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb','complete_units':[[4,36],[164,169],[171,176]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_MODULE_AND_TWO_REGISTRATIONS_READ; no other species handlers'}
d['ui_mainmenu']={'path':'Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb','range':[6,19],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_COMMANDMENU_METHOD_READ; no native UI run'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(351,[
 'Constructor initializes ownercount-sized per-side arrays to−1; normal qualified registration stores actorindex and reached successful Mega changes owner slot to−2.',
 'Normal CanMega requires−1, so two actors of same trainer share one perbattle allowance. Two different owners on one side have separate slots.',
 'Bare register/toggle APIs can overwrite slots and debug exception bypasses normal used/ring restrictions; whole-document normal once rule includes its earlier explicit qualification exception.',
 'Primal helper neither reads nor writes these slots and doesnot consume this allowance. No reinterpretation of Primal as another once-per-trainer Mega.'
],['other','battlefull','command'],'owner-array lifecycle→normal oneuse gate; exception layering and separate Primal domain.')
row(352,[
 'Primal helper returns for missingBattler/missingPokemon/fainted, then for !hasPrimal? OR alreadyprimal?. Battler hasPrimal rejectsTransform then realPokemon predicate.',
 'Pokemon.hasPrimalForm? calls MultipleForms getPrimalForm and tests nonnil; primal? calls same handler and compares returnedform to real @form.',
 'Default Groudon producer yields1 only hasItem REDORB; Kyogre yields1 only BLUEORB; absentitem implicitnil. MultipleForms dispatch returnsnil when no species/function entry.',
 'Battle helper has no Mega switch/ring/owner-slot/wildrestriction, so same valid Primal state can apply to either allegiance without Mega allowance. Form callback/resource conditions remain necessary.',
 'These are static reached predicates, not proof host loaded every default compiled species/item entry or all plugins. No actual battle execution.'
],['other','battlerfull','pokemon_mega_full','primal_producers'],'real formhandler+heldorb→Transform/liveness/alreadyform gates→Primal helper without Mega eligibility.')
row(353,[
 'Eligible Kyogre/Groudon select own firstanimation; other eligible custom species skip those cases but still proceed through generic form/UI/message.',
 'Pokemon.makePrimal invokes getPrimalForm again and assigns form when nonnil; battle form sync and pbUpdate(true) precede scenechange/refresh, second speciesanimation and generic message.',
 'This helper contains no Mega slotwrite or direct pbCalculatePriority call; other nested form callbacks remain separately scoped and no global prohibition on all indirect callbacks claimed.',
 'Animation/form/UI callback failure preserves earlier writes; no ensure reverting actualPokemon form and no guaranteed finalmessage on all failures.'
],['other','pokemon_mega_full','primal_producers','battlerfull','b_change'],'two handler invocations→real/battle form/cache→UI→message; no Mega-slot/directpriority interface.')
row(354,[
 'Call bare registration writes choiceaction Call/index0/movenil and returns true, without Shadow/status/type qualification or targetslotrewrite.',
 'Normal playercommand loop only reaches menu for actual owned/eligible unforced actor; CallMenu simply delegates bare register.',
 'Actual scene command grid uses SHADOW type existence AND trainerBattle to put Call in fourthslot, and converts returned3 to4. Other ordinary grids expose Run or Cancel there.',
 'Menu availability differs from callable registration and executor; no inference every callable Call requires actorShadow.'
],['other','command','ui_mainmenu','ui_command'],'player menu eligibility→type/trainer grid choice→Call code4→bareactionwrite.')
row(355,[
 'Attack Call stage selects living registeredCall, assigns lastMoveFailed=false before invoking pbCall, making it successful for later failure-based move logic.',
 'pbCall first invokes pbDebugRun; nonzero exits before Call feedback/result branches but doesnot undo already-cleared failureflag.',
 'Success classification doesnot require HP/stat/gauge change: ordinary no-effect Call still retains falsefailure; scene/debug exceptions can leave this earlywrite.'
],['attack','other','running','stomping'],'Call stage failureflagfalse→debug control→result branch; no success iff visibleeffect.')
row(356,[
 'After normal debug return, Call displays trainercalled/name before result checks; these messages can fail before later statewrites.',
 'If actualshadowPokemon? then inHyperMode branch writes Pokemon.hyper_mode=false before change_heart_gauge(call), then came-to-senses feedback.',
 'Shadow nothyper yields nothinghappened and doesnot enter following sleep/stat branches, even if its status is SLEEP.',
 'Only nonShadow and statusSLEEP invokes pbCureStatus; nonShadow/nonsleep eligibleaccuracy calls central raise by1 then pbItemOnStatDropped.',
 'Remaining branch shows nothinghappened. Central stat eligibility and ability/reflection transformations remain actual predicates, so requested+1 is not universal finalstage+1.',
 'Heartgauge writer, curestatus and stage machinery can commit before later feedback/item callbacks; the result branches are exclusive, no shared transactional cleanup.'
],['other','shadowother','battlerfull','b_change','ability_item'],'two initialmessages→Shadow-first hyper split→nonShadow sleep→eligibleaccuracy→noeffect; sequential writes and actual centralcallbacks.')
row(357,['This line explicitly delegates full Shadow gauge/purification lifecycle to WP23 while retaining battle Call entry/result taxonomy; it is a scopeboundary rather than a new wholeShadow behavior guarantee.'],['other','shadowother'],'scope routes lifecycle producer outside this WP40 battleentry; no cross-domain PASS transfer.')
row(358,[
 'CanShift first requires side0>2 OR side1>2; ownside1 returnsfalse.',
 'Ownside2 maps idxOther=(idx+2)%4; ownside3 refuses middle indices2/3, otherwise uses ownside center2/3.',
 'Computed destinationowner must equal actorowner. It is ownerindex equality, not all same-side actors eligible; no explicit destinationliving requirement in this predicate.',
 'Qualification is separate from bareRegisterShift and actual swap; valid declared layouts assumed, overflow bug context remains existing COM003.'
],['other','battlefull'],'sidesize→destinationmapping→owner equality→qualification; no allally/fainted target substitution.')
row(359,[
 'RegisterShift writes Shift/index0/movenil and true without rechecking CanShift or clearing targetslot itself.',
 'In processTurn, living actor Shift recomputes destination from ownside; nonnegative destination invokes pbSwapBattlers then across/center message.',
 'Then BeginTurn clears defined turneffects, CancelMoves resets multiturndata and actor lastRoundMoved=current; no ordinary move/PP path or EndTurn call in this Shift branch.',
 'Position swap is same activeobjects/index-linked arrays, not recall/newPokemon initialization/entry abilities. Full source swap contracts are continued in WP41.',
 'Swap/message failure can leave partially exchanged array/object state before cancel/completion; no guarantee completedShift in exception case.'
],['other','use','swap','battlerfull'],'bare Shift→actualpos exchange/message→BeginTurn/CancelMoves→completion; no switch replacement chain.')
row(360,[
 'Commandphase clears choice only for actual actors where CanShowCommands true; forced existing choices retained.',
 'Each player/AI loop skips missing/wrongownership actor, then nonNonechoice OR !CanShowCommands before adding actor to chosenaction list.',
 'Thus forced/multiturn actors do not consume that loop first-choosable/actioned selection slot. No claim they lack later attack actions.',
 'Current CanShowCommands also checks fainted and usingMultiTurnAttack; exact source overrides may vary for alternate battle classes.'
],['command','battlerfull','recordedfull','palace'],'command reset/loop eligibility→forced choice reuse versuschoosable tracking; execution distinct.')
row(361,[
 'Move register validates selection at that time; later TryUse/PP/target gates independently validate reached execution with actual current state.',
 'Item register removes consumable Bag unit after generic/handler qualification; family executors repeat relevant conditions and may refund on false according to concrete branch.',
 'Pre-PP move refusal leaves ordinary PP, post-PP noTarget/ownfailure retain deducted PP; specialUsage and unlimitedPP rules separately apply.',
 'Switch attack execution doesnot repeat combined CanSwitch? registration check, though interrupt/faint/battle decision and replacement callbacks still run.',
 'No global rollback connects registration and execution; failedcallback may preserve inventory/choice/HP prefix beyond ordinary false-return refund contract.'
],['priority','checksfull','use','itemhandlers','battleitems','items','attack','switching','bag'],'selectionwrite→state changes→family-specific executecheck→conditionalrefund versusretainedPP; distinct switch layering.')
row(362,[
 'Base commandphase calls whole playerloop first, checks decision!=0 and returns before AIloop if set; otherwise AIloop follows.',
 'Each command-loop outer iteration checks decision!=0 before advancing nextactor. Inner menu callbacks can return/create decisions with their explicit local control paths.',
 'The summary means phase/loop decisions truncate subsequent choices at reached checks, not a source guarantee of asynchronous interruption after every instruction or no cross-side stateeffect.'
],['command','running'],'fixed playerthenAI control→explicit decision checks; ordinary callback state changes may influence later selection.')
row(363,[
 'RunMenu returns pbRun!=0: codes−1 and1 end current playerselection pass, code0 retries/cancels via outer choiceclear.',
 'Normal run outcomes are decided now in commandphase; −1 failedrun still consumes selectionopportunity, 1 decision ends battle. Other forcedwild run has own executor.',
 'Item chosen whose ItemUsesAllActions true breaks remaining playerselection; default ball classification occupies pass, without proof catchsuccess.',
 'Actual scene regular firstAction has Run; later ordinary grid has Cancel, while Shadowtrainergrid maps Call instead. Firstaction refers eligible actioned list, not absolute Battlerindex0.'
],['command','running','items','ui_mainmenu','ui_command'],'current menu code→immediate Run outcome versusitem allactionflag→selectionpass end; no nextactor reordering.')
row(364,[
 'Original entry specialUsage and nonStruggle compute skipAccuracyCheck before any continuing-multiturn replacement.',
 'Continuing attack replaces chosen move by currentMove-derived BattleMove and sets specialUsage=true; ordinary reducer skipped, captured skipflag not retroactivelytrue.',
 'Specialusage guards regularmove bookkeeping; original regular entry versus nested/simple special call retained as distinct paths. No blanket identical history for all uses.'
],['use','checksfull','battlerfull'],'entry flagcapture→multiturnreplacement→effective specialusage→PP/history decisions; initial flagstable.')
row(365,[
 'Normal choosing target filters via targetmetadata/CanTarget and UI chosenindex; actual execution reconstructs/validates current targets separately after current-type setup.',
 'Redirection earlyreturns for Pursuit switchingcontext or position-target move; eligible single-target redirection checks ordered Spotlight then strongest FollowMe/RagePowder then elemental attracting ability.',
 'Counter/targetstate gates and currenteligible Near/opposition/liveness still apply; mere redirection flag doesnot override all geometry or all ability immunity.',
 'The shorthand eachstageonce doesnot forbid explicit later reconstruction (Curse after Protean) or pertarget/perhit checks already specified. No additional second redirect for that default Curse path.'
],['priority','targetresolve','redirect_producers','checksfull','use','ui_targets'],'selectiontarget→executiontarget→orderedredirection→later targetsuccess; explicitly named reconstruction retained.',open=['All AI-selected target producer branches and every concrete redirect/type callback not yet bound in current semantic pass remain OPEN.'])
row(366,[
 'Table comparator is descendingmovepriority/subpriority then TrickRoom-directed cachedspeed then tie; forcedNext/quash scheduler layers still apply.',
 'Every full calculation redraws tie; incremental config-triggered recalculation preserves it and cached bracketvalues, refreshing speed/current ability movepriority only.'
],['priority','attack','use','b_settings'],'summary binds full comparison and actual recalculation scope, not all schedule overrides.')
row(367,[
 'TryUse after earlier four gates returns true at capturedskipflagtrue before status/obedience tail; false reaches later sequence when earlierchecks pass.',
 'Struggle effective specialUsage true but skipflagfalse, so doesnot inherit status/obedience exemption from specialusage alone.',
 'Obedience itself bypasses continuingmultiturn/nonmove/noninternal/nonplayerowner, otherwise performs actual level/config and hyper checks.',
 'Integer BattleRandom256 handles level/alternate/sleep/selfharm choices, globalrand100 handles hyper; ordinary alternatemove continuation rereads and consumes actualnewmove PP, not originalmove.'
],['use','checksfull','shadowother','battlerfull','b_settings'],'two flags→TryUse earlygate→obedience restrictions→specificdraw/PP; preserve no-later-check guarantee only reachedskip.')
row(368,[
 'Normal Mega menu eligibility includes ring and owner-unused slot; registration then successfulhelper writes used−2. Earlier explicit debug shortcut remains qualified exception.',
 'Primal checks separate form/liveness without ring/Mega-switch/ownerregistration/count and helper doesnot consume Mega slot. No shared qualification contract.'
],['other','command','attack','pokemon_mega_full','primal_producers'],'normal Mega once/registration versusPrimal independent form eligibility; preserve same-document exception.')
row(369,[
 'Call taxonomy is Shadowhyper, Shadownonhyper, nonShadowsleep and remainingaccuracy/noeffect; Shadow branch takes precedence over sleep.',
 'Shift exchanges activepositions and cancels multiturndata with owncompletion write, whereas replacement recalls/reinitializes a Pokemon and entrynotifications through WP41. These actions cannot be merged.'
],['other','use','swap','switching','shadowother'],'summary selects exclusive Call branch and routes Shift versusreplacement actualconsumer chains.')
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_07e.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children']) for x in rows)})
