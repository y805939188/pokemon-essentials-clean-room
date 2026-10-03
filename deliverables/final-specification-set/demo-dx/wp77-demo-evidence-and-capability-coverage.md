# WP77：示例工程证据与能力覆盖

分类：Demo / Developer Experience（demo-dx）

本稿是 WP77 已批准行为规格的净化交付：内容等价于被审批准文本的行为合同，源码标识、脚本名与内部结构描述已移除或改写为实现中立表述；配置键、数据字段名与内容身份名（物种、道具、类型、招式、地图名等）按数据标识保留。数学记法统一为全角括号。全部源路径、行号与溯源细节集中于审计文件，不属本稿。**本稿全部结论为静态配置与已批准合同的核验结果，未经任何运行确认。**核心原则：**配置存在 ≠ 已演示，入口存在 ≠ 可达**——示例工程素材的缺口（U01）使全部玩家侧事件链保持不可验证。

## 1. 目的、范围与非目标

### 1.1 目的

本规格登记示例工程当前材料**实际能证明什么**，按证据强度分档，避免把「配置了」误述为「能玩」：

- **① 配置事实**：数据文件中存在对应记录（静态可读、可计数、可交叉引用）。
- **② 静态能力**：已批准规格证实消费者/解释器合同存在，配置若被加载即被消费。
- **③ 事件证据链**：demo 事件把入口接到玩家可达路径——**当前不可达**（地图、公共事件、系统档案均缺）。
- **④ 运行观察**：实机运行确认——**不做**（本阶段不运行参考实现）。

### 1.2 范围（A～D 具名静态范围）

- **A 世界配置与入口候选**：起始/回程配置、地图登记、地图连接、区域地图/飞行点、地牢参数。
- **B 生物与玩家流程候选**：野外遭遇、训练家、电话联系人。
- **C 特殊玩法与设施候选**：Safari、捕虫大会、战斗边疆、小游戏场所、进化地点旗标链。
- **D UI 与作者工作流候选**：区域地图/飞行、电话、作者工具链入口与 demo 玩家事件入口的区分。

### 1.3 非目标

不证明任何地图可通行、任何事件可触发、任何流程可完整游玩；不据 PBS 配置断言「已演示」；不据设施场所登记断言「可玩」；不推出缺失档案的运行回退形态；不修复配置原文中的指向异常（如实登记）。

## 2. 概念与术语

- **能力候选**：已配置数据＋已批准消费合同的组合，因缺事件链证据而不能升格为「已演示能力」。
- **缺口（U01 系）**：示例工程素材缺失清单——地图档案、地图信息档案、公共事件档案、系统档案、图块集档案、动画档案、图像资源目录、音频资源目录、插件目录、工程配置与工程文件均不存在（逐项存在性复核，见 §3）。
- **节**：数据表中按编号分组的记录单元（如地图元数据节、遭遇节、训练家节）。
- **旗标**：地图元数据中的布尔标记，驱动特定消费链。本稿涉及四条已批准消费链：扭曲世界旗标（形态切换）、野外等级缩旗标（遭遇等级偏移）、地点旗标进化（升级时求值当前地图旗标）、大会旗标（捕虫大会会话）。
- **证据档位**：①～④ 如 §1.1；缺口表与测试目录统一使用。

## 3. 当前材料状态

示例工程数据目录顶层**仅三项**：

1. 脚本散文件目录（312 个脚本文件）；
2. 脚本归档；
3. 核心消息数据文件。

**逐项缺失**（存在性复核结论）：全部地图档案、地图信息档案、公共事件档案、系统档案、图块集档案、动画档案；图像资源目录；音频资源目录；插件目录；工程配置文件；工程文件。

**不推出**：不据缺失清单推断运行时的回退形态（何种错误、何种默认）；不据 PBS 文本配置断言任何内容「已演示」。

## 4. A：世界配置与入口候选

### 4.1 全局元数据（33 行）

