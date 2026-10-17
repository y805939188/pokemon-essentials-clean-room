# R2来源接收与后继工具独立补充审查

固定候选 `a32873d2860b15d9f5e27727db8f131f4ec433b6`。当前908的真实来源数据没有发现回执身份失配，21个新增标题的现有消费者建议均有具体语义依据。发现三项可复现的后继来源工具缺陷，不能预授这些代码PASS。它们不摊派为736个功能分类FAIL；U04尚未接受、未切换的真实阶段本身不是本轮分类失败。

## 已核事实与资格

累计8批回执的33目标bytes/SHA256/blob全部与固定Git相等；这些目标在0eee中仍同字节。R8-U07为非正式正文overlay，未制造新功能。实际写集比原计划增加6份正式文档：U09的WP26、WP23附表、WP31、WP34、WP66-A，以及U06的WP58；不能从旧计划未列写集推为不受接受门约束。当前清单仍只有908/U02/U03，独立重算736active、191绑定=17接受+174待核。

从Git重算131文档历史/908均2683标题，0eee为2704；新增21、删除0。11个accepted-source标题只形成准备建议，另10个U04标题为pending建议。完整读908→49的713行/112106 bytes及49→0eee的361行/57082 bytes全部增删/上下文和文件/hunk头，证据与Git diff逐字节一致；另读B8→908两处单行改动。21新章完整正文均在这些新鲜diff读集中，另完整读WP33兼容、WP34亲本角色、WP51候选以及UI65§6/§8指定范围。未宣称131篇全量新鲜全文阅读。

`prepared-source-backfill.json`的736个locator及49个changed-unit ID已独立重算全相等；没有将它们当当前应用。真实作者prepare/apply I/O中的3核心输入hash和工具hash与候选相等，apply因6个纯U04文件缺正式接受被拒且核心不变。未发布或要求U04回执。

UI65的U01只接收§3.1/§4.1；实际§6.1仍写玩家未移动/静止，§8.1仅回指§6.1，未绑定WP12的普通移动/跳跃计时定义。对应645/647仍为明确待同步消费者；U01整文件身份不转授U04义务。当前拒绝门保持正确。

## 三项工具发现

### SOURCE-R2-001（P2）接受事件只约束旧actual身份，可把同路径后继未接受字节当作已接受来源

Event target matches old accepted commit, ancestry passes, current changed bytes need only a nonempty relevant accepted_event. Unaccepted blob92a99ce3 is accepted under d895aa9d receipt.

复现：`python review/r8-disposition-r2-independent-a32873d-20261017/agents/source-audit.py; isolated Git descendant of908 adds one sentence to accepted WP04 L196. Recompute actual identities/locators, retain exact old receipt/registry. routing.errors returns []. No apply executed.`

必要修正：Validate each changed current document against the accepted target identities whose bytes still apply at the exact current snapshot; do not use path membership/ancestry as accepted-content identity. Shared U01/U04 consumers require explicit source-scope and pending-batch handling. Add stale-receipt descendant regression.

当前影响：Real908 and all33 target bytes in0eee match their receipts; no observed candidate data mismatch. The future source gate code is unsound. Do not reclassify736 functional rows.

代码：`planning/implementation-routing/r8-20261017/routing.py:257`, `planning/implementation-routing/r8-20261017/routing.py:278`, `planning/implementation-routing/r8-20261017/routing.py:332`, `planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py:131`, `planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py:171`。证据：[source-stale-receipt-probe.json](source-stale-receipt-probe.json), [source-fixture-command-io.json](source-fixture-command-io.json), [source-audit.py](source-audit.py)。

### SOURCE-R2-002（P3）backfill继承1776个null理由，输出不满足新current coverage schema

1776 historical metadata_reason keys are explicitly null. dict.get(default) preserves null; schema requires a nonempty string. Independent schema check returns1776 type errors. prepare validates only manifest/historical coverage, so misses these future output errors.

复现：`python review/r8-disposition-r2-independent-a32873d-20261017/agents/source-null-reason-probe.py. Build inherited sections with exact backfill get/default expressions; validate synthetic908 current relation against fixed new schema.`

必要修正：Either model functional-mapping null reasons intentionally in current schema or normalize them to meaningful strings in backfill. Validate complete prospective current coverage before any core writes; retain historical coverage unchanged. Add a schema round-trip regression.

当前影响：Current source switch is correctly blocked before writes; no real current-section-coverage exists. This is independently demonstrated future output incompatibility, not a claim that current2704 full checks ran or failed.

代码：`planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py:186`, `planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py:227`, `planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py:235`, `planning/implementation-routing/r8-20261017/current-section-coverage.schema.json:121`。证据：[source-coverage-null-reason-summary.json](source-coverage-null-reason-summary.json), [source-null-reason-probe.py](source-null-reason-probe.py), [source-coverage-null-reason-probe.json](source-coverage-null-reason-probe.json)。

