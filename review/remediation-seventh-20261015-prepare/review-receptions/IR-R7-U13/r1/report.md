# R7-U13 r1 独立实际整合复审

**GR7-D07-001：PASS_SCOPED_ACTUAL_INTEGRATION。** 本次新实际上下文亲自审查固定 MI 的累计字节，确认 MIDI 独立音色库静态声明的最小修订及相关消费者相容性。没有发现阻塞这一有限静态判断的内容缺陷、缺失输入或独立性问题。全部十五项行为向量仍 **NOT_EXECUTED**；不认证其它必修、全局覆盖、原生消费或运行等价，不登记 ACCEPTED/CLOSED。

## 身份、合同与固定输入

实际环境返回 `CODEX_THREAD_ID=CODEX_SESSION_ID=01a14027-3f25-7584-8ccc-ad5a234b9016`，与派发列出的十九个真实可见排除标识全部不同。父来源是 `01a13f49-a154-7054-9b04-ce31f924d01c`；作者 `01a13f80-5248-7789-ab67-26ce7270c019`、候选审者 `01a13ff1-4e91-74b4-ac83-5838dbb59018` 均与本上下文不同。独立 opaque task/context、环境 opaque ID 与模型 PID 未暴露，保留 UNVERIFIED，不从 `/root`、角色名或工具 PID 推断。没有创建任何子任务、辅助 agent、子会话或额外模型调用。

请求为 gpt-6.1-sol / ultra / service_tier=default / 普速、禁 Fast；有效 model、effort、tier、speed 无有效平台回参，四项分别 **UNVERIFIED**。未查询额度或认证，未另启模型 CLI。实际工具 PID/UTC/退出只证明普通取证进程。

| 输入 | 不可变提交 | 根 tree／正式子树 |
| --- | --- | --- |
| 本次完整派发 | `c64774c60d91e522cb515ef71e3e9d4ea6b4712c` | 实际根 tree 见输入回执 |
| 实际累计 MI | `45c80832a41c1b56dcd7e9d93497758cbb7721de` | `6480ffe3df49bd9776c719f3c9be1c13618fdb0a`／`8403869aaeb4726518414b409b3808c3c0780e65` |
| 实际输入冻结 FI | `13d76ba61838b13925ba9d41f58a6b047564d926` | `6747a584b91c86acd4771c1a6dee93260602106f` |
| 固定 B | `e646432c644dec04d306842cc5a559a29c718fbc` | `84f79ec6e772aacbf3a464fde68cdc5a280e2950`／`ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c` |
| 只读参考 R | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | `7589c800b61ba13a13040ed0d686979b80a84fd0`；本次仅重核具名恢复文件 |
| 原七组合同 | `f622356f3beb9e84ea8cff9db07c7fb382565d3f` | 精确 `delegation/contracts/R7-U13.json` |
| 候选冻结 | `aa369555b0e8b6c8b077f964b54ed63d3b924f26` | 精确 `candidate-freezes/R7-U13/candidate-input.json` |
| 作者候选 | `5635c73ea14adc278961da0e3917c2d00d580a25` | `e2c261a77a7268a5eb07e7e364ac257d9fed3e31` |
| 独立候选审查 | `f34cb117cdd06f8b4462a95c5196f458848ff729` | `1d1fcbc9cd6c933d8b62ab871d80352b59ec4403` |

先直接完整读取派发，再读完整原七组和固定恢复工具／说明／计划；实际 MI AGENTS.md 全文已读。固定 B/MI 无 tracked `.agents`，本容器 `/workspace/.agents` 为空，没有相关 `.agents/skills`，未声称使用不存在的技能。未读取80MB交接 manifest，未反复扫描完整 core，未执行恢复的参考、作者、审者或 native 程序。

## 本容器恢复和实际范围

所有输入在本容器独立恢复，不借用整合者目录。原合同／反证／源／限制恢复至 `/workspace/r7-ir-R7-U13/original`，21 文件、16,814,642 字节；实际计划恢复至 `/workspace/r7-ir-R7-U13/actual-input`，107 文件、6,029,364 字节。后者计划本身55,511字节，SHA256 `1716809019ce9172cda2e7dacb1d2e481c9ea9399bacb63419312e1fc2a9d3a3`。初始恢复和实际 `--resume` 回执分别归档，不把复用重核伪装成首次下载。原128成员全部重新核 bytes/SHA256/blob；107实际成员另与对应真实 Git blob/mode 完整比较，均匹配。

