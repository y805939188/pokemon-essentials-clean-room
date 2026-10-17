# U02、U03 联合实际整合复审入口

配置必须为 gpt-6.1-sol / ultra / service_tier default。父任务提供实际 INPUT_BINDING_COMMIT；从该固定提交读取本目录 actual-review-input.json，再只按其 artifact_snapshot_commit `908273093e1f6b27fc58249417675dd62d146224` 读取受审结果。

完整执行 `review/remediation-eighth-20261016-prepare/coordination/actual-integration-review-prompt.md`。分别给出 R8-U02/GR8-KER-003 和 R8-U03/GR8-PBSW-001 的 actual integrated PASS/FAIL/BLOCKED，报告不能合并成无法区分两批的单一状态。两批候选均已由真实非作者分别PASS，报告及来源commit在输入manifest绑定。

正式目标为 WP04 §5.2 L196、WP60 §3.3 L45；每份完整文件读取并核候选一致性、累计保留、必要catalog/引用/公共贡献，不能只核两行。其余129个正式文件保持原字节；没有公共索引改动。候选报告中的助手tier未提供，不能把父云根任务的default设置转授给助手；本次由已配置根审者独立完整接收，任何并行审者都须由父任务明确配置ultra/default。

只写 `review/remediation-eighth-20261016-prepare/reviews/actual-U02-U03/r1/`。不改候选/正式文件、不签ACCEPTED/CLOSED、不接受其它未PASS批次或未回填打标。场景仍为静态推导/NOT_EXECUTED，不执行Ruby、游戏、宿主或新框架。结果交父任务转整合者；每批actual PASS及必要接收齐备后，才由整合者分别登记批次ACCEPTED并提供标签接受事件。
