**RES 定点独立反证补充审查：指定静态数据与接口工作完成，整体二进制语义不签全审。**

固定 B5=`9366d9d17aaeac3b4414236468affa650fb3dd27`，正式根为 `deliverables/final-specification-set/`。R 只读根为 `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`，commit=`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree=`7589c800b61ba13a13040ed0d686979b80a84fd0`。沿用主会话已核身份，没有重复行政审计。

原样保留运行请求：“请求 gpt-6-astra / reasoning_effort=ultra / service_tier=default，禁Fast。”实际参数回显不可得，记 **UNVERIFIED**；未改请求、全局配置或调查额度、认证、私有会话、后端。没有创建其他 agent/模型会话。本 RES 参考执行、模型执行、宿主/Demo 执行均为 **0**。作者安全解析器、对象文件读取器和解析器校验属于 TOOL_VALIDATION，不是执行 R。既有 M12 的其他执行记录没有挪作本轮证据。

本轮仅在 RES 目录写产物，未改正式、参考、历史、共享、M10 或 M12；未提交、推送、安装、启动 update、下载媒体或播放音频。没有实现新框架。

SoundFont 已完成所有存储记录及数值样本的静态审查。独立解析器直接读取 R；既有 M12 后来新增的内容 ledger 只用于全记录交叉核验，未执行或改写它。文件 SHA-256 为 `614ffa8eb1ac9bbb63fc97943dd67aa8fa706e2178b888777610c87e4e4b8cc8`。布局依据为 [E-mu SoundFont 2.01 原始格式文档](https://www.synthfont.com/SFSPEC21.PDF)，其默认规则与 R 中实际存储行严格分列，不把外部合成器代码算作 R。

| 表/数据 | 有效记录 | 终止记录 | 审查结果 |
| --- | ---: | ---: | --- |
| 预设 / 乐器 / 样本头 | 236 / 240 / 505 | 各 1 | 名称、bank/program、范围、关联、保留字段及所有权全读 |
| 预设区 / 乐器区 | 241 / 1463 | 各 1 | 全局/局部、生成器/调制器跨度、所有引用全读 |
| 预设生成器 / 乐器生成器 | 252 / 21509 | 各 1 | 原值、符号性、单位、顺序、有效继承与名义范围全读 |
| 预设调制器 / 乐器调制器 | 0 / 1331 | 各 1 | 两个源的位域、目的、金额、变换及继承关系全读 |
| PCM 采样点 | 2,000,710 | 不适用 | 1,984,550 个样本内点＋16,160 个间隔点全部数值扫描 |

全部 25,786 个表记录都有 data/consumer 投影，包括终止行。[全量证据](soundfont-full-audit.json)保留字节偏移、每行字段、消费者、所有 1,524 条预设到样本关系、逐关系参数和调制器、样本统计及未归样本的区间；[合同](resource-contracts.json)提供每条记录的索引。没有输出原始 PCM 媒体。

需要保留的反证与边界如下：

- **1,524 条是结构链接，不是 1,524 个可触发层。**其中 106 条键位交集为空，全部位于 bank 128 / program 127；1,418 条有非空选择域。21 个样本没有非空的完整预设选择关系，仍完整记录，不删数据。
- 1,331 个活动调制器的金额全部为 0。2.01 文档 §8.4.2 的印刷金额源 `0x502` 与位域描述所编码的 `0x0d02` 矛盾；[2.04 文档](https://www.synthfont.com/sfspec24.pdf)该处又记录 0。按 2.01 位域解释，匹配的文件零金额行会覆盖默认；按这些印刷值则身份不同。每条关系保留条件投影及替代解释，不能宣称宿主必然保留或消除默认滤波调制。默认项不是从文件读出的额外行。
- 两条非零**终止调制器**分别为 pmod 的 transform=1、imod 的 transform=3；它们不进入活动调制器集合。不是生成器异常，也不是可播放数据。
- 42 个存储参数超出格式表名义范围。样本全为 mono，采样率为 22050、24000 或 44100；所有声明/有效地址的本次界限检查通过。
- 每段样本之后的实际间隔是 **32 个零点**。前 504 段检查后 46 点会进入下一段；最后一段只余 32 点且全部为零。因此原 M12 “505 段后 46 点内均有非零”表述过强；正确结论是 505 段均不满足完整 46 零点谓词。这里只提供修正证据，不改 M12。
- 格式可移植性检查还发现 41 个循环前不足 8 点、36 个循环后不足 8 点、503 个循环两端的 8 点邻域不相同。它们不能证明宿主拒绝、卡顿或听感缺陷；非循环关系也不应被说成实际循环故障。

`mkxp.json:64–66` 明确选择此 SoundFont 供 MIDI 使用；它不是 `Audio/` 下的曲目。FileTests、四类音频请求、MusicFileLister、Jukebox、消息 SE/ME 和动画导入的消费投影已核。WP15 的文件存在性、参数/音量/逻辑登记与宿主请求合同仍成立；SF2 的存在不补出缺失 MIDI 曲目，更不证明真实发声。WP17 与 M10 的 `SHARED-AUDIO-REQUESTS`、`SHARED-RESOURCE-SELECTION`、`SHARED-FONT-MEASUREMENT` 已按交界核对。动画导入中 `.midi` 因末三字符检查不复制的边界，WP74 已准确覆盖，不重复提报。

`animmaker.exe` 已超过 PE 头层：全部五个 CLR 元数据流、16 个实际表、全部 blob/字符串/签名以及 **15 个方法的 1,670 字节 IL、743 条指令**均解码并逐方法静态审读；分支与异常区间检查通过。参考解释使用 [ECMA CLI 标准](https://docs.ecma-international.org/ecma-335/Ecma-335-part-i-iv.pdf)及后续标准的元数据定义；无 IL 解释器、JIT 或程序执行。完整逐方法审读结论见 [reading-coverage.json](reading-coverage.json)，元数据和调用证据见 [binary-interface-audit.json](binary-interface-audit.json)。

可读正常/边界行为包括：画布宽 960、五列 192 格、高为 `192×max(1,ceil(N/5))`；图样两倍放大后居中；缺图保留原槽；以 x 属性是否缺失/空作为整图/矩形开关；矩形字段允许 0、拒负数、没有 96 上限检查；非 alpha 图取左上角颜色请求透明化。请求的插值数值 5 和绘制单位 2 分别对应 [NearestNeighbor](https://learn.microsoft.com/en-us/dotnet/api/system.drawing.drawing2d.interpolationmode)及 [Pixel](https://learn.microsoft.com/en-us/dotnet/api/system.drawing.graphicsunit)。这些是调用参数解释，未证明实际像素或输出编码。

失败合同也已单列：整数转换只捕获指定异常；缺 XML 请求退出；缺图片提示后继续；读 XML 的 IOException 路径可保留已积累结果；XmlException 诊断引用第三个格式参数却只传两个替换值，不能承诺友好报错。未被入口调用的整数辅助方法另标定义级。`.NET` 库实现、XML/编码器策略、文件实际写入和 `.anm` 衔接仍未知。

`extendtext.exe` 已沿字符串、IAT、应用函数和导入跳板核对可读请求路径。除文档的 Script/Show Text 外，还有 Comment 和 Batch Text Entry；四类分别请求 840×240、840×144、840×164、840×444，配套 EDIT 及批量输入按钮位置见合同。窗口类/标题匹配、具名 mutex、150ms 轮询请求、未检查调整结果均已登记。Win32 参数含义参照 [SetWindowPos 官方文档](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowpos)；没有操作任何真实窗口，也不把 CRT 启动/异常代码签成全语义已审。

其余 PE 已完整枚举可得的节、导入、导出、资源目录、版本、manifest 与 COFF 符号。Game.exe 内部版本声明 mkxp-z 2.4.2；Ruby DLL 版本资源声明 3.1.3p185。Game.exe 对这两份本地 DLL 的 4 个 zlib / 130 个 Ruby 符号均有同名导出，但未据此推 ABI 或加载验收。格式解读取自 [Microsoft PE 文档](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format)。

Game.exe 中 1,666 条控制器映射已解码；可读兼容脚本的音频尾部已核，发现不同包装变体，选择机制未证。**其余三块可读兼容脚本正文、29 个已定位长着色器块、26 个其它可打印长数据块与未逐项解释的字符串候选没有混入 opaque。**它们分别登记为接口 inventory / 部分审读，不认证全部内嵌程序语义。原生 Game/Ruby/zlib 机器码的任意行为也未全量证明。

现有 `dwarfdump` 能读取 Ruby DLL 的 64 个 MinGW CRT/数学/支持编译单元；[调试接口证据](native-debug-metadata.json)记录已解码属性。可选 `--verify` 在继续工作期间一直未返回，已通过工具 control-C 中断，状态 **INTERRUPTED_NO_RESULT**，绝不算通过；正常 `--debug-info` 读取成功。没有把“缺 monodis”等同于不能读托管 IL，也没有把“工具能反汇编”等同于能证明全部原生语义。

已有八字体全部 cmap/metrics/contactsheet 和两个 BMP 全像素证据已读取作上下文，未重做解析或渲染。字体存在、映射及度量不推出宿主 `Font.exist?`、字宽、hinting 或实际界面结果；预览证据仍归原 M12。

本轮保留 **GR5-M12-202/203** 两项 P3 建议候选：animmaker 新静态行为范围、extendtext 四类窗口请求范围。均为 `candidate_pending_independent_counterevidence`，**未自签 required**。父会话最新 `parent-note.md`、`host-config-contracts.json` 与 `M12-ROOT-23` 已承接 SF2 配置依赖；GR5-M12-201 据此并回既有能力，不另计新必修问题。已有 hydra/PCM 分母复用并交叉核对，不累加为 RES 新覆盖工作量；新增部分是全局/局部关系、选择域、默认调制器、终止记录及更深二进制接口。WP74/75 已明确“仅文档/不反编译”，这是候选成立范围的反证约束；新可读证据不自动成为现有正文错误。全局 Feature Matrix 未改，本地合同身份仅供后续整合。

30 项解析器检查通过：既有 M12 全部非终止字段/样本哈希与新解析逐条一致，结构链接一致；新增终止/选择域/尾部边界明确补充；内存中畸形输入拒绝检查通过；PE 依赖目录与独立 objdump 对照一致。没有第二套可用 CLI 解码器，故 CLI 证据为有界解码、逐方法人工审读与格式核对，而非独立双工具认证。复现入口为 [audit_resources.py](audit_resources.py)、[audit_binaries.py](audit_binaries.py)、[audit_debug.py](audit_debug.py)、[verify_parsers.py](verify_parsers.py)，使用 `PYTHONDONTWRITEBYTECODE=1`。完整技术边界见 [limits.json](limits.json)，完成状态见 [progress.json](progress.json)。
