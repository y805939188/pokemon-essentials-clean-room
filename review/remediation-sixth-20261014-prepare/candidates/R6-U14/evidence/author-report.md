# R6-U14 作者候选交接

六项实际修订均已写入本批14份候选镜像。状态为 **REVISED_PENDING_NONAUTHOR_REVIEW**；作者未签 CANDIDATE_PASS、正式接受或 CLOSED。唯一正式接收者为 R6-I。发布对象由后继 publication-readback 绑定，不在本文件预填未生成SHA。

固定准备提交 `469a268b92daed7b4d28d7fd0da75520cbb7228f`；分支 `codex/remediation-sixth-r6-u14-author-20261014`。正式输入 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。仓库在 `/workspace/pokemon-essentials-clean-room`，只写本批 mirror/evidence；未操作Mac、正式文件、公共台账或其它批目录。

## 逐ID结果

| ID | 实际候选规则及正常/边界对照 | 静态目录行 |
| --- | --- | --- |
| R6-D-LZ-001 | 源拼写双反斜线+n、收集键反斜线+LF、运行键反斜线+n分开；仅收集键→Q时运行缺译回原输入，后继窗口换行不证明命中。普通运行键→Q对照及先库存写入/导出取消/导入截断分别保留。 | LZ36–38 |
| R6-D-LZ-002 | 当前语言可选择指定图像身份，缺译请求A、非空A→B请求B；七个控制键图、图形战斗菜单、训练家卡和翻牌基名分列。背景/说明标签独立，资源入口各自处理空身份与失败，无通用重试A保证。 | LZ39–41 |
| R6-D-PBS-C05 | 补Type和Move有限省略默认；Item单数Review不派生复数，省NamePlural为Unnamed，显式Reviews保留。原始名称与本地化输出、份名回退、价格/用途/消耗、类别×威力门均保留。 | R6-U14-C05-01–05 |
| R6-D-PBS-C06 | 五项指标缺字段默认表；已有部分形态记录采用自身默认，缺整条才克隆。基础背面5,6下，部分/整条缺席/显式7,8分别0,0/5,6/7,8；保存路径、来源后缀与已有布局刷新边界保留。 | R6-U14-C06-01–03 |
| R6-D-PBS-C07 | 限定无条件0–255断言：合法作者基础Happiness256可登记并在成功创建返回后保留256；255/省略70/0对照。正常变化末端夹限保持，不把末档无限外推。 | R6-U14-CI01–04、GR01–05 |
| R6-D-DATA-C01 | Flags省略空列表、显式空含一个缺值元素、Other文本三例分开；显式空登记后普通标志查询失败。两成员蛋步条件投影先2→1后查询失败，未到额外减步/夹0/孵化；外层恢复未知。 | R6-U14-FLAGS-01–04 |

全部27行都是 **DERIVED_VECTOR / NOT_EXECUTED_THIS_UPDATE**。CI/GR包含四组重叠创建观察，27不是独立玩法执行数。七组逐ID合同、原裁决/反证绑定、原前提、实际文件SHA与每行位置见 [per-id-author-handoff.json](per-id-author-handoff.json)。精确14条镜像路径、bytes、SHA256、git blob与基线身份见 [candidate-manifest.json](candidate-manifest.json)。

## 新读取与证据

适用根AGENTS全文已读；固定prompt350085字节、SHA256 `9e6b3d0b26724332cb0b87b45d68f9ee4b408e99e79690b8482be24a4f05c4f3`、blob `6a474a14d2ff2fb025cea63e8e5304426b992dd4`匹配。prompt按连续12段读完；234757字节合同原件与全文内嵌合同字节相同。原六完整proposal与独立counter全文、三个原领域报告、换行诊断和48行图像矩阵已读；当前六规范记录与合同逐条身份一致。

