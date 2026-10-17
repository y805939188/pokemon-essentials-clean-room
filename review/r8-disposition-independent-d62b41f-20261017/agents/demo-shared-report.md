# Demo/DX 与共享根：固定基线独立语义复审

结论：**FAIL（固定基线粗标需返修）**。本域70行中21 PASS、49 FAIL；失败按下列3项根因汇总，逐feature明细见 `demo-shared-results.json`。分类/粒度独立判定61 PASS、9 FAIL；46行另受正式必需依赖遗漏影响，不能将这46行都误读为去向标签本身错误。

受审 commit `d62b41f4d620e50bb04c80a7505374bd284d8210`；固定来源 `fd1df570cad987dc3852a3b958f03916e317f7fe`；交付快照 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`；formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`。当前工作树HEAD与受审对象一致，10份源文档在这三身份及工作副本中逐字节相同。独立子任务 `/root/demo_shared_semantics`；请求 gpt-6.1-sol / ultra / default，实际模型、effort、tier、Fast均无权威echo，逐字段UNVERIFIED。

## 全文覆盖与机械证据

实际连续分块读完7份Demo/DX正文、正式README、scope-statement、Demo/DX测试目录；合计10文档、624,641字节、3,143行、339有效Markdown标题、70功能行。读取过程中超长工具输出发生截断的地方已用更小区间补读；全文包括120项效果参数、35项转换兼容表、全部测试表与尾部历史/向量。未把标题遍历或结构脚本当成全文阅读。

| 文档 | 全文区间 | 标题 | 功能 | SHA256 |
| --- | --- | --- | --- | --- |
| README.md | L1–L169 | 14 | 0 | `36360d775d9f88a09dbed1146db2ba1c00e5fc8d401792eb401516c5951b0174` |
| wp72-debug-contexts-and-controls.md | L1–L451 | 43 | 9 | `4e6142b356d5c8937572e56120ca17b2f84b26bdfb5afb85a5e4ec4b18b70509` |
| wp73-a-content-editors.md | L1–L225 | 26 | 7 | `4d1702ddc9bb3f915239bba917882148da21753cd718e0b18552ea0dba6b9f0f` |
| wp73-b-world-editors.md | L1–L220 | 27 | 8 | `624c021c96f2507495109cedb33f8fe3064bc34520b6b552d19f5de941e493b1` |
| wp74-battle-animation-authoring-and-exchange.md | L1–L521 | 66 | 17 | `3676fec795b326d9b4fea6aab934537db419e2fbc6a3d7d52fec2bfce83adf77` |
| wp75-project-conversion-and-authoring-tools.md | L1–L460 | 53 | 14 | `48f8fb39334b07e3124f20dab42ccb8a8d133057dad47985bfd420cc10b02c5c` |
| wp76-facility-content-generation-and-simulation.md | L1–L279 | 42 | 9 | `354028776cd47dfab5c12d5bf1b41ed0b65dec5c335b9a2b4b618b560ca3a75b` |
| wp77-demo-evidence-and-capability-coverage.md | L1–L230 | 34 | 6 | `d1ba7c694f41ee5c3763a725467996632264e504563be74036c20d6ad5021ca6` |
| scope-statement.md | L1–L155 | 15 | 0 | `3261173cf02c47650c6cd7f7cbbacde73bc1c5e6f662880ffa180d0f29bb809a` |
| demo-dx-wp72-73-74-75-76-77.md | L1–L433 | 19 | 0 | `1ab7fc2ee02df106045eda5435e2c037c944b87216582d1f8c00392214366104` |

`demo-shared-evidence.json`保留每文档完整固定路径、字节/行/标题、blob/SHA、实际阅读区间及元数据映射，全部70行的来源unit/heading、状态分离和生成视图字段核对。独立只读Git/Markdown/JSON检查exit 0，errors=[]；标题映射全相等、功能区间无重叠、70源unit哈希一致，生成view全部70个唯一ID与来源/计划/状态/依赖关键字段一致。生成视图105,043字节，SHA256 `a5073e6eb9a18cc6e939621583638a2987461df1a622b1141049c3b1595025c8`。人工核视图表头及WP72连续行，重复生成文字未单独再全文语义读取；全文语义判定来自完整来源正文及每行计划字段。

## 必修问题

### DS-001 / P2：WP72战斗调试没有战斗引擎协作边界

涉及：FR-000257, FR-000261。

MZ+框架通用宿主理由覆盖了测试战斗生成/加载事件、捕获/结算、原个体与战斗当前写穿、120项四层效果、AI/NPC资源与退出后形态/场地刷新。没有Showdown协作方，也没有固定战斗引擎后的可编辑性/暂停恢复/同步/随机/异常问题。待验证不是免除承载假设合理性的理由。

来源：demo-dx/wp72-debug-contexts-and-controls.md:L177-L230；demo-dx/wp72-debug-contexts-and-controls.md:L307-L451。候选位置：routing-manifest.json:L31353/L31713；views/demo-dx.md对应行。

