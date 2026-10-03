# WP50 持物效果有界覆盖 v1

状态：**Reviewed（限定静态范围，2026-09-28有限复审PASS_SCOPED；管理性回填）**；范围随[WP50主稿](wp50-held-item-triggers-and-consumption.md)A～F的32族／196身份有界合同。32族、165直接登记、21复制语句，别名展开196个（族，物品）身份。复制行第一身份是来源，余身份为本族新登记；不推出其它族也复制。CriticalCalcFromTarget／TrappingByTarget为空，仍有真实调用接口。源码名称仅审计，不按其结构设计未来系统。

## 1. 登记与具体合同

文件为`Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb`。参数、对象、有效性和消费必须结合所指主节，不能从名字补规则。

| 族 | 登记 | 物品身份／复制方向 | 源起行 | 主合同 |
| --- | --- | --- | ---: | --- |
| SpeedCalc | add | CHOICESCARF | 221 | WP50 §3 |
| SpeedCalc | add | IRONBALL | 227 | WP50 §3 |
| SpeedCalc | add | MACHOBRACE | 233 | WP50 §3 |
| SpeedCalc | copy | MACHOBRACE、POWERANKLET、POWERBAND、POWERBELT、POWERBRACER、POWERLENS、POWERWEIGHT | 239 | WP50 §3 |
| SpeedCalc | add | QUICKPOWDER | 243 | WP50 §3 |
| WeightCalc | add | FLOATSTONE | 253 | WP50 §3 |
| HPHeal | add | AGUAVBERRY | 263 | WP50 §4 |
| HPHeal | add | APICOTBERRY | 271 | WP50 §4 |
| HPHeal | add | BERRYJUICE | 277 | WP50 §4 |
| HPHeal | add | FIGYBERRY | 294 | WP50 §4 |
| HPHeal | add | GANLONBERRY | 302 | WP50 §4 |
| HPHeal | add | IAPAPABERRY | 308 | WP50 §4 |
| HPHeal | add | LANSATBERRY | 316 | WP50 §4 |
| HPHeal | add | LIECHIBERRY | 332 | WP50 §4 |
| HPHeal | add | MAGOBERRY | 338 | WP50 §4 |
| HPHeal | add | MICLEBERRY | 346 | WP50 §4 |
| HPHeal | add | ORANBERRY | 364 | WP50 §4 |
| HPHeal | add | PETAYABERRY | 389 | WP50 §4 |
| HPHeal | add | SALACBERRY | 395 | WP50 §4 |
| HPHeal | add | SITRUSBERRY | 401 | WP50 §4 |
| HPHeal | add | STARFBERRY | 426 | WP50 §4 |
| HPHeal | add | WIKIBERRY | 436 | WP50 §4 |
| OnStatLoss | add | EJECTPACK | 447 | WP50 §5 |
| StatusCure | add | ASPEARBERRY | 477 | WP50 §4 |
| StatusCure | add | CHERIBERRY | 490 | WP50 §4 |
| StatusCure | add | CHESTOBERRY | 503 | WP50 §4 |
| StatusCure | add | LUMBERRY | 516 | WP50 §4 |
| StatusCure | add | MENTALHERB | 551 | WP50 §4 |
| StatusCure | add | PECHABERRY | 586 | WP50 §4 |
| StatusCure | add | PERSIMBERRY | 599 | WP50 §4 |
| StatusCure | add | RAWSTBERRY | 617 | WP50 §4 |
| PriorityBracketChange | add | CUSTAPBERRY | 634 | WP50 §3 |
| PriorityBracketChange | add | LAGGINGTAIL | 640 | WP50 §3 |
| PriorityBracketChange | copy | LAGGINGTAIL、FULLINCENSE | 646 | WP50 §3 |
| PriorityBracketChange | add | QUICKCLAW | 648 | WP50 §3 |
| PriorityBracketUse | add | CUSTAPBERRY | 658 | WP50 §3 |
| PriorityBracketUse | add | QUICKCLAW | 666 | WP50 §3 |
| OnMissingTarget | add | BLUNDERPOLICY | 677 | WP50 §3 |
| AccuracyCalcFromUser | add | WIDELENS | 693 | WP50 §3 |
| AccuracyCalcFromUser | add | ZOOMLENS | 699 | WP50 §3 |
| AccuracyCalcFromTarget | add | BRIGHTPOWDER | 713 | WP50 §3 |
| AccuracyCalcFromTarget | copy | BRIGHTPOWDER、LAXINCENSE | 719 | WP50 §3 |
| DamageCalcFromUser | add | ADAMANTORB | 725 | WP50 §3 |
| DamageCalcFromUser | add | BLACKBELT | 733 | WP50 §3 |
| DamageCalcFromUser | copy | BLACKBELT、FISTPLATE | 739 | WP50 §3 |
| DamageCalcFromUser | add | BLACKGLASSES | 741 | WP50 §3 |
| DamageCalcFromUser | copy | BLACKGLASSES、DREADPLATE | 747 | WP50 §3 |
| DamageCalcFromUser | add | BUGGEM | 749 | WP50 §3 |
| DamageCalcFromUser | add | CHARCOAL | 755 | WP50 §3 |
| DamageCalcFromUser | copy | CHARCOAL、FLAMEPLATE | 761 | WP50 §3 |
| DamageCalcFromUser | add | CHOICEBAND | 763 | WP50 §3 |
| DamageCalcFromUser | add | CHOICESPECS | 769 | WP50 §3 |
| DamageCalcFromUser | add | DARKGEM | 775 | WP50 §3 |
| DamageCalcFromUser | add | DEEPSEATOOTH | 781 | WP50 §3 |
| DamageCalcFromUser | add | DRAGONFANG | 789 | WP50 §3 |
| DamageCalcFromUser | copy | DRAGONFANG、DRACOPLATE | 795 | WP50 §3 |
| DamageCalcFromUser | add | DRAGONGEM | 797 | WP50 §3 |
| DamageCalcFromUser | add | ELECTRICGEM | 803 | WP50 §3 |
| DamageCalcFromUser | add | EXPERTBELT | 809 | WP50 §3 |
| DamageCalcFromUser | add | FAIRYGEM | 817 | WP50 §3 |
| DamageCalcFromUser | add | FIGHTINGGEM | 823 | WP50 §3 |
| DamageCalcFromUser | add | FIREGEM | 829 | WP50 §3 |
| DamageCalcFromUser | add | FLYINGGEM | 835 | WP50 §3 |
| DamageCalcFromUser | add | GHOSTGEM | 841 | WP50 §3 |
| DamageCalcFromUser | add | GRASSGEM | 847 | WP50 §3 |
| DamageCalcFromUser | add | GRISEOUSORB | 853 | WP50 §3 |
| DamageCalcFromUser | add | GROUNDGEM | 861 | WP50 §3 |
| DamageCalcFromUser | add | HARDSTONE | 867 | WP50 §3 |
| DamageCalcFromUser | copy | HARDSTONE、STONEPLATE、ROCKINCENSE | 873 | WP50 §3 |
| DamageCalcFromUser | add | ICEGEM | 875 | WP50 §3 |
| DamageCalcFromUser | add | LIFEORB | 881 | WP50 §3 |
| DamageCalcFromUser | add | LIGHTBALL | 889 | WP50 §3 |
| DamageCalcFromUser | add | LUSTROUSORB | 895 | WP50 §3 |
| DamageCalcFromUser | add | MAGNET | 903 | WP50 §3 |
| DamageCalcFromUser | copy | MAGNET、ZAPPLATE | 909 | WP50 §3 |
| DamageCalcFromUser | add | METALCOAT | 911 | WP50 §3 |
| DamageCalcFromUser | copy | METALCOAT、IRONPLATE | 917 | WP50 §3 |
| DamageCalcFromUser | add | METRONOME | 919 | WP50 §3 |
| DamageCalcFromUser | add | MIRACLESEED | 926 | WP50 §3 |
| DamageCalcFromUser | copy | MIRACLESEED、MEADOWPLATE、ROSEINCENSE | 932 | WP50 §3 |
| DamageCalcFromUser | add | MUSCLEBAND | 934 | WP50 §3 |
| DamageCalcFromUser | add | MYSTICWATER | 940 | WP50 §3 |
| DamageCalcFromUser | copy | MYSTICWATER、SPLASHPLATE、SEAINCENSE、WAVEINCENSE | 946 | WP50 §3 |
| DamageCalcFromUser | add | NEVERMELTICE | 948 | WP50 §3 |
| DamageCalcFromUser | copy | NEVERMELTICE、ICICLEPLATE | 954 | WP50 §3 |
| DamageCalcFromUser | add | NORMALGEM | 956 | WP50 §3 |
| DamageCalcFromUser | add | PIXIEPLATE | 962 | WP50 §3 |
| DamageCalcFromUser | add | POISONBARB | 968 | WP50 §3 |
| DamageCalcFromUser | copy | POISONBARB、TOXICPLATE | 974 | WP50 §3 |
| DamageCalcFromUser | add | POISONGEM | 976 | WP50 §3 |
| DamageCalcFromUser | add | PSYCHICGEM | 982 | WP50 §3 |
| DamageCalcFromUser | add | ROCKGEM | 988 | WP50 §3 |
| DamageCalcFromUser | add | SHARPBEAK | 994 | WP50 §3 |
| DamageCalcFromUser | copy | SHARPBEAK、SKYPLATE | 1000 | WP50 §3 |
| DamageCalcFromUser | add | SILKSCARF | 1002 | WP50 §3 |
| DamageCalcFromUser | add | SILVERPOWDER | 1008 | WP50 §3 |
| DamageCalcFromUser | copy | SILVERPOWDER、INSECTPLATE | 1014 | WP50 §3 |
| DamageCalcFromUser | add | SOFTSAND | 1016 | WP50 §3 |
| DamageCalcFromUser | copy | SOFTSAND、EARTHPLATE | 1022 | WP50 §3 |
| DamageCalcFromUser | add | SOULDEW | 1024 | WP50 §3 |
| DamageCalcFromUser | add | SPELLTAG | 1035 | WP50 §3 |
| DamageCalcFromUser | copy | SPELLTAG、SPOOKYPLATE | 1041 | WP50 §3 |
| DamageCalcFromUser | add | STEELGEM | 1043 | WP50 §3 |
| DamageCalcFromUser | add | THICKCLUB | 1049 | WP50 §3 |
| DamageCalcFromUser | add | TWISTEDSPOON | 1057 | WP50 §3 |
| DamageCalcFromUser | copy | TWISTEDSPOON、MINDPLATE、ODDINCENSE | 1063 | WP50 §3 |
| DamageCalcFromUser | add | WATERGEM | 1065 | WP50 §3 |
| DamageCalcFromUser | add | WISEGLASSES | 1071 | WP50 §3 |
| DamageCalcFromTarget | add | ASSAULTVEST | 1084 | WP50 §3 |
| DamageCalcFromTarget | add | BABIRIBERRY | 1090 | WP50 §3 |
| DamageCalcFromTarget | add | CHARTIBERRY | 1096 | WP50 §3 |
| DamageCalcFromTarget | add | CHILANBERRY | 1102 | WP50 §3 |
| DamageCalcFromTarget | add | CHOPLEBERRY | 1108 | WP50 §3 |
| DamageCalcFromTarget | add | COBABERRY | 1114 | WP50 §3 |
| DamageCalcFromTarget | add | COLBURBERRY | 1120 | WP50 §3 |
| DamageCalcFromTarget | add | DEEPSEASCALE | 1126 | WP50 §3 |
| DamageCalcFromTarget | add | EVIOLITE | 1134 | WP50 §3 |
| DamageCalcFromTarget | add | HABANBERRY | 1146 | WP50 §3 |
| DamageCalcFromTarget | add | KASIBBERRY | 1152 | WP50 §3 |
| DamageCalcFromTarget | add | KEBIABERRY | 1158 | WP50 §3 |
| DamageCalcFromTarget | add | METALPOWDER | 1164 | WP50 §3 |
| DamageCalcFromTarget | add | OCCABERRY | 1172 | WP50 §3 |
| DamageCalcFromTarget | add | PASSHOBERRY | 1178 | WP50 §3 |
| DamageCalcFromTarget | add | PAYAPABERRY | 1184 | WP50 §3 |
| DamageCalcFromTarget | add | RINDOBERRY | 1190 | WP50 §3 |
| DamageCalcFromTarget | add | ROSELIBERRY | 1196 | WP50 §3 |
| DamageCalcFromTarget | add | SHUCABERRY | 1202 | WP50 §3 |
| DamageCalcFromTarget | add | SOULDEW | 1208 | WP50 §3 |
| DamageCalcFromTarget | add | TANGABERRY | 1218 | WP50 §3 |
| DamageCalcFromTarget | add | WACANBERRY | 1224 | WP50 §3 |
| DamageCalcFromTarget | add | YACHEBERRY | 1230 | WP50 §3 |
| CriticalCalcFromUser | add | LUCKYPUNCH | 1240 | WP50 §3 |
| CriticalCalcFromUser | add | RAZORCLAW | 1246 | WP50 §3 |
| CriticalCalcFromUser | copy | RAZORCLAW、SCOPELENS | 1252 | WP50 §3 |
| CriticalCalcFromUser | add | LEEK | 1254 | WP50 §3 |
| CriticalCalcFromUser | copy | LEEK、STICK | 1260 | WP50 §3 |
| OnBeingHit | add | ABSORBBULB | 1272 | WP50 §5 |
| OnBeingHit | add | AIRBALLOON | 1282 | WP50 §5 |
| OnBeingHit | add | CELLBATTERY | 1290 | WP50 §5 |
| OnBeingHit | add | ENIGMABERRY | 1300 | WP50 §5 |
| OnBeingHit | add | JABOCABERRY | 1311 | WP50 §5 |
| OnBeingHit | add | KEEBERRY | 1338 | WP50 §5 |
| OnBeingHit | add | LUMINOUSMOSS | 1347 | WP50 §5 |
| OnBeingHit | add | MARANGABERRY | 1362 | WP50 §5 |
| OnBeingHit | add | ROCKYHELMET | 1371 | WP50 §5 |
| OnBeingHit | add | ROWAPBERRY | 1381 | WP50 §5 |
| OnBeingHit | add | SNOWBALL | 1403 | WP50 §5 |
| OnBeingHit | add | STICKYBARB | 1413 | WP50 §5 |
| OnBeingHit | add | WEAKNESSPOLICY | 1430 | WP50 §5 |
| OnBeingHitPositiveBerry | add | ENIGMABERRY | 1456 | WP50 §5 |
| OnBeingHitPositiveBerry | add | KEEBERRY | 1481 | WP50 §5 |
| OnBeingHitPositiveBerry | add | MARANGABERRY | 1501 | WP50 §5 |
| AfterMoveUseFromTarget | add | EJECTBUTTON | 1525 | WP50 §5 |
| AfterMoveUseFromTarget | add | REDCARD | 1543 | WP50 §5 |
| AfterMoveUseFromUser | add | LIFEORB | 1579 | WP50 §5 |
| AfterMoveUseFromUser | add | SHELLBELL | 1600 | WP50 §5 |
| AfterMoveUseFromUser | add | THROATSPRAY | 1612 | WP50 §5 |
| OnEndOfUsingMove | add | LEPPABERRY | 1628 | WP50 §4 |
| OnEndOfUsingMoveStatRestore | add | WHITEHERB | 1669 | WP50 §4 |
| ExpGainModifier | add | LUCKYEGG | 1696 | WP50 §6 |
| EVGainModifier | add | MACHOBRACE | 1706 | WP50 §6 |
| EVGainModifier | add | POWERANKLET | 1712 | WP50 §6 |
| EVGainModifier | add | POWERBAND | 1718 | WP50 §6 |
| EVGainModifier | add | POWERBELT | 1724 | WP50 §6 |
| EVGainModifier | add | POWERBRACER | 1730 | WP50 §6 |
| EVGainModifier | add | POWERLENS | 1736 | WP50 §6 |
| EVGainModifier | add | POWERWEIGHT | 1742 | WP50 §6 |
| WeatherExtender | add | DAMPROCK | 1752 | WP50 §6 |
| WeatherExtender | add | HEATROCK | 1758 | WP50 §6 |
| WeatherExtender | add | ICYROCK | 1764 | WP50 §6 |
| WeatherExtender | add | SMOOTHROCK | 1770 | WP50 §6 |
| TerrainExtender | add | TERRAINEXTENDER | 1780 | WP50 §6 |
| TerrainStatBoost | add | ELECTRICSEED | 1790 | WP50 §6 |
| TerrainStatBoost | add | GRASSYSEED | 1800 | WP50 §6 |
| TerrainStatBoost | add | MISTYSEED | 1810 | WP50 §6 |
| TerrainStatBoost | add | PSYCHICSEED | 1820 | WP50 §6 |
| EndOfRoundHealing | add | BLACKSLUDGE | 1834 | WP50 §6 |
| EndOfRoundHealing | add | LEFTOVERS | 1851 | WP50 §6 |
| EndOfRoundEffect | add | FLAMEORB | 1865 | WP50 §6 |
| EndOfRoundEffect | add | STICKYBARB | 1872 | WP50 §6 |
| EndOfRoundEffect | add | TOXICORB | 1882 | WP50 §6 |
| CertainSwitching | add | SHEDSHELL | 1894 | WP50 §6 |
| OnSwitchIn | add | AIRBALLOON | 1910 | WP50 §6 |
| OnSwitchIn | add | ROOMSERVICE | 1917 | WP50 §6 |
| OnIntimidated | add | ADRENALINEORB | 1931 | WP50 §6 |
| CertainEscapeFromBattle | add | SMOKEBALL | 1944 | WP50 §6 |

