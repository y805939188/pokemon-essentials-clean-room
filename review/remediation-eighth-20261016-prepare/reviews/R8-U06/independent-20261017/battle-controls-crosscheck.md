# R8-U06 战斗控制与成长交叉审查

本交叉审对 **GR8-CRE-001、GR8-COM-001～008 共9项的有限源语义判定均为 PASS**，未发现需要候选作者修订的新语义缺陷。判定依据是下列本人实读的固定源、完整9条合同及候选文字，不以作者132项身份核验、62项静态核验或旧审者的 FULL 声称替代语义检查。

这是父任务的专项交叉证据，**不单独授予整批14项候选 PASS、实际整合 PASS、ACCEPTED 或 CLOSED**。本人完整读取7份相关镜像；其余镜像、完整批次 readset、全部历史及 evidence 的整批阅读门未在本子审单独完成，详细界限见末节及独占台账。没有运行 Ruby、游戏、行为模型或宿主，没有媒体、真实存档/回放、像素或声音观察信用。

## 固定输入与角色

- 复核工作树：`/workspace/r8-u06-review`，候选 HEAD `16f986afc1c85e64131f1dc8c6f2477a79c04029`。
- 直接基线：`4575e80d041ab0c74a42e2e36399d05791dbaa5b`；已用 Git 核实为候选祖先。
- 参考源：`/workspace/pokemon-essentials`，HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。
- B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`、C35 `2460370f1e410bd49cc29e377b89662838aed2b3` 及原5caff来源/恢复路径按合同分别保留，不把历史批准转为当前行为免审。
- 实际审查上下文：`/root/battle_controls_review`，与候选作者分离。requested `gpt-6.1-sol / ultra / default / normal / Fast off`；actual model、effort、tier、speed、Fast 无权威 echo，逐项 `UNVERIFIED`。

下文 `C/` 是 `review/remediation-eighth-20261016-prepare/candidates/R8-U06/mirror/deliverables/final-specification-set/`；`R/` 是固定参考根 `/workspace/pokemon-essentials/`。行号对应本次实际读取的文件。

## 逐项结果

| ID | 判定 | 候选位置 | 本人源核查与结论 |
| --- | --- | --- | --- |
| GR8-CRE-001 | PASS，有限静态语义 | `C/pokemon-rules/wp19-attributes-ability-and-stats.md:164–180`；`C/creature-rpg/wp30-growth-learning-and-friendship.md:116–123`；`C/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:65–85`；两个目录 EV/ST 组 | 模板产物255/255与重算保持成立；普通分配先检查HP单项区间，产出1及0都不能绕过负上界，尚未总量夹限和此接收者首写。默认设施非内部成长早门、此前其它接收者/回调前缀以及未达参与者清空均被正确保留。源为 `R/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:113–219`、`004_Challenge_Battles.rb:40–97`、`R/Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb:5–90`、`R/Data/Scripts/014_Pokemon/001_Pokemon.rb:1085–1127`。 |
| GR8-COM-001 | PASS，有限静态语义 | `C/combat-requirements/wp40-commands-obedience-and-action-order.md:255–259`，同篇 `:184、218–231` | 示例明确 STALL；QUICKDRAW 概率身份另列，未把 TRUANT 的后段交替拒绝混入排序档。`R/Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb:69–72、140–149、848–858` 的默认0/STALL−1，与 `004_Battle_ActionAttacksPriority.rb:136–278` 及 `009_Battler_UseMoveSuccessChecks.rb:183–297` 的后段 TRUANT 门一致。 |
| GR8-COM-002 | PASS，有限静态语义 | `C/combat-requirements/wp39-battle-context-and-participants.md:96、159–181、310–318`；`C/user-interface/wp67-a-battle-interaction-and-presentation.md:60、343–346`；BC/Z目录 | 缺失首计数没有被改写为数值0；默认相等1v1先在玩家布局枚举失败，早于业主范围/建席/场景及专用中止捕获。显式2v1、玩家skip、NPC BC19/20和蛋输入分别保留。源为 `R/Data/Scripts/011_Battle/001_Battle/001_Battle.rb:365–381`、`002_Battle_StartAndEnd.rb:16–104、247–317`、世界核心 `001_Overworld_BattleStarting.rb:375–440` 及过渡包装 `002_Overworld_BattleIntroAnim.rb:51–152`。 |
| GR8-COM-003 | PASS，有限静态语义 | `C/combat-requirements/wp39-battle-context-and-participants.md:165、177–181`；`C/combat-requirements/wp40-commands-obedience-and-action-order.md:255–259`；M目录 | 正计数允许资格检查返回，原序全量建野生席而配置限制优先序的独立根保留。候选分别列建席0/1/3、实际存活0/3、全量0/1及普通活序0；AI登记、早peer/seen、晚形态检查未混为行动消费。反序、双健康、3v1、伙伴/蛋前门与不推自动胜利均正确，详细源链见下节。 |
| GR8-COM-004 | PASS，有限静态语义 | `C/combat-requirements/wp39-battle-context-and-participants.md:109–114`；BC-09 `:17` | 括注已改为消息与结果均有差异。`R/Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb:142–169` 在零可战斗玩家下，野生返回/写入1，训练家返回/写入0。原结果行113和BC09没有改动，不需要新增用例或重开旧no-battle根。 |
| GR8-COM-005 | PASS，有限静态语义 | `C/combat-requirements/wp39-battle-context-and-participants.md:271`；`C/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:207` | 两处均修为行走动画/预锁记录复位，未要求朝向恢复。源 `001_Overworld_BattleStarting.rb:306–329` 尾调用到 `R/Data/Scripts/004_Game classes/006_Game_Character.rb:356–360`；方向4/6各保持原值，有walk/step才重置pattern，动画计数与预锁归零。此前结束回调可改方向或失败，候选未否定该前缀。 |
| GR8-COM-006 | PASS，有限静态语义 | `C/combat-requirements/wp40-commands-obedience-and-action-order.md:167` | 火药仍导致失败；只对自损补上使用者有效天气非雨/大雨与可承间伤双门。源 `R/Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb:154–335`，尤其 `:310–323`，与 `001_Battle_Battler.rb:518–533、561–565` 一致。雨/大雨或Magic Guard可跳自损但仍取消/结束行动；原始天气压制仍在后，PP与历史前缀未被抹去。 |
| GR8-COM-007 | PASS，有限静态语义 | `C/combat-requirements/wp40-commands-obedience-and-action-order.md:337`，同篇`:210–216` | 具名世代消费者已改为王者盾牌接触反制。源 `009_Battler_UseMoveSuccessChecks.rb:303–526` 中 `:367–378` 明确世代≥8请求降攻1、旧代2并阻挡命中；`008_Battle_AbilityEffects.rb:720–735` 的HYPERCUTTER是独立外来降攻免疫。中央资格、反转/单纯/镜甲及后继回调边界未被配置表短句改写；原§5.3保留。 |
| GR8-COM-008 | PASS，有限静态语义 | `C/combat-requirements/wp41-switching-positioning-and-escape.md:75–104、201` | 不变量已与正确详约一致：派出后按配置更新该席位缓存，再完整入场。源 `005_Battle_ActionSwitching.rb:142–226、274–374` 及完整 `004_Battle_ActionAttacksPriority.rb:136–278` 表明入场消费缓存速度，增量不重抽档/平局且不插入新条目。开场全算→入场→另一次增量→forms在`:303–310`独立存在，候选没有删去或否定。 |

## COM002/003 的独立反证与消费链

1. **零计数默认例**：玩家一名健康非蛋、无伙伴/DEBUG/覆写，唯一已有合法非蛋P由HP1单改HP0。持久HP设置允许该状态（`Pokemon.rb:246–250`），计数资格排蛋并要求HP正（`:264–270`）。计数生产只在遇到合格成员时建立该段（`Battle.rb:365–381`）。野生同步先把默认相等两侧改为缺项，玩家枚举随即失败（`StartAndEnd.rb:30–55`）；不应复用稍后的NPC invalid-owner错误或受控abort0。
2. **显式2v1**：只把野生一侧改为缺项，玩家需求先从2降至1；野生在该需求循环被跳过。资格可继续到后继布局消费者。场景初始化先构造目标菜单，目标菜单在计算最大布局时需要比较双侧（`Scene_Initialize.rb:14–48`；`Battle_Scene_Menus.rb:459–502`），故不能把默认相等例的首失败复制到此输入。候选用“后续布局消费者才可能首先失败”正确限定依赖正常的可达范围。
3. **旧NPC与更早skip**：已有NPC全濒死队非空可过构造，但没有野生同步，BC19先需求/计数范围失败；BC20的中间空计数可在数量比较先失败。候选旧§4.3第3项与BC19/20完整保留。玩家自身零可战则先skip；包装生成与直接核心skip的不同先后仍由WP39§3.1保留。
4. **正计数原序例**：已有[P HP0,Q健康]、玩家仅一名健康，初始2v2同步1v1。野生建席完整遍历原输入（`StartAndEnd.rb:120–165`），故P1/Q3及早peer/seen/used都存在；玩家分支才做可战过滤。全量优先序只遍历配置最大索引（`Battle.rb:208–210`、`Priority.rb:136–176`），得到0/1；普通活序过滤昏厥后只有0（`:264–278`）。
5. **AI登记不是调度**：AI包装依实际对象构造并刷新（`001_Battle_AI.rb:14–68`），命令阶段按实际对象长度扫描（`009_Battle_CommandPhase.rb:174–265`）。普通CATERPIE不含传说标记，野生技能档0；换人、道具、Mega前门及有效TACKLE/STRINGSHOT正权重均已沿真实接收链核对。`AI_ChooseMove.rb:23–137、232–392`可以给Q登记行动。攻击的普通、MoveNext和Quash三类消费都重取既有优先序（`010_Battle_AttackPhase.rb:102–171`），增量也只遍历已有条目（`Priority.rb:177–215`），均不补Q3。
6. **入场/场景/裁判分离**：开场请求全部实际存活索引，但完整入场按缓存速度序消费；随后全实际存活者形态检查仍可见Q（`ActionSwitching.rb:303–374`）。场景精灵/数据框初始化使用全部实际席，单侧尺寸1不做2/3席偏移查表；野生叫声、数据框出现和恢复色调则按配置人数（`Scene_Initialize.rb:14–92、183–190`；`Battle_Scene_Objects.rb:28–103`；`Battle_Scene.rb:36–53`；`Scene_PlayAnimations.rb:5–55`；`Battle_Scene_Animations.rb:64–79`）。这只支持请求集合，不支持真实画面/发声保证。裁判按参与队伍可战计数（`Battle.rb:348–350`、`StartAndEnd.rb:557–567`），不能由Q漏行动推出自动获胜。
7. **必要控制**：反序[Q健康,P0]仍1v1但Q1入序；双健康且玩家一名健康变1v2，两野生均入范围；显式3v1且玩家三健康的最大索引4含Q3。伙伴额外业主在同步1v1后可能先无席位，蛋混合则在活动个体初始化拒绝（`Battler_Initialize.rb:60–91`）；不能套无伙伴非蛋例的全过程。候选Z01–05/M01–04均写为未执行静态向量。

零计数失败之前，世界核心开战记录、创建及清规则已发生；过渡正常进入时还可有战斗中标志、暂停音频、淡出/地图待机前缀。`BattleIntroAnim.rb:51–152`没有覆盖yield异常的局部必执行恢复；标准后段恢复、善后、Input更新及结果写回没有到达。候选明确保留远层宿主恢复未知，没有把它写成永久全局损坏或进程必退出。

## 累计保留与静态辅助核验

- CRE001保留GR-016/ST67的模板正常255、重算不规范化；EV0与252/252总504的正常对照；默认设施internalBattle=false门。WP28§6第6条原有“从受限状态增加”限制实读并保留；不把普通分配反例扩张到全部道具、Shadow或净化。
- COM001保留CM07/08、WP48 QUICKDRAW/STALL表及增量不重抽；TRUANT仍属执行拒绝。COM007与其不同位置/消费者，未合根。
- COM004原结果行113、原BC09；COM002/003原BC02、BC11–16、BC19/20；原测试编号和历史资格没有改写。
- COM005两处末动作纠正没有删中毒计数、Mega/Primal、伙伴治疗、可败治疗/等待或结束通知。COM006没有改正确WP47-A生产与前向、WP45天气三层和合格EOR尾清理。
- COM008详§4.1/4.2、EOR继续扫描/异常前缀、SW35、GR013及WP47B正确次序保留；配置false可留旧缓存。有限速度10/30与DRIZZLE/DROUGHT对照支持先更新缓存时晴→雨，延后更新产生反序只是错误实现反事实，未执行。
- 用Python/Git额外核实12份镜像与候选HEAD全字节相等；两个相关测试目录的整个原文件均为候选的完整前缀；WP40原§5.3/执行拒绝块、WP41原§4/EOR块和WP39原结果行保持。粗范围含已授权修改时不应宣称整块相等；未把这些结构核验当作源语义结论。

## 本人实读范围与接收界限

独占机器台账为同目录 `battle-reading-ledger.json`。本人完整读了根AGENTS、review-SKILL、候选README/independent-review/tagging-handoff、9条合同的全部7节及其附带证据/保留/验收/历史出处字段；并核实这些完整JSON记录与reviewer-prompt对应9个内嵌块逐值相等。review-SKILL明确不适用于审计报告，本次没有把它当成候选修订授权。

完整候选镜像实读7份：WP39、WP40、WP41、WP42、WP19、WP30、BC/CM/SW/G/R/E完整目录。属性测试目录实读1–91及334–356（含完整新增ST组及原ST67）；WP67-A实读1–77及324–357（COM相关开场/失败接收上下文）。WP51、WP47B、WP48和WP28读了台账列出的保留/消费条款，没有冒称通读这些只读整文件。主要源的完整文件/具名单元和额外上下文逐项在台账列出；未读的相邻源码不转为宿主材料限制。

批次reviewer-prompt其余AI/UI/optional完整块、完整readset所有载荷、所有evidence以及全部历史根伴件的整批阅读，未由本交叉审完成。已读history的WP39批准来源资格确认只是历史来源声称成立，未授权当前行为PASS；accepted-facts中与本9项无关的CREB内容没有声称实读。本子审的9项源语义PASS只能由父审与其它实际非作者阅读证据合并评估，不能单独关闭完整批次阅读门。

另有只读辅助上下文 `/root/battle_controls_review/secondary_control_probe` 对COM004–008提供同向PASS及真实范围回报；它没有写文件。本报告逐项源判断以本人的已列阅读为主，辅助回报未计入本人FULL信用。候选/正式规格/其它批均未修改；本子审仅写本报告和独占台账，未提交或推送。