补取固定 C2 的原 D07完整提案与 C11有限 native forward-map，核编码对象和解码身份；具名 MI 的 WP02/WP03/WP07/WP75、scope、DX目录、WP24以及 R6限制/政策另定向取得。原 D07 finding 与根 delta `/records/30/original_proposal` 相同、canonical SHA一致；独立 C11 payload 与根已接收 decision_record 及单列 counter_payload 相同。晚到 `/records/3` 明确旧 collector 把 C11 已接独立反证错当 D07 作者变动，其历史资格保持。旧 P02 raw-binding manifest 没有此晚到项的行；用实际六个七组引用、完整冻结载荷与 delta 绑定，没有补造旧行。

全部十份指定实际文件全文已读：AGENTS、audit、WP39、WP41、WP15、WP34、combat目录、engine目录、pokemon目录、matrix。字节未改部分没有跳过指定全文阅读；补充材料的精确读段与未读范围在 [输入回执](review-input-receipt.json)。四份具名参考脚本和 mkxp.json 全文重读；Game.exe 完整身份核验，本次没有新授机器码语义证明。原 C11、D07、C17、native map、作者／候选审者报告与逐ID全文均读；其它候选证据全量接收／核 Git 身份，不声称其所有程序均已执行或获得新语义批准。

独立核正式131路径与每份 B/MI 身份：26改变、105未改。八新批18项的24目标、56个 baseline-relative hunk 从固定B独立重建，所有56处又与各自实际候选 Git blob 的独立 diff、候选切片及最终 MI 位置对齐；完整生成补丁与172,979字节冻结 patch 完全相同。十六个作者／审者 commit-tree 绑定匹配。五份先前接受文件与原接受 MI 逐字相同，只有机械保留信用；本次另读其与 U13 相交的领域意义。

作者完整24文件／862,370字节与候选审者完整22文件／264,314字节均核同。作者 manifest 只显式列四镜像，另十九个非自身证据未逐个列身份；原提示要求镜像身份，当前不可变commit/tree、穷举冻结表及本次真实 Git 比较足以绑定整个交付。不倒称作者 manifest 列了24项，也不借候选 PASS 推导本次 actual PASS。

## 实际条款与原七组结论

| MI 路径／行 | 本次独立判断 |
| --- | --- |
| WP15 §7 L196 | 随附配置为 MIDI 声明独立库输入及 `soundfont.sf2` 身份，轨道查找与声明、实际选择／读取／载入／接受及声音分开。缺／坏／省略／无效、guards、解析、后端、合成均未知，L04/L09及旧 SF2证据保持，不选未来格式／API／兼容档位。 |
| WP15 §10 L215 | 依赖项仅交叉引用声明，原路径解析、请求、登记、选项、时长与媒体结果未被扩大。§6与§11完整字节保持。 |
| engine目录 L436–442 | 独立 S01 只增加声明向量，theme.mid、正常系统、记录80/pitch100/options100、无默认覆盖前提齐全；纸面只变库身份，无动态结果。唯一新编号，不替换 B04-R。 |
| audit T-WP15 L322–324 | 三行来源精确到固定R与具名消费者；Game.exe身份和原有限 map 与未知范围分列；原批准输入／审查资格保持。 |
| matrix F05-02 L174 | Pending静态补充与原Reviewed／Inventoried媒体资格并列，未升级实际播放；F05-01原行不变。 |

四目标完整与片段 bytes/SHA256/blob、B/候选／实际hunk坐标及逐项 C11-A01–A07 结论在 [per-id.json](per-id.json)。原七组分别完成：身份与 required/P3不变；原反证及普通/取消/失败/部分提交前提重核；最小修订和正确保留一致；全部十四原向量与新S01重核；C11独立及根缩窄历史保留；准确读写／消费者／共享接收分列；执行与未知无升级。

## 十五项纸面向量

以下均是本次对固定 MI 的静态内容核验，**行为 NOT_EXECUTED**。实际输入／期望／来源／逐项理由在逐ID文件完整列出。

