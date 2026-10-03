# WP58／WP62／WP38 独立首审报告

2026-09-30；独立reviewer；reference固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

**结论：REQUEST_CHANGES。WP58三项、WP62七项、WP38五项，共15项必修；三包继续ReviewPending，不启动下一批。** WP55／56限定Reviewed回填及WP57引用同步接受，旧通过范围不重开。另有非阻塞BATCH-C01维护。

本轮读完三稿与相关主实现，回读实际消费者和已审依赖的直接交界。静态字节／集合／独立常数检查与行为判断分别记账；提取侧“0失败”没有被当成外审通过。未运行参考、游戏、回放、捕获、编译器、生成器、真实存档或网络。

## 1. 实际固定输入

| 对象 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| WP58 v1 | `82c4a3f5ee0633a725b78ae1b9f66fe451c921eaca8299472c2d6605e723b2eb` | 22,819 |
| WP62 v1 | `24f9e1235ec1b19f8f8834d58f036142297a1fc1d9058868fec27dd585c4cce9` | 22,952 |
| WP38 v1 | `b0fa1b4cc80481e1bd65710f2c4a18f79e0f0668f0f6a5600cf124e1ea8457fb` | 19,689 |
| feature-matrix | `38039570201dc16a96b892d607e1d08cb16523e08d4efad5e1a77566f27d775b` | 53,976 |
| manifest | `a8861ce0294d7fb0f9d7fd211092b6da1ee9deb5e1ebc4960a1906a353112c9a` | 414,952 |
| 本批摘要v1 | `2e8792f3c1337c67b4806c01a70831f3a3d216bb2ec2b2d37346b25699a7b0b6` | 5,657 |
| 本批self | `187336d3f17b89092ba74eb3de023c70f97e0b18ceb23e8785704f15dc437bd2` | 27,736 |
| 本批boundary | `172395aa2b33043d4e4f53e1bbac6cd18aa09b18325abbc49ba8c018b13f4cfe` | 10,249 |
| 主TSV v35 | `e69bd4222ef1eef8d45ada06a83a5bdd09f98db4f5e98b09010e0c95b5f20a6d` | 94,072 |

已固定782项输入，见 [input-manifest.json](input-manifest.json)、[current-hashes.tsv](current-hashes.tsv)、[input-snapshot/](input-snapshot/)。780条manifest、684条TSV完整哈希／字节／短标签匹配，无缺失或重复。相对上轮755项只有9个原有文件变化，见 [changes-from-previous.diff](changes-from-previous.diff)。

下面每一编号的被审完整身份均为上表相应主稿。源码行号相对 `reference/pokemon-essentials/Data/Scripts/`。简称：

- **Recorded**＝`011_Battle/008_Other battle types/005_RecordedBattle.rb`。
- **Catch／Balls／Peer**＝`011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb`、`010_Battle_PokeBallEffects.rb`、`004_Battle_Peers.rb`。
- **Dex**＝`015_Trainers and player/005_Player_Pokedex.rb`；**Main／Entry／Summary**＝`016_UI/003_UI_Pokedex_Main.rb`、`004_UI_Pokedex_Entry.rb`、`006_UI_Summary.rb`。

## 2. WP58：三项必修

### WP58-R01：未记录某操作，不等于录制战斗不会执行该操作

**位置**：[WP58第61行](../../specs/combat/wp58-battle-recording-and-playback.md:61)、第71、77、108–110行，W07及相关命令表。

**证据**：Recorded:80–133只覆盖特定记录入口，没有禁用Mega／换位／呼叫；`001_Battle/008_Battle_ActionOther.rb:21–34,104–129`仍登记实际行动／Mega标记；CommandPhase:62–83、155–156、198–260和AI:66仍能调用；AttackPhase:92–99执行已登记Mega。Recorded初始化的普通Battle路径没有取消这些能力。

因此“记录与回放都不会产生Mega登记”错误：**原录制战斗可登记／执行，但记录没有保存这个标记，回放通常不能重现它**。同轮旧FIGHT记录后撤销，再选择没有记录钩子的Call／Shift，实际选择已变而记录仍可保留旧FIGHT；不能统一称未记录动作“均为空席”。

