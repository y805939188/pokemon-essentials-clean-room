# WP03 规格：内容身份、注册与 schema

| 字段 | 内容 |
| --- | --- |
| 工作包 | WP03（内容身份、注册和 schema） |
| 关联功能 | F01-02（内容身份与注册查找，D01）、F02-01（内容目录与字段约束，D02） |
| 分类 | Generic Kernel（身份/注册/schema 机制）；内容本身多为 Pokémon 数据，键名与路径是参考侧取证记录，不是未来框架的 ID 类型或 API 设计 |
| 参考基线 | `reference/pokemon-essentials/` @ commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（WP01 固定） |
| 输入 | 证据包 E04（重点 GameData、Species、Item、Move、MapMetadata）；E05（编译期校验） |
| 前置依赖 | WP01（已 Reviewed）；WP02 提供配置背景（非完成依赖） |
| 规格状态 | **ReviewPending（WP03 自身范围）**：2026-09-19 提交外部 review |
| 证据等级 | 全部为静态证据：已定位 / 静态确认 / 数据样本确认；**无运行确认** |

## 1. 目的、范围与非目标

**目的**：建立跨域统一的内容引用概念——各类内容（物种、招式、道具、地图等）以什么身份被注册、查找、枚举和引用；未知或重复身份如何处理；固定规则与作者数据如何区分；每类内容的字段语义由哪个后续工作包负责。后续领域包引用本文的概念，不再各自发明"内容如何标识"的解释。

**范围**（WP03 自身声明范围，extraction-plan 第 2.1 节 (a) 类）：

1. WP03-A：内容身份模型（三类身份、查找语义、完整类清单）。
2. WP03-B：注册、查找与缺失值处理（加载、默认值、缺失文件）。
3. WP03-C：schema 与作者内容校验（字段约束结构、编译期错误）。
4. WP03-D：固定规则与作者数据的区分。
5. WP03-E：字段责任目录（内容类 → 领域包指派）。
6. F01-02、F02-01 中属于 WP03 部分的状态更新。

**非目标**：

- 不提取各类内容的字段语义全集（归 WP03-E 指派的领域包，如物种字段归 WP18–WP21）。
- 不展开完整编译生命周期、写回与失败分支（WP04）；不描述编辑器行为（WP73）。
- 不设计未来框架的 ID 类型、注册 API 或类层级（F01-02 明确"不预设未来 ID 类型"）。
- 不提取资源文件命名与回退规则（物种图像/声音归 WP15）。
- 不修改 `reference/`，不运行游戏或编译器。

## 2. 概念与术语

- **内容身份**：一个内容条目在注册表中的唯一键。本参考实现存在三类：符号身份（:BULBASAUR 式）、整数身份（地图 ID 式）、符号+整数双身份。
- **复合身份**：由基础身份与序号合成的身份（物种 + 形态，如 `SPECIES_1`）。
- **注册表**：每类内容一个内存数据表，启动时从编译产物载入；提供存在性检查、查找、枚举。
- **schema**：每类作者内容声明的字段约束——PBS 属性名到字段、类型模式与枚举引用的映射。
- **固定规则数据（hardcoded）**：在脚本中直接注册、不经 PBS 编译的内容（类型、能力值、成长曲线、进化方式等），可作作者内容的枚举引用源。
- **作者数据（PBS data）**：由作者在文本中定义、经编译产物载入的内容。
- **必选/可选数据文件**：缺失时是否强制重编译/容忍不加载（可选仅一例）。
- 影响域编号 Dxx 见 module-map；证据状态五档定义见总览第 7 节。

## 3. WP03-A：内容身份模型

### 3.1 三类身份与统一查找语义

全部内容类共用同一注册表模式（`S/010_Data/001_GameData.rb`，本轮逐行阅读确认），按身份形式分三类：

