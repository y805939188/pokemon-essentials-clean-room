# R6-U11 独立证据与载荷审计

结论：**ARTIFACT_IDENTITIES_AND_REMOTE_READBACK_PASS_SCOPED_STATIC**。作者21份evidence、manifest、四份mirror差分、931条旧目录表行、20份core加5份publication载荷均完成独立核验；25份新鲜远端完整内容共463,567字节与冻结Git对象逐字节、SHA256及Git blob相等。没有因这些核验自签候选行为PASS、整合PASS、正式接受或CLOSED。实际模型／effort／tier／speed／平台UUID均为 **UNVERIFIED**。

## 固定绑定与本人读集

本审计路由任务为`/root/evidence_audit`，非作者。冻结publication P=`e93d0e56750a6a16cc50cc68b2c97f11ea255153`、tree=`930b677271ddfb2f8833a0deac79d87b6d01c157`；语义C=`54af598ca85211641348e6057ed0c348044787fe`、tree=`7ef921cc86dcad69213ec4bbf2d43810f9d60faf`；父基准B=`469a268b92daed7b4d28d7fd0da75520cbb7228f`。固定formal main=`8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，R=`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。实际cwd=`/workspace/pokemon-essentials-clean-room`。

根AGENTS全文297行已读；`/workspace/AGENTS.md`、仓库`.agents`／`.agents/skills`／`.codex`缺失。本人完整读reviewer prompt全部3446行、214824字节（SHA256 `bfc9b60c7b006e1fdd2205b55d0cb21198aa4366e0aa4c4c5eecc82aa111e030`，blob `cd1d62ebaec092af61a76918a4abe6c6d41e1e9d`）。其中合同2016行与独立`contracts/R6-U11.json`逐字节相同：101881字节，SHA256 `4ca9174de80cf3928468fe7dd2e89eec99a606bc702cf138f82db99f85a866d3`，blob `cb364ae2583f408901e6d4e750793ee7205745b9`。通则与三ID七组、完整原提案、证据要求、scope与接收边界均读取，不以摘要替代。

本人完整语义读取作者21份evidence（包括44行reading-ledger、三个utility脚本、per-ID七组、全部publication记录）；脚本只读文本，未执行作者脚本。本人完整读取四mirror和四formal的Git字节以作独立身份、差分和表行核验，不将完整字节读取当作本人全文语义批准。本人另完成UI目录formal1–243与candidate1–243的联合全文语义阅读：两完整Git blob先分别取得，前243行逐字节相等；连续1–90、91–180、181–243完整展示，共37303字节。MG／DT／PG／PL／NV／CH／TC／PT的范围、取消与失败前缀、素材／宿主未知、A41当前盒写入保留均未变；本读集不声称本人全读UI945行或全部外域源。完整双坐标与身份见`ui-catalog-prefix-read.json`。

指定参考对象库`/workspace/pokemon-essentials-reference-r6`实际不存在。所需R对象已在clean-room对象库中，全部用固定Git blob只读取得；本审计未fetch参考、未checkout、未执行参考或游戏。本环境没有本机Mac工作区观察能力，不借当前clean-room状态证明Mac历史保护。

## 独立核验结果

