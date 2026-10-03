# WP55／WP56／WP57 v2 有限复审报告

2026-09-29；独立 reviewer。reference固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

**结论：批次仍为REQUEST_CHANGES，但原13项已有11项CLOSED。仅余WP55-R02的一句引用写入总述、WP56-R04新增的Palace结算否认。WP57自身范围PASS_SCOPED，可以管理性回填；暂不启动下一批。**

C01与继承C02关闭；C03为非阻塞的场景／来源记法维护。其他已接受行为不重开，下次只检查本报告§3剩余点、WP57回填及直接传播，不重做首审。

## 1. 本轮固定对象

| 对象 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| WP55 v2 | `0bcff15b2e5683a3b9b96c621ba650b55220131dddf34957d75c39caf83557c7` | 27,698 |
| WP56 v2 | `8ed7940bdd732e8d960a7c5292e1baeacc27489c34dc67f15ffe0501fb4966b0` | 21,274 |
| WP57 v2 | `7e69ccdccb422d1b04799990041a3745d747ebab3a765b8f7d686ad4f270ef8b` | 14,776 |
| feature-matrix | `b97ed8836dd510b8f0c2ca8f0485cf03a01737d2fb515b6d4f0e65a3a56684cc` | 51,500 |
| manifest | `b390f14890a2b5486a70be39d53660757f5b3fe863a770cca4961771f2b1b4e3` | 390,315 |
| 本批摘要v2 | `0fcab05d9f13dd9109bf70c699b7c6159dcca43e766524e5529855bc54909ac8` | 6,514 |
| 本批self v2 | `36704503193cadbd3120ceabf3e2b38cd26274f90ad29f9dd18e7367aa026cb3` | 20,320 |
| 本批boundary v2 | `8c2033a751f405376cf2375c033c5d6d691e61ff9f296995c71594c9cc49c64c` | 8,670 |
| 主TSV v33 | `0f8113065947f4b94c3ed8cf8d0ea9db8ef53160b7d1728fce7abe56028c2333` | 87,544 |

固定734项输入，实际路径／完整身份及快照在 [input-manifest.json](input-manifest.json)、[current-hashes.tsv](current-hashes.tsv)、[input-snapshot/](input-snapshot/)。manifest有732条可核完整身份，TSV636条均匹配；两个“见原件”占位不冒充哈希条目。相对首审707项输入仅12个原有文件变更，见 [changes-from-v1.diff](changes-from-v1.diff)。

本轮只读原13项的实际修改和必要直接消费者。33个先前相关源／数据文件均与固定commit及首审字节一致；其中17个路径本轮定点回读，其余继承首审限定证据。没有执行参考代码，也没有以提取侧回应直接判通过。

## 2. 原编号逐项结论

以下源码简称沿首审报告：Challenge／Data／Choose／Battles／Swap为`018_Alternate battle modes/001_Battle Frontier/`的五个对应文件，Palace／Arena为`011_Battle/008_Other battle types/`的两份变体文件；完整路径和本轮范围在 [static-checks.json](static-checks.json)、[source-checks.json](source-checks.json)。

