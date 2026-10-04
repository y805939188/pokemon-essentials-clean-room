# 最终净化规格集（WP80；2026-10-03）

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

批次 1–15 的全集作者交付与最终全局独立 review 已完成；233 个规范 finding 中 229 项必修仍全部 OPEN。B01 实际整合已获有界 PASS_SCOPED 并在 `0a12de641542f9a59909d2a950c1de8df17ca09d` 接受，证据保留。B02 完整候选 `46cd726c35e9d754a8e42b32986313ce3d4d1782` 由独立报告 `94b012ee12d457aa4b99103477a0d35f083b1182` 给出 PASS_SCOPED，13 份正式字节已整合；本次 B02 公共登记／八处导航／索引仍待 R-B02 Ultra 实际整合核验，B03/B06/B16/B18/B21 等下游未开放。B05 未审作者内容未消费；跨批欠项及具名未知继续有效。

当前入口：[整合交接](../../review/remediation/20261003-prepare/final-integration-review.md)、[B02 当前输入身份](../../review/remediation/20261003-prepare/batches/B02/integration-stage-1/integration-manifest.json)、[B02 独立候选报告](../../review/remediation/20261003-prepare/batches/B02/review-round-1/report.md)、[历史 B01 输入身份](../../review/remediation/20261003-prepare/integration-manifest.json)、[后继勘误](../../review/remediation/20261003-prepare/historical-errata.md)。

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
