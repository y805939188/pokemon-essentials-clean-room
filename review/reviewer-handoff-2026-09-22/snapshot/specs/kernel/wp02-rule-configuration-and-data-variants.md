# WP02 规格：规则配置档案与数据变体

| 字段 | 内容 |
| --- | --- |
| 工作包 | WP02（规则配置与数据变体） |
| 关联功能 | F01-01（配置与机制选择，D01）、F02-03（备选数据与机制兼容，D02） |
| 分类 | Generic Kernel（配置机制）；F02-03 部分为 Pokémon Rules（备选内容）。**目录归类说明**：本文位于 `specs/kernel/` 只表示配置机制的主要分类，不表示全部条目属于通用 Kernel——内容同时跨 Pokémon 规则、宿主集成、UI 与作者配置；Settings 键名、路径与默认值是参考侧取证记录，不是未来框架的公开 API（C03） |
| 参考基线 | `reference/pokemon-essentials/` @ commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（WP01 固定） |
| 输入 | 证据包 E02、E04、E05；PBS 顶层与备份目录；[wp02-settings-inventory-appendix](wp02-settings-inventory-appendix.md)（逐定义清单与检索索引附表） |
| 前置依赖 | WP01（基线与材料缺口已固定，满足） |
| 规格状态 | **Reviewed（固定基线配置档案、声明默认/派生、候选材料与输入边界、静态场景范围）**：2026-09-19 经 WP02 复审与复检修订后，由 WP02 闭合复审（`review/wp02-closure-review-2026-09-19.md`）通过；领域语义、数据组合与 Demo 范围不在本状态内 |
| 证据等级 | 全部为静态证据：已定位 / 静态确认 / 数据样本确认；**无运行确认** |

## 1. 目的、范围与非目标

**目的**：建立可审计的规则配置档案——参考实现提供哪些影响行为的配置项、各自的默认值、哪些派生于机制世代、哪些需要作者手动选择，以及哪些配置/数据组合尚未验证。后续每个领域包引用本档案定位其规则受哪些配置影响，而不是各自重复搜索设置文件。

**范围**（WP02 自身声明范围，extraction-plan 第 2.1 节 (a) 类）：

1. WP02-A：配置体系总览（定义点、世代基准、直接世代引用）。
2. WP02-B：配置词典——两个设置文件全部定义的默认值、派生方式、行为语义、候选使用点与影响域。
3. WP02-C：派生关系分析（世代阈值分组、设置间派生、模式选择、可覆盖性）。
4. WP02-D：候选数据与手动选择（默认数据集、普通发现机制及其边界、备份目录、语言数据集）。
5. WP02-E：未验证组合表。
6. F01-01、F02-03 中属于 WP02 部分的状态更新。

**非目标**：

- 不提取各开关在具体规则中的完整语义（归相应领域包，如捕获开关归 WP38、成长开关归 WP30）。
- 不描述 PBS 字段 schema（WP03）或完整编译生命周期（WP04）。
- 不验证任何配置组合的实际运行结果；不把备份目录的存在当作变体已受支持的证明。
- 不比对官方版本的设置差异（U02 保持开放）。
- 不修改 `reference/`，不运行游戏或编译器。

## 2. 概念与术语

- **统计单位**（WP02-R01 修订后固定）：**独立常量**（Settings 命名空间单个常量定义）、**方法型配置**（`def self.*` 定义，调用形式 `Settings.<name>`）、**元信息**（Essentials 命名空间常量，不混入 Settings 统计）、**展示行**（本词典表格行，一行可合并多个常量）。逐定义清单见附表第 3–6 节，全部统计可按附表第 2 节方式复算。
- **独立设置 / 世代派生设置 / 设置间派生**：默认值表达式是否引用机制世代或另一设置。派生只发生在**默认值计算**层面；作者把某条派生设置改写字面量后，该条即脱离联动（设置文件注释明确允许逐条修改）。
- **直接世代引用**：消费者代码不经派生设置、直接引用世代值的位置。统计单位为**文件级命中**与**行级出现**，不等于独立分支数（附表第 7.2 节）。
- **候选文件命中 / 候选使用点 / 已核消费者**：按检索得到的文件数（含注释/字符串可能）、行级出现位置、经行内容确认的代码使用点，三者分层（附表第 7.1 节检索规则）。
- **候选变体材料**：快照中存在、但未被默认发现路径纳入的备选内容（本快照为 PBS 备份目录）。
- 影响域编号 Dxx 见 module-map；证据状态五档定义见总览第 7 节。

## 3. WP02-A：配置体系总览

