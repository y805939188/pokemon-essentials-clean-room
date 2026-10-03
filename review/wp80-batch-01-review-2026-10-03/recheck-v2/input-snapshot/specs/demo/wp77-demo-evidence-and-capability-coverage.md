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

### 4.1 起始与玩家元数据（`PBS/metadata.txt`，33 行全文；R01 修订——四类事实分开）

- **新游戏资源**：StartMoney＝3000、StartItemStorage＝POTION（PC 初始存放）；野生/训练家战斗与胜利 BGM、Surf/Bicycle BGM 已配置——属新游戏初始化消费范围（WP24/WP65 合同引用）。
- **家地点回退（Home）**：Home＝3,7,5,8（地图 3＝Player's house 内点 (7,5)、朝向 8）——**它是失败回程/Teleport 等的家地点回退**（编辑器属性明示「未访问中心时失败后的去处」；WP61 已批准合同中角色家优先于全局家），**不是新游戏起始位置的证据**。
- **系统起始位置**：新游戏起始地图/坐标来自系统数据（`Game.initialize`/`start_new` 读取 `System.rxdata` 的 start_map_id/start_x/start_y——**该文件当前缺失**，`016_Metadata.rb:21–43`、`001_StartGame.rb:7–16, 39–58` 定点）——**不能由家地点或地图注释推定新游戏从 Lappet 或玩家家开始**（③待证）。
- **[1] Red／[2] Leaf**：两位玩家外观定义（TrainerType `POKEMONTRAINER_Red`／`POKEMONTRAINER_Leaf`；走/跑/骑行/冲浪/潜水/垂钓角色图名已配置）。
- 档位：①配置事实（各字段各自成立）；**Home 已知、系统起始位置未知**——对照登记，不把缺失证据写成已配置起点。

### 4.2 地图登记（`PBS/map_metadata.txt`，69 节，[001]–[075]，缺号 022／032／033／042／043／048）

