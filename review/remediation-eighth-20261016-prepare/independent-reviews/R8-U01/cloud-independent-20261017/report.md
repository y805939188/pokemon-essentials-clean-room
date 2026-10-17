# R8-U01 独立完整候选复审

结论：三项正文静态语义均 **PASS**；完整候选交接证据 **FAIL**，需修正一项精确定位后重新冻结证据。该问题不推翻正文修正，不是新增行为根或新业务测试要求。

| 对象 | 判定 | 有限范围 |
| --- | --- | --- |
| GR8-KER-001 | PASS | 有序删除、失败前缀及下次主档存在门 |
| GR8-KER-002 | PASS | 成功读取结果的空/非空装配门及后续分层 |
| 已选择 GR8-UI-001 | PASS | 普通保存拒绝仅澄清为不调用持久层保存 |
| 完整交接证据 | FAIL | KER002 的 WP09 行号/章节/锚点指向未改位置 |

## 固定对象与独立性

- 仓库：`y805939188/pokemon-essentials-clean-room`。
- 完整候选：`bce1659e01ca33ecafb91464ce1ada32c0499faf`；tree：`c7456f86bf3c1e7a00f2b3faf55bf75a1b4d6f7b`；作者分支：`revision/r8-u01-20261017`。
- 作者输入：`4575e80d041ab0c74a42e2e36399d05791dbaa5b`；B8：`fd1df570cad987dc3852a3b958f03916e317f7fe`。
- 只读参考：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；四 mirror 的原载荷提交：`06c5bc45974d2958cd7ba60fa171e07cb6515dd7`。
- 语义 core：`2460370f1e410bd49cc29e377b89662838aed2b3`。原合同来源 `5caff3bd1a1b062b48b7eda46777a614921946f3` 与 C35 恢复路径分别保留，不把全部历史事实改写为 C35 原生。
- 本次是用户另行委派的非作者复审上下文；主审 `/root`，辅助只读任务为 `/root/ker001`、`/root/ker002`、`/root/ui001`、`/root/readset_history`、`/root/evidence_audit`。这些是本次五个辅助任务，不计作五张独立最终验收票。作者未参与裁决；审者未改候选。
- 请求配置为 gpt-6.1-sol / ultra / default / normal / Fast off；actual model、effort、tier、speed、Fast 和当前实际任务 UUID 无权威 echo，逐项 **UNVERIFIED**。来源线程与协调 ID 只作路由，不冒充审者 UUID。
- 当前用户明确采用 UI001，覆盖冻结旧 prompt 的 UNSELECTED/未启动状态；其 optional 历史分类保持，其余九项 optional 与独立视觉 policy 不在本批采用范围。

## 唯一发现：WP09 精确定位错位

**R8-U01-REVIEW-LOC-01，P3，证据交接缺陷。**

