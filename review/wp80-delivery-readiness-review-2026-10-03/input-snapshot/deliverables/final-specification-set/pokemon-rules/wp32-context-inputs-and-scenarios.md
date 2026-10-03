# 情境输入、默认数据与前后状态（净化附表；批次 6）

本附表是 [wp32-contextual-trade-and-post-battle-evolution](wp32-contextual-trade-and-post-battle-evolution.md) 的附件：35 个情境身份与默认数据覆盖、默认顶层数据条目（57 行）、地图/天气的具名数据对照、固定算术/状态对照。基础条件/成功提交引用《基础进化》。表中零数据行只表示顶层内容数据没有该身份的字面示例，不表示功能不存在。文件与行号定位见 `../../../audit/source-traceability.md` 本包条目。

## 1. 35 个情境身份与默认数据覆盖

| 身份（审计） | 顶层进化数据行数 | 主要输入与消费上下文 |
| --- | ---: | --- |
| LevelDay | 4 | 升级类检查时的宿主时段；持物/友好附加条件见《基础进化》 |
| LevelNight | 5 | 升级类检查时的宿主时段；持物/友好附加条件见《基础进化》 |
| LevelMorning | 0 | 升级类检查时的宿主时段；持物/友好附加条件见《基础进化》 |
| LevelAfternoon | 0 | 升级类检查时的宿主时段；持物/友好附加条件见《基础进化》 |
| LevelEvening | 1 | 升级类检查时的宿主时段；持物/友好附加条件见《基础进化》 |
| LevelNoWeather | 0 | 升级类检查当时的世界天气，非战斗天气 |
| LevelSun | 0 | 升级类检查当时的世界天气，非战斗天气 |
| LevelRain | 1 | 升级类检查当时的世界天气，非战斗天气 |
| LevelSnow | 0 | 升级类检查当时的世界天气，非战斗天气 |
| LevelSandstorm | 0 | 升级类检查当时的世界天气，非战斗天气 |
| LevelCycling | 0 | 升级类检查当时的全局载具状态 |
| LevelSurfing | 0 | 升级类检查当时的全局载具状态 |
| LevelDiving | 0 | 升级类检查当时的全局载具状态 |
| LevelDarkness | 0 | 升级类检查当时的当前地图/元数据 |
| LevelDarkInParty | 1 | 升级类检查当时的玩家非蛋队伍 |
| HappinessDay | 3 | 升级类检查时的宿主时段；持物/友好附加条件见《基础进化》 |
| HappinessNight | 3 | 升级类检查时的宿主时段；持物/友好附加条件见《基础进化》 |
| DayHoldItem | 1 | 升级类检查时的宿主时段；持物/友好附加条件见《基础进化》 |
| NightHoldItem | 2 | 升级类检查时的宿主时段；持物/友好附加条件见《基础进化》 |
| HasInParty | 1 | 升级类检查当时的玩家非蛋队伍 |
| Location | 0 | 升级类检查当时的当前地图/元数据 |
| LocationFlag | 6 | 升级类检查当时的当前地图/元数据 |
| Region | 0 | 升级类检查当时的当前地图/元数据 |
| ItemDay | 0 | 使用道具检查时的宿主时段 |
| ItemNight | 0 | 使用道具检查时的宿主时段 |
| Trade | 8 | 交换收尾；收到者、送出者/时钟/持物，实际关系见主稿 §6 |
| TradeMale | 0 | 交换收尾；收到者、送出者/时钟/持物，实际关系见主稿 §6 |
| TradeFemale | 0 | 交换收尾；收到者、送出者/时钟/持物，实际关系见主稿 §6 |
| TradeDay | 0 | 交换收尾；收到者、送出者/时钟/持物，实际关系见主稿 §6 |
| TradeNight | 0 | 交换收尾；收到者、送出者/时钟/持物，实际关系见主稿 §6 |
| TradeItem | 16 | 交换收尾；收到者、送出者/时钟/持物，实际关系见主稿 §6 |
| TradeSpecies | 2 | 交换收尾；收到者、送出者/时钟/持物，实际关系见主稿 §6 |
| BattleDealCriticalHit | 1 | 战后检查；本场 K；有目标后可取消演出 |
| Event | 1 | 事件显式编号；可复用 |
| EventAfterDamageTaken | 1 | 战后 D≥49 只置 R；后续事件编号＋R 才命中 |

