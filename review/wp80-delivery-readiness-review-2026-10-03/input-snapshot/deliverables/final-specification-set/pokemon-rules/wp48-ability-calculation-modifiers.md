# 特性参与计算、免疫与有效性（净化正文；批次 7）

分类：Pokémon Rules／Combat Requirements。本文件给出特性身份/有效性和消费者分层，速度/重量/优先级，类型/命中/会心，普通伤害修正，状态/阶级/招式/换出与逃跑资格的已述 27 族计算/资格/免疫/有效性合同、具体修正参数、直接消费者门和计算副作用。全部内容为只读静态文本与独立算术；**无运行确认**（见 `../scope-statement.md`）。

## 1. 目的与边界

A 为能力身份/有效性和消费者分层，B 为速度/重量/优先级，C 为类型/命中/会心，D 为普通伤害修正，E 为状态/阶级/招式/换出与逃跑资格。每个登记身份在 §9 追溯到下文具体合同；表中的标识仅作数据身份，不提出未来 API 或类结构。回合事件与能力获得/失去等由阶段触发规格负责，基础公式《战斗类型、命中与伤害计算》、状态与阶级中央入口《异常状态、能力阶级与免疫》、场域规格保持唯一主规则。

玩家可看到能力提示、免疫/行动失败、速度先后和 HP/阶级变化；显示关闭不总等于纯查询，必须看 §7 的具名入口。注册缺项本身不证明该能力无效果：核心直接检查见 §8。完整招式、物品、形态、Shadow、AI、设施、demo/宿主与阶段出口仍具名前向，不声称这些域已完成。

## 2. 输入、有效性与读取约定

输入包括当前场上能力身份、存活/胃液/中和气体、使用者 U/目标 T/能力拥有者 B、双方存活盟友集合、当前天气/场地、阶段值、招式实际类型与分类/标记、HP 与上限、性别/物种/形态、选择记录、世代配置和固定随机抽取。持久个体能力与场上能力可能不同，查询以该入口传入的场上身份为准。数据身份由《内容身份、注册与 schema》/个体规格承接；本快照每场上对象是一个当前能力字段，不推导任意多能力列表。

普通有效性拒绝濒死（显式允许濒死的调用除外）、胃液及场上有效中和气体压制。查询中和气体自身以及中和气体拥有者有防递归的专门分支；普通有效性本身不检查是否有非空能力身份，具体能力匹配还必须核身份。查全局能力以存活场上成员和实际有效性为门。不可失去/不可获得名单用于能力变化入口，不代表每个普通查询都可忽略压制。获得/失去名单与调用例外由阶段触发规格展开。

返回式计算若未提供结果，保留传入速度倍率/重量/类型/优先级/会心级；资格式未提供结果默认为假。同一登记复制到别名意味着在**该族**共享合同，不意味着其所有生命周期都相同。命中/伤害处理器修改计算参数而不是以返回真假表示是否生效。不存在登记时只是该入口中性，不能推出整个能力无效果。

| 消费位置 | 谁必须普通有效 | 模式破坏者门/其它例外 |
| --- | --- | --- |
| 速度、类型、优先级、使用者命中/会心/伤害 | U/速度拥有者 | 这些位置不统一受模式破坏者关闭 |
| 重量 | 被查询者 | 模式破坏者真时跳能力层，物品层仍继续 |
| 命中盟友 | 各 U 盟友 | 不受目标能力忽略门；按集合逐个叠加 |
| 命中目标、会心目标、普通伤害目标 | T | 模式破坏者真时跳过 |
| 伤害 U 盟友/T 盟友 | 各相应盟友 | 两侧盟友伤害入口都受模式破坏者门，包括 U 方有益效果 |
| 不可忽略伤害目标 | T | 不受模式破坏者，但仍要普通有效；不可忽略不等于不可压制 |
| 视为异常、不可忽略状态免疫 | 不先套普通有效查询 | COMATOSE 等按传入身份/物种/形态；中央状态入口其它前门仍适用 |
| 普通状态免疫/盟友状态免疫 | T/盟友 B | 自施或模式破坏者假时检查；不可忽略状态免疫先检查 |
| 普通/不可忽略防降阶 | T | 非自降才到这层；两族都要有效，只有普通族受模式破坏者；盟友层也受该门 |
| 招式免疫 | T | 普通免疫消费者受模式破坏者；显示开关另影响提交，见 §7 |
| 全招式阻止 | 扫描到的 B | 真实调用没有模式破坏者门；按速度序找到首个阻止者短路 |
| 换出/逃跑资格 | 相应 B | 按换人规格入口的存活、幽灵、必走、束缚和战斗种类前门；不添加统一忽略门 |

