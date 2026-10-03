# 多次攻击、特殊伤害与恢复（净化正文；批次 7）

分类：Pokémon Rules／Combat Requirements。本文件描述一次使用内多击、跨回合伤害、替代普通伤害/改变输入、吸取/反伤/治疗及代价怎样形成可见结果。全部内容为静态证据与独立常数算术；**无运行确认**（见 `../scope-statement.md`）。覆盖表：[wp46-damage-healing-coverage](wp46-damage-healing-coverage.md)（139 项有界主合同逐项归属）。

## 1. 目的、边界与共同输入

A 为共同调用与数据，B 为多击/蓄力/连用，C 为固定伤害/反击，D 为威力/类别/能力值特例，E 为恢复/吸取/持续效果，F 为自损/同归与失败。

基础公式、类型、普通命中和会心主规则在《战斗类型、命中与伤害计算》；状态/阶级中央资格与写回在《异常状态、能力阶级与免疫》；位置/场域生命周期在场域规格；命令/PP 及调用标志在命令规格；主阶段与终局在战斗结果规格；能力计算/生命周期在《特性参与计算、免疫与有效性》/阶段触发规格。这里只写该族的替代和具体请求。完整物品处理器《持有物计算、触发与消耗》、完整个体变身《Mega、Primal 与显式还原》、Shadow、AI/设施/运行/demo 及出口均保留。

记 U 为本次实际使用者、T 为实际目标，h/H 为当前/总 HP，L 为等级，P 为数据威力或本族给出的基底，R(x) 为正数四舍五入（恰半向上），⌊x⌋ 为向下取整，⌈x⌉ 为向上取整。速度/重量均为当时查询结果，含已审能力等修正，不能以裸属性替代。输入还包括当前类型、能力/物品有效性、阶级、选择、使用记录、上轮失败、伤害状态、世代开关和数据标记。输出分为计算伤害、计划/实际损失（可含替身）、HP 与状态写回、持续标记/计数、决定、消息和等待，不以一个「成功」概括。

## 2. 整次使用、每击与中断

### 2.1 实际消费者顺序

前置使用资格/服从性 → 普通使用扣 PP → 本次类型/模式破坏者/两回合状态 → 使用计数和记录 → 目标寻找/改变及压力/整招阻止 → 本招整次失败检查 → 本次初始化（如随机威力、类别快照）→ 其它前门/变类型/快速蓄力 → 无目标门。详细位置以命令规格已审合同为准，失败位置不同，前面已扣 PP 或消耗道具不自动退回。

目标集确定后，逐目标整次检查一次：重置跨击状态、计算相性、目标特例/保护/反射/免疫等；不通过者记 unaffected。蓄力回合在计算相性后提前通过该层，不在此检查全部普通目标门。然后决定计划击数。

每击入口先拒 U 倒下，执行本击初始化、亲子爱计数 −1。第 1 击或明确「每击命中」的族才做半无敌/命中检查；有目标列表却无一目标成功且不允许空目标时提示、失手物品、坠落自损、取消连用并返回假。正常续击不把所有保护/类型免疫/状态资格再跑一遍。第一击确定的相性、unaffected 和跨击总损失不会被每击重置。

本击选取要打的目标后，重置本击 calcDamage/hpLost/会心/替身/耐受等；逐有效目标重新查询吸收、计算伤害/会心及当时攻防与倍率、规划损失；展示本击招式/宝石使用提示，然后提交各目标 HP（替身只扣耐久）。接着第 1 击的自我失能/自损入口 → U 濒死 → 记录伤害 → 伤害当下副效果（如溅射）→ 每击能力/物品反应 → 耐受和破皮提示 → 全场恢复物品与濒死 → 裁判检查点 → 逐目标主要效果（含吸取）→ 全局主要效果 → 濒死 → 附效与额外畏缩 → 减伤果消耗 → 蒸汽机等 → 再濒死。顺序沿阶段触发规格，不能改为「所有吸取先于反伤反应」。

每成功击后实计击数＋1；U 倒下、真实睡眠/冰冻、全部目标倒下时停止；处理中定身不阻止剩余击数。其它异常或能力变化仍通过后续实际消费者生效，不能自行增加每击服从/PP 检查。随后逐原目标执行本招「所有击后」处理，即使本次击数 0 也可能到达（前提没有更早整招返回）；本地 unaffected 守卫各不相同。再按阶段触发规格整招后置（同命、U 能力、物品/退出等）和战斗结果规格成长/裁判。没有每次写决定就立即打断所有嵌套回调的统一保证。

替身破坏后下一击重新查吸收，可伤真实 HP；每击能力值/HP/物品可变，但本次类型通常更早固定，相性来自整次目标检查。固定伤害也经过吸收和留 1 等 HP 限制；亲子爱的普通威力减幅不施加到绕普通公式的固定值。新临时组合没有真实运行验证。

### 2.2 计量、取消与可见失败

- hpLost 为本击经截断的实际计划损失，可含替身；totalHPLost 是同目标跨击累计；普通反伤读后者，吸取读前者。不能以计算伤害替代二者。
- 常规扣 HP/回 HP 写持久个体，金额先 R、夹到可损失/可恢复值；存活损失请求 <1 至少 1，缺 HP 恢复请求 <1 至少 1。canHeal 另拒倒下、满 HP、治疗封锁；中央恢复本身不自动重跑这份资格。
- 可受间接伤害查询拒倒下和有效 MAGICGUARD；ROCKHEAD 是普通反伤的额外门，不能推广给所有自损。液体污泥吸取反损直接扣 HP，没有通用 MAGICGUARD 门。
- 取消连用清两回合、滚动、暴走、吵闹、忍耐及连续切割；不清破坏光线休息。暴走剩 1 被非完全取消打断，若可自混乱仍会混乱。PP 与 specialUsage/skipAccuracyCheck 两标志沿命令规格：续回合不重新普通耗 PP，但不因此成为统一必中。
- 消息/动画随实际门和击数出现。多目标＋多击自定义组合的消息模板未保证覆盖所有排列；当前数据和源有限目录确认不等于任意扩展组合通过。

