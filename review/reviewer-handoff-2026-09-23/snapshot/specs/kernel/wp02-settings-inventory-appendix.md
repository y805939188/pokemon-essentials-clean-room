# WP02 附表：逐定义配置清单与检索索引（参考侧取证材料）

本附表是 [wp02-rule-configuration-and-data-variants](wp02-rule-configuration-and-data-variants.md) 的取证附件。
**生成路径**：本 Markdown 由 `analysis/inventory/wp02_build_appendix.py` 写出；`analysis/inventory/wp02_settings_inventory.py` 是独立的控制台清单程序，两者共用 `analysis/inventory/wp02_settings_common.py` 对固定基线（commit `8c5911e4`）的设置文件做**只读解析**（不修改 reference）。统计由本表逐定义行独立复算，不采用任何审查方给出的数字。

## 1. 统计单位约定

- **独立常量**：`Settings` 命名空间内单个常量定义（合并展示行按展开计）。
- **方法型配置**：`def self.<name>` 定义的配置方法（调用形式为 `Settings.<name>`，与常量的 `Settings::<NAME>` 不同）。
- **元信息**：`Essentials` 命名空间常量，不属于 Settings 统计。
- **展示行**：WP02 主文档词典表格中的行（一个展示行可合并多个常量）。
- **值列口径**："派生"列记录表达式/引用关系；"世代 8 默认值"列记录求值结果；无法解析的项显式标"未求值"并附原因，不静默吞掉。

## 2. 独立复算统计

| 集合 | 数量 | 复算方式 |
| --- | --- | --- |
| 001 Settings 常量 | 88 | 第 3 表逐行计数 |
| 002 Settings 常量 | 30 | 第 4 表逐行计数 |
| Settings 常量合计 | 118 | 88 + 30 |
| 世代派生常量 | 47 | 第 3、4 表"派生"列以"世代"开头行计数（001 文件 25 + 002 文件 22） |
| 设置间派生 | 1 | APPLY_HAPPINESS_SOFT_CAP（= AFFECTION_EFFECTS） |
| 方法型配置 | 3 | 第 5 表 |
| Essentials 元信息 | 3 | 第 6 表 |
| 世代派生阈值分组 | (==5):1、(==5或≥7):1、(≤3):1、(≤4):1、(≤5):2、(≤6):2、(≤7):1、(≥4):7、(≥5):1、(≥6):11、(≥7):9、(≥8):10 | 第 3、4 表"派生"列分组计数 |

世代派生中含数值型 6 条：SHINY_POKEMON_CHANCE（16 或 8）、NUM_BADGES_BOOST 五项（999 或 1/5/7/7/3）；其余 41 条为布尔型。
本轮求值覆盖检查：未求值项 = 无（118 常量全部求值）。

## 3. 逐定义清单：`S/001_Settings.rb`（Settings 命名空间常量）