有效天气按场域规格局部查询，晴包含通常晴/大日照，雨包含通常雨/大雨，冰雹不替换为现代雪规则。正值整数的「整除」向下取整。最终计算和夹限使用《战斗类型、命中与伤害计算》/命令规格已有规则，表内倍率不自行提前取整。

## 3. 速度、重量与行动顺序

| 计算/审计身份 | 条件与具体结果 |
| --- | --- |
| 速度 CHLOROPHYLL／SWIFTSWIM／SANDRUSH／SLUSHRUSH | 分别有效晴/雨/沙暴/冰雹时速度倍率 ×2 |
| 速度 QUICKFEET | 视为有任意异常时 ×1.5；核心实际麻痹减速另在该能力有效时免除，不只是覆盖麻痹倍率 |
| 速度 SLOWSTART | 慢启动计数 >0 时 ÷2；计数建立/递减归阶段触发规格 |
| 速度 SURGESURFER | 当前电场时 ×2，不加接地门 |
| 速度 UNBURDEN | 轻装标记真且当前无物品时 ×2；仅无物品不足，重新持物可令本条件失败 |
| 重量 HEAVYMETAL／LIGHTMETAL | 前者 ×2；后者整除 2 且最少 1。先用个体重量（无个体默认 500）加临时重量变化并夹到至少 1，再能力，再物品，最终至少 1；单位沿数据重量，不引入新单位换算 |
| 优先级 GALEWINGS | 原始招式类型为飞行且（世代 ≤6 或满 HP）时＋1；这里不借后续实际类型转换重判 |
| 优先级 PRANKSTER | 变化招＋1，同时写恶作剧之心标记真；反复计算不是纯读取，清标记由别处负责 |
| 优先级 TRIAGE | 治疗标记招＋3 |
| 档内 QUICKDRAW | 全量排序时抽 0..99<30 输出＋1，否则 0；不是实际命中时才抽 |
| 档内 STALL | 输出 −1，无抽取 |

速度基底先按速度阶级整数计算，再乘能力/物品/顺风/湿地/麻痹/徽章倍率，最后四舍五入且最少 1；濒死查询直接 1，绕能力。顺风 ×2、湿地 ÷2，麻痹当前世代 ÷2（旧世代 ÷4），玩家内部徽章门满足时 ×1.1。完整排序、同速随机、戏法空间、物品档覆盖见命令规格；局部重算更新速度和招式优先级，不重抽 QUICKDRAW 等档内项。UseMove 或 Shift 才参与初始档内计算，Shift 无普通招式优先级加成。档效果实际采用时的 QUICKDRAW 消息归阶段触发规格，不能把输出＋1 写成一定先于更高优先级行动。

## 4. 本次类型、命中与会心

### 4.1 类型

进入本次类型计算时强化标记先清；AERILATE／GALVANIZE／PIXILATE／REFRIGERATE 仅将一般分别改飞行/电/妖精/冰，要求目的类型数据存在，并置强化标记。NORMALIZE 要求一般类型存在，改一般；世代 ≥7 才置强化标记。LIQUIDVOICE 要求水类型存在且声音招，改水，不设置该强化。表中无条件满足则保留当前传入类型。

