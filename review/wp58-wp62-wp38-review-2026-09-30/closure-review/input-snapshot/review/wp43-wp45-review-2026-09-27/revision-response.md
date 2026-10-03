# WP43回填、N01同步与WP44／WP45有限修订回应

2026-09-27（Asia/Shanghai）。提取／修订方，不是独立reviewer。依据本目录 [report.md](report.md) 与权威执行细节 [revision-prompt.md](revision-prompt.md)，已读根AGENTS.md及适用目录检查；活动子目录无另行适用AGENTS.md。reference只读，固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

**独立结论保留原样**：批次REQUEST_CHANGES；WP43本体PASS_SCOPED；WP44-R01/R02、WP45-R01三项必修；N01新证据CONFIRMED，实际修订需复核；C01两处维护。WP39／40／41管理回填接受及旧12项关闭继承。本次完成指定回填／修订，不自行把三个必修或N01实际修订标CLOSED。

## 1. 输入固定与意见适用性

每件使用`shasum -a 256`和`stat -f %z`实测，再与本轮input-snapshot逐字节比较。七项必检，加WP40／WP41／self／boundary／主TSV五项补检，**十二件全部MATCH，无漂移，意见适用**；快照未覆盖。

| 对象 | 被审／修订前完整SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/pokemon-rules/wp43-types-accuracy-and-damage.md` | `6021d835ebd2b62eac63062c5475e53501b5e6d46ff94873f2284799cf11ef0e` | 29,511 |
| `specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md` | `b7eae260636adef8e1e301737765c5ab396216f481086aecaab0c42857a1cf67` | 35,014 |
| `specs/pokemon-rules/wp44-effect-coverage.md` | `ea5237d3257e1326876d3aae8d36c9bac003eb9682ad7402b05bc02797b45e39` | 24,809 |
| `specs/combat/wp45-weather-terrain-side-and-position-effects.md` | `2fbe3b6586b41214f02a8e1ec59257dad5dd740f5ce882279497e388f7a8afab` | 34,109 |
| `planning/feature-matrix.md` | `bf77403c9b402f55830a0db482006465d9b74e0e798ab758c80f204e33ab1661` | 47,030 |
| `planning/review-manifest-2026-09-19.md` | `022a35f6d57ca87d33d2dc6d8475db73afa04200b2a94ace85c2990023ebdc14` | 240,319 |
| `review/wp43-wp45-delivery-2026-09-27/delivery-summary.md` | `96b9abf484d4eafa958b81f41c4755ff250e19c240804577a74236eed3027619` | 8,597 |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `07789951f9aaaa7cac82508218a3f58c76caa735e18e4fad9f9a2dcd123a80d3` | 40,547 |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `e6b835af5db676a28b80e7fb1513cf379267b2cdab427c7e9cc916e8e8a4c234` | 31,897 |
| `review/wp43-wp45-delivery-2026-09-27/self-checks.json` | `3c1259dd3f8966282b7880de4bee02b8c7a5bcd8640ed6dae8e729dc6b841113` | 40,415 |
| `review/wp43-wp45-delivery-2026-09-27/boundary-checks.json` | `c20c3cbcf1e0488f899ab8ff389635543efc49a5499f58741456ad481200687a` | 4,122 |
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` | `f9650af5cc4b9d450006844b96436592211721e49a0dba1036df6e8d6e4175f7` | 48,017 |

## 2. BATCH-N01：上游实际校准

**回源结论**：`Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb:542–576` 的无防守、未来攻击、帮助条件，只跳过相应半无敌／天空摔投阻挡，后续仍有skip标志和实际命中入口；`003_Move/003_Move_UsageCalculations.rb:126–154` 的目标处理器受模式破坏者门控制；`007_Other battle code/008_Battle_AbilityEffects.rb:1111–1115,1149–1153` 才把普通命中的基础命中设0。复核支持N01，不存在反证。

**修改位置**：WP40 §5.3 :155及随后N01段、§12.2两条对照、§13追溯与§15版本说明；WP43 §4.3 :89改为独立已确认／上游已实际修订／待传播复核。旧“一方有即命中”的当前保证已改写；相邻未来攻击／帮助的职责也收紧。WP41只改 :10 的上游身份行。


**静态验收**：普通非特殊调用q70、双方命中／闪避0阶、用户有效模式破坏者且无无防守、目标有效无防守，排除其它提前门和修正→目标处理器跳过，r69命中、r70失败；只关闭模式破坏者→普通目标处理器可设基础命中0，普通入口通过。不把普通家族处理器反推为所有特殊入口同样通过。

