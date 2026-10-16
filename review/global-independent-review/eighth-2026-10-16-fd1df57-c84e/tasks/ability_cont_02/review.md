# ABILITY-CONT-02 有限接口续审

本组完成 `IF-02/03/04/05/06/09` 的有限实际接收，状态为 `COMPLETE_FINITE_SUBMISSION_PARENT_RECEPTION_PENDING`。当前六接口所需可读未审、必要未接收均为0；结论仅限下述有限事实。未新增正式缺陷提案或必修裁决，不据此宣告整个特性域无缺口或全局 `NO_REQUIRED_UPDATE`。整改为 `UPDATE_NOT_STARTED`。

## 范围与身份

输入固定为 `b924c4cec2ce2eab65964d7bb4879feb456b4f87`，原合同 `40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232`。B8仍为 `fd1df570cad987dc3852a3b958f03916e317f7fe`，正式目录tree为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`；只读参考R为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree为 `7589c800b61ba13a13040ed0d686979b80a84fd0`。输入提交相对B8的正式目录及AGENTS无差异。实际checkout为 `/workspace/pokemon-essentials-clean-room` 与 `/workspace/pokemon-essentials`，没有把Mac保护审计声称为云端检查。

已全文读取根AGENTS、全局prompt、技能、原完整合同/readset、续审调度、原review及interfaces。`clean-document-revision`明确不用于审计报告；此处保留事实、来源、更正及未决边界。唯一写集为本目录，分支 `codex/r8-ability-cont-02-20261016`；未改原贡献、正式规格、参考源码、main或tag，未spawn。

请求配置按合同保留；无权威配置及本上下文opaque ID回显，实际各字段均 `UNVERIFIED`。父source_thread_id不是本上下文ID。原provider的实际reader和原根反证者不因同名`/root`被替换成本上下文。

## 实际覆盖

- [trigger-sites.json](trigger-sites.json)：参考内全部91个字面AbilityEffects触发点，逐点给完整调用单元、守卫、返回用途、默认、注册族ID和operative正文。`005_AI`有17点，`006_AI MoveEffects`另有4点，实际AI合计21；原17口径只涵盖前者。另70点包含注册文件内MIMICRY嵌套调用。搜索枚举与实际语义审读分列。
- [forward-mapping.json](forward-mapping.json)：32组人工有限接口事实，每组有准确源身份/范围、正文段落或表项、普通对照、最小反对照、失败前缀和原provider事实ID；[reverse-mapping.json](reverse-mapping.json)提供同范围反向接点。32、91都不是穷尽行为原子数。
- [provider-receptions.json](provider-receptions.json)：62个完整选定贡献对象，保留CORE、CRE、PBS、KERNEL、MOVE、AI原reader及原状态。MOVE另亲读125条完整原始TSV事实，并只接收能力所需具体覆盖；其它内容仍归原primary。大型foreign reverse矩阵未获全文或子断言接收信用。
- [companion-reception.json](companion-reception.json)：Battler强制supplement和两件companion全部必要内容已实际读取；31段逐段和固定R/B8核同字节。保留raw add、空子类、Exp−1/EV登记、野生初始图与派出图、普通与超级异色、刷新直接委派边界。没有把它扩成24以外、810子断言或完整Battler接受。
- [data-activation.json](data-activation.json)：五份能力数据全部身份可用性与213个独立注册能力名逐项接合，接收四个完整备份对象、四字段合同及具名所需完整原值记录。1122个原始数据记录的全文source-reader仍是PBS；本组不另冒领1122条原始正文亲读。

实际连续阅读范围、完整对象指针及截断修复在 [reading-ledger.json](reading-ledger.json)，79个输入身份在 [identities.json](identities.json)。相同输入身份复用；不重复全系统库存或旧报告全量审查。

## 六接口结果

| 接口 | 已接收的具体范围 | 对应事实 |
| --- | --- | --- |
| IF-02 | 普通/不可忽略有效性，普通/同步/瞌睡及后装睡冻条款，空来源降阶，HP/反馈与标志前缀，强制持物，各击及整招后段消费者 | F02–08、F16 |
| IF-03 | 真实入场与获得/气体重入标志，危害短路和逐成员退出，优先级缓存/速击，回合末决定检查，天气/默认场地重复通知，正常终局及显式中止 | F09–15 |
| IF-04 | 能力字段、显示与行为分离、默认/Gen5–8身份与启用、个体ID缓存和场上赋值边界 | F26–27、F30 |
| IF-05 | 原键/复制/未命中，直接登记与编译重复门，清表/合法前缀/保存/故障，数据表替换与旧实例、处理器表独立 | F01、F28–29 |
| IF-06 | 普通计算与具体Move覆盖、全部21个AI字面消费者、AI局部替代和真实效果差异、静默免疫不提交奖励 | F17–25 |
| IF-09 | 已写HP与场景双门、刷新非纯读边界、野生初始图/幻觉派出、两种异色getter、噩梦显示前缀 | F31–32 |

每个接口均为有限接收完成、待父任务实际接收；不自动签全域formal clauses。所有触发点连接既有 `family.identity.add/copy` 稳定ID，供CONT-01后续子ID继续引用；不把CONT-01尚未冻结的子分母填成完成。

## 发现与反证

新增正式candidate0、独立裁决required0。已使用普通/最小反对照检验：nil与false/0、普通与不可忽略门、自施/空来源、允许濒死、强制外来物、真实入场/重入、旧缓存/真实当前速度、普通/AI计算、数据登记/处理器、HP写入/反馈完成。全部为静态推导，未执行业务。

既有 `GR8-COM-008`（原 `GR8-CAR-CAND-006`）保持原CORE提案、原主审不同上下文反证及历史去重待决资格；它只针对WP41§9第4项的可选重算与入场相对次序，不新增重复根因。本组接收正确源次序，不重新裁决全部原finding。

噩梦先展示拥有者能力条，再检查目标间伤许可；拒绝时不进入内含隐藏的伤害块，目标魔法防守还可能在另一侧展示/隐藏自己的条。该可读前缀已具名保留。当前WP49给伤害资格，WP67给新展示前隐藏已有条，未作无条件成对清理保证；本组未将源观察自动升为正式必修。后续若提出具体正文不一致，由父任务安排真正不同上下文反证。

## 真实剩余与执行边界

本组没有剩余可读缺口。特性域原 `CONT-01` 的处理器子断言／全反向条款、`CONT-03` 的旧证据与历史资格，以及主审最终接收仍待各自完成；这些是任务范围边界，不冒充宿主limit，也不新增多层核验任务。未接收的其它provider主域条款仍保留原归属。

Ruby参考、独立行为模型、游戏/Demo、native/媒体、真实存档/回放均 `NOT_EXECUTED`。只执行无业务代码的文本解析、Git/身份与本增量一致性检查；没有测试/编译参考实现，没有整改或自动启动整改。

## 发布

用户已授权专属报告普通commit/push。先冻结本目录语义core，再由一次后继 [publication-binding.json](publication-binding.json) 绑定实际core commit/tree、增量文件身份和完整远端读回。发布验证不增加语义阅读或独立票数；最后绑定文件自身的真实发布身份由最终回复给出，避免未来commit自填或递归自哈希。
