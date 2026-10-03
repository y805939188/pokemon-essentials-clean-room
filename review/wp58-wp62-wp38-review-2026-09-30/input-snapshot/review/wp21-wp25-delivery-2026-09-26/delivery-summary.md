# WP21–WP25 批次交付摘要（含 WP18/WP19 状态回填记录）

日期：2026-09-26（Asia/Shanghai）。本目录为提取侧交付包，**不是**外审报告，也不是 WP80 sanitized 产物。工作区：`/Users/dingshinn/Desktop/pokemon-framework-reference/`；参考基线 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，`reference/` 全程只读。

## 1. WP18/WP19 管理性状态回填（依据闭合报告执行）

- 依据：`review/wp18-wp20-closure-review-2026-09-26/report.md`（`93f1de1c`，8,748 字节）§4 与同目录 `next-batch-prompt.md`（`cd213c33`，10,450 字节）。
- 回填前实测（与闭合报告 §1 固定输入一致）：WP18 v3 `4428049b`（36,889 字节）、WP19 v3 `6c669fcf`（35,935 字节）、WP20 回填后 `f8272acf`（35,018 字节）、矩阵 `5fc73d82`（38,333 字节）、manifest `9a566498`（73,407 字节）。
- 回填内容：
  - WP18 头部/§14 → **Reviewed（限定静态范围）**；回填后 `85368fe3`（37,294 字节）——管理性变更，差异见 `wp18-backfill.diff`（仅头尾两处）。
  - WP19 头部/§11 → **Reviewed（限定静态范围）**；回填后 `489984f7`（36,325 字节）——差异见 `wp19-backfill.diff`。
  - WP20 仅同步上游引用为"已 Reviewed"（管理性）；`f8272acf` → `f2f904e5`（34,978 字节）——差异见 `wp20-refsync.diff`。
  - 被审哈希 `4428049b`/`6c669fcf` 保留于 manifest 历史；回填后新哈希不伪称为复审对象。
  - 矩阵 F06-01/F06-02/F07-01、F06-03/F06-04 → Reviewed（对应子范围）＋前向 Inventoried。
- 至此 **WP01–WP20 全部限定 Reviewed**。

## 2. 本批三包（WP21/WP24/WP25 均已限定通过并回填）

| 包 | 文件（`specs/` 下） | 固定哈希（前 8 位 → 完整见 `current-hashes.tsv`） | 字节数 | 自身范围摘要 |
| --- | --- | --- | ---: | --- |
| WP21（**Reviewed（限定范围）**，回填后） | `pokemon-rules/wp21-dynamic-forms-and-display.md` | `19a36297` | 42,449 | 形态注册机制与全部 49 条注册/9 条复制的触发族目录（读取/创建/提交/战斗/蛋/位图/Primal 接口；含 R02 取值数据表）；提交副作用链与三类招式改写路径（R03 修正：直接换招标识保留槽位与 PP 提升计数、当前 PP 按新招式总 PP 钳制）；锁定与限时形态；标记/缎带/华丽大赛属性的读取与边界 |
| WP24（**Reviewed（限定范围）**，回填后） | `creature-rpg/wp24-player-trainers-partners.md` | `32594094` | 29,668 | 训练家/玩家字段与标识（编号三层语义）；玩家内容与初始命名；四类资源域与写入者；徽章与七项功能标记；训练家装载/版本/缺失反馈/调试新增；伙伴注册分阶段/再读取查询（BATCH-C02 同步）/参与谓词/战后双分支 |
| WP25（**Reviewed（限定范围）**，回填后；含 WP21 引用同步） | `creature-rpg/wp25-party-and-storage.md` | `edc275c5` | 27,058 | 队伍 6/盒 40（每盒默认 30、容量=当前长度）与伪位置；容器操作与界面流转（守卫按目标/持有条件）；限制分层；存入治疗（默认关）与持久状态交界；地区代理差异分列（BATCH-C02 场景同步） |

