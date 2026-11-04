# Repository reconnaissance：Pokémon Essentials

本轮范围：Repository Reconnaissance、High-level Module Inventory、Feature Inventory、Dependency Mapping 和后续提取计划。调查日期：2026-09-17 至 2026-09-18。已完整阅读根目录 `AGENTS.md`；本文是分析记录，不是新框架设计，也不是详细行为规格。

2026-09-19 根据模块地图 review 补核关键调用并修订责任边界、任务追踪与证据标签；本地 commit 与 review 基线一致。本次只修订调查材料，没有启动详细规格提取。

## 1. 参考快照与证据边界

- 参考根目录：`reference/pokemon-essentials/`，下文简称 **R**；**S** = `R/Data/Scripts/`，**P** = `R/PBS/`。路径前缀仅用于缩短审计记录。
- 参考 Git commit：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；README 标注基于 Essentials v21.1，设置也标识 21.1。不能把该 commit 等同于未经修改的官方 v21.1 发布包。
- 实际枚举：432 个非 `.git` 文件；`Data/Scripts/` 内 312 个 Ruby 文件、140,865 行；另有根目录脚本提取/合并工具。行数只衡量调查规模，不代表行为覆盖率。
- PBS 顶层 33 个文本文件；备份子目录另有 40 个文本文件；核心英文文本 18 个分类文件。
- 当前设置的机制世代为 8。设置文件明确说明各世代并非精确复刻，只对第五世代及以后提供较合理的支持；机制开关、数据集和实际行为必须分别核实。
- 本轮仅进行文件枚举、文本搜索、关键入口及关联片段阅读、PBS 抽样和静态调用核对。没有启动游戏、运行编译器、执行参考脚本、访问示例网络服务或观察运行时画面。
- 文档中的“已确认”表示有当前快照的静态证据；不表示所有分支、数值和交互已验证。参考目录始终只读。

**最重要的限制：这不是完整可运行的 bundled demo checkout。** README 和 `.gitignore` 说明此仓库需叠加到完整 Essentials v21.1 工程。实际 `Data/` 顶层只有 `Scripts.rxdata` 与 `messages_core.dat`；地图、地图目录、系统、公共事件、tileset、动画等工程数据不在当前快照。`Graphics/`、`Audio/`、`Plugins/`、`Game.ini` 和 `Game.rxproj` 也缺失。因此可以研究核心能力和 demo 配置，但无法确认具体 NPC 对话、事件页、任务流程、商店库存、奖励和可达性。

## 2. 主要目录与组织方式

