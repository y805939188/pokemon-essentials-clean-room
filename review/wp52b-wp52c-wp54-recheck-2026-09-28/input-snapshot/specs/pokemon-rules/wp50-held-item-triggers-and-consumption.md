# WP50 — 持有物计算、触发与消耗

状态：**Reviewed（限定静态范围，2026-09-28有限复审PASS_SCOPED；管理性回填）**；范围A～F持物计算/有效性/普通与强制触发/消费写回及具名核心接点。2026-09-28；F08-05持有效果子范围，Pokémon Rules／Combat Requirements。基线commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，只读静态取证。

## 1. 目的、概念与范围（A）

A定义物品身份／有效性／消费返回；B计算；C恢复／状态／阶级；D受击／整招后段／退出；E环境／成长／回合末；F直接核心与失败、例子。可见输出是HP／PP／阶级、状态清除、速度顺序、道具提示／消失／转移、换入选择与结果。计算倍率、记录已触发、真正消费和战后还原分别记账。注册名仅追溯，不作为未来API／类结构建议。

C＝当前持物（写穿持久个体），I＝可更新还原记录，R＝回收记录，P＝拾取物／序号，Belch＝该个体本战吃果记录；主字段定义和招式转移由WP20／47-B，主动背包道具WP28／27，本包补被动处理器。HP／PP中央取整／上限引用WP20／43；等级／EV上限WP19／30；场域期限WP45；全阶段WP42；能力有效／连锁WP48／49。未运行、未实现框架、未将源码翻译为模型。

普通物品有效性拒倒下（显式允许倒下除外）、查封、魔法空间、按侧／队伍索引腐蚀、有效KLUTZ；身份存在性与有效性分开。普通能力的模式破坏门不统一作用于物品：命中、伤害和会心物品层不因模式破坏者跳过。特定消费中的能力／状态资格可另受该门。物种专属处理器看个体原物种；多数变身后仍可满足，金属粉／速度粉显式排变身。

## 2. 调用与提交层（A）

| 族／消费阶段 | 真实资格、顺序与返回用途 |
| --- | --- |
| SpeedCalc／WeightCalc | 拥有者普通物品有效；速度在能力之后、尾部统一四舍五入最少1；重量在能力之后，物品层不受模式破坏者门。无返回保持输入 |
| AccuracyCalcFromUser／Target | U能力与盟友／T能力之后，再U物→T物，核心重力／命中果等随后。修改命中参数容器，返回值不表示效果成功 |
| DamageCalcFromUser／Target | 各能力层后U物→T物→通用后置；P/A/D/F槽各自到WP43指定位置取整，不把P变成A或F |
| CriticalCalcFromUser／Target | 幸运咒语和能力更早；会心级非负且物品有效才读取。无返回保持级；目标族本快照空 |
| HPHeal／StatusCure／OnEndOfUsingMove／StatRestore | 普通helper先有效性；完整持物检查先HP→状态→使用结束（LEPPA优先，失败才WHITEHERB）→强制正向受击果。HP入口本身未先统括拒倒下，普通有效性会拒；显式强制身份可绕此门，但完整强制入口先拒倒下。各处理器仍有自己的可恢复／资格 |
| OnBeingHit | 每击calcDamage>0且非替身，能力／吐导弹／U击中能力之后T物；这里itemActive显式允许倒下，处理器按自身条件再拒。U失HP后可检查U恢复物品；不自动等待整招 |
| AfterMoveUseFromTarget／User | 招式拖出之后，WP49后段二；U有效SHEERFORCE且附效数据>0则整段不进入。目标须在原目标集、非unaffected、calcDamage>0且物品有效，速度序处理；U须未被换出且物品有效。之后才目标能力／跨半退出 |
| OnStatLoss | statsDropped真＋物品有效；入场最终扫描、招式后段、MOODY等具名点消费；返回是否退出影响“首个退出即停”／已换集合 |
| EndOfRoundHealing／Effect | WP42先青草→能力治疗→同成员物品治疗；后段先成员期限→能力效果→物品效果→能力取得物。每步重读有效性，非统一提前快照；决定正值只在主阶段具名点退出 |
| OnSwitchIn／TerrainStatBoost／OnIntimidated | 入场能力后物品，再持物检查；场地通知全能力后全物品；威吓后是否查道具由其消费者的预先许可决定，不要求实际降攻必成功。真返回才接通用已触发helper消费 |
| ExpGainModifier／EVGainModifier | 使用持久个体当前物品，**没有场上itemActive门**。经验无处理器返回−1，才查I；EV无登记返回假才查I，有登记即真。当前与I不叠两次；之后病毒／上限沿WP30 |

