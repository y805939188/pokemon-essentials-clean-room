# 固定候选独立完整复审：FAIL

受审候选 `d62b41f4d620e50bb04c80a7505374bd284d8210` 的固定基线粗标**不通过，须返修后绑定新 SHA 复核**。全文阅读已覆盖全部131份正式文档；未以标题遍历或结构脚本代替语义阅读。逐项功能结果为 448 PASS、227 FAIL、46 待查。PASS仅表示本次粗标相应范围可接受；待查行已读，但职责依据不足。当前不授予最终整改验收。

## 固定输入和任务资格

固定交付 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`，历史正式来源 `fd1df570cad987dc3852a3b958f03916e317f7fe`；来源、交付及候选正式子树均为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。只读参考提交 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。候选25文件集合、24个非自指文件的bytes/SHA256/blob/mode及manifest本身身份已核对，无差异；完整身份见 [固定输入证据](evidence/candidate-identities.json)。

用户委派请求为 gpt-6.1-sol / ultra / default。可见本上下文 `/root` 及11个累计审查上下文；真实云任务UUID与平台创建回显未暴露，实际model/effort/tier/speed/Fast逐字段UNVERIFIED。原生工具没有default tier入参且广告为priority，不能据其推造普通档执行资格。各子审仅为同一独立复审的分工，不另计独立验收票；作者原候选没有由本团队改写。[配置资格证据](evidence/task-qualification.json)保留此缺口。

## 完整覆盖与读取方式

| 口径 | 文档 | 字节 | 正文行 | 标题 |
| --- | ---: | ---: | ---: | ---: |
| shared-governance | 3 | 88443 | 451 | 46 |
| behavior-or-data | 111 | 3152779 | 23496 | 2389 |
| test-design | 17 | 1122886 | 6009 | 248 |

总计131文档、4,364,108字节、29,956行、2683标题（H1=131/H2=1307/H3=1212/H4=33）；721是候选功能行数，不能代替行为覆盖。原始specs/113份、87WP计划行（84内容+3阶段）另计。文件全集由固定Git树、正式README/测试索引和现行固定索引联合核对；没有硬编码131忽略差异。

各领域连续分块全文读过正文、表格、历史与限制层，截断区间补读；后继上下文补完kernel和所有未读catalog。每文档实际范围/哈希/归属证据见 [阅读覆盖](reading-coverage.json)，未读文档及正文行均为0。root负责全局协议、schema/577行工具、状态/批次/保护和补充复核；没有冒称root亲自重读所有委派正文。重复生成视图以10文件逐字节重建和721逐行关键字段投影核对，不另算一次全文语义阅读。

[721项裁定](feature-results.json)保留具体源锚点/行范围、候选JSON pointer/实际行号、生成view行号及每项审查理由；[2683章节导航](section-results.json)保留全部映射及阅读归属。标题结构通过没有被升级为章节分类合理性通过。管理/历史/测试元数据可以关联合适的功能；问题单列出其中吞掉真实行为或制造伪功能的反例。

## 复审合同九项裁定

| 项 | 结果 | 限定理由 |
| --- | --- | --- |
| 1. 正式全集与章节 | FAIL | 机械全集通过；存在行为漏标/元数据伪功能 |
| 2. 固定定位与历史身份 | PASS | 仅当前固定身份及seed拒重建；后继续接仍待验 |
| 3. 粒度与分类 | FAIL | 混合职责及独立验收边界未完整表达 |
| 4. 五类去向及范围决定 | FAIL | 枚举/排除0正确；部分特殊范围门缺传播 |
| 5. 协作与行为证据 | FAIL | 四门诚实未运行；相关消费者与归属遗漏 |
| 6. 字段与状态分离 | FAIL | 状态分栏正确；具体归属/必要依赖/来源分类有缺口 |
| 7. 整改绑定及后继校准 | PASS | 仅基线183行保守绑定；最终校准待办 |
| 8. 工具及生成视图 | FAIL | 原校验/生成通过；扩展静态负例暴露缺口 |
| 9. 隔离与保全 | PASS | 仅本次可观察路径、参考与main保护范围 |

## 按严重度列出的问题

共44组问题，完整可复现源区间、功能ID、候选位置、原因及必要修正在 [findings.json](findings.json) 和各域报告。组内多个ID共享根因；不能把组数当不同新历史根或整改必修分母。

| ID | 严重度 | 问题 | 详情 |
| --- | --- | --- | --- |
| CK-BATTLE-001 | P2 | 持久状态与战斗执行的明确交界仍只有框架职责 | [agents/creature-kernel-results.json](agents/creature-kernel-results.json) |
| CK-META-001 | P2 | WP27两个可验收行为子节被概念父节吞成元数据 | [agents/creature-kernel-results.json](agents/creature-kernel-results.json) |
| COMBAT-01 | P2 | 退款后续消费者落回Showdown父行，物品原型范围不完整 | [agents/combat-results.json](agents/combat-results.json) |
| COMBAT-02 | P2 | 持久写回、学习和物权边界被整体Showdown标签掩盖 | [agents/combat-results.json](agents/combat-results.json) |
| COMBAT-03 | P2 | 独立音频、队伍选择与裁判/回放交互未拆表现边界 | [agents/combat-results.json](agents/combat-results.json) |
| COMBAT-05 | P2 | 文档模板依赖漏掉直接背包、成长、终局、保存和图鉴消费者 | [agents/combat-results.json](agents/combat-results.json) |
| COMBAT-06 | P2 | 替补/招式逃离的协作原型只覆盖一个标题 | [agents/combat-results.json](agents/combat-results.json) |
| DS-001 | P2 | WP72战斗调试没有战斗引擎协作边界 | [agents/demo-shared-results.json](agents/demo-shared-results.json) |
| KF-002 | P2 | 日志/控制流与宿主呈现、启动/恢复与持久状态的独立承载边界被合并 | [agents/kernel-full-results.json](agents/kernel-full-results.json) |
| KF-003 | P2 | 随机服务父行吞入战斗记录/回放协作合同 | [agents/kernel-full-results.json](agents/kernel-full-results.json) |
| POK-S01 | P2 | 核心行为被概念标题规则降为metadata | [agents/pokemon-results.json](agents/pokemon-results.json) |
| POK-S02 | P2 | Shadow跨战斗/成长/主动道具界面未拆协作 | [agents/pokemon-results.json](agents/pokemon-results.json) |
| POK-S03 | P2 | 漫游复用个体与逃跑结果写回被框架单方吞并 | [agents/pokemon-results.json](agents/pokemon-results.json) |
| POK-S04 | P2 | 持久异常与持物提交没有明确两端责任 | [agents/pokemon-results.json](agents/pokemon-results.json) |
| POK-S05 | P2 | 同节UI/资源/宿主时序未按独立验收边界拆分 | [agents/pokemon-results.json](agents/pokemon-results.json) |
| POK-S06 | P2 | 进化演出整节承包了领域提交 | [agents/pokemon-results.json](agents/pokemon-results.json) |
| ROOT-TOOL-01 | P2 | 验证器放过失真的当前定位和部分身份/章节字段 | [root-findings.json](root-findings.json) |
| WU-01 | P2 | 元数据规则吞掉完整行为或主数据 | [agents/world-ui-findings.json](agents/world-ui-findings.json) |
| WU-02 | P2 | 独立特殊玩法规则被统一标为MZ表现 | [agents/world-ui-findings.json](agents/world-ui-findings.json) |
| WU-03 | P2 | 战斗交互行缺具体协作原型边界 | [agents/world-ui-findings.json](agents/world-ui-findings.json) |
| CAI-01 | P3 | AI全41行协作标签共用整篇理由，未给实际AI承载边界 | [agents/combat-ai-report.json](agents/combat-ai-report.json) |
| CAI-02 | P3 | 责任与保留章节被制造成独立待实现功能 | [agents/combat-ai-report.json](agents/combat-ai-report.json) |
| CAI-03 | P3 | 从旧WP计划复制的依赖遗漏现行正文的明确评分消费者 | [agents/combat-ai-report.json](agents/combat-ai-report.json) |
| CC-CATALOG-F01 | P3 | WP68编号碰撞把Triad静态目录错误关联到Duel动作对决 | [agents/cc-catalog-full-results.json](agents/cc-catalog-full-results.json) |
| CK-DEP-001 | P3 | 重要新拆边界仍只继承旧WP计划依赖而漏正式直接合同 | [agents/creature-kernel-results.json](agents/creature-kernel-results.json) |
| CK-MIXED-001 | P3 | 特殊玩法泛列MZ伙伴仍未说明交互/规则的不同验收点 | [agents/creature-kernel-results.json](agents/creature-kernel-results.json) |
| CK-MZ-001 | P3 | 多处真实UI/事件交界继承整篇框架模板而无宿主职责 | [agents/creature-kernel-results.json](agents/creature-kernel-results.json) |
| CK-TOOLS-001 | P3 | 嵌在领域文档内的调试/作者工具未保留专门范围决定 | [agents/creature-kernel-results.json](agents/creature-kernel-results.json) |
| COMBAT-04 | P3 | 覆盖、域外归属和历史保留被制造成独立实现功能 | [agents/combat-results.json](agents/combat-results.json) |
| DS-003 | P3 | 来源归属与Demo证据登记被制造为独立实现功能 | [agents/demo-shared-results.json](agents/demo-shared-results.json) |
| DS-004 | P3 | 规划WP依赖被当成完整正式章节依赖，漏掉显式必需消费者 | [agents/demo-shared-results.json](agents/demo-shared-results.json) |
| KF-001 | P3 | 纯未验证/责任索引被制造为独立实现功能 | [agents/kernel-full-results.json](agents/kernel-full-results.json) |
| KF-004 | P3 | 依赖字段沿旧WP计划复制，遗漏正文已有的必要调用/状态合同 | [agents/kernel-full-results.json](agents/kernel-full-results.json) |
| KF-005 | P3 | 旧格式支持范围未接上已有用户决策门 | [agents/kernel-full-results.json](agents/kernel-full-results.json) |
| KF-006 | P3 | 统计附表被填入不存在的“共享导航/无实现承诺”来源分类 | [agents/kernel-full-results.json](agents/kernel-full-results.json) |
| POK-S07 | P3 | 纯证据/向量/范围段被制造为实现功能 | [agents/pokemon-results.json](agents/pokemon-results.json) |
| POK-S08 | P3 | 作者内容缺省/校验与战斗配置被同标Showdown | [agents/pokemon-results.json](agents/pokemon-results.json) |
| ROOT-TOOL-02 | P3 | 已知批次/接受事件和计划引用的结构关系缺少核验 | [root-findings.json](root-findings.json) |
| WORLD-CATALOG-F01 | P3 | 同一WP编号下的不同子体系被当成测试消费者 | [agents/world-catalog-full-results.json](agents/world-catalog-full-results.json) |
| WORLD-CATALOG-F02 | P3 | 具名跨领域验收章节缺必要消费者与协作原型入口 | [agents/world-catalog-full-results.json](agents/world-catalog-full-results.json) |
| WU-04 | P3 | 名人堂持久记录与演出未分责任 | [agents/world-ui-findings.json](agents/world-ui-findings.json) |
| WU-05 | P3 | 特殊体系消费者缺对应范围决定入口 | [agents/world-ui-findings.json](agents/world-ui-findings.json) |
| WU-06 | P3 | 实际消费者依赖未落入行字段 | [agents/world-ui-findings.json](agents/world-ui-findings.json) |
| WU-07 | P3 | 审计/依赖说明被制造为独立功能 | [agents/world-ui-findings.json](agents/world-ui-findings.json) |

关键反例已由root额外核实：WP40 §4.2.1 L106–115的退款残留身份仍落FR-000010/Showdown，FR-000011协作范围仅L97–105；§4.2.1实际为同级H3，问题是语义后续消费者遗漏，并非虚构的H4解析错误。WP27 §2.1–2.2 L45–72的缺省/数量显示真实行为、Mining数据附页L9–75的61候选主表却只获泛元数据映射。WP74 §21明确6个必需依赖，清单仅3个。源定位完整和数据一致均不能消除这些语义缺口。

返修须保留既有stable ID、immutable source和原规格事实。可追加子行/继承或把伪功能保留为历史导航并转元数据关联；不要删旧ID重新seed，也不要修改正式正文来使清单通过。允许章节级粗标以及MZ带框架伙伴处理普通交互提交；本报告不要求逐句/逐向量造ID。纯数值/战斗内部规则可继续保留Showdown候选，未指控Showdown实际不支持；需解决的是具体持久状态/资源/宿主消费者归属及必要依赖。

## 工具、状态和整改绑定

作者validate、check-generated、assess-current实际exit=0，stdout/stderr/UTC见 [命令日志](evidence/commands.jsonl)。check-generated重建比较10文件无陈旧；隔离运行原CLI self-test/render/check-generated均exit=0，原9负例全拒；seed对已存在清单exit=1拒重建；仅在本review隔离副本追加STALE PROBE后check-generated exit=1拒陈旧view。原工件始终未改。

扩展14负例3拒绝、11接受；[扩展结果](evidence/extended-validator-negatives.json)与保留脚本可复现。错误当前提交/路径、失真部分身份字段、已知批次删除和未绑定接受事件等结构问题列为必修工具缺口。任意目标证据结构的真实性、分类依据、用户决定及源引用是否等于兼容证据仍须人工审核；没有要求工具自动证明运行行为。

独立复算确认所有721行去向待验证、阶段待定且未批准、未实现、未验收；排除0。捕获/主动战斗道具/逃跑/战中成长四门均未运行，当前没有固定目标Showdown版本/世代/格式。没有原型本身不阻止合格粗标收尾；遗漏相关调用者、消费关系和具体问题仍是本候选缺陷。

183行/32文档的整文件保守R8绑定与固定actual_target_write_set一致，保留待整改后核对和空接受事件。此绑定没有声称每个finding都修改每行。U07必修写集仅新导航overlay，正式行不应虚绑；其资格/来源索引后继须单独检查，正式tree不变不能证明U07已校准。[绑定证据](evidence/batch-binding-check.json)、[U07范围](evidence/u07-routing-scope.json)。

本任务收到整改接受候选/回执0；旧handoff的UPDATE_NOT_STARTED按生成时点保留，不作为协调线程实时状态。修订任务 `01a14a05-405f-7581-9119-73cd53d4a0d2` 返修后须给新40位SHA；协调任务 `01a14a04-b178-7567-a4eb-0f0bfac9a0d9` 提供正式接受固定基线后，还须回填current_applicability、完整受影响差分/消费者/依赖及独立再验收。初版粗标、R8规格整改、实际整合、接受和关闭分别登记。

## 隔离和交付边界

交付→候选完整差分仅新增25个独立打标文件；正式规格子树未变，历史报告/来源材料不改。只读参考HEAD正确且diff空；远端main在观察时仍为fd1df57。本团队仅在本独占review目录写报告/静态证据；无参考/游戏/Ruby/宿主/Showdown/框架/业务向量执行，无force、删除历史或合并main。

输出commit由发布回执和父任务转交消息作外部绑定，不在该commit内填未来自指SHA。推送与独立远端回读须按实际发布证据核实；本报告的FAIL不会因推送成功转为通过。后续仍待用户范围决定、目标行为原型、上游正式校准，以及可得的真实云任务/执行配置资格。