**保留边界**：这是新证据造成的WP40局部行为简写校准，不称纯状态回填。既有限定Reviewed、旧12项及WP40-R03两标志／PP等合同保留；N01实际差异及直接传播仍待有限复核。未改reviewer原件、未执行命中判定。

## 3. WP43：依授权管理性回填

依报告§2.1，只把A～F已述当前输入／类型相性、普通命中与分层短路、会心、普通伤害阶段／舍入、伤害状态／HP提交及有界特例登记 **Reviewed（限定静态范围，2026-09-27首审PASS_SCOPED；管理性回填）**。头部／§13、F12-01及上游身份同步；被审首版完整身份留在头尾与本回应表，不冒充回填后新字节被审。

WP43 §5到§10之前的会心／基础伤害正文与被审稿逐字节相同，前20条既有数值向量整行相同；第21条N01仅更新审查语境。完整处理器、特殊家族、AI、WP42、浮点扩展与运行前向保留。WP44／45及附表并未因此回填Reviewed。

## 4. WP44-R01：22条具体合同与精确索引

**回源结论**：定点读取`Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb`的16条泛化项、破壳与五集合族；并查`004_Move_BaseEffects.rb:78–155,176–283`的正常／伤害附效分流。确认缺口在行为参数／分支，114项身份集合本身无错；不需重提取或削减范围。

**修改位置**：主稿 §7.1 :158新增K01–K22，完整给对象、请求量、阶段／次序、前门、部分成功与实际入口；§7导言改为这些规则是复杂合同的主出处；附表16泛化行、破壳及五集合行共22行链接稳定锚点。原67条普通参数的对象／量文本逐行保持，114/31/23全部168项审计身份及起始行保持。


具名补充包括：

| 合同 | 主要补充／验收 |
| --- | --- |
| K01–K08 | 蜷缩防御＋1、充电特防＋1且先置计数2、轻量化速度＋2与重量比较、变小闪避＋2、聚气设2、成长双攻量、背水五项顺序和拘束聚合、愤怒建立与受击升攻分开 |
| K09–K12 | 目标攻击＋1的变化／伤害入口、忽略替身特防＋1、装饰攻→特攻各＋2、忽略替身攻击−1与普通族对照 |
| K13 | 重力正值：本招整数基底81×3/2=121.5，先截断为121，再交WP43普通倍率阶段；防御下降请求−1 |
| K14–K16 | 诱惑特攻−2与性别／迟钝分支、青草基底61/2=30.5→31且不加目标接地门／降速−1、沥青新标记时的失败门与下降提交顺序 |
| K17 | 破壳精确顺序：防御−1→特防−1→攻击＋2→特攻＋2→速度＋2；至少一项可变才不整招失败，提交逐项再查，部分成功不回滚 |
| K18 | 同侧盟友攻防：排自身／对侧，攻击→防御各＋1，普通逐目标与部分成功 |
| K19／K20 | 正负电池含符合条件自身与同侧，不含对侧；分别攻击→特攻或防御→特防各＋1。UserSide直接遍历预选池，区别于普通逐目标成功检查；由目标数据决定，非按世代自动假定 |
| K21／K22 | 双方草成员可含自身；耕地排浮空和半无敌，攻→特攻各＋1；鲜花防守仅排半无敌，防御＋1；各自逐目标资格／提交给出 |

**静态验收**：主稿J01–J07覆盖两处独立威力取整、无视替身对照、破壳五项次序、五集合族及UserSide对照。UserSide对照额外定点核对`010_Data/001_Hardcoded data/017_Target.rb:1–93,168–172`与成功检查:320–333：UserAndAllies的targets_all为假，戏法防守可拦非自身盟友；UserSide通道直接遍历预选池，不补跑同一逐目标检查。22个锚点全部存在且被附表引用，没有靠英文名称／数字解释规则。

**保留边界**：不改WP43已通过的公式；K13/K15只提供本招基底输入替代。普通参数、其它正确复杂族、域外负责包、数据集合与起始行保留。没有转译参考函数或补造运行结果。

## 5. WP44-R02：中央镜甲与招式层预检分开

