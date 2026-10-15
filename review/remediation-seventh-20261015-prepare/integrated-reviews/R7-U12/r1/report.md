# R7-U12 r1：实际输入核验与独立复审 WAIT

**GR7-M19-001：WAIT；GR7-H08-001：WAIT。** 本次已在独立容器实际恢复固定材料，完成下面具名字节、导航和局部静态内容核对，但没有完成合同要求的完整当前共享正文、五份批准条件目标及其目录、全部消费者与历史接收内容复审。因此不签发 `PASS_SCOPED_ACTUAL_INTEGRATION`。这是可读材料的剩余审查义务，不是材料缺失、宿主限制或已经发现的规格错误；不能用下载完成、哈希相同、工具退出0或旧候选 PASS 填补。

派发全文固定 `c64774c60d91e522cb515ef71e3e9d4ea6b4712c` 的 `review/remediation-seventh-20261015-prepare/integration/wave2/v1/dispatch/R7-U12-R7IR.md`，在任何委派之前直接取得并阅读。本轮从未创建子任务、子会话、辅助 agent 或其它模型调用。当前容器环境实际返回 `CODEX_THREAD_ID=CODEX_SESSION_ID=01a1402e-9f4a-72f7-863e-018ee4a4e036`，不同于合同列出的所有排除标识、作者 `01a13f80-31d8-738b-b99d-3d3465db503c`、候选审者 `01a13ff1-2d9f-748e-a450-710ab3337034` 和派发来源 `01a13f49-a154-7054-9b04-ce31f924d01c`。内部 opaque context 未暴露，保留 `UNVERIFIED`，不从 `/root`、角色或 PID 推断。有效 model/effort/tier/speed 均无有效回参，分别 `UNVERIFIED`；模型 PID 未暴露。命令 PID 只标识审计子进程。

固定 B 为 `e646432c644dec04d306842cc5a559a29c718fbc`，正式子树 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。固定 R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，仅取得具名只读快照，没有运行参考或 native 程序。实际 MI 为 `45c80832a41c1b56dcd7e9d93497758cbb7721de` / tree `6480ffe3df49bd9776c719f3c9be1c13618fdb0a`，正式子树 `8403869aaeb4726518414b409b3808c3c0780e65`。实际 FI 为 `13d76ba61838b13925ba9d41f58a6b047564d926` / tree `6747a584b91c86acd4771c1a6dee93260602106f`。MI/FI 均以实际 Git 对象和精确路径复核，不采用浮动 HEAD 或作者镜像代替 MI。

已全文读实际 AGENTS.md 和原两项七组合同，检查 B、MI 的 `.agents` 及 `/workspace/.agents`：项目无 `.agents/skills`，工作区该目录为空，没有可应用的本地技能。保留行为规格净室约束，没有实现引擎/TS 包、复制或转译参考架构。先读固定 `658488c81f1f3181a488298ab27850c8af951d73` 的恢复工具、说明和 U12 原计划，再执行两次规定恢复。原始材料恢复到 `/workspace/r7-ir-R7-U12/original`，26 文件／7,587,353 字节；实际计划恢复到 `/workspace/r7-ir-R7-U12/actual-input`，240 文件／8,075,455 字节。FI 实际计划 123,709 字节，SHA256 `238057ab33de2cb5e1a5405ba83859665d8a01bcf152ecb0c2d9b7a766d3c2a8`。没有假定跨容器目录共享、读取80MB manifest或扫描完整core包。

`tool-evidence/restored-byte-audit.json` 对266成员／15,662,808字节逐个重新核 bytes/SHA256/Git blob。`formal-131-identity-table.json` 对完整131文件核正式路径、模式、MI/B身份与FI表：26改变、105未变。`all-56-clauses-audit.json` 从固定B重新拼接全部56片段／24目标，核每个删除/新增文本、原候选行段、目标结果及root三个行政调整；两处共同EOF按U01→U02连接，无覆盖或漏接的机械证据。五份先前接受文件与其固定实际快照逐字保持，R6和B21历史子树保持。以上仅是机械证据，不给其它必修、历史或全局语义PASS。

| ID | 本次已核对内容 | 结论及剩余门 |
| --- | --- | --- |
| GR7-M19-001 | 三入口实际字节等于冻结的对应作者镜像；十处href为3+3+4，指向固定H四原作者文件；只逆转十href并移除各一条勘误说明，可重建三份完整B。 | WAIT；共享全文、批准条件目标/目录、全部消费者和历史接收内容复审未完成。 |
| GR7-H08-001 | 实际errata、matrix553、audit1833均指定WP72§5.3／WP27；原item42仍保留§5.2；原状态列不变；LF-inclusive条款身份一致。 | WAIT；同上，尤其不能从完整R6子树字节不变推出其全部历史消费者已经语义接收。 |

M19 的新工具再次得到 B 三入口136个本地inline目的地中126可解析、10缺席／4唯一目标；MI的126个普通本地目的地仍按原href和顺序解析，另十个URL覆盖同四H目标。存在的 `user-interface/` 是目录，不能算第11个坏链接。17目录族以及根README、CURRENT-DELIVERY、第六轮README对照均保持。四历史文件已在本容器从不可变远端取得，bytes/SHA/blob与原合同一致；历史README仍是NEW2作者候选，当前actual-freeze入口明确区分ACT。static-cases仍为14项未执行作者设计，另两JSON只核身份/导航资格，不移授历史正文语义批准。

