# WP79 v6 覆盖与遗漏审查报告（第六版）

2026-10-03；规格提取方。依据 `review/wp79-stage-review-2026-10-03/recheck-v5/`（v5 复审：**REQUIRES_REVISION——主要补提取已通过；只剩 R02（P2）的定点修正：A 输入与资源侧别、B 守卫与重试条件、C 覆盖表重复行，无新增编号**；修订提示）。v6 完成 A/B/C 三处定点修订，**送有界复审**；作者状态 REVISED_PENDING_REVIEW——不自行 CLOSED、不自行 Reviewed。R01/R03/R04 保持关闭；v1–v5 材料、独立审查与冻结快照全部留史未改写。

## 1. 范围与方法

- **本轮范围**：仅 R02 余项定点校正——WP16 战前过渡附表 v1→v2（§1/§4.3/§5/§8/§9/§10 六处局部）与 coverage.md §2.2 去重。不新增附表；不重做注册表/默认表/14 项固定时长；不扩大源码阅读；v4/v5 已接受校准保持。
- **方法**：纯静态文本/哈希/集合/链接/表格计数/固定算术检查；三类统计分别命名、不自动升级；回应与报告不复写源码语句；扫描区分机器原始命中、审计定位误报与人工确认。

## 2. 执行摘要

- **A（输入与资源侧别）**：附表 §4.3 改为按侧分开——对手条形图/立绘直接按对手类型选基础资源（不查询装束变体）；玩家条形图与立绘各自独立尝试装束变体并分别回退（允许混合命中，不扩展至对手侧）。§1/§9 按真实传值校正——普通训练家链类别 1/3 按单双打、对手为训练家列表（:521–522）；普通野生链类别 0/2 按队伍数、对手为野生个体列表（:401–402）；设施挑战/回放仅传音乐→默认类别 0 与空对手上下文（`004_Challenge_Battles.rb:65–66, 125–126`）；**过渡类别是调用方输入，不从音乐或实际战斗类型反推**（参考行为不改写）。新增 BT13（混合命中）与 BT16（默认类别边界）。
- **B（守卫与重试条件）**：§5 补全——中断旗标**先检查**：置位即返回否（本调用不处置在途旧过渡、不实例化、不阻塞），未置位才按既有路径处置在途；未处置不推成永不更新/清理（BT14）。零/负时长早退限定为实际被选中并进入具名效果初始化的路径（BT11 同步限定）。异常重试：首次异常本层捕获、**仅文件名非空才以空文件名重试一次、文件名已空不重试、第二次不兜底**；具名效果选中后的收尾调用文件名已空不承诺重试；具名效果实例化在捕获范围外（保持）。新增 BT15（文件名非空/已空两预期）。
- **C（覆盖表去重）**：coverage.md §2.2 重复四行已删除（程序化确认无残留重复行）；明细 JSON 不受影响（312 唯一、291/4/17 可复算）；R04 旧关闭不重开。
- **联动**：source-judgments v6 一行同步（BT01–BT16＋v2 校正注记，其余 311 行继承）；ui-scenario-relations v6 战前过渡入口同步（原 16 入口保持）；coverage.md v6 同步；分布不变（291＋4＋17＝312）；规格文件 113 份不变、包 ID 84 不变。

## 3. 逐项处置（详见 [revision-response.md](revision-response.md)）

| 编号 | 优先级 | 处置 |
| --- | --- | --- |
| R01 | —（v3 已关闭） | 保持关闭 |
| R02-A | P2 | 已修：§4.3 玩家/对手资源规则分开＋§1/§9 调用侧真实传值（BT13/BT16） |
| R02-B | P2 | 已修：§5 中断守卫先于在途处置＋异常重试文件名条件（BT14/BT15，BT11 限定） |
| R02-C | P3（联动） | 已修：coverage.md §2.2 重复四行删除（程序化确认） |
| R03 | —（v4 已关闭） | 保持关闭 |
| R04 | —（v2 已关闭继承） | 保持关闭 |

## 4. 阅读范围（诚实登记）

详见 [reading-log.json](reading-log.json)：reference 定点（:277–298 资源规则、:401–402/:521–522 真实传值、设施两处仅音乐调用、Transitions :18–50/:109–120 守卫/重试/早退）；规格定点（recheck-v5 复审材料、附表 v1 全稿、coverage §2.2 重复定位——程序化确认逐字重复后删除）。身份核验不声称阅读。

## 5. 量化统计（分母分列）

Feature 113（＋1 补充范围单列）／内容包 84／E 包 34／规格 **113**（不变）／.rb 312（**291 已覆盖＋4 补提取＋17 不适用＋0 部分覆盖＋0 行为层＋0 仅定位＋0 未引用**——与 v5 相同）／PBS 33（v4 口径保持）／场景行 1,731（统计量）／UI/功能入口 17／补提取场景 TC01–TC08、CH01–CH05、DP01–DP05、**BT01–BT16**／不适用 17（具名）／根目录工具脚本 2／辅助汇总新增 0。

## 6. 独立复审入口

- 材料全集：附表 v2（[wp16-pre-battle-transitions-appendix.md](../../../specs/overworld/wp16-pre-battle-transitions-appendix.md)）、本目录 [revision-response.md](revision-response.md)、[source-judgments.json](source-judgments.json)、[ui-scenario-relations.json](ui-scenario-relations.json)、[reading-log.json](reading-log.json)、[input-manifest.json](input-manifest.json)、[checks.json](checks.json)、[report.md](report.md)、[delivery-summary.md](delivery-summary.md)；[planning/coverage.md](../../../planning/coverage.md)（v6）；v5 材料（source-judgments/ui-scenario-relations/feature-navigation-addendum 基线）留史于 `../revision-v5/`；config-details 沿用 `../revision-v4/config-details.json`；feature-details 沿用 `../revision-v2/feature-details.json`。
- 重点核验建议：(1) §4.3 与 :277–298 的按侧资源规则对应（对手无装束查询、玩家两项独立回退）；(2) §1/§9 与 :401–402/:521–522/设施两处的真实传值（类别为调用方输入、默认类别 0 边界）；(3) §5 中断守卫（:44–50/:31）与异常重试（:26–30）的条件完整性；(4) coverage §2.2 去重结果；(5) BT13–BT16 与 A/B 验收点对照。
- **阶段门**：本复审通过且 R02 确认关闭后才进入 WP80（净化交付，消费本表审定基线）；不以自检替代独立通过。

## 7. 状态

**ReviewPending（WP79 v6，待有界复审）**。不自行宣布全项目完成；不进入 WP80；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 只读、Git 清洁；未创建任务/Agent、未跨会话发消息、未提交/推送；未运行参考/编译器/游戏/反序列化/参考行为模拟器。
