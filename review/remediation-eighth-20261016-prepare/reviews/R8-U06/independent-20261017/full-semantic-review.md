# R8-U06 全部14项独立主语义复审

结论：**14/14项有限静态语义 PASS；11 required（含COM002、COM003两项P2）及3项已采用 optional全部逐项复核，无抽样、无新增语义阻塞。** 本报告由实际非候选作者上下文 `/root/full_semantic_review` 完成。结论来自本人完整合同、必要原源/消费者及最终整文件阅读，不以作者自证、旧批准、132项身份或62项静态检查替代语义判断。

本报告交协调主审接收。整批 candidate 接收还应与其跨批资格、身份及发布证据合并；本报告不代签 actual integrated PASS、ACCEPTED、CLOSED。没有执行任何业务 Ruby、游戏、模型、宿主、媒体、真实存档或回放。

## 固定对象、请求配置与范围

- 候选固定HEAD：`16f986afc1c85e64131f1dc8c6f2477a79c04029`；直接基线：`4575e80d041ab0c74a42e2e36399d05791dbaa5b`。
- 原源R：`/workspace/pokemon-essentials` 的 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。下文R路径均相对此根，行号为该固定对象行号。
- B8：`fd1df570cad987dc3852a3b958f03916e317f7fe`；C35恢复/当前根：`2460370f1e410bd49cc29e377b89662838aed2b3`；原c44、后继40f及恢复C35没有混成同一身份。
- 请求：`gpt-6.1-sol / ultra / default / normal / Fast off`。无权威运行配置echo，actual model、effort、tier、speed、Fast、opaque UUID均为 **UNVERIFIED**。未探测CLI或补造平台回显。
- `RR/`＝`review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/`；`M/`＝`review/remediation-eighth-20261016-prepare/candidates/R8-U06/mirror/deliverables/final-specification-set/`；`F/`＝B8的 `deliverables/final-specification-set/`。

当前用户明确指定“11必改…及3采用可选”，并逐名要求AI002、CP01、F05完整复核，因此三项当前选择授权成立。三项仍是optional，不增加required根或代选其它7项optional；独立视觉policy仍未选。作者当时选择动作的最早原始聊天未由本上下文另行取得，不声称历史授权原话已经权威回读。

## 本人完整阅读与证据资格

本人全文读取根 `AGENTS.md`、`RR/inputs/review-SKILL.md`、5555行批次 `reviewer-prompt.md`，其中14个完整合同全部读取；并全文读取accepted-facts、history-qualifications、policy-and-preservation三个伴件。review-SKILL只依其实际适用范围使用，不将净化正文规则当成审计报告的额外审批门。

当前批次readset全部结构与字面内容、原继承readset和delta index均完整接收。60个源/规格父身份、64根载体、8伴件及72个delta条目全部映射；这几个分母互有交叠，不能相加。本人对本批相关原源作143个实际完整范围阅读，涉及67个固定R路径；原继承39个R父路径均有本人直接必要单位阅读。另有28个B8正式/历史范围直接读取，及原counter内完整正式片段的实际读取。范围和整文件信用严格分开，不由父文件SHA授予全文信用。

原40f根11条、原c44对应11条、C35当前14条根、当前14条findings及14份原完整合同逐值接收；涉及的完整提案、独立反例、COM005传播、COM008补闭合、CP002原15409B提案/9260B反例/exact-inputs、CP01完整提案和counter、F05原65366B八节候选均已实际读取其必要完整载荷。精确重复JSON值只复用本人已读的同一字面payload；enclosing pointer、用途和资格仍逐处接收。空数组/布尔等短值未按无关用途省略。内嵌源字符串只在与本人固定原源实读片段精确相等时去重，保留来源、偏移、字节数和SHA。旧OPEN是当时生成时点，不抹去C35当前后继资格，也不把后继接收倒填成原时点已完成。

以下12份候选正文均本人全文读完，合计534,372B，包含全部旧正确正文、表格、目录与新增段落；不只读diff：