强化标记到伤害 U 能力层才产生威力 ×1.2，四皮/NORMALIZE 共享此量值；这里没有世代 ≤6 改成 ×1.3 的分支。之后等离子浴/输电等可能再改类型、清强化，顺序沿《战斗类型、命中与伤害计算》§3.1。属性特殊招式的前后覆盖归其具名招式域，不能保证所有招式都走相同类型入口。

### 4.2 命中参数

记 q 为基底命中、a/e 为使用者命中/目标闪避阶级、ma/me 为两倍率。调用次序 U → 逐 U 盟友 → T → 物品 → 核心覆盖；下表改变这些输入，普通最终判定/取整引用《战斗类型、命中与伤害计算》§4.2：命中与闪避百分数分别四舍五入成整数后，通常的整数 q 参与最终整数除法；抽取须严格小于该整数阈值，不把未取整数商的比值直接用于比较。

| 位置/审计身份 | 修改 |
| --- | --- |
| U COMPOUNDEYES | ma ×1.3 |
| U HUSTLE | 物理招 ma ×0.8 |
| U KEENEYE | 世代 ≥6 且 e>0，覆盖 e=0；负 e 不改 |
| U NOGUARD | q=0，普通计算中是必中哨兵 |
| U UNAWARE | 伤害招 e=0，包括原负阶级 |
| U VICTORYSTAR／各 U 盟友 VICTORYSTAR | 每个入口 ma ×1.1，可叠加 |
| T LIGHTNINGROD／STORMDRAIN | 分别电/水实际类型时 q=0；普通招式免疫还可能在更早阻挡 |
| T NOGUARD | q=0，但 T 层可被模式破坏者跳过 |
| T SANDVEIL／SNOWCLOAK | T 有效沙暴/冰雹时 me ×1.25 |
| T TANGLEDFEET | T 混乱计数 >0 时 ma ÷2，不是覆盖闪避阶级 |
| T UNAWARE | 伤害招 a=0，包括原负阶级 |
| T WONDERSKIN | 对侧 U 的变化招且 q>50 时 q=50；同侧、q≤50 或 q=0 不改 |

无防守在成功检查还参与半无敌例外，那与本表命中入口分开。已关闭 N01：目标无防守＋模式破坏者真，允许越过相应半无敌门不等于最后必中；继续按 skip 标志或具体命中入口走，普通 q70 仍可在 r70 失败。特殊必中、OHKO、多击等并不自动套全部普通表。

### 4.3 会心

U MERCILESS 对视为中毒的 T 把会心级覆盖为 99；SUPERLUCK＋1。T BATTLEARMOR／SHELLARMOR 把级设 −1。先幸运咒语硬拒，再 U 能力，再 T 能力（可忽略），再双方物品；级 <0 拒绝，之后才招式覆盖/级 >50 保证/其它加级和随机。因此毒目标也能被防会心能力阻止；模式破坏者开时 T 门跳过。倍率/世代会心概率表、亲密追加和是否应用阶级归《战斗类型、命中与伤害计算》§5，不从 99 推导新概率公式。

## 5. 伤害倍率合同

记 P＝威力倍率、A＝选定攻击倍率、D＝选定防御倍率、F＝最终倍率。下面每个身份仅改变所写槽，未写槽保持。先全局气场，再 U，再模式破坏者门内的 U 盟友与 T 普通，再 T 不可忽略，再门内 T 盟友，再物品和核心后置项。所有表内条件均在调用时读取；多盟友每个各乘一次。最后 P/A/D 各作用于对应已定输入并四舍五入、最少 1，公式中分段向下取整、加 2，最后 F 作用并四舍五入最少 1（《战斗类型、命中与伤害计算》§6）。不同槽相同倍率一般不能交换，尤其加 2 与舍入边界。

### 5.1 使用者

