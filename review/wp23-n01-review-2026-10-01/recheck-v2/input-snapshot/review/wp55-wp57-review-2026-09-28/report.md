# WP55／WP56／WP57 独立首审报告

2026-09-28固定输入，2026-09-29完成；独立 reviewer；reference 固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

**结论：REQUEST_CHANGES，暂不进入下一批。WP55五项、WP56五项、WP57三项，共13项必修。** 三包保持各自ReviewPending；本轮旧WP52-B管理回填接受，旧行为通过不撤销。继承C02的artifacts表和Q41已修，但当前packages中还有两条旧身份，列非阻塞维护。

本轮读完三份新稿、七个主要行为源文件及必要直接消费者。以下是实际回源发现，不以提取侧“无硬失败”代替外审；没有运行Ruby、参考表达式、游戏、UI、生成器、保存或网络。

## 1. 固定输入

| 对象 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| WP55主稿v1 | `d5ee5ba7b3f48fc14c7552248d865d560b64a626624e96e6cbf64d1f9916b1dc` | 21,873 |
| WP56主稿v1 | `fde119eaca1bd3543571b76343972a26903da905b02e30ebe55ed3c7cf50145b` | 16,917 |
| WP57主稿v1 | `e510f8402a2d253ac78cf97bb6eeb5d2bd04b196f9ec5da5437567d0c33f0858` | 11,933 |
| feature-matrix | `0a726a5f3b57e81652fe87c888925a632fbcb0b61a6cf551ceab0abdd2dc90f4` | 51,444 |
| manifest | `bca20e3c4aa9e62b9d1cd8848a123d84e3231d3f1b37d91c7ec2ab26545a0741` | 376,932 |
| 本批交付摘要 | `6217eeb05793b2b0a6620a1bb06b30ad5d51cc24e59d74c6f43c0e1b18568bad` | 4,970 |
| 本批self-checks | `72396ffb1676cce44cb43dab3ec9f0ec8a8c36cd939febde402e08ca834d3d30` | 17,131 |
| 本批boundary-checks | `5839c099ef7fe3ee675f9b880a853c6fb043e52acb8b4baaa07c0186b07ebcd8` | 7,571 |
| 主TSV v32 | `edcc4b54979e635f95a70324d5b501a03a03bc865441acab120878c2ad26274f` | 83,890 |

实际固定707项输入。全部路径／完整身份见 [current-hashes.tsv](current-hashes.tsv)、[input-manifest.json](input-manifest.json)，副本见 [input-snapshot/](input-snapshot/)。当前705条manifest、609条TSV的完整哈希／字节／短标签匹配，无缺失／重复。相对上一轮有11个原有文件变化，完整差异在 [changes-from-previous.diff](changes-from-previous.diff)。身份匹配不表示行为正确。

以下源码路径均相对 `reference/pokemon-essentials/Data/Scripts/`。为缩短定位：

- **Challenge**＝`018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb`。
- **Data／Choose／Swap／Battles**＝同目录 `002_Challenge_Data.rb`、`003_Challenge_ChooseFoes.rb`、`005_UI_BattleSwap.rb`、`004_Challenge_Battles.rb`。
- **Palace／Arena**＝`011_Battle/008_Other battle types/003_BattlePalaceBattle.rb`、`004_BattleArenaBattle.rb`。

每一R项的被审文件完整哈希均以上表相应主稿为准；新版本行号须重新定位，不复用为新稿身份。

## 2. WP55：五项必修

### WP55-R01：会话决定与单场决定、暂停标记、保存条件必须分层

**位置**：[WP55第32行](../../specs/combat/wp55-facility-session-and-restoration.md:32)、第44–46、59–63、113行及相关状态机／不变量。

**证据**：Challenge:95–104、131–132、205–228、243–267、275–281；Battles:64–96。单场包装把战斗返回码放入自己的局部决定，最终返回“是否胜利”；它不写会话的决定，也不自动调用会话加胜。会话决定由独立设置入口写入；加胜需显式调用。暂停只置resting真，不清inProgress。开始把会话决定设0后仍保存，暂停／继续也可以在决定0时保存；只有结束分支按决定非0决定是否保存。

**影响**：现稿“决定由单场／裁判／条款写入”“暂停与进行中互斥”“未决定会话不落盘”会导出错误的状态机、终局和持久化条件。W23已经写暂停不影响进行中，与不变量直接冲突。

