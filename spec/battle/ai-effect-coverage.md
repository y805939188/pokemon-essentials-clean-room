# WP52-B 有界登记、覆盖与数据附表

参考版本的静态规则与推导条件。[证据范围](../../reference/scope-and-evidence.md) · [本功能的验收案例](../../vectors/ability-triggers-and-battle-ai.md)

分类：combat-requirements／pokemon-rules 数据附表；性质：实现独立行为数据。

本表列出登记项，具体条件/数值/分支以主稿合同为准，不以登记索引替代行为。全部内容为静态证据；**无运行确认**（见 [证据范围](../../reference/scope-and-evidence.md)）。

## 1. 集合与注册语义

按来源分组时 B 有 247 条出现、C 有 190 条。按实际效果分组时，ChangeMoveEffect 中的 23 条纯数值/恢复/誓约登记属于 B，因此 B 有 270 条出现／268 个不同有效键，C 有 167 条出现；A 有 334 条，WP51 有 15 条，总 786 出现／783 不同出现键，实际最终 782 有效键（另两处 C 的缺源 copy 在 C 具体展开）。源登记 784 语句／12 文件；这 23 条登记对应 14 个身份，见 §2 的「数值、恢复与誓约」标记。

同族同键只有最终有效行为；复制只取得当时同族已有源行为，缺源不写目的，也不是未来动态别名。连续切割的效果分读取回声侧计数、基数仍读连续切割计数。RemoveProtections 的有效目标分仍为 +7；不存在的 RemoveProtectionsBypassSubstitute 目标评分不能覆盖它，也不能反向补造该别名。MoveEffectScore / PowerHigherWithConsecutiveUseOnUserSide 未登记，按共同默认保持输入；不得把连续切割的最终效果分配给这个未登记身份。C 的第三重复键由 C 附表展开。

## 2. 逐登记出现、最终绑定与具体合同

被覆盖的原段不是同时执行；copy 无源行不创建新行为。「←X」表示 copy 且最终绑定到 X 的处理器。

### 2.1 Misc 文件（主稿 §4/§5.1/§5.2/§6.2）

MoveEffectAgainstTargetScore：CrashDamageIfFailsUnusableInGravity（§6.2）。

MoveFailureCheck：StartSunWeather（§5.1）；StartRainWeather←StartSunWeather；StartSandstormWeather←StartSunWeather；StartHailWeather←StartSunWeather；StartElectricTerrain；StartGrassyTerrain；StartMistyTerrain；StartPsychicTerrain；RemoveTerrain（均 §5.1）；AddSpikesToFoeSide；AddToxicSpikesToFoeSide；AddStealthRocksToFoeSide；AddStickyWebToFoeSide（均 §5.2）；UserMakeSubstitute、RemoveAllScreensAndSafeguard（§5.2）；StartShadowSkyWeather←StartSunWeather（§5.1）。

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

MoveFailureAgainstTargetCheck：LowerTargetHPToUserHP、OHKO、CannotMakeTargetFaint（§2/§6）；OHKOIce（独立冰类型拒绝门，再采用普通 OHKO 条件；§2）；OHKOHitsUndergroundTarget←OHKO；TargetMovesBecomeElectric（§6.2）。

MoveEffectAgainstTargetScore：OHKO（§2）；OHKOIce←OHKO；OHKOHitsUndergroundTarget←OHKO；DamageTargetAlly（§2）；DoublePowerIfTargetAsleepCureTarget、DoublePowerIfTargetParalyzedCureTarget、DoublePowerIfTargetLostHPThisTurn、DoublePowerIfTargetActed、DoublePowerIfTargetNotActed（§2）；RecoilQuarterOfDamageDealt、RecoilThirdOfDamageDealtParalyzeTarget、RecoilThirdOfDamageDealtBurnTarget、RecoilHalfOfDamageDealt（§6.2）；CategoryDependsOnHigherDamagePoisonTarget←PoisonTarget（§2.1/§6.2，绑定到 BattlerOther 的 PoisonTarget）；EnsureNextMoveAlwaysHits、StartNegateTargetEvasionStatStageAndGhostImmunity、StartNegateTargetEvasionStatStageAndDarkImmunity、TargetMovesBecomeElectric（§6.2）；RemoveProtections（§6）；RemoveProtections←RemoveProtectionsBypassSubstitute（源不存在，不写入，原 RemoveProtections 目标 +7 保留）；HoopaRemoveProtectionsBypassSubstituteLowerUserDef1（§6）。

