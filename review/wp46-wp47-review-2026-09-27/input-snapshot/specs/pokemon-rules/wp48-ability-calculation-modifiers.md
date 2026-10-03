# WP48 — 特性参与计算、免疫与有效性

状态：**Reviewed（限定静态范围，2026-09-27 v2有限复审PASS_SCOPED；管理性回填）**。日期2026-09-27。Feature：F12-06计算子范围；分类：Pokémon Rules／Combat Requirements。证据为固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的只读静态文本与独立算术，未运行参考。

被审首稿v1：`480016af9731a97607300ae84851b6b6286ae624b1452a0193b849295f2b3728`（34,233字节）保留历史；被审v2 `87e39127e14eddd10f6e0d10e6d63999e0cb9ff70fa0e2505dc97a195f3b3bb8`（35,021字节）经[独立闭合报告](../../review/wp42-wp48-wp49-recheck-2026-09-27/report.md)限定通过，WP48-R01 CLOSED。本稿仅状态回填，新字节不冒充被审版；批准范围：A～E已述27族计算／资格／免疫／有效性、具体修正参数、直接消费者门和计算副作用；148展开身份有界合同。

## 1. 目的与边界

A为能力身份／有效性和消费者分层，B为速度／重量／优先级，C为类型／命中／会心，D为普通伤害修正，E为状态／阶级／招式／换出与逃跑资格。每个登记身份在§12追溯到下文具体合同；表中的英文标识仅作审计身份，不提出未来API或类结构。回合事件与能力获得／失去等由本批WP49负责，基础公式WP43、状态与阶级中央入口WP44、场域WP45保持唯一主规则。

玩家可看到能力提示、免疫／行动失败、速度先后和HP／阶级变化；显示关闭不总等于纯查询，必须看§7的具名入口。注册缺项本身不证明该能力无效果：核心直接检查见§8。完整招式、物品、形态、Shadow、AI、设施、Demo／宿主与阶段出口仍具名前向，不声称这些域已完成。

## 2. 输入、有效性与读取约定（A）

输入包括当前场上能力身份、存活／胃液／中和气体、使用者U／目标T／能力拥有者B、双方存活盟友集合、当前天气／场地、阶段值、招式实际类型与分类／标记、HP与上限、性别／物种／形态、选择记录、世代配置和固定随机抽取。持久个体能力与场上能力可能不同，查询以该入口传入的场上身份为准。数据身份由WP03／18承接；本快照每场上对象是一个当前能力字段，不推导任意多能力列表。

普通有效性拒绝濒死（显式允许濒死的调用除外）、胃液及场上有效中和气体压制。查询中和气体自身以及中和气体拥有者有防递归的专门分支；普通有效性本身不检查是否有非空能力身份，具体能力匹配还必须核身份。查全局能力以存活场上成员和实际有效性为门。不可失去／不可获得名单用于能力变化入口，不代表每个普通查询都可忽略压制。获得／失去名单与调用例外由WP49展开。

返回式计算若未提供结果，保留传入速度倍率／重量／类型／优先级／会心级；资格式未提供结果默认为假。同一登记复制到别名意味着在**该族**共享合同，不意味着其所有生命周期都相同。命中／伤害处理器修改计算参数而不是以返回真假表示是否生效。不存在登记时只是该入口中性，不能推出整个能力无效果。

| 消费位置 | 谁必须普通有效 | 模式破坏者门／其它例外 |
| --- | --- | --- |
| 速度、类型、优先级、使用者命中／会心／伤害 | U／速度拥有者 | 这些位置不统一受模式破坏者关闭 |
| 重量 | 被查询者 | 模式破坏者真时跳能力层，物品层仍继续 |
| 命中盟友 | 各U盟友 | 不受目标能力忽略门；按集合逐个叠加 |
| 命中目标、会心目标、普通伤害目标 | T | 模式破坏者真时跳过 |
| 伤害U盟友／T盟友 | 各相应盟友 | 两侧盟友伤害入口都受模式破坏者门，包括U方有益效果 |
| 不可忽略伤害目标 | T | 不受模式破坏者，但仍要普通有效；不可忽略不等于不可压制 |
| 视为异常、不可忽略状态免疫 | 不先套普通有效查询 | COMATOSE等按传入身份／物种／形态；中央状态入口其它前门仍适用 |
| 普通状态免疫／盟友状态免疫 | T／盟友B | 自施或模式破坏者假时检查；不可忽略状态免疫先检查 |
| 普通／不可忽略防降阶 | T | 非自降才到这层；两族都要有效，只有普通族受模式破坏者；盟友层也受该门 |
| 招式免疫 | T | 普通免疫消费者受模式破坏者；显示开关另影响提交，见§7 |
| 全招式阻止 | 扫描到的B | 真实调用没有模式破坏者门；按速度序找到首个阻止者短路 |
| 换出／逃跑资格 | 相应B | 按WP41入口的存活、幽灵、必走、束缚和战斗种类前门；不添加统一忽略门 |

有效天气按WP45局部查询，晴包含通常晴／大日照，雨包含通常雨／大雨，冰雹不替换为现代雪规则。正值整数的“整除”向下取整。最终计算和夹限使用WP43／WP40已有规则，表内倍率不自行提前取整。

## 3. 速度、重量与行动顺序（B）

