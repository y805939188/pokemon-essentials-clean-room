# R6-U04-A 作者候选交付

状态：`AUTHOR_COMPLETE_PENDING_NONAUTHOR_REVIEW`。仅完成三项 required 的隔离规格候选与作者静态验收；无独立 CANDIDATE_PASS、整合、正式接受或 CLOSED。本报告由候选作者撰写，不能作为独立终裁。

## 身份、实际环境与写集

- 准备提交：`469a268b92daed7b4d28d7fd0da75520cbb7228f`；作者分支：`codex/remediation-sixth-r6-u04-author-20261014`，从该固定提交建立。启动时工作区干净，未发现已有同名作者远端分支。
- 正式输入：`8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`。R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 实际 cwd：`/workspace/pokemon-essentials-clean-room`，执行环境 `ccarenv_b64_Y2NhcmVudl83ZGNmMjIyZDRlY2M4MTkxOWRmMDNjOGY3OTBmY2U2MA`。原 Mac 项目根等价映射为该根；未操作 Mac。合同指定 `/workspace/pokemon-essentials-reference-r6` 不存在，固定 R 只读对象读取等价使用 `/tmp/r6-u04-reference-objects`（bare，无工作树）；primary raw 缓存位于 `/tmp/r6-u04-inputs/`。
- 活动逻辑身份：`R6-U04-A`；平台任务路径 `/root`。要求模型 `gpt-6.1-sol / xhigh / default tier / default speed`。实际 model、effort、tier、speed、opaque task UUID 均 `UNVERIFIED`：本会话没有有效配置回显。按最新委派不启动 CLI 或额外代理追查，未更改认证、安全配置或服务。source_thread_id 是父线程引用，不冒充本作者任务 UUID。
- 唯一整合接收者按最新委派：`thread01a13a93-d1da-71e4-a488-63b8524f503d`（R6-I）。不以旧合同的角色或 source_thread_id 取代该接收者。
- 变更仅在 `review/remediation-sixth-20261014-prepare/candidates/R6-U04/`：mirror 的以下三份文件及本 evidence 目录。原 deliverables、公共 ledger/task-register、其它候选、旧证据未写。

| mirror 内正式相对路径 | 精确改动 |
| --- | --- |
| `deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md` | §2.1 自然之恩行（54）及新增两段（61–63）；§3 围攻行（93）及新增两段（105–107）；§7 场景数/目录（242）；§8 具名边界（248） |
| `deliverables/final-specification-set/combat-requirements/wp52-b-effect-coverage.md` | 仅第21行：天气/地形/移除地形仍§5.1，四危害失败改§5.2 |
| `deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md` | BE 标题75→86；B16只补预测开前提，预期不变；新增共同夹具（230）和B72–B82（234–244）；其它原测试行原样 |

各载荷 bytes/SHA256/blob 及完整文件集合见 `package-manifest.json`。`formal-only.patch` 使用正式相对路径，供整合者串行接收；不授权直接覆盖共享文件。

## 本人新读及证据分期

项目根 `AGENTS.md` 全文已读，遵循行为抽取、架构中立与不改参考原则。3527行作者合同按连续段 `1–320 / 321–880 / 881–1450 / 1451–1980 / 1981–2530 / 2531–3030 / 3031–3527` 全文读完；221692 bytes、SHA256 `f1bc00612214728cdeb5cebd82c71f21f857e329fe6a13d0cf0eacec1ae30974`、blob `bc8e0d52dd27bb4c2206aceda153f58cc2517db7` 全部吻合。独立读取 `contracts/R6-U04.json` 的全部字节并验证与已完整阅读的合同展开JSON逐字节相同，包含三个 scope_contracts 的七组及 original_full_proposal；未用摘要代替原提案。

