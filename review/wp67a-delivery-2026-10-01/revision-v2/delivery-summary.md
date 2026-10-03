# WP67-A 首审修订 v2 交付摘要（R01–R14／C01–C02）

2026-10-01；规格提取方。依据 `review/wp67a-review-2026-10-01/`（REQUEST_CHANGES：14 P2＋2 P3；执行提示）。**本轮只修订 WP67-A 首版 16 项**，完成送定点复审，不启动 WP67-B。

- **主稿**：`specs/ui/wp67-a-battle-interaction-and-presentation.md`，v1 被审 `b6fdd96a`／71,691 → v2 当前 `f5ac2a269cff135f9539af8a3d69f79c356150aad740f36a09335342497dd1b2`／85,929（磁盘程序化实测）。相对审查 input-snapshot 的 diff 11 个 hunk、patch 精确重建（[diff-bindings.json](diff-bindings.json)）。
- **状态**：**ReviewPending（v2，R01–R14／C01–C02 已修订待定点复审）**；作者状态 REVISED_PENDING_REVIEW——不自行关闭、不自行 Reviewed。
- **场景**：K01–K42 保留（14 行修订）＋新增 K43–K56 对照，共 56 个定义行、全文唯一。
- **入口附表**：[entry-coverage-table.md](entry-coverage-table.md) 自 v1 的 54 行出发修订受影响行；**本版八组数据行机械实测 9／7／9／7／6／6／8／7＝59 行**（C02；首版摘要"40 行"之误在此更正，v1 材料留史不回写）。
- **逐项回应**：[revision-response.md](revision-response.md)（16 项：原错误／回源路径行段／修订位置／静态对照／附表行）。
- **自检**：[checks.json](checks.json)——逐项验收向量、56 场景唯一性、全文残留扫描（16 项同根旧句全部为空）、附表实测计数、上游保护。
- **来源身份**：[source-identities.json](source-identities.json)——基线 65/65 复核不变＋v2 新增 4 份定点来源（Battler 两份、Challenge_Battles、PBS/moves.txt）磁盘实测身份。
- **上游保护**：WP38／WP41／WP42／WP56／WP58 批准合同仅按报告指示更正本稿转述、字节未改；WP65 已批准范围与 GR-001～016 保持；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，Git 清洁。

## 修订主题速览

- **取消/返回层级**（R01/R02）：物品按"列表→Use/Cancel 子菜单→成员/目标"分层；队伍成员命令取消只回成员列表、列表取消才服从 canCancel；场景返回值与战斗包装结果分列。
- **显示与游标**（R03/R04/C01）：非单打零目标类别也进目标窗口（整体高亮不可移动）、目标三态分列；命令框初始下标 0（Yes/No 初始 Yes、满队初始 Add to your party）、BACK 返回值非游标；图形菜单 total_pp≤0 不绘制 PP 文本。
- **等待与时点**（R05/R08/R14）：abortable 仅快进文字、计时与驻留保留；多个体派出并行推进、各数据框只等自身球动画；经验消息先于暗影分支、空槽学招两段写入、满槽双写先于 Ta-da。
- **捕获与投球**（R06/R07）：图鉴消息/条目需持图鉴＋已解锁（记录照写）、多个体逐个完成；容量门=队伍且仓库同时满；无存活队友直接触达在状态查询先失败。
- **特殊模式**（R09/R10/R11/R12/R13）：Call 睡眠/命中仅属非暗影；回放常规无菜单＋条件化目标窗口例外；替补提议实际门与回合末逃跑差异；Palace 无力非挣扎、危机门完整；Arena 换人入口保留、自动替补分列。

## 停止点

16 项修订完成并备齐材料，停止送定点复审；不自行关闭 16 项、不自行 Reviewed；不启动 WP67-B、集中回填、B 批整合或整体 double review；未创建任务／Agent、未发跨会话消息、未提交／推送。
