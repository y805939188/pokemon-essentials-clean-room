# WP47-A 覆盖与默认数据附表（净化正文；批次 11）

分类：combat-requirements／pokemon-rules 数据附表；性质：实现独立行为数据。

本附表为净化正文的一部分：按统一交接将批准输入 WP47-A《覆盖与默认数据附表》转写为独立行为数据，不含源文件路径与行号（源定位集中登记于 `../../audit/source-traceability.md` 批次 11 条目）。表中效果身份/物品身份是审计及行为数据，不是未来类/API 设计。全部内容为静态证据；**无运行确认**（见 `../scope-statement.md`）。

## 1. 完整调用排除表

「常」表示所有世代明列排除，「≥6」表示仅世代 ≥6 追加，「—」表示该明列名单未排除（仍可能被其它资格/标记拒绝）。各列对应主稿 §6 七个调用/复制入口；按效果字符串匹配，不是按招式显示名或父级族匹配。仿效/抢先/挥指/借助/梦话/模仿/写生各自集合如下，不将注释掉的行当有效数据。

| 效果身份 | 仿效 | 抢先 | 挥指 | 借助 | 梦话 | 模仿 | 写生 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AllBattlersLoseHalfHPUserSkipsNextTurn | — | — | — | ≥6 | 常 | — | — |
| AttackerFaintsIfUserFaints | 常 | — | 常 | 常 | — | — | — |
| BounceBackProblemCausingStatusMoves | 常 | — | 常 | 常 | — | — | — |
| BurnAttackerBeforeUserActs | 常 | 常 | 常 | 常 | 常 | — | — |
| CounterDamagePlusHalf | 常 | 常 | 常 | 常 | — | — | — |
| CounterPhysicalDamage | 常 | 常 | 常 | 常 | — | — | — |
| CounterSpecialDamage | 常 | 常 | 常 | 常 | — | — | — |
| DoesNothingCongratulations | 常 | — | 常 | 常 | — | — | — |
| DoesNothingFailsIfNoAlly | 常 | — | 常 | 常 | — | — | — |
| FailsIfUserDamagedThisTurn | 常 | 常 | 常 | 常 | 常 | — | — |
| FailsIfUserNotConsumedBerry | 常 | 常 | 常 | 常 | 常 | — | — |
| FlinchTargetFailsIfUserNotAsleep | — | — | 常 | — | — | — | — |
| MultiTurnAttackBideThenReturnDoubleDamage | — | — | — | — | 常 | — | — |
| MultiTurnAttackPreventSleeping | — | — | — | — | 常 | — | — |
| PowerUpAllyMove | 常 | — | 常 | 常 | — | — | — |
| ProtectUser | 常 | — | 常 | 常 | — | — | — |
| ProtectUserBanefulBunker | 常 | — | 常 | 常 | — | — | — |
| ProtectUserFromDamagingMovesKingsShield | 常 | — | 常 | 常 | — | — | — |
| ProtectUserFromDamagingMovesObstruct | 常 | — | 常 | 常 | — | — | — |
| ProtectUserFromTargetingMovesSpikyShield | 常 | — | 常 | 常 | — | — | — |
| ProtectUserSideFromDamagingMovesIfUserFirstTurn | 常 | — | 常 | 常 | — | — | — |
| ProtectUserSideFromMultiTargetDamagingMoves | 常 | — | 常 | 常 | — | — | — |
| ProtectUserSideFromPriorityMoves | 常 | — | 常 | 常 | — | — | — |
| ProtectUserSideFromStatusMoves | 常 | — | 常 | 常 | — | — | — |
| RedirectAllMovesToTarget | 常 | — | 常 | 常 | — | — | — |
| RedirectAllMovesToUser | 常 | — | 常 | 常 | — | — | — |
| ReduceAttackerMovePPTo0IfUserFaints | 常 | — | 常 | 常 | — | — | — |
| RemoveProtections | 常 | — | 常 | 常 | — | — | — |
| ReplaceMoveThisBattleWithTargetLastMoveUsed | 常 | — | 常 | 常 | 常 | 常 | — |
| ReplaceMoveWithTargetLastMoveUsed | 常 | — | 常 | 常 | 常 | 常 | 常 |
| StealAndUseBeneficialStatusMove | 常 | — | 常 | 常 | — | — | — |
| Struggle | 常 | 常 | 常 | 常 | 常 | 常 | 常 |
| SwitchOutTargetDamagingMove | ≥6 | — | — | 常 | — | — | — |
| SwitchOutTargetStatusMove | ≥6 | — | — | ≥6 | — | — | — |
| TargetActsLast | — | — | 常 | — | — | — | — |
| TargetActsNext | — | — | 常 | — | — | — | — |
| TargetTakesUserItem | 常 | — | 常 | 常 | — | — | — |
| TargetUsesItsLastUsedMoveAgain | — | — | 常 | — | — | — | — |
| TransformUserIntoTarget | 常 | — | 常 | 常 | — | 常 | — |
| TwoTurnAttack | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackBurnTarget | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackChargeRaiseUserDefense1 | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackFlinchTarget | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackInvulnerableInSky | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackInvulnerableInSkyParalyzeTarget | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackInvulnerableInSkyTargetCannotAct | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackInvulnerableRemoveProtections | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackInvulnerableUnderground | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackInvulnerableUnderwater | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackOneTurnInSun | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackParalyzeTarget | — | — | — | ≥6 | 常 | — | — |
| TwoTurnAttackRaiseUserSpAtkSpDefSpd2 | — | — | — | ≥6 | 常 | — | — |
| UseLastMoveUsed | 常 | — | 常 | 常 | 常 | — | — |
| UseLastMoveUsedByTarget | 常 | — | 常 | 常 | 常 | — | — |
| UseMoveDependingOnEnvironment | 常 | — | 常 | ≥6 | 常 | — | — |
| UseMoveTargetIsAboutToUse | 常 | — | 常 | 常 | 常 | — | — |
| UseRandomMove | 常 | — | 常 | 常 | 常 | 常 | — |
| UseRandomMoveFromUserParty | 常 | — | 常 | 常 | 常 | — | — |
| UseRandomUserMoveIfAsleep | 常 | — | 常 | 常 | 常 | — | — |
| UsedAfterUserTakesPhysicalDamage | 常 | 常 | 常 | 常 | 常 | — | — |
| UserEnduresFaintingThisTurn | 常 | — | 常 | 常 | — | — | — |
| UserTakesTargetItem | 常 | 常 | 常 | 常 | — | — | — |
| UserTargetSwapItems | 常 | — | 常 | 常 | — | — | — |

