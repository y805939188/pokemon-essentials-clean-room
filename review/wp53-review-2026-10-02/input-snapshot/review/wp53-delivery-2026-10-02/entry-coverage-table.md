# WP53 数据／状态／覆盖附表 v1（入口／通知 → 前置状态／门 → 随机或用户输入 → 状态变化 → 显示／返回 → 清理及未达点 → 来源 → 主责规格）

2026-10-02；WP53 首版附件（Safari 与捕虫大会）。每行一个已核对入口；「主责规格」指该行为规则的主责规格（本包=WP53 主稿章节，其余为引用）。来源定位见主稿 §11.1/§12。本表是取证覆盖记录，不是功能数量或完成证明。分组数据行数按机械实测登记（见 checks.json）。

## 1. Safari 会话与区域

| 入口 | 前置状态／门 | 随机／用户输入 | 状态变化 | 显示／返回 | 清理及未达点 | 主责规格 |
| --- | --- | --- | --- | --- | --- | --- |
| 会话惰性创建（pbSafariState） | 全局元数据无会话对象 | — | 新建初始态（起点 nil、球数/捕获/步数/决定 0、未进行） | 返回会话对象 | — | WP53 §3.1；WP09 |
| 开始（pbStart，实参为球数） | 接待事件调用（demo/U01） | 球数实参 | @start=当前图/坐标/朝向、ballcount=实参、inProgress 置真、steps=配置步数；**captures/decision 不重置** | — | 重复开始不自动彻底重置（M02） | WP53 §3.1 |
| 清空（pbEnd） | 正常流程仅由离开区域触发 | — | 起点清空、球数/捕获/步数/决定归零、inProgress 置否、请求刷新 | — | 无正常脚本调用者（U01） | WP53 §3.1/§3.2 |
| 回起点（pbGoToStart） | 当前场景为地图场景 | — | 淡出转移（起点、朝向向下、下车） | — | 非地图场景跳过转移；@start 为 nil 处失败（人工前置） | WP53 §3.4 |
| 换图钩子（on_enter_map:end_safari_game） | 会话进行中 | — | 新图不在区域内（非接待图且无 SafariMap 旗标）→ pbEnd | — | 区域内不动；回起点不自动清会话 | WP53 §3.2 |
| 计步钩子（on_player_step_taken_can_transfer:safari_game_counter） | handled 未占用、配置步数非 0、区域内、决定为 0 | 每一步 | steps −1；减到 0 → 决定置 1＋回起点＋handled 置真 | 到 0 时两条消息（铃声＋结束） | 到 0 的当步不再遭遇；配置 0 不执行；配置负值第一步即结束（M06） | WP53 §3.3 |

## 2. Safari 战斗

