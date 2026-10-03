# WP04–WP07 v2 批次复审

日期：2026-09-19。Reference/Audit 侧独立 reviewer。R = `reference/pokemon-essentials/`；S = `R/Data/Scripts/`。本报告与快照是内部审查材料，不是 WP80 sanitized 产物。

**结论：REQUEST_CHANGES。原 12 项中 6 项关闭、6 项部分关闭；BATCH-C01/C02 关闭。四包仍分别有剩余问题，暂不进入 WP08–WP10。**

本轮认可已经正确的修订；剩余项均沿用原编号，不要求重新核对已经关闭的整组范围。WP01–WP03 的限定 Reviewed 继续有效。

## 1. 实际对象与版本

工作区 `/Users/dingshinn/Desktop/pokemon-framework-reference/`。固定参考 HEAD 实测仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，describe 为 `v21.1-23-g8c5911e4`。

| 对象 | SHA-256 | 字节数 |
| --- | --- | ---: |
| WP04 v2 | `ffe83e59158e5bc25ef318854939df236fc68770beb8540aa6858521c8a2227c` | 20261 |
| WP05 v2 | `d969f23e5d97e75e56717849ec79731ec0985e8a9b594c424b2f337515d29071` | 17026 |
| WP06 v2 | `04cd172fc730e56df003409e1e96826e6623d439e7e746c68156e52f373c611f` | 20867 |
| WP07 v2 | `e8300872d0963e134114457342b4bfc70eb1382c4a9e5a36854ded988c10a3a8` | 16562 |
| Feature Matrix | `563cff0efb8c8a8a478f35ad25274deb94e30990b127b2b6bc045370bcea056e` | 31051 |
| manifest | `fac345649111b18a41bf49a78b5eada8878ea790d274c48c7e01f4955fab0c12` | 15007 |

WP04–WP07 对应 `specs/kernel/wp04-pbs-lifecycle.md`、`wp05-events-extensions-plugins.md`、`wp06-time-random-steps-stats.md`、`wp07-diagnostics-files-http.md`；以下行号均针对本表哈希的固定版本。

当前 manifest **27 项完整哈希和字节数全部匹配**。额外核对并固定上轮报告与提示词，均与上轮 final-checks 记录一致；合计固定 31 项输入。既有文件仅四份规格、矩阵和 manifest 有变化，WP01–WP03 未修改。

矩阵实际有七行备注修订，另将 F02-02 的送审范围文字从“触发/顺序/写回/失败”改为“触发/解析/写回/失败”；其状态等级仍为 ReviewPending，未升级。这比交付摘要的“仅补充修订说明”更精确，不作为新增阻塞项。

记录：[input-manifest.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-2026-09-19/input-manifest.json)、[changes-from-v1.diff](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-2026-09-19/changes-from-v1.diff)。

## 2. 实际检查与限制

- 按上轮 12 项问题阅读实际修订、场景和关联记录，重点追踪新增结论及仍有争议的消费者/依赖；没有重开全仓或旧包审查。
- 重新核对活跃分节/记录解析、BerryPlant 和 Metadata 的 schema/编译校验、插件 metadata 缺省与执行、HandlerHashSymbol 触发、统计实际写入、HTTP 返回及异常包装。
- 对上轮 77 个源文件复算完整性，均未变；另核 Safari 与场地动作两份实际统计消费者，合计 **79 个文件与固定提交 Git blob 一致**。这不是 79 文件全文语义审查。只读 Git 查询均退出 0；普通状态为空，ignored 仍为 `.DS_Store`、`PBS/.DS_Store`。见 [source-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-2026-09-19/source-checks.json)。
- sample/shuffle 的复算为 53 个匹配行、55 次出现、无整行注释命中；两种单位须区别。本轮不将其作为新阻塞项，结果见 [sample-shuffle-check.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-2026-09-19/sample-shuffle-check.json)。
- **未运行游戏、Ruby、编译器、参考表达式或网络请求**；下列反例与验收为静态推导。只写本轮独立 review 目录，未修改提取方规格、矩阵、manifest 或旧报告。

## 3. 原问题逐项处置