非计算通知不统一自动消费。返回真处理器由helper调用“已触发”后置：若传入物品为果且有效CHEEKPOUCH、可治，先请求H整除3；是自己当前物则普通消费；强制外来物不是自己物，不清自己的C，非投掷可共生。直接调用pbConsumeItem的物品绕颊囊通用层，按各条记。

普通消费先R=C、P=C及递增序号（可回收开），允许的树果设Belch；再清C、若C=I清I、无GORILLATACTICS清讲究锁、UNBURDEN有效置轻装，最后可共生。AIRBALLOON的不可回收消费不新写R/P，不等于清空先前R/P。退出包／按钮关闭消费时共生，红牌普通消费可先共生再检查是否拖出。C改变后后续helper读取当前物品，可能递归触发；没有通用一轮一次或事务回滚。正常终局读I还原的范围／显式中止不还原的风险沿WP42。

## 3. 计算修正（B）

### 3.1 速度、重量、命中、会心与档内顺序

| 物品／族 | 完整修正 |
| --- | --- |
| CHOICESCARF速度 | ×1.5；讲究锁另在WP40，不以倍率代替选择门 |
| IRONBALL／MACHOBRACE／POWERANKLET／POWERBAND／POWERBELT／POWERBRACER／POWERLENS／POWERWEIGHT速度 | ÷2 |
| QUICKPOWDER速度 | 原DITTO且未变身×2 |
| FLOATSTONE重量 | 整除2、至少1；输入已含临时重量与能力结果 |
| WIDELENS用户命中 | 命中倍率×1.1 |
| ZOOMLENS用户命中 | T选择不是UseMove／Shift，或已经行动时×1.2；None也满足前者，不用纯速度比代替 |
| BRIGHTPOWDER／LAXINCENSE目标命中 | 修改U命中倍率×0.9，不修改闪避阶级 |
| LUCKYPUNCH／LEEK／STICK会心 | 前者原CHANSEY＋2；后两原FARFETCHD／SIRFETCHD＋2 |
| RAZORCLAW／SCOPELENS会心 | 会心级＋1 |
| CUSTAPBERRY档内 | 普通低HP食果资格满足输出＋1；计算时不消费，实际采用物品档的攻击阶段提示才直接消费 |
| LAGGINGTAIL／FULLINCENSE档内 | −1 |
| QUICKCLAW档内 | 0..99<20输出＋1否则0；实际提示不消费。局部速度重算不重抽这份初始档，能力／物品档冲突WP40 |
| BLUNDERPOLICY失手 | 第1击才可触发，半无敌落空不触发，三个OHKO效果排除；U可升速才＋2并经已触发helper消费。不是所有整招失败都触发 |

普通命中仍先分别取整命中／闪避百分数，再整数q取商，r严格小于阈值；不重犯WP48 C06的浮点阈值错误。会心早期否决不会被＋级物品恢复。

### 3.2 威力／攻击／最终倍率

P威力、A攻击、D防御、F最终。附表完整列共享复制身份／类型映射，下面给不依赖名称推断的条件与量。

- 单类型P×1.2：BLACKBELT/FISTPLATE→格斗；BLACKGLASSES/DREADPLATE→暗；CHARCOAL/FLAMEPLATE→火；DRAGONFANG/DRACOPLATE→龙；HARDSTONE/STONEPLATE/ROCKINCENSE→岩；MAGNET/ZAPPLATE→电；METALCOAT/IRONPLATE→钢；MIRACLESEED/MEADOWPLATE/ROSEINCENSE→草；MYSTICWATER/SPLASHPLATE/SEAINCENSE/WAVEINCENSE→水；NEVERMELTICE/ICICLEPLATE→冰；PIXIEPLATE→妖精；POISONBARB/TOXICPLATE→毒；SHARPBEAK/SKYPLATE→飞行；SILKSCARF→一般；SILVERPOWDER/INSECTPLATE→虫；SOFTSAND/EARTHPLATE→地面；SPELLTAG/SPOOKYPLATE→幽灵；TWISTEDSPOON/MINDPLATE/ODDINCENSE→超能。
- ADAMANTORB：原DIALGA的龙／钢；GRISEOUSORB：原GIRATINA的龙／幽灵；LUSTROUSORB：原PALKIA的龙／水，均P×1.2。
- CHOICEBAND物理、CHOICESPECS特殊：**P×1.5**；MUSCLEBAND物理、WISEGLASSES特殊P×1.1。不按通行名称写成全部攻击槽修正。
- DEEPSEATOOTH原CLAMPERL特殊A×2；LIGHTBALL原PIKACHU两类别A×2；THICKCLUB原CUBONE／MAROWAK物理A×2。
- EXPERTBELT相性克制F×1.2；LIFEORB非混乱自伤F×1.3。生命宝珠扣HP在§5单独决定，增伤不等于必定扣。
- METRONOME F×(1＋0.2×min(连续计数,5))；计数建立／不同使用清理引用WP40，不擅自钳非法负计数。
- SOULDEW原LATIAS／LATIOS：当前“提升类型”设置真时龙／超能F×1.2；假且特殊招、无souldewclause时A×1.5。旧防御分支见下；不把开关简化为当前必永久禁用。
- 18类型宝石：BUGGEM、DARKGEM、DRAGONGEM、ELECTRICGEM、FAIRYGEM、FIGHTINGGEM、FIREGEM、FLYINGGEM、GHOSTGEM、GRASSGEM、GROUNDGEM、ICEGEM、NORMALGEM、POISONGEM、PSYCHICGEM、ROCKGEM、STEELGEM、WATERGEM各匹配本次对应类型；所有誓约族排除。匹配先记录GemConsumed=C，P×1.3（世代≥6）或1.5（旧代）；使用提示在首击，实际消费整招后段才做。多击消费前仍可反复参与本次计算，后续属性变化读真实当前值；不在查询第一刻从背包扣物。