- 状态：三包均已限定通过（**WP21 于 2026-09-26 闭合复审 PASS_SCOPED；WP24/WP25 继承 PASS_SCOPED，回填接受**）并回填 **Reviewed（各自具名范围）**。本文件 v4：WP21 回填（被审 `4e475505` 保留历史；回填后 `19a36297`、42,449 字节不伪称为复审对象）；WP25 同步 WP21 状态引用（`edc275c5`、27,058 字节）。所有被审哈希保留于清单历史与差异文件。
- 关键前向引用（各文档 §依赖表详列）：WP22（Mega/Primal 生命周期）；WP23（Shadow）；WP26/WP38（赠送/捕获接收）；WP31（进化复制交界）；WP33–WP35（寄养/遗传/孵化）；WP39/WP40/WP42（战斗资格与刷新）；WP50（持有效果族）；WP51（AI 技能档）；WP54/WP64/WP66/WP67/WP68（设施/礼物/UI/小游戏）；WP62（图鉴）；WP04/WP73（编译写回/编辑器）。
- 主要未决（各文档 §未决具名）：`forced_form` 非调试写入者；华丽大赛完整流程（U04）；墙纸解锁写入者；地区化储存组合；徽章/功能标记写入者（U01）；伙伴+设施组合；多类型/HandlerHash 机制可用无用例等。

## 3. 逐包自检与版本固定记录

- WP21：首版自检后按首轮复审 WP21-R01～R06 修订（v2）：注册机制改用真实底层（单键/复制时绑定/无字符串归一）、触发族目录校正复制目标数与 HOOPA 归属并补 R02 取值数据表、招式改写分三类（直接换标识/交互学招/逐项删除）含 KYUREM 跳项例、标记编辑双界面对照、缎带升级/移除边界、华丽大赛属性消费者（Beauty 进化）与复制接收路径修正；`55a47313`（v2）。经定点复审按 WP21-R03（直接换招标识：保留槽位/PP 提升计数，当前 PP 按新招式总 PP 钳制；新增 15→5、3→3 两对照）与 BATCH-C02（球重置为 POKEBALL）修订（v3），`4e475505`（42,037 字节）。经闭合复审 **PASS_SCOPED**（R03 与 C02 关闭、未发现直接回归）后回填 **Reviewed（限定范围）**（管理性变更），`19a36297`（42,449 字节）。
- WP24：自检期内修正两处笔误与一处未证实概括（移除对战设施金钱写入者）；按首轮复审 WP24-R01～R03 修订（v2）：编号三层语义（记录 1 回退）、伙伴注册分阶段/身份 ID 当版本/参与谓词顺序/战后双分支、金钱守卫与分阶段统计（封顶不提示）；`8b06ddc4`（v2）。经定点复审 PASS_SCOPED 后按 BATCH-C02（查询键未命中语义、刷新三态）同步并回填 **Reviewed（限定范围）**，`32594094`（29,668 字节）。
- WP25：自检期修正屏幕/场景分层；按首轮复审 WP25-R01～R03 修订（v2）：容量=当前长度与 clear/直写语义、地区代理（pbMove 只复制/删除与墙纸失败）分列、界面守卫按"目标/持有"条件化；并同步 WP24 最终引用；`98b52717`（v2）。经定点复审 PASS_SCOPED 后按 BATCH-C02（不可存放对照、墙纸工具对照）同步、回填 **Reviewed（限定范围）** 并同步 WP24 引用，`46bd905d`（27,081 字节）。
- 每包均按 AGENTS 适用 17 项要求组织；数值/统计类规则未用参考表达式执行，形态随机与倍率档均以输入分布/表格表达。

## 4. 批末交界核对（通过）

