# B10 actual 影响复审 — B05

**PASS_SCOPED**；影响判定 **AFFECTED**。本角色新增必修问题0、阻塞0。

角色 `INDEPENDENT_AFFECTED_B05_ACTUAL`；范围：HP均分新caller→已接受HP写回、物品消费者与HP24–31持久化/终局边界；WP20§6.4。

## 冻结与独立核验

本报告 reviewed actual SHA 为 `ff68272b385254b0aa90a7fc23b22b3f8b4126c1`，tree `715cb48c7b563c24ffd3411c9b129856ff11b3bb`；候选 SHA 为 `3c6365a4ce35c3ef08e6ba53fd81a426ffd026aa`，已接受正式前驱为 `aef4e56ca2f7514f54b0c976fbdb400caef138b9`，行政重冻结为 `c4eed12c0b9963fd65e296dcc4ce1940b5277570`。报告提交 SHA 与 reviewed SHA 分开，由普通提交、推送和远端读回后的最终交接提供；不递归回填自身。

本独立工作树 `/workspace/B10-actual-affected-review` 和分支 `codex/cloud-dot-B10-actual-affected-B09-B05-B14-review-1-20261009` 从准确 actual 开始；actual 单一父提交是上述候选。origin fetch/push 均已核为 `https://github.com/y805939188/pokemon-essentials-clean-room.git`，远端 `codex/cloud-dot-B10-integration-1-20261009` 与冻结 actual 一致。已读根 `AGENTS.md`；该树无 `.agents/skills`。仅新增本次三个获派 actual 报告目录，不修改作者、正式文件、公共登记、参考源码、历史报告或其它 review 目录。

请求配置保持 `gpt-6.1-sol / ultra / default / Standard`。无可信 effective backend 回显，按 actual 请求沿用的 approved Plan A 记 **UNVERIFIED**；未收到明确 unsupported/downgrade 通知，没有主动降级、CLI/native 替代、模型/额度/认证探测或派生子任务。

依据 `integration-stage-1/actual-review-request.json` 的本角色条目及未变的 `refreeze-after-B14-C-1/B10-downstream-contract.json`。固定 ORIGINAL `93e10babe0b9c9ef8b3f5277754541b447beeeb4`、PLAN `41fffb540c6483f5296ea0d33b789b75180d27ed` 的7个完整对象、当前控制与 minimum 投影重新核对；shared003全部11个有效扩展保留。这里核验 qualified 登记身份和影响接口，未代替 full R-B10 的全部7项质量/2项最低语义判断。

共用冻结核验只做一次：**264项检查通过，0失败，179个唯一 commit/path 身份**；摘要 `0be58da625e536e6d7945eb355d7d07419034dd403ee95b1083d55afe2b8337f`。B09 的 `identity-checks.json` 保存完整共用对象，B05/B14按其SHA256引用，同一核验不被重复计成三次检查。每个角色的actual语义和影响结论独立。

两份完整未过滤差异均使用 `--no-ext-diff --no-textconv --no-renames --binary --full-index --no-color`，无路径过滤。前驱→actual：1,591,304字节、29,335行、74文件，SHA256 `4ba63d2f4d9c7a5f1a28ced719d786586840741f0cf51152ded530725820a51e`；候选→actual：945,002字节、17,707行、37文件，SHA256 `8faa01962a24fbe7bb7ebdbe1cfc4ea76456ded98135407e4e2de33c189ed3cc`。每个文件块均记录身份并分类：actual新增/变化仅24报告复制、10整合元数据、3公共登记。全部13正式文件与独立已审候选逐字相同；五原稿授权片段、正确65与原139成员及其它候选变化依据原独立 full 收据和精确版本复用，并在actual核验保留，不借作者自检重授质量PASS。没有把完整 diff 的存在、同blob或候选PASS自动转换为actual gate。

24个候选报告文件分别对照原报告提交 `8a657aab8406e9f175f398363303097d1768a7b5`、`ef233f54337a0f1a86c5f474a10d0dccdbc74791`、`0b873d7402a56975ccd29f838a2ff4ec7f90a481`，git blob/SHA256/长度全同；六个manifest角色、reviewed候选、verdict、各自三项非自身artifact散列及actual请求收据全部一致。Full/B04/B08候选只作为其原范围收据，不成为本角色对这些接口或actual门的新结论。自己的候选静态源阅读与历史有效证据按 `0b873d7402a56975ccd29f838a2ff4ec7f90a481` 及其中精确引用复用；actual正文/consumer/公共增量另作本轮判断，没有要求重新完整读历史或递归证明阅读。

两个TSV独立解析旧194记录＋header为actual原字节前缀，新增7个唯一B10贡献键仍 OPEN、INTEGRATED_PENDING_ACTUAL/NOT_ACCEPTED；接受贡献194、B10接受0，不能消费候选minimum或候选PASS。交接页仅新增1742字节前缀，旧历史后缀逐字保留；canonical ledger与B14-C接受统计/记录未变，正式接受仍10/21、specific minima128、strict119/9、canonical229 OPEN/0 CLOSED。shared003/B015接受贡献者与待办列表按当前已接受批次集合重新核对，B09/B14既有qualified限定未被pending登记覆盖。

