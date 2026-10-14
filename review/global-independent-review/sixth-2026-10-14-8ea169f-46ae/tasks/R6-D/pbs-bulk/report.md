# R6-D / PBS bulk：作者字段与消费接线审查

本次续审已按主审澄清的范围完成：**104 个实际家族×字段的独立规则阅读、116 个含省略字段的规则、9 类节身份规则，以及16,732条记录的全字段有前提映射**。必要字段规则、消费者、正式条款与所用向量的真实连续区间缺读为0。状态为 `REVIEW_COMPLETE_WITH_PROPOSALS_FOR_PARENT`，**没有生成PASS，也没有替代主审终裁**。最初BLOCKED属于未完成工作及过宽的下游算法义务，已经继续消除本域字段/合同缺读。

人工规则结论与结构证据分开保存：先独立阅读schema、缺省/继承/覆盖、校验、反写和必要消费者，再把每条记录每个字段联到这些规则。全量字节/逐原子检查与规则应用由审查脚本完成；**没有声称模型逐字人工读过206,649行，或执行过每条记录的游戏效果**。招式/特性/物品/AI内部算法属于具名跨域交接，不能重复变成每个PBS记录的未完成义务。

## 固定输入与保护

| 输入 | 独立核对值 |
| --- | --- |
| main HEAD / tree | `8ea169fbd0f33f378b5d732fd6bea59e854e04a6` / `6ab3429170d2762607fbc2237014c3a160449fa1` |
| 正式规格 tree | `1046fbb657882e84b3dfc6d017943a9edf7782e5` |
| reference HEAD / tree | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 仅写入 | 本 `pbs-bulk/` 目录 |

44个文件共206,649行、29个不同字节内容、16,732节。逐文件完整读字节并核对Git blob和SHA-256；当前八类数据分别与Gen8备份完全相同，五套metrics也完全相同。保留所有路径，不导入历史PASS；字节相同只支持材料身份，语义规则仍在本轮独立阅读。`protected-input-check.json`证明reference和正式/specs/planning/audit跟踪文件未改变。

## 规则与逐记录覆盖

| 检查 | 本轮结果与限定 |
| --- | --- |
| 人工字段规则 | 104个实际字段全部有规则；含12个未出现但省略影响实际记录的字段，共116条；另有9类节身份规则 |
| 必要阅读核验 | `field-rule-reading-gaps.json`为空；逐规则检查schema、构造、转换、必要消费者、正式条款、引用向量与导出范围均有模型可见连续区间记录 |
| 每记录全字段映射 | 16,732条，281,930个字段应用：173,014个有属性、79,337个记录缺省、29,519个继承有效基础值、60个因另一个野生持物档显式给定而取空池 |
| 普通引用原子 | 382,294个条件化联接，未解析0；不会由此推出完整编译、时序或备份支持 |
| 分阶段引用 | 基础物种进化目标/后代在形态登记前可用性另查，异常0 |
| 嵌入旗标 | 2,330个Fling数值、332个NaturalGift类型/数值、17个DefaultForm数值；NaturalGift类型未解析0，均标明运行编码而非编译枚举 |
| DefaultForm边界 | 6个当前/Gen8物种共12个路径位置没有同号形态数据；它们是运行选择器，后续可回基础记录，不能报为解析失败。OBSTAGOON/PERRSERKER/CURSOLA/SIRFETCHD/MRRIME/RUNERIGUS逐处保存在嵌入旗标材料 |
| 字面形状 | 141,555项形状检查异常0；审查器不冒充编译分词器或任意未来输入的运行结果 |
| 招式接线 | 每条招式关联真实效果定义位置或通用fallback及正式同名条款；唯一缺匹配实现名是可选SHADOWSHED的RemoveAllScreens，现有正式合同已保留其失败分支 |
| Shadow表 | 131个量表/有序招式、18个效果身份、4个道具用途/价格/无旗标，153行与正式表相符；不代表可选内容已启用 |

字段规则明确区分：Type防守端相克与冲突优先；属性/特性候选不擅设两项硬上限；Species形态缺省继承、Moves/Evolution空表继承、三档野生持物的整组门；EV产出与训练EV分层；尺寸十分之一单位；进化分组顺序/参数/反向关系；原始EggMoves与祖先回溯查询的不同消费者；Item机器类型与Move字段的不同职责；价格无文本资源上限；有效消费与数量显示；BerryPlant符号身份与运行Item关联；Metrics显式记录缺字段和整条缺席惰性克隆的区别；Shadow可选缺席、基础回退与有序招式输入。每条都列明前提及跨域交接。

