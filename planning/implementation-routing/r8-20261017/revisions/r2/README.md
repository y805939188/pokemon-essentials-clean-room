# R2精准返修候选

固定输入是R1候选`5666b7b912e2fb79b5119283ee6a37401a7071db`；独立失败报告为`8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8`。本轮按用户要求精准处理剩余12项（2 P2、10 P3），不以作者处置替代独立裁定。状态为`R2_AUTHOR_REVISED_AWAITING_PARENT_ULTRA_DEFAULT_REVIEW`。

## 数据修正

- FR-000067保留普通能力反应，L106的逃跑决定、业主替补等待与世界终局交接拆为新FR-000769；父source保留，当前有效范围与locator精确排除子范围。
- FR-000261限定当前战斗四层120项效果编辑，明确框架/Showdown/MZ责任，移除原个体持久写入接收者147/148。
- 六个AI行明确共享准备状态写入、具名正常清理及异常残留的候选责任。共享状态合同见[逐字段说明](shared-ai-preparation.json)；没有宣称查询纯函数或统一回滚。
- FR-000086为历史责任索引，完整d62原行加retirement归档为META-000033，连接现行换人/评分/数据绑定消费者。原ID不重用。
- 七项Demo/作者元数据与三项内核元数据按源表行重新绑定真实消费者；元数据、退役replacement和章节导航同步。WP03完整字段责任表逐组保留依据。
- 补B17/B20、未知效果回退、内核具名跨域目录的漏接消费者；清除16节宝可梦目录中Fishing/Slot/Mining同WP号误连。
- 七个生物依赖行及FR-000420/436按实际音频、伙伴、治疗、PP、战斗用物、Mega计数和失败层用途修正。
- 父任务修复可读父行到excluded_child_refs子ID的显式导航，作者没有承担独立review。

## 证据入口

[12项问题映射](finding-resolution.json)、[721旧ID及全部非PASS逐项处置](feature-resolution.json)、[35个旧PASS组及同根因保全](retained-pass-propagation.json)、[显式修改决策](explicit-decisions.json)、[源表消费关系](consumer-mappings.json)、[数据差分](data-diff.json)、[源章定向阅读](source-reading-scope.json)、[73份固定复审输入台账](tools/review-input-ledger.json)、[实际工具I/O](tools/actual-command-io.json)、[首次结构失败证据](tools/first-freeze-command-io.json)、[VIEW作者修复](tools/root-tool-resolution.json)。

11项数据修正由[显式脚本](revise-data.py)从固定R1原字节输入产生；它遇到当前文件不同会拒绝覆盖，不是去向重建器。R1旧迁移脚本不得重跑。证据脚本只从固定输入生成处置台账，不运行来源/业务/原型。

当前已应用908快照有736个活跃行、33个完整退役旧行与33个元数据。相对最初721功能ID累计新增48个，其中47个R1新增行原样保留，新769待独立复核；R1通过的693个旧ID整行、22个元数据整行也保持不变。文档与标题分母仍由实际索引/Git树求得，当前观察为131/2683，不硬编码为永恒要求。

最终静态工具7命令全部exit0且输入hash稳定：27项结构负例、9项自检、2项导航负例通过，11份生成文件一致，12项保全通过。导航检查实际覆盖36个显式父行、39个子行、39条边；旧报告29个父行只是缺失整个子ID的受影响子集。735个存续活跃分类、全部旧source和32个旧退役历史body保全；10项retirement导航按所需修正单列。该结果是作者工具核验，不是独立语义验收。

本候选当前实际应用仍为`908273093e1f6b27fc58249417675dd62d146224`及U02/U03两个事件；191个原批次绑定行中17个已回填、174个待核对，是当前已应用快照的口径。另已收到并核对累计8批回执，33个实际目标身份匹配，真实写集比原计划增加6份正式文档。后继actual `0eee6d141f33758eda34bd8ebad94a3e2b617f5a`的736个locator仅已准备，**未应用8批切换**：6个纯U04变更文件无ACCEPTED，UI65还有U01/U04共享接收边界。历史2683标题已覆盖；0eee实际观察2704标题，新增11个已接受源标题有显式现有消费者建议，另外10个U04标题仅PENDING建议，不能把2704称当前已应用覆盖。完整源切换被真实门拒绝，待正式U04回执及最后源差分复核后再执行。

来源接收与后继准备：[8批回执身份接收](tools/accepted-receipt-intake.json)、[736定位准备](tools/prepared-source-backfill.json)、[早期缺U04拒绝历史](tools/missing-u04-backfill-rejection.json)、[作者完整源差分/11标题接收](accepted-source-reading.json)、[10个U04待接受关联建议](accepted-u04-proposed-mappings.json)。这是准备证据，不是8批回填完成或新的独立验收。

## 边界和待办

历史来源B8/R8正式子树仍为`f292698cdd4a8e725525a9be6dc34b75faaf151e`，当前接受payload为`908273093e1f6b27fc58249417675dd62d146224`、正式树`6ae817df5b11eafdec671214b0d04e542ad364bc`，分别通过固定Git对象读取。U02/U03两个接受事件和17个相关行的回填保留，191个批次绑定活跃行中174个仍待核对。全部上游CLOSED未获确认。

全部去向验证仍待验证，阶段待定/未批准、实现未完成/未验收；四类协作原型未执行。原型未运行、上游174待绑、范围门未决是独立待办，不能被工具通过消除，也不将这些已诚实登记的待办冒充本轮修复失败。XP工程/特殊玩法/工具与首版范围仍需用户决定，未擅自排除。

父任务须以新固定SHA另建`gpt-6.1-sol ultra/default`独立复核，入口见[复审合同](review-prompt.md)。本作者仍为请求的xhigh角色；创建请求与有效执行echo分开，无权威echo的字段继续`UNVERIFIED`。本次没有执行Ruby、参考游戏、业务向量、MZ宿主、Showdown原型或框架实现，没有改正式正文或抢写整改分支。

R2语义保全的精确输入绑定见[pre-calibration-binding.json](pre-calibration-binding.json)：693旧PASS/47新增/22元数据整行相等是该f7e6…作者快照事实；后继接受可更新current_applicability与源差异，须另列来源回填证据，不因此把未来计划/历史source当重改。新完整源覆盖入口仍待可绑定输入执行，现有prepare/拒绝证据不替代该后继检查。

最终阶段工具记录为`r2-fixed-source`：当前908上的7命令全部exit0，13个登记输入hash全程稳定；27结构负例、9自检、2导航负例、11生成物一致、12保全检查通过。后继source prepare成功、apply被6个未接受源guard拒绝且核心三文件hash未变；5个接受扩展fixture与完整current全量检查明确`NOT_EXECUTED_AWAITING_U04`。这些后继未运行项不包含在当前阶段通过数中，最新工具SHA下prepare成功和apply拒绝的完整argv/stdout/stderr/exit及核心hash保全见[最新来源准备记录](tools/accepted-preparation-command-io.json)；早先missing-u04记录仅为保留历史。
