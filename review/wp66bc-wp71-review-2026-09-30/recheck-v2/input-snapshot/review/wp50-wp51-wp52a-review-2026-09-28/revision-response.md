# WP50／WP51／WP52-A 首审有限修订回应

2026-09-28；提取方。依据[report.md](report.md)与[revision-prompt.md](revision-prompt.md)，仅处理两原编号、BATCH-C01、WP51限定回填与直接传播。两必修项为提取侧已修订待复审，不自行CLOSED或Reviewed；前批三观察/C01及回填已接受，不重开。

## 1. 固定预检与保护

六主稿/附表＋矩阵＋manifest＋摘要九件必检，另self/boundary/主TSV三件配套，共12件SHA-256/字节及逐字节均匹配本轮input-snapshot。实测详值在交付self的preflight；reviewer原件共14件，修改前已测量固定。当前reference仍固定8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b且只读；无参考执行。

## 2. WP50-R01 — 已有限修订，待复审

**回源核实**：AbilityAndItem:212–221、399–449；ItemEffects:364–404及五混乱果调用265/296/310/340/438。参数是“半血扩展是否要求有效贪吃”，false省去贪吃条件，食果门仍先行。ORAN/SITRUS传false；五混乱果≤6 false、≥7 true；默认true的其它果保持原门。报告成立，无反证。

**修改位置**：WP50 §4参数段、ORAN/SITRUS与五果行，替换V05错误期望；新增V29–V33。旧false禁止扩展／四分之一专属断言已删除。覆盖附表只登记身份/主节，没有错误阈值，保持原字节。

**静态验收**：普通有效、可治可食且无额外连锁：ORAN H100/HP26无或有效贪吃均36；HP50→60、51不触发；SITRUS半血无贪吃→75；五混乱果世代6半血无贪吃→请求12至62；世代8无贪吃半血拒、有有效贪吃→请求33至83。新增UNNERVE对照仍被先行食果门拒。分支逐处手工核，数值只独立常数算术。

**传播与保留**：self当前V05和新向量、boundary B01/B02与摘要更新；WP51/WP52-A引用级联WP50 v2且注明尚未外审。V06 RIPEN取整与V07 forced满HP／Nature对照保留；恢复量、强制入口、消费/颊囊/共生与C/I/R/P/Belch不重写；WP28与WP51主动道具估量未改。

## 3. WP52-A-R01 — 已有限修订，待复审

**回源核实**：AIMove:336–355三墙均调相同计数；Battle:458–460/474–475筛非空、未濒死、同侧场上对象，包含T，排倒下/空席/后备。与名义布局不同，报告成立。

**修改位置**：WP52-A §3.2中等D/F行，将侧规模改为目标当前同侧存活场上人数，并明确三个墙分支；新增N09–N11分别定位物理反射壁、特殊光墙及极光幕的物理/特殊分支。

**静态验收**：固定名义双席，中等技能、普通单目标L50/P80/A100/D100、零阶、会心级0且无幸运咒/禁会心覆盖，无本系/天气/其它倍率，未绕墙且相应墙正。墙前37：两名存活R(37×2/3)=25；另一人倒下或空位、仅T活R(37/2)=19；后备不参与。三分支分别定位，不执行AI。

**传播与保留**：self新增N09–N11与两项常数，boundary B04、摘要及矩阵同步；WP51改引用限定通过回填版、WP50引用未审v2，附表只传播WP51状态。保留中等、预计非会心、无穿墙/不忽略墙、极光幕优先/类别门；WP43/49及已支持负会心索引、96命中边界、非致死截断不改。

## 4. BATCH-C01与WP51管理回填

**回源与维护**：Switch:476–496对至少一组后备/招/对手未被吸收即可停止搜索，WP51 §3.1改清存在性，新增S06一吸收一不吸收/全吸收局部对照。AIBattler:60–65在天气期限1重估默认天气，CLOUDNINE/AIRLOCK和UTILITYUMBRELLA分别清相应预计天气，WP51 §3.3具名化并新增S07；NEUTRALIZINGGAS不是这里直接清天气门。没有改其它位置正确的气体条件、后续按能力身份分派的既有差异或治疗估量。

**管理状态**：依报告§4–5，WP51主稿/附表与F12-07限定Reviewed，A～E控制/技能/换人替补与残余近似/主动道具/Mega/候选目标/权重/回退及具名失败边界。C01维护、状态回填及哈希级联在diff中可区分，附表默认数据不变。WP50、WP52-A与其矩阵子范围继续ReviewPending；新增通过集合只有WP51，不写成WP50–52连续通过。

## 5. 被审首稿与当前实测身份

