# Controller 与有限字符串的当前独立审读结果

固定输入为 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe` / tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`、formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。本上下文开始时报告 HEAD 为合法后继 `7956f5cba2061702b30f3a021da47f386c92250f`，没有替换受审对象。36 个入口身份绑定见 `identities.json`。

本报告的结论是：**controller 有限表已完成实际新读；260161 个候选已全部逐 ID 入账，但字符串总域语义审查未完成，真实 UNREAD 为 57948。** 不能据本报告宣布资源域通过、NO_REQUIRED_UPDATE 或全量程序发现完备。四项稳定提案均为限定范围的 no-required 建议，等待主会话安排实际非提出者反证；接受数为 0，不将自己的提案签为独立裁决。

请求配置是 `gpt-6.1-sol / ultra / default普速 / Fast off`。实际 model、effort、tier、speed、平台 session/agent UUID 均无回显，逐项 `UNVERIFIED`。`/root/binary_controller_strings_review` 是实际分配的逻辑任务入口，不冒充平台 UUID。

## 已接收的 controller 分母

原表为 Game `[9774912,10217559)`，442647 字节，SHA256 `8883f85acfad455feedca7a95203e18629d5c60fc3933d7f511eebd731089cfe`。严格 ASCII、真实 CRLF 与字段顺序保留；完整覆盖 1678 行、1666 记录、790 个完整映射、122 个键顺序、806 个字面名称。读取按 `controller-pattern-view.txt` 的 P0–200、P201–450、P451–789 连续完成；该无损表示复制先前完整映射后逐项替换/删除，并以独立的完整顺序表还原每条原映射。脚本逐条验证重构与原有序字段相同，不以模式数代替阅读。806 个名称组及其全部 1666 行引用也已按连续三块读完。

平台为 Windows731、Mac OS X211、Linux484、Android214、iOS26；其完整模式分别331/108/206/130/15。共36个键，含 platform、带正负号的目标、misc1、paddle1–4、touchpad；源字段有按钮、轴、hat、正负向、反向字面记号及高编号值。没有重复键。GUID 原字节按身份完整处置：1605 个全局 GUID，1666 个唯一 GUID+platform；仅两条特殊 GUID 为 xinput，分别位于 Windows 第732行和 Linux 第1432行。第344行名称末尾 tab、第644/1334行名称尾空格均保留。缺项没有补为默认绑定。

`controller-ledger.jsonl.gz` 对全部原行给出 source offset/end/SHA、映射和新阅读凭据；GUID 的身份处置与映射/名称的 FULL_READ 分开。该接收没有证明任何实际硬件、注册成功、游戏逻辑键或运行结果。

## 新的局部原生接线证据

该证据来自实际指令和 PE 导出/IAT 绑定，并非字符串命中推断。Game 偏移59023读取9774880处的长度字442647；59029取得当前表地址，59036请求导出 `SDL_RWFromConstMem`；59049把返回值及参数1交给导出 `SDL_GameControllerAddMappingsFromRW`，随后有 `SDL_JoystickUpdate` / `SDL_NumJoysticks` 请求。**前提是控制流到达此处且前一分支没有跳开**。导出入口自身仍是间接 dispatch thunk，不能据此确定最终 receiver、所选解析器、平台筛选、注册优先级或宿主查询到游戏键的映射。所读局部续段没有先检查 mapping 请求结果。

R 的 `Input` 八个逻辑别名、F8 更新钩子、鼠标窗口内守卫、`mkxp.json` 的 display-only bindingNames、四页帮助场景和 `EventScene` 完整定义均已新读。帮助同轮 BACK 优先于 USE，标准空 BACK 回调仍会抑制 USE；全脚本定位搜索只找到帮助定义/说明注释，没有实际可执行调用点。F8 助手主相对 Screenshots 路径、一次保护回退、保护前取时及条件完成音，与 WP17 现有限定合同相符。帮助中的默认键和存档同目录说明不替代实际源路径或绑定证据。

B8 WP17 §6.1 的21目标合同本来就限定于先前选定字段解析器和普通分配前提。当前表有36键并不反证该有限条件句，也不能由 `a:b0` 直接推出游戏 USE/ACTION。原 CC04 的更宽查询桥、真实设备及后端选择仍未接收。新接线事实保存在 R8 证据，未据此强制修改未来框架架构。

## 新发现并读完的短程序与数据类型

完整有限候选定位揭示了旧五条 marker 未覆盖的七个短程序单位，逐一按原字节恢复到 `new-programs/`，身份见 `new-program-inventory.json`。其一是 Game 48字节的条件 zlib 装载片段；原生535423取其地址，535435经准确 IAT 请求 `x64-msvcrt-ruby310.dll!rb_eval_string_protect`，535444检查保护状态。查询结果为真时不请求装载，假时才请求；未接收的原生错误续段不被写成成功或统一恢复。R 的插件压缩/运行、翻译源收集、Mystery Gift 和动画交换的具名 Zlib 使用单位也已读，完整消费域仍由各 primary 负责。独立脚本工具自己的 require 与 native 前置装载分开。

