# WP79 v4 覆盖与遗漏审查报告（第四版）

2026-10-03；规格提取方。依据 `review/wp79-stage-review-2026-10-03/recheck-v3/`（v3 复审：**REQUIRES_REVISION——R01 本次 CLOSED、R04 继承 CLOSED；只剩 R02（P2 覆盖判断校准）与 R03（残留 P3 回应文字净化），无新增编号**；修订提示）。v4 完成 2 项原位修订，**送有界复审**；作者状态 REVISED_PENDING_REVIEW——不自行 CLOSED、不自行 Reviewed。R01/R04 保持关闭；v1/v2/v3 材料、独立审查与冻结快照全部留史未改写。

## 1. 范围与方法

- **审查对象**：`specs/` 现行 **112 份规格**（109 原规格＋3 个补提取附表）＋Feature Matrix 113 行＋reference 固定快照（312 个 .rb、33 顶层 PBS＋备份、E01–E34 索引、根目录 2 个工具脚本）。
- **方法**：纯静态文本/哈希/集合/链接/表格计数/固定算术检查；**字符串匹配统计（候选引用证据）、阅读统计、行为覆盖统计分别命名、不互相替代、不自动升级**；不以 grep 命中当覆盖；不为凑零标签把缺证升级为已覆盖；不重新全文读 312 文件（按复审要求从已有批准的完整附表与具名章节继承），也不一概交给 WP80。
- **证据边界（承接不改写）**：U01＋G01–G12 保留；③已证事件链＝0、④运行观察＝0；20 项 AX 异常事实保持；R01/R04 保持关闭；WP78 的 11 项关闭与既有具名限定批准保持。

## 2. 执行摘要

- **R02（已修）**：覆盖判断逐行校准后交付 [source-judgments.json](source-judgments.json)（312 行：实际行为/数据范围、承担章节/表项、批准依据、覆盖判断、剩余处置、候选引用证据独立 candidate_refs 字段）——校准后分布 **290 已覆盖＋1 部分覆盖（具名缺证）＋3 补提取＋1 行为层（具名实现边界）＋17 不适用＋0 仅定位＋0 未引用**（由校准后明细重新汇总，未承诺保持 270/20）。四项点名校准全部落实：**AI 评分**撤销整体排除（WP51 §3.1–3.3/§4/§5、WP52-A §2.1–2.2/§3、WP52-B §2–6、WP52-C §2–6 及三包有界附表逐登记绑定直接关联；实现细节仅限不改变评分/排序/选择概率的组织方式；无具名未覆盖行为数值）；**来源子范围**（WildEncounters→WP36 §3–6 全文、EventScene 与 WP13 §B 分开、Settings/BattleSettings 词典＋候选使用点、Transitions 调用/时长语义与逐帧绘制的界线、Environment 注册契约与逐环境映射；Battle triggering 目录规则整组校准，BattleIntroAnim 主体演出段保留具名缺证）；**UI 关系**（暂停保存 T11–T14、可见条件 T24、标题/载入 T01–T10 正确分开；全部入口关联实测场景 ID 或具名入口表位置；合同章节独立 contract_ref）；**配置证据**（WP48 计算/WP49 触发/WP19 §3.4 派生；名单引用不充当样本证据；机制/样本/内容/启用四者分开）。配套：[config-details.json](config-details.json)（35 行）、[ui-scenario-relations.json](ui-scenario-relations.json)（16 入口）、[planning/coverage.md](../../../planning/coverage.md)（v4 主覆盖表）。
- **R03（已修）**：v4 回应及全部新材料**不再复写被删除的源码语句**——仅以独立文字登记：控制帮助附表的背景暂存、页号递增、页面更新和过渡调用已改写为独立行为合同；过渡推进说明改为「**按已过时间占目标时长的比例**」（8 个 1/20 秒单位＝目标 0.4 秒）；路径/行号保留作审计定位。扩展模式重扫（连字符化审计名避免自匹配）：**v4 新材料 0 命中**（重新实测，不沿用旧声明）；三份附表保持 recheck-v3 已接受基线未改（其中仅有的带参调用形为已接受审计名与 DP 向量输入）。已接受的 0.4 秒、默认 BACK 无退出、实际调用者未定位、告警首行必有与参数/正常返回限定全部保持。