### SOURCE-R2-003（P3）任意行为标题可用ALL_FORMAL_FEATURES标签逃过空消费者拒绝

The special literal exempts any section from nonempty feature/metadata mappings; schema permits arbitrary coverage_scope strings and check has no path/class qualification. This is a structural blank-mapping hole, not a request to automate consumer relevance.

复现：`python review/r8-disposition-r2-independent-a32873d-20261017/agents/source-coverage-probe.py. Synthetic908 section table normalizes the separate null-reason issue; baseline[]. Clear both consumer arrays for WP39 chapter4 and set coverage_scope=ALL_FORMAL_FEATURES; check returns[].`

必要修正：Constrain ALL_FORMAL_FEATURES to the fixed governance-document identities or explicitly approved governing headings; require nonempty resolved refs elsewhere. Add an ordinary behavior-heading negative fixture using the exemption literal.

当前影响：Actual21 proposed heading mappings have consumers and no observed abuse. Do not convert this guard finding into failures for the39 consumer features or736 classifications.

代码：`planning/implementation-routing/r8-20261017/revisions/r2/tools/current-coverage-check.py:45`, `planning/implementation-routing/r8-20261017/current-section-coverage.schema.json:117`。证据：[source-coverage-scope-probe.json](source-coverage-scope-probe.json), [source-coverage-probe.py](source-coverage-probe.py)。

## 21个新增标题的逐项建议

以下PASS仅表示建议的语义消费者合理；没有应用locator，没有授pending源接受，也没有给目标兼容、实现或原型PASS。

| # | 标题 | 现有消费者 | 资格 | 独立判断 |
| --- | --- | --- | --- | --- |
| 1 | 4.3.1 已有野生个体的零计数与原序边界 | FR-000002, FR-000007, FR-000009, FR-000013, FR-000677, FR-000686 | accepted-source建议 | 初始化/人数与实际席位、失败前缀归2/7；命令/优先序归9/13；UI请求与失败入口归677/686。新子节细化现有职责，不产生新的承载功能。 |
| 2 | 6.2 蛋群的固定作者身份目录 | FR-000397, FR-000137, FR-000214, FR-000508, META-000020 | accepted-source建议 | 15个作者身份是397固定目录，137继承，214兼容先行门与508亲本角色真实消费；META20字段责任导航适合保留。 |
| 3 | 5.1.1 有序删除与下次载入门 | FR-000451, FR-000446, FR-000642 | accepted-source建议 | 主档→单备份删除与下次主档门是451失败恢复、446保存和642标题入口的交接；部分删除失败不回滚。 |
| 4 | 已有野生输入与越额 EV 的静态边界 | FR-000002, FR-000007, FR-000009, FR-000013, FR-000456, FR-000204, FR-000029 | accepted-source建议 | Z/M组接2/7/9/13，EV组接456/204/29；分类与静态向量分母保持，不把21个测试ID新造为功能。 |
| 5 | 纹理目标评分查询的静态对照 | FR-000092, FR-000076 | accepted-source建议 | Conversion直接目标贡献归92，普通User0候选是否进入归76；不把贡献NOT_ENTERED当整候选固定100。 |
| 6 | 有序删除与启动读取结果的静态对照 | FR-000445, FR-000446, FR-000449, FR-000451, FR-000439, FR-000642 | accepted-source建议 | H2聚合下方删除/系统装配两组；445/446/449/451/439/642为真实启动、持久、迁移、语言及UI消费者。 |
| 7 | 默认主档与相邻备份删除 | FR-000451, FR-000446, FR-000642 | accepted-source建议 | KER001五例只消费451/446/642的有序删除、前缀与标题回返；没有新增独立文件I/O功能。 |
| 8 | 系统装配与后续有效性分层 | FR-000445, FR-000449, FR-000451, FR-000439, FR-000642 | accepted-source建议 | KER002区分旧序列适配449、空性装配445、有效性/递归备份451、语言439与标题642；身份/后验门完整。 |
| 9 | 普通 EV 分配输入域的静态对照 | FR-000456, FR-000204, FR-000029 | accepted-source建议 | ST01–05归456模板存储、204普通非Shadow分配和29成长同步；默认非内部设施早门与道具/Shadow排除保留。 |
| 10 | 2.2 图像身份与当前语言 | FR-000699, FR-000440, FR-000352 | accepted-source建议 | 七个Slot图像角色归699，game/core查找440与资源352；固定背景等不被批量翻译。 |
| 11 | 6.1 图像选择、加载失败与已完成前缀 | FR-000703, FR-000354, FR-000702 | accepted-source建议 | 空身份提示/转轮路径分别归703/354，已完成财务前缀归702；32×32普通fallback与更早空名失败不能合并。 |
| 12 | 5.2.1 范围修剪与当前图引用 | FR-000325, FR-000323 | pending-U04建议 | 当前图的范围门/容器集合归325，按ID取图与全局引用区别归323；有限滚屏静态夹具不新造相机或保存功能。 |
| 13 | 5.2.2 邻图摆放失败后的后继能力 | FR-000325, FR-000323, FR-000326, FR-000409 | pending-U04建议 | 摆放阶段异常后同容器抑制归325/323；同实例重建326与通知首次异常409为明确交界，没有保证恢复。 |
| 14 | 3.4 直接119、缺目标与末尾入口 | FR-000336, FR-000335, FR-000339 | pending-U04建议 | 直接119主矩阵336、外层推进335和主文镜像339准确；不套101预读或移动路线体系。 |
| 15 | R8 地图、末端调用与解释器边界 | FR-000323, FR-000325, FR-000326, FR-000330, FR-000335, FR-000336, FR-000338, FR-000339, FR-000346, FR-000409, FR-000445, FR-000446, FR-000642, FR-000645, FR-000647 | pending-U04建议 | H2只聚合六静态族的现有消费者；子标题分组保持具体用途，无新增运行功能。 |
| 16 | R8-PBS：文本配置与运行资格 | FR-000346, FR-000323 | pending-U04建议 | PBS051文本Dungeon标记归生成输入346/临时图查询323；文本已知不提高编译、资源、Demo和运行资格。 |
| 17 | R8-NP：邻图摆放失败后的后继能力 | FR-000325, FR-000323, FR-000326, FR-000409 | pending-U04建议 | NP01–05归生命周期325、获取323、重建326与通知409；外层捕获继续前提和成功/入口前后失败分开。 |
| 18 | R8-RP：当前图范围修剪与消费者 | FR-000325, FR-000323, FR-000326, FR-000446, FR-000445, FR-000642 | pending-U04建议 | RP01–05归325/323，RP06条件保存446，RP07正常读档326/445及更早面板642；不称真实存档往返。 |
| 19 | R8-JT：活动跳跃与地图末端门 | FR-000330, FR-000645, FR-000647 | pending-U04建议 | JT01–06归330普通移动/跳跃计时，645菜单和647快捷是明确待同步入口；UI65缺口仍PENDING，不授U04接受。 |
| 20 | R8-CE：117父子绑定与私有键 | FR-000338, FR-000336, FR-000339 | pending-U04建议 | CE117子携父当前编号并绑定建立时当前图归338，矩阵336与主文339同步；不新造保存功能。 |
| 21 | R8-LB：直接119命中、缺目标与末尾 | FR-000336, FR-000335, FR-000339 | pending-U04建议 | LB命中/缺目标/末尾/重复及后继失败归336/335/339；入口前门与已分派缺目标分开，未执行资格保持。 |

