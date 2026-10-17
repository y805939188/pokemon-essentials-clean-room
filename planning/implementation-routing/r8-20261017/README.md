# 正式规格去向清单

本清单为未来实现提供章节级候选。固定历史来源为`fd1df570cad987dc3852a3b958f03916e317f7fe`，R8交付为`4575e80d041ab0c74a42e2e36399d05791dbaa5b`，两者正式子树均为`f292698cdd4a8e725525a9be6dc34b75faaf151e`。当前适用版本由主清单`current_snapshot`和真实接受事件决定；打标分支工作区的正式规格始终保持B8的`f292`子树；工具通过`git show`读取独立的接受payload，不能将工作区字节当作当前版本。原规格正文、原稳定ID和immutable source不随规划修订改写。

当前为R2精准返修候选，固定独立R1 FAIL为`8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8`；12项作者修复等待父任务另建ultra/default独立复核。现有736个活跃行、33个完整退役旧行与33个元数据；R2新增769并退役86，保留全部历史source。

本候选当前实际应用仍为`908273093e1f6b27fc58249417675dd62d146224`及U02/U03两个事件；191个原批次绑定行中17个已回填、174个待核对，是当前已应用快照的口径。另已收到并核对累计8批回执，33个实际目标身份匹配，真实写集比原计划增加6份正式文档。后继actual `0eee6d141f33758eda34bd8ebad94a3e2b617f5a`的736个locator仅已准备，**未应用8批切换**：6个纯U04变更文件无ACCEPTED，UI65还有U01/U04共享接收边界。历史2683标题已覆盖；0eee实际观察2704标题，新增11个已接受源标题有显式现有消费者建议，另外10个U04标题仅PENDING建议，不能把2704称当前已应用覆盖。完整源切换被真实门拒绝，待正式U04回执及最后源差分复核后再执行。

来源接收与后继准备：[8批回执身份接收](revisions/r2/tools/accepted-receipt-intake.json)、[736定位准备](revisions/r2/tools/prepared-source-backfill.json)、[缺U04时真实拒绝](revisions/r2/tools/missing-u04-backfill-rejection.json)、[作者完整源差分/11标题接收](revisions/r2/accepted-source-reading.json)、[10个U04待接受关联建议](revisions/r2/accepted-u04-proposed-mappings.json)。这是准备证据，不是8批回填完成或新的独立验收。

## 阅读入口

- [主清单](routing-manifest.json)、[Schema](routing-manifest.schema.json)、[静态验证/生成器](routing.py)、[显式修订策略和历史初版档案](routing-policy.json)。
- 逐行明细：[通用内核](views/generic-kernel.md)、[生物](views/creature-rpg.md)、[宝可梦规则](views/pokemon-rules.md)、[战斗](views/combat-requirements.md)、[世界](views/engine-overworld.md)、[界面](views/user-interface.md)、[制作/示例](views/demo-dx.md)、[元数据/旧ID导航](views/metadata.md)。来源事实与未来计划分栏，展示责任、直接依赖及当前有效范围。
- [章节映射](section-coverage.json)、[文档覆盖](coverage.md)、[覆盖汇总](coverage-summary.json)、[验证结果](validation-result.json)。文档/标题/活跃功能/来源元数据为不同分母，实际分母从索引和Git树计算，历史131文档/87WP仅作核对。
- [R2精准返修交接](revisions/r2/README.md)、[12项逐问题映射](revisions/r2/finding-resolution.json)、[28旧FAIL/18activeFAIL/10metaFAIL处置](revisions/r2/feature-resolution.json)、[通过区域保全](revisions/r2/retained-pass-propagation.json)、[源组消费映射](revisions/r2/consumer-mappings.json)、[源章阅读](revisions/r2/source-reading-scope.json)、[73份输入身份](revisions/r2/tools/review-input-ledger.json)、[精确最终工具I/O](revisions/r2/tools/actual-command-io.json)。
- [R1历史返修交接](revisions/r1/README.md)、[44组问题映射](revisions/r1/finding-resolution.json)、[全部721旧行处置](revisions/r1/feature-resolution.json)、[合理PASS传播](revisions/r1/retained-pass-propagation.json)、[新增/退役单元](revisions/r1/new-and-retired-units.json)。
- [97份固定复审输入台账](revisions/r1/tools/review-input-ledger.json)、[源章定向阅读](revisions/r1/source-reading-scope.json)、[依赖校准](revisions/r1/dependency-calibration.json)、[元数据依赖](revisions/r1/metadata-dependencies.json)、[工具真实I/O](revisions/r1/tools/actual-command-io.json)、[24项负例](revisions/r1/tools/actual-results.json)。
- [交接状态](handoff.json)、[接受事件](accepted-source-updates.json)、[回填合同](backfill-contract.json)、[待验证边界](unresolved-boundaries.json)、[独立复审合同](review-prompt.md)、[候选文件身份](candidate-file-manifest.json)。

## 数据和状态规则

五类去向为框架实现、Showdown承担、框架与Showdown协作、MZ接入与表现重建、不纳入目标。名称表示承载假设；去向验证、实现完成、目标验收和阶段批准分别登记。当前目标兼容未验证、四类原型未运行，首版细项未全面批准。相同公式/数值、正式来源引文或来源静态PASS均不能证明Showdown行为覆盖。

v2中`features`只含活跃功能；`retired_features`保存完整旧行加退役原因/替代关系，`metadata_records`保存纯责任、来源、静态向量和证据边界，均不另计实现功能。旧ID永久保留，新增或拆分只追加ID；不能因标题/排序漂移重编号，也不把元数据塞入“不纳入目标”。

