# R8 去向打标 R3 最终累计独立复核

固定受审候选：`c0f62d973180679134f2eb1a488c1dc359c8658f`。

**分类修正 PASS；最终累计来源校准 FAIL；总体 FAIL。** 原R2七项问题全部修复，28行依赖及六行职责/依赖精化均通过。736行分类、职责、有效范围和依赖分别全部PASS；当前来源校准为729 PASS、7 FAIL。剩余仅两个P3根因：三行来源差分摘要归属错配，四行把EV单项越额混成总量越额。已接受的正式5f正文、九批回执及其身份没有因此被否定。

本报告只写新的独占review目录，不修改清单来取得PASS，不改正式规格、参考、旧报告或main。**最小修复集是七行当前差异说明及相应侧证据/补丁/生成视图**，无需新增ID、重新设计去向或启动新一轮全局规格审查。具体固定源、指针、反例和修复见[findings.json](findings.json)。

## 固定输入及审查资格

| 输入 | 固定SHA |
| --- | --- |
| R3候选 | `c0f62d973180679134f2eb1a488c1dc359c8658f` |
| R2候选 / 独立FAIL | `a32873d2860b15d9f5e27727db8f131f4ec433b6` / `0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add` |
| R1候选 / 独立FAIL | `5666b7b912e2fb79b5119283ee6a37401a7071db` / `8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8` |
| 初候选 / 独立FAIL | `d62b41f4d620e50bb04c80a7505374bd284d8210` / `a0352c7fba38391afc535525988245701d5ce202` |
| B8 / R8交付 | `fd1df570cad987dc3852a3b958f03916e317f7fe` / `4575e80d041ab0c74a42e2e36399d05791dbaa5b` |
| 当前累计源 | `5f87743293290de2e219ecdd6c19e88280f60c9a` |
| 完整累计包 | `8336249c78b4698cd77445653d3b05ff6a76ce94` |
| U04最终回执 / actual报告 | `a974eb133bdb280ac46f2684df4b309a18fc6cc1` / `40f428ef33d9b09ba9cc584ef4794779cc9869cb` |
| U02/U03回执 / actual报告 | `861f7a44a6f763c265a11761ab17a8ec3b55f304` / `548d6bb9a21d0967680445c013e66d9d5661d2d6` |
| 五批回执 / actual报告 | `e042c2f061eb2951a8d662a5987804e3314cb6b4` / `834888e29f939d0a5ed9478d763deb86eb021211` |
| U06回执 / actual报告 | `3157ef455fdac41f0bf5485b281ef2e1699c8599` / `8f71c18480a847348b8450c9df1e7e8194c03985` |

所有对象按精确SHA取得，含旧908比较对象，完整tree/正式tree见[evidence/fixed-objects.json](evidence/fixed-objects.json)。R2报告94文件、累计包11文件与候选159文件逐项核bytes/SHA256/Git blob及适用行数/模式；相对R2的91项非自身payload差分加两项明确自身身份排除，与实际93个变化路径完全相等，全部限routing目录。作者的身份和修复声明均只作被审输入。

