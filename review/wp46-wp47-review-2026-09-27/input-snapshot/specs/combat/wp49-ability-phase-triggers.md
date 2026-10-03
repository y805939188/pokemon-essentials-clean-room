# WP49 — 特性阶段触发、反应与连锁

状态：**Reviewed（限定静态范围，2026-09-27 v2有限复审PASS_SCOPED；管理性回填）**。日期2026-09-27。Feature F12-06阶段子范围；Combat Requirements／Pokémon Rules。基线commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，只读静态确认，不是运行确认。

被审首稿v1：`9286900834514d363d0e15b50aeefdd581c0b86b930c9cfe006421dcc470ca6d`（50,601字节）保留历史；被审v2 `7a4ecf931a65931cd8c6255d09b2697f83a5b538da907a016e5712efa32a67d7`（52,573字节）经[独立闭合报告](../../review/wp42-wp48-wp49-recheck-2026-09-27/report.md)限定通过，WP49-R01／C01 CLOSED。本稿仅状态及上游身份回填，新字节不冒充原被审版；批准范围：A～F已述21族阶段触发、直接生命周期／排序／失能／连锁／写入边界；119展开身份有界合同。

## 1. 范围、概念与输入输出

A为主体／有效性／能力改变，B为入场与离场，C为HP／状态／阶级／畏缩反应，D为每击／招式结束，E为回合末／濒死／场地，F为注册表外直接生命周期与嵌套。目录27族数值／免疫由WP48负责，本包21族不重定伤害公式或中央状态规则。§13审计身份对应正文合同，名称不作为未来结构建议。

输入为当前能力身份与压制、场上对象／席位／个体索引、使用者U／目标T／拥有者B／来源、存活与真实／视为状态、当前HP和本次伤害记录、选择及已换席位集合、类型／形态、天气／场地、当前轮数、物品及可更新还原／回收记录。输出分别为：资格真假（尤其是否发生退出）、局部或持久写入、后续回调／选择等待、能力提示／动画。回调被调用、显示消息、实际升阶／治疗和成功退出是不同结果。

集合约定：普通全场／盟友／对侧遍历是存活场上集合（不含后备），自然席位序；标“速度序”则采用WP42§5的速度缓存序，不受戏法空间反转，持有者在消费时再核资格。排序缓存可持有被换入重新初始化的同席位对象，不能以席位相同断言还是原个体。使用招式目标列表则沿本次实际选取顺序，不能一律改成速度序。

## 2. 通用入口与能力变化（A）

普通能力有效性主规则WP48§2。大多数阶段只查普通有效性；每击受击／击中显式允许濒死拥有者（仍拒胃液／气体），具体处理器可再拒濒死。入场／获得能力允许**存活且不可失去能力**或普通有效者。原始能力身份的直接形态分支不自动套普通有效性。模式破坏者不是统一关闭全部回调；只在明列的资格或子查询中起作用。

场上能力赋值只改场上身份，不写回持久个体能力；物品／HP／真实状态通常经各自字段写回个体。场上形态普通赋值会写个体，随后能力／能力值回读按形态入口，不能将所有能力改变等同持久变更。局部HP直接归0的离场处理不等同持久HP归0。

不可失去／压制名单：BATTLEBOND、DISGUISE、GULPMISSILE、ICEFACE、MULTITYPE、POWERCONSTRUCT、SCHOOLING、SHIELDSDOWN、STANCECHANGE、ZENMODE、ASONECHILLINGNEIGH、ASONEGRIMNEIGH、COMATOSE、RKSSYSTEM。不可获得名单在此前提再含FLOWERGIFT、FORECAST、ILLUSION、IMPOSTER、NEUTRALIZINGGAS。未知／缺失身份的名单查询为假，不能由此承诺不合法数据可正常完成全部后续。

失去能力后置入口依实际旧能力处理气体结束／紧张感结束／幻觉解除，再按**当前**能力清理：不可失去者取消胃液，非SLOWSTART清慢启动，非TRUANT清懒惰；检查强天气结束→天气形态检查（标能力改变）→场地能力检查（标能力改变）。幻觉解除仅在有幻觉记录时清，非变身才还原外观及已见登记。

获得能力后置入口：持续检查（Trace可再改能力，此处不立即重复触发它复制到的入场项）→当前能力的入场回调，实际入场标志为假→状态治疗检查→强天气结束检查。默认“入场回调”不等于真的换入：IMPOSTER要求真实入场标志，因此此路径不变身。没有为所有后置路径补统一事务回滚；更早的能力赋值不会因后续无效果而撤销。

| 改变来源 | 实际后置调用 |
| --- | --- |
| 普通能力赋予／复制招式、Mega更新 | 保存旧身份，完成赋值／外观后失去旧能力→获得新能力；完整招式前门WP47、Mega整体WP22 |
| 交换招式、WANDERINGSPIRIT | 先双方赋值，U失去→T失去→U获得→T获得；前一步可影响后一步有效性 |
| MUMMY | U失去→U获得；接触防护导致未赋值时也到达这两个后置调用，旧身份参数可为空 |
| 胃液／核心惩罚抑制 | 先设胃液、清懒惰，再“失去”后置（压制标志真），不调获得 |
| TRACE | 直接复制；持续检查若不在真实入场准备中，仅另调复制后入场回调，不套完整失去／获得程序 |
| POWEROFALCHEMY／RECEIVER | 直接继承；该处理器没有失去／获得后置；濒死流程第二遍会读取新身份 |
| IMPOSTER的变身提交 | 复制场上能力等后只调失去旧能力后置，未再调完整获得；见§9 |

## 3. 入场顺序与具体反应（B）

实际换入入口先按条件重置全场跨半HP／降阶事件标记，命令换人会更早重置并跳本次重复重置（气体结束引起的降阶不能被抹掉）。按速度序逐入场者：参与记录→入场提示→位置愿望等→入场危害；危害致倒下则濒死→成长→裁判→跳该成员后段。其余：形态→Primal→持续能力检查→入场回调（真实入场真）→强天气结束→入场物品→持物触发→能力状态治疗。最后全场速度序先降阶物品退出、再跨半HP退出，首个真即停止这一退出扫描；然后清全场这两事件标记。已写决定并不在每个回调之间统一return，入口与WP41／42实际检查点一致。

### 3.1 展示与可见探测

| 身份 | 条件／行为 |
| --- | --- |
| AIRLOCK／CLOUDNINE | 展示天气影响消失，不清当前天气／期限；有效天气压制由WP45查询负责 |
| AURABREAK、DARKAURA、FAIRYAURA、MOLDBREAKER、PRESSURE、TERAVOLT、TURBOBLAZE、UNNERVE、COMATOSE | 此回调仅对应能力／气场／紧张感／瞌睡提示，实际数值、耗PP或视为睡眠在各主规则；COMATOSE此提示本身没有物种门 |
| ASONECHILLINGNEIGH／ASONEGRIMNEIGH | 先复合能力提示，再临时把场上能力标识改UNNERVE作提示，随后恢复原身份；不构造任意多能力系统 |
| ANTICIPATION | 仅玩家拥有者；扫描存活对侧伤害招。基于基础相性（无效跳过），有克制或三种OHKO效果则提示；无自身类型时只OHKO。世代≥6的觉醒力量按对方个体IV取类型，其余用招式原类型，不跑完整本次命中／伤害 |
| FRISK | 仅玩家拥有者；对侧有持物者。世代≥6逐个展示拥有者与物品；旧世代均匀选一个只报物品，无目标不展示；不检查物品当前能否生效 |

