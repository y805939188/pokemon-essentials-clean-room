# WP50／WP51／WP52-A 有限复审与闭合报告

日期：2026-09-28（Asia/Shanghai）。独立 reviewer；Reference/Audit侧材料，非提取侧自检，非WP80 sanitized产物。

**结论：PASS_SCOPED。WP50-R01、WP52-A-R01及BATCH-C01全部CLOSED；WP51限定Reviewed回填接受。无剩余必修、无新增阻塞项。** 可以先按§4回填WP50／WP52-A，再串行 **WP52-B → WP52-C → WP54**，逐包自检、批末统一送审。配套 [管理回填与下一批提示](next-batch-prompt.md)。本会话不代执行回填或新包。

本轮只审两原编号、C01、WP51回填和直接传播；[首审报告](../wp50-wp51-wp52a-review-2026-09-28/report.md)已支持范围继承，前批三个旧摘要观察及其它已关闭项不重开。

## 1. 本轮固定输入

| 对象 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md` | `fcbbca67dafbb1aaa1cfd2560983a6f34830c31c11feccb7688f08b372a395b1` | 31,648 |
| `specs/pokemon-rules/wp50-held-item-effect-coverage.md` | `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686` | 13,855 |
| `specs/combat/wp51-ai-action-selection-and-skill.md` | `baebd58a7f4eed635f685f583fa7b4d21785a9ac13a0a1ee4c2ccd6ec7b6bac5` | 26,784 |
| `specs/combat/wp51-ai-decision-defaults.md` | `5069a3690c6886204ebe9877ff0165e77c4c437fb8273032ac9d6f52bf89c2d0` | 5,472 |
| `specs/combat/wp52-a-generic-numerical-and-status-evaluation.md` | `6c0534fea6d4a18284c1e54a38e413ad010d38291088b0df45d8ac087ca44c9c` | 48,127 |
| `specs/combat/wp52-a-evaluation-coverage-and-data.md` | `a5a13acaf8572fa621b91911430b2286b23340618c72d4b5d2e1522aaf4ec5f9` | 58,772 |
| `planning/feature-matrix.md` | `f2c1a5810dd6fcba6fc7f37f0c0fd5666062f81e8628b70471993cc62d9a1001` | 49,715 |
| `planning/review-manifest-2026-09-19.md` | `a1e818788aa7a55dbceb832271b622e836aa768769de67198dc5ebb31fdded13` | 331,077 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/delivery-summary.md` | `7f2207b4267758a9483bd7042554116192c669061663a07c5178c3ec63c66748` | 9,407 |

提取侧回应另固定：`review/wp50-wp51-wp52a-review-2026-09-28/revision-response.md`，SHA-256 `47dfc20d1d1fe50fc582856b9a6ad83ec9fb3e39dc6f74bcaf7cfdb6b88e95eb`，7,997字节。全部身份见 [input-manifest.json](input-manifest.json)、[current-hashes.tsv](current-hashes.tsv)及 `input-snapshot/`。

实测manifest **611条**、主TSV **515条**的完整哈希／字节／短标签均匹配，无缺失／重复，TSV路径均有manifest登记。本轮固定 **613项输入**，相对首审有11个既有文件变化；WP50覆盖附表逐字节未变。

九份修订diff经内存逐块校验，均精确重建当前文件。三轮589／548／521项快照，以及各轮final-checks列出的13／12／11份reviewer原件未变；final-checks自身也与当前登记哈希一致。31份相关文档 **332条相对链接有效**，登记 **151份JSON可解析**，29条上游／附表绑定匹配。见 [diff-checks.json](diff-checks.json)、[changes-from-v1.diff](changes-from-v1.diff)、[text-checks.json](text-checks.json)。

这些完整性数据用于身份和保护原件，不替代下面的行为裁定。

## 2. 两原编号与C01闭合

S表示 `reference/pokemon-essentials/Data/Scripts/`；只读取证，未执行参考。

