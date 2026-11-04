# WP06 附表：GameStats 统计字段目录（74 个声明字段）

本附表是 [wp06-time-random-steps-stats](wp06-time-random-steps-stats.md) 的取证附件（WP06-R03 验收物）。
范围为 `S/004_Game classes/012_Game_Stats.rb` 中 GameStats 类的全部 **74 个声明字段**（attr 声明；不含派生 getter 与 Game_Temp 锚点，见文末说明）。
更新入口按 2026-09-19 对固定基线（commit `8c5911e4`）的 `$stats.<字段>` 全仓检索与关键段阅读登记；"更新逻辑静态已知"与"Demo 事件可达未证"可以同时成立，**事件可达性一律不证明**。

证据等级：静态确认（有明确脚本写入入口）/ 已定位（入口明确但未逐行精读）/ 待验证 U01（写入依赖缺失的 NPC/地图事件，代码注释声明但当前快照无事件可读）。

## 1. 旅行（8 字段）

| 字段 | 单位/形态 | 初始化 | 更新规则类别与定位 | 持久化/重置 | 证据等级 | 后续责任 |
| --- | --- | --- | --- | --- | --- | --- |
| distance_walked | 累计量（步） | 0 | 移动距离累加 `008_Game_Player.rb:136` | 保存值 | 静态确认 | WP61（步数效果） |
| distance_cycled | 累计量（步） | 0 | 骑行距离累加 同文件:134 | 保存值 | 静态确认 | WP61 |
| distance_surfed | 累计量（步，含潜水） | 0 | 水上距离累加 同文件:132 | 保存值 | 静态确认 | WP61 |
| distance_slid_on_ice | 累计量（步，计入 walked） | 0 | 冰面滑行距离累加 同文件 | 保存值 | 静态确认 | WP61 |
| bump_count | 次数 | 0 | 碰撞累加 同文件:123 | 保存值 | 静态确认 | WP61 |
| cycle_count | 次数 | 0 | 骑行开始累加 同文件 | 保存值 | 静态确认 | WP59 |
| surf_count | 次数 | 0 | 冲浪开始累加 `012_Overworld/004_Overworld_FieldMoves.rb` | 保存值 | 静态确认 | WP59 |
| dive_count | 次数 | 0 | 潜水开始累加 同文件 | 保存值 | 静态确认 | WP59 |

## 2. 场地动作（10 字段）

| 字段 | 单位/形态 | 初始化 | 更新规则类别与定位 | 持久化/重置 | 证据等级 | 后续责任 |
| --- | --- | --- | --- | --- | --- | --- |
| fly_count | 次数 | 0 | 飞翔使用累加 `004_Overworld_FieldMoves.rb` | 保存值 | 静态确认 | WP59 |
| cut_count | 次数 | 0 | 砍树使用累加 同文件 | 保存值 | 静态确认 | WP59 |
| flash_count | 次数 | 0 | 闪光使用累加 同文件 | 保存值 | 静态确认 | WP59 |
| rock_smash_count | 次数 | 0 | 碎岩使用累加 同文件 | 保存值 | 静态确认 | WP59 |
| rock_smash_battles | 次数 | 0 | 碎岩触发战斗累加 同文件 | 保存值 | 静态确认 | WP59/WP36 |
| headbutt_count | 次数 | 0 | 头锤使用累加 同文件 | 保存值 | 静态确认 | WP59 |
| headbutt_battles | 次数 | 0 | 头锤触发战斗累加 同文件 | 保存值 | 静态确认 | WP59/WP36 |
| strength_push_count | 次数（推动次数，非使用次数） | 0 | 怪力推动累加 `003_Game processing/003_Interpreter.rb` | 保存值 | 静态确认 | WP59 |
| waterfall_count | 次数 | 0 | 攀瀑使用累加 `004_Overworld_FieldMoves.rb` | 保存值 | 静态确认 | WP59 |
| waterfalls_descended | 次数 | 0 | 瀑布下行累加 `004_Overworld_FieldMoves.rb:910`；瀑顶跳下 `008_Game_Player.rb:157` | 保存值 | 静态确认 | WP59 |

## 3. 道具活动（9 字段）

