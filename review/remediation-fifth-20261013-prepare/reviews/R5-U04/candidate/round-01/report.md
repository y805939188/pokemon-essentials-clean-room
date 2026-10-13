# R5-U04 独立候选复审（round-01）

固定候选结论：**5 PASS／2 FAIL／0 WAIT**。32 个必修 static/preserve 条件为 **30 PASS／2 FAIL**。两处阻塞分别是节拍器数值例缺少最近招式身份前提，以及 Shadow HP 显示消费者描述错误。只签下面的固定候选范围，不签实际整合、正式接受或 CLOSED。

| 必修 | 结论 | 独立核验结果／最小返修 |
| --- | --- | --- |
| GR5-JXN-002 | PASS | 普通动作内层与阶段外层分开；诊断返回不补完成轮号；完整前提下重新尝试整招、PP5→4→3；ERR01–09及旧首次异常前缀保持 |
| GR5-M07-001 | PASS | 最先实际门决定失败布尔；回复期／天空摔投／不服从终止不统一写真；完整存活尾部后跺脚75／150对照成立 |
| GR5-M07-002 | FAIL | 生产规则正确；MET01／继承它的MET02和主例需补“第一尝试前最近使用身份为空或非TACKLE”，才能唯一导出0→1／F1.2 |
| GR5-M07-003 | PASS | 合法3v3生成显示秩缺项；幻觉消息在新成员绑定前失败，持久健康与场上副本失能分开；2v2／失能／多一成员／未查询／取消对照保持 |
| GR5-M08-001 | FAIL | 四原值及四Shadow的数值、状态、持久／失败门支持；须纠正HP条与公共扣血演出的区别，其它正确子事实保留 |
| GR5-M08-002 | PASS | 攻击者自身替身查询首次失败；δ／PP／命中记录已提交而灼伤未写；无替身与更早短路对照成立，不套用自然之恩终止性 |
| GR5-M08-003 | PASS | 合法可解析未知效果：变化失败、伤害普通回退；nil与空字符串分开；条件化SHADOWSHED不清屏障、不冒充默认740绑定 |

## 两处精确返修