| 身份类 | 键形式 | 接受的查找输入 | 未知身份行为 | 枚举顺序 |
| --- | --- | --- | --- | --- |
| 符号身份 | 符号 | 符号 / 条目实例 / 字符串（字符串转符号后匹配） | `get` 抛出"Unknown ID"异常；`try_get` 返回 nil；`exists?` 返回 false（nil 输入亦为 false） | 定义顺序；另有按显示名字母序的枚举 |
| 整数身份 | 整数 | 条目实例 / 整数 | 同上（字符串/符号不可用于查找） | 数值顺序 |
| 双身份（符号+整数） | 同一条目同时以符号和整数为键（计数为条目数的两倍键） | 符号 / 条目实例 / 字符串 / 整数 | 同上 | 按整数序号顺序 |

- 相等判定：条目与符号/字符串按符号身份比较，与整数按整数序号比较，与同类实例按身份比较（`InstanceMethods`，`001_GameData.rb` 第 217–243 行）。
- 反向读取：`get_property_for_PBS` 按 schema 取字段值；false 与空数组归一化为 nil（用于 PBS 反写时省略默认值）。

### 3.2 完整内容类清单（本轮逐一核对声明）

**作者数据类（PBS 编译，含 DATA_FILENAME）**：符号身份 14 类——Type、Ability、Move、Item、BerryPlant、Species、SpeciesMetrics、ShadowPokemon、Ribbon、Encounter、TrainerType、Trainer、DungeonParameters、PhoneMessage；整数身份 5 类——TownMap、Metadata、PlayerMetadata、MapMetadata、DungeonTileset；另有 Species 声明双 PBS 基名（pokemon + pokemon_forms，注册表展开为 :Species 与 :Species1 两个编译键）。

**固定规则数据类（脚本内注册，无 DATA_FILENAME，load/save 为空操作）**：符号身份 15 类——GrowthRate、GenderRatio、EggGroup、BodyShape、BodyColor、Habitat、Evolution、Stat、Nature、Status、EncounterType、Environment、BattleWeather、BattleTerrain、Target；双身份 2 类——TerrainTag、Weather。

**非 GameData 注册表的编译产物**（`002_PBS data/001_MiscPBSData.rb`）：regional_dexes、map_connections、trainer_lists、战斗动画数据与 map_infos，经独立缓存加载；编译新鲜度检查中与 GameData 数据文件一并列为必选（见 4.2）。

**复合身份（物种 + 形态）**：形态条目以"物种符号_形态号"合成符号注册（如 `SPECIES_1`）；查找时先合成该符号，不存在则回退基础物种符号，仍不存在返回 nil；nil 输入直接返回 nil（`008_Species.rb` 第 154–163 行）。

**来源标记**：每个条目携带 `pbs_file_suffix`（其来源文件相对基名的后缀），多文件内容可追溯到具体输入文件。

## 4. WP03-B：注册、查找与缺失值处理

### 4.1 注册与加载

- 注册：条目按身份键写入本类数据表（双身份同时写两个键）。固定规则类在脚本加载时逐条注册（如 GrowthRate 的 6 条注册调用，第 77–173 行）。
- 加载：启动时统一从 `Data/*.dat` 载入全部作者数据（`GameData.load_all`，仅处理声明 DATA_FILENAME 的类）；加载本身是宿主提供的序列化读取（RGSS 内建），失败行为未验证。
- 新鲜度检查：编译器比对各数据文件与 PBS 的修改时间，决定是否重编译（`001_Compiler.rb` 第 1040–1076 行，详见 WP04）。

### 4.2 缺失数据文件

| 情形 | 行为 | 证据 |
| --- | --- | --- |
| 必选数据文件缺失 | 新鲜度检查判定必须重编译 | `001_Compiler.rb` 第 1063–1075 行（含 regional_dexes、map_connections、trainer_lists 三个非类文件） |
| 可选数据文件缺失（仅 ShadowPokemon，`OPTIONAL = true`） | 不强制重编译；加载时先检查文件存在，不存在则不加载（容忍缺席，本类数据为空） | `011_ShadowPokemon.rb` 第 14、27–30 行；`001_Compiler.rb` 第 1072–1074 行 |
| 可选类的 PBS 输入全部缺失 | 编译时直接跳过该类 | `002_Compiler_CompilePBS.rb` 第 4–6 行 |

可选数据缺席后，其消费者（Shadow 相关流程）如何行为未逐点核实（U06，归 WP23）。

