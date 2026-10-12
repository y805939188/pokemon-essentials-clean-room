# Pokémon Essentials 净室行为规格

本项目整理 Pokémon Essentials 的完整功能、游戏规则、状态变化与使用流程，为以后从零开发独立的现代 TypeScript 游戏框架提供行为依据。交付物是规格、数据条件和测试设计，不是 Ruby 代码翻译，也不是框架实现。参考实现的类、方法、文件组织和 RPG Maker 架构不约束未来设计。

**本轮整改已完成原合同两次最终独立审查：21/21 批次、341 条接受贡献、229 项必修 CLOSED、0 OPEN。** FINAL-1 与 FINAL-2 均通过；这是原必修整改控制的限定关闭，不能解释为全部原始能力或运行行为已经证明。

从 [当前交付入口](delivery/2026-10-11/README.md) 开始；需要开展下一轮审查时，复制 [第三次全局 review 完整提示词](delivery/2026-10-11/third-global-review-prompt.md) 到新的本地会话。本次发布只准备交付和合并计划，没有合并 main，也没有启动第三轮。

- [最终行为规格](deliverables/final-specification-set/)：七分类正文、附表与静态测试目录，全部字节保留在已审最终实际版本。
- [当前状态与精确身份](delivery/2026-10-11/current-status.json)：最终实际、两次独立报告、关闭状态与证明边界。
- [当前／历史材料导航](delivery/2026-10-11/history-navigation.md)：历史待审文字按原时点保留，使用者以当前交付状态识别阶段。
- [保留历史的合并计划](delivery/2026-10-11/merge-plan.md)与[重复内容整理候选](delivery/2026-10-11/cleanup-plan.md)。

已审最终实际 commit：`167296dbe9e2384627b0ed696e87aeb01f211252`，tree：`33598d8a2a3acdd093cc4fe23f48eea8666100f3`。本交付分支增加导航及完整原报告，未改正式规格、原稿、公共关闭登记或旧证据字节；新增导航本身不冒充已获 FINAL-2 签署的规格。

参考只读 HEAD：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。已知本地参考不是完整资源包，缺 Audio、Graphics、Plugins、Game.ini、Game.rxproj 和地图资源。此前运行观察、真实 Demo 链及行为案例执行均为 0；静态、未知、未读与资源／宿主限定继续有效。旧规格 README、规划和批次文件中的历史数字与 PENDING 文字保留，当前状态由本交付入口和固定独立报告解释。

## 第三轮 U07 当前有限整合候选（2026-10-12）

本节是当前第三轮阶段入口；上文保留各固定生成时点。六主题批的真实整合字节已分别获独立 PASS 并正式接受：23/23 必修、6/6 主题批；本轮最终 CLOSED 为 0，U07 实际整合独立验收待审。U07 是现有 23 项的整合与依赖关闭报告，不增加修复批次或必修分母，也不以复审次数计算完成率。

当前 [整合报告](review/remediation-third-20261012-prepare/U07/actual-integration/integration-report.md)、[逐项完整标准](review/remediation-third-20261012-prepare/U07/actual-integration/required23-matrix.json)、[正式字节身份](review/remediation-third-20261012-prepare/U07/actual-integration/formal131-current.json)、[批准登记](review/remediation-third-20261012-prepare/registration/approval-ledger.json)、[追溯后继](review/remediation-third-20261012-prepare/registration/traceability-successor.json)、[交界后继](review/remediation-third-20261012-prepare/registration/junction-successor.json)和[六批实际独立报告目录](review/remediation-third-20261012-prepare/U07/actual-integration/report-catalog.json)构成同一候选。固定 actual commit/tree 由 [独立验收输入](review/remediation-third-20261012-prepare/U07/actual-integration/actual-review-input.json) 外部绑定，不把旧整文件签名转移到新索引字节。

旧 229 CLOSED 与 341 exact tuple 均按原 qualified scope 保留；原始报告的 PENDING 表示各自生成时点。GR3-M09-001 可选暂缓、U08 未启动，GR3-M02-003 不需修订且不重开。参考只读固定 R；行为、参考、工具编译/转换、反序列化、真实 Demo、宿主交互与渲染执行均为 0 / NOT_EXECUTED，缺失资源及未知不得改成通过。
