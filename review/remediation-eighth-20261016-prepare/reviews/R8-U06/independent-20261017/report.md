# R8-U06 固定候选独立完整复审

**候选 PASS：11项必修（2 P2、9 P3）及3项已采用可选，14/14；FAIL 0。** 未发现需要候选修订的新语义缺陷。本结论只适用于下列固定候选及本批合同，不表示全部29必修完成、实际整合通过、正式接受或关闭。

候选：`16f986afc1c85e64131f1dc8c6f2477a79c04029`；基线：`4575e80d041ab0c74a42e2e36399d05791dbaa5b`；参考R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。B8为`fd1df570cad987dc3852a3b958f03916e317f7fe`，C35为`2460370f1e410bd49cc29e377b89662838aed2b3`。原5caff来源与C35恢复路径分别保留，早期c44/40f同路径旧载荷按准确commit/blob恢复，没有用当前字节冒充旧输入。

审查分支：`codex/r8-u06-independent-review-20261017`。协调接收任务：`01a14a04-b178-7567-a4eb-0f0bfac9a0d9`。只新增本目录审查证据，候选、正式规格、原报告、planning/audit、R和main未改；没有force push或业务Ruby执行。

## 逐项结论

| ID | 分类 | 结果 | 覆盖位置与关键判据 |
| --- | --- | --- | --- |
| GR8-CRE-001 | 必修 P3 | PASS | WP19 §5.3；WP30 §4.4；WP42 §4.2；EV/ST组；255模板保持，HP产出1/0首项反向区间失败；合法额度与默认非内部设施早门分开 |
| GR8-COM-001 | 必修 P3 | PASS | WP40 §6.1；STALL排序与TRUANT后段拒绝分开，原排序/平局规则保持 |
| GR8-COM-002 | 必修 P2 | PASS | WP39 §4.3.1；WP67-A §3.2/§12；Z01–05；缺失计数非0；默认1v1首失败及2v1、NPC、玩家skip、蛋/伙伴和先行前缀分别核验 |
| GR8-COM-003 | 必修 P2 | PASS | WP39 §4.3.1；WP40 §6.1；WP67-A；M01–04；实际0/1/3与配置行动序0/1分开；AI登记不补调度，早peer/seen与晚形态、反序/双健康/3v1及不推自动胜利均保持 |
| GR8-COM-004 | 必修 P3 | PASS | WP39 §3.4；括注同时承认消息与结果差异，原结果行和BC09保持 |
| GR8-COM-005 | 必修 P3 | PASS | WP39 §7.4；WP42 §7.1；尾动作复位动画/预锁，不保证转向或整场方向不变 |
| GR8-COM-006 | 必修 P3 | PASS | WP40 §5.2第14步；火药失败保持；自损需有效天气非雨/大雨且可承间伤，PP/历史前缀保持 |
| GR8-COM-007 | 必修 P3 | PASS | WP40 §10；王者盾牌接触反制世代分支身份正确；独立Hypercutter资格保持 |
| GR8-COM-008 | 必修 P3 | PASS | WP41 §9第4项；换人席位可选增量重算先于完整速度入场；配置false、缓存/tie与startup另路保持 |
| GR8-AI-001 | 必修 P3 | PASS | WP52-A §6；原AE-T02；CV01–05；原始类型/计算类型及PP门分开；直接查询单次+14；普通User/0不消费该贡献 |
| GR8-UI-FAINT-AUDIO-001 | 必修 P3 | PASS | WP67-A §9.3；100/d22、75/d29、双缺d12与零长d2；形态同后缀回退、独立音效、并行完成/Off/HP先后均对应原源 |
| GR8-AI-002 | 已采用可选 | PASS | WP52-A §6计数句；20直接+5复制=25，行为表/默认/拼写不改；降低核验歧义 |
| GR8-UI-BATTLE-END-MARK-001 | 已采用可选 | PASS | WP67-A §9.1括注；两胜利入口先置标记后BGM；败/平普通对照保持，仅局部时序理解精修 |
| GR8-COM-RECORD-DEBUG-RNG-001 | 已采用可选 | PASS | WP58 §5.1原L105短语；辅助选择返回与实际AI主路径分开且仍不入记录流；WP76/RC29只读，局部归属导航精修 |

精确原源路径/行范围、正反控制、失败时序与保留依据见[完整语义主审](full-semantic-review.md)、[战斗9项交叉复核](battle-controls-crosscheck.md)及[AI/音频5项交叉复核](optional-audio-crosscheck.md)。[机器可读逐项结果](results.json)保持同一14项身份和分类。

