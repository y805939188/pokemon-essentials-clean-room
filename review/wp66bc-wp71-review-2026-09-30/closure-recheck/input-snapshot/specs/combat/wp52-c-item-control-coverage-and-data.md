# WP52-C 覆盖、物品评级与条件数据 v1

状态：**Reviewed（限定静态范围，2026-09-28独立首审PASS_SCOPED；管理性回填）**。随[主稿](wp52-c-items-calling-and-control-evaluation.md)A～F的167出现／165有效直接键、215基础评级与57条件身份数据。本表记录审计身份和完整默认值，不输出参考处理器或未来类层级。正文给输入、门、值与阶段，索引不替代合同。通过仅限该静态范围，不使WP52-B或整个AI通过。

## 1. 当前有界账本

原A的add/copy定位C190条，B按数值/恢复责任接走23条，C现167出现／166不同出现键／165有效直接键。本轮还读出ItemRanking.addIf两个条件组，39类型增幅物＋18宝石；57身份不与当前直接物品评级键重叠。以旧口径说的784语句/786出现/783不同键均为add/copy文本定位，不包含这两条件组，不能称全AI物品评级只有那些直接键。

完整扫描：12文件786条登记语句＝784 add/copy＋2 addIf；直接/复制展开786出现，783不同出现键，最终782有效直接键；另57条件式物品身份，完整839有效可定位键。直接键优先、否则条件组按登记顺序首匹配，未来直接登记可遮住条件，不是条件组叠加。能力评级默认沿A，物品基础数据如下。

三组重复键与额外缺源：B连续切割整体评分被后add覆盖；B解除保护目标copy源不存在，旧+7保留；C撤退射击目标copy找不到仅登记在整体族的伤害自换源，旧降阶评分保留。另写生整体copy也找不到仅在目标族的模仿源，写生该键根本未创建，因此有效直接782而非783。数据索引和最终可调用行为分列，不能把这四处静默修成理想语义。

## 2. C逐登记及最终绑定

文件相对`Data/Scripts/011_Battle/`。空绑定表示copy失败且目的不存在；不是自动回退到另一个评分族。

