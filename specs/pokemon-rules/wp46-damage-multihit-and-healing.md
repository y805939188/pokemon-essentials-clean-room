# WP46 — 多次攻击、特殊伤害与恢复

B10 当前修订提案：本次新增/修正条款及测试连接尚待独立复审，不能继承下文旧版本的 PASS_SCOPED；旧首审及后继历史保留，仍无运行确认。

状态：**Reviewed（限定静态范围，2026-09-27首审PASS_SCOPED；管理性回填）**。日期2026-09-27；F12-04，Pokémon Rules／Combat Requirements。只读基线commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，无参考执行或运行确认。

## 1. 目的、边界与共同输入

本包描述一次使用内多击、跨回合伤害、替代普通伤害／改变输入、吸取／反伤／治疗及代价怎样形成可见结果。A为共同调用与数据，B为多击／蓄力／连用，C为固定伤害／反击，D为威力／类别／能力值特例，E为恢复／吸取／持续效果，F为自损／同归与失败。覆盖表逐个给实际效果标识和责任；源码名称仅审计，不规定未来API、类层次或文件布局。

基础公式、类型、普通命中和会心主规则在WP43；状态／阶级中央资格与写回在WP44；位置／场域生命周期在WP45；命令／PP及调用标志在WP40；主阶段与终局在WP42；能力计算／生命周期在WP48／49。这里只写该族的替代和具体请求。完整物品处理器WP50、完整个体变身WP22、Shadow WP23、AI／设施／运行／Demo及WP78→79→80均保留。

记U为本次实际使用者、T为实际目标，h/H为当前／总HP，L为等级，P为数据威力或本族给出的基底，R(x)为正数四舍五入（恰半向上），⌊x⌋为向下取整，⌈x⌉为向上取整。速度／重量均为当时查询结果，含已审能力等修正，不能以裸属性替代。输入还包括当前类型、能力／物品有效性、阶级、选择、使用记录、上轮失败、伤害状态、世代开关和PBS标记。输出分为计算伤害、计划／实际损失（可含替身）、HP与状态写回、持续标记／计数、决定、消息和等待，不以一个“成功”概括。

## 2. 整次使用、每击与中断（A）

### 2.1 实际消费者顺序

前置使用资格／服从性→普通使用扣PP→本次类型／模式破坏者／两回合状态→使用计数和记录→目标寻找／改变及压力／整招阻止→本招整次失败检查→本次初始化（如随机威力、类别快照）→其它前门／变类型／快速蓄力→无目标门。详细位置以WP40已审合同为准，失败位置不同，前面已扣PP或消耗道具不自动退回。

目标集确定后，逐目标整次检查一次：重置跨击状态、计算相性、目标特例／保护／反射／免疫等；不通过者记unaffected。蓄力回合在计算相性后提前通过该层，不在此检查全部普通目标门。然后决定计划击数。

每击入口先拒U倒下，执行本击初始化、亲子爱计数−1。第1击或明确“每击命中”的族才做半无敌／命中检查；有目标列表却无一目标成功且不允许空目标时提示、失手物品、坠落自损、取消连用并返回假。正常续击不把所有保护／类型免疫／状态资格再跑一遍。第一击确定的相性、unaffected和跨击总损失不会被每击重置。

本击选取要打的目标后，重置本击calcDamage／hpLost／会心／替身／耐受等；逐有效目标重新查询吸收、计算伤害／会心及当时攻防与倍率、规划损失；展示本击招式／宝石使用提示，然后提交各目标HP（替身只扣耐久）。接着第1击的自我失能／自损入口→U濒死→记录伤害→伤害当下副效果（如溅射）→每击能力／物品反应→耐受和破皮提示→全场恢复物品与濒死→裁判检查点→逐目标主要效果（含吸取）→全局主要效果→濒死→附效与额外畏缩→减伤果消耗→蒸汽机等→再濒死。顺序沿WP49，不能改为“所有吸取先于反伤反应”。

每成功击后实计击数＋1；U倒下、真实睡眠／冰冻、全部目标倒下时停止；处理中定身不阻止剩余击数。其它异常或能力变化仍通过后续实际消费者生效，不能自行增加每击服从／PP检查。随后逐原目标执行本招“所有击后”处理，即使本次击数0也可能到达（前提没有更早整招返回）；本地unaffected守卫各不相同。再按WP49整招后置（同命、U能力、物品／退出等）和WP42成长／裁判。没有每次写决定就立即打断所有嵌套回调的统一保证。

替身破坏后下一击重新查吸收，可伤真实HP；每击能力值／HP／物品可变，但本次类型通常更早固定，相性来自整次目标检查。固定伤害也经过吸收和留1等HP限制；亲子爱的普通威力减幅不施加到绕普通公式的固定值。新临时组合没有真实运行验证。

### 2.2 计量、取消与可见失败

- hpLost为本击经截断的实际计划损失，可含替身；totalHPLost是同目标跨击累计；普通反伤读后者，吸取读前者。不能以计算伤害替代二者。
- 常规扣HP／回HP写持久个体，金额先R、夹到可损失／可恢复值；存活损失请求<1至少1，缺HP恢复请求<1至少1。canHeal另拒倒下、满HP、治疗封锁；中央恢复本身不自动重跑这份资格。
- 可受间接伤害查询拒倒下和有效MAGICGUARD；ROCKHEAD是普通反伤的额外门，不能推广给所有自损。液体污泥吸取反损直接扣HP，没有通用MAGICGUARD门。
- 取消连用清两回合、滚动、暴走、吵闹、忍耐及连续切割；不清破坏光线休息。暴走剩1被非完全取消打断，若可自混乱仍会混乱。PP与specialUsage／skipAccuracyCheck两标志沿WP40：续回合不重新普通耗PP，但不因此成为统一必中。
- 消息／动画随实际门和击数出现。多目标＋多击自定义组合的消息模板未保证覆盖所有排列；当前PBS和源有限目录确认不等于任意扩展组合通过。

## 3. 多击、两回合与连用（B）

### 3.1 一次使用的击数

