# WP67-A 首审修订 v2 回应（R01–R14 P2＋C01–C02 P3，共 16 项）

2026-10-01；规格提取方。依据有界审查 [report.md](../../wp67a-review-2026-10-01/report.md) 与 [next-task-prompt.md](../../wp67a-review-2026-10-01/next-task-prompt.md)：**首版主稿 14 项 P2＋2 项 P3 共 16 项待修**。本目录只处理这 16 项；首版交付材料留史于 `../` 根目录，不改写其旧计数与旧声明——本回应逐项说明哪些首版结论被更正。写入前已复测主稿与审查 input-snapshot 一致（v1 被审身份 `b6fdd96a`／71,691）；按各 ID 回源核对后修订。reference 固定 commit、Git 清洁。

修订对象与当前身份（磁盘程序化实测）：

| 文件 | v1 被审（审查快照冻结） | v2 当前 |
| --- | --- | --- |
| `specs/ui/wp67-a-battle-interaction-and-presentation.md` | `b6fdd96ae201d67637f71795193ea00c80cb7a7233e71c5bf597215eeb9935b3`／71,691 | `f5ac2a269cff135f9539af8a3d69f79c356150aad740f36a09335342497dd1b2`／85,929 |

差异相对审查 input-snapshot patch 精确重建到当前字节（11 个 hunk），见 [diff-bindings.json](diff-bindings.json) 与 [revision-diffs/](revision-diffs/)。场景 K01–K42 保留（14 行修订）、新增 K43–K56 对照，共 56 个定义行、全文唯一。作者状态：**REVISED_PENDING_REVIEW**——不自行 CLOSED、不自行 Reviewed。

## R01（P2）— 物品取消/拒绝按"列表→子菜单→成员/目标"分层（接受）

- **首版错误**：§5.1 把 Use/Cancel 子菜单取消写成退出到主命令；§5.3 把任一校验拒绝写成"留在背包菜单（画面不变）"。
- **回源**：`004_Scene/003_Scene_ChooseCommands.rb:196–324`（未选物品 `break` 才出菜单；Use/Cancel 后 `next` 回物品列表；类型 1/3 自动提交 yield 失败后落到成员画面；成员画面 yield 失败 `next` 留成员循环、取消才 `pbFadeInScene` 回背包；类型 4 手动目标取消/被拒恢复背包）；`001_Battle/009_Battle_CommandPhase.rb:100–137`。
- **修订位置**：§5.1（取消两层分开）、§5.2（自动提交被拒后续路径、成员画面提交被拒留成员选择、类型 4 回列表）、§5.3（拒绝按提交入口分列）、§5 分界句、K14 修订、新增 K43；附表物品组 5 行同步。
- **静态对照**：报告三例（Use/Cancel 取消仍在背包列表；满 HP 成员提交给无效果消息留成员选择；类型 1 自动目标满 HP 被拒后进成员画面）→ 正文 §5.2/§5.3 与 K14/K43 已定位。

## R02（P2）— 队伍成员命令取消与整屏退出分开（接受）

- **首版错误**：§6.1 把成员命令 Cancel 并入 canCancel 整屏退出；K18 把蛋/昏厥防御性消息写成普通菜单实际反馈；场景 −1 与战斗包装 −1 混写。
- **回源**：`004_Scene/003_Scene_ChooseCommands.rb:141–191`（成员命令不匹配任何分支 → 回成员循环；列表 `idxParty < 0` 才查 canCancel；Switch In 要求 able）；`016_UI/005_UI_Party.rb:589–617`（成员命令窗 BACK 返回 −1）；`001_Battle/005_Battle_ActionSwitching.rb:9–33, 113–127`。
- **修订位置**：§6.1（两层取消＋−1 归属）、§6.2（拒绝消息可达性分层——蛋/昏厥无 Switch In 故不沿该 UI 触达）、K18 修订；附表队伍组增"换入命令可见门"行。
- **静态对照**：报告三例（可战斗成员命令 Cancel 回列表、列表再取消回主命令；蛋/昏厥无 Switch In；强制替补成员命令可取消但列表不可退出）→ §6.1/§6.2 与 K18 已定位。

