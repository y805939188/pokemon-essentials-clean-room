import pathlib,json
P=pathlib.Path(__file__).resolve().parent;base=json.loads((P/'manual_batch_06b.json').read_text());d=base['source_dictionary'];rows=[]
d['typefull']={'path':'Data/Scripts/010_Data/002_PBS data/003_Type.rb','range':[1,141],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
d['calculations']={'path':'Data/Scripts/011_Battle/003_Move/003_Move_UsageCalculations.rb','range':[1,515],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
d['three_pbs']={'complete_units':[{'path':'PBS/moves.txt','range':[4107,4117]},{'path':'PBS/moves.txt','range':[5326,5336]},{'path':'PBS/types.txt','range':[47,52]}],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILES_COMPLETE_NAMED_PBS_RECORDS_READ; compiled native load not executed'}
d['unimplemented']={'path':'Data/Scripts/011_Battle/003_Move/004_Move_BaseEffects.rb','range':[10,18],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_CLASS_READ'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(295,[
 'Not-continuing action, current lastMoveFailed Boolean and lastRoundMoved are independent fields/outcomes; nonnil attempt first clears currentfailure before TryUse.',
 'Refused TryUse clears recent records according effective special flag, then Exp/Cancel/End; refusal alone does not unconditionally rewritefailure true.',
 'Branch results below apply earliest actual terminating gate, normal callbacks/no reentry or other failure-write. Later gate existing concurrently does not override earlier terminal branch.'
],['use','checksfull','battlerfull'],'nonnil attempt→clearfailure→ordered earliestgate→outer history/exp/cancel/end; no conflation of action success/completion.')
rows.append({'number':296,'layout_reason':'Two-column table header first terminalgate/currentfailure only; actual behavior in following five complete gate rows, not separate executable assertion.'})
row(297,[
 'Execution pbCanChooseMove?(move,false,true,specialUsage) false causes TryUse lastMoveFailed=true then false.',
 'This first gate precedes SkyDrop/recharge/Palace/skip/status/obedience; ordinary PP not yet deducted. Helper own messages/side effects may precede outer failure write.'
],['checksfull','use'],'current move eligibility→explicittrue failure→refusal tail; existing later recharge cannot replace this true result.')
row(298,[
 'After choose passes, SkyDrop>=0 logs then returnsfalse without lastMoveFailed write; initialfalse remains under no other callback change.',
 'Next HyperBeam>0 logs/displays recharge, toggles Truant ifcurrentlyactive then false with no failurewrite.',
 'Next choice index−2 Palace incapable displays then false with no failurewrite; full Palace register selects−2/struggle marker for no category move.',
 'These all occur before skipAccuracyCheck earlytrue and before PP; their feedback refusal is not equivalent to currentfailure true.'
],['checksfull','use','palace','ability_item'],'first three pre-skip terminalgates afterchoose→false retained→outer cancel/end; actual Palace producer/source distinguished.')
row(299,[
 'Reached status Sleep decrementsstatusCount; ifcount<=0 cures/continues, else displays status and unusableWhenAsleep sets currentfailuretrue and refuses.',
 'Frozen non-selfthaw checks20% cure; failedthaw continuesstatus, sets currentfailuretrue and refuses. Selfthaw move permits later thaw step.',
 'These branches require skipAccuracyCheckfalse and all earlier gates pass; normal special non-Struggle skip reaches none of these status mutations.'
],['checksfull','use','b_change'],'ordered status gate actualstate/callback→explicittrue only refusing path; no ordinary PP yet.')
row(300,[
 'Obedience reached after sleep/frozen, and its false return is used without explicit currentfailurewrite in TryUse.',
 'Obedience passes immediately for multiturn/nonUseMove/noninternal/notplayerowned; otherwise badge threshold/config/foreignness and ShadowHyper random gate determine disobedient.',
 'Disobey active asleep sleepusable move may keep sleeping and false; alternative-move branch false ifnoFightMenu or nootherusable move, else replaces index/move/target and true continues.',
 'Remaining disobey can sleep self, self-confusion-damage or refuse message and false; neither helper call site explicitly sets currentfailuretrue.',
 'Selfdamage mayfaint/item/ability callbacks mutate state, so retained initialfalse vector excludes fatal/other fieldwriters; ordinary confusion caller separately writestrue after same damage helper.',
 'Changing to alternative move and continuing is not a terminal table row; later PP is for replaced actualchoice and later failure gates still apply.'
],['checksfull','use','command','shadowother','b_change','ability_item'],'obedience configured gates→Disobey branch→false retained or replacementtrue; damage helper reuse does not define caller Boolean.')
row(301,[
 'Reached activeTRUANT toggles flag then loaf branch sets failuretrue and false; normal no-loaf passes. Correct ability is TRUANT under existingCOM001.',
 'Flinch feedback and active OnFlinch ability callback precede explicit failuretrue/refusal, so callback exception can stop before fieldwrite.',
 'Ordinary confusion decrementsduration/cures or displays, threshold33current>=7 else50, selfdamage then logs then failuretrue/refuses.',
 'Paralysis25% blocker continuesstatus/log then setsfailuretrue; attraction existingtarget feedback then50% block message/log setsfailuretrue.',
 'All require earlier gates/obediencepass and skipfalse; no simultaneous later condition can redefine an earlier returnedfalse result.'
],['checksfull','use','abilityeffects','ability_item','config'],'status and action blockers explicittrue write location; field may be written after earlier effects/messages.')
row(302,[
 'Disobey selfdamage and ordinary confusion share damage helper but only ordinary caller explicitly setsfailuretrue; damage amount or message does not prove Boolean.',
 'Recharge effect HyperBeam is distinct from REST healing move; earlier eligibility refusaltrue dominates concurrent recharge/SkyDrop state.',
 'Refusal precedes PP; recent move/type alwaysclear, regularhistory only !effective specialUsage. Ordinary entry continuation can rewrite specialtrue before cleanup.',
 'CancelMoves does not clear HyperBeam and retains currentMove while rechargepositive; its full_cancel parameter only changes final-Outrage confusion gate among listed logic.',
 'Arena after normal baseEOR and count>=3 calls both battlers CancelMoves(true); judging later HP/faint/replacement is separate. Surviving un-replaced actor with rechargepositive can still face next-turn rechargegate.',
 'No claim generic winner isalwaysrecharging; counter decrements, prior outcomes and participant replacement must be bound to reached exact state.'
],['use','checksfull','successstate','eor','b_change','battlerfull'],'caller-specificfailure→conditionalhistory→cancel preservingrecharge→Arena same complete cancel→next reached precheck; no heal/REST conflation.')
row(303,[
 'Only full EOR reaching final liveallBattlers loop copies current lastMoveFailed to lastRoundMoveFailed; faint/exited/notreachedtail cases excluded.',
 'Same living member recharge1 stopsaction with currentfailurefalse and noextraPP; reached fullEOR decrementsHyperBeam1→0 then copiesfalse.',
 'Default StompingTantrum PBS power75/class DoublePowerIfUserLastMoveFailed multipliesbase by2 only lastRoundMoveFailedtruthy, so false75/true150 conditionalbase contrast.',
 'Eligibility refusaltrue and same fulltail yields true→base150; damage output also has stats/type/items/variance/rounding and cannot equal inferred finalHP75/150.',
 'Source-static vectors require unchanged relevant identity and noextra failure/status/history writers, normal callbacks and no earlyfinaloutcome.'
],['use','checksfull','eor','stomping','three_pbs','calculations'],'earliest failurefield→fullEOR live membership/copy→next move base callback; no rawfield snapshot mistaken for universal future outcome.')
row(304,[
 'Metronome update occurs after initialprechecks/basePP, actualtype/usagecounter callback, before recentidentity overwritten.',
 'Requires activeMETRONOME and !callsAnotherMove; retained same lastMoveUsed and current failurefalse increments elsecount0.',
 'Normal attempt already clears currentfailurefalse before precheck; immune/miss previous attempt can retain identity so prior finalsuccess is not tested at this update.',
 'Counter reading damage callback multiplies final_damage_multiplier by1+0.2*min(count,5); writer counter itself can grow beyond5.'
],['use','item','ability_item','calculations'],'newattemptgate→retained priorID/current attemptflag→counterwrite→item damage multiplier read. Activation and concrete type callback constraints preserved.')
row(305,[
 'Early precheck/NoPP return skips Metronome update and clears recentidentity; subsequent reached update can then reset due absentidentity.',
 'Different noncalling move at reached point resetscounter0; inactiveitem/calling shell skip doesnot reset storedcount.',
 'An inner calledmove may independently reach update using shared battler identity/counters; no blanket calls alwaysskip every layer.',
 'CancelMoves has no Metronome clear; normal InitEffects setsMetronome0 on switching initializer. Count lifetime follows actual initialization, not direct multiplier cap.',
 'Formula min(count,5) limits only contribution and final damage laterrounding/other multipliers remain independent.'
],['use','b_init','item','calculations','movebase'],'skip/reset/increment distinct writers→switch initializerreset→clippedconsumerread; no universal perturn clear.')
row(306,[
 'Conditional ordinary same living activeMETRONOME user, count0, recentIDnil/nonTackle; normalTACKLE qualification/PP pass reachesupdate sets0 thenrecordsTACKLE.',
 'Default TACKLE PBS Normal physical None-function uses actual factoryfallbackUnimplemented damaging path, not a custom effect; Ghost PBS immunitiesNormal/Fighting yields type0 absent RingTarget/Scrappy/Foresight/type rewrite etc.',
 'Target no protection and other immunity-removal excluded: firsttargetcheck flagsunaffected, firsthit noaffected returnsfalse, outer markscurrentfailuretrue but retainslastMoveUsedTACKLE.',
 'Next normal opponent replacement to hittable nonGhost, same user/no reentry and secondordinaryTACKLE front/PPpass reachesupdate; currentfailure alreadyfalse, retainedsameID count0→1.',
 'Reached active item damage multiplier contributes1.2 at final multiplier layer; previous success with same retainedID likewise0→1.',
 'This is not a promised exact1.2 ratio of finalHP loss; variantHP/stats/stages/critical/type/variance/rounding/capping and activeitem gates still apply.'
],['use','checksfull','typefull','calculations','three_pbs','unimplemented','movebase','item','b_init','switching'],'registered defaultdata→firstimmune attempt retainsID despitefailure→normalreplacement→secondattempt clearscurrentfailure beforeupdate→sameID increment→1.2 contribution.',premise='Fixed default ordinary valid registered source-described data; no dynamic/plugin override, reentry, user switch/faint, item suppression, IonDeluge/Electrify/type-converter, RingTarget/Scrappy/Foresight or other immunity override; callbacks/messages normal. Conditional source vector, compiled/native execution not claimed.')
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_06c.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n');print({'rows':len(rows),'children':sum(len(x.get('children',[])) for x in rows)})
