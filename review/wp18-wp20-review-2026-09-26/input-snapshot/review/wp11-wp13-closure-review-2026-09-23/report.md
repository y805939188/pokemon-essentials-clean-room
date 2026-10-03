# WP11–WP13 闭合复审

日期：2026-09-23（Asia/Shanghai）。Reference/Audit 侧 reviewer；本报告不是 WP80 sanitized 材料。R = `reference/pokemon-essentials/`，S = `R/Data/Scripts/`。

**结论：WP11 PASS_SCOPED、WP12 PASS_SCOPED、WP13 PASS_SCOPED。** WP13-R05 最后一个分支已闭合；WP01–WP10 的既有限定通过范围继续继承。本批没有剩余行为阻塞，可以在 WP13 做管理性 Reviewed 回填后开始下一批。真实 Demo、运行、媒体、插件组合和各 Feature 的前向范围仍保持未决。

## 1. 实际版本核对

用户提供了 WP13 v4、WP11/WP12 状态回填和差异摘要，因此按修订稿直接固定版本复审，没有重新做首轮 122 文件检查。

| 对象 | 当前 SHA-256 | 字节数 |
| --- | --- | ---: |
| WP11 `specs/overworld/wp11-map-topology-transfer.md` | `84ca24a5919f05a280e67b0470436cdaf5557800ced19a0fccb218fbf3f38275` | 19944 |
| WP12 `specs/overworld/wp12-terrain-movement-vehicles.md` | `8187e7deb59950301a12a6518a3c81a1e2a3aebabc347f7fa388e02364e8b280` | 32153 |
| WP13 `specs/overworld/wp13-map-events-npc-followers.md` | `b9b809e4ce1e979397295944f40b219fec841670964232428b5a51d7a6b4994e` | 28482 |
| WP13 主命令矩阵 | `ab69bc87c97b805f1a2f0848a35e9b86aa8b582f8128553038f2487b85245de5` | 17561 |
| WP13 移动路线矩阵 | `f637f1c32db9fd59e93b0b3c81f33637f22e715dfeaaabb74f5fad6a71db12c7` | 8315 |
| `planning/feature-matrix.md` | `3861c4b1d8748307d08669e012f3e10f1a20b1a9a63f99415d508cac85cdae98` | 33656 |
| `planning/review-manifest-2026-09-19.md` | `ced93abf10a2bf52deb63e287b7198177e6ecb4bc674945a988dd4c65ef0b59f` | 31337 |
| v3 修订回应 | `ded1f0874f0e0fc1b5e4d499e35bafcff357759dc9fd0a5ac277e1df9e0e4830` | 3860 |

当前 manifest 的 **68 条完整哈希/字节数记录全部匹配**。v3 固定输入和旧 review artifacts 未发生意外变化；v3 的四个差异文件均可精确重建当前对应文本。两份 WP13 矩阵未改动，96 个主命令集合、28 dummy/2 标记/66 其他入口及 0–45 路线集合无回归。

参考仓库 HEAD 仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`），普通状态为空，ignored 仍为 `.DS_Store` 与 `PBS/.DS_Store`。本轮重新比对跟随、地图位置和地图工厂相关参考文件的固定 commit blob，全部一致；未运行参考代码、游戏、解释器、编译器、转换器、插件或网络请求。

独立检查材料：`input-manifest.json`、`changes-from-v3.diff`、`source-checks.json`、`static-checks.json`。全部写入本闭合复审目录，未覆盖旧报告或旧提示词。

## 2. WP13-R05 最后分支

**结果：CLOSED。**

修订后的 WP13:123 将 `fancy_moveto` 未命中同轴一格/两格分支的目标统一定义为“其他非重合目标直接定位”，明确包含非同轴目标及同轴相距三格或以上；WP13:200 新增同轴三格场景。该表述与固定源码 `S/004_Game classes/010_Game_Follower.rb:91–110` 的末分支一致；`follow_leader` 的调用前提和传送/强制路线边界仍保留。

独立静态向量：人工 20×20 地图、跟随者 `(5,5)`、向右领队 `(9,5)`，身后目标为 `(8,5)`，偏移为 `(3,0)`，落点在有效范围内，结果为直接定位到 `(8,5)`。这是坐标算术和源码条件的静态核对，不是实际地图运行。

已接受的一格、两格四种许可分支及 `(1,1)` 非同轴场景没有被改写；WP13-R01/R02/R03/R04 继承前轮 CLOSED 结论。

## 3. 包级结论与状态传播

| 包 | 结论 | 可登记范围 | 尚未通过的前向范围 |
| --- | --- | --- | --- |
| WP11 | PASS_SCOPED | 地图身份、连接锚点/单位、边缘与显式转移、通知时序、取模/索引、实例生命周期、缺图失败阶段及 WP09/WP10 恢复引用 | 真实地图尺寸/可达性、元数据语义、绘制和 Demo 流程 |
| WP12 | PASS_SCOPED | 分入口通行、运动状态和统计时点、载具、上下水/瀑布交界、进入地图骑行调整、正常跟随位置判定 | 完整资格、动画/媒体、多格角色组合、真实地图流程 |
| WP13 | PASS_SCOPED | 事件页/触发、解释器和命令/路线矩阵、等待/失联、NPC 感知、事件级跟随生命周期与条件位移 | Demo 事件可达/收费/奖励、完整跟随宝可梦系统、战斗内命令、未逐分支命令行为 |

WP11/WP12 的 Reviewed 状态回填已经与其 PASS_SCOPED 报告范围一致。WP13 当前文件头仍为 ReviewPending；这是管理性登记尚未完成，不是行为问题。提取方应保留本轮被审哈希 `b9b809e4`，将 WP13 自身限定范围登记为 Reviewed，并在 manifest/Feature Matrix 保留历史替代关系；本 reviewer 不代改规格或矩阵。

Feature Matrix 中 F04-01～F04-03 的 Reviewed＋Inventoried 分层符合限定范围；F04-04/F04-05 可在 WP13 回填后同步为对应范围 Reviewed＋Inventoried，不能清除 Demo/完整系统的前向状态。U01–U10 继续开放。

## 4. 下一批判断

**可以开始下一批。** 前提是先完成 WP13 的管理性 Reviewed 回填并固定新哈希；这不会触发 WP11–WP13 行为重审。建议下一批按计划选择 **WP14、WP15、WP16**，顺序为 WP14 与 WP15 可先分别提取，WP16 在 WP15 的固定自检版本之后推进：

- WP14：随机地牢，依赖 WP11、WP12、WP06；需区分参数/布局生成、事件摆放和地图集成，不把未证可达性或跨实现种子一致性写成不变量。
- WP15：资源匹配、资源访问及声音，依赖 WP03、WP07；需区分资源身份/变体选择、缓存/缺失、声音切换与实际媒体内容，不用目录存在证明完整资源支持。
- WP16：世界绘制与视觉过渡，依赖 WP11、WP12、WP15；需描述可见行为、刷新/转场/天气/反射/阴影交界，不设计渲染器架构，并将缺媒体和未运行结果保持待证。

WP17（消息、窗口与输入）可安排为后续包，依赖 WP08、WP15；本轮不把它混入 WP14–WP16。WP14–WP16 的执行提示词见同目录 `next-batch-prompt.md`。本报告完成后停止，不执行下一批。