逐列数据量（常＋≥6 新增）：仿效 41＋2；抢先 9＋0；挥指 45＋0；借助 41＋16；梦话 30＋0；模仿 5＋0；写生 2＋0。不同入口候选集合和额外过滤见主稿 §6，标「—」不是无条件允许。

特别保留：ReduceAttackerMovePPTo0IfUserFaints 与实际 SetAttackerMovePPTo0IfUserFaints 不是同一字符串；未将 Meteor Beam 等未明列项补进「两回合」名单。未知或新增效果仍按此明确集合和具体调用者条件处理，不承诺通用递归终止。

## 2. 持物改类型的完整默认映射

只在主稿所述有效持物与目的类型存在时使用。否则一般。

| 族/效果身份 | 物品身份 | 类型身份 |
| --- | --- | --- |
| TypeDependsOnUserPlate | FISTPLATE | FIGHTING |
| TypeDependsOnUserPlate | SKYPLATE | FLYING |
| TypeDependsOnUserPlate | TOXICPLATE | POISON |
| TypeDependsOnUserPlate | EARTHPLATE | GROUND |
| TypeDependsOnUserPlate | STONEPLATE | ROCK |
| TypeDependsOnUserPlate | INSECTPLATE | BUG |
| TypeDependsOnUserPlate | SPOOKYPLATE | GHOST |
| TypeDependsOnUserPlate | IRONPLATE | STEEL |
| TypeDependsOnUserPlate | FLAMEPLATE | FIRE |
| TypeDependsOnUserPlate | SPLASHPLATE | WATER |
| TypeDependsOnUserPlate | MEADOWPLATE | GRASS |
| TypeDependsOnUserPlate | ZAPPLATE | ELECTRIC |
| TypeDependsOnUserPlate | MINDPLATE | PSYCHIC |
| TypeDependsOnUserPlate | ICICLEPLATE | ICE |
| TypeDependsOnUserPlate | DRACOPLATE | DRAGON |
| TypeDependsOnUserPlate | DREADPLATE | DARK |
| TypeDependsOnUserPlate | PIXIEPLATE | FAIRY |
| TypeDependsOnUserMemory | FIGHTINGMEMORY | FIGHTING |
| TypeDependsOnUserMemory | FLYINGMEMORY | FLYING |
| TypeDependsOnUserMemory | POISONMEMORY | POISON |
| TypeDependsOnUserMemory | GROUNDMEMORY | GROUND |
| TypeDependsOnUserMemory | ROCKMEMORY | ROCK |
| TypeDependsOnUserMemory | BUGMEMORY | BUG |
| TypeDependsOnUserMemory | GHOSTMEMORY | GHOST |
| TypeDependsOnUserMemory | STEELMEMORY | STEEL |
| TypeDependsOnUserMemory | FIREMEMORY | FIRE |
| TypeDependsOnUserMemory | WATERMEMORY | WATER |
| TypeDependsOnUserMemory | GRASSMEMORY | GRASS |
| TypeDependsOnUserMemory | ELECTRICMEMORY | ELECTRIC |
| TypeDependsOnUserMemory | PSYCHICMEMORY | PSYCHIC |
| TypeDependsOnUserMemory | ICEMEMORY | ICE |
| TypeDependsOnUserMemory | DRAGONMEMORY | DRAGON |
| TypeDependsOnUserMemory | DARKMEMORY | DARK |
| TypeDependsOnUserMemory | FAIRYMEMORY | FAIRY |
| TypeDependsOnUserDrive | SHOCKDRIVE | ELECTRIC |
| TypeDependsOnUserDrive | BURNDRIVE | FIRE |
| TypeDependsOnUserDrive | CHILLDRIVE | ICE |
| TypeDependsOnUserDrive | DOUSEDRIVE | WATER |

