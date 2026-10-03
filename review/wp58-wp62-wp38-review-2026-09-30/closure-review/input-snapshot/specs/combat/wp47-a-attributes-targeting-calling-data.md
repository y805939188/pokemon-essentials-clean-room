# WP47-A 覆盖与默认数据附表 v1

状态：Reviewed（限定静态范围，2026-09-27首审PASS_SCOPED；管理性回填）。表中效果身份／物品身份是审计及行为数据，不是未来类／API设计。固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

## 1. 完整调用排除表

“常”表示所有世代明列排除，“≥6”表示仅世代≥6追加，“—”表示该明列名单未排除（仍可能被其它资格／标记拒绝）。各列对应主稿§6七个调用／复制入口；按效果字符串匹配，不是按招式显示名或父级族匹配。仿效／抢先／挥指／借助／梦话／模仿／写生各自集合如下，不将注释掉的行当有效数据。

| 效果身份 | 仿效 | 抢先 | 挥指 | 借助 | 梦话 | 模仿 | 写生 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `AllBattlersLoseHalfHPUserSkipsNextTurn` | — | — | — | ≥6 | 常 | — | — |
| `AttackerFaintsIfUserFaints` | 常 | — | 常 | 常 | — | — | — |
| `BounceBackProblemCausingStatusMoves` | 常 | — | 常 | 常 | — | — | — |
| `BurnAttackerBeforeUserActs` | 常 | 常 | 常 | 常 | 常 | — | — |
| `CounterDamagePlusHalf` | 常 | 常 | 常 | 常 | — | — | — |
| `CounterPhysicalDamage` | 常 | 常 | 常 | 常 | — | — | — |
| `CounterSpecialDamage` | 常 | 常 | 常 | 常 | — | — | — |
| `DoesNothingCongratulations` | 常 | — | 常 | 常 | — | — | — |
| `DoesNothingFailsIfNoAlly` | 常 | — | 常 | 常 | — | — | — |
| `FailsIfUserDamagedThisTurn` | 常 | 常 | 常 | 常 | 常 | — | — |
| `FailsIfUserNotConsumedBerry` | 常 | 常 | 常 | 常 | 常 | — | — |
| `FlinchTargetFailsIfUserNotAsleep` | — | — | 常 | — | — | — | — |
| `MultiTurnAttackBideThenReturnDoubleDamage` | — | — | — | — | 常 | — | — |
| `MultiTurnAttackPreventSleeping` | — | — | — | — | 常 | — | — |
| `PowerUpAllyMove` | 常 | — | 常 | 常 | — | — | — |
| `ProtectUser` | 常 | — | 常 | 常 | — | — | — |
| `ProtectUserBanefulBunker` | 常 | — | 常 | 常 | — | — | — |
| `ProtectUserFromDamagingMovesKingsShield` | 常 | — | 常 | 常 | — | — | — |
| `ProtectUserFromDamagingMovesObstruct` | 常 | — | 常 | 常 | — | — | — |
| `ProtectUserFromTargetingMovesSpikyShield` | 常 | — | 常 | 常 | — | — | — |
| `ProtectUserSideFromDamagingMovesIfUserFirstTurn` | 常 | — | 常 | 常 | — | — | — |
| `ProtectUserSideFromMultiTargetDamagingMoves` | 常 | — | 常 | 常 | — | — | — |
| `ProtectUserSideFromPriorityMoves` | 常 | — | 常 | 常 | — | — | — |
| `ProtectUserSideFromStatusMoves` | 常 | — | 常 | 常 | — | — | — |
| `RedirectAllMovesToTarget` | 常 | — | 常 | 常 | — | — | — |
| `RedirectAllMovesToUser` | 常 | — | 常 | 常 | — | — | — |
| `ReduceAttackerMovePPTo0IfUserFaints` | 常 | — | 常 | 常 | — | — | — |
| `RemoveProtections` | 常 | — | 常 | 常 | — | — | — |
| `ReplaceMoveThisBattleWithTargetLastMoveUsed` | 常 | — | 常 | 常 | 常 | 常 | — |
| `ReplaceMoveWithTargetLastMoveUsed` | 常 | — | 常 | 常 | 常 | 常 | 常 |
| `StealAndUseBeneficialStatusMove` | 常 | — | 常 | 常 | — | — | — |
| `Struggle` | 常 | 常 | 常 | 常 | 常 | 常 | 常 |
| `SwitchOutTargetDamagingMove` | ≥6 | — | — | 常 | — | — | — |
| `SwitchOutTargetStatusMove` | ≥6 | — | — | ≥6 | — | — | — |
| `TargetActsLast` | — | — | 常 | — | — | — | — |
| `TargetActsNext` | — | — | 常 | — | — | — | — |
| `TargetTakesUserItem` | 常 | — | 常 | 常 | — | — | — |
| `TargetUsesItsLastUsedMoveAgain` | — | — | 常 | — | — | — | — |
| `TransformUserIntoTarget` | 常 | — | 常 | 常 | — | 常 | — |
| `TwoTurnAttack` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackBurnTarget` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackChargeRaiseUserDefense1` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackFlinchTarget` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackInvulnerableInSky` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackInvulnerableInSkyParalyzeTarget` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackInvulnerableInSkyTargetCannotAct` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackInvulnerableRemoveProtections` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackInvulnerableUnderground` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackInvulnerableUnderwater` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackOneTurnInSun` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackParalyzeTarget` | — | — | — | ≥6 | 常 | — | — |
| `TwoTurnAttackRaiseUserSpAtkSpDefSpd2` | — | — | — | ≥6 | 常 | — | — |
| `UseLastMoveUsed` | 常 | — | 常 | 常 | 常 | — | — |
| `UseLastMoveUsedByTarget` | 常 | — | 常 | 常 | 常 | — | — |
| `UseMoveDependingOnEnvironment` | 常 | — | 常 | ≥6 | 常 | — | — |
| `UseMoveTargetIsAboutToUse` | 常 | — | 常 | 常 | 常 | — | — |
| `UseRandomMove` | 常 | — | 常 | 常 | 常 | 常 | — |
| `UseRandomMoveFromUserParty` | 常 | — | 常 | 常 | 常 | — | — |
| `UseRandomUserMoveIfAsleep` | 常 | — | 常 | 常 | 常 | — | — |
| `UsedAfterUserTakesPhysicalDamage` | 常 | 常 | 常 | 常 | 常 | — | — |
| `UserEnduresFaintingThisTurn` | 常 | — | 常 | 常 | — | — | — |
| `UserTakesTargetItem` | 常 | 常 | 常 | 常 | — | — | — |
| `UserTargetSwapItems` | 常 | — | 常 | 常 | — | — | — |

逐列数据量（常＋≥6新增）：仿效 41＋2；抢先 9＋0；挥指 45＋0；借助 41＋16；梦话 30＋0；模仿 5＋0；写生 2＋0。不同入口候选集合和额外过滤见主稿§6，标“—”不是无条件允许。

特别保留：ReduceAttackerMovePPTo0IfUserFaints与实际SetAttackerMovePPTo0IfUserFaints不是同一字符串；未将Meteor Beam等未明列项补进“两回合”名单。未知或新增效果仍按此明确集合和具体调用者条件处理，不承诺通用递归终止。

## 2. 持物改类型的完整默认映射

只在主稿所述有效持物与目的类型存在时使用。否则一般。

| 族／效果身份 | 物品身份 | 类型身份 |
| --- | --- | --- |
| `TypeDependsOnUserPlate` | FISTPLATE | FIGHTING |
| `TypeDependsOnUserPlate` | SKYPLATE | FLYING |
| `TypeDependsOnUserPlate` | TOXICPLATE | POISON |
| `TypeDependsOnUserPlate` | EARTHPLATE | GROUND |
| `TypeDependsOnUserPlate` | STONEPLATE | ROCK |
| `TypeDependsOnUserPlate` | INSECTPLATE | BUG |
| `TypeDependsOnUserPlate` | SPOOKYPLATE | GHOST |
| `TypeDependsOnUserPlate` | IRONPLATE | STEEL |
| `TypeDependsOnUserPlate` | FLAMEPLATE | FIRE |
| `TypeDependsOnUserPlate` | SPLASHPLATE | WATER |
| `TypeDependsOnUserPlate` | MEADOWPLATE | GRASS |
| `TypeDependsOnUserPlate` | ZAPPLATE | ELECTRIC |
| `TypeDependsOnUserPlate` | MINDPLATE | PSYCHIC |
| `TypeDependsOnUserPlate` | ICICLEPLATE | ICE |
| `TypeDependsOnUserPlate` | DRACOPLATE | DRAGON |
| `TypeDependsOnUserPlate` | DREADPLATE | DARK |
| `TypeDependsOnUserPlate` | PIXIEPLATE | FAIRY |
| `TypeDependsOnUserMemory` | FIGHTINGMEMORY | FIGHTING |
| `TypeDependsOnUserMemory` | FLYINGMEMORY | FLYING |
| `TypeDependsOnUserMemory` | POISONMEMORY | POISON |
| `TypeDependsOnUserMemory` | GROUNDMEMORY | GROUND |
| `TypeDependsOnUserMemory` | ROCKMEMORY | ROCK |
| `TypeDependsOnUserMemory` | BUGMEMORY | BUG |
| `TypeDependsOnUserMemory` | GHOSTMEMORY | GHOST |
| `TypeDependsOnUserMemory` | STEELMEMORY | STEEL |
| `TypeDependsOnUserMemory` | FIREMEMORY | FIRE |
| `TypeDependsOnUserMemory` | WATERMEMORY | WATER |
| `TypeDependsOnUserMemory` | GRASSMEMORY | GRASS |
| `TypeDependsOnUserMemory` | ELECTRICMEMORY | ELECTRIC |
| `TypeDependsOnUserMemory` | PSYCHICMEMORY | PSYCHIC |
| `TypeDependsOnUserMemory` | ICEMEMORY | ICE |
| `TypeDependsOnUserMemory` | DRAGONMEMORY | DRAGON |
| `TypeDependsOnUserMemory` | DARKMEMORY | DARK |
| `TypeDependsOnUserMemory` | FAIRYMEMORY | FAIRY |
| `TypeDependsOnUserDrive` | SHOCKDRIVE | ELECTRIC |
| `TypeDependsOnUserDrive` | BURNDRIVE | FIRE |
| `TypeDependsOnUserDrive` | CHILLDRIVE | ICE |
| `TypeDependsOnUserDrive` | DOUSEDRIVE | WATER |

## 3. 自然之恩默认内容数据

当前PBS/items.txt所有完整NaturalGift标志按数据原顺序逐项读取。实际资格仍要求当前有效树果；此表不给其它道具效果。类型／基底读取的时点、前缀检查与消费路径见主稿§3.1。作者可修改Flags，缺失或畸形值按该节处理，不能用表名自动补值。

| 物品身份 | 类型身份 | 标志给定威力 | PBS章节起行 |
| --- | --- | ---: | ---: |
| CHERIBERRY | FIRE | 80 | 5192 |
| CHESTOBERRY | WATER | 80 | 5202 |
| PECHABERRY | ELECTRIC | 80 | 5212 |
| RAWSTBERRY | GRASS | 80 | 5222 |
| ASPEARBERRY | ICE | 80 | 5232 |
| LEPPABERRY | FIGHTING | 80 | 5242 |
| ORANBERRY | POISON | 80 | 5252 |
| PERSIMBERRY | GROUND | 80 | 5262 |
| LUMBERRY | FLYING | 80 | 5271 |
| SITRUSBERRY | PSYCHIC | 80 | 5281 |
| FIGYBERRY | BUG | 80 | 5291 |
| WIKIBERRY | ROCK | 80 | 5299 |
| MAGOBERRY | GHOST | 80 | 5307 |
| AGUAVBERRY | DRAGON | 80 | 5315 |
| IAPAPABERRY | DARK | 80 | 5323 |
| RAZZBERRY | STEEL | 80 | 5331 |
| BLUKBERRY | FIRE | 90 | 5339 |
| NANABBERRY | WATER | 90 | 5347 |
| WEPEARBERRY | ELECTRIC | 90 | 5355 |
| PINAPBERRY | GRASS | 90 | 5363 |
| POMEGBERRY | ICE | 90 | 5371 |
| KELPSYBERRY | FIGHTING | 90 | 5380 |
| QUALOTBERRY | POISON | 90 | 5389 |
| HONDEWBERRY | GROUND | 90 | 5398 |
| GREPABERRY | FLYING | 90 | 5407 |
| TAMATOBERRY | PSYCHIC | 90 | 5416 |
| CORNNBERRY | BUG | 90 | 5425 |
| MAGOSTBERRY | ROCK | 90 | 5433 |
| RABUTABERRY | GHOST | 90 | 5441 |
| NOMELBERRY | DRAGON | 90 | 5449 |
| SPELONBERRY | DARK | 90 | 5457 |
| PAMTREBERRY | STEEL | 90 | 5465 |
| WATMELBERRY | FIRE | 100 | 5473 |
| DURINBERRY | WATER | 100 | 5481 |
| BELUEBERRY | ELECTRIC | 100 | 5489 |
| OCCABERRY | FIRE | 80 | 5497 |
| PASSHOBERRY | WATER | 80 | 5505 |
| WACANBERRY | ELECTRIC | 80 | 5513 |
| RINDOBERRY | GRASS | 80 | 5521 |
| YACHEBERRY | ICE | 80 | 5529 |
| CHOPLEBERRY | FIGHTING | 80 | 5537 |
| KEBIABERRY | POISON | 80 | 5545 |
| SHUCABERRY | GROUND | 80 | 5553 |
| COBABERRY | FLYING | 80 | 5561 |
| PAYAPABERRY | PSYCHIC | 80 | 5569 |
| TANGABERRY | BUG | 80 | 5577 |
| CHARTIBERRY | ROCK | 80 | 5585 |
| KASIBBERRY | GHOST | 80 | 5593 |
| HABANBERRY | DRAGON | 80 | 5601 |
| COLBURBERRY | DARK | 80 | 5609 |
| BABIRIBERRY | STEEL | 80 | 5617 |
| ROSELIBERRY | FAIRY | 80 | 5625 |
| CHILANBERRY | NORMAL | 80 | 5633 |
| LIECHIBERRY | GRASS | 100 | 5641 |
| GANLONBERRY | ICE | 100 | 5649 |
| SALACBERRY | FIGHTING | 100 | 5657 |
| PETAYABERRY | POISON | 100 | 5665 |
| APICOTBERRY | GROUND | 100 | 5673 |
| LANSATBERRY | FLYING | 100 | 5681 |
| STARFBERRY | PSYCHIC | 100 | 5689 |
| ENIGMABERRY | BUG | 100 | 5697 |
| MICLEBERRY | ROCK | 100 | 5705 |
| CUSTAPBERRY | GHOST | 100 | 5713 |
| JABOCABERRY | DRAGON | 100 | 5721 |
| ROWAPBERRY | DARK | 100 | 5729 |
| KEEBERRY | FAIRY | 100 | 5737 |
| MARANGABERRY | DARK | 100 | 5745 |

共67条默认标志数据；本族威力至少10的夹限仍适用。表是数据，不是源程序的翻译。

## 4. 本包效果身份与主合同

共55项，均有主稿具体行为；源文件相对`Data/Scripts/011_Battle/003_Move/`。

| 效果身份 | 文件与起行 | 主合同 |
| --- | --- | --- |
| `DoesNothingCongratulations` | `005_MoveEffects_Misc.rb`:10 | WP47-A §4 |
| `DoesNothingFailsIfNoAlly` | `005_MoveEffects_Misc.rb`:23 | WP47-A §4 |
| `DoesNothingUnusableInGravity` | `005_MoveEffects_Misc.rb`:38 | WP47-A §4 |
| `SetUserTypesBasedOnEnvironment` | `007_MoveEffects_BattlerOther.rb`:659 | WP47-A §2 |
| `SetUserTypesToResistLastAttack` | `007_MoveEffects_BattlerOther.rb`:721 | WP47-A §2 |
| `SetUserTypesToTargetTypes` | `007_MoveEffects_BattlerOther.rb`:762 | WP47-A §2 |
| `SetUserTypesToUserMoveType` | `007_MoveEffects_BattlerOther.rb`:799 | WP47-A §2 |
| `SetTargetTypesToPsychic` | `007_MoveEffects_BattlerOther.rb`:833 | WP47-A §2 |
| `SetTargetTypesToWater` | `007_MoveEffects_BattlerOther.rb`:855 | WP47-A §2 |
| `AddGhostTypeToTarget` | `007_MoveEffects_BattlerOther.rb`:877 | WP47-A §2 |
| `AddGrassTypeToTarget` | `007_MoveEffects_BattlerOther.rb`:898 | WP47-A §2 |
| `UserLosesFireType` | `007_MoveEffects_BattlerOther.rb`:919 | WP47-A §2 |
| `EnsureNextCriticalHit` | `008_MoveEffects_MoveAttributes.rb`:642 | WP47-A §4 |
| `UserEnduresFaintingThisTurn` | `008_MoveEffects_MoveAttributes.rb`:682 | WP47-A §4 |
| `ProtectUser` | `008_MoveEffects_MoveAttributes.rb`:852 | WP47-A §4 |
| `ProtectUserBanefulBunker` | `008_MoveEffects_MoveAttributes.rb`:864 | WP47-A §4 |
| `ProtectUserFromDamagingMovesKingsShield` | `008_MoveEffects_MoveAttributes.rb`:875 | WP47-A §4 |
| `ProtectUserFromDamagingMovesObstruct` | `008_MoveEffects_MoveAttributes.rb`:888 | WP47-A §4 |
| `ProtectUserFromTargetingMovesSpikyShield` | `008_MoveEffects_MoveAttributes.rb`:899 | WP47-A §4 |
| `RemoveProtections` | `008_MoveEffects_MoveAttributes.rb`:977 | WP47-A §4 |
| `RemoveProtectionsBypassSubstitute` | `008_MoveEffects_MoveAttributes.rb`:994 | WP47-A §4 |
| `HoopaRemoveProtectionsBypassSubstituteLowerUserDef1` | `008_MoveEffects_MoveAttributes.rb`:1002 | WP47-A §4 |
| `EnsureNextMoveAlwaysHits` | `008_MoveEffects_MoveAttributes.rb`:1222 | WP47-A §4 |
| `StartNegateTargetEvasionStatStageAndGhostImmunity` | `008_MoveEffects_MoveAttributes.rb`:1234 | WP47-A §4 |
| `StartNegateTargetEvasionStatStageAndDarkImmunity` | `008_MoveEffects_MoveAttributes.rb`:1248 | WP47-A §4 |
| `IgnoreTargetDefSpDefEvaStatStages` | `008_MoveEffects_MoveAttributes.rb`:1262 | WP47-A §4 |
| `TypeIsUserFirstType` | `008_MoveEffects_MoveAttributes.rb`:1277 | WP47-A §3 |
| `TypeDependsOnUserIVs` | `008_MoveEffects_MoveAttributes.rb`:1287 | WP47-A §3 |
| `TypeAndPowerDependOnUserBerry` | `008_MoveEffects_MoveAttributes.rb`:1338 | WP47-A §3 |
| `TypeDependsOnUserPlate` | `008_MoveEffects_MoveAttributes.rb`:1385 | WP47-A §3 |
| `TypeDependsOnUserMemory` | `008_MoveEffects_MoveAttributes.rb`:1422 | WP47-A §3 |
| `TypeDependsOnUserDrive` | `008_MoveEffects_MoveAttributes.rb`:1459 | WP47-A §3 |
| `TypeDependsOnUserMorpekoFormRaiseUserSpeed1` | `008_MoveEffects_MoveAttributes.rb`:1495 | WP47-A §3 |
| `TypeAndPowerDependOnWeather` | `008_MoveEffects_MoveAttributes.rb`:1513 | WP47-A §3 |
| `TypeAndPowerDependOnTerrain` | `008_MoveEffects_MoveAttributes.rb`:1550 | WP47-A §3 |
| `TargetMovesBecomeElectric` | `008_MoveEffects_MoveAttributes.rb`:1584 | WP47-A §3 |
| `RedirectAllMovesToUser` | `012_MoveEffects_ChangeMoveEffect.rb`:5 | WP47-A §5 |
| `RedirectAllMovesToTarget` | `012_MoveEffects_ChangeMoveEffect.rb`:21 | WP47-A §5 |
| `CannotBeRedirected` | `012_MoveEffects_ChangeMoveEffect.rb`:37 | WP47-A §5 |
| `EffectDependsOnEnvironment` | `012_MoveEffects_ChangeMoveEffect.rb`:224 | WP47-A §3 |
| `HitsAllFoesAndPowersUpInPsychicTerrain` | `012_MoveEffects_ChangeMoveEffect.rb`:340 | WP47-A §3 |
| `TargetNextFireMoveDamagesTarget` | `012_MoveEffects_ChangeMoveEffect.rb`:360 | WP47-A §4 |
| `PowerUpAllyMove` | `012_MoveEffects_ChangeMoveEffect.rb`:431 | WP47-A §4 |
| `UseLastMoveUsed` | `012_MoveEffects_ChangeMoveEffect.rb`:694 | WP47-A §6 |
| `UseLastMoveUsedByTarget` | `012_MoveEffects_ChangeMoveEffect.rb`:787 | WP47-A §6 |
| `UseMoveTargetIsAboutToUse` | `012_MoveEffects_ChangeMoveEffect.rb`:814 | WP47-A §6 |
| `UseMoveDependingOnEnvironment` | `012_MoveEffects_ChangeMoveEffect.rb`:861 | WP47-A §3 |
| `UseRandomMove` | `012_MoveEffects_ChangeMoveEffect.rb`:923 | WP47-A §6 |
| `UseRandomMoveFromUserParty` | `012_MoveEffects_ChangeMoveEffect.rb`:1019 | WP47-A §6 |
| `UseRandomUserMoveIfAsleep` | `012_MoveEffects_ChangeMoveEffect.rb`:1136 | WP47-A §6 |
| `BounceBackProblemCausingStatusMoves` | `012_MoveEffects_ChangeMoveEffect.rb`:1207 | WP47-A §5 |
| `StealAndUseBeneficialStatusMove` | `012_MoveEffects_ChangeMoveEffect.rb`:1217 | WP47-A §5 |
| `ReplaceMoveThisBattleWithTargetLastMoveUsed` | `012_MoveEffects_ChangeMoveEffect.rb`:1232 | WP47-A §6 |
| `ReplaceMoveWithTargetLastMoveUsed` | `012_MoveEffects_ChangeMoveEffect.rb`:1285 | WP47-A §6 |
| `HigherPriorityInGrassyTerrain` | `013_MoveEffects_SwitchingActing.rb`:673 | WP47-A §3 |

## 5. 已有／域外责任

| 效果身份 | 文件与起行 | 唯一已有主合同 |
| --- | --- | --- |
| `StartPreventCriticalHitsAgainstUserSide` | `008_MoveEffects_MoveAttributes.rb`:654 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `StartWeakenElectricMoves` | `008_MoveEffects_MoveAttributes.rb`:696 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `StartWeakenFireMoves` | `008_MoveEffects_MoveAttributes.rb`:723 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `StartWeakenPhysicalDamageAgainstUserSide` | `008_MoveEffects_MoveAttributes.rb`:751 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `StartWeakenSpecialDamageAgainstUserSide` | `008_MoveEffects_MoveAttributes.rb`:772 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `StartWeakenDamageAgainstUserSideIfHail` | `008_MoveEffects_MoveAttributes.rb`:794 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `RemoveScreens` | `008_MoveEffects_MoveAttributes.rb`:821 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `ProtectUserSideFromDamagingMovesIfUserFirstTurn` | `008_MoveEffects_MoveAttributes.rb`:909 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `ProtectUserSideFromStatusMoves` | `008_MoveEffects_MoveAttributes.rb`:930 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `ProtectUserSideFromPriorityMoves` | `008_MoveEffects_MoveAttributes.rb`:950 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `ProtectUserSideFromMultiTargetDamagingMoves` | `008_MoveEffects_MoveAttributes.rb`:964 | WP45 §3～8；场域、侧保护及生命周期已有合同 |
| `NormalMovesBecomeElectric` | `008_MoveEffects_MoveAttributes.rb`:1604 | WP45 §3～8；场域、侧保护及生命周期已有合同 |

WP46附表的139项伤害／恢复身份不再次算本包主合同；两文件中交错／誓约／蓄力／反击等已由WP46逐项给参数，相关本次目标与类型查询仅交叉引用。BattlerOther内已审状态31项与阶级114项仍WP44；类型变更9项在本包，能力／浮空／变身的招式操作归WP47-B，完整持久形态／Shadow仍WP22／23。SwitchingActing仅青草优先级本包主合同，号令／提前延后／轮唱等由WP47-B；物品目录归WP47-B，完整被动物品处理器WP50。没有将全局未归属审查WP79提前判完成。

本轮批准：[独立首审报告](../../review/wp46-wp47-review-2026-09-27/report.md)§2／4；A～E／55项属性目标调用主合同与默认数据限定通过。本次状态回填、C01维护和必要身份级联分开记账；被审首稿`1c164a68ed2d35c1dceaa9314038a9fe0f6a011c845a9adf512f740a466a898c`（18,920字节）留史，当前新字节不冒充原被审版本。运行、完整形态／物品／AI组合及阶段出口保留。