### WP50-R01 — CLOSED

被审主稿为§1的 `fcbbca67dafbb1aaa1cfd2560983a6f34830c31c11feccb7688f08b372a395b1`，§4 :74,79–80，V05 :167及V29–V33 :192–196。

回读 `S/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb:212–221,297–323,399–449`，以及 `S/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb:263–275,294–314,338–342,364–440`。当前稿已准确区分：false使半血门不用要求有效贪吃；true才要求贪吃扩展，四分之一默认门保留；两者都不扩大到半血以上。ORAN／SITRUS的false调用与五混乱果≤6／≥7的参数分支均同步。

独立验收：H100的ORAN在HP26恢复至36，在HP50至60，HP51不触发；有无贪吃不改变这三个false分支。SITRUS半血无贪吃至75；世代6混乱果半血无贪吃请求12至62；世代8半血无贪吃拒、有效贪吃请求33至83。新增UNNERVE对照保留先行食果门；普通有效性、canHeal、forced、Nature混乱、RIPEN取整和后置消费各层没有被一并改写。

原错误V05已替换，self／boundary／摘要的当前断言同步；历史错误只保留在明确的首稿／历史记录中。WP28主动道具、WP51主动治疗估量未受本次门槛修订影响。该项闭合，不再要求重提取整个持物目录。

### WP52-A-R01 — CLOSED

被审主稿为§1的 `6c0534fea6d4a18284c1e54a38e413ad010d38291088b0df45d8ac087ca44c9c`，§3.2 :85及N09–N11 :271–273。

回读 `S/011_Battle/005_AI/011_AIMove.rb:336–374`与 `S/011_Battle/001_Battle/001_Battle.rb:458–475`。三个墙分支均已改为目标当前同侧存活场上人数：目标计入，倒下者／空位／后备排除；名义双席布局不再代替此值。

新增对照具名中等技能、普通单目标、会心级0、无幸运咒／禁会心覆盖、无本系／其它修正、未绕墙等条件；墙前量37时，两名同侧存活得到R(37×2/3)=25，只剩目标得到R(37/2)=19。反射壁定位物理、光墙定位特殊、极光幕覆盖两类别并保留优先级，不叠乘其它墙。self／boundary／摘要同步，旧正确的命中96、负会心索引和非致死截断未改。

### BATCH-C01 — CLOSED；WP51回填接受

- WP51 :40及S06 :140已明确后备可伤条件是存在后备／招式／对手的一组合，未要求同时打穿全部对手。回读 `002_AI_Switch.rb:476–498`，条件和局部对照相符，没有把局部通过写成最终必换。
- WP51 :68及S07 :141已具名CLOUDNINE／AIRLOCK和UTILITYUMBRELLA；回读 `010_AIBattler.rb:57–84`，天气到期重估没有被替换成NEUTRALIZINGGAS直接清天气。原能力身份分派的近似差异仍保留。

WP51头尾、默认数据附表及F12-07按首审批准A～E回填限定Reviewed；其默认数值表、登记表和已有23条场景不变。新C01两场景与必要身份级联可追踪，回填后版本未冒称首稿被审对象。WP50、WP52-A在本次裁定前仍保持ReviewPending，未自批。

## 3. 直接回归与本轮限定通过范围

本轮只替换原场景V05，新增十个对照；其余 **100条原场景逐字节不变**。当前WP50／WP51／WP52-A分别33／25／53，共111条，与self输入／期望逐行一致。七个新增常数独立复算一致；先前21项算术与其它已接受行为作为继承证据，不冒称重新执行了完整模拟。

三附表数据表保持不变，WP52-A仅规范化比较两行WP51状态标签。继承首审的32持物族／196展开身份、AI A334登记出现／267评级数据，以及B/C归属和三个前向重复键的独立集合核对。WP50附表连字节都未变，WP51默认表没有借回填修改。证据见 [coverage-checks.json](coverage-checks.json)、[static-vectors.json](static-vectors.json)、[static-checks.json](static-checks.json)。

