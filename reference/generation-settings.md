# 机制世代与配置默认值

以下来自基于 v21.1、标签后 23 个提交的参考快照，默认机制世代为 8。各标识指原配置中的对应项目。作者可以逐项覆盖派生默认值。世代判断还可能直接用于个别规则。完整的例外、数值低世代分支和合并词典见[规则配置与数据变体](../spec/core/rule-configuration-and-data-variants.md)。

## 逐项默认值

| 配置 | 默认值的来源 | 世代 8 取值 | 用途 |
| --- | --- | --- | --- |
| GAME_VERSION | 独立 | "1.0.0" | 元信息 |
| MECHANICS_GENERATION | 独立 | 8 | 元信息 |
| MAX_MONEY | 独立 | 999_999 | 玩家资源 |
| MAX_COINS | 独立 | 99_999 | 玩家资源 |
| MAX_BATTLE_POINTS | 独立 | 9_999 | 玩家资源 |
| MAX_SOOT | 独立 | 9_999 | 玩家资源 |
| MAX_PLAYER_NAME_SIZE | 独立 | 10 | 玩家资源 |
| RIVAL_NAMES | 独立 | 数组（见词典） | 玩家资源 |
| TIME_SHADING | 独立 | true | 世界与野外 |
| ANIMATE_REFLECTIONS | 独立 | true | 世界与野外 |
| NEW_BERRY_PLANTS | 世代(≥4) | true | 世界与野外 |
| FISHING_AUTO_HOOK | 独立 | false | 世界与野外 |
| FISHING_BEGIN_COMMON_EVENT | 独立 | -1 | 世界与野外 |
| FISHING_END_COMMON_EVENT | 独立 | -1 | 世界与野外 |
| SAFARI_STEPS | 独立 | 600 | 世界与野外 |
| BUG_CONTEST_TIME | 独立 | 20 * 60（= 1200） | 世界与野外 |
| NO_SIGNPOSTS | 独立 | 数组（见词典） | 世界与野外 |
| POISON_IN_FIELD | 世代(≤4) | false | 世界与野外 |
| POISON_FAINT_IN_FIELD | 世代(≤3) | false | 世界与野外 |
| FIELD_MOVES_COUNT_BADGES | 独立 | true | 场地招式许可 |
| BADGE_FOR_CUT | 独立 | 1 | 场地招式许可 |
| BADGE_FOR_FLASH | 独立 | 2 | 场地招式许可 |
| BADGE_FOR_ROCKSMASH | 独立 | 3 | 场地招式许可 |
| BADGE_FOR_SURF | 独立 | 4 | 场地招式许可 |
| BADGE_FOR_FLY | 独立 | 5 | 场地招式许可 |
| BADGE_FOR_STRENGTH | 独立 | 6 | 场地招式许可 |
| BADGE_FOR_DIVE | 独立 | 7 | 场地招式许可 |
| BADGE_FOR_WATERFALL | 独立 | 8 | 场地招式许可 |
| MAXIMUM_LEVEL | 独立 | 100 | 个体与生成 |
| EGG_LEVEL | 独立 | 1 | 个体与生成 |
| SHINY_POKEMON_CHANCE | 世代(≥6) | 16 | 个体与生成 |
| SUPER_SHINY | 世代(≥8) | true | 个体与生成 |
| LEGENDARIES_HAVE_SOME_PERFECT_IVS | 世代(≥6) | true | 个体与生成 |
| POKERUS_CHANCE | 独立 | 3 | 个体与生成 |
| DISABLE_IVS_AND_EVS | 独立 | false | 个体与生成 |
| MOVE_RELEARNER_CAN_TEACH_MORE_MOVES | 世代(≥6) | true | 个体与生成 |
| DAY_CARE_POKEMON_GAIN_EXP_FROM_WALKING | 世代(≤6) | false | 寄养与繁殖 |
| DAY_CARE_POKEMON_CAN_SHARE_EGG_MOVES | 世代(≥8) | true | 寄养与繁殖 |
| BREEDING_CAN_INHERIT_MACHINE_MOVES | 世代(≤5) | false | 寄养与繁殖 |
| BREEDING_CAN_INHERIT_EGG_MOVES_FROM_MOTHER | 世代(≥6) | true | 寄养与繁殖 |
| ROAMING_AREAS | 独立 | 映射（见词典） | 漫游 |
| ROAMING_SPECIES | 独立 | 数组（见词典） | 漫游 |
| MAX_PARTY_SIZE | 独立 | 6 | 队伍与储存 |
| NUM_STORAGE_BOXES | 独立 | 40 | 队伍与储存 |
| HEAL_STORED_POKEMON | 世代(≤7) | false | 队伍与储存 |
| REBALANCED_HEALING_ITEM_AMOUNTS | 世代(≥7) | true | 道具效果 |
| NO_VITAMIN_EV_CAP | 世代(≥8) | true | 道具效果 |
| RAGE_CANDY_BAR_CURES_STATUS_PROBLEMS | 世代(≥7) | true | 道具效果 |
| FLUTES_CHANGE_WILD_ENCOUNTER_LEVELS | 世代(≥6) | true | 道具效果 |
| RARE_CANDY_USABLE_AT_MAX_LEVEL | 世代(≥8) | true | 道具效果 |
| USE_MULTIPLE_STAT_ITEMS_AT_ONCE | 世代(≥8) | true | 道具效果 |
| TAUGHT_MACHINES_KEEP_OLD_PP | 世代(==5) | false | 道具效果 |
| MORE_BONUS_PREMIER_BALLS | 世代(≥8) | true | 道具效果 |
| BAG_MAX_POCKET_SIZE | 独立 | 数组（见词典） | 背包 |
| BAG_POCKET_AUTO_SORT | 独立 | 数组（见词典） | 背包 |
| BAG_MAX_PER_SLOT | 独立 | 999 | 背包 |
| USE_CURRENT_REGION_DEX | 独立 | false | 图鉴 |
| DEX_SHOWS_ALL_FORMS | 独立 | false | 图鉴 |
| DEXES_WITH_OFFSETS | 独立 | 数组（见词典） | 图鉴 |
| SHOW_NEW_SPECIES_POKEDEX_ENTRY_MORE_OFTEN | 世代(≥7) | true | 图鉴 |
| REGION_MAP_EXTRAS | 独立 | 数组（见词典） | 城镇地图 |
| CAN_FLY_FROM_TOWN_MAP | 独立 | true | 城镇地图 |
| PHONE_REMATCHES_POSSIBLE_FROM_BEGINNING | 独立 | false | 电话 |
| COLOR_PHONE_CALL_MESSAGES_BY_CONTACT_GENDER | 独立 | true | 电话 |
| REPEL_COUNTS_FAINTED_POKEMON | 世代(≥6) | true | 遭遇与战斗开始 |
| MORE_ABILITIES_AFFECT_WILD_ENCOUNTERS | 世代(≥8) | true | 遭遇与战斗开始 |
| HIGHER_SHINY_CHANCES_WITH_NUMBER_BATTLED | 世代(≥8) | true | 遭遇与战斗开始 |
| OVERWORLD_WEATHER_SETS_BATTLE_TERRAIN | 世代(≥8) | true | 遭遇与战斗开始 |
| STARTING_OVER_SWITCH | 独立 | 1 | 游戏开关 ID |
| SEEN_POKERUS_SWITCH | 独立 | 2 | 游戏开关 ID |
| SHINY_WILD_POKEMON_SWITCH | 独立 | 31 | 游戏开关 ID |
| FATEFUL_ENCOUNTER_SWITCH | 独立 | 32 | 游戏开关 ID |
| DISABLE_BOX_LINK_SWITCH | 独立 | 35 | 游戏开关 ID |
| GRASS_ANIMATION_ID | 独立 | 1 | 动画 ID |
| DUST_ANIMATION_ID | 独立 | 2 | 动画 ID |
| EXCLAMATION_ANIMATION_ID | 独立 | 3 | 动画 ID |
| RUSTLE_NORMAL_ANIMATION_ID | 独立 | 1 | 动画 ID |
| RUSTLE_VIGOROUS_ANIMATION_ID | 独立 | 5 | 动画 ID |
| RUSTLE_SHINY_ANIMATION_ID | 独立 | 6 | 动画 ID |
| PLANT_SPARKLE_ANIMATION_ID | 独立 | 7 | 动画 ID |
| LANGUAGES | 独立 | 数组（见词典） | 语言 |
| SCREEN_WIDTH | 独立 | 512 | 屏幕 |
| SCREEN_HEIGHT | 独立 | 384 | 屏幕 |
| SCREEN_SCALE | 独立 | 1.0 | 屏幕 |
| SPEECH_WINDOWSKINS | 独立 | 数组（见词典） | 窗口皮肤 |
| MENU_WINDOWSKINS | 独立 | 数组（见词典） | 窗口皮肤 |
| PROMPT_TO_COMPILE | 独立 | false | 调试 |
| SKIP_CONTINUE_SCREEN | 独立 | false | 调试 |
| RECALCULATE_TURN_ORDER_AFTER_MEGA_EVOLUTION | 世代(≥7) | true | 回合顺序与服从 |
| RECALCULATE_TURN_ORDER_AFTER_SPEED_CHANGES | 世代(≥8) | true | 回合顺序与服从 |
| ANY_HIGH_LEVEL_POKEMON_CAN_DISOBEY | 独立 | false | 回合顺序与服从 |
| FOREIGN_HIGH_LEVEL_POKEMON_CAN_DISOBEY | 独立 | true | 回合顺序与服从 |
| NO_MEGA_EVOLUTION | 独立 | 34 | Mega 开关 |
| MOVE_CATEGORY_PER_MOVE | 世代(≥4) | true | 招式计算 |
| NEW_CRITICAL_HIT_RATE_MECHANICS | 世代(≥6) | true | 招式计算 |
| MORE_TYPE_EFFECTS | 世代(≥6) | true | 招式计算 |
| NUM_BADGES_BOOST_ATTACK | 世代(≥4) | 999 | 招式计算 |
| NUM_BADGES_BOOST_DEFENSE | 世代(≥4) | 999 | 招式计算 |
| NUM_BADGES_BOOST_SPATK | 世代(≥4) | 999 | 招式计算 |
| NUM_BADGES_BOOST_SPDEF | 世代(≥4) | 999 | 招式计算 |
| NUM_BADGES_BOOST_SPEED | 世代(≥4) | 999 | 招式计算 |
| FIXED_DURATION_WEATHER_FROM_ABILITY | 世代(≥6) | true | 特性与道具效果 |
| X_STAT_ITEMS_RAISE_BY_TWO_STAGES | 世代(≥7) | true | 特性与道具效果 |
| NEW_POKE_BALL_CATCH_RATES | 世代(≥7) | true | 特性与道具效果 |
| SOUL_DEW_POWERS_UP_TYPES | 世代(≥7) | true | 特性与道具效果 |
| AFFECTION_EFFECTS | 独立 | false | 亲密 |
| APPLY_HAPPINESS_SOFT_CAP | 设置间(=AFFECTION_EFFECTS) | false | 亲密 |
| ENABLE_CRITICAL_CAPTURES | 世代(≥5) | true | 捕获 |
| NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER | 世代(≥7) | true | 捕获 |
| SCALED_EXP_FORMULA | 世代(==5或≥7) | true | 经验与 EV |
| SPLIT_EXP_BETWEEN_GAINERS | 世代(≤5) | false | 经验与 EV |
| MORE_EXP_FROM_TRAINER_POKEMON | 世代(≤6) | false | 经验与 EV |
| MORE_EVS_FROM_POWER_ITEMS | 世代(≥7) | true | 经验与 EV |
| GAIN_EXP_FOR_CAPTURE | 世代(≥6) | true | 经验与 EV |
| NO_MONEY_LOSS | 独立 | 33 | 战后 |
| CHECK_EVOLUTION_AFTER_ALL_BATTLES | 世代(≥6) | true | 战后 |
| CHECK_EVOLUTION_FOR_FAINTED_POKEMON | 独立 | true | 战后 |
| SMARTER_WILD_LEGENDARY_POKEMON | 独立 | true | AI |