- **户外图**：Lappet Town(002)、Route 1(005)、Cedolan City(007)、Route 2(021)、Lerucean Town(023)、Natural Park(028)、Route 3(031)、Ingido Plateau(035)、Route 4(039/040)、**Route 5(041)**、**Route 6(044/045——045 为 Route 6 自行车道，源注释与 Name 均属 Route 6，N01 修订）**、Route 7(047)、Battle Frontier(052)、Safari Zone 外(066)/内(068)、Route 8(069)、Berth Island(072)、Faraday Island(073)、Tiall Region(075)——均带 MapPosition（区域坐标，与 §4.4 区域地图点对应）。
- **室内/设施图**：玩家家(003)、实验室(004)、Kurt 家(006)、Daisy 家(008)、**注释标为 Poké Center 的条目 3 个**(009 Cedolan、024 Lerucean、053 边疆——注释性场所标题与 Name 字段分开，R08 修订)、商店(025/054)、研究所(011)、公寓(012)、Game Corner(013)、百货 1–5F＋天台＋电梯(014–020)、Cedolan Gym(010)、球迷俱乐部(026)、寄养屋(027)、公园入口/会馆(029/030)、联盟入口/房间 1/名人堂(036/037/038)、自行车道闸口×2(046/074)、岩洞 1F/B1F(049/050)、Dungeon(051)、商店(054)、Battle Tower(055)/arena(056)、Stadium Cup lobby(057)、Battle Palace(058)/arena(059)、Battle Arena(060)/arena(061)、Battle Factory(062)/intro corridor(063)/arena(064)/corridor(065)、Safari 大门(067)、水下(070)、码头(071)。
- **治疗点（HealingSpot 字段，共 6 处）**：玩家家(003：地图 2＠(8,8))、Cedolan PC(009：地图 8＠(17,11))、Lerucean PC(024：地图 23＠(11,15))、联盟入口(036：地图 35＠(17,7))、边疆 PC(053：地图 52＠(17,14))、Battle Tower(055：地图 52＠(30,10))——**按配置原样登记**（009 行指向地图 8，为配置原文，不作语义修正）。**字段出现次数（6）与注释标为 Poké Center 的条目数（3）是两个单位**；缺事件/MapInfos 时不推断完整游戏共有多少治疗设施（R08）。
- **天气**：Route 2(021)＝Rain 100、Route 7(047)＝Rain 0、Berth Island(072)＝Storm 50。
- **特殊旗标/图**（消费链见 §6.2）：MossRock(028)、IceRock(034)、Magnetic(049/050/051)、DistortionWorld(049/050/051/072/073)、ScaleWildEncounterLevels(051)、BugContest(028)、BugContestReception(029/030)、DisableBoxLink(010/037/038/056/059/061/063/064/065)、DarkMap(050)、Dungeon(051)、SafariMap(068)、DiveMap 70(069)、Environment 各值（Cave/Rock/Forest/Underwater）、Bicycle/BicycleAlways 各行、MapSize 各行。
- 档位：①配置事实。几何与可达性不可验证（③缺口）；元数据消费合同按 WP11/WP12/WP13/WP61/WP66-B 引用。

### 4.3 地图连接（`PBS/map_connections.txt`，19 条全文；R02 修订）

19 条配置记录全部命中已登记地图（§6.1 实测）。规范化连接表（无向边，逐条不重不漏）：(41,40)、(41,45)、(44,5)、(66,5)、(7,5)、(2,5)、(7,44)、(2,66)、(69,66)、(35,39)、(7,23)、(31,23)、(21,23)、(47,7)、(21,7)、(31,35)、**(69,2)**、(47,52)、(21,47)——含 **Route 8(69)↔Lappet Town(2) 直连**（源表第 36 行）。计数口径：**配置记录数＝19（无向边同数）**；从多个节点重复列举的邻接项数是另一单位，不混用。方向/偏移按来源定位；**配置连接不证明实际通行或几何**（③缺口）。

### 4.4 区域地图与飞行点（`PBS/town_map.txt`，2 区 27 点全文；R03/R04 修订）

- **[0] Essen 区**（mapRegion0.png）：**26 条点记录，按互斥类别分组为 18 条普通点＋6 条带飞行目的地记录＋2 条开关点**。**6 条飞行记录对应 5 个不同目的地**（Cedolan 两条记录共用同一目的地）：Lappet Town→地图 2＠(8,8)、Cedolan（(13,10) 与 (14,10) 两条，含 Dept. Store 标注）→地图 7＠(47,11)、Lerucean Town→地图 23＠(11,15)、Ingido Plateau→地图 35＠(17,7)、Battle Frontier→地图 52＠(17,14)。普通点 18 条（Route 1/2/3/4/5/6/7 各道路点、Natural Park、Rock Cave、Safari Zone、Route 8 Diving area、Route 3 Ice Cave、Cycle Road×3——按记录逐项可复算；**两个 Cedolan 点均带飞行目的地、只归飞行记录组，普通组不含任何 Cedolan 记录**——R03 修订）。
- **飞行目的地与治疗点匹配（R03）**：与 HealingSpot **完全匹配的是 4 个**——2＠(8,8)（玩家家）、23＠(11,15)（Lerucean PC）、35＠(17,7)（联盟入口）、52＠(17,14)（边疆 PC）；**Cedolan 飞行目的地 7＠(47,11) ≠ map 009 的 HealingSpot 8＠(17,11)**（配置原文，不作纠正或运行推断）；map 055 的 HealingSpot 52＠(30,10)（Battle Tower）**不是飞行目的地**。
- **[1] Tiall 区**（mapRegion1.png）：1 条点记录（Here）——总数 27 保持。
- **开关点的读取消费者已存在（R04）**：Berth Island 开关 51、Faraday Island 开关 52——**普通区域地图的地点名/详情/飞行目的地查询都会读取点记录的开关字段**：开关字段为真且（墙图模式、或开关编号非正、或该开关未置位）时，对应信息/目的地被隐藏（`016_UI/009_UI_RegionMap.rb:183–191, 211–230` 定点）；**墙图（wall map）等入口另有隐藏条件**，按 WP63 已批准合同引用。**继续待证的是：哪个剧情/事件把 51 或 52 置位、玩家何时能见到这些点及实际访问路径**（③）——不是读取消费者是否存在。
- 档位：①配置事实＋②（飞行—治疗点匹配与开关读取消费可静态核对）；飞行解锁（开关/剧情前提）与实际访问不可验证（③缺口）。

### 4.5 地牢参数（`PBS/dungeon_parameters.txt`，2 套全文；R05 修订——三件事分开）

- **地图启用生成**：map 051 的 `Dungeon = true` 只**启用**生成路径（`on_game_map_setup` 对带本标记的地图走随机地牢生成——`008_Overworld_RandomDungeons.rb:1063–1074` 定点）——**该字段不直接绑定任何参数集**。
- **参数集存在**：[cave] 与 [forest] 两套已配置（内容见下）。
- **具体选中哪一集**：由全局 `dungeon_area`（**默认 `:none`**）与 `dungeon_version`（**默认 0**）决定——查找**先 `区域_版本` 键、后 `区域` 键，均未中则使用默认参数实例**（`020_DungeonParameters.rb:58–66` 定点；WP14 已批准合同）。**独立对照：区域 none/版本 0 → 默认参数（5×5 节点）**——**不是实际 demo 运行观察**；**区域 cave/版本 0 才能选到本包的 5×4 样本**。**当前地图元数据没有证明 demo 把区域写为 cave 或 forest**；区域/版本赋值事件与实际地图 tileset 供给（`DungeonTileset` 查找依赖 tileset 数据）**均缺证据**（③待证）。
- **两套参数内容与差异**：[cave]＝5×4 节点、单元 10×10、房间 5–9、走廊宽 2、**ShiftCorridors＝true（通道随机偏移开启）**、NodeLayout/RoomLayout＝full、RoomChance 70、ExtraConnections 2、FloorPatches 2,50,25、FloorDecorations/VoidDecorations 50,200；[forest]＝5×4 节点、房间 4–8、FloorPatches 3,75,25，**未写 ShiftCorridors（省略＝未开启）**——**两集差异含通道随机偏移的开/关**，不只房间范围与地板斑块。
- 档位：①配置事实＋②（选择合同与默认回退可静态核对）；实际生成结果与区域/版本赋值不可验证（③缺口）。

## 5. B：生物与玩家流程候选

### 5.1 遭遇配置（`PBS/encounters.txt`，19 节全文）

- **节—图对应**（§6.1 实测全部命中 §4.2 登记）：002 Lappet Town、005 Route 1、**[005,1] Route 1 变体**、021 Route 2、028 Natural Park、031 Route 3、034 Ice Cave、039 Route 4、041 Route 5、044 Route 6、047 Route 7、049/050 Rock Cave、051 Dungeon、066 Safari 外、068 Safari、069 Route 8、070 水下、075 Tiall Region。
- **遭遇类型矩阵**（13 种实测）：Land（陆／晨昏时段）、LandMorning、LandNight、Water（水面）、Cave（洞穴）、OldRod／GoodRod／SuperRod（三级钓竿）、RockSmash（碎岩）、HeadbuttLow／HeadbuttHigh（撞树两档）、PokeRadar（雷达）、**BugContest（捕虫大会专用——已在遭遇类型注册表注册，§6.3）**。
- **内容形态（R07 修订——槽位记录数与不同标识数分开）**：每条为「权重, 物种(_形态), 等级(或区间)」。**051 Dungeon 全表为等级 1 的幼年种**（配合 ScaleWildEncounterLevels 旗标——§6.4）；**075 Tiall 共 8 条：6 条带 _1 形态后缀**（GEODUDE_1／RATTATA_1／DIGLETT_1／MEOWTH_1／SANDSHREW_1／VULPIX_1）**＋2 条无后缀**（CUBONE／PIKACHU）——各自权重与等级范围保持原表。**068 Safari 内区：陆遇 12 条／11 个不同物种**（VENONAT 重复两槽）；**水/钓 14 条／12 个不同物种**——**重复者为 MAGIKARP 三条（OldRod 两条、GoodRod 一条）；FEEBAS 仅 GoodRod 一条**——**不合并同物种重复槽位或权重**。**数量仅限 `PBS/` 根目录当前 encounters 数据**；**同名 Gen 5–8 backup/encounters.txt 属可选材料**（存在性登记：Gen 5 与 Gen 6 备份内容相同、Gen 7 与 Gen 8 备份相同且与当前根表一致——本轮仅身份核验、**未全文阅读备份**，不把备份当当前默认；默认根集与备份的选择边界按 WP01/WP02 已登记发现机制）。
- 档位：①配置事实；遭遇触发/时段/工具合同按 WP36/WP60/WP12 引用；具体遭遇发生不可验证（③缺口）。

### 5.2 训练家配置（`PBS/trainers.txt`，20 节全文）

- **类型核对**（§6.4 实测）：15 个使用类型（BEAUTY、CAMPER、CHAMPION、COOLCOUPLE、FISHERMAN、HIKER、LASS、LEADER_Brock、PICNICKER、POKEMONTRAINER_May、RIVAL1、SWIMMER2_F、TEAMROCKET_F、TEAMROCKET_M、YOUNGSTER）**全部在 `PBS/trainer_types.txt` 注册**。
- **全字段样例**：LEADER Brock——道具 FULLRESTORE×2；GEODUDE(12) 指定招式/特性位/性别/IV 全 20；ONIX(14) 昵称 Rocky、指定招式、SITRUSBERRY、**Shiny、HEAVYBALL**。
- **Shadow 个体×2**：TEAMROCKET_M Grunt(1) 的 WEEPINBELL(21)、TEAMROCKET_F Grunt(1) 的 ELECTABUZZ(20)（WP23 净化室/Shadow 合同引用）。
- **版本系列**：RIVAL1 Blue 三变体（初始伙伴差异）、CHAMPION Blue（三只 63 级各持 SITRUSBERRY）、CAMPER Jeff 与 PICNICKER Susie 的**再战版 v1**（等级提升队伍——与 §5.3 电话对应）。
- 档位：①配置事实；训练家战斗起式/数据消费按 WP73-A（编辑器）、WP54（资格）引用；实际战斗事件不可验证（③缺口）。

### 5.3 电话联系人（`PBS/phone.txt`，48 行全文）

- **[Default] 通用台词族**：**通用 Intro 5 条**＋**时段 Intro 3 条**（IntroMorning／IntroAfternoon／IntroEvening 各 1 条——两组分开计数，R08 修订）、Body×2、Body1×4、Body2×4、BattleRequest×2（含 \TN／\PN／\TP／\TE／\TM 占位）。
- **具名联系人 2 名**：CAMPER Jeff、PICNICKER Susie——各有 Intro/Body1/Body2/BattleRequest/BattleRemind/End 台词；**与 §5.2 的再战版训练家（Jeff v1、Susie v1）对应**（WP63 电话系统的「再战就绪→版本推进」合同引用）。
- 档位：①配置事实＋②（与再战版的数据对应可静态核对）；注册/来电/再战推进的实际事件不可验证（③缺口）。

## 6. C：特殊玩法与设施候选

### 6.1 Safari Zone（地图 066/067/068）

- 配置链：外围(066，陆遇 6 条)、大门(067)、内区(068，`SafariMap = true`、Environment＝Forest，**陆遇 12 条／11 种＋水/钓 14 条／12 种**——槽位记录与不同物种分开，R07)——**Safari 会话消费者已批准**（WP53：步数预算/专用球/动作/结束回程的合同；`pbInSafari?`/会话入口存在，`001_SafariZone.rb` 定点）。
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
- **特殊机制图**：051 Dungeon（`Dungeon = true`＋ScaleWildEncounterLevels——**等级缩放消费者实测**（`004_Overworld_EncounterModifiers.rb:51–60`：遇敌创建时先取**偏移值＝队伍平衡级 −4＋0–4 随机量**，**再夹到 [1, 成长系统最大等级]**，随后赋等级、重算能力并重置招式——**中间量不是最终等级**；R06 补上下界——偏移 ≤0 → 夹到 1、偏移 > 上限 → 夹到上限）；049/050/051/072/073 带 **DistortionWorld**——**Giratina 形态消费者实测**（`001_FormHandlers.rb:267–271`：持 Griseous Orb 或本旗标图 → 形态 1）；049/050/051 带 **Magnetic**（进化链见 §6.5）；Berth Island 天气 Storm 50。
- 档位：①＋②；机制的实际触发（进入地图）不可验证（③缺口）。

### 6.5 进化地点旗标链（LocationFlag 求值实测）

- **消费链**：`007_Evolution.rb:490–497`——LocationFlag 进化法在**升级时求值当前地图元数据是否带参数指定的旗标**（地图缺元数据时按无旗标处理）。
- **数据对应**（`PBS/pokemon.txt` 定点）：LEAFEON＝Item LEAFSTONE／**LocationFlag MossRock**（→028 Natural Park）；GLACEON＝Item ICESTONE／**LocationFlag IceRock**（→034 Ice Cave）；MAGNEZONE＝Item THUNDERSTONE／**LocationFlag Magnetic**（→049/050/051）；PROBOPASS／VIKAVOLT＝**LocationFlag Magnetic**；CRABOMINABLE＝**LocationFlag IceRock**。
- 档位：①＋②（数据与求值代码双侧可静态核对）；实际进化事件不可验证（③缺口）。

## 7. D：UI 与作者工作流候选

- **区域地图/飞行**（§4.4）：WP63 消费合同引用；飞行解锁的剧情/开关前提不可验证（③缺口）。
- **电话系统**（§5.3）：WP63 消费合同引用；联系人注册事件不可验证（③缺口）。
- **作者工具链**（**与 demo 玩家事件入口分开**）：调试菜单（WP72）、内容/世界编辑器（WP73-A/B——训练家/地图元数据等可按已批准界面编辑）、动画制作（WP74）、编译转换（WP75——含 `compile_trainer_lists` 与全部 PBS 编译）、设施内容生成器（WP76——`pbWriteCup` 调试门与生成产物反写）——**工具可用入口 ≠ demo 玩家侧事件可达**；工具的 demo 素材前提（地图/系统/tileset/图形）按 WP75/WP76 已登记的缺口保持。

## 8. 跨表引用完整性（实测核对；R03/R09 修订——8 项具名检查＋1 项汇总）

| # | 核对 | 方法 | 结果 |
| --- | --- | --- | --- |
| C1 | 连接 → 地图登记 | 19 条连接两端 ID 对 69 节 | 全部命中（规范化连接表见 §4.3，含 69↔2） |
| C2 | 遭遇节 → 地图登记 | 19 节（含 [005,1] 变体）对 69 节 | 全部命中 |
| C3 | 训练家类型 → 类型注册 | 15 个使用类型对 `trainer_types.txt` | 全部注册、无缺失 |
| C4 | 电话联系人 → 训练家节 | Jeff/Susie 对 trainers.txt | 均有本体＋再战版 v1 |
| C5 | 飞行记录 → 目的地/治疗点 | 6 条飞行记录、5 个不同目的地对登记 | 全部指向已登记地图；**与 HealingSpot 完全匹配 4 个**（2＠(8,8)、23＠(11,15)、35＠(17,7)、52＠(17,14)）；Cedolan 7＠(47,11) ≠ map 009 的 8＠(17,11)（原文登记） |
| C6 | 进化 LocationFlag 链 | 6 条进化数据对求值代码与旗标图 | 双侧命中（§6.5） |
| C7 | 杯赛挑战 ID → 设施列表 | battle_facility_lists 的 8 个挑战 ID 对 WP54 杯赛规则 | 规则族已批准（具体 ID 绑定为配置原文） |
| C8 | BugContest 遭遇类型 → 类型注册 | `013_EncounterType.rb:175` | 已注册 |
| 汇总 | 未解析引用 | 以上 C1–C8 实际检查过的引用集合 | **0 项**（仅限该集合；另有：fancy 杯非 _single 文件无引用——WP76 已登记；map 075 的 Tiall 区与 town_map [1] 对应） |

## 9. 缺口与影响（U01 系，逐项待证；R01/R09 修订——12 条链统一行 ID）

| # | 候选链 | 已能证明（档位） | 仍缺证据 | 缺口影响的结论 | 补证时应验证 |
| --- | --- | --- | --- | --- | --- |
| G01 | 新游戏→起始位置 | 初始金钱/PC 存放①、Home 回程①、外观① | **System.rxdata 起始地图/坐标**、Intro 剧情 | **系统起始位置与新游戏流程**（Home 已知但起始位置未知） | 系统数据与 Intro 事件、新游戏初始化 |
| G02 | 野外遭遇/钓/碎岩/撞树/雷达 | 遭遇表①、触发合同② | 地图几何与通行 | 各点实际遭遇发生 | 地图事件与通行验证 |
| G03 | Brock/火箭队/宿敌/冠军 | 训练家数据①、类型注册② | 放置事件 | 各战可达与顺序 | 事件页与战斗交接 |
| G04 | 再战（Jeff/Susie） | 电话文本①、再战版对应② | 联系人注册事件 | 再战就绪/推进 | 电话系统事件 |
| G05 | Safari 入园 | 地图/遭遇①、会话合同② | 接待事件 | 收费/步数/动作链 | 接待事件与收费 |
| G06 | 捕虫大会 | 旗标/遭遇①、会话合同② | 接待/评奖事件 | 举办与判分 | 大会事件与计时 |
| G07 | 边疆四设施＋杯赛 | 地图/列表①、规则会话合同② | 接待事件 | 参赛/租赁/评级链 | 接待事件与挑战登记 |
| G08 | 小游戏/拼图 | 场所①、静态规格依赖② | 事件入口 | 可玩性 | Game Corner 等事件页 |
| G09 | 寄养/商店/百货 | 场所①、WP27/WP66-C 合同② | 商店库存/寄养收费事件 | 收费差异（E17 继承） | 商店/寄养事件 |
| G10 | 进化地点 | 数据①、求值② | 到达地图 | 地点进化实际发生 | 通行与升级验证 |
| G11 | 地牢/磁穴/扭曲图 | 参数①、消费者②（含夹限完整规则） | 地图生成与进入；**区域/版本赋值事件与 tileset 供给** | 生成结果/形态切换/参数集选择 | 生成器运行、区域/版本写入、地图进入 |
| G12 | 飞行与岛屿开关 | 飞行点①、匹配 4 个②、开关读取消费② | **开关 51/52 的置位/解锁事件**与实际访问路径 | 飞行可用性与两点可见性 | 开关写入事件、解锁剧情与访问验证 |

缺口表（gap-register）与本表采用**相同的 12 组**（v2 起一致）；①/② 计数按覆盖附表档位列逐行复算（①15 行、②11 行，R09）。

## 10. 可复核性与静态场景

### 10.1 复核方式

E34 九份全文阅读（metadata 33、map_metadata 398、map_connections 40、encounters 311、trainers 118、battle_facility_lists 25、dungeon_parameters 30、town_map 36、phone 48）；跨表引用实测（§8 具名 C1–C8＋汇总）；定点消费链（`007_Evolution.rb:485–503`、`001_FormHandlers.rb:267–271`、`004_Overworld_EncounterModifiers.rb:51–60`、`013_EncounterType.rb:175`、`001_SafariZone.rb:63–94`、`002_Challenge_Data.rb:21–33`）；`trainer_types.txt` 类型核对；demo `Data/` 与缺失项逐项存在性复核。**v2 补读（R01～R06 来源）**：`016_Metadata.rb:21–43`（Home 编辑器属性）、`001_StartGame.rb:7–16, 39–58`（系统起始位置读取）、`016_UI/009_UI_RegionMap.rb:183–191, 211–230`（开关点读取消费）、`020_DungeonParameters.rb:58–95`（参数查找回退与默认值）、`008_Overworld_RandomDungeons.rb:1047–1074`（区域/版本默认与生成入口）；Gen 5–8 backup/encounters.txt 存在性核验（仅身份，未全文阅读）；WP61（Home 回程合同行）与 WP14（地牢参数合同行）已批准文本定点复核。未运行游戏/编译器/生成器/反序列化/模拟器；二进制只作身份/存在性证据。

### 10.2 静态场景（M01–M16）

| 编号 | 场景（前提） | 预期（静态推导） |
| --- | --- | --- |
| M01 当前材料状态（存在性核验） | 当前快照 Data 顶层 | 仅 Scripts/、Scripts.rxdata、messages_core.dat；Map\*/MapInfos/CommonEvents/System/Tilesets/Animations、Graphics/Audio/Plugins/Game.ini/Game.rxproj 均不存在（不推出运行回退形态） |
| M02 起始配置（配置事实；R01 修订） | metadata [0]/[1]/[2]；系统数据缺失 | 初始金钱 3000、PC 初始存放 POTION 已配置；**Home＝地图 3＠(7,5) 朝向 8 为失败回程/Teleport 家地点回退（非新游戏起点证据）**；**系统起始地图/坐标来自缺失的 System.rxdata——Home 已知、系统起始位置未知**；Red/Leaf 双外观及角色图名已配置（新游戏流程不可验证） |
| M03 地图登记完整性（结构核对） | map_metadata 69 节 | [001]–[075] 缺号 022/032/033/042/043/048；户外图均带 MapPosition；HealingSpot 字段 6 处按原文登记（字段次数与注释 Poké Center 条目 3 个分开） |
| M04 连接引用（引用核对；R02 修订） | 19 条配置记录 | 两端地图 ID 全部命中 69 节；规范化连接表逐项不重不漏——**含 Route 8(69)↔Lappet(2) 直连**（配置记录数＝无向边数＝19，邻接重复列举是另一单位；通行/几何待证） |
| M05 区域地图（配置事实；R03 修订） | town_map 2 区 | Essen 26 条＝**18 普通＋6 飞行记录＋2 开关点**；6 条飞行记录对 **5 个不同目的地**（Cedolan 两条共用）；**飞行—治疗点完全匹配 4 个**（2＠(8,8)、23＠(11,15)、35＠(17,7)、52＠(17,14)）；**Cedolan 7＠(47,11) ≠ map 009 的 8＠(17,11)**（原文）；Tiall 1 条、总数 27 |
| M06 遭遇引用（引用核对） | 19 节遭遇 | 全部命中登记地图；[005,1] 为 Route 1 变体节 |
| M07 遭遇类型矩阵（结构核对；R07 修订） | 13 种类型 | Land/早/晚/Water/Cave/三钓竿/碎岩/撞树两档/雷达/BugContest；051 全表等级 1 幼年种；**075 为 6 条 _1 后缀＋2 条无后缀（CUBONE/PIKACHU）**；**Safari 内区陆遇 12 条/11 种、水/钓 14 条/12 种**（槽位与不同物种分开）；数量限根目录当前表，Gen 5–8 备份仅身份登记 |
| M08 地牢参数与缩放（双侧核对；R05/R06 修订） | [cave]/[forest] 参数＋051 Dungeon 旗标 | 参数集已配置（**cave 通道随机偏移开启、forest 省略未开启**）；**051 标记只启用生成——区域/版本默认 none/0 走默认参数（5×5，非本运行观察）；区域 cave/0 才选到 5×4 样本**；赋值事件与 tileset 供给待证；**等级缩放完整规则：偏移＝平衡级 −4＋0–4，再夹 [1, 最大等级]，赋级、重算、重置招式**（偏移 ≤0 → 1、偏移 > 上限 → 上限；进入地图不可验证） |
| M09 进化地点链（双侧核对） | 6 条 LocationFlag 数据 | 升级时检测当前地图旗标；MossRock→028、IceRock→034、Magnetic→049/050/051（通行与升级不可验证） |
| M10 训练家配置（引用核对） | 20 节训练家 | 15 个使用类型全部注册；Brock 全字段（道具×2/招式/IV 20/Shiny/HEAVYBALL）；Shadow 个体×2 |
| M11 电话联系人（双侧核对；R08 修订） | Jeff/Susie；Default 台词族 | 联系人台词齐备；trainers.txt 均有本体＋再战版 v1；**Default 通用 Intro 5 条、时段 Intro 3 条（早/午/晚各 1）两组分开**（具名联系人的时段台词不并入 Default 计数）——注册/推进事件不可验证 |
| M12 Safari 配置链（R07 修订） | 066/067/068＋遭遇 | 地图/遭遇已配置——**内区陆遇 12 条／11 种、水/钓 14 条／12 种**（VENONAT 等重复槽位不合并）；SafariMap 旗标与 WP53 会话消费者存在（接待/收费事件缺失，不断言免费或收费） |
| M13 捕虫大会配置链 | 028/029/030 旗标＋BugContest 表 | MossRock/BugContest/BugContestReception 旗标已配置；BugContest 类型已注册；WP53 会话合同引用（举办事件缺失） |
| M14 边疆配置链 | 052–065＋battle_facility_lists | 设施地图群已配置；默认＋4 杯赛列表引用关系明确（fancy 非 _single 无引用）；接待/参赛事件缺失 |
| M15 小游戏/拼图 | Game Corner 013＋WP68-70/71 依赖 | 场所登记存在；玩法入口以事件调用形式存在、demo 事件入口材料缺失——不据场所断言可玩 |
| M16 缺口影响（综合；R09 修订） | §9 全部 12 条候选链（G01–G12 统一行 ID，与缺口表同组） | 配置/候选各档分别计数（①15 行、②11 行——按覆盖附表档位列复算）；**③已证事件链与④运行观察继续为 0**；事件页选择、开关变量门、收费/授奖、跨图可达链一律保持待证（不写成已演示或不存在；**不为凑数字提升证据档位**） |

## 11. 证据与来源（traceability）

**E34 全文（9 份，1,039 行）**：`PBS/metadata.txt`（33）、`PBS/map_metadata.txt`（398）、`PBS/map_connections.txt`（40）、`PBS/encounters.txt`（311）、`PBS/trainers.txt`（118）、`PBS/battle_facility_lists.txt`（25）、`PBS/dungeon_parameters.txt`（30）、`PBS/town_map.txt`（36）、`PBS/phone.txt`（48）。

**定点（同 HEAD）**：`010_Data/001_Hardcoded data/007_Evolution.rb`（485–503 LocationFlag 求值与邻近）；`010_Data/001_Hardcoded data/013_EncounterType.rb`（175 BugContest 注册）；`010_Data/002_PBS data/016_Metadata.rb`（21–43 Home 属性定义）；`010_Data/002_PBS data/020_DungeonParameters.rb`（58–95 查找回退与默认值）；`014_Pokemon/001_Pokemon-related/001_FormHandlers.rb`（267–271 Giratina/DistortionWorld）；`012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb`（51–60 等级缩放含夹限）；`012_Overworld/008_Overworld_RandomDungeons.rb`（1047–1074 区域/版本默认与生成入口）；`016_UI/009_UI_RegionMap.rb`（183–191, 211–230 开关点读取消费）；`003_Game processing/001_StartGame.rb`（7–16, 39–58 系统起始位置）；`018_Alternate battle modes/001_SafariZone.rb`（63–94 会话入口）；`018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb`（21–33 列表查询）；`PBS/pokemon.txt`（2177–2178、3536–3539、7917、19067、19117 进化数据）；`PBS/trainer_types.txt`（类型注册核对）；`PBS/Gen 5 backup/encounters.txt`、`Gen 6 backup/encounters.txt`、`Gen 7 backup/encounters.txt`、`Gen 8 backup/encounters.txt`（存在性核验——仅身份，未全文阅读）；demo `Data/` 与缺失项存在性复核；`specs/pokemon-rules/wp61-field-passive-effects-and-blackout.md`（Home 回程合同行）、`specs/overworld/wp14-random-dungeons.md`（地牢参数合同行）已批准文本定点复核。WP01/WP04/WP11/WP12/WP13/WP15/WP17/WP36/WP53/WP54/WP55/WP56/WP57/WP60/WP61/WP63/WP64/WP65/WP66-A/B/C/WP67-A/B/WP68/WP69/WP70/WP71/WP72/WP73-A/WP73-B/WP74/WP75/WP76 已通过合同按引用继承（当前磁盘身份见登记，未冒充本轮新阅读）。

## 12. 未决问题

1. **U01 保持开放**：完整 demo 的地图/公共事件/资源获得前，全部事件链（收费、授予、奖励、可达）不可验证；补证须获得完整工程材料并在独立分析副本检查事件（WP01 §5 继承）。
2. 各候选链的接待/注册/放置事件（Safari、大会、边疆、小游戏、电话、寄养/商店）均未证——不据配置/场所断言可达或收费。
3. map 009 的 HealingSpot 指向地图 8 与 Cedolan 飞行点（地图 7 城内）的关系：按配置原文登记，语义待事件/地图材料佐证。
4. Tiall 区（map 075＋town_map [1]）的接入方式（无连接条目）与 _1 形态遭遇的实际进入路径：待证。
5. **岛屿开关点（51/52）的读取消费者已存在**（区域地图查询在开关未置位时隐藏对应信息/目的地——普通图与墙图入口条件分开，§4.4）；**继续待证的是开关的置位/解锁事件与实际访问路径**，不是读取消费者是否存在（R04 修订）。
6. 全部运行表现（遭遇发生、战斗结果、玩法结果、生成结果）未验证，留运行验证阶段。

## 13. 状态与后续

- 状态：**ReviewPending（A～D 具名静态范围，首版经首审修订 v3，待短复审）**；未验证子范围＝全部事件证据链与运行表现（§9）；**F18-06 本轮可交付范围＝配置/候选/缺口登记（WP77 具名子范围），不把整包或 F18-06/F18-07 的全部范围标完成**。
- 本包交付：本主稿＋`review/wp77-delivery-2026-10-03/`（v1 材料——留史）＋`review/wp77-delivery-2026-10-03/revision-v2/`（v2 材料——留史）＋`review/wp77-delivery-2026-10-03/revision-v3/`（v3 回应、checks、来源身份、摘要、diff 绑定与严格 diff）。
- 后续：三项短复审；完整 demo 材料缺失时后续阶段采用的限定范围由 WP77 审查明确；不自行宣布全项目完成或直接进入 WP78/79/80。

## 修订记录

- 2026-10-03 **首版**（WP77，D18 第六包）：E34 九份全文（1,039 行）＋跨表引用 10 项实测＋定点消费链；场景 M01–M16 建立；附表与缺口表见交付目录。登记 ReviewPending（待统一 review）。
- 2026-10-03 **首审修订 v2**（首审 9 项：7 P2＋2 P3）：**R01** Home 更正为失败回程/Teleport 家地点回退（编辑器属性明示）——新游戏起始位置来自缺失的 System.rxdata（`001_StartGame.rb:7–16, 39–58` 定点），Home 已知、系统起始位置未知对照；初始金钱/PC 存放/Home/系统起始位置四类事实分开。**R02** 连接补 Route 8(69)↔Lappet(2) 直连（源表第 36 行）；19 条规范化连接表逐项不重不漏，配置记录数/无向边数/邻接重复列举分开。**R03** 区域地图分 6 条飞行记录与 5 个不同目的地（Cedolan 两条共用）；Essen 26 条＝18 普通＋6 飞行＋2 开关；飞行—治疗点完全匹配更正为 4 个（2＠(8,8)、23＠(11,15)、35＠(17,7)、52＠(17,14)），Cedolan 7＠(47,11) ≠ map 009 的 8＠(17,11)、map 055 的 52＠(30,10) 非飞行点。**R04** 岛屿开关 51/52 的读取消费者已存在（区域地图查询在开关未置位时隐藏对应信息/目的地；普通图/墙图入口分开，WP63 合同引用）——继续待证的是置位/解锁事件与访问路径。**R05** Dungeon 标记只启用生成；参数选择由全局区域（默认 none）/版本（默认 0）经版本键→区域键→默认参数（5×5）回退——区域 cave/0 才选到 5×4 样本；cave 通道随机偏移开启、forest 省略未开启的差异补记；赋值事件与 tileset 供给待证。**R06** 等级缩放完整规则：偏移＝队伍平衡级 −4＋0–4，再夹 [1, 最大等级]，赋级、重算、重置招式（偏移 ≤0 → 1、> 上限 → 上限）。**R07** 遭遇计数分槽位记录与不同标识——Safari 内区陆遇 12 条/11 种、水/钓 14 条/12 种；Tiall 8 条＝6 条 _1 后缀＋2 条无后缀（CUBONE/PIKACHU）；数量限根目录当前表，Gen 5–8 备份仅身份登记（未全文阅读，不当当前默认）。**R08** Default 通用 Intro 5 条、时段 Intro 3 条（早/午/晚各 1）分开；注释标为 Poké Center 的条目 3 个与 HealingSpot 字段 6 处分开，不推断完整游戏设施总数。**R09** 计数口径统一——覆盖附表档位列实测①15 行/②11 行；缺口链统一为 G01–G12 十二组（主稿与缺口表同组）；跨表检查为 8 项具名＋1 项汇总（0 未解析仅限实际检查集合）；③已证事件链与④运行观察继续为 0，不为凑数字提升证据档位。新增定点阅读：Metadata 属性、StartGame、RegionMap 开关读取、DungeonParameters 回退、RandomDungeons 默认、WP61/WP14 已批准合同行；Gen 备份存在性核验。v1 主稿 `db304223`／29,990 留史；v1 材料与审查原件不改写。
- 2026-10-03 **首审修订 v3**（复审残留 2 项 P2＋1 项新增 P3，共 3 项）：**R03** §4.4 普通点 18 条枚举删去 Cedolan 第二点位——town_map (13,10) 与 (14,10) 两个 Cedolan 点均带飞行目的地 7＠(47,11)，只归飞行记录组，普通组不含任何 Cedolan 记录；26＝18＋6＋2、5 个不同目的地、4 个治疗点匹配保持不变（`town_map.txt:8–9` 复核）。**R07** §5.1 水/钓重复者更正——Safari 内区重复者为 MAGIKARP 三条（OldRod 两条、GoodRod 一条），FEEBAS 仅 GoodRod 一条，不存在「MAGIKARP 与 FEEBAS 各重复槽位」；14 条/12 种、陆遇 12 条/11 种、Tiall 6＋2 与备份身份保持不变（`encounters.txt:245–262` 复核）。**N01**（本轮补充发现，P3）§4.2 户外图清单更正——map 045 源注释与 Name 均属 Route 6（Route 6 Cycling Road），清单更正为 Route 5(041)、Route 6(044/045)；已正确的 041↔045 连接不改（`map_metadata.txt:200–221` 复核）。本轮无新增源码阅读，为同 HEAD 既有阅读复核；场景 M01–M16 全部保留、本轮无场景行变更（M05/M12 已核对无同类错误）、无新增/删除。v2 被复审主稿 `40f21b99`／41,773 与 v2 附表 `95d38a6c`／7,628 留史；v2 材料与复审原件不改写。