## 工具约束与未执行项

backfill能核receipt目标本身的固定身份、旧事件兼容、正式文档索引、行映射歧义、保全source/plan/retired以及未接受路径/未映射新标题。其机械行对齐不是语义证明。current coverage能拒绝标题身份/顺序缺失、无效消费者ID、事件导航不等与缺新标题显式声明；新schema负责对象字段类型，但上述空映射豁免仍可绕过。accepted-binding-regressions的5项只针对扩展门遗漏、回执域外文档、部分共享事件、无关事件和清空已变源接受；不含本次旧回执后继字节探针，且它从真实扩展/共享应用基线取样，当前908不具备该基线。

作者5项扩展/共享绑定回归和真实current2704全量检查仍为`NOT_EXECUTED_AWAITING_U04`。本补充分工没有运行这些后继完整验收；独立函数/JSON-schema/Git夹具只证明三个具体结构缺口。第一个coverage夹具构造曾因可选字段缺失而失败；补默认后暴露1776个null-schema错误，随后为隔离ALL_FORMAL探针显式归一null。失败与后继结果分开留证，没有给失败输入PASS。接受来源证据中的21个heading hash为标题字符串hash，规范current locator用整行hash；两种已分别核清，未误报为locator身份失真。

原ROOT-TOOL-02的历史PASS针对当时已知batch/event存在、固定绑定与可解析范围；新receipt-current身份facet作为同根扩展单列，是否重开原组交root统一裁定。此补充未分配旧ID表，未继承或重复投票给旧721/736/33裁定。完整机器结果见[source-results.json](source-results.json)，逐输入/读集身份见[source-machine-evidence.json](source-machine-evidence.json)及[source-prior-reconciliation.json](source-prior-reconciliation.json)。

本分工保留交付仅为本review的source-*工件；两次早期探索importlib曾生成作者目录下忽略的routing/backfill Python缓存，已逐文件删除并清理空缓存目录，候选源码/数据字节未改。Git变异夹具位于`/tmp/r8-r2-source-fixture-a32873d.git`，原对象库只作只读alternates，没有修改作者formal/reference/history/main或运行Ruby/游戏/业务模型/宿主/Showdown原型。真实model、effort、tier、speed、Fast与云UUID无权威echo，逐字段UNVERIFIED；这是一个审查的分工，不是新增独立接受票。
