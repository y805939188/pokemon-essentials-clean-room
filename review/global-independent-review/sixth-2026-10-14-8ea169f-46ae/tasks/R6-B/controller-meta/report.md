# R6-B controller / repository metadata / native interface subreview

状态：`COMPLETE_STATIC_SCOPE_WITH_LIMITS`。五份根元资料、三份原生 PE 接口结构范围和全部控制器数据语义已按下列口径审完；机器码与未选字符串的精确限制保留，没有把结构核对升级为行为。最终明细见 `task-status.json` 与 `controller-rows/report.md`。没有修改 formal、reference 或其它审查目录，没有启动 update，没有执行 exe、DLL、IL、参考 Ruby、行为模型、游戏宿主或 Demo。

固定身份：main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，workspace tree `6ab3429170d2762607fbc2237014c3a160449fa1`，formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`（131 文件），R commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。AGENTS.md 全文已读，源只读、行为规格独立、审查输出与正式规格分离。实际 model / effort / tier / speed / platform UUID 均未回显，全部 `UNVERIFIED`；没有查认证或配置。

## 1. 证据等级与分母

`binary-interface-audit.json` 是本轮新静态解析证据，不作为语义阅读、运行或宿主选择的替代。这里独立从原始三份 PE 字节重新解析全部区段/目录、1114 导入、3702 导出、27309 个非辅助 COFF 记录核心字段，并复核全部资源载荷哈希及全部 290 个已选字符串的原字节。`verify_pe.py` 为本任务新写且全文理解的只读解析工具；输入固定、输出限定在本目录。所有复核项与本轮 root 证据一致，结果见 `independent-pe-checks.json`。

全文语义阅读、完整结构核对、自动索引及未解析机器码分别登记；没有将扫描、JSON 解析、导出符号名或字节一致判为行为 PASS。

| 文件 | 区段 / 目录 | 导入组 / 条目 | 导出 | COFF 原始条目 / 非辅助 / 辅助 | 已选字面量 / 全候选 | 资源 / PE debug directory 记录 |
| --- | --- | --- | --- | --- | --- | --- |
| Game.exe | 12 / 16 | 17 / 733 | 824 | 0 / 0 / 0 | 284 / 161104 | 4 / 0 |
| x64-msvcrt-ruby310.dll | 21 / 16 | 9 / 331 | 2773 | 32411 / 27253 / 5158 | 6 / 97340 | 1 / 0 |
| zlib1.dll | 11 / 16 | 2 / 50 | 105 | 56 / 56 / 0 | 0 / 1471 | 0 / 0 |

三者均为 AMD64 / PE32+ 结构。它们存在于 R，但没有载入或执行。所有导入与导出名称已完整呈现阅读并分类；COFF 的全部核心字段属于结构核对，不是 27309 个机器码函数的语义审查。259915 个 printable 候选中只有已选 290 条在这里逐字阅读，未选 259625 条不是逐条语义 PASS；它们含符号、压缩字典/偶然可打印字节及普通诊断材料。可恢复脚本、shader、controller 数据是独立可读工作量，不藏在这项限制中。

逐结构/数据 forward 有 34219 行（32553 元资料/结构行加1666控制器行），使用本轮证据 JSON path 逐单元追溯，避免复制源表达式到规格。reverse 只签本子审实际读取的 WP17 输入交界、scope line151、WP75 README 文档接合与 L13，不转签整篇 WP17/WP75。控制器完整原始行矩阵另在 `controller-rows/`。

## 2. 根目录五份元资料全文处置

| 来源 | 全文范围 | 已读内容与用途 | consumer / 正式处置 |
| --- | --- | --- | --- |
| README.md | 1–42 | v21.1 基线、fork/clone 作者使用流程、散文件与归档的文档关系、加载次序陈述、提取删除/备份/装载器与合并保留散文件陈述、所需 Ruby、未跟踪资源类别 | 仓库作者读物。WP75 §12.1 line307、§12.2 line317、§12.4 line339 作文档接合；真正脚本行为仍须 R6-B 父任务独立建立，不把 README 陈述当运行观察。 |
| LICENSE | 1–436 | CC BY-NC-SA 4.0 标题、前言/考虑事项、定义、许可范围、条件、数据库条款、责任/担保、期限/终止、其它条款、解释、末尾 CC 机构说明全部读过 | 仅来源仓库许可元资料。没有就新框架或某使用行为作法律结论，没有扩张为游戏机制或未来许可要求。 |
| .gitignore | 1–34 | Audio/Graphics/Plugins/Screenshots、Data 通配排除及 Scripts.rxdata / Scripts / messages_core.dat 例外；errorlog、Game.ini/rxproj、RGSS DLL；编辑器/OS/临时项 | Git 跟踪策略。ignore 规则不证明目录或文件事实上缺失，不是游戏读写/删除规则，也不约束未来工程布局。 |
| .rubocop.yml | 1–225 | Ruby 3.0 目标、新 cops；Layout/Lint/Metrics/Naming/Security/Style 全部键值与注释。包括对排列/对齐、文档/指标/命名、eval/Marshal 警告、字面量/格式/条件/循环等检查规则的设置 | 源代码检查器配置。关闭 lint 检查不证明运行安全或不安全；注释不代替消费者审查。没有要求未来采用 Ruby、这些类名/方法形态或同一代码风格。 |
| Essentials Engine wiki.url | 1–5 | Internet Shortcut 类型、shell 属性、外部 wiki URL、空 IDList | OS/用户网页快捷方式。未访问网页、未导入网页内容或版本假设，文件存在不证明网站可用。 |

五份文件均以 R commit 原始 blob 与工作区字节相等复核。元资料全文读取不是对未来产品义务、源码架构或完整 Demo 的背书。L13 保持。

## 3. 每类 PE 结构字段的独立解释

文件名、字节数和 SHA256 绑定被解析的原字节；machine / PE32+ 指明本文件的静态目标格式。entry RVA 是可执行入口的静态位置；image base 是首选映像基址；它们不证明入口曾到达。section 的名称、虚拟尺寸、RVA、原始文件尺寸/偏移、flags、哈希分别描述布局、映射、权限/属性和字节身份；可执行 flag 不代表每字节都是有效指令。

全部 16 个 data-directory 索引按用途分类：0 导出、1 导入、2 资源、3 异常/展开表、4 certificate、5 relocation、6 debug directory、7 architecture、8 global pointer、9 TLS、10 load config、11 bound import、12 IAT、13 delay import、14 CLI、15 保留。RVA 和 size 是结构边界。三个文件只有 0/1/3/5/9/12 共通非空；Game/Ruby 另有资源2。certificate/debug/CLI 目录均空，不把目录为空外推成没有调试字节、没有动态装载、没有安全功能或完整运行通过。

区段按静态用途解释：`.text` 是原生可执行字节范围；`.data/.rdata/.bss` 为初始化/只读/无文件载荷的映像数据；`.edata/.idata` 为导出/导入材料；`.pdata/.xdata` 为异常/展开元资料；`.CRT/.tls` 为运行库/TLS 结构；`.rsrc` 为打包资源；`.reloc` 为重定位。Ruby 另外具有 `.debug_aranges/.debug_info/.debug_abbrev/.debug_line/.debug_frame/.debug_str/.debug_line_str/.debug_loclists/.debug_rnglists` 九种命名区段。它们是调试元资料，不是本轮重建完整 native CFG 的证明。空 PE debug directory 与存在这些区段并不冲突。

导入每一条的 DLL、name/ordinal、hint、IAT RVA 均已结构复核：这是链接依赖与查找材料，hint 不是调用次数，IAT 位置不是已执行 call。导出每一条的 ordinal、name、RVA、forwarder 均已复核：ordinal 是导出表编号，不是业务顺序；所有导出均无 forwarder。导出并非一律函数，部分位于数据区段。

COFF 全部 core 字段 index、name、value、section number、type、storage class、auxiliary count 都独立复核。value 必须在其 section/绝对/未定义语境中解释，不当成流程结果；section -2 是调试记录类别、-1 是绝对类别、0 是未定义类别。Ruby 的记录落在代码、数据、导入、TLS、CRT、资源和九类 debug 区段，也有 180 个 file-parent、642 个绝对记录及 1 个未定义记录。zlib 的 56 个 COFF 记录均为 `.idata` 元资料。5158 个辅助条目的边界与关联父记录完整核对；并未把辅助字段当成可执行算法。

Ruby file-parent 的 180 个辅助名已完整呈现阅读，其中有 `<artificial>`、`fake`、截断构建名与两条含非文本字节/替换字符的值；这些字段只能按静态调试材料处置，不证明存在同名可得源文件。root 将 `section_aux_fields` 视图也附在 68 个 type32/static-function 父记录上，本子审把这 68 条辅助字节保留为不透明元资料，不推为 section definition。该工具注释注意项不构成正式行为缺陷，待 root 判断是否细化标注。

## 4. 三份接口表逐组分类与 consumer

Game 的 17 组完整导入：ADVAPI32（密码/注册表/事件/进程令牌）、CRYPT32（证书存储）、DSOUND（音频接口）、GDI32（绘制/字体/像素格式）、IMM32（IME 接口）、KERNEL32（系统、进程/线程、文件/内存/同步等）、msvcrt（C runtime / 数学/字符串/文件）、ole32/OLEAUT32（COM/OLE）、SHELL32（shell 路径/参数/拖放）、USER32（窗口/输入/剪贴板/消息）、VERSION（文件版本查询）、WINMM（MIDI/wave/计时）、WS2_32/WSOCK32（socket）、zlib1（4 个压缩相关入口）、Ruby DLL（130 个宿主语言接口）。这只是名称分类，不能判定每族在当前游戏中的可达性或调用成功。

Game 的全部 824 导出由 IMG 50、SDL 701、TTF 71 与两个 GPU 偏好数据符号组成。IMG 名称覆盖图像/动画格式与载入/保存候选；SDL 涵盖系统/平台、视频/窗口、renderer/texture/surface、输入/控制器/joystick/haptic/sensor、音频、事件、线程/同步、文件与辅助计算；TTF 是字体/度量/文本绘制接口。没有将它们提升为未来所有格式支持、renderer 架构或物理输入承诺。两个 GPU 标记位于非可执行区段，不能从名字推出高性能 GPU 实际被系统采用。

Ruby 的 9 组完整导入：ADVAPI32、bcrypt、imagehlp、IPHLPAPI、KERNEL32、msvcrt、SHELL32、USER32、WS2_32，按系统/随机/调试/网络/文件/控制台/进程等链接元资料分类。2773 导出为 Onig 156、rb 2392、ruby 151、其它74；其中 737 个导出 RVA 位于非可执行区段。它们说明此 DLL 暴露语言运行库/编码/正则/容器/对象/VM/GC/I/O/线程与平台等符号，不要求未来复刻 VM、类层级或这些原生 API。+YJIT/+MJIT 版本字面量并不证明某 JIT 已选用。

zlib 的 2 组导入为 KERNEL32 18、msvcrt 32。105 个导出逐名读过，覆盖压缩/解压、字典、checksum、gzip I/O、流/内存/错误查询和内部数据/辅助入口；有 5 个数据区段导出。Game 的 4 个 zlib 导入只是当前静态链接候选，不能推完整 gzip/所有导出被游戏使用，更不构成未来使用此库的要求。

全部 consumer 最多建立到原生链接/宿主界面；本次未证明调用、参数、异常、业务状态或实际图形/声音结果。源脚本更高层行为另由相应 reviewer 审查。

## 5. 资源、字符串与静态元资料限制

Game 的全部 4 个资源：类型3/id1/lang1033 图标 DIB（256 宽、含 mask 的512高、1 plane、32 bpp、未压缩）；类型14/id101/lang1033 icon group 对应上述图标（宽高字节0，记录256尺寸约定，bytes/resource id 对接）；类型16/id1/lang1033 完整版本树（文本 ProductName mkxp-z、OriginalFilename mkxp-z.exe、FileVersion/ProductVersion 2.4.2、translation 0409/04b0）；类型24/id1/lang1033 manifest。manifest 612字节全文读过，只有 assembly/namespace/version 与 dpiAware=true、dpiAwareness=PerMonitorV2 声明，不保证实际 DPI/窗口行为。资源表路径、offset、size、codepage、sha256 都复核，未把图标或版本内容当游戏规则。

Ruby 的唯一资源是类型16/id1/lang1033 版本树：Comments 日期、CompanyName URL、Ruby 3.1.3p185 描述/版本、DLL 文件名、版权文本、ProductName/ProductVersion 和 translation 全部 read；它是封装元资料，没有推导许可义务、真实解释器执行结果或兼容全部 Ruby 脚本。zlib 无资源。三个空 debug directory 已登记；不能由此说 Ruby 无 debug 区段。

已选 290 字面量逐条解释为版本、配置名、音频/字体/音色库接口候选、诊断/帮助候选、符号或偶然字节。Game 284 条中的类别 fonts 也混有 SoundFont 内容和压缩文本片段，editor_windows 的 comment 不能证明编辑器窗口调用，`|$ fontt` 与 Ruby `EBFONT` 不能证明字体能力。诊断字面量的存在不保证错误会被检测/捕获/显示；库帮助文案不证明游戏提供 shell 命令；默认 SoundFont 路径字面量不覆盖 mkxp.json 指定的 soundfont.sf2。外部媒体 consumer 与字体/SF2 结构由 D/root 独立审查，本子审不转签声音/字形结果。

## 6. 控制器表与游戏输入交界

本轮 BIN-0003 原字节定位：Game.exe `[9774912,10217559)`，442647 bytes、1678 行，SHA256 `8883f85acfad455feedca7a95203e18629d5c60fc3933d7f511eebd731089cfe`。自动结构索引为 1666 数据行、790 个按原字段顺序区分的完整模式，剩余为标题/来源注释/平台节注释与空行；索引不是语义 PASS。`controller-rows` 子任务已读全部完整 GUID/未裁剪名称/源行/模式关联、全部790完整有序键值模式、全部12注释/空行。19条全文账本与结构账本分开；不是每条原始长行都独立原样显示，而是无损重复压缩后的全部数据语义阅读。父任务独立核对原 Game 字节与提取、子审原文日志相等，全部1678源行无覆盖缺口（`controller-integration-checks.json`）。自动核验只证明来源/关联/覆盖，语义结论来自子任务实际阅读与报告。

标识是该表记录的设备选择令牌，不在这里按本地硬件生成或承诺厂商/平台查询结果；1664条为32位小写十六进制字符，另两条是源732/1432的 `xinput`。name 是设备显示名，完整保留源344的末尾tab、644/1334的末尾空格及iOS七条星号名称；星号名称不等于GUID通配。每个 control→binding 值属于 SDL 标准控件到 raw button/axis/hat 的候选关联，platform 为唯一键值元资料字段。a/b/x/y、方向、shoulder/stick/trigger、guide/back/start、misc/paddle/touchpad 及带正负目标轴分量的字段和全表异常/遗漏在子审报告逐类解释。原始轴和 button 索引、半轴/反向、hat index/bitmask 不等价于当前主机采样阈值或游戏命令。

平台数据行全集为 Windows5–735共731、Mac OS X738–948共211、Linux951–1434共484、Android1437–1650共214、iOS1653–1678共26。30734次binding值包含18414按钮、5160方向帽、7160轴；字段无重复键。无同平台同标识竞争记录；58组跨平台同标识、全部同名和同模式重复、30条完全相同物理来源令牌共享、583条缺至少一个核心字段、20条带符号目标轴、24条反转轴来源、3条非通常hat方向关联、前导零/高索引/稀疏设备等均完整枚举留档，不判为录入缺陷或给缺项补默认。表中未提供死区/阈值/校准、热插拔、振动或游戏命令字段。

必要 consumer 接合：Game 导出表确有 SDL GameController/Joystick 名称，与内嵌 SDL 表静态关联；在整个可得 Data/Scripts 和 mkxp.json 中检索 GameController、gamecontrollerdb、joystick、controller mapping、SDL_Game，未定位显式表加载/选择者。该负证据不排除 native consumer。`004_Input.rb:1–31` 全文另读：八个动作别名依附既有 host 常量，update 包装加 F8 截图查询；Mouse 默认窗内守卫、catch_anywhere 可绕过。`mkxp.json:1–159` 全文另读：bindingNames 只定义 F1 菜单显示名，没有其它用处，不是设备 raw binding 配置。

普通对照：SDL 表中的 a/b 控件、mkxp bindingNames 的 a/b/c 文案与脚本 ACTION/BACK/USE 各属于不同层。把某行 a:b1 直接等同“button1 触发 ACTION”没有本域 consumer 证据。Linux、Mac OS X、Android、iOS 行嵌在 Windows PE 中也不证明对应宿主运行或跨平台兼容。WP17 line21 与 lines165–167 已正确区分 host 提供和参考脚本别名；无需由表存在增加必修的特定设备/GUID 全集或原生 API。

未知：实际 GUID 来源/查找优先序、平台选择/加载、热插拔、raw索引有效范围、axis阈值/量化、重复/按下沿、rumble、SDL动作到游戏动作映射、任意覆写和物理输入。全部维持 L04 host 边界。

## 7. 精确 L04 与结论范围

未建立完整 native CFG / data flow 的 `.text` 原始字节范围：

| 文件 | 半开文件范围 | bytes | 区段 SHA256 |
| --- | --- | --- | --- |
| Game.exe | [1024,9738752) | 9737728 | f75bc490275eb7562b1ea95638c1cf8d205227e93dd0e87d9f1b306dd62b2f67 |
| Ruby DLL | [1536,4072960) | 4071424 | 0a3e27a9f35ba23e99e85de6ca82c13c29b8bb53eb35b1efb50045bd83b571e5 |
| zlib DLL | [1024,82432) | 81408 | 162bb7246550edb8a6a59afd7112f72e134d73538e80593ac515743dcbc6422e |

这不是源可读脚本/着色器/控制器尚未读的通用借口。三份文件的其它数据、TLS/异常/重定位、debug/COFF 与字符串同样只获相应结构级或限定字面量处置，不冒称全部 native 行为被审。没有执行三者，不能由接口名判断运行功能通过或当前 selector 实际选中了哪个后端/平台表/版本。恢复完整 native 或 host 结论需另有有界独立分析或明确隔离宿主证据。

本子审无必修 formal 修订提案。两项静态证据标注注意点在 `findings.json`，均为 boundary/tool annotation，必须由非提出者/root 裁决，不能自动并入 mandatory。五份根元资料、三份 PE 的上述结构范围、必要 script/config 输入交界与控制器完整静态数据语义均已完成。指定根元资料/控制器可读工作量未读为0；这不取消259625个未选候选的inventory-only处置、L04机器码/host/consumer未知，也不转签父任务其它compat脚本、shader、IL、工具或整篇formal。