| 事实 | 内容 | 证据强度 |
| --- | --- | --- |
| 设置定义点 | 固定快照中，`module Settings` 的显式定义仅见于 2 个文件：`S/001_Settings.rb`（524 行）、`S/002_BattleSettings.rb`（140 行）。限定：该结论覆盖固定快照与已搜索的声明形式，不排除插件、动态定义或其他配置体系（当前快照无 Plugins 内容，U09） | 静态确认（本轮全仓库搜索，限定形式） |
| 配置规模 | Settings 命名空间：**118 个常量**（001 文件 88 + 002 文件 30）+ **3 个方法型配置**（game_credits、bag_pocket_names、pokedex_names）；Essentials 命名空间 3 条元信息（VERSION、ERROR_TEXT、MKXPZ_VERSION）单列 | 静态确认（逐定义清单复算，附表第 2–6 节） |
| 世代基准 | `MECHANICS_GENERATION = 8`（`S/001_Settings.rb` 第 17 行）；注释声明各世代非精确复刻、仅第五世代及以后"较合理支持" | 数据样本确认 |
| 派生规模 | **世代派生 47 条**（001 文件 25 + 002 文件 22；含数值型 6 条）、**设置间派生 1 条**（APPLY_HAPPINESS_SOFT_CAP），其余 70 条常量独立 | 静态确认（附表第 2 节复算） |
| 直接世代引用 | **41 个文件**含 `Settings::MECHANICS_GENERATION` 引用（不含两个设置文件），**行级出现共 139 行**，注释命中 0。单位限定：不是"41 处分支"——同一文件可含多个判断（最多单文件 12 行），且含引用的路径可能同时受其他设置影响 | 静态确认（附表第 7.2 节） |
| 行为决定因素 | 设置文件确定**声明的默认值**；游戏当前全部行为还取决于消费者、数据、运行状态、游戏开关与玩家选项（如语言、捕获替换选项），不能只从设置文本推断 | 静态确认（原则性限定） |

## 4. WP02-B：配置词典

说明：

- 本节 4.1 共 75 个展示行（覆盖 001 文件 88 个常量与 3 个方法型配置）；4.2 共 26 个展示行（覆盖 002 文件 30 个常量，徽章加成 5 常量合并 1 行）。逐定义对照见附表第 3–5 节。
- "默认值"指**当前快照在机制世代 = 8 下的取值**；派生条目的取值随世代改变，标注阈值。
- "候选文件命中"为 `Settings::<NAME>` 检索的文件数（检索规则与行级分类见附表第 7 节）；注释/字符串可能未逐行排除，故不称"消费者数"。
- 语义为行为层面简述；完整规则归相应领域包。内容定义类（名单、文本、图形名）只登记存在与用途，不展开、不复制内容。

### 4.1 `S/001_Settings.rb`

**元信息与玩家资源**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| GAME_VERSION | "1.0.0" | 独立 | 游戏版本号（MAJOR.MINOR.PATCH 格式约束） | D03 | 3 |
| MECHANICS_GENERATION | 8 | 独立（基准） | 战斗与部分野外规则跟随的机制世代 | 全部 | 41（文件级） |
| game_credits（方法型） | 作者名单数组 | 独立（内容定义） | 片尾 credits 文本来源；插件与引擎 credits 自动附加。用途登记，内容不复制 | D16/D18 | 1（`Settings.game_credits`，dot 形式） |
| MAX_MONEY | 999,999 | 独立 | 玩家金钱上限 | D08 | 5 |
| MAX_COINS | 99,999 | 独立 | 游戏角代币上限 | D17 | 4 |
| MAX_BATTLE_POINTS | 9,999 | 独立 | 战斗点数（BP）上限 | D13/D08 | 3 |
| MAX_SOOT | 9,999 | 独立 | 火山灰上限 | D14 | 1 |
| MAX_PLAYER_NAME_SIZE | 10 | 独立 | 玩家名字符上限 | D07/D16 | 3 |
| RIVAL_NAMES | 3 条（训练家类型→游戏变量） | 独立（内容定义） | 指定类型的 NPC 训练家可按变量改名 | D07/D02 | 1 |

**世界与野外**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| TIME_SHADING | true | 独立 | 室外地图是否按时段调色 | D05/D14 | 3 |
| ANIMATE_REFLECTIONS | true | 独立 | 角色倒影是否波动 | D05 | 1 |
| NEW_BERRY_PLANTS | true | 世代 ≥ 4 | 树果生长按新（Gen 4 式）还是旧（Gen 3 式）机制 | D14 | 1 |
| FISHING_AUTO_HOOK | false | 独立 | 钓鱼自动上钩还是需要反应输入 | D14 | 1 |
| FISHING_BEGIN_COMMON_EVENT | -1 | 独立 | 开始钓鱼时运行的公共事件 ID（-1 = 无，播默认动画） | D14/D04 | 1 |
| FISHING_END_COMMON_EVENT | -1 | 独立 | 结束钓鱼时运行的公共事件 ID（-1 = 无） | D14/D04 | 1 |
| SAFARI_STEPS | 600 | 独立 | 狩猎区步数预算（0 = 不限） | D13 | 2 |
| BUG_CONTEST_TIME | 1200 秒 | 独立 | 捕虫大会时长（0 = 不限） | D13 | 2 |
| NO_SIGNPOSTS | [] | 独立（内容定义） | 跨指定地图对不显示地点路牌 | D05/D04 | 1 |
| POISON_IN_FIELD | false | 世代 ≤ 4 | 中毒个体在野外行走是否损失 HP | D14 | 1 |
| POISON_FAINT_IN_FIELD | false | 世代 ≤ 3 | 野外中毒是否可致死（false = 保留 1 HP） | D14 | 1 |

**场地招式许可**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| FIELD_MOVES_COUNT_BADGES | true | 独立 | 场地招式许可模式：true = 需要徽章**数量**达标；false = 需要**特定**徽章 | D14/D07 | 1 |
| BADGE_FOR_CUT / FLASH / ROCKSMASH / SURF / FLY / STRENGTH / DIVE / WATERFALL | 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 | 独立 | 各场地招式所需徽章数量或编号（含义随上一设置模式改变；徽章 0 为第一枚） | D14/D07 | 各 1 |