| 入口 | 前置状态／门 | 随机／用户输入 | 状态变化 | 显示／返回 | 清理及未达点 | 主责规格 |
| --- | --- | --- | --- | --- | --- | --- |
| 覆盖钩子（on_calling_wild_battle:safari_battle） | handled 空、pbInSafari? | — | handled 记为 Safari 战斗返回（核心编号整数） | 已被处理/区域外 → 不动 | 注册序漫游→Safari→捕虫（M13） | WP53 §4.1；WP37 |
| 直接入口（pbSafariBattle） | 实参=个体或物种标识＋等级 | 物种标识经 pbGenerateWildPokemon 生成（触发 on_wild_pokemon_created） | 构造 SafariBattle、战斗球数←会话球数、prepare_battle | — | 不触发 :on_start_battle、不查跳战、不走 after_battle/set_outcome；battle_rules 不经核心清理 | WP53 §4.1/§4.2 |
| Ball | 容量检查（pbBoxesFull?）——满则作废重选 | — | 球数 −1、刷新数据盒；按 R=⌊F_c×1275/100⌋ 投球（SAFARIBALL ×1.5、WP38 计算） | 投球消息/动画；摇动结果消息 | 捕获 → 记录与存储 → 核心编号置 4；未捕获 → 回合末 | WP53 §4.4/§4.5；WP38 |
| Bait | — | — | 90% 概率 F_c 减半；F_e 必减半；动作后重新钳制 | "threw some bait"＋动画 | 回合末 | WP53 §4.3/§4.4 |
| Rock | — | — | F_c 必翻倍；90% 概率 F_e 翻倍；动作后重新钳制 | "threw a rock"＋动画 | 回合末 | WP53 §4.3/§4.4 |
| Run | — | — | 核心编号置 3 | 逃离音效＋"got away safely" | 会话继续（不置会话决定） | WP53 §4.4 |
| 无效/取消 | — | — | 重新选择 | — | 不耗球/回合/抽样 | WP53 §4.4 |
| 回合末判定 | 核心编号仍为 0 | 逃跑判定 0..99 < 5×F_e | 球数 ≤0 → 核心编号 2；逃跑通过 → 核心编号 3；否则观察消息 | "no Safari Balls left"/"{野生} fled!"/吃/怒/注视 | 天气动画（有天气时） | WP53 §4.4 |
| 显式中止（pbAbort） | 战斗内 | — | 核心编号置 0、结束场景 | — | 会话继续；球数回写原值（M10） | WP53 §4.4/§4.7 |
| 结果写回（pbSafariBattle 尾部） | 战斗返回核心编号 | — | 球数回写会话；球数 ≤0 → 决定置 1＋回起点；核心 4 → 统计三项；变量 1=核心编号；触发 on_wild_battle_end | 球尽消息（核心非 2 时） | wild-end 在回起点之后触发；**外层返回=核心编号整数（非布尔）** | WP53 §4.6/§4.7 |

## 3. 捕虫会话与队伍

| 入口 | 前置状态／门 | 随机／用户输入 | 状态变化 | 显示／返回 | 清理及未达点 | 主责规格 |
| --- | --- | --- | --- | --- | --- | --- |
| 配置入口组（pbSetPokemon/pbSetContestMap/pbSetReception/pbSetJudgingPoint/pbIsContestant?） | 接待事件调用（demo/U01） | 下标/图 ID/旗标字符串/判奖点 | 只写对应字段（图集/接待集为累加式） | — | 不校验参赛下标（M16 前置） | WP53 §5.1 |
| 开始（pbStart，实参为球数） | 已配置 | 对手去重抽取 min(5,8) 名 | 球数=实参、inProgress 置真、计时器写单调时钟、队伍缩为[选中员]、其余存 otherparty、统计 +1 | — | 成员对象原样（不治疗/不重置）；未选择/越界下标处失败（先写状态再失败） | WP53 §5.1；M03 |
| 结束（pbEnd，实参=是否中断） | 会话进行中 | — | 拼队（原序不保留）→ 中断：不存储、ended 置否／非中断：昵称+存储、ended 置真 → 榜首 wins+1 → 清字段 → lastContest=墙钟 → 刷新 | 存储/箱满消息 | **places 为空在名次查询处失败**（拼队已完成、字段未清）；重复结束无效果 | WP53 §5.2；M15/M16 |
| 判奖开始（pbStartJudging） | — | — | 决定置 1 → pbJudge → 地图场景时转移判奖点（同图也刷新） | — | 判奖点 nil 在转移处失败（先写状态再失败） | WP53 §5.4 |
| 黑屏/战败回退（pbBugContestStartOver） | pbStartOver 且捕虫中 | — | 队伍治疗+去 Mega/原始 → pbStartJudging | — | 不走宝可梦中心流程 | WP53 §5.4/§6.1 |
| 越界钩子（on_leave_map:end_bug_contest） | 进行中、目标图越界 | — | pbEnd（中断实参） | — | 未判奖中断在名次查询处失败（M16） | WP53 §5.5 |
| 清理钩子（on_enter_map:end_bug_contest） | 已结束 | — | 无判奖点或当前图非判奖图 → clear 全清 | — | 停留判奖图保留（places 可查） | WP53 §5.5 |
| 倒计时钩子（on_frame_update:bug_contest_counter） | expired? 三门（未决定、限时 >0、单调时钟差 ≥ 限时）；移动路线/解释器/消息窗三门全过 | 单调时钟 | — | "BEEEEEP!"＋"Time's up!" → pbStartJudging | 菜单/战斗期间落地推迟（M17） | WP53 §5.3 |
| 定时器显示（on_map_or_spriteset_change） | 进行中、未决定、限时非 0 | 单调时钟 | 挂接 TimerDisplay（分:秒、下界 0） | 倒计时显示 | 限时 0 不显示；限时 <0 显示 00:00 永不到期（M18） | WP53 §5.3 |

