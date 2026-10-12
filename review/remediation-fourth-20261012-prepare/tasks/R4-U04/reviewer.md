# R4-U04 独立review任务

本任务已获用户授权。目标是事实行为规格，参考和旧接受只读，不实现引擎、不转译Ruby、不合并main、不force、不删分支、不动Mac。完整规范以固定根findings为准，原稿须服从独立质疑后的精确化。保护既有正确条款，旧229/341/GR3只复用原qualified身份；仅受影响回归，不补签全部历史。

先读本目录 findings-input.json 和 handoff-findings.md 的完整正文，以及 read-scope.json、根 input-verification.json / resource-scope.json / dispatch-plan.json。源R按固定commit读取；正式输入仍是固定B。父任务提供本次发布回执的精确commit；先在准备checkout或用git show该commit读取根freeze-and-publication.json，取得任务包冻结commit/tree和author_start_commit，再创建作者worktree。回执是任务包的后继提交，所以作者起点不自嵌该回执；不能以浮动分支替代。共用当前环境的作者也必须独立worktree，不在登记员checkout或其他作者工作树修改。

证据分 SOURCE_STATIC、SPEC_STATIC、DERIVED_VECTOR（未执行）、TOOL_VALIDATION、EXECUTED_MODEL、EXECUTED_REFERENCE、EXECUTED_HOST_OR_DEMO。第四review已有4次隔离原函数调用；本准备未新增行为执行。媒体/地图/完整Demo/宿主不足不阻塞事实修订，条件静态向量不得写成真实UI、联网、像素或动画通过。未来兼容政策不在本次整改代选。

主责：GR4-M05-001

请求 gpt-6.1-sol / ultra / service_tier=default / Fast=false；请求接纳即可，回显未知记UNVERIFIED。必须独立于作者，记录真实任务/thread标识。

当前门：READ_ONLY_PREPARATION_READY。可实际读R/B、完整前提/反例/精确化、caller/override/data及全正式集反证，在自己的 `review/remediation-fourth-20261012-prepare/batches/R4-U04/review/preparation/` 写审查计划和读取记录。作者尚未给候选，所以当前不得写候选/actual PASS。

正式写域为空；只读作者28条中本批路径（见batch-contract.json），只写 `review/remediation-fourth-20261012-prepare/batches/R4-U04/review/` 的自身具名证据。不能改作者正文、别的reviewer材料或全球账。

作者冻结后，核commit/tree/完整文件身份，读R证据、整批差异及必要消费者，逐条测试完整验收条件与正常/失败反向案例，一次有效独立质疑；输出candidate-v1/report.md、findings.json、identity.json、read-ledger.json及逐findingcriteria结果。问题仍在则FAIL/REQUEST_CHANGES，仅回本批修订，不自修、不签全域。

候选PASS后等唯一登记员按U01→U05整合并冻结实际commit/tree。随后核actual差异和完整字节、已经进入分支的共享消费者与受影响历史范围，一次独立实际整合检查，输出actual-v1/同样产物和限定ACTUAL_PASS。候选PASS不得转作实际PASS；签名绑定输入身份与scope。实际PASS只是登记ACCEPTED_SCOPED的前提，最终CLOSED还需U06。
