# WP51 / WP52 AI 全文独立复审

FAIL：固定基线AI域粗标尚不能限定通过；来源/标题/状态/保守整改绑定可通过，分类依据待查且有元数据与依赖缺陷。最终R8整改回填/验收仍待协调固定后继。

固定候选 `d62b41f4d620e50bb04c80a7505374bd284d8210`；正式子树 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。真实逻辑任务 `/root/combat_semantics/combat_ai`。上级请求 `gpt-6.1-sol / ultra / default / Fast off`，实际 model/effort/tier/speed/Fast/opaque平台ID 均 `UNVERIFIED`，未将请求参数当执行遥测。

全文阅读 8 篇正文，共 1523 行、101 个实际标题；另完整读 AI 共享测试目录 349 行、8 标题。核对全部 41 行 feature。独立标题/锚点/范围/单位hash核对0缺失，9篇在源/交付/候选同字节。逐文件 SHA 与读取分块见 `combat-ai-evidence.json`。没有执行Ruby、参考游戏、框架、Showdown或业务向量。

## 问题

### CAI-01 / P3 / AI全41行协作标签共用整篇理由，未给实际AI承载边界

待验证状态允许兼容性未知，但不能替代章节分类依据。纯偏好数据、评分近似和实际资源登记目前都由一句持久状态/会话边界理由覆盖，没有说明谁计算策略、谁提供规则查询、谁写共享准备字段及谁承接真实登记。

候选位置：routing-policy.json:L36–46；routing-manifest.json所列41行/future_plan；views/combat-requirements.md相应41行

- WP52-C主稿L11、102：评分不提交持物C/I/R/P/Belch，真实操作属WP47-B/50。
- WP52-A主稿L11、17：只给WP51评分输入，真实执行不同；准备共享字段并无统一回滚证明。
- WP51主稿L108–128：真实业主列表、完整资格扫描、AI上下文异常、玩家接管背包消费均为实质交界。
- 41行rationale/questions完全相同，prototype_refs全空。

必要修正：按可共同验收的行为组补AI策略/查询/登记归属假设与具体问题；必要时拆开真正跨责任的子节，允许保留协作或待决策，不预设Showdown现有兼容。对FR-000075补业主资源/AI上下文与背包物品验证门的对应关系；无需现在运行原型。

### CAI-02 / P3 / 责任与保留章节被制造成独立待实现功能

这些段落没有新的独立能力/验收边界，却有独立destination/stage/implementation，违反管理/范围章节作为元数据关联功能的口径。共有开关/默认事实已由已有AI行为行承接。

候选位置：routing-manifest.json:L15579（FR-000081）、L17090（FR-000097）、L18080（FR-000108）；section-coverage.json对应mapping_kind=behavior-unit

- wp51-ai-decision-defaults.md:L90–92：责任划分和特殊模式/全局未决。
- wp52-b-effect-coverage.md:L109–111：A/51/B/C职责和既有开关/默认交叉引用。
- wp52-c-item-control-coverage-and-data.md:L189–191：A/51/B/C职责、全局未关闭范围。

必要修正：保留稳定ID历史导航，不删除来源事实；改为元数据/退役导航并关联相应已有功能，补迁移关系，重建计数/生成视图，避免重新seed改号。

### CAI-03 / P3 / 从旧WP计划复制的依赖遗漏现行正文的明确评分消费者

doc_bindings仅并集wp-index行dependencies并逐行复制，无法表示已交付正文当前实际消费关系。特别是B/C评分依赖A但清单没有A，粗伤/命中依赖WP50却遗漏。未来协作实施者按此表可遗漏规则输入和验收前提。

候选位置：routing.py:L129–142、L252；routing-manifest.json各features/dependencies；views/combat-requirements.md的WP依赖列

