# WP58／WP62／WP38 v2 独立有限复审

2026-09-30；独立reviewer；reference固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

**整批结论：REQUEST_CHANGES。原15项中12项CLOSED，仅WP62-R01、WP62-R03、WP62-R06的下述剩余点未闭合。WP58与WP38分别PASS_SCOPED；WP62仍ReviewPending。可以做已通过范围的管理性回填与定点收尾，不能开始新包。**

BATCH-C01的1／3／4已关闭，C01-2的W07数值样例仍需非阻塞维护；另列C02限定记法维护。WP38的限定通过不认可这个错误样例，也不替WP62整体通过。只复审原编号、维护与直接传播，继承首审已支持范围，不重做首审。WP55／56回填、WP57引用同步及所有旧限定通过结论不重开。

## 1. 本轮实际固定版本

以下10项均从磁盘复算，与交接完整值一致；不是采用提取侧摘要前缀补全。

| 对象 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| WP58 v2 | `19582962a78f773e57833f825ee833a78449504a33b2dd597fd7e5568b98e27d` | 29,329 |
| WP62 v2 | `003532aabc518faf42bfd937951e60d33294771d706a5457a6ce1bead5212046` | 31,350 |
| WP38 v2 | `8ffe0f48b1373394a59290925561e3ed1aa7366c14c08e16f071facc0eb122e2` | 23,752 |
| feature-matrix | `9ed7533b6ce291e2b91de50152fc05e77540c477d68a1450c674b64e860592c8` | 54,180 |
| manifest第六十一轮 | `3aa7e16e611a0edda4b4ebe7fbceff1ef3ee95a29570ae7f2967f0b38ef8ac72` | 428,008 |
| 主TSV v36 | `f24d0b998365900518021b941d2156c0dcb79635bbcb33c0a5db85c964f46cb2` | 97,382 |
| 本批摘要v2 | `8036990dc3d3504f033ac35de49617327e7f623bc963bf7c4ce34ff6d3d15140` | 7,602 |
| 本批self v2 | `f2ec2b7251a3f91973a3650a110423236d71dd585fb510a856c2eb3a3fcbcfa2` | 32,576 |
| 本批boundary v2 | `a1a1fa225dc5277a6be1215fc4f29c155d67315270b6b2169151b4a05a45312e` | 11,331 |
| 回填回应C01维护后 | `609d8f24a811bffabbf1015b7448ab73705d7a694a24542b0967a74bde0ad8cf` | 8,318 |

本批材料位于 `review/wp58-wp62-wp38-delivery-2026-09-29/`。提取侧修订回应位于本目录上一级，实测为 `b9c6b4879c1eb741b898f1c78cd6ec891efd6490c45efd53448098cb67a6fb83`／21,078字节。

本轮固定806项，见 [input-manifest.json](input-manifest.json)、[current-hashes.tsv](current-hashes.tsv) 与 [input-snapshot/](input-snapshot/)。相对首审782项，恰有交接列出的10个现有文件变化；8份修订diff全部可逐块重建至当前字节。新增24条登记＝首审reviewer15件＋回应1＋diff8。首审被审v1、原报告／提示和快照仍保留原身份；本报告没有把v2当成首审已通过版本。

## 2. 原编号逐项结论

源码简称均相对 `reference/pokemon-essentials/Data/Scripts/`：

- Recorded＝`011_Battle/008_Other battle types/005_RecordedBattle.rb`；Battle＝`011_Battle/001_Battle/001_Battle.rb`；StartEnd＝同目录`002_Battle_StartAndEnd.rb`。
- Dex＝`015_Trainers and player/005_Player_Pokedex.rb`；Main／Entry／Summary＝`016_UI/003_UI_Pokedex_Main.rb`／`004_UI_Pokedex_Entry.rb`／`006_UI_Summary.rb`。
- Catch／Balls／Peer＝`011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb`／`010_Battle_PokeBallEffects.rb`／`004_Battle_Peers.rb`。
- Pokemon＝`014_Pokemon/001_Pokemon.rb`；Forms＝`014_Pokemon/001_Pokemon-related/001_FormHandlers.rb`；UtilitiesPokemon＝`019_Utilities/002_Utilities_Pokemon.rb`。

