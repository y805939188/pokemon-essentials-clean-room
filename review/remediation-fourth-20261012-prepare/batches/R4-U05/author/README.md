# R4-U05 作者候选证据

任务：`R4-U05-author`；真实执行 thread/task ID：`01a130c4-6a34-7221-b8d4-20e3e887600e`。父来源 thread：`01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`。本目录只记录作者事实修订和自查，独立 reviewer 由父任务派遣；无作者自签独立 PASS，无正式接受或关闭登记。

固定任务包／作者起点 `08a57fb55118914a74ac1ffaf617647c01df8938`，tree `8fc388710e3433890416f6d01247fd09df9d2ea8`。准备发布回执从精确后继 `a53b11789bdfe0ee6a373e0c705a2c79f5187400` 读取，其冻结作者起点与父任务提供值一致。分支 `codex/remediation-fourth-R4-U05-20261012`，独立工作树 `/workspace/r4-u05-author`。原 checkout 保持固定 B。

只修改两份批准正文：WP73-B §6.1／§6.2／§6.4 的复制边界及 §11 对照引用，测试目录 WE-M11 的非空前提及新增 WE-M11-E01 静态向量。既有 M01–M22 编号保持；E01 是 M11 补充向量。没有新正文文件或生产代码。

- `input-check.json`：任务包、发布回执、固定 B/R、最终第四 review 与 handoff 完整字节绑定；六份参考文件完整 bytes/SHA256/blob；28正式写域不交；当前输入漂移检查。
- `read-ledger.json`：实际阅读的 source／消费者／历史边界及结论；不含参考代码复制。
- `negative-search.json`：固定 B 的131篇正式 Markdown 中本 finding 的反证检索位置；仅具名上下文语义阅读，不是新全局 review。
- `self-check.json`：四项验收、静态反例／正常／反向对照与受影响回归映射。
- `formal-file-identities.json`：两个完整正式文件的字节身份。
- `scope-check.json`：全 changed-path allowlist、未受影响章节／测试目录其它字节保护、JSON与 diff 格式检查。
- `verify-batch.py`：仅字节、绑定、范围及格式检查；不运行参考函数、编辑器、模型或宿主。运行方式：`python review/remediation-fourth-20261012-prepare/batches/R4-U05/author/verify-batch.py preflight /tmp/r4-u05-reference.git`。

候选 commit/tree 由后继 `candidate-publication.json` 绑定，避免递归自嵌。`candidate-remote-readback.json` 记录新空对象库从远端 fetch 后完整 changed-file 字节比较；候选与后继回执的冻结身份分别记录。

执行范围：`NOT_EXECUTED_THIS_UPDATE`。所有新增结果为 SOURCE_STATIC／SPEC_STATIC／DERIVED_VECTOR（未执行）；哈希、Git和JSON检查为 TOOL_VALIDATION。保留固定第四 review 的4次限定 EXECUTED_REFERENCE 历史回执，不扩大、不重新认证、不冒用于本 finding。完整宿主／Demo、媒体、物理输入与自定义插件未验证。未来兼容政策留待独立决策，不修改参考。

适用根 `AGENTS.md` 已完整阅读；没有路径级额外指令。本任务是仓库限定文件修订，未调用其它技能。模型请求承接 `gpt-6.1-sol / xhigh / default / Fast=false`，实际回显 `UNVERIFIED`，未做后端或额度审计。

独立 reviewer 入口：固定任务包 `review/remediation-fourth-20261012-prepare/tasks/R4-U05/reviewer.md`，连同 `findings-input.json`、`handoff-findings.md`、`batch-contract.json`、`read-scope.json`。reviewer 必须从后继回执取得精确候选 commit/tree，实际读取整批差异、固定 source 与具名消费者；本目录不能替代独立复审。实际整合与接受由唯一登记员串行执行。
