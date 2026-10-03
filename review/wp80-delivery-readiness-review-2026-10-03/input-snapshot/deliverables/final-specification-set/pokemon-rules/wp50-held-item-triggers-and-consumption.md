# 持有物计算、触发与消耗（净化正文；批次 7）

分类：Pokémon Rules／Combat Requirements。本文件定义物品身份/有效性/消费返回、计算修正、恢复/状态/阶级、受击/整招后段/退出、环境/成长/回合末、直接核心与失败。全部内容为静态取证；**无运行确认**（见 `../scope-statement.md`）。覆盖表：[wp50-held-item-effect-coverage](wp50-held-item-effect-coverage.md)（32 族/196 展开身份逐项归属）。

## 1. 目的、概念与范围

可见输出是 HP/PP/阶级、状态清除、速度顺序、道具提示/消失/转移、换入选择与结果。计算倍率、记录已触发、真正消费和战后还原分别记账。注册名仅追溯，不作为未来 API/类结构建议。

C＝当前持物（写穿持久个体），I＝可更新还原记录，R＝回收记录，P＝拾取物/序号，Belch＝该个体本战吃果记录；主字段定义和招式转移由《HP、状态、招式与持物》/招式变更-B 规格，主动背包道具归道具使用规格，本文件补被动处理器。HP/PP 中央取整/上限引用《HP、状态、招式与持物》/《战斗类型、命中与伤害计算》；等级/EV 上限《属性派生、特性选择与六项能力》/成长规格；场域期限场域规格；全阶段战斗结果规格；能力有效/连锁《特性参与计算、免疫与有效性》/阶段触发规格。

普通物品有效性拒倒下（显式允许倒下除外）、查封、魔法空间、按侧/队伍索引腐蚀、有效 KLUTZ；身份存在性与有效性分开。普通能力的模式破坏门不统一作用于物品：命中、伤害和会心物品层不因模式破坏者跳过。特定消费中的能力/状态资格可另受该门。物种专属处理器看个体原物种；多数变身后仍可满足，金属粉/速度粉显式排变身。

## 2. 调用与提交层

| 族/消费阶段 | 真实资格、顺序与返回用途 |
| --- | --- |
| SpeedCalc／WeightCalc | 拥有者普通物品有效；速度在能力之后、尾部统一四舍五入最少 1；重量在能力之后，物品层不受模式破坏者门。无返回保持输入 |
| AccuracyCalcFromUser／Target | U 能力与盟友/T 能力之后，再 U 物 → T 物，核心重力/命中果等随后。修改命中参数容器，返回值不表示效果成功 |
| DamageCalcFromUser／Target | 各能力层后 U 物 → T 物 → 通用后置；P/A/D/F 槽各自到《战斗类型、命中与伤害计算》指定位置取整，不把 P 变成 A 或 F |
| CriticalCalcFromUser／Target | 幸运咒语和能力更早；会心级非负且物品有效才读取。无返回保持级；目标族本快照空 |
| HPHeal／StatusCure／OnEndOfUsingMove／StatRestore | 普通 helper 先有效性；完整持物检查先 HP → 状态 → 使用结束（LEPPA 优先，失败才 WHITEHERB）→ 强制正向受击果。HP 入口本身未先统括拒倒下，普通有效性会拒；显式强制身份可绕此门，但完整强制入口先拒倒下。各处理器仍有自己的可恢复/资格 |
| OnBeingHit | 每击 calcDamage>0 且非替身，能力/吐导弹/U 击中能力之后 T 物；这里有效性显式允许倒下，处理器按自身条件再拒。U 失 HP 后可检查 U 恢复物品；不自动等待整招 |
| AfterMoveUseFromTarget／User | 招式拖出之后，阶段触发规格后段二；U 有效 SHEERFORCE 且附效数据 >0 则整段不进入。目标须在原目标集、非 unaffected、calcDamage>0 且物品有效，速度序处理；U 须未被换出且物品有效。之后才目标能力/跨半退出 |
| OnStatLoss | statsDropped 真＋物品有效；入场最终扫描、招式后段、MOODY 等具名点消费；返回是否退出影响「首个退出即停」/已换集合 |
| EndOfRoundHealing／Effect | 战斗结果规格先青草 → 能力治疗 → 同成员物品治疗；后段先成员期限 → 能力效果 → 物品效果 → 能力取得物。每步重读有效性，非统一提前快照；决定正值只在主阶段具名点退出 |
| OnSwitchIn／TerrainStatBoost／OnIntimidated | 入场能力后物品，再持物检查；场地通知全能力后全物品；威吓后是否查道具由其消费者的预先许可决定，不要求实际降攻必成功。真返回才接通用已触发 helper 消费 |
| ExpGainModifier／EVGainModifier | 使用持久个体当前物品，**没有场上有效性门**。经验无处理器返回 −1，才查 I；EV 无登记返回假才查 I，有登记即真。当前与 I 不叠两次；之后病毒/上限沿成长规格 |