合计 57 行、17 个身份有数据、18 个身份无本次顶层样本。35 个身份均在进化方法注册文本中存在；EventAfterDamageTaken 跨两个检查上下文但只算一个身份。

## 2. 默认顶层数据条目

表中数据不证明检查会通过：例如两条 TradeSpecies 因实际比较自身物种而不匹配默认参数；详主稿。

| 来源个体数据节 | 目标 | 方法 | 参数 |
| --- | --- | --- | --- |
| POLIWHIRL | POLITOED | TradeItem | KINGSROCK |
| KADABRA | ALAKAZAM | Trade | 无 |
| MACHOKE | MACHAMP | Trade | 无 |
| GRAVELER | GOLEM | Trade | 无 |
| SLOWPOKE | SLOWKING | TradeItem | KINGSROCK |
| MAGNETON | MAGNEZONE | LocationFlag | Magnetic |
| HAUNTER | GENGAR | Trade | 无 |
| ONIX | STEELIX | TradeItem | METALCOAT |
| RHYDON | RHYPERIOR | TradeItem | PROTECTOR |
| SEADRA | KINGDRA | TradeItem | DRAGONSCALE |
| SCYTHER | SCIZOR | TradeItem | METALCOAT |
| ELECTABUZZ | ELECTIVIRE | TradeItem | ELECTIRIZER |
| MAGMAR | MAGMORTAR | TradeItem | MAGMARIZER |
| EEVEE | LEAFEON | LocationFlag | MossRock |
| EEVEE | GLACEON | LocationFlag | IceRock |
| EEVEE | ESPEON | HappinessDay | 无 |
| EEVEE | UMBREON | HappinessNight | 无 |
| PORYGON | PORYGON2 | TradeItem | UPGRADE |
| GLIGAR | GLISCOR | NightHoldItem | RAZORFANG |
| SNEASEL | WEAVILE | NightHoldItem | RAZORCLAW |
| PORYGON2 | PORYGONZ | TradeItem | DUBIOUSDISC |
| NOSEPASS | PROBOPASS | LocationFlag | Magnetic |
| FEEBAS | MILOTIC | TradeItem | PRISMSCALE |
| DUSCLOPS | DUSKNOIR | TradeItem | REAPERCLOTH |
| CLAMPERL | HUNTAIL | TradeItem | DEEPSEATOOTH |
| CLAMPERL | GOREBYSS | TradeItem | DEEPSEASCALE |
| BUDEW | ROSELIA | HappinessDay | 无 |
| CHINGLING | CHIMECHO | HappinessNight | 无 |
| HAPPINY | CHANSEY | DayHoldItem | OVALSTONE |
| RIOLU | LUCARIO | HappinessDay | 无 |
| MANTYKE | MANTINE | HasInParty | REMORAID |
| BOLDORE | GIGALITH | Trade | 无 |
| GURDURR | CONKELDURR | Trade | 无 |
| KARRABLAST | ESCAVALIER | TradeSpecies | SHELMET |
| SHELMET | ACCELGOR | TradeSpecies | KARRABLAST |
| PANCHAM | PANGORO | LevelDarkInParty | 32 |
| SPRITZEE | AROMATISSE | TradeItem | SACHET |
| SWIRLIX | SLURPUFF | TradeItem | WHIPPEDDREAM |
| TYRUNT | TYRANTRUM | LevelDay | 39 |
| AMAURA | AURORUS | LevelNight | 39 |
| SLIGGOO | GOODRA | LevelRain | 50 |
| PHANTUMP | TREVENANT | Trade | 无 |
| PUMPKABOO | GOURGEIST | Trade | 无 |
| YUNGOOS | GUMSHOOS | LevelDay | 20 |
| CHARJABUG | VIKAVOLT | LocationFlag | Magnetic |
| CRABRAWLER | CRABOMINABLE | LocationFlag | IceRock |
| FOMANTIS | LURANTIS | LevelDay | 34 |
| COSMOEM | SOLGALEO | LevelDay | 53 |
| COSMOEM | LUNALA | LevelNight | 53 |
| SNOM | FROSMOTH | HappinessNight | 无 |
| KUBFU | URSHIFU | Event | 1 |
| RATTATA,1 | RATICATE | LevelNight | 20 |
| FARFETCHD,1 | SIRFETCHD | BattleDealCriticalHit | 3 |
| CUBONE,1 | MAROWAK | LevelNight | 28 |
| LINOONE,1 | OBSTAGOON | LevelNight | 35 |
| YAMASK,1 | RUNERIGUS | EventAfterDamageTaken | 2 |
| ROCKRUFF,2 | LYCANROC | LevelEvening | 25 |

