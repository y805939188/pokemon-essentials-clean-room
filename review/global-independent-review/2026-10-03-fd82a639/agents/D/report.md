# SPEC_ONLY_READER D — 独立净化规格阅读报告

RUN_ID：2026-10-03-fd82a639。结论：**全文阅读完成；存在待澄清合同，不能判为内部一致性通过。**

- **131/131份全文实读**，共23,153行、1,391,830字符；未读清单为空。
- G01–G41分组推进，每份完整行段登记于`reading-log.tsv`，各组独立判断保存为`group-01.md`至`group-41.md`；发生的工具输出截断已补读，不能以关键词扫描替代全文阅读。
- **25项OPEN：P2 24项、P3 1项；P0/P1 0项。**这些是净化文本内部矛盾、未定义必要数据/条件或不充分测试输入，未断言源码一定有错。
- **参考/游戏/编译器/生成器/模拟器/反序列化/行为测试执行次数均为0。**仅使用允许文本的读取、文本搜索/计数及独立固定算术。静态测试目录未被称为已执行测试。
- 输出仅写入本任务`reader-output/`；未修改任何输入材料或新框架代码。Standard速度状态：**UNVERIFIED**。

## 阅读与判断范围

本轮是SPEC_ONLY_READER D：只从清单内的最终净化材料判断独立读者能否确定输入、状态、数值规则、失败/取消出口和预期结果，不要求源码证据，不提出具体实现/API，不以源架构或Pokémon常识补全。各文件即使被全文阅读，也不等于其中的引用材料已在本轮访问；范围外依赖单列。

## 发现索引

| 编号 | 优先级 | 合同范围 |
| --- | --- | --- |
| RUN-D-001 | P2 | WP80 scope |
| RUN-D-002 | P2 | WP13 interpreter command 314; IM01/IM09 |
| RUN-D-003 | P2 | WP14 room count |
| RUN-D-004 | P2 | WP15 audio parameter parsing |
| RUN-D-005 | P2 | WP25 capture storage; PS-11 |
| RUN-D-006 | P2 | WP33 compatibility; DC-08 |
| RUN-D-007 | P2 | WP36 EN-01 encounter opportunity / active request |
| RUN-D-008 | P2 | WP28 / WP19 EV caps |
| RUN-D-009 | P2 | WP18 creation / WP21 creation forms |
| RUN-D-010 | P3 | WP44/WP46/WP48/WP50 coverage inventories |
| RUN-D-011 | P2 | WP52-C gem ItemRanking; CE C05 |
| RUN-D-012 | P2 | WP52-C LowerPPOfTargetLastMoveBy4; CE C41 |
| RUN-D-013 | P2 | WP43 / WP46 / WP54 OHKOIce target eligibility |
| RUN-D-014 | P2 | WP09 / WP65 debug skip-continue startup |
| RUN-D-015 | P2 | WP71 mode 7 five-move initialization |
| RUN-D-016 | P2 | WP72 battle effect editor whitelist |
| RUN-D-017 | P2 | WP67-A target cursor initial choice and cross-side navigation |
| RUN-D-018 | P2 | WP42 end-of-round automatic distant-position adjustment |
| RUN-D-019 | P2 | WP19 Nature modifiers and mint/stat calculations |
| RUN-D-020 | P2 | WP21 form submission move rewrites |
| RUN-D-021 | P2 | WP66-A PT A23/A31/A33 fixtures |
| RUN-D-022 | P2 | WP73-A / WP74 / WP72 Demo-DX test selectors |
| RUN-D-023 | P2 | WP66-C BP shop display total |
| RUN-D-024 | P2 | WP74 freehand and frame-count resampling |
| RUN-D-025 | P2 | WP72 debug variable type/value toggle |

## 逐项发现

### RUN-D-001 · P2 · WP80 scope

类型：contradiction/scope。状态：OPEN。

文字证据：

- `scope-statement.md:7-9`：当前仅批次 1（WP16 两文）——未列批次不代表已净化。
- `README.md:31-48`：列出批次 1–15 已交付；全集 113 份输入已全部交付，本目录当前内容为全集交付状态。

两种结果／最小反例：

1. 以约束整个规格集的 scope 为准，仅 WP16 两文可视为净化正文，后续批次不在可使用范围。
2. 以 README 全集交付状态为准，目录内批次 1–15 均可作为净化正文。

影响：实现方无法一致判定本包哪些合同为有效交付范围，既可能拒用绝大多数内容，也可能违背必读范围约束。

最小澄清：更新 scope 的当前批次与完成度到本交付基线，并统一 README 范围声明。

可判定复审条件：两文对当前已交付批次和可使用正文范围给出同一结果。

验证口径：static textual comparison only。

### RUN-D-002 · P2 · WP13 interpreter command 314; IM01/IM09

类型：test-oracle contradiction。状态：OPEN。

文字证据：