固定正式全文：WP52-B正文240行（1–110、111–240）、coverage111行、测试目录294行（1–100、101–205、206–294）均完整阅读。固定身份由已读 helper 校验，又以实际 Git blob/mode/type复核。五份指定反证 EV-8dd3ec6afe1b1ada、EV-e0bd1ab619cc4c90、EV-1c4621c48f63b0f5、EV-8c075af60e244dcc、EV-9164b2d28833a017 全文读取并逐一核 bytes/SHA256/blob；其中 GR6-C-001 空槽反证与24隔离向量属于其它根因，不转记成本批执行。

主要 R 新读范围（路径以 R 根为起点）：

| 输入/消费者 | 本人新读范围 |
| --- | --- |
| `Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb` | 全文1–393：真实资格、独立门、类型准备、目标枚举、包装外初值、内层赋值、通用评分、最后权重与登记 |
| `Data/Scripts/001_Technical/001_Debugging/001_PBDebug.rb` | 全文1–77：普通异常捕获和诊断返回条件 |
| `Data/Scripts/011_Battle/005_AI/009_AITrainer.rb` | 全文1–100：作者Flags、Anti清理、中等32与高48门 |
| `Data/Scripts/011_Battle/005_AI/011_AIMove.rb` | 1–400及495–545：准备、粗类型、基数/普通粗伤全链、共享字段及会心历史接点 |
| `Data/Scripts/011_Battle/005_AI/007_AI_ChooseMove_OtherScores.rb` | 260–390，含297–323通用伤害消费者 |
| `Data/Scripts/011_Battle/006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb` | 1–210，含围攻151–185及双击/多击对照 |
| `Data/Scripts/011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb` | 1409–1450自然之恩；180–200压榨、435–475磨砺历史回归 |
| `Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb` | 1330–1390：真实起用、类型空守卫、基数空物查询与后段消费 |
| `Data/Scripts/011_Battle/003_Move/009_MoveEffects_MultiHit.rb` | 145–195：真实围攻只在使用阶段建立名单，无该族命令可选覆写 |
| `Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb` | 1–145：PP/安可/命令资格及NearOther目标门 |
| `Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb` | 1–110：命令资格；`003_Move/002_Move_Usage.rb` 1–100默认可选 |
| `Data/Scripts/011_Battle/005_AI/010_AIBattler.rb` | 1–100、270–305（item委托）；`002_Battler/001_Battle_Battler.rb` 60–95：当前物品查询；`010_Data/001_GameData.rb` 85–125：空输入try_get返回空 |
| `Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb` | 120–170：声音/穿透替身绕过及共同默认 |
| `Data/Scripts/011_Battle/006_AI MoveEffects/001_AI_MoveEffects_Misc.rb` | 325–465，含四危害失败及整体分；另回读天气/地形157–325作为定位对照 |
| `Data/Scripts/011_Battle/006_AI MoveEffects/006_AI_MoveEffects_Healing.rb` | 225–255：第五轮生命水滴独立守卫 |
| `PBS/moves.txt` | 625–650 BEATUP、5575–5600 NATURALGIFT；`PBS/items.txt` 5252–5260 ORANBERRY完整标志 |

额外消费者都绑定同一 R commit/tree/blob，已登记 `new-reading-ledger.jsonl`；未扩大作者写集。初始读取发生在记录器建立前，精确UTC未捕获，保留为 `UNVERIFIED/NOT_CAPTURED`，不从文件mtime补造。后续读取器和验证进程保留实际argv/cwd/UTC/exit/stderr。个别过长工具显示曾被截断，所需合同/正式全文已用上述无截断分段读取；历史大JSON只采用具名对象/字段投影，不宣称其全文件语义复审。

证据等级：`SOURCE_STATIC`＝上述新读与人工核对；`DERIVED_VECTOR`＝B72–B82及下列人工路径推导；`TOOL_VALIDATION`＝337项输入身份、文本保留、目录定位、结构和常数算术检查（两次exit0，首轮保留），Python进程exit0；`ISOLATED_REFERENCE_EXECUTION / INDEPENDENT_MODEL / COMPLETE_HOST_DEMO / real save / production service` 均 `NOT_EXECUTED`。不加载R、不生成/运行评分器、不运行游戏或Ruby定义。安全验证仅已审Python文本/哈希/整数算术及Git只读对象操作；无未知程序、序列化执行或真实用户存档。

