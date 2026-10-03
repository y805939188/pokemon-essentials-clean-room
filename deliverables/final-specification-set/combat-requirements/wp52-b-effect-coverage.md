# WP52-B 有界登记、覆盖与数据附表（净化正文；批次 12）

分类：combat-requirements／pokemon-rules 数据附表；性质：实现独立行为数据。

本附表为净化正文的一部分：按统一交接将批准输入 WP52-B《有界登记、覆盖与数据》转写为独立行为数据，不含源文件路径与行号（源定位集中登记于 `../../audit/source-traceability.md` 批次 12 条目）。本表仅审计定位，具体条件/数值/分支以主稿合同为准，不以登记索引替代行为。全部内容为静态证据；**无运行确认**（见 `../scope-statement.md`）。

## 1. 集合与注册语义

原 WP52-A 附表将 B 定位为 247 出现；本批具名移入 ChangeMoveEffect 中 23 条纯数值/恢复/誓约登记，当前 B 270 出现／268 不同有效键，C190 → 167 出现；A334、WP51 已有 15 不变，总 786 出现／783 不同出现键，实际最终 782 有效键（另两处 C 的缺源 copy 在 C 具体展开）。源登记 784 语句／12 文件；覆盖边界变化是责任修正，不修改旧已审材料、不把 C 提前算已提取。移入的 14 身份列于 §2 标记「由 C 定位移入」。

同族同键后 add 替代旧处理；copy 抓取当时已定义的源，缺源则不改目的。本包两组：连续切割分由 MoveAttributes:238 覆盖 :220；解除保护 :1190 缺源 copy 不生效、保留 :1175。两个不能按「出现两次」加分；MoveEffectScore PowerHigherWithConsecutiveUseOnUserSide 未登记，RemoveProtectionsBypassSubstitute 目标分未登记，按共用默认保持输入。C 的第三重复键在 C 展开。

## 2. 逐登记出现、最终绑定与具体合同

被覆盖的原段不是同时执行；copy 无源行不创建新行为。「←X」表示 copy 且最终绑定到 X 的处理器（源文件与行号见追溯条目）。

### 2.1 Misc 文件（主稿 §4/§5.1/§5.2/§6.2）

MoveEffectAgainstTargetScore：CrashDamageIfFailsUnusableInGravity（§6.2）。

MoveFailureCheck：StartSunWeather（§5.1）；StartRainWeather←StartSunWeather；StartSandstormWeather←StartSunWeather；StartHailWeather←StartSunWeather；StartElectricTerrain；StartGrassyTerrain；StartMistyTerrain；StartPsychicTerrain；RemoveTerrain；AddSpikesToFoeSide；AddToxicSpikesToFoeSide；AddStealthRocksToFoeSide；AddStickyWebToFoeSide（均 §5.1）；UserMakeSubstitute、RemoveAllScreensAndSafeguard（§5.2）；StartShadowSkyWeather←StartSunWeather（§5.1）。

MoveEffectScore：StartSunWeather、StartRainWeather、StartSandstormWeather、StartHailWeather、StartElectricTerrain、StartGrassyTerrain、StartMistyTerrain、StartPsychicTerrain、RemoveTerrain、StartShadowSkyWeather（均 §5.1）；AddSpikesToFoeSide、AddToxicSpikesToFoeSide、AddStealthRocksToFoeSide、AddStickyWebToFoeSide、UserMakeSubstitute、RemoveAllScreensAndSafeguard（§5.2）；AttackTwoTurnsLater（§5.2）；AllBattlersLoseHalfHPUserSkipsNextTurn、UserLosesHalfHP（§4）。

MoveFailureAgainstTargetCheck：AttackTwoTurnsLater（§5.2）。

### 2.2 BattlerStats 文件（主稿 §4/§5.2）

MoveFailureAgainstTargetCheck：LowerTargetEvasion1RemoveSideEffects（§5.2）。
MoveEffectAgainstTargetScore：LowerTargetEvasion1RemoveSideEffects（§5.2）；UserTargetAverageHP（§4）。
MoveFailureCheck：StartUserSideDoubleSpeed（§5.2）。
MoveEffectScore：StartUserSideDoubleSpeed（§5.2）；StartSwapAllBattlersBaseDefensiveStats（§5.2）。

