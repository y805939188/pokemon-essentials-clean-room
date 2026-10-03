# WP66-B／WP66-C／WP71 交付摘要 v3（WP66-C 限定回填＋三项定点修订）

2026-10-01；规格提取方。有限复审（recheck-v2）结论：**11/14 CLOSED；WP66-C v2 PASS_SCOPED；WP66-B／WP71 各剩 1+1 项 P2（共 3 项）OPEN**。本轮＝**WP66-C 管理性回填＋WP66B-R01／WP66B-R04／WP71-R03 三项定点修订（v3）**。WP66-B／WP71 仍为 **ReviewPending（定点修订 v3，待复审）**；WP66-C 已回填 **Reviewed（限定静态范围）**；不启动下一提取批次。reference 固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、普通 Git 清洁；976 项固定输入与 reviewer 原件开工前复测一致。

## 1. WP23 限定回填（管理性，行为未改；回填差异已获首审通过）

依据有限复审[报告](../wp22-wp23-wp32-review-2026-09-30/recheck-v2/report.md)§4（PASS_SCOPED，A～G）。被审 v2 主稿 `1a11060e2a1a2c37052734fb8d264655f8179ec6bca0d122cbc07b8afafe6f4c`／40,939 与附表 `afeab7580e39bc0a0dc78d3d6ae13f9f0e4db321101dc78600452670b0888abe`／13,534 留史；回填后身份 `6343cfea…`／41,529、`20a561cb…`／13,995（见 §4 登记）。N02 宿主未决保留；净化／Hyper／N01 行为未动；N01（旧 WP23 可达性冲突）仍 CONFIRMED_STATIC 待专项处理，本轮不改旧稿。

## 2. WP66-C 管理性回填（A～E 限定通过）

依据 [recheck-v2 报告](../wp66bc-wp71-review-2026-09-30/recheck-v2/report.md)§6：主稿头尾与 F16-04 子范围回填 **Reviewed（限定静态范围，2026-10-01 有限复审 PASS_SCOPED；管理性回填）**。被审 v2 `665d0ae28594c8b6314bc0c489d360056f8a6f8dcee786e42a21ba9d35a8e4b9`（28,275 字节，36 场景）留史；回填后 `1fd83f230aef76b7990ad9dd8384f987f8acfcdb1a95f8889631e0653fb64fdc`／28,913，不冒充被审对象。行为未改；不扩为 WP66 族完成，不扩上游通过范围；C35 按「先完成排序再取消存入」受理，排序中直接 BACK 回退仍有效。

## 3. 三项定点修订（v3）

| 编号 | 修订 | 场景 |
| --- | --- | --- |
| WP66B-R01 | §6.2 会话参数初始化时点更正（场景建立时初始化；同场景再开搜索复制上次接受参数）；B35 改四状态分列：Start 无结果 → 持久模式已写、**当前列表不重建不重排**、会话参数不更新、编辑草稿来自旧会话参数；同场景重开 vs 退出整个图鉴再打开两条路径对照（Zeta／Alpha 例） | B35 |
| WP66B-R04 | 仅交付检查字面更正：身高／体重表均 **37** 项，体重零基 36＝具体值 5000、37 才是表长哨兵；旧 revision-v2 检查（留史、不回写）的 len=36 输入明确撤回，主稿端点表与 B37 未改 | 见 revision-v3/targeted-checks.json |
| WP71-R03 | T09 换合法可达初态（初始化五次均在格 5 旋转 → 中心与四邻角度 3；「仅格 5 角度 1」违反偶数交集不变量、不可达，§8 第 6 条）；T05 补第二对未完成；T07 改注「左移一格」＋第 3 行保持未完成；T08 同前提；T16 完成截断限定；§9 空槽拒绝限定未暂持块 | T05、T07、T08、T09、T15、T16 |

## 4. 当前身份与登记

| 对象 | 当前身份 | 字节 |
| --- | --- | ---: |
| WP66-B v3 `specs/ui/wp66-b-storage-and-pokedex-ui.md` | `4563171ab239231ed917c1d0ecfc138197482010b60f07aa397c6788a3003c4b` | 37,449 |
| WP66-C 回填后 `specs/ui/wp66-c-bag-item-storage-and-shop-ui.md` | `1fd83f230aef76b7990ad9dd8384f987f8acfcdb1a95f8889631e0653fb64fdc` | 28,913 |
| WP71 v3 `specs/ui/wp71-tile-puzzles.md` | `d41e0fedd9526743cb39bc984d44b810bfd66a44ab8a3582e9468ba3e41d7a02` | 24,170 |
| 矩阵 `planning/feature-matrix.md` | `d3ca0fd30862817393c4b615c9dd95a9c841297316d7f2c253c14eb52127b1d1` | 57,310 |

材料：回填回应与三项回应见 [revision-v3/revision-response.md](revision-v3/revision-response.md)；差异（相对 recheck-v2/input-snapshot）与绑定见 [revision-v3/](revision-v3/)；被审 v1／v2 与回填后身份分列。manifest 续**第六十七轮**、主 TSV 续**v42**（历史行保留）。

备妥定点复审材料后**停止**：不启动新工作包／第四包，不执行全局 16 项修订，不合入 B 批，不处理 N01 旧 WP23，不执行 WP78→WP79→WP80；未创建任务／Agent、未发其它会话消息、未提交／推送。reviewer 原件、快照、revision-v2（留史）与 reference 未动。Demo、宿主、媒体、插件、U01–U10 出口保留。

v2 摘要 `8458ca4424e47267f200697205577c65bf5a99c4f246dc0fe0cb8a7a0e1d8a07`（6,189 字节）留史于 recheck-v2 input-snapshot；本版替代之。

