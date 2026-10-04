# 最终净化规格集（WP80；2026-10-03）

## 当前B04-G状态（实际整合待Ultra）

接受基线 `6452c0e03025605222f3de9a272221e2b82eeda4` 为 B01/B02/B03/B05/B06 五批。B04完整候选 `50f9ca2506bf0de21c33c644569c9987f84b80a3`、作者交接 `5da06e2baf0879978a871c6952fab1105909b511`、第二轮独立报告 `c500ed089fd1192409c1c77a7a91e093c59a8a45` 为35贡献／23主责 PASS_SCOPED；13份正式文件原字节整合。本次实际新SHA及全部公共／依赖登记待同一 R-B04 Ultra，未接受 B04。规范必修229 OPEN／0 CLOSED。

[当前交接](../../review/remediation/20261003-prepare/final-integration-review.md)、[逐ID与范围登记](../../review/remediation/20261003-prepare/batches/B04/integration-stage-1/finding-registration.json)、[返修历史](../../review/remediation/20261003-prepare/batches/B04/integration-stage-1/historical-repair-registration.json)、[候选报告](../../review/remediation/20261003-prepare/batches/B04/review-round-2/report.md)、[五读者接口](../../review/remediation/20261003-prepare/batches/B04/integration-stage-1/downstream-handshake.json)。ROOT002仅34具名静态场景（地点条10／灯光5／黑暗6／图片8／计时器5）限定后继；旧WP79 source-judgments NA/EXCLUDE原字节保留，未作实际事件／素材／文件全覆盖推断。C003仅本批C-04扩展，原根与全部八扩展及其他责任保持；C061/C062两P2返修归原根，不新增ID。

五批已接受主责52，具体原修订51满足／1缺具体消费／0证据不足，严格全贡献47／5；79已接受贡献记录／76触及ID保持原口径。差别A017、A034、C053、WP80-B02-R02保留，A024仍等B07；本批候选23主责及35条新候选记录不混入接受分母。

B07四计划读＋原WP17消息＝5，B06四计划读＋原WP15音频＝5均重冻结。B04→B07必须串行，actual Ultra及父任务C接受后才以精确后继重冻结B07；B07后续WP28/WP30反向变更必须受影响B04复核。B06 WP24§5.4/PT41–63六逻辑请求与引子记忆字节不变，伙伴／雷达及其余贡献不获额外接受。未派发任务。 参考程序、运行观察、已证Demo链、行为向量执行均0；容量1024/2048为条件夹具，缺文件抛错为具名宿主前提。以下旧层按各自冻结版本保留，旧批准不转授新字节。

## 当前 B06-G 状态（实际整合待 Ultra）

已接受上游为 B01/B02/B03/B05，固定 `1fd612d47dcda164de61ab2d25a1cb5e0fbde085`。B06完整十项候选 `4076a3fbbf6fe355b73f3fe2229d1f981fe735d2`、作者交接 `ee7461e90ad5e0943e39c56c22a080f761f4e1c0`、独立Ultra报告 `70babef632539c952aa988e7762d0c2aa19cfeb3`为本批10贡献／7主责 PASS_SCOPED；八份原／净化／目录字节原样整合，本次实际新SHA及公共登记待 R-B06 Ultra。规范必修229 OPEN／0 CLOSED。

当前入口：[整合交接](../../review/remediation/20261003-prepare/final-integration-review.md)、[B06具体登记](../../review/remediation/20261003-prepare/batches/B06/integration-stage-1/finding-registration.json)、[候选复审](../../review/remediation/20261003-prepare/batches/B06/review-full-round-1/report.md)、[下游合同](../../review/remediation/20261003-prepare/batches/B06/integration-stage-1/downstream-handshake.json)。A034/B08、A059/B04/B09/B17/B21、C103/B14、C120/B16继续OPEN；候选PASS与旧批准均不代替本次实际受影响复审。参考程序／运行观察／已证Demo链／行为向量执行均0。

以下既有正文和旧公共状态按其冻结版本保留；当前状态以本层及中央后继为准。

本目录是 Pokémon Essentials 净室行为规格项目的**最终净化交付物**（WP80 全集作者交付已完成，当前为全局审查后的整改阶段）。内容面向后续独立实现：全部正文以**独立行为文字**书写（目的、输入输出、条件、状态变化、数学规则、失败边界、场景与依赖），不含有意保留的参考实现标识（源方法名、源文件路径、宿主专有对象关系、历史修订叙述）——这些审计定位信息统一移至 [audit/source-traceability.md](../../audit/source-traceability.md)（来源追溯索引）。

## 目录结构

