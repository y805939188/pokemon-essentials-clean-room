# 项目交接：Pokémon Essentials 行为规格提取工程（2026-09-26，WP26–WP30 闭合复审后；回填＋WP31→WP28→WP29 待执行）

> 本文是会话交接恢复材料，取代 `handoff-2026-09-26.md`（旧文件保留作历史，不覆盖）。请先完整读本文，再按其中引用的文件深入。**本文件不是规格、审查通过报告或交付物，不入 manifest 版本表。** 文中所有哈希/字节为 2026-09-26 本会话实测。

## 1. 项目使命与硬约束（不可违反）

工作区：`/Users/dingshinn/Desktop/pokemon-framework-reference/`

目标：研究 Pokémon Essentials（参考实现），提取**行为规格**（可观察行为、游戏规则、功能需求、领域概念、状态转换、数学规则、输入输出、边界条件、用户工作流、功能依赖、兼容要求），供后续**独立 clean-room 实现**使用。

角色：参考实现研究员 / 行为规格提取员 / 需求分析员——**不是** Ruby→TypeScript 迁移工程师，**不是**新框架实现工程师。

- 根 `AGENTS.md` 为最高约束（clean-room、参考源码只读、不复制源码、不设计未来框架结构/API、实现无关、一次一个工作包/获批批次）。
- 参考基线（WP01 固定）：commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`git describe` = `v21.1-23-g8c5911e4`；**不等于**未修改的官方发布包，U02 开放）。reference 全程只读；不 fetch/pull/切换基线；不生成补丁。
- **禁止**：运行游戏、Ruby、编译器、参考脚本/表达式、插件、网络请求；操作真实地图/存档/输入；创建 TS 包/MZ 插件/引擎适配器/战斗实现等任何生产框架代码；自动提交/推送；自行创建并行 Agent；自行启动未获授权的批次/包。
- **证据纪律**：材料不能证明的内容保持"未知/推断/待验证"；"搜索未命中 ≠ 不存在"；"方法存在 ≠ 实现"；"return 值 ≠ 业务成功"；"注释 ≠ 实际行为"；缺失 demo 不阻塞无关静态范围，但要具名保留。
- **哈希纪律**：一律 `shasum -a 256` + `stat -f "%z"` 实测；**禁止凭前缀推补完整值、禁止凭记忆填字节数**。修订/回填前先对照被审固定版本；被审哈希与新哈希分开记录，新哈希不伪称为复审对象。
- 不修改 `review/` 下 reviewer 原件（报告/提示/检查/快照）；新增一律用新文件/新目录。记录每轮开始/结束的工作区差异；不清理或覆盖用户已有工作。

## 2. 材料与基线现状

- `reference/pokemon-essentials/`：`Data/Scripts/`（核心脚本，只读）、`Data/Scripts.rxdata`、`messages_core.dat`、**`PBS/` 数据样本**（`pokemon.txt`、`trainers.txt` 等，可用于内容/数据核对）、各世代与 Shadow PBS 备份目录。**缺**：Graphics/Audio/Plugins/全部地图、事件、Game.ini、系统数据（U01 开放）。
- 总控文档：`analysis/repository-overview.md`（18 领域、113 功能、34 证据包 E01–E34、U01–U10）、`planning/module-map.md`、`planning/feature-matrix.md`、`planning/extraction-plan.md`（87 工作包 + §2.1 状态约定）。**每轮以 manifest（`planning/review-manifest-2026-09-19.md`）与矩阵为准。**
- 状态约定（extraction-plan §2.1，沿用）：包/功能状态最小集合 **Drafted / ReviewPending / Reviewed（注明范围；自检不能标 Reviewed）/ Partial / Blocked**；每包分离"自身声明范围 / 必须满足的完成依赖 / 前向引用（目标包、主题、未闭合内容、影响范围、复核触发条件）"。**"限定范围通过 ≠ 整行完成"**：矩阵用"Reviewed 对应子范围＋前向 Inventoried"，不整行笼统完成。
- 每轮节奏：读计划行与相关 review → 明确范围与不做项 → 定位证据（定义/调用者/配置/数据/UI 消费者）→ 提取行为 → 写规格与静态场景（标"静态推导、未运行"）→ 检查交界（已定义规则引用不复制）→ 更新追踪（矩阵/manifest/未决）→ **停止并交付 review**。
- 交付约定：修订回应写 `revision-response.md`、逐文件差异写 `revision-diffs/`（相对该轮 `input-snapshot/` 的 `diff -u`）；回填/批次差异、交付摘要放入（新）交付目录；manifest 每轮登记被审/回填哈希（分开）、替代关系与新轮次；TSV 主表（`review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv`）延续更新、**不丢旧当前项**；manifest/TSV 自身不自哈希，最终实测值写入交付消息。

