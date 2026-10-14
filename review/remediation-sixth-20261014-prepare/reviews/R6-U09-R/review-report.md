# R6-U09-R 独立非作者复审

裁决：**PASS**，仅批准下列精确冻结候选的三项合同范围内静态修订。R6-DX-COMP-001、002、003 分别 PASS；没有必修返工。此裁决不是整合后 PASS、正式接受或 CLOSED，也不是参考行为执行证明。

## 1. 身份与阅读范围

| 对象 | 精确绑定 |
| --- | --- |
| 仓库 | y805939188/pokemon-essentials-clean-room |
| 准备基准 | 469a268b92daed7b4d28d7fd0da75520cbb7228f |
| 作者发布 commit | c3044166390b3d8c36f4cd121bb8619060b58bfe |
| 作者 workspace tree | 7c51331ffff17fad2de47024591ac2397a7a5196 |
| R6-U09 candidate tree | a5655aa6cbd68d2829f85691cc8fc1faf6adda70 |
| mirror tree | 77ef423806d8f8c6fcd97dd065fd2e89e82d3261 |
| evidence tree | 6b9a675a556573c3a24ef87af6424205e28dcd17 |
| 正式 main 基准 | 8ea169fbd0f33f378b5d732fd6bea59e854e04a6 |
| 正式规格 subtree | 1046fbb657882e84b3dfc6d017943a9edf7782e5 |
| 固定参考 R / repository tree | 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b / 7589c800b61ba13a13040ed0d686979b80a84fd0 |
| 作者分支 | codex/remediation-sixth-r6-u09-author-20261014 |
| 审者分支 | codex/remediation-sixth-r6-u09-review-20261014 |

完整提示词 `prompts/R6-U09-R.md` 的 226189 bytes、SHA256 `5e041f81d5b34505e8d4b8656a8f93f92b5478c52b794a8f75aa9a1cb12d12cd`、blob `1481887f8a75707a0591fbcadb05d6e39f0e7162` 均吻合。提示词逐段读完，内嵌 JSON 与完整 `contracts/R6-U09.json` 的原始字节完全相同；合同 113246 bytes、SHA256 `e03df62db8b457f3582d9170d625941f2bdef887a15dd4c623c6fc9098eedc20`、blob `eda7f39c10f6d651f16742a30beaff3dbc378e3c`。文中准备、候选和 inputs 的相对路径前缀均为 `review/remediation-sixth-20261014-prepare/`。

已全文读取适用根 AGENTS.md，没有发现本读写范围内更近的 AGENTS。此次只写本报告目录。七份相关正式全文（WP04、WP62、WP72、WP74、WP75、内核目录、DX 目录）及只读消费者 WP73-A 全文均已读；完整 300 行候选差异已读，并独立重算补丁一致性（46773 bytes，SHA256 `73257e34bd738bca3024187c17947efd7ea36472dc8b1b754d3987c3d9f2e3df`）。候选改动与这些全文交叉评估，不以摘要或命中替代全文。镜像的实际新增重点段和全部 KL37–50、DXCOMP-C01–08 也直接读过。

逐 ID 原提案、原裁决、反证和验收来自完整冻结合同；原 `inputs/evidence/tasks/R6-DX/debug/counter-B-compiler.json` 1–1075 全文及其调用检索原文另读。作者 `finding-responses.json` 1–2500、author-report、输入绑定、补充读集和历史绑定均完整审阅。共同证据中不属于这三项的动画编辑器等大范围材料不获得本审签名。

