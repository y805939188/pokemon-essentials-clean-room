# R-B04：B09 受影响 actual 第一轮独立复审

结论 **PASS_SCOPED**。精确被审 actual 为 `dc64807c2d726171827017ec636c6a73efd8e4b5`（tree `6f836ef1e40c1720413b8b1202845320880e0954`），单亲 payload `3ec4af10f9822999b329ac794e4694bc5aa89aac`。候选 C `18873059e56314fcd48f6081d5a65a79301a52f6`，已接受前驱 B `407536adb682a04161d3e9c82f153a62b1becd97`。本报告单亲必须是 actual A；报告 commit 由普通提交及远端读回在外部绑定，不能把报告 HEAD 当成被审 payload。

本轮仅判断 B04 的受影响公共资源／音频／过渡／消息／输入／共享身份交界，以及 actual 的身份、有效资格、公共登记和依赖边界。它不构成完整 B09/R09 的20贡献／13主责复审，也不重放整个 B04 已接受35贡献／23主责。没有新增本范围阻塞缺陷；所有 canonical ID、其他责任批义务和父任务接受门保留。

请求配置为 gpt-6.1-sol / Ultra / 继承 Standard(default)，没有可信有效配置回显，故 **UNVERIFIED**。沿已接受 Plan A；未改配置、未作 quota/auth/config 探测、未增加认证门，未派生子任务。参考、游戏、编译、转换、生成、反序列化、参考行为模拟器、作者或历史 verifier、行为向量执行均为0；运行观察0，Demo链0。

## 精确身份与完整差分

独立重建 B→A **199路径＝24M＋175A**；C→A **112路径＝10M＋102A**。24M是14正式＋10公共；没有删改类型、重命名或范围外新增。175A为73候选历史材料、88五方候选报告和14整合／最终冻结证据。A相对payload只新增三份枚举的冻结JSON；payload与报告版本分开核验。

14正式文件＝8最终正文／目录＋6已具名授权原稿，与 C 逐文件字节相同；B04 当前13正式产物与 B/C/A 相同。五份候选回执的88文件和来源175文件按明确来源commit逐项验证，历史报告没有重写；普通native合并图和最终单亲冻结符合清单。本文的 PASS 来自本容器新读固定参考、actual正文和有效控制，不由相同blob或历史PASS标签继承。

完整未过滤差分保存在 [B→A](baseline-to-actual.diff.gz) 和 [C→A](candidate-to-actual.diff.gz)，包括正式、历史、回执、公共和阶段文件；gzip仅压缩本报告差分。14正式／10公共的辅助差分不是总范围替代。[全路径身份](baseline-to-actual-identities.json)、[正式14](formal14-identities.json)、[B04保持13](B04-current-preserved13.json) 和 [差分清单](diff-manifest.json) 给出commit/path/blob/SHA256/字节数。

新身份审计最终 **2701/2701** 项通过，18条current-hashes另逐项绑定同A。脚本只做Git、文本、JSON及哈希 bookkeeping；未执行任何源行为。此前独立结论在 2,671项通过后冻结，随后增加同批读证及18条哈希核验；见 [独立先判](first-judgment.json) 和 [最终新审计](actual-identity-audit.json)。

## 当前接口静态核对

在本容器新准备参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，核实真实commit/tree后保持只读。完整当前WP39/WP40、28条前后条款、5个保持owner段以及具名相关消费者都重新读过。15组是带前提、唯一预期和相邻反向对照的**未执行静态阅读组**，不是测试通过、分支覆盖或默认内容可达证明；见 [15组与逐项行证据](fresh-independent-static-designs.json) 和 [范围／完整条款](scope-and-impact.json)。

| 组 | 本轮重核结论与保留边界 |
| --- | --- |
| 01–02 | 六入口独立预置、nil与确实储存空文本、地图／全局／默认，直接FromType空请求；引子已有备忘、待播计时及位置查询三分支保持。请求不证声音，播放失败不回滚先提交状态。 |
| 03–04 | 训练家过渡1/3先于参与者确保／缩减；skip、handled override及正常返回清理分开。野生捕获ME/3.5秒目标与训练家抢夺反向对照保持，宿主发声／墙钟未证。 |
| 05–07 | NPC非空全倒前置失败、PP前资格与历史字段、Direct5空处理器登记扣量／使用消息／不退款次序保持；异常无统一回滚保证，战斗消息不取代WP17通用四态。 |
| 08–09 | NearAlly远4可高亮／登记但执行拒绝，类别nil与倒下空文字区别；布局保持是必要前提。SW09全询问条件和确认后合法替补选择保持。B17专业UI仍须自身验收。 |
| 10–12 | 胜利请求先于经验早退，ExpAll提示先于收益计算；单个体4旧+1新摘要无队伍先选层；自动移位先收计划、3v2双席跳过及成功消息保持。既有成长提交不回滚。 |
| 13 | 伙伴实际参与／同一身份储存／玩家删移记录／一次终局，固定例盒A=Y、留队B=空；昵称、菜单、确认、消息前序不变。完整物品映射和其他效果不在B04批准范围。 |
| 14–15 | C071–73的无符号负值／有符号幅值、ACTION导航定位OK、同轮优先序、非正命名上限差异继续保持；正常捕获正上限不抹去反例。必要身份／次序／兼容字符保留，无新富文本、数值、音频参数或全资源安全承诺。 |

