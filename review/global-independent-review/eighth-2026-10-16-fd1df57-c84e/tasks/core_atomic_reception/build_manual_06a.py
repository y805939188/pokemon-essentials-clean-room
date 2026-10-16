import json,pathlib
P=pathlib.Path(__file__).resolve().parent;base=json.loads((P/'manual_batch_05b.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(271,[
 'pbUseMove computes skipAccuracyCheck once at entry as initial specialUsage and move object different from battle.struggle, before pbBeginTurn or continuation rewrite.',
 'If not FutureSight and usingMultiTurnAttack, choice move replaced from currentMove and specialUsage=true afterwards; original skip flag not recomputed.',
 'skip flag only bypasses later pbTryUseMove status/obedience/Truant/flinch/confusion/paralysis/attraction after choose/SkyDrop/recharge/Palace gates, not the target accuracy function globally.',
 'Battle.struggle identity makes skip flag false even when specialUsage=true; specialUsage controls base PP branch and regular-use record writes independently.'
],['use','choose_check','b_multiturn','priority'],'call-time flags→BeginTurn→multiturn rewrite→prechecks→PP and history; two flags have distinct timing and consumers.')
rows.append({'number':272,'layout_reason':'Comparison table column headers only: call class/skip marker/later checks/PP. Behavior belongs complete following four rows, not extra atom per header.'})
row(273,[
 'Ordinary pbProcessTurn calls pbUseMove without specialUsage argument except Struggle equality, so normal selected non-Struggle starts false/skipfalse.',
 'After earliest prechecks pass, later checks run in ordered gates; ordinary finite positive PP reduces1 before target determination; precheck refusal prevents this base deduction.'
],['use','choose_check','b_change'],'ordinary stored choice→defaultfalse call→gate sequence→PP. AI merely supplying ordinary registered choice does not prove its entire scoring/registration policy.',open=['All AI command producer/heuristic choices outside conditional ordinary registered choice remain exact OPEN.'])
row(274,[
 'Called/simple non-Struggle defaults specialUsage=true and entry skip=true; still passes initial choose/SkyDrop/recharge/Palace gates.',
 'Reached skip point bypasses later status/obedience checks; base PP deduction and later Pressure block both guarded !specialUsage and skipped.',
 'Special call helper uses actual slot move if idxMove>=0 else new move with pp=-1; each actual calling move may pass different specialUsage, so Instruct false path is separately handled.'
],['use','choose_check','b_change'],'pbUseMoveSimple arguments→exact entryflags→reached skip→no ordinary PP; not a blanket all summoned moves exemption.')
row(275,[
 'Ordinary action selecting battle.struggle passes specialUsage=true from pbProcessTurn equality, but skipAccuracyCheck=false by entry identity comparison.',
 'Sleep/frozen/obedience/confusion/paralysis/attraction later gates therefore remain ordered and eligible; specialUsage alone does not bypass them.',
 'Base PP not deducted under specialUsage, distinct from infinite PP guard inside reducer; no guarantee Struggle ignores every effect/helper gate.'
],['use','choose_check','b_change','priority'],'autoStruggle choice→specialtrue/skipfalse→normal later gates→base PP skipped.')
row(276,[
 'Multi-turn continuation rewrites specialUsage=true after initial skip value computed; usual ordinary entry starts skipfalse, so later gates still run.',
 'Continuation does not deduct ordinary base PP after rewriting; original already-special non-Struggle entry can retain skiptrue, so table does not define every continuation initialcall as false.',
 'If earlier recharge/SkyDrop/choose gate refuses, no later status gate runs regardless continuation flag; HyperBeam is among usingMultiTurnAttack checks.'
],['use','choose_check','b_multiturn','b_change'],'initial flag captured→continuation form→earliest gate→PP; no retroactive skip rewrite.')
row(277,[
 'Only not-futureSight, not-existing-multiturn branch considers Encore mid-round; needs Encore>0, registered move index>=0, commands-show gate.',
 'Gets currently encored move index; must be valid>=0, different from choice[1] and new index pbCanChooseMove? true.',
 'Then writes choice move index and actual moves[newIndex] and target=-1 before precheck; it checks new move eligibility, not previously registered move.',
 'If any condition fails retains original choice; later own precheck may reject. Choice writes can survive later callback/PP failure.'
],['use','priority','command','choose_check'],'current Encore binding→new-target eligibility→three choice writes→normal move attempt.')
row(278,[
 'After continuation/Encore rewrite, nil move returns before lastMoveFailed=false; paragraph requires nonempty valid move attempt.',
 'For nonnil move, lastMoveFailed=false before pbTryUseMove. Refusal returns with whatever earliest terminating gate actually wrote, not unconditional true.',
 'Refusal always clears lastMoveUsed and lastMoveUsedType; only effective !specialUsage also clears lastRegularMoveUsed/target.',
 'Then pbGainExp, CancelMoves and EndTurn sequentially; either can fail after earlier history clearing, so movedThisRound is only written if reached EndTurn.',
 'Exp opportunity accommodates self-confusion faint before ordinary PP, not proof every refusal gains positive exp.',
 'CancelMoves does not clear HyperBeam or Metronome; regular-vs-special cleanup uses flag after continuation rewrite, not initial entry flag.'
],['use','choose_check','b_change','b_multiturn'],'clearcurrentfailure→earliest precheck→history clears→gainExp/cancel/end. Runtime choice/effect failure fields distinct.')
row(279,[
 'After precheck true reloads choice move (disobedience may replace it); nil replacement returns before PP.',
 'Ordinary !specialUsage invokes pbReducePP. Positive finite normal PP5→4 through pbSetPP before type/targets/move-own-failure.',
 'Reducer returns true without deduction for active multi-turn, negative PP or nonpositive totalPP; PP==0 returns false, not negative infinite special.',
 'NoPP refusal announces used-move then noPP, clears recent move/type/regular/target, sets lastMoveFailed=true, cancels and ends; no target/type/effect branch reached.',
 'pbSetPP writes battle move.pp first, then realMove.pp only matching ID with realMove present and not Transform; transformed or copied identities need separate premise.',
 'Precheck refusal occurs before deduction, but no target/blocking/move-specific failures later do not automatically reimburse earlier PP.',
 'Any exception after scene/messages, PP write or setter first mutation retains reached prefix; no generic rollback or guaranteed real/battle PP alias.'
],['use','b_change','choose_check'],'qualification→possibly replacement→reduce/syncPP→type/targets/failure; first committed PP is not conditioned on eventual hit.')
row(280,[
 'Reached after PP, requires actual species AEGISLASH and raw current ability equality STANCECHANGE; this branch does not call hasActiveAbility? for that comparison.',
 'Damaging move requests form1 Blade; otherwise exact KINGSSHIELD requests form0 Shield; other status move does neither.',
 'pbChangeForm rejects faint/Transform/sameform then writes form/update preserving old damage amount, scene/form message/seen with source prefixes; request is not unconditional visible transform.',
 'This uses ability identity and move semantics, not a held-item family; underlying Pokemon form and scene consumer failures can follow earlier PP deduction.'
],['use','b_change','access','movebase'],'PP passed→species/rawability/move condition→guarded formsetter/update/scene/seen; source-valid request not native animation proof.')
row(281,[
 'Reached computes move.calcType from actual move.pbCalcType(user), then battle.moldBreaker=hasMoldBreaker? before target mapping.',
 'pbIsChargingTurn? true writes TwoTurnAttack and currentMove to move.id; false clears TwoTurnAttack only.',
 'Calls actual move.pbChangeUsageCounters(user,specialUsage) before Metronome/history overwrite; concrete callback can mutate or fail first.',
 'Only active METRONOME and !move.callsAnotherMove? updates count: retained lastMoveUsed equals current id and current lastMoveFailed false increments; otherwise count0.',
 'Recent identity is still prior value here, while ordinary attempt already cleared current failure before precheck; false here does not prove previous attempt succeeded.',
 'Skipped update for inactive item or calling shell is no count reset; later inner move may independently reach update. Counter is not clamped by writer.'
],['use','ability_item','access','b_multiturn','movebase','item'],'actual type/counter callbacks→Metronome gate before recent identity overwrite→later multiplier reader. Concrete type/usage counter callback completeness stays exact.',open=['Complete concrete Move pbCalcType/pbIsChargingTurn/pbChangeUsageCounters overrides beyond named partial/full facts remain OPEN; no blanket all-class proof.'])
row(282,[
 'Reached writes lastMoveUsed=id and lastMoveUsedType=calcType for regular and special use.',
 'Only !specialUsage writes lastRegularMoveUsed/Target and adds id to unique movesUsed list; special leaves this regular history unchanged.',
 'Writes battle.lastMoveUsed and battle.lastMoveUser original index before user Snatch rewrite; later clauses use global history distinct from actual rewritten user.',
 'Original index SuccessState.useState=1 assumes failure before user/target mapping; later success-state updates are separate, not guaranteed by history record.'
],['use','successstate','access'],'type/counters→per-user history→conditional regular history→global originaluser history→assumedfailure state→Snatch/targets.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_06a.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n');print({'rows':len(rows),'children':sum(len(x.get('children',[])) for x in rows)})
