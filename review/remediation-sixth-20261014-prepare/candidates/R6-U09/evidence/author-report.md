# R6-U09-A 作者候选交付

三项必修已完成实际规格修订，状态为 **REVISED_CANDIDATE_PENDING_NON_AUTHOR_REVIEW**。本报告是作者的有限静态核对；没有签发 CANDIDATE_PASS、INTEGRATED_PASS、正式接受或 CLOSED。独立 ultra 审者由父线程另派；唯一正式整合者按最新用户指令为 thread `01a13a93-d1da-71e4-a488-63b8524f503d`。准备文件中的旧整合入口保留原历史时点，不替代最新分工。

实际工作根 `/workspace/pokemon-essentials-clean-room`，作者分支 `codex/remediation-sixth-r6-u09-author-20261014` 从准备提交 `469a268b92daed7b4d28d7fd0da75520cbb7228f` 创建。正式输入 main 为 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，正式目录 tree 为 `1046fbb657882e84b3dfc6d017943a9edf7782e5`；R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree 为 `7589c800b61ba13a13040ed0d686979b80a84fd0`。候选 C/P 的最终提交和目录 tree 由真实发布回执及最终响应外部绑定，本报告不预填未知对象。

请求配置为 gpt-6.1-sol / xhigh / default tier / default 普速，Fast=false。平台未提供有效 model/effort/tier/speed/任务 UUID 回显，因此实际值均 **UNVERIFIED**。依最新授权直接完成作者工作，没有启动 CLI 或额外代理证明模型，也没有追查认证/私密配置。初次工具活动的 UTC 未独立本地捕获；首份本地记录为输入检索的 `2026-10-14T13:59:30.362520+00:00`，不倒补为会话启动时间。

## 输入与阅读

适用根 AGENTS.md 已全文阅读。完整作者合同 3552 行按结构分段读完，227242 bytes / SHA256 `b21be4d214a9d157f0526122981669ea72fe0c39e534aff8376a00f7538b5c0b` / blob `500382c78bf7d13b1383f8ba3b7fe8f1997a9abf` 校验相符；其完整嵌入 JSON 经解析与独立 `contracts/R6-U09.json` 相等。完整原提案、逐 ID 原裁决、独立 `counter-B-compiler.json` 1075 行和相关调用检索证据已读；不是以检索或 hash 替代正文。

7 份正式输入均全文读完。四份 Compiler 文件分别 1117/1321/821/1751 行全文新读，StartGame 126 行与 MiscPBSData 64 行全文新读；菜单/分派、连接辅助与消费者、地区图鉴编辑器、区域查询、动画播放的完整具名上下文另读。WP73-A 140–153 是只读保存 Yes 控制。范围、载荷身份和记录在 [author-reading.json](author-reading.json)、[reading-ledger.jsonl](reading-ledger.jsonl)、[input-manifest.json](input-manifest.json)。原始 prompt/行政/历史阅读的早期 stdout 留在平台工具记录，未另捕获的 UTC/退出元数据不伪造。

本环境没有准备中指定的 `/workspace/pokemon-essentials-reference-r6`。R 固定原字节先由已提供 read-frozen-input 工具取至 `/workspace/r6-input-cache/frozen-payloads/`，随后正常 shallow fetch 固定已发布 R 到只读对象缓存 `/tmp/r6-u09-reference-objects.git`；12 个实际用到的源 blob 全部与先前原字节相等，commit/tree/path/mode/blob 均核定。历史 Mac 根映射到上述云端根，未操作 Mac，未扩大正式写集。新 literal `compile_all`/`pbClearData` 检索只涵盖固定 R 的 tracked `Data/Scripts` 文本；不声称动态/原生/插件调用不存在，也不声称对全部432材料进行了本作者语义全文重读。

## 逐 ID 修订与静态验收

完整七组实录见 [finding-responses.json](finding-responses.json)，逐组展开身份裁决、双向源/规格接合、前提/反例、最小修订、验收/历史回归、独立裁决状态及接收依赖，绑定每份源/候选载荷。

| ID / 原分类 | 实际规则修订 | 有效反例与正常/边界对照 | 新目录行 |
| --- | --- | --- | --- |
| R6-DX-COMP-001 / required P2 | WP04、WP75 区分启动检查与运行中直接内容阶段；WP72 同步实际菜单阶段、完成及释放门。直接入口不取得启动缺目录反写、导入/mtime/预删及局部异常诊断/清理/转换。 | 完整兼容工程、PBS/旧档案有效、先行阶段正常；Status/Power40 在条目校验失败，早期档案新、moves.dat 旧、当前表可有前缀，坏条目未登记；完成/释放未必到达。启动同态仅诊断正常返回才进入异常后删除尝试。未登记 Map007 在直接入口不导入，999排除另列；全合法直接流程正常收尾是独立静态对照。 | KL37–39；DXCOMP-C01–03。KL02/03 仅修前提为启动，原结果不改。 |
| R6-DX-COMP-002 / required P2 | WP04/WP75/WP72/WP62 明确区域磁盘、缓存查询和反写三观察点；WP74 编译缓存行改为不清既有集合/关联。WP04 两处动画写入摘要统一至既有 WP74 的有效条目门。 | 已预载区域 A=[BULBASAUR]，合法作者 B=[IVYSAUR]、两物种已定义、全阶段成功、无独立失效：编译档案 B/查询 A，导出 PBS A/档案仍 B。缓存未建立、编辑器 Yes/No、新临时会话数据、独立连接清理/新进程分别观察；新 Game_Temp 不清独立连接缓存。有有效动画写新磁盘而两缓存仍 A，与零有效条目保留旧磁盘 M 不同。Reload 仅证明宿主请求。 | KL40–45；DXCOMP-C04–08。 |
| R6-DX-COMP-003 / required P3 | WP04 增加首列注释/纯空白/行内注释/缩进独立注释的解析家族边界及失败前缀。 | 合法唯一普通类型 A/B，无早期错；B 内一个 ASCII 空格接 # note：A 已登记，B 未交付登记，终检/整表保存未到。首列 #、纯空白正常；前首节为缺少初始节错误；合法专用 Trainer 同行可略过。旧 Name/q 井号后缀与引号不保护规则保留；不推断随附语料数量或全部 PBS 家族。 | KL46–50。 |

