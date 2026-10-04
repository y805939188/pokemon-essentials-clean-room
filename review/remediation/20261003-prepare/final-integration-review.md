# B02-G 实际整合交接（待 R-B02 Ultra）

状态：候选 PASS_SCOPED／13 正式文件原字节已整合／本次公共登记与八导航新字节待整合核验／229 项必修 OPEN／B02 下游 BLOCKED。

接受起点 `0a12de641542f9a59909d2a950c1de8df17ca09d`，完整候选 `46cd726c35e9d754a8e42b32986313ce3d4d1782`，独立候选报告 `94b012ee12d457aa4b99103477a0d35f083b1182`；报告直接后继候选，候选 v1 父从已接受起点派生。本次只快进整合完整作者/报告，未消费 B05未审内容、无冲突或 ours/theirs覆盖。候选判决范围是8主责行为/3局部贡献/A017八导航建议；当前应用的公共层另待 R-B02 对冻结的实际 integration SHA 核验。

仓库内可审入口：[B02-G完整交接](batches/B02/integration-stage-1/README.md)、[正式/公共/依赖身份](batches/B02/integration-stage-1/integration-manifest.json)、[逐ID登记](batches/B02/integration-stage-1/finding-registration.json)、[A017八导航原/后继对照](batches/B02/integration-stage-1/a017-navigation-successor.json)、[限定计数](batches/B02/integration-stage-1/scope-counts.json)。两份完整差异及精确payload身份以新增 diff-and-freeze.json 与 patch交接，最后 Git inclusion SHA 由最终发布回读给出，提交内不构造自引用哈希。

B01 接受段原文、中央规范ledger229行、原B01 manifest/计数/模型/PRE0/全部审查材料保留；approval/trace仅追加B02贡献行，以 finding+candidate 区分批贡献，不用重复贡献行计 canonical finding。A006原/附表/最终同步由本批独立候选覆盖；B01在旧源身份上的批准不替代本批新源身份。A015/B16、C003全部有效扩展/B21及WR12/B04、C081/WP36/B08继续开放；A017实际公共修正仍待B02-I和B21。原范围、严重度/别名、全部贡献/最终Ultra关闭门禁不变，B03/B06/B16等未开放或启动。

本轮自身验证仅为Git/文本/JSON/路径身份与保护边界检查，不代替独立Ultra。请求gpt-6.1-sol Max/Standard，review要求Ultra/Standard；实际三项UNVERIFIED，无降级/改配置。参考只读，参考程序/游戏/编译/转换/生成/反序列化/模拟/求解、运行观察、真实Demo、静态向量执行全部0；U01–U10/G01–G12/AX01–AX20及素材/宿主/插件未知保持。

---

以下 B01-C 接受与 B01-G 旧交接原文完整保留；其精确身份及历史时点不由本批覆盖。

# B01-C 有限接受登记与下游交接

当前状态：**B01 实际整合 PASS_SCOPED／14 项本批贡献已登记／229 项必修规范 finding 仍 OPEN／下游由父任务按固定计划指派**。此段只承接独立结论与接受记录；不增加正式行为或公共语义，不代替最终全局签收。

## 本次接受的对象与证据

- 实际被审整合提交：`93d0714ddfdb4900e946c0acd1cc80cf6431f0a0`；PRE0 差异基线：`8f3a811855fc43b5fe5eb7809931b4e1749200de`。
- 独立整合报告提交：`8a1fdfb2b582df4cefb408b56eea144a2e53dcfe`，直接后继上述整合，仅新增 10 份报告材料。[完整报告](batches/B01/integration-review-1/report.md)、[逐 ID 处置](batches/B01/integration-review-1/finding-dispositions.json)、[下游冻结范围](batches/B01/integration-review-1/downstream-freeze.json)均原样整合。
- B01-C 只更新 `finding-ledger.tsv` 的 14 项本批工作流字段、`approval-ledger.tsv` 的实际整合接受字段及本文新增段；候选结论、规范 ID/优先级/责任人/贡献批次、关闭门禁和其他 215 项工作流保留。当前两台账明确绑定被审提交与报告提交。
- 交付基线是本次 B01-C 登记后的 integration 冻结提交。完整 SHA、远端核验、相对 `93d0714…` 的树差异及 B02/B05 精确读写清单见提交后的外部 publication receipt 与 downstream handoff；提交内不写自引用 SHA。
- `integration-manifest.json`、`traceability-successor.tsv`、原 PRE0/方案/作者/候选复审记录及下文旧交接保留其原审查时点身份。它们的 `PENDING/BLOCKED` 与旧 hash 不是本次接受后的实时状态；当前结论由本段、两台账和新增独立报告承接，不循环回填历史 hash。

