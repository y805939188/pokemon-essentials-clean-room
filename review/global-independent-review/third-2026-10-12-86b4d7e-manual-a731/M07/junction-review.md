# M07 交界复核

审查角色 `/root/m07_battle_session_v3`；参考固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，正式规格固定 `167296dbe9e2384627b0ed696e87aeb01f211252`。下表判定只覆盖 M07 的来源、前门、输出与消费者；跨模块最终裁决交独立主角色。全部为静态阅读，运行/案例执行/已证 Demo 链均 0。完整源文件身份和精确范围见 `file-coverage.tsv`、`capability-coverage.tsv`；所有十份分配规格 blob 见 `input-identities.json`，不能用这些身份计数代替行为审查。

以下源路径的公共前缀为 `Data/Scripts/011_Battle/`。世界入口前缀为 `Data/Scripts/012_Overworld/002_Battle triggering/`。

| 分配交界 | M07 正常/失败/边界判断 | 具体证据与当前条款 | 消费者、状态与未决 |
| --- | --- | --- | --- |
| G4-3 Mega/Primal 分入口 | 普通换下没有统一解除；入场是进入原始形态。正式失能显式解除；世界返回按玩家/伙伴全队解除。显式中止不保证正常终局清理。 | `001_Battle/008_Battle_ActionOther.rb:180–200`；`002_Battler/003_Battler_ChangeSelf.rb:64–99`；`002_Battler/006_Battler_AbilityAndItem.rb:5–28`；世界 `001_Overworld_BattleStarting.rb:306–328`。WP40 §7.2、WP41 §4.3、WP42 §7/8。 | M04 WP22、M06 WP38、M09 WP55/58；M07调用支持，跨模式恢复 PARTIAL。WP41 §4.2 的“Primal还原”用语易混，但§4.3及WP40已有明确方向，暂不新增必修。 |
| G4-5 参战标记下标 | 派出按侧内位置写，正常终局按队伍下标读；不替参考纠正为稳定个体身份。 | `001_Battle/005_Battle_ActionSwitching.rb:289–297`；`001_Battle/002_Battle_StartAndEnd.rb:506–509`；`007_Other battle code/004_Battle_Peers.rb:53–59`。WP41 §4.1、WP42 §6、E07b/E08b/E09b。 | M04 BURMY离场形态、M09回放消费者；M07两端 SUPPORTED_STATIC。形态处理器与图鉴消费者非本轮全域签署。 |
| G4-6 副本与持久字段 | 特性局部、物品指定入口同步；初始化拒蛋；空队伍拒绝与可战斗计数的首个错误分开。接力与非接力不是同一清理。 | `002_Battler/001_Battle_Battler.rb:58–130`；`002_Battler/002_Battler_Initialize.rb:36–91,93–280,285–324`；`001_Battle/002_Battle_StartAndEnd.rb:16–104`。WP39 §4.1/4.3/6，BC19/20。 | M04 WP19/20，M07 WP40/41/42；主要写回支持，全部接力效果消费者 PARTIAL。 |
| G4-7 异常/阶级状态层 | 五持久异常与临时混乱/着迷/畏缩/剧毒累计不同。施加查询不写、提交不重查、立即连锁治疗不抹去已发生反应。正式失能先清临时再清持久异常；普通换下不治持久异常。 | `002_Battler/004_Battler_Statuses.rb:25–271,425–574`；`002_Battler/005_Battler_StatStages.rb:9–300`；`001_Battle/011_Battle_EndOfRoundPhase.rb:207–252,320–389,713–779`。WP44 §2–5/8。 | M04 WP20、M08反应处理器；M07中央层 SUPPORTED_STATIC，外部完整注册族不代签。 |
| G4-9 当前数值与修正管线 | 先阶级截断，再各自 P/A/D 舍入夹限，基础两次整数阶段，最终倍率只末端一次舍入。模式破坏者连用户盟友段也跳；多目标按当前列表长度。 | `003_Move/003_Move_UsageCalculations.rb:239–484`；`002_Battler/001_Battle_Battler.rb:91–103,248–287`。WP43 §6，TD12–17；WP44 §8，SS25。 | M04派生值，M08 WP46/48/50；M07核心支持，完整倍率处理器 PARTIAL。未知处理器不得按倍率1。 |
| G5-1 成长门 | 野生音乐门先于内部/经验开关早退；关闭时不清参与。空记录跳过与有效参战数0不同。只玩家本人可战斗接收者先EV后经验，处理后清记录。最大Exp与零经验不会统一刷新场上副本。 | `001_Battle/003_Battle_ExpAndMoveLearning.rb:5–224`，世界 `001_Overworld_BattleStarting.rb:112–132`。WP42 §4，G01–13。 | M04 WP19、M06 WP30/Shadow；M07门/集合/同步 SUPPORTED_STATIC，Shadow写入及完整UI消费者 PARTIAL。 |
| G5-2 战后进化时序 | 世界返回先异常计数/变身/伙伴治疗，再结束通知的进化检查，之后才清战前记录。只有2/5被关闭“所有战斗后”配置排除，0/3仍可进检查。扫描每成员一次。 | 世界 `001_Overworld_BattleStarting.rb:306–328,608–652`；`003_Move/002_Move_Usage.rb:294–304,399–403`；失能清直伤 `002_Battler/003_Battler_ChangeSelf.rb:90–94`。WP42 §7.1。 | M06 WP31/32、M10进化取消/展示；M07前后写入支持，进化条件/取消及NINCADA附加个体 PARTIAL。 |
| G6-3 持物消费/还原 | 正常终局先捕获接收再按届时记录还原玩家侧参与集合；还原记录可更新，伙伴合并列表可与当前玩家顺序分离。只一次终局遍历，不能补第二次移位玩家遍历。 | 世界 `001_Overworld_BattleStarting.rb:183–201`；`001_Battle/002_Battle_StartAndEnd.rb:479–510`。WP42 §6、E14；历史B013精确来源见 `regression-review.json`。 | M05物品容器，M06接收，M08持物，M09设施；M07终局消费者支持，捕获左移/存储无clone未新全文读，PARTIAL，保持旧有效反例范围。 |
| G7-5 命令UI与选择/执行 | NearAlly初选使用存活同侧序，三席0活/2倒/4活能登记远4；执行解析按真正邻接拒远且无近活兜底。2活先2，全部非自身盟友倒下才初选自身。物品登记扣库存早于执行资格复检。 | `004_Scene/003_Scene_ChooseCommands.rb:326–445`；`001_Battle/004_Battle_ActionAttacksPriority.rb:103–130`；`002_Battler/008_Battler_UseMoveTargeting.rb:36–90,173–201`。WP40 §4.3、CM31。 | M10 WP67-A；M07登记与执行 SUPPORTED_STATIC，按钮像素/素材与宿主不观察。新退款后终局消费者另见GR3-M07-001。 |
| CHAIN-1 伙伴/捕获/持物/存储 | 伙伴实际参战才形成独立合并列表；仅登记伙伴未参战不构成B013。正常满队、有盒位、接收完成再还原；送盒旧A可被后继Y覆盖，留队B空。 | 上述G6-3源及WP42 §6；E14。历史有效主夹具无需KnockOff，CP20训练家Snag另有合法前提。 | M05/06/08/10；PARTIAL：M07实际重读编组/终局，接收内部用精确历史证据限定复用，不签完整捕获链运行。 |
| CHAIN-4 设施提交/恢复/异常 | 裸战斗内部标记可关经验/金钱；正常终局与显式中止清理不同。M07没有设施提交/报名/快照恢复的额外保证。 | `001_Battle/003_Battle_ExpAndMoveLearning.rb:5–8`；`001_Battle/002_Battle_StartAndEnd.rb:247–347,352–403,405–511`；WP39/42。 | M09 WP54/55/56/58、M10、M12；PARTIAL。nil/空报名、等级/物品快照与异常落盘的完整设施门本轮M07未新审，交主角色；不据正常核心推理自动补恢复。 |
| CHAIN-7 Arena/攻击记录/回放 | 普通使用核心在各具名阶段写成功/失败、实计击数、类型累计，再更新技能；指令普通入口恢复已行动轮但不回滚PP/最近招。随机与记录输入不可统一为一份保证。 | `002_Battler/007_Battler_UseMove.rb:403–577`；`003_Move/002_Move_Usage.rb:369–404`；WP40 §5.2。 | M09 Arena/录像，M10/M12；PARTIAL：特殊覆盖/回放消费者未新全文审。B030保持原非必修裁决，不增加记录字段义务。 |
| CHAIN-8 世界呈现/时序/目标几何 | M07仅签三席邻接、命令目标与世界入口正常返回时清预置/战斗中标记；无异常finally保证。过渡分派读取位置/昼夜，实际媒体缺失。 | `001_Battle/001_Battle.rb:505–577`；上述G7-5；世界 `002_Overworld_BattleIntroAnim.rb:59–188`；WP39 §7/9与WP42 §7/8。 | M03/M05/M10/M11；M07静态边界支持，世界计时/消息/34场景全链与资源未代签，PARTIAL。 |

