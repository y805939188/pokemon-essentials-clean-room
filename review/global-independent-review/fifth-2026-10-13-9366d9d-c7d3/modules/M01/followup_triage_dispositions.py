"""One explicit disposition for every finite input row; old mappings stay intact."""
from followup_triage_common import *
from followup_triage_findings import NEW

by_new={f['id']:f for f in NEW}
def segment(route,scope,reason,existing=(),new=(),owner=None):
    return dict(route=route,subscope=scope,reason=reason,
       existing_findings=[canon(n,sub) for n,sub in existing],
       new_findings=[dict(id=f'GR5-M01-{n:03d}',status='candidate_pending_independent_counterevidence',
                         subscope=sub,anchor='findings.json') for n,sub in new],
       unique_main_rule=owner,reading_complete=True)
def old(number,scope,reason):return segment('existing_canonical_finding',scope,reason,existing=[(number,scope)],owner=f'GR5-M01-{number:03d}')
def new(number,scope,reason):return segment('new_finding_candidate',scope,reason,new=[(number,scope)],owner=f'GR5-M01-{number:03d}')
def ok(scope,reason,owner=None):return segment('existing_contract_sufficient',scope,reason,owner=owner)
def bounded(scope,reason,owner=None):return segment('definition_or_policy_boundary',scope,reason,owner=owner)

