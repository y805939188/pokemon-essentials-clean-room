# Generic kernel R1 独立复核

固定候选 `5666b7b912e2fb79b5119283ee6a37401a7071db`；结论 **FAIL（需返修）**。旧66行：61 PASS、5 FAIL；新活跃64行：62 PASS、2 FAIL；3个退役旧行及3个元数据后继均逐项检查。11正文＋2catalog共258标题（172行为映射、86元数据映射），分母分别保留。

本审者非作者，只读候选与固定Git对象，只写本目录kernel-*；没有运行Ruby、游戏、宿主、Showdown、业务向量或未来框架。请求gpt-6.1-sol / ultra / default / normal / Fast off；权威创建/执行model、effort、tier、speed、Fast及云UUID逐字段UNVERIFIED。

## 必修问题

### R1-KF-001 / P3 — 元数据消费者仍由整篇/邻近WP泛连，遗漏真实责任及具名跨域验收消费者

退役不是丢弃原责任表。稳定ID/完整归档已满足，但消费者的语义关联仍不满足完整复核合同；同WP或邻行并非真实主责证明。

- **META-000019 / FR-000392**：`/metadata_records/18/feature_refs`；组合表明确指编译生命周期、亲密/进化/战斗、场地能力、插件和Shadow/捕获；现refs含FR385–387钓鱼，而无WP04编译、WP30亲密、WP59场地、WP05插件、WP38捕获主责。配置词典有钓鱼开关不证明§7表与这三钓鱼行的直接责任关系。
- **META-000020 / FR-000398**：`/metadata_records/19/feature_refs`；字段责任表明确Species能力→WP19、学习→WP30、状态→WP20、Item→WP27/28、指标→WP15/WP67-A等；现大量refs是WP02/03/04邻行，无这些具名主责。部分WP21/31/62/63链接正确不能覆盖其余责任。
- **META-000021 / FR-000407**：`/metadata_records/20/feature_refs`；首项文本提取/翻译/保存归WP08，数据/世界编辑器归WP73；资源/呈现归真实播放方。现无WP08/内容世界编辑主责，FR277仅动画编辑入口、FR355仅音频，不能代表这些交界。
- **DOC-0108 named catalog consumers**：`section-coverage.json:/sections/2226/feature_refs; /sections/2227/feature_refs; /sections/2228/feature_refs; /sections/2230/feature_refs; /sections/2231/feature_refs; /sections/2232/feature_refs`；9个标题全用同一37行列表。KC03场地许可、KC05/06语言入口、KR13 Nature/WP19及KL的地图连接/编辑消费没有链接至其实际领域主责；U01-M01-021/022与J01-V01–06/V11具名地牢/图块集，未关联WP14真实消费者；R6-U14-FLAGS-04是孵化步数失败前缀，未关联WP35；指标编辑No/Yes具名WP73-B而列表无该主责。不是要求每个向量造新ID，可按这些已有跨域主责分组引用。
- **DOC-0109 language image catalog consumers**：`section-coverage.json:/sections/2245/feature_refs`；LZ36–41明确WP15资源解析及WP65控制帮助；该节仍只有FR409–453的同一45行generic列表，FR440只拥有语言图像身份选择，实际指定键图创建/加载消费者未登记。此处不再把catalog→427→excluded745、catalog→445/451→326的有效机器链判为遗漏。

**必要修正：** 保留全部旧行与ID；按完整责任表/具名跨域目录把metadata及section-coverage关联到已有真实主责，可作章节级合并，不要求逐句新增功能；现有父功能→excluded_child_refs子功能的有效机器链可保留。

### R1-KF-002 / P3 — 战斗统计生产依赖仍漏Mega门，诊断失败依赖用途被本地化模板替代

原KF004要求必要调用/状态资格和真实生产/消费方向。补齐文档名仍不足以表达本行实际生产门和失败链。

