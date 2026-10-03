# C-01-S2：WP73-A/B 剩余来源补审

**结论：NEEDS_REVISION_SCOPED。** WP72、WP73-A、WP73-B 的14份主源码累计已全文读完，已列本包实质属性、选择器、工具和编辑行为的承接处置；没有剩余的整族主来源未读。本批仍有8项新P2待修，不签发整包/全局通过。

## 基线、独立性与范围

项目输入固定 `e1e01bb18d824931e54f182dd61af5a9f908ba85`；参考独立只读克隆固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。沿用 `review/2026-10-03-fd82a639/C`，开工提交 `02ad5b24f8adea87cff94447a807912d2660391c`。旧 C-01、C-01-S1 报告和首判原样保留；未读 A/B/D 本轮发现；这是同一 C 主审的延续，不冒充新第二审查者。

指标场景独立首判于 **2026-10-03 13:40:05 UTC** 写入 [metrics-first-judgment.md](metrics-first-judgment.md)，在任何外部审查结论输入之前形成。父任务只给场景与定位，本报告按来源推导。

本批补齐4份源文件原余段 **2,377行**：Editor_Utilities全410行、Editor_DataTypes余1,290行、Editor_Listers余538行、EditorScreens余139行。结合 C-01/C-01-S1，14份主文件累计 **11,098/11,098行**（WP72七份5,759行＋内容编辑四份4,087行＋世界编辑三份1,252行）。这些数字仅是防漏辅助；equivalence.tsv按35个行为族记录实际判断，并将4份内容/工具文件的100个顶层声明全部关联到具名行为或有理由的边界。

原稿与净化稿全文阅读复用 C-01；本批又定点回读受影响段，CE20条/WE22条全量复读。四份关联表的处理：WP73-A/B现行revision-v4 entry表本批全文逐项比对；WP72 revision-v3 entry表及revision-v2 120效果目录复用C-01全文与S1后续核验，不重复读取不相关项、不重算为本批新增覆盖。

## 新发现

### RUN-C-016 · P2 · 指标反写路径只由非零形态驱动，基础记录保存不保证更新PBS

类型：conditional_output_path_omission；状态OPEN；置信度HIGH；范围：WP73-B / WP04。

原稿、净化稿和WE-M19/M20把指标保存概括为数据保存＋PBS反写，未给出决定是否真正打开PBS文件的形态/后缀条件。

保存链先写species_metrics.dat；反写收集路径时跳过所有0形态，只按其余记录后缀产生文件路径。若保存时全部记录为0形态，则没有PBS路径被打开。若有非零形态，只写这些形态覆盖的后缀；随后同路径基础记录可输出，而五组指标全等于基础值的非零记录自身被省略。

前提：保存链执行时，登记数据仅含基础形态记录；把一个基础指标A改成B并确认保存；该后缀PBS原有A且所有实际文件操作成功；没有在保存前浏览/查询非零形态而惰性建立记录。

最小对照：数据档案写B，但PBS仍A；从数据档案重载读B，以旧PBS成功重编译又得到A。加入同后缀非零记录后路径才产生；即使该非零记录因等值被省略，路径仍会打开。

影响：交付无法决定哪些文件实际更新以及档案/PBS是否一致；后续实现可能无条件写全量指标而与参考不等价。

最低更正：补保存时记录集合→后缀路径→记录省略→重载/重编译的状态表，含仅基础形态、同后缀非零、不同后缀和等值非零四例；说明预览/自动定位可先惰性创建非零记录。保留来源异常，不修参考。

复核条件：逐阶段区分运行数据、数据档案、PBS文件及已布局精灵；基于保存时集合而非进入前文件内容判定路径；维持metrics-first-judgment.md的独立来源推导；不执行参考。