47 项默认值取决于机制世代，1 项跟随另一设置，70 项独立。其中 6 个世代派生数值项为异色阈值与五项徽章能力加成门槛。徽章场地许可的数量或指定编号模式由 FIELD_MOVES_COUNT_BADGES 决定，配套的八项许可值须按同一模式解释。

## 内容配置与版本

片尾作者名单（game_credits）、8 个口袋名称（bag_pocket_names）、区域图鉴名称（pokedex_names）由作者内容提供。前者汇合插件与引擎的署名。参考配置将三项元信息标为不可编辑，其完整字符串值为 `VERSION = "21.1"`、`ERROR_TEXT = ""`、`MKXPZ_VERSION = "2.4.2/c9378cf"`。

多语言且无档时，启动流程提供语言选择。读档页候选至少有两种语言时提供语言菜单。选择后加载对应文本资源。作者可另选导出目标语言，玩家语言与当前游戏文本仍保持原值。

## 设施名单的显式输入

当前默认训练家名单一节、具名训练家名单四节，各有训练家与个体两个输入字段。以下十个路径只经名单显式读取，普通顶层基名发现规则不会匹配它们。

| 节类别 | 字段 | 输入名 | 普通发现可匹配 |
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

同目录还存在 cup_fancy_pkmn.txt、cup_fancy_trainers.txt，本名单未引用，其余用途未验证。插件与动态配置的覆盖范围未穷尽。

