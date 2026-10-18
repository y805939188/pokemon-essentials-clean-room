import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11c.json').read_text());d=base['source_dictionary'];rows=[]
d['scene_choose_target_complete']={'path':'Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb','complete_units':[[333,356],[360,382],[384,439]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete target texts/first cursor/selection methods actually read; no entire Scene file or native Input execution'}
d['target_buttons_complete']={'path':'Data/Scripts/011_Battle/004_Scene/005_Battle_Scene_Menus.rb','range':[520,546],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete refreshButtons actually read; constructor/mode state supplied by separately received UI finite facts'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(821,[
 'CM20 distinguishes valid ordinary item families rather than treating every outcome as one use-result Boolean.',
 'For family1, after the normal use message and current party/battler lookup, execution eligibility false reaches no-effect message and pbReturnUnusedItemToBag.',
 'Refund requires consumed_after_use and actual ownership/capacity; that branch retains the item identity in the choice, leaving the separately documented later refund/clear consumers applicable.',
 'When eligibility is true, family1 invokes the Pokemon effect, then clears choice[1] on normal return regardless of the effect return value; a false effect return alone does not trigger generic refund.',
 'Family4 directly invokes the ball UseInBattle handler, then clears choice[1] on normal return, without that family1 execution-eligibility/refund branch.',
 'A failed capture is therefore not equivalent to refund; callback exceptions can prevent later choice clearing while preserving earlier Bag/HP/capture prefixes.',
 'Neither branch claims selection-time egg/Embargo/Hyper auxiliaries are rerun identically in every executor; actual call sites and current eligibility callback determine them.'
],['items','command','itemhandlers','bag','itemdata','catch_full'],'registered family -> exact executor -> eligibility-false refund with identity retained OR effect-return ignored +identity clear; ball direct handler separate.')
row(822,[
 'CM21 assumes a status move that canSnatch and eligible living allBattlers with positive Snatch marks2/4, another mark0 and a SkyDrop victim.',
 'The resolver resets move.snatched=false before scanning and initializes strength100.',
 'Mark0 and marks>=current strength are skipped; eligible lower mark2 beats4 regardless of which of those two appears first.',
 'SkyDrop>=0 is rejected even if its Snatch mark would otherwise win.',
 'On a winner it replaces the move user, clears only that winner Snatch mark, sets move.snatched=true, updates battle.moldBreaker from the new user and resets prechosen target to-1.',
 'If status/canSnatch is false or no eligible mark<100 exists, the original user remains; this vector does not bypass those outer conditions.',
 'The changed user/target/flag prefix is not rolled back if later target/effect processing fails.'
],['targetresolve','battlefull','battlerfull','use'],'status/canSnatch -> living scan -> minimum qualifying positive mark -> winner writes -> later target/effect consumers.')
row(823,[
 'CM22 uses an actual Call action with the ordinary pbDebugRun result0, a non-Shadow battler and SLEEP status.',
 'After owner and two call messages, the non-Shadow sleep branch calls pbCureStatus.',
 'This clears actual status/count through the normal bound Pokemon write path; it does not also take the later Accuracy raise branch.',
 'A nonzero debug-run result exits before these Call effects, and a Shadow member takes the separate Hyper/heart-gauge branch even if also asleep.',
 'Only reached cure/presentation prefixes are established; no game/input/audio execution is claimed.'
],['other','running','statuses_full','b_change','shadowother'],'Call -> debug0 -> messages -> !Shadow &&sleep -> CureStatus; mutually exclusive later accuracy branch.')
row(824,[
 'CM23 changes the same ordinary Call fixture to non-Shadow, non-SLEEP and actual CanRaiseAccuracy true.',
 'It invokes pbRaiseStatStage(ACCURACY,1,battler), then item-on-stat-dropped checking after normal return.',
 'The actual stat helper still implements caps/Contrary/Simple and relevant ability semantics; the listed one-stage input is not a bypass of that helper.',
 'If raising is not permitted, it gives nothing-happened feedback instead; Hyper/Shadow and sleep branches still have precedence.',
 'Battle stat stages are runtime effects; this does not directly rewrite permanent Pokemon accuracy or establish native/save behavior.'
],['other','stages','battlerfull','abilityeffects','ability_item'],'debug0 -> !Shadow/!sleep -> CanRaiseAccuracy -> raise helper1 -> item check; capped/other branches separate.')
row(825,[
 'CM24 has both sides of size2 or smaller, satisfying the first pbCanShift? rejection.',
 'The command Shift option is consequently not selectable through that eligibility check.',
 'An asymmetric battle with one side3 is outside this first rejection and must still pass side size/center/owner checks; this row does not forbid all such cases.',
 'This is a selection predicate, distinct from manually invoking the lower-level Shift executor or directly mutating a choice.'
],['other','scene_fight','command'],'both side sizes<=2 -> CanShift false -> ordinary option availability; executor is not selection authorization.')
row(826,[
 'CM25 assumes a valid selectable three-slot-side Shift from outer0 to central2 with matching owner and existing legal swap occupants.',
 'The Shift choice is consumed in the attack move loop according to the same priority scheduling gates as UseMove.',
 'pbProcessTurn computes destination2, calls pbSwapBattlers, then displays moved-to-center feedback.',
 'The swap moves resident battler objects/indices and associated choice references but leaves position effects attached to their slots; it is not ordinary withdrawal/entry or a hazard application.',
 'After the swap/message, it calls pbBeginTurn, pbCancelMoves and records lastRoundMoved=current turn before true return.',
 'Thus multi-turn state is cancelled on this normal path; if swap/message/helper fails earlier, later cancellation/acted marker is not guaranteed or rolled back.'
],['other','use','swap','attack','b_change'],'legal registered Shift -> ProcessTurn -> swap0/2 -> message -> BeginTurn/CancelMoves -> acted marker true.')
row(827,[
 'CM26 uses the first ordinary player battler command selection where Run is offered.',
 'RunMenu calls pbRun immediately during command selection and returns result!=0.',
 'Result1 successful escape or result-1 spent failed attempt both make RunMenu true; command loop sets commandsEnd and stops choosing remaining actions.',
 'Result0 means no permitted/completed attempt, so the loop reaches cancellation and continues choosing.',
 'A failed actual attempt is different from a trap/forbidden-run result0; runCommand increments only in the reached ordinary attempt path, not every menu click.',
 'Decision/audio/messages and choices follow their actual earlier branches; no universal atomic rollback accompanies return values.'
],['running','command','ui_mainmenu'],'first Run -> immediate pbRun -> !=0 -> commandsEnd; zero -> CancelChoice/continue.')
row(828,[
 'CM27 enters DEBUG+CTRL outcome selection and chooses Cancel, or the equivalent else branch.',
 'pbDebugRun returns-1 without writing @decision in that branch.',
 'pbRun propagates that nonzero result immediately, and RunMenu treats-1 as true.',
 'Consequently ordinary command selection stops remaining actions even though the decision value is unchanged.',
 'This is a debug menu path, not a successful normal flee; preceding messages/UI may have occurred and host Input was not executed.'
],['running','command'],'debug selector Cancel -> -1 unchanged decision -> Run immediate -1 -> RunMenu true -> command stop.')
row(829,[
 'CM28 is N01 ordinary non-special accuracy70 with both stages0, effective MoldBreaker on user, no user NoGuard, target effective NoGuard and no other named override/multiplier/affection branch.',
 'Per-hit semi-invulnerability handling sees target.hasActiveAbility?(NOGUARD) directly and lets that layer proceed; it does not apply the accuracy target-handler MoldBreaker guard there.',
 'The later accuracy modifier path invokes target ability handlers only when target abilityActive AND !battle.moldBreaker, so target NoGuard does not set base_accuracy0 in this fixture.',
 'With stage multipliers both100 and all other modifiers neutral, threshold remains70.',
 'The ordinary draw requires r<threshold, so69 hits and70 misses.',
 'This ordinary method contract excludes OHKO or move-specific override paths; dropping one fixture exclusion can change the draw or outcome.',
 'The accuracy helper may consume MicleBerry or set affection-missed in other fixtures; neither extra effect is silently included here.'
],['checksfull','calculations','abilityeffects','battlerfull','use'],'NoGuard semi-invulnerability boolean -> normal accuracy -> MoldBreaker skips target callback -> threshold70 -> strict random boundary.')
row(830,[
 'CM29 changes only MoldBreaker to false in the CM28 ordinary fixture.',
 'Target abilityActive now admits its NoGuard AccuracyCalcFromTarget handler, which writes modifiers.base_accuracy=0.',
 'After modifier processing, ordinary pbAccuracyCheck returns true for base_accuracy0 before drawing accuracy RNG.',
 'Other earlier failure/protection/target gates and distinct accuracy-overriding function families remain operative; this is not every move always succeeds.'
],['checksfull','calculations','abilityeffects','battlerfull'],'same targetNoGuard +!MoldBreaker -> target callback base0 -> ordinary accuracy early true/no accuracy draw.')
row(831,[
 'CM30 gives the same live member positive HealBlock, a healing move with PP5, nonempty recent-use/type and regular-move/target records, and no earlier blocking change.',
 'pbCanChooseMove tests HealBlock and move.healingMove? without the specialUsage exemption applied to Disable; both ordinary and non-Struggle special calls therefore reject at this first Try check.',
 'Both failures set lastMoveFailed and clear lastMoveUsed/type before the PP stage, leaving the attempted slot PP5.',
 'Ordinary failure also clears lastRegularMoveUsed and sets lastRegularMoveTarget=-1.',
 'Special failure preserves those regular records because their clear is guarded !specialUsage, while recent lastMoveUsed/type are still cleared.',
 'Both proceed through reached EXP/cancel/end-turn failure helpers; their earlier effects or later errors are separate, not transactional state restoration.',
 'The healing classification uses actual predicate/family definitions already finitely read, not a move name or English description heuristic.'
],['checksfull','use','b_change','move_predicates'],'HealBlock healing predicate -> Try false beforePP -> common recent clears +ordinary-only regular clears -> failure tail.')
row(832,[
 'CM31 fixes a legal later3v3 state: user0 alive, central ally2 existing fainted without backup, far ally4 alive and no other living nonself ally; target mode NearAlly and no state change before resolution.',
 'FirstTarget loops living same-side battler objects and passes the object itself into nearBattlers?(b,idx); that method does not normalize this first object argument, so integer-pair exclusion[0,4] does not reject this object4.',
 'The initial cursor is therefore4, while candidate text creation passes integer indices through MoveCanTarget and rejects integer0-to4 as far, leaving texts[4]=nil.',
 'This nil is distinct from an eligible existing fainted candidate text equal to empty string.',
 'ChooseTarget explicitly highlights battler/data box4 despite the nil text; target button refresh only sets selection inside if texts[i], so that button is not selected.',
 'USE returns current cursor4 without an independent texts[4] validity guard; registration writes target4 if the ordinary caller reaches it.',
 'At execution pbAddTarget validates current integer adjacency, rejects far4, and the NearAlly random fallback has no living near nonself ally, so no valid target is recovered.',
 'Keeping ally2 alive instead makes initial target2; with both2/4 fainted, the living same-side scan leaves no nonself candidate and the final default is user0.',
 'This is the already specified abnormal selection/parse boundary, not permission to equate every lack of a near ally with choosing self, and no new finding is counted.'
],['scene_choose_target_complete','target_buttons_complete','ui_targets','firsttarget','priority','battlefull','targetresolve','command'],'object-argument initial scan -> cursor4 vs integer niltext -> highlight/no button -> USE4/register -> integer execution reject/no near fallback.')
row(833,[
 'CM32 explicitly supplies a legal registered consumable Direct5 item I that is non-important/nonball/nonSnag, has no effect or eligibility handlers/conditional match, and an internal live actionable player with Bag quantity1.',
 'Ordinary UI offers Use under those data/menu conditions; this is not an arbitrary unknown ID or every Direct item.',
 'Command family5 selects the user Pokemon and has no family1/2/3 effect-existence rejection.',
 'With no applicable CanUseInBattle handler, triggerCanUseInBattle defaults true and ordinary registration records the choice then removes1 from Bag, yielding0.',
 'At attack execution family5 rechecks the same default-true eligibility, invokes the missing UseInBattle handler without a meaningful effect, and on normal return clears choice[1].',
 'Effect return is not tested for generic refund, so Bag remains0 and the item identity is gone; earlier accepted lifecycle keeps this distinct from eligibility-false identity retention.',
 'Changing the same item data only to family1 or3 makes their effect-existence check reject before registration, so Bag stays1.',
 'A callback, Bag failure, data mismatch or different conditional handler violates this controlled fixture and can leave different prefixes; compiled/game execution is not claimed.'
],['command','items','itemhandlers','battleitems','bag','itemdata','ui_command'],'legal Direct5 data -> UI Use -> default eligibility true -> register consume1 -> no effect callback normal -> choice clear/no refund; family1/3 reject earlier.')
row(834,[
 'CM33 fixes the CM02 high-level internal player-owned ordinary non-Hyper fixture and compares config categories while preserving threshold40/strict level>threshold.',
 'ANY=true enables high-level sampling for both original self-owned and foreign individuals, independent of FOREIGN flag.',
 'ANY=false and FOREIGN=true enables it only when Pokemon.foreign?(battle.pbPlayer) is true.',
 'ANY=false and FOREIGN=false enables it for neither category.',
 'Therefore defaults false/true sample only foreign members, and self-owned members do not consume that high-level draw.',
 'At or below the threshold neither category consumes the high-level random draw even if its config category is enabled.',
 'Independent Hyper failure and the gate early-return conditions still apply; this matrix concerns only the named high-level source of disobedience.'
],['checksfull','b_settings','foreign_method','shadowother'],'config OR expression +owner identity -> strict high-level test -> conditional pbRandom; Hyper flag independent.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11d.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows))