## GR6-CA-EB-001（required/P2）七组

1. **身份与裁决**：无别名，同名根因；主合同原WP52-B§3第89行。保留原提案与R6-CA非提出者反证，执行固定root的required/P2裁决，不把常规异常总述当作原文保证没有异常。
2. **双向证据/必要消费者**：AI MultiHit151–185分别登记失败、合计基数、目标分；AITrainer55–87允许只关预测。ChooseMove25–42真实资格后按预测门，65–68包外设100，232–285评分完整返回才赋值，294–310评分门仍可调用专属目标分。AIMove81–106/367–374表明围攻普通粗伤不因合计0早返，至少1基础量后返回；目标分重数n并除n。反向由候选正文§3与B72–B76可回到这些固定源；真实围攻155–180、WP46§3.1只定义使用时名单/逐击，未替AI前门拦截。无保存消费者；最终概率/动作在后续WP51，不冒称已到达。
3. **前提、反例、部分提交**：合法普通内部训练家单打已到选招；技能32/AntiPredictMoveFailure/评分开，U真实中毒、仅U业主队伍（或全可战成员真状态），默认BEATUP/PP正、无其它选择障碍；T存活合法敌、正替身、本招不绕，正攻防HP、无持物、无粗伤先行异常，诊断器正常返回。n0时先粗伤后除人数，异常早于严格破替身比较及通用目标分；外层未完成赋值，候选100保留。无取消，无本处HP/阶级/PP/物品提交，无动作登记；类型/模式破坏准备已发生，不补事务回滚。诊断器自身失败、其它能力/持物异常和最终选择不在本反例保证内。
4. **最小实际修订**：§3行93限定“空名单预计失败”受预测门；105–107展开合法n0入口/首次异常/包装出口与四对照；B16补预测开前提，新增B72–B76，§7/§8同步。保留P27、名单含合格U、正常n、替身严格小于、真实逐击合同；不修参考、不实施安全守卫或未来永久兼容政策。
5. **验收与回归**：B72异常/100；B73只开预测→20、目标评分NOT_ENTERED；B74只添健康无状态种族攻100队员→n1/P15、破替身界0、继续通用修正；B75仅去替身→不发生本处除零、通用粗伤仍执行；B76只关评分→目标评分NOT_ENTERED。均人工静态推导。工具核旧测试保留、P27与n1常数边界、输入源身份；不是执行这5条。R1/R2/R5精确保留span见历史表。
6. **独立审查**：本作者仅自检；指定R6-U04-R的非作者ultra审查由父线程候选发布后另派，当前`PENDING`，不能自签。
7. **依赖/接收**：WP51独立标记/资格/异常包装、WP52-A通用目标评分/权重、WP46真实围攻均非阻塞作者依赖。候选两路径交R6-I；原同步要求的`audit/source-traceability.md`由R6-I在实际接收后同步，不在本作者写集。共享测试目录与R6-U02候选串行合成，保留双方新增条目。

## GR6-CA-EB-002（required/P2）七组

