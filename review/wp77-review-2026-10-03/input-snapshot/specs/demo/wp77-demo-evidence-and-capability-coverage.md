# WP77 规格：demo 证据与能力覆盖（配置事实／静态能力候选／事件链待证）

分类：**Demo / Developer Experience**（demo 配置与能力覆盖）；遭遇/训练家/生物流程标 **Creature-RPG** 与 **Pokémon Rules**；战斗设施/大会/规则交界标 **Combat Requirements**（只登记接口要求）；地图/连接/天气/地牢/宿主环境标 **Engine / Overworld Integration**；区域地图/电话/Pokégear 标 **User Interface**；配置加载与 PBS 管线标 **Generic Kernel**。

状态：**ReviewPending（A～D 具名静态范围，待统一 review）**——不自行标 Reviewed、不宣称通过；**配置存在 ≠ 已演示，入口存在 ≠ 可达**。

---

## 1. 目的、范围与非目标

### 1.1 目的

从作者/玩家可理解的功能视角，登记当前快照中 demo 的**配置事实与能力候选**，并按证据强度分层：

1. **已有配置事实**：某地图/区域/场景/设施/遭遇/训练家/联系人被配置（PBS 文本直接证据）。
2. **静态能力/调用证据**：已有源码入口和条件，或已批准规格可解释配置的消费行为。
3. **有地图/公共事件内容支持的具体演示调用链**：**当前材料无法建立**（地图/公共事件/资源缺失，U01）。
4. **运行观察**：**本任务不运行，不产生运行确认**。

同时给出每个能力候选的**缺口登记**：已能证明什么、仍缺何种事件/地图/资源证据、缺口影响哪个结论、以后补证应验证什么。

### 1.2 范围（A～D）

- **A 世界配置与入口候选**：起始元数据、地图登记（69 节）、地图连接（19 条）、区域地图（2 区 27 点）、地牢参数与特殊旗标图。
- **B 生物与玩家流程候选**：遭遇配置（19 节）、训练家配置（20 节）、电话联系人（2 名）。
- **C 特殊玩法与设施候选**：Safari Zone、捕虫大会、战斗边疆（Tower/Palace/Arena/Factory/Stadium）、小游戏场所、特殊机制图。
- **D UI 与作者工作流候选**：区域地图飞行点、电话系统、编辑器/编译/生成工具链。

### 1.3 非目标与硬边界

- **不把配置存在写成已演示/可达**：地图 ID/坐标/连接存在不证明实际几何、事件页或路径可达；入口函数存在、编译器能生成事件或注释中的示例，均不证明 bundled demo 实际放置了事件、执行到该入口或完成奖励/收费流程。
- **不把「没有事件材料」写成「demo 没有该活动」**；没有搜索命中也不自动证明某能力不存在。不假定正常启动可达，也不假定缺文件时所有读取都回退。
- 不重提取已通过主规格（WP01/WP04/WP11～WP17/WP19/WP20/WP23～WP76 等按依赖身份引用）；不运行游戏/编译器/生成器/反序列化/参考行为模拟器；不使用 WP79 的 coverage 占位文件或 WP80 最终 traceability 占位文件冒充本轮交付。
- 额外费用、奖励和剧情前提若归缺失事件，**逐项待证**；候选示例与已证示例各有状态，不混为同一计数。

### 1.4 必需依赖（具名通过范围按引用继承，当前磁盘身份见登记）

