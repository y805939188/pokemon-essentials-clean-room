# 静态测试目录索引（WP80 净化规格集）

本目录按「分类/包」组织静态推导场景条目。每条记录：**ID、输入／前提、推导预期**——全部为静态推导，**不是已执行测试**；素材、宿主输出与运行表现按 `../scope-statement.md` 保留。

## 目录

| 文件 | 覆盖 | 条目 | 对应净化正文 |
| --- | --- | --- | --- |
| [engine-overworld-wp16.md](engine-overworld-wp16.md) | 世界绘制与视觉过渡＋战前过渡（批次 1，v2 修正后） | WR01–WR17、BT01–BT16 | `engine-overworld/wp16-world-rendering-and-visual-transitions.md`、`engine-overworld/wp16-pre-battle-transitions.md` |
| [generic-kernel-wp02-03-04.md](generic-kernel-wp02-03-04.md) | 规则配置档案＋内容身份/schema＋PBS 生命周期（批次 2） | KC01–KC06、KR01–KR13、KL01–KL32 | `generic-kernel/wp02-rule-configuration-and-data-variants.md`、`generic-kernel/wp03-content-identity-and-schema.md`、`generic-kernel/wp04-pbs-lifecycle.md` |
| [engine-overworld-wp11-15-59-60.md](engine-overworld-wp11-15-59-60.md) | 地图拓扑/地形运动/事件与跟随（含两矩阵）/随机地牢/资源与音频/时间天气场地/钓鱼（批次 3） | MP01–MP27、MV01–MV77、EV01–EV39、FW01–FW07、IM01–IM41、MR01–MR17、DG01–DG43、RS01–RS20、WT01–WT25、FS01–FS15 | `engine-overworld/` 下 WP11–WP15、WP59、WP60 九篇 |
| [generic-kernel-wp05-06-07-08-09-10.md](generic-kernel-wp05-06-07-08-09-10.md) | 通知扩展插件/时间随机计步统计/诊断文件 HTTP/弃用告警/本地化/保存启动/迁移恢复（批次 4） | EP01–EP21、TM01–TM14、IO01–IO15、DP01–DP05、LZ01–LZ17、SV01–SV11、MG01–MG16 | `generic-kernel/` 下 WP05–WP10 八篇（WP01 为基线范围承接，无行为场景） |
| [pokemon-rules-wp19-21-22-23-34.md](pokemon-rules-wp19-21-22-23-34.md) | 属性与能力/动态形态/Mega 与 Primal/Shadow 与净化/遗传（批次 5） | ST01–ST67、FM01–FM43、ME01–ME26、SH01–SH52、BR01–BR25 | `pokemon-rules/` 下 WP19、WP21、WP22（含附表）、WP23（含附表）、WP34 七篇 |
| [pokemon-rules-wp31-32-37-38.md](pokemon-rules-wp31-32-37-38.md) | 基础进化/情境交换战后事件/漫游与雷达/捕获与接收（批次 6） | BE01–BE35、CX01–CX38、RM01–RM32、CP01–CP20 | `pokemon-rules/` 下 WP31、WP32（含附表）、WP37、WP38 五篇 |
| [pokemon-rules-wp43-44-46-48-50.md](pokemon-rules-wp43-44-46-48-50.md) | 类型命中伤害/状态与阶级/多击特殊伤害恢复/特性计算/持物触发消耗（批次 7） | TD01–TD21、SS01–SS40、MH01–MH38、AB01–AB23、HI01–HI33 | `pokemon-rules/` 下 WP43、WP44（含附表）、WP46（含附表）、WP48、WP50（含附表）八篇 |
| [pokemon-rules-wp53-60-61-62-69-70.md](pokemon-rules-wp53-60-61-62-69-70.md) | Safari 与捕虫/树果/野外被动与回程/图鉴/Voltorb Flip/Lottery（批次 8） | SF01–SF34、BP01–BP17、FP01–FP31、PD01–PD25、VF01–VF18、LT01–LT16 | `pokemon-rules/` 下 WP53、WP60、WP61、WP62、WP69（含附表）、WP70 七篇 |
| [creature-rpg-wp18-20-24-25-26.md](creature-rpg-wp18-20-24-25-26.md) | 生物身份物种与拥有者/HP 异常招式与持有/玩家训练家与伙伴/队伍与盒子/获得赠送与脚本交换（批次 9a） | CI01–CI28、HP01–HP45、PT01–PT69、PS01–PS42、AQ01–AQ36 | `creature-rpg/` 下 WP18、WP20、WP24、WP25、WP26 五篇 |
| [creature-rpg-wp27-28-29-30-33.md](creature-rpg-wp27-28-29-30-33.md) | 背包与物品储存/主动道具与培养教学/买卖与 BP 商店/成长学习与友好/寄养会话与兼容性（批次 9b） | BG01–BG31、IU01–IU48、SH01–SH26、GR01–GR44、DC01–DC20 | `creature-rpg/` 下 WP27、WP28、WP29、WP30、WP33 五篇 |
| [creature-rpg-wp35-36-57-64-68.md](creature-rpg-wp35-36-57-64-68.md) | 蛋与孵化/普通遭遇与修正/Factory 租借换队/邮件与神秘礼物/Triple Triad（批次 9c） | EG01–EG19、EN01–EN24、FC01–FC17、MG01–MG30、TT01–TT24 | `creature-rpg/` 下 WP35、WP36、WP57、WP64、WP68 五篇 |
| [combat-requirements-wp39-40-41-42-45.md](combat-requirements-wp39-40-41-42-45.md) | 战斗上下文与参与者/命令服从与行动顺序/换人位置与逃跑/成长回合末与终局/天气场地阵营与位置效果（批次 10） | BC01–BC18、CM01–CM29、SW01–SW27、G01–G10/R01–R08/E01–E13＋E07b/E08b/E09b、W01–W07/T01–T04/F01–F03/S01–S07/H01–H04/P01–P05/C01 | `combat-requirements/` 下 WP39、WP40、WP41、WP42、WP45 五篇 |
| [combat-requirements-wp47-ab.md](combat-requirements-wp47-ab.md) | 招式属性目标与复制调用/招式换人控制与物品变化（批次 11） | MA（A01–A10/T01–T06/P01–P03/C01–C10）、SB（S01–S07/B01–B05/C01–C05/I01–I15/A01–A06） | `combat-requirements/` 下 WP47-A、WP47-B 四篇（含两数据附表） |
| [combat-requirements-wp49-51-52.md](combat-requirements-wp49-51-52.md) | 特性阶段触发/AI 动作选择与技能/AI 通用数值与状态评估/AI 场域伤害恢复与多目标评估/AI 物品调用与行动控制评估（批次 12） | AB（L01–L08/H01–H03/D01–D08/E01–E07/F01–F05）、AI（A01–A04/S01–S07/I01–I05/M01–M09）、AE（A01–A10/N01–N11＋N02b–d/G01–G12/S01–S11/T01–T07/F01–F02）、BE（B01–B60＋B04b/B04c/B12b）、CE（C01–C55） | `combat-requirements/` 下 WP49、WP51（含附表）、WP52-A/B/C 九篇（含四数据附表） |
| [combat-requirements-wp54-55-56-58.md](combat-requirements-wp54-55-56-58.md) | 参赛资格等级调整与杯赛条款/设施基础会话/Palace 与 Arena 变体/战斗记录与回放（批次 13） | QC（Q01–Q42）、WS（W01–W34）、PA（P01–P27）、RC（W01–W23＋W22b） | `combat-requirements/` 下 WP54（含附表）、WP55、WP56、WP58 五篇 |
| [user-interface-wp17-63-65-66-67-68-69-70-71.md](user-interface-wp17-63-65-66-67-68-69-70-71.md) | 消息窗口与输入/宝可齿轮/主导航（含两附页）/队伍摘要/盒子图鉴/背包商店/战斗交互/生命周期演出/决斗/老虎机/挖矿/板块拼图（批次 14） | MG（27）、DT（8）、PG（P01–P33）、NV（T01–T36＋T06b/T25b/T34b）、CH（5）、TC（8）、PT（A01–A41）、BX（B01–B39）、BG（C01–C36）、BT（K01–K59）、LC（L01–L35）、DU（D01–D12）、SL（S01–S16）、MN（M01–M22）、TP（T01–T21） | `user-interface/` 下 WP17（含附表）、WP63、WP65（含两附页）、WP66-A/B/C、WP67-A/B、WP68、WP69（含附表）、WP70（含附表）、WP71 十七篇 |
| [demo-dx-wp72-73-74-75-76-77.md](demo-dx-wp72-73-74-75-76-77.md) | 调试上下文与控制台/内容编辑器/世界编辑器/战斗动画制作与交换/工程转换与作者工具/设施内容生成与模拟/示例工程证据与能力覆盖（批次 15） | DG（M01–M30）、CE（M01–M20）、WE（M01–M22）、AN（M01–M33）、CV（M01–M30）、GN（M01–M24）、DM（M01–M16） | `demo-dx/` 下 WP72、WP73-A、WP73-B、WP74、WP75、WP76、WP77 七篇 |