项目定位：`specs/demo/wp73-b-world-editors.md:35;114;128;191`；`deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md:17;96;110`；`review/wp73b-delivery-2026-10-02/revision-v4/entry-coverage-table.md:37-38`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:93-94`。

参考定位（固定提交）：`Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb:291-351`；`Data/Scripts/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb:91-106`；`Data/Scripts/010_Data/002_PBS data/010_SpeciesMetrics.rb:32-68`；`Data/Scripts/010_Data/001_GameData.rb:138-144`；`Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb:4-68;543-563`。

### RUN-C-017 · P2 · 物种招式选择器的默认招式预选错位未承接

类型：default_selection_coverage_gap；状态OPEN；置信度HIGH；范围：WP73-A。

合法招式优先的选择器只记录两段排序，未描述传入当前招式后实际初始选中行及错误偏移。

列表是“合法招式段＋完整招式段”。完整段找到默认招式时使用该段的局部下标，却把它当合并后列表下标；默认在合法段第0项时还会被后续查找覆盖。取消仍保留旧值，但确认初始行可能改成另一个招式。

前提：合法段只有招式A；完整表按名称序为A、B、C；当前招式为C，三项均已定义；打开训练家个体的招式属性后不移动光标而USE确认。

最小对照：合并行是A、A、B、C，当前C在完整段下标2；初始选中合并第2行B，确认后父槽得到B而非C。BACK返回空再由属性保留C，两个动作不能混同。

影响：默认输入/输出无法从规格确定；按直观当前值预选会与参考的实际编辑结果不同。

最低更正：以行为向量定义合法段/完整段、初始行和确认/取消结果，并明确这是来源边界；不要求照搬列表容器或下标算法。

复核条件：覆盖默认在合法段首项、非首项、仅完整段三种前提；对照确认与BACK，保留两段中同招式可重复出现的事实。

项目定位：`specs/demo/wp73-a-content-editors.md:73;138;215`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:57;122`；`review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md:22;53`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:66`。

参考定位（固定提交）：`Data/Scripts/020_Debug/001_Editor_Utilities.rb:181-218`；`Data/Scripts/020_Debug/002_Editor_DataTypes.rb:546-563`；`Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb:639-642`。

### RUN-C-018 · P2 · 字符串/进化子编辑确认原值会自匹配删项，字符串ESC也可到达

类型：unchanged_value_self_deduplication_gap；状态OPEN；置信度HIGH；范围：WP73-A。

正文只概括“改为已存在值/路径时删除本项”，未明确重复查找包含被编辑项自身以及未改值的路径；测试未给出该边界。

字符串集合编辑没有新旧值不同的守卫，非空旧文本也会匹配本项并删除。自由文本ESC返回旧文本，因此同样到达删除分支。进化工作列表中确认原物种、原方法或原参数也会自匹配删除；但进化数值参数BACK具有−1取消值，返回空并跳过删除，不能泛化成所有取消都会删。

前提：字符串工作集合只有非空值A，选择Edit，ESC取消文本输入或直接确认原值；进化对照：子编辑工作集中已有一条路径（可在本次先新增），再确认其原物种/原方法/原参数；只有随后子页保存且父层确认保存，局部删除才落盘；父层No的规则不变。

最小对照：字符串ESC后该项已从工作列表移除；选择Keep Yes会将空集合回父槽。进化确认同值会删当前路径，而数值参数BACK不会删。

影响：取消/未改值被误理解为无操作，数据删除的可达性及保存边界不完整。

最低更正：明确自匹配与两类取消；增加单项集合/单路径的同值确认和ESC/BACK对照，分开工作列表变化、父槽回写及文件保存。

复核条件：字符串ESC→旧文本→自匹配删除链；进化确认旧值与独立取消哨兵的相反结果；不得把子页删除直接宣称为已写文件。

项目定位：`specs/demo/wp73-a-content-editors.md:68;88;151`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:52;72;135`；`review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md:15;29`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:64`。

参考定位（固定提交）：`Data/Scripts/020_Debug/002_Editor_DataTypes.rb:290-327;1466-1526;1535-1552`；`Data/Scripts/020_Debug/002_Editor_DataTypes.rb:1350-1378`；`Data/Scripts/007_Objects and windows/011_Messages.rb:821-848`。

### RUN-C-019 · P2 · 天气属性取消的结果取决于停在哪个输入阶段

类型：multi_stage_cancel_overgeneralization；状态OPEN；置信度HIGH；范围：WP73-A / WP73-B。

原稿/净化稿统一写“取消或选None→空”，没有限定为天气类型选择阶段。

天气类型列表取消或选None会清空；选择了新天气后，概率数字框BACK返回旧概率（没有独立取消哨兵），随后返回新天气与旧概率组合，父属性会接收这个新组合。

前提：原天气W1、概率30；W1/W2均为已登记非None天气；先选择W2，再在概率输入按BACK；最后父页是否保存另行决定。

最小对照：父属性收到W2/30，并非空，也非旧W1/30。若在第一阶段BACK则收到空；两者必须分别预测。

影响：未来实现可能错误清空天气或回滚已选天气，无法设计唯一的取消测试预期。

最低更正：按“类型选择取消／None／概率BACK／正常概率确认”分列返回值及父层保存门；不要套用全局取消规则。

复核条件：数字框默认/取消返回与调用方无条件组合返回一起核验；父页No丢弃局部新组合、Yes保存的后置边界保持。

项目定位：`specs/demo/wp73-a-content-editors.md:76`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:60`；`review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md:24`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:49`。

参考定位（固定提交）：`Data/Scripts/020_Debug/002_Editor_DataTypes.rb:860-881`；`Data/Scripts/007_Objects and windows/011_Messages.rb:93-111;166-205`；`Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb:793-816`。

### RUN-C-020 · P2 · 共享文件列表缺目录/图形载入失败不都回落为空白

类型：resource_failure_overgeneralization；状态OPEN；置信度HIGH；范围：WP73-A。

原稿与净化稿称图形/音频缺失仅显示层回落，并把列表器预览概括为有异常捕获的空白回退。

图形和音乐列表先直接切入指定目录；目录不存在时没有本地捕获，无法到达“没有文件”消息。普通图形列表的预览也无训练家图列表所具备的局部异常捕获。保护只存在于具名训练家图预览等路径，不能推广到所有列表。

前提：宿主及前置UI构造正常；指定Graphics/Windowskins或Audio/BGM子目录不存在；对照是目录存在但没有匹配文件；不假定真实素材已验证。

最小对照：存在但为空的目录可给“没有文件”消息并正常返回；不存在的目录在切换目录处失败。二者不等价于统一空白预览。

影响：失败合同虚构了不存在的降级能力，隐藏异常传播/清理边界，尤其与U01缺素材前提相关。

最低更正：分别列缺目录、空目录、具名受保护预览与普通未保护预览；保留宿主异常显示/恢复未验证，不承诺所有失败都变成提示。

复核条件：从属性入口到列表commands/refresh及底层图形加载的保护范围逐段核对；正常dispose恢复BGM的承诺须限定正常退出，不凭它推导异常也必恢复。

项目定位：`specs/demo/wp73-a-content-editors.md:39;137;173-175`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:23;121;157-159`；`review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md:23;52`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:65`。

参考定位（固定提交）：`Data/Scripts/020_Debug/003_Editor_Listers.rb:117-179;185-244;516-527;615-627`；`Data/Scripts/020_Debug/003_Editor_Listers.rb:13-58`；`Data/Scripts/007_Objects and windows/007_BitmapSprite.rb:176-195`。

### RUN-C-021 · P2 · 无询问复合子页返回会把未指定IV/EV归零，并可建立零宽地图尺寸

类型：nullable_composite_default_materialization_gap；状态OPEN；置信度HIGH；范围：WP73-A / WP73-B。

规格说明IV/EV/地图尺寸子页BACK直接回父槽，但未给出空输入在返回时被实体化的精确结果。

IV/EV原来未指定时，进入子页显示空项，直接BACK会返回六项全0的显式集合；逐项取消得到的空也在子页返回时变0。训练家加载对“整个集合未指定”才使用按等级计算的默认值，因此仅打开子页再保存会改变实际个体。地图尺寸原空时也会建立宽0/空有效格文本的结构；1–30仅是打开宽度数字输入后的范围。

前提：20级训练家个体的IV与EV整字段原未指定；无加载钩子改写这些值；分别打开IV/EV子页，不调整任何项，BACK返回；随后父层/外层正常确认保存；地图尺寸对照：原字段空，打开子页直接BACK后父层保存。

最小对照：原训练家加载时每项IV10、EV30；保存显式全0后每项都0。地图尺寸对照由未指定变为宽0与空串，不能预测为保持空或默认宽1。

影响：缺省与显式零的语义被混淆，改变训练家数值及地图元数据；子页“无询问”不够决定输出内容。

最低更正：补未指定、部分空、逐项取消、仅打开后BACK的返回值表，明确父层No/Yes及实际加载默认值差异。不要把归零改成“合理保留”来修参考。

复核条件：字段不存在和六项零集合分别走训练家加载两分支；IV/EV例20级只做独立固定算术10/30，不执行生成；地图宽0初始化与数字编辑范围1–30分开。

项目定位：`specs/demo/wp73-a-content-editors.md:75;80;85;107;152`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:59;64;69;91;136`；`review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md:9;24;26;40`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:56;67`。

参考定位（固定提交）：`Data/Scripts/020_Debug/002_Editor_DataTypes.rb:607-690;730-738`；`Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb:620-627;648-680`；`Data/Scripts/010_Data/002_PBS data/015_Trainer.rb:86-101;154-164`。

### RUN-C-022 · P2 · 物种编辑读取旧进化字段名，保存可清空现有进化；参数转文本时点也被误述

类型：schema_key_and_side_effect_timing_mismatch；状态OPEN；置信度HIGH；范围：WP73-A / WP04。

原稿/净化稿认为物种属性会读出当前进化路径，并以“打开后No使原参数转文本”为共享副作用例；普通保存被描述为保存用户所编辑的物种数据。

实际编辑属性用复数Evolutions，而取值逻辑对该旧键直接返回空；随后编辑器填默认空列表。若用户不重新填进化列表而确认保存，所选物种的全部进化条目会被空表替换并保存，包含前向及前身条目。参数转文本位于单数Evolution取值分支，由PBS反写真正调用，不是此编辑打开分支。

前提：已编译且数据一致的基础物种A有A→B的等级进化；B为终末基础物种，含由A生成的前身条目；打开A物种属性，不操作进化子页；分比较父页No与Yes；保存/反写正常完成；没有插件替换此字段映射。

最小对照：父页No：不会因该进化取值把A的数值参数转文本；父页Yes：A的进化列表为空并进入数据档案/PBS，即使只改名称或没有改字段。B已有的反向条目仍留在当前数据/档案；之后整体重编译按新PBS重建关系。

影响：普通内容保存的破坏性结果漏记，且已登记共享副作用的触发时点错误；后续实现可能保留原进化或在错误时点改参数，均不等价。

最低更正：按精确字段名重写“打开/取消/保存/反写/重编译”五阶段合同，列空表覆盖与前向/反向关系分层；把转文本副作用归到真正调用单数字段的路径。旧审计保留，本审查不修参考或倒写AX历史。

复核条件：editor_properties字段名→get_property分支→默认填充→schema保存逐步核验；区分所选物种条目丢失与其它物种保留的反向记录；单独核反写遍历对未丢失路径参数的运行中类型变化，不用“打开即转文本”替代。

项目定位：`specs/demo/wp73-a-content-editors.md:35;119;154-155`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:19;103;138-139`；`review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md:9;42`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:58;64;67`。

参考定位（固定提交）：`Data/Scripts/010_Data/002_PBS data/008_Species.rb:103-108;147;392-440`；`Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb:940-979`；`Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb:292-365`；`Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb:174-223`；`Data/Scripts/010_Data/002_PBS data/008_Species.rb:299-327`。

### RUN-C-023 · P2 · 空训练家个体槽尚未选物种时，打开招式选择会失败

类型：missing_required_input_failure_branch；状态OPEN；置信度HIGH；范围：WP73-A。

TrainerPokemonProperty只记“物种为空则整槽返回空”和合法招式优先，未记录在返回前操作依赖物种的属性所需前提。

新增空槽把物种设为空，但四个招式属性仍可操作。物种招式选择器立即查询该物种的合法招式；严格物种查询不接受空值。整槽返回空的检查在属性页关闭之后，不能保护更早的招式操作。

前提：在训练家编辑器打开一个尚未使用的个体槽；物种仍未指定；前置UI正常，直接选择任一招式属性；未先选物种。

最小对照：操作在合法招式查询处失败，未到关闭子页后“整槽返回空”的正常路径；单纯BACK关闭未指定槽才正常返回空。

影响：可见的新建工作流缺少必要输入与失败行为，未来实现可能提供空合法集或温和提示而与参考不同。

最低更正：明确物种未指定时招式属性的限定失败，给出先选物种与直接BACK的对照；不把源异常自动修为禁用按钮。

复核条件：空槽初始化→招式属性创建→选择器→严格查询→本地异常传播；不声称发生文件写入，不推断宿主最终恢复画面。

项目定位：`specs/demo/wp73-a-content-editors.md:73;107`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:57;91`；`review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md:22;40`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:56;66`。

参考定位（固定提交）：`Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb:604-654`；`Data/Scripts/020_Debug/002_Editor_DataTypes.rb:546-553`；`Data/Scripts/020_Debug/001_Editor_Utilities.rb:4-13;181-189`；`Data/Scripts/010_Data/001_GameData.rb:99-104`。

## 原问题影响扩展，不重复计数

- **RUN-C-005**：指标编辑预览在文件保存之前已消费当前登记值；档案重载替换登记表，不向已布局普通战斗精灵广播位置更新。原“保存后读取方立即新数据”应继续限定直接查询/快照/布局消费者。
- **RUN-C-003**：CE-M10“口袋选0”应明确为取消导致属性返回0，不能解释为选择列表第0行；第0行确认返回第1口袋。与已有测试前提不充分合并，不新增计数。
- **RUN-C-006**：补读的属性/列表/工具再次确认源类名及调用组织残留；原问题保持，不按每个同名类重复编号。

C-001至C-015的原始记录不改写；本报告不按“又看到相同源类名/同一宽泛生效句”再次新增编号。C-022是新证明的精确字段名/触发时点错配，不能沿用旧文“打开即转文本”的推导。此补充修正的是规格判断，不修改参考或倒写既有AX审计。

## 独立指标场景的要点

保存档案、产生PBS路径、输出该路径内记录、重新装载、实际显示取值是不同阶段。仅基础形态的**保存时登记集合**不会产生PBS路径；带同后缀非零记录才可打开该路径，即使非零记录之后因与基础值全等而被省略。不同后缀可以只更新部分PBS文件。预览/自动定位会惰性建立记录，故不能把进入前只有基础形态的文件内容直接当成保存时集合。数据档案保存先发生，后续PBS失败不回滚已存档案。

指标编辑预览在改运行值时即刷新，普通战斗精灵在设置位图/重新定位时应用指标，普通逐帧更新不重新取指标。因此整体重载或保存不等于所有已布局精灵马上变位置。完整首判及五组条件对照保存在独立文件中，未运行任何保存或编译。

## 已核实的边界与未报为缺陷的候选

- 数值/布尔取消子型、父页确认、共享池打开时规范化、地区图鉴No压空和空表非终止、训练家新建嵌套反写、改键覆盖、地形文件B/内存C等既有来源事实，继续按具名前提承接，不因反直觉自动修正。
- 进化数值参数BACK有独立−1取消值，返回空而不进入自匹配删除；C-018只将**确认原值**的进化分支与**ESC返回旧文本**的字符串分支并列，未泛化成所有取消都删。
- ACTION＋方向的交换先经过命令窗口移动光标；只看交换表达式会误判方向，本批已追到窗口更新。未把它报成上下倒置。
- 图形/音乐文件列表按带扩展名的完整文件名匹配预选；去扩展名旧值通常回到首行。元数据列表对非首角色的预选实际落在首角色行。这些默认定位事实已在矩阵登记；本批新C-017集中于招式选择器可导致确认返回另一招式的错位。
- 旧进化家族辅助三函数和EnumProperty2：已读来源；全Scripts仅定位定义/内部互调（EnumProperty2另标Unused）。没有把它们归零为“功能不存在”，也没有把未证demo直接调用当默认编辑入口。
- 动画组织器、动画分配/文件复制共享辅助已读；组织器No可能保留运行动画缓存改动，复制有“比较路径/实际写目标”分层。完整动画交换和生成/转换工具仍归后续C-02，不在本批冒充整工具通过。

## 检查与后续

只新增C-01-S2目录内六份标准审查文件及一份独立首判；无新框架实现、API设计、源码片段复制或参考修改。只做静态搜索/文本阅读与固定常数算术（20级默认IV10、EV30）；未运行游戏、UI、编译、反序列化、转换、生成器或模拟器。读取范围采用commit＋path＋range，未新增常规SHA表。

U01–U10、G01–G12、既有20项AX及未验证配置/插件/随机组合保持审查保留；已证demo事件链与运行观察仍为0。素材、地图、宿主文件、真实插件材料未补造。对于C-022揭示的旧文字错配，应由统一修订明确更正其归属与时点，不以“保留旧记录”把不成立的反例升级为来源事实。

Astra/Ultra沿用原成功spawn证据；speed **UNVERIFIED**，未改变服务速度。提交/推送只C分支，精确远程回执由本批回报给出，checkpoint不预报网络成功。完成本批后等待C-02（WP74/75/77）授权派发。
