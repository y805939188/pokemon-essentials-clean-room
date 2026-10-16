import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11l.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(965,[
 'The FH/MET/RANK/ERR suite declares DERIVED_VECTOR and executionNOT_EXECUTED.',
 'Front-refusal vectors assume a valid nonempty move entered, unchanged original choice, normally returning callbacks and only the named earliest rejecting gate.',
 'Tail/Stomping controls additionally require the same member alive at the complete silent EOR tail and no later last-failure rewrite.',
 '75/150 denote StompingTantrum base power under its lastRoundMoveFailed check, not fixed final damage.',
 'No early result, formal faint/replacement, uncompleted tail or special-call record-clear exception can be silently excluded outside the stated case conditions.'
],['use','checksfull','eor','stomping','b_init'],'declared successful-read/static premises -> exact firstfailure/currenthistory -> reachedtail copy -> conditional base75/150.',support='SUPPORTED_BOUNDED_SCOPE_QUALIFICATION')
rows.append(dict(number=966,layout_reason='R5 FH/MET/RANK table column heading only.'))
row(967,[
 'FH01 starts an ordinary move call with active valid multi-turn continuation and HyperBeam1, original PP5 and earlier selection eligibility passing.',
 'skipAccuracyCheck is computed from original specialUsage before continuation overwrites choice move and changes specialUsage=true; the stated original ordinary call therefore keeps skipfalse.',
 'pbUseMove sets current lastMoveFailed=false, then TryUseMove rejects recharge without setting it true.',
 'Failure clears lastMoveUsed/type but because specialUsage is nowtrue retains lastRegularMoveUsed/Target.',
 'PP reduction was not reached, so the real slot stays5; CancelMoves clears ordinary multi-turn counters while deliberately not clearing HyperBeam1.',
 'Normal EndTurn marks acted; if the same live member reaches full EOR tail, HyperBeam1 decrements0 and lastRoundMoveFailed copiesfalse.',
 'With no intervening failure rewrite, next Stomping base remains75 rather than150; these tail consequences require the explicit alive/full-tail premises.'
],['use','checksfull','b_change','eor','stomping','battlerfull'],'originalskipfalse -> continuation specialtrue -> failedfalse/recharge refusal -> noPP/retainregular -> cancel notHyperBeam -> normaltail0/copyfalse/base75.')
row(968,[
 'FH02 has no multi-turn override, ordinary use, HealBlock-positive healing move and PP5, with that execution eligibility gate rejecting first.',
 'TryUseMove writes lastMoveFailed=true for the failed CanChooseMove predicate before returning.',
 'No PP stage is reached; ordinary failure clears both recent-use and regular-move/target record groups.',
 'Reaching the full live-member EOR tail copiestrue into lastRoundMoveFailed.',
 'After removing the restriction with no other rewrite, Stomping base becomes150.',
 'Concurrent recharge/SkyDrop does not replace this provenance because CanChooseMove is earlier than those action gates.'
],['checksfull','use','eor','stomping','b_change'],'first HealBlock choose-refusal true -> noPP -> live tail copytrue -> later base150; later gates unreached.')
row(969,[
 'FH03 independently supplies first-action rejection by SkyDrop or Palace choice slot-2 after CanChooseMove passes.',
 'Each gate returns false without setting the freshly reset lastMoveFailed=true.',
 'The attempt therefore does not subtractPP but can normally reach failure cleanup/EndTurn and be marked acted.',
 'Acted this round and current failureBoolean are distinct; these cases do not justify every inability to act settingtrue.',
 'An earlier eligibility failure would instead take FH02 provenance and is excluded by the stated first-gate control.'
],['checksfull','use','palace','b_change'],'CanChoose passes -> first SkyDrop/Palace return false withouttrue -> noPP +normal actedmarker.')
row(970,[
 'FH04 fixes actual disobedience self-damage with user surviving, or independently nap, usable-asleep continued sleeping, no selectable alternative, or refusal message.',
 'The named disobedience branches terminate with false but do not write current lastMoveFailed=true at their call sites.',
 'Thus the resetfalse can remain even though the attempt stops; actual sleep or HP self-damage prefixes already occurred where selected.',
 'NoPP/failure record clearing/normal EndTurn follow the reached ordinary path, without reversing those prefixes.',
 'Disobedience that selects another move and returns true continues ordinary use and is explicitly outside this terminating group.'
],['checksfull','use','statuses_full','b_change'],'disobey named terminating branch -> no explicitfailedtrue -> preserve reachedsleep/HP -> failuretail, not successful replacement-move branch.')
row(971,[
 'FH05 instead fixes ordinary applied Confusion self-hit with user still alive and previous eligibility/obedience passing.',
 'The ordinary confusion action gate calls self-damage then explicitly sets lastMoveFailed=true before returningfalse.',
 'This differs from the disobedience self-hit call site despite shared damage helper/message similarities.',
 'Other explicit true-writing ordinary action rejections are still-asleep with nonusable move, frozen-not-thawed, Truant loaf, Flinch, full paralysis and attraction block.',
 'Those conditions retain their own ordering/random/activeability guards; the list does not say every member simultaneously encounters them or that a prior false writer becomes true by naming alone.'
],['checksfull','use','statuses_full','b_change'],'ordinary Confusion HPprefix -> explicitfailedtrue; distinct exact true-writer action gates.')
row(972,[
 'FH06 independently makes the member formally faint before the EOR tail, or causes EOR early return/unreached tail.',
 'allBattlers tail filters/current execution then do not guarantee copying its current failure into lastRoundMoveFailed.',
 'Formal initialization/replacement can reset failure history separately, so FH01/FH02 next75/150 cannot be promised under those changed premises.',
 'The CM30 special eligibility-refusal control clears lastMoveUsed/type but preserves regular-move/target records; ordinary refusal clears both groups.',
 'An invoked diagnostic or a completed local failed attempt alone does not establish the later live full-tail prerequisite.'
],['use','checksfull','b_change','b_init','eor','stomping'],'changed faint/earlyexit -> no guaranteedtailcopy/base; special/ordinary record-clear guard retained.')
row(973,[
 'MET01 starts activeMetronome counter0 and lastMoveUsed nil/other thanTackle, ordinary Tackle to a Ghost with no immunity bypass, valid pre-use/PP, same surviving user and normal later opponent replacement to nonGhost.',
 'First attempt resets current failurefalse; at the Metronome update point differing/nil prior identity sets counter0, then recordsTackle.',
 'Later type immunity sets the ordinary failure outcome, leaving recordedTackle and counter0.',
 'On the next same-move attempt the new current failure is resetfalse before Metronome compares lastMoveUsed==Tackle, so it increments0to1 despite the earlier attempt having failed.',
 'The active item damage handler reads1+0.2*min(counter,5), contributing1.2 to final_damage_multiplier.',
 'Other rounding/critical/type/defense/multiplier changes mean this is not a guaranteed observed1.2 total HP-damage ratio.'
],['use','checksfull','item','calculations','b_init','battlerfull','typefull'],'first identitydifferent counter0 -> laterimmune/recordTackle -> next resetfailedfalse/sameid -> counter1 -> Fmult1.2.')
row(974,[
 'MET02 keeps MET01 initial nil/different recent identity but changes only the first attempt to a normal success.',
 'Its first update still leaves counter0 because prior identity differed, then recordsTackle.',
 'Next same identity reaches the same reset-current-failure comparison and increments0to1, matching the failed-first control at this update point.',
 'Independent changing the next arrived move to another noncalling identity resets counter0 instead.',
 'The stored counter follows reached update/identity timing, not a simple previous whole-move-success streak assumption.'
],['use','item','calculations'],'initial identitydifference -> first0 regardlesslater success -> nextsame1/different0 at update point.')
row(975,[
 'MET03 begins with stored counter2 but a pre-use rejection or noPP rejection before the Metronome update block.',
 'That early-return attempt does not execute a counter update, so counter2 remains there while recent move identity is cleared by its failure branch.',
 'When a later ordinary same-named move genuinely reaches the update block, nil recent identity causes counter0.',
 'The reset therefore happens at that later update, not automatically at the earlier refusal itself.',
 'MissingPP/control and ordinary/special record rules remain distinct actual gates, not proof all nested calls clear the same fields.'
],['use','checksfull','b_change','item'],'earlybeforeupdate -> counter2unchanged/recentnil -> laterarrival nilcomparison ->counter0.')
row(976,[
 'MET04 independently makes the held Metronome inactive at the update point, leaving stored counter2 unchanged by that guarded block.',
 'Another control keeps the item active but uses a callsAnotherMove shell; the outer block again does not update.',
 'A normally reached inner noncalling use with its own activeitem/identity conditions can update independently.',
 'Skipping the outer calling shell therefore does not prove the entire nested action leaves the counter unchanged.',
 'No callback execution or family-wide nested-call eligibility is inferred beyond the exact guard/body.'
],['use','item','movebase','usagefull','battlerfull'],'!activeitem OR calling shell -> skiplocalupdate; reached eligibleinner can ownupdate.')
row(977,[
 'MET05 independent ordinary replacement initializes stored Metronome counter0.',
 'The same-move positive-control update can increment stored5to6; the update writer does not cap it5.',
 'Only the item damage reader uses min(counter,5), so stored6 contributes capped factor2.',
 'A read multiplier cap must not be represented as a storage cap, and an early skipped update need not increment or reset anything.'
],['b_init','use','item'],'replacementInit0; sameid update5to6; reader min6,5 ->factor2 only.')
row(978,[
 'RANK01 fixes legal ordinary trainer triple/noPartner: one player owner with3 able, opponentA/B each2 healthy nonEgg, mergedA0/A1/B0/B1 with starts0/2.',
 'The side owner mapping requiresA two active slots andB one, satisfying the available-team validation.',
 'Setup uses a global battlerNumber across trainers, puttingA0/A1 in enemy1/3 andB0 in5.',
 'ForB0 partyindex2, idxOther=startsB2+globalbattlerNumber2=4, beyond the original four-element order array.',
 'Swapping index2 with4 produces order[0,1,nil,3,2] while the actual merged Pokemon party still contains only4 members.',
 'The extra nil/order slot is not a fifth participant, and this legal static authored trainer fixture does not certify every multiowner layout or a Demo run.'
],['ensure','startendfull','owners','teams','constructor','b_init'],'validrequiredA2/B1 -> globalbattlerNumber2 forB -> orderidx2/4 swap ->[0,1,nil,3,2], party4.')
row(979,[
 'RANK02 keeps that damaged order and legally registers healthyB0 replacing with nonactive healthyB1 whose stored abilityILLUSION, noactiveGas/randomreplacement/trap/duplicate/PursuitKO/interference, normal earlier presentation.',
 'Executor first recalls and runs outgoing ability/Peer handling, whose raw battle-copy HP0/fainted prefix does not make persistentB0 unable.',
 'MessagesOnReplace sees candidateB1 Illusion and calls LastInTeam before actual pbReplace binding/order swap.',
 'LastInTeam enumerates still-persistently-ableB0(index2) thenB1(index3), attempting numeric order3>nil.',
 'That comparison fails before B1 binding and before the new order swap; earlier recall/leave/temporary-faint prefixes remain.',
 'Outer diagnostics do not restore the resident snapshot or establish later entry/cleanup completion, and normal registration is not proof replacement succeeded.'
],['attack','switching','ability_item','peer','battlefull','b_init','pbdebug'],'registeredswitch -> recall/leave rawcopyfaint -> candidateIllusion LastInTeam B0/B1 ->3>nil failure -> no bind/order commit.')
row(980,[
 'RANK03 independently changes the original2+2 opponent fixture to double side size2.',
 'Setup gives each owner one initial slot and theB start/global-number target swap uses existing order indices2/3.',
 'The resulting order[0,1,3,2] is nonnatural but has no same missing-rank comparison from the triple2+2 case.',
 'This control avoids that particular nil defect rather than proving all subsequent multiowner consumers correct.'
],['ensure','startendfull','owners','battlefull'],'double owneroneeach -> swap2/3 ->[0,1,3,2] no samehole, other consumers scoped.')
row(981,[
 'RANK04 preserves the damaged triple order but changes persistentB0 to genuinely fainted before LastInTeam.',
 'The team query now skipsB0 by !able? and takes onlyB1 as its first ret index without comparing against the missingB0 rank.',
 'The formerly failing two-item numeric comparison is therefore absent in this control.',
 'The missing order entry itself is not repaired, and future other consumers can still observe it.'
],['battlefull','pokemon_growth_qual','switching'],'persistentB0 not able -> skip -> onlyB1 ret -> no3>nil comparison, hole retained.')
row(982,[
 'RANK05 independently givesB three healthy members in the original triple setup, yielding a merged five-member opponent party.',
 'The same B first-active destination index4 now exists in the initial five-element order.',
 'The result is[0,1,4,3,2] with no same nil hole.',
 'This one legal population control does not validate all multiowner counts, indices or current-history findings globally.'
],['ensure','startendfull','owners','teams','battlefull'],'tripleB3/party5 -> existingidx4 ->[0,1,4,3,2], no same missing slot.')
row(983,[
 'RANK06 preserves the damaged order but independently avoids the Illusion LastInTeam query at this replacement site.',
 'Without that particular consumer the hole alone does not force the same comparison failure in every later operation.',
 'A separate control cancels before legal SwitchOut registration, so no new stored switch choice enters this recall/message chain.',
 'Neither control rewrites the already existing startup party-order record or erases other potential future consumers.',
 'The correct bounded anomaly/control documentation is retained without converting possible exposure into a universal global failure or another required finding.'
],['command','switching','battlefull','startendfull','pbdebug'],'damagedorder +no queriedconsumer OR cancelbeforeSwitchOut -> no same localchain, original startup retained.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11m.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