FOREWARN也只玩家拥有者：扫描对侧每个招式，按以下“比较分数”选最大并均匀抽取并列**条目**之一展示名称；同名多条不去重，不执行伤害计算。默认取数据威力；OHKO三类设160；反击／镜面反射／金属爆炸设120；固定20／40／使用者等级／随机等级伤害、降目标HP至自身、亲密或不亲密威力、自身HP越高、目标比自身越快、树果类型威力、剩PP越少、自身HP越低、目标重量越大这些效果设80；觉醒力量世代≤5也设80。**自身HP越高的效果先被设150，后又被80覆盖，最终比较80**，不能依注释写150。其它保持数据威力，包括可能为0的变化招；没有候选则不展示。

### 3.2 状态与数值

| 身份 | 具体提交 |
| --- | --- |
| CURIOUSMEDICINE | 存活盟友有非零阶级时逐个重置全部七阶级，正负均归0；不重置自己，不逐项模拟升降触发 |
| DAUNTLESSSHIELD／INTREPIDSWORD | 分别请求自身防御＋1／攻击＋1，经中央资格；没有每场一次标记 |
| DOWNLOAD | 求存活对侧的当前防御与特防数值各总和（数值读取受奇妙空间交换，非含阶级计算）；防总和<特防总和则攻＋1，否则特攻＋1，空集合0=0也选择特攻 |
| PASTELVEIL | 入场回调治存活盟友真实中毒；自己由之后StatusCure入口治疗；无盟友中毒不展示 |
| SCREENCLEANER | 依次对侧极光幕→光墙→反射壁，再己侧同序；每个正期限归0并提示，全部0不展示；不动其它屏障／保护 |
| SLOWSTART | 每次到达该回调置计数5并提示；气体结束等重新触发也重置5，回合末计数按WP42／44 |
| INTIMIDATE | 逐存活且邻近的对侧请求降攻1；具体前门与后置见下段 |

威吓先确定是否稍后检查道具：目标CONTRARY有效且攻已＋6，或非CONTRARY且攻已−6时不检查，其余检查。中央威吓入口先拒倒下、替身；世代≥8有效OBLIVIOUS／OWNTEMPO／INNERFOCUS／SCRAPPY拒绝。随后按WP44能力降阶helper（含反向／镜甲／防降）提交；返回成功才调用OnIntimidated，其后按先存的道具许可调用物品威吓检查，故即使威吓未成功也可能检查道具。不开能力条时还有具名消息所需的白雾／防降／盟友检查，不将显示分支概括为完全相同的入口顺序。OnIntimidated仅RATTLED：世代≥8请求自身速度＋1，旧世代不改。

### 3.3 天气、场地与入场形态

DRIZZLE／DROUGHT／SANDSTREAM／SNOWWARNING分别请求雨／晴／沙暴／冰雹；同当前天气不刷新期限，普通能力不能覆盖强天气。DELTASTREAM／DESOLATELAND／PRIMORDIALSEA分别强风／大日照／大雨，可走覆盖强天气入口。普通天气默认固定5回合并可由有效延长物品改变；关闭能力固定天气配置时无限，强天气本来无限。WP45主规格给建立、覆盖、有效压制和失去拥有者时默认恢复的完整规则。

ELECTRICSURGE／GRASSYSURGE／MISTYSURGE／PSYCHICSURGE分别电／青草／薄雾／精神场地；已有同场地不刷新，否则建立默认5并允许有效延长物品。建立时全场能力通知一遍，再全场物品通知一遍，不按每成员能力→物品交错。MIMICRY入场仅当前场地非无时调用其场地合同§8，不加接地门。

ICEFACE入场回调：EISCUE且形态1、有效冰雹时请求形态0，**本处理器不要求switch_in真**；气体结束以默认假标志重调它时仍可恢复，实际形态提交还受§9通用门约束。IMPOSTER则要求真实入场真、自己未变身，选择正对面，拒其倒下／变身／幻觉／替身／被天空摔投／半无敌，随后请求变身。变身不是隐式重新登记所有入场技能，局部提交见§9。

NEUTRALIZINGGAS到达入场回调后提示，遍历存活场上者：慢启动归0、懒惰假；若无有效三种讲究物品则清锁招；有幻觉则清、非变身者恢复外观／已见。为比较紧张感压制前后，暂时将自身能力标识清空查询全局紧张感，再恢复气体；如果从有变无，对每个存活成员调用“紧张感结束”。该helper又速度序扫描全场树果，故可重复检查，不是一次去重全局通知。普通有效性对气体的持续压制由WP48负责，不由这条提示的出现次数决定。

## 4. 离场、濒死与恢复有效性（B/E）

普通离场先普通有效的OnSwitchOut（结束标志假）→个体离场形态回调→若原气体／紧张感有效，将**局部**HP置0、标已倒下后通知结束→无论何能力最终也局部置0／标已倒下→检查强天气终止。这里不经持久HP字段，也不统一撤Mega／Primal；真正倒下和终局另有合同。

OnSwitchOut：IMMUNITY仅真实毒、INSOMNIA／VITALSPIRIT仅真睡、LIMBER仅麻痹、MAGMAARMOR仅冻、WATERVEIL／WATERBUBBLE仅灼伤时直接将真实状态设无；NATURALCURE无条件设无。这走字段写回和计数清理，主要只诊断记录，不统一作普通治疗动画。此族没有PASTELVEIL或SWEETVEIL复制登记。REGENERATOR普通离场请求总HP整除3恢复，不先套canHeal，因此治疗封锁不能自动禁止；正常终局结束标志真则明确不恢复。正常終局只对仍普通有效的场上对象调本族，已倒下者不因“战斗结束”被统一治好；WP42其它外层治疗另计。

真正濒死程序在HP≤0且尚未处理时执行：提示／演出、击败记录、临时效果初始化、真实异常与计数清、内部战斗友好度、离场形态、撤Mega／Primal、清选择及同侧倒下轮次等，然后能力反应。按速度序第一遍处理其它当前有效成员的ChangeOnBattlerFainting，第二遍再次读各自当前能力处理OnBattlerFainting。最后对已倒下者用“允许濒死”的有效查询处理气体／紧张感结束，再强天气检查。

- POWEROFALCHEMY／RECEIVER：同侧倒下者能力可获得，且不是POWEROFALCHEMY／RECEIVER／TRACE／WONDERGUARD，则复制其当前能力并提示；不要求倒下者当时普通有效。不调用完整获得程序，第二遍可直接按新SOULHEART等反应。
- SOULHEART：每次到达对任意一侧的倒下事件，请求自身特攻＋1；中央封顶可能使其无实际增量。一次多成员倒下有多次事件，不能只按招式一次计。
- 气体结束helper先检查仍有全局有效气体则返回；否则提示、强天气检查，速度序对存活且（不可失去或普通有效）者重调入场回调（真实入场假）。可重新威吓、设天气、慢启动等；并不包含通用持物／状态治疗全套入场链。
- 紧张感结束helper速度序对持有树果者调用持物触发，该入口自己检查存活、物品有效与能否食用。仍有另一侧紧张感时不能只因“结束通知到了”就强行吃树果。

## 5. HP、状态、阶级与行动失败反应（C）