| 类别 | 独立结果与精确范围 |
| --- | --- |
| 作者配置及身份 | snapshot/报告都明确请求gpt-6.1-sol／xhigh／default普速、实际全部UNVERIFIED；未冒充实际配置。本审计合同请求gpt-6.1-sol／ultra／default普速，实际同样缺有效回显，未运行CLI配置探测。路由task不作平台UUID。 |
| 作者输入prompt | 作者A prompt为215316字节／3448行，SHA256 `ba7a90019e999a1a2b141a0443a9aed9ba5a7c00662fbb16c29afd6cbd7da54f`，blob `bd9edf17c1cb0835b5bb6566ae540ae4ccb7e45a`，与B固定对象相等；不与reviewer214824字节身份混淆。声明10段连续覆盖全3448行；没有作者原工具transcript，不能据此独立证明作者实际语义交付。 |
| manifest | 19条恰等于C的20变更路径减manifest自身。19条bytes／SHA256／Git blob／mode与C对象全部一致；manifest自身由有限publication回执绑定，不递归自哈希。P另加5份publication证据是具名分期，不要求把它们倒填入语义core manifest。 |
| 固定源/formal身份 | 作者fixed-payload-validation全部11项由独立Git字节、Python hashlib和Git entry复核，bytes／SHA256／blob／tree／mode均一致；不以身份核验替源语义PASS。 |
| per-ID原裁决 | UI-ST-001／003／005均保持required/P2；原identity_and_verdict与合同逐对象相等；三ID全部七组存在，无新增根因或optional/policy接受。 |
| 变更权限 | B→P恰25路径：C20＋P5，均在本批candidate allowlist；实际formal、audit、planning、reference树没有该两提交造成的差异，四实际formal仍等固定main。该检查不证明未登记瞬态写入、历史非提交写入或不可见Mac写入从未发生；INC-R6-001没有清零。 |
| 931旧表行 | 领域目录208＋UI目录723＝931，**包含表头与分隔行，不能称931业务向量**。逐原始字节（含LF）与原顺序全部保留；候选分别213／742表行。完整逐行双坐标与row SHA256见JSON。新15条UI设计及3条领域同步行也不成为18条独立执行向量。 |
| 正确历史span | 搜索§6.2–6.3、物种/页§7.1、暂持/整理§3.2–3.3、退出§4.4、WP62逐入口§3.4、地图/掩码§5.3、形态资格完整原段七块均独立逐字节相等；旧表行和原历史证据未改。历史语义资格由root/领域审者另核，本证据工具核验不代R1–R5回源验收。 |
| 作者reading-ledger | 44条输入均重新从固定对象取得；每条bytes／SHA256／blob、range或JSON pointer、可重建stdout SHA256全部匹配；所称8主全文读集的连续区间覆盖完整。没有作者原始工具stdout归档，不能把声明重建当作作者输出绝未截断、实际阅读或理解的独立证明。 |
| 远端core20 | fresh GitHub fetch_commit取得C相同SHA及准确20变更路径；作者core-readback20项与C对象全部匹配，共439832字节。其声明raw tree字段未由connector暴露的限制准确保留。 |
| 远端publication5＋全25 | fresh fetch_commit取得P相同SHA及准确5publication路径；fresh25次fetch_blob完整UTF-8内容，在独立捕获后用Python SHA256和Git blob SHA1重算，25/25逐字节相等，总463567字节，其中publication23735字节。当前origin作者branch独立ls-remote返回P。 |

远端核验没有复用作者JS SHA256程序，也没有依赖push exit0、branch存在、remote-tracking ref或截断diff作为完整载荷证明。`remote-full-content-capture.json`保存25次完整返回内容及UTC；`remote-commit-binding.json`保存C/P路径绑定。connector不单独暴露raw tree／mode：相同完整commit SHA绑定本地独立核验的不可变Git tree；mode/type/path来自该固定tree，此限制没有改写成直接远端字段暴露。

## 四份mirror准确差分

| formal路径末段 | baseline→candidate行数／字节增量 | 有效差分（基准行→候选行） |
| --- | --- | --- |
| pokemon-rules/wp62-pokedex-records-regions-and-content.md | 190→192；+405字节 | 基准173行后插candidate174–175：§6.1交叉引用、记录接点、R6-PD同步。 |
| test-catalog/pokemon-rules-wp53-60-61-62-69-70.md | 269→281；+1738字节 | 基准150行后插candidate151–162：R6-PD01–03及静态共同前提。 |
| test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md | 914→945；+5985字节 | 基准286行后插candidate287–317：R6-BX01–11／R6-DX01–04及共同前提。 |
| user-interface/wp66-b-storage-and-pokedex-ui.md | 300→313；+2897字节 | 基准65→candidate65–76；89→100；104→115；239→250；基准282后插candidate294–295。对应§3.1、§4.1、§4.2标记、§7.2与目录引用。 |

