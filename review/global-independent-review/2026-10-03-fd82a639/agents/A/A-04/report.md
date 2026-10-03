# A-04 独立主审报告：WP21–WP23

结论：**REQUIRES_REVISION_SCOPED**。6项新发现（5 P2、1 P3），涉及原文固定数据/边界缺口与净化误改。三个工作包均需在具名问题上修订；不把已读片段扩成整包完整通过。

固定项目输入：e1e01bb18d824931e54f182dd61af5a9f908ba85。固定只读参考：8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。本批五份原稿/附表与五份净化文本全文实读，FM35/ME25/SH46共106个测试逐条核对；95条阅读记录、76条来源覆盖、374条双向/三方对照。来源精度、同代理既有阅读复用和未读片段分别记录，不以计数、搜索或哈希替代语义阅读。

独立性：首判在2026-10-03 14:59:55 UTC保存，未读其他组本批发现；首判文件未重写。后续数据逐值检查新增SNORUNT同根因实例，合并RUN-A-030，不增加根因数。历史PASS只用作输入身份/范围线索。原始显式请求Astra/Ultra保持；子代理没有独立运行模型回显，Standard速度要求未能独立核验，记UNVERIFIED且未更改设置。

## 覆盖与边界

| 工作包 | 原文/净化 | 实读主要来源与判定 |
| --- | --- | --- |
| WP21 | 1主稿/1净化；FM01–35 | 完整形态注册表及全部注册/复制分支、提交链、相关交互学招、展示数据与界面/进化/寄养/捕获调用；RUN-A-026/027需修订。 |
| WP22 | 1主稿+1附表/对应2净化；ME01–25 | 个体Mega/Primal全文、许可/执行器全文、菜单/命令/攻击/入场/濒死/世界/设施定点、全部48目标与46基础HP对照、47石/环/两宝珠；RUN-A-028需修订。 |
| WP23 | 1主稿+1附表/对应2净化；SH01–46 | Shadow及Other全文、Shadow数据全文、净化室领域/输入主段、成长/用物/存放/类型等消费者、全部131条可选配置/25性格/18招数据接点/4物品；RUN-A-029/030/031需修订。 |

完整新读/重读短模块为FormHandlers、MegaEvolution、ShadowPokemon、ShadowPokemon_Other、Shadow数据、Ribbon、Type、ActionOther、AI_MegaEvolve。Pokemon/Move/Species/Stat/Trainer/配置/事件/时间/存档转换/回放/Peer/捕获采用本代理同固定来源既有具名阅读，并只在需要处补读；精确段见TSV。净化室绘制中段、完整战斗效果/AI/设施、其它PBS内容与真实事件运行不作穷尽保证。

五份文件对应关系按readiness映射核定；依赖只读。最终WP66-B §2.2保留默认特殊负位置的盒38/格29，因此WP23省去重复编码未另报语义丢失。WP23原文头尾的N01旧待审措辞与审计明确的获准固定身份分开，不据其管理残留新增批准链缺陷。

## 新发现

| ID | 优先级 | 包 | 结论 |
| --- | --- | --- | --- |
| RUN-A-026 | P2 | WP21 | 提交与战斗改招缺少形态到具名招式的固定对应 |
| RUN-A-027 | P2 | WP21 | ROTOM 已掌握目标招时删除旧招的分支与空招式边界未登记 |
| RUN-A-028 | P2 | WP22 | BANETTE 的 Mega 石身份被净化改写 |
| RUN-A-029 | P2 | WP23 | 香类无效条件从友好度255误变为心阶段5 |
| RUN-A-030 | P2 | WP23 | 可选 Shadow 表的 GROWLITHE 与 SNORUNT 首招被改写 |
| RUN-A-031 | P3 | WP23 | SH06 的90点香下降缺少储存性格前提 |

### RUN-A-026 — 提交与战斗改招缺少形态到具名招式的固定对应

P2 / FIXED_RULE_DATA_NOT_DELIVERED / OPEN / HIGH_STATIC。

**当前主张与实际来源**：原稿和净化稿以“对应新招”“专属招”“固定基础招”概括 ROTOM、KYUREM、NECROZMA、CALYREX 的形态改招，并用同样代称表示 ZACIAN/ZAMAZENTA 的战斗改招；FM15没有具体输出身份。 固定来源提供每个形态对应的招式及保底身份。全文规格与最终目录定向检索未定位一张承接完整映射的数据表；少数测试仅给 AIRSLASH/HYDROPUMP、GLACIATE/ICEBURN/FUSIONFLARE 等局部样本，不能唯一推出其余映射。未将源码注册结构作为未来API要求。

