# WP52-B 有界登记、覆盖与数据 v1

状态：**ReviewPending（随[主稿](wp52-b-field-damage-healing-and-target-evaluation.md)A～F送审，尚未外审）**。本表仅审计定位，具体条件/数值/分支以主稿合同为准，不以登记索引替代行为。

## 1. 集合与注册语义

原WP52-A附表将B定位为247出现；本批具名移入ChangeMoveEffect中23条纯数值/恢复/誓约登记，当前B270出现／268不同有效键，C190→167出现；A334、WP51已有15不变，总786出现／783不同出现键，实际最终782有效键（另两处C的缺源copy在C具体展开）。源登记784语句／12文件；覆盖边界变化是责任修正，不修改旧已审材料、不把C提前算已提取。移入的14身份列于下表标记“由C定位移入”。

同族同键后add替代旧处理；copy抓取当时已定义的源，缺源则不改目的。本包两组：连续切割分由:238覆盖:220；解除保护:1190缺源copy不生效、保留:1175。两个不能按“出现两次”加分；MoveEffectScore PowerHigherWithConsecutiveUseOnUserSide未登记，RemoveProtectionsBypassSubstitute目标分未登记，按共用默认保持输入。C的第三重复键在C展开。

## 2. 逐登记出现、最终绑定与具体合同

文件相对`Data/Scripts/011_Battle/`；最后一列给该(族,身份)在整个固定文本登记完成后的处理器来源，只是审计，不提倡同样架构。被覆盖的原段不是同时执行；copy无源行不创建新行为。

