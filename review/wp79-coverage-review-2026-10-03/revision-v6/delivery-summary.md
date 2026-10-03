# WP79 v6 交付摘要（第六版）

2026-10-03；规格提取方。依据 `review/wp79-stage-review-2026-10-03/recheck-v5/`（v5 复审：主要补提取已通过；只剩 R02 的 A/B/C 定点修正）。v6 完成 3 处定点修订，**停止送有界复审**；通过前不进入 WP80。

## 交付清单（本目录）

- **逐项修订回应**：[revision-response.md](revision-response.md)——R02-A/B/C（定点修正/回源定位/新增向量）、已关闭项保持说明、自检。
- **覆盖判断明细（v6）**：[source-judgments.json](source-judgments.json)——312 行：BattleIntroAnim 行场景范围 BT01–BT16＋附表 v2 校正注记；其余 311 行继承。分布不变（291 已覆盖＋4 补提取＋17 不适用＋0＋0＋0＋0）。
- **UI/场景关系（v6）**：[ui-scenario-relations.json](ui-scenario-relations.json)——17 入口；战前过渡入口同步 BT01–BT16 与 §4.3/§5/§9 校正点。
- **定点校正附表**：[specs/overworld/wp16-pre-battle-transitions-appendix.md](../../../specs/overworld/wp16-pre-battle-transitions-appendix.md)（v1→v2；v1 身份 `bd3b01c6` 保留于登记历史）——§1/§9 调用侧真实传值、§4.3 玩家/对手资源规则分开、§5 中断守卫与异常重试条件、BT11 限定＋BT13–BT16 新增。
- **主覆盖表**：[planning/coverage.md](../../../planning/coverage.md)（v6——§2.2 去重、BT 范围、v6 校正说明）。
- **输入与自检**：[input-manifest.json](input-manifest.json)（138 份冻结输入）、[reading-log.json](reading-log.json)、[checks.json](checks.json)、[report.md](report.md)、本摘要。
- **沿用**：`../revision-v5/`（source-judgments/ui-scenario-relations/feature-navigation-addendum 基线）、`../revision-v4/config-details.json`、`../revision-v2/feature-details.json`；v1–v5 材料全部留史。

## 关键结论

- **R02-A**：装束回退只作用于玩家（条形图/立绘两项独立、允许混合命中），不扩展到对手；调用侧输入准确区分（类别为调用方输入；训练家链 1/3、野生链 0/2、设施/回放默认类别 0 与空上下文；不从音乐或实际战斗类型反推）。
- **R02-B**：中断先检查（置位不处置/不实例化/不阻塞，未置位才处置在途；不推成永不更新）；异常重试补全条件（首次异常仅文件名非空才空名重试一次、已空不重试、第二次不兜底、具名效果实例化在捕获范围外）；零/负时长早退限定为实际选中并初始化路径。
- **R02-C**：coverage.md §2.2 重复四行已删除（程序化确认无残留）；明细不受影响；R04 旧关闭不重开。
- 分布不变（291＋4＋17＝312）；规格 113 份、包 ID 84 不变；R01/R03/R04 保持关闭；v4/v5 已接受校准保持；U01＋G01–G12 保留；③④＝0；20 项 AX 异常事实保持。

## 登记

第 148 轮：附表 v2、coverage.md v6 与 v6 八份材料登记；v1–v5 材料与独立审查字节留史；全量 TSV/manifest 复测 0 偏差（见 manifest 第 148 轮 §4 与本目录 registration-final-checks.json——末检文件单独保存不登记）。

## 停止点

WP79 v6 交付完成，**ReviewPending 待有界复审**（A/B 定点差异与 C 去重、登记联动）；1 项不自行 CLOSED；通过前不进入 WP80；不自行宣布全项目完成。