D={
0:[new(8,'作者收集来源选择、字面片段及事件原文组装','实际作者候选集合/原文值可变化，不能按“内部扫描器”一律免除；只补明确外部结果。'),
   old(2,'收集结果进入默认game的哈希过滤、替换/追加与同地图桶','C01已裁决；本条不重复立默认集合规则。'),
   ok('来源类别、共享/地图桶、超时部分结果','WP08§6.1已有明确承接，保留正确段落。')],
1:[new(9,'条件方括号编码使带前导空格的译文成为节头','具名相邻输入改变导入接受结果；不是仅输出排版。'),
   ok('字面转义标记与基本控制字符','WP08§6.2互换表和§6.3逆转义顺序已经决定保留的字面标记会被解码；无无损承诺，不另把每个标记碰撞立项。')],
2:[old(2,'导出条目由所选默认材料决定；目标语言独有键不扩充条目','采用母裁决修正：外层可能遍历较长语言域号，不能再写“只遍历默认域”；这部分主要是既有合同澄清，不额外独立required。'),
   ok('覆盖删除、输出分形态、稀疏事件桶','WP08§6.2–6.2.1已具体定义，包括零有效输出与删除前缀；字段编码由009唯一承接。')],
3:[old(3,'规范键的行边空白先后与内部LF','复用required/P2；按C01强调可跨相邻空行，不能用split/trim/join替代。原始值不按同一键规则改写。')],
4:[ok('主动/延迟加载、语言对清空、外层校验及错误回退','WP08§4、§5.2、§7可独立实现具名语言选择/查找，不要求沿用Translation对象组织。'),
   bounded('默认消息缓存、低层延迟加载重试次数、默认双文件保存顺序','保留默认对首次读取后缓存（失败也缓存空）、延迟文件名完成后清除、保存core先game事实。现行合同没有磁盘热更自动重试/同步双文件原子保证；WP04§6/WP08§6.4已允许I/O失败的部分状态。仅这些内部缓存/细写入顺序不足以新增公开产品能力或要求同名API，不宣称入口不存在。')],
5:[old(2,'实际默认哈希材料的core键排除、set/add及地图同桶','复用required/P2，明确add跳过输入不删除旧game同键；哈希只跳nil，空串与数组分支不同。'),
   bounded('低层数组同索引值排除','C01明确可作补充事实，不能仅凭数组辅助方法存在另升必修；保留事实，不强制未来API。','M01-LZ-DEFAULT-BUILD')],
6:[segment('alias_projection_only','延迟加载及默认差量的私有导航别名','没有独立能力分母；加载去向为输入4，默认构造去向为输入5及002。',existing=[(2,'默认哈希构造子范围')],owner=['M01-LZ-LOAD','M01-LZ-DEFAULT-BUILD'])],
7:[ok('分节前处理、普通重复、重复属性累加、实际身份校验','WP03§5与WP04§4.2已有承接；元数据实际编译走通用分节后严格schema转换，不能把旁边numbered辅助器的过滤套上去。'),
   segment('consumer_projection_only','合法有名但无属性的节仍进入记录默认处理','字段默认缺口由016唯一处理，专用必需字段仍由各验证者负责。',new=[(16,'作者缺席属性与默认记录')],owner='GR5-M01-016'),
   bounded('空节/编号包装的旧概括','更正为“空节名被包装器过滤”，不是“有合法节名但无属性的节被过滤”；后者可建默认记录，接016及专用必需校验015/022。numbered helper保留定义事实，静态实际主编译调用并不因此改用它；不以未发现调用断言功能不存在。')],
8:[old(1,'实际Height/Weight单行浮点接受门','复用required/P3及最近整数取整、基础省略默认/形态省略继承的最终边界；不扩张旧ID。'),
   new(10,'实际布尔作者字段词汇','YES/Y/NO/N等影响真正PBS输入的接受与有效值。'),
   bounded('十六进制辅助模式及更宽输入组合','x定义事实保留；当前247作者字段未指定x，不凭这一点说该辅助不存在。没有现行承诺要求未来公开任意schema求值API；不能单凭内部扩展可能性立必修。i/u/v/m/n明确约束仍由当前模式表承接。')],
9:[new(11,'当前内联作者枚举的词汇、别名与默认语义数值区别','对实际Gender、Item使用类型和Category给决定性接受/拒绝，避免要求复制哈希/数组结构。'),
   bounded('列表第一位置、哈希false值和常量模块反射等内部实现分支','通用内容引用/未知身份拒绝已有合同；没有独立发布对任意自定义枚举容器的兼容API。保留已读定义，不把每种内部承载结构另算功能。')],
10:[new(12,'定长多余尾项及出现的重复属性首次组求值','直接改变合法/边界作者输入结果，给Home和Moves而不只报内部循环。'),
    old(4,'六列实际字段顺序和Trainer尾项补首值','复用C01唯一主规则，BaseStats必需六正值及编辑缺项补0保持分开。'),
    ok('可选大写位、q整条值和返回语义','WP04§4.2已能实施；不强制未来返回数组或同名函数。')],
11:[ok('保持位置的内部空位、可选尾项及枚举/文本有效输出','WP03字段模式、WP04§4.2/§5.5及已审M01-CSV-QUOTE共同承接；不同合法同义枚举输出/可选末逗号/分组字节不必唯一。','M01-WRITE-GENERIC'),
    bounded('通用formatter的flatten、内部索引、首个别名及具体循环','这些组织方式没有独立产品契约；不把“不保字节”误作可以丢语义。真正语义变化分别落017/018/023，必须保留false的物品例外落030，不能由本行一律省略。')],
12:[new(28,'regional_dexes实际调用的物种词大写/特例归一','这是正面找到的作者消费者，不再把parseSpecies一并视作纯辅助细节。'),
    bounded('parseItem/parseMove及标Unused的Nature/Trainer等定义','定义与静态可用规则保留；现行一般注册查询已有统一身份合同，未承诺复现任意源辅助API。核心词法导航未见其它这些直接调用，不是功能不存在的证明；设施自身的宽容解析由其实际合同单独承接。')],
13:[new(27,'第一端方向门造成的混合端点接受不对称','作者编译结果不同；只记录接受/拒绝，不承诺混合记录可运行。'),
    bounded('两个地图同时缺失时只先提示第一端','当前缺图警告与非保证可用已足够；该警告的具体择一顺序不新增独立恢复/运行承诺，保留源事实。')],
14:[new(13,'类别×威力的拒绝/警告改类','属于作者数据结果，不是可忽略的校验内部组织。'),
    old(2,'编译名字/描述收集到默认哈希','默认消息规则只有002一个主身份；不再以Move消费者计另一能力。')],
15:[old(1,'尺寸浮点字段子范围','复用最终有界裁决，不复审。'),old(4,'BaseStats/具名EVs的作者列映射','复用最终有界裁决。'),
    new(25,'两种进化属性拼写的有序合并','与同名重复属性或编辑器复数视图不同。'),new(26,'终检生成反向前身的首次发现选择','对婴儿种/最低等级有具体消费。'),
    ok('已登记引用、缺参数、类型去重及分阶段终检','WP03§5.2、WP18、WP31各有承接；不把每次校验调用的结构当作另一必修。')],
16:[ok('标量/集合继承、等级招式和进化空表继承、三组持物整组门','WP18§3.1第4点（54行）、原稿55行已经逐项具体写出。旧“仅一般继承措辞”的评价撤回为后继更正。'),
    old(1,'形态尺寸输入及省略继承','复用001正确收窄后的形态规则。'),old(4,'形态BaseStats文本六列','复用004。'),
    new(26,'形态终检的反向前身优先子范围','与已有普通字段继承区分。'),
    old(2,'形态追加三个默认哈希域的集合更新','唯一主规则002；不另报每个域。')],
17:[new(14,'编号缺口与显式空节的编译终检','运行空表/缺表回退不消解作者输入阶段。'),
    new(28,'物种词专用归一','与一般内容查询不同，唯一主规则028。'),
    ok('顺序平铺、重复节/物种拒绝和运行缓存','WP62§5.1–5.2及WP03已明确；不得重复立项。')],
18:[old(4,'成员IV/EV列序/尾项/限额','复用C01作者输入主规则。'),old(6,'记录到NPC成员的缺省覆盖','仅消费投影，复用C01装载结果范围。'),
    new(29,'专用杂行识别与成员属性前置','不把通用坏行错误机械套到此消费者。'),
    ok('重复身份后项覆盖、重复招式去重及已述数值上限','当前WP03/18/19/24已有承接，编辑器数值上限不替代PBS验证。')],
19:[new(15,'全局0、玩家1与全局Home的必需检查','实际作者输入/失败前缀，不能仅由运行读取回退推出。'),
    new(16,'可省略全局字段的具名默认子表','仅仍缺的StartMoney等；不重报已有音频优先级与资源setter限制。'),
    old(2,'存储作者文本域默认集合','默认哈希主规则002。')],
20:[new(16,'编译地图Name缺/空时的MapInfos依赖','显式非空Name和缺省不是同一路；非所有地图缺失都有安全空名。'),
    new(21,'空图块集注册表不能首条回退','指向唯一021。'),new(22,'缺Autotile/Tile输入列表的建记录失败','指向唯一022。'),
    ok('地牢参数身份/版本与重复、合法数据字段','WP03§3.2、WP14§3.3已能实现；不把缺详细内部转换组织当新规则。')],
21:[ok('动画映射重建、重复后槽覆盖、有效条目写入门、零有效不写旧文件','WP74§15（394–403行）明确“不是与磁盘映射比较”，§16表亦有门；原稿同段及对应向量已有。旧歧义评价由这些当前实质条款消解，不新增发现。','M01-PBS-ANIMATION')],
22:[ok('有效连接锚点换算、删除地图跳过和可再读输出','WP11§3与WP04§5.5提供语义；方向优先/交换负号可输出等价锚点，未要求唯一文本表示。','M01-PBS-CONNECTION'),
    bounded('W/N/E/S优先、字符串保留及坐标交换的具体规范式','保留参考写出事实；不把等价语法规范化强制为未来格式或API。混合无效形状的接受另由027，不在此追加运行成功。')],
23:[new(17,'形态Generation0/Habitat None省略导致重读值改变','只把真实语义损失提升为候选；其余等价省略不照单立项。'),
    old(4,'BaseStats等输出列序','复用004。'),
    ok('源后缀分组、基本/形态分开与单数进化写出副作用','WP04§5.5已有具体承接；复数编辑读取不是本导出入口。')],
24:[ok('地区图鉴实际成员顺序、逐行分组与缎带通用写出','WP62§5.1定义行内/行间平铺，故同顺序不同族换行不是编号差异；WP04不要求重建旧字节。空槽/族换行等事实保留，不强制同一文本组织。','M01-WRITE-DEX-RIBBON'),
    segment('consumer_projection_only','按族工具生成的族内顺序','真正改变成员顺序的是工具填充而非这里换行，指向031，不重复算导出问题。',new=[(31,'工具生成有序族块')],owner='GR5-M01-031')],
25:[new(18,'负版本导出省略及身份碰撞','当前作者文本明确接受负值，不能以缺默认负数据关闭。'),
    ok('非正概率省略/恢复、空方式、相同等级短式','概率往返已有KL22/WP04§5.5；短式同一等级/空方式无额外条目是现有专用格式范围，不重报。')],
26:[old(4,'Trainer IV/EV输出顺序','唯一主规则004。'),
    segment('consumer_projection_only','省略字段对NPC装载结果的解释','006的最终覆盖规则用于判定等价输出，不另立输出必修。',existing=[(6,'普通/超级/Shadow缺省与最终覆盖')],owner='GR5-M01-006'),
    ok('有效训练家与设施反写、缺资料/宽容引用、严格输出失败及非原子写入','WP76§8.4、WP04§5.5和WP73A保存链已覆盖具体消费者；设施同一数据接口只计一次。','M01-PBS-FACILITY'),
    bounded('成员false/nil/空值/零版本和超级异色的等价省略','结合006的普通/超级/Shadow最终覆盖，普通false与省略不改变装载结果；超级真时省略普通真仍恢复同一结果，Shadow后段仍单独覆盖。只限定有效作者记录，不保证任意直接构造坏状态可无损。')],
27:[ok('来源后缀并集、全局/玩家记录与有效继承字符集输出','WP04§5.5允许按登记条目的后缀选路径，WP24§3.3完整给字符集回退，WP73A§6给保存链；可独立输出等效有效记录。','M01-WRITE-METADATA'),
    bounded('同文件内先全局后玩家、注释名、把继承值显式化','不保字节/原始省略形式，已解析继承值可被物化；未承诺未来手改父字段会继续影响被显式化的子字段。保留源事实，不要求同内部结构。')],
28:[ok('22项全量写出及非事务失败','WP04§5–6已有作者写出和部分状态合同。','M01-WRITE-GENERIC'),
    bounded('无输出路径也读取Tilesets资源、可选名称注释、原始映射标识','未给缺宿主资源仍必成功/任意内部生成记录往返保证；这些具体组织本身不产生新公开能力。墙型变换与原始/派生映射事实保留，并由输入51限定可输出等效配置的边界。')],
29:[new(16,'TownMap具名省略值/文件名缺省','实际作者字段子表；不凭全部默认样本已填字段当作省略规则。'),
    ok('Point位置/地点/详情/治疗/开关含义与消费门','WP63§3、WP62§5.3、WP03模式表以及WP75区域文本的八字段说明足以承接；没有必要照搬构造器组织。')],
30:[new(16,'Ability原名/描述/标记省略值','仅具名作者数据默认；不重新定义特性效果。'),
    ok('两个消息域与不分大小写标记查询','WP08域/回退及已完成标记消费者投影承接，不能把每个类的同义局部封装再算能力。')],
31:[new(13,'Category/Power交叉处理','编译结果由013唯一承接。'),new(11,'Category实际文本词汇','内联枚举词域由011承接。'),
    new(16,'剩余Move省略值','不重报WP03已给NONE类型/accuracy100/PP5，也不把旧damage弃用访问器立未来API。')],
32:[new(13,'成功PBS不能把Physical/Special+0原样登记','编译时的真正产品差异已由013独立确定。'),
    bounded('数据层physical/special的零威力守卫与战斗包装同名谓词差别','保留两种定义。当前可实现合同已分数据类别、实际战斗分类和显示属性；成功普通PBS的0威力被归Status，不由此新增一种正常伤害类别。没有承诺未来公开源辅助谓词的所有返回域；不声明该辅助无消费者或不存在。HM关联按Item机器字段已有承接。')],
33:[ok('Power/Priority/EffectChance为0时省略的等价作者输出','零值的来源默认与已有字段语义保持，省略不增加新的状态变化；输出样式非逐字节保证。剩余缺省值由016补齐而不另立一个getter能力。','M01-DATA-Move'),
    segment('consumer_projection_only','缺省值表依赖','本行只消费016的Move字段子范围。',new=[(16,'Move字段缺省')],owner='GR5-M01-016')],
34:[new(11,'使用方式枚举的合法字面与内部0区别','真实作者格式。'),new(16,'道具剩余可省略字段','仅缺的字段默认。'),
    segment('consumer_projection_only','不消耗false的反写保持','同一例外由030处理，不增独立能力。',new=[(30,'非重要Consumable=false')],owner='GR5-M01-030'),
    ok('编辑数值界与PBS无符号范围分开、机器关联在Item.Move','WP03/WP28/WP73A已有明确承接，未把编辑上限当输入模式。')],
35:[new(16,'份名缺省回退、确存空值和口袋/价格等剩余默认','已读实际消费者，不是单纯给私有字段补注释。'),
    ok('五文本域、售出半价、BP1和非重要缺省消耗','WP08、WP03§4.3、WP28§8/29已经明确，排除出新增缺口。'),
    ok('名称编辑默认与父保存门','WP73A§2/§3.3/§6已经说明属性缺值取默认、道具名默认???、Yes保存；不承诺编辑确认永久保留缺省raw空值。源中PortionName也用道具名属性已定点核对，份名查询与编辑工作表分别观察。')],
36:[new(19,'ShowQuantity有效真值及背包登记图标排除','以真实Bag/PC消费者落具体显示结果。'),
    ok('重要、可持、消费及具名不可丢失组合','WP28/38/50和已完成字段/标记交界已有可执行语义，不把此行所有方法都立项。')],
37:[new(30,'非重要物品Consumable=false保留例外','不能由通用false省略实现；唯一主规则030。'),
    ok('半价/BP1/使用方式0等价省略','已明确默认，加上011区分无使用0不是可接受枚举文本；输出这些值的省略可独立实现，不需统一保留所有原始位。')],
38:[old(1,'Height/Weight作者词法','复用001。'),old(4,'BaseStats列映射','复用004。'),
    new(25,'Evolutions/Evolution共存合并','旧“overwrite”纠正为旧表先赋、单数后追加；不是源反证未读。'),
    ok('基础/形态属性集、引用和已明确字段','WP18§3.1–3.2和WP04已承接，不能把全部schema再次转为新类架构要求。')],
39:[new(26,'实际反向前身的首次发现选择','会影响后代/最低等级，不能当纯遍历细节。'),
    new(31,'按族生成图鉴的族内次序','找到正面工具消费者，和反写换行分组不同。'),
    ok('DefaultForm、指标查询副作用、婴儿种/熏香、共享蛋招、最低等级公式','WP18/03/31/33/34已有具名规则；布尔归属查询可用关系集合独立实现，不要求复制便利方法集合。')],
40:[new(17,'形态0/None覆盖值反写丢失','只落具名语义变化，未把所有省略都列必修。'),old(4,'六项数值反写列序','复用004。'),
    ok('单数进化参数文本化、前驱过滤、复数编辑空视图','WP04§5.5明确；不是本次新发现。'),
    bounded('ID显示别名、空形态名、默认形态号、0消息/还原字段、正EV对等表示','按各字段已声明默认和有效输入，等价省略/表现形式不构成独立新增能力；尺寸输出的极端浮点/非有限数不扩张001。')],
41:[new(16,'Ribbon原名/描述/icon0等作者省略值','只补输入记录默认；已拥有列表与授予行为保持原合同。'),
    bounded('未在普通核心中独立消费的任意Flags及构造辅助','定义存在和大小写查询事实保留，不据缺默认使用断言特性不存在；未承诺任意扩展标记自带奖励效果。')],
42:[new(11,'类型Gender别名词域','与普通成员字段区别唯一落011。'),new(16,'类型Gender2/名称的省略子范围','其余已有默认排除。'),
    ok('BaseMoney30、SkillLevel随BaseMoney及技能阈值','WP51§2（21行）和原稿15行已有完整具体规则，旧“未说明随资金”评价撤回；不依名称统计支持。')],
43:[new(16,'类型原名和Gender的剩余缺省','只接016已有子表，不新增方法能力。'),
    ok('资金/技能、音频nil/空以及同资金技能省略','WP51§2和WP24§5.4已有规则；定点核对编辑SkillLevel使用可空数值默认nil，普通打开/保存仍按资金回落，不能虚构重置0缺陷。')],
44:[old(4,'普通训练家IV/EV字段形状、列序/尾项','复用004，原6列与编辑填0分开。'),new(11,'成员Gender仅两性别词域','类型Unknown不能直接套用。'),
    ok('类型/姓名/版本身份、物品/台词/物种等级及字段责任','WP03/18/24已定义，没有必要按源schema/subschema组织设计未来API。')],
45:[old(6,'普通NPC装载的缺省覆盖/顺序','采用完整当前键序、显式Ability覆盖、Shadow后段普通异色例外等C01更正；不重新取证相同反例。'),
    ok('RIVAL名字首个类型/字符串门及已给IV/EV','已有当前合同，未扩展到设施模板或外部预建NPC。')],
46:[old(4,'Trainer IV/EV输出列序','唯一主规则004。'),
    segment('consumer_projection_only','false/省略的NPC结果','由006已裁决覆盖规则承接，不扩张为任意内部原始位无损。',existing=[(6,'普通NPC覆盖后的等价值')],owner='GR5-M01-006'),
    ok('0版本、false/空字段、gender文本及超级异色下普通位省略','在有效作者记录/普通006装载结果的层次可由默认与覆写顺序确定等价结果；WP03默认省略和WP04非字节合同允许这种表示。不能声称任意手工内部坏状态无损，也不要求保存等价原始位。')],
47:[new(15,'全局必需记录/字段','编译规则唯一落015。'),new(16,'StartMoney/StorageCreator等尚缺默认','只限作者省略/回退。'),
    ok('初始PC每条加1、Home实际消费、音频优先级、初始money直拷与setter限额','WP27/24/61等已有入口分层；不能从setter范围反推初始化必夹限，也不重报该已有限定的合同。')],
48:[new(20,'地图名首次读取对共享模板的写入与改名后重读','正面找到电话消费者，不能以全部文本getter普遍纯或普遍变异概括。'),
    ok('普通本地化/基本地图名回退、flags和ID输出','现有WP08/11/63对应规则已能实现；旧指向trainer-card附表的continue-preview锚点纠正到WP65标题/载入正文，非另立问题。')],
49:[new(21,'空注册表对未知ID的失败','只为已存在“不报错”加必要范围；不要求完整任意参数API。'),
    ok('非空首条回退、整数身份及六开关默认','WP03§3.2/WP14§3.4已给正常路径；布尔词汇只由010承担。')],
50:[new(22,'作者输入缺整类映射列表的构建失败','与已建记录缺用途返回0分开。'),
    ok('四种墙型排布及数值转换','WP14§5.1完整表已逐单元核对，保留正确来源；不以缺构造前置抹掉该支持。')],
51:[ok('输出作者映射编号，与已知展开表相对应','WP14§5.1给普通384+t/自动48a及墙组合规则，WP04允许非字节等价输出；可独立导出有效等价配置，不需要源“origin marker”字段。'),
    bounded('只输出原始登记项、不另输出派生墙项的参考规范式','源事实明确保留；避免重复添加概率/图块语义是当前数据意义的一部分，但保持原有组合拼写和内部起源标志不是另一个产品能力。没有无条件保证随意改导出文本后仍保留此前隐含关系。')],
52:[ok('组合字段反写、0版本省略及没有额外上界','WP14§3.3与WP03类型约束足以构建等效字段。作者版本是非负模式，0省略回0。'),
    bounded('直接内部记录的负版本导出省略','事实保留；缺失参数查询返回未登记默认对象，不能据此把任意内部负版本提升成已发布作者输入。没有规定未来复现源构造器API；不以没有样本断言不存在。')],
53:[new(23,'含逗号姓名的专用header输出','新候选只落已可建立的作者身份再读变化。'),
    ok('Default与普通0版本的正常写法','WP03/63身份规则和非负版本默认可实施，字面负版本并非该PBS的U模式输入，不另扩为任意负内部记录兼容要求。')],
54:[new(24,'14个既有体型身份/次序/参考图标关联','已有真实作者枚举与搜索消费，不能仅凭字段名实现。构造任意新增固定记录的API不在此要求。')],
55:[new(24,'10个既有体色身份/次序','同一固定物种目录主规则的另一子表，不另算一个功能缺口。')],
56:[new(24,'10个既有Habitat作者枚举身份','即使未定位独立普通玩法，作者枚举/编辑已是正面消费者；不把它误当Area地理计算或声称功能不存在。')],
57:[old(4,'主能力PBS位置与非PBS命中/闪避区别','复用C01，公式/个性/Hidden Power自身的已声明顺序不是错误。'),
    bounded('内部type标签、PBS−1默认和各遍历便利器','保存已读定义和主/战斗子集概念即可；无须未来提供同样枚举函数/容器。')],
58:[bounded('候选数据集的完整差异事实与组合政策','WP02§6.2/§7已明确备份不自动扫描、不等于世代兼容或自动保存迁移；全部逐记录比较结论保留。不能从同一SLOWBRO形态键变义推出一个已承诺但缺失的自动迁移功能，也不把候选存在升级为支持。','M01-PBS-GENERATION-PROFILES')],
59:[old(5,'已声明容量/自动扫描的负盒号局部例外','复用required/P3；只修已存在过宽表述，不强制未来新增所有负参数接口。保留−2原址寻址与容量6的区分，按C01更正WP25§7–8锚点为167–187行。')],
}
assert set(D)==set(range(60))