### 5.1 跨半HP退出

记录损失的中央扣HP在扣后HP<总HP整除2、扣前≥该界时置跨半标记；是严格低于整数一半。中央回血达到该界可清标记。消费入口要求标记真及普通能力有效，才调用EMERGENCYEXIT／WIMPOUT，返回真假由退出消费者使用。

二者共同先拒被天空摔投或正在执行对应天空摔投两回合动作。野生战中，只有拥有者在敌方且其**当前同侧存活场上成员数>1**才由额外人数门拒绝。计数含存活拥有者和其它非空、未濒死的同侧场上成员；已倒下者、空位、后备不计，名义双席／多席布局不等于这个数量；玩家侧拥有者不加这道敌方人数门。随后仍按WP41能否逃跑检查，准许则反馈逃走、决定3并返回真。训练家战先拒对侧全灭、不能换出、无合格后备；回合末中只召回并走普通离场（返回真，补位留后段），其它时点等待所有者选后备，负选择返回假，已发生的提示不回滚；正常选择后实际替换、清本席选择，若退出者就是传入招式U则清模式破坏者，再完整入场并返回真。

不是每次扣HP立刻调用此能力：效果伤害helper先清旧跨半标记→扣HP／消息→恢复物品→退出能力→若倒下则真正濒死→清跨半标记。毒／灼伤等显式消费者也分别处理；天气持续回调只扣HP→物品→由外层濒死，不自行消费跨半标记。每击后的目标／U退出在§6.3规定位置，强行套成全局HP监听会改变次序。

### 5.2 状态、阶级、畏缩和档内反馈

真实状态提交并显示后先检查状态形态，再普通有效OnStatusInflicted，然后物品状态治疗，再能力状态治疗。SYNCHRONIZE要求有来源且非自身，只反射毒（按自身正状态计数保留剧毒）、灼伤、麻痹；先用各自同步资格，不再用普通招式资格替代。提交给来源时不继续携带来源对象，避免无限同步往返；原状态不因反射失败而回滚。

StatusCure：IMMUNITY／PASTELVEIL治真毒，INSOMNIA／VITALSPIRIT治真睡，LIMBER治麻痹，MAGMAARMOR治冻，WATERVEIL／WATERBUBBLE治灼伤；OWNTEMPO仅混乱计数非0则清；OBLIVIOUS清迷恋，世代≥6还清正挑衅计数，旧世代保留挑衅。逐项实际有状态才反馈；不把COMATOSE“视为”睡眠当真睡治疗。除状态提交，还由迷恋／混乱后段、实际入场／能力获得调用，均先查能力有效。

中央实际升／降阶正增量提交后，能力有效才通知对应族。OnStatGain本快照空。OnStatLoss的COMPETITIVE／DEFIANT：来源为空或对侧才请求自身特攻＋2／攻击＋2；存在同侧或自身来源则不触发。一次多项成功下降逐项通知，可升多次；封顶／被拒无实际下降不通知，反向升阶按升族，镜甲依WP44真实接收者。

OnFlinch STEADFAST：成功检查确因畏缩阻止本次行动时、能力有效则请求速度＋1，之后记录招式失败并返回，不让本次恢复行动；只是建立畏缩标记不立即升速。

PriorityBracketUse QUICKDRAW：攻击阶段优先级效果提示阶段，已标本轮采用能力档效果且能力仍有效才显示加速；此回调不抽样、不再改顺序。WP48的档计算与本通知分开；中途更换能力可能沿旧档排序而没有相同提示。

## 6. 每击与整次招式（D）

### 6.1 每击时点与合同

伤害招对未unaffected的各目标，先记录伤害及招式处理伤害时的副效，再进入每击：仅当计算伤害>0且非替身时，T能力（允许濒死）→若U失HP检查U恢复物品→吐导弹直接分支→若U失HP检查物品→U能力（允许濒死）→U恢复物品→T物品（允许濒死）及U失HP检查。之后其它愤怒、鸟嘴加热、陷阱、怨念／同命记录不自动受该能力前门。后段才耐受／画皮提示、全场恢复物品、全场濒死、裁判检查点、招式主要效果、附效等。能力回调自身不自动裁判或成长；同一击后段可能继续处理，直到实际调用者检查点。

这里的“接触”默认是招式实际接触（含LONGREACH修正）；“接触效果许可”另拒已倒下者和有效PROTECTIVEPADS。POISONTOUCH／PICKPOCKET用**原始**接触标记，下文明确例外。模式破坏者不全局跳过T每击回调；各回调及中央资格自行查门。

| T受击身份 | 分支、量值与副作用 |
| --- | --- |
| AFTERMATH | T已倒下且实际接触；模式破坏者假时全局有效DAMP阻止。否则U可受间接伤害且接触许可，扣U总HP整除4；不要求T仍存活 |
| ANGERPOINT | 本击会心且T中央可升攻：直接攻设＋6并标本轮升阶，不走逐增量升阶通知；如果不能升则无效 |
| COTTONDOWN | 有至少一个其它存活场上者可降速才展示；随后逐所有其它存活场上者请求速度−1，包括盟友与U，来源T |
| CURSEDBODY | U存活且未禁用；找到U最近普通使用招式的当前槽，不能是PP0且总PP>0；抽0..99<30，再香气幕前门，成功设禁用3与该招式身份，然后检查U状态恢复物品。不是必定禁用这次外层招式 |
| CUTECHARM | T存活、实际接触、r<30，再U可迷恋且接触许可，建立迷恋来源T |
| EFFECTSPORE | 实际接触、r<30，再均匀抽0睡／1毒／2麻痹；U已“视为”对应异常时退出。粉末与接触许可、该异常中央资格皆过才提交；不会为免疫重抽。睡眠提交不携来源，毒／麻痹带T |
| FLAMEBODY／POISONPOINT／STATIC | 实际接触、U未视为对应灼伤／毒／麻痹且r<30，再中央资格与接触许可；施加对应普通状态、来源T。T不另加存活门 |
| GOOEY／TANGLINGHAIR | 实际接触，请求U速度−1并明确检查接触许可；中央防降／反向／镜甲仍可影响结果 |
| ILLUSION | 有幻觉记录则清、还原展示、登记已见，不显示普通能力条；Mega还会以空U／招式定点调用这个具体处理器，不推广其它受击项支持空参数 |
| INNARDSOUT | T倒下且U非dummy，可受间接伤害则按T本击实际hpLost扣U，非累计总伤害；不要求接触 |
| IRONBARBS／ROUGHSKIN | 实际接触，U可受间接伤害且接触许可，扣U总HP整除8 |
| JUSTIFIED | 本次暗类型，请求T攻击＋1 |
| MUMMY | 实际接触、U存活、能力可失去且与木乃伊不同；接触许可则U能力改木乃伊；无论许可是否通过，仍失去／获得后置，见§2 |
| PERISHBODY | 实际接触、U存活，U和T灭亡计数都不正；接触许可则双方设4，来源均T席位。任一已有计数则整个不重置 |
| RATTLED | 本次虫／暗／幽灵，请求T速度＋1 |
| SANDSPIT | 请求沙暴，用普通能力天气入口（不能覆盖强天气），没有T存活的额外本地门 |
| STAMINA | 请求T防御＋1 |
| WANDERINGSPIRIT | 实际接触，U能力可获得且非RECEIVER／WONDERGUARD；接触许可才交换U/T身份。其后无论是否交换都U失去→T失去→U获得→T获得；无统一U存活前门，许可本身会拒倒下U |
| WATERCOMPACTION | 本次水类型，请求T防御＋2 |
| WEAKARMOR | 物理招且至少可自降防或自升速；先防−1，再速度世代≥7＋2、旧世代＋1，逐项资格、可部分成功 |