- **初始金钱** 3000；**初始 PC 存放** 1 个伤药——①配置事实。
- **Home＝地图 3，坐标（7,5），朝向 8**：经编辑器属性明示，其语义为**失败回程/传送类家地点回退**（WP61 合同），**不是新游戏起点证据**。系统起始位置来自缺失的系统档案——**Home 已知、系统起始位置未知**（游戏初始化/新游戏开始入口定点移审计）。
- **双外观**：[1] Red／[2] Leaf 两套玩家外观及角色图名已配置。
- 背景音乐相关配置存在。

### 4.2 地图元数据（69 节）

- 节号区间 [001]–[075]，缺号 022、032、033、042、043、048，实有 **69 节**。
- **户外图**（均带区域地图坐标）：Lappet Town（002）、Route 1（005）、Cedolan City（007）、Route 2（021）、Lerucean Town（023）、Natural Park（028）、Route 3（031）、Ingido Plateau（035）、Route 4（039/040）、Route 5（041）、Route 6（044/045——045 为 Route 6 自行车道，源注释与名称字段一致）、Route 7（047）、Battle Frontier（052）、Safari Zone 外区（066）与内区（068）、Route 8（069）、Berth Island（072）、Faraday Island（073）、Tiall Region（075）。
- **室内/设施图**：玩家家（003）、实验室（004）、Kurt 家（006）、Daisy 家（008）、注释标为 Poké Center 的条目 3 个（009/024/053——注释性场所标题与名称字段分开计数）、商店（025/054）、研究所（011）、公寓（012）、Game Corner（013）、百货 1–5 层＋天台＋电梯（014–020）、Cedolan Gym（010）、球迷俱乐部（026）、寄养屋（027）、公园入口/会馆（029/030）、联盟入口/房间 1/名人堂（036/037/038）、自行车道闸口两处（046/074）、岩洞 1F/B1F（049/050）、Dungeon（051）、Battle Tower（055）与 arena（056）、Stadium Cup 大厅（057）、Battle Palace（058）与 arena（059）、Battle Arena（060）与 arena（061）、Battle Factory（062）与引导走廊（063）、arena（064）、走廊（065）、Safari 大门（067）、水下（070）、码头（071）。
- **治疗点字段 6 处**（字段次数与注释 Poké Center 条目数是两个单位）：玩家家（003：地图 2＠（8,8)）、Cedolan PC（009：地图 8＠（17,11)）、Lerucean PC（024：地图 23＠（11,15)）、联盟入口（036：地图 35＠（17,7)）、边疆 PC（053：地图 52＠（17,14)）、Battle Tower（055：地图 52＠（30,10)）。**009 行指向地图 8 为配置原文，不作语义修正**。
- **天气**：Route 2（021）＝Rain 100；Route 7（047）＝Rain 0；Berth Island（072）＝Storm 50。
- **特殊旗标/字段**：MossRock（028）、IceRock（034）、Magnetic（049/050/051）、DistortionWorld（049/050/051/072/073）、ScaleWildEncounterLevels（051）、BugContest（028）、BugContestReception（029/030）、DisableBoxLink（010/037/038/056/059/061/063/064/065）、DarkMap（050）、Dungeon（051）、SafariMap（068）、DiveMap 70（069）、Environment 各值、Bicycle/BicycleAlways、MapSize。

### 4.3 地图连接（19 条）

规范化无向边表（每对相邻地图列一次）：(41,40)、(41,45)、(44,5)、(66,5)、(7,5)、(2,5)、(7,44)、(2,66)、(69,66)、(35,39)、(7,23)、(31,23)、(21,23)、(47,7)、(21,7)、(31,35)、(69,2)、(47,52)、(21,47)——含 **Route 8（69）↔ Lappet Town（2）直连**。

**计数口径**：配置记录数＝无向边数＝19；邻接关系按两端重复列举是另一单位，不混计。连接表证明拓扑登记，**不证明通行性或几何衔接**。

### 4.4 区域地图（2 区 27 点）