| 审计身份 | 完整本族合同 |
| --- | --- |
| HitTwoTimes | 计划2击；普通首击命中门，续击重算伤害／反应但不再次普通命中 |
| HitTwoTimesPoisonTarget | 同2击；每击按数据附效概率独立尝试普通中毒，替身挡附效，状态资格WP44 |
| HitTwoTimesFlinchTarget | 同2击；每击按数据附效概率尝试畏缩；被标为自带畏缩族，不额外叠物品同类畏缩抽取 |
| HitThreeTimesPowersUpWithEachHit | 初始化累计威力0；每次基底求值加一份数据P，普通单目标第1／2／3击为P／2P／3P；开始时SKILLLINK有效则关闭每击命中，其余三击分别检查，失手即止。不是把已完成的击撤销 |
| HitThreeTimesAlwaysCriticalHit | 固定3击；每击请求必会心覆盖，但幸运咒语／防会心等更早拒绝仍有效（WP43），不保证绝对会心 |
| HitTwoToFiveTimes | 先均匀抽0..19：0–6→2，7–13→3，14–16→4，17–19→5，即7/20、7/20、3/20、3/20。SKILLLINK有效时仍发生此次抽取，随后选末项强制5 |
| HitTwoToFiveTimesOrThreeForAshGreninja | GRENINJA形态2直接计划3、各击基底20；本分支不需再查BATTLEBOND有效性。不满足则上述2–5次数与数据P |
| HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1 | 2–5规则；所有击后对非unaffected目标先请求U防−1，再速＋1，各中央资格，可部分成功。顺序不是说明标题的“先升速” |
| HitOncePerUserTeamMember | 整招前收U业主队伍段内所有可战斗且真实状态无的成员，**包括符合条件的U**、不包括伙伴；空则失败。快照名单长度为计划次数，逐击按队伍顺序取一名，其物种基础攻击值b决定基底5＋⌊b/10⌋；仍用U普通伤害输入，不用参与者等级／攻击作整个伤害公式 |
| 普通招式的PARENTALBOND接点 | 有效亲子爱、当前是实际伤害回合、非蓄力族且目标列表长度1时默认计划2；明写击数的族按其覆盖。标记3，在两击各−1，第二击普通P倍率世代≥7÷4、旧代÷2；固定伤害绕普通倍率，不能说固定伤害第二击也按该分母减 |

HitTwoTimesTargetThenTargetAlly（龙箭）是两个发射过程，外层计划1、允许再发，而非普通multiHit。原列表恰1时，从原目标存活盟友中按可加目标／邻近规则找候选，多个时均匀选1加入；无候选保留原目标。首次对扩展列表做资格和命中检查，按未unaffected列表首目标发射，第二发取第二有效目标、无第二则重复第一。只有第一发所选目标在后段仍存活且非unaffected，才递归第二发；若它倒下，本快照不会仅因另一个候选仍活而保证第二发。递归入口也拒U倒下；第二发不普通重测命中。两候选均有效时失效消息可隐藏；全部无效只显示一次相关失手消息。WP48静默免疫不获吸收奖励的合同保留，完整通用重定向由WP47-A承接。

### 3.2 两回合共同合同

TwoTurnAttack、TwoTurnAttackOneTurnInSun、TwoTurnAttackParalyzeTarget、TwoTurnAttackBurnTarget、TwoTurnAttackFlinchTarget、TwoTurnAttackRaiseUserSpAtkSpDefSpd2、TwoTurnAttackChargeRaiseUserDefense1、TwoTurnAttackChargeRaiseUserSpAtk1、TwoTurnAttackInvulnerableUnderground、TwoTurnAttackInvulnerableUnderwater、TwoTurnAttackInvulnerableInSky、TwoTurnAttackInvulnerableInSkyParalyzeTarget、TwoTurnAttackInvulnerableInSkyTargetCannotAct、TwoTurnAttackInvulnerableRemoveProtections属于此有界族。

开始无两回合标记时确定蓄力；普通情形只蓄力不造成伤害，保存当前招式／两回合标记。已有标记时为攻击回合，并清两回合标记。有效POWERHERB可令同回合兼有蓄力与伤害：在目标资格检查前显示快速蓄力、执行各目标蓄力效果并消耗香草，然后才走后续失败／命中；后续失败不退香草或蓄力升阶。天空摔投完全不获香草收益。蓄力中普通目标资格和逐击命中在上述早门通过，但整招失败及更早阻止仍可生效；不从注释猜测全族相同效果次序。

| 身份／变体 | 具体差异、资格与状态 |
| --- | --- |
| TwoTurnAttack | 蓄力提示，下一轮普通伤害；无其它数值覆盖 |
| TwoTurnAttackOneTurnInSun | 首轮有效晴／大日照时直接兼蓄力与攻击、不开香草消耗；P末端倍率在有效天气非无／晴／大日照时÷2。无天气不减半，不按标题泛称“非晴皆半” |
| TwoTurnAttackParalyzeTarget／TwoTurnAttackBurnTarget | 攻击击按数据附效概率施麻痹／灼伤，替身挡附效，中央资格；不在蓄力时施加 |
| TwoTurnAttackFlinchTarget | 攻击击附效畏缩；自带畏缩标记；蓄力不因此先畏缩 |
| TwoTurnAttackRaiseUserSpAtkSpDefSpd2 | 既有两回合标记时其局部整招失败检查先返回不失败；否则至少一项可升才继续；攻击阶段依特攻＋2→特防＋2→速度＋2，各自资格、部分成功。实际无伤害类别，不复制为未来攻击算法 |
| TwoTurnAttackChargeRaiseUserDefense1／TwoTurnAttackChargeRaiseUserSpAtk1 | 蓄力效果分别防御＋1／特攻＋1；被后续攻击拒绝不回滚已升项 |
| TwoTurnAttackInvulnerableUnderground／Underwater | 蓄力半无敌身份分别地下／水下；命中豁免招式与倍率例外见§5和WP43 |
| TwoTurnAttackInvulnerableInSky／InSkyParalyzeTarget | 蓄力空中半无敌且重力不可使用；后者攻击附效麻痹、替身挡。重力／半无敌成功门按WP40，N01不扩为一律必中 |
| TwoTurnAttackInvulnerableInSkyTargetCannotAct | 天空摔投：不消耗香草；局部目标门拒同侧、未绕过替身、世代≥6查询重量≥2000、半无敌目标、蓄力时已有天空摔投、攻击时指向不是U的目标。蓄力目标标记指向U；T飞行类型的相性覆盖为免疫（不是所有浮空）；攻击所有击后清目标指向−1，该后置没有unaffected门。蓄力通用早门与实际攻击门分开，不能假定蓄力就跑全部此局部门 |
| TwoTurnAttackInvulnerableRemoveProtections | 蓄力消失半无敌；攻击实际主要效果清T碉堡／王盾／拦堵／守住／尖刺防守及T侧戏法／掀榻榻米／快速／广域防守，具体保护绕过还取决招式标记及成功层；不清挺住或其它任意标记 |

### 3.3 跨回合连用

| 身份 | 建立／消费／失败合同 |
| --- | --- |
| AttackAndSkipNextTurn | 实际全局主要效果设休息计数2、保存招式；WP40下一行动消耗休息，取消其它连用不清它。所有目标无效且逐击过程提前失败时不到该建立 |
| MultiTurnAttackPreventSleeping | 吵闹原计数0才设3、保存招式，速度序唤醒真实睡眠且无有效SOUNDPROOF的存活成员；重复正计数不重设。之后按WP42回合末递减、WP44阻睡；不套百科“隔音也受影响” |
| MultiTurnAttackConfuseUserAtEnd | 非unaffected目标且原暴走0时抽2或3各1/2并锁当前招式；每次所有击后正计数−1，归0且可自混乱则混乱。失败取消／舞者额外处理分别WP40／49 |
| MultiTurnAttackPowersUpEachTurn | 始用基底P；后续读滚动剩余计数c，使P×2^(5−c)，首次c0不加指数；变圆标记另×2。所有击后若目标有效且原c0设5，再正值−1；常规五次P、2P、4P、8P、16P，变圆再翻倍；计划1击不被亲子爱扩展 |
| MultiTurnAttackBideThenReturnDoubleDamage | 始用建立计数3、累计0、来源−1、锁当前招式，主要效果每次−1；计数1时放出，前两回合不伤害。累计每次伤害记录（含替身的本击损失）并更新最近来源；放出先尝试来源席位，不可加则随机存活对手（不要求邻近）；累计0或无目标整招失败且计数0，其它辅助字段不在这一步统一清。伤害为累计×2、至少1的固定伤害 |

