# WP42／WP48／WP49 v2 有限复审与闭合报告

日期：2026-09-27（Asia/Shanghai）。独立 reviewer；Reference/Audit 侧材料，不是提取侧自检或 WP80 sanitized 交付。

**结论：PASS_SCOPED。WP42-R01、WP48-R01、WP49-R01 及 BATCH-C01 两处维护全部 CLOSED；无剩余必修、无新增维护要求。可以先回填三包限定 Reviewed，再按 WP46 → WP47-A → WP47-B 推进下一批。** 配套 [管理性回填与下一批提示](next-batch-prompt.md)。本会话只写本审查目录，没有代做回填或启动提取。

本轮仅审三个原编号、C01及直接传播。首审 [report.md](../wp42-wp48-wp49-review-2026-09-27/report.md) §6–7 已支持范围继续继承；旧 WP44／45 回填、N01 CLOSED 和其它通过范围不重开。

## 1. 被审固定版本与完整性

| 对象 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `6644c77775b1e02481674079c847652dbbf2c566214d3969f1f333f741c22f7d` | 41,329 |
| `specs/pokemon-rules/wp48-ability-calculation-modifiers.md` | `87e39127e14eddd10f6e0d10e6d63999e0cb9ff70fa0e2505dc97a195f3b3bb8` | 35,021 |
| `specs/combat/wp49-ability-phase-triggers.md` | `7a4ecf931a65931cd8c6255d09b2697f83a5b538da907a016e5712efa32a67d7` | 52,573 |
| `planning/feature-matrix.md` | `6d9a28754bd2cfb3622a8a6dbf6b624600fd8c45aa34db570dc111f57c455a20` | 48,271 |
| `planning/review-manifest-2026-09-19.md` | `6dfa15eadfa3b40a125741b90192a80b17ae0925e993b7f95a62b8a476ec4631` | 279,090 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md` | `e41b85316b620dede8ce1b8c30f61cbbdabee155a069ae34bbce19c5258a1e58` | 8,520 |

补充固定：提取侧回应 `review/wp42-wp48-wp49-review-2026-09-27/revision-response.md`，SHA-256 `5d20434afff2e59ef9b1286272bdf95ef8aed62694ee4684bdddfd25dd6a40d2`，8,707字节。self／boundary／主TSV及全部登记输入均固定于 [input-manifest.json](input-manifest.json) 与 `input-snapshot/`，完整身份见 [current-hashes.tsv](current-hashes.tsv)。

实测 manifest **519 条**、TSV **423 条**，全值／字节／短标签匹配，无缺失或重复，TSV路径均有manifest登记；固定 **521项输入**。九个既有文件发生变化，详见 [changes-from-v1.diff](changes-from-v1.diff)，另新增的提取回应与七份差异已纳入固定输入。

七份修订diff在内存逐块校验后均精确重建当前目标；首审501项快照及其final-checks列出的11份reviewer原件未变，final-checks自身登记哈希亦匹配。相关14份文档 **141 条相对链接有效**；登记 **120份JSON可解析**。这些是身份与追踪证据，不单独构成行为通过。

## 2. 原编号闭合与本轮新证据

本节 S 表示 `reference/pokemon-essentials/Data/Scripts/`；源码仅作只读证据，没有执行或复制进规格。

### WP42-R01 — CLOSED

当前 WP42 `6644c77775b1e02481674079c847652dbbf2c566214d3969f1f333f741c22f7d`，§7.2 :183–249、E12/E13 :292–293、数据要求 :295–297。

普通18项与稀有11项的顺序逐项匹配；稀有第7／9／11位的DESTINYKNOT均保留。新增窗口表将9个普通权重与两个稀有权重明确对应整数区间，总和98＋1＋1＝100。过滤在取窗口前，保序且不去重，长度不足放弃。这里补的是默认行为数据，未扩张到物品效果全集。

回读 `S/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb:654–749`，涵盖保序过滤、两表、资格／等级窗口／累计抽取及采蜜直接回归；对 `PBS/items.txt` 只检索25个不同身份的章节标识，全部存在。未声称读取完整物品效果。

静态验收：默认身份全存在、非蛋、拾取能力、空持有物且首个10%门已过时，等级1第二抽98／99为HYPERPOTION／NUGGET；等级91为LEFTOVERS／DESTINYKNOT。四个输出能直接从规格推出。旧首抽9／10、过滤后不足、采蜜独立抽取及其它成长／终局合同保留。

### WP48-R01 — CLOSED

当前 WP48 `87e39127e14eddd10f6e0d10e6d63999e0cb9ff70fa0e2505dc97a195f3b3bb8`，§4.2 :64–66、C06 :207；self／boundary／摘要的当前断言一致更新。

回读 `S/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb:1123–1137` 与 `S/011_Battle/003_Move/003_Move_UsageCalculations.rb:104–124`，并对照未改动的 WP43 §4.2。通常整数入口下，两次1.1得到倍率1.21，分别取整后命中121、闪避100；最终整数商为 **80×121÷100＝96**。严格比较得到 **r95命中、r96／97失败**，已具名排除其它修正、亲密及提前必中。

独立复算使用常数有理数／整数商，没有运行参考计算器。旧96.8断言只保留在明确撤回的历史记录中；旧 `match=true` 不再作为当前正确性证据。未修改 WP43 的正确规则，也未重开148身份目录。

### WP49-R01 — CLOSED

当前 WP49 `7a4ecf931a65931cd8c6255d09b2697f83a5b538da907a016e5712efa32a67d7`，§5.1 :94–98、H03 :250；self／boundary／摘要同步。

回读 AbilityEffects :367–408，以及 `S/011_Battle/001_Battle/001_Battle.rb:448–480`、`S/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb:44–48`、`S/011_Battle/001_Battle/007_Battle_ActionRunning.rb:5–22`。额外人数门只在野生战的敌方拥有者分支使用当前同侧存活场上数；持有者计入，已倒下者、空位、后备不计；名义布局不能替代此值。人数门之后仍保留逃跑资格。

静态对照：固定双席布局、跨半标记、有效能力、无天空摔投、后续可逃，二活→人数门返回假；另一名倒下后仅拥有者存活→人数门不拒，决定3并返回真。玩家侧不新增这道人数门。EMERGENCYEXIT／WIMPOUT共用修订合同；WP41已审主规则未被改写。

### BATCH-C01 — CLOSED（非阻塞维护）

- WP49 E03 :261 现在用攻击0、其它四主阶级＋6的合法输入。预先可降五项，升攻击后排除攻击剩四项；固定再选防御，得到攻击＋2、防御＋5，其余＋6。回读 AbilityEffects :2436–2464 与 StatStages :1–34,123–178；不再把防御说成唯一可降者。
- WP49 :73、L02 :241 明确ICEFACE是入场回调且不要求真实换入标志为真。回读 AbilityEffects :264–266,2820–2848、AbilityAndItem :62–70、ChangeSelf :155–169。气体结束的默认假标志仍可使存活、非变身、有效冰雹下的EISCUE形态1请求形态0；IMPOSTER保留真标志门，通用形态提交守卫未被抹掉。

本轮没有需要再为措辞另开一轮的残留。

## 3. 直接回归与限定通过范围

[diff-checks.json](diff-checks.json)、[coverage-checks.json](coverage-checks.json)、[text-checks.json](text-checks.json)记录独立对照：

- 三稿原有79条未受影响场景逐字节不变；只新增WP42 E12/E13，修改WP48 C06及WP49 L02/H03/E03。当前31＋23＋31＝85条场景与提取侧self对应文本一致。
- 能力审计表263行未变；继承首审48族、239直接／24复制语句、267展开身份（WP48 148、WP49 119）的集合证据，不重做全目录首审。
- WP49对WP42／48的当前完整哈希匹配；其它已审规格不变。矩阵仅三个具名行的修订状态变化，无自批Reviewed。self中的旧错误断言留史与当前断言已分开。

据首审已支持范围与本轮闭合结果，批准：

| 包 | 本轮 PASS_SCOPED 范围 | 对应Feature子范围 |
| --- | --- | --- |
| WP42 | A～E已述成长触发／学招等待／场上同步、普通回合末27阶段与早退／替补、正常结果／终局／世界交接、默认世界拾取／采蜜，以及显式中止与异常边界 | F11-06；F11-07 |
| WP48 | A～E已述27族计算／资格／免疫／有效性，具体修正参数、直接消费者门与计算副作用；148展开身份的有界合同 | F12-06计算子范围 |
| WP49 | A～F已述21族阶段触发、直接生命周期／排序／失能／连锁／写入边界；119展开身份的有界合同 | F12-06阶段子范围 |

本结论不是完整战斗引擎、所有组合、未来招式／物品／形态域或运行验证通过。原前向引用保留。限定通过集合由此为 **WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP45、WP48–WP49、WP59–WP60**；不能写成连续WP01–WP49全部完成。

## 4. 授权的管理性回填与下一批

提取侧可按配套提示先实测本报告§1六件与本轮快照匹配，再将WP42／48／49头部和尾节回填 **Reviewed（限定静态范围，2026-09-27 v2有限复审PASS_SCOPED；管理性回填）**。只登记§3范围；WP49的上游身份与必要旧状态引用可同步。矩阵F11-06/07及F12-06按各自子范围Reviewed＋前向Inventoried，不作整行无条件完成。

保留v1／被审v2完整身份，回填后的新哈希不得冒充本轮被审对象。新增回填回应和相对本轮快照的差异，不覆盖旧审查原件；更新自有交付摘要、manifest当前表／历史链／轮次与主TSV，补登本轮reviewer材料。

随后按现有计划 :114–116 串行执行 **WP46 → WP47-A → WP47-B**，逐包自检与固定，批末统一送审并停止。三包完成依赖分别为43/44/45、40/43/44/45、41/44/45/27/20，所需限定范围均已通过；本轮又闭合了42/48/49，可作为时序与能力组合输入。WP47-A/B是既有两个可执行包，WP47简称不另计第四包。不进入WP50、AI或其它新包。

三新包及对应Feature仅ReviewPending；引用同批成果须说明批内固定、尚未外审。完整目录映射、失败／取消、逐击／递归／控制与物品交界的要求见 [next-batch-prompt.md](next-batch-prompt.md)。本报告仅允许按依赖推进，不预先批准新规格。

## 5. 证据分层与操作边界

[static-vectors.json](static-vectors.json)是本轮独立常数算术／有序文本对照和手工分支验收；[static-checks.json](static-checks.json)记录编号闭合。提取侧回应与self只作待核声明；旧首审证据负责继承范围，不能冒称本轮再次全文读取。

[source-checks.json](source-checks.json)记录35个源／数据文件与固定commit blob一致，其中10条为本轮实际读取或检索（包括一段仅作上下文的UseMove）；其余仅身份回归。下一批文件清单定位不算行为审查。reference HEAD 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，普通Git状态为空。

只在本目录新增报告、提示、检查和快照；未改规格、矩阵、manifest、计划、旧审查或reference。未运行游戏／参考Ruby或表达式／解释器或事件脚本／生成器／编译器／转换器／插件／真实网络，未操作地图、存档或输入；未创建任务或并行Agent、未发消息、未提交或推送。

Demo、宿主、媒体、插件、U01–U10及WP78→WP79→WP80出口继续保留。最终输入稳定性与产物身份见 [final-checks.json](final-checks.json)。