非计算通知不统一自动消费。返回真处理器由 helper 调用「已触发」后置：若传入物品为果且有效 CHEEKPOUCH、可治，先请求 H 整除 3；是自己当前物则普通消费；强制外来物不是自己物，不清自己的 C，非投掷可共生。直接调用消费入口的物品绕颊囊通用层，按各条记。

普通消费先 R=C、P=C 及递增序号（可回收开），允许的树果设 Belch；再清 C、若 C=I 清 I、无 GORILLATACTICS 清讲究锁、UNBURDEN 有效置轻装，最后可共生。AIRBALLOON 的不可回收消费不新写 R/P，不等于清空先前 R/P。退出包/按钮关闭消费时共生，红牌普通消费可先共生再检查是否拖出。C 改变后后续 helper 读取当前物品，可能递归触发；没有通用一轮一次或事务回滚。正常终局读 I 还原的范围/显式中止不还原的风险沿战斗结果规格。

## 3. 计算修正

### 3.1 速度、重量、命中、会心与档内顺序

| 物品/族 | 完整修正 |
| --- | --- |
| CHOICESCARF 速度 | ×1.5；讲究锁另在命令规格，不以倍率代替选择门 |
| IRONBALL／MACHOBRACE／POWERANKLET／POWERBAND／POWERBELT／POWERBRACER／POWERLENS／POWERWEIGHT 速度 | ÷2 |
| QUICKPOWDER 速度 | 原 DITTO 且未变身 ×2 |
| FLOATSTONE 重量 | 整除 2、至少 1；输入已含临时重量与能力结果 |
| WIDELENS 用户命中 | 命中倍率 ×1.1 |
| ZOOMLENS 用户命中 | T 选择不是 UseMove/Shift，或已经行动时 ×1.2；None 也满足前者，不用纯速度比代替 |
| BRIGHTPOWDER／LAXINCENSE 目标命中 | 修改 U 命中倍率 ×0.9，不修改闪避阶级 |
| LUCKYPUNCH／LEEK／STICK 会心 | 前者原 CHANSEY＋2；后两原 FARFETCHD/SIRFETCHD＋2 |
| RAZORCLAW／SCOPELENS 会心 | 会心级＋1 |
| CUSTAPBERRY 档内 | 普通低 HP 食果资格满足输出＋1；计算时不消费，实际采用物品档的攻击阶段提示才直接消费 |
| LAGGINGTAIL／FULLINCENSE 档内 | −1 |
| QUICKCLAW 档内 | 0..99<20 输出＋1 否则 0；实际提示不消费。局部速度重算不重抽这份初始档，能力/物品档冲突归命令规格 |
| BLUNDERPOLICY 失手 | 第 1 击才可触发，半无敌落空不触发，三个 OHKO 效果排除；U 可升速才＋2 并经已触发 helper 消费。不是所有整招失败都触发 |

普通命中仍先分别取整命中/闪避百分数，再整数 q 取商，r 严格小于阈值；不重犯《特性参与计算、免疫与有效性》AB06 的浮点阈值错误。会心早期否决不会被＋级物品恢复。

### 3.2 威力/攻击/最终倍率

P 威力、A 攻击、D 防御、F 最终。附表完整列共享复制身份/类型映射，下面给不依赖名称推断的条件与量。