[remediation-record.json L628–629](https://github.com/y805939188/pokemon-essentials-clean-room/blob/bce1659e01ca33ecafb91464ce1ada32c0499faf/review/remediation-eighth-20261016-prepare/candidates/R8-U01/evidence/remediation-record.json#L628) 的 `/records/1/change_locations/0` 写成 WP09 第 33 行；[tagging-handoff.json L49–53](https://github.com/y805939188/pokemon-essentials-clean-room/blob/bce1659e01ca33ecafb91464ce1ada32c0499faf/review/remediation-eighth-20261016-prepare/candidates/R8-U01/evidence/tagging-handoff.json#L49) 的 `/changes/4` 还指定 §3.1“登记机制”与 `#31-登记机制`。第 33 行是未修改的登记配置说明，同名 locator 能命中错误位置。

实际 KER002 修订位于 [WP09 L102](https://github.com/y805939188/pokemon-essentials-clean-room/blob/bce1659e01ca33ecafb91464ce1ada32c0499faf/review/remediation-eighth-20261016-prepare/candidates/R8-U01/mirror/deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md#L102)，所属标题在 L97：§4.1“启动阶段表”。四份真实差异和原完整合同均支持这一位置。照当前交接直接打标会把行为变化贴到未改的配置行，遗漏真正的装配期修订。

最小修复：由候选证据作者将两处行号改为 102；tagging 章节改为 `4.1 启动阶段表`、锚点改为 `#41-启动阶段表`；两处 locator 宜扩为唯一前缀 `| 启动读取 | 先检查默认主档：`。无需改四个 mirror、正式规格、目录场景或历史根。修正后重新冻结证据，并独立核对该小差异及四 mirror 身份即可。

最强反方：正确正文、原合同及 diff 已足以恢复真位置，因此这不阻断三项行为判定。该反方成立，故三项正文仍 PASS；但本次明确检查完整候选、引用与可直接消费的打标交接，不能把两份错误定位判为准确。此 FAIL 只阻完整证据交接的无保留 PASS，不宣称业务修订失败。

## GR8-KER-001：PASS

独立源链为参考 `001_SaveData.rb` L15–17、L65–68，`013_UI_Load.rb` L216–279、L298–300，及 `999_Main.rb` L25–41。删除先完成 P，再检查/删除单个相邻 P.bak；第一步异常不会检查备份。下一次载入构造先查 P，孤立备份不经此门自动发现。

候选 [WP10 L228–246](https://github.com/y805939188/pokemon-essentials-clean-room/blob/bce1659e01ca33ecafb91464ce1ada32c0499faf/review/remediation-eighth-20261016-prepare/candidates/R8-U01/mirror/deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md#L228)、[WP09 L139](https://github.com/y805939188/pokemon-essentials-clean-room/blob/bce1659e01ca33ecafb91464ce1ada32c0499faf/review/remediation-eighth-20261016-prepare/candidates/R8-U01/mirror/deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md#L139) 和目录 L293–307 一致覆盖五类控制：任次拒绝、双成功、第一步失败且未删 P、第二步失败且未删 P.bak、无备份。每例分别给文件状态与 UI 请求。第二步失败留下 P 无/P.bak 在；正常失败提示后回标题，下次主档门为假，普通菜单无继续项。

无效档删除提示另列：拒绝产生退出信号；同意后即使系统调用错误被正常处理，仍重置两个系统对象并返回空数据。提示失败或非捕获异常不保证后继；回标题与重新执行全新进程装配分开。递归备份读取不扩展成递归删除，既有 UI 不重试/不回滚及紧急保存规则保持。

最强反方是“UI 已有部分失败和不回滚，顺序补记多余”。通用条款不能确定留下哪个文件；有序前缀决定下一主档门，因此本次必要补记成立。候选没有替用户选择未来原子性政策，也未声称真实故障已复现。

## GR8-KER-002：PASS

参考 `001_StartGame.rb` L21–35，`001_SaveData.rb` L24–50、L73–80，`002_SaveData_Value.rb` L97–100、L213–267，及全部 17 个默认登记共同支持结果门。全新未加载标记、无旧格式提取/插件、恰两种有效语言及正常依赖下：

| 输入 | 系统装配时结果 |
| --- | --- |
| 无主档 | 空表，初始化五类启动值，请求语言选择 |
| 现存可读单个非表对象后 EOF 的旧序列 | 适配空表；跳过转换、转换备份和写回；仍初始化并请求语言选择 |
| 有效当前版本非空档 | 加载启动值，跳过启动选择，按已存索引请求消息 |

候选 WP09 L102 与 WP65 L27 正确改正两处穷尽二分；目录 L311–324 的八行控制保持全新进程、默认 17 项和两语言前提。默认语言列表仍为空，两语言是显式变体。

后续 `013_UI_Load.rb` L216–252、L281–341 的有效性/递归备份/删除逻辑独立保留：原主档仍在且再次适配为空时，默认有效性为假；无备份拒绝删除退出，同意且收尾成功才到无继续菜单；有效备份可使最终菜单显示继续。语言 BACK 由 `Utilities.rb` L603–609 与 `Messages.rb` L721–755 的默认取消哨兵 0 支持；读取/解码抛错不冒充成功空表。

最强反方是“启动空表就必定进入无继续菜单”，以及“删除失败必定阻止重置”。候选 WP10 L246、目录 L307、L316–320 明确区分两者，未作这种过强推断。WP08 的空性门、SV02 调试三门、LZ13/14、UI65 后继链和 WP02/KC05 无文件充分示例保持。

## GR8-UI-001：PASS

[候选 WP65 L88](https://github.com/y805939188/pokemon-essentials-clean-room/blob/bce1659e01ca33ecafb91464ce1ada32c0499faf/review/remediation-eighth-20261016-prepare/candidates/R8-U01/mirror/deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md#L88) 仅把普通 No 括注澄清为“不调用持久层保存”。选择音、false、正常收尾和同节 L90 确认前变化/保存失败不回滚均保留；没有新增命名规则、mandatory 根、UI 目录写集或强制向量。

参考 `014_UI_Save.rb` L39–72、L100–128 的信息窗先于确认；地图名经 `Game_Map.rb` L103–105、`Messages.rb` L245–263、`MapMetadata.rb` L121–125 读取；`Intl_Messages.rb` L600–612、L752–754、L768–770 的无命中路径可交出共享文本。合法可变未展开名称、game/core 的地图名域均空、普通 Alice 名字、无别名/其它写入且正常依赖等完整前提下，首次信息窗可先形成 Alice Place 的内存前缀，普通 No 不撤回。Town/已展开名称没有新替换；覆盖拒绝、保存 false 也保此前前缀，读后异常不保证收尾。真实 Demo 首次读取时机仍未证。

最强反方成立：原同节已写确认前变化不回滚，旧“无副作用”可以限于拒绝分支，因此原根只授 optional。当前采用忠实限于这一澄清。WP11 §5.3.1、NV T11–14、LZ 与 JXN-NAME05 各原前提完整保留。

## 全文、写集、身份与执行信用

主审完整读取四 mirror 及 reviewer-prompt 的三份完整合同；独立确认其 JSON 与 `contracts.zh.json /records/0,1,9` 完全相等。团队重新实际读取合同 21 个固定源/规格整文件，详见 [read-ledger.json](read-ledger.json)，没有借作者“FULL”授予本次读信用。相关根提案、完整反方、当前 canonical/history 与 mandatory companions 按 typed-purpose 接收；外域身份/导航不冒称全文语义审读。

主审重新从固定源/规格提交取得全部 21 个单位，独立计算 UTF-8 bytes、SHA256 和 Git blob SHA1，21/21 与合同一致。四 mirror 与四基线也独立重算一致。身份核验只是 TOOL_VALIDATION，不替代前述语义审查。

实际差异为 WP09 L102/L139 两行；WP65 L27/L88 两行；WP10 L228 替换并补 L230–246；同族目录只在原 46520 字节后追加。目录旧正文及历史场景完整保留，新增 13 个唯一 ID 与 record/tagging 一致。新增 WP09→WP10 §5.1.1 引用可解析；其它七个改动定位正确，唯一例外见本报告。

基线到候选比较为 ahead 3 / behind 0，共 35 个新增文件，全部在本批候选根内，mirror 恰四个。正式 deliverables、audit、planning、AGENTS、旧报告、旧接受/关闭台账无本批改动。WP08、WP11 与 UI catalog 的固定全文及 blob 相等；其原场景与关闭资格未重开。

新增 13 行全部是 **SOURCE_STATIC / DERIVED_VECTOR，NOT_EXECUTED**。作者 57 项仅是文档 TOOL_VALIDATION；本复审未执行原 validator（它会覆写作者证据并硬编码作者分支），未执行 Ruby、独立业务模型、真实文件故障/旧档回放、游戏、原生宿主、像素/声音观察或 Demo。既有 7 数学/有限证书 + 1 环境探针、旧 PBS 原过程身份未证及其非额外过程资格原样保留；本次不增加这些运行信用。

执行环境在 container_creation 阶段失败（container_service_failed）。读取、独立文档计算和提交/分支发布通过已连接 GitHub 工具完成；没有本地 shell、git push 或 fresh clone 的执行回执。远端发布采用新 commit 加新分支/非 force 前进，再完整远端文件回读；实际证据见后继 [remote-readback.json](remote-readback.json)。

## 剩余依赖与门

1. 作者更正 R8-U01-REVIEW-LOC-01 的两份证据定位并重新冻结；独立核对小差异和四 mirror 保持后，才能给完整交接证据 PASS。
2. R8-INTEGRATOR 才能写正式目标/共享层；实际整合后须另读受影响整文件和累计保留、接收共享消费者与历史条件。
3. actual integrated PASS、ACCEPTED、CLOSED 本次均 **NOT_GRANTED**。候选静态语义 PASS 不等于实际整合或正式关闭，也不等于运行等价。
4. 语义前置批次直接/传递依赖均无；材料/宿主/未来兼容政策仍限原范围，不据本次静态结论授全系统通过。

报告只新增本批独占独立 review 证据。协调 `01a14a04-b178-7567-a4eb-0f0bfac9a0d9` 由父任务转交，本次未向他人发送外部消息。