## 3. 当前进度总览

### 3.1 包状态（截至本会话结束，2026-09-26）

- **WP01–WP21、WP24、WP25：限定 Reviewed**（各包范围见 manifest §1/§2.1 与各规格头部）。
- **WP26、WP27、WP30（v3）：PASS_SCOPED（2026-09-26 闭合复审），待管理性回填 Reviewed**——三包现文件头部仍为 ReviewPending 措辞；回填是下一次会话的第一项工作。回填后限定通过集合 = **WP01–WP21、WP24–WP27、WP30**；WP22/WP23/WP28/WP29 未完成，**不得写成"WP01–WP30 全部通过"**。
- 下一步授权批次：**WP31→WP28→WP29**（串行，逐包自检固定版本，批末统一送审后停止）。
- 本批（WP26–WP30）评审历程：首审（13 项必修＋2 维护）→ v2 → 复审（8 项关闭、剩 5 项）→ v3 → 闭合复审 PASS_SCOPED（最后五项与 C01/C02 全部关闭、未发现直接回归；C03 记法维护随回填同步、无需再等短审）。

### 3.2 关键固定值（本会话实测；更全表见 manifest §1 与闭合报告 §1）

| 对象 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/creature-rpg/wp26-acquisition-gifts-and-script-trade.md`（v3，被审） | `afc7214aa636369021e2bb1d71daa536e78170c850d2a09e58a075367e13bbe9` | 35,387 |
| `specs/creature-rpg/wp27-bag-and-item-storage.md`（v3，被审） | `969cb37c0d38cc27ad97c178f821debdef394a6e3fdf6492847a799faf914c67` | 27,166 |
| `specs/creature-rpg/wp30-growth-learning-and-friendship.md`（v3，被审） | `41e71624796647479e6428a13f04838010bfb97e44cbb2316927cdc70a669117` | 36,040 |
| `planning/feature-matrix.md` | `6b49c40b3508f8863500a8e36ca8ddf9960e3f411a42ed9f508007e9ceccdf0a` | 41,342 |
| `planning/review-manifest-2026-09-19.md` | `88af4e6d88306f6bcb913e66bfc0b7146dd5c75d77f0c9c9b836d65570ec4156` | 112,415（§1 当前版本行 179 条；自身不自哈希） |
| `review/wp26-wp27-wp30-delivery-2026-09-26/delivery-summary.md`（交付摘要 v3） | `df4926ae7007de65c6b4b4bcaa85b35956b9e065a6531710a5ec43f7aee11109` | 11,682 |
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv`（TSV v10 主表） | `35cd3605987cc8778cf30d9296e7cea3da073c446750b845a631368a9545b9fa` | 11,707（85 行 = 2 行注释 + 83 条记录） |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/report.md`（闭合报告） | `21712a5c8715b793e18f2426868685f6e83caccf4e3f59eee083daef7e6d6e29` | 11,449 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/next-batch-prompt.md`（闭合提示） | `8091fed24599616048b6b2ac83b25fba4bebc0070b96eed18e1c79d319e58fda` | 12,982 |

本会话末次全量自检：manifest 179 行、TSV 83 行，**0 不一致**（脚本见 §6）。
说明：闭合报告与提示**尚未登记入 manifest**（§1 未含）；下一个回填轮需按惯例补登（§1＋§4，配合提取侧回应/差异、交付摘要与 TSV 更新）。

### 3.3 本轮 review 原件（已归档；新会话必须完整读原文）

目录 `review/wp26-wp27-wp30-closure-review-2026-09-26/`：