| 审计身份 | 条件 | 槽与量值 |
| --- | --- | --- |
| AERILATE／GALVANIZE／NORMALIZE／PIXILATE／REFRIGERATE | 本次强化标记真 | P ×1.2 |
| ANALYTIC | 「最后行动」查询为真：没有其它存活且选择 UseMove/Shift、尚未行动者；不追忆早前倒下者原排序 | P ×1.3 |
| BLAZE／OVERGROW／SWARM／TORRENT | HP ≤ 总 HP 整除 3，实际类型分别火/草/虫/水 | A ×1.5 |
| DEFEATIST | HP ≤ 总 HP 整除 2 | A ÷2，物理/特殊均可 |
| DRAGONSMAW／TRANSISTOR／STEELWORKER | 分别龙/电/钢类型 | A ×1.5 |
| FLAREBOOST | 视为灼伤且特殊招 | P ×1.5 |
| FLASHFIRE | 引火强化标记真且火类型 | A ×1.5 |
| FLOWERGIFT | 物理招且 U 有效晴 | A ×1.5 |
| GORILLATACTICS／HUSTLE | 物理招 | A ×1.5；锁招/命中副作用各归自身入口 |
| GUTS | 视为任意异常且物理招 | A ×1.5；核心灼伤减伤有效性另见 §8 |
| HUGEPOWER／PUREPOWER | 物理招 | A ×2 |
| IRONFIST | 拳标记 | P ×1.2 |
| MEGALAUNCHER | 波动标记 | P ×1.5 |
| MINUS／PLUS | 特殊招且至少一个存活盟友有有效 MINUS 或 PLUS | A ×1.5；多个合格盟友也只在本 U 入口乘一次 |
| NEUROFORCE | 已计算相性为克制 | F ×1.25 |
| PUNKROCK | 声音招 | A ×1.3 |
| RECKLESS | 反作用标记招 | P ×1.2 |
| RIVALRY | 双方性别均非无性别 | 同性 P ×1.25，异性 P ×0.75；任一无性别不改 |
| SANDFORCE | U 有效沙暴且岩/地/钢类型 | P ×1.3 |
| SHEERFORCE | 招式附效概率数据 >0 | P ×1.3；不要求本次抽到附效 |
| SLOWSTART | 计数 >0 且物理招 | A ÷2 |
| SNIPER | 当前击会心真 | F ×1.5，在会心基础倍率之外 |
| SOLARPOWER | 特殊招且 U 有效晴 | A ×1.5 |
| STAKEOUT | T 当时的选择种类仍是 SwitchOut | A ×2；不概括所有本轮曾换入者 |
| STEELYSPIRIT | 钢类型 | F ×1.5 |
| STRONGJAW | 咬标记 | P ×1.5 |
| TECHNICIAN | 非自身、招式存在且非挣扎，当时输入威力乘已累积 P ≤60 | P ×1.5；读取全局气场后的 P，早于帮助等后置倍率 |
| TINTEDLENS | 已计算相性为抵抗 | F ×2；不把免疫前门重新变成可命中 |
| TOUGHCLAWS | 原始接触标记真 | P ×4/3；不是 ×1.3，也不是已考虑 LONGREACH 的实际接触查询 |
| TOXICBOOST | 视为中毒且物理招 | P ×1.5 |
| WATERBUBBLE | 水类型 | A ×2 |

### 5.2 盟友、目标与不可忽略项