`source`是首次固定的提交/文档/锚点/范围/内容身份；`current_applicability`是接受后继后的当前适用定位。旧source对象不变，当前行为范围由`functional_scope`表达：父范围排除新子source，活跃范围不重叠。纯来源或标题不得留成空壳功能。章节覆盖也保留metadata_refs和retired_feature_refs导航。

`dependencies.wp_refs`保留旧WP计划索引来源；`document_wp_refs`仅为来源文档归属，不能冒称完整语义依赖。`direct_refs`指固定正式合同/具名交界，具体用途见reason；强制前置、共享合同、领域消费者和排除性对照阅读应按实际源文理解。特别是Duel读取WP19/27用来排除生物伤害/库存规则套用，并未新增此类结算。WP77是来源证据索引，其明列依赖另作元数据导航。

捕获、背包战斗道具、逃跑、战中成长绑定四类协作原型。清单明确持久个体/库存、战斗临时状态、随机/记录、UI/宿主消费及异常前缀职责，仍待固定目标Showdown commit/格式后验证。AI策略/偏好常量与实时规则查询、共享准备字段及真实登记分别核对，不能假设目标自带同一AI。

Shadow、设施、独立活动、调试/编辑工具、XP工程/旧格式支持及实现阶段保持用户范围门。只有用户明确决定可支持“不纳入目标”；首版暂缓不等于排除。独立活动规则权威与会话/资源由框架候选拥有，MZ承担具体输入/表现。

## 阅读与核验边界

标题与源身份是全集机械核对；返修读取全部域报告和逐功能裁定，正文为问题源章、混合表格及显式依赖的定向阅读，不声称所有正式全文逐句语义复审。R1档案保留原227 FAIL/46待查及合理448 PASS的具体处置；R2针对独立R1剩12项，逐28旧FAIL、18activeFAIL、10metaFAIL处理，并保留35个通过旧组、693个旧ID PASS整行、47个R1新增整行与22个通过元数据整行。以上是作者处置/保全证据，未由作者宣布独立PASS或CLOSED。

工具只分析Markdown/JSON/Git，核对schema、完整Git身份、当前定位、标题、批次/事件、稳定ID/归档、有效范围、依赖和生成一致性。已记录的当前908阶段7命令全部exit0且输入hash稳定：27项结构负例、9项自检、2项导航负例、11份生成物一致及12项保全检查；显式导航覆盖36个父行/39个子行/39条边。首次freeze的5项结构错误和修后记录均保留。这些检查只验证工具约束，不运行业务向量、Ruby、参考游戏、宿主、Showdown原型或未来框架。

上游接受与目标去向验证分开。父任务收到正式U02/U03 ACCEPTED回执后唯一负责回填；实际payload为`908273093e1f6b27fc58249417675dd62d146224`，正式回执在`861f7a44a6f763c265a11761ab17a8ec3b55f304:review/remediation-eighth-20261016-prepare/acceptance/U02-U03/receipt.json`。当前适用正式子树为`6ae817df5b11eafdec671214b0d04e542ad364bc`，131份观察文档身份已核对；17个相关活跃行完成回执核对，直接文本变化为FR-000403和FR-000588。191个有批次绑定的活跃行中其余174个继续待核对，上游全部CLOSED未确认。每个当前定位另存当前anchor/ranges/unit/file身份，保留原历史source。具体回填证据见[父任务记录](revisions/r1/tools/accepted-backfill-result.json)。

根AGENTS和用户[clean-document-revision技能](../../../review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md)适用。配置创建请求与有效执行telemetry逐字段分开，无权威echo的字段仍为UNVERIFIED。新固定候选由父任务另建gpt-6.1-sol ultra/default真正非作者复审。

## 命令

从仓库根执行，需Python和jsonschema：

```bash
python planning/implementation-routing/r8-20261017/routing.py validate
python planning/implementation-routing/r8-20261017/routing.py self-test
python planning/implementation-routing/r8-20261017/routing.py render
python planning/implementation-routing/r8-20261017/routing.py check-generated
python planning/implementation-routing/r8-20261017/routing.py assess-current --commit <精确payload提交>
```

validate与assess-current只读；check-generated在临时目录重建并逐字节比较；render更新视图/汇总；self-test只写工具负例结果。seed入口永久拒绝重建，初版算法仅保存在d62历史。R1显式数据迁移脚本为历史返修证据，接受回填后不能重跑覆盖当前适用状态。R2显式脚本只从固定5666原字节输入定点迁移，遇到当前文件不同即拒绝覆盖；routing-policy保留R1显式策略/初版历史，不充当R2去向重建器。

新后继入口为`revisions/r2/tools/backfill-accepted-sources.py`与`current-section-coverage.schema.json`。prepare只写独立准备证据；apply须完整固定接受输入与显式当前章节映射，现有缺U04会拒绝并保留核心。新增接受绑定/全源覆盖工具不等于已运行完整源切换验收。

最终阶段工具记录为`r2-fixed-source`：当前908上的7命令全部exit0，13个登记输入hash全程稳定；27结构负例、9自检、2导航负例、11生成物一致、12保全检查通过。后继source prepare成功、apply被6个未接受源guard拒绝且核心三文件hash未变；5个接受扩展fixture与完整current全量检查明确`NOT_EXECUTED_AWAITING_U04`。这些后继未运行项不包含在当前阶段通过数中，真实I/O见[来源准备记录](revisions/r2/tools/accepted-preparation-command-io.json)。