目标计算：ASSAULTVEST特殊D×1.5；DEEPSEASCALE原CLAMPERL特殊D×2；EVIOLITE持久个体当前形态物种记录有至少一条有效后续进化（排前进化和方法None）则D×1.5，不先检查当下能否满足进化条件；METALPOWDER原DITTO且未变身D×1.5，两类别都可；SOULDEW在上述设置假、原双水都、特殊且无条款时D×1.5。

减伤果类型：BABIRI钢、CHARTI岩、CHILAN一般、CHOPLE格斗、COBA飞行、COLBUR暗、HABAN龙、KASIB幽灵、KEBIA毒、OCCA火、PASSHO水、PAYAPA超能、RINDO草、ROSELI妖精、SHUCA地面、TANGA虫、WACAN电、YACHE冰（各身份完整后缀BERRY）。本次类型匹配且相性克制才F÷2，一般果免克制门；有效RIPEN再÷2。**该helper没有食果／紧张感门**，但外层须T物品有效。立刻标本击berryWeakened并展示吃果动画，真消费在每击后附效／畏缩之后；下击可因已消费而无修正。替身／画皮普通伤害算法的早退以及不同伤害族WP43/46负责，不能以有动画保证T损HP为正。

## 4. HP、状态与阶级恢复（C）

食果资格canConsumeBerry拒对侧有效UNNERVE／复合紧张感。低HP资格先过食果；HP≤H整除4可；四分之一以上至H整除2时，参数false表示**半血门不要求GLUTTONY**，参数true（默认）才要求GLUTTONY有效。两种参数均不放宽到半血以上。普通持物有效性及各调用者的canHeal／阶级资格仍须满足；forced具体绕过哪些门按各条，不概括为忽略所有资格。

| HPHeal身份 | 量、门与返回 |
| --- | --- |
| BERRYJUICE | 必须canHeal；非forced还须HP≤H整除2；请求20恢复，真返回 |
| ORANBERRY／SITRUSBERRY | 必须canHeal；非forced用低HP资格false（半血及以下可，毋须GLUTTONY；仍须可食果）；请求10／H整除4，有效RIPEN先把已取整请求×2。恢复完成真 |
| FIGY／WIKI／MAGO／AGUAV／IAPAPA BERRY | 非forced要求canHeal及低HP资格，世代≤6传false，半血及以下毋须GLUTTONY；世代≥7传true，无有效GLUTTONY只四分之一及以下，有有效GLUTTONY可到半血。请求H整除3（≥8）、整除2（7）、整除8（≤6），RIPEN×2。对应嫌弃味道能力项分别攻击／特攻／速度／特防／防御，性格降低该项则提示并在可自混乱时混乱。forced不要求canHeal，中央夹限后即使回血0也可混乱并真返回；不要把强制满HP果说成绝不消费 |
| LIECHI／GANLON／PETAYA／APICOT／SALAC BERRY | 非forced低HP资格；中央可升才各请求攻／防／特攻／特防／速＋1，RIPEN请求翻倍；返回中央是否提交，封顶假 |
| STARFBERRY | 先收五项中央可升集合，空假；**先均匀抽项再进入低HPhelper**，即门最后拒也可能已有抽取。请求该项＋2，RIPEN变4 |
| LANSATBERRY | 非forced低HP资格；聚气已≥2假，否则直接设2并真。不走阶级＋2，也不因RIPEN自动设4 |
| MICLEBERRY | 非forced低HP资格；当前MicleBerry标记假则返回假，**原本真才保持真并反馈、真返回消费**。不将这处反向守卫按常见规则修正。普通命中消费已存标记会×1.2并清假（WP43） |