| 计算／审计身份 | 条件与具体结果 |
| --- | --- |
| 速度 CHLOROPHYLL／SWIFTSWIM／SANDRUSH／SLUSHRUSH | 分别有效晴／雨／沙暴／冰雹时速度倍率×2 |
| 速度 QUICKFEET | 视为有任意异常时×1.5；核心实际麻痹减速另在该能力有效时免除，不只是覆盖麻痹倍率 |
| 速度 SLOWSTART | 慢启动计数>0时÷2；计数建立／递减归WP49 |
| 速度 SURGESURFER | 当前电场时×2，不加接地门 |
| 速度 UNBURDEN | 轻装标记真且当前无物品时×2；仅无物品不足，重新持物可令本条件失败 |
| 重量 HEAVYMETAL／LIGHTMETAL | 前者×2；后者整除2且最少1。先用个体重量（无个体默认500）加临时重量变化并夹到至少1，再能力，再物品，最终至少1；单位沿数据重量，不引入新单位换算 |
| 优先级 GALEWINGS | 原始招式类型为飞行且（世代≤6或满HP）时＋1；这里不借后续实际类型转换重判 |
| 优先级 PRANKSTER | 变化招＋1，同时写恶作剧之心标记真；反复计算不是纯读取，清标记由别处负责 |
| 优先级 TRIAGE | 治疗标记招＋3 |
| 档内 QUICKDRAW | 全量排序时抽0..99<30输出＋1，否则0；不是实际命中时才抽 |
| 档内 STALL | 输出−1，无抽取 |

速度基底先按速度阶级整数计算，再乘能力／物品／顺风／湿地／麻痹／徽章倍率，最后四舍五入且最少1；濒死查询直接1，绕能力。顺风×2、湿地÷2，麻痹当前世代÷2（旧世代÷4），玩家内部徽章门满足时×1.1。完整排序、同速随机、戏法空间、物品档覆盖见WP40§6；局部重算更新速度和招式优先级，不重抽QUICKDRAW等档内项。UseMove或Shift才参与初始档内计算，Shift无普通招式优先级加成。档效果实际采用时的QUICKDRAW消息归WP49，不能把输出＋1写成一定先于更高优先级行动。

## 4. 本次类型、命中与会心（C）

### 4.1 类型

进入本次类型计算时强化标记先清；AERILATE／GALVANIZE／PIXILATE／REFRIGERATE仅将一般分别改飞行／电／妖精／冰，要求目的类型数据存在，并置强化标记。NORMALIZE要求一般类型存在，改一般；世代≥7才置强化标记。LIQUIDVOICE要求水类型存在且声音招，改水，不设置该强化。表中无条件满足则保留当前传入类型。

强化标记到伤害U能力层才产生威力×1.2，四皮／NORMALIZE共享此量值；这里没有世代≤6改成×1.3的分支。之后等离子浴／输电等可能再改类型、清强化，顺序沿WP43§3.1。属性特殊招式的前后覆盖归其具名招式域，不能保证所有招式都走相同类型入口。

### 4.2 命中参数

记q为基底命中、a/e为使用者命中／目标闪避阶级、ma/me为两倍率。调用次序U→逐U盟友→T→物品→核心覆盖；下表改变这些输入，普通最终判定／取整引用WP43§4.2：命中与闪避百分数分别四舍五入成整数后，通常的整数q参与最终整数除法；抽取须严格小于该整数阈值，不把未取整数商的比值直接用于比较。

| 位置／审计身份 | 修改 |
| --- | --- |
| U COMPOUNDEYES | ma×1.3 |
| U HUSTLE | 物理招ma×0.8 |
| U KEENEYE | 世代≥6且e>0，覆盖e=0；负e不改 |
| U NOGUARD | q=0，普通计算中是必中哨兵 |
| U UNAWARE | 伤害招e=0，包括原负阶级 |
| U VICTORYSTAR／各U盟友 VICTORYSTAR | 每个入口ma×1.1，可叠加 |
| T LIGHTNINGROD／STORMDRAIN | 分别电／水实际类型时q=0；普通招式免疫还可能在更早阻挡 |
| T NOGUARD | q=0，但T层可被模式破坏者跳过 |
| T SANDVEIL／SNOWCLOAK | T有效沙暴／冰雹时me×1.25 |
| T TANGLEDFEET | T混乱计数>0时ma÷2，不是覆盖闪避阶级 |
| T UNAWARE | 伤害招a=0，包括原负阶级 |
| T WONDERSKIN | 对侧U的变化招且q>50时q=50；同侧、q≤50或q=0不改 |

无防守在成功检查还参与半无敌例外，那与本表命中入口分开。已关闭N01：目标无防守＋模式破坏者真，允许越过相应半无敌门不等于最后必中；继续按skip标志或具体命中入口走，普通q70仍可在r70失败。特殊必中、OHKO、多击等并不自动套全部普通表。

### 4.3 会心

U MERCILESS对视为中毒的T把会心级覆盖为99；SUPERLUCK＋1。T BATTLEARMOR／SHELLARMOR把级设−1。先幸运咒语硬拒，再U能力，再T能力（可忽略），再双方物品；级<0拒绝，之后才招式覆盖／级>50保证／其它加级和随机。因此毒目标也能被防会心能力阻止；模式破坏者开时T门跳过。倍率／世代会心概率表、亲密追加和是否应用阶级归WP43§5，不从99推导新概率公式。

## 5. 伤害倍率合同（D）

