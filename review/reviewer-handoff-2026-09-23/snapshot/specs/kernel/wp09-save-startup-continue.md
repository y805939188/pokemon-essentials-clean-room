# WP09 规格：保存、启动、新游戏与继续

| 字段 | 内容 |
| --- | --- |
| 工作包 | WP09（保存、启动、新游戏/继续） |
| 关联功能 | F03-01（持久状态登记与保存，D03）、F03-03（启动、新游戏与继续，D03） |
| 分类 | Generic Kernel（持久化机制）＋ Engine/Overworld（启动与地图恢复）；保存值名称是参考侧取证记录，不是未来框架的存储格式 |
| 参考基线 | `reference/pokemon-essentials/` @ commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（WP01 固定） |
| 输入 | 证据包 E07（保存/读取/转换入口、持久值登记）、E08（启动、新游戏、统计消费者）、E31（载入 UI） |
| 前置依赖 | WP03（内容身份）、WP06（时间/统计），均已 Reviewed |
| 规格状态 | **Reviewed（固定默认 17 项持久状态的已述登记、类型检查、启动加载、新游戏/继续、地图恢复分流、保存前后内存/磁盘边界及静态场景范围）**：2026-09-19 经批次复审系列修订后，由 WP08–WP10 v2 复审（`review/wp08-wp10-recheck-2026-09-19/report.md`）通过；任意扩展登记、完整迁移/恢复、缺失 Demo 可达性与宿主落盘结果不在本状态内 |
| 证据等级 | 全部为静态证据：已定位 / 静态确认 / 数据样本确认；**无运行确认** |

## 1. 目的、范围与非目标

**目的**：建立持久状态目录和启动阶段/新游戏/继续的状态规则——在何时读取、保留、初始化、重置、写入哪些状态。后续包据此判断"某状态是否持久、何时生效、新游戏后保留什么"，而不是各自重新追踪保存系统。

**范围**（WP09 自身声明范围，extraction-plan 第 2.1 节 (a) 类）：

1. WP09-A：持久值登记目录（登记项、形态、校验、默认/初始化、读取时机）。
2. WP09-B：启动阶段与新游戏/继续（状态阶段、上游顺序、无存档与调试入口、地图恢复）。
3. WP09-C：保存路径与写入边界（成功路径、前置、内存与磁盘边界、失败形式）。
4. WP09-D：设置与进度的区分（语言/选项 vs 游戏进度状态）。
5. F03-01、F03-03 中属于 WP09 部分的状态更新。

**非目标**：

- 不提取保存文件的二进制格式与旧格式迁移细则（WP10 主规格，本文只登记交界）。
- 不提取各保存值字段的领域语义（如玩家/背包/储存的字段，归相应领域包）。
- 不提取备份/紧急保存/恢复的全部失败分支（WP10 主规格）。
- 不宣称完整 Demo 启动成功（缺失地图/事件材料）；不运行游戏或任何参考脚本；不修改 `reference/`。

## 2. 概念与术语

- **持久值（SaveData.Value）**：一个被登记为保存内容的状态单元，具有保存/读取/新游戏值/类型校验/启动读取/新游戏重置等配置。
- **启动读取（load_in_bootup）**：启动时即读取的值（在标题/选择之前就需要）。
- **新游戏值（new_game_value）**：无存档或新游戏时用于初始化的值。
- **新游戏重置（reset_on_new_game）**：即使已加载，新游戏时也强制重置为初始值。
- **设置（settings/options）**：玩家的偏好（如语言、文本速度），与游戏进度状态分开。
- 影响域编号 Dxx 见 module-map；证据状态五档定义见总览第 7 节。

## 3. WP09-A：持久值登记目录

### 3.1 登记机制（`S/002_Save data/002_SaveData_Value.rb`，本轮逐行阅读）

每个持久值按以下配置登记（`SaveData.register(id) { … }`）：

