# 本轮报告 schema 与口径

JSON文件均schema_version 1.0。findings.json的findings为最终规范ID数组；模块原始提出、独立反证与汇总裁决通过review_resolution和独立记录保留。必修只计disposition=REQUIRED且最终CONFIRMED；OPTIONAL、UNRESOLVED、NO_REQUIRED_REVISION另分母，重复项不再计为规范ID。P1/P2/P3按实际实现影响，不按文风。

每条finding字段包含身份/主责/严重性/处置，固定B/R，source/spec anchors，参考事实、现规格表述和差异，前提/最小反例/正常与边界，独立实现影响，全套规格及源端反证搜索，建议最小修订，静态与运行验收要求，影响文件与依赖，历史关联，证据类别与未执行限制，未知/排除/政策决定与最终裁决。锚点中源符号只作审计定位，不要求未来实现同样组织。正式文件精确身份共用evidence/formal-identity-check.json。

覆盖status统一supported、partial、missing、unresolved、not_reviewed。supported只承认checked_branches_boundaries和premises中的范围；SOURCE_STATIC/SPEC_STATIC的supported即supported_static，不表示运行通过或其他变体通过。partial表示已承接但某重要范围不充分；missing必须有正面源证据且经全套规格/合理别名反证仍无承接；unresolved表示资料/证据不足；not_reviewed表示没有实际语义检查。material_availability单列，缺资料不等于规格缺能力。

source-to-spec矩阵以稳定capability_id为主，允许明确标注主身份与消费投影；它是本轮记录的有界能力集合，不是参考全功能数学全集。文件责任盘点与历史113/757/432/131各有不同分母，不能相除成全功能覆盖率。spec-to-source每份正式文件一行，保留各reviewer实际契约投影、未审部分与依据，不用身份一致代替语义支持。

证据级别：SOURCE_STATIC=源码/数据/调用静态审阅；SPEC_STATIC=规格与静态向量审阅；DERIVED_VECTOR=推导未执行案例；TOOL_VALIDATION=身份/路径/格式/报告结构检查；EXECUTED_MODEL=运行独立模型（须说明与R距离）；EXECUTED_REFERENCE=运行固定参考路径（须说明宿主、夹具与差距）；EXECUTED_HOST_OR_DEMO=真实宿主/UI/Demo观察。它们不是从低到高可自动继承的总等级。

历史229项与341 scoped contributions保持原控制、owner、输入候选/实际/独立报告身份及qualification；默认historical_qualified_evidence_reused/not_reexecuted。仅本轮明确列出的语义投影是新审查，不向同ID其他owner或其他条件扩张。GR3历史CLOSED保持；新证据另建GR4身份。
