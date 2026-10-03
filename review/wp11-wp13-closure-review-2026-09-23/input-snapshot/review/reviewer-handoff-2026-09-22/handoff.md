# 独立 Reviewer 交接（2026-09-22）

本文件接替 `review/reviewer-handoff-2026-09-19/handoff.md` 的当前状态入口。旧件完整保留，供历史审计；其中“尚未发现 v2”和 WP11–WP13 首轮待办已过时。本文件是 Reference/Audit 侧交接，不是规格或 WP80 sanitized 材料。

## 0. 接手后首先要知道

**WP01–WP12 各自限定范围已审通过；WP13 仅余 WP13-R05 的一个定位分支遗漏。** 不需要重新审 WP11–WP13 首版或再次处理全部 10 个原问题。

本会话实际执行了两轮后续复审：

| 时间/被审版 | 报告 | 结果 |
| --- | --- | --- |
| 2026-09-20 开始、09-21 完成；v2 | `review/wp11-wp13-recheck-2026-09-20/report.md` | 三包 REQUEST_CHANGES；关闭 WP11-R01、WP13-R03、WP11-C01；剩余 8 R 项 |
| 2026-09-22；三份主规格 v3、命令矩阵 v3、路线附表 v2 | `review/wp11-wp13-recheck-v3-2026-09-22/report.md` | WP11/WP12 PASS_SCOPED；WP13 REQUEST_CHANGES；上轮 8 项中关闭 7 项，仅 WP13-R05 的单一分支待补 |

此前 `review/wp11-wp13-review-2026-09-19/report.md` 的首轮检查，是第一次交接时读取和继承的既有材料，不能冒称本会话重新完成其 122 文件检查。最新一轮自身比对了 11 个参考文件固定 blob，并定点核对修订；检查深度各自分开。

**审查结论与磁盘登记分开**：交接固定时，WP11/WP12/WP13 的头尾与矩阵仍为 ReviewPending。WP11/WP12 已获得本轮限定通过，提取方可回填 Reviewed；reviewer 没有代为修改。WP13 仍不可登记通过。交接后若文件变化，以实际哈希/diff 为准。

最优先读取：

- [最新 v3 审查报告](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp11-wp13-recheck-v3-2026-09-22/report.md)
- [有限修订与回填提示词](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp11-wp13-recheck-v3-2026-09-22/revision-prompt.md)
- [本交接的实际工作区核对](/Users/dingshinn/Desktop/pokemon-framework-reference/review/reviewer-handoff-2026-09-22/workspace-checks.json)
- [完整当前哈希表](/Users/dingshinn/Desktop/pokemon-framework-reference/review/reviewer-handoff-2026-09-22/current-hashes.tsv)

## 1. 唯一行为待办与下一轮边界

### WP13-R05 [P2]：同轴超过两格的回退

被审主文档 `specs/overworld/wp13-map-events-npc-followers.md`，完整 SHA-256 `1ec410b6d084d841ba0701e6089d6c7b1e11a4eda2f2e6294a21ce1dce3d5f97`，第 120–124 行，重点 123。

v3 已正确描述同轴一格、同轴两格的四种许可结果以及非同轴 (1,1) 定位，却把剩余直接定位分支限定成“非同轴”。固定源码 `Data/Scripts/004_Game classes/010_Game_Follower.rb:91–110` 的回退涵盖所有其他非重合目标，包括同轴距离大于两格。

最小验收：人工有效地图 20×20，同图、非强制路线、非即时，无桥/岩架/其他干扰；跟随者 (5,5)，向右领队 (9,5)，身后目标 (8,5)。应直接定位到 (8,5)。只需补完整回退条件和这个场景；既有两格许可分支及 (1,1) 例不应改变。

这属于原 R05 修订直接造成的分支遗漏，编号不变。不要重审已关闭的 R01/R02/R03/R04，不扩成完整跟随宝可梦系统，不要求运行实际地图。

### 非阻塞 WP12-C01 与状态回填

