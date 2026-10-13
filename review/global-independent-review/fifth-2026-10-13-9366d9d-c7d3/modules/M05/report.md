# M05 第五轮全局独立静态审查

schema_version: `gr5.review.v1`  
complete: **true**

分配范围内可得、可审的玩家与物品业务材料已完成静态语义审查。登记 **5 条 P2 拟必修候选、2 条 P3 覆盖待裁决候选**；全部仍为 `candidate_pending_independent_counterevidence`，没有自行签署最终必修或全局通过。

`complete=true` 指本审者的分配阅读与比较完成，不表示所有能力 supported，也不表示父会话已完成独立反证、运行验证或兼容政策裁决。

## 固定输入与证据边界

- 规格 B5：`9366d9d17aaeac3b4414236468affa650fb3dd27`；正式子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。
- 参考 R：`/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`；commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 请求为 `gpt-6-astra / ultra / service_tier=default`，禁 Fast；实际参数无可得回显，记录 **UNVERIFIED**。未调查配置、认证、额度、私有会话或后端。
- 本轮只有源与规格静态阅读、手工条件推导，以及只读解析和审查产物校验。**参考、翻译行为模型、游戏宿主、实际 UI、网络请求均未执行**；历史 PASS 和隔离执行回执不作本轮独立证据。
- 启动和收尾均无本模块 parent-note。未创建子 agent，未提交、推送、启动 update、安装工具或修改配置。未改正式规格、原稿、参考材料、历史证据或共享报告。

## 覆盖与映射

七份主责正式正文 WP24／25／26／27／28／29／64及其原稿均全文阅读；正式条款、表行和全部主责测试向量逐项映射。原稿按实质事实与当前有效后继对照，未发现仅由净化造成的独有正确事实遗失；原稿中的同一错误不构成现行合同的反证。历史行政段按 CURRENT 与固定接受限定解释。

源范围包括指定 Trainer／Player（独立图鉴除外）、装载与资源选择、Storage、Bag、八份 Items 文件；获得／交换／教学／持物／邮件／Mystery Gift／商店及 UI 业务；全部主动物品、被动物品、球处理器与别名／条件组；必要战斗、AI、形态／进化、繁殖、野外、设施／回放、小游戏奖励、调试／编辑／编译和持久化消费者。跨域只签所列业务投影，不替 M06 捕获／成长或 M10 呈现／按键签完整模块。

默认 items 表的 **693** 个身份及业务字段、Gen 5／6／7／8 四份备选表（526／601／637／693 条）及 Shadow 四物品备选均已逐字段或等价差异视图审读。默认与备选不混用。名称、份名、描述的逐字措辞准确性不属 M05 数据结论，其未审行与纯分隔行单列。

产物含 **154 个来源记录、38 个唯一能力、643 条向量映射**。能力为 30 supported、7 partial、1 unresolved；supported 均限定为 **supported_static**。登记索引有 602 个出现记录；被动物品是 32 家族、196 个展开身份配对。登记、别名、数据与消费者不重复增加能力数，数量一致不作语义完备证明。

有效补充已跟读 B07 物品／成长控制、B16 相关业务控制与目录、精确归档 source-limits、WP73-A v4 覆盖附表和 B19 精确归档后继。版本与实际逻辑范围见 [spec-to-source.json](spec-to-source.json)。未因当前路径缺失就断言归档材料不可得，也未递归重审历史管理包。

## 候选结论

完整前提、源锚、当前条款、反证、正反例、静态验收与排除项在 [findings.json](findings.json)。`required` 仅为本审者拟修订意见，独立裁决仍待父会话。

| ID | 级别／拟处置 | 静态结论 | 主要交界 |
| --- | --- | --- | --- |
| GR5-M05-001 | P2 / required | PC 信箱 Give 给空手非蛋成员，持物赋值前读取邮件时因失配自清，继而失败；现行成功转移与 MG-12 不成立。 | WP64、20、66-A／65 |
| GR5-M05-002 | P2 / required | 融合第二成员选择允许 SPECIAL 盒子重入；存放原主体后，移除最后可战成员失败仍提交融合和工具替换，第二成员以同一身份留队。 | WP28、25、21、66-A／B |
| GR5-M05-003 | P2 / required | 盒中或暂持摘要给予邮件，快照用摘要索引查询玩家队伍，不总是持有者之后的成员。 | WP64、66-A／B |
| GR5-M05-004 | P2 / required | 六属性培养身份映射、特性道具精确槽位／ZYGARDE 排除，以及 DIREHIT 三种资格阈值与赋值未完整承接。 | WP28、19／30、44 |
| GR5-M05-005 | P2 / required | 新建道具／训练家类型的手写文本未被记录构造接收；已有训练家保存可重置败北台词，登记与写回没有补偿转换。 | WP73-A、03／04、24／28 |
| GR5-M05-006 | P3 / unresolved | 部分 Item 缺省与普通物 ShowQuantity=false 仍显示数量的合同覆盖不足；是否列为必要作者字段合同待裁决。 | WP03、27／28、66-C |
| GR5-M05-007 | P3 / unresolved | 事件选择／转换未完整给返回值、NONE／空值、重复／首匹配及失败前清变量规则；必要兼容范围待裁决。 | WP27、13、66-C／77 |

已承接而未重复立项的行为包括：选袋初始袋与游标恢复、失败退款残留及同轮终局再退款、伙伴捕获替换的持物错配、Micle 反向门、Leppa 异招 PP 写入、Natural Gift／Fling 当前持物异常、AI 道具估量与资格异常、购物回退总量而非槽分布，以及 Shadow 备选物品缺 Scent 旗标。

## 保留范围与交付检查

地图、公共事件、系统档案及 Graphics／Audio 在固定 R 中缺失；真实配送／交换／商店库存／价格／获赠事件、宿主表现及 Demo 可达性不可证。共享模块余下源码按区间排除，partial 文件不冒称整个模块全文审完。P3 unresolved 是覆盖粒度裁决，不是尚未读取的可得主责源段。

七份主产物为本报告及 [reading-coverage.json](reading-coverage.json)、[source-to-spec.json](source-to-spec.json)、[spec-to-source.json](spec-to-source.json)、[findings.json](findings.json)、[shared-interfaces.json](shared-interfaces.json)、[progress.json](progress.json)。本地能力映射承担 M05 Feature Matrix 投影，未改全局矩阵。progress.md 为父会话可读状态，其余同目录文件仅为审查索引／解析辅助。

JSON、schema_version、候选必需字段、唯一能力身份、源／规格行范围及全部主责向量映射检查无错误，见 [artifact-validation.json](artifact-validation.json)。这些仅为产物检查，不执行参考或行为模型，不替代语义审查。

过程例外：一份导航索引曾误写 `/private/tmp/m05-item-hits.txt`，随即移入本任务目录并净化为仅路径／行号的 consumer-search.txt；该操作无目录外遗留，未改参考或正式规格。progress.json 已如实记录。
