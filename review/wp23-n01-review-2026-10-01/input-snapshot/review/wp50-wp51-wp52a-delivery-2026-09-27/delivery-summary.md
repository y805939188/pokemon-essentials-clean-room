# WP50 → WP51 → WP52-A 交付摘要 v3（有限复审闭合后管理回填）

2026-09-28；提取侧管理维护，非独立review、非WP80 sanitized。**三包均Reviewed（各自限定静态范围）**：WP51首审通过及回填接受；WP50/52-A有限复审PASS_SCOPED。依据[独立复审报告](../wp50-wp51-wp52a-recheck-2026-09-28/report.md)与[下一批提示](../wp50-wp51-wp52a-recheck-2026-09-28/next-batch-prompt.md)。

## 1. 版本和闭合

v1首稿；v2两项有限修订、C01及WP51管理回填；v3本次WP50/52-A限定Reviewed回填、必要身份传播与两个新增场景段落表格连接，111条输入/期望不变。旧revision-response/9份diff与前批backfill-response/18份diff原件保留，只重建到对应被审快照。新字节不冒充被审v2；附表WP50本次被审仍v1，WP51/52-A被审为v2。

WP50-R01、WP52-A-R01、BATCH-C01均CLOSED。false半血无需贪吃及五果代际门、三墙同侧存活人数25/19、WP51存在性/天气抑制合同不再重写。前批WP40/41三观察及WP46/47维护回填已接受，范围不重开。

限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP51（WP47为A/B）、WP52-A、WP59–WP60。WP52整个族、设施或运行没有一并通过。

## 2. 当前身份与本轮被审身份

| 文件 | 当前SHA-256 | 当前字节 | 本轮被审SHA-256 | 被审字节 |
| --- | --- | ---: | --- | ---: |
| [wp50-held-item-triggers-and-consumption](../../specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md) | `6c97afebe925f9cbe4aedfb1deb815b1d3277bd952ceae04e532887a16cd9627` | 32,132 | `fcbbca67dafbb1aaa1cfd2560983a6f34830c31c11feccb7688f08b372a395b1` | 31,648 |
| [wp50-held-item-effect-coverage](../../specs/pokemon-rules/wp50-held-item-effect-coverage.md) | `f62603f26e7570e32949ebce97c531ef0af59ba6da4f083bff9d85775de2fc69` | 14,418 | `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686` | 13,855 |
| [wp51-ai-action-selection-and-skill](../../specs/combat/wp51-ai-action-selection-and-skill.md) | `8deea695576b9786d5026dd9a66ce7ea3c4dc7d3332b88891d23a8998c6b87a0` | 27,283 | `baebd58a7f4eed635f685f583fa7b4d21785a9ac13a0a1ee4c2ccd6ec7b6bac5` | 26,784 |
| [wp51-ai-decision-defaults](../../specs/combat/wp51-ai-decision-defaults.md) | `5069a3690c6886204ebe9877ff0165e77c4c437fb8273032ac9d6f52bf89c2d0` | 5,472 | `5069a3690c6886204ebe9877ff0165e77c4c437fb8273032ac9d6f52bf89c2d0` | 5,472 |
| [wp52-a-generic-numerical-and-status-evaluation](../../specs/combat/wp52-a-generic-numerical-and-status-evaluation.md) | `5cdc3edf5c14428166215d2b5b214eee95e751cd58902fe6047cd47eb4489c5e` | 48,733 | `6c0534fea6d4a18284c1e54a38e413ad010d38291088b0df45d8ac087ca44c9c` | 48,127 |
| [wp52-a-evaluation-coverage-and-data](../../specs/combat/wp52-a-evaluation-coverage-and-data.md) | `fa760facb18685586550f4a831c30616e4503942e2e170eaf605afa517ed868b` | 59,366 | `a5a13acaf8572fa621b91911430b2286b23340618c72d4b5d2e1522aaf4ec5f9` | 58,772 |

更早首稿v1完整值由各稿历史、manifest替代链和本轮input-snapshot保留；WP51默认附表当前字节未变。

## 3. 已通过范围与保留

WP50 A～F32族196持物身份、计算/有效性/普通强制触发/消费写回与直接核心；WP51 A～E控制技能/换人资源/选择权重回退；WP52-A A～F共同失败/合成/22通用修正/粗数值/状态阶级类型能力、164效果/334登记与267评级数据。原33/25/53共111场景和28常数作为已审证据保留，不假称动态运行。

self/boundary为v3，revision_history保留v2语境；当前绑定更新为已限定通过回填版。原登记的B/C只是当时定位，实际后续展开见新批摘要；全部运行/插件/设施与WP79保留。

## 4. 当前维护材料

| 文件 | SHA-256 | 字节 |
| --- | --- | ---: |
| `planning/feature-matrix.md` | `529569423b895c73026c47d6eef6745dfb387b09d37859f1527cb47f8cd9276d` | 50,343 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/self-checks.json` | `6e83255802631e198518cd5178f75ec4204498ae2a0d2b92592e6b69b87f13bc` | 464,719 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/boundary-checks.json` | `26acad41c8a5f49468d0aeeffd5e9584770c8f74947dd64066da5cffc323d256` | 49,349 |

本次回填差异与12件预检见[新批回填回应](../wp52b-wp52c-wp54-delivery-2026-09-28/backfill-response.md)。主TSV v30/manifest第五十五轮登记当前回填与新批，清单不自哈希。

## 5. 新批与停止

已按授权串行完成[WP52-B→WP52-C→WP54首稿](../wp52b-wp52c-wp54-delivery-2026-09-28/delivery-summary.md)，新包只ReviewPending，批末统一送审。WP54-N01是新条款入口观察、待独立判断，未回改旧规格。未启动WP55或其它第四包；运行/Demo/宿主/媒体/插件/U01–U10及WP78→79→80保留，不发reviewer消息、不创建任务/Agent、不提交推送。
