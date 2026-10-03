# WP78 v5 交付摘要（第五版）

2026-10-03；规格提取方。依据 `review/wp78-stage-review-2026-10-03/recheck-v4/`（v4 复审：累计 8 项 CLOSED 继承、剩 R10/R02 两处；最小修订提示）。v5 完成两处最小修订，**停止送定点复审**；通过前不进入 WP79。

## 交付清单（本目录；最小增量＋[version-index.md](version-index.md)）

- **消费者处置/继承表**：[consumer-disposition.md](consumer-disposition.md)——B03 行 WP36 两事件入口按 v5 时点分开（R10）；A/B 行加稳定 ID（A01–A09/B01–B07）；§D 统计由行 ID 程序化生成（16＝12＋3＋1；C 表 6 条单列；两条保留菜单行在计）（R02）。
- **适用交界清单**：[junction-inventory.md](junction-inventory.md)——54 项闭合（v5 不增减 ID；G8-1 行内 WP36 两子入口时点修正）。
- **一致性矩阵**：[consistency-matrix.md](consistency-matrix.md)——G8 行与处置表统计行同步。
- **映射**：[mappings.md](mappings.md)——「插件载入与扩展机制」行内 WP36 事件消费改两具名子入口。
- **逐项修订回应**：[revision-response.md](revision-response.md)——R10/R02（残留/回源/修订位置/验收向量/程序化计数）、已关闭 8 项继承说明、阅读分布时点标注、V01、E01–E04。
- **实际阅读清单**：[reading-log.json](reading-log.json)——109 份逐文件（WP36 区间补记）；阅读方式 1/72/16/20 与文件角色 88/21 独立成列（v3 的 1/70/18/20 标注为历史）。
- **输入与自检**：[input-manifest.json](input-manifest.json)、[checks.json](checks.json)（R10 验收向量、R02 程序化计数复算、净化扫描、链接解析）、[report.md](report.md)（v5 报告＋定点复审入口）。
- **沿用**：`../revision-v3/anomaly-register.json`（异常事实注册表）、`../revision-v4/pending-and-na.md`（待证清单）——本轮无内容变化。

## 关键结论

- **R10**：`on_wild_species_chosen` 面向候选 [物种, 等级]、**先于该路径实际个体创建**（普通步进中早于允许遭遇判断——许可拒绝时无创建通知；主动遭遇中通知后还有候选为空返回）；`on_wild_pokemon_created` 位于**具名生成修正之后的生成末尾**。WP36 主稿已正确、未改动。
- **R02**：处置表 16 行＝直接/交界覆盖 12＋继承或混合 3＋不适用 1（稳定行 ID 程序化复算）；C 表 6 条归类对账单列；两条保留菜单行在计。
- 已关闭 8 项（R01/R03–R09）继承，未从头重审；本轮无规格文件修订；54 项交界不增减 ID。
- U01＋G01–G12 保留；③已证事件链＝0、④运行观察＝0；20 项异常事实如实保持。

## 登记

第 140 轮：v5 材料登记；旧版全部字节未动；全量 TSV/manifest 复测 0 偏差（见 manifest 第 140 轮 §4）。

## 停止点

WP78 v5 交付完成，**ReviewPending 待定点复审**；2 项不自行 CLOSED；通过前不进入 WP79／WP80；不自行宣布全项目完成。