StatusCure：ASPEARBERRY冻、CHERIBERRY麻痹、CHESTOBERRY真睡、PECHABERRY真毒、RAWSTBERRY灼伤；非forced还须可食果，匹配才治疗并真。PERSIMBERRY混乱计数非0才清混乱；LUMBERRY真实异常或混乱非0才同时治状态／混乱，COMATOSE仅视为睡不当真实异常。治疗函数已写状态与计数不因后续提示失败回滚。

MENTALHERB不受食果门：迷恋、挑衅、安可、折磨、定身、治疗封锁至少一项有效才真；分别清，安可计数和招式身份都清，定身只清计数、没有在此清DisableMove辅助身份。不治地狱突刺或任意临时效果。WHITEHERB对七阶级所有负值直接归0、标本轮升阶真；无负值假；不逐项中央升阶、无反向／单纯等转换，正阶级不改。用后通用消费，两者都不是树果，不触发颊囊。

LEPPABERRY用**持久个体招式列表**收PP有损且总PP>0的槽，非forced仅有空PP槽可触发；forced可在无空槽时选首个部分损PP槽。都先空槽的首个，不按最低百分比或随机。非forced还查食果。请求10，RIPEN20，持久PP钳到上限，然后**直接把同下标战斗槽PP写成持久新值，不检查身份相同或变身**；与WP20通常专门同步入口不同，必须单列例外。当前真实招式不同也可能收到数值，不能由通用PP归属推断这次不回读；两赋值先后不原子。返回真才通用消费。

## 5. 每击、招式后段与换人（D）

### 5.1 受击处理器

共有外层calcDamage>0、非替身、允许濒死物品有效性。无另述的本地守卫不补造存活／模式破坏门；中央升阶或canHeal会拒倒下。受击物在能力反应之后读取，前序转物／失物可影响它。

| 身份 | 条件、请求与消费 |
| --- | --- |
| ABSORBBULB／LUMINOUSMOSS／CELLBATTERY／SNOWBALL | 分别水→特攻1／水→特防1／电→攻1／冰→攻1；可升才提交并通用已触发消费 |
| AIRBALLOON | 提示破裂，消费不可回收、允许共生，再显式共生检查一次；不要求本击实际hpLost>0，中央外层calcDamage门足够；浮空消失可影响后续击 |
| ENIGMABERRY | 非替身／非画皮／非冰脸且克制才转正向受击果helper；helper需canHeal，非forced须可食果，请求H整除4，RIPEN×2；真才通用消费 |
| KEEBERRY／MARANGABERRY | 物理／特殊命中分别转正向受击果helper，非forced食果门、中央可升防／特防，＋1或RIPEN＋2；真才消费。不被此层SHEERFORCE统一禁止，完整后段抑制是另一处 |
| JABOCABERRY／ROWAPBERRY | 可食果，物理／特殊招，U可间傷才损U总HP整除8，T有效RIPEN将已整除量×2，通用消费；不要求接触。T已倒下时它的RIPEN常规查询未必活跃，不能沿外层允许倒下扩大能力门 |
| ROCKYHELMET | 实际接触且U接触许可、可间伤，U损H整除6，不消费 |
| STICKYBARB | 实际接触且U接触许可、存活且无物：直接T.C→U.C、T.C清，T轻装有效置标记；野生战、U为玩家侧且U.I空、转物=T.I时转I并清T.I。不走消费、不写R/P，不统一立即触发新持物 |
| WEAKNESSPOLICY | 排画皮／冰脸，要求克制且攻／特攻至少可升一项；依攻＋2→特攻＋2各自资格、部分成功，之后通用消费；不因升一项而额外升另一封顶项 |

OnBeingHitPositiveBerry族只有ENIGMA／KEE／MARANGA，强制传入身份可绕上述“克制／物理／特殊”触发前门，但helper本身的canHeal／中央可升仍有效。返回真假决定颊囊等后置，不是仅动画标志。

### 5.2 使用后／退出