| 位置/审计身份 | 条件与具体改动 |
| --- | --- |
| U 盟友 BATTERY | 特殊招 F ×1.3 |
| U 盟友 FLOWERGIFT | 物理招且 **U** 有效晴，A ×1.5 |
| U 盟友 POWERSPOT | F ×1.3，无招式分类门 |
| U 盟友 STEELYSPIRIT | 钢类型 F ×1.5 |
| T DRYSKIN | 火类型 P ×1.25 |
| T FILTER／SOLIDROCK | 克制 F ×0.75 |
| T FLOWERGIFT | 特殊招且 **T** 有效晴，D ×1.5 |
| T FLUFFY | 本次类型火则 F ×2；同时若实际接触则 F ÷2，两条件独立，可相抵。实际接触考虑 LONGREACH，不是 TOUGHCLAWS 的原始标记门 |
| T FURCOAT | 物理招或使用目标防御替代特防的特殊效果，D ×2 |
| T GRASSPELT | 当前青草场地 D ×1.5，无物理/接地附加门 |
| T HEATPROOF | 火类型 P ÷2 |
| T ICESCALES | 特殊招 F ÷2 |
| T MARVELSCALE | T 视为任意异常且物理招，D ×1.5 |
| T MULTISCALE | T 满 HP 时 F ÷2 |
| T PUNKROCK | 声音招 F ÷2 |
| T THICKFAT | 火/冰类型 P ÷2 |
| T WATERBUBBLE | 火类型 F ÷2 |
| T 不可忽略 PRISMARMOR | 克制 F ×0.75，仍要求 T 普通有效 |
| T 不可忽略 SHADOWSHIELD | T 满 HP 时 F ÷2，仍要求 T 普通有效 |
| T 盟友 FLOWERGIFT | 特殊招且 T 有效晴，D ×1.5 |
| T 盟友 FRIENDGUARD | F ×0.75，无额外招式分类门 |

## 6. 状态与阶级资格

「视为」不修改真实持久状态。COMATOSE 只对 KOMALA：询问任意异常或睡眠时真；其它状态查真实值。它的不可忽略状态免疫对该物种拒所有新异常；SHIELDSDOWN 只对 MINIOR 且形态 <7 拒所有新异常。此两个入口不先套普通能力有效性，不推论可被普通治疗改掉「视为睡眠」。

普通自身状态免疫：FLOWERVEIL 保护草类型免全部；IMMUNITY／PASTELVEIL 免毒；INSOMNIA／SWEETVEIL／VITALSPIRIT 免睡；LEAFGUARD 在自身有效晴免全部；LIMBER 免麻痹；MAGMAARMOR 免冰冻；WATERVEIL／WATERBUBBLE 免灼伤。盟友拥有 FLOWERVEIL 时保护**被施加者为草**者免全部，PASTELVEIL 免毒，SWEETVEIL 免睡；不要求盟友与目标共享物种或类型。中央入口早先已有存活、同状态/已有状态、替身、地形、类型等门，入睡、剧毒、同步等入口差异沿《异常状态、能力阶级与免疫》§3，不能用本表替代全部资格。

普通防降：BIGPECKS 防防御降，HYPERCUTTER 防攻击降，KEENEYE 防命中降；CLEARBODY／WHITESMOKE 防所有降；FLOWERVEIL 自身草类型防所有降。不可忽略 FULLMETALBODY 防所有降，但仍需有效。盟友 FLOWERVEIL 保护被降者草类型；拥有者不用也是草。中央自降不套这些防降；消息真时展示拥有者能力并给拒绝说明，消息假只返回资格拒绝。中央反向、单纯、镜甲与多项招式预检遵守《异常状态、能力阶级与免疫》§5 及 K 合同，尤其模式破坏者开也不自动删除多项招式自己的镜甲预检，不能由本表推出所有招式都准入。

## 7. 招式阻止、免疫、换出与逃跑

DAZZLING／QUEENLYMAJESTY：B 与 U 对立、U 已保存优先级 >0、目标集合中存在与 U 对立者，则阻止整次使用。B 不必就是单独目标；目标集为空时不成立。调用位于压力等 PP 处理之后，失败展示、标失败、取消招式并结束行动，不返此前 PP；不补造模式破坏者绕过。