ROWS=[]
OVERRIDES=[]
for i,r in enumerate(INPUT):
    parts=D[i]
    existing=list(dict.fromkeys(f['id'] for p in parts for f in p['existing_findings']))
    newids=list(dict.fromkeys(f['id'] for p in parts for f in p['new_findings']))
    refs=[]
    for identity in newids:
        assert identity in by_new,identity
        refs.extend(by_new[identity]['spec_anchors'])
    for p in parts:
        for c in p['existing_findings']:
            cf=next(x for x in CANON if x['id']==c['id'])
            refs.extend(cf['spec_anchors'])
    # Existing-contract-only entries use the actual current anchors rather than
    # a claim of sufficiency from reading extent or from a section heading.
    precise={
      4:[spec('08',34,63,'语言选择、立即/延迟加载和失败回退足以承接公开行为；没有热更新自动重试保证。'),spec('04',179,203,'部分状态与本地化交界已明确。')],
      7:[spec('03',103,117,'非空身份字符模式与类型规则已有定义；实际metadata走严格schema，不套numbered helper。'),spec('04',62,92,'预处理、普通/重复属性和登记规则明确。')],
      11:[spec('04',64,80,'位置语义、可选位和q保持。'),spec('04',153,177,'有效写出/不逐字节保证与具名语义变化分开。')],
      16:[spec('18',49,55,'第4点已逐项给标量/集合、空Moves/Evolution、三组持物整体继承。'),spec('specs/creature-rpg/wp18-creature-identity-species-ownership.md',49,56,'原稿55行同样明确。')],
      21:[spec('74',394,421,'写入门不是磁盘比较：任一有效条目就写，零有效不写/旧文件保持；字段前导空白、重复后槽覆盖和保存表均明确。','§15–16')],
      22:[spec('11',25,42,'同一锚点/偏移可用等价表示，运行转换已明确。'),spec('04',160,166,'专用连接输出跳缺地图，无字节规范式保证。')],
      24:[spec('62',94,102,'物种词平铺顺序决定编号；族换行不改此顺序。'),spec('04',160,166,'通用/专用输出不要求原字节。')],
      26:[spec('76',227,234,'设施专用写出、输入缺失/未知引用及输出严格读取的已有边界。'),spec('73A',130,151,'保存、注册、档案和PBS层次明确。')],
      27:[spec('24',71,79,'七字符集回退链具体，导出物化有效值有明确定义基础。'),spec('04',153,162,'来源后缀分组，不重建所有旧输入。')],
      28:[spec('04',153,203,'有效输出路径和非原子/宿主边界已有，未承诺无路径时可忽略所有依赖。')],
      29:[spec('63',34,61,'Point三个消费者、可见/治疗、位置都已给行为规则。'),spec('75',30,30,'明确列出Point八个字段。'),spec('75',310,323,'区域地图作者文本的输入/输出边界已有。')],
      32:[spec('43',13,38,'数据属性/实际计算输入分开；不要求同名辅助谓词一一对应。')],
      33:[spec('04',153,166,'默认值等价输出与不保字节合同。')],
      35:[spec('28',309,323,'默认消耗、半售价、BP1已有。'),spec('73A',33,52,'属性初始化及道具名文本默认???已明确，父保存门另定。')],
      37:[spec('28',309,323,'现有默认给等价省略依据；false例外独立030。')],
      39:[spec('31',108,116,'最低等级和相关消费者已有。'),spec('34',52,67,'前身回溯/熏香已给。')],
      40:[spec('04',168,178,'指标路径及进化编辑/正式写出的具体正确合同。')],
      42:[spec('51',19,25,'BaseMoney默认30、SkillLevel缺省取BaseMoney明确。')],
      43:[spec('51',19,25,'资金/技能默认已有。'),spec('24',167,192,'各音频nil/空/多类型后项等优先规则已明确。')],
      46:[spec('04',153,166,'输出规范化没有字节保证；普通装载覆写按006。')],
      48:[spec('65',43,47,'正确continue-preview锚点是标题/载入正文，而非trainer-card附表。')],
      50:[spec('14',185,227,'四种墙型与自动图块邻接完整具体表已有；不重报。')],
      51:[spec('14',185,208,'作者编号及墙展开足以输出等效有效配置。'),spec('04',153,166,'不保来源文本组织/字节。')],
      52:[spec('14',44,72,'参数组合、默认与字段含义已明确。'),spec('03',54,55,'缺失参数返回未登记默认对象。')],
      58:[spec('02',228,256,'候选材料及组合未承诺表明确，完整字面差异不自动成为新支持/迁移要求。')],
      59:[spec('25',44,65,'容量表/寻空位按005修正范围。'),spec('25',167,187,'C01已更正的不变量/失败锚点。')],
    }
    refs.extend(precise.get(i,[]))
    for a in r['spec_anchors']:
        # Keep original anchors explicitly as provenance, not as unverified
        # replacement of corrected detailed anchors above.
        pass
    if not refs:refs=copy.deepcopy(r['spec_anchors'])
    # Deduplicate only exact audit anchors; does not collapse semantic rows.
    uniq=[]
    for a in refs:
        if a not in uniq:uniq.append(a)
    route_set={p['route'] for p in parts}
    final='partial_linked_to_findings' if (existing or newids) else ('existing_contract_sufficient' if route_set=={'existing_contract_sufficient'} else 'source_fact_retained_no_required_revision')
    row=dict(record_index=i,capability_id=r['capability_id'],input_status=r['status'],
      input_anchor=dict(path='followup-partial-triage-input.json',sha256=BASE['input_sha256'],json_pointer='/records/'+str(i)),
      main_review_record_anchor=oldref(i),original_source_anchors=copy.deepcopy(r['source_anchors']),
      original_spec_anchors=copy.deepcopy(r['spec_anchors']),effective_spec_anchors=uniq,
      disposition_status=final,reading_complete=True,finite_disposition_complete=True,
      existing_finding_ids=existing,new_finding_ids=newids,subscope_dispositions=parts,
      status_reason='；'.join(p['reason'] for p in parts),
      current_mapping_semantics='原source-to-spec结果不改；本后继限定读完后的去向。'+('partial保留并明确连接裁决/候选。' if existing or newids else '不因读完自动升supported；已有承接或定义/政策边界逐子项说明。'),
      capability_count_policy='同一主规则的别名/消费者投影不另计能力或发现。',
      execution_status='STATIC_ONLY; reference/model/author tools not executed',
      pending_work_in_this_finite_review=[],independent_counterevidence_needed_only_for=newids)
    ROWS.append(row)
    OVERRIDES.append(dict(capability_id=r['capability_id'],main_review_record_anchor=oldref(i),
      old_value=dict(status=r['status'],comparison=r.get('comparison'),current_contract_comparison=r.get('current_contract_comparison'),spec_anchors=r['spec_anchors']),
      successor_value=dict(status='partial' if existing or newids or 'definition_or_policy_boundary' in route_set else 'supported',
                           disposition_status=final,comparison=row['status_reason'],effective_spec_anchors=uniq,
                           existing_finding_ids=existing,new_finding_ids=newids,reading_complete=True),
      reason='有限后继逐子范围裁定；原文件保留，不无痕回写。',
      meaning_changes_explicit=True))

