# WP47-B 有界覆盖与默认数据 v1

状态：Reviewed（限定静态范围，2026-09-27首审PASS_SCOPED；管理性回填）。仅规格／分析；标识与有序数据用于审计及行为判断，不是未来类／API。

## 1. 号令与安可完整排除表

按功能标识精确匹配。“常”为所有世代，“≥7”为当代追加，“—”不在本地名单，仍可能被其它资格拒绝。名单不等于所有递归／两回合家族的普遍守卫，主稿§3／4给实际候选与消费者。

| 效果身份 | 号令 | 安可 |
| --- | --- | --- |
| `AllBattlersLoseHalfHPUserSkipsNextTurn` | 常 | — |
| `AttackAndSkipNextTurn` | 常 | — |
| `BurnAttackerBeforeUserActs` | 常 | — |
| `DisableTargetUsingDifferentMove` | — | 常 |
| `FailsIfUserDamagedThisTurn` | 常 | — |
| `MultiTurnAttackBideThenReturnDoubleDamage` | 常 | — |
| `ProtectUserFromDamagingMovesKingsShield` | 常 | — |
| `ReplaceMoveThisBattleWithTargetLastMoveUsed` | 常 | 常 |
| `ReplaceMoveWithTargetLastMoveUsed` | 常 | 常 |
| `Struggle` | 常 | 常 |
| `TargetUsesItsLastUsedMoveAgain` | 常 | — |
| `TransformUserIntoTarget` | 常 | 常 |
| `TwoTurnAttack` | 常 | — |
| `TwoTurnAttackBurnTarget` | 常 | — |
| `TwoTurnAttackChargeRaiseUserDefense1` | 常 | — |
| `TwoTurnAttackFlinchTarget` | 常 | — |
| `TwoTurnAttackInvulnerableInSky` | 常 | — |
| `TwoTurnAttackInvulnerableInSkyParalyzeTarget` | 常 | — |
| `TwoTurnAttackInvulnerableInSkyTargetCannotAct` | 常 | — |
| `TwoTurnAttackInvulnerableRemoveProtections` | 常 | — |
| `TwoTurnAttackInvulnerableUnderground` | 常 | — |
| `TwoTurnAttackInvulnerableUnderwater` | 常 | — |
| `TwoTurnAttackOneTurnInSun` | 常 | — |
| `TwoTurnAttackParalyzeTarget` | 常 | — |
| `TwoTurnAttackRaiseUserSpAtkSpDefSpd2` | 常 | — |
| `UseLastMoveUsed` | 常 | ≥7 |
| `UseLastMoveUsedByTarget` | 常 | 常 |
| `UseMoveDependingOnEnvironment` | 常 | ≥7 |
| `UseMoveTargetIsAboutToUse` | 常 | ≥7 |
| `UseRandomMove` | 常 | ≥7 |
| `UseRandomMoveFromUserParty` | 常 | ≥7 |
| `UseRandomUserMoveIfAsleep` | 常 | ≥7 |
| `UsedAfterUserTakesPhysicalDamage` | 常 | — |

号令常排32；安可常排6、世代≥7追加6。选择记录／PP／当前多回合／准备标记的其它拒绝在主稿，不由名单自动替代。

## 2. 不可移物的默认物种组合

先后门见主稿§5.1：邮件先拒、变身例外、Mega石动态物种数据再本表。ARCEUS须原能力MULTITYPE、SILVALLY须RKSSYSTEM才使用对应行；不把普通能力压制或未来任意形态规则混入。

