# Combat 固定基线独立语义复审

受审候选 `d62b41f4d620e50bb04c80a7505374bd284d8210`；来源 `fd1df570cad987dc3852a3b958f03916e317f7fe`；交付 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`。本域结论 **FAIL**，不足以授予“固定基线粗标限定通过”；更不构成最终R8整改/验收。

本上下文实际全文阅读15篇、3213行、426858字节；独立核对318个标题及95条feature（PASS 65 / FAIL 26 / 待查 4）。WP51/52另8篇及AB/AI catalog由独立子上下文combat_ai完整阅读，证据见其报告；其余3篇catalog由root后继补审，本报告不计为已读。

本报告未应用clean-document-revision重写规格；该技能明确排除审计报告。根AGENTS、README、review-prompt、DELIVERY、review-SKILL、handoff入口相关内容及U06实际写集/读集索引已读；长handoff首次工具输出存在截断，本报告不主张其全合同/全原始读集已经全文读完。真实执行配置没有权威echo，model/effort/tier逐项UNVERIFIED。

## 固定输入与机械核对

正式子树 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。15篇工作字节逐篇与受审候选、历史来源、固定交付相同；来源文件/unit哈希、有效标题、锚点及映射集合独立核对结果见JSON。结构错误数 0。稳定ID未改写或重建。

生成view的95行已逐行解析并核对来源锚点、去向、四组状态及相应行位置；唯一字段和来源正文已做语义审查。未把重复的210596字节view另称为人工视觉全文阅读。Schema/验证器与远端保全由root汇总，不在此子报告重复授予通过。

U06正式写集覆盖WP39/40/41/42及WP52-A主稿、相关成长/属性/catalog/UI；本域四篇各行保守绑定R8-U06和11 required ID、状态待整改后核对，接受事件空。其余combat正文未因未选optional F05/AI002自动绑定为已接受或排除。保守整文件绑定是允许的初版口径；仍须未来精确受影响章节差分。

## 逐项问题

### COMBAT-01 P2 — 退款后续消费者落回Showdown父行，物品原型范围不完整

功能ID：FR-000010, FR-000011。

4.2.1实际是H3，与4.2同Markdown层级，但其具名行为显然是同一背包物品退款链；FR10范围含106–123，FR11只97–105。退款后身份残留决定终局二次退款/次轮清身份/失能清身份；不能仅把首次选择和执行分类为协作。

证据：`deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md` L97–115。

必要修正：把106–115纳入FR11，或追加保留稳定ID继承的协作子行，绑定PROTO-BATTLE-ITEM及FR31/背包合同；从父行排除同范围并重新生成映射/view。

### COMBAT-02 P2 — 持久写回、学习和物权边界被整体Showdown标签掩盖

功能ID：FR-000004, FR-000052, FR-000061, FR-000066, FR-000068, FR-000069, FR-000071。

正文明确区分临时能力与持久HP/状态/形态/招式/当前物及可变还原记录。候选只给Showdown通用行为比对问题，没有框架持久写回、索引/身份、事件提交与异常前缀的责任分配；partners中列框架不代替五去向分类和验收边界。

证据：`deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md` L207–226；`deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md` L201–211；`deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md` L116–159；`deliverables/final-specification-set/combat-requirements/wp49-ability-phase-triggers.md` L84–101；`deliverables/final-specification-set/combat-requirements/wp49-ability-phase-triggers.md` L171–210；`deliverables/final-specification-set/combat-requirements/wp49-ability-phase-triggers.md` L226–256。

必要修正：对纯引擎部分保留粗行；把持久提交/回读/学习/物权子节拆成协作边界或将整个真实混合单元标协作，并明确哪个方拥有与提交持久记录；新增原型问题而非宣告Showdown不支持。

### COMBAT-03 P2 — 独立音频、队伍选择与裁判/回放交互未拆表现边界

功能ID：FR-000005, FR-000010, FR-000018, FR-000114, FR-000129, FR-000136。

这些不是单个战斗消息，而是完整音频候选/交付、队伍多选/焦点/摘要/取消、目标光标可视状态、裁判屏幕和回放等待/中止流程，具有与逻辑判定不同的MZ接入与表现验收边界。整行Showdown/框架/双方协作都未描述MZ。

证据：`deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md` L260–278；`deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md` L116–123；`deliverables/final-specification-set/combat-requirements/wp41-switching-positioning-and-escape.md` L65–71；`deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md` L42–50；`deliverables/final-specification-set/combat-requirements/wp56-palace-and-arena-variants.md` L102–112；`deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md` L160–165。

必要修正：按现有子章节拆出MZ表现/输入消费行或明确关联已登记表现功能，并从父行排除对应独立验收范围；逻辑资格/状态写入继续保持相应逻辑去向。

### COMBAT-04 P3 — 覆盖、域外归属和历史保留被制造成独立实现功能

功能ID：FR-000046, FR-000047, FR-000056, FR-000057, FR-000063, FR-000122, FR-000131。

正文主要列来源效果身份→已有主合同、域外责任、旧N01/N02批准同步/CLOSED或未决保留，没有该行独立的新功能。候选把它们全部作为behavior-unit/待实现待验收功能，重复实现计数并把审计事实混入计划。

证据：`deliverables/final-specification-set/combat-requirements/wp47-a-attributes-targeting-calling-data.md` L202–214；`deliverables/final-specification-set/combat-requirements/wp47-b-control-items-coverage-data.md` L95–105；`deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md` L186–195；`deliverables/final-specification-set/combat-requirements/wp54-entry-rules-and-cup-data.md` L66–87；`deliverables/final-specification-set/combat-requirements/wp56-palace-and-arena-variants.md` L139–141。

必要修正：保留永久ID历史导航，明确这些行是来源元数据/不单计实现单元，并关联已存在行为行；不得删除历史ID来重建编号，不得用不纳入目标回避元数据归属。

### COMBAT-05 P2 — 文档模板依赖漏掉直接背包、成长、终局、保存和图鉴消费者

功能ID：FR-000011, FR-000022, FR-000029, FR-000061, FR-000124, FR-000136。

每文档全部行复制同一小组WP依赖，feature_refs全空。例如FR11没有WP27/28/42，FR22没有WP42，FR29没有WP19/20，FR61没有WP42/49/50，FR124没有WP09/10/25，FR136没有WP62/09。它们均由正文直接规定，关系不是可选远期猜测。

证据：`deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md` L97–115；`deliverables/final-specification-set/combat-requirements/wp41-switching-positioning-and-escape.md` L172–175；`deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md` L59–95；`deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md` L116–159；`deliverables/final-specification-set/combat-requirements/wp55-facility-session-and-restoration.md` L62–69；`deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md` L144–155。

必要修正：补真实输入、提交和消费者依赖；允许WP级粗标但须纳入必要合同或具体feature引用，并区分来源叙述关联和未来实现依赖，重新检查图与view。

### COMBAT-06 P2 — 替补/招式逃离的协作原型只覆盖一个标题

功能ID：FR-000020, FR-000058。

FR20包含野生拒下一只→替补逃跑决定3→同次扫描继续提示/绑定的完整非致死链；FR58含可逃查询/决定3和玩家不可取消中途替补等待。它们均为Showdown且未关联FR22/PROTO-ESCAPE，只有通用行为比对问题，遗漏实际入口及调用者消费。

证据：`deliverables/final-specification-set/combat-requirements/wp41-switching-positioning-and-escape.md` L114–128；`deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md` L19–47。

必要修正：将相关子边界标为协作或明确待原型裁决，关联逃跑/替补协议与世界终局；保留普通战斗内部状态机的粗粒度，勿把所有换人统一改成同一资格。

## 每文档完整阅读与固定身份

| 文档 | 完整实读 | 标题 | SHA256 |
| --- | --- | ---: | --- |
| wp39-battle-context-and-participants.md | L1–L335 | 35 | `7935a16da1143adb97f1f8fcfc83ce68c658ad19e64660d2c711aaaf87571a20` |
| wp40-commands-obedience-and-action-order.md | L1–L360 | 40 | `18dad0c34d67fe156e0e4a9663c6e63db86724fe842f8af514467e41918bc8c5` |
| wp41-switching-positioning-and-escape.md | L1–L250 | 31 | `b736c186f666fab4e68f3b82dd928a825e7c0385021e2e7623e6037ea05ae2eb` |
| wp42-growth-end-of-round-and-battle-outcomes.md | L1–L285 | 29 | `414b69714ed8233f46b0f1ffa5aac34d2252c4ccd7cfddca70b31a0eb55e91ec` |
| wp45-weather-terrain-side-and-position-effects.md | L1–L232 | 32 | `bcb8c6c7d4b86e30799d866952db35ca5448d4922d6e7873d95f368a498623da` |
| wp47-a-attributes-targeting-calling-data.md | L1–L214 | 6 | `1137ca38a1a52a527b9058063ac8cbf82c1f3452097f3943d23f0425174ce141` |
| wp47-a-move-attributes-targeting-and-calling.md | L1–L221 | 20 | `0e3a3fa46ab07fd82331db7b5790788c75b5aa45f6093aa9b2db5cf6c55b3fa3` |
| wp47-b-control-items-coverage-data.md | L1–L105 | 6 | `3a4b189f23a82dae95b0750ca6967d168ee85afe6e27594e00e6d183f4a63827` |
| wp47-b-switching-control-and-item-changes.md | L1–L200 | 20 | `ffe11e08dee19a63a9a8108aa62f1d820cf40d76047c05b137a71047c6b3b6eb` |
| wp49-ability-phase-triggers.md | L1–L272 | 24 | `f48646d40325a44265d2a85e7459366d894bde64f206e931a7574dfc39cb368f` |
| wp54-entry-eligibility-level-adjustment-and-clauses.md | L1–L156 | 15 | `ce75fa71462b015963efb374f35325a8572698d86ab8d7595362a10675ca9148` |
| wp54-entry-rules-and-cup-data.md | L1–L109 | 10 | `8a888bc922e222bdf11f78fe9d25713a0d33f0ac140406f99082f3e2ce70ec03` |
| wp55-facility-session-and-restoration.md | L1–L152 | 15 | `226c00f62dd915bc089e41f640c2bff1ec707a3845d683e4bfb75221ad8047c6` |
| wp56-palace-and-arena-variants.md | L1–L141 | 16 | `fee7a028ad9b1db8fae48145b092b18efc89757db943eb6e3f234ace7c111368` |
| wp58-battle-recording-and-playback.md | L1–L181 | 19 | `91afabffb2bc6def0f1db64835b1833751613392a26735ba863994ed49d7f061` |

## 95行逐项裁定

PASS只表示该固定粗标的分类/粒度可接受，不代表目标支持、实现或验收已完成。FAIL行依据正文与候选实际字段；待查是已全文阅读后仍缺具体职责依据，不能计作PASS。

| ID | 结果 | 语义理由 |
| --- | --- | --- |
| FR-000001 | PASS | 包装生成、对象复用、伙伴编组和世界入口跨边界，协作候选合理；未把返回真当胜利。 |
| FR-000002 | PASS | 布局/所有者与持久参与成员接入相关，协作候选合理；保留合法三打显示秩异常。 |
| FR-000003 | PASS | 席位—所有者—玩家/伙伴段映射与参与记录需共同约定，粗标协作可接受。 |
| FR-000004 | FAIL | 本节不仅建立临时席位，还逐字段写穿持有物/等级/形态/HP/真实异常，并从持久个体回读；单一Showdown承担遗漏明确持久提交边界。 |
| FR-000005 | FAIL | 创建规则/世界环境映射的协作候选合理，但同一行并入7.5整套选曲请求、预置和播放交付，遗漏表现职责独立边界。 |
| FR-000006 | PASS | 规则/不变量约束入口和双方模型，作为已有功能的共同验收约束可接受；不视为额外已实现功能。 |
| FR-000007 | PASS | 入口报错、skip和包装返回边界横跨世界与战斗，协作候选合理。 |
| FR-000008 | PASS | 配置变体对创建、捕获/伙伴等组合有直接行为影响，粗标协作合理；未批准首版。 |
| FR-000009 | PASS | 玩家命令、AI控制和即时逃跑/背包登记是共同输入协议，协作候选合理。 |
| FR-000010 | FAIL | 物品4.2已拆，但4.2.1退款残留身份/正常终局/次轮命令消费者仍留本Showdown父行；4.3目标光标到确认亦含表现边界。 |
| FR-000011 | FAIL | 去向和PROTO-BATTLE-ITEM合理，但范围只97–105，未关联106–115退款整链，且缺背包WP27/28与终局WP42必要依赖。 |
| FR-000012 | PASS | 攻击全序调用物品、Mega、成长、诊断和普通招式，协作粗标可接受；通用待验证不能代表通过。 |
| FR-000013 | PASS | 优先级、子优先级、速度/同速、增量重排属于战斗内部规则，Showdown承载候选合理。 |
| FR-000014 | PASS | Mega资源/次数与个体变形、Shadow Call及Shift接入有不同领域，协作候选合理。 |
| FR-000015 | PASS | 登记/执行、退款、PP与控制权的不变量供本篇共同验收，协作候选合理。 |
| FR-000016 | PASS | 终止、失败/消耗与特殊模式边界是共享观察结果，协作粗标合理。 |
| FR-000017 | PASS | 徽章/Shadow/环物品和战斗配置有真实领域消费者，协作候选合理。 |
| FR-000018 | FAIL | 换入/换出战斗资格可调查引擎，但3.4独立队伍界面canCancel/按钮/摘要/登记正交流程未从Showdown承担拆出。 |
| FR-000019 | PASS | 出入场顺序及同席位临时效果属于引擎候选，持久个体来源已有上下文映射；可接受粗标但需继续校准R8缺秩整改。 |
| FR-000020 | FAIL | 替补循环含野生拒下一只的即时逃跑与决定3后继续扫描；与FR22/PROTO-ESCAPE缺少显式关联，需纳入同一协作原型。 |
| FR-000021 | PASS | Shift重映射十项/例外、选择交换、行动代价是战斗内部状态，Showdown候选合理；立绘消费由表现域接。 |
| FR-000022 | FAIL | 三种入口、计数/随机、决定3与世界终局为协作原型，去向合理，但依赖只WP27/40，未列明确终局WP42。 |
| FR-000023 | PASS | 招式逃离/替补/后备交互与决定3交界，协作粗标合理。 |
| FR-000024 | PASS | 换人与Shift/拖出/逃跑不变量关联本篇，协作粗标合理。 |
| FR-000025 | PASS | 取消、无替补、目标变化及结果消费者跨输入和战斗，协作候选合理。 |
| FR-000026 | PASS | 玩家系统switchStyle及接力/多打配置有双方消费者，粗标协作合理。 |
| FR-000027 | PASS | 持久个体、临时场上副本、捕获队列与世界状态分层明确，协作候选合理。 |
| FR-000028 | PASS | 主循环/裁判内部顺序可调查引擎承担，捕获/逃跑结果仍按已有跨域行输入，未声称兼容。 |
| FR-000029 | FAIL | 成长立即提交、逐级/学招等待、场上回读以协作+原型登记正确；缺WP19/20等明示持久能力/招式依赖。 |
| FR-000030 | PASS | 完整回合末顺序/早退、缓存与重读为引擎候选，成长/替补通过已独立合同交接，粗标可接受。 |
| FR-000031 | PASS | 终局退款、捕获接收、病毒、可变还原记录与双方资源清理确属协作，粗标合理。 |
| FR-000032 | PASS | 世界善后/队伍治疗、进化、拾取/采蜜与包装返回由框架编排合理；音频/过渡的消费还应关联表现域。 |
| FR-000033 | PASS | skip/中止/一般异常有不同内外层出口，协作候选合理，未补造finally或已校准。 |
| FR-000034 | PASS | 配置和跨阶段不变量是该合同验收约束，协作粗标合理。 |
| FR-000035 | PASS | 天气/场地/侧/位置域状态模型是战斗内部状态，Showdown候选合理。 |
| FR-000036 | PASS | 规则和世界天气的创建瞬间映射需共同输入协议，单独协作行拆分适当。 |
| FR-000037 | PASS | 天气覆盖/压制/期限/原始来源和ShadowSky明确战斗内生命周期，Showdown候选合理；Shadow范围待决策另行保留。 |
| FR-000038 | PASS | 场地接地查询与自然到期/直接移除通知属战斗引擎候选，不把数值相同当行为通过。 |
| FR-000039 | PASS | 44项作用域目录是行为数据，独立按全场/侧/位置生命周期承载可接受。 |
| FR-000040 | PASS | 火海双递减、侧保护最后行动和13项换场/清除是战斗内部规则，Showdown候选合理。 |
| FR-000041 | PASS | 危害资格顺序/实际伤害/吸收属战斗引擎候选，持久HP交接需沿共享写回合同。 |
| FR-000042 | PASS | 祈愿/延迟来源/位置交换的生命周期和组合规则为引擎候选，可保留合并粗标。 |
| FR-000043 | PASS | 七调用入口的完整排除名单与世代增量是行为数据，可与引擎承载候选对应。 |
| FR-000044 | PASS | 17/17/4持物改类型映射是规则数据，Showdown候选合理，不据数据一致宣告支持。 |
| FR-000045 | PASS | 自然之恩67条默认内容及缺标志边界为规则数据，Showdown候选合理。 |
| FR-000046 | FAIL | 本节仅列59身份→已有主合同位置，属覆盖/追溯索引，独立待实现功能行重复制造实现承诺。 |
| FR-000047 | FAIL | 本节只划WP45/46/44/47B等已有域外责任，无独立实现行为，应该关联已有行作元数据。 |
| FR-000048 | PASS | 当前类型与四种原能力数值只改场上副本，持久不变边界明确，Showdown候选合理。 |
| FR-000049 | PASS | 类型/环境/每击当前持物读取及异常前缀为引擎规则候选；不把自然之恩等同背包主动道具。 |
| FR-000050 | PASS | 命中/保护/时机和具名例外属于引擎规则，Showdown候选合理。 |
| FR-000051 | PASS | 执行期动态目标构造、重定向/反射属于战斗引擎规则，Showdown候选合理。 |
| FR-000052 | FAIL | 调用/模仿属引擎，但6.3写生先写持久招式再写场上槽与新PP，整体Showdown承担漏持久学习提交边界。 |
| FR-000053 | PASS | 号令32项/安可常6增6排除表是引擎行为数据，Showdown候选合理。 |
| FR-000054 | PASS | 不可移物物种/原能力组合及邮件/Mega限制数据是战斗规则数据，Showdown候选合理。 |
| FR-000055 | PASS | 578条投掷默认威力仅内容数据，Showdown候选合理，未把静态数据登记当运行。 |
| FR-000056 | FAIL | 60项身份→主合同位置只是覆盖索引，应作来源元数据关联行为行。 |
| FR-000057 | FAIL | 已有/共享域外归属主要说明WP44/45/46/47A责任保留，不应成为独立实现功能。 |
| FR-000058 | FAIL | 招式逃离、强制替补和玩家中途选择具有决定3与等待接缝，整体Showdown且无逃跑/替补原型关联不足。 |
| FR-000059 | PASS | 拘束/代价/行动推进、号令记录恢复属于引擎规则，Showdown候选合理。 |
| FR-000060 | PASS | PP减少通过真实招/变身身份同步条件明列，战斗规则候选合理，需沿WP20共享写回合同。 |
| FR-000061 | FAIL | 当前持物写穿、I/R/P/Belch、野生永久转移/终局还原不是单纯临时计算，整体Showdown缺持久物权协作职责；并漏WP42/49/50依赖。 |
| FR-000062 | PASS | 能力只改场上、浮空/变身临时复制边界明确，Showdown候选合理。 |
| FR-000063 | FAIL | 本节为N01/N02已批准同步和CLOSED事实，只有历史/审计责任，不构成新待实现功能。 |
| FR-000064 | PASS | 能力身份/有效性与失去获得顺序是引擎候选，持久与场上字段差异已作为输入合同保留。 |
| FR-000065 | PASS | 入场反应/威吓/天气场地与能力获取全序为引擎候选，Showdown粗标合理。 |
| FR-000066 | FAIL | 离场恢复真实异常/HP、濒死友好和图鉴等跨持久域，整体Showdown缺框架提交与终局层次的职责说明。 |
| FR-000067 | PASS | HP跨半、状态/阶级/失败回调规则属引擎候选，持久字段写回仍需共享提交合同。 |
| FR-000068 | FAIL | 每击时序虽为引擎，MAGICIAN/PICKPOCKET转当前物与还原记录并立即触发，跨物权状态协作边界未细分。 |
| FR-000069 | FAIL | 回合末普通规则可引擎承担，但BALLFETCH/HARVEST/PICKUP获得物、还原和消费跨持久物权；整体Showdown缺协作接点。 |
| FR-000070 | PASS | MIMICRY场上类型和通知顺序为引擎规则，Showdown候选合理。 |
| FR-000071 | FAIL | 9.2通用形态提交个体/图鉴、9.3共生当前物转移与还原记录差异跨持久层，整体Showdown不足。 |
| FR-000072 | PASS | 本节混合不变量/失败/配置和依赖，有实际回调约束，可关联本篇作为验收合同；不解释为完成实现。 |
| FR-000114 | FAIL | 资格/组合由框架筛选合理；2.3独立多选界面的次序、按钮/焦点/取消/摘要与提交流程未拆出MZ表现责任。 |
| FR-000115 | PASS | 赛前成员/队伍约束和数据缓存为框架领域合同，归属合理。 |
| FR-000116 | PASS | 临调经验/HP、两侧按索引还原、异常前缀和战斗调用跨层，协作候选合理。 |
| FR-000117 | PASS | 规则组合含报名、临调和战斗条款，协作候选合理，保留直接样本/工厂/模式差异。 |
| FR-000118 | PASS | 14条款键的设置与实际战斗消费者有共同接入职责，协作候选合理。 |
| FR-000119 | PASS | 工厂组合数据含领域资格、临调与战斗条款，协作候选合理。 |
| FR-000120 | PASS | 直接样本/模式转换数据需框架装配并交战斗，协作粗标合理。 |
| FR-000121 | 待查 | 固定资格限制数据与框架资格筛选相同责任，整篇套协作缺为何与FR115框架实现不同的依据，待确认。 |
| FR-000122 | FAIL | 明确56个来源定义身份/主合同定位只是审计索引，独立协作功能行不当。 |
| FR-000123 | PASS | 条款设置与真实消费接缝有直接行为数据，协作候选合理。 |
| FR-000124 | FAIL | 会话存档、原队伍引用、暂停继续/位置恢复、内容生成全塞协作；未拆框架会话与战斗对局接点，缺WP09/10保存及队伍必要依赖。 |
| FR-000125 | PASS | 单场包装的经验/物品调整还原与结果回传为协作边界，粗标合理。 |
| FR-000126 | 待查 | 失败/取消主要会话/生成/保存与单场异常混合；框架职责和协作故障接点未区分，待确认。 |
| FR-000127 | PASS | 配置/内容资源/消息/地图坐标与依赖清单是来源数据合同，协作粗标可接受但资源呈现需关联MZ。 |
| FR-000128 | 待查 | 特殊模式保留用户范围决定正确；自动命令取代正常选招、AI换人/随机域与引擎交接未在框架实现建议中说明，待查。 |
| FR-000129 | FAIL | Arena同时规定引擎成功状态机/裁判持久HP与非战斗裁判画面，单一框架实现缺逻辑/战斗/MZ独立边界。 |
| FR-000130 | 待查 | 普通/Palace/Arena差异是验证矩阵，可关联功能，但单一框架建议未解释引擎改造或协作方案，待查。 |
| FR-000131 | FAIL | 仅声明回放/内容生成/事件/宿主/运行保留，应作范围元数据，不应成为独立框架实现功能。 |
| FR-000132 | PASS | 导出临时记录和全局上次战斗的生命周期跨战斗输出/保存，协作候选合理。 |
| FR-000133 | PASS | 18初始条件与布局/未录选项差异需框架与引擎共同冻结，协作候选合理。 |
| FR-000134 | PASS | 登记钩子/撤销残留/记录槽与实际命令分层需共同协议，协作候选合理。 |
| FR-000135 | PASS | 三随机域和询问式替补/回放序列交界清楚，协作候选合理。 |
| FR-000136 | FAIL | 回放副本仍扣实时背包/写实时图鉴的协作候选合理，但6.4消息自动/选靶/中止表现未拆，且未列实时WP09/38/62等关键依赖。 |

## 限定与后继

捕获/背包道具/逃跑/战中成长原型均未运行；相关行未把来源规格当兼容证明、阶段待定且未批准、实现未实现、验收未验收，状态诚实是保留项。去向合理性仍必须修正上述缺陷。未知原型不阻止接受合理粗标，但不豁免本次语义判断。

Palace/Arena范围及框架如何接管引擎调度、纯框架会话/数据为何被套协作等4行已列待查。既有异常仍按来源事实保留，未来是否兼容应由用户/原型决定，不能通过改正式正文消除问题。当前未批准“不纳入目标”行0，本域未发现暗中排除。

本代理只写本独占review/agents/combat-*，未切分支、未提交、未改作者工件/正式规格/reference/main。后继必须绑定新的精确commit，保留本失败证据，针对变更影响重新核验；正式整改完成后再接受协调任务的固定新基线、回填并独立验收。
