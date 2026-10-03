# WP05 规格：通知、扩展与插件

| 字段 | 内容 |
| --- | --- |
| 工作包 | WP05（通知/扩展和插件） |
| 关联功能 | F01-03（事件与可扩展菜单，D01）、F01-04（插件依赖与载入，D01） |
| 分类 | Generic Kernel（扩展机制）；机制名称与事件名是参考侧取证记录，不是未来事件总线或插件 API 设计 |
| 参考基线 | `reference/pokemon-essentials/` @ commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（WP01 固定） |
| 输入 | 证据包 E03（插件管理器、事件/菜单扩展点）、E08（启动顺序）；实际世界/菜单消费者 |
| 前置依赖 | WP02（配置）、WP03（内容身份），均已 Reviewed |
| 规格状态 | **ReviewPending（WP05 自身范围）**：2026-09-19 提交外部 review |
| 证据等级 | 全部为静态证据：已定位 / 静态确认 / 数据样本确认；**无运行确认** |

## 1. 目的、范围与非目标

**目的**：记录参考实现为游戏内容与工具提供的扩展行为约束——通知（事件订阅）、可扩展菜单和插件载入各自支持什么、按什么顺序、在什么条件下生效、失败时发生什么。后续包据此判断"某行为能否被扩展/覆盖/拦截"，而不是各自重新阅读扩展机制。

**范围**（WP05 自身声明范围，extraction-plan 第 2.1 节 (a) 类）：

1. WP05-A：通知机制（事件订阅、命名事件、内容处理器表）。
2. WP05-B：菜单扩展（选项注册、排序、可用条件、调用）。
3. WP05-C：插件元数据与依赖（格式、注册校验、依赖/冲突/循环处理）。
4. WP05-D：插件载入（发现、顺序、编译、执行、版本兼容）。
5. WP05-E：失败与边界（错误致命性、发布模式、无插件样本、与 WP07 诊断的关系）。
6. F01-03、F01-04 中属于 WP05 部分的状态更新。

**非目标**：

- 不设计未来事件总线、菜单系统或插件 API。
- 不提取各事件/菜单项的具体业务行为（归相应领域包，如步数效果归 WP61、菜单可见性归 WP65）。
- 不验证真实插件组合（当前快照无插件样本，U09）；不运行游戏或编译器。
- 不重复定义错误/诊断机制（WP07 主规格，本文引用）。

## 2. 概念与术语

- **通知（事件订阅）**：命名的游戏事件（如进入地图、玩家迈步、战斗开始/结束）允许注册回调，在事件发生时被依次调用。
- **内容处理器表**：按内容 ID（物种/特性/道具/招式）登记处理逻辑的表，支持精确匹配与条件回退（addIf）。
- **可扩展菜单**：菜单选项以数据注册（名称、排序、可用条件、效果），菜单本身按注册数据生成。
- **插件**：`Plugins/<目录>/` 下带 `meta.txt` 的脚本包；经依赖排序、编译、按序执行。
- **依赖/冲突/循环**：插件声明的 Requires/Exact/Optional/Conflicts 关系及其校验。
- 影响域编号 Dxx 见 module-map；证据状态五档定义见总览第 7 节。

## 3. WP05-A：通知机制

### 3.1 事件订阅原语（`S/003_Game processing/005_Event_Handlers.rb`，本轮逐行阅读）

| 原语 | 行为 |
| --- | --- |
| Event（回调列表） | `set` 替换全部回调；`+` 添加（**已存在则不重复添加**）；`-` 移除；`clear` 清空；`trigger` 依次调用全部回调，参数为（发送者, 参数数组），回调参数个数匹配时传完整参数；`trigger2` 恒传完整参数 |
| NamedEvent（命名回调） | 按键登记/移除回调；`trigger` 依次调用全部回调（完整参数） |
| HandlerHash（ID→处理器） | `add` 校验处理器类型（非 Proc/Hash/块则抛 ArgumentError）；**nil 或空 ID 被忽略**；查找未中返回 nil；`copy` 把处理器复制到其他 ID；`trigger` 返回处理器的返回值（无处理器为 nil） |
| HandlerHashSymbol（符号版） | 仅符号 ID；`addIf` 登记条件回退（精确未中时按登记顺序尝试条件处理器）；查找时非符号输入取其 `.id`；`trigger` 把符号作为首参传入 |
| 内容专用表 | Species/Ability/Item/MoveHandlerHash 为 HandlerHashSymbol 的空子类——为四类内容的效果提供各自的处理器表（效果族归 WP46–WP50 等战斗包） |

### 3.2 命名事件注册表（`006_Event_HandlerCollections.rb`）