| 物种 | 默认绑定物品身份 |
| --- | --- |
| ARCEUS | FISTPLATE, FIGHTINIUMZ, SKYPLATE, FLYINIUMZ, TOXICPLATE, POISONIUMZ, EARTHPLATE, GROUNDIUMZ, STONEPLATE, ROCKIUMZ, INSECTPLATE, BUGINIUMZ, SPOOKYPLATE, GHOSTIUMZ, IRONPLATE, STEELIUMZ, FLAMEPLATE, FIRIUMZ, SPLASHPLATE, WATERIUMZ, MEADOWPLATE, GRASSIUMZ, ZAPPLATE, ELECTRIUMZ, MINDPLATE, PSYCHIUMZ, ICICLEPLATE, ICIUMZ, DRACOPLATE, DRAGONIUMZ, DREADPLATE, DARKINIUMZ, PIXIEPLATE, FAIRIUMZ |
| SILVALLY | FIGHTINGMEMORY, FLYINGMEMORY, POISONMEMORY, GROUNDMEMORY, ROCKMEMORY, BUGMEMORY, GHOSTMEMORY, STEELMEMORY, FIREMEMORY, WATERMEMORY, GRASSMEMORY, ELECTRICMEMORY, PSYCHICMEMORY, ICEMEMORY, DRAGONMEMORY, DARKMEMORY, FAIRYMEMORY |
| GIRATINA | GRISEOUSORB |
| GENESECT | BURNDRIVE, CHILLDRIVE, DOUSEDRIVE, SHOCKDRIVE |
| KYOGRE | BLUEORB |
| GROUDON | REDORB |
| ZACIAN | RUSTEDSWORD |
| ZAMAZENTA | RUSTEDSHIELD |

Mega石不另抄物种全集：具体已Mega所需石由当前物种记录mega_stone给；未Mega则扫描同物种且unmega_form等于当前形态的记录。相应数据定义与形态资格已有WP18／21，完整Mega域WP22仍前向。未知／缺失数据不自动中性。

## 3. 投掷完整默认威力数据

当前PBS/items.txt完整数字Fling标志578项，按威力分组、组内保留原数据顺序。查表只说明基底请求，不说明此刻一定可投；普通物品有效性、树果紧张感、不可失物、替身、鳞粉、消耗时点仍按主稿§5.3。作者可改Flags；有前缀但无完整数字标志时主稿给默认10。高值250等属于真实内容，不能为贴近常见攻略自行删去。

