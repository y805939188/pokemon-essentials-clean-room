# 第三轮云端整改就绪与首次派发

READY。此提交仅完成有界就绪核验和派发；父任务已有用户开始更新授权，负责创建可见独立作者/复审角色。本角色是唯一整合登记角色，不兼任独立review。本次没有修改正式131、旧报告、参考、历史台账或main，没有运行模型CLI/游戏/静态行为案例。

固定最终交接 `d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65` / tree `c8a523150d75c8d1bede346857263ddd00ef0035`；main/D `86b4d7e1d8645e75af91a215240f8786a5bb4ca8` / tree `42c29efb5422772a1d90f657f25983600f500f28`；S `167296dbe9e2384627b0ed696e87aeb01f211252` / tree `33598d8a2a3acdd093cc4fe23f48eea8666100f3`。任务书完整213613bytes已分段读完；最终manifest6256569bytes、blob8657d7de3b6a10561a8048a6cd320478ded955db、SHA25676c969215071c3dfa8af75fd98550c59b8f92c3e2a8666637aa4903c33549ecd完整读取。manifest205附件逐完整字节/hash一致，连自身206Git对象已实际读取；131正式逐S/D/H/工作字节一致；A/B历史manifest身份分别保留，未混用。所有完整身份见 [readiness-check.json](readiness-check.json)、[handoff-file-identities.json](handoff-file-identities.json) 与 [publication-anchors.json](publication-anchors.json)。

R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 已在执行器以已有HTTPS授权只读取得，路径 `/workspace/pokemon-essentials-reference-fixed`；432 tracked路径、64保留ID关键source完整字节/blob/SHA一致。23必修source/spec/premise/scenario/acceptance完整可解引用，见 [required23-acceptance.json](required23-acceptance.json) 与 [reference-availability.json](reference-availability.json)。旧229/341保持qualified历史，无新全局review；一次固定身份校验见 [fixed-history-identities.json](fixed-history-identities.json)。

首批可并行：

| 批 | 必修ID数 | 作者派发 | 复审派发 | 精确候选路径 |
| --- | ---: | --- | --- | --- |
| U01 内核输入 | 6 | [author-task.md](U01/author-task.md) | [independent-review-task.md](U01/independent-review-task.md) | [candidate-paths.json](U01/candidate-paths.json) |
| U03 个体/道具/成长 | 4 | [author-task.md](U03/author-task.md) | [independent-review-task.md](U03/independent-review-task.md) | [candidate-paths.json](U03/candidate-paths.json) |
| U06 工具 | 2 | [author-task.md](U06/author-task.md) | [independent-review-task.md](U06/independent-review-task.md) | [candidate-paths.json](U06/candidate-paths.json) |

三个候选写集互不重叠；作者写隔离候选完整镜像及本批产物，当前正式文件只读；唯一整合员以后提交真实整合字节，再冻结commit/tree/path给独立reviewer。每批 frozen-inputs.json含精确Git身份，findings.json保完整canonical对象，regression-scope.json含定点控制和341 exact tuple，不要求递归全历史。父任务以最终交付管理commit为不可变派发资料版本，分别建立作者worktree/branch；复审必须绑定真实作者commit/tree，禁止浮动HEAD。

依赖：U01→U02（WP09仍由内核共享整合员写）；U03→U04（WP28有序交接）；U03/U04→U05；U01–U06→U07真实整合/登记报告。U07不是第7修复批。U08不启动，M09-001待可选决定，M02-003不重开。准确路径/写者/依赖见 [dispatch-plan.json](dispatch-plan.json) 和 [exact-write-owners.json](exact-write-owners.json)。

作者/登记 gpt-6.1-sol/xhigh，独立review gpt-6.1-sol/ultra，全部default。显式请求接纳有效，回显缺失UNVERIFIED，不审额度。候选、自检、独立候选复审、真实整合、独立实际整合复审、正式接受、依赖满足、最终关闭分层；当前23必修接受0/关闭0、6主题接受0、整合报告0，不用复审次数替完成率。

当前无需用户决定事项即可派发。未来bug兼容策略、尺寸产品范围/默认视觉、资源补交/扩大审查/运行及可选导航仅保留待未来决定，均不阻塞参考事实修订。缺素材/宿主/实际Demo与全内容未审限界继续保留，文件检查不能冒运行PASS。技术取消先核任务/commit去重再重试；真正用户停止与权限拒绝遵守。不得配置新凭据、force、覆盖或删除不明资料。最终管理commit及远端读回身份由外部最终回执给出，避免自嵌SHA循环提交。

## 第三轮 U07 当前有限整合候选（2026-10-12）

本节是当前第三轮阶段入口；上文保留各固定生成时点。六主题批的真实整合字节已分别获独立 PASS 并正式接受：23/23 必修、6/6 主题批；本轮最终 CLOSED 为 0，U07 实际整合独立验收待审。U07 是现有 23 项的整合与依赖关闭报告，不增加修复批次或必修分母，也不以复审次数计算完成率。

当前 [整合报告](U07/actual-integration/integration-report.md)、[逐项完整标准](U07/actual-integration/required23-matrix.json)、[正式字节身份](U07/actual-integration/formal131-current.json)、[批准登记](registration/approval-ledger.json)、[追溯后继](registration/traceability-successor.json)、[交界后继](registration/junction-successor.json)和[六批实际独立报告目录](U07/actual-integration/report-catalog.json)构成同一候选。固定 actual commit/tree 由 [独立验收输入](U07/actual-integration/actual-review-input.json) 外部绑定，不把旧整文件签名转移到新索引字节。

旧 229 CLOSED 与 341 exact tuple 均按原 qualified scope 保留；原始报告的 PENDING 表示各自生成时点。GR3-M09-001 可选暂缓、U08 未启动，GR3-M02-003 不需修订且不重开。参考只读固定 R；行为、参考、工具编译/转换、反序列化、真实 Demo、宿主交互与渲染执行均为 0 / NOT_EXECUTED，缺失资源及未知不得改成通过。
