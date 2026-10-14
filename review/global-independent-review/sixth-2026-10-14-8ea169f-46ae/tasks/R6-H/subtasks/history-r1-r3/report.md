# R6-H / history-r1-r3 独立资格核查

本子任务完成 **R1–R3 历史身份、分母、资格继承和当前激活解释的有限审计**。没有发现需提案的新身份或口径缺陷。此结果不能作为任何当前游戏域的全量语义 PASS；原 WP、229 旧控制、341 局部贡献的游戏事实仍须由本轮主域 reviewer 独立读源/合同，不用本报告或旧 PASS 代签。

唯一输出目录是本目录。已全文读工作树 AGENTS.md，后以固定 main 再分段读取其 1–297 行。适用要求为 reference 只读、净室描述、不得实现框架、不得按 Ruby 架构翻译、明确未知。本轮只写独立审计材料；未改 formal/specs/planning/audit/旧报告/reference，未 git 切换、提交、push、联网、安装、执行仓库旧脚本、真实存档或宿主。

固定 main 为 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`。第五原报告入口从 `f49d870c6fd616ab6736754a218a4553b5acac7f` 新读；其报告没有被误当作本地 main 的同路径内容。必要 U08/U03 独审报告从 report-index 指定的固定对象新读，未从旧结论推当前游戏通过。

## 新读与完整类型处置

24 份资格/历史说明实际全文阅读，准确固定版本、区间日志与人工处置见 `reading-ledger.jsonl`、`manual-reading-dispositions.json` 和 `read-*.log`。其中 U08 actual 的 regression-results.json 真实连续读 1–280、281–560、561–828，boundary-results.json 连续读 1–150、151–304；21 批历史索引连续读 1–210、211–420、421–630、631–840、841–979。

大幅生成/历史导航 JSON 的**结构审计**与人工语义阅读分开：

| 历史载荷 | 完整结构范围 | 处置 |
| --- | ---: | --- |
| all341-public-source-map.json | 8,883 行 / 341 记录 | 精确 batch/ID/candidate/actual/independent_report 五元组及公共行/关闭指针；没有游戏语义转签 |
| all229-closure-records.json | 10,543 行 / 229 记录 | 原控制/批准控制/FINAL1/各贡献与历史 CLOSED 身份，保留未知/未读/运行 0 条件 |
| accepted-341-scope.json | 11,262 行 / 341 记录 | 与原映射每个共同字段完整相等，并保留新第三轮 join 指针 |
| 第五 regression-third-23.json | 70,569 行 / 23 控制 | 完整递归类型/身份；23 原范围及 76 标准另以完整字段投影人工实读 |
| 第五 regression-legacy-scope.json | 437,255 行 / 229+341 记录 | 完整递归类型/身份；原 qualification 容器完整 hash 对照，无旧 verdict 转签 |
| U08 historical-regression-input.json | 76,816 行 / 610 记录 | 全结构；本分工独立核 R2/R3 593 个 owner/record/qualified-scope 容器，R4 17 项由同级分工处理 |
| R1 review-manifest | 4,127 行 | 完整历史表/叙事类型结构与身份分类；不是 R1 各 WP 原游戏语义复审 |

这些文件所有递归单元均解析；每文件 bytes/SHA/blob、所有类型路径与叶数量在 `structural-inventory.json`，不是 inventory_only 和不是自动语义 PASS。R1 manifest 另在 `r1-manifest-structural-inventory.json` 完整分类 2,431 表行、1,129 非空非表行。没有把可读历史叙事包装成资源缺失；仅以类型/身份处置它们，不引用它们作为本轮当前游戏语义证据。

分配的资格说明全文未读 = 0；分配的生成/历史资格结构未读 = 0。这里的分母**仅是历史资格任务的上述说明/容器**，不能解读为 reference/formal 的所有可审游戏范围未读 = 0。本子任务没有声称全文人工重读 437,255 行内嵌游戏历史，也没有给其自动结构解析发语义通过。若 root 将这种历史游戏叙事重新列为本轮 primary 游戏审读分母，须另列实际未读；不得用本子任务 COMPLETE 或 L13 闭合它。

## R1：保留原 WP 范围，拒绝臆造合计

R1 没有被换算成第二轮/第三轮控制总数。新读 `review/wp80-delivery-readiness-review-2026-10-03/report.md` 1–44：其 3–5、26、44 行明确只是输入就绪，不签全集语义/净化/运行批准。其 32–34 行还保留原 WP68/69/70 限定批准与新净化输出待审之别。R1 manifest 3–6、18、23、25、27–28 等保留固定 WP/版本/限定范围和管理回填；旧当前/ReviewPending 字样按所在历史时点解释。未逐 WP 重新发通过结论，未发明 R1 必修/标准总数。

## R2：229 / 21 / 341 是三个精确口径

原二次全局 final-report 9–20 行的新读结果是 233 规范项、229 必修（P2 200/P3 29）、4 非必修 A019/B030/D012/D017；不是 233 个产品功能。历史关闭解释由 delivery history-navigation 15–22、28–30 行和 closure-summary 3–7 行限定：21 批/341 已接受局部贡献，229 控制在 FINAL1 支持后历史 CLOSED、OPEN 0；接受与关闭原为不同阶段。

本轮独立结构复算：229 distinct ID；21 distinct batch；341 distinct 五元组且 341 distinct batch/ID。第三轮 accepted-341 每个共同字段逐行等于原 all341；第五 229 控制 ID 集和 341 五元组集亦完全等于原集。所有 593 R2/R3 frozen record hash、qualified-scope hash、ID、owner、record_key 均匹配；没有以摘要旧数字代替全数组。详 `structural-checks.json`、`qualified-binding-checks.json`、`r2-341-tuples.tsv`、`qualified-593-bindings.json`。

批次贡献数依序 B01–B21：14/12/27/35/16/10/19/17/20/7/6/9/8/24/16/24/12/8/24/19/14，总和 341。限定范围保留 proposal-only、partial、read-only、NOT_AFFECTED、只改标号/导航等各种历史资格；同 ID 的局部作者贡献不升级为整 ID 或整文件签名。

原 B10–B19 历史标签 **158** 对实际数组 **138** 的勘误是另一口径。B20 historical-count-clarification 18–37 行保留历史数组与按 owner 的 138，不改旧签名；这不是当前 R5 568 schema−410 native=158 的附加单位。

## R3：23 / 76 与两项排除

第三轮 final-report 3、32–60 行列 25 保留 ID：23 REQUIRED、1 OPTIONAL、1 NO_REQUIRED，不是 25 必修。final-closure-acceptance 新读 111–166 行激活的原 required ID 集恰 23，且与第五 regression-third 原数组的 23 ID 集完全相等；数组真实 criteria 合计 76。

`r3-all76-qualification-read.jsonl` 将 23 记录的全部原前提、unknowns、historical relation、reuse qualification、76 个标准原文完整投影，分 1–8/9–16/17–23 实际人工审读。它保存旧正常/反向/失败/部分提交条件，且全部明确只是原身份/范围和 criteria 继承，不是本轮当前游戏事实裁决。`r3-76-clause-matrix.tsv` 给每个 criterion 精确原 clause pointer。

`GR3-M09-001` 仍 OPTIONAL / DEFERRED_U08_NOT_STARTED；`GR3-M02-003` 仍 NO_REQUIRED_REVISION_NOT_REOPENED。第三轮 proposed-batches 217–239 行的新读说明历史 GR3-U08 是用户将来可选范围；现在的 R5-U08 是独立第五轮必修整合任务，同名后缀不使历史 U08 启动。第四/第五的各 76 也不与此 76 相加。

## 当前激活与历史失败

固定 main report-index 310–399 行绑定候选 `13fddb0a217b36974c75657aa68da0caf104ee48` 与非作者 closing review `044c3483229e7e76bedf1fc244fc84d274bf059c`。该 closing report 27–41 行明确 current_effective 是生成时 OPEN，唯一激活回执选择同一已审不可变 records/proposed_only_after_valid_activation；旧 OPEN/WAIT 不重开当前 CLOSED。

另作 92 全选择结构核验：92 个唯一 ID/准确 index/pointer，所选状态 hash 及**完整 closure record** 的 scope_record hash 全匹配；proposal bytes/hash 匹配。所选为 CLOSED/true，原 current snapshot 为 OPEN_REQUIRED/false。这是身份/状态选择 TOOL_VALIDATION，不是新游戏语义 PASS。审计初次误将 scope_record hash 目标解释为 frozen_required_scope 子对象，出现 92 个 False；查完整记录后确认它绑定整条 closure record，已明确保留该审计假设更正于 `activation-structural-checks.json`，不提出伪缺陷。

新读历史 candidate01 report（7533）3、24、30、39–41 行确认为 G03/G09 FAIL，唯一三行 UI scope 修复，不回写旧 FAIL。新读 U03 actual01 report（1eda）3、21、25–31、41 行确认 59/60 static、10/11 具名项通过，WING 合法 Consumable=false 的反例仍 EV+1/库存 1。后继限定 report（b158）3、9–13、19–27 行只补非重要且有效可消耗为真，一项新 actual 复验＋59 精确未变复用，旧 FAIL 与两 advisory MISMATCH 保留。

U08 actual boundary-results 151–192 行具体保留两对实际/冻结 SHA：root-M01 canonical `b900a28d…` vs `e5a04266…`，M01 module `7181ecb0…` vs `0a3b1cb6…`；只接受四个明确记录身份，未宣称整个旧 advisory SHA 匹配。SC 捕获体 LF 的资格排除在同文件 123–149 行和 closing report 35 行保留；本分工未新读其源正则，因此没有凭这些历史结论签本轮源事实。

## 证据等级、矩阵和提案

`forward-matrix.tsv` / `reverse-matrix.tsv` 全 593 记录逐 unit→qualified-fact pointer→当前必要新 ID/正式消费者路径→原范围，且标记 CURRENT_GAME_CLAUSES_REQUIRE_PARENT_PRIMARY_REVIEW。原文件和指针精確到 clause；旧 accepted 闭合关系未转为当前新语义签名。

本轮历史解释属于新静态人工资格审读；递归解析/hash/tuple/selector 属 TOOL_VALIDATION。DERIVED_VECTOR 只审其历史条件，不新生成运行通过。新增隔离参考执行 = 0、独立模型 = 0、host = 0、完整 Demo = 0。旧 R4/R5 隔离各 4 记录只保留分期身份，不并入本轮执行。

`findings.json` 没有新提案；本报告不给最终 root 裁决。model/effort/tier/speed/实际 UUID 均 UNVERIFIED；只记录用户请求 sol/ultra/default/普速/禁 Fast，没有查额度/认证或追配置。