| 配置 | 行为 |
| --- | --- |
| `save_value`（必需） | 保存时取什么值（缺则登记报错） |
| `load_value`（必需） | 读取时如何恢复（缺则登记报错） |
| `new_game_value`（可选） | 无存档或新游戏时的初始化值（无存档键时用它） |
| `ensure_class` | 保存/读取时校验值的类型，不符抛 InvalidValueError |
| `load_in_bootup` | 启动早期即读取（标题/选择之前） |
| `reset_on_new_game` | 已加载值在新游戏时也强制重置 |
| `from_old_format` | 从旧格式存档取值的转换入口（迁移归 WP10；**当前 17 项均未配置**） |

读取规则（WP09-R01 修订）：

- `valid?(save_data)`：逐值校验类型，**不因为有 new_game_value 就容忍缺键**——缺键即 invalid（与"键存在但值类型错"是不同情况）。**限定范围（BATCH-C02）**：该结论适用于当前默认 17 项均配置 ensure_class 的情形（缺失项以 nil 参与类型检查）；未配置 ensure_class 的 Value 没有独立必需键保证（`002_SaveData_Value.rb:31–33, 210–212`），不能外推到未绑定类型的扩展登记。
- `load_values` 按条件遍历：存档有键则读取；**无键且有 new_game_value 则用新游戏值**；**键存在但类型错误**抛 InvalidValueError（与缺键默认分支不同）。
- 已加载标记：只跳过已加载值；`mark_values_as_unloaded` 把"非启动读取或需重置"的值标记为未加载。
- **新游戏初始化**只作用于"有新游戏值且（未加载或要求重置）"的登记项，不是所有登记项。

### 3.2 持久值目录（`S/002_Save data/004_Game_SaveValues.rb`，本轮逐行阅读，共 17 项）

| 登记项 | 类型 | 启动读取 | 新游戏值 | 新游戏重置 | 备注 |
| --- | --- | --- | --- | --- | --- |
| player | Player | — | 有（未命名 + 首个训练家类型） | — | 玩家 |
| frame_count | Integer | — | 0 | — | **已弃用**（由 $stats.play_time 取代；弃用注释明示） |
| game_system | Game_System | **是** | 有 | — | 系统（含 save_count、magic_number）；**启动已加载、非强制重置——新游戏时可保留**（WP09-R01） |
| pokemon_system | PokemonSystem | **是** | 有 | — | 玩家选项/设置（语言、文本速度等） |
| switches | Game_Switches | — | 有 | — | 游戏开关 |
| variables | Game_Variables | — | 有 | — | 游戏变量 |
| self_switches | Game_SelfSwitches | — | 有 | — | 自开关 |
| game_screen | Game_Screen | — | 有 | — | 画面状态 |
| map_factory | PokemonMapFactory | — | **无** | — | 地图工厂（恢复用） |
| game_player | Game_Player | — | 有 | — | 玩家角色 |
| global_metadata | PokemonGlobalMetadata | — | 有 | — | 全局元数据（含 encounter_version 等，WP06 引用） |
| map_metadata | PokemonMapMetadata | — | 有 | — | 地图元数据 |
| bag | PokemonBag | — | 有 | — | 背包 |
| storage_system | PokemonStorage | — | 有 | — | 储存系统 |
| essentials_version | String | **是** | 有 | — | 引擎版本（启动加载的状态 vs 保存时读取当前常量，两种形态分开） |
| game_version | String | **是** | 有 | — | 游戏版本（同上，WP02 词典） |
| stats | GameStats | **是** | 有 | **是** | 统计（WP06 主规格；启动读取 + 新游戏强制重置——**重建后 play_sessions 又 +1，新游戏完成时 stats.play_sessions = 1，不是 0**（`001_StartGame.rb:48–50`）） |

对象整体保存与其字段语义分开：本表只登记持久单元与配置，各对象的字段语义归相应领域包（如玩家/背包/储存/元数据）。

## 4. WP09-B：启动阶段与新游戏/继续

