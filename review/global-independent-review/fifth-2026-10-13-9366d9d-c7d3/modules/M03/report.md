# M03 第五轮全局独立审查

`schema_version: gr5.review.v1` · `complete: true`

已完成分配范围内全部可得、可审的静态语义审查。发现 **13 条 P2 候选**，全部保持 `candidate_pending_independent_counterevidence`；`disposition=required` 仅为修订建议，**最终必修签核数为 0**，等待父会话独立反证。

固定规格 B5：`9366d9d17aaeac3b4414236468affa650fb3dd27`，正式子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。固定参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，来自任务指定的只读参考根。主会话身份核验未重复。

模型请求沿用父会话声明的 `gpt-6-astra / ultra / service_tier=default`；实际参数回显 **UNVERIFIED**。未请求 Fast、未替换模型，未调查额度、认证、私有会话或后端；未创建会话或子 agent。

## 候选

| ID | 需要独立反证的行为 | 等级 |
| --- | --- | --- |
| GR5-M03-001 | 页切换与路线41的朝向/图案写入缺少“原始值改变”门 | P2 |
| GR5-M03-002 | 绑定地图与当前地图的“本事件”身份未分列，跟随互动可命中同ID地图事件 | P2 |
| GR5-M03-003 | 事件私有冷却只有“过期”概述，缺秒/日算法与登记刷新合同 | P2 |
| GR5-M03-004 | 强制路线安装、覆盖和自主频率的调度合同不完整 | P2 |
| GR5-M03-005 | 玩家对角路线的位移未累计距离，且绕过四向移动副作用 | P2 |
| GR5-M03-006 | 零偏移原地跳跃不经过占格许可门 | P2 |
| GR5-M03-007 | 事件脚本直接钓鱼可运行公共事件后仍执行内置演出 | P2 |
| GR5-M03-008 | 力量只写激活状态，推动巨石的严格通行与提交顺序未承接 | P2 |
| GR5-M03-009 | 命令202漏掉变量位置、交换位置与缺目标/朝向分支 | P2 |
| GR5-M03-010 | 同一s:开关在页/公共并行/条件分支/公共自动运行中的语义不同 | P2 |
| GR5-M03-011 | 树果确认等待期间仍可重植，拒摘后“保持成熟”缺少时间推进边界 | P2 |
| GR5-M03-012 | 消去/碎除脚本辅助的索引自增会跳过独立脚本后的下一命令 | P2 |
| GR5-M03-013 | 地牢34/136错误修复缺少决定局部墙/通道改写的条件合同 | P2 |

每条候选的源版本、行范围、入口/调用者/配置、当前合同、最小反例、正常/失败对照、实际负证据阅读、建议与静态验收条件均在 [findings.json](findings.json)。它们描述固定参考事实；是否复刻异常属于后续兼容政策，不要求修改参考或设计新框架。

## 覆盖和限制

- source-first 逐段完成 Scene_Map、Interpreter、全部主事件命令、Map/Factory/Character/Event/Player/CommonEvent/两份 Followers，以及 Overworld 核心、Metadata、Time、FieldMoves、Fishing、BerryPlants、RandomDungeons。每段规则比较及确切未审区间见 [reading-coverage.json](reading-coverage.json)。必要 caller、覆写、注册、刷新、让出和异常前缀均已纳入。
- 96 个主分派命令与路线码 0–45 各有独立兼容映射；数字只用于入口核对，不作为功能覆盖率或执行证据。配置、18 地形记录、9 天气记录、全部地图元数据/连接/地牢记录及树果数据消费均有分段/按键记录。M01 的结构审查与 M03 的消费语义不重复计为能力。
- 10 份分配正式正文/矩阵及相应 10 份 B5 specs 原稿已全文比较；各节、条款、表行和本域向量映射见 [spec-to-source.json](spec-to-source.json)。同文件的原稿检查未发现未承接的独有正确业务事实；结构性表达正确排除，旧错误由当前合同替代。新候选来自源语义缺口，不能归咎于净化时丢稿。
- B21 archive 精确对象中的 CASE-DISPATCH、SOURCE-PATH 已跟读并复核；CHAIN-2/6/8只作导航，已逆查当前合同。AX20 负水分与惩罚时点支持当前树果规则。未递归审计历史管理包，未继承旧 PASS。GR3-M09-001 暂缓与 GR3-M02-003 NO_REQUIRED 保持。
- 缺失的是实际 Map/CommonEvents/Tilesets/System 等二进制 Demo 内容；未据此虚构地图大小、事件编排、宿主效果或运行可达性。PBS 51 的 Dungeon=true 文本可读，与实际 Map051 文件缺失分开记录。依赖文件的 partial 区间为其它主责域的未读尾段，不冒称这些文件全文已审；本模块分配可得主责范围没有遗留未审段。

## 共享接口与反证结果

[shared-interfaces.json](shared-interfaces.json) 为每项共享能力保留唯一身份及 M03/M06/M10/M01 等消费者投影。移动/地图状态与渲染音频分开签核；本报告不代签其它模块。

现有正面反证排除了资源添加非原子行为、5000 变量/开关上限、过场跳过、冲浪临时残留、116让出、旧树果显示链不结算等重复缺失说法。119缺标签的静态回落、mapTrail重复等作为可选完善记录，未为文风或内部辅助强立必修。完整来源→合同评估及这些判断见 [source-to-spec.json](source-to-spec.json)。本地 [feature-matrix-projection.json](feature-matrix-projection.json) 供父会话合并；共享 Feature Matrix 未修改。

## 验证与交付

只运行文件读取、数据记录解析、JSON/必需字段/引用与行范围校验；[artifact-validation.json](artifact-validation.json) 的文档结构检查无错误。这些检查不是参考执行、模型执行或宿主测试。所有行为向量均 **NOT_EXECUTED**，第四轮隔离执行不计入本轮。

仅在指定 M03 目录写入审查产物；未修改正式规格、参考、历史证据或共享报告，未提交、推送、update、安装工具、改配置或外传原数据。下一步是父会话对 13 条候选进行独立反证与跨模块去重；M03 无剩余可得主责阅读任务。
