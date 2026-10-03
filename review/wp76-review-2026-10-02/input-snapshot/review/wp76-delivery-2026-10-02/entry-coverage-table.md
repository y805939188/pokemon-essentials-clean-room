# WP76 入口/能力覆盖附表（设施内容生成与模拟；首版）

2026-10-02；规格提取方。主稿 [wp76-facility-content-generation-and-simulation.md](../../specs/demo/wp76-facility-content-generation-and-simulation.md)（首版当前）。覆盖粒度＝作者可用能力/入口；每行给出行为锚点、来源（traceability）与对应静态场景。结构法实测：**六组 3／2／7／6／5／6＝29 行**（死入口/未引用文件在附录，不占数据行）。

## A 入口与触发（3 行）

| 能力/入口 | 行为锚点 | 来源 | 场景 |
| --- | --- | --- | --- |
| 设施设置联动 | `BattleChallenge.set` 登记挑战后**无条件调用** `pbWriteCup`——生成询问内嵌于设置流程，非独立菜单 | `001_Challenge_BattleChallenge.rb:18–26` | M01 |
| 外层调试门 | **非调试模式直接返回**——正式配置下生成/复用询问整体不可达 | `001_ChallengeGenerator_Data.rb:276–277` | M01-a |
| 生成/复用询问 | 无列表→两选（默认 NO）；有列表→三选（默认 NO）；新生成支再经长任务确认（**取消即返回**、启动后无中途取消）＋消息窗口＋5 秒刷帧＋完成提示 | `001_ChallengeGenerator_Data.rb:289–337` | M01-b/c、M03 |

## B 复用已有列表（2 行）

| 能力/入口 | 行为锚点 | 来源 | 场景 |
| --- | --- | --- | --- |
| 列表选择与 ID 迁移 | 取消选择不改数据；选中后本挑战 ID 从**全部非默认列表**移除，仅所选**非默认**列表追加——**选默认列表不追加**（靠默认回退覆盖） | `001_ChallengeGenerator_Data.rb:304–314` | M02 |
| 复用写回 | 保存 `Data/trainer_lists.dat`＋`Compiler.write_trainer_lists` 全量反写 PBS | `001_ChallengeGenerator_Data.rb:315–318`；`003_Compiler_WritePBS.rb:511–529` | M02-a/b |

## C 候选个体生成（7 行）

| 能力/入口 | 行为锚点 | 来源 | 场景 |
| --- | --- | --- | --- |
| 拒绝采样结构 | **无迭代上限**外循环；`isPokemonValid?` 为唯一出口门；无可满足输入不终止 | `002_ChallengeGenerator_Pokemon.rb:144–148, 354–357` | M04 |
| 物种/等级门 | 等级＝suggestedLevel；形态 0；**奇偶交替 BST 门**（偶：r<16 拒 <400、r<13 拒 <500；奇：拒 >400、r<10 拒非宝宝）；共通：最低等级、宝宝 r<10、有进化形 r<7 | `002_ChallengeGenerator_Pokemon.rb:150–170` | M04 |
| EV/性格 | 每主能力 50% 入 EV；中性/LAX/GENTLE 95% 拒；提升项不在 EV 60% 拒；降低项在 EV 90% 拒 | `002_ChallengeGenerator_Pokemon.rb:171–192` | M05 |
| 道具 | 41 项候选表；**1/40 直取 LEFTOVERS**；12 个物种专属门；FOCUSSASH 高 BST 80% 重抽；三果 50% 补 EV；等级 <10／>20 段对称替换 | `002_ChallengeGenerator_Pokemon.rb:196–258` | M06 |
| 合法招式集 | 三路来源（升级 ≤ 级／机器 ∩ 教学／宝宝蛋招）；`addMove` 权重（BUBBLE/BUBBLEBEAM 永不）；四支剪枝（必中/同代码变化/剧毒去毒/同系攻击 PP 门）；按等级缓存 | `002_ChallengeGenerator_Pokemon.rb:50–103, 105–124` | M07 |
| 招式选取 | Sketch 全位替换；<4 直接用；≥4 选取循环：大威力 50% 跳过、蓄力-喷吞成对、梦话鼾声需睡觉（20% 例外）、物理/特殊一致 80%、总威力随机门 | `002_ChallengeGenerator_Pokemon.rb:259–338` | M08、M09 |
| 终校与构造 | 道具-招式终校（LIGHTCLAY/BLACKSLUDGE/双岩石→LEFTOVERS；REST→33%/25% 双果）；IV 全 31、EV 均分、personalID 随机；`fromPokemon` EV 阈值 **>60** | `002_ChallengeGenerator_Pokemon.rb:339–357`；`002_Challenge_Data.rb:141–218` | M10 |

## D 队伍组建与迭代（6 行）