本轮逐项回读相应源码与消费者。下表的“CLOSED”是独立判断，不是复述提取侧“核实成立”。更早通过部分继承；新增记录与已接受范围见 [static-checks.json](static-checks.json)。

| 原编号 | 结论 | 本轮证据与接受范围 |
| --- | --- | --- |
| WP58-R01 | CLOSED | Recorded:80–133；CommandPhase:5–24,62–83,155–156；ActionOther:21–36,104–130；AttackPhase:92–99；Palace:97–103、UseMoveSuccessChecks:202–205。实际行动／记录／回放已拆分；原录制Mega可执行、旧FIGHT残留、−2无力哨兵均修正。 |
| WP58-R02 | CLOSED | Recorded:47–68,147–179,198–221；Battle:98–198；DoubleBattle规则:17–19。缺布局、同版双打默认1v1、初建4槽与扩展／消费4席、数组首次失败已说明；保留W20的FIGHT输入前提（§4记法）。 |
| WP58-R03 | CLOSED | StartEnd:506–509→Peer:53–58→Pokemon:159–165；Forms:178–199；Recorded:214–215→ActionUseItem:34–60；ActionAttacksPriority:36–57。BURMY全局图鉴与消耗型BAG背包反例已落实；副本与全局依赖分开，−1选靶条件不再全称化。 |
| WP62-R01 | 未闭合，接受新增§3.4大部分 | 原有全称句未同步，且新增“原键与归并键互不覆盖”过宽，详见§3.1。 |
| WP62-R02 | CLOSED | Dex:115–126,195–228；PBS UNOWN形态2:636–637。计数只查0／1、形态2可精确命中但计数0，以及0／1／2对照正确；原键覆盖问题只归R01。 |
| WP62-R03 | 未闭合，仅直接传播剩余 | Battle:658–684、Catch:88–104、Pokemon:159–165。三稿正文与boundary B02已按包装／直接写入区分；B04仍保留相反总述，详见§3.2。不重开已经接受的正文。 |
| WP62-R04 | CLOSED | Utilities:389–419；Dex:102–109,351–358；Main:348–355。成员nil、编号／长度、区域遍历失败、全国专门分支和UI回退已分开。 |
| WP62-R05 | CLOSED | UtilitiesPokemon:4–6,48–173；Pokemon:1219–1225、Forms:146–149；Evolution:5–20,218–245；Trading:171–201。具名获得矩阵、容量、see_form门、蛋构造副作用、复制／正常进化提示、交换演出前写入已修正。W24前提维护见§4。 |
| WP62-R06 | 未闭合，仅W15剩余 | Main:378–391,775–781；Entry:85–91,154–199；Summary:410–417。正文列表裁剪、首区即停、形态0例外和搜索已接受；W15旧期望未同步，详见§3.3。 |
| WP62-R07 | CLOSED | Entry:325→Encounter:30–36,53–59；Compiler:713；已审WP36:51–52。版本枚举并入同图v0缺陷已落实，未误改单次get语义。 |
| WP38-R01 | CLOSED | Catch:219–227。状态倍率后才floor，44.85×2.5→112、提前取整110反例正确；C01-W07另列，不重开此算法。 |
| WP38-R02 | CLOSED | Balls:103–178；Battle:458–461；Battler_Statuses:11–16,276–278；AbilityEffects:414–418。完整体重档、存活场上集合、梦球有效睡眠与真实状态倍率已区分。 |
| WP38-R03 | CLOSED | ActionUseItem:126–130；Item_BattleEffects:322–327；Catch:115–129；Battler:747–749。目标索引不是投掷者；无存活同伴时nil首次失败正确，未补退款／回滚。 |
| WP38-R04 | CLOSED | Peer:15–23；PokemonStorage:231–251；全Scripts定义检索。满盒返回−1后缺方法先失败，正常预检与后段触达、早期提交均已分列。 |
| WP38-R05 | CLOSED | Catch:37–60；StartEnd:480,506–509；Battler_AbilityAndItem:226–241；MoveEffects_Items:179–188。记录X／当前nil的暂时移除前提下，留队还原X、先送盒保留nil；未以永久消耗冒充。 |

## 3. 三个剩余编号的最小收尾

### 3.1 WP62-R01：同步旧全称句，并去掉原键必然隔离的保证

