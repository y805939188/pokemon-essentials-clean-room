# WP67-A 首版有界审查（2026-10-01）

**结论：REQUEST_CHANGES；暂不进入 WP67-B。** 本轮提出14项P2行为修订和2项P3修订，共16项。登记及历史保护通过，行为稿仍有错误分支、等待时机和测试预期；首版自检中的一致性通过不能据此作为验收结论。

审查对象：[WP67-A主稿](../../specs/ui/wp67-a-battle-interaction-and-presentation.md)，SHA-256 `b6fdd96ae201d67637f71795193ea00c80cb7a7233e71c5bf597215eeb9935b3`，71,691字节。全文369行、K01–K42与入口附表均已检查。六份场景主文件及调试对照全文核对，相关调用者、目标数据、捕获／存放、成长和特殊模式定点核对。全部结论来自静态阅读，未运行战斗、UI、回放或行为模型。

## 1. 已通过的部分

- manifest §1共有1,133条完整SHA-256身份，另2条既有无哈希历史行；主TSV v68有1,038条唯一记录，完整身份与磁盘一致，阶段最终身份一致。
- 相对上一轮固定输入，既有文件仅矩阵、manifest、TSV变化；矩阵只改变F16-05。manifest旧§2／§3／§4内容按仅插入方式保留，主要标题未丢失。编辑过程的误删已经恢复，不作为未解决问题。
- 23份上游／边界规格、42份起始来源身份一致；WP65已批准范围与GR-001～016全部关闭结论保持。
- K01–K42标识唯一。入口附表实为八组54行，错误的是摘要中的40行计数（C02），不是哈希登记。

见[登记核验](registration-checks.json)、[输入与固定副本](inputs.json)、[矩阵差异](feature-matrix.diff)、[manifest差异](manifest.diff)。本审查只新增当前审查目录，未改主稿及登记文件。

## 2. 问题索引

下列行号均绑定上述首版身份；C02指首版交付摘要。R编号仅属于WP67-A，不沿用WP65或GR编号。所有项均为OPEN。

| ID | 优先级 | 必须修正 |
| --- | --- | --- |
| R01 | P2 | 分开物品列表、命令子菜单和目标画面的取消／拒绝 |
| R02 | P2 | 区分队伍列表取消、成员命令取消和换入可见门 |
| R03 | P2 | 补齐非单打零目标类别的窗口及空位置语义 |
| R04 | P2 | 确认框初始选中项与BACK返回值必须分列 |
| R05 | P2 | 可中止场景并不让所有等待立即结束 |
| R06 | P2 | 修正捕获图鉴场景前提与多个体接收顺序 |
| R07 | P2 | 保留WP38的投球容量门和无目标异常边界 |
| R08 | P2 | 将多个体派出的串行描述改为并行推进与本体等待 |
| R09 | P2 | Call的睡眠／命中分支只属于非暗影个体 |
| R10 | P2 | 回放无菜单只能描述通常命令路径 |
| R11 | P2 | 补足替补提议的实际门，并分开回合末逃跑路径 |
| R12 | P2 | Palace无力行动不可当作挣扎执行 |
| R13 | P2 | Arena禁止换人不等于没有换人入口 |
| R14 | P2 | 成长中的可见消息与两份招式状态提交时点要分层 |
| C01 | P3 | 区分图形与文本招式菜单的零总PP显示 |
| C02 | P3 | 入口表行数须按实际内容统计 |

## 3. 逐项证据和最小对照

来源路径均相对只读的 `reference/pokemon-essentials/`，固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。标识仅供审计，不是未来实现API。下列为静态推导场景，要求前序资源和未特别讨论的流程正常；直接触达、条件化入口和通常用户流程明确区分。

### R01（P2）：分开物品列表、命令子菜单和目标画面的取消／拒绝

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第128、134、141、144、320行；§5.1–5.3、K14、入口附表物品组。

物品的 Use/Cancel 子菜单取消被写成退出到主命令；任一校验拒绝又被写成背包画面不变。两条都会产生错误返回层级。

**应有合同：**未选物品而退出列表才回主命令。已选物品后在 Use/Cancel 取消，回物品列表。类型1/2/3在成员画面提交被拒，仍留成员选择；单成员／单场上成员的类型1/3自动提交被拒后，还会进入成员画面。类型4手动选目标被拒则恢复背包。

**修订验收对照：**