**个体与生成**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| MAXIMUM_LEVEL | 100 | 独立 | 个体等级上限 | D06/D09 | 1 |
| EGG_LEVEL | 1 | 独立 | 新孵化个体等级 | D09 | 3 |
| SHINY_POKEMON_CHANCE | 16 | 世代 ≥ 6 时 16，否则 8 | 异色判定的**基础阈值（以 65536 为尺度的分子参数）**，非概率分母；各生成入口、重试与修正（如雷达连锁修正式，路径见第 4.3 节）会改变最终发生概率，完整规则归领域包 | D06/D10 | 2 |
| SUPER_SHINY | true | 世代 ≥ 8 | 是否启用超级异色（不同动画） | D05/D06 | 1 |
| LEGENDARIES_HAVE_SOME_PERFECT_IVS | true | 世代 ≥ 6 | 带特定旗帜的物种生成时至少 3 项满个体值 | D06/D10 | 1 |
| POKERUS_CHANCE | 3 | 独立 | 病毒判定的**基础阈值（以 65536 为尺度的分子参数）**；当前所见使用点为野生与蛋两个入口（路径见第 4.3 节），最终规则归领域包 | D06/D14 | 2 |
| DISABLE_IVS_AND_EVS | false | 独立 | 计算能力时是否把 IV/EV 视为 0（数据仍保留） | D06/D12 | 1 |
| MOVE_RELEARNER_CAN_TEACH_MORE_MOVES | true | 世代 ≥ 6 | 招式回忆是否扩展到蛋招式与曾教学的 TR 招式 | D09/D16 | 1 |

**寄养与繁殖**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| DAY_CARE_POKEMON_GAIN_EXP_FROM_WALKING | false | 世代 ≤ 6 | 寄养个体是否随步数获得经验（寄养/培育屋差异） | D09 | 1 |
| DAY_CARE_POKEMON_CAN_SHARE_EGG_MOVES | true | 世代 ≥ 8 | 同物种寄养个体间是否互传蛋招式 | D09 | 1 |
| BREEDING_CAN_INHERIT_MACHINE_MOVES | false | 世代 ≤ 5 | 后代是否可从父亲继承机器招式（母亲永不） | D09 | 1 |
| BREEDING_CAN_INHERIT_EGG_MOVES_FROM_MOTHER | true | 世代 ≥ 6 | 后代是否可从母亲继承蛋招式（父亲总是可以） | D09 | 1 |

**漫游（内容定义）**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| ROAMING_AREAS | 10 个顶层地图键，每键 9 项邻接 | 独立（内容定义） | 漫游个体可活动的地图节点及相邻移动路径（节点数 10，每节点邻接数 9） | D10 | 1 |
| ROAMING_SPECIES | 4 条（物种/等级/开关/遭遇方式/BGM/专用区域） | 独立（内容定义） | 漫游个体定义及其触发开关与遭遇范围 | D10 | 2 |

**队伍与储存**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| MAX_PARTY_SIZE | 6 | 独立 | 队伍容量上限 | D07/D11/D13 | 11 |
| NUM_STORAGE_BOXES | 40 | 独立 | 储存盒子数量 | D07 | 2 |
| HEAL_STORED_POKEMON | false | 世代 ≤ 7 | 存入储存时是否自动治疗（false 时由治疗事件负责） | D07/D14 | 4 |

**道具与背包**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| REBALANCED_HEALING_ITEM_AMOUNTS | true | 世代 ≥ 7 | HP 治疗道具的治疗量按新旧哪套数值 | D08 | 3 |
| NO_VITAMIN_EV_CAP | true | 世代 ≥ 8 | 营养剂是否可无视为 100 的 EV 上限 | D08/D06 | 1 |
| RAGE_CANDY_BAR_CURES_STATUS_PROBLEMS | true | 世代 ≥ 7 | true 时该道具按**解除状态异常类效果**处理（Full Heal 类），false 时按 HP 伤药处理；不是 HP+状态双恢复的"全恢复"，完整效果归道具领域包 | D08 | 3 |
| FLUTES_CHANGE_WILD_ENCOUNTER_LEVELS | true | 世代 ≥ 6 | 黑/白笛改变野生等级（true）还是遭遇率（false） | D10/D08 | 2 |
| RARE_CANDY_USABLE_AT_MAX_LEVEL | true | 世代 ≥ 8 | 满级个体能否用神奇糖果触发等级进化 | D08/D09 | 1 |
| USE_MULTIPLE_STAT_ITEMS_AT_ONCE | true | 世代 ≥ 8 | 经验/EV 类道具是否可一次选数量批量使用 | D08/D16 | 1 |
| TAUGHT_MACHINES_KEEP_OLD_PP | false | 世代 == 5 | 机器教学替换招式时是否保留被替换招式的 PP | D08/D06 | 1 |
| MORE_BONUS_PREMIER_BALLS | true | 世代 ≥ 8 | 纪念球赠送按任意球 10 个（true）还是普通球 10+（false） | D08 | 1 |
| bag_pocket_names（方法型） | 8 个口袋名 | 独立（内容定义） | 背包口袋划分与命名（dot 形式调用） | D08/D16 | 3 |
| BAG_MAX_POCKET_SIZE | 全 -1（无限） | 独立 | 各口袋槽位上限（-1 = 不限） | D08 | 2 |
| BAG_POCKET_AUTO_SORT | 仅机器、树果两口袋 true | 独立 | 各口袋是否按 PBS 定义序自动排序 | D08/D16 | 2 |
| BAG_MAX_PER_SLOT | 999 | 独立 | 单槽物品数量上限 | D08 | 5 |