## 使用约定

- 条目 ID 在净化正文中引用（正文 §示例场景 指向本目录）。
- 预期列为静态推导：实现方据此设计可执行测试时，环境前提（素材存在性、宿主行为）须单独验证。
- 目录条目与正文同步维护；新增/修订条目需在对应批次检查记录中登记。

## 历史 B01-G 目录登记（93d 时点原文保留）

B01 当前目录登记：两份相关目录分别 51、87 条，共 138 条；相对 PRE0 新增 20 个 ID，仅原 KL10／EP07／EP08 行有修订。共享 WP05–10 目录的非 EP 行保持原字节。候选的本批相关条款／向量已获有界 PASS_SCOPED，本次索引新字节待整合核验；条目均未运行，其他批次条目不因这次计数登记获批。见 [整合交接](../../../review/remediation/20261003-prepare/final-integration-review.md)。

## B02-G 当前目录登记（待整合 Ultra）

共享 WP05–10 目录当前 99 行：EP21、TM14、IO15、DP5、LZ17、SV11、MG16；相对已接受上游新增 12 个 ID，修订 12 条本批旧行，无删除。B01 EP01–EP21 与 DP 整段原字节保留；另一 B01 目录 51 行保持，两目录当前合计 150（历史 B01-G 合计 138）。WP07/08/10 原稿场景当前为 14/17/16，新增 2/3/4 条，共 9；这些是未执行静态场景数，不是行为覆盖或运行数。B01 实际核验已接受；B02 独立结论只绑定候选，本次索引新字节待 R-B02 整合核验。详见 [B02 当前计数](../../../review/remediation/20261003-prepare/batches/B02/integration-stage-1/scope-counts.json)。