记P＝威力倍率、A＝选定攻击倍率、D＝选定防御倍率、F＝最终倍率。下面每个身份仅改变所写槽，未写槽保持。先全局气场，再U，再模式破坏者门内的U盟友与T普通，再T不可忽略，再门内T盟友，再物品和核心后置项。所有表内条件均在调用时读取；多盟友每个各乘一次。最后P/A/D各作用于对应已定输入并四舍五入、最少1，公式中分段向下取整、加2，最后F作用并四舍五入最少1（WP43§6）。不同槽相同倍率一般不能交换，尤其加2与舍入边界。

### 5.1 使用者

| 审计身份 | 条件 | 槽与量值 |
| --- | --- | --- |
| AERILATE／GALVANIZE／NORMALIZE／PIXILATE／REFRIGERATE | 本次强化标记真 | P×1.2 |
| ANALYTIC | “最后行动”查询为真：没有其它存活且选择UseMove／Shift、尚未行动者；不追忆早前倒下者原排序 | P×1.3 |
| BLAZE／OVERGROW／SWARM／TORRENT | HP≤总HP整除3，实际类型分别火／草／虫／水 | A×1.5 |
| DEFEATIST | HP≤总HP整除2 | A÷2，物理／特殊均可 |
| DRAGONSMAW／TRANSISTOR／STEELWORKER | 分别龙／电／钢类型 | A×1.5 |
| FLAREBOOST | 视为灼伤且特殊招 | P×1.5 |
| FLASHFIRE | 引火强化标记真且火类型 | A×1.5 |
| FLOWERGIFT | 物理招且U有效晴 | A×1.5 |
| GORILLATACTICS／HUSTLE | 物理招 | A×1.5；锁招／命中副作用各归自身入口 |
| GUTS | 视为任意异常且物理招 | A×1.5；核心灼伤减伤有效性另见§8 |
| HUGEPOWER／PUREPOWER | 物理招 | A×2 |
| IRONFIST | 拳标记 | P×1.2 |
| MEGALAUNCHER | 波动标记 | P×1.5 |
| MINUS／PLUS | 特殊招且至少一个存活盟友有有效MINUS或PLUS | A×1.5；多个合格盟友也只在本U入口乘一次 |
| NEUROFORCE | 已计算相性为克制 | F×1.25 |
| PUNKROCK | 声音招 | A×1.3 |
| RECKLESS | 反作用标记招 | P×1.2 |
| RIVALRY | 双方性别均非无性别 | 同性P×1.25，异性P×0.75；任一无性别不改 |
| SANDFORCE | U有效沙暴且岩／地／钢类型 | P×1.3 |
| SHEERFORCE | 招式附效概率数据>0 | P×1.3；不要求本次抽到附效 |
| SLOWSTART | 计数>0且物理招 | A÷2 |
| SNIPER | 当前击会心真 | F×1.5，在会心基础倍率之外 |
| SOLARPOWER | 特殊招且U有效晴 | A×1.5 |
| STAKEOUT | T当时的选择种类仍是SwitchOut | A×2；不概括所有本轮曾换入者 |
| STEELYSPIRIT | 钢类型 | F×1.5 |
| STRONGJAW | 咬标记 | P×1.5 |
| TECHNICIAN | 非自身、招式存在且非挣扎，当时输入威力乘已累积P≤60 | P×1.5；读取全局气场后的P，早于帮助等后置倍率 |
| TINTEDLENS | 已计算相性为抵抗 | F×2；不把免疫前门重新变成可命中 |
| TOUGHCLAWS | 原始接触标记真 | P×4/3；不是×1.3，也不是已考虑LONGREACH的实际接触查询 |
| TOXICBOOST | 视为中毒且物理招 | P×1.5 |
| WATERBUBBLE | 水类型 | A×2 |

### 5.2 盟友、目标与不可忽略项

| 位置／审计身份 | 条件与具体改动 |
| --- | --- |
| U盟友 BATTERY | 特殊招F×1.3 |
| U盟友 FLOWERGIFT | 物理招且**U**有效晴，A×1.5 |
| U盟友 POWERSPOT | F×1.3，无招式分类门 |
| U盟友 STEELYSPIRIT | 钢类型F×1.5 |
| T DRYSKIN | 火类型P×1.25 |
| T FILTER／SOLIDROCK | 克制F×0.75 |
| T FLOWERGIFT | 特殊招且**T**有效晴，D×1.5 |
| T FLUFFY | 本次类型火则F×2；同时若实际接触则F÷2，两条件独立，可相抵。实际接触考虑LONGREACH，不是TOUGHCLAWS的原始标记门 |
| T FURCOAT | 物理招或使用目标防御替代特防的特殊效果，D×2 |
| T GRASSPELT | 当前青草场地D×1.5，无物理／接地附加门 |
| T HEATPROOF | 火类型P÷2 |
| T ICESCALES | 特殊招F÷2 |
| T MARVELSCALE | T视为任意异常且物理招，D×1.5 |
| T MULTISCALE | T满HP时F÷2 |
| T PUNKROCK | 声音招F÷2 |
| T THICKFAT | 火／冰类型P÷2 |
| T WATERBUBBLE | 火类型F÷2 |
| T不可忽略 PRISMARMOR | 克制F×0.75，仍要求T普通有效 |
| T不可忽略 SHADOWSHIELD | T满HP时F÷2，仍要求T普通有效 |
| T盟友 FLOWERGIFT | 特殊招且T有效晴，D×1.5 |
| T盟友 FRIENDGUARD | F×0.75，无额外招式分类门 |

