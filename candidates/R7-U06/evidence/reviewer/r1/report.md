# R7-U06 r1 独立候选复审

GR7-M09-001、GR7-M10-001 均为 **PASS_SCOPED_CANDIDATE**。结论仅适用于下列冻结候选的精确字节；没有签署实际整合 PASS、正式 ACCEPTED 或 CLOSED。

## 身份、输入与独立性

- 本审者实际 `CODEX_THREAD_ID` / `CODEX_SESSION_ID`：`01a13ff0-6000-748c-a2ed-b6965f662032`。环境：`ccarenv_b64_Y2NhcmVudl9iZTdlNTk3ODkxNTg4MTkxOTU0ODVkYjVmMTM2ZDdhNw`。父 source thread：`01a13f49-a154-7054-9b04-ce31f924d01c`。独立 task/context 字段及模型进程 PID 未单独暴露，不编造。
- 作者实际 thread：`01a13f7f-5a16-72cd-87a7-6b9fd59a1025`，来自冻结输入及实际作者 `runtime-identity.json`，两者一致；其环境与本审者环境不同。独立性来自不同实际 thread/environment，不能从双方都称 `/root` 推断相同或不同。未创建子任务或其它作者、审者。
- 用户入口 commit：`95c260d8f3fb4a171675dde877137fcd4c2f1c8d`，tree `577c350364bb4e2eb712325a9095d53d29eeeeb3`；已完整读取其 `review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U06/reviewer-dispatch.md`。
- 不可变 freeze：`aa369555b0e8b6c8b077f964b54ed63d3b924f26`，tree `08bd0f362c74ef7645b5bbd70b557489c122ae29`。精确 candidate-input 路径为同目录 `candidate-input.json`。输入、候选恢复清单、mirror-diffs、根 remote-readback 在入口与 freeze 的字节完全相同。
- 候选 commit：`fd0c1e6f50587331846921d446d893f1c1e84f3d`，tree `113069992c0d13f80c41312c26f2143a9e31c15f`。作者分支仅作来源标签：`codex/r7-u06-author-20261015-wave1`；没有 checkout 或修改它。
- B：`e646432c644dec04d306842cc5a559a29c718fbc`；正式规格子树 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。R：`Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。R 的合同给定 tree 为 `7589c800b61ba13a13040ed0d686979b80a84fd0`；本审只核具名文件，未认证完整参考树。
- 请求 gpt-6.1-sol / ultra / service_tier=default 普通速度、禁 Fast；实际 model/effort/tier/speed 均无有效平台回参，逐项 **UNVERIFIED**。PID、请求、工具退出均未被当作配置证明，未查询额度或认证。
- 已读实际根 AGENTS.md。工作区、固定 B 和入口 commit 均未发现项目 `.agents/skills`；`/workspace/.agents` 为空，无可读取的相关 SKILL.md。未虚构技能读取。

## 本容器实际恢复与字节核验

先完整读取 `658488c81f1f3181a488298ab27850c8af951d73` 下固定恢复工具、U06 原清单及跨容器说明，再在本环境恢复到 `/workspace/r7-context/R7-U06-reviewer`：36 文件／7,536,934 字节。随后按 freeze 的实际清单另恢复候选至 `/workspace/r7-review-input/R7-U06-r1-fd0c1e6f50587331846921d446d893f1c1e84f3d`：43 文件／597,346 字节。没有假设父容器共享目录，没有使用浮动 HEAD 作为输入。

原绑定明确需要的 source/formal inventory、M10 原 finding、M09 原 finding 别名另定向恢复4文件／391,290字节；其身份与本次已恢复 C13 raw-binding-manifest 核对，再用同一固定工具在同目录 `--resume`。为核合法数据、形态、配置、速度重排及旧 AI 消费者，又具名补取7份固定 R 文件／211,412字节。原上下文累计47个逻辑位置／8,139,636字节；M09别名没有新增独立性或语义票数。

`review-input-receipt.json` 记录全部43个候选文件的实际 bytes/SHA256/blob/mode，逐个与固定候选 Git blob 相同；实际 candidate tree 和对 B 的完整43项差异均匹配 freeze，仅新增 `candidates/R7-U06/` 下普通100644 blob。作者 manifest 的42个非自身声明均重新核对；manifest 自身由固定 candidate commit/tree 和完整接收表绑定。274处原绑定引用（含重复及记录外层溯源）通过原载荷SHA、JSON pointer、canonical SHA及原始字节区间验证，不能把这些工具检查当作内容 PASS。

四份完整候选正文／目录已经全文审读；B 对照通过全部真实差异及原字节保留检查。WP46只替换原第23、54、59行；WP49仅插入157–164行；combat目录只插入42–65行；pokemon目录只插入134–157行。除这些位置外，B原字节及顺序保留。两份目录各增15条向量，原MH02/MH06、全部AB31条及其它TD/SS/MH/HI/AI/AE/BE/CE行保留。没有WP43镜像、optional/policy或公共台账变更。

## GR7-M09-001

**PASS_SCOPED_CANDIDATE**。原完整七组、原M09提案、实际C01非作者反证及其六组回归范围均已读，并对固定 R 的实际生产／消费链重新核验。主候选为 WP46 第54、59行，目录为 pokemon-rules 测试目录新增小节。

围攻在整招前确定合格业主队伍与计划数，实际普通基底求值才消费首位；形态吸收早于普通基底、会心和波动，成功返回与击计数则由外层单独处理。因此在共同存活／命中前提下，两名参与者95/10对应14/6；首击画皮吸收时第二击首次取得14，6未求值。三连踢已有“每次基底求值加P”的正确触发保留，并将序号例限定为三次求值；结冻头首吸收后只产生10/20，仍成功3击。替身优先吸收但不设置这两种形态早返标记，普通求值仍推进。

| 实际目录向量 | 本次独立内容判断 |
| --- | --- |
| C01-M09-BU-ABS | 计划2、首击C1/直接损失0、破皮当代额外损血另计；第二击14，总成功2，6未求值；前提充分 |
| C01-M09-BU-CONTROL | 初态形态1时14/6，计划及成功计数不变 |
| C01-M09-TK-ABS | 首吸收不求基底，后两次10/20，总成功3，无补击 |
| C01-M09-TK-CONTROL | 无吸收时10/20/30；独立命中与SKILLLINK规则保留 |
| C01-M09-SUB-BU | 从破皮对照加替身，首14消费首名，续6；替身与个体HP分开 |
| C01-M09-SUB-TK | 从无形态吸收对照加替身，三次普通基底10/20/30 |
| C01-M09-MISS-STOP-FIRST-BU | 合法降低命中、抽99失败，基底未求值、成功0、只保留前缀 |
| C01-M09-MISS-STOP-FIRST-TK | q90且无有效SKILLLINK，首失手不求值、不补后击 |
| C01-M09-MISS-STOP-LATER | 首击吸收后次击失败，保留成功1及切形；无后续10/20 |
| C01-M09-MISS-STOP-FAINT-U | 给定独立反应已经使U倒下时，外层停止门生效 |
| C01-M09-MISS-STOP-SLEEP | 给定未治愈真睡状态时，成功击后的独立门阻后击 |
| C01-M09-MISS-STOP-FREEZE | 给定未治愈真冻状态时，同样仅保留已到前缀 |
| C01-M09-MISS-STOP-FAINT-T | 唯一目标已倒下时不补剩余计划 |
| R7-U06-M09-CANCEL | 上游取消尚未建立使用，不造计划、消费或扣PP；族内无UI取消 |
| R7-U06-M09-PREFIX | 写点前后分开，不补未到基底/HP、不回滚已到前缀；宿主继续未知 |

停止／故障行是已给定到达状态或中断位置的条件对照，不认证它们都由无额外反应的默认BU/TK生存夹具自然产生，也没有执行故障注入。候选没有据这些行保证后击完成或宿主恢复。

固定PBS核SNEASEL学习BEATUP、种族攻95，MAGIKARP种族攻10，MIMIKYU/DISGUISE、EISCUE/ICEFACE，默认TRIPLEKICK物理P10/q90，并补读HITMONTOP的合法学习例及EISCUE形态1。基底不是最终伤害；换形后的攻防仍按当前值。业主边界、包含合格U、不包含伙伴、资格、命中、计划/成功击数、固定伤害与AI估量均未改。

WP43全文及§6.2/§7已有C1早返正确，候选与之相容，无条件同步矛盾，故未采用可选WP43扩写。原“整个伤害核心缺失”或“三连踢完全缺触发”的宽主张没有复活。

历史回归：重新读固定B的R6-CA非提出者反证、固定R独立AI围攻消费者及本候选完整目录BE-B72–B76。旧GR6-CA-EB-001是预测关／评分开／空合格名单／正替身的评分除零，与本次正常实际多击基底消费不同；其已修目录所有原行按字节保留。本次不继承历史PASS，不重新关闭旧项。

## GR7-M10-001

**PASS_SCOPED_CANDIDATE**。原完整七组、M10原提案、实际C05非作者反证及C1–C7验收范围均已读。主候选WP49 §6.1.1第157–164行，WP46第23行只把既有正确时点连接到主规则；combat目录新增15条。

源的直接尾部位于附效／额外畏缩／减伤果消费之后、后续目标和U濒死之前，沿本击实际目标列表。候选分别给出本次计算类型火／水、unaffected、calcDamage0、替身、当下普通有效STEAMENGINE、中央可升资格及自身来源增量请求＋6。它与更早允许濒死的动态OnBeingHit分开；没有加正肉身HP损失门，也没有独立模式破坏者或强行屏蔽门。中央能力包装和普通有效性仍拒倒下／胃液／有效气体，夹限及反馈保持。

| 实际目录向量 | 本次独立内容判断 |
| --- | --- |
| R7-U06-SE01 | 给定L20/P40/特攻33/特防55，普通基础量6，本系与相性合成×3得18，HP82/PP4；后速度阶级＋6，原35保持，普通查询140 |
| R7-U06-SE02 | 独立合法火招满足其余门也请求＋6，不复制水伤18 |
| R7-U06-SE03 | ROLYCOLY默认另能力HEATPROOF与水招不产生蒸汽机反应，水伤前缀保持 |
| R7-U06-SE04 | 非火水、本次经合法输电改电分别拒；按计算类型而非数据原类型 |
| R7-U06-SE05 | 替身门独立拒，calcDamage非零不足以绕过，已扣PP不退 |
| R7-U06-SE06 | 保护或失手使unaffected，不补升阶或伤害 |
| R7-U06-SE07 | 到达入口且calcDamage0的条件守卫对照；不声称普通正伤害例可自然生成0 |
| R7-U06-SE08 | 胃液、有效气体各自令普通有效性拒绝 |
| R7-U06-SE09 | 尾部已倒下者不获请求；更早受击回调许可不能移用 |
| R7-U06-SE10 | −4→＋2、＋5→＋6、＋6不再升；原35在＋2普通查询70 |
| R7-U06-SE11 | 两合法火水击各次重查，首封顶后续不再升；能力改变／压制按第二击当下输入 |
| R7-U06-SE12 | 模式破坏者没有本尾部独立阻断；中央资格仍保留 |
| R7-U06-SE13 | 默认DARMANITAN的SHEERFORCE及EMBER附效10合法；强行抑制附效和具名后段二／三，不吞直接尾部 |
| R7-U06-SE14 | 未建立使用的取消及更早失败／故障分别保留实际前缀，不造请求或退款 |
| R7-U06-SE15 | 阶级写点后反馈故障保留已写PP/HP/阶级，不补完成、无宿主证书 |

逐项核C1–C7对应SE01/02、SE04、SE05–09、SE10、SE11、SE12/13、SE14/15。多击、类型改变及故障例均按所列合法输入或已经到达入口的条件使用，没有认证获取链、任意中间改写或全域可达。

中央阶级与速度消费者已重新读：请求＋6不等于赋值＋6，原速度不重写。合法水使用者可由默认SQUIRTLE学习WATERGUN实现；ROLYCOLY默认普通能力确含STEAMENGINE/HEATPROOF，当前PP5与总PP25分开；DARMANITAN/EMBER有默认数据依据。固定R速度查询及行动后的配置重算、B的WP40 §5.2/§5.2.3/§6均与此相容；没有声称速度写入当场强制中断／重排行动或异常后必继续。

正确保留：单一当前能力，不造同时蒸汽机／唱反调／单纯；48族267配对与WP48的27族148配对不变；能力描述、FasterEggHatching及AI评级3仍分别属于数据／孵化／估量，不用它们替代直接战斗合同。旧持物／自然之恩／鸟嘴加热与OnBeingHit时序保持。WP46自然之恩续击失败、WP40异常后有限同轮重选、原MH39–44与BE-B72–B82等历史内容已读且未受本次差异改变。

## 接收范围与执行限制

无候选输入、身份或本批内容阻塞。原合同具名作者阻塞入边为空、共享冲突组为空；不因此声称其它批次、共享消费者或领域依赖已完成。四份贡献可按已核条款从B交R7-I接收，仍须由R7-I逐clause串行整合，保护其它批次已接贡献及共享目录。

尚未满足：R7-I实际条款整合、WP43/WP46语义责任者及WP49/共享目录接收、实际累积整合字节的新独立R7-IR、精确历史与直接／传递依赖最终接收、根正式接受及关闭。早期历史全域同义去重未认证；旧56/92关闭边界与27项／13批分母保持。

本次新增仅 SOURCE_STATIC、DERIVED_VECTOR 内容审查与 TOOL_VALIDATION（传输／字节／范围／指针／声明／独立常数算术）。全部30条新增行为向量仍 **NOT_EXECUTED**。REFERENCE_OBSERVATION、参考Ruby、游戏宿主、Demo、native媒体、真实存档回放及完整独立模型均0；未执行任何作者或恢复参考程序。R7整体原有H14/UTIL-03局部1进程／10输入仅保原历史资格，不算本次执行。L01–L14完整保留，有限文件阅读不升级为整树／完整游戏覆盖。

初始侦察、合同／源分段读取与两次恢复通过平台工具真实完成；初始每次命令未独立落盘UTC/PID及完整I/O，缺口见 `receipts/initial-provenance.json`，不补造。原HTTP恢复回执完整保留；`commands/001`起包装工具保存实际argv、UTC、工具子进程PID、完整stdout/stderr和底层退出，不能代认证模型。作者早期I/O缺口以及005验证失败、009差异退出1、012空白检查失败、其后成功均沿作者固定证据保留，不由本次工具退出0抹去。

## 交付

唯一成果分支 `codex/r7-u06-reviewer-20261015-r1`，在本环境干净隔离checkout从固定B创建。创建前远端同名分支无结果。仅提交 `candidates/R7-U06/evidence/reviewer/r1/`；不携带作者镜像，不改正式文件、作者分支、整合分支、main或tag，不force。

`per-id.json`给逐项结论与每条向量判断；`review-input-receipt.json`绑定输入；`receipts/source-read-set.json`给精确源身份／已读范围；`artifact-manifest.json`覆盖本批审者产物（自身由结果commit/tree及完整远端回读绑定）。普通提交／push和首次完整回读证据随后随证据提交发布。最终结果commit/tree及对它的全部新增文件完整远端回读在包外回报，避免伪造“包含自身发布后回执”的循环身份。
