# R8 资源、序列化与二进制有限静态审查

本任务交付状态为 **PARTIAL_REVIEW_PENDING_INDEPENDENT_RECEPTION**，`UPDATE_NOT_STARTED`。已读的有限程序体和已核对的命名条款中没有形成 `GR8-RES-*` 必须修订提案；这不构成资源全域 `NO_REQUIRED_UPDATE`，更不构成本轮全局接受。未读材料、未接收消费者与独立反证仍有明确余量。

受审身份始终为 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe` / tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`、R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。后继报告提交不改变该绑定。预检与配置、refs/worktree、保护库存、技能替代路径及历史恢复资格见 `preflight-report.md`；请求模型/effort/tier/speed 的实际逐字段回显均为 `UNVERIFIED`。

## 本轮新读的有限材料

| 材料 | 完整新读单位 | 资格边界 |
| --- | --- | --- |
| animmaker.exe | 全15方法、743 CIL指令、1670 CIL bytes、11 EH；元数据及程序集依赖 | `FULL_READ_FINITE_PROGRAM_BODY`；.NET外部库效果未执行 |
| extendtext.exe | 全1740 bytes有限.text控制流、17导入及窗口/互斥/控件字面量；callback按0x40129c正确对齐 | `FULL_READ_FINITE_PROGRAM_BODY`；原生Win32程序，无CLR/IL |
| Game.exe shader候选 | 全66单元、35544 bytes、1337行；55完整main正文、5prelude、6误命中 | `FULL_READ_LITERAL_UNITS`；native构造/选择/供参/GPU像素未知 |
| Ruby DLL C候选 | 全650单元、30064 bytes、751行；646条件生成片段、4字符表/标点误命中 | `FULL_READ_LITERAL_UNITS`；不构成完整generator或Ruby运行时控制流 |
| Game.exe 三兼容程序 | Ace968行、VX1004行、XP1476行，合计3448行 | 全三份字面程序；配置互斥，native选择与反序列化值未知 |
| Scripts.rxdata | 594 bytes全惰性解析；唯一Main正文49行全文 | 没有实例化Marshal类/回调或求值Ruby；原生boot未知 |
| 两根脚本工具、配置、文档、区域地图工具 | scripts_extract/combine各183行、mkxp.json全部、animmaker/extendtext文档全文、townmapgen414行 | 只读代码/声明/DOM请求；没有执行其业务 |
| knownpoint/selpoint BMP | 两头部与全部128像素 | 全有限结构；没有浏览器或图像输出观察 |

`current-programs-v2/inventory.json` 为720个当前字节绑定单元及偏移/SHA导航；它不是全二进制可读字符串的完备证明。历史定位器只用于导航，每个提取单元重新核对当前R字节。前一次locator缺SHA失败及partial目录保持，不以v2成功擦除失败。随后对5 PE全部当前字节独立扫描5条明确ASCII marker规则，得到315候选，248包含在已读单元，67另行全部新读：13条额外条件C生成片段、53条诊断/metadata非程序、1条已读shader尾接字符。因此本任务完整新读的C片段至少659条；有限规则集合已接收，不外推Unicode/UTF16、压缩、其他语法或全二进制发现完备。详见 `current-literal-discovery.json` / `literal-discovery-reception.json`。

`native-region-denominator.json` 对5 PE、合计24,636,234 bytes提供无缝字节分区、全部section与导入库计数；分区SHA及当前对象身份均校验。该分母是结构分母，不能换算为语义百分比。Game的733、Ruby DLL的331、zlib的50个导入只表明静态名字边界；不证明对应函数行为。其他native控制流、exports/debug符号/资源子树的语义未完整新读。

## 实际消费者与双向核对

当前新读消费者包括 RPG_Sprite、RPG_Cache、MessageConfig、AnimatedBitmap、Game_Screen、Game_System、Spriteset_Global、Sprite_AnimationSprite、Weather登记及Overworld_Weather、Main、FileTests与Audio时长入口。各文件确切行数和源身份见 `reading-ledger.json` / `source-identities.json`。这些是完整文件新读，但不自动证明所有下游调用链闭合；动态插件、宿主native和未知反序列化字段不从旧兼容构造默认值推出。

`forward-map.json` 保存751条有限source事实或字面片段分类，包含本轮读者、源位置、消费者、前提、formal入口及NOT_EXECUTED。`reverse-map.json` 有42个命名section/vector绑定；明确不是全部formal逐条款映射。其指向的WP15/WP16已全文阅读；WP74 §18及WP75 §12–§14、对应AN/EXT/CV向量完整读取。其余条款和其他任务主责消费者不由本任务代接收。

完整CIL支持WP74 §18的条件输入、XML先全解析、保序五列192格、缺路径跳过仍占原槽、零值与异常类型分列、顺序Save及前缀失败边界。没有把图像/XML库与文件请求升级为实际结果。

