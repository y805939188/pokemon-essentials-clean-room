# Battler 有限剩余接收组 1：P01A 报告及组入口

本组分配的语义审查完成，结论为 **BOUNDED_REVIEW_COMPLETE_FOREIGN_CUMULATIVE_JOINS_OPEN**。全部主责源体、正向断言、分配反向断言及必要消费者已核；新增 required、optional、policy 整改项均为 0。父任务 INCOMPLETE/最终签收状态由父协调者决定，本组不授 B8 全局 PASS 或 READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE。

合同固定于 `02c8206651676effe40ff9a33dbb70998b79c1b1`；目标作者提交 `5cf9503a99a855c06a8ac9c932e6778b57e71049`；B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。内嵌旧合同只作既有证据来源，不覆盖最新用户授权。

| 分片 | 完整主责结构 | 正向子断言 | 分配反向子断言 | 必要消费者事实 | 明示外域累计 facet |
| --- | ---: | ---: | ---: | ---: | ---: |
| P01A | 103 | 171 | 31 | 19 | 7 |
| [P01B](../../P01B/result/report.md) | 48 | 65 | 18 | 18 | 3 |
| [P02](../../P02/result/report.md) | 9 | 146 | 12 | 6 | 2 |
| 组内去重合计 | 160 | 382 | 61 | 23 | 12 |

分母互不相加。E006 主源 1–777 行与 E007 初始化主源 1–325 行完整阅读，共 1,102 行、37,959 bytes。P01A 主责是 E006 1–388 行内合同指定的 103 个完整对象。160 个结构包含 102 方法和 58 声明/数据/别名，内部字面 API 没有被提升为未来架构义务。

三份 prompt/readset 全文接收，共同前提一次复用。43 个去重完整正式映射组的 120 条上下文含义已读，仅签分配的 61 条反向断言。17 个跨片必要 Battler 方法及其 62 个断言也已核，作为反向上下文，不签兄弟片主责。六文件 bytes/SHA256/blob 与 dispatch 完全一致；身份/传输核验不产生语义信用。

P01A 的实质判断：

- 能力/id 与裸 item_id 是战斗局部，专用持物、HP、状态、等级、形态入口按各自顺序写穿。战斗持物未知输入规范为空再写穿，与个体未知持物请求忽略不同；局部先写的失败前缀不支持统一事务/回滚。
- 原五能力值、阶段及最终修正分层。Wonder Room 只交换防/特防的原读取；pbSpeed 按阶段整数基底、能力、物品、环境、麻痹、玩家徽章、末端 round/clamp 顺序；重量按独立顺序与模式门。
- pbTypes 先去重，BurnUp 删火；只有 Roost 所在分支空表才补一般，BurnUp 单独清空不补；额外类型须参数允许。原能力、有效性、14/19 不可失去/获得名单分别成立。
- gender/nature/shiny/super_shiny 直接委托不证明下游纯读，个体 getter 可缓存。普通 shiny 可取 Illusion，自身 super shiny 不随之替换。
- 野生初始 bitmap 取真实队伍个体，后续 sendOut 可取 Illusion。直接刷新方法未显式重算战斗能力值，但不足以证明 bitmap/species 下游无动态读取或缓存。

逐对象完整断言、前提、源范围、正式关系、消费者与独立语义理由在 [reception-ledger.json](reception-ledger.json)，不是从 ID 或行号授信用。[proposal-counters.json](proposal-counters.json) 的有限正常/边界/反例向量均为静态推导，未运行。直接对面选择的早 break 已被 WP39 明确覆盖，未当作新缺漏。

八事实强制后继及 31 个完整必要源片全文接收，并与固定直接源逐字一致。Handler add 保存原键，lookup/trigger 才按实际规则规范，空子类没有 registry resolve；copy 共享当时 handler。ExpGainModifier 缺省 -1；EVGainModifier 按登记有无给 false/true，不按回调结果统一消费。场景两路/直接刷新限制如上。原列去重 23 个完整 consumer 原事实、后继限制及独立理由见 [interfaces.json](interfaces.json)。

另按 FC20-HP.03 的反向需要，补读 RX-POKEMON-PP 完整事实及 E177 1–77 行，核持久 PP 夹限与 pbSetPP 的绑定/变身门；这 1 个附加反向消费者不混入原列 23 的分母。

本组分配源/断言/必要消费者未读数为 0。以下既有外域 facet 的**累计签收**仍 OPEN；局部 facet 和具名必要接点已核，不等于完整原 owner 域已接：

- P01A：FC20-HP.03、FC20-ITEM.03、FC43-ACCURACY.03、FC48-SPEEDWEIGHT.03、FC42-CONSUMERS.01、FC22-MEGA.01、FC67-DISPLAY.03。
- P01B：FC45-INDIRECT.02、FC47-CONTROL.01、FC41-TRAP.02。
- P02：FC42-GROWTH.01、FC42-GROWTH.02。

各项原 needed、owner 和局部理由保留在三个 interfaces/reception ledger。成长、终局还原、换出/逃跑、命中、天气/场地、Mega 等必要有限接点亦已补读；这些读取不扩张为全部合法建立方、菜单/控制路径或宿主结果。H01 的 ECB001/002 历史资格及 canonical/optional/facet 裁定、四中央接口累计、IF04 完整展示/宿主和全局 task-final 由父协调者/原接收者整合。它们不构成本组延期未读的主责。

[冻结分母](frozen-denominator.json)、[阅读台账](reading-ledger.json)、[共享证据清单](evidence/source-read-manifest.json) 与上述逐项文件构成完整交付。初次发布工具中断，临时结构丢失后，从同一持续审查记录与固定 readset 恢复；重新验证身份和必要源片，不产生新审查票或额外主责。恢复后的共享清单只列精确保留的范围，不把整份下载当全文语义信用。

独立新委派审查者没有参与目标编写，没有 spawn；三个片是同一实际上下文，不是三个投票。平台接收者 UUID、模型/effort/tier/Fast 均 UNVERIFIED，父线程号不冒充本人 UUID。根 AGENTS 及相关路径检查已处理，审查技能 clean-document-revision 明确排除审计报告。所选环境失败、重启后启动等待仍未恢复可用执行器；使用固定 GitHub 对象读取和普通发布，没有本地 checkout、dirty-tree 或 shell git 验证。大 forward-mapping 返回空 content 不授全文信用，17 个必要对象由固定兄弟 readset 取得并核完整源。

行为、模型、游戏、native、UI/音频、存档执行 **NOT_EXECUTED / 0**；未称运行测试通过。**UPDATE_NOT_STARTED**。唯一内容写集为 P01A/P01B/P02 的 result/，独占分支 `codex/r8-battler-reception-group-1-20261016`；用户最新普通 commit/push 授权覆盖旧 prompt 父统一发布指示。未整改、未改正式规格、未合并 main。实际提交/树/远端回读结果由 publication receipt 和最终交付绑定，避免自引用哈希。
