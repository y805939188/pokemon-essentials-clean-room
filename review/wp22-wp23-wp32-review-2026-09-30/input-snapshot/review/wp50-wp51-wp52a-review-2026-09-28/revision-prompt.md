# 给提取模型：WP50／WP51／WP52-A 首审有限修订

直接执行，无需再问是否继续。你是提取方，不是独立reviewer。本轮只有两个必修编号、C01和直接传播；允许WP51限定范围的管理回填，**不启动下一批**。

先完整读本目录 [report.md](report.md)、根及适用AGENTS.md、当前manifest及本批六件主稿／附表，按原编号逐项回源核实。若有反证，给完整固定来源、行号、具名输入／结果，不只照改结论；无反证则作最小修订，不重做首审。

工作区 `/Users/dingshinn/Desktop/pokemon-framework-reference/`。reference `reference/pokemon-essentials/`只读，commit固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

## 1. 固定输入与范围

独立结论 **REQUEST_CHANGES**：必修 **WP50-R01、WP52-A-R01**。WP51 A～E主稿及默认数据附表 **PASS_SCOPED**；BATCH-C01两处为非阻塞维护。前批三条旧摘要同步、C01和WP46／47-A／47-B回填已接受，已关闭结果保留，不再重开。

改动前复算下表完整SHA-256／字节，与本目录 `input-snapshot/` 逐字节比较。一致则直接继续；若有漂移，先登记实测差异与意见适用范围，不覆盖快照、不凭短前缀补全哈希，不把新版本冒称已审。

| 文件 | 被审首稿完整SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md` | `937551e00ec61a8a807bfa197ece1e2f91b6b5f91f620375e6c14ea900e9027a` | 29,336 |
| `specs/pokemon-rules/wp50-held-item-effect-coverage.md` | `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686` | 13,855 |
| `specs/combat/wp51-ai-action-selection-and-skill.md` | `1174d485f2648682cbd98a446044dfd487bab694d7afdb94e309f3d3fe4a6972` | 25,064 |
| `specs/combat/wp51-ai-decision-defaults.md` | `f3837410a9c41617495d2691e69f2e7baa11e7e5c3d7521f618a0f1472ad6c09` | 4,811 |
| `specs/combat/wp52-a-generic-numerical-and-status-evaluation.md` | `f7f400c642d77f29c5411ac156fe0e49716848b87ed232b02b8d418e1c67126a` | 46,332 |
| `specs/combat/wp52-a-evaluation-coverage-and-data.md` | `b620a868091aff4e1bb519f18e89698688eef279dbb020f828e2a0dfa25739c6` | 58,177 |
| `planning/feature-matrix.md` | `35935419cb9648d4bfd60665d7a7719a9d79230b9d7585bf852a9120ef87ab30` | 49,556 |
| `planning/review-manifest-2026-09-19.md` | `34308ae1293a9ac7a272b8e93ef7e82999e7aa3a15b53a2d50ab7b6b6404de50` | 315,913 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/delivery-summary.md` | `0df9331d437df132728bc58cb36af53d16d09c4f787e99445db3de56c483029b` | 6,554 |

self／boundary／主TSV等配套完整身份在本目录 `input-manifest.json`／`current-hashes.tsv` 中，也应预检。独立实测587条manifest、491条TSV与589项固定输入匹配；原18份回填diff可重建、548＋521项旧快照未变。这些保护原件和身份，不替代行为验收。

## 2. WP50-R01：低HP果参数方向

回读：

- `Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb:212–221,399–409,434–449`。
- `Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb:364–404`及混乱果的真实调用者；只核本问题及直接传播。

核心合同：食果资格先行；四分之一以下可；四分之一以上至半血时，**false参数表示不用要求GLUTTONY，true才要求其有效**。false不是关闭半血扩展。保留普通物品有效性、canHeal／食果与forced各自消费者门，不改成“半血就无条件使用”。

最小修改位置：WP50 §4:74参数解释、:79 ORAN／SITRUS、:80五混乱果世代门、V05:167、self和摘要的“四分之一门”概括及直接同句传播。恢复量分母／RIPEN顺序、Nature混乱、颊囊／共生、回收与还原记录不随阈值修订重写。

分入口给清楚的合同：

1. ORAN／SITRUS非forced传false：半血可触发，毋须贪吃；仍查可治／可食与普通有效性。
2. 五混乱恢复果非forced：世代≤6传false，半血毋须贪吃；世代≥7传true，无贪吃四分之一、有有效贪吃半血。世代≤6/7/≥8恢复量仍分别H整除8/2/3。
3. 其它默认true的低HP调用者保持原门；forced由调用者决定绕哪些门，不可一概说强制忽略所有资格。

静态验收（无额外恢复／消费连锁，普通物品有效、可治可食，Nature效果另算）：

| 输入 | 修订后期望 |
| --- | --- |
| ORAN，H100，HP26，无／有GLUTTONY | 均触发，＋10至36 |
| ORAN，HP50／51 | 50触发至60；51不触发 |
| SITRUS，H100，HP50，无GLUTTONY | 触发，＋25至75 |
| 混乱果，世代6，H100，HP50，无GLUTTONY | 触发，请求12，HP62；混乱按Nature和中央资格另查 |
| 混乱果，世代8，H100，HP50，无／有效GLUTTONY | 前者不触发，后者请求33至83 |

保留现有RIPEN数量向量和forced满HP等对照。可以加入普通食果资格被紧张感拒的对照，不能由半血门修正取消食果门。不要改WP28主动道具或WP51主动药品估量，它们是不同入口。

只做自有常数算术与手工条件核对，不调用参考helper、不用Ruby／生成器，不转译成可执行模拟函数。