## 3. 多击、两回合与连用

### 3.1 一次使用的击数

| 审计身份 | 完整本族合同 |
| --- | --- |
| HitTwoTimes | 计划 2 击；普通首击命中门，续击重算伤害/反应但不再次普通命中 |
| HitTwoTimesPoisonTarget | 同 2 击；每击按数据附效概率独立尝试普通中毒，替身挡附效，状态资格《异常状态、能力阶级与免疫》 |
| HitTwoTimesFlinchTarget | 同 2 击；每击按数据附效概率尝试畏缩；被标为自带畏缩族，不额外叠物品同类畏缩抽取 |
| HitThreeTimesPowersUpWithEachHit | 初始化累计威力 0；每次基底求值加一份数据 P，普通单目标第 1/2/3 击为 P/2P/3P；开始时 SKILLLINK 有效则关闭每击命中，其余三击分别检查，失手即止。不是把已完成的击撤销 |
| HitThreeTimesAlwaysCriticalHit | 固定 3 击；每击请求必会心覆盖，但幸运咒语/防会心等更早拒绝仍有效（《战斗类型、命中与伤害计算》），不保证绝对会心 |
| HitTwoToFiveTimes | 先均匀抽 0..19：0–6→2，7–13→3，14–16→4，17–19→5，即 7/20、7/20、3/20、3/20。SKILLLINK 有效时仍发生此次抽取，随后选末项强制 5 |
| HitTwoToFiveTimesOrThreeForAshGreninja | GRENINJA 形态 2 直接计划 3、各击基底 20；本分支不需再查 BATTLEBOND 有效性。不满足则上述 2–5 次数与数据 P |
| HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1 | 2–5 规则；所有击后对非 unaffected 目标先请求 U 防−1，再速＋1，各中央资格，可部分成功。顺序不是说明标题的「先升速」 |
| HitOncePerUserTeamMember | 整招前收 U 业主队伍段内所有可战斗且真实状态无的成员，**包括符合条件的 U**、不包括伙伴；空则失败。快照名单长度为计划次数，逐击按队伍顺序取一名，其物种基础攻击值 b 决定基底 5＋⌊b/10⌋；仍用 U 普通伤害输入，不用参与者等级/攻击作整个伤害公式 |
| 普通招式的 PARENTALBOND 接点 | 有效亲子爱、当前是实际伤害回合、非蓄力族且目标列表长度 1 时默认计划 2；明写击数的族按其覆盖。标记 3，在两击各 −1，第二击普通 P 倍率世代 ≥7 ÷4、旧代 ÷2；固定伤害绕普通倍率，不能说固定伤害第二击也按该分母减 |

HitTwoTimesTargetThenTargetAlly（龙箭）是两个发射过程，外层计划 1、允许再发，而非普通 multiHit。原列表恰 1 时，从原目标存活盟友中按可加目标/邻近规则找候选，多个时均匀选 1 加入；无候选保留原目标。首次对扩展列表做资格和命中检查，按未 unaffected 列表首目标发射，第二发取第二有效目标、无第二则重复第一。只有第一发所选目标在后段仍存活且非 unaffected，才递归第二发；若它倒下，本快照不会仅因另一个候选仍活而保证第二发。递归入口也拒 U 倒下；第二发不普通重测命中。两候选均有效时失效消息可隐藏；全部无效只显示一次相关失手消息。静默免疫不获吸收奖励的合同保留，完整通用重定向由招式变更规格承接。

### 3.2 两回合共同合同

TwoTurnAttack 族（含 OneTurnInSun、ParalyzeTarget、BurnTarget、FlinchTarget、RaiseUserSpAtkSpDefSpd2、ChargeRaiseUserDefense1、ChargeRaiseUserSpAtk1、InvulnerableUnderground、InvulnerableUnderwater、InvulnerableInSky、InvulnerableInSkyParalyzeTarget、InvulnerableInSkyTargetCannotAct、InvulnerableRemoveProtections 十四个审计身份）属于此有界族。

开始无两回合标记时确定蓄力；普通情形只蓄力不造成伤害，保存当前招式/两回合标记。已有标记时为攻击回合，并清两回合标记。有效 POWERHERB 可令同回合兼有蓄力与伤害：在目标资格检查前显示快速蓄力、执行各目标蓄力效果并消耗香草，然后才走后续失败/命中；后续失败不退香草或蓄力升阶。天空摔投完全不获香草收益。蓄力中普通目标资格和逐击命中在上述早门通过，但整招失败及更早阻止仍可生效；不从注释猜测全族相同效果次序。