独立报告的范围是八份已审正式文件、B01-G 的公共登记及相关依赖在精确整合提交上的核验：7 项 B01 主责更正/后继勘误、6 项跨批局部贡献，以及 GIR-FD82-001 的入口/状态局部修正均通过。独立 41 项 Git/文本/JSON/路径检查通过；188 个被列举本地文件/目录引用可达，此数不代表全部仓库链接或锚点。规范关闭数仍为 0；这不是其他批次的通过结论或运行验证。

7 项主责为 `GIR-FD82-A001/A002/A003/A004/A009`、`WP80-B02-R01/R02`。其本批整合贡献已登记，但原全部贡献及最终 Ultra 关闭门禁仍保留。6 项局部贡献为 `GIR-FD82-A006/A020/C004/C016/C022/C080`，剩余范围如下；GIR-FD82-001 的原候选 `PROPOSAL_ONLY_NO_FORMAL_REPAIR` 作为历史候选处置保留，实际整合的入口修正判定另列。

## 保留的未完成范围

| 原规范 ID | 本次已验证范围后的欠项 | 责任/门禁 |
| --- | --- | --- |
| GIR-FD82-A006 | WP02 原规格:288、settings appendix:200、WP08 原规格:58 与最终 WP08:37 的 Debug 语言表述及相应同步/测试 | B02 与公共登记；原规格扩写须父任务明确授权 |
| GIR-FD82-A020 | WP19 完整 25 性格／20 修正／5 中性映射与属性测试，WP28 消费条款 | B05/B07；WP03/KR13 前提通过不等于整个领域通过 |
| GIR-FD82-C004 | WP36、WP73-B、原规格及编辑器测试；存档 0/PBS 省略后重编译的区别 | B08/B19 |
| GIR-FD82-C016 | metrics 编辑器/preview、WP15/WP16 原及相关领域条款；保存时非零形态路径与分节省略的区别 | B19 与相关领域/公共登记 |
| GIR-FD82-C022 | WP73-A 原规格:35、最终:19、编辑器保存/测试/入口追溯；复数 No 与单数写入器行为的区别 | B19/B21 |
| GIR-FD82-C080 | WP36 原/最终规格及测试；同节重复 Land 保留概率并清空旧槽、显式概率替换等规则 | B08 |

GIR-FD82-001 的 7 处正文审计断链继续由 B18/B21 承接，文件及原目标均未改：

1. `deliverables/final-specification-set/creature-rpg/wp68-triple-triad.md`
2. `deliverables/final-specification-set/user-interface/wp68-duel.md`
3. `deliverables/final-specification-set/user-interface/wp69-slot-machine.md`
4. `deliverables/final-specification-set/user-interface/wp69-slot-reels.md`
5. `deliverables/final-specification-set/user-interface/wp70-mining-data.md`
6. `deliverables/final-specification-set/user-interface/wp70-mining.md`
7. `deliverables/final-specification-set/user-interface/wp71-tile-puzzles.md`

这些正文的 `../../audit/source-traceability.md` 指向不存在的 `deliverables/audit`；正确三级回退为 `../../../audit/source-traceability.md`。Voltorb 正文已经采用正确三级目标，不计入这 7 处。

[证据勘误 R-B01-I-ERR01](batches/B01/integration-review-1/reviewer-evidence-errata.md)明确：旧候选复审的手列 7 项漏了 mining-data、误含 Voltorb，且子串检查不能区分二级/三级回退。旧“39 项全部有效”的表述须扣除此项支持检查；旧六份审查材料保持原字节，由本次独立解析与 Git 存在性证据承接。此勘误不改变规范 ID、P3 优先级、7 处实际断链、本批限定判决或 canonical OPEN。

## B02 / B05 可消费边界