OnDealingHit唯一POISONTOUCH：**原始接触**且r<30，T有效SHIELDDUST且模式破坏者假则阻止；否则T可中毒才普通毒。没有用U接触许可或实际接触查询替代该条件，U能力调用虽允许濒死，T中央状态门仍拒倒下。每击可分别抽；不是整次招式只抽一次。

### 6.2 招式结束的使用者能力

所有击结束和招式自身后效之后，先目标解冻、同命（可使U倒下并裁判），再U普通有效OnEndOfUsingMove。该族不被后面SHEERFORCE的“后段二／三”总门关闭。

| 身份 | 具体合同 |
| --- | --- |
| BEASTBOOST | 对侧队伍未全灭，目标列表中damageState.fainted数量n>0；取U未算阶级的五项数值最高者，按攻→防→特攻→特防→速遇并列取首个。若该项可升则＋n，即使已封顶也不改选下一项 |
| MOXIE | 同样对侧未全灭且n>0，攻击＋n |
| CHILLINGNEIGH／ASONECHILLINGNEIGH | 同样门，攻击只＋1（不是＋n）；临时把能力标识设CHILLINGNEIGH展示／执行后恢复传入身份 |
| GRIMNEIGH／ASONEGRIMNEIGH | 同上但特攻＋1及临时GRIMNEIGH身份 |
| MAGICIAN | 非未来攻击、是伤害招、U无物且非野生拥有者；按目标列表找非unaffected／非替身且有可转移物品者。双方不可失去物品门；T有效STICKYHOLD拒该目标但可继续下个，没有模式破坏者例外。首个成功物转U、T清，T轻装有效时标记；野生战且U还原记录空、转物等于T还原物时转移两份还原记录；U持物触发后结束扫描 |

目标倒下标记n是此次目标记录，不重算所有场上倒下者、不限对侧目标；真正对侧是否全灭另用队伍判定。U已经倒下则能力普通有效门拒，不能因为它也造成击倒就给加成。

### 6.3 更后段的目标与退出

接§6.2之后：战斗牵绊／吐导弹使用后形态→客房服务→实际消耗本次宝石→招式强迫目标换人→若U非SHEERFORCE有效且附效数据>0的组合，则执行后段二。后段二速度序先目标物品、各非U降阶物品退出；再未被换出的U物品；再速度序目标能力（在目标列表、非unaffected、未换、普通有效），接着对每个非U跨半退出（仅尚无任何换人且伤害招，包括被波及非目标）。同一列表按席位记录，不能跨替换仍对旧对象保证生效。

AfterMoveUseFromTarget：BERSERK要求伤害招、跨半标记仍真、中央可升，特攻＋1；COLORCHANGE要求本次calcDamage非0、非替身、类型非空且非伪类型、T尚非单一该类型，改成该类型并清多余类型；PICKPOCKET要求T非野生、U未换出、原始接触、U当前替身无且T本击非替身、T无物且U有可转物、双方不可失去门；U有效STICKYHOLD阻止，无模式破坏者例外。成功物转T、U清、U轻装标记，野生战符合空还原／原物条件则转还原记录，最后T持物触发。

随后若U未换出，执行招式使用结束效果（如U换人／物品消耗）；再同样SHEERFORCE门控制后段三：尚未任何换人时先U降阶物品退出，再伤害招U跨半退出。最后numHits>0才全场持物结束检查。SHEERFORCE只跳具名二／三段，不跳前面击中状态反应、U击倒升阶或所有物品。

整个常规使用完成后清模式破坏者→成长→设施记账／暗影入口→结束行动持续能力检查，再号令、舞者等嵌套。能力造成HP0、决定已写和随后成员继续处理分别记录，不能自动补“决定非0马上退出全部回调”。

## 7. 回合末四族（E）

主全序和三个早退点由WP42§5固定。本包输入按那份速度缓存序，但各次消费重新检查普通能力有效。

| 族／身份 | 时点与完整行为 |
| --- | --- |
| EndOfRoundWeather DRYSKIN | 天气期限先到期／恢复默认后，逐成员在普通天气伤害前用其有效天气：晴且可受间伤扣总HP整除8，再恢复物品；雨且canHeal请求总HP整除8恢复 |
| 同族 ICEBODY／RAINDISH | 有效冰雹／雨且可恢复时分别总HP整除16；其它天气无效 |
| 同族 SOLARPOWER | 有效晴且可受间伤，扣总HP整除8后恢复物品 |
| 同族 ICEFACE | 输入有效冰雹、允许恢复标记真且形态1，请求形态0；该处理器本身不再加物种门，标记建立在具名EISCUE天气检查 |
| EndOfRoundHealing HEALER | 在青草治疗之后、同成员回血物品之前，一次r<30成功后遍历全部存活盟友，治各自真实异常；不是每盟友独立30%，无异常者跳过 |
| 同族 HYDRATION | 自己有真实异常且有效雨，治疗 |
| 同族 SHEDSKIN | 自己有真实异常再抽r<30，治疗；不是三分之一 |
| EndOfRoundEffect BADDREAMS | 侧／场期限和场地到期后的后段；逐邻近存活对侧“视为睡眠”者，可受间伤则经效果伤害helper扣总HP整除8，可嵌套物品、退出、濒死；不等同只对真实睡眠 |
| 同族 MOODY | 世代≥8候选五项主战斗阶级，旧世代七项含命中闪避；分别收集中央可升／可自降集合。均空不做；均匀选可升一项请求＋2，再从预先可降集合删除同项，均匀选剩可降一项−1。可只升或只降；剩可降集合非空才检查阶级恢复物品，随后总会检查降阶退出物品 |
| 同族 SPEEDBOOST | 在场turnCount>0、选择非Run且可升速度，＋1；本轮开始后才入场者turnCount0不升 |
| EndOfRoundGainItem BALLFETCH | 同成员后段能力→后段物品→取物能力顺序。自身空物且全局首个未回收球记录非空，取该物；自身还原记录空才补，清全局球记录，持物触发 |
| 同族 HARVEST | 空物、回收记录为树果；晴免抽，其它r<50；取树果、清回收记录、空还原记录才补，持物触发 |
| 同族 PICKUP | 空物；扫描其它存活场上者的PickupUse，选严格大于当前最大且最大>0者（并列保留先见），最后选出的PickupItem非空才取；清来源拾取物／序号、同物回收记录；野生战符合空还原／原物相等条件时转还原记录；持物触发 |

天气能力后外层立即按需要真正濒死，再同成员普通天气伤害；不会把回调返回解释为自动结束该轮。后段Effect使决定改变时，仍可能继续该成员物品／GainItem和后续成员，直到WP42显式成长后早退检查；资格会随当前存活／能力变化而改变。Pickup是战斗内拾取，不用WP42世界10%物品表。

恢复／损失请求总HP整除分母，再由中央HP过程取整／夹限／极小值处理；不能把请求0写成保证不改变HP。新获得物可在持物检查立即消耗并触发SYMBIOSIS等，最终持有物不一定仍是刚取到者。还原记录“为空才补”／“野生转移”是各表明列的差异，不统称永远回到入战物品。