## 4. 固定伤害、反击与伤害记录（C）

这些效果提供固定calcDamage、最少1并强制非会心，绕过普通P／攻防／本系／波动／威力倍率，却仍经过本次类型／能力免疫、保护、命中、替身／画皮／结冻头吸收和留1／实际HP上限。不是“固定伤害忽略全部规则”。

| 身份 | 固定量与局部拒绝 |
| --- | --- |
| FixedDamage20／FixedDamage40 | 固定20／40 |
| FixedDamageHalfTargetHP | R(T当前HP/2)；1HP给1，不是0 |
| FixedDamageUserLevel | U等级L |
| FixedDamageUserLevelRandom | 从⌊L/2⌋到⌊3L/2⌋的所有整数均匀抽取，含两端；可能生成0，随后固定值下限改1 |
| LowerTargetHPToUserHP | U当前HP≥T当前HP失败，否则差值T−U；明确计划1击；HP上限／替身可能令实际个体HP不等于U |
| OHKO | T等级更高拒；有效STURDY且模式破坏者假拒。命中专用阈值＝招式命中＋U等级−T等级，0..99严格小于，**不经过普通命中倍率表**；伤害给T总HP，仍有其它上层门和下层耐受 |
| OHKOIce | 目标失败门分入口。**原定义**先拒T冰类型，其后才走父类等级／坚硬门。**条款文件加载后且无后续覆盖**（该文件在该定义之后加载，依序重开父类与冰子类）：父类已保存的原目标检查可被继承，子类未另保存自身拒冰门；条款假时新目标检查走继承的等级／坚硬门，不再仅因T冰拒绝，条款真仍拒。命中入口独立：上述专用阈值在U非冰时再−10未改。效果标识对应的原实现没有局部世代门，PBS选择该标识和世代配置分开，不据注释擅自跳过。目标失败门通过不等于命中、击倒或整招成功 |
| OHKOHitsUndergroundTarget | OHKO并允许地下半无敌目标；不等于所有半无敌 |
| CounterPhysicalDamage／CounterSpecialDamage | 目标取最近物理／特殊伤害记录的来源席，必须与U对侧、可加入（不要求邻近）；无目标整招失败，不随机替补。固定值分别该记录×2，0至少1；记录初始−1通常无来源不进入 |
| CounterDamagePlusHalf | 用U最近对侧攻击者列表末项作目标，要求可加且对侧；无目标失败；固定值⌊最近对侧hpLost×1.5⌋、至少1 |
| UserFaintsFixedDamageUserHP | 初始化保存U当时HP，固定伤害取保存值、计划1；自损时扣当前全部HP，见§7，与随后回复／变化不能混同 |

伤害记录在每击反应前更新：非替身才写物理Counter或特殊MirrorCoat的当前损失与来源；忍耐累计不带替身排除。lastHPLost、受伤标志和来源列表分开：直接伤害标志要求正损失且非替身，普通受伤标志正损失即可，攻击来源列表可记录0损失的命中；对侧另记其最近损失／来源。旧按类型分类时觉醒力量的反击分类有一般类型强制输入；同一击的记录不代表整招累计。尾清／初始化沿WP42／WP41。

DamageTargetAlly：目标在伤害当下处理阶段，遍历其存活邻近盟友、可受间伤者扣各总HP整除16；先都扣再提示，再各自恢复物品。没有本地“目标本击非替身”门，不能据溅射名称附加；后续全场濒死／退出按WP49。溅射量不乘目标类型相性，也不当U直接命中那些盟友。

### 4.1 使用时机／记录限定的伤害招

这些局部失败发生在普通前置与扣PP之后，除明列选择门外不保证菜单时提前拒绝。

| 身份 | 局部准入／反馈 |
| --- | --- |
| FailsIfNotUserFirstTurn | U的在场turnCount>1时整招失败；没有把合法turnCount0也拒掉 |
| FailsIfUserHasUnusedMove | 逐当前U招式槽：必须含本招且至少另1招，所有其它身份都在U.movesUsed内；任一缺少则逐目标失败；不要求其它槽当前仍有PP |
| FailsIfUserNotConsumedBerry | 选择和使用时均查U已吃果记录，假拒；记录来源／持久口径沿WP20及WP47-B／WP50，不以“当前持有树果”代替已吃 |
| FailsIfTargetHasNoItem | T无当前物或物品不生效则逐目标失败；通过会显示该物正要发动的提示，show_message假也不抑制这段通过提示；不移除物品 |
| FailsUnlessTargetSharesTypeWithUser | U与T当前完整类型集合至少一交集才准，无共同类型逐目标无效 |
| FailsIfUserDamagedThisTurn | 回合蓄势提示先置FocusPunch真；只有该标记与本轮直接招式受伤标记都真才整招失败；特殊调用未设蓄势标记不能仅凭曾受伤直接拒绝 |
| FailsIfTargetActed | T须选UseMove且招式存在；除抢先使用目标将用招的效果标识外，T已行动或所选变化招均失败。特殊例外不删除外层“必须选UseMove”门 |

## 5. 威力、类别和输入替代（D）

下表标“基底”在普通公式前替换P；标“P倍率末端／F末端”分别在WP43所有通用倍率之后的招式专用位置改威力倍率／最终倍率，不能任意换槽。基底按每次求值读取当前状态，明确初始化快照者例外。

### 5.1 数值输入表