四baseline mirror等固定formal；四candidate均有实际变化，没有未声明第五formal路径。完整独立统一差分见`mirror-diff.patch`。上述差分仅描述实际变更，最终行为裁决由本批source/formal审者完成。

## 九份原反证的当前独立补读

委派当前非作者子任务`/root/evidence_audit/counter_payloads`完整语义读取全部9载荷，9/9 bytes／SHA256／blob及冻结P字节一致；不是复用作者dispositions摘要。大型EV-156全部320对象、8627物理行语义内容按原序八段逐对象所有键值读取，77 party／120 storage／123 Bag/Mart，全部原source_read_credit_to_K=0保留。9载荷及每对象原行范围完整身份在`counter-payload-audit.json`，结论在同名md；本人全文阅读该md并将peer信用与本人阅读分列。

直接root storage反证支持三ID；导入文件只对UI-ST-001／005提供储存上下文，没有图鉴形态事实，不能替UI-ST-003追加源信用。五份混合载荷及Encounter读日志逐份区分应用范围，不成为三条必修的统一支持。PARTY-004旧静态肯定与R6-F后继隔离否定两份均保留，不复活撤销；UI-ST-002仍可选。没有原载荷内容推翻三条确定合同。

作者实际只读大型11节点、五份混合仅身份校验；作者明确说明局部范围。本次独立补齐当前复审的9全文，不倒补作者本人的阅读信用。旧5210b009 recovery commit本库不可用；仅可证明缓存与固定指纹及P相等，不能说本环境重新取回历史commit。九载荷没有终态旧FAIL门报告，不能据本审计消除其它历史FAIL或替代历史资格。peer报告CP-01–03保留这些边界。

## 最小补强与限制

三个非阻断证据定位应在新复审记录中更正，保留冻结作者记录：Main普通预览为766–769（作者曾列771–779）；列表行字段生成348–375、末次字段读取361（378–401只是后继刷新/排序上下文）；SaveValues储存字段登记97–102（作者曾列101–106，后段已是版本字段）。本审计实际回读这三源区间，源对象身份与固定R相等。作者已经声明Main全1–1302阅读，定位误差没有证明源单元丢失。另UI-ST-001 per-ID actual_changes列§3.3，Git差分该节原字节保持：准确措辞是§3.1新增引用并保持既有§3.3。

作者初期组合输出截断、对象未fetch、猜错路径、读取范围超实际行数及其修正均在早期证据保留；缺失UTC不能倒补。工具validation独立exit0和push exit0仅证明各自工具过程；作者静态目录仍NOT_EXECUTED。原18次Ruby尝试、无效/重复/未知exit分母及INC-R6-001没有被本次0源执行清零。本人独立Python只核有限静态字节、JSON、表行与hash，没有reference/model/host/Demo/物理输入/真实save执行。

剩余配置核验缺口为有效模型／effort／tier／speed／UUID没有回显，按用户约束不做CLI配置探测；历史recovery对象、作者原始工具transcript与不可见Mac历史也未伪补。本artifact审计没有新的字节、manifest、旧行或远端发布阻塞。候选行为验收、R6-I实际整合、共享全文与接口回归、正式接受、CLOSED各需对应实际版本独立事件，不由本报告越级消除。

机器证据主交付为`evidence-audit.json`；底层`static-object-results.json`保留所有Git读集身份、25完整远端身份、931逐行映射和44声明重建结果，`protected-span-checks.json`／`supplementary-evidence-checks.json`／`static-audit-execution.json`分别保存限定块、配置与输入、工具执行范围。所有本代理新增文件只在`reviews/R6-U11-R/peers/evidence/`；未提交或push，未改candidate/formal/public/main/Mac。