| 文件 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `report.md` | `21712a5c8715b793e18f2426868685f6e83caccf4e3f59eee083daef7e6d6e29` | 11,449 |
| `next-batch-prompt.md` | `8091fed24599616048b6b2ac83b25fba4bebc0070b96eed18e1c79d319e58fda` | 12,982 |
| `input-manifest.json` | `a7c303750debf8adb2c2f36f5d05516b3ce07c6bbd3adb623ac0942f608a9eb0` | 113,632 |
| `current-hashes.tsv` | `b2d4dc7fcad71a76b3b95a113abb7388df61b7b9890367bfb919028f5beeefd5` | 24,945 |
| `changes-from-v2.diff` | `23ad4a7cc7b21b32454fb71666093eefd97f66b636382df913c6b32b16a7298e` | 99,411 |
| `diff-checks.json` | `0eb2cd90438e26190d6756c95ea226ae62a8b5f904261fb7891fcb6bbc9ce391` | 1,674 |
| `source-checks.json` | `5edade54951848612ae8ac1cf3f2d42f9cfd91c7e1ea729e362ef0e6c281c7ed` | 8,661 |
| `static-checks.json` | `155addb33407eca3c3c1fc156339c9ef8bc50882cdfec19c489febaef381debe` | 1,937 |
| `final-checks.json` | `dfcfad8acfaa9eb433bc8c84e16695a2c89b9e3bd77730e844927eac6beb3ecd` | 2,354 |

`input-snapshot/`：回填 diff 的**基准快照**（v3 字节；镜像含三规格、矩阵、manifest、AGENTS.md 与既往 review 材料）。已复核：快照内三规格 = 被审 v3 三哈希（`afc7214a`/`969cb37c`/`41e71624`）、快照矩阵 = `6b49c40b`、快照 manifest = `88af4e6d`，与本会话实测一致。回填差异基准路径形如：
`review/wp26-wp27-wp30-closure-review-2026-09-26/input-snapshot/specs/creature-rpg/wp26-acquisition-gifts-and-script-trade.md`。

**结论摘要（细节以原文为准）**：WP26、WP27、WP30 均 **PASS_SCOPED**（限定静态范围）；最后五项 WP26-R02/R04、WP27-R01/R02、WP30-R05 全部关闭、未发现直接回归；上轮 8 项与 C01/C02 继承关闭；C03 非阻塞记法维护可随回填直接同步、无需再等短复审。授权：**先回填 Reviewed，再执行 WP31→WP28→WP29**，逐包自检固定、批末统一送审。

### 3.4 review 归档目录一览（不改写；新增用新文件）

`review/` 下各轮目录：wp01～wp17 系列（review/recheck/closure）、`wp18-wp20-review / -recheck / -closure-review`、`wp21-wp25-review / -recheck / -closure-review`、`wp26-wp27-wp30-review / -recheck / -closure-review`；提取侧交付目录：`review/wp18-wp20-delivery-2026-09-26/`（含 TSV 主表 v10）、`review/wp21-wp25-delivery-2026-09-26/`、`review/wp26-wp27-wp30-delivery-2026-09-26/`（摘要 v3 ＋矩阵合并差异 `c8b70094`/12,628）；各轮 `revision-response.md`/`revision-diffs/` 在对应轮次目录内。

## 4. 下一步待办（新会话执行清单，按顺序）——权威执行细节以闭合提示 `next-batch-prompt.md` §2–§8 为准

### A. 预备

1. 读根 `AGENTS.md`、本交接、闭合报告与提示全文（§3.3 两份原件）、`input-manifest.json`、闭合轮 `current-hashes.tsv` 与各 checks json；读 `planning/extraction-plan.md` §1/§2.1（含 WP28/29/31 行）、manifest §1/§2/§4、矩阵相关行；完整读三包当前 v3 与上两轮回应（`review/wp26-wp27-wp30-review-2026-09-26/revision-response.md`、`review/wp26-wp27-wp30-recheck-2026-09-26/revision-response.md`）以知已关闭范围。
2. **复算六项固定对象**（§3.2）并与闭合报告 §1 / `input-snapshot/` 对照；有差异先登记差异及其是否超出授权，不倒称变化后的字节已被审；不覆盖 reviewer 快照。

### B. 回填 WP26/WP27/WP30 → Reviewed（限定静态范围）