WP12 `7f1979bd` 第 282 行仍将“动画/状态置位细节”笼统留给 WP59；正文第 172–173 行已完成运动状态提交/清理。本轮接受正文，可随 Reviewed 回填把未决范围缩至完整资格、动画/媒体及其他真正未提取效果，不再称本包仅登记入口与守卫。

该维护不阻塞 WP12，不要求再做全文审查。回填时保留本报告被审哈希、新哈希及差异；状态变更产生新哈希并不使旧行为结论自动失效。

下一轮若仅收到回填，核对管理性变化后等待 WP13 修订；若收到实际 WP13 修订，直接复审最后一项和直接传播。若全部闭合，可依计划发下一批提示词，通常 3–4 包、可 2–5 包；本交接未预先批准 WP14 或任何下一批产物。

## 2. 当前版本锚点

| 产物 | SHA-256 | 字节数 |
| --- | --- | ---: |
| WP11 v3 | `df39a9e5210b4fdd3ff63f27a76b82fbb0ed37d13c6e6bd53e4160e5b36c1f36` | 19521 |
| WP12 v3 | `7f1979bd4734cc2f878117b934589f1e5ccf26754984d703d3e14701f9cee974` | 31489 |
| WP13 主文档 v3 | `1ec410b6d084d841ba0701e6089d6c7b1e11a4eda2f2e6294a21ce1dce3d5f97` | 27706 |
| WP13 主命令矩阵 v3 | `ab69bc87c97b805f1a2f0848a35e9b86aa8b582f8128553038f2487b85245de5` | 17561 |
| WP13 移动路线附表 v2 | `f637f1c32db9fd59e93b0b3c81f33637f22e715dfeaaabb74f5fad6a71db12c7` | 8315 |
| feature-matrix | `55352c019b90f84411f8dc54a6ab890321394b86cfb06add89ef660fdd1f2bce` | 33653 |
| manifest | `9c49398392e00bc6d7e9c8f5da2c00bf8c6a27770085626248e18c9736914c38` | 27523 |

五份产物路径分别为 `specs/overworld/wp11-map-topology-transfer.md`、`wp12-terrain-movement-vehicles.md`、`wp13-map-events-npc-followers.md`、`wp13-interpreter-command-matrix.md`、`wp13-move-route-matrix.md`。当前 manifest 为 `planning/review-manifest-2026-09-19.md`，文件名日期不是最后修订日期。

最新报告的检查：61 项完整 manifest 哈希/大小全部匹配；67 项固定输入；相对 v2，既有输入变化只限五份规格/附表、矩阵、manifest，另有新的回应/diff。五份提交 diff 均可从旧文本精确重建新产物。旧审查 artifacts 无改写。

总控稳定锚点：AGENTS `41cea9c6`；repository-overview `1ca34f44`；module-map `32eab70d`；extraction-plan `c1735877`。WP01–WP10 当前字节保持上一交接哈希；完整值见本目录 current-hashes.tsv。

## 3. 身份、权限与 clean-room 边界

你是独立 reviewer，提取/修订和状态登记由另一个模型负责。用户摘要和提取方“已全部处理”声明仅作索引，不能替代实际文件和证据。

- 默认只读源码、规格、计划、manifest、工具及旧 review。只在 review 下新建本轮报告、检查、快照、diff、提示词；不覆盖旧件，不代改提取方产物。
- 不运行游戏、参考 Ruby、解释器/事件脚本、编译器、转换器、插件、参考表达式或真实网络请求；不操作真实地图/存档。可以用安全的自有文本、哈希、索引和独立数值检查；已有工具先读再考虑执行，不能变成参考代码执行器。
- reference 只读；不 fetch/pull/checkout，不以默认分支或网上新版本替代固定提交。
- 不创建 TypeScript 包/API、MZ 插件、战斗实现或引擎适配器。只描述可观察规则、状态、前后条件、数学关系、兼容边界和静态场景。
- 源码路径及必要符号可作内部审计定位；不复制长段实现，不按源码逐行改写伪代码，不照搬类层级/模块结构。
- reviewer 与提取方都在 Reference/Audit 侧；未来实现 Agent 只能接收最终经 WP80 清理批准的规格，不能把这些内部报告、reference 或看过源码的会话历史当成 sanitized 输入。
- 不自行创建并行 Agent、新任务，或向其他模型发送消息；用户将在另一个会话安排接手。