- EJECTPACK：消费者先降阶事件标记及物品有效；处理器拒天空摔投、对侧队伍全灭、野生拥有者、不能换出、没有后备；通过先消费（可回收、禁共生）。回合末只召回／离场并返回真，补位后做；其它时点才选替补，负值返回假但**已消费**，成功替换／清选择／按是否U清模式破坏／入场。不能把返回假当物品未扣。
- EJECTBUTTON：后段目标物入口，尚无已换席、对側未全灭、有后备才消费（禁共生）→选替补。**不检查普通换出拘束门**；负选择不回滚消费；成功替换／清选择／记已换／按U身份清模式破坏／入场。
- REDCARD：同入口，尚无已换且U活；先随机选U合格后备，无候选不消耗；再普通消费红牌（可共生），**随后**有效SUCTIONCUPS且非模式破坏或扎根可挡实际拖出。已耗不退；成功拖出U、清选择、记已换、模式破坏假、入场。不是野生终局逃跑处理器。
- LIFEORB后段U物：U可间伤、实际伤害招、击数>0且至少一个原目标非unaffected／非替身，损U总HP整除10→恢复物品→濒死；不消费。所有击最终替身标志／后段SHEERFORCE门可使有增伤却无此扣HP。
- SHELLBELL：U可恢复，累加每目标totalHPLost（含替身跨击量），正值则请求总和整除8。恢复达半可清跨半事件，随后危急回避可能不再触发；本快照未保留官方例外。不消费，不用总calcDamage。
- THROATSPRAY：双方参与队伍未全灭，声音招、实计击数>0且U可升特攻，＋1后直接消费；不是必须伤害类，局部无“伤害>0”门。

## 6. 场域、成长与回合末（E）

| 族／身份 | 合同 |
| --- | --- |
| WeatherExtender DAMPROCK／HEATROCK／ICYROCK／SMOOTHROCK | 当前新天气分别雨／晴／冰雹／沙暴时把正期限输入覆盖8，其它保持。消费者仅原有限期限>0、来源存在且物有效时查；不把强天气无限变8 |
| TerrainExtender TERRAINEXTENDER | 调到即覆盖8，但建立消费者同样只在有限期限和有效来源时查；不消费 |
| TerrainStatBoost ELECTRICSEED／GRASSYSEED／MISTYSEED／PSYCHICSEED | 当前电／青草／薄雾／精神匹配且中央可升：前两防＋1，后两特防＋1；**没有接地门**。真经通用消费；重复场地通知可能再查新物，不能说每通知都消费同一物 |
| OnSwitchIn AIRBALLOON | 只浮空提示；查询浮空在核心，不等于此提示永久建浮空标记 |
| OnSwitchIn ROOMSERVICE | 戏法空间计数非0且中央可降速（来源空）才速−1、直接消费；使用招式建立戏法空间后的全场检查另在WP49，也可触发；两入口并非只换入一次 |
| OnIntimidated ADRENALINEORB | 中央可升速才＋1，返回结果由helper消费。威吓原本失败仍可能到物品检查，实际消费者许可沿WP49 |
| EndOfRoundHealing BLACKSLUDGE | 当前毒类型且canHeal：H整除16恢复；非毒且可间伤：效果伤害H整除8，包含物品／退出／濒死嵌套。毒而满HP不改，不反伤 |
| 同族 LEFTOVERS | canHeal时H整除16恢复，不消费 |
| EndOfRoundEffect FLAMEORB／TOXICORB | 先按自己作为来源查可灼伤／可毒，实际提交不携来源，毒珠为剧毒；物品不消费；状态提交可引起治疗等重入，不能假设下一轮一定仍有异常 |
| 同族 STICKYBARB | 可间伤则效果伤害H整除8，不消费；接触转移见§5 |
| CertainSwitching SHEDSHELL | 输出真、WP41确定换出门早于拘束；不直接换人／不消费 |
| CertainEscapeFromBattle SMOKEBALL | 输出真，实际逃跑入口仍有战斗种类等先行门；不直接写决定／不消费 |
| ExpGainModifier LUCKYEGG | 当前收益×3整除2；无登记−1使消费者回看I。不是从第一个经验基数重新开公式 |
| EVGainModifier MACHOBRACE | 每能力收益×2；POWERANKLET速／POWERBAND特防／POWERBELT防／POWERBRACER攻／POWERLENS特攻／POWERWEIGHT HP增加8（当前开关）或4；之后病毒倍增／上限截断WP30。按注册有无返回是否处理，不依返回容器真假 |

## 7. 注册表外直接核心与边界（F）

不得以32族目录穷尽所有持物影响：以下已有主规则的直接检查继续保留，非本包遗漏的空操作。