1. **身份与裁决**：无别名，同名根因；主合同原WP52-B§2.1第54行。按固定required/P2裁决补具名合法无物入口，不将有物但标志不完整的正常0基数也写成异常。
2. **双向证据/必要消费者**：AI MoveAttributes1423–1436的失败与基数分族；真实MoveAttributes1338–1380的类型查询有空守卫，基数查询先读取当前物身份，再查完整数字标志，空物先失败。Battler81–83→GameData109–115确认空物非虚构NONE对象。ChooseMove142–156准备可安全继续，294–310通用目标评分→OtherScores297–323伤害消费者→AIMove81–92中等基数，故不要求本招有专设目标评分才触发。异常出口同包外100/未完成赋值/正常诊断返回。正文§2.1与B77–B82反向到上述链；WP47-A真实起用/续击定义保留，无新增保存/显示成功主张。
3. **前提、反例、部分提交**：普通内部训练家单打已到选招，无先行换人/用物/已有选择；技能32、AntiPredictMoveFailure、评分开，默认NATURALGIFT/PP正、U无物且真实可选门放行，T为正常存活敌、正攻防HP、无前置评分异常、诊断成功返回。类型一般成功，通用粗伤进入专属基数，缺失物品身份先异常，无正常1或0。候选初100保留不等于威力100/最终动作；不扣HP/PP、不改状态或消费物品，准备字段不统一回滚，无菜单取消。
4. **最小实际修订**：§2.1行54区分预测门/中等基数/有物正常缺值；61–63补缺失查询与包外出口、开预测/完整果/缺值/评分关/低档对照；B77–B82与§7/§8同步。真实无果起用失败、67默认数据、完整标志至少10、有持物无完整标志1→0均保持；不补getter或评分守卫。
5. **验收与回归**：B77无物异常/100；B78只开预测→20、基数NOT_ENTERED；B79有效ORAN完整NaturalGift_POISON_80→P80、不由评分耗果；B80存在有效树果但仅前缀无完整数字→正常1→0，与无物分开（作者数据边界，非默认PBS样本）；B81只关评分→伤害消费者NOT_ENTERED；B82技能31且显式保留评分、预测关→P1先替60、跳专属基数。全为静态设计。工具核ORAN固定数据、旧行保留；不执行这些6条。GR3-M08-001的真实第二击空物异常时点/已提交HP71前缀不由本次AI包外100替代。
6. **独立审查**：`PENDING_R6-U04-R`；原提出者支持、旧反证、337工具检查均不是本候选独立通过。
7. **依赖/接收**：WP51标记/异常包装、WP52-A通用伤害消费者、WP47-A真实类型/数据/起用/续击边界；均不阻作者候选。交R6-I接收两镜像并按实际整合同步audit；共享测试与R6-U02须合成。无新增政策或运行前置必修。

## R6-CA-EA-P001（required/P3）七组

1. **身份与裁决**：原ID保留，无别名；导航缺口P3，不计AI运行缺陷。
2. **双向证据/消费者**：Misc358–362菱≥3、386–390毒菱≥2、414–418隐岩真、440–444黏网真是四个整体失败登记，ChooseMove38–43/177–191在预测开且合法候选时消费，失败20。主稿§5.2仍有这些正确条件；原coverage21末“均§5.1”使读者/测试设计者错到天气收益。整体效果分coverage23已正确§5.2，作为普通对照。
3. **前提/反例/影响**：读者从AddSpikesToFoeSide失败登记只循§5.1找不到满3层失败；§5.2可找到。没有运行前提、菜单取消、资源提交或动作改变，不声称影响实际评分。
4. **最小修订**：仅coverage21拆分定位组：天气/四地形/RemoveTerrain保留§5.1；四危害失败§5.2；其它身份/copy/整体分/正文条件不变。新候选正文危害在186行（基线178），采用稳定§5.2导航，不机械保留已位移的旧行号。
5. **验收与历史回归**：四个身份全部映射到§5.2，天气/地形仍§5.1；工具核cover全体英文身份/copy顺序完全一致、仅一行变更、原危害行为段逐字不变；正文§5.2与B39等原行保留。静态定位比较，不需要行为模型/参考运行。
6. **独立审查**：指定非作者审查待父线程安排；作者不宣告独立PASS或关闭。
7. **依赖/接收**：唯一主批R6-U04；coverage文件仅本批候选，仍由R6-I唯一正式写者接收。无作者阻塞依赖，不因导航项扩运行/架构范围。

## 精确历史与接口回归

以下是本次受影响span/接口的新核对，不把旧PASS转签到新增异常。工具以固定main作旧字节基准，除7个明确替换旧行外保留所有旧行。