## 完整覆盖与证据资格

实际非作者 `/root/full_semantic_review` 本人完整读取本批reviewer-prompt的14合同、12份最终mirror整文件、15份非mirror全部内容，并对规定原源、必要formal、原提案、独立counter、当前与历史根记录逐项接收。没有以差异、旧reader FULL、132身份或62静态检查代替语义审查。主审最终为143个固定源范围（67个R路径）和28个必要正式/历史范围；全部窗口、身份和lossless同用途去重关系以[主审阅读账本](full-reading-ledger.json)为准；跨批资格由下述实际reader分工接收，不转授为主审本人FULL。

- `/root/battle_controls_review` 对CRE001及COM001–008另作9项原源交叉核验，含两个P2全部指定控制；[账本](battle-reading-ledger.json)说明7份整文件及其余有界范围。
- `/root/optional_audio_review` 对AI001、倒下音频及三项可选另作5项原源交叉核验；[账本](optional-reading-ledger.json)说明4份整文件、必要CP提案/反证和F05六源单位。
- `/root/qualification_reception` 完成M0–31所有必要独有资格及39+2接口的purpose判定；[资格接收](qualification-reception.md)、[账本](qualification-reading-ledger.json)保留原blob/pointer与当前C35资格的区别。
- `/root` 完成M32–63/C0–7全部必要资格原值、三伴件全文及额外完整载体，见[跨批账本](cross-batch-reading-ledger.json)和[协调阅读账本](coordination-reading-ledger.json)。不扩成其它领域全源新审，也不把原快照OPEN或原读者信用倒填为当前结论。
- `/root/identity_scope_audit` 独立验证132/132原输入、57/57恢复别名、72/72增量身份、F05 10/10及12/12镜像。各分母交叠，不能相加为语义覆盖率；[范围审计](identity-scope-audit.md)、[逐项核验](identity-checks.json)、[阅读账本](scope-reading-ledger.json)与[复核脚本](verify_identity.py)分别保存证据。

12份镜像共534,372B。三个目录保留全部旧行，只有授权的AE同ID T02修订；新增21个独立向量ID另计，原系列计数不漂移。7条Markdown相对链接按候选文件或固定正式基线路径投影解析，不声称mirror自含所有依赖。WP76、RC-W11/RC29、WP28正确受限域、原关闭资格与UI/宿主范围均保持。[打标增量入口](../../../candidates/R8-U06/evidence/tagging-handoff.md)仍为作者固定交接，本审查没有重做全面打标。

三项可选的计数/括注/归属短语均有明确低风险理解或验证收益，符合当前用户明确的“三采用可选”范围；仍为optional，不提高必修分母，不选其它7可选或独立视觉policy。作者当时更早聊天的原授权措辞未单独恢复，未把其自述当作已权威检索的历史原话。

请求配置为gpt-6.1-sol / ultra / default普速 / Fast off；实际主语义、交叉及资格reader均以明确model/effort工具请求创建。无权威运行echo的actual model/effort/tier/speed/Fast及opaque UUID逐项UNVERIFIED，没有探测CLI/认证。具名实际reader及来源分工保留，不以角色改名或续turn制造独立性。

全部行为判断为SOURCE_STATIC / DERIVED_VECTOR；身份、结构、算术和发布为TOOL_VALIDATION。未执行参考Ruby、游戏、业务模型、宿主、真实媒体、保存或回放，不授予像素、发声、墙钟或运行等价信用。历史数学/有限证书与环境探针按原分类保留，不转入本次新增业务运行。

## 其余门与发布

本批直接/传递语义前置批次为空，当前语义和必要资格阻塞0。仍需R8-INTEGRATOR唯一写入正式整文件、冻结新的实际整合SHA并逐贡献接收；实际非作者随后核完整最终共享文件及累计保留，再分别登记actual integrated PASS、ACCEPTED、CLOSED。未来缺陷兼容政策与真实宿主/媒体未知保持原有限范围，对本次静态候选复审不构成新阻塞。

先冻结本报告与证据的语义载荷commit，再普通push独立分支；后继[发布回读回执](publication-readback.json)绑定该实际载荷，最终完整发布SHA由外部最终回复收口，不在文件中写自身未来hash。固定候选27个文件已在无alternates的独立远端仓库完整回读，889,123B逐字节一致，见[候选远端回读](candidate-remote-readback.json)。审查发布须对本目录新增文件逐一完整远端回读，实际结果见后继回执和外部完整SHA。身份与传输信用不升级为语义或正式接受。
