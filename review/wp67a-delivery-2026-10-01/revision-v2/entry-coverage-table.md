# WP67-A 菜单／反馈入口覆盖附表 v2（入口 → 实际调用者 → 模式／权限 → 输出／状态变化 → 所属规格）

2026-10-01；WP67-A 首审修订 v2 附件（revision-v2）。每行一个已核对入口；「所属规格」指该行为规则的主责规格（本包=WP67-A 主稿章节，其余为引用）。来源定位见主稿 §14。本表是取证覆盖记录，不是功能数量或完成证明。v2 自 v1 的 54 行出发修订受影响行（R01～R14、C01 涉及处），分组数据行数按本版实测登记（见 checks.json）。

## 1. 主命令与阶段

| 入口 | 实际调用者 | 模式／权限 | 输出／状态变化 | 所属规格 |
| --- | --- | --- | --- | --- |
| 主命令菜单 `pbCommandMenu` | Battle#pbCommandPhaseLoop 玩家循环 | 首行动=Run／后续=Cancel／暗影训练家战=Call | 返回 −1/0/1/2/3/4（−2=调试）；确认写回 lastCmd | WP67-A §3.3 |
| 菜单构建 `pbCommandMenuEx` | 普通战（模式 0–2）、Safari（3）、捕虫（4） | BACK 仅模式 1 有效 | 2×2 导航；模式决定按钮图形；初始下标=lastCmd | WP67-A §3.3、§10 |
| 回退（命令 −1） | 命令阶段循环 | 本轮已有完成位置才允许 | 撤销上一位置选择（物品退回、Mega 撤销） | WP67-A §3.4 |
| 逃跑 `pbRun` | 主菜单 Run（仅首行动） | 训练家战内部禁、规则 canRun、束缚、保证逃脱链；计逃跑计数 | 成功 decision=3；失败行动耗尽；未构成尝试回主菜单 | WP67-A §3.4；WP41 |
| 回合末逃跑 `pbRun(duringBattle=true)` | 野生昏厥拒绝"Use next Pokémon?"后 | 保留 canRun 门；**跳过幽灵/必逃特性道具/束缚整组、不计数** | 成功 decision=3；失败必须选替补 | WP67-A §6.3；WP41 |
| 调试菜单（F9） | 命令菜单 $DEBUG | — | 调试菜单后全量刷新＋形态检查 | WP67-A §3.4；WP13 |
| 呼唤 `pbRegisterCall`/`pbCall` | 主菜单 Call → 攻击阶段呼唤子阶段 | 暗影训练家战 | 暗影：Hyper 解除／非 Hyper 无效果；**仅非暗影**：治睡眠／升命中／无效果 | WP67-A §4.2；WP23 |
| 阶段次序 | pbAttackPhase | 固定：优先级消息→呼唤→换人→物品→Mega→招式 | 各领域子阶段按优先序消费 choices | WP67-A §3.5；WP40 |
| 中止（abortable） | 场景输入循环 | 非交互战斗 | BACK→中止异常→decision=0＋pbEndBattle；与普通取消分开 | WP67-A §3.5、§9.1 |

## 2. 招式与目标

| 入口 | 实际调用者 | 模式／权限 | 输出／状态变化 | 所属规格 |
| --- | --- | --- | --- | --- |
| 招式菜单 `pbFightMenu` | 命令菜单 Fight（pbCanShowFightMenu? 门） | Encore/无招→自动登记不开菜单 | yield −1/−2/−3/下标；写回 lastMove | WP67-A §4.1 |
| 招式校验 `pbRegisterMove` | 战斗对象（yield 链） | PP=0／Encore／领域封锁 | 写入 choices（:UseMove）或拒绝留菜单 | WP67-A §4.1；WP40 |
| 自动招式 `pbAutoChooseMove` | Encore／无招可用 | 昏厥→清空 | 登记被束缚招或挣扎；多人时提示＋选目标 | WP67-A §4.1；WP40 |
| Mega 切换 | 招式菜单 ACTION | pbCanMegaEvolve? 全门（开关/持石/环/槽位/SkyDrop；$DEBUG+CTRL 直通） | 登记/撤销 Mega；攻击阶段执行进化 | WP67-A §4.1；WP40 |
| Shift | 招式菜单 SPECIAL | pbCanShift?（三重、非中位、同训练家） | 撤 Mega＋登记 :Shift | WP67-A §4.1；WP41 |
| 目标选择 `pbChooseTarget` | 招式登记成功后（**非双方各 1 席即进入，含 0 目标类别**）／背包球类 | 目标类别数据驱动；**单选模式仅 num_targets==1，其余整体高亮不可移动** | 可选集合 nil（无对象/类别筛除）/空串（现存昏厥）/名字（未昏厥）；初始目标按类别；USE 登记、BACK 回招式菜单/背包 | WP67-A §4.3；WP40/WP43 |
| 对位次序 `pbGetOpposingIndicesInOrder` | 目标初始化与跨侧导航 | 按已证席位组合（1v2–3v3） | 硬编码次序表 | WP67-A §4.3；WP39 |