| 文件 | 被审v1完整SHA-256 | v1字节 | 当前完整SHA-256 | 当前字节 |
| --- | --- | ---: | --- | ---: |
| `specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md` | `937551e00ec61a8a807bfa197ece1e2f91b6b5f91f620375e6c14ea900e9027a` | 29,336 | `fcbbca67dafbb1aaa1cfd2560983a6f34830c31c11feccb7688f08b372a395b1` | 31,648 |
| `specs/pokemon-rules/wp50-held-item-effect-coverage.md` | `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686` | 13,855 | `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686` | 13,855 |
| `specs/combat/wp51-ai-action-selection-and-skill.md` | `1174d485f2648682cbd98a446044dfd487bab694d7afdb94e309f3d3fe4a6972` | 25,064 | `baebd58a7f4eed635f685f583fa7b4d21785a9ac13a0a1ee4c2ccd6ec7b6bac5` | 26,784 |
| `specs/combat/wp51-ai-decision-defaults.md` | `f3837410a9c41617495d2691e69f2e7baa11e7e5c3d7521f618a0f1472ad6c09` | 4,811 | `5069a3690c6886204ebe9877ff0165e77c4c437fb8273032ac9d6f52bf89c2d0` | 5,472 |
| `specs/combat/wp52-a-generic-numerical-and-status-evaluation.md` | `f7f400c642d77f29c5411ac156fe0e49716848b87ed232b02b8d418e1c67126a` | 46,332 | `6c0534fea6d4a18284c1e54a38e413ad010d38291088b0df45d8ac087ca44c9c` | 48,127 |
| `specs/combat/wp52-a-evaluation-coverage-and-data.md` | `b620a868091aff4e1bb519f18e89698688eef279dbb020f828e2a0dfa25739c6` | 58,177 | `a5a13acaf8572fa621b91911430b2286b23340618c72d4b5d2e1522aaf4ec5f9` | 58,772 |
| `planning/feature-matrix.md` | `35935419cb9648d4bfd60665d7a7719a9d79230b9d7585bf852a9120ef87ab30` | 49,556 | `f2c1a5810dd6fcba6fc7f37f0c0fd5666062f81e8628b70471993cc62d9a1001` | 49,715 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/self-checks.json` | `5faccf42e26c67da07e0d844cc03a0d4c9120246e6823f7bab438691361279fc` | 364,926 | `0960427cb4ce0f2044604a15b1754dc310f47162d1e16ad67999dd753ad4111d` | 416,764 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/boundary-checks.json` | `f5eb0aca474da0ba48adb816b8289b3b4a8e4e5966fe4dbcd18b8a3e69fc914d` | 14,164 | `82c7c95c75abd44d48213cc470b16ca62c21123eb332d09b36905aeae6b1be90` | 31,428 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/delivery-summary.md` | `0df9331d437df132728bc58cb36af53d16d09c4f787e99445db3de56c483029b` | 6,554 | `7f2207b4267758a9483bd7042554116192c669061663a07c5178c3ec63c66748` | 9,407 |

WP50主稿v2、WP52-A主稿/附表v2均待复审，WP50附表v1未变；WP51为限定通过后的维护回填v2。当前self/boundary/摘要v2保留revision_history或被审表，不以新字节冒称已审版。

## 6. 差异、自检与停止

[revision-diffs](revision-diffs/)共9份：5规格＋矩阵＋摘要/self/boundary，基线均本轮input-snapshot。原18份回填diff只重建到本轮快照中的v1，不覆盖成当前差异。原101场景仅替换V05错误期望并新增10对照，当前33/25/53＝111；原21常数保留，新7项共28。登记身份、32族196物品/AI334个A登记、B/C分工、三个前向重复键、267评级数据不变。

TSV v29／manifest第五十四轮保留原491/587行、补登本轮14 reviewer原件＋本回应＋9份diff，新增24行。最终完整哈希/字节/短标签、缺失/重复/集合、链接/JSON/绑定、9份新diff及18份历史diff到快照重建、589/548/521快照与reviewer保护、reference HEAD/Git状态由登记后脚本实测，结果在交付消息报告，不把这些完整性检查称外审通过。

**只送WP50-R01、WP52-A-R01、BATCH-C01、WP51管理回填及直接传播有限复审后停止**。不启动WP52-B/C或任何下一批；不发reviewer消息、不创建任务/Agent、不提交/推送。运行、Demo/宿主/媒体/插件/U01–U10及WP78→79→80出口保留。未运行参考Ruby/表达式/事件/生成器/编译器/转换器或真实网络，未操作真实地图/存档/输入，未实现框架。