17份指定Ruby文本与SCRIPT_TEXTS全部6614行、14份正式基线全文均由作者新读。补读四份资源帮助文件全文；消息处理与孵化回调只读必要完整局部分支，范围不扩成两文件全体。源对象只取固定Git blob，没有reference工作树改动或求值。输入hash/bytes/mode及真实连续范围见 [input-snapshot.json](input-snapshot.json)、[reading-receipts.jsonl](reading-receipts.jsonl)、[packet-validation.json](packet-validation.json)。

二进制messages_core全字节身份已核；新工具只做具名键原始字节成员检查，没有Marshal解码或加载。收集键在798247和798325，运行键及裸LF对照无匹配，与原counter一致，见 [newline-byte-validation.json](newline-byte-validation.json)。这不证明语言安装、原生loader或真实运行查找通过，也不继承原D作者10697单元审查为本作者全语料语义验收。

## 验收和回归的实际层级

文档工具独立退出0：29次精确编辑、8次前提澄清，全部14镜像可从固定准备文本重放到精确最终字节；新5处本地链接及锚可解析；4目录910条原表格行逐行字节保持。910包含结构行，不是910条新的行为签名。git diff --check通过，检查时正式/audit/planning/specs/reference无跟踪差异。工具结果见 [author-tool-validation.json](author-tool-validation.json)，每个已捕获命令argv/cwd/真实UTC/stdout/stderr/退出见 [tool-attempts.jsonl](tool-attempts.jsonl)。工具检查不替代非作者语义审查。

历史按本批精确接点取回：R2九控制具名资格与A006的B01/B02局部贡献；R3三项与R4两项本地化/解析原前提和准则；R5十三项原准则与正常/反例/失败/排除域。原指针和载荷身份见 [historical-qualified-spans.json](historical-qualified-spans.json)、[historical-case-premises.json](historical-case-premises.json)。同源现文已全文对照，旧目录行保持，新默认/指标/初值/空Flags不替换原输入与结果。R5所选候选的14份正式字节与本次正式输入相同；唯一activation92条选定状态及scope原hash全部匹配，这项是身份工具检查，未重新全仓审查。

R1只按原WP资格；R2保留229/21/341，R3保留23/76、M09 optional/U08历史未启动/M02 NO_REQUIRED；R4当前17/76与B5 16/75分开；R5唯一92CLOSED/0OPEN、51P2/41P3和exact owner scope保留。旧G03/G09 FAIL、U03旧FAIL与定向修复、两advisory MISMATCH、SC-U07-001错误捕获体LF及纠正不回写。410native/568schema/158额外、21shared/18deps/85solewriter、262原贡献/6行政transfer/3纠正不混计。本批不修改optional、policy或limits。

本作者新增参考函数执行、独立玩法模型、宿主、Demo、真实save及媒体执行均 **0**。原R6的18次Ruby尝试和R4/R5各4隔离记录属于原审查分母，不转入本次；未运行不作为事实修订的虚构前置门。有效model/effort/tier/speed和任务UUID未回显，记UNVERIFIED；按用户指令未启动CLI或额外代理证明配置。

## 后继门与元资料限制

作者完成范围内没有未修订ID。非作者候选审查待父线程指定审者；实际接收、共享全文/跨域接口/历史精确回归复验、正式接受和CLOSED均未发生。U01/U09/U10/U12共享接点与管理员同步请求见 [integration-request.json](integration-request.json)；原audit/source-traceability、planning及公共记录只能由R6-I接受后办理。

早期部分命令只保留平台输出，未另存实际UTC/独立stdout/stderr；本次不补造。一次过大合同显示和一次队伍目录显示截断不计为完整读取，已分别通过连续内嵌原合同和原缺段补读完成。输入工具首次因formal索引没有type键失败，原失败保留，修正后33身份验证通过。一次patch定位遗漏字符串前缀未写入镜像，随后修正；两次错误handoff文件名只读失败后已按真实路径取回。没有把工具失败误判为源行为失败或删除原失败记录。
