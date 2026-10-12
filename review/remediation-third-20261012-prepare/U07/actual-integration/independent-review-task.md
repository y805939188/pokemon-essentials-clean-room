# U07 真实整合有限独立验收任务

父任务新建独立角色：`gpt-6.1-sol / ultra / default`（非 fast）。这是第三轮原 U07 的实际整合验收，不是新的全局领域 review，不增加修复批次，不审计模型额度／凭据／后端。作者、登记者不得代替独立 reviewer；不在执行器启动隐藏 CLI 模型任务，不自行另开模型任务。请求接纳即有效；工具缺失实际 model/reasoning/tier 回显记 `UNVERIFIED`，不要臆造。

## 唯一固定输入

- 仓库 `y805939188/pokemon-essentials-clean-room`。从父任务返回的精确伴随包 Q 读取本任务及 `actual-review-input.json`；Q 父提交是 P。不要把浮动管理分支／HEAD 当审核目标。
- 真正 current actual P：`8a0b36520b5c9c57dd893d9116cfae8620aea229`，tree `8fca4c1e4dbf051d7749276060623e2480f23992`。
- 上一 U05 正式接受 AC：`c2eb74c7cbcf8a190d5e902d871fbce44904efd6`，tree `7f830a0b27111a76b35a294c0e9a4a1d524a008d`。
- 原第三轮 H：`d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65`，tree `c8a523150d75c8d1bede346857263ddd00ef0035`；目录 `review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731`。
- 原 main交付 D `86b4d7e1d8645e75af91a215240f8786a5bb4ca8` / tree `42c29efb5422772a1d90f657f25983600f500f28`；原131 S `167296dbe9e2384627b0ed696e87aeb01f211252` / tree `33598d8a2a3acdd093cc4fe23f48eea8666100f3`。
- 参考 Maruno17/pokemon-essentials R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，`/workspace/pokemon-essentials-reference-fixed` 已只读可达。不访问用户 Mac、不改参考。

先读取仓库 AGENTS 和实际存在的适用 `.agents/skills`。完整冻结文件通过执行器 `git show <commit>:<path>` 读取；大manifest在连接器空响应不是空文件。完整字节hash检查是身份检查，不能当成实质评判。必要新 source 读取限于当前变化、依赖前提或具体反例；不递归重读旧全部历史。

六批已经在各自精确 actual 上独立 PASS 并正式接受，23/23必修、6/6主题批；最终CLOSED0。U07 P 未改131正式，44最新修订逐字匹配最新版批准 actual、87逐字匹配S。P新的公共／管理字节尚无U07独立签署。报告只读当前 P：Q 包装只帮助定界，不属于正式修订。

## 有限必读顺序与用途

1. Q本任务及 [actual-review-input.json](actual-review-input.json)：核对 P/tree、AC、22实际改动、11当前共享文件、131当前正式、7核心入口、patch完整身份。以精确diff `c2eb74c7cbcf8a190d5e902d871fbce44904efd6..8a0b36520b5c9c57dd893d9116cfae8620aea229` 和完整P对象读取。
2. P的 [integration-report.md](integration-report.md)、[scope-and-execution.json](scope-and-execution.json)、[closure-stage-plan.json](closure-stage-plan.json)、[integrator-self-check.json](integrator-self-check.json)：明确当前候选、自检、独立验收、正式接受、最终关闭分层；不能用自检或旧签名代独立PASS。
3. P的 [required23-matrix.json](required23-matrix.json) 完整读取：23 canonical全文、全部76条标准、具名前提/场景/未知、精确 local实际independent record全文及指针。逐项判断当前P保持/消费者是否充分；结合必要当前正式条款及案例。冻结的来源PENDING是当时状态，当前接受回执不是伪造其历史。
4. P的 [formal131-current.json](formal131-current.json) 与 [report-catalog.json](report-catalog.json)：一次核对正式身份、六批actual+报告commit/tree及36产物完整字节（各报告分支可达）。完整读取六份实际 `report.md`；其它已有local verdict依矩阵全文与准确指针复用，只在问题相关时读额外局部文件。不得无界重读所有候选尝试／raw／ACT。
5. P的 [dependency-closure.json](dependency-closure.json)：原U01→U02、U03→U04、U03/U04→U05门禁、最新WP09 U02/最新WP28 U04，七个有限消费者join。给每个join明确当前PASS/NEEDS_REVISION/BLOCKED及必要证据。特别核对旧本批规则在后继共享文件中的必要承接；不能把旧U01/U03整文件签名转给新WP09/WP28。
6. P的 [qualified-regression-reuse.json](qualified-regression-reuse.json)：保留229原CLOSED qualified scope、341 exact batch/ID/candidate/actual/report tuples；只消费六批已签的73个相关控制投影及必要当前字节变化。原完整qualification／precise tuple优先；A022/A059、G2-5/G6-5等排除/纠正继续有效。现有行已绑定对象身份不要求复审所有旧控制。当前具体变化或前提矛盾才能定点重验。
7. P的 `review/remediation-third-20261012-prepare/registration/junction-successor.json`：54既有交界、8既有链、18新增链逐个有限join结果；保留原前提/正常/失败/未知及历史状态，判断当前正式载体对相关修订的承接。未涉及字节/前提的原限定行可明确qualified reuse，不扩成新完整能力PASS。每行结果要区别复用与当前实质影响检查。
8. P的 [shared-file-delta.json](shared-file-delta.json)、11当前共享整文件及 `review/remediation-third-20261012-prepare/registration/approval-ledger.json`、`traceability-successor.json`、`finding-ledger.json`、`batch-ledger.json`、`current-status.json`：核对新whole-file hash、增量和索引一致性。五个prose保留AC全文逐字前缀，追加当前权威阶段限定；三份旧current ledgers仅有限状态／定位更新，三份新后继索引全文是当前输入。各自给明确有限当前影响判决；旧签名不可覆盖新字节。核对23接受/6主题接受/最终0、独立待审，六本批actual/report locators无错配，旧PENDING/旧交付描述被明确限定为各自生成时点。必要相对链接必须解析。

