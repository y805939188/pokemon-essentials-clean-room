# R5-U03 作者候选回执

11项必修已提交候选；本回执是作者静态核对，不是独立复审或正式接受。候选共8个独占formal镜像、8个共享目标文件的31片段、66条DERIVED_VECTOR（全部NOT_EXECUTED）。正文只表达行为，证据和范围说明在本目录。

固定B5 `9366d9d17aaeac3b4414236468affa650fb3dd27` / tree `594e65edcb192a19110540245fc1663bae2de007`，正式131子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`；固定R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。任务冻结 `22fba7786b0090a1955ce6211315b0036cddfbcd` / tree `21f3484d167d8cab7a288e0204c72f275414d52e`；准备发布 `93524fe5cf396de2bd01f3c5c1e08ba4b874bc68`；报告发布 `f49d870c6fd616ab6736754a218a4553b5acac7f`，语义报告身份复用contract。

| 必修 | 作者结果 | 新向量 | 核心候选 |
| --- | --- | ---: | --- |
| GR5-JXN-003 | CANDIDATE_READY；待非作者复审 | 5 | 创建初值/普通写入分开，免费成功仍写钱包；SH03加适用前提 |
| GR5-M01-005 | CANDIDATE_READY；待非作者复审 | 4 | 负盒容量与寻址/首空分开，保留正常UI和地区scope |
| GR5-M01-006 | CANDIDATE_READY；待非作者复审 | 7 | NPC省略覆盖表、零基Nature序、双异色/Shadow顺序 |
| GR5-M04-001 | CANDIDATE_READY；待非作者复审 | 6 | 完整自然候选枚举及索引2碰撞，药膏/调试消费者一致 |
| GR5-M04-002 | CANDIDATE_READY；待非作者复审 | 7 | 摘要读取副作用与瓶子刷新重入的最终0/新时间 |
| GR5-M05-001 | CANDIDATE_READY；待非作者复审 | 3 | PC Give提示后自清读取失败、原信箱对象保持，MG12纠正 |
| GR5-M05-002 | CANDIDATE_READY；待非作者复审 | 5 | 盒中主体融合、最后伙伴删除false仍提交工具替换 |
| GR5-M05-003 | CANDIDATE_READY；待非作者复审 | 7 | 调用者k×玩家party快照表，盒格/暂持/普通队伍对照 |
| GR5-M05-004 | CANDIDATE_READY；待非作者复审 | 6 | 六项×三族、条件WING、ZYGARDE和三DIREHIT参数 |
| GR5-M05-006 | CANDIDATE_READY；待非作者复审 | 6 | Item字段默认、数量三态、图标门和当前槽数 |
| GR5-M05-007 | CANDIDATE_READY；待非作者复审 | 10 | 选择写NONE、转换清前/清后失败及函数/变量返回分层 |

逐项完整mandatory及preserve映射：[finding-responses.json](finding-responses.json)。精确历史owner/scope与原正确规则保护：[regression-results.json](regression-results.json)。参考路径/字节身份与实际读取范围：[source-reading-log.json](source-reading-log.json)。共享片段位置/原文/新文/依赖：[fragment-manifest.json](fragment-manifest.json)。可重放差异：[formal-diff.patch](formal-diff.patch)，机器操作：[operations.json](operations.json)。

验证命令：`python review/remediation-fifth-20261013-prepare/candidates/R5-U03/author/verify-candidate.py`。仅做UTF-8/JSON、范围、完整blob/hash、相对链接、向量ID/状态与B5补丁重放；结果属TOOL_VALIDATION，静态语义判断属作者核对。

实际整合依赖R5-U01仍WAIT；须由非作者审固定候选，再由R5-I按依赖门整合，独占镜像机械接入、共享只由R5-I实写；同独立审者再审实际字节，U08/唯一登记回执另行安排。候选不登记接受/CLOSED，不启动本批审者。原稿未授权同步的边界见scope-conflicts。

独立审者入口：准备发布的 `review/remediation-fifth-20261013-prepare/contracts/R5-U03/reviewer-entry.md`，父任务绑定固定candidate/evidence commit/tree及完整清单后分发；本目录不冒用独立签名。

本update新增参考/模型/宿主/Demo行为执行0；R4历史隔离4与R5review隔离4分别保留、未重跑。宿主、媒体、完整Demo、无界插件/配置组合、真实存档和后续融合后果保持限制；optional/兼容政策未自动纳入。请求模型参数gpt-6.1-sol/xhigh/default/禁Fast，实际回显UNVERIFIED；真实作者task ID未由平台暴露，交父任务绑定，不以源thread ID或环境ID冒充。

候选/证据commit/tree外部绑定于最终回执，manifest不嵌自身哈希。
