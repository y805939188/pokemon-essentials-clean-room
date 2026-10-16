# Facility 有限物种资格依赖审读

实际审者：`/root/pbs_creature_facility/trait_eligibility`。固定 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`，R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。仅本证据目录可写；未提交、推送、安装或运行游戏/参考函数/独立行为模型。全部行为向量 `NOT_EXECUTED`，`UPDATE_NOT_STARTED`。请求 gpt-6.1-sol/ultra/default/Fast off；实际 model、effort、tier、speed 均 `UNVERIFIED`。

## 实读分母与接收范围

六个模板文件共 2,770 条：Tower 882、未被当前列表选择的 Fancy 618、当前单双 Fancy 共用的 Fancy-single 254、Little 369、Pika 284、Poke 363。原始模板全文信用属于父任务及 PBSW 原审者；本子任务只从它们定位物种，不冒充重复全文阅读。有限集合为 453 个基础 species，无模板指定形态后缀。为解析祖先另含 PRINPLUP。

默认与 Gen 5–8 的 pokemon/pokemon_forms 中，这 454 个物种及其已有形态有 2,732 个相关记录。逐记录提取 BaseStats、Abilities、HiddenAbilities、Height、Weight、Evolution/Evolutions、Flags、Incense（含缺省），按相同物种/形态及精确字段值结构关联去重为 649 行；已亲读 `species-fields.view.txt` 1–649 连续全文。`species-field-classes.json` 保留每处 PBS 文件、记录首尾、字段实际行号；关联去重不移除各配置语义。此信用为 **FULL_READ_RELEVANT_FIELDS**，不扩为物种每条招式/图鉴文本全文信用。

`finite-traits.json` 对直接模板 species 输出 2,727 个实际配置/形态字段表：默认570、Gen5 496、Gen6 536、Gen7 555、Gen8 570；差额5是仅作祖先依赖的 PRINPLUP。`default-base-traits.json` 为父组合证明用的453键基形表。表中资格列都是在已读定义支持下的静态推导，不是运行结果；脚本只机械整理字段、求和、单位和已明确的有限谓词，不授语义信用。限定字段未读0；以上表尚待父任务独立复核、接收，不能自行算接收完成。

备选 PBS 是分别采用完整 Gen5/6/7/8 数据集的前提，不能当成五套同时活跃。材料中未读取/运行实际编译的 species.dat；本表针对源 PBS 经已读编译规则形成的字段，不宣称真实宿主当前加载表一致。其它 species 全字段、地图 Demo、无界插件由各 primary 或真实边界分别处理。

## 真实 receiver 与创建次序

Species registry 的已读定义区分普通标识、复合形态标识及 species/form。查给定形态不存在时退基础记录；不存在 species 时数据查询仍可能空/异常，没有统一资格恢复。普通字符串转符号，重登记替换同键；类型检查与查不到异常保留。

PBS 六基础值依顺序为 HP、攻、防、速、特攻、特防；已读 Stat 定义确认每主属性的实际 pbs_order。编译对身高/重量乘10四舍五入并至少1，运行个体的身高和重量直接读当前形态数据；身高单位dm、重量hg。个体 baseStats 复制当前形态的六主属性，不用当前战斗能力、性格后能力、轻石或战斗重量。

形态缺省字段继承基础数据：缺省的六基础值、普通/隐藏特性、Flags等继承；缺省标量高重继承；没有非空进化表时复制基础进化表。普通物种缺省基础值每主属性至少1、高重各1、普通特性表空、进化表空。逆进化来自编译后的首条入边，不能从显示名或官方图鉴知识补造。形态最终分配优先按其 base_form 的形态入边，再退普通入边；编译还会给缺少真实普通边的基础种加 None 占位。

设施模板检查输入名称存在性：未知 species 被置空，未知 item/nature 置空，未知招式丢弃；无有效招式时取当前 registry 第一招式。EV词只认显式别名，丢其它词。模板创建先构造普通个体（不自动装等级招式，但保持创建形态复查开启），然后设置模板物品、重新抽PID、设置模板性格、友好0、已知招式、EV、统一IV并重算能力。RETURN 在 FRUSTRATION 已定义时转换。新建本身 steps_to_hatch=0，非蛋；无隐含野生持物。缺省性格按PID及 Nature registry顺序决定；设置模板性格覆盖它，未知/空性格恢复普通缺省。重新抽PID在创建形态钩子之后，所以不能用最终PID倒推所有创建时世界状态；此有限集合的动态钩子也不依PID。

普通特性索引缺省为PID最低位；无对应普通第二特性退第一特性，指定隐藏索引若该隐藏槽不存在也退PID普通路径。**StandardRestriction根本不查这个最终个体特性，而是扫描当前形态的普通 abilities 表**。隐藏特性单独列出供审计，不作为提前允许依据。

## 创建形态的完整有限分支

真实 MultipleForms 调用先按基础 species 选完整注册处理表，再按函数名调用；没有该函数返回空。赋形态会清个体特性缓存、重算能力并可能向玩家图鉴登记。普通 species_data 用 form_simple，资格读取不会主动调用外部世界 getForm；不能把任意时点动态 getForm 更新等同资格查询。

所有453个模板 species 的创建输入都是基形；除以下三种，其默认 Flags 未指定非零 DefaultForm，且已读注册/复制集合未给它们创建形态回调。因此本固定材料下创建形态为0。对这三种：

| species | 创建形态有限域 | 判定前提及资格影响 |
| --- | --- | --- |
| UNOWN | 0..27，各1/28 | 构造尾部独立随机选形态；全部相关资格字段继承基形。Factory具名禁UNOWN，Standard不因UNOWN身份拒。 |
| BURMY | 0/1/2 | 环境Rock/Sand/Cave→1，None→2，其余→0；全部资格字段/有效进化数量一致，BST224、高0.2m、重3.4kg、基础阶段且有有效后继。 |
| WORMADAM | 0/1/2 | 同环境选择。三种BST424且高重相同、普通特性表同、基础阶段均假、有效后继均空；六项分配不同仍须保留形态数据。 |

环境真实 receiver 先用地图 metadata.battle_environment，随后用玩家脚下地形，钓鱼遇敌则用面对地形；Forest遇Grass/TallGrass保留ForestGrass，其它有tile环境则覆盖地图环境。缺地图/玩家等属性可能异常；没有默认None统一兜底对象。

649行还完整列有限species的其它已定义形态，供已有个体/改形态后报名审查，并不意味着基础模板会随机生成Mega或地区形态。比如 VENUSAUR基形525可过Standard，Mega625拒；TYRANITAR的具名提前允许对其Mega仍有效。此有限材料中会让有效后继布尔随形态变化的species有 FARFETCHD、MRMIME、PICHU、CORSOLA、LINOONE；其中PICHU0有有效后继、PICHU2只有None。它们在冷缓存表分列，不能折成物种永恒属性。

## 所有工厂、直接样本与模式的资格谓词

以下变量对正常个体定义：s为基础species，f为当前form_simple，ℓ为当前等级，a为当前形态**普通**特性表，t为六基础值总和。S先拒空/蛋，再按顺序：a含TRUANT/SLOWSTART→真；否则s属于DRAGONITE/SALAMENCE/TYRANITAR→真；否则s属于WYNAUT/WOBBUFFET→假；否则t<600。H表示当前身高≤20dm，W20/99分别表示当前重量≤200/990hg。

B表示 s等于当前全局baby缓存[s]。键不存在时，以当前形态get_baby_species结果填一次；默认不查孵化Incense物品，会沿首次逆进化递归到祖先（首步之后查询祖先的基础记录），包括None描述的逆边。U表示先B，再取当前全局canEvolve[s]为真；缓存尚未赋值时，它填当前形态中非逆向且方法不是None的后继记录是否非空。它不执行等级/道具/性别等进化条件；false缓存也保留。两缓存都不按形态/配置刷新。cold表只表示首次查询该形态时的结果，后续必须传入真实共享缓存状态。

D为所有成员基础species两两不同，形态不同仍冲突。I为有持物者item_id两两不同，无物可重复。T(c)为整队等级和≤c。K为当前持物非BERRYJUICE/DEEPSEATOOTH，已会招式无SONICBOOM/DRAGONRAGE，species非SCYTHER/SNEASEL/MEDITITE/YANMA/TANGELA/MURKROW。普通 team最终判定另先检查非空成员及人数范围。

| 规则入口 | 最终人数 | 每成员有限谓词 | 全队谓词 |
| --- | --- | --- | --- |
| Pika工厂 | 恰3 | S且15≤ℓ≤20 | D且I且T(50) |
| Poke工厂 | 恰3 | S且50≤ℓ≤55 | D且I且T(155) |
| Prime工厂 | 单3/双4 | 非空即可，未装蛋/倒下/等级成员门 | D且I |
| Fancy工厂 | 恰3 | S且25≤ℓ≤30且H且W20且B | D且I且T(80) |
| Little工厂 | 单3/双4 | S且U且ℓ≤5 | D且I |
| StrictLittle工厂 | 恰3 | S且U且ℓ≤5且K | D；未装I |
| Tower工厂 | 单3/双4 | S | D且I |
| Palace工厂 | 单3/双4 | S | D且I |
| Arena工厂 | 恰3单打 | S | D且I |
| Factory工厂 | 单3/双4 | s≠UNOWN且ℓ≤100(open)或≤50(非open)，未装S/蛋/倒下门 | D且I |
| 直接StandardRules(n,L可选) | 1..n；n<0公开最大6 | S，L存在时另ℓ≤L | D且I |
| 直接StandardCup | 1..3 | S且ℓ≤50 | D且I |
| 直接DoubleCup | 1..4 | S且ℓ≤50 | D且I |
| 直接FancyCup | 1..3 | S且ℓ≤30且H且W20且B；无最低25 | D且I且T(80) |
| 直接LittleCup | 1..3 | S且ℓ≤5且B；无有效后继门 | D且I |
| 直接LightCup | 1..3 | S且ℓ≤50且W99且B | D且I |
| mode1 | 1..所给n；负n公开最大6 | S且ℓ≤100 | D且I |
| mode2 | 同上 | S且ℓ≤100 | D且I |
| 其它mode | 同上 | S且ℓ≤50 | D且I |

mode不调用setDoubleBattle，所以人数不会因单双重新变3/4；Arena只强制单布局，保留给定n。这里的mode100来自当前MAXIMUM_LEVEL=100。已有规则对象使modeToRules不被重建；Factory register额外装租借数据和把局部numPokemon改3等边界由父会话证据接收，不能把Factory工厂谓词无条件套到注册路径。

成员条件按加入顺序求合取，先失败即返；无内置最低1级成员门，普通创建等级写口自身检查1..100。最终人数的下限/上限先判，随后成员、整队、真实独立子集列表。普通addSubsetRule实际写入整队列表，故T是上述整队谓词；不能改为只存在一个子集满足。所有普通工厂和直接样本都至少有D，所以存在性查组最终仍会逐组用完整成员+队伍谓词。

建议等级由最后最小/最大成员门与真实独立subset列表算，默认T没有进入该列表；因此Pika/Poke/Fancy的构造等级20/55/30使恰3人组总级60/165/90分别超50/155/80。直接Fancy建议30，建议3但最少1：对手候选池≤3走无校验返回，>3走3人重复抽样不能通过T；不能把无校验分支结果算资格成功。父任务另作有限池可行性证明。

## 表的消费规则与静态反证

`default-base-traits.json`：父可在正常生成、已采用默认PBS、只生成当前模板基形（动态三种字段资格等价）、cold或与该基形同值缓存前提下按上述组合筛选。`*_species_cold`均未含等级、全队D/I/T，strict还未含其物品/招式门。`standard_non_egg`必须另外排空/蛋；Factory仅species列不含其最高等级。

静态核验对照均未执行：Slaking670因普通TRUANT提前允许，Metagross600拒；Articuno580与Phione480允许，标签不构成黑名单；Wynaut260因具名拒；Pikachu即使身高/重量通过，也因Pichu祖先不满足B；Pichu2先填canEvolve=false后Pichu0仍拒U，反序先填true则Pichu2可被缓存放过。两个Pichu不同形态仍在D冲突。Factory可接受正常非UNOWN的Metagross600但仍受自身等级及D/I；Prime额外不装标准门。

本子任务未提出新的required。WP54主稿§3及附表§1–3已经明确普通特性优先、形态共享缓存、有效后继与工厂/直接/mode差异；这里补有限PBS接合证据，不把补证自动当正式缺项。发现判定与父独立反证/全局裁决分列。实际运行、真实缓存历史、真实编译存档及世界选择继续未知，不升级SOURCE_STATIC。