- `EventHandlers.add(event, key, proc)`：按事件名 + 回调键注册；可按键移除/清空；`trigger(event, *args)` 调用该事件全部回调（事件未定义时不报错、无效果）。
- 文档化事件集（当前快照）：地图设置/进入/离开、每帧更新、玩家转向/迈步/可转移迈步/互动、训练家载入、野生物种选择/个体创建/战斗呼叫/战斗开始/战斗结束/野生战斗结束。
- **本轮统计**：注册调用 53 处（18 个事件名）、触发调用 35 处（19 个事件名），**均在文档化事件集内**；未发现临时新事件名。注意形似属性（如 Evolution 数据的 `on_trade_proc` 回调）不是本注册表的事件。
- 典型用法（`012_Overworld/001_Overworld.rb:70–83`）：按命名键订阅迈步效果（如 `:gain_happiness`）；`on_player_step_taken_can_transfer` 的消费者通过共享数组约定"已发生转移则跳过"。

## 4. WP05-B：菜单扩展

- `MenuHandlers.add(menu, option, hash)`：为指定菜单注册选项。选项数据（本轮样例核实，如 `016_UI/001_UI_PauseMenu.rb:133–141`）：`"name"`（显示名，可翻译或过程动态生成）、`"order"`（排序值）、`"condition"`（可用条件过程，返回假则不显示）、`"effect"`（选择效果过程）；其他函数键可经 `MenuHandlers.call(menu, option, function, *args)` 调用。
- `each_available`：按 `order` 排序（缺省按注册序号），过滤条件不满足的选项，依次产出（选项, 数据, 显示名）。
- 本轮统计：注册调用 202 处，覆盖暂停菜单、队伍菜单、Pokégear、选项、PC、调试菜单族（调试族占多数）；菜单内容由注册数据驱动，插件可增删选项。
- 与地图事件解释器的关系：菜单扩展是独立机制，不等于事件命令扩展（D04 领域，WP13）。

## 5. WP05-C：插件元数据与依赖

### 5.1 meta.txt 与注册（`S/001_Technical/005_PluginManager.rb:106–286, 406–467`）

- 每个插件目录须含 `meta.txt`；必需字段：Name、Version、Essentials（兼容版本列表）、Link、Credits；可选：Requires（任意/最低版本）、Exact（精确版本）、Optional（存在则最低版本）、Conflicts、Scripts。
- `register(options)`：逐字段校验（空名/版本/链接报错）；依赖校验——Requires 未安装报错、已安装但版本不足报错（附已装版本与更新链接）；Conflicts 双向校验（新插件声明冲突 + 已注册插件声明中是否含本插件）；重名报错。
- 版本比较 `compare_versions`：逐字符字母数字比较（"1.10" > "1.9"）。
- **错误处理**：`error(msg)` 输出"Plugin Error"到控制台与标准输出后 `Kernel.exit!`——**注册期错误一律终止进程**，不进入后续加载。
- `readMeta`：解析 meta.txt；脚本清单 = SCRIPTS 行 + 目录下全部 .rb（去重）；无 meta.txt 的目录被忽略。

### 5.2 依赖排序与循环

- `validateDependencies`：递归检测依赖环，成环报错（终止）。
- `sortLoadOrder`：按依赖关系交换排序（依赖先于使用方）；缺失非 Optional 依赖报错；Optional 依赖缺失可跳过。
- `getPluginOrder`：读取全部插件目录的 meta，校验必需字段与重名，再验证依赖、排序。

## 6. WP05-D：插件载入

### 6.1 发现与编译

- `listAll`：仅调试模式、非发布包（无 Game.rgssad）、Plugins 目录存在时返回插件目录列表——**发布模式下插件整体不加载**。
- `needCompiling?`：调试模式下满足任一即编译——`$full_compile`、`Data/PluginScripts.rxdata` 缺失、按住 SHIFT/CTRL、任一脚本或 meta.txt 新于 PluginScripts.rxdata。
- `compilePlugins`：按排序结果把各插件脚本压缩序列化写入 `Data/PluginScripts.rxdata`。

### 6.2 执行与版本兼容

- `runPlugins`（启动顺序：核心消息 → **插件** → 编译检查 → 初始化，`999_Main/999_Main.rb:25–41`，WP03/WP04 已登记）：
  1. 需要则先编译；随后读取 PluginScripts.rxdata。
  2. 插件的 Essentials 兼容列表不含当前版本时**警告但照常加载**。
  3. 逐插件 `register`（依赖/冲突校验在此生效）。
  4. 逐脚本以插件标记的文件名 eval 执行；**任一脚本异常 → 格式化错误（`pluginErrorMsg`）后终止进程**。
- 插件运行**早于**编译检查：插件可能先修改数据/规则，随后编译检查再处理（WP04 主规格，引用）。
- 发布边界：注释明确 Plugins 目录应在发布时删除；发布包（Game.rgssad 存在）跳过插件发现与编译。

## 7. WP05-E：失败与边界

