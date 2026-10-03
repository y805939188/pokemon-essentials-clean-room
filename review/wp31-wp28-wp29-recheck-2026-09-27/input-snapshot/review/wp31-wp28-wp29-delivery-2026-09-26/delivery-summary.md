# WP31–WP28–WP29 批次交付摘要（含 WP26–WP30 闭合回填）

日期：2026-09-26（Asia/Shanghai）。本目录为提取侧交付包，**不是**外审报告，也不是 WP80 sanitized 产物。工作区：`/Users/dingshinn/Desktop/pokemon-framework-reference/`；参考基线 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，`reference/` 全程只读。

依据：`review/wp26-wp27-wp30-closure-review-2026-09-26/report.md`（`21712a5c8715b793e18f2426868685f6e83caccf4e3f59eee083daef7e6d6e29`，11,449 字节）与同目录 `next-batch-prompt.md`（`8091fed24599616048b6b2ac83b25fba4bebc0070b96eed18e1c79d319e58fda`，12,982 字节）：WP26/WP27/WP30 均 **PASS_SCOPED**；先管理性回填 Reviewed，再执行 **WP31→WP28→WP29**（串行、逐包自检固定、批末统一送审）。

## 1. 回填（先执行）

- 回填前实测六项固定对象与闭合报告 §1 及闭合轮 `input-snapshot/` 完全一致；回填回应见本目录 `backfill-response.md`，差异（相对闭合轮 `input-snapshot/`）见 `backfill-diffs/`。
- 三包登记 **Reviewed（限定静态范围）**；被审 v3 保留历史、不伪称为复审对象：

| 包 | 被审 v3 | 回填后 | 字节 |
| --- | --- | --- | ---: |
| WP26 | `afc7214a` | `c87101adc78d2bf5d6c51fd6bb2f608fec0b2536da19d855f12cdaca79520f18` | 35,738 |
| WP27 | `969cb37c` | `8064f17284c50a05420198f62340b4dfa48613c00898ca293a64e1fc42c58ea4` | 27,516 |
| WP30 | `41e71624` | `6fbc5a201689d43706af806ba57922c319c0821b79ef7ee27abbd084e7505a79` | 36,970 |

- C03 三项已同步（WP30 §12.2 锚定与 Shadow 前提承接；`008_PokemonBag.rb` 笔误更正、旧回应保留；“整批 8 项关闭”历史语境）。
- 必要状态引用同步（管理性，5 文件）：WP18 `54b54743`（37,399）、WP19 `1c4325f5`（36,443）、WP20 `9a2ad1ab`（35,027）、WP21 `b5eeb48e`（42,498）、WP25 `f505afd5`（27,107）。
- 矩阵：六行回填（中间版 `347dfff0`，41,242 字节）；最终版含新批次四行增量 `cbf671a8`（42,243 字节）。

## 2. 批次固定版本（均 ReviewPending；首审 REQUEST_CHANGES，按原编号修订后再送——见 §8）

| 顺序 | 包/主题 | 文件 | 完整 SHA-256 | 字节 | 关联功能 |
| --- | --- | --- | --- | ---: | --- |
| 1 | WP31 基础进化 | `specs/pokemon-rules/wp31-basic-evolution.md` | `b5966bbfdf6f69365e12efebf51d497a165da088d64c07a11476422cec31ce25` | 35,629 | F09-03 |
| 2 | WP28 主动道具与培养/教学 | `specs/creature-rpg/wp28-item-use-and-training.md` | `f9cd5fe3d130a6aab877e068a8e1a1eb688a33ec21a458daea61050c9f6fa129` | 32,848 | F08-03、F08-04 |
| 3 | WP29 买卖与 BP 商店 | `specs/creature-rpg/wp29-shops-and-exchanges.md` | `3705047ff534c54d1474ec8286978ec568b37c88c035b37ed0cab13932c3c4d7` | 21,918 | F08-06 |

- 批内顺序与固定：WP31 先自检固定；WP28 引用 WP31 的**批内固定版本**并注明“尚未外审”＋哈希（随批次末级联同步至 `b5966bbf`）；WP29 独立核对商店调用链、不套用 WP27 包装结论。
- 三包保持 **ReviewPending（各自具名范围）**；不自批 Reviewed。**2026-09-26 首审：REQUEST_CHANGES（10 项必修＋C01/C02），已按原编号修订（v2）——见 §8。**

## 3. 逐包自检概要（详见 `self-checks.json`）