- FR-000076：缺 WP52-A/WP52-B/WP52-C；WP51主稿L136、142直接将效果与共同评分交WP52-A/B/C。
- FR-000079：缺 WP44；WP51附表L80明确中央反向/单纯/封顶由WP44/28。
- FR-000088：缺 WP47-A/WP50；WP52-A主稿L35调用边界交WP47-A；L59物品触发登记查询来自持物合同。
- FR-000089：缺 WP50；WP52-A主稿L90及L104直接调用WP50倍率/命中物品查询。
- FR-000092：缺 WP47-B；WP52-A主稿L233、237明确操作前门、共享状态主合同。
- FR-000093：缺 WP40/WP41/WP46/WP47-A/WP47-B/WP50；WP52-A主稿L245列出的当前上游未进入清单依赖。
- FR-000098：缺 WP52-A；WP52-B主稿L11–15、246明确共同评分/查询/合成由WP52-A消费，本组依赖表无WP52-A。
- FR-000099：缺 WP52-A；WP52-B主稿L11–15、246明确共同评分/查询/合成由WP52-A消费，本组依赖表无WP52-A。
- FR-000100：缺 WP52-A；WP52-B主稿L11–15、246明确共同评分/查询/合成由WP52-A消费，本组依赖表无WP52-A。
- FR-000101：缺 WP52-A；WP52-B主稿L11–15、246明确共同评分/查询/合成由WP52-A消费，本组依赖表无WP52-A。
- FR-000102：缺 WP52-A；WP52-B主稿L11–15、246明确共同评分/查询/合成由WP52-A消费，本组依赖表无WP52-A。
- FR-000109：缺 WP52-A（另有WP20/27/28、WP40/41、WP52-B）；WP52-C主稿L11、207明确共同评分和当前上游，清单只有WP47-A/B、49、50、51。
- FR-000110：缺 WP52-A（另有WP20/27/28、WP40/41、WP52-B）；WP52-C主稿L11、207明确共同评分和当前上游，清单只有WP47-A/B、49、50、51。
- FR-000111：缺 WP52-A（另有WP20/27/28、WP40/41、WP52-B）；WP52-C主稿L11、207明确共同评分和当前上游，清单只有WP47-A/B、49、50、51。
- FR-000112：缺 WP52-A（另有WP20/27/28、WP40/41、WP52-B）；WP52-C主稿L11、207明确共同评分和当前上游，清单只有WP47-A/B、49、50、51。
- FR-000113：缺 WP52-A（另有WP20/27/28、WP40/41、WP52-B）；WP52-C主稿L11、207明确共同评分和当前上游，清单只有WP47-A/B、49、50、51。

必要修正：将历史WP计划依赖保留为事实来源，另明确当前行为依赖/feature_refs或补齐现字段，并标明阶段/关系；无需把所有同篇引用无区别变为强依赖。

## 逐行结论

身份/定位、状态分离和整改绑定均PASS。下表“待查”表示分类依据不足，未认定协作类别本身必错；FAIL另有已证元数据或依赖问题。分类待验证不免除此语义复核。