### 2.3 BattlerOther 文件

MoveBasePower：FlinchTargetDoublePowerIfTargetInSky（§2.1）。

### 2.4 MoveAttributes 文件（主稿 §2/§2.1/§2.2/§6/§6.2）

MoveBasePower：FixedDamage20、FixedDamage40、FixedDamageHalfTargetHP、FixedDamageUserLevel、FixedDamageUserLevelRandom（§2）；LowerTargetHPToUserHP（§2）；OHKO（§2）；OHKOIce←OHKO；OHKOHitsUndergroundTarget←OHKO；PowerHigherWithUserHP（§2）；PowerLowerWithUserHP←PowerHigherWithUserHP；PowerHigherWithTargetHP←PowerHigherWithUserHP；PowerHigherWithUserHappiness←PowerHigherWithUserHP；PowerLowerWithUserHappiness←PowerHigherWithUserHP；PowerHigherWithUserPositiveStatStages←PowerHigherWithUserHP；PowerHigherWithTargetPositiveStatStages←PowerHigherWithUserHP；PowerHigherWithUserFasterThanTarget←PowerHigherWithUserHP；PowerHigherWithTargetFasterThanUser←PowerHigherWithUserHP；PowerHigherWithLessPP、PowerHigherWithTargetWeight（§2）；PowerHigherWithUserHeavierThanTarget←PowerHigherWithTargetWeight；PowerHigherWithConsecutiveUse（§2）；PowerHigherWithConsecutiveUseOnUserSide（§2，未登记效果分）；RandomPowerDoublePowerIfTargetUnderground、DoublePowerIfTargetHPLessThanHalf（§2）；DoublePowerIfUserPoisonedBurnedParalyzed←DoublePowerIfTargetHPLessThanHalf；DoublePowerIfTargetAsleepCureTarget←DoublePowerIfTargetHPLessThanHalf；DoublePowerIfTargetPoisoned（§2）；DoublePowerIfTargetParalyzedCureTarget←DoublePowerIfTargetPoisoned；DoublePowerIfTargetStatusProblem、DoublePowerIfUserHasNoItem、DoublePowerIfTargetUnderwater（§2）；DoublePowerIfTargetUnderground←DoublePowerIfTargetUnderwater；DoublePowerIfTargetInSky（§2）；DoublePowerInElectricTerrain←DoublePowerIfTargetInSky；DoublePowerIfUserLastMoveFailed←DoublePowerIfTargetInSky；DoublePowerIfAllyFaintedLastTurn←DoublePowerIfTargetInSky；EffectivenessIncludesFlyingType（§2.1/§6.2）；TypeDependsOnUserIVs（§2.1）；TypeAndPowerDependOnUserBerry（§2.1）；TypeAndPowerDependOnWeather（§2.1）；TypeAndPowerDependOnTerrain←TypeAndPowerDependOnWeather。

MoveFailureAgainstTargetCheck：LowerTargetHPToUserHP、OHKO、CannotMakeTargetFaint（§2/§6）；OHKOIce←OHKO；OHKOHitsUndergroundTarget←OHKO；TargetMovesBecomeElectric（§6.2）。

MoveEffectAgainstTargetScore：OHKO（§2）；OHKOIce←OHKO；OHKOHitsUndergroundTarget←OHKO；DamageTargetAlly（§2）；DoublePowerIfTargetAsleepCureTarget、DoublePowerIfTargetParalyzedCureTarget、DoublePowerIfUserLostHPThisTurn、DoublePowerIfTargetActed、DoublePowerIfTargetNotActed（§2）；RecoilQuarterOfDamageDealt、RecoilThirdOfDamageDealtParalyzeTarget、RecoilThirdOfDamageDealtBurnTarget、RecoilHalfOfDamageDealt（§6.2）；CategoryDependsOnHigherDamagePoisonTarget←PoisonTarget（§2.1/§6.2，绑定到 BattlerOther 的 PoisonTarget）；EnsureNextMoveAlwaysHits、StartNegateTargetEvasionStatStageAndGhostImmunity、StartNegateTargetEvasionStatStageAndDarkImmunity、TargetMovesBecomeElectric（§6.2）；RemoveProtections（§6）；RemoveProtections←RemoveProtectionsBypassSubstitute（源不存在，不写入，:1175 保留）；HoopaRemoveProtectionsBypassSubstituteLowerUserDef1（§6）。