| 能力/入口 | 行为锚点 | 来源 | 场景 |
| --- | --- | --- | --- |
| 重复判定 | 同种两判据或：**槽位序敏感**的招式判据（紧凑/排序结果被丢弃，如实登记）＋道具/性格/EV 全等 | `001_ChallengeGenerator_Data.rb:126–141` | M11 |
| 补充与同种上限 | 池不足 20 反复生成至无重复入池（无上限）；**同种超 10 删最早成员**（FIFO） | `001_ChallengeGenerator_Data.rb:113–124, 143–166` | M12 |
| 队伍取样 | 按 suggestedNumber（主流程固定 2）**随机抽取即从池删除**；团队校验不过重抽（无上限、池净消耗） | `004_ChallengeGenerator_BattleSim.rb:7–22` | M13 |
| 主流程常量与检查点 | 库上限 600、高分 65、低分 40、**11 轮**；每轮池/队伍库检查点（游戏根目录 `<id>.rxdata`/`<id>_teams.rxdata`） | `001_ChallengeGenerator_Data.rb:171–197, 219, 226, 252` | M14 |
| 更替五支 | 首命中互斥：评分 <65 且场次 ≥80 替换；成员 <2 替换；**下标 ≥600 删除**；场次 ≥250 退休（成员回池）；评分 <40 替换 | `001_ChallengeGenerator_Data.rb:199–218` | M14 |
| 分层汇集 | 九层限制器（T0–T8：BST 段×非传说/仅传说/不限）；位次映射 `可入层数×位次÷总数`；层内 BST 升序拼接；**>65 队伍成员入池** | `001_ChallengeGenerator_Data.rb:56–108, 254–268` | M21、M22 |

## E 模拟对战与评级（5 行）

| 能力/入口 | 行为锚点 | 来源 | 场景 |
| --- | --- | --- | --- |
| 对战分流 | **1% 真实／99% 估算**；胜/负/平三分记入双方历史 | `004_ChallengeGenerator_BattleSim.rb:377–379, 427–437` | M15 |
| 真实分支 | 等级归一（不恢复）；NPC 类型取表首项；无视觉场景＋createBattle；debug/controlPlayer/internalBattle 关；**战后 heal＋持物还原**，其余不回滚 | `004_ChallengeGenerator_BattleSim.rb:379–419` | M16 |
| 无视觉场景合同 | 命令 1/15 Bag、1/10 Call、否则 Fight；出招/目标/换宠随机（至多 50 次门控）；确认恒真、选择恒 0 | `009_Battle_DebugScene.rb:60–105` | M16 |
| 估算打分 | 效果矩阵 **-16/-8/0/4/12/20**（飘浮/神奇守护按 Effectiveness 合同）；+BST÷10；持物 +10；评分 ×15÷100 缩放＋0–31 随机加项；平分→比评分、同→平局 | `004_ChallengeGenerator_BattleSim.rb:310–372` | M17 |
| 评级数学 | Glicko-2（1500/350/0.9；波动率牛顿迭代 ≤100 次）；**胜率两式按偏差 100 分轨**（Smogon／GLIXARE）；updateRating 累计并入＋清历史；**Elo 备选仅定义无引用** | `004_ChallengeGenerator_BattleSim.rb:135–305` | M18、M19、M20 |

## F 训练家池与写出（6 行）

| 能力/入口 | 行为锚点 | 来源 | 场景 |
| --- | --- | --- | --- |
| 列表查询 | 先含 ID 非默认列表 → **回退第一个默认列表** → 空表 | `002_Challenge_Data.rb:21–33` | M02 |
| 训练家生成 | 空表 → **200 名随机**：1/30 YOUNGSTER、余抽基础奖金 **<100** 类型；音节名（≤12 字符、≤50 次）；固定三句台词；按奖金升序 | `003_ChallengeGenerator_Trainers.rb:14–48` | M23 |
| 类型统计 | 类型计数 ≥5 → 除 4 封顶 10，否则清 0；全 0 → 普通系 1；无宝可梦号 → 全类型 1 | `003_ChallengeGenerator_Trainers.rb:64–96` | M24 |
| 权重分配与补足 | 位次差权重表 **[32,12,5,2,1,0,0,0]**；同种直判、同型乘计数；不足先同种/同型补、再**随机补位**（表长上界即停） | `003_ChallengeGenerator_Trainers.rb:99–172` | M24 |
| 列表写回 | 含 ID 列表就地换表；否则新建条目（`<id>_trainers.txt`/`<id>_pkmn.txt`）；**默认标志唯一化**（无默认则本次条目置默认） | `003_ChallengeGenerator_Trainers.rb:181–207` | M24-d |
| 反写与编译往返 | `write_trainer_lists` 重写总表＋训练家/宝可梦 PBS；编译侧逐节编回 `.dat`（台词四组 MessageTypes 哈希；`fromInspected` 解析——不存在 → nil、无效招式丢弃、全空取任意招） | `003_Compiler_WritePBS.rb:511–619`；`002_Compiler_CompilePBS.rb:951–1063` | M02、M24 |

## 附：死入口／未引用与识别边界（不占数据行）

`PlayerRatingElo` 仅定义、生成流程无引用（`004:135–164`）；`cup_fancy_trainers.txt` 与 `cup_fancy_pkmn.txt`（非 _single 变体）无任何列表/脚本引用（未引用文件）；`tocompact` 与注释掉的 `_dump/_load` 为停用代码（`002_Challenge_Data.rb:182–194`）；工厂租赁生成（`pbBattleFactoryPokemon`）属 WP57 另一条路径，不属本包。对应场景 M19、M24。