| 免疫身份 | 匹配条件/副作用 |
| --- | --- |
| BULLETPROOF | 炮弹标记招免疫；无自身排除 |
| SOUNDPROOF | 声音招免疫；世代 ≥8 排除对自己，旧世代没有这一排除 |
| TELEPATHY | 非变化、非自己、非对侧 U（同侧其它使用者）免疫 |
| WONDERGUARD | 伤害招、类型非空且已算相性不是克制，则免疫；变化/无类型不由本项免疫 |
| FLASHFIRE | 非自身火类型免疫；显示真且标记尚假时置强化真，显示假不置标记；已强化依然免疫 |
| LIGHTNINGROD／MOTORDRIVE／SAPSIPPER／STORMDRAIN | 非自身，分别电/电/草/水类型免疫。显示真时经中央可升检查分别特攻＋1/速度＋1/攻击＋1/特攻＋1；已封顶仍免疫，显示假不升 |
| VOLTABSORB／WATERABSORB／DRYSKIN | 非自身，电/水/水类型免疫。显示真且可恢复时请求总 HP 整除 4，经中央恢复夹限；显示假不回血，满 HP/禁恢复仍可免疫 |

可见分支会显示拥有者与免疫/强化/恢复反馈，显示隐藏不改变返回免疫真，但上表明确的强化/升阶/恢复确会随它关闭。其它资格式免疫只产生所述消息，不消费能力或物品。后续招式特殊目标挑选可以静默调用，不能把这些预查询写成已经应用吸收奖励。

换出保证族 CertainSwitching 本快照**无登记**。TrappingByTarget：ARENATRAP 对非浮空候选真；MAGNETPULL 对钢类型真；SHADOWTAG 对候选没有有效同能力时真。它们只提供阻止资格，不执行换人，也不替代换人规格的仅换入/组合检查/界面/登记/执行分层。逃跑保证 RUNAWAY 返回真，真实调用仍先拒训练家战、玩家不可逃设置；幽灵特例、道具、局部束缚和实际速度逃跑分支按换人规格。RUNAWAY 不是换出保证，不把逃跑处理器投射到替补选择。

## 8. 注册表外核心与共享责任

以下直接分支已由主规格或本文件消费者确认，不能从登记集合中删掉：

| 直接规则 | 唯一主规则与本文件接点 |
| --- | --- |
| DARKAURA／FAIRYAURA／AURABREAK | 《战斗类型、命中与伤害计算》§6.3：匹配暗/妖精的全局气场在本表前使 P ×4/3，有破坏者改 ×3/4，不因多个同气场重复乘 |
| UNAWARE 攻防阶级、ADAPTABILITY 本系、GUTS 灼伤、INFILTRATOR 屏障、SCRAPPY／LEVITATE 等类型资格 | 《战斗类型、命中与伤害计算》§3/§6/§7；本表只补对应登记项，核心相性/伤害规则不另造 |
| SHEERFORCE／SHIELDDUST／SERENEGRACE、INNERFOCUS、STENCH | 《战斗类型、命中与伤害计算》§7、《异常状态、能力阶级与免疫》/命令规格：附效/畏缩入口及概率，不从威力增幅断言所有后段回调关闭 |
| PRESSURE、PRANKSTER 暗系门、STICKYHOLD／OVERCOAT 等具体交界 | 命令规格/《异常状态、能力阶级与免疫》既有成功/PP 规则；具体物品转移、粉末和未展开招式全集仍归《多次攻击、特殊伤害与恢复》/招式变更/《持有物计算、触发与消耗》；本文件不自批其余规则 |
| DISGUISE／ICEFACE、DAMP、PROTEAN／LIBERO、PARENTALBOND、MAGICBOUNCE、MOLDBREAKER／TERAVOLT／TURBOBLAZE | 命令/《战斗类型、命中与伤害计算》已有前门与阶段；生命周期/受击直接分支见阶段触发规格，完整形态与招式域见《Mega、Primal 与显式还原》/《多次攻击、特殊伤害与恢复》/招式变更规格。没有把这些当未登记＝无效果 |
| MAGICGUARD、AIRLOCK／CLOUDNINE、雨/晴强天气等 | 《异常状态、能力阶级与免疫》/场域规格、战斗结果主阶段与阶段触发规格；§2 的有效天气是其结果输入 |