| 依赖 | 用途 |
| --- | --- |
| WP01（基线） | 材料缺口清单、U01 处置登记、证据五档定义 |
| WP04（PBS 生命周期） | PBS 编译发现/写回管线与默认数据载入边界 |
| WP11/WP12（地图拓扑/地形） | 地图连接、通行、传送与地图位置的运行语义（只引用） |
| WP13（地图事件） | 事件/页面/命令的运行语义（配置消费只引用） |
| WP15（资源匹配与音频） | 地图 BGM/战斗背景与素材缺失影响 |
| WP17（消息与输入） | 电话/消息文本的合同（只引用） |
| WP36/WP60（遭遇/树果） | 遭遇表类型与时段/工具触发的合同 |
| WP53（Safari/捕虫大会） | Safari 会话、捕虫会话与 BugContest 遭遇类型消费 |
| WP54/WP55/WP56/WP57（设施） | 参赛资格、设施会话、Palace/Arena、Factory 租赁的合同 |
| WP61（野外被动） | 野外步进/天气/效果次序的合同 |
| WP63（Pokégear/地图/电话） | 区域地图点/飞行/电话系统的消费合同 |
| WP64（邮件/神秘礼物） | 邮件/礼物流程的交界（事件证据缺失） |
| WP65（标题/载入） | 启动/载入与新游戏入口的合同 |
| WP66-A/B/C（队伍/存储/背包 UI） | Box Link、图鉴、背包入口的合同（DisableBoxLink 旗标消费） |
| WP67-A/B（战斗 UI/生命周期） | 战斗呈现与进化/名人堂演出合同 |
| WP68/69/70（小游戏） | Duel/Triad/Slot/Voltorb/Lottery/Mining 的具名静态范围（B 导入稿） |
| WP71（Tile Puzzles） | 拼图玩法具名静态范围 |
| WP72/WP73-A/B（调试/编辑器） | 调试入口与内容/世界编辑器的作者工作流 |
| WP74/WP75/WP76（动画/编译/生成器） | 动画制作、编译转换与设施内容生成工具链 |

## 2. 概念与术语（实现中立）

- **证据四档**：①配置事实（文本直接证据）→②静态能力证据（源码入口/已批准规格可解释消费）→③事件证据链（需地图/公共事件材料，当前不可达）→④运行观察（本任务不做）。每条登记标明档位；档位不提升。
- **能力候选**：有配置或入口线索、但事件证据不足以确认完整行为的能力；候选与已证示例分别计数。
- **缺口（U01 系）**：快照中不存在且限制结论证据强度的材料——`Data/Map*.rxdata`/`MapInfos.rxdata`/`CommonEvents.rxdata`/`System.rxdata`/`Tilesets.rxdata`/`Animations.rxdata`、`Graphics/`、`Audio/`、`Plugins/`、`Game.ini`、`Game.rxproj`（WP01 §4.2 继承）。
- **节（section）**：PBS 文本中 `[编号]` 或 `[类型,名]` 的登记单位；地图节 69、遭遇节 19、训练家节 20（本包实测）。
- **旗标（flag）**：地图元数据的行为标记，消费方为脚本或进化数据（本包实测四条消费链：DistortionWorld、ScaleWildEncounterLevels、LocationFlag 进化、WP53 大会旗标）。

## 3. 当前材料状态（WP01 基线继承）

- **Data 顶层仅三项**：`Scripts/`（312 个 .rb）、`Scripts.rxdata`、`messages_core.dat`（开工实测同 WP75/WP76 轮复核一致）。
- **缺失清单（逐项存在性核验）**：`Data/Map*.rxdata`、`Data/MapInfos.rxdata`、`Data/CommonEvents.rxdata`、`Data/System.rxdata`、`Data/Tilesets.rxdata`、`Data/Animations.rxdata`、`Graphics/`、`Audio/`、`Plugins/`、`Game.ini`、`Game.rxproj` **均不存在**。
- **直接后果**：地图几何/事件页/NPC 对话/传送链/商店库存/奖励收费/公共事件流程**一律不可验证**；配置消费行为只按已批准主规格的静态合同描述，不断言 demo 实际放置与执行。
- **不推出**：不据缺文件断言正常启动必走空表回退（编译管线可从现存 PBS 生成运行数据——WP75 已批准范围）；不据 PBS 存在断言 demo 已演示。

## 4. A：世界配置与入口候选

### 4.1 起始与玩家元数据（`PBS/metadata.txt`，33 行全文）

- **[0] 全局**：StartMoney＝3000、StartItemStorage＝POTION、Home＝3,7,5,8（地图 3＝Player's house 内点 (7,5)、朝向 8）；野生/训练家战斗与胜利 BGM、Surf/Bicycle BGM 已配置。
- **[1] Red／[2] Leaf**：两位玩家外观定义（TrainerType `POKEMONTRAINER_Red`／`POKEMONTRAINER_Leaf`；走/跑/骑行/冲浪/潜水/垂钓角色图名已配置）。
- 档位：①配置事实。新游戏初始化与角色外观的消费者属 WP24/WP65 合同；实际新游戏流程不可验证（③缺口）。

### 4.2 地图登记（`PBS/map_metadata.txt`，69 节，[001]–[075]，缺号 022／032／033／042／043／048）

