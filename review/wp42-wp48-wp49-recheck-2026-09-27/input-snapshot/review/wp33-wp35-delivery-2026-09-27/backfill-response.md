# WP28／WP29 闭合复审后回填回应（2026-09-27）

日期：2026-09-27（Asia/Shanghai）。提取侧回填记录；依据 `review/wp31-wp28-wp29-closure-review-2026-09-27/report.md`（`8d56d23e3271907e3522557cbed6315c85f01f4503ccdeae824abf5cfc76c6e3`，8,920 字节）与同目录 `next-batch-prompt.md`（`a9e31d54a7b096bc7849d8fd14f0f01063fdb98bd1815aeb166dca4cf41deb0e`，12,960 字节）。闭合复审结论：**WP28、WP29 均 PASS_SCOPED（限定静态范围）**，最后三项（WP28-R03/R06、WP29-R02）与 C03 全部关闭、未发现直接回归；WP31 继承 PASS_SCOPED 且回填接受。**本回应是回填索引与验收记录，不是外审通过依据。**

## 0. 回填前复算（六项固定对象）

实测与本轮报告 §1 及 `input-snapshot/` **完全一致**：WP28 `7e10cb25`/43,917、WP29 `1ed4b957`/25,793、WP31 `ee47f124`/39,499、矩阵 `909080cb`/42,493、manifest `50966444`/139,772、交付摘要 v3 `6b22ac03`/13,286。

## 1. 回填后版本（管理性回填 → Reviewed（限定静态范围））

| 文件 | 被审 v3（保留历史） | 回填后完整 SHA-256 | 字节 |
| --- | --- | --- | ---: |
| `specs/creature-rpg/wp28-item-use-and-training.md` | `7e10cb25` | `a4ccb38365521eeb130b30d9e04a281812cd03ccc76ca5443393f5fbc352d95a` | 44,159 |
| `specs/creature-rpg/wp29-shops-and-exchanges.md` | `1ed4b957` | `f7788c7d600c7e9c266f3c8178c81a587b4807f5218b66286a3f3d3a4e5ef31f` | 26,053 |
| `planning/feature-matrix.md` | `909080cb` | `77c3bff0bcb1804a2a7b50a147209b3a89f7305b792fa9a3f21c12dbfad297b2` | 43,092 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/delivery-summary.md`（v4） | `6b22ac03` | `990f30b417e4d561a67530992df3428ea5fdae78c9f038f90a0c046e6cfa2109` | 14,649 |

- 回填范围（按报告 §4）：WP28＝已述四类使用上下文、注册/回退/资格与返回、数量和效果/扣减/退回分支、已述效果族与形态/融合工具有界使用；WP29＝已述商店入口/库存原地过滤、价格来源/覆盖与生命周期、数量/资源守卫、写入/回退/统计/赠品、价格输入层级与显示边界。
- 头部（第 11 行"规格状态"）与尾节（WP28 §13、WP29 §14）登记 **Reviewed（限定静态范围，2026-09-27 闭合复审 PASS_SCOPED；管理性回填）**；矩阵 F08-03/F08-04 → Reviewed（WP28 子范围）＋前向 Inventoried、F08-06 → Reviewed（WP29 子范围）＋前向 Inventoried；被审 v3 保留历史、回填后版本不伪称为复审对象。
- **未借回填改已接受行为**；差异见 `backfill-diffs/`（相对闭合轮 `input-snapshot/`）。

## 2. 必要状态引用同步（管理性级联）

| 文件 | 同步位置 | 回填后完整 SHA-256 | 字节 |
| --- | --- | --- | ---: |
| `specs/creature-rpg/wp18-creature-identity-species-ownership.md` | §10 WP28 行 | `55fb5004ecf99272f2f88332d20bb076cce6ca5075f6ed546eb24e83df579791` | 37,448 |
| `specs/pokemon-rules/wp19-attributes-ability-and-stats.md` | §8 WP28 行 | `cd3dcf4bf8e7dbea0a45d4abb30540fe2c28406a614590ac1a198a622930055f` | 36,492 |
| `specs/creature-rpg/wp20-hp-status-moves-helditem.md` | §10 WP28 行 | `05a59789554a4824121a852f05bf643f799b6e52af6837eb966c19cbec678d3c` | 35,076 |
| `specs/creature-rpg/wp27-bag-and-item-storage.md` | §10 WP28/WP29 两行 | `6ac234e466918123fe0382cef95829d20456522b4e17d377df31e079649a908d` | 27,602 |
| `specs/creature-rpg/wp30-growth-learning-and-friendship.md` | §10 WP28 行 | `b9f58991b095f780b6dd9fbfe6f460224433f1b608cc575767c59278f5a4cf21` | 37,019 |
| `specs/pokemon-rules/wp31-basic-evolution.md` | §10 WP28 行、§13 第 7 项 | `0b40917c3a0c9b942f004dd5fb6bc75addf749d154e162e75e06a2f001806d91` | 39,554 |

各行为"已触发（WP28/WP29 限定通过，2026-09-27）；规则变化时复核"。

## 3. 保留边界与停止点

- 被审 v3 哈希全部保留历史（manifest §3）；回填后哈希/字节另记；旧 v1/v2/v3 链不抹除。
- 回填**无需再等短审**（报告明确允许），同会话继续执行授权批次 **WP33→WP34→WP35**（见 `delivery-summary.md`）。
- 当前限定通过集合＝**WP01–WP21、WP24–WP31**（WP22/WP23 未完成，不得写成连续全部通过）。
- 未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送；reviewer 报告/提示/检查/快照未覆盖（差异基准 `review/wp31-wp28-wp29-closure-review-2026-09-27/input-snapshot/`）。