**图鉴、地图与电话**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| pokedex_names（方法型） | 2 个地区图鉴 + 全国图鉴 | 独立（内容定义） | 图鉴列表及对应区域地图编号（dot 形式调用） | D15 | 4 |
| USE_CURRENT_REGION_DEX | false | 独立 | 图鉴默认显示当前地区（true）还是手动选择（false） | D15/D16 | 5 |
| DEX_SHOWS_ALL_FORMS | false | 独立 | 见过物种即显示全部形态（true）还是逐形态解锁（false） | D15 | 1 |
| DEXES_WITH_OFFSETS | [] | 独立 | 哪些图鉴编号从 0 开始 | D15 | 3 |
| SHOW_NEW_SPECIES_POKEDEX_ENTRY_MORE_OFTEN | true | 世代 ≥ 7 | 新获得物种的图鉴页是否在孵化/进化/交换后也展示 | D15/D16 | 5 |
| REGION_MAP_EXTRAS | 2 条 | 独立（内容定义） | 区域地图上按开关显示的附加图形 | D15/D05 | 2 |
| CAN_FLY_FROM_TOWN_MAP | true | 独立 | 能否在城镇地图界面直接使用飞翔 | D14/D15 | 1 |
| PHONE_REMATCHES_POSSIBLE_FROM_BEGINNING | false | 独立 | 电话再战功能初始是否开放 | D15 | 1 |
| COLOR_PHONE_CALL_MESSAGES_BY_CONTACT_GENDER | true | 独立 | 电话文本是否按联系人性别着色（公共事件电话除外） | D15/D16 | 1 |

**遭遇与战斗开始**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| REPEL_COUNTS_FAINTED_POKEMON | true | 世代 ≥ 6 | 驱赶按队首个体等级（true）还是队首未濒死个体（false） | D10/D08 | 1 |
| MORE_ABILITIES_AFFECT_WILD_ENCOUNTERS | true | 世代 ≥ 8 | 是否有更多特性影响野外遭遇的种类与出现 | D10/D12 | 1 |
| HIGHER_SHINY_CHANCES_WITH_NUMBER_BATTLED | true | 世代 ≥ 8 | 同物种大量对战/捕获后异色率是否提高 | D10/D06 | 1 |
| OVERWORLD_WEATHER_SETS_BATTLE_TERRAIN | true | 世代 ≥ 8 | 野外天气是否设定战斗默认场地（风暴→电气、雾→薄雾） | D14/D12 | 1 |

**开关/动画/语言/屏幕/资源/调试**

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| STARTING_OVER_SWITCH | 1 | 独立 | 玩家全灭失败回程时置 ON 的游戏开关 | D14/D04 | 1 |
| SEEN_POKERUS_SWITCH | 2 | 独立 | 标记已在治疗点见过病毒提示的开关 | D14 | 1 |
| SHINY_WILD_POKEMON_SWITCH | 31 | 独立 | ON 时野生个体全部异色 | D06/D10 | 1 |
| FATEFUL_ENCOUNTER_SWITCH | 32 | 独立 | ON 时生成个体均视为命运邂逅 | D06/D10 | 1 |
| DISABLE_BOX_LINK_SWITCH | 35 | 独立 | ON 时禁用队伍界面直连储存的功能 | D07/D16 | 1 |
| GRASS / DUST / EXCLAMATION / RUSTLE_NORMAL / RUSTLE_VIGOROUS / RUSTLE_SHINY / PLANT_SPARKLE（动画 ID） | 1 / 2 / 3 / 1 / 5 / 6 / 7 | 独立（资源引用） | 野外各效果的动画资源 ID | D05/D14 | 各 1 |
| LANGUAGES | []（空） | 独立 | 作者提供的语言候选列表及数据文件名片段；空 = 不提供候选。作者配置与玩家选择的关系见第 6.3 节 | D02/D16 | 5（含 1 处注释命中，附表 7.3 节） |
| SCREEN_WIDTH / SCREEN_HEIGHT / SCREEN_SCALE | 512 / 384 / 1.0 | 独立 | 默认画面尺寸与缩放；注释要求与 `mkxp.json` 同步修改 | D05 | 8 / 8 / 1 |
| SPEECH_WINDOWSKINS / MENU_WINDOWSKINS | 21 / 28 个图形名 | 独立（资源引用） | 对话框/菜单框可选皮肤资源清单 | D05/D16 | 4 / 3 |
| PROMPT_TO_COMPILE | false | 独立 | 调试模式下启动时是否提示完整编译 | D18 | 1 |
| SKIP_CONTINUE_SCREEN | false | 独立 | 调试模式下是否跳过继续/新游戏画面 | D18/D16 | 1 |

### 4.2 `S/002_BattleSettings.rb`（30 个常量，26 个展示行）