| 位置 | 实际内容及作用 | 本轮解释边界 |
| --- | --- | --- |
| `R/README.md`、`.gitignore` | 使用前提、脚本加载约定、排除的工程材料 | 用于确定当前证据范围 |
| `S/001_Settings.rb`、`002_BattleSettings.rb` | 游戏参数、机制变体、野外及战斗设置、资源及开关约定 | 同一功能可能同时受世代、专用设置、地图标记影响 |
| `S/001_Technical/`、`002_Save data/`、`003_Game processing/` | 兼容层、输入、文本、插件、持久化、游戏启动、事件分发和事件命令 | 同时混有可泛化能力与现有运行环境依赖 |
| `S/004_Game classes/` 至 `009_Scenes/` | 地图状态、角色运动、事件、地图连接、渲染、窗口、声音和场景过渡 | 不是将来的模块划分；职责经入口和调用片段核实 |
| `S/010_Data/` | 公共数据查找与注册；固定规则目录；PBS 内容字段和引用关系 | 固定规则也可能包含行为判定，不只是枚举 |
| `S/011_Battle/` | 战斗准备后的运行过程、参战者状态、招式效果、AI、表现、捕获及特殊战斗 | 78 个文件、46,947 行；必须按行为族分批提取 |
| `S/012_Overworld/` | 世界事件联动、时间、场地招式、钓鱼、树果、寄养繁殖、随机地牢、战斗触发 | 不能因目录名把繁殖或遭遇概率都归为引擎功能 |
| `S/013_Items/` 至 `015_Trainers and player/` | 背包及道具效果、电话邮件雷达、个体、训练家、玩家、图鉴与储存 | 类似“电话在 Items 下”不代表其概念属于物品库存 |
| `S/016_UI/` | 玩家操作界面及孵化、进化、交换、名人堂等流程 | 部分规则写在界面文件中，提取不能只检查所谓逻辑目录 |
| `S/017_Minigames/`、`018_Alternate battle modes/` | 7 类小游戏、狩猎区、捕虫大会、设施挑战、规则组、租借、生成工具 | 比赛规则、演示内容和开发工具需要分开判断 |
| `S/019_Utilities/`、`020_Debug/`、`021_Compiler/` | 获得生物等脚本入口、编辑调试、PBS 与地图事件转换 | 工具可写回参考工程，因此本轮只读其行为 |
| `S/999_Main/` | 插件、编译、初始化及场景启动顺序 | 不是新框架的入口方案 |
| `P/` | 物种、形态、招式、道具、特性、训练家、遭遇、地图、电话、设施与地牢配置 | 核心规则内容与 demo 内容共存，不能整体视作纯框架 |
| `P/Gen 5 backup/` 至 `Gen 8 backup/`、`Shadow Pokémon backup/` | 备选规则内容 | 编译发现逻辑枚举 PBS 顶层文本；这些子目录不能自动算作启用数据 |
| `R/Text_english_core/`、`Data/messages_core.dat` | 核心术语、说明及脚本文本的翻译基础 | 不等于当前 demo 的地图对话全集 |
| 根目录可执行文件、DLL、`mkxp.json`、Fonts、soundfont | 现有运行环境、字体与声音支持材料 | 存在二进制文件不等于已验证当前平台可运行 |
| 根目录 `scripts_extract.rb`、`scripts_combine.rb`、`townmapgen.html` 等 | 脚本往返组织及外围制作工具 | README/文件内容抽查；未执行转换与生成 |

## 3. 重要入口与数据流

1. README 约定外部脚本按字母数字顺序、逐层先当前目录后子目录加载；`Data/Scripts.rxdata` 被说明为加载这些文件的入口。本轮没有解包验证该二进制文件的内部内容。
2. `S/999_Main/999_Main.rb` 读取核心消息，运行插件，进入编译检查，初始化游戏数据和系统，再进入标题或调试载入界面。插件运行早于编译检查，后续需要核实插件对数据和规则的影响。
3. `S/003_Game processing/001_StartGame.rb` 区分启动阶段的设置载入、新游戏初始化、已有游戏载入与保存，并将地图、遭遇、玩家和持久状态连接起来。
4. `S/021_Compiler/001_Compiler.rb` 发现 PBS 内容，按引用关系编译，处理地图事件和可翻译文本。实际代码包含数据删除重建、PBS 改写和地图事件写回，因此它不是纯解析器。
5. `S/003_Game processing/002_Scene_Map.rb`、地图/玩家状态与世界事件联动：输入、移动、互动、地图转移和逐帧/逐步通知触发其他功能。
6. `S/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb` 将地图环境、训练家、队伍、临时战斗规则与战斗呈现组合起来，并在结束后通知成长、拾取、形态清理及失败处理等消费者。
7. `S/011_Battle/001_Battle/002_Battle_StartAndEnd.rb` 可见命令选择、行动处理、回合结束、胜负结算这几个行为阶段。这里仅标识需要规格化的阶段，不复制其控制结构。
8. 获得生物不是捕获独有能力：野外捕获、赠送、蛋、交换、神秘礼物都会影响所有权、队伍/储存、命名和图鉴。对应流程散布于战斗、工具入口和 UI。

已抽查的主要内容引用关系（非完整 schema 依赖全集）：类型 → 招式 → 道具；类型、招式、道具、特性 → 物种；物种 → 形态、图鉴及遭遇；训练家类型、物种、道具、招式 → 训练家。训练家个体配置在显式指定时还引用特性、性格等规则目录（E04）；这不意味着每个被引用的目录都对应 PBS 文件。训练家类型也供玩家元数据、电话及设施名单使用。编译执行顺序、内容引用关系和运行时行为依赖应分别记录；不能仅凭编译顺序或注释推定全部引用，也不据此规定未来代码模块。