## 8. 场地变化（E）

OnTerrainChange唯一MIMICRY，普通有效才调用，不查接地，不使用ability_changed参数作额外拒绝。当前无场地则重置回基础类型并提示；否则电→电、青草→草、薄雾→妖精、精神→超能，目标类型数据存在才改类型／提示；未知或缺失类型保留原值。没有“已经相同就不通知”的本地守卫。

真实建立由§3.3全场先能力后物品。自然到期先当前设无并全场能力恢复，若有默认场地则建立默认（内部能力→物品），之后外层再次能力→物品。因此拟态可恢复一次、对默认类型变更提示两次；重复检查道具也未去重，但已消耗物可能不再满足资格。能力失去后置也调用本接口，读取的是**当前**能力，所以失去MIMICRY本身不保证立即通过旧MIMICRY重置类型。调试菜单退出亦有天气／场地再检查入口，未操作真实调试菜单。

## 9. 注册表外直接生命周期（F）

### 9.1 持续检查与舞者

TRACE：持续检查先强天气结束，再当前TRACE有效则从存活对侧选能力可获得且非POWEROFALCHEMY／RECEIVER／TRACE者，均匀抽一个复制（不要求来源能力此时有效），展示；空集合保留TRACE，后来每次行动结束、回合末或进入场景的持续检查可重试，包括旧世代5，不强行限制只在初次入场。复制成功后是否触发新入场项按§2。行动结束用自然存活集合，回合末用WP42缓存速度序，不能统一成同一顺序。

DANCER：外层不是舞者递归、U未失败、真实击数>0、招式舞蹈、未被抢夺／反射且有全局有效舞者时，按速度序收集除U之外的有效拥有者，再从尾部取，即慢者先（同速沿缓存的逆向顺序）。每个先保存已行动轮／暴走计数／当前招式，已有暴走正计数先＋1，计算目标：与U对立或原选择目标与舞者同侧时改为U，否则保留原目标；展示、设舞者标记，选择资格过则简单使用，恢复三项，裁判，若终局立即返回可留下舞者标记真；正常继续才清标记。资格失败时不执行恢复三项的成功分支，故先加的暴走计数也不被统一回滚；标记仍在正常后段清。候选集合一开始固定，逐个取出时不重新以能力是否仍DANCER筛集合，但使用招式入口还有其存活与使用门。两使用标志与PP合同沿WP40，不额外消耗原槽PP。

### 9.2 直接形态与受击差异

通用形态请求拒倒下、变身或当前相同形态；保存旧缺HP量，提交形态并更新数据，再以新上限减旧缺量调整场上HP；世代≥6清临时重量，更新外观／已见。这不是随意恢复满HP，也不据此关闭WP22所有持久形态机制。

| 能力／直接检查 | 时点与局部规则 |
| --- | --- |
| FORECAST／FLOWERGIFT | 存活非变身者天气检查；CASTFORM有效FORECAST按晴1／雨2／冰雹3／其它0，失去有效能力回0；CHERRIM有效FLOWERGIFT晴1否则0，失效回0 |
| ICEFACE | EISCUE形态1、身份ICEFACE、有效冰雹且天气检查不是“能力改变”时置可恢复标记；回合末／入场恢复见前表，不能把天气通知等同当场立刻恢复 |
| ZENMODE | DARMANITAN身份匹配，入场／回合末检查：HP≤总HP整除2且偶形态则＋1；高于界且奇形态则−1 |
| SHIELDSDOWN | MINIOR匹配：高于半血且形态≥7则−7；否则半血及以下且形态<7则＋7 |
| SCHOOLING | WISHIWASHI匹配，等级≥20且HP>总HP整除4为形态1，否则0 |
| POWERCONSTRUCT | ZYGARDE匹配，仅回合末，HP≤半、形态<2，形态＋2 |
| HUNGERSWITCH | MORPEKO且能力有效，仅回合末在0／1间切换 |
| STANCECHANGE | AEGISLASH原身份匹配，使用招式前本次类型计算之前，伤害招形态1，KINGSSHIELD形态0；形态请求仍有倒下／变身拒绝 |
| PROTEAN／LIBERO | 普通有效、非调用其它招式、未抢夺、有不同当前类型且本次类型非伪类型时改为本次类型；此快照无每次入场一次限制。诅咒转换为幽灵后空目标会重新选对手，不把官方自我诅咒修入 |
| BATTLEBOND | 存活非变身且对侧队伍未全灭，GRENINJA匹配、本个体战斗牵绊未用、形态1且本次击倒数>0；标已用并改形态2 |
| GULPMISSILE使用后 | 同样存活非变身／对侧未全灭通用门，CRAMORANT原身份、形态0；冲浪且击数>0或潜水蓄力回合，HP>半为1否则2 |
| DISGUISE／ICEFACE吸收 | WP43§7：替身更早；模式破坏者假、对应物种及形态0，冰脸还要求物理。原能力身份查询不套普通有效。后续画皮改1，世代≥8扣总HP整除8；冰脸改1。计算伤害哨兵与实际hpLost分别记账 |

吐导弹受击是每击T能力与U能力之间的直接分支：CRAMORANT身份匹配、形态>0且非变身，不普通有效查询；先请求形态0，再可受间伤的U扣总HP整除4，然后**读此时T形态**决定形态1降U防1／形态2麻痹。T存活且形态请求成功时已0，因此本快照不执行这两额外分支；T倒下导致形态请求拒绝时仍可能保留1／2并进入额外分支（中央资格仍适用）。不把这段按通行游戏直觉改写为总会产生储存形态附效。新有界差异记录于场景D08，不修改既有规格制造一致。

IMPOSTER变身请求：建立变身及复制物种记录，复制类型、能力、五项能力值、七阶级；新会心机制开时复制聚气／磨砺计数；替换场上招式各PP和总PP均5，清禁用、复制重量变化、刷新展示，最后失去旧能力后置。没有直接复制目标HP或等级，没有把当前能力写回持久个体。全部变身／还原、其它形态插件与持久覆盖仍WP22主域。

### 9.3 物品取得的能力接点

SYMBIOSIS：消费后若允许共生且自身存活无物，速度序首个同侧有效共生、持物且双方允许转移者把物给自己，来源清物／可置轻装，然后自己持物触发；此处不更新两份还原记录。先新物入手再触发，可能递归消费／共生，不补“一轮最多一次”守卫。CHEEKPOUCH：已触发物品是树果且能力有效、可恢复时，**实际移除自身物之前**请求总HP整除3恢复；自身物再消费，非自身物且非投掷入口也可共生。紧张感和复合能力阻对侧食树果，GLUTTONY允许夹攻树果阈值从四分之一扩到半血；RIPEN对具名树果恢复／升阶请求翻倍、减伤树果再减半。具体物品表、强制食用与消耗标志由WP50承接；已读本能力接点不宣称全部物品域闭合。

## 10. 具名静态场景

以下固定输入／手工状态推导不执行参考；除明列外无其它能力／物品／条款。中央状态／阶级按已审WP44、HP按WP43／20；消息次数只按已读正常控制流，不当真实宿主演出确认。

