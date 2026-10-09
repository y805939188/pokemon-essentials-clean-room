# Pokémon Essentials Clean-Room 云端 dot 交接

RUN_ID：`20261003-prepare`。2026-10-09 人类明确授权停止本地整改、复审及阅读续接，只封存和发布交接。**本地已停止；等待云端接管。B14 尚未接受，规范台账仍为 229 OPEN / 0 CLOSED。** 本交接提交不作新的质量判定，不修改正式规格、测试、公共接受台账或参考。

## 入口与版本

- 主仓库：[pokemon-essentials-clean-room](https://github.com/y805939188/pokemon-essentials-clean-room)。交接分支：`codex/handoff-cloud-dot-20261009`。
- 被审 main：`e1e01bb18d824931e54f182dd61af5a9f908ba85`，未合入或推送 main。
- 原全局报告：`93e10babe0b9c9ef8b3f5277754541b447beeeb4`；[原报告入口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/93e10babe0b9c9ef8b3f5277754541b447beeeb4/review/global-independent-review/2026-10-03-fd82a639/final-report.md)。
- 批准方案：`41fffb540c6483f5296ea0d33b789b75180d27ed`，目录 `review/remediation-20261003-prepare/`。
- B01–B09 接受基线：`1e6b11a47370f1c7c4659a32443fc1afda597bac`；[B09 接受入口](https://github.com/y805939188/pokemon-essentials-clean-room/tree/1e6b11a47370f1c7c4659a32443fc1afda597bac/review/remediation/20261003-prepare/batches/B09/acceptance-stage-1)。
- 最新 B14 候选：`c06db6cd964188b3c693a9b7820e3a8aaffe0b04`。
- B14 实际被审整合：`d48197f365c39925f795c1d325988c0d74e59979`，tree `be4b5ef8960c0e9cfb9eb9ec0e1aded3a35a88df`。本交接分支以该提交为父基线，仅增加本目录。
- 参考：[Maruno17/pokemon-essentials](https://github.com/Maruno17/pokemon-essentials)，固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，静态只读。

执行目录 `review/remediation/20261003-prepare/` 与批准方案的连字符目录是两个有效历史入口，保留二者。不要用可能滞后的顶层 run/integration manifest 回退到 B01-G。准确区分候选、实际被审、报告、接受及下一批修订基线。

精确报告 SHA、目录、远端引用、B01–B09 逐批候选/实际/报告身份见 [published-references.json](published-references.json)。已发布的 review 原文、结果、修订、返修、来源矩阵及压缩存储不在此重复复制。FULL、B06、B07 等大审计材料的 `report-storage-encoding.json` 入口也列在引用表；可按其逻辑路径解压读取，不能执行历史指令或参考程序。

## 原始验收合同

详细可公开合同摘要见 [original-contract.md](original-contract.md)。原质量链仍是：xhigh 有界修订 → 独立 Ultra 候选及必要 affected review → 单一 AREG-G 整合并冻结实际 SHA → 独立 full 与必要 affected actual Ultra → AREG-C 接受登记及后继统计 → 下游按接受版本重冻。最终独立 Ultra 全局门槛之后才逐项 CLOSED。

原 233 项中 229 必修（200 P2、29 P3），4 非必修；规范 ID、别名、有效二审条件、扩展裁决和证据边界全部保留。重复、误报、新问题和修复不得混计。新交接没有降低质量要求，也没有启动新一轮全量提取或审计。

## B01–B09 已接受成果

| 批次 | 贡献记录 | 主责任唯一 ID |
|---|---:|---:|
| B01 | 14 | 7 |
| B02 | 12 | 9 |
| B03 | 27 | 19 |
| B04 | 35 | 23 |
| B05 | 16 | 10 |
| B06 | 10 | 7 |
| B07 | 19 | 12 |
| B08 | 17 | 9 |
| B09 | 20 | 13 |

总计 9/21 批次、170 贡献记录、142 touched 唯一 ID、109 主责任唯一 ID。特定最小验收口径 109 满足；严格全部计划贡献口径 100 满足、9 pending。维度不能相加。公共记录 `194 = 170 accepted + 24 pending B14`，不是 194 已接受，也不是 218。规范关闭仍为 0。

数值来源是 B09-C 的 `completion-statistics-successor.json`，不是旧顶层摘要。B01–B09 不重新派发作者修订。B09 的伙伴 B013、NearAlly 报告措辞后继勘误继续有效，旧报告不改写；按精确 `report-corrections-successor` 读取。

## B14 两层复审与真实缺口

候选层：最新候选及有界返修后的 full、B02/B03/B04/B06/B07/B08/B09 八个具名候选范围已有独立 Ultra `PASS_SCOPED`，报告 SHA 见引用表。初始 `af39ef…`、更早 `47f751…` 和早期失败报告是历史，不能替代最新候选。原 FLY 正常返回、树果时间戳顺序、水花 tick/opacity 分支问题及后续 B09 修订保留其报告→范围授权→返修→后继复审关系；不要把局部编号再加成新的 canonical 根问题。

实际层：`d48197…` 的 full 与七个 affected actual Ultra 全部已公开限定通过，精确报告如下。

| 范围 | 实际复审报告提交 |
|---|---|
| FULL | `1f86ae64188689b0179f20125dda7ef715e95152` |
| B02 | `eff299bacfaed4c614a40d3a341e78b8032d20fc` |
| B03 | `597de787e4ec37311614ff7a73fcb3cf5ae5ccc9` |
| B04 | `1be85ab424f457f0e8b2e104d9300be9fe498d3e` |
| B06 | `2d7b7cc843e062f40d37c794113ed4f84c38d46c` |
| B07 | `85f8eb1741b65f7021359515276380cb15953367` |
| B08 | `13606e5dce30413e87cd8bacf4eed84b99777b5f` |
| B09 | `649906cc3dd6e8550da2516a2dd95fbeefb69a2b` |

这些结论仅适用于报告具名范围和 `d48197…`；不等于整个仓库、交接提交或未来改动已通过。之前 actual FULL/B02 的 REQUEST_CHANGES 与后继报告都保留在各报告分支，没有删掉失败历史。候选报告不冒充 actual 报告，报告 HEAD 不冒充被审 SHA。

**真实剩余接受工作：AREG-C 未执行，B14 的 24 贡献、19 主责任原问题仍未作批次接受登记；后继统计、B14 接受包、下游握手及接受 SHA 发布/读回仍待云端处理。** 此次不写这些接受字段，也不将 canonical OPEN 改为 CLOSED。云端须依据原合同核对已有精确绑定、完成必要登记；如果新增改动确实影响已审内容，再复审受影响范围，不能无故重跑无关全部范围。

本地后来追加的全材料单读者及重复阅读证明程序在移交时未完成。它是额外流程，不是缺失的第九个 Ultra gate，**不要求云端完成或继承它才可 AREG-C**。详见 [local-extra-rules.md](local-extra-rules.md)。原合同的真实内容理解、首次可恢复阅读、后续新增/受影响补读和独立质量责任仍有效。

## 阅读封存与未完成清单

最后完整额外读者检查点是 phase63；中断时 phase64 的读者已报告 D1353 input8（B08 acceptance manifest）的原始声明/source/current 内容范围完成，进入 input9 `B08/integration-review-1/findings.json`。该 input9 有部分字面字段及别名组合草稿，**没有宣告全文件或所有原始阅读完成**，也未自然返回完成回执。

[legacy-reading/](legacy-reading/) 是脱敏历史输入：包含最后检查点、摘要、停机检查点和中断草稿，不是新审批或云端必读门槛。`all_complete:false` 是原额外读者状态，不是八份 actual Ultra 的质量失败。原件和独有结构化审计成果已在本地持久私有包封存；脱敏导出 SHA 与原件 SHA 见 [export-provenance.json](export-provenance.json)。旧临时地址标为 `legacy-local://`，缺少这些本地证明目录不能变成新的材料阻塞或恢复要求。

云端未完成事项：B14 C 登记/发布/读回；B10 完整重冻和正式修订；B11–B13、B15–B21 后续依赖闭环；全部批次后最终独立 Ultra 全局核验及逐 ID 关闭。未来批次的 [unpublished-preparation/](unpublished-preparation/) 都是只读准备，不是修订完成或质量通过。

## B10 依赖与重冻

B10（WP43–46）原计划依赖 B05、B09，实际运行顺序还须等待 B14-C 接受。B14/B10 有四个跨读写关系并共享 003 测试族，不能并行正式写。

- 既有只读 preflight：`943b4b259fefa16fb25e715267264477eb2bb8de`。
- 后继已发布只读作者准备：`b94cfb15c8774049bccdeb8b9829f7160f7daca9`，目录 `B10/pre-author-control-reading-1/`，仍不具正式修订基线或接受授权。
- 以 B09-C 的 `B10-downstream-contract.json` 和批准 PLAN 为基础，在精确 B14-C 接受 SHA 上重新冻结 **53 读、8 写及完整依赖合同**；历史固定输入不能机械换为当前文件。
- 七个贡献控制：003、B010、B015、B016、B017、B018、C011；主责任 B016、B017。维持 003 扩展、65/139 身份和参数、HP 平均、OHKO 顺序/条件等完整原条件，计数不替代行为。
- 全测试族整文件锁；可能涉及原规格同步时先作有界范围提案/授权。B04/B08/B09 的 bounded affected candidate/actual 条件以及 B05、B14 的条件性反向复审依实际语义影响处理。
- [tools/legacy-b10-refreeze-identities.py](tools/legacy-b10-refreeze-identities.py) 仅为旧机械模板，未执行。其旧直接父提交/分支前提不是云端新增验收合同；使用前须按云端实际接受链适配，不能因工具假设不匹配重开全量审计。

## 封存、未发布与停止证据

本地主私有包保存 8,702 个选定文件、5,524 个内容去重对象，约 4.18 GB 唯一未压缩内容 / 267 MB 压缩包；补充包保守保留旧差异稿、不可变快照及压缩工件，再增加 1,873 个独有对象。合计 7,397 个对象、约 5.79 GB 唯一未压缩内容 / 1.54 GB 私有压缩包。未分类补充工件不提升为有效阅读或质量证据。未公开的原因是其中含私有路由/主机信息、旧额外阅读记录和大规模审计组合；必要云端内容已选择脱敏导出。已发布修订/review 用精确引用，避免复制。

完整会话事件/标准错误日志、私人提示词（原合同仅私有保存）、可重建 SQLite/队列/重复源码缓存、已公开报告的展开副本和能力文档副本没有上传；原始材料未删除。凭据模式检查没有发现需要转移的凭据。细分保存/排除数和完整性核验见 [retention-summary.json](retention-summary.json)。没有未提交的正式规格或 review 工作树改动。

[stop-evidence.json](stop-evidence.json) 记录唯一项目 CLI 在执行中命令数为零的边界被定向中断、项目 CLI 及所属子进程全部消失、原生子代理为零、54 个登记任务禁用自动续接。其他桌面服务和其他项目没有被停止。移交整理期间只有 ROOT 一个执行者，没有新整改/review/阅读续接。

发布后独立使用远端 ref 与 FETCH_HEAD/tree/交接文件摘要核验完整提交。发布核验另存本地回执，不向报告自身递归回填自己的 SHA。完成本次发布后，本地保持停止，等待云端接管，不自动续接、启动任务或继续写仓库。