| 向量 | 重新核对的观察点 |
| --- | --- |
| C11-V01 | R配置用途/身份与§7一致；声明不等于消费。 |
| C11-V02 | 合法可发现theme.mid、正常系统、80/100、options100、无覆盖，保持80/100请求；实际加载／输出未知。 |
| C11-V03 | 纸面仅改为absent-bank.sf2，关系输入不同而同脚本请求保持；无真实配置改动，不推静音／失败／后备。 |
| C11-V04 | 广义字面＋六后缀与专用SE字面＋四后缀分开；显式.midi命中不等于无后缀SE可补.midi，也非格式证书。 |
| C11-V05 | 通用nil／空名早返，无库建立／释放／取消推论。 |
| C11-V06 | 暂停12恢复有效B，先登记B、请求12参数错后只重试0；第二次普通失败越出，paused／保存12仍在，frame_reset及resume清理未达，无统一回滚。 |
| C11-V07 | 无覆盖时缺BGM/BGS轨道先登记而无对应轨道请求；WAV正常对照不抵消MIDI声明。 |
| C11-V08 | 不选额外旧数据库profile；GR6-POL-001和未来后端／格式选择保持独立。 |
| D07-SF-CFG-01 | 默认配置只记录MIDI用途与soundfont.sf2身份。 |
| D07-SF-CFG-02 | 可命中mid/midi正常请求不认证库加载或声音。 |
| D07-SF-CFG-03 | 文件身份／请求与未知接受／guard／合成分开，原完整SF2结构和独立复算资格保留。 |
| D07-SF-CFG-04 | nil／空名早返不成为库初始化／释放／取消。 |
| D07-SF-CFG-05 | 非零位置第一次BGM参数错误只重试0，不概括SF2错误处理。 |
| D07-SF-CFG-06 | 普通wav沿旧请求与时长合同，不抵消MIDI声明。 |
| GR7-D07-001-S01 | 新唯一声明块与以上原14项相容，不取代原行／顺序／状态。 |

四份参考脚本的直接重新阅读支持以上判断：FileTests的广义与专用后缀，Audio_Play的解析／路由／nil早返，Game_System的登记／选项缩放／有限重试／暂停记忆，以及Audio的WAV/Ogg/MP3时长职责。没有将时长解析当成SF2解析，也没有把请求正常返回称发声。原十四向量的 input/expected/execution 在作者与候选审者逐ID中均与原载荷完全相同，机械比较只是辅助，以上内容另行核对。

## 共享接收、消费者与历史

CG01 audit、CG04 engine目录、CG07 matrix 的完整实际文件均已读。九个同文件其它贡献与固定B、各自候选、原非作者报告／逐ID批准边界及根资格回执对齐：audit的U11/U12/U01/U02四处、engine的U01一处、matrix的U11/U12/U01/U02四处。本批五个hunk完整保留，没有整文件镜像替换。

两处共同 EOF 插入按 U01→U02 连接；U01 r2登记/复合节头的追溯、同一J01交叉索引与matrix行未被S01或U13替换。U01旧r1的J01 FAIL及流程偏差保持原绑定，不由r2或当前共享保留抹去。U02有限手柄词汇／未知字段继续、CC04未读桥与真实设备未知保持；U02/U08在UI目录的三个实际hunk和完整新段已核，不把图像／输入／截图完成音请求提升为库消费或输出证明。UI其它主体只有机械保留信用。

U11 audit/F18-04有限extendtext证据与当前WP75 §14、DX末段12个向量逐条相容：四目标独立请求、标记／互斥、缺席／假返回／退出前缀未被MIDI说明重写；CV-M29原文档事实、L07实际几何／时序／进程所有权未知保持。U12只改本ID导航至WP72 §5.3并关联勘误，旧R6冻结内容与状态未回写。

根两处追加当前接收入口的本地目标在固定 MI 均存在；十个新本地href的目标／所含fragment完成静态核对，不称浏览器运行。作者证据依 public-reception 的固定 candidate commit及精确 `candidates/<batch>/evidence/author/` 路径读取，不假定在MI当前树。errata的三处差异仅是 status、candidate_review、shared_integration 接收阶段字段，仍非正式接受／关闭；完整字段差异记录于工具证据。

本批与先前接受文件的相交意义另行实读：WP39 §7.5及WP24 §5.4的野生／训练家／胜利／捕获选曲与引子记忆是请求前状态，后项音频失败不回滚前缀；WP41保留换人／逃跑及成功SE请求条件；WP34和pokemon目录保留亲本动态读取与子显式同值提交、容量／生成／图像请求及失败前缀。BC旧行、SW旧行、BR01–31/PF01–09没有被bank声明变成音频运行保证。五份原接受内容逐字保持，只就上述相容性核验，不重签三项必修的语义PASS。

原B04-R01–28全行／顺序、R17、GR-007的BGS差异请求BGM淡出、默认覆盖／选项／暂停／记忆／时长／缺文件／部分效果、engine中M10-008帧刷新边界均保留。WP02/WP03的配置与内容身份职责不能吞并独立库声明；WP07存在性／路径／诊断不保证播放或所有异常收尾；WP75引用WP15的图形资源合同与其有限工具事实不冲突。指定实际十文件内其它历史规则虽已读，只给U13相容与保持结论，不新授其它ID或全历史批准。

