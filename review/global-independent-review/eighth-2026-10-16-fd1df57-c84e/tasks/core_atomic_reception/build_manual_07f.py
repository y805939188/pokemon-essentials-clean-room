import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_07e.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(370,[
 'After setup/thaw/Powder/primordial/Protean/quickcharge, actual targets empty AND actual targetdata.num_targets>0 AND !worksWithNoTargets? displays noTarget and marks currentactualuserfailuretrue.',
 'Ordinary successfulfrontchecks/PP5/noextraPressure already writes4 before this branch; no PP refund is called for noTarget.',
 'If earlier TryUse refused, ordinary PP unchanged and this noTarget branch is never reached. Specialusage/continuingmultiturn/unlimitedPP each retain own reducer rules.',
 'Common tail can still GainExp/Arena/Hyper/EndTurn and nested callbacks after this failure; noTarget doesnot mean no later effects or guaranteed noexception.'
],['use','checksfull','b_change','targetresolve','usagefull'],'ordinary PPcommit→late targettest→failureflag→commontail; exact failurepoint controls retainedprefix.')
row(371,[
 'Execution calls BattlerCanChoose with commandPhase=false after selected command may have become disabled/healblocked/gravity/throatchop/choice/taunt/torment/imprison restricted.',
 'Display for execution falsecommand uses ordinary pbDisplay instead of paused selection message; each actual restriction and specialUsage exception remains local.',
 'ChooseMove refusal explicitly sets lastMoveFailedtrue at TryUse; other earlier/later status-refusal branches retain own booleans and are not all uniformfailedtrue.',
 'Normal wrapper clears usehistory as specified, cancels multiturndata and EndTurn; exception or earlier return changes laterprefix, PPnotdeducted for reached frontrefusal.'
],['checksfull','use','battlerfull','choose_callbacks'],'current changedrestriction→nonpaused feedback/refusal→history/cancel/completion, preserving perbranch failureboolean.')
row(372,[
 'Choice lock selection/execution predicate first clears stored ChoiceBand move when actor no longer has that move; mutation happens before activeitem/ability lock refusal.',
 'If move still known, actual activeChoiceitem OR GorillaTactics determines whether choosing a differentmove refuses. Raw recorded identity alone is not sufficient.'
],['checksfull','battlerfull','ability_item'],'storedmove membership→selfclear or active lockgate; no mandatory helditem permanence.')
row(373,[
 'Ordinary use reaching reducer with currentPP0 and totalPP>0 returnsfalse: usedmove then noPP messages, clears lastused/regular identities, failuretrue, cancels/endturn.',
 'Specialusage skips ordinary reducer altogether, so zeroPP alone doesnot cause this branch. Captured skipAccuracy/status checks remain separate.',
 'Reducer treats movePP<0 OR totalPP<=0 as unlimited success without decrement; ordinary positivePP subtracts1 through write-through helper.',
 'External rawchosen0PP can reach branch, while normal selection rejects0 with positivetotal before registration; no claim every noPPmove is normally choosable.'
],['use','b_change','priority','checksfull'],'selection eligibility versusactual reducer→two messages/failure orskip/unlimited; separate ordinaryPP semantics.')
row(374,[
 'Snatch scans positiveeffect smaller than currentminimum100, excluding SkyDrop; selected snatcher clears its effect and clears targetchoice−1 before new user identity.',
 'Original user use/PP/history already committed; originaluser lastMoveFailedtrue when Snatch message stage reached, while actualsnatcher executes remaining move and target pipeline.',
 'New user determines MoldBreaker/targets and actual downstream ability/type/side consumers. Source doesnot debit newusers realPP for this transferred execution.'
],['use','targetresolve','redirect_producers','battlerfull'],'original-useprefix→snatcheridentity/targetreset→messagefailedoriginal→remainingexecution asnewuser.')
row(375,[
 'No-target status/canMagicCoat scan uses speed-only snapshot, opposingliving/nonsemiInvulnerable actors; Coat consumed first or activeBounce with !moldBreaker and !alreadybounced setsrecord.',
 'Reached living reflector path marks originaluserfailuretrue, displaysbounce, checks actual movefailure with reflector as newuser and emptytargets, then calls ProcessMoveHit(move,reflector,[],0,false).',
 'If reflected execution unsuccessful, reflector.lastMoveFailedtrue; successful path doesnot globally reset every previous reflector failureflag in this branch.',
 'Read with explicit step17 new-user contract, summary 对反弹者执行 means reflected invocation associated with that actor; it doesnot require using reflector as target. No candidate from isolated ambiguous shorthand.',
 'Original targetarray stays empty for this no-target path; side/global effects derive newuser. No second ordinary PP debit or universal targetaccuracy invocation implied.'
],['use','priority','checksfull','usagefull'],'emptytargetreflector discovery→originalfailed→reflector-as-user ownfailure/hitcall→conditionalreflectorfailed; complete context disambiguates.')
row(376,[
 'Incremental calculate sees TrickRoom positive-state mismatch, updates snapshot and resorts current cachedtable without redrawtie.',
 'Source move/expiry callers must actually invoke calculation to observe fieldchange; getteralone doesnot poll. EOR MagicRoom source uses cachedspeed getter, not new fullspeed calculation.',
 'Fullcalc is a different explicit call that redraws tie; formal boundary expressly nonfull.'
],['priority','eor','use','attack'],'fieldwrite→reachedincremental snapshotdetect→resort; unchangedcachedtie retained.')
row(377,[
 'Palace autoFightMenu overrides normal chooser, uses own AI category/legal partial selection and can register moveindex−2 with Struggleobject for incapacity; TryUse−2 refuses before ordinaryPP.',
 'Debug commandcode−2 in base menu loop calls DebugMenu then next/retry, distinct from Palace moveindex−2; codefield and moveindex must not be conflated.',
 'Base BattleLoop when @debug&&turnCount>=100 sets decision from on-time method, logs, aborts andbreaks before new commandphase.',
 'Not a universal production100round limit; perturn exceptions/normaldecision can endearlier and no menu/native/probability execution was done.'
],['palace','command','checksfull','startendfull'],'two distinct−2 producers/consumers→specialqualification ordebug retry; independent debugroundlimit.')
row(378,[
 'Actual hyper obedience on inHyper actor returns true for nil/rawShadow move; otherwise globalrand100<20. Full original-entry obedience restrictions still precede it.',
 'UseMove end calls pbHyperMode only when current battle.choice at actorindex action!=None, preventing this oldactor trigger when replacement cleared choice.',
 'Hyper producer additionally rejects fainted/nonShadow/alreadyhyper/nonplayerowned, then ownheartgauge random rule; choiceNone is one guard, not complete qualification.'
],['use','shadowother','checksfull','battlerfull'],'obedience rawtype cutoff versuslater hyperentry producer/currentchoice identity; separate random and state gates.')
row(379,[
 'Clause module aliases relevant basecalls: selfkoclause and modifiedselfdestruct choose draw/winner outcomes at explicit Judge checkpoints.',
 'Selfdestruct failureoverride can reject with display or write decision according exact rules/lastable conditions before inherited movefailure; rules registration alone doesnot guarantee reachedconsumer.',
 'Suddendeath runs after underlying EOR returns and decisionstill0, compares able counts and writes1/2 onlyunequal. Earlier baseEOR prefix can remain even if wrapperchangesresult.',
 'This line forwards full combinedrule consequences; no simulated fullmatch or newhistory issue from registration-point mapping.'
],['clauses','startendfull','use','eor'],'rules keys→explicit alias/checkpoint/failure/EOR consumers→boundeddecision writes; wholecombination outside this summary.')
row(380,[],[], '',layout_reason='Explicit static-only/unrun evidence qualification. It grants no behavior assertion or execution credit; actual present review also ran no random/menu/battle target.')
row(381,[],[], '',layout_reason='Configuration table header defines columns only; not a behavior atom.')
row(382,[
 'Speedchange setting currenttrue derives MECH>=8. Completed itempass and normal peractor moveprocess call incremental when enabled.',
 'Earlydecision item return and process refusal/Shift branches have different exact calls; table summary read with actual stage contract doesnot mean every instruction/attemptalwaysrecalculates.'
],['b_settings','config','attack','use','priority'],'configurationproducer→namedcompletedcaller→incremental consumer, respecting earlyreturns.')
row(383,[
 'Mega setting currenttrue derives MECH>=7; normal reached helper finalcall targets [actorindex] withfullCalcfalse.',
 'Thus own speed/ability movepriority refreshed, tie/brackets retained and global TrickRoom mismatch still can require resort; not isolated fulltable reconstruction.'
],['b_settings','config','other','priority'],'Mega config and finalcaller→singleindexincremental withglobalspace comparison.')
row(384,[
 'CurrentMECH8 makes confusion threshold33 rather than old50 and generation>=8 quash handled once at deferredpass; these separate actual branches supported.',
 'Exact middle label 怪力钳世代分支 requires bounded independent assessment: realgeneration−1/−2 branch belongs KingsShield contactreaction; HYPERCUTTER StatLossImmunity is separate Attack-only handler with no generation read. No newfinding credit before complete candidate/counter.'
],['checksfull','attack','abilityeffects','b_settings','config'],'MECH producer→three claimed consumers; confusion/quash supported, precise middleidentity pending.',support='CANDIDATE_REQUIRES_OTHER_REVIEW',open=['Full candidate including wholeWP40 context/strongest overview-and-cross-contract rebuttal and actual different nonproposer counter required for 怪力钳 label; not autoextend COM001.'])
row(385,[
 'BattleSettings NO_MEGA_EVOLUTION is switchID34; CanMega reads game_switches[34] as its firstguard, true refuses before HasMega/wild/debug.',
 'Table default关 means ordinary fresh/missing switchfalse from GameSwitches getter, not guarantee all loadedprogress has34off. Earlier configuredsave can keeptrue.',
 'Switch identity and getter differ from immediate Booleanconstant; DEBUGshortcut later doesnot override disable switch.'
],['b_settings','other','config'],'switchIDproducer→ordinarymissingfalse/loadedstate→firstCanMega refusal.')
row(386,['Independent literal constants ANYfalse/FOREIGNtrue select actual Owner/level qualified population; they are not automatically derived from generation and not equivalent to allowned/highlevel refuse.'],['b_settings','checksfull','foreign_method'],'configuration two independentvalues→actualforeign/level gate.')
row(387,['Player.badge_count counts ==true progressentries; obedienceL10*(count+1) thenmaxlevel at>=8, affecting highlevel sample gate separately from hyper.'],['playerfull','checksfull','maxlevel_method','maxlevel_constant'],'actual progressgetter→L→sourceinteger gate.')
row(388,[
 'GameData SHADOW type existence AND trainerbattle controls displayedCall grid; actorShadow is not itself menucondition.',
 'Actual Pokemon/battler hyperstate and rawmove type govern obedience extension after execution entry gates; displayedtype existence doesnot automatically make actorhyper.'
],['ui_mainmenu','other','shadowother','checksfull'],'different type registry/menu and individualstate/executor consumers; no conflation.')
row(389,[
 'Constructor snapshots all registeredItem IDs with MegaRing flag; player Bag presence or nonplayerowneritems list determines ringqualification.',
 'Ringname scans same orderedIDs and returns firstpresent registereditem localizedname, otherwise translated MegaRing fallback. Flag inventory changes afterconstructor not automatically rescanned.'
],['battlefull','other','bag','itemdata'],'registeredflag snapshot→ownercontainer membership→qualification/display getter; no compiledload guarantee.')
for n,why in [(390,'Explicit unrun combinations boundary; source-static review can bind named paths but no actual battle/menu combination execution granted.'),(391,'Catalog navigation/count and coverage overview. Complete catalog CM01–33 content was actually read; its individual scenario meanings are decomposed later in their own locators, not closed by this index.'),(392,'Upstream scope/navigation to participant/derived/PP/Bag/items/Player domains; finite actual cross-domain reception remains per named facts, no automaticwhole-domain credit.'),(393,'Downstream scope/navigation to switch/ending/damage/effects/capture/Mega/Shadow/AI. Routing itself doesnot prove each caller/receiver contract.'),(394,'Explicit alternate-facility command scope: only Palace/debug−2 existence coveredhere; complete facility semantic domain not granted by this routing.'),(395,'Explicit full-clause-combination noncoverage; concrete ruleconsumers read separately, no wholematch run.'),(396,'Explicit runtime targetcursor/menu-experience noncoverage. UI finite sourcefacts received but native experience NOT_EXECUTED.'),(398,'Explicit source-static-only qualification; no round/menu/random target executed.')]:row(n,[],[],'',layout_reason=why)
row(397,[
 'Nonplayerowned AIactors bypass playerownership obedience gate. Source-controlPlayer can route a playerowned actor to AI chooser while executor ownership gate still applies.',
 'Parenthetical player-side AI unrun remains accurate evidence boundary; phrase AI席位 is read as normal nonplayer actor, not a blanket exemption based merely on controlflag.'
],['command','checksfull'],'normalAI ownershiproute versusplayercontrolledbyAI; explicit unrunvariant preserved.',open=['All actual AI selection producers/filter paths and runtime interaction remain exactOPEN; no wholeAI legal-choice credit.'])
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_07f.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x.get('children',[])) for x in rows),'layout':sum('layout_reason'in x for x in rows)})