- `test-catalog/engine-overworld-wp11-15-59-60.md:123-131`：IM01 将 311–322 全部列为跳过且无效果；IM09 对 314 参数 0 则要求按配置治疗队伍或队伍及储存。
- `engine-overworld/wp13-interpreter-command-matrix.md:95-98`：314 参数 0 为有实现的全部恢复；311/312/313 与 315 后各命令为空操作。

两种结果／最小反例：

1. 按 IM01 的闭区间 311–322，314 也无效果，受伤队伍保持 HP。
2. 按命令正文与 IM09，314 参数 0 治疗队伍，HP 恢复。

影响：同一固定命令存在相反测试预期，符合正文的实现会无法同时通过两项。

最小澄清：把 IM01 的范围写成 311–313、315–322，明确排除 314。

可判定复审条件：给 314 参数 0、受伤队伍及开启储存自动治疗的固定场景，所有相关条目均唯一预期队伍治疗。

验证口径：static comparison only。

### RUN-D-003 · P2 · WP14 room count

类型：undefined numerical rounding。状态：OPEN。

文字证据：

- `engine-overworld/wp14-random-dungeons.md:46-52`：默认节点 5×5，节点/可房间图样 full，房间概率 70。
- `engine-overworld/wp14-random-dungeons.md:94-98`：房间数＝可房间节点数 × 房间概率% 与 1 的较大者；随机抽取相应节点标记为房间。
- `test-catalog/engine-overworld-wp11-15-59-60.md:154-160`：测试只要求房间 ≥1、零房间回退，没有非整积的精确房间数。

两种结果／最小反例：

1. 25 个可房间节点、70% 时，17.5 向下取整为 17 个房间。
2. 同一输入按向上或四舍五入取 18 个房间。

影响：默认参数即可产生非整数房间数；两种实现布局分布与后续摆放容量不同，现有测试不能判别。

最小澄清：定义百分比乘积的整数化方式和执行顺序，并补 25×70% 的精确向量。

可判定复审条件：读者不依赖语言除法约定即可唯一得出 25 个候选、70% 时的房间整数数目。

验证口径：independent fixed arithmetic: 25*70/100=17.5; generator not executed。

### RUN-D-004 · P2 · WP15 audio parameter parsing

类型：ambiguous input grammar。状态：OPEN。

文字证据：

- `engine-overworld/wp15-resource-matching-and-audio.md:78-83`：字符串支持 文件名、文件名:音量、文件名:音调 三种形式，默认音量/音调 100。
- `test-catalog/engine-overworld-wp11-15-59-60.md:179-202`：RS01–RS20 未提供带音量/音调字符串的解析向量。

两种结果／最小反例：

1. 输入 theme:80 解析为音量 80、音调 100。
2. 同一字符串解析为音量 100、音调 80。

影响：两个已声明格式有相同词法形状，独立实现无法区分；影响音量与音调等可见输出参数。

最小澄清：给出可区分的完整格式或优先规则，并提供同时指定音量和音调及只给一个数的示例。

可判定复审条件：theme:80 及包含两数的合法字符串均有唯一解析结果；无需核验真实音频文件。

验证口径：static grammar analysis only。

### RUN-D-005 · P2 · WP25 capture storage; PS-11

类型：test precondition insufficient。状态：OPEN。

文字证据：

- `test-catalog/creature-rpg-wp18-20-24-25-26.md:121`：PS-11 仅给当前盒满、盒 2 有空位，推导写入盒 2 并返回 2。
- `creature-rpg/wp25-party-and-storage.md:94,154`：当前盒优先首个空位；否则从 0 号盒起扫描所有盒。

两种结果／最小反例：

1. 当前盒为 3 且满，盒 0 有空位，盒 2 有空位：按正文写入盒 0、返回 0。
2. 当前盒为 3 且满，盒 0/1 满而盒 2 有空位：写入盒 2、返回 2。两组均符合 PS-11 输入。

影响：符合正文的盒扫描实现可能不满足测试给定结果；该条不能作为确定性验收向量。

最小澄清：补充盒 0 和盒 1 已满、当前盒不是可用盒的完整前提，或把预期改为从 0 起首个有位盒。

可判定复审条件：给定所有较早候选盒的占用后，PS-11 唯一推导盒 2；另设盒 0 有位对照应返回 0。

验证口径：static specification/test comparison only。

### RUN-D-006 · P2 · WP33 compatibility; DC-08

类型：test-oracle overgeneralization。状态：OPEN。

文字证据：

- `test-catalog/creature-rpg-wp27-28-29-30-33.md:182-183`：DC-07 要求 Shadow/Undiscovered → 0；DC-08 对 Ditto+任意非 Ditto 预期兼容。
- `creature-rpg/wp33-daycare-and-breeding-session.md:111-118`：任一个体为 Shadow 或蛋组含 Undiscovered 先返回 0，之后才检查 Ditto 性别例外。

两种结果／最小反例：

1. 按 DC-08 的任意非 Ditto，Ditto 与含 Undiscovered 的非 Ditto 个体兼容。
2. 按正文先行守卫和 DC-07，同一输入兼容等级 0。

