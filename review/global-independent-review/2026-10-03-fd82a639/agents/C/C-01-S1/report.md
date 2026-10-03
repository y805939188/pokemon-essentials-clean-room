# C-01-S1：WP72 来源覆盖补审

**结论：NEEDS_REVISION_SCOPED。** 本批补齐 WP72 七份主文件的剩余阅读，并完成全部主注册节点的逐行为族承接处置；这不是全局通过，也不将 WP73 的未读部分升级。

## 身份与独立性

- 项目行为输入固定 `e1e01bb18d824931e54f182dd61af5a9f908ba85`；参考只读独立克隆固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。
- C-01 原报告与首判提交 `01fa3c2f36923127eff9168abe142aca8b6d787b` 保持原样。本批是该首判之后、**同一独立主审的延续**，不是第二位审查者；没有阅读 A/B/D 本轮结论。
- 写入仅限 `review/global-independent-review/2026-10-03-fd82a639/agents/C/C-01-S1/`。未改原规格、净化稿、中央审计/Feature Matrix、历史报告或 reference；未运行参考、游戏、编译/转换/生成/反序列化器或行为模拟器。
- 沿用成功 spawn 的 Astra/Ultra 明确配置证据；speed **UNVERIFIED**，未宣称实测 Standard，未改变速度。

## 阅读和承接结果

C-01 已实质读过的菜单框架、120项效果表/编辑器与其它具名段不重复阅读。本批新增主文件余段 **3,903 行**；合并 C-01 的 **1,856 行**，七份 WP72 主文件累计 **5,759/5,759 行**实质阅读，无剩余主文件行段。这里的数字只做防漏核对；判断依据是各行为分支、调用者和状态效果的阅读。

四份注册主文件共 **161 个节点**（含分组节点；不是161项独立功能），全部映射到 equivalence.tsv 的37个行为族。每族记录原文/净化承接、DG场景、取消/失败/写入分层与判断；机械检查只验证没有漏映射，不能代替语义判定。reference 的读取范围和前次累计范围见 source-coverage.tsv；本批 reading-log.tsv 不增加SHA列。

重点反核了：寄养与遗迹石的事件选择器写入；静默添加容量预检；预设队伍的固定内容；非战斗与战斗 Teach 的差异；HP写入后的状态/进化待办/Hyper变化；性格重算；PPUp的总PP消费；变身刷新门；奇妙空间读写方向；电话和货币修改；所有主菜单编辑/文件工具入口。工具主体仍按 WP73/74/75/64 的分工委派，不能把入口覆盖当作整个工具内部通过。

## 新发现

### RUN-C-008 · P2 · 完整调试菜单的 Use PC 入口没有规格或测试承接

类型：registered_capability_omission；状态 OPEN；置信度 HIGH。

WP72 声明覆盖世界控制与完整入口，正文/覆盖表/DG 目录只列“打开存储”，没有“Use PC”入口。

Field options 下独立注册 Use PC，打开通常的 PC 主菜单，经 PC 菜单可访问不同服务；Pokémon options 下的“Access Pokémon storage”则直接进入盒子整理模式。这是两个不同入口。受限菜单因 Field 父级排除而不可达。

最小前提：调试标志真，完整地图或暂停调试菜单；正常玩家/PC 菜单数据可用。

最小对照：选择 Field options → Use PC 会出现“访问哪台 PC”的服务选择；只实现文中直接打开盒子整理的能力不能产生该结果。

影响：主注册能力被整项遗漏，可能把 PC 主导航与直接盒子整理合并，丢失玩家 PC 等可达服务。

最低更正：增设 Use PC 的层级、完整/受限可达性、正常 PC 合同委派及取消返回；给出与直接盒子整理的对照。更新 Feature Matrix 的修订追踪由作者完成，本审查不改中央文件。

复核条件：正文、覆盖表、DG 至少一个对照场景承接该入口；检查没有将 PC 主菜单误述为直接整理盒子。

项目定位：`specs/demo/wp72-debug-contexts-and-controls.md:18-25;71-119;134-139`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:53-94;110-118`；`review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md:21-41;62`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:11-40`。

参考定位（固定提交）：`Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb:41-48;705-716`；`Data/Scripts/016_UI/019_UI_PC.rb:134-154`。

### RUN-C-009 · P2 · 寄养与遗迹石选人取消仍覆盖固定事件变量

类型：hidden_persistent_write_on_cancel；状态 OPEN；置信度 HIGH。

WP72 将选择列表取消概括为无写入，寄养和遗迹石的状态表未记录固定事件变量的覆盖。