| feature | 源章节 | 逐行结论 | 语义判断 |
| --- | --- | --- | --- |
| FR-000073 | wp51-ai-action-selection-and-skill.md / 2. 技能值、标记与次序（A/B） | 待查 / CAI-01 | 技能/Flags/传奇野生档、普通调度与Mega登记；需区分框架策略配置和战斗查询/登记消费者。 |
| FR-000074 | wp51-ai-action-selection-and-skill.md / 3. 换人意愿、否决与替补（B） | 待查 / CAI-01 | 普通换人意愿/否决、持久后备近似和回合末估计；保留原集合空槽异常与非事务前缀，协作候选合理但未定义双方责任。 |
| FR-000075 | wp51-ai-action-selection-and-skill.md / 4. 主动道具决策（C） | 待查 / CAI-01 | 主动物品完整资格扫描、整阶段异常、业主资源和登记后消费；协作候选合理，须明确AI上下文、玩家背包/训练家列表和消费顺序验证。 |
| FR-000076 | wp51-ai-action-selection-and-skill.md / 5. 招式/目标候选、分数转选择（D） | FAIL / CAI-03, CAI-01 | 合法槽/目标候选、重定向近似、野生重复、权重抽取与登记；需分策略评分消费者和真实登记，不能只称持久状态交接。 |
| FR-000077 | wp51-ai-decision-defaults.md / 1. HP 道具估量 | 待查 / CAI-01 | AI治疗估量表，SITRUSBERRY估量1与主动真实量分开；这是策略数据，不等同真实HP效果。 |
| FR-000078 | wp51-ai-decision-defaults.md / 2. 治疗/复活类别 | 待查 / CAI-01 | 治疗/复活类别与排序数据，真实许可仍外部消费；策略数据责任待明确。 |
| FR-000079 | wp51-ai-decision-defaults.md / 3. X 道具完整身份与请求量 | FAIL / CAI-03, CAI-01 | X道具身份及请求量供AI偏好，实际中央反向/单纯/封顶另WP44/28；依赖遗漏WP44。 |
| FR-000080 | wp51-ai-decision-defaults.md / 4. 普通换人处理器目录 | 待查 / CAI-01 | 普通换人处理器有序目录，具体条件交主稿；同策略域可保持粗粒度，不应按每个身份再拆。 |
| FR-000081 | wp51-ai-decision-defaults.md / 5. 责任与未决 | FAIL / CAI-02, CAI-01 | 仅总结本包责任、前向交界、特殊模式/全局未决；没有新增独立实现功能。 |
| FR-000082 | wp52-a-evaluation-coverage-and-data.md / 1. 有界集合与责任 | 待查 / CAI-01 | 含有界注册统计、历史B/C责任与共同默认；应区分审计数字和真实默认查询，不据计数证明策略覆盖。 |
| FR-000083 | wp52-a-evaluation-coverage-and-data.md / 2. 本包具体效果登记 | 待查 / CAI-01 | F/T/S/G/P分族及具体效果身份/参数，属于行为数据；同一验收域归组可接受。 |
| FR-000084 | wp52-a-evaluation-coverage-and-data.md / 3. 通用修正与能力评级注册 | 待查 / CAI-01 | 通用修正22项和AbilityRanking add/copy登记；策略数据和分族消费，不是持久状态提交。 |
| FR-000085 | wp52-a-evaluation-coverage-and-data.md / 4. 基础能力评级完整表 | 待查 / CAI-01 | 267身份基础能力评级与字面拼写/默认值；纯AI偏好数据，无事实要求持久写入。 |
| FR-000086 | wp52-a-evaluation-coverage-and-data.md / 5. 已有与前向登记逐项归属 | 待查 / CAI-01 | 已有/前向逐身份归属，包含跨族真正参数边界；应保留目录事实和历史状态，当前单独实现承诺需解释。 |
| FR-000087 | wp52-a-evaluation-coverage-and-data.md / 6. 重复登记定点 | 待查 / CAI-01 | 重复登记的最终有效绑定、缺源不覆盖与共同默认；可作为可观察查询合同，不能要求沿用源码模块。 |
| FR-000088 | wp52-a-generic-numerical-and-status-evaluation.md / 2. 失败、合成与通用修正（A/B） | FAIL / CAI-03, CAI-01 | 预测失败、逐目标/整体合成、友方反转及通用修正；不是实际状态执行，准备副作用仍需独立验证。 |
| FR-000089 | wp52-a-generic-numerical-and-status-evaluation.md / 3. 粗略类型、速度、伤害与命中（B） | FAIL / CAI-03, CAI-01 | 粗类型/速度/会心/伤害/命中与附效估量，保留近似差异；明显消费WP50而依赖表遗漏。 |
| FR-000090 | wp52-a-generic-numerical-and-status-evaluation.md / 4. 能力阶级偏好（C） | 待查 / CAI-01 | 阶级收益、可用招门、天然/残余门和直接变化偏好；同评分边界粗分合理，真实提交仍WP44。 |
| FR-000091 | wp52-a-generic-numerical-and-status-evaluation.md / 5. 状态、异常与持续计数（D） | 待查 / CAI-01 | 状态/混乱/迷恋偏好和状态保留意愿；真实资格与效果分分开，普通评分无持久提交承诺。 |
| FR-000092 | wp52-a-generic-numerical-and-status-evaluation.md / 6. 类型与能力改变的偏好（E） | FAIL / CAI-03, CAI-01 | 类型/能力评分、评级方向及普通User0不消费；GR8-AI-001精确命中该节，WP47-B实际前门依赖遗漏。 |
| FR-000093 | wp52-a-generic-numerical-and-status-evaluation.md / 7. 其它局部前门、依赖和保留（F） | FAIL / CAI-03, CAI-01 | Misc局部前门及依赖/前向保留混合；含真实评分行为可保留粗行，但依赖表遗漏正文明确当前上游。 |
| FR-000094 | wp52-b-effect-coverage.md / 1. 集合与注册语义 | 待查 / CAI-01 | 注册出现和最终有效绑定语义；数字是有界审计，缺源/default行为才是查询合同。 |
| FR-000095 | wp52-b-effect-coverage.md / 2. 逐登记出现、最终绑定与具体合同 | 待查 / CAI-01 | B全登记/最终绑定与正文连接，保持族+身份和原缺源；目录不能替代真实数值行为覆盖。 |
| FR-000096 | wp52-b-effect-coverage.md / 3. 场域收益匹配数据 | 待查 / CAI-01 | 天气/地形收益匹配数据，组内一次匹配；纯AI评分默认数据。 |
| FR-000097 | wp52-b-effect-coverage.md / 4. 保留责任 | FAIL / CAI-02, CAI-01 | 保留责任/未关闭范围和共有开关默认的交叉引用；应挂已有评分功能，不应新增独立协作实现行。 |
| FR-000098 | wp52-b-field-damage-healing-and-target-evaluation.md / 2. 固定量、条件基数、记录与类别（B） | FAIL / CAI-03, CAI-01 | 固定/条件基数、代表估量、最近记录与反击；普通候选与直接处理器异常分开，需WP52-A消费者依赖。 |
| FR-000099 | wp52-b-field-damage-healing-and-target-evaluation.md / 3. 多击、两回合与持续攻击（C） | FAIL / CAI-03, CAI-01 | 多击合并近似、两回合罚、围攻空名单和Geomancy目标族不消费；与真实逐击写入分责明确。 |
| FR-000100 | wp52-b-field-damage-healing-and-target-evaluation.md / 4. 治疗、吸取、持续与牺牲（D） | FAIL / CAI-03, CAI-01 | 治疗/吸取/牺牲偏好含独立可恢复守卫；真实HP夹限/写入与AI分数边界须保留，消费A共同评分。 |
| FR-000101 | wp52-b-field-damage-healing-and-target-evaluation.md / 5. 天气、地形、危害与空间（E） | FAIL / CAI-03, CAI-01 | 天气/地形建立收益、危害和空间偏好；真实期限/入场交WP45，仍需A/51查询消费者。 |
| FR-000102 | wp52-b-field-damage-healing-and-target-evaluation.md / 6. 墙、保护、命中控制与剩余具体合同（F） | FAIL / CAI-03, CAI-01 | 保护、墙、命中/反伤和类型控制评分；近似门、copy缺源和真实执行分开，需A共同合成。 |
| FR-000103 | wp52-c-item-control-coverage-and-data.md / 1. 当前有界账本 | 待查 / CAI-01 | 有界账本统计同时明确直接键优先/条件首匹配/缺源默认；不要把839键当已运行行为覆盖。 |
| FR-000104 | wp52-c-item-control-coverage-and-data.md / 2. C 逐登记及最终绑定 | 待查 / CAI-01 | C全登记及最终绑定；保持167出现/165有效键和跨族copy无效，可作为行为数据粗行。 |
| FR-000105 | wp52-c-item-control-coverage-and-data.md / 3. 完整基础物品评级 | 待查 / CAI-01 | 215默认物品评级，纯AI价值而非实际伤害/恢复值。 |
| FR-000106 | wp52-c-item-control-coverage-and-data.md / 4. 两条件组精确映射 | 待查 / CAI-01 | 39类型增幅物+18宝石条件映射，机制世代/可用伤害门；纯查询数据，可同域归组。 |
| FR-000107 | wp52-c-item-control-coverage-and-data.md / 5. 固定辅助集合与已审数据交叉引用 | 待查 / CAI-01 | 辅助集合和WP47-A/B交叉引用；已有黑名单保持唯一主合同，不应复制制造第二份。 |
| FR-000108 | wp52-c-item-control-coverage-and-data.md / 6. 保留责任 | FAIL / CAI-02, CAI-01 | 仅职责归属、开关默认/未关闭范围交叉引用；应关联已有C/A/B功能，不新增独立实现。 |
| FR-000109 | wp52-c-items-calling-and-control-evaluation.md / 2. 持物价值与消费即时效用（B） | FAIL / CAI-03, CAI-01 | 持物V/即时E价值和熟成/拼写差异；评分不消费物，不能把价值当真实持物收益。 |
| FR-000110 | wp52-c-items-calling-and-control-evaluation.md / 3. 物品操作的预测及偏好（C） | FAIL / CAI-03, CAI-01 | 移物/查封/回收/强制食果/投掷预测偏好，明确不改C/I/R/P/Belch；协作理由必须区别查询与真实操作。 |
| FR-000111 | wp52-c-items-calling-and-control-evaluation.md / 4. 调用、复制、目标和混合控制（D） | FAIL / CAI-03, CAI-01 | 调用替代评估、缺源copy、黑名单/目标与诅咒；准备可写共享字段，真实调用/PP与纯评分分责待具体化。 |
| FR-000112 | wp52-c-items-calling-and-control-evaluation.md / 5. 换人、拘束、先后与 PP 限制（E） | FAIL / CAI-03, CAI-01 | 换人/逃离评分、拘束/号令/行动PP限制；评分不执行逃跑/换出/耗PP，不能替代真实合作原型门。 |
| FR-000113 | wp52-c-items-calling-and-control-evaluation.md / 6. 浮空、变身、侧交换与直接接缝（F） | FAIL / CAI-03, CAI-01 | 浮空/变身/重力/侧交换/位置交换评分；实际写入交WP45/47-B，单一协作理由未说明预测字段归属。 |

