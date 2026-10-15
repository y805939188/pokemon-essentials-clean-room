# R7-U06 作者候选报告

状态：**CANDIDATE_READY_NOT_REVIEWED**。只提交隔离候选；不是独立 PASS、正式 ACCEPTED 或 CLOSED。作者工作完成后冻结，由 R7-I 接收真实 commit/tree、生成 candidate-input.json，再交不同实际 context 的 ultra reviewer；不在本作者 context 创建 reviewer 或签署接收。

## 固定身份与角色

- 用户指定入口：远端 `codex/remediation-seventh-20261015-cloud`，固定提交 `6ec1d09e9c470954964d72761c83a760ef4f0364`；已普通 fetch，FETCH_HEAD 完整等于此提交，并完整读取其 `delegation/parallel-dispatch/authors/R7-U06-author.md`。
- 原完整七组合同/原角色入口：`f622356f3beb9e84ea8cff9db07c7fb382565d3f`；恢复工具及清单：`658488c81f1f3181a488298ab27850c8af951d73`。完整合同共 1,837 行/86,072 字节，已分段读完，不能由精简入口替代。
- B：`e646432c644dec04d306842cc5a559a29c718fbc`；仓库 tree `84f79ec6e772aacbf3a464fde68cdc5a280e2950`；正式规格子树 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。四份完整候选均从 B 原字节建立。
- R：`Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，合同给定 tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；本次只恢复具名文件快照，没有认证完整参考 checkout/tree。
- 唯一成果分支：`codex/r7-u06-author-20261015-wave1`。创建前 HEAD=B、工作区干净、只有 `work` 分支、唯一 checkout，指定远端成果分支查询无结果；没有覆盖旧成果。
- 实际环境及 thread 见 `runtime-identity.json`。请求为 gpt-6.1-sol/xhigh/default 普通速度、禁 Fast；有效 model/effort/tier/speed 无平台回参，逐项 UNVERIFIED。source_thread_id 不是本次实际作者 thread。
- 已读项目根 AGENTS.md。项目工作区及固定 B/6ec Git tree 无 `.agents/skills`；`/workspace/.agents` 为空挂载。没有可读相关 SKILL.md，未虚构技能读取。

## 精确改动

1. GR7-M09-001：WP46 §3.1 围攻仅在实际普通基底求值时取并消费参与者；形态吸收仍计成功击，但不消费参与者。三连踢已有“每次基底求值加P”保留，只限定普通三次序号例并说明吸收不推进。普通无吸收序列、替身普通求值、业主资格、计划/成功击数、实际攻防、AI与固定伤害覆盖保持。
2. GR7-M10-001：WP49 §6.1.1 增加具名直接规则：本次计算类型火/水，实际本击目标列表，独立排除 unaffected/calcDamage0/替身，要求当下普通有效 STEAMENGINE及中央可升资格，自身来源请求速度＋6。保留附效/畏缩/减伤果后、再次濒死前的原时序，不添加模式破坏者或强行统一屏蔽。WP46 §2.1 只把既有时序名词改为该合同链接。
3. 两份共享测试镜像各新增独立小节15行；全部30行均 DERIVED_VECTOR／NOT_EXECUTED，逐项见 `per-id.json`。两份目录所有原行和顺序按字节保留。
4. 条件 WP43 **未建立镜像、未修改**：原 §6.2 的 C1 早返已正确，没有必须同步以消除的具体矛盾。不复活可选提案，不改矩阵、追溯公共表或任何正式文件。

机器可读原B/新bytes、SHA256和Git blob见 `artifact-manifest.json`；具体原始行位置与插入区间见 `scope-validation.json`，完整有界diff见 `changes.patch`。WP46只替换B第23/54/59行；其它三份镜像仅插入新小节。

## 本容器恢复与阅读

先完整读固定恢复工具和本批清单，再执行原命令，恢复36文件/7,536,934字节；同目录 `--resume` 全部复用精确字节。原HTTP回执和复用回执分别保存；没有假设整合者共享目录，没有操作Mac、执行恢复参考程序或读取80MB Manifest。

作者校验继续遍历规范化记录12/13的原绑定时，命令005因缺 source inventory 原载荷退出1。定向识别并补取4个已具名原位置：formal/source inventory、M09原finding快照别名、M10原finding。绑定、C2精确对象路径、编码/解码身份及真实HTTP/复用结果见 `supplemental-plan.json`/`supplemental-receipt.json`。恢复不扩大语义阅读信用，也没有把可读缺项冒称limit；首次失败I/O保留在 `commands/005-validation.json`。

累计40输入位置/7,928,224字节，按bytes/SHA256/blob逐项核对；其中M09别名不构成新增独立证据。262处引用（含重复）通过原载荷字节范围、字节SHA、JSON pointer和canonical SHA核验。源/正式精确阅读范围及身份见 `read-set.json`；它区分全文已读、具名范围已读和仅恢复身份。

已完整阅读两记录原七组、C01/C05实际非作者反证成员、根中原提案及全部接收向量/依赖/阶段；保留已被反证排除的范围。源阅读为SOURCE_STATIC，不借原作者检索证明全库语义缺失或历史全域完整性。

## 验证结果与四路径

- 命令007：40文件、262处原绑定、4完整镜像、30新增静态向量，范围与原行保留检查完成，exit0。它是TOOL_VALIDATION，不是行为或独立语义验收。
- 命令012对随附统一diff的空上下文标记报尾空格，exit2；将证据diff改成合法零上下文统一diff后重新校验，未修改候选正文。原失败完整保留。
- 命令009以 `git diff --check --no-index /dev/null <新增报告>` 返回1且stdout/stderr空；这是no-index有新增差异的底层退出，不用它冒称检查成功。后续以暂存区 `git diff --cached --check` 单独核验。
- 命令008：独立常数算术核14/6、10/20/30、水例6→18→HP82、阶级−4→＋2、＋5→＋6、原速35的70/140。没有重建处理器、运行状态模型或执行向量。
- M09正常/对照：BU吸收后第二基底14、无吸收14/6；TK吸收后10/20、无吸收10/20/30；替身从已破形态对照出发，仍普通求值。基底不等同最终伤害/真实HP损失。
- M09取消/失败/部分提交：上游取消不建立使用；首击/后击失手、吸收后U倒下/真睡/真冻/唯一目标倒下各自停止；反馈/宿主错误仅保留已到吸收/形态/HP/PP前缀，不回滚、不补击、不保证继续。
- M10正常/对照：火/水独立、HEATPROOF对照、非火水及合法本次变类型、替身/unaffected/calcDamage0/胃液/气体/已倒下各自门、−4/0/＋5/＋6、两击重查、模式破坏者和合法强行火招独立对照。calcDamage0仅条件化直接入口，不冒称普通正伤害可达；不造同时蒸汽机/单纯/唱反调。
- M10取消/失败/部分提交：更早取消或错误不补升阶；速度写点前后分别保留已到PP/HP或已写阶级，不把消息/exit0当业务成功；没有真实故障注入或宿主恢复观察。

REFERENCE_OBSERVATION、参考Ruby、游戏宿主、Demo、native媒体、真实存档回放、完整独立模型本任务均0。原R7整体H14/UTIL-03既有1进程/10输入的历史局部执行仅保原资格，不是本任务新增。L01–L14、旧56/92关闭边界、27项/13批分母均保持。

## 未满足的接收门

作者排程阻塞入边为空，作者候选没有剩余内容阻塞；这不表示无领域/历史依赖。两项候选独立review、共享语义owner/目录接收、R7-I逐clause串行整合、新R7-IR实际整合复审及根正式接受/关闭全部未到达、保持OPEN。M09跨消费者/WP43/WP46与历史去重、M10中央阶级/速度消费者/WP46/WP49责任及完整早期历史资格均不由作者关闭。没有继承历史PASS或重开旧问题。

本角色按完整派发“只执行本次具名角色，不创建子任务或其它作者/reviewer”及完成后等待ultra复审执行；用户授权复审不等于授权作者自行签独立PASS。

## 工具与发布证据

`commands/`逐命令保存真实argv、UTC、工具子进程PID、完整stdout/stderr和底层exit；`runtime-identity.json`独立保存请求/实际资格；不上传私有模型流。初始侦察/分段读取经平台工具回执完成，未独立落盘每次UTC/stdout/stderr；`initial-provenance.json`保留真实可见回执与这一缺口，不补造历史日志或作者模型PID。该审计限制交R7-I保留，不能用后继exit0抹去。

发布仅普通提交和普通push至唯一成果分支，逐新文件以完整固定commit的GitHub raw URL读取全部字节，另核远端ref与commit/tree。最终commit不可能包含其自身发布后的回执：首次发布的完整回执可随证据后继提交；最终commit/tree及最终全部文件读回结果在包外工具回执/最终回报绑定。`artifact-manifest.json`不自含自身哈希；完整Git tree与最终逐文件读回覆盖它。完成最终读回后停止候选写入，等待R7-I/独立ultra复审。