## 3. 物品

| 入口 | 实际调用者 | 模式／权限 | 输出／状态变化 | 所属规格 |
| --- | --- | --- | --- | --- |
| 战斗背包 `pbItemMenu` | 命令菜单 Bag；internalBattle 门 | 过滤 battle_use>0；战斗内独立游标 | **未选物品退出列表→主命令**；提交→校验链 | WP67-A §5.1；WP66-C |
| 物品命令（Use/Cancel） | 背包内命令列表 | battle_use 非 0 才有 Use | **Cancel/BACK→回物品列表**（不退菜单） | WP67-A §5.1 |
| 成员目标（类型 1/2/3） | 背包→队伍画面 | 蛋跳过；类型 2 再选招式 | 取消→背包重显；**提交被拒→留成员选择** | WP67-A §5.2；WP66-A |
| 自动目标（类型 1/3/4） | 单成员队伍／单玩家场上／单对方未昏厥 | 跳过选择直接提交 | **被拒后：类型 1/3→进成员画面；类型 4→回物品列表** | WP67-A §5.2 |
| 对方目标（类型 4 手动） | 背包→战斗目标窗口 | 多对方时手选 | 取消/被拒→背包淡入重显回物品列表；确认→校验 | WP67-A §5.2 |
| 使用门 `pbCanUseItemOnPokemon?`/`triggerCanUseInBattle` | 战斗对象 | 蛋/Embargo/Hyper；球类：**队伍且仓库同时满**/禁球/非首行动/半无敌/多对方 | 拒→按提交入口分层返回（消息） | WP67-A §5.3；WP28/WP23 |
| 登记扣减 `pbRegisterItem` | 校验全部通过后 | 仅用后即耗物品 | 写 choices（:UseItem）＋立即从背包删除 | WP67-A §5.3；WP27 |
| 执行 | 攻击阶段物品子阶段 | 按优先序 | 成功→选择物品位清空；无效→消息＋退回背包 | WP67-A §5.3；WP28 |
| 撤回 | 命令回退／执行无效／战斗结束清理 | — | 物品退回背包 | WP67-A §5.3 |

## 4. 队伍与换人