**GR5-M07-002，static/1。** [候选WP40第196行](https://github.com/y805939188/pokemon-essentials-clean-room/blob/9a4b090a817197d3f570759171f2c678d914a00d/review/remediation-fifth-20261013-prepare/candidates/R5-U04/author/formal/deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md#L196)和[MET01第259行](https://github.com/y805939188/pokemon-essentials-clean-room/blob/9a4b090a817197d3f570759171f2c678d914a00d/review/remediation-fifth-20261013-prepare/candidates/R5-U04/author/formal/deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md#L259)只限定起始计数0，没有限定最近使用身份。合法计数0＋最近身份TACKLE也满足所列输入：例如先前物品失效时正常TACKLE记录了身份，随后物品恢复有效。该主例第一次更新到1，下一次同招到2，物品贡献为1.4。“首次”是本例第一次尝试，不能替代输入状态字段。固定R [UseMove第231–244行](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb#L231)及物品倍率消费者支持这一静态反例。

最小修订仅在该主例及MET01夹具加入“第一尝试前最近使用身份为空或非TACKLE”；MET02继承相同前提。同步 `static-vectors.json` 的对应输入／夹具副本、`finding-responses.json` 对应证明、`edit-operations.json` 和 `formal-diff.patch`，重建受影响manifest/hash。§5.2.2的身份更新算法及WP50倍率公式保持。

**GR5-M08-001，static/3，显示消费者。** [候选WP46第281行](https://github.com/y805939188/pokemon-essentials-clean-room/blob/9a4b090a817197d3f570759171f2c678d914a00d/review/remediation-fifth-20261013-prepare/candidates/R5-U04/author/formal/deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md#L281)称“压制的是本次HP条动画”；[SH04第134行](https://github.com/y805939188/pokemon-essentials-clean-room/blob/9a4b090a817197d3f570759171f2c678d914a00d/review/remediation-fifth-20261013-prepare/candidates/R5-U04/author/formal/deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md#L134)及向量副本写“HP动画关闭”。固定R [HP入口第5–19行](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb#L5)仍调用显示消费者；[Scene第221–232行](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb#L221)只跳过HealthDown公共扣血演出，仍启动旧HP→新HP的HP条插值并等待。B5 WP67-A §9.2的HP条／公共演出分层保持正确。

最小替换为“只跳过公共扣血演出；HP条仍按共享显示合同更新并等待；显示正常返回后，正扣血默认登记两种本轮受伤标记并条件登记跨半血”。同步SH04、`static-vectors.json /vectors/38/expected_static`及内嵌目录副本、`edit-operations.json /13/replacement`与`/26/replacement`、diff、对应作者证明和清单。static/4要求的伤害登记本身正确，仍PASS；不改量、HP写穿、PainSplit的第三参数区别或其它八效果规则。

以上两例均为复审者手工静态反例（DERIVED_VECTOR／NOT_EXECUTED），没有运行参考、行为模型或宿主。

## 固定身份与上游事实

- 合同：`22fba7786b0090a1955ce6211315b0036cddfbcd`／tree `21f3484d167d8cab7a288e0204c72f275414d52e`。
- 候选：`9a4b090a817197d3f570759171f2c678d914a00d`／tree `6401891a017daedefc125852c1d241d7dbc3973a`。
- 作者证据：`624d3708065c36d73bf209e5bf55615323bfb2fc`／tree `a74cbc5b06eb13b415b77cfd9797dac34569fb00`；相比候选仅新增作者读回回执。
- B5：`9366d9d17aaeac3b4414236468affa650fb3dd27`／tree `594e65edcb192a19110540245fc1663bae2de007`。
- 只读R：`Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- U03：`debf2ee76ff7fdf7823b5c03a7f167b543639644`的限定登记已满足U04所需上游门。作者旧WAIT属于历史陈述，不是当前上游事实。该上游至B5的差异未改动U04的16个正式目标路径；WP03新增Move默认／分类约束与本候选回退前提相容。

## 证据边界与发布

七项冻结验收、反例、共享合同和必要精确旧回归由非作者审查任务实际阅读。B09/B001与B002、B10主责／B12共享B017、B05/A030及GR3-M08-001／U05呈现前缀／GR4-J08分别保留准确owner/scope；没有按主题相似转签旧PASS。逐条证据和读取范围见[criterion-results.json](criterion-results.json)、[source-reading-log.json](source-reading-log.json)与[regression-results.json](regression-results.json)。

机械核验见[independent-validation.json](independent-validation.json)：固定候选28个、证据29个载荷身份，15正文镜像＋1共享片段，32验收映射、55个候选静态向量与33旧向量字节保留已核。机械通过只证明结构／身份；两处语义FAIL仍阻止本批整体候选PASS。作者工具末尾用B5全树差异归因作者写集而失败；独立按固定出版基线归因并重建投影通过，此工具归因问题单独不作为七项新增语义缺陷。

本update新增参考执行0、行为模型0、宿主／Demo0；R4历史隔离执行4与R5 review历史隔离执行4分别保留、均未重跑。全轮92必修范围不扩展，optional7、no-required7、政策6及M11-005可选方面继续隔离。真实媒体、诊断自身成功、默认Demo可达、无界插件／所有组合和未来兼容政策仍受原限制。请求模型／参数回显为UNVERIFIED，不审计额度。

工作区`.agents`为空，仓库及冻结树无相关`.agents/skills`，已读完整`AGENTS.md`及R5-U04合同。所有仓库新增／修改仅在本独立目录；未改作者候选、正式规格或公共登记，未合并main、触碰Mac或删除分支。[review-manifest.json](review-manifest.json)绑定身份及逐scope字节。返修后只需定向重审两处受影响范围和同步载荷；其它本次限定PASS不自动转签到新字节。
