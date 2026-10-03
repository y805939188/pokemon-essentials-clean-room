# WP50／WP51／WP52-A 首轮独立审查

日期：2026-09-28（Asia/Shanghai）。独立 reviewer；Reference/Audit侧材料，非提取侧自检，非WP80 sanitized产物。

**整体结论：REQUEST_CHANGES，暂不启动下一批。仅两项必修：WP50-R01、WP52-A-R01。WP51主稿及附表的A～E限定静态范围 PASS_SCOPED，可按§5管理回填；另有BATCH-C01两处非阻塞维护。** 配套 [有限修订提示](revision-prompt.md)。

前批三条旧摘要同步、C01及WP46／47-A／47-B回填均接受；已关闭的WP47-B-N01/N02、BATCH-N03不重开。新问题分别改变实际果实触发阈值和AI墙类估伤，不是要求重做首审或追求措辞统一。

## 1. 被审版本与完整性

| 对象 | 完整SHA-256 | 字节 |
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

实测manifest **587条**、TSV **491条**的完整哈希／字节／短标签匹配，无缺失、重复；TSV路径均被manifest登记。本轮固定 **589项输入**，20个既有文件变化。见 [input-manifest.json](input-manifest.json)、[current-hashes.tsv](current-hashes.tsv)、[changes-from-previous.diff](changes-from-previous.diff)和 `input-snapshot/`。

18份回填diff在内存逐块校验，均精确重建当前文件；前轮548项、再前轮521项快照未变。两轮final-checks所列12／11份原件未变，final-checks自身也与当前登记哈希一致。旧WP40号令普通入口、WP41反射0击／野生破替身对照，及鸟嘴加热、来源区间、神秘守护责任均按前轮批准合同同步；其它旧稿只级联必要完整身份。详见 [diff-checks.json](diff-checks.json)和 [backfill-changed-lines.json](backfill-changed-lines.json)。

本轮扩大到30份相关文档的 **316条相对链接有效**（与提取侧281条的选择范围不同，不是坏链）；登记 **141份JSON可解析**；新稿29条上游／附表绑定匹配；101条场景与self的输入／期望文本一致。**文本匹配不能证明期望正确，WP50 V05就是反例。** 证据见 [text-checks.json](text-checks.json)。

## 2. WP50-R01 — false参数取消贪吃要求，不是取消半血门

**对象**：WP50主稿，SHA-256 `937551e00ec61a8a807bfa197ece1e2f91b6b5f91f620375e6c14ea900e9027a`，§4 :74、:79–80、V05 :167；直接传播到self、摘要关于“四分之一门”的断言及其它同句概括。

当前稿明确说false参数禁止GLUTTONY扩展、ORAN／SITRUS非强制只在四分之一触发，并给HP26/100不触发的V05。该解释与源相反。

**证据**（S＝`reference/pokemon-essentials/Data/Scripts/`）：

- `S/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb:217–221`：先查食果资格；四分之一以下通过；四分之一至半血之间，在“未要求检查贪吃，或贪吃有效”时通过。所以false使半血门**不要求**GLUTTONY；true才要求它。
- `S/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb:364–404`：ORAN和SITRUS的非forced入口传false。canHeal、可食果、普通物品有效性仍各自生效，不能理解为无条件吃果。
- `AbilityAndItem:399–409`：五种混乱恢复果传“世代≥7”为该参数，因此≤6传false，同样是半血不要求贪吃；≥7传true，普通无贪吃四分之一、有效贪吃半血。恢复量世代分母是另一条规则，不随阈值解释一起改。

**影响**：原稿漏掉四分之一以上至半血的普通橙橙果／文柚果触发，也错误描述旧代混乱果。它会改变回血、果实消失、颊囊／共生等后置能否开始，不只是布尔参数命名。

**最小修订**：把参数解释改为“是否要求贪吃才能扩展到半血”；同步两个false调用者、五果世代分支、V05和当前自检／摘要。保留forced与非forced、canHeal／可食果、恢复量／RIPEN取整、Nature混乱及消费顺序的已正确合同。不要扩改WP28主动道具或WP51治疗估量；相同物品不等于同一入口。

