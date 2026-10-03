# WP78 v5 逐项修订回应（R10／R02 最小修订）

2026-10-03；规格提取方。依据 [report.md](../../wp78-stage-review-2026-10-03/recheck-v4/report.md)（v4 复审：**REQUIRES_REVISION——累计 8 项 CLOSED（R01/R03/R04/R05/R06/R07/R08/R09，继承保持）、剩 R02（P3）及新增 R10（P2）；不再重做消费者范围**）与 [revision-prompt.md](../../wp78-stage-review-2026-10-03/recheck-v4/revision-prompt.md)（最小修订：两钩子时序与处置表计数）：2 项按原编号原位修订；已关闭 8 项保持、不从头重审；旧版全部字节留史。作者状态：**REVISED_PENDING_REVIEW**——不自行 CLOSED、不自行 Reviewed。

本轮无规格文件修订（2 项均落在 WP78 交付层；WP36 主稿已正确，未改动）。交付采用**最小增量＋版本索引**（[version-index.md](version-index.md)）：仅 10 份文件以 v5 替代同名旧版；异常注册表（v3）与待证清单（v4）沿用。

## R10（P2，新增）两个 WP36 事件入口被合并写成「生成后触发」（已修）

- **v4 残留**：[consumer-disposition.md](consumer-disposition.md) B03 行与 [revision-response.md](revision-response.md) 同义摘要把 `on_wild_species_chosen` 与 `on_wild_pokemon_created` 一起写成「生成后/生成钩子」。
- **回源**：WP36 §3（45 行——created 钩子描述）/§5.1（135 行——写 `encounter_type`、选择候选后触发 species_chosen）/§6.1（162 行——记录初始形态后触发 created）；reference 只读核对：`012_Overworld/001_Overworld.rb:197–216`（步进：`choose_wild_pokemon` → 触发 `on_wild_species_chosen` → 才走 `allow_encounter?` → `WildBattle.start`）；`002_Battle triggering/003_Overworld_WildEncounters.rb:271–346`（**`choose_wild_pokemon` 返回 `[物种, 等级]`——候选对，尚非已生成个体**）、同文件 383–461（`pbGenerateWildPokemon` 末尾、性格/形态等具名修正之后触发 `on_wild_pokemon_created`）、440–464（`pbEncounter`：触发 species_chosen 后 **`return false if !encounter1`——候选为空的返回**）。
- **修订位置**：[consumer-disposition.md](consumer-disposition.md) B03 行（同一行内分两个具名子入口，不改变清单结构）、[junction-inventory.md](junction-inventory.md) G8-1 行、[consistency-matrix.md](consistency-matrix.md) G8 行、[mappings.md](mappings.md) §1 行、本文件与 [checks.json](checks.json) 验收向量。
- **两具名子入口**：**子入口一 `on_wild_species_chosen`**——面向选择出的候选 [物种, 等级]，**先于该路径的实际个体创建**；普通步进中在**允许遭遇判断之前**触发（通知后才走允许判断）；主动遭遇中通知之后还有**候选为空的返回**——**不能概括成个体已生成**。**子入口二 `on_wild_pokemon_created`**——面向**已创建并完成具名生成修正**的个体，位于**生成末尾**。
- **验收向量（≥2，均静态）**：(1) 普通步进候选选择通知已触发、随后许可拒绝（`allow_encounter?` 假）——**没有因此走到个体创建通知**（reference 197–216 行顺序可复算）；(2) 实际生成个体路径在具名生成修正之后触发 created（`pbGenerateWildPokemon` 末尾、`form_simple` 形态行之后，383–461 行）。以入口前提为限，**不补造「所有调用都必须经过同一选择链」的保证**；插件具体组合验证与这些可静态核对的机制分开（留 P05）。

## R02（P3，残留）处置表计数与摘要矛盾、保留菜单行漏计（已修）

