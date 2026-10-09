# 多次攻击、特殊伤害与恢复——有界效果覆盖（净化附表；批次 7）

本附表是 [wp46-damage-multihit-and-healing](wp46-damage-multihit-and-healing.md) 的附件：原有 139 项审计身份及另接收的 1 项 HP 均分身份按行为合同归属，每项具体条件/量/阶段/失败结果在主文指定节；审计身份仅用于对应，不能从名字推导未写算法。不建议未来类层级。源文件与行号定位见 `../../../audit/source-traceability.md` 本包条目。

## 1. 本包实际合同（原有 139 项，另接收 1 项）

### 1.1 §3 多击/两回合/连用族（30 项）

`Struggle`（内建挣扎，§7 同族接点）、`HitTwoTimes`、`HitTwoTimesPoisonTarget`、`HitTwoTimesFlinchTarget`、`HitTwoTimesTargetThenTargetAlly`、`HitThreeTimesPowersUpWithEachHit`、`HitThreeTimesAlwaysCriticalHit`、`HitTwoToFiveTimes`、`HitTwoToFiveTimesOrThreeForAshGreninja`、`HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1`、`HitOncePerUserTeamMember`、`AttackAndSkipNextTurn`、`TwoTurnAttack`、`TwoTurnAttackOneTurnInSun`、`TwoTurnAttackParalyzeTarget`、`TwoTurnAttackBurnTarget`、`TwoTurnAttackFlinchTarget`、`TwoTurnAttackRaiseUserSpAtkSpDefSpd2`、`TwoTurnAttackChargeRaiseUserDefense1`、`TwoTurnAttackChargeRaiseUserSpAtk1`、`TwoTurnAttackInvulnerableUnderground`、`TwoTurnAttackInvulnerableUnderwater`、`TwoTurnAttackInvulnerableInSky`、`TwoTurnAttackInvulnerableInSkyParalyzeTarget`、`TwoTurnAttackInvulnerableInSkyTargetCannotAct`、`TwoTurnAttackInvulnerableRemoveProtections`、`MultiTurnAttackPreventSleeping`、`MultiTurnAttackConfuseUserAtEnd`、`MultiTurnAttackPowersUpEachTurn`、`MultiTurnAttackBideThenReturnDoubleDamage`

（每项主合同见主文 §3.1–§3.3 对应行；均标注「本包主合同」。）

### 1.2 §4 固定伤害/反击/使用时机族（22 项）

`FailsIfNotUserFirstTurn`、`FailsIfUserHasUnusedMove`、`FailsIfUserNotConsumedBerry`、`FailsIfTargetHasNoItem`、`FailsUnlessTargetSharesTypeWithUser`、`FailsIfUserDamagedThisTurn`、`FailsIfTargetActed`、`AttackTwoTurnsLater`（§6 未来攻击接点）、`FixedDamage20`、`FixedDamage40`、`FixedDamageHalfTargetHP`、`FixedDamageUserLevel`、`FixedDamageUserLevelRandom`、`LowerTargetHPToUserHP`、`OHKO`、`OHKOIce`、`OHKOHitsUndergroundTarget`、`DamageTargetAlly`、`CounterPhysicalDamage`、`CounterSpecialDamage`、`CounterDamagePlusHalf`、`UserFaintsFixedDamageUserHP`（§7 同族接点）

（每项主合同见主文 §4/§4.1/§6.3/§7 对应行；均标注「本包主合同」。）

### 1.3 §5 威力/类别/输入替代族（44 项）

