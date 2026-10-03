# WP79 v3 覆盖与遗漏审查报告（第三版）

2026-10-03；规格提取方。依据 `review/wp79-stage-review-2026-10-03/recheck-v2/`（v2 复审：**REQUIRES_REVISION——R04 本次关闭，R01/R02/R03 仍 OPEN（3 项 P2），无新增编号**；修订提示）。v3 完成 3 项原位修订，**送有界复审**；作者状态 REVISED_PENDING_REVIEW——不自行 CLOSED、不自行 Reviewed。R04 保持关闭；v1/v2 材料、独立审查与冻结快照全部留史未改写。

## 1. 范围与方法

- **审查对象**：`specs/` 现行 **112 份规格**（109 原规格＋3 个补提取附表）＋Feature Matrix 113 行＋reference 固定快照（312 个 .rb、33 顶层 PBS＋备份、E01–E34 索引、根目录 2 个工具脚本）。
- **方法**：纯静态文本/哈希/集合/链接/表格计数/固定算术检查；**字符串匹配统计（候选引用证据）、阅读统计、行为覆盖统计分别命名、不互相替代、不自动升级**；不以文件数等同功能覆盖；不以目录引用充当整目录已覆盖；不以 grep 命中当覆盖；搜索无命中不作不存在证明。
- **证据边界（承接不改写）**：U01＋G01–G12 保留；③已证事件链＝0、④运行观察＝0；20 项 AX 异常事实保持；R04 保持关闭；WP78 的 11 项关闭与既有具名限定批准保持。

## 2. 执行摘要

- **R01（已修）**：训练家卡 §3 开场表残留「水平垂直居中」已同步为「横向对齐到 128 宽区域、底边保持 240（放置规则见 §4）」——与已接受的 §4 更正一致；TC 向量保持。
- **R02（已修）**：交付 [source-judgments.json](source-judgments.json)（312 行逐路径覆盖判断）——实际行为/数据子范围、承担规格章节、批准依据、覆盖判断、剩余处置：**270 已覆盖＋20 部分覆盖（AI 评估：身份与评估合同在案、内部评分算术为实现细节）＋3 补提取＋2 行为层＋17 不适用＋0 仅定位＋0 未引用**。点名分层示例全部落实（Settings→WP02 词典＋分层消费；abilities.txt→WP34/WP35 三样本＋WP48/WP19/WP44 分层；Transitions→WP16 §4.2/§6 引擎内部为实现细节；EventScene→WP13 §B＋附页面；AI 评估系列→WP51/WP52 身份与合同）。三类统计命名分开、不自动升级；[config-details.json](config-details.json)（配置逐文件分层）、[ui-scenario-relations.json](ui-scenario-relations.json)（入口连到可定位场景 ID/入口表，不只以「静态场景节」或全库行数作证明）。
- **R03（已修）**：**控制帮助**——过渡改为**目标 0.4 秒（8 个 1/20 秒单位）**（`001_Transitions.rb:18–35, 44–95, 440–447` 只读核对）；BACK 改为实际规则（`002_EventScene.rb:155–171` 触发 `onBTrigger` 事件、`005_Event_Handlers.rb:4–48` 空回调表即无事发生——**标准初始化且无额外回调时不产生退出动作**，不泛称「按父级默认」）；调用点改为「实际调用者未定位（待证）」；源码表达（具体调用、全局赋值、实例页号自增等）全部清理为独立合同，扩展模式重扫 **0 命中**（重新实测，不沿用旧声明）。**弃用告警**——首行（方法名）必有、移除版本与替代建议分别可选统一；直接调用者（`001_FileTests.rb:78–85`、`005_Move.rb:61`、`004_Pokemon_Move.rb:68`、`001_Pokemon.rb:319/325`、`010_DrawText.rb:44/50/56/62/68`、`001_Compiler.rb:517`）与别名构造器分开（`deprecated_method_alias` 在当前核心脚本未找到登记调用，如实登记）；转发限定到位置/关键字参数与正常返回（未显式转发块回调、目标自身失败边界不被抹掉）。

## 3. 逐项处置（详见 [revision-response.md](revision-response.md)）