所有新行为案例均为 **SOURCE_STATIC 支持的 DERIVED_VECTOR / NOT_EXECUTED**。没有执行 R 原函数/回调、完整独立行为模型、完整宿主、Demo、真实用户存档或生产服务；当前作者各执行数均 0。没有未知 Marshal/eval、EXE/DLL/loader 执行，没有引擎实现或参考源码修补。

## 保留与工具验证

[static-validation.json](static-validation.json) 的 198 项有限检查全部 OK，33 个本地链接目标存在；[static-check-4.json](static-check-4.json) 独立捕获 argv/cwd/UTC/stdout/stderr/exit=0。检查包括冻结身份、7份准备镜像原为 baseline、只改本批 allowlist、正式 deliverables 未变、diff --check（排除统一差异文件的空行上下文标记）、旧向量原结果、具名历史段落保留与 JSON 解析。它们是 TOOL_VALIDATION，不是行为运行或独立审查。

精确保留项包括 WP04 启动发现/整数 mtime/异常表、分词/schema、遭遇专用解析/概率往返、指标布局/写出、进化与电话身份/默认/井号往返；WP74 原命名、零有效写入门、播放回退、交换/保存、SC-U07-001 LF纠正；WP75 原事件转换、门/出口、脚本数量守卫与 B20-C024 往返；WP62 原记录写入/身份/解锁/展示刷新；WP72 原调试入口与全部效果表。原 Demo 测试目录327行是完整字节前缀保留；内核旧向量除 KL02/03 前提范围收窄，其余行原字节保持。

R1原WP资格、R2 229/21/341、R3 23/76、R4 17/76与B5 16/75、R5唯一 activation 所选92 CLOSED原精确范围均保留，不扩大为整文件/领域/宿主通过。相关 R5-U07 所选7条资格元数据、001–004 准则及 SC-U07-001 原纠正已读；新核对只覆盖本次实际受影响段与消费者。[history-selected-bindings.json](history-selected-bindings.json) 保留原时点 OPEN/拟关闭字段，不重新打开已激活第五项。[history-hash-input-contract.json](history-hash-input-contract.json) 的内容实际是 GR5-M01-002 本地化默认消息材料，不用文件名把它充作 PBS 井号旧验收。精确整合后的独立历史回归仍待接收者执行。

原失败尝试保全：初次在 clean-room origin 混合取准备/main/R 的 fetch 失败，随后固定准备与 R 正确来源取得成功（早期 fetch 原 stdout/退出在平台记录，未补写本地 UTC）；source-tree-query 第一次因缺 commit 字段在联网前失败，retry-1 API被代理403阻断，随后已授权 Git 固定对象 fetch/完整 blob 比较成功；static-check-1 因 formal 输入缺 commit 字段停止，修正输入元数据继承后 static-check-2 为0失败。static-check-3 将已提交的统一差异文件的空行上下文标记当作文本尾空白，exit=1且独立差异检查exit=2；限定排除该证据格式后static-check-4对真实规格和其余文件检查为0失败。对应文件不删除、不把失败倒写为成功；均未执行参考行为。

## 精确写集与接收

本批只改 `candidates/R6-U09/mirror/` 下以下正式路径及自己的 `evidence/`；[candidate-files.json](candidate-files.json) 展开每份 baseline/candidate 的 bytes/SHA256/blob，正式源文件保持原样。

| 正式相对路径 | 本批接合 | 其它共享作者 |
| --- | --- | --- |
| demo-dx/wp72-debug-contexts-and-controls.md | §8.3 三行 | U08 |
| demo-dx/wp74-battle-animation-authoring-and-exchange.md | §15磁盘门；§16编译缓存/消费者 | U07 |
| demo-dx/wp75-project-conversion-and-authoring-tools.md | §3.1；§4入口；§16.1 | U06 |
| generic-kernel/wp04-pbs-lifecycle.md | §2/§3；§4.2；§5缓存与接合；§6/§9 | U14 |
| pokemon-rules/wp62-pokedex-records-regions-and-content.md | §5.1内容缓存与查询/反写 | U01、U11 |
| test-catalog/demo-dx-wp72-73-74-75-76-77.md | 仅尾部追加8行对照 | U06、U07、U08 |
| test-catalog/generic-kernel-wp02-03-04.md | KL02/03范围；追加KL37–50 | U14 |

作者准备没有跨批阻塞依赖。R6-I 必须接收所有相关候选的具体差量，避免拿本镜像整文件覆盖其它作者；共享文件收齐后做独立全文回源、直接/传递接口和精确历史回归。本作者未写原 deliverables、公共 ledger/task-register、别批目录或旧证据；未移动 main/delivery tag、force push、删分支/tag、merge main 或释放环境。

剩余状态：独立候选 ultra 审查、唯一写者实际整合、共享全文独立审查、接口/历史整合回归、正式接受与 CLOSED 登记均待办。宿主错误 UI/可见播放/隐藏 Reload 副作用继续未知；这是原执行边界，不阻塞已完成的有限静态修订。无新增实质作者阻塞，也未把 optional/policy/limit 扩为必修。
