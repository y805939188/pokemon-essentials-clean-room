# WP11–WP13 v3 独立复审

日期：2026-09-22（Asia/Shanghai）。Reference/Audit 侧材料，不是 WP80 sanitized 交付。R = `reference/pokemon-essentials/`；S = `R/Data/Scripts/`。

**结论：WP11 PASS_SCOPED；WP12 PASS_SCOPED；WP13 REQUEST_CHANGES。** 上轮 8 个剩余编号中，本轮关闭 7 个；WP13-R05 仅保留一个条件分支遗漏。已通过部分继续继承，不重新做首轮审查。

| 包 | 判断 | 范围与后续 |
| --- | --- | --- |
| WP11 | PASS_SCOPED | 已述地图身份/连接锚点与单位、转移入口/通知位置、取模/索引、实例生命周期及缺图失败阶段；地图恢复引用既有 WP09/WP10 |
| WP12 | PASS_SCOPED | 已述地形/分入口通行、运动状态与统计时点、载具及上下水/瀑布交界、进入地图骑行调整和正常跟随位置判定 |
| WP13 | REQUEST_CHANGES | 命令/路线、等待、失联、接触与感知等修订已闭合；跟随位移表遗漏同轴相距超过两格的直接定位分支，仍属 WP13-R05 |

WP11/WP12 可由提取方分别登记限定 Reviewed，不受 WP13 剩余项牵连。当前磁盘文档及矩阵仍为 ReviewPending，本 reviewer 未回填。WP01–WP10 各自限定通过不重开。Demo、运行、媒体、插件组合及未闭合前向引用不因本报告通过。

## 1. 固定输入与核对

参考 commit 实测为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，describe 为 `v21.1-23-g8c5911e4`。普通 Git 状态为空，ignored 仍为 `.DS_Store` 与 `PBS/.DS_Store`。

| 对象 | 完整 SHA-256 | 字节数 |
| --- | --- | ---: |
| `specs/overworld/wp11-map-topology-transfer.md` v3 | `df39a9e5210b4fdd3ff63f27a76b82fbb0ed37d13c6e6bd53e4160e5b36c1f36` | 19521 |
| `specs/overworld/wp12-terrain-movement-vehicles.md` v3 | `7f1979bd4734cc2f878117b934589f1e5ccf26754984d703d3e14701f9cee974` | 31489 |
| `specs/overworld/wp13-map-events-npc-followers.md` v3 | `1ec410b6d084d841ba0701e6089d6c7b1e11a4eda2f2e6294a21ce1dce3d5f97` | 27706 |
| `specs/overworld/wp13-interpreter-command-matrix.md` v3 | `ab69bc87c97b805f1a2f0848a35e9b86aa8b582f8128553038f2487b85245de5` | 17561 |
| `specs/overworld/wp13-move-route-matrix.md` v2 | `f637f1c32db9fd59e93b0b3c81f33637f22e715dfeaaabb74f5fad6a71db12c7` | 8315 |
| `planning/feature-matrix.md` | `55352c019b90f84411f8dc54a6ab890321394b86cfb06add89ef660fdd1f2bce` | 33653 |
| `planning/review-manifest-2026-09-19.md` | `9c49398392e00bc6d7e9c8f5da2c00bf8c6a27770085626248e18c9736914c38` | 27523 |
| `review/wp11-wp13-recheck-2026-09-20/revision-response.md` | `afeca04a52f7b0a447fb68c51e876144e29a4e3abdb8a8c42a8828aa7bc2833a` | 9382 |

当前 manifest 的 **61 条完整哈希及字节数全部匹配**；两条“见原件”历史行不计入。固定 67 项输入。对照 v2 固定快照，原有输入中仅五份规格/附表、矩阵、manifest 改变；旧报告、提示词和其交付检查文件均未被覆盖。WP01–WP10、总览、module-map、计划、AGENTS.md 保持原哈希。

五个提取方 diff 均可从 v2 文本精确重建本次被审产物。WP12 的 diff 分块与 difflib 输出不同，但重建文本完全一致，**不构成差异文件错误**。另保存独立 `changes-from-v2.diff`。

