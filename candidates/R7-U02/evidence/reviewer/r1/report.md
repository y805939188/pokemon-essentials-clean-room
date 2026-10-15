# R7-U02 r1 独立候选复审

结论：三个必修均为 **PASS_SCOPED_CANDIDATE**，无本版本限定候选阻塞缺陷。本结论只覆盖下列固定候选的三个最小合同及本批贡献；不登记实际整合 PASS、ACCEPTED 或 CLOSED。

| 必修 | 结论 | 内容依据与候选定位 |
| --- | --- | --- |
| GR7-M04-301 | PASS_SCOPED_CANDIDATE | WP17 L169–173；目录 R7-U02-SS01–12：主路径、有限一次回退、命名前置、音效与外部前缀完整 |
| GR7-M06-002 | PASS_SCOPED_CANDIDATE | WP17 L167、L283；目录 IN01–13：显式循环内请求与各入口尾部请求分开，原忙暂停与异常合同保持 |
| GR7-D06-001 | PASS_SCOPED_CANDIDATE | WP17 L175–184；目录 DB01–05、BT01–15、AX01–06；audit L1845–1866、matrix L570–577：有限词汇、字段处理与未读桥边界一致 |

表中 WP17、目录、audit、matrix 均指候选 `candidates/R7-U02/` 内的对应完整路径。逐ID、逐向量判定及来源范围见 [per-id.json](per-id.json)，逐文件完整身份见 [byte-validation.json](byte-validation.json)。全文正文319行、完整目录1107行已读；audit/matrix审本批新增全文、有关既有条款及历史接收边界，其余历史正文只核全字节保留，不新签其语义。

## 不可变输入与独立性