寄养空槽存入调用事件选人助手，把选择索引写变量1、名字写变量3；取消也写−1和空串。遗迹石在存在可净化成员的前提下调用同族助手，但使用变量1和2。每次变量写入还请求地图刷新；取消仅阻止寄存/净化业务提交。

最小前提：世界场景存在事件变量表与地图；寄养有空槽、队伍非空，变量1原99、变量3原“保留名”；进入存入选择后 BACK；遗迹石对照：外层合格成员存在，变量1/2各有旧值，再取消选人。

最小对照：寄养取消后队伍/槽位不变，但变量1＝−1、变量3＝空串，地图刷新请求为真；遗迹石对应变量1/2被覆盖。并非取消净化就等于没有任何持久状态写入。

影响：事件作者状态会被调试操作覆盖；后续实现若使用无副作用选择器，与参考的取消与事件变量兼容行为不同。

最低更正：把“取消不写”限定为本次寄存/净化提交，明确两个入口各自的变量编号、成功/取消输出与刷新副作用；补取消向量。

复核条件：调用方实参→选人返回→变量写→业务提交门的四段链完整核对；保留 WP66-A 事件助手通用合同，同时补本入口固定变量编号。

项目定位：`specs/demo/wp72-debug-contexts-and-controls.md:97;112;301`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:79;94;283`；`review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md:31;41`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:19`。

参考定位（固定提交）：`Data/Scripts/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb:353-368`；`Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:147-160`；`Data/Scripts/016_UI/005_UI_Party.rb:1141-1169;1504-1527`；`Data/Scripts/019_Utilities/001_Utilities.rb:516-520`。

### RUN-C-010 · P2 · 示例队伍缺少固定物种顺序与逐物种招式映射

类型：deterministic_fixture_data_omission；状态 OPEN；置信度 HIGH。

正文只说“6 个预设物种”并列举一串场地招式，DG-M11 只要求六只20级；未给出六物种或教授顺序。

该命令的预置内容是固定可观察数据：按皮卡丘、比比鸟、勇基拉、暴鲤龙、地鼠、吉利蛋顺序过滤存在物种；每只20级。附加招式依物种按固定次序教授，最后记录初始招式；皮卡丘没有额外教授步骤。教授超容量时遵循既有静默学习的移除最早招式规则。

最小前提：默认六物种与相关招式均定义；命令从完整调试菜单执行；不要求随机个体值或随机源实际序列相同。

最小对照：任何六个不同物种的20级队伍都能满足当前正文/DG-M11 的字面，但参考首只必须是 PIKACHU，第二只 PIDGEOTTO 并执行教授 FLY，且次序固定。

影响：示例行为无法从净化交付独立复现，功能演示与可设计测试缺失确定输入数据。

最低更正：提供小型行为数据表，列六物种顺序、各自附加招式及其顺序、存在性跳过规则、记录初始招式时点；这些是数据身份，不应因净化删去。DG-M11 增明确前提与预期成员。

复核条件：数据表与参考预置逐项核对，不复制源语句；缺一种物种时保持其余相对顺序并少一成员；不错误补到六只。

项目定位：`specs/demo/wp72-debug-contexts-and-controls.md:134;342`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:116`；`review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md:60`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:21`。

参考定位（固定提交）：`Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb:654-693`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:646-660`。

### RUN-C-011 · P2 · 奇妙空间中防御/特防编辑的显示与生效方向未定义

类型：cross_domain_edit_readback_gap；状态 OPEN；置信度 HIGH。

WP72 将战斗能力值编辑概括为逐项写当前战斗数值；正文与DG没有奇妙空间开启时的读写方向及回读反馈。

菜单初始值从当前防御/特防读取，奇妙空间会交换这两个读取结果；但写入仍分别改原防御/原特防。菜单当前局部显示行随后显示输入值，重新进入才重新读取。WP45 只说明读取互换，未描述此调试读写交界。

最小前提：非变身在场成员；原防御100、原特防200；奇妙空间期限为正；进入能力值编辑，把显示为200的防御项设为300；期间不推进回合、不执行重置、不过战斗调试总退出刷新链。

最小对照：当次菜单防御行显示300，但实际防御读取仍为200、特防读取变为300；关闭该子菜单再进入，显示防御200/特防300。不能把界面写入值等同同名有效能力值。

影响：调试效果与反馈的跨域行为无法确定；直观地设置有效防御300会与参考不等价。

最低更正：增奇妙空间下的独立行为对照，区分菜单输入、当前显示缓存及战斗读取结果；不复制访问器结构，也不自动修参考。

复核条件：防御和特防各做对称向量；无奇妙空间对照正常同名写入；明确向量停留在子菜单范围，避免混入额外刷新或回合结束。

项目定位：`specs/demo/wp72-debug-contexts-and-controls.md:217`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:199`；`review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md:111`；`deliverables/final-specification-set/combat-requirements/wp45-weather-terrain-side-and-position-effects.md:104`。