| 行 | 键名 | 派生 | 世代 8 默认值 | 词典分组 |
| --- | --- | --- | --- | --- |
| 9 | GAME_VERSION | 独立 | "1.0.0" | 元信息 |
| 17 | MECHANICS_GENERATION | 独立 | 8 | 元信息 |
| 49 | MAX_MONEY | 独立 | 999_999 | 玩家资源 |
| 51 | MAX_COINS | 独立 | 99_999 | 玩家资源 |
| 53 | MAX_BATTLE_POINTS | 独立 | 9_999 | 玩家资源 |
| 55 | MAX_SOOT | 独立 | 9_999 | 玩家资源 |
| 57 | MAX_PLAYER_NAME_SIZE | 独立 | 10 | 玩家资源 |
| 61 | RIVAL_NAMES | 独立 | 数组（见词典） | 玩家资源 |
| 72 | TIME_SHADING | 独立 | true | 世界与野外 |
| 74 | ANIMATE_REFLECTIONS | 独立 | true | 世界与野外 |
| 77 | NEW_BERRY_PLANTS | 世代(≥4) | true | 世界与野外 |
| 80 | FISHING_AUTO_HOOK | 独立 | false | 世界与野外 |
| 83 | FISHING_BEGIN_COMMON_EVENT | 独立 | -1 | 世界与野外 |
| 86 | FISHING_END_COMMON_EVENT | 独立 | -1 | 世界与野外 |
| 88 | SAFARI_STEPS | 独立 | 600 | 世界与野外 |
| 90 | BUG_CONTEST_TIME | 独立 | 20 * 60（= 1200） | 世界与野外 |
| 97 | NO_SIGNPOSTS | 独立 | 数组（见词典） | 世界与野外 |
| 99 | POISON_IN_FIELD | 世代(≤4) | false | 世界与野外 |
| 102 | POISON_FAINT_IN_FIELD | 世代(≤3) | false | 世界与野外 |
| 110 | FIELD_MOVES_COUNT_BADGES | 独立 | true | 场地招式许可 |
| 117 | BADGE_FOR_CUT | 独立 | 1 | 场地招式许可 |
| 118 | BADGE_FOR_FLASH | 独立 | 2 | 场地招式许可 |
| 119 | BADGE_FOR_ROCKSMASH | 独立 | 3 | 场地招式许可 |
| 120 | BADGE_FOR_SURF | 独立 | 4 | 场地招式许可 |
| 121 | BADGE_FOR_FLY | 独立 | 5 | 场地招式许可 |
| 122 | BADGE_FOR_STRENGTH | 独立 | 6 | 场地招式许可 |
| 123 | BADGE_FOR_DIVE | 独立 | 7 | 场地招式许可 |
| 124 | BADGE_FOR_WATERFALL | 独立 | 8 | 场地招式许可 |
| 131 | MAXIMUM_LEVEL | 独立 | 100 | 个体与生成 |
| 133 | EGG_LEVEL | 独立 | 1 | 个体与生成 |
| 135 | SHINY_POKEMON_CHANCE | 世代(≥6) | 16 | 个体与生成 |
| 137 | SUPER_SHINY | 世代(≥8) | true | 个体与生成 |
| 140 | LEGENDARIES_HAVE_SOME_PERFECT_IVS | 世代(≥6) | true | 个体与生成 |
| 142 | POKERUS_CHANCE | 独立 | 3 | 个体与生成 |
| 146 | DISABLE_IVS_AND_EVS | 独立 | false | 个体与生成 |
| 151 | MOVE_RELEARNER_CAN_TEACH_MORE_MOVES | 世代(≥6) | true | 个体与生成 |
| 160 | DAY_CARE_POKEMON_GAIN_EXP_FROM_WALKING | 世代(≤6) | false | 寄养与繁殖 |
| 163 | DAY_CARE_POKEMON_CAN_SHARE_EGG_MOVES | 世代(≥8) | true | 寄养与繁殖 |
| 166 | BREEDING_CAN_INHERIT_MACHINE_MOVES | 世代(≤5) | false | 寄养与繁殖 |
| 169 | BREEDING_CAN_INHERIT_EGG_MOVES_FROM_MOTHER | 世代(≥6) | true | 寄养与繁殖 |
| 177 | ROAMING_AREAS | 独立 | 哈希（见词典） | 漫游 |
| 203 | ROAMING_SPECIES | 独立 | 数组（见词典） | 漫游 |
| 220 | MAX_PARTY_SIZE | 独立 | 6 | 队伍与储存 |
| 222 | NUM_STORAGE_BOXES | 独立 | 40 | 队伍与储存 |
| 225 | HEAL_STORED_POKEMON | 世代(≤7) | false | 队伍与储存 |
| 233 | REBALANCED_HEALING_ITEM_AMOUNTS | 世代(≥7) | true | 道具效果 |
| 236 | NO_VITAMIN_EV_CAP | 世代(≥8) | true | 道具效果 |
| 238 | RAGE_CANDY_BAR_CURES_STATUS_PROBLEMS | 世代(≥7) | true | 道具效果 |
| 242 | FLUTES_CHANGE_WILD_ENCOUNTER_LEVELS | 世代(≥6) | true | 道具效果 |
| 245 | RARE_CANDY_USABLE_AT_MAX_LEVEL | 世代(≥8) | true | 道具效果 |
| 249 | USE_MULTIPLE_STAT_ITEMS_AT_ONCE | 世代(≥8) | true | 道具效果 |
| 253 | TAUGHT_MACHINES_KEEP_OLD_PP | 世代(==5) | false | 道具效果 |
| 257 | MORE_BONUS_PREMIER_BALLS | 世代(≥8) | true | 道具效果 |
| 277 | BAG_MAX_POCKET_SIZE | 独立 | 数组（见词典） | 背包 |
| 280 | BAG_POCKET_AUTO_SORT | 独立 | 数组（见词典） | 背包 |
| 282 | BAG_MAX_PER_SLOT | 独立 | 999 | 背包 |
| 306 | USE_CURRENT_REGION_DEX | 独立 | false | 图鉴 |
| 311 | DEX_SHOWS_ALL_FORMS | 独立 | false | 图鉴 |
| 315 | DEXES_WITH_OFFSETS | 独立 | 数组（见词典） | 图鉴 |
| 319 | SHOW_NEW_SPECIES_POKEDEX_ENTRY_MORE_OFTEN | 世代(≥7) | true | 图鉴 |
| 333 | REGION_MAP_EXTRAS | 独立 | 数组（见词典） | 城镇地图 |
| 339 | CAN_FLY_FROM_TOWN_MAP | 独立 | true | 城镇地图 |
| 348 | PHONE_REMATCHES_POSSIBLE_FROM_BEGINNING | 独立 | false | 电话 |
| 353 | COLOR_PHONE_CALL_MESSAGES_BY_CONTACT_GENDER | 独立 | true | 电话 |
| 361 | REPEL_COUNTS_FAINTED_POKEMON | 世代(≥6) | true | 遭遇与战斗开始 |
| 364 | MORE_ABILITIES_AFFECT_WILD_ENCOUNTERS | 世代(≥8) | true | 遭遇与战斗开始 |
| 367 | HIGHER_SHINY_CHANCES_WITH_NUMBER_BATTLED | 世代(≥8) | true | 遭遇与战斗开始 |
| 370 | OVERWORLD_WEATHER_SETS_BATTLE_TERRAIN | 世代(≥8) | true | 遭遇与战斗开始 |
| 377 | STARTING_OVER_SWITCH | 独立 | 1 | 游戏开关 ID |
| 380 | SEEN_POKERUS_SWITCH | 独立 | 2 | 游戏开关 ID |
| 382 | SHINY_WILD_POKEMON_SWITCH | 独立 | 31 | 游戏开关 ID |
| 385 | FATEFUL_ENCOUNTER_SWITCH | 独立 | 32 | 游戏开关 ID |
| 389 | DISABLE_BOX_LINK_SWITCH | 独立 | 35 | 游戏开关 ID |
| 396 | GRASS_ANIMATION_ID | 独立 | 1 | 动画 ID |
| 399 | DUST_ANIMATION_ID | 独立 | 2 | 动画 ID |
| 402 | EXCLAMATION_ANIMATION_ID | 独立 | 3 | 动画 ID |
| 405 | RUSTLE_NORMAL_ANIMATION_ID | 独立 | 1 | 动画 ID |
| 408 | RUSTLE_VIGOROUS_ANIMATION_ID | 独立 | 5 | 动画 ID |
| 411 | RUSTLE_SHINY_ANIMATION_ID | 独立 | 6 | 动画 ID |
| 414 | PLANT_SPARKLE_ANIMATION_ID | 独立 | 7 | 动画 ID |
| 425 | LANGUAGES | 独立 | 数组（见词典） | 语言 |
| 436 | SCREEN_WIDTH | 独立 | 512 | 屏幕 |
| 439 | SCREEN_HEIGHT | 独立 | 384 | 屏幕 |
| 441 | SCREEN_SCALE | 独立 | 1.0 | 屏幕 |
| 448 | SPEECH_WINDOWSKINS | 独立 | 数组（见词典） | 窗口皮肤 |
| 472 | MENU_WINDOWSKINS | 独立 | 数组（见词典） | 窗口皮肤 |
| 510 | PROMPT_TO_COMPILE | 独立 | false | 调试 |
| 514 | SKIP_CONTINUE_SCREEN | 独立 | false | 调试 |