## R03（P2）— 非单打零目标类别窗口与空位置语义（接受）

- **首版错误**：§4.3 把目标窗口限定为"目标数据需要选择"、多选模式限定为 2+；空串解释为"无成员"。
- **回源**：`001_Battle/009_Battle_CommandPhase.rb:60–97`（非单打即调 `pbChooseTarget`，不区分目标类别）；`004_Scene/003_Scene_ChooseCommands.rb:333–438`（mode 仅按 num_targets==1 分；texts 三态生成）；`005_Battle_Scene_Menus.rb:514–545`；`017_Target.rb:26–33, 53–62`；`PBS/moves.txt:6541–6550`（SWORDSDANCE=User/0 目标）。
- **修订位置**：§4.3 显示时机（非双方各 1 席即进入、0 目标类别同进入）、可选择集合三态（无对象 nil／现存昏厥空串／未昏厥名字）、导航模式（单选仅 num_targets==1，其余整体高亮不可移动）；新增 K44；附表目标行同步。
- **静态对照**：2v2 手选 SWORDSDANCE → 目标窗口自身按钮、不移动、USE 确认、BACK 回招式菜单；昏厥现存=空名按钮、不存在=不可选 → K44 已定位。

## R04（P2）— 确认框初始选中与 BACK 返回值分列（接受）

- **首版错误**：§9.1 写"默认 No（下标 1）"；§8.3 把 99 写成"默认/取消值"——把取消返回值误当初始游标。
- **回源**：`004_Scene/001_Battle_Scene.rb:267–307`（`cw.index = 0` 初始；BACK 返回 defaultValue）；`005_Battle_CatchAndStoreMixin.rb:15–34`（满队框初始 Add to your party；99 为 BACK 标记由 sendToBoxes 分支解释）。
- **修订位置**：§9.1（确认/命令列表初始下标 0、BACK 返回值≠游标）、§8.3（初始选中 Add to your party、99 仅 BACK 标记）、§8.2 命名确认同步、K32/K33 修订、新增 K45；附表确认/满队两行同步。
- **静态对照**：全显后不移动 USE=Yes、BACK=No；sendToBoxes=0 不移动 USE 进选人、BACK 送盒；=2 时 BACK 继续循环 → K32/K33/K45 已定位。

## R05（P2）— abortable 不让所有等待立即结束（接受）

- **首版错误**：§9.1 写"abortable 为真即立即放行"；K41 把回放暂停转普通等同零等待。
- **回源**：`004_Scene/001_Battle_Scene.rb:103–108, 169–307`（abortable 仅使逐字 skipAhead；普通消息全显后仍走 1 秒计时、brief 仍驻留、暂停非战末仍 3 秒计时；`pbShowCommands` 循环无 abortable 分支）；`005_RecordedBattle.rb:194–196`（暂停降级为普通）；`004_Challenge_Battles.rb:111–127`（回放场景 abortable=true 的上下文）。
- **修订位置**：§9.1（abortable 实际行为枚举）、§10 回放行与 §12 降级行（非零等待）、K41 修订、新增 K46；附表增"abortable 消息行为"行。
- **静态对照**：回放普通消息文字快进后仍等计时；abortable 命令列表不自动选项、BACK 走中止路径 → K41/K46 已定位。

## R06（P2）— 捕获图鉴前提与多个体接收顺序（接受）