| 物品／直接作用 | 唯一主规则／本包消费关系 |
| --- | --- |
| FOCUSSASH／FOCUSBAND | WP43§7满HP留1分支：披带保证一次后在提示处消费；头带10%且也在该快照满HP分支，不消费 |
| KINGSROCK／RAZORFANG | WP43额外畏缩10%，天恩或彩虹20%，鳞粉／自带畏缩／倒下／替身门；允许倒下的拥有者查询也不等于目标允许倒下 |
| ASSAULTVEST／三讲究物 | WP40选择／执行门，背心只命令阶段限制变化（抢先使用例外），讲究锁在结束行动记录；本包数值槽不能替代动作门 |
| IRONBALL／AIRBALLOON／RINGTARGET | WP43地面／飞行与相性；铁球先接地，气球浮空、破裂不恢复；标靶只改原免疫的单类型项 |
| SAFETYGOGGLES／UTILITYUMBRELLA／PROTECTIVEPADS | WP44/45/49：护目镜粉末和沙雹资格；伞使拥有者有效晴／雨及强版本为无；护具拒接触效果，不删除原接触标记或普通伤害 |
| BIGROOT／GRIPCLAW／BINDINGBAND／LIGHTCLAY／POWERHERB | WP46／47-B／45：根对具名恢复请求×1.3向下取整，束缚计数8／旧6及伤害分母，光黏土墙8，香草快蓄力先消费；已给具体主合同不重复设计 |
| DESTINYKNOT | WP44迷恋提交后在相应中央资格下反施给来源；不是每次“拥有迷恋”都循环反射；持物不消费 |
| HEAVYDUTYBOOTS | WP45入场危害：针对各危害具体门，毒类型吸毒菱等前序不因靴子一律跳过 |
| EXP.SHARE／AMULETCOIN／LUCKINCENSE及其它世界持物输入 | WP30成长分配／WP42奖金标记、WP20个体状态及WP28主动入口；本包不把背包EXPALL误作持物处理器 |

持物定义／Flags由WP03及WP47-A/B自然之恩／投掷／不可移物完整数据给定；复制登记只共享本族合同，不说明所有族一致。默认世代8、更多努力值开、心之水滴类型开；数据可以替换，未知身份查询通常无登记不改此层，但数据解析异常不承诺统一恢复。两空族CriticalCalcFromTarget、TrappingByTarget明确空；未发现脚本其它文件追加此注册目录，AI读取不作真实处理器证明。

## 8. 静态场景与向量

普通数值例沿WP43共同前提L50、P60、攻防100、非会心、中性、无本系／其它修正、最大随机，基准28；只改变所列项。固定输入／手工状态推导，独立常数算术，不运行参考。