固定计划为 `41fffb540c6483f5296ea0d33b789b75180d27ed` 的 [stage-locks.json](../../remediation-20261003-prepare/stage-locks.json) 与 [execution-schedule.tsv](../../remediation-20261003-prepare/execution-schedule.tsv)。B02-A、B05-A 的依赖均为 B01-I 与 PRE0，已由精确 `93d0714…` 的独立 PASS_SCOPED 和保留的 PRE0 满足。作者须从本次冻结交付 SHA 获取完整材料；原全局 findings/index 仍从 `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 按 Git 对象读取，不能把不在 integration 工作树的这两文件当作丢失或借改。

| 批次 | 作者范围及许可 | 精确写路径 |
| --- | --- | --- |
| B02-A | WP06–10；9 主责/12 贡献 ID；仅指定 finding 条款与本 WP 测试行 | 下列 7 文件 |
| B05-A | WP18–23；10 主责/16 贡献 ID；仅指定 finding 条款与本 WP 测试行 | 下列 10 文件 |

B02-A：

- `deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md`
- `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md`
- `deliverables/final-specification-set/generic-kernel/wp07-diagnostics-files-http.md`
- `deliverables/final-specification-set/generic-kernel/wp08-localization.md`
- `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md`
- `deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md`
- `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`

B05-A：

- `deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md`
- `deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md`
- `deliverables/final-specification-set/pokemon-rules/wp19-attributes-ability-and-stats.md`
- `deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md`
- `deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md`
- `deliverables/final-specification-set/pokemon-rules/wp22-transformation-data.md`
- `deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md`
- `deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md`
- `deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md`
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md`

B02-A/B05-A 的写路径交集、互相写→读交集均为空；如父任务采用锁允许的并发，两者须使用独立工作树、同一冻结读取身份、满足依赖，并将所有作者/公共作业/reviewer 合计限制在 3 个活动槽内。既有推荐排程仍为 B05-A wave 6、B05-R 与 B02-A wave 7；本次不改排程，也不启动任务。B02-G/B05-G/C 共用公共路径，必须由 A-REG 串行；任何冻结依赖被后续写入都须冻结/rebase 并复审受影响的新字节。

B02 的共享测试文件须保留已审 EP01–EP21 及无关 WP 行；B05 两测试族须保留 WP24–26、WP34 等无关行。原规格、历史报告/批准、AGENTS、参考均只读；B01 已获准的原规格扩写不能继承成 B02/B05 的写授权。公共导航、覆盖、traceability、中央台账/manifest 的更正统一交 A-REG。

未完成共用前提仍包括上表的跨批原/最终同步、所有贡献及最终 Ultra 签收、U01–U10/G01–G12/AX01–AX20、未读备份/样本与素材/宿主/真实插件未知。运行观察、真实 Demo 链、参考程序和静态向量执行均为 0。作者请求 gpt-6.1-sol Max / Standard，独立复审请求 Ultra / Standard；实际生效三项仍 UNVERIFIED，按已授权请求/平台接受依据执行，不用模型自述补证或改配置。

---

以下保留 `93d0714ddfdb4900e946c0acd1cc80cf6431f0a0` 时的 B01-G 作者交接原文。其待审/下游阻断语句记录当时状态；当前有限接受结果以上方 B01-C 段及绑定的独立报告为准。

# B01-G 整合核验交接（尚无整合审查结论）

状态：**候选PASS_SCOPED／已整合待Ultra核验／规范finding全OPEN／下游BLOCKED**。本文件是A-REG交接，不能当作独立整合报告或最终通过。

- PRE0：`8f3a811855fc43b5fe5eb7809931b4e1749200de`；从此干净起点整合。
- 完整被审候选：`c7e30a1197083e86315d735fcfde5e31574d935a`。
- 独立候选报告：`c919657840bb09394ce03a8a8688b02666f030dc`；只新增六份审查材料，直接后继候选。
- 保留双父提交的整合：`56a2391b49156abbf81b8e8f0add5ac7a9e5bff0`，父为PRE0与独立报告提交；无冲突、无选择另一版本丢弃内容。其树与review提交一致。
- 本轮追加公共登记提交的完整冻结SHA由提交/推送后的独立publication receipt给出；提交内不构造自引用SHA。

本次唯一新增语义是公共状态、导航、索引与后继追溯：scope/README统一为全集作者交付与全局review完成而229项必修OPEN，user-interface目录可达；两份B01测试索引更新为KC06/KR13/KL32/EP21；audit、coverage、Feature Matrix只增加本批当前限定与旧状态时点层；公共ledger、approval、candidate/当前integration身份与逐ID后继记录分列候选审核和新公共登记待审。**被审八份正式文件、全部作者与独立review原件、旧报告/批准和固定方案字节保留**；没有追加正式行为修订。

## 原ID、贡献与跨批欠项

