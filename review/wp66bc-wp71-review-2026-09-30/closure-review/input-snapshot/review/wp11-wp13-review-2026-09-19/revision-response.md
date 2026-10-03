# WP11–WP13 批次修订回应（对应 report.md 逐项）

日期：2026-09-19。提取/修订侧。本文件是对 [report.md](report.md)（REQUEST_CHANGES）的逐项处理回应，**不改写任何 review 原件**。被审哈希已于修订前核对：四份规格/附表与 manifest 的 SHA-256 和字节数与 report.md 第 1 节固定版本完全一致，修订意见全部适用。

修订产物（v2）：

- `specs/overworld/wp11-map-topology-transfer.md`
- `specs/overworld/wp12-terrain-movement-vehicles.md`
- `specs/overworld/wp13-map-events-npc-followers.md`
- `specs/overworld/wp13-interpreter-command-matrix.md`
- `specs/overworld/wp13-move-route-matrix.md`（**新增**，WP13-R01 要求的移动路线目录）

逐项差异见 `revision-diffs/`（与被审快照的 diff）。新哈希与字节数已写入 `planning/review-manifest-2026-09-19.md`（被审哈希保留于历史）。

## WP11-R01 [P1] 连接向量 — 已修订

- 原表述：边字母换算（N/W→0、E→宽、S→高）+ "目标坐标 = (B边坐标或B连接坐标 − A边坐标或A连接坐标) + 当前坐标"；场景 41,S,6→45,N,0 写 (x+6,0)；7,W,5→44,E,0 用 A 图宽推 x−5；显示偏移写"(偏移差 × 图块像素) + 显示坐标"。
- 源码事实（`005_Game_MapFactory.rb:397–418, 467–473, 68–91, 114–140`；`004_Game_Map.rb:32–37`）：端点换算为二维锚点——N/S 的配置数值为锚点 x、边值为锚点 y；E/W 的边值为锚点 x、配置数值为锚点 y；显式坐标直接用。换算 xB = B锚点x − A锚点x + xA，目标须在 B 图有效范围。显示偏移按锚点差 × REAL_RES（128 子像素/格），display 坐标为子像素单位。
- 最小改动：3.2 节重建锚点定义与换算公式；第 2 节新增坐标单位分层；9.2 两例改为 (xA−6, 0) 与 (19,2)（人工 wB=20），补反向例；全部标注"仅验证参数公式，不证明真实地图可达"。
- 静态验收：锚点对齐（连接锚点映射到另一锚点）与目标合法区间检查已写入 3.2 与 9.2。

## WP11-R02 [P1] 转移入口混用 — 已修订

- 原表述：边缘跨图无 moving 守卫；"找不到目标则保持图外"被误读为可走出无连接地图；显式传送套用 Game.load_map 的缺图恢复；on_enter_map 时机不分；索引错误处理笼统；邻图生命周期整体标"未验证"。
- 源码事实：setCurrentMap 与 updateMapsInternal 均有 moving 守卫；普通移动先经 Game_Player.passable? 与 isPassableFromEdge?；transfer_player 无 ENOENT 恢复且 setup 先清集合；跨图 setup 的 on_enter_map 在 moveto 前、边缘跨图在 moveto 后；moveto 对图宽/高取模；索引 nil/负归 0、不命中回退首图、全空抛错；getMap 复用实例、setup 重建；事件临时状态（erased/starting/临时自开关）在 initialize 重置，页条件自开关在全局 $game_self_switches。
- 最小改动：第 4 节改为四入口对照表（守卫/顺序/失败）；补 moveto 取模、索引回退、通知时机与玩家位置；5.2 补实例复用/重建与临时/持久自开关分层；第 8 节改写失败条目；9.2 增补 moving、无邻图、同图传送、缺图两入口差异、索引回退、越界取模、卸载重载场景。
- 未机械接受处：报告建议"业务 on_enter 回调应具名引用"——本包只登记通知时机与订阅机制（WP05 引用），具名业务订阅者超出 WP11 范围，已在 5.1 注明不展开。

## WP11-C01（非阻塞）表头证据列 — 已修订

- 5.1 节表头补齐为 `| 时机 | 顺序（调用链） | 证据 |`，与既有三列行一致。

## WP12-R01 [P1] 通行入口混用 — 已修订

- 原表述：3.2 把"水上只能去其他水域""冰面拒绝"写成通用规则；优先级 0 写成"不受事件阻挡"；调试穿透写成无边界前提。
- 源码事实（`004_Game_Map.rb:142–268`、`006_Game_Character.rb:237–257`、`008_Game_Player.rb:238–250`）：水/冰限制在地图层**非玩家分支**；玩家走 playerPassable?（桥/冲浪/骑行规则）；角色层先边界、再 through、再源/目标双向地图层、再事件碰撞（非玩家移动者被任意非 through 事件阻挡、玩家仅被具名图形事件阻挡）；玩家覆写先 validLax?/跨图、再调试 Ctrl。
- 最小改动：3.2 重构为五层（地图层/玩家专用层/角色层/玩家覆写/跟随者严格入口），每条规则标适用对象与检查顺序；9.2 增补水→陆（玩家/普通事件）、进冰面、优先级 0+阻挡角色、无图形事件、单向阻挡、无邻图按 Ctrl 场景。
- 保留：18 地形标签能力表（复审确认可保留）未改；WP59 资格边界未扩写。