| ID | 前提 | 期望 |
| --- | --- | --- |
| V01 | CHOICEBAND物理，P60 | P90，普通伤害41；不是先把基础28×1.5得到42 |
| V02 | WIDELENS＋T BRIGHTPOWDER，q80、0阶 | 合乘0.99，命中整数99／闪避100，阈值79；r78命中、79失败 |
| V03 | FLOATSTONE输入重量101／1 | 50／1；模式破坏者不跳本物品层 |
| V04 | QUICKCLAW r19／20，局部重排 | 档＋1／0，后续局部重排不重新抽，仍可能被更高优先级超过 |
| V05 | 普通ORAN总HP100、HP26，可治可食且持物有效，无／有有效GLUTTONY，无其它连锁 | 两者均由false半血门通过，恢复10至36；HP25对照也通过至35，不能把false解释为关闭半血门 |
| V06 | SITRUS H101、HP25、RIPEN | 先101整除4=25再×2=50，HP25→75；不是R(101/2)=51 |
| V07 | FIGY世代8 H100、HP25，无RIPEN、性格降攻 | 请求33，随后可自混乱则混乱；forced满HP对照可0回血仍混乱、返回真 |
| V08 | MICLE低HP可食但标记假／真 | 假不触发不消费；真保持真并消费，后续命中才清标记和×1.2 |
| V09 | STARF五项仅速可升，但当前HP高于门 | 可先抽到唯一速，再helper拒低HP门，物品不消费；不是无抽取保证 |
| V10 | MENTALHERB只定身计数5、DisableMove=X | 清计数0，辅助身份X本地保持；不能声称所有字段都清 |
| V11 | WHITEHERB阶级攻−2／速＋3，其它0 | 攻0、速＋3，标升阶真；不是按中央＋2后再受单纯放大 |
| V12 | LEPPA持久槽X PP0上限20，同位变身槽Y PP5 | 持久X→10，战斗Y直接赋10；不按通常同身份同步门跳过本处理器 |
| V13 | 命中克制火，OCCABERRY有效且RIPEN、对侧紧张感 | 本helper仍F÷4并标果；不是食果门拒。消费在每击后另发生 |
| V14 | 宝石匹配多击，尚未到整招消耗 | 计算先标GemConsumed和P×1.3，首击提示、整招后才C清；誓约同物不触发 |
| V15 | ROCKYHELMET U.H101、可接触许可／间傷 | 扣整除6=16；T物外层允许倒下，不因T已HP0自动禁止 |
| V16 | WEAKNESSPOLICY攻＋6、特攻0且克制 | 攻不变、特攻＋2，然后消费；两项封顶则不消费 |
| V17 | REDCARD有候选，但U扎根 | 红牌先消费，再扎根拒换；不能将无换人解释成无消耗 |
| V18 | EJECTPACK已降阶且其它前门过，中途选择负值 | 先消费后返回假，原成员仍在；回合末分支只离场后等补位 |
| V19 | EJECTBUTTON拥有者被局部拘束但有后备、其它门过 | 本处理器不查换出拘束，仍消费并选换；与EJECTPACK有别 |
| V20 | SHELLBELL累计损失80、U.H100/HP45且跨半真 | 恢复10→55、跨半可清，之后危急回避未必退出 |
| V21 | LIFEORB伤害命中但最终各目标均本击替身 | 可能已增伤，但此后段hitBattler条件假，不损H/10 |
| V22 | 地形种子拥有者浮空、匹配当前场地且可升 | 仍升防／特防1并消费；没有接地门 |
| V23 | LEFTOVERS H15当前14 | 名义整除16=0，中央最低恢复1至15；满HP则前门拒 |
| V24 | LUCKYEGG当前收益101；POWER物对速基础1，开8，病毒加倍 | 经验151；速收益(1+8)×2=18，再按EV上限；不是先病毒后加8 |
| V25 | 成长成员魔法空间中持LUCKYEGG，真实收益入口已到 | 持久物品登记直接参与，不以场上物品失效删去奖励 |
| V26 | 退出包普通消费I等于C，R/P旧另有物 | 新R/P置当前包、I清、C清，共生禁止；气球对照不新写R/P但可共生 |
| V27 | BLACKSLUDGE毒类型满HP／非毒可间伤H101 | 毒无回复也不反伤；非毒扣12并走效果伤害反应 |
| V28 | THROATSPRAY变化声音招、实计1且双方队伍未灭可升 | 可升特攻1并消费，不添加伤害类门；强行后段总门仍要先到达 |
| V29 | 普通ORAN H100、HP50／51，可治可食且持物有效，无／有有效GLUTTONY，无其它连锁 | HP50均触发至60；HP51均不通过低HP门、不消费，GLUTTONY不扩大到半血以上 |
| V30 | 普通SITRUS H100、HP50，无GLUTTONY，可治可食且持物有效，无其它连锁 | false门通过，请求25至75，随后按普通成功后置消费 |
| V31 | 五混乱恢复果任一，世代6、H100、HP50，无GLUTTONY，普通有效可治可食，无其它连锁 | false门通过，请求100整除8＝12至62；Nature混乱及中央资格另查 |
| V32 | 五混乱恢复果任一，世代8、H100、HP50，无／有有效GLUTTONY，普通有效可治可食，无其它连锁 | true门使无贪吃者不触发；有效贪吃者通过，请求100整除3＝33至83；Nature效果另查 |
| V33 | 普通ORAN H100、HP26，canHeal且物品有效，对侧有效UNNERVE／无该阻碍，无其它连锁 | 前者先被食果资格拒，不触发不消费；后者半血门过并恢复至36；阈值修订不取消食果门 |

## 9. 依赖、证据与状态

- specs/creature-rpg/wp28-item-use-and-training.md：`a4ccb38365521eeb130b30d9e04a281812cd03ccc76ca5443393f5fbc352d95a`（44,159字节），已限定通过当前维护版。
- specs/pokemon-rules/wp43-types-accuracy-and-damage.md：`d8ba547b3c1f8338f9f00fdac67c146ecd147942c94d576f77d27e4375cb905b`（30,921字节），已限定通过当前维护版。
- specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md：`3d4d9c40d83746459df0c89353a046abd8d4ca32e82e2de76e0ab44499273d1e`（50,426字节），已限定通过当前维护版。
- specs/combat/wp45-weather-terrain-side-and-position-effects.md：`046e8bf04fc663e41a6e48c3f9aaa193022d141fea39752eeb2db87a306bd597`（36,525字节），已限定通过当前维护版。
- specs/creature-rpg/wp20-hp-status-moves-helditem.md：`05a59789554a4824121a852f05bf643f799b6e52af6837eb966c19cbec678d3c`（35,076字节），已限定通过当前维护版。
- specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md：`126e2612e2776c41557475a98cd97b8ef40a0a7f02fd95f16c434de49855a3eb`（41,759字节），已限定通过当前维护版。
- specs/combat/wp47-b-switching-control-and-item-changes.md：`007699019544203b9b5f4c42f18db8eb91711d2d96f6fa8afdf047d44b16e778`（39,000字节），必要身份级联后的当前维护版。
- specs/pokemon-rules/wp48-ability-calculation-modifiers.md：`1c701d507747d95ba456f3df8a2697b0a1e409d1508dd2d8651b7d50d102403c`（35,320字节），已限定通过当前维护版。
- specs/combat/wp49-ability-phase-triggers.md：`e41ca96da9f15bc88526f31337aefe3ba767b9b19776ceba0a6472df1061253c`（53,127字节），已限定通过当前维护版。