## 4. 基线与材料限制

工作区 `/Users/dingshinn/Desktop/pokemon-framework-reference/`。R = `reference/pokemon-essentials/`，S = `R/Data/Scripts/`，P = `R/PBS/`。

固定仓库 Maruno17/pokemon-essentials；commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；describe `v21.1-23-g8c5911e4`；默认机制世代 8。

最新检查普通 Git 状态为空，ignored 为 `.DS_Store`、`PBS/.DS_Store`。普通 clean 不等于没有额外 ignored 文件。Git blob 一致证明字节身份，不等于全文语义验证或运行成功。

该仓库不是完整发行包或可运行 Demo。完整地图、公共事件、系统/动画、媒体、插件样本不足。Game.exe、字段、函数定义、文本命中不证明运行成功、NPC 可达、收费奖励或组合兼容。本提交不等于未改动 v21.1 发布包；新增材料必须单独登记来源和基线。

最终产品设想为可独立设计的怪物收集 RPG 框架，MZ 为首先适配目标，Pokémon 为首套规则内容；Showdown 是候选可插拔后端。当前阶段不能据这些设想预设架构或省略战斗需求，也不能宣称后端已支持。

## 5. 已通过范围与历史定位

下列为继承/本轮限定结论，均非整游戏功能或运行通过：

| 包 | 限定通过概要 | 权威报告 |
| --- | --- | --- |
| WP01 | 固定基线、材料缺口、来源与证据范围 | WP01 历轮及 `review/wp02-closure-review-2026-09-19.md` |
| WP02 | 配置词典、默认/派生、候选材料及输入发现边界、附表 | `review/wp02-closure-review-2026-09-19.md` |
| WP03 | 内容身份、注册/查询/枚举、schema 锚点、字段责任 | `review/wp03-closure-review-2026-09-19/report.md` |
| WP04 | PBS 发现、已述解析/校验、触发/写回/失败副作用 | WP04–WP07 v3 及闭合报告 |
| WP05 | 通知/菜单、插件元数据/依赖、发现/编译/产物消费 | 同上 |
| WP06 | 时间/随机/计步、有限种子、74 字段及已述统计/保存交界 | `review/wp04-wp07-closure-review-2026-09-19/report.md` |
| WP07 | 已述文件/HTTP/诊断分层与失败前提 | WP04–WP07 v3 及闭合报告 |
| WP08 | 文本域、消息层、载入/查找/空译/格式化、作者工作流 | `review/wp08-wp10-closure-review-2026-09-19/report.md` |
| WP09 | 默认保存登记、启动/新游戏/继续、地图恢复、内存/磁盘边界 | WP08–WP10 recheck，后续闭合继承 |
| WP10 | 默认转换目录、筛选/顺序、旧入口、备份/写回/恢复及反例 | `review/wp08-wp10-closure-review-2026-09-19/report.md` |
| WP11 | 已述地图身份、连接/单位、转移/通知、实例/坐标与失败阶段 | 本次 v3 报告，尚待磁盘 Reviewed 回填 |
| WP12 | 已述地形/通行、运动统计时点、载具及水上交界/进入地图骑行 | 本次 v3 报告，尚待磁盘 Reviewed 回填 |

WP13 原 5 R 项中，R01/R02/R03/R04 已关闭；R05 只保留 §1 的分支。原首轮三包 10 R 项累计 9 项关闭。WP11-C01 已关闭；WP12-C01 是本次非阻塞维护。