- **Essen 区 26 条＝18 普通点＋6 飞行记录＋2 开关点**；普通点组不含任何 Cedolan 记录（两个 Cedolan 点均带飞行目的地、只归飞行记录组）。
- **6 条飞行记录对应 5 个不同目的地**（Cedolan 两条共用同一目的地）：Lappet Town→2＠（8,8)；Cedolan（（13,10) 与 （14,10) 两条）→7＠（47,11)；Lerucean Town→23＠（11,15)；Ingido Plateau→35＠（17,7)；Battle Frontier→52＠（17,14)。
- **飞行—治疗点完全匹配 4 个**：2＠（8,8)、23＠（11,15)、35＠（17,7)、52＠（17,14) 与 §4.2 治疗点一致；**Cedolan 飞行点 7＠（47,11) ≠ 地图 009 治疗点的 8＠（17,11)**（配置原文登记）；地图 055 的 52＠（30,10)（Battle Tower）**不是飞行目的地**。
- **开关点 2 条**：Berth Island（开关 51）、Faraday Island（开关 52）——**读取消费者已存在**（WP63 合同：普通区域地图查询在开关未置位时隐藏对应信息/目的地；普通图与墙图入口条件分开）。**继续待证的是开关的置位/解锁事件与访问路径，不是读取消费者是否存在**。
- Tiall 区 1 条；两区合计 **27 条**。

### 4.5 地牢参数（2 套）

- 地图 051 的 `Dungeon = true` 只**启用**随机地牢生成路径（地图设置回调定点移审计），不直接绑定参数集。
- 已配置两套参数集：[cave] 与 [forest]。**具体选中由全局区域（默认无赋值）与版本（默认 0）决定**：先查「区域_版本」键、后查「区域」键、均未中则用默认参数实例（WP14 合同）。
- **独立对照（非运行观察）**：区域无赋值/版本 0 → 默认参数（5×5 节点）；区域 cave/版本 0 才选到 5×4 样本。当前地图元数据没有证明 demo 把区域写为 cave 或 forest；区域/版本赋值事件与图块集供给均缺证据。
- [cave]：5×4 节点、单元 10×10、房间 5–9、走廊宽 2、**通道随机偏移开启**、节点/房间布局 full、房间概率 70、额外连接 2、地面补丁 2,50,25、地面装饰/虚空装饰 50,200。
- [forest]：5×4 节点、房间 4–8、地面补丁 3,75,25、**未写通道随机偏移项**——两集差异含通道随机偏移开/关。

## 5. B：生物与玩家流程候选

### 5.1 野外遭遇（19 节）

- **节—图全部命中**（§8 C2）：002 Lappet Town、005 Route 1 与 [005,1] 变体、021、028、031、034 Ice Cave、039、041、044、047、049/050 Rock Cave、051 Dungeon、066、068、069、070 水下、075 Tiall。
- **13 种遭遇类型矩阵**：Land（陆/晨昏时段）、LandMorning、LandNight、Water、Cave、OldRod／GoodRod／SuperRod、RockSmash、HeadbuttLow／HeadbuttHigh、PokeRadar、**BugContest（已注册类型）**。
- **051 全表为等级 1 幼年种**（配合野外等级缩放，§6.4）。
- **075 Tiall 8 条**：6 条带 _1 形态后缀（GEODUDE_1／RATTATA_1／DIGLETT_1／MEOWTH_1／SANDSHREW_1／VULPIX_1）＋2 条无后缀（CUBONE／PIKACHU）。
- **068 Safari 内区**：陆遇 **12 条／11 个不同物种**（VENONAT 重复两槽）；水/钓 **14 条／12 个不同物种**——重复者为 MAGIKARP 三条（旧钓竿两条、好钓竿一条）、FEEBAS 仅好钓竿一条。**重复槽位不合并、权重不重整**。
- 数量仅限根目录当前表。**Gen 5–8 备份遭遇表属可选材料**（存在性登记：Gen 5 与 Gen 6 相同、Gen 7 与 Gen 8 相同且与根表一致——**仅身份核验、未全文阅读**，不把备份当当前默认；默认根集与备份的选择边界按 WP01/WP02 已登记发现机制）。

