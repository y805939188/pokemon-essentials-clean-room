import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11b.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(802,[
 'CM01 is the ordinary internal player-owned UseMove fixture, not a multi-turn continuation or Hyper Mode case; earlier action eligibility checks must have passed.',
 'Three badges produce badge_level=10*(3+1)=40.',
 'With level40 the strict level>badge_level predicate is false, so no high-level random draw occurs even when the applicable configuration category permits disobedience.',
 'Hyper obedience is true in the stated non-Hyper fixture, leaving disobedient false and returning true.',
 'This establishes the obedience gate result, not immunity from later Truant/confusion/paralysis or target/effect failures.'
],['checksfull','b_settings','shadowother','playerfull'],'normal eligibility -> owned/internal/multiturn gates -> threshold40 -> strict > false -> nonHyper true -> obedience true.')
row(803,[
 'CM02 holds earlier eligibility and non-Hyper conditions fixed and uses level60, badge_level40 and a foreign member under default ANY=false/FOREIGN=true.',
 'Pokemon.foreign? compares original owner id OR name with the player, rather than current battler side or a display-only foreign label.',
 'The enabled foreign category and 60>40 cause pbRandom(256) to be consumed.',
 'The source a=floor((60+40)*r/256) is floor(100*r/256), with r102 producing39 and r103 producing40.',
 'r102 leaves the high-level disobedient flag false; r103 sets it because a>=40, leading to pbDisobey rather than a guaranteed particular refusal outcome.',
 'Changing only to a self-owned member under those default settings bypasses that high-level draw and, with non-Hyper true, obeys.',
 'This is a conditional static RNG vector, not an observed frequency or execution of the battle random generator.'
],['checksfull','b_settings','foreign_method','shadowother','playerfull'],'config category + owner comparison -> strict level test -> integer draw transform -> disobedient flag -> conditional pbDisobey.')
row(804,[
 'CM03 is already inside pbDisobey with b<badge_level, a showable fight menu and at least one other currently selectable move; ordinary later gates and no extra PP drains are the successful continuation premise.',
 'It first logs disobedience and clears Rage; asleep usable-when-asleep refusal is an earlier branch, excluded by reaching this branch.',
 'It displays ignored-orders before checking the fight menu and collecting alternatives.',
 'Alternative collection excludes the originally chosen slot and checks each other slot with battle pbCanChooseMove?(index,slot,false).',
 'The selected alternative uses a separate random index; choice slot and Move reference are overwritten and target reset to -1, then this gate returns true.',
 'pbUseMove re-reads choice[2] after pbTryUseMove, so an ordinary successful continuation reduces the replacement move PP, not the previous move PP.',
 'No selectable alternative or unavailable fight menu instead returns false before that replacement/PP continuation; later interruption does not roll back an already changed choice.'
],['checksfull','priority','use','b_change'],'disobey branch -> message -> choose alternative -> mutate same choice -> later Try success -> re-read changed move -> ordinary PP reduction.')
row(805,[
 'CM04 has reached the final disobedience section with c=level-badge_level=20, a new r<20, and pbCanSleep?(self,false) true.',
 'The sleep branch is evaluated before the self-damage branch and invokes pbSleepSelf with the nap message.',
 'After that normal sleep application it returns false, ending this attempted action before ordinary PP subtraction.',
 'Sleep status/count and their bound Pokemon writes are real earlier prefix effects; later feedback/callback failure has no general rollback.',
 'This is not a claim that every disobedient member can sleep: actual status immunity/terrain/ability and other pbCanSleep? conditions remain operative.'
],['checksfull','statuses_full','b_change','use'],'final c/r -> actual sleep eligibility -> sleep mutation/message -> false -> pbUseMove failure tail without PP decrement.')
row(806,[
 'CM05 reaches the same final section with c20 and non-SLEEP status, but the earlier r<c AND CanSleep conjunction did not succeed.',
 'The code then subtracts c from r and tests the changed value r-c<c.',
 'If that inequality holds and status remains non-SLEEP, it invokes confusion self-damage and returns false; actual damage/faint/item/EXP consequences follow the called ordinary helpers.',
 'If original r0 and sleep eligibility is true, the earlier nap branch returns first, so the same numerical self-damage inequality cannot move self-damage ahead of sleep.',
 'If neither branch succeeds, a separate random refusal message is selected and false returned; the c20 vector does not force all r values into damage.',
 'PP subtraction is still later than this failure, while damage or sleep prefixes already reached may persist.'
],['checksfull','statuses_full','use','b_change'],'ordered nap conjunction -> only if not taken subtract20 -> conditional non-SLEEP confusion call -> false; ordinary failure tail separate.')
row(807,[
 'CM06 describes the Hyper Mode obedience subgate: not-in-Hyper returns true without its rand draw.',
 'While in Hyper, a nil move or raw move.type==SHADOW returns true without this draw.',
 'An actual non-Shadow move uses rand(100)<20, so only values0–19 pass this Hyper subgate.',
 'The caller ORs failure of this subgate into the independent high-level disobedience flag; a passing Shadow/20-percent Hyper result does not erase a high-level failure already established.',
 'The table shadow-always-obeys statement is read in its explicit Hyper subgate context, not as bypass of the separately documented high-level gate.'
],['shadowother','checksfull','b_settings'],'Hyper/type predicate -> local rand100 threshold -> caller disobedient OR; independent high-level flag preserved.')
row(808,[
 'CM07 assumes the priority production callbacks have returned ability subpriority-1 and item subpriority+1 for the same eligible entry.',
 'The final arbitration selects the item because a negative ability subpriority is beaten by item>=1.',
 'It clears both source flags first, then sets PriorityItem=true and final subpriority+1, leaving PriorityAbility=false.',
 'A later source-specific use message additionally requires the current itemActive? gate; saved source attribution alone is not proof an item effect was consumed.',
 'The local arithmetic does not claim every held item always returns+1 or every stored ability returns-1.'
],['priority','attack','item','abilityeffects','battlerfull'],'callback results -1/+1 -> source flags clear -> item branch -> final+1 +item flag -> later current-active consumer.')
row(809,[
 'CM08 uses the same incremental ordering calculation with TrickRoom active, equal move priority and equal final subpriority, known saved tie values, and speeds100/50.',
 'Incremental calculation rechecks current speeds and move priorities but does not create or reshuffle randomOrder; saved tie-breaker entries remain.',
 'Within those equal higher keys, TrickRoom sorts speed ascending, putting50 before100.',
 'Changing only the100-speed member to higher move priority makes that member first, because move priority is compared before subpriority or speed.',
 'Equal speed uses the stored tie value comparator; TrickRoom does not reverse the higher priority keys or redraw ties in this incremental path.',
 'These statements concern a reached priority recalculation, not a guarantee every speed change immediately invokes it regardless of Settings/caller timing.'
],['priority','attack','b_settings','battlerfull'],'incremental current keys +saved tie -> priority desc -> subpriority desc -> TrickRoom speed asc -> saved tie comparator.')
row(810,[
 'CM09 has generation>=8 and two valid quashed, alive, unmoved UseMove/Shift candidates in the current priority result.',
 'MoveNext candidates are attempted before ordinary candidates; the ordinary pass excludes positive Quash.',
 'When those passes cannot advance, the generation>=8 quashed pass visits positive Quash candidates in that priority order without ranking their numeric Quash level.',
 'A successful pbProcessTurn breaks that individual pass and the outer loop starts again, preserving ordinary decision/recalculation behavior; single-pass means one Quash priority scan per outer attempt, not two simultaneous completed actions.',
 'The pre-generation8 branch separately searches increasing Quash levels and is not applied to this vector.'
],['attack','orderproducers','use','b_settings'],'MoveNext -> ordinary excludingQuash -> gen8 priority-order quashed scan -> one successful action/reloop; old level-loop distinct.')
row(811,[
 'CM10 gives an owner-array state[-1,2,-2] before the new command phase.',
 'The phase resets only entries>=0 to-1, yielding[-1,-1,-2].',
 'The used marker-2 stays used and does not regain ordinary eligibility from that reset.',
 'This reset follows command-phase scene entry and per-battler choice clearing; an earlier exception can prevent reaching it and no total rollback is supplied.'
],['command','other'],'command entry/clear choices -> each side owner slot>=0 reset -> negative unused/used preserved.')
row(812,[
 'CM11 distinguishes the first three Mega eligibility checks from the later DEBUG+CTRL shortcut.',
 'The disabled switch returns false first; absent hasMega? eligibility returns false second; wild battler returns false third.',
 'Only after all three pass does DEBUG+CTRL return true, before SkyDrop, ring and unused-owner-slot checks.',
 'Thus debug input cannot bypass a disabled switch, missing Mega eligibility or the wild check; it can bypass those named later gates.',
 'The switch is read through actual Game_Switches semantics/config ID, not assumed forcibly off for every loaded save.'
],['other','pokemon_mega_full','battlerfull','config','crec_form_join'],'NO_MEGA switch -> hasMega -> wild -> DEBUGCTRL -> later SkyDrop/ring/owner count.')
row(813,[
 'CM12 invokes the Primal executor with an existing living battler and bound Pokemon, legal hasPrimal? result and not already primal.',
 'The executor has no Mega Ring or Mega registration/owner-slot gate and does not write the Mega times slot.',
 'On normal continuation it plays species-specific first animation, Pokemon.makePrimal, battler form assignment/update, scene changes/refresh and second animation/message.',
 'Fainted, missing form eligibility, or already primal each returns before that transformation; no-ring/no-registration alone is not sufficient eligibility.',
 'Actual individual/species/form/orb callback qualification is only the complete finite CTF reception, not an inference all species or plugins transform.',
 'Earlier form/individual recalculation writes can remain if later scene/presentation fails; normal final message does not establish save/reload/native output.'
],['other','pokemon_mega_full','primal_producers','crec_form_join','battlerfull','b_change'],'present/live/hasPrimal/!primal -> individual makePrimal -> battler sync -> scene/messages; no Mega owner slot write.')
row(814,[
 'CM13 assumes successful Fight or Bag menu registration in the command loop.',
 'A true menu result breaks its inner loop before the bottom pbCancelChoice, preserving UseMove or UseItem for attack phase.',
 'Bag may also mark commandsEnd when the registered item consumes all actions, without clearing that registered choice.',
 'Failed/cancelled paths reaching the loop bottom invoke pbCancelChoice; backing to a prior battler explicitly cancels that prior choice.',
 'Ordinary item cancellation refund is distinct from direct choice clearing or effect failure; preserve actual Bag/capacity/owner conditions and previously accepted refund lifecycle.',
 'A successful registration does not imply later effect succeeds or that all subsequent command/debug/decision branches necessarily preserve it.'
],['command','priority','items','bag','itemhandlers','ui_command'],'menu successful register -> break beforeCancel -> attackphase choice consumer; cancel path explicit CancelChoice/refund.')
row(815,[
 'CM14 uses the special simple-use entry with the battle Struggle object and an asleep member whose normal sleep check does not wake it.',
 'skipAccuracyCheck is specialUsage AND move!=battle.struggle, so it is false for this Struggle object.',
 'The ordinary earlier choice/action gates run, then sleep count is decremented and either cured at<=0 or continued.',
 'If still asleep and the move is not usableWhenAsleep, TryUseMove returns false before PP subtraction/effect execution.',
 'Special use therefore does not provide a general sleep bypass for Struggle, while the sleep-count/cure prefix itself may mutate the individual.'
],['use','checksfull','statuses_full','b_change'],'special Struggle identity -> skip=false -> sleep update -> still asleep refusal -> failure tail; no PP stage.')
row(816,[
 'CM15 is ordinary non-special use with all pre-use eligibility passing, initial PP5, no pressure drain and a later no-target failure.',
 'The code reduces PP immediately after successful TryUseMove and before user/target resolution and no-target handling.',
 'pbReducePP writes4 through pbSetPP; matching realMove with no Transform also writes the persistent Pokemon move PP.',
 'When execution later reaches no-target failure it does not restore that PP, yielding4 under the stated no-other-drain premise.',
 'Other move-use records and callbacks before no-target can also have changed; this vector claims the PP prefix rather than transactional all-state purity.'
],['use','checksfull','b_change','targetresolve'],'Try success -> PP5to4 -> matching realMove write-through -> target resolution -> later no-target failure no refund.')
row(817,[
 'CM16 keeps ordinary non-special PP5 but fails a pre-use eligibility check before the PP stage.',
 'That false TryUseMove branch clears lastMoveUsed/type, clears regular move/target for ordinary use, runs EXP/cancel/end-turn and returns.',
 'Since the ordinary PP reduction statement is not reached, this attempt itself leaves the move PP5.',
 'This PP result does not erase earlier status/count/choice/effect changes or claim callbacks in the failure tail cannot mutate unrelated state.'
],['use','checksfull','b_change'],'Try false -> record clears/EXP/Cancel/EndTurn -> return before PP -> own PP unchanged5.')
row(818,[
 'CM17 has no multi-turn override, a matching real move slot X with PP2, an Instruct flag and lastMoveUsed X when the consumer scans it, and passing preconditions.',
 'Instruct producer eligibility separately requires a known current regular move, no active multi-turn attack, no blacklisted function/charging command and available finite PP.',
 'After the original move ends, the consumer scans living allBattlers, requires Instruct and lastMoveUsed, clears Instruct before finding the matching move slot.',
 'It saves lastRoundMoved, sets Instructed, and invokes pbUseMoveSimple(lastMoveUsed,lastRegularMoveTarget,idxMove,false), so the actual slot is reused and specialUsage is false.',
 'With ordinary checks passing and no extra drain, the slot PP2 becomes1, with normal realMove/Transform write-through conditions.',
 'After normal return from logonerr it restores lastRoundMoved and judges; the global original command choice is not replaced by the helper local choice.',
 'The repeated ordinary use can still update recent-move/type/regular-target/used-record fields; restoring the acted-round marker is not a rollback of those records.',
 'An absent slot exits after clearing Instruct; later callback/diagnostic failure can leave earlier flags/PP/records, and a decision>0 return precedes the final Instructed=false cleanup.'
],['instruct','use','checksfull','b_change','battlefull'],'eligible producer flag -> end-use consumer -> localchoice actualslot special=false -> ordinary PP -> normal acted-round restore -> judge/flag tail.')
row(819,[
 'CM18 changes that instructed member to ordinary sleep that remains asleep, with X initial PP2 and no multi-turn override.',
 'The instruction still calls the same slot with specialUsage=false and therefore skipAccuracyCheck=false.',
 'Ordinary sleep decrement/continue rejects the use before PP reduction, leaving slot X PP2 from this attempt.',
 'Normal return still permits the outer instructed consumer to restore lastRoundMoved and clear Instructed after judge unless a decision branch returns first.',
 'The failed attempt can clear recent ordinary move records and advance status/count; it is neither a special sleep exemption nor an all-state no-op.'
],['instruct','use','checksfull','statuses_full','b_change'],'Instruct ordinary localentry -> sleep update/refusal -> noPP -> ordinary failurerecords/tail -> outer normal restoration only.')
row(820,[
 'CM19 supplies internal battle, player ownership, non-multi-turn Struggle special usage, earlier eligibility passing, level above the applicable threshold and configuration permitting high-level disobedience.',
 'The special Struggle object makes skipAccuracyCheck=false, so the obedience call is still reached after ordinary status checks.',
 'The obedience gate retains its own multi-turn/nonUseMove/noninternal/not-owned early returns; the supplied fixture excludes those bypasses.',
 'Thus applicable high-level sampling still occurs and may disobey; special use alone does not force obedience.',
 'Struggle special-use PP rules remain a later separate concern, not evidence the pre-use obedience gate was skipped.'
],['use','checksfull','b_settings','foreign_method','shadowother'],'special Struggle skip=false -> ordinary status -> own obedience gates -> applicable high-level draw; no automatic obedience.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11c.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows))
