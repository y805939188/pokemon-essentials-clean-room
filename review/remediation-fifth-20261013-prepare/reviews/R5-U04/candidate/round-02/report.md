# R5-U04 v2 定向独立复验（candidate/round-02）

**两项旧失败标准均 PASS，无剩余 FAIL／WAIT 或返修。** 其余五项只在精确未变的 owner/scope 字节上复用 round-01 签名；固定 v2 的七项必修均为限定候选 PASS，32 条条件均满足。此次只重验两项失败标准及必要传播影响，没有展开全局复审，也没有签实际字节、正式接受或 CLOSED。

| 必修 | v2 结论 | 本轮依据 |
| --- | --- | --- |
| GR5-JXN-002 | PASS | 复用未变主条款、引用、ERR及旧前缀范围 |
| GR5-M07-001 | PASS | 复用未变失败布尔生产／尾部消费范围 |
| GR5-M07-002 | PASS | static/1定向复验；static/0、2精确未变复用 |
| GR5-M07-003 | PASS | 复用未变WP39片段、WP41正文及RANK范围 |
| GR5-M08-001 | PASS | static/3定向复验；static/4登记证明传播复核，其余未变子范围复用 |
| GR5-M08-002 | PASS | 复用未变鸟嘴加热首次错误及BB范围 |
| GR5-M08-003 | PASS | 复用未变分类回退及FB范围 |

## 两项失败标准的精确结论

**GR5-M07-002/static/1：PASS。** [WP40第196行](https://github.com/y805939188/pokemon-essentials-clean-room/blob/f7dba61471c674c6e45efb0595be06bf3cdc773b/review/remediation-fifth-20261013-prepare/candidates/R5-U04/author/formal/deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md#L196)与MET01已明确第一尝试前最近使用身份为空或非TACKLE；MET02显式继承。首次更新为0，失败保留TACKLE身份，后次同招更新为1／F贡献1.2。旧“计数0＋最近TACKLE”反例仍是合法参考状态，但已被新夹具排除，不再推翻此主例。更新算法、前置／无PP早退、无效物品／调用外壳、初始化与倍率读取未改。正文、目录、JSON记录／内嵌夹具、操作2／25、完整与增量patch和清单同步成立。

**GR5-M08-001/static/3：PASS。** [WP46第281行](https://github.com/y805939188/pokemon-essentials-clean-room/blob/f7dba61471c674c6e45efb0595be06bf3cdc773b/review/remediation-fifth-20261013-prepare/candidates/R5-U04/author/formal/deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md#L281)与SH04已明确只跳过HealthDown公共扣血演出，HP条仍更新并等待；显示正常返回后才默认登记两种本轮受伤标记，并条件登记跨半血。固定R的HP入口／Scene／HP条消费者与round-01缓存身份一致。正常显示、显示失败发生在登记前、反馈失败发生在登记后分别核验；没有补造未到写点的标记。SH09、正确扣量／HP写穿、PainSplit第三参数区别及其它Shadow合同保持。正文、SH04、JSON及夹具镜像、操作13／26、patch、证明与清单同步成立。static/4支持证明的文字同步已定向复核，不增加第三个必修义务。

## 未变范围与证据复用

独立比较v1→v2，规范镜像差异仅四文件／五行，操作仅2、13、25、26，候选向量仅MET01、MET02、SH04改变。**其余52个候选向量与33个旧向量保留**；三份旧目录前缀、其它操作和五项通过范围的正文片段／共享主条款／消费者仍精确一致。共享WP40或目录文件整体身份发生变化时，只复用已验证未变的scope字节，不把旧整文件签名转签到新容器。

32条件的来源区分为：两项失败标准定向复验、一个正确登记标准的必要证明传播复核、其余29个原PASS条件限定复用。逐条结论见[criterion-results.json](criterion-results.json)，原记录及新读取范围见[source-reading-log.json](source-reading-log.json)，字节保留与精确签名复用见[regression-results.json](regression-results.json)。没有重新下载整仓历史或未变参考源。

固定合同 `22fba7786b0090a1955ce6211315b0036cddfbcd`、B5 `9366d9d17aaeac3b4414236468affa650fb3dd27`及只读R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`保持；原独立报告为 `88bb040c83186c5c5d153b7fd1162e2c037e7d3f`／tree `9feb5578605e329b902d3fe1a7a175ff95235a28`，原签名继续绑定其原字节，本报告记录限定复用依据。U03所需上游贡献在 `debf2ee76ff7fdf7823b5c03a7f167b543639644`已满足，无上游WAIT。

v2候选：`f7dba61471c674c6e45efb0595be06bf3cdc773b`／tree `02499fe1cea46dc9e04a1b127d32702fddf42c7c`。证据：`e22def9449b65ef83e11dc267dc0c7937245eace`／tree `dce5aa8c1634cbbd51fdb1613eccd43482b3e953`；后者仅追加v2读回回执，作者声明不代替本次独立校验。

本次新增参考／行为模型／宿主Demo执行均为0；设计为DERIVED_VECTOR／NOT_EXECUTED，格式、hash、投影及差异复建为TOOL_VALIDATION。R4历史隔离4与R5 review历史隔离4分别记录、均未重跑。55候选设计总数保持，不以本轮复审计新批次；92必修及optional7／no-required7／政策6／M11-005可选方面隔离保持。模型与参数回显UNVERIFIED，不审计额度。真实媒体、诊断自身成功、Demo可达、无界插件／全部组合及未来兼容政策仍受原限制。

仅写本round-02独立域；未改作者候选、正式规格、公共登记或round-01报告，未合并main、触碰Mac、删分支或释放原环境。工作区`.agents`仍为空，仓库无相关技能文件；复用已读且blob一致的AGENTS和冻结合同。本轮round-02写入由最新用户指令明确授权。[review-manifest.json](review-manifest.json)绑定逐scope与载荷身份；[independent-validation.json](independent-validation.json)记录完整读回依据。