核心原手交书完整约213613bytes，manifest约6256569bytes均固定 H，整合登记角色已完整读取和一次完整核验。新U07角色利用此包的原合同完整字段、23完整canonical与准确核心身份，只在条款上下文确需时读取原prompt的U07/相关条款，不重新无限消费全局历史。

## 必须保护的判断边界

- 25保留=23 REQUIRED_REVISION、GR3-M09-001 OPTIONAL、GR3-M02-003 NO_REQUIRED_REVISION；无P1。初始必修仍23，U08未启动；可选导航及无必修例不重开。新链里引用M09只核既有消费事实，不把可选变必修。
- K40已经在U05实际修正，与同一连续文本busy/pause/full消息合同一致；普通全关闭路径不另触发恢复回调。C109是旧过宽叙述的限定说明，当前WP63/P34无位置→0事实未改，不借此另开修复。PA-P28/WP56/WP17/WP63及AI现有职责未修；其邻接前提保持。
- 正式行为规格供独立实现，不能翻译Ruby、复制代码或设计新框架。参考static来源、原缺素材/启用/宿主/未知不能升级成运行通过。
- 行为案例、参考、compile/convert、反序列化、真实Demo、输入/渲染/audio全部0/NOT_EXECUTED；Git／JSON／identity checks不是这些运行。
- 未来是否修复兼容历史bug不在这23事实文档控制里自动裁决。
- 不写正式规格、现有公共文件、旧review／receipt、reference；不写正式接受或CLOSED；不合main、不清理分支、不配置凭据、不force、不覆盖未知数据。

## 当前验收与关闭分层

原合同要求真实整合独立review、依赖满足、正式接受及最终关闭分层；第三轮并未规定重复两次全局FINAL1/FINAL2。你现在评判上述固定P，明确 `independent_actual_integration_verdict`，并说明是否满足有限整合接受条件。P里最终CLOSED0/独立待审是正确阶段，不是缺陷；此报告不预签未知未来文件。后续关闭登记产生新共享字节时，需要冻结并独立做有限关闭影响接受，可按父任务授权由原U07角色延续；不能宣称本次P报告已经签了未来关闭hash。

## 独立输出与可执行验收

父任务在精确Q基础上创建独立工作分支（建议 `remediation/third-U07-actual-review-20261012`，若已存在先核对不得覆盖）。只允许新建 `review/remediation-third-20261012-prepare/U07/actual-integration/independent-review/attempt-01/` 下六文件：

- `report.md`：固定P/tree/Q身份、独立角色、实际读范围/复用范围、23标准与跨批判决汇总、11新共享字节影响、54+8+18有限join、73控制qualified reuse、未知/0运行、所有真正blockers、当前接受与后续关闭边界。结果明确PASS/NEEDS_REVISION/BLOCKED，不把counts当质量。
- `per-id-verdicts.json`：`actual:{commit,tree}`、`verdicts23`（每ID含完整具名前提与76条标准逐条评判、current clauses/case证据、准确复用scope、局部actual与当前P分开、unknowns/runtime）、`dependencies7`、`shared11_current_verdicts`（全部P identity与scope）、`existing_junctions54`、`existing_chains8`、`new_chains18`（逐行明确qualified reuse或新影响检查）、`qualified_regression`（73有限控制原资格/tuple绑定及当前影响汇总）、`overall_actual_integration_verdict`、blockers、`formal_acceptance:false`、`CLOSED_written:false`。允许同等无歧义schema，必须完整可机器定位。
- `findings.json`：仅当前有界输入真正缺口；无新增required blockers写空集合或明确0。不无证重开229/optional，不隐藏NEEDS_REVISION。
- `input-snapshot.json`：完整固定P/树/Q及读取文件身份、source/spec范围、local复用记录、76条标准/有限join输入、11全字节身份，所有unknown/NOT_EXECUTED边界。
- `model-request-receipt.json`：独立角色身份、父任务可见新建请求及接纳、requested gpt-6.1-sol/ultra/default、非作者非登记者、native工具无tier回显则UNVERIFIED、无隐藏CLI/无quota audit。
- `output-identities.json`：其余5文件完整bytes/sha256/Gitblob；自己的完整身份由外部最终report commit/tree绑定，避免自hash循环。

正常提交并推送报告分支，对六文件做完整远端字节读回，返回精确 report commit/tree/branch/path、P/tree、每23判决、整体判决、blockers、未知/执行0。技术取消先核对是否成功避免重复派发；真实用户停止或权限拒绝遵守。登记者随后独立核对，作者不可登记自审PASS。
