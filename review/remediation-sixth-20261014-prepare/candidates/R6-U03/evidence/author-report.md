# R6-U03-A 作者候选

GR6-O-001、GR6-O-002 的正文修订和作者静态验证已完成，状态为 **AUTHOR_READY_FOR_NON_AUTHOR_REVIEW**。没有作者自签的独立 CANDIDATE_PASS、正式接受或 CLOSED；指定 ultra 非作者复审由父线程另派。

作者分支为 `codex/remediation-sixth-r6-u03-author-20261014`，从固定准备提交 `469a268b92daed7b4d28d7fd0da75520cbb7228f` 创建。正式基线为 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；两份 tree、主载荷 bytes/SHA256/blob/mode 均已核。请求 gpt-6.1-sol / xhigh / default tier / default 普速，实际有效配置和作者平台 UUID 为 UNVERIFIED；依用户覆盖指令没有启动 CLI、配置追查或额外代理。实际根 `/workspace/pokemon-essentials-clean-room`，R 恢复为 `/tmp/r6-u03-reference.git` 的固定只读对象上下文，无检出源工作树，路径映射见 [execution-snapshot.json](execution-snapshot.json)。

## 修订与证据

| ID | 实际正文与目录修改 | 验证 |
| --- | --- | --- |
| GR6-O-001 / required P3 | WP60 §4.4.3 明确允许咬钩 false 不抽 bite；随机目录改成等待、咬钩、窗口、收竿四阶段的到达前提与次数，限定为协调器自身。同步 FS05/FS11，新增 R6-FS01–11。 | 源 Fishing 1–110 全文、三竿回调与公共事件助手链新读；无表/加速无表/取消/未咬钩/超时/普通及 auto 成功、开始/等待/动画/结束消息异常前缀逐项静态推导。保留 5–10、段数+1、首空段、全部阈值和整数有效概率、strict>截止及输入优先、正常清理、统计/遭遇调用方分工。 |
| GR6-O-002 / required P3 | WP13 §4.1 改为本次更新从0计数、每轮先+1、第101轮在业务/等待/分派之前请求图形更新，正常归零；正文纳入 terminal 后空列表轮。新增 R6-EV01–06。 | 源 Interpreter 1–454 全文、分派/终止及116有界上下文新读；98注释无请求，99注释在终止后请求，100注释在终止前请求。提前false/等待后次从0、Graphics请求失败未达归零/分派、独立depth>100均核；不把请求当已渲染或输入poll。 |

三份实际候选正式路径均在 `../mirror/deliverables/final-specification-set/` 下：

- [engine-overworld/wp13-map-events-npc-followers.md](../mirror/deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md)
- [engine-overworld/wp60-fishing.md](../mirror/deliverables/final-specification-set/engine-overworld/wp60-fishing.md)
- [test-catalog/engine-overworld-wp11-15-59-60.md](../mirror/deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md)

逐ID七组实录、必要消费者、前提、反例、失败前缀、验收与接收条件在 [id-evidence.json](id-evidence.json)。[reading-ledger.json](reading-ledger.json) 区分正式/源全文、选定完整历史记录、限定 span/结构与元数据用途；固定原规范两条与合同各字段完全相同，见 [normative-input-binding.json](normative-input-binding.json)。原非作者反证七载荷逐字节身份匹配，完整作者合同 153401 bytes、指定 SHA256/blob 匹配；没有以 hash 代语义阅读。

## 验证与历史回归

最终 [static-checks.json](static-checks.json) 的 **136项作者工具/有限算术检查通过**；[validation-command.json](validation-command.json) 保留真实 argv/cwd/PID/UTC/stdout/stderr/底层 exit0。检查覆盖固定身份、写集保护、UTF-8/LF、17个唯一静态向量、全部其它原行保留、无新增正式源代码、冻结计数及三档概率算术。没有运行原参考定义、完整行为模型、原生宿主、真实输入、Demo 或存档；17条设计向量均 NOT_EXECUTED。历史 R6-O 七钓鱼夹具的原隔离执行结果只按原资格引用，其两次失败与 UTC 缺口不改写。

本批三个路径的33个历史资格 span 已重新核对：32个完整 span 字节同一；WP13 的 GR5-M03-002 旧81–94跨度插入新防护段后，14条原行仍按序同字节，新包含跨度 SHA 另记，不能冒称整段原SHA不变。GR5-M03-007 原 packet `/findings/7`、候选 `/records/41`、唯一 activation 选择及公共事件接收上下文重新核读；R5-FS01–06 等旧向量保持。R2 B21-CASE-DISPATCH 的完整选定案例已从固定 e584 对象恢复，主动 OldRod 与步进表分工保持。R1原WP范围、R2 229/21/341、R3 23/76、R4 17/76与B5 16/75、R5唯一92 CLOSED的原精确资格与排除都保留；没有为其它批次重签游戏语义PASS。详见 [historical-regression-input.json](historical-regression-input.json) 及 [R2-B21-regression-binding.json](R2-B21-regression-binding.json)。

保留两项作者工作纠正：草稿误把106等待命令当false返回，经回源确认106为true后改用116/eventID0；首次静态检查误要求带插入的历史跨度只对应一个连续equal块，失败记录保留于 [static-checks-attempt-01.json](static-checks-attempt-01.json)，最终改为明确核原行投影及新跨度身份。二者不是新增源缺陷或待整改ID。

直接 Git Trees API 被代理403拒绝；改用可用 GitHub只读连接器返回的固定 path/ref blob 与完整 raw字节比对，相关报告/探针/H矩阵的载荷身份全部匹配。原失败、一次不存在的猜测 proposal 文件入口，以及大规范 JSON 的空连接器内容均保留；完整规范改从 fixed raw 恢复并匹配连接器返回 blob，原完整提案也已在合同内全文阅读。见 [report-object-checks.json](report-object-checks.json)、[report-connector-checks.json](report-connector-checks.json)、[report-recovery.json](report-recovery.json)。这些网络/元数据恢复失败已解决，不作为实质修订阻塞。

## 接收与未闭合项

仅写本批三份 mirror 与 evidence，没有修改原 deliverables、R、公共 ledger/task-register、其它作者目录、main或tag，没有实现引擎。当前没有新发现的材料/行为实质阻塞；原 L01工程/地图、L02媒体、L03原生宿主、L14早期工具元数据未知分别保留，不扩大为必修或已运行通过。

接收人为用户指定的唯一整合者 thread `01a13a93-d1da-71e4-a488-63b8524f503d`，覆盖历史准备入口中的接收身份。冻结冲突表给这三文件的候选贡献均为R6-U03；作者仍不能直接写正式。剩余关口是针对已发布候选 commit/tree 的非作者 ultra 复审、唯一写者实际接收、正式共享全文与直接/传递接口复验、历史精确回归、正式接受及 CLOSED登记，分别保持待办。

语义候选 core 与有限发布回执分开；候选 commit/tree 由真实发布后的回执及最终响应绑定，manifest 排除自身而不递归自哈希。复核脚本 [verify_candidate.py](verify_candidate.py) 只读固定Git对象/候选并执行有限算术；新云端复核时须先恢复同一R对象至脚本登记的 `/tmp/r6-u03-reference.git`，不得以别版同名文件替代。
