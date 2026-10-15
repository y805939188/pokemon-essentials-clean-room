# R7-U08 作者隔离候选

状态：**CANDIDATE_READY_NOT_REVIEWED**。本交付只提供四项必修的候选字节；不作独立 PASS、ACCEPTED、CLOSED 或正式接收。完成发布及读回后停止写入，等待统筹冻结输入及不同实际 context 的 ultra 复审。

固定派发输入为远端 `codex/remediation-seventh-20261015-cloud` 的 `6ec1d09e9c470954964d72761c83a760ef4f0364`，已真实 fetch；派发入口全文及 `f622356f3beb9e84ea8cff9db07c7fb382565d3f` 的四记录完整七组合同均已分段读完，不以摘要代替。基线 B 为 `e646432c644dec04d306842cc5a559a29c718fbc`，正式目录 tree 为 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`；参考固定 R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。派发内较早准备提交只是历史定位，实际入口按用户指定 6ec1d09e 读取。

唯一成果分支为 `codex/r7-u08-author-20261015-wave1`，从 B 创建。创建前已核工作树干净、原分支 work、同名本地及远端分支不存在。全部相对 B 的新增路径只在 `candidates/R7-U08/`；正式文件、公共台账、旧证据、main、tag、reference 均未写入。

## 精确贡献

| 必修 | 候选变更 | 保留控制 |
| --- | --- | --- |
| GR7-M13-001 | WP67-A 原 L247：用当下显示 HP h 与整数总量的向下取整阈值选色；目录在原 K35 后新增 R7-U08-HP01–04 | 1 秒补间及等待、Off 仍播放、实际 HP 先提交、数字单独取整、比例宽度及偶数舍入；不扩到队伍/摘要条或图标 |
| GR7-J16-001 | WP67-B 原 L141 一句：基础准备正常后，非空 BGM 先请求并正常返回，再登记；记录先于逐成员视觉 | 克隆及默认蛋收录、正/负/0 上限、每次只删一届、编号/PC 门、无取消/自动保存/片尾；L22 不改 |
| GR7-J16-002 | WP67-A 原 L196/L248 仅“闪白→闪光”两处 | 1.75 秒比例、满槽名义 0.2 秒、音效及等待、经验先提交和逐级顺序、无条立即完成、Off 仍播放；不追加 RGBA 或像素断言 |
| GR7-J16-003 | 目录原 L440（候选 L444）仅收紧 L13 后续：统一净化返回后存放、存放正常返回后清中心、尚有下一组才询问 | L15–L19 全部原字节；双满提示正常返回仍清中心；WP23/SH38/39/43–45 不改，不新增领域根因或兼容政策 |

三个目标均以 B 的 Git 原字节建立完整镜像；其余行逐字保持。精确补丁在 [changes.patch](changes.patch)，逐镜像旧/新 bytes、SHA256、Git blob 在 [artifact-manifest.json](artifact-manifest.json)。原 K22/K35 不改；新增 HP 行属于 M13 必修，而非经验闪光项的扩大。

## 容器恢复与实读

已先阅读实际根 AGENTS.md。当前项目和工作区没有适用 `.agents/skills`，B 也无该跟踪目录，未声称读取不存在的技能。按指定固定工具及批次清单恢复到 `/workspace/r7-context/R7-U08-author`，不假设与父容器共享目录；39 文件、7,698,787 字节逐项核大小、SHA256、Git blob，三个重复逻辑提案路径也分别核实。恢复只是有界快照，并非完整参考 checkout 或语义验收。

完整恢复收据随本目录提交；[input-identities.json](input-identities.json) 绑定固定原件及来源，[reading-ledger.json](reading-ledger.json) 逐项登记实际范围。WP67-A、WP67-B、UI 目录均全文读完；按合同实读源及必要消费者、WP23/SH 的旧回归。C04 原始裁决成员已按精确字节区间实读，C14 三项反证已读。六个原始 offset/length/hash/JSON pointer 引用已核。经验驱动用实际 283–293；旧 234–254 错定位只保留为历史，不作支持。

## 验证与资格

[per-id.json](per-id.json) 给出每项完整前提、普通对照、取消/拒绝、异常、部分提交、必要读写集及全部 17 条具名向量。四条 HP 纸面结果为：T101 的 50.5 绿/50 黄、25.25 黄/25 红；T100 与 T101 静止整数、数字开关及 Effects Off 另列独立对照。HOF4、EXP4、PURIFY5 同样保留原给定观察点。

**全部行为向量 NOT_EXECUTED。** 本作者仅作 SOURCE_STATIC、DERIVED_VECTOR 和文档身份/边界 TOOL_VALIDATION；参考执行、独立完整模型、游戏宿主、Demo、native 媒体、真实存档回放均为 0。没有通过 Python 模拟参考行为；[verify_candidate.py](verify_candidate.py) 只核文档差异与身份。命令 024 校验精确修改位置及其余原行；正式字节不变。哈希匹配和 exit0 均不替代语义验收，也不改变 R7 已有 UTIL-03 局部执行的独立口径。

领域 HP/经验或净化前缀可以已提交，表现失败不自动回滚。HP 与经验组件没有独立取消；外层 BACK 分开。HOF 请求不返回时未到登记；EXP 的 SE/某一子精灵失败不保证剩余交付；PURIFY 跨级失败在首窗，未到精确经验尾写/存放/清中心，同级 S0、遗迹石、下一组拒绝及双满正常返回各按原合同。不得据此保证资源、错误窗口、退出、补画、清理或宿主成功。

作者请求 gpt-6.1-sol / xhigh / default 普通速度、禁 Fast；有效 model/effort/tier/speed **逐项 UNVERIFIED**，无有效配置回参，未查额度/认证。实际选定环境及 `/root` context、可见来源线程、真实工具 PID/UTC/退出见 [execution-context.json](execution-context.json) 与 commands；父线程 ID 不冒充本作者平台 task ID。实际作者平台 task/context UUID 未暴露，须 R7-I 用真实派发回执绑定。

审计记录从 audit.py 建立起保留完整可发布命令 argv/stdout/stderr/退出及 UTC；更早 bootstrap 的本地分流日志缺口明确保留，不倒填。命令 025 在已完成六个字节引用核验后，因把 list 当 dict 检查而 exit1，原输出/错误完整保留；026 修正读取并成功，失败记录不算完成阅读。平台曾截断 007 的一小段，022 已按真实范围补读；恢复出的参考程序从未执行。

全候选 `git diff --cached --check` 会报告原始 stdout 的行号后空格和补丁上下文空行；这些是保全的真实 I/O/补丁字节，未为消除格式提示而改写。三镜像及手写报告/JSON/校验脚本的限定 whitespace 检查 029 退出 0；不把全候选原始日志检查描述为通过。

## 待接收及发布

作者无前置阻塞批次，但仍有接收门：R7-I 逐文件接收、生成 candidate-input.json 并绑定真实 author task/context；另一实际 context 的 ultra reviewer 审冻结候选；R7-I 按 CG06 逐 clause 串行整合；新的 R7-IR 审实际整合字节；直接/传递消费者及历史回归满足后才考虑关闭。未满足者保持 OPEN。L01–L14、旧 56/92 关闭边界、27 项/13 批分母均不变；7 optional、2 导航 facet、1 no-required、2 policy 均未采用。

按后继派发授权普通提交、普通推送唯一分支，并对每个新增文件从完整固定远端 URL 读回。发布证据以真实 Git commit/tree、远端分支回参及逐文件读回结果为准；最终 commit 的自身读回由平台末次工具输出及最终回传绑定，避免制造自引用哈希。候选提交不得整分支合并进正式目录。