## B05-G 当前目录登记（待实际整合 Ultra）

仅更新本批两个表项范围：CI28/HP45/PT28/PS28/AQ35，共164行；ST67/FM43/ME26/SH52/BR25，共213行。相对B02接受基线，两目录339→377行，新增38条；既有行只修订FM15/FM20/SH06，无删除。PT/PS/AQ和BR整个尾段原字节保留；B01/B02共享WP05–10目录仍99行、另一B01目录51行及EP/DP保留，旧索引登记段继续保留其原时点。

上述为未执行静态文本目录计数。完整候选十五文件含五原稿批准同步，候选R-B05已给16项贡献PASS_SCOPED；本次索引及新实际integration SHA仍待Ultra。131份最终Markdown与17个静态目录文件数量不变，B07/B16/B17尚待其自身贡献。详见 [B05限定计数](../../../review/remediation/20261003-prepare/batches/B05/integration-stage-1/scope-counts.json)。

## B03-G 当前目录登记（实际整合待 Ultra）

本批范围为MP27/MV77/EV39/FW7/IM41/MR17/DG43，共251条未执行静态向量；相对B02冻结原139条新增112，第二轮新增16，旧235行逐字保留。共享文件另有RS20/WT25/FS15共60条，整文件311条；不把251当整文件总数。H节起WP15/59/60尾部原字节保留，A–G仅本批具名行和表结构。

候选第二轮27贡献局部通过；本次索引/实际新SHA仍待Ultra，B04/B14整文件锁和陈旧读取门继续有效。131份最终Markdown及17个静态目录文件不变；数字仅文本库存。见 [计数](../../../review/remediation/20261003-prepare/batches/B03/integration-stage-1/scope-counts.json)。

## B06-G 当前目录登记（实际整合待 Ultra）

B06两目录当前CI28/HP45/PT69/PS42/AQ36＝220行，BG31/IU48/SH26/GR44/DC20＝169行，合计389；接受基线合计331，新增58行，既有仅PS11/AQ04获准修订，无删除。本批分配60静态行（其中原两行修订）＝七项25＋新增35，不能把60当整文件总数或执行次数。B05 CI/HP及第二目录IU/SH/GR/DC整段保持，WP26/WP66-B原与净化正文保持。本批8份正式候选局部通过；索引新字节／实际新SHA待R-B06 Ultra，目录全文件锁保持。见 [计数](../../../review/remediation/20261003-prepare/batches/B06/integration-stage-1/scope-counts.json)。旧登记段为历史时点，原字节保留。