完整extendtext程序支持WP75 §14的精确目标、独立四分支、首EDIT、Batch两个按钮独立请求、忽略返回、marker/mutex门、Sleep150请求及退出不恢复。解释器只有诊断建议，未证明自动启动工具；实际几何、进程归属和周期未知。

Archive/Main与两工具支持WP75 §12的方向不同的数量门、先本层文件再子目录、排序/递归、文件名归一和阶段失败前缀。Main压缩身份区分Marshal字符串节点[25,590)与真实压缩payload[29,590)共561 bytes，解压1197 bytes/49行；详见 `current-serialized/Main.identity.json`。

三兼容程序的Cache/Sprite/Weather/Audio有不同旧定义，不能合成一份当前默认规则；当前源码重开定义和消费者需逐项接收。R6 `GR6-POL-001`的未选择兼容政策已经重新全文阅读，未将旧数据类型作为新必须需求。Shader公式只获得字面条件事实，现有WP16高层渲染条款不由未证native选择反推完整GPU算法需求。

`findings.json` 记录8组有限无差异观察及各自前提，独立反证全部仍为 `PENDING`。没有把本任务自己的再次核对写成独立非提案者接受。

## 完整结构解析而非语义全文

下列数据均可读，不能记为opaque或宿主limit来掩盖未读：

| 材料 | 当前完成分母 | 本任务未取得的资格 |
| --- | --- | --- |
| controller表 | 442647 bytes、1666记录、790完整字段模式，2个xinput特殊身份 | 所有记录语义接收；宿主激活与物理输入另未知 |
| 有限可打印候选库存 | 258727 ASCII min4、1434 UTF16LE-ASCII子集min4，共260161候选 | 255158候选尚未逐项接收；含可打印机器码/随机候选，不能自动称真实字符串，须继续分类 |
| 8字体 | 104 tables、2326 glyphs、60954 points全机械解析 | 全字段/字形语义阅读；宿主发现、hinting、渲染另未知 |
| SF2 | 25786 hydra行、1524声部链接、2000710 PCM points全结构解析 | 全字段与样本语义接收；native loader/guard/合成另未知 |
| messages_core.dat | 31 rootslots、76 mapslots、85 hashes、10697 pairs全惰性解析 | 全key/body语义阅读、译文质量与native接收 |

结构文件已作为 `resource_media_serialized` 可恢复输入通知主会话，任务计划和实际完成严格区分。kernel任务已独立新读Intl定义及WP08，但没有授予messages记录语义信用。本任务不得用那个跨域定义读取代替全部key/body。

## 恢复、执行与剩余工作

`restore_selected.py` 从本地固定B8 gzip运输恢复125文件104487771 bytes；逐对象校验编码/解码SHA、长度及Git内容身份。恢复本身没有程序执行或语义阅读信用。R6 L01–L14全部原记录已重新阅读全文，且9aa历史对象与B8当前14319 bytes同字节；旧资格没有转成本轮FULL_READ或行为PASS。

本任务参考行为、独立行为模型、宿主/Demo、原生媒体及存档/回放执行均0。全部有限向量是 `NOT_EXECUTED`。静态工具/结构解析的真实stdout、stderr、exit、UTC见 `evidence/`；旧早期直接读取只有平台回显，未补造当时的本地捕获。主会话另有数值探索进程，不能把本任务0外推全轮。

按主会话要求，controller和有限字符串库存已冻结为后继独立新上下文输入：`handoff/readset-index.json` 及 `handoff/manifest.json` 提供精确文件/decoder SHA、五个字符串库存、恢复旧工具及候选consumer/formal身份；`handoff/controller-readset.json` 保留全部1678行的字节偏移/SHA/原文/有序字段；`handoff/next-context-prompt.md` 是完整可派发任务提示。平台分母实际为Windows731、Linux484、Android214、Mac OS X211、iOS26；不是只有Windows/Linux/Mac。现有literal/元数据接收与未读边界逐项列出，未把既有可得材料塞入L04。

有限库存最初提取实现逐候选反复构造路径，运行偏慢；本任务中断了自己的该静态提取进程。真实exit254、KeyboardInterrupt与不完整输出保留在 `evidence/current-controller-string-readset.*`、`handoff/failed-first-*`，未接受。优化为先分文件并经无重叠断言的区间查找，v2实际3.21秒、exit0，完整库存与旧controller解析逐字段相同。失败、中断、后继成功各自保留，没有业务执行或语义信用。

继续完成需要：controller所有记录和255158有限字符串候选的语义接收/真实类型处置；字体/SF2/messages语义接收；其他已定位PE exports/debug/resource等可恢复元数据新读；完整实际消费者/formal分母接收；独立非提案者反证。只把真正native CFG/selector/任意编码无界解码及宿主结果留在准确未知边界。本任务最终状态 `DELIVERED_WITH_OPEN_READ_ITEMS`，不是全域完成。本任务没有改动R、formal、planning/audit、历史报告、refs或其他任务目录，没有安装、提交或推送。最后固定formal tree、受保护路径差异及R干净状态见 `evidence/final-protection-records.json`，每条带真实分离输出、UTC和exit。