固定参考对象由审者新建的只读 bare 缓存重新获取；没有借用作者缺失的本地源缓存。001_Compiler（1117 行）、002_Compiler_CompilePBS（1321）、003_Compiler_WritePBS（821）、MiscPBSData（64）、StartGame（126）、999_Main（60）完整阅读。004_Compiler_MapsAndEvents 只签署已读的导入、MapData 及主驱动上下文（1–87、280–410、1670–1751）；没有声称读完其全部 1751 行。调试分派、菜单、区域编辑器、区域查询、连接缓存、播放消费者及 MenuHandlers 则按 [reading-ledger.jsonl](reading-ledger.jsonl) 的完整相关方法范围读取。所有十二份作者声明的参考输入和八份正式输入的真实字节、SHA256、blob、mode、tree 已独立核对，见 [identity-manifest.json](identity-manifest.json)。正式输入的 tree 是正式 subtree；其 whole-repository tree 是 `6ab3429170d2762607fbc2237014c3a160449fa1`，两者不能混用。

审者逻辑身份 R6-U09-R、当前直接审查 agent `/root`，不是作者 R6-U09-A。另一个只读 identity_audit agent 仅核对对象、补丁和包载荷，不参与语义裁决、不写本仓库。各 ID 的源/规范反证和最终 PASS 由当前审者直接完成。

## 2. R6-DX-COMP-001：required / P2 / PASS

### 身份及范围

此项是运行中 Compile data 入口覆盖缺口；原 WP04 已限定的启动合同本身没有被认定错误。不把旧启动清理复制到另一入口，不授未来永久缺陷兼容。

### 双向证据

固定 R 的 `Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb:1335–1344` 直接调用全量内容阶段，完成提示和消息窗释放位于正常返回之后。`001_Debug_Menus.rb:69–146` 与 `Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb:80–123` 的实际分派不增加局部 rescue/ensure 或缓存清理。`Data/Scripts/021_Compiler/001_Compiler.rb:993–1037` 依序发现/兼容改写、PBS、动画、已登记地图/公共事件、文本、消息保存/载入；`1039–1115` 才是启动调试检查、缺目录前缀、导入、mtime、清单预删除与异常转换。`Data/Scripts/999_Main/999_Main.rb:26–38` 绑定插件→启动检查→Game.initialize 的实际入口。

`002_Compiler_CompilePBS.rb:4–68、206–231` 证明先清当前表、逐节校验后登记、全部完成后终检/保存，Status/Power40 在当前招式登记前拒绝。`004_Compiler_MapsAndEvents.rb:45–83、293–318、1683–1751` 证明启动导入与只遍历 MapInfos 登记编号的内容驱动有不同门，999 排除保持。

反向对应候选 WP04 §2、§3.2/新 §3.3（40–55）、§5.1/5.3、§6/9；WP75 §3.1（35–44）、§4（56–62）、§16第1条；WP72 §8.3 Compile data 行（265）；内核 KL02/03 与 KL37–39；DX C01–C03（335–337）。每个新断言都回到上述实际入口/生产者/消费者，所有声明的五份同步文件都有落点。

### 前提、正常对照与反例

完整兼容工程、默认调试菜单可达、PBS 存在、旧 dat 有效、无覆写；兼容改写和 town/connection/types/abilities 等前段均正常，唯一新招式词法合法、Type 已定义、Status/Power40 且其余字段合法。直接入口在招式校验失败时：前段文件可新，当前 Move 表已清并可有新登记前缀，坏条目未登记，最终 Move 保存未到，旧 moves.dat 保留。没有启动预删/诊断清理/异常转换，也不保证其后的完成提示或窗口释放。这不是原子回滚，也不是所有 dat 未变。

尝试反驳“直接入口仍间接经过启动检查”：新固定 R 的整个 Data/Scripts 字面调用清单只找到菜单直接调用、启动内部调用及主入口；结合完整内容阶段和真实分派排除此有限默认路径反驳。此检索不能排除动态扩展、反射或原生外部覆写。全合法、所有依赖/I/O/消息正常的正常例可按顺序到完成收尾；Map007 未登记的独立同态例则直接入口不补登记，启动检查可导入，999 另作排除对照。

### 最小修订与保留

