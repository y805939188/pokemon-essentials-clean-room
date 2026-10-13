# R5-U01 非作者独立候选复审 — round-01

固定候选整体 **FAIL**：34项中32项限定静态候选PASS、2项FAIL；248项必修条件中243 PASS、5 FAIL、0 WAIT。133个静态向量已独立核对；它们均为DERIVED_VECTOR，不是新增执行。

审阅任务 `01a1352e-01d1-765f-975a-e2917852301a`（/root），请求gpt-6.1-sol / ultra / default普速、禁Fast；实际模型/effort/tier回显均UNVERIFIED，不因此判内容失败。作者候选在本任务前固定，当前审阅人员未编写或修改候选。作者真实任务ID未由输入提供，不把来源线程或预留角色槽当作作者任务ID。

冻结准备 `22fba7786b0090a1955ce6211315b0036cddfbcd` / tree `21f3484d167d8cab7a288e0204c72f275414d52e`；候选 `1cf377b17ef2d621a932a47c6425f4784a35afe0` / tree `89281cbe3d667759db6707d38241c1c8725156e1`；证据后继 `1f44bbc335752fc79bca103a9d5e86b128916786` / tree `0e604fba5343946775cd72620ca8ae92d469cf6c`。B5/R/语义报告/发布身份见[审阅清单](review-manifest.json)。

最小返修点均位于已授权的U01提案范围：

1. **GR5-M01-016 / static/06**：候选WP03 §4.3.1（投影行110，U01-O003）仅称四道具默认“按道具主责合同”，未明确绑定冻结验收指定的 **GR5-M05-006**。补此主责ID及准确交接引用，并明示该贡献尚待实际接入；不复制四默认表，不声称B5已修。其余16条件通过。原反证：C01F resolution `/resolutions/8`、root-M05 canonical `/findings/5`；限定默认事实和空译/原字段缺值区分本身通过。
2. **GR5-M01-021**：新WP14 §3.2和WP03已写空表失败，但同一25文件候选投影WP14 §8行267仍无条件写“身份未命中→回退…不报错”；旧DG17行269也未限定登记表非空。定向同步WP14 §8的非空回首条/空表失败两支，并给DG17显式非空前提，保留已有U01-M01-021空表反例。参数缺配置产生默认实例仍独立保持。失败4条件为static/01、static/02、static/04、reference_facts_to_cover/02；021其它4条件通过。固定R的整数图块查询、参数回退及真实地图建立调用已直接核对。

逐项裁决如下。PASS只签固定候选中对应U01有限贡献；整份共享文件、实际整合、正式接受与关闭仍分别WAIT。

| ID | 候选裁决 | 必修条件 | 最小返修 |
| --- | --- | ---: | --- |
| GR5-M01-001 | PASS | 4/4 PASS | 无（仅限定scope） |
| GR5-M01-002 | PASS | 4/4 PASS | 无（仅限定scope） |
| GR5-M01-003 | PASS | 3/3 PASS | 无（仅限定scope） |
| GR5-M01-004 | PASS | 4/4 PASS | 无（仅限定scope） |
| GR5-M01-008 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M01-009 | PASS | 7/7 PASS | 无（仅限定scope） |
| GR5-M01-010 | PASS | 6/6 PASS | 无（仅限定scope） |
| GR5-M01-011 | PASS | 8/8 PASS | 无（仅限定scope） |
| GR5-M01-012 | PASS | 8/8 PASS | 无（仅限定scope） |
| GR5-M01-013 | PASS | 8/8 PASS | 无（仅限定scope） |
| GR5-M01-014 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M01-015 | PASS | 10/10 PASS | 无（仅限定scope） |
| GR5-M01-016 | FAIL | 16/17 PASS | 明确GR5-M05-006引用 |
| GR5-M01-017 | PASS | 10/10 PASS | 无（仅限定scope） |
| GR5-M01-018 | PASS | 10/10 PASS | 无（仅限定scope） |
| GR5-M01-021 | FAIL | 4/8 PASS | 同步WP14 §8及DG17前提 |
| GR5-M01-022 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M01-023 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M01-024 | PASS | 11/11 PASS | 无（仅限定scope） |
| GR5-M01-025 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M01-026 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M01-027 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M01-028 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M01-029 | PASS | 10/10 PASS | 无（仅限定scope） |
| GR5-M01-030 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M01-031 | PASS | 9/9 PASS | 无（仅限定scope） |
| GR5-M02-001 | PASS | 3/3 PASS | 无（仅限定scope） |
| GR5-M02-002 | PASS | 3/3 PASS | 无（仅限定scope） |
| GR5-M02-003 | PASS | 3/3 PASS | 无（仅限定scope） |
| GR5-M02-004 | PASS | 4/4 PASS | 无（仅限定scope） |
| GR5-M02-005 | PASS | 3/3 PASS | 无（仅限定scope） |
| GR5-M02-006 | PASS | 4/4 PASS | 无（仅限定scope） |
| GR5-M02-007 | PASS | 4/4 PASS | 无（仅限定scope） |
| GR5-M02-008 | PASS | 6/6 PASS | 无（仅限定scope） |

全部逐条件理由、独立源/候选行和原证据指针见[criterion-results.json](criterion-results.json)；完整身份与实际实读范围见[source-reading-log.json](source-reading-log.json)。没有以作者映射、旧PASS或hash批准候选。15共享文件/23局部操作按producer→write→consumer→display→persistence及准确主责保持隔离；U01没有整合依赖，不授予其它批次或整份共享文件签名。

隔离重放独立执行：在/tmp重建B5的25目标文件，git apply --check及实际应用通过，与47操作重建、10完整镜像和15共享片段逐字节一致；196项TOOL_VALIDATION通过。5份现有测试目录1112条完整旧表行均保留。旧历史的22合同指定指针及2额外保留对照直接核对，共24记录；保留其owner/scope/前提/状态，不沿用历史签名、不重开全局review。021的DG17缺前提是当前范围未闭合，不改旧历史CLOSED。见[regression-results.json](regression-results.json)和[independent-validation.json](independent-validation.json)。

| 执行分期 | 隔离参考记录/新增行为执行 | 资格 |
| --- | ---: | --- |
| R4历史review | 4 | 原限定历史，未重跑 |
| R4云端update | 0 | 保持历史口径 |
| R5 review历史 | 4 | 原限定历史；004含失败及修正后两个进程，不把记录数当案例/进程数 |
| 本R5-U01作者update新增 | 0 | AUTHOR静态提案 |
| 本次非作者review新增 | 0 | SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR / TOOL_VALIDATION |

真实文件/存档/归档往返、完整编译/生成器、原生宿主/Demo、地图/媒体实效、统计随机与跨宿主序列、动态插件和无界组合保持NOT_EXECUTED或具体有界未知；浮点/空表等兼容事实不自动成为未来支持政策。optional7、no-required7、政策6与M11-005内optional方面继续隔离。

本任务只提交本round-01的6个review文件。正式131文件及公共registration/冻结历史/作者域均未改变；没有merge或push main，没有触碰Mac。接收、关闭及候选返修由后继任务按精确字节处理；修复后只定向重审上述受影响条款/向量与同步范围。普通推送与完整远程读回回执由审阅清单的后继publication字段及任务最终输出绑定。
