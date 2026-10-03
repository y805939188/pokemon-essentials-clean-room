# CLOSURE-R01：仅修历史身份登记

在 `/Users/dingshinn/Desktop/pokemon-framework-reference` 工作。先读本目录 [report.md](report.md)、[history-identity-audit.json](history-identity-audit.json)、[history-corrections.md](history-corrections.md)、[proposed-metadata-corrections.diff](proposed-metadata-corrections.diff) 和 [input-manifest.json](input-manifest.json)。

当前结论：**三包规格已限定通过，两包管理性回填 ACCEPTED；原 14 项全部 CLOSED。只有一个登记问题 CLOSURE-R01 需补修。** 不改规格、不重审玩法、不重做此前已通过的修订。

## 1. 预检与取值规则

复测本轮 1036 个当前输入／快照、5 个外部输入及 `review-artifacts.json` 中的 reviewer 原件。reference 必须维持固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 且 Git 清洁。

历史哈希／字节只能从明确的冻结文件计算并核对，不得凭前缀填写完整值，不得用更早一轮的同名文件代替指定轮次。更正表包含每项实际来源快照；重新测量后再写入。

## 2. 修正范围

本轮历史审计固定为 manifest §3 的**第六十六至六十八轮、本批 35 条替代记录**：其中 18 条有错（5＋6＋7）。只修这些具名身份及当前摘要的关联历史尾注，不扩查或批量清洗其它旧包。

采用追加勘误方式保留历史：

- 在**当前 manifest** 中新增历史身份勘误，逐项注明轮次／文件、实际前后完整哈希与字节、替代的错误记载。原历史行保留为当时记录，明确由勘误取代其错误身份。
- 使用 `history-identity-audit.json` 的 expected_before／expected_after 及快照路径，重新从字节复测。manifest 自身不自哈希，该历史行只修正指定轮次的输入身份。
- 当前活动摘要的 v3 历史身份改为 `edd48222503490a2ab3084e252e56173545ac1e44c2e0e4f4f11d449b8d3bb3c`／4,586；同时将 v2 复审日期更正为 2026-10-01，修正六列身份表的分隔行。

建议差异 `proposed-metadata-corrections.diff` 只覆盖上述正文更正，并未应用。可以在确认当前输入一致后采用，但**应用后仍须计算新摘要身份、更新当前登记和生成本轮材料**。不要沿用更正前摘要的当前哈希。

尤其核对第六十八轮 manifest 的输入应为 `83245b5591b488557921dbff308c511deafae42e1a4cc35b81ed4456480d16c8`／527,363（recheck-v3 冻结），不是 512,404 字节的更早版本。

## 3. 可写与不可写

可写：

- `planning/review-manifest-2026-09-19.md` 的本轮具名历史勘误、必要当前条目／本轮登记与说明。
- `review/wp66bc-wp71-delivery-2026-09-30/delivery-summary.md` 的上述勘误、当前状态及新材料链接。
- `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` 的必要当前身份传播及新材料登记。
- 新建 `review/wp66bc-wp71-delivery-2026-09-30/closure-metadata-fix/`，保存本轮回应、实测清单、更正检查、差异／绑定。若目录已存在先辨认，不覆盖旧工作。

不可写：三份规格、矩阵、其它旧规格；所有 reviewer 原件／快照；旧 closure-backfill／revision-v2／revision-v3 的回应、差异、检查与固定身份；旧 WP23 回填材料；reference。错误存在于**当前历史记载**，不授权改动被冻结的原文件或抹掉当时错误记录。

活动摘要已是本轮可写材料，补修后按新身份登记；其它当前活动 JSON 无本次必要变更就保持。原 closure-backfill 的差异／绑定是当时版本的历史证明，不要重写成新当前结果。

## 4. 必须分别验证的两层

1. **当前层**：manifest §1、主 TSV、当前摘要及新增材料的完整哈希／字节／短标签一致；无缺失、重复和悬空链接，JSON 可解析。
2. **历史层**：新增勘误的每个前后身份，逐字节对应更正表具名的冻结文件；35 条原记录中 17 条原本正确，18 条错误都被明确且唯一的更正覆盖。不能仅证明哈希长度为 64 或前 8 位相同。

本轮回应清楚列出一个原编号 CLOSURE-R01 的处理，保留三包通过／14 项关闭状态；登记表中的旧错值标记为已被勘误替代，不宣称它们原来就是正确的。差异相对本轮 `closure-review/input-snapshot`，重建并绑定最终目标；摘要修改后必须由磁盘重算新身份，再级联 TSV／manifest。

证明所有规格、矩阵、旧交付目录、各轮 reviewer／快照及 reference 均未改。自检完成后交付并停止，仅送一次登记复核；不启动新包、不处理 N01／GR／B 整合或 WP78～80。

允许自有文本／哈希／JSON／差异与固定算术；不运行参考代码／表达式、游戏、解释器、生成器、编译／转换、插件或网络；不操作真实地图／存档／输入；不实现框架；不创建任务／Agent、不发其它会话消息、不提交／推送。