**静态验收**（普通物品有效、可恢复／可食果、无额外连锁，除所列条件外固定）：

| 输入 | 预期 |
| --- | --- |
| ORAN，H100，HP26，无或有GLUTTONY | 均触发，恢复10至36；不是拒绝 |
| ORAN，HP50／51 | 50触发恢复至60；51不通过低HP门，GLUTTONY不扩大到半血以上 |
| SITRUS，H100，HP50，无GLUTTONY | 触发，恢复25至75 |
| 混乱果，世代6，H100，HP50，无GLUTTONY | 触发，请求12；无其它条件时HP62；Nature混乱另查 |
| 混乱果，世代8，H100，HP50，无／有效GLUTTONY | 前者不触发；后者触发，请求33至83 |

forced跳过低HP／食果门的现有边界不变；强制满HP混乱果等已支持场景保留。仅手工分支与自有常数算术，不执行参考helper。

## 3. WP52-A-R01 — 墙类粗伤按存活场上人数，不按名义布局

**对象**：WP52-A主稿，SHA-256 `f7f400c642d77f29c5411ac156fe0e49716848b87ed232b02b8d418e1c67126a`，§3.2 :85“侧规模>1用F×2/3，否则÷2”。

**证据**：`S/011_Battle/005_AI/011_AIMove.rb:336–355`分别对极光幕、反射壁、光墙调用`pbSideBattlerCount`；`S/011_Battle/001_Battle/001_Battle.rb:458–460,474–475`按非空、未濒死、同侧场上集合计数。名义side size、空席位和后备不是这个值。

**影响**：双席布局只剩目标一名存活时，本稿会按2/3预测，实际此估算按1/2；会改变后续伤害分及可能的动作偏好。这不是AI与真实规则的允许近似差异，而是规格与AI源本身不符。

**最小修订**：改为“目标当前同侧存活场上人数大于1”，说明计入目标及其它存活同侧者，排倒下／空位／后备；三个墙分支统一。保留中等技能、预计非会心、无穿墙能力、招式不忽略墙、极光幕优先及物理／特殊墙类别门；不重写WP43或已审WP49的正确计数规则。

**静态验收**：固定名义双席布局，中等技能、L50/P80/A100/D100、单目标、零阶、会心级0（无幸运咒／禁会心覆盖）、无本系／天气／其它修正、相应墙为正，墙前量37：

| 仅改变目标同侧存活场上人数 | 粗伤 |
| --- | ---: |
| 2人 | R(37×2/3)＝25 |
| 1人（另一成员倒下或空位） | R(37/2)＝19 |

反射壁用物理、光墙用特殊、极光幕用适用的普通伤害分别定位；无需运行评分器或复制整套伤害函数。新增对照并同步self／boundary和相关摘要即可。已正确的会心负下标、命中整数96、末端非致死截断等范围不重开。

## 4. BATCH-C01 非阻塞维护与其余已支持范围

### WP51两处条件表达

- **:40后备可伤谓词**：将“不被任一对手吸收”明确为“存在一个后备、其中一招伤害招、对至少一个对手未被吸收近似阻挡”。`002_AI_Switch.rb:476–496`命中一个这样的组合便停止寻找，不要求同一招对全部对手都可伤。当前范围按此存在性解释接受，随回填对齐文字即可。
- **:68天气抑制名称**：将“气体”具名为CLOUDNINE／AIRLOCK的天气抑制，另列UTILITYUMBRELLA；`010_AIBattler.rb:60–65`重估天气到期并不在此直接把NEUTRALIZINGGAS当清天气门。保留本段“能力身份分派不统一先有效”已确认差异。

不为这两处再要求整个WP51首审。它们随本轮有限修订／管理回填同步，不改已审战斗能力主规则。

### 目录、数据与行为支持

