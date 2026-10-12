# R4-U05 作者任务

本任务已获用户授权。目标是事实行为规格，参考和旧接受只读，不实现引擎、不转译Ruby、不合并main、不force、不删分支、不动Mac。完整规范以固定根findings为准，原稿须服从独立质疑后的精确化。保护既有正确条款，旧229/341/GR3只复用原qualified身份；仅受影响回归，不补签全部历史。

先读本目录 findings-input.json 和 handoff-findings.md 的完整正文，以及 read-scope.json、根 input-verification.json / resource-scope.json / dispatch-plan.json。源R按固定commit读取；正式输入仍是固定B。父任务提供本次发布回执的精确commit；先在准备checkout或用git show该commit读取根freeze-and-publication.json，取得任务包冻结commit/tree和author_start_commit，再创建作者worktree。回执是任务包的后继提交，所以作者起点不自嵌该回执；不能以浮动分支替代。共用当前环境的作者也必须独立worktree，不在登记员checkout或其他作者工作树修改。

证据分 SOURCE_STATIC、SPEC_STATIC、DERIVED_VECTOR（未执行）、TOOL_VALIDATION、EXECUTED_MODEL、EXECUTED_REFERENCE、EXECUTED_HOST_OR_DEMO。第四review已有4次隔离原函数调用；本准备未新增行为执行。媒体/地图/完整Demo/宿主不足不阻塞事实修订，条件静态向量不得写成真实UI、联网、像素或动画通过。未来兼容政策不在本次整改代选。

主责：GR4-M12-001

请求 gpt-6.1-sol / xhigh / service_tier=default / Fast=false；请求接纳即可，回显未知记UNVERIFIED。父任务填写真实任务/thread标识。

唯一正式写域（2条）：

- `deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md`
- `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`

证据仅写 `review/remediation-fourth-20261012-prepare/batches/R4-U05/author/`；禁止更新全球台账、其他批证据、review目录、旧报告或reference。按完整前提补正文/必要数据/静态向量和引用，勿整篇重写。28条之外不扩大。

从根freeze-and-publication.json的author_start_commit建立独立作者分支，完整记录输入commit/tree。提交普通整改分支后冻结候选commit/tree，提供全changed-path allowlist检查、正式文件完整bytes/SHA256/blob、逐finding全部验收映射、源/消费者阅读、反证及受影响回归。作者自查不构成独立PASS。候选回执可在后继证据提交绑定候选，不能自嵌候选commit。

返回候选冻结身份和证据入口给父任务/唯一登记员。作者只提交自身候选，不整合其他批、不登记ACCEPTED_SCOPED或CLOSED。无运行写NOT_EXECUTED_THIS_UPDATE，并保留固定第四review的4次限定历史执行。