- 普通内部战斗，背包有药水：打开 Use/Cancel 后取消，应仍在背包列表，未登记、数量未变。
- 玩家队伍至少两名，选药水后对满HP且可战斗成员提交：给无效果消息，留在成员选择；再取消才回背包。
- 类型1自动目标只有一名且满HP：自动提交失败后打开成员画面，不能断言留背包画面不变。

证据：`Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb:196–324`；`Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb:100–137`；`Data/Scripts/013_Items/003_Item_BattleEffects.rb:66–78`。

### R02（P2）：区分队伍列表取消、成员命令取消和换入可见门

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第151、156、324行；§6.1–6.2、K18、入口附表队伍组。

成员命令的 Cancel 被并入 canCancel 的整屏退出合同；K18把蛋／昏厥成员的防御性验证消息写成普通菜单实际反馈；场景返回值与战斗包装的−1也混在一起。

**应有合同：**成员命令 Cancel／BACK只回成员列表，与能否退出整屏分开。列表取消才服从 canCancel。普通模式下蛋／昏厥成员没有 Switch In，通常只能看摘要或取消，不能沿该UI触发蛋／昏厥换入拒绝消息。−1是战斗包装未取得选择时的结果，不是场景方法保证的直接返回。

**修订验收对照：**

- 主动换人可取消，选一名可战斗成员后在命令子菜单选 Cancel：回成员列表；再在列表取消才回主命令。
- 分别选择蛋／昏厥成员：没有 Switch In；另用已在场的可战斗成员测试可达的拒绝提示。
- 强制替补时，成员命令仍可取消返回列表，但列表取消不能退出整个替补画面。

证据：`Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb:141–191`；`Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb:9–33,113–127`。

### R03（P2）：补齐非单打零目标类别的窗口及空位置语义

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第115、116、118、316行；§4.3、K08–K10、目标入口附表。

目标窗口被限定为目标数据需要选择的招式，多选显示模式被限定为2+；空字符串又被解释成对象不存在。这与实际显示条件和对象状态不符。

**应有合同：**普通手选招式登记成功后，只要不是双方各1席，就进入目标窗口；User／None等0目标类别也进入，使用不可移动的整体高亮模式。只有目标数为1才采用可移动单选模式。不存在的战斗者对象产生不可选标记；通过类别筛选但已昏厥的现存对象产生空名按钮；未昏厥才显示名字。

**修订验收对照：**

- 普通内部2v2，玩家手选有PP且可登记的SWORDSDANCE（User、目标数0）：打开目标窗口，自身按钮高亮、方向键不移动，USE确认，BACK回招式菜单。
- 分别给同一可显示位置设置现存昏厥对象与不存在对象：前者空名按钮，后者不可选；不得把两者合并。

证据：`Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb:60–97`；`Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb:333–438`；`Data/Scripts/011_Battle/004_Scene/005_Battle_Scene_Menus.rb:514–545`；`Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb:26–33,53–62`；`PBS/moves.txt:6541–6550`。

### R04（P2）：确认框初始选中项与BACK返回值必须分列

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第209、222、223行；§8.3、§9.1、相关确认和满队场景／附表。

确认框被写成默认No，满队命令又把99写成默认值；实际将取消返回值误当成了初始游标。

**应有合同：**每次命令框初始选中第0项。Yes/No框初始Yes；文本全显后不移动直接USE确认Yes，BACK返回No。满队去向框初始Add to your party；99只是BACK返回标记，随后由sendToBoxes分支解释。

**修订验收对照：**

- 普通非abortable场景、消息全显、无方向输入：确认框USE返回Yes，另开一框BACK返回No。
- 满队sendToBoxes=0、存放容量充足：不移动USE进入选换出成员；BACK走送盒。sendToBoxes=2时BACK继续循环。

证据：`Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb:267–307`；`Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb:15–34`。

### R05（P2）：可中止场景并不让所有等待立即结束

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第224、259、347行；§9.1、§10消息列、K34／K41、消息入口附表。

abortable被描述为任何消息／命令等待立即放行；K41又把回放暂停消息改普通消息等同于没有等待。

**应有合同：**abortable使消息文字自动快进，普通消息全显后仍有1秒计时，brief残留等待仍存在；普通暂停消息在非战末仍有3秒自动关闭计时。命令列表不因abortable而自动选项／返回。回放只把暂停消息转为普通消息，不能写成零等待。BACK经场景输入处理触发中止，须与普通取消返回区别。

**修订验收对照：**