此外Palace的−2保留为“无力”哨兵：Palace:97–103确实放入挣扎对象作载体，但`002_Battler/009_Battler_UseMoveSuccessChecks.rb:202–205`按−2提前失败。回放把−2传回Palace登记，不能把它描述成实际使用普通挣扎攻击。

**最小修订／静态验收**：分开实际行动登记、记录写入、回放执行三层。列：满足资格的原录制Mega发生但标记未录；旧FIGHT→撤销→Call／Shift后记录可残留旧槽；Palace[0,−2]回放仍可能“无力”，不等同−1普通自动入口。只修这些合同与直接场景，不提前提取完整WP22／23。

### WP58-R02：布局没有恢复；四槽是初始化，不是记录容量保证

**位置**：[WP58第57行](../../specs/combat/wp58-battle-recording-and-playback.md:57)、第61、114、124、128行，W02／W12及复现范围。

**证据**：Recorded:47–68的18键没有双方场上人数；147–179只恢复这18键。普通Battle初始化`001_Battle.rb:98–174`默认1v1；setBattleMode:185–198只改sideSizes。设施DoubleBattle规则（`018_Alternate battle modes/002_Battle Frontier rules/005_Challenge_BattleRules.rb:17–19`）直接设置双打，不把布局写入所录rules字典；回放入口没有再应用该规则工厂。

同快照的双打记录也可能回放成默认单打，随后非空2号／3号席指令访问缺失战斗者。不能只用“跨版本不保证”等价掩盖**同版本已有布局缺失**。另外Recorded:121–124只先建4空槽；后续按索引赋值可扩展记录数组，回放却在198–221固定处理4席。缺轮次／缺席对象会在下标或`.length`读取处失败，和随机／换人序列越界取得nil再递增不是同一失败阶段。

**最小修订／静态验收**：明确缺失的布局状态及真实后果，不修reference；区分初始四槽、可能扩展、回放四席循环。用双打记录且2号席有FIGHT的输入，核对回放默认1v1与后续缺战斗者路径；另列空轮次表的首次失败，保留随机／换人nil取用的既有合同。字段表中未保存的其它关键运行选项也应具名说明其回放默认值责任，不宣称18键等于完整战斗状态。

### WP58-R03：重建队伍副本不构成实时状态隔离

**位置**：[WP58第124行](../../specs/combat/wp58-battle-recording-and-playback.md:124)、第132、136行及“不改实时对象／背包／设置”的总述；向WP62相关总述直接传播。

**本轮反例一（普通非内部回放也可触达）**：正常终局`002_Battle_StartAndEnd.rb:506–509`对回放队伍调用Peer离场；Peer:53–58可调用个体form=；`014_Pokemon/001_Pokemon.rb:159–165`直接登记**全局$player图鉴**，没有internalBattle门。FormHandlers:178–199的BURMY提供具体入口：使用过、结束、旧形态0、环境Cave→形态1；副本变形仍可改实时玩家图鉴。队伍对象是副本不阻止这条全局写入。

**反例二（给定记录／直接入口边界）**：Recorded回放:214–215直接调用物品登记；ActionUseItem:34–58会按玩家席归属扣**实时$bag**，失败还会报错。`Battle#pbOwnedByPlayer?:283–286`按侧／业主索引判断，不比较是否为原$player对象。设施正常菜单禁止用物只限制该来源，不是回放入口的隔离保护或记录校验。

**最小修订／静态验收**：删除全面隔离保证，区分副本字段、仍读取的实时依赖、可写入的全局状态和普通设施输入限制。列BURMY离场记录图鉴及“合法玩家BAG记录、实时背包有／无该物”的分支；不运行回放、不反序列化文件、不伪造真实录像。是否进入特殊交互也按条件记录：共用−1自动入口在非单打且安可时可走选靶，即使showMessages=false（ActionAttacks:36–57、Scene_ChooseCommands:384–438）；标准回放丢布局的问题另见R02，不用该缺陷推导普遍非交互保证。