| 标志威力 | 物品身份（完整默认集合） |
| ---: | --- |
| 10 | REDNECTAR, YELLOWNECTAR, PINKNECTAR, PURPLENECTAR, AIRBALLOON, BRIGHTPOWDER, DESTINYKNOT, REDCARD, SHEDSHELL, SOOTHEBELL, CHOICEBAND, CHOICESPECS, CHOICESCARF, SMOOTHROCK, BIGROOT, LEFTOVERS, MENTALHERB, WHITEHERB, POWERHERB, ELECTRICSEED, GRASSYSEED, MISTYSEED, PSYCHICSEED, EXPERTBELT, MUSCLEBAND, WISEGLASSES, WIDELENS, ZOOMLENS, LAGGINGTAIL, FOCUSBAND, FOCUSSASH, RINGTARGET, LAXINCENSE, FULLINCENSE, LUCKINCENSE, PUREINCENSE, SEAINCENSE, WAVEINCENSE, ROSEINCENSE, ODDINCENSE, ROCKINCENSE, SOFTSAND, SILVERPOWDER, SILKSCARF, METALPOWDER, QUICKPOWDER, REAPERCLOTH, STRAWBERRYSWEET, LOVESWEET, BERRYSWEET, CLOVERSWEET, FLOWERSWEET, STARSWEET, RIBBONSWEET, LONELYMINT, ADAMANTMINT, NAUGHTYMINT, BRAVEMINT, BOLDMINT, IMPISHMINT, LAXMINT, RELAXEDMINT, MODESTMINT, MILDMINT, RASHMINT, QUIETMINT, CALMMINT, GENTLEMINT, CAREFULMINT, SASSYMINT, TIMIDMINT, HASTYMINT, JOLLYMINT, NAIVEMINT, SERIOUSMINT, TM04, TM05, TM06, TM07, TM08, TM10, TM11, TM12, TM16, TM17, TM18, TM20, TM32, TM33, TM37, TM41, TM44, TM45, TM48, TM51, TM56, TM58, TM61, TM63, TM67, TM69, TM70, TM73, TM74, TM75, TM76, TM77, TM82, TM86, TM87, TM90, TM92, TM97, CHERIBERRY, CHESTOBERRY, PECHABERRY, RAWSTBERRY, ASPEARBERRY, LEPPABERRY, ORANBERRY, PERSIMBERRY, LUMBERRY, SITRUSBERRY, FIGYBERRY, WIKIBERRY, MAGOBERRY, AGUAVBERRY, IAPAPABERRY, RAZZBERRY, BLUKBERRY, NANABBERRY, WEPEARBERRY, PINAPBERRY, POMEGBERRY, KELPSYBERRY, QUALOTBERRY, HONDEWBERRY, GREPABERRY, TAMATOBERRY, CORNNBERRY, MAGOSTBERRY, RABUTABERRY, NOMELBERRY, SPELONBERRY, PAMTREBERRY, WATMELBERRY, DURINBERRY, BELUEBERRY, OCCABERRY, PASSHOBERRY, WACANBERRY, RINDOBERRY, YACHEBERRY, CHOPLEBERRY, KEBIABERRY, SHUCABERRY, COBABERRY, PAYAPABERRY, TANGABERRY, CHARTIBERRY, KASIBBERRY, HABANBERRY, COLBURBERRY, BABIRIBERRY, ROSELIBERRY, CHILANBERRY, LIECHIBERRY, GANLONBERRY, SALACBERRY, PETAYABERRY, APICOTBERRY, LANSATBERRY, STARFBERRY, ENIGMABERRY, MICLEBERRY, CUSTAPBERRY, JABOCABERRY, ROWAPBERRY, KEEBERRY, MARANGABERRY |
| 20 | PRETTYFEATHER, HEALTHFEATHER, MUSCLEFEATHER, RESISTFEATHER, GENIUSFEATHER, CLEVERFEATHER, SWIFTFEATHER |
| 25 | TM09 |
| 30 | REPEL, SUPERREPEL, MAXREPEL, BLACKFLUTE, WHITEFLUTE, HONEY, REDSHARD, YELLOWSHARD, BLUESHARD, GREENSHARD, FIRESTONE, THUNDERSTONE, WATERSTONE, LEAFSTONE, MOONSTONE, SUNSTONE, ICESTONE, SWEETAPPLE, TARTAPPLE, GALARICACUFF, GALARICAWREATH, TINYMUSHROOM, BIGMUSHROOM, BALMMUSHROOM, PEARL, BIGPEARL, PEARLSTRING, STARDUST, STARPIECE, COMETSHARD, NUGGET, HEARTSCALE, RELICCOPPER, RELICSILVER, RELICGOLD, RELICVASE, RELICBAND, RELICSTATUE, RELICCROWN, GROWTHMULCH, DAMPMULCH, STABLEMULCH, GOOEYMULCH, SHOALSALT, SHOALSHELL, FLOATSTONE, PROTECTIVEPADS, EJECTBUTTON, SMOKEBALL, LUCKYEGG, EXPSHARE, AMULETCOIN, CLEANSETAG, LIGHTCLAY, BINDINGBAND, BLACKSLUDGE, SHELLBELL, ABSORBBULB, CELLBATTERY, LUMINOUSMOSS, SNOWBALL, THROATSPRAY, ADRENALINEORB, LIFEORB, METRONOME, SCOPELENS, KINGSROCK, RAZORFANG, FLAMEORB, TOXICORB, CHARCOAL, MYSTICWATER, MAGNET, MIRACLESEED, NEVERMELTICE, BLACKBELT, TWISTEDSPOON, SPELLTAG, BLACKGLASSES, METALCOAT, LIGHTBALL, SOULDEW, DEEPSEASCALE, EVERSTONE, DRAGONSCALE, UPGRADE, PRISMSCALE, POTION, SUPERPOTION, HYPERPOTION, MAXPOTION, FULLRESTORE, SACREDASH, AWAKENING, ANTIDOTE, BURNHEAL, PARALYZEHEAL, ICEHEAL, FULLHEAL, PEWTERCRUNCHIES, RAGECANDYBAR, LAVACOOKIE, OLDGATEAU, CASTELIACONE, LUMIOSEGALETTE, SHALOURSABLE, BIGMALASADA, REVIVE, MAXREVIVE, BERRYJUICE, SWEETHEART, FRESHWATER, SODAPOP, LEMONADE, MOOMOOMILK, ENERGYPOWDER, ENERGYROOT, HEALPOWDER, REVIVALHERB, MAXHONEY, ETHER, MAXETHER, ELIXIR, MAXELIXIR, PPUP, PPMAX, HPUP, PROTEIN, IRON, CALCIUM, ZINC, CARBOS, EXPCANDYXS, EXPCANDYS, EXPCANDYM, EXPCANDYL, EXPCANDYXL, RARECANDY, XATTACK, XATTACK2, XATTACK3, XATTACK6, XDEFENSE, XDEFENSE2, XDEFENSE3, XDEFENSE6, XSPATK, XSPATK2, XSPATK3, XSPATK6, XSPDEF, XSPDEF2, XSPDEF3, XSPDEF6, XSPEED, XSPEED2, XSPEED3, XSPEED6, XACCURACY, XACCURACY2, XACCURACY3, XACCURACY6, MAXMUSHROOMS, DIREHIT, DIREHIT2, DIREHIT3, GUARDSPEC, RESETURGE, ABILITYURGE, ITEMURGE, ITEMDROP, BLUEFLUTE, YELLOWFLUTE, REDFLUTE, POKEDOLL, FLUFFYTAIL, POKETOY |
| 40 | EVIOLITE, ICYROCK, LUCKYPUNCH, TM54, TM98 |
| 50 | EJECTPACK, SHARPBEAK, FIREMEMORY, WATERMEMORY, ELECTRICMEMORY, GRASSMEMORY, ICEMEMORY, FIGHTINGMEMORY, POISONMEMORY, GROUNDMEMORY, FLYINGMEMORY, PSYCHICMEMORY, BUGMEMORY, ROCKMEMORY, GHOSTMEMORY, DRAGONMEMORY, DARKMEMORY, STEELMEMORY, FAIRYMEMORY, DUBIOUSDISC, TM57, TM66, TM93 |
| 55 | TM78 |
| 60 | ROCKYHELMET, UTILITYUMBRELLA, HEATROCK, DAMPROCK, TERRAINEXTENDER, MACHOBRACE, LEEK, ADAMANTORB, LUSTROUSORB, GRISEOUSORB, TM03, TM34, TM39, TM40, TM46, TM72, TM83, TM88 |
| 65 | TM27, TM55 |
| 70 | POWERWEIGHT, POWERBRACER, POWERBELT, POWERLENS, POWERBAND, POWERANKLET, POISONBARB, DRAGONFANG, DOUSEDRIVE, SHOCKDRIVE, BURNDRIVE, CHILLDRIVE, TM42, TM43, TM47, TM65, TM89 |
| 75 | TM19, TM31, TM60, TM80 |
| 80 | DUSKSTONE, DAWNSTONE, SHINYSTONE, CRACKEDPOT, CHIPPEDPOT, ODDKEYSTONE, ASSAULTVEST, SAFETYGOGGLES, HEAVYDUTYBOOTS, WEAKNESSPOLICY, BLUNDERPOLICY, RAZORCLAW, QUICKCLAW, STICKYBARB, PROTECTOR, ELECTIRIZER, MAGMARIZER, OVALSTONE, WHIPPEDDREAM, SACHET, VENUSAURITE, CHARIZARDITEX, CHARIZARDITEY, BLASTOISINITE, BEEDRILLITE, PIDGEOTITE, ALAKAZITE, SLOWBRONITE, GENGARITE, KANGASKHANITE, PINSIRITE, GYARADOSITE, AERODACTYLITE, MEWTWONITEX, MEWTWONITEY, AMPHAROSITE, STEELIXITE, SCIZORITE, HERACRONITE, HOUNDOOMINITE, TYRANITARITE, SCEPTILITE, BLAZIKENITE, SWAMPERTITE, GARDEVOIRITE, SABLENITE, MAWILITE, AGGRONITE, MEDICHAMITE, MANECTITE, SHARPEDONITE, CAMERUPTITE, ALTARIANITE, BANETTITE, ABSOLITE, GLALITITE, SALAMENCITE, METAGROSSITE, LATIASITE, LATIOSITE, LOPUNNITE, GARCHOMPITE, LUCARIONITE, ABOMASITE, GALLADITE, AUDINITE, DIANCITE, TM02, TM21, TM28, TM30, TM49, TM79, TM81, TM84, TM91, TM96, TM99 |
| 85 | TM59 |
| 90 | GRIPCLAW, FLAMEPLATE, SPLASHPLATE, ZAPPLATE, MEADOWPLATE, ICICLEPLATE, FISTPLATE, TOXICPLATE, EARTHPLATE, SKYPLATE, MINDPLATE, INSECTPLATE, STONEPLATE, SPOOKYPLATE, DRACOPLATE, DREADPLATE, IRONPLATE, PIXIEPLATE, THICKCLUB, DEEPSEATOOTH, TM13, TM24, TM29, TM35, TM36, TM53, TM62, TM94, TM95, TM100 |
| 100 | HELIXFOSSIL, DOMEFOSSIL, OLDAMBER, ROOTFOSSIL, CLAWFOSSIL, SKULLFOSSIL, ARMORFOSSIL, COVERFOSSIL, PLUMEFOSSIL, JAWFOSSIL, SAILFOSSIL, FOSSILIZEDBIRD, FOSSILIZEDFISH, FOSSILIZEDDRAKE, FOSSILIZEDDINO, RAREBONE, ROOMSERVICE, HARDSTONE, TM23, TM26, TM71, TM85 |
| 110 | TM14, TM25, TM38 |
| 120 | TM22, TM52 |
| 130 | BIGNUGGET, IRONBALL, TM50 |
| 150 | TM01, TM15, TM68 |
| 250 | TM64 |