影响：测试把性别兼容例外扩大为绕过前置资格，独立实现无法同时满足泛称测试与正文。

最小澄清：将 DC-08 限定为两个占用槽且双方非 Shadow、均不含 Undiscovered，再描述 Ditto 的性别兼容例外。

可判定复审条件：Ditto+Undiscovered、Ditto+Shadow 均唯一预期 0；合法非 Ditto 对照才按物种和拥有者算等级。

验证口径：static textual comparison only。

### RUN-D-007 · P2 · WP36 EN-01 encounter opportunity / active request

类型：test precondition insufficient。状态：OPEN。

文字证据：

- `test-catalog/creature-rpg-wp35-36-57-64-68.md:33`：EN-01 仅给本地图无任何 land/cave/water 表，预期机会判定假、步进不触发、主动请求各自失败。
- `creature-rpg/wp36-wild-encounters-and-modifiers.md:75-78,85,188-193`：fishing/none/contest 为独立类；冲浪中机会判定直接为真；主动请求按请求类型取候选，有合法候选且调用正常返回时返回真。

两种结果／最小反例：

1. 地图无 land/cave/water，但有合法 OldRod 表，正常主动请求 OldRod 可以选择候选并返回 true。
2. 地图既无 land/cave/water 也无所请求的 OldRod 表，主动请求返回 false。两组都符合 EN-01 所列输入。另在冲浪状态机会判定本身仍为真。

影响：把三类步进表的缺失扩大为所有主动遭遇失败，并省略冲浪优先分支；正常的独立钓鱼实现会违背该测试预期。

最小澄清：分别限定非冲浪的机会判定、步进触发，以及请求类型自身无表的主动请求场景。

可判定复审条件：无步进类表但有 OldRod 表的固定正常场景允许主动请求成功；非冲浪且无步进表才唯一预期机会判定假。

验证口径：static comparison only; no encounter or game execution。

### RUN-D-008 · P2 · WP28 / WP19 EV caps

类型：cross-spec invariant contradiction。状态：OPEN。

文字证据：

- `creature-rpg/wp28-item-use-and-training.md:211-213`：252/510 是所有 EV 写入的统一上限。
- `pokemon-rules/wp19-attributes-ability-and-stats.md:119-126,188,201`：252/510仅为培养/增量写入者保证；设施/工厂正常模板创建两项各255，数据层自身亦不钳制。
- `demo-dx/wp76-facility-content-generation-and-simulation.md:114`：生成路径单EV条目510，两条255；不自动夹回252。

两种结果／最小反例：

1. 按WP28的全称不变量，设施创建也须将每项255夹为252，或拒绝255。
2. 按WP19明确例外，设施两项保持255、合计510，不夹252。

影响：统一数据校验可能错误改变正常设施个体的存储EV，使跨模块状态与测试不一致。

最小澄清：把WP28不变量收窄为本包培养/增量写入入口，明确引用WP19的设施创建和原始存储例外。

可判定复审条件：双努力项设施模板稳定保留255/255；相同属性的培养道具路径仍遵循252/510余量约束。

验证口径：static cross-spec comparison only。

### RUN-D-009 · P2 · WP18 creation / WP21 creation forms

类型：cross-spec random contract contradiction。状态：OPEN。

文字证据：

- `creature-rpg/wp18-creature-identity-species-ownership.md:168,170-172`：创建复检可调用创建形态处理器；紧接文字却称创建时只有personalID和六项IV两类随机来源。
- `pokemon-rules/wp21-dynamic-forms-and-display.md:60-73,158`：创建形态族另有UNOWN随机0–27、PUMPKABOO概率档、MINIOR随机7–13、ALCREMIE随机0–62、URSHIFU随机0–1等。

两种结果／最小反例：

1. 把WP18的只有两类作为完整创建合同，所有其它创建结果由PID/IV和上下文确定，不另作形态随机抽样。
2. 按WP21正常创建复检，对具名物种另取随机形态；创建合同必须包含该随机输入。

影响：独立实现与可控随机测试会漏掉正常创建路径的随机形态步骤，无法统一规定创建所需随机输入和输出。

最小澄清：将两类限定为基础个体初始化，并明确创建复检可能追加WP21的随机形态输入。

可判定复审条件：UNOWN复检开与关的创建输入清单分别明确是否需要额外形态抽样；不再对完整创建宣称仅两类随机。

验证口径：static cross-spec comparison only; no random generator executed。

### RUN-D-010 · P3 · WP44/WP46/WP48/WP50 coverage inventories

类型：coverage inventory inconsistent counts。状态：OPEN。

文字证据：