- 单类型 P ×1.2：BLACKBELT/FISTPLATE→格斗；BLACKGLASSES/DREADPLATE→暗；CHARCOAL/FLAMEPLATE→火；DRAGONFANG/DRACOPLATE→龙；HARDSTONE/STONEPLATE/ROCKINCENSE→岩；MAGNET/ZAPPLATE→电；METALCOAT/IRONPLATE→钢；MIRACLESEED/MEADOWPLATE/ROSEINCENSE→草；MYSTICWATER/SPLASHPLATE/SEAINCENSE/WAVEINCENSE→水；NEVERMELTICE/ICICLEPLATE→冰；PIXIEPLATE→妖精；POISONBARB/TOXICPLATE→毒；SHARPBEAK/SKYPLATE→飞行；SILKSCARF→一般；SILVERPOWDER/INSECTPLATE→虫；SOFTSAND/EARTHPLATE→地面；SPELLTAG/SPOOKYPLATE→幽灵；TWISTEDSPOON/MINDPLATE/ODDINCENSE→超能。
- ADAMANTORB：原 DIALGA 的龙/钢；GRISEOUSORB：原 GIRATINA 的龙/幽灵；LUSTROUSORB：原 PALKIA 的龙/水，均 P ×1.2。
- CHOICEBAND 物理、CHOICESPECS 特殊：**P ×1.5**；MUSCLEBAND 物理、WISEGLASSES 特殊 P ×1.1。不按通行名称写成全部攻击槽修正。
- DEEPSEATOOTH 原 CLAMPERL 特殊 A ×2；LIGHTBALL 原 PIKACHU 两类别 A ×2；THICKCLUB 原 CUBONE/MAROWAK 物理 A ×2。
- EXPERTBELT 相性克制 F ×1.2；LIFEORB 非混乱自伤 F ×1.3。生命宝珠扣 HP 在 §5 单独决定，增伤不等于必定扣。
- METRONOME F ×(1＋0.2×min（连续计数, 5）)；计数建立/不同使用清理引用命令规格，不擅自钳非法负计数。
- SOULDEW 原 LATIAS/LATIOS：当前「提升类型」设置真时龙/超能 F ×1.2；假且特殊招、无 souldewclause 时 A ×1.5。旧防御分支见下；不把开关简化为当前必永久禁用。
- 18 类型宝石（BUGGEM、DARKGEM、DRAGONGEM、ELECTRICGEM、FAIRYGEM、FIGHTINGGEM、FIREGEM、FLYINGGEM、GHOSTGEM、GRASSGEM、GROUNDGEM、ICEGEM、NORMALGEM、POISONGEM、PSYCHICGEM、ROCKGEM、STEELGEM、WATERGEM）各匹配本次对应类型；所有誓约族排除。匹配先记录 GemConsumed=C，P ×1.3（世代 ≥6）或 1.5（旧代）；使用提示在首击，实际消费整招后段才做。多击消费前仍可反复参与本次计算，后续属性变化读真实当前值；不在查询第一刻从背包扣物。

目标计算：ASSAULTVEST 特殊 D ×1.5；DEEPSEASCALE 原 CLAMPERL 特殊 D ×2；EVIOLITE 持久个体当前形态物种记录有至少一条有效后续进化（排前进化和方法 None）则 D ×1.5，不先检查当下能否满足进化条件；METALPOWDER 原 DITTO 且未变身 D ×1.5，两类别都可；SOULDEW 在上述设置假、原双水都、特殊且无条款时 D ×1.5。

减伤果类型：BABIRI 钢、CHARTI 岩、CHILAN 一般、CHOPLE 格斗、COBA 飞行、COLBUR 暗、HABAN 龙、KASIB 幽灵、KEBIA 毒、OCCA 火、PASSHO 水、PAYAPA 超能、RINDO 草、ROSELI 妖精、SHUCA 地面、TANGA 虫、WACAN 电、YACHE 冰（各身份完整后缀 BERRY）。本次类型匹配且相性克制才 F ÷2，一般果免克制门；有效 RIPEN 再 ÷2。**该 helper 没有食果/紧张感门**，但外层须 T 物品有效。立刻标本击 berryWeakened 并展示吃果动画，真消费在每击后附效/畏缩之后；下击可因已消费而无修正。替身/画皮普通伤害算法的早退以及不同伤害族《战斗类型、命中与伤害计算》/《多次攻击、特殊伤害与恢复》负责，不能以有动画保证 T 损 HP 为正。

## 4. HP、状态与阶级恢复