## B09-G-O01：独立保留与逐层核对

这是已登记的历史R09报告文字差异，不是新增canonical根因或正式正文缺陷。R09 `report.md:46,54,58` 与 `contribution-review.json#GIR-FD82-B013.independent_judgment` 声称盒A还原X、留队B经历两遍还原后为Y；固定有效B013验收和当前CP21/E14要求盒A=Y、B=空。

本轮从固定源重新读伙伴真实参与、储存保留同一身份、玩家删除／左移／追加、正常终局及战后heal。正常终局只有一次持物写回；after_battle的heal不提供第二次持物还原。具名前提下送盒时A先为X，终局后改Y，留队B为空。无实际伙伴／仅登记未参与对照为盒A保持X、B=Y。当前WP20§6.4、WP38／WP42及CP21/E14保持此限定结果，公共消息／输入前序没有被改写。

独立受影响B05 actual报告 `2790043cc7f605fd58489806ce2dc8c54ffbeb2c` 是同一A的单亲子提交，其 report-only successor erratum明确相同结果；只作为外部只读输入，本轮没有把它整合到A、重写历史或据此批准完整R09。[逐层证据与来源关系](B09-G-O01-independent-assessment.json) 保留全部门：**完整actual R09须显式处理固定资格、源链、当前正文／目录与旧报告／机器判断不一致，父任务C须独立判断该回执；相同blob和PASS标签不能关闭观察。**

## 公共登记、有效资格与后续门

G `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 的有效 current_qualifications、effective_case_constraints、root_adjudications、完整extensions／extension_decisions及 P `41fffb540c6483f5296ea0d33b789b75180d27ed` 的最低验收字段逐项绑定20个B09记录；A059的完整限定前提没有丢失。C071–73额外绑定为B04当前交界控制，不把历史措辞扩大为新范围。[完整控制绑定](complete-control-bindings.json) 提供固定整对象哈希和字段相等证据。

10公共文件保留候选通过／INTEGRATED_PENDING_ACTUAL／五份actual待审的登记边界，并同步已批准静态目录范围。两TSV原150行完整字节前缀保持，新20行为170行；7份Markdown历史正文保持次序和字节；目录README仅两条已批准静态范围行校准并加入待审范围说明。B09接受贡献仍0；B01–08的150记录／128触及ID／96唯一主责、具体最低96/0/0、严格89满足／7待办保持，canonical 229 OPEN／0 CLOSED，没有新根因／AX，未将候选PASS写成actual接受。A059的全部other-batch义务及当前条款版本保留，见 [公共10核对](public10-audit.json)。

当前70读者按原62＋修订8保持次序并精确绑定，历史固定G/P来源使用自身commit；当前10公共另绑同A。B14的72读／6写只是当前评估输入，不是author baseline或写入授权。B09→B14仍串行，即使write/write为0；跨读写六路径／共享003根须在B09-C接受后全72/6重冻结并受影响重核。B04→B07历史串行、以后WP28/WP30和其他caller／条件修改再核本批的门，以及B16 A048/C003/D023、B17专业UI义务均保留。没有派发或释放下游、整合ID、关闭根因或写公共登记。

本轮独立先判后再比AREG的799整合与511输入检查标签／状态；其身份和有界登记结果与新检查相符，但历史跨容器锁、当时远端状态及准备时序仍属自述，不作当前认证；AREG未作新源行为裁决。本轮也知道历史PASS和B05更正输入，不宣称盲审。见 [比对](AREG-check-comparison.json)。

## 阅读与具名限制

[参考身份](reference-identity.json)、[参考新读记录](reference-reading-log.json)、[项目新读记录](project-reading-log.json)、[只含路径／行号的检索](source-searches.json) 给出本容器证据。成功bounded读取计入；失败请求不计，受影响的截断输出已重发，重复读取不加覆盖。完整Git／JSON哈希不等于完整历史正文或全部70输入的人类语义重读。

U01–10／G01–12／AX01–20、八个杯赛名单与pokemon_metrics、二进制／反序列化资料、备份／gen、mkxp／宿主容量、真实素材／字体／声音、动态调用／插件组合、实际地图事件／Demo链等具名未知原样保留。本轮所有PBS内容及未列源段未读，实际媒体与运行输出未确认；合法对象／资源／宿主均属明示条件前提。[配置与完整继承限制](model-and-limits.json)、[后续义务](retained-obligations.json) 不被本次PASS消除。

报告本身的JSON、全部引用新读范围、文件身份和完整差分重建校验已通过，见 [报告校验](report-validation-results.json) 与 [报告文件清单](report-file-manifest.json)。

本报告仅新增 `review/remediation/20261003-prepare/batches/B09/affected-B04-integration-review-1/`，普通提交分支 `remediation/20261003-prepare/review-B09-affected-B04-actual-1`，单亲A；正式、公共、历史产物均不修改。精确报告SHA和远端SHA由交付回执外部提供。父任务收到本范围PASS后仍须等完整R09及其他owner的精确actual回执并自行接受。