### 4.3 字段缺失值（默认值）

条目构造时对缺失字段赋类级默认值，例如（本轮阅读确认）：物种未命名显示名 → "Unnamed"、类型 → [:NORMAL]、捕获率 → 255、亲密度 → 70、身高/体重 → 1；道具卖价 → 买价的一半、BP 价 → 1、口袋 → 1；招式类型 → :NONE、命中 → 100、PP → 5、效果率 → 0；地图元数据标志 → 空表。默认值是**当前快照的类级声明**，不是 Pokémon 通用规则；完整字段语义归领域包。

## 5. WP03-C：schema 与作者内容校验

### 5.1 schema 结构

每个作者数据类声明 schema：PBS 属性名 → [目标字段, 类型模式, 枚举引用]。多数类为常量表；Species 为方法（基础物种与形态使用不同属性集，如形态可有 Mega 相关属性，基础物种有性别/成长属性）。

观察到的类型模式（行为描述，非完整定义；解析细节归 WP04）：

| 模式 | 含义（行为层） |
| --- | --- |
| `m` | 节名（必填身份） |
| `s` / `q` | 文本（q 类可含转义文本，如图鉴描述） |
| `u` / `v` / `i` / `f` | 数值（无符号/有符号/整数/浮点；v 见用于枚举序数） |
| `b` | 布尔 |
| `e` | 单个枚举值，引用固定规则类（如 :Type、:Move、:Item、:Weather）或内联枚举表（如道具 FieldUse 的名值映射、招式 Category 的字符串数组） |
| `*` 前缀 | 列表（如 `*e` 枚举列表、`*s` 文本列表） |
| `^` | 可重复属性（同一属性多行累加，如 Evolution） |
| 复合 | 固定长度元组（如 `vvvvvv` 六项能力、`vuu` 坐标） |

### 5.2 编译期身份与引用校验（E05，本轮核实）

| 校验 | 行为 | 位置 |
| --- | --- | --- |
| 重复节名 | 编译错误："Section name 'X' is used twice."，附文件/行位置报告 | `002_Compiler_CompilePBS.rb`（通用编译函数，去重检查） |
| 未定义枚举引用 | 编译错误："Undefined item/species/move/trainer type constant name: X."，附文件/行位置报告（枚举在写入 PBS 时也可自动补写新常量） | `001_Compiler.rb` 第 867–941 行 |
| 必需参数缺失 | 编译错误（如进化方式需要参数而未给） | `002_Compiler_CompilePBS.rb` 第 313–319 行 |
| 内容特定重复 | 地区图鉴重复物种、同种升级招式重复等逐项检查 | 同文件第 618、885 行附近 |
| 校验时机 | 每条目级校验（编译该节时）+ 全量终检（全部读入后） | `compile_pokemon` 等（第 283–286 行） |

## 6. WP03-D：固定规则与作者数据的区分

| 维度 | 固定规则数据 | 作者数据 |
| --- | --- | --- |
| 定义位置 | 脚本内注册（17 类） | PBS 文本编译（19 类 + 5 个非类产物） |
| 加载 | 无 .dat；load/save 为空操作 | 从 `Data/*.dat` 载入 |
| 角色 | 作者内容的枚举引用源与规则参数（类型、能力值、成长曲线、进化方式、地形、天气、目标、环境等） | 游戏实际内容（物种、招式、道具、地图、训练家等） |
| 可否含行为 | **可以**（如 GrowthRate 的经验公式、Evolution 的方式判定、Stat 的 PBS 顺序），不只是枚举 | 字段语义按类归领域包 |
| 修改方式 | 改脚本（开发者） | 改 PBS（作者/编辑器） |

区分意义：判断"某行为由什么决定"时，枚举型固定规则（如类型列表）与含行为的固定规则（如成长曲线公式）必须分别对待；后者是规则本体的一部分，不能当作纯数据目录。这也回应 WP03 关键问题之二——固定规则与作者数据不能混为一谈。

## 7. WP03-E：字段责任目录

每类内容的字段语义由以下后续工作包负责（指派依据：module-map 的领域职责与 extraction-plan 的包范围；本表只指派责任，不展开语义）：