| 身份/变体 | 具体差异、资格与状态 |
| --- | --- |
| TwoTurnAttack | 蓄力提示，下一轮普通伤害；无其它数值覆盖 |
| TwoTurnAttackOneTurnInSun | 首轮有效晴/大日照时直接兼蓄力与攻击、不开香草消耗；P 末端倍率在有效天气非无/晴/大日照时 ÷2。无天气不减半，不按标题泛称「非晴皆半」 |
| TwoTurnAttackParalyzeTarget／BurnTarget | 攻击击按数据附效概率施麻痹/灼伤，替身挡附效，中央资格；不在蓄力时施加 |
| TwoTurnAttackFlinchTarget | 攻击击附效畏缩；自带畏缩标记；蓄力不因此先畏缩 |
| TwoTurnAttackRaiseUserSpAtkSpDefSpd2 | 既有两回合标记时其局部整招失败检查先返回不失败；否则至少一项可升才继续；攻击阶段依特攻＋2 → 特防＋2 → 速度＋2，各自资格、部分成功。实际无伤害类别，不复制为未来攻击算法 |
| TwoTurnAttackChargeRaiseUserDefense1／ChargeRaiseUserSpAtk1 | 蓄力效果分别防御＋1/特攻＋1；被后续攻击拒绝不回滚已升项 |
| TwoTurnAttackInvulnerableUnderground／Underwater | 蓄力半无敌身份分别地下/水下；命中豁免招式与倍率例外见 §5 和《战斗类型、命中与伤害计算》 |
| TwoTurnAttackInvulnerableInSky／InSkyParalyzeTarget | 蓄力空中半无敌且重力不可使用；后者攻击附效麻痹、替身挡。重力/半无敌成功门按命令规格，不扩为一律必中 |
| TwoTurnAttackInvulnerableInSkyTargetCannotAct | 天空摔投：不消耗香草；局部目标门拒同侧、未绕过替身、世代 ≥6 查询重量 ≥2000、半无敌目标、蓄力时已有天空摔投、攻击时指向不是 U 的目标。蓄力目标标记指向 U；T 飞行类型的相性覆盖为免疫（不是所有浮空）；攻击所有击后清目标指向 −1，该后置没有 unaffected 门。蓄力通用早门与实际攻击门分开，不能假定蓄力就跑全部此局部门 |
| TwoTurnAttackInvulnerableRemoveProtections | 蓄力消失半无敌；攻击实际主要效果清 T 碉堡/王盾/拦堵/守住/尖刺防守及 T 侧戏法/掀榻榻米/快速/广域防守，具体保护绕过还取决招式标记及成功层；不清挺住或其它任意标记 |

### 3.3 跨回合连用

| 身份 | 建立/消费/失败合同 |
| --- | --- |
| AttackAndSkipNextTurn | 实际全局主要效果设休息计数 2、保存招式；命令规格下一行动消耗休息，取消其它连用不清它。所有目标无效且逐击过程提前失败时不到该建立 |
| MultiTurnAttackPreventSleeping | 吵闹原计数 0 才设 3、保存招式，速度序唤醒真实睡眠且无有效 SOUNDPROOF 的存活成员；重复正计数不重设。之后按战斗结果规格回合末递减、《异常状态、能力阶级与免疫》阻睡；不套百科「隔音也受影响」 |
| MultiTurnAttackConfuseUserAtEnd | 非 unaffected 目标且原暴走 0 时抽 2 或 3 各 1/2 并锁当前招式；每次所有击后正计数 −1，归 0 且可自混乱则混乱。失败取消/舞者额外处理分别归命令/阶段触发规格 |
| MultiTurnAttackPowersUpEachTurn | 始用基底 P；后续读滚动剩余计数 c，使 P×2^(5−c)，首次 c0 不加指数；变圆标记另 ×2。所有击后若目标有效且原 c0 设 5，再正值 −1；常规五次 P、2P、4P、8P、16P，变圆再翻倍；计划 1 击不被亲子爱扩展 |
| MultiTurnAttackBideThenReturnDoubleDamage | 始用建立计数 3、累计 0、来源 −1、锁当前招式，主要效果每次 −1；计数 1 时放出，前两回合不伤害。累计每次伤害记录（含替身的本击损失）并更新最近来源；放出先尝试来源席位，不可加则随机存活对手（不要求邻近）；累计 0 或无目标整招失败且计数 0，其它辅助字段不在这一步统一清。伤害为累计 ×2、至少 1 的固定伤害 |

## 4. 固定伤害、反击与伤害记录

这些效果提供固定 calcDamage、最少 1 并强制非会心，绕过普通 P/攻防/本系/波动/威力倍率，却仍经过本次类型/能力免疫、保护、命中、替身/画皮/结冻头吸收和留 1/实际 HP 上限。不是「固定伤害忽略全部规则」。

| 身份 | 固定量与局部拒绝 |
| --- | --- |
| FixedDamage20／FixedDamage40 | 固定 20/40 |
| FixedDamageHalfTargetHP | R(T 当前 HP/2)；1 HP 给 1，不是 0 |
| FixedDamageUserLevel | U 等级 L |
| FixedDamageUserLevelRandom | 从 ⌊L/2⌋ 到 ⌊3L/2⌋ 的所有整数均匀抽取，含两端；可能生成 0，随后固定值下限改 1 |
| LowerTargetHPToUserHP | U 当前 HP ≥ T 当前 HP 失败，否则差值 T−U；明确计划 1 击；HP 上限/替身可能令实际个体 HP 不等于 U |
| OHKO | T 等级更高拒；有效 STURDY 且模式破坏者假拒。命中专用阈值＝招式命中＋U 等级−T 等级，0..99 严格小于，**不经过普通命中倍率表**；伤害给 T 总 HP，仍有其它上层门和下层耐受 |
| OHKOIce | 目标失败门分入口。**原定义**先拒 T 冰类型，其后才走父类等级/坚硬门。**条款文件加载后且无后续覆盖**（该文件在该定义之后加载，依序重开父类与冰子类）：父类已保存的原目标检查可被继承，子类未另保存自身拒冰门；条款假时新目标检查走继承的等级/坚硬门，不再仅因 T 冰拒绝，条款真仍拒。命中入口独立：上述专用阈值在 U 非冰时再 −10 未改。效果标识对应的原实现没有局部世代门，数据选择该标识和世代配置分开，不据注释擅自跳过。目标失败门通过不等于命中、击倒或整招成功 |
| OHKOHitsUndergroundTarget | OHKO 并允许地下半无敌目标；不等于所有半无敌 |
| CounterPhysicalDamage／CounterSpecialDamage | 目标取最近物理/特殊伤害记录的来源席，必须与 U 对侧、可加入（不要求邻近）；无目标整招失败，不随机替补。固定值分别该记录 ×2，0 至少 1；记录初始 −1 通常无来源不进入 |
| CounterDamagePlusHalf | 用 U 最近对侧攻击者列表末项作目标，要求可加且对侧；无目标失败；固定值 ⌊最近对侧 hpLost×1.5⌋、至少 1 |
| UserFaintsFixedDamageUserHP | 初始化保存 U 当时 HP，固定伤害取保存值、计划 1；自损时扣当前全部 HP，见 §7，与随后回复/变化不能混同 |