- **FR-000420**：`/features/398/dependencies`；mega_evolution_count的玩家本人门和先统计后变形/异常前缀在WP22§4.3 L58–60；420仅新连WP42/WP38，wp/direct/feature refs均无WP22生产合同。WP42的正常终局统计不是该先提交点。
- **FR-000436**：`/features/414/dependencies/direct_refs`；4条新增specific reasons为“本地化提取/编译”“消息集合”“语言选项”“语言状态”；实际§6讲编译位置错误、插件输出终止、调试包装与非调试超时紧急保存。路径存在不等于用途正确。

**必要修正：** 给FR420补WP22真实统计生产锚点/既有稳定功能引用；将FR436各direct reason重写为实际编译/插件/主流程与紧急保存的失败用途，并核生成视图。

## 六组原问题逐项裁定

| 原组 | 新裁定 | 证据与剩余 |
| --- | --- | --- |
| KF-001 | FAIL | Retirement/count correction passes; real metadata consumers remain incomplete. |
| KF-002 | PASS | All four concrete mixed-boundary cases corrected through responsibilities and existing feature links; no sentence-by-sentence split required. |
| KF-003 | PASS | Original parent, new collaboration row and explicit parent→excluded-child metadata chain corrected; no duplicated dependency ID required. |
| KF-004 | FAIL | 12/14 original cases corrected; 420/436 remain. |
| KF-005 | PASS | Both exact legacy support scope gates corrected; user decision remains pending. |
| KF-006 | PASS | Document and all ten row source classifications corrected without deleting real stats behavior. |

全部原case分别保存在kernel-results.json/finding_results；没有用作者finding-resolution的处置代替独立裁定。KF003的catalog→父427→excluded_child_refs→子745是有效显式机器链；不要求重复deps.feature_refs或每个catalog标题直接列子ID。世界读档目录经445/451到326同样有效，未误判缺项。

## 阅读与继承

实际新读本域源文本 2302 行；另 635 行仅继承旧独立报告的完整源阅读信用，逐文件字节身份已核。旧36 PASS的源内容、原路由/范围不变部分可保留；每个新职责、依赖、当前定位均重新审查。所有变化或受同根因影响的混合表/章节按下表重读，并读必要下游。没有把继承源信用写成新的全文阅读。

| 文件 | 本次实际新读B8区间 | 当前适用 / 旧全文信用 |
| --- | --- | --- |
| wp02-rule-configuration-and-data-variants.md | 1–32, 204–278 | 908与B8完整字节相同；未重读区间 [[33, 203]] |
| wp03-content-identity-and-schema.md | 1–24, 73–243, 313–393 | 908与B8完整字节相同；未重读区间 [[25, 72], [244, 312]] |
| wp04-pbs-lifecycle.md | 1–56, 184–320 | 908仅L196变更；git show读184–210及完整差分；未重读区间 [[57, 183]] |
| wp05-events-extensions-plugins.md | 1–147 | 908与B8完整字节相同；未重读区间 [] |
| wp06-stats-directory.md | 1–143 | 908与B8完整字节相同；未重读区间 [] |
| wp06-time-random-steps-stats.md | 1–196 | 908与B8完整字节相同；未重读区间 [] |
| wp07-deprecation-appendix.md | 1–54 | 908与B8完整字节相同；未重读区间 [] |
| wp07-diagnostics-files-http.md | 1–191 | 908与B8完整字节相同；未重读区间 [] |
| wp08-localization.md | 1–52, 199–231 | 908与B8完整字节相同；未重读区间 [[53, 198]] |
| wp09-save-startup-continue.md | 1–20, 95–179 | 908与B8完整字节相同；未重读区间 [[21, 94]] |
| wp10-migration-failure-recovery.md | 1–281 | 908与B8完整字节相同；未重读区间 [] |
| generic-kernel-wp02-03-04.md | 1–236 | 908与B8完整字节相同；未重读区间 [] |
| generic-kernel-wp05-06-07-08-09-10.md | 1–288 | 908与B8完整字节相同；未重读区间 [] |

源身份、blob/SHA256、旧全文范围、实际新范围和继承理由均在reading_ledger。依赖阅读包括WP58全文、WP11恢复全节、WP59时钟/巨石推动、WP12移动表、WP13页冷却/解释器表、WP22 Mega提交、WP42终局统计、WP38失败球和WP65标题/语言设置；确切区间见JSON。原源文件被截断的工具输出已由后续分段补读；不声称完整重读未列区间。