候选已完成原合同要求的入口区分、局部失败前缀与五文件同步，**没有剩余必修修订**。原异常表、整数 mtime/≥、拒绝启动提示不否决自动条件、缺目录清单前失败、Reset/SystemExit 原样抛、删除仅尝试全部保留。新增诊断必须正常返回才继续清理的前提准确；不假定诊断本身成功。

### 验收与历史回归

KL37/C01：上述失败前缀成立；KL38/C02：新地图导入门成立；KL39/C03：全合法直接入口的正常收尾成立，三组均 SOURCE_STATIC 支持的 DERIVED_VECTOR，全部 NOT_EXECUTED。KL01–36 原结果保留，只有 KL02/03 输入显式限定启动（KL02 增诊断正常返回）。WP75 §3.2–3.3 及 §5–15 原字节保留，包含 B20-C024、事件条件/自开关、六族/门/数量守卫/脚本往返；不能扩大为整模块旧验收重签。

### 独立裁决

原非提出者反证的 NOT_REFUTED_SCOPED_COVERAGE_GAP 与本次直接回源一致；没有把原全局 PENDING 或作者 198 项静态工具检查当成新 PASS。裁定该冻结候选 PASS，执行状态 NOT_EXECUTED。

### 依赖及接收

无作者阻塞依赖、无非阻塞领域依赖。必须由 R6-I 接收 U09 与 U06 的 WP75/DX 目录、U08 的 WP72/DX 目录、U14 的 WP04/内核目录差异，再审整合全文；本审未写实际正式文件。

## 3. R6-DX-COMP-002：required / P2 / PASS

### 身份及范围

仅补已预载缓存与新磁盘输出的分离，以及区域反写采用旧缓存的消费者后果。三个缓存族分别审，不提出统一广播刷新、全部缓存失效或理想行为。

### 双向证据

`002_Compiler_CompilePBS.rb:593–629` 使用局部区域列表写 regional_dexes.dat；`Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb:28–54` 优先返回已有区域、动画集合和关联缓存。`003_Compiler_WritePBS.rb:364–391、794–819` 单项/全量都使用区域 getter，取对象早于覆盖文件；`Data/Scripts/019_Utilities/001_Utilities.rb:389–418` 编号、成员、长度也消费同一 getter。编译写盘不等于更新这些对象。

`Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb:1099–1203` 的总保存 Yes 明确保存区域档案→清区域缓存→区域反写；No 不走该链，子页去空洞的已有副作用另外保留。`StartGame.rb:1–17` 重建 Game_Temp 是区域/动画的不同重读前提；`Data/Scripts/004_Game classes/005_Game_MapFactory.rb:383–491` 的类级连接/尺寸缓存与其 clear 独立，不由 Game_Temp 替换清空。

`002_Compiler_CompilePBS.rb:1274–1321` 从磁盘动画集合重建关联；出现有效 Move/OppMove 条目即写两份磁盘材料，零有效不写，不清预载对象。`Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb:429–506` 的播放查找及集合读取接合缓存消费者。菜单区域导出 `1346–1408` 与 Reload system cache `1488–1496` 是不同入口；后者只证明请求 System.reload_cache，不证明隐藏对象副作用。导入地图 `004:45–83` 仅清 MapInfos 缓存，不能推广到三族。

反向对应候选 WP04 新 §5.6（251–261）、§5.4 有效条目写入门；WP75 §3.1/§16第1条；WP74 §16（401–423）；WP62 §5.1（95–106）；KL40–45（81–86）；DX C04–C08（338–342）。WP73-A §5.3 总保存及 CE-M14/CE-M20 是必要只读对照，文件未改。所有六份同步文件均有落点。

### 前提、正常对照与反例

