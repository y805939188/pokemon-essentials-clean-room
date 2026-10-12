# R4-U01 新独立候选审查

裁决：**CANDIDATE_PASS_SCOPED**。五项均 PASS；18 条必需静态验收条件满足，5 条可选执行边界已审。没有需要作者修改的问题。本签名仅绑定下列真实候选，不构成实际整合 PASS、ACCEPTED_SCOPED、CLOSED 或全域接受。

## 身份与输入

- 独立 reviewer：任务 `/root`，真实 thread `01a130d6-8ef2-73c8-8b1a-b14f8bc1d029`（从本任务环境 CODEX_THREAD_ID 读取）。来源父 thread `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`；作者 thread `01a130c3-c02a-75a8-939d-36db3954a00c`，彼此区分。
- 固定合同：`08a57fb55118914a74ac1ffaf617647c01df8938` / tree `8fc388710e3433890416f6d01247fd09df9d2ea8`。已读本批 reviewer、batch-contract、read-scope、完整 findings/精确化及验收，核冻结发布后继 `2b60c7bd0dce8d972e34a9d86a8f6cf6a3b1dd65` 的起点绑定。
- **候选**：`db879d9034acf2fa3a3721ad3b94614827922ec4` / tree `f47c43195a60b8edb2922f40d38582874a675cc5`。
- 作者证据后继：`c1e5c8a780426aef1611a5b139375de15e6cd468`；相对候选仅增加 author/candidate-publication.json，正式字节完全相同。
- B：`1f36475d22120a0d1175967d5b17d71fe8311d88` / tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`。
- R：Maruno17/pokemon-essentials `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；新专用 bare 仓库取固定对象，仅读取，未修改参考内容。
- 审查分支：`review/r4-u01-independent-20261012-codex`。只新增本批 review/candidate-v1 下自身报告证据；原工作树仍为 B 且干净。
- 请求 gpt-6.1-sol / ultra / default / Fast=false；两个语义子任务的模型/推理请求获工具接纳。根及子任务的实际模型、tier、Fast 回显均为 **UNVERIFIED**，不进行后端、额度或凭据审计。真实子任务为 `/root/localization`、`/root/utilities`，另有只读 `/root/localization/map_boundary` 边界反查。

## 逐项裁决

| Finding | 裁决 | 实际核查及候选位置 |
| --- | --- | --- |
| GR4-M01-001 | PASS | WP08 §6.3.2、LZ26–30准确给同规范键后值、重复同域节逐项覆盖与早节独有项/稀疏索引保留；同域编译与运行game/core优先分开；混合形态失败不泛化，Map形态门与完整入口先截断仍保留。 |
| GR4-M01-002 | PASS | WP08 §5.3/§8、LZ31–35准确给Q、U+005C/U+0026和U+005C/U+0031的返回；地图普通路径同义、格式化字符串保留参数；观察发生在消息窗口前，与U+0001和WP17暂停转换分开。 |
| GR4-M02-001 | PASS | WP06 §3.4、TM15–19准确给1099/1100清0、1101保留、提前再迟查均false；一般天数D公式、默认/负持续量和具体负数正确；与事件私有冷却/命令124分开，并保留刷新不回写槽前提及WP09持久化依赖。 |
| GR4-M02-002 | PASS | WP07 §4.2/§6/§7、IO16–20准确分请求前构造、基础宿主局部捕获、便利全调用捕获；三类输入与替身0/1次、长度8正确；空串不证明发送，HTTPS提前门和GET原合同保留，精确异常仅归历史Ruby2.6隔离输入。 |
| GR4-M02-003 | PASS | WP06 §5.4、TM20–23准确给跨次状态、1/7重复门、未中选未见、耗尽后下次重开和n=1；用条件概率与无放回0/独立均匀1/2对照，没有每n次覆盖、默认系统采用或统计执行承诺。 |

完整逐criterion理由、原前提/未知限制及每项独立质疑见 [findings.json](findings.json)。源静态阅读、callers/条件备用定义与消费者反查见 [read-ledger.json](read-ledger.json)、[localization-notes.json](localization-notes.json)、[utilities-notes.json](utilities-notes.json)。

## 独立质疑与反向案例

这次审查实际读固定R、四个候选正式文件和整批差异，没有以hash或旧PASS替代行为核验。每项至少一次有结果的质疑：

1. 导入归并：把运行层优先级、整节替换和全部混合失败作为替代解释。实际写入只覆盖后节提供条目；历史反向哈希→数组成功，数组→非数字哈希失败，候选正确限定同形态成功及早节状态保留。
2. 占位参数：反查WP17层和条件备用入口，并静态检查参数1引入后续{2}时能再被参数2替换、同次不递归处理重新引入的{1}。候选“按参数次序”与主源一致；更多转义组合仍未证，未制造范围外补测要求。
3. 变量计时：反查“标准午夜截止”“false保留等待”“事件私有冷却”等解释。实际持续量D、false清槽路径与严格大于门共同排除这些解释；独立查询与连续查询、刷新替身与事件页执行清楚区分。
4. POST：反查假宿主导致前置失败、所有POST均失败或空串证明发送的解释。安全符号键及空表的静态路径能到达宿主；构造位于宿主局部捕获之前；候选没有把有界失败外推默认游戏或真实联网。
5. 有状态选择：0,0单序列不能区别独立均匀，条件分布才可；耗尽后先清旧状态，首抽不经过重复门。候选把数学对照和执行证据分开。