- `pokemon-rules/wp44-effect-coverage.md:15-17`：§2.1 列表实际65个标识，说明却称以上68项。
- `pokemon-rules/wp46-damage-healing-coverage.md:7-41`：主族标题声称36/22/43/22/4/16，实际逐行标识数为30/22/44/23/4/16；合计实际139，标题合计143；计数说明又称§3族31＋Struggle＝32。
- `pokemon-rules/wp46-damage-healing-coverage.md:51-65`：域外A/B/场域/状态标题声称25/26/24/30项，实际列出45/20/28/29项。
- `pokemon-rules/wp48-ability-calculation-modifiers.md:203,217,219`：StatusImmunity标题8实列11、DamageCalcFromUser标题41实列43、Target标题15实列14；逐族标题合计144而实列148。
- `pokemon-rules/wp50-held-item-effect-coverage.md:11-22`：Speed9实10、HPHeal17实16、StatusCure9实8、TargetAccuracy3实2、UserDamage86实71、TargetDamage25实23；逐族标题合计215而实列196。

两种结果／最小反例：

1. 按标题计数分配覆盖与测试责任，WP46主合同需143项，A责任25项。
2. 按实际列举标识分配，主合同139项，A责任45项；同一份交付产生不同基数。

影响：覆盖统计无法稳定复算；不能用标题作为责任或验收数量依据，但这本身未证明139主合同有实际遗漏。

最小澄清：按实际明确的计数口径同步四份文档各族标题/说明；分清唯一标识、跨族重复和行为行。

可判定复审条件：文本枚举计数与各族标题一致，WP46的139、WP48的148、WP50的196均可从净化枚举重算且族数相加同总数。

验证口径：text-only regex count of explicit backtick identifiers; no source/code executed。

### RUN-D-011 · P2 · WP52-C gem ItemRanking; CE C05

类型：parameter/condition contradiction。状态：OPEN。

文字证据：

- `combat-requirements/wp52-c-item-control-coverage-and-data.md:100,116`：FIREGEM默认基础评级6；条件表说明基础值≤5先＋2。
- `combat-requirements/wp52-c-items-calling-and-control-evaluation.md:58`：18类型宝石：≤5先＋2；有对应可用伤害招保留（通常6或8），未写≤5的参数名。
- `test-catalog/combat-requirements-wp49-51-52.md:216`：CE C05中等火宝石，有可用火招，世代5/8分别预期8/6。

两种结果／最小反例：

1. 按附表明确的基础评级≤5条件，火宝石6不加2，世代5和8均为6。
2. 按C05把≤5解释为机制世代，世代5得8，世代8得6。

影响：同一默认物品在旧世代产生不同AI物品价值，连带偷取、交换、投掷等评分差异；正文省略变量无法消除附表冲突。

最小澄清：为≤5明确写出所比较参数，并统一正文、附表和C05。若预期确为世代门，删除附表的基础值措辞。

可判定复审条件：基础6、合法火招、中等技能、无其它后置加分的FIREGEM在世代5/8有唯一一致评级。

验证口径：static comparison and fixed arithmetic only。

### RUN-D-012 · P2 · WP52-C LowerPPOfTargetLastMoveBy4; CE C41

类型：test-oracle arithmetic contradiction。状态：OPEN。

文字证据：

- `combat-requirements/wp52-c-items-calling-and-control-evaluation.md:171`：降PP4：U更快时PP≤4加20、≤6加10、>10减10；所有未早退情况最后−10。
- `test-catalog/combat-requirements-wp49-51-52.md:252`：C41较快U、PP6/7/11预期＋10/−10/−10。

两种结果／最小反例：

1. 按正文累加末尾−10：PP6为+10−10=0，PP7为−10，PP11为−10−10=−20。
2. 按C41：PP6为+10，PP7为−10，PP11为−10；等于部分分支没有执行正文承诺的末尾项。

影响：同一局部评分输入的确定输出冲突；根据正文实现的评分无法通过C41，且可能改变动作权重。

最小澄清：核定末尾−10适用的实际分支，统一正文流程和C41三个向量；不以真实战术常识决定答案。

可判定复审条件：输入基分100、U更快、最近槽合法且PP6/7/11、无其它修正时，正文和测试逐项给出相同局部终分。

验证口径：independent fixed arithmetic: 10-10=0; 0-10=-10; -10-10=-20; no AI executed。

### RUN-D-013 · P2 · WP43 / WP46 / WP54 OHKOIce target eligibility

类型：cross-spec stale refusal rule。状态：OPEN。

文字证据：

- `pokemon-rules/wp43-types-accuracy-and-damage.md:78`：冰系一击必杀分支对非冰使用者减10，冰目标先失败。
- `pokemon-rules/wp46-damage-multihit-and-healing.md:97`：原定义先拒冰；条款文件加载后且无后续覆盖，条款假走继承的等级/坚硬门，不再仅因冰拒绝。
- `combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md:136-142`：固定既定加载顺序、ohkoclause假、双方同级50、冰目标无坚硬及其它门过，目标失败查询不拒；AI预测拒冰独立保留。

两种结果／最小反例：

1. 按WP43未限定的冰目标先失败，固定场景在目标资格处拒绝，不进入命中。
2. 按WP46/54当前加载合同，同一固定场景目标资格通过，再用独立命中阈值；可继续到伤害判定。