MoveEffectScore：PowerHigherWithConsecutiveUse（:220 后被 :238 覆盖——效果分读取回声侧计数，其 P 仍读连续切割）；DoublePowerIfUserLostHPThisTurn（§2）；EnsureNextCriticalHit（§2.2）；StartPreventCriticalHitsAgainstUserSide（§2.2）；UserEnduresFaintingThisTurn（§6）；StartWeakenElectricMoves、StartWeakenFireMoves、StartWeakenPhysicalDamageAgainstUserSide、StartWeakenSpecialDamageAgainstUserSide、StartWeakenDamageAgainstUserSideIfHail、RemoveScreens、ProtectUser、ProtectUserBanefulBunker、ProtectUserFromDamagingMovesKingsShield、ProtectUserFromDamagingMovesObstruct、ProtectUserFromTargetingMovesSpikyShield、ProtectUserSideFromDamagingMovesIfUserFirstTurn、ProtectUserSideFromStatusMoves、ProtectUserSideFromPriorityMoves、ProtectUserSideFromMultiTargetDamagingMoves、TypeDependsOnUserMorpekoFormRaiseUserSpeed1、NormalMovesBecomeElectric（§6/§2.1/§6.2）。

MoveFailureCheck：StartPreventCriticalHitsAgainstUserSide（§2.2）；StartWeakenElectricMoves、StartWeakenFireMoves、StartWeakenPhysicalDamageAgainstUserSide、StartWeakenSpecialDamageAgainstUserSide、StartWeakenDamageAgainstUserSideIfHail、ProtectUserSideFromDamagingMovesIfUserFirstTurn、ProtectUserSideFromStatusMoves、ProtectUserSideFromPriorityMoves、ProtectUserSideFromMultiTargetDamagingMoves、HoopaRemoveProtectionsBypassSubstituteLowerUserDef1、EnsureNextMoveAlwaysHits、TypeAndPowerDependOnUserBerry、TypeDependsOnUserMorpekoFormRaiseUserSpeed1（§6/§2.1/§6.2）。

MoveEffectScore（复制绑定）：TypeDependsOnUserMorpekoFormRaiseUserSpeed1←RaiseUserSpeed1（绑定到 BattlerStats 的 RaiseUserSpeed1）。

### 2.5 MultiHit 文件（主稿 §3）

MoveBasePower：HitTwoTimes（§3）；HitTwoTimesPoisonTarget←HitTwoTimes；HitTwoTimesFlinchTarget←HitTwoTimes；HitTwoTimesTargetThenTargetAlly、HitThreeTimesPowersUpWithEachHit（§3）；HitThreeTimesAlwaysCriticalHit←HitTwoTimes；HitTwoToFiveTimes、HitTwoToFiveTimesOrThreeForAshGreninja（§3）；HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1←HitTwoToFiveTimes；HitOncePerUserTeamMember、TwoTurnAttackOneTurnInSun、MultiTurnAttackPowersUpEachTurn、MultiTurnAttackBideThenReturnDoubleDamage（§3）。

MoveEffectAgainstTargetScore：HitTwoTimes（§3）；HitTwoTimesPoisonTarget、HitTwoTimesFlinchTarget、HitThreeTimesPowersUpWithEachHit、HitTwoToFiveTimes、HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1、HitOncePerUserTeamMember（§3）；HitThreeTimesAlwaysCriticalHit←HitTwoTimes（目标分绑定）；HitTwoToFiveTimesOrThreeForAshGreninja←HitTwoToFiveTimes；TwoTurnAttack、TwoTurnAttackOneTurnInSun、TwoTurnAttackParalyzeTarget、TwoTurnAttackBurnTarget、TwoTurnAttackFlinchTarget、TwoTurnAttackRaiseUserSpAtkSpDefSpd2、TwoTurnAttackChargeRaiseUserDefense1、TwoTurnAttackChargeRaiseUserSpAtk1、TwoTurnAttackInvulnerableUnderground、TwoTurnAttackInvulnerableUnderwater、TwoTurnAttackInvulnerableInSky、TwoTurnAttackInvulnerableInSkyParalyzeTarget、TwoTurnAttackInvulnerableRemoveProtections（§3）；TwoTurnAttackInvulnerableInSkyTargetCannotAct←TwoTurnAttackInvulnerableInSky。