| 设置 | 世代 8 默认值 | 派生 | 行为语义 | 影响域 | 候选文件命中 |
| --- | --- | --- | --- | --- | --- |
| RECALCULATE_TURN_ORDER_AFTER_MEGA_EVOLUTION | true | 世代 ≥ 7 | Mega 进化后是否重算回合行动顺序 | D11 | 1 |
| RECALCULATE_TURN_ORDER_AFTER_SPEED_CHANGES | true | 世代 ≥ 8 | 速度变化后是否重算行动顺序 | D11 | 3 |
| ANY_HIGH_LEVEL_POKEMON_CAN_DISOBEY | false | 独立 | 自有高等级个体是否也可不服从（按徽章数判定） | D11/D07 | 1 |
| FOREIGN_HIGH_LEVEL_POKEMON_CAN_DISOBEY | true | 独立 | 外来高等级个体是否可不服从 | D11/D07 | 1 |
| NO_MEGA_EVOLUTION | 34 | 独立 | ON 时禁止战斗中 Mega 进化的游戏开关 | D11/D06 | 1 |
| MOVE_CATEGORY_PER_MOVE | true | 世代 ≥ 4 | 物理/特殊分类按招式本身（true）还是按属性（false） | D12 | 2 |
| NEW_CRITICAL_HIT_RATE_MECHANICS | true | 世代 ≥ 6 | 会心按 1.5 倍 4 段（true）还是 2 倍 5 段（false）；并影响变身/自我暗示是否复制会心率 | D12 | 6 |
| MORE_TYPE_EFFECTS | true | 世代 ≥ 6 | 一组属性相关免疫/必中规则是否生效（电免麻痹、鬼免束缚、草免粉末、毒用剧毒必中） | D12 | 11 |
| NUM_BADGES_BOOST_ATTACK / DEFENSE / SPATK / SPDEF / SPEED（5 常量合并展示） | 全部 999 | 世代 ≥ 4 时 999，否则 1/5/7/7/3 | 徽章数为各能力提供 1.1 倍战斗加成的门槛；999 = 默认不触发 | D12/D07 | 各 1–2 |
| FIXED_DURATION_WEATHER_FROM_ABILITY | true | 世代 ≥ 6 | 特性引起的天气持续 5 回合（true）还是永久（false） | D12 | 1 |
| X_STAT_ITEMS_RAISE_BY_TWO_STAGES | true | 世代 ≥ 7 | 战斗道具（X 攻击等）提升 2 段（true）还是 1 段（false） | D12/D08 | 2 |
| NEW_POKE_BALL_CATCH_RATES | true | 世代 ≥ 7 | 部分球的捕获率修正按新（Gen 7+）还是旧数值 | D10/D12 | 1 |
| SOUL_DEW_POWERS_UP_TYPES | true | 世代 ≥ 7 | 心之水滴强化属性招式 20%（true）还是提升特攻/特防 50%（false） | D12/D08 | 2 |
| AFFECTION_EFFECTS | false | 独立 | 高亲密度是否在战斗中产生额外效果（经验加成、自愈、撑住等） | D09/D12 | 4 |
| APPLY_HAPPINESS_SOFT_CAP | false | **= AFFECTION_EFFECTS**（设置间派生） | 亲密度是否设 179 软上限（仅亲密果可突破）并把亲密进化门槛降至 160 | D09 | 3 |
| ENABLE_CRITICAL_CAPTURES | true | 世代 ≥ 5 | 是否启用会心捕获（注释：按 600+ 物种图鉴进度计算，物种不足时效果减弱） | D10 | 1 |
| NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER | true | 世代 ≥ 7 | 满队捕获时是否询问替换队员（true 时可在选项中开关询问） | D10/D07/D16 | 2 |
| SCALED_EXP_FORMULA | true | 世代 == 5 或 ≥ 7 | 击倒经验是否按获得方等级缩放 | D09/D11 | 1 |
| SPLIT_EXP_BETWEEN_GAINERS | false | 世代 ≤ 5 | 参战者平分经验（true）还是各得全额（false）；含学习装置分配 | D09/D11 | 1 |
| MORE_EXP_FROM_TRAINER_POKEMON | false | 世代 ≤ 6 | 击倒训练家个体经验是否 ×1.5 | D09/D11 | 1 |
| MORE_EVS_FROM_POWER_ITEMS | true | 世代 ≥ 7 | 力量道具提供 8 点（true）还是 4 点（false）对应 EV | D09/D08 | 1 |
| GAIN_EXP_FOR_CAPTURE | true | 世代 ≥ 6 | 捕获是否获得经验 | D09/D10/D11 | 2 |
| NO_MONEY_LOSS | 33 | 独立 | ON 时战败不扣钱（战胜仍可获奖金）的游戏开关 | D11/D08 | 1 |
| CHECK_EVOLUTION_AFTER_ALL_BATTLES | true | 世代 ≥ 6 | 战后进化检查在所有战斗后（true）还是仅胜利后（false）进行 | D09/D11 | 1 |
| CHECK_EVOLUTION_FOR_FAINTED_POKEMON | true | 独立 | 濒死个体是否也做战后进化检查 | D09/D11 | 1 |
| SMARTER_WILD_LEGENDARY_POKEMON | true | 独立 | 带特定旗帜的野生个体是否使用更高 AI 技能档（中档 32） | D12 | 1 |

### 4.3 重点候选使用点路径（词典引用用）

以下为关键开关的候选使用点路径（文件级命中；行级出现均非注释，见附表第 7.4 节）；领域包提取语义时从这些入口入手：