被审对象为§1的WP62 v2完整哈希。实际位置：

- [第27行](../../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:27)仍说“每次记录写入后重算”；第105行重复。
- [第86行](../../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:86)仍说“一切记录按基种键”“未知标识在查询与写入处都静默失败”。这与新增§3.4和W01、W23直接冲突。
- [第77行](../../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:77)及W21第187行新增“与register写入的归并键互不覆盖”。原键可能恰好就是同一个基种键，不能保证隔离。

源码：Dex:41–46、147–152、195–218的刷新可关闭；74–78、129–140、260–273等不刷新；register在203行可因未知数据为nil先失败；原键setter在139行直接写入同一末次形态表，register在216–217行使用基种键。

**影响**：后续消费者读§4或字段表仍会实现统一静默／自动刷新；读W21则可能错误设计两份隔离记录。不是措辞偏好，是同一文档两套相反合同。

**最小修订**：第27／105行指向§3.4的分入口刷新；第86行限定守卫族并指向register与原键例外；第77行／W21按“键相同或不同”分列，不必重写其它已接受表。

**静态验收**：

1. 未知符号：set_seen无效；register仍在数据解引用处失败。
2. should_refresh=false：写见过标记但不重算可访问缓存；两个计数入口也不自动刷新。
3. 先由register在`:UNOWN`留下末次形态，再用直接setter按同一`:UNOWN`键写新三元组：新值覆盖旧值；改用不同的原始形态键时才分别存储。只作状态推导，不执行表达式。

### 3.2 WP62-R03：boundary B04仍把局部门扩大为整个设施战斗

被审boundary完整哈希 `a1a1fa225dc5277a6be1215fc4f29c155d67315270b6b2169151b4a05a45312e`／11,331字节。

[boundary第45行](../../wp58-wp62-wp38-delivery-2026-09-29/boundary-checks.json:45)仍是当前B04断言：“设施战不写图鉴”。同文件第24行B02与三稿正文已经改对；这条不是历史引文。

Battle:658–684只给三个包装设internalBattle门。Catch:94,97,102是直接写入；StartEnd:506–509→Peer:53–58→Pokemon:165可写全局玩家图鉴。非内部、使用过的BURMY按环境离场变形仍是本轮接受的反例。

**最小修订／验收**：只同步B04及仍引用其总述的活动材料，说明三个包装的门与直接写入／形态提交不同；或者明确引用B02的完整条件。同一个BURMY反例在B02／B04不得给相反结果。正文已接受，不要求再重提取图鉴战斗交界。

### 3.3 WP62-R06：W15必须保留无名默认形态0例外

被审对象仍为§1的WP62 v2。[W15第181行](../../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:181)仍写“无命名形态不列”；第130行正文已经限定为“非0形态”。

Entry:161只排除无名称的非0形态；164–199按性别／已见门构成列表并可给默认形态补显示名。因此“已见默认形态0、无FormName、其余显示门通过”可以列出。W15当前输入就包含形态0，不足以排除这个反例。

**最小修订／验收**：W15拆或补成成对前提：默认形态0无名且已见→可列；非0形态无名→被过滤。保持已接受的其它性别／已见门、摘要两区域分叉、数值序裁剪和搜索结论；不增加整套UI测试。

## 4. 非阻塞维护与回填许可

### BATCH-C01

| 子项 | 结论 |
| --- | --- |
| C01-1 当前身份表 | CLOSED。回填回应已把旧self／摘要的中间阶段与当前磁盘值分开，实际当前值匹配；无需修改更早原件。 |
| C01-2 W07样例 | 未闭合，仍按非阻塞维护处理。见下。 |
| C01-3 复制语义 | CLOSED。字段按clone、序列化、直接赋值区分；不再统一深复制。 |
| C01-4 保存来源与源身份 | CLOSED。玩家SaveValues:3–8正确；self73条源身份匹配，Balls／Peer已补入。 |

[WP38 W07第157行](../../../specs/pokemon-rules/wp38-capture-and-receiving.md:157)新补了“满血无状态输入（x=90）”。巢穴球等级21、基础率45使修正率90；**满血无状态则血量项为90／3＝30，y为43874**，不是53910。53910只对另设x=90的独立常数成立。提取回应§4第2项也复制了错误前提，self的x90常数本身算对，不能据此验证完整输入链。