### 5.2 训练家（20 节）

- **15 个使用类型全部在类型表注册**：BEAUTY、CAMPER、CHAMPION、COOLCOUPLE、FISHERMAN、HIKER、LASS、LEADER_Brock、PICNICKER、POKEMONTRAINER_May、RIVAL1、SWIMMER2_F、TEAMROCKET_F、TEAMROCKET_M、YOUNGSTER。
- **LEADER Brock 全字段样本**：携带 FULLRESTORE×2；GEODUDE（12 级）指定招式/特性位/性别/个体值全 20；ONIX（14 级）昵称 Rocky、指定招式、SITRUSBERRY、**异色、HEAVYBALL**。
- **暗影个体×2**：TEAMROCKET_M Grunt（1）的 WEEPINBELL（21 级）、TEAMROCKET_F Grunt（1）的 ELECTABUZZ（20 级）。
- **版本系列**：RIVAL1 Blue 三变体（初始伙伴差异）、CHAMPION Blue（三只 63 级各持 SITRUSBERRY）、CAMPER Jeff 与 PICNICKER Susie 的**再战版 v1**。

### 5.3 电话（48 行）

- **[Default] 组**：通用 Intro **5 条**＋时段 Intro **3 条**（早/午/晚各 1——两组分开计数）、Body×2、Body1×4、Body2×4、BattleRequest×2（含训练家名/玩家名/类型/地点/金钱占位符）。
- **具名联系人 2 名**（CAMPER Jeff、PICNICKER Susie）：各有 Intro/Body1/Body2/BattleRequest/BattleRemind/End 全组台词。
- 与再战版训练家（Jeff v1、Susie v1）对应——WP63「再战就绪→版本推进」合同引用；具名联系人的时段台词不并入 Default 计数。

## 6. C：特殊玩法与设施候选

### 6.1 Safari

- 外区（066，陆遇 6 条）、大门（067）、内区（068，`SafariMap = true`、Environment＝Forest；陆遇 12 条/11 种＋水/钓 14 条/12 种——槽位与不同物种分开计数）。
- **Safari 会话消费者已批准**（WP53：步数预算/专用球/动作/结束回程的合同）；**会话查询/会话入口存在**（源码入口定点移审计）。
- 入园事件（收费/接待）缺失——**不据设施存在断言免费或收费**。

### 6.2 捕虫大会

- 028 Natural Park 带 **MossRock** 与 **BugContest** 旗标；029/030 带 **BugContestReception** 旗标。
- 028 的 BugContest 遭遇表（10 种，含 SCYTHER/PINSIR 各 5）；BugContest 遭遇类型已注册（定点移审计）；WP53 捕虫会话合同引用。

### 6.3 战斗边疆

- 地图群：052 户外＋053 PC＋054 商店＋055/056 Tower、057 Stadium Cup 大厅、058/059 Palace、060/061 Arena、062–065 Factory；arena/corridor 各图均带 **DisableBoxLink**（WP66-B 合同）。
- **设施列表配置（25 行）**：默认列表（battle_tower_trainers／battle_tower_pokemon）＋4 杯赛列表——pokecup（单/双打引用 cup_poke_\*）、littlecup（cup_little_\*）、pikacup（cup_pika_\*）、fancycup（单双打均引用 cup_fancy_\*_single 变体；**非 _single 的 fancycup 训练家/生物文件无引用**，WP76 已登记）。
- WP54/WP55/WP56/WP57/WP76 消费者合同引用。

### 6.4 小游戏场所与特殊机制图

- **Game Corner（013）**：仅地图元数据登记（无户外/旗标字段）——WP68–WP70 六个活动与 WP71 的静态依赖可用；各玩法脚本入口以事件调用形式存在，demo 事件入口材料缺失——**不据场所登记断言可玩**。
- **特殊机制图**：051 Dungeon（`Dungeon = true`＋野外等级缩放）；049/050/051/072/073 带 **DistortionWorld**——形态消费者实测合同：持特定宝珠或处于本旗标图 → 形态 1；049/050/051 带 **Magnetic**；Berth Island 天气 Storm 50。
- **野外等级缩放完整规则**：偏移值＝队伍平衡级 −4＋0–4 随机量，再夹到 [1, 成长系统最大等级]，随后赋等级、重算能力并重置招式——**中间量不是最终等级**；偏移 ≤0 → 夹到 1，偏移 > 上限 → 夹到上限。