| 设置 | 候选使用点路径 |
| --- | --- |
| GAIN_EXP_FOR_CAPTURE | `S/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb`；`S/011_Battle/001_Battle/002_Battle_StartAndEnd.rb` |
| ENABLE_CRITICAL_CAPTURES | `S/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb` |
| NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER | `S/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb`；`S/016_UI/015_UI_Options.rb` |
| AFFECTION_EFFECTS | `S/011_Battle/003_Move/002_Move_Usage.rb`、`003_Move_UsageCalculations.rb`；`S/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb`、`011_Battle_EndOfRoundPhase.rb` |
| APPLY_HAPPINESS_SOFT_CAP | `S/010_Data/001_Hardcoded data/007_Evolution.rb`；`S/014_Pokemon/001_Pokemon.rb`；`S/011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb` |
| RECALCULATE_TURN_ORDER_AFTER_MEGA_EVOLUTION / NO_MEGA_EVOLUTION | `S/011_Battle/001_Battle/008_Battle_ActionOther.rb` |
| CHECK_EVOLUTION_AFTER_ALL_BATTLES / CHECK_EVOLUTION_FOR_FAINTED_POKEMON | `S/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb` |
| HEAL_STORED_POKEMON | `S/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb`；`S/003_Game processing/004_Interpreter_Commands.rb`；`S/011_Battle/007_Other battle code/004_Battle_Peers.rb`；`S/016_UI/017_UI_PokemonStorage.rb` |
| DISABLE_IVS_AND_EVS | `S/014_Pokemon/001_Pokemon.rb` |
| 服从性两个开关 | `S/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb` |
| OVERWORLD_WEATHER_SETS_BATTLE_TERRAIN | `S/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb` |
| MORE_ABILITIES_AFFECT_WILD_ENCOUNTERS / HIGHER_SHINY_CHANCES_WITH_NUMBER_BATTLED | `S/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb` |
| LEGENDARIES_HAVE_SOME_PERFECT_IVS | `S/012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb` |
| MOVE_CATEGORY_PER_MOVE | `S/010_Data/002_PBS data/005_Move.rb`；`S/011_Battle/003_Move/001_Battle_Move.rb` |
| SHINY_POKEMON_CHANCE / POKERUS_CHANCE | `S/014_Pokemon/001_Pokemon.rb`；`S/013_Items/005_Item_PokeRadar.rb`（异色修正例）；`S/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb`、`007_Overworld_DayCare.rb`（病毒入口） |

## 5. WP02-C：派生关系分析

1. **世代派生 47 条**，阈值分组（复算自附表逐定义清单）：≥4：7 条；≥5：1 条；≥6：11 条；≥7：9 条；≥8：10 条；≤3：1 条；≤4：1 条；≤5：2 条；≤6：2 条；≤7：1 条；==5：1 条；==5 或 ≥7：1 条。其中数值型 6 条（SHINY_POKEMON_CHANCE、NUM_BADGES_BOOST 五项），其余 41 条为布尔型。
2. **设置间派生 1 条**：APPLY_HAPPINESS_SOFT_CAP 默认跟随 AFFECTION_EFFECTS。注释说明关联理由（亲密效果在 179 以上生效）；作者可分离设置。
3. **模式选择 1 组**：FIELD_MOVES_COUNT_BADGES 决定 BADGE_FOR_* 八个设置的语义（徽章数量 vs 特定徽章），两组设置必须配套解读（场景例见第 9 节 S3）。
4. **派生仅是默认值**：派生设置在作者改写为字面量后脱离世代联动；世代基准本身独立。因此**声明的默认配置**由设置文件最终文本确定，不由世代数字单独决定；但具体行为仍需消费者、数据、状态和其他选项共同决定（见第 3 节末行限定）。
5. **直接世代引用不受派生覆盖**：41 个文件、139 行直接世代引用（单位见第 3 节）。即使作者把全部 47 条派生设置改为同一取值，这些直接引用仍按世代值变化。且含直接引用的行为路径可能同时受其他设置影响——"世代派生"不是该路径的唯一输入。
6. **组合状态**：本包只登记表达式与默认值；任何"世代 X 下行为如何"的组合结论待相应领域包与 WP78 核对，本包不宣称跨世代兼容（呼应 F02-03 的 Provisional 状态与 U03）。

## 6. WP02-D：候选数据与手动选择

### 6.1 普通 PBS 发现机制及其边界（作者输入/编译发现层面）

本轮阅读 `S/021_Compiler/001_Compiler.rb` 第 967–991 行确认普通发现函数的**确切范围**：

- 各数据类声明基名；函数在 `P/` 内枚举**顶层** `*.txt`（`Dir.glob("*.txt")`，**不递归子目录**）。
- 匹配规则：文件名基名与数据类基名**完全相等**，或以"基名 + 下划线"开头（如 `items_shadow_pkmn.txt` 按基名 `items` 匹配）。候选基名按**最长基名优先**排序后逐一匹配，先匹配成功即归属（影响多基名数据类的归属结果）。
- 编译调用顺序（同一文件第 993–1018 行，节选定位）：TownMap、Connection、Type、Ability、Move、Item、BerryPlant、Species、Forms、Metrics、Shadow、RegionalDex、Ribbon、Encounter、TrainerType、Trainer、TrainerLists、Metadata、MapMetadata、DungeonTileset、DungeonParameters、PhoneMessage，共 **22 项内容编译调用**（不含发现与改写两个准备调用）。**调用先后是调度顺序，不等于内容依赖关系，也不等于完整编译生命周期**（归 WP04）。

**边界与例外（WP02-R04 修订）**：