| 身份 | 具体数学／条件 |
| --- | --- |
| PowerHigherWithUserHP | 基底max(⌊150×U.h/U.H⌋,1) |
| PowerLowerWithUserHP | n=⌊48×U.h/U.H⌋；n<2／5／10／17／33时依次200／150／100／80／40，否则20 |
| PowerHigherWithTargetHP | 基底max(⌊120×T.h/T.H⌋,1) |
| PowerHigherWithUserHappiness／PowerLowerWithUserHappiness | 基底max(⌊2×友好/5⌋,1)／max(⌊2×(255−友好)/5⌋,1) |
| PowerHigherWithUserPositiveStatStages | 七项正阶级之和s，负值不计，基底20×(1+s) |
| PowerHigherWithTargetPositiveStatStages | T七项正阶级和s，基底min(20×(3+s),200) |
| PowerHigherWithUserFasterThanTarget | 当时U速度整除T速度n；n≥4→150，≥3→120，≥2→80，≥1→60，否则40 |
| PowerHigherWithTargetFasterThanUser | 基底夹限⌊25×T速度/U速度⌋至1..150 |
| PowerHigherWithLessPP | 普通PP已先扣：剩PP0／1／2／3／≥4时基底200／80／60／50／40；不按使用前PP。负PP为特殊调用内部输入，若−1会取此表末项40；不推广任意非法负数兼容 |
| PowerHigherWithTargetWeight | 查询重量≥2000／1000／500／250／100依次120／100／80／60／40，否则20（重量单位沿数据，2000为200kg） |
| PowerHigherWithUserHeavierThanTarget | U重量整除T重量n≥5／4／3／2依次120／100／80／60，否则40 |
| RandomPowerDoublePowerIfTargetUnderground | 本次初始化均匀0..19，威力10／30／50／70／90／110／150权重1／2／4／6／4／2／1，同时显示震级4..10；整次共享随机基底。允许地下命中；地下目标F×2，当前青草场地F÷2，无接地附加门 |
| PowerHigherWithConsecutiveUse | 使用计数阶段先保留旧连续切割，通用清后加1至上限；上限是数据P逐次翻倍首次达到≥160所需次数（非硬夹最终P160）；基底乘2^(次数−1)。换招／失败取消可清，不能把未命中也算持续成功 |
| PowerHigherWithConsecutiveUseOnUserSide | 每侧每轮首次使用时旧回声计数＋1、最多5，设本轮已用；基底P乘该数；同轮多成员不再＋1，尾部若整轮未用才清（WP45／42） |

### 5.2 条件加倍与后处理

| 身份 | 实际门／槽／其它结果 |
| --- | --- |
| DoublePowerIfTargetHPLessThanHalf | T.h≤T.H整除2，基底×2 |
| DoublePowerIfUserPoisonedBurnedParalyzed | U视为毒／灼伤／麻痹任一，基底×2；世代≥6不受通常灼伤减伤，旧代仍受 |
| DoublePowerIfTargetAsleepCureTarget／DoublePowerIfTargetParalyzedCureTarget | T视为睡／麻痹且无替身或本招绕替身，基底×2；所有击后T存活、未unaffected、非替身且真实状态匹配才治对应状态；COMATOSE等视为状态不被治 |
| DoublePowerIfTargetPoisoned／DoublePowerIfTargetStatusProblem | T视为毒／任意状态且无替身或可绕替身，基底×2；不治疗 |
| DoublePowerIfUserHasNoItem | U无当前物品或本次GemConsumed标记真，P倍率末端×2；不只查物品有效 |
| DoublePowerIfTargetUnderwater | 可命中潜水，目标正在潜水时F末端×2 |
| DoublePowerIfTargetUnderground | 可命中挖洞，挖洞F末端×2；当前青草场地F末端÷2，无接地门 |
| DoublePowerIfTargetInSky／FlinchTargetDoublePowerIfTargetInSky | 可命中空中，T处飞翔／弹跳／天空摔投两回合或被天空摔投时基底×2；后者畏缩附效主合同WP44 |
| DoublePowerInElectricTerrain | 当前电场且T受场地影响，基底×2；是T门，不是U门 |
| DoublePowerIfUserLastMoveFailed | U上轮失败标记真，基底×2；不是本次已设lastMoveFailed |
| DoublePowerIfAllyFaintedLastTurn | U侧LastRoundFainted≥0且等于当前轮−1，基底×2 |
| DoublePowerIfUserLostHPThisTurn | U的lastAttacker列表含T席位，基底×2；实际记录可能含0损失，不能加“本次实际失HP>0”的不存在守卫 |
| DoublePowerIfTargetLostHPThisTurn | T本轮受伤标记真，基底×2，含间伤及替身所导致的记录差异依消费者 |
| DoublePowerIfUserStatsLoweredThisTurn | U本轮下降阶级标记真，基底×2 |
| DoublePowerIfTargetActed | T选择非None，且（选择既非UseMove也非Shift，或T已行动），基底×2；不以速度比较代替 |
| DoublePowerIfTargetNotActed | T选择None，或选择UseMove／Shift且未行动，基底×2；名义换入只是None的常见来源 |
| DoublePowerAfterFusionFlare／DoublePowerAfterFusionBolt | 使用计数先保存另一交错招标记，再通用计数清双方交错标记；保存真则本次P倍率末端×2，全局主要效果才设自己标记。中间普通使用也清标记，不能仅记同轮曾用过就永久加倍 |
| AlwaysCriticalHit | 请求会心覆盖1，仍在WP43早期不可会心门之后 |
| CannotMakeTargetFaint | 普通损失会致命时留下1，非满HP也适用；不防后续附效／残余／自损 |

### 5.3 类别、相性和攻防替代

EffectivenessIncludesFlyingType：每个防御类型的通常单项相性结果，另乘飞行类型对该防御类型的基础倍率；飞行身份不存在则不乘。数据的0／1／2／4先在基础相性查询中除以2成为0／1/2／1／2，本覆盖点相乘的是已归一倍率，不重复除以2。额外飞行项不重跑通常单项的标靶／识破／强风等例外；全局类型与HP门仍引用WP43，向量见D09。

CategoryDependsOnHigherDamagePoisonTarget：本次初始化只读首目标，按U攻／特攻和T防／特防各自阶级取整（防御读数受奇妙空间交换），比较物理攻击/防御与特殊攻击/特防的比值；大者决定本次类别，平手均匀两类。正常战斗用战斗随机，命令期预览用另一随机入口，不能保证统一种子；无首目标则保留该招对象当前类别（初始特殊）。不试算完整伤害或能力倍率。物理类别才带接触；普通毒附效沿WP44。

CategoryDependsOnHigherDamageIgnoreTargetAbility：只比U阶级后取整的攻与特攻，攻严格更大才物理，否则特殊，平手不抽；目标能力忽略采用IgnoreTargetAbility具名效果（WP47-B），不据注释断言所有不可忽略／生命周期能力失效。

UseUserDefenseInsteadOfUserAttack取U当时防御读数及防阶级作攻击输入，后续仍用攻击修正槽；UseTargetAttackInsteadOfUserAttack按实际类别取T攻及攻阶级／T特攻及特攻阶级作U攻击输入；UseTargetDefenseInsteadOfTargetSpDef取T防御及防階级。三者只替换值／阶级来源，后续会心、纯朴、能力倍率、灼伤等仍按WP43实际U／T规则，不能交换身份。前两者依赖物理／特殊配置，缺失类别数据归内容合同。

### 5.4 蓄力资源与誓约组合

UserAddStockpileRaiseDefSpDef1：已蓄力≥3整招失败；否则先蓄力＋1，再防＋1→特防＋1，各自资格；每项中央返回成功才把对应“由蓄力产生的记录次数”＋1（记录1不必等于最终实升量，单纯／反向另作用）。即使两项都封顶，蓄力仍可增加。

PowerDependsOnUserStockpile：0蓄力失败，基底100×蓄力；所有击后U倒下／蓄力0／目标unaffected均不清；到达后先提示效果消退，若目标侧队伍全灭则提前返回，**蓄力及记录仍保留**。其余按记录请求自降防、特防（各自资格），最后清三项记录0，不保证降阶数值还原为最初阶级。

