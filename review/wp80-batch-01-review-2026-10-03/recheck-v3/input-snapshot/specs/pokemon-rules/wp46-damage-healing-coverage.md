# WP46 有界效果覆盖与责任表 v1

状态：Reviewed（限定静态范围，2026-09-27首审PASS_SCOPED；管理性回填）。本表按行为合同归属，不建议未来类层级。主文见[WP46](wp46-damage-multihit-and-healing.md)。固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

## 1. 本包实际合同

139项审计身份，每项具体条件／量／阶段／失败结果在主文指定节；共享基底／继承只用于定位，不能从名字推导未写算法。来源均在`Data/Scripts/011_Battle/003_Move/`。

| 效果身份 | 文件与行 | 主合同 | 共享范围 |
| --- | --- | --- | --- |
| `Struggle` | `004_Move_BaseEffects.rb`:51 | WP46 §7 | 本包主合同 |
| `FailsIfNotUserFirstTurn` | `005_MoveEffects_Misc.rb`:75 | WP46 §4 | 本包主合同 |
| `FailsIfUserHasUnusedMove` | `005_MoveEffects_Misc.rb`:88 | WP46 §4 | 本包主合同 |
| `FailsIfUserNotConsumedBerry` | `005_MoveEffects_Misc.rb`:109 | WP46 §4 | 本包主合同 |
| `FailsIfTargetHasNoItem` | `005_MoveEffects_Misc.rb`:134 | WP46 §4 | 本包主合同 |
| `FailsUnlessTargetSharesTypeWithUser` | `005_MoveEffects_Misc.rb`:148 | WP46 §4 | 本包主合同 |
| `FailsIfUserDamagedThisTurn` | `005_MoveEffects_Misc.rb`:169 | WP46 §4 | 本包主合同 |
| `FailsIfTargetActed` | `005_MoveEffects_Misc.rb`:193 | WP46 §4 | 本包主合同 |
| `CrashDamageIfFailsUnusableInGravity` | `005_MoveEffects_Misc.rb`:214 | WP46 §7 | 本包主合同 |
| `AttackTwoTurnsLater` | `005_MoveEffects_Misc.rb`:604 | WP46 §6 | 本包主合同 |
| `FlinchTargetDoublePowerIfTargetInSky` | `007_MoveEffects_BattlerOther.rb`:579 | WP46 §5 | 状态／阶级中央资格引用WP44；本包仅完整本族时点与数值 |
| `FixedDamage20` | `008_MoveEffects_MoveAttributes.rb`:4 | WP46 §4 | 本包主合同 |
| `FixedDamage40` | `008_MoveEffects_MoveAttributes.rb`:13 | WP46 §4 | 本包主合同 |
| `FixedDamageHalfTargetHP` | `008_MoveEffects_MoveAttributes.rb`:22 | WP46 §4 | 本包主合同 |
| `FixedDamageUserLevel` | `008_MoveEffects_MoveAttributes.rb`:31 | WP46 §4 | 本包主合同 |
| `FixedDamageUserLevelRandom` | `008_MoveEffects_MoveAttributes.rb`:40 | WP46 §4 | 本包主合同 |
| `LowerTargetHPToUserHP` | `008_MoveEffects_MoveAttributes.rb`:51 | WP46 §4 | 本包主合同 |
| `OHKO` | `008_MoveEffects_MoveAttributes.rb`:70 | WP46 §4 | 本包主合同 |
| `OHKOIce` | `008_MoveEffects_MoveAttributes.rb`:112 | WP46 §4 | 本包主合同 |
| `OHKOHitsUndergroundTarget` | `008_MoveEffects_MoveAttributes.rb`:132 | WP46 §4 | 本包主合同 |
| `DamageTargetAlly` | `008_MoveEffects_MoveAttributes.rb`:139 | WP46 §4 | 本包主合同 |
| `PowerHigherWithUserHP` | `008_MoveEffects_MoveAttributes.rb`:165 | WP46 §5 | 本包主合同 |
| `PowerLowerWithUserHP` | `008_MoveEffects_MoveAttributes.rb`:174 | WP46 §5 | 本包主合同 |
| `PowerHigherWithTargetHP` | `008_MoveEffects_MoveAttributes.rb`:196 | WP46 §5 | 本包主合同 |
| `PowerHigherWithUserHappiness` | `008_MoveEffects_MoveAttributes.rb`:205 | WP46 §5 | 本包主合同 |
| `PowerLowerWithUserHappiness` | `008_MoveEffects_MoveAttributes.rb`:214 | WP46 §5 | 本包主合同 |
| `PowerHigherWithUserPositiveStatStages` | `008_MoveEffects_MoveAttributes.rb`:224 | WP46 §5 | 本包主合同 |
| `PowerHigherWithTargetPositiveStatStages` | `008_MoveEffects_MoveAttributes.rb`:236 | WP46 §5 | 本包主合同 |
| `PowerHigherWithUserFasterThanTarget` | `008_MoveEffects_MoveAttributes.rb`:247 | WP46 §5 | 本包主合同 |
| `PowerHigherWithTargetFasterThanUser` | `008_MoveEffects_MoveAttributes.rb`:267 | WP46 §5 | 本包主合同 |
| `PowerHigherWithLessPP` | `008_MoveEffects_MoveAttributes.rb`:276 | WP46 §5 | 本包主合同 |
| `PowerHigherWithTargetWeight` | `008_MoveEffects_MoveAttributes.rb`:287 | WP46 §5 | 本包主合同 |
| `PowerHigherWithUserHeavierThanTarget` | `008_MoveEffects_MoveAttributes.rb`:309 | WP46 §5 | 本包主合同 |
| `PowerHigherWithConsecutiveUse` | `008_MoveEffects_MoveAttributes.rb`:329 | WP46 §5 | 本包主合同 |
| `PowerHigherWithConsecutiveUseOnUserSide` | `008_MoveEffects_MoveAttributes.rb`:349 | WP46 §5 | 本包主合同 |
| `RandomPowerDoublePowerIfTargetUnderground` | `008_MoveEffects_MoveAttributes.rb`:368 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetHPLessThanHalf` | `008_MoveEffects_MoveAttributes.rb`:401 | WP46 §5 | 本包主合同 |
| `DoublePowerIfUserPoisonedBurnedParalyzed` | `008_MoveEffects_MoveAttributes.rb`:412 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetAsleepCureTarget` | `008_MoveEffects_MoveAttributes.rb`:424 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetPoisoned` | `008_MoveEffects_MoveAttributes.rb`:444 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetParalyzedCureTarget` | `008_MoveEffects_MoveAttributes.rb`:458 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetStatusProblem` | `008_MoveEffects_MoveAttributes.rb`:478 | WP46 §5 | 本包主合同 |
| `DoublePowerIfUserHasNoItem` | `008_MoveEffects_MoveAttributes.rb`:491 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetUnderwater` | `008_MoveEffects_MoveAttributes.rb`:502 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetUnderground` | `008_MoveEffects_MoveAttributes.rb`:515 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetInSky` | `008_MoveEffects_MoveAttributes.rb`:529 | WP46 §5 | 本包主合同 |
| `DoublePowerInElectricTerrain` | `008_MoveEffects_MoveAttributes.rb`:544 | WP46 §5 | 本包主合同 |
| `DoublePowerIfUserLastMoveFailed` | `008_MoveEffects_MoveAttributes.rb`:554 | WP46 §5 | 本包主合同 |
| `DoublePowerIfAllyFaintedLastTurn` | `008_MoveEffects_MoveAttributes.rb`:564 | WP46 §5 | 本包主合同 |
| `DoublePowerIfUserLostHPThisTurn` | `008_MoveEffects_MoveAttributes.rb`:576 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetLostHPThisTurn` | `008_MoveEffects_MoveAttributes.rb`:586 | WP46 §5 | 本包主合同 |
| `DoublePowerIfUserStatsLoweredThisTurn` | `008_MoveEffects_MoveAttributes.rb`:596 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetActed` | `008_MoveEffects_MoveAttributes.rb`:606 | WP46 §5 | 本包主合同 |
| `DoublePowerIfTargetNotActed` | `008_MoveEffects_MoveAttributes.rb`:621 | WP46 §5 | 本包主合同 |
| `AlwaysCriticalHit` | `008_MoveEffects_MoveAttributes.rb`:634 | WP46 §5 | 本包主合同 |
| `CannotMakeTargetFaint` | `008_MoveEffects_MoveAttributes.rb`:675 | WP46 §5 | 本包主合同 |
| `RecoilQuarterOfDamageDealt` | `008_MoveEffects_MoveAttributes.rb`:1037 | WP46 §7 | 本包主合同 |
| `RecoilThirdOfDamageDealt` | `008_MoveEffects_MoveAttributes.rb`:1046 | WP46 §7 | 本包主合同 |
| `RecoilThirdOfDamageDealtParalyzeTarget` | `008_MoveEffects_MoveAttributes.rb`:1056 | WP46 §7 | 本包主合同 |
| `RecoilThirdOfDamageDealtBurnTarget` | `008_MoveEffects_MoveAttributes.rb`:1071 | WP46 §7 | 本包主合同 |
| `RecoilHalfOfDamageDealt` | `008_MoveEffects_MoveAttributes.rb`:1086 | WP46 §7 | 本包主合同 |
| `EffectivenessIncludesFlyingType` | `008_MoveEffects_MoveAttributes.rb`:1096 | WP46 §5 | 本包主合同 |
| `CategoryDependsOnHigherDamagePoisonTarget` | `008_MoveEffects_MoveAttributes.rb`:1112 | WP46 §5 | 本包主合同 |
| `CategoryDependsOnHigherDamageIgnoreTargetAbility` | `008_MoveEffects_MoveAttributes.rb`:1160 | WP46 §5 | 本包主合同 |
| `UseUserDefenseInsteadOfUserAttack` | `008_MoveEffects_MoveAttributes.rb`:1191 | WP46 §5 | 本包主合同 |
| `UseTargetAttackInsteadOfUserAttack` | `008_MoveEffects_MoveAttributes.rb`:1201 | WP46 §5 | 本包主合同 |
| `UseTargetDefenseInsteadOfTargetSpDef` | `008_MoveEffects_MoveAttributes.rb`:1212 | WP46 §5 | 本包主合同 |
| `HitTwoTimes` | `009_MoveEffects_MultiHit.rb`:4 | WP46 §3 | 本包主合同 |
| `HitTwoTimesPoisonTarget` | `009_MoveEffects_MultiHit.rb`:12 | WP46 §3 | 本包主合同 |
| `HitTwoTimesFlinchTarget` | `009_MoveEffects_MultiHit.rb`:20 | WP46 §3 | 本包主合同 |
| `HitTwoTimesTargetThenTargetAlly` | `009_MoveEffects_MultiHit.rb`:36 | WP46 §3 | 本包主合同 |
| `HitThreeTimesPowersUpWithEachHit` | `009_MoveEffects_MultiHit.rb`:69 | WP46 §3 | 本包主合同 |
| `HitThreeTimesAlwaysCriticalHit` | `009_MoveEffects_MultiHit.rb`:92 | WP46 §3 | 本包主合同 |
| `HitTwoToFiveTimes` | `009_MoveEffects_MultiHit.rb`:101 | WP46 §3 | 本包主合同 |
| `HitTwoToFiveTimesOrThreeForAshGreninja` | `009_MoveEffects_MultiHit.rb`:121 | WP46 §3 | 本包主合同 |
| `HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1` | `009_MoveEffects_MultiHit.rb`:137 | WP46 §3 | 本包主合同 |
| `HitOncePerUserTeamMember` | `009_MoveEffects_MultiHit.rb`:155 | WP46 §3 | 本包主合同 |
| `AttackAndSkipNextTurn` | `009_MoveEffects_MultiHit.rb`:185 | WP46 §3 | 本包主合同 |
| `TwoTurnAttack` | `009_MoveEffects_MultiHit.rb`:195 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackOneTurnInSun` | `009_MoveEffects_MultiHit.rb`:205 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackParalyzeTarget` | `009_MoveEffects_MultiHit.rb`:232 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackBurnTarget` | `009_MoveEffects_MultiHit.rb`:247 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackFlinchTarget` | `009_MoveEffects_MultiHit.rb`:262 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackRaiseUserSpAtkSpDefSpd2` | `009_MoveEffects_MultiHit.rb`:279 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackChargeRaiseUserDefense1` | `009_MoveEffects_MultiHit.rb`:322 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackChargeRaiseUserSpAtk1` | `009_MoveEffects_MultiHit.rb`:345 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackInvulnerableUnderground` | `009_MoveEffects_MultiHit.rb`:368 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackInvulnerableUnderwater` | `009_MoveEffects_MultiHit.rb`:378 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackInvulnerableInSky` | `009_MoveEffects_MultiHit.rb`:388 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackInvulnerableInSkyParalyzeTarget` | `009_MoveEffects_MultiHit.rb`:401 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackInvulnerableInSkyTargetCannotAct` | `009_MoveEffects_MultiHit.rb`:420 | WP46 §3 | 本包主合同 |
| `TwoTurnAttackInvulnerableRemoveProtections` | `009_MoveEffects_MultiHit.rb`:483 | WP46 §3 | 本包主合同 |
| `MultiTurnAttackPreventSleeping` | `009_MoveEffects_MultiHit.rb`:508 | WP46 §3 | 本包主合同 |
| `MultiTurnAttackConfuseUserAtEnd` | `009_MoveEffects_MultiHit.rb`:526 | WP46 §3 | 本包主合同 |
| `MultiTurnAttackPowersUpEachTurn` | `009_MoveEffects_MultiHit.rb`:545 | WP46 §3 | 本包主合同 |
| `MultiTurnAttackBideThenReturnDoubleDamage` | `009_MoveEffects_MultiHit.rb`:570 | WP46 §3 | 本包主合同 |
| `HealUserFullyAndFallAsleep` | `010_MoveEffects_Healing.rb`:4 | WP46 §6 | 本包主合同 |
| `HealUserHalfOfTotalHP` | `010_MoveEffects_Healing.rb`:28 | WP46 §6 | 本包主合同 |
| `HealUserDependingOnWeather` | `010_MoveEffects_Healing.rb`:38 | WP46 §6 | 本包主合同 |
| `HealUserDependingOnSandstorm` | `010_MoveEffects_Healing.rb`:58 | WP46 §6 | 本包主合同 |
| `HealUserHalfOfTotalHPLoseFlyingTypeThisTurn` | `010_MoveEffects_Healing.rb`:69 | WP46 §6 | 本包主合同 |
| `CureTargetStatusHealUserHalfOfTotalHP` | `010_MoveEffects_Healing.rb`:84 | WP46 §6 | 本包主合同 |
| `HealUserByTargetAttackLowerTargetAttack1` | `010_MoveEffects_Healing.rb`:111 | WP46 §6 | 本包主合同 |
| `HealUserByHalfOfDamageDone` | `010_MoveEffects_Healing.rb`:170 | WP46 §6 | 本包主合同 |
| `HealUserByHalfOfDamageDoneIfTargetAsleep` | `010_MoveEffects_Healing.rb`:184 | WP46 §6 | 本包主合同 |
| `HealUserByThreeQuartersOfDamageDone` | `010_MoveEffects_Healing.rb`:205 | WP46 §6 | 本包主合同 |
| `HealUserAndAlliesQuarterOfTotalHP` | `010_MoveEffects_Healing.rb`:218 | WP46 §6 | 本包主合同 |
| `HealUserAndAlliesQuarterOfTotalHPCureStatus` | `010_MoveEffects_Healing.rb`:243 | WP46 §6 | 本包主合同 |
| `HealTargetHalfOfTotalHP` | `010_MoveEffects_Healing.rb`:285 | WP46 §6 | 本包主合同 |
| `HealTargetDependingOnGrassyTerrain` | `010_MoveEffects_Healing.rb`:314 | WP46 §6 | 本包主合同 |
| `HealUserPositionNextTurn` | `010_MoveEffects_Healing.rb`:341 | WP46 §6 | 本包主合同 |
| `StartHealUserEachTurn` | `010_MoveEffects_Healing.rb`:364 | WP46 §6 | 本包主合同 |
| `StartHealUserEachTurnTrapUserInBattle` | `010_MoveEffects_Healing.rb`:385 | WP46 §6 | 本包主合同 |
| `StartDamageTargetEachTurnIfTargetAsleep` | `010_MoveEffects_Healing.rb`:405 | WP46 §6 | 本包主合同 |
| `StartLeechSeedTarget` | `010_MoveEffects_Healing.rb`:424 | WP46 §6 | 本包主合同 |
| `UserLosesHalfOfTotalHP` | `010_MoveEffects_Healing.rb`:454 | WP46 §7 | 本包主合同 |
| `UserLosesHalfOfTotalHPExplosive` | `010_MoveEffects_Healing.rb`:468 | WP46 §7 | 本包主合同 |
| `UserFaintsExplosive` | `010_MoveEffects_Healing.rb`:499 | WP46 §7 | 本包主合同 |
| `UserFaintsPowersUpInMistyTerrainExplosive` | `010_MoveEffects_Healing.rb`:532 | WP46 §7 | 本包主合同 |
| `UserFaintsFixedDamageUserHP` | `010_MoveEffects_Healing.rb`:543 | WP46 §7 | 本包主合同 |
| `UserFaintsLowerTargetAtkSpAtk2` | `010_MoveEffects_Healing.rb`:565 | WP46 §7 | 状态／阶级中央资格引用WP44；本包仅完整本族时点与数值 |
| `UserFaintsHealAndCureReplacement` | `010_MoveEffects_Healing.rb`:590 | WP46 §7 | 本包主合同 |
| `UserFaintsHealAndCureReplacementRestorePP` | `010_MoveEffects_Healing.rb`:614 | WP46 §7 | 本包主合同 |
| `StartPerishCountsForAllBattlers` | `010_MoveEffects_Healing.rb`:637 | WP46 §7 | 本包主合同 |
| `AttackerFaintsIfUserFaints` | `010_MoveEffects_Healing.rb`:671 | WP46 §7 | 本包主合同 |
| `SetAttackerMovePPTo0IfUserFaints` | `010_MoveEffects_Healing.rb`:690 | WP46 §7 | 本包主合同 |
| `RandomlyDamageOrHealTarget` | `012_MoveEffects_ChangeMoveEffect.rb`:46 | WP46 §6 | 本包主合同 |
| `HealAllyOrDamageFoe` | `012_MoveEffects_ChangeMoveEffect.rb`:93 | WP46 §6 | 本包主合同 |
| `DoublePowerAfterFusionFlare` | `012_MoveEffects_ChangeMoveEffect.rb`:381 | WP46 §5 | 本包主合同 |
| `DoublePowerAfterFusionBolt` | `012_MoveEffects_ChangeMoveEffect.rb`:406 | WP46 §5 | 本包主合同 |
| `CounterPhysicalDamage` | `012_MoveEffects_ChangeMoveEffect.rb`:453 | WP46 §4 | 本包主合同 |
| `CounterSpecialDamage` | `012_MoveEffects_ChangeMoveEffect.rb`:479 | WP46 §4 | 本包主合同 |
| `CounterDamagePlusHalf` | `012_MoveEffects_ChangeMoveEffect.rb`:505 | WP46 §4 | 本包主合同 |
| `UserAddStockpileRaiseDefSpDef1` | `012_MoveEffects_ChangeMoveEffect.rb`:532 | WP46 §5 | 本包主合同 |
| `PowerDependsOnUserStockpile` | `012_MoveEffects_ChangeMoveEffect.rb`:566 | WP46 §5 | 本包主合同 |
| `HealUserDependingOnUserStockpile` | `012_MoveEffects_ChangeMoveEffect.rb`:603 | WP46 §5 | 本包主合同 |
| `GrassPledge` | `012_MoveEffects_ChangeMoveEffect.rb`:654 | WP46 §5 | 本包主合同 |
| `FirePledge` | `012_MoveEffects_ChangeMoveEffect.rb`:668 | WP46 §5 | 本包主合同 |
| `WaterPledge` | `012_MoveEffects_ChangeMoveEffect.rb`:682 | WP46 §5 | 本包主合同 |

