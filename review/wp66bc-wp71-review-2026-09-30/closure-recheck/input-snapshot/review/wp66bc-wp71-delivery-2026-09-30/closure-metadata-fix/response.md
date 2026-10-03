# CLOSURE-R01 登记勘误回应

2026-10-01；规格提取方。依据收尾验收 [report.md](../../wp66bc-wp71-review-2026-09-30/closure-review/report.md)、[revision-prompt.md](../../wp66bc-wp71-review-2026-09-30/closure-review/revision-prompt.md)、[history-corrections.md](../../wp66bc-wp71-review-2026-09-30/closure-review/history-corrections.md) 与 [history-identity-audit.json](../../wp66bc-wp71-review-2026-09-30/closure-review/history-identity-audit.json)。**唯一原编号 CLOSURE-R01：manifest §3 第六十六至六十八轮本批 35 条替代记录中 18 条的完整哈希或版本身份错误，另有一处摘要沿用错误历史哈希。** 三包限定通过与原 14 项关闭不受影响；不涉及规格或行为复审。

## 1. 成因与范围

错误有两类（均为登记叙述层，不影响当前文件与磁盘的匹配事实）：

1. §3 替代记录中 16 条活动材料行的完整 64 位哈希错（前 8 位相同，后缀为凭记忆补写而非从冻结文件实测）；
2. 第 68 轮 manifest 自身行误用 recheck-v2 冻结值（`8b9343a9…`／512,404），应为 recheck-v3 冻结值 `83245b5591b488557921dbff308c511deafae42e1a4cc35b81ed4456480d16c8`／527,363。

当前活动摘要第 44 行的 v3 历史身份同型错误（前 8 位相同）。

## 2. 处理

- **manifest §3 新增「3.1 历史身份勘误」**：18 行逐项（轮次＋文件＋实际前后完整哈希与字节＋被取代的错误记载＋来源快照）；**原历史行保留为当时记录，明确由勘误取代其错误身份字段**，不全局替换同前缀字符串、不扩大到其它包；17 条原记录正确、不受牵连。
- **当前摘要**：v3 历史身份更正为 `edd48222503490a2ab3084e252e56173545ac1e44c2e0e4f4f11d449b8d3bb3c`／4,586（并注明被取代的错误记载）；v2 有限复审日期更正为 2026-10-01；六列身份表分隔行补齐第六列。摘要新身份 `d0b30aeff9a8afc4071a1617a35f9fc9d32714da06002bd2ee0a6ab9d967a0fc`／5,448，已级联当前 TSV 与 manifest §1 行。
- **复核**：更正表 35 条记录的 36 项可测前后身份中 35 项与具名冻结快照逐字节匹配（manifest 自身输出按惯例不自哈希，见 [identity-fix-checks.json](identity-fix-checks.json)）；17 条原正确记录的 34 项可测值中 32 项匹配（2 项同为 manifest 自身输出，按惯例不可测）。**没有凭前缀补写任何完整值。**

## 3. 验证（两层分别成立）

- **当前层**：manifest §1 全部登记行、主 TSV 全部行与磁盘完整哈希／字节／短标签一致；无缺失、重复；新 JSON 可解析；摘要与新材料链接可解析。
- **历史层**：勘误中每个前后身份逐字节对应具名冻结文件；18 条错误均有唯一明确的更正覆盖。
- **保护层**：三包规格、矩阵、其它旧规格、三轮 reviewer 原件／快照、closure-backfill／revision-v2／revision-v3、旧 WP23 回填材料、reference 均未改（白名单与原件核对见 identity-fix-checks.json）。

## 4. 登记

- 差异相对本轮 `closure-review/input-snapshot`，见 [metadata-fix-diffs/](metadata-fix-diffs/) 与 [diff-bindings.json](diff-bindings.json)（重建验证）。
- manifest 续第六十九轮、主 TSV 续 v44（旧行与历史链保留；错误记载标记为已被勘误替代，不宣称其原本正确）。
- 本批状态：三包限定通过且管理性回填完成、原 14 项全部关闭、CLOSURE-R01 已勘误。N01／全局 GR-001～016 整改／B 批整合／未提取包／WP78→WP79→WP80 保持独立范围。

完成本勘误与登记复核材料后停止：不启动新包，不处理 N01／GR／B 整合；未创建任务／Agent、未发其它会话消息、未提交／推送。
