# WP66-B／WP66-C／WP71 交付摘要 v2（首审修订后）

2026-09-30；规格提取方。授权：`pokemon-next-extraction-handoff-2026-09-30/prompt.md`＋`status-and-inputs.json`（25/25 项固定身份开工前复测一致；reference 固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、普通 Git 清洁）。独立首审结论：**REQUEST_CHANGES（12 项 P2＋2 项 P3）**；WP23 管理性回填差异 **PASS_SCOPED**（不重做）。已按原编号完成 v2 修订（WP66B-R01～R06、WP66C-R01～R03、WP71-R01～R04、CR-R01），三稿仍为 **ReviewPending（首审修订 v2，待有限复审）**，未自批 Reviewed；不启动第四包。

## 1. WP23 限定回填（管理性，行为未改；回填差异已获首审通过）

依据有限复审[报告](../wp22-wp23-wp32-review-2026-09-30/recheck-v2/report.md)§4（PASS_SCOPED，A～G）。主附表头尾与 F06-08 的 WP23 子范围回填 **Reviewed（限定静态范围，2026-09-30有限复审PASS_SCOPED；管理性回填）**；同步 WP32 及活动材料。被审 v2 主稿 `1a11060e2a1a2c37052734fb8d264655f8179ec6bca0d122cbc07b8afafe6f4c`／40,939 与附表 `afeab7580e39bc0a0dc78d3d6ae13f9f0e4db321101dc78600452670b0888abe`／13,534 留史；N02 宿主未决保留；净化／Hyper／N01 行为未动。回填回应与十份差异见 [backfill-response.md](backfill-response.md)（差异相对有限复审 input-snapshot，重建 10/10；首审独立重建复核通过）。

| 对象 | 回填后当前身份 | 字节 |
| --- | --- | ---: |
| `specs/pokemon-rules/wp23-shadow-hyper-and-purification.md` | `6343cfea16f78218cd9dc6df3ecd31677a30745181cc20d62344ec5f71f4979b` | 41,529 |
| `specs/pokemon-rules/wp23-shadow-data-and-vectors.md` | `20a561cb27c6b6d164ad3f6814aa0d926ea0ba1389cfc85a7118a097170b7457` | 13,995 |
| `specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md`（仅 WP23 引用同步） | `f228cc7fd4de132b9c1be6a70e2bf720105b39949b615f87ba6a861df1a51b6b` | 30,435 |

回填后限定通过集合＝**WP01–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62**（各包具名静态范围；其中 18 包另有全局复核 P2 修订要求待另行处理，历史通过记录保留）。

## 2. 三包 v2（ReviewPending，首审修订，待有限复审）

| 包／文件 | v2 修订要点 | 被审 v1（留史） | 当前 v2 身份 | 字节 | 场景 |
| --- | --- | --- | ---: | ---: | ---: |
| WP66-B [wp66-b-storage-and-pokedex-ui.md](../../specs/ui/wp66-b-storage-and-pokedex-ui.md) | R01 空结果搜索仍先写持久模式；R02 选择模式队伍按钮泄漏 [-2,-1]；R03 双属性状态转移；R04 体型端点哨兵；R05 结构排除与首轮写入；R06 ACTION 按页限定；CR-R01 分层行为化 | `0032257262eb010e52993069576608641db3a473c2e6d1f6ac1b3144003d7f10`／30,215 | `4eeb05eff1e30a5bc16314ee081d5540a557c88d654afa2e5a313552e6e1ab8a` | 36,552 | 39 |
| WP66-C [wp66-c-bag-item-storage-and-shop-ui.md](../../specs/ui/wp66-c-bag-item-storage-and-shop-ui.md) | R01 PC 存入＝正常背包画面（配对预检限存／取）；R02 使用结果三层分离；R03 Give 非蛋与可携带可见门；CR-R01 库存过滤行为化 | `355417e0db441daa59e6c757bc231be2579bc9e43b30fc38560f0c9078e6436a`／23,526 | `665d0ae28594c8b6314bc0c489d360056f8a6f8dcee786e42a21ba9d35a8e4b9` | 28,275 | 36 |
| WP71 [wp71-tile-puzzles.md](../../specs/ui/wp71-tile-puzzles.md) | R01 末格空白漏扫、全尺寸可解性声明撤回；R02 非方形列端点缺陷与奇宽整数拆分；R03 动作向量未完成前提；R04 角度 3 三次递减；CR-R01 行为化 | `ef2693fdcfb95924826e44210273b220f27924c562fa70174b52a57a25dcf7e2`／17,239 | `0319689374ca5cb4f0a0d10226469c9e1565a6744a703991edf3bfd8b4873b40` | 21,984 | 21 |

七个完成依赖（WP25／WP62／WP17／WP27／WP28／WP29／WP06）身份未变、均限定 Reviewed 且全局复核 PASS_SCOPED；9 条绑定见 [boundary-checks.json](boundary-checks.json)。矩阵：`planning/feature-matrix.md` 当前 `d2abb30c6cd21af213bf104da0b752b27b98654f9cfa8a70922ae157a86fb0fe`／57,172（F16-03／F16-04／F17-07 三行改为首审修订 v2 状态；F06-08 的 WP23 回填与 WP66-A 保留不动）。逐项回应与差异见 [revision-v2/revision-response.md](revision-v2/revision-response.md) 与 [revision-v2/revision-diffs/](revision-v2/revision-diffs/)（相对首审 input-snapshot）。

## 3. 材料清单

- [backfill-response.md](backfill-response.md)：WP23 回填回应与差异表；[backfill-diffs/](backfill-diffs/)（10 份）；[diff-bindings.json](diff-bindings.json)。
- [revision-v2/](revision-v2/)：首审修订回应、差异、固定身份与检查材料。
- [self-checks.json](self-checks.json)：v1 自检＋v2 逐项修订核对（含 14 编号覆盖与 clean-room 扫描）。
- [boundary-checks.json](boundary-checks.json)：四组交界（含 v2 更正注记）。
- [source-identities.json](source-identities.json)：21 份实际读取来源，全部与固定 commit blob 一致。
- [reading-log.json](reading-log.json)：v1＋v2 两轮的读取与检索范围。
- [new-observations.md](new-observations.md)：N01（旧 WP23 可达性冲突，CONFIRMED_STATIC，本轮不改旧稿）；已撤回 v1「无新增观察」结论。

## 4. 登记与停止

manifest 续**第六十六轮**、主 TSV 续**v41**（旧行与历史链保留；被审 v1／修订 v2 身份分列）。自检仅覆盖其检查项，不构成外审通过；备妥有限复审材料后**停止**：不启动第四包（WP63／WP66-A／WP67 等），不执行全局 16 项修订，不合入 B 批，不处理 N01 旧 WP23，不执行 WP78／79／80。

未运行游戏／参考 Ruby／事件解释器／生成器／编译器／转换器／插件／网络；未操作真实地图／存档／输入；未实现新框架；未创建任务／Agent、未发其它会话消息、未提交／推送。reviewer 原件、快照与历史交付只读未动。Demo、宿主、媒体、插件、U01–U10 与 WP78→WP79→WP80 出口继续保留。

v1 摘要 `89e05485192ff485411e5ac180376cb8013dce5b4b080109aec6411b393ce5b5`（5,814 字节）留史于首审 input-snapshot；本版替代之。