区域0先缓存 A=[BULBASAUR]，合法 PBS 改 B=[IVYSAUR]，两物种均已定义，直接全阶段/I/O 成功且无独立失效/会话重建/覆写：磁盘 B、查询 A（BULBASAUR 编号1、IVYSAUR 0、成员 A）。随后区域导出成功写 A 的内容，磁盘仍 B、缓存仍 A；不承诺恢复 A 原文件字节。覆盖写失败可留下截断/部分 PBS，不能回滚 B。缓存未建立时，编译后首次 getter 才加载 B；有效工作表 C 的编辑器 Yes 清缓存后反写 C，No 不走该链而不能推广为“所有 No 都无副作用”。

动画集合/关联 A 均预载，磁盘 B 有不同且有效的 TACKLE 关联，成功编译后磁盘更新而两缓存仍 A；播放查找可继续用旧对象，不签实际画面。零有效名称与旧磁盘映射 M 的对照不写新关联，是独立门。连接 A 预载、合法 B 编译成功且无连接清理时磁盘 B/查询 A；只重建 Game_Temp 仍 A，明确 clear 或新进程才有重载前提。

尝试用初始化、地图导入、编辑器保存、动画写入门、全局 pbClearData 和 Reload 反驳：它们各有独立门/对象或宿主边界。完整 MiscPBSData 的全局 clear 定义确实会清对象及连接；新调用清单没有将它接入直接 Compile data。完整 001–003 内容路径及 004 相关驱动/MapData 未补此链；不从字面搜索宣称无界动态/原生不存在。

### 最小修订与保留

原要求的区域反写链、三族缓存分离、显式正常刷新前提及六文件同步已完成，**没有剩余必修修订**。WP74 原 §1–14、命名/前缀、播放回退、AN-M29/30 零有效门和 §17 后全文保留；将 WP04 旧“有变化才保存”摘要准确接合为既有有效条目门，不引入所有动画均写/均清的承诺。WP62 §5.2 后解锁、展示、形态/记录写入与刷新参数保持。遭遇快照、21/0/70、指标输出路径、进化反写、电话身份/默认等其它旧合同未被替换。

### 验收与历史回归

KL40/C04 的连续区域链，KL41 与 C05 的冷缓存正常例，KL42/C05 的 Yes/No，KL43/C06 的动画对象对照，KL44/C07 的独立连接，KL45/C08 的零有效门逐一静态支持。不是六次或十一次行为执行；每组可分条件复位，连续观察按 KL40 前提。所有向量 NOT_EXECUTED。原 DX 目录完整 327 行逐字保留为候选前缀，未重签其中全部旧向量；WP73-A 全文读取只用于当前必要消费者及保留验证。

### 独立裁决

接受原非提出者 NOT_REFUTED_SCOPED 且 STARTUP_CONNECTION_CONTROL_NEEDS_NARROWING 的限定。本候选已明确同进程新 Game_Temp 不清连接，不再把其误作统一启动刷新。三个缓存族与零有效磁盘门各有准确前提，故 PASS。

### 依赖及接收

无作者阻塞/非阻塞领域依赖。R6-I 仍须接收 U07 的 WP74/DX、U01/U11 的 WP62，以及 U06/U08/U14 相关共享路径；必须审组合后完整文件与区域/动画/连接消费者，不以 U09 整文件镜像覆盖别批修订。

## 4. R6-DX-COMP-003：required / P3 / PASS

### 身份及范围

仅区分普通分节与专用预处理逐行的输入边界。不是所有 PBS 都拒绝缩进注释，也没有随附 PBS 语料受影响数量结论。

### 双向证据

固定 R `001_Compiler.rb:72–77、95–135` 的普通入口先按物理首列井号/纯空白过滤，再删除井号后缀和 trim；删除后为空没有第二次跳过，节内按非法属性语法拒绝，首节前则报缺少初始节。`232–249` 的专用逐行入口先预处理再略过空结果。`002_Compiler_CompilePBS.rb:791–862` 的实际 Trainer 入口使用该专用读取；`4–68` 给普通 A 节校验/登记与最终保存的接合顺序。