- **首版错误**：K29 输入未持图鉴却预期图鉴消息与条目；§8.3 多个体段写成"命名→图鉴→存放"。
- **回源**：`005_Battle_CatchAndStoreMixin.rb:5–13, 88–107`（拥有记录无条件写入；消息/条目需 `has_pokedex && species_in_unlocked_dex?`；逐个体循环内依次图鉴、命名、存放）。
- **修订位置**：§8.2（条件分层明示）、§8.3 多个体（图鉴→命名→存放逐个完成、不分批）、K29 修订为未持图鉴反例、新增 K47（全条件对照）与 K48（两个体顺序）；附表图鉴/常规存放两行同步。
- **静态对照**：报告三例（未持图鉴无消息/条目；全条件对照图鉴→命名→存放；两个体各自完整完成）→ K29/K47/K48 已定位。

## R07（P2）— 投球容量门与无目标直接触达边界（接受）

- **首版错误**：§5.3 把"仓库满"单独写成禁球条件；§8.1/§12 把无存活队友写成显示两条无目标消息后正常返回。
- **回源**：`013_Items/003_Item_BattleEffects.rb:28–64`（`party_full? && $PokemonStorage.full?` 同时成立才拒）；`005_Battle_CatchAndStoreMixin.rb:112–143`（昏厥改取 `allAllies[0]`）；`002_Battler/001_Battle_Battler.rb:746–749`（allAllies 仅未昏厥）；`001_Battle/001_Battle.rb:458–460`；WP38 既有合同（`specs/pokemon-rules/wp38-capture-and-receiving.md:21`，未改）。
- **修订位置**：§5.3（容量门改为队伍且仓库同时满）、§8.1（改取为空→状态查询先失败、两条消息不可达、三前提分开、不承诺退球/回滚/退出）、§12 同步、K17 修订、新增 K49；附表投球/使用门两行同步。
- **静态对照**：报告四例（仓库满队伍有空位不拒；队伍也满才拒；直接触达空对象先失败无两条消息；有存活队友改取继续）→ K17/K49 已定位。

## R08（P2）— 多个体派出并行推进（接受）

- **首版错误**：§9.3 写"串行：上一个的球动画完成才播下一个的数据框"。
- **回源**：`004_Scene/004_Scene_PlayAnimations.rb:93–156`（同一更新循环推进 fadeAnim 与全部 sendOutAnims；各数据框只在自身球动画完成后启动；退出条件为全部完成且排列动画结束）；`008_Battle_Scene_Animations.rb:385–524`；`007_Battle_Scene_BaseAnimation.rb:51–62`。
- **修订位置**：§9.3 派出段（并行推进、错峰、各数据框只等自身、整体退出条件）；新增 K50；附表派出行同步。
- **静态对照**：同侧派出两名——两球动画同循环推进、数据框各随自身球动画、不以第一只完成为第二只唯一启动条件 → K50 已定位。

## R09（P2）— Call 的睡眠/命中分支仅属非暗影（接受）

- **首版错误**：§4.2 把睡眠治愈/命中提升平铺为通用分支，遗漏外层暗影分支优先级。
- **回源**：`001_Battle/008_Battle_ActionOther.rb:31–62`（shadowPokemon? 分支内：Hyper→解除改心量，否则"But nothing happened!"；elsif 睡眠/命中只属于非暗影）。
- **修订位置**：§4.2（暗影单独分支、仅非暗影继续检查）；新增 K51；附表呼唤行同步。
- **静态对照**：非 Hyper 暗影睡眠→无效果保持睡眠；非暗影睡眠→治愈；非 Hyper 暗影命中可升→无效果 → K51 已定位。

## R10（P2）— 回放无菜单仅描述通常命令路径（接受）

- **首版错误**：§10/§12/K41 写"不出现任何菜单"的普遍保证。
- **回源**：`005_RecordedBattle.rb:198–222`（回放命令循环按记录注册）；`004_Battle_ActionAttacksPriority.rb:36–57`（Encore 自动招式在多人且玩家所有时提示并调 `pbChooseTarget`）；`009_Battle_CommandPhase.rb:92–97`；`004_Scene/003_Scene_ChooseCommands.rb:384–438`；WP58 既有合同（`specs/combat/wp58-battle-recording-and-playback.md:138`，未改）。
- **修订位置**：§10 回放行（通常无常规菜单＋条件化目标窗口例外、1v1 重建使该分支通常不可达但不推为无交互保证）、§10 尾注、§12 同步、K41 修订、新增 K56；附表回放行同步。
- **静态对照**：1v1 回放记录驱动不开常规菜单；条件化对照（非单打＋玩家所有＋有效 Encore＋记录 FIGHT 自动入口）仍调目标窗口 → K41/K56 已定位。

