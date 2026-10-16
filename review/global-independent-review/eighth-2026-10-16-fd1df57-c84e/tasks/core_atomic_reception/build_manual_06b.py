import pathlib,json
P=pathlib.Path(__file__).resolve().parent;base=json.loads((P/'manual_batch_06a.json').read_text());d=base['source_dictionary'];rows=[]
def src(k,p,r):d[k]={'path':p,'range':r,'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
src('checksfull','Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb',[1,595]);src('battlerfull','Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',[1,777]);src('abilityeffects','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',[1,3208]);src('targetdata','Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb',[1,185]);src('shadowother','Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb',[1,460]);src('damage_state','Data/Scripts/011_Battle/007_Other battle code/003_Battle_DamageState.rb',[1,61]);src('startendfull','Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb',[1,568]);src('growth','Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',[1,271]);src('battlefull','Data/Scripts/011_Battle/001_Battle/001_Battle.rb',[1,867])
d['redirect_producers']={'path':'Data/Scripts/011_Battle/003_Move/012_MoveEffects_ChangeMoveEffect.rb','actual_reader':'/root/core_atomic_reception','complete_units':[[5,15],[21,32],[37,39],[140,219],[360,376],[1207,1212],[1217,1226]],'reading':'PARTIAL_FILE_COMPLETE_SEVEN_CLASSES_READ; no entire-file/class inventory approval'}
d['instruct']={'path':'Data/Scripts/011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb','range':[563,647],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_CLASS_READ including all blacklist values and predicates'}
d['dragon_darts_scale']={'path':'Data/Scripts/011_Battle/003_Move/009_MoveEffects_MultiHit.rb','actual_reader':'/root/core_atomic_reception','complete_units':[[36,63],[101,115],[137,147]],'reading':'PARTIAL_FILE_COMPLETE_THREE_CLASSES_READ; other first150-line classes read but no all-file claim'}
d['move_default_callbacks']={'path':'Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb','actual_reader':'/root/core_atomic_reception','complete_units':[[5,9],[12,18],[20,22],[35,53],[56,56],[61,65],[67,81]],'reading':'PARTIAL_FILE_COMPLETE_INDICATED_METHODS_READ'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(283,[
 'Default pbFindUser returns originalself; pbChangeUser first sets move.snatched=false, considers only status and canSnatch true.',
 'Scans allBattlers living order, starts strength100, rejects Snatch0 or >=currentstrength and SkyDrop>=0; ordinary positive producer marks in1..99 can replace with smaller.',
 'Equal eligible value is rejected by >=strength after first adoption, preserving first traversed. Source does not define arbitrary malformed negative marker as legal.',
 'Normal Snatch effect writes1 then raises user mark beyond current encountered marks over all living battlers, including itself; do not infer final installed value always1.',
 'Adoption changes actual user, consumes its Snatch0, sets move.snatched=true, recalculates battle.moldBreaker from new user and clears choice pretarget=-1.',
 'Original recent histories/global lastMoveUser were already recorded before adoption; actualuser rewrite does not relocate those previous writes.'
],['targetresolve','use','redirect_producers','battlerfull'],'positive marker producer→minimum-below100 live scan→consume/user/typeflag/target writes. Callback exceptions retain prior original-history prefix.')
row(284,[
 'pbFindTargets calls actual move.pbTarget(currentuser), starts empty and chooses family-specific pretarget/fallback helpers.',
 'NearAlly tries pretarget then random live ally; UserOrNearAlly tries pretarget allowing user then ownuser; AllAllies excludes self, UserAndAllies includes ownuser and live same side.',
 'NearFoe/NearOther try pretarget then randomally if selected same side else randomfoe; RandomNearFoe always randomfoe; AllNearFoes iterates livefoes.',
 'Foe/Other remove near restriction with analogous side-based fallback; AllFoes iterates non-near livefoes; AllNearOthers liveall near/excludesuser; AllBattlers liveall permitsuser/nonnear.',
 'Other target IDs invoke actual move.pbAddTarget callback, including default empty User/side targets and special counter/mirror/bide overrides; no generic always-one-target guarantee.',
 'Generic add rejects nil, faint unless targetsPosition, self unlessallowUser, nonnear unlessallowed orself; duplicates kept once. It does not independently enforce every opposing-family relation on arbitrary forged pretarget.',
 'Redirection returns immediately for battle.switching, cannotRedirect or targetsPosition, or not one-foe-target data / targetlist length!=1.',
 'Then move.pbModifyTargets may expand DragonDarts targets before active PropellerTail/Stalwart early return; no assertion those abilities skip this prior callback.',
 'Spotlight scan living/notSkyDropped/opposes/near-ifrequired chooses smallest positive below100 in speed/tie priority, returns adopted singleton before lower redirections.',
 'FollowMe/RagePowder next uses analogous rank/opposing/near gates; RagePowder additionally requires user.affectedByPowder?; successful singleton returns before drawing abilities.',
 'Then LightningRod Electric and StormDrain Water use current calculatedtype, preserve already-correct target ability, choose first other active drawingbearer in speed/tie order within near requirement; no inherent opponent-only filter in ability scan.',
 'TargetData can_target_one_foe means num_targets1 and targets_foe; distantchoice means num_targets1 and long_range. Raw display labels alone do not establish redirection eligibility.'
],['targetresolve','targetdata','battlerfull','query','priority','redirect_producers','dragon_darts_scale','move_default_callbacks'],'target-data/move override→family add/fallback→pre-gates→modify callback→ability bypass→Spotlight→FollowMe→drawing abilities; each normal branch and passed move object qualified.',open=['Complete special counter/mirror/bide target-add classes and every target/type override beyond exact named classes remain OPEN; no all Move promise.'])
row(285,[
 'Only !effective specialUsage enters Pressure block after final current targets mapping.',
 'For each actual target opposing actualuser with active PRESSURE, calls actualuser.pbReducePP(passed move) once; each qualifies independently.',
 'Separately when actual targetdata.affects_foe_side, iterates all liveother-side battlers and deducts once for activePRESSURE; default FoeSide/BothSides have empty Pokemon target lists.',
 'Uses same reducer skips/realMove/Transform rules, ignores false return for exhausted extra PP; passed move object and realMove binding are retained, not presumed rewritten user own move-slot identity.'
],['use','b_change','targetdata','targetresolve','ability_item'],'effective special flag→two independent pressure loops→same move PP writer; extra deductions precede blockers/own move failures.')
row(286,[
 'After Pressure, speed/tie pbPriority(true) scans nonnil current abilityActive bearers and calls MoveBlocking handler.',
 'DAZZLING/QUEENLYMAJESTY handler returnsfalse for choice[currentuser.index][4]<=0 or nonopposing bearer, and otherwise true iff targets contains opposing-to-user battler.',
 'True branch displays used briefly/splash/cannot-use/hides, marks actualuser.lastMoveFailed=true, then originalself CancelMoves and EndTurn, returns before use-message/own-failure/setup.',
 'No wrapper moldBreaker gate or ordinary PP reimbursement here; priority flag comes saved actualuser choice and can differ from raw move default priority.'
],['use','abilityeffects','priority','ability_item'],'adopted current priority→active blocker caller→handler priority/opposing/targets gate→failure/cancel/end after earlier PP writes.')
row(287,[
 'Actual move.pbDisplayUseMessage receives originalself intentionally even if Snatch changes actualuser; concrete overrides may differ from default used-text.',
 'Snatched flag then marks originalself.lastMoveFailed=true, displays newuser snatched original move; newuser failure state and original failure state remain distinct.'
],['use','targetresolve','move_default_callbacks'],'original source display→Snatch flag-specific history and feedback; no success inference from message.')
row(288,[
 'Actual move.pbMoveFailed?(actualuser,targets) runs after use/Snatch message and PP/history; true logs function, marks actualuser failure, originalself CancelMoves/EndTurn then return.',
 'Concrete failure predicate can itself mutate or raise; ordinary false return only permits later setup and does not guarantee later target/accuracy/hit success.'
],['use','move_default_callbacks','redirect_producers','orderproducers'],'move-specific whole-use check→normalfailure lifecycle or later setup; every concrete callback body has own exact source scope.',open=['All other complete Move whole-use failure predicates remain exact consumer OPEN; no all-class PASS.'])
row(289,[
 'Actual pbOnStartUse(user,targets) setup runs after own failure check, before thaw/Powder/primordial/Protean/quickcharge.',
 'Frozen actualuser and move.thawsUser? cures status then displays thaw; earlier precheck allowed a selfthaw move and real damage is not needed.',
 'Powder&&calculatedFire plays animation/message then sets actualuser failure; normal branch always CancelMoves/EndTurn/return, including when selfdamage guardfalse.',
 'Powder selfdamage occurs only when actualuser effectiveWeather is neither Rain nor HeavyRain AND takesIndirectDamage? true; activeMagicGuard blocks, UtilityUmbrella can suppress Rain toNone. Formal damage consequent of this precise child is candidate GR8-CAR-CAND-003 pending other review.',
 'Allowed Powder damage requests round(totalHP/4.0), actual effect-damage helper commits HP then message/healing/ability/faint callbacks; gated false skips damage and its pbGainExp call.',
 'Only damaging moves enter primordial suppression: effective battle HeavyRain+Fire or HarshSun+Water displays failure, marksactualuser failure, cancels and ends.',
 'Active LIBERO/PROTEAN requires !callsAnotherMove, !snatched, differentcurrenttype and nonpseudo actual type before splash/typechange/message; this uses existing source no added later-generation one-use restriction.',
 'Curse originally no targets can become Ghost via type change: clear choice target and rerun FindTargets only, not ChangeTargets; later target success still runs.',
 'Complete Curse target override chooses RandomNearFoe current>=8 or NearFoe earlier only when Ghost; otherwise base target. It changes own stats or cursed-target/ownHP through qualified effect callbacks.',
 'After these normal surviving branches actual pbQuickChargingMove callback runs before no-target/hit processing.'
],['use','b_change','battlerfull','battlefull','redirect_producers','move_default_callbacks','config'],'setup→thaw→Powder failed-action branch withconditionaldamage→damaging primordial failure→active typechange/Curse rebuild→quickcharge. Candidate only exactPowderdamage child, other clauses supported.',open=['GR8-CAR-CAND-003 actual other-context counterreview pending; no required credit before decision.','All other concrete setup/quickcharge/type overrides beyond actual named classes remain OPEN.'])
row(290,[
 'Empty targets plus current targetdata.num_targets>0 and !worksWithNoTargets displays no-target and marks userfailure; otherwise enters target/hit block.',
 'Entering block clears living allBattlers halfHP/statsDropped markers, resets each target whole DamageState, then first success check flags unaffected onfalse.',
 'Whole reset clears typeMod/unaffected/protection/Coat/Bounce/totalHPLost/faint flags plus perhit fields; perhit reset alone later preserves whole-use unaffected and cumulative HP loss.',
 'For no-target status canMagicCoat move, scans opposing living/notsemiinvulnerable in speed/tie order: MagicCoat consumes its flagfirst, otherwise activeMagicBounce without moldBreaker and notalreadyBounce marksflag; first wins.',
 'Failure no-target still proceeds shared tail after skipped hitblock; no generic refund of ordinary PP or history.'
],['use','checksfull','damage_state','targetdata','priority','redirect_producers'],'resolved targetcount and data→whole target state/checks ORno-target failure→shared end tail; reflecting flags map separately.')
row(291,[
 'Actual pbNumHits callback determines plannedcount; ordinary base1 or valid activeParentalBond/damaging/noncharging/onetarget returns2 and setsParentalBond3; named multihit classes override.',
 'Loop stops before hit on no-target Coat/Bounce selected; otherwise ProcessMoveHit called with hitindex and original skip flag.',
 'If first hit returnsfalse with targets, recomputes currentuser failure using unprotected targets unaffected states; protected entries skipped. Later-hit false breaks without this same first-hit reassignment.',
 'True hit increments realNumHits then stops for userfaint, userSleep/Frozen or alltargetsfaint; midhitDisable is not an added loop stop.',
 'Perhit actual entry rejects userfaint, runs InitialEffect, decrementsParentalBond ifpositive and first/perHit-success flag controls accuracy callback.',
 'Zero valid targets when nonempty list and !worksNoTargets causes missfeedback/current active missing-item hook, crashdamage, HPitemcheck, CancelMoves then false; not every message means HP damage.',
 'Continuing hit designates DragonDarts target subset, resetsperhit fields, calls damage/animation/HP callbacks and each source effect stage; all required concrete callbacks still qualified.'
],['use','checksfull','damage_state','move_default_callbacks','dragon_darts_scale','ability_item','item'],'planned count→each hit success/partialcommit→realcount+terminalgates; keep current vsperhit vswhole state distinct.',open=['Full concrete damage/accuracy/absorption/formula/effect callbacks not all received by this loop proof; exact other Move stages OPEN.'])
row(292,[
 'After hitloop entered, SuccessState.useState=2 regardless realNumHits; with targets typeMod starts0 and sums unaffectedfalse target typeMod. Arena adjudication derives skill separately.',
 'Plannedcount>1 conditionally prints effectiveness for damaging unaffectedfalse nonsubstitute targets, then realcount1 or>1 hit message.',
 'Targeted bounce checks each living target magicCoat/magicBounce; chooses new user, clones choice targetoriginaluser, reruns FindTargets/ChangeTargets, own-failure and first-targetchecks then one ProcessMoveHit(...false).',
 'Untargeted bounce uses selected coater/bouncer index with [] target list and its own check; originaluser markedfailed, newuser failed if callback unsuccessful; faint checks follow reached branch.',
 'Actual post-loop hook is targets.each pbEffectAfterAllHits(user,target), once per original target after entire hit loop, not inside perhit loop. WP40 phrase 每击后钩子 exact semantic assessment pending named ScaleShot vector; do not claim phrase already exact.',
 'Then original targets/user formally faint ifneeded, general EffectsAfterMove runs, living halfHP/statdrop markers reset; damage/effect/bounce prefixes survive later failure.'
],['use','successstate','damage_state','checksfull','targetresolve','redirect_producers','dragon_darts_scale','move_default_callbacks'],'hitloop complete→Arena state/multihit feedback→reflection callbacks→all-hits-per-target hook→faint/general effects; concrete count/identity matters.',open=['WP40:170 每击后钩子 semantic wording compared against real all-hits hook; full candidate not yet frozen, no newfinding credit.','All specific after-all-hits/general effect callbacks remain OPEN beyond named full classes and finite AbilityItem joins.'])
row(293,[
 'Reached common tail turns moldBreaker=false, invokes GainExp, updatesSkill for current liveall, calls pbHyperMode only originalchoice!=None, then EndTurn.',
 'Loaded ShadowOther actual pbHyperMode requires living Shadow/notalreadyhyper/playerowned, draws pbRandom(heartGauge)<=maxGauge/4 then writes Pokemon.hyper_mode before feedback; base empty method is not loaded default behavior.',
 'EndTurn marks lastRoundMoved, conditional Choice lock, clears BeakBlast/Charge1/GemConsumed/ShellTrap and continual ability checks; count2Charge retained.',
 'Instruct producer checks recentregular knownregistered move, notmultiturn, excludes pendingcharge functions/whole blacklist, positivefinite PP requirement, then marksInstruct=true only.',
 'Consumption liveall requires flag and current lastMoveUsed; clears flag before actual lastMoveUsed-slot scan. No match skips; captured slot is current recent-use identity, distinct from producer regular-history validation.',
 'Matching Instruct saves lastRoundMoved, showsfeedback, Instructed=true, current move-choice check then UseMoveSimple(...idxMove,false) throughlogonerr; normaldiagnostic return restores movedround, Judge, decisionreturn; normaltail clearsInstructed.',
 'Instruct false specialUsage means actual prechecks/obedience/ordinary PP; original registered command retained, recent history/PP maychange. Exception/positive decision can preserve transientInstructed flag; no ensure restore.',
 'Dancer requires originalself !Dancer flag, actualuser !failure, realhits>0, !snatched, magicCoater<0, globalDancer and danceflag; selected active other dancers collectspeed/tie and pop reverse order.',
 'For each Dancer saves movedround/Outrage/currentMove, adjusts Outrage ifpositive, choosespretarget, displaysability, setsDancer true, currentchoosecheck then specialsimple call; normalreturn restores saved fields and judges.',
 'Dancer normaltail clearsDancer; decisionreturn or diagnostic/restoreexception may leaveprefix. Whole method does not guarantee atomic restoration, nooccupancy guarantee beyond specified callbacks.'
],['use','growth','successstate','b_change','shadowother','battlerfull','ability_item','priority','instruct','debuglog','checksfull'],'shared end tail→actualShadow alias→EndTurn→Instruct ordinary reentry→Dancer special reentry; each has distinct saved/restored/retained fields and partialprefix.')
row(294,[
 'Default pbJudge checks both allFainted then DecisionOnDraw; else playerallfaintloss2 or foeallfaintwin1. Earlier callback mayalready set decision.',
 'pbJudgeCheckpoint defaultempty is overridden by Clauses; full selfKO/source lastMoveUser clause conditions maychange draw result. It is not universal instantaneous exit from every nested callback.'
],['startendfull','clauses','use'],'named judge checkpoints and finaljudge→default win/loss/draw or clauseoverride; normaldecision drives outer boundary, not all callbacks transactional.')
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_06b.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n');print({'rows':len(rows),'children':sum(len(x['children']) for x in rows)})
