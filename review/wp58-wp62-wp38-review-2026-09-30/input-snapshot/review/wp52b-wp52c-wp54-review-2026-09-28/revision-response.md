# 提取侧修订回应：WP52-B-R01、WP54-N01、BATCH-C01与C／WP54限定管理回填

2026-09-28。角色：提取方有限修订，非独立复审。依据本目录 [report.md](report.md)（§3必修、§4.1／4.2、§5回填授权）与 [revision-prompt.md](revision-prompt.md)。差异基准统一为本目录 `input-snapshot/`；全部改动均为静态文本与登记维护，未运行Ruby、游戏、事件、生成器或网络，`reference/pokemon-essentials/`（commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，HEAD正确、普通Git状态为空）未改。

## 0. 固定输入预检

- 报告 §1 与 revision-prompt §1 所列 15 项关键对象（B／C／WP54 主附表、WP46、WP52-A 主附表、feature-matrix、manifest、本批旧交付摘要／self／boundary、主TSV v30）逐一复测：完整 SHA-256 与字节数全部与本轮快照逐字节一致；`reference` HEAD 与普通 Git 状态如上。
- 本轮 reviewer 顶层 16 件原件（含 `check_constants.py`、`check_text_and_identity.py` 两份检查脚本）与 `input-snapshot/`、更早 613／589／548／521 快照均未改动；本回应与 `revision-diffs/` 为本目录新增材料。

## 1. WP52-B-R01：区分候选跳过与直接处理器失败（已修订，待有限复审）

**回源核实**（路径相对 `reference/pokemon-essentials/Data/Scripts/`，均本轮亲自复读）：

- `011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:188–194`：基数处理器在 PP 恰为 0 时先查询 `totalpp`，其后才可能给出 0 或进入剩余 PP 索引。
- `011_Battle/005_AI/011_AIMove.rb:4–15,81–86`：到达该处理器的包装内部招式是战斗招式；该处理器仅中等技能起经基数预测调用。
- `011_Battle/003_Move/001_Battle_Move.rb:1–20,34–82`：战斗招式提供 `total_pp`，没有 `totalpp`。全 Scripts 名称检索仅 `014_Pokemon/004_Pokemon_Move.rb:44–48` 在持久个体招式上定义 `totalpp` 别名；未发现别的别名、`method_missing`／`respond_to_missing?` 兜底。
- `011_Battle/005_AI/005_AI_ChooseMove.rb:23–34` 与 `011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb:5–17`：普通候选遍历用正确查询提前排除有限总PP且当前PP0的槽；不能把处理器内失败扩大为所有耗尽槽。

**结论**：原稿把方法名的意图当成可用实现。固定快照、正常战斗招式类型且确实到达该处理器时，PP0 对缺失查询先失败，尚未比较总PP、也未输出基数（总PP正与总PP0皆然）；PP非0时该查询被短路，正PP与PP−1数值不受影响。**未**补兼容getter、**未**把持久招式别名套给战斗招式、**未**改 `reference`、**未**运行Ruby。

**实际修改位置**：

- B主稿 §2 `PowerHigherWithLessPP` 行：改为分入口记载（普通候选跳过／到达处理器PP0先失败／PP非0短路）。
- B主稿 §8：旧 `B04` 行替换为 `B04`／`B04b`／`B04c` 三行对照（60→62场景）。
- B主稿 §7 依赖与尾部记录；交付侧 `self-checks.json` 复制的该向量同步为三条；摘要说明同步。**B附表（`wp52-b-effect-coverage.md`，`d2ccf48f…`，57,193字节）登记与绑定正确，未改为行为修改集合**；boundary 中另有一个同名 B04 组（WP54交界编号）未被误替换。

**静态验收对照**：

| 输入／入口 | 期望 |
| --- | --- |
| 普通候选遍历，有限总PP、当前PP0，其余条件正常 | 候选资格阶段跳过，不取得此处理器的P0 |
| 中等技能路径确实到达该处理器，当前PP0、总PP正 | 缺失`totalpp`查询先失败，无正常基数 |
| 同入口，当前PP0、总PP0 | 同样先失败，不能承诺倒数索引得到40 |
| 到达处理器，当前PP1／2，其他输入正常 | 200／80保留 |
| 到达处理器，当前PP−1 | 非零短路，原倒数第二项50保留；不据此声称普通候选必能选它 |

**身份与传播**：被审v1 `b41c2773e3b00f8654767e597dfad20b34587fcb7d8d73bab11dbf784e13569d`（42,914字节）保留为历史；修订后当前完整身份 `8036a674606d1455cd77f35b335e90a34b694afde08e8add950ac89931a12d00`（44,557字节），已级联至C主稿对B引用与self/摘要。**WP52-B仍为 ReviewPending（仅R01待有限复审），不得自批Reviewed**。

## 2. WP54-N01：旧WP46定点同步（独立证据已确认；实际同步见下）

**回源核实**：

