# R5-U02 独立候选审者入口

请求 gpt-6.1-sol / ultra / default（普速），禁Fast。必须与本批作者不同的真实任务。当前可前读固定输入；正式审查须等父任务提供固定candidate commit/tree及完整字节清单。当前没有候选PASS。

固定B5/R及本轮语义/发布身份；只提取行为规格，不实现新引擎、不复制参考代码、不改参考/冻结历史/main、不碰Mac。optional7、no-required7、政策6、M11-005内optional方面隔离；本update新增执行0，静态向量DERIVED_VECTOR，格式/hash TOOL_VALIDATION。模型回显不可得记UNVERIFIED，不审计额度或认证。

读 [contract.json](contract.json)、[task-packet.json](task-packet.json)、[shared-contract-readset.json](shared-contract-readset.json)、[regression-readset.json](regression-readset.json)。实际读取候选差异、固定R必要源/调用者/配置与B5全部本scope正文/附表/测试/共享主条款；直接反查必要原证据。逐项验证全部必修子范围、反例、正常/失败/取消/部分提交、必须同步文件、producer→write→consumer→display→persistence及准确旧owner/scope。对缺条件或未完成贡献输出明确FAIL/WAIT，不据作者声明、旧PASS或机械检查批准。

只写 `review/remediation-fifth-20261013-prepare/reviews/R5-U02/candidate/round-01/`：report.md、criterion-results.json、source-reading-log.json、regression-results.json、independent-validation.json、review-manifest.json（固定候选commit/tree、逐受审范围/文件身份、本人任务ID和独立性、请求参数及UNVERIFIED回显）。不修改作者字节或公共台账。不以review轮次数计新批次。

PASS只签该固定候选限定scope；上游未到可签明确隔离的局部候选，但依赖门仍WAIT。若内容随上游改变，仅定向重审影响部分。有效质疑及一次定向回应后继续；无新增实质证据不无限复审。

同审者可后续执行 [actual-reviewer-entry.md](actual-reviewer-entry.md)，不能把候选签名转到实际字节。

冻结报告不在工作树时，使用仓库中Git对象 `git show <fixed-commit>:<path>`，或 tools/read-frozen-file.py 定向获取单个源/证据文件并核完整bytes/SHA256/blob；只取本scope必要原证据，不重复全仓1GB读回。