## 4. 逐定义清单：`S/002_BattleSettings.rb`（Settings 命名空间常量）

| 行 | 键名 | 派生 | 世代 8 默认值 | 词典分组 |
| --- | --- | --- | --- | --- |
| 10 | RECALCULATE_TURN_ORDER_AFTER_MEGA_EVOLUTION | 世代(≥7) | true | 回合顺序与服从 |
| 12 | RECALCULATE_TURN_ORDER_AFTER_SPEED_CHANGES | 世代(≥8) | true | 回合顺序与服从 |
| 16 | ANY_HIGH_LEVEL_POKEMON_CAN_DISOBEY | 独立 | false | 回合顺序与服从 |
| 19 | FOREIGN_HIGH_LEVEL_POKEMON_CAN_DISOBEY | 独立 | true | 回合顺序与服从 |
| 27 | NO_MEGA_EVOLUTION | 独立 | 34 | Mega 开关 |
| 35 | MOVE_CATEGORY_PER_MOVE | 世代(≥4) | true | 招式计算 |
| 39 | NEW_CRITICAL_HIT_RATE_MECHANICS | 世代(≥6) | true | 招式计算 |
| 45 | MORE_TYPE_EFFECTS | 世代(≥6) | true | 招式计算 |
| 48 | NUM_BADGES_BOOST_ATTACK | 世代(≥4) | 999 | 招式计算 |
| 49 | NUM_BADGES_BOOST_DEFENSE | 世代(≥4) | 999 | 招式计算 |
| 50 | NUM_BADGES_BOOST_SPATK | 世代(≥4) | 999 | 招式计算 |
| 51 | NUM_BADGES_BOOST_SPDEF | 世代(≥4) | 999 | 招式计算 |
| 52 | NUM_BADGES_BOOST_SPEED | 世代(≥4) | 999 | 招式计算 |
| 59 | FIXED_DURATION_WEATHER_FROM_ABILITY | 世代(≥6) | true | 特性与道具效果 |
| 62 | X_STAT_ITEMS_RAISE_BY_TWO_STAGES | 世代(≥7) | true | 特性与道具效果 |
| 65 | NEW_POKE_BALL_CATCH_RATES | 世代(≥7) | true | 特性与道具效果 |
| 68 | SOUL_DEW_POWERS_UP_TYPES | 世代(≥7) | true | 特性与道具效果 |
| 77 | AFFECTION_EFFECTS | 独立 | false | 亲密 |
| 82 | APPLY_HAPPINESS_SOFT_CAP | 设置间(=AFFECTION_EFFECTS) | false | 亲密 |
| 92 | ENABLE_CRITICAL_CAPTURES | 世代(≥5) | true | 捕获 |
| 96 | NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER | 世代(≥7) | true | 捕获 |
| 104 | SCALED_EXP_FORMULA | 世代(==5或≥7) | true | 经验与 EV |
| 109 | SPLIT_EXP_BETWEEN_GAINERS | 世代(≤5) | false | 经验与 EV |
| 112 | MORE_EXP_FROM_TRAINER_POKEMON | 世代(≤6) | false | 经验与 EV |
| 115 | MORE_EVS_FROM_POWER_ITEMS | 世代(≥7) | true | 经验与 EV |
| 117 | GAIN_EXP_FOR_CAPTURE | 世代(≥6) | true | 经验与 EV |
| 125 | NO_MONEY_LOSS | 独立 | 33 | 战后 |
| 128 | CHECK_EVOLUTION_AFTER_ALL_BATTLES | 世代(≥6) | true | 战后 |
| 130 | CHECK_EVOLUTION_FOR_FAINTED_POKEMON | 独立 | true | 战后 |
| 139 | SMARTER_WILD_LEGENDARY_POKEMON | 独立 | true | AI |

