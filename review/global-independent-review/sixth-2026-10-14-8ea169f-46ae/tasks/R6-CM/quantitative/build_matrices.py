from pathlib import Path
import re,json
OUT=Path(__file__).parent
ROOT=Path.cwd()
B='reference/pokemon-essentials/Data/Scripts/011_Battle/'
SPEC='deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md'
COV='deliverables/final-specification-set/pokemon-rules/wp46-damage-healing-coverage.md'
def ref(path,a,z=None):return {'path':path,'lines':[a,z or a]}
U=B+'002_Battler/007_Battler_UseMove.rb'; CAL=B+'003_Move/003_Move_UsageCalculations.rb'; BASE=B+'003_Move/004_Move_BaseEffects.rb'; SUC=B+'002_Battler/009_Battler_UseMoveSuccessChecks.rb'; TARGET=B+'002_Battler/008_Battler_UseMoveTargeting.rb'; HP=B+'002_Battler/003_Battler_ChangeSelf.rb'; ITEM=B+'002_Battler/006_Battler_AbilityAndItem.rb'; EOR=B+'001_Battle/011_Battle_EndOfRoundPhase.rb'
# Independently authored behavioral descriptions, checked against the complete files.
FACTS={
'HitTwoTimes':(51,'Two planned hits; the second skips ordinary accuracy.'),
'HitTwoTimesPoisonTarget':(52,'Two planned hits, with the ordinary poison additional-effect request on each reached hit.'),
'HitTwoTimesFlinchTarget':(53,'Two planned hits with native flinch additional effects; no redundant item-flinch chance.'),
'HitTwoTimesTargetThenTargetAlly':(62,'One outer planned hit, a recursive second volley, eligible ally expansion, per-volley target designation and failure-message gating.'),
'HitThreeTimesPowersUpWithEachHit':(54,'Three planned hits; successive base-power evaluations accumulate P,2P,3P for the ordinary one-target case; Skill Link is snapshotted for per-hit accuracy.'),
'HitThreeTimesAlwaysCriticalHit':(55,'Three planned hits and an always-critical request subject to earlier critical-immunity gates.'),
'HitTwoToFiveTimes':(56,'Draw one uniform integer among 20 slots, map to 2/3/4/5 with 7/7/3/3 slots; Skill Link still draws then selects 5.'),
'HitTwoToFiveTimesOrThreeForAshGreninja':(57,'Greninja form 2 selects three hits and base 20 without requiring a fresh Battle Bond check; other forms use the parent distribution.'),
'HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1':(58,'After all hits on an affected target, request Defense minus one before Speed plus one, each with separate eligibility.'),
'HitOncePerUserTeamMember':(59,'Snapshot all able real-status-free members in the owner team, including the user; consume one species base-Attack input per hit, with power 5 plus its integer tenth.'),
'AttackAndSkipNextTurn':(87,'Reached global main effect establishes recharge 2 and remembers this move.'),
'TwoTurnAttack':(72,'Ordinary charge message; common two-turn behavior supplies charge then attack.'),
'TwoTurnAttackOneTurnInSun':(73,'Initial effective sun permits charge and attack together without consuming Power Herb; nonempty nonsunny weather halves power multiplier.'),
'TwoTurnAttackParalyzeTarget':(74,'Attack hit additional effect requests paralysis, excluding an absorbed substitute hit.'),
'TwoTurnAttackBurnTarget':(74,'Attack hit additional effect requests burn, excluding an absorbed substitute hit.'),
'TwoTurnAttackFlinchTarget':(75,'Attack hit additional effect requests flinch, marks native flinch, and does not apply on the charging-only turn.'),
'TwoTurnAttackRaiseUserSpAtkSpDefSpd2':(76,'Stored charge bypasses the local maximum-stage failure check; damage-phase global effect requests Special Attack, Special Defense, Speed plus two in that order.'),
'TwoTurnAttackChargeRaiseUserDefense1':(77,'Charge effect requests Defense plus one; a later target failure does not undo it.'),
'TwoTurnAttackChargeRaiseUserSpAtk1':(77,'Charge effect requests Special Attack plus one; a later target failure does not undo it.'),
'TwoTurnAttackInvulnerableUnderground':(78,'Underground charging identity and corresponding charge feedback; caller controls semi-invulnerability.'),
'TwoTurnAttackInvulnerableUnderwater':(78,'Underwater charging identity and corresponding charge feedback; caller controls semi-invulnerability.'),
'TwoTurnAttackInvulnerableInSky':(79,'Air charging identity is unusable in gravity; caller controls semi-invulnerability.'),
'TwoTurnAttackInvulnerableInSkyParalyzeTarget':(79,'Air charging identity is unusable in gravity and requests paralysis on an attack hit excluding substitute.'),
'TwoTurnAttackInvulnerableInSkyTargetCannotAct':(80,'Sky Drop excludes Power Herb, has opposing/substitute/weight/semi-invulnerable/link guards, Flying-type immunity, source linkage on charge and attack-after-hits linkage clearing.'),
'TwoTurnAttackInvulnerableRemoveProtections':(81,'Disappearing charge identity; reached attack main effect removes the named target and target-side protections, excluding Endure.'),
'MultiTurnAttackPreventSleeping':(88,'First reached global effect sets Uproar 3 and wakes living real sleepers lacking active Soundproof in speed order; positive existing duration is not refreshed.'),
'MultiTurnAttackConfuseUserAtEnd':(89,'On first affected target draw duration 2 or 3, then decrement after each use; zero duration requests self-confusion if allowed.'),
'MultiTurnAttackPowersUpEachTurn':(90,'One hit per use; base power advances through five doubling steps, doubled again by Defense Curl; after-hit duration establishes 5 then decrements.'),
'MultiTurnAttackBideThenReturnDoubleDamage':(91,'Charge begins at 3 and decrements in main effects; release at 1 uses twice accumulated hit losses and recent-source target or uniform opposing fallback, rejecting zero accumulation/no target.'),
'HealUserFullyAndFallAsleep':(212,'Reject counted sleep, ineligible self-sleep and full HP; submit sleep duration 3 before healing all missing HP.'),
'HealUserHalfOfTotalHP':(213,'Request nearest-integer half of user total HP.'),
'HealUserDependingOnWeather':(214,'Snapshot weather-dependent requested healing during initialization: sunny two thirds, none/strong winds half, others quarter, all nearest integer.'),
'HealUserDependingOnSandstorm':(215,'Evaluate sandstorm at requested-healing query: nearest two thirds, otherwise nearest half.'),
'HealUserHalfOfTotalHPLoseFlyingTypeThisTurn':(216,'Nearest-half healing precedes the temporary Roost flag.'),
'CureTargetStatusHealUserHalfOfTotalHP':(217,'Cannot be snatched but can reflect; reject target with no real status; cure target before global nearest-half user recovery; inherited full-user-HP rejection still applies.'),
'HealUserByTargetAttackLowerTargetAttack1':(218,'Reject appropriate Attack boundary; snapshot floor of target staged Attack, attempt Attack minus one, then Liquid Ooze damage or eligible user healing with Big Root floor amplification.'),
'HealUserByHalfOfDamageDone':(228,'Positive per-hit actual loss gives nearest half drain; tagged healing only from generation six.'),
'HealUserByHalfOfDamageDoneIfTargetAsleep':(228,'Require target counted asleep, then positive per-hit loss gives nearest half drain; tagged healing only from generation six.'),
'HealUserByThreeQuartersOfDamageDone':(228,'Positive per-hit loss gives nearest three-quarter drain; tagged healing only from generation six.'),
'HealUserAndAlliesQuarterOfTotalHP':(219,'At least one same-side healable battler is required; each healable target requests integer quarter total HP.'),
'HealUserAndAlliesQuarterOfTotalHPCureStatus':(220,'At least one ally can heal or has real status; per target heal if eligible then cure real status.'),
'HealTargetHalfOfTotalHP':(221,'Reflectable targeted healing rejects full HP then general inability to heal; nearest half, or nearest three quarters for a Pulse move with Mega Launcher.'),
'HealTargetDependingOnGrassyTerrain':(222,'Reflectable targeted healing rejects full HP then general inability to heal; current Grassy Terrain gives nearest two thirds without grounding checks, otherwise nearest half.'),
'HealUserPositionNextTurn':(236,'Reject existing positive Wish; otherwise remember duration 2, nearest half source total HP and source party identity on the position.'),
'StartHealUserEachTurn':(237,'Reject duplicate Aqua Ring, otherwise establish it; later end-round consumer handles healing.'),
'StartHealUserEachTurnTrapUserInBattle':(238,'Reject duplicate Ingrain, otherwise establish it; grounding/trapping and end-round healing are separate consumers.'),
'StartDamageTargetEachTurnIfTargetAsleep':(239,'Require counted target sleep and no existing Nightmare, then establish the residual flag.'),
'StartLeechSeedTarget':(240,'Reflectable; reject existing seed linkage or Grass target; establish beneficiary position and special missed-target feedback.'),
'UserLosesHalfOfTotalHP':(261,'Per-original-target after-hit callback requests ceiling half user total HP if indirect damage is allowed, without target-unaffected guard, then checks healing item.'),
'UserLosesHalfOfTotalHPExplosive':(262,'Allows no targets but fails at active Damp unless Mold Breaker; first-hit self-loss requests nearest half total HP if indirect damage is allowed.'),
'UserFaintsExplosive':(263,'Allows no targets, forces one hit, fails at active Damp unless Mold Breaker; reached first-hit self-KO loses current full HP after target HP submission.'),
'UserFaintsPowersUpInMistyTerrainExplosive':(264,'Same explosion behavior, with integer three-half base power in stored Misty Terrain without grounding.'),
'UserFaintsFixedDamageUserHP':(109,'Snapshot user current HP at start; force one hit and fixed snapshot damage; reached first-hit self-KO loses current full HP.'),
'UserFaintsLowerTargetAtkSpAtk2':(266,'Local target gate does not reject impossible stat lowering; reached self-KO loses all current HP before ordered Attack and Special Attack minus two requests.'),
'UserFaintsHealAndCureReplacement':(267,'Healable/snatchable action requires an eligible nonactive replacement; reached self-KO loses full current HP then sets position Healing Wish.'),
'UserFaintsHealAndCureReplacementRestorePP':(267,'Healable/snatchable action requires an eligible nonactive replacement; reached self-KO loses full current HP then sets position Lunar Dance.'),
'StartPerishCountsForAllBattlers':(268,'Reject if all target durations already positive; each new target gets count 4 and source identity; completion shows the three-turn countdown feedback.'),
'AttackerFaintsIfUserFaints':(269,'Generation seven and later reject immediately repeated Destiny Bond; reached global effect establishes current flag.'),
'SetAttackerMovePPTo0IfUserFaints':(270,'Reached global effect establishes Grudge; actual hit caller clears attacking move PP only for opposing lethal hit.'),
}
CONSUMERS={
'multiHitMove?':[ref(B+'003_Move/002_Move_Usage.rb',319,325),ref(U,439,453)],
'pbNumHits':[ref(U,403,429)],'pbRepeatHit?':[ref(U,603,615),ref(U,755,759)],
'pbModifyTargets':[ref(TARGET,96,102)],'pbShowFailMessages?':[ref(SUC,303,304)],
'pbDesignateTargetsForHit':[ref(U,619,621)],'successCheckPerHit?':[ref(U,590,617)],
'pbOnStartUse':[ref(U,302,304)],'pbBaseDamage':[ref(CAL,250,280)],
'pbCritialOverride':[ref(CAL,178,219)],'pbEffectAfterAllHits':[ref(U,499,503)],
'pbMoveFailed?':[ref(U,294,301)],'pbEffectGeneral':[ref(U,703,711)],
'pbIsChargingTurn?':[ref(U,220,227)],'pbChargingTurnMessage':[ref(BASE,329,334),ref(BASE,356,361)],
'pbBaseDamageMultiplier':[ref(CAL,480,483)],'pbAdditionalEffect':[ref(U,712,719)],
'flinchingMove?':[ref(CAL,503,513)],'initialize':[ref(B+'003_Move/001_Battle_Move.rb',55,74)],
'pbChargingTurnEffect':[ref(BASE,329,334),ref(BASE,370,375)],'unusableInGravity?':[ref(SUC,27,33)],
'pbFailsAgainstTarget?':[ref(SUC,303,312)],'pbCalcTypeMod':[ref(SUC,303,308)],
'pbAttackingTurnMessage':[ref(BASE,356,361)],'pbAttackingTurnEffect':[ref(BASE,370,375)],
'pbAddTarget':[ref(TARGET,86,90)],'pbDisplayUseMessage':[ref(U,283,288)],
'pbDamagingMove?':[ref(U,624,637),ref(U,660,682)],
'pbFixedDamage':[ref(BASE,287,294)],'pbShowAnimation':[ref(U,638,639)],
'pbHealAmount':[ref(BASE,407,410)],'canSnatch?':[ref(TARGET,9,30)],
'canMagicCoat?':[ref(SUC,434,447)],'pbEffectAgainstTarget':[ref(U,704,708)],
'healingMove?':[ref(SUC,19,25)],'pbMissMessage':[ref(SUC,586,592)],
'worksWithNoTargets?':[ref(U,369,375),ref(U,602,615)],'pbSelfKO':[ref(U,660,675)]}
ROLE={'pbNumHits':'Planned hit count','multiHitMove?':'Multi-hit feedback classification','pbRepeatHit?':'Second-volley eligibility','pbModifyTargets':'Target expansion','pbShowFailMessages?':'Failure feedback gating','pbDesignateTargetsForHit':'Per-volley target selection','successCheckPerHit?':'Per-hit accuracy switch','pbOnStartUse':'Use-initialization snapshot','pbBaseDamage':'Base-power query','pbCritialOverride':'Critical-hit request','pbEffectAfterAllHits':'Reached after-hit state/output','pbMoveFailed?':'Whole-use local failure check','pbEffectGeneral':'Reached global main-effect state/output','pbIsChargingTurn?':'Charge/attack mode determination','pbChargingTurnMessage':'Charging feedback','pbBaseDamageMultiplier':'Move-specific power-multiplier tail','pbAdditionalEffect':'Reached additional-effect request','flinchingMove?':'Native-flinch classification','initialize':'Local ordered stat requests','pbChargingTurnEffect':'Reached charge effect','unusableInGravity?':'Gravity usability classification','pbFailsAgainstTarget?':'Target-local failure check','pbCalcTypeMod':'Type-effectiveness override','pbAttackingTurnMessage':'Attack/release feedback','pbAttackingTurnEffect':'Reached attack effect','pbAddTarget':'Stored-source release targeting','pbDisplayUseMessage':'Use-message selection','pbDamagingMove?':'Whether this use commits ordinary damage','pbFixedDamage':'Fixed calculation damage query','pbShowAnimation':'Use animation variant','pbHealAmount':'Healing request quantum','canSnatch?':'Snatch eligibility','canMagicCoat?':'Reflection eligibility','pbEffectAgainstTarget':'Reached target main effect','healingMove?':'Heal Block usage classification','pbMissMessage':'Miss feedback','worksWithNoTargets?':'Empty-target eligibility','pbSelfKO':'Reached first-hit self-loss'}
forward=[]
for file in ['009_MoveEffects_MultiHit.rb','010_MoveEffects_Healing.rb']:
 path=B+'003_Move/'+file;a=(ROOT/path).read_text().splitlines();starts=[i for i,x in enumerate(a) if x.startswith('class ')]
 for k,start in enumerate(starts):
  end=(starts[k+1] if k+1<len(starts) else len(a));name=re.search(r'class Battle::Move::(\w+)',a[start])[1];line,fact=FACTS[name]
  last=max(i for i in range(start,end) if a[i].strip() and not a[i].startswith('#'))
  methods=[i for i in range(start,last+1) if a[i].startswith('  def ')];attrs=[i for i in range(start,last+1) if a[i].startswith('  attr_')]
  forward.append({'unit_kind':'class','source':ref(path,start+1,last+1),'unit':name,'fact':fact,'consumers':[ref(U,294,304),ref(U,403,429),ref(U,583,760)],'formal':[ref(SPEC,line)],'status':'STATIC_MATCH','evidence':'static_read','runtime':'NOT_EXECUTED'})
  for m,idx in enumerate(methods):
   method=re.search(r'  def ([^ (;]+)',a[idx])[1];stop=(methods[m+1]-1 if m+1<len(methods) else last-1)
   if ';' in a[idx] and re.search(r';\s*end',a[idx]):stop=idx
   while stop>idx and (not a[stop].strip() or a[stop].startswith('#')):stop-=1
   forward.append({'unit_kind':'method','source':ref(path,idx+1,stop+1),'unit':name+'.'+method,'fact':ROLE[method]+': '+fact,'consumers':CONSUMERS[method],'formal':[ref(SPEC,line)],'status':'STATIC_MATCH','evidence':'static_read','runtime':'NOT_EXECUTED'})
  for idx in attrs:
   forward.append({'unit_kind':'inspection_metadata','source':ref(path,idx+1),'unit':name+'.stat-request-exposure','fact':'Exposes the configured ordered stat requests to inspection; this declaration alone changes no game state. '+fact,'consumers':[ref(path,methods[0]+1,last+1)],'formal':[ref(SPEC,line)],'status':'AUDIT_METADATA_NO_ADDITIONAL_BEHAVIOR','evidence':'static_read'})