- `README.md`（本文件）——使用说明。
- `scope-statement.md`——范围与未验证声明（U01＋G01–G12、素材/demo/插件/运行未验证范围、20 项来源异常、证据层级口径；**使用本集前必读**）。
- `<分类>/`——净化后的行为正文，按项目既有分类组织：
  - `generic-kernel/`（通用内核：持久化、事件、配置、注册、诊断等）
  - `creature-rpg/`（通用生物收集 RPG：个体、队伍、储存、遭遇、成长等）
  - `pokemon-rules/`（宝可梦规则：能力数值、特性、类型、进化、图鉴等）
  - `combat-requirements/`（战斗需求：战斗流程、伤害、AI、设施等）
  - `engine-overworld/`（引擎/世界集成：地图、移动、绘制、天气、过渡等）
  - [user-interface/](user-interface/)（用户界面：场景、菜单、输入、画面流程等）
  - `demo-dx/`（示例与开发者体验：调试、编辑器、工具、demo 证据等）
- `test-catalog/`——静态测试目录：每条记录输入、前提与推导预期（**静态推导，不是已执行测试**；可用于后续实现的测试设计）。

## 使用说明

1. **先读** `scope-statement.md`：本集只覆盖静态可核对的行为规则；素材缺失、demo 事件链、运行观察、宿主输出与真实插件组合均为**未验证保留项**（已证 demo 事件链＝0、运行观察＝0），不得把静态合同当作运行通过证明。
2. 行为正文按分类与包组织；每篇末尾的「未决与未验证」列出该包具名保留项。
3. 每条规则可通过 `audit/source-traceability.md` 反查：批准的输入规格及身份、独立审查依据、参考文件及已读范围、证据层级、对应场景/向量——追溯索引是审计用途，行为正文可独立阅读。
4. 测试目录与本集正文一一对应（目录条目 ID 在正文中引用）；目录条目为静态推导预期，不承诺已在任何引擎上执行。
5. 本集**不构成**任何具体实现架构：不规定语言、类层级、渲染/战斗/引擎适配器的结构；数学规则与数据条件以独立表述给出。

## 当前整改状态

批次 1–15 的全集作者交付与最终全局独立review已完成；233个规范finding中229项必修仍全部OPEN。B01/B02/B05的有界实际整合已接受，最新冻结 `ae230e76e9c041f39c28948321d0960804c02388`。B03完整候选 `3c5728a47142c57abfdf3d55033768bc44a1f627`由第二轮独立报告 `a69d6e057723cc8f8aec8cac0f868da4e456d0eb`给出27贡献/19主责PASS_SCOPED，十三正式文件原字节整合；本次实际新SHA、公共登记和索引待R-B03 Ultra，B03下游仍BLOCKED。跨批欠项和具名未知保留。

当前入口：[整合交接](../../review/remediation/20261003-prepare/final-integration-review.md)、[B03当前身份](../../review/remediation/20261003-prepare/batches/B03/integration-stage-1/integration-manifest.json)、[B03第二轮候选报告](../../review/remediation/20261003-prepare/batches/B03/review-round-2/report.md)、[B01/B02/B05主责逐ID统计](../../review/remediation/20261003-prepare/batches/B03/integration-stage-1/accepted-primary-completion.json)、[已接受B05与B06旧冻结](../../review/remediation/20261003-prepare/batches/B05/acceptance-stage-1/README.md)、[后继勘误](../../review/remediation/20261003-prepare/historical-errata.md)。

## 原作者交付记录（批次 1–15；历史时点）

下表“待统一复审”等词保留当时交付记录；当前状态以上节及新冻结整合身份为准，不把历史 PASS_SCOPED 转移给本轮新字节。