## 3. 自然之恩默认内容数据

当前物品数据所有完整 NaturalGift 标志按数据原顺序逐项读取。实际资格仍要求当前有效树果；此表不给其它道具效果。类型/基底读取的时点、前缀检查与消费路径见主稿 §3.1。作者可修改标志；缺失或畸形值按该节处理，不能用表名自动补值。

| 物品身份 | 类型身份 | 标志给定威力 |
| --- | --- | ---: |
| CHERIBERRY | FIRE | 80 |
| CHESTOBERRY | WATER | 80 |
| PECHABERRY | ELECTRIC | 80 |
| RAWSTBERRY | GRASS | 80 |
| ASPEARBERRY | ICE | 80 |
| LEPPABERRY | FIGHTING | 80 |
| ORANBERRY | POISON | 80 |
| PERSIMBERRY | GROUND | 80 |
| LUMBERRY | FLYING | 80 |
| SITRUSBERRY | PSYCHIC | 80 |
| FIGYBERRY | BUG | 80 |
| WIKIBERRY | ROCK | 80 |
| MAGOBERRY | GHOST | 80 |
| AGUAVBERRY | DRAGON | 80 |
| IAPAPABERRY | DARK | 80 |
| RAZZBERRY | STEEL | 80 |
| BLUKBERRY | FIRE | 90 |
| NANABBERRY | WATER | 90 |
| WEPEARBERRY | ELECTRIC | 90 |
| PINAPBERRY | GRASS | 90 |
| POMEGBERRY | ICE | 90 |
| KELPSYBERRY | FIGHTING | 90 |
| QUALOTBERRY | POISON | 90 |
| HONDEWBERRY | GROUND | 90 |
| GREPABERRY | FLYING | 90 |
| TAMATOBERRY | PSYCHIC | 90 |
| CORNNBERRY | BUG | 90 |
| MAGOSTBERRY | ROCK | 90 |
| RABUTABERRY | GHOST | 90 |
| NOMELBERRY | DRAGON | 90 |
| SPELONBERRY | DARK | 90 |
| PAMTREBERRY | STEEL | 90 |
| WATMELBERRY | FIRE | 100 |
| DURINBERRY | WATER | 100 |
| BELUEBERRY | ELECTRIC | 100 |
| OCCABERRY | FIRE | 80 |
| PASSHOBERRY | WATER | 80 |
| WACANBERRY | ELECTRIC | 80 |
| RINDOBERRY | GRASS | 80 |
| YACHEBERRY | ICE | 80 |
| CHOPLEBERRY | FIGHTING | 80 |
| KEBIABERRY | POISON | 80 |
| SHUCABERRY | GROUND | 80 |
| COBABERRY | FLYING | 80 |
| PAYAPABERRY | PSYCHIC | 80 |
| TANGABERRY | BUG | 80 |
| CHARTIBERRY | ROCK | 80 |
| KASIBBERRY | GHOST | 80 |
| HABANBERRY | DRAGON | 80 |
| COLBURBERRY | DARK | 80 |
| BABIRIBERRY | STEEL | 80 |
| ROSELIBERRY | FAIRY | 80 |
| CHILANBERRY | NORMAL | 80 |
| LIECHIBERRY | GRASS | 100 |
| GANLONBERRY | ICE | 100 |
| SALACBERRY | FIGHTING | 100 |
| PETAYABERRY | POISON | 100 |
| APICOTBERRY | GROUND | 100 |
| LANSATBERRY | FLYING | 100 |
| STARFBERRY | PSYCHIC | 100 |
| ENIGMABERRY | BUG | 100 |
| MICLEBERRY | ROCK | 100 |
| CUSTAPBERRY | GHOST | 100 |
| JABOCABERRY | DRAGON | 100 |
| ROWAPBERRY | DARK | 100 |
| KEEBERRY | FAIRY | 100 |
| MARANGABERRY | DARK | 100 |