with (OUT/'forward-matrix.jsonl').open('w') as f:
 for x in forward:f.write(json.dumps(x,ensure_ascii=False)+'\n')
# Build class source lookup only from files/ranges read freshly. These are audit identifiers, not proposed architecture.
classrefs={}
allowed={
'003_Move/009_MoveEffects_MultiHit.rb':[(1,633)],'003_Move/010_MoveEffects_Healing.rb':[(1,695)],'003_Move/008_MoveEffects_MoveAttributes.rb':[(1,1620)],'003_Move/005_MoveEffects_Misc.rb':[(1,300),(604,649)],'003_Move/012_MoveEffects_ChangeMoveEffect.rb':[(46,132),(381,426),(453,689)],'003_Move/006_MoveEffects_BattlerStats.rb':[(1899,1916)],'003_Move/007_MoveEffects_BattlerOther.rb':[(579,589)],'003_Move/004_Move_BaseEffects.rb':[(51,80)]}
for file,ranges in allowed.items():
 path=B+file;a=(ROOT/path).read_text().splitlines();starts=[i for i,x in enumerate(a) if x.startswith('class Battle::Move::')]
 for k,i in enumerate(starts):
  end=(starts[k+1] if k+1<len(starts) else len(a));last=max(j for j in range(i,end) if a[j].strip() and not a[j].startswith('#'))
  if not any(lo<=i+1 and last+1<=hi for lo,hi in ranges):continue
  name=re.search(r'class Battle::Move::(\w+)',a[i])[1];classrefs[name]=ref(path,i+1,last+1)
