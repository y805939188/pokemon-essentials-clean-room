import pathlib,json
P=pathlib.Path(__file__).resolve().parent;base=json.loads((P/'manual_batch_06c.json').read_text());d=base['source_dictionary'];rows=[]
d['errors']={'path':'Data/Scripts/001_Technical/001_Debugging/003_Errors.rb','range':[1,94],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
d['natural_gift']={'path':'Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb','range':[1338,1380],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_CLASS_READ'}
d['ng_pbs']={'payload':'natural-gift-complete-pbs-records.json','actual_reader':'/root/core_atomic_reception','reading':'Three complete PBS record contents and parent bytes/SHA actually read, not native compiled load'}
d['ng_specific_formal']={'path':'deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md','range':[76,92],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_RELEVANT_SUBSECTION_READ; no wholeWP47 credit'}
d['hit_triggers']={'path':'Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb','range':[1,218],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(307,[
 'Ordinary selected process calls logonerr around pbUseMove; this inner wrapper is itself inside outer attack-phase logonerr in base BattleLoop.',
 'Bare rescue catches ordinary StandardError, logs error/backtrace, calls pbPrintException and flush; no explicit rethrow after normal diagnostics.',
 'DEBUG/INTERNAL only gate log buffers/optional debuglog write; pbPrintException formats version/error/backtrace, appends errorlog, nativeprint and uptime/Input/clipboard loop irrespective log enabled.',
 'If all diagnostics return, process still Judge, optional speed recalc and true advance even if move failed by exception before completion.',
 'Neither wrapper writes missing lastRoundMoved. EndTurn normally writes that field before Choice/continual-ability followups, so error location before/after fieldwrite matters.',
 'Diagnostic formatting/disk/print/time/Input/clipboard can themselves fail; ordinary rescue outcome is conditional, not guarantee native resume or exit.'
],['use','attack','startendfull','debuglog','errors'],'inner effecterror→ordered diagnostics→conditional normalreturn→Judge/recalc/advance; no implicit action completion/rollback.')
row(308,[
 'Advance restarts scheduler with fresh pbPriority; stored table retains actors including alreadyattempted entries, filters moved flag/current choice/liveness perpass.',
 'ForcedNext then regularnonQuash then generationquashed all require live and UseMove/Shift and lastRoundMoved!=current; source pergroup flags still apply.',
 'Error before movedwrite with decision0, retainedchoice and livingactor may therefore satisfy selection again; none of these facts alone guarantee repeat.',
 'Reselection invokes whole ordinary pbProcessTurn/pbUseMove again, repeats qualification/obedience and normal PP gate, not continuation at interrupted secondhit.',
 'If precheck refuses or noPP, no extra base PP; if ordinary precheckpasses with positivePP can deduct again. An exception alone does not imply every repeat losesPP.'
],['attack','use','battlerfull','checksfull','b_change','priority'],'diagnosticadvance→freshfilters→whole actionentry→conditional PP; no fixed resume point or universal retry theorem.')
row(309,[
 'NG01 common vector is normal1v1, current-generation default NATURALGIFT real slot, nonTransform user notmoved, matching real/battle PP5, decision0, noextraPressure.',
 'Actual valid current held ORAN NaturalGift_POISON_80 and activeParentalBond, H160/h81; target activeJaboca, firstpositivephysicaldamage and bothsurvive; eating/heal allowed.',
 'All explicit noSuppression/noSnatch/bounce/protection/substitute/disguise/iceface/miss/immunity/status/switch/Unnerve/HealBlock/Symbiosis/Ripen/CheekPouch/reentry gates retained from complete WP47 common premises.',
 'Both attempts frontqualification/obedience pass; each fresh priority UbeforeT, no forcednext/quash/TrickRoom/speed/choice/multiturn/type override; diagnostics/Judge/recalc/secondfailedEndTurn return normally.',
 'These stipulations describe legal reached source state and conditional random/HP branch, not executed acquisition of ability or exact full damage formula.'
],['ng_specific_formal','ng_pbs','natural_gift','use','attack','priority','calculations','checksfull'],'complete existing vector premises jointly bind firstdamage+itemconsume+secondbaseerror+repeat scheduler; no partial premise adoption.')
row(310,[
 'First ordinary PP5→4 writes both real/battle when realMove matches/noTransform; typePoison and base80 obtained while currentORAN exists.',
 'Positive first physical targethit commits damage record, then active target OnBeingHit Jaboca requires berrycanconsume/physical/userindirect; H160/8 requests20, user81→61 and targetJaboca consume.',
 'OnBeingHit caller immediately checks userHPitem when HPdropped. ORAN canHeal/pinch(false),61<=80, heals10→71 then normalHeldItemTriggered consumes userORAN.',
 'Consume writes recycle/PickupID/useindex, Belch forberry, clears initialItem only when sameORAN, clears actualheld item with Pokemon write-through; no Bag quantity change. Symbiosis and other extra changes excluded.',
 'Base parent plans2; firsthit returnsnormal and bothalive, so realcount1 then secondhit enters ordinary calculation. Current user.item nil→pbBaseDamage user.item.id raises before data lookup/default1 and before secondhit HP commit.',
 'Firsthit damage/PP/history/71HP/current-initial/recycle/Pickup/Belch prefix remains; error occurs before original EndTurn and end-of-use itemguard consumption.',
 'Normal diagnostics then Judge0/recalc+advance, freshU-first selection stilleligible; second ordinary entry resets currentfailure, PP4→3 and recalculates generaltype/history.',
 'Now safe whole-use NaturalGift gate sees nilitem, reportsfailure then CancelMoves/EndTurn writes lastRoundMoved; no secondattempt hit/targetdamage.',
 'At before T acts, real/battlePP3,U71 and prior consumptionprefix retained. Subsequent U filtered by moved flag; finite later processing can finish phase under stipulated normal otheractions.',
 'Finite termination rests second normal whole-use failure and completionfield, not debug100-round limit; no game/diagnostic/native run asserted.'
],['ng_specific_formal','ng_pbs','natural_gift','use','calculations','attack','priority','hit_triggers','item','ability_item','b_change','battlerfull','debuglog','errors'],'first PP/hit→Jaboca→immediateORANconsume→secondbase nilerror→conditionaldiagnosticreturn→whole ordinaryretry→safe ownfailure+EndTurn; preserve exact first committedprefix.',persistence='Actualheld setter writes partyPokemon; initial/recycle/Pickup/Belch battle arrays distinct. No successful Save/reload/host execution inferred; source-state prefix only.')
row(311,[
 'Only initialPP1 variation: first1→0, reattempt prechecks pass but reducerfalse0 nofurtherdeduct, noPP messages/failure/cancel/EndTurn writesmoved.',
 'Removing activeParentalBond plansonehit: PP5→4/U71 ordinarycomplete/no secondbasequery; end-of-use currentnilguard skipsduplicateconsume.',
 'Secondattempt executioneligibility refusal prevents seconddeduction, outer rejectionnormalEndTurn stillwritesmoved.',
 'Error after completionwrite/decisionpositive/faint/choiceclear-or-retarget/swap requires freshactualfilter analysis; no automatic repeat from wrappercatch.',
 'Bare ordinary pbUseMove without this processwrapper propagates to realcaller; no automatic scheduling retry. Instruct/Dancer own saved/restored flags and nested wrappers differ.',
 'Diagnosticerror/nonStandardError/outsidewrapper error canreach outerboundary; no guarantee PP3/cleanup/exit/recovery/globaltermination for arbitrary exceptions.',
 'All cases conditional static designs NOT_EXECUTED; existing correct formal histories remain preserved and no new candidate.'
],['use','attack','checksfull','natural_gift','ability_item','b_change','debuglog','errors'],'single controlledvariation→actual nextgate/actioncompletion→preciseprefix; no broad error-recovery contract.')
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_07a.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n');print({'rows':len(rows),'children':sum(len(x['children']) for x in rows)})
