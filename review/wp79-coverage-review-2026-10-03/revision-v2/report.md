# WP79 v2 覆盖与遗漏审查报告（修订版）

2026-10-03；规格提取方。依据 `review/wp79-stage-review-2026-10-03/`（首版 **REQUIRES_REVISION：原 WP79-R01 保持 OPEN，新增 R02/R03/R04——共 4 项（P2×3、P3×1）**；修订提示）。v2 完成 4 项原位修订与 3 份有界补提取，**送独立复审**；作者状态 REVISED_PENDING_REVIEW——不自行 CLOSED、不自行 Reviewed。首版材料、独立审查与冻结快照全部留史未改写。

## 1. 范围与方法

- **审查对象**：`specs/` 现行 **112 份规格**（109 原规格＋3 个补提取附表）＋Feature Matrix 113 行＋reference 固定快照（312 个 .rb、33 顶层 PBS＋备份、E01–E34 索引、根目录 2 个工具脚本）。
- **方法**：纯静态文本/哈希/集合/链接/表格计数/固定算术检查；五维覆盖；字符串匹配统计、阅读统计、行为覆盖统计分别命名；不以文件数等同功能覆盖；不以目录引用充当整目录已覆盖；不以 grep 命中当覆盖；搜索无命中不作不存在证明。
- **证据边界（承接不改写）**：U01＋G01–G12 保留；③已证事件链＝0、④运行观察＝0；20 项 AX 异常事实保持；WP78 的 11 项关闭与既有具名限定批准保持。

## 2. 执行摘要

- **R01（已修）**：训练家卡附表三处错误原位更正——画像放置改为**横向对齐到 128 宽区域＋底边保持 240**（固定算术：128×256 → (336,−16)、128×128 → (336,112)，底边同为 240）；补**装扮编号消费**（`$player.outfit`——优先 `_N` 装扮变体、解析失败回退基础图，`014_TrainerType.rb:52–61, 78–81`），删除「不读取其他玩家字段」的错误排除；TC01 改**按真值位**（0/3/7 为真 → 槽位 0/3/7 三处绘制、不紧排前三槽）；TC06 补「下标 11–15 为假」前提；新增 TC07（底边不随图高变化）、TC08（装扮变体/回退/装扮 0 先试 `_0`）。附表保持 ReviewPending；旧 WP65/WP24/WP15 未改写。
- **R02（已修）**：交付四份可枚举明细——[feature-details.json](feature-details.json)（113 Feature 逐行＋3 个补充范围单列）、[source-details.json](source-details.json)（312 个 .rb 逐路径处置：290 引用＋3 补提取＋2 行为层＋17 不适用＋**0 未引用**）、[config-details.json](config-details.json)（33 顶层 PBS＋备份＋未引用文件逐处置）、[ui-scenario-relations.json](ui-scenario-relations.json)（13 个入口↔场景 ID↔责任规格）。三类统计命名分开；根目录 2 个工具脚本单独登记（312 不是全 reference 总数）。
- **R03（已修）**：**控制帮助**（四页交互帮助场景——确认推进、页面内容、末页过渡退出；父级 EventScene 分发已定点）补提取 [specs/ui/wp65-controls-help-appendix.md](../../../specs/ui/wp65-controls-help-appendix.md)（CH01–CH05）；**弃用告警**（warn_method 三部分独立可选、弃用别名先告警后执行并透传返回值、校验与 ArgumentError 分阶段）补提取 [specs/kernel/wp07-deprecation-appendix.md](../../../specs/kernel/wp07-deprecation-appendix.md)（DP01–DP05）。14 个精灵/渲染原语保留不适用（给确切章节）；`001_Transitions.rb` 改判行为层已覆盖（WP16 §4.2/§6）；新确证遗漏 0 项。
- **R04（已修）**：保护对象时点改为 **31,690 不变＋manifest/TSV/coverage 三项授权变化**（coverage.md 不计入「字节不变」）；规格文件 109→**112**；包 ID 仍 **84**；10 个多包关系按实际分工分类（不统称 A/B/C 拆分）；计数三命名（字符串匹配/阅读/行为覆盖）同步全部材料。