| 编号 | 处置 | 已通过或剩余范围 |
| --- | --- | --- |
| WP04-R01 | 关闭 | 提示拒绝与自动条件、Reset/SystemExit、删除尝试及早期清单未建立已区分。日志失败的通用限制由修订后的 WP07 提供。 |
| WP04-R02 | 部分关闭 | 已增加活跃路径、大写可选模式和发现/固定路径交界；常规/未知属性、新身份场景及新增依赖边仍有错误或缺口，见 §4。 |
| WP04-R03 | 关闭 | 主动导出调用者、通用/专用写出、无条目无路径与不保证旧文本往返已补。 |
| WP05-R01 | 关闭 | 源发现、编译、产物消费三阶段正确；发布消费、空产物/读取失败已分开。 |
| WP05-R02 | 部分关闭 | 版本比较、缺键/空值、optional_exact 已修正；新校验表仍把省略 Scripts 行当成缺少解析后键，见 §5.1。 |
| WP05-R03 | 部分关闭 | 回调展开、同键覆盖、校验先后及注册键范围正确；trigger 首参仍错误地保证符号类型，见 §5.2。 |
| WP06-R01 | 关闭 | 电话秒节流/delta/守卫及游戏时间锚点、离线限制已补。 |
| WP06-R02 | 关闭 | 参数/待播种子组合和提前返回前已清空/播种的状态已补。 |
| WP06-R03 | 部分关闭 | sample/shuffle、初始化形态和通用计步机制已补；统计更新目录仍未完成，且新表将现成脚本错误归为缺失事件，见 §6。 |
| WP07-R01 | 部分关闭 | GET/POST 与基础/便利入口主要分层正确；第 115 行可区分性总结反向，见 §7.1。 |
| WP07-R02 | 关闭 | 主要捕获集合、EISDIR 差异、Char 返回形态、Open 分支和 RTP.eachPath 已区分。 |
| WP07-R03 | 部分关闭 | 调试/非调试、EventScriptError 和日志失败已补；新场景的 Reset/SystemExit“任意阶段”仍超出适用入口，见 §7.2。 |
| BATCH-C01 | 关闭 | 两处旧原件大小已与实际字节一致。 |
| BATCH-C02 | 关闭 | 22 项写出、注释命中、rand 的正则与计数单位已修正，不再将文本数等同运行调用数。 |

## 4. WP04-R02 [P2] 活跃解析目录还缺关键分支，新增依赖链混淆依据

**被审位置**：WP04@ffe83e59:77–106、205–209。

### 4.1 属性处理与新身份仍未准确描述

上轮要求的“未知属性/普通重复属性”没有补入，新增第 208 行却写成“节名未定义或重复，通用报错/专用覆盖”，把**新定义身份、外键不存在、同一身份重复、同节属性重复**混成一种情形。

实际通用路径：

- `S/021_Compiler/001_Compiler.rb:95–134` 中，非 `^` 的同名属性后值覆盖前值；`^` 属性累加。
- `S/021_Compiler/002_Compiler_CompilePBS.rb:30–60` 仅消费 schema 列出的键。合法键值语法中的未知属性不会因此触发通用未知字段错误，而是未被这个通用求值循环消费。
- 同一文件的通用流程先校验再注册：一个合法、此前不存在的普通道具身份可以成为新记录；不能把“新身份未存在”当成“未定义枚举引用”拒绝。存在性检查用于拒绝已经登记的重复身份。专用入口分别保留其约束。

**最小修订**：补上述属性级规则；将第 208 行拆成新身份定义、重复身份、未知引用三个明确场景。保留已有 WP03 锚点和本轮可选/重复模式说明，不重写全部领域 schema。

**静态验收**：同一合法道具节内 Name 两次→后值生效；一个语法合法但不在该 schema 的属性→通用流程不消费；一个合法且尚未登记的新道具 ID→可登记；同 ID 的第二个通用节→拒绝；未知 Move 引用→枚举拒绝。`^` 累加作为对照。其他必需条件均设为合法，不能用无关错误遮盖该分支。

### 4.2 两条新增依赖边没有所述 schema 证据

- 第 102 行称 **BerryPlant 的 Item 枚举**：`S/010_Data/002_PBS data/007_BerryPlant.rb:13–18` 的 SectionName 为普通符号模式，其余为数值，没有 Item 枚举。`002_Compiler_CompilePBS.rb:268–278` 的条目/全量校验也为空。Item 与 BerryPlant 的运行期关联、调度注释，与“编译校验依赖 Item 枚举”必须区分，不能由编译顺序推成此边。
- 第 105 行 **TrainerType → Trainer → Metadata** 误造了 Trainer → Metadata。`016_Metadata.rb:21–34`（同 PBS data 目录）有 StartItemStorage 的 Item 引用；`017_PlayerMetadata.rb:12–23` 引用 TrainerType；`compile_metadata:1070–1143` 分别处理二者。它们不是经 Trainer 队伍数据串成的一条链。