| 原规范ID | 独立候选处置 | 当前剩余／门禁 | 规范状态 |
| --- | --- | --- | --- |
| GIR-FD82-001 | PROPOSAL_ONLY_NO_FORMAL_REPAIR | scope/README已作者修正待核验；七正文断链仍B18/B21 | OPEN |
| GIR-FD82-A001 | SCOPED_CORRECTION_VERIFIED | 实际integration与公共登记Ultra核验 | OPEN |
| GIR-FD82-A002 | SCOPED_CORRECTION_VERIFIED | 实际integration与公共登记Ultra核验 | OPEN |
| GIR-FD82-A003 | SCOPED_CORRECTION_VERIFIED | 实际integration与公共登记Ultra核验 | OPEN |
| GIR-FD82-A004 | SCOPED_CORRECTION_VERIFIED | 实际integration与公共登记Ultra核验 | OPEN |
| GIR-FD82-A006 | SCOPED_CONTRIBUTION_VERIFIED_DEFERRED | specs/kernel/wp02-rule-configuration-and-data-variants.md:288；specs/kernel/wp02-settings-inventory-appendix.md:200；specs/kernel/wp08-localization.md:58；deliverables/final-specification-set/generic-kernel/wp08-localization.md:37 | OPEN |
| GIR-FD82-A009 | SCOPED_CORRECTION_VERIFIED | 实际integration与公共登记Ultra核验 | OPEN |
| GIR-FD82-A020 | SCOPED_CONTRIBUTION_VERIFIED_DEFERRED | WP19 complete fixed mapping and stats tests；WP28 dependent consumer | OPEN |
| GIR-FD82-C004 | SCOPED_CONTRIBUTION_VERIFIED_DEFERRED | WP36；WP73-B；corresponding originals/editor tests | OPEN |
| GIR-FD82-C016 | SCOPED_CONTRIBUTION_VERIFIED_DEFERRED | metrics editor and preview；original/related WP15/WP16 domain clauses | OPEN |
| GIR-FD82-C022 | SCOPED_CONTRIBUTION_VERIFIED_DEFERRED | specs/demo/wp73-a-content-editors.md:35；deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:19；editor save/test/entry traceability | OPEN |
| GIR-FD82-C080 | SCOPED_CONTRIBUTION_VERIFIED_DEFERRED | specs/creature-rpg/wp36-wild-encounters-and-modifiers.md；deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md；WP36 tests | OPEN |
| WP80-B02-R01 | SCOPED_RESIDUAL_AND_SUCCESSOR_ERRATA_VERIFIED | 实际integration与公共登记Ultra核验 | OPEN |
| WP80-B02-R02 | SCOPED_SUCCESSOR_DESTINATIONS_VERIFIED | successor errata current index | OPEN |

GIR-FD82-001七份小游戏正文的审计断链不在B01-G写路径内，原字节保留：creature-rpg/wp68-triple-triad及user-interface/wp68-duel、wp69-slot-machine、wp69-slot-reels、wp70-mining-data、wp70-mining、wp71-tile-puzzles；逐文原目标/实际断链与正确三级回退对照记录在当前manifest，不把本轮入口修正称为finding解决。其他215必修项工作流不推进；WP08语言、WP19映射、WP36遭遇、WP73编辑器等仍按原计划等待各贡献修订与复审。

## 新增公共输入与依赖

当前原/最终/测试/公共入口的blob、完整SHA-256、字节和原被审/当前身份分列见 [integration-manifest.json](integration-manifest.json)。历史批准身份仍保留在audit原表及原报告；[traceability-successor.tsv](traceability-successor.tsv)承接当前原ID→正文→测试→后继登记→跨批欠项，[approval-ledger.tsv](approval-ledger.tsv)只登记候选实际PASS_SCOPED并明确整合NOT_REVIEWED_PENDING_ULTRA，[historical-errata.md](historical-errata.md)索引已接受后继更正。

本轮新增入口与索引没有候选判决；需要R-B01独立阅读scope/README准确状态、解析新链接、核测试ID/计数及原语义保护、检查audit/coverage/Feature当前与旧版本关系、检查229项OPEN及全部跨批欠项、复核实际完整PRE0→整合diff。相对候选新增项、合并记录、公共登记及每个文件的依赖/语义检查由manifest逐项列出，不能只核哈希声称通过。

完整diff取 `git diff 8f3a811855fc43b5fe5eb7809931b4e1749200de <frozen-integration-SHA>`；相对候选新增取 `git diff c7e30a1197083e86315d735fcfde5e31574d935a <frozen-integration-SHA>`。独立publication receipt及两份完整patch在执行workspace交接，并随最终冻结SHA提供。

实际模型/推理/速度UNVERIFIED；明确作者Max/Standard、核验Ultra/Standard，未降级或改配置。U01–U10/G01–G12/AX01–AX20和素材/宿主/真实插件等既有未知保持；运行观察、真实Demo链、参考执行、向量执行均0。main不合入、不force、不关闭finding、不开放或启动B02/B05。完成ordinary push并独立核远端后停止待整合核验。