MoveEffectScore：PowerHigherWithConsecutiveUse（最终效果分读取回声侧计数，其 P 仍读连续切割）；DoublePowerIfUserLostHPThisTurn（§2）；EnsureNextCriticalHit（§2.2）；StartPreventCriticalHitsAgainstUserSide（§2.2）；UserEnduresFaintingThisTurn（§6）；StartWeakenElectricMoves、StartWeakenFireMoves、StartWeakenPhysicalDamageAgainstUserSide、StartWeakenSpecialDamageAgainstUserSide、StartWeakenDamageAgainstUserSideIfHail、RemoveScreens、ProtectUser、ProtectUserBanefulBunker、ProtectUserFromDamagingMovesKingsShield、ProtectUserFromDamagingMovesObstruct、ProtectUserFromTargetingMovesSpikyShield、ProtectUserSideFromDamagingMovesIfUserFirstTurn、ProtectUserSideFromStatusMoves、ProtectUserSideFromPriorityMoves、ProtectUserSideFromMultiTargetDamagingMoves、NormalMovesBecomeElectric（§6/§2.1/§6.2）。

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

MoveFailureAgainstTargetCheck：CureTargetStatusHealUserHalfOfTotalHP、HealUserByTargetAttackLowerTargetAttack1、HealUserByHalfOfDamageDoneIfTargetAsleep、HealUserAndAlliesQuarterOfTotalHP、HealUserAndAlliesQuarterOfTotalHPCureStatus、HealTargetHalfOfTotalHP、StartDamageTargetEachTurnIfTargetAsleep、StartLeechSeedTarget、StartPerishCountsForAllBattlers（§4）；HealTargetDependingOnGrassyTerrain←HealTargetHalfOfTotalHP。

MoveEffectAgainstTargetScore：CureTargetStatusHealUserHalfOfTotalHP、HealUserByTargetAttackLowerTargetAttack1、HealUserByHalfOfDamageDone、HealUserByThreeQuartersOfDamageDone、HealUserAndAlliesQuarterOfTotalHP、HealUserAndAlliesQuarterOfTotalHPCureStatus、HealTargetHalfOfTotalHP、HealTargetDependingOnGrassyTerrain、StartDamageTargetEachTurnIfTargetAsleep、StartLeechSeedTarget、UserFaintsLowerTargetAtkSpAtk2（§4）；HealUserByHalfOfDamageDoneIfTargetAsleep←HealUserByHalfOfDamageDone。

MoveBasePower：UserFaintsPowersUpInMistyTerrainExplosive、UserFaintsFixedDamageUserHP（§4）。

### 2.7 ChangeMoveEffect 文件（数值、恢复与誓约；主稿 §2.1/§2.2/§4/§6.2）

MoveBasePower：RandomlyDamageOrHealTarget（§2.1；数值、恢复与誓约）；HitsAllFoesAndPowersUpInPsychicTerrain（§2.1；数值、恢复与誓约）；CounterPhysicalDamage、CounterSpecialDamage、CounterDamagePlusHalf（§2.2；数值、恢复与誓约）；PowerDependsOnUserStockpile（§2.1；数值、恢复与誓约）。

MoveEffectScore：RandomlyDamageOrHealTarget（§2.1；数值、恢复与誓约）；DoublePowerAfterFusionFlare、DoublePowerAfterFusionBolt（§2.2；数值、恢复与誓约）；CounterPhysicalDamage、CounterSpecialDamage、CounterDamagePlusHalf（§2.2；数值、恢复与誓约）；UserAddStockpileRaiseDefSpDef1、HealUserDependingOnUserStockpile（§4；数值、恢复与誓约）；PowerDependsOnUserStockpile（§2.1；数值、恢复与誓约）；GrassPledge、FirePledge、WaterPledge（§6.2；数值、恢复与誓约）。

MoveFailureAgainstTargetCheck：HealAllyOrDamageFoe（§4；数值、恢复与誓约）。

MoveEffectAgainstTargetScore：HealAllyOrDamageFoe（§4；数值、恢复与誓约）。

MoveFailureCheck：UserAddStockpileRaiseDefSpDef1（§4；数值、恢复与誓约）；PowerDependsOnUserStockpile、HealUserDependingOnUserStockpile（§2.1/§4；数值、恢复与誓约）。

## 3. 场域收益匹配数据

主稿 §5.1 完整给量值、阵营符号、技能与伞门；下表给效果名精确效果标识，组内任一匹配一次，不按多个匹配叠加。仅提取字面值。

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

A 为共同评分/数值/状态阶级，WP51 为选择/技能/资源；本包补具体 B 处理器。物品评级、调用/替换、行动与换出控制仍 C，完整设施规则见各设施章节；真实写入和数值依 WP43–50。低档不启 MoveBasePower、ScoreMoves 关不启效果分，以及 copy 失败后的默认行为不能用完整目录名代替。运行与插件组合仍未验证。