本轮对 11 个相关参考文件复算哈希并比对固定提交 blob，全部一致；新语义核对仅限修订所需片段和直接回归，详见 `source-checks.json`，不冒称重做首审的全部源码检查。主命令仍为 96 个不同代码，28 dummy、2 标记、66 其他入口；路线目录仍覆盖 0–45，集合无回归。

证据文件：`input-manifest.json`、`input-snapshot/`、`changes-from-v2.diff`、`source-checks.json`、`static-checks.json`、`final-checks.json`。哈希、文本差异及索引工具均为自有静态检查；未运行参考源码或表达式，未运行游戏/解释器/编译器/转换器/插件，未请求真实网络、操作真实地图或存档。

## 2. 原问题逐项结论

下表规格行号指本轮固定文件；源码定位以 S 为前缀。未改动的已接受部分继承前两轮结论。

| 编号 | 结论 | 本轮验证 |
| --- | --- | --- |
| WP11-R01、WP11-C01 | 继承 CLOSED | 锚点/单位/正反向例与表头未改变 |
| WP11-R02 | CLOSED | WP11:72,120,148–149 按有/无 BGM/BGS 区分 autofade 前置读取失败与已到达 setup 的失败；对应 `003_Game processing/002_Scene_Map.rb:56–81`、`004_Game classes/005_Game_MapFactory.rb:17–26` |
| WP12-R01 | CLOSED | WP12:77,106–110,249–251 明确地图层提前返回、外层碰撞仍执行；区分实际跟随位置方向判定与 strict helper。对应 `004_Game_Map.rb:145–156`、`006_Game_Character.rb:237–257`、`010_Game_Follower.rb:48–88,174–213` |
| WP12-R02 | CLOSED | WP12:124–129,252–253 将普通步/跳跃的逻辑位置、距离及条件性离格放在运动开始，完成后的全局计步继续引用 WP06；对应 `008_Game_Player.rb:162–192,543–552`、`006_Game_Character.rb:387–399,767–786,967–985` |
| WP12-R03 | CLOSED | WP12:167,171–173,239–244 补上水前跳前提交及失败不回滚、surf_jump 分层守卫、force_cycling 在边缘/跨图显式传送中的作用；对应 `012_Overworld/004_Overworld_FieldMoves.rb:685–751,776–785`、`001_Overworld.rb:268–275`，及工厂通知/载具入口 |
| WP13-R01 | CLOSED | 路线附表:10–18,24,80–83 区分玩家 bump 和普通事件受阻，补 size≤1 强制路线不能执行恢复分支；对应 `006_Game_Character.rb:348–350,362–373,427–469`、`008_Game_Player.rb:121–127,172–173` |
| WP13-R02 | CLOSED | WP13:80,175–176 与命令矩阵:23 一致：等待取决于标记，相邻 101 不被消费；对应 `003_Interpreter.rb:30–31,105–115`、`004_Interpreter_Commands.rb:169–189,856–873` |
| WP13-R03 | 继承 CLOSED | 失联只清 event_id，已有命令列表仍有效；未出现相反修订 |
| WP13-R04 | CLOSED | WP13:60–62,187–191 按玩家失败/NPC 失败/步完成同位检查分开，并限制 counter 的 NPC 感知检查为移动完成入口；对应 `008_Game_Player.rb:172,332–344,389–409,543–552`、`006_Game_Character.rb:553–564`、`007_Game_Event.rb:142–183` |
| WP13-R05 | PARTIALLY_FIXED | WP13:121–122,195–199 的一格/两格许可分支及 (1,1) 例接受；第 123 行把直接定位范围缩成非同轴，遗漏另一类位置，详见 §3 |

WP12-R02 的“失败无提交”在此只批准正文明确描述的成功位移距离/increase_steps 范围，不推导为失败跳跃连朝向等一切状态都不变。

## 3. 唯一阻塞剩余项：WP13-R05 [P2]