## 4. 高层依赖与跨域边界

领域编号见 [module-map](../planning/module-map.md)，功能编号见 [feature-matrix](../planning/feature-matrix.md)。

| 行为链 | 已找到的连接 | 对后续提取的影响 |
| --- | --- | --- |
| 配置/内容 → 个体 → 队伍 → 战斗 | 数据注册、物种字段、个体生成、参战队伍检查 | 先定义术语、身份和状态，再研究完整战斗 |
| 地图/地形/时间 → 遭遇 → 战斗准备 | 世界事件、遭遇表、天气/环境映射、临时规则 | “触发战斗”和“战斗规则”分别立项后联审 |
| 捕获 → 图鉴 → 命名 → 队伍/储存 | 捕获结果登记及存放流程；赠送也使用相近能力 | 容量满、强制入队、取消、登记顺序需要联合测试 |
| 战斗 → 经验/EV/招式 → 进化 | 战斗内成长与战后检查均存在 | D09 定义成长/学习，D11 记录战斗中触发与能力/招式反馈，以及战后检查；不能只记战后奖励 |
| 步数/时间 → 寄养、孵化、树果、电话、漫游 | 世界事件订阅与各系统状态 | 时钟、步数和存档恢复是横切关注点 |
| 背包/货币 → 道具/商店/小游戏 | UI 中也含消耗、限制、买卖与奖励行为 | 不能仅从存储结构提取库存规格 |
| 形态/特性/持有物 → 战斗/繁殖/进化 | 生成、进入/离开战斗、遗传与进化检查的消费者 | 可变形态、永久个体状态和临时战斗状态要区分 |
| 设施挑战 → 队伍选择/等级调整 → 战斗 → 恢复/记录 | 组织化战斗入口保存并恢复等级、物品等状态 | 设施流程在基础战斗以后提取 |
| 插件/编辑/编译 → 数据/文本/地图事件 | 插件依赖检查、数据生成、事件转换和文本收集 | 开发者工作流是行为范围，不是未来插件 API 设计 |

捕获判定主规格固定为 D10；D08 的库存/消耗、D11 的动作合法性/时机、D07 的集合、D15 的图鉴和 D16 的交互分别引用各自主规则。强制入队与取消接收权限是捕获领域策略，UI 呈现允许的操作。变身、Shadow、学招、位置移动、呼唤和服从性的跨域追踪见模块地图；文件所在目录不决定规则归属。

Generic Kernel 是**候选行为归类**，不意味着现有实现独立、可直接复用。随机性目前见于多个独立使用点、战斗随机入口及录像记录；不能据此宣称已有统一、可注入、全局可重放的随机服务。同理，持久化、资源和时间规则都与现有宿主有交叉。

## 5. Bundled demo：能证明什么

P 中有 69 条地图元数据、19 条遭遇配置节（包含同地图的版本变体）、20 条训练家配置节。物种/形态的节数不作为“功能数量”。这些统计是当前文件的节数，不是完整 demo 中实际地图或战斗的数量。