**项目定位（固定项目commit）**：
- specs/pokemon-rules/wp21-dynamic-forms-and-display.md:97–116
- specs/pokemon-rules/wp21-dynamic-forms-and-display.md:184–196
- deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md:75–94
- deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md:160–172
- deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md:94–96

**来源定位（固定参考commit）**：
- Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:221–265
- Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:330–383
- Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:562–587
- Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:653–729
- Data/Scripts/013_Items/001_Item_Utilities.rb:582–628
- PBS/moves.txt:8016–8022

**最小静态反例前提**：
- 固定有效数据；NECROZMA 非蛋、非 Shadow、无强制形态；当前形态0，唯一已知招式 TACKLE，默认 SUNSTEELSTRIKE 已注册。
- 经会执行提交处理器的入口写形态1；消息及后续重算/图鉴调用正常返回，不再初始化招式。

**预期**：
- 持久招式按顺序成为 TACKLE、SUNSTEELSTRIKE；新增招式初始 PP5、提升计数0。
- 仅凭现有“专属招”文字不能独立确定 SUNSTEELSTRIKE，而其他任意已注册新招也能满足抽象句；这是固定输入缺口，不是运行失败。

**影响**：独立实现无法在这些常见形态提交中决定招式身份、判断重复目标或执行正确保底；仅运行目前抽象场景也无法发现不同实现的偏差。

**最小修正**：在 WP21 补充独立数据表，逐项列出 ROTOM 1–5及回退招、KYUREM 0/1/2的双向招式对应、NECROZMA/CALYREX 1/2及回退招、ZACIAN/ZAMAZENTA开始/终战对应；正文和测试引用该表。只表达数据和行为，不抄处理器代码。

**确定复核条件**：
- 对照所列六物种固定映射，每个分支的目标身份与无效/缺失数据门可由最终交付唯一决定。
- FM15给出 SUNSTEELSTRIKE 与 PP5；为其余映射分别给具名目标或明确引用完整表。

### RUN-A-027 — ROTOM 已掌握目标招时删除旧招的分支与空招式边界未登记

P2 / REFERENCE_BRANCH_OMITTED / OPEN / HIGH_STATIC。

**当前主张与实际来源**：形态1–5的概括为忘记旧形态招并在同槽学习对应新招；细节把 ROTOM 已有旧形态招列为直接改标识路径，专项边界只述无旧招满槽、替换/保底不存在抛错。 处理器先选中第一条旧形态招；目标招存在但已经掌握时会转入删除旧招分支。保底检查早于该重复目标检查，因此合法同值提交可删除唯一目标招而不补招。普通形态提交没有“相同值无操作”守卫；正常 ROTOMCATALOG 自己拒绝同形态，两层不能合并。

**项目定位（固定项目commit）**：
- specs/pokemon-rules/wp21-dynamic-forms-and-display.md:99–101
- specs/pokemon-rules/wp21-dynamic-forms-and-display.md:186–192
- deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md:77–79
- deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md:162–168

**来源定位（固定参考commit）**：
- Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:230–262
- Data/Scripts/014_Pokemon/001_Pokemon.rb:159–178
- Data/Scripts/013_Items/002_Item_Effects.rb:1249–1260
- PBS/moves.txt:2476–2482

**最小静态反例前提**：
- 默认有效 ROTOM 形态及招式数据，非蛋、非 Shadow、无强制形态；存储形态1，唯一已知招为 OVERHEAT。
- 直接经普通形态提交入口再写形态1；呈现与后续重算/图鉴正常，无随后重置招式操作。此为裸提交边界，不是假称正常 ROTOMCATALOG 可重复选择相同形态。

**预期**：
- 形态仍为1，唯一的 OVERHEAT 被删除，招式列表为空；没有重建同槽、没有补 THUNDERSHOCK。
- 对照：通过正常 ROTOMCATALOG 选择当前形态被其外层拒绝，不能用该界面验证前一裸入口结果。

**影响**：只按现有规格实现会保留或替换该槽，甚至错误承诺保底至少一招，抹去已声明低层入口的可观察边界。

**最小修正**：在 ROTOM 行和删除路径中明确“目标已掌握”导致删除第一条旧形态招；说明保底只在更早的无有效目标且唯一旧招分支触发，并给出同值提交可清空列表的具名前提。保持正常道具的同形态拒绝。

**确定复核条件**：
- 静态复核直接形态1/唯一OVERHEAT/再写1得到空列表。
- 复核换到不同形态且目标未掌握仍为原有同槽替换/PP钳制；正常目录同形态仍不触发。

### RUN-A-028 — BANETTE 的 Mega 石身份被净化改写

P2 / SANITIZATION_IDENTIFIER_CORRUPTION / OPEN / HIGH_STATIC。