食果资格 canConsumeBerry 拒对侧有效 UNNERVE/复合紧张感。低 HP 资格先过食果；HP ≤ H 整除 4 可；四分之一以上至 H 整除 2 时，参数 false 表示**半血门不要求 GLUTTONY**，参数 true（默认）才要求 GLUTTONY 有效。两种参数均不放宽到半血以上。普通持物有效性及各调用者的 canHeal/阶级资格仍须满足；forced 具体绕过哪些门按各条，不概括为忽略所有资格。

| HPHeal 身份 | 量、门与返回 |
| --- | --- |
| BERRYJUICE | 必须 canHeal；非 forced 还须 HP ≤ H 整除 2；请求 20 恢复，真返回 |
| ORANBERRY／SITRUSBERRY | 必须 canHeal；非 forced 用低 HP 资格 false（半血及以下可，毋须 GLUTTONY；仍须可食果）；请求 10/H 整除 4，有效 RIPEN 先把已取整请求 ×2。恢复完成真 |
| FIGY／WIKI／MAGO／AGUAV／IAPAPA BERRY | 非 forced 要求 canHeal 及低 HP 资格，世代 ≤6 传 false，半血及以下毋须 GLUTTONY；世代 ≥7 传 true，无有效 GLUTTONY 只四分之一及以下，有有效 GLUTTONY 可到半血。请求 H 整除 3（≥8）、整除 2（7）、整除 8（≤6），RIPEN ×2。对应嫌弃味道能力项分别攻击/特攻/速度/特防/防御，性格降低该项则提示并在可自混乱时混乱。forced 不要求 canHeal，中央夹限后即使回血 0 也可混乱并真返回；不要把强制满 HP 果说成绝不消费 |
| LIECHI／GANLON／PETAYA／APICOT／SALAC BERRY | 非 forced 低 HP 资格；中央可升才各请求攻/防/特攻/特防/速＋1，RIPEN 请求翻倍；返回中央是否提交，封顶假 |
| STARFBERRY | 先收五项中央可升集合，空假；**先均匀抽项再进入低 HP helper**，即门最后拒也可能已有抽取。请求该项＋2，RIPEN 变 4 |
| LANSATBERRY | 非 forced 低 HP 资格；聚气已 ≥2 假，否则直接设 2 并真。不走阶级＋2，也不因 RIPEN 自动设 4 |
| MICLEBERRY | 非 forced 低 HP 资格；当前 MicleBerry 标记假则返回假，**原本真才保持真并反馈、真返回消费**。不将这处反向守卫按常见规则修正。普通命中消费已存标记会 ×1.2 并清假（《战斗类型、命中与伤害计算》） |

StatusCure：ASPEARBERRY 冻、CHERIBERRY 麻痹、CHESTOBERRY 真睡、PECHABERRY 真毒、RAWSTBERRY 灼伤；非 forced 还须可食果，匹配才治疗并真。PERSIMBERRY 混乱计数非 0 才清混乱；LUMBERRY 真实异常或混乱非 0 才同时治状态/混乱，COMATOSE 仅视为睡不当真实异常。治疗函数已写状态与计数不因后续提示失败回滚。

MENTALHERB 不受食果门：迷恋、挑衅、安可、折磨、定身、治疗封锁至少一项有效才真；分别清，安可计数和招式身份都清，定身只清计数、没有在此清 DisableMove 辅助身份。不治地狱突刺或任意临时效果。WHITEHERB 对七阶级所有负值直接归 0、标本轮升阶真；无负值假；不逐项中央升阶、无反向/单纯等转换，正阶级不改。用后通用消费，两者都不是树果，不触发颊囊。

LEPPABERRY 用**持久个体招式列表**收 PP 有损且总 PP>0 的槽，非 forced 仅有空 PP 槽可触发；forced 可在无空槽时选首个部分损 PP 槽。都先空槽的首个，不按最低百分比或随机。非 forced 还查食果。请求 10，RIPEN 20，持久 PP 钳到上限，然后**直接把同下标战斗槽 PP 写成持久新值，不检查身份相同或变身**；与《HP、状态、招式与持物》通常专门同步入口不同，必须单列例外。当前真实招式不同也可能收到数值，不能由通用 PP 归属推断这次不回读；两赋值先后不原子。返回真才通用消费。

## 5. 每击、招式后段与换人

### 5.1 受击处理器

