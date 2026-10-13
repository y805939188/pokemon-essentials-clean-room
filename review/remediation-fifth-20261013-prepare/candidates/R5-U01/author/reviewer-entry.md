# R5-U01 非作者复审入口

本目录是作者候选，当前34项均为AUTHOR_STATIC_ADDRESSED。只有父任务安排的非作者审者可以给独立结论；候选不是正式接受，未启动审者。

固定合同入口：`review/remediation-fifth-20261013-prepare/contracts/R5-U01/reviewer-entry.md`，任务冻结22fba7786b0090a1955ce6211315b0036cddfbcd/tree21f3484d167d8cab7a288e0204c72f275414d52e。准备发布93524fe5cf396de2bd01f3c5c1e08ba4b874bc68，B5/R/报告全部按author-response与candidate-manifest固定身份。

1. 将父任务绑定的候选commit/tree作为输入，完整读取author-response、candidate-manifest、finding-responses与static-vectors。
2. 读取formal-diff.patch、operations.json的全部47操作；10份formal是非共享完整镜像，15份fragments依fragment-manifest逐byte定位，只能由R5-I实际接入。
3. 每个finding的全部mandatory_criteria按静态规则、正常/最小反例、失败/取消/部分提交与消费者引用验收；hash/count不能代替语义反证。必要固定原证据与源/B5锚点见source-reading-log；依据冻结contract可复用未变身份，不重复取全仓。
4. 精确历史范围与保留向量见regression-results；原owner/scope保持，不从旧PASS/CLOSED继承新签名；R4/R5历史执行与此次0分开。
5. 可在临时目录运行`python reproduce.py --repo <仓库路径> --out /tmp/r5-u01-independent-projection`重建25份提案字节；脚本只验证和重建规格，未执行参考或引擎。补丁应用同样只准隔离投影，不能据候选过门提前写共享正式文件或公共台账。

U01实际整合依赖为空，当前门为WAIT_NON_AUTHOR_CANDIDATE_REVIEW；随后R5-I实际接入、固定实际commit/tree、非作者实际复审与唯一接受回执仍各自必须。共享文件整份验收须等待其它贡献，关闭还须U08门。原生宿主、真实文件/存档/归档、媒体、统计随机和动态扩展仍NOT_EXECUTED或有界未知。模型回显不可得记UNVERIFIED即可。
