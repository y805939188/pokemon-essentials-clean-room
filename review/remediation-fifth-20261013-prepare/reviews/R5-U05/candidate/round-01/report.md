# R5-U05 非作者独立候选复审 — PASS（限定静态候选）

GR5-M09-001：四项标准 C1–C4 全部 PASS；新增 B64–B71 全部通过独立静态推导。未发现本候选内容阻塞。该签名仅绑定本页给定的候选字节，实际整合依赖 R5-U04 仍 WAIT；未审 actual、未授予正式接受或 CLOSED。

| 固定对象 | 身份 |
| --- | --- |
| 合同冻结 | `22fba7786b0090a1955ce6211315b0036cddfbcd` / tree `21f3484d167d8cab7a288e0204c72f275414d52e` |
| 真实作者候选 | `4bdfd36aca3dbfb6ef0c61ef6e7af057acd6820b` / tree `ca2dfe5eefb2ffc021bcc7191baf1f825f0ec219` |
| 作者分支 | `codex/r5-u05-author-candidate-20261013` |
| B5 正式输入 | `9366d9d17aaeac3b4414236468affa650fb3dd27` / 正式131文件子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2` |
| R | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 语义/发布 | `c0ff33024aea424c68d29f9778fe7c8e807d21e8` / `f49d870c6fd616ab6736754a218a4553b5acac7f` |

审者为当前新委派的非作者任务，平台任务路径 `/root`；辅助只读核验任务 `/root/source_semantics`、`/root/consumer_history`。可追溯审查运行标识 `R5-U05-candidate-round-01-1023bf46-031f-4d7d-a26d-498f4e018d07` 是本报告审计标识，并非平台 UUID。平台未暴露全局 task UUID，需父任务角色回执绑定；`/root` 与作者清单的通用路径名不被当成同一全局任务，来源线程 ID 也未冒充审者任务 ID。本审查未撰写或修改作者候选。请求 `gpt-6.1-sol / ultra / default` 普速禁 Fast；实际模型、推理、速度回显仅 `UNVERIFIED`，不因此制造内容阻塞、不审计额度或认证。

已读仓库 AGENTS.md、冻结入口/合同/验收/精确共享与回归读集；仓库 .agents/本地 SKILL.md 不存在、工作区 .agents 空、executor skills 列表空。按冻结合同只写本 review 域。全部12份真实作者载荷完整身份、两份镜像、必要固定源与 B5 主文/附表/测试/共享条款和原反证身份见 [review-manifest.json](review-manifest.json)、[source-reading-log.json](source-reading-log.json)。原证据采用单文件定向取得，未重下全仓或开启新全局 review。

| 标准 | 裁决 | 独立依据 |
| --- | --- | --- |
| C1 独立评分守卫与预测门分列 | PASS | 候选 WP52-B119行先给独立可恢复守卫，拒绝时保留 s；R 两个独立登记与 ChooseMove 的 PredictMoveFailure/ScoreMoves 分门一致，HPAware 在资格后。 |
| C2 必需正常、边界与封锁对照 | PASS | 合法训练家 SkillLevel/Flags 的实际消费者到普通候选入口可追溯；满血、50%、75%、预测开、受封锁盟友与自身封锁分别对上 B64/B65/B66/B68/B67/B71。 |
| C3 评分/HP意识关闭及阶段边界 | PASS | B69不进入评分体，B70守卫通过但比例分关闭；局部不提交HP/状态/PP/物品/行动，通用修正、合成及权重仍由原主合同消费。 |
| C4 收窄过强断言 | PASS | 作者回应与候选证据限定为旧表允许导出95、不能唯一复现100；没有“所有实现者必减5”或最终选错断言。 |

| 向量 | 静态裁决与观察阶段 |
| --- | --- |
| B64 | PASS：满HP、预测关；普通入口可达，局部守卫保留100，跳过减5。 |
| B65 | PASS：50/100可恢复；100＋⌊15×50/100⌋＝107，HP仍50。 |
| B66 | PASS：75/100可恢复；3/4等号落在减5分支，局部95。 |
| B67 | PASS：双打未封锁U、存活受封锁盟友T；同侧枚举不滤其HealBlock，独立守卫保留100。 |
| B68 | PASS：满HP仅恢复预测；目标预测−1，评分体NOT_ENTERED；无有效目标的后续整体处理保留原合同。 |
| B69 | PASS：仅AntiScoreMoves；本体NOT_ENTERED，目标基准100不经过本体。 |
| B70 | PASS：可恢复、仅AntiHPAware；局部保持100。 |
| B71 | PASS：U自身封锁；治疗招在可选资格阶段先拒，本体NOT_ENTERED。普通倒下目标也被存活枚举排除，只保留资格定义。 |

全部向量均为 DERIVED_VECTOR，未执行参考或评分模型。直接核 R 的 Healing231–249、AI ChooseMove23–83/175–323、AITrainer28–100、TrainerType及Trainer配置消费者、canHeal资格、目标数据与普通选择门；满血不是选择资格拒绝条件，默认LIFEDEW为同侧多目标，普通路径确实消费目标评分。真实整招“无人可治”失败属于执行层，不自动成为AI整招预测。无新实质质疑要求作者回应。

补丁以 B5 正式路径在隔离临时目录独立 `git apply --check --whitespace=error-all` 后重放，两个完整文件逐字节等同候选镜像。正文只改119行的LIFEDEW规则和234行目录；测试新增共同夹具及B64–B71，BE67→75，原254条表行全部按完整UTF-8行保留。候选正式131文件子树、冻结contracts/frozen-input及公共registration不变。工具通过只证明格式/字节/重放，不代替上表语义裁决。

共享与消费者仅签本项投影：COMBAT-AI-EVALUATION主责M09（原shared `/contracts/74`），COMBAT-EFFECT-RESOLUTION主责M08（`/contracts/9`），记录哈希均匹配冻结身份。合同共享片段输出为空，无需新增共享提案或扩大写集；两个直接镜像须由R5-I后续机械接入，再核实际字节。WP51技能旗、WP52-A管线、WP52-B附表两独立登记和WP46真实恢复均可继续承接；未升级整个共享合同的状态。

producer为训练家配置、默认目标数据与当前资格/HP；本地write仅分数输出，但前置准备仍可改临时计算状态。consumer继续目标通用修正、平均、多目标偏好、整体修正、阈值权重和行动登记；debug/display与选中记录属于后续投影。实际治疗另行经资格、逐目标中央恢复、HP演出更新和恢复消息，HP赋值同步持久个体；局部评分不写这些状态，也未验证保存往返或宿主显示。无本局部菜单取消入口；“不提交HP”不扩大为全AI无副作用或异常统一回滚。实际群体治疗可恢复一目标、跳过另一目标，与局部评分守卫分层。

独立保护 B26/JungleHealing：固定R仍误调整体族，LIFEDEW仅有目标族评分；不追加HP奖励，状态项保持。其它治疗族及旧BE向量字节保留。旧 GR3-M09-001 的精确owner/scope为 M09/WP51§7录像主责任导航（WP57/76→WP58），与本项新评分组合不同root cause；OPTIONAL、DEFERRED、旧U08 NOT_STARTED保持，未重开、未把历史PASS转签。当前 canonical反证与原历史文件按精确身份复核，冻结28MB全历史关系不重复下载。详见 [regression-results.json](regression-results.json)。

剩余具体门：R5-U04所需实际贡献/接受回执与依赖握手尚未提供，R5-I实际commit/tree也未提供，故 actual integration/acceptance/closure 为 WAIT。取得依赖后按 actual-reviewer-entry核限定实际字节；候选PASS不得转签，若上游改变本scope，只定向复审受影响部分。随后仍需R5-I登记、U08统一限定验收与关闭字节核验/唯一激活回执。

R4历史隔离执行4、R5 review新增隔离执行4、本update新执行0分别保留，未重跑或充作本候选执行证据。宿主/完整Demo/最终选招与分布、默认样本是否使用Anti配置、任意插件组合仍UNVERIFIED。optional7、no-required7、政策6及M11-005内optional方面保持隔离。没有修改候选、正式规格、公共登记、reference或冻结历史，没有merge main或访问Mac。

审查发布分支 `codex/r5-u05-independent-review-20261013`，只新增本目录六份文件。报告commit/tree及六文件完整远端读回（含manifest自身）由外部最终回执绑定，避免自哈希递归；检查方法与结果见 [independent-validation.json](independent-validation.json)。
