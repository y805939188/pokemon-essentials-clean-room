import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11m.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
N='Complete N/E fixture: legal default real NATURALGIFT slot, ordinary1v1/no variant/override/plugin, nonTransform U, actual/real PP5, no extraPressure, decision0 and U unmoved. U active ORANBERRY, totalHP160/current81, activePARENTALBOND (legally established state, not executed acquisition), both stages0/currentgeneration and physical positive ordinary first damage delta; targetT initialHP>delta, activeJABOCABERRY and both able/eatable as specified. U takesIndirectDamage/canHeal/canEatBerry, initial C/I bothORAN and R/P initiallynil/Belchfalse. Exclude Snatch/reflection/suppression/protection/Substitute/Disguise/IceFace/miss/typeimmunity/sleepfreeze interruption/switch/Unnerve eating block/HealBlock/Symbiosis/Ripen/CheekPouch/otherhandlers/reentry/extraerrors. Both pre-use eligibility/obedience checks pass. Each fresh effective priority putsU beforeT, with no competingMoveNext/Quash/TrickRoom/speed/choice/multiturn/externalchanges. All logging/formatting/message/Input/refresh/flush diagnostics, subsequent Judge/recalc and second cleanup normallyreturn. No IonDeluge/Electrify/other typeoverride except the specifically independent ERR09. Observation beforeT action; actual firstdamage delta remains symbolic, not executed numeric damage.'
row(984,[
 'ERR shared fixtureE completely retains N user/target ability/item/eating/positive-hit/survival/exclusion conditions, rather than treating mere NaturalGift+ParentalBond as sufficient.',
 'U is ordinary1v1 real-slot nonTransform with actual/realPP5, no extraPressure, decision0 and not yet moved.',
 'U has activeORAN, H160/h81, activeParentalBond; T has activeeatableJABO and initialHP greater than the actual positive first delta; all earlier eligibility/obedience and ordinary targeting pass.',
 'U can take indirect damage/heal/eat, C/I initiallysameORAN, Recycle/Pickupnil and Belchfalse; exact suppressed/reflect/protect/substitute/absorption/miss/status/switch/eating/reaction exceptions are excluded.',
 'Every fresh effective priority still putsU beforeT with no competing scheduling/state/choice/type override; the observation occurs beforeT acts.',
 'All diagnostic logging/formatting/message/input/refresh/flush plus subsequent judge/recalculation/second cleanup normally return, supplying a strict continuation premise rather than host reliability observation.',
 'ParentalBond is a lawful already-established state, not an assertion a SkillSwap acquisition sequence was run.',
 'First actual damage delta is positive but symbolic; no complete numeric damage fixture or simulated target/game execution is claimed.'
],['ng_specific_formal','ng_pbs','natural_gift','use','usagefull','calculations','checksfull','item','ability_item','attack','pbdebug','errors'],'complete N reactionfixture + strict E scheduler/diagnostic continuation premises -> finite static next-attempt trace.',premise=N,support='SUPPORTED_BOUNDED_SCOPE_QUALIFICATION')
rows.append(dict(number=985,layout_reason='ERR table column heading only.'))
row(986,[
 'ERR01 first ordinary attempt passes TryUseMove and spends actual/realPP5to4 before type/records/damage.',
 'Active ORAN supplies Poison base type and NaturalGift power80; the positive first target damage delta and its ordinary records are committed.',
 'T JABO physical response requests floor(Utotal160/8)=20, writes U81to61 and consumes T JABO through its normal held-item trigger.',
 'The making-hit caller then immediately checks U HP item because userHP fell;61<=80 admits ordinary ORAN recovery10 to71.',
 'ORAN consumption writes Cnil through bound Pokemon, clears matching initialI, sets RecycleORAN/PickupORAN with sequence and Belchtrue; no Symbiosis refills it underN.',
 'First hit completes successfully with both alive, so real hit count1 reaches the planned second hit; NaturalGift BaseDamage dereferences missing user.item.id before item-data lookup/default1/seconddamage and before end-use consumption.',
 'The local NoMethodError is StandardError caught by pbProcessTurn inner logonerr under E; no transaction restores firstPP/records/damage/HP71/item history.',
 'Because that first fault happened before normal EndTurn acted marker, user remains unmoved; after diagnostics return, Judge0/recalculation and ProcessTurn true restart the outer attack scan.',
 'Fresh priority still lists U first and its stored UseMove choice remains, so a whole new ordinary use passes prerequisites and spendsPP4to3.',
 'With Cnil, fresh base type returnsNormal and updates records; the whole-use no-berry gate now fails normally, completing failure cleanup/EndTurn and marking U moved.',
 'T receives no second new damage; later scans filter movedU and reach the finite following action rather than relying on the100-round abort limit.',
 'Committed Recycle/Pickup/Belch remain after the retry normal failure unless a named later writer acts; no native/game run is inferred.'
],['natural_gift','ng_specific_formal','ng_pbs','use','usagefull','calculations','checksfull','item','ability_item','hit_triggers','b_change','battlerfull','attack','priority','start_end_full','pbdebug','errors'],'PP5to4 -> targetdelta/JABO20/U61 -> ORAN10/U71+C/Inil/RPBelch -> secondhit nil.idfault beforeEndTurn -> caught -> re-scanU -> PP4to3/Normal/noBerryfail -> acted/filter.',premise=N)
row(987,[
 'ERR02 independently removes active ParentalBond while retaining all other N/E first-hit reaction and normal callback conditions.',
 'The move plans only its ordinary single hit, spendingPP5to4 once.',
 'That hit still gives delta/JABO20/ORAN10 to U71 and commits the stated item/history prefix.',
 'There is no planned second BaseDamage dereference after the self-consumption, so no same missing-item second-hit exception.',
 'Normal end-use sees itemnil and skips its guarded consumption, then reaches normal acted marking without this scheduling retry.'
],['natural_gift','use','usagefull','item','ability_item','hit_triggers','attack'],'no activeParentalBond -> singlehit firstprefix -> end guardednilskip/normalacted -> no samefault/retry.',premise=N+' Independent change: remove activeParentalBond.')
row(988,[
 'ERR03 changes only initial actual/realPP from5 to1.',
 'The first attempted use consumes1to0 and reaches the same committed first-hit/item/HP prefix and later second-hit fault.',
 'Under the same successful diagnostics/scheduler continuation it can be attempted again as unmovedU.',
 'That retry fails the ordinary PP reduction gate with PP0, does not decrement below0 and completes normal noPP failure cleanup/acted marking.',
 'FinalPP0 replaces ERR01PP3; the earlier targetdelta/U71/consumption prefix is not rolled back or repeated by a successful second hit.'
],['use','b_change','natural_gift','item','ability_item','attack','pbdebug'],'initial1 -> first0/samefault -> caught reattempt -> noPP0/no furtherdecrement -> normalacted.',premise=N+' Independent change: initial PP1.')
row(989,[
 'ERR04 directly invokes the same ordinary pbUseMove fault through an actual caller with no additional catch, rather than pbProcessTurn logonerr.',
 'The same first hit/item/PP prefix can commit before the missing-item NoMethodError.',
 'The local use method has no self-contained rescue/retry, so the error propagates to that actual bare caller.',
 'It does not itself create the attack-phase outer-loop same-round reselection shown in ERR01.',
 'Any higher caller rescue/state changes are separately scoped; this local propagation does not imply process exit or rollback.'
],['use','natural_gift','item','ability_item','hit_triggers','pbdebug','errors'],'bare actualcaller -> same innerfault propagates; no local scheduler retry/rollback/hostexit guarantee.',premise=N+' Independent caller: bare ordinaryuse without extra catch.')
row(990,[
 'ERR05 independently allows diagnostic code itself to fail, a non-StandardError exception, or an exception outside the local wrapped pbUseMove block.',
 'Bare rescue inside logonerr catches StandardError from its yield; it does not guarantee completion of logging/format/backtrace/PrintException/flush if those operations fail.',
 'A nonmatching exception or outside-block error need not return through that inner wrapper.',
 'Therefore ERR01 continuation, fresh PP3, local cleanup and finite normal next scan are not guaranteed under these changed premises.',
 'No failed diagnostic implies earlier PP/HP/item writes were reverted, nor establishes host exit/recovery or whole battle cleanup.'
],['pbdebug','errors','use','attack','battle_loop_complete'],'changed exception location/type/diagnosticfailure -> catch/return premise may fail -> only reachedprefix, no PP3/host guarantee.',premise=N+' Independent changed error type/site or diagnostic failure.')
row(991,[
 'ERR06 places an error after the original use has already normally written its acted round, in later continual-ability/Instruct/Dancer handling.',
 'A diagnostic catch alone does not erase that already committed marker.',
 'The next attack scan tests actual current movedThisRound, choice, liveness, priority and decision rather than replaying every caught action.',
 'Nested Instruct/Dancer calls additionally save/restore their own lastRoundMoved under exact normal-return branches, so those markers must be judged at the actual nesting boundary.',
 'It is invalid to infer the original choice automatically executes again solely from catch success; failed nested restoration/positive decision remains a separate prefix condition.'
],['use','attack','battlerfull','priority','pbdebug','instruct'],'postacted fault -> catch doesnotunmark -> actual current/nestedrestored scheduling filters -> no automatic originalreplay.',premise=N+' Independent error after original normal acted marker.')
row(992,[
 'ERR07 adds active Torment and Instructedfalse with a different first prior lastMoveUsed, so the first ordinary eligibility check still passes.',
 'The first NaturalGift attempt records its own identity before the same later fault, spendingPP5to4 and committing the first-hit prefix.',
 'On reselection the ordinary CanChooseMove Torment guard sees lastMoveUsed==NaturalGift, !Instructed and !specialUsage and rejects before PP subtraction.',
 'This retry therefore leavesPP4, clears ordinary recent/regular records through its failure path and normally marks acted.',
 'The control disproves an unconditional second PP decrement for all caught/reselected states; exact later eligibility remains required.'
],['checksfull','use','attack','pbdebug','natural_gift'],'firstTormentallowed/priorother -> recordNaturalGift/faultPP4 -> retry sameid Tormentreject beforePP ->4/acted.',premise=N+' Independent activeTorment/nonInstructed; first recent identitydifferent.')
row(993,[
 'ERR08 independently changes after-fault decision to positive, current user fainted, choice type/clearing/position or effective priority order.',
 'Attack moves checks positive decision after processing, and each fresh loop reads current priority and filters fainted/nonUseMove-or-Shift/moved members.',
 'Actual switch/position/choice modifications can therefore remove or reorder the previously attempted user.',
 'U-before-T and PP3 are no longer guaranteed once their exact E premises are changed.',
 'Conversely the generic outer rescan does not permanently pop an attempted user merely because a prior call was tried; it relies on current state/markers.'
],['attack','use','priority','swap','command','b_change','pbdebug'],'changed reached state -> decision/filter/order re-evaluation -> conditional nextactor, no permanent attemptedqueue removal.',premise=N+' Independent afterfault decision/liveness/choice/index/priority change.')
row(994,[
 'ERR09 independently enables IonDeluge with registered Electric type, no Electrify/other override and unchanged positive firstPoison damage/reaction premises.',
 'The first ORAN-derived base typePoison is notNormal, so IonDeluge does not change that first type or its required first-hit prefix.',
 'After consumed-item fault and successful retry continuation, the missing-item base type returnsNormal.',
 'Common CalcType sees IonDeluge and converts thatNormal toElectric before recording lastMoveUsedType.',
 'The later no-berry whole-use failure still follows, so retry record type isElectric rather than guaranteedNormal merely because item is empty.',
 'Other prior PP/HP/history/item writes remain committed; enabling type conversion is not a reset/rollback or executed damage assertion.'
],['natural_gift','calculations','use','attack','item','ability_item','typefull','sport_ion_producers'],'firstPoison unaffected -> selfconsume/fault -> retry baseNormal -> IonDeluge Electric record -> noBerryfail; prefixes retained.',premise=N+' Independent IonDeluge true/ELECTRIC registered, no other typeoverride; firstPoison premise intact.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11n.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