- **v4 残留**：处置表实际 A＝9 行、B＝7 行（A/B 共 16 行），摘要写「A 表 7／总计 15」；对账「本轮已核 10」漏掉两条保留菜单行（WP65-D、WP72 MenuHandlers）；C 表对账条数与消费者行数混用。
- **修订**：[consumer-disposition.md](consumer-disposition.md) A/B 行加**稳定行 ID**（A01–A09、B01–B07）——**主处置互斥单列**、**证据方式可多值另列**、**历史保留/本轮新增另列**；§D 统计**由行 ID 程序化生成**（脚本复算见 [checks.json](checks.json)）：
  - **消费者/接点行**：A 表 9 行（A01–A09）＋B 表 7 行（B01–B07）＝**16 行**。
  - **主处置（互斥）**：**直接/交界覆盖已核 12 行**（A01–A06、B01–B06）；**继承或混合证据已核 3 行**（A07 WP53、A08 WP67-A、A09 WP67-B）；**不适用 1 行**（B07 WP21）——**12＋3＋1＝16**（两条保留菜单行 B05/B06 在 12 之内，不漏计）。
  - **证据方式（另列）**：双方章节 12、交界引用 3（A05/A06/B07）、继承报告 3（A07/A08/A09）、reference 只读核对 1（B03）。
  - **历史保留/本轮新增（另列）**：v3 保留 6 行（A01–A04、B05、B06）；v4 新增 9 行（A05–A09、B01–B04、B07）；v5 修正 1 行（B03）。
  - **C 表**：6 条归类对账（C01–C06，含 C05/C06 两类真正缺证）——**不计入消费者/接点行数**。
- **同步**：[junction-inventory.md](junction-inventory.md)（分解行加 v5 注记）、[consistency-matrix.md](consistency-matrix.md)（处置表统计行）、[mappings.md](mappings.md)、本文件、[checks.json](checks.json)、[report.md](report.md)、[delivery-summary.md](delivery-summary.md) 全部按程序化计数。
- **阅读分布时点标注**：v3 的 1/70/18/20 为**历史**；当前按 [reading-log.json](reading-log.json) 复算为 **1/72/16/20**（全文 1／定点章节 72／头部＋结构 16／结构骨架＋身份 20；文件角色 88／21 不变；本轮仅 WP36 补记区间，类别未变）。
- **既有主计数保持**：54 唯一交界（v5 不增减 ID）、109 路径、N-A～N-F 六类、20 AX/16 交界——v4 核验方已复算通过，本轮仅在实际内容变化处重新生成（处置表统计与 WP36 区间）。

## 已关闭 8 项保持（继承复审结论）

R01（WP10 双 diff）、R03（消费者范围——v4 复审确认关闭）、R04（图鉴）、R05（Mega/Primal 分入口）、R06（编译/反写具名入口）、R07（证据分类多对多）、R08（成长守卫分开）、R09（寄养蛋三具名入口）——本轮仅 R10 同根修订 B03 行时点表述（范围未动）、R02 统计重生成，未再开启其他结论。

## V01（已核·有意管理决策；沿用）

45 份头部滞后全集沿用 v2 枚举（本轮复扫一致）；决策链与措辞不变（当前批准状态及批准范围；不扩为所有旧注记自动免责）。不要求改写 45 份主稿字节。

## E 系（证据不足具名，v5 保留）

E01 备份数据集启用路径（U03/U06）；E02 帐篷档脚本外调用者（U01 系）；E03 全满兜底运行表现（运行验证）；E04 真实插件组合与工具/素材运行结果（P05 重述后范围）。全部落入既有框架。

## 总体自检结果

- R10 两子入口时点与 reference 行序一致（选择→species_chosen→允许判断→生成（修正）→created）；WP36 主稿未改。
- 处置表 16 行＝12＋3＋1（程序化复算通过）；C 表 6 条单列；两条保留菜单行在计。
- 54 项交界清单逐 ID 可复算（v5 不增减 ID）；异常事实 20（AX 编号，v3 注册表沿用）／带异常交界 16／本轮确证错误 0（累计 WP78-R01 已关闭）——三分母分列。
- v5 新材料净化扩展扫描 **0 命中**；全部本地链接可解析（见 [checks.json](checks.json)）。
- 旧版全部字节未动；责任规格未改动。
- U01＋G01–G12 保留；③已证事件链＝0、④运行观察＝0；来源异常保持。
- 状态：**REVISED_PENDING_REVIEW**——2 项均不自行 CLOSED；送 WP78 v5 定点复审。
