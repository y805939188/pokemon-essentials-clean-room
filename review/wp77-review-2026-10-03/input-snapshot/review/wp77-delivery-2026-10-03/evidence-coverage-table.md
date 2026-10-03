# WP77 能力/证据覆盖附表（demo 证据与能力覆盖；首版）

2026-10-03；规格提取方。主稿 [wp77-demo-evidence-and-capability-coverage.md](../../specs/demo/wp77-demo-evidence-and-capability-coverage.md)（首版当前）。覆盖粒度＝能力候选/入口；每行给出证据档位（①配置事实／②静态能力／③事件链待证／④运行观察——本包无④）、主规格或来源与缺口。结构法实测：**四组 5／3／5／3＝16 行**（缺口附录不占数据行）。

## A 世界配置与入口候选（5 行）

| 能力候选 | 证据档位 | 已能证明 | 来源 | 缺口 | 场景 |
| --- | --- | --- | --- | --- | --- |
| 起始元数据 | ① | StartMoney 3000、POTION、Home＝地图 3＠(7,5) 朝向 8、BGM 组、Red/Leaf 双外观 | `metadata.txt:3–33`；WP24/WP65 合同 | Intro 剧情与新游戏事件 | M02 |
| 地图登记 | ① | 69 节（[001]–[075] 缺 6 号）；户外图位置、治疗点×6、天气×3、旗标组 | `map_metadata.txt` 全文；WP11/WP12/WP13/WP61 合同 | 几何/事件页/通行 | M03 |
| 地图连接 | ① | 19 条连接全部命中登记地图 | `map_connections.txt` 全文；WP11 合同 | 通行条件与位移验证 | M04 |
| 区域地图/飞行 | ①＋② | Essen 26 点（5 飞行点＋2 开关点）、Tiall 1 点；飞行三元组全部指向已登记地图 | `town_map.txt` 全文；WP63 消费合同 | 飞行解锁前提（开关/剧情） | M05 |
| 地牢参数 | ①＋② | [cave]/[forest] 两套参数；051 `Dungeon = true` 绑定；等级缩放消费者实测 | `dungeon_parameters.txt` 全文；`004_Overworld_EncounterModifiers.rb:45–70`；WP14 合同 | 生成器运行与进入地图 | M08 |

## B 生物与玩家流程候选（3 行）

| 能力候选 | 证据档位 | 已能证明 | 来源 | 缺口 | 场景 |
| --- | --- | --- | --- | --- | --- |
| 遭遇配置 | ① | 19 节全部命中登记地图；13 种遭遇类型（含 BugContest 注册）；051 全表等级 1、075 为 _1 形态 | `encounters.txt` 全文；`013_EncounterType.rb:175`；WP36/WP60 合同 | 地图几何与通行 | M06、M07 |
| 训练家配置 | ① | 20 节；15 个使用类型全部注册；Brock 全字段；Shadow 个体×2；宿敌三变体与冠军队 | `trainers.txt` 全文；`trainer_types.txt` 核对；WP23/WP54/WP73-A 合同 | 放置事件与战斗顺序 | M10 |
| 电话联系人 | ①＋② | Jeff/Susie 台词齐备且均有本体＋再战版 v1 训练家对应 | `phone.txt` 全文；`trainers.txt` 对应节；WP63 合同 | 联系人注册/再战推进事件 | M11 |

## C 特殊玩法与设施候选（5 行）

| 能力候选 | 证据档位 | 已能证明 | 来源 | 缺口 | 场景 |
| --- | --- | --- | --- | --- | --- |
| Safari Zone | ①＋② | 066/067/068 地图与遭遇；SafariMap 旗标；WP53 会话合同与入口存在 | `map_metadata.txt:334–353`；`encounters.txt:222–262`；`001_SafariZone.rb:63–94`；WP53 | 接待事件（收费/步数链——不断言免费或收费） | M12 |
| 捕虫大会 | ①＋② | MossRock/BugContest/BugContestReception 旗标；BugContest 遭遇表与类型注册；WP53 会话合同 | `map_metadata.txt:128–146`；`encounters.txt:85–119`；`013_EncounterType.rb:175`；WP53 | 接待/评奖事件 | M13 |
| 战斗边疆 | ①＋② | 052–065 设施群（Tower/Palace/Arena/Factory/Stadium lobby）；默认＋4 杯赛列表；fancy 非 _single 无引用 | `map_metadata.txt:264–332`；`battle_facility_lists.txt` 全文；WP54/WP55/WP56/WP57/WP76 合同 | 接待事件与参赛/租赁链 | M14 |
| 小游戏/拼图 | ①＋②（依赖） | Game Corner 013 登记存在；WP68-70 六活动与 WP71 具名静态范围可作依赖 | `map_metadata.txt:60–66`；主区导入稿与 WP71 规格（依赖身份） | 事件入口材料（场所登记 ≠ 可玩） | M15 |
| 特殊机制图 | ①＋② | 051 等级缩放消费者、DistortionWorld→Giratina 形态消费者、Magnetic 进化链双侧命中 | `map_metadata.txt:238–262, 372–388`；`004_Overworld_EncounterModifiers.rb:45–70`；`001_FormHandlers.rb:267–271`；`007_Evolution.rb:490–497`；`pokemon.txt` 定点 | 进入地图与触发验证 | M08、M09 |

## D UI 与作者工作流候选（3 行）

| 能力候选 | 证据档位 | 已能证明 | 来源 | 缺口 | 场景 |
| --- | --- | --- | --- | --- | --- |
| 区域地图 UI | ①＋② | 点/飞行配置与 WP63 消费合同 | `town_map.txt` 全文；WP63 | 解锁前提事件 | M05 |
| 电话系统 | ①＋② | 台词与联系人配置；WP63 注册/来电/推进合同 | `phone.txt` 全文；WP63 | 注册/推进事件 | M11 |
| 作者工具链 | ②（依赖） | 调试/编辑器/动画/编译/生成器的已批准入口（与 demo 玩家事件入口分开） | WP72/WP73-A/B/WP74/WP75/WP76 已通过合同（依赖身份） | 工具的 demo 素材前提（按 WP75/WP76 已登记缺口） | M15、M16 |

## 附：缺口与未证边界（不占数据行）

事件证据链（§③档）一律待证：新游戏 Intro、遭遇发生、训练家放置、电话注册、Safari 接待、大会举办、边疆接待、小游戏入口、寄养/商店库存、进化地点通行、地牢进入、飞行解锁——缺 `Data/Map*.rxdata`/`MapInfos.rxdata`/`CommonEvents.rxdata` 等材料（U01）；不据配置或场所断言可达、不据缺材料断言不存在、不假定正常启动或缺文件回退形态；全部运行观察（④）不在本包。对应场景 M01、M16。