**当前主张与实际来源**：净化附表把 BANETTE 形态1的石要求写成 BANETTEITE；原附表为 BANETTITE。 固定物种形态字段与物品身份都是 BANETTITE。资格按身份匹配，不按展示名称模糊匹配。48个目标表逐行阅读后静态字段对照只发现这一资格身份差异，基础值在本次对照中一致。

**项目定位（固定项目commit）**：
- specs/pokemon-rules/wp22-transformation-data.md:44–44
- deliverables/final-specification-set/pokemon-rules/wp22-transformation-data.md:44–44
- deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md:27–27

**来源定位（固定参考commit）**：
- PBS/pokemon_forms.txt:957–960
- PBS/items.txt:2798–2805
- Data/Scripts/014_Pokemon/002_Pokemon_MegaEvolution.rb:6–27

**最小静态反例前提**：
- 默认有效物种/物品目录；BANETTE 当前简化形态0，持物 BANETTITE，无强制形态。
- 只查询个体 Mega 目标；若扩到战斗，则另给正常所属业主有环、未用、非野生、无Transform/SkyDrop/禁止开关的全部许可。

**预期**：
- 个体目标为形态1且可Mega；按净化表错误拼写匹配则无法从合法 BANETTITE 找到对应目标。

**影响**：直接影响合法默认内容的变形资格，并与最终其它物品目录的 BANETTITE 身份不一致。

**最小修正**：将净化附表的身份恢复为 BANETTITE；保留原稿和参考源不变，加入 BANETTE 持合法石的具名对照。

**确定复核条件**：
- 默认48个Mega目标的条件身份逐项与固定源、原附表和实际物品身份对应；BANETTE→BANETTITE→1。

### RUN-A-029 — 香类无效条件从友好度255误变为心阶段5

P2 / SANITIZATION_PREDICATE_CHANGED / OPEN / HIGH_STATIC。

**当前主张与实际来源**：净化野外行变为“非 Shadow 或 H5且G0”失败，战斗专用资格变为“不是H5/G0”；原文这两处均为友好度 h255与G0。 实际两处条件使用友好度255且心量表0；合规M>0且G0时心阶段为0，不会为5。将两个不同状态域混为一谈使满友好且已开锁的Shadow仍满足错误的净化稿资格。

**项目定位（固定项目commit）**：
- specs/pokemon-rules/wp23-shadow-hyper-and-purification.md:120–124
- deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md:120–124
- deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md:34–34

**来源定位（固定参考commit）**：
- Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:226–244
- Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:247–274
- Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:286–324
- Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:93–106
- Data/Scripts/013_Items/001_Item_Utilities.rb:672–687
- Data/Scripts/013_Items/001_Item_Utilities.rb:774–775
- Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb:87–101

**最小静态反例前提**：
- 条件化内容前提：三种香之一按已读可选物品数据有效注册，库存1；并不据此声称备份已安装或默认启用。
- 有效非蛋 Shadow，G0，友好度255；因此有效Hyper为假。普通个体用物门通过，战斗对照还无Embargo等其它拒绝，消息正常。

**预期**：
- 野外处理器/共同工具返回失败，友好度/G不变，外层不消费这份香。
- 战斗的专用资格拒绝；若登记后才变成此状态，执行复检失败并退回未用物品。错误H5/G0谓词无法产生这些结果。

**影响**：会错误允许无效用物并改变消费/退还行为；不是可选资源缺失造成的不确定性。

**最小修正**：把两处H5恢复为“友好度=255”，明确与心阶段H区分；添加G0且友好度254/255的两侧对照，仍保留有效Hyper与Scent旗标的独立门。

**确定复核条件**：
- 默认M4000/G0时H0；友好度255拒绝、254可进入共同工具。
- 逐行对照野外工具、战斗资格与执行复检，确认资源消费只随正确成功结果发生。

### RUN-A-030 — 可选 Shadow 表的 GROWLITHE 与 SNORUNT 首招被改写

P2 / SANITIZATION_ORDERED_CONTENT_CHANGED / OPEN / HIGH_STATIC。

**当前主张与实际来源**：净化附表 GROWLITHE 写 SHADOWRUSH/SHADOWWAVE，SNORUNT 写 SHADOWBLITZ/SHADOWSHED。 原附表与固定可选源分别为 GROWLITHE:SHADOWBLITZ/SHADOWWAVE、SNORUNT:SHADOWWAVE/SHADOWSHED。Shadow建立保留配置顺序；RUSH、BLITZ、WAVE都是不同且存在于可选表的招式，不会因存在性检查自动修复错误。131行原表字段对照0差异，净化表2差异；SNORUNT为首判后静态对照发现并再次逐行阅读确认，归同一根因，不另加编号。

**项目定位（固定项目commit）**：
- specs/pokemon-rules/wp23-shadow-data-and-vectors.md:80–80
- specs/pokemon-rules/wp23-shadow-data-and-vectors.md:194–194
- deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md:80–80
- deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md:194–194
- deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md:52–56