- **户外图**：Lappet Town(002)、Route 1(005)、Cedolan City(007)、Route 2(021)、Lerucean Town(023)、Natural Park(028)、Route 3(031)、Ingido Plateau(035)、Route 4(039/040)、Route 5(041/045)、Route 6(044)、Route 7(047)、Battle Frontier(052)、Safari Zone 外(066)/内(068)、Route 8(069)、Berth Island(072)、Faraday Island(073)、Tiall Region(075)——均带 MapPosition（区域坐标，与 §4.4 区域地图点对应）。
- **室内/设施图**：玩家家(003)、实验室(004)、Kurt 家(006)、Daisy 家(008)、Poké Center×4(009/024/053)、商店(025/054)、研究所(011)、公寓(012)、Game Corner(013)、百货 1–5F＋天台＋电梯(014–020)、Cedolan Gym(010)、球迷俱乐部(026)、寄养屋(027)、公园入口/会馆(029/030)、联盟入口/房间 1/名人堂(036/037/038)、自行车道闸口×2(046/074)、岩洞 1F/B1F(049/050)、Dungeon(051)、边疆 Poké Center(053)/商店(054)、Battle Tower(055)/arena(056)、Stadium Cup lobby(057)、Battle Palace(058)/arena(059)、Battle Arena(060)/arena(061)、Battle Factory(062)/intro corridor(063)/arena(064)/corridor(065)、Safari 大门(067)、水下(070)、码头(071)。
- **治疗点（HealingSpot）**：玩家家(003：地图 2＠(8,8))、Cedolan PC(009：地图 8＠(17,11))、Lerucean PC(024：地图 23＠(11,15))、联盟入口(036：地图 35＠(17,7))、边疆 PC(053：地图 52＠(17,14))、Battle Tower(055：地图 52＠(30,10))——**按配置原样登记**（009 行指向地图 8，为配置原文，不作语义修正）。
- **天气**：Route 2(021)＝Rain 100、Route 7(047)＝Rain 0、Berth Island(072)＝Storm 50。
- **特殊旗标/图**（消费链见 §6.2）：MossRock(028)、IceRock(034)、Magnetic(049/050/051)、DistortionWorld(049/050/051/072/073)、ScaleWildEncounterLevels(051)、BugContest(028)、BugContestReception(029/030)、DisableBoxLink(010/037/038/056/059/061/063/064/065)、DarkMap(050)、Dungeon(051)、SafariMap(068)、DiveMap 70(069)、Environment 各值（Cave/Rock/Forest/Underwater）、Bicycle/BicycleAlways 各行、MapSize 各行。
- 档位：①配置事实。几何与可达性不可验证（③缺口）；元数据消费合同按 WP11/WP12/WP13/WP61/WP66-B 引用。

### 4.3 地图连接（`PBS/map_connections.txt`，19 条全文）

19 条连接全部命中已登记地图（§6.1 实测）：Lappet(002)↔Route 1(005)↔Cedolan(007)↔{Route 2(021)、Route 6(044)、Lerucean(023)、Route 7(047)}、Lappet↔Safari 外(066)↔{Route 1、Route 8(069)}、Lerucean(023)↔{Route 2、Route 3(031)、Cedolan}、Route 3↔Ingido Plateau(035)↔Route 4(039)、Route 5(041)↔{Route 4 自行车道(040)、Route 6 自行车道(045)}、Route 6(044)↔Route 1、Route 7(047)↔{Cedolan、Route 2、Battle Frontier(052)}——**连接图存在 ≠ 通行条件已配置**（方向/位移按 WP11 合同；几何不可验证）。

### 4.4 区域地图与飞行点（`PBS/town_map.txt`，2 区 27 点全文）