| demo 能力线索 | 当前证据 | 可以下的结论 | 尚不能下的结论 |
| --- | --- | --- | --- |
| 城镇、路线与连续世界 | 地图元数据、地图连接、区域地图数据 | 已配置多个地点、连接关系及区域定位 | 地图几何、传送事件和实际通路可用 |
| 草地、昼夜、水上、钓鱼与遭遇变体 | Route 1 等遭遇表，包含日夜/钓竿/版本/雷达条目 | 存在这些遭遇配置及对应消费逻辑 | 玩家何时解锁、事件具体如何修改版本 |
| 天气、骑行、潜水、黑暗洞穴 | 地图天气、强制骑行、潜水目标、黑暗标志 | demo 数据配置了环境与移动能力 | 特定 NPC 授予能力或场地招式完整流程 |
| 随机地牢 | Dungeon 地图标志、cave/forest 参数、地牢 tileset 配置 | 配置与地图创建时的生成处理有对应关系 | 当前地图 tileset ID 和可运行布局；原始地图缺失 |
| 道馆及训练家再战 | 训练家队伍、变体、道具、电话文本配置 | 可配置战斗与训练家不同版本 | 道馆奖励、徽章赋予或再战事件可达性 |
| 狩猎区、捕虫大会 | Safari 标志、BugContest/Reception 标志、专用遭遇表 | 专用模式在代码和 demo 配置中都有证据 | 报名费、接待 NPC、发奖流程 |
| Battle Frontier 与各类杯赛 | 地图元数据、设施名单、预制队伍和规则入口 | Tower/Palace/Arena/Factory、租借及杯赛有代码/数据依据 | 每个大厅事件实际调用的完整参数和奖励 |
| 寄养、商店、游戏角、名人堂 | 场所元数据与相应脚本入口 | 存在场所线索及框架支持；证据强度低于有具体标志/配置的条目 | 仅凭地点名称确定使用了哪些具体小游戏、库存、收费 |
| Shadow、交换、赠送、邮件、神秘礼物 | 训练家含 Shadow 标记；相关入口/调试操作存在 | 核心支持及部分数据示例存在 | 可从 demo 到达全部入口；可选 Shadow 数据均已启用；在线示例可用 |

寄养源文件还明确指出：寄养与培育屋收费差异的一部分由接待事件负责。它是“缺失 demo 事件会遗漏规则”的直接证据。后续即使获得完整工程，也需在独立分析副本检查事件，不能启动当前只读参考目录中的自动编译流程。

## 6. 不确定性与下一轮调查问题

| ID | 未知点 | 目前证据与影响 | 后续位置 |
| --- | --- | --- | --- |
| U01 | 完整 demo 的地图/公共事件/资源 | 当前明确缺失；影响事件收费、授予能力、奖励和可达性验证 | WP01、WP77 |
| U02 | 当前 commit 与基准发布包的行为差异 | 有明确 commit，但未比对发布包；不能把设置注释当一致性证明 | WP01、WP02 |
| U03 | 世代开关和 PBS 备份的组合边界 | 默认机制为 8，编译不自动遍历备份目录；需分别记录配置和数据集 | WP02、WP04 |
| U04 | 数据存在与完整功能存在的区别 | 有华丽大赛属性，但未建立完整华丽大赛流程证据；关键词搜索未找到 Dynamax/Z-Move/Terastal 或网络对战入口 | WP01、WP79；搜索未命中不等于不存在 |
| U05 | 随机数、时间、录像确定性 | 普通随机、地牢种子、战斗录像三类证据共存，未验证跨系统一致性 | WP06、WP14、WP58 |
| U06 | Shadow 数据与脚本的启用条件 | 核心脚本与训练家标记存在；可选 PBS 在备份目录 | WP23、WP04 |
| U07 | 取消/失败时的跨域状态一致性 | 捕获、赠送、交易、道具和商店有分散的容量检查；尚未逐分支审查 | 对应领域包及 WP78 |
| U08 | RMXP 命令兼容范围 | 事件解释器中部分标准 RPG 命令明确为空操作；不能声称完整 RMXP 行为兼容 | WP13 |
| U09 | 插件实际组合及外部服务行为 | 无 Plugins 内容；神秘礼物有下载入口但未联网测试 | WP05、WP64 |
| U10 | 战斗效果、AI 判断与版本差异覆盖 | 是最大代码区域；本轮只标识机制族和关键连接 | WP39–WP52（含子包）、WP79 |

下一阶段应首先确定基线/证据缺口，建立配置与内容身份概念，再开始生物个体、队伍/储存、持久化与事件边界的详细提取。本轮不执行这些包，完整顺序见 [extraction-plan](../planning/extraction-plan.md)。

## 7. 证据索引（供四份文档共同使用）

下列 E 编号是 **Reference locations** 的可解析索引。所有路径展开规则见第 1 节。一个证据包列出检查过的入口、搜索范围及内容样本；不表示包内所有文件已逐行阅读。目录范围表示已枚举/搜索，关键文件表示有内容阅读或调用核对。