- 回放场景、非brief普通消息、无输入：文字快进后仍等普通消息计时，不立即放行。
- 一般abortable场景中打开命令列表，消息全显后不输入：不会自动选择；BACK触发中止路径。

证据：`Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb:103–108,169–307`；`Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb:194–196`；`Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb:111–127`。

### R06（P2）：修正捕获图鉴场景前提与多个体接收顺序

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第214、335行；§8.2–8.3、K29及捕获接收附表。

K29输入未持图鉴，却预期图鉴新增消息与条目画面；多个体段写成命名→图鉴→存放，与本稿正确的§8.2相反。

**应有合同：**新物种的拥有记录仍可写入，但只有持图鉴且物种属于已解锁图鉴时才显示新增消息及条目。逐个个体均先图鉴处理，再命名，再存放，完成后处理下一个。命名画面还需非暗影、选项Give且确认Yes。

**修订验收对照：**

- 保留未持图鉴的K29反例：无图鉴新增消息／条目画面；满足命名门且选Yes时才进命名，随后入队。
- 另增持图鉴、已解锁、新物种、非暗影、Give且Yes对照：图鉴消息／条目→命名→存放。
- 两个待接收个体：各自按图鉴→命名→存放完成，不颠倒也不按全部图鉴／全部命名分批。

证据：`Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb:5–13,88–107`。

### R07（P2）：保留WP38的投球容量门和无目标异常边界

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第141、195、274、323行；§8.1、§12及捕获失败场景。

仓库满被单独写成禁球条件；目标已昏厥且无存活同伴时又被写成显示无目标消息后正常返回。两者均与WP38当前已确认边界不符。

**应有合同：**容量拒绝要求队伍已满且仓库已满，不能仅凭仓库满拒绝仍可入队的捕获。无存活同伴的直接触达边界在改取同伴后得到空对象，后续状态查询先失败，尚未到投掷消息／无目标提示。分开普通菜单保护、直接投球触达和已登记扣球前提，不承诺自动退球、回滚或整个进程必定退出。

**修订验收对照：**

- 仓库已满但队伍有空位、其他球门均通过：不因容量拒绝；再以队伍也满对照，才显示容量不足消息。
- 直接到达投球入口，索引指向现存昏厥对手且无存活同伴：在目标状态查询处失败，无两条预期消息。
- 如测试已登记扣球，则明确其先前扣减已发生；仅直接调用投球本身不等于发生背包扣减。
- 目标昏厥但另有存活同伴：可改取同伴继续，作为对照。

证据：`Data/Scripts/013_Items/003_Item_BattleEffects.rb:28–64`；`Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb:112–143`；`Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb:746–749`；`Data/Scripts/011_Battle/001_Battle/001_Battle.rb:458–460`。

既有合同／材料：`specs/pokemon-rules/wp38-capture-and-receiving.md:21`。上游保持原有批准状态，本轮修订WP67-A及其新交付材料。

### R08（P2）：将多个体派出的串行描述改为并行推进与本体等待

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第237行；§9.3、开场引用、动画附表及新增对照场景。

正文要求上一只球动画完成才播放下一只数据框，并将训练家淡出写成先完成的独立阶段；实际动画在同一更新循环推进。

**应有合同：**等待已有排列结束后，训练家淡出与各个体球动画共同推进；每只数据框只等待自己的球动画完成。多个体的出现可以错峰，但不是逐只全串行；各数据框完成且排列动画结束后才离开该等待段。

**修订验收对照：**

- 同侧一次派出两名且资源有效：两个球动画均随更新推进，各自数据框跟随自身球动画；不得以第一只球完成作为第二只数据框的唯一启动条件。

证据：`Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb:93–156`；`Data/Scripts/011_Battle/004_Scene/008_Battle_Scene_Animations.rb:385–524`；`Data/Scripts/011_Battle/004_Scene/007_Battle_Scene_BaseAnimation.rb:51–62`。

### R09（P2）：Call的睡眠／命中分支只属于非暗影个体

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第111行；§4.2、Call入口附表及新增场景。

暗影Hyper后平铺睡眠→治愈、命中→提升，遗漏外层暗影分支的优先级，会把非Hyper暗影误判为可唤醒／升命中。

**应有合同：**暗影个体单独处理：Hyper时解除并改心量，否则无效果。只有非暗影才继续检查睡眠治愈和命中提升。

**修订验收对照：**

- 训练家战具Call入口，玩家暗影成员非Hyper、处于睡眠、无调试中止：呼唤后无效果，睡眠保持。
- 非暗影睡眠成员同入口可治愈；非Hyper暗影且命中可提升仍无效果。