1. 头部（三包第 11 行"规格状态"）与尾节（WP26/WP27 §13、WP30 §15）→ **Reviewed（限定静态范围，2026-09-26 闭合复审 PASS_SCOPED；管理性回填）**。范围按闭合报告 §4：WP26=已述六类获得/赠送/蛋/脚本交换入口、顺序、命名、容量、返回/失败与直接消费者交界；WP27=背包/PC 容器及存取、纯预检/部分执行、游标、登记/取消/图标/快捷收集及已述入口对照；WP30=已述曲线/换算边界、经验/EV 主规则、等级/经验辅助、学习/替换/重学、友好/亲密派生与直接写入交界。保留各文档具名前向（捕获/图鉴/事件、专门 UI、主动/持有效果、Shadow 完整生命周期、战斗触发时序、进化/寄养/孵化等）。
2. 矩阵六行：F07-06、F10-05（WP26）；F08-01、F08-02（WP27）；F09-01、F09-02（WP30）→ "Reviewed（对应子范围）＋前向 Inventoried"；**不整行笼统完成**；F06-07（WP21，已 Reviewed）不动。
3. **C03 记法维护**（随回填同步；不借机改已接受行为、不改变通过范围与算法）：
   - ① WP30 §12.2（:283–291）"同上"统一锚定"战斗经验·单参与"基准行（:282）：各行只覆写自己点名的 ID/语言/参与人数/开关/物品前提，不继承上一行语言差异；Shadow :295–296 承接"Shadow 提交"行（:294）前提（Shadow、心阶段2、当前 E/暂存 S），只改余量 10 或心阶段 4。
   - ② 新回填回应注明：上轮（recheck 轮）`revision-response.md`（:25）中 WP27-R01 源码名 `004_PokemonBag.rb` 为 `008_PokemonBag.rb` 笔误；旧回应保留历史原件、不改写。
   - ③ 三包头部/尾节"8 项关闭"（WP26 :11/:272、WP27 :11/:232、WP30 :11/:340）是**整批**计数：回填改写时放回历史语境（写"整批 8 项"或并入回填说明），避免被读作单包计数。
4. 记录：保存被审 v3 与回填后哈希/字节（**分开记录**）、管理性 diff（相对 `input-snapshot/`）；manifest 保留 v1/v2/v3 链；"变更后的新字节仍须记录为回填后版本，不能倒称其为本轮被审 v3"。
5. 回填不需再等短审，可接着执行三包（同会话）；参照先例：WP21 回填 `19a36297`、WP24 `32594094`、WP25 `46bd905d`（差异在 `review/wp21-wp25-closure-review-2026-09-26/revision-diffs/` 与 `review/wp21-wp25-recheck-2026-09-26/revision-diffs/`）。

### C. 新批次 WP31→WP28→WP29（串行、逐包自检固定、批末统一送审）

- **WP31 基础进化**（F09-03，建议 `specs/pokemon-rules/wp31-basic-evolution.md`；依赖 WP20/WP30/WP03/WP02）。要点：做有边界的条件族目录（输入/参数/优先遍历顺序/可行目标/失败）；区分条件判定、入口触发、阻止/取消、实际提交、展示收尾；取消前后变更与消耗归属；提交前后物种/形态、重算与 HP、招式/昵称/图鉴/来源、持有状态的实际改变（引用 WP18–WP21、WP30 主规则，不复制）；额外个体接收、队伍容量、球/物品前提、写入顺序的静态场景；WP32 跨域触发与 WP67-B 完整演出保留具名前向，但本包必需的提交不能全推给 UI 未来包。取证起点：`S/010_Data/001_Hardcoded data/007_Evolution.rb`、`S/014_Pokemon/001_Pokemon.rb`、`S/016_UI/001_Non-interactive UI/004_UI_Evolution.rb`、道具/成长调用者及物种文本数据。
- **WP28 主动道具与培养/教学**（F08-03/F08-04，建议 `specs/creature-rpg/wp28-item-use-and-training.md`；依赖 WP20/WP27/WP30/WP31）。要点：按上下文分流（背包/野外/个体/战斗）列资格/数量/目标/确认/效果/返回/关闭与消耗时机；登记使用与主要效果族覆盖目录、注册/复制/别名/未命中归属；治疗/复活/PP、EV 与培养、经验糖果、机器/教学、进化道具引用已审或批内主规格；区分 100 点培养阈值与 252/510 总约束、非蛋/蛋与 Shadow 前置、机器空槽/满槽路径；失败/取消是否消耗、部分成功副作用按真实调用链登记，不补事务/回滚保证；界面内实际写入/消耗必须读到。**引用 WP31 须注明"批内固定版本，尚未外审"＋实际哈希。** 取证起点：`S/013_Items/001_Item_Utilities.rb`、`002_Item_Effects.rb`、`003_Item_BattleEffects.rb` ＋登记基础、物品数据与背包/队伍/野外/战斗调用者。
- **WP29 买卖与 BP 商店**（F08-06，建议 `specs/creature-rpg/wp29-shops-and-exchanges.md`；依赖 WP24/WP27）。要点：金钱商店与 BP 入口分别列库存/命令可见性、价格来源/覆盖/取整、数量、禁售、取消/失败；交易前后钱/BP、物品、赠品、统计的写入顺序与守卫由真实调用链确定（不套用 WP27 某包装结论）；免费/零价/资源边界/容量边界/数量极值用具名前提与独立算术向量；追踪金钱/BP setter 钳制与交易层差异；不把资源域上限当所有入口规则。取证起点：`S/016_UI/020_UI_PokeMart.rb`、`021_UI_BattlePointShop.rb`、物品价格/标记、价格覆盖与事件包装、实际资源/背包写入者。
- **批末四项交界核对**：①WP31×WP18/19/20/21/25/26/30；②WP28×WP20/27/30/31；③WP29×WP24/27；④追踪一致性（范围/状态/前向/Feature 增量/批内固定与 manifest 一致；只读文本、独立算术、自检不得称为运行/外审确认）。发现上游矛盾：具名局部证据＋受影响范围＋最小修订，不静默改旧规则；批内引用与哈希级联同步。

