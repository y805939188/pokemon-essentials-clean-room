# R8-U05 完整独立复审入口

本文件是作者准备的复审输入说明，不是review结论。父任务另建实际非作者 `gpt-6.1-sol / ultra / default` 任务；normal、Fast off。无权威echo的actual配置逐字段UNVERIFIED。禁止以同context改角色名自验。

## 冻结输入与权限

- 仓库：`y805939188/pokemon-essentials-clean-room`，项目 `/workspace/pokemon-essentials-clean-room`。
- 原输入完整SHA：`4575e80d041ab0c74a42e2e36399d05791dbaa5b`。
- 待审提交：使用作者最终交付消息中的真实完整SHA；必须fetch并核验，不以移动分支头代替冻结输入。分支为 `revision/r8-u05-20261017`，最终提交是原输入的普通后继。
- R：`/workspace/pokemon-essentials`，固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只读。
- B8：`fd1df570cad987dc3852a3b958f03916e317f7fe`；语义core：`2460370f1e410bd49cc29e377b89662838aed2b3`。原5caff来源与core恢复位置双身份保留。
- 本次只审候选及其证据；正式目标由R8-INTEGRATOR唯一写。审者使用父任务分配的独占review证据位置，不修改本作者镜像/证据、正式规格、main、旧报告或公共台账。不运行Ruby、不开发框架、不自行切换模型。

## 完整读集

报告根为 `review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/`，候选根为 `review/remediation-eighth-20261016-prepare/candidates/R8-U05/`。

1. 完整读 `AGENTS.md`、报告根 `inputs/review-SKILL.md`、`handoff/batches/R8-U05/prompt.md`、`readset.json`、`reviewer-prompt.md`、`handoff/batch-assignment.json` 中本批完整assignment，以及manifest。最新用户已授权启动并允许按既定标准逐项选择可选项，覆盖旧未启动/全部未选限制；本批无归属optional，不跨批。
2. 完整读 `handoff/contracts.zh.json#/records/22` 和 `#/records/30`，以及 `handoff/accepted-facts-and-mandatory-companions.json`、`history-qualifications.json`、`policy-and-preservation.json` 的共同资格与适用伴件。复审原完整根记录、完整反证及历史接合，不以摘要或身份校验替代语义。
3. 原完整根记录恢复入口：报告根 `evidence/external-recovered/handoff_preparation_cloud/5caff3bd1a1b062b48b7eda46777a614921946f3/audit/received-root-records.json.gz` 的完整记录22/30。当前权威为 `findings.json` 对应完整记录及 `adjudication/root-final-history-and-canonical-reception.v1.json` 对应完整canonical对象/共同资格。原OPEN按时点保留，不冒当当前历史阻塞。
4. 完整读 `adjudication/root-world004-counterreview.json`、`root-cd002-negative-probability-counterreview.v1.json`、`root-cd001-cd002-exact-inputs.v1.json`，以及 `tasks/pbs_world_record_audit/history-final-joins/finite-comparisons.json` 对应接合、`tasks/pbs_creature_current_cloud/mandatory-encounter-trigger-counter-clarification.v1.json`。重置调用者采用完整具名单位，不能把触发返回真当自动重置。
5. 依原readset恢复固定源/正式身份；完整读两份候选及两份原正式正文、共享 `deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md`，并本人完整读所需源文件/完整单位。源包括Settings、WildEncounters、Trainer、Encounter注册、Compiler001/002/003、五份encounters文本；必要caller/Radar/PIDGEY记录及单位范围详见本目录 `reading-ledger.json`。原审者FULL或作者读账不授予审者实读。
6. 完整读作者 `remediation-records.json`、`optional-disposition.json`、`candidate-manifest.json`、`validation.json`、`input-identity-verification.json`、`commands.jsonl`、`tagging-handoff.json` 与本目录说明。作者verify.py只作可检查支持材料，不能替代独立判断；不要在冻结作者输入上运行会改写作者证据的脚本。

## 待区分的行为与累计保留

GR8-WORLD-004：候选WP61 §3.3 应只修本地比较者引用。合法P0非蛋50级HP0/P1非蛋10级健康/野生20/repel真/雷达假/无相关能力时，默认仍拒绝并清累积；换配置false按10放行。健康50、等于50、雷达真、候选空六组控制完整核验。保持WP36 §4.3、严格小于、雷达/能力次序、步进活动快照/递减/续用与GR-011标记消费；允许门通过不等于实际开战。

GR8-EXT-CD-002：候选WP36 §4.2 第5项只限定非负结论并明确向下整数商/负前缀。合法作者 `Land,-1` 与健康普通PIDGEY，正常八次宽限拒绝可达步数8/累加0；随后常规失败到-1，下一次商-1使概率-2、再失败累加-2。对比正概率21及既有21/189/210、Repel真失败后清0、非步进不累加。保持§3.2原接受域、宽限先增步/拒绝不累加、setup保累加与reset清两计数、雷达/快照。不得新增验证/钳零、改算法或声称默认附带地图故障。

作者记录的场景全部是静态推导，NOT_EXECUTED。没有新增正式目录案例的合同要求。两份候选与base的差异应各且仅一处替换，章节标题、行数及其它字节精确相同；检查完整正文的一致性与保留范围，不只看diff。

## 输出与后续门

逐项给实际冻结输入、本人完整实读、反方尝试、修改位置、六控制/负前缀对照、保留情况及结论；注明范围与未决项。正式候选PASS必须来自实际非作者。若发现缺口，返回具体位置/前提/最小要求，由作者另修，不在审查中重写候选。

即使候选PASS，仍需R8-INTEGRATOR正式整合并真实冻结实际结果；随后实际非作者完整核最终受影响整文件及累计保留，再分别登记actual integrated PASS、ACCEPTED、CLOSED。本入口不替父任务创建review，也不提前签任一门。