反向对应候选 WP04 §4.2（68–80）的边界表、A/B 前缀与原行内井号规则，§9 的场景接合，以及 KL46–50（87–91）。两份声明同步文件齐备。普通/q 文本先处理井号、引号不保护后缀、分词的位置相关标记规则保持。

### 前提、正常对照与反例

普通类型输入具有合法唯一 A/B 节与其余有效字段，无覆写、读取正常、无更早错误。A 完整后出现 B 节头，B 内放一个 ASCII 空格后接 `# note`：A 已被交付并校验登记；坏行预处理为空但不略过，B 尚未交给校验/登记，终检/整表保存未到，不回滚 A。外层磁盘删除和异常转换仍按 COMP-001 的入口前提，不推出全局 dat 未变。

相同材料改成首列 `# note` 或物理纯空白可略过；`Name = Alpha #Beta` 得 Alpha，无井号的 AlphaBeta 保持。坏行在首节前是缺初始节，而非节内非法属性。已定义类型/物种、有效 Pokemon 等其余字段的合法 Trainer 专用输入则略过同一缩进注释。

对“prep 后空文本会被普遍忽略”的反驳直接核对两个完整读取方法和真实 caller；只在专用家族成立。没有把标注 Unused 的旧 helper 作为当前控制，也没有将未知字段忽略、训练家垃圾行规则误套为普通分节非法属性接受。

### 最小修订与保留

原合同要求的物理列首/空白/行内/缩进边界、家族区别、首节前/节内状态前缀及测试已完成，**没有剩余必修修订**。KL07–10、KL33–36 旧行逐字保留。原 q 反写再读丢井号后缀、电话默认重复例外及联系人有效三元身份前提保持，不变成全解析器或永久缺陷兼容要求。

### 验收与历史回归

KL46 A/B 部分登记、KL47 首列/空白正常、KL48 行内/无井号、KL49 首节前、KL50 Trainer 专用正常均 SOURCE_STATIC 支持，NOT_EXECUTED。失败可达的是当前普通 parser 的指定前缀；不承诺文件系统错误结果或外层 UI。作者文件名 `history-hash-input-contract.json` 实际是 GR5-M01-002 消息默认哈希合同，全文核对后明确不把它当 PBS 井号验收证据。

### 独立裁决

原非提出者 NOT_REFUTED_SCOPED_COVERAGE_GAP 经本次直接回源成立；候选严格按两类输入门描述，不扩大 corpus/家族范围，裁定 PASS。

### 依赖及接收

无作者阻塞/非阻塞领域依赖。WP04 与内核目录同时有 U14 修订；R6-I 接收后须核对完整 parser/schema/浮点/专用输入接合，当前 PASS 不接受后续组合字节。

## 5. 历史资格、工具检查与执行限制

原 R1 只保留原 WP scope；R2 229 controls /21 batches /341 精确 owner 贡献；R3 23/76，M09 optional、历史 U08 not-started 和 M02 NO_REQUIRED 保持；R4 current 17/76 与 B5 16/75 区分。R5 的唯一 activation 所限定 92 CLOSED（51 P2/41 P3、OPEN0）是 inputs 的历史资格，不能覆盖当前整文件或宿主；optional7、NO_REQUIRED7、policy6、limits13 保持。当前 R6 required56/optional8/no-required1、独立 optional facet、policy7、limits14 未新增/重分类。L01–L14、历史 FAIL/MISMATCH/LF errata 不由本审关闭。

直接核对 `history-selected-bindings.json` 七条 GR5-M12-001–004/101–103 与固定 `13fddb0a217b36974c75657aa68da0caf104ee48` closure 对象的原记录完全一致。其“候选可关闭/等待 activation”等是旧对象自身状态，不能覆盖当前历史资格投影。GR5-M12-001–004 的完整具名验收/输入/失败/保留/原裁决字段另从原 task-packet 取出并逐项读，见 [history-contract-projection.json](history-contract-projection.json)。001 装载排序/短长错误；002 六族行门/整字段丢周围行/18夹具；003 门及独立转移配方；004 两布尔累计/新事件复位，均在已全文读取且未改的 WP75 §5–15 和原目录中保持。101–103 仅保留旧绑定及未改相关正文，不声称此次重做全部历史源或运行验收。

