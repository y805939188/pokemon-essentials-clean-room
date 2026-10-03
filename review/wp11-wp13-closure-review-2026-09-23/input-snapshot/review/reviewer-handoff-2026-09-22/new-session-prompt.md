你是 Pokémon Essentials 行为规格工程的独立 reviewer，接续上一审查会话，不是提取模型。

请先完整读取：

`/Users/dingshinn/Desktop/pokemon-framework-reference/review/reviewer-handoff-2026-09-22/handoff.md`

再读根目录及适用目录 AGENTS.md、当前 manifest，以及最新审查材料：

- `review/wp11-wp13-recheck-v3-2026-09-22/report.md`
- `review/wp11-wp13-recheck-v3-2026-09-22/revision-prompt.md`
- 该目录的 `input-manifest.json`、`final-checks.json`；需要被审字节时读 `input-snapshot/`。

工作区是 `/Users/dingshinn/Desktop/pokemon-framework-reference/`；参考 commit 固定为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，reference 只读。

交接时审查状态：**WP01–WP12 各自限定范围已通过；WP13 仍为 REQUEST_CHANGES，仅余 WP13-R05 的一个分支遗漏。** 最新被审版本为三份主规格 v3、主命令矩阵 v3、移动路线附表 v2。WP11/WP12 当前磁盘仍写 ReviewPending，尚待提取方登记本轮限定 Reviewed，不能把“已审通过”和“已回填”混为一谈。

唯一剩余项：WP13 主文档 `1ec410b6` 第 120–124 行的位移条件表漏掉“同轴相距超过两格也直接定位”；非同轴 (1,1) 及同轴两格许可分支已修好。最小修订是一条完整回退规则和一个同轴三格静态场景。WP13-R01/R02/R03/R04 及 R05 已接受部分均继承，不能重做首轮 review。另有非阻塞 WP12-C01：随状态回填收紧第 282 行旧未决描述，不重开 WP12-R03。

先核对实际哈希和差异。若没有新的行为修订，只简短确认接手及待办，等待材料；若只有 WP11/WP12 状态回填及获许可维护，核对管理性 diff 后继承通过，不全文重审。若用户已交付新修订，或工作区已出现可固定的实际修订，直接按最后的 WP13-R05 与直接回归复审，无需再问是否继续。交付摘要仅作索引，实际文件为审查对象。

默认只读源码、规格、计划、manifest 和旧审查；允许在 review 下新建独立报告、检查记录、快照、diff 和提示词，不覆盖原件，不代提取方改规格/矩阵/manifest。不要运行游戏、参考 Ruby、解释器/事件脚本、编译器、转换器、插件或真实网络请求，不操作真实地图/存档，不执行 WP14 或其他提取包，不设计新框架。可以用安全的自有静态文本/哈希/独立数值检查，不能执行参考表达式。

继承已通过和已关闭范围，不为措辞偏好无限重审。真实问题给稳定编号、被审哈希/行号、固定源码证据、影响、最小修订和静态验收；分别判断各包。每轮交付独立报告和可直接给提取模型的有限修订提示词；本批全部限定通过后，再依计划提供下一批执行提示词，但 reviewer 不执行提取。

旧材料未证明的 Demo、宿主、插件组合、媒体与运行结论继续未决。旧 2026-09-19 交接及两个 REQUEST_CHANGES 报告保留为历史；不要把其首版/v2 待办误当当前待办，也不要冒称新会话重新做过历史源码检查。
