# U04 战斗消费整改作者派发（依赖已满足）

固定交接H `d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65`；U03接受/交接base `3538202ff571268fb712c4b83cd555b83d6424b4` / tree `c5771cb2c864da5581a7f63799c2fcc6d29510d7`；批准WP28来自actual `5004b201183574eabc92764ec4212613314bdecd` / tree `5ed463cba4d9bb5160c33e4e6819a5a05e250ba6`，blob daaa7d1e1ec6b73999cb4c6aae980aebd145aa77、43439bytes。只读参考R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；新环境无路径则已有授权获取精确版本并核身份，不用浮动版本、不访问用户Mac、不配置凭据。父任务以外部最终精确包commit建独立分支/工作树，不在共享checkout混切作者分支。

先读根AGENTS及适用指令，完整读findings.json两canonical对象、frozen-inputs.json、regression-scope.json、junction-scope.json、acceptance-checklist.json。原spec_evidence仍记受审S，当前WP28输入必须继承已接受U03新字节。只处理GR3-M07-001、GR3-M08-001及必要相关回归/消费者，不重做全局或全229/341历史，不改旧原件/状态，不启动U08或重开M02-003。只描述行为/数学/状态/输入输出/失败及静态设计，不翻译Ruby/设计具体TS API/框架/改参考或main。

作者gpt-6.1-sol/xhigh/default，独立review gpt-6.1-sol/ultra/default，请求接纳有效，回显不足UNVERIFIED、不审后台额度、不用隐藏/CLI模型。作者、独立reviewer、唯一整合登记员分离，候选→自检→独立候选PASS→真实actual→独立actual复审→正式接受→依赖满足后CLOSED分层。所有案例/运行NOT_EXECUTED；字节/JSON/补丁/计数不冒行为PASS。历史bug未来兼容政策/缺资源/宿主/真实Demo未知不新增事实补文阻塞。每有实质进展汇报，技术取消先核任务/commit去重，真正用户停止或权限拒绝遵守。

U03四项已正式接受，WP28批准有序交接，U04现在可启动，不等待已运行的U02世界作者。两候选写集无交叉；公共/实际写入仍由唯一整合员顺序负责。

有限必修验收：

- GR3-M07-001：资格失败退款后残留消费身份，默认POTION2→两登记0→首件治满且清身份→次件无效退1/身份还在→同轮正常毒伤终局再退2；继续下一命令对照最终1，使用者正式失能清选择反例及退款容量门；WP28/WP40/WP42与测试一致，原B008资格通过无效果规则不重开。
- GR3-M08-001：默认NaturalGift/有效PARENTALBOND/ORAN，U H160 h81、存活目标JABO：首击基底80/目标伤害提交→反伤20到61→ORAN回复10到71并消费当前物→第二击缺当前物品身份首次失败，早于物品get/默认1；首击与C/I/R/P前缀不回滚。h101对照不自耗且正常第二击，单击对照没有再查询。外层恢复/退出未知，不写必然进程崩溃。AI当前ORAN预测只读WP52-A/B，不传播原早期WP52-C误指，也不把实际每击故障泛化AI。

精确候选路径（每文件从本接受base完整复制，有界修订；覆盖附表只有必要相关行才创建，未改可以省略，禁止空文件/摘录冒完整候选）：

- `deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md`
- `deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md`
- `deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md`
- `deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md`
- `deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md`
- `deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md`
- `deliverables/final-specification-set/pokemon-rules/wp46-damage-healing-coverage.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/pokemon-rules/wp46-damage-healing-coverage.md`
- `deliverables/final-specification-set/combat-requirements/wp47-a-attributes-targeting-calling-data.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/combat-requirements/wp47-a-attributes-targeting-calling-data.md`
- `deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md`
- `deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md`
- `deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md`
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md` → `review/remediation-third-20261012-prepare/U04/candidate/deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md`

作者附属允许路径：

- `review/remediation-third-20261012-prepare/U04/author-report.md`
- `review/remediation-third-20261012-prepare/U04/author-self-check.json`
- `review/remediation-third-20261012-prepare/U04/candidate-identities.json`
- `review/remediation-third-20261012-prepare/U04/candidate.patch`
- `review/remediation-third-20261012-prepare/U04/traceability-proposal.json`
- `review/remediation-third-20261012-prepare/U04/registration-proposal.json`
- `review/remediation-third-20261012-prepare/U04/model-request-receipt.json`
- `review/remediation-third-20261012-prepare/U04/ui-consumer-proposal.json`

WP28独占候选从新daaa身份开始，保留已接受U03探测仪/经验糖果/尺寸/HP/TR/取消/EXP资格，仅同步本次战斗退款交界。WP67-A/UI由U05唯一写，只交ui-consumer-proposal.json。AI资料只读，不改世界文档/WP09/U02目录或公共台账/旧报告/正式文件。

candidate-identities列base/new完整blob/SHA/bytes；candidate.patch只含允许正式映射路径，核base后供唯一整合员使用，作者不apply正式。自检逐ID具名前提/完整步骤/静态終值/失败点/边界/unknown与qualified保留，不能自行独立PASS/接受/CLOSED。正常选择性提交推送独立分支并完整读回，返真实作者commit/tree/path；父任务随后把精确候选给另一独立reviewer。