## 3. 地图/天气的具名数据对照

| 地图元数据编号 | 相关字段 | 可以支持的结论 |
| --- | --- | --- |
| 028 | MossRock | 当前图旗标输入可满足此类条件；不证明真实岩石事件存在 |
| 034 | IceRock | 同上，冰岩旗标 |
| 049／050／051 | Magnetic | 同上，磁场旗标；050 另有 DarkMap |
| 021 | Rain,100 | 正常转移天气输入可成为 Rain；实际天气读取仍在检查时 |
| 047 | Rain,0 | 数据声明不等于当前正在下雨；概率分支为 0 |
| 072 | Storm,50 | 随机成为 Storm，类别 Rain；不执行随机验证 |

世界天气 None 不命中五个天气族中除 LevelNoWeather 外的类别；Sun→LevelSun，Rain／Storm／HeavyRain／Fog→LevelRain，Snow／Blizzard→LevelSnow，Sandstorm→LevelSandstorm。只有 9 种默认世界天气；战斗天气标识不是本表输入。

## 4. 固定算术/状态对照

| 前提 | 预期 | 区别 |
| --- | --- | --- |
| 本场替身实损 30＋19，未濒死 | D49 | 个体 HP 损失可以为 0；战后只置 R |
| 混乱实损 10＋友方实损 39 | D49 | 没有必须敌方来源的门 |
| 第一场 48、下一场 1 | 各自 D48、D1 | 非历史累计 49 |
| 当前 HP20，致死伤害被撑住改到 1 | D 增 19 | 实损不是预计伤害 100 |
| 某次逐目标要害共 3 个可计写入点 | K 增 3 | 不是一招记 1；其中可含友方与替身 |
| [A,B,C] 换出 A、新增 X | [B,C,X]；[10,20,30]→[20,30,空]，K[1,3,0]→[3,0,空]，D[0,49,5]→[49,5,空] | 空槽不继承被移出成员，默认 0 和缺失槽不同 |
| 全结果检查开／关 | 开={0,1,2,3,4,5}；关={0,1,3,4} | 前提是进入世界结束通知；准入跳过不是决定 0 这一行 |
| R 真、事件 2 命中后取消 | 触发工具 true；R 仍真、物种不变 | 事件编号不消费；真正提交后才清 R |

## 5. 来源与限制

35 身份字面集合（进化方法注册全文）；顶层物种/形态内容数据对应进化行；地图元数据具名字段；时间/天气/战斗记录消费者见主稿与审计。没有执行参考表达式、模拟器、事件或编译器。数据计数/来源身份、数学向量、人工控制流检查分别登记，不互相代替。