| 编号 | 结论 | 本轮核实 |
| --- | --- | --- |
| WP55-R01 | CLOSED | Challenge:95–104、131–132、205–228、243–267及Battles:64–96支持：单场只回胜利布尔，会话决定／加胜独立；暂停与进行中并存；决定0不阻止开始／暂停／继续保存。§2.2／2.4／3与W26／27已同步 |
| WP55-R02 | 部分接受，仅§3.1剩余 | 空列表真值、nil取消保留、未开始结束置nil、引用保存均已正确；第46行仍保留不正确的全称写入保证。W28入口命名另列非阻塞C03 |
| WP55-R03 | CLOSED | Game.save:111–125与Challenge:306–318的捕获false／未捕获异常分层正确；W33／34没有再把所有失败统一为传播或回滚 |
| WP55-R04 | CLOSED | Challenge:18–42、79–82、139–142、324–343支持字符串比较失败与未初始化配置读取项；§2.1／2.2及W32已修 |
| WP55-R05 | CLOSED | Choose:26–33、59–82与RubyUtilities:366–388支持数值0随机入口和短／长名单分支；W06／08／31及正文已修，不再声明抽样处统一立即失败 |
| WP56-R01 | CLOSED | Palace:105–139实际A与2A+D；CommandPhase:42–64的玩家安可分流与自动返回已区分。P01–03／P27和三组阈值均正确 |
| WP56-R02 | CLOSED | ActionSwitching:274–279、Battler_Initialize:60–63／234支持换入清Pinch；同次在场回血不清。§2.3、P08／23、差异表一致 |
| WP56-R03 | CLOSED | Palace:184–243的最佳后备早返跳过标记写入、后段赋值与回退已分列；P09／12／24／25正确 |
| WP56-R04 | 部分接受，仅§3.2剩余 | skill覆盖、protected保持、攻击阶段清理、回合末累加、整体失败早返均已修；新差异表却错误排除Palace共用结算 |
| WP56-R05 | CLOSED | Arena:96–109、142–200和Battler.hp=:107–109支持三具名心分负项、2/0与1/1、HP直接写穿；P13／17／18及self总分正确 |
| WP57-R01 | CLOSED | Choose:154–158→Data:201–217→Pokemon:1198–1205为默认Owner；Challenge分队及Swap交换不改Owner。WP57与WP55第96行已同步 |
| WP57-R02 | CLOSED | Challenge:414–423计数有成功守卫、setParty无条件；Swap:208–244两屏退出均有确认。正文、F11及WP55第100行直接传播已正确 |
| WP57-R03 | CLOSED | Choose:100–124、144–164的N端点、nil模板创建失败、成功路径才还原已说明；F16／17正确。§5失败类型的括注记法另列C03 |

WP57依赖的具体创建／计数／队伍提交／恢复入口已在本轮独立核实；WP55待修的是上层总述，不能因此把WP55整包标通过，也不需要撤销已独立成立的WP57子范围。

## 3. 仅剩两处必修

### 3.1 WP55-R02：第46行的全称保证仍漏列开始和取消

被审文件为§1 WP55完整哈希 `0bcff15b2e5683a3b9b96c621ba650b55220131dddf34957d75c39caf83557c7`。位置：[第46行](../../specs/combat/wp55-facility-session-and-restoration.md:46)。

该行仍称：**“除‘进行中的报名／租借提交’与结束路径外不改玩家队伍引用”**。这直接否定了同文第51行开始替换和第53行取消恢复，不是单纯措辞偏好。

本轮回源：`018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb:200–203,225–228,270–281`，写玩家队伍的四个具名入口分别为进行中提交、开始时有报名值的替换、取消时有原队伍的恢复、结束时无条件恢复字段值。开始／取消不是仅靠提交入口发生的写入。

**最小修订**：删除这句错误排他保证，或按上述四入口及守卫改写；无需改已正确的§2.3或重做原空列表／nil修订。静态验收沿现有W10／W13：原队伍P、报名Q且两者不同，开始后玩家队伍Q；取消后P。不变量必须允许这两次赋值。除此之外，本项原已修范围接受。

### 3.2 WP56-R04：新增“Palace不走该结算”与继承调用链不符

被审文件为§1 WP56完整哈希 `8ed7940bdd732e8d960a7c5292e1baeacc27489c34dc67f15ffe0501fb4966b0`。位置：[差异表第121行](../../specs/combat/wp56-palace-and-arena-variants.md:121)，Palace栏新增 **“无（Palace不走该结算）”**。

本轮新证据：

- `011_Battle/008_Other battle types/003_BattlePalaceBattle.rb:4,61–65,160–164`继承普通Battle路径；其专有改动不跳过普通战斗者创建／出招成功状态结算。
- `011_Battle/001_Battle/002_Battle_StartAndEnd.rb:109–118`共用创建SuccessState；`010_Battle_AttackPhase.rb:176–184`清理；`002_Battler/007_Battler_UseMove.rb:248,431–438,512–520`写状态并结算，均没有排除Palace的类型门。
- Arena:127–133才是额外的“将当前skill槽累加到裁判技分”消费。Palace没有这一Arena裁判消费，不等于没有成功跟踪／结算。

**最小修订**：该格改为“沿普通战斗建立／更新并结算成功状态；不作Arena裁判技分累计／评判”或等义表述。保留§3.1已正确的覆盖、protected保持和早返区别。静态验收使用正常Palace（含相应可记录变体）、合法招式、无提前返回且确实到达共用结算入口：成功状态会更新／结算，但不进入Arena三回合裁判；不得用“无力−2”等提前失败个案否定整个模式的共用路径。

## 4. 非阻塞维护