| ID | 前提／事件 | 预期与边界 |
| --- | --- | --- |
| L01 | 入场危害使新成员HP0且有DRIZZLE | 濒死→成长→裁判，跳该成员入场降雨；不先触发能力再判危害 |
| L02 | 非真实换入的两种对照：获得IMPOSTER且对面可变身；气体结束重调ICEFACE，拥有者存活非变身EISCUE、形态1且有效冰雹 | 两次入场回调的switch_in均假；IMPOSTER因标志门拒变身，ICEFACE不检查该标志，后者满足形态提交门则1→0 |
| L03 | 最后一只气体拥有者普通换下，另有存活SLOWSTART计数0／INTIMIDATE | 局部倒下后气体结束重调入场，慢启动5，威吓可再降攻；旧个体持久HP不归0 |
| L04 | 普通换出REGENERATOR总HP101、HP20、治疗封锁真 | 恢复请求33→53；正常终局同输入不由该处理器回血，外层治疗另计 |
| L05 | 一只同侧SOULHEART倒下，RECEIVER存活特攻0 | 第一遍继承SOULHEART，第二遍读新身份请求＋1；无需完整获得程序 |
| L06 | 中毒成员SYNCHRONIZE且来源对侧、剧毒计数正；来源毒免疫 | 原毒已提交，反射拒，随后自己的物品／能力治疗仍继续；不回滚原毒 |
| L07 | COMPETITIVE特攻0、对侧一次分别成功降攻与防 | 两次降阶通知，特攻0→2→4；同侧来源对照不升；来源空可触发 |
| L08 | STEADFAST速度0，已建立畏缩但尚未轮到行动 | 此刻仍0；实际因畏缩失败时请求＋1，本次依旧失败 |
| H01 | 总HP101，扣前50，扣后49，跨半记录开启且EMERGENCYEXIT有效 | 整数界50，严格低于成立；若扣后50不成立。恢复物品先回到50会清，后续退出不触发 |
| H02 | 训练家回合末跨半退出、可换且有后备 | 先召回／局部离场，当前不立即选换入，后续WP42补位；返回真不是已完成替补 |
| H03 | 野生敌方双席布局，EMERGENCYEXIT／WIMPOUT拥有者跨半标记真、能力有效、无天空摔投限制且后续逃跑资格过；另一同侧场上成员存活／已倒下两种对照 | 两名存活时人数门拒、返回假；另一名倒下后只剩拥有者，计数1，人数门不拒，后续置决定3并返回真。后备／空位不增加计数；玩家侧无这道额外人数门，仍查其它逃跑守卫 |
| D01 | T AFTERMATH倒下、U实际接触、U总HP101当前100，DAMP有效，模式破坏者关／开 | 关被DAMP阻止；开可扣25→75，之后恢复物品检查；T濒死不取消该受击回调 |
| D02 | EFFECTSPORE r29、随后抽毒，U钢类型；另r30对照 | 前者通过30%触发但中毒资格拒，不重抽睡；后者不作第二次状态抽取 |
| D03 | U有接触防护，碰到MUMMY，U原SLOWSTART计数2 | 能力赋值被接触许可拒，但仍失去／获得后置；原能力仍SLOWSTART，入场后置可把计数重设5 |
| D04 | 同一招击倒目标数2且对侧有后备；U MOXIE／CHILLINGNEIGH各攻0 | 前者＋2，后者只＋1；对侧全灭对照都跳，不保证最后击倒也升 |
| D05 | BEASTBOOST攻=防=100最高，攻阶级＋6、防0，击倒数1 | 并列选攻，封顶不升，不回退防御 |
| D06 | 目标BERSERK跨半真，但U有效SHEERFORCE且附效数据>0 | 后段二被跳，狂怒不升；U的OnEndOfUsingMove不由该总门跳过 |
| D07 | PICKPOCKET受击目标无物，原始接触，U已被红牌等换出 | U席位在已换集合，拒窃取，不能拿新换入个体物品 |
| D08 | 吐导弹T形态1，受击后仍活／已倒下，U可间伤总HP100 | 存活者形态先0、U扣25后不进形态1降防；倒下者形态请求拒，可仍进1分支请求降防。保留静态读后写差异 |
| E01 | HEALER有两异常盟友，固定r29／30 | 前者一次抽后两者均治，后者均不治，不是两个独立30% |
| E02 | 真实毒HYDRATION、当前雨期限1且无默认雨 | 天气先终止，到治疗族时非雨不治；期限2对照可治 |
| E03 | MOODY世代8，攻击0，其它四主阶级＋6，无其它资格改写；第一次选唯一可升攻击，第二次固定选防御 | 预先可降有五项；攻击0→＋2后从可降集合删攻击，剩防御／特攻／特防／速度四项；固定选防御使＋6→＋5，其它不变。命中／闪避不进入本代集合；旧代可入 |
| E04 | HARVEST回收树果、无物、晴／非晴r49／50 | 晴免抽必取；非晴49取50拒；取得后树果可能立即消耗，空还原记录才补 |
| E05 | PICKUP两个存活来源使用序号5／8，物品X／Y，拾取者空物 | 选Y，清其拾取记录、同物回收；若最终序号8对应空物，则不改选5的X |
| E06 | 拟态草类型，电场到期、默认精神场地非空 | 无场地先重置，再精神改变两次通知；不以已有超能而略后一次提示 |
| E07 | 一成员BADDREAMS效果伤害使决定已写，但后段当前成员仍活有可取物能力的变化 | 当前／后续处理按每步实际身份／有效性继续，直到主阶段显式检查；不能推导每个回调统一退出 |
| F01 | TRACE无可复制对侧，后来对侧换入可复制能力 | 首次保留TRACE，后续持续检查可成功，不限制世代5只能第一次 |
| F02 | 两舞者速度100／50，舞蹈成功且可选 | 收集快到慢，实际先50再100；嵌套带舞者标记防递归，不耗原槽PP |
| F03 | 舞者已有暴走2，但本次选择资格拒 | 预先＋1→3，成功恢复分支未到，正常后段仅清舞者标记；不自动恢复暴走2 |
| F04 | FOREWARN候选只有自身HP越高威力族及普通威力100 | 前者最终比较80，提示普通100，不按早先150选择 |
| F05 | 气体压制紧张感从有变无，全场3名存活树果持有者 | 可由外层3次各触发全场检查，消耗与否仍读各实际资格；不认定9次都产生物品效果 |

## 11. 不变量、失败、配置与依赖

能力消息不是提交成功保证，静默处理也可能已有字段改变。回调内中央升降／状态／恢复各有资格，封顶或拒绝可能部分成功；多次回调不默认去重。濒死HP、已处理濒死标记、已写决定和战斗终局不是一件事。普通离场与真实倒下／正常终局不统一；普通能力赋值与持久形态／物品写入也不同。

当前世代8，能力天气固定期限开、世代8威吓额外免疫与心情不定五项、碎裂铠甲速度＋2、画皮损血生效；能力提示条配置影响展示与部分查询路径，正文保留实际分支。概率均离散均匀抽取，30%用0..99<30；没有实测随机频率。缺能力／类型数据、插件扩展、异常中断及真实宿主显示不承诺统一恢复。完整普通异常／显式中止边界引用WP42§8，不把上述后置链写成finally。

完成依赖及交界版本（WP42／48为**已限定通过的管理回填版本**，其它为已限定通过的当前管理维护版）：

