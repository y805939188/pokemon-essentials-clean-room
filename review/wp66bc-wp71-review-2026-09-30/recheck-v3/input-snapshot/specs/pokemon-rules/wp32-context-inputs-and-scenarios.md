# WP32 附表 — 情境输入、默认数据与前后状态

状态：**Reviewed（限定静态范围，2026-09-30独立首审PASS_SCOPED；管理性回填）**。35身份／57条默认数据与已述静态对照随WP32主稿限定通过；N02宿主运行、地图／事件可达与前向范围保留。主规则与读写时点见[WP32](wp32-contextual-trade-and-post-battle-evolution.md)；基础条件／成功提交引用WP31。表中零数据行只表示顶层PBS没有该身份的字面示例，不表示功能不存在。

## 1. 35个情境身份与默认数据覆盖

| 身份（审计） | 顶层进化数据行数 | 主要输入与消费上下文 |
| --- | ---: | --- |
| LevelDay | 4 | 升级类检查时的宿主时段；持物／友好附加条件见WP31 |
| LevelNight | 5 | 升级类检查时的宿主时段；持物／友好附加条件见WP31 |
| LevelMorning | 0 | 升级类检查时的宿主时段；持物／友好附加条件见WP31 |
| LevelAfternoon | 0 | 升级类检查时的宿主时段；持物／友好附加条件见WP31 |
| LevelEvening | 1 | 升级类检查时的宿主时段；持物／友好附加条件见WP31 |
| LevelNoWeather | 0 | 升级类检查当时的世界天气，非战斗天气 |
| LevelSun | 0 | 升级类检查当时的世界天气，非战斗天气 |
| LevelRain | 1 | 升级类检查当时的世界天气，非战斗天气 |
| LevelSnow | 0 | 升级类检查当时的世界天气，非战斗天气 |
| LevelSandstorm | 0 | 升级类检查当时的世界天气，非战斗天气 |
| LevelCycling | 0 | 升级类检查当时的全局载具状态 |
| LevelSurfing | 0 | 升级类检查当时的全局载具状态 |
| LevelDiving | 0 | 升级类检查当时的全局载具状态 |
| LevelDarkness | 0 | 升级类检查当时的当前地图／元数据 |
| LevelDarkInParty | 1 | 升级类检查当时的玩家非蛋队伍 |
| HappinessDay | 3 | 升级类检查时的宿主时段；持物／友好附加条件见WP31 |
| HappinessNight | 3 | 升级类检查时的宿主时段；持物／友好附加条件见WP31 |
| DayHoldItem | 1 | 升级类检查时的宿主时段；持物／友好附加条件见WP31 |
| NightHoldItem | 2 | 升级类检查时的宿主时段；持物／友好附加条件见WP31 |
| HasInParty | 1 | 升级类检查当时的玩家非蛋队伍 |
| Location | 0 | 升级类检查当时的当前地图／元数据 |
| LocationFlag | 6 | 升级类检查当时的当前地图／元数据 |
| Region | 0 | 升级类检查当时的当前地图／元数据 |
| ItemDay | 0 | 使用道具检查时的宿主时段 |
| ItemNight | 0 | 使用道具检查时的宿主时段 |
| Trade | 8 | 交换收尾；收到者、送出者／时钟／持物，实际关系见主稿§6 |
| TradeMale | 0 | 交换收尾；收到者、送出者／时钟／持物，实际关系见主稿§6 |
| TradeFemale | 0 | 交换收尾；收到者、送出者／时钟／持物，实际关系见主稿§6 |
| TradeDay | 0 | 交换收尾；收到者、送出者／时钟／持物，实际关系见主稿§6 |
| TradeNight | 0 | 交换收尾；收到者、送出者／时钟／持物，实际关系见主稿§6 |
| TradeItem | 16 | 交换收尾；收到者、送出者／时钟／持物，实际关系见主稿§6 |
| TradeSpecies | 2 | 交换收尾；收到者、送出者／时钟／持物，实际关系见主稿§6 |
| BattleDealCriticalHit | 1 | 战后检查；本场K；有目标后可取消演出 |
| Event | 1 | 事件显式编号；可复用 |
| EventAfterDamageTaken | 1 | 战后D≥49只置R；后续事件编号＋R才命中 |

合计57行、17个身份有数据、18个身份无本次顶层样本。35个身份均在Evolution注册文本中存在；EventAfterDamageTaken跨两个检查上下文但只算一个身份。

## 2. 默认顶层数据条目