## 覆盖及保留

- 8篇正文及1篇catalog的全部有效标题/固定锚点已独立重建并逐项比对，覆盖映射无遗漏；父子功能范围在本域无拆出子行/重计问题。目录可按同一查询域保留粗粒度，不要求逐身份编号。
- catalog正文明确静态推导/未执行，8标题均section-metadata、无独立feature，文档保守绑定R8-U06；没有把这些场景升级成验收PASS。
- GR8-AI-001完整合同：纹理现有目标查询+14定义仅改WP52-A主稿和共享catalog；A主文6行全部保守绑定U06/待整改后核对，FR-000092为直接影响行。该整篇绑定没有冒称11个required都改每行。
- GR8-AI-002是UNSELECTED可选计数维护，附表F/G保持正确；没有将optional混入required。
- 41行均待验证/阶段待定未批准/未实现/未验收，evidence与accepted_events为空，未见已验证或“不纳入目标”误用。
- 四大合作原型不执行不是本轮粗标收尾阻塞；需补具体AI验证问题，尤其主动道具扫描、真实AI上下文、登记/资源消费前缀及预测共享字段。
- 本子审查不修改任何候选、正式正文、参考、main或旧报告，不切分支/commit；提交与远端回读由父审者执行。

## 阅读边界与证据

DELIVERY/review-SKILL/routing README/review-prompt已读；handoff主入口先整体输出有截断，随后以AI合同完整对象与所属索引补读相关范围；不把被截断的其它批次内容计为已完整阅读。
R8-U06 readset.json完整JSON加载，只审AI对象/身份/写集相关索引，不声称读完所有Ruby或其它U06必要伴件。
schema、验证器全局负例、全仓保护与输出commit/push由父审者负责；本报告不替代。

重放本子域静态身份检查：`python review/r8-disposition-independent-d62b41f-20261017/agents/combat-ai-check.py`。本次真实exit=0；UTC、argv、stdout/stderr见 `combat-ai-command.json` 与相邻输出。该脚本只证明身份/结构，不替代上述逐行语义结论。

本结论只针对固定初版候选。R8整改正式完成后，仍须接收协调任务的新精确基线回填和独立再验收；不能称最终完成。