另六个单位属于 Ruby 原生代码生成：include前缀、空 relocation helper、inline-cache 条件片段、预处理 guard、self 宏及类型/类序列条件前缀。具体地址引用进入 `convert_unit_to_func`、`compile_insn.lto_priv.0`、`mjit_compile_body` 符号区间中的局部 fprintf 请求。完整已定位片段已读，不等于整个生成器、完整组装源文件、文件写成、编译或执行均已接收。旧659个C片段仍保留原提出者的实际语义贡献，这六个单独计数，不强制搬入未来 VM/框架架构。

两项精确类型证据避免把可打印候选当成程序：

- Game `[12051776,12174560)` 的122784字节，与本机已安装 `libbrotlicommon.a` 的 `dictionary.c.o` 中完整 `kBrotliDictionaryData` 符号 `.rodata` 逐字节相同，SHA256 `20e42eb1b511c21806d4d227d07e5dd06877d8ce7b3a817f378f313653f35c70`。59个 HTML/JS 形式的 nomination 是压缩字典 token，不是独立网页程序。只读取 archive/object 字节，没有加载或执行对象。
- Game13227296起的13758个可打印字节，精确基址被8094406取址，8094415按16位索引读取，随后字节旋转并写出；13241056是另一个有独立引用的表基址。该长 run 是数值查表编码。此理由仅覆盖具名范围，没有扩成对任意诊断/配置/GUI文本的自动豁免。

另外连续读完1187个 `.text` 词形/长串/空终止 nomination 的完整内容（含编译进立即数的诊断片段、标识、crypto来源字样、CIL名字与用法文本），见 `code-fragment-reception.json`。其余可打印 opcode 子run给出逐候选连续指令字节覆盖证据；这仍不证明完整原生 CFG、组装消息或执行等价。

## 精确有限库存与剩余工作

ASCII最大run为258727个，UTF16LE-ASCII子集为1434个，共260161；只对应指定有限规则，不声称任意 Unicode、编码、压缩或机器CFG完备。完整 status 分母如下：

| 处置 | 候选数 | 信用边界 |
| --- | ---: | --- |
| INVENTORY_ONLY | 191850 | PE/COFF/debug/导入导出身份、具体指令字节覆盖、字典/数字表、PNG/图标等精确类型证据 |
| FULL_READ_CONTROLLER_TABLE_TEXT | 1674 | 1678行/1666记录所产生的有限regex候选；数不同于记录数，含注释及tab切分 |
| FULL_READ_TEXT_LITERAL_ONLY | 3521 | 1577个已读字面内容的出现；不等于原生消费者已证 |
| FULL_READ_RESOURCE_METADATA | 33 | 完整版本键值与612字节manifest；不认证宿主输出 |
| STRUCTURE_PARSED_PRIOR_SEMANTIC_CONTRIBUTION | 5135 | 旧程序/元资料/CIL的具体贡献归原实际审者；不是本上下文重读的FULL_READ |
| UNREAD | 57948 | Game37041、Ruby20817、zlib90；可得材料，不能归L04 |

787个旧/补充单位均独立核其当前原始字节及提取物身份；旧55shader mains、5preludes、659C片段、3Ruby profiles等语义贡献具名保留，未继承旧PASS。候选包含关系与类型差异在完整逐ID台账中，原5003个前读引用不能与本表5135的当前处置行数混算。

`full-disposition-ledger.jsonl.gz` 全260161条守恒；`remaining-unread.jsonl.gz` 是真实57948条的逐路径/encoding/offset/end/SHA/section清单。其41849个不同字面文本中还有实际诊断、接口、配置/GUI文字及未获精确类型证明的数值表子run，仍需后继实际上下文逐结构阅读和消费核对。`semantic-text-readset.json` 是早期可读优先集，**不能当作全部剩余分母**。另有764条 address-shaped word 证据候选保存在 `address-literal-ledger.jsonl.gz`，本报告保守地未据其自动减少UNREAD。

本上下文全文读了WP17和WP65控制帮助附页；共享1111行测试目录只接收1030–1111的R7-U02及具名CH定位，WP15/WP16/WP75也只读具名片段/接口。没有把这些共享文件标成整篇反向通过。完整formal/source的主责接收、所有跨域消费者和本任务四个提案的非提出者反证仍须主会话收口。

## 执行和交付资格

Python3.12.14、GNU objdump2.44仅做静态解码/校验。所有目标EXE/DLL、恢复Ruby/C/GLSL、生成对象均未执行；参考观察、独立行为模型、宿主/Demo、原生媒体、真实保存/回放计数均为0，全部行为向量 `NOT_EXECUTED`。

原stdout/stderr、真实exit、执行UTC保留在prepare/disassembly/dispose/finish记录和gzip完整stdout；三次inline Python语法失败、一次xref前缀索引纠正、PNG伪签名拒绝均具名保留。没有可恢复的历史/inline精确UTC不倒填，标UNVERIFIED。工具退出0与本域语义完成分开。

唯一写集为本任务目录。没有修改R、formal、planning/audit或旧报告，没有安装、spawn、commit/push、目标运行或整改。`UPDATE_NOT_STARTED`。
