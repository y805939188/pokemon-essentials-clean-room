# R4-U02 作者候选入口

本包只提交 GR4-M03-001/002/003 的有界事实规格修订，待独立候选复审；作者自查不构成独立 PASS。实际接受与关闭由唯一登记员按任务包后续门处理。

作者起点 `08a57fb55118914a74ac1ffaf617647c01df8938` / tree `8fc388710e3433890416f6d01247fd09df9d2ea8`；固定 B、R、最终第四review及发布回执完整身份见 input-verification.json。候选与后继发布回执不可互相递归绑定；精确候选commit/tree由后继 candidate-publication.json 给出。

- acceptance-map.json：15项完整验收和独立反证精确化，逐条正文/向量锚点。
- source-and-consumer-read-log.json / counterevidence.json：固定源码身份、实际阅读范围、消费者与有界反证。
- affected-regression.json：具名对照及GR3/C064旧资格，未执行与不转签限制。
- formal-identities.json：8正式文件完整bytes/SHA256/blob及B前身份。
- validate_candidate.py / validation-result.json：可复跑工具核验，不能替代源码语义复审或行为执行。
- execution.json：本批 NOT_EXECUTED_THIS_UPDATE；第四review历史4次限定原函数调用保留。
- integration-proposals.json：公共消费者只读提案，未改公共台账。

正式差异仅8条allowlist；新增26条 DERIVED_VECTOR / NOT_EXECUTED，不运行宿主/参考/行为模型。完整Demo/地图/资源及插件覆盖未证，非法范围未穷尽；不重启全球review。独立reviewer入口：tasks/R4-U02/reviewer.md（固定任务包08a57fb），父任务另派审者，作者未调度review。

真实任务角色 R4-U02-author；platform thread `01a130c3-eed0-73b0-9128-90bd04e3b00d`；源父thread `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`。模型请求 sol/xhigh/default/Fast=false，实际回显 UNVERIFIED；无额度审计。