- specs/combat/wp41-switching-positioning-and-escape.md：`1b7e395b98727e3aa7272ad73d3873c77f4581d0acd18ac71cc6703736a77ccb`（31,948字节），限定已审当前版。
- specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md：`8b8149c3b1f6ee7d130802a4fe1638404a5ac76e7927ee4ce77c85ee5127620f`（41,759字节），已限定通过的管理回填版本；被审v2 `6644c77775b1e02481674079c847652dbbf2c566214d3969f1f333f741c22f7d`（41,329字节）留史；被审v1 `9bde1314b9b96f36fa243abfd0ca965775dd651c7861e0f20f475d5f83d97161`（37,859字节）保留历史。
- specs/pokemon-rules/wp48-ability-calculation-modifiers.md：`457a47b0438a5664fa75e1988251e5aefea2620efec0c006c4f78f7c12a00611`（35,320字节），已限定通过的管理回填版本；被审v2 `87e39127e14eddd10f6e0d10e6d63999e0cb9ff70fa0e2505dc97a195f3b3bb8`（35,021字节）留史；被审v1 `480016af9731a97607300ae84851b6b6286ae624b1452a0193b849295f2b3728`（34,233字节）保留历史。
- specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md：`a4e82ddf09d9d9db4e4d610e8dc074d5ef093136b74290dd83b84f764a6bdf9c`（50,426字节），限定已审当前版。
- specs/combat/wp45-weather-terrain-side-and-position-effects.md：`7ddb026aa71e8576d54ab2f98df5e78e84066e28eccbada4f551ca5ae58e5d95`（36,525字节），限定已审当前版。

前向责任：WP22完整形态／变身及持久还原，WP23完整Shadow，WP46／47全部招式前门／多击及嵌套，WP50具体物品族／恢复值与消耗组合，WP38球记录产生与捕获接收，WP51/52及53–58的AI／设施组合；这些包启动或改变本包输入时复核§2–9。WP42主阶段、WP48有效性及数值已在本批联合核对，不以循环引用遮蔽自己的调用合同。Demo／宿主／媒体／插件、U01–U10、WP78→79→80仍未关闭。

## 12. 来源与证据范围

以下相对`Data/Scripts/`，全部只读；源码标识只审计，不构成实现设计。

- 能力目录`011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb`的1–294共享声明／包装，以及367–408、511–665、795–817、864–882、1661–2548、2575–3200本包正文已逐段读取；与WP48互补覆盖3208行文件的全部登记。不能按注释“None!”漏掉QUICKDRAW反馈。
- `011_Battle/002_Battler/006_Battler_AbilityAndItem.rb:1–476`全文；`010_Battler_UseMoveTriggerEffects.rb:1–218`全文；`003_Battler_ChangeSelf.rb:1–115,155–328`；`001_Battle_Battler.rb:61–129,344–420,598–613`。
- `011_Battle/001_Battle/005_Battle_ActionSwitching.rb:278–377`；`011_Battle_EndOfRoundPhase.rb:1–83,473–499,600–722`，主全序沿WP42全文证据；`001_Battle.rb:735–818`；`002_Battle_StartAndEnd.rb`终局调用沿WP42；`008_Battle_ActionOther.rb:135–175`；`009_Battle_CommandPhase.rb:149–170`；`010_Battle_AttackPhase.rb:1–25`。
- `011_Battle/002_Battler/004_Battler_Statuses.rb:238–266`及迷恋／混乱后置调用检索（已有资格／治疗主规则WP44）；`005_Battler_StatStages.rb:101–120,195–240,278–378`；`007_Battler_UseMove.rb:97–116,205–227,343–366,490–576,664–717`；`009_Battler_UseMoveSuccessChecks.rb:240–260`。
- `011_Battle/003_Move/002_Move_Usage.rb:147–199,329–352`；`007_MoveEffects_BattlerOther.rb:934–1005,1020–1045,1066–1082,1135–1191`只取能力赋值／压制与后置调用，不据此宣称该招式全集完成；`010_Data/001_Hardcoded data/008_Stat.rb`全文核遍历顺序。
- 全Scripts注册／调用检索；AI调用仅定位，未作为真实阶段证明。能力数据与配置输入继承WP48／WP02，真实事件可达性缺口沿WP01。注册族联合身份检查是文本集合证据，不代替上面具体行为阅读。

本轮定点回读：能力目录`:367–408,1123–1137,2436–2464,2820–2848`，共享入场包装`:264–266`；Battle集合／规模`:204–206,448–475`；AbilityAndItem`:43–70`；StatStages`:1–34,123–141`及已审中央阶级合同；逃跑查询`:5–22`。R01以存活计数为准，C01校准合法MOODY输入及ICEFACE回调标志；其余来源继承首稿。

## 13. 有界登记覆盖与提交状态

本包21族，106直接登记＋13复制语句，展开为119个（族，能力）身份；OnStatGain空，其余20族有登记。与WP48联合为48族、239直接＋24复制语句；展开总267身份，主归属无重叠。copy首身份是来源，余身份新增。