| M下完整文件 | 实读行范围 |
| --- | --- |
| combat-requirements/wp39-battle-context-and-participants.md | 1–351 |
| combat-requirements/wp40-commands-obedience-and-action-order.md | 1–361 |
| combat-requirements/wp41-switching-positioning-and-escape.md | 1–250 |
| combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md | 1–285 |
| combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md | 1–259 |
| combat-requirements/wp58-battle-recording-and-playback.md | 1–181 |
| creature-rpg/wp30-growth-learning-and-friendship.md | 1–287 |
| pokemon-rules/wp19-attributes-ability-and-stats.md | 1–274 |
| test-catalog/combat-requirements-wp39-40-41-42-45.md | 1–317 |
| test-catalog/combat-requirements-wp49-51-52.md | 1–363 |
| test-catalog/pokemon-rules-wp19-21-22-23-34.md | 1–356 |
| user-interface/wp67-a-battle-interaction-and-presentation.md | 1–368 |

candidate目录其余15个文件也全部本人读完：README、independent-review、author-reading-ledger、candidate-files、candidate.diff、commands、dispositions全部14条、input-identity-checks、prepublication、publication-commands、两份publication-readback、static-validation、tagging-handoff、verify_candidate.py。脚本仅阅读，未执行；日志是审计输入，未重放其中push等动作。该目录27个文件没有本人未读项。

机器台账：[full-reading-ledger.json](full-reading-ledger.json)。其中每个原源/formal范围与carrier pointer保留固定commit、wholefile/unit/value SHA及完成状态；不捏造原始读取UTC或opaque工具ID。截断均实际修复后才给完整信用，包括formal五单位、publication日志全量重读和readset大窗重读。不可得的CP002旧外部路径改从原SHA命名的精确冻结载荷接收，失败查找信用为0。

## 逐项判定

### 1. GR8-CRE-001 — PASS，required P3

M `pokemon-rules/wp19-attributes-ability-and-stats.md` L164–180为唯一增量域主约；WP30 L116–123、WP42 L65–85作消费接合；属性目录L343–356的ST01–05与战斗目录L315–317的EV01–02保持为未执行向量。

本人沿 `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb` L1–219、`004_Challenge_Battles.rb` L1–144、`Data/Scripts/014_Pokemon/001_Pokemon.rb` L1040–1128及 `Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb` L1–271核对：有效模板可分配HP/ATK各255，重算不规范化；普通EV接收先对当前HP项构造0..−3区间，产出1与0均先失败，尚未总量夹限或本接收者首写。默认设施internalBattle=false先挡普通成长，不表示模板不能由其它普通内部战斗接收。

最强“总量510会先挡住/零产出可绕过/默认设施不增长所以无反例”均不能消掉这个限定增量域。候选保留先前接收者/回调前缀与未到参与者清空，不扩到全部物品、Shadow、false/nil/mail/berry新facet。F/WP28 L227–232、342–358、WP54 L72–105、WP55 L94–105及原ST67消费范围已实读，正确既有合同保持。

### 2. GR8-COM-001 — PASS，required P3

M WP40 L255–259明确用STALL解释排序档，TRUANT仍在后段执行拒绝。原源 `Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb` L140–149、844–858，`001_Battle/004_Battle_ActionAttacksPriority.rb` L136–278及 `002_Battler/009_Battler_UseMoveSuccessChecks.rb` L183–248分别支持STALL−1、全量排序适用动作和TRUANT门。

最强“只是译名，可由WP48推知”不能使具名身份准确；此处只作最小替换，未改正确WP48排序表、QUICKDRAW概率、速度/tie缓存或增量不重抽。取消未登记、行动拒绝与优先序计算分阶段，不借此新增排序bug或整轮保证。

### 3. GR8-COM-002 — PASS，required P2

M WP39 L96、159–183、310–318，WP67-A L60–61、343–346与Z01–05明确“缺失首计数”及默认相等布局的首失败。本人直接读 `Data/Scripts/011_Battle/001_Battle/001_Battle.rb` L329–411、`002_Battle_StartAndEnd.rb` L16–347，世界 `Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb` L354–529及 `002_Overworld_BattleIntroAnim.rb` L51–152。合法非空wild全不可战时，计数未建立该段；默认相等1v1把缺项同步到双侧，先在玩家布局枚举失败，早于owner范围、建席/场景与专用abort捕获。

显式2v1不能复制同一首失败：玩家可先降至1，后续布局消费者才可能先失败；已核Scene初始化与目标菜单必要单位。玩家自身零可战更早skip；NPC BC19/20没有野生同步；蛋混合有后继初始化拒绝。最强“统一计0/owner失败/返回abort0”的读法均被排除。已发生的建对象、战前记录、清规则及条件过渡标志/音频前缀不回滚；未到正常善后/结果写回，不推出永久全局损坏或宿主必退出。

