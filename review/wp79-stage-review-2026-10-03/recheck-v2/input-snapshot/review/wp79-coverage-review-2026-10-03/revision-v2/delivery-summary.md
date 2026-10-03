# WP79 v2 交付摘要（修订版）

2026-10-03；规格提取方。依据 `review/wp79-stage-review-2026-10-03/`（首版 REQUIRES_REVISION：原 WP79-R01 保持 OPEN，新增 R02/R03/R04——共 4 项；修订提示）。v2 完成 4 项原位修订与 3 份有界补提取，**停止送独立复审**；通过前不进入 WP80。

## 交付清单（本目录）

- **逐项修订回应**：[revision-response.md](revision-response.md)——R01–R04（残留/回源/修订位置/对照/验收向量）、已关闭项保持说明、总体自检。
- **Feature 明细**：[feature-details.json](feature-details.json)——113 Feature 逐行（包/规格文件/状态分类/未验证子范围）＋3 个补充范围 ReviewPending 单列。
- **来源明细**：[source-details.json](source-details.json)——312 个 .rb 逐路径处置（290 引用＋3 补提取＋2 行为层＋17 不适用＋0 未引用）；三类统计命名分开。
- **配置明细**：[config-details.json](config-details.json)——33 顶层 PBS 逐文件＋备份目录（存在性登记）＋未引用 fancy 文件（如实登记）。
- **UI/场景关系**：[ui-scenario-relations.json](ui-scenario-relations.json)——13 个入口↔场景 ID↔责任规格（1,731 行只作统计量）。
- **补提取规格（3 份）**：[wp65-trainer-card-appendix.md](../../../specs/ui/wp65-trainer-card-appendix.md)（R01 更正后：对齐/装扮/徽章已修，TC01–TC08）、[wp65-controls-help-appendix.md](../../../specs/ui/wp65-controls-help-appendix.md)（R03-1：四页控制帮助场景，CH01–CH05）、[wp07-deprecation-appendix.md](../../../specs/kernel/wp07-deprecation-appendix.md)（R03-2：弃用告警机制，DP01–DP05）——均 ReviewPending，不冒充被审内容。
- **主覆盖表**：[planning/coverage.md](../../../planning/coverage.md)（v2——五维覆盖关系＋统计口径说明）。
- **输入与自检**：[input-manifest.json](input-manifest.json)（冻结输入）、[checks.json](checks.json)（验收向量、计数完整性、净化扫描、链接解析）、[reading-log.json](reading-log.json)（阅读范围）、[report.md](report.md)（v2 报告＋复审入口）。

## 关键结论

- **R01**：训练家卡附表三处错误原位更正（对齐＝横向到 128 宽区域＋底边 240；装扮编号消费优先变体回退基础图；徽章按真值位不紧排），新增 TC07/TC08。
- **R02**：四份可枚举明细交付，312 行来源未引用 0；312 不是全 reference 总数（根目录 2 个工具脚本单独登记）。
- **R03**：控制帮助与弃用告警两份补提取完成（83/52 行全文阅读）；14 个精灵/渲染原语保留不适用（给确切章节）；Transitions 改判行为层。
- **R04**：保护时点 31,690＋3 授权变化；规格 109→112；包 ID 84；多包关系按实际分工分类；计数三命名。
- U01＋G01–G12 保留；③④＝0；20 项 AX 异常事实保持；WP78 的 11 项关闭与既有具名批准保持。

## 登记

第 144 轮：3 份补提取附表（含 R01 更正后的训练家卡附表新身份）、coverage.md v2 与 v2 材料登记；v1 材料与首版字节留史；全量 TSV/manifest 复测 0 偏差（见 manifest 第 144 轮 §4）。

## 停止点

WP79 v2 交付完成，**ReviewPending 待独立复审**；4 项不自行 CLOSED；通过前不进入 WP80；不自行宣布全项目完成。
