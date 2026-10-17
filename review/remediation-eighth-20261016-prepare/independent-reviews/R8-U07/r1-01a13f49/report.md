# R8-U07 独立候选复审

结论：**PASS_SCOPED_CANDIDATE，3 必修及已采用 U12 optional 全部 PASS，FAIL 0。** 该结论只针对固定候选；实际整合 PASS、ACCEPTED、CLOSED 均未授予。

## 固定输入与独立性

- 仓库：`y805939188/pokemon-essentials-clean-room`
- 候选分支：`codex/r8-u07-revision-20261017`
- 候选 commit：`b91bb8143fb8bf257d0b9ecd5b1ace294e799c49`
- 候选 tree：`602313763168f26d9e0926347b52b92f0ddc0647`
- 基线 commit：`4575e80d041ab0c74a42e2e36399d05791dbaa5b`
- 基线 tree：`e8fb0884694afee309c57504babf9f849a5f1498`
- B8：`fd1df570cad987dc3852a3b958f03916e317f7fe`；参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`
- 唯一镜像：`review/remediation-eighth-20261016-prepare/candidates/R8-U07/mirror/review/remediation-eighth-20261016-prepare/navigation/current-r7-metadata-qualification.json`
- 镜像 24072B，mode100644，SHA256 `e2299cc269deda6b5517a5b150f985ae367356d646b9e73bfd24658e89960650`，blob `10cb81e48d35ed39fda532c4f75a218f470e002f`。

本复审是与作者 `01a14a0d-f778-7352-adc5-0670af8770c3` 分开的委派任务；没有参加候选创作，也未通过改角色名取得独立性。只读子核负责计数与累计保留、R2、U06/U12、根合同来源及边界；主审接收这些完整结论并独立取回全部候选和22份历史单位核身份、候选全文、合同接合及所有引用。当前复审运行 task UUID 未在接口暴露，记 UNVERIFIED，不从 source parent 或协调 UUID 猜造。请求配置为 gpt-6.1-sol / ultra / default / normal / Fast off；无权威运行 echo，实际五字段逐项 UNVERIFIED。

已先读 AGENTS 和 `review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md`。后者明确不用于评审报告、变更日志或审计记录；本任务只写独占复审证据，不改作者候选。指定容器创建失败，改用已连接 GitHub 接口及隔离 JavaScript 核元资料。未运行 shell、Ruby、参考游戏或实际业务。

## 逐项裁决

| ID | 判定 | 有限理由与最强反方处置 |
| --- | --- | --- |
| GR8-HIST-001 | PASS | `/stage_counts`准确保留旧3项/2批及其它阶段0为历史投影，当前四门各27项/13批绑定原ledger、最终公开接收和关闭。字段生成UTC仍UNVERIFIED；原文档UTC不倒推生成时点。合法旧快照及内嵌早期pending均保留，不与最终有限SATISFIED混同。 |
| GR8-HIST-R2-BINDING-001 | PASS | `/candidate_r2_bindings/0–2`三组完整SHA/tree/task/candidate/freeze/verdict与原r2回执、报告及registry逐一一致。虽原reviewer_context/fresh_r2已正确，直接reviewer_task_id仍会配错当前r2；新overlay只限定旧直接ID/prompt为初次r1派发，保原r1 WAIT/helper资格和原关闭。 |
| GR8-HIST-U06-CONTINUATION-001 | PASS | `/u06_continuation`区分历史启动WAIT、程序不授PASS和同context新内容完成。旧启动字段可合法保存；当前完成来自新签内容裁决，不来自程序允许继续。旧WAIT、违例及UTC/PID缺口保持。 |
| GR8-HIST-U12-RECEIPT-SCOPE-001 | PASS（optional） | `/u12_input_receipt_scope`把15:43输入UTC/两WAIT旧句限定为初次输入/发布范围，后继两有限PASS归于新report/per-id及相符parent/eligibility。完整原回执本已提供分层，故不新增required、不撤销当前合格结果，也不造完成UTC或增审者。 |

三组 R2 实际配对：

| batch | result commit | r2 reviewer task |
| --- | --- | --- |
| R7-U03 | `a8a65bc4f29e2b19c8b63fd59c9c2a0941be6520` | `01a1401b-538b-764d-b23c-eafd6825c025` |
| R7-U07 | `1bd0799d1819ef87c3c383a7f8e50d78756333c4` | `01a1401b-7752-70f1-ab8b-2e9b903e1029` |
| R7-U10 | `d7337be83dae5aa7b848cd6a603c2aa7048ffa0c` | `01a1401b-a243-7253-9411-101ed805d019` |

U06 程序裁定为 `2026-10-15T16:11:58.542538+00:00`、PASS=false；同审者在 `18:41:34.372710`签两项内容PASS，parent于 `19:22:51.970639`接收 `55a843b3ab01d26442f604770f30932e120f923b` / tree `da27609dd33db77db5f74bb288d6b80970bda7f1`。原审者 `01a1401c-1527-75c6-9a36-7bc9b3a00007`、续turn `01a140d9-0f0a-7559-983e-21717145aac0`不增加context/票；旧 `84dd2631af9f3496008fa9971c136c43a4b772a7`两WAIT及一次认证状态查询程序违例未豁免。

U12 两份输入回执均保留 `2026-10-15T15:43:09.153030+00:00`原输入UTC。初次 `38ea9afb84395d7c20d3beed322281dd50a688e4`两WAIT与后继 `fd112431b76e39980364e1177cbb3109b34b5a33` / tree `93b40b40305140ef9964ab68493e638e81348eb4`两有限内容PASS分开。parent `16:04:29.983181`、eligibility `16:10:57.892737`均绑定同一结果及审者 `01a1402e-9f4a-72f7-863e-018ee4a4e036`。这些时间各保其职责，不把任何输入UTC重命名为完成时间。

完整证据路径、指针、最强反方、区分场景和未决门见 [per-id.json](per-id.json)。区分场景是静态 DERIVED_VECTOR，NOT_EXECUTED。

## 证据覆盖与保留

候选全部28文件（357523B）及本批22份历史单位（952892B）均独立取回全载荷，UTF-8 bytes、SHA256、Git blob一致；候选manifest27个非自身条目348629B准确，自身8894B另核。31个source/pointer全部解析。身份/运输检查不授语义FULL；manual SOURCE_STATIC判断来自原报告、裁决、回执及完整适用合同。

完整读取/接收清单、当前/原来源双身份、typed-purpose去重及各实际reader见 [coverage.json](coverage.json)。本批15继承单位加7份所选U12单位无增漏。继承87原输入的原commit/path/blob及完整bytes/SHA均另核一致（8909932B）；这些结构/运输接收不冒称87份外域语义FULL。原根14–17、完整提案/反证及三counterreview已读，旧与当前canonical资格准确接合。审计gzip流未直接解压、不授FULL：完整原源、13491nodes→64roots typed等值以及重建restored精确hash复核提供本批同用途语义；历史reading-projections工具投影不作本次证据。R7 registry全42条、ledger全27 issue/13 batch、final decision全27记录的非重复semantic/shared/dependency/history资格已核读；旧内嵌pending按原时点保留，最终有限门另核SATISFIED。原r2及U06/U12结果commit的报告/相关per-id与B8副本另作固定身份交叉核。

42仍为唯一任务ID人口，13作者/17候选/12actual；17候选结果+15actual结果=32版本，不认证42个不同真实context。U04/U05共用实际审者 `01a13fef-cc3c-730e-a5ba-a59a61501034`；U06/U10/U12同context续turn均+0。旧FAIL/WAIT、辅助披露、27/56/92有限关闭、L01–14与有效配置UNVERIFIED均保留。新复审协作任务不回填R7人口或旧独立票数。

作者95断言只覆盖身份、本地保持、字段和工作区；31引用解析只证明存在。它们不能替代三份r2报告的有限内容资格、U06新签裁决或U12报告/eligibility的语义实读。本审未重跑作者脚本；独立元资料核验与完整语义阅读记录在 [validation.json](validation.json)。实际业务、Ruby、参考/游戏/native/宿主媒体/真实存档回放新增运行0，所有新业务向量NOT_EXECUTED。原7数学/有限证书+1环境探针及旧PBS摘要原ID/I/O/exit/UTC的UNVERIFIED/alias_UNRESOLVED资格均未被修改或增加信用。

## 写入边界与发布

baseline→candidate 为 ahead3/behind0，28个新增文件均限作者U07独占前缀，无修改、删除或改名。镜像只有合同指定一个目标；正式 `review/remediation-eighth-20261016-prepare/navigation/current-r7-metadata-qualification.json`尚不存在，未实际整合。root/review逐节点比较表明正式规格、公共导航、catalog、audit、planning、旧报告及R7历史保持原树。R7 subtree `a2041f872f95034aa064b6661ddc9a5a2f8a7242`；旧global-independent-review subtree `d3ea45e854129517de92a4e1ee57a38b22ccf673`。main及第七轮delivery tag当前均为B8；双快照稳定不追造作者操作期间的ref历史。

作者content回读仅绑定 `dc3c90f9ee4be7da7197d0fccccf207dc8bdf5b8`（18文件312280B），evidence回读仅绑定 `ccc0ce0b843509f892fc16b73db9a2eba3b7cf64`（27文件334284B），各自清单与历史tree一致。二者不冒充b91最终回读。本次已另核b91全部28载荷；mirror三提交同一blob。原工具失败、错误SHA被拒及原始stderr尾空白按原证据保留，无业务通过推断。

本次只新增 `review/remediation-eighth-20261016-prepare/independent-reviews/R8-U07/r1-01a13f49/`独占证据，发布到 `codex/r8-u07-independent-review-20261017-01a13f49`，不改作者分支、mirror、正式目标或main，不force、不打tag。真实发布commit/tree和最终全包回读由后继回读及本任务包外回传绑定，不预填未来hash。

## 未决接收门

本批无direct/transitive语义编辑前驱，四项候选语义无未决依赖。仍须R8-INTEGRATOR唯一写正式目标，冻结真实实际整合commit/tree，由非作者完整核受影响整文件和累计保留，具名R7资格owner、历史资格owner、U06资格owner及唯一整合者接收，再分别登记ACCEPTED/CLOSED。公共导航/追溯是否同步由协调者按实际需要具名处理。本审不以候选PASS替代这些门，也不认证实际运行等价。

协调 `01a14a04-b178-7567-a4eb-0f0bfac9a0d9`由父任务转交结果；本审不直接发送外部消息。
