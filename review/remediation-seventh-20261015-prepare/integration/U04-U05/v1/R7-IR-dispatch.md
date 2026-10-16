# 新 R7-IR ultra：U04/U05 实际整合字节独立复审

父会话可用本全文创建新的独立云端审者。请求gpt-6.1-sol ultra、service_tier=default普通速度，禁Fast；有效模型/effort/tier/speed无回参仍UNVERIFIED，不查额度/认证。必须是新的实际context，不能是覆盖作者、候选reviewer或整合者；排除已知外部标识 01a13f52-cc74-7568-9e75-85ac773c6015、01a13f7e-d577-727a-9565-f64f6a663024、01a13f52-ecf8-73f9-8c9b-f5c164f0c017、01a13f7e-f6bd-737a-9530-318764196012。U04作者内部context未暴露的资格保留，不伪造匹配；父会话需实际创建不同cloud thread并回报真实ID。不要创建子任务或自己担任作者，不自行接受/关闭。

仓库https://github.com/y805939188/pokemon-essentials-clean-room.git，整合分支codex/remediation-seventh-20261015-cloud。
实际整合commit **b0eea808887a688d52d28390ac8886fed9c10bcf**，workspace tree **73ad4ff20527d4bdcf27d55fc17932a232e2f912**，正式131份子树 **dcb3f744d78fa5c4c62994de5e4cf6eb1f886d3b**。
实际输入冻结commit **d9021aa2d704476f644ef15f1a3b8291653ff8f1**，tree **7efe118d11965ea842b5522cfa9dd7a8c7842d2d**。
完整输入精确路径 **review/remediation-seventh-20261015-prepare/integration/U04-U05/v1/integrated-input.json**。
两份运输清单：该冻结commit下 **review/remediation-seventh-20261015-prepare/integration/U04-U05/v1/integrated-restore/R7-U04.json** 和 **review/remediation-seventh-20261015-prepare/integration/U04-U05/v1/integrated-restore/R7-U05.json**。
真实按条款应用记录及实际diff位于实际整合commit的 **review/remediation-seventh-20261015-prepare/integration/U04-U05/v1/applied-clauses.json** 和 **actual-changes.patch**。
所有固定文件可从 `https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/<完整commit>/<精确路径>` 获取，不能用浮动HEAD或作者镜像替代实际整合字节。

本次仅覆盖三项required：GR7-M03-001、GR7-M03-002（U04），GR7-M07-002（U05）。实际5个正式文件、11个变更片段；root对B的全部正式差异恰为这5份。U01旧r1 J01失败已保留，旧U01和未审返修a3938bbb均未整合；不把旧M01候选PASS移作当前批准。未覆盖其它24项或其它批次，分母始终27项/13批。

必须取得并完整阅读：原两批f622356f3beb9e84ea8cff9db07c7fb382565d3f下 review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U04.json、R7-U05.json；原七组、独立反证及所有正确保留/历史回归；各实际候选和作者完整证据；实际候选审者结果U04=3d6fcea6c2d5930c4c299278895077079d7afd28（实际审者01a13f7e-d577-727a-9565-f64f6a663024）、U05=e9e47920ee26ecc87e0aaf02e84ec6f33b5cfed7（实际审者01a13f7e-f6bd-737a-9530-318764196012）；本次MI实际正文/目录、B原文、根逐hunk记录和未改消费者。候选PASS只允许进入整合，本次结果仍待你对实际MI独立复审，不得机械继承候选PASS。

先读实际AGENTS.md及固定恢复工具658488c81f1f3181a488298ab27850c8af951d73下 review/remediation-seventh-20261015-prepare/tools/restore_container_context.py 和recovery/independent-containers.md；不得盲跑下载脚本，不操作Mac，不执行作者/参考/native程序。为两个批次分别取得该658488c8下 recovery/batches/R7-U04.json、R7-U05.json，在本容器新目录恢复固定原合同/源/反证/限制：

```bash
python3 /workspace/r7-ir-bootstrap/tools/restore_container_context.py --plan-directory /workspace/r7-ir-bootstrap/original-plans --batch R7-U04 --destination /workspace/r7-ir-context/U04
python3 /workspace/r7-ir-bootstrap/tools/restore_container_context.py --plan-directory /workspace/r7-ir-bootstrap/original-plans --batch R7-U05 --destination /workspace/r7-ir-context/U05
```