- `011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb:70–89,112–125`：原OHKO目标检查只有等级／坚硬；冰子类原定义先拒T冰，命中阈值−10是另一个入口；`OHKOIce` 没有后续其它重定义（全 Scripts 检索确认）。
- `011_Battle/007_Other battle code/006_Battle_Clauses.rb:192–221`：条款文件按目录顺序在 `003_Move` 之后加载；先在父类保存原目标检查，再对冰子类检查“是否已有同名保存入口”——查询包含继承方法，因此冰子类不另存自身拒冰门；新目标检查在条款假时调用继承的父类原门。
- `011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:63–110`：AI 的冰目标失败预测独立保留。
- `011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb:303–312`：实际逐目标入口消费该失败结果；通过此门不等于必中／必击倒／整招成功。

**实际修改位置**：

- WP46 §4 `OHKOIce` 行：分“原定义先拒冰”与“条款加载后、无后续覆盖”两个入口；条款假时不再仅因T冰拒绝、条款真仍拒；U非冰−10未改；目标门通过不等于命中／击倒／整招成功。§10 补记条款文件定点回读；尾部记录本次授权同步与新身份留史。
- WP54 主稿 §6 N01 章由“待独立判定”改为“独立证据已确认，WP46已按授权同步”；`ohkoclause` 行与 Q41 语境同步；附表尾注同步。
- 矩阵 F13-03、boundary／self 的 N01 状态同步为“已确认＋已同步”。**AI拒冰门、A专用命中估计与WP43命中公式均保留未动**。

**静态对照**：同级50、T冰、无坚硬、其它外层资格过——原定义拒；条款加载后条款假不因冰拒（走等级／坚硬门），条款真仍拒；命中入口与数据结构（U非冰−10）未变。仅源码定义／继承查找与加载顺序的静态推导，无运行验证。

**身份与传播**：被审/此前身份 `aa9a7f1e206275ce934a1bc3cf860813bafac852795a5d939316c6f5d9e8bf4c`（47,646字节）保留为历史；同步后当前身份 `0f7c9b4b21ec45c2084876de08218812aab7a615b6fb2d53ff1c0de603d3b662`（48,872字节）。WP46 其它限定通过范围与 WP43 不改；新字节未经外审。

## 3. BATCH-C01：A阶段前向定位改为明确历史（非阻塞维护）

**实际修改位置**：WP52-A 主稿 §1（“它们未启动”改为A阶段历史定位，并记当前B270／C167、B待R01复审、C限定通过）；A附表 §1（247／190标注A阶段历史定位）、§5 表头与48处行内状态词（“未启动”→“A阶段定位”）、尾部记录。**未改A任何行为／场景，不重审A**。

**身份与传播**：A主稿 `5cdc3edf…`（48,733字节）→ `9c74d50cd8d886707c9d6addd1b6f5be162beec6333daca924d7b4d7ddc3df70`（49,622字节）；A附表 `fa760fac…`（59,366字节）→ `7bce736d31418d5e02e441956806c218cf9e8f97e9f24051c54398fc0239f80f`（60,674字节）；两者旧身份留史，引用已级联。

## 4. C／WP54限定管理回填（Reviewed，限定静态范围）

按报告 §5 回填两主稿、两附表头尾：

- **WP52-C**：A～F 物品 V/E 与条件评级、转移／调用／复制、换人／拘束、时机／PP限制、浮空／变身／侧位置及具名数据；167出现／165有效直接键、215基础评级、57条件身份保留。C对B引用改为“R01修订稿，尚待有限复审”并使用B新完整哈希；**通过不使WP52-B或整个AI通过**。
- **WP54**：A～F 四资格层、规则组合／复制／建议、等级／经验／HP调整与按索引还原、默认杯赛／模式、界面／单场接点、14条款及已述例外；56定义身份、10活动工厂、5直接样本、3模式、14条款键保留。N01语境同步见§2。
- 矩阵：F12-08 保留A已Reviewed、新增C具名Reviewed、B为ReviewPending（仅R01）、全局组合／设施／运行Inventoried；F13-03 仅WP54批准范围Reviewed，设施会话／Demo／运行前向保留。
- **身份**：C主稿 `542e7b01…`（39,343字节）→ `290bee81e83140473c30aa9fd74d8debad25d80e1de4aae440b0b20f5371934f`（40,332字节）；C附表 `9e8d3030…`（37,701字节）→ `f83205eebd3889354a4fb8afe9847c9e489d0eec9d84b876e06b6da3c0f09088`（38,390字节）；WP54主稿 `3ef7ae5a…`（32,322字节）→ `2a1518c3351ed9fa3dfaf839010dcc0f4c56df862353c39a227151aa83d06dfb`（33,809字节）；WP54附表 `b45c976e…`（11,746字节）→ `0ec502366b743770f95d7971cf3f087a153694bc6ff4395b8852642fd422a18d`（12,381字节）。被审v1身份全部留史，新字节不冒充被审对象。

