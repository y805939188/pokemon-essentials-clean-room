import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_05a.json').read_text());d=base['source_dictionary'];rows=[]
d['successstate']={'path':'Data/Scripts/011_Battle/008_Other battle types/004_BattleArenaBattle.rb','range':[1,366],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
d['palace']={'path':'Data/Scripts/011_Battle/008_Other battle types/003_BattlePalaceBattle.rb','range':[1,245],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
d['debuglog']={'path':'Data/Scripts/001_Technical/001_Debugging/001_PBDebug.rb','range':[1,77],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
d['stomping']={'path':'Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb','range':[554,559],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_CLASS_READ'}
d['charge_extra']={'complete_classes':[{'path':'Data/Scripts/011_Battle/003_Move/005_MoveEffects_Misc.rb','range':[169,187]},{'path':'Data/Scripts/011_Battle/003_Move/005_MoveEffects_Misc.rb','range':[687,693]}],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_TWO_CLASSES_READ'}
d['move_order_helpers']={'complete_units':[{'path':'Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb','range':[6,6]},{'path':'Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb','range':[119,126]}],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_EMPTY_CALLBACK_AND_ALREADY_MOVED_HELPER_READ'}
d['orderproducers']={'path':'Data/Scripts/011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb','range':[426,558],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_CLASSES Pursuit/ShellTrap/Round/AfterYou/Quash ACTUALLY_READ; no entire effect-file claim'}
def row(n,c,u,chain,**extra):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**extra))
row(256,[
 'Attack begins scene.pbBeginAttackPhase before per-battler state writes; every nonnil battler gets successStates[i].clear, including a faint battler.',
 'Only nonfaint battler gets turnCount+=1; this is per-battler count, not outer battle turnCount.',
 'SuccessState.clear default full=true resets typeMod to normal effectiveness, useState0, protectedfalse, skill0; updateSkill later clear(false) retains its skill.',
 'Choice other than UseMove/Shift/SwitchOut clears DestinyBond and Grudge; each nonnil battler independently checked.',
 'Rage clears unless chosen function StartRaiseUserAtk1WhenDamaged; this uses actual choice-function predicate, not displayed move name.'
],['attack','successstate','priority'],'scene attack start→per-slot counter/success/effect prefix→full priority. Error in any earlier consumer preserves reached writes; no atomic whole-phase reset.')
row(257,[
 'Attack calls pbCalculatePriority(true) after reset before messages/Call/Switch/Item/Mega/Move processing.',
 'true requests full stored bracket/speed/tie/priority initialization under actual calculator; later partial recalculation has distinct update semantics and is not substituted here.'
],['attack','priority'],'fresh whole-round calculation→stored priority consumers; full algorithm children remain exact §6 independent mapping.')
row(258,[
 'Priority message loop walks pbPriority; PriorityAbility flag plus currently abilityActive triggers ability PriorityBracketUse.',
 'Only elsif PriorityItem flag plus currently itemActive triggers item use; ability flag active branch has precedence.',
 'Flags are saved by bracket calculator only for adopted source; callbacks are not repeated for every tentative/bracket-losing trial.',
 'QuickClaw/Custap adopted callback may display and Custap consume on this actual current-active gate; earlier bracket adoption alone does not guarantee later message/item consumption.'
],['attack','priority','ability_item','item'],'calculator stored source flags→current activity recheck→one adopted PriorityBracketUse; failure/message/item consumption prefixes separate.')
row(259,[
 'Call loop pbPriority order selects choice Call and living user; sets lastMoveFailed=false before pbCall.',
 'Call can debug-exit early, calm Shadow hyper mode/heart gauge, cure sleep, raise accuracy or no-op; lastMoveFailed flag was already cleared.',
 'End-of-round copies lastMoveFailed into lastRoundMoveFailed; StompingTantrum complete class doubles base power only when this latter flag truthy. No-effect Call false bookkeeping therefore differs from prior failure if retained through round end.'
],['attack','other','use','eor','stomping'],'Call eligibility→failure flag clear→actual Call branch; no hit/damage or learned-move success inferred.')
row(260,[
 'Switch phase pbPriority chooses living SwitchOut, saves target, sets lastMoveFailed=false and lastMoveUser=user before recall message.',
 'Recall message precedes pbPursuit; pursuit can decide battle and then switch phase returns before actual replacement.',
 'If no decision, all living battlers returned by allBattlers have droppedBelowHalfHP/statsDropped=false, then RecallAndReplace and entering hook.',
 'Pursuit switching=true during scan, eligible living opposing unmoved pursuit-function users must pass target and move choice, awake/not frozen, no SkyDrop and no TRUANT loafing.',
 'Nonwild eligible pursuer can registered-Mega evolve before its forced target update/processTurn(false); decision or switcher faint breaks scan, normal tail switching=false.',
 'Pursuit complete move override gets always-hit and double base damage only while battle.switching; if callback raises before tail, switching=true prefix can remain. Correct TRUANT spelling is preserved under COM001.'
],['attack','switching','query','priority','choose_check','other','orderproducers'],'recall bookkeeping→Pursuit special process→decision gate→living marker reset→replace/entry; no blanket guarantee selected switch completes after interception.',open=['All switch hazard/ability combinations remain represented by bounded entry/AbilityItem joins and later WP41 exact children; not closed by this phase summary.'])
row(261,['After Call then Switch phase completes, attack returns immediately when decision>0 before Item/Mega/Move.'],['attack'],'ordered phase boundary decision check; zero continues.')
row(262,[
 'Item phase scans priority for living UseItem and marks lastMoveFailed=false before checking item identity; cleared/nil item skips.',
 'Registered battle_use1/2 executes Pokemon item only for target>=0;3 current battler;4 ball;5 direct; other type skips.',
 'After each dispatched item, decision>0 returns from item phase, bypassing its final optional priority recalculation.',
 'Normal completed whole item pass recalculates priority only if RECALCULATE_TURN_ORDER_AFTER_SPEED_CHANGES; this is distinct from per-item unconditional recalc.'
],['attack','items','itemdata','priority','b_settings'],'stored choice/type→family executor→per-item decision return OR completed pass config recalc; previous inventory/effect/identity writes retained.')
row(263,['After Item phase, attack decision>0 returns before Mega/Move even if item phase returned early.'],['attack'],'item decision boundary; no later action mandated after battle end.')
row(264,[
 'Mega phase uses current priority list, skips wild, requires living user and UseMove choice.',
 'It resolves owner/own side and calls Mega only when that owner registration equals this battler index.',
 'Called Mega action itself has narrower nil/pokemon/hasMega/alreadyMega guard, early player count and transform/event/ability/recalc prefixes; menu eligibility checks are not all repeated here.'
],['attack','other','owners'],'priority→wild/choice/liveness/owner registration→Mega action; actor, owner token and callback conditions are separate.')
row(265,[
 'Before main loop, current priority living UseMove users not movedThisRound invoke their actual move.pbDisplayChargeMessage.',
 'ShellTrap override writes ShellTrap=true before common animation and message; later effect failure checks this flag and tookPhysicalHit; its charge message is not its actual damage.',
 'FocusPunch charge writes FocusPunch=true before animation/message, later fails only when flag and tookMoveDamageThisRound; BeakBlast writes its flag before animation/message. Default charge callback is empty.'
],['attack','use','movebase','orderproducers','charge_extra','move_order_helpers'],'preloop charge callbacks→loop; received original Move facts alone not all charge methods.',open=['Lexical census found3 concrete default-source overrides; those3 complete classes and empty default callback received. Plugin overrides/native presentation remain OPEN; no whole Move approval.'])
row(266,[
 'Each loop snapshots pbPriority; forced-next pass requires MoveNext truthy, living, choice UseMove or Shift, and not movedThisRound.',
 'Calls pbProcessTurn and breaks this pass only when returned advance truthy; decision>0 returns; advance restarts loop at forced-next.',
 'Round effect marks own side Round and first live ally choosing same function and not moved MoveNext=true/Quash0; AfterYou effect similarly marks target after its own failure gates.',
 'pbBeginTurn clears MoveNext and Quash for reached user; these are transient scheduling flags, not persistent speed/priority edits.'
],['attack','use','orderproducers','query','move_order_helpers'],'actual effect producer writes flags→next loop forced consumer→processBeginTurn clears→advance restarts; no native/random execution.')
row(267,[
 'Regular pass uses loop priority snapshot, skips positive Quash/faint/already moved/non Move-or-Shift; processTurn result advance stops pass and restarts loop.',
 'Regular scan decision>0 returns before quashed pass; a move may alter ordering/forced flags in its callback before the next snapshot.'
],['attack','use','priority'],'nonquashed pending action→one normal process result→new snapshot on advance. No fixed old snapshot across completed actions.')
row(268,[
 'Generation>=8 quashed pass scans current loop priority once for positive Quash/living/not-moved Move-or-Shift; advance true breaks then restarts whole loop.',
 'Earlier generation starts quashLevel1 and scans for exact rank, keeping moreQuash when larger rank exists; level loops stop on advance or no larger rank.',
 'Complete Quash effect finds maximum live battler Quash and sets target max+1 and MoveNext=false; failure rejects already moved/no chosen move/already-maximal or ordinary last-in-priority target.',
 'Current configuration MECHANICS_GENERATION8 takes >=8 branch; earlier branch is conditional source contract, no claim host earlier-gen run.'
],['attack','orderproducers','config','move_order_helpers'],'effect rank producer→generation-specific consumer→pbBeginTurn clear. All actual Quash failure gates separate from scheduler predicate.')
row(269,[
 'Each normal action returns advance true from pbProcessTurn, so caller restarts at forced-next after one successful process; non-action/fainted returns can permit further scan.',
 'After all passes without advance, final scan asks whether any living not-moved UseMove/Shift remains; if any repeats, otherwise exits move phase.',
 'Decision positive checked after each forced/regular/quashed pass before further work; no action replay for movedThisRound users under normal bookkeeping.'
],['attack','use'],'one process→advance→forced-next restart; all-done liveness/choice/moved check controls termination, not count of menu choices alone.')
row(270,[
 'Single-user process returns false immediately when fainted, before flee/shift/use.',
 'Normal tryFlee=true wild alwaysflee rule and pbCanRun? true runs BeginTurn, flee sound/message, sets decision3, EndTurn then true; interruption of earlier display can precede decision write.',
 'Shift computes across/center index by sideSize, requests actual swap when valid and displays corresponding movement text; then BeginTurn, cancels multiturm moves, sets lastRoundMoved=current and returns true.',
 'Shift does not call EndTurn in this branch; swap may refuse when either battler missing or owners differ; branch bookkeeping/message calls still follow reached source order.',
 'Other non-UseMove calls BeginTurn and EndTurn then returns false; ordinary Move logs, invokes actual pbUseMove through logonerr, judges, optional speed recalc and true.',
 'logonerr rescues ordinary StandardError via bare rescue, logs/backtrace/prints/flushes; normal error-reporting return permits later Judge/recalc despite failed pbUseMove prefix. Handler/reporting itself may raise and non-StandardError not covered.',
 'BeginTurn snapshots DestinyBondPrevious then clears DestinyBond/Grudge/MoveNext/Quash and invalid Encore; EndTurn marks moved, conditional Choice lock, clears BeakBlast/Charge1/Gem/ShellTrap and runs all-living continual abilities.',
 'CancelMoves clears specified TwoTurn/Rollout/Outrage/Uproar/Bide/currentMove-if-noHyperBeam/FuryCutter, possible final-Outrage confusion; HyperBeam itself not canceled by this routine.'
],['use','running','swap','ability_item','b_multiturn','b_settings','debuglog'],'phase actor→branch-local Begin/End/cancel/moved writes→Judge/recalc. Persistent Pokemon setters can write through but these transient scheduling fields do not certify save/reload.',open=['pbPrintException/native logging/disk and every concrete Move effect beyond exact named source units remain precise consumer OPEN; wrapper return is not effect success.'])
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_05b.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children']) for x in rows)})
