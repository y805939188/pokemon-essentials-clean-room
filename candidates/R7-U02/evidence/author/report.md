# R7-U02 作者候选

状态：**CANDIDATE_READY_NOT_REVIEWED**。本容器已按三个必修的最小合同完成四份固定 B 全镜像及作者证据；未作独立 PASS、正式接受或关闭。候选完整 commit/tree、普通推送及逐新文件远端读回，以最终包外回传绑定为准，避免提交自包含自身哈希。

## 固定输入、角色与权限

- 用户指定远端派发提交：`6ec1d09e9c470954964d72761c83a760ef4f0364`，输入分支 `codex/remediation-seventh-20261015-cloud`。已取得该固定 Git commit/tree，并完整读作者入口；入口内部的旧准备提交标签按历史保留，不替代用户固定提交。
- 完整七组合同：`f622356f3beb9e84ea8cff9db07c7fb382565d3f:review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U02.json`，94,049 bytes，SHA-256 `55f05fe26ed94a036415bbca1fca9a5af5819a853e797522d54705cee5868715`。三项七组逐项完整阅读，另完整阅读 C04 records/2、records/5 和 C08 challenges/3，不以精简入口替代。
- 行为基线 B：`e646432c644dec04d306842cc5a559a29c718fbc`；正式规格子树：`ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，本容器只恢复有界文件，未声称重新校验参考整树 `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 唯一成果分支：`codex/r7-u02-author-20261015-wave1`，从 B 新建前已检查本地和远端无同名成果。初始 checkout 为独立 `work` 分支、干净且 HEAD=B，没有切换统筹工作树。
- 实际 context/thread：`01a13f7f-17e2-7472-80c4-d2b7eac2703d`；父来源 thread：`01a13f49-a154-7054-9b04-ce31f924d01c`。平台未给额外 task/context ID，分别记 UNAVAILABLE，不用线程 ID 冒充不同身份；工具子进程真实 PID/UTC/退出另在 logs。
- 请求配置：gpt-6.1-sol / xhigh / service_tier=default / 普通速度，禁 Fast。有效 model、effort、tier、speed 四项均 **UNVERIFIED**，无权威实际回参；不查认证或额度，不用请求或 exit0 认证配置。
- 已完整读实际项目 AGENTS.md。项目、固定 B/派发树及可用 workspace/用户运行目录未找到相关 `.agents/skills`；未套用依赖库内无关技能。未创建子任务、作者或 reviewer。

## 恢复与身份

先完整阅读固定 `658488c81f1f3181a488298ab27850c8af951d73` 的恢复工具、本批清单和跨容器说明，再按派发指定路径执行恢复。结果：**33 个逻辑文件、21,406,782 bytes**，全部核大小、SHA-256、Git blob；原证据、固定正式/参考输入、原合同/Prompt 均在本容器重新取得，没有假设共享目录。实际 HTTP 与 UTC 见 [context-recovery.json](context-recovery.json)。

二次独立工具读取恢复字节，核 33 文件身份、18 处成员原始切片/JSON pointer/规范哈希绑定、15 个按钮及 6 个轴名指针。Game.exe 仅有界读取数据与反汇编；没有启动该文件、参考 Ruby、原生程序、宿主或行为模型。恢复、哈希、指针与文档检查只属于 TOOL_VALIDATION，不是语义批准。

前两次未过滤 Git 抓取因载荷较大未完成，分别主动终止；第一条复合 shell 的最终 exit0 来自后继 ls，不能当 fetch 成功，保留 early EOF/对象缺失；第二次退出 143。随后 `--filter=blob:none --depth=1` 从 origin 取得用户指定固定提交成功。没有覆盖/删除任何已有成果。

## 三项精确贡献

| 必修 | 候选贡献 | 必要静态向量 |
| --- | --- | --- |
| GR7-M04-301 | WP17 §6.1：墙钟日期/时分秒/毫秒 PNG 名、相对 Screenshots 主请求、一次同名宿主目录回退、命名前置/可捕获族及回退传播、正常捕获后条件完成音；无沿/无取消、同名及部分前缀均明确 | R7-U02-SS01–12；对应原 C04-SS-A–E，并分别列目录/主截图失败、回退解析/截图失败、命名失败、音效失败前缀 |
| GR7-M06-002 | 只替换 B 的 WP17 L167、L266 两处全称出口说明；通用消息/普通与带帮助选项/自由文本及共享静态帮助与共享普通/确认、队伍/摘要局部显示/确认分开，nil/缺命令不套循环出口 | R7-U02-IN01–13；对应原 C04-IN-A–E，保留循环刷新、忙暂停四态、异常边界及正确 GR6-O-002/R6-EV01–06 |
| GR7-D06-001 | WP17 §6.1 增有限目标名与条件字段处理资料；UI 目录增 a/misc1/后继、21 名、分配失败/取消/桥边界；audit 新增精确字节/VA 追溯；Feature Matrix 仅一行 F05-06 有界贡献 | R7-U02-DB01–05、BT01–15、AX01–06；DB-0087 后继实际为 rightshoulder:b5；不采纳宽注册优先级/设备等价主张 |

