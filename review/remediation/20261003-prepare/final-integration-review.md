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