| 编号 | 优先级 | 处置 |
| --- | --- | --- |
| R01 | P2 | 已修：开场表残留句同步（横向对齐＋底边 240） |
| R02 | P2 | 已修：312 行覆盖判断（270＋20＋3＋2＋17＋0＋0）＋配置/UI/Feature 分层明细 |
| R03 | P2 | 已修：控制帮助（0.4 秒、BACK 实际规则、源码清理）与弃用告警（首行必需、调用者分开、转发限定） |
| R04 | —（已关闭） | 保持关闭 |

## 4. 阅读范围（诚实登记）

- **全文阅读**：`016_UI/012_UI_TrainerCard.rb`（111）、`016_UI/001_Non-interactive UI/002_UI_Controls.rb`（83）、`001_Technical/001_Debugging/005_Deprecation.rb`（52）。
- **定点阅读**：`009_Scenes/001_Transitions.rb:18–35, 44–95, 440–447`、`009_Scenes/002_EventScene.rb:155–171`、`003_Game processing/005_Event_Handlers.rb:4–48`、`001_Technical/002_Files/001_FileTests.rb:78–85`、`005_Move.rb:61`、`004_Pokemon_Move.rb:68`、`001_Pokemon.rb:319/325`、`010_DrawText.rb:44/50/56/62/68`、`001_Compiler.rb:517`；`deprecated_method_alias` 调用点检索（当前核心脚本 0 命中）。
- **结构化分析**：矩阵 113 行、计划 87 行、E 索引 34 包、109 份规格 traceability 段、reference 312 .rb 与 33 PBS 清单。
- **仅身份**：109 份规格哈希、备份 PBS、WP78 批准材料。

## 5. 量化统计（分母分列）

Feature 113／内容包 84／规格包 ID 84／E 包 34／.rb 312（270 已覆盖＋20 部分覆盖＋3 补提取＋2 行为层＋17 不适用＋0 仅定位＋0 未引用）／PBS 33（＋备份 2 族＋未引用文件 2）／场景行 1,731（统计量）／补提取场景 TC01–TC08、CH01–CH05、DP01–DP05／确证遗漏 3（已补提取待复审）／不适用 17（具名）／行为层 2／根目录工具脚本 2／辅助汇总新增 0。

## 6. 独立复审入口

- 材料全集：[planning/coverage.md](../../../planning/coverage.md)（v3 主覆盖表）、本目录 [revision-response.md](revision-response.md)、[source-judgments.json](source-judgments.json)、[config-details.json](config-details.json)、[ui-scenario-relations.json](ui-scenario-relations.json)、[checks.json](checks.json)、[report.md](report.md)、[delivery-summary.md](delivery-summary.md)、[input-manifest.json](input-manifest.json)、[reading-log.json](reading-log.json)；v2 明细沿用 `../revision-v2/`（feature-details.json）；三份补提取附表（[wp65-trainer-card-appendix.md](../../../specs/ui/wp65-trainer-card-appendix.md)、[wp65-controls-help-appendix.md](../../../specs/ui/wp65-controls-help-appendix.md)、[wp07-deprecation-appendix.md](../../../specs/kernel/wp07-deprecation-appendix.md)）。
- 重点核验建议：(1) 312 行判断与分层示例（Settings/abilities/Transitions/EventScene/AI 评估）；(2) 控制帮助的 0.4 秒与 BACK 实际规则（`001_Transitions.rb:18–35, 44–95, 440–447`、`002_EventScene.rb:155–171`、`005_Event_Handlers.rb:4–48`）；(3) 弃用告警的直接调用者与构造器分开（`deprecated_method_alias` 当前核心脚本 0 命中）；(4) 源码清理后的扩展模式重扫。
- **阶段门**：本复审通过且 3 项确认关闭后才进入 WP80（净化交付，消费本表审定基线）；不以自检替代独立通过。

## 7. 状态

**ReviewPending（WP79 v3，待有界复审）**。不自行宣布全项目完成；不进入 WP80；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 只读、Git 清洁；未创建任务/Agent、未跨会话发消息、未提交/推送；未运行参考/编译器/游戏/反序列化/参考行为模拟器。