## 2. 类型宝石与减伤果完整映射

所有当前类型宝石均与对应类型匹配，默认18项；减伤果18项。下表是实际处理器传给helper的类型数据，不是按物品名猜测；条件及数值在主稿§3.2。

| 角色 | 物品身份 | 类型 |
| --- | --- | --- |
| 宝石 | BUGGEM | BUG |
| 宝石 | DARKGEM | DARK |
| 宝石 | DRAGONGEM | DRAGON |
| 宝石 | ELECTRICGEM | ELECTRIC |
| 宝石 | FAIRYGEM | FAIRY |
| 宝石 | FIGHTINGGEM | FIGHTING |
| 宝石 | FIREGEM | FIRE |
| 宝石 | FLYINGGEM | FLYING |
| 宝石 | GHOSTGEM | GHOST |
| 宝石 | GRASSGEM | GRASS |
| 宝石 | GROUNDGEM | GROUND |
| 宝石 | ICEGEM | ICE |
| 宝石 | NORMALGEM | NORMAL |
| 宝石 | POISONGEM | POISON |
| 宝石 | PSYCHICGEM | PSYCHIC |
| 宝石 | ROCKGEM | ROCK |
| 宝石 | STEELGEM | STEEL |
| 宝石 | WATERGEM | WATER |
| 减伤果 | BABIRIBERRY | STEEL |
| 减伤果 | CHARTIBERRY | ROCK |
| 减伤果 | CHILANBERRY | NORMAL |
| 减伤果 | CHOPLEBERRY | FIGHTING |
| 减伤果 | COBABERRY | FLYING |
| 减伤果 | COLBURBERRY | DARK |
| 减伤果 | HABANBERRY | DRAGON |
| 减伤果 | KASIBBERRY | GHOST |
| 减伤果 | KEBIABERRY | POISON |
| 减伤果 | OCCABERRY | FIRE |
| 减伤果 | PASSHOBERRY | WATER |
| 减伤果 | PAYAPABERRY | PSYCHIC |
| 减伤果 | RINDOBERRY | GRASS |
| 减伤果 | ROSELIBERRY | FAIRY |
| 减伤果 | SHUCABERRY | GROUND |
| 减伤果 | TANGABERRY | BUG |
| 减伤果 | WACANBERRY | ELECTRIC |
| 减伤果 | YACHEBERRY | ICE |

## 3. 覆盖边界

所有32族含两空族具名；静态全Scripts登记检索未见其它文件追加。同物品多族分别计，196不是196种不同物品。注册外核心包括气势道具、接触／粉末护具、背心／讲究锁、天气伞、根／爪／香草／黏土等，主稿§7引用已有明确合同，不能以缺登记默认无效果。主动道具WP28与物品招式WP47-B、自然之恩／投掷默认数据沿原已审主规格，不重写。全局组合、AI/设施、运行及出口仍未关闭。

本次闭合回填：2026-09-28 [独立有限复审报告](../../review/wp50-wp51-wp52a-recheck-2026-09-28/report.md)§3–4，32族／196展开身份与已述消费/计算合同限定通过；本次只维护状态、排版与完整身份，行为及场景输入/期望不变。被审附表v1 `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686`（13,855字节）保留历史；当前新字节不冒充被审对象。运行及阶段出口继续保留。