伤害记录在每击反应前更新：非替身才写物理 Counter 或特殊 MirrorCoat 的当前损失与来源；忍耐累计不带替身排除。lastHPLost、受伤标志和来源列表分开：直接伤害标志要求正损失且非替身，普通受伤标志正损失即可，攻击来源列表可记录 0 损失的命中；对侧另记其最近损失/来源。旧按类型分类时觉醒力量的反击分类有一般类型强制输入；同一击的记录不代表整招累计。尾清/初始化沿战斗结果/换人规格。

DamageTargetAlly：目标在伤害当下处理阶段，遍历其存活邻近盟友、可受间伤者扣各总 HP 整除 16；先都扣再提示，再各自恢复物品。没有本地「目标本击非替身」门，不能据溅射名称附加；后续全场濒死/退出按阶段触发规格。溅射量不乘目标类型相性，也不当 U 直接命中那些盟友。

### 4.1 使用时机/记录限定的伤害招

这些局部失败发生在普通前置与扣 PP 之后，除明列选择门外不保证菜单时提前拒绝。

| 身份 | 局部准入/反馈 |
| --- | --- |
| FailsIfNotUserFirstTurn | U 的在场 turnCount >1 时整招失败；没有把合法 turnCount 0 也拒掉 |
| FailsIfUserHasUnusedMove | 逐当前 U 招式槽：必须含本招且至少另 1 招，所有其它身份都在已用记录内；任一缺少则逐目标失败；不要求其它槽当前仍有 PP |
| FailsIfUserNotConsumedBerry | 选择和使用时均查 U 已吃果记录，假拒；记录来源/持久口径沿《HP、状态、招式与持物》及招式变更/持物规格，不以「当前持有树果」代替已吃 |
| FailsIfTargetHasNoItem | T 无当前物或物品不生效则逐目标失败；通过会显示该物正要发动的提示，show_message 假也不抑制这段通过提示；不移除物品 |
| FailsUnlessTargetSharesTypeWithUser | U 与 T 当前完整类型集合至少一交集才准，无共同类型逐目标无效 |
| FailsIfUserDamagedThisTurn | 回合蓄势提示先置 FocusPunch 真；只有该标记与本轮直接招式受伤标记都真才整招失败；特殊调用未设蓄势标记不能仅凭曾受伤直接拒绝 |
| FailsIfTargetActed | T 须选 UseMove 且招式存在；除抢先使用目标将用招的效果标识外，T 已行动或所选变化招均失败。特殊例外不删除外层「必须选 UseMove」门 |

## 5. 威力、类别和输入替代

下表标「基底」在普通公式前替换 P；标「P 倍率末端／F 末端」分别在《战斗类型、命中与伤害计算》所有通用倍率之后的招式专用位置改威力倍率/最终倍率，不能任意换槽。基底按每次求值读取当前状态，明确初始化快照者例外。

### 5.1 数值输入表

| 身份 | 具体数学/条件 |
| --- | --- |
| PowerHigherWithUserHP | 基底 max（⌊150×U.h/U.H⌋, 1） |
| PowerLowerWithUserHP | n=⌊48×U.h/U.H⌋；n<2／5／10／17／33 时依次 200／150／100／80／40，否则 20 |
| PowerHigherWithTargetHP | 基底 max（⌊120×T.h/T.H⌋, 1） |
| PowerHigherWithUserHappiness／PowerLowerWithUserHappiness | 基底 max（⌊2×友好/5⌋, 1）／max（⌊2×(255−友好)/5⌋, 1） |
| PowerHigherWithUserPositiveStatStages | 七项正阶级之和 s，负值不计，基底 20×(1+s) |
| PowerHigherWithTargetPositiveStatStages | T 七项正阶级和 s，基底 min（20×(3+s), 200） |
| PowerHigherWithUserFasterThanTarget | 当时 U 速度整除 T 速度 n；n≥4→150，≥3→120，≥2→80，≥1→60，否则 40 |
| PowerHigherWithTargetFasterThanUser | 基底夹限 ⌊25×T 速度/U 速度⌋ 至 1..150 |
| PowerHigherWithLessPP | 普通 PP 已先扣：剩 PP 0／1／2／3／≥4 时基底 200／80／60／50／40；不按使用前 PP。负 PP 为特殊调用内部输入，若 −1 会取此表末项 40；不推广任意非法负数兼容 |
| PowerHigherWithTargetWeight | 查询重量 ≥2000／1000／500／250／100 依次 120／100／80／60／40，否则 20（重量单位沿数据，2000 为 200kg） |
| PowerHigherWithUserHeavierThanTarget | U 重量整除 T 重量 n≥5／4／3／2 依次 120／100／80/60，否则 40 |
| RandomPowerDoublePowerIfTargetUnderground | 本次初始化均匀 0..19，威力 10／30／50／70／90／110／150 权重 1／2／4／6／4／2／1，同时显示震级 4..10；整次共享随机基底。允许地下命中；地下目标 F×2，当前青草场地 F÷2，无接地附加门 |
| PowerHigherWithConsecutiveUse | 使用计数阶段先保留旧连续切割，通用清后加 1 至上限；上限是数据 P 逐次翻倍首次达到 ≥160 所需次数（非硬夹最终 P160）；基底乘 2^(次数−1)。换招/失败取消可清，不能把未命中也算持续成功 |
| PowerHigherWithConsecutiveUseOnUserSide | 每侧每轮首次使用时旧回声计数＋1、最多 5，设本轮已用；基底 P 乘该数；同轮多成员不再＋1，尾部若整轮未用才清（场域/战斗结果规格） |

