# R5-U03 非作者独立候选复审 — round-01

结论：**本批候选 FAIL；11 必修逐项为 10 PASS / 1 FAIL。** GR5-M01-006 的新增覆盖表及四条新增静态验收成立，但此次替换删除了原正确 NPC 形态/招式选择合同，未满足批级保留门。其余签名仅覆盖下表限定贡献，不是整份共享文件接受。

**R5-U01 实际接受依赖仍 WAIT；actual 字节未审、正式接受与 CLOSED 均未授予。** 本报告不改变公共登记或冻结历史，不启动后继整合。

固定候选 `047c458a461c924dfe481be018f4009f3cedc04e` / tree `5bcedb775baa1b4070253a4fc108bfcef791ff62`；作者证据 `d93776e127c1dec08fcb4297c7280e60020ced68` / tree `976d6f939e81f44aeda97164c443cf683789058d`。任务冻结 `22fba7786b0090a1955ce6211315b0036cddfbcd` / tree `21f3484d167d8cab7a288e0204c72f275414d52e`；B5 `9366d9d17aaeac3b4414236468affa650fb3dd27`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。B5 正式131子树仍为 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`，候选是镜像/片段投影，未写入正式路径。

| 必修 | 候选裁决 | 独立核查要点 |
| --- | --- | --- |
| GR5-JXN-003 | PASS | 创建初值与后续写入分离；免费成功仍按物品/统计/钱包顺序写回，拒绝/取消保持初值 |
| GR5-M01-005 | PASS | 全负号容量与仅−1队伍寻址分开；首空位保留真实盒读法及正常UI/地区scope |
| GR5-M01-006 | **FAIL** | 新槽/性别/双异色/Nature覆盖正确；删去原NPC简单形态及显式/默认招式选择分支 |
| GR5-M04-001 | PASS | 自然候选完整枚举、索引2碰撞与实际解析分层；药膏/调试一致，正常resolver保留 |
| GR5-M04-002 | PASS | 摘要读可先提交形态；瓶子首用0/空时间链最终0/新时间，刷新和新鲜时间对照完整 |
| GR5-M05-001 | PASS | PC Give提示先于失败；失配邮件读取自清，持物未赋、原信箱对象保留；MG12及UI同步 |
| GR5-M05-002 | PASS | 当前会话许可与永久三门分开；同主体入盒后最后伙伴删除false仍提交融合/工具替换；取消保留嵌套移动 |
| GR5-M05-003 | PASS | caller零基k与玩家party快照分开，第三项为实际目标；盒格/暂持/普通队伍与显示读取一致 |
| GR5-M05-004 | PASS | 六能力×三族及条件WING、ZYGARDE门、三DIREHIT资格/赋值均核；保留既有算法/退款边界 |
| GR5-M05-006 | PASS | 合法字段默认与文本/记录输入域分开；数量三态、重要物图标门、PC逐槽消费者一致 |
| GR5-M05-007 | PASS | 选择ID/nil与NONE写入、转换清前/清后失败、首匹配/奇尾/函数配对数返回及公开0分层 |

逐条60条显式static、原具名preserve、附加原正确合同保留检查，以及正常/失败/取消/部分提交、producer→write→consumer→display→persistence，见 [criterion-results.json](criterion-results.json)。新增静态条件通过不能抵消删除既有合同；未把66条静态向量报成实测。

## 唯一候选必需返修

GR5-M01-006：候选共享 [WP18片段](../../../../candidates/R5-U03/author/fragments/deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md.md) 第1/5行取代了 B5 WP18 第198行。新文仅说“处理可选形态、持物和招式”；WP24只委托新表。WP18通用三形态入口和WP20通用招式规则不能确定NPC选哪一入口、招式缺省/空列表走哪一分支。

固定R `Data/Scripts/010_Data/002_PBS data/015_Trainer.rb` 129–140，以及个体形态/招式消费者确认：NPC可选形态采用简单存储形态写入；显式招式列表存在且非空时按给定顺序逐个静默学习，否则重建等级可达默认招式。原规则决定中途形态处理器/图鉴/缓存副作用以及无显式招式时是否仍有默认招式；不能用“处理”代替。

最小操作：

1. 在WP18片段第5行恢复该绑定：可选形态走简单存储写入（不调用形态处理器、不登记、不清特性缓存，仍重算），随后持物与招式；显式非空招式按序逐个静默学习，否则重建等级可达默认招式，通用细节引用WP20。保留新覆盖表、缓存/钩子与失败前缀边界，不要求原API或复制源码。
2. 同步此片段、fragment-manifest、operations、formal-diff.patch及完整字节清单；用非空、省略/空列表与简单形态的静态保护对照核该删除已恢复。无须新增宿主运行。
3. 仅针对006受影响片段/消费者及新固定commit/tree复审；未变的其它10项与历史证据按固定身份复用。上游接受门满足后仍须另审实际整合字节。

## 原证据、共享与历史限定

8独占镜像、8共享目标文件的31片段、16投影目标、52操作及66向量已独立重放比对；44完整投影相对链接、6作者回执链接及38原片段身份已核。13共享主合同原记录、21当前记录hash及精确历史owner/scope直接反查，不只重跑作者验证器。复现脚本与命令嵌于 [independent-validation.json](independent-validation.json)。

工具共1014项：1012 PASS、2 MISMATCH，其它工具失败0。两处MISMATCH是冻结canonical历史中对 `counterevidence/root-M01/canonical-findings.json` 与 `modules/M01/findings.json` 的过时整文件SHA导航：固定版本实际完整字节/blob已核，21指定当前记录hash全吻合。只允许逐记录限定复用，**不签旧整文件hash通过**；差异、实际身份与最小后继说明需要见 [regression-results.json](regression-results.json)。不改冻结原文件或旧状态，不将该元数据问题算成新的全局必修。

31唯一明确历史记录＋3必要关联记录、86唯一原绑定记录（122核验事件）均按具名指针核验。A020主责为B07，B01/B05是局部贡献；A026主责B07，B05局部；A035主责B06。R4-M04-001为R4-U03，原Summary条件保留；本轮Summary残留与新增瓶子消费者分别限定，不改R4当时CLOSED，不归因整改引入。旧PASS不转签，未重开全局review。

## 独立性、执行与发布边界

真实可见审者任务路径为 `/root`，并行子审路径登记于 [review-manifest.json](review-manifest.json)；平台任务UUID未暴露记UNVERIFIED，不以源thread/环境ID冒充。该独立团队没有撰写047c458/d93776作者字节。AGENTS与冻结入口已读；本环境 `.agents` 为空，无额外本地skills可读，未访问Mac。

请求gpt-6.1-sol/ultra/default普速、禁Fast；实际模型/推理/服务参数未回显均 **UNVERIFIED**，未审计额度、认证或后端。R4历史隔离参考执行4、R5review隔离参考执行4分别复用且未重跑；**本update新增参考/模型/宿主/Demo行为执行均0**。66新向量为DERIVED_VECTOR/NOT_EXECUTED，JSON、hash、链接、重放均TOOL_VALIDATION。宿主、媒体、真实存档、完整Demo和无界组合不授运行PASS；optional7、no-required7、政策6及M11-005可选方面未扩为必修。

本报告只新增独立review域。普通推送至 `codex/r5-u03-independent-review-20261013`；精确新增载荷远端读回以后继 [remote-readback.json](remote-readback.json) 固定报告commit/tree和完整bytes/SHA256/blob。该回执仅证明发布字节，不改变候选/实际裁决。没有merge/push main、改作者/正式/公共登记或冻结历史。