| 入口 | 实际调用者 | 模式／权限 | 输出／状态变化 | 所属规格 |
| --- | --- | --- | --- | --- |
| 队伍画面 `pbPartyScreen`（场景） | 主菜单换人（模式 0）／捕获换入（模式 1）／查看（模式 2） | canCancel 由调用者传入 | **成员命令 Cancel/BACK→只回成员列表；列表层取消才服从 canCancel**（假→重显、真→结束）；−1 为战斗包装未取得选择的结果值 | WP67-A §6.1；WP66-A |
| 换入命令可见门 | 场景成员命令构建 | 模式 0＋成员 able＋（canSwitch 或不可取消） | **蛋/昏厥成员无 Switch In**（其拒绝消息不沿此 UI 触达）；Summary/Cancel 总有 | WP67-A §6.1–6.2 |
| 换人校验 `pbCanSwitch?`/`pbRegisterSwitch` | 战斗对象 | 蛋/他人/昏厥/在场/同回合同人/束缚 | 拒→画面内消息（可达者：在场/已选/非所有/束缚类）；过→登记 :SwitchOut | WP67-A §6.2；WP41 |
| 主动换人 `pbPartyMenu` | 主菜单 Pokémon | 可取消；@debug→AI | 登记或返回 | WP67-A §6.3 |
| 流程中替补 `pbSwitchInBetween` | U-turn/Baton Pass/回合末 | 玩家→画面（权限随调用点）；否则 AI | checkLaxOnly 只查换入 | WP67-A §6.3；WP41 |
| 回合末替补 `pbEORSwitch` | 回合末阶段 | 提议门：内部＋Switch＋训练家战＋玩家侧恰 1 席＋首席存活未换＋有后备＋Outrage=0（**不查一般束缚**）；同意进选人仍可被换出束缚拒；玩家昏厥（训练家）必须选；（野生）先确认"Use next Pokémon?" | 收回/派出消息＋替换＋入场链 | WP67-A §6.3；WP41/WP42 |
| 收回/派出消息 | pbRecallAndReplace | 按 HP/回合数/对方 HP 分级 | brief 消息＋动画（§9.3） | WP67-A §6.3、§9.3 |

## 5. 成长与学招

| 入口 | 实际调用者 | 模式／权限 | 输出／状态变化 | 所属规格 |
| --- | --- | --- | --- | --- |
| 经验结算 `pbGainExp` | 回合末／捕获（配置） | internalBattle＋expGain | 参与者/学习装置/ExpAll 分配 | WP42（主）；WP67-A §7.1 |
| 经验获得消息 | pbGainExpOne | 增量为正＋showMessages | **先于暗影分支显示（暗影也有）**；暗影随后仅暂存、无经验条/升级/学招 | WP67-A §7.1；WP23 |
| 经验条 `pbEXPBar` | pbGainExpOne 逐级 | 仅玩家侧单打框显示 | 阻塞动画；无框立即结束 | WP67-A §7.1、§9.2 |
| 升级显示 | pbGainExpOne | 暗影 heartStage≤3 不进入 | LevelUp 动画→数值重算/刷新→暂停消息＋音→两个右上数值窗（仅 USE） | WP67-A §7.1；WP30/WP42 |
| 学招 `pbLearnMove` | 升级后按等级逐个 | 已会跳过 | 空槽：**持久先写→learned 消息→消息返回后追加战斗招式表**；满槽→确认→遗忘画面分支 | WP67-A §7.2；WP30 |
| 遗忘画面 `pbForgetMove` | 满槽且同意遗忘 | HM 不可忘（$DEBUG 豁免） | 选中→**两份招式先于 Ta-da 写好**→替换序列；取消→放弃确认→重选循环 | WP67-A §7.2；WP66-A |

## 6. 捕获与接收

| 入口 | 实际调用者 | 模式／权限 | 输出／状态变化 | 所属规格 |
| --- | --- | --- | --- | --- |
| 投球 `pbThrowPokeBall` | 攻击阶段物品执行（球类）／Safari | 目标解析；训练家挡球（非 Snag 暗影）；**无存活队友直接触达→状态查询先失败（无两条消息）** | 摇动数（WP38）→投掷动画→0–3 逃脱消息／4 捕获序列 | WP67-A §8.1；WP38 |
| 捕获成功 | 摇动数=4 | 野生才有成功旋律 | 移除→经验（配置）→复位→结局判定→onCatch→收球隐藏→入待接收列表 | WP67-A §8.1；WP38/WP42 |
| 图鉴登记 | pbRecordAndStoreCaughtPokemon（战后） | 拥有记录照写；**消息/条目需持图鉴＋已解锁** | "added to the Pokédex."暂停＋图鉴条目画面（条件不满足则不显示） | WP67-A §8.2；WP62/WP66-B |
| 命名 | 非暗影＋选项 Give | **确认框初始 Yes**；选 Yes→命名画面 | 写入个体名 | WP67-A §8.2；WP17/WP65 |
| 满队选择 `pbStorePokemon` | 满队且（询问／必须入队） | sendToBoxes 0/2；**初始选中 Add to your party**；BACK 返回 99（2 时继续循环、否则=送盒） | 四命令循环；换入→选人送盒（可取消视配置）→重排记忆 | WP67-A §8.3；WP38/WP25 |
| 常规存放 | 队伍未满或不询问 | — | 入队/入盒暂停消息；**多个体按图鉴→命名→存放逐个完成** | WP67-A §8.3；WP38 |