### 4. GR8-COM-003 — PASS，required P2

M WP39 L165、177–183、WP40 L255–259及战斗目录M01–04保留正计数与原序全量建席的独立根。固定 `[P HP0,Q健康]`、玩家一名健康、无伙伴/蛋等限定下，布局降为1v1，实际建席0/1/3，实际活者0/3；全量优先序只有0/1，普通活序只有0。原源关键为上述StartAndEnd L120–165、Battle L208–210、Priority L136–278；它们没有按可战成员过滤野生建席，也不会在增量中插入Q3。

本人继续读完整CommandPhase L1–265、AttackPhase L1–202、AI核心L10–116、ChooseMove L1–392及Battle L548–600，核实实际对象AI包装/扫描可给Q登记，1v1目标邻近判定不额外阻止，而普通/MoveNext/Quash消费仍受已有优先序限制。早Peer/seen/used、配置人数的野生开场请求、全实际活者后段形态检查与参与队伍裁判分开。反序、双健康、3v1、伙伴与蛋前门对照均已核。最强“正常资格/AI必先失败”不足以推翻有限例；候选也不声称Q获得正常UI、正常行动、自动胜利或整场安全结局。

### 5. GR8-COM-004 — PASS，required P3

M WP39 L109–114仅修引导括注，原L113与BC-09结果合同保留。`Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb` L142–169完整helper及其两个public core caller支持：合法零可战玩家下，普通野生skip写/返回1，训练家skip写/返回0，消息亦不同。

最强“主结果条款本来正确”限定了更改幅度，不能使原括注“只差消息”准确。候选未引入新用例要求、正常战斗终局或异常回滚；包装生成、DEBUG对照与此前规则/计数前缀保持。

### 6. GR8-COM-005 — PASS，required P3

M WP39 L271和WP42 L207均修到同一根传播：行走动画/预锁记录复位，当前方向不由末动作更改。世界BattleStarting L306–329、`Data/Scripts/004_Game classes/006_Game_Character.rb` L1–30、356–360、815–826及Game_Player L1–12已直接读取。方向4/6各自保持；pattern仅在walk/step动画条件满足时复位，anime_count与prelock归0。

最强“朝向恢复只是泛称”不抵消具体方向写入的差异，但仅需两处末短语统一。既有治疗、进化/结束通知、资源与结果时序保持；结束回调可先改方向或抛错，候选未许诺整个核心始终保持方向，也未许诺回调失败后末动作仍执行。

### 7. GR8-COM-006 — PASS，required P3

M WP40 L167只给粉尘自损补双门。`Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb` L154–578（关键310–323）、`001_Battle_Battler.rb` L518–533、561–566、`012_MoveEffects_ChangeMoveEffect.rb` L360–376及EOR L597–780支持：Powder且计算FIRE仍失败；只有使用者有效天气非Rain/HeavyRain且能承间伤才自损。

雨/大雨及Magic Guard等可跳过自损而保留动画/消息、失败标记、取消及结束行动；原始天气与有效天气分开，Umbrella等有效天气None不等于原天气不存在。最强“旧断言只概述火药失败”不能支持无条件1/4扣血；修订保持PP/历史已提交前缀、后段天气压制及尾清理资格，不推广为全部异常可恢复。

### 8. GR8-COM-007 — PASS，required P3

M WP40 L337把世代消费者纠正为王者盾牌接触反制，§5.3正确主体保持。原源 `Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb` L303–526（367–378）、`005_Battler_StatStages.rb` L1–387、AbilityEffects L69–74、118–120、720–735，及完整Protect/KingsShield生产单位、PBS身份均已读。有限普通接触条件下世代≥8请求降攻1、旧代2，同时挡该命中；HyperCutter是中央外来Attack下降免疫，局部没有该世代分支。

最强“WP48已正确，配置表可由全文推知”限定为P3具名身份纠正；候选未改效果值、中央资格、Contrary/Simple/MirrorArmor、阶段上下限或回调前缀，也未强制新联合用例。COM001排序档是另一消费者，不因同文件/术语而合根。

### 9. GR8-COM-008 — PASS，required P3