### D. 记录与交付

- 在 `review/` 下按实际日期新建本批交付目录（如 `wp31-wp28-wp29-delivery-YYYY-MM-DD/`）：保存回填前后差异（相对闭合轮 `input-snapshot/`）、回填回应、交付摘要、完整哈希/字节、逐包自检与批末交界记录。
- 更新 WP26–WP30 交付摘要为 **v4**（加闭合回填注记；先例：wp18-wp20 摘要 v4 `5118e628`、wp21-wp25 摘要 v4 `8d8b7e5d`）。
- 更新矩阵（六行回填＋F09-03/F08-03/F08-04/F08-06 增量，均具名范围、保留前向 Inventoried）；manifest（§1 当前表、§2.1 对应关系、§3 替代关系、§4 新增轮次——从**第三十六轮**起，回填与新批次可分两轮或同轮分节，**被审 v3/回填后/新交付三类哈希分开记录**；补登闭合报告与提示；保留 v1/v2/v3 链）；TSV 主表延续、更新表题（v11 起）、不丢旧行。
- 全量自检（§6 脚本）：所有当前版本行哈希＋字节比对，应保持 **0 不一致**（本轮基线 179/83）。
- 三新包保持 **ReviewPending**，不得自批 Reviewed。

### E. 停止点

- **批末统一送审后停止**：不启动 WP22/WP23/WP32/WP33 或任何其它包（WP22 依赖 WP39/WP40、WP23 依赖 WP30/WP38/WP49 且状态未齐；后续批次授权由 reviewer 报告/提示给出，不能把本批停止点误写成永久禁止调查）；不创建并行 Agent；不向 reviewer 发消息；不提交/推送。

## 5. 未决与开放项（不得擅自关闭）

- **U01** 完整 demo 地图/公共事件/资源缺失 → 事件可达性、收费/奖励等一律待证。**U02** 当前 commit 与官方发布包差异未比对。**U03** 世代开关与 PBS 备份组合边界。**U04** 数据存在 vs 完整功能存在。**U05** 随机/时间/录像确定性。**U06** Shadow 数据与脚本启用条件。**U07** 取消/失败时跨域状态一致性。**U08** RMXP 命令兼容范围。**U09** 插件实际组合与外部服务。**U10** 战斗效果/AI 版本差异覆盖。
- 具体待查（散见规格未决节）：`battle_points_won` 写入来源（WP55/WP77）；缺失 NPC/道馆/名人堂事件的 8 个统计字段（U01）；寄养/电话转换的参考快照反例；WP46 全局效果映射验收；非调试写入者未定位项（`forced_form`、`cannot_store/release/trade`、徽章、功能标记、墙纸解锁、华丽大赛属性）；`RegionalStorage` 消费者未定位。
- 具名前向（WP26–WP30 保留）：捕获/图鉴/事件、专门 UI、主动/持有效果、Shadow 完整生命周期、战斗触发时序与参战反馈、进化/寄养/孵化等；"生物—队伍—储存"检查点待 WP26/WP38 加入后复核（不替代 WP78）。
- 阶段出口：WP78 一致性 → WP79 覆盖（`planning/coverage.md` 预留）→ WP80 sanitized（`audit/source-traceability.md` 预留）；限定通过不替代最终覆盖、sanitized 交付或完整运行验证。