## R11（P2）— 替补提议实际门与回合末逃跑路径（接受）

- **首版错误**：§6.3 把提议门写成"单打且未被束缚类锁定"；把回合末逃跑指向主命令整套规则。
- **回源**：`005_Battle_ActionSwitching.rb:142–215`（提议门：`@internalBattle && @switchStyle && trainerBattle? && pbSideSize(0)==1 && opposes? && !@battlers[0].fainted? && !switched.include?(0) && pbCanChooseNonActive?(0) && Outrage==0`；同意后进选人仍走 pbSwitchInBetween 校验）；`007_Battle_ActionRunning.rb:60–158`（`duringBattle` 跳过 `if !duringBattle` 整组——幽灵/必逃/束缚——且不计 `@runCommand`；canRun 门在此前）；WP41 既有合同（`specs/combat/wp41-switching-positioning-and-escape.md:103`，未改）。
- **修订位置**：§6.3（提议门逐项、玩家侧 1 席不收窄为双方 1 席、Outrage 不扩大为束缚、同意后选人可被拒；回合末逃跑跳过整组且不计数）；K20/K21 修订、新增 K52；附表回合末替补行同步、增"回合末逃跑"行。
- **静态对照**：报告三例（被一般束缚仍提议、同意后选人可被拒；1v2 玩家侧 1 席仍提议；野生拒绝后 duringBattle 逃跑不套用幽灵必逃/拘束、失败再必选替补）→ K20/K21/K52 已定位。

## R12（P2）— Palace 无力非挣扎、危机门（接受）

- **首版错误**：§10/K39 写"无合法则挣扎 -2"、"HP≤1/2 进入危机态"。
- **回源**：`003_BattlePalaceBattle.rb:78–165`（无合格槽 `pbRegisterMove(-2)`；危机 `pbPinchChange`：非昏厥、非睡眠、未危机、HP≤1/2，回合末未终局时逐员检查）；`002_Battler/009_Battler_UseMoveSuccessChecks.rb:191–205`（choice[1]==-2 → "appears incapable of using its power!" 并失败）；`009_Battle_CommandPhase.rb:42–64`（Fight 前仍先经 pbCanShowFightMenu?/pbAutoChooseMove 门）；WP56 既有合同（`specs/combat/wp56-palace-and-arena-variants.md:66`，未改）。
- **修订位置**：§10 Palace 行（无力消息失败非实际挣扎、先经 Encore/无常规可选招门、危机门完整条件）；K39 修订、新增 K53；附表 Palace 行同步。
- **静态对照**：抽中攻击类无合格槽→无力消息、不执行挣扎攻击；半血睡眠或已有危机标记→不再播消息 → K39/K53 已定位。

## R13（P2）— Arena 禁止换人不等于没有换人入口（接受）

- **首版错误**：K40 写"全程无换人入口"，与正文换入拒绝消息不相容。
- **回源**：`004_BattleArenaBattle.rb:41–71, 111–125, 127–200`（仅覆写 `pbCanSwitchIn?` 恒拒与自动按序替补）；`009_Battle_CommandPhase.rb:140–147`（普通换人入口链不变）；`004_Scene/003_Scene_ChooseCommands.rb:141–185`（Switch In 可见门不变）。
- **修订位置**：§10 Arena 行（入口保留、提交后被拒留循环；自动替补分列）；K40 修订；附表增"Arena 换人入口"行。
- **静态对照**：正常 Arena、canSwitch 真、健康后备 → Pokémon→后备→Switch In 可达、提交被拒留队伍循环；裁判/倒下后按序替补无玩家画面 → K40 已定位。