SC-U07-001 原纠正记录完整读并绑定，[history-erratum-binding.json](history-erratum-binding.json) 保留原 task-packet 的错误 LF 子主张以及纠正：六族捕获体不跨 LF，独立完整调用行和外围空白跨 LF 分开；U07-C02 原行及 WP75 六族限定未改。本审不签原错误句、不重开/删 GR5-M12-002，也不要求新增 Ruby 执行来保持字节未改的历史范围。

审者工具检查最终 **90 项 / 0 失败**，见 [verification-result.json](verification-result.json)、[verification-command.json](verification-command.json)。包括独立源/正式/候选身份、精确补丁、隔离路径、正式 subtree 未变、七条历史绑定、若干完整保留段和 KL01–36 原结果。检查器初次 tree 范围、扩展时 ID 零补位及 KL02/03 列索引错误均已纠正并留初次失败记录；这些不是候选行为失败。没有运行作者验证器，作者 198/0 只视为其工具载荷；两者都不是参考执行或行为验收计数。

本审执行计数：参考/隔离原函数 0；独立完整行为模型 0；原生宿主 0；Demo 0；真实存档 0；游戏生产服务 0。Git 获取、字节/JSON/结构校验是 TOOL_VALIDATION，阅读是 SOURCE_STATIC，向量结论是 DERIVED_VECTOR。发布用网络不算游戏服务执行。未验证：完整兼容宿主、实际文件失败、最外层错误界面、可见动画/音频、System.reload_cache 隐藏副作用、任意插件/覆写/动态调用。当前缺完整地图/System/Tilesets 等材料的 Demo 未执行；不得因未跑而新增本合同没有的 must-execute 要求。

请求配置 gpt-6.1-sol / ultra / default tier / default normal speed；实际 model、effort、tier、speed、平台 UUID 均 **UNVERIFIED**，未回显即未验证，没有开新 CLI 或探测配置/凭据。当前父 source thread 由用户绑定为 `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`；作者声称更新的 integrator thread `01a13a93-d1da-71e4-a488-63b8524f503d` 在本审用户指令中没有独立确认。本审接收方只签合同角色 R6-I，具体执行线程交由父方按真实授权绑定，不把作者元数据当平台 UUID。

初始读/checkout 的独立本地 UTC 未捕获，不补造。最早本地命令时间见 reference-init.json（14:44:12 UTC 左右）；读 ledger 开始于 `2026-10-14T14:45:02.717651+00:00`。早期提示词/合同和部分原反证阅读保存在平台工具输出，不伪造进后继 ledger。工具输出的相关截断均补读；两个错误 EditorScreens 路径读取 exit1 由正确路径范围补齐，执行服务短暂断连重试后恢复。详细限制见 [execution-limits.json](execution-limits.json)。

## 6. 非阻断观察与交付界限

内核目录候选第77行空行使 KL37–50 与上方表头分离，普通 GFM 渲染可能把新增行显示为管道文本。全部 ID、前提和预期仍明确存在，正文及 DX 表可相互导航；此为非阻断排版观察，不新增必修 ID/任务，不更改三项静态 PASS。最小可选改善为移除该空行或给新增块加同样表头。

所有七共享文件尚待 R6-I 实际整合、逐文件接收、直接/传递消费者与精确历史回归、整合全文非作者复审、正式接受及 CLOSED 登记。当前 review 只能解除这三个冻结候选的非作者候选审查门；没有操作 main、作者镜像、正式规格、公共台账或 Mac。

本报告及附属证据是有限 core；发布 commit/tree 与完整远端读回由独立 publication receipt 和最终回执绑定，不通过让文件包含自己的未来 hash 制造递归签名。