能力数据提供身份、名称、说明、标志；说明文字不是行为证明。普通缺失登记回退依《通知、扩展与插件》/《内容身份、注册与 schema》的有限调用语义；插件注入和无效数据组合没有运行验证。当前世代 8、更多类型效果开、速度中途重排开、亲密效果关。替代世代只按正文实际分支保留，不声称完整历代兼容。

## 9. 有界登记覆盖（27 族，148 展开身份）

文本集合：27 族，133 直接登记＋11 复制语句，复制展开后 148 个（族，能力）身份；CertainSwitching 为空，其余 26 族有登记。复制行首项是来源，其余才为新增身份。具体量值与分支必须连同前文合同阅读，不以有名字替代行为。

| 族 | 审计身份（add/copy 方向） | 合同 |
| --- | --- | --- |
| SpeedCalc（8） | CHLOROPHYLL、QUICKFEET、SANDRUSH、SLOWSTART、SLUSHRUSH、SURGESURFER、SWIFTSWIM、UNBURDEN | §3 |
| WeightCalc（2） | HEAVYMETAL、LIGHTMETAL | §3 |
| StatusCheckNonIgnorable（1） | COMATOSE | §6 |
| StatusImmunity（8） | FLOWERVEIL；IMMUNITY→PASTELVEIL；INSOMNIA→SWEETVEIL、VITALSPIRIT；LEAFGUARD；LIMBER；MAGMAARMOR；WATERVEIL→WATERBUBBLE | §6 |
| StatusImmunityNonIgnorable（2） | COMATOSE、SHIELDSDOWN | §6 |
| StatusImmunityFromAlly（3） | FLOWERVEIL、PASTELVEIL、SWEETVEIL | §6 |
| StatLossImmunity（6） | BIGPECKS；CLEARBODY→WHITESMOKE；FLOWERVEIL；HYPERCUTTER；KEENEYE | §6 |
| StatLossImmunityNonIgnorable（1） | FULLMETALBODY | §6 |
| StatLossImmunityFromAlly（1） | FLOWERVEIL | §6 |
| PriorityChange（3） | GALEWINGS、PRANKSTER、TRIAGE | §3 |
| PriorityBracketChange（2） | QUICKDRAW、STALL | §3 |
| MoveBlocking（2） | DAZZLING→QUEENLYMAJESTY | §7 |
| MoveImmunity（12） | BULLETPROOF、FLASHFIRE、LIGHTNINGROD、MOTORDRIVE、SAPSIPPER、SOUNDPROOF、STORMDRAIN、TELEPATHY、VOLTABSORB；WATERABSORB→DRYSKIN；WONDERGUARD | §7 |
| ModifyMoveBaseType（6） | AERILATE、GALVANIZE、LIQUIDVOICE、NORMALIZE、PIXILATE、REFRIGERATE | §4.1 |
| AccuracyCalcFromUser（6） | COMPOUNDEYES、HUSTLE、KEENEYE、NOGUARD、UNAWARE、VICTORYSTAR | §4.2 |
| AccuracyCalcFromAlly（1） | VICTORYSTAR | §4.2 |
| AccuracyCalcFromTarget（8） | LIGHTNINGROD、NOGUARD、SANDVEIL、SNOWCLOAK、STORMDRAIN、TANGLEDFEET、UNAWARE、WONDERSKIN | §4.2 |
| DamageCalcFromUser（41） | AERILATE→GALVANIZE、NORMALIZE、PIXILATE、REFRIGERATE；ANALYTIC、BLAZE、DEFEATIST、DRAGONSMAW、FLAREBOOST、FLASHFIRE、FLOWERGIFT、GORILLATACTICS、GUTS；HUGEPOWER→PUREPOWER；HUSTLE、IRONFIST、MEGALAUNCHER；MINUS→PLUS；NEUROFORCE、OVERGROW、PUNKROCK、RECKLESS、RIVALRY、SANDFORCE、SHEERFORCE、SLOWSTART、SNIPER、SOLARPOWER、STAKEOUT、STEELWORKER、STEELYSPIRIT、STRONGJAW、SWARM、TECHNICIAN、TINTEDLENS、TORRENT、TOUGHCLAWS、TOXICBOOST、TRANSISTOR、WATERBUBBLE | §5.1 |
| DamageCalcFromAlly（4） | BATTERY、FLOWERGIFT、POWERSPOT、STEELYSPIRIT | §5.2 |
| DamageCalcFromTarget（15） | DRYSKIN；FILTER→SOLIDROCK；FLOWERGIFT、FLUFFY、FURCOAT、GRASSPELT、HEATPROOF、ICESCALES、MARVELSCALE、MULTISCALE、PUNKROCK、THICKFAT、WATERBUBBLE | §5.2 |
| DamageCalcFromTargetNonIgnorable（2） | PRISMARMOR、SHADOWSHIELD | §5.2 |
| DamageCalcFromTargetAlly（2） | FLOWERGIFT、FRIENDGUARD | §5.2 |
| CriticalCalcFromUser（2） | MERCILESS、SUPERLUCK | §4.3 |
| CriticalCalcFromTarget（2） | BATTLEARMOR→SHELLARMOR | §4.3 |
| TrappingByTarget（3） | ARENATRAP、MAGNETPULL、SHADOWTAG | §7 |
| CertainEscapeFromBattle（1） | RUNAWAY | §7 |

