# R6-U06-A 作者候选交付

本批仅修订 R6-B-001、R6-B-002、R6-DX-E001、R6-DX-E002。作者状态为 **AUTHOR_COMPLETE_AWAITING_NON_AUTHOR_REVIEW**；没有独立 CANDIDATE_PASS、正式接受或 CLOSED。

准备提交 `469a268b92daed7b4d28d7fd0da75520cbb7228f`；正式基线 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，其 tree 已核为 `7589c800b61ba13a13040ed0d686979b80a84fd0`。作者分支 `codex/remediation-sixth-r6-u06-author-20261014` 从准备提交创建，初始没有已有任务成果。

实际云端根为 `/workspace/pokemon-essentials-clean-room`。原 Mac 项目根等价映射到此根；R 在 `/tmp/r6-u06-reference.git` 中按固定 blob 只读，无检出树。用户指定唯一整合者为 thread `01a13a93-d1da-71e4-a488-63b8524f503d`，覆盖历史准备入口中的整合者登记。此作者不直接写 formal、公共 ledger/task-register、其它作者目录或历史输入。

请求模型为 gpt-6.1-sol / xhigh / default tier / default speed；实际 model、effort、tier、speed、平台任务 UUID 均 **UNVERIFIED**。直接由本云端任务完成，没有启动 CLI、额外代理或配置追查，也未自签独立审查。

## 修订与必要消费者

| ID／原裁决 | 实际候选规则 | 源与消费者接合 | 验收与保留范围 |
| --- | --- | --- | --- |
| R6-B-001／required P3 | WP75 §10、§15.1 和 CV-M24 分开图块集访问异常与无效图块诊断 | 两个图块集表访问救援只构造图块集编号、地图编号；非空图块通行条目无结果才构造地图、坐标、一基层号。活动柜台、调试图块修复、外层编译处理已新读；通道唯一调用停用。 | ID7/地图5且有效(2,3)的缺对象／优先级属性访问异常、顶层无条目层3、合法查询与正常返回nil分别判定。nil不保证同一描述；地图载入跳过、已写前图不回滚、保存容错和宿主未知保持。 |
| R6-B-002／required P2 | WP75 §8.3 与 CV-M11 明确免费提示→接收，收费扣款→提示→接收 | 构建器尾追加→同轮单行提示不重排→解释器同步消息→金钱写入→脚本到达时求值→接收自身消息／入包。接收内部引用既有 WP27 §7，消息等待引用 WP17 §7.1。 | 有效单页、已注册POTION、无外部改写：免费首次提示1000/0，价格200收费首次提示800/0；正常接收后数量1。金额不足、容量拒绝不扣/不接收。提示失败只说明收费已扣且尚未接收；生成段无退款或事务取消，不推全局补偿。ASCII/大小写/非负价/首行等原门保留。 |
| R6-DX-E001／required P2 | WP73-A §4.4 实际数据池绑定表，§3.3/3.5 接合；CE-M15/M19 消费者限定及 CE-TYPES-01–06 | Types一般池不重复、不自动排序，通用目录含已注册伪类型；专门单引用选择器仍排伪，双槽自身合同保留。父工作槽→校验去重去空→登记／档案／基础PBS完整序列→WP19完整副本与成员判断。TutorMoves等既有物种池参数同步具名。 | 三不同类型和P的合法作者输入、重复/取消、Apply No／父No／Cancel、原共享入口去重、登记后或档案后失败各分开。进化空表、原PBS投影、旧名称/BP缺陷与其它字段结果不变；不设计三类型战斗或未来UI/API。 |
| R6-DX-E002／required P3 | 仅 WE-M20 独立行补基础记录保留、非零等值省节主语 | 非零记录后缀先选择路径→遍历所有同后缀记录→仅非零五组等值省节。档案重载、PBS编译与缺失形态查询分开。 | 仅基础无路径；同后缀差异两节；同后缀等值基础一节；不同后缀仅非零路径。WP73-B §7.5 与 B19-C016 正确详细矩阵原字节保留；No重载、Yes档案后PBS、失败前缀与已有布局不广播规则保持。 |