### 6.5 进化地点旗标链

- LocationFlag 进化法在**升级时求值当前地图元数据是否带参数指定的旗标**（地图缺元数据时按无旗标处理）。
- 已配置六条：LEAFEON＝叶之石／**LocationFlag MossRock**（→028）；GLACEON＝冰之石／**LocationFlag IceRock**（→034）；MAGNEZONE＝雷之石／**LocationFlag Magnetic**（→049/050/051）；PROBOPASS／VIKAVOLT＝**LocationFlag Magnetic**；CRABOMINABLE＝**LocationFlag IceRock**。

## 7. D：UI 与作者工作流候选

- **区域地图/飞行与电话系统**：按 WP63 已批准消费合同引用（飞行解锁剧情/开关前提、联系人注册事件不可验证）。
- **作者工具链与 demo 玩家事件入口分开**：WP72 调试菜单、WP73-A/B 编辑器、WP74 动画制作、WP75 编译转换（含训练家列表编译与全部 PBS 编译）、WP76 设施内容生成器（写杯调试门与生成产物反写）——**工具可用入口 ≠ demo 玩家侧事件可达**；工具的 demo 素材前提按 WP75/WP76 已登记缺口保持。

## 8. 跨表引用完整性

| 编号 | 检查 | 结果 |
| --- | --- | --- |
| C1 | 连接 → 地图登记 | 19 条两端编号全部命中 69 节（含 69↔2） |
| C2 | 遭遇节 → 地图登记 | 19 节（含 [005,1] 变体）全部命中 |
| C3 | 训练家类型 → 类型注册 | 15 个使用类型全部注册 |
| C4 | 电话联系人 → 训练家节 | Jeff/Susie 均有本体＋再战版 v1 |
| C5 | 飞行记录 → 目的地/治疗点 | 6 条飞行记录、5 个不同目的地全部指向已登记地图；与治疗点完全匹配 4 个；Cedolan 7＠（47,11) ≠ 地图 009 的 8＠（17,11)（原文登记） |
| C6 | 进化 LocationFlag 链 | 6 条进化数据对求值合同与旗标图双侧命中 |
| C7 | 杯赛挑战 ID → 设施列表 | 8 个挑战 ID 对 WP54 杯赛规则族已批准；具体 ID 绑定为配置原文 |
| C8 | BugContest 遭遇类型 | 已注册 |
| 汇总 | 未解析引用 | **0 项**（仅限实际检查集合；fancycup 非 _single 文件无引用已登记；地图 075 与 Tiall 区条目对应） |

## 9. 缺口与影响（G01–G12）

| 缺口 | 候选链 | 已能证明（档位） | 仍缺证据 | 影响的结论 |
| --- | --- | --- | --- | --- |
| G01 | 新游戏→起始位置 | 初始金钱/PC 存放①、Home 回程①、外观① | 系统档案起始地图/坐标与 Intro 剧情 | 系统起始位置与新游戏流程不可证 |
| G02 | 野外遭遇/钓/碎岩/撞树/雷达 | 遭遇表①、触发合同② | 地图几何与通行 | 实际遇敌不可证 |
| G03 | Brock/火箭队/宿敌/冠军 | 训练家数据①、类型注册② | 放置事件 | 剧情战不可证 |
| G04 | 再战 Jeff/Susie | 电话文本①、再战版对应② | 联系人注册事件 | 电话再战链不可证 |
| G05 | Safari 入园 | 地图/遭遇①、会话合同② | 接待事件（收费/步数/动作链） | 入园流程不可证 |
| G06 | 捕虫大会 | 旗标/遭遇①、会话合同② | 接待/评奖事件 | 大会举办不可证 |
| G07 | 边疆四设施＋杯赛 | 地图/列表①、规则会话合同② | 接待事件（参赛/租赁/评级链） | 设施挑战不可证 |
| G08 | 小游戏/拼图 | 场所①、静态规格依赖② | 事件入口 | 可玩性不可证 |
| G09 | 寄养/商店/百货 | 场所①、WP27/WP66-C 合同② | 商店库存/寄养收费事件 | 交易流程不可证 |
| G10 | 进化地点 | 数据①、求值② | 到达地图 | 地点进化实际发生不可证 |
| G11 | 地牢/磁穴/扭曲图 | 参数①、消费者②（含夹限完整规则） | 地图生成与进入、区域/版本赋值事件与图块集供给 | 生成结果/形态切换/参数集选择不可证 |
| G12 | 飞行与岛屿开关 | 飞行点①、匹配 4 个②、开关读取消费② | 开关 51/52 的置位/解锁事件与实际访问路径 | 飞行可用性与两点可见性不可证 |