### 5.2 条件加倍与后处理

| 身份 | 实际门/槽/其它结果 |
| --- | --- |
| DoublePowerIfTargetHPLessThanHalf | T.h ≤ T.H 整除 2，基底 ×2 |
| DoublePowerIfUserPoisonedBurnedParalyzed | U 视为毒/灼伤/麻痹任一，基底 ×2；世代 ≥6 不受通常灼伤减伤，旧代仍受 |
| DoublePowerIfTargetAsleepCureTarget／DoublePowerIfTargetParalyzedCureTarget | T 视为睡/麻痹且无替身或本招绕替身，基底 ×2；所有击后 T 存活、未 unaffected、非替身且真实状态匹配才治对应状态；COMATOSE 等视为状态不被治 |
| DoublePowerIfTargetPoisoned／DoublePowerIfTargetStatusProblem | T 视为毒/任意状态且无替身或可绕替身，基底 ×2；不治疗 |
| DoublePowerIfUserHasNoItem | U 无当前物品或本次 GemConsumed 标记真，P 倍率末端 ×2；不只查物品有效 |
| DoublePowerIfTargetUnderwater | 可命中潜水，目标正在潜水时 F 末端 ×2 |
| DoublePowerIfTargetUnderground | 可命中挖洞，挖洞 F 末端 ×2；当前青草场地 F 末端 ÷2，无接地门 |
| DoublePowerIfTargetInSky／FlinchTargetDoublePowerIfTargetInSky | 可命中空中，T 处飞翔/弹跳/天空摔投两回合或被天空摔投时基底 ×2；后者畏缩附效主合同归《异常状态、能力阶级与免疫》 |
| DoublePowerInElectricTerrain | 当前电场且 T 受场地影响，基底 ×2；是 T 门，不是 U 门 |
| DoublePowerIfUserLastMoveFailed | U 上轮失败标记真，基底 ×2；不是本次已设 lastMoveFailed |
| DoublePowerIfAllyFaintedLastTurn | U 侧 LastRoundFainted ≥0 且等于当前轮−1，基底 ×2 |
| DoublePowerIfUserLostHPThisTurn | U 的 lastAttacker 列表含 T 席位，基底 ×2；实际记录可能含 0 损失，不能加「本次实际失 HP>0」的不存在守卫 |
| DoublePowerIfTargetLostHPThisTurn | T 本轮受伤标记真，基底 ×2，含间伤及替身所导致的记录差异依消费者 |
| DoublePowerIfUserStatsLoweredThisTurn | U 本轮下降阶级标记真，基底 ×2 |
| DoublePowerIfTargetActed | T 选择非 None，且（选择既非 UseMove 也非 Shift，或 T 已行动），基底 ×2；不以速度比较代替 |
| DoublePowerIfTargetNotActed | T 选择 None，或选择 UseMove/Shift 且未行动，基底 ×2；名义换入只是 None 的常见来源 |
| DoublePowerAfterFusionFlare／DoublePowerAfterFusionBolt | 使用计数先保存另一交错招标记，再通用计数清双方交错标记；保存真则本次 P 倍率末端 ×2，全局主要效果才设自己标记。中间普通使用也清标记，不能仅记同轮曾用过就永久加倍 |
| AlwaysCriticalHit | 请求会心覆盖 1，仍在《战斗类型、命中与伤害计算》早期不可会心门之后 |
| CannotMakeTargetFaint | 普通损失会致命时留下 1，非满 HP 也适用；不防后续附效/残余/自损 |

### 5.3 类别、相性和攻防替代

EffectivenessIncludesFlyingType：每个防御类型的通常单项相性结果，另乘飞行类型对该防御类型的基础倍率；飞行身份不存在则不乘。数据的 0/1/2/4 先在基础相性查询中除以 2 成为 0/1/2/1/2，本覆盖点相乘的是已归一倍率，不重复除以 2。额外飞行项不重跑通常单项的标靶/识破/强风等例外；全局类型与 HP 门仍引用《战斗类型、命中与伤害计算》，向量见测试目录 D09。

CategoryDependsOnHigherDamagePoisonTarget：本次初始化只读首目标，按 U 攻/特攻和 T 防/特防各自阶级取整（防御读数受奇妙空间交换），比较物理攻击/防御与特殊攻击/特防的比值；大者决定本次类别，平手均匀两类。正常战斗用战斗随机，命令期预览用另一随机入口，不能保证统一种子；无首目标则保留该招对象当前类别（初始特殊）。不试算完整伤害或能力倍率。物理类别才带接触；普通毒附效沿《异常状态、能力阶级与免疫》。

CategoryDependsOnHigherDamageIgnoreTargetAbility：只比 U 阶级后取整的攻与特攻，攻严格更大才物理，否则特殊，平手不抽；目标能力忽略采用 IgnoreTargetAbility 具名效果（招式变更规格），不据注释断言所有不可忽略/生命周期能力失效。

