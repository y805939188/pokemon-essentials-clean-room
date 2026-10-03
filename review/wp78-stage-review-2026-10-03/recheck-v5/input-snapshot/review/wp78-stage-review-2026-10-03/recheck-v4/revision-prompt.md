# WP78 v5 最小修订：两钩子时序与处置表计数

工作目录：`/Users/dingshinn/Desktop/pokemon-framework-reference`。

先读 AGENTS.md、`review/wp78-stage-review-2026-10-03/recheck-v4/report.md`、`findings.md`。v4 为 REQUIRES_REVISION，但 **R03 已关闭**；R01/R03/R04/R05/R06/R07/R08/R09 共八项保持 CLOSED。仅处理 **新增 R10（P2）与 R02（P3）**，不再扩展消费者范围、不从头重做 WP78、不开始 WP79/80。

在新 `review/wp78-consistency-review-2026-10-03/revision-v5/` 固定输入与最小增量。保留旧版全部字节。可以复用未变化的 v4 文档，通过当前版本索引明确哪些文件被替代；不要为了改版本号重写全部映射或责任主稿。

## R10：分别描述两个事件入口

回读 WP36 §4.5、§6、主动遭遇入口；必要时只读 `Data/Scripts/012_Overworld/001_Overworld.rb:197–216` 与 `002_Battle triggering/003_Overworld_WildEncounters.rb:440–464`。

- `on_wild_species_chosen`：面向选择出的候选物种/等级，先于该路径的实际个体创建。普通步进中通知之后才走允许遭遇判断；主动遭遇中通知之后还有候选为空的返回。不能概括成个体已生成。
- `on_wild_pokemon_created`：面向已经创建并完成具名生成修正的个体，位于生成末尾。

修 consumer-disposition 的 WP36 行和 revision-response 的同义摘要，并核对 inventory/matrix/mappings/checks 中引用这些时点的表述。可在同一行内分两个具名子入口，避免不必要地改变清单结构。保持插件具体组合验证与这些可静态核对的机制分开。

验收向量至少两项：普通候选选择通知已触发、随后许可拒绝，没有因此走到个体创建通知；实际生成个体路径在生成修正之后触发 created。以入口前提为限，不补造所有调用都必须经过同一选择链的保证。WP36 主稿已正确，不改它。

## R02：按稳定行 ID 生成全部统计

v4 A 表实际9行、B表7行，A/B共16个消费者/接点行。若将 WP53/WP67-A/WP67-B 三行归为“继承或混合证据”的互斥主类别，则其余直接/交界覆盖为12行，另1行不适用：12＋3＋1＝16。两条 B 表保留菜单行不能漏计；历史保留/本轮新增应是另一列，不能与主处置混用。

C 表是6条归类对账，含2类真正缺证，不能加到消费者行数中。为 A/B 每行加稳定 ID，固定互斥的主处置及可多值的证据方式，再用文本/集合脚本生成统计；若实际拆行，则按新 ID 重算，不硬套16。

同步 consumer-disposition §D、report、response、summary、checks 和所有相关数字。回应中的旧阅读分布1/70/18/20应标明历史，当前值按 reading-log 复算为1/72/16/20（若本轮再改阅读范围，则以实际新清单为准）。原 N-A～N-F 六类及54交界、109路径、88/21角色、20 AX/16交界已通过，仅在实际内容变化时重新生成。

## 交付和停止点

提供两项最小修订、准确受影响范围、静态向量、文件差分/版本索引及程序化计数；作者仅标 REVISED_PENDING_REVIEW。复用已关闭八项，不再开全域补审。登记按当前磁盘版本串行更新、追加历史，核验 TSV/manifest、旧文件保护和 reference 清洁。

完成后停止送定点复审。通过后才进入 WP79，再按遗漏闭环及独立复审门衔接 WP80。reference 固定 HEAD 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b，只读；不运行参考/游戏/编译器/反序列化/行为模拟器，不实现框架，不创建 Agent/聊天，不跨会话发消息，不提交推送。