## 6. 状态与阶级资格（E）

“视为”不修改真实持久状态。COMATOSE只对KOMALA：询问任意异常或睡眠时真；其它状态查真实值。它的不可忽略状态免疫对该物种拒所有新异常；SHIELDSDOWN只对MINIOR且形态<7拒所有新异常。此两个入口不先套普通能力有效性，不推论可被普通治疗改掉“视为睡眠”。

普通自身状态免疫：FLOWERVEIL保护草类型免全部；IMMUNITY／PASTELVEIL免毒；INSOMNIA／SWEETVEIL／VITALSPIRIT免睡；LEAFGUARD在自身有效晴免全部；LIMBER免麻痹；MAGMAARMOR免冰冻；WATERVEIL／WATERBUBBLE免灼伤。盟友拥有FLOWERVEIL时保护**被施加者为草**者免全部，PASTELVEIL免毒，SWEETVEIL免睡；不要求盟友与目标共享物种或类型。中央入口早先已有存活、同状态／已有状态、替身、地形、类型等门，入睡、剧毒、同步等入口差异沿WP44§3，不能用本表替代全部资格。

普通防降：BIGPECKS防防御降，HYPERCUTTER防攻击降，KEENEYE防命中降；CLEARBODY／WHITESMOKE防所有降；FLOWERVEIL自身草类型防所有降。不可忽略FULLMETALBODY防所有降，但仍需有效。盟友FLOWERVEIL保护被降者草类型；拥有者不用也是草。中央自降不套这些防降；消息真时展示拥有者能力并给拒绝说明，消息假只返回资格拒绝。中央反向、单纯、镜甲与多项招式预检遵守WP44§5及K合同，尤其模式破坏者开也不自动删除多项招式自己的镜甲预检，不能由本表推出所有招式都准入。

## 7. 招式阻止、免疫、换出与逃跑（E）

DAZZLING／QUEENLYMAJESTY：B与U对立、U已保存优先级>0、目标集合中存在与U对立者，则阻止整次使用。B不必就是单独目标；目标集为空时不成立。调用位于压力等PP处理之后，失败展示、标失败、取消招式并结束行动，不返此前PP；不补造模式破坏者绕过。

| 免疫身份 | 匹配条件／副作用 |
| --- | --- |
| BULLETPROOF | 炮弹标记招免疫；无自身排除 |
| SOUNDPROOF | 声音招免疫；世代≥8排除对自己，旧世代没有这一排除 |
| TELEPATHY | 非变化、非自己、非对侧U（同侧其它使用者）免疫 |
| WONDERGUARD | 伤害招、类型非空且已算相性不是克制，则免疫；变化／无类型不由本项免疫 |
| FLASHFIRE | 非自身火类型免疫；显示真且标记尚假时置强化真，显示假不置标记；已强化依然免疫 |
| LIGHTNINGROD／MOTORDRIVE／SAPSIPPER／STORMDRAIN | 非自身，分别电／电／草／水类型免疫。显示真时经中央可升检查分别特攻＋1／速度＋1／攻击＋1／特攻＋1；已封顶仍免疫，显示假不升 |
| VOLTABSORB／WATERABSORB／DRYSKIN | 非自身，电／水／水类型免疫。显示真且可恢复时请求总HP整除4，经中央恢复夹限；显示假不回血，满HP／禁恢复仍可免疫 |

可见分支会显示拥有者与免疫／强化／恢复反馈，显示隐藏不改变返回免疫真，但上表明确的强化／升阶／恢复确会随它关闭。其它资格式免疫只产生所述消息，不消费能力或物品。后续招式特殊目标挑选可以静默调用，不能把这些预查询写成已经应用吸收奖励。

换出保证族CertainSwitching本快照**无登记**。TrappingByTarget：ARENATRAP对非浮空候选真；MAGNETPULL对钢类型真；SHADOWTAG对候选没有有效同能力时真。它们只提供阻止资格，不执行换人，也不替代WP41的仅换入／组合检查／UI／登记／执行分层。逃跑保证RUNAWAY返回真，真实调用仍先拒训练家战、玩家不可逃设置；幽灵特例、道具、局部束缚和实际速度逃跑分支按WP41。RUNAWAY不是换出保证，不把逃跑处理器投射到替补选择。

## 8. 注册表外核心与共享责任

以下直接分支已由主规格或本包消费者确认，不能从§12登记集合中删掉：

| 直接规则 | 唯一主规则与本包接点 |
| --- | --- |
| DARKAURA／FAIRYAURA／AURABREAK | WP43§6.3：匹配暗／妖精的全局气场在本表前使P×4/3，有破坏者改×3/4，不因多个同气场重复乘 |
| UNAWARE攻防阶级、ADAPTABILITY本系、GUTS灼伤、INFILTRATOR屏障、SCRAPPY／LEVITATE等类型资格 | WP43§3／6／7；本表只补对应登记项，核心相性／伤害规则不另造 |
| SHEERFORCE／SHIELDDUST／SERENEGRACE、INNERFOCUS、STENCH | WP43§7、WP44／WP40：附效／畏缩入口及概率，不从威力增幅断言所有后段回调关闭 |
| PRESSURE、PRANKSTER暗系门、STICKYHOLD／OVERCOAT等具体交界 | WP40／WP44既有成功／PP规则；具体物品转移、粉末和未展开招式全集仍WP46/47/50；本稿不自批其余规则 |
| DISGUISE／ICEFACE、DAMP、PROTEAN／LIBERO、PARENTALBOND、MAGICBOUNCE、MOLDBREAKER／TERAVOLT／TURBOBLAZE | WP40／43已有前门与阶段；生命周期／受击直接分支见WP49，完整形态与招式域见WP22／46／47。没有把这些当未登记＝无效果 |
| MAGICGUARD、AIRLOCK／CLOUDNINE、雨／晴强天气等 | WP44／45、WP42主阶段与WP49触发；§2的有效天气是其结果输入 |

