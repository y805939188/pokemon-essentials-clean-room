# R4-U02 actual-v1 独立实际整合复审

结论：**ACTUAL_PASS_SCOPED**。三项 finding 均在本次精确 actual 与当前必要消费者范围内通过，**无本范围必修或阻塞**。本报告不登记接受或关闭，不预签未来 U03/U05/U06 输入。

| Finding | 实际裁决 | 实际检查及复用范围 |
| --- | --- | --- |
| GR4-M03-001 | ACTUAL_PASS_SCOPED | 八文件中相关正文与 v2 完整一致；实际范围负/零/正、原始锚点、严格过滤/候选序、UD/LR、一次尝试及路线45/9分层保持；WP75 §8.6 当前引用无冲突。原固定源与 RM01–12 的限定证据复用 |
| GR4-M03-002 | ACTUAL_PASS_SCOPED | 实际失败转移残留、成功步后条件清理、人工结束标记等待门保持；SF04 可冲浪水域与 SF06 陆地反向精确等 v2。新增实际 WP59 握手与当前 WP11/12/16/61、WP06/13 分层均通过 |
| GR4-M03-003 | ACTUAL_PASS_SCOPED | 实际116三入口、正ID缺实例登记、一次推进/让出和后条等待保持；WP11/WP09 辅助/恢复与新生产端边界一致。原 GR3-M03-004/C064 限定资格复用，未重签旧全项 |

## 精确绑定与实际整合

实际输入：`8a61dc3e4e123ac0a734793dffc9261f9911b7a6`，tree `20a0d63b352b80f1d8aae9b3d3e8a5819b93b115`。任务发布：`1784673abf1024b1eb5b265ad548280ff4713f2b`，tree `777c66a65bb18e841cee813240b5fe53619d0803`；任务/机器包按该固定提交读取。合同仍为 `08a57fb55118914a74ac1ffaf617647c01df8938`，固定 R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只读。

实际父提交 `e6d147c613b7456ff8fa267ce78432a63ae84014` 的 U01 有效接受回执已核：五项为 ACCEPTED_SCOPED，CLOSED=false。实际四份 U01 正式文件保持已接受 actual `1ec8655fc3186ad88e3fb1ff1700540eb33d41ff` 的完整字节；此依赖沿原签名保留，本审者没有重新接受 U01。

独立整合核验确认：八个 U02 正式文件逐字节、bytes/SHA256/blob 完整等于 v2 候选 `46255c6c4445b1f6d0bb18cce850deff85eb82a3` / tree `34c9a09b2762cfca7160e1fb65d9e2a8dc0de068`；父→actual 的正式补丁与 B→候选的八文件补丁完全一致。其余119正式文件保持 B `1f36475d22120a0d1175967d5b17d71fe8311d88`。131文件仅作本实际分区的完整性核验，未进行131篇重新语义审查。

三十六份作者、v1 原 REQUIRES_CHANGES、v2 最新 PASS 及发布证据逐字节等于各原固定来源。v1 历史判断没有被改写；v2 候选 PASS 由 [原候选报告](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e28e115f7983c9537559386348a56ecd49b74562/review/remediation-fourth-20261012-prepare/batches/R4-U02/review/candidate-v2/report.md) 保持，实际结论另由本次整合与握手检查作出。

## WP59 当前有限握手

六项独立握手全部 PASS，详见 [assessments/wp59-handshake.json](assessments/wp59-handshake.json)。