- **[0] Essen 区**（mapRegion0.png）：26 点——城镇/道路/地标点 21（Lappet Town(Oak's Lab)、Route 1/2/3/4/5/6/7、Cedolan City×2(Dept. Store)、Lerucean Town、Natural Park、Route 3 Ice Cave、Ingido Plateau、Battle Frontier、Safari Zone、Route 8 Diving area、Rock Cave、Cycle Road×3）＋**5 个飞行点**（Lappet Town→地图 2＠(8,8)、Cedolan Dept.→地图 7＠(47,11)、Lerucean→地图 23＠(11,15)、Ingido Plateau→地图 35＠(17,7)、Battle Frontier→地图 52＠(17,14)）＋**2 个开关点**（Berth Island 开关 51、Faraday Island 开关 52）。
- **[1] Tiall 区**（mapRegion1.png）：1 点（Here）。
- 档位：①配置事实；飞行点与 §4.2 治疗点/地图的对应关系可静态核对（②——仅 Lappet/Battle Frontier 与治疗点同图同坐标；Cedolan 飞行点指向地图 7 城内坐标、与治疗点配置不同，按配置原样登记）。区域地图 UI 消费合同按 WP63 引用；实际飞行解锁（开关/剧情前提）不可验证（③缺口）。

### 4.5 地牢参数（`PBS/dungeon_parameters.txt`，2 套全文）

- **[cave]**：5×4 网格、单元 10×10、房间 5–9、走廊宽 2、NodeLayout/RoomLayout＝full、RoomChance 70、ExtraConnections 2、FloorPatches 2,50,25、FloorDecorations/VoidDecorations 50,200。
- **[forest]**：同构（房间 4–8、FloorPatches 3,75,25）。
- 档位：①配置事实；地牢生成器合同按 WP14（随机地牢）引用；参数集与地图的绑定（map 051 `Dungeon = true`）按配置原文登记，实际生成结果不可验证。

## 5. B：生物与玩家流程候选

### 5.1 遭遇配置（`PBS/encounters.txt`，19 节全文）

- **节—图对应**（§6.1 实测全部命中 §4.2 登记）：002 Lappet Town、005 Route 1、**[005,1] Route 1 变体**、021 Route 2、028 Natural Park、031 Route 3、034 Ice Cave、039 Route 4、041 Route 5、044 Route 6、047 Route 7、049/050 Rock Cave、051 Dungeon、066 Safari 外、068 Safari、069 Route 8、070 水下、075 Tiall Region。
- **遭遇类型矩阵**（13 种实测）：Land（陆／晨昏时段）、LandMorning、LandNight、Water（水面）、Cave（洞穴）、OldRod／GoodRod／SuperRod（三级钓竿）、RockSmash（碎岩）、HeadbuttLow／HeadbuttHigh（撞树两档）、PokeRadar（雷达）、**BugContest（捕虫大会专用——已在遭遇类型注册表注册，§6.3）**。
- **内容形态**：每条为「权重, 物种(_形态), 等级(或区间)」；**051 Dungeon 全表为等级 1 的幼年种**（配合 ScaleWildEncounterLevels 旗标——运行时等级由队伍平衡级重算，§6.2）；**075 Tiall 为 _1 形态种**（GEODUDE_1／RATTATA_1／DIGLETT_1／MEOWTH_1／SANDSHREW_1／VULPIX_1＋CUBONE／PIKACHU）。
- 档位：①配置事实；遭遇触发/时段/工具合同按 WP36/WP60/WP12 引用；具体遭遇发生不可验证（③缺口）。

### 5.2 训练家配置（`PBS/trainers.txt`，20 节全文）

- **类型核对**（§6.4 实测）：15 个使用类型（BEAUTY、CAMPER、CHAMPION、COOLCOUPLE、FISHERMAN、HIKER、LASS、LEADER_Brock、PICNICKER、POKEMONTRAINER_May、RIVAL1、SWIMMER2_F、TEAMROCKET_F、TEAMROCKET_M、YOUNGSTER）**全部在 `PBS/trainer_types.txt` 注册**。
- **全字段样例**：LEADER Brock——道具 FULLRESTORE×2；GEODUDE(12) 指定招式/特性位/性别/IV 全 20；ONIX(14) 昵称 Rocky、指定招式、SITRUSBERRY、**Shiny、HEAVYBALL**。
- **Shadow 个体×2**：TEAMROCKET_M Grunt(1) 的 WEEPINBELL(21)、TEAMROCKET_F Grunt(1) 的 ELECTABUZZ(20)（WP23 净化室/Shadow 合同引用）。
- **版本系列**：RIVAL1 Blue 三变体（初始伙伴差异）、CHAMPION Blue（三只 63 级各持 SITRUSBERRY）、CAMPER Jeff 与 PICNICKER Susie 的**再战版 v1**（等级提升队伍——与 §5.3 电话对应）。
- 档位：①配置事实；训练家战斗起式/数据消费按 WP73-A（编辑器）、WP54（资格）引用；实际战斗事件不可验证（③缺口）。

### 5.3 电话联系人（`PBS/phone.txt`，48 行全文）

- **[Default] 通用台词族**：时段 Intro×5＋通用 Intro×5、Body×2、Body1×4、Body2×4、BattleRequest×2（含 \TN／\PN／\TP／\TE／\TM 占位）。
- **具名联系人 2 名**：CAMPER Jeff、PICNICKER Susie——各有 Intro/Body1/Body2/BattleRequest/BattleRemind/End 台词；**与 §5.2 的再战版训练家（Jeff v1、Susie v1）对应**（WP63 电话系统的「再战就绪→版本推进」合同引用）。
- 档位：①配置事实＋②（与再战版的数据对应可静态核对）；注册/来电/再战推进的实际事件不可验证（③缺口）。

## 6. C：特殊玩法与设施候选

### 6.1 Safari Zone（地图 066/067/068）

- 配置链：外围(066，陆遇 6 种)、大门(067)、内区(068，`SafariMap = true`、Environment＝Forest，陆遇 13 种＋水/钓 12 种)——**Safari 会话消费者已批准**（WP53：步数预算/专用球/动作/结束回程的合同；`pbInSafari?`/会话入口存在，`001_SafariZone.rb` 定点）。
- 档位：①＋②；入园事件（收费/接待）不可验证（③缺口——接待事件材料缺失，不据设施存在断言免费或收费）。

### 6.2 捕虫大会（Natural Park 028/029/030）

- 配置链：028 Natural Park 带 **MossRock** 与 **BugContest** 旗标、029/030 入口/会馆带 **BugContestReception** 旗标；028 的 **BugContest 遭遇表**（10 种，含 SCYTHER/PINSIR 各 5）；**BugContest 遭遇类型已注册**（`013_EncounterType.rb:175` 定点）；WP53 捕虫会话（限时/保留/判分/对手）合同引用。
- 档位：①＋②；大会举办事件（接待/计时/评奖）不可验证（③缺口）。

### 6.3 战斗边疆（地图 052–065）

- 设施群配置：Battle Frontier 户外图(052)＋Poké Center(053)＋商店(054)＋**Battle Tower(055)/arena(056)**、**Stadium Cup lobby(057)**、**Battle Palace(058)/arena(059)**、**Battle Arena(060)/arena(061)**、**Battle Factory(062–065)**——arena/corridor 均带 **DisableBoxLink**（WP66-B 合同）。
- **`PBS/battle_facility_lists.txt`（25 行全文）**：默认列表（battle_tower_trainers/pokemon）＋4 杯赛列表——pokecup（单/双打引用 cup_poke_\*）、littlecup（cup_little_\*）、pikacup（cup_pika_\*）、fancycup（单双打均引用 cup_fancy_\*_single 变体；**非 _single 的 cup_fancy_trainers.txt／cup_fancy_pkmn.txt 无引用**，WP76 已登记）。
- 规则/会话消费者：WP54（杯赛资格）、WP55（设施会话）、WP56（Palace/Arena）、WP57（Factory 租赁）、WP76（内容生成器——`pbWriteCup` 调试门）合同引用。
- 档位：①＋②；接待事件与参赛流程不可验证（③缺口）。

### 6.4 小游戏场所与特殊机制图

- **Game Corner（地图 013）**：仅地图元数据登记（无 Outdoor/旗标）——WP68-70 六活动（Duel/Triad/Slot/Voltorb/Lottery/Mining，主区已导入稿）与 WP71（Tile Puzzles）的**静态依赖可用**；**各玩法的脚本入口以事件调用形式存在（"Run with" 注释），demo 事件入口材料缺失**——不据场所登记断言可玩（③缺口）。
- **特殊机制图**：051 Dungeon（`Dungeon = true`＋ScaleWildEncounterLevels——**等级缩放消费者实测**（`004_Overworld_EncounterModifiers.rb:53–62`：遇敌创建时按队伍平衡级 −4＋0–4 重算并重置招式）；049/050/051/072/073 带 **DistortionWorld**——**Giratina 形态消费者实测**（`001_FormHandlers.rb:267–271`：持 Griseous Orb 或本旗标图 → 形态 1）；049/050/051 带 **Magnetic**（进化链见 §6.5）；Berth Island 天气 Storm 50。
- 档位：①＋②；机制的实际触发（进入地图）不可验证（③缺口）。

### 6.5 进化地点旗标链（LocationFlag 求值实测）

- **消费链**：`007_Evolution.rb:490–497`——LocationFlag 进化法在**升级时求值当前地图元数据是否带参数指定的旗标**（地图缺元数据时按无旗标处理）。
- **数据对应**（`PBS/pokemon.txt` 定点）：LEAFEON＝Item LEAFSTONE／**LocationFlag MossRock**（→028 Natural Park）；GLACEON＝Item ICESTONE／**LocationFlag IceRock**（→034 Ice Cave）；MAGNEZONE＝Item THUNDERSTONE／**LocationFlag Magnetic**（→049/050/051）；PROBOPASS／VIKAVOLT＝**LocationFlag Magnetic**；CRABOMINABLE＝**LocationFlag IceRock**。
- 档位：①＋②（数据与求值代码双侧可静态核对）；实际进化事件不可验证（③缺口）。

## 7. D：UI 与作者工作流候选

- **区域地图/飞行**（§4.4）：WP63 消费合同引用；飞行解锁的剧情/开关前提不可验证（③缺口）。
- **电话系统**（§5.3）：WP63 消费合同引用；联系人注册事件不可验证（③缺口）。
- **作者工具链**（**与 demo 玩家事件入口分开**）：调试菜单（WP72）、内容/世界编辑器（WP73-A/B——训练家/地图元数据等可按已批准界面编辑）、动画制作（WP74）、编译转换（WP75——含 `compile_trainer_lists` 与全部 PBS 编译）、设施内容生成器（WP76——`pbWriteCup` 调试门与生成产物反写）——**工具可用入口 ≠ demo 玩家侧事件可达**；工具的 demo 素材前提（地图/系统/tileset/图形）按 WP75/WP76 已登记的缺口保持。

## 8. 跨表引用完整性（实测核对）

| 核对 | 方法 | 结果 |
| --- | --- | --- |
| 连接 → 地图登记 | 19 条连接两端 ID 对 69 节 | 全部命中 |
| 遭遇节 → 地图登记 | 19 节（含 [005,1] 变体）对 69 节 | 全部命中 |
| 训练家类型 → 类型注册 | 15 个使用类型对 `trainer_types.txt` | 全部注册、无缺失 |
| 电话联系人 → 训练家节 | Jeff/Susie 对 trainers.txt | 均有本体＋再战版 v1 |
| 飞行点 → 地图/治疗点 | 5 个飞行点三元组对登记 | 全部指向已登记地图（坐标对应按原文登记） |
| 进化 LocationFlag 链 | 6 条进化数据对求值代码与旗标图 | 双侧命中（§6.5） |
| 杯赛挑战 ID → 设施列表 | battle_facility_lists 的 8 个挑战 ID 对 WP54 杯赛规则 | 规则族已批准（具体 ID 绑定为配置原文） |
| BugContest 遭遇类型 → 类型注册 | `013_EncounterType.rb:175` | 已注册 |
| 未解析引用 | 以上各项 | **0 项**（另有：fancy 杯非 _single 文件无引用——WP76 已登记；map 075 的 Tiall 区与 town_map [1] 对应） |

## 9. 缺口与影响（U01 系，逐项待证）

| 候选链 | 已能证明（档位） | 仍缺证据 | 缺口影响的结论 | 补证时应验证 |
| --- | --- | --- | --- | --- |
| 新游戏→Lappet 起始 | 起始元数据① | 地图事件/Intro 剧情 | 起始流程可达性 | Intro 事件与新游戏初始化 |
| 野外遭遇/钓/碎岩/撞树/雷达 | 遭遇表①、触发合同② | 地图几何与通行 | 各点实际遭遇发生 | 地图事件与通行验证 |
| Brock/火箭队/宿敌/冠军 | 训练家数据①、类型注册② | 放置事件 | 各战可达与顺序 | 事件页与战斗交接 |
| 再战（Jeff/Susie） | 电话文本①、再战版对应② | 联系人注册事件 | 再战就绪/推进 | 电话系统事件 |
| Safari 入园 | 地图/遭遇①、会话合同② | 接待事件 | 收费/步数/动作链 | 接待事件与收费 |
| 捕虫大会 | 旗标/遭遇①、会话合同② | 接待/评奖事件 | 举办与判分 | 大会事件与计时 |
| 边疆四设施＋杯赛 | 地图/列表①、规则会话合同② | 接待事件 | 参赛/租赁/评级链 | 接待事件与挑战登记 |
| 小游戏/拼图 | 场所①、静态规格依赖② | 事件入口 | 可玩性 | Game Corner 等事件页 |
| 寄养/商店/百货 | 场所①、WP27/WP66-C 合同② | 商店库存/寄养收费事件 | 收费差异（E17 继承） | 商店/寄养事件 |
| 进化地点 | 数据①、求值② | 到达地图 | 地点进化实际发生 | 通行与升级验证 |
| 地牢/磁穴/扭曲图 | 参数①、消费者② | 地图生成与进入 | 生成结果/形态切换 | 生成器运行与地图 |
| 飞行 | 飞行点①、WP63 合同② | 解锁前提 | 飞行可用性 | 开关/剧情验证 |

## 10. 可复核性与静态场景

### 10.1 复核方式

E34 九份全文阅读（metadata 33、map_metadata 398、map_connections 40、encounters 311、trainers 118、battle_facility_lists 25、dungeon_parameters 30、town_map 36、phone 48）；跨表引用实测（§8 全部 10 项）；定点消费链（`007_Evolution.rb:485–497`、`001_FormHandlers.rb:267–271`、`004_Overworld_EncounterModifiers.rb:45–70`、`013_EncounterType.rb:175`、`001_SafariZone.rb:63–94`、`002_Challenge_Data.rb:21–33`）；`trainer_types.txt` 类型核对；demo `Data/` 与缺失项逐项存在性复核。未运行游戏/编译器/生成器/反序列化/模拟器；二进制只作身份/存在性证据。

### 10.2 静态场景（M01–M16）

| 编号 | 场景（前提） | 预期（静态推导） |
| --- | --- | --- |
| M01 当前材料状态（存在性核验） | 当前快照 Data 顶层 | 仅 Scripts/、Scripts.rxdata、messages_core.dat；Map\*/MapInfos/CommonEvents/System/Tilesets/Animations、Graphics/Audio/Plugins/Game.ini/Game.rxproj 均不存在（不推出运行回退形态） |
| M02 起始配置（配置事实） | metadata [0]/[1]/[2] | StartMoney 3000、初始存放 POTION、Home＝地图 3＠(7,5) 朝向 8；Red/Leaf 双外观及角色图名已配置（新游戏流程不可验证） |
| M03 地图登记完整性（结构核对） | map_metadata 69 节 | [001]–[075] 缺号 022/032/033/042/043/048；户外图均带 MapPosition；6 个 HealingSpot 按原文登记 |
| M04 连接引用（引用核对） | 19 条连接 | 两端地图 ID 全部命中 69 节（连接存在 ≠ 通行已配置） |
| M05 区域地图（配置事实） | town_map 2 区 | Essen 26 点（5 飞行点＋2 开关点）、Tiall 1 点；飞行三元组全部指向已登记地图 |
| M06 遭遇引用（引用核对） | 19 节遭遇 | 全部命中登记地图；[005,1] 为 Route 1 变体节 |
| M07 遭遇类型矩阵（结构核对） | 13 种类型 | Land/早/晚/Water/Cave/三钓竿/碎岩/撞树两档/雷达/BugContest；051 全表等级 1 幼年种、075 为 _1 形态 |
| M08 地牢参数与缩放（双侧核对） | [cave]/[forest] 参数＋051 Dungeon 旗标 | 参数集已配置；等级缩放消费者实测——遇敌创建按队伍平衡级 −4＋0–4 重算并重置招式（进入地图不可验证） |
| M09 进化地点链（双侧核对） | 6 条 LocationFlag 数据 | 升级时检测当前地图旗标；MossRock→028、IceRock→034、Magnetic→049/050/051（通行与升级不可验证） |
| M10 训练家配置（引用核对） | 20 节训练家 | 15 个使用类型全部注册；Brock 全字段（道具×2/招式/IV 20/Shiny/HEAVYBALL）；Shadow 个体×2 |
| M11 电话联系人（双侧核对） | Jeff/Susie | 联系人台词齐备；trainers.txt 均有本体＋再战版 v1（注册/推进事件不可验证） |
| M12 Safari 配置链 | 066/067/068＋遭遇 | 地图/遭遇已配置；SafariMap 旗标与 WP53 会话消费者存在（接待/收费事件缺失，不断言免费或收费） |
| M13 捕虫大会配置链 | 028/029/030 旗标＋BugContest 表 | MossRock/BugContest/BugContestReception 旗标已配置；BugContest 类型已注册；WP53 会话合同引用（举办事件缺失） |
| M14 边疆配置链 | 052–065＋battle_facility_lists | 设施地图群已配置；默认＋4 杯赛列表引用关系明确（fancy 非 _single 无引用）；接待/参赛事件缺失 |
| M15 小游戏/拼图 | Game Corner 013＋WP68-70/71 依赖 | 场所登记存在；玩法入口以事件调用形式存在、demo 事件入口材料缺失——不据场所断言可玩 |
| M16 缺口影响（综合） | §9 全部 11 条候选链 | 配置/候选各档分别计数；事件页选择、开关变量门、收费/授奖、跨图可达链一律保持待证（不写成已演示或不存在） |

## 11. 证据与来源（traceability）

**E34 全文（9 份，1,039 行）**：`PBS/metadata.txt`（33）、`PBS/map_metadata.txt`（398）、`PBS/map_connections.txt`（40）、`PBS/encounters.txt`（311）、`PBS/trainers.txt`（118）、`PBS/battle_facility_lists.txt`（25）、`PBS/dungeon_parameters.txt`（30）、`PBS/town_map.txt`（36）、`PBS/phone.txt`（48）。

**定点（同 HEAD）**：`010_Data/001_Hardcoded data/007_Evolution.rb`（485–497 LocationFlag 求值；500–503 Region 邻近）；`010_Data/001_Hardcoded data/013_EncounterType.rb`（175 BugContest 注册）；`014_Pokemon/001_Pokemon-related/001_FormHandlers.rb`（267–271 Giratina/DistortionWorld）；`012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb`（45–70 等级缩放）；`018_Alternate battle modes/001_SafariZone.rb`（63–94 会话入口）；`018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb`（21–33 列表查询）；`PBS/pokemon.txt`（2177–2178、3536–3539、7917、19067、19117 进化数据）；`PBS/trainer_types.txt`（类型注册核对）；demo `Data/` 与缺失项存在性复核。WP01/WP04/WP11/WP12/WP13/WP15/WP17/WP36/WP53/WP54/WP55/WP56/WP57/WP60/WP61/WP63/WP64/WP65/WP66-A/B/C/WP67-A/B/WP68/WP69/WP70/WP71/WP72/WP73-A/WP73-B/WP74/WP75/WP76 已通过合同按引用继承（当前磁盘身份见登记，未冒充本轮新阅读）。

## 12. 未决问题

1. **U01 保持开放**：完整 demo 的地图/公共事件/资源获得前，全部事件链（收费、授予、奖励、可达）不可验证；补证须获得完整工程材料并在独立分析副本检查事件（WP01 §5 继承）。
2. 各候选链的接待/注册/放置事件（Safari、大会、边疆、小游戏、电话、寄养/商店）均未证——不据配置/场所断言可达或收费。
3. map 009 的 HealingSpot 指向地图 8 与 Cedolan 飞行点（地图 7 城内）的关系：按配置原文登记，语义待事件/地图材料佐证。
4. Tiall 区（map 075＋town_map [1]）的接入方式（无连接条目）与 _1 形态遭遇的实际进入路径：待证。
5. Berth/Faraday 开关点（51/52）的消费者：未见配置/脚本证据，留待事件材料。
6. 全部运行表现（遭遇发生、战斗结果、玩法结果、生成结果）未验证，留运行验证阶段。

## 13. 状态与后续

- 状态：**ReviewPending（A～D 具名静态范围，首版待统一 review）**；未验证子范围＝全部事件证据链与运行表现（§9）；**F18-06 本轮可交付范围＝配置/候选/缺口登记（WP77 具名子范围），不把整包或 F18-06/F18-07 的全部范围标完成**。
- 本包交付：本主稿＋`review/wp77-delivery-2026-10-03/`（首版材料）。
- 后续：WP77 有界审查；完整 demo 材料缺失时后续阶段采用的限定范围由 WP77 审查明确；不自行宣布全项目完成或直接进入 WP78/79/80。

## 修订记录

- 2026-10-03 **首版**（WP77，D18 第六包）：E34 九份全文（1,039 行）＋跨表引用 10 项实测＋定点消费链；场景 M01–M16 建立；附表与缺口表见交付目录。登记 ReviewPending（待统一 review）。