能力数据提供身份、名称、说明、标志；说明文字不是行为证明。普通缺失登记回退依WP05／03的有限调用语义；插件注入和无效数据组合没有运行验证。当前世代8、更多类型效果开、速度中途重排开、亲密效果关。替代世代只按正文实际分支保留，不声称完整历代兼容。

## 9. 独立静态向量

基础普通伤害共同前提：WP43§6同公式，等级50、威力60、攻100、防100、单目标、中性相性、非会心、无本系／天气／灼伤／道具，随机取最大（×1）。基础整数伤害28。以下只改变所列变量；输入能力均有效，除非明确压制／模式破坏者。没有执行参考或其转译模型。

| ID | 输入变化 | 手工期望 |
| --- | --- | --- |
| C01 | 速度基底101，QUICKFEET＋实际麻痹，其余速度倍率1 | 101×1.5=151.5→152；不再麻痹÷2。胃液对照能力无效：101÷2=50.5→51 |
| C02 | 重量101、LIGHTMETAL、无物品修正 | 整除→50；模式破坏者开→101；重量1对照仍至少1 |
| C03 | SURGESURFER＋电场，拥有者浮空 | 速度基底100→200；不加接地条件 |
| C04 | QUICKDRAW固定r29／30，全量排序后只局部重算 | 首次档＋1／0，局部重算不重抽；不保证越过更高优先级 |
| C05 | q70，T NOGUARD，模式破坏者开，成功检查可越半无敌、无skip | 普通命中q仍70，r69命中、r70失败；关模式破坏者才在T层q=0 |
| C06 | q80、U与一盟友VICTORYSTAR，a=e=0、me=1；普通整数命中入口，无其它修正、亲密效果或提前必中 | ma=1.21，命中四舍五入为整数121、闪避为整数100；最终整数商80×121÷100=96；r95命中，r96／97均失败 |
| C07 | 变化招q80、对侧WONDERSKIN | q变50，r49／50分界；若U NOGUARD先将q设0，则T不覆盖0 |
| C08 | 基础伤害＋U HUGEPOWER | 攻200，中间伤害54；不是28×2=56 |
| C09 | 基础伤害＋U TOUGHCLAWS且原始接触 | 威力80，中间伤害37；×1.3的威力78并非此合同 |
| C10 | 基础伤害＋T GRASSPELT，青草，特殊且T浮空 | 防150，整段17＋2=19；该处理器仍触发 |
| C11 | 基础改火类型且T FLUFFY，实际接触真／假 | F2×0.5=1→28；非接触F2→56 |
| C12 | U钢类型STEELYSPIRIT＋一同能力盟友，基础无钢本系 | F2.25，28×2.25=63；模式破坏者开只留U1.5→42 |
| C13 | 满HP T SHADOWSHIELD，模式破坏者开／胃液压制 | 前者28÷2=14；后者能力不活跃→28 |
| C14 | P输入威力50、U TECHNICIAN、妖精气场匹配 | 50×4/3>60，不触发技术高手；去气场、后段帮助真时技术高手先通过，然后帮助再乘，门不回看后段 |
| C15 | 毒目标T BATTLEARMOR、U MERCILESS，幸运咒语无 | U99→T−1不暴击；模式破坏者开跳T后由99通过；幸运咒语有则更早拒 |
| C16 | T LIGHTNINGROD特攻0，非自身电，静默／可见免疫 | 都返回免疫；静默0不变，可见请求＋1；特攻＋6仍免疫但不再升 |
| C17 | T WATERABSORB总HP101当前50，非自身水 | 可见恢复25→75；静默保持50；显示不只是装饰 |
| C18 | T COMATOSE＋KOMALA、胃液，询问睡眠／请求中毒 | “视为睡眠”真；不可忽略免疫拒中毒；不能用普通有效假删除两查询 |
| C19 | T FULLMETALBODY、胃液，非自身降攻；无其它门 | 不可忽略防降也不活跃，不以族名保证拒绝；无胃液则模式破坏者开仍拒 |
| C20 | B DAZZLING与U对侧、保存优先级＋1、目标集含对側，模式破坏者开 | 整次阻止，此前PP保留已扣；空目标集对照不由此B阻止 |
| C21 | U一般招＋AERILATE但目的飞行类型不存在 | 保留传入类型、不设强化；不产生虚构类型身份 |
| C22 | 非自身水免疫通过但禁回复／满HP | 返回免疫真，HP不变；免疫成功不等于回血量正 |
| C23 | 野生可逃且RUNAWAY有效／训练家同能力 | 前者资格保证入口真；后者在更早战斗种类门拒，不概括所有场景必逃 |

## 10. 失败、不变量、依赖与未决