**影响**：后续包会错误判断编译前置条件，错误拒绝内容或因无必要依赖而阻塞。

**最小修订及验收**：将每条边标为编译解析/校验依赖、调度先后或运行期关联，并附相应定位。拆开 TrainerType→Trainer 与 TrainerType→PlayerMetadata、Item→Metadata.StartItemStorage。BerryPlant 的普通符号身份不能被叙述为已通过 Item 枚举校验。不要求绘制未来架构或穷尽全部领域关系。

## 5. WP05 的两处剩余项

### 5.1 WP05-R02 [P2] 省略 Scripts 行不等于触发缺 Scripts 错误

**位置**：WP05@d969f23e:79；manifest 的本轮 R02 说明及交付摘要也重复此表述。

**证据**：`S/001_Technical/005_PluginManager.rb:457–464` 在 readMeta 中给 scripts 建立默认空数组，再追加递归发现的脚本；getPluginOrder 在 536 行调用此解析器，541 行只判断解析后的键值是否为假。普通流程中，作者省略 Scripts 行不会因此缺少该键；空数组也不触发此判断。

**影响**：作者会被告知一个实际并非必填的清单必须填写。只列出下游 guard，仍没有核对输入如何被上游归一化。

**最小修订**：区分“代码有缺少解析后 scripts 值的防御检查”与“meta.txt 必须写 Scripts 行”。恢复自动发现/缺省数组的行为说明；其他已修正元数据与版本规则保留。

**静态验收**：Name/Version 等其他条件合法；省略 Scripts 但目录含脚本→自动收集；省略 Scripts 且目录无脚本→得到空脚本列表，不因缺该行触发 541 行错误。空脚本插件条目也不能与整个预编译产物为空混为一谈。无需创建或执行插件。

### 5.2 WP05-R03 [P2] trigger 首参仍写成一定是符号

**位置**：WP05@d969f23e:53 最后一句。

**证据**：`S/003_Game processing/005_Event_Handlers.rb:192–195` 仅在非符号对象响应 id 时取 id，然后把所得键传给处理器；它不执行强制转符号。注册/查找的修订已说明其他真值键可原样保留，但同一行仍写“trigger 把符号作为首参传入”，构成冲突。

**最小修订及验收**：改成“把按上述规则归一化后的键作为首参，类型不保证为 Symbol”。以字符串键登记并触发，首参仍为该字符串；对象键则以实际 id 归一化结果为准。只需修正此处及相应场景，不重做回调机制。

## 6. WP06-R03 [P2] 代表性分组没有闭合统计目录，U01 还覆盖了实际存在的写入

**位置**：WP06@04cd172f:86–102、190–192、196–197。

第 90 行表头仍是“代表字段”“实际更新入口（举例）”；多数行仅给 E 编号，明确注明更新点未逐一枚举，第 192 行继续把各统计字段更新入口整体交给 WP09/WP79。因此，它没有满足上轮要求的本包更新/恢复清单。可以按字段组紧凑表达，但必须可核对每个声明字段的归属和更新证据；不能用“74”总数证明覆盖。

新增第 99 行将整组特殊统计标为“由道馆/四天王/名人堂事件写入，U01 待证”，但该行包含以下**当前源码已有的更新**：

| 字段 | 已存在的静态更新证据 |
| --- | --- |
| safari_pokemon_caught | `S/018_Alternate battle modes/001_SafariZone.rb:150–153`：捕获结果分支累加 |
| most_captures_per_safari_game | 同段：以本次捕获累计与原纪录取最大值 |
| bug_contest_count | `S/018_Alternate battle modes/002_BugContest.rb:192–195`：开始会话时增加 |
| bug_contest_wins | 同文件 205–216：结束处理且名次为第一时增加 |

这些入口是否在缺失 Demo 中可达仍待证，但**写入机制存在且可读**不是 U01 阻塞。类似地，`waterfalls_descended` 是真实声明字段，更新在 `S/012_Overworld/004_Overworld_FieldMoves.rb:910` 及 `004_Game classes/008_Game_Player.rb:157`；当前场地动作的“各 count 及 battles”省略表述不能清楚覆盖它。