允许同轮采用最小方案：删去“满血无状态”并明确“另设x=90作独立常数对照”；或保留满血输入而把x／y改为30／43874。只改该样例与直接复制材料，并在新回应勘误；旧回应留史不覆盖。WP38-R01正确算法与W02不再重审。此样例不计入本轮PASS_SCOPED认可的正确数值集合。

### BATCH-C02（随本轮收尾的限定记法维护，不另作阻塞编号）

1. WP58§3／§6.3的高席失败描述保持**FIGHT等需要读取战斗者的分支**前提；不要推广为每种非空指令都在相同时点失败。Recorded:219的RUN只写决定；W20本身已给FIGHT。BAG反例／W23明确给“使用后消耗的物品，如POTION”前提：ActionUseItem:50–51会跳过空物品／非消耗品，随后才触及实时背包。这两处只收紧已列反例的输入，不重开布局缺失或全局隔离判断。
2. WP62 W24的静默入口对照明确给“有效且已经构造的个体、此前未见、队伍有位”，避免把包装本身的see_form门扩大为构造阶段无副作用；构造UNOWN的既有例外保留。第159行“战斗侧4类／获得侧7项、蛋生成不写”的旧目录计数／简写同步当前5行／11行及§3.2限定，不重新扩域。

### 可以回填的具体范围

- **WP58：PASS_SCOPED**。A～F已述记录生命周期与提升、18属性与五元组、实际行动／记录／回放分层、随机与换人序列、布局／数组限度、模式差异、已述全局依赖和中止／终局边界。结合上述C02限定场景前提。对应F13-06只回填该子范围。
- **WP38：PASS_SCOPED**。A～F已述五层许可与消耗、捕获数学／取整／随机、26球／22登记与具体效果、成功提交、目标／满盒首次失败、接收与队员替换持物还原、已述Shadow抢夺交界；C01-W07按上述维护，不作为已核准样例。对应F10-06只回填该子范围。
- **WP62：REQUEST_CHANGES**，保留ReviewPending和F15-01对应状态。WP38引用其已经接受的图鉴接点，不等于WP62整体Reviewed；新引用仍注明WP62收尾稿尚待短复审。

提取方可在同一收尾轮做这两包管理性回填及指定维护；保留本轮被审v2完整哈希，回填新字节不冒充被审对象。无需为仅状态／引用变化重新首审。当前reviewer没有代改任何规格或清单。

## 5. 检查边界与停止

独立检查：804条manifest／708条TSV全值、字节、短标签一致；806项固定输入稳定；8份修订diff重建8／8；17条正文绑定和17条boundary绑定匹配；221份登记JSON有效；specs＋矩阵411条相对链接有效；场景计数23／25／20与self一致。**这些是身份／计数检查，不代表68条场景逐条均正确**，W15／W07反例正说明二者不同。

首审782项及旧九轮755／734／707／677／644／613／589／548／521项快照与各轮已列reviewer原件均未变；首审15件原件身份匹配。78份来源与固定commit blob一致，其中提取侧73条源身份亦匹配；实际回读范围单独记在 [static-checks.json](static-checks.json)。reference HEAD正确、普通Git状态为空。独立检查脚本只处理文本／哈希／JSON／集合／差异及固定常数，没有执行参考。

证据文件：[preflight-checks.json](preflight-checks.json)、[diff-checks.json](diff-checks.json)、[integrity-checks.json](integrity-checks.json)、[source-checks.json](source-checks.json)、[constant-checks.json](constant-checks.json)、[reference-checks.json](reference-checks.json)。

**下一步只做WP62三个剩余编号、C01-2、C02、WP58／WP38限定回填及必要身份级联，送短复审后停止。** 可直接使用 [revision-prompt.md](revision-prompt.md)。不启动第四包，不补做WP22／23／32／37／53，不重开本轮12项关闭或旧已审行为。Demo、宿主、媒体、插件、U01–U10与WP78→WP79→WP80出口继续保留。未运行游戏／参考代码／网络，未创建任务或Agent，未发消息、提交或推送；本轮仅在这个新建`recheck-v2/`子目录写审查材料。