classrefs['AllBattlersLoseHalfHPUserSkipsNextTurn']=ref('reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb',330,348)
classrefs['UserLosesHalfHP']=ref('reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb',353,367)
# Additional evidence for prose clauses and combined rows. Exact behavioral ranges were read and checked.
EXTRA={17:[ref(U,154,375)],19:[ref(U,376,404),ref(SUC,303,525)],21:[ref(U,583,621)],23:[ref(U,622,754),ref(B+'002_Battler/010_Battler_UseMoveTriggerEffects.rb',1,218)],25:[ref(U,407,429),ref(U,499,520),ref(B+'002_Battler/010_Battler_UseMoveTriggerEffects.rb',87,218)],27:[ref(B+'003_Move/002_Move_Usage.rb',163,238),ref(U,621,636),ref(BASE,287,294)],31:[classrefs['TypeAndPowerDependOnUserBerry'],ref(U,583,758),ref(B+'007_Other battle code/009_Battle_ItemEffects.rb',1311,1331),ref(B+'007_Other battle code/009_Battle_ItemEffects.rb',364,387),ref(ITEM,212,243),ref(ITEM,315,323)],33:[classrefs['TypeAndPowerDependOnUserBerry'],ref(B+'003_Move/002_Move_Usage.rb',45,53),ref(ITEM,212,243)],39:[ref(B+'003_Move/002_Move_Usage.rb',184,238),ref(U,621,635),ref(BASE,421,430)],40:[ref(HP,5,34),ref(B+'002_Battler/001_Battle_Battler.rb',596,599)],41:[ref(B+'002_Battler/001_Battle_Battler.rb',518,533),ref(HP,37,52),ref(BASE,421,430)],42:[ref(U,75,95),ref(U,154,207)],43:[ref(U,439,453)],60:[ref(B+'003_Move/002_Move_Usage.rb',45,53),ref(U,588,589),ref(CAL,339,342),ref(BASE,287,294)],66:[ref(BASE,300,389)],68:[ref(BASE,300,389),ref(U,220,227),ref(U,364,365),ref(SUC,303,310),ref(SUC,532,539)],95:[ref(BASE,287,294),ref(B+'003_Move/002_Move_Usage.rb',163,238),ref(SUC,303,580)],105:[classrefs['OHKOIce'],ref(B+'007_Other battle code/006_Battle_Clauses.rb',192,221)],111:[ref(B+'003_Move/002_Move_Usage.rb',368,404),ref(EOR,713,760)],113:[classrefs['DamageTargetAlly'],ref(U,677,701)],117:[ref(U,179,301)],131:[ref(CAL,239,484)],158:[classrefs['DoublePowerIfTargetAsleepCureTarget'],classrefs['DoublePowerIfTargetParalyzedCureTarget']],159:[classrefs['DoublePowerIfTargetPoisoned'],classrefs['DoublePowerIfTargetStatusProblem']],178:[classrefs['EffectivenessIncludesFlyingType'],ref(CAL,32,78)],180:[classrefs['CategoryDependsOnHigherDamagePoisonTarget'],ref(B+'002_Battler/001_Battle_Battler.rb',91,103)],182:[classrefs['CategoryDependsOnHigherDamageIgnoreTargetAbility']],184:[classrefs[x] for x in ['UseUserDefenseInsteadOfUserAttack','UseTargetAttackInsteadOfUserAttack','UseTargetDefenseInsteadOfTargetSpDef']]+[ref(CAL,250,484)],188:[classrefs['UserAddStockpileRaiseDefSpDef1'],ref(B+'002_Battler/005_Battler_StatStages.rb',5,67)],190:[classrefs['PowerDependsOnUserStockpile']],192:[classrefs['HealUserDependingOnUserStockpile'],ref(SUC,19,25),ref(HP,23,34)],194:[ref(BASE,530,591)],198:[classrefs['GrassPledge'],classrefs['FirePledge']],199:[classrefs['FirePledge'],classrefs['WaterPledge']],200:[classrefs['WaterPledge'],classrefs['GrassPledge']],202:[ref(BASE,567,619),ref(EOR,135,151),ref(EOR,401,431)],208:[ref(BASE,394,411),ref(SUC,19,25)],228:[classrefs[x] for x in ['HealUserByHalfOfDamageDone','HealUserByHalfOfDamageDoneIfTargetAsleep','HealUserByThreeQuartersOfDamageDone']],230:[ref(HP,37,52),ref(B+'002_Battler/001_Battle_Battler.rb',344,355),ref(U,683,711)],237:[classrefs['StartHealUserEachTurn'],ref(EOR,169,178)],238:[classrefs['StartHealUserEachTurnTrapUserInBattle'],ref(EOR,179,187),ref(B+'002_Battler/001_Battle_Battler.rb',611,620)],239:[classrefs['StartDamageTargetEachTurnIfTargetAsleep'],ref(EOR,257,265)],240:[classrefs['StartLeechSeedTarget'],ref(EOR,188,201),ref(HP,37,62)],241:[classrefs['AttackTwoTurnsLater'],ref(EOR,78,115),ref(B+'002_Battler/002_Battler_Initialize.rb',5,58),ref(B+'002_Battler/002_Battler_Initialize.rb',150,279)],245:[classrefs['UserTargetAverageHP'],ref('reference/pokemon-essentials/PBS/moves.txt',6214,6223)],247:[classrefs['UserTargetAverageHP'],ref(HP,5,34),ref(SUC,19,25),ref(SUC,518,524)],249:[classrefs['UserTargetAverageHP'],ref(HP,5,34),ref(ITEM,315,323),ref(B+'002_Battler/001_Battle_Battler.rb',107,110)],251:[classrefs['UserTargetAverageHP'],ref(HP,5,34)],257:[classrefs[x] for x in ['RecoilQuarterOfDamageDealt','RecoilThirdOfDamageDealt','RecoilHalfOfDamageDealt']]+[ref(BASE,417,430)],258:[classrefs[x] for x in ['RecoilThirdOfDamageDealtParalyzeTarget','RecoilThirdOfDamageDealtBurnTarget']]+[ref(BASE,417,430)],263:[classrefs['UserFaintsExplosive'],ref(U,658,675)],265:[classrefs['UserFaintsFixedDamageUserHP'],ref(U,658,675)],266:[classrefs['UserFaintsLowerTargetAtkSpAtk2'],ref(BASE,238,281),ref(U,667,711)],267:[classrefs[x] for x in ['UserFaintsHealAndCureReplacement','UserFaintsHealAndCureReplacementRestorePP']]+[ref(B+'001_Battle/005_Battle_ActionSwitching.rb',394,422)],268:[classrefs['StartPerishCountsForAllBattlers'],ref(EOR,370,389)],269:[classrefs['AttackerFaintsIfUserFaints'],ref(U,61,65),ref(B+'002_Battler/010_Battler_UseMoveTriggerEffects.rb',76,80),ref(B+'002_Battler/010_Battler_UseMoveTriggerEffects.rb',100,110)],270:[classrefs['SetAttackerMovePPTo0IfUserFaints'],ref(U,61,65),ref(B+'002_Battler/010_Battler_UseMoveTriggerEffects.rb',70,75),ref(HP,104,111)],278:[classrefs['AllBattlersLoseHalfHPUserSkipsNextTurn'],ref(B+'001_Battle/001_Battle.rb',448,450),ref(EOR,713,725)],279:[classrefs['UserLosesHalfHP'],ref(U,499,505)],281:[ref(HP,5,34),ref(B+'002_Battler/001_Battle_Battler.rb',107,110)],283:[classrefs['AllBattlersLoseHalfHPUserSkipsNextTurn'],classrefs['UserLosesHalfHP'],ref(HP,5,34)],287:[ref('reference/pokemon-essentials/Data/Scripts/001_Settings.rb',17),ref('reference/pokemon-essentials/Data/Scripts/002_BattleSettings.rb',35,77),ref('reference/pokemon-essentials/PBS/moves.txt',2243,2253),ref('reference/pokemon-essentials/PBS/moves.txt',1039,1049),ref('reference/pokemon-essentials/PBS/moves.txt',1076,1086),ref('reference/pokemon-essentials/PBS/moves.txt',632,642),ref('reference/pokemon-essentials/PBS/moves.txt',5593,5603),ref('reference/pokemon-essentials/PBS/moves.txt',53,63),ref('reference/pokemon-essentials/PBS/moves.txt',7620,7628),ref('reference/pokemon-essentials/PBS/moves.txt',4562,4572),ref('reference/pokemon-essentials/PBS/moves.txt',2268,2278),ref('reference/pokemon-essentials/PBS/moves.txt',2426,2436),ref('reference/pokemon-essentials/PBS/moves.txt',7955,7965),ref('reference/pokemon-essentials/PBS/moves.txt',3508,3518),ref('reference/pokemon-essentials/PBS/moves.txt',8639,8650),ref('reference/pokemon-essentials/PBS/moves.txt',1633,1643)],297:[classrefs['HitOncePerUserTeamMember'],classrefs['HitTwoTimesTargetThenTargetAlly'],classrefs['PowerDependsOnUserStockpile'],ref(BASE,593,619)]}
# Defaults for combined identities occur in some rows whose spelling abbreviates a shared prefix.
EXTRA[74]=[classrefs['TwoTurnAttackParalyzeTarget'],classrefs['TwoTurnAttackBurnTarget']]
EXTRA[77]=[classrefs['TwoTurnAttackChargeRaiseUserDefense1'],classrefs['TwoTurnAttackChargeRaiseUserSpAtk1']]
EXTRA[78]=[classrefs['TwoTurnAttackInvulnerableUnderground'],classrefs['TwoTurnAttackInvulnerableUnderwater'],ref(SUC,549,567)]
EXTRA[79]=[classrefs['TwoTurnAttackInvulnerableInSky'],classrefs['TwoTurnAttackInvulnerableInSkyParalyzeTarget'],ref(SUC,27,33)]
EXTRA[140]=[classrefs['PowerHigherWithUserHappiness'],classrefs['PowerLowerWithUserHappiness']]
EXTRA[99]=[classrefs['FixedDamage20'],classrefs['FixedDamage40']]
EXTRA[107]=[classrefs['CounterPhysicalDamage'],classrefs['CounterSpecialDamage']]
reverse=[]
for path in [SPEC,COV]:
 lines=(ROOT/path).read_text().splitlines()
 for i,text in enumerate(lines,1):
  if not text.strip() or text.startswith('#') or re.fullmatch(r'\|[ |:-]+\|',text):continue
  if text.startswith('|') and i in ([49,70,85,97,119,135,154,196,210,234,255,276] if path==SPEC else [45]):continue
  ids=[x for x in classrefs if re.search(r'(?<![A-Za-z])'+re.escape(x)+r'(?![A-Za-z])',text)]
  evidence=[classrefs[x] for x in ids]
  if path==SPEC:evidence+=EXTRA.get(i,[])
  dedup={json.dumps(x,sort_keys=True):x for x in evidence};evidence=list(dedup.values())
  if path==SPEC:
   kind='behavioral_clause' if evidence else 'scope_notation_dependency_or_editorial'
   status='STATIC_MATCH' if evidence else 'EDITORIAL_OR_DELEGATED_NOT_BEHAVIOR_ASSERTION'
  else:
   # Domain-outside lists are attribution inventories, never a claim of fresh source validation.
   kind='identity_attribution_inventory' if '`' in text else 'coverage_scope_note'
   status='IDENTITY_MATCH_FOR_FRESH_READ_SUBSET' if evidence else 'EDITORIAL_OR_OUT_OF_PARTITION'
  reverse.append({'formal':ref(path,i),'kind':kind,'identities':ids,'source_evidence':evidence,'evidence':'static_read' if evidence else 'formal_text_only','status':status,'note':'Exact row read. Supplemental sources are evidence of this clause only; no unread file-wide coverage claimed.','runtime':'NOT_EXECUTED'})
with (OUT/'reverse-matrix.jsonl').open('w') as f:
 for x in reverse:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print(json.dumps({'forward_records':len(forward),'reverse_records':len(reverse),'owned_classes':len(FACTS),'owned_methods':sum(x['unit_kind']=='method' for x in forward),'inspection_metadata':sum(x['unit_kind']=='inspection_metadata' for x in forward),'class_refs':len(classrefs)},indent=2))