## 5. 方法型配置（`def self.*`）

| 文件 | 行 | 键名 | 调用形式 | 已见使用点 | 词典分组 |
| --- | --- | --- | --- | --- | --- |
| 001_Settings.rb | 28 | game_credits | `Settings.game_credits` | `S/016_UI/001_Non-interactive UI/007_UI_Credits.rb:61`（`Settings.game_credits \|\| []`） | 元信息 |
| 001_Settings.rb | 264 | bag_pocket_names | `Settings.bag_pocket_names` | `S/013_Items/008_PokemonBag.rb:12`；编辑器/调试 2 处 | 背包 |
| 001_Settings.rb | 296 | pokedex_names | `Settings.pokedex_names` | `S/016_UI/003_UI_Pokedex_Main.rb:427,872`；`S/016_UI/002_UI_Pokedex_Menu.rb:102`；调试 1 处 | 图鉴 |

## 6. Essentials 命名空间元信息（不混入 Settings 统计）

| 文件 | 行 | 键名 | 值 | 备注 |
| --- | --- | --- | --- | --- |
| 001_Settings.rb | 521 | VERSION | "21.1" | 源文件标记为不可编辑 |
| 001_Settings.rb | 522 | ERROR_TEXT | "" | 源文件标记为不可编辑 |
| 001_Settings.rb | 523 | MKXPZ_VERSION | "2.4.2/c9378cf" | 源文件标记为不可编辑 |