HealUserDependingOnUserStockpile：0失败；不可恢复且两项记录都0也失败。1／2／3蓄力分别请求总HP整除4／整除2／总HP；进入主要效果后直接中央恢复，不再加canHeal门，先恢复再按上述记录下降并清三项；正常治疗封锁仍可能在更早使用资格拒绝此治疗招，不能据后段推出可绕过全局前门。

GrassPledge／FirePledge／WaterPledge：本次先看U保存的先誓约标记能否组合；否则扫描存活盟友，须选择UseMove且未行动、招式属于另一誓约，取首合格者等待。本次作为等待者不造成伤害，全局主要效果清自己先誓约、给伙伴标记本招身份及MoveNext真，自己记lastMoveFailed真。伙伴是否最后能行动仍由WP40处理，不能保证组合一定释放。

| 组合的两种誓约（先后皆可） | 后手实际类型／基底／场域 |
| --- | --- |
| 草＋火 | 火类型（对应类型数据存在才覆盖）、后手数据P×2，对侧火海 |
| 火＋水 | 水类型、后手数据P×2，本侧彩虹 |
| 水＋草 | 草类型、后手数据P×2，对侧湿地 |

类型在更早类型计算已根据标记处理，本次初始化确定组合并设置动画；各自同类型常规使用不是组合。场域所有击后处理只检查本次组合标志，**没有本地unaffected门**，因此已经进入组合而目标失败时也不能概括一律不建场。场域为0才设4，不刷新正期限；效果和回合末双递减等沿WP45。基本数据类型仍来自PBS，表的覆盖只在后手类型不同需替换时作数据存在性检查。

## 6. 治疗、吸取与持续建立（E）

### 6.1 即时恢复

普通自身治疗族可被抢夺，先满HP失败，使用资格中的治疗封锁门另在WP40；实际主要效果直接中央恢复并提示，不重跑一般canHeal。这包括下列前五行，净化另有目标前门。

| 身份 | 条件、请求量与次序 |
| --- | --- |
| HealUserFullyAndFallAsleep | 先拒U视为睡眠，再自睡资格（允许覆盖已有状态），再拒满HP；先自睡3计数（含本次循环的计数语义WP44），再请求全部缺HP。治疗能力可能在睡眠提交后立刻清睡，不回滚后续恢复 |
| HealUserHalfOfTotalHP | R(U.H/2) |
| HealUserDependingOnWeather | 本次初始化保存：有效晴R(2H/3)，无天气／强风R(H/2)，其它有效天气R(H/4)；随后使用此量，不按后来天气重算 |
| HealUserDependingOnSandstorm | 恢复求值时有效沙暴R(2H/3)，其它R(H/2) |
| HealUserHalfOfTotalHPLoseFlyingTypeThisTurn | R(H/2)后设当轮羽栖真；类型查询与尾清由WP43／42，不永久删除个体飞行类型 |
| CureTargetStatusHealUserHalfOfTotalHP | 不可抢夺、可反射；仍有U满HP的共同整招失败；T真实异常无则失败。逐目标先治T异常，随后全局主要效果恢复U R(H/2)，不因T只“视为异常”成功 |
| HealUserByTargetAttackLowerTargetAttack1 | 吸取力量：局部前门在非模式破坏且T有效反向时只拒攻＋6，否则拒攻−6；其它免降能力不自动令整招失败。先取T攻×其攻击阶级并向下取整为量，再尝试降攻1；之后T有效LIQUIDOOZE（允许濒死）则U扣该量并检查恢复物品，否则U可恢复才按有效BIGROOT×1.3向下取整再恢复。降攻不成功仍可回血；倍率不含T巨大力量等攻击倍率 |
| HealUserAndAlliesQuarterOfTotalHP | 整招要求当前同侧至少1名可恢复；逐目标不能恢复则跳；实际恢复总HP整除4 |
| HealUserAndAlliesQuarterOfTotalHPCureStatus | 整招只需同侧至少1名可恢复或有真实异常；逐目标两者皆无才跳；先能恢复则整除4，再有真实异常则治疗。不是只治睡眠等某一种 |
| HealTargetHalfOfTotalHP | 可反射；先满HP拒、再不可恢复拒；请求R(T.H/2)，若本招波动标记且U有效MEGALAUNCHER则R(3T.H/4) |
| HealTargetDependingOnGrassyTerrain | 同上述目标门、可反射；当前青草场地R(2T.H/3)，其它R(T.H/2)，**没有目标或U接地门** |
| RandomlyDamageOrHealTarget | 本次初始化r0..99：0–39基底40，40–69为80，70–79为120，80–99是治疗；治疗分支非实际伤害，T不可恢复失败，否则总HP整除4。保留PBS伤害分类下其它前门，不自动改变化招；本分支不进入通常宝石伤害消费 |
| HealAllyOrDamageFoe | U治疗封锁正时目标种类改近对手；本次初始化按首目标是否同侧保存治疗模式。同侧模式拒未绕替身或不可恢复目标，恢复T总HP整除2；对侧按普通伤害。无首目标治疗标志假，不执行强制恢复 |

### 6.2 吸取

HealUserByHalfOfDamageDone／HealUserByHalfOfDamageDoneIfTargetAsleep／HealUserByThreeQuartersOfDamageDone各次实际主要效果在hpLost>0时请求R(hpLost/2)／R(hpLost/2)／R(3hpLost/4)；食梦型目标必须视为睡眠，别的状态不算，COMATOSE可参与。世代≥6才有治疗招标记，因此治疗封锁的使用资格世代分支保留。

共享吸取先查目标LIQUIDOOZE有效（允许濒死，仍有压制门）：有则直接把上述请求量作为U损失，检查U恢复物品；没有才在U可恢复时，有效BIGROOT把请求×1.3再向下取整、中央恢复。这里不把模式破坏者自动加到液体污泥门。替身损失可作为hpLost，不从“吸生命”名字自行排除；满HP通常不妨碍伤害发生，只不产生恢复。每击反应可能先使U倒下，普通恢复门拒，污泥分支不保证取消其它已提交状态。

### 6.3 位置、持续和未来攻击接点