## 3. WP52-A-R01：墙类估伤的人数口径

回读：

- `Data/Scripts/011_Battle/005_AI/011_AIMove.rb:336–355`。
- `Data/Scripts/011_Battle/001_Battle/001_Battle.rb:458–460,474–475`。

把WP52-A §3.2:85“侧规模>1”改为 **目标当前同侧存活场上人数>1**。计数含目标及其它非空、未濒死的同侧场上成员；名义布局、已倒下者、空位和后备不等价。极光幕／反射壁／光墙三个分支同步，不只改表中的一个名字。

保留中等技能门、预计非会心、无穿墙能力／不忽略墙、极光幕优先与物理／特殊类别门；不重新提取真实WP43墙规则，不改已确认的负会心下标、命中96或普通基础公式。

新增静态对照：同一名义双席布局，中等技能，普通单目标L50/P80/A100/D100，会心级0（无幸运咒／禁会心覆盖等导致AI负下标特例），无本系／天气／其它倍率，相应墙正值且未绕墙，墙前量37。两名同侧存活→R(37×2/3)=25；另一成员倒下／空位、只剩目标→R(37/2)=19。反射壁配物理、光墙配特殊、极光幕按对应普通伤害分别定位；不需要运行AI评分或战斗。

同步主稿、self／boundary与相关摘要的当前断言；旧错误断言只保留在明确历史语境，不让字符串自等充当新验收。能力／物品的已接受修正次序和未知组合边界不变。

## 4. BATCH-C01及WP51限定Reviewed回填

两点随本轮维护，不重做WP51：

- WP51:40改清存在性：“存在一个后备、其中一招伤害招、对至少一个对手未被能力吸收近似阻挡”。源`002_AI_Switch.rb:476–496`；不是要求某招同时打穿全部对手。可给双对手一吸收／一不吸收的局部对照，不扩大到完整目标合法性或真实伤害。
- WP51:68把“气体”明确为CLOUDNINE／AIRLOCK天气抑制，加UTILITYUMBRELLA分列；源`010_AIBattler.rb:60–65`。不把NEUTRALIZINGGAS直接写成这里的清天气判断，保留本段其它按能力身份而非统一有效性的近似差异。

WP51主稿和数据附表可回填 **Reviewed（限定静态范围，2026-09-28首审PASS_SCOPED；管理性回填）**，链接本轮报告§4，范围为：AI控制／技能与标记、换人和替补近似、主动道具偏好、Mega登记、候选目标／加权选择／回退及具名失败边界。F12-07同样限定Reviewed＋前向Inventoried。C01与状态回填分开列差异。

保留被审WP51主稿 `1174d485f2648682cbd98a446044dfd487bab694d7afdb94e309f3d3fe4a6972`／25,064字节及附表 `f3837410a9c41617495d2691e69f2e7baa11e7e5c3d7521f618a0f1472ad6c09`／4,811字节；回填后的新字节不冒称本轮原始审查对象。

WP50、WP52-A仍 **ReviewPending（各自具名范围，首审有限修订后再送）**。WP51通过不代表WP50–52整批连续通过；WP51依赖WP50仅有本批持物交界前向参照，不能删去这次真实剩余问题。

## 5. 保留范围、级联与材料

本轮不动已接受的完整注册分工、数据表、其它能力／物品量值、AI基础能力评级和数值／状态／阶级反例。32族196持物身份、AI334个A登记出现及B/C边界、三个后续重复键、101条原场景的其它接受部分继续保留；身份集合正确不代表本轮两条错误也已正确。

按WP50修订→WP51维护／回填→WP52-A修订及上游完整身份级联。当前WP52-A对WP51引用改成“已限定通过的回填后版本”，对WP50仍注明“批内修订稿，尚未外审”，不得因批内自检将WP50标为已审。所有附表绑定和依赖字节数据实重测，不只替换短标签。

在本轮目录 `review/wp50-wp51-wp52a-review-2026-09-28/` **新增**提取侧 `revision-response.md` 和 `revision-diffs/`，基准为本轮 `input-snapshot/`。逐原编号记录亲自回源结论、修改位置、输入／输出验收、传播及保留边界。旧reviewer报告／提示／checks／快照、旧回应／差异原件不能覆盖。

更新自有当前交付摘要、self／boundary、矩阵子范围、manifest当前表／审查记录／历史替代链／新轮次及主TSV `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv`。保留被审首稿完整身份；补登本轮reviewer材料，TSV不丢旧行。manifest不自哈希，TSV不收自身，终值在交付消息实测报告。

完成后全量复算哈希／字节／短标签、缺失／重复、路径集合、相关链接／JSON、批内绑定、原reviewer／快照保护与reference HEAD／Git状态。旧值只留在历史或被审语境；当前值逐字对应磁盘。

## 6. 送审与停止

仅送 **WP50-R01、WP52-A-R01、BATCH-C01、WP51管理回填差异及直接传播**有限复审，然后停止。不重做首审、不新增其它包；**不启动WP52-B/C或下一批**。前批N01/N02/N03及C01已闭合，不再次修改那些已接受行为。

reference只读、不切基线。禁止运行游戏、参考Ruby／表达式、解释器／事件脚本、生成器、编译器、转换器、插件或真实网络，不操作真实地图／存档／输入。只允许安全自有文本、哈希、集合、JSON、diff和独立常数算术；不逐行转译参考过程取得期望。

不设计或实现新框架，不复制源代码／长表达式／逐行伪代码，不创建并行Agent或其它任务，不向reviewer发消息，不提交／推送。Demo、宿主、媒体、插件、U01–U10及WP78→WP79→WP80出口继续保留。
