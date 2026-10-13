# R5-U06 作者候选交接

18项必修的候选已撰写，作者静态核对为 AUTHOR_STATIC_ADDRESSED；这不是独立候选PASS、正式接受或CLOSED。复审由父任务安排不同真实任务，本文不启动审者、不登记公共台账。

固定B5 `9366d9d17aaeac3b4414236468affa650fb3dd27` / tree `594e65edcb192a19110540245fc1663bae2de007`；只读R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。合同冻结 `22fba7786b0090a1955ce6211315b0036cddfbcd` / tree `21f3484d167d8cab7a288e0204c72f275414d52e`；分支从准备发布 `93524fe5cf396de2bd01f3c5c1e08ba4b874bc68` 建立。报告发布 `f49d870c6fd616ab6736754a218a4553b5acac7f` / tree `e5dc6aaf626885666e7d472865563f0c9bfbdf46`；语义报告 `c0ff33024aea424c68d29f9778fe7c8e807d21e8` 保持。

候选分支 `codex/r5-u06-author-20261013`。父任务入口未指定具体批次分支名，本作者在授权的独立候选范围内选择此名称；未移动准备分支/main。请求模型/推理/服务为gpt-6.1-sol/xhigh/default，禁Fast；实际回显全部UNVERIFIED，不审计额度或认证。

候选包含14份非共享完整镜像和10个共享目标的定位提案，共24个正式目标、43个编辑、106个DERIVED_VECTOR / NOT_EXECUTED向量。`formal-diff.patch`包括共享提案，必须只在临时目录复现审查；共享及公共登记只由R5-I在门满足后写入。`fragment-manifest.json`给每片目标、B5 blob/完整锚点、ID、位置、保留行为及WAIT依赖。`edits.json`和`tools/replay-candidate.py`可从B5复现全部字节；补丁采用零上下文（完整B5锚点在edits.json），临时目录应用须用`git apply --unidiff-zero`。`candidate-manifest.json`给所有产物字节/SHA256/blob，commit/tree由父任务或后继证据回执绑定，避免自哈希递归。

逐项全部mandatory criterion及接收位置/源锚/向量在`finding-responses.json`；消费者producer→write→consumer→display→persistence和失败/取消/部分提交在`consumer-consistency.json`；原scope精确回归与未变旧向量字节在`regression-results.json`。阅读日志区分完整载荷验证和本scope静态语义，不将旧PASS转签。M11-002单键焦点与M11-003同轮仲裁分列；M10-012完整单元坐标与M10-013抑制后空单元失败分列；005只接收六个required时序子项，未纳入可选图集/兼容政策。

本update新增参考/模型/宿主/Demo执行均0。Git/hash/格式/补丁复现和数学算数检查归TOOL_VALIDATION，不是行为模型执行。历史R4隔离4与R5review隔离4分别保持；R5-REF-004仅复用身份/原五观察作静态比对，保留先设施失败后补惰性Rect替身的两次进程，不复跑，不借给005或其它媒体/输入证据。原记录自动match仅主要检查index/给定spinning，其它字段本作者静态逐项核对；未推完整支付执行。

R5-U02、U03、U04、U05所需贡献均WAIT；候选不等待上游，但实际整合/接受/关闭须等待合同门。共享文件其它贡献须齐备后整份复审，最终CLOSED还需U08有限整合、同独立审者实际关闭字节验收与唯一接受回执。

限制：缺完整原生宿主、Graphics/Audio和地图/Demo；显示属性量化、真实采样/输入缓存、动态插件、异常外层恢复、真实媒体效果仍未证。名义时长不是精确原生墙钟/真实帧数；逻辑音效/坐标/资源请求不是可听或可见结果。冻结报告13限制和optional/no-required/政策各分母不变。

独立审者入口：冻结合同`contracts/R5-U06/reviewer-entry.md`；先由父任务绑定候选commit/tree、证据commit/tree和完整manifest，再按该入口逐项验收。作者没有独立签署、正式接受或关闭权限。

| ID | 作者候选状态 | 候选入口 | 独立/实际状态 |
| --- | --- | --- | --- |
| GR5-M10-001 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-001 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-002 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-002 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-003 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-003 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-004 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-004 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-005 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-005 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-006 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-006 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-007 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-007 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-008 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-008 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-009 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-009 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-010 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-010 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-011 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-011 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-012 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-012 | WAIT复审 / WAIT依赖整合 |
| GR5-M10-013 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M10-013 | WAIT复审 / WAIT依赖整合 |
| GR5-M11-001 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M11-001 | WAIT复审 / WAIT依赖整合 |
| GR5-M11-002 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M11-002 | WAIT复审 / WAIT依赖整合 |
| GR5-M11-003 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M11-003 | WAIT复审 / WAIT依赖整合 |
| GR5-M11-004 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M11-004 | WAIT复审 / WAIT依赖整合 |
| GR5-M11-005 | AUTHOR_STATIC_ADDRESSED | finding-responses.json#GR5-M11-005 | WAIT复审 / WAIT依赖整合 |