## 3. WP62：七项必修

### WP62-R01：登记API的守卫、键、清理和刷新不能统一概括

**位置**：[WP62第13行](../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:13)、第17、30、66、85行，W01。

**证据**：Dex:24–46、61–78、129–160、195–218、235–272、335–341。set_seen／set_owned／计数接口有try_get守卫；register却经Species.get_species_form（`010_Data/002_PBS data/008_Species.rb:154–162`）取得nil后在Dex:203解引用，未知标识会失败。last_form_seen／set_last_form_seen按原键读写，不统一做基种归并／未知忽略；全国已解锁时species_in_unlocked_dex?甚至先返回真。

clear是现有公开入口，清记录并刷新，保留解锁表，并非“只能重建时整体清空”。set_seen、set_owned、register有可关闭的刷新参数；蛋、最近显示、捕获／击败计数等不统一刷新。某些查询还会初始化内部记录，不能以注释或方法名一律标纯查询。

**最小修订／验收**：按具体入口分表，不改参考。至少核对未知符号下set_seen无效与register失败的区别；原键set_last_form_seen与查询的往返；should_refresh=false时见过标记已写而accessible缓存未重算；clear后记录清除但区域解锁保留。修W01的全称断言。

### WP62-R02：已见形态计数实际上只检查形态0／1

**位置**：[WP62第71行](../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:71)、W05；相邻形态／性别入口说明。

**证据**：Dex:115–125取的是两组性别数组的长度；它们各只有两个异色槽，因此循环只访问形态下标0／1，不是所有已登记形态。当前PBS的UNOWN形态2有名称C（`PBS/pokemon_forms.txt:633–640`），可作具名反例：只登记该形态，seen_form?为真，而seen_forms_count为0。

**最小修订／验收**：保留真实计数缺陷，给“仅形态2／仅形态0／形态0与1与2”三例，分别0／1／2。register、register_last_seen和直接末次形态setter分别描述：首次登记的性别≥2并0、展示形态重查不能泛化到最近显示入口（后者保留个体gender，见195–228）。不要把参考修成理想的全部形态去重计数。

### WP62-R03：internalBattle只约束部分包装，不约束所有图鉴写入

**位置**：[WP62第38行](../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:38)至43行、第171行；WP58隔离总述及WP38§6相应传播归此编号。

**证据**：Battle:658–683只在pbSetSeen／Caught／Defeated三个包装设门。Catch:88–104直接set_owned、register_last_seen、set_shadow_pokemon_owned不带该门；记录版只把pbStorePokemon覆盖为空，并未覆盖整个登记队列。另有Pokemon.form=:159–165直接写全局玩家图鉴（见WP58-R03），不经这些战斗包装。普通出场的pbSendOut也在ActionSwitching:287–296调用pbSetSeen，不仅限“野生首次出场”。

**最小修订／验收**：列具体写入、接收者（战斗玩家对象／全局玩家）和门；正常设施菜单不可捕获与“直接到达队列消费时哪些字段仍写”分开。非内部且队列含未拥有个体：三个包装门不写相应seen／计数，但直接owned／暗影写入仍可发生；非内部形态提交也可触及全局图鉴。不得概括为所有非内部战斗均不写图鉴，也不得反向把三个包装的门删除。

### WP62-R04：区域成员nil返回与计数失败不能套用UI回退

**位置**：[WP62第92行](../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:92)、W11。

**证据**：`019_Utilities/001_Utilities.rb:401–405`在负区域／缺表／空表返回nil。Dex:102–109、351–358的非全国查询直接对它遍历，没有空数组兜底；可能在计数、seen_any或刷新中先失败。Main:348–355另有列表回退全国，不能覆盖上述数据层行为。

**最小修订／验收**：成员查询nil、区域编号查询0、区域长度查询0、seen／owned计数或seen_any失败、主列表回退全国分别列明。用存在但空的区域或越界区域作静态对照；不要统一声明“成员为空／计数0／UI全国”。全国−1计数的专门分支保持。