原作者排程没有具名record→record入边／传递边，不能据此推导无领域依赖。配置→文件查找→路由→登记/请求→WP15及三同步目标，在本次有限静态范围已接合；共享九项、直接／传递消费者和具名旧控制的核验结果供R7-I接收。原native map的 NATIVE-U01–U05未闭合范围仍按原件保留，实际配置供应／选择／解析／分派、库读取／接受、异常guards、合成和声音继续OPEN。L09已接完整RIFF/hydra九表25,786记录（含sentinel）、独立复算／配置审查事实不抹去，也不扩大为全格式合规或采样器等价；本任务没有重做SF2算法审查。

U03/U07/U10合同前AI辅助的流程WAIT保持，未合入其未来贡献。7 optional、2额外导航facet、1 no-required、2 policy未采用；27项/13批、旧56/92有限边界与历史局部运行资格保持。本次结论不更新公共分母或已有关闭证书。

## 执行、日志与剩余门

SOURCE_STATIC为本次具名配置／脚本／实际正文阅读；DERIVED_VECTOR为十五项纸面预期；TOOL_VALIDATION为传输、身份、tree/mode、完整补丁／片段／行保留／链接和写集检查。REFERENCE_OBSERVATION、独立完整行为模型、参考程序／Ruby、游戏宿主、Demo、native媒体、合成／声音、真实存档回放新增运行全部0。原L01–L14完整保留，不用限制掩盖可具名补取的源；旧局部Ruby观察不回填成本任务执行。

初始缺Git对象的查看失败、控制脚本访问尚未fetch的作者提交失败均保留。独立hunk审计先错误假定新errata在B存在，随后未正确区分后继行政字段、又假定只有一个字段，三次真实exit1均保留；按实际空基线与三个精确字段修正后重核56处通过。回执生成器最初把已经通过controls完整读的AGENTS误纳纯read-ledger计数而exit1；改为单列其真实读取证据后十文件覆盖检查通过。这些是工具边界修正，没有修改被审内容或赋予行为信用。

早期侦察／fetch／bootstrap／读取有真实平台I/O和原恢复HTTP回执，但并非每条都另存本地逐命令UTC/PID/分离流；不倒填。[commands.jsonl](tools/commands.jsonl)起记录实际公共工具子进程与完整流身份。大段输出被平台截断的缺段已经具名重读。完整参考程序阅读stdout保存在本容器 `/workspace/r7-ir-R7-U13/local-reference-source-io/`，公开包仅保留其真实身份／迁移回执，不把源实现文本推送进净化仓库。没有保存或发布私有模型流。

完整暂存集 `git diff --cached --check` 实际exit2，诊断均在真实stdout文本：带行号的空白阅读行保留冒号后空格、控制输出的尾空格／空尾行。完整输出和路径分类保留于 `tools/full-whitespace-*`，不清洗原I/O、不改称通过。报告／JSON／Python工具的限定空白检查在发布时另行执行，真实结果进入运输日志。

仅从固定B的隔离worktree创建唯一分支 `codex/r7-ir-u13-20261015-r1`，只写本 `integrated-reviews/R7-U13/r1/` 的报告、逐ID、回执、manifest及真实工具证据，不携带或修改MI正文、作者镜像、正式正文、公共台账、main或tag。普通提交／推送，未force或覆盖他人同名分支。最终结果commit/tree与所有文件不可变远端完整响应体的逐文件验证在实际运输后绑定；manifest不伪造自身最终hash或递归回执。

尚未由本任务完成：R7-I接收本新结果精确commit/tree、登记语义／共享／直接及传递依赖／历史责任，再按其授权分别决定正式接受和关闭；更宽native／真实宿主／兼容范围仍须各自证据。本报告仅提供这一个ID的限定静态实际整合结论。

首个证据载荷已普通推送并完整回读：commit `514542fe620262e30d38fc6ddba94d34d1326513`，tree `3764f3114023fb19b748a067d71e82167f4ed7ed`；261文件、2,743,112字节，全部HTTP完整响应体／bytes／SHA256／blob／模式匹配，分支回读前后相同。报告、JSON和Python工具限定空白检查实际exit0。真实Git命令I/O和逐文件回执归档于 [payload运输证据](tools/publication-payload/publication-and-full-readback.json)。后继提交只归档运输证据、补充本段／回执并更新manifest；GR7-D07-001内容结论及MI/FI不变。最终封装提交另做全文件远端回读，由最终工具I/O与返回在包外绑定。