必要修正：保留原ID历史；按真实跨去向/验收边界拆宿主UI与测试开战/战斗观察写入。后者登记双方协作或具名待原型决定，列状态映射、持久写穿、原型许可、随机/事件顺序与异常前缀问题。不要为了修标签改正文。

### DS-003 / P3：来源归属与Demo证据登记被制造为独立实现功能

涉及：FR-000266, FR-000317, FR-000318, FR-000319, FR-000320, FR-000321, FR-000322。

WP73-A§7明确“只登记，不展开”；WP77明确配置存在不等于演示、登记材料实际能证明什么。§8跨表检查和§9缺口不是新实现能力，§4–7也主要是配置证据与既有消费者引用。machine却以behavior-unit建立未来框架/MZ实现行，和rationale“支持规划和验收设计”不一致。

来源：demo-dx/wp73-a-content-editors.md:L193-L198；demo-dx/wp77-demo-evidence-and-capability-coverage.md:L49-L197。候选位置：routing-manifest.json:L32159/L36712-L37359；section-coverage.json对应behavior-unit。

必要修正：保留已经发放的稳定ID为历史导航/继承关系，显式区分元数据记录与实现功能分母；按真实消费者关联。不要直接删除/重新seed编号，也不要把未证Demo链改成不纳入。若确需未来Demo建设功能，应另给用户授权范围和独立验收目标。

### DS-004 / P3：规划WP依赖被当成完整正式章节依赖，漏掉显式必需消费者

涉及：FR-000277, FR-000278, FR-000279, FR-000280, FR-000281, FR-000282, FR-000283, FR-000284, FR-000285, FR-000286, FR-000287, FR-000288, FR-000289, FR-000290, FR-000291, FR-000292, FR-000293, FR-000294, FR-000295, FR-000296, FR-000297, FR-000298, FR-000299, FR-000300, FR-000301, FR-000302, FR-000303, FR-000304, FR-000305, FR-000306, FR-000307, FR-000308, FR-000309, FR-000310, FR-000311, FR-000312, FR-000313, FR-000314, FR-000315, FR-000316, FR-000317, FR-000318, FR-000319, FR-000320, FR-000321, FR-000322。

doc_bindings只复制既有WP索引dependencies，没有正式正文语义校准。WP74显式6必需却仅15/16/67-A，漏04/72/73-A；WP75显式7必需却仅04/13/15/17，漏08/61/73-A；WP76还明列44/72/73-A/75/08未登记；WP77§11.1明列的04/02/11/12/14/15/17/36/57/27/54/55/56均未在依赖字段表达。feature_refs均空、differences仅通用句，无法补足。

来源：demo-dx/wp74-battle-animation-authoring-and-exchange.md:L515-L521；demo-dx/wp75-project-conversion-and-authoring-tools.md:L454-L460；demo-dx/wp76-facility-content-generation-and-simulation.md:L271-L279；demo-dx/wp77-demo-evidence-and-capability-coverage.md:L202-L213。候选位置：routing-manifest.json DOC-0043–0046所有features dependencies；routing.py:129–134。

必要修正：保留原WP计划依赖的来源身份并给类型，补正式合同必需/同批共享/边界引用；至少逐文档语义核对显式必需清单。允许章节级粗标继承整篇依赖，但不能将旧计划字段冒称完整正文依赖。

## 粗标判断与元数据

允许MZ主责并列框架伙伴承接作者编辑交互；未因每次持久写入自动要求拆ID，也未把通用rationale本身当FAIL。WP73-A数据提交FR-000265与WP74交换FR-000285/287的框架分类合理；WP76真实分支FR-000313单拆协作，父行FR-000312排除L164–170，剩余估算/评级归框架合理。特殊玩法、Shadow、调试/编辑器、XP旧工程/格式迁移均保持阶段待定/未批准，排除0，未将未知材料转成“不纳入”。

两共享根都是治理/范围/证据资格，不造实现功能；ALL_FORMAL_FEATURES广域元数据关联合理。测试目录19标题只作静态验收来源，不升级运行通过；同70行的广绑按本次粗标口径可作整目录导航，精确按DG/CE/WE/AN/CV/GN/DM、TOOL-AN/R7-U11家族关联为非阻塞改进。DS-002/DS-005在JSON中明确列为观察，不混入必修/FAIL。

本域10文档都不在R8九批正式实际写集中，空batches与“固定基线待后继差分核对”保持诚实，没有accepted_events；未把U07历史/源索引职责自动误绑为本域正文改动。U07及全仓183待整改绑定由父审者核验。

## 限制与交接

所有70行去向待验证、阶段待定、未实现/未验收与空证据分离正确；没有把来源规格或数据一致性当成Showdown行为兼容证书。本任务没有运行Ruby、参考游戏、MZ、Showdown原型、框架或行为向量。没有修改作者清单/正式规格/参考/main/历史报告，没有切分支或commit/push；只写本独占demo-shared前缀，发布由父任务执行。

固定基线初版不能称最终验收。返修后需要新的精确candidate复核，R8实际整改正式接受后还要以协调任务给定固定基线回填、差异校准并独立核验。