**最小修订与验收**：将单场结果、会话决定、显式加胜／加交换、进行中和暂停分别列出写入者。对照：会话开始后决定0仍请求保存；暂停后`inProgress=true/resting=true`；单场胜利返回真而没有外部推进调用时，会话决定和胜场不自动变；显式加胜才推进轮次／胜场。实际接待事件未提供，不补造自动事件序列。

### WP55-R02：空报名和未开始结束不是“无写入／空操作”

**位置**：[WP55第50行](../../specs/combat/wp55-facility-session-and-restoration.md:50)、第51–54、104、125行，W11。

**证据**：Data:38–49；Challenge:200–203、225–228、270–281、292–303；`015_Trainers and player/001_Trainer.rb:9`。空列表在此语言中是真值，若调用者确实交回空列表会写报名引用；随后开始时也会替换玩家队伍为空列表。取消nil不覆盖已有报名值，不能在没有“旧报名为空”前提时断言之后开始不替换。结束先无条件把原队伍字段写给玩家，再检查是否进行中；新建／重置状态的原队伍为nil，因此未开始就结束会把玩家队伍设nil，绝非空操作。取消的条件恢复与结束不同。

**影响**：会丢失空列表／nil／旧报名的区别，并把真实队伍写入隐藏成安全无操作。

**最小修订与验收**：分普通UI可达结果与直接工具边界，不声称正常多选必能返回空列表。静态对照：直接提交`[]`后开始→玩家队伍就是该空引用；取消nil且此前无报名→不替换；取消nil但已有报名P→保留P，之后开始仍可替换为P；未开始且原队伍nil时结束→玩家队伍nil。明确保存原队伍是保留引用，不凭“快照”补深复制。

### WP55-R03：保存返回false与未捕获异常的后续状态不同

**位置**：[WP55第126行](../../specs/combat/wp55-facility-session-and-restoration.md:126)、§2.4／异常段。

**证据**：Challenge:225–228、258–281、306–318；`003_Game processing/001_StartGame.rb:111–124`。Game.save会捕获IOError／SystemCallError并返回false；设施调用没有据该false回滚。暂停／继续保存助手仍会执行后续地图、坐标、朝向恢复。只有未被Game.save捕获而向上抛出的异常才会跳过这些恢复语句；此助手没有ensure。

**影响**：“失败会向上传播”的统一表述既漏掉静默失败，也错误预测地图临时位置何时残留。

**最小修订与验收**：分别记录成功、返回false、未捕获异常。保存false时进行中／暂停／队伍等先前写入保留，暂停助手恢复临时地图位置；未捕获异常时这些临时位置可能未恢复。开始以保存调用收尾，可返回false却已经处于进行中。沿用WP09的保存本体合同，不重写或重审WP09。

### WP55-R04：正常字符串挑战标识会使data查询先失败

**位置**：[WP55第19行](../../specs/combat/wp55-facility-session-and-restoration.md:19)至22行、第43行。

**证据**：Challenge:18–35、79–82、139–142、172–174、324–343。set按字符串正则读取double／factory／open，start把同一标识存为当前挑战。进行中data查询却先把当前标识与整数0比较；字符串标识在此比较处失败，不能保证返回记录副本。非进行中路径会先短路返回nil。类型记录构造仅初始化六个胜场／交换计数；register没有将所接收的double、人数、类型、mode写入该记录的同名字段。

**影响**：把参数解析／即时规则生成误记成持久配置登记，并把会失败的查询描述成安全的显示快照。

**最小修订与验收**：分开set保存的参数、register实际副作用、类型计数记录与data查询边界。输入“进行中，当前挑战为正常字符串标识”→比较阶段失败，不到clone；非进行中→nil。配置参数可参与即时规则生成，不因此宣称类型记录字段已填。不要修参考比较或假造未见的配置写入者。

### WP55-R05：零长度抽样不能等同空区间异常；W06走错生成分支

**位置**：[WP55第45行](../../specs/combat/wp55-facility-session-and-restoration.md:45)、第87、91、121、124行，W06／W08及对应self断言。