**档位计数**：①15 行、②11 行（按覆盖附表档位列复算）；**③已证事件链与④运行观察继续为 0**——不为凑数字提升证据档位。缺口分组与本表统一为 12 组（G01–G12）。

## 10. 示例场景与测试目录

示例场景 16 条见 `../test-catalog/demo-dx-wp72-73-74-75-76-77.md` 的 DM 系列（M01–M16），覆盖：当前材料状态（M01）、起始配置与 Home/系统起始位置区分（M02）、地图登记完整性与治疗点 6 处口径（M03）、19 条连接引用与 Route 8 直连（M04）、区域地图 18＋6＋2 与 4 个飞行—治疗点匹配（M05）、遭遇节引用（M06）、13 类型矩阵与 Tiall 6＋2、Safari 两组槽位/物种口径（M07）、地牢参数选择与等级缩放夹限（M08）、进化地点链（M09）、训练家配置（M10）、电话联系人与 Default 两组口径（M11）、Safari 配置链（M12）、捕虫大会配置链（M13）、边疆配置链（M14）、小游戏/拼图（M15）、缺口影响与证据档位 0（M16）。

## 11. 依赖与未决

### 11.1 依赖（已净化交付件）

- 数据与生命周期：[WP04](../generic-kernel/wp04-pbs-lifecycle.md)、[WP02](../generic-kernel/wp02-rule-configuration-and-data-variants.md)
- 世界：[WP11](../engine-overworld/wp11-map-topology-transfer.md)、[WP12](../engine-overworld/wp12-terrain-movement-vehicles.md)、[WP13](../engine-overworld/wp13-map-events-npc-followers.md)、[WP14](../engine-overworld/wp14-random-dungeons.md)、[WP15](../engine-overworld/wp15-resource-matching-and-audio.md)
- 消息/UI：[WP17](../user-interface/wp17-messages-windows-input.md)、[WP63](../user-interface/wp63-pokegear-map-music-and-phone.md)、[WP65](../user-interface/wp65-title-load-options-pause-and-pc.md)、[WP66-A](../user-interface/wp66-a-party-and-summary-ui.md)、[WP66-B](../user-interface/wp66-b-storage-and-pokedex-ui.md)、[WP66-C](../user-interface/wp66-c-bag-item-storage-and-shop-ui.md)、[WP67-A](../user-interface/wp67-a-battle-interaction-and-presentation.md)、[WP67-B](../user-interface/wp67-b-lifecycle-presentations-and-history.md)、[WP68](../user-interface/wp68-duel.md)、[WP69](../user-interface/wp69-slot-machine.md)、[WP70](../user-interface/wp70-mining.md)、[WP71](../user-interface/wp71-tile-puzzles.md)
- 生物：[WP36](../creature-rpg/wp36-wild-encounters-and-modifiers.md)、[WP57](../creature-rpg/wp57-factory-rentals-and-swaps.md)、[WP64](../creature-rpg/wp64-mail-and-mystery-gift.md)、[WP27](../creature-rpg/wp27-bag-and-item-storage.md)
- 规则：[WP53](../pokemon-rules/wp53-safari-and-bug-catching-contest.md)、[WP60](../pokemon-rules/wp60-berry-plants.md)、[WP61](../pokemon-rules/wp61-field-passive-effects-and-blackout.md)
- 战斗设施：[WP54](../combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md)、[WP55](../combat-requirements/wp55-facility-session-and-restoration.md)、[WP56](../combat-requirements/wp56-palace-and-arena-variants.md)
- 工具链：[WP72](wp72-debug-contexts-and-controls.md)、[WP73-A](wp73-a-content-editors.md)、[WP73-B](wp73-b-world-editors.md)、[WP74](wp74-battle-animation-authoring-and-exchange.md)、[WP75](wp75-project-conversion-and-authoring-tools.md)、[WP76](wp76-facility-content-generation-and-simulation.md)