| 身份 | 建立与消费责任 |
| --- | --- |
| HealUserPositionNextTurn | 位置祈愿正计数时失败，否则置2、保存R(U.H/2)和U队伍索引；以后当前占位者获保存量。建立时不要求U缺HP；计时与空位早退WP45／42 |
| StartHealUserEachTurn | 水流环已有真失败，否则真；回合末可恢复者请求总HP整除16，有效BIGROOT再×1.3向下取整 |
| StartHealUserEachTurnTrapUserInBattle | 扎根同样重复失败／建立和回复；拘束与接地沿WP41／43，实际回合末顺序在水流环之后 |
| StartDamageTargetEachTurnIfTargetAsleep | 要求T视为睡眠且噩梦未真；建真，残余按WP42先重查睡眠／清除，合格间伤为总HP整除4 |
| StartLeechSeedTarget | 可反射；已有种子指向≥0或T草类型失败，命中失败有专属反馈；建U席位为受益位置。回合末要求受害者可受间伤、该席有存活者，先扣受害者总HP整除8，按实际损失对受益者吸取（含污泥／BIGROOT），再相应跨半／濒死反应；不同个体可以占来源席获益 |
| AttackTwoTurnsLater | 设置回合不是实际伤害且自己的命中检查真；同位置已正倒计时拒，否则记3、本招身份、U席／队伍索引；命中／类型门仍按当前入口区分。到期由WP42／45解析当前来源或补建离场来源的计算输入，以未来攻击标记作特殊使用。离场来源需要补建计算输入时，在复制该来源的当前个体数值之前，清理当前存活成员指向保存来源席位的着迷、紧咬不放、黑色目光、Octolock、天空摔关系；指向该席且计数正的锁定同时清计数和位置，指向该席的束缚同时清计数和来源但不在此清束缚招式身份。关系可能由仍在该席的替补刚建立，仍按席位清理。指向其它席位的关系不受影响；来源已经在场时没有这次额外交叉清理。此副作用在延迟攻击的伤害计算/资格结果之前已提交，后续落空或无效不回滚；无合格离场来源或目标不可用的更早返回不触发它。不再重复设标记，仍用当前调用的计算数据，不保存最初伤害值。空位／来源不可用及默认守卫见WP45，不保证延迟必定落地 |

### 6.4 HP 均分

`UserTargetAverageHP` 是从阶级效果覆盖表移交的独立 HP 合同（默认 PAINSPLIT），不改变阶级。以下前提为双方存活，已通过行动、PP、目标范围、保护和替身等普通前门；默认数据为变化招、命中 0，可被保护且未设忽略替身。

用进入本效果时两端当前 HP 一次求出 **m＝⌊(U.hp＋T.hp)/2⌋**。先处理使用者，再处理目标：当前 HP 高于 m 则减至 m，低于 m 则请求恢复到 m，等于 m 则不做这一端的 HP 增减；恢复各自受本端总 HP 上限限制。两端都用同一个 m，不在使用者提交后重算，不要求最终 HP 相等或合计守恒。恢复直接提交，不在此重查普通“可恢复”资格；本招本身没有治疗招标记，所以使用者只有正治疗封锁计数时仍可使用，不能据名称归入普通治疗门。目标未被绕过的替身或保护则在更早的目标检查阻止该效果，两种前提应分别做对照。

本次减少 HP 不新增普通直接招式伤害记录及本轮受伤/跨半标记，既有记录不因此清空；恢复若达到半 HP 会按共享 HP 恢复规则清跨半标记。HP 写入沿战斗参与者与其关联持久个体的既有写回合同。双方 HP 处理完成后仍显示均分反馈，然后先检查使用者、再检查目标的 HP 恢复物品；即使两端 HP 原本等于 m，这两个检查也不会因未增减而略过。物品有效性、资格、消耗与可能的后续连锁沿持有物规格，不能把检查请求等同无条件恢复；其结果可能继续改变 HP 和持久持物。

静态例：U 为 51/60、T 为 150/200，无影响本例的能力、物品或回调，m＝100，物品检查前及后都是 U60/T100，合计由 201 变 160。U1/T2、各总 HP100 得 m1，结果 1/1；两端各 50/100 且无有效物品时 HP 不变但仍有反馈和两端物品检查。完整正反例见净化测试目录 MH39–MH44（`../../deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md`）；这不是已执行行为测试。

## 7. 反伤、自损与同归（F）

| 身份 | 何时／用何值／失败与守卫 |
| --- | --- |
| RecoilQuarterOfDamageDealt／RecoilThirdOfDamageDealt／RecoilHalfOfDamageDealt | 逐目标所有击后，T未unaffected、U可受间伤且无有效ROCKHEAD才按该T的totalHPLost取R(1/4／1/3／1/2)，最少1，中央扣HP后检查恢复物品；不是每击单独向上补1 |
| RecoilThirdOfDamageDealtParalyzeTarget／RecoilThirdOfDamageDealtBurnTarget | 同1/3反伤；另在每击数据附效机会下尝试麻痹／灼伤，替身挡附效。防反伤不自动禁止目标附效 |
| Struggle（特殊内建动作） | 无类型物理P50、命中0、PP−1、近随机对手、接触和可保护标记；所有击后T未unaffected就损R(U.H/4)，不检查MAGICGUARD／ROCKHEAD；恢复物品随后检查。使用入口仍按WP40，不能统括免检查 |
| CrashDamageIfFailsUnusableInGravity | 被标为反伤、重力不可用；实际坠落在该击无任何目标成功且不准空目标时，U可受间伤才损总HP整除2→恢复物品→濒死。普通ROCKHEAD不能拦此路径；不能将更早整招前置失败一律加坠落 |
| UserLosesHalfOfTotalHP | 所有击后每原目标调用，U可受间伤才损⌈H/2⌉、至少1，检查恢复物品；无unaffected门，即使目标无效／失手也可损；但更早整招返回或空目标无此逐目标后置时不凭名称保证自损 |
| UserLosesHalfOfTotalHPExplosive | 可空目标；整招模式破坏者假且全局DAMP有效就失败。第1击自损位置若U可受间傷请求R(H/2)，恢复物品；不是普通反伤、不查ROCKHEAD。允许空目标仍有先前使用门 |
| UserFaintsExplosive | 可空目标、强制1击；同DAMP门；到第1击自我失能时U存活则扣当前全HP并检查恢复物品，随后正式濒死，目标伤害HP已提交；不是先自灭再算目标伤害 |
| UserFaintsPowersUpInMistyTerrainExplosive | 同自爆；当前薄雾场地基底⌊3P/2⌋，不加接地条件 |
| UserFaintsFixedDamageUserHP | 见§4保存U起用HP；不允许无有效目标硬做效果；第1击提交目标后扣当前全HP。免疫／完全失败可在自灭前退出 |
| UserFaintsLowerTargetAtkSpAtk2 | 请求目标攻−2→特攻−2，局部目标失败检查特意不以无法降阶拒绝；可到自灭即扣当前全HP，之后中央逐项资格，可能两项都不变。其它保护／免疫／无目标门不被这个局部返回取消 |
| UserFaintsHealAndCureReplacement／UserFaintsHealAndCureReplacementRestorePP | 治疗／可抢夺，先有可选非在场成员才准；第1击自灭扣U全HP后设本位置治愈之愿／新月舞。实际换入前消费顺序、世代8无可用效果可保留、PP恢复差异用WP45，不在此强行即时换人 |
| StartPerishCountsForAllBattlers | 若目标列表全部已有正灭亡计数整招失败；逐目标已有正则跳，否则设4并保存U为来源，作用集合与隔音免疫沿实际目标／WP48；自然计时／倒下／裁判由WP42，不保证来源离场后取消 |
| AttackerFaintsIfUserFaints | 世代≥7上次行动前保存的同命Previous真则重复失败；成功设同命真。下一行动开始保存Previous并清当前真；被对侧命中致倒下先记录来源，全部击后才扣仍活U全HP、濒死／裁判。不是任何间接倒下都反杀 |
| SetAttackerMovePPTo0IfUserFaints | 建怨念真，下一行动开始清；对侧招式每击后T怨念且倒下时把实际使用招式PP置0，经WP20/40决定是否写回真实槽。阶段早于同命，不用“同归发生”作PP清零前提 |