- 普通发现函数**不是**编译输入的唯一来源。设施名单编译流程读取 `P/battle_facility_lists.txt` 各节的 Trainers/Pokemon 字段，并**显式读取字段指定的其他输入文件**：当前名单共 1 个 DefaultTrainerList 与 4 个 TrainerList，去重后引用 10 个输入路径（battle_tower_* 2 个、cup_* 8 个，均存在于 `P/` 顶层）；逐一核对它们不满足普通发现的匹配规则，不经普通发现进入编译。另有 2 个候选文件存在于 `P/` 顶层但未被当前名单引用（cup_fancy_pkmn.txt、cup_fancy_trainers.txt，用途未调查）。引用集合与目录存在集合的区分及逐节清单见附表第 7.5 节；完整专用读取路径归 WP04 追踪。
- 不能据普通函数不递归子目录，就证明所有专用读取路径绝不访问子路径；也不能把它当成备份切换的完整性证明。
- 不匹配普通发现的文件**仍可能**经显式引用进入编译（如上例）；"不匹配即不进入"的概括已撤回。

### 6.2 候选变体材料登记（存在性证据，非支持结论）

| 候选材料 | 内容 | 与默认发现路径的关系 | 状态 |
| --- | --- | --- | --- |
| `P/Gen 5 backup/` 至 `P/Gen 8 backup/` | 各 9 个文本：abilities、berry_plants、encounters、items、moves、pokemon、pokemon_forms、pokemon_metrics、types | 文件名与默认顶层数据同名；位于子目录，普通发现路径不扫描 | **已定位**。内容完整性、与世代开关的组合兼容性待验证（U03） |
| `P/Shadow Pokémon backup/` | 4 个文本：items_shadow_pkmn、moves_shadow_pkmn、shadow_pokemon、types_shadow_pkmn | 命名符合"基名 + 后缀"的普通发现模式，但位于子目录、默认不扫描；另有 shadow_pokemon.txt 对应独立 Shadow 数据类 | **已定位**。启用条件与完整生命周期待验证（U06，归 WP23/WP04） |

- 固定快照、已搜索形式下，**未发现**脚本对备份目录的引用（唯一 backup 相关命中是存档备份，无关），也**未发现**自动切换数据集的机制。该结论不扩展为"全局绝无引用"或"唯一启用办法已证"。
- 作者若要用备选内容，可能涉及把文件放入 `P/` 顶层等手动操作；其效果（编译结果、引用完整性）**未验证**。
- 本包不据目录存在、文件命名或开关存在宣称任何变体"已受支持"（延续 WP01-R03）。

### 6.3 语言数据：作者配置与玩家选择

- **作者配置**：LANGUAGES 定义语言候选列表（每条 = 显示名 + 数据文件名片段，对应 `Data/messages_片段_core/game.dat`）；默认为空（不提供候选）。
- **玩家选择**（本轮核实的消费入口，行号见附表第 7.3 节）：启动流程在候选 ≥ 2 且无存档时提供语言选择；载入界面在候选 ≥ 2 时显示语言菜单；选择保存在玩家系统选项中，文本资源按所选片段加载。调试菜单另有语言切换。
- **边界**：完整本地化与 UI 流程归 WP08/WP65；`S/016_UI/015_UI_Options.rb` 的 LANGUAGES 命中为注释性引用，不计为使用点。
- **内容定义类设置**（RIVAL_NAMES、ROAMING_AREAS/SPECIES、REGION_MAP_EXTRAS、pokedex_names、bag_pocket_names、窗口皮肤清单、NO_SIGNPOSTS、DEXES_WITH_OFFSETS）：介于配置与内容之间，属于作者内容而非机制变体；语义归相应领域包。

## 7. WP02-E：未验证组合表

| 组合 | 已知事实 | 待验证内容 | 处置责任 |
| --- | --- | --- | --- |
| 世代基准 × 备选数据集 | 默认世代 8 + 顶层数据集；备份目录不被普通发现扫描 | 改用备份数据后的编译结果与引用完整性；世代与数据集的匹配边界（U03） | WP04、WP79 |
| 世代基准 × 逐条覆盖 | 派生可被逐条改写；41 文件直接引用仍在 | 任意覆盖组合的行为一致性；官方各世代预期（U02） | 领域包、WP78 |
| AFFECTION_EFFECTS × APPLY_HAPPINESS_SOFT_CAP | 默认联动（均 false） | 分离设置后的亲密度/进化/战斗效果行为 | WP30（亲密度与软上限语义）、WP31（进化门槛）、WP42（战斗中亲密效果时序） |
| FIELD_MOVES_COUNT_BADGES × BADGE_FOR_* | 模式联动 | 两种模式各自的许可判定细节 | WP59 |
| 配置 × 插件 | 无插件实例（U09） | 插件对设置与数据的影响 | WP05 |
| Shadow 数据 × 捕获/成长/净化 | 候选材料存在；核心脚本存在（E25） | 启用条件与完整生命周期（U06） | WP23、WP04、WP38 |

## 8. 边界、失败与未知

- 设置取值**无校验证据**：未发现在加载时对非法取值（如负数容量、超范围概率）做检查的逻辑；非法取值的后果**未知**，不推测。
- `SCREEN_WIDTH/HEIGHT` 与 `mkxp.json` 需人工保持一致（注释级要求）；不一致行为未验证。
- `PROMPT_TO_COMPILE`、`SKIP_CONTINUE_SCREEN` 仅调试模式生效。
- 开关/动画 ID 类设置与游戏内资源/开关编号绑定；编号冲突的后果未验证。
- 普通发现函数对**同名冲突、空 PBS、缺失基名文件**的行为未在本包穷尽（归 WP04）。

## 9. 静态预期场景（WP02-R06：推导所得，全部待运行验证）