M WP41 L75–104与L201现在一致：派出后按配置更新该换人席位顺序缓存，再完整入场。原源 `Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb` L142–204、220–226、274–374，Priority L136–278，完整AttackPhase/EOR必要caller已读；原unit6遗漏的closing end L278也本人直接读到，未继承原不完整范围。

入场读取缓存速度；增量更新既有条目，不重抽档/tie且不补插。配置false可合法留旧缓存。10/30速度及Drought→Drizzle有限对照支持先更新后最终Rain；延后产生反序是错误实现的静态反事实，未执行。最强“§9是缩略，可能指额外后算”不能解释换人固定不变量里同一可选操作倒置。开场L303–311确有全算→入场→另一次增量→forms，候选保持该独立caller；绑定/派出/计算/入场异常的不同已提交前缀、GR013及SW35均保留。

### 10. GR8-AI-001 — PASS，required P3

M WP52-A L215–221及AI目录L170、350–363正确区分直接目标评分定义与普通User/0接线。`Data/Scripts/011_Battle/006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb` L760–845、`005_AI/005_AI_ChooseMove.rb` L1–392、`010_AIBattler.rb` L285–315、AI核心registry、Target数据与CONVERSION PBS记录本人已读。

世代≥6只发现首槽原始类型，旧代扫描全部；排伪类型/已有类型。发现不滤PP，伤害匹配helper另查计算类型并只排有限总PP正且当前PP0；无完整Disable/Taunt资格偷加。首个匹配只+14一次，无匹配保传入分。100→114、旧代后槽、PP0、多个候选仍只114等CV01–05正确。最强“User0不消费就无定义”只能支持保留接线；普通完整候选仍可有其它评分修正，所以没有断言整候选恒100。原AE-T02同ID修正，覆盖表F/G与真实Conversion运行效果未改。

### 11. GR8-UI-FAINT-AUDIO-001（CP002）— PASS，required P3

M WP67-A L258–280（新锚点L265起）精确给出专用/普通/双缺三分支和共同等待。原源 `Data/Scripts/011_Battle/004_Scene/008_Battle_Scene_Animations.rb` L202–215、610–657，`004_Scene_PlayAnimations.rb` L313–326，`007_Battle_Scene_BaseAnimation.rb` L1–64，`Data/Scripts/010_Data/002_PBS data/009_Species_files.rb` L183–244、PictureEx登记/调度/执行/完成及Audio全部必要单位本人直接实读。

专用_faint按形态→基础同后缀，命中默认pitch100；仅普通命中显式75且长度同用75。1秒静态夹具的下落起点分别22、29、双缺12；命中零长为2，不能合并为缺失。独立Pkmn faint SE仍登记，数据框自身8单位轨道共同推进，全部轨道结束后的另次聚合观察才完成。d不等于总阻塞、固定update次数或真实墙钟。

最强“不必复制全部视觉轨道/颜色”仍适用于未选policy，不能产生此有限音频请求的75/10+2及选择分支。候选不扩为粒子/像素保真。Off不取消固定倒下；HP先提交，scene返回后才继续正式faint清理；无独立取消，显式abort/普通诊断/中途构造更新销毁失败分开，不授ensure或回滚保证。WP15、WP16、WP74及BT K01–K59必要全文区段已对照，无冲突。

### 12. GR8-AI-002 — PASS，selected optional；severity=null

M WP52-A L225仅把计数改为20直接登记＋5复制目标＝25；L227–243原修正表保持。原源 `Data/Scripts/011_Battle/005_AI/008_AI_Utilities.rb` L231–382全族20 add及3次copy的5目标全部本人读取，附覆盖表L180–199、209–213保持25。

最强“行为表已经完整，不能凭23证明行为缺失”成立，所以仍optional。选择理由是降低核验口径歧义，局部低风险且符合当前用户明确选择。没有改任何修正、默认、技能、拼写或资格，SYMBOISIS等字面登记保持。

### 13. GR8-UI-BATTLE-END-MARK-001（CP01）— PASS，selected optional P3

M WP67-A L241只修括注为两条胜利入口先置标记、再请求BGM；L79–89正确主体保持。原源Scene_Initialize L1–11、`Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb` L230–267、408–419及StartAndEnd L405–512本人已读：新普通scene初始false；胜利置true先于BGM；仅把decision变2/5不走success，全显后首次正常访问elapsed≥3才关闭。

