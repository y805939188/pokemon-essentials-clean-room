# R5-U02 作者候选交接

14项必修均提交候选修订；46条mandatory static逐条映射于finding-responses.json，73个DERIVED_VECTOR未执行。8份独占正文镜像、8个共享目标的16个候选片段，只写本author目录。formal-diff.patch是B5上的审查投影，不是实际正式整合。

B5 9366d9d17aaeac3b4414236468affa650fb3dd27；任务冻结 22fba7786b0090a1955ce6211315b0036cddfbcd（tree21f3484d167d8cab7a288e0204c72f275414d52e）；准备发布93524fe5cf396de2bd01f3c5c1e08ba4b874bc68；报告 f49d870c6fd616ab6736754a218a4553b5acac7f；R Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b只读。候选/证据commit及tree由提交后外部回执绑定，manifest不自引用。

| 问题 | 作者结果 | 向量 |
| --- | --- | --- |
| GR5-JXN-001 | 已覆盖，待非作者复审 | JXN-NAME01, JXN-NAME02, JXN-NAME03, JXN-NAME04, JXN-NAME05, JXN-NAME06, JXN-NAME07 |
| GR5-M03-001 | 已覆盖，待非作者复审 | R5-EV01, R5-EV02, R5-EV03, R5-EV04 |
| GR5-M03-002 | 已覆盖，待非作者复审 | R5-ID01, R5-ID02, R5-ID03, R5-ID04 |
| GR5-M03-003 | 已覆盖，待非作者复审 | R5-TIME01, R5-TIME02, R5-TIME03, R5-TIME04 |
| GR5-M03-004 | 已覆盖，待非作者复审 | R5-RT01, R5-RT02, R5-RT03, R5-RT04, R5-RT05 |
| GR5-M03-005 | 已覆盖，待非作者复审 | R5-DI01, R5-DI02, R5-DI03 |
| GR5-M03-006 | 已覆盖，待非作者复审 | R5-JP01, R5-JP02, R5-JP03 |
| GR5-M03-007 | 已覆盖，待非作者复审 | R5-FS01, R5-FS02, R5-FS03, R5-FS04 |
| GR5-M03-008 | 已覆盖，待非作者复审 | R5-PUSH01, R5-PUSH02, R5-PUSH03, R5-PUSH04 |
| GR5-M03-009 | 已覆盖，待非作者复审 | R5-LOC01, R5-LOC02, R5-LOC03 |
| GR5-M03-010 | 已覆盖，待非作者复审 | R5-SW01, R5-SW02, R5-SW03 |
| GR5-M03-011 | 已覆盖，待非作者复审 | R5-BP01, R5-BP02, R5-BP03, R5-BP04 |
| GR5-M03-012 | 已覆盖，待非作者复审 | R5-ER01, R5-ER02, R5-ER03 |
| GR5-M03-013 | 已覆盖，待非作者复审 | R5-DG01, R5-DG02, R5-DG03, R5-DG04, R5-DG05, R5-DG06, R5-DG-34-01, R5-DG-34-02, R5-DG-34-03, R5-DG-34-04, R5-DG-34-05, R5-DG-34-06, R5-DG-34-07, R5-DG-34-08, R5-DG-136-01, R5-DG-136-02, R5-DG-136-03, R5-DG-136-04, R5-DG-136-05, R5-DG-136-06, R5-DG-136-07, R5-DG-136-08 |

逐项正常/失败/取消/部分提交/消费同步映射见finding-responses.json；source-reading-log.json绑定完整字节和必要锚点，regression-results.json固定精确owner/scope关系，不转签历史PASS。consumer-consistency.json记录反向消费者限定。validate-candidate.py只运行文档/补丁/身份检查，不执行参考或行为模型。

复现：在可读B5与冻结合同Git对象的仓库运行`python <author>/rebuild-candidate.py`，随后`python <author>/validate-candidate.py`；默认正式投影在/tmp/r5-u02-projection，工作树正式文件不写。共享片段以fragment-manifest.json中的B5完整身份、精确before与marker载荷交R5-I；其他已接受贡献若改变锚点，必须协调并复审实际字节，禁止整文件覆盖。

依赖R5-U01为WAIT，仅约束实际整合/接受；没有作者自签候选PASS、接受或CLOSED。非作者入口：冻结`contracts/R5-U02/reviewer-entry.md`；实际字节复审入口`contracts/R5-U02/actual-reviewer-entry.md`。父任务安排审者，本任务未启动。

R4历史隔离4与R5review隔离4分别保留。本update新增参考/模型/原生宿主/Demo行为执行全部0。缺地图/CommonEvents/媒体与原生宿主、任意插件/异常文本/无界配置组合仍保留限制，局部地牢正常不保证整图、终止或摆放成功；未来兼容政策未裁决。optional7/no-required7/政策6及M11-005 optional方面未纳入。实际模型回显UNVERIFIED，未检查额度/认证。

独立分支：codex/r5-u02-author-20261013。未merge main、未改公共registration、未改参考/冻结合同、未删分支、未动Mac。