共有外层 calcDamage>0、非替身、允许濒死物品有效性。无另述的本地守卫不补造存活/模式破坏门；中央升阶或 canHeal 会拒倒下。受击物在能力反应之后读取，前序转物/失物可影响它。

| 身份 | 条件、请求与消费 |
| --- | --- |
| ABSORBBULB／LUMINOUSMOSS／CELLBATTERY／SNOWBALL | 分别水→特攻 1/水→特防 1/电→攻 1/冰→攻 1；可升才提交并通用已触发消费 |
| AIRBALLOON | 提示破裂，消费不可回收、允许共生，再显式共生检查一次；不要求本击实际 hpLost>0，中央外层 calcDamage 门足够；浮空消失可影响后续击 |
| ENIGMABERRY | 非替身/非画皮/非冰脸且克制才转正向受击果 helper；helper 需 canHeal，非 forced 须可食果，请求 H 整除 4，RIPEN ×2；真才通用消费 |
| KEEBERRY／MARANGABERRY | 物理/特殊命中分别转正向受击果 helper，非 forced 食果门、中央可升防/特防，＋1 或 RIPEN＋2；真才消费。不被此层 SHEERFORCE 统一禁止，完整后段抑制是另一处 |
| JABOCABERRY／ROWAPBERRY | 可食果，物理/特殊招，U 可间伤才损 U 总 HP 整除 8，T 有效 RIPEN 将已整除量 ×2，通用消费；不要求接触。T 已倒下时它的 RIPEN 常规查询未必活跃，不能沿外层允许倒下扩大能力门 |
| ROCKYHELMET | 实际接触且 U 接触许可、可间伤，U 损 H 整除 6，不消费 |
| STICKYBARB | 实际接触且 U 接触许可、存活且无物：直接 T.C→U.C、T.C 清，T 轻装有效置标记；野生战、U 为玩家侧且 U.I 空、转物=T.I 时转 I 并清 T.I。不走消费、不写 R/P，不统一立即触发新持物 |
| WEAKNESSPOLICY | 排画皮/冰脸，要求克制且攻/特攻至少可升一项；依攻＋2 → 特攻＋2 各自资格、部分成功，之后通用消费；不因升一项而额外升另一封顶项 |

OnBeingHitPositiveBerry 族只有 ENIGMA／KEE／MARANGA，强制传入身份可绕上述「克制/物理/特殊」触发前门，但 helper 本身的 canHeal/中央可升仍有效。返回真假决定颊囊等后置，不是仅动画标志。

### 5.2 使用后/退出

- EJECTPACK：消费者先降阶事件标记及物品有效；处理器拒天空摔投、对侧队伍全灭、野生拥有者、不能换出、没有后备；通过先消费（可回收、禁共生）。回合末只召回/离场并返回真，补位后做；其它时点才选替补，负值返回假但**已消费**，成功替换/清选择/按是否 U 清模式破坏/入场。不能把返回假当物品未扣。
- EJECTBUTTON：后段目标物入口，尚无已换席、对侧未全灭、有后备才消费（禁共生）→ 选替补。**不检查普通换出拘束门**；负选择不回滚消费；成功替换/清选择/记已换/按 U 身份清模式破坏/入场。
- REDCARD：同入口，尚无已换且 U 活；先随机选 U 合格后备，无候选不消耗；再普通消费红牌（可共生），**随后**有效 SUCTIONCUPS 且非模式破坏或扎根可挡实际拖出。已耗不退；成功拖出 U、清选择、记已换、模式破坏假、入场。不是野生终局逃跑处理器。
- LIFEORB 后段 U 物：U 可间伤、实际伤害招、击数 >0 且至少一个原目标非 unaffected/非替身，损 U 总 HP 整除 10 → 恢复物品 → 濒死；不消费。所有击最终替身标志/后段 SHEERFORCE 门可使有增伤却无此扣 HP。
- SHELLBELL：U 可恢复，累加每目标 totalHPLost（含替身跨击量），正值则请求总和整除 8。恢复达半可清跨半事件，随后危急回避可能不再触发；本快照未保留官方例外。不消费，不用总 calcDamage。
- THROATSPRAY：双方参与队伍未全灭，声音招、实计击数 >0 且 U 可升特攻，＋1 后直接消费；不是必须伤害类，局部无「伤害>0」门。