**回源结论**：`003_Move/004_Move_BaseEffects.rb:238–267`的普通多项预检，及`006_MoveEffects_BattlerStats.rb:1388–1417`毒液陷阱预检均不检查模式破坏者门；先要求目标某拟降项不在下限且来源能通过该项下降查询，找不到就整体放弃。之后才回到`002_Battler/005_Battler_StatStages.rb:123–173,198–224`的中央查询／提交；这里的镜甲反射才受模式破坏者关闭。

**修改位置**：主稿 §5.2原概括改为“中央分支”，§5.3 :114专门给多项预检；§7普通多项／特定集合摘要与§9失败说明同步；新增M01–M03。附表双项攻防、攻特攻及毒液陷阱三行连接§5.3，不改其参数。


**静态验收**（双方存活，模式破坏者开，目标有效镜甲，无其它拒绝）：

| 调用 | 输入 | 预期 |
| --- | --- | --- |
| 普通攻／特攻各−1 | 目标0／0，来源−6／−6 | 目标中央资格可过，招式预检找不到可降来源项，双方不变 |
| 同上 | 目标0／0，来源0／0 | 预检过，中央不反射；目标−1／−1、来源0／0 |
| 普通单项攻击−1 | 目标攻击0，来源攻击−6 | 没有多项预检；中央忽略镜甲，目标−1、来源仍−6 |

毒液陷阱同类预检适用于其攻／特攻／速度三项和中毒预选集合，不把两项向量直接冒充三项全被拒绝的输入。

**保留边界**：中央单纯／唱反调／上限等正确部分保留；不扩成所有镜甲不可忽略，不向reference补模式破坏者守卫，不展开WP48/49完整族。

## 6. WP45-R01：最后行动失败门

**回源结论**：`003_Move/004_Move_BaseEffects.rb:448–480`在侧型免连续抽签之后仍检查最后行动失败，失败把保护计数复位1；`002_Move_Usage.rb:106–115`精确定义其它成员须登记UseMove／Shift且本轮未动；`008_MoveEffects_MoveAttributes.rb:950–971`确认快速／广域使用共同侧型入口。

**修改位置**：WP45 §6.2侧保护目录、§7.2 :132、§13失败摘要；新增S06/S07，self／boundary同步。旧“免抽签”正确结论保留，补明不等于免最后行动门。


**静态验收**：世代8、侧标记假、保护计数9，无其它合格未动UseMove／Shift（即使另有物品／换人选择者）→不抽连续保护随机，但失败、计数9→1、侧标记仍假；另有一名符合者且其余前门通过→成功设真、9×3=27。旧世代抽签分支保留。

**保留边界**：不修改已支持的保护消费、天气／场地／火海／位置生命周期；WP45§3–5、§7.1及§7.3至§10前的已支持段落与被审稿逐字节相同。

## 7. C01与必要传播

- WP44普通／剧毒行明确**仅statusCount>0的剧毒**推进Toxic；普通毒不增。V11/V12既有数值保持，新增V16普通毒累计0保持0。
- WP45取证范围由请求窗口尾数统一为实际 :781，与self有效范围一致；没有重提取WP42。
- WP40改后立即实测，WP41仅上游身份行级联；WP43回填后固定，再WP44主稿／附表，最后WP45。十条受影响完整哈希绑定逐条匹配。
- 矩阵只更新F12-01/02/03；WP43子范围Reviewed＋Inventoried，WP44／45继续ReviewPending＋Inventoried并具名修订编号。self／boundary／摘要更新v2，旧声明加revision_history，旧回填diff的验证只作v1历史，不冒称能重建本轮新稿。

## 8. 当前固定身份与十份差异

下表全部为写入后的实测值；WP43管理回填、WP40证据校准与WP44／45修订身份分开。原首版／回填前身份留在§1和manifest替代链。

