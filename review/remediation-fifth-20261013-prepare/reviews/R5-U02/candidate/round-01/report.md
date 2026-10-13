# R5-U02 非作者独立候选复审 · round-01

**本批候选裁决：FAIL（12 项限定 PASS、2 项 FAIL）。** 46 条冻结 mandatory static 中 45 条 PASS、1 条 FAIL；另有 M03-007 的生产者→消费者一致性 FAIL。载荷完整性与独立补丁重放 PASS 不能抵销语义缺口。

本报告只签固定候选的限定范围。R5-U01 **实际接受依赖仍 WAIT**；没有 actual 审查签名、正式接受或 CLOSED，不把本轮复审计作新批次。返修后只定向重审两项受影响载荷；内容若随后随上游改变，再复核其实际字节。

## 固定身份与独立性

| 输入 | commit | tree |
| --- | --- | --- |
| 冻结合同 | `22fba7786b0090a1955ce6211315b0036cddfbcd` | `21f3484d167d8cab7a288e0204c72f275414d52e` |
| B5 正式基线 | `9366d9d17aaeac3b4414236468affa650fb3dd27` | `594e65edcb192a19110540245fc1663bae2de007` |
| 候选 | `62f1689c6fe787abdbdf4b41dcd1597c36314760` | `c2f74a4fe1063dbe2b17b0bf10d3f5f92b58e819` |
| 作者证据 | `bd38d2e67c1e5b633f620aa557116411ef23aae4` | `12fb3122d46bd5990d68247b133eb42fc1ca372d` |
| 只读参考 R | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | `7589c800b61ba13a13040ed0d686979b80a84fd0`（冻结合同绑定） |

本次审者任务 `/root`，由独立 Codex delegation 启动；源线程 `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`，在本次调用中未参与作者修订。四个非作者分审任务分别核事件/身份、移动/钓鱼、树果/消去/地牢和载荷/重放；主审重新核定两个 FAIL、共享消费者与精确历史关系。请求参数为 `gpt-6.1-sol / ultra / default（普速，禁 Fast）`；实际模型、推理档与服务档未回显，均记 **UNVERIFIED**，没有额度或认证审计。

读取冻结 `reviewer-entry.md`、本批四份 JSON 合同及仓库 `AGENTS.md`。可访问的 `.agents` 为空；未发现适用本次仓库审查的本地技能。仅写本独立 review 域；报告分支为 `codex/r5-u02-independent-review-20261013`。

## 逐项裁决

| 必修 ID | 候选裁决 | mandatory static | 独立核验结果 |
| --- | --- | --- | --- |
| GR5-JXN-001 | **FAIL** | 5 PASS / 1 FAIL | 地图原名/译文/基本名、别名、预览与显式保存正文支持；NAME02/07 的共同前提与分支前提冲突 |
| GR5-M03-001 | PASS | 2 PASS | 页切换/路线41的原始方向与图案改变门、同页早退、返回观察点一致 |
| GR5-M03-002 | PASS | 2 PASS | 绑定图私有键与当前图角色键分列，驻留连接与主解释器/跟随例外齐全 |
| GR5-M03-003 | PASS | 2 PASS | 秒式严格大于、日式余数、本地分量、登记顺序及持久A/tempA分离 |
| GR5-M03-004 | PASS | 3 PASS | 强制路线同步安装、覆盖/原路线、有效新页/同页/无页、频率门与空路线悬置保留 |
| GR5-M03-005 | PASS | 2 PASS | 玩家继承对角位移与距离/四向独有副作用分离，失败/固定方向/四向与非零跳对照齐全 |
| GR5-M03-006 | PASS | 2 PASS | 直接零偏移跳旁路占格门，非零阻挡跳与前后包装0对照保留 |
| GR5-M03-007 | **FAIL** | 3 PASS | 开始/结束公共事件的两个接收者与 FS14/16 限定正确；成功返回值的战斗统计/遭遇消费者仍被泛化 |
| GR5-M03-008 | PASS | 3 PASS | 严格双端许可、普通移动许可、计数/快照/等待顺序及部分提交分列 |
| GR5-M03-009 | PASS | 3 PASS | 202直接/变量/交换、缺主/缺副、战斗跳过和最终转向守卫一致 |
| GR5-M03-010 | PASS | 3 PASS | s:页/公共并行/111/公共自动运行四消费者、nil与true/false对照一致，IM16–18保留 |
| GR5-M03-011 | PASS | 3 PASS | CHERIBERRY 3h、新机制4+4、确认窗口微更新、拒摘/满包/旧数量确认边界一致 |
| GR5-M03-012 | PASS | 3 PASS | 355独立辅助的双推进与116让出对照，缺事件/碎除正常返回和当前图记录门一致 |
| GR5-M03-013 | PASS | 9 PASS | 34/136 各8个有序条件及所有局部输出/子分支逐条匹配；上层重算读层、void与首命中齐全 |

全部 criterion 的原文、候选锚点、源锚点和逐条理由见 [criterion-results.json](criterion-results.json)。静态支持限定在给定前提；正常、失败、取消、部分提交及消费者链分别记录，没有把作者覆盖表或旧 PASS 当批准依据。