## 6. 场域、成长与回合末

| 族/身份 | 合同 |
| --- | --- |
| WeatherExtender DAMPROCK／HEATROCK／ICYROCK／SMOOTHROCK | 当前新天气分别雨/晴/冰雹/沙暴时把正期限输入覆盖 8，其它保持。消费者仅原有限期限 >0、来源存在且物有效时查；不把强天气无限变 8 |
| TerrainExtender TERRAINEXTENDER | 调到即覆盖 8，但建立消费者同样只在有限期限和有效来源时查；不消费 |
| TerrainStatBoost ELECTRICSEED／GRASSYSEED／MISTYSEED／PSYCHICSEED | 当前电/青草/薄雾/精神匹配且中央可升：前两防＋1，后两特防＋1；**没有接地门**。真经通用消费；重复场地通知可能再查新物，不能说每通知都消费同一物 |
| OnSwitchIn AIRBALLOON | 只浮空提示；查询浮空在核心，不等于此提示永久建浮空标记 |
| OnSwitchIn ROOMSERVICE | 戏法空间计数非 0 且中央可降速（来源空）才速−1、直接消费；使用招式建立戏法空间后的全场检查另在阶段触发规格，也可触发；两入口并非只换入一次 |
| OnIntimidated ADRENALINEORB | 中央可升速才＋1，返回结果由 helper 消费。威吓原本失败仍可能到物品检查，实际消费者许可沿阶段触发规格 |
| EndOfRoundHealing BLACKSLUDGE | 当前毒类型且 canHeal：H 整除 16 恢复；非毒且可间伤：效果伤害 H 整除 8，包含物品/退出/濒死嵌套。毒而满 HP 不改，不反伤 |
| 同族 LEFTOVERS | canHeal 时 H 整除 16 恢复，不消费 |
| EndOfRoundEffect FLAMEORB／TOXICORB | 先按自己作为来源查可灼伤/可毒，实际提交不携来源，毒珠为剧毒；物品不消费；状态提交可引起治疗等重入，不能假设下一轮一定仍有异常 |
| 同族 STICKYBARB | 可间伤则效果伤害 H 整除 8，不消费；接触转移见 §5 |
| CertainSwitching SHEDSHELL | 输出真、换人规格确定换出门早于拘束；不直接换人/不消费 |
| CertainEscapeFromBattle SMOKEBALL | 输出真，实际逃跑入口仍有战斗种类等先行门；不直接写决定/不消费 |
| ExpGainModifier LUCKYEGG | 当前收益 ×3 整除 2；无登记 −1 使消费者回看 I。不是从第一个经验基数重新开公式 |
| EVGainModifier MACHOBRACE | 每能力收益 ×2；POWERANKLET 速/POWERBAND 特防/POWERBELT 防/POWERBRACER 攻/POWERLENS 特攻/POWERWEIGHT HP 增加 8（当前开关）或 4；之后病毒倍增/上限截断归成长规格。按注册有无返回是否处理，不依返回容器真假 |

## 7. 注册表外直接核心与边界

不得以 32 族目录穷尽所有持物影响：以下已有主规则的直接检查继续保留，非本文件遗漏的空操作。