实际阅读：`011_Battle/007_Other battle code/009_Battle_ItemEffects.rb`1–1948全文；`002_Battler/006_Battler_AbilityAndItem.rb`213–476消费与全部helper（前1–212继承WP49）；`001_Battle_Battler.rb`248–287、421–456、495–613、664–696；`003_Move/003_Move_UsageCalculations.rb`126–164、177–204、290–340及WP43核心；`002_Move_Usage.rb`185–237、329–368；`002_Battler/010_Battler_UseMoveTriggerEffects.rb`1–47、138–218；`007_Battler_UseMove.rb`590–761具名消费点；`001_Battle/003_Battle_ExpAndMoveLearning.rb`57–77、146–159；`001_Battle.rb`686–719、786–813；`005_Battle_ActionSwitching.rb`35–71、350–368、429–468；`011_Battle_EndOfRoundPhase.rb`600–711总序继承WP42；`010_Data/002_PBS data/008_Species.rb`277–285核进化表过滤。其余核心直查按§7已审主规则继承，不冒称本次全文重读引擎。全Scripts登记检索无另一追加文件，PBS物品身份为数据证据，不执行。

[有界覆盖表](wp50-held-item-effect-coverage.md)（`f62603f26e7570e32949ebce97c531ef0af59ba6da4f083bff9d85775de2fc69`，14,418字节；本包附表已限定通过的管理回填版）把每登记／别名落到上述量值与消费合同。所有输出只静态确认，显示／素材／输入与真实运行仍未决；捕获、形态、Shadow、设施特殊组合、Demo／插件／U01–U10和WP78→79→80出口保留。LEPPA等具名路径是对通用同步入口的额外消费者，不自动重写旧WP20。A～F及32族／196身份有界范围按本次有限复审PASS_SCOPED管理回填Reviewed；完整运行与域外组合保留。

本次回源：AbilityAndItem:212–221、399–449；ItemEffects:364–404及五混乱果调用点265/296/310/340/438。默认true的阶级果、聚气／命中果与先制果门不变；恢复量／RIPEN、Nature混乱、forced满HP与后置消费合同不变。

本轮记录：2026-09-28 [独立首审报告](../../review/wp50-wp51-wp52a-review-2026-09-28/report.md)／[有限修订提示](../../review/wp50-wp51-wp52a-review-2026-09-28/revision-prompt.md)；WP50-R01参数方向与具体调用者／V05、V29–V33的v2修订已在本次有限复审CLOSED；附表当时为未变v1，本次只管理回填。被审首稿v1完整身份 `937551e00ec61a8a807bfa197ece1e2f91b6b5f91f620375e6c14ea900e9027a`（29,336字节）保留历史，当前新字节不冒充被审对象；其它已支持范围、运行未决与阶段出口保留。

本次闭合回填：2026-09-28 [独立有限复审报告](../../review/wp50-wp51-wp52a-recheck-2026-09-28/report.md)§3–4，A～F及32族／196身份的持物计算、有效性、触发与消费写回限定通过；本次只维护状态、排版与完整身份，行为及场景输入/期望不变。被审主稿v2 `fcbbca67dafbb1aaa1cfd2560983a6f34830c31c11feccb7688f08b372a395b1`（31,648字节）保留历史；当前新字节不冒充被审对象。运行及阶段出口继续保留。

本次必要身份级联：2026-09-28；§9仅更新WP47-B（身份级联后版）完整身份引用，行为与通过范围不变。本次维护后当前字节不冒充此前被审对象；此前管理回填版 `6c97afebe925f9cbe4aedfb1deb815b1d3277bd952ceae04e532887a16cd9627`（32,132字节）保留历史。运行及阶段出口继续保留。