表中数据不证明检查会通过：例如两条TradeSpecies因实际比较自身物种而不匹配默认参数；详主稿。

| 来源个体数据节 | 目标 | 方法 | 参数 | 文件:行 |
| --- | --- | --- | --- | --- |
| POLIWHIRL | POLITOED | TradeItem | KINGSROCK | pokemon.txt:1615 |
| KADABRA | ALAKAZAM | Trade | 无 | pokemon.txt:1696 |
| MACHOKE | MACHAMP | Trade | 无 | pokemon.txt:1777 |
| GRAVELER | GOLEM | Trade | 无 | pokemon.txt:1990 |
| SLOWPOKE | SLOWKING | TradeItem | KINGSROCK | pokemon.txt:2097 |
| MAGNETON | MAGNEZONE | LocationFlag | Magnetic | pokemon.txt:2178 |
| HAUNTER | GENGAR | Trade | 无 | pokemon.txt:2473 |
| ONIX | STEELIX | TradeItem | METALCOAT | pokemon.txt:2524 |
| RHYDON | RHYPERIOR | TradeItem | PROTECTOR | pokemon.txt:2971 |
| SEADRA | KINGDRA | TradeItem | DRAGONSCALE | pokemon.txt:3107 |
| SCYTHER | SCIZOR | TradeItem | METALCOAT | pokemon.txt:3270 |
| ELECTABUZZ | ELECTIVIRE | TradeItem | ELECTIRIZER | pokemon.txt:3322 |
| MAGMAR | MAGMORTAR | TradeItem | MAGMARIZER | pokemon.txt:3349 |
| EEVEE | LEAFEON | LocationFlag | MossRock | pokemon.txt:3537 |
| EEVEE | GLACEON | LocationFlag | IceRock | pokemon.txt:3539 |
| EEVEE | ESPEON | HappinessDay | 无 | pokemon.txt:3541 |
| EEVEE | UMBREON | HappinessNight | 无 | pokemon.txt:3542 |
| PORYGON | PORYGON2 | TradeItem | UPGRADE | pokemon.txt:3643 |
| GLIGAR | GLISCOR | NightHoldItem | RAZORFANG | pokemon.txt:5478 |
| SNEASEL | WEAVILE | NightHoldItem | RAZORCLAW | pokemon.txt:5691 |
| PORYGON2 | PORYGONZ | TradeItem | DUBIOUSDISC | pokemon.txt:6163 |
| NOSEPASS | PROBOPASS | LocationFlag | Magnetic | pokemon.txt:7917 |
| FEEBAS | MILOTIC | TradeItem | PRISMSCALE | pokemon.txt:9243 |
| DUSCLOPS | DUSKNOIR | TradeItem | REAPERCLOTH | pokemon.txt:9433 |
| CLAMPERL | HUNTAIL | TradeItem | DEEPSEATOOTH | pokemon.txt:9699 |
| CLAMPERL | GOREBYSS | TradeItem | DEEPSEASCALE | pokemon.txt:9700 |
| BUDEW | ROSELIA | HappinessDay | 无 | pokemon.txt:10728 |
| CHINGLING | CHIMECHO | HappinessNight | 无 | pokemon.txt:11413 |
| HAPPINY | CHANSEY | DayHoldItem | OVALSTONE | pokemon.txt:11596 |
| RIOLU | LUCARIO | HappinessDay | 无 | pokemon.txt:11778 |
| MANTYKE | MANTINE | HasInParty | REMORAID | pokemon.txt:12057 |
| BOLDORE | GIGALITH | Trade | 无 | pokemon.txt:13724 |
| GURDURR | CONKELDURR | Trade | 无 | pokemon.txt:13928 |
| KARRABLAST | ESCAVALIER | TradeSpecies | SHELMET | pokemon.txt:15330 |
| SHELMET | ACCELGOR | TradeSpecies | KARRABLAST | pokemon.txt:16029 |
| PANCHAM | PANGORO | LevelDarkInParty | 32 | pokemon.txt:17489 |
| SPRITZEE | AROMATISSE | TradeItem | SACHET | pokemon.txt:17689 |
| SWIRLIX | SLURPUFF | TradeItem | WHIPPEDDREAM | pokemon.txt:17739 |
| TYRUNT | TYRANTRUM | LevelDay | 39 | pokemon.txt:18037 |
| AMAURA | AURORUS | LevelNight | 39 | pokemon.txt:18087 |
| SLIGGOO | GOODRA | LevelRain | 50 | pokemon.txt:18263 |
| PHANTUMP | TREVENANT | Trade | 无 | pokemon.txt:18338 |
| PUMPKABOO | GOURGEIST | Trade | 无 | pokemon.txt:18389 |
| YUNGOOS | GUMSHOOS | LevelDay | 20 | pokemon.txt:18991 |
| CHARJABUG | VIKAVOLT | LocationFlag | Magnetic | pokemon.txt:19067 |
| CRABRAWLER | CRABOMINABLE | LocationFlag | IceRock | pokemon.txt:19117 |
| FOMANTIS | LURANTIS | LevelDay | 34 | pokemon.txt:19480 |
| COSMOEM | SOLGALEO | LevelDay | 53 | pokemon.txt:20418 |
| COSMOEM | LUNALA | LevelNight | 53 | pokemon.txt:20419 |
| SNOM | FROSMOTH | HappinessNight | 无 | pokemon.txt:22469 |
| KUBFU | URSHIFU | Event | 1 | pokemon.txt:22946 |
| RATTATA,1 | RATICATE | LevelNight | 20 | pokemon_forms.txt:87 |
| FARFETCHD,1 | SIRFETCHD | BattleDealCriticalHit | 3 | pokemon_forms.txt:385 |
| CUBONE,1 | MAROWAK | LevelNight | 28 | pokemon_forms.txt:441 |
| LINOONE,1 | OBSTAGOON | LevelNight | 35 | pokemon_forms.txt:840 |
| YAMASK,1 | RUNERIGUS | EventAfterDamageTaken | 2 | pokemon_forms.txt:1395 |
| ROCKRUFF,2 | LYCANROC | LevelEvening | 25 | pokemon_forms.txt:1807 |