## 3. 逐项处置（详见 [revision-response.md](revision-response.md)）

| 编号 | 优先级 | 处置 |
| --- | --- | --- |
| R01 | P2 | 已修：附表三处更正＋TC07/TC08 新增 |
| R02 | P2 | 已修：四份可枚举明细（feature/source/config/ui-scenario） |
| R03 | P2 | 已修：两份补提取（控制帮助/弃用告警）＋其余不适用逐项复核 |
| R04 | P3 | 已修：统计同步（保护时点/文件包口径/多包分类/计数命名） |

## 4. 阅读范围（诚实登记）

- **全文阅读**：`016_UI/012_UI_TrainerCard.rb`（111）、`016_UI/001_Non-interactive UI/002_UI_Controls.rb`（83）、`001_Technical/001_Debugging/005_Deprecation.rb`（52）。
- **定点阅读**：画像放置（26–33 行）、装扮资源（`014_TrainerType.rb:52–61, 78–81`）、EventScene 分发（`009_Scenes/002_EventScene.rb:66–100, 166–170`）、WP21 §5.2、WP13 矩阵 231–235、WP16 §4.2/§6、WP52-A 覆盖表。
- **结构化分析**：矩阵 113 行、计划 87 行、E 索引 34 包、109 份规格 traceability 段、reference 312 .rb 与 33 PBS 清单。
- **仅身份**：109 份规格哈希、备份 PBS、WP78 批准材料。

## 5. 量化统计（分母分列）

Feature 113／内容包 84／规格包 ID 84／E 包 34／.rb 312（引用 290＋补提取 3＋行为层 2＋不适用 17＋未引用 0）／PBS 33（＋备份 2 族＋未引用文件 2）／场景行 1,731（统计量）／补提取场景 TC01–TC08、CH01–CH05、DP01–DP05／确证遗漏 3（已补提取待复审）／不适用 17（具名）／行为层 2／根目录工具脚本 2／辅助汇总新增 0。

## 6. 独立复审入口

- 材料全集：[planning/coverage.md](../../../planning/coverage.md)（v2 主覆盖表）、本目录 [revision-response.md](revision-response.md)、[feature-details.json](feature-details.json)、[source-details.json](source-details.json)、[config-details.json](config-details.json)、[ui-scenario-relations.json](ui-scenario-relations.json)、[checks.json](checks.json)、[report.md](report.md)、[delivery-summary.md](delivery-summary.md)、[input-manifest.json](input-manifest.json)、[reading-log.json](reading-log.json)；三份补提取附表（[wp65-trainer-card-appendix.md](../../../specs/ui/wp65-trainer-card-appendix.md)、[wp65-controls-help-appendix.md](../../../specs/ui/wp65-controls-help-appendix.md)、[wp07-deprecation-appendix.md](../../../specs/kernel/wp07-deprecation-appendix.md)）。
- 重点核验建议：(1) R01 的对齐算术与装扮输入（`012_UI_TrainerCard.rb:28–31`、`014_TrainerType.rb:52–61, 78–81`）；(2) 312 行明细的处置与未引用 0 的复核；(3) 两份 R03 补提取与 WP65/WP07 边界（不冒充被审内容）；(4) R04 的保护时点与计数命名。
- **阶段门**：本复审通过且 4 项确认关闭后才进入 WP80（净化交付，消费本表审定基线）；不以自检替代独立通过。

## 7. 状态

**ReviewPending（WP79 v2，待独立复审）**。不自行宣布全项目完成；不进入 WP80；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 只读、Git 清洁；未创建任务/Agent、未跨会话发消息、未提交/推送；未运行参考/编译器/游戏/反序列化/参考行为模拟器。