## 5. 必要身份级联（只改引用与记录，不改行为）

按实际无环顺序（依赖在前）：WP46 → WP47-A → WP47-B → WP50 → WP51 → A附表 → A主稿 → B主稿 → C附表 → C主稿 → WP54附表 → WP54主稿。级联只更新各文件依赖节的完整哈希与字节、标注维护性质并追加记录段落：

| 文件 | 旧身份 | 新完整身份 | 字节 |
| --- | --- | --- | ---: |
| WP52-B 主稿（R01） | `b41c2773…` | `8036a674606d1455cd77f35b335e90a34b694afde08e8add950ac89931a12d00` | 44,557 |
| WP46（N01同步） | `aa9a7f1e…` | `0f7c9b4b21ec45c2084876de08218812aab7a615b6fb2d53ff1c0de603d3b662` | 48,872 |
| WP47-A 主稿 | `1b1dea7c…` | `e49349438e19be9bbd09bcc192e69f4d839a8e715c46cf09291f0f8c5c390f96` | 34,014 |
| WP47-B 主稿 | `0287e0b2…` | `007699019544203b9b5f4c42f18db8eb91711d2d96f6fa8afdf047d44b16e778` | 39,000 |
| WP50 主稿 | `6c97afeb…` | `f0b6b1472ed1eceb7679c0bf50d836076a0a52a593ce011132ee90c1e01e6f72` | 32,490 |
| WP51 主稿 | `8deea695…` | `2b0847b5d52d9907804c62703871a9a6557a6b9940a8fd0a93c702329808a025` | 27,645 |
| WP52-A 主稿 | `5cdc3edf…` | `9c74d50cd8d886707c9d6addd1b6f5be162beec6333daca924d7b4d7ddc3df70` | 49,622 |
| WP52-A 附表 | `fa760fac…` | `7bce736d31418d5e02e441956806c218cf9e8f97e9f24051c54398fc0239f80f` | 60,674 |
| WP52-C 主稿 | `542e7b01…` | `290bee81e83140473c30aa9fd74d8debad25d80e1de4aae440b0b20f5371934f` | 40,332 |
| WP52-C 附表 | `9e8d3030…` | `f83205eebd3889354a4fb8afe9847c9e489d0eec9d84b876e06b6da3c0f09088` | 38,390 |
| WP54 主稿 | `3ef7ae5a…` | `2a1518c3351ed9fa3dfaf839010dcc0f4c56df862353c39a227151aa83d06dfb` | 33,809 |
| WP54 附表 | `b45c976e…` | `0ec502366b743770f95d7971cf3f087a153694bc6ff4395b8852642fd422a18d` | 12,381 |
| feature-matrix | `52956942…` | `abacb77523d5a08c13ebbfed5954c3dbc69e03c42119ff69ebb0540d806900aa` | 50,610 |

- B附表未改（`d2ccf48f…`，57,193字节）；WP47-A／B、WP50附表未动。所有旧被审身份与其替代链保留于manifest §3，未做全局旧哈希替换；reviewer 快照、历史回应与旧差异均未动。
- 交付侧：`delivery-summary.md→v2`、`self-checks.json→v2`、`boundary-checks.json→v2`（旧身份留 revision_history；旧错误断言只作明确历史）。

## 6. 材料与差异

- 本目录新增本回应，与 `revision-diffs/` 共16份差异，全部相对本目录 `input-snapshot/`：wp46、wp47-a、wp47-b、wp50、wp51、wp52-a（主／附表）、wp52-b、wp52-c（主／附表）、wp54（主／附表）、feature-matrix、delivery-summary、self-checks、boundary-checks。未改文件不造空diff。
- 交付目录 `review/wp52b-wp52c-wp54-delivery-2026-09-28/`：摘要与 self／boundary 升 v2（追加 revision_history；B04旧期望、N01待判定只作历史）；旧 `backfill-response.md` 与9份 `backfill-diffs/` 保持原件。
- 登记：主TSV v30→v31、manifest 第五十五→第五十六轮；本轮 reviewer 16件全部补登。manifest不自哈希、TSV不收自身；终值由交付消息实测报告。

## 7. 保留边界与停止

- 未运行游戏／Ruby／参考表达式／解释器／事件脚本／生成器／编译器／转换器／插件／网络；未操作地图、存档、输入；未实现新框架、未创建Agent／任务、未发reviewer消息、未提交推送。
- **WP52-B仍未通过**（R01待有限复审）；C／WP54为限定静态范围管理回填；不得写“WP39–WP54连续完成”。限定通过集合：WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP51（WP47=A/B）、WP52-A／C、WP54、WP59–WP60。
- 设施完整会话、Demo／宿主／媒体／插件／U01–U10、运行与 WP78→WP79→WP80 出口继续保留。本轮修订与回填仅送有限短复审，不重做首审、不启动 WP55 及其它提取包。