静态目录独立重数：战斗159→161、规则155→168，314旧行字节、换行、顺序、重数全保留，新增15设计。请求的227条非连字符ID旧行包含在内，另87条BC-/CM-/SW-同样受保护；候选已核14个未变整节在actual整文件不变。这里是文本保留，不是执行结果。

只读参考仍为 `Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，读取过的17个文本文件身份再次匹配，工作树仍clean。沿用 U01–U10/G01–G12/AX01–AX20、current scope与完整具名限制：Scripts.rxdata及所有二进制/序列化数据；可执行文件/宿主DLL/mkxp配置；实际地图/事件/媒体/图片/音频/字体/soundfont/容量结果；八cup-list与pokemon_metrics样本；backup/gen；实际插件组合/动态派发/废弃别名/EventScene/动态阴影可达性；真实Demo链仍未证。参考/编译/转换/生成/反序列化、历史作者/审者程序均未执行；本次Git及新写Python仅做JSON/散列/文本账务。**行为向量执行0、运行观察0、已证Demo链0**。

## actual 条款、调用者与条件比较

### B05-ACT-01：实际caller与持久HP

actual WP46§6.4、WP44委派、覆盖表及原稿完整保留。进入局部效果求同一个m=floor((U.hp+T.hp)/2)，U先T后，各自夹上限、不重算、不守恒。51/60＋150/200→60/100；1/100＋2/100→1/1；59/60＋200/200→60/129。正常前门通过时HP经既有战斗→关联个体写回；与阶级清零无关。

actual条款：`deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md` §6.4；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md` MH39/MH40

### B05-ACT-02：治疗封锁与替身/保护分层

PAINSPLIT无治疗招标记，U仅正HealBlock不阻用，均分恢复不局部重查canHeal。目标未绕过替身/保护在更早目标门阻止本效果，故无局部均分反馈/两端检查；不推广为普通动作之后其它检查全部取消。物品消费者自己的恢复资格仍可拒U。

actual条款：`deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md` §6.4；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md` MH41/MH42

### B05-ACT-03：既有伤害记录保留

HP均分扣减不新增普通直接伤害、Counter/MirrorCoat/lastHPLost/来源/本轮受伤或跨半登记，不清旧值。恢复达到半HP按共享恢复规则清原跨半标记；无新登记不能误写成清空所有记录。

actual条款：`deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md` §6.4；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md` MH44

### B05-ACT-04：反馈后双端物品消费者

HP处理完成→反馈→U HP物品检查→T检查，即使原HP相等也执行。各50/100且双方有效ORAN、无其它能力/连锁/回调时，各恢复10→60/60并永久消费；HP与持物写回。无有效物品对照50/50但检查仍请求；独立邻近U正HealBlock且各50/100/ORAN时U保持50并持物，T60且消费。不得把请求称无条件恢复或忽略抑制/能力/连锁。

actual条款：`deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md` §6.4；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md` MH43

### B05-ACT-05：HP24–31持物与终局

WP20正文/原稿和HP-24–31所有旧行未变：邮件失配清理，未知个体入口忽略/战斗入口清空；正常永久消费清当前及匹配还原记录、临时Knock Off保留记录、永久取得按合法路径更新记录；新捕获入队登记当前持物，直接送箱新捕获个体不参加队伍还原。无伙伴实际参战、集合与队伍对齐、无再取得/回调、正常终局到达时ORAN消费后仍空，不能写战后必返还。

actual条款：`deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md` §6.4；`deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md` HP-24–31

### B05-ACT-06：限定B013与旧成员送箱

实际伙伴参与＋满队捕获移出旧成员可能保留旧共享参与身份而玩家记录左移；一次正常终局还原先于外层治疗/拾取，可将盒中旧成员写成后继物品、留队成员写空。新直接送箱捕获与旧成员被送箱不能混同；伙伴登记不等于参与，后续治疗不恢复持物。actual没有改身份/还原时点或重建记录。保留已接受B013反向证据，未重新审核B05其它16根。

actual条款：`deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md` §6.4；`deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md` §7.3 terminal boundary

参考文本只记录定位，不复制源代码：`PBS/moves.txt:6214–6226`；`Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb:1890–1922`；`Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb:75–115,410–437,590–602,655–675`；`Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb:1–37`；`Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb:210–353`；`Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb:345–387`；`Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb:665–722`；`Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb:10–30,340–370,505–527`；`Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb:360–403`；`Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb:475–516`。候选已独立阅读的固定文本按版本复用；本轮重新读取延迟攻击/HP均分/物品检查的关键片段并比较actual条件，没有执行参考。

## 结束条件与剩余门

本角色actual新caller、持久写回和qualified终局回归通过；没有REQUEST_CHANGES，不代替B04/B08/full角色。 发现问题时应由作者做最小修复并新冻结；本次无必修问题，因此最小修复清单为空。

本角色以精确actual报告普通发布及远端读回结束。父统筹仍须收齐同一actual的full、B04/B08和本次三个affected角色门，再由唯一登记者执行B10-C；本报告不记录接受、不关闭canonical、不宣称其它actual门已完成。后续B11需B10-C后重新冻结；B10/B15正式写串行及其它贡献者/最终全局门继续保留。没有扩为第三轮全局review。