**证据**：Choose:26–33、39–80；`001_Technical/002_RubyUtilities.rb:366–387`。抽取只把缩放长度交给全局rand，数值参数转给保留的Kernel.rand；零长度没有本地拒绝。标准Kernel.rand的数值0语义是给出`[0,1)`浮点值，并非Random实例的空区间错误。不得把后续内容索引／缺记录的失败提前到这一步。这里是宿主方法契约与包装分派的静态推导，未调用rand。

W06输入“名单5、建议3”，却写“名单不超过建议数，按原位置生成3”。实际5>3进入有放回重抽／整体校验分支。真正短名单（例如2≤3）按原顺序全部生成2只并直接返回，不补齐、不再作该循环的整体校验。

**最小修订与验收**：长度0的抽取不得声明当场因空区间报错，应说明非整索引及后续消费风险；空表开始也不能统一断言在名单抽取立即失败。短名单2/建议3与长名单5/建议3成对列出，分别验证“2只原序直接返回”和“随机选3直至合格”。保留真实的去重／合法性重试无上限边界，勿按期待给参考补验证或改随机入口。

## 3. WP56：五项必修

### WP56-R01：Palace真正的第二阈值是2A+D，不能按三列概率直接抽取

**位置**：[WP56第25行](../../specs/combat/wp56-palace-and-arena-variants.md:25)、第61–68行，P01–P03及self前三组Palace常数。

**证据**：Palace:105–139先把防御边界暂存为A+D，比较时又加一次A；实际抽样门为`r<A`、否则`r<2A+D`，r在0..99。原始25×3两表抄录正确，但原始表行不等于生效的攻／防／辅比例。

**静态反例**：HARDY基准A61/D7，第二门129，实际61／39／0；r68仍防御。SASSY压半A22/D20，第二门64，实际22／42／36；原P02还把基准88／6误作压半行。GENTLE压半A90/D5，第二门185，实际90／10／0；r95仍防御。

入口直接回归：`011_Battle/001_Battle/009_Battle_CommandPhase.rb:42–64`在玩家安可正时就先转普通自动选招，不以“全槽均不可选”为唯一条件；Palace自动入口返回后也不会继续打开同次普通选靶菜单。AI在`005_AI/001_Battle_AI.rb:48–68`的入口不同。目标−1的执行时解析不等于菜单选择。

**最小修订**：保留原始表，明确实际阈值与有效分布，修P01–P03／自检；把玩家分流和AI直接抽样区分。验收用上述边界与“玩家安可且仍有可用槽”对照，不执行选招或重写成理想概率。

### WP56-R02：压半不是整场永久，换入初始化会清除

**位置**：[WP56第57行](../../specs/combat/wp56-palace-and-arena-variants.md:57)、差异表第118行、P08。

**证据**：Palace:142–164只说明同一当前战斗者已置真就不重复检查；`011_Battle/001_Battle/005_Battle_ActionSwitching.rb:274–278`换入调用初始化，`002_Battler/002_Battler_Initialize.rb:60–62,93–127,234`明确把Pinch置false，且该写入不在接力保留分支内。

**最小修订与验收**：同次在场恢复HP不会直接清压半；换出再换入按初始化清false，接力也不保留这一标记。高于半血换回后使用基准表，直到再次满足回合末检查。保留未睡／未倒下和不超过整数半血门，不把局部不复位扩大为整场不复位。

### WP56-R03：AI选中最佳后备的早返跳过“刚换过”标记

**位置**：[WP56第77行](../../specs/combat/wp56-palace-and-arena-variants.md:77)至79行及对应换人状态说明。

**证据**：Palace:184–243，特别是230–235。概率分支决定换人且有最佳候选时，登记后立即返回真，跳过后面的justswitched赋值。只有到达后段才将它写为shouldswitch，再尝试首个可换成员。不能声称“无论结果都会记录刚换过”。

**最小修订与验收**：按早分支、概率最佳早返、后段失败／回退分列。原标记false、概率命中、最佳后备存在→成功登记且标记仍false；灭亡计数1→到后段标记true并找首个合法后备；后段shouldswitch=false→标记false。保持原概率常数和状态奖励，不把成功登记自动等同下一轮必减60。

### WP56-R04：Arena每回合skill槽是覆盖值，只有回合末才累加到总技分

**位置**：[WP56第85行](../../specs/combat/wp56-palace-and-arena-variants.md:85)至91行，P14／P15及差异表。