| 内容类（身份类） | 责任工作包 |
| --- | --- |
| Type（符号） | WP19（属性与个体）、WP43（属性相克计算） |
| Ability（符号） | WP48（计算修正）、WP49（阶段触发） |
| Move（符号） | WP43–WP47（计算与效果族）、WP30（学习/替换）、WP16（表现引用 WP16 边界） |
| Item（符号） | WP27（背包/储存）、WP28（使用资格/消耗）、WP29（买卖）、WP50（持有触发） |
| BerryPlant（符号） | WP60（树果种植） |
| Species（符号，双基名） | WP18（物种与个体）、WP19（数值）、WP20（状态/招式槽）、WP21（形态）、WP30–WP35（成长/进化/繁殖）、WP62（图鉴引用） |
| SpeciesMetrics（符号） | WP15（资源匹配）、WP16（世界绘制） |
| ShadowPokemon（符号，可选） | WP23（Shadow 生命周期）、WP38（抢夺引用）、WP40（呼唤时机） |
| Ribbon（符号） | WP21（展示属性）、WP67-B（演出） |
| Encounter（符号） | WP36（遭遇选择）、WP37（漫游/雷达引用） |
| TrainerType（符号） | WP24（训练家内容）、WP15（资源） |
| Trainer（符号） | WP24（NPC 队伍）、WP63（电话再战） |
| DungeonParameters（符号） | WP14（随机地牢） |
| PhoneMessage（符号） | WP63（电话） |
| TownMap（整数） | WP15（资源）、WP63（地图工具） |
| Metadata（整数） | WP09（启动/全局元数据）、WP24（玩家元数据引用） |
| PlayerMetadata（整数） | WP24（玩家角色）、WP15（资源） |
| MapMetadata（整数） | WP11（地图拓扑）、WP12（地形/运动）、WP36（遭遇环境）、WP59（天气/场地）、WP14（地牢标志） |
| DungeonTileset（整数） | WP14（随机地牢）、WP15（资源） |
| 固定规则 17 类 | GrowthRate→WP30；GenderRatio/EggGroup→WP18/WP34；BodyShape/BodyColor/Habitat→WP18/WP15；Evolution→WP31/WP32；Stat/Nature→WP19；Status→WP20/WP44；TerrainTag→WP12/WP36；Weather→WP59/WP45；EncounterType→WP36；Environment/BattleWeather/BattleTerrain→WP45；Target→WP43 |
| 非类产物（regional_dexes、map_connections、trainer_lists、战斗动画、map_infos） | WP62（图鉴）、WP11（地图连接）、WP54/WP55（设施名单）、WP16/WP67-A（战斗表现）、WP11（地图信息） |

## 8. 默认行为与配置变体

- **基线默认**：全部作者数据按第 3.2 节清单编译载入；ShadowPokemon 为唯一可选类（当前无顶层 shadow_pokemon.txt，见 WP02 第 6.2 节，其数据缺席）。
- **支持但未默认启用**：Shadow 备选数据（候选材料，启用条件与完整生命周期待证，U06/WP23/WP04）。
- **未验证组合**：可选数据缺席时各消费者的行为（4.2 节）；多文件后缀内容的归属组合（4.1 节来源标记）。
- 参考快照行为、官方版本预期、未来目标分开标记；本包只记录第一类。

## 9. 边界、失败与未知

- 运行时 `get` 遇到未知身份抛出异常；**异常的最终用户呈现**（错误对话框/崩溃）未运行验证。
- `try_get`/`exists?` 对 nil 与未知输入安全返回 nil/false；字符串查找经符号化转换，大小写敏感性与符号一致性未逐类验证。
- 双身份类以整数或符号查找同一条目等价；`count` 为键数一半（条目数）。
- 可选数据缺席时 Shadow 消费者的容错（U06）未逐点核实。
- schema 类型模式的完整解析规则（错误输入的拒绝行为）归 WP04；本包只登记结构与校验锚点。
- 固定规则类的行为内容（成长公式、进化判定）只登记存在与责任归属，不提取规则（WP30/WP31/WP32）。