## WP12-R02 [P2] 移动状态与计步层次 — 已修订

- 原表述：can_run? 条件不全（缺 diving 例外、must_walk_or_run 误为禁跑）；速度表写成无条件强制值；岩架失败"按普通碰撞"；increase_steps 写成直接累加全局步数。
- 源码事实（`008_Game_Player.rb:52–61, 64–99, 141–160`、`006_Game_Character.rb:110–123, 397–400`）：强制路线分支按 move_speed > 3；跑鞋例外含 diving；仅 must_walk 禁跑、must_walk_or_run 不禁跑、二者都禁骑行；速度赋值受非强制路线限制且 bumping 覆盖为 3；速度等级换算 3=0.25s/4=0.125s/5=0.1s 每格；岩架分支无论 jumpForward 成败都返回；increase_steps 只重设停止计时并通知离开旧格。
- 最小改动：4.2 重写 can_run? 与状态表前提；第 2 节新增速度等级换算；4.1 补计步层次段（请求→判定→移动/跳→落地/步完成→距离统计→步后触发，全局计步引用 WP06 不另写）；强制路线与冰滑/瀑布 forced_movement 分开；9.2 增补冰面跑/骑、潜水无跑鞋、强制路线速度、岩架落点阻挡场景。

## WP12-R03 [P2] 上下水/瀑布/载具清理 — 已修订

- 原表述：上下岸笼统归 pbEndSurf；瀑布清理标"未逐分支验证"；pbCancelVehicles 写成"所有跨图都取消载具"；未登记重复上车。
- 源码事实（`004_Overworld_FieldMoves.rb:715–751, 901–923`、`001_Overworld.rb:158–168`、`008_Game_Player.rb:587–615`）：pbEndSurf 只结束冲浪（冲浪中+面前非可冲浪+跳跃成功→ending_surf；步后订阅清理）；上水是 on_player_interact 另一入口；pbTraverseWaterfall 在调试 Ctrl 或离开瀑布地形时清标记与 through；pbCancelVehicles 的游泳按 cancel_swimming、骑行按目的地 pbCanUseBike?；pbMountBike 已骑行直接返回。
- 最小改动：5.2 分上水/下水两入口并列条件与失败；5.3 补瀑布清理两分支与调用链；5.1 写清 pbCancelVehicles 参数语义与重复上车不计数；9.2 增补上岸失败、保留游泳转移、重复上车、离瀑/调试中断场景。

## WP13-R01 [P1] 命令矩阵误报与移动路线 — 已修订

- 原表述：126/133/301/311–313/315–318 被描述为有实际功能；统计 48 有实现/18 空操作；"未分派无效果"未限定；无移动路线目录。
- 源码事实：上述 10 项均直接进入 command_dummy（663、692、1064、1092–1094、1110–1113 行）；分派集合 96 = 28 dummy + 2 标记 + 66 其他入口；401 由 101 消费、655/相邻 355 由 355 合并；移动路线独立分派（`006_Game_Character.rb:428–550`）。
- 最小改动：矩阵 10 项改空操作、统计改 28/2/66/96 并加口径声明；第 1 节补续行消费规则；**新增附表 `wp13-move-route-matrix.md`**（结束/重复、1–14 移动/跳跃与 skippable 推进、15–26 等待/转向、27+ 状态/脚本、强制路线恢复、45 脚本特例）；主文档第 5 节摘要同步改写。
- 静态例已列：126 不改变背包、301 不启动战斗、311 不改变 HP、355+655 合并、skippable 与不可跳过路线推进差异（附表第 3 节）。

## WP13-R02 [P1] 启动效果/等待/推进混谈 — 已修订

- 源码事实（逐项重核）：209 设路线后返回 true（不等），210 才置路线等待；203 仅已有滚动返回 false；205/206/207/223/224/225/232/234/236 启动后继续；233 设旋转速度；242/246 淡出后立即继续；355 合并续行且总返回 true；105 体内 +1 且返回 true（双重推进）；111 支持 0/1/2/3/6/7/11/12，actor/enemy/item/weapon/armor 被注释沿默认 false；122 六操作、除/余 0 或 1 跳过、乘 1 跳过、±99,999,999 截断；314 参数 0 按 HEAL_STORED_POKEMON 分支；204 仅 panorama/fog/battleback；353 调 pbStartOver(true)；351 置标记 + @index+=1 + 返回 false。
- 最小改动：矩阵新增"控制结果列口径"段并逐行改写受影响行（203/204/205/206/207/209/210/223/224/225/232/233/234/236/242/246/105/111/122/314/351/353/355）；主文档 4.1 补指令推进行、第 5 节补"启动效果 ≠ 等待完成"要点；9.2 增补 209→开关 vs 209→210→开关、新旧滚动、效果后下一命令、355 false、105 双推进、未支持条件、除零/取余 1、314 参数场景。
- 未修参考缺陷（如 105 双推进如实登记为行为事实）。