**证据**：Arena:12–35用赋值写skill，失败但protected时不写；清理保留旧skill；Arena:127–133才将此槽加进侧累计。`001_Battle/010_Battle_AttackPhase.rb:176–182`每回合全清；`002_Battler/007_Battler_UseMove.rb:248,431–437,516`给状态、相性及结算时点。第295–300行整体失败可早返，并不经过516；`pbEndTurn:97–114`也不补这次结算。

**影响**：原稿把同回合多次行动算术累计，并把每次失败都当成即时结算，会错误预测技分和三回合判断。普通战斗同样创建／更新SuccessState（`001_Battle/002_Battle_StartAndEnd.rb:109–117`），Arena的专用性在消费它的评判，不在对象只存在于Arena。

**最小修订与验收**：同回合已结算+2再结算−1→槽为−1，不是+1；随后一次protected失败→仍−1；下一攻击阶段清0；回合末仅把当前槽加到Arena总分。再给一条“最后行动在整体失败门早返，之前skill0，未到结算入口”的对照，不能自动记−2。记录实际到达时点，不为参考补结算。

### WP56-R05：Arena每项胜负是2/0；心分负项是具名集合

**位置**：[WP56第85行](../../specs/combat/wp56-palace-and-arena-variants.md:85)、第97、102–120、134行，P13／P17及self总分常数。

**证据**：Arena:142–176初始化两侧分项为0，不相等仅胜方写2，败方仍0；相等才各1。界面227–257、320–345显示相同总分。因此两胜一负为4比2，不是5比4；全相等仍3比3。Arena:96–109的心−1只有ProtectUser、UserEnduresFaintingThisTurn、FlinchTargetFailsIfNotUserFirstTurn，不能扩为全部“守住类”；其它保护变化招按变化类别为0。

此外Arena:183–196的HP置0会经`002_Battler/001_Battle_Battler.rb:107–109`写穿到持久个体，不能用源码注释衍生“非真实HP写入”。它是裁判直接置零，而非普通伤害计算／受击流程。

**最小修订与验收**：修分项表、总分和P17；保留平局1/1。普通Protect与另一保护变化身份成对核心分−1／0；裁判失败者战斗HP和持久HP均归0，和普通伤害事件分开。此项不要求改通用WP39／42写回规则。

## 4. WP57：三项必修

### WP57-R01：Factory对手成员没有继承NPC训练家属主

**位置**：[WP57第53行](../../specs/creature-rpg/wp57-factory-rentals-and-swaps.md:53)、第61行、F15；WP55第96行的对手概括直接传播。

**证据**：Choose:154–158对所有Factory候选传入nil训练家；Challenge:373–385、398–411只把这些对象抽样后赋入NPC队伍；Data:201–217将nil传至个体构造；`014_Pokemon/001_Pokemon.rb:1198–1204`创建默认拥有者（id0、空名、gender2、language2）。队伍赋值不改Owner。Swap:224–227交换的是对象引用，也不重写Owner。普通设施对手的Choose:65／77确实传NPC，不能套到Factory。

**最小修订与验收**：分普通对手与Factory对手／租借生成；Factory是默认Owner记录，不是Owner对象不存在，也不是对手NPC身份。创建→分给对手队伍→交换到租借队伍后默认Owner保持。只修该属主合同及WP55直接概括，不改WP18所有权主规则。

### WP57-R02：取消交换仍会调用队伍提交，只有计数受成功守卫

**位置**：[WP57第51行](../../specs/creature-rpg/wp57-factory-rentals-and-swaps.md:51)、第59行、F11；WP55第100行“仅成功提交”概括。

**证据**：Challenge:414–423，swapMade只守卫加交换数，后面的setParty无条件执行；setParty:200–203在进行中会立即写玩家队伍。Swap:208–244的取消返回false且不替换槽，但会话包装仍提交现有租借引用。首屏取消也有退出确认，不仅第二屏。

**最小修订与验收**：区分界面槽替换、计数、会话报名引用与玩家队伍写入。取消→不换槽／不加数，但仍提交当前租借集合；普通状态下可能同一引用值不变，不能因此称没调用提交。可用“当前报名P与租借R不同且正在进行中”的静态前提显示取消后的P→R写入；非进行中只更新报名引用、不加数、不改玩家队伍。补首屏退出确认路径。

