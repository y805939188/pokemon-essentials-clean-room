# R5-U06 作者入口：资源选择、演出时间及界面操作

本入口可供父任务单独分发。现在可开始候选准备。

请求 gpt-6.1-sol / xhigh / default（普速），禁Fast；实际回显不可得记UNVERIFIED。真实task ID由父任务写入独立角色回执，预留槽不冒充已启动。

固定B5/R及本轮语义/发布身份；只提取行为规格，不实现新引擎、不复制参考代码、不改参考/冻结历史/main、不碰Mac。optional7、no-required7、政策6、M11-005内optional方面隔离；本update新增执行0，静态向量DERIVED_VECTOR，格式/hash TOOL_VALIDATION。模型回显不可得记UNVERIFIED，不审计额度或认证。

完整读取 [contract.json](contract.json)、[task-packet.json](task-packet.json)、[shared-contract-readset.json](shared-contract-readset.json)、[regression-readset.json](regression-readset.json)，以及冻结输入目标/门禁/限制。逐项按contract读取固定R源锚点、B5正文/附表/向量及原提出者和独立反证，完整条件保留在task-packet。严禁仅凭标题修订。

必修18项：GR5-M10-001, GR5-M10-002, GR5-M10-003, GR5-M10-004, GR5-M10-005, GR5-M10-006, GR5-M10-007, GR5-M10-008, GR5-M10-009, GR5-M10-010, GR5-M10-011, GR5-M10-012, GR5-M10-013, GR5-M11-001, GR5-M11-002, GR5-M11-003, GR5-M11-004, GR5-M11-005。实际整合依赖：R5-U02, R5-U03, R5-U04, R5-U05。可先按B5撰写自己scope；上游贡献未到则相应依赖标WAIT，不产生正式接受/CLOSED。

只写 `review/remediation-fifth-20261013-prepare/candidates/R5-U06/author/`。非共享正文用contract指定的formal镜像；共享内容用fragments片段，逐片段声明目标路径、B5锚点、所属ID、替换/插入位置、原正确行为和依赖。不写公共台账或工作树正式文件。R5-I对非共享只机械接入独立通过的字节，共享仅R5-I实际写入。

提交候选应含 author-response.md、finding-responses.json（每项全部mandatory criterion及静态向量/正常/失败/取消/部分提交/消费同步）、formal-diff.patch、fragment-manifest.json、source-reading-log.json、regression-results.json、validation-results.json、scope-conflicts.json、candidate-manifest.json。可按需要增加本目录内净化数据表。候选manifest记录固定输入、逐产物bytes/SHA256/blob、所有同步文件与仍WAIT的依赖；commit/tree由外部父任务绑定，避免自哈希递归。必须满足预期行为，可引用已正确主合同，不机械复制源API或结构。普通推送独立候选分支由父任务提供；不得修改准备分支的冻结contracts。

完成后返回固定candidate commit/tree、自己的输出入口、逐项结果、依赖/范围阻塞及执行0；候选待非作者复审。

冻结报告不在工作树时，使用仓库中Git对象 `git show <fixed-commit>:<path>`，或 tools/read-frozen-file.py 定向获取单个源/证据文件并核完整bytes/SHA256/blob；只取本scope必要原证据，不重复全仓1GB读回。
