# 本轮独立 reviewer 合同

只 review。根 AGENTS.md 生效。固定交付 86b4d7e1d8645e75af91a215240f8786a5bb4ca8 / 42c29efb5422772a1d90f657f25983600f500f28；正式规格 167296dbe9e2384627b0ed696e87aeb01f211252 / 33598d8a2a3acdd093cc4fe23f48eea8666100f3。参考 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b / 7589c800b61ba13a13040ed0d686979b80a84fd0。所有受审材料只读。

只写自己 Mxx 新目录，不修改全局台账、正式规格、参考、公共登记或任何旧文件；不 commit/push。旧停止目录只是候选导航，不使用旧 PASS、不恢复旧任务。分配清单仅作初始导航；独立发现全部可得能力，搜索相关调用者、配置、schema、UI、工具；发现归属遗漏通知主角色。不要无限拆分任务。

模型要求 gpt-6.1-sol / ultra / Standard(default)，显式请求被接纳足够，缺回显记录 UNVERIFIED。不使用隐蔽 CLI 模型进程。新 reviewer 未参与受审正式字节的作者或登记工作，报告独立角色声明与实际 task ID。平台仅通过父会话显示 subagent，不能伪造独立 Desktop 链接。

每模块完成 report.md、findings.json、file-coverage.tsv、capability-coverage.tsv、spec-coverage.tsv、regression-review.json、junction-review.md。所有结果净室 prose/数学/案例，不复制源表达式或代码。SUPPORTED_STATIC、PARTIAL、UNRESOLVED、MISSING_MATERIAL、NOT_REVIEWED、N/A 分开；OBSERVED_RUNTIME 仅真实运行，本轮运行=0。数据静态结构审查、样本、全内容语义、实际启用、宿主执行分别记；禁止将扫描行数/名称/命中/身份计数当语义覆盖。

file-coverage.tsv：source_path,git_blob,category,read_scope,status,capability_ids,limitations。所有分配文件要有记录，未审不得填完成。二进制与备份/外部工具具体分类。

capability-coverage.tsv：capability_id,module,category,capability,source_paths,source_loci,spec_paths,spec_clauses,test_design,normal_failure_boundary,status,limitations。从参考能力建立分母，粒度按行为族，避免只罗列方法；必要参数、时序、取消/失败、持久状态、数学和消费者实质审查。

spec-coverage.tsv：spec_path,clause,source_paths,source_loci,status,test_design,limitations。每份正文所有有行为含义的条款/表族、数据附表、测试设计有对应证据或明确未知；不以文件级 COVERED 替代条款支持。

findings.json 为数组。ID GR3-Mxx-nnn；severity P1/P2/P3；status CANDIDATE/CONFIRMED/DISPUTED/DUPLICATE/UNRESOLVED；disposition REQUIRED_REVISION/USER_DECISION/OPTIONAL/UNKNOWN；title,module,capability,category,reviewer,source_evidence 与 spec_evidence 数组（repo,commit,tree,path,git_blob,loci,note）、evidence_level,premises,scenarios,current_vs_expected,impact,implementation_risk,consumers,historical_relation,recommendation,acceptance_criteria,dependencies,aliases,unknowns。没有发现用空数组，但不得凭旧 PASS 声称无问题。

历史 regression-controls.json 是原控制、关闭及完整 FINAL 定位的复用导航。按当前模块消费完整有效前提、反例、最低修订、确定复核；逐项 regression-review.json 记实际阅读范围、当前条款、相关新 finding、历史证据复用理由/精确身份与限制。不是重新运行229项。原4非必修保持旧裁决，新证据独立提新ID。

junction-review.md 按分配交界与新发现给正常/失败/边界判定、具体证据、另一模块消费者及未决。跨模块最终裁决由独立主角色负责；不要覆盖或抹掉异议。

report.md 记录能力覆盖分母、可得文件类别、实际审读范围、规格支持/缺口、净室质量、未决和运行=0。完成是有限静态约定范围的完成，不是资源/宿主/全内容/运行PASS。若材料限制，保留具体受影响能力和验收条件。