最强“全文§3.5已正确，仅局部归因欠准”成立，因此只选局部optional精修，不新增机制或与CP002合根。普通USE/BACK、忙时快进、abort链保持；BGM异常可留下已写true，不能把播放成功写成置位前提。选择收益是避免同篇时序与胜利限定误读，符合当前授权。

### 14. GR8-COM-RECORD-DEBUG-RNG-001（F05）— PASS，selected optional；NOT_REQUIRED_BOUNDARY_PRECISION

M WP58 L105只修调试随机的归属短语并导航既有WP76§7.2；记录主约L39–85、91–168保持。本人直接全文读取 `Data/Scripts/011_Battle/004_Scene/009_Battle_DebugScene.rb` L1–106、CommandPhase L1–265、`008_Other battle types/005_RecordedBattle.rb` L1–287、Challenge_Battles L1–144及factory L204–206、BattleSim L377–438；另实读F/WP76 L158–169、RC共同静态前提/header/W11。

普通设施/回放factory造普通Scene；生成器造DebugScene但controlPlayer使主命令先走AI，debug标记本身不是玩家AI路由。直接command helper随机返回Bag1/Call4/Fight0有选择含义，仍不经记录随机入口；Fight先访问单数move可在抽样前失败，target空−1、party空nil及至多50次yield分别保留。

最强“普通产品记录与WP76本来正确，未消费helper不产生公共API需求”成立，限制此项为optional局部归属精修。候选没有把直接helper改成默认主路径，没有改变记录序列、RNG、策略或新强制测试。选择理由是单处消歧并指向既有正确合同，符合当前授权；WP76-R12、R6-DX-DEBUG-004、GIR-FD82-B029及FAC001/W04/CD003保留。

## 跨项、目录与全文件保留

本人全文读取12镜像并完整读32,768B差异，核对每个变更的唯一receiver与周边范围。原BC31、CM33、SW35、G13、R11、E17及其它既有族未重算；新增Z01–05、M01–04、EV01–02、CV01–05、ST01–05为21个独立ID；AE族T02保同ID修正。场景向量是静态输入/预期，不伪造已运行结果，三个optional没有强制新目录义务。

WP39§4.3.1、WP19§5.3、WP30§4.4、WP42§4.2、Conversion与faint锚点/交叉导航语义一致。新增链接指向共享正文/正式只读消费者，不要求mirror自包含全部外篇。净化正文没有新增源路径、源码、内部类组织或未来强制API；数据身份和必要公式保持为行为数据。

累计保留包括R7 Metronome失败历史、SteamEngine、原始PP/HP颜色、U04物品退款、NaturalGift续击前缀、Quash、GR013、设施内部标志及旧NO_REQUIRED/撤回/关闭资格。本人没有将旧批准作当前免审：WP39批准来源、administrative/recovered/raw/sanitized各字节身份按history伴件分别接收。普通有效ID/nil域未扩为false/mail/berry等新facet；当前14项required/optional分母与跨批接受门未改。

跨批64+8载体剩余有效资格由协调主审 `/root` 与实际 `/root/qualification_reception` 分担本人读取；详见 [cross-batch-reading-ledger.json](cross-batch-reading-ledger.json) 和协调主审最终报告。该部分不冒称为本上下文全载体语义FULL，结构helper的72载体/522 pointer导航也不是读完载荷的证明。无关其它delta领域没有被新开成全域source审查。

本人已全文接收 [battle-controls-crosscheck.md](battle-controls-crosscheck.md)、[optional-audio-crosscheck.md](optional-audio-crosscheck.md)、[identity-scope-audit.md](identity-scope-audit.md) 作第二检查。它们分别保留自身未读边界；其源FULL或身份/transport结果不计入本人实读数。双方独立语义结论相符，无未解决反证。

## 余项及门

本主语义范围内无PENDING阅读项、无材料limit、无候选语义修订要求。作者132身份与62静态核验的定位/资格已审读，但不变成本人的132/62项语义检查或业务执行。

协调主审仍须冻结本报告及账本、接收其它实际reader的资格结果，独立给出整批candidate门。实际共享正式整文件整合尚未发生；其后的actual integrated PASS、ACCEPTED、CLOSED依合同分别处理。本上下文没有改候选、正式规格、其它批、R、main或tag，没有提交或推送。