| 批次 | 范围 | 状态 |
| --- | --- | --- |
| 批次 1 | engine-overworld：WP16 世界绘制与视觉过渡＋战前过渡（含附表） | **已通过独立复审（PASS_SCOPED）**；检查记录见 `review/wp80-delivery-2026-10-03/` |
| 批次 2 | generic-kernel：WP02 规则配置档案＋WP03 内容身份/schema＋WP04 PBS 生命周期（含 WP02 设置附表） | v2 修正后已交付（检查记录见 `review/wp80-delivery-2026-10-03/batch-02/`，ADDRESSED_PENDING_UNIFIED_REVIEW） |
| 批次 3 | engine-overworld：WP11 地图拓扑/WP12 地形运动/WP13 事件与跟随（含两矩阵附表）/WP14 随机地牢/WP15 资源与音频/WP59 时间天气场地/WP60 钓鱼 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-03/`） |
| 批次 4 | generic-kernel：WP01 基线（范围承接）/WP05 通知扩展插件/WP06 时间随机计步统计（含 74 字段附表）/WP07 诊断文件 HTTP（含弃用告警附表）/WP08 本地化/WP09 保存启动/WP10 迁移恢复 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-04/`） |
| 批次 5 | pokemon-rules：WP19 属性与能力/WP21 动态形态/WP22 Mega 与 Primal（含数据附表）/WP23 Shadow 与净化（含数据附表）/WP34 遗传 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-05/`） |
| 批次 6 | pokemon-rules：WP31 基础进化/WP32 情境交换战后事件（含数据附表）/WP37 漫游与雷达/WP38 捕获与接收 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-06/`） |
| 批次 7 | pokemon-rules：WP43 类型命中伤害/WP44 状态与阶级（含归属附表）/WP46 多击特殊伤害恢复（含覆盖附表）/WP48 特性计算/WP50 持物触发消耗（含覆盖附表） | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-07/`） |
| 批次 8 | pokemon-rules：WP53 Safari 与捕虫/WP60 树果/WP61 野外被动与回程/WP62 图鉴/WP69 Voltorb Flip（含候选附表）/WP70 Lottery | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-08/`） |
| 批次 9a | creature-rpg：WP18 生物身份物种与拥有者/WP20 HP 异常招式与持有/WP24 玩家训练家与伙伴/WP25 队伍与盒子/WP26 获得赠送与脚本交换 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-09a/`） |
| 批次 9b | creature-rpg：WP27 背包与物品储存/WP28 主动道具与培养教学/WP29 买卖与 BP 商店/WP30 成长学习与友好/WP33 寄养会话与兼容性 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-09b/`） |
| 批次 9c | creature-rpg：WP35 蛋与孵化/WP36 普通遭遇与修正/WP57 Factory 租借换队/WP64 邮件与神秘礼物/WP68 Triple Triad | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-09c/`） |
| 批次 10 | combat-requirements：WP39 战斗上下文与参与者/WP40 命令服从与行动顺序/WP41 换人位置与逃跑/WP42 成长回合末与终局/WP45 天气场地阵营与位置效果 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-10/`） |
| 批次 11 | combat-requirements：WP47-A 招式属性目标与复制调用（含数据附表）/WP47-B 招式换人控制与物品变化（含数据附表） | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-11/`） |
| 批次 12 | combat-requirements：WP49 特性阶段触发/WP51 AI 动作选择与技能（含默认数据附表）/WP52-A 通用数值与状态评估（含覆盖附表）/WP52-B 场域伤害恢复与多目标评估（含登记附表）/WP52-C 物品调用与行动控制评估（含覆盖附表） | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-12/`） |
| 批次 13 | combat-requirements：WP54 参赛资格等级调整与杯赛条款（含规则附表）/WP55 设施基础会话/WP56 Palace 与 Arena 变体/WP58 战斗记录与回放 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-13/`） |
| 批次 14 | user-interface：WP17 消息窗口与输入（含绘制标记附表）/WP63 宝可齿轮/WP65 主导航（含控制帮助与训练家卡两附页）/WP66-A 队伍摘要/WP66-B 盒子图鉴/WP66-C 背包商店/WP67-A 战斗交互/WP67-B 生命周期演出/WP68 决斗/WP69 老虎机（含转轮附表）/WP70 挖矿（含数据附表）/WP71 板块拼图 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-14/`） |
| 批次 15（本批） | demo-dx：WP72 调试上下文与控制台/WP73-A 内容编辑器/WP73-B 世界编辑器/WP74 战斗动画制作与交换/WP75 工程转换与作者工具/WP76 设施内容生成与模拟/WP77 示例工程证据与能力覆盖 | 已交付待统一复审（批次检查记录见 `review/wp80-delivery-2026-10-03/batch-15/`） |
| 全集作者交付 | 113 份输入的批次 1–15 作者交付及完成报告已完成 | 全局 review 已完成；229 项必修整改 OPEN，B01 整合待核验 |

输入基线：WP79 独立复审 PASS_SCOPED 通过基线（`review/wp79-stage-review-2026-10-03/recheck-v6/`；113 份批准规格、revision-v6 明细、revision-v4 配置、revision-v2 功能主表、revision-v5 增补）。coverage 版本链按管理时点分列：**WP79 通过基线为 v6（被审身份 `192cba52`／19,948）；WP80 导航回填为 v7（`1f9f415f`／20,726）；本轮整改前的管理回填版本为 v8（`fbbf0bfd`／20,820，保护口径同步）**。参考快照：`reference/pokemon-essentials/` 固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（只读，未运行）。
