# WP52-C 有界登记、物品评级与条件数据附表（净化正文；批次 12）

分类：combat-requirements／pokemon-rules 数据附表；性质：实现独立行为数据。

本附表为净化正文的一部分：按统一交接将批准输入 WP52-C《覆盖、物品评级与条件数据》转写为独立行为数据，不含源文件路径与行号（源定位集中登记于 `../../audit/source-traceability.md` 批次 12 条目）。本表仅审计定位与默认值，具体条件/数值/分支以主稿合同为准，不以登记索引替代行为。全部内容为静态证据；**无运行确认**（见 `../scope-statement.md`）。

## 1. 当前有界账本

原 A 的 add/copy 定位将 C 记为 190 条；B 按数值/恢复责任接走 23 条后，C 现 **167 出现／166 不同出现键／165 有效直接键**。本批还读出 ItemRanking 两个条件登记组：39 类型增幅物＋18 宝石，共 57 个条件式物品身份，与当前直接物品评级键不重叠。旧口径的 784 语句／786 出现／783 不同键均为 add/copy 文本定位，**不包含**这两条件组，不能称全 AI 物品评级只有那些直接键。

完整扫描口径：12 个登记源共 786 条登记语句＝784 add/copy＋2 条件登记；直接/复制展开 786 出现、783 不同出现键，最终 782 有效直接键；另 57 条件式物品身份，完整 **839 有效可定位键**。解析顺序：直接键优先；无直接键时条件组按登记顺序取首匹配；未来新增直接登记可遮住条件组，**不是**条件组叠加。能力评级默认沿 A 口径，物品基础数据见 §3。

三组重复键与一处额外缺源（分散在 A/B/C，此处汇总收口）：

1. B 连续切割整体评分被同族后登记覆盖（先登记值不执行）；
2. B 解除保护目标分的 copy 源不存在，先登记的旧值保留；
3. C 撤退射击（LowerTargetAtkSpAtk1SwitchOutUser）目标分的 copy 源仅登记在整体分族，copy 不生效，先登记的降阶评分保留；
4. 另整体分族的 ReplaceMoveWithTargetLastMoveUsed 其 copy 源仅在目标分族存在，copy 不生效且**该键根本未创建**——有效直接键因此为 782 而非 783。

数据索引与最终可调用行为必须分列；不能把这四处静默修成理想语义。

## 2. C 逐登记及最终绑定

空绑定表示 copy 失败且目的不存在，**不是**自动回退到另一个评分族。「←X」表示 copy 且最终绑定到 X 的登记（源文件与行号见追溯条目）。被覆盖/缺源的原段不是同时执行。

### 2.1 ItemRanking（53 出现；主稿 §2.1）

直接登记（46）：ADAMANTORB, AGUAVBERRY, ASSAULTVEST, BERRYJUICE, BIGROOT, BINDINGBAND, BLACKSLUDGE, CHESTOBERRY, CHOICEBAND, CHOICESPECS, DEEPSEASCALE, DAMPROCK, DEEPSEATOOTH, ELECTRICSEED, EVIOLITE, FIGYBERRY, FLAMEORB, FULLINCENSE, GRASSYSEED, GRISEOUSORB, HEATROCK, IAPAPABERRY, ICYROCK, IRONBALL, KINGSROCK, LEEK, LIGHTBALL, LIGHTCLAY, LUCKYPUNCH, LUSTROUSORB, MAGOBERRY, METALPOWDER, MISTYSEED, ORANBERRY, POWERHERB, PSYCHICSEED, RINGTARGET, SMOOTHROCK, SOULDEW, TERRAINEXTENDER, THICKCLUB, THROATSPRAY, TOXICORB, WHITEHERB, WIKIBERRY, ZOOMLENS。

复制登记（7，均绑定成功）：GRIPCLAW←BINDINGBAND；MUSCLEBAND←CHOICEBAND；WISEGLASSES←CHOICESPECS；LAGGINGTAIL←FULLINCENSE；RAZORFANG←KINGSROCK；STICK←LEEK；QUICKPOWDER←METALPOWDER。

### 2.2 Misc 效果组（9 出现；主稿 §3/§5.2/§6）

MoveFailureAgainstTargetCheck：FailsIfTargetHasNoItem（§3）。

MoveEffectAgainstTargetScore：FailsIfUserDamagedThisTurn（§5.2）；FailsIfTargetActed（§5.2）。

MoveFailureCheck：SwapSideEffects（§6）；UserSwapsPositionsWithAlly（§6）。

MoveEffectScore：SwapSideEffects（§6）；RemoveUserBindingAndEntryHazards（§6）；UserSwapsPositionsWithAlly（§6）；BurnAttackerBeforeUserActs（§5.2）。

### 2.3 BattlerOther 效果组（9 出现；主稿 §6）

