# B01 作者候选逐 ID 回应

状态：**待父任务指派独立 Ultra 复审**。这是PRE0+B01-A交付；229规范必修仍全部开放，未整合、未关闭、未批准、未启动下游。只改6份白名单正文/测试；原specs与历史review留原字节。

原始14对象与全部字段在original-findings.json，源身份由93e10报告提交固定。无损叶值读取2538出现→573唯一值，完整对象及字段引用保留；不是只阅读摘要。细分首判/二审/扩展按原对象优先级继承。

## GIR-FD82-001

B01-A只有WP01范围/导航的有证据登记提案，不改写未授权公共入口。

- 条款：仅本目录后继登记提案/勘误
- 静态向量：文档去向与状态对照，见正文说明
- 前提：在相同审查基线读取scope和README，区分作者全集交付、旧局部批准和本轮229项开放必修。
- 唯一静态结果：scope仍称仅批次1；README已列1–15，且使用不存在的ui目录。新执行冻结只确认全集作者材料与当前开放review，不能冒充全集批准。
- 反向对照：历史批次1的PASS_SCOPED保留其对象与时点；运行观察及真实Demo链均为0。
- 尚未触及：scope/README和七份正文审计链接均未改；按B01-G及B18/B21授权分别处理，B21为唯一汇总责任。
- 公共登记建议：后续公共入口把当前状态写为全集作者交付、最终全局review已完成且233中229项开放必修、整改候选待复审；ui改实际user-interface；具名七正文审计路径三级回退。不得声称统一通过。