**影响**：把可以现在审查的机制推成缺失材料，也使累计、最大值、数组、时长与距离混在不完整分类中，后续无法判断还缺什么。

**最小修订**：补紧凑附表或可展开的字段组目录。对全部 74 个声明字段列明确成员归属，区分单位/形态、初始化、更新规则类别、实际源码入口、持久化/重置交界与证据等级。多字段共用一个入口可合并，不需要 74 份长篇规则或展开各领域玩法。只有确实依赖缺失事件的写入才标 U01；不要把一组字段统一标待证。WP09 管保存生命周期、WP10 管迁移、WP79 检查覆盖，均不能替代这份基础清单。

**静态验收**：声明集合与清单成员集合一致、无漏项；上述四个特殊统计改为“脚本更新静态确认，Demo 可达未证”；waterfalls_descended 有归属；累加量、最大值、数组、时间及派生 getter 分开。若该清单尚未完成，应诚实登记 WP06 的 Partial 范围，不继续声称“自身目录已补齐”。

随机入口扩充和通用计步的原问题已实质修正，本项不要求重做它们；领域概率公式、完整电话/设施规则仍按既有前向引用处理。

## 7. WP07 的两处剩余项

### 7.1 WP07-R01 [P2] 汇总表把 HTTP 失败可区分性写反

**位置**：WP07@e8300872:115。

前面的第 79–82 行分层基本正确，但汇总表却写“基础入口仅 HTTPLite 调用失败可区分；其余不可区分”。实际 `S/001_Technical/002_Files/003_HTTP_Utilities.rb:28–33,45–50` 将被捕获的宿主请求异常变为空字符串，与非 200 及成功空正文可以相同；写文件异常才可能从基础入口传播。

**影响**：与本轮刚修好的异常边界相反，会错误指导调用方识别失败原因。

**最小修订及验收**：同步汇总表与主表：请求异常、非 200、成功空正文可同为 `""`，不能据此区别；基础写入异常可以传播，便利包装按其捕获范围处理；非 Hash 响应原样返回。用这四类结果对照即可，不重审协议或联网。

### 7.2 WP07-R03 [P2] Reset/SystemExit 的原样传播不能覆盖“任意阶段”

**位置**：WP07@e8300872:90、159；与 WP05 插件脚本异常相交。

原样传播适用于 `pbCriticalCode`（`003_Errors.rb:81–89`）及 Compiler.main（`001_Compiler.rb:1103–1105`）等明确分支。插件执行却在 `005_PluginManager.rb:634–640` 捕获 Exception，包含插件脚本抛出的 Reset/SystemExit，并进入 pluginErrorMsg/退出路径；它没有相同的原样重抛特判。

**影响**：新增场景“Reset/SystemExit，任意阶段→原样传播”又引入跨入口统一承诺，与本批 WP05 的实际捕获范围不一致。

**最小修订及验收**：将第 90、159 行限定为相关包装/编译入口，并补插件执行入口的对照。相同 Reset 信号到达 pbCriticalCode/Compiler.main 与从插件脚本内部抛出，静态路径不同；若插件诊断写日志自身失败，继续沿用已有“后续退出/输出不能保证”的限制。无需执行插件或模拟宿主重启。

## 8. 保留范围、状态与下一步

本轮未增加与旧问题无关的新阻塞项。剩余六项都属于原项未完成部分或修订引入的局部回归。已关闭的六项及两项维护问题不要求再次全文自检；后续只核对相关改动是否回归。

WP01–WP03 的限定 Reviewed 不变。WP04–WP07 暂不升级 Reviewed；WP06 的自身清单未完成部分应与矩阵/摘要如实一致。U01–U10 保持已有处置；“源码更新机制已知”与“缺失 Demo 中可达”分开，不要求凭空关闭未知。

下一轮集中处理 §4–§7，尤其让 WP04 的解析/依赖表和 WP06 的统计目录真正落到可核对产物，而非继续增加泛化说明。各包仍独立判定，修完的包可以先通过。本轮暂不启动依赖这些范围的 WP08–WP10。

已提供 [针对剩余六项的修订提示词](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-2026-09-19/revision-prompt.md)。本轮停止于审查报告及提示词交付；实际输入稳定性与交付哈希见 [final-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-2026-09-19/final-checks.json)。