## 6. 常用操作速查

- 哈希+字节：`shasum -a 256 <file>`；`stat -f "%z" <file>`。
- 回填差异（相对闭合快照）：`diff -u review/wp26-wp27-wp30-closure-review-2026-09-26/input-snapshot/<路径> <工作区同路径> > <新交付目录>/<名>.diff`（如 `wp26-backfill.diff`）。
- 全量自检脚本（`python3`，于工作区根运行；本会话末次：manifest 179 行、TSV 83 行、0 不一致；manifest 带"见原件"的行自动跳过，带括注的行已覆盖）：

```python
import re, subprocess, os

def shasum(p):
    r = subprocess.run(['shasum','-a','256',p],capture_output=True,text=True)
    return r.stdout.split()[0] if r.returncode==0 else None

mrows=[]
for line in open('planning/review-manifest-2026-09-19.md',encoding='utf-8'):
    m=re.match(r'^\|\s*`([^`]+)`[^|]*\|\s*`([0-9a-f]{8})`[^|]*\|\s*`([0-9a-f]{64})`[^|]*\|\s*([\d,]+)\s*\|',line)
    if m: mrows.append((m.group(1),m.group(3),int(m.group(4).replace(',',''))))
bad=0
for path,h,b in mrows:
    h2=shasum(path)
    if h2 is None or not os.path.exists(path): bad+=1; print('ERR',path); continue
    b2=os.path.getsize(path)
    if h2!=h or b2!=b: bad+=1; print('MISMATCH',path,h2,b2,'expected',h,b)
print('manifest rows:',len(mrows),'bad:',bad)

trows=[]
for line in open('review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv',encoding='utf-8'):
    m=re.match(r'^([0-9a-f]{64})\t(\d+)\t(.+)$',line.rstrip('\n'))
    if m: trows.append((m.group(3),m.group(1),int(m.group(2))))
bad=0
for path,h,b in trows:
    h2=shasum(path)
    if h2 is None or not os.path.exists(path): bad+=1; print('ERR',path); continue
    b2=os.path.getsize(path)
    if h2!=h or b2!=b: bad+=1; print('MISMATCH',path,h2,b2,'expected',h,b)
print('tsv rows:',len(trows),'bad:',bad)
```

- 不改写旧 review；新增文件放对应轮次/新交付目录；manifest/TSV 自身不自哈希，最终值实测写入交付消息。

## 7. 新会话启动提示词（可直接复制粘贴）

```text
工作区：/Users/dingshinn/Desktop/pokemon-framework-reference/。你是本项目的提取模型，接续 2026-09-26 会话（WP26–WP30 闭合复审已回、待回填与下一批）。先做三件事，全部以文件原文为准：

1. 完整读根 AGENTS.md 与 handoff-2026-09-26-wp26-30-closure.md（交接：当前进度、待办与纪律）。
2. 完整读 review/wp26-wp27-wp30-closure-review-2026-09-26/report.md（闭合复审：WP26/WP27/WP30 均 PASS_SCOPED、最后五项关闭、C03 维护随回填）与同目录 next-batch-prompt.md（回填＋下一批执行提示，权威执行细节）、input-manifest.json、current-hashes.tsv 及各 checks json；再读 planning/review-manifest-2026-09-19.md §1/§2/§4、planning/extraction-plan.md §1/§2.1（含 WP28/29/31 行）、planning/feature-matrix.md 相关行（F07-06、F10-05、F08-01、F08-02、F09-01、F09-02、F09-03、F08-03/F08-04、F08-06），以及三包当前规格（specs/creature-rpg/wp26-acquisition-gifts-and-script-trade.md、wp27-bag-and-item-storage.md、wp30-growth-learning-and-friendship.md）与上两轮回应 review/wp26-wp27-wp30-review-2026-09-26/revision-response.md、review/wp26-wp27-wp30-recheck-2026-09-26/revision-response.md（知已关闭范围）。
3. 复算六项固定对象并与闭合报告 §1 对照（基准亦可对照 review/wp26-wp27-wp30-closure-review-2026-09-26/input-snapshot/）——一律实测 shasum -a 256 与 stat -f "%z"；不同则先登记差异及是否超出授权，再处理；绝不凭前缀推补哈希、不凭记忆填字节数：
   - WP26 afc7214aa636369021e2bb1d71daa536e78170c850d2a09e58a075367e13bbe9（35,387）
   - WP27 969cb37c0d38cc27ad97c178f821debdef394a6e3fdf6492847a799faf914c67（27,166）
   - WP30 41e71624796647479e6428a13f04838010bfb97e44cbb2316927cdc70a669117（36,040）
   - 矩阵 6b49c40b3508f8863500a8e36ca8ddf9960e3f411a42ed9f508007e9ceccdf0a（41,342）
   - manifest 88af4e6d88306f6bcb913e66bfc0b7146dd5c75d77f0c9c9b836d65570ec4156（112,415）
   - 交付摘要 v3 df4926ae7007de65c6b4b4bcaa85b35956b9e065a6531710a5ec43f7aee11109（11,682）

随后直接执行以下工作，不要询问是否继续（用户已授权）：

A. 回填 WP26/WP27/WP30 → Reviewed（限定静态范围，2026-09-26 闭合复审 PASS_SCOPED；范围按闭合报告 §4）：改三包头部（第 11 行规格状态）与 WP26/WP27 §13、WP30 §15；矩阵六行 F07-06/F10-05、F08-01/F08-02、F09-01/F09-02 → "Reviewed 对应子范围＋前向 Inventoried"，不整行笼统完成；随回填同步 C03 三项：①WP30 §12.2"同上"锚定"战斗经验·单参与"基准行、Shadow 两行承接"Shadow 提交"前提（只改余量10/心阶段4）；②新回填回应注明上轮 `004_PokemonBag.rb` 为 `008_PokemonBag.rb` 笔误（旧回应保留）；③头部"整批 8 项关闭"移入历史语境。被审 v3 哈希保留历史、回填后哈希不伪称为复审对象；不借回填改已接受行为。

B. 新批次 WP31→WP28→WP29（串行、逐包自检固定、批末统一送审；细节按 next-batch-prompt §3–§8）：WP31 基础进化（F09-03，specs/pokemon-rules/wp31-basic-evolution.md）；WP28 主动道具与培养/教学（F08-03/F08-04，specs/creature-rpg/wp28-item-use-and-training.md；引用 WP31 须注明"批内固定版本，尚未外审"＋哈希）；WP29 买卖/BP 商店（F08-06，specs/creature-rpg/wp29-shops-and-exchanges.md；独立核对真实调用链，不套用 WP27 包装结论）。批末四项交界核对（WP31×WP18/19/20/21/25/26/30；WP28×WP20/27/30/31；WP29×WP24/27；追踪一致性）。三新包保持 ReviewPending、不自批 Reviewed。

C. 记录与交付：在 review/ 下按实际日期新建本批交付目录（如 wp31-wp28-wp29-delivery-YYYY-MM-DD/），保存回填前后差异（相对闭合轮 input-snapshot/）、回应、交付摘要、完整哈希/字节、逐包自检与交界记录；更新矩阵、manifest（§1/§2.1/§3/§4 新增轮次从第三十六轮起；补登闭合报告与提示；被审/回填后/新交付三类哈希分开记录；保留 v1/v2/v3 链）、WP26–WP30 交付摘要 v4 与 TSV（主表沿用 review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv，更新表题、不丢旧行）；对全部当前版本行做哈希＋字节自检（脚本见交接 §6，本轮基线 179/83 行 0 不一致）。所有值为实测。

D. 停止：批末统一送审后停止；不启动 WP22/WP23/WP32/WP33 或其他新包；不创建并行 Agent；不提交/推送。

全程硬约束（AGENTS.md 与项目纪律）：reference/ 只读；不运行游戏/Ruby/编译器/参考脚本/表达式/插件/网络；只交付规格与分析（不设计未来框架结构/API）；不改写 review/ 下原件（新增用新文件）；状态附范围、不自批 Reviewed。
```
