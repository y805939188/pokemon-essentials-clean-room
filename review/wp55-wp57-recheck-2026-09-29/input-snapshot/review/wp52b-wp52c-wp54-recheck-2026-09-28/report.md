# WP52-B／C／WP54 有限复审与闭合报告

2026-09-28；独立 reviewer。固定 reference commit：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

**结论：PASS_SCOPED。WP52-B-R01、WP54-N01 实际同步及 BATCH-C01 均 CLOSED；C／WP54 限定回填和直接引用传播接受。可以先回填 WP52-B，再串行开展 WP55→WP56→WP57，批末统一外审。**

另有 **BATCH-C02 非阻塞维护**：提取侧 self-checks 的五个旧身份和 Q41 旧状态尾句需在回填时同步。它不影响本轮实际固定的规格或行为结论，不新增一轮行为复审门槛。本报告不是新三包已通过，也不是运行验证。

## 1. 本轮实际固定版本

| 对象 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| WP52-B 主稿 v2 | `8036a674606d1455cd77f35b335e90a34b694afde08e8add950ac89931a12d00` | 44,557 |
| WP52-B 附表 v1，未改 | `d2ccf48fbd64cc786bcd7bf060631a007523ea48afff6d38a00391c7ac8b47fe` | 57,193 |
| WP52-C 主稿，回填后 | `290bee81e83140473c30aa9fd74d8debad25d80e1de4aae440b0b20f5371934f` | 40,332 |
| WP52-C 附表，回填后 | `f83205eebd3889354a4fb8afe9847c9e489d0eec9d84b876e06b6da3c0f09088` | 38,390 |
| WP54 主稿，回填／同步后 | `2a1518c3351ed9fa3dfaf839010dcc0f4c56df862353c39a227151aa83d06dfb` | 33,809 |
| WP54 附表，回填后 | `0ec502366b743770f95d7971cf3f087a153694bc6ff4395b8852642fd422a18d` | 12,381 |
| WP46 主稿，N01 同步后 | `0f7c9b4b21ec45c2084876de08218812aab7a615b6fb2d53ff1c0de603d3b662` | 48,872 |
| WP52-A 主稿，维护后 | `9c74d50cd8d886707c9d6addd1b6f5be162beec6333daca924d7b4d7ddc3df70` | 49,622 |
| WP52-A 附表，维护后 | `7bce736d31418d5e02e441956806c218cf9e8f97e9f24051c54398fc0239f80f` | 60,674 |
| feature-matrix | `abacb77523d5a08c13ebbfed5954c3dbc69e03c42119ff69ebb0540d806900aa` | 50,610 |
| manifest | `1ff10a66304f03ae6433dab523540e7b16fef382d166c2bd030e56db49cb4bcc` | 363,103 |
| 本批交付摘要 v2 | `c173bc0062de20ad14be16efd17cb7ddae7aa944532e85161b35453f1b45d4c9` | 7,973 |
| 主 TSV v31 | `e91e849cbd56f88fcb0792521e17eb9382669fa5911a9a2066e511df9e37f64f` | 79,741 |
| 提取侧 revision-response | `0b179892f81a02bd592885de20de6cf96882a7e736ba0dd6e63d28a081b5e4e1` | 12,855 |

全部 677 项固定输入的路径、完整哈希及字节见 [input-manifest.json](input-manifest.json)、[current-hashes.tsv](current-hashes.tsv)；逐字节副本在 [input-snapshot/](input-snapshot/)。相对上轮 644 项输入，18 个原有文件变化，其中 16 份交付 diff 覆盖规格／矩阵／摘要／self／boundary，另两项为 manifest 和主 TSV。[changes-from-v1.diff](changes-from-v1.diff) 保留完整机械差异。

本轮只审上轮指定 R01、N01、C01、C／54 回填与直接传播；首审接受的 B 其余合同以及 C、WP54 的具名通过范围继承，不重新全量首审。

## 2. 原编号闭合结果

### WP52-B-R01 — CLOSED

本轮新回读以下来源，路径相对 `reference/pokemon-essentials/Data/Scripts/`：

- `011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:188–194`。
- `011_Battle/005_AI/011_AIMove.rb:4–15,81–86`。
- `011_Battle/003_Move/001_Battle_Move.rb:1–20,34–82`；`014_Pokemon/004_Pokemon_Move.rb:44–48`。
- `011_Battle/005_AI/005_AI_ChooseMove.rb:23–34`；`011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb:5–17`。

全 Scripts 名称检索仍只在持久个体招式上找到 `totalpp` 别名，没有战斗招式的别名／method_missing 兜底。本轮核对的是对象类型、名称与短路／调用顺序，没有执行 Ruby。