## 7. 检索索引（WP02-R03：命中与消费者分类）

### 7.1 检索规则

- 常量使用点：`grep -rn "Settings::<NAME>\b" --include="*.rb" S/`（`::` 形式，词边界）。
- 方法型使用点：`grep -rn "Settings\.<name>" --include="*.rb" S/`（`.` 形式；常量模式会漏掉此类调用）。
- 世代直接引用：`grep -rn "Settings::MECHANICS_GENERATION" --include="*.rb" S/`（不含两个设置文件内部的裸常量）。
- 命中分类：**文件级命中**（含该串的文件数）、**行级出现**（总行数）、**注释命中**（命中行形如注释）。行级出现不等于独立分支数：同一条件表达式可多次出现，同一文件可含多个判断。

### 7.2 世代直接引用统计（本轮实测）

| 指标 | 数值 | 说明 |
| --- | --- | --- |
| 含直接引用的文件 | 41 | 文件级命中，不含两个设置文件 |
| 行级出现总数 | 139 | 例：`006_MoveEffects_BattlerStats.rb` 11 行、`008_Battle_AbilityEffects.rb` 12 行 |
| 注释命中 | 0 | 全部出现在代码行 |

结论限定：只能说"41 个文件含直接世代引用、共 139 行出现"；不能称为"41 处分支"，也不排除同一路径同时受其他设置影响。

### 7.3 LANGUAGES 使用点分类（本轮实测）

| 位置 | 行 | 分类 | 内容 |
| --- | --- | --- | --- |
| `S/003_Game processing/001_StartGame.rb` | 31–33 | 已核消费者（代码） | 多语言且无存档时进入语言选择；按选择加载文本资源 |
| `S/016_UI/013_UI_Load.rb` | 307, 337 | 已核消费者（代码） | 载入界面在候选 ≥2 时显示语言菜单；按选择加载文本资源 |
| `S/019_Utilities/001_Utilities.rb` | 605 | 已核消费者（代码） | 生成语言选项列表 |
| `S/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb` | 1428–1439 | 已核消费者（代码） | 调试菜单切换语言 |
| `S/016_UI/015_UI_Options.rb` | 28 | **注释命中** | 注释性引用，非使用 |