基底至少10的规则仍适用。本表没有展开578种物品的被动效果；实际投掷附效只有主稿具名六种身份／组，其它走强制持物触发，完整处理器WP50。

## 4. 本包主合同覆盖

60项审计身份，文件相对`Data/Scripts/011_Battle/003_Move/`。主文每项提供具体资格／参数／时点／写入，覆盖表不是行为替代。

| 效果身份 | 源文件与起行 | 主合同 |
| --- | --- | --- |
| `AddMoneyGainedFromBattle` | `005_MoveEffects_Misc.rb`:53 | WP47-B §5 |
| `DoubleMoneyGainedFromBattle` | `005_MoveEffects_Misc.rb`:65 | WP47-B §5 |
| `UserMakeSubstitute` | `005_MoveEffects_Misc.rb`:525 | WP47-B §3 |
| `UserSwapsPositionsWithAlly` | `005_MoveEffects_Misc.rb`:654 | WP47-B §2 |
| `BurnAttackerBeforeUserActs` | `005_MoveEffects_Misc.rb`:687 | WP47-B §3 |
| `SetTargetAbilityToSimple` | `007_MoveEffects_BattlerOther.rb`:939 | WP47-B §6 |
| `SetTargetAbilityToInsomnia` | `007_MoveEffects_BattlerOther.rb`:973 | WP47-B §6 |
| `SetUserAbilityToTargetAbility` | `007_MoveEffects_BattlerOther.rb`:1007 | WP47-B §6 |
| `SetTargetAbilityToUserAbility` | `007_MoveEffects_BattlerOther.rb`:1047 | WP47-B §6 |
| `UserTargetSwapAbilities` | `007_MoveEffects_BattlerOther.rb`:1086 | WP47-B §6 |
| `NegateTargetAbility` | `007_MoveEffects_BattlerOther.rb`:1155 | WP47-B §6 |
| `NegateTargetAbilityIfTargetActed` | `007_MoveEffects_BattlerOther.rb`:1178 | WP47-B §6 |
| `IgnoreTargetAbility` | `007_MoveEffects_BattlerOther.rb`:1196 | WP47-B §6 |
| `StartUserAirborne` | `007_MoveEffects_BattlerOther.rb`:1206 | WP47-B §6 |
| `StartTargetAirborneAndAlwaysHitByMoves` | `007_MoveEffects_BattlerOther.rb`:1229 | WP47-B §6 |
| `HitsTargetInSky` | `007_MoveEffects_BattlerOther.rb`:1260 | WP47-B §6 |
| `HitsTargetInSkyGroundsTarget` | `007_MoveEffects_BattlerOther.rb`:1268 | WP47-B §6 |
| `TransformUserIntoTarget` | `007_MoveEffects_BattlerOther.rb`:1338 | WP47-B §6 |
| `UserTakesTargetItem` | `011_MoveEffects_Items.rb`:5 | WP47-B §5 |
| `TargetTakesUserItem` | `011_MoveEffects_Items.rb`:32 | WP47-B §5 |
| `UserTargetSwapItems` | `011_MoveEffects_Items.rb`:73 | WP47-B §5 |
| `RestoreUserConsumedItem` | `011_MoveEffects_Items.rb`:136 | WP47-B §5 |
| `RemoveTargetItem` | `011_MoveEffects_Items.rb`:168 | WP47-B §5 |
| `DestroyTargetBerryOrGem` | `011_MoveEffects_Items.rb`:194 | WP47-B §5 |
| `CorrodeTargetItem` | `011_MoveEffects_Items.rb`:213 | WP47-B §5 |
| `StartTargetCannotUseItem` | `011_MoveEffects_Items.rb`:253 | WP47-B §5 |
| `UserConsumeBerryRaiseDefense2` | `011_MoveEffects_Items.rb`:297 | WP47-B §5 |
| `AllBattlersConsumeBerry` | `011_MoveEffects_Items.rb`:343 | WP47-B §5 |
| `UserConsumeTargetBerry` | `011_MoveEffects_Items.rb`:379 | WP47-B §5 |
| `ThrowUserItemAtTarget` | `011_MoveEffects_Items.rb`:403 | WP47-B §5 |
| `CurseTargetOrLowerUserSpd1RaiseUserAtkDef1` | `012_MoveEffects_ChangeMoveEffect.rb`:140 | WP47-B §3 |
| `FleeFromBattle` | `013_MoveEffects_SwitchingActing.rb`:4 | WP47-B §2 |
| `SwitchOutUserStatusMove` | `013_MoveEffects_SwitchingActing.rb`:23 | WP47-B §2 |
| `SwitchOutUserDamagingMove` | `013_MoveEffects_SwitchingActing.rb`:64 | WP47-B §2 |
| `LowerTargetAtkSpAtk1SwitchOutUser` | `013_MoveEffects_SwitchingActing.rb`:91 | WP47-B §2 |
| `SwitchOutUserPassOnEffects` | `013_MoveEffects_SwitchingActing.rb`:123 | WP47-B §2 |
| `SwitchOutTargetStatusMove` | `013_MoveEffects_SwitchingActing.rb`:153 | WP47-B §2 |
| `SwitchOutTargetDamagingMove` | `013_MoveEffects_SwitchingActing.rb`:228 | WP47-B §2 |
| `BindTarget` | `013_MoveEffects_SwitchingActing.rb`:261 | WP47-B §3 |
| `BindTargetDoublePowerIfTargetUnderwater` | `013_MoveEffects_SwitchingActing.rb`:302 | WP47-B §3 |
| `TrapTargetInBattle` | `013_MoveEffects_SwitchingActing.rb`:316 | WP47-B §3 |
| `TrapTargetInBattleMainEffect` | `013_MoveEffects_SwitchingActing.rb`:351 | WP47-B §3 |
| `TrapTargetInBattleLowerTargetDefSpDef1EachTurn` | `013_MoveEffects_SwitchingActing.rb`:368 | WP47-B §3 |
| `TrapUserAndTargetInBattle` | `013_MoveEffects_SwitchingActing.rb`:393 | WP47-B §3 |
| `TrapAllBattlersInBattleForOneTurn` | `013_MoveEffects_SwitchingActing.rb`:406 | WP47-B §3 |
| `PursueSwitchingFoe` | `013_MoveEffects_SwitchingActing.rb`:426 | WP47-B §3 |
| `UsedAfterUserTakesPhysicalDamage` | `013_MoveEffects_SwitchingActing.rb`:442 | WP47-B §3 |
| `UsedAfterAllyRoundWithDoublePower` | `013_MoveEffects_SwitchingActing.rb`:470 | WP47-B §3 |
| `TargetActsNext` | `013_MoveEffects_SwitchingActing.rb`:491 | WP47-B §3 |
| `TargetActsLast` | `013_MoveEffects_SwitchingActing.rb`:521 | WP47-B §3 |
| `TargetUsesItsLastUsedMoveAgain` | `013_MoveEffects_SwitchingActing.rb`:563 | WP47-B §3 |
| `LowerPPOfTargetLastMoveBy3` | `013_MoveEffects_SwitchingActing.rb`:684 | WP47-B §4 |
| `LowerPPOfTargetLastMoveBy4` | `013_MoveEffects_SwitchingActing.rb`:699 | WP47-B §4 |
| `DisableTargetLastMoveUsed` | `013_MoveEffects_SwitchingActing.rb`:724 | WP47-B §4 |
| `DisableTargetUsingSameMoveConsecutively` | `013_MoveEffects_SwitchingActing.rb`:763 | WP47-B §4 |
| `DisableTargetUsingDifferentMove` | `013_MoveEffects_SwitchingActing.rb`:786 | WP47-B §4 |
| `DisableTargetStatusMoves` | `013_MoveEffects_SwitchingActing.rb`:860 | WP47-B §4 |
| `DisableTargetHealingMoves` | `013_MoveEffects_SwitchingActing.rb`:897 | WP47-B §4 |
| `DisableTargetSoundMoves` | `013_MoveEffects_SwitchingActing.rb`:919 | WP47-B §4 |
| `DisableTargetMovesKnownByUser` | `013_MoveEffects_SwitchingActing.rb`:933 | WP47-B §4 |