[B 主稿第35行](../../specs/combat/wp52-b-field-damage-healing-and-target-evaluation.md:35) 已分别说明：普通有限总PP、当前PP0槽在候选资格阶段跳过；中等技能路径确实到达处理器的PP0输入，无论总PP正或0，均先触及缺失查询，没有正常基数结果；PP非0短路这一查询。第240行的修订记录及 [B04／B04b／B04c，第251行起](../../specs/combat/wp52-b-field-damage-healing-and-target-evaluation.md:251) 与此一致。

| 有限静态验收 | 本轮结果 |
| --- | --- |
| 普通候选、有限总PP、当前PP0 | 提前跳过，不称取得P0 |
| 直接到达处理器、当前PP0、总PP正 | 缺失查询先失败，无基数 |
| 直接到达处理器、当前PP0、总PP0 | 同样先失败，不承诺40 |
| 到达处理器、当前PP1／2 | 200／80保留 |
| 到达处理器、当前PP−1 | 非零短路、50保留；没有扩大普通候选可选资格 |

B 从60增至62条场景，仅原B04替换并新增两个子编号，其余59条原样；self的B62条输入／期望与正文逐行一致。B附表字节、登记和绑定完全未改。未改真实PP规则或重新打开WP20／40／51。

### WP54-N01 — CLOSED（证据确认＋实际同步）

本轮回读 `011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb:70–89,112–125`、`007_Other battle code/006_Battle_Clauses.rb:192–221`、AI MoveAttributes `:63–110`、`002_Battler/009_Battler_UseMoveSuccessChecks.rb:303–312`。全 Scripts 的 OHKOIce 定义检索仅原定义与此条款重开；结论仍限原定义后加载该条款、无后续覆盖的静态条件。

[WP46第97行](../../specs/pokemon-rules/wp46-damage-multihit-and-healing.md:97) 已区分原定义拒冰与条款加载后的目标入口；第325／333行补来源和同步记录。WP54第120、134–140、210行及附表、矩阵、boundary的当前状态对应更新。

同级50、冰系目标、无坚硬、其它资格过：原定义拒冰；条款加载后条款假走已保存父类等级／坚硬门，不仅因冰拒；条款真仍拒。U非冰命中−10未改，目标门通过不等于必中／击倒。B第28行的独立AI拒冰合同保留，WP43字节未改。没有扩展成WP46整包重审。self中一条旧状态注记另列C02，不影响这项已完成的正文同步。

### BATCH-C01 — CLOSED

A主稿第15行、附表第7–9行与前向表均明确旧B247／C190属于A阶段历史定位，当前B270／C167的责任转归有说明。48行状态词改为“A阶段定位”；归一化这些状态词后，身份列表逐字一致。A的行为／场景未改，不重新审A。

## 3. 回填、传播和独立校验

C／WP54两主稿、两附表的头尾回填范围与上轮授权一致。C仍仅自身A～F通过，明确B修订稿当时待复审；WP54保留设施会话／租借／回放／运行边界。矩阵F12-08保留A/C的Reviewed和B的ReviewPending，F13-03仅回填WP54子范围。

WP47-A→WP47-B→WP50→WP51的变化只有必要引用与维护记录；随后A／B／C／WP54的当前身份级联匹配。本轮没有借回填修改这些包的已接受行为。C和WP54附表的全部表格数据未变；B附表逐字节未变。C55条场景全部未变，WP54仅Q41的同步状态尾句改变，其余41条未变。

| 独立检查 | 结果与口径 |
| --- | --- |
| 当前manifest／TSV | 675／579条完整哈希、字节、短标签匹配；无缺失／重复；原642／546路径顺序保留 |
| 本轮新增登记 | 两表新增集合相同，共33项：reviewer16＋回应1＋diff16 |
| 修订diff | 16／16从各自上轮快照在内存逐块重建到当前字节；未应用到工作区 |
| 历史保护 | 644、613、589、548、521五轮快照未变；各轮final-checks所列15、11、13、12、11项artifacts均匹配；本轮实际固定上轮final-checks本身 |
| 规格当前身份引用 | 触改规格100条依赖／附表绑定匹配；boundary35条绑定匹配 |
| 文本完整性 | 当前specs＋矩阵＋本次回应／摘要373条相对链接存在；171份登记JSON可解析 |
| reference | 上轮51个相关文件与本轮磁盘及固定commit blob均匹配；本轮新读9个路径，余继承首审；HEAD正确，普通Git状态为空 |
| self内部记录 | B62条向量匹配；五个旧artifact身份、Q41旧状态尾句需C02维护，不能宣称所有内部记录均零差异 |

