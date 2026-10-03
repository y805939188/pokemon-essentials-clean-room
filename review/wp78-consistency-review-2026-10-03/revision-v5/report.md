# WP78 v5 跨模块一致性审查报告（第五版）

2026-10-03；规格提取方。依据 `review/wp78-stage-review-2026-10-03/recheck-v4/`（v4 复审：**REQUIRES_REVISION——累计 8 项 CLOSED 继承、剩 R02（P3）及新增 R10（P2）；不再重做消费者范围**；最小修订提示）。v5 完成两处最小修订，**送定点复审**；作者状态 REVISED_PENDING_REVIEW——不自行 CLOSED、不自行 Reviewed。旧版全部字节留史。

## 1. 范围与方法

- **范围**：本版仅处理 R10 与 R02 两处；消费者范围、54 项交界清单、已关闭 8 项均不重做。交付采用**最小增量＋版本索引**（[version-index.md](version-index.md)）：10 份文件以 v5 替代同名旧版；异常注册表（v3）与待证清单（v4）沿用。
- **方法**：纯静态文本/哈希/集合/链接/表格计数/固定算术检查；reference 仅只读核对指定行；不运行参考/游戏/编译器/生成器/反序列化/参考行为模拟器。
- **本轮无规格文件修订**（WP36 主稿已正确，未改动；责任规格均未改动）。

## 2. 执行摘要

- **R10（已修）**：WP36 两个事件入口按各自时点分开（同一行内两个具名子入口，不改变清单结构）——**`on_wild_species_chosen`**：面向选择出的候选 **[物种, 等级]**（`choose_wild_pokemon` 返回候选对、**尚非已生成个体**）；普通步进中在**允许遭遇判断之前**触发（通知后才走 `allow_encounter?`——随后被拒绝时**没有因此走到个体创建通知**）；主动遭遇（`pbEncounter`）中通知之后还有**候选为空的返回**（`return false if !encounter1`）——**不能概括成个体已生成**。**`on_wild_pokemon_created`**：面向**已创建并完成具名生成修正**的个体，位于**生成末尾**（`pbGenerateWildPokemon` 末尾、性格/形态等具名修正之后）。证据：WP36 §3（45 行）/§5.1（135 行）/§6.1（162 行）；reference `001_Overworld.rb:197–216`、`003_Overworld_WildEncounters.rb:271–346/383–461/440–464`（只读核对）。验收向量两条静态成立（许可拒绝路径无创建通知；生成路径修正后触发 created）；以入口前提为限，不补造统一选择链保证；插件具体组合留 P05。
- **R02（已修）**：处置表加**稳定行 ID**（A01–A09、B01–B07）并**由行 ID 程序化生成统计**——A 表 9 行＋B 表 7 行＝**16 行**；主处置互斥：**直接/交界覆盖 12＋继承或混合 3＋不适用 1＝16**（两条保留菜单行 B05/B06 在计）；证据方式另列（双方章节 12、交界引用 3、继承报告 3、reference 只读核对 1）；历史保留/本轮新增另列（v3 保留 6、v4 新增 9、v5 修正 1）；**C 表 6 条归类对账（含 2 类真正缺证）不计入消费者行数**。阅读分布时点标注：1/70/18/20 为 v3 历史、当前 1/72/16/20。其余主计数（54 交界、109 路径、N-A～N-F 六类、20 AX/16 交界）经 v4 核验方复算通过、仅在实际变化处重新生成。
- **已关闭 8 项保持**：R01/R03/R04/R05/R06/R07/R08/R09 继承复审关闭结论；仅 B03 行时点表述（R10 同根）与统计（R02）修订，未再开启其他内容。

## 3. 逐项处置（详见 [revision-response.md](revision-response.md)）

| 编号 | 优先级 | 处置 |
| --- | --- | --- |
| R10 | P2（新增） | 已修：两具名子入口（候选选择通知先于创建、且可在许可拒绝/候选为空时单独发生；创建通知位于具名生成修正之后） |
| R02 | P3 | 已修：稳定行 ID＋程序化统计（16＝12＋3＋1；C 表 6 条单列；保留菜单行在计；历史/本轮另列） |
| R01/R03–R09 | —（已关闭） | 继承，未再开启 |

## 4. 阅读范围（诚实登记；两维度独立成列）

阅读方式：全文 1（WP77）／定点章节 72／头部＋结构 16／结构骨架＋身份 20＝109；文件角色：主规格/合同文档 88／附表/数据文档 21＝109；v5 新增补读：WP36 §3（45 行）/§5.1（135 行）/§6.1（162 行）与 reference 四段定点（只读）。

## 5. 量化统计（单位分列）

交界 54（组 9；v5 不增减 ID）；处置表 16 行＝12＋3＋1（程序化复算）；C 表 6 条单列；异常事实 20（AX 编号，v3 注册表沿用）／带异常交界 16／确证规格错误本轮 0（累计 WP78-R01 已关闭）；证据不足具名 4（E01–E04）；待证 8（P01–P08）、不适用 6 类（N-A～N-F）；本轮规格修订 0 份；管理轮次第 140 轮（登记 v5 材料）。

## 6. 独立复审入口

- v5 材料全集：本目录 [consumer-disposition.md](consumer-disposition.md)、[junction-inventory.md](junction-inventory.md)、[consistency-matrix.md](consistency-matrix.md)、[mappings.md](mappings.md)、[revision-response.md](revision-response.md)、[reading-log.json](reading-log.json)、[input-manifest.json](input-manifest.json)、[checks.json](checks.json)、[report.md](report.md)、[delivery-summary.md](delivery-summary.md)、[version-index.md](version-index.md)；沿用 [anomaly-register.json](../revision-v3/anomaly-register.json)（v3）、[pending-and-na.md](../revision-v4/pending-and-na.md)（v4）；v1–v4 留史于 `../`、`../revision-v2/`、`../revision-v3/`、`../revision-v4/`。
- 重点核验建议：(1) B03 行两子入口与 WP36 §3/§5.1/§6.1 及 reference 197–216/271–346/383–461/440–464 行序对照；(2) 处置表行 ID 与 §D 统计的程序化复算；(3) 保留菜单行 B05/B06 计入情况；(4) 阅读分布历史/当前时点标注。
- **阶段门**：本复审通过后才进入 WP79（WP79→遗漏修订复审→WP80 串行；WP80 消费 WP79 审定后的覆盖基线）；需要独立复审时停在阶段门。

## 7. 状态

**ReviewPending（WP78 v5，待定点复审）**。不自行宣布全项目完成；不进入 WP79/80；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 只读、Git 清洁；未创建任务/Agent、未跨会话发消息、未提交/推送；未运行参考/编译器/游戏/反序列化/参考行为模拟器。
