# 有限补修提示：GR-013／GR-016（2026-10-01）

你是提取／修订方。本轮复审 **REQUEST_CHANGES：GR-014／015 CLOSED；GR-013／016 OPEN_PARTIAL**。四项原始问题的核心行为已获接受，只处理本提示两项剩余点；完成后再次送定点复审。不要进入新内容包或整体double review。

先读本目录 [report.md](report.md)、[findings.json](findings.json)、[scenario-id-checks.json](scenario-id-checks.json)、[registration-checks.json](registration-checks.json)与[route-checks.json](route-checks.json)，遵守仓库AGENTS.md和现有审查门禁。原始总审及reviewer文件、旧回应／diff／快照只读。

## 1. 当前基线与保护

仅需编辑的主稿当前身份如下，本目录 input-snapshot 已固定：

| 文件 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `f6e5d683fc18a5d3d7d28b255cc3bd5acafd98dba7fae35fc09b755ce0ab72fe` | 44,526 |
| `specs/pokemon-rules/wp19-attributes-ability-and-stats.md` | `f5611332759af16658dce669552a04764672449e5e6aae73c2af5c61657c6f41` | 40,355 |

以下五份本轮行为修订已被接受，保持字节不变；GR-013 尚有WP42编号问题，不意味着其WP41／WP58行为需要重写：

| 文件 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `c456e49407c54a9f5dbae206698dd67af9e60894f2a05705abdfa11f9f2780bb` | 35,065 |
| `specs/combat/wp58-battle-recording-and-playback.md` | `74a2077b517a10051a3edaf5b178986f0e4510d5f891726b3ed32601f212b995` | 32,625 |
| `specs/combat/wp47-b-switching-control-and-item-changes.md` | `00409b29ded9dbd29d29e1a9384b9bc365c4da1e55f6b70326e05cc01d10866e` | 43,261 |
| `specs/combat/wp52-a-generic-numerical-and-status-evaluation.md` | `42138911ff6ec27780170f10c630c0e9e4eacae1f59e4f36d6658b6e5022cc67` | 52,988 |
| `specs/combat/wp52-b-field-damage-healing-and-target-evaluation.md` | `15e28d3975d69eb5735004c38297f2dcee34d6617bbc1bbc20f8258d304c66c5` | 47,142 |

六份只读支持稿及WP62、GR-001～012、第一组31项、WP23-N01与其他既有批准范围均保持。GR-014／015的关闭结论继承，不在本轮集中回填旧头部或管理状态；矩阵六行归属已接受，不需要挪行或合并／重复计算问题。

新交付目录使用 `review/gr013-gr016-revision-2026-10-01/revision-v2/`，v1材料留史。先实测两份基线及受保护文件，再修订；差异以本轮reviewer input-snapshot当前稿为起点。

## 2. GR-013：只修WP42新增案例编号冲突

WP42 §9 当前第287～289行新增的BURMY三例用了E07／E08／E09；第290～292行原有病毒传播、调试中止、未退物品三例也使用同名。当前34条带编号行只有31个唯一编号，新例“同E07”的引用也歧义。

保留旧三例的编号、内容和历史引用，只对新增三例使用未占用编号。例如当前未占用的 **E07b／E08b／E09b**；也可采用另一组经验证唯一的编号。同步新增例内“同E07”等交叉引用、当前§13注记与v2交付引用。明确旧到新编号映射；不要全仓替换历史E07／E08／E09，更不能改v1回应、旧diff或reviewer快照。

参战标记写入／读取口径、BURMY正反例与WP58回放结论均已接受，保持行为、输入和预期；不重写WP41／58或引入新场景族。

验收要求：WP42当前34条编号案例应有34个唯一编号，原31个编号和案例仍在，新增三例引用唯一可解析；对七份现稿的同格式案例标识扫描无新增冲突。只扫描活动稿来判当前唯一性，历史快照中的旧名字正常保留。

## 3. GR-016：去掉“设施EV合计恒为510”，补四项余数对照

WP19 §4.4 第152行新加“合计恒为510（项数≤510的整数商）”没有来源支持。设施创建是逐项整数分配，不补余数。原默认SUNKERN双项255／255、DROWZEE三项各170与禁用计算不改变存储这三例均正确，保持它们。

请删除该一般保证，明确：**对非空、由不同有效努力项构成的模板**，设总额为E、项数为n，每个指定项得到⌊E/n⌋，新个体的这些项合计n×⌊E/n⌋，其余项仍为0；未分配余数不会自动补到任一项。仅能整除时合计等于E。不要把此“不同项”公式无条件推广到重复项；本轮无需扩展重复项完整目录。

补一组合法人工模板的静态验收：默认E=510；四个互不重复的有效努力项 **HP／ATK／DEF／SA**；模板其余字段、等级、IV、训练家合法且创建正常返回，无额外EV写入。可沿用SUNKERN模板的其它有效字段，仅将努力项作为人工输入设为四项；**必须标为人工输入，不伪称默认PBS中存在该行**。结果四项各127、其余0、总508，未分配2；不是总510，不补余数，也不夹到252。

回源核对 `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:113–138,201–217` 的有效项解析与逐项写入，和 `Data/Scripts/014_Pokemon/001_Pokemon.rb:1191–1197` 的初始零值；具体身份见 [source-checks.json](source-checks.json)。仅静态阅读和510÷4、127×4等固定常数核算，不修改PBS、不执行编译／创建／生成器或行为模型。

扫描本轮新增当前结论和状态注记中的“恒为／必为510”等同根表述，作最小同步。保持设施255例外、普通培养入口上限、存储不钳位与原能力计算公式，不改WP55／57的正确行为。

## 4. 交付、自检与停止点

逐ID回应上述两项，提供两份主稿精确diff、完整旧新身份绑定、编号唯一性及四项508静态验收。当前修订仍标ReviewPending，不自批GR-013／016关闭；保留其余通过结论。

只作这两份规格及必要的活动登记／引用身份同步。更新manifest与主TSV后全量复测路径集合、重复、哈希／字节、短标签、链接、JSON、diff精确重建和阶段最终身份；另外执行案例编号唯一性检查，文件登记零偏差不能替代它。旧材料／快照及五份保护稿要逐字节保持。最后再固定阶段检查，避免自引用循环和登记前后身份混用。

不修改reference，不复制源码进规格，不实现框架，不运行游戏、战斗、回放、AI、PBS编译或设施生成，不操作真实存档或真实数据；不创建任务／Agent、不发跨会话消息、不提交／推送。

**完成后停在GR-013／016定点复审送审点。** 本轮不启动WP65等新包、集中回填、B批整合或整体double review。

路线提醒：已知GR全部关闭后，仍有WP65／WP67-A／WP67-B、WP37／WP53／WP61、WP72／WP73-A／WP73-B、WP74／WP75／WP76、WP77共13个内容包。按既定有界批次提取／审查；全部完成后才做WP78／WP79整体double review，最后WP80。不要把“16项GR都做过修订”当成全部内容包已完成。