1. 新 WP59 §7 与 actual WP11 §4 / WP12 §5.2 同样分开载具标记和两个临时字段：失败上水先提交、没有回滚；正常201保游泳，直接默认转移只取消载具标记；转移/落位/刷新不独立清两个临时字段。
2. actual WP61 §3.2 仍要求地图场景、玩家、有基点，结束标记真才额外收尾；actual WP16 §4.3 仍在临时坐标存在时取旧基点、清后随父、双载具假撤基底。人工结束标记真阻止解释器到达正常201，不把直接转移当成越过等待门。稳定显示的 C064 旧前提和 visible/opacity 条件不被扩大。
3. actual SF04 `(11,10)` 是合法可通行 `can_surf=true` 水域，普通一步不先写上岸状态，合格通知仅清旧基点；SF06 非可冲浪且前跳成功则先置结束标记，完成后取消载具/恢复地图音乐。两个完整行与 v2 相同，原阻塞没有在整合中返回。
4. WP59 完整 §3 时间/日历 8620字节、SHA256 `a238e64f7dd4a112347b918b06ea3a989d4d4dfed5b19695095ca707d032596b` 保持 B 与 U01 父提交原字节；WP06 全文件等于 U01 已接受字节。宿主时钟来源不替代变量槽的 `(t,D)`、查询清零及天数公式。
5. WP06 §3.4 的游戏变量墙钟计时、WP13 的事件私有记录/临时自开关冷却、命令124累计游戏时间计时分别保留自己的状态、时钟与门。当前引用和消费者无冲突。本握手只签当前必要范围，没有把 U01 签名转移到新 WP59 全文件。
6. author/integration-proposals 的世界状态→显示/等待动作在本冻结 actual 的现时消费者上已核，处置为 CURRENT_FROZEN_CONSUMERS_CHECKED；原提案保留历史。当前没有必须改正文的反向引用缺口。

编辑登记→PBS→当前运行地图快照提案仍留 U05/U06 的有限门；本 actual 的 WP75 §8.6 只增加范围能力引用，没有宣称编辑/复制会刷新当前地图。U03 后续新消费者字节需要自己的精确实际复审，U06 最终受影响整合/关闭尚未执行。这些未来门不作为本批当前实际范围的必修，也未被提前签过。

## 逐项标准、旧范围与边界

[findings.json](findings.json) 逐三项列十五标准的实际裁决、来源和限定范围。未变的候选源行为/前提/反向向量可按原资格复用，本次实际读取了具名正文、当前消费者与必要边界，没有重新重复整批独立质疑。二十六向量完整保持并全部 NOT_EXECUTED；文档逻辑判断不等于执行通过。

GR3-M03-004 的正常进入清表→图更新→辅助、实例/记录区分、条件恢复和异常前缀保持；116只是新增生产端，不变成默认读档保留旧表保证。C064 原229/exact341只有稳定显示限定资格复用；其旧 tuple、范围和未执行限制不变。其余GR3/229/341未扩审、不转签、不重开旧关闭记录。

完整身份与工具检查见 [validation-result.json](validation-result.json)；实际读取与复用记录见 [read-ledger.json](read-ledger.json)，审者和固定输入见 [identity.json](identity.json)。主审仍为 thread `01a130d7-7e94-7407-a89d-ef57dbfa6021`，独立于作者；辅助 actual 握手审者为 `01a130da-7748-76e1-ac35-691f6bb6d03a`。请求 sol/ultra/default/Fast=false，实际模型/推理/tier/Fast 回显 **UNVERIFIED**；未审计后台或额度。

本次 **NOT_EXECUTED_THIS_UPDATE**：新增参考、模型、宿主/Demo执行均0。第四review原历史4条（M01一次、M02两次、M12一次）按原有限资格保留，未重跑、未作为M03实际执行。Git/JSON/路径/完整字节检查只是 TOOL_VALIDATION；真实地图、媒体、像素、宿主继续时机、Demo与外部覆写仍未证。未来异常兼容政策未代选。

本报告只写独立分支的本批 `review/actual-v1/`。正式、作者、公共台账/main及他人证据未修改；未登记 ACCEPTED_SCOPED/CLOSED。ACTUAL_PASS_SCOPED 仅是唯一登记员后续接受的前提，后续次序与 U06 门保持。报告提交及后继发布回执的 commit/tree 由完整远端读回和最终回应绑定。