## 5. 共享与域外归属

| 效果身份 | 源文件与起行 | 主规则 |
| --- | --- | --- |
| `RemoveUserBindingAndEntryHazards` | `005_MoveEffects_Misc.rb`:558 | WP45 §8危害／种子／束缚清理；WP44升速；本包不重复主合同 |
| `StartGravity` | `007_MoveEffects_BattlerOther.rb`:1299 | WP45 §3/7：重力；本稿§6具名取消当前动作交界 |
| `StartNegateHeldItems` | `011_MoveEffects_Items.rb`:274 | WP45 §3/7：魔法空间建立／直接取消／自然到期 |
| `StartSlowerBattlersActFirst` | `013_MoveEffects_SwitchingActing.rb`:653 | WP45 §3/7：戏法空间建立、期限；WP40调度消费 |
| `HigherPriorityInGrassyTerrain` | `013_MoveEffects_SwitchingActing.rb`:673 | WP47-A §3：青草优先级 |

原WP44状态／阶级范围、WP45天气／侧／位置范围保持。WP47-A承担BattlerOther类型变更与ChangeMoveEffect调用／目标，WP46承担MultiHit、Healing及指定特殊伤害／恢复；三包不重复计算主身份。关于共同消费者只说明本包进入点，主稿已在本轮获限定PASS_SCOPED，但不扩大为完整域外组合通过。全局未归属／AI对应仍WP79／WP52，完整物品／变身／Shadow仍WP50／22／23。

本轮批准：[独立首审报告](../../review/wp46-wp47-review-2026-09-27/report.md)§2／4；A～F／60项换人控制物品与能力操作主合同及默认数据限定通过。本次状态回填、C01维护和必要身份级联分开记账；被审首稿`3a092b6653b0d283a47e45aa4ed9b06b04ca62683a14b17b42048829bf00d83c`（17,454字节）留史，当前新字节不冒充原被审版本。运行、完整形态／物品／AI组合及阶段出口保留。