重要已校准事实供后续辨认，不要求重新证明：96 个主命令代码，28 dummy/2 标记/66 其他入口；10 个旧误报命令均已纠正；路线目录 0–45；401 与 655 分别为上游消费的续行，相邻 101 不被吞并而相邻 355 可合并；209 不设等待，210 才设；105 有双推进；失联只清事件上下文，不清既有命令列表；玩家 bump 可使不可跳过路线推进；仅终止项的强制路线可能不清 forcing。这些是固定快照事实，不是未来版本硬编码真值。

更早各轮详细校准（WP03 查询副作用、插件版本比较、保存转换等）见 [旧交接的历史章节](/Users/dingshinn/Desktop/pokemon-framework-reference/review/reviewer-handoff-2026-09-19/handoff.md) §5–6 及所链接原报告。读取旧件时只继承历史，不覆盖本文最新待办。

## 6. 规划和状态协议

权威恢复顺序：AGENTS → repository-overview → module-map → feature-matrix → extraction-plan（尤其 §2.1）→ 当前 manifest/实际包产物/最新报告与回应。旧哈希和 mtime 都不能替代当前内容检查。

18 个领域用于导航，113 个初始高层功能组不等于最终规则总数或架构。原计划共有 **87 个可执行 WP**，不是存在 WP87：主号 WP01–WP80，WP47/67/73 各 A、B，WP52/66 各 A、B、C，父号不重复计入，80−5+12=87。

依赖是完成前的知识/输出依赖，不是源码加载顺序。区分自身范围、必须闭合输入、前向引用；同批可引用已固定且自检的上游，但不能声称已外审。Reviewed 必须来自真实外审，提取方照报告登记不等于自批。

Feature 可同时带不同范围的 Reviewed/Inventoried 等状态。包通过不等于整项 Feature 完成；不能将本包静态未完成项目笼统留给 WP79，或以“未运行”掩盖未提取。`planning/coverage.md` 留 WP79，`audit/source-traceability.md` 留 WP80，不建平行总控。

WP78 跨模块一致性、WP79 覆盖、WP80 sanitized 仍是最终阶段出口，局部审查不能替代。

## 7. 继续开放的限制

U 项以 repository-overview 为权威，不因 WP01–WP12 通过而关闭：

| ID | 保留边界 |
| --- | --- |
| U01 | Demo 地图/事件/媒体及实际可达、收费奖励 |
| U02 | 固定提交与基准发行包差异 |
| U03 | 世代开关、备选 PBS 与组合兼容 |
| U04 | 关键词/函数存在或搜索未中不能证明完整机制有无 |
| U05 | 跨系统随机/时间/回放确定性 |
| U06 | Shadow 可选内容完整生命周期 |
| U07 | 取消/失败时跨域状态一致性 |
| U08 | RMXP 命令完整兼容与实际事件流程；WP13 仅处理已述部分 |
| U09 | 真实插件组合与外部服务 |
| U10 | 战斗效果、AI 估算与版本覆盖 |

WP06 的部分统计调用来源、WP10 的旧档样本/宿主落盘/重启等具名限制继续保留。静态测试向量不是实测记录。

## 8. Reviewer 工作纪律与交付

用户偏好：授权内直接推进，不反复询问普通工作选择；分别判断各包；继承关闭项，不为措辞偏好无限审查。没有新材料就短确认后等待，有实际修订就固定版本并复审。

每轮只新建审查目录，固定输入完整哈希/大小、快照、相对上轮的 diff。核对实际调用者、消费者、守卫、单位/时点与失败副作用。源码读取、哈希一致、索引集合、静态推导、运行观察分别记账；不混称。

真实问题写稳定编号、被审哈希/行号、源码路径/定位、影响、最小修改和静态验收。有限修订报告要说明已经接受的部分；通过后提供下一批提示词。报告完成后停止，不代执行提取。

本目录文件：`new-session-prompt.md` 可直接发给接手 reviewer；`handoff.md` 为本说明；`current-hashes.tsv` 为实际完整哈希；`workspace-checks.json` 为交接核对；`snapshot/` 固定约束、规划、当前五份产物、最新报告/提示词及旧交接历史入口。旧文件均不覆盖。