### WP62-R05：获得入口矩阵须按实际包装及前提分列

**位置**：[WP62第49行](../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:49)至57行，W17。

**证据与必要更正**：

- Utilities_Pokemon:4–5、48–91，主容量拒绝是**队伍满且盒子满**，不能仅写箱子满。一般静默加入显式写seen／owned再按see_form登记；仅入队静默入口121–129只按see_form登记再写owned，两者see_form=false时seen结果不同。
- 同文件63–64、106–107、147–148的赠送提示还要求see_form，当前“完整提示条件”漏此门。
- 脚本生蛋162–172本身不直接登记，但构造1219–1223可经form=:159–165写图鉴；UNOWN的getFormOnCreation（FormHandlers:146–149）是现成入口。不能把“没有set_seen_egg”扩大为生成蛋绝不写任何图鉴记录。
- UI_Evolution:5–20复制个体只登记／拥有，无该复制物种的新条目提示块；正常进化223–244另有提示。两条路径不能合并。
- UI_Trading:171–185先登记／拥有再开始交换演出；W17却把交换写入也归为动画后，与正文第53行及源码冲突。

**最小修订／验收**：用具名入口矩阵修上述单元格。队伍有位且盒满仍可进入获得；两静默入口see_form=false对照；UNOWN脚本生蛋可seen但不seen_egg；分裂复制与正常进化提示分开；交换动画前已有记录。继承WP18／26／31／34／35既有规则，不重开这些旧包。

### WP62-R06：可见列表、形态列表和摘要编号有具体例外

**位置**：[WP62第106行](../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:106)至115行，W13／15。

**证据**：Main:378–391的数值序会裁去末尾连续未见行；偏移图鉴还可删首个未见编号0行，并非全目录都保留占位。Entry:154–199只排**非0且无名称**的形态，默认形态0可列出；已见性别、单一性别和无性别处理不能套“所有无命名都不列”。Summary:410–416在首个已解锁区域查不到物种即break，不再找后续已解锁区域；Entry简略入口85–91则会next，两者不同。

**最小修订／验收**：列“已见最高编号后面的未知尾部被裁剪／中间未知仍占位”、已见默认无名形态0可列、全国锁定且首个已解锁区域无X但下一区域有X时摘要仍???而简略入口可取后者。名字搜索按Main:775–780是首字符匹配选中组，也应澄清“逐字符多选”表述，不推导任意姓名子串搜索。

### WP62-R07：栖息地页必须消费WP36已审的版本枚举反例

**位置**：[WP62第97行](../../specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md:97)、W16。

**证据**：Entry:325调用Encounter.each_of_version；`010_Data/002_PBS data/013_Encounter.rb:53–59`检查回退时用数组键，编译登记实际为符号键（Compiler:713及注册）。正常固定数据下v>0时仍会产出同图版本0，即使该图已有v版。当前已审WP36第51–52、278行已明确记载这一反例，完整哈希 `5a05aad72cec624397912038f3fb2f7df920eac220b2e55cbe9ee583c161ac33`；本轮再次回源确认，不重审WP36。

**最小修订／验收**：同地图v0有物种X、v1无X、其余显示门通过时，图鉴枚举v1仍可能通过v0点亮地点；不能如W16直接预期不显示。区分单次get查询的正常版本优先与枚举的并入行为；隐藏标志／区域／可见点门保持。

## 4. WP38：五项必修

### WP38-R01：状态倍率之前不取整

**位置**：[WP38第40行](../../specs/pokemon-rules/wp38-capture-and-receiving.md:40)，W02及相关公式。

**证据**：Catch:219先保留浮点血量结果，221–224乘状态倍率，226才floor，随后下限1。正文先把血量式写为floor会提前取整。原W02的112反而符合源码：A200/B1/率45得44.85，乘2.5后112.125再取整112；若按正文提前取整则得110。

**最小修订／验收**：分未取整中间量与最终x，明确唯一floor时点，保留已正确W02和y56167并给110反例对照。其余必捕获、暴击和普通摇晃顺序不因此改写。独立常数核对x1／15／22／90／112的y均匹配，说明算术值正确不能弥补公式时点错误。