WP50的32族、165直接／21复制、展开196个（族，物品）身份、两个空族和36条宝石／减伤果映射均与源文本匹配。除了R01阈值及传播，已支持其P/A/D/F槽、普通／强制入口、LEPPA持久与战斗同位PP直接写入例外、MICLE反向标记门、STARF先抽后查、红牌先耗再拒、不同退出道具资格、回收与还原记录及具名阶段消费者。

WP51的A～E主稿与附表**PASS_SCOPED**：控制／技能／标记、决策顺序、15个普通换人意愿／否决入口、替补评级、回合末近似输入、主动道具分类／排序／错误字段边界、Mega登记、候选／目标／加权／无候选／零权重区分及本批直接交界。14项HP估量的两配置分支、32项X道具、15条换人登记顺序匹配；不把状态治疗布尔方向、SITURUSBERRY拼写或MAXMUSHROOMS取错组按理想策略修正。

WP52-A除R01外已支持共同失败／目标合成／22通用修正、粗速度／会心／命中／伤害骨架、阶级helper、具体状态／类型／能力评分及有界数据。独立注册扫描12文件784语句，展开786出现／783不同键；A334、WP51已有15、B247、C190，三个重复键与附表一致，均在B/C边界留待后审。A侧164效果身份的索引／来源、267条基础能力评级数据匹配；这不证明未展开B/C已通过。

101条场景逐条核对文本及所列行为；21项交付常数算术复算一致，但没有覆盖R01真实门槛反例。检查见 [coverage-checks.json](coverage-checks.json)、[static-vectors.json](static-vectors.json)和 [static-checks.json](static-checks.json)。不同证据的含义分开，不能把“集合无遗漏”当作“每条行为都无误”。

## 5. 有限修订、WP51管理回填与停止点

修订只按 **WP50-R01、WP52-A-R01、BATCH-C01及直接传播**推进；不要重做新三包首审，也不重开前批闭合项。

本轮允许WP51主稿与数据附表按上述A～E范围回填 **Reviewed（限定静态范围，2026-09-28首审PASS_SCOPED；管理性回填）**，F12-07同样限定Reviewed＋前向Inventoried；C01两点与状态回填分别列差异。WP50及F08-05持有效果子范围仍ReviewPending；WP52-A及F12-08该子范围仍ReviewPending，已有其它子范围不退回、B/C前向不关闭。

保留六件被审首稿完整身份，新修订和WP51回填后哈希不得冒充本轮被审值。WP50／51变化须级联WP52-A及当前self／boundary／摘要／矩阵／manifest／主TSV。新增 `revision-response.md` 和相对本轮 `input-snapshot/` 的差异；原报告／提示／checks／快照及旧回应原件不得覆盖。

修后静态验收、全量身份／集合／链接／JSON和快照保护核对，然后只统一送两原编号及C01／WP51回填差异复审并停止。**本轮不授权WP52-B/C或其它下一批，不创建任务／Agent、不发消息、不提交／推送。**

原限定通过集合保持WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP49（WP47为A/B）、WP59–WP60；本轮新增WP51限定通过，不能写成WP50–52整批连续通过。

## 6. 本轮证据与操作边界

[source-checks.json](source-checks.json)记录41个源／数据文件与固定commit blob一致；33条本轮实际读取或检索，其中27条有行为正文／具名数据阅读、6条仅登记边界扫描，其余身份回归。未照抄提取方的读取声明；代码分段展示时省略空行和纯注释，未执行参考。旧已审消费者依相应范围继承，不声称重新全文读整个引擎。

Reference HEAD为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，普通Git状态为空。本会话只新增本review目录，未代改规格／计划／矩阵／manifest或旧审查。未运行游戏、参考Ruby／表达式、解释器／事件脚本、生成器、编译器、转换器、插件或真实网络，未操作真实地图／存档／输入，未创建任务或并行Agent，未发消息／提交／推送。

Demo、宿主、媒体、插件、U01–U10及WP78→WP79→WP80出口保留。最终输入稳定性与产物身份见 [final-checks.json](final-checks.json)。
