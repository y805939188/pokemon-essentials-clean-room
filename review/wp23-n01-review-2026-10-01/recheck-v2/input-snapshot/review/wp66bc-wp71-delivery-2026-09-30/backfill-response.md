# WP23 限定 Reviewed 管理性回填 — 回应与差异

2026-09-30；规格提取方。依据：独立有限复审[报告](../wp22-wp23-wp32-review-2026-09-30/recheck-v2/report.md)§4（**WP23主稿v2与附表v2：PASS_SCOPED，A～G具名静态范围**）、同目录 `next-batch-prompt.md` §2 回填授权，以及本批交接提示（`pokemon-next-extraction-handoff-2026-09-30/prompt.md` §5）。本次只做管理性状态回填与必要的当前状态／完整身份同步，**行为内容未改**：净化、Hyper、N01 行为不动；N02 仍为静态双调用确认／宿主未决；O03／O04 条件化口径与三个已关闭 R 保留。

## 1. 回填范围（严格采用复审报告 §4 的 A～G）

- A：默认／可选内容的启用边界，Shadow 建立、重新建立和状态字段。
- B：心量表／Nature 数据、阶段、下降入口、原招与 Shadow 招式保存／恢复。
- C：Hyper 进入／有效查询／服从／反伤／退出及默认 G0 边界。
- D：经验／EV 暂存与恢复、友好／成长限制，以及净化调用者不同的提交／失败结果。
- E：净化与香／遗迹石分入口合同；净化室编成、原始比较门、节奏／流量、推进／领取／容量／异常和复制交界。
- F：已述捕获、形态、图鉴、队伍快照和生命周期交界、固定数据与静态场景（报告 §4 的 A～G 覆盖上述全部具名范围）。
- G：同报告 §4 所列的具名静态范围整体；运行／宿主／媒体／插件与前向范围继续保留。

## 2. 变更对象与身份（前后完整 SHA-256／字节）

| 对象 | 回填前（有限复审快照实测） | 回填后（当前） |
| --- | --- | --- |
| `specs/pokemon-rules/wp23-shadow-hyper-and-purification.md` | `1a11060e2a1a2c37052734fb8d264655f8179ec6bca0d122cbc07b8afafe6f4c`／40,939（**被审v2，留史**） | `6343cfea16f78218cd9dc6df3ecd31677a30745181cc20d62344ec5f71f4979b`／41,529 |
| `specs/pokemon-rules/wp23-shadow-data-and-vectors.md` | `afeab7580e39bc0a0dc78d3d6ae13f9f0e4db321101dc78600452670b0888abe`／13,534（**被审v2，留史**） | `20a561cb27c6b6d164ad3f6814aa0d926ea0ba1389cfc85a7118a097170b7457`／13,995 |
| `specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md` | `931c8b05f580bea154e68e8134c7c51a4714c4ebad58523af5c57056320fd193`／30,346 | `f228cc7fd4de132b9c1be6a70e2bf720105b39949b615f87ba6a861df1a51b6b`／30,435 |
| `planning/feature-matrix.md` | `ff645588705c714a8acc69295ad5d201b85e39717562a7ac158fb24220b331bd`／56,091 | 阶段身份 `9beb4b374f64c6f450f8942ca3a623ed45187e396b8c404f938c5eab79abed7a`／56,107（**见 §4 分阶段说明**） |
| `review/wp22-wp23-wp32-delivery-2026-09-30/wp23-fixed.json` | `c638a4f956dd3a6f00227999db023e530bc35094532206c04ae96b9b03c4a854`／11,086 | `a9ccbb4e7ae8214373c244923e6a9976362d0ce8e3bee962472fe78eabddac88`／12,084 |
| `review/wp22-wp23-wp32-delivery-2026-09-30/wp32-fixed.json` | `039a680540cfe0650fe199f38f28b4984a84136b385b6aef97514ce9d2538194`／9,564 | `f0fa69df096db0183b6504e0859a16f3d2196acff022677b61c48a759e9cad4c`／9,586 |
| `review/wp22-wp23-wp32-delivery-2026-09-30/self-checks.json` | `71fdd18ed76c7234c02e4cc0317082c61ca12040e1b1de511f5a7a627c1b2139`／35,018 | `82b1e332f32b0c794ad0908eca34a04b4bfe5d62ea0ed5f5de14166c46051be6`／35,361 |
| `review/wp22-wp23-wp32-delivery-2026-09-30/boundary-checks.json` | `91473989f3f6a1a03a6dc4faf612ccce3f82488aabb11ecfcf340d6bce3d1aee`／22,804 | `9ed3bb4698d5914b53760a95743518b0c3ed4dce79eb32ac499d7e327ddcc761`／22,848 |
| `review/wp22-wp23-wp32-delivery-2026-09-30/delivery-summary.md` | `055425c0f344492a62230d6a8dd5d8b44c0f8e825f88929b11a5b175b84e2f13`／5,696 | `ad1d9fac1769fa7d472d1f5137c9128e1d77eb88487e2e11cfb702c536ec9eef`／6,098 |
| `review/wp22-wp23-wp32-delivery-2026-09-30/new-observations.md` | `931f33583682bcd59fca52124c7cbafc29ab471a70736c9715ad672c1fa8bf77`／5,384 | `34e5049496914d11ee17944757fc4358d0eaae834c80a093a409654e92bf6089`／5,415 |