### WP57-R03：含端点抽样会纳入等于数组长度的越界下标

**位置**：[WP57第13行](../../specs/creature-rpg/wp57-factory-rentals-and-swaps.md:13)至30行、失败／容量段、F02／F14。

**证据**：Choose:100–124、144–162。模板上端881经缩放后恰等实际池长度N；抽样又包含两端。普通组7及开放组4–7均可选到N，而合法索引最大N−1。随后取得nil，在创建个体入口失败，未到整体合法性检查或人数还原。空池时区间缩成0..0，确定在取条目／创建处失败，也不是在该rand调用因空区间报错。

**最小修订与验收**：保留真实881端点，不擅改为880；明确默认生成即有越界抽值和部分状态风险。静态对照N881／普通组7：抽880进入正常内容创建，抽881取不到模板并在创建处失败；规则人数仍为生成时的临时值。不得统称“都靠合法性校验不过再重抽”；成功后的范围还原与异常路径分开。

## 5. 已支持范围、维护与完整性

本轮支持并保留：三包主责任划分；训练家15行抽取数据、8档IV；Palace两套25行原始数据；Factory两张8行区间、IV与阈值数据；租借选择／撤销及正常交换引用；已述多数显式流程和直接依赖。匹配数据表不等于已证消费算法；三包目前均有必修，不能管理回填Reviewed。

- **旧WP52-B回填接受**：9份backfill-diff均可从上一轮快照内存重建到当前；A／B／C触改规格全部表格／场景数据未变，B62条和附表绑定范围保留。旧R01／N01／C01不重开。
- **继承BATCH-C02，非阻塞剩余**：旧self v3 `3a05f9e0cfcc9fc54820a1c0ab6c93c745d1d23787bba91a03facef43062fb11`／1,069,184字节，artifacts六项及Q41已匹配；但packages中的B仍`8036a674…`／44,557，C仍`290bee81…`／40,332，应与当前B`73fa6ffa…`／45,342、C`658b40bc…`／40,722同步。第191／645行起的这两包当前身份不要继续称零残留。只维护该两条及必要记录，不因此阻塞旧B范围。
- **本批BATCH-C01，非阻塞记法**：WP55 W19的“网络到”改“抽到”；WP56配置段“过半含等于”与其阈值方向统一；本批backfill-response中“本轮16件”应按实际上一reviewer目录14件（13个已列artifact＋final-checks）维护。历史轮16件不要全局替换。

实测记录：705／609清单身份匹配；本轮707输入固定；677／644／613／589／548／521六轮快照与各自已列reviewer artifacts未变；182份登记JSON可解析；当前specs＋矩阵377条相对链接存在；本批13条绑定匹配。新三包25／22／15共62条场景；18组提交常数中4组与回源后的正确消费值不符（WP56-R01三组、R05一组），不能以“算术自检同预期”证明分支正确。

相关检查见 [identity-checks.json](identity-checks.json)、[diff-checks.json](diff-checks.json)、[backfill-checks.json](backfill-checks.json)、[coverage-checks.json](coverage-checks.json)、[constant-checks.json](constant-checks.json)、[integrity-checks.json](integrity-checks.json)、[source-checks.json](source-checks.json)。reference HEAD正确、普通Git状态为空，33个相关源／数据文件与固定commit blob一致；实际全文／片段范围在 [review-notes.json](review-notes.json)。宿主方法契约的静态推理不冒称执行验证。

## 6. 下一步与停止

按WP55→WP56→WP57顺序有限修订上述原13编号及直接传播，同步主稿／不变量／场景／self／boundary／矩阵／当前哈希，保留全部旧被审身份。三包继续ReviewPending，批末统一送有限复审。修订提示见 [revision-prompt.md](revision-prompt.md)。**本轮不放行WP58或其它新包，也不要求重做三包首审。**

原有限通过集合保持：WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP52（WP47=A/B、WP52=A/B/C）、WP54、WP59–WP60。Demo、宿主、媒体、插件、U01–U10、真实地图／存档／输入／网络、WP78→WP79→WP80出口继续保留。本reviewer只写本新review目录，未改规格／矩阵／manifest／reference，未运行参考或代修订，未启动新包、任务或Agent，未发消息、未提交／推送。
