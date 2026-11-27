# 静态测试目录

按规则与输入前提选取案例。同一短 ID 可在不同族中出现。下表保留基础目录的范围，打开条目可见各案例的输入、边界与跨功能预期。

| 目录 | 基础案例范围 |
| --- | --- |
| [世界绘制与过渡](world-rendering-and-transitions.md) | WR01–WR17、BT01–BT17；B04-W01–B04-W24、XC-L01–L10/B01–B05/D01–D06/P01–P08/T01–T05 |
| [配置、身份与编译](configuration-content-and-compilation.md) | KC01–KC06、KR01–KR13、KL01–KL32 |
| [地图、移动、事件与场地操作](maps-movement-events-and-field-actions.md) | MP01–MP27、MV01–MV77、EV01–EV39、FW01–FW07、IM01–IM41、MR01–MR17、DG01–DG43、RS01–RS20、WT01–WT44、FS01–FS18；B04-R01–B04-R28 |
| [扩展、本地化与存档](extensions-localization-and-persistence.md) | EP01–EP21、TM01–TM14、IO01–IO15、DP01–DP05、LZ01–LZ17、SV01–SV11、MG01–MG16 |
| [能力、形态、暗影与遗传](attributes-forms-shadow-and-inheritance.md) | ST01–ST67、FM01–FM43、ME01–ME26、SH01–SH52、BR01–BR26 |
| [进化、漫游与捕获](evolution-roaming-and-capture.md) | BE01–BE37、CX01–CX42、RM01–RM37、CP01–CP24 |
| [战斗计算与效果](battle-calculations-and-effects.md) | TD01–TD21、SS01–SS40、MH01–MH38、AB01–AB23、HI01–HI33 |
| [大会、回程、图鉴与小游戏](field-contests-blackout-dex-and-games.md) | SF01–SF34、BP01–BP20、FP01–FP35、PD01–PD25、VF01–VF18、LT01–LT16 |
| [身份、队伍与获得](identity-party-and-acquisition.md) | CI01–CI28、HP01–HP45、PT01–PT69、PS01–PS42、AQ01–AQ36 |
| [背包、成长与寄养](inventory-growth-and-daycare.md) | BG01–BG31、IU01–IU59、SH01–SH28、GR01–GR53、DC01–DC20 |
| [蛋、遭遇、租借、邮件与卡牌](eggs-encounters-rentals-mail-and-cards.md) | EG01–EG20、EN01–EN32、FC01–FC17、MG01–MG30、TT01–TT24 |
| [回合、参战者与终局](turns-participants-and-outcomes.md) | BC01–BC25、CM01–CM33、SW01–SW29、G01–G13/R01–R11/E01–E14＋E07b/E08b/E09b、W01–W07/T01–T04/F01–F03/S01–S07/H01–H04/P01–P05/C01 |
| [招式目标、控制与物品](move-targets-control-and-items.md) | MA（A01–A10/T01–T06/P01–P03/C01–C10）、SB（S01–S07/B01–B05/C01–C05/I01–I15/A01–A06） |
| [特性触发与战斗决策](ability-triggers-and-battle-ai.md) | AB（L01–L08/H01–H03/D01–D08/E01–E07/F01–F05）、AI（A01–A04/S01–S07/I01–I05/M01–M09）、AE（A01–A10/N01–N11＋N02b–d/G01–G12/S01–S11/T01–T07/F01–F02）、BE（B01–B60＋B04b/B04c/B12b）、CE（C01–C55） |
| [参赛资格、设施与回放](entry-facilities-and-replays.md) | QC（Q01–Q42）、WS（W01–W34）、PA（P01–P27）、RC（W01–W23＋W22b） |
| [菜单、演出与小游戏](menus-presentations-and-minigames.md) | MG（28）、DT（8）；B04-M01–M18/I01–I04/D01–D04、PG（P01–P33）、NV（T01–T36＋T06b/T25b/T34b）、CH（5）、TC（8）、PT（A01–A41）、BX（B01–B39）、BG（C01–C36）、BT（K01–K59）、LC（L01–L35）、DU（D01–D12）、SL（S01–S16）、MN（M01–M22）、TP（T01–T21） |
| [编辑、转换与示例范围](authoring-and-demo-coverage.md) | DG（M01–M30）、CE（M01–M20）、WE（M01–M22）、AN（M01–M33）、CV（M01–M30）、GN（M01–M24）、DM（M01–M16） |

## 参考版本的条件与跨域案例

- [注册道具、空值和假值](creature-compatibility-controls.md)
- [跨功能边界场景](cross-domain-contrasts.md)
- [跨域顺序和部分失败的静态案例](cross-domain-scenarios.json)
- [进化 · 30 个方法 × 6 种入口 × 16 个边界](evolution-integer-boundaries.csv)
- [战斗与场地效果](qualified/battle-and-field-effects.json)
- [战斗与奖励结算](qualified/battle-and-rewards.json)
- [行动顺序与失败](qualified/battle-order-and-failures.json)
- [战斗演出](qualified/battle-presentation.json)
- [内容输入、保存及失败](qualified/content-io.json)
- [遭遇与场地效果](qualified/encounter-and-field-effects.json)
- [遭遇进入战斗](qualified/encounter-to-battle.json)
- [成长与场地效果](qualified/growth-and-field-effects.json)
- [道具使用与演出](qualified/items-and-presentation.json)
- [地图移动与时间](qualified/map-movement-and-time.json)
- [地图时序与恢复](qualified/map-timing-and-recovery.json)
- [玩家状态与计步](qualified/player-and-step-effects.json)
- [天气与演出](qualified/weather-and-presentation.json)
- [世界时间与状态](qualified/world-time-and-state.json)
- [参考行为的前提、边界和反例](reference-boundary-cases.json)

## 可选兼容条件的静态对照

- [颜色、工具、评分与资源操作](conditional-behavior-examples.json)
- [可选兼容对照](optional-compatibility-observations.md)

## 可移植规则与验收

- [独立框架的存档、领取、世界与战斗用例](portable-framework-cases.json)
- [可移植规则的静态验收](portable-expectations.md)
- [可移植行为 · 38 条 JSON 静态预期](portable.json)

[适用范围与证据等级](../reference/scope-and-evidence.md) · [任务入口](../README.md)