UseUserDefenseInsteadOfUserAttack 取 U 当时防御读数及防阶级作攻击输入，后续仍用攻击修正槽；UseTargetAttackInsteadOfUserAttack 按实际类别取 T 攻及攻阶级/T 特攻及特攻阶级作 U 攻击输入；UseTargetDefenseInsteadOfTargetSpDef 取 T 防御及防阶级。三者只替换值/阶级来源，后续会心、纯朴、能力倍率、灼伤等仍按《战斗类型、命中与伤害计算》实际 U/T 规则，不能交换身份。前两者依赖物理/特殊配置，缺失类别数据归内容合同。

### 5.4 蓄力资源与誓约组合

UserAddStockpileRaiseDefSpDef1：已蓄力 ≥3 整招失败；否则先蓄力＋1，再防＋1 → 特防＋1，各自资格；每项中央返回成功才把对应「由蓄力产生的记录次数」＋1（记录 1 不必等于最终实升量，单纯/反向另作用）。即使两项都封顶，蓄力仍可增加。

PowerDependsOnUserStockpile：0 蓄力失败，基底 100×蓄力；所有击后 U 倒下/蓄力 0/目标 unaffected 均不清；到达后先提示效果消退，若目标侧队伍全灭则提前返回，**蓄力及记录仍保留**。其余按记录请求自降防、特防（各自资格），最后清三项记录 0，不保证降阶数值还原为最初阶级。

HealUserDependingOnUserStockpile：0 失败；不可恢复且两项记录都 0 也失败。1/2/3 蓄力分别请求总 HP 整除 4/整除 2/总 HP；进入主要效果后直接中央恢复，不再加 canHeal 门，先恢复再按上述记录下降并清三项；正常治疗封锁仍可能在更早使用资格拒绝此治疗招，不能据后段推出可绕过全局前门。

GrassPledge／FirePledge／WaterPledge：本次先看 U 保存的先誓约标记能否组合；否则扫描存活盟友，须选择 UseMove 且未行动、招式属于另一誓约，取首合格者等待。本次作为等待者不造成伤害，全局主要效果清自己先誓约、给伙伴标记本招身份及 MoveNext 真，自己记 lastMoveFailed 真。伙伴是否最后能行动仍由命令规格处理，不能保证组合一定释放。

| 组合的两种誓约（先后皆可） | 后手实际类型/基底/场域 |
| --- | --- |
| 草＋火 | 火类型（对应类型数据存在才覆盖）、后手数据 P×2，对侧火海 |
| 火＋水 | 水类型、后手数据 P×2，本侧彩虹 |
| 水＋草 | 草类型、后手数据 P×2，对侧湿地 |

类型在更早类型计算已根据标记处理，本次初始化确定组合并设置动画；各自同类型常规使用不是组合。场域所有击后处理只检查本次组合标志，**没有本地 unaffected 门**，因此已经进入组合而目标失败时也不能概括一律不建场。场域为 0 才设 4，不刷新正期限；效果和回合末双递减等沿场域规格。基本数据类型仍来自数据，表的覆盖只在后手类型不同需替换时作数据存在性检查。

## 6. 治疗、吸取与持续建立

### 6.1 即时恢复

普通自身治疗族可被抢夺，先满 HP 失败，使用资格中的治疗封锁门另在命令规格；实际主要效果直接中央恢复并提示，不重跑一般 canHeal。这包括下列前五行，净化另有目标前门。

| 身份 | 条件、请求量与次序 |
| --- | --- |
| HealUserFullyAndFallAsleep | 先拒 U 视为睡眠，再自睡资格（允许覆盖已有状态），再拒满 HP；先自睡 3 计数（含本次循环的计数语义《异常状态、能力阶级与免疫》），再请求全部缺 HP。治疗能力可能在睡眠提交后立刻清睡，不回滚后续恢复 |
| HealUserHalfOfTotalHP | R(U.H/2) |
| HealUserDependingOnWeather | 本次初始化保存：有效晴 R(2H/3)，无天气/强风 R(H/2)，其它有效天气 R(H/4)；随后使用此量，不按后来天气重算 |
| HealUserDependingOnSandstorm | 恢复求值时有效沙暴 R(2H/3)，其它 R(H/2) |
| HealUserHalfOfTotalHPLoseFlyingTypeThisTurn | R(H/2) 后设当轮羽栖真；类型查询与尾清由《战斗类型、命中与伤害计算》/战斗结果规格，不永久删除个体飞行类型 |
| CureTargetStatusHealUserHalfOfTotalHP | 不可抢夺、可反射；仍有 U 满 HP 的共同整招失败；T 真实异常无则失败。逐目标先治 T 异常，随后全局主要效果恢复 U R(H/2)，不因 T 只「视为异常」成功 |
| HealUserByTargetAttackLowerTargetAttack1 | 吸取力量：局部前门在非模式破坏且 T 有效反向时只拒攻＋6，否则拒攻−6；其它免降能力不自动令整招失败。先取 T 攻×其攻击阶级并向下取整为量，再尝试降攻 1；之后 T 有效 LIQUIDOOZE（允许濒死）则 U 扣该量并检查恢复物品，否则 U 可恢复才按有效 BIGROOT ×1.3 向下取整再恢复。降攻不成功仍可回血；倍率不含 T 巨大力量等攻击倍率 |
| HealUserAndAlliesQuarterOfTotalHP | 整招要求当前同侧至少 1 名可恢复；逐目标不能恢复则跳；实际恢复总 HP 整除 4 |
| HealUserAndAlliesQuarterOfTotalHPCureStatus | 整招只需同侧至少 1 名可恢复或有真实异常；逐目标两者皆无才跳；先能恢复则整除 4，再有真实异常则治疗。不是只治睡眠等某一种 |
| HealTargetHalfOfTotalHP | 可反射；先满 HP 拒、再不可恢复拒；请求 R(T.H/2)，若本招波动标记且 U 有效 MEGALAUNCHER 则 R(3T.H/4) |
| HealTargetDependingOnGrassyTerrain | 同上述目标门、可反射；当前青草场地 R(2T.H/3)，其它 R(T.H/2)，**没有目标或 U 接地门** |
| RandomlyDamageOrHealTarget | 本次初始化 r0..99：0–39 基底 40，40–69 为 80，70–79 为 120，80–99 是治疗；治疗分支非实际伤害，T 不可恢复失败，否则总 HP 整除 4。保留数据伤害分类下其它前门，不自动改变化招；本分支不进入通常宝石伤害消费 |
| HealAllyOrDamageFoe | U 治疗封锁正时目标种类改近对手；本次初始化按首目标是否同侧保存治疗模式。同侧模式拒未绕替身或不可恢复目标，恢复 T 总 HP 整除 2；对侧按普通伤害。无首目标治疗标志假，不执行强制恢复 |