1. **WP21 形态提交/查询副作用**：提交链（写入→清特性缓存→处理器→重算→图鉴登记）与 WP18 §3.4/§4.1（缓存与登记读取）、WP19 §4.6（重算/HP 写回）、WP20 §5.1（招式状态）逐条互引一致；与 WP15 资源边界（位图路径/缎带资源）不冲突（只引用，不重复定义）。
2. **WP24 身份规则**：拥有者构造（类型性别 + 字段语言）、外来判定（标识+名字）、伙伴重设拥有者，与 WP18 §6 一致引用，无重复定义。
3. **WP25 集合规则**："生物—队伍—储存"检查点本包部分完成——移动=同一对象（与 WP18 §5 复制语义区分）；治疗/进化准备保留引用 WP20 §3.2；守卫分层（领域 vs 界面）与 WP24 训练家层移除守卫一致；WP26/WP38 加入后仍需复核，不替代 WP78。
4. **追踪一致性**：三包矩阵增量、未决与前向引用与文档一致；批内上游修订（WP18/WP19 回填、WP20 引用同步）已传播到 WP21/WP25 的依赖引用；未发现规则重复定义或冲突。

## 5. 追踪与清单更新

- Feature Matrix（`8b83d668`，39,577 字节；v1 `5379d879`、v2 `bb037cea`、v3 `e0762970`）：五个 Feature 增量——F06-07（WP21）；F07-02、F07-03（WP24）；F07-04、F07-05（WP25）。闭合复审后全部完成回填：F06-07 → Reviewed（WP21 子范围）＋前向 Inventoried；F07-02～F07-05 维持 Reviewed（对应子范围）＋前向 Inventoried。
- 上游状态引用同步（管理性）：WP18 `85368fe3` → `0464ca07`（37,313 字节；§9 依赖行触发条件"已触发"）；WP19 `03167162` → `c7fb40fa`（36,406 字节；§9 依赖行"已触发"）；WP25 `46bd905d` → `edc275c5`（27,058 字节；§10 行"已限定通过"）。
- `planning/review-manifest-2026-09-19.md`：§1 当前版本表、§2.1 对应记录、§3 历史替代关系、§4 第三十二轮均新增/更新；闭合报告/提示与 `revision-response.md`、差异入册；WP21 被审/回填哈希与替代关系记录完毕。manifest 自身不自哈希，最终实测值由交付消息报告。
- `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` 已按 v7 重测（含本批全部交付、两轮修订与两次收尾材料）；本目录 `current-hashes.tsv` 沿用该主表（不再另建）。

## 6. 工作区差异记录（本轮，2026-09-26）

- 本轮写入：`specs/creature-rpg/wp18-…`、`specs/pokemon-rules/wp19-…`、`specs/creature-rpg/wp20-…`（回填/引用同步）；新增 `specs/pokemon-rules/wp21-…`、`specs/creature-rpg/wp24-…`、`specs/creature-rpg/wp25-…`；`planning/feature-matrix.md`、`planning/review-manifest-2026-09-19.md`；`review/wp18-wp20-delivery-2026-09-26/`（摘要 v4、TSV v4）；新增本目录（摘要 + 3 份回填差异）。
- v3 收尾追加写入（定点复审后）：`specs/pokemon-rules/wp21-…`（R03＋C02 修订）、`specs/creature-rpg/wp24-…`、`specs/creature-rpg/wp25-…`（C02 同步＋回填）；`planning/feature-matrix.md`（F07-02～F07-05 回填）、`planning/review-manifest-2026-09-19.md`（第三十一轮）；新增 `review/wp21-wp25-recheck-2026-09-26/revision-response.md` 与 `revision-diffs/`（5 份）；`review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv`（v6 重测）。
- v4 收尾追加写入（闭合复审后）：`specs/pokemon-rules/wp21-…`（Reviewed 回填）；`specs/creature-rpg/wp18-…`、`specs/pokemon-rules/wp19-…`、`specs/creature-rpg/wp25-…`（WP21 状态引用同步）；`planning/feature-matrix.md`（F06-07 回填）、`planning/review-manifest-2026-09-19.md`（第三十二轮）；`review/wp21-wp25-closure-review-2026-09-26/revision-response.md` 与 `revision-diffs/`（6 份）；`review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv`（v7 重测）。
- `reference/` 未修改；未运行游戏/参考脚本/编译器/网络；未提交/推送（工作区非 git 仓库）。

## 7. 送审指引与停止点