MoveFailureCheck：StartUserAirborne；StartGravity。

MoveEffectScore：StartUserAirborne；StartGravity。

MoveFailureAgainstTargetCheck：StartTargetAirborneAndAlwaysHitByMoves；TransformUserIntoTarget。

MoveEffectAgainstTargetScore：StartTargetAirborneAndAlwaysHitByMoves；HitsTargetInSkyGroundsTarget；TransformUserIntoTarget。

### 2.4 Items 效果组（23 出现；主稿 §3）

MoveFailureAgainstTargetCheck：TargetTakesUserItem；UserTargetSwapItems；CorrodeTargetItem；StartTargetCannotUseItem；AllBattlersConsumeBerry。

MoveEffectAgainstTargetScore：UserTakesTargetItem；TargetTakesUserItem；UserTargetSwapItems；RemoveTargetItem；DestroyTargetBerryOrGem；CorrodeTargetItem；StartTargetCannotUseItem；AllBattlersConsumeBerry；UserConsumeTargetBerry；ThrowUserItemAtTarget。

MoveFailureCheck：RestoreUserConsumedItem；UserConsumeBerryRaiseDefense2；ThrowUserItemAtTarget。

MoveEffectScore：RestoreUserConsumedItem；StartNegateHeldItems；UserConsumeBerryRaiseDefense2。

MoveBasePower：RemoveTargetItem；ThrowUserItemAtTarget。

### 2.5 ChangeMoveEffect 效果组（24 出现；主稿 §4）

MoveEffectScore：RedirectAllMovesToUser；CurseTargetOrLowerUserSpd1RaiseUserAtkDef1；PowerUpAllyMove；BounceBackProblemCausingStatusMoves；StealAndUseBeneficialStatusMove。

MoveEffectAgainstTargetScore：RedirectAllMovesToTarget；CurseTargetOrLowerUserSpd1RaiseUserAtkDef1；EffectDependsOnEnvironment；TargetNextFireMoveDamagesTarget；PowerUpAllyMove；UseMoveTargetIsAboutToUse；ReplaceMoveThisBattleWithTargetLastMoveUsed。

MoveFailureCheck：CurseTargetOrLowerUserSpd1RaiseUserAtkDef1；UseLastMoveUsed；UseRandomMoveFromUserParty；UseRandomUserMoveIfAsleep；ReplaceMoveThisBattleWithTargetLastMoveUsed。

MoveFailureAgainstTargetCheck：CurseTargetOrLowerUserSpd1RaiseUserAtkDef1；TargetNextFireMoveDamagesTarget；PowerUpAllyMove；UseLastMoveUsedByTarget；UseMoveTargetIsAboutToUse；ReplaceMoveThisBattleWithTargetLastMoveUsed；ReplaceMoveWithTargetLastMoveUsed←ReplaceMoveThisBattleWithTargetLastMoveUsed（绑定成功）。

复制缺源（1）：MoveEffectScore / ReplaceMoveWithTargetLastMoveUsed←ReplaceMoveThisBattleWithTargetLastMoveUsed——源仅在目标分族存在，copy 不生效且该键不创建；此族无专用处理器，查询落共用默认（§1 第 4 条）。

### 2.6 SwitchingActing 效果组（49 出现；主稿 §5.1/§5.2/§5.3）

MoveFailureCheck：FleeFromBattle（§5.1）；SwitchOutUserStatusMove（§5.1）；SwitchOutUserPassOnEffects（§5.1）；TrapAllBattlersInBattleForOneTurn（§5.2）；UsedAfterUserTakesPhysicalDamage（§5.2）；DisableTargetMovesKnownByUser（§5.3）。

MoveEffectScore：FleeFromBattle（§5.1）；SwitchOutUserStatusMove（§5.1）；SwitchOutUserDamagingMove（§5.1）；SwitchOutUserPassOnEffects（§5.1）；TrapAllBattlersInBattleForOneTurn（§5.2）；UsedAfterUserTakesPhysicalDamage（§5.2）；UsedAfterAllyRoundWithDoublePower（§5.2）；StartSlowerBattlersActFirst（§5.3）；DisableTargetMovesKnownByUser（§5.3）。

MoveFailureAgainstTargetCheck：LowerTargetAtkSpAtk1SwitchOutUser（§5.1）；SwitchOutTargetStatusMove（§5.1）；TrapTargetInBattle（§5.2）；TrapTargetInBattleMainEffect←TrapTargetInBattle（§5.2）；TrapTargetInBattleLowerTargetDefSpDef1EachTurn（§5.2）；TargetUsesItsLastUsedMoveAgain（§5.3）；LowerPPOfTargetLastMoveBy4（§5.3）；DisableTargetLastMoveUsed（§5.3）；DisableTargetUsingSameMoveConsecutively（§5.3）；DisableTargetUsingDifferentMove（§5.3）；DisableTargetStatusMoves（§5.3）；DisableTargetHealingMoves（§5.3）。