再把本次冻结commit d9021aa2d704476f644ef15f1a3b8291653ff8f1 的两份integrated-restore清单保存到/workspace/r7-ir-bootstrap/actual-plans/，用同一个已读固定工具恢复**实际整合输入**：

```bash
python3 /workspace/r7-ir-bootstrap/tools/restore_container_context.py --plan-directory /workspace/r7-ir-bootstrap/actual-plans --batch R7-U04 --destination /workspace/r7-ir-actual/U04
python3 /workspace/r7-ir-bootstrap/tools/restore_container_context.py --plan-directory /workspace/r7-ir-bootstrap/actual-plans --batch R7-U05 --destination /workspace/r7-ir-actual/U05
```

actual/为MI实际正文，baseline/为B原文，candidate/为原候选，candidate-review/为真实候选独立报告及全部证据，freeze/、integration/、root-reception/为冻结/逐hunk/根接收，unchanged-consumer/为MI内与B相同的必要消费者。它们全是只读具名快照，不是完整参考checkout/运行认证。不共享整合者本地/workspace目录。中断同容器同目录--resume、保留失败/冲突字节，不另起替代任务。原源/反证恢复不能替代实际MI恢复，两批计划都须取得。

先核所有身份和实际MI tree、完整正式diff，后逐项内容审查：
1. U04 WP41/SW对决定3后同扫描非致死延续、外层消费、布局/速度/玩家/入场前提及单席/Yes/已决定/取消/故障前缀；不升级危害致死扩张。WP39/BC的存活偏好与首个既存濒死回退、[3,5,1]、原始查询/投球补救/显式目标三层及无活同伴旧失败，false/默认其它调用和其它目标族保持。
2. U05 WP34仅收紧无条件两槽不写入，既有WP21动态守卫、形态相等/同值显式提交、母系/永石顺序、派生/重算/登记前缀和队满时序；PF01-09全部具名前提、正常/无取消/异常/部分提交及SHELLOS/EG/R4历史对照保持。不扩成所有读取、任意插件或统一回滚。
3. 实际5份正文/目录全文与B、已通过候选逐条比对。11hunk之外字节保持，场景计数/目录/向量和反向消费者准确，未把整个镜像覆盖其它贡献；所有旧正确条款及旧56/92证据保留。当前累计正式差异仅覆盖这两批；U01未整合，optional/policy未采用。
4. 对WP38/WP42/WP47-A和WP21/WP33等必要消费者以及精确历史回归逐条件接收。字节未变只证明未改，不替代语义相容核；源/消费者额外需求按固定R具名补取，未读可读材料不得伪标limit。直接/传递依赖未满足则WAIT相应范围，不以无共享冲突组推断全局依赖满足。

逐必修给 PASS_SCOPED_ACTUAL_INTEGRATION / FAIL / WAIT，绑定实际MI文件、具体条款/前提/反证/向量、源与消费者、候选独立证据和实际接收。不要只看汇总/作者镜像，不以hash、工具退出0或旧PASS替代新内容审查。新增SOURCE_STATIC/DERIVED_VECTOR/TOOL_VALIDATION与真实运行分开；所有行为向量NOT_EXECUTED，完整模型/宿主/Demo/native媒体/真实存档回放0保持，L01-L14及有效配置UNVERIFIED保持。静态限定PASS不认证运行等价。

只写 **review/remediation-seventh-20261015-prepare/integrated-reviews/U04-U05/r1/** 的report.md、per-id.json、review-input-receipt.json、artifact-manifest.json及真实工具证据。在自己隔离checkout从固定B e646432c644dec04d306842cc5a559a29c718fbc创建唯一结果分支 **codex/r7-ir-u04-u05-20261015-r1**，只普通提交/推送该证据目录，不携带/修改实际MI文档、候选/公共台账/main/tag，不force。如同名分支或未发布成果不是本task所有，保护并回报，不换替代分支。返回真实审者task/context、MI/FI实际输入、逐ID结论和未满足依赖、结果commit/tree及全文件远端读回。

你仅给独立实际整合结论，无权登记ACCEPTED/CLOSED。R7-I实际接收你的结果、核原有限合同的精确依赖/回归后，才可分开正式接受与关闭；任何未满足项保持OPEN。不要自行派发新的任务，不把本全文当成任务已创建或实际整合已PASS。