## 10. 示例场景与测试目录

独立静态向量（基础普通伤害共同前提：《战斗类型、命中与伤害计算》§6 同公式，等级 50、威力 60、攻 100、防 100、单目标、中性相性、非会心、无本系/天气/灼伤/道具，随机取最大（×1），基础整数伤害 28；以下只改变所列变量；输入能力均有效，除非明确压制/模式破坏者；没有执行参考或其转译模型）见测试目录 [`../test-catalog/pokemon-rules-wp43-44-46-48-50.md`](../test-catalog/pokemon-rules-wp43-44-46-48-50.md) 的 AB01–AB23（QUICKFEET 麻痹免除与胃液对照、LIGHTMETAL、SURGESURFER、QUICKDRAW 不重抽、N01 反例、VICTORYSTAR 叠加整数阈值、WONDERSKIN 与 NOGUARD 次序、HUGEPOWER/TOUGHCLAWS 中间值、GRASSPELT 浮空、FLUFFY 两条件、STEELYSPIRIT 盟友叠乘、SHADOWSHIELD 压制、TECHNICIAN 气场门、MERCILESS vs BATTLEARMOR 三层、LIGHTNINGROD 静默/可见、WATERABSORB 显示差异、COMATOSE 胃液、FULLMETALBODY 胃液、DAZZLING 阻止与空目标集、AERILATE 目的类型不存在、水免疫禁回复、RUNAWAY 训练家门）。

## 11. 失败、不变量、依赖与未决

不满足表内门则本入口保持输入或返回假；其它核心规则可能仍改变最终行为。倍率容器已改与命中/伤害真的提交不同；成功检查后再失败不会自动返 PP。显示假对吸收奖励的差异必须保留。参数、顺序、舍入与主规则冲突时按具名入口回源，不以官方常识修正快照。

- 完成依赖：基础公式（《战斗类型、命中与伤害计算》）；状态/阶级中央（《异常状态、能力阶级与免疫》及其覆盖附表）；场域（场域规格）；命令（命令规格）——均已限定通过。
- 前向：阶段触发规格承接本目录余 21 族、状态/形态/入离场触发，批末核对本文件门与阶段；《持有物计算、触发与消耗》承接所有物品具体修正/转移，本文件只保留其调用位置；《Mega、Primal 与显式还原》/Shadow 规格承接完整变身/Shadow；《多次攻击、特殊伤害与恢复》/招式变更规格承接特殊招式全集，若出现改写 q、P/A/D/F 或有效性入口需复核 §2–§8；AI/设施规格、demo 与 U01–U10、出口不关闭。当前没有以待运行掩盖本文件静态参数缺口，真实显示、插件组合和随机运行验证仍未做。