- **WP31**：条件族目录逐行比对注册表（升级/道具/交换/战后/事件全族）；五入口守卫与首目标选择；提交顺序（统计→消息→进化后动作→物种变更→濒死保持→重算→标记→图鉴→进化时招式→收尾）与取消/复制逐行核对；独立算术与静态推论（个体号互斥样本、满级糖果取消后消耗、复制前提顺序）；引用存在性校验发现并修正 WP18 §4.1→§3.4（级联）。
- **WP28**：注册家族与触发点全量清点（两文件逐行为主）；四类上下文入口（背包/队伍/野外/战斗）与消耗时机逐处核对；效果辅助逐段核对；教学计数路径差异按真实调用链登记；引用 WP31 批内哈希；独立算术（维生素世代阈值、羽毛/252/510、糖果、数量上限）。
- **WP29**：两商店全文逐行核对；价格来源/覆盖/取整与命令语义核对；资源 setter 钳制与交易层判断分列；写入顺序/回退/赠品/退出清除逐条核对；独立算术（600/750/上限 +49/60/BP 半价显示怪癖）；自检修正两处表述（出售顺序、默认光标）。
- 全部为静态证据（逐行阅读、集合清点、独立算术、哈希实测）；无运行确认。

## 4. 批末交界核对（四项通过；详见 `boundary-checks.json`）

1. **WP31×WP18/19/20/21/25/26/30**：通过（修正 1 处引用——WP31 对 WP18 的引用由 §4.1 改为 §3.4；WP32 触发组合保留）。
2. **WP28×WP20/27/30/31**：通过（资格/效果/消耗、批量/部分成功、机器计数差异按调用链登记）。
3. **WP29×WP24/27**：通过（资源域钳制与交易层分列；商店自身添加/回退链独立核对）。
4. **追踪一致性**：通过（三新包范围/状态/前向、矩阵四行增量、批内固定与 manifest/TSV 登记一致；只读与算术检查未称运行/外审）。

## 5. 追踪与清单更新

- 矩阵：F09-03、F08-03、F08-04、F08-06 → ReviewPending（各自范围，批内固定、尚未外审）＋前向 Inventoried；最终 `cbf671a8`（42,243 字节）。
- `planning/review-manifest-2026-09-19.md`：§1 当前版本表（更新 20 项、新增本目录与闭合轮材料）、§2.1 本轮记录、§3 历史替代链（v1/v2/v3 保留）、§4 **第三十六轮**均已更新；闭合报告与提示已补登。
- `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv`：延续更新为 **v11**（表题更新、不丢旧行；含本目录与闭合轮材料）。
- WP26–WP30 交付摘要 **v4**：`review/wp26-wp27-wp30-delivery-2026-09-26/delivery-summary.md`＝`bdd353fdf5ab24efe6014c01f707e653998d61c60c9d39b1950bdd1b14bf93de`（13,366 字节；加闭合回填注记，v3 原文保留历史）。

## 6. 交付材料（本目录；全部实测）

| 文件 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `backfill-response.md`（回填回应；含六项复算、C03 三项、引用同步） | `fd800ef2534491eeaae1a8a7023f59fe185eb605a78d65849c2bd52cc56a7e56` | 6,306 |
| `self-checks.json`（逐包自检记录） | `f22d8fdcf5c39c96d5507c66a49c373a7b8be768485898109b298f6dbeb702f6` | 7,388 |
| `boundary-checks.json`（批末四项交界与级联记录） | `63fb993be6c6a2c5f697a6324d24429b6a8caa3fd49391a96004729948d6a59b` | 3,359 |
| `backfill-diffs/wp26-backfill.diff` | `1f290388f1e1616baac1be3dea65e4278cd99e3c9a160f8614b3866d75dc909d` | 3,567 |
| `backfill-diffs/wp27-backfill.diff` | `f2131aec5dfaaf55d359a73e1b7b5986d9a7227d9712d15035446a5e4a77ada5` | 3,083 |
| `backfill-diffs/wp30-backfill.diff` | `c6025a2d6bb1db8315a6f7562b8d2309cb3ba7728c9fa6a69ea667ddf757a12c` | 7,784 |
| `backfill-diffs/feature-matrix.diff`（回填六行＋新批次四行，合计） | `1204fc1b792f39a0a74981974c639d6900ed4ce1f6ca566c84c72511b4c50da9` | 12,806 |
| `backfill-diffs/wp18-refsync.diff` | `7cda993cf38a4f52fa072d69c1a19241bcd5b179799f7fdbdeb5d6cf5ca3f516` | 1,705 |
| `backfill-diffs/wp19-refsync.diff` | `c0d9b8738e2c25759ba498dcd33b7efad2fa8e0a80ac48b6f89974e758571380` | 1,272 |
| `backfill-diffs/wp20-refsync.diff` | `9514fa6e43a60a982a2d1bd1f6c43eec0f9922fd2d3b86ba2752a05e66a93983` | 1,206 |
| `backfill-diffs/wp21-refsync.diff` | `7905061cb71ebaaacd77e790db2cfe719b03441705edc1d1932efc77d41d2896` | 1,417 |
| `backfill-diffs/wp25-refsync.diff` | `5725a497f03edec25d77c61cd625edd165f8fec4d569f6af9a227440d4dbaeeb` | 1,175 |
| `backfill-diffs/delivery-summary.diff`（v3→v4） | `99700a02325b517e6e3c73051f81a7f35c486f01d2ea5e37ec6e1b0fc535b6ab` | 4,208 |
| `backfill-diffs/review-manifest.diff`（manifest 回填+批次差异；因避免自引用不入 manifest/TSV 清单） | 见交付消息（最终实测） | — |