## 最小可操作返修

**1. GR5-JXN-001：修正 NAME02/NAME07 的分支前提，保持正确正文。** `author/fragments/deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md.md` 第71行 NAME02 在共同前提要求大写 PN 后又要求无大写占位的 Town；第75行 NAME07 在共同前提要求“可变合法文本；查找与替换正常”后又要求查询前类型/结构失败。`author/derived-vectors.json` 的同名记录也存在相同冲突。必须为这些独立分支明确自己的前提：Town 分支不要求含大写占位；失败分支排除成功查找前提，并明确失败发生在替换之前。无需为异常文本扩大必修范围或新增行为执行。

同步 `derived-vectors.json`、相应 `edits.json` 载荷、共享测试片段、`formal-diff.patch`、片段/候选清单及受影响映射身份；主成功 NAME01/05、正确的 WP11/WP08/WP65 正文可保留。本项 static/3 FAIL；其余5条正文/主例验收支持，不对整项转签 PASS。

**2. GR5-M03-007：把成功结果与消费该结果的入口分开。** 候选镜像 `author/formal/deliverables/final-specification-set/engine-overworld/wp60-fishing.md` 第62/64、84、100/101行仍给出无入口限定的“钓到→fishing_battles＋1＋遭遇请求”。第30、72/76行已纳入非战斗解释器直接调用等待循环，因而读者可把上述消费规则错误用于该新增入口。

固定 R 的 `005_Overworld_Fishing.rb` 30–70 只写 fishing_count、执行等待/清理并返回结果；`002_Item_Effects.rb` 276–314 的普通鱼竿回调才在 true 后写 fishing_battles 并请求遭遇。仅直接 `pbFishing(true, 1)` 正常钓到并返回 true，且无额外公共事件/脚本写入时，不经过这些回调，不自动增加 battles 或请求遭遇。这是本项新增接收上下文的反向消费者检查，没有重开旧物品向量。

在 WP60 §5/§7/§8 明确 battles/request 由普通物品/快捷回调消费 true 后提交；直接等待调用只返回结果，后续由调用方另行消费。增加一个具名静态对照：正常直接成功时 count＋1、battles不变、遭遇请求0，对照普通物品成功时 battles＋1、请求一次。保留 FS14/16 的普通物品结果与 R5-FS01–03 的演出分流。同步正文镜像、共享测试片段、派生向量、编辑/补丁及清单身份。本项3条 mandatory static PASS，但全项消费者一致性 FAIL。

## 独立载荷、重放、共享合同与旧回归

独立读取实际 Git 对象；候选父提交→候选仅新增22个作者载荷，候选→作者证据仅新增9文件，原22个候选载荷全部未变。未执行作者的 rebuild/validate 脚本作为批准依据。

自行按 B5 完整字节和66个精确 before/after 锚点重构16个目标；8份独占镜像、8共享目标的16片段、候选清单、补丁完整字节一致。在隔离临时仓库运行 `git apply --index --check`、重放和 `git diff --cached --check`，均退出0，重放后16个目标与独立投影逐字节相等。286项工具检查全 PASS；详见 [independent-validation.json](independent-validation.json)。投影只供审查，不是正式整合。

直接反查原证据、反例与当前候选；9个共享主条款按 producer→write→consumer→display→persistence/failure 逐一核定，尤其地图名、事件身份、步进和微更新。电话/漫游/通用消息/元数据编辑消费者直接定向读源及 B5；无需把 WP73-B 已保存/共享嵌套取消合同重开或重复整套地图名算法。

14项的历史关系、36个精确旧控制/贡献 pointer 与 owner 只复用身份和限定范围。1164条旧测试目录行保持原字节；MV24、DG10、DG38、FS14、FS16、BP13、载入面板T02的7条修订逐条核语义，原有限正确结果在新入口/时间前提下保留。GR3-M03-004、GR4-M03-003、GR4-M02-001 的既有控制没有改状态或转签；其他主题相近控制未猜配、未重开。详见 [regression-results.json](regression-results.json) 与 [source-reading-log.json](source-reading-log.json)。

## 执行与接受边界

| 分栏 | 行为执行记录 |
| --- | --- |
| R4 历史 | 4；复用既有身份/导航，未重跑 |
| R5 全局 review 历史 | 4个 EXECUTED_REFERENCE 记录；不等同case/进程数；模型、原生宿主、Demo为0 |
| 本 update / 本候选复审新增 | 参考、模型、原生宿主、Demo均0 |

73个作者向量及本报告的消费者对照为 **DERIVED_VECTOR / NOT_EXECUTED**；格式、hash、清单和补丁命令为 **TOOL_VALIDATION**。没有真实地图/CommonEvents/媒体、原生宿主或无界插件组合 PASS；地牢局部正常不证明全图连通、终止或摆放成功。

optional7、no-required7、政策6及 M11-005 optional方面继续隔离。报告仅写独立 review 域，未改作者、正式文件、公共登记、参考或冻结历史，未 merge main、未操作 Mac、未重开全局 review。该分支只普通推送报告；发布 commit/tree 和全部6个新增文件的精确远端读回由提交后的外部回执绑定，manifest 不自引用。