| 字段 | 单位/形态 | 初始化 | 更新规则类别与定位 | 持久化/重置 | 证据等级 | 后续责任 |
| --- | --- | --- | --- | --- | --- | --- |
| repel_count | 次数 | 0 | 喷雾使用累加 `013_Items/002_Item_Effects.rb` | 保存值 | 静态确认 | WP28 |
| itemfinder_count | 次数 | 0 | 探测仪使用累加 同文件 | 保存值 | 静态确认 | WP28 |
| fishing_count | 次数 | 0 | 钓鱼开始累加 `012_Overworld/005_Overworld_Fishing.rb` | 保存值 | 静态确认 | WP60 |
| fishing_battles | 次数 | 0 | 钓鱼战斗累加 `013_Items/002_Item_Effects.rb` | 保存值 | 静态确认 | WP60/WP36 |
| poke_radar_count | 次数 | 0 | 雷达使用累加 `013_Items/005_Item_PokeRadar.rb` | 保存值 | 静态确认 | WP37 |
| poke_radar_longest_chain | 最大值 | 0 | 雷达连锁最长纪录更新 同文件 | 保存值 | 静态确认 | WP37 |
| berry_plants_picked | 次数 | 0 | 树果采摘累加 `012_Overworld/006_Overworld_BerryPlants.rb` | 保存值 | 静态确认 | WP60 |
| max_yield_berry_plants | 次数（达到/超过该树果最高产量条件的采摘） | 0 | 确认且背包可添加后，采摘量 ≥ 该树果 maximum_yield 时加 1 `012_Overworld/006_Overworld_BerryPlants.rb:437–454`（不保存最大产量值） | 保存值 | 静态确认 | WP60 |
| berries_planted | 次数 | 0 | 树果种植累加 同文件 | 保存值 | 静态确认 | WP60 |

## 4. NPC（3 字段）

| 字段 | 单位/形态 | 初始化 | 更新规则类别与定位 | 持久化/重置 | 证据等级 | 后续责任 |
| --- | --- | --- | --- | --- | --- | --- |
| poke_center_count | 次数 | 0 | 治疗点事件累加——**缺失 NPC 事件**（代码注释声明，当前快照无事件可读） | 保存值 | **待验证 U01** | WP77 |
| revived_fossil_count | 次数 | 0 | 化石复活事件累加——缺失 NPC 事件 | 保存值 | **待验证 U01** | WP77 |
| lottery_prize_count | 次数 | 0 | 彩票兑奖事件累加——缺失 NPC 事件 | 保存值 | **待验证 U01** | WP70/WP77 |

## 5. 宝可梦（11 字段）

| 字段 | 单位/形态 | 初始化 | 更新规则类别与定位 | 持久化/重置 | 证据等级 | 后续责任 |
| --- | --- | --- | --- | --- | --- | --- |
| eggs_hatched | 次数 | 0 | 孵化完成累加 `016_UI/001_Non-interactive UI/003_UI_EggHatching.rb` | 保存值 | 静态确认 | WP35/WP67-B |
| evolution_count | 次数 | 0 | 进化完成累加 `016_UI/001_Non-interactive UI/004_UI_Evolution.rb` | 保存值 | 静态确认 | WP31/WP67-B |
| evolutions_cancelled | 次数 | 0 | 进化取消累加 同文件 | 保存值 | 静态确认 | WP31/WP67-B |
| trade_count | 次数 | 0 | 交换完成累加 `016_UI/001_Non-interactive UI/005_UI_Trading.rb` | 保存值 | 静态确认 | WP26/WP67-B |
| moves_taught_by_item | 次数 | 0 | 机器教学累加 `019_Utilities/001_Utilities.rb` | 保存值 | 静态确认 | WP28/WP30 |
| moves_taught_by_tutor | 次数 | 0 | 导师教学累加 同文件 | 保存值 | 静态确认 | WP30 |
| moves_taught_by_reminder | 次数 | 0 | 回忆教学累加 `016_UI/022_UI_MoveRelearner.rb` | 保存值 | 静态确认 | WP30/WP66-A |
| day_care_deposits | 次数 | 0 | 寄存放置累加 `012_Overworld/007_Overworld_DayCare.rb` | 保存值 | 静态确认 | WP33 |
| day_care_levels_gained | 累计量（级） | 0 | 寄养升级累计 同文件 | 保存值 | 静态确认 | WP33 |
| pokerus_infections | 次数 | 0 | 病毒感染累加 `014_Pokemon/001_Pokemon.rb` | 保存值 | 静态确认 | WP61 |
| shadow_pokemon_purified | 次数 | 0 | 净化完成累加 `014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb` | 保存值 | 静态确认 | WP23/WP67-B |

## 6. 战斗（10 字段）