对全131正式文件作本批概念反证检索；本批外实质命中是PBS/遭遇重复节、宫殿权重、漫游状态、镜头/界面编号等其它入口，不能代替或推翻这五个有界合同。读取必要WP04、WP09、WP13、WP17、WP59、WP64消费者，没有新增跨批正文。

## 旧范围与完整性

- 独立核对全部候选changed-path：四个批准正式文件及七个作者证据文件；后继仅一个发布证据文件。B→合同起点无正式漂移；其它127正式文件与B完整字节相同。
- 作者四正式文件的bytes/SHA-256/git blob、整份formal-diff.patch、源与B锚点身份均独立复核。旧121测试行、旧27章节逐字保留；新增恰为24向量TM15–23、IO16–20、LZ26–35。JSON、相对链接、UTF-8/LF及正式差异检查满足。
- GR3-M01-001/002：当前源、WP08导入行过滤/形态/截断及稀疏导出边界作受影响静态回归，LZ01–25保留。GR3-M01-003/004的PBS井号、电话默认覆盖是不同入口；相邻WP04区别及未改字节保持原qualified事实。
- GR3-M02-001/002：原通知部分状态/诊断条款与持久注册身份、EP/SV旧行保持；新计时与POST不赋予事务恢复或改写保存注册规则。GR3-M02-003仍NO_REQUIRED_REVISION/NOT_REOPENED；GR3-M09-001仍DEFERRED、U08未启动。
- 原229中的GIR-FD82-A013及精确341中的B02/GIR-FD82-A013：读取固定manifest两处qualified_scope、验证完整文件与规范JSON对象hash，只复用非零数字前缀/数字0/常量/Map顺序、内容形态与先截断的原限定范围。精确元组保留：candidate `46cd726c35e9d754a8e42b32986313ce3d4d1782`，actual `1b1e169faf273e89ad6b7f5e46fd7b60d87d3946`，independent_report `361e4e69126559c266a08fdf093082dbbcd83f8d`。本批合法24号头后的归并不是旧项重开；旧签名未转移给新字节/全ID/其它owner。
- WP35/EG-13/20、WP34正确3/5继承及同Power一次计数、其它GR3/229/341、正式/公共账、main、交付标签和用户数据均未修改。其它历史为historical_qualified_evidence_reused/not_reexecuted，没有补签全局。

详细可复核记录见 [validation-result.json](validation-result.json) 与 [validate-inputs.py](validate-inputs.py)。整候选diff --check会把保存的patch中必须存在的单空格空白上下文行报告为尾随空格；四正式文件检查无问题，且patch完整字节等于真实diff。这不是行为或交付缺陷，不要求整理型返工。

## 执行证据与限制

第四review的历史EXECUTED_REFERENCE仍是**4条执行记录**，不是四个用例。本批只复用M01一次、M02两次的原函数隔离回执；M03一次不在本批。历史脚本及两版M02结果均只读，不重跑，第一次字符串键安全对照的FrozenError没有被隐藏。AntiRandom没有历史执行。本次新参考/模型/宿主/完整Demo行为执行均**0，NOT_EXECUTED_THIS_UPDATE**；文档检查属于TOOL_VALIDATION。

精确Ruby2.6异常只归原输入、版本及替身观测；地图反斜线1/地图格式化、便利安全字符串键、HTTPS符号键和默认/负天数等新增对照仍为SOURCE_STATIC/DERIVED_VECTOR。没有真实HTTP、文件目标POST、真实存档、事件页刷新、UI/像素/动画、完整导入/导出或随机统计通过。随附Ruby3.1宿主及实际模型设置回显UNVERIFIED。缺资源/宿主不阻塞这次必需事实静态修订；未来兼容异常的政策未代选。

没有候选必需验收阻塞。actual整合输入尚未提供，未进行actual审查；唯一登记员按合同整合并冻结后须另做限定实际审查。本报告未登记任何接受/关闭。

## 发布证据

本报告提交及后继发布回执只在上述独立分支。推送后由 [remote-readback.py](remote-readback.py) 在全新无alternates对象库fresh fetch，读完整报告、真实候选11文件和作者后继1文件，逐字节比对并核commit/tree及main/交付标签。首份报告绑定见后继 [publication-readback.json](publication-readback.json)；含回执的最终提交再次fresh fetch完整读回，最终commit/tree由外部答复提供，避免递归自嵌。