## 3. 逐项处置（详见 [revision-response.md](revision-response.md)）

| 编号 | 优先级 | 处置 |
| --- | --- | --- |
| R01 | —（v3 复审已关闭） | 保持关闭，不重开 |
| R02 | P2 | 已修：312 行覆盖判断校准（290＋1＋3＋1＋17＋0＋0）＋配置/UI 关系校准＋remaining/candidate_refs 字段规则 |
| R03 | P3（残留） | 已修：回应文字净化（不复写原语句、过渡说明独立表述）＋扩展模式重扫 v4 新材料 0 命中 |
| R04 | —（已关闭继承） | 保持关闭 |

## 4. 阅读范围（诚实登记）

详见 [reading-log.json](reading-log.json)。要点：reference 定点（Environment :1–40 注册结构核对；5 个文件行数统计）；规格定点（WP51/WP52-A/B/C 及三包附表、WP36/WP37/WP39/WP42/WP47-A、WP16/WP13/WP02/WP19/WP48/WP49、WP65 T01–T36 全表、WP76/WP77/WP02 附表、PBS 样本证据抽查 15 处）；场景 ID 上限全部程序化实测；结构化分析（v3 九份材料、recheck-v3 复审材料、登记基线）。身份核验不声称阅读；行数统计不声称逐行阅读。

## 5. 量化统计（分母分列）

Feature 113／内容包 84／规格包 ID 84／E 包 34／规格 112（109＋3 附表）／.rb 312（**290 已覆盖＋1 部分覆盖（具名缺证）＋3 补提取＋1 行为层＋17 不适用＋0 仅定位＋0 未引用**）／PBS 33（8 个杯赛名单引用文件与 pokemon_metrics.txt 机制已覆盖·样本未读；2 个非 _single fancy 未引用文件；备份 2 族存在性登记）／场景行 1,731（统计量）／UI 入口 16（全部实测 ID 或具名入口表位置）／补提取场景 TC01–TC08、CH01–CH05、DP01–DP05／不适用 17（具名）／根目录工具脚本 2／辅助汇总新增 0。

## 6. 独立复审入口

- 材料全集：[planning/coverage.md](../../../planning/coverage.md)（v4 主覆盖表）、本目录 [revision-response.md](revision-response.md)、[source-judgments.json](source-judgments.json)、[config-details.json](config-details.json)、[ui-scenario-relations.json](ui-scenario-relations.json)、[reading-log.json](reading-log.json)、[input-manifest.json](input-manifest.json)、[checks.json](checks.json)、[report.md](report.md)、[delivery-summary.md](delivery-summary.md)；v2 明细沿用 `../revision-v2/feature-details.json`；v3 材料留史于 `../revision-v3/`；三份补提取附表（[wp65-trainer-card-appendix.md](../../../specs/ui/wp65-trainer-card-appendix.md)、[wp65-controls-help-appendix.md](../../../specs/ui/wp65-controls-help-appendix.md)、[wp07-deprecation-appendix.md](../../../specs/kernel/wp07-deprecation-appendix.md)——本轮未改）。
- 重点核验建议：(1) 20 个 AI 文件的承担章节与 WP51/WP52-A/B/C 及有界附表的对应（附表逐登记绑定可直接抽查）；(2) remaining/candidate_refs 字段规则与 193 行迁移结果；(3) WildEncounters/Battle triggering 组/EventScene/Settings/Transitions/Environment 校准行；(4) 暂停保存 T11–T14 vs 标题/载入 T01–T10 的分开与各入口实测场景 ID 上限；(5) abilities.txt 的 WP48/WP49/WP19 §3.4 分层与 8 个杯赛文件样本限定；(6) v4 新材料扩展模式重扫与 R03 文字净化。
- **阶段门**：本复审通过且 2 项确认关闭后才进入 WP80（净化交付，消费本表审定基线）；不以自检替代独立通过。

## 7. 状态

**ReviewPending（WP79 v4，待有界复审）**。不自行宣布全项目完成；不进入 WP80；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 只读、Git 清洁；未创建任务/Agent、未跨会话发消息、未提交/推送；未运行参考/编译器/游戏/反序列化/参考行为模拟器。