| 失败/边界 | 行为 |
| --- | --- |
| 注册期错误（字段、依赖、冲突、循环、重名） | 输出错误并终止进程（`Kernel.exit!`） |
| 载入期脚本异常 | `pluginErrorMsg`：格式化异常、追加写入 `errorlog.txt`、打印（可按 Ctrl 复制），随后终止进程 |
| Essentials 版本不匹配 | 仅警告，照常加载 |
| 无 Plugins 目录/无 meta.txt | 跳过对应插件；无插件时正常继续（"No plugins found"） |
| 发布包 | 插件发现/编译整体跳过 |
| 真实插件组合 | **当前快照无插件样本（U09 保持开放）**；静态检查器行为不证明真实组合有效 |

错误与诊断的共用面（`errorlog.txt` 写入、控制台输出）归 WP07 主规格，本包引用，不重复定义两套错误机制。

## 8. 默认行为与配置变体

- **基线默认**：调试模式下自动发现、按需编译、按序加载插件；版本不匹配仅警告；无插件时正常启动。
- **支持但未默认启用**：`$full_compile` 强制编译；SHIFT/CTRL 手动触发编译；`optional_exact` 依赖形式（仅注册 API，meta.txt 无法表达，源码注释注明）。
- **未验证组合**：真实插件组合、插件对编译/数据的影响（U09）、发布包行为（无 Game.rgssad 材料）。
- 参考快照行为、官方版本预期、未来目标分开标记；本包只记录第一类。

## 9. 可复核性与静态场景

### 9.1 复核方式

| 事实 | 复核方式 |
| --- | --- |
| 事件订阅原语 | 阅读 `S/003_Game processing/005_Event_Handlers.rb` |
| 命名事件集与注册表 | 阅读 `S/003_Game processing/006_Event_HandlerCollections.rb` |
| 事件/菜单使用规模 | 在 `S/` 检索 `EventHandlers.add/trigger`、`MenuHandlers.add` 计数 |
| 菜单选项结构 | 阅读 `S/016_UI/001_UI_PauseMenu.rb:133–141` |
| 插件注册与依赖 | 阅读 `S/001_Technical/005_PluginManager.rb:106–286` |
| 插件载入流程 | 同文件 469–649 行；启动顺序 `999_Main/999_Main.rb:25–41` |

### 9.2 静态推导场景（未运行，待运行验证）

| 场景 | 输入 | 推导预期 |
| --- | --- | --- |
| 重复回调 | 同一 Event 两次 `+` 同一过程 | 不重复添加；触发时只调用一次 |
| 空 ID 注册 | HandlerHash.add(nil, proc) / add("", proc) | 被忽略；查找返回 nil |
| 条件回退 | HandlerHashSymbol 精确未中但有 addIf 条件命中 | 返回条件处理器；无命中返回 nil |
| 依赖版本不足 | 插件 A Requires B 2.0，已装 B 1.0 | 注册期报错并终止（附已装版本与更新链接） |
| 依赖环 | A 依赖 B、B 依赖 A | 循环检测报错并终止 |
| Optional 缺失 | 插件声明 Optional 依赖且未安装 | 跳过该依赖，正常加载 |
| 版本不匹配 | 插件 Essentials 列表不含当前版本 | 警告后照常加载 |
| 脚本异常 | 某插件脚本执行抛错 | pluginErrorMsg 记录 errorlog.txt 并终止进程 |
| 发布模式 | Game.rgssad 存在 | 插件发现与编译整体跳过 |
| 菜单条件 | 选项 condition 返回假 | `each_available` 不产出该选项；order 缺省按注册序号 |

## 10. 证据与来源（traceability）

- **本轮复核（2026-09-19）**：逐行阅读 `005_Event_Handlers.rb`（298 行）、`006_Event_HandlerCollections.rb`（123 行）、`005_PluginManager.rb`（664 行）；统计 EventHandlers/MenuHandlers 使用点；样例核实 `001_Overworld.rb:70–83`、`001_UI_PauseMenu.rb:133–141`、`004_Item_Phone.rb`（菜单/电话注册表外事件辨析）；启动顺序 `999_Main/999_Main.rb:25–41`。
- **继承同基线既有记录**：E03（扩展入口/依赖处理，本轮已全文核实）；E08（启动与状态入口）。
- 全部静态证据；**无运行确认**。

## 11. 未决问题

1. 真实插件组合及其对数据/规则/编译的影响（U09）。
2. 发布包（Game.rgssad）下的实际行为（无材料）。
3. 各事件回调的具体业务语义（归相应领域包）。
4. HandlerHashEnum（注释标记 Unused）是否有实际消费者——本轮未见使用点。
5. 插件错误终止进程前的状态一致性（未运行）。

## 12. 状态与后续

- WP05 自身范围（第 1 节六项）已提取并自检，状态 **ReviewPending**，提交外部 review。
- **WP05 完成 ≠ F01-03/F01-04 完成**：F01-03 的各事件/菜单语义需领域包闭合，F01-04 的真实插件组合需 U09 材料；Feature Matrix 按聚合规则分别显示。
- 后续包引用本文的扩展机制时，不得把事件名、选项结构或插件目录约定当作未来框架的扩展 API；发现与本文冲突的新证据时，先修订本文并通知受影响包。