影响：真实战斗基础计算规格仍保留旧拒绝摘要，与已明确的当前加载状态相冲突，实施者可能错误加回冰免疫门。

最小澄清：将WP43此处目标拒冰文字限定为原定义，当前加载后资格引用WP46/54；保持命中−10公式及AI预测的独立差异。

可判定复审条件：上述同级冰目标夹具在三份真实合同中均不因冰属性本身拒绝；条款真时均拒；AI仍按独立预测说明。

验证口径：static cross-spec comparison only; no battle or clause execution。

### RUN-D-014 · P2 · WP09 / WP65 debug skip-continue startup

类型：test missing save-state premise。状态：OPEN。

文字证据：

- `test-catalog/generic-kernel-wp05-06-07-08-09-10.md:95`：SV02仅给出调试模式＋无打包归档＋SKIP_CONTINUE_SCREEN三者成立，预期跳过菜单直接新游戏。
- `user-interface/wp65-title-load-options-pause-and-pc.md:35-36`：相同跳过门满足时，无存档直接新游戏，有存档直接按已读数据载入。
- `test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:94`：NV-T03明确无存档新游戏、有存档直接载入的两分支。

两种结果／最小反例：

1. SV02所列三门为全部前提，则有有效存档时仍应直接新游戏。
2. 按WP65三门只决定跳过菜单；同一有效存档输入直接继续载入已有进度。

影响：SV02可把正确的已有存档继续流程判为失败，或诱使实现跳过并丢弃本应载入的进度。

最小澄清：SV02补无存档前提，并增加或交叉引用有效存档时直接继续的对照向量。

可判定复审条件：三门全真且无存档预期新游戏；三门全真且有有效存档预期继续，两个状态均有可判定结果。

验证口径：static premise comparison only; no save read/write or startup execution。

### RUN-D-015 · P2 · WP71 mode 7 five-move initialization

类型：fixed arithmetic contradicts initialization reachability。状态：OPEN。

文字证据：

- `user-interface/wp71-tile-puzzles.md:47,76-77,122`：模式7从完成态执行5次联动旋转；同时称未排斥抵消后全0，并把7列为初始即完成模式。
- `user-interface/wp71-tile-puzzles.md:49,66`：每次合法操作使所选格及全部有效相邻格角度各减1 mod4。

两种结果／最小反例：

1. 按初始化可达性声明，默认4×4的5次联动旋转有机会回到全0并首帧完成。
2. 按动作规则的固定奇偶量，5次后必非完成。取T={4,5,6,7,8,11,12,13,14,15}（行优先零基），16个合法联动组与T的交集数依次为1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3，均奇数。每步翻转T内角度和的奇偶，初始0经5步为奇，全0必为偶，故不可能。

影响：规格声明了由给定初始化无法产生的正常完成入口，测试设计或初始化兼容会据此接受不可达状态。

最小澄清：撤回模式7由五次初始化抵消为全0的可达声明，区分任意外部状态与正常五次构造；其它模式的初始完成可能性按各自尺寸限定。

可判定复审条件：默认4×4的16项交集固定算术均为奇，正文与测试不再声称正常模式7五次构造可首帧完成；仍允许之后合法玩家操作完成。

验证口径：independent fixed-set parity proof only; no puzzle generator, simulation, solver or reference execution。

### RUN-D-016 · P2 · WP72 battle effect editor whitelist

类型：required normative catalogue outside sanitized handoff。状态：OPEN。

文字证据：

- `demo-dx/wp72-debug-contexts-and-controls.md:212-215`：效果编辑以成员83、阵营22、全场13、席位2共120项为白名单，表外不可编辑；逐项类型、默认、范围与哨兵只指向清单外review/wp72-delivery-2026-10-02/revision-v2/battle-effects-catalog.md。

两种结果／最小反例：

1. 读者仅依总数，可把某成员效果E放入83项白名单。
2. 同样总数可用另一效果替代E，令E不可编辑；正文没有成员表或等价选择规则裁决。

影响：允许的131份净化材料不能确定某项效果是否出现、其值类型和合法范围；这是交付自足性缺口，不是断言外部表不存在。

最小澄清：把120项行为化目录作为净化正文附表交付，或明确把该编辑能力标为未闭合而不让未来实现依赖清单外review。无需附源码或原结构。

可判定复审条件：净化允许集内能逐项回答白名单成员、层级、类型、默认、范围/哨兵，并与120项计数及编辑行为一致。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

### RUN-D-017 · P2 · WP67-A target cursor initial choice and cross-side navigation

类型：missing deterministic target-order data。状态：OPEN。

文字证据：