以下场景由设置文件文本与普通发现函数文本**静态推导**，均未运行；不展开其他工作包的完整规则。

**S1 世代派生默认值随世代变化**（视为按该世代重新求默认值；不暗示运行中动态切换世代会自动更新常量）：

| 设置 | 世代 5 推导默认 | 世代 6 推导默认 | 世代 8 推导默认 |
| --- | --- | --- | --- |
| SHINY_POKEMON_CHANCE | 8 | 16 | 16 |
| HEAL_STORED_POKEMON | true | true | false |
| SCALED_EXP_FORMULA | true | false | true |
| TAUGHT_MACHINES_KEEP_OLD_PP | true | false | false |
| ENABLE_CRITICAL_CAPTURES | true | true | true |
| POISON_IN_FIELD | false | false | false |

**S2 亲密联动与分离（声明值，不预断进化/战斗结果）**：

| 情形 | AFFECTION_EFFECTS | APPLY_HAPPINESS_SOFT_CAP | 推导声明 |
| --- | --- | --- | --- |
| 默认（联动） | false | false（跟随前者） | 不设软上限；无亲密战斗效果 |
| 作者显式分离 | true | false（作者改写） | 有亲密战斗效果；不设软上限 |

**S3 场地招式许可两种模式（同一数值参数的不同含义；许可判定逻辑归 WP59）**：

| FIELD_MOVES_COUNT_BADGES | BADGE_FOR_SURF = 4 的含义 |
| --- | --- |
| true（默认） | 需要徽章**数量** ≥ 4 |
| false | 需要**第 4 号**徽章（徽章 0 为第一枚，即第五枚） |

**S4 PBS 输入边界（普通发现 vs 显式引用）**：

| 输入 | 推导结果 | 依据 |
| --- | --- | --- |
| `P/moves.txt`（顶层） | 按基名 `moves` 匹配，进入编译 | 完全基名匹配 |
| `P/moves_shadow_pkmn.txt`（顶层，假设放入） | 按基名 `moves` + 后缀匹配，进入编译 | 基名+下划线规则 |
| `P/Gen 8 backup/moves.txt` | 不被扫描 | 普通发现不递归子目录 |
| `P/battle_tower_trainers.txt`（顶层） | **不被普通发现匹配**（不满足任何基名规则），但经 `battle_facility_lists.txt` 的 Trainers 字段显式读取 | 附表第 7.5 节实测 |

**S5 语言候选与选择入口（运行画面未验证）**：

| LANGUAGES | 推导的选择入口 |
| --- | --- |
| []（默认） | 启动无语言选择；载入界面无语言菜单 |
| ≥ 2 条且无存档 | 启动时出现语言选择 |
| ≥ 2 条 | 载入界面出现语言菜单 |

## 10. 证据与来源（traceability）

- **本轮复核（2026-09-19）**：逐行阅读两个设置文件全文（E02 范围）；逐定义清单解析与独立复算（附表全部统计）；全仓库 Settings 定义点搜索；消费者检索与行级分类（附表第 7 节）；普通发现函数与设施名单编译入口阅读（`001_Compiler.rb` 第 967–1018 行、`002_Compiler_CompilePBS.rb` `compile_trainer_lists`）；`P/battle_facility_lists.txt` 全文；LANGUAGES 全部使用点行级核实；game_credits 使用点核实。
- **继承同基线既有记录**：E02 对亲密/捕获经验/进化资格/Mega 顺序/服从性消费者的既有静态确认（与本轮抽查一致）；E04 的数据类基名声明；E05 的编译写回入口登记。
- **外部有限抽查**：2026-09-19 联合 review 对两个设置文件部分范围的抽查（独立开关与世代派生需分别记录的结论与本包一致）。
- 全部静态证据；**无运行确认**。

## 11. 未决问题

1. U02（官方版本差异）、U03（世代 × 数据集组合）、U06（Shadow 启用）、U09（插件组合）保持开放，本包登记事实不构成解决。
2. 各开关在领域规则中的完整语义（捕获率修正式、经验公式、服从性判定等）归相应领域包；本包词典只定位入口。
3. 非法取值的后果未知（第 8 节），如有需要由 WP79 登记。
4. 设施名单等专用读取路径的全集归 WP04；本包只登记了当前样本涉及的一组。

## 12. 状态与后续

- WP02 自身范围（第 1 节六项）已提取并自检；2026-09-19 经 WP02 复审后完成 WP02-R01（逐定义清单与统计单位）、WP02-R02（数值语义）、WP02-R03（命中与消费者分层）、WP02-R04（普通发现边界与显式输入例外）、WP02-R05（语言层次与任务引用）、WP02-R06（静态预期场景）六项修订后送审，复检后又完成 F1/F2/C1 修订。（本行是当时送审记录；最新状态：经 2026-09-19 WP02 闭合复审通过，头部规格状态为 **Reviewed**（固定基线配置档案、声明默认/派生、候选材料与输入边界、静态场景范围），以头部为准。）
- **WP02 完成 ≠ F01-01/F02-03 完成**：F01-01 的配置语义需领域包闭合，F02-03 的变体兼容性验证需 WP04/WP79；Feature Matrix 按聚合规则分别显示。
- 后续包引用本词典时，应以设置文件最终文本确定**声明的默认配置**（具体行为仍需消费者、数据、状态和其他选项），并区分默认值、派生表达式与直接世代引用；Settings 键名与路径是取证记录，不是未来框架的 API 约定。
