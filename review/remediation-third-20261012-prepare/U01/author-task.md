# GR3-U01 作者派发

固定交接 H `d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65` / tree `c8a523150d75c8d1bede346857263ddd00ef0035`；正式基线 D `86b4d7e1d8645e75af91a215240f8786a5bb4ca8` / tree `42c29efb5422772a1d90f657f25983600f500f28`，131字节等于 S `167296dbe9e2384627b0ed696e87aeb01f211252` / tree `33598d8a2a3acdd093cc4fe23f48eea8666100f3`。参考只读 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，本环境已实际获取在 `/workspace/pokemon-essentials-reference-fixed`。先读根 AGENTS；H及当前环境没有适用 .agents/skills 文件。完整任务书与manifest在 `review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/`；不要误用历史A/B manifest身份。

只修本批 REQUIRED_REVISION 事实规格、数学/状态/输入输出和静态测试设计。U08不启动，M02-003不重开，历史229/341只保完整qualified scope。不得翻译源码、设计新框架/API、修参考、修改旧报告/历史裁决/main、启动隐藏CLI模型任务、配置凭据、force或删除不明资料。参考bug政策、尺寸产品范围、视觉重设计、资源补交保留待未来决定，不阻塞准确事实补文。

gpt-6.1-sol/xhigh/default 作者；独立review为 gpt-6.1-sol/ultra/default，必须另一个角色且独立于作者与唯一整合登记员。请求接纳有效，回显缺失记UNVERIFIED。技术取消先核实际任务/commit状态去重后重试；用户停止或权限拒绝则遵守。每有实质进展汇报。按23必修与6主题批+U07报告统计，复审次数不作完成率。

本批ID：GR3-M01-001, GR3-M01-002, GR3-M01-003, GR3-M01-004, GR3-M02-001, GR3-M02-002。无前置批次，可与另外两初始批并行。

父任务先绑定最终交付管理commit并创建独立分支/工作目录；三个作者不能在同一checkout切分支。读取 `review/remediation-third-20261012-prepare/U01/frozen-inputs.json`、`findings.json`、`regression-scope.json`。每个finding完整premises/scenarios/acceptance_criteria是本批逐项结束标准。仅定点读取相关source/spec/qualified历史，不重新全局review。

精确候选写入映射（均从固定H正式文件完整复制后有界修订；新候选镜像保持完整上下文，正式131本轮作者直接只读）：

- `deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md` → `review/remediation-third-20261012-prepare/U01/candidate/deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md`

- `deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md` → `review/remediation-third-20261012-prepare/U01/candidate/deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md`

- `deliverables/final-specification-set/generic-kernel/wp05-events-extensions-plugins.md` → `review/remediation-third-20261012-prepare/U01/candidate/deliverables/final-specification-set/generic-kernel/wp05-events-extensions-plugins.md`

- `deliverables/final-specification-set/generic-kernel/wp08-localization.md` → `review/remediation-third-20261012-prepare/U01/candidate/deliverables/final-specification-set/generic-kernel/wp08-localization.md`

- `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md` → `review/remediation-third-20261012-prepare/U01/candidate/deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md`

- `deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md` → `review/remediation-third-20261012-prepare/U01/candidate/deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md`

- `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` → `review/remediation-third-20261012-prepare/U01/candidate/deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`


不需要改的候选文件可以不创建；禁止用空文件或局部摘录充当完整候选。所有跨域/公共变更通过traceability-proposal与registration-proposal交唯一整合登记员，禁止写其他批目录或公共台账。精确作者附属写路径：

- `review/remediation-third-20261012-prepare/U01/author-report.md`

- `review/remediation-third-20261012-prepare/U01/author-self-check.json`

- `review/remediation-third-20261012-prepare/U01/candidate-identities.json`

- `review/remediation-third-20261012-prepare/U01/candidate.patch`

- `review/remediation-third-20261012-prepare/U01/traceability-proposal.json`

- `review/remediation-third-20261012-prepare/U01/registration-proposal.json`

- `review/remediation-third-20261012-prepare/U01/model-request-receipt.json`


每项自检列实际候选path/条款、完整前提、正常/失败/边界结果、保留unknown、相关旧控制对照。静态设计全部NOT_EXECUTED；文字/身份检查不作游戏行为PASS。candidate-identities列每文件base blob/SHA256/bytes及新blob/SHA256/bytes；candidate.patch必须是可作用于固定正式基线对应路径的完整差异，apply前由整合员先核base，作者不apply到正式目录。报告返回精确作者commit/tree和changed paths。只选择性提交自己允许路径，可正常推独立分支，无force。

作者自检完成仍为CANDIDATE；不得自行写独立PASS、正式接受或CLOSED。父任务把作者精确commit/tree和候选manifest交独立reviewer；其接受后的真正整合字节仍需独立实际整合复审。


WP09候选归U01唯一作者；U02启动前，由唯一整合员冻结实际承接字节并登记prior/new SHA；U02作者只交WP09建议，最终写者仍为内核共享整合员。
