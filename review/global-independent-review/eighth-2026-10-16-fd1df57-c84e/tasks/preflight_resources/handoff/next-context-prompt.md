# R8 controller 与有限可读字符串独立新上下文任务

你是第八轮全局审查的新审者。主会话分配新的独占输出目录后才开始写文件；**不要改本提示所在的preflight_resources目录**。本任务不安装、不运行目标EXE/DLL、不改R/formal/planning/audit/旧报告、不提交或推送、不自行spawn。必须完成实际新读，不能把旧报告或已解析计数继承为本轮FULL_READ。

先完整阅读合同 `libfile_f8ff592304d081918512f51317a8ecee` 的 `eighth-global-review-prompt.md`（36653 bytes，SHA256 `63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b`）。Library read可分块；本地逐字副本在本目录 `contract/eighth-global-review-prompt.md`。完整读 `/workspace/pokemon-essentials-clean-room/AGENTS.md`。指定clean-document-revision技能本地缺失，已恢复完整替代 `contract/review-SKILL.md`（3598 bytes，SHA256 `ac3c8560f38192269b65b061673896a77f5eb794b90e90644e3c445b2c3be1f8`）；其审计历史不适用边界须准确保留。

固定B8 `/workspace/pokemon-essentials-clean-room` commit `fd1df570cad987dc3852a3b958f03916e317f7fe`，tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`。固定R `/workspace/pokemon-essentials` commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。受审始终固定对象；报告分支HEAD允许主会话合法纯报告前移，不能以HEAD必须B8阻断。所有使用的实际文件先与固定对象核身份。

请求配置为gpt-6.1-sol、ultra、default普速、Fast off。之前实际model/effort/tier/speed/platform session ID均UNVERIFIED，新会话也须按真实回显逐字段记，不能猜。Linux当前有Python/Node/git/binutils/fonttools等，Ruby/mono/dotnet/wine不在PATH，之前没有安装。只做有限、安全静态解码；先完整读懂工具再运行/改写。每次真实运行保存完整分离stdout/stderr、实际exit、start/end UTC；未运行保持NOT_EXECUTED。结构解析与独立行为模型、参考行为、宿主观察分开计数。

输入根为本提示上一级 `preflight_resources/`。先完整读 `handoff/readset-index.json`，校验每个输入的长度/SHA；工具 `freeze_controller_string_readset.py` 是本轮完整可读新解码器，历史工具路径/SHA在index中。历史工具只作恢复导航，执行前须读懂依赖。若工具连接断开，具名报告exec-server transport问题并有限重试，不能冒称远端Git失败。

第一读集：`handoff/controller-readset.json`。当前Game.exe为14,732,288 bytes、SHA256 `5c75e92fcbb6ec50b9f8fc61913d751a8945d6a1fc69c3017c7b8686b532bf04`。表区域offset9774912、length442647、end10217559、SHA256 `8883f85acfad455feedca7a95203e18629d5c60fc3933d7f511eebd731089cfe`；原始字节在 `current-controller/raw.txt`，旧本轮解析 `current-controller/records.json`。新readset逐行保留实际源偏移、SHA、原文、guid/name/有序mapping及pattern_group，1678行/1666记录/790完整模式。解码为严格ASCII，按真实CRLF分行，逗号拆字段，GUID与名称后每个非空字段仅按首个冒号拆分，保留顺序和重复。仅两条特殊GUID为xinput。平台五类Windows731/Linux484/Android214/Mac OS X211/iOS26，不能漏写Android/iOS。

这1666记录的语义接受原先整体UNREAD。请完整读全部记录与注释，逐完整mapping单位接收：标识/名称、控制项、按钮/轴/hat/正负方向/反向表示、缺项、重复键和平台字段；790模式只可用于无损重用，不能只读790数量或机器去重结果。记录/模式/行之间须可回溯，并给连续read ledger。不能因已解析而FULL_READ，更不能由表内绑定推出实际设备激活、native选择、物理输入或成功运行。

第二读集：index指定的5个 `handoff/*.strings.jsonl`。规则分别为全部文件字节的 `[0x20–0x7e]{4,}` ASCII最大run，以及 `(?:[0x20–0x7e] 0x00){4,}` UTF16LE的ASCII子集最大run，任意字节对齐。每条含路径、encoding、start/end、字节SHA、text与前读引用；这是精确有限候选库存，不是任意Unicode/UTF8/UTF16全编码或压缩解码的完备声明。所有没有前读引用的 `UNREAD_FINITE_STRING_CANDIDATE` 都是可得已定位未读，不得放入L04。

完整审读/分类现有有限库存：纯诊断/状态/版本metadata、符号/路径/接口名字、控制器记录、实际程序/生成片段、随机可打印候选，以及仍无法确定的具名候选。以完整结构/程序单位为准，不能只搜关键词宣称无程序。可先按可逆的原始结构分组和无损重复复用，但不得让转换丢失记录、字段或前提。发现新可读程序须按当前字节完整恢复与新读，检查实际consumer和formal；不能停在“有字符串”或“native未知”。

前审已完整读的有限单位：`current-programs-v2/inventory.json`的66 shader候选（55main/5prelude/6非程序）、650C候选（646片段/4非程序）、3XP/VX/Ace兼容程序全3448行、extendtext小程序；animmaker全部15方法743指令1670CIL bytes11EH。还有 `current-literal-discovery.json` 的5条明确ASCII marker规则315候选，248包含在旧已读单元，67由 `literal-discovery-reception.json` 另行全读：13额外条件C片段、53非程序诊断/metadata、1个shader尾接字节。因此至少659C片段已被提案者完整读。它们可以作为反证入口，**不能继承为你的独立接受**，五条规则也不能替代此任务完整有限字符串库存。

第三读集：配置/实际消费者/formal分母。`mkxp.json`已有提案者全文读取，只能证明声明，不证明native wiring。请先选择并冻结实际R输入消费者（至少定位核验 `Data/Scripts/001_Technical/004_Input.rb`、`Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb` 及它们的实际入口/覆盖），完整读被使用的定义和调用链；不用一份全R关键词命中表冒充消费者接收。formal至少定位 `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md`、相关catalog，以及字符串所涉WP15/WP16/WP75条款的实际边界。相关共享文件和结构单位须由主责全文接收，其他领域须与主会话协调，避免碎读后全文件PASS。controller是否选择为未来实现强制需求仍未接受，禁止无证将旧SDL表或旧兼容API作为必修政策。

PE其他可读元数据/资源存在但未完整语义接收：exports、COFF/debug符号、manifest/version/string-table等。`native-region-denominator.json`给完整5PE字节/section分母；`current-other-pe.stdout`仅结构解析，输出曾截断，不得标全文读。可复用恢复的audit_binaries.py中有限PE资源/符号解码器，但必须先读懂完整依赖、绑定当前固定对象、日志真实并区分解析与语义。不得把已定位元数据包入L04；也无需无限逆向整台native CFG或猜测任意编码/压缩。

最后交付完整source事实→实际consumer→formal条款与反向核对、每个疑似GR8-RES-*的反例/边界/证据、连续read ledger、实际运行记录与具名UNREAD/opaque/宿主差异。独立非提案者反证由主会话分配，不自行验收自己的NO_REQUIRED。所有行为向量保持NOT_EXECUTED除非确有另行安全授权且真实执行。持续更新自己的progress.json，并在收尾准确写出接收分母、实际完成与剩余项。