## 8. 配置、默认数据与有界场景

当前世代8，普通随机伤害／会心等默认沿WP43；各表的旧代差异仅按明确条件，不承诺完整历代复刻。PBS决定数据P、命中、附效率、目标和可保护／接触／反射等标记，效果标识本身不能替代这些输入。静态样本：TRIPLEKICK P10/q90；DRAGONDARTS P50/q100；SCALESHOT P25/q90；BEATUP P1/q100（实际P被覆盖）；PRESENT P1/q90；POLLENPUFF P90/q100；REST变化/q0；SHEERCOLD q30，功能OHKOIce；FINALGAMBIT P1/q100；MINDBLOWN P150/q100／STEELBEAM P140/q95；SOLARBEAM P120/q100；WATERSHURIKEN P15/q100；DRAININGKISS P50/q100。目标和概率应按实际数据，不预设所有同族技能相同。

以下无未列能力／物品／条款；固定输入，手工状态推导和独立常数数学，不执行参考处理器。

| ID | 输入／入口 | 期望 |
| --- | --- | --- |
| M01 | 2–5击r6／7／13／14／16／17 | 2／3／3／4／4／5；SKILLLINK有效也先抽再强制5 |
| M02 | 三连踢P10，前两击命中、第三击失手 | 已完成基底10、20两击，第三停止，不回滚前伤；SKILLLINK对照只首击命中检查 |
| M03 | 计划多击，首击T替身耐久10耗尽、真实HP100 | 首击只替身减10；次击重新查替身可伤真实HP，累计量包括10 |
| M04 | 首击诅咒之躯定身U本招／效果孢子令U真睡 | 前者不中止后续击，后者成功击返回后停止；不统一每击重查使用资格 |
| M05 | 龙箭原T和盟友T2都有效，第一发T倒下 | 第二发条件针对第一发实际所选T，倒下则不再发；不保证转向仍活T2 |
| M06 | 围攻业主队伍只有U合格，U物种基础攻109 | 名单含U，1击基底5＋10=15；伙伴不增加次数 |
| M07 | 续回合太阳光束，晴首轮／无天气／雨 | 晴同轮蓄力攻击且不消耗香草；无天气攻击不半威力；雨P倍率末端÷2 |
| M08 | POWERHERB有效、蓄力升防1招，后段目标保护 | 快速蓄力已升防／消耗香草，后段失败不回滚 |
| M09 | 暴走初选3，前三次完成 | 每次后计数3→2→1→0，归0可混乱；最后剩1遭取消也按已审取消门处理 |
| M10 | 滚动P30、正常连五次且变圆 | 基底60／120／240／480／960；不是数据P改写持久招式 |
| F01 | 随机等级伤害L1，原抽取0／1 | 固定值下限把两结果都变1；不保留0伤 |
| F02 | 削半固定伤害T.hp101／1 | R(50.5)=51／R(0.5)=1，再按替身／耐受实际限制 |
| F03 | 反击记录hpLost7，物理／金属爆炸 | 固定14／⌊10.5⌋=10；有有效目标和其它资格才应用 |
| F04 | 忍耐累计20，最近来源已倒下，另有可加入对手 | 放出改随机对手、固定40；无其它对手则计数清0失败 |
| D01 | 电球速度199／100与200／100 | 整数比1→60，2→80，不用浮点插值 |
| D02 | 低HP威力U.H100，hp4／5 | n1→200；n2→150，阈值是48比例的整数值 |
| D03 | 陀螺球T速度3、U速度100；或T1000/U1 | 基底1下限／150上限 |
| D04 | 王牌使用前PP2、普通扣1；特殊无槽PP−1对照 | 实算剩1基底80；−1内部输入取表末项40，不用使用前PP2的60 |
| D05 | 地下目标＋青草场地，地震／震级 | F末端×2再÷2相抵；不要求目标接地才减 |
| D06 | 吸取力量T攻击101、攻击阶级＋1、防降能力有效，U可治 | 先⌊101×1.5⌋=151，降攻可被拒但恢复仍可151；BIGROOT时⌊151×1.3⌋=196 |
| D07 | 双防封顶仍蓄力0 | 蓄力先0→1，两记录可仍0；喷出用100，吞下满HP且两记录0则失败 |
| D08 | 喷出成功击倒T侧最后成员，蓄力2、记录1／1 | 提示消退后早退，三记录仍2／1／1；不自动归0 |
| D09 | Flying Press本次格斗，对纯一般T；飞行数据存在，无单项例外 | 格斗基础倍率4/2=2，再乘飞行2/2=1，最终2；空类型不存在额外固定乘项 |
| D10 | 类别自适应毒招，阶级后物理／特殊攻防比相等 | 两类别各1/2；光子喷涌同样攻特攻相等则固定特殊，无平手抽取 |
| H01 | 自身半恢复总HP101、当前40 | 请求51、到91；生命水滴整除4请求25，不是同样四舍五入26 |
| H02 | REST满HP但真实中毒 | 因自身治疗满HP门失败，不自睡／不治毒；缺HP时先睡再恢复 |
| H03 | 净化U满HP、T真毒 | U满HP整招失败，不能先治T再宣称治疗成功 |
| H04 | 半吸取本击实际损失1，U缺HP，BIGROOT有效 | R(0.5)=1后⌊1.3⌋=1，不以原calcDamage为基数 |
| H05 | 液体污泥T已倒下仍有效，半吸取量20，U有MAGICGUARD | 此吸取污泥分支直接损20，不套普通间伤资格；其它HP上限仍适用 |
| H06 | PRESENT固定r39／40／69／70／79／80 | 40／80／80／120／120／恢复分支；恢复总HP101整除4=25 |
| H07 | 花疗T浮空、当前青草、总HP101缺足够HP | 无接地门，请求R(202/3)=67 |
| H08 | 祈愿来源H101，随后换入H200成员 | 到期请求保存的51，不重新按新成员总HP100；位置资格沿WP45 |
| R01 | 普通1/3反伤，T跨击总损失5，U可间伤 | R(5/3)=2；ROCKHEAD免；挣扎总HP101自损25不随此门 |
| R02 | STEELBEAM目标失手，进入所有击后，U.H101 | 可间伤时⌈50.5⌉=51；此前无目标整招跳过对应逐目标后置另算 |
| R03 | 自爆目标HP已扣到0，同时U还有100HP | 目标损失先写，U再损100并正式濒死，然后每击记录／反应／裁判；不是原子同时回滚 |
| R04 | FINALGAMBIT初始化U.hp61，T类型免疫 | 目标失败早于自灭入口，U不因名称必定自灭；成功对照固定61后扣U当时全部HP |
| R05 | 同命世代8本轮建立、下次行动仍选同命 | 开始行动保存Previous=true并清当前，再局部重复门失败；不是永久不能再次用 |
| R06 | 连携后手已识别组合、目标命中失败但到达所有击后 | 局部场域建立不查unaffected，可按原0状态设4；不把“击数0”当所有后效统一取消 |