| 当前文件 | SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `ad4718722897ef448623fb2bdcd7e9e8ca9a51538a5015edc331fcae50516654` | 42,476 |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `42878fac04b7ba5e195663f183fb484489200bab8ef5dc17333b0c0525b14085` | 31,939 |
| `specs/pokemon-rules/wp43-types-accuracy-and-damage.md` | `0cd9958c256ef2caf7d6f9933127f35e5644131a3a97ed79d46998c6bcc15688` | 30,543 |
| `specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md` | `85e17c6c15225040eb5dd5f38503bbcac6c8fd96916f40270e3c989e86559311` | 49,950 |
| `specs/pokemon-rules/wp44-effect-coverage.md` | `47bd80e20c877e612bb99e6929cf46b2efe7d87d94862760e9871234eecac3ef` | 27,133 |
| `specs/combat/wp45-weather-terrain-side-and-position-effects.md` | `f92b0f3cfa807d0c9a069fb586cde3673f878d4762dbede3425b08b86f06f35b` | 35,823 |
| `planning/feature-matrix.md` | `b230d1d7840b31923c741d439c2344990c18e00108a45801fdc45b6fd5078cc7` | 47,092 |
| `review/wp43-wp45-delivery-2026-09-27/self-checks.json` | `307d1ff0d54d9c1ddbcf8ee10f6161e6eff044cb5d486352b3acab643313004d` | 56,423 |
| `review/wp43-wp45-delivery-2026-09-27/boundary-checks.json` | `21abfe14138ed5e2fcd5ba3d3f0b499d192326e970c4495a905fcafa0098ac4e` | 6,629 |
| `review/wp43-wp45-delivery-2026-09-27/delivery-summary.md` | `39275cb4291ba561557e2ee014cb5c1d5236836bcd615d981b8a31878d8b2d7d` | 9,790 |

十份新diff以本目录input-snapshot为基准；含六份规格／附表、矩阵、摘要、self与boundary。已独立按差异块在内存重建，10/10与当前目标逐字节匹配，不向快照或reference应用补丁。

| 差异 | SHA-256 | 字节 |
| --- | --- | ---: |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp40-n01.diff` | `8c01d8b98251ac7e85fcf48e9a354b7129855e94355a65df2df920385dcfec6f` | 7,407 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp41-reference-sync.diff` | `f231032c94a6ddd90ffdd2c76e3c406b94da536d3ab6d38b723b379be2211dac` | 2,806 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp43-reviewed-backfill.diff` | `888681b4087f9f4cebc75c71fc6b737b144f354c9e221ca82acc7e9e31dc6132` | 7,853 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp44-revision.diff` | `c01fc160de111374358d1b8aac71dcfcd178410da14f2192bb3fed7e984c55b2` | 30,434 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp44-effect-coverage.diff` | `634ac62a326307724db91374afafdd589da47e85fbdc5cd84d2590d6602d69ab` | 20,722 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp45-revision.diff` | `c7bfed7488b3a3dfdadc8a59bc71cdf266f8a99d781c9fec5d09a0ae7d0978a9` | 14,233 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/feature-matrix.diff` | `c1dfb980e895a9a883b4ae138121fad873edd217f795460cfd3207a3a1c0072e` | 5,015 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/self-checks.diff` | `8376bae01dde0c2c92e7dfaa31266164b9168d3fe1d81607b0b84cce9ef16bbf` | 29,928 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/boundary-checks.diff` | `b85e7836549f856b9301dc6da136cda92cba25cc2d546254a08bd51e1aa164c7` | 8,872 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/delivery-summary.diff` | `6aeb2ec62d3fc62ecfba2055d48d05926363dbaea983dfb81e1252de237f4940` | 18,490 |

本轮13个源文件的定点范围、完整哈希／字节与固定commit核对见 [self-checks.json](../wp43-wp45-delivery-2026-09-27/self-checks.json)。首稿源范围作为继承证据，不冒称本轮全文重读；新增独立算术三项121／31／27已实测。公式、入口、失败摘要、向量与索引已作静态对照，**这不是独立修订通过**。

登记本轮reviewer材料12份、本回应及10diff；主TSV v24沿用353旧行，新增23行；manifest第四十九轮更新当前表／记录／替代链／轮次。manifest／TSV不自哈希；登记完成后的全量身份、短标签、缺失重复、集合、相对链接、JSON、快照与reference Git终检由最终交付消息报告。

## 9. 停止点

仅送 **WP44-R01/R02、WP45-R01、BATCH-N01、C01及直接传播**有限复审，然后停止。WP43按独立批准回填；WP44主稿／附表与WP45继续ReviewPending，不自批。当前限定通过集合为 **WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43、WP59–WP60**。

未启动任何新包，未创建任务／并行Agent、未发reviewer消息、未提交／推送。未运行游戏、参考Ruby／表达式、解释器／事件脚本、生成器、编译器、转换器、插件或真实网络；未操作地图／存档／真实输入。仅自有文本、哈希、集合、JSON、diff和独立算术，不实现新框架。Demo、宿主、媒体、插件、U01–U10及WP78→WP79→WP80出口保留。
