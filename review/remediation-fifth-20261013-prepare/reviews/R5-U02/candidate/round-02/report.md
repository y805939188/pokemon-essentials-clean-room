# R5-U02 v2 非作者有限复验 · round-02

**限定候选 PASS：两项返修 PASS，其余12项复用原未变限定 PASS。** 46条必修静态结论均支持，JXN STATIC-03原FAIL与M03-007消费者/同步原FAIL已修复。没有新的必修返修阻塞；**R5-U01 actual接受依赖仍WAIT**，不签actual、正式接受或CLOSED。

## 固定输入、范围与身份

| 输入 | commit | tree |
| --- | --- | --- |
| v2候选 | `44a533fbf98ed5cee185a87f46bcd517bc1d5765` | `3464b82a43c6827029822a91b4ca52adf0df2c78` |
| v2作者证据 | `c6455ef13e5e6d74bc91ecd167534c85167955fa` | `a255d79769429d9cf8717da899f689950cc071a5` |
| 原round-01独立复审 | `4a6e11ca2ad84b53ff2faab8f3b6eb98c5a87b64` | `fd345f68daed91f6e4c6afa545424fca9fd31bd4` |
| 冻结合同 | `22fba7786b0090a1955ce6211315b0036cddfbcd` | `21f3484d167d8cab7a288e0204c72f275414d52e` |