## R14（P2）— 成长消息与两份招式状态时点分层（接受）

- **首版错误**：§7.1/K23 把暗影经验统称"静默"；§7.2 把学招写入笼统称"都在消息前"。
- **回源**：`003_Battle_ExpAndMoveLearning.rb:160–195, 229–270`（经验获得消息在暗影分支之前；空槽：`learn_move` 后播 learned 消息、随后才 `battler.moves.push`＋形态检查；满槽：个体与战斗两份招式替换均在 Ta-da 消息前）。
- **修订位置**：§7.1（经验消息先于暗影分支、暗影"静默"仅限经验条/升级/学招）、§7.2（空槽分层时点、满槽双写先于 Ta-da）、K23/K24 修订、新增 K54；附表增"经验获得消息"行、学招/遗忘两行同步。
- **静态对照**：暗影 heartStage≤3 正经验→有获得消息、无经验条/升级/学招；在场空槽→消息显示时持久已增、战斗招式表未追加、返回后同步；满槽双写对照 → K23/K24/K54 已定位。

## C01（P3）— 图形/文本菜单的零总 PP 显示（接受）

- **首版错误**：§4.1 把"PP: ---"当作默认图形菜单行为。
- **回源**：`005_Battle_Scene_Menus.rb:210, 384–413`（文本分支 total_pp≤0 显示 "PP: ---"；图形分支 total_pp>0 才绘制 PP 文本、≤0 不绘制但保留类型图标）。
- **修订位置**：§4.1（两分支分列）；新增 K55。
- **静态对照**：总 PP=0 有效数据 → 图形模式无 PP 文本（类型图标保留）、文本模式显示占位 → K55 已定位。

## C02（P3）— 入口表行数按实测统计（接受）

- **首版错误**：首版摘要写"八组 40 行"，实际 54 数据行。
- **修订位置**：v2 附表 [entry-coverage-table.md](entry-coverage-table.md) 自 v1 的 54 行出发修订受影响行（增：回合末逃跑、自动目标、换入命令可见门、经验获得消息、abortable 消息行为、Arena 换人入口；Arena 换人自队伍组移入特殊模式组）；**本版八组数据行机械实测：9／7／9／7／6／6／8／7，共 59 行**（排除表头与分隔行）。v2 摘要与 checks 使用该实测值；首版材料（含旧计数）留史不回写。

## 总体自检结果（全文口径）

- v2 diff 对审查 input-snapshot patch 精确重建（11 个 hunk，重建后字节级一致）；变更仅在 16 项批准位置及其直接交叉引用（§4.1–§4.3、§5.1–§5.3、§6.1–§6.3、§7.1–§7.2、§8.1–§8.3、§9.1、§9.3、§10、§12、§13.2 场景表、§14 来源、§16 注记）。
- **残留扫描覆盖最终活动主稿全文**（不只新增段）：16 项同根旧句逐一命名扫描全部为空（"三层都回到主命令菜单"、"任一拒绝 → 留在背包菜单"、"默认 No"、"默认/取消值为 99"、"立即放行"、"命名→图鉴→存放"、"串行：上一个"、"不出现任何菜单"、"无合法则挣扎"、"全程无换人入口"、"换人恒拒"、"暗影经验静默"、"写入发生在对应消息"等）。
- 场景编号：K01–K42 保留（14 行修订）＋K43–K56 新增，共 56 个定义行，全文唯一、交叉引用可解析。
- 未改写首版交付材料、reviewer 原件与 input-snapshot 快照；WP38／WP41／WP42／WP56／WP58 等上游批准合同仅按报告指示更正本稿转述，未改上游字节；WP65 已批准范围与 GR-001～016 保持。
- 修订后状态：WP67-A 保持 **ReviewPending（v2，R01–R14／C01–C02 已修订待定点复审）**；不自行关闭 16 项、不自行 Reviewed、不宣称通过。