`FlinchTargetDoublePowerIfTargetInSky`（状态/阶级中央资格引用《异常状态、能力阶级与免疫》；本包仅完整本族时点与数值）、`PowerHigherWithUserHP`、`PowerLowerWithUserHP`、`PowerHigherWithTargetHP`、`PowerHigherWithUserHappiness`、`PowerLowerWithUserHappiness`、`PowerHigherWithUserPositiveStatStages`、`PowerHigherWithTargetPositiveStatStages`、`PowerHigherWithUserFasterThanTarget`、`PowerHigherWithTargetFasterThanUser`、`PowerHigherWithLessPP`、`PowerHigherWithTargetWeight`、`PowerHigherWithUserHeavierThanTarget`、`PowerHigherWithConsecutiveUse`、`PowerHigherWithConsecutiveUseOnUserSide`、`RandomPowerDoublePowerIfTargetUnderground`、`DoublePowerIfTargetHPLessThanHalf`、`DoublePowerIfUserPoisonedBurnedParalyzed`、`DoublePowerIfTargetAsleepCureTarget`、`DoublePowerIfTargetPoisoned`、`DoublePowerIfTargetParalyzedCureTarget`、`DoublePowerIfTargetStatusProblem`、`DoublePowerIfUserHasNoItem`、`DoublePowerIfTargetUnderwater`、`DoublePowerIfTargetUnderground`、`DoublePowerIfTargetInSky`、`DoublePowerInElectricTerrain`、`DoublePowerIfUserLastMoveFailed`、`DoublePowerIfAllyFaintedLastTurn`、`DoublePowerIfUserLostHPThisTurn`、`DoublePowerIfTargetLostHPThisTurn`、`DoublePowerIfUserStatsLoweredThisTurn`、`DoublePowerIfTargetActed`、`DoublePowerIfTargetNotActed`、`AlwaysCriticalHit`、`CannotMakeTargetFaint`、`EffectivenessIncludesFlyingType`、`CategoryDependsOnHigherDamagePoisonTarget`、`CategoryDependsOnHigherDamageIgnoreTargetAbility`、`UseUserDefenseInsteadOfUserAttack`、`UseTargetAttackInsteadOfUserAttack`、`UseTargetDefenseInsteadOfTargetSpDef`、`DoublePowerAfterFusionFlare`、`DoublePowerAfterFusionBolt`

（每项主合同见主文 §5.1–§5.3 对应行；均标注「本包主合同」。）

### 1.4 §6 治疗/吸取/持续建立族（23 项）

`HealUserFullyAndFallAsleep`、`HealUserHalfOfTotalHP`、`HealUserDependingOnWeather`、`HealUserDependingOnSandstorm`、`HealUserHalfOfTotalHPLoseFlyingTypeThisTurn`、`CureTargetStatusHealUserHalfOfTotalHP`、`HealUserByTargetAttackLowerTargetAttack1`、`HealUserByHalfOfDamageDone`、`HealUserByHalfOfDamageDoneIfTargetAsleep`、`HealUserByThreeQuartersOfDamageDone`、`HealUserAndAlliesQuarterOfTotalHP`、`HealUserAndAlliesQuarterOfTotalHPCureStatus`、`HealTargetHalfOfTotalHP`、`HealTargetDependingOnGrassyTerrain`、`HealUserPositionNextTurn`、`StartHealUserEachTurn`、`StartHealUserEachTurnTrapUserInBattle`、`StartDamageTargetEachTurnIfTargetAsleep`、`StartLeechSeedTarget`、`RandomlyDamageOrHealTarget`、`HealAllyOrDamageFoe`、`UserAddStockpileRaiseDefSpDef1`、`HealUserDependingOnUserStockpile`

（每项主合同见主文 §5.4/§6.1–§6.3 对应行；均标注「本包主合同」。）

### 1.5 §5.4 蓄力/誓约族（4 项）

`PowerDependsOnUserStockpile`（§5.4 喷出）、`GrassPledge`、`FirePledge`、`WaterPledge`（§5.4 誓约组合）

### 1.6 §7 反伤/自损/同归族（16 项）

`CrashDamageIfFailsUnusableInGravity`、`RecoilQuarterOfDamageDealt`、`RecoilThirdOfDamageDealt`、`RecoilThirdOfDamageDealtParalyzeTarget`、`RecoilThirdOfDamageDealtBurnTarget`、`RecoilHalfOfDamageDealt`、`UserLosesHalfOfTotalHP`、`UserLosesHalfOfTotalHPExplosive`、`UserFaintsExplosive`、`UserFaintsPowersUpInMistyTerrainExplosive`、`UserFaintsLowerTargetAtkSpAtk2`（状态/阶级中央资格引用《异常状态、能力阶级与免疫》；本包仅完整本族时点与数值）、`UserFaintsHealAndCureReplacement`、`UserFaintsHealAndCureReplacementRestorePP`、`StartPerishCountsForAllBattlers`、`AttackerFaintsIfUserFaints`、`SetAttackerMovePPTo0IfUserFaints`

