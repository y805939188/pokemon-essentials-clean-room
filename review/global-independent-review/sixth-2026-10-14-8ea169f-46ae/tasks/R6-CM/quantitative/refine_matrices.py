from pathlib import Path
import json
O=Path(__file__).parent;B='reference/pokemon-essentials/Data/Scripts/011_Battle/'
def r(p,a,z=None):return {'path':p,'lines':[a,z or a]}
p=O/'reverse-matrix.jsonl';a=[json.loads(x) for x in p.read_text().splitlines()]
extras={
11:[r(B+'002_Battler/001_Battle_Battler.rb',248,287),r(B+'003_Move/003_Move_UsageCalculations.rb',239,484),r(B+'002_Battler/003_Battler_ChangeSelf.rb',5,34)],
35:[r(B+'003_Move/008_MoveEffects_MoveAttributes.rb',1338,1380),r(B+'002_Battler/007_Battler_UseMove.rb',583,760)],
274:[r(B+'002_Battler/007_Battler_UseMove.rb',154,375),r(B+'002_Battler/007_Battler_UseMove.rb',583,711)],
291:[{'artifact':'numerical-vectors.jsonl','records':'MH01–MH44','evidence':'independent_static_derivation'}],
302:[r(B+'002_Battler/007_Battler_UseMove.rb',439,453)],
281:[r(B+'004_Scene/004_Scene_PlayAnimations.rb',219,232)],
52:[r(B+'003_Move/007_MoveEffects_BattlerOther.rb',75,97),r(B+'003_Move/003_Move_UsageCalculations.rb',489,498),r(B+'002_Battler/007_Battler_UseMove.rb',712,719)],
53:[r(B+'003_Move/007_MoveEffects_BattlerOther.rb',532,544),r(B+'003_Move/003_Move_UsageCalculations.rb',503,513)],
}
for x in a:
 if x['formal']['path'].endswith('wp46-damage-multihit-and-healing.md'):
  line=x['formal']['lines'][0]
  if line in extras:
   x['source_evidence']+=extras[line];x['evidence']='static_read_or_independent_derivation';x['status']='STATIC_MATCH';x['kind']='behavioral_clause_or_vector_index'
  if line in [3]:x['evidence']='static_text_count';x['source_evidence']=[{'artifact':'coverage-counts.json','evidence':'identity_arithmetic_only'}];x['status']='COUNT_MATCH_NOT_BEHAVIOR_PROOF'
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in a))
p=O/'forward-matrix.jsonl';a=[json.loads(x) for x in p.read_text().splitlines()]
over={
'HitTwoTimesTargetThenTargetAlly.pbModifyTargets':'Only one initial target permits expansion. Collect living eligible allies; no candidate keeps the original list, one candidate consumes no choice draw, multiple candidates use a uniform choice; final addition enforces target distance.',
'HitTwoTimesTargetThenTargetAlly.pbShowFailMessages?':'For expanded target lists, visible failure messages are enabled only when at most one living unaffected-free candidate remains; otherwise suppress them. Ordinary single-target uses retain ordinary visible failures.',
'HitTwoTimesTargetThenTargetAlly.pbDesignateTargetsForHit':'Build the unaffected-free list; volley two selects its second entry when available, otherwise its first. Recursive consumer additionally requires the first selected target to remain living.',
'HitThreeTimesPowersUpWithEachHit.pbOnStartUse':'Set accumulated base power to zero and snapshot whether active Skill Link suppresses the later-hit accuracy checks.',
'HitTwoToFiveTimes.pbNumHits':'One uniform20-slot draw is made first, with slots0–6/7–13/14–16/17–19 producing2/3/4/5. Active Skill Link then overrides selection to the final5-hit slot.',
'HitOncePerUserTeamMember.pbMoveFailed?':'Snapshot the owner team in party order, keeping able real-status-free members including user; reject with feedback when the list is empty. This does not use partner-trainer members.',
'HitOncePerUserTeamMember.pbBaseDamage':'Consume the next snapshotted team member and use its species base Attack integer tenth plus5 as this evaluation’s base power; ordinary attacker inputs remain the user.',
'TwoTurnAttackInvulnerableInSkyTargetCannotAct.pbFailsAgainstTarget?':'Local target gate rejects same side, non-bypassed substitute, generation6+ weight at least2000 units, semi-invulnerability, existing carried-source linkage on charge, and a different carried-source linkage on attack; earlier charging shortcut can bypass this local gate.',
'TwoTurnAttackInvulnerableInSkyTargetCannotAct.pbEffectAfterAllHits':'Attack-phase after-hit callback clears target carried-source linkage to−1 even if that target was marked unaffected.',
'MultiTurnAttackBideThenReturnDoubleDamage.pbMoveFailed?':'Release-phase count1 rejects zero accumulated loss or empty targets and clears only the main count0 locally; charging uses are not rejected by this local check.',
'MultiTurnAttackBideThenReturnDoubleDamage.pbEffectGeneral':'If count is zero, initialize count3, loss0 and source−1 and remember current move, then decrement the main count. Reached main-effect invocations determine how often this occurs.',
'HealUserDependingOnWeather.pbOnStartUse':'Snapshot nearest two-thirdsHP under effective sun/harsh sun, nearest half under none/strong winds, nearest quarter under other effective weather; later healing returns the stored amount.',
'HealUserByTargetAttackLowerTargetAttack1.pbEffectAgainstTarget':'Snapshot floor of target raw Attack times Attack-stage factor before attempting Attack−1. Liquid Ooze requests direct user loss and an HP-item check; otherwise a currently healable user requests snapshot healing, amplified by active Big Root with floor after1.3.',
'HealUserAndAlliesQuarterOfTotalHPCureStatus.pbEffectAgainstTarget':'If the target can heal, request its integer totalHP quarter and give restored feedback; then cure any real status and show status-specific feedback. The two components are individually optional.',
'UserLosesHalfOfTotalHP.pbEffectAfterAllHits':'For each original target whose after-hit callback is reached, current user indirect-damage eligibility gates ceiling(totalHP/2), minimum1, followed by recoil feedback and HP-item check; no target-unaffected check.',
'UserFaintsExplosive.pbSelfKO':'If user currentHP is positive, request all currentHP loss, then HP-item check. The actual caller runs after target damage commits and formally faints user immediately afterward.',
'StartPerishCountsForAllBattlers.pbShowAnimation':'Use normal move animation then show a three-turn remaining-perish countdown statement; count4 is initialized earlier and consumed by reached end-round phases.'}
for x in a:
 if x['unit'] in over:x['fact']=over[x['unit']]
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in a))
print('Refined17 method facts and9 clause/metadata evidence entries.')