## 静态检索口径

原记录中有 41 个文件出现直接世代引用，共 139 行，注释命中 0。一个文件可有多个判断，单个判断也可能多次引用。以下 16 项是非注释行级候选使用点数量，实际消费者和分支仍以相应规格为准。

GAIN_EXP_FOR_CAPTURE(2 行)、ENABLE_CRITICAL_CAPTURES(1)、NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER(2)、AFFECTION_EFFECTS(5)、APPLY_HAPPINESS_SOFT_CAP(12)、RECALCULATE_TURN_ORDER_AFTER_MEGA_EVOLUTION(1)、NO_MEGA_EVOLUTION(1)、CHECK_EVOLUTION_AFTER_ALL_BATTLES(1)、CHECK_EVOLUTION_FOR_FAINTED_POKEMON(1)、HEAL_STORED_POKEMON(8)、DISABLE_IVS_AND_EVS(2)、OVERWORLD_WEATHER_SETS_BATTLE_TERRAIN(1)、MORE_ABILITIES_AFFECT_WILD_ENCOUNTERS(7)、LEGENDARIES_HAVE_SOME_PERFECT_IVS(1)、HIGHER_SHINY_CHANCES_WITH_NUMBER_BATTLED(1)、MOVE_CATEGORY_PER_MOVE(4)。
