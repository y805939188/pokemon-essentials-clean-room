# 给原提取会话：v5仅更正记录，不改行为规格

工作目录 `/Users/dingshinn/Desktop/pokemon-framework-reference`。v4有限复审已关闭全部五项行为残留，累计36/37 CLOSED，唯一剩余BATCH-R02为P3交付记录。遵守AGENTS.md与reference只读要求。

先读 `review/wp72-wp73ab-review-2026-10-02/recheck-v4/report.md`、`change-counts.json`和`next-task-inputs.json`。这次只新增记录更正，不再修订任何行为主稿、案例行、入口表或效果目录，不再扩源；不要为了使旧“改了两行”的声明成立而实际改案例。

## 只需这份更正

在 `review/wp73a-delivery-2026-10-02/revision-v5/` 新建 `record-correction-note.md` 与 `checks.json`，作为本批统一记录更正。可用一个note合并回应与摘要，不要求重复文件；WP72/B不需要再生整套v5交付。note应明确取代v4错误记录，旧v4文件和主稿里的带日期v4工作量注记留史不改。

准确写入以下事实：

- **WP73-A v3相对v2**：实际修改M15/M20两条案例；**v4相对v3**：案例行实际修改为0，M15/M20字节未变；累计相对v1仍为9；无新增/删除案例ID。不要把v3的两条改动继续称为v4或v5的本轮改动。
- **本次v5**：仅元数据更正，三包主稿/案例/附表均无改动，新增案例ID为空。WP72 v4案例改动0、累计9；WP73-B v4案例改M05/M09、累计8，这些已正确的事实保持。
- **WP73-B附表链**：v2为069f97b6／9,317字节；v3为91f4a26f／9,680；v4为51386600／9,785。069f97b6是v3修订的前态，不是v3表自身，也不是v4的直接前态。完整身份直接引用本次change-counts.json。
- WP72 v3附表3行行为＋1行格式共4行的更正已正确，沿用v4 record-correction-note，无需重生。

checks用文本比较实测这些数量：案例行以原有M编号定位，比较recheck-v3/input-snapshot里的v3主稿与当前v4主稿；WP73-A20行均相等。按轮次命名字段，明确“本轮v5案例改动0”“v4相对v3 A为0、B为2”“累计9/9/8”。身份核验与实际阅读分开，不声明新读源码或运行验证。

## 七个通过对象全部保持

| 文件 | SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/demo/wp72-debug-contexts-and-controls.md` | `d6ee4e2d96f7230f5b8298a5fafa066a9139c3ea4005074647ca1d84425d61d4` | 88,617 |
| `review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md` | `c9492b0814ec7d9e1f5828ae4c3612eab466fb36282658d6fa19623588afade4` | 25,856 |
| `review/wp72-delivery-2026-10-02/revision-v2/battle-effects-catalog.md` | `6bba8070da27c1c9dd298781d27064fe935f4581b942477c6a3c24ed2532bdf2` | 11,204 |
| `specs/demo/wp73-a-content-editors.md` | `69053cf27f5d2d3c0b331e9ffa430f65e66c811f7648ba85c50670c6dbd183a9` | 51,685 |
| `specs/demo/wp73-b-world-editors.md` | `e4c9543d491e871d8de1a51e60e0fe3c4cc991a41ca7419b8c80d416b6731786` | 47,985 |
| `review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md` | `48a6fc8c18673652794e4ba5430763c159f95a5bd5c5ef8fc5b5a74e781fbffd` | 12,511 |
| `review/wp73b-delivery-2026-10-02/revision-v4/entry-coverage-table.md` | `5138660038c440beb2da8c4a41de4f1eff8a1f00a1806ea9855bab99137114fb` | 9,785 |

上述文件都不改，因此不生成新的主稿/附表diff、不输出空diff，不需要重制入口表或120项目录。source-identities可引用已核验版本并复测，无需机械复制整套文件。31项旧闭环＋本次5项新闭环、WP61（11/11）、WP53、WP37、WP65、WP67-A/B、GR-001～016、WP23-N01及所有旧批准保持。

## 末检与停止点

新增note/checks按实际文件数登记，不套固定增量；manifest§1与TSV实测，历史§2/§3/§4只续写，阶段末检单独保存避免自指。Matrix不需要为这次纯记录更正改变范围或宣称Reviewed。当前基数manifest115轮1,318＋2、TSV v90共1,223条，完整前态身份见next-task-inputs。

检查新note/checks不复制源码表达式、统计按实际证据写，七个保持对象及旧作者/审查材料全部字节不变。返回更正note/checks路径、实测结果和登记，停止送仅BATCH-R02的记录复核。复核通过后才准备WP74＋WP75＋WP76的执行交接；本轮不开始该批。

不修改reference，不执行游戏/战斗/编辑器/编译/保存/反序列化，不写参考行为模型；不创建聊天/Agent、不发跨会话消息、不提交推送。