当前5f正式树为`93dc967b4cdb653359afc123d3b8b318d6475fdd`；候选工作区正式树仍为B8的`f292698cdd4a8e725525a9be6dc34b75faaf151e`。所有current正文及定位从5f Git对象读取。参考HEAD为`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，只读且clean。旧R1/R2 FAIL及当时未应用/U04待办事实完整保留。

父委派的`gpt-6.1-sol / ultra / default / normal / Fast off`请求与admission可追溯；本环境没有权威实际runtime/model/effort/tier/speed/Fast/云UUID回显，各实际字段保持**UNVERIFIED**。这不是本次FAIL原因。工具广告priority或逻辑任务名不能证明实际default或云UUID。六个分工组成一份独立审查，不重复计接受票。详见[evidence/task-qualification.json](evidence/task-qualification.json)。

## 覆盖、阅读和继承

从正式索引及Git独立重算：131文档、87WP、历史2683/当前2704标题，新增21；736活跃、33完整退役、33元数据。五个primary归属为combat27、creature18、kernel13、demo/shared11、Pokémon/世界/UI62，合计131且无重复。全部721原ID、736active、33metadata、44原组、7项R2问题和12项R1残留逐项对齐，不是抽样。

[reading-coverage.json](reading-coverage.json)逐131篇连接历史/当前身份、实际新读区间、固定旧全文信用和不受影响依据；[section-results.json](section-results.json)逐2704标题保存层级、锚点、末行、身份、消费者及读取责任人。21新增标题按主文档归属为combat3、kernel5、Pokémon/世界/UI13；creature、demo与source的交叉消费者证据单列，不重复计标题。

五域分别完整读自己的累计变源差异和全部受影响有效单元/必要消费者；source分工独立完整新读38文件差异、21新增标题正文及39个消费者的完整当前有效范围。root另完整读六域报告、51条源差异摘要投影及六个争议完整有效单元，重算全部身份/章节/locator与补丁。未声称本轮重新全文阅读131篇，也未把JSON/AST解析、标题枚举、字节相等或运行静态工具当语义全文。

旧PASS只在对应有效源、职责、范围、依赖用途未改变且当前目标变化经核不影响后继承。字节相等只证明保全；708个旧active PASS中七条本轮新注记仍被判FAIL。全部当前出站依赖按实际有效scope复核，接受真实共享合同、具名排除对照和父→excluded_child_refs→子导航，不要求重复所有最小ID。错误incoming或消费者自身注记失败不倒扣目标功能。

| 裁定口径 | PASS | FAIL |
| --- | ---: | ---: |
| 原721个ID（含33退役） | 714 | 7 |
| 当前736 active总体/来源校准 | 729 | 7 |
| 分类、职责、范围、依赖四facet | 各736 | 0 |
| 33 metadata/完整退役处理 | 33 | 0 |
| R2七项问题 | 7 | 0 |
| R2失败28 active回查 | 28 | 0 |
| R2通过708 active传播 | 701 | 7 |
| R1十二项残留 | 12 | 0 |
| 44原组具体case与分类/依赖facet | 44 | 0 |
| 含新校准注记的扩大当前scope组 | 42 | 2 |

扩大scope中COMBAT-05、POK-S05因新注记FAIL；其原具体case与R2依赖修复仍PASS。其它领域新注记单列，不凭一个词或无关新问题自动重开全部旧组。逐组两层含义见[finding-results.json](finding-results.json)，逐行五facet见[feature-results.json](feature-results.json)。

## 原七项修复与六职责精化

| R2问题 | R3结论及完整核对 |
| --- | --- |
| COMBAT-R2-DEP-001 | PASS。61/66/69精确移除739错PP边，740持物交界及68/71真实PP对照保留；本域96边全部核真实用途。 |
| R2-CRE-DEP-001 | PASS。186/190退款落正常终局31，192白雾建立/期限落39；不再用32外层治疗或40交换清理替代。 |
| R2-CRE-DEP-002 | PASS。244礼物四层工具清263/265错族边，741奖金统计落420；742真实训练家共享编辑器及741→579→755保留。Creature55当前边与57旧边全部对齐。 |
| POK-WORLD-R2-DEP-001 | PASS。20行全部按真实源/目标修复，另清664→159/160/161、751/760→355五条同根边；世界动画365、天气366、地牢364、存储/过滤道具等替代有依据。本域329条当前feature边全部审查。 |
| SOURCE-R2-001 | PASS。旧回执不能授权同路径后继未接受字节；全部文档快照须等于全局快照，无active行的metadata文档也包含。 |
| SOURCE-R2-002 | PASS。current-only规范化及prospective完整schema/标题/消费者验证发生在四核心和输入归档写入之前。 |
| SOURCE-R2-003 | PASS。豁免仅限固定三治理文档/46精确标题，普通行为不能借ALL_FORMAL_FEATURES清空消费者。 |

六行源职责精化分别新读判断：645/647把final UI65 L152/L210与WP12独立跳跃/普通移动门、消息早退、新请求/已有请求和微更新区别接好；92保留原始类型候选、PP限定计算类型匹配、一次+14与普通User/0不消费；397保留15蛋群固定作者身份、基础/形态输入与WP18/33/34消费者分工；699/703明确七语言图像、实际高度、空译/加载入口和对象/随机/音效/财务前缀。类别不变没有替代这些判断。新增direct_ref均使用真实B8父锚点，current新增子锚点另列证据。

744训练家数据卡、735复制/正常教学排除对照、753诊断/语言、BoxLink经114→736→654及其它真实间接导航均保留。捕获、背包战斗道具、逃跑、战中成长继续为框架/Showdown/MZ协作候选；未执行原型不妨碍合理粗标，也不能冒称兼容或已实现。

## 两项剩余P3及最小完整修复集

错误只在新增当前来源摘要及其副本，实际5f正式正文、current locator和回执身份正确。以下指针均相对固定候选的`routing-manifest.json`。

| 根因 / 行 | 精确指针 | 实际当前事实与必要替换 |
| --- | --- | --- |
| R3-SOURCE-ATTRIBUTION-001 / 173 | `/features/161/differences/1` | WP26 §5 L138改为记录战斗收服存储空操作；回放另按WP58副本/实时依赖/正常终局及中止分层。当前却写Gift ESC命名。 |
| 同根 / 227 | `/features/215/differences/1` | WP36 §4.2 L132补负概率/负累加器、整数商向下取整且不钳零；当前却写B8 L143已有的Repel比较成员。 |
| 同根 / 596 | `/features/566/differences/1` | WP61 §3 L56补默认首非蛋（含濒死）与替代首可战成员；当前却写应属WP36的概率/取整语义。 |
| R3-EV-BOUNDARY-001 / 29 | `/features/28/differences/1` | WP42 L73引用正常模板HP255首项反向区间失败；“超总量→先单项门失败”概括不成立。 |
| 同根 / 32 | `/features/31/differences/1` | 本行真实新改动为WP42 L207复位行走动画/转向预锁；附带文件级EV摘要也须准确区分单项和总量。 |
| 同根 / 204 | `/features/192/differences/1` | WP30 L122新增普通非Shadow分配的HP单项负余量首失败；模板255/255总510，没有超总量。 |
| 同根 / 456 | `/features/433/differences/1` | WP19 L174/L178明确HP/ATK各255、总510；越的是单项252，先单项夹限失败而未到总量夹限。 |

可区分的静态反例：Repel活动时首非蛋濒死L50、下一健康L10、野生L20，默认与替代比较结论不同；概率取整不能校准该修订。累加器−1的floor(−1/200)=−1区别于截成0。记录战斗的存储空操作不证明回放隔离或统一空操作。

EV方面，255＋255＝510满足总量上限但越单项252；相反HP/ATK/DEF/SPA/SPD各100、速度20总520，各单项均在额度内，首先处理HP时单项余量152非负，随后总量余量−10才非法。故“总量越额”不能推出“首单项门失败”。这些是按固定源规则作的静态区分，未执行业务向量/分配器。

最小完整修复要求：

1. 只替换上述七行`differences`的错误事实/差分归属，保留正确职责、范围、依赖、来源、阶段及未验证状态。
2. 同步相应`feature-source-deltas`的源事实/未来边界重估、`source-file-reassessment`的事实/分责摘要、统一`source-refinement-patch`的对应after值及当前派生视图。每个具体侧证据指针在[findings.json](findings.json)中，七case合并成两根，不重复计分工票。可复用生成输入仍包含这些摘要时同时纠正其对应值；不要解除历史writer的固定输入保护强行重跑。
3. 保留真实35175接受后归档和原应用回执，以更新的显式after值重建最终manifest；重新生成受影响resolution/facet/身份/摘要与静态I/O，冻结后继SHA，对这组有界校准修正再独立复核。正式5f、九批回执、R1/R2 FAIL及其它已核通过区域保留。

这是当前新注记的正确性问题，不要求原型、用户范围决定或新的游戏功能；也不要求重开全部正式规格。

## 累计来源、标题与保全证据

独立核九真实ACCEPTED回执和39项状态链：29 required＋10 selected optional，CLOSED0。40目标贡献逐原commit/blob/SHA/bytes相符，含38正式变源文件、共享UI65历史贡献及U07非正式overlay；六份旧计划外正式扩展文档已纳入接收，未因原计划缺写集而漏绑定。

131current身份及736locator从5f独立核，所有历史source/ID不变、当前范围无重叠；51个直接变源有效单元独立重算。230绑定全部回填、pending0/partial0，原191义务保留；39新绑定与47新增或扩展分别重算。**零pending说明回执绑定覆盖完成，不消去七条新增摘要错误。**

UI65的U01旧目标与final不同是历史贡献，不冒领最后两行；final U04真实回执匹配5f的L152/L210修复。较早actual的GR8-WORLD-003 FAIL保留，真正后继40f428才对final给PASS，不改写历史。

全部2704标题的标题行/层级/锚点/范围/末行/消费者引用从Git重算一致，21新增标题全部按final正文及真实消费者重估，含原10pending-U04标题。21条标题字符串hash与原Markdown整行hash分别按声明核，不混为漂移。当前131行可读覆盖及全部736行/33metadata视图、36父/39子/39边链接独立投影通过。目录与治理/字段表可聚合，不伪造实现功能。

33完整退役体剥去retirement后逐字段等于初d62，33metadata与R2完整对象相等，replacement/coverage/当前消费者导航同步。历史2683覆盖原字节保留，58份R1/R2作者历史文件原字节保留。精确35175归档＋78行/162字段before/after可重建**完整对象和最终序列化字节**，manifest SHA为`ee46bb7278bb21311115a62e93bd93770a205dc691a01a48f45c22b6c09b4f71`；重建通过仍不证明摘要语义正确。见[evidence/patch-reconstruction.json](evidence/patch-reconstruction.json)。

## 静态执行与保护

独立干净shared clone中按候选原字节重放`run-author-checks.py --phase cumulative-source`：10命令全exit0，17登记输入hash稳定且等于候选。27结构负例、9自检、2导航负例、11生成一致、19保全、5接受绑定负例、2704覆盖/4负例、4来源门夹具通过；另重放最终15项校准proof。干净fixture避免审查untracked文件被保全器误当作者变更，没有弱化检查或修改候选。

source分工另有七项实际Git/schema/apply负例：陈旧WP04回执在R2放过/R3拒绝；纯metadata文档旧快照两版均拒绝、同步后未接受新字节R2放过/R3拒绝；第2704节注入null在四核心及全部归档写入前拒绝；普通空映射/治理正文变化拒绝，真实2704及46豁免有效。真实argv/stdout/stderr/exit/UTC、前后hash、输入身份和负例均保存，不只依据作者十命令结果。

首次累计apply确用归档旧代码并已写入，随后完整current检查发现1776个null类型错误及陈旧可读覆盖。后继仅current规范化1776项、增prospective门是后来修复；原失败I/O、代码gzip及修后证据分别核对，不倒填首次已有门。R2当时七命令/后继未执行事实也未回写。

输出格式检查151条提示均来自原样保留的读取证据：148个Git patch空白上下文、两行回执读取标签尾空格、一个readset末尾空行；逐项验证后保留冻结字节，报告/JSON/代码检查通过，见[evidence/output-whitespace-check.json](evidence/output-whitespace-check.json)。

审查自身的路径排除字典、扩大组scope及各分工的元数据/格式/探针构造假设错误均留证后纠正，未改候选求通过。被截断输出未计未打印语义信用。仅静态Markdown/JSON/Python/Git；Ruby、参考游戏、业务场景、宿主、Showdown/框架原型运行0。

[evidence/protection-final-precommit.json](evidence/protection-final-precommit.json)记录正式diff空、参考clean及main/作者/R2报告远端引用。输出字节由`output-file-manifest.json`绑定，首次报告提交的全新无alternates远端逐文件回读保存在`publication-proof.json`；最终提交另再fresh回读并在交接给出精确SHA，不制造自身未来hash证明循环。

全部去向仍待验证、阶段待定/未批准、未实现/未验收；框架307、Showdown74、协作130、MZ225、排除0。四协作原型、固定目标版本、用户范围/首版细项与全轮CLOSED仍为独立待办，未被静态通过代替，也未被拿来否决合理粗标。当前有界结论为：**分类修正PASS，最终累计校准FAIL，修七行摘要后再固定候选复核。**
