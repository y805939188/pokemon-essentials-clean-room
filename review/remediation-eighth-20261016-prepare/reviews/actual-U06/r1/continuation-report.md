# R8-U06 实际整合独立验收后继回执

**结论：actual integrated PASS。11 必改与 3 项选入可选逐项 PASS；无本批未决阻塞。** 此结论仅针对下列固定输入与实际快照的静态规格整合，不签收其它批、整轮交付或打标，不登记 ACCEPTED/CLOSED。

| 绑定 | 完整身份 |
| --- | --- |
| 输入绑定 | `5ff355c53b73171a0277c95af97e1cbd40eb8b28` |
| 实际快照 | `0eee6d141f33758eda34bd8ebad94a3e2b617f5a` |
| 接收时最新登记 | `2e2d5e6ab3f531ee902f60574b22e20fb065e04b` |
| 被整合候选 | `16f986afc1c85e64131f1dc8c6f2477a79c04029` |
| 独立候选报告来源 | `052236414f6cb350f1781efe98761f336bb43108` |
| 原始交付 / B8 | `4575e80d041ab0c74a42e2e36399d05791dbaa5b` / `fd1df570cad987dc3852a3b958f03916e317f7fe` |
| 只读参考 | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` |
| 实际正式树 | `a46d25e8aead9af2a91c8424b41e2a3c324d108b` |
| 实际工作区树 | `967e7ca85cf0b0cd0c9b80d4c591319f74532055` |
| 独立输出分支 | `codex/r8-u06-actual-review-r1-20261017` |
| 父交协调 | `01a14a04-b178-7567-a4eb-0f0bfac9a0d9` |

## 后继关系与审者资格

历史提交 `f7915c033bce24b08e94b21b88cf0d485b159afe` 的 [BLOCKED 回执](report.md)、配置文件、阅读状态及发布回读均原样保存。它们准确描述当时尚缺创建证明、尚未完成实际审读的状态，不作为当前结论。父任务随后在同一上下文提供创建证明并要求继续；本回执是同一审者的后继完成判断，不增加独立人数。

[父创建证明](continuation-parent-creation-receipt.json) 记录 `cloud_threads.create` 的 `gpt-6.1-sol / ultra / service_tier=default` 请求、实际创建参数与 admission=started；thread `01a14a49-64c1-764e-b294-c70bb87680fd`、turn `01a14a49-6d4e-7396-ae92-2903e357f766`。这是父任务明确提供的创建证明，不伪称本上下文直接调用或取得运行回显。model/effort/tier/speed/Fast 的未暴露运行值全部保持 UNVERIFIED，未观察到冲突回显。原 B01 由此解除，B02 在后续完整实际审读完成后解除。

实际语义审者为当前云端根上下文，与 U06 作者 `01a14a0d-7b0f-767d-bac9-4cbd85b900dc`、串行整合者不同。原生辅助上下文仅作机械身份、导航、逐叶等值和保护校验；没有语义签票、FULL 信用或档位转授。原候选复审的读者、配置和历史 FULL 声明保留各自原资格，不算本次新增独立审者。

## 实读、证据接收与候选对应

本根完整读取 AGENTS、原 review-SKILL、实际验收协议、U06 入口及实际输入、批次 reviewer-prompt 的非合同部分和全部 14 份嵌入合同、14 份完整当前合同记录，以及 readset、accepted-facts/history/policy 伴件的本批内容。完整合同包括七组正文之外的 wrapper、操作、历史关系、条件目标与关闭限制。prompt/reviewer-prompt 的 28 份合同嵌入对象与所读合同逐项等值，经工具单独确认。

本次实际快照的 12 份受影响正式文件共 **3,652 行、534,372 字节**，包括 WP67-A 和三个测试目录，均由本根连续分段完整阅读；截断输出的缺段另行补读。实际 patch 全部 220 行和逐项实际变更记录亦已接收。阅读身份、完整范围、必要消费者和源码片段详见 [本次阅读账本](continuation-reading-ledger.json)。源码只是静态阅读，不执行。

候选 27 文件、独立报告 19 文件全部取得完整原字节，并核对各自来源、实际快照、绑定与登记。12 个实际正式文件与被独立 PASS 的候选镜像逐字节一致；本次结论另外建立在实际整文件、14 项合同、源生产/消费顺序及场景独立判断上。原报告 14 PASS 只接收为候选阶段证据，未直接转换为 actual PASS。

候选说明、dispositions、完整差异、静态验证及独立 report/results、full-semantic、battle-controls、optional-audio、identity-scope、qualification-reception 全部语义内容已接收。重复 JSON 阅读账本按原路径/pointer 接收所有非身份叙述，原值与全部出现位置保存在 [叙述接收投影](continuation-qualification-narrative.jsonl) 和 [投影资格](continuation-qualification-projection.json)；完整 144,634 字符叙述已连续读完。身份、hash、路径、运输及命令回执由完整字节工具校验接收，不授整载体的人类逐字 FULL，也不把原审者的参考阅读变成本根阅读。1,856 个账本指针均可解引用；其成立仅证明导航。

原继承 readset 的 60 源定位与当前完全一致，64/8 项定位除 `current_recovered_at` 外一致；原 10 份合同与当前对应全文逐叶比较，另完整读回 17 个不同的非身份原值和其用途。原 delta 的 72 units 相同，其旧 freeze/status 与当前冻结身份分层记录。原 OPEN/PENDING 是旧时点资格，不能抹除，也不能当成当前新阻塞。详见 [继承接收差异](continuation-inherited-readset-delta.json)。本根不声称新读完旧审者的全部 143 源单元/67 源路径或全部历史档案；本任务也未扩大为第九轮全局历史复审。

## 逐项 actual 结论

| ID | 分类 | actual | 落点、独立判断与保持边界 |
| --- | --- | --- | --- |
| GR8-CRE-001 | 必改 P3 | PASS | WP19 §5.3、WP30 §4.4、WP42 §4.2 及 ST01–05/EV01–02：设施模板可带 255/255，普通属性重算不归一化 EV；普通非 Shadow 战斗受领者先发生单项 0..负余量夹取失败，早于本受领者总量夹取、EV/EXP 提交和属性刷新。已发生的前缀及先前受领者不回滚，后继参与者清理未到达。默认设施 internalBattle=false 的更早门、正常 EV 对照及道具/Shadow/净化边界保留。 |
| GR8-COM-001 | 必改 P3 | PASS | WP40 §6.1：STALL 的 bracket=-1 与默认 0、TRUANT 后续行动拒绝分属不同阶段。100/50 速度对照成立；速度、同速缓存、Quick Draw 等原顺序未改变。 |
| GR8-COM-002 | 必改 P2 | PASS | WP39 §4.3.1、WP67-A §3.2/§12 与 Z01–05：缺失数量区别于既存非空但 0 可战斗队伍。默认等布局在玩家布局的首次消费失败，早于 owner/seat/scene；保留先行规则/记录等前缀，不冒称覆盖外层 in_battle/audio/fade 或专用 abort 捕获。显式不等布局的后继消费、NPC 非法 owner/空比较、玩家 0 的更早 skip、蛋/伙伴门均独立保持。 |
| GR8-COM-003 | 必改 P2 | PASS | WP39、WP40、WP67-A 与 M01–04：正常玩家单席、对手 [倒下 P, 健康 Q] 时，配置仍 1v1，实际创建 0/1/3、存活 0/3、旧优先队列 0/1，普通有效优先行动仅 0；Q 可由实际遍历登记命令且具正常 AI 选择，但不会因 MoveNext、Quash、速度增量加入缺失的优先条目。peer/seen/used、入场效果、场景实际遍历与配置布局资源各集合分开。反序、双健康、显式 3v1、蛋/伙伴门及不保证自动结束均保留。 |
| GR8-COM-004 | 必改 P3 | PASS | WP39 §3.4 括注已覆盖消息与结果差异；正常零可战斗跳过时 wild 返回 1、trainer 返回 0。原正确结果行、BC-09 及旧 no-battle 根保持，不额外造用例。 |
| GR8-COM-005 | 必改 P3 | PASS | WP39 §7.4 与 WP42 §7.1 一致描述末尾动画复位；尾调用不写 direction，方向 4/6 的正常对照成立，pattern 受 walk/step 条件限制。形态/治疗/等待/end 事件、提前异常及回调可转向的边界保留。 |
| GR8-COM-006 | 必改 P3 | PASS | WP40 §5.2 第 14 步：火属性且 Powder 时到此门必失败；只有有效天气非 Rain/HeavyRain 且可承间接伤害才自损。雨天/Magic Guard 仍失败并保留取消及尾处理，Umbrella 的有效天气区别、PP/历史前缀、四分之一取整和 HP 截断/回调均保持，不承诺统一最终 HP。 |
| GR8-COM-007 | 必改 P3 | PASS | WP40 §10：KINGSSHIELD 接触反应在世代≥8 请求攻击 -1，否则 -2；HYPERCUTTER 是独立的中央外来攻击下降免疫。保护标记先行，阶段上下限、Contrary/Simple/Mirror Armor 等门保留；配置表仅作身份绑定。 |
| GR8-COM-008 | 必改 P3 | PASS | WP41 §9：启用替补后速度重算时，在 send-out 后、入场特性速度消费前更新旧队列的速度缓存；不开启时旧缓存允许保留，不重掷 tie/bracket，不补新条目。旧同速 0/2、替补后 10/30、DRIZZLE/DROUGHT 的顺序得到最终雨；延后重算的晴是错误反事实，未执行为真实游戏结果。开场完整计算/入场/增量/形态时序保持。 |
| GR8-AI-001 | 必改 P3 | PASS | WP52-A §6、AE-T02 同 ID 与 CV01–05：普通 User(0) Conversion 不进入逐目标贡献，不能据此把整候选分数固定为 100。直接从 100 调贡献时，世代≥6 取首槽类型，旧世代扫描全部，排除自身/伪类型；发现阶段不检查 PP，伤害帮助器排除有限 PP=0 并算有效类型，不等价于 Disable/Taunt 完整选择门。每条匹配仅 +14 一次并停止。 |
| GR8-UI-FAINT-AUDIO-001 | 必改 P3 | PASS | WP67-A §9.3：同后缀 form→base 专用 cry 为 100，1 秒资源排期 22；专用缺失再试普通 75，1 秒排期 29；双缺为 12，选中零长为 2，仍有独立倒下 SE。数据框 8 单位轨并行，聚合完成有下一次 update 观察，不写成串行等待或固定实际帧/墙钟。Off、HP 提交早于呈现而领域 faint 后续、公共负长度截 0 等边界均保持。 |
| GR8-AI-002 | 选入可选 | PASS | WP52-A 仅把能力评级数量澄清为 20 add + 5 copy = 25；SYMBOISIS/GULPMISSLE/PROPELLORTAIL 等源拼写、默认与全部评级行为未修改。不是新增必改根。 |
| GR8-UI-BATTLE-END-MARK-001 | 选入可选 | PASS | WP67-A §9.1 括注准确限定两胜利入口先置 end mark 再请求 BGM；新普通 scene 初始 false，败/平并未因此置位，暂停消息全显后正常等待 3 秒关闭。BGM 失败时置位前缀仍已发生；§3.5 原正确主规则和其它异常/退款入口保持。 |
| GR8-COM-RECORD-DEBUG-RNG-001 | 选入可选 | PASS | WP58 §5.1 局部归因已链接 WP76 正确范围：正常设施/回放选用 scene factory，生成器是 DebugScene 且 controlPlayer=true 走 AI；只有直接用 debug helper 的 Bag 1/15、否则 Call 1/10（总 7/75）、否则 Fight 选择需要该局部限定。Fight 的 singular move 缺失早失败、空目标 -1/空 party nil/50 次让步及不进入记录 pbRandom 保留。5 元组、18 attributes、RC-29、WP76-R12/R6-DX-DEBUG-004/GIR-FD82-B029 均不重开。 |

每项完整机器记录、合同 pointer、实际文件与直接参考定位见 [continuation-results.json](continuation-results.json)。所有正反向量都是静态推导，执行资格均为 NOT_EXECUTED。

## 累计保持、公共目录与跨批接点

三个目录整文件接收保留全部旧测试族；825 条旧表行中 824 原文保持，唯一 AE-T02 为授权同 ID 修正，不以新 ID 重复；Z5/M4/EV2/CV5/ST5 共 21 新 ID 另计。所有原编号/同义和旧正确语义保留，未借计数更正删除内容。WP67-A 的参与者、命令扫描、HP 颜色/呈现、cry、结束标志各阶段完整保持，没有并成单一生命周期门；U04 的退款/Natural Gift/Quash 及 R7 Metronome PP 等正确内容保留。

U05 WP36 §4.3 驱虫比较对象按设置选首个非蛋（可倒下）或首个可战斗，和 U06 配置席位/实际创建/priority 各集合不同。U08 WP15 的本地化 7 槽与通用音频定位继续成立，专用 cry 的 form→base 同后缀、普通 fallback 及音高不套用其它资源域。U09 WP26 将空存储归于记录战斗，WP58/WP76 仍区分 Playback 的普通存储与实时依赖、DebugScene helper 和正常 AI 路；不把录像封套当完整状态隔离。WP19/30/42 与 WP28 普通合法 EV 消费域、WP54/55 默认设施门也一致。

公共 source-traceability 的 WP19/30/39/40/41/42/52-A/58/67-A 条目、Feature Matrix 的相关领域行、BT-K/RC 目录具名相关族及章节去向已接收；实际输入 public_contributions=[] 与既有路径对应，没有本批必须另增的公共索引贡献。历史索引计数与接受状态保留原时点，不虚改成当前 actual 或最终状态。协调 integration-plan 的 X02/X03/X04/X06/X09 接点均按上述实际消费者核对；编辑 DAG 为空未被当成共享语义通过的理由。

完整身份/范围复核见 [continuation-final-mechanical.json](continuation-final-mechanical.json)，原工具证据仍留存。79 项载荷在各自声明 commit 上全部匹配；其中 task-registry 在 `0eee6d…` 到 `5ff355…` 已有后继登记差异，`5ff355…`、`2e2d5e…` 与本分支保持一致。不能笼统声称 79 项跨所有时点原文相同。12 正式目标、候选 27/独立报告 19 来源身份不受该登记差异影响。

六批 U01/U04/U05/U07/U08/U09 的 `49a558f7d5498680ba88d532f3815e07d7844459` 原冻结五文件及 `56cc0f683249bd54658b94134d1a61be6e8748e0` 输入绑定七文件逐字节保持。实际正式 131 文件累计 38 变更/93 保持是整合背景的机械事实，不替代逐项判断。本分支对 `2e2d5e…` 的全部改动仅在本 r1 目录，原 AGENTS/audit/planning/历史报告及 main/tag、参考和其它批文件未修改。

## 未决依赖、交付与权限边界

本批实际静态验收未决阻塞为空，无需正式内容回修。owner 后续接收/登记、打标修复、其它批独立验收及最终累计验收仍由各任务负责；最终整轮/打标的未完成门不转换为本批语义编辑前置。原历史关闭根与独立视觉保真政策未重开，视觉政策未选择，不据此要求新增游戏行为。

业务 Ruby、游戏、宿主、媒体播放、保存/回放和所有行为向量均 NOT_EXECUTED；没有开发框架或改写正式文本。只新增本目录后继证据，普通 push 独立分支，不 force，不写协调登记/main/tag，不登记 ACCEPTED/CLOSED。

先提交本回执及证据载荷，再用 [独立远端回读脚本](continuation-publication-verify.py) 从新建 bare 仓库网络 fetch、完整取得本目录每个 blob，核对本地提交/工作树/远端字节、mode/blob/SHA256；保存后继 [载荷回读回执](continuation-publication-readback.json)，再提交并推送该回执，最后完整回读包含回执的输出提交。最终输出 SHA 由外部回复提供，本文不填自身未来 SHA。