- `user-interface/wp67-a-battle-interaction-and-presentation.md:95-96`：Foe/Other初选取对位次序表首个未昏厥者，跨侧导航也取表首非nil；只列1v2=[3,1]，其余仅称2v2按位置四组、2v3/3v2/3v3各组。
- `test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:298`：K09的2v2预期仍只是对位次序表首个未昏厥者，没有给出实际位置。
- `combat-requirements/wp39-battle-context-and-participants.md:157`：邻近关系给出可相邻集合，双侧≤2时任意异席均相邻；没有给同集合内的排序。

两种结果／最小反例：

1. 2v2中位置0使用Foe招式，对方1/3均存活，若次序[1,3]则初选1。
2. 相同输入若次序[3,1]则初选3；两表都满足已给邻近关系，允许材料未给优先值。

影响：默认双打的确认目标与跨侧导航不能由规格确定；测试K09循环引用未定义表，不能作独立验收。

最小澄清：补足每个已支持席位组合、每个来源位置的有序目标表或等价独立规则；区分该次序与邻近集合。

可判定复审条件：固定2v2位置0/2与敌方1/3的初选和跨侧导航均有唯一值，扩展组合也能直接查算，K09给出具体索引。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

### RUN-D-018 · P2 · WP42 end-of-round automatic distant-position adjustment

类型：source-dependent automatic reposition predicate。状态：OPEN。

文字证据：

- `combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:129`：远位自动调整仅说无近邻可交手时寻找同业主空位/中央位，涉及两个侧双席候选时按源排除相应交换。
- `combat-requirements/wp41-switching-positioning-and-escape.md:128-138`：Shift给出了玩家动作资格与交换后的写入，但没有远位自动调整的候选搜索次序与排除表。
- `user-interface/wp67-a-battle-interaction-and-presentation.md:65`：UI只列回末替补后远距移位并引用WP41。

两种结果／最小反例：

1. 3v3仅0和1存活且均可与本侧空中央交换时，先将0移至2即令双方邻近，随后停止。
2. 同一前提先将1移至3，或双方都移至中央；都符合寻找同业主空/中央位概括，但最终占位及指向效果不同。

影响：回末位置变化会影响后续邻近目标与索引效果，当前合同要求独立读者回看源才能知道哪些交换被排除。

最小澄清：将按源排除改为完整的行为条件、候选次序、每侧/全局终止条件，并给至少单侧可移与两侧可移的固定例。

可判定复审条件：给定席位、存活、业主与空位分布即可唯一算出自动交换序列；不需要源文件来补排除条件。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

### RUN-D-019 · P2 · WP19 Nature modifiers and mint/stat calculations

类型：missing fixed Nature-to-stat mapping。状态：OPEN。

文字证据：

- `pokemon-rules/wp19-attributes-ability-and-stats.md:79-83`：列25性格顺序与五个中性身份，其余仅称一项+10%、一项−10%，未列每个身份对应哪两项。
- `pokemon-rules/wp19-attributes-ability-and-stats.md:140-147`：能力公式需要每项的N=90/100/110，并称对该性格每项变化累加。
- `generic-kernel/wp03-content-identity-and-schema.md:63,199`：Nature为固定注册规则数据，主责指向WP19；不是由交付中某PBS模式另行提供的自由作者参数。

两种结果／最小反例：

1. 同一ADAMANT身份把攻击指定为+10%、特攻指定为−10%，符合其为非中性的一增一减概括。
2. 改把防御指定为+10%、特防指定为−10%也符合概括；若五项修正前均105，攻击可分别为115或105。

影响：正常创建、薄荷和重算无法仅用净化材料得到正确五维能力；不能要求实施者以外部Pokémon常识补足固定规则。

最小澄清：补25种身份到增/减能力的独立数据表（中性明确无），并给至少一个非中性六维固定向量。

可判定复审条件：所有25性格每项N均可在允许材料内确定，ADAMANT等非中性向量无需外部数据。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

### RUN-D-020 · P2 · WP21 form submission move rewrites

类型：missing form-to-move behavioral data。状态：OPEN。

文字证据：

- `pokemon-rules/wp21-dynamic-forms-and-display.md:79,83-84`：ROTOM形态1–5学习对应新招并有固定基础保底；NECROZMA/CALYREX学习/忘记专属招或固定基础招，但具体映射/身份未给。
- `pokemon-rules/wp21-dynamic-forms-and-display.md:162-169`：给出了直接改标识、交互学招、压缩和PP处理，但仍以形态招/专属招/保底招指代。
- `test-catalog/pokemon-rules-wp19-21-22-23-34.md:92-99`：FM13只补ROTOM形态2的HYDROPUMP；FM15仍以专属招表达预期，没有补全其它形态。

两种结果／最小反例：

1. ROTOM提交形态1且无旧形态招、存在空招槽时，取已登记招式X作对应新招。
2. 取另一已登记招式Y同样符合未具名的对应新招；待删除旧招的集合与保底身份也无法确定。

影响：形态切换的招式结果与缺目标招的失败条件不可独立验证；交付要求行为但缺不可自由选择的数据。

最小澄清：补齐四类提交处理器所需的形态→目标招、旧招识别集合、基础形态保底招映射；保持PP与交互合同分层，不复制来源代码。