## 10. 可复核性与静态场景

### 10.1 复核方式

| 事实 | 复核方式 |
| --- | --- |
| 三类身份的查找语义 | 阅读 `S/010_Data/001_GameData.rb` 三个混入模块 |
| 各类身份/文件声明 | 在 `S/010_Data/` 检索 `extend ClassMethods`、`DATA_FILENAME`、`PBS_BASE_FILENAME`、`OPTIONAL` |
| 重复节名编译错误 | 阅读 `S/021_Compiler/002_Compiler_CompilePBS.rb` 通用编译函数的去重检查 |
| 未定义引用编译错误 | 阅读 `S/021_Compiler/001_Compiler.rb` 第 867–941 行 |
| 可选类的容忍缺席 | 阅读 `011_ShadowPokemon.rb` 第 14、27–30 行与 `001_Compiler.rb` 第 1063–1075 行 |
| 复合身份查找 | 阅读 `008_Species.rb` 第 154–163 行 |

### 10.2 静态推导场景（未运行，待运行验证）

| 场景 | 输入 | 推导预期 |
| --- | --- | --- |
| 符号查找 | `Item.get(:POKEBALL)`（已注册） | 返回该条目；`Item.exists?("POKEBALL")` 为 true |
| 未知符号 | `Item.get(:NOTHING)`（未注册） | 抛出 Unknown ID 异常；`try_get` 为 nil；`exists?` 为 false |
| nil 输入 | `Item.exists?(nil)`、`Item.try_get(nil)` | false、nil |
| 重复节名 | PBS 中两节同名 `[POKEBALL]` | 编译错误"used twice"并报告位置 |
| 未定义引用 | 道具 `Move = SOMEMOVE`（未定义） | 编译错误"Undefined move constant name"并报告位置 |
| 复合身份 | `Species.get_species_form(:BULBASAUR, 1)`：形态存在 / 不存在 / form 为 nil | 形态条目 / 基础物种或 nil / nil |
| 可选缺席 | shadow_pokemon.dat 不存在 | 该类不加载、不强制重编译（数据为空） |

## 11. 证据与来源（traceability）

- **本轮复核（2026-09-19）**：逐行阅读 `001_GameData.rb`（283 行）、`008_Species.rb`（455 行）、`006_Item.rb`（270 行）、`018_MapMetadata.rb`（138 行）；阅读 `005_Move.rb`、`001_GrowthRate.rb`、`011_ShadowPokemon.rb`、`009_Species_files.rb`、`001_MiscPBSData.rb` 头部/关键段；逐一核对 21 个 PBS 数据类与 17 个固定规则类的身份/文件声明；阅读编译器节解析（`001_Compiler.rb` 第 95–148、867–941、1040–1076 行）与通用编译函数（`002_Compiler_CompilePBS.rb` 第 4–60、283–327 行）；核实 OPTIONAL 唯一性与基名集合（19 声明 + 3 合并）。
- **继承同基线既有记录**：E04（注册/查找与字段抽查，本轮已扩展为全类清单）、E05（编译校验入口，本轮已核实具体错误形式）。
- 全部静态证据；**无运行确认**。

## 12. 未决问题

1. 可选数据缺席时 Shadow 消费者行为（U06，归 WP23）。
2. 字符串查找的大小写/符号一致性边界（未逐类验证）。
3. 未知身份运行时异常的用户呈现（未运行）。
4. schema 类型模式全集与非法输入的拒绝行为（归 WP04）。
5. 非类产物（战斗动画等）的结构未提取（归 WP16/WP67-A）。

## 13. 状态与后续

- WP03 自身范围（第 1 节六项）已提取并自检，状态 **ReviewPending**，提交外部 review。
- **WP03 完成 ≠ F01-02/F02-01 完成**：各类内容的字段语义全集需领域包闭合（见第 7 节责任目录）；Feature Matrix 按聚合规则分别显示。
- 后续包引用本文的身份/查找/缺失值概念时，不得把键名、混入模块名或目录结构当作未来框架的设计依据；发现与本文冲突的新证据时，先修订本文并通知受影响包。
