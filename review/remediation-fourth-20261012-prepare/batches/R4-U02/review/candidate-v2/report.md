# R4-U02 candidate-v2 有限独立复核

结论：**CANDIDATE_PASS_SCOPED**。唯一阻塞 `R4-U02-CV1-001` 的 SF04 前提已修正，本候选无本批剩余必修。仅复核该修改及必要差异，未重新进行全批或全球语义审查。

| Finding | 最新候选裁决 | 证据来源 |
| --- | --- | --- |
| GR4-M03-001 | PASS | 复用固定 v1 限定 PASS；相关正文、RM01–12 和验收记录完整字节保持 |
| GR4-M03-002 | PASS | 第2项及 SF04 作本次有限独立复核；其它四项和未变对照复用固定 v1 资格 |
| GR4-M03-003 | PASS | 复用固定 v1 限定 PASS；相关正文、ER01–07、旧辅助/恢复对照和验收记录完整字节保持 |

## 绑定输入

合同仍为 `08a57fb55118914a74ac1ffaf617647c01df8938`。新候选 `46255c6c4445b1f6d0bb18cce850deff85eb82a3`，tree `34c9a09b2762cfca7160e1fb65d9e2a8dc0de068`；作者发布回执位于 `7fdec6c45ae190d05578c897477704f797a00e7d` 的 `author/candidate-publication-v2.json`，后继仅新增该回执。

复用的独立报告为 [v1 report](https://github.com/y805939188/pokemon-essentials-clean-room/blob/be0be4c4c8fb1040b21ec9d3bee6ee270e537457/review/remediation-fourth-20261012-prepare/batches/R4-U02/review/candidate-v1/report.md) / [逐项 finding](https://github.com/y805939188/pokemon-essentials-clean-room/blob/be0be4c4c8fb1040b21ec9d3bee6ee270e537457/review/remediation-fourth-20261012-prepare/batches/R4-U02/review/candidate-v1/findings.json)，报告提交 `be0be4c4c8fb1040b21ec9d3bee6ee270e537457`，tree `251e5ef6c393b98a1b88830ef797058023ff2abe`；发布后继 `81f9f156273396efec32526c39a08e4f51b2c66c`。原评判保持为历史原结论，不改写 v1 的 REQUIRES_CHANGES，也不把其执行或实际接受资格扩大到新输入。

## SF04 判定

候选测试目录 `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md:521` 现在明确：SF01 转移后玩家 `(10,10)` 向右，后继 `(11,10)` 覆盖为合法、可通行的 `can_surf=true` 水域；排除岩架/冰/瀑布、遭遇及其它改写。普通向右一步完成，合格玩家步后通知正常返回。

根审者与原002审者独立质疑了“未上岸/ending保持假”是否只是循环预设。决定性输入是前方目标可冲浪：固定 R 的上岸入口在任何基点/结束标记写入之前由可冲浪门返回。玩家移动随后继续普通平移；结束标记从 SF01 的假值保持。完成步的合格通知清旧基点，结束标记门为假，因而不取消冲浪、不进行上岸音乐收尾。该结论能由独立输入和固定源顺序推出，原阻塞已在新候选消除。

未变 SF06 提供陆地反向对照：冲浪中，前方不可冲浪且前跳成功，先写离水前基点及结束标记；完成通知再清基点、取消载具、重置遭遇、恢复地图音乐并清结束标记。新 SF04 正确引用它，没有删除或改写该反例。

固定参考为 `Maruno17/pokemon-essentials` 的 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（tree `7589c800b61ba13a13040ed0d686979b80a84fd0`）。本次根审语义读取仅为 `Data/Scripts/004_Game classes/004_Game_Map.rb` 222–247、`008_Game_Player.rb` 141–177、`006_Game_Character.rb` 935–991，以及 `012_Overworld/004_Overworld_FieldMoves.rb` 715–724、738–751；辅助审者的必要面对目标/通行追踪见 [sf04-recheck.json](assessments/sf04-recheck.json)。未执行或修改参考。

## 有限差异、验收与限制

[input-validation.json](input-validation.json) 独立确认正式差异只有第521行（1删1增），其余七批准正式文件及二十五条向量完整字节保持，测试目录所有其它行也逐字节相同。验收映射只新增 `records/1/criteria/1/review_followup`；反证文件只追加本问题 followup，更新的完整行及行身份一致。作者 `revision-sf04.json` 与完整新文件身份吻合；旧 v1 自查/发布回执被明确保留为历史，未作为 v2 新字节签名。

十五项最新限定静态结论均 PASS：十四项复用原有正确资格，一项重新核 SF04。二十六向量的最新静态判断均成立，其中二十五条复用未变 v1 结果，一条作本次有限复核；**全部 NOT_EXECUTED**。GR3/229/341 限定资格与消费者未变，未重开或重新签旧全项。

[findings.json](findings.json) 给出最新三项及逐 criterion 的来源；[identity.json](identity.json)、[read-ledger.json](read-ledger.json)、[execution.json](execution.json) 记录真实任务、读取和边界。主审 thread `01a130d7-7e94-7407-a89d-ef57dbfa6021`，辅助审者 thread `01a130da-7748-76e1-ac35-691f6bb6d03a`，均独立于作者。请求 sol/ultra/default/Fast=false；实际 model/reasoning/tier/Fast 回显 **UNVERIFIED**。

本次仍为 **NOT_EXECUTED_THIS_UPDATE**：新增参考、模型、宿主/Demo执行均0。固定第四review原有4次隔离原函数调用仍按原 M01/M02/M12 范围保留，未重跑或转签为本批运行。真实地图、媒体、像素、宿主继续时机、Demo可达和外部覆写仍未证。

报告只写独立分支的本批 `review/candidate-v2/`；未代修、未接受/关闭、未改公共台账或 main。此候选 PASS 仅满足候选门；实际整合仍须唯一登记员冻结实际 commit/tree，再作独立 actual 复核及后续门。报告/发布提交完整身份由后继发布回执与最终回应绑定。