- 全部差异基准：`review/wp26-wp27-wp30-closure-review-2026-09-26/input-snapshot/`（reviewer 快照未覆盖）。
- 本摘要自身与 TSV/manifest 不自哈希；最终实测值由交付消息报告。

## 7. 停止点

- 批末统一送审后**停止**：不启动 WP22/WP23/WP32/WP33 或任何其它包；不向 reviewer 发消息；不创建并行任务；不提交/推送。
- Demo、宿主、媒体、插件、U01–U10 与 WP78→WP79→WP80 阶段出口保持开放；本批交付与回填均不替代最终 sanitized 规格与运行兼容验证。

## 8. 修订注记（v2，2026-09-27 首审后）

- 依据：`review/wp31-wp28-wp29-review-2026-09-26/report.md`（`5e34d822`，21,709 字节；**REQUEST_CHANGES**：WP31 两项、WP28 六项、WP29 两项必修＋BATCH-C01/C02；205 条 manifest 与 109 条 TSV 匹配）与同目录 `revision-prompt.md`（`13d32a4b`，10,673 字节）。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。
- 修订（10 项＋两组维护**全部核实认可并修订**，v2）：WP31-R01（事件编号无一次性消费状态；复用/取消后重试/不匹配对照）、WP31-R02（物种设置的形态/性别例外，按 WP18 §3.4；提交表/保留表/不变量/依赖同步）；WP28-R01（背包回退与快捷入口/返回分层）、R02（队伍集合、循环返回、工具库存边界）、R03（界面上限/效果应用/外层扣除分列；树果与糖果向量改正）、R04（战斗退回按资格复检/目标分支）、R05（复活药草回满、X 分档、MAXMUSHROOMS 五项、GUARDSPEC=白雾、HONEY 返回语义）、R06（形态/融合道具 §5.6 有界使用表与库存输出；修正"物品种类不变"）；WP29-R01（库存原地过滤与列表复用）、R02（价格输入层级与旧覆盖保留）。BATCH-C01/C02 同步（取消不进入成功序列、VENUSAUR 0 级样本、复制个体号静态闭合、缓存措辞、场景前提与"语句数"口径）。
- 修订后（v2；被审首版哈希保留历史）：WP31 `e541c650`（39,138 字节；被审 `b5966bbf`/35,629）、WP28 `f2f7618c`（42,586 字节；被审 `f9cd5fe3`/32,848；含级联后的 WP31 修订稿引用）、WP29 `d5c847f1`（25,211 字节；被审 `3705047f`/21,918）；矩阵 `cbf671a8` → `a05c39f4`（42,454 字节；四行"首审已送审：REQUEST_CHANGES，修订后再送"）。
- 逐项回应见 `review/wp31-wp28-wp29-review-2026-09-26/revision-response.md`，逐文件差异见同目录 `revision-diffs/`（wp31/wp28/wp29/feature-matrix/delivery-summary 五份，相对本轮 `input-snapshot/`）。
- 追踪口径（C02）：静态证据、集合清点与独立算术分开记录；§4 的"批末四项交界通过"是提取侧静态自检记录，不作为独立外审结论沿用。
- 未改动：§1/§3–§7 的历史记录与批末交界结论；三包保持 ReviewPending，不自批 Reviewed。