### 4.1 启动阶段表（本轮核实）

| 阶段 | 行为 | 证据 |
| --- | --- | --- |
| 上游准备 | 核心消息加载 → 插件 → 编译检查 → 游戏初始化 → **系统设置**（读取并加载启动值，错误可能在此中断，不到达备份界面，WP10 引用） → 标题场景 | `999_Main/999_Main.rb:25–41`；`001_StartGame.rb:21–27` |
| 启动读取 | 存档存在时先读取 load_in_bootup 值（game_system、pokemon_system、essentials_version、game_version、stats）；无存档时以 new_game_value 初始化这些启动值 | `002_SaveData_Value.rb:255–267`；`001_StartGame.rb:22–27` |
| 标题/载入界面 | **普通无存档路径仍构建菜单**（有存档时首项"继续"，另有新游戏、选项、语言（候选 ≥2）、调试（$DEBUG）、退出）；**仅当 $DEBUG + 无 Game.rgssad + SKIP_CONTINUE_SCREEN 三者同时成立时**，才跳过菜单直接新游戏/继续 | `016_UI/013_UI_Load.rb:281–325` |
| 新游戏 | `load_new_game_values`（有新游戏值且未加载或要求重置的值取新游戏值）→ 设游戏时间锚点 → play_sessions += 1 → 建地图工厂与玩家位置 → 进入地图场景 | `001_StartGame.rb:45–58` |
| 继续（读档） | `load_all_values`（全部未加载值）→ 设游戏时间锚点 → play_sessions += 1 → `load_map`（恢复地图）→ 进入地图场景 | `001_StartGame.rb:60–70` |
| 地图恢复 | **magic_number 不一致或 safesave 为真时重新 setup 地图**（缺地图时：调试给选图入口（取消则退出，选择后设图与坐标），非调试抛"地图未找到，无法继续"）；**两者都不成立才 setMapChanged**；此后 `$game_map.events` 为 nil 时抛"地图损坏，游戏无法继续"（与缺图是不同错误） | `001_StartGame.rb:76–104` |

### 4.2 设置与进度的区分（WP09-D）

- **设置（pokemon_system）**：玩家选项（语言、文本速度、选项配置）——启动读取，**新游戏时也读取保留**（不属于进度，不随新游戏重置）。
- **进度（其余各值）**：玩家、背包、储存、开关/变量、地图、统计等——按上表的新游戏值/重置规则处理；**game_system 是启动已加载、非强制重置的值，与 pokemon_system 一样可能保留**（WP09-R01 修订：不能把所有非选项对象统一为"新游戏重置的进度"）；stats 启动读取但**新游戏强制重置**（重建后 play_sessions 又 +1，完成时为 1，WP06 对齐）。
- **版本（essentials_version、game_version）**：随存档保存的引擎/游戏版本，启动读取，供版本兼容判断（迁移归 WP10）；启动加载的状态与保存时读取当前常量是两种形态，分别记录。
- 语言属于设置（WP08 引用）：新游戏不重置语言选择；具体选项集合的语义归 WP65（选项 UI）。

## 5. WP09-C：保存路径与写入边界

### 5.1 保存成功路径与前后状态（`001_StartGame.rb:106–125`，本轮逐行阅读；WP09-R03 修订）

| 阶段 | 内存状态变化 | 磁盘状态 |
| --- | --- | --- |
| 保存前 | 设 safesave 标志；`save_count += 1`；`magic_number = $data_system.magic_number`；`set_time_last_saved`（写入当前 play_time 为最近保存时刻，可能经 play_time 刷新锚点，WP06 对齐） | 未触及 |
| 取值/校验 | `compile_save_hash`：全部持久值的 save_value 取值并校验（ensure_class 不符抛 **InvalidValueError**——**不在 IOError/SystemCallError 捕获集合内，save_count 不回退**） | 未触及（此阶段尚未打开文件） |
| 打开/序列化 | `File.open(..., "wb")` 后 `Marshal.dump` | 打开即截断旧文件（覆盖模式） |
| 成功后 | `Graphics.frame_reset` | 新存档文件 |
| IOError/SystemCallError 分支 | **仅回退 save_count（-1）** 并返回 false——safesave、magic_number、time_last_saved、锚点等**均不回退** | 文件状态未验证（可能部分写入/截断） |

