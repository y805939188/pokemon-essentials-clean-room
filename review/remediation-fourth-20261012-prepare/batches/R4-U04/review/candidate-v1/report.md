# R4-U04 独立候选审查

结论：**GR4-M05-001 — PASS（CANDIDATE_PASS_SCOPED）**。固定候选已满足本项四条验收；未发现需要整改的语义、数学、状态、边界或写域问题。此结论仅绑定以下候选，不登记 ACCEPTED_SCOPED／CLOSED，也不代表 actual、整轮、历史全域或运行通过。

| 身份 | 精确绑定 |
| --- | --- |
| 候选 commit | `1c2cdcbe6509839a19fd3c48c8a412a6c19e161a` |
| 候选 tree | `fcd0cff8a0830b7e3a8860f8e84c55c5bb793ec3` |
| 合同／候选 parent | `08a57fb55118914a74ac1ffaf617647c01df8938` |
| 正式 B | `1f36475d22120a0d1175967d5b17d71fe8311d88` / `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a` |
| 参考 R | `Maruno17/pokemon-essentials`，`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 作者证据后继 | `53edd67b69d3641de3d748ceb1bfeb847f621f6a` / `69d4088db4c03b490d8e0dcd1a19b76dd91d86a1`；仅增加发布回执，不作为候选 |
| 准备冻结回执 | `2b60c7bd0dce8d972e34a9d86a8f6cf6a3b1dd65`，根 freeze-and-publication.json |

审者任务 `/root`，真实环境提供的 thread ID `01a130d5-fcbe-7506-9573-e758528ad023`；父源线程 `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`。审者未参与作者候选写作、未代修作者文件、未运行会写 author/validation.json 的作者脚本。请求 gpt-6.1-sol / ultra / default / Fast=false；实际模型、effort、tier、Fast 回显 **UNVERIFIED**。辅助只读任务 `/root/source_eligibility` 与 `/root/consumers_regression` 的结论由本审者核对、裁决，不转作作者自签或替代 actual。

审查在独立工作树 `/workspace/r4-u04-independent-review`、普通分支 `review/r4-u04-independent-candidate-20261012` 完成。分支从证据后继起步以保留作者证据，所有审查均对精确候选 Git 对象取值。固定合同优先于入口中“尚无候选”的准备阶段文字，用户本次已明确给出冻结候选与审查授权。本报告新增写域仅为本批 `review/candidate-v1/`；正式文件、作者文件、公共登记和 main 均未改。

## 验收结果

| 项 | 合同要求 | 结果与证据 |
| --- | --- | --- |
| 1 | 五种主动 PP 物品的战斗非蛋且 HP>0 门，场外无存活门；不扩大至所有物品 | **PASS**。候选 WP28 L204–212 独立列 ETHER、MAXETHER、LEPPABERRY、ELIXIR、MAXELIXIR 的资格和量值。R 的 Item_BattleEffects L155–186 明确两族存活门及全部别名；Pokemon L264–270 解释可战斗。场外 Item_Effects L632–684 与 Item_Utilities L774–775 没有 HP>0 门；WP28 保留复活等原规则。 |
| 2 | 夹具唯一推出战斗库存1／PP0／HP0，场外库存0／PP10／HP0；MAX 和别名量值明确 | **PASS**。WP28 L208–216、目录 L108–114 的 PP01／02 给出完整独立重置前提。CommandPhase L110–133 在资格后才登记；ActionUseItem L34–59 扣减发生于登记。Item_Utilities L367–382 恢复 PP 封顶且不改 HP，L644–690 场外效果成功后扣减；MAX 两种回满35，主动 LEPPABERRY 与 ETHER 同量。 |
| 3 | 存活、满 PP、取消对照；WP20／WP40／WP67-A 无冲突；AI 与被动 LEPPA 分开 | **PASS**。目录 PP03–07（L114–120）分别覆盖 HP1、PP满、选招取消、30→35 封顶及多槽，WP28 L214–219 保留执行复检、退款残留和同步。ChooseCommands L239–285 支持非蛋成员选招及拒绝／取消回成员循环；WP20 §5.4–5.5、WP40 §4.2／4.2.1、WP67-A §5.2–5.3.1 均能消费新资格。WP51 缺索引 AI 与 WP50 持有 LEPPABERRY 不被新表覆盖。 |
| 4 | 不要求运行；静态向量标 NOT_EXECUTED，不能签运行通过 | **PASS（证据边界满足）**。WP28 L216、目录 L108、作者 execution.json 均明确 NOT_EXECUTED。本审查也无参考／模型／宿主行为执行，脚本只作 TOOL_VALIDATION。历史4次隔离调用未改写为本次 PP 向量通过。 |

逐项机器可读结果在 criteria-results.json 与 findings.json；精确文件 bytes／SHA256／Git blob、完整读取层次在 identity.json、read-ledger.json。所有行号按上表固定 commit 解读。

## 有效独立质疑与状态推导

审查主动尝试用现有通用门、底层恢复辅助、AI／被动消费者推翻新增资格差异。结果是：通用战斗门处理蛋、查封和 Hyper，场外通用门处理蛋／Hyper；两者均不能替代 PP 家族的战斗存活门。非蛋濒死成员可先进入选招，故本项拒绝发生在提交后的资格阶段，不应改写成 UI 预先过滤全部濒死者。源注册／复制／覆写检索未找到固定默认规则的反向覆盖。正式集具名与中文 PP／濒死检索也没有另一个条款使场外恢复自动要求存活。

在合法夹具中，单槽总 PP 为35、初始0，10点补给的实际增量为 min(10,35−0)=10；初始30的实际增量为 min(10,35−30)=5；回满增量为35−当前值。全招两种按每槽分别求增量，以至少一个槽有正增量为成功。PP07 的三个同标识槽通过 WP20 的招标识赋值边界成立，不把常规学习去重当作所有列表状态的全局不变量；ELIXIR 输出 [35,10,35]，MAXELIXIR 输出 [35,35,35]。这些计算为 DERIVED_VECTOR，没有执行该公式模型或参考函数。

HP0 战斗分支在资格阶段返回拒绝，尚无本次登记，因此库存保持1，也不存在该次执行退款或身份残留。HP0 场外分支先通过普通非蛋／非Hyper门，恢复成功后库存1→0，HP仍0。只改 HP1 的正常分支在战斗登记时扣1，执行前资格保持且效果正常返回才恢复并清物品消费身份；未把这个条件正常例覆盖到中途变化、异常回调或退款分支。满 PP 和取消均发生于成功登记／成功效果之前，库存保持1。

单招总 PP≤0 的旧 IU-07 失败与 PPUP／PPMAX 的总 PP≤1／提升计数3边界保持；恢复 PP、成长 PP 和复活仍各有入口资格。未穷举非法 PP 超上限字段、全部第三方插件及世代替换，也没有以这些合同外状态制造本批返工。

## 写域、消费者和有限历史回归

独立 validate-inputs.py 已实际运行并得到 `PASS_INTEGRITY_SCOPE_AND_PRESERVATION_ONLY`：固定 T→候选共12个变化路径，恰为2个允许正式文件和10个本批作者证据；候选→证据后继仅增加 author/candidate-publication.json。完整12个候选 blob 与发布回执一致，任务包完整文件与准备冻结回执一致，根 finding 与固定最终第四 review 同一记录。

正式集131文件中其余129文件与 B 完整字节一致。将 WP28 本次 PP 段和 LEPPABERRY 身份行精确还原，可得到完整 B 原文；将目录新 PP 段和 IU-07 精确还原，同样得到完整 B 原文。因此探测仪 §3.3-R01、治疗／复活 §5.1、PPUP／PPMAX 与原同步、§3.5–3.5.1 退款残留、旧 IU／U03-IF／U04-RF 等条款保持。这里的字节保留证明只证明未改，相关消费者的语义一致另由实际读取确认。

GR3-M05-001（尺寸）仍为未改变文件的限定历史复用；GR3-M05-002（探测仪）和 GR3-M07-001（退款残留）完成受影响保留与交界静态核对，未重开、未补签运行／全历史 PASS。旧229／341在本批没有选定直接原项，保留原身份和 qualified scope，状态为 `historical_qualified_evidence_reused/not_reexecuted`。WP35／EG-13／20、WP34 正确3／5继承与同 Power 一次计数、交付导航及原报告不在变化路径。

本候选只含 B 的 WP67-A 消费者；未读取或认可 U03 的浮动候选。后续唯一登记员按 U01→U05 整合并冻结 actual 后，同一审者须重新读取实际 WP67-A、完整字节、差异和共享消费，核取消选招回成员、成员拒绝留循环与登记前无库存变化。该门仍 PENDING；候选 PASS 不能转授 actual PASS、ACCEPTED_SCOPED 或 CLOSED，最终关闭另属 U06。

## 实际执行与发布边界

本次新增行为执行：**EXECUTED_REFERENCE=0、EXECUTED_MODEL=0、EXECUTED_HOST_OR_DEMO=0；NOT_EXECUTED_THIS_UPDATE**。执行的 Python/Git 身份、JSON、写域、表格、完整字节保留检查仅 TOOL_VALIDATION。源读取只用固定 R Git 对象；随包旧本地参考路径不在当前环境，因此取入独立只读对象仓库，没有改参考内容或真实数据。

固定第四 review execution-evidence.json 保留4次历史隔离原函数执行：M01 本地化1次、M02 HTTP／计时2次、M12评级结算1次，均有初始化／替身和限定范围；M05 原模块本来没有行为执行。它们不证明本批 PP 菜单、联网、媒体、动画、地图、存档或宿主通过。完整 Demo／兼容宿主与全部资源未建立；这些限制不阻塞本合同的静态事实修订。

发布采用普通 push 本独立分支，fresh fetch 到全新对象仓库后逐文件读回完整报告和候选输入。后继 publication.json 绑定报告 commit／tree 和完整读回结果，避免报告自嵌自身身份；其最终发布身份另由返回值提供。

候选必修阻塞：**无**。尚待执行的阶段：唯一登记员 actual 整合冻结、本审者实际复审与 U06；本报告没有替这些阶段登记通过。