（每项主合同见主文 §7 对应行；均标注「本包主合同」。）

> 计数说明：§1.1–§1.6 的实际身份数依序为 30/22/44/23/4/16，共 139，且这 139 个身份唯一；Struggle 只在 §1.1 身份目录计一次，其行为合同仍在主文 §7。139 是这一固定审计身份集合的大小，不是全部招式数量或效果全覆盖证明。HP 均分的域间接收单列 §1.7，不改这 139 个身份、既有归属和分母。

### 1.7 从阶级效果表接收的 HP 均分（1 项）

| 审计身份 | 接收后的实际合同 | 原归属与计数 |
| --- | --- | --- |
| `UserTargetAverageHP` | [主文 §6.4](wp46-damage-multihit-and-healing.md#64-hp-均分)：一次整数平均、使用者先于目标、各自 HP 上限、既有伤害记录、普通前门与两端物品检查 | WP44 覆盖表 §2.5 委派；仍在其 114 身份内作域外归属，WP46 另接收，不纳入原 139 集合 |

本目录的明确主合同身份共 140＝原有 139＋域间接收 1。此数不代表全参考效果集合，也不能替代行为参数核对。

## 2. 同目录已定位的其它责任（不计本包主合同数量）

这些行不计本包主合同数量。招式变更两规格将逐包阅读补合同；《异常状态、能力阶级与免疫》、场域规格已审范围仅引用，不冒称当前重读全部源文件；源行可机械定位，不能当行为验收。

### 2.1 归《战斗类型、命中与伤害计算》（1 项）

`None`——无额外效果的基础伤害（§3～§7 主规则）。

### 2.2 归招式变更-A 规格（属性/目标/调用合同，待该包固定；当前只定位，共 45 项）

`DoesNothingCongratulations`、`DoesNothingFailsIfNoAlly`、`DoesNothingUnusableInGravity`、`EnsureNextCriticalHit`、`UserEnduresFaintingThisTurn`、`ProtectUser`、`ProtectUserBanefulBunker`、`ProtectUserFromDamagingMovesKingsShield`、`ProtectUserFromDamagingMovesObstruct`、`ProtectUserFromTargetingMovesSpikyShield`、`RemoveProtections`、`RemoveProtectionsBypassSubstitute`、`HoopaRemoveProtectionsBypassSubstituteLowerUserDef1`、`EnsureNextMoveAlwaysHits`、`StartNegateTargetEvasionStatStageAndGhostImmunity`、`StartNegateTargetEvasionStatStageAndDarkImmunity`、`IgnoreTargetDefSpDefEvaStatStages`、`TypeIsUserFirstType`、`TypeDependsOnUserIVs`、`TypeAndPowerDependOnUserBerry`、`TypeDependsOnUserPlate`、`TypeDependsOnUserMemory`、`TypeDependsOnUserDrive`、`TypeDependsOnUserMorpekoFormRaiseUserSpeed1`、`TypeAndPowerDependOnWeather`、`TypeAndPowerDependOnTerrain`、`TargetMovesBecomeElectric`、`RedirectAllMovesToUser`、`RedirectAllMovesToTarget`、`CannotBeRedirected`、`EffectDependsOnEnvironment`、`HitsAllFoesAndPowersUpInPsychicTerrain`、`TargetNextFireMoveDamagesTarget`、`PowerUpAllyMove`、`UseLastMoveUsed`、`UseLastMoveUsedByTarget`、`UseMoveTargetIsAboutToUse`、`UseMoveDependingOnEnvironment`、`UseRandomMove`、`UseRandomMoveFromUserParty`、`UseRandomUserMoveIfAsleep`、`BounceBackProblemCausingStatusMoves`、`StealAndUseBeneficialStatusMove`、`ReplaceMoveThisBattleWithTargetLastMoveUsed`、`ReplaceMoveWithTargetLastMoveUsed`

### 2.3 归招式变更-B 规格（奖励标记/交换位置/行动准备、控制/物品/能力变化，共 20 项）

`AddMoneyGainedFromBattle`、`DoubleMoneyGainedFromBattle`、`UserMakeSubstitute`、`UserSwapsPositionsWithAlly`、`BurnAttackerBeforeUserActs`、`SetTargetAbilityToSimple`、`SetTargetAbilityToInsomnia`、`SetUserAbilityToTargetAbility`、`SetTargetAbilityToUserAbility`、`UserTargetSwapAbilities`、`NegateTargetAbility`、`NegateTargetAbilityIfTargetActed`、`IgnoreTargetAbility`、`StartUserAirborne`、`StartTargetAirborneAndAlwaysHitByMoves`、`HitsTargetInSky`、`HitsTargetInSkyGroundsTarget`、`StartGravity`、`TransformUserIntoTarget`、`CurseTargetOrLowerUserSpd1RaiseUserAtkDef1`

### 2.4 归场域规格（天气/场地/侧危害/屏障建立与清除，共 28 项）

`StartSunWeather`、`StartRainWeather`、`StartSandstormWeather`、`StartHailWeather`、`StartElectricTerrain`、`StartGrassyTerrain`、`StartMistyTerrain`、`StartPsychicTerrain`、`RemoveTerrain`、`AddSpikesToFoeSide`、`AddToxicSpikesToFoeSide`、`AddStealthRocksToFoeSide`、`AddStickyWebToFoeSide`、`SwapSideEffects`、`RemoveUserBindingAndEntryHazards`、`StartPreventCriticalHitsAgainstUserSide`、`StartWeakenElectricMoves`、`StartWeakenFireMoves`、`StartWeakenPhysicalDamageAgainstUserSide`、`StartWeakenSpecialDamageAgainstUserSide`、`StartWeakenDamageAgainstUserSideIfHail`、`RemoveScreens`、`ProtectUserSideFromDamagingMovesIfUserFirstTurn`、`ProtectUserSideFromStatusMoves`、`ProtectUserSideFromPriorityMoves`、`ProtectUserSideFromMultiTargetDamagingMoves`、`NormalMovesBecomeElectric`、`StartUserSideImmunityToInflictedStatus`

### 2.5 归《异常状态、能力阶级与免疫》（已审状态/附效有界覆盖，共 29 项）

`SleepTarget`、`SleepTargetIfUserDarkrai`、`SleepTargetChangeUserMeloettaForm`、`SleepTargetNextTurn`、`PoisonTarget`、`PoisonTargetLowerTargetSpeed1`、`BadPoisonTarget`、`ParalyzeTarget`、`ParalyzeTargetIfNotTypeImmune`、`ParalyzeTargetAlwaysHitsInRainHitsTargetInSky`、`ParalyzeFlinchTarget`、`BurnTarget`、`BurnTargetIfTargetStatsRaisedThisTurn`、`BurnFlinchTarget`、`FreezeTarget`、`FreezeTargetSuperEffectiveAgainstWater`、`FreezeTargetAlwaysHitsInHail`、`FreezeFlinchTarget`、`ParalyzeBurnOrFreezeTarget`、`GiveUserStatusToTarget`、`CureUserBurnPoisonParalysis`、`CureUserPartyStatus`、`CureTargetBurn`、`FlinchTarget`、`FlinchTargetFailsIfUserNotAsleep`、`FlinchTargetFailsIfNotUserFirstTurn`、`ConfuseTarget`、`ConfuseTargetAlwaysHitsInRainHitsTargetInSky`、`AttractTarget`

### 2.6 类型/属性改变族（归招式变更两规格，共 9 项）

`SetUserTypesBasedOnEnvironment`、`SetUserTypesToResistLastAttack`、`SetUserTypesToTargetTypes`、`SetUserTypesToUserMoveType`、`SetTargetTypesToPsychic`、`SetTargetTypesToWater`、`AddGhostTypeToTarget`、`AddGrassTypeToTarget`、`UserLosesFireType`

## 3. 覆盖边界

本包多击、治疗全文件身份有合同；伤害属性的伤害/恢复部分、杂项的伤害资格及延迟攻击、效果变更的伤害/恢复/蓄力/誓约、 battler 其它的空中加倍与内建挣扎均具名。基底效果的通用约束已纳入主文，不把辅助类型当数据可用标识。其它文件中已审的阶级附加威力引用《异常状态、能力阶级与免疫》K 合同；物品投掷、拍落等直接伤害与物品变化耦合族由招式变更-B 完整承接；先行/轮唱等伤害与行动控制族由招式变更-B 承接。全局未归属项仍由 WP79 后续审查，不凭本表宣称全部招式已覆盖。