证据：
- [deliverables/final-specification-set/scope-statement.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e1e01bb18d824931e54f182dd61af5a9f908ba85/deliverables/final-specification-set/scope-statement.md#L1)，1–41。
- [deliverables/final-specification-set/README.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e1e01bb18d824931e54f182dd61af5a9f908ba85/deliverables/final-specification-set/README.md#L1)，1–50。

## GIR-FD82-A001

改WP04分词合同及KL10，保存合并耗尽与存在独立尾字段的差异；KL07/08/09原字节不改。

- 条款：deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md §4.2
- 静态向量：KL10、KL07、KL08、KL09
- 前提：合法道具Flags列表；每端一个U+005C加一个U+0022；无空白，首例无第三字段。
- 唯一静态结果：完整输入为\"Alpha,Beta\"；合并耗尽后唯一标志仍保留两端标记。
- 反向对照：仅追加,Other后，首标志为Alpha,Beta，第二标志Other；普通PokeBall原样且精确匹配成功。
- 尚未触及：原specs/kernel/wp04-pbs-lifecycle.md §4.2/§9.2仍错，按现行read-only规则未改；已列最小范围修订请求。
- 公共登记建议：追溯新增末次合并耗尽反例；原GR-001的单值/末值与正确非末值对照保留，历史批准不改。

证据：
- [Data/Scripts/021_Compiler/001_Compiler.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/001_Compiler.rb#L255)，255–293,690–735。
- [Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb#L4)，4–68。
- [Data/Scripts/010_Data/002_PBS data/006_Item.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/010_Data/002_PBS%20data/006_Item.rb#L25)，25–44。

## GIR-FD82-A002

改WP04新鲜度为各文件先截整秒、各集合取最大值后>=比较，补隔离前提。

- 条款：deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md §3.1
- 静态向量：KL19、KL20、KL21
- 前提：调试、PBS目录存在且有可读合法被发现文本；必选数据全存在可读；无导图/强制/按键等其他触发，非负时间戳。
- 唯一静态结果：PBS1000.1与数据1000.9均为1000，新鲜度触发；不按高精度判否。
- 反向对照：相等仍触发；PBS999.9与数据最大1000.1截为999/1000，不由新鲜度触发；不逐类配对。
- 尚未触及：原specs/kernel/wp04-pbs-lifecycle.md §3.1仍为高精度式概述，未在只读范围中改写。
- 公共登记建议：追溯写明时间精度、集合比较与其他触发独立；非调试提前返回及缺文件触发保留。

证据：
- [Data/Scripts/021_Compiler/001_Compiler.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/001_Compiler.rb#L1040)，1040–1096。

## GIR-FD82-A003

WP05发现校验和Scripts归一化明确缺失/nil/false与空列表；正常省略Scripts无自动候选仍合法。

- 条款：deliverables/final-specification-set/generic-kernel/wp05-events-extensions-plugins.md §5.1
- 静态向量：EP06、EP07、EP18
- 前提：Name、依赖等其他前提合法；正常meta解析与防御边界故障输入分别列。
- 唯一静态结果：解析后nil/false/缺失在防御边界报缺Scripts；空列表不报该错误。
- 反向对照：省略Scripts且无自动候选自然得到空列表，仍是合法插件；整个产物无插件条目不同。
- 尚未触及：原WP05该假值表述本已正确，未为消除finding改写正确规则；真实插件组合U09不提升。
- 公共登记建议：核对最终WP05和EP07/18，不把nil/false与长度0统一。

证据：
- [Data/Scripts/001_Technical/005_PluginManager.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/001_Technical/005_PluginManager.rb#L400)，400–464,527–549。

## GIR-FD82-A004

WP05补完整路径.rb子串、显式先行/自动追加、精确路径首次去重及编译/消费同序。

- 条款：deliverables/final-specification-set/generic-kernel/wp05-events-extensions-plugins.md §5.1/§6.2/§6.3
- 静态向量：EP19、EP20、EP21
- 前提：自动发现以完整路径为输入，区分大小写；顺序向量指定合法单插件、全部文件可读且内容有效，假定编译消费成功。
- 唯一静态结果：old.rb.bak及目录名Marked.rb中的readme.txt入选；显式b.rb,a.rb最终及消费均b,a,c。
- 反向对照：Plain/readme.txt和Plain/a.RB不入选；无显式列表自动顺序a,b,c；重复显式b保留首次。
- 尚未触及：原specs/kernel/wp05-events-extensions-plugins.md §5.1/§9.2仍把自动候选概述为.rb文件，未改；不执行候选脚本证明入选。
- 公共登记建议：路径筛选与脚本内部顺序区别于插件依赖排序；不承诺路径别名去重，不把候选路径误当成功执行。

证据：
- [Data/Scripts/001_Technical/005_PluginManager.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/001_Technical/005_PluginManager.rb#L400)，400–464,576–643。
- [Data/Scripts/001_Technical/002_Files/001_FileTests.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/001_Technical/002_Files/001_FileTests.rb#L1)，1–35。

## GIR-FD82-A006

WP02把调试入口限定为翻译提取目标选择；补当前玩家语言不变的取消对照。

- 条款：deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md §6.3
- 静态向量：KC05、KC06
- 前提：当前语言/已加载消息A，作者候选A/B；提取选B后在文本类别取消。
- 唯一静态结果：取消后玩家语言及消息仍A；选择只决定输出目标，不调用当前消息重新载入。
- 反向对照：真正载入菜单语言项选择B会更新玩家语言并载入B；原启动无存档多语言入口保留。
- 尚未触及：WP08最终/原始对应句、原WP02 §6.3、设置附表§7.3的旧分类仍需B02/公共登记处理；不推断全局绝无其他切换入口。
- 公共登记建议：更新设置使用点追溯中该入口的角色为提取目标选择；与WP08共享前提，待B02经整合核验后消费。

证据：
- [Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/020_Debug/003_Debug%20menus/002_Debug_MenuCommands.rb#L1423)，1423–1455。
- [Data/Scripts/003_Game processing/001_StartGame.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/003_Game%20processing/001_StartGame.rb#L1)，1–40。
- [Data/Scripts/016_UI/013_UI_Load.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/016_UI/013_UI_Load.rb#L330)，330–345。

## GIR-FD82-A009

EP08拆有/无已登记Link条件；WP05依赖错误正文补同一消息前提。

- 条款：deliverables/final-specification-set/generic-kernel/wp05-events-extensions-plugins.md §5.2
- 静态向量：EP08、EP13、EP14
- 前提：A最低要求B2.0；B1.0已合法注册；其他调用成功，分别缺Link或有非空合法已登记Link。
- 唯一静态结果：无Link仍报已装版本不足并终止，不显示或补造更新链接。
- 反向对照：有Link追加该链接，仍终止；缺键不是显式空键错误。
- 尚未触及：原specs/kernel/wp05-events-extensions-plugins.md §9.2场景仍无Link前提，未改；缺Link允许规则保持。
- 公共登记建议：源错误消息的条件后缀入追溯，原场景最小同步列入范围修订请求。

证据：
- [Data/Scripts/001_Technical/005_PluginManager.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/001_Technical/005_PluginManager.rb#L168)，168–185。

## GIR-FD82-A020

WP03登记Nature固定目录顺序/修正的必要依赖和LONELY/BRAVE两身份对照；未把完整领域能力算法移进通用档案。

- 条款：deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md §6
- 静态向量：KR13
- 前提：固定25项目录未扩展，未显式指定性格；个人标识取余1/2，数值对照关闭IV/EV禁用、无计算用覆盖。
- 唯一静态结果：1=LONELY攻击+10防御−10；2=BRAVE攻击+10速度−10。Bulbasaur50级IV31EV0应分别为攻击/防御/速度75/62/65与75/69/58（本条领域结果只作B05/B07交接向量）。
- 反向对照：5个中性身份无修正；显式/薄荷覆盖的优先关系仍属WP19/28合同，不新增道具使用门缺陷。
- 尚未触及：完整25身份映射、WP19正文/测试及WP28消费者尚由B05/B07交付；本批只完成WP03依赖贡献，全局finding开放。
- 公共登记建议：固定映射及计算用性格输入链须进入WP19追溯；附B05/B07必要上下游依赖，无新增根因。

证据：
- [Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/010_Data/001_Hardcoded%20data/009_Nature.rb#L1)，1–173。
- [Data/Scripts/014_Pokemon/001_Pokemon.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/014_Pokemon/001_Pokemon.rb#L490)，490–506,1088–1117。
- [PBS/pokemon.txt](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/PBS/pokemon.txt#L1)，1–22。

## GIR-FD82-C004

WP04反写补0概率非往返，KL22区分登记/档案/PBS/再编译及0默认类型对照。

- 条款：deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md §5.5
- 静态向量：KL22
- 前提：合法地图版本且方式有合法非空槽，编辑/保存/写出/再编译成功；不含当前地图缓存。
- 唯一静态结果：Land0先留运行登记/档案0，PBS省略概率，成功再编译取默认21并保存。
- 反向对照：OldRod默认0省略后仍0；Land70显式写出/再编译仍70；不补事务回滚。
- 尚未触及：完整编辑器三层与遭遇运行合同由B19/B08；原规格同处同步尚未授权。
- 公共登记建议：将0默认恢复与C005当前地图缓存问题分开；B08/B19签收四阶段，不单独关闭。

证据：
- [Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/020_Debug/001_Editor%20screens/001_EditorScreens.rb#L115)，115–120,280–287。
- [Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb#L403)，403–448。
- [Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb#L664)，664–765。
- [Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/010_Data/001_Hardcoded%20data/013_EncounterType.rb#L1)，1–178。

## GIR-FD82-C016

WP04补保存时非零形态决定路径、相等只省略节、不同后缀与惰性查询对照。

- 条款：deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md §5.5
- 静态向量：KL23、KL24、KL25、KL26、KR05
- 前提：保存/反写调用成功；使用保存时实际登记集合，不假设初始全0集合始终不变；五组相等对保存时基本记录比较。
- 唯一静态结果：全基本形态从A改B：档案B，PBS仍A；重载档案B，旧PBS再编译恢复A。
- 反向对照：同后缀非零记录选路径且可省略该形态节；异后缀只选该路径；保存前查询可新建空后缀非零记录改变路径集合。
- 尚未触及：指标编辑操作/预览、WP15/16领域副作用及原规格同步由后续责任批次；不称全0是正常UI必然可达。
- 公共登记建议：B19必须按保存时记录集验证，不以非零相等跳过节解释为不写文件；保留重载与再编译反向对照。

证据：
- [Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb#L291)，291–351。
- [Data/Scripts/010_Data/002_PBS data/010_SpeciesMetrics.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/010_Data/002_PBS%20data/010_SpeciesMetrics.rb#L16)，16–88。
- [Data/Scripts/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/020_Debug/001_Editor%20screens/004_EditorScreens_SpritePositioning.rb#L70)，70–122。
- [Data/Scripts/010_Data/001_GameData.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/010_Data/001_GameData.rb#L130)，130–151。
- [Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb#L4)，4–68,543–565。

## GIR-FD82-C022

WP04按真实单数写出和复数编辑读取分别登记参数转换/No无该副作用/Yes清空与暂留旧反向关系。

- 条款：deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md §5.5
- 静态向量：KL27、KL28、KL29
- 前提：合法A→B数值进化16，父属性操作不修改进化字段；No向量期间没有其他PBS写出，Yes向量各步骤成功。
- 唯一静态结果：父No保留关系和数值参数；父Yes用默认空列表清空A前向/前驱，B旧反向关系仍可能留在登记及先保存档案。
- 反向对照：正式单数Evolution写出可把真实前向参数转文本，但此前档案仍数值；全量PBS再编译才重建关系。
- 尚未触及：WP73-A最终§2等仍有旧“打开No可转文本”错误，原规格/旧审查/旧AX不能改；B19及B21需后继修正，不合理化为参考异常。
- 公共登记建议：撤回该父No反例的当前使用；保留池/地图尺寸真正共享副作用。旧A-R04批准事实不改，新记录引用纠正。

证据：
- [Data/Scripts/010_Data/002_PBS data/008_Species.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/010_Data/002_PBS%20data/008_Species.rb#L103)，103–108,135–150,299–327,385–445。
- [Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/020_Debug/001_Editor%20screens/001_EditorScreens.rb#L935)，935–987。
- [Data/Scripts/020_Debug/002_Editor_DataTypes.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/020_Debug/002_Editor_DataTypes.rb#L1550)，1550–1560。
- [Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb#L174)，174–223。
- [Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb#L292)，292–365。

## GIR-FD82-C080

WP04新增遭遇专用解析例外：整数前缀、0/负值、重方式清槽保留概率、严格槽门及负权重入口差异。

- 条款：deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md §4.4
- 静态向量：KL30、KL31、KL32
- 前提：合法引用/合法地图上下文按向量分别隔离；重复方式为单节，重复地图×版本是独立反向情形。
- 唯一静态结果：同节Land70+PIDGEY后Land无概率+RATTATA，最终概率70只余RATTATA；不恢复默认21。
- 反向对照：第二次显式21覆盖旧概率；junk概率0而槽权重/等级0拒绝；负权重走未知方式错误，重复节仍拒绝。
- 尚未触及：完整WP36正文/测试与原规格专用格式同步由B08；本批只描述PBS入口，运行概率行为不在本次范围。
- 公共登记建议：按root最终有效限定保留70，禁止混用早期“恢复21”描述；数据约束按字段而非统一非负数规则。

证据：
- [Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb#L664)，664–765。
- [Data/Scripts/021_Compiler/001_Compiler.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/021_Compiler/001_Compiler.rb#L384)，384–403,690–735。

## WP80-B02-R01

从WP02§7移除41文件计数，保留直接世代依赖；新后继勘误纠正历史“已全移出”检查断言。

- 条款：deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md §7
- 静态向量：文档去向与状态对照，见正文说明
- 前提：审查同一固定旧v2回应与WP02；行为性配置数量和默认值与源文件命中数量分开。
- 唯一静态结果：旧v2回应称已移出，旧WP02§7却仍有41文件；候选§7只表述直接世代依赖仍在。
- 反向对照：118/88/30/47及41布尔型等档案清单数量不删除；直接依赖不受派生覆盖的有效规则保留。
- 尚未触及：原WP02用于审计的文件统计保留；历史回应原件不改，后继勘误待独立复审。
- 公共登记建议：当前修订检查改为新候选字节的残留检查；历史v2全面移除断言不能继续作为当前验收证据。

证据：
- [review/wp80-delivery-2026-10-03/batch-02/revision-v2/revision-response.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e1e01bb18d824931e54f182dd61af5a9f908ba85/review/wp80-delivery-2026-10-03/batch-02/revision-v2/revision-response.md#L1)，1–30。
- [deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e1e01bb18d824931e54f182dd61af5a9f908ba85/deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md#L1)，1–277。
- [Data/Scripts/001_Settings.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/001_Settings.rb#L8)，8–17。

## WP80-B02-R02

新增历史去向后继勘误，两条精确索引取代当前使用的错误声明；原历史表不改。

- 条款：仅本目录后继登记提案/勘误
- 静态向量：文档去向与状态对照，见正文说明
- 前提：打开旧处置表14/81和audit T-WP02-01/02，再打开原主文§4.3、附表§7.2/7.4；身份与元信息正确记录不动。
- 唯一静态结果：16开关路径是原主文§4.3及附表§7的索引，非全部复制迁移；41/139/0在原附表§7.2经audit T-WP02-02索引，不在净化§3。
- 反向对照：WP02/WP03被审与当前完整身份分列、三项元信息及WP04 GR-001审查依据已正确，不为修这两行重开它们。
- 尚未触及：后继勘误是作者待审记录，不撤销历史批准或直接宣告残留关闭。
- 公共登记建议：当前处置去向使用historical-errata.md两条后继记录；历史表旧14/81保留原字节。

证据：
- [review/wp80-delivery-2026-10-03/batch-02/revision-v2/clause-disposition.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e1e01bb18d824931e54f182dd61af5a9f908ba85/review/wp80-delivery-2026-10-03/batch-02/revision-v2/clause-disposition.md#L1)，1–21,71–87。
- [audit/source-traceability.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e1e01bb18d824931e54f182dd61af5a9f908ba85/audit/source-traceability.md#L47)，47–83。
- [specs/kernel/wp02-rule-configuration-and-data-variants.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e1e01bb18d824931e54f182dd61af5a9f908ba85/specs/kernel/wp02-rule-configuration-and-data-variants.md#L227)，227–247。
- [specs/kernel/wp02-settings-inventory-appendix.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e1e01bb18d824931e54f182dd61af5a9f908ba85/specs/kernel/wp02-settings-inventory-appendix.md#L174)，174–206。
- [Data/Scripts/001_Settings.rb](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/001_Settings.rb#L517)，517–524。