**来源定位（固定参考commit）**：
- PBS/Shadow Pokémon backup/shadow_pokemon.txt:55–57
- PBS/Shadow Pokémon backup/shadow_pokemon.txt:511–513
- Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:114–171
- PBS/Shadow Pokémon backup/moves_shadow_pkmn.txt:102–136

**最小静态反例前提**：
- 仅作可选数据条件化合同：对应样本的Shadow目录、18招与类型均已有效注册，保持固定字面内容；没有实际安装/编译/运行这些样本。
- 分别取普通GROWLITHE、SNORUNT，正常建立Shadow，未做额外改招，量表为各自最大4000/2500而H5；其它前序调用正常。

**预期**：
- GROWLITHE 的两招依次为 SHADOWBLITZ、SHADOWWAVE。
- SNORUNT 的两招依次为 SHADOWWAVE、SHADOWSHED。净化表的首招会产生不同的实际可用招式。

**影响**：依据最终附表制作同一可选内容的独立实现会出现错误招式身份、攻击类别/威力和目标规则。

**最小修正**：恢复两行准确的有序招式列表。保留“可选原始样本、非默认启用”的范围，加入这两个具名建立结果，并对131行逐值核对。

**确定复核条件**：
- 131个物种的量表和有序招式逐项与原附表及固定样本匹配。
- 两个H5建立结果与本反例相符，不只核对行数或标识是否存在。

### RUN-A-031 — SH06 的90点香下降缺少储存性格前提

P3 / STATIC_VECTOR_UNDERPREMISED / OPEN / HIGH_STATIC。

**当前主张与实际来源**：W06/SH06 只给Shadow H4、友好度h80、JOYSCENT倍率1、无友好修正，却固定预期量表减90。 下降量按储存Nature身份取表：HARDY为90，LONELY为130。H4与友好度80不能唯一选定这行；本次原附表和净化附表25行性格数据相互及与固定来源均一致，问题在测试前提。

**项目定位（固定项目commit）**：
- specs/pokemon-rules/wp23-shadow-hyper-and-purification.md:193–193
- deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md:155–155
- specs/pokemon-rules/wp23-shadow-data-and-vectors.md:9–10
- deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md:9–10

**来源定位（固定参考commit）**：
- Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:46–90
- Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:108–111
- Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:226–244

**最小静态反例前提**：
- 共同前提：有效Shadow，M4000/G2500/H4，友好度80、有效Hyper假，直接共同香工具倍率1、其它调用正常，无友好修正。
- 对照A显式储存HARDY；对照B显式储存LONELY。两者都满足现有SH06所列前提。

**预期**：
- A量表2410，仍H4；B量表2370，变H3。两者友好度均因调用前H4而保持80；不因下降后阶段改变追补。

**影响**：现有向量把多种合法输入写成一个数值结果，未来验收可误判正确实现。

**最小修正**：在W06/SH06补“储存Nature=HARDY”及需要比较跨阶段时的明确初始G；可另加LONELY对照，不改变正确下降表。

**确定复核条件**：
- 对照完整前提后90与130分别可唯一推出；友好变化门仍使用下降前心阶段。

## 已确认的非新缺陷与保留

保留并回源确认：METAGROSS默认Mega基础HP异常；Shadow暂存EV复制共享；TIMEFLUTE前后门不相交；可选香缺Scent旗标；净化室跨级首窗缺更新方法及此前已提交状态；S0同等级对照；LUGIA分入口差异；替换使用原始Shadow返回值；正常负位置先经成员/Select出口；盒满WITHDRAW与真正到达最终存放后的清中心；心量表快照未随捕获队伍重排。它们已被现有规格如实记录，不把参考异常再次作为规格错误。

未产生运行观察、未证明demo事件链，二者计数均0。U01–U10、G01–G12与既有20 AX全部保留。没有修改reference、正式规格、中央Feature Matrix或批准记录，没有新框架/兼容API/语言转换/行为模拟。A-019旧项按root提供的显式历史状态限定收窄为非阻断建议，A-02保持原件，此协调不影响本批独立结论。

## 交付与下一步

本目录包含report.md、reading-log.tsv、findings.json、source-coverage.tsv、equivalence.tsv、checkpoint.json与不可追改的independent-first-judgment.md。仅本批目录可提交。提交后核对目标remote与远端精确commit；本文件不写自身提交哈希，固定发布身份随回报提供。

发布后先执行已授权X-A-EDIT-CACHE第一阶段，仅读X-A-C01/X-A-EDIT2中性说明并保存独立判断，再请求原结论比较；等待比较时可继续A-05。每次仅一个有界主审批次，不自行派生子代理。