| 包 | 本轮结论与范围 | Feature |
| --- | --- | --- |
| WP50 | PASS_SCOPED：A～F已述32族持物计算／有效性／普通及强制触发／消费与写回时序、196身份有界合同及注册外具名核心接点；主稿与覆盖附表共同限定通过 | F08-05持有效果子范围，原WP20／47-B等子范围保留 |
| WP51 | 原首审A～E通过继续保留，本轮C01及管理回填接受；不重新扩大为全AI通过 | F12-07限定范围 |
| WP52-A | PASS_SCOPED：A～F通用失败／评分合成／22通用修正、粗数值、阶级／状态／类型能力评估与具名数据，164效果身份、334登记出现；主稿与附表共同限定通过 | F12-08仅A子范围，B/C尚未审 |

上述仍是静态有界范围。完整AI、设施、所有规则组合、动态等价和运行没有因本轮闭合而自动通过。限定通过集合为 **WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP51（WP47为A/B）、WP52-A、WP59–WP60**；不得把WP52整个族写成已完成。

## 4. 管理回填与下一批

先重新实测§1九件与本轮快照一致，再将WP50主稿／覆盖附表和WP52-A主稿／覆盖数据附表登记 **Reviewed（限定静态范围，2026-09-28有限复审PASS_SCOPED；管理性回填）**。只按§3范围回填；WP51当前通过状态保留，其对WP50的必要状态与完整身份引用可同步。

F08-05和F12-08按相应子范围Reviewed＋前向Inventoried，不能整行宣称所有相关域完成。保留首稿、被审修订稿和回填后字节的完整身份，当前v2被审哈希不能用新回填哈希替代。头尾状态／身份级联与自有活动摘要、manifest、TSV分别留差异，不覆盖reviewer原件或旧回应。追加场景的表格排版可随回填整理，内容和ID不变，不另列行为修订要求。

随后按 `planning/extraction-plan.md:122–123,130` 串行 **WP52-B → WP52-C → WP54**：

| 包 | 计划完成依赖 | 本批任务 |
| --- | --- | --- |
| WP52-B | WP51、WP45、WP46、WP49、WP50 | 场地／伤害恢复／多目标的具体AI评估 |
| WP52-C | WP51、WP47全部子包、WP49、WP50 | 物品／复制调用／行动控制的AI评估 |
| WP54 | WP25、WP30、WP39、WP44 | 个体／队伍／子集参赛资格、等级调整与杯赛条款 |

上述完成依赖的相关限定范围均已有独立结论；WP52-A可作为共用评分输入。WP54的规则合同为后续设施会话提供基础，不在本轮扩展成WP55会话。三个新包均须逐包自检固定，再批末统一ReviewPending送审；B/C以前的目录定位不算已经提取或通过。完整要求见 [next-batch-prompt.md](next-batch-prompt.md)。本报告不提前批准新包，也不代执行它们。

## 5. 证据分层与操作边界

[source-checks.json](source-checks.json)记录41个源／数据路径与固定commit blob一致；本轮只有6个路径作上述定点正文回读，其余仅身份回归、行为证据继承首审。提取侧声明、首审记录、本轮源码核对与手工验收分开。下一批文件清单定位仅作计划输入，不算行为审查。

Reference HEAD为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，普通Git状态为空。本会话只新增本review目录；未改规格、矩阵、计划、manifest、旧审查或reference。未运行游戏、参考Ruby／表达式、解释器／事件脚本、生成器、编译器、转换器、插件或真实网络，未操作真实地图／存档／输入，未创建任务／并行Agent、发消息、提交或推送。

Demo、宿主、媒体、插件、U01–U10及WP78→WP79→WP80出口继续保留。最终稳定性与产物身份见 [final-checks.json](final-checks.json)。