可判定复审条件：对每个已列形态可直接写出具体招式前后列表，并可判定任意缺失目标身份是否触发具名失败。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

### RUN-D-021 · P2 · WP66-A PT A23/A31/A33 fixtures

类型：quantitative party test fixtures lack decisive constraints。状态：OPEN。

文字证据：

- `test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:181`：A23只给来源50/120、目标hp30，却定目标恢复24。
- `creature-rpg/wp28-item-use-and-training.md:142`：HP回复定值并封顶，消息含实际回复量。
- `test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:189,191`：A31给升级表2招未会、初始记录1招未会即定候选3；A33把非蛋选择中的蛋称为唯一合格成员。
- `creature-rpg/wp30-growth-learning-and-friendship.md:167-168`：最初记录仅前置未掌握且不在等级列表的项；去重。

两种结果／最小反例：

1. A23目标总HP≥54时恢复24；A31初始招在两升级招外时共3。
2. A23目标总HP40也满足原前提但只恢复10；A31初始招与其中一升级招相同也满足原前提但只有2。A33的蛋不能同时满足合格与被拒两项。

影响：这些固定预期不能唯一从测试输入推出，自动测试可误报正确的封顶/去重行为，A33还无法构造其文字前提。

最小澄清：A23补非蛋目标总HP≥54等合法门；A31补初始招不在两升级招内，或分重叠对照；A33把唯一合格改为唯一候选/唯一成员。

可判定复审条件：恢复量与去重计数均由完整夹具唯一计算，蛋拒绝用例不再含自矛盾合格前提。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

### RUN-D-022 · P2 · WP73-A / WP74 / WP72 Demo-DX test selectors

类型：test dispatch discriminants omitted。状态：OPEN。

文字证据：

- `test-catalog/demo-dx-wp72-73-74-75-76-77.md:49`：CE-M02泛称数值类数值取消/布尔类取消，预期均返回空清槽。
- `demo-dx/wp73-a-content-editors.md:42-49`：可空数值LimitProperty2取消为nil，UInt/Limit等按普通数值框；BooleanProperty与BooleanProperty2也有不同取消合同。
- `test-catalog/demo-dx-wp72-73-74-75-76-77.md:131`：AN-M28输入泛称音乐文件，预期音乐文件不复制，未限定.midi。
- `demo-dx/wp74-battle-animation-authoring-and-exchange.md:317`：wav/ogg/mp3/mid/wma可复制，仅.midi因后缀比较不命中不复制。
- `test-catalog/demo-dx-wp72-73-74-75-76-77.md:28`：DG-M18给对方人数2、首家仅1成员就定拒绝，没有该子例的训练家数量。
- `demo-dx/wp72-debug-contexts-and-controls.md:185`：首家仅1成员的拒绝还要求对方席位数大于训练家数。

两种结果／最小反例：

1. CE-M02取LimitProperty2、AN-M28取.midi、DG-M18取1名训练家，目录的既定预期分别成立。
2. CE-M02取旧值5的UIntProperty取消则返回5；AN-M28取存在且可复制的.wav则复制；DG-M18取2名各1成员训练家、对方2席且其余门过，不因首家1成员而拒。三组均符合目录现有泛称前提。

影响：净化测试丢失了决定分支的类型、后缀和人数，无法区分行为例外与一般规则。

最小澄清：各子例补具体属性变体、.midi后缀和训练家数；为普通数值/支持音频/两名训练家增加或指向反向对照。

可判定复审条件：每个子例的分派键明确，允许的相反分支不再被同一泛称测试覆盖成错误预期。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

### RUN-D-023 · P2 · WP66-C BP shop display total

类型：display formula missing quantity multiplier。状态：OPEN。

文字证据：

- `user-interface/wp66-c-bag-item-storage-and-shop-ui.md:98`：数量窗按floor(单价÷2)显示总价，文字漏数量因子。
- `creature-rpg/wp29-shops-and-exchanges.md:99`：BP数量窗显示为数量×floor(价÷2)。
- `test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:277`：C29单价20、数量2的数量窗显示20BP。

两种结果／最小反例：

1. 按WP66-C总价公式，单价20、数量2显示10BP。
2. 按WP29与C29，显示2×10=20BP；确认/实扣同为40BP。

影响：界面规格的总价公式与领域及测试不同，会使多件购买显示错价。

最小澄清：补数量×floor(单价÷2)，明确半价为显示单价的计算，实际确认与扣款仍全价。

可判定复审条件：价20、数量1/2/3显示10/20/30BP，各处一致。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

### RUN-D-024 · P2 · WP74 freehand and frame-count resampling

类型：path resampling grid/count undefined or contradictory。状态：OPEN。

文字证据：

- `demo-dx/wp74-battle-animation-authoring-and-exchange.md:235-239`：初次手绘称弧长等距重采样为N+2候选取前N，却给0→12,N4写0/3/6/9；改帧数也称N+2但未给参数网格。
- `test-catalog/demo-dx-wp72-73-74-75-76-77.md:121-122`：AN-M18重复同一数量与向量，AN-M19只定义任意t的弧长取点，未定义调用t序列。