### 6.2 吸取

HealUserByHalfOfDamageDone／HealUserByHalfOfDamageDoneIfTargetAsleep／HealUserByThreeQuartersOfDamageDone 各次实际主要效果在 hpLost>0 时请求 R(hpLost/2)／R(hpLost/2)／R(3hpLost/4)；食梦型目标必须视为睡眠，别的状态不算，COMATOSE 可参与。世代 ≥6 才有治疗招标记，因此治疗封锁的使用资格世代分支保留。

共享吸取先查目标 LIQUIDOOZE 有效（允许濒死，仍有压制门）：有则直接把上述请求量作为 U 损失，检查 U 恢复物品；没有才在 U 可恢复时，有效 BIGROOT 把请求 ×1.3 再向下取整、中央恢复。这里不把模式破坏者自动加到液体污泥门。替身损失可作为 hpLost，不从「吸生命」名字自行排除；满 HP 通常不妨碍伤害发生，只不产生恢复。每击反应可能先使 U 倒下，普通恢复门拒，污泥分支不保证取消其它已提交状态。

### 6.3 位置、持续和未来攻击接点

| 身份 | 建立与消费责任 |
| --- | --- |
| HealUserPositionNextTurn | 位置祈愿正计数时失败，否则置 2、保存 R(U.H/2) 和 U 队伍索引；以后当前占位者获保存量。建立时不要求 U 缺 HP；计时与空位早退归场域/战斗结果规格 |
| StartHealUserEachTurn | 水流环已有真失败，否则真；回合末可恢复者请求总 HP 整除 16，有效 BIGROOT 再 ×1.3 向下取整 |
| StartHealUserEachTurnTrapUserInBattle | 扎根同样重复失败/建立和回复；拘束与接地沿换人/《战斗类型、命中与伤害计算》，实际回合末顺序在水流环之后 |
| StartDamageTargetEachTurnIfTargetAsleep | 要求 T 视为睡眠且噩梦未真；建真，残余按战斗结果规格先重查睡眠/清除，合格间伤为总 HP 整除 4 |
| StartLeechSeedTarget | 可反射；已有种子指向 ≥0 或 T 草类型失败，命中失败有专属反馈；建 U 席位为受益位置。回合末要求受害者可受间伤、该席有存活者，先扣受害者总 HP 整除 8，按实际损失对受益者吸取（含污泥/BIGROOT），再相应跨半/濒死反应；不同个体可以占来源席获益 |
| AttackTwoTurnsLater | 设置回合不是实际伤害且自己的命中检查真；同位置已正倒计时拒，否则记 3、本招身份、U 席/队伍索引；命中/类型门仍按当前入口区分。到期由战斗结果/场域规格解析当前来源/dummy 并临时未来攻击标记作简单使用；不再重复设标记，仍用当前调用的计算数据，不保存最初伤害值。空位/来源不可用及默认守卫见场域规格，不保证延迟必定落地 |

## 7. 反伤、自损与同归