证据：`Data/Scripts/011_Battle/001_Battle/008_Battle_ActionOther.rb:31–62`。

### R10（P2）：回放无菜单只能描述通常命令路径

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第259、262、281、347行；§10、§12、K41、回放入口附表。

无任何菜单被写成普遍保证，与WP58已批准的自动招式／选靶例外冲突。

**应有合同：**常规命令由记录提供，通常不打开主命令和手选招式菜单；但自动招式入口在非单打、有效可用Encore且玩家所有的上下文仍调用目标窗口。标准回放通常按1v1重建导致此分支通常不可达，不能把布局缺失推为无交互保证。等待问题另按R05处理。

**修订验收对照：**

- 正常1v1回放命令走记录驱动，记录读取本身不打开常规命令菜单。
- 明确标为条件化入口对照：非单打上下文、玩家所有、有效可用Encore、记录FIGHT自动入口，仍调用目标窗口。不得声称未修复的标准双打录制能完整按双打回放。

证据：`Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb:198–222`；`Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb:36–57`；`Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb:92–97`；`Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb:384–438`。

既有合同／材料：`specs/combat/wp58-battle-recording-and-playback.md:138`。上游保持原有批准状态，本轮修订WP67-A及其新交付材料。

### R11（P2）：补足替补提议的实际门，并分开回合末逃跑路径

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第165、327行；§6.3、K20／K21、逃跑与替补入口附表。

提议条件被写成通常单打且未被束缚，并将野生拒绝替补后的逃跑指向主命令整套规则。实际提议门并不检查一般束缚，且回合末逃跑跳过保证逃脱／束缚整组。

**应有合同：**提议实际要求内部训练家战、Switch风格、玩家侧恰1席、对方替补、玩家首席存活且本轮未换、有可换入者、Outrage计时为0。不要将玩家侧1席收窄成双方1席，也不要把Outrage扩大为所有束缚。同意后进入选人仍可因换出束缚被拒。野生拒绝下一只后的逃跑保留禁逃规则，但跳过幽灵／必逃特性道具／拘束整组，也不增加命令逃跑计数。

**修订验收对照：**

- 内部1v1训练家战，Switch、玩家有健康后备、首席存活、Outrage为0且未换，但被一般束缚：仍出现换人提议；同意再选人时可显示换出拒绝。
- 玩家侧1席、对方2席的有效训练家战，其他提议门均真：对方替补仍可提议。
- 野生昏厥拒绝下一只且canRun=true：进入duringBattle逃跑计算，不套用主命令的幽灵必逃或拘束拒绝；失败再必须选替补。

证据：`Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb:142–215`；`Data/Scripts/011_Battle/001_Battle/007_Battle_ActionRunning.rb:60–158`。

既有合同／材料：`specs/combat/wp41-switching-positioning-and-escape.md:103`。上游保持原有批准状态，本轮修订WP67-A及其新交付材料。

### R12（P2）：Palace无力行动不可当作挣扎执行

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第257、345行；§10 Palace、K39、Palace入口附表。

抽样类别无合格招写成挣扎−2，危机消息又被简化成HP≤1/2即发生。这会把无力反馈变成一次实际攻击并错置消息时机。

**应有合同：**未命中抽样类别的合格槽时登记无力，虽内部承载挣扎对象，执行成功检查仍给无力消息并失败。玩家先经过Encore／无常规可选招门，可能转普通自动入口，不必经过性格抽样。危机判定在仍未终局的回合末，要求存活、非睡眠、尚未进入危机、HP不高于一半。

**修订验收对照：**

- 玩家有可用招，全部为变化类，抽中攻击类且无合格槽：无力消息，不执行挣扎攻击；不能靠改抽类别补救。
- 半血睡眠或已有危机标记：本次不再出危机消息；首次满足全部门时才在回合末显示。

证据：`Data/Scripts/011_Battle/008_Other battle types/003_BattlePalaceBattle.rb:78–165`；`Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb:42–64`；`Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb:191–205`。

既有合同／材料：`specs/combat/wp56-palace-and-arena-variants.md:66`。上游保持原有批准状态，本轮修订WP67-A及其新交付材料。

### R13（P2）：Arena禁止换人不等于没有换人入口

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第346行；K40并核对§10 Arena及附表。

K40的全程无换人入口与本稿正文的换入拒绝消息并不相容；Arena继承普通命令和队伍画面，只在换入校验拒绝。