| 字段 | 单位/形态 | 初始化 | 更新规则类别与定位 | 持久化/重置 | 证据等级 | 后续责任 |
| --- | --- | --- | --- | --- | --- | --- |
| wild_battles_won | 次数 | 0 | 野生战斗胜利累加 `012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb` | 保存值 | 静态确认 | WP42 |
| wild_battles_lost | 次数（含逃跑） | 0 | 野生战斗失败/逃跑累加 同文件 | 保存值 | 静态确认 | WP42 |
| trainer_battles_won | 次数 | 0 | 训练家战斗胜利累加 同文件；设施挑战 `018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb` | 保存值 | 静态确认 | WP42/WP55 |
| trainer_battles_lost | 次数 | 0 | 训练家战斗失败累加 同两处 | 保存值 | 静态确认 | WP42/WP55 |
| total_exp_gained | 累计量（经验） | 0 | 战斗经验累计 `011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb` | 保存值 | 静态确认 | WP30/WP42 |
| battle_money_gained | 累计量（金钱） | 0 | 战斗奖金累计 `011_Battle/001_Battle/002_Battle_StartAndEnd.rb` | 保存值 | 静态确认 | WP42 |
| battle_money_lost | 累计量（金钱） | 0 | 战败扣款累计 同文件 | 保存值 | 静态确认 | WP42/WP61 |
| blacked_out_count | 次数 | 0 | 全灭回程累加 `012_Overworld/001_Overworld visuals/003_Overworld_MapTransitionAnims.rb` | 保存值 | 静态确认 | WP61 |
| mega_evolution_count | 次数 | 0 | Mega 进化累加 `011_Battle/001_Battle/008_Battle_ActionOther.rb` | 保存值 | 静态确认 | WP40 |
| failed_poke_ball_count | 次数 | 0 | 捕获失败球累加 `011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb` | 保存值 | 静态确认 | WP38 |

## 7. 货币（11 字段）

| 字段 | 单位/形态 | 初始化 | 更新规则类别与定位 | 持久化/重置 | 证据等级 | 后续责任 |
| --- | --- | --- | --- | --- | --- | --- |
| money_spent_at_marts | 累计量 | 0 | 商店消费累计 `016_UI/020_UI_PokeMart.rb` | 保存值 | 静态确认 | WP29 |
| money_earned_at_marts | 累计量 | 0 | 商店收入累计 同文件 | 保存值 | 静态确认 | WP29 |
| mart_items_bought | 累计量（件） | 0 | 全部物品成功加入后按数量累加 `016_UI/020_UI_PokeMart.rb:636–644`；BP 商店 `016_UI/021_UI_BattlePointShop.rb:484–492`（非每笔交易固定加 1） | 保存值 | 静态确认 | WP29 |
| premier_balls_earned | 累计量（个） | 0 | 按实际添加的纪念球数累加 `016_UI/020_UI_PokeMart.rb:647–661`（多球奖励分支按成功添加数；单球奖励分支加 1） | 保存值 | 静态确认 | WP29 |
| drinks_bought | 次数 | 0 | 饮料购买事件累计——**缺失售卖机事件** | 保存值 | **待验证 U01** | WP29/WP77 |
| drinks_won | 次数 | 0 | 饮料中奖事件累计——缺失售卖机事件 | 保存值 | **待验证 U01** | WP29/WP77 |
| coins_won | 累计量 | 0 | 代币赢取累计 `017_Minigames/004_Minigame_VoltorbFlip.rb`、`003_Minigame_SlotMachine.rb` | 保存值 | 静态确认 | WP69 |
| coins_lost | 累计量 | 0 | 代币损失累计 `003_Minigame_SlotMachine.rb` | 保存值 | 静态确认 | WP69 |
| battle_points_won | 累计量 | 0 | **当前未定位到更新入口，写入来源待查**（声明与初始化 `012_Game_Stats.rb:49,131`；"可能位于缺失设施发奖事件"为推断/待证，不由搜索未命中证明） | 保存值 | **待验证**（来源待查，归 WP55/WP77 核实） | WP55/WP77 |
| battle_points_spent | 累计量 | 0 | BP 消费累计 `016_UI/021_UI_BattlePointShop.rb` | 保存值 | 静态确认 | WP29 |
| soot_collected | 累计量 | 0 | 火山灰收集累计 `012_Overworld/001_Overworld.rb` | 保存值 | 静态确认 | WP61 |

## 8. 特殊（9 字段）

