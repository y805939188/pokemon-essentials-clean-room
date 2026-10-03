# GR-001 字面样例更正（revision v2）

2026-10-01；规格提取方。依据有界复审 [report.md](../../gr001-gr003-review-2026-10-01/report.md) 与 [next-task-prompt.md](../../gr001-gr003-review-2026-10-01/next-task-prompt.md)：**GR-002、GR-003 已 CLOSED（保持其当前字节不动）；GR-001 的规则修订与 JSON 验收向量已正确，仅样例字符需更正**。本目录只处理这一项；原回应／checks／diff 留史于 `../` 根目录，不改写。

## 问题与更正

- **错误**：WP04 第 81 行 GR-001 括注的 PokeBall 例子，及原回应（`../revision-response.md`）第 17 行（原问题说明）与第 23–25 行（验收表前三行）的样例，把包围符写成了**反斜线 U+005C＋反引号 U+0060**；正确输入必须是**反斜线 U+005C＋双引号 U+0022**。这不是排版差异：非末字段实际含反引号而不含双引号时不会进入双引号重组／剥除分支，原表中该写法标 true 的预期不成立；内部反引号还打断了 Markdown 代码跨度。
- **更正**：WP04 第 81 行样例改为 `` `\"PokeBall\"` ``（已按码点核验：两端均为 U+005C U+0022）。本回应的验收表数据直接取自**已核实正确的** `../checks.json` 的 `static_acceptance_vectors` GR-001 四项（与复审 `literal-checks.json` 的 canonical 向量逐条一致），Markdown 外层代码标记仅用于显示，实际输入不含反引号。
- **范围**：只改 WP04 第 81 行样例与本更正材料；已正确的 §4.2 规则、§9.2 场景、JSON 向量与 WP08／WP10 已关闭内容一律未动；不运行参考分词器或模拟器。

## 更正后的验收表（数据源：`../checks.json` GR-001 向量）

| 输入 | 预期 Flags | 球标志 |
| --- | --- | --- |
| `\"PokeBall\"` | `\"PokeBall\"` | false |
| `\"PokeBall\",Other` | `PokeBall`、`Other` | true |
| `Other,\"PokeBall\"` | `Other`、`\"PokeBall\"` | false |
| `PokeBall` | `PokeBall` | true |

## 身份（磁盘程序化实测）

| 对象 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| WP04 被审修订稿（复审快照冻结） | `63fe6933bdd47f361a96195c138276b94c0919d0286f230a90134ea18b6ba594` | 25,112 |
| WP04 当前（样例更正后） | `6cbb57db365be998ec3d117a61fb388008d2f7c63e6674d23e9f6bcf86880a9b` | 25,113 |

差异仅第 81 行两处 U+0060→U+0022（[revision-diffs/wp04-pbs-lifecycle.diff](revision-diffs/wp04-pbs-lifecycle.diff)，[diff-bindings.json](diff-bindings.json) 已按 patch 精确重建验证）。WP08（`07466254`／20,394）与 WP10（`07ccae9a`／23,833）保持已关闭字节不动。

状态：**GR-001 修订待复审（不自行关闭）**；GR-002／GR-003 保持 CLOSED；GR-004～016、新包、第一组回填与 B 批整合不动；reference 固定 commit、Git 清洁。