### WP38-R02：球规则表需补齐可执行的阈值和所查集合

**位置**：[WP38第67行](../../specs/pokemon-rules/wp38-capture-and-receiving.md:67)至78行，尤其沉重球／等级球／甜蜜球／梦境球。

**证据**：Balls:125–147完整沉重球条件为：新式≥3000加30、≥2000加20、<1000减20，中间1000..1999不变；旧式≥4096加40、≥3072加30、≥2048加20，其余减20，率0早返，余夹1..255。当前只列增减数，没有完整阈值／不变区间。等级／甜蜜球的allSameSideBattlers默认侧0且只含未倒下场上者（Balls:103–113／150–157，Battle:458–460），不能把后备算“己方有”。梦境球用asleep?，而捕获状态倍率直接读真实status；Battler_Statuses:11–16、276–278及AbilityEffects:414–418使KOMALA／COMATOSE可视为睡眠。

**最小修订／验收**：补新旧完整体重表；明示等级／甜蜜球扫描当前己方存活场上集合，后备不计。梦境球判“视为睡眠”与公式真状态分开：真实NONE的合格COMATOSE目标可获梦球4倍，但不另获睡眠2.5倍。重量边界999／1000／1999／2000／2999／3000及旧三界给少量对照，保持原始数据／注册集合。

### WP38-R03：索引不是投掷者；无存活同伴时先nil访问失败

**位置**：[WP38第25行](../../specs/pokemon-rules/wp38-capture-and-receiving.md:25)、W16。

**证据**：ActionUseItem:126–130和Item_BattleEffects:322–326传的是选定目标／候选战斗者索引；Catch:115–120按这个索引所属侧解析，不是按“由敌方／友方使用球”解析。目标倒下后取allAllies[0]，Battle_Battler:747–748及Battle:458–460只提供存活同伴。没有存活同伴时为nil，Catch:123先调用fainted?失败，达不到129的“无目标”正常消息／返回。

**最小修订／验收**：区分使用者、输入目标索引和最终目标；敌侧索引直接指该对象，己侧索引取对位敌人。倒下目标有存活同伴→替换；无同伴→缺对象失败，不承诺正常提示／返回。正常菜单保护、直接到达执行入口的边界分别写；勿修参考nil保护或扩大成每次投球都会报错。

### WP38-R04：满盒Peer兜底在返回旧盒之前就失败

**位置**：[WP38第112行](../../specs/pokemon-rules/wp38-capture-and-receiving.md:112)、第114行，W17。

**证据**：PokemonStorage:231–251满盒返回−1；Peer:15–23随后调用自身未定义的pbDisplayPaused，尚未到return oldCurBox。固定脚本中该方法定义在Battle／场景／特定UI类，不在默认Peer或全局；未见Peer重开、混入或缺方法兜底。不能把注释里的期望当成实际“显示消息并返回原盒”。

**最小修订／验收**：当确实触达这个兜底时，定位缺失方法为首次失败，不保证旧盒号／成功存放。正常菜单的双满预检与直接／后段触达条件分开。保留此前可能已经发生的图鉴、昵称、治疗／离场等提交，不补回滚；不用真实存档造满盒测试。

### WP38-R05：满队转送盒子的成员不再参加结束时持物还原

**位置**：[WP38第102行](../../specs/pokemon-rules/wp38-capture-and-receiving.md:102)、第111、122行及预定WP20交界。

**证据**：Catch:37–60先把选中旧队员按**当前持物**送盒、移出队伍，再移位／删除还原记录；StartAndEnd:480先完成接收，506–509只对之后留在队伍的成员按届时initialItems还原。移位记录不是给已送盒者恢复物品。已审WP20§6.4和未决第311行明确把这两条路径的完整对照交给WP38，本稿不能只说“另有还原记录机制”。