## 7. 消息与动画

| 入口 | 实际调用者 | 模式／权限 | 输出／状态变化 | 所属规格 |
| --- | --- | --- | --- | --- |
| 普通/brief/暂停消息 | 全战斗流程 | — | 1 秒自关／驻留／3 秒自关（战末例外需输入） | WP67-A §9.1；WP17 |
| abortable 消息行为 | 非交互战斗/回放 | — | 文字自动快进；**1 秒/3 秒计时与 brief 驻留保留**；命令列表不自动选项 | WP67-A §9.1 |
| 确认/命令列表 | pbDisplayConfirmMessage/pbShowCommands | **初始下标 0（Yes/No 初始 Yes）**；BACK=默认（≥0 才可） | 返回下标/默认值；BACK 返回值≠初始游标 | WP67-A §9.1；WP17 |
| HP/经验条 | pbHPChanged/pbHitAndHPLossAnimation/pbEXPBar | 动画开关不门 | 1.0 秒固定／1.75 秒比例；阻塞 | WP67-A §9.2 |
| 派出/收回/倒下/投球 | pbSendOutBattlers/pbRecall/pbFaintBattler/pbThrow 等 | 动画开关不门（闪光公共动画受门） | 阻塞序列；**多个体派出并行推进、各数据框只等自身球动画** | WP67-A §9.3 |
| 特性提示条 | pbShowAbilitySplash | 世代 ≥5 | 出现/消隐动画；可选 1 秒延迟 | WP67-A §9.2 |
| 招式/公共动画 | pbAnimation/pbCommonAnimation | **动画开关门**；数据缺失静默 | 查找链（精确→类型默认→Tackle→nil）；pbAnimationCore 阻塞；球爆开非阻塞 | WP67-A §9.4；WP15/WP74 前向 |
| 胜利 BGM | pbWildBattleSuccess/pbTrainerBattleSuccess | — | 置 @battleEnd（暂停消息不再自关）＋BGM | WP67-A §3.5、§9.1 |

## 8. 特殊模式与对照

| 入口 | 实际调用者 | 模式／权限 | 输出／状态变化 | 所属规格 |
| --- | --- | --- | --- | --- |
| Safari 命令/投球/饵石 | SafariBattle 主循环（独立类） | 模式 3 菜单 | 球数扣减、因子变化、逃逸/球尽结局 | WP67-A §10；WP53 前向 |
| 捕虫菜单/存放 | BugContestBattle 覆写 | 模式 4 菜单；球直登 | 暂存替换确认；球尽 decision=3 | WP67-A §10；WP53 前向 |
| Palace 自动招式 | pbAutoFightMenu 覆写 | 性格概率表；先经 Encore/无常规可选招门 | Fight 不开菜单自动登记；**无合格槽→"无力"消息失败（非实际挣扎）**；危机门=回合末未终局＋存活＋非睡眠＋未危机＋HP≤1/2 | WP67-A §10；WP56 |
| Arena 判决 | pbEndOfRoundPhase 覆写 | 每 3 回合 | 评分窗＋判决消息＋负方倒下＋自动替补 | WP67-A §10；WP56 |
| Arena 换人入口 | 普通命令链继承 | canSwitch 为真时可开 | 队伍画面/Switch In 可达、提交被拒留循环；与自动替补分列 | WP67-A §10；WP56 |
| 回放 | RecordedBattlePlaybackModule | 录制数据 | **通常无常规菜单；自动招式（非单打＋Encore＋玩家所有）仍调目标窗口**；暂停消息转普通（非零等待） | WP67-A §10；WP58 |
| 调试替身 | DebugSceneNoVisuals | 挑战生成 | 固定/随机返回（非玩家行为） | WP67-A §3.6、§10 |