路径选择（`001_SaveData.rb:8–12`）：默认保存路径为 `System.data_directory + "/Game.rxdata"`（该目录存在时），否则 `./Game.rxdata`；也可传入自定义路径（调用方决定，与默认路径是两种写入目标）。

### 5.2 其他写档路径（各自责任，不暗示都经过 Game.save）

- **语言菜单直写**：已有存档时切换语言把选项写入存档 Hash 并直接写回（WP08 主规格，引用）。
- **转换读取写回**：读取存档后若发生转换则把结果重新写回（WP10 主规格，引用）。
- **删除存档**：`SaveData.delete_file` 删除存档与 `.bak`（`001_SaveData.rb:63–68`）。

### 5.3 无存档/损坏/备份（启动侧事实）

- 无存档：`@save_data = {}`；普通路径仍显示菜单（4.1）。
- 存档无效（`SaveData.valid?` 假）：有 `.bak` 备份时提示"存档损坏，将载入备份"并读备份；无备份时询问是否删除存档并重新开始（`013_UI_Load.rb:228–239`）。完整失败/恢复规则归 WP10 主规格。

## 6. 默认行为与配置变体

- **基线默认**：启动读取五类启动值；有存档显示继续选项；保存按 5.1 路径；设置与进度分开。
- **支持但未默认启用**：`SKIP_CONTINUE_SCREEN`（调试 + 非归档 + 配置三者同时成立时跳过菜单，直接新游戏/继续）；`.bak` 备份恢复路径。
- **配置/数据关联**：`GAME_VERSION`/`Essentials::VERSION` 随存档保存（版本兼容输入，WP10）；`MECHANICS_GENERATION` 与数据集组合对存档兼容的影响（U02/U03）。
- **未验证组合**：部分写入后的文件状态、备份恢复的真实路径、地图损坏分支、完整 Demo 启动（缺失地图/事件材料）。
- 参考快照行为、官方版本预期、未来目标分开标记；本包只记录第一类。

## 7. 边界、失败与未知

- 保存写入失败（IOError/SystemCallError）：仅 save_count 回退并返回 false；其余内存变更不回退（5.1）；文件状态未验证（可能部分写入）。
- 保存校验失败（InvalidValueError）：不在 IOError/SystemCallError 捕获集合内，save_count 不回退；此阶段尚未打开文件（5.1）。
- 存档无效：备份恢复或删除重开（5.3）；无备份时的删除确认流程（删除动作本身捕获 SystemCallError 并提示失败，WP10 引用）。
- 地图损坏（events 为 nil）：抛错无法继续（与缺图不同，4.1）。
- 读取时写回：转换后存档被重写（5.2，归 WP10）。
- 完整 Demo 启动流程未验证（缺失地图/事件材料，U01）。

## 8. 可复核性与静态场景

### 8.1 复核方式

| 事实 | 复核方式 |
| --- | --- |
| 持久值机制 | 阅读 `S/002_Save data/002_SaveData_Value.rb` |
| 持久值目录 | 阅读 `S/002_Save data/004_Game_SaveValues.rb`（17 项） |
| 启动/新游戏/继续 | 阅读 `S/003_Game processing/001_StartGame.rb`；`S/016_UI/013_UI_Load.rb:215–325` |
| 保存路径与边界 | 阅读 `S/003_Game processing/001_StartGame.rb:106–125`；`S/002_Save data/001_SaveData.rb:8–12, 57–60` |
| 读取写回 | 阅读 `S/002_Save data/001_SaveData.rb:43–50`（WP10 引用） |
| 上游顺序 | `S/999_Main/999_Main.rb:25–41`；`S/003_Game processing/001_StartGame.rb:21–27` |