**最小修订／验收**：明确留队／提前送盒两条结果。以前置“还原记录仍X，当前持物已为nil”的合法暂时移除状态作对照：留队→正常结束还原X；捕获接收时先送盒→保持nil，退出还原循环。**不要用普通消耗作这个前提**：Battler_AbilityAndItem:226–241的永久移除可能同步清记录；可用有资格的暂时打落路径（MoveEffects_Items:179–188）或明确已给定此状态。永久消耗且记录也nil时两路径都nil。修完整接收交界，不重开WP20／50已通过规则。

## 5. 支持范围、回填与非阻塞维护

**先行回填ACCEPTED**：WP55／56头尾和F13-04回填、WP56／57引用级联符合授权；三份旧稿全部表格和78条场景未变，七份diff可从闭合轮快照内存重建到当前。旧13项关闭及更早通过范围继承。

本轮支持并保留：18个记录属性键和五元组的字面集合；明确保留1／2／5结果与记录提升；图鉴主要字段／正向登记、默认设置、区域编译重复检查；捕获球26项／22登记（1＋19＋2，失败族0）、已述多数倍率、暴击和普通摇晃顺序、昵称／选择菜单与成功提交主顺序。**三包各有实质必修，均不能回填Reviewed。**

**BATCH-C01（本批非阻塞维护，随修订完成）**：

- 回填回应`5bf9bb3afefe389a5aee8bbffae68c988b96e5fba0aa66260c0593da0afdc2ad`／7,781字节的§4“当前身份”表仍写旧self `be72db7b…`、旧摘要`78a42a6b…`。磁盘／manifest实际是self `2a9f4d3cc743628a5934cad4d181c2b1e105d12b404353385bc9df3ff741f564`／21,490，摘要 `df3c22290d32117257461e19e63ce39aba934a41dd103d79c137d9c539262412`／9,320。同步表或明确标为中间阶段；不得声称所有当前表互相一致。
- WP38 W07只有球率／等级，未给HP／状态或x就附y53910。删此y或补足输入；当前数值只在x90时成立。把“60位小数”明确为独立高精度常数核对，不称参考双精度运行验证。
- WP58“属性值一律副本／去引用”过宽：Recorded:28–66对名字／徽章作clone，对队伍等作序列化，而NPC台词及若干字段直接赋值；按字段说明，不承诺统一深复制。
- WP62玩家保存来源应为SaveValues:3–8；77–80保存的是全局元数据。当前self的64条源身份还漏了正文已列的Balls与Peer两份关键文件，补登记即可。

独立完整性检查：[identity-checks.json](identity-checks.json)、[diff-checks.json](diff-checks.json)、[backfill-checks.json](backfill-checks.json)、[integrity-checks.json](integrity-checks.json)、[coverage-checks.json](coverage-checks.json)、[constant-checks.json](constant-checks.json)、[source-checks.json](source-checks.json)。本轮55条场景；17条当前依赖及17条boundary绑定匹配；211份已登记JSON可解析；specs＋矩阵411条相对链接存在；755／734／707／677／644／613／589／548／521九轮快照及已列reviewer原件未变。来源字节检查与实际读取范围分开，详见 [review-notes.json](review-notes.json)。

原始表／调用行计数匹配不证明消费者行为：74处随机调用行（非Safari71）、区域2节212行、26球及22登记均匹配；真正需要修的是上述门、次序、失败点和消费语义。reference HEAD正确、普通Git状态为空。

## 6. 下一步与停止

只按原15编号、C01及直接传播有限修订，顺序WP58→WP62→WP38，保持三包ReviewPending；WP62变化向WP38实际引用级联，旧被审v1留史。提示见 [revision-prompt.md](revision-prompt.md)。不重做首审，不自动开启新工作包；本轮不发下一批执行许可。

旧限定通过集合保持：WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP52（WP47=A/B、WP52=A/B/C）、WP54–WP57、WP59–WP60。Demo、宿主、媒体、插件、U01–U10、真实地图／存档／输入／网络、WP78→WP79→WP80出口保留。此reviewer只写本新review目录，未代修改规格／矩阵／manifest／reference，未创建任务／Agent、未发消息、未提交／推送。