| 历史资格/接口 | 本次实际核对与保留结论 |
| --- | --- |
| R1原WP范围：WP52-B-R01 | 复读`review/wp52b-wp52c-wp54-recheck-2026-09-28/report.md`原R01与源资格/压榨局部。候选保留压榨PP0普通候选早拒/确达处理器缺失查询、PP1/2=200/80、负PP短路50；B04/B04b/B04c原字节保留。原R01不是围攻/自然之恩新增边界已验收凭据 |
| R2的229/21/341精确贡献资格；GR-015接合 | 复读2026-10-01原report§3与recheck-v2；新读AIMove495–545及AI MoveAttributes435–475，核当前表与B12b原行。旧16/8/4/3/2截到4得2、局部115；新24/8/2/1截到3得1、局部60。负下标旧2/新1均仍满足粗伤近似≤2，不改为真实必会心。B12/B12b及整段磨砺原样；总数只保留历史资格，不宣称重审341贡献 |
| R3 23/76；GR3-M08-001跨域 | 读取`required23-acceptance.json`该完整对象与当前WP47-A§3.1/§3.1.1及WP46§2.1.1/§3.1。首击ORAN自耗后U71/160、C/I/R/P/Belch前缀、第二击首次缺物查询、高HP101与单击对照保持。没有把AI评分包装异常等同真实续击继续；这些正式文件字节未改。M09 optional/U08历史未启动与M02 no-required不重开 |
| R4当前17/76与B5原16/75 | 当前修订不替换R4已有贡献；R4-U04的PP恢复是实际主动道具资格，不能被本批“候选无物/全状态仍可选”推成无资格检查。保留WP51真实选择前门、B04分入口、已知Summary残余范围。R4/B5身份与范围分列，未拿旧时点WAIT/FAIL重开已接受项 |
| R5唯一92CLOSED精确选择 | 新读activation-receipt的唯一键/保留历史、closing-candidate中GR5-M09-001完整选择对象、U05 task-packet该具名守卫/向量/反证/验收及当前accepted ledger具名字段。92关闭由13fddb候选+044c348审查及12df95/0378dc激活绑定，不扩成整领域PASS。候选生命水滴行（原119→127）及B64–B71原字节逐行保留，原100/107/95、封锁盟友、预测开/评分关/HP意识关/自身封锁早拒全部不变；AI Healing225–255新读确认评分独立守卫。其余历史G03/G09 FAIL、U03定向修复、两advisory MISMATCH与SC体内LF纠错保持原件 |
| 必要共享消费者 | WP51§2/§5、WP52-A§1–§3.1、WP47-A§3.1/§3.1.1、WP46§2.1.1/§3.1新读并验证固定main原字节未变；普通预测门、类型准备、目标通用伤害、权重/实际出招与真实消费的责任均未改。共享测试AB/AI/AE前缀及CE全文原样，所有旧测试行除B16加明确前提均原样 |

不以此宣称整仓R1–R5重新通过；第五7optional/7no-required/6policy/13limits、R6新增政策与L14元数据限制继续隔离。新增问题仅处理本批3个required；没有新增实质语义阻塞。

## 接收、复审与未闭合项

作者静态检查结果、源身份与逐条检查在 `static-validation-run02.stdout.json`，真实进程回执在 `static-validation-run02-process.json`（首轮原结果/回执另保留）。`patch-reconstruction.json`另记录补丁只在临时目录对固定main应用，三份文件逐字重建候选成功；这仍是TOOL_VALIDATION。候选载荷还需指定ultra非作者针对发布commit/hash新读。之后由R6-I接收，测试目录合并R6-U02贡献，再对实际共享全文、受影响接口和历史span独立复验，才能正式接受/关闭。原audit同步要求交由唯一整合者执行；本作者不写公共台账。

剩余门：非作者候选复审、唯一写者实际整合、共享全文/接口/精确历史回归、正式接受、CLOSED登记均待办。模型配置回显缺口为UNVERIFIED，不妨碍已授权作者静态工作完成。完整宿主/媒体/原生行为、任意插件组合、真实保存/生产服务均未执行，不转为通过。
