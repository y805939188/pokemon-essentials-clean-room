# U06 actual-01：审定v2当前机械接入

去重键 `R5-U06/actual/round-01@5ab3af08f9159a37d416241f82f59e4c0390670b+4512ab7327294619547e5f9b3025538504cb6d62`；没有既存同包actual，本次只机械应用一次。固定作者 `5ab3af08f9159a37d416241f82f59e4c0390670b` / tree `ed0316dd2909253442a7eab8567d15b62f8f4460`、证据 `b3b5d74c19aa4cb7c4b4623731c8454a2b5b56b0` / tree `1fe69168ce67e13e99ce6cf84c2f1699b0a50c73`、原独审 `4512ab7327294619547e5f9b3025538504cb6d62` / tree `160472f6a58ec342f0679b21f8153db85bc785b5` 的18项/145条件候选PASS已核：3有限复验＋142准确未变复用，16旧通过范围不重审。

U02/U03/U04/U05当前唯一接受回执均已满足门，原候选/审者WAIT是当时历史陈述，不回写。按43原编辑接入24正式路径：14直接镜像完全等同受审候选，10共享路径只接本批15片段，同时保留之前67个限定接受owner贡献。候选B5零上下文补丁只在隔离目录重放；实际补丁从当前891已接受字节生成，保留原所有新文字和范围，不覆盖共享B5整份。

[逐文件/操作/145条件映射](candidate-to-actual.json)、[当前精确补丁](current-to-actual.patch)、[上游/共享影响](upstream-impact-and-gates.json)、[机械核验](mechanical-validation.json)、[正式131身份](formal-tree.json)。24条当前锚唯一，无内容冲突。33个受影响既有贡献均保留原字节，6个因新增表/节被分段的compound可逆重组；原54接受路径全文blob不变。E026最终跨度包含后续已审E027的同批组合，不把原未组合跨度当最终完整字节。

实际独审必须核新邻接/消费者对原scope的影响，字节保持不自动授旧整文件或新actual语义PASS。U06实际PASS/正式接受0，累计接受仍67owner/390条件/205作者操作；共享整份/U07/U08/CLOSED继续原门。实际commit/tree由后继locator绑定，交[原独审入口](reviewer-entry.md)。

原环境及作者/审者未发布域不触碰，不归档/释放/危险恢复，不重做或丢弃先前贡献；源/旧round01三FAIL、U03旧FAIL、两MISMATCH、SC-U07-001及005内部optional/政策/原13限制均保留。106向量DERIVED_VECTOR/NOT_EXECUTED，R4历史4与R5review历史4分列不重跑；本update新增参考/模型/宿主行为执行0，main不合并，Mac不动。