**应有合同：**在允许普通命令和可见Switch In的前提下，仍能打开Pokémon和队伍菜单，提交后显示Arena拒绝。倒下／裁判后的替补自动按队伍顺序完成，无玩家替补选择，二者分列。

**修订验收对照：**

- 正常Arena、非自动控制、canSwitch为真、健康后备：Pokémon→后备→Switch In可到达，随后被拒并留队伍循环。
- 裁判／倒下后按序替补没有玩家选人画面，但不能据此删除主动入口。

证据：`Data/Scripts/011_Battle/008_Other battle types/004_BattleArenaBattle.rb:41–71,111–125,127–200`；`Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb:140–147`；`Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb:141–185`。

### R14（P2）：成长中的可见消息与两份招式状态提交时点要分层

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第177、184、189、329、330行；§7.1–7.2、K23／K24及成长附表。

暗影经验笼统称静默，以及学招写入全部在消息前的观察点，会掩盖已可见的经验获得消息和空槽分支的战斗招式表延后同步。

**应有合同：**经验增量为正且showMessages开启时，经验获得消息位于暗影分支之前；暗影不走经验条／升级／学招循环，不等于完全无消息。空槽学招先写持久招式，再显示learned消息，消息返回后才追加在场战斗招式并检查形态；满槽替换则两份招式均在Ta-da消息前写好。

**修订验收对照：**

- 暗影heartStage≤3、正经验、showMessages=true且流程正常：有经验获得消息，之后才暂存经验；仍无经验条／升级／学招。
- 在场非暗影有空槽：learned消息正在显示时持久招式已增加，战斗招式表尚未追加；消息返回后同步。满槽替换作前置双写对照。

证据：`Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb:160–195,229–270`。

既有合同／材料：`specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md:79`。上游保持原有批准状态，本轮修订WP67-A及其新交付材料。

### C01（P3）：区分图形与文本招式菜单的零总PP显示

定位：`specs/ui/wp67-a-battle-interaction-and-presentation.md` 第101行；§4.1及一个配置对照。

将总PP为0时显示PP: ---当作默认图形菜单行为。

**应有合同：**默认图形菜单保留类型图标，但总PP不大于0时不绘制PP文本；PP: ---属于关闭图形模式的文本分支。

**修订验收对照：**

- 到达招式信息渲染的总PP0有效测试数据：分别记录默认图形模式无PP文本与文本模式占位符；这是显示分支对照，不要求改PBS或运行UI。

证据：`Data/Scripts/011_Battle/004_Scene/005_Battle_Scene_Menus.rb:210,384–413`。

### C02（P3）：入口表行数须按实际内容统计

定位：`review/wp67a-delivery-2026-10-01/delivery-summary.md` 第9行；新修订摘要／自检中的覆盖计数。

首版摘要称八组40行，实际附表有54个数据行。登记身份通过不等于此内容计数正确。

**应有合同：**修订版重新统计八组数据行（首版为8、7、8、7、5、6、7、6，共54），排除表头和分隔行；更新新摘要、自检及当前登记叙述，旧首版材料保留原样，不回写历史。

**修订验收对照：**

- 机械统计各组数据行并断言总数等于各组相加；修订若增删行则记录实测新值，不固定要求54。

既有合同／材料：`review/wp67a-delivery-2026-10-01/entry-coverage-table.md`。上游保持原有批准状态，本轮修订WP67-A及其新交付材料。

## 4. 修订边界和下一步

交给原提取方执行[WP67-A v2修订提示](next-task-prompt.md)。需同步活动主稿中的正文、汇总、场景和新版本入口附表；不能只新增正确段落却保留相反的旧句。首版交付和旧审查材料作为历史原件保留，新回应应明确承认本次已证差异。

本轮不是全项目覆盖审查；没有新增WP，也不开展WP67-B、集中回填、B批整合或整体double review。深层公式／领域规则继续引用各自主规格；R07、R10、R12、R14等只修正本稿对既有合同的错误转述。真实资源、demo可达性和宿主运行缺口继续保留，不能用本次静态通过替代运行验证。

修订后仍停在ReviewPending，送16项定点复审。只有复审关闭后再决定WP67-B。未修改reference、未执行参考实现／UI／存档写入，未创建任务或Agent、未发跨会话消息、未提交或推送。

[结构化问题](findings.json) · [来源与身份核验](source-checks.json) · [最终保护检查](final-checks.json)

