import json,pathlib,datetime,hashlib
P=pathlib.Path(__file__).parent;NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
s=json.loads((P/'sourcefact-consumer-receptions.json').read_text())
# Each entry is manually authored for this fact, not inferred from tokens or old PASS.
entries=r'''
1|species_data用form_simple读取已编译记录；calc_stats/level招式/类型和身高查询据此，不因此调用getForm；UI精灵先读普通form是另一先行路径。
2|species=先解析目标Species再比较base species；同基早返不清forced_form/缓存或calc，形态别名输入不因此强制改变当前form。
3|异基species=优先getFormOnCreation默认标记（若存在），否则目标显式非零form，最后0；产蛋inherit_form和Evolution后续提交是独立写入。
4|异基提交species与form后清forced_form、条件性别、level、abilityindex/ability，calc可再次填nature/HP；并非清全部shiny或nature缓存。
5|forced_form非nil先返回；不先读取inBattle/in_storage或执行动态handler，species_data/simple仍用保存form。
6|无强制时inBattle或in_storage真返回保存form，仓库正常出口才清标志；异常出口可影响随后Summary/Sprite普通form读取。
7|MultipleForms.getForm非nil且与保存值不同才form=；0在Ruby真值且参与不同值比较；Full FormHandlers定义已读，不再声称所有处理器未读。
8|form=即使同值仍写form、清ability缓存、onSetForm、calc、条件全局图鉴；Hoopa/UI回调可嵌套重入，外层后继时间戳仍继续。
9|onSetForm在calc和global Pokedex.register前；任何早期异常保前缀且阻后段，记录接收者为$player而非回放battle player副本。
10|setForm先写并清缓存，yield后才onSetForm/calc/register；融合/进化界面在yield里可修改其它对象，取消或异常无通用回滚。
11|form_simple=只写form和calc；不调用onSetForm/图鉴且不清ability解析缓存；Shadow/捕获离场的具体显式form入口另列。
12|level缓存为空时由当前species growth_rate和exp求并缓存；Shadow可把exp增量改存saved_exp，不能把外层exp=当普通写入。
13|level=先校验1..max再改exp和level缓存；ItemUtilities升级/设施调整/DayCare成功分支都继承此门，早期消息/道具等由实际包装决定。
14|普通exp=只裸写exp并清level缓存，不立即calc；DayCare每步+1、战斗收益后继calc与Shadow暂存覆盖必须分别接合。
15|egg?仅hatch_steps>0；DayCare先基本蛋构造后写正步数再inherit_form，既有对象pbGenerateEgg可保留旧seen状态。
16|exp_fraction在level>=max直接0.0；否则用该曲线当前/下一等级阈值和exp比率；可见UI进度条不倒写exp。
17|hp=在当前totalhp上下钳；Battler普通同步进入该setter，离场raw hp=0局部写不等同；calc_stats仅条件self.hp=而非全程直接写。
18|hp归0调用heal_status并ready=false；Shadow heal_status受其覆盖门影响，不能推成所有HP0都必NONE；Battle局部faint与持久对象接合已收。
19|status=先!able?返，故蛋/濒死连未知status解析都不发生；合法非nil状态才规范注册id，Battler同步失败前缀独立。
20|成功status=只写@status不改statusCount；战斗poison复位在after_battle按status==POISON门另行count=0，与旧count正负无关。
21|able?与fainted?均先排蛋，再分别HP>0/<=0；Trainer筛选、伙伴资格、DayCare兼容和UI注释不能用非蛋数替代可用数。
22|heal_HP/heal_status/heal_PP/heal均在蛋守卫返；Interpreter314据HEAL_STORED配置遍历player或所有party/box，同一对象重复遍历可重复治疗。
23|heal_HP直接@hp=@totalhp，不走HP0setter副作用；Storage storeCaught先治疗后容量全满失败亦可保治疗，设施战前/战后亦会早治。
24|heal_status蛋门后写NONE和count0；默认Shadow不覆写该方法，普通heal_HP直接@hp写不经过Shadow hp=清hyper位，hyper_mode getter在HP0或heart0时另返回false。
25|heal_PP非负索引直接@moves[index].pp=total_pp；越界nil receiver可失败，负索引分支为全部迭代；战斗PP写穿与Leppa例外分别接收。
26|types返回species_data.types.clone，外层列表改动不改记录；每个元素Symbol共用无可变嵌套承诺；Battler局部类型另从接收包限定。
27|type2在当前列表第二项无值回第一项，空列表仍可nil；人工三类型记录不截成双类型，Type类effectiveness顺序已读。
28|gender懒缓存用PID低8位对GenderRatio.female_chance；之后改PID不重派，register/Summary/offspring会触发该读取。
29|单性/无性别species忽略gender=；普通setter仅0/1写，foreign gift的默认gender写不等于可改变Genderless记录。
30|shiny?独立缓存普通判定；Owner/PID变更不自动清缓存；DayCare重掷显式shiny=nil，Trade换Owner未替它清理。
31|super_shiny?有独立缓存与阈值；先查普通或超级的次序不产生统一失效协议，Summary/recording/Trainer overrides消费原缓存状态。
32|super_shiny=true同时ordinary=true；false只本缓存，nil再推导；构造trainer可直接override，两缓存不必一致。
33|ability_index nil由PID&1；写index后清ability解析缓存，记录可保hidden索引而实际回退普通能力；DayCare选择后续calc不保证index改写。
34|不存在hidden slot时ability解析退普通槽/首槽，但保@ability_index；后续form变更/图鉴读取不能把实际ability当storedindex。
35|ability=只要求GameData::Ability已注册，允许非species候选；Ability类name/description只是翻译查询，不反向校验候选。
36|ability_list枚举普通和隐藏原索引，普通第二槽重复或nil按实际分支；UI选择、Debug调用与设施模板用index和值区别。
37|Nature按PID%当前registry count并用登记序匹配；25个Nature完整定义已读；登记变更是外部前提，不能假定PID后写自动换nature。
38|nature=保存表现性格；nature_for_stats已覆盖时不calc，即使显示nature变而能力旧；Summary显示和DayCare遗传读表现性格。
39|nature_for_stats=无论值清除/同值都calc，若无覆盖则calc回表现nature；mint物品完整包装仅有限UI/Item来源，不扩全ItemEffects。
40|hasNature?无参只查@nature是否非nil，不填；ctor末calc会填表现nature，register仅必要gender/shiny，分别保缓存来源。
41|item=未知非nil id静默忽略；nil清物品但不直接清mail缓存，读取mail才清；战斗remove/restore、融合工具和GiveTake路径已有限接合。
42|mail getter在当前item非Mail或id不同清@mail；Mail对象自身字段可变，setter不会强制克隆；持物替换与邮箱转移保身份顺序。
43|reset_moves先依当前simple form的level表筛等级，重复保最新再取末四；自定义零招/超过四招夹具不是默认record承诺。
44|learn_move已会时移动同Move对象到尾部，其PP/ppup保留；battle学习包装可能再建Battler::Move，不能据局部包装说持久Move已换。
45|新增learn_move push新Pokemon::Move再只shift一次；超长人工列表不会被强制缩到4；普通合法四槽前提与畸形夹具分开。
46|record_first_moves整体按当前moves映射id，重复/顺序原样保；捕获先记录再入queue，TR背包只逐项追加，不误当全表重录。
47|add_first_move若include?则不追加；Tutor bymachine+oneuse成功后追加，Party ItemUse路径缺该包装，实际TM57 TR差异需两路径限定。
48|compatible_with_move?依Tutor表、等级全表、baby species egg表三支，不受当前level门；MAGNEMITE CHARGEBEAM在Tutor表且非等级表已实际核。
49|can_relearn_move?先蛋/Shadow排除，再等级已达未会或first_moves未会；UI SHOW_MORE_RELEARNABLE_MOVES只控制候选追加，BULBASAUR AMNESIA记录对照保留。
50|owner=类型校验后只换Owner引用，不清性别/异色/能力/nature缓存；Trade/foreign/Mystery/partner分别产生Owner，不根据新Owner强制所有派生刷新。
51|foreign?只ID或name不同，不读Owner.gender/language；服从FOREIGN门调用此谓词，Masuda另比较language，Owner可畸形name同值哈希碰撞样本另列。
52|timeReceived=调用to_i；Summary由Time.at显示，host实际时区/时间不补造；Trade/Hatch对来源/时间写顺序使用完整实际源。
53|timeEggHatched getter仅obtain_method==1返回Time.at；hatch写obtain_method=1和时间，已有来源其它值即使字段存在亦读nil。
54|name=nil或空/等当前species.name使@name=nil；species=不自动清昵称，evolution显式是否改名和Shedinja duplicate清名各自执行。
55|height/weight由simple form Species取整数十分单位，pbSize用height及raw IV/PID；resource选择普通form可先动态提交，勿把两读取合并。
56|calc_stats用ivMaxed对应IV最大值，stored iv仍原值；Summary personality、pbSize、Egg继承均读raw iv而非effective stats用值。
57|calcHP先base==1回1，HP强化与nature后续不进入该分支；SHEDINJA actualrecord未在本接收中全批准，规则夹具能力定义仍有界成立。
58|oldhp>0保持缺失量且至少1；species/form/nature/level/IV变化可能条件hp=触发副作用，不能误写为calc全直接@hp。
59|oldhp<=0仅newmax>oldmax时补差；普通濒死升级可复活，Evolution显式wasfainted后hp=0再calc另有保濒死包装。
60|clone重建IV、ivMaxed、EV哈希与Move对象/Owner；Shadow clone在非nil saved_ev逐项回写但未新建该哈希，因而仍共享；shadow_moves另clone，Shedinja duplicate后续替换/清理字段与原共享分开。
61|clone未新建markings/mail/fused；标记UI clone表后替换本方打断共享，直接数组append/共同Mail字段写穿；融合工具给主体保存原伙伴对象不克隆。
62|ctor @happiness=species_data.happiness不夹；Compiler u只要求非负整数，256可保留到ctor，后续changeHappiness/happiness=才夹255，不从普通PBS全50推类不可能越界。
63|ctor末calc_stats调用nature_for_stats→nature懒派生；即withMoves=false/creationrecheck=false仍Nature缓存；gender/shiny是否填取决之后登记/消费者。
64|ctor initialform==0且recheckForm真才getFormOnCreation；handler返回nil不提交；SINISTEA egg强制0/继承form属于EggGenerator之后包装。
65|getFormOnCreation返回0在Ruby真值，ctor仍form=并onSet/calc/globalregister；UNOWN随机0与1两样本都可能填gender/shiny缓存。
66|Owner.new局部Hash keys由值构造，同值id/name/gender/language可先合并遮蔽String验证；不能从validate无范围检查推额外name正常显示。
67|new_from_trainer复制已有trainer.language，不重新读host；partner注册先load/event再Owner逐个替换，后段失败不回滚先改成员。
68|new_foreign省language用2，不调用pbGetLanguage；foreigngift把Owner替换不改已有obtain_method；host英值2是独立映射巧合。
69|pokemon_party排蛋，able_party还排HP<=0，count分别length；实际party成员引用保留，Double/Triple fallback可能nil，伙伴是否能参战另一门。
70|remove_pokemon_at_index只validindex且其它able存在才delete_at；融合Handler忽略false的路径必须保工具/主体先写与伙伴仍留的结果。
71|Trainer.initialize先随机id再pbGetLanguage再party=[]；host语言错误可阻party赋值，Owner newfromexisting不重复此入口。
72|Player初始化money直接Metadata.start_money；schema u可大于MAX，显式money=才夹；metadata当前默认记录实读不替代变体能力定义。
73|character_ID/outfit先写后刷新charset；GamePlayer source对有效metadata/charset条件分支已读，画面资源失败不回滚已写编号。
74|money/coins/battle_points/soot setters先Integer验证再clamp；Mart/BP/slotmoney/soot实际写入顺序有限已接，读资源上限与初始裸值区别。
75|Pokedex.clear清seen/owned/forms/last/access列表但保unlocked_dexes原数组；summary firstunlock与refresh currentregion选择可因此不同。
76|set_seen refresh=false只写seen不刷新accessible；Battle.pbSetSeen含internal门而form提交global register无此门，回放与捕获direct调用分开。
77|seen_form?可懒初始化缺项三维数组；查询产生空记录，不等于seen/owned真；UI forms/Dex显示依此，但保存对象图会包含该懒写。
78|seen_forms_count只gender0/1每形态or，不数gender2独立栏；registergender2归0而set_last_form_seen原gender2可保，不能混算。
79|set_last_form_seen保原species参数键与gender，不先base归一；UI Entry解释由记录/帮助方法决定，不能把它等同register_last_seen。
80|register把个体gender==2映0记录seen_form，并可读普通shiny填缓存；形态提交在蛋存在时亦可写，EGG守卫由caller决定。
81|register仅last缺项首填，不覆盖已存在last；species/form登记未因此强制改变Summary下一次最近见到值。
82|register_last_seen总覆盖，保原gender并消费普通form（可动态提交）及shiny；Summary/条目提示先写再UI失败保写前缀。
83|unlock/lock负数或超regional count转national末位；-1是公开映射，不类比Storage其它负盒索引；全局metadata区域helper静态已接。
84|USE_CURRENT_REGION refresh仅当前region有seen则accessible，不读unlock；普通模式按unlocked遍历与national独立，regional cache/PBS整表已读。
85|PokemonBox长度0时empty?遍历全空true且full?无niltrue；正常默认30格前提与人工0格夹具各自有界。
86|maxPokemon任何box<0返6，但pbGetPokemon只有-1转party；box=-2容量/实际寻址可不一致，UI负盒消费者Chamber sentinel另有限接合。
87|只有-1读player.party，-2等按Array负索引真实取盒；不以容量helper重写底层寻址语义；regional代理保其实现错误。
88|pbCopy目标party不使用目标格，append原Pokemon并compact；source不删，所以两容器可同一对象；后续mail/HP/Owner写入双侧可见。
89|pbMove只有pbCopy真才delete源；UI先scene action再modelmove，model失败已可有画面前缀；不是copy原子事务。
90|pbStoreCaught先heal（配置）后找空位，全部满时-1保早治；Peer路径同对象，entry/nickname/dex早写也可先于最终存放失败。
91|RegionalStorage.pbMove只代理pbCopy，不删除source；无默认调用者仍审公开能力定义，未据没有caller删去此合同。
92|RegionalStorage.pbDelete使用未定义box变量（参数名不同）在调用时失败；前置region选择/boxgetter可能先执行，无默认成功推断。
93|getBoxBitmap精确/^box(\d+)$/匹配一行并捕获转整数，先写box.background后可用性校验；含LF多行不能强化为整字符串只数字。
94|storage UI给当前成员in_storage=true，正常尾部遍历false，无ensure；持有移出/先前异常对象可能保真并压动态form读取。
95|withdraw pbWithdraw先于storage.pbMove，成功模型移动后pbRefresh；scene动作非commit证明，原对象身份与afterfailureprefix保留。
96|hold先scene.pbHold，再@heldpkmn引用赋值后delete，异常可停在不同前缀；mail/fused/sharedstate不因此clone。
97|place party空格路径先按合法格/lastable等自己的门，不套用box mail/cannot_store门；交换/存盒分支另各守卫。
98|release pbConfirm默认No；拒绝前UI选择/持有状态可已有，确认后delete、dispose/refresh先后依单位；不把确认写成自动重建对象。
99|Summary characteristic用raw IV+PID%6环序，ivMaxed和naturestats不改变选项；locale翻译输出未运行，数据key选择静态可接。
100|Summary regionalnumber按第一个unlocked regional尝试并break，即查不到也不继续后一个；national fallback和currentregion Dex访问表并非同一算法。
101|Summary打开Dex先register_last_seen再scene构建，Entry构造/资源失败不回滚末次记录；UI region参数/shape消费已有限接收。
102|pbSize为静态公开能力，raw IV低4位与PID低字节进两段整除/15区间表，simpleheight；没有默认caller不妨碍定义审计，动态map调用存在性未全穷尽。
'''
manual={int(line.split('|',1)[0]):line.split('|',1)[1] for line in entries.strip().splitlines()};assert set(manual)==set(range(1,103))
G={
'FORM':dict(ids=list(range(1,12))+[55,64,65],own=['Pokemon','Species','Species_files','FormHandlers792L','Pokemon_Sprites','MegaEvolution','DayCare564L','EvolutionUI276L','Player_Pokedex'],received=['KERNEL SP01–15+catalog correction','UI73+5 parent units','UI bottle-fusion55','CORE F01,F09 and J02/J04','Chamber U015–02071facts+root receiver qualification'],premise='有效Species/表项和必要资源正常；固定R原默认handler集合已全文，不等于任意插件handler。产蛋、构造、显式提交、普通读取、simple读取按各自顺序。',production='Pokemon.new/species=/form=/setForm/form_simple=；EggGenerator.generate/inherit_form；EvolutionUI species=；Hoopa/Kyurem两个精确handler；catch离场form。',write_consume='form/cache先写→onSetForm/yield→calc→global Pokedex.register；Species(simple)读属性，Sprite(ordinary form)可先动态提交；UI refresh可重入。',failure='handler/yield/calc/register异常保已写前缀；Hoopa callback已refresh后外层仍写timestamp；fusion伙伴删除false不撤主体fused写。',remaining=['具体未在本任务或原贡献内读到的外部插件/地图事件form提交调用不计已穷尽；默认FormHandlers所有定义本身已全文','备份/替代species/forms/metrics的实际值见record-scope ledger，未从generic继承规则给全PBS批准']),
'LEVEL_EGG':dict(ids=list(range(12,17)),own=['Pokemon','GrowthRate188L全部六曲线','Pokemon_ShadowPokemon221L','DayCare564L','EggHatching','EvolutionUI276L','ItemUtilities917L'],received=['CORE F03,F04,F15','KERNEL SP+SAVE','UI Summary/Party complete finite'],premise='合法growth record；level输入1..MAX；Shadow覆写门按其实际定义；蛋由正hatch_steps确定而非名字。',production='构造level=/exp；DayCare步进slot.add_exp；Battle经验收益；Hatching步数消耗/取消；ItemUtilities changelevel。',write_consume='普通exp=清level懒缓存→level query→calc/moves/UI；Shadow已purify流程saved_exp置nil早于changelevel；蛋form提交可早写seen。',failure='level越界在自身exp/cache写之前抛；包装早期消息/stat/selecteditem写不因之回滚；collect_egg先生成再partyfull检查，因此构造副作用可留。',remaining=['真实host时间/随机及交互未执行；不是本地源码材料缺失','非原默认脚本的外部caller没有穷尽，不把它写成GrowthRate未读']),
'HP_STATUS_PP':dict(ids=list(range(17,26)),own=['Pokemon','Pokemon_Move','Status','Pokemon_ShadowPokemon','ShadowPokemon_Other','ItemUtilities','PokemonStorage','DayCare','Interpreter command314完整'],received=['CORE F01–F11+46atoms+5joins','CORE F12–F16 complete sourceunits','UI Party/Summary/Storage','UI facility-entry36/lifecycle63'],premise='有效当前HP上限、Move槽和状态记录；公开畸形索引可失败；Shadow覆盖前提与普通个体分开。',production='Battler同步/普通治疗/场景储存/DayCare deposit/设施preheal及postheal；command314按配置遍历party或party+boxes。',write_consume='Pokemon setter或heal直接写→Battler scene/离场→after_battle POISON count0与伙伴heal→UI；PP persistent普通写穿受身份/Transform门，Leppa同下标例外。',failure='蛋先返；status不可用先于规范解析；PP越界receiver失败；facility normal-tail恢复无ensure；after_battle后段失败保早count/HP/item写。',remaining=['未实际完整接收的其它Move/Ability/Item效果家族保本身责任范围；不借16CORE facts冒全战斗','真实native UI及存档roundtrip未执行']),
'DERIVED':dict(ids=list(range(26,41))+[56,57,58,59,62,63,99],own=['Pokemon','Species','GenderRatio','Nature全部25','Stat全部6','GrowthRate','Type完整','Ability完整','FormHandlers','WildEncounters','EncounterModifiers','DayCare','GameDataTrainer'],received=['CORE Battler完整有限','KERNEL Species+validation','UI Summary/P01–12/S01–13及finite DATA'],premise='当前registry、PID、Owner、raw IV/EV和显式override按给定夹具；普通个体与Shadow/disabledsetting变体分开；默认handler/PBS选例有真实记录。',production='ctor随机ID/IV→calcNature；wild/Trainer overrides；DayCare遗传rawIV/nature/index；form/species更新不同缓存集。',write_consume='懒gender/shiny/super/ability/nature缓存→Pokedex/offspring/Summary/Battler；calc有效IV覆盖但personality/size/继承读raw；HP条件setter。',failure='无自动跨字段统一失效；Owner/PID后写不能隐式清缓存；Registry/handler失败可停在已写PID/IV/覆盖后；UI显示不是反向重算保证。',remaining=['Type/Ability注册表类完整已读；不等于所有abilities/types PBS与全部战斗handler逐组合批准','备份species actual value差异需具名record阅读；Nature/Gender/Stat不再列为未读']),
'MOVES_ITEMS':dict(ids=list(range(41,50)),own=['Pokemon','Pokemon_Move','Mail125L','ItemUtilities917L','MoveRelearner','TutorChoose452–487','Species','Species_files','DayCare','Trading'],received=['CORE F12–F15含KnockOff168–189和ConsumeItem完整单位','UI Party Item/use/Move Summary有限','UI bottle-fusion55'],premise='有效Move/Item注册；slot列表普通4或显式畸形夹具区别；TM57实为TR，MAGNEMITE实际Tutor含CHARGEBEAM、等级表不含。',production='reset/learn/forget/record_first/add_first；背包TR pbMoveTutorChoose vsParty itemuse；战斗升级learn两路径；GiveTakeMail/融合/ConsumeItem。',write_consume='Move对象PP/ppup与list位置→Summary；record第一招在TR背包成功后追加，Party路径不自动追加；mail引用读时校正，耗物/initialItems终局另行恢复。',failure='通用learn取消返回false不写列表/record；满槽UI故障不推广零槽；Tutor earlier UI/movelist.map!可先改输入列表；stat计数/firstmove写先后精确保存。',remaining=['ItemEffects整个effects集合/全部技术机器数据未在本接收中全批准，已收Hoopa/Kyurem及TR路径有界','WP64完整邮箱UI/全部邮件展示与native资源并非单个Mail类FULL信用']),
'OWNER_ACQUIRE':dict(ids=list(range(50,55))+[66,67,68,71],own=['Owner','Trainer','TrainerLoadAndNew','Player','UtilitiesPokemon','Trading完整','EggHatching完整','MysteryGift完整','EvolutionUI完整','Obedience107–185','Trainer data class'],received=['KERNEL VAL/LANG/SAVE/EVT全部有限','CORE partner4','UI Party/Summary/Dex/Storage finite'],premise='Owner constructor同值Hash键碰撞需精确输入值；合法registry/player；host language尚未观察，其映射函数与Settings语言索引独立。',production='foreigngift既有对象或new；Trade clone/newOwner与source写；Hatch obtain_method1/time；MysteryGift下载标识/Owner/claim；partnerload/event/逐Owner。',write_consume='Owner引用→foreign? ID/name→obedience配置门；language→Masuda重掷；Summary Time.at与name显示；acquire登记/nickname/存party或box。',failure='先改Owner/来源/图鉴后UI/容量失败保前缀；Trainer hostlang失败发生随机id后party前；Trade/Hatch早演出stat与最终party槽替换有先后；无通用回滚。',remaining=['任意地图脚本/插件download/事件真实参与者没有全穷尽；完整默认包装定义已读不能再泛称Trade/Hatch/MysteryGift未读','host locale/Time/Marshal实际行为与异常、真实存档读回未执行']),
'COPY':dict(ids=[60,61],own=['Pokemon','Pokemon_Move','Owner','PokemonStorage','Pokemon_ShadowPokemon','Mail','DayCare','EvolutionUI'],received=['UI S11/B08 marking units','UI bottle-fusion55','UI facility lifecycle63','KERNEL SAVE objectgraph'],premise='Ruby clone/shallow引用语义仅按源静态；普通clone重建字段与Shadow override（saved_ev不重建、shadow_moves重建）另列；存储copy是整对象复用。',production='clone→Shedinja duplicate后续species/name/markings/item/ribbons/calc/heal→party.push；mail/fused后继mutator；storage copy。',write_consume='IV/maxed/EV/Move/Owner独立；markings/mail/fused共享→直接mutate写穿；UI marks替换数组只断一方；fusion保存同伙伴对象；Shadow saved_ev仍共享而shadow_moves另clone。',failure='duplicate已有clone后早写不改原被替换字段，但clearRibbons等共享性必须依据Pokemon.clone实际ribbons克隆；pbDuplicate push前失败无party提交；原对象其它shared fields仍按定义保。',remaining=['所有插件自定义mail/fused深图与隐藏host native/cycle重载身份未运行；native部分不冒源码事实','完整Mail内部类和Shadow override已读；不能保旧未读标志']),
'PLAYER_PARTY':dict(ids=[69,70,72,73,74],own=['Trainer','Player','Metadata','PlayerMetadata','TrainerSprites','GamePlayer charset/vehicles完整单位','Mart adapter/screen','BP adapter/screen','GameStats','TrainerCard','Soot step handler','BugContest pbEnd'],received=['CORE money F03/F04 fullunits','CORE partner4','UI Party/Pokedex/Dex/Storage full finite','KERNEL save/events'],premise='actual player对象和metadata；initial money裸读与资源setter校验不同；party一般有最多6或明确畸形夹具。',production='Player.new初值；shops actual money/BP setters；soot handler；party remove/fusion；Double/Triple和battle partnermerge。',write_consume='resource integerclamp→UI/Stats delta；GamePlayer charset在ID/outfit已写后；party筛选同成员引用；partner无参与路径保原party数组别名，有参与新数组旧成员对象。',failure='setter校验先于该字段写；Mart buy扣钱/加包及确认prefix按实际screen；fusion removefalse不撤旧写；BugContest还party早于昵称Store，可失败留恢复前缀。',remaining=['其它未具名地图事件/插件资源writer不计穷尽；现有商店/soot/charset实际单位已读','任意trainer版本记录和debug生成的全场景穷尽不从partner4转移批准']),
'DEX':dict(ids=list(range(75,85))+[100,101],own=['Pokedex','UtilitiesPokemon','Regional4helpers完整','regionalcompile593–629/write364–391','Species','Encounter','MiscPBS','regional_dexes整个212L','EggHatching','EvolutionUI','DayCare','PokeRadar','Entry construct/forms/area有限'],received=['UI D01–10/E01–06/S/DATA/X有限','CORE capture/seen/caught wrappers','UI recorded lifecycle63','KERNEL SP+SAVE'],premise='全局$player与battle player不同接收者；seen/owned/forms/last/access/unlock相互独立；region cache文件存在/构建native不执行。',production='捕获wrapper internal门/direct queue owned；form=任意来源含egg；acquire see_form提示；Hatch/Trade/Evo提示无see_form；Debug set_seen optionalrefresh。',write_consume='base species归一与原key APIs分开→seen_forms懒初始化→last首写/覆盖→region accessible→Summary/Dex list/Entry area；区域PBS原表/compile/cachehelper选择精确接合。',failure='提示消息后写last再开Entry，后失败保last；form callback前写不回滚；bad index national映射与实际array寻址分开；compile重建/clear cache不能从getter推已执行。',remaining=['全部encounters/metric备份实际记录与最终Data缓存载荷未全部审读；Entry area只具名必要完整单位','本地源/默认regional完整已读；真实cache文件/图形媒体/Marshal reload未执行']),
'STORAGE':dict(ids=list(range(85,99)),own=['PokemonStorage','Pokemon','Owner','Player','Pokedex','CatchAndStore','BattlePeers','Mail','DayCare','Chamber Screen348–628/SceneUpdate1072–1088'],received=['UI B01–12/P/S/PC complete finite','Chamber6units71facts+minimum receiver qualifier/rootreceipt','UI facilities entry36/lifecycle63','KERNEL SaveData17registration'],premise='基础Storage与Regional代理保持各自定义；-1党、其它负数组索引，Chamber自己的sentinel不反推基础统一策略；同Pokemon引用。',production='UI withdraw/hold/place/swap/release→model copy/move/delete；Catch Peer→storeCaught；DayCare deposit/withdraw引用；Chamber UI交换/净化后移除。',write_consume='scene先动作→模型后提交→UIrefresh；copy alias后hp/item/mail/Owner写穿；normal尾in_storage=false；主从容器变化不重建个体；player/storage各注册root。',failure='storeCaught早heal后full失败；release默认No；storage无ensure留in_storage；Regionaldelete undefinedbox；Chamber跨级pbPurify把Screen self作scene，第一次窗口callback缺pbUpdate前缀，Scene类本身有该方法。',remaining=['RegionalStorage实际默认caller未定位，但两个能力定义已静态审核；不要求有caller才成立','真实存档多根alias/cycle/资源与交互未执行；整个1308LChamber不冒本人FULL_READ']),
'SIZE':dict(ids=[102],own=['UtilitiesPokemon243–272完整pbSize','Pokemon raw IV/PID/height','Species'],received=['KERNEL Species height/defaults'],premise='合法raw6IV/PID以及contentheight；显式非默认输入按合同不夹raw值；两次整数阶段和15区间表分别拆。',production='公开pbSize能力；默认*.rb literal search只有定义，未据此宣称地图/动态不存在。',write_consume='只读rawIV低四位/PID低两字节/simpleheight，返回mm整数；不写EV/IV/个人缓存；无默认display/persist写点。',failure='合法tuple按15段边界；非法receiver/值失败不造成功输出；无确认/取消入口。',remaining=['动态地图/插件caller存在性未穷尽，定义本身及全部15段formal/vector已拆；不再列15段未拆','业务执行NOT_EXECUTED'])}
assert set(i for g in G.values() for i in g['ids'])==set(range(1,103))
# These group contracts bind actual named complete reads and received payloads. They do not assign PASS to parents.
for g in G.values():g['save_reload']='KERNEL SAVE01–07原reader完整有限接收：默认17顶层注册，player对象含party/Pokedex，pokemon_storage独立root，load验证/顺序/失败prefix已接；本任务没有执行dump/load，不从普通对象图静态推多root native alias/cycle已实证。'
for f in s['facts']:
 i=int(f['id'].split('F')[-1]);gs=[k for k,v in G.items() if i in v['ids']]
 # Derived source facts 55 etc can have multiple group-specific receivers; retain all.
 f['prior_consumer_open_at_initial_reception']=f.get('prior_consumer_open_at_initial_reception',f['consumers']['open'])
 f['whole_formal_clause_decomposition']='All1430 supplied oldlocators manually decomposed or bounded typed; fullglobal atomic denominator remains unfrozen. See exact parent children, never substitute this sourcefact.'
 f['premise_status']='MANUALLY_RECONSTRUCTED_SPECIFIC_AND_GROUP_PREMISES; FINITE_NAMED_RECEPTION_ONLY'
 f['manual_consumer_reassessment_v2']=dict(recorded_utc=NOW,reader='/root/creature_a_atomic_reception',specific_join=manual[i],complete_contract_refs=gs,source_identity_ledger='reading-ledger.json',named_payload_ledger='named_contributions with frozen original payload/common premises',source_credit='Own FULL_READ and original named reader reception remain separate',bounded_static_adoption=True,parent_acceptance_granted=False)
 f['consumers']['local']=list(dict.fromkeys(f['consumers']['local']+[g+':'+G[g]['production'] for g in gs]))
 f['consumers']['received']=list(dict.fromkeys(f['consumers']['received']+[g+':'+','.join(G[g]['received']) for g in gs]))
 f['consumers']['open']=list(dict.fromkeys(x for g in gs for x in G[g]['remaining']))
 f['consumer_completeness']='BOUNDED_NAMED_PRODUCTION_WRITE_CONSUME_DISPLAY_SAVE_JOINED; GLOBAL_DYNAMIC_DENOMINATOR_NOT_FROZEN'
s['manual_group_contracts_v2']=G;s['recorded_utc']=NOW;s['all_consumers_closed']=False;s['all_original_empty_consumers_replaced_with_explicit_local_received_open']=True;s['no_whole_domain_pass']=True
save('sourcefact-consumer-receptions.json',s)
# Static join interfaces rebuilt using the same manually authored complete contracts, not inherited old UNREAD strings.
I=[]
for k,g in G.items():I.append(dict(id='CAA-IF-V2-'+k,sourcefact_ids=['CRE-A-F%03d'%i for i in g['ids']],actual_contract=g,status='BOUNDED_STATIC_NAMED_JOINS_RECEIVED; GLOBAL_DENOMINATOR_UNFROZEN',open=g['remaining']))
save('interfaces.json',dict(schema='gr8-cre-a-interfaces/v2',recorded_utc=NOW,reader='/root/creature_a_atomic_reception',interfaces=I,actual_interface_denominator_frozen=False,whole_domain_pass=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED'))
print(json.dumps(dict(utc=NOW,facts=len(s['facts']),specific_manual_joins=len(manual),complete_group_contracts=len(G),interfaces=len(I)),ensure_ascii=False))