## 2. 同目录已定位的其它责任

这些行不计本包主合同数量。WP47-A/B将逐包阅读补合同；WP44/45已审范围仅引用，不冒称当前重读全部源文件；本表给出的源行可机械定位，不能当行为验收。

| 效果身份 | 文件与行 | 负责包／状态 | 主规则或移交 |
| --- | --- | --- | --- |
| `None` | `005_MoveEffects_Misc.rb`:4 | WP43 | 无额外效果的基础伤害，§3～7 |
| `DoesNothingCongratulations` | `005_MoveEffects_Misc.rb`:10 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `DoesNothingFailsIfNoAlly` | `005_MoveEffects_Misc.rb`:23 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `DoesNothingUnusableInGravity` | `005_MoveEffects_Misc.rb`:38 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `AddMoneyGainedFromBattle` | `005_MoveEffects_Misc.rb`:53 | WP47-B | 奖励标记／交换位置／行动准备；终局已有WP42 |
| `DoubleMoneyGainedFromBattle` | `005_MoveEffects_Misc.rb`:65 | WP47-B | 奖励标记／交换位置／行动准备；终局已有WP42 |
| `StartSunWeather` | `005_MoveEffects_Misc.rb`:231 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `StartRainWeather` | `005_MoveEffects_Misc.rb`:241 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `StartSandstormWeather` | `005_MoveEffects_Misc.rb`:251 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `StartHailWeather` | `005_MoveEffects_Misc.rb`:261 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `StartElectricTerrain` | `005_MoveEffects_Misc.rb`:273 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `StartGrassyTerrain` | `005_MoveEffects_Misc.rb`:292 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `StartMistyTerrain` | `005_MoveEffects_Misc.rb`:311 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `StartPsychicTerrain` | `005_MoveEffects_Misc.rb`:330 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `RemoveTerrain` | `005_MoveEffects_Misc.rb`:348 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `AddSpikesToFoeSide` | `005_MoveEffects_Misc.rb`:375 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `AddToxicSpikesToFoeSide` | `005_MoveEffects_Misc.rb`:397 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `AddStealthRocksToFoeSide` | `005_MoveEffects_Misc.rb`:418 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `AddStickyWebToFoeSide` | `005_MoveEffects_Misc.rb`:439 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `SwapSideEffects` | `005_MoveEffects_Misc.rb`:461 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `UserMakeSubstitute` | `005_MoveEffects_Misc.rb`:525 | WP47-B | 替身建立与代价／控制；吸收消费已有WP43 |
| `RemoveUserBindingAndEntryHazards` | `005_MoveEffects_Misc.rb`:558 | WP45 | 天气／场地／侧危害建立与清除，已有§3～8；招式交界本批核对 |
| `UserSwapsPositionsWithAlly` | `005_MoveEffects_Misc.rb`:654 | WP47-B | 奖励标记／交换位置／行动准备；终局已有WP42 |
| `BurnAttackerBeforeUserActs` | `005_MoveEffects_Misc.rb`:687 | WP47-B | 奖励标记／交换位置／行动准备；终局已有WP42 |
| `SleepTarget` | `007_MoveEffects_BattlerOther.rb`:4 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `SleepTargetIfUserDarkrai` | `007_MoveEffects_BattlerOther.rb`:26 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `SleepTargetChangeUserMeloettaForm` | `007_MoveEffects_BattlerOther.rb`:40 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `SleepTargetNextTurn` | `007_MoveEffects_BattlerOther.rb`:54 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `PoisonTarget` | `007_MoveEffects_BattlerOther.rb`:75 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `PoisonTargetLowerTargetSpeed1` | `007_MoveEffects_BattlerOther.rb`:102 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `BadPoisonTarget` | `007_MoveEffects_BattlerOther.rb`:132 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `ParalyzeTarget` | `007_MoveEffects_BattlerOther.rb`:146 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `ParalyzeTargetIfNotTypeImmune` | `007_MoveEffects_BattlerOther.rb`:169 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `ParalyzeTargetAlwaysHitsInRainHitsTargetInSky` | `007_MoveEffects_BattlerOther.rb`:183 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `ParalyzeFlinchTarget` | `007_MoveEffects_BattlerOther.rb`:200 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `BurnTarget` | `007_MoveEffects_BattlerOther.rb`:217 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `BurnTargetIfTargetStatsRaisedThisTurn` | `007_MoveEffects_BattlerOther.rb`:240 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `BurnFlinchTarget` | `007_MoveEffects_BattlerOther.rb`:249 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `FreezeTarget` | `007_MoveEffects_BattlerOther.rb`:266 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `FreezeTargetSuperEffectiveAgainstWater` | `007_MoveEffects_BattlerOther.rb`:288 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `FreezeTargetAlwaysHitsInHail` | `007_MoveEffects_BattlerOther.rb`:298 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `FreezeFlinchTarget` | `007_MoveEffects_BattlerOther.rb`:308 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `ParalyzeBurnOrFreezeTarget` | `007_MoveEffects_BattlerOther.rb`:325 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `GiveUserStatusToTarget` | `007_MoveEffects_BattlerOther.rb`:339 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `CureUserBurnPoisonParalysis` | `007_MoveEffects_BattlerOther.rb`:385 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `CureUserPartyStatus` | `007_MoveEffects_BattlerOther.rb`:420 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `CureTargetBurn` | `007_MoveEffects_BattlerOther.rb`:500 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `StartUserSideImmunityToInflictedStatus` | `007_MoveEffects_BattlerOther.rb`:512 | WP45 | WP45建立／期限；WP44免疫查询 |
| `FlinchTarget` | `007_MoveEffects_BattlerOther.rb`:532 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `FlinchTargetFailsIfUserNotAsleep` | `007_MoveEffects_BattlerOther.rb`:549 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `FlinchTargetFailsIfNotUserFirstTurn` | `007_MoveEffects_BattlerOther.rb`:565 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `ConfuseTarget` | `007_MoveEffects_BattlerOther.rb`:594 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `ConfuseTargetAlwaysHitsInRainHitsTargetInSky` | `007_MoveEffects_BattlerOther.rb`:618 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `AttractTarget` | `007_MoveEffects_BattlerOther.rb`:635 | WP44 | 已审状态／附效有界覆盖，主稿§3～7及覆盖附表 |
| `SetUserTypesBasedOnEnvironment` | `007_MoveEffects_BattlerOther.rb`:659 | WP47-A | 类型／属性改变，待本批后续包固定 |
| `SetUserTypesToResistLastAttack` | `007_MoveEffects_BattlerOther.rb`:721 | WP47-A | 类型／属性改变，待本批后续包固定 |
| `SetUserTypesToTargetTypes` | `007_MoveEffects_BattlerOther.rb`:762 | WP47-A | 类型／属性改变，待本批后续包固定 |
| `SetUserTypesToUserMoveType` | `007_MoveEffects_BattlerOther.rb`:799 | WP47-A | 类型／属性改变，待本批后续包固定 |
| `SetTargetTypesToPsychic` | `007_MoveEffects_BattlerOther.rb`:833 | WP47-A | 类型／属性改变，待本批后续包固定 |
| `SetTargetTypesToWater` | `007_MoveEffects_BattlerOther.rb`:855 | WP47-A | 类型／属性改变，待本批后续包固定 |
| `AddGhostTypeToTarget` | `007_MoveEffects_BattlerOther.rb`:877 | WP47-A | 类型／属性改变，待本批后续包固定 |
| `AddGrassTypeToTarget` | `007_MoveEffects_BattlerOther.rb`:898 | WP47-A | 类型／属性改变，待本批后续包固定 |
| `UserLosesFireType` | `007_MoveEffects_BattlerOther.rb`:919 | WP47-A | 类型／属性改变，待本批后续包固定 |
| `SetTargetAbilityToSimple` | `007_MoveEffects_BattlerOther.rb`:939 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `SetTargetAbilityToInsomnia` | `007_MoveEffects_BattlerOther.rb`:973 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `SetUserAbilityToTargetAbility` | `007_MoveEffects_BattlerOther.rb`:1007 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `SetTargetAbilityToUserAbility` | `007_MoveEffects_BattlerOther.rb`:1047 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `UserTargetSwapAbilities` | `007_MoveEffects_BattlerOther.rb`:1086 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `NegateTargetAbility` | `007_MoveEffects_BattlerOther.rb`:1155 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `NegateTargetAbilityIfTargetActed` | `007_MoveEffects_BattlerOther.rb`:1178 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `IgnoreTargetAbility` | `007_MoveEffects_BattlerOther.rb`:1196 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `StartUserAirborne` | `007_MoveEffects_BattlerOther.rb`:1206 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `StartTargetAirborneAndAlwaysHitByMoves` | `007_MoveEffects_BattlerOther.rb`:1229 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `HitsTargetInSky` | `007_MoveEffects_BattlerOther.rb`:1260 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `HitsTargetInSkyGroundsTarget` | `007_MoveEffects_BattlerOther.rb`:1268 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `StartGravity` | `007_MoveEffects_BattlerOther.rb`:1299 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `TransformUserIntoTarget` | `007_MoveEffects_BattlerOther.rb`:1338 | WP47-B | 能力／浮空／变身等控制，待本批后续包固定；完整形态域WP22前向 |
| `EnsureNextCriticalHit` | `008_MoveEffects_MoveAttributes.rb`:642 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `StartPreventCriticalHitsAgainstUserSide` | `008_MoveEffects_MoveAttributes.rb`:654 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `UserEnduresFaintingThisTurn` | `008_MoveEffects_MoveAttributes.rb`:682 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `StartWeakenElectricMoves` | `008_MoveEffects_MoveAttributes.rb`:696 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `StartWeakenFireMoves` | `008_MoveEffects_MoveAttributes.rb`:723 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `StartWeakenPhysicalDamageAgainstUserSide` | `008_MoveEffects_MoveAttributes.rb`:751 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `StartWeakenSpecialDamageAgainstUserSide` | `008_MoveEffects_MoveAttributes.rb`:772 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `StartWeakenDamageAgainstUserSideIfHail` | `008_MoveEffects_MoveAttributes.rb`:794 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `RemoveScreens` | `008_MoveEffects_MoveAttributes.rb`:821 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `ProtectUser` | `008_MoveEffects_MoveAttributes.rb`:852 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `ProtectUserBanefulBunker` | `008_MoveEffects_MoveAttributes.rb`:864 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `ProtectUserFromDamagingMovesKingsShield` | `008_MoveEffects_MoveAttributes.rb`:875 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `ProtectUserFromDamagingMovesObstruct` | `008_MoveEffects_MoveAttributes.rb`:888 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `ProtectUserFromTargetingMovesSpikyShield` | `008_MoveEffects_MoveAttributes.rb`:899 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `ProtectUserSideFromDamagingMovesIfUserFirstTurn` | `008_MoveEffects_MoveAttributes.rb`:909 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `ProtectUserSideFromStatusMoves` | `008_MoveEffects_MoveAttributes.rb`:930 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `ProtectUserSideFromPriorityMoves` | `008_MoveEffects_MoveAttributes.rb`:950 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `ProtectUserSideFromMultiTargetDamagingMoves` | `008_MoveEffects_MoveAttributes.rb`:964 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `RemoveProtections` | `008_MoveEffects_MoveAttributes.rb`:977 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `RemoveProtectionsBypassSubstitute` | `008_MoveEffects_MoveAttributes.rb`:994 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `HoopaRemoveProtectionsBypassSubstituteLowerUserDef1` | `008_MoveEffects_MoveAttributes.rb`:1002 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `EnsureNextMoveAlwaysHits` | `008_MoveEffects_MoveAttributes.rb`:1222 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `StartNegateTargetEvasionStatStageAndGhostImmunity` | `008_MoveEffects_MoveAttributes.rb`:1234 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `StartNegateTargetEvasionStatStageAndDarkImmunity` | `008_MoveEffects_MoveAttributes.rb`:1248 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `IgnoreTargetDefSpDefEvaStatStages` | `008_MoveEffects_MoveAttributes.rb`:1262 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TypeIsUserFirstType` | `008_MoveEffects_MoveAttributes.rb`:1277 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TypeDependsOnUserIVs` | `008_MoveEffects_MoveAttributes.rb`:1287 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TypeAndPowerDependOnUserBerry` | `008_MoveEffects_MoveAttributes.rb`:1338 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TypeDependsOnUserPlate` | `008_MoveEffects_MoveAttributes.rb`:1385 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TypeDependsOnUserMemory` | `008_MoveEffects_MoveAttributes.rb`:1422 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TypeDependsOnUserDrive` | `008_MoveEffects_MoveAttributes.rb`:1459 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TypeDependsOnUserMorpekoFormRaiseUserSpeed1` | `008_MoveEffects_MoveAttributes.rb`:1495 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TypeAndPowerDependOnWeather` | `008_MoveEffects_MoveAttributes.rb`:1513 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TypeAndPowerDependOnTerrain` | `008_MoveEffects_MoveAttributes.rb`:1550 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TargetMovesBecomeElectric` | `008_MoveEffects_MoveAttributes.rb`:1584 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `NormalMovesBecomeElectric` | `008_MoveEffects_MoveAttributes.rb`:1604 | WP45 | 场域／侧保护／清理已有主合同；参数消费WP43 |
| `RedirectAllMovesToUser` | `012_MoveEffects_ChangeMoveEffect.rb`:5 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `RedirectAllMovesToTarget` | `012_MoveEffects_ChangeMoveEffect.rb`:21 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `CannotBeRedirected` | `012_MoveEffects_ChangeMoveEffect.rb`:37 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `CurseTargetOrLowerUserSpd1RaiseUserAtkDef1` | `012_MoveEffects_ChangeMoveEffect.rb`:140 | WP47-B | 诅咒状态／阶级双入口，待本批后续包固定 |
| `EffectDependsOnEnvironment` | `012_MoveEffects_ChangeMoveEffect.rb`:224 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `HitsAllFoesAndPowersUpInPsychicTerrain` | `012_MoveEffects_ChangeMoveEffect.rb`:340 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `TargetNextFireMoveDamagesTarget` | `012_MoveEffects_ChangeMoveEffect.rb`:360 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `PowerUpAllyMove` | `012_MoveEffects_ChangeMoveEffect.rb`:431 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `UseLastMoveUsed` | `012_MoveEffects_ChangeMoveEffect.rb`:694 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `UseLastMoveUsedByTarget` | `012_MoveEffects_ChangeMoveEffect.rb`:787 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `UseMoveTargetIsAboutToUse` | `012_MoveEffects_ChangeMoveEffect.rb`:814 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `UseMoveDependingOnEnvironment` | `012_MoveEffects_ChangeMoveEffect.rb`:861 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `UseRandomMove` | `012_MoveEffects_ChangeMoveEffect.rb`:923 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `UseRandomMoveFromUserParty` | `012_MoveEffects_ChangeMoveEffect.rb`:1019 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `UseRandomUserMoveIfAsleep` | `012_MoveEffects_ChangeMoveEffect.rb`:1136 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `BounceBackProblemCausingStatusMoves` | `012_MoveEffects_ChangeMoveEffect.rb`:1207 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `StealAndUseBeneficialStatusMove` | `012_MoveEffects_ChangeMoveEffect.rb`:1217 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `ReplaceMoveThisBattleWithTargetLastMoveUsed` | `012_MoveEffects_ChangeMoveEffect.rb`:1232 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |
| `ReplaceMoveWithTargetLastMoveUsed` | `012_MoveEffects_ChangeMoveEffect.rb`:1285 | WP47-A | 属性／目标／调用合同，待本批后续包固定；当前只定位 |

## 3. 覆盖边界

本包MultiHit、Healing全文件身份有合同；MoveAttributes的伤害／恢复部分、Misc的伤害资格及延迟攻击、ChangeMoveEffect的伤害／恢复／蓄力／誓约、BattlerOther的空中加倍与内建挣扎均具名。基底效果的通用约束已纳入主文，不把辅助类型当PBS可用标识。其它文件中已审的阶级附加威力引用WP44 K合同；物品投掷、拍落等直接伤害与物品变化耦合族由WP47-B完整承接；先行／轮唱等伤害与行动控制族由WP47-B承接。全局未归属项仍由WP79后续审查，不凭本表宣称全部招式已覆盖。

本轮批准：[独立首审报告](../../review/wp46-wp47-review-2026-09-27/report.md)§2／4；A～F／139项伤害与恢复主合同限定通过。本次状态回填、C01维护和必要身份级联分开记账；被审首稿`170e063faaea4b66b5e8a7fc0b9bba907ff7aba7b4c15d8f435ff50d51f7ce88`（36,408字节）留史，当前新字节不冒充原被审版本。运行、完整形态／物品／AI组合及阶段出口保留。
