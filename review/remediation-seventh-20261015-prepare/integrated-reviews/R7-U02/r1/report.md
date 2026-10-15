# R7-U02 r1 独立实际整合复审

GR7-M04-301、GR7-M06-002、GR7-D06-001 均为 **PASS_SCOPED_ACTUAL_INTEGRATION**。结论仅覆盖固定 MI 的这三项有限静态合同、相应向量及本报告列明的共享保留/消费者相容性；不是其它必修或整体运行等价结论。本审者不登记 ACCEPTED 或 CLOSED。

审者实际环境回显 `CODEX_THREAD_ID=CODEX_SESSION_ID=01a1401b-eec4-72eb-800e-6ff904adc009`，与派发排除的所有作者、候选审者、R7-I 和先前实际审者标识不同。来源 thread 为 `01a13f49-a154-7054-9b04-ce31f924d01c`；额外 opaque task/context ID 未暴露，不用 `/root` 或工具 PID 推断身份。没有创建任何子任务、辅助 agent、子会话或模型调用。请求 gpt-6.1-sol / ultra / default 普速禁 Fast；有效 model、effort、tier、speed 四项始终 **UNVERIFIED**，未查询认证或额度，PID/退出0不认证配置。

| 固定对象 | 实际绑定 |
| --- | --- |
| 本次完整派发 | `c64774c60d91e522cb515ef71e3e9d4ea6b4712c:review/remediation-seventh-20261015-prepare/integration/wave2/v1/dispatch/R7-U02-R7IR.md`，工作前全文读取 |
| B / 正式子树 | `e646432c644dec04d306842cc5a559a29c718fbc` / `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c` |
| 实际 MI / workspace tree | `45c80832a41c1b56dcd7e9d93497758cbb7721de` / `6480ffe3df49bd9776c719f3c9be1c13618fdb0a` |
| MI 正式131子树 | `8403869aaeb4726518414b409b3808c3c0780e65` |
| FI / tree | `13d76ba61838b13925ba9d41f58a6b047564d926` / `6747a584b91c86acd4771c1a6dee93260602106f` |
| 原完整七组合同 | `f622356f3beb9e84ea8cff9db07c7fb382565d3f:review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U02.json`，94,049字节，SHA256 `55f05fe26ed94a036415bbca1fca9a5af5819a853e797522d54705cee5868715` |
| 固定参考 R | `Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；只取得有界快照，未重新认证参考整树 |
| 作者 / 独立候选结果 | `84e2cca132ada38405657f19cbbd3d6891d4794f` / `44276c5ae69ef0970a98464a5a9e6ff7eb1c1f1c`，仅作原资格和精确贡献对照，不继承其 PASS |

先完整读取实际 AGENTS、固定658488恢复工具、跨容器说明及原恢复计划，再按合同两个命令在本容器实际恢复：原输入 **33文件 / 21,406,782字节**，实际输入 **186文件 / 7,112,903字节**，均独立复核大小、SHA256及Git blob。实际计划为95,551字节，SHA256 `7ee75b059f3a0f6653e52780521f8faae05e71c840ff55bd44494e9391f25c73`。两份真实HTTP恢复回执为 [restore-original.json](restore-original.json)、[restore-actual.json](restore-actual.json)。没有假设共享目录、用候选镜像替代 actual/，或启动恢复出的程序/脚本。工作区 `.agents` 为空、项目 `.agents/skills` 不存在，固定 B/派发/MI 没有 tracked `.agents`，无相关本地技能可应用。

实际 Git 验证了 MI/FI/root/formal tree 及全部131文件身份：26改变、105与B完全相同。随后逐项以B片段、各固定候选全文字节和MI最终片段重建 **56 hunks / 24 targets**，加上根三处当前接收元数据调整后，结果精确匹配MI。未在本地祖先中的候选使用已核恢复文件或不可变完整提交 raw URL定向取得，不追随branch tip。五份先前U04/U05接受正式文件精确保持；这些机械事实没有替代下面的内容复核。证据为 [scope-validation.json](scope-validation.json)、[bindings-and-links.json](bindings-and-links.json)。18处原raw offset/JSON pointer/canonical绑定亦由本容器独立复核。

合同指定的14份实际文件已全部全文审读：AGENTS、完整audit和Feature Matrix、WP39/WP41/WP13/WP34、四份指定测试目录、WP17、WP65正文及controls-help。另新读原三项七组、C04 records/2与5、C08 challenges/3、原提案5/8/28、normalized verification/dependencies、晚到D06原载荷/接收及L01–L14。作者报告、独立候选报告/per-ID/read-ledger、root eligibility，以及五个共享来源的独立批准报告和相关per-ID范围/共享资格字段均已阅读；其余恢复的工具/身份元数据按完整字节绑定，不声称每个字段都重新语义审查。逐文件和逐源实读范围见 [review-input-receipt.json](review-input-receipt.json)；分段交付记录 [read-delivery.jsonl](read-delivery.jsonl) 只证明输出交付，不自行证明语义PASS。工具输出发生截断的区间已另行补读，不能以初次范围标签代替完整读取。

| 本次必修 | 实际条款与新判断 |
| --- | --- |
| GR7-M04-301 | WP17 §6.1 L169–173及SS01–12。给定A≠B，主目录为A下相对Screenshots；先墙钟/命名，再必要mkdir/主截图。仅主阶段可捕获错误产生一次同名B目录解析/截图；保护前失败、rescue再失败、不可捕获信号分别保留。主或回退截图正常返回后才查完成音资源并条件请求SE。无沿是未触发，无独立取消；同毫秒可同名，已到目录/截图前缀及后续音效失败没有回滚保证。帮助“存档同目录”仍只是内容。有限静态内容通过。 |
| GR7-M06-002 | WP17 L167与§7.3 L283及IN01–13。共享普通短文本USE/brief、共享确认BACK/Yes及Party/Summary局部入口没有统一额外尾部；通用消息、普通/带帮助选项、自由文本及共享静态帮助的正常尾部保持。nil/缺commands不进循环，[]不同。循环内刷新、busy/pausing/等待/全显四态、业务前缀及异常可能绕过后继清理均保持；无尾部不等于宿主绝不刷新。有限静态内容通过。 |
| GR7-D06-001 | WP17 L175–184、DB01–05/BT01–15/AX01–06、audit L1864–1884及matrix本批F05-06追加。独立追读15按钮和6轴名称指针及其NUL字符串，实际a:b0→misc1:b9→rightshoulder:b5与有界解析控制流相符。选中解析器、已成功前序、正常源/分配前提完整；未知字段错误请求/无追加/外层继续，不等于所有失败都保前项。CC04、设备/后端、优先级、全1923字段及76/48语义均未获新签署。有限静态内容通过。 |

[per-id.json](per-id.json) 为三项分别保存实际MI整文件及条款身份、全部 **51行** 的当前前提/输入/预期/独立静态理由、原反证映射、正常/取消/失败/部分提交、直接/传递依赖和剩余接收门。每行均 **DERIVED_VECTOR / NOT_EXECUTED**，没有把工具检查当向量执行。BT/AX逐名使用普通b0/a0且继承已选解析器/成功前序/正常分配的完整条件，没有补造物理设备或游戏查询链。

本次重新读固定R的截图、默认Input、目录/音效解析、共享helper、Bag/Party/Summary及更新块、MessageConfig与Messages的具名正常尾部和异常前缀。对原必要消费者中可读的重学、净化室和BattleSwap又定向补取并核blob，其包装/更新块支持相同局部输入范围。Busy组件有界源与旧目录完整前提均已读；三行共享自动暂停不被正常短文本出口例覆盖。未运行参考Ruby、native PE、宿主、模型或异常注入。

原 GR6-O-002 的B独立 finding 13行与完整ledger该记录、MI WP13全文/R6-EV01–06及固定R解释器/116源重新核读：局部第101轮先额外Graphics请求再归0，98/99/100注释加终止分别0/终止后1/终止前1；116让出、等待和深度100/101独立。这与本次输入尾部不同根因，旧正确合同及历史关闭不重开、不转授全ID PASS。17条具名历史向量的实际前提/预期、行身份和本次相容理由另见 [historical-vector-reception.json](historical-vector-reception.json)。M06原canonical_candidate仍为null，不能改成无历史根或补造ID。M04与紧急保存提示根因分开；D06晚到前提只缩窄，TV02–05更宽建议没有采用。全历史去重/alias最终接收仍由R7-I负责。

D06静态工具重新核Game.exe完整身份及精确21名称/样本范围，且本审者完整读了VA `[0x1403b2630,0x1403b2bb0)` 的有界反汇编：未知名在0x1403b278e请求错误后返回；普通b0经0x1403b28e9到0x1403b28f9追加；allocation失败0x1403b2979清计数；外层0x1403b2a70/2a79清字段缓存继续。反汇编正文只留本容器scratch，公开 [binary-validation.json](binary-validation.json) 只存身份、范围和有限事实。mkxp显示标签、Input逻辑别名、WP65/help都不能补出CC04桥。既有1666+257和731 Windows是工具结构计数，本次没有重新清点全库或宣称它们是全语义/硬件证明。

共享接收按 [shared-reception.json](shared-reception.json) 的16处相关实际贡献逐条对齐，不授予其它ID新的语义PASS：

- audit和matrix的两个共同EOF均按U01→U02连接，片段完整且各一次；U13音色库、U11有限extendtext、U12 Debug导航勘误及U01/U02追加各自保留。原批准身份、原时点候选标签及旧状态列保持；当前入口明确等待实际复审，未提前接受。
- engine目录的U13 S01和U01 J01索引分别保留，既有R6-EV正确链未改。新R7-U03未接入，不能从历史同名向量或未来请求假定已整合。
- UI目录的U08四个HP行与本批51行各自完整，新增行偏移没有造成覆盖/重复/漏接；已接收WP39/WP41/WP34及combat/pokemon目录全文新读，本批不更改其非致死替补继续、目标解析和条件亲本提交前缀。
- U11 DX新段与B前缀及固定独立批准逐字对齐；本次只审其批准段的保留/与U02相容，未对整份DX其它历史新签语义。U01没有在该条件目标写入，新R7-U10保持WAIT未合入。
- 两个根追加仅解释制作时点标签并指向固定MI的public-reception，链接实际可解析；作者证据必须用该登记的固定候选commit/精确路径读取。errata第三处仅改变status/reception，旧R6 payload及WP72条款身份未变，§5.3导航未变，不是正式接受/关闭。

所有具名作者record→record排程入边为0；这不消除领域依赖。本文提供三项局部语义、必要消费者、共享保留和具名历史相容证据；**R7-I仍须明确接收并登记这些责任**，连同其它批次实际门及全局直接/传递依赖、历史去重接收，再分开决定ACCEPTED和CLOSED。U03/U07/U10的流程WAIT及原内容资格保留；8批18项只是当前整合范围，旧U04/U05三项不是本次18项的PASS依据。7 optional、2导航facet、1 no-required、2 policy未采用，27项/13批和旧56/92边界不变。

运行与配置限制全部保持：REFERENCE_OBSERVATION、参考程序、独立完整行为模型、游戏宿主、Demo、native媒体、真实存档/回放新增运行均0；51向量和相关历史向量全部NOT_EXECUTED。L01–L14原件逐项保留在输入回执，CC04 NOT_READ及资源/宿主/后端/未来兼容未知不自动放行。原R7局部Ruby1进程/10输入只保原资格，不回填本任务。

真实日志限制：早期侦察、fetch、bootstrap及直接读取有平台工具I/O和原生HTTP恢复回执，未另存每条独立PID/UTC/stdout/stderr，不事后补造。从logs/001开始仅具名包装调用有真实分流和子进程信息；交互读取仍以平台输出为证。005/006因未取得非祖先候选Git对象而失败；修正为固定提交HTTP/已核恢复字节。007把errata候选行直接与根调整后行比较而失败；后继单独核status/reception再整体比较，008全部56/24/3通过。错误日志完整保留，不把后继exit0改写为首轮通过。两次错误路径的交互展示读取已纠正，不是行为失败。没有保存或发布私有模型流、参考源正文或反汇编正文。

成果仅在从B创建的隔离checkout分支 `codex/r7-ir-u02-20261015-r1`，只写本 `review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U02/r1/`。不携带作者镜像、不修改MI/正式/main/tag或公共台账，不force或覆盖同名分支。最终commit/tree和全部文件远端字节回读由提交后的真实工具回执与最终回传绑定，manifest自身不伪造递归自哈希。没有阻塞本次三项限定静态裁决的缺失输入；上述正式接收、全局责任、运行和配置门仍保持原资格。