## 4. 捕虫战斗

| 入口 | 前置状态／门 | 随机／用户输入 | 状态变化 | 显示／返回 | 清理及未达点 | 主责规格 |
| --- | --- | --- | --- | --- | --- | --- |
| 覆盖钩子（on_calling_wild_battle:bug_contest_battle） | handled 空、pbInBugContest? | — | handled 记为捕虫战斗返回（布尔） | 已被处理/未进行 → 不动 | 注册序在漫游/Safari 之后 | WP53 §6.1 |
| 直接入口（pbBugContestBattle） | 实参=个体或物种标识＋等级 | 先触发 :on_start_battle；物种标识生成 | 构造 BugContestBattle（internalBattle 真）、起始下标 0、预算←会话、单打规则、prepare_battle | — | 不查跳战；战斗后 after_battle；败/平 → 恢复音乐＋StartOver 判奖 | WP53 §6.1；WP42 |
| Ball（pbItemMenu 覆写） | — | — | 恒登记 Sport Ball 一枚；**消耗只扣会话预算（>0 才 −1）、不动背包** | 菜单标题 "Sport Balls: n" | 投球失败不返还预算；球类占用全部行动（WP40） | WP53 §6.2 |
| 投球捕获（WP38 引用） | — | 摇动判定 | SPORTBALL ×1.5、x/y 计算；DEBUG+CTRL 必捕 | 摇动结果消息 | 捕获走 Mixin 记录（图鉴照常）→ 存储落 §6.3 覆写 | WP53 §6.2；WP38 |
| Fight/Pokémon/Run | 普通战斗合同（WP40/WP41 引用） | — | 同普通 Battle | — | 菜单与一般背包分开 | WP53 §6.2 |
| 保留（pbStorePokemon 覆写） | — | 确认/拒绝 | 无保留 → 登记；有保留 → 比较窗 → 确认替换／拒绝不保留 | "already caught"/比较窗/"Switch Pokémon?"/"Caught!" | **不进队伍/箱子**；拒绝不回滚图鉴/统计；旧保留被换下（M21） | WP53 §6.3 |
| 回合末（pbEndOfRoundPhase 覆写） | 正常回合末之后 | — | 预算 ≤0 且未决 → 核心编号置 3 | — | 战斗阶段球尽（M19） | WP53 §6.4 |
| 结果写回（pbBugContestBattle 尾部） | 战斗返回核心编号 | — | 预算回写；**预算恰为 0 → 消息＋pbStartJudging**；通用结果写入变量 1＋统计；触发 on_wild_battle_end | "Contest is over!" | 败/平已 StartOver 判奖后预算恰 0 → **重复判奖**（M20）；**外层返回布尔（败/平为否）** | WP53 §6.5 |

## 5. 判分与结算

| 入口 | 前置状态／门 | 随机／用户输入 | 状态变化 | 显示／返回 | 清理及未达点 | 主责规格 |
| --- | --- | --- | --- | --- | --- | --- |
| 评分（pbBugContestScore） | — | — | S=4L＋⌊100×Σ(iv/31)⌋＋⌊100×HP/HP_max⌋＋R；R∈{60,80,100}（c_r≤120／≤60 两道阈值） | — | 按当前实现，不以原作公式替代（M23） | WP53 §7.1 |
| 判奖（pbJudge） | decision 置 1 后调用 | 选图/抽遭遇/HP 1..上限−1 | 遭遇图集构建（无 BugContest 类型回退 Land）→ 每对手 Pokemon.new 直构＋随机 HP＋评分 → 降序排序 → places **追加**前三名 | — | 空图集/空候选/判奖数组 <3 → 异常（M25）；对手无生成钩子修饰（M24） | WP53 §7.2/§7.3 |
| 名次（place） | places 非空 | — | 返回玩家在前三条中的位置（否则 3） | — | places 为空在读取处失败（M16/M26） | WP53 §7.3 |
| 名次查询（pbGetPlaceInfo，实参=名次位） | places 非空且下标合法 | — | 变量 1=玩家/对手名、2=物种名、3=分数 | — | 空/越界在读取处失败（事件前置） | WP53 §7.3 |
| 结算次序（pbEnd 非中断） | 判奖后 | — | 拼队 → 保留个体昵称+存储 → 榜首 wins+1 → 清字段 → lastContest | 存储/箱满消息 | 箱满不存储；不一概承诺事务回滚；奖励事件未知（U01/WP77） | WP53 §5.2/§7.3 |