| 文件:行 | 族／身份 | 登记方式 | 合同 | 最终处理器来源／责任 |
| --- | --- | --- | --- | --- |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:157 | MoveEffectAgainstTargetScore / `CrashDamageIfFailsUnusableInGravity` | add | 主稿§6.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:157 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:169 | MoveFailureCheck / `StartSunWeather` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:169 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:174 | MoveEffectScore / `StartSunWeather` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:174 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:193 | MoveFailureCheck / `StartRainWeather` | copy←StartSunWeather | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:169 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:195 | MoveEffectScore / `StartRainWeather` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:195 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:214 | MoveFailureCheck / `StartSandstormWeather` | copy←StartSunWeather | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:169 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:216 | MoveEffectScore / `StartSandstormWeather` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:216 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:235 | MoveFailureCheck / `StartHailWeather` | copy←StartSunWeather | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:169 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:237 | MoveEffectScore / `StartHailWeather` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:237 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:256 | MoveFailureCheck / `StartElectricTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:256 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:261 | MoveEffectScore / `StartElectricTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:261 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:278 | MoveFailureCheck / `StartGrassyTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:278 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:283 | MoveEffectScore / `StartGrassyTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:283 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:300 | MoveFailureCheck / `StartMistyTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:300 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:305 | MoveEffectScore / `StartMistyTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:305 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:322 | MoveFailureCheck / `StartPsychicTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:322 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:327 | MoveEffectScore / `StartPsychicTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:327 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:344 | MoveFailureCheck / `RemoveTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:344 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:349 | MoveEffectScore / `RemoveTerrain` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:349 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:358 | MoveFailureCheck / `AddSpikesToFoeSide` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:358 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:363 | MoveEffectScore / `AddSpikesToFoeSide` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:363 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:386 | MoveFailureCheck / `AddToxicSpikesToFoeSide` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:386 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:391 | MoveEffectScore / `AddToxicSpikesToFoeSide` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:391 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:414 | MoveFailureCheck / `AddStealthRocksToFoeSide` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:414 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:419 | MoveEffectScore / `AddStealthRocksToFoeSide` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:419 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:440 | MoveFailureCheck / `AddStickyWebToFoeSide` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:440 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:445 | MoveEffectScore / `AddStickyWebToFoeSide` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:445 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:511 | MoveFailureCheck / `UserMakeSubstitute` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:511 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:517 | MoveEffectScore / `UserMakeSubstitute` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:517 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:560 | MoveFailureAgainstTargetCheck / `AttackTwoTurnsLater` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:560 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:565 | MoveEffectScore / `AttackTwoTurnsLater` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:565 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:614 | MoveEffectScore / `AllBattlersLoseHalfHPUserSkipsNextTurn` | add | 主稿§4 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:614 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:639 | MoveEffectScore / `UserLosesHalfHP` | add | 主稿§4 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:639 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:650 | MoveFailureCheck / `StartShadowSkyWeather` | copy←StartSunWeather | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:169 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:652 | MoveEffectScore / `StartShadowSkyWeather` | add | 主稿§5.1 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:652 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:671 | MoveFailureCheck / `RemoveAllScreensAndSafeguard` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:671 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:683 | MoveEffectScore / `RemoveAllScreensAndSafeguard` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:683 |
| 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:970 | MoveFailureAgainstTargetCheck / `LowerTargetEvasion1RemoveSideEffects` | add | 主稿§5.2 | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:970 |
| 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:993 | MoveEffectAgainstTargetScore / `LowerTargetEvasion1RemoveSideEffects` | add | 主稿§5.2 | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:993 |
| 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:1588 | MoveEffectAgainstTargetScore / `UserTargetAverageHP` | add | 主稿§4 | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:1588 |
| 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:1600 | MoveFailureCheck / `StartUserSideDoubleSpeed` | add | 主稿§5.2 | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:1600 |
| 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:1605 | MoveEffectScore / `StartUserSideDoubleSpeed` | add | 主稿§5.2 | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:1605 |
| 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:1635 | MoveEffectScore / `StartSwapAllBattlersBaseDefensiveStats` | add | 主稿§5.2 | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:1635 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:614 | MoveBasePower / `FlinchTargetDoublePowerIfTargetInSky` | add | 主稿§2.1 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:614 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:4 | MoveBasePower / `FixedDamage20` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:4 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:13 | MoveBasePower / `FixedDamage40` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:13 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:22 | MoveBasePower / `FixedDamageHalfTargetHP` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:22 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:31 | MoveBasePower / `FixedDamageUserLevel` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:31 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:40 | MoveBasePower / `FixedDamageUserLevelRandom` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:40 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:49 | MoveFailureAgainstTargetCheck / `LowerTargetHPToUserHP` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:49 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:54 | MoveBasePower / `LowerTargetHPToUserHP` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:54 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:63 | MoveFailureAgainstTargetCheck / `OHKO` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:63 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:70 | MoveBasePower / `OHKO` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:70 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:75 | MoveEffectAgainstTargetScore / `OHKO` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:75 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:91 | MoveFailureAgainstTargetCheck / `OHKOIce` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:91 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:97 | MoveBasePower / `OHKOIce` | copy←OHKO | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:70 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:99 | MoveEffectAgainstTargetScore / `OHKOIce` | copy←OHKO | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:75 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:105 | MoveFailureAgainstTargetCheck / `OHKOHitsUndergroundTarget` | copy←OHKO | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:63 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:107 | MoveBasePower / `OHKOHitsUndergroundTarget` | copy←OHKO | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:70 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:109 | MoveEffectAgainstTargetScore / `OHKOHitsUndergroundTarget` | copy←OHKO | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:75 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:115 | MoveEffectAgainstTargetScore / `DamageTargetAlly` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:115 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 | MoveBasePower / `PowerHigherWithUserHP` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:140 | MoveBasePower / `PowerLowerWithUserHP` | copy←PowerHigherWithUserHP | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:146 | MoveBasePower / `PowerHigherWithTargetHP` | copy←PowerHigherWithUserHP | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:152 | MoveBasePower / `PowerHigherWithUserHappiness` | copy←PowerHigherWithUserHP | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:158 | MoveBasePower / `PowerLowerWithUserHappiness` | copy←PowerHigherWithUserHP | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:164 | MoveBasePower / `PowerHigherWithUserPositiveStatStages` | copy←PowerHigherWithUserHP | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:170 | MoveBasePower / `PowerHigherWithTargetPositiveStatStages` | copy←PowerHigherWithUserHP | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:176 | MoveBasePower / `PowerHigherWithUserFasterThanTarget` | copy←PowerHigherWithUserHP | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:182 | MoveBasePower / `PowerHigherWithTargetFasterThanUser` | copy←PowerHigherWithUserHP | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:131 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:188 | MoveBasePower / `PowerHigherWithLessPP` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:188 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:200 | MoveBasePower / `PowerHigherWithTargetWeight` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:200 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:209 | MoveBasePower / `PowerHigherWithUserHeavierThanTarget` | copy←PowerHigherWithTargetWeight | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:200 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:215 | MoveBasePower / `PowerHigherWithConsecutiveUse` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:215 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:220 | MoveEffectScore / `PowerHigherWithConsecutiveUse` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:238 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:233 | MoveBasePower / `PowerHigherWithConsecutiveUseOnUserSide` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:233 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:238 | MoveEffectScore / `PowerHigherWithConsecutiveUse` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:238 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:251 | MoveBasePower / `RandomPowerDoublePowerIfTargetUnderground` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:251 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:261 | MoveBasePower / `DoublePowerIfTargetHPLessThanHalf` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:261 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:270 | MoveBasePower / `DoublePowerIfUserPoisonedBurnedParalyzed` | copy←DoublePowerIfTargetHPLessThanHalf | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:261 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:276 | MoveBasePower / `DoublePowerIfTargetAsleepCureTarget` | copy←DoublePowerIfTargetHPLessThanHalf | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:261 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:278 | MoveEffectAgainstTargetScore / `DoublePowerIfTargetAsleepCureTarget` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:278 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:294 | MoveBasePower / `DoublePowerIfTargetPoisoned` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:294 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:303 | MoveBasePower / `DoublePowerIfTargetParalyzedCureTarget` | copy←DoublePowerIfTargetPoisoned | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:294 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:305 | MoveEffectAgainstTargetScore / `DoublePowerIfTargetParalyzedCureTarget` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:305 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:321 | MoveBasePower / `DoublePowerIfTargetStatusProblem` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:321 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:330 | MoveBasePower / `DoublePowerIfUserHasNoItem` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:330 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:340 | MoveBasePower / `DoublePowerIfTargetUnderwater` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:340 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:349 | MoveBasePower / `DoublePowerIfTargetUnderground` | copy←DoublePowerIfTargetUnderwater | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:340 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:355 | MoveBasePower / `DoublePowerIfTargetInSky` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:355 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:364 | MoveBasePower / `DoublePowerInElectricTerrain` | copy←DoublePowerIfTargetInSky | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:355 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:370 | MoveBasePower / `DoublePowerIfUserLastMoveFailed` | copy←DoublePowerIfTargetInSky | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:355 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:376 | MoveBasePower / `DoublePowerIfAllyFaintedLastTurn` | copy←DoublePowerIfTargetInSky | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:355 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:382 | MoveEffectScore / `DoublePowerIfUserLostHPThisTurn` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:382 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:396 | MoveEffectAgainstTargetScore / `DoublePowerIfTargetLostHPThisTurn` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:396 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:416 | MoveEffectAgainstTargetScore / `DoublePowerIfTargetActed` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:416 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:426 | MoveEffectAgainstTargetScore / `DoublePowerIfTargetNotActed` | add | 主稿§2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:426 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:441 | MoveEffectScore / `EnsureNextCriticalHit` | add | 主稿§2.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:441 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:476 | MoveFailureCheck / `StartPreventCriticalHitsAgainstUserSide` | add | 主稿§2.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:476 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:481 | MoveEffectScore / `StartPreventCriticalHitsAgainstUserSide` | add | 主稿§2.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:481 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:531 | MoveFailureAgainstTargetCheck / `CannotMakeTargetFaint` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:531 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:540 | MoveEffectScore / `UserEnduresFaintingThisTurn` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:540 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:569 | MoveFailureCheck / `StartWeakenElectricMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:569 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:575 | MoveEffectScore / `StartWeakenElectricMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:575 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:605 | MoveFailureCheck / `StartWeakenFireMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:605 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:611 | MoveEffectScore / `StartWeakenFireMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:611 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:641 | MoveFailureCheck / `StartWeakenPhysicalDamageAgainstUserSide` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:641 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:646 | MoveEffectScore / `StartWeakenPhysicalDamageAgainstUserSide` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:646 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:671 | MoveFailureCheck / `StartWeakenSpecialDamageAgainstUserSide` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:671 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:676 | MoveEffectScore / `StartWeakenSpecialDamageAgainstUserSide` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:676 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:701 | MoveFailureCheck / `StartWeakenDamageAgainstUserSideIfHail` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:701 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:708 | MoveEffectScore / `StartWeakenDamageAgainstUserSideIfHail` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:708 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:728 | MoveEffectScore / `RemoveScreens` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:728 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:751 | MoveEffectScore / `ProtectUser` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:751 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:795 | MoveEffectScore / `ProtectUserBanefulBunker` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:795 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:847 | MoveEffectScore / `ProtectUserFromDamagingMovesKingsShield` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:847 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:900 | MoveEffectScore / `ProtectUserFromDamagingMovesObstruct` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:900 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:949 | MoveEffectScore / `ProtectUserFromTargetingMovesSpikyShield` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:949 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:997 | MoveFailureCheck / `ProtectUserSideFromDamagingMovesIfUserFirstTurn` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:997 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1002 | MoveEffectScore / `ProtectUserSideFromDamagingMovesIfUserFirstTurn` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1002 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1043 | MoveFailureCheck / `ProtectUserSideFromStatusMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1043 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1048 | MoveEffectScore / `ProtectUserSideFromStatusMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1048 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1084 | MoveFailureCheck / `ProtectUserSideFromPriorityMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1084 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1089 | MoveEffectScore / `ProtectUserSideFromPriorityMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1089 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1129 | MoveFailureCheck / `ProtectUserSideFromMultiTargetDamagingMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1129 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1134 | MoveEffectScore / `ProtectUserSideFromMultiTargetDamagingMoves` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1134 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1175 | MoveEffectAgainstTargetScore / `RemoveProtections` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1175 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1190 | MoveEffectAgainstTargetScore / `RemoveProtections` | copy←RemoveProtectionsBypassSubstitute（源不存在，不写入） | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1175 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1196 | MoveFailureCheck / `HoopaRemoveProtectionsBypassSubstituteLowerUserDef1` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1196 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1201 | MoveEffectAgainstTargetScore / `HoopaRemoveProtectionsBypassSubstituteLowerUserDef1` | add | 主稿§6 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1201 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1212 | MoveEffectAgainstTargetScore / `RecoilQuarterOfDamageDealt` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1212 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1229 | MoveEffectAgainstTargetScore / `RecoilThirdOfDamageDealtParalyzeTarget` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1229 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1252 | MoveEffectAgainstTargetScore / `RecoilThirdOfDamageDealtBurnTarget` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1252 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1275 | MoveEffectAgainstTargetScore / `RecoilHalfOfDamageDealt` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1275 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1292 | MoveBasePower / `EffectivenessIncludesFlyingType` | add | 主稿§2.1／§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1292 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1306 | MoveEffectAgainstTargetScore / `CategoryDependsOnHigherDamagePoisonTarget` | copy←PoisonTarget | 主稿§2.1／§6.2 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:98 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1332 | MoveFailureCheck / `EnsureNextMoveAlwaysHits` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1332 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1337 | MoveEffectAgainstTargetScore / `EnsureNextMoveAlwaysHits` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1337 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1364 | MoveEffectAgainstTargetScore / `StartNegateTargetEvasionStatStageAndGhostImmunity` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1364 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1384 | MoveEffectAgainstTargetScore / `StartNegateTargetEvasionStatStageAndDarkImmunity` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1384 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1414 | MoveBasePower / `TypeDependsOnUserIVs` | add | 主稿§2.1 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1414 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1423 | MoveFailureCheck / `TypeAndPowerDependOnUserBerry` | add | 主稿§2.1 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1423 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1431 | MoveBasePower / `TypeAndPowerDependOnUserBerry` | add | 主稿§2.1 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1431 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1456 | MoveFailureCheck / `TypeDependsOnUserMorpekoFormRaiseUserSpeed1` | add | 主稿§2.1 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1456 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1461 | MoveEffectScore / `TypeDependsOnUserMorpekoFormRaiseUserSpeed1` | copy←RaiseUserSpeed1 | 主稿§2.1 | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:10 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1467 | MoveBasePower / `TypeAndPowerDependOnWeather` | add | 主稿§2.1 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1467 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1476 | MoveBasePower / `TypeAndPowerDependOnTerrain` | copy←TypeAndPowerDependOnWeather | 主稿§2.1 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1467 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1482 | MoveFailureAgainstTargetCheck / `TargetMovesBecomeElectric` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1482 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1487 | MoveEffectAgainstTargetScore / `TargetMovesBecomeElectric` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1487 |
| 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1527 | MoveEffectScore / `NormalMovesBecomeElectric` | add | 主稿§6.2 | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:1527 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:4 | MoveBasePower / `HitTwoTimes` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:4 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:9 | MoveEffectAgainstTargetScore / `HitTwoTimes` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:9 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:25 | MoveBasePower / `HitTwoTimesPoisonTarget` | copy←HitTwoTimes | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:4 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:27 | MoveEffectAgainstTargetScore / `HitTwoTimesPoisonTarget` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:27 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:43 | MoveBasePower / `HitTwoTimesFlinchTarget` | copy←HitTwoTimes | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:4 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:45 | MoveEffectAgainstTargetScore / `HitTwoTimesFlinchTarget` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:45 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:60 | MoveBasePower / `HitTwoTimesTargetThenTargetAlly` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:60 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:69 | MoveBasePower / `HitThreeTimesPowersUpWithEachHit` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:69 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:74 | MoveEffectAgainstTargetScore / `HitThreeTimesPowersUpWithEachHit` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:74 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:89 | MoveBasePower / `HitThreeTimesAlwaysCriticalHit` | copy←HitTwoTimes | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:4 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:91 | MoveEffectAgainstTargetScore / `HitThreeTimesAlwaysCriticalHit` | copy←HitTwoTimes | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:9 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:97 | MoveBasePower / `HitTwoToFiveTimes` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:97 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:103 | MoveEffectAgainstTargetScore / `HitTwoToFiveTimes` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:103 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:119 | MoveBasePower / `HitTwoToFiveTimesOrThreeForAshGreninja` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:119 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:128 | MoveEffectAgainstTargetScore / `HitTwoToFiveTimesOrThreeForAshGreninja` | copy←HitTwoToFiveTimes | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:103 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:134 | MoveBasePower / `HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1` | copy←HitTwoToFiveTimes | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:97 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:136 | MoveEffectAgainstTargetScore / `HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:136 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:151 | MoveFailureCheck / `HitOncePerUserTeamMember` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:151 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:162 | MoveBasePower / `HitOncePerUserTeamMember` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:162 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:171 | MoveEffectAgainstTargetScore / `HitOncePerUserTeamMember` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:171 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:190 | MoveEffectScore / `AttackAndSkipNextTurn` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:190 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:203 | MoveEffectAgainstTargetScore / `TwoTurnAttack` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:203 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:256 | MoveBasePower / `TwoTurnAttackOneTurnInSun` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:256 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:261 | MoveEffectAgainstTargetScore / `TwoTurnAttackOneTurnInSun` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:261 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:274 | MoveEffectAgainstTargetScore / `TwoTurnAttackParalyzeTarget` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:274 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:290 | MoveEffectAgainstTargetScore / `TwoTurnAttackBurnTarget` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:290 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:306 | MoveEffectAgainstTargetScore / `TwoTurnAttackFlinchTarget` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:306 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:322 | MoveFailureCheck / `TwoTurnAttackRaiseUserSpAtkSpDefSpd2` | copy←RaiseUserAtkDef1 | 主稿§3 | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb:324 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:324 | MoveEffectAgainstTargetScore / `TwoTurnAttackRaiseUserSpAtkSpDefSpd2` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:324 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:339 | MoveEffectAgainstTargetScore / `TwoTurnAttackChargeRaiseUserDefense1` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:339 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:355 | MoveEffectAgainstTargetScore / `TwoTurnAttackChargeRaiseUserSpAtk1` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:355 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:371 | MoveEffectAgainstTargetScore / `TwoTurnAttackInvulnerableUnderground` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:371 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:392 | MoveEffectAgainstTargetScore / `TwoTurnAttackInvulnerableUnderwater` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:392 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:413 | MoveEffectAgainstTargetScore / `TwoTurnAttackInvulnerableInSky` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:413 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:434 | MoveEffectAgainstTargetScore / `TwoTurnAttackInvulnerableInSkyParalyzeTarget` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:434 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:450 | MoveFailureAgainstTargetCheck / `TwoTurnAttackInvulnerableInSkyTargetCannotAct` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:450 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:460 | MoveEffectAgainstTargetScore / `TwoTurnAttackInvulnerableInSkyTargetCannotAct` | copy←TwoTurnAttackInvulnerableInSky | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:413 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:466 | MoveEffectAgainstTargetScore / `TwoTurnAttackInvulnerableRemoveProtections` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:466 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:494 | MoveBasePower / `MultiTurnAttackPowersUpEachTurn` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:494 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:507 | MoveBasePower / `MultiTurnAttackBideThenReturnDoubleDamage` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:507 |
| 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:512 | MoveEffectScore / `MultiTurnAttackBideThenReturnDoubleDamage` | add | 主稿§3 | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:512 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:4 | MoveFailureCheck / `HealUserFullyAndFallAsleep` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:4 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:12 | MoveEffectScore / `HealUserFullyAndFallAsleep` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:12 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:37 | MoveFailureCheck / `HealUserHalfOfTotalHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:37 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:42 | MoveEffectScore / `HealUserHalfOfTotalHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:42 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:56 | MoveFailureCheck / `HealUserDependingOnWeather` | copy←HealUserHalfOfTotalHP | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:37 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:58 | MoveEffectScore / `HealUserDependingOnWeather` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:58 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:77 | MoveFailureCheck / `HealUserDependingOnSandstorm` | copy←HealUserHalfOfTotalHP | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:37 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:79 | MoveEffectScore / `HealUserDependingOnSandstorm` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:79 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:92 | MoveFailureCheck / `HealUserHalfOfTotalHPLoseFlyingTypeThisTurn` | copy←HealUserHalfOfTotalHP | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:37 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:94 | MoveEffectScore / `HealUserHalfOfTotalHPLoseFlyingTypeThisTurn` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:94 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:108 | MoveFailureAgainstTargetCheck / `CureTargetStatusHealUserHalfOfTotalHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:108 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:113 | MoveEffectAgainstTargetScore / `CureTargetStatusHealUserHalfOfTotalHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:113 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:127 | MoveFailureAgainstTargetCheck / `HealUserByTargetAttackLowerTargetAttack1` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:127 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:135 | MoveEffectAgainstTargetScore / `HealUserByTargetAttackLowerTargetAttack1` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:135 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:166 | MoveEffectAgainstTargetScore / `HealUserByHalfOfDamageDone` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:166 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:193 | MoveFailureAgainstTargetCheck / `HealUserByHalfOfDamageDoneIfTargetAsleep` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:193 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:198 | MoveEffectAgainstTargetScore / `HealUserByHalfOfDamageDoneIfTargetAsleep` | copy←HealUserByHalfOfDamageDone | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:166 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:204 | MoveEffectAgainstTargetScore / `HealUserByThreeQuartersOfDamageDone` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:204 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:231 | MoveFailureAgainstTargetCheck / `HealUserAndAlliesQuarterOfTotalHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:231 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:236 | MoveEffectAgainstTargetScore / `HealUserAndAlliesQuarterOfTotalHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:236 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:254 | MoveFailureAgainstTargetCheck / `HealUserAndAlliesQuarterOfTotalHPCureStatus` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:254 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:259 | MoveEffectAgainstTargetScore / `HealUserAndAlliesQuarterOfTotalHPCureStatus` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:259 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:275 | MoveFailureAgainstTargetCheck / `HealTargetHalfOfTotalHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:275 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:280 | MoveEffectAgainstTargetScore / `HealTargetHalfOfTotalHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:280 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:303 | MoveFailureAgainstTargetCheck / `HealTargetDependingOnGrassyTerrain` | copy←HealTargetHalfOfTotalHP | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:275 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:305 | MoveEffectAgainstTargetScore / `HealTargetDependingOnGrassyTerrain` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:305 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:327 | MoveFailureCheck / `HealUserPositionNextTurn` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:327 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:332 | MoveEffectScore / `HealUserPositionNextTurn` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:332 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:349 | MoveFailureCheck / `StartHealUserEachTurn` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:349 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:354 | MoveEffectScore / `StartHealUserEachTurn` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:354 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:365 | MoveFailureCheck / `StartHealUserEachTurnTrapUserInBattle` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:365 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:370 | MoveEffectScore / `StartHealUserEachTurnTrapUserInBattle` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:370 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:382 | MoveFailureAgainstTargetCheck / `StartDamageTargetEachTurnIfTargetAsleep` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:382 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:387 | MoveEffectAgainstTargetScore / `StartDamageTargetEachTurnIfTargetAsleep` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:387 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:397 | MoveFailureAgainstTargetCheck / `StartLeechSeedTarget` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:397 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:404 | MoveEffectAgainstTargetScore / `StartLeechSeedTarget` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:404 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:434 | MoveEffectScore / `UserLosesHalfOfTotalHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:434 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:457 | MoveFailureCheck / `UserLosesHalfOfTotalHPExplosive` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:457 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:462 | MoveEffectScore / `UserLosesHalfOfTotalHPExplosive` | copy←UserLosesHalfOfTotalHP | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:434 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:468 | MoveFailureCheck / `UserFaintsExplosive` | copy←UserLosesHalfOfTotalHPExplosive | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:457 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:470 | MoveEffectScore / `UserFaintsExplosive` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:470 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:493 | MoveFailureCheck / `UserFaintsPowersUpInMistyTerrainExplosive` | copy←UserFaintsExplosive | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:457 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:495 | MoveBasePower / `UserFaintsPowersUpInMistyTerrainExplosive` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:495 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:501 | MoveEffectScore / `UserFaintsPowersUpInMistyTerrainExplosive` | copy←UserFaintsExplosive | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:470 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:507 | MoveBasePower / `UserFaintsFixedDamageUserHP` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:507 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:512 | MoveEffectScore / `UserFaintsFixedDamageUserHP` | copy←UserFaintsExplosive | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:470 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:518 | MoveEffectAgainstTargetScore / `UserFaintsLowerTargetAtkSpAtk2` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:518 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:543 | MoveFailureCheck / `UserFaintsHealAndCureReplacement` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:543 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:548 | MoveEffectScore / `UserFaintsHealAndCureReplacement` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:548 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:581 | MoveFailureCheck / `UserFaintsHealAndCureReplacementRestorePP` | copy←UserFaintsHealAndCureReplacement | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:543 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:583 | MoveEffectScore / `UserFaintsHealAndCureReplacementRestorePP` | copy←UserFaintsHealAndCureReplacement | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:548 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:589 | MoveFailureAgainstTargetCheck / `StartPerishCountsForAllBattlers` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:589 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:597 | MoveEffectScore / `StartPerishCountsForAllBattlers` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:597 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:637 | MoveFailureCheck / `AttackerFaintsIfUserFaints` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:637 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:642 | MoveEffectScore / `AttackerFaintsIfUserFaints` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:642 |
| 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:665 | MoveEffectScore / `SetAttackerMovePPTo0IfUserFaints` | add | 主稿§4 | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:665 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:42 | MoveBasePower / `RandomlyDamageOrHealTarget` | add | 主稿§2.1 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:42；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:47 | MoveEffectScore / `RandomlyDamageOrHealTarget` | add | 主稿§2.1 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:47；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:57 | MoveFailureAgainstTargetCheck / `HealAllyOrDamageFoe` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:57；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:62 | MoveEffectAgainstTargetScore / `HealAllyOrDamageFoe` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:62；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:187 | MoveBasePower / `HitsAllFoesAndPowersUpInPsychicTerrain` | add | 主稿§2.1 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:187；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:214 | MoveEffectScore / `DoublePowerAfterFusionFlare` | add | 主稿§2.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:214；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:227 | MoveEffectScore / `DoublePowerAfterFusionBolt` | add | 主稿§2.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:227；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:255 | MoveBasePower / `CounterPhysicalDamage` | add | 主稿§2.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:255；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:260 | MoveEffectScore / `CounterPhysicalDamage` | add | 主稿§2.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:260；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:287 | MoveBasePower / `CounterSpecialDamage` | add | 主稿§2.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:287；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:292 | MoveEffectScore / `CounterSpecialDamage` | add | 主稿§2.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:292；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:319 | MoveBasePower / `CounterDamagePlusHalf` | add | 主稿§2.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:319；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:324 | MoveEffectScore / `CounterDamagePlusHalf` | add | 主稿§2.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:324；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:349 | MoveFailureCheck / `UserAddStockpileRaiseDefSpDef1` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:349；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:354 | MoveEffectScore / `UserAddStockpileRaiseDefSpDef1` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:354；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:370 | MoveFailureCheck / `PowerDependsOnUserStockpile` | add | 主稿§2.1 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:370；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:375 | MoveBasePower / `PowerDependsOnUserStockpile` | add | 主稿§2.1 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:375；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:380 | MoveEffectScore / `PowerDependsOnUserStockpile` | add | 主稿§2.1 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:380；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:392 | MoveFailureCheck / `HealUserDependingOnUserStockpile` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:392；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:401 | MoveEffectScore / `HealUserDependingOnUserStockpile` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:401；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:418 | MoveEffectScore / `GrassPledge` | add | 主稿§6.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:418；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:431 | MoveEffectScore / `FirePledge` | add | 主稿§6.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:431；由C定位移入 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:444 | MoveEffectScore / `WaterPledge` | add | 主稿§6.2 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:444；由C定位移入 |

## 3. 场域收益匹配数据

主稿§5.1完整给量值、阵营符号、技能与伞门；下表给效果名精确审计身份，组内任一匹配一次，不按多个匹配叠加。数据来自GenericEffects:655–685/759–769，仅提取字面值。

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

A为共同评分/数值/状态阶级，WP51为选择/技能/资源；本包补具体B处理器。物品评级、调用/替换、行动与换出控制仍C，完整设施仍各既定包；真实写入和数值依WP43–50。低档不启MoveBasePower、ScoreMoves关不启效果分，以及copy失败后的默认行为不能用完整目录名代替。全局运行/插件组合与WP79未关闭。