## WP13-R03 [P1] 失联 ≠ 终止 — 已修订

- 原表述："忘记事件 ID（终止当前事件）"。
- 源码事实（`003_Interpreter.rb:92–101`、`004_Interpreter_Commands.rb:128–135`）：失联仅 @event_id = 0，不清 list/index/child；command_end 才清列表并结束跟随者覆盖、解锁事件。
- 最小改动：4.1 失联行改写；4.2 分"命令结束/显式退出/地图失联"三态；9.2 补"失联后合法开关命令仍执行"场景；第 8 节同步。

## WP13-R04 [P2] 触发类型与更新机会 — 已修订

- 原表述：trigger=1 配 check_event_trigger_touch；"事件接触=同位可穿透"；感知"进入视野即启动"；"屏幕外不更新"。
- 源码事实（`007_Game_Event.rb:133–195, 260–271`、`008_Game_Player.rb:332–407, 543–552`、`004_Game_Map.rb:461–465`、`001_Overworld.rb:340–389`）：事件侧 check_event_trigger_touch 处理 trigger=2；玩家侧另有 here/there/touch 三检查；over_trigger? 非 through 别名（图形、hiddenitem、占格通行）；感知要 trigger=2+解释器未运行+非 starting+非跳跃/over_trigger，sight/trainer 可达、counter 面向；should_update? 有提前许可；菜单中地图事件不更新、公共事件仍更新。
- 最小改动：3.2 改为按调用者分入口的触发表 + 更新机会段；第 2 节新增 over_trigger? 定义；9.2 增补屏外并行、菜单中地图/公共差别、无图形非 through 同位、hiddenitem、视线命中不可达场景。

## WP13-R05 [P2] 跟随流程补全 — 已修订

- 原表述：跟随一节是方法导航；"有跟随者时地图传送与载具使用被阻止"扩大化；现有机制整体留待"完整跟随系统"。
- 源码事实（`010_Game_Follower.rb:91–109, 134–167`、`011_Game_FollowerFactory.rb:30–50, 89–136, 165–189, 242–290`、`008_Game_Player.rb:42–48`）：守卫只在调用它的场地/道具入口生效；transfer_player 无守卫且携带跟随者；add_follower 去重；remove 三入口；follow_leader 强制路线跳过/身后格/岩架/相连与不相连/相对向量换图；fancy_moveto 1 走 2 跳远定位；map_transfer_followers 放置+invisible_after_transfer+移动恢复；update 同步速度/透明/冰滑；interact 公共事件覆盖。
- 最小改动：6.2 重写为行为条目（加入去重/移除/实例化/移动更新/显式传送/互动/转移限制/持久化）；明确"受守卫阻止的入口"与"仍携带跟随者的显式传送"区分；9.2 增补重复加入、跨图跟随、显式传送携带、受守卫阻止场景。
- 未扩张：完整"跟随宝可梦"系统仍列未决问题 3，未无证扩写。

## 交叉检查（revision-prompt 第 6 节）

- WP11 转移入口 × WP12 载具：transfer_player 调 pbCancelVehicles 的参数语义已统一（WP11 第 4 节引用调用点、WP12 5.1 主规格）。
- WP12 步完成 × WP06 计步：WP12 只登记 increase_steps 实际行为与阶段顺序，全局计步引用 WP06 主规格，未另写第二套。
- WP13 路线/触发/跟随 × WP11/12：跟随者跨图用 WP11 相对位置换算；路线阻挡通行归 WP12 引用；210 的移动等待与 WP12 强制路线一致。
- WP13 解释器异常 × WP07：脚本异常分类（SystemExit/Reset 原样抛出）引用 WP07 分层。
- WP11 缺图入口 × WP09/10：缺图恢复分支仅属 Game.load_map（WP09/WP10 引用），transfer_player 路径无恢复（WP11 第 8 节）。

## 状态声明

- WP11/WP12/WP13 三包 v2 自检完成，状态保持 **ReviewPending**，再送外部复审；不自批 Reviewed。
- 所有场景均为静态推导、待运行验证；真实地图/事件/媒体缺口（U01–U10）保持开放，未擅自关闭。
- 未执行 WP14；未修改 reference/；未提交/推送。
