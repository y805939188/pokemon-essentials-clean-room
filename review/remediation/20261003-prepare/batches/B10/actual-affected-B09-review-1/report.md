# B10 actual 影响复审 — B09

**PASS_SCOPED**；影响判定 **AFFECTED**。本角色新增必修问题0、阻塞0。

角色 `INDEPENDENT_AFFECTED_B09_ACTUAL`；范围：shared003/B015：WP45/WP46离场来源清理传播、R10及P06/P07边界。

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

### B09-ACT-01：B015传播与存活集合

actual WP45§9.3及WP46§6.3 AttackTwoTurnsLater同候选；对照未变WP39§6.1/WP42§5.1阶段2。仅合格离场来源补建计算输入，先清当前存活成员指向保存来源席位的关系，再读当前来源个体。替补仍占该席也会失去刚建立的关系；在场来源复用无此次额外清理。

actual条款：`deliverables/final-specification-set/combat-requirements/wp45-weather-terrain-side-and-position-effects.md` §9.3；`deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md` §6.3 AttackTwoTurnsLater；`deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md` §6.1；`deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md` §5.1 stage2

### B09-ACT-02：精确清理值及不回滚

着迷/JawLock/MeanLook/Octolock/SkyDrop来源关系改−1；锁定正计数才同时清计数/位置，计数0旧位置保留；束缚计数与来源清除，TrappingMove身份保留。其它席关系保留。清理早于攻击资格/伤害结果，后续失手/无效不撤销。

actual条款：`deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md` P06/P07；`deliverables/final-specification-set/combat-requirements/wp45-weather-terrain-side-and-position-effects.md` §9.3

### B09-ACT-03：R10保留与早退反向

R10旧行在B/C/actual字节相同：普通1v1、非幽灵T攻击后仍存活、A后备可战斗、B占保存席0且T刚受其黑色目光。目标空/濒死或A不可用更早返回，计数1→0但无补建/清理，可残留招式和来源辅助值且不重试。可执行正常末尾恢复旧失败记录、濒死检查、清辅助值。P06/P07补足边界，均未执行。

actual条款：`deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md` R10；`deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md` P06/P07

### B09-ACT-04：shared003及实际登记边界

正文移除dummy/源组织要求，保留来源个体/目标席身份、替补关系的可见副作用与真实入口差异；不要求未来实现复制类或构造器。新增actual元数据没有新caller，没有改WP41拘束/换出规则。B015登记B09 accepted、B10 pending；shared003的B09/B14已接受范围和其它贡献者待办均保留。

actual条款：`deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md` §6.3

参考文本只记录定位，不复制源代码：`Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb:74–116`；`Data/Scripts/011_Battle/002_Battler/002_Battler_Initialize.rb:1–48,144–277`；`Data/Scripts/011_Battle/001_Battle/001_Battle.rb:440–458`。候选已独立阅读的固定文本按版本复用；本轮重新读取延迟攻击/HP均分/物品检查的关键片段并比较actual条件，没有执行参考。

## 结束条件与剩余门

本角色actual有界传播/回归通过，没有REQUEST_CHANGES；不授予整个B09或B10全局PASS。 发现问题时应由作者做最小修复并新冻结；本次无必修问题，因此最小修复清单为空。

本角色以精确actual报告普通发布及远端读回结束。父统筹仍须收齐同一actual的full、B04/B08和本次三个affected角色门，再由唯一登记者执行B10-C；本报告不记录接受、不关闭canonical、不宣称其它actual门已完成。后续B11需B10-C后重新冻结；B10/B15正式写串行及其它贡献者/最终全局门继续保留。没有扩为第三轮全局review。