### 8.2 静态推导场景（未运行，待运行验证）

| 场景 | 输入 | 推导预期 |
| --- | --- | --- |
| 无存档启动（普通） | 无存档文件 | @save_data = {}；仍显示菜单（新游戏/选项/退出等；语言候选 ≥2 时含语言项） |
| 无存档启动（调试跳过） | $DEBUG + 无 Game.rgssad + SKIP_CONTINUE_SCREEN | 跳过菜单直接新游戏 |
| 正常继续（两条件均不成立） | magic_number 一致且非 safesave | setMapChanged 恢复地图 |
| 正常继续（magic_number 不一致） | magic_number 不一致 | 重新 setup 地图；缺图时调试给选图入口（取消则退出）、非调试报错 |
| 正常继续（safesave 为真） | safesave 为真 | 重新 setup 地图（同上的缺图分支） |
| 地图损坏 | $game_map.events 为 nil | 抛"地图损坏，游戏无法继续"（与缺图不同） |
| 新游戏保留设置 | 有存档但选新游戏 | pokemon_system 与 game_system 保留读取（非强制重置）；进度值取新游戏值；stats 强制重置后会话数为 1 |
| valid? 缺键 | 存档缺某持久值键 | valid? 为假（不容忍缺键） |
| 键存在但类型错误 | 某键值类型不符 ensure_class | load 时抛 InvalidValueError（与缺键默认分支不同） |
| 保存 IOError | save_to_file 抛 IOError | save_count 回退 -1 并返回 false；safesave/magic_number/time_last_saved/锚点不回退；文件状态未验证 |
| 保存校验失败 | 某持久值类型不符 | 抛 InvalidValueError（不在 IOError 捕获内，save_count 不回退；此阶段尚未打开文件） |

## 9. 证据与来源（traceability）

- **本轮复核（2026-09-19）**：逐行阅读 `002_SaveData_Value.rb`（284 行）、`004_Game_SaveValues.rb`（127 行）、`001_SaveData.rb`（82 行）；`001_StartGame.rb` 全文（启动/新游戏/继续/保存/地图恢复）；`013_UI_Load.rb:215–325`（载入界面、无存档菜单、损坏/备份入口）；`999_Main/999_Main.rb:25–41`。
- **继承同基线既有记录**：E07（保存/迁移入口，本轮已扩展为登记目录）；E08（启动与状态入口）；E31（载入 UI 入口）。
- 全部静态证据；**无运行确认**。

## 10. 未决问题

1. 保存写入失败后的文件状态（部分写入/截断可能性，未验证）。
2. 备份恢复的真实路径与转换规则全集（WP10 主规格）。
3. 地图损坏分支与恢复行为（WP10）。
4. 完整 Demo 启动流程（缺失地图/事件材料，U01）。
5. 设置项全集（选项 UI 语义，归 WP65）。
6. frame_count 弃用字段的存档迁移（WP10）。

## 11. 状态与后续

- WP09 自身范围（第 1 节五项）已提取并自检；2026-09-19 经批次复审后完成 WP09-R01（保留/重置条件与 valid?/缺键分层）、WP09-R02（无存档入口与地图恢复分支）、WP09-R03（保存前后内存与磁盘边界）三项修订。（本行是当时送审记录；最新状态：经 2026-09-19 WP08–WP10 v2 复审通过，头部规格状态为 **Reviewed**（限定范围），以头部为准。）
- **WP09 完成 ≠ F03-01/F03-03 完成**：持久值的字段语义需领域包闭合，启动 UI 与失败/迁移需 WP10/WP65/WP77；Feature Matrix 按聚合规则分别显示。
- 后续包引用本文的持久状态规则时，不得把登记结构或存储格式当作未来框架的保存 API；发现与本文冲突的新证据时，先修订本文并通知受影响包。