每个 ID 的前提、普通对照、最小反例、失败／取消／部分提交、双向载荷身份、必要消费者、最小修订、历史回归、反证处理、接收依赖与 pending 独立门完整展开于 [author-findings.json](author-findings.json)。全部 22 个新具名案例是 **DERIVED_VECTOR／NOT_EXECUTED**。

## 阅读与历史资格

适用根 `AGENTS.md` 已全文读。指定224391字节作者入口的 bytes/SHA256/Git blob 一致，按结构连续范围完整读3671行；其中 contracts/R6-U06.json 的111186字节全文以原字节嵌入，全部字段完整语义读取，不以摘要或hash替代。WP73-A 210行、WP75 438行、测试目录327行和必要WP73-B 217行均全文新读。MapsAndEvents全部1751行无缺口，其它源上下文和必要消费者按完整相关单元新读。详见 [reading-summary.json](reading-summary.json)、[reading-scopes.jsonl](reading-scopes.jsonl) 和 [input-identities.json](input-identities.json)。初期读取／fetch未单独捕获UTC的字段保持NOT_CAPTURED；后继记录不倒补。

相关原提案七组在完整合同中读取，B独立反证两项、animation/editor两项及debug/Compiler针对B的完整记录新读。14个具名反证载荷的全字节身份已核；其中全局机械覆盖、其它领域或55 shader记录的索引核验不冒称本作者语义全文或PASS。

历史回归按实际受影响区间和接口，未全扫历史。R4/B5固定输入的三路径、R5原R5-U07语义字段及所选关闭／唯一activation对象已恢复身份，并核对应静态条件。R1仅原WP范围；R2 229／21／341；R3 23／76及M09 optional、U08历史未启动、M02 NO_REQUIRED；R4当前17／76与B5 16／75；R5唯一92 CLOSED／OPEN0各限定保持。历史旧FAIL、advisory MISMATCH与SC-U07-001错误捕获体LF及其纠正保留，不能从旧字段重开或扩大资格。原任务包错误跨LF表述作为历史输入保留，当前WP75／U07-C02正确无LF捕获体不变。见 [historical-regression.json](historical-regression.json)。旧PASS没有替代本批新验收。

## 实际验证与交接

[validation.json](validation.json) 的30项 **TOOL_VALIDATION** 通过：固定身份、镜像起始字节、正式文件未变、精确允许的替换／插入区间、旧测试ID/顺序/重复次数、所有其它旧表行、B17/B19/B20/U07原字节保留、新增链接/标题、写集隔离、完整读取范围。`git diff --check` exit0。首次验证把新表头计入旧ID而失败，保留 `commands/candidate-validation-01.*`；修正表头计数后第二次exit0，保留独立UTC/stdout/stderr/exit。初始向项目origin请求R失败亦保留，随后从正确Maruno17仓库取得固定R并核tree。

规格差集为三份mirror，39新增／10替换；证据、工具和日志只在本批evidence。Python仅做固定blob读取、身份/文档检查和发布核验；没有执行R定义、编辑器、转换器、行为向量、完整独立模型、原生宿主、Demo、真实存档或生产服务。上述新增执行分母均0。

没有未解决的本批语义修订项。L01完整地图/工程、L02媒体、L03宿主、L10序列化执行、L11任意扩展组合、L14有效元数据等原限制保持，未提升optional/policy为必修。下一步由父线程派非作者ultra审者审确定候选版本；通过后由唯一整合者接收，WP75须收齐U09、共享测试目录须收齐U07/U08/U09，再对实际整合全文、接口及历史回归独立复验。作者完成不等于上述门已通过。

候选语义core、发布commit/tree及远端逐载荷全字节回读由有限发布回执与最终响应外部绑定；manifest不递归自哈希。正常提交／推送，不force、不改main/tag、不merge main、不删除、不释放环境。