## 9. 依赖、前向与新观察

以下已审版本完整固定；WP47-A/B已在本次独立首审限定通过；本稿仅维护已审身份，不改普通公式。

- specs/pokemon-rules/wp43-types-accuracy-and-damage.md：`d8ba547b3c1f8338f9f00fdac67c146ecd147942c94d576f77d27e4375cb905b`（30,921字节），已限定通过的当前版本。
- specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md：`3d4d9c40d83746459df0c89353a046abd8d4ca32e82e2de76e0ab44499273d1e`（50,426字节），已限定通过的当前版本。
- specs/pokemon-rules/wp44-effect-coverage.md：`c226232d523b899197590800b8e6f75230de103363eebf6c12a16111a24cb2ad`（27,346字节），已限定通过的当前版本。
- specs/combat/wp45-weather-terrain-side-and-position-effects.md：`046e8bf04fc663e41a6e48c3f9aaa193022d141fea39752eeb2db87a306bd597`（36,525字节），已限定通过的当前版本。
- specs/combat/wp40-commands-obedience-and-action-order.md：`8c80e5f3f4c3d6ad151bfa65c8a4fce5691adafb318b14565f89f929b24acbe8`（43,769字节），已限定通过的当前版本。
- specs/combat/wp41-switching-positioning-and-escape.md：`a5232a1ed18dc24257748c34b2ec83eca9730e2c8ef077c7be638ff3b4d38036`（33,281字节），已限定通过的当前版本。
- specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md：`126e2612e2776c41557475a98cd97b8ef40a0a7f02fd95f16c434de49855a3eb`（41,759字节），已限定通过的当前版本。
- specs/pokemon-rules/wp48-ability-calculation-modifiers.md：`1c701d507747d95ba456f3df8a2697b0a1e409d1508dd2d8651b7d50d102403c`（35,320字节），已限定通过的当前版本。
- specs/combat/wp49-ability-phase-triggers.md：`e41ca96da9f15bc88526f31337aefe3ba767b9b19776ceba0a6472df1061253c`（53,127字节），已限定通过的当前版本。

WP47-A承接一般目标重定向、调用／复制、类型改变和排除表；本包龙箭的目标差异及誓约协作／伤害合同已给出，不留在索引。WP47-B承接其它控制／物品／能力变化招式；IgnoreTargetAbility本包只消费其已审模式破坏者输入，完整触发写入由该包核对。WP50具体物品族完成时复核香草／根／宝石／恢复物的连锁；WP22、23、38、AI/设施和WP77及出口仍保留。发现与旧主规则的新反证须另登记，不静默改旧稿。

本次具名快照差异：围攻实际包含U；龙箭第一发目标倒下不保证第二发；喷出对侧全灭会留下蓄力记录；誓约场域后置不统一要求目标有效。均从实际正文／调用读得，不用百科纠正，也未运行验证。

## 10. 来源、覆盖与当前状态

实际文本读取（相对`Data/Scripts/`，路径／标识仅追溯）：

- `011_Battle/003_Move/009_MoveEffects_MultiHit.rb`1–633、`010_MoveEffects_Healing.rb`1–695全文；`008_MoveEffects_MoveAttributes.rb`1–642、675–695、1033–1221；`005_MoveEffects_Misc.rb`1–229、604–653；`012_MoveEffects_ChangeMoveEffect.rb`46–132、377–424、453–696；`007_MoveEffects_BattlerOther.rb`579–590。
- `004_Move_BaseEffects.rb`1–84、287–435、530–626；`002_Move_Usage.rb`1–125、165–237、258–415；`003_Move_UsageCalculations.rb`已审基础全文范围继承WP43，本轮定点336–349、467–485、1–80类型单项交界；`010_Data/002_PBS data/003_Type.rb`73–144基础倍率归一。
- `011_Battle/002_Battler/007_Battler_UseMove.rb`1–240、284–484、490–520、580–761；`009_Battler_UseMoveSuccessChecks.rb`1–29、290–327、409–454、500–603；`003_Battler_ChangeSelf.rb`1–67；`001_Battle_Battler.rb`513–530、592–605；`008_Battler_UseMoveTargeting.rb`173–204；`011_Battle/007_Other battle code/003_Battle_DamageState.rb`全文；`006_Battle_Clauses.rb`192–221仅N01定点回读（重开顺序与保存别名继承），不重开全条款行为。
- `011_Battle/001_Battle/001_Battle.rb`400–415业主队伍遍历；`011_Battle_EndOfRoundPhase.rb`79–126、140–204，本轮只核位置／持续接口、总序继承WP42；`002_Battler_Initialize.rb`检索两回合／蓄力／连用初值；PBS/moves.txt具名14项数据样本只读，不声称所有描述全文读取。
- 已审WP40／42／43／44／45／48／49相关主节和WP44覆盖附表；新批全目录身份集合和未归属责任在配套覆盖表。哈希／集合检查不代替行为阅读。地图／事件／演出与U01–U10未验证。

[有界效果覆盖表](wp46-damage-healing-coverage.md)（`549cd587095df207bf359c34fd66f14f2dda0c93ce1dcaec6bf4f63fc4d084c1`，36,824字节；本包附表已限定通过的回填版）列本包主合同、引用已有合同及域外责任。A～F及139项有界主合同按独立PASS_SCOPED管理性回填Reviewed；不宣称全部招式／物品／形态域或运行通过。

本轮批准：[独立首审报告](../../review/wp46-wp47-review-2026-09-27/report.md)§2／4；A～F／139项伤害与恢复主合同限定通过。本次状态回填、C01维护和必要身份级联分开记账；被审首稿`0e5a676e234a71a949602d93a2a6aeb4c26cf09acc894e47eee66eb3c1e8a323`（47,352字节）留史，该次管理回填的新字节不冒充原被审版本。运行、完整形态／物品／AI组合及阶段出口保留。

本次定点同步：2026-09-28 [WP52-B／C／WP54独立首审报告](../../review/wp52b-wp52c-wp54-review-2026-09-28/report.md)§4.1独立确认WP54-N01；§4 OHKOIce行已按授权区分原定义与条款加载后目标入口（来源补记于§10），WP43命中公式及本文件其它已通过范围不动；AI独立拒冰门与A专用命中估计不属本文件、未被删除。本次同步后当前字节不冒充此前被审对象；此前身份 `aa9a7f1e206275ce934a1bc3cf860813bafac852795a5d939316c6f5d9e8bf4c`（47,646字节）保留历史。运行、完整形态／物品／AI组合及阶段出口保留。