共 **51 行 DERIVED_VECTOR，全部 NOT_EXECUTED**，不是新增 51 个本轮问题。每行前提、静态预期、执行阶段和非作者待审在 [per-id.json](per-id.json)；原向量对应关系、正常/取消/失败/部分提交、精确读写集、未满足依赖同列。不存在本轮新增游戏/宿主/Demo/native媒体/真实存档回放/独立完整模型执行或 REFERENCE_OBSERVATION。

正文全镜像由 `git show B:<path>` 原字节建立并与恢复快照逐一比较。WP17 只在 B L167 添 F8/手柄有界资料并替换刷新全称、B L266 替换另一全称；其它原字节保持。目录、audit、Feature Matrix 均为 B 全字节前缀加本批有界内容，全部旧案例/历史记录保持。条款级完整差异以零行上下文补丁保存，见 [clauses.patch](clauses.patch)，逐镜像原 B/新 bytes、SHA-256、blob、变更行范围见 [mirror-identities.json](mirror-identities.json)。统筹须按条款串行整合 CG01/CG06/CG07，不得整文件覆盖其它作者。

## 校验与证据资格

[validation.json](validation.json) 记录作者工具检查：四镜像边界、三文件完整 B 前缀、WP17 两处最小变更、21 名与固定指针表一致、51 行全部未执行、正式文件无改动、正式子树保持 B。正常控制、WP17 §3.3.1/§7.3 原异常段与全部旧目录行保持原字节。没有把来源定位检索当全文语义阅读；大索引/目录虽全字节纳入镜像和身份检查，仅相关条款作本次语义阅读，全部无关历史行没有新签署。详见 [source-read-ledger.json](source-read-ledger.json)。

当前公开 audit 命令由 run_audit.py 保存真实 argv/cwd/PID、分离 UTC、完整 stdout/stderr 与底层退出；初始侦察/阅读的工具 I/O 留在平台，但未各自保存本地独立 UTC/PID/分离流，**不回填这一来源缺口**。源代码/机器码阅读输出与私有模型流不复制到公共证据；可发布的是精确身份/定位、行为观察和审计工具 I/O。首次全文件空白检查 exit2 仅命中补丁的标准空白上下文行；已改为零上下文补丁。后继检查又命中首轮原始诊断流本身的空白；这两次失败的 stdout/stderr 原字节均以 base64 无损保留，不删除失败记录。最终检查另计。固定派发全文的只读 Git 回读在 logs/004-fixed-dispatch.stdout，保留原入口与新授权的可复核文本。

## 保留 OPEN 与下一门

- 非作者 ultra 候选复审尚未开始；本作者不得自行创建或冒充该复审。R7-I 须先核 commit/tree、完整差异及逐文件身份，再冻结 candidate-input.json，交不同实际 context 审候选。
- R7-I 对共享文件逐条接收/串行整合、之后新 R7-IR 对实际整合字节复审，以及精确历史/直接与传递消费者回归接收，均 **OPEN**。本批无作者阻塞入边，不等于没有领域依赖。
- CC04 实际注册/宿主查询桥仍 NOT_READ；真实设备/后端未验证；全 1923 记录字段语义、76 字段/48 记录和注册优先级无本独立签署。1666+257、731 Windows 保持旧 TOOL_VALIDATION 结构计数；源有限词汇不强制未来厂商库/架构/缺陷兼容。
- 原 canonical_candidate=null 不补造历史 ID；正确解释器防冻分支及旧台账不改。帮助文本、鼠标/输入顺序、业务前缀、L01–L14、旧 56/92 关闭边界及本轮 27 项/13 批保持。7 optional、2 导航 facet、1 no-required、2 policy 未采用。
- 仅普通 push 到唯一成果分支；不写统筹分支/main/tag/reference/正式文件/公共台账，不 force。完成最终远端逐文件全字节读回后冻结，等待 ultra 复审；候选 PASS、整合 PASS、ACCEPTED、CLOSED 各门未到。