B5与R仍为 `9366d9d17aaeac3b4414236468affa650fb3dd27`、`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。本轮入口为固定证据提交的 `candidates/R5-U02/author/revision-receipt.json`；回执用于导航，全部结论另以实际差异、必要原证据和直接源阅读核定。

原独立审者任务 `/root` 延续有限复验，非作者；分审 `/root/event_identity_review`、`/root/movement_fishing_review` 与 `/root/integrity_replay_review` 分别复核两项修复和载荷。请求 `gpt-6.1-sol / ultra / default（普速，禁Fast）`，实际模型/推理/服务档未回显，均为 **UNVERIFIED**；未检查额度或认证。

用户本次明确授权round-02，覆盖冻结入口原round-01的写入路径限定。原报告保留，不把原候选FAIL改写成历史PASS。只新增本review域六个文件；v2从固定Git对象读取到临时目录，未改作者、正式、公共登记、参考、冻结合同/main，未操作Mac，未重开全局review。

候选44a内继承了v1作者元数据（含旧向量数73）。本轮使用证据c645的新清单绑定候选实际规格载荷；两个commit及所有文件身份分别记录，旧候选元数据不作为v2自证。候选规格/片段/向量/编辑/补丁字节在44a→c645未变。

## 两项有限复验

**GR5-JXN-001：PASS。** NAME02三分支分别给出无大写占位Town、无玩家且无预览、只用通用消息显示的独立前提，不再套NAME01共同成功条件。NAME07明确A在名称选择/替换前失败且不要求查找成功；B成功展开后UI失败不回滚共享材料；C首次缺中、展开后的Alice键命中Town，改Bob后按新键返回Town。定位：engine共享载体第71/75行，独立B5投影第549/553行；派生向量、edits及补丁对应载荷相等。

直接核固定R lookup→selected text→substitution与消息先复制输入的必要锚点；普通Alice/Bob、命中层、无别名/中途改写、预览及后续显式保存的原边界保留。6条静态验收支持，正确WP11/WP08/WP65/UI目录字节未变。失败A只签给定“替换前失败”的条件，不扩为所有畸形输入或未来兼容政策。最小返修为空。

**GR5-M03-007：PASS。** WP60第30/62/64、84、100/101、108行已区分循环产生返回值与消费结果的入口。固定R钓鱼等待只写count并返回true/false；普通三支鱼竿回调才在true后写battles，再请求该竿遭遇。新的FS05明确直接正常成功：count＋1、battles不变、请求0；FS06明确普通OldRod/快捷回调成功：count＋1、battles＋1、再请求一次，物品整体true。两个例均固定正常资源/时钟/输入/清理、正ID立即结束公共事件、无额外脚本/公共事件统计或遭遇写入；一次请求不保证战斗或胜利。

旧FS04/15补普通物品消费者限定，保留正确成功与候选空的已提交battles边界。FS14/16与R5-FS01～04不变；开始/结束两个公共事件接收者、普通false/取消不消费battles或请求、正常共同清理、异常不保证回滚/清理，以及调用者额外主动消费的边界均保留。3条mandatory static及消费者、成对向量、结果边界、同步5项检查PASS。最小返修为空。

## 逐项裁决与12项签名复用

| 必修 ID | 限定结论 | 签名来源 |
| --- | --- | --- |
| GR5-JXN-001 | PASS | 本轮有限复验 |
| GR5-M03-001 | PASS | 复用原未变限定签名 |
| GR5-M03-002 | PASS | 复用原未变限定签名 |
| GR5-M03-003 | PASS | 复用原未变限定签名 |
| GR5-M03-004 | PASS | 复用原未变限定签名 |
| GR5-M03-005 | PASS | 复用原未变限定签名 |
| GR5-M03-006 | PASS | 复用原未变限定签名 |
| GR5-M03-007 | PASS | 本轮有限复验 |
| GR5-M03-008 | PASS | 复用原未变限定签名 |
| GR5-M03-009 | PASS | 复用原未变限定签名 |
| GR5-M03-010 | PASS | 复用原未变限定签名 |
| GR5-M03-011 | PASS | 复用原未变限定签名 |
| GR5-M03-012 | PASS | 复用原未变限定签名 |
| GR5-M03-013 | PASS | 复用原未变限定签名 |

[criterion-results.json](criterion-results.json)列两项逐条验收及原12项的固定review文件、pointer、record hash和受审范围。未变37条静态验收复用原记录；两项涉及9条静态验收，本轮只修复指定前提/消费者缺口并保留其已有支持，不重做其余12项。

复用由实际内容证明：12个原独立PASS记录的canonical SHA256、12作者响应、各限定操作/向量与混合目录的单项旧行内容一致。F063共享整段因两NAME行和新增FS05/06改变；旧末行新增分隔换行单列，不把共享整文件或整个新tree自动转签。其余14镜像/载体及14投影完整字节不变；只钓鱼正文与engine目录两个目标变化。精确旧owner/scope与历史关系沿round-01固定文件/pointer复用，没有新给旧全项签名或改状态。

## 载荷与重放证据

102项有限工具检查全部PASS，原286项未重跑。31个候选文件、32个证据文件身份分开核；实际75个向量＝73个旧记录加FS05/06，仅NAME02/07已有记录改变。74个编辑中的原F030/F063发生限定改变，新F067～074属于冻结007的两文件权限；8共享目标的18片段及marker/锚点一致。

按B5完整字节和新edits独立重构16投影，在隔离临时仓库检查并重放formal-diff.patch，所有目标与独立投影逐字节相等、命令退出0。没有以作者脚本或作者“已修复”表批准。完整新载荷、原未变身份、独立工具驱动、命令与结果见 [independent-validation.json](independent-validation.json)；读取与回归关系见 [source-reading-log.json](source-reading-log.json)、[regression-results.json](regression-results.json)。

## 执行与发布边界

| 分栏 | 执行记录 |
| --- | --- |
| R4历史 | 4；既有回执身份复用，未重跑 |
| R5全局review历史 | 4个隔离参考执行记录；不当作case/进程数 |
| 本update / v2有限复验新增 | 参考、行为模型、原生宿主、Demo均0 |

75个向量及FS05/06为DERIVED_VECTOR / NOT_EXECUTED；字节、hash、清单、锚点、补丁与签名复用检查为TOOL_VALIDATION。宿主/地图/CommonEvents/媒体、无界插件、原保留不确定性及optional/no-required/政策隔离沿v1，未扩必修范围。

只普通推送本round-02报告。报告commit/tree及全部六个新增文件完整bytes/SHA256/blob的远端读回由提交后的外部回执绑定；review-manifest不自引用。本候选PASS不等于actual/接受/关闭，依赖R5-U01保持WAIT。
