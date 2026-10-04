# B02-I 实际核验命令记录

2026-10-04，R-B02；仅Git/文本/JSON/身份审查，非参考程序或静态向量执行。

1. 读取AGENTS.md；用rg --files检查项目和/workspace/.agents适用技能。本项目本地SKILL.md未发现。
2. 普通 `git fetch origin 1b1e169faf273e89ad6b7f5e46fd7b60d87d3946`；`git ls-remote --heads origin refs/heads/remediation/20261003-prepare/integration`精确回读同SHA。
3. 从送审SHA创建独立 `remediation/20261003-prepare/review-B02-integration-1`，不合入main，不改integration。
4. 从固定Git直接读取并重建BASE→TARGET、CAND→TARGET、PAYLOAD→TARGET完整diff，使用 `--binary --full-index --no-renames --no-ext-diff --no-textconv`，无路径排除。完整补丁存/tmp，哈希/长度/路径集存本报告complete-diff-manifest.json。
5. 读取integration-stage-1十份交接/台账/哈希/计数/JSON/两payload补丁及三文件证据增量。大重复对象按候选作者/独立报告/原finding固定对象精确比较，独立判断所有新公共文字、字段、路径及状态。两payload补丁按原Git重建精确相等，不运行任何代码补丁。
6. 核实际十三正式字节、作者三十/报告十二字节、35依赖/58哈希、B01保护段与历史原文、十二登记映射/严重度/别名/有效限定、229OPEN/0关闭，独立核八导航/旧行保留/引用范围及30真实Markdown链接。
7. 固定参考独立Git在/tmp/r-b02-reference，git rev-parse HEAD/HEAD^{tree}、status --porcelain核固定SHA/tree/clean；只读路径/blob/原始文本。Scene_Map240–250本轮再次以nl/sed静态读取；其他七导航只核身份及范围，不称全文阅读。
8. 复核B02与B03合同、B01/B02-I/PRE0锁、物理/语义依赖和WP36等残留条款。未启动下游或执行参考。
9. 独立验证入口：`python review/remediation/20261003-prepare/batches/B02/integration-review-1/verify-integration.py`。最终62 PASS、0 FAIL。首次脚本把目录README计入17静态目录文件，且把作者表已归一化目标再次作相对路径拼接，产生两项脚本误报；修正计数口径与真实href解析后全部通过。无候选/整合内容修改。
10. 发布前检查本目录JSON/链接/结论/范围及git diff --cached --check，仅新增本integration-review-1材料。普通commit/push后，在提交外记录真实报告SHA、精确远端回读、报告父=送审SHA及两个Git clean结果，避免自引用。

请求Ultra/Standard，实际三项UNVERIFIED；未请求降级/加速/派生。参考运行0、运行观察0、Demo链0、静态向量执行0。原报告和正式材料只读。