当前说明明确要求已拥有H对象或匹配档案，缺少时检索仍不可用；没有声称所有历史对象就在本地或有浏览器/fragment/全131链接运行证书。本次固定raw完整恢复是当前运输事实。C01原012误计目录并JSON解析失败的exit1、013更正exit0及7个原对象，已直接从固定C2重新取回并与保留副本比较；不是重跑历史脚本。十二个原合同raw切片按offset/长度/SHA、JSON pointer和canonical SHA重新核实，原C01/C08反证的缩窄范围保持。

M19逐项正常/取消/失败/部分提交：普通有效路线可读；停止只读导航没有领域写入；缺席相对目标不能由邻近好链接替代；没有领域事务或真实存档提交。四个C01与四个M19-NAV向量逐项的前提、静态理由和执行阶段见 `per-id.json`，全部行为 `NOT_EXECUTED`。未重新批准M20历史资格或M21当前补充判断。

H08 已定点读固定 Debug778–797、Bag81–93/263–281及容量与填包控制段，读WP72§5.2/§5.3、WP27§3.2–3.3和DG-U08-01–04。合法登记道具、指定有限槽数/999上限、无并发改包、依赖正常是有限反例前提；有限一槽不代表默认无限口袋。正常请求1实入1，正常DG请求2实入2；列表取消/BACK0均不添加、不请求给予消息。998请求2时只实入1至999、返回假、跳过成功排序；调用方不检查假返回，正常后段仍按请求2反馈，已写1保留。999请求1和零可用空间可实入0、返回假而正常反馈仍使用请求数。添加或后段消息失败不保证正常反馈/收尾、没有统一回滚。无限口袋可扩槽，独立填包先清后填、重要道具1／普通3及容量跳过保持。全部16个具名向量分别记录，均 `SOURCE_STATIC + DERIVED_VECTOR / NOT_EXECUTED`，没有运行参考、独立完整行为模型或宿主。

root errata 与作者原件的完整JSON差异恰为 `status`、`reception`，从候选运输阶段变为已整合待实际审查；原/新标签、固定身份、规则、当前导航优先条件不变。该优先条件仍等待R7-I正式接受，不能当已接受。audit/matrix新增“当前接收状态”区分保留的作者时点标签与当前累计状态，并指向实际public-reception；固定候选提交加精确路径的作者证据读法已读。`ACCEPTED=false`、`CLOSED=false`保持。

CG01/CG07中U01/U02/U11/U13的八个共享文件贡献与固定B、各候选和原候选批准定位已建立机械对齐表，见 `shared-contribution-receipt.json`。唯一receiver为R7-I。全部56条的重建也保留U01/U13 engine、U02/U08 UI和U11 DX的原片段身份；本次未完成这些相交消费者、完整共享文件与各原批准内容的全部语义核对，因此共享语义接收标为PENDING，不因哈希保留而签发相容PASS。U03/U07/U10未准入且未整合，不能假定未来贡献已经存在，也不能据此抹去领域依赖。

两项没有具名直接/传递作者排程边，但这不代表全局或领域依赖满足。M19三入口、H四历史目标、current/actual-freeze导航及M20/M21责任；H08当前errata→audit/matrix→WP72§5.3→WP27及DG四行、WP72/domain owner（含M15）与root current-supplement/public-sync owner，均须准确接收。五份先前接受文件只获得本次机械保持证明，不能代替它们与U12相交领域的内容复审。

完整剩余可读路径和门列于 `tool-evidence/content-review-coverage.json`。明确未完成：audit/matrix全部当前共享正文；WP39、WP41、WP34及其两个目录全部内容；整个旧sync-input与相关历史接收；所有强制消费者/共享批准内容。部分长显示曾被截断或省略，`complete-content-line-map.json`只是完整文本分页/相同行映射的生成记录，不是54页都已经审读的证明。本报告不把程序全文读入或页面生成伪称完整语义复审；这些未满足门决定两项最终WAIT。

L01–L14原件已读并保留。REFERENCE_OBSERVATION、所有行为向量均 `NOT_EXECUTED`；新参考程序、独立完整模型、宿主、Demo、native媒体、真实存档/回放执行0。历史H14/UTIL03局部Ruby执行不回填本任务。有效配置UNVERIFIED、旧56/92有限关闭、27项/13批分母保持；7 optional、2导航facet、1 no-required、2 policy均未采用。没有请求认证/额度、读取或发布私有模型流。

初始侦察、Git/raw获取及交互内容读取保留于平台工具I/O，两次恢复有真实UTC/HTTP原生回执；这些早期与交互命令未分别文件化每个PID/start/stdout/stderr，明确保留，不补造。`logs/001`起的具名新命令才有真实分离I/O、UTC、PID与exit。001中查询B尚不存在的新errata路径产生预期Git诊断，已按唯一允许的新文件显式处理；不伪称该路径原先存在。作者002构建失败、013空白检查exit2、020错误提交ID、021API失败及原C01失败均保留原资格，后继成功没有覆盖它们。

成果只写 `review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U12/r1/`，从固定B建立唯一隔离分支 `codex/r7-ir-u12-20261015-r1`。不携带MI正文或作者镜像、不改公共台账、main、tag，不force。manifest自身由外部真实结果commit/tree及最终完整逐文件远端回读绑定，避免自哈希递归；最终commit/tree及回读以提交后的工具I/O和包外回执为准。R7-I仍须独立登记语义/共享/依赖/历史责任，再分别决定正式接受与关闭。