## 3. 各文件变更内容

- **WP23 主稿**：头部状态 → **Reviewed（限定静态范围，2026-09-30有限复审PASS_SCOPED；管理性回填）**，按报告 §4 的 A～G 具名；尾注保留被审 v1 `cd8b5e24`（34,418）与**被审 v2 `1a11060e`（40,939）**留史，声明回填后字节不冒充被审对象。正文行为未改。
- **WP23 附表**：头部状态同上回填；尾注保留被审 v1 `416ac411`（12,071）与**被审 v2 `afeab758`（13,534）**留史。数据目录未改。
- **feature-matrix F06-08**：WP23 子范围由 ReviewPending 改为 **Reviewed（限定静态范围，2026-09-30有限复审PASS_SCOPED；管理性回填——WP23 A～G…；被审主附表v2留史）**；WP22 子范围与 Inventoried 前向保留不动。
- **WP32 主稿**：仅同步 WP23 当前状态与完整身份——§9 完成依赖段、§10 通过范围段、依赖身份表（WP23 行改 `6343cfea`／41,529）；已接受行为、N01／N02 表述与具名历史未改；头部“引用WP23只限已核实交界，不表示WP23整体通过”保持原样（WP23 另行限定通过、不并入本包范围，该句仍成立）。
- **wp23-fixed.json**：status／artifacts／status_scope 更新；review_history 追加 v2 PASS_SCOPED 记录（被审 v2 完整身份留史）；bindings（16 个 sender）未变。
- **wp32-fixed.json**：WP32 自身 artifact 身份级联；WP23 绑定改当前身份，状态文字改“本轮有限复审PASS_SCOPED限定Reviewed回填版；仅引用已核实交界”。
- **self-checks.json**：WP23 条目 status／artifacts；WP32 条目 artifacts 级联；WP23→WP32 绑定身份与状态文字同步。
- **boundary-checks.json**：WP23→WP32 绑定身份与状态文字同步；binding_count 46 不变。
- **delivery-summary.md**：v3——WP23 两行状态与身份、WP32 身份级联、§3 材料哈希、§4 集合表述（F06-08 分别为 WP22、WP23 限定 Reviewed；限定通过集合＝WP01–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62）；v1／v2 摘要身份留史。
- **new-observations.md**：仅两处状态文字（WP23 修订 v2 已经有限复审通过）；O01～O06／N01／N02 观察内容未改。

## 4. 差异与分阶段绑定

十份统一差异见 [backfill-diffs/](backfill-diffs/)，逐文件绑定见 [diff-bindings.json](diff-bindings.json)。基线为有限复审 `recheck-v2/input-snapshot/`（919 项固定输入）。

- 九份差异（除 feature-matrix 外）绑定快照 → 当前最终字节，可从快照逐块重建到当前目标。
- **feature-matrix.diff 绑定快照 → 回填阶段身份 `9beb4b37`／56,107**：本批随后将在同一交付中加入 WP66-B／WP66-C／WP71 的 Feature 增量，矩阵最终身份以批末摘要、manifest 第六十五轮与主 TSV v40 登记为准；阶段身份不称为最终当前。

## 5. 保护与未决

- 复审报告／提示／检查／快照与历史回应／差异只读未动；首审与有限复审两轮 reviewer 原件、919 项 input-snapshot 未修改。
- 未重复回填 WP22／WP32；未借本次覆盖全局 review 的 16 项问题；未修改 WP26 或 N02 相关推断；未把 F06-08 扩大为所有媒体／插件／运行组合完成。
- 保留：N02 宿主未决、可选内容实际启用、宿主／媒体／插件、U01–U10、Demo、WP78→WP79→WP80 出口。

本次只做自有文本／哈希／JSON／差异操作；未运行参考代码、游戏、编译器或网络；未创建任务／Agent、未发其它会话消息、未提交／推送。