| 身份 | 何时/用何值/失败与守卫 |
| --- | --- |
| RecoilQuarterOfDamageDealt／RecoilThirdOfDamageDealt／RecoilHalfOfDamageDealt | 逐目标所有击后，T 未 unaffected、U 可受间伤且无有效 ROCKHEAD 才按该 T 的 totalHPLost 取 R(1/4／1/3／1/2)，最少 1，中央扣 HP 后检查恢复物品；不是每击单独向上补 1 |
| RecoilThirdOfDamageDealtParalyzeTarget／RecoilThirdOfDamageDealtBurnTarget | 同 1/3 反伤；另在每击数据附效机会下尝试麻痹/灼伤，替身挡附效。防反伤不自动禁止目标附效 |
| Struggle（特殊内建动作） | 无类型物理 P50、命中 0、PP−1、近随机对手、接触和可保护标记；所有击后 T 未 unaffected 就损 R(U.H/4)，不检查 MAGICGUARD/ROCKHEAD；恢复物品随后检查。使用入口仍按命令规格，不能统括免检查 |
| CrashDamageIfFailsUnusableInGravity | 被标为反伤、重力不可用；实际坠落在该击无任何目标成功且不准空目标时，U 可受间伤才损总 HP 整除 2 → 恢复物品 → 濒死。普通 ROCKHEAD 不能拦此路径；不能将更早整招前置失败一律加坠落 |
| UserLosesHalfOfTotalHP | 所有击后每原目标调用，U 可受间伤才损 ⌈H/2⌉、至少 1，检查恢复物品；无 unaffected 门，即使目标无效/失手也可损；但更早整招返回或空目标无此逐目标后置时不凭名称保证自损 |
| UserLosesHalfOfTotalHPExplosive | 可空目标；整招模式破坏者假且全局 DAMP 有效就失败。第 1 击自损位置若 U 可受间伤请求 R(H/2)，恢复物品；不是普通反伤、不查 ROCKHEAD。允许空目标仍有先前使用门 |
| UserFaintsExplosive | 可空目标、强制 1 击；同 DAMP 门；到第 1 击自我失能时 U 存活则扣当前全 HP 并检查恢复物品，随后正式濒死，目标伤害 HP 已提交；不是先自灭再算目标伤害 |
| UserFaintsPowersUpInMistyTerrainExplosive | 同自爆；当前薄雾场地基底 ⌊3P/2⌋，不加接地条件 |
| UserFaintsFixedDamageUserHP | 见 §4 保存 U 起用 HP；不允许无有效目标硬做效果；第 1 击提交目标后扣当前全 HP。免疫/完全失败可在自灭前退出 |
| UserFaintsLowerTargetAtkSpAtk2 | 请求目标攻−2 → 特攻−2，局部目标失败检查特意不以无法降阶拒绝；可到自灭即扣当前全 HP，之后中央逐项资格，可能两项都不变。其它保护/免疫/无目标门不被这个局部返回取消 |
| UserFaintsHealAndCureReplacement／UserFaintsHealAndCureReplacementRestorePP | 治疗/可抢夺，先有可选非在场成员才准；第 1 击自灭扣 U 全 HP 后设本位置治愈之愿/新月舞。实际换入前消费顺序、世代 8 无可用效果可保留、PP 恢复差异用场域规格，不在此强行即时换人 |
| StartPerishCountsForAllBattlers | 若目标列表全部已有正灭亡计数整招失败；逐目标已有正则跳，否则设 4 并保存 U 为来源，作用集合与隔音免疫沿实际目标/《特性参与计算、免疫与有效性》；自然计时/倒下/裁判由战斗结果规格，不保证来源离场后取消 |
| AttackerFaintsIfUserFaints | 世代 ≥7 上次行动前保存的同命 Previous 真则重复失败；成功设同命真。下一行动开始保存 Previous 并清当前真；被对侧命中致倒下先记录来源，全部击后才扣仍活 U 全 HP、濒死/裁判。不是任何间接倒下都反杀 |
| SetAttackerMovePPTo0IfUserFaints | 建怨念真，下一行动开始清；对侧招式每击后 T 怨念且倒下时把实际使用招式 PP 置 0，经《HP、状态、招式与持物》/命令规格决定是否写回真实槽。阶段早于同命，不用「同归发生」作 PP 清零前提 |

## 8. 配置、默认数据与有界场景

当前世代 8，普通随机伤害/会心等默认沿《战斗类型、命中与伤害计算》；各表的旧代差异仅按明确条件，不承诺完整历代复刻。数据决定 P、命中、附效率、目标和可保护/接触/反射等标记，效果标识本身不能替代这些输入。静态样本：TRIPLEKICK P10/q90；DRAGONDARTS P50/q100；SCALESHOT P25/q90；BEATUP P1/q100（实际 P 被覆盖）；PRESENT P1/q90；POLLENPUFF P90/q100；REST 变化/q0；SHEERCOLD q30，功能 OHKOIce；FINALGAMBIT P1/q100；MINDBLOWN P150/q100／STEELBEAM P140/q95；SOLARBEAM P120/q100；WATERSHURIKEN P15/q100；DRAININGKISS P50/q100。目标和概率应按实际数据，不预设所有同族技能相同。

## 9. 示例场景与测试目录

静态场景（无未列能力/物品/条款；固定输入，手工状态推导和独立常数数学，不执行参考处理器）见测试目录 [`../test-catalog/pokemon-rules-wp43-44-46-48-50.md`](../test-catalog/pokemon-rules-wp43-44-46-48-50.md) 的 MH01–MH38（多击十组（2–5 击抽取、三连踢失手、替身累计、定身/睡眠停止、龙箭、围攻、太阳光束、香草、暴走、滚动）、固定伤害四组（随机等级、削半、反击、忍耐放出）、威力十组（电球、低 HP 威力、陀螺球、王牌、地下青草、吸取力量、蓄力两组、Flying Press、类别平手）、恢复八组（半恢复/REST/净化/吸取 BIGROOT/污泥/PRESENT/花疗/祈愿）、反伤同归六组（普通反伤/STEELBEAM/自爆/FINALGAMBIT/同命/连携场域））。

## 10. 依赖、前向与新观察

- 基础公式/命中/会心（《战斗类型、命中与伤害计算》）；状态/阶级中央资格（《异常状态、能力阶级与免疫》及其覆盖附表）；场域生命周期（场域规格）；命令/PP（命令规格）；换人（换人规格）；主阶段/终局（战斗结果规格）；能力计算（《特性参与计算、免疫与有效性》）；阶段触发（阶段触发规格）——均已限定通过。
- 招式变更两规格承接一般目标重定向、调用/复制、类型改变和排除表；本文件龙箭的目标差异及誓约协作/伤害合同已给出。《持有物计算、触发与消耗》具体物品族完成时复核香草/根/宝石/恢复物的连锁；《Mega、Primal 与显式还原》、《Shadow》、《捕获判定与接收策略》、AI/设施和 demo 及出口仍保留。
- 本次具名快照差异：围攻实际包含 U；龙箭第一发目标倒下不保证第二发；喷出对侧全灭会留下蓄力记录；誓约场域后置不统一要求目标有效。均从实际正文/调用读得，不用百科纠正，也未运行验证。

## 11. 未决与未验证

1. 完整物品处理器连锁（香草/根/宝石/恢复物）——归《持有物计算、触发与消耗》。
2. 多目标＋多击自定义组合的消息模板覆盖（未保证所有排列）。
3. 新临时组合、真实运行、AI/设施组合与阶段出口（U01 类保留）。
