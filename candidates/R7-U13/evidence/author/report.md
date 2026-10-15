# R7-U13 作者隔离候选

状态仅为 **CANDIDATE_READY_NOT_REVIEWED**。本批 GR7-D07-001（required/P3）保持根 `REQUIRED_OPEN_FOR_MANUAL_UPDATE`；没有独立审查 PASS、ACCEPTED 或 CLOSED。本作者未创建其它作者/reviewer；完成交付后冻结，由 R7-I 核完整候选、生成 candidate-input.json，再交不同实际 context 的 ultra reviewer。

输入以用户指定提交 `6ec1d09e9c470954964d72761c83a760ef4f0364` 的完整派发为准；全文读取其引用的固定 `f622356f3beb9e84ea8cff9db07c7fb382565d3f` 七组合同和原作者入口。派发内较旧准备 hash 仅作历史元资料；原不提交/不推送限制仅由本次派发和用户授权覆盖。行为基线 B=`e646432c644dec04d306842cc5a559a29c718fbc`，仓库 tree=`84f79ec6e772aacbf3a464fde68cdc5a280e2950`，正式集合子 tree=`ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`；参考 R=`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree=`7589c800b61ba13a13040ed0d686979b80a84fd0`。这两种 B tree 的用途不同，没有把正式子树误作仓库根树。

从固定 B 创建唯一分支 `codex/r7-u13-author-20261015-wave1`；创建前本地/远端同名分支均不存在，原独立工作区 `work` 位于干净 B，只有一个 worktree。没有切换统筹工作树。四份完整镜像由 `git show B:<path>` 原字节建立，并与容器恢复的固定 B 文件逐字节比较；原 B/新 bytes、SHA256、Git blob 及精确 scope 见 [artifact-manifest.json](artifact-manifest.json)，可审差异见零上下文 [changes.patch](changes.patch)。该补丁用于审查，R7-I 仍须按 clause 整合。

本候选只做以下四项同步：

- WP15 §7 增加 MIDI 独立音色库静态声明及随附身份 `soundfont.sf2`；§10 增加对应依赖引用。轨道查找、声明、原生选择/读取/载入/接受、合成、发声分开；不选择未来 SF2、FluidSynth、宿主 API 或旧兼容配置。
- engine-overworld 测试目录在 B04-R01–28 后追加独立静态向量 `GR7-D07-001-S01`。原 28 行、顺序、标题和执行资格逐字节保留，包括 B04-R17 的广义六后缀/专门 SE 四后缀及字面路径区别。
- Feature Matrix 仅 F05-02 加待非作者核验及 R7-I 接收的静态声明候选注记，不提升历史批准、实际媒体或宿主状态。
- T-WP15-01 追加固定 R 的配置、定点脚本消费者及既有有限原生证据资格，不复制参考程序。Game.exe 本作者只核完整身份，读取原 C11 的具名有限 forward-map；没有把旧原生阅读算作本作者新读。

§11、F05-01 和所有其它正式/历史字节均未改。没有额外 conditional 写入，也没有采用 optional、两个额外导航 facet、no-required 或两个 policy。

恢复在本容器实际运行，未假定任何共享目录：`/workspace/r7-context/R7-U13-author/` 映射原 evidence/reference 路径。固定恢复工具与本批清单在读取后运行；首次 HTTPS 恢复 21 文件、16,814,642 字节，逐文件核 bytes/SHA256/blob。bootstrap 文本物化最初各多一个终止 LF，此差异没有改程序或计划字段；保留首次回执，随后按固定 Git 对象恢复精确工具/清单，再在原目录 `--resume`，21 文件全部精确复用且无新 HTTP。两次原回执、[bootstrap-integrity.json](bootstrap-integrity.json)、[recovery-command.json](recovery-command.json) 均保留，不覆盖恢复输入。

另按具名具体依赖定向恢复固定 C2 的 `tasks/R7-D07/findings.json` 和 `tasks/R7-C11/challenges/native/forward-map.json`，核压缩/解码身份；见 [targeted-recovery.json](targeted-recovery.json)。未读取80MB Manifest、未扫描完整 core 载荷或恢复全包；Git 分支取回不作为语义阅读证明。原七组、已接 C11 反证、根 `/records/30` 和晚到接收 `/records/3` 均按各自用途读取，旧 collector 对 C11 的误标不变成 D07 新作者变更。

完整读写范围和身份见 [read-set.json](read-set.json)。项目 AGENTS.md 全文读取；固定 B、指定准备提交和实际工作区均没有 `.agents/skills` 文件，workspace `.agents` 为只读空挂载，executor skills 列表为空，没有虚构技能已读。

逐向量纸面核对见 [per-id.json](per-id.json)：原 C11-V01–V08 和 D07-SF-CFG-01–06 保留原 ID、前提、预期和执行字段，另有 S01；15 个行为结果全部 **NOT_EXECUTED**。普通控制为正常系统、无默认覆盖、可查到 theme.mid、记录80/100、选项100；纸面只换 absent-bank.sf2 不推出静音、失败或成功。nil/空名提前返回不成为库初始化/释放/取消；缺库/坏库/字段缺省无效/guard/后端结果仍未知。

部分提交核对保留具体失败前缀：主 BGM 暂停位置12，恢复有效 B，首请求12出现参数错误，位置0重试再出现普通错误；B 已逻辑登记，paused 和保存12保持，后继 frame reset 与恢复清理未到达。没有统一回滚承诺，也没有把参数错误重试升级为 SF2 错误处理。缺轨道登记与普通 WAV 对照、默认覆盖、选项、暂停、记忆和时长规则保持。

仅运行传输/身份/文档生成与校验工具（TOOL_VALIDATION）；SOURCE_STATIC 与 DERIVED_VECTOR 分开。参考程序、Ruby、独立完整行为模型、游戏宿主、Demo、native媒体、合成、声音、真实存档回放新增执行均0。R7 历史收到的 H14/UTIL-03 局部 Ruby 观察仍保持其原范围，不改写本批或旧任务 NOT_EXECUTED。L01–L14、原 SF2 全结构/独立复算/配置审查事实、旧56/92关闭边界及固定27项/13批分母均保留。

实际作者 thread=`01a13f80-5248-7789-ab67-26ce7270c019`，父源 thread=`01a13f49-a154-7054-9b04-ce31f924d01c`，环境和实际工具进程 PID/UTC 见 [execution-context.json](execution-context.json)。请求 gpt-6.1-sol / xhigh / default / 普速禁Fast；实际 model、effort、tier、speed 各为 **UNVERIFIED**，没有用 argv、自报、退出0或环境ID认证配置，也未查询额度/认证。平台未暴露的 task ID、独立 context ID、模型进程 PID 不编造。

公开后继工具命令的 argv、真实 UTC、PID、stdout、stderr 和退出分别保存在 [commands.jsonl](commands.jsonl)。首轮候选生成因矩阵列数断言退出1，已保留原失败；修正工具后只复用完全匹配的三个部分镜像，完成第四镜像并退出0，没有覆盖冲突字节、没有触及正式文件。早期只读定位/读取的完整工具 I/O 保留在平台记录；没有伪造其未单独落盘的 UTC/stdout/stderr，也没有把参考程序正文复制到候选。最终提交自身的 commit/tree 和最终推送/远端读回尾部须由平台工具结果及最终回传绑定，避免自引用 hash。所有文件须进入候选提交，不能以容器绝对路径代替交付。

提交前暂存区检查曾因补丁文件的常规空上下文行包含单个空格而退出2，未产生提交；改成零上下文审查补丁后再次检查。原记录见 [precommit-check-failure.json](precommit-check-failure.json)，四份镜像内容不受此格式修正影响。

[validation.json](validation.json) 只记作者文档完整性/范围校验结果，不作独立语义验收。首次范围校验退出1，发现 §10 新依赖条目插在原标题前的空行之后，落到严格行锚点之外；已把同一条目移到 B L214 之前，保持原依赖和 §11 原字节，未放宽验证边界。该失败与修正保留。交付只普通推送唯一成果分支，并逐新文件从远端固定完整 commit 读取全部字节、比较 bytes/SHA256/blob；不 force、不合并 main、不移动 tag。首次候选推送/读回回执将作为后继证据提交保留，最终提交及逐文件远端复核由平台尾部回传。

仍待接收的门：CG01/CG04/CG07 由 R7-I 串行按 clause 整合，保护其它批次；实际候选须不同 context 的 ultra reviewer；整合实际字节须新的 R7-IR；直接/传递依赖和历史回归未满足保持 OPEN。L04 原生配置供应/分派以及 L09 实际读取、接受、guard、合成、声音仍 OPEN；旧已读有限材料不被抹去，不要求无限递归整 exe。作者完成候选后停止写入等待复审，不自行接受或关闭依赖。