本域新视图145行、64行均作关键字段/职责/状态/定位一致性核对；语义基于完整机器行及去重字段投影，未声称逐字完整阅读约百KB重复的literal view。根团队负责整体生成字节/工具校验。metadata view的三条后继链接已直接读，未把生成一致性当消费者正确性。

## 接受回填与身份

候选工作区正式树仍为B8 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。真实current908树为 `6ae817df5b11eafdec671214b0d04e542ad364bc`；WP04当前blob `d895aa9d0df2024d9bcd99f1d954d8a5685f6211`，41768B，SHA256 `70d794ed63d4ff1f98ed21a9aecfea4923063d10a45e69965e7dad294678adb2`。

已真实git show读取861接受回执及548 actual报告/机器结果，并读908的实际§5.2。U02只删除L196特定提示承诺；FR403差异、当前unit/file身份正确，7个活跃WP04行401/402/403/404/405/406/408已按ACCEPTED核对。第8个原WP04行407是完整退役历史，保持旧pending字节，不是第8个当前活跃接受行。全部64当前locator的file/blob/unit/heading身份正确，66旧ID恰落active/retired一次、source完整对象不变，3退役去retirement后与d62完整行逐字段相同；新增745未复用。活跃源有效范围无物理交叠。

U01、U08、U09以及其它已绑定范围仍待整改后核对；U07范围仅历史overlay，不据猜测绑定本域正式来源。861为U02/U03 ACCEPTED=true、CLOSED=false；实际报告的有限静态PASS没有被扩成目标验证、实现/验收、整轮通过。

## 逐旧行与追加行