## 6. 公共交界、UI 与保存

| 入口 | 前置状态／门 | 随机／用户输入 | 状态变化 | 显示／返回 | 清理及未达点 | 主责规格 |
| --- | --- | --- | --- | --- | --- | --- |
| 覆盖竞争次序（on_calling_wild_battle） | handled 空门 | — | 漫游（012）→ Safari（018/001）→ 捕虫（018/002） | — | Safari 区域内漫游门全过 → 漫游战斗优先（M13/M29） | WP53 §8.1/§8.2；WP37 |
| 物种/生成钩子（on_wild_species_chosen／on_wild_pokemon_created） | 各自门（WP37/WP36 引用） | — | 漫游替换→雷达连锁；闪光开关→**Safari/捕虫 IV 重摇（无满 IV 才重摇全部主属性、至多 4 次、命中即停、重摇才重算）**→传说保底→等级缩放 | — | 两钩子均无模式门；判奖对手不走生成链 | WP53 §8.1；WP36 |
| 换图/步进/帧钩子次序 | — | — | on_enter_map：漫游推进→雷达取消→Safari 清空→捕虫清理；on_leave_map：捕虫越界；计步：毒伤→Safari 计步；帧：Pokérus 等→捕虫倒计时 | — | wild-end 由两模式入口在结果写回后显式触发（在回起点/判奖之后） | WP53 §8.1 |
| 暂停菜单信息（pbShowInfo 追加） | 模式进行中 | — | Safari：步数 x/y＋球数（步数 ≤0 只球数）；捕虫：Caught/Level/Balls 或 None | 信息行 | — | WP53 §8.3 |
| 主动 Quit（Safari）／Quit Contest（捕虫） | 模式进行中、确认 | 确认对话框 | Safari：决定置 1＋回起点；捕虫：pbStartJudging（进入判奖≠中断） | 确认消息 | 取消返回菜单（M27） | WP53 §8.3 |
| 背包（pause_menu:bag） | !pbInBugContest? | — | 捕虫中不显示 | — | Safari 中可用（战斗内无背包） | WP53 §8.3；WP65 |
| 保存（pause_menu:save） | !save_disabled、!pbInSafari?、!pbInBugContest? | — | 两种模式中不显示 | — | 持久化仅未开始/已结束态可达 | WP53 §8.3/§8.4；WP09 |
| 调试编辑（debug_menu:safari_zone_and_bug_contest） | 模式进行中、DEBUG | 数值输入 0–99999 | Safari 步数（配置 >0 才可编）/球数；捕虫剩余分钟（限时 >0 才可编、同步 TimerDisplay）/Sport 球数 | 调试菜单 | 调试不混进默认用户流程（M28） | WP53 §8.3 |
| 持久与统计（全局元数据/$stats） | — | — | safariState/bugContestState 随存档；统计四字段；无相关保存转换 | — | 运行时刻值（timer_start 等）与落盘分开、语义未证 | WP53 §8.4；WP06/WP09 |
| demo 配置样本（PBS） | — | — | SAFARI_STEPS=600、BUG_CONTEST_TIME=1200；[068] SafariMap 旗标；[028] BugContest 旗标＋BugContest,21 遭遇表；[029]/[030] BugContestReception 旗标；SAFARIBALL/SPORTBALL 条目 | — | 只作配置证据，不作完整接待/奖励事件证据（U01/WP77） | WP53 §8.5 |