| 字段 | 单位/形态 | 初始化 | 更新规则类别与定位 | 持久化/重置 | 证据等级 | 后续责任 |
| --- | --- | --- | --- | --- | --- | --- |
| gym_leader_attempts | 数组（[0]*50） | 数组 | 道馆挑战事件按序号累加——**缺失道馆事件** | 保存值 | **待验证 U01** | WP77 |
| times_to_get_badges | 数组（秒，[]） | 空数组 | 赋值方法 `012_Game_Stats.rb:165–166`（按徽章序号写入当前 play_time）；**赋值机制静态已知，事件调用者未定位**（待证，不以"缺失事件"否定机制） | 保存值 | 静态确认（方法可读；调用者未证） | WP77 |
| elite_four_attempts | 次数 | 0 | 四天王门前事件累加——缺失事件 | 保存值 | **待验证 U01** | WP77 |
| hall_of_fame_entry_count | 次数 | 0 | 名人堂进入事件累加——缺失事件 | 保存值 | **待验证 U01** | WP67-B/WP77 |
| time_to_enter_hall_of_fame | 秒 | 0 | 赋值方法 `012_Game_Stats.rb:169–170`（当前值为 0 时赋当前 play_time）；**赋值机制静态已知，事件调用者未定位**；UI 为展示读取（`016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:246`） | 保存值 | 静态确认（方法可读；调用者未证） | WP67-B |
| safari_pokemon_caught | 次数 | 0 | 狩猎区捕获累加 `018_Alternate battle modes/001_SafariZone.rb:150–153` | 保存值 | **静态确认**（写入机制存在；Demo 可达未证） | WP53 |
| most_captures_per_safari_game | 最大值 | 0 | 以本次捕获累计与原纪录取最大值 同段 | 保存值 | **静态确认**（同上） | WP53 |
| bug_contest_count | 次数 | 0 | 捕虫大会开始累加 `018_Alternate battle modes/002_BugContest.rb:192–195` | 保存值 | **静态确认**（同上） | WP53 |
| bug_contest_wins | 次数 | 0 | 名次第一时累加 同文件:205–216 | 保存值 | **静态确认**（同上） | WP53 |

## 9. 游戏时间（3 字段）

| 字段 | 单位/形态 | 初始化 | 更新规则类别与定位 | 持久化/重置 | 证据等级 | 后续责任 |
| --- | --- | --- | --- | --- | --- | --- |
| play_time | 秒 | 0 | 锚点惰性累加（9 处读取点；锚点机制见主文档 3.1） | 保存值；有迁移历史（WP10） | 静态确认 | WP09 |
| play_sessions | 次数 | 0 | 新游戏/载入累加 `003_Game processing/001_StartGame.rb:50, 67` | 保存值 | 静态确认 | WP09 |
| time_last_saved | 秒 | 0 | 保存时写入当前 play_time `003_Game processing/001_StartGame.rb:116` | 保存值 | 静态确认 | WP09 |

## 10. 派生值与非声明项（不计入 74）

- `distance_moved`：walk+cycle+surf 三者之和（派生 getter）。
- `caught_pokemon_count`：按图鉴现算（非计数器）。
- `save_count`：来自 `$game_system`（非本类字段）。
- `Game_Temp.last_uptime_refreshed_play_time`：游戏时间锚点（临时状态，非保存字段）。

## 11. 口径与限制

- 本目录覆盖全部 74 个声明字段；声明集合与本目录成员集合机械对照一致，无漏项。
- 更新入口以 `$stats.<字段>` 全仓文本检索 + 关键段阅读登记；检索不是调用可达证明，逐入口语义核对仍在相应领域包完成。
- 标"待验证 U01"的字段（8 个）：写入依赖缺失的 NPC/地图事件（poke_center_count、revived_fossil_count、lottery_prize_count、drinks_bought、drinks_won、gym_leader_attempts、elite_four_attempts、hall_of_fame_entry_count），代码注释声明更新方式但当前快照无事件可读；不对同组其他字段连带标待证。
- **赋值机制静态已知、事件调用者未证**（不标 U01）：time_to_enter_hall_of_fame（`012_Game_Stats.rb:169–170`）、times_to_get_badges（同文件 165–166）——方法定义可读不等于调用链已确认，调用事件缺失也不等于赋值方法未知。
- **来源待查**（不标 U01、不虚构）：battle_points_won——当前未定位到更新入口，"可能位于缺失设施发奖事件"为推断/待证，归 WP55/WP77 核实，不由搜索未命中证明一定来自该事件。
- 保存/恢复生命周期与迁移归 WP09/WP10；覆盖审查归 WP79；本表不替代它们。
