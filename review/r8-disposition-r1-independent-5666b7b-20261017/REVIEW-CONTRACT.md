# R1独立复审分工合同

新工作树 `/workspace/r8-disposition-r1-review`；固定候选 `5666b7b912e2fb79b5119283ee6a37401a7071db`。作者目录 `planning/implementation-routing/r8-20261017/`，新协议是该目录根 `review-prompt.md`（revisions/r1/ 内没有独立review-prompt）。先读根AGENTS、README、R1 README和完整review-prompt及R8 DELIVERY/review-SKILL/handoff相关范围索引。

固定旧候选 `d62b41f4d620e50bb04c80a7505374bd284d8210`，旧独立FAIL报告 `a0352c7fba38391afc535525988245701d5ce202:review/r8-disposition-independent-d62b41f-20261017/`，旧工作区只读镜像仍在 `/workspace/pokemon-essentials-clean-room/review/r8-disposition-independent-d62b41f-20261017/`。以Git对象核验身份，不能把作者处置映射当独立结论。

当前接受payload `908273093e1f6b27fc58249417675dd62d146224`，正式树 `6ae817df5b11eafdec671214b0d04e542ad364bc`；ACCEPTED回执 `861f7a44a6f763c265a11761ab17a8ec3b55f304:review/remediation-eighth-20261016-prepare/acceptance/U02-U03/receipt.json`；actual报告 `548d6bb9a21d0967680445c013e66d9d5661d2d6`。已按精确SHA fetch，工作区正式正文仍为B8，只能用git show读取908当前字节。只有U02/U03接受回填；其余pending和最终整合待办必须保留。

只写本新review目录下自己的agents前缀，不改作者清单/正式规格/参考/main/旧报告，不切分支或提交。只分析Markdown/JSON/Git，不运行Ruby/游戏/宿主/业务向量/框架。不再自行spawn抢占slots；需要补分工告root。

负责域内必须覆盖全部旧行（含旧PASS/FAIL/待查）、新活跃行、全部退役/metadata单元、相关catalog章节及跨域消费者。完整读旧本域报告/results及原finding；逐44组中分配的组给PASS/FAIL/待查。按实际字段差分判断合理PASS能否继承：证明来源与相关责任/去向/边界未变且不受同根因影响才继承；变更或受影响必须重新语义阅读相应完整源节/混合表格及必要消费者。记录真实新阅读区间与继承依据；不是抽样，也不是强制再读所有不受影响的旧全文。

逐旧ID验证新active或retired恰一次；旧source完整对象不变，retired去掉retirement后与d62完整行一致；新增ID不复用。独立检查functional_scope、父子扣除、不重计/不漏行为、纯元数据不留空壳；新职责文本要真正说明谁拥有状态/规则/输入表现，不能只依模板造理由。章节级粗标允许合理合并，不逐句造ID；未知原型不阻正确粗标，待验证不免分类语义审核。

输出每域 `*-report.md` 与 `*-results.json`，至少包含：

- `old_feature_results`: 每个负责旧ID的旧verdict、新PASS/FAIL/待查、active/retired处置、具体reason、继承或重读方式、finding_refs。
- `active_feature_results`: 每个负责新活跃ID的PASS/FAIL/待查及独立理由（包括追加ID）。
- `retired_metadata_results`: 每个负责退役/metadata单元定位、消费者/非功能处理结论。
- `finding_results`: 每个原finding_id的PASS/FAIL/待查、全部原case及相关同根因/新增子行是否修正的证据，不只抽样。
- `reading_ledger`: 每文档path、固定commit、完整身份、实际新读区间、哪些旧完整阅读信用被继承及为何适用；诚实标未读/待查。
- `new_findings`: 具体ID、严重度、源行/候选JSON pointer/为何不满足/必要修正。

生成view/关键字段/schema/全局验收与保护由root复核；各域仍须检查本域可读视图、依赖、状态和适用版本语义。所有新结论只适用于5666b7b固定候选；不能提前称最终整改/原型通过。

用户维持gpt-6.1-sol ultra/default。工具不暴露权威执行echo或云任务UUID时逐字段UNVERIFIED，不将继承/自然语言请求冒充真实telemetry；原生工具广告priority也不当作default资格证明。