| 证据状态 | 可以支持的结论 |
| --- | --- |
| 已定位 | 已找到相关文件、配置或入口；不独立证明行为 |
| 静态确认 | 已阅读实现及必要调用/消费者，支持注明范围的行为描述 |
| 数据样本确认 | 已检查实际内容或配置样本，不等于事件可达或运行通过 |
| 运行确认 | 已在注明环境、配置、输入下观察到结果；本轮无此证据 |
| 待验证 | 材料不足、调用未追完、公式/边界未穷尽或组合尚未核实 |

这些标签按具体结论使用，可以并存，不是从弱到强的完成进度。实现分支存在不证明默认启用或所有组合可运行。下表状态只覆盖注明的抽查范围；所有证据包均未运行确认，未列出的分支不算已覆盖。后续详细规格需把规则编号连到实际文件、观察条件及测试场景；E 包不能充当整域完成证书。

| ID | Reference locations | 本轮阅读/核对范围 | 证据状态与边界 |
| --- | --- | --- | --- |
| E01 | `R/README.md`；`R/.gitignore`；`R/mkxp.json`；`R/scripts_extract.rb`、`R/scripts_combine.rb`（README 描述）；`R/Data/` 文件枚举 | 快照、加载约定、资源缺口及运行配置 | 已定位、静态确认：快照/README；待验证：二进制加载器与运行条件 |
| E02 | `S/001_Settings.rb`；`S/002_BattleSettings.rb` | 世代/容量/场地/成长与表现设置；补核亲密、捕获经验、进化资格、Mega 顺序与服从性开关，消费者见 E16/E18/E21/E22 | 数据样本确认：基线设置；静态确认：所列消费者；待验证：全部组合 |
| E03 | `S/001_Technical/005_PluginManager.rb`；`S/003_Game processing/005_Event_Handlers.rb`；`006_Event_HandlerCollections.rb`（同目录） | 插件元数据、依赖排序、事件和菜单扩展点 | 静态确认：扩展入口/依赖处理；待验证：真实插件组合 |
| E04 | `S/010_Data/001_GameData.rb`；`S/010_Data/001_Hardcoded data/`；`S/010_Data/002_PBS data/`，其中 `015_Trainer.rb`；`P/` | 注册/查找、字段与消费者抽查；Species、MapMetadata 等内容；补核训练家节标识对训练家类型的引用、个体配置对特性/性格的引用及生成时的使用 | 已定位、静态确认、数据样本确认：注册及抽查字段；训练家引用已静态确认，未穷尽 schema |
| E05 | `S/021_Compiler/001_Compiler.rb`；`002_Compiler_CompilePBS.rb`、`003_Compiler_WritePBS.rb`、`004_Compiler_MapsAndEvents.rb`（同目录） | 编译发现、引用顺序、诊断、写回与事件转换入口 | 静态确认：发现/编译/写回入口；待验证：完整输入与失败分支 |
| E06 | `S/001_Technical/003_Intl_Messages.rb`；`R/Text_english_core/`；`S/003_Game processing/001_StartGame.rb` | 文本提取/编译入口、分类文件枚举、语言载入 | 已定位、静态确认：文本分类和载入；待验证：翻译运行结果 |
| E07 | `S/002_Save data/001_SaveData.rb`；`002_SaveData_Value.rb`、`003_SaveData_Conversion.rb`、`004_Game_SaveValues.rb`、`005_Game_SaveConversions.rb`（同目录） | 保存/读取/转换入口、持久值登记；迁移细则未穷尽 | 静态确认：保存/迁移入口；待验证：迁移细则与旧档样本 |
| E08 | `S/999_Main/999_Main.rb`；`S/003_Game processing/001_StartGame.rb`；`S/004_Game classes/012_Game_Stats.rb` | 启动、载入、新游戏、错误出口、统计消费者 | 静态确认：启动与状态入口；待验证：全部故障/恢复路径 |
| E09 | `S/004_Game classes/004_Game_Map.rb`；`005_Game_MapFactory.rb`、`006_Game_Character.rb`、`008_Game_Player.rb`（同目录）；`S/010_Data/001_Hardcoded data/011_TerrainTag.rb` | 地图连接/运动入口与互动片段；地形定义搜索 | 已定位、静态确认：连接/运动片段；待验证：地图几何与组合通行 |
| E10 | `S/003_Game processing/003_Interpreter.rb`；`004_Interpreter_Commands.rb`（同目录）；`S/004_Game classes/007_Game_Event.rb`；`009_Game_CommonEvent.rb`、`010_Game_Follower.rb`、`011_Game_FollowerFactory.rb`（同目录） | 事件命令、触发/条件、跟随入口与兼容性空操作 | 静态确认：事件入口和空操作；待验证：命令全集及 demo 事件 |
| E11 | `S/001_Technical/001_MKXP_Compatibility.rb`；`004_Input.rb`（同目录）；`S/001_Technical/002_Files/003_HTTP_Utilities.rb`；`S/005_Sprites/`；`S/006_Map renderer/001_TilemapRenderer.rb`；`S/007_Objects and windows/001_RPG_Cache.rb`、`011_Messages.rb`；`S/008_Audio/002_Audio_Play.rb`；`S/009_Scenes/` | 资源读取、地图绘制、消息/输入、音频、场景入口；补核 HTTP 下载/提交、响应返回或文件写入的包装逻辑，下载调用见 E30；动画细节仅枚举 | 已定位、静态确认：抽查入口及 HTTP 包装逻辑；待验证：外部服务可用性、宿主网络实现、完整失败行为及媒体/动画输出；无网络运行确认 |
| E12 | `S/014_Pokemon/001_Pokemon.rb`；`004_Pokemon_Move.rb`、`005_Pokemon_Owner.rb`（同目录）；`S/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb`；`S/010_Data/002_PBS data/008_Species.rb` | 个体字段、生成、形态入口、成长/进化连接 | 静态确认：个体/形态与连接；待验证：全部属性规则与特例 |
| E13 | `S/015_Trainers and player/001_Trainer.rb`；`002_Trainer_LoadAndNew.rb`、`004_Player.rb`（同目录）；`S/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb`；`S/019_Utilities/002_Utilities_Pokemon.rb` | 玩家能力、训练家载入、储存容量、获得和命名 | 静态确认：集合/玩家/获得入口；待验证：容量与取消全分支 |
| E14 | `S/013_Items/008_PokemonBag.rb`；`001_Item_Utilities.rb`、`002_Item_Effects.rb`、`003_Item_BattleEffects.rb`（同目录）；`S/010_Data/002_PBS data/006_Item.rb` | 背包入口、道具使用分流/返回行为；效果注册搜索；补核球使用限制与捕获调用边界 | 已定位、静态确认：使用分流及球限制；待验证：全部道具效果 |
| E15 | `S/016_UI/020_UI_PokeMart.rb`；`021_UI_BattlePointShop.rb`（同目录）；`S/013_Items/006_Item_Mail.rb` | 买卖价格与容量检查片段、积分商店和邮件入口 | 静态确认：交易检查片段；待验证：完整买卖/邮件流程 |
| E16 | `S/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb`；`S/010_Data/001_Hardcoded data/001_GrowthRate.rb`、`007_Evolution.rb`；`S/016_UI/022_UI_MoveRelearner.rb`；`S/016_UI/001_Non-interactive UI/004_UI_Evolution.rb`；E12 | 成长/学习、进化触发及消费者；补核战斗中升级后的当前参战能力和招式同步、放弃学习路径 | 静态确认：成长反馈与学习入口；待验证：公式/取整、全部触发及交互 |
| E17 | `S/012_Overworld/007_Overworld_DayCare.rb`；`S/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb` | 寄养步数、遗传流水线、收费边界注释、孵化入口 | 静态确认：寄养/遗传/孵化入口；待验证：遗传细则与接待事件 |
| E18 | `S/012_Overworld/001_Overworld.rb`；`S/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb`、`003_Overworld_WildEncounters.rb`、`004_Overworld_EncounterModifiers.rb`；`P/encounters.txt` | 遭遇选择、阻止/修改、战斗创建和结束回调 | 静态确认、数据样本确认：入口及遭遇样本；待验证：全情境组合 |
| E19 | `S/012_Overworld/002_Battle triggering/005_Overworld_RoamingPokemon.rb`；`S/013_Items/005_Item_PokeRadar.rb`；`S/012_Overworld/005_Overworld_Fishing.rb` | 漫游/雷达状态入口和事件订阅；钓鱼调用搜索 | 已定位、静态确认：状态入口/订阅；待验证：连锁和钓鱼完整规则 |
| E20 | `S/011_Battle/007_Other battle code/004_Battle_Peers.rb`；`005_Battle_CatchAndStoreMixin.rb`、`010_Battle_PokeBallEffects.rb`（同目录） | 捕获判定/球修正、抢夺例外、经验衔接、形态恢复及登记/存放；补核强制入队与取消选项限制 | 静态确认：捕获与接收策略；待验证：完整公式、球/模式组合和取消分支 |
| E21 | `S/011_Battle/001_Battle/`，重点 `001_Battle.rb`、`002_Battle_StartAndEnd.rb`、`008_Battle_ActionOther.rb`、`010_Battle_AttackPhase.rb`；E18 | 参战组织/阶段/终局；补核野生/训练家区分、双方场上数量、控制归属及 E18 伙伴组队/模式设置；Shift/Call、Mega/Primal 各自处理与行动阶段调用；成长及 Primal 其他调用点仅搜索 | 静态确认：参战组织/布局入口及所列行动和阶段；已定位：其他调用点；待验证：完整时序及布局/控制组合 |
| E22 | `S/011_Battle/002_Battler/`，其中 `009_Battler_UseMoveSuccessChecks.rb`；`S/011_Battle/003_Move/`，重点 `002_Move_Usage.rb`、`003_Move_UsageCalculations.rb` | 目标/使用/计算入口与效果族索引；补核服从性实际消费者对所有者、等级/徽章、开关和 Hyper 的使用；未提取完整判定 | 已定位、静态确认：计算入口/服从性消费者；待验证：公式与规则全集 |
| E23 | `S/011_Battle/007_Other battle code/001_PBEffects.rb`；`002_Battle_ActiveField.rb`、`006_Battle_Clauses.rb`、`008_Battle_AbilityEffects.rb`、`009_Battle_ItemEffects.rb`（同目录） | 场域状态、限制及特性/道具触发族 | 已定位、静态确认：状态及触发族入口；待验证：每项效果/交互 |
| E24 | `S/011_Battle/005_AI/001_Battle_AI.rb`；`009_AITrainer.rb`（同目录）；`S/011_Battle/005_AI/`、`S/011_Battle/006_AI MoveEffects/` | 行动选择链、技能档/标记、效果评分族枚举 | 已定位、静态确认：选择链；待验证：各效果评分与实际效果差异 |
| E25 | `S/014_Pokemon/002_Pokemon_MegaEvolution.rb`；`003_Pokemon_ShadowPokemon.rb`（同目录）；`S/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb`；`S/016_UI/023_UI_PurifyChamber.rb`；`P/Shadow Pokémon backup/` | Mega/Primal 与 Shadow 入口；补核净化资格、招式恢复、暂存 EV/经验、成长、缎带和命名；可选内容启用待查 | 静态确认：变身/净化所列片段；已定位：备选数据；待验证：启用与完整生命周期 |
| E26 | `S/018_Alternate battle modes/001_SafariZone.rb`；`002_BugContest.rb`（同目录）；`S/011_Battle/008_Other battle types/001_SafariBattle.rb`、`002_BugContestBattle.rb` | 模式入口、会话状态、步数/时间与战斗接管 | 静态确认、数据样本确认：模式/配置；待验证：接待/收费/判奖事件 |
| E27 | `S/018_Alternate battle modes/001_Battle Frontier/`；`002_Battle Frontier rules/`、`003_Battle Frontier generator/`（同层目录）；`S/011_Battle/008_Other battle types/003_BattlePalaceBattle.rb`、`004_BattleArenaBattle.rb`、`005_RecordedBattle.rb`；`P/battle_facility_lists.txt` | 入场规则、等级恢复、租借入口、AI 变体、录像和生成工具 | 已定位、静态确认、数据样本确认：设施入口/名单；待验证：全模式与回放 |
| E28 | `S/012_Overworld/003_Overworld_Time.rb`；`004_Overworld_FieldMoves.rb`、`006_Overworld_BerryPlants.rb`、`001_Overworld.rb`（同目录）；`S/012_Overworld/001_Overworld visuals/`；`P/berry_plants.txt` | 时间/场地能力、植物状态、逐步效果和野外表现 | 静态确认、数据样本确认：时间/场地/植物入口；待验证：时钟与场景组合 |
| E29 | `S/012_Overworld/008_Overworld_RandomDungeons.rb`；`S/010_Data/002_PBS data/019_DungeonTileset.rb`、`020_DungeonParameters.rb`；`P/dungeon_parameters.txt`、`P/dungeon_tilesets.txt` | 布局/房间入口、地图创建回调、事件摆放失败及种子字段 | 静态确认、数据样本确认：生成入口/参数；待验证：实际地图和可达性 |
| E30 | `S/015_Trainers and player/005_Player_Pokedex.rb`；`S/013_Items/004_Item_Phone.rb`；`S/016_UI/008_UI_Pokegear.rb`、`009_UI_RegionMap.rb`、`010_UI_Phone.rb`、`011_UI_Jukebox.rb`、`024_UI_MysteryGift.rb`；`P/phone.txt` | 图鉴记录入口、电话再战、工具菜单、下载/领取礼物 | 已定位、静态确认、数据样本确认：工具入口/电话样本；待验证：完整交互/联网 |
| E31 | `S/016_UI/`，重点 `001_UI_PauseMenu.rb`、`019_UI_PC.rb`；`S/016_UI/001_Non-interactive UI/005_UI_Trading.rb`、`006_UI_HallOfFame.rb`；`S/011_Battle/004_Scene/` | 界面全集枚举、菜单/交换/名人堂入口；战斗呈现只做职责索引 | 已定位：界面全集；静态确认：抽查菜单/交换/名人堂；待验证：所有 UI 流程 |
| E32 | `S/017_Minigames/001_Minigame_Duel.rb` 至 `007_Minigame_TilePuzzles.rb` | 七个文件全部枚举并检索入口，阅读入口/奖品与权限片段 | 已定位：七类文件；静态确认：抽查入口/奖品/许可片段；待验证：各小游戏完整规则 |
| E33 | `S/020_Debug/003_Debug menus/`；`S/020_Debug/001_Editor screens/`、`002_Animation editor/`；`R/animmaker.txt`、`R/extendtext.txt`、`R/townmapgen.html`（文件发现）；E05 | 调试菜单能力、编辑入口与辅助工具清单；未验证可执行工具 | 已定位：工具/编辑入口；静态确认：抽查调试菜单；待验证：外围工具实际行为 |
| E34 | `P/metadata.txt`、`map_metadata.txt`、`map_connections.txt`、`encounters.txt`、`trainers.txt`、`battle_facility_lists.txt`、`dungeon_parameters.txt`、`town_map.txt`、`phone.txt` | demo 配置抽样、节数统计、设施/地图/遭遇交叉核对 | 数据样本确认：配置与节数；待验证：完整地图事件、参数使用和可达性 |

## 8. 本轮成果边界

本轮建立 18 个概念领域、113 个初始功能组、87 个后续可执行工作包和 34 组来源索引。已校验 ID 唯一性、功能到任务的覆盖、任务依赖无环、显式来源路径及文档链接；这些检查只验证本轮地图的内部一致性，不代表已完成后续跨模块规格或功能覆盖审查。

交付只包含地图、初始矩阵、依赖驱动的工作包计划及本文。未新增实现代码、未建立最终 API/类层级、未输出参考源码片段、未展开具体规则的完整公式或测试向量。详细提取、跨模块一致性审查、覆盖审查及最终 sanitized 规格均安排在后续阶段。