## 送主审反证/裁决的提案

`findings.json`保留全部8项，均为 `PENDING_PARENT_REBUTTAL_OR_ADJUDICATION`，没有提出者自判终结。

| 提案 | 内容 | 提出者意见/边界 |
| --- | --- | --- |
| C01 | SHADOWSHED无匹配效果 | 已有WP23/WP43及FB05明确合同，建议主审反证为非新增缺陷；不能误报未知招式枚举 |
| C02 | 两个形态TutorMoves重复项 | 已定位WP20成员查询合同；重复不改变该查询，完整教学流程仍交WP28/30 |
| C03 | EffectChance101 | 非负字段允许；现有WP43保留大于100分支，建议主审反证为非新增缺陷 |
| C04 | BerryPlant到Item关联 | 正式已区分运行关联和编译枚举，建议主审反证为非新增缺陷 |
| C05 | Type/Move/Item有限省略默认缺口 | 例：Item只给单数名Review而省复数，复数为Unnamed；类型、招式另有尚未明确的省略组合。建议补有限合同和向量，保留现有已明示默认 |
| C06 | 部分形态指标记录的缺字段默认 | 显式形态指标省BackSprite得0,0；整条不存在再查询才克隆基础5,6。建议把这两个入口在正式合同分开 |
| C07 | 合法作者Happiness256可直接进入创建 | PBS只非负，物种和个体创建保留256；与WP30无条件0–255措辞冲突。仅为人工作者夹具，默认随附值没有该超界声称 |
| C08 | ShadowSize0的None标签范围 | 资源选择仍可请求Shadow/0；建议限定编辑标签与资源请求层。只做条件化路径反例，不认证像素或声称本快照有Graphics资源 |

每项均提供精确来源/正式定位、前提、普通对照、最小反例、取消/异常/部分状态范围、负搜索、必要消费者、影响、最小修订、保留scope、同步文件、验收和依赖。C05/C06/C08主要是完整性或措辞范围提案，C07为范围矛盾提案；是否接受仍须非提出者裁决。

## 文件入口与复算

- `field-semantic-rules.json`：116条人工规则，包含schema→默认/继承/覆盖/校验→必要消费者→正式/向量→导出边界。
- `field-rule-reading-gaps.json`、`field-semantics-summary.json`：必要真实区间缺读0及104/116计数。
- `header-contracts.json`：9类身份；不把指标/Shadow的可选形态号误扩成形态记录存在性校验。
- `source-to-spec-matrix.json`：16,732条全字段正向映射，含形态隐式固定继承字段。
- `spec-to-source-matrix.json`：正式条款→人工规则→具体源声明/消费者/记录/前提的反向映射；限定PBS作者scope。
- `record-inventory.jsonl`、`field-value-domains.json`、`shape-checks.json`、`reference-relations.json`：完整结构、值域和引用证据。语料只留哈希/长度，不复制参考程序。
- `stage-specific-reference-checks.json`、`embedded-flag-contracts.json`：阶段前提及旗标编码语义，不将运行fallback误判为编译非法。
- `profile-record-deltas.json`、`deduplication-proof.json`：每个备份与当前的逐记录/字段差异和精确重复证明。
- `move-effects-bidirectional-locations.json`、`shadow-formal-table-comparison.json`：效果定义/fallback/正式接线及153行有限表比较。
- `proposed-author-vectors.json`：116个规则级静态向量提案，全部NOT_EXECUTED；已有相关正式向量另逐条引用。
- `scope-boundary-and-handoffs.json`：明确域外所有者；`runtime-consumer-candidates.json`只是宽泛词法发现，不是需要重复审完的全游戏任务。
- `reading-ledger.jsonl`、`command-log.jsonl`、`direct-reading-coverage.json`：保留实际模型可见区间与程序全字节清点/标识扫描的区别，不把截断输出算全文阅读。

最终复算顺序为 `field_semantics.py` → `finalize_scope.py`。早期 `close_review.py`仅是初次未完成检查点，不能用于覆盖最终状态。大数组以`.json.gz`保存，同名`.json`记录编码/位置/尺寸/SHA-256；最终核验JSON语法、压缩收据、映射数量及受保护输入。没有执行参考、编译器、游戏、存档或外部服务，没有修改正式规格、提交/切换/推送或实现框架。

实际模型、effort、tier、速度及运行UUID未回显，均为UNVERIFIED，未查认证配置。后续仅由主审独立反证/裁决提案并整合跨域接线；本域没有剩余必需字段语义缺读，且没有全局或运行通过结论。