- 用户固定派发：`95c260d8f3fb4a171675dde877137fcd4c2f1c8d`，tree `577c350364bb4e2eb712325a9095d53d29eeeeb3`。指定 reviewer-dispatch.md 已完整读，并与固定 Git blob 全字节比较。
- 实际候选冻结：`aa369555b0e8b6c8b077f964b54ed63d3b924f26`，tree `08bd0f362c74ef7645b5bbd70b557489c122ae29`；精确 `review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U02/candidate-input.json`。四个冻结载荷均按此提交接收，未用浮动 HEAD 替换。
- 作者候选：commit `84e2cca132ada38405657f19cbbd3d6891d4794f`，tree `772d24ea3619989a0c97bd2c601f68f48a0b14c1`；作者分支 `codex/r7-u02-author-20261015-wave1` 只作身份记录，未 checkout 或修改。
- 基线 B：`e646432c644dec04d306842cc5a559a29c718fbc`；正式规格子树 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。参考 R：`Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，只核恢复文件，未重新认证参考整树。
- 本审者实际可见 `CODEX_THREAD_ID`：`01a13ff0-0f85-70d4-b48e-b15a4ba68038`。作者冻结外部标识和其 context.json 的实际 thread 均为 `01a13f7f-17e2-7472-80c4-d2b7eac2703d`，二者不同。父来源 thread 为 `01a13f49-a154-7054-9b04-ce31f924d01c`。未获另一个独立 task ID/opaque context ID，不编造等同映射；没有创建子任务或担任作者/R7-IR。
- 合同请求为 gpt-6.1-sol / ultra / default / 普通速度，禁 Fast；有效 model、effort、tier、speed 均 **UNVERIFIED**。环境 thread/PID、请求值和工具 exit0不认证模型配置；没有查询额度或认证。
- 已读实际 AGENTS.md；工作区、项目、固定 B/派发树及用户运行目录没有相关 `.agents/skills`，未套用无关技能。实际查找路径与结果列于输入回执。

## 恢复、原证据与写集

在本容器先完整读取固定 `658488c81f1f3181a488298ab27850c8af951d73` 的恢复工具及本批原清单，再恢复原合同/参考/反证到 `/workspace/r7-context/R7-U02-reviewer`：**33文件、21,406,782字节**。随后完整读冻结候选清单，用同一工具恢复到 `/workspace/r7-review-input/R7-U02-r1-84e2cca132ada38405657f19cbbd3d6891d4794f`：**63文件、1,088,679字节**。真实HTTP、UTC和结果见 [restoration](restoration/)。从未假定另一个容器的目录存在，未执行恢复出的作者、参考或native程序。

独立重新计算全部候选 bytes/SHA256/Git blob，并与冻结表、恢复清单和实际候选 commit/tree 的所有63叶逐一比较，全部为普通100644 blob。候选对B的完整差异恰63个新文件且仅在本批 candidates/；其中4份批准镜像与59份作者证据。作者manifest的62个显式成员另行全核；manifest自身由固定commit/tree及本审者完整表绑定。原33文件也全部重核；[binding-validation.json](binding-validation.json) 独立验证18处原始切片大小/哈希、JSON pointer及canonical哈希，并核51行作者向量与实际目录相同。以上均属TOOL_VALIDATION，不替代下述内容审查。

完整七组合同固定于 `f622356f3beb9e84ea8cff9db07c7fb382565d3f:review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U02.json`，94,049字节，SHA256 `55f05fe26ed94a036415bbca1fca9a5af5819a853e797522d54705cee5868715`。已逐项读三份七组，另读原非作者 C04 records/2、records/5，C08 challenges/3完整内容、原提案向量/依赖及D06晚到接收records/2。原成员位于已恢复的 C13 inputs/tasks/R7-P02/evidence/inputs/：C04 `88d6ae6f…raw`，C08 `2d7b2df0…raw`，根/原提案 `e0c5ebb2…raw`。接受C04/C08已缩窄合同，不复活原提案更宽断言。

完整差异独立比较结果：WP17只替换B L167、L266；其余字节相同；目录完整保留B前1026行，audit完整保留B前1844行，matrix完整保留B前569行。三者只追加本批内容。没有条件同步目标；不存在借同步采纳optional/policy的改动。51行新向量不增加27项/13批分母。

## 内容审查

### GR7-M04-301

独立读固定R `004_Input.rb` L1–31，Utilities L600–630，FileTests L1–60、L230–275，Audio_Play L190–230；结合B/WP65帮助全文及候选完整正文/目录核对。默认宿主更新先于F8沿查询；墙钟取时与命名在主保护前。目录检查/建立、主截图在有限保护内；主阶段可捕获错误才转一次同名宿主数据目录请求，回退解析/截图失败不重新捕获。正常捕获返回后才作音资源判据及完成音请求。

逐SS01–12核正常主路径/缺目录/资源假、目录检查与建立及主截图分别失败、回退解析与截图分别失败、取时及命名失败、同毫秒同名、无沿与无交互取消、完成音后项失败、不属捕获族的退出信号。候选保留目录/截图外部前缀且不承诺回滚，不把请求正常返回写成文件/像素/声音成功。原C04-SS-A–E映射完整。WP65帮助“与存档同一文件夹”仍是文案；鼠标守卫、其它别名与输入顺序未改。本项与紧急保存备份提示不是同一失败链，不新授全历史穷尽排重。

### GR7-M06-002

独立读ItemStorage共享普通/静态帮助/确认与其Bag、PC包装、精灵更新消费者，Party/Summary局部显示/确认和更新函数、通用消息显示完整函数与包装/普通及带帮助命令/自由文本出口。共享短文本A不忙时USE/brief返回，恢复可见后没有同一尾部输入请求；BACK不结束共享普通显示；共享确认BACK为No且无统一尾部。Party/Summary正常局部尾部同样不可补统一刷新。相反，通用消息正常收尾、普通/带帮助选项、自由文本及共享静态帮助均有显式请求；循环内刷新、可见恢复、窗口释放与输入刷新分别核验。

逐IN01–13覆盖原C04-IN-A–E及正常/取消、nil/缺commands未进入循环、空数组建窗、异常绕过后项、忙暂停四态和业务前缀。特别复核MG02–04、MG13–15、MG25/27/28、B04-M14、U06-M10-001-A–E、R6-U12-TS01–05；从固定R补取并读消息组件的忙/暂停、自动插入暂停和恢复范围，三行忙暂停不能冒作正常出口的反例。候选不宣称宿主绝不刷新或实际连按缺陷。

原GR6-O-002记录全文、B/WP13 §4.1与R6-EV01–06已读；具名补取固定R Interpreter L1–38/L78–150、Commands L1–45/L110–137/L500–513后核对：98/99/100条108注释加终止分别0/终止后1/终止前1次额外图形请求。116让出、更新调用重新计数、消息等待、图形请求抛错前缀及深度100/101分门保持。此为静态回归审读，未执行解释器或纸面向量。原canonical_candidate=null保持其生成时未指名资格，不伪造历史ID或全局唯一性。

### GR7-D06-001

独立对实际Game.exe字节读取PE节映射、两个完整指针表和21个实际NUL名称，9个具名范围与VA均匹配候选追溯。DB-0087真实样本含依序 `a:b0`、`misc1:b9`、后继 `rightshoulder:b5`；misc1不在15+6表。另用静态objdump完整读VA `[0x1403b2630,0x1403b2bb0)`：未知目标到0x1403b278e错误请求路径，不到普通追加；普通b源到0x1403b28e9/0x1403b28f9，分配失败0x1403b2979重置计数；外层0x1403b2a79调用后清字段缓存并继续。没有运行该PE。独立结果见 [binary-validation.json](binary-validation.json)。

逐DB01–05和BT01–15/AX01–06核此前成功接收、被审解析器被实际选用/物化、普通源与分配正常等前提；字段无交互取消，游戏BACK另层；未知字段局部继续不能推广所有失败保全部前项或全局回滚。候选不把错误请求写成显示成功，也不从a/back跨接游戏ACTION/USE/BACK。mkxp标签显示、WP17宿主查询/别名及WP65帮助/物理键未知保持。

原C08窄验收完整覆盖；D06-TV01由DB01承接，较宽TV02–05的平台、空字段、轴重叠及注册优先级不属已采最小合同，保留未签资格；TV06沿已有逻辑消费者合同，不授硬件桥证书。1666+257及731 Windows仅为既有工具结构计数，本审者未重做这些计数、不签全1923记录字段、76字段/48记录或优先级。晚到native premise只缩窄物化前提，没有改变本批必修范围。CC04真实注册/宿主查询桥仍NOT_READ，设备/后端验证仍NOT_EXECUTED；它们阻止更宽等价结论，不否定本次有限候选结论。

## 共享贡献与后续门

| 冲突组 | 本批贡献的可接收范围 | 仍未完成 |
| --- | --- | --- |
| CG01 audit/source-traceability.md | B前缀全保留，仅追加D06精确binary字节/VA、消费者和未读桥条款 | R7-I按条款保留U01/U10/U11/U12/U13等其它贡献，新R7-IR审实际累积结果 |
| CG06 UI目录 | 原1026行全保留，仅追加具名前提和51行U02向量；与U08按独立条款接收 | 未审U08当前候选或实际合入；不得用本完整镜像覆盖其贡献 |
| CG07 Feature Matrix | 一条F05-06有界提取行；旧状态与计数保持，不改全局分母 | R7-I保留其它各批行并完成实际接收/回归，不能以本候选PASS替代 |

三项均无具名作者阻塞入边；直接/传递record排程边为空不表示无领域或共享消费者依赖。R7-I串行条款整合、共享接收、独立新R7-IR对实际累积commit/tree审查、正式接受与精确历史/直接及传递回归接收仍OPEN。只有该后续链满足才可决定关闭；本审者不动公共台账。7 optional、2额外导航facet、1 no-required、2 policy未采用；旧56/92与27项/13批边界保持。

## 执行、日志与运输资格

本次SOURCE_STATIC/BINARY_DATA_STATIC/NATIVE_DISASSEMBLY_STATIC为有界内容审读；DERIVED_VECTOR为纸面预期核验。51行均NOT_EXECUTED；参考执行、REFERENCE_OBSERVATION、独立完整行为模型、游戏宿主、Demo、native媒体、真实存档/回放均新增0。Python恢复/身份/PE数据解码、git和静态objdump只算TOOL_VALIDATION。全部L01–L14已读并保留；没有用限制豁免可具名补取的Interpreter/消息组件依赖。

logs/001起保存审计命令真实argv/cwd、独立UTC、PID、完整可发布stdout/stderr及底层退出。早期侦察、fetch、源阅读和一次提取路径错误的工具I/O在平台记录中，未另外保存每条本地UTC/PID/分离流，不回填元数据；恢复器自己的逐文件HTTP回执原样保留。源代码/机器码阅读输出仅留本容器输入/平台I/O，不复制到公共规格或证据；私有模型流不发布。后续工具exit0不修补早期来源缺口，不升级运行或模型配置资格。

唯一成果分支 `codex/r7-u02-reviewer-20261015-r1`，独立worktree从固定B创建；只提交本r1下报告、回执、manifest及真实工具证据。不携带作者镜像，不写候选、正式、reference、main、tag或统筹分支，不force。最终完整commit/tree和普通push及完整远端回读绑定在本报告所属提交之外的最终回传，避免自包含自身哈希。所有非自身文件由artifact-manifest逐项绑定，manifest自身由实际提交tree与最后全文件远端回读绑定。

附：补充依赖的可选直接GitHub API元数据请求遭代理403，首次生成器exit1完整保留于logs/005；固定raw正文已正常恢复。随后用固定B追溯的两个blob及已连接GitHub在固定R返回的消息组件blob核对，logs/006生成成功。没有用403标记源不可读，也没有查询凭据、提升权限或把重试成功回填成首次成功。