详见 [identity-checks.json](identity-checks.json)、[diff-checks.json](diff-checks.json)、[propagation-checks.json](propagation-checks.json)、[coverage-checks.json](coverage-checks.json)、[source-checks.json](source-checks.json)、[static-checks.json](static-checks.json)。本轮没有重跑首审31项常数；这批数值与接受范围未变，本轮核心是入口／失败阶段和状态同步。

## 4. BATCH-C02：非阻塞的自检记录维护

对象：`review/wp52b-wp52c-wp54-delivery-2026-09-28/self-checks.json`，完整哈希 `7f77e8c250ea6999daa149bf006c79d75ca7e794cc5f8756e9e9599f9e027602`，1,068,195字节。

- 第1391行起的 `artifacts` 六项表，除未改B附表外，另外五项仍指向首稿身份；第33817行却称该表为当前身份。对应五项为B主稿、C主稿／附表、WP54主稿／附表。`packages`当前身份正确，manifest／TSV与本文§1也正确，所以不存在本轮被审字节不明的问题。
- 第1377行起的当前WP54向量Q41仍保留“旧摘要影响单列待外审，不修改旧规则”尾句，未跟随WP54正文第210行。目标检查的行为期望未变，落后的是同步状态。

最小维护：回填结束后从磁盘重固定`artifacts`六项当前身份，使之与`packages`及清单一致；Q41当前记录与正文同步。旧身份／旧状态保留在明确历史或本轮快照，不覆盖旧reviewer材料。[embedded-record-checks.json](embedded-record-checks.json)逐项列出差异。

**C02随下面的管理回填一起完成，不要求先停下来再送一次行为复审，不阻止本轮PASS_SCOPED与下一批。** 不为记录维护重新打开R01／N01／C01或扩审C／WP54。

## 5. WP52-B回填授权与下一批

允许提取方先将B主稿／附表头尾及矩阵F12-08的B子范围回填 **Reviewed（限定静态范围，2026-09-28有限复审PASS_SCOPED；管理性回填）**。具名范围是首审接受的A～F具体基数、多击／跨回合、恢复／自损、天气／地形／危害／保护／多目标合同及270出现／268有效键，连同本轮闭合的PP0分入口失败边界。

本报告实际被审B主稿为§1的 `8036a674…`／44,557字节，附表为 `d2ccf48f…`／57,193字节。保留完整身份与差异，回填后新字节不能冒称本轮被审版本。A、C及活动摘要中B“待R01复审”的当前引用按本报告维护；历史记录留史。C／WP54本轮回填已经接受，毋须重复改变它们的行为。C02一并维护并级联真实哈希。

回填后限定通过集合可记为：**WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP52（WP47=A/B，WP52=A/B/C）、WP54、WP59–WP60**。WP22／23／32／37／38／53等仍未完成，不能称连续到WP60。

下一批按 `planning/extraction-plan.md:131–133`：

| 顺序 | 工作包 | 计划完成依赖 | 批内执行约束 |
| --- | --- | --- | --- |
| 1 | WP55 设施基础会话，F13-04子范围 | WP54、WP42、WP50 | 已有依赖限定范围可用；先自检并固定会话产物 |
| 2 | WP56 Palace／Arena变体，F13-04子范围 | WP55、WP51、WP44 | 引用WP55批内固定稿并注明尚未外审 |
| 3 | WP57 Factory租借／换队，F13-05 | WP55、WP25、WP54 | 引用批内固定WP55；逐包自检，批末统一审三包 |

执行文本见 [next-batch-prompt.md](next-batch-prompt.md)。只执行这三包，不自动扩到WP58回放或WP76生成器。新增规格均保持ReviewPending（各自具名范围），本报告只批准回填和提取顺序，不预批内容。若缺输入，具名保留，不以缺Demo为由跳过可静态闭合的会话／取消／还原规则。

## 6. 证据边界与本会话停止点

本轮新证据是九处相关源码回读、实际修订差异和输入核对；其余通过范围继承上一报告。提取方回应是待审声明，未被当成独立证据。R01、N01结论仍为固定快照的静态推导，没有Ruby、游戏或宿主运行验证。

Demo、宿主、媒体、插件、真实地图／存档／输入、U01–U10、完整设施／全局组合／动态等价及WP78→WP79→WP80继续保留。此会话仅在本新review目录写报告、检查、快照与提示词，未改规格／矩阵／manifest／reference，未执行回填或WP55–57，未创建任务／Agent、未发消息、未提交或推送。