不满足表内门则本入口保持输入或返回假；其它核心规则可能仍改变最终行为。倍率容器已改与命中／伤害真的提交不同；成功检查后再失败不会自动返PP。显示假对吸收奖励的差异必须保留。参数、顺序、舍入与主规则冲突时按具名入口回源，不以官方常识修正快照。

完成依赖固定如下（均已限定通过，当前管理回填／身份同步版，不冒充原被审字节）：

- specs/pokemon-rules/wp43-types-accuracy-and-damage.md：`b5ac8946316fae5cac765db52d2344767bca2f9e5abed52ebfc331a216040ed7`（30,921字节）。
- specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md：`a4e82ddf09d9d9db4e4d610e8dc074d5ef093136b74290dd83b84f764a6bdf9c`（50,426字节）。
- specs/pokemon-rules/wp44-effect-coverage.md：`c226232d523b899197590800b8e6f75230de103363eebf6c12a16111a24cb2ad`（27,346字节）。
- specs/combat/wp45-weather-terrain-side-and-position-effects.md：`7ddb026aa71e8576d54ab2f98df5e78e84066e28eccbada4f551ca5ae58e5d95`（36,525字节）。
- specs/combat/wp40-commands-obedience-and-action-order.md：`13ac33470f375f2a3c5f0af7acddb6b038b98ba058e73397f39babf592d32b42`（42,751字节）。

前向：WP49承接本目录余21族、状态／形态／入离场触发，批末核对本包门与阶段；WP50承接所有物品具体修正／转移，本包只保留其调用位置；WP22／23承接完整变身／Shadow；WP46／47承接特殊招式全集，若出现改写q、P/A/D/F或有效性入口需复核§2–8；WP51/52及53–58承接AI／设施；WP77与U01–U10、WP78→79→80不关闭。当前没有以待运行掩盖本包静态参数缺口，真实显示、插件组合和随机运行验证仍未做。

## 11. 取证范围

源码路径相对`Data/Scripts/`。全文／定点是实际文本阅读，非执行。

- `011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb`：1–294声明／包装，299–364、414–510、670–792、818–860、886–1660、2549–2572、3200–3208本包登记正文；生命周期段留WP49，§12联合计数为文本集合证据。
- `011_Battle/002_Battler/001_Battle_Battler.rb:248–287,344–420`；`006_Battler_AbilityAndItem.rb:1–197`共享与免疫helper；`004_Battler_Statuses.rb:1–40,100–137`；`005_Battler_StatStages.rb:123–177`。
- `011_Battle/003_Move/003_Move_UsageCalculations.rb:1–28,109–123,126–220,239–338`；`002_Move_Usage.rb:86–115`；`011_Battle/002_Battler/007_Battler_UseMove.rb:258–284`；`011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb:120–230`、`005_Battle_ActionSwitching.rb:35–71`、`007_Battle_ActionRunning.rb:1–34`。
- `003_Game processing/005_Event_Handlers.rb:97–200,284–300`通用登记／复制语义；`010_Data/002_PBS data/004_Ability.rb`全文；PBS能力样本WONDERGUARD、NOGUARD、TECHNICIAN、GRASSPELT、NEUTRALIZINGGAS只核身份／描述不替代源码。
- Scripts全局检索该登记族，未发现另一注册正文文件；AI引用只定位，不算实际使用者行为证据。WP43／44／45已审核心直接规则继承其证据，不声称重新全文读取整个引擎。

本轮R01定点回读：能力目录`:1123–1137`的两个VICTORYSTAR倍率入口、命中计算`:109–123`的分次取整与整数阈值，并对照已审WP43§4.2；不修改该主规则。其余读取范围继承首稿。

## 12. 有界登记覆盖

文本集合：27族，133直接登记＋11复制语句，复制展开后148个（族，能力）身份；CertainSwitching为空，其余26族有登记。copy列首项是来源，其余才为新增身份。