### 11.2 未决（6 条）

1. **U01 保持开放**：完整工程材料齐备前，全部事件链不可验证。
2. 各候选链的接待/注册/放置事件均未证（G03–G09、G12）。
3. 地图 009 治疗点指向地图 8 与 Cedolan 飞行点（地图 7 城内）的关系按配置原文登记，语义待事件/地图材料佐证。
4. Tiall 区（地图 075＋区域地图条目）的接入方式（无连接条目）与 _1 形态遭遇的实际进入路径待证。
5. 岛屿开关（51/52）的读取消费者已存在——继续待证的是开关的置位/解锁事件与实际访问路径，不是读取消费者是否存在。
6. 全部运行表现未验证，留运行验证阶段。

## 12. 证据来源（类别）

九份数据表全文（合计 1,039 行：全局元数据 33、地图元数据 398、地图连接 40、遭遇 311、训练家 118、设施列表 25、地牢参数 30、区域地图 36、电话 48）＋跨表引用实测（C1–C8＋汇总）＋定点消费链（地点旗标进化求值、扭曲世界形态、野外等级缩放含夹限、捕虫大会类型注册、Safari 会话入口、设施列表查询、Home 属性、系统起始位置、区域地图开关读取、地牢参数回退、随机地牢默认）＋物种数据进化字段定点＋训练家类型注册核对＋Gen 5–8 备份遭遇表存在性核验（仅身份、未全文阅读）＋demo 数据目录与缺失项逐项存在性复核＋WP61（Home 回程合同行）与 WP14（地牢参数合同行）已批准文本定点复核。**全部源路径与行号集中审计文件。**

## 13. 状态与修订记录

- **被审身份**：WP77 v3（2026-10-03 短复审 PASS_SCOPED，10/10 闭环）；v1、v2 留史。净化后如实登记被审身份，不声明新一轮行为复审。
- **主要修订留痕**：v2 R01 Home 语义更正（回程回退 vs 系统起始位置）；R02 连接补 Route 8 直连、计数三口径分开；R03 区域地图 6 条飞行记录对 5 个目的地、Essen 26＝18＋6＋2、飞行—治疗点匹配更正为 4 个；R04 岛屿开关读取消费者已存在；R05 地牢标记只启用生成、参数选择回退链、cave 通道随机偏移开启 vs forest 省略；R06 等级缩放完整规则（偏移＝平衡级 −4＋0–4，再夹 [1, 最大等级]）；R07 遭遇计数分槽位记录与不同标识、数量限根目录当前表；R08 Default 通用 Intro 5 条 vs 时段 Intro 3 条分开、注释 Poké Center 3 个 vs 治疗点字段 6 处分开；R09 计数口径统一（①15/②11）、缺口链统一十二组、跨表检查 8 项具名＋1 项汇总、③④继续为 0；v3 R03 普通点 18 条枚举删去 Cedolan 第二点位；R07 水/钓重复者更正为 MAGIKARP 三条（旧钓竿两、好钓竿一）、FEEBAS 仅好钓竿一条；N01（P3）户外图清单更正 045 属 Route 6（自行车道）、清单更正为 Route 5（041) 与 Route 6（044/045)。