**C01、继承C02均CLOSED。** W19笔误、阈值方向和14件计数已正确。旧self v4的artifacts六项、packages三项及对应向量已与当前规格匹配，没有上一轮B／C两条旧身份残留。旧范围不再重开。

**BATCH-C03（本轮非阻塞；随修订／回填维护，不增加行为复审门槛）**：

1. WP55 W28（第192行）“直接提交空列表……整体返回假”应具名入口。`Challenge#setParty`及其转发没有布尔false转换，直接赋值的返回与`Data.rb:38–49`报名包装把空界面结果转换为false不同。若仅测队伍状态，可删除返回值期望；若意图测报名包装，写明“包装接收到ret=[]的工具边界”，不声称正常多选可达。此处空列表写入和之后开始替换的主体行为已接受。
2. WP57第63行把“整体校验永不过”放在“中途报错”的括号里；§2已明确这是无上限重试。同步为“异常或持续重试未返回”即可，保留不还原临时人数的边界；不为此改区间数据或重审生成规则。
3. 提取侧旧revision-response的WP57-R02误引`002_Challenge_Data.rb:200–203`作为setParty位置，实际为`001_Challenge_BattleChallenge.rb:200–203`。在新回应勘误，旧回应留史，不改reviewer原件。

## 5. 独立检查与分包状态

| 检查 | 本轮结果 |
| --- | --- |
| 当前登记 | 732条manifest与636条TSV完整身份／字节／短标签匹配，原路径顺序保留；两表新增27项集合相同 |
| 修订差异 | 10份均从首审快照在内存逐块重建到当前字节 |
| 当前场景 | WP55 34、WP56 27、WP57 17，共78；相对首审仅相关原场景修订及16条新增，无删除 |
| 原始数据 | Palace25行双表、训练家15行表、Factory8行双域表均未变 |
| 独立常数 | 重新核对61／129、22／64、90／185与Arena4／2四组，均正确；没有重复运行其余无变化检查 |
| 当前引用 | boundary13条与三稿13条内嵌依赖身份均匹配；提取侧30条源身份和三稿身份匹配 |
| 文档完整性 | 193份已登记JSON可解析；当前specs＋矩阵380条相对链接存在；这是明确范围，不与用户扫描347份JSON口径混同 |
| 历史保护 | 707／677／644／613／589／548／521七轮快照及各自已列reviewer artifacts未变 |
| reference | 33个相关文件与固定commit及首审字节一致；HEAD正确，普通Git状态为空 |

检查记录：[diff-checks.json](diff-checks.json)、[propagation-checks.json](propagation-checks.json)、[coverage-checks.json](coverage-checks.json)、[identity-checks.json](identity-checks.json)、[source-checks.json](source-checks.json)、[static-checks.json](static-checks.json)。哈希、场景数量和算术匹配均不代替行为判断。

分包状态：

- **WP55：REQUEST_CHANGES**，仅WP55-R02第46行总述；原其他四R关闭。
- **WP56：REQUEST_CHANGES**，仅WP56-R04第121行新增回归；原其他四R关闭，R04主体修正接受。
- **WP57：PASS_SCOPED**，R01／R02／R03全关闭。通过范围为A～F候选域／数量／IV／合法性与失败、租借选择、交换配对／取消／计数／引用提交、默认Owner、原队伍隔离和WP54／WP55／WP25的已述直接交界。完整设施演出、事件、运行、回放和生成器仍前向。

允许提取方按本报告管理回填WP57头尾与F13-05具名Reviewed，保留被审v2完整身份，维护C03第2点与实际依赖引用，回填后新哈希不得冒称本轮被审对象。WP55／WP56和F13-04仍待上述两点；不因WP57通过扩为设施整体通过。

## 6. 下一步与停止点

仅执行两处剩余修订、C03维护、WP57管理性回填及必要身份级联，统一送短复审；提示词见 [revision-prompt.md](revision-prompt.md)。**不启动WP58或其它包，不重新审已关闭11项。**

WP57回填后可在原限定通过集合上增加WP57，不能写“WP54–57全部通过”。Demo、宿主、媒体、插件、U01–U10、真实地图／存档／输入／网络、WP78→WP79→WP80继续保留。本会话只在新review目录写材料，未代修规格／矩阵／manifest，未运行参考，未执行回填或下一包，未创建任务／Agent、未发消息、未提交／推送。
