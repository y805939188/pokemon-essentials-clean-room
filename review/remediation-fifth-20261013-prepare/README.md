# 第五轮整改冻结准备包 — READY

仅交接核验、有限合同与初始登记准备。B5/main `9366d9d17aaeac3b4414236468affa650fb3dd27`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；语义报告 `c0ff33024aea424c68d29f9778fe7c8e807d21e8`；最终报告发布 `f49d870c6fd616ab6736754a218a4553b5acac7f`。准备分支 `codex/remediation-fifth-20261013-9366d9d` 从B5建立，正式131子树仍为 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。

完整交接见 frozen-input；逐项全量规范事实、前提、反例、验收、正常/失败/排除、消费者和历史限定保存在各批task-packet，原证据固定指针见contract。没有重做全局review。

92必修（51P2/41P3），7 optional、7 no-required、6独立兼容政策及13限制分开。可审432参考/131正式/有效补充未审0是R5报告的有限静态完成，不授予宿主、资源、机器码或动态边界运行PASS。R4历史隔离4与R5新增隔离4分开；本update新增执行0。

| 批次 | 必修 | 作者入口 | 独立审者入口 | 实际整合依赖 |
| --- | ---: | --- | --- | --- |
| R5-U01 内容、编译、本地化及通用内核 | 34 | [author](contracts/R5-U01/author-entry.md) | [reviewer](contracts/R5-U01/reviewer-entry.md) | 无 |
| R5-U02 地图、事件、移动及野外交互 | 14 | [author](contracts/R5-U02/author-entry.md) | [reviewer](contracts/R5-U02/reviewer-entry.md) | R5-U01 |
| R5-U03 个体、NPC队伍、储存、道具及邮件 | 11 | [author](contracts/R5-U03/author-entry.md) | [reviewer](contracts/R5-U03/reviewer-entry.md) | R5-U01 |
| R5-U04 战斗实际执行、效果与异常调度 | 7 | [author](contracts/R5-U04/author-entry.md) | [reviewer](contracts/R5-U04/reviewer-entry.md) | R5-U03 |
| R5-U05 AI评分与实际执行的对应 | 1 | [author](contracts/R5-U05/author-entry.md) | [reviewer](contracts/R5-U05/reviewer-entry.md) | R5-U04 |
| R5-U06 资源选择、演出时间及界面操作 | 18 | [author](contracts/R5-U06/author-entry.md) | [reviewer](contracts/R5-U06/reviewer-entry.md) | R5-U02, R5-U03, R5-U04, R5-U05 |
| R5-U07 开发工具、内容编辑与转换 | 7 | [author](contracts/R5-U07/author-entry.md) | [reviewer](contracts/R5-U07/reviewer-entry.md) | R5-U01, R5-U03, R5-U06 |
| R5-U08 有限跨批整合、实际字节复审与登记 | 0 | [author](contracts/R5-U08/author-entry.md) | [reviewer](contracts/R5-U08/reviewer-entry.md) | R5-U01, R5-U02, R5-U03, R5-U04, R5-U05, R5-U06, R5-U07 |

第一波可同时分发U01–U07七位作者（92项），七位不同任务的独立审者可同时前读，候选完成后分别审固定字节；起始可出审查结论数0。每批1作者+1审者，共14角色，实际复审可复用该独立审者。U08另1作者/整合登记角色+1独立审者，等待7批所需贡献接受；不新增必修分母。父任务负责分发，未启动任何作者/审者任务。

所有候选只写自己目录；85个路径唯一语义写者，21个共享文件只由R5-I实际写，公共registration亦唯一R5-I。依赖边不阻独立候选准备；它们约束所需贡献实际整合/接受/关闭，未满足则WAIT。按scope接受不等于整文件接受或全问题CLOSED；共享文件各贡献齐备后整份验收。详见[图](contracts/graphs.md)和[依赖图](contracts/dependency-graph.json)。

[初始台账](registration/initial-ledger.json)：OPEN92，候选PASS0、实际PASS0、正式接受0、CLOSED0。初始账和contracts冻结，后续状态用新后继回执解释。CLOSED须全部子范围、同步文件、受影响消费者和依赖都满足，再经U08实际整合与同审者关闭字节验收/唯一激活回执。

更新请求sol xhigh、review请求sol ultra，均gpt-6.1-sol/default普速禁Fast；没有实际回显仅UNVERIFIED，不检查额度/认证。optional和政策不自动纳入mandatory；不明决策隔离并继续独立必修。

[交接核验](verification/handoff-verification.json)、[完整结构分块读取](verification/full-structural-reading.json)、[角色槽](registration/role-slots.json)、[机器分发入口](dispatch.json)。正式规格/公共历史未改；未merge/push main、不删除分支、不动Mac。