MoveFailureCheck：HitOncePerUserTeamMember（§3）；TwoTurnAttackRaiseUserSpAtkSpDefSpd2←RaiseUserAtkDef1（绑定到 BattlerStats 的 RaiseUserAtkDef1）。

MoveFailureAgainstTargetCheck：TwoTurnAttackInvulnerableInSkyTargetCannotAct（§3）。

MoveEffectScore：AttackAndSkipNextTurn、MultiTurnAttackBideThenReturnDoubleDamage（§3）。

### 2.6 Healing 文件（主稿 §4）

MoveFailureCheck：HealUserFullyAndFallAsleep（§4）；HealUserHalfOfTotalHP（§4）；HealUserDependingOnWeather←HealUserHalfOfTotalHP；HealUserDependingOnSandstorm←HealUserHalfOfTotalHP；HealUserHalfOfTotalHPLoseFlyingTypeThisTurn←HealUserHalfOfTotalHP；HealUserPositionNextTurn、StartHealUserEachTurn、StartHealUserEachTurnTrapUserInBattle（§4）；UserLosesHalfOfTotalHPExplosive（§4）；UserFaintsExplosive←UserLosesHalfOfTotalHPExplosive；UserFaintsPowersUpInMistyTerrainExplosive←UserFaintsExplosive；UserFaintsHealAndCureReplacement（§4）；UserFaintsHealAndCureReplacementRestorePP←UserFaintsHealAndCureReplacement；AttackerFaintsIfUserFaints（§4）。

MoveEffectScore：HealUserFullyAndFallAsleep、HealUserHalfOfTotalHP、HealUserDependingOnWeather、HealUserDependingOnSandstorm、HealUserHalfOfTotalHPLoseFlyingTypeThisTurn、HealUserPositionNextTurn、StartHealUserEachTurn、StartHealUserEachTurnTrapUserInBattle（§4）；UserLosesHalfOfTotalHP（§4）；UserLosesHalfOfTotalHPExplosive←UserLosesHalfOfTotalHP；UserFaintsExplosive（§4）；UserFaintsPowersUpInMistyTerrainExplosive←UserFaintsExplosive；UserFaintsFixedDamageUserHP←UserFaintsExplosive；UserFaintsHealAndCureReplacement（§4）；UserFaintsHealAndCureReplacementRestorePP←UserFaintsHealAndCureReplacement；StartPerishCountsForAllBattlers、AttackerFaintsIfUserFaints、SetAttackerMovePPTo0IfUserFaints（§4）。

MoveFailureAgainstTargetCheck：CureTargetStatusHealUserHalfOfTotalHP、HealUserByTargetAttackLowerTargetAttack1、HealUserByHalfOfDamageDoneIfTargetAsleep、HealUserAndAlliesQuarterOfTotalHP、HealUserAndAlliesQuarterOfTotalHPCureStatus、HealTargetHalfOfTotalHP、HealTargetDependingOnGrassyTerrain、StartDamageTargetEachTurnIfTargetAsleep、StartLeechSeedTarget、StartPerishCountsForAllBattlers（§4）；HealTargetDependingOnGrassyTerrain←HealTargetHalfOfTotalHP。

MoveEffectAgainstTargetScore：CureTargetStatusHealUserHalfOfTotalHP、HealUserByTargetAttackLowerTargetAttack1、HealUserByHalfOfDamageDone、HealUserByThreeQuartersOfDamageDone、HealUserAndAlliesQuarterOfTotalHP、HealUserAndAlliesQuarterOfTotalHPCureStatus、HealTargetHalfOfTotalHP、HealTargetDependingOnGrassyTerrain、StartDamageTargetEachTurnIfTargetAsleep、StartLeechSeedTarget、UserFaintsLowerTargetAtkSpAtk2（§4）；HealUserByHalfOfDamageDoneIfTargetAsleep←HealUserByHalfOfDamageDone。

MoveBasePower：UserFaintsPowersUpInMistyTerrainExplosive、UserFaintsFixedDamageUserHP（§4）。