### 7.4 重点设置行级分类（WP02 词典第 4.3 节 16 个开关）

GAIN_EXP_FOR_CAPTURE(2 行)、ENABLE_CRITICAL_CAPTURES(1)、NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER(2)、AFFECTION_EFFECTS(5)、APPLY_HAPPINESS_SOFT_CAP(12)、RECALCULATE_TURN_ORDER_AFTER_MEGA_EVOLUTION(1)、NO_MEGA_EVOLUTION(1)、CHECK_EVOLUTION_AFTER_ALL_BATTLES(1)、CHECK_EVOLUTION_FOR_FAINTED_POKEMON(1)、HEAL_STORED_POKEMON(8)、DISABLE_IVS_AND_EVS(2)、OVERWORLD_WEATHER_SETS_BATTLE_TERRAIN(1)、MORE_ABILITIES_AFFECT_WILD_ENCOUNTERS(7)、LEGENDARIES_HAVE_SOME_PERFECT_IVS(1)、HIGHER_SHINY_CHANCES_WITH_NUMBER_BATTLED(1)、MOVE_CATEGORY_PER_MOVE(4)：以上行级出现**注释命中均为 0**，均为代码行候选使用点；逐行行为语义仍归领域包确认。

### 7.5 设施引用集合与普通发现规则的关系（本轮从名单实际解析）

当前名单 `P/battle_facility_lists.txt` 含 1 个 DefaultTrainerList 与 4 个 TrainerList，每节各 1 个 Trainers 与 1 个 Pokemon 字段，去重后**被引用输入路径共 10 个**：

| 名单节 | 字段 | 引用路径 | 普通发现可匹配 |
| --- | --- | --- | --- |
| DefaultTrainerList | Trainers | battle_tower_trainers.txt | 否 |
| DefaultTrainerList | Pokemon | battle_tower_pokemon.txt | 否 |
| TrainerList | Trainers | cup_poke_trainers.txt | 否 |
| TrainerList | Pokemon | cup_poke_pkmn.txt | 否 |
| TrainerList | Trainers | cup_little_trainers.txt | 否 |
| TrainerList | Pokemon | cup_little_pkmn.txt | 否 |
| TrainerList | Trainers | cup_pika_trainers.txt | 否 |
| TrainerList | Pokemon | cup_pika_pkmn.txt | 否 |
| TrainerList | Trainers | cup_fancy_trainers_single.txt | 否 |
| TrainerList | Pokemon | cup_fancy_pkmn_single.txt | 否 |

| 集合 | 数量 | 内容 |
| --- | --- | --- |
| 被当前名单引用的文件 | 10 | 上表去重路径 |
| 目录存在的 battle_tower/cup 候选文件 | 12 | `P/` 顶层按前缀枚举 |
| 存在但未被当前名单引用的候选文件 | 2 | cup_fancy_pkmn.txt、cup_fancy_trainers.txt |

上表 10 个被引用路径逐一核对：均**不满足**普通发现的完全基名或基名+下划线匹配（如 `battle_tower_trainers.txt` 不以任何基名开头），不经普通发现进入编译，只经名单字段显式读取。未被当前名单引用的候选文件用途**未调查**；其他入口（专用读取路径全集、失败行为）归 WP04，不据本表断言全局无引用。

## 8. 用途与限制

- 本表供 WP02-R01 验收：词典与逐定义清单双向对应；所有集合计数可按第 2 节方式从本表复算。
- Settings 键名、路径与默认值是参考侧取证记录，**不是**未来框架的公开 API 或模块划分依据。
- 本表只覆盖固定快照中两个设置文件的显式定义；不排除插件、动态定义或其他配置体系存在更多入口（当前快照无 Plugins 内容，U09 开放）。