参考定位（固定提交）：`Data/Scripts/020_Debug/003_Debug menus/005_Debug_BattlePkmnCommands.rb:179-240`；`Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb:91-103`。

### RUN-C-012 · P2 · 战斗调试 Teach 绕过普通学招的 Shadow 拒绝门

类型：incorrect_normal_flow_equivalence；状态 OPEN；置信度 HIGH。

WP72 §7.4 称战斗内 Teach 为“正常学招写原”，没有说明与非战斗调试 Teach 的 Shadow 资格差异。

非战斗调试调用普通学招助手，Shadow 总是被拒绝；战斗调试只检查招式数、取消和已知招式，随后直接教授，并在存在在场对象时追加战斗招式。它不调用 Shadow 拒绝门。调试标志可解除普通助手的蛋门，但不会解除其 Shadow 门，因此不能泛化为调试都走同一资格逻辑。

最小前提：合法 Shadow 成员，已知招式少于最大数，选择一个已定义且未学会的招式；正常调试模式；比较非战斗个体调试与战斗内队伍/成员调试入口。

最小对照：同一前提下，非战斗 Teach 提示 Shadow 不能学招且不新增；战斗调试 Teach 新增原招式，有在场对象时再追加战斗招式。只陈述提交时状态，不推断后续净化/形态更新保留所有招式。

影响：引用正常学招会让独立实现错误拒绝该战斗调试操作，或错误放宽所有非战斗 Shadow 学招。

最低更正：把战斗 Teach 明确写为独立调试路径，列其三个守卫和不存在的 Shadow 门；补两入口对照测试。保留非战斗正常助手规则。

复核条件：两入口调用链及 Shadow 拒绝位置逐段核对；原招式/战斗招式两层预期仍按有无在场对象区分。

项目定位：`specs/demo/wp72-debug-contexts-and-controls.md:165;220`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:147;202`；`review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md:80;114`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:29`。

参考定位（固定提交）：`Data/Scripts/020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb:460-470`；`Data/Scripts/020_Debug/003_Debug menus/005_Debug_BattlePkmnCommands.rb:468-488`；`Data/Scripts/013_Items/001_Item_Utilities.rb:582-601`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:646-660`。

### RUN-C-013 · P2 · 只有一个玩家角色时并非只有提示：延后执行的退出分支会失败

类型：unrecorded_source_failure_branch；状态 OPEN；置信度 HIGH。

玩家角色选择及覆盖表仅记“只有一个定义→消息”，未记提示后的异常分支。

该效果作为普通非lambda闭包注册，随后由菜单调用；数量恰为1时显示消息后使用非局部退出。按标准 Ruby 非lambda闭包控制流，该延后执行的退出会触发 LocalJumpError，而非正常结束该效果。本地没有异常捕获。宿主最终显示/恢复方式未执行确认。

最小前提：有效配置只注册一个玩家角色；从已经装载完成的正常调试菜单执行 Set player character；消息正常结束；采用参考语言的普通非lambda闭包语义，不假定未见的宿主语言改写。

最小对照：先显示只有一个角色的提示，随后在打开选择列表或修改角色之前发生控制流异常；不能把这一支描述成已证明安全返回菜单。

影响：配置分支的失败行为被净化为无害提示，会导致兼容测试和异常恢复要求遗漏。

最低更正：将这一来源异常作为限定静态失败记录：提示已显示、角色未改、本地不恢复；全局宿主结果保持未验证。审计留源语义解释，行为正文不必规定语言或类结构。

复核条件：注册保存→延后call→单条目分支→异常向上传播的静态链；不把异常事实列为源代码修复任务；不宣称实际宿主崩溃或重启。

项目定位：`specs/demo/wp72-debug-contexts-and-controls.md:123`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:105`；`review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md:52`。

参考定位（固定提交）：`Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb:1076-1099`；`Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb:83-86;118-122`；`Data/Scripts/003_Game processing/005_Event_Handlers.rb:97-112`。

