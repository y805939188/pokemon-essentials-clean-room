# WP78 v5 版本索引（最小增量交付）

2026-10-03；规格提取方。按 v4 复审提示「可复用未变化的 v4 文档，通过当前版本索引明确哪些文件被替代」。本索引为 v5 交付的文件效力声明：**只有「v5 替代」列中的文件是本轮当前版本**；「沿用」列中的旧版文件仍为当前有效内容（未被替代、未改写）。

## v5 替代（本目录新建，取代同名旧版）

| 文件 | 取代 | 变化 |
| --- | --- | --- |
| [consumer-disposition.md](consumer-disposition.md) | `../revision-v4/consumer-disposition.md` | B03 行 WP36 两事件入口按 v5 时点分开（R10）；A/B 行加稳定 ID（A01–A09/B01–B07）；§D 统计由行 ID 程序化生成（16＝12＋3＋1；C 表 6 条单列）；历史保留/本轮新增另列（R02） |
| [junction-inventory.md](junction-inventory.md) | `../revision-v4/junction-inventory.md` | G8-1 行内 WP36 两子入口时点修正；分解行加 v5 注记（54 项不增减 ID） |
| [consistency-matrix.md](consistency-matrix.md) | `../revision-v4/consistency-matrix.md` | G8 行同步 R10；处置表统计行同步 R02；登记行更新至第 140 轮 |
| [mappings.md](mappings.md) | `../revision-v4/mappings.md` | §1「插件载入与扩展机制」行内 WP36 事件消费改两具名子入口（R10） |
| [revision-response.md](revision-response.md) | `../revision-v4/revision-response.md` | R10/R02 逐项；已关闭 8 项继承说明；阅读分布历史时点标注 |
| [reading-log.json](reading-log.json) | `../revision-v4/reading-log.json` | WP36 阅读区间补记（§3/§5.1/§6.1 与 reference 定点） |
| [input-manifest.json](input-manifest.json) | `../revision-v4/input-manifest.json` | v5 冻结输入（含 v4 复审授权文件） |
| [checks.json](checks.json) | `../revision-v4/checks.json` | R10 验收向量、R02 程序化计数复算、链接与净化 |
| [report.md](report.md) | `../revision-v4/report.md` | v5 报告与定点复审入口 |
| [delivery-summary.md](delivery-summary.md) | `../revision-v4/delivery-summary.md` | v5 摘要 |

## 沿用（旧版仍为当前有效内容，未被替代）

| 文件 | 版本 | 说明 |
| --- | --- | --- |
| `../revision-v3/anomaly-register.json` | v3 | 异常事实注册表（AX01–AX20／16 交界）——本轮无内容变化，继续有效 |
| `../revision-v4/pending-and-na.md` | v4 | 待证与不适用清单（P05 已重述）——本轮无内容变化，继续有效 |

## 留史（全部旧版，字节未改）

v1（`../`）、v2（`../revision-v2/`）、v3（`../revision-v3/`）、v4（`../revision-v4/`）全部材料与各级审查原件、冻结快照——一律留史，未改写。