MoveEffectAgainstTargetScore：LowerTargetAtkSpAtk1SwitchOutUser（§5.1，先登记降阶评分）；LowerTargetAtkSpAtk1SwitchOutUser←SwitchOutUserDamagingMove（copy 源仅登记在整体分族，不生效，先登记值保留——§1 第 3 条）；SwitchOutTargetStatusMove（§5.1）；SwitchOutTargetDamagingMove（§5.1）；BindTarget（§5.2）；BindTargetDoublePowerIfTargetUnderwater←BindTarget（§5.2）；TrapTargetInBattle（§5.2）；TrapTargetInBattleMainEffect←TrapTargetInBattle（§5.2）；TrapTargetInBattleLowerTargetDefSpDef1EachTurn（§5.2）；TrapUserAndTargetInBattle（§5.2）；TargetActsNext（§5.3）；TargetActsLast（§5.3）；TargetUsesItsLastUsedMoveAgain（§5.3）；LowerPPOfTargetLastMoveBy3（§5.3）；LowerPPOfTargetLastMoveBy4（§5.3）；DisableTargetLastMoveUsed（§5.3）；DisableTargetUsingSameMoveConsecutively（§5.3）；DisableTargetUsingDifferentMove（§5.3）；DisableTargetStatusMoves（§5.3）；DisableTargetHealingMoves（§5.3）；DisableTargetSoundMoves（§5.3）。

MoveBasePower：BindTargetDoublePowerIfTargetUnderwater（§5.2）。

合计 53＋9＋9＋23＋24＋49＝167 出现；唯一重复出现键为 LowerTargetAtkSpAtk1SwitchOutUser 的目标分（先 add 后 copy 失败），不同出现键 166；ReplaceMoveWithTargetLastMoveUsed 整体分未创建，有效直接键 165。

## 3. 完整基础物品评级

下表为公用工具段登记的完整默认评级（源顺序）；未列身份为 0，空物 NONE 为 0。中等修正、投掷与杂技后置按主稿 §2；不能把这些默认值当真实物品伤害/恢复值。

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

共 215 个默认身份、15 档，无重复。

## 4. 两条件组精确映射

类型增幅组：中等技能下需持有者另有对应该类型的可用伤害招才保留基础 5，否则 0。宝石组：基础值 ≤5 先 ＋2，再过同类型有招门，通常得 8 或 6，无对应招为 0。匹配条件本身只检查物品身份，不执行处理器。两组共 57 个条件身份（39＋18），与 §2.1 直接键不重叠。

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

## 5. 固定辅助集合与已审数据交叉引用

| 数据 | 完整身份／责任 |
| --- | --- |
| 投掷附加价值＋1 | FLAMEORB, KINGSROCK, LIGHTBALL, POISONBARB, RAZORFANG, TOXICORB |
| 侧交换预测好组（9） | AuroraVeil, LightScreen, Mist, Rainbow, Reflect, Safeguard, SeaOfFire, Swamp, Tailwind |
| 侧交换预测坏组（4） | Spikes, StealthRock, StickyWeb, ToxicSpikes |
| 挑衅保护加分组（10） | ProtectUser, ProtectUserSideFromPriorityMoves, ProtectUserSideFromMultiTargetDamagingMoves, UserEnduresFaintingThisTurn, ProtectUserSideFromDamagingMovesIfUserFirstTurn, ProtectUserSideFromStatusMoves, ProtectUserFromDamagingMovesKingsShield, ProtectUserFromDamagingMovesObstruct, ProtectUserFromTargetingMovesSpikyShield, ProtectUserBanefulBunker |

[WP47-A 完整调用排除表](wp47-a-attributes-targeting-calling-data.md) §1 给仿效/抢先/挥指/借助/梦话/模仿/写生并集 63 效果与代际行；[WP47-B 完整号令/安可及投掷数据](wp47-b-control-items-coverage-data.md) 给 32 及 6＋6 排除和 578 项投掷威力。本文不创建第二份不一致的黑名单。实际资格与 AI 分数分开；WP54 或设施后续不会自动让当前运行/动态等价通过。

## 6. 保留责任

A 为共同评分/数值/状态阶级，WP51 为选择/技能/资源，B 为场域/伤害/恢复/目标处理器；本附表收口 C 的物品评级、调用/替换与行动控制的登记数据。完整设施仍各既定包；真实写入和数值依 WP43–50。低档不启 MoveBasePower、ScoreMoves 关不启效果分，以及 copy 失败后的默认行为不能用完整目录名代替。全局运行/插件组合与 WP79 未关闭范围不在本附表承诺内。
