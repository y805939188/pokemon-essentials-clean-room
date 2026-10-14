# R6-U08-A 作者候选交接

五项 required 的行为规格已在本批隔离镜像修订，作者静态核对完成。状态为 **READY_FOR_NON_AUTHOR_REVIEW**；未自签 CANDIDATE_PASS、INTEGRATED_PASS、正式接受或 CLOSED。父线程负责另派指定 ultra 非作者审者。

准备基点 `469a268b92daed7b4d28d7fd0da75520cbb7228f`；正式输入 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`；参考输入 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。作者分支为 `codex/remediation-sixth-r6-u08-author-20261014`。实际仓库 `/workspace/pokemon-essentials-clean-room`，原 Mac 根作等价映射，未操作 Mac。模型请求 gpt-6.1-sol / xhigh / default tier / default speed；有效模型、effort、tier、speed、平台 UUID 均 UNVERIFIED，无另启 CLI 或代理。

## 精确写集

全部路径位于 `review/remediation-sixth-20261014-prepare/candidates/R6-U08/`。

- `mirror/deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md`
- `mirror/deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`
- `evidence/` 中的逐 ID、阅读、历史回归、验证和发布记录。

没有写原 deliverables、reference、公共 ledger/task-register、audit/planning、其他作者候选；没有引擎实现、main 合并、force、删除、tag 移动或环境释放。完整载荷清单与 bytes/SHA256/blob 见 `core-manifest.json`；候选 commit/tree 由外部实际 Git 对象及发布回执绑定，不自哈希。

## 修订与验收

| 发现／原裁级 | 实际正文修订 | 新静态对照 |
| --- | --- | --- |
| R6-DX-DEBUG-001／P2 | §5.3 普通添加不预检、不检查返回值；添加正常返回后反馈请求数量，可全量／部分／零添加。假结果不排序、已写不回滚；§10 同步该容量边界 | DG-U08-01–04：空槽2→2；998请求2→1但消息2；999请求1→0但消息1；列表／数量0取消、后段消息失败、无限口袋及旧填包对照 |
| R6-DX-DEBUG-002／P2 | §4.1 两转移支后同步刷新目标图全部地图事件，再公共事件，正常清请求后返回真；后项失败只支持已有前缀。§4.3 独立请求原规则保留 | DG-U08-05–08：两个转移支、取消、后项失败及独立刷新请求。直接请求的对照观察在消息未给地图更新机会时；消息也可消费请求，未声称真实返回时必仍为真 |
| R6-DX-DEBUG-003／P2 | §3.1 F9为按住查询；消息早退、解释器／强移、新输入互斥顺序、置标记与停步后打开两阶段。已有请求另依后段暂停菜单优先序，先清标记再打开 | DG-U08-09–16：空闲、消息、解释器、强移、更早三输入、普通行走后松键停步、已有请求、暂停菜单优先、调试假与打开后段失败 |
| R6-DX-DEBUG-004／P3 | §8.1 零变化在共同门及输出前早退，既不追加也不flush、保留已有缓冲；非零双门、普通输出和显式flush原合同保留 | DG-U08-17–22：0／+1／−1、关闭标志、已有缓冲、显式flush与I/O失败；读到AI评分差量消费者，不把日志当评分执行保证 |
| R6-DX-DEBUG-005／P3 | §5.1 调用侧仍查并传性别，活动建议名不消费它；准确写首片段、严格小于上限、去尾数字、重新取完整名并首大写其余小写／截长。普通命名／设施算法保持 | DG-U08-23–28：Bert直接写、Ada同用户名性别0／1、长度等号与数字／完整名回退、空回退、拒默认、查询／处理及消息失败。命名取消按WP17各模式，不泛化BACK为旧名返回 |

完整七组实际记录见 `id-evidence.json`，固定源定位及载荷身份、原反证、合法输入前提、普通／边界／取消／失败前缀、必要消费者与接受条件均逐项具名。作者手工回源与推导是 SOURCE_STATIC／DERIVED_VECTOR；`validation.json` 是 TOOL_VALIDATION，互不冒充执行或非作者裁定。

`verify_candidate.py` 已实际运行，Python 独立 exit 0，stderr 空。它核对授权差集、受保护路径、逐 ID 七组与镜像 hash、28 行唯一编号、只替换六个 WP72／四个原目录行，并核第五所选候选的完整基线字节。其余原行保留：WP72 441 行、目录 323 行。运行的 argv/cwd/实际 UTC/runtime/stdout/stderr/exit 见 `validation-run.json`。`git diff --check` 通过。

## 阅读与历史回归

完整作者合同按结构分段实读，给定 260157 bytes／SHA256／blob 已核；内嵌合同与 `contracts/R6-U08.json` 全部 JSON 值一致。六个指定源文件共 3315 行全文、WP72正式447行、测试目录327行、原WP72规范388行及适用AGENTS全文实读；大段输出曾截断的合同001双向证据与WP72中段已单独补读。精确共享合同和新消费者阅读区间、输入身份见 `reading-and-inputs.json`。

R1 原WP72 R01–R14范围保留，R02传送关闭、R03数值取消和R13日志门与新规则接合；未修改其余正确条款。R2 保持229／21／341的精确贡献，固定历史B19字段projection完整取回与读取，角色C013、示例队伍C010及架构中性资格与当前相邻段一致。R3 23／76及历史U08未启动、M09 optional、M02 no-required保持；新F9规则与WP13消息／解释器和地图更新接合。R4 当前17／76与B5 16／75分别保留，WP17同轮数字优先及命名分模式规则未改。R5唯一所选 `13fddb0a217b36974c75657aa68da0caf104ee48` 两正式文件与main基线全字节相同；92 CLOSED原精确资格未重开，R5-U07、B17/B19/B20、其它目录原行与120效果表保留。原FAIL／MISMATCH／LF更正历史没有重写。详见 `historical-regression.json`；这是新改动的有限回归核对，不继承旧PASS或授整域终裁。

只读 R 的六载荷通过固定 raw commit 取得并核 bytes/SHA256/blob；随后从原参考仓库正常fetch至 `/tmp/r6-u08-reference-objects` 的bare对象库，核固定commit/tree及九个所用源路径的mode/blob；本环境没有参考检出或执行。最初从主仓库取R ref失败、附加GitHub API tree查询代理403、证据生成脚本首次语法错误都保留于执行记录；其后准备提交单独fetch、源载荷取回、脚本纠正与最终验证成功，没有重建任务或洗掉失败。

## 接收与未完成层

唯一实际整合接收者为 `thread01a13a93-d1da-71e4-a488-63b8524f503d`。WP72与U09共享；目录与U06/U07/U09共享。整合者须按本批精确改动段串行接收，并收齐其他候选；本作者不以整文件覆盖正式稿。

作者事实修订没有剩余实质阻塞。独立candidate审查、唯一写者实际整合、共享全文和接口／历史回归非作者复验、正式接受及CLOSED登记均待父线程与接收者处理。完整宿主、Demo、参考定义、独立完整行为模型、物理输入、真实保存和真实用户名读取均未执行；模型与配置有效回显未知。历史L01–L14及INC-R6-001的原边界保持，不因此放弃可定静态修订，也不转成新的行为必修或已运行结论。