## 新交界：失败退款 → 正常终局

`GR3-M07-001` 是本轮新证据，关联 M05 WP28/27、M07 WP40/42、M10 物品UI。默认 Potion 两次正常登记给同一缺1HP后备：两次都通过选择门；第一件治满并清消费身份，第二件资格失败先退款，却保留消费身份。两名玩家使用者一直存活，无中间换人/清选择/新命令阶段；唯一野生HP1普通中毒、无治疗，合法无伤害行动之后回合末倒下并正常终局：库存2→0→1→2。若对手撑过回合并进入下一命令期，直接清选择，库存保持1。玩家使用者先正式失能则选择已清，不能套重复退款。

来源精确链：`001_Battle/006_Battle_ActionUseItem.rb:34–74,87–101` → `001_Battle/011_Battle_EndOfRoundPhase.rb:207–238,700–706` → `001_Battle/005_Battle_ActionSwitching.rb:142–146` → `001_Battle/002_Battle_StartAndEnd.rb:501–504` → `001_Battle/009_Battle_CommandPhase.rb:13–22`。默认物品资格/效果见 `Data/Scripts/013_Items/003_Item_BattleEffects.rb:66–79,333–337`、`PBS/items.txt:2942–2950`。当前正文没有失败保留身份与晚终局第二退款的唯一库存结果，必要修订是补写参考静态异常；未来独立实现是否修复历史缺陷另由用户决定，不自动要求永久复刻。

## 已转交 M08 的效果消费线索

`002_Battler/010_Battler_UseMoveTriggerEffects.rb:14–34` 中吞吐飞弹先变形，再读取形态分支；存活目标与已倒下目标的变形前门可能产生不同降防/麻痹结果。已经发给主角色，待 M08 独立核 WP49 正文及处理器。M07不擅自扩成完整特性族审查，未另增finding或抹掉可能异议。