**题目：条件位移表遗漏同轴相距超过两格的直接定位。**

**被审文件**：`specs/overworld/wp13-map-events-npc-followers.md`，SHA-256 `1ec410b6d084d841ba0701e6089d6c7b1e11a4eda2f2e6294a21ce1dce3d5f97`，**第 120–124 行，重点第 123 行**；相关场景第 195–199 行。

v3 正确区分了同轴一格、同轴两格以及非同轴目标，但没有规定同轴距离为 3、4 等时的结果。v2 的“更远直接定位”在修正两格分支时被删除；前轮提示要求的“其他非重合目标”被缩成了“非同轴目标”。这是该次修订的直接遗漏，不是要求重做跟随系统或更换写法。

**固定源码证据**：`S/004_Game classes/010_Game_Follower.rb:91–110`。先处理同轴相差一格与两格，剩余只要目标与当前位置不同就直接定位；末分支并不要求非同轴。`follow_leader` 在非强制路线、非即时、地图相连时可调用这一决策（同文件 134–167）。本轮该源文件完整哈希及固定 blob 校验在 `source-checks.json`。

**影响**：当前条件表无法决定同一行或列上落后超过两格的跟随者如何追赶；后续实现/测试可能错误地停留或逐格追赶，漏掉参考的直接定位结果。

**最小修订**：仅将第 123 行恢复成“未命中同轴一格/两格分支的其他非重合目标均直接定位”，明确包含同轴超过两格与非同轴目标；保留已正确的一格/两格分支。增加一个同轴三格静态场景即可。正文、场景和回应保持一致，不必改动两份已通过矩阵，不新增跟随功能。

**静态验收**：人工有效地图 20×20、无桥/岩架/事件等额外干扰；同图、非强制路线、instant=false。跟随者 (5,5)，向右的领队在 (9,5)，身后目标为 (8,5)。同轴相差三格应直接定位到 (8,5)，不是走一格或跳两格。既有 (1,1) 直接定位及同轴两格四种许可分支保持不变。无需运行地图、事件脚本或构造参考实例。

下一轮只需查这一分支、补充场景与直接传播，不重新检查已经关闭的 WP13-R01/R02/R03/R04。

## 4. 非阻塞维护：WP12-C01

WP12 `7f1979bd`:282 仍把“动画/状态置位细节”整体列为前向未决，并称本包只登记入口与守卫；正文第 172–173 行已经完成运动状态提交和清理。本轮接受正文，故 WP12-R03 已关闭。

提取方可随 Reviewed 回填将该未决项缩至完整资格、动画/媒体及其他尚未提取效果，明确本包运动状态交界已覆盖。该管理性同步不要求再做 WP12 全文审查；只核对新旧差异没有改变已批准行为。

## 5. 状态登记与交接

- WP11/WP12 可以按 §1 的被审哈希登记限定 Reviewed；回填后保留被审哈希及新哈希，不能把新字节冒称本报告已审版本。
- WP13 保持 ReviewPending；已通过子范围继承，仅 WP13-R05 上述小范围待修。原 10 个 R 项中累计 9 个已关闭，WP11-C01 已关闭；新增 WP12-C01 为非阻塞维护。
- WP11/WP12 的通过不等于 F04-01～F04-03 全量通过；真实地图/媒体、完整资格及元数据等前向范围继续保留。U01–U10、宿主/插件组合/运行结果未决。
- 本批尚未全部通过，本轮不给 WP14 执行授权；不执行或代提取下一批。

给提取方的有限修订与状态回填提示见 [revision-prompt.md](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp11-wp13-recheck-v3-2026-09-22/revision-prompt.md)。给接手 reviewer 的新版入口见 [new-session-prompt.md](/Users/dingshinn/Desktop/pokemon-framework-reference/review/reviewer-handoff-2026-09-22/new-session-prompt.md) 和 [handoff.md](/Users/dingshinn/Desktop/pokemon-framework-reference/review/reviewer-handoff-2026-09-22/handoff.md)。旧交接和旧审查保留为历史，不覆盖。