| 族 | 登记种类 | 审计身份／复制方向 | 源起行 | 具体合同 |
| --- | --- | --- | ---: | --- |
| SpeedCalc | add | CHLOROPHYLL | 299 | §3 |
| SpeedCalc | add | QUICKFEET | 305 | §3 |
| SpeedCalc | add | SANDRUSH | 311 | §3 |
| SpeedCalc | add | SLOWSTART | 317 | §3 |
| SpeedCalc | add | SLUSHRUSH | 323 | §3 |
| SpeedCalc | add | SURGESURFER | 329 | §3 |
| SpeedCalc | add | SWIFTSWIM | 335 | §3 |
| SpeedCalc | add | UNBURDEN | 341 | §3 |
| WeightCalc | add | HEAVYMETAL | 351 | §3 |
| WeightCalc | add | LIGHTMETAL | 357 | §3 |
| StatusCheckNonIgnorable | add | COMATOSE | 414 | §6 |
| StatusImmunity | add | FLOWERVEIL | 425 | §6 |
| StatusImmunity | add | IMMUNITY | 431 | §6 |
| StatusImmunity | copy | IMMUNITY、PASTELVEIL | 437 | §6 |
| StatusImmunity | add | INSOMNIA | 439 | §6 |
| StatusImmunity | copy | INSOMNIA、SWEETVEIL、VITALSPIRIT | 445 | §6 |
| StatusImmunity | add | LEAFGUARD | 447 | §6 |
| StatusImmunity | add | LIMBER | 453 | §6 |
| StatusImmunity | add | MAGMAARMOR | 459 | §6 |
| StatusImmunity | add | WATERVEIL | 465 | §6 |
| StatusImmunity | copy | WATERVEIL、WATERBUBBLE | 471 | §6 |
| StatusImmunityNonIgnorable | add | COMATOSE | 477 | §6 |
| StatusImmunityNonIgnorable | add | SHIELDSDOWN | 483 | §6 |
| StatusImmunityFromAlly | add | FLOWERVEIL | 493 | §6 |
| StatusImmunityFromAlly | add | PASTELVEIL | 499 | §6 |
| StatusImmunityFromAlly | add | SWEETVEIL | 505 | §6 |
| StatLossImmunity | add | BIGPECKS | 670 | §6 |
| StatLossImmunity | add | CLEARBODY | 687 | §6 |
| StatLossImmunity | copy | CLEARBODY、WHITESMOKE | 702 | §6 |
| StatLossImmunity | add | FLOWERVEIL | 704 | §6 |
| StatLossImmunity | add | HYPERCUTTER | 720 | §6 |
| StatLossImmunity | add | KEENEYE | 737 | §6 |
| StatLossImmunityNonIgnorable | add | FULLMETALBODY | 758 | §6 |
| StatLossImmunityFromAlly | add | FLOWERVEIL | 777 | §6 |
| PriorityChange | add | GALEWINGS | 822 | §3 |
| PriorityChange | add | PRANKSTER | 829 | §3 |
| PriorityChange | add | TRIAGE | 838 | §3 |
| PriorityBracketChange | add | QUICKDRAW | 848 | §3 |
| PriorityBracketChange | add | STALL | 854 | §3 |
| MoveBlocking | add | DAZZLING | 886 | §7 |
| MoveBlocking | copy | DAZZLING、QUEENLYMAJESTY | 896 | §7 |
| MoveImmunity | add | BULLETPROOF | 902 | §7 |
| MoveImmunity | add | FLASHFIRE | 919 | §7 |
| MoveImmunity | add | LIGHTNINGROD | 945 | §7 |
| MoveImmunity | add | MOTORDRIVE | 952 | §7 |
| MoveImmunity | add | SAPSIPPER | 959 | §7 |
| MoveImmunity | add | SOUNDPROOF | 966 | §7 |
| MoveImmunity | add | STORMDRAIN | 983 | §7 |
| MoveImmunity | add | TELEPATHY | 990 | §7 |
| MoveImmunity | add | VOLTABSORB | 1008 | §7 |
| MoveImmunity | add | WATERABSORB | 1014 | §7 |
| MoveImmunity | copy | WATERABSORB、DRYSKIN | 1020 | §7 |
| MoveImmunity | add | WONDERGUARD | 1022 | §7 |
| ModifyMoveBaseType | add | AERILATE | 1043 | §4 |
| ModifyMoveBaseType | add | GALVANIZE | 1051 | §4 |
| ModifyMoveBaseType | add | LIQUIDVOICE | 1059 | §4 |
| ModifyMoveBaseType | add | NORMALIZE | 1065 | §4 |
| ModifyMoveBaseType | add | PIXILATE | 1073 | §4 |
| ModifyMoveBaseType | add | REFRIGERATE | 1081 | §4 |
| AccuracyCalcFromUser | add | COMPOUNDEYES | 1093 | §4 |
| AccuracyCalcFromUser | add | HUSTLE | 1099 | §4 |
| AccuracyCalcFromUser | add | KEENEYE | 1105 | §4 |
| AccuracyCalcFromUser | add | NOGUARD | 1111 | §4 |
| AccuracyCalcFromUser | add | UNAWARE | 1117 | §4 |
| AccuracyCalcFromUser | add | VICTORYSTAR | 1123 | §4 |
| AccuracyCalcFromAlly | add | VICTORYSTAR | 1133 | §4 |
| AccuracyCalcFromTarget | add | LIGHTNINGROD | 1143 | §4 |
| AccuracyCalcFromTarget | add | NOGUARD | 1149 | §4 |
| AccuracyCalcFromTarget | add | SANDVEIL | 1155 | §4 |
| AccuracyCalcFromTarget | add | SNOWCLOAK | 1161 | §4 |
| AccuracyCalcFromTarget | add | STORMDRAIN | 1167 | §4 |
| AccuracyCalcFromTarget | add | TANGLEDFEET | 1173 | §4 |
| AccuracyCalcFromTarget | add | UNAWARE | 1179 | §4 |
| AccuracyCalcFromTarget | add | WONDERSKIN | 1185 | §4 |
| DamageCalcFromUser | add | AERILATE | 1197 | §5 |
| DamageCalcFromUser | copy | AERILATE、GALVANIZE、NORMALIZE、PIXILATE、REFRIGERATE | 1203 | §5 |
| DamageCalcFromUser | add | ANALYTIC | 1205 | §5 |
| DamageCalcFromUser | add | BLAZE | 1221 | §5 |
| DamageCalcFromUser | add | DEFEATIST | 1229 | §5 |
| DamageCalcFromUser | add | DRAGONSMAW | 1235 | §5 |
| DamageCalcFromUser | add | FLAREBOOST | 1241 | §5 |
| DamageCalcFromUser | add | FLASHFIRE | 1247 | §5 |
| DamageCalcFromUser | add | FLOWERGIFT | 1255 | §5 |
| DamageCalcFromUser | add | GORILLATACTICS | 1263 | §5 |
| DamageCalcFromUser | add | GUTS | 1269 | §5 |
| DamageCalcFromUser | add | HUGEPOWER | 1277 | §5 |
| DamageCalcFromUser | copy | HUGEPOWER、PUREPOWER | 1283 | §5 |
| DamageCalcFromUser | add | HUSTLE | 1285 | §5 |
| DamageCalcFromUser | add | IRONFIST | 1291 | §5 |
| DamageCalcFromUser | add | MEGALAUNCHER | 1297 | §5 |
| DamageCalcFromUser | add | MINUS | 1303 | §5 |
| DamageCalcFromUser | copy | MINUS、PLUS | 1312 | §5 |
| DamageCalcFromUser | add | NEUROFORCE | 1314 | §5 |
| DamageCalcFromUser | add | OVERGROW | 1322 | §5 |
| DamageCalcFromUser | add | PUNKROCK | 1330 | §5 |
| DamageCalcFromUser | add | RECKLESS | 1336 | §5 |
| DamageCalcFromUser | add | RIVALRY | 1342 | §5 |
| DamageCalcFromUser | add | SANDFORCE | 1354 | §5 |
| DamageCalcFromUser | add | SHEERFORCE | 1363 | §5 |
| DamageCalcFromUser | add | SLOWSTART | 1369 | §5 |
| DamageCalcFromUser | add | SNIPER | 1375 | §5 |
| DamageCalcFromUser | add | SOLARPOWER | 1381 | §5 |
| DamageCalcFromUser | add | STAKEOUT | 1389 | §5 |
| DamageCalcFromUser | add | STEELWORKER | 1395 | §5 |
| DamageCalcFromUser | add | STEELYSPIRIT | 1401 | §5 |
| DamageCalcFromUser | add | STRONGJAW | 1407 | §5 |
| DamageCalcFromUser | add | SWARM | 1413 | §5 |
| DamageCalcFromUser | add | TECHNICIAN | 1421 | §5 |
| DamageCalcFromUser | add | TINTEDLENS | 1430 | §5 |
| DamageCalcFromUser | add | TORRENT | 1436 | §5 |
| DamageCalcFromUser | add | TOUGHCLAWS | 1444 | §5 |
| DamageCalcFromUser | add | TOXICBOOST | 1450 | §5 |
| DamageCalcFromUser | add | TRANSISTOR | 1458 | §5 |
| DamageCalcFromUser | add | WATERBUBBLE | 1464 | §5 |
| DamageCalcFromAlly | add | BATTERY | 1474 | §5 |
| DamageCalcFromAlly | add | FLOWERGIFT | 1481 | §5 |
| DamageCalcFromAlly | add | POWERSPOT | 1489 | §5 |
| DamageCalcFromAlly | add | STEELYSPIRIT | 1495 | §5 |
| DamageCalcFromTarget | add | DRYSKIN | 1505 | §5 |
| DamageCalcFromTarget | add | FILTER | 1511 | §5 |
| DamageCalcFromTarget | copy | FILTER、SOLIDROCK | 1519 | §5 |
| DamageCalcFromTarget | add | FLOWERGIFT | 1521 | §5 |
| DamageCalcFromTarget | add | FLUFFY | 1529 | §5 |
| DamageCalcFromTarget | add | FURCOAT | 1536 | §5 |
| DamageCalcFromTarget | add | GRASSPELT | 1543 | §5 |
| DamageCalcFromTarget | add | HEATPROOF | 1549 | §5 |
| DamageCalcFromTarget | add | ICESCALES | 1555 | §5 |
| DamageCalcFromTarget | add | MARVELSCALE | 1561 | §5 |
| DamageCalcFromTarget | add | MULTISCALE | 1569 | §5 |
| DamageCalcFromTarget | add | PUNKROCK | 1575 | §5 |
| DamageCalcFromTarget | add | THICKFAT | 1581 | §5 |
| DamageCalcFromTarget | add | WATERBUBBLE | 1587 | §5 |
| DamageCalcFromTargetNonIgnorable | add | PRISMARMOR | 1597 | §5 |
| DamageCalcFromTargetNonIgnorable | add | SHADOWSHIELD | 1605 | §5 |
| DamageCalcFromTargetAlly | add | FLOWERGIFT | 1615 | §5 |
| DamageCalcFromTargetAlly | add | FRIENDGUARD | 1623 | §5 |
| CriticalCalcFromUser | add | MERCILESS | 1633 | §4 |
| CriticalCalcFromUser | add | SUPERLUCK | 1639 | §4 |
| CriticalCalcFromTarget | add | BATTLEARMOR | 1649 | §4 |
| CriticalCalcFromTarget | copy | BATTLEARMOR、SHELLARMOR | 1655 | §4 |
| TrappingByTarget | add | ARENATRAP | 2553 | §7 |
| TrappingByTarget | add | MAGNETPULL | 2559 | §7 |
| TrappingByTarget | add | SHADOWTAG | 2565 | §7 |
| CertainEscapeFromBattle | add | RUNAWAY | 3204 | §7 |

此表是追溯索引；具体量值与分支必须连同前文合同阅读，不以有名字替代行为。27族上述范围依独立PASS_SCOPED管理回填Reviewed；其余完整招式／物品／形态组合与运行保留。被审v2合同不改，未修改reference或实现未来框架。