### 2.7 ChangeMoveEffect 文件（由 C 定位移入；主稿 §2.1/§2.2/§4/§6.2）

MoveBasePower：RandomlyDamageOrHealTarget（§2.1；由 C 定位移入）；HitsAllFoesAndPowersUpInPsychicTerrain（§2.1；由 C 定位移入）；CounterPhysicalDamage、CounterSpecialDamage、CounterDamagePlusHalf（§2.2；由 C 定位移入）；PowerDependsOnUserStockpile（§2.1；由 C 定位移入）。

MoveEffectScore：RandomlyDamageOrHealTarget（§2.1；由 C 定位移入）；DoublePowerAfterFusionFlare、DoublePowerAfterFusionBolt（§2.2；由 C 定位移入）；CounterPhysicalDamage、CounterSpecialDamage、CounterDamagePlusHalf（§2.2；由 C 定位移入）；UserAddStockpileRaiseDefSpDef1、HealUserDependingOnUserStockpile（§4；由 C 定位移入）；PowerDependsOnUserStockpile（§2.1；由 C 定位移入）；GrassPledge、FirePledge、WaterPledge（§6.2；由 C 定位移入）。

MoveFailureAgainstTargetCheck：HealAllyOrDamageFoe（§4；由 C 定位移入）。

MoveEffectAgainstTargetScore：HealAllyOrDamageFoe（§4；由 C 定位移入）。

MoveFailureCheck：UserAddStockpileRaiseDefSpDef1（§4；由 C 定位移入）；PowerDependsOnUserStockpile、HealUserDependingOnUserStockpile（§2.1/§4；由 C 定位移入）。

## 3. 场域收益匹配数据

主稿 §5.1 完整给量值、阵营符号、技能与伞门；下表给效果名精确审计身份，组内任一匹配一次，不按多个匹配叠加。仅提取字面值。

| 数据组 | 场域 | 完整默认身份 |
| --- | --- | --- |
| beneficial_moves | Sun | HealUserDependingOnWeather, RaiseUserAtkSpAtk1Or2InSun, TwoTurnAttackOneTurnInSun, TypeAndPowerDependOnWeather |
| beneficial_moves | Rain | ConfuseTargetAlwaysHitsInRainHitsTargetInSky, ParalyzeTargetAlwaysHitsInRainHitsTargetInSky, TypeAndPowerDependOnWeather |
| beneficial_moves | Sandstorm | HealUserDependingOnSandstorm, TypeAndPowerDependOnWeather |
| beneficial_moves | Hail | FreezeTargetAlwaysHitsInHail, StartWeakenDamageAgainstUserSideIfHail, TypeAndPowerDependOnWeather |
| beneficial_moves | ShadowSky | TypeAndPowerDependOnWeather |
| negative_moves | Sun | ConfuseTargetAlwaysHitsInRainHitsTargetInSky, ParalyzeTargetAlwaysHitsInRainHitsTargetInSky |
| negative_moves | Rain | HealUserDependingOnWeather, TwoTurnAttackOneTurnInSun |
| negative_moves | Sandstorm | HealUserDependingOnWeather, TwoTurnAttackOneTurnInSun |
| negative_moves | Hail | HealUserDependingOnWeather, TwoTurnAttackOneTurnInSun |
| good_moves | Electric | DoublePowerInElectricTerrain |
| good_moves | Grassy | HealTargetDependingOnGrassyTerrain, HigherPriorityInGrassyTerrain |
| good_moves | Misty | UserFaintsPowersUpInMistyTerrainExplosive |
| good_moves | Psychic | HitsAllFoesAndPowersUpInPsychicTerrain |
| bad_moves | Grassy | DoublePowerIfTargetUnderground, LowerTargetSpeed1WeakerInGrassyTerrain, RandomPowerDoublePowerIfTargetUnderground |

## 4. 保留责任

A 为共同评分/数值/状态阶级，WP51 为选择/技能/资源；本包补具体 B 处理器。物品评级、调用/替换、行动与换出控制仍 C，完整设施仍各既定包；真实写入和数值依 WP43–50。低档不启 MoveBasePower、ScoreMoves 关不启效果分，以及 copy 失败后的默认行为不能用完整目录名代替。全局运行/插件组合与 WP79 未关闭。