| 族 | 种类 | 审计身份／复制方向 | 源起行 | 具体合同 |
| --- | --- | --- | ---: | --- |
| OnHPDroppedBelowHalf | add | EMERGENCYEXIT | 367 | §5 |
| OnHPDroppedBelowHalf | copy | EMERGENCYEXIT、WIMPOUT | 408 | §5 |
| OnStatusInflicted | add | SYNCHRONIZE | 515 | §5 |
| StatusCure | add | IMMUNITY | 558 | §5 |
| StatusCure | copy | IMMUNITY、PASTELVEIL | 570 | §5 |
| StatusCure | add | INSOMNIA | 572 | §5 |
| StatusCure | copy | INSOMNIA、VITALSPIRIT | 584 | §5 |
| StatusCure | add | LIMBER | 586 | §5 |
| StatusCure | add | MAGMAARMOR | 598 | §5 |
| StatusCure | add | OBLIVIOUS | 610 | §5 |
| StatusCure | add | OWNTEMPO | 637 | §5 |
| StatusCure | add | WATERVEIL | 652 | §5 |
| StatusCure | copy | WATERVEIL、WATERBUBBLE | 664 | §5 |
| OnStatLoss | add | COMPETITIVE | 804 | §5 |
| OnStatLoss | add | DEFIANT | 811 | §5 |
| PriorityBracketUse | add | QUICKDRAW | 864 | §5 |
| OnFlinch | add | STEADFAST | 876 | §5 |
| OnBeingHit | add | AFTERMATH | 1661 | §6 |
| OnBeingHit | add | ANGERPOINT | 1691 | §6 |
| OnBeingHit | add | COTTONDOWN | 1709 | §6 |
| OnBeingHit | add | CURSEDBODY | 1720 | §6 |
| OnBeingHit | add | CUTECHARM | 1749 | §6 |
| OnBeingHit | add | EFFECTSPORE | 1768 | §6 |
| OnBeingHit | add | FLAMEBODY | 1816 | §6 |
| OnBeingHit | add | GOOEY | 1833 | §6 |
| OnBeingHit | copy | GOOEY、TANGLINGHAIR | 1840 | §6 |
| OnBeingHit | add | ILLUSION | 1842 | §6 |
| OnBeingHit | add | INNARDSOUT | 1853 | §6 |
| OnBeingHit | add | IRONBARBS | 1871 | §6 |
| OnBeingHit | copy | IRONBARBS、ROUGHSKIN | 1890 | §6 |
| OnBeingHit | add | JUSTIFIED | 1892 | §6 |
| OnBeingHit | add | MUMMY | 1899 | §6 |
| OnBeingHit | add | PERISHBODY | 1925 | §6 |
| OnBeingHit | add | POISONPOINT | 1947 | §6 |
| OnBeingHit | add | RATTLED | 1964 | §6 |
| OnBeingHit | add | SANDSPIT | 1971 | §6 |
| OnBeingHit | add | STAMINA | 1977 | §6 |
| OnBeingHit | add | STATIC | 1983 | §6 |
| OnBeingHit | add | WANDERINGSPIRIT | 2001 | §6 |
| OnBeingHit | add | WATERCOMPACTION | 2037 | §6 |
| OnBeingHit | add | WEAKARMOR | 2044 | §6 |
| OnDealingHit | add | POISONTOUCH | 2061 | §6 |
| OnEndOfUsingMove | add | BEASTBOOST | 2087 | §6 |
| OnEndOfUsingMove | add | CHILLINGNEIGH | 2106 | §6 |
| OnEndOfUsingMove | copy | CHILLINGNEIGH、ASONECHILLINGNEIGH | 2118 | §6 |
| OnEndOfUsingMove | add | GRIMNEIGH | 2120 | §6 |
| OnEndOfUsingMove | copy | GRIMNEIGH、ASONEGRIMNEIGH | 2132 | §6 |
| OnEndOfUsingMove | add | MAGICIAN | 2134 | §6 |
| OnEndOfUsingMove | add | MOXIE | 2174 | §6 |
| AfterMoveUseFromTarget | add | BERSERK | 2188 | §6 |
| AfterMoveUseFromTarget | add | COLORCHANGE | 2197 | §6 |
| AfterMoveUseFromTarget | add | PICKPOCKET | 2211 | §6 |
| EndOfRoundWeather | add | DRYSKIN | 2250 | §7 |
| EndOfRoundWeather | add | ICEBODY | 2276 | §7 |
| EndOfRoundWeather | add | ICEFACE | 2291 | §7 |
| EndOfRoundWeather | add | RAINDISH | 2304 | §7 |
| EndOfRoundWeather | add | SOLARPOWER | 2319 | §7 |
| EndOfRoundHealing | add | HEALER | 2336 | §7 |
| EndOfRoundHealing | add | HYDRATION | 2363 | §7 |
| EndOfRoundHealing | add | SHEDSKIN | 2388 | §7 |
| EndOfRoundEffect | add | BADDREAMS | 2417 | §7 |
| EndOfRoundEffect | add | MOODY | 2436 | §7 |
| EndOfRoundEffect | add | SPEEDBOOST | 2468 | §7 |
| EndOfRoundGainItem | add | BALLFETCH | 2483 | §7 |
| EndOfRoundGainItem | add | HARVEST | 2497 | §7 |
| EndOfRoundGainItem | add | PICKUP | 2514 | §7 |
| OnSwitchIn | add | AIRLOCK | 2575 | §3 |
| OnSwitchIn | copy | AIRLOCK、CLOUDNINE | 2586 | §3 |
| OnSwitchIn | add | ANTICIPATION | 2588 | §3 |
| OnSwitchIn | add | ASONECHILLINGNEIGH | 2622 | §3 |
| OnSwitchIn | copy | ASONECHILLINGNEIGH、ASONEGRIMNEIGH | 2635 | §3 |
| OnSwitchIn | add | AURABREAK | 2637 | §3 |
| OnSwitchIn | add | COMATOSE | 2645 | §3 |
| OnSwitchIn | add | CURIOUSMEDICINE | 2653 | §3 |
| OnSwitchIn | add | DARKAURA | 2671 | §3 |
| OnSwitchIn | add | DAUNTLESSSHIELD | 2679 | §3 |
| OnSwitchIn | add | DELTASTREAM | 2685 | §3 |
| OnSwitchIn | add | DESOLATELAND | 2691 | §3 |
| OnSwitchIn | add | DOWNLOAD | 2697 | §3 |
| OnSwitchIn | add | DRIZZLE | 2709 | §3 |
| OnSwitchIn | add | DROUGHT | 2715 | §3 |
| OnSwitchIn | add | ELECTRICSURGE | 2721 | §3 |
| OnSwitchIn | add | FAIRYAURA | 2730 | §3 |
| OnSwitchIn | add | FOREWARN | 2738 | §3 |
| OnSwitchIn | add | FRISK | 2790 | §3 |
| OnSwitchIn | add | GRASSYSURGE | 2811 | §3 |
| OnSwitchIn | add | ICEFACE | 2820 | §3 |
| OnSwitchIn | add | IMPOSTER | 2833 | §3 |
| OnSwitchIn | add | INTIMIDATE | 2851 | §3 |
| OnSwitchIn | add | INTREPIDSWORD | 2870 | §3 |
| OnSwitchIn | add | MIMICRY | 2876 | §3 |
| OnSwitchIn | add | MISTYSURGE | 2883 | §3 |
| OnSwitchIn | add | MOLDBREAKER | 2892 | §3 |
| OnSwitchIn | add | NEUTRALIZINGGAS | 2900 | §3 |
| OnSwitchIn | add | PASTELVEIL | 2934 | §3 |
| OnSwitchIn | add | PRESSURE | 2950 | §3 |
| OnSwitchIn | add | PRIMORDIALSEA | 2958 | §3 |
| OnSwitchIn | add | PSYCHICSURGE | 2964 | §3 |
| OnSwitchIn | add | SANDSTREAM | 2973 | §3 |
| OnSwitchIn | add | SCREENCLEANER | 2979 | §3 |
| OnSwitchIn | add | SLOWSTART | 3016 | §3 |
| OnSwitchIn | add | SNOWWARNING | 3030 | §3 |
| OnSwitchIn | add | TERAVOLT | 3036 | §3 |
| OnSwitchIn | add | TURBOBLAZE | 3044 | §3 |
| OnSwitchIn | add | UNNERVE | 3052 | §3 |
| OnSwitchOut | add | IMMUNITY | 3064 | §4 |
| OnSwitchOut | add | INSOMNIA | 3072 | §4 |
| OnSwitchOut | copy | INSOMNIA、VITALSPIRIT | 3080 | §4 |
| OnSwitchOut | add | LIMBER | 3082 | §4 |
| OnSwitchOut | add | MAGMAARMOR | 3090 | §4 |
| OnSwitchOut | add | NATURALCURE | 3098 | §4 |
| OnSwitchOut | add | REGENERATOR | 3105 | §4 |
| OnSwitchOut | add | WATERVEIL | 3113 | §4 |
| OnSwitchOut | copy | WATERVEIL、WATERBUBBLE | 3121 | §4 |
| ChangeOnBattlerFainting | add | POWEROFALCHEMY | 3127 | §4 |
| ChangeOnBattlerFainting | copy | POWEROFALCHEMY、RECEIVER | 3140 | §4 |
| OnBattlerFainting | add | SOULHEART | 3146 | §4 |
| OnTerrainChange | add | MIMICRY | 3156 | §8 |
| OnIntimidated | add | RATTLED | 3193 | §3 |

本包自身A～F上述范围按[独立闭合报告](../../review/wp42-wp48-wp49-recheck-2026-09-27/report.md)管理性回填Reviewed；原v2行为保持，仅同步WP42／48回填身份。完整形态／招式／物品／设施组合、运行及阶段出口继续保留；未修改reference、运行参考或提交／推送。