两种结果／最小反例：

1. 若N+2指包含首末端的N+2个等距点，0→20,N4的6点为0/4/8/12/16/20，写前4即0/4/8/12。
2. 若按例子的步距总长/N，0→20,N4写0/5/10/15；要同时声称N+2个候选，需额外终点/重复点或越界处理，正文未定义。

影响：独立作者无法从该合同重建任意N的写入坐标；既定示例与通常的N+2等距点定义冲突，参数网格和取整时点无法判定。

最小澄清：直接给出候选参数t的序列、候选总数如何形成（是否含重复端点）、前N取舍与整数舍入规则；三个路径分别给非整点向量。

可判定复审条件：对0→20,N4及一条非整数分段线，能逐项算出全部候选和实际写入点，候选计数与现有0→12示例相容或明确修正。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

### RUN-D-025 · P2 · WP72 debug variable type/value toggle

类型：contradictory variable ACTION transition。状态：OPEN。

文字证据：

- `demo-dx/wp72-debug-contexts-and-controls.md:65`：ACTION在0与空字符串之间互换，但括注又写数值→0、字符串→空串。
- `test-catalog/demo-dx-wp72-73-74-75-76-77.md:17`：DG-M07明确预期0↔空串互换。

两种结果／最小反例：

1. 变量原值0按互换读法，ACTION后应为空字符串；原空串应为0。
2. 按括注类型归零读法，原0仍0、原空串仍空串，两个状态都不转换。

影响：同一次按键的值与类型变化相反，后续USE分派数值框还是文本框也不同。

最小澄清：改成按输入类型/值列明的转移表，至少列0、非零数、空串、非空串、其它类型；消除互换与同类型归零的冲突。

可判定复审条件：正文与DG-M07对0和空串两次ACTION有相同的唯一状态轨迹，其余类型行为也明示。

验证口径：static allowed-text comparison and fixed arithmetic only; no reference, generator, simulator, compiler or game execution。

## 已交叉消解或不立项的候选

- 电话双倒计时：WP63§5.2 line106明确共同菜单/战斗等守卫。WP06消费者表虽简写，未显式否定共同门；TM02可与完整合同相容，不立项。
- 地图恢复“空事件集合”：WP11明确nil，合法空容器的含义可经专门地图合同辨别；将WP09空字解释为缺对象即可相容，本轮不据此新增矛盾项。
- NPC默认EV的整数化由WP19明确；其它尚未形成决定性反例的除法/数据入口候选不立项。
- 接力效果白名单已在WP47-B的允许附表给出，不能因WP41仅引用就称缺失。
- 同排序菜单次序明确未承诺稳定，不能把允许的自由度当作欠定义缺陷。
- Palace基值/压半与Nest Ball边界可由允许测试补足；没有以官方机制常识改动参考快照。
- 无视觉辅助菜单Call的1/10在WP76明确是先未选Bag后的条件抽样，整体7/75；按具体合同能解读WP67-A摘要，不另立项。
- 异常/取消后的已提交副作用（邮件、储存、编辑器、净化等）以及生成器已声明无终止保护，是已写定的行为；只检查描述一致性，不要求参考行为被修成理想事务。

## 独立阅读限制

- 输入边界为 allowed-files.txt 的131份净化材料及本任务说明；允许文件内的审计、review、源码、外部网页链接一律未跟出清单。WP72必需白名单外置登记为RUN-D-016，不把未访问误称不存在。
- WP75的35对旧标识替换给出行为分组与若干身份，部分精确旧/新标识仍外置审计；本报告未取得这些兼容输入数据，不宣称能据此完成逐字符旧工程兼容。
- 宿主输入、图像/音频、存档与地图档案、事件可达性、随机实现、插件组合、异常顶层恢复均按各稿已声明边界保留；未用外部Pokémon知识补资料，也未把已明示的参考异常当成待修实现缺陷。
- 文中既有PASS_SCOPED、修订编号与批准状态仅作为输入文字，不构成本轮源证据或自动豁免；本轮只评价净化材料内部合同。
- 隔离为明确指令约束，不是硬沙箱。工具可能具备其它路径权限，但本次未读取参考、来源审计、历史review、仓库Git历史或他人发现；未派生子agent、未联网。
- 请求模型为gpt-6-astra、推理ultra；速度要求Standard。当前工具没有可用的速度设置/核验控制，因此speed_verified=UNVERIFIED，未声称已设置或已核验Standard。

## 交付自检

覆盖登记为131个唯一允许路径，均为完整1–末行；未读0。25个发现编号唯一，所有证据路径在允许清单内，行号均在对应文件范围内；结构化JSON可解析。以上为文档一致性自检，不是行为测试或来源正确性复审。原始发现保留于`findings.json`，本报告不替总审决定修订或关闭。