共 67 条默认标志数据；本族威力至少 10 的夹限仍适用。表是数据，不是源程序的翻译。

## 4. 本包效果身份与主合同

共 55 项，均有主稿具体行为。身份 → 主合同位置（源文件与行号见追溯条目）：

DoesNothingCongratulations、DoesNothingFailsIfNoAlly、DoesNothingUnusableInGravity（主稿 §4）；SetUserTypesBasedOnEnvironment、SetUserTypesToResistLastAttack、SetUserTypesToTargetTypes、SetUserTypesToUserMoveType、SetTargetTypesToPsychic、SetTargetTypesToWater、AddGhostTypeToTarget、AddGrassTypeToTarget、UserLosesFireType（主稿 §2）；EnsureNextCriticalHit、UserEnduresFaintingThisTurn、ProtectUser、ProtectUserBanefulBunker、ProtectUserFromDamagingMovesKingsShield、ProtectUserFromDamagingMovesObstruct、ProtectUserFromTargetingMovesSpikyShield、RemoveProtections、RemoveProtectionsBypassSubstitute、HoopaRemoveProtectionsBypassSubstituteLowerUserDef1、EnsureNextMoveAlwaysHits、StartNegateTargetEvasionStatStageAndGhostImmunity、StartNegateTargetEvasionStatStageAndDarkImmunity、IgnoreTargetDefSpDefEvaStatStages（主稿 §4）；TypeIsUserFirstType、TypeDependsOnUserIVs、TypeAndPowerDependOnUserBerry、TypeDependsOnUserPlate、TypeDependsOnUserMemory、TypeDependsOnUserDrive、TypeDependsOnUserMorpekoFormRaiseUserSpeed1、TypeAndPowerDependOnWeather、TypeAndPowerDependOnTerrain、TargetMovesBecomeElectric（主稿 §3）；RedirectAllMovesToUser、RedirectAllMovesToTarget、CannotBeRedirected、EffectDependsOnEnvironment、HitsAllFoesAndPowersUpInPsychicTerrain、TargetNextFireMoveDamagesTarget、PowerUpAllyMove（主稿 §5/§3/§4）；UseLastMoveUsed、UseLastMoveUsedByTarget、UseMoveTargetIsAboutToUse、UseMoveDependingOnEnvironment、UseRandomMove、UseRandomMoveFromUserParty、UseRandomUserMoveIfAsleep（主稿 §6）；BounceBackProblemCausingStatusMoves、StealAndUseBeneficialStatusMove（主稿 §5）；ReplaceMoveThisBattleWithTargetLastMoveUsed、ReplaceMoveWithTargetLastMoveUsed（主稿 §6）；HigherPriorityInGrassyTerrain（主稿 §3）。

## 5. 已有/域外责任

StartPreventCriticalHitsAgainstUserSide、StartWeakenElectricMoves、StartWeakenFireMoves、StartWeakenPhysicalDamageAgainstUserSide、StartWeakenSpecialDamageAgainstUserSide、StartWeakenDamageAgainstUserSideIfHail、RemoveScreens、ProtectUserSideFromDamagingMovesIfUserFirstTurn、ProtectUserSideFromStatusMoves、ProtectUserSideFromPriorityMoves、ProtectUserSideFromMultiTargetDamagingMoves、NormalMovesBecomeElectric——WP45（场域、侧保护及生命周期）已有唯一主合同；本包只引用已审建立/期限，不重复另造新门。

WP46 附表的 139 项伤害/恢复身份不再次算本包主合同；两文件中交错/誓约/蓄力/反击等已由 WP46 逐项给参数，相关本次目标与类型查询仅交叉引用。BattlerOther 内已审状态 31 项与阶级 114 项仍 WP44；类型变更 9 项在本包，能力/浮空/变身的招式操作归 WP47-B，完整持久形态/Shadow 仍 WP22/23。SwitchingActing 仅青草优先级本包主合同，号令/提前延后/轮唱等由 WP47-B；物品目录归 WP47-B，完整被动物品处理器 WP50。没有将全局未归属审查 WP79 提前判完成。