| 文件:行 | 族／身份 | 登记方式 | 主合同 | 最终绑定 |
| --- | --- | --- | --- | --- |
| 005_AI/008_AI_Utilities.rb:387 | ItemRanking / `ADAMANTORB` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:387 |
| 005_AI/008_AI_Utilities.rb:395 | ItemRanking / `AGUAVBERRY` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:395 |
| 005_AI/008_AI_Utilities.rb:411 | ItemRanking / `ASSAULTVEST` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:411 |
| 005_AI/008_AI_Utilities.rb:420 | ItemRanking / `BERRYJUICE` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:420 |
| 005_AI/008_AI_Utilities.rb:426 | ItemRanking / `BIGROOT` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:426 |
| 005_AI/008_AI_Utilities.rb:439 | ItemRanking / `BINDINGBAND` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:439 |
| 005_AI/008_AI_Utilities.rb:446 | ItemRanking / `GRIPCLAW` | copy←BINDINGBAND | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:439 |
| 005_AI/008_AI_Utilities.rb:448 | ItemRanking / `BLACKSLUDGE` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:448 |
| 005_AI/008_AI_Utilities.rb:455 | ItemRanking / `CHESTOBERRY` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:455 |
| 005_AI/008_AI_Utilities.rb:464 | ItemRanking / `CHOICEBAND` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:464 |
| 005_AI/008_AI_Utilities.rb:471 | ItemRanking / `MUSCLEBAND` | copy←CHOICEBAND | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:464 |
| 005_AI/008_AI_Utilities.rb:473 | ItemRanking / `CHOICESPECS` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:473 |
| 005_AI/008_AI_Utilities.rb:480 | ItemRanking / `WISEGLASSES` | copy←CHOICESPECS | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:473 |
| 005_AI/008_AI_Utilities.rb:482 | ItemRanking / `DEEPSEASCALE` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:482 |
| 005_AI/008_AI_Utilities.rb:489 | ItemRanking / `DAMPROCK` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:489 |
| 005_AI/008_AI_Utilities.rb:496 | ItemRanking / `DEEPSEATOOTH` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:496 |
| 005_AI/008_AI_Utilities.rb:504 | ItemRanking / `ELECTRICSEED` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:504 |
| 005_AI/008_AI_Utilities.rb:511 | ItemRanking / `EVIOLITE` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:511 |
| 005_AI/008_AI_Utilities.rb:518 | ItemRanking / `FIGYBERRY` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:518 |
| 005_AI/008_AI_Utilities.rb:534 | ItemRanking / `FLAMEORB` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:534 |
| 005_AI/008_AI_Utilities.rb:542 | ItemRanking / `FULLINCENSE` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:542 |
| 005_AI/008_AI_Utilities.rb:551 | ItemRanking / `LAGGINGTAIL` | copy←FULLINCENSE | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:542 |
| 005_AI/008_AI_Utilities.rb:553 | ItemRanking / `GRASSYSEED` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:553 |
| 005_AI/008_AI_Utilities.rb:560 | ItemRanking / `GRISEOUSORB` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:560 |
| 005_AI/008_AI_Utilities.rb:568 | ItemRanking / `HEATROCK` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:568 |
| 005_AI/008_AI_Utilities.rb:575 | ItemRanking / `IAPAPABERRY` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:575 |
| 005_AI/008_AI_Utilities.rb:591 | ItemRanking / `ICYROCK` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:591 |
| 005_AI/008_AI_Utilities.rb:598 | ItemRanking / `IRONBALL` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:598 |
| 005_AI/008_AI_Utilities.rb:605 | ItemRanking / `KINGSROCK` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:605 |
| 005_AI/008_AI_Utilities.rb:614 | ItemRanking / `RAZORFANG` | copy←KINGSROCK | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:605 |
| 005_AI/008_AI_Utilities.rb:616 | ItemRanking / `LEEK` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:616 |
| 005_AI/008_AI_Utilities.rb:624 | ItemRanking / `STICK` | copy←LEEK | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:616 |
| 005_AI/008_AI_Utilities.rb:626 | ItemRanking / `LIGHTBALL` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:626 |
| 005_AI/008_AI_Utilities.rb:634 | ItemRanking / `LIGHTCLAY` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:634 |
| 005_AI/008_AI_Utilities.rb:645 | ItemRanking / `LUCKYPUNCH` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:645 |
| 005_AI/008_AI_Utilities.rb:652 | ItemRanking / `LUSTROUSORB` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:652 |
| 005_AI/008_AI_Utilities.rb:660 | ItemRanking / `MAGOBERRY` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:660 |
| 005_AI/008_AI_Utilities.rb:676 | ItemRanking / `METALPOWDER` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:676 |
| 005_AI/008_AI_Utilities.rb:683 | ItemRanking / `QUICKPOWDER` | copy←METALPOWDER | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:676 |
| 005_AI/008_AI_Utilities.rb:685 | ItemRanking / `MISTYSEED` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:685 |
| 005_AI/008_AI_Utilities.rb:692 | ItemRanking / `ORANBERRY` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:692 |
| 005_AI/008_AI_Utilities.rb:698 | ItemRanking / `POWERHERB` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:698 |
| 005_AI/008_AI_Utilities.rb:708 | ItemRanking / `PSYCHICSEED` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:708 |
| 005_AI/008_AI_Utilities.rb:715 | ItemRanking / `RINGTARGET` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:715 |
| 005_AI/008_AI_Utilities.rb:727 | ItemRanking / `SMOOTHROCK` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:727 |
| 005_AI/008_AI_Utilities.rb:734 | ItemRanking / `SOULDEW` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:734 |
| 005_AI/008_AI_Utilities.rb:748 | ItemRanking / `TERRAINEXTENDER` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:748 |
| 005_AI/008_AI_Utilities.rb:760 | ItemRanking / `THICKCLUB` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:760 |
| 005_AI/008_AI_Utilities.rb:768 | ItemRanking / `THROATSPRAY` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:768 |
| 005_AI/008_AI_Utilities.rb:775 | ItemRanking / `TOXICORB` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:775 |
| 005_AI/008_AI_Utilities.rb:783 | ItemRanking / `WHITEHERB` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:783 |
| 005_AI/008_AI_Utilities.rb:792 | ItemRanking / `WIKIBERRY` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:792 |
| 005_AI/008_AI_Utilities.rb:808 | ItemRanking / `ZOOMLENS` | add | 主稿§2.1 | 005_AI/008_AI_Utilities.rb:808 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:82 | MoveFailureAgainstTargetCheck / `FailsIfTargetHasNoItem` | add | 主稿§3 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:82 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:102 | MoveEffectAgainstTargetScore / `FailsIfUserDamagedThisTurn` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:102 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:139 | MoveEffectAgainstTargetScore / `FailsIfTargetActed` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:139 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:466 | MoveFailureCheck / `SwapSideEffects` | add | 主稿§6 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:466 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:487 | MoveEffectScore / `SwapSideEffects` | add | 主稿§6 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:487 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:537 | MoveEffectScore / `RemoveUserBindingAndEntryHazards` | add | 主稿§6 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:537 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:576 | MoveFailureCheck / `UserSwapsPositionsWithAlly` | add | 主稿§6 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:576 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:588 | MoveEffectScore / `UserSwapsPositionsWithAlly` | add | 主稿§6 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:588 |
| 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:597 | MoveEffectScore / `BurnAttackerBeforeUserActs` | add | 主稿§5.2 | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb:597 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1115 | MoveFailureCheck / `StartUserAirborne` | add | 主稿§6 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1115 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1124 | MoveEffectScore / `StartUserAirborne` | add | 主稿§6 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1124 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1151 | MoveFailureAgainstTargetCheck / `StartTargetAirborneAndAlwaysHitByMoves` | add | 主稿§6 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1151 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1157 | MoveEffectAgainstTargetScore / `StartTargetAirborneAndAlwaysHitByMoves` | add | 主稿§6 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1157 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1195 | MoveEffectAgainstTargetScore / `HitsTargetInSkyGroundsTarget` | add | 主稿§6 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1195 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1220 | MoveFailureCheck / `StartGravity` | add | 主稿§6 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1220 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1225 | MoveEffectScore / `StartGravity` | add | 主稿§6 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1225 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1270 | MoveFailureAgainstTargetCheck / `TransformUserIntoTarget` | add | 主稿§6 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1270 |
| 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1278 | MoveEffectAgainstTargetScore / `TransformUserIntoTarget` | add | 主稿§6 | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb:1278 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:4 | MoveEffectAgainstTargetScore / `UserTakesTargetItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:4 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:29 | MoveFailureAgainstTargetCheck / `TargetTakesUserItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:29 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:36 | MoveEffectAgainstTargetScore / `TargetTakesUserItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:36 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:55 | MoveFailureAgainstTargetCheck / `UserTargetSwapItems` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:55 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:65 | MoveEffectAgainstTargetScore / `UserTargetSwapItems` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:65 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:88 | MoveFailureCheck / `RestoreUserConsumedItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:88 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:93 | MoveEffectScore / `RestoreUserConsumedItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:93 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:106 | MoveBasePower / `RemoveTargetItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:106 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:111 | MoveEffectAgainstTargetScore / `RemoveTargetItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:111 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:129 | MoveEffectAgainstTargetScore / `DestroyTargetBerryOrGem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:129 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:148 | MoveFailureAgainstTargetCheck / `CorrodeTargetItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:148 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:157 | MoveEffectAgainstTargetScore / `CorrodeTargetItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:157 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:171 | MoveFailureAgainstTargetCheck / `StartTargetCannotUseItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:171 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:176 | MoveEffectAgainstTargetScore / `StartTargetCannotUseItem` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:176 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:191 | MoveEffectScore / `StartNegateHeldItems` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:191 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:232 | MoveFailureCheck / `UserConsumeBerryRaiseDefense2` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:232 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:238 | MoveEffectScore / `UserConsumeBerryRaiseDefense2` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:238 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:268 | MoveFailureAgainstTargetCheck / `AllBattlersConsumeBerry` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:268 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:273 | MoveEffectAgainstTargetScore / `AllBattlersConsumeBerry` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:273 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:300 | MoveEffectAgainstTargetScore / `UserConsumeTargetBerry` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:300 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:329 | MoveFailureCheck / `ThrowUserItemAtTarget` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:329 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:338 | MoveBasePower / `ThrowUserItemAtTarget` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:338 |
| 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:343 | MoveEffectAgainstTargetScore / `ThrowUserItemAtTarget` | add | 主稿§3 | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb:343 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:4 | MoveEffectScore / `RedirectAllMovesToUser` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:4 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:21 | MoveEffectAgainstTargetScore / `RedirectAllMovesToTarget` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:21 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:80 | MoveFailureCheck / `CurseTargetOrLowerUserSpd1RaiseUserAtkDef1` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:80 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:98 | MoveFailureAgainstTargetCheck / `CurseTargetOrLowerUserSpd1RaiseUserAtkDef1` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:98 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:106 | MoveEffectScore / `CurseTargetOrLowerUserSpd1RaiseUserAtkDef1` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:106 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:115 | MoveEffectAgainstTargetScore / `CurseTargetOrLowerUserSpd1RaiseUserAtkDef1` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:115 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:144 | MoveEffectAgainstTargetScore / `EffectDependsOnEnvironment` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:144 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:196 | MoveFailureAgainstTargetCheck / `TargetNextFireMoveDamagesTarget` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:196 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:201 | MoveEffectAgainstTargetScore / `TargetNextFireMoveDamagesTarget` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:201 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:240 | MoveFailureAgainstTargetCheck / `PowerUpAllyMove` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:240 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:245 | MoveEffectAgainstTargetScore / `PowerUpAllyMove` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:245 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:460 | MoveFailureCheck / `UseLastMoveUsed` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:460 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:473 | MoveFailureAgainstTargetCheck / `UseLastMoveUsedByTarget` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:473 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:484 | MoveFailureAgainstTargetCheck / `UseMoveTargetIsAboutToUse` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:484 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:489 | MoveEffectAgainstTargetScore / `UseMoveTargetIsAboutToUse` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:489 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:514 | MoveFailureCheck / `UseRandomMoveFromUserParty` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:514 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:535 | MoveFailureCheck / `UseRandomUserMoveIfAsleep` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:535 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:551 | MoveEffectScore / `BounceBackProblemCausingStatusMoves` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:551 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:573 | MoveEffectScore / `StealAndUseBeneficialStatusMove` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:573 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:594 | MoveFailureCheck / `ReplaceMoveThisBattleWithTargetLastMoveUsed` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:594 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:599 | MoveFailureAgainstTargetCheck / `ReplaceMoveThisBattleWithTargetLastMoveUsed` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:599 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:610 | MoveEffectAgainstTargetScore / `ReplaceMoveThisBattleWithTargetLastMoveUsed` | add | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:610 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:625 | MoveFailureAgainstTargetCheck / `ReplaceMoveWithTargetLastMoveUsed` | copy←ReplaceMoveThisBattleWithTargetLastMoveUsed | 主稿§4 | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:599 |
| 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb:627 | MoveEffectScore / `ReplaceMoveWithTargetLastMoveUsed` | copy←ReplaceMoveThisBattleWithTargetLastMoveUsed；复制源在本族不存在 | 主稿§4 | 无专用处理器，使用共用默认 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:4 | MoveFailureCheck / `FleeFromBattle` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:4 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:9 | MoveEffectScore / `FleeFromBattle` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:9 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:19 | MoveFailureCheck / `SwitchOutUserStatusMove` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:19 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:27 | MoveEffectScore / `SwitchOutUserStatusMove` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:27 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:62 | MoveEffectScore / `SwitchOutUserDamagingMove` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:62 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:93 | MoveFailureAgainstTargetCheck / `LowerTargetAtkSpAtk1SwitchOutUser` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:93 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:104 | MoveEffectAgainstTargetScore / `LowerTargetAtkSpAtk1SwitchOutUser` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:104 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:109 | MoveEffectAgainstTargetScore / `LowerTargetAtkSpAtk1SwitchOutUser` | copy←SwitchOutUserDamagingMove；复制源在本族不存在 | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:104 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:115 | MoveFailureCheck / `SwitchOutUserPassOnEffects` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:115 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:120 | MoveEffectScore / `SwitchOutUserPassOnEffects` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:120 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:164 | MoveFailureAgainstTargetCheck / `SwitchOutTargetStatusMove` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:164 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:169 | MoveEffectAgainstTargetScore / `SwitchOutTargetStatusMove` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:169 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:200 | MoveEffectAgainstTargetScore / `SwitchOutTargetDamagingMove` | add | 主稿§5.1 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:200 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:238 | MoveEffectAgainstTargetScore / `BindTarget` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:238 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:277 | MoveBasePower / `BindTargetDoublePowerIfTargetUnderwater` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:277 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:282 | MoveEffectAgainstTargetScore / `BindTargetDoublePowerIfTargetUnderwater` | copy←BindTarget | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:238 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:288 | MoveFailureAgainstTargetCheck / `TrapTargetInBattle` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:288 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:296 | MoveEffectAgainstTargetScore / `TrapTargetInBattle` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:296 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:329 | MoveFailureAgainstTargetCheck / `TrapTargetInBattleMainEffect` | copy←TrapTargetInBattle | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:288 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:331 | MoveEffectAgainstTargetScore / `TrapTargetInBattleMainEffect` | copy←TrapTargetInBattle | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:296 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:337 | MoveFailureAgainstTargetCheck / `TrapTargetInBattleLowerTargetDefSpDef1EachTurn` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:337 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:345 | MoveEffectAgainstTargetScore / `TrapTargetInBattleLowerTargetDefSpDef1EachTurn` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:345 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:375 | MoveEffectAgainstTargetScore / `TrapUserAndTargetInBattle` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:375 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:406 | MoveFailureCheck / `TrapAllBattlersInBattleForOneTurn` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:406 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:411 | MoveEffectScore / `TrapAllBattlersInBattleForOneTurn` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:411 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:426 | MoveFailureCheck / `UsedAfterUserTakesPhysicalDamage` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:426 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:437 | MoveEffectScore / `UsedAfterUserTakesPhysicalDamage` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:437 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:456 | MoveEffectScore / `UsedAfterAllyRoundWithDoublePower` | add | 主稿§5.2 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:456 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:475 | MoveEffectAgainstTargetScore / `TargetActsNext` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:475 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:505 | MoveEffectAgainstTargetScore / `TargetActsLast` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:505 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:540 | MoveFailureAgainstTargetCheck / `TargetUsesItsLastUsedMoveAgain` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:540 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:545 | MoveEffectAgainstTargetScore / `TargetUsesItsLastUsedMoveAgain` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:545 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:574 | MoveEffectScore / `StartSlowerBattlersActFirst` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:574 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:618 | MoveEffectAgainstTargetScore / `LowerPPOfTargetLastMoveBy3` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:618 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:638 | MoveFailureAgainstTargetCheck / `LowerPPOfTargetLastMoveBy4` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:638 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:643 | MoveEffectAgainstTargetScore / `LowerPPOfTargetLastMoveBy4` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:643 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:658 | MoveFailureAgainstTargetCheck / `DisableTargetLastMoveUsed` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:658 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:665 | MoveEffectAgainstTargetScore / `DisableTargetLastMoveUsed` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:665 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:685 | MoveFailureAgainstTargetCheck / `DisableTargetUsingSameMoveConsecutively` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:685 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:692 | MoveEffectAgainstTargetScore / `DisableTargetUsingSameMoveConsecutively` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:692 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:710 | MoveFailureAgainstTargetCheck / `DisableTargetUsingDifferentMove` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:710 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:722 | MoveEffectAgainstTargetScore / `DisableTargetUsingDifferentMove` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:722 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:762 | MoveFailureAgainstTargetCheck / `DisableTargetStatusMoves` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:762 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:771 | MoveEffectAgainstTargetScore / `DisableTargetStatusMoves` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:771 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:815 | MoveFailureAgainstTargetCheck / `DisableTargetHealingMoves` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:815 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:822 | MoveEffectAgainstTargetScore / `DisableTargetHealingMoves` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:822 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:840 | MoveEffectAgainstTargetScore / `DisableTargetSoundMoves` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:840 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:857 | MoveFailureCheck / `DisableTargetMovesKnownByUser` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:857 |
| 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:862 | MoveEffectAgainstTargetScore / `DisableTargetMovesKnownByUser` | add | 主稿§5.3 | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb:862 |

## 3. 完整基础物品评级

Utilities:163–228；未列0，空物NONE0。中等修正、投掷与杂技后置按主稿§2，不能把这些默认值当真实物品伤害/恢复值。

| 默认值 | 完整身份（源顺序） |
| ---: | --- |
| 10 | EVIOLITE, FOCUSSASH, LIFEORB, THICKCLUB |
| 9 | ASSAULTVEST, BLACKSLUDGE, CHOICEBAND, CHOICESCARF, CHOICESPECS, DEEPSEATOOTH, LEFTOVERS |
| 8 | LEEK, STICK, THROATSPRAY, WEAKNESSPOLICY |
| 7 | EXPERTBELT, LIGHTBALL, LUMBERRY, POWERHERB, ROCKYHELMET, SITRUSBERRY |
| 6 | KINGSROCK, LIECHIBERRY, LIGHTCLAY, PETAYABERRY, RAZORFANG, REDCARD, SALACBERRY, SHELLBELL, WHITEHERB, BABIRIBERRY, CHARTIBERRY, CHILANBERRY, CHOPLEBERRY, COBABERRY, COLBURBERRY, HABANBERRY, KASIBBERRY, KEBIABERRY, OCCABERRY, PASSHOBERRY, PAYAPABERRY, RINDOBERRY, ROSELIBERRY, SHUCABERRY, TANGABERRY, WACANBERRY, YACHEBERRY, BUGGEM, DARKGEM, DRAGONGEM, ELECTRICGEM, FAIRYGEM, FIGHTINGGEM, FIREGEM, FLYINGGEM, GHOSTGEM, GRASSGEM, GROUNDGEM, ICEGEM, NORMALGEM, POISONGEM, PSYCHICGEM, ROCKGEM, STEELGEM, WATERGEM, ADAMANTORB, GRISEOUSORB, LUSTROUSORB, SOULDEW, AGUAVBERRY, FIGYBERRY, IAPAPABERRY, MAGOBERRY, WIKIBERRY |
| 5 | CUSTAPBERRY, DEEPSEASCALE, EJECTBUTTON, FOCUSBAND, JABOCABERRY, KEEBERRY, LANSATBERRY, MARANGABERRY, MENTALHERB, METRONOME, MUSCLEBAND, QUICKCLAW, RAZORCLAW, ROWAPBERRY, SCOPELENS, WISEGLASSES, BLACKBELT, BLACKGLASSES, CHARCOAL, DRAGONFANG, HARDSTONE, MAGNET, METALCOAT, MIRACLESEED, MYSTICWATER, NEVERMELTICE, POISONBARB, SHARPBEAK, SILKSCARF, SILVERPOWDER, SOFTSAND, SPELLTAG, TWISTEDSPOON, ODDINCENSE, ROCKINCENSE, ROSEINCENSE, SEAINCENSE, WAVEINCENSE, DRACOPLATE, DREADPLATE, EARTHPLATE, FISTPLATE, FLAMEPLATE, ICICLEPLATE, INSECTPLATE, IRONPLATE, MEADOWPLATE, MINDPLATE, PIXIEPLATE, SKYPLATE, SPLASHPLATE, SPOOKYPLATE, STONEPLATE, TOXICPLATE, ZAPPLATE, DAMPROCK, HEATROCK, ICYROCK, SMOOTHROCK, TERRAINEXTENDER |
| 4 | ADRENALINEORB, APICOTBERRY, BLUNDERPOLICY, CHESTOBERRY, EJECTPACK, ENIGMABERRY, GANLONBERRY, HEAVYDUTYBOOTS, ROOMSERVICE, SAFETYGOGGLES, SHEDSHELL, STARFBERRY |
| 3 | BIGROOT, BRIGHTPOWDER, LAXINCENSE, LEPPABERRY, PERSIMBERRY, PROTECTIVEPADS, UTILITYUMBRELLA, ASPEARBERRY, CHERIBERRY, PECHABERRY, RAWSTBERRY |
| 2 | ABSORBBULB, BERRYJUICE, CELLBATTERY, GRIPCLAW, LUMINOUSMOSS, MICLEBERRY, ORANBERRY, SNOWBALL, WIDELENS, ZOOMLENS, ELECTRICSEED, GRASSYSEED, MISTYSEED, PSYCHICSEED |
| 1 | AIRBALLOON, BINDINGBAND, DESTINYKNOT, FLOATSTONE, LUCKYPUNCH, METALPOWDER, QUICKPOWDER, BURNDRIVE, CHILLDRIVE, DOUSEDRIVE, SHOCKDRIVE, BUGMEMORY, DARKMEMORY, DRAGONMEMORY, ELECTRICMEMORY, FAIRYMEMORY, FIGHTINGMEMORY, FIREMEMORY, FLYINGMEMORY, GHOSTMEMORY, GRASSMEMORY, GROUNDMEMORY, ICEMEMORY, POISONMEMORY, PSYCHICMEMORY, ROCKMEMORY, STEELMEMORY, WATERMEMORY |
| 0 | SMOKEBALL |
| -5 | FULLINCENSE, LAGGINGTAIL, RINGTARGET |
| -6 | MACHOBRACE, POWERANKLET, POWERBAND, POWERBELT, POWERBRACER, POWERLENS, POWERWEIGHT |
| -7 | FLAMEORB, IRONBALL, TOXICORB |
| -9 | STICKYBARB |

共215个默认身份、15档，无重复。

## 4. 两条件组精确映射

类型增幅组中等需对应可用伤害招才保留基础5，否则0；宝石组≤5先＋2，再同类型门，通常8或6／无招0。匹配条件本身只检查物品身份，不执行处理器。

| 条件组 | 物品 | 对应类型 |
| --- | --- | --- |
| type_boosting_items | SILVERPOWDER | BUG |
| type_boosting_items | INSECTPLATE | BUG |
| type_boosting_items | BLACKGLASSES | DARK |
| type_boosting_items | DREADPLATE | DARK |
| type_boosting_items | DRAGONFANG | DRAGON |
| type_boosting_items | DRACOPLATE | DRAGON |
| type_boosting_items | MAGNET | ELECTRIC |
| type_boosting_items | ZAPPLATE | ELECTRIC |
| type_boosting_items | PIXIEPLATE | FAIRY |
| type_boosting_items | BLACKBELT | FIGHTING |
| type_boosting_items | FISTPLATE | FIGHTING |
| type_boosting_items | CHARCOAL | FIRE |
| type_boosting_items | FLAMEPLATE | FIRE |
| type_boosting_items | SHARPBEAK | FLYING |
| type_boosting_items | SKYPLATE | FLYING |
| type_boosting_items | SPELLTAG | GHOST |
| type_boosting_items | SPOOKYPLATE | GHOST |
| type_boosting_items | MIRACLESEED | GRASS |
| type_boosting_items | MEADOWPLATE | GRASS |
| type_boosting_items | ROSEINCENSE | GRASS |
| type_boosting_items | SOFTSAND | GROUND |
| type_boosting_items | EARTHPLATE | GROUND |
| type_boosting_items | NEVERMELTICE | ICE |
| type_boosting_items | ICICLEPLATE | ICE |
| type_boosting_items | SILKSCARF | NORMAL |
| type_boosting_items | POISONBARB | POISON |
| type_boosting_items | TOXICPLATE | POISON |
| type_boosting_items | TWISTEDSPOON | PSYCHIC |
| type_boosting_items | MINDPLATE | PSYCHIC |
| type_boosting_items | ODDINCENSE | PSYCHIC |
| type_boosting_items | HARDSTONE | ROCK |
| type_boosting_items | STONEPLATE | ROCK |
| type_boosting_items | ROCKINCENSE | ROCK |
| type_boosting_items | METALCOAT | STEEL |
| type_boosting_items | IRONPLATE | STEEL |
| type_boosting_items | MYSTICWATER | WATER |
| type_boosting_items | SPLASHPLATE | WATER |
| type_boosting_items | SEAINCENSE | WATER |
| type_boosting_items | WAVEINCENSE | WATER |
| gems | BUGGEM | BUG |
| gems | DARKGEM | DARK |
| gems | DRAGONGEM | DRAGON |
| gems | ELECTRICGEM | ELECTRIC |
| gems | FAIRYGEM | FAIRY |
| gems | FIGHTINGGEM | FIGHTING |
| gems | FIREGEM | FIRE |
| gems | FLYINGGEM | FLYING |
| gems | GHOSTGEM | GHOST |
| gems | GRASSGEM | GRASS |
| gems | GROUNDGEM | GROUND |
| gems | ICEGEM | ICE |
| gems | NORMALGEM | NORMAL |
| gems | POISONGEM | POISON |
| gems | PSYCHICGEM | PSYCHIC |
| gems | ROCKGEM | ROCK |
| gems | STEELGEM | STEEL |
| gems | WATERGEM | WATER |

## 5. 固定辅助集合与已审数据

| 数据 | 完整身份／责任 |
| --- | --- |
| 投掷附加价值+1 | FLAMEORB, KINGSROCK, LIGHTBALL, POISONBARB, RAZORFANG, TOXICORB |
| 侧交换预测好组 | AuroraVeil, LightScreen, Mist, Rainbow, Reflect, Safeguard, SeaOfFire, Swamp, Tailwind |
| 侧交换预测坏组 | Spikes, StealthRock, StickyWeb, ToxicSpikes |
| 挑衅保护加分组 | ProtectUser, ProtectUserSideFromPriorityMoves, ProtectUserSideFromMultiTargetDamagingMoves, UserEnduresFaintingThisTurn, ProtectUserSideFromDamagingMovesIfUserFirstTurn, ProtectUserSideFromStatusMoves, ProtectUserFromDamagingMovesKingsShield, ProtectUserFromDamagingMovesObstruct, ProtectUserFromTargetingMovesSpikyShield, ProtectUserBanefulBunker |

[WP47-A完整调用排除表](wp47-a-attributes-targeting-calling-data.md)§1给仿效/抢先/挥指/借助/梦话/模仿/写生并集63效果与代际行；[WP47-B完整号令/安可及投掷数据](wp47-b-control-items-coverage-data.md)给32及6＋6排除和578项投掷威力。本文不创建第二份不一致的黑名单。实际资格与AI分数分开；WP54或设施后续不会自动让当前运行/动态等价通过。

本轮记录：2026-09-28 [独立首审报告](../../review/wp52b-wp52c-wp54-review-2026-09-28/report.md)§5；A～F具名静态范围（167出现／166不同出现键／165有效直接键、215基础评级、39＋18条件身份及三重复键/缺源差异）独立首审PASS_SCOPED后限定Reviewed管理回填。被审首稿v1 `9e8d3030b462c2bef28cf0793aea5b6802e87c6db1d7c80b04fb63f0fc766261`（37,701字节）保留历史，当前新字节不冒充被审对象；不使WP52-B或整个AI通过。