| 物品/直接作用 | 唯一主规则/本文件消费关系 |
| --- | --- |
| FOCUSSASH／FOCUSBAND | 《战斗类型、命中与伤害计算》§7 满 HP 留 1 分支：披带保证一次后在提示处消费；头带 10% 且也在该快照满 HP 分支，不消费 |
| KINGSROCK／RAZORFANG | 《战斗类型、命中与伤害计算》额外畏缩 10%，天恩或彩虹 20%，鳞粉/自带畏缩/倒下/替身门；允许倒下的拥有者查询也不等于目标允许倒下 |
| ASSAULTVEST／三讲究物 | 命令规格选择/执行门，背心只命令阶段限制变化（抢先使用例外），讲究锁在结束行动记录；本文件数值槽不能替代动作门 |
| IRONBALL／AIRBALLOON／RINGTARGET | 《战斗类型、命中与伤害计算》地面/飞行与相性；铁球先接地，气球浮空、破裂不恢复；标靶只改原免疫的单类型项 |
| SAFETYGOGGLES／UTILITYUMBRELLA／PROTECTIVEPADS | 《异常状态、能力阶级与免疫》/场域/阶段触发规格：护目镜粉末和沙雹资格；伞使拥有者有效晴/雨及强版本为无；护具拒接触效果，不删除原接触标记或普通伤害 |
| BIGROOT／GRIPCLAW／BINDINGBAND／LIGHTCLAY／POWERHERB | 《多次攻击、特殊伤害与恢复》/招式变更-B/场域规格：根对具名恢复请求 ×1.3 向下取整，束缚计数 8/旧 6 及伤害分母，光黏土墙 8，香草快蓄力先消费；已给具体主合同不重复设计 |
| DESTINYKNOT | 《异常状态、能力阶级与免疫》迷恋提交后在相应中央资格下反施给来源；不是每次「拥有迷恋」都循环反射；持物不消费 |
| HEAVYDUTYBOOTS | 场域规格入场危害：针对各危害具体门，毒类型吸毒菱等前序不因靴子一律跳过 |
| EXP.SHARE／AMULETCOIN／LUCKINCENSE 及其它世界持物输入 | 成长分配/战斗结果奖金标记、《HP、状态、招式与持物》个体状态及道具使用主动入口；本文件不把背包 EXPALL 误作持物处理器 |

持物定义/Flags 由《内容身份、注册与 schema》及招式变更两规格自然之恩/投掷/不可移物完整数据给定；复制登记只共享本族合同，不说明所有族一致。默认世代 8、更多努力值开、心之水滴类型开；数据可以替换，未知身份查询通常无登记不改此层，但数据解析异常不承诺统一恢复。两空族 CriticalCalcFromTarget、TrappingByTarget 明确空；未发现脚本其它文件追加此注册目录，AI 读取不作真实处理器证明。

## 8. 示例场景与测试目录

静态场景（普通数值例沿《战斗类型、命中与伤害计算》共同前提 L50、P60、攻防 100、非会心、中性、无本系/其它修正、最大随机，基准 28；只改变所列项。固定输入/手工状态推导，独立常数算术，不运行参考）见测试目录 [`../test-catalog/pokemon-rules-wp43-44-46-48-50.md`](../test-catalog/pokemon-rules-wp43-44-46-48-50.md) 的 HI01–HI33（CHOICEBAND 中间值、WIDELENS×BRIGHTPOWDER 阈值、FLOATSTONE、QUICKCLAW 不重抽、ORAN 半血门两组、SITRUS×RIPEN、FIGY 世代 8 与 forced 满 HP、MICLE 标记、STARF 先抽后拒、MENTALHERB 定身保留、WHITEHERB 直接归零、LEPPA 持久/战斗槽例外、OCCA 紧张感不免、宝石多击、ROCKYHELMET 允许倒下、WEAKNESSPOLICY 部分成功、REDCARD 扎根、EJECTPACK 负值已消费、EJECTBUTTON 不查拘束、SHELLBELL 跨半清除、LIFEORB 替身门、地形种子浮空、LEFTOVERS 最低 1、LUCKYEGG/POWER 物、魔法空间成长物、退出包消费写回、BLACKSLUDGE 两分支、THROATSPRAY 变化声音、ORAN 51 边界、SITRUS 50、五混乱果世代 6/8 四门、ORAN 紧张感门）。

## 9. 依赖、证据与状态

- 道具使用主规则（道具使用规格）；基础公式（《战斗类型、命中与伤害计算》）；状态/阶级中央（《异常状态、能力阶级与免疫》）；场域（场域规格）；持久状态/PP（《HP、状态、招式与持物》）；成长/终局（战斗结果规格）；招式变更-B（必要身份级联后版）；能力计算（《特性参与计算、免疫与有效性》）；阶段触发（阶段触发规格）——均已限定通过。
- 附表把每登记/别名落到上述量值与消费合同。所有输出只静态确认，显示/素材/输入与真实运行仍未决；捕获、形态、Shadow、设施特殊组合、demo/插件/U01–U10 和出口保留。LEPPA 等具名路径是对通用同步入口的额外消费者，不自动重写旧《HP、状态、招式与持物》。
- 回源核对：五混乱果调用点、默认 true 的阶级果、聚气/命中果与先制果门不变；恢复量/RIPEN、性格混乱、forced 满 HP 与后置消费合同不变（WP50-R01 已 CLOSED）。