CORRECTIONS=[
 dict(record_index=7,old='Empty section filtered; numbered wrapper restrictions treated as current metadata pipeline.',
      new='过滤的是空节名，不是所有空内容节；合法有名无属性节仍交通用处理。metadata实际消费者使用pbEachFileSection后严格schema，不使用numbered wrapper。',
      source_anchors=[source('parse',95,151,'包装门测试名称，不测试内容长度。'),source('compile',1079,1099,'实际metadata分节调用和严格身份求值。')]),
 dict(record_index=16,old=INPUT[16]['current_contract_comparison'],
      new='WP18正式54行/原稿55行已经明确空Moves/Evolution继承与三组野生持物整体门；该子范围不再声称一般措辞不足。',
      spec_anchors=[spec('18',49,55,'明确继承条款。'),spec('specs/creature-rpg/wp18-creature-identity-species-ownership.md',49,56,'原稿同义具体条款。')]),
 dict(record_index=21,old=INPUT[21]['current_contract_comparison'],
      new='WP74§15及§16已明确任一有效映射就写/零有效不写旧文件/非磁盘比较；旧partial歧义被当前合同消解。',
      spec_anchors=[spec('74',394,421,'完整决定性合同。')]),
 dict(record_index=38,old=INPUT[38]['comparison'],
      new='Evolutions先赋旧表，Evolution再在已有表上累加；不是单数覆写复数，已用025的跨拼写有序合并表达。',
      source_anchors=[source('species',102,110,'两键顺序。'),source('compile',30,52,'赋表后追加。')]),
 dict(record_index=42,old=INPUT[42]['current_contract_comparison'],
      new='BaseMoney默认30、SkillLevel缺省取BaseMoney在WP51§2已有明确合同；Gender别名/剩余省略字段分别另处置。',
      spec_anchors=[spec('51',19,25,'字段默认及档位明确。')]),
 dict(record_index=48,old=INPUT[48]['spec_anchors'][-1],
      new=spec('65',43,47,'继续预览应指标题/载入正文，不是trainer-card附表。'),reason='旧映射具体路径错误；只在后继更正，不修改旧证据。'),
 dict(record_index=59,old='Old M01 finding005 anchored WP25§7–8 to138–153.',new='采用C01最终167–187行更正，不再复审005。',canonical_anchor=canon(5,'容量/扫描局部边界及锚点更正')),
]

if __name__=='__main__':
    write('followup-partial-dispositions.json',dict(schema_version='gr5.finite_partial_disposition.v1',module='M01',complete=False,
       input=dict(path='followup-partial-triage-input.json',sha256=BASE['input_sha256'],record_count=60),
       canonical_decisions=dict(path=CANON_PATH,sha256=BASE['canonical_sha256'],scope='001–006 required /007 optional final bounded reuse'),
       boundary='Only the finite60 prior non-supported records. No old mapping/reading proof mutation, no repeated full PBS/corpus review and no reference/model/tool execution.',
       records=ROWS))
    write('followup-partial-mapping-overrides.json',dict(schema_version='gr5.review.v1',module='M01',
       original_modified=False,overrides=OVERRIDES,explicit_source_or_anchor_corrections=CORRECTIONS))
    write('followup-partial-new-findings-draft.json',dict(schema_version='gr5.review.v1',module='M01',complete=False,findings=NEW))
    print('Finite dispositions materialized:',len(ROWS),'new candidate drafts:',len(NEW))