非局部退出仅用 [Ruby Proc 语言文档的 Orphaned Proc 说明](https://ruby-doc.org/core-3.1.2/Proc.html#class-Proc-label-Orphaned+Proc)作静态语义核验，未执行其中示例或参考程序；未将文档版本当作已验证宿主版本。

### RUN-C-014 · P3 · 普通随机 EV 总额的上界是否可取未明确

类型：numeric_contract_ambiguity；状态 OPEN；置信度 MEDIUM。

原稿/净化稿只写“总额上限内的随机值”，测试只测最大随机全体，没有普通随机总额的端点定义。

普通随机目标是0到总额上限减1的离散整数，均匀取目标；最大随机分支则恰为上限。默认总额上限510时，普通随机取不到510。原表述可被读作含上限，属于可消除的数值合同歧义。

最小前提：默认 EV 总额上限510，选择 Randomise all，而不是 Max randomise all。

最小对照：目标509可取、510不可取；最大随机分支目标510。这里只核随机目标支持集，不将最终六项EV分布误称均匀。

影响：未来独立随机实现可能将上端点纳入，形成不同支持集和概率。

最低更正：明确普通随机目标的闭开区间与整数性，最大分支独立描述；增加端点静态向量。

复核条件：两种命令的目标选择分支分开；不模拟随机序列，不对六维最终分布作无证均匀保证。

项目定位：`specs/demo/wp72-debug-contexts-and-controls.md:160`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:142`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:24`。

参考定位（固定提交）：`Data/Scripts/020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb:255-269`；`Data/Scripts/020_Debug/003_Debug menus/005_Debug_BattlePkmnCommands.rb:336-350`。

### RUN-C-015 · P3 · 战斗背景及底座名称输入的100字符上限未记录

类型：input_limit_omission；状态 OPEN；置信度 HIGH。

背景名称控制只写自由文本及空文本回落，没有输入长度上限。

Backdrop 和 Base modifier 两个输入均配置最长100字符。这个限制属于输入合同，与通用属性文本的250字符上限不同。

最小前提：进入战斗背景名称调试项，尝试提交101字符名称；输入控件按给定上限工作。

最小对照：两项均不能接受超过100字符的输入；空名称分别回落Indoor1/无值。仅实现无限文本或复用250上限与参考不同。

影响：可输入值域和边界测试不完整；资源是否存在仍是独立未验证项。

最低更正：在两项输入字段补100字符上限，并为DG-M21加100/101长度对照。

复核条件：两项上限均为100；不误改其它250字符文本输入；保留空文本回落和资源未证声明。

项目定位：`specs/demo/wp72-debug-contexts-and-controls.md:241`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:223`；`review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md:119`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:31`。

参考定位（固定提交）：`Data/Scripts/020_Debug/003_Debug menus/004_Debug_BattleCommands.rb:399-418`。

## 已确认承接，不重复报缺陷

- C-001/C-002 的表达式开关问题、C-006 的净化残留、C-007 的白名单交付缺口继续保留，本补审不重复编号。C-003/C-004/C-005 亦不撤销；本批不改其原首判。
- 变身时能力刷新不覆盖复制来的五项能力，由 WP39 §6.1 已明确承接；不能因 WP72 单句“同步”而忽略该有界引用，未另报重复问题。
- 复制的独立招式/IV/EV/拥有者与邮件等共享边界，由 WP18 §5 已逐项描述，源码克隆段与其一致；不把“非全深复制”本身当规格缺陷。
- 打开净化室先把见过标志设真，由 WP23 §8 已说明；本批追到实际写入，未当成新遗漏。遗迹石和寄养的**固定事件变量编号**及取消后写入则属于 C-009 的新交界缺口。
- Shadow 经验赋值暂存、HP归零清异常/待进化/Hyper、正常治疗对蛋早退，以及填盒数值0/1都登记闪光等来源事实保持；没有自动修参考。
- 标准席位初始化同时建立在场对象与位置；人为破坏成“位置存在而在场对象不存在”时位置列表可能失败，这不被升级为已证正常运行故障。未知/异常对象组合仍具名保留。
- 天气/场地改期限的0映射受“与现值比较”门限制；同值不写。DG-M21的用例解释应采用合法已生效天气/场地与具名当前期限，不凭简写推成任何0状态均改为无限。

## 后续与范围保留

C-01-S1 已完成授权的 WP72 主来源补齐，仍需作者修订上述问题并由后续复核确认。WP73 的属性/选择器/列表剩余来源留 C-01-S2；WP74/75/77 留 C-02，未提前展开或给通过结论。翻译编译入口的可变路径实参与整个工具的实际文件合同在后续 WP75 继续核验，本批已读入口本身。

U01–U10、G01–G12、既有20项AX、未验证随机/配置/插件组合原样保留；本批新识别的来源异常只作为待登记的静态事实，不擅自修改AX中央清单。已证 demo 事件链＝0，运行观察＝0；地图、图形、音频、宿主文件和真实插件材料缺失均未补造。完整源文件阅读不等于所有外部配置组合、宿主异常处理或运行行为均已验证。

本批提交/推送仍限定C分支；checkpoint.json记录写入时进度与校验，最终本地/远程精确提交由批次回报给出，不在文件中伪造自引用提交哈希。
