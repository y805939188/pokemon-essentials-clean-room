# R4-U04 作者候选说明

状态：AUTHOR_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW。唯一主责为 GR4-M05-001（GR4-CAP-M05-017）；本文件不是独立 PASS、实际接受或关闭登记。

作者真实 thread/task ID：`01a130c4-45c5-73ea-ba46-bedd143fb03a`；平台角色 `/root`；源父线程 `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`。用户请求 gpt-6.1-sol / xhigh / default / Fast=false，实际参数回显 UNVERIFIED；没有模型替换、Fast 或额度/凭据/后端审计。

## 固定输入与范围

作者在独立工作树 `/workspace/r4-u04-author`、独立普通分支 `remediation-fourth-20261012-r4-u04-author` 工作。固定作者起点/任务包为 `08a57fb55118914a74ac1ffaf617647c01df8938`，tree `8fc388710e3433890416f6d01247fd09df9d2ea8`。通过精确后继 `2b60c7bd0dce8d972e34a9d86a8f6cf6a3b1dd65` 的根 freeze-and-publication.json 核验这些身份；未用浮动分支替代作者输入。

正式 B：`1f36475d22120a0d1175967d5b17d71fe8311d88` / `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`。第四 review 最终：`130452d902530140331c21064a3188b7887f72ae` / `b2677e819a85422c353bd3eac3ff55409698d5d8`。参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `7589c800b61ba13a13040ed0d686979b80a84fd0`；因随包本地路径不存在，自行 fetch 到 `/tmp/r4-u04-reference.git` 只读取证，未改任何既有 reference 或用户数据。

已完整读取本批 author、batch-contract、read-scope、findings-input、handoff-findings、launch-contract、legacy-navigation 和 reviewer 入口；根三份准备 JSON 完整解析，按本批锚点核对完整 bytes/SHA256/blob。适用根 AGENTS.md 要求行为规格、源分离及架构中立；允许写域祖先未发现额外 AGENTS.md。未使用额外技能，因为这是已授权的仓库事实规格修订，不是独立 Library、Page 或引擎开发任务。

正式仅修改：

1. `deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md`：§4 将 LEPPA 样本身份明确为 LEPPABERRY；§5.2 补五物品的战斗/非战斗资格、量值和主动入口边界。战斗目标需非蛋且 HP>0，拒绝发生在登记扣减之前；场外无该存活门，恢复 PP 不改 HP。
2. `deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md`：精确化 IU-07 的上下文前提，增加 R4-U04-PP01–PP07 静态向量（濒死战斗/场外、存活、满 PP、取消、封顶、多槽）。

其余写入全部在本 author 证据目录。公共 traceability/共享文件只交 `shared-proposals.md`，不改全球台账、其它批、reviewer 目录、main、reference、旧报告或交付导航。

## 作者静态验收

四条原验收完整保存在 acceptance.json 并映射到正式条款、源依据和向量。前三条作者结论为 AUTHOR_STATIC_CHECK_SATISFIED；第四条运行边界为 NOT_EXECUTED_THIS_UPDATE。没有行为模型或参考函数执行，也没有宿主/UI 演出通过。

最小反例以普通内部战斗、可行动 A、非場上普通濒死 B（HP0/100，TACKLE0/35，库存1）为前提：人工确认后 PP 家族资格拒绝，尚无本次 UseItem，留成员选择，库存1/PP0/HP0。独立重置同字段，从场外背包确认 ETHER：PP10/35、HP0/100，效果成功后库存0。MAXETHER/MAXELIXIR 回满35，主动 LEPPABERRY 与 ETHER 同量，ELIXIR 逐招+10封顶。只改HP1时两上下文正常；已满和取消不消费。

源链已读菜单提交、通用门、PP 家族/别名、登记扣减、恢复辅助/场外成功扣减以及默认物品与 TACKLE 数据。必要补充 caller `006_Battle_ActionUseItem.rb` 只读取证：通用门没有濒死总拒绝，真正战斗存活门来自 PP 家族，登记才扣减。此序不意味着 UI 先过滤所有濒死成员；非蛋目标仍可进入选招，然后提交被拒。

## 反证与有限回归

已对固定 B 全正式集作具名 PP/濒死及别名查询，并对固定 R 脚本作注册/覆写反查；结果、覆盖数量和命中路径/行号在 counterevidence.json，未保存源代码片段。WP20 的恢复辅助/同步不替代使用资格；WP40 登记和 WP67-A 拒绝返回均已有指向 WP28 的消费合同，本批只补生产者条款，无需越域复制规则。WP51 缺索引 AI 异常、WP50 被动 LEPPABERRY 的 RIPEN/选槽/消费属于其它入口，不用本批人工有效下标覆盖。

WP28 原 §3.3-R01 探测仪、§3.5–3.5.1 登记/退款残留、§5.1 治疗/复活和 §5.2 PPUP/PPMAX/同步行均原字节保留；旧测试除 IU-07 外保持，包含 U03-IF 和旧其它 IU。GR3-M05-001 尺寸无变化，GR3-M05-002 探测仪及 GR3-M07-001 退款身份保持原 CLOSED 的限定历史证据；本轮仅做受影响条款的保留/交界检查，不重新签历史 PASS。旧229/341无本批选定原项，全部仍 historical_qualified_evidence_reused/not_reexecuted，不重启全局 review。

## 执行限制与 reviewer 入口

第四 review 既有4次隔离原参考调用（本地化1、HTTP/计时2、评级结算1）及宿主/Demo NOT_EXECUTED 是固定历史事实；M05 本项原证据本来只有 SOURCE_STATIC/SPEC_STATIC/DERIVED_VECTOR，未借其它域的4次调用为 PP 向量签运行结果。

本次 Python/JSON、Git 身份、allowlist、未改条款重构、链接/表格和远端完整字节核验仅 TOOL_VALIDATION。真实地图/媒体/宿主、按键和菜单演出、插件覆写/世代替换、异常回调不在新运行证据内；这些限制不阻塞本次事实修订。

独立 reviewer 从本批固定 `tasks/R4-U04/reviewer.md` 进入，再读本 report、acceptance/read-ledger/regression/counterevidence/execution 和候选完整差异。作者冻结身份由后继 `candidate-publication.json` 绑定，避免候选自嵌自身 commit。父任务安排 reviewer；作者没有自调度或自签。候选通过后仍须唯一登记员按合同整合、冻结 actual 并取得独立实际复核，方能限定接受；最终关闭另属 U06。