## 3. 地图／天气的具名数据对照

| 地图元数据编号 | 相关字段 | 可以支持的结论 |
| --- | --- | --- |
| 028 | MossRock | 当前图旗标输入可满足此类条件；不证明真实岩石事件存在 |
| 034 | IceRock | 同上，冰岩旗标 |
| 049／050／051 | Magnetic | 同上，磁场旗标；050另有DarkMap |
| 021 | Rain,100 | 正常转移天气输入可成为Rain；实际天气读取仍在检查时 |
| 047 | Rain,0 | 数据声明不等于当前正在下雨；概率分支为0 |
| 072 | Storm,50 | 随机成为Storm，类别Rain；不执行随机验证 |

世界天气None不命中五个天气族中除LevelNoWeather外的类别；Sun→LevelSun，Rain／Storm／HeavyRain／Fog→LevelRain，Snow／Blizzard→LevelSnow，Sandstorm→LevelSandstorm。只有9种默认世界天气；战斗天气标识不是本表输入。

## 4. 固定算术／状态对照

| 前提 | 预期 | 区别 |
| --- | --- | --- |
| 本场替身实损30＋19，未濒死 | D49 | 个体HP损失可以为0；战后只置R |
| 混乱实损10＋友方实损39 | D49 | 没有必须敌方来源的门 |
| 第一场48、下一场1 | 各自D48、D1 | 非历史累计49 |
| 当前HP20，致死伤害被撑住改到1 | D增19 | 实损不是预计伤害100 |
| 某次逐目标要害共3个可计写入点 | K增3 | 不是一招记1；其中可含友方与替身 |
| [A,B,C]换出A、新增X | [B,C,X]；[10,20,30]→[20,30,空]，K[1,3,0]→[3,0,空]，D[0,49,5]→[49,5,空] | 空槽不继承被移出成员，默认0和缺失槽不同 |
| 全结果检查开／关 | 开={0,1,2,3,4,5}；关={0,1,3,4} | 前提是进入世界结束通知；准入跳过不是决定0这一行 |
| R真、事件2命中后取消 | 触发工具true；R仍真、物种不变 | 事件编号不消费；真正提交后才清R |

## 5. 来源与限制

`Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb`35身份字面集合；`PBS/pokemon.txt`与`pokemon_forms.txt`对应Evolution行；`PBS/map_metadata.txt`具名字段；时间／天气／战斗记录消费者见主稿traceability。没有执行参考表达式、模拟器、事件或编译器。数据计数／来源身份、数学向量、人工控制流检查分别登记，不互相代替。

依据[独立首审报告](../../review/wp22-wp23-wp32-review-2026-09-30/report.md)§4回填；被审附表v1 `869cbbaafb6dab2c9bd2da0c2711a7443b2ae88b8007e238f5c156acc53c498d`（9,798字节）留史；本次仅状态回填，数据／场景未改。