- v4 状态（固定哈希）：本批（WP21–WP25）**全部限定通过**——闭合复审（`review/wp21-wp25-closure-review-2026-09-26/report.md`）结论 WP21 PASS_SCOPED、WP24/WP25 继承 PASS_SCOPED；WP21 已回填 `19a36297`（42,449）、WP24 `32594094`（29,668）、WP25 `edc275c5`（27,058）；矩阵 `8b83d668`（39,577）、manifest（最终实测值见交付消息）。回填材料：`review/wp21-wp25-closure-review-2026-09-26/revision-response.md` 及同目录 `revision-diffs/`（6 份）。
- 进展：首版送审（三包 REQUEST_CHANGES，12 项必修＋1 组维护）→ v2 修订再送 → 定点复审（WP24/WP25 PASS_SCOPED 并回填；WP21 仅剩 WP21-R03）→ v3 修订（R03＋BATCH-C02 同步）→ 闭合复审 PASS_SCOPED → 本 v4 回填。**WP21 依外审结论登记 Reviewed（限定范围），非自批。**
- 回填为管理性变更（报告已批准）；被审哈希（WP21 `4e475505`、WP24 `8b06ddc4`、WP25 `98b52717`）保留于清单历史与差异文件，回填后新哈希不伪称为复审对象。
- 本批次至此**停止**；下一批 WP26→WP27→WP30 按闭合复审提示执行（另行记录交付），不启动 WP22/WP23 或其他包。WP78→WP79→WP80 阶段出口与 U01–U10 未决项保持开放。

## 8. 修订注记（v2，2026-09-26 首轮复审后）

- 依据：`review/wp21-wp25-review-2026-09-26/report.md`（三包 REQUEST_CHANGES；12 项必修＋BATCH-C01）与同目录提示；逐项核实与回应见同目录 `revision-response.md`，逐文件差异见同目录 `revision-diffs/`。
- 本文件同步项：§2 表行与状态、§3 修订记录、§5 矩阵哈希、§7 送审对象；旧被审哈希保留于清单历史与差异文件。
- 同轮管理性变更：WP19 三处旧上游引用文字同步（v3 已获外审闭合；见 manifest）；矩阵五行状态措辞。
- 未改动：§4 批末交界核对的结论（v2 修订不改变交界事实，只修正表述与数据完备性）。

## 9. 修订注记（v3，2026-09-26 定点复审收尾后）

- 依据：`review/wp21-wp25-recheck-2026-09-26/report.md`（WP24/WP25 PASS_SCOPED；WP21 仅剩 WP21-R03）与同目录提示；逐项核实与回应见同目录 `revision-response.md`，逐文件差异见同目录 `revision-diffs/`（wp21/wp24/wp25/feature-matrix/delivery-summary 五份，相对本轮 `input-snapshot/`）。
- 本文件同步项：§2 表行与状态、§3 修订记录、§5 矩阵/清单/TSV、§6 追加写入、§7 送审对象。
- 回填：WP24/WP25 限定 Reviewed（被审 `8b06ddc4`/`98b52717` 保留历史）；WP21 保持 ReviewPending（`4e475505`）。
- 未改动：§4 批末交界核对结论与 §8 的 v2 记录。

## 10. 修订注记（v4，2026-09-26 闭合复审后）

- 依据：`review/wp21-wp25-closure-review-2026-09-26/report.md`（WP21 PASS_SCOPED；WP24/WP25 继承 PASS_SCOPED，回填接受）与同目录提示；回填回应见同目录 `revision-response.md`，逐文件差异见同目录 `revision-diffs/`（wp21/wp18/wp19/wp25/feature-matrix/delivery-summary 六份，相对本轮 `input-snapshot/`）。
- 本文件同步项：§2 表行与状态、§3 修订记录、§5 矩阵/清单/TSV/同步哈希、§6 追加写入、§7 状态与停止点。
- 回填：WP21 限定 Reviewed（被审 `4e475505` 保留历史）；同步 WP18/WP19/WP25/矩阵的 WP21 状态引用；WP25 当前 `edc275c5`。
- 未改动：§4、§8、§9 的历史记录与批内结论。