| ID | 旧判定 | R1判定 / 处置 | 独立理由 |
| --- | --- | --- | --- |
| FR-000388 | PASS | PASS / active | 配置规模、世代基准和默认值作用域仍是框架配置输入；源§3未变，新增WP03/04/08/65合同是身份、编译和消费交界，未替领域规则实施。 |
| FR-000389 | PASS | PASS / active | 完整配置词典的历史全文信用仅用于未改默认/分类事实；新职责仍限作者配置输入，去向未变，领域效果没有被移入本行；直接引用提供编译、语言和UI消费者导航。 |
| FR-000390 | PASS | PASS / active | 默认值派生及显式覆盖、模式联动、直接世代读取是配置规则；重读§5确认框架维护配置关系合理，没有许诺组合兼容。 |
| FR-000391 | PASS | PASS / active | 普通发现与显式输入、候选材料、作者语言配置归框架；§6明确具体本地化/UI归消费者，现有WP08/WP65直接引用承接，材料不等于支持。 |
| FR-000392 | FAIL | FAIL / retired | 退役完整行身份保存，但META-000019没有按§7的真实责任关联编译、亲密/进化、场地能力、插件、捕获；仍有钓鱼邻行式泛连，后继导航不合格。 |
| FR-000393 | PASS | PASS / active | 非法配置、资源ID冲突与发现失败仍保留未知；新框架职责不升级这些事实，依赖指向本篇明确交界。 |
| FR-000394 | PASS | PASS / active | 36类身份/查询与回退的旧源全文事实及范围未变；当前框架登记责任与WP04/02共同合同相符，没有引入内容规则实现。 |
| FR-000395 | FAIL | PASS / active | 重读§4完整混合表，当前WP04承接缺失文件/编译门，WP08承接名称/描述和StorageCreator回退；正确保留原始字段与消费者查找两层。 |
| FR-000396 | FAIL | PASS / active | 重读§5完整schema/复合节头/重复身份/作者数值表，WP04直接引用承接实际解析和编译生命周期；作者数据校验框架候选合理。 |
| FR-000397 | PASS | PASS / active | 固定规则身份目录确有登记顺序及引用拒绝合同；旧全文与当前范围/去向不变，可保留框架数据合同；未把字段责任目录退役误扩至本行。 |
| FR-000398 | FAIL | FAIL / retired | 退役对象完整保存，但META-000020未指到表列的WP19能力、WP20状态、WP27/28道具、WP30成长等主责，邻近WP02/03/04行不能替这些消费者。 |
| FR-000399 | PASS | PASS / active | 可选Shadow缺席与候选材料不等于目标排除；新框架职责仅数据载入及来源边界，当前仍待U09核对。 |
| FR-000400 | PASS | PASS / active | 严格/宽容查询、错型拒绝、副作用与最终宿主未知保持；新WP02/04引用与来源共同交界相符。 |
| FR-000401 | FAIL | PASS / active | 重读§3启动及直接编译全表，新增WP05/07用于真实插件先后和失败诊断；U02接受只回填来源，所有目标验证/阶段仍待定。 |
| FR-000402 | PASS | PASS / active | 解析/校验旧全文信用适用于未改的§4；U02只改§5.2，当前locator逐字节核对，框架作者内容职责没有因回填扩大，WP03/07/08等为明列交界。 |
| FR-000403 | PASS | PASS / active | 真实git show 908的§5.2已删特定提示承诺；父范围继续排除地图/动画子节，保留编译写回、反写、缓存及失败前缀，历史source保持。 |
| FR-000404 | PASS | PASS / active | 独立地图事件转换粗标保持MZ/框架双方，源门为已登记地图及实际修改；用户XP迁移范围仍待决策，U02接受没有给目标批准。 |
| FR-000405 | PASS | PASS / active | 动画映射仍单列MZ接入与框架数据，零/有效条目写入门和缓存边界保持；新引用没有把静态有效条目升级成播放验证。 |
| FR-000406 | PASS | PASS / active | 启动与直接编译的部分状态和失败前缀已重读；框架编排持有本行，实际事件/动画及诊断由明确源合同消费，未重复实现。 |
| FR-000407 | FAIL | FAIL / retired | 转元数据方向正确、完整旧行保真，但META-000021没有关联首项本地化主责和具名世界/内容编辑器、呈现消费者；仅近邻编译与音频/动画编辑入口不足。 |
| FR-000408 | PASS | PASS / active | 默认编译触发、主动导出和未证组合仍为本篇配置投影；U02状态回填不代表其它批接受或目标实现。 |
| FR-000409 | PASS | PASS / active | 完整通知/处理器表、条件/精确登记和中断前缀重读；框架维护扩展规则合理，具体业务不被本行重做。 |
| FR-000410 | PASS | PASS / active | 可扩展菜单行只承担注册/排序/过滤/分派；页面业务按原§4归UI，新增共同引用没有把业务菜单归入本行。 |
| FR-000411 | PASS | PASS / active | 插件元数据、循环/冲突、逐字符版本比较与注册终止门完整重读；框架扩展合同合理，源目录空并未被当作无插件支持。 |
| FR-000412 | PASS | PASS / active | 发现、编译和预编译消费各前提完整保留；框架承接能力候选未指定Ruby组织或声称发布包运行验证。 |
| FR-000413 | FAIL | PASS / active | 源§7明确格式化/日志/控制台交WP07，现已补同名直接合同；异常传播与直接终止仍按入口区分。 |
| FR-000414 | PASS | PASS / active | 基线、强制编译、真实插件组合和产物读取未知保留；框架职责/待验证状态没有额外承诺。 |
| FR-000415 | FAIL | PASS / active | 逐字段旅行表已重读；初始化、生产事件和持久化是真行为，来源分类已改为未单列的统计附表，框架数据责任合理。 |
| FR-000416 | FAIL | PASS / active | 完整场地动作表及WP59§5.3.1已读，新增直接锚点和FR374准确提供严格预检后增计数、失败不回退的生产门；分类修复适用。 |
| FR-000417 | FAIL | PASS / active | 道具/钓鱼/雷达/树果九字段表完整重读；框架持久统计与原证据等级区分，源分类不再虚构导航；未宣称事件全部可达。 |
| FR-000418 | FAIL | PASS / active | NPC三字段仍仅机制登记，更新可达性缺材料保留U01；新分类忠实，框架统计状态没有制造NPC事件实现。 |
| FR-000419 | FAIL | PASS / active | 个体/孵化/进化/交换等十一统计字段已重读，含交换先增后验失败；框架维护持久计数，领域生产按责任表限定，不改真实业务规则。 |
| FR-000420 | FAIL | FAIL / active | WP42/WP38补回结果/经验/金钱与失败球，但Mega统计真实生产为WP22§4.3 L58–60的玩家本人门及先增后变形；本行仍没有WP22直接/功能引用，生产合同未补全。 |
| FR-000421 | FAIL | PASS / active | 货币十一字段表保留实际增额、件数、缺事件和battle_points_won来源待查；新分类/框架统计职责不把待查来源变已知。 |
| FR-000422 | FAIL | PASS / active | 特殊九字段表保留数组/默认、可调用赋值机制和调用者未证两层；仍是框架统计合同，未因Demo缺材料删除行为。 |
| FR-000423 | FAIL | PASS / active | 保存/会话/最近保存时间三字段，现补WP09和WP10当前持久及旧帧数迁移真实合同；与临时锚点分离。 |
| FR-000424 | FAIL | PASS / active | 派生查询及临时游戏时间锚点有真实读写副作用，仍非74个声明字段；不因来源分类修正把它删为纯目录。 |
| FR-000425 | FAIL | PASS / active | 时间四来源、现实/帧消费者及变量计时全节已重读；WP09持久、WP13事件冷却/等待与WP59墙钟作为不同输入/消费者合同，直接引用准确且未统一成离线推进。 |
| FR-000426 | FAIL | PASS / active | 完整计步/统计节和WP12移动完成表已核，WP05有序通知、WP12守卫/零位移完成、WP09保存边界已连接；没有从距离未增推全局步数未变。 |
| FR-000427 | FAIL | PASS / active | 父当前范围精确扣除§5.3并指FR745，保留普通随机、地牢/彩票种子和有状态选择；不再把录像序列吞作统一内核随机。 |
| FR-000428 | FAIL | PASS / active | 已补WP09和WP14；完整地牢种子消费节确认保存待播状态、生成即清和全局随机副作用/失败前缀，新增reason指向真实合同。 |
| FR-000429 | PASS | PASS / active | 默认随机/时间与未证组合依旧是粗标配置投影；重读§7及§5.3，录像主责已另列FR745，本行未声称统一随机或兼容已证。 |
| FR-000430 | FAIL | PASS / active | 直接告警全节及依赖已重读，新增WP08对应本地化，WP07对应控制台输出，参数与输出通道分开。 |
| FR-000431 | PASS | PASS / active | 弃用别名参数校验、先告警后转发和块回调限制已重读；框架兼容行为粗标合理，新增WP07/08共同合同不改变原返回前提。 |
| FR-000432 | PASS | PASS / active | 边界/不变量已重读；框架保留创建失败与使用期顺序，控制台呈现仍由WP07/MZ边界承担。 |
| FR-000433 | PASS | PASS / active | 完整文件/归档内存流、路径、小端协议混合表已重读；框架I/O候选正确，宿主读取与具体资源播放没有被冒认已支持。 |
| FR-000434 | PASS | PASS / active | 完整HTTP分层及请求前构造表已读；框架拥有协议和捕获边界，历史隔离替身没有被升级为联网/宿主兼容。 |
| FR-000435 | FAIL | PASS / active | 框架现在明确负责格式化、日志失败前缀和0/1控制流，MZ负责窗口/复制/控制台/重启消费；FR446/451/625/628为具体保存/恢复/UI交界，整节不再仅标MZ。 |
| FR-000436 | FAIL | FAIL / active | WP04/05/09/10路径虽存在，但新增四条specific reason分别谈本地化提取、消息集合、语言选项和语言状态，与源§6实际编译错误/插件终止/主流程超时紧急保存不符；不可把有链接当正确职责。 |
| FR-000437 | PASS | PASS / active | 诊断配置/模式限制已重读；错误头、内部版回溯与宿主未知没有升级成全模式保证，框架粗标保留合理。 |
| FR-000438 | PASS | PASS / active | 31文本域、键规范化和地图桶已重新读，框架文本身份服务责任合理；与具体UI表现分开。 |
| FR-000439 | FAIL | PASS / active | 完整语言配置/选择源节及WP65对应节核对：框架拥有候选/当前语言/消息载入及入口直写，MZ菜单交付选择，现已关联FR444/446/642/644。 |
| FR-000440 | PASS | PASS / active | 历史完整查找/回退、占位及指定图像身份源信用适用，未改源/范围/去向；新通用框架职责仍只文本身份选择，实际加载/呈现仍属已明确资源消费者。 |
| FR-000441 | PASS | PASS / active | 作者收集/提取/导入/部分写入全源节未改，旧完整阅读信用保留；新依赖是编译/保存/config共同交界，没有擅加具体UI或目标执行资格。 |
| FR-000442 | PASS | PASS / active | 默认语言及延迟构造/多语言工作流已读；未把无候选变成未来排除，新待验证状态保持。 |
| FR-000443 | PASS | PASS / active | 完整边界节保留空译、格式异常、覆盖删除及缺地图可达性；框架文本失败合同与UI实际结果分离。 |
| FR-000444 | PASS | PASS / active | 17持久登记、动态重复身份及槽存取源与范围未变；旧完整信用保留，框架持久状态主责适合，新增WP06/07/08/10属来源明列合同。 |
| FR-000445 | FAIL | PASS / active | 源启动混合表与WP11完整恢复节、WP65载入节已读；框架持装载/保留/重建条件，MZ供标题/选图/取消/地图通知，FR324/326/451/642具体交接已列。 |
| FR-000446 | PASS | PASS / active | 保存成功/失败与三直写路径已重读；框架持久状态与I/O提交，已改恢复主行负责UI，未因U01仍待整改伪称保存实现。 |
| FR-000447 | PASS | PASS / active | 默认启动与保存配置已读；新合同引用不改变设置/进度/版本事实，阶段未批准和上游pending保持。 |
| FR-000448 | FAIL | PASS / active | 源§7及WP10完整失败恢复已核，补WP10载入/备份/删除/转换写回真实合同；错型与I/O失败保持不同。 |
| FR-000449 | FAIL | PASS / active | 完整转换机制及WP05版本比较已读；新增范围门明确支持哪些旧数组/表、版本/身份由用户决定，通用编排和具体兼容分开验收。 |
| FR-000450 | FAIL | PASS / active | 完整14项转换目录、64树果/4敷料/旧槽表已重新读；待决策与DEC-SPECIAL-AND-HOST-SCOPE及具体旧版本问题完整绑定，没有自动排除。 |
| FR-000451 | FAIL | PASS / active | 完整恢复混合表已读，框架持有效性/备份/删除/保存及异常前缀，MZ持询问、拒绝退出、清场景/条件恢复与缺图输入；FR326/435/445/642与源相符。 |
| FR-000452 | PASS | PASS / active | 默认备份/紧急保存/单对象入口不等同具体旧格式承诺；449/450范围门传播已核，新框架候选仍待用户/验证。 |
| FR-000453 | PASS | PASS / active | 备份同路径、转换失败前缀、寄养/电话缺陷已重读；框架候选不把参考缺陷当未来已批准政策。 |
| FR-000745 | 新增 | PASS / active | §5.3是录像协作边界，框架保存初态/命令/随机/换人及版本，Showdown按实际域消费已录序列；链接FR132–136提供固定版本/格式、序列、回放/中止与清理合同，普通随机父范围已精确扣除。按章节边界行理解，不另宣称独立新业务能力。 |

全部退役、3 metadata记录及86元数据章节另有逐单元定位/消费者/非功能处理结果；未执行静态向量仍为NOT_EXECUTED。机械脚本kernel-check.py真实exit0，完整Git读取argv/exit/输出身份在kernel-command.json，覆盖与逐行身份在kernel-mechanical.json。早期结构探索曾因path/document字段假设出现只读KeyError，未用于任何PASS信用；后续按真实结构补核。

剩余：修正两组metadata/依赖问题后冻结新候选复核；目标原型、用户范围决定、其它上游批次和最终累计接受门继续保留。
