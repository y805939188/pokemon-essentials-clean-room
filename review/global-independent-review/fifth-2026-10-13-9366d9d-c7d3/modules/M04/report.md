# M04 第五轮独立静态审查

本模块分配的可得、可审范围已完成全文语义审查与现行合同反查。结论不是全量 PASS：**3 个同根因合并后的候选，均为 P2 / unresolved / candidate_pending_independent_counterevidence；最终必修签出 0。** 未执行参考、独立行为模型、游戏、编译器、界面或历史 R4 探针。

固定规格 B5：`9366d9d17aaeac3b4414236468affa650fb3dd27`，正式子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。固定参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。请求参数 `gpt-6-astra / ultra / service_tier=default`；实际参数回显 **UNVERIFIED**。未调查额度、认证、私有会话、后端或模型配置；未创建会话或子 agent。

## 候选

| ID | 静态发现与最小反例 | 受影响合同 |
| --- | --- | --- |
| GR5-M04-001 | **特性候选枚举不限两项自然候选。** 人工有效配置自然表 `[OVERGROW, CHLOROPHYLL, TORRENT]`、隐藏表空，候选仍包含第三项、索引 2。药膏据该候选可成功写索引 2并以 TORRENT 命名消息，随后实际解析因隐藏缺项回到 PID 决定的自然特性。默认数据没有这种三自然项配置，不把它伪称默认样本。 | WP19 §3.4 的自然候选 0/1 限定；WP28 药膏、WP72 可能特性选择的消费投影。 |
| GR5-M04-002 | **显示读取会提交形态，且可在提示型提交中重入。** 摘要仅打开即可提交过期 FURFROU；WP66A 仍称一切显示只读。正常队伍界面首次给形态 0、时间戳空的 HOOPA 用 PRISONBOTTLE：先写 1，中途刷新图标读动态形态又提交 0，外层之后才写新时间戳；最终仍 0、时间戳新、效果真、重要物品不消耗，与 WP28 的 0↔1 成功输出不符。两消费者按同一显示读取根因合并。 | WP66A §8；WP28 §5.6；WP21 提示型提交与动态读取的交界。WP18/WP21/WP15 已正确的取图主合同不重报缺失。 |
| GR5-M04-003 | **两项 Shadow 专用实际伤害合同未完成交接。** Shadow Half 对存活场上 HP>1 者扣当前 HP 整除 2，之后全场恢复物品检查并建立使用者休息；Shadow End 在所有击后按使用者当时当前 HP 半数四舍五入、至少 1 反伤，绕过普通防反伤能力门。现行只找到数据身份、排除表及 AI 评分，不能替代实际执行合同。例如 End 的 U 当前 5/总 20 且目标受影响，扣 3余 2，即使有效 MAGICGUARD/ROCKHEAD。 | WP23 的战斗效果委派、Shadow 数据附表与 WP46 实际效果接收；WP52B 仅作预测消费者。可选内容未默认启用的边界保持。 |

每项的精确源行、调用者、当前条款、正反例、已读反证范围、影响、静态验收及排除声明在 [findings.json](findings.json)。父会话仍须安排独立反证后裁决，不将本报告的候选直接升级为必修。

## 已完成的实质范围

- Pokemon 本体、Owner、Move、Mega、Shadow、FormHandlers、ShadowOther、PokemonSprites、PurifyChamber 全文逐段分析；另完整跟读 PokemonStorage 的个体状态/净化室消费边界。10 份核心及完整跟读文件没有未审行段。
- 全部形态注册、复制注册、默认/空返回、分支、错误及必要调用链；包括提示型/普通/简化提交、强制形态、战斗/仓库守卫、创建与地区蛋、存储和显示、融合招式变化、Mega/Primal 许可与分入口收尾、净化室真实输入和接收链。
- 必要 GrowthRate、Nature、Stat、Species、Species_files、Metrics、Shadow 数据以及直接调用者。字段的实际消费与 schema 主责分开；成长、繁育、进化按稳定能力投影到 M06，不重复签出其整域结论。
- 正式 WP18/19/20/21/22/23、transformation-data、shadow-data 八份全文，以及八份 B5 specs 原稿全文。正式表、案例及主责测试 CI28、HP45、ST67、FM43、ME26、SH52、R4-IF6、U03-SP10、U03-SZ20 共 297 个具名向量逐条比较；共享测试文件其它模块族明确保留为本审者未审。
- 默认 48 个 Mega 目标逐条数据/条件/基础 HP 对照，47 石、环与宝珠的字段消费；可选 Shadow 131 项配置、18 招、4 物品、1 类型全文。只读文本核对额外确认 48/131 表无转录差异；自动核对没有被当作语义审查或运行验证。

共记录 96 个源文件/数据路径：29 full、67 partial。后者是必要调用者或字段投影，逐路径列明实际已审范围及其余物理行段；**不声称这些外域文件全文已审**。稳定能力台账为 34 个本模块能力（31 supported、3 partial），另 1 个不计数的共享投影；supported 一律限定为 supported_static。partial 表示已审出的合同问题，不是尚未阅读。

## 反证、补充与原稿承接

当前有效反证已排除多项疑似问题：净化室中心独存时 SUMMARY 不打开、持握单成员摘要及返回游标在 WP67-B §6.2 / L14；图标 HP 周期在 WP66-C；指标尺度与已有布局刷新边界在 WP73-B；标记迁移的其它容器在 WP10。Shadow 超四原招的恢复受 S05 的过滤/保留/追加容量规则共同约束，不另以惯常四槽简写立必修。详见 [counterevidence-and-exclusions.json](counterevidence-and-exclusions.json)。

B21 的 FORM-P/FORM-N 已按精确 archive 对象 `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/static-cases.json` 跟读，支持 GIRATINA 宝珠/地图旗标/强制入口分层。B16 当前相关 UI 补充行为行已跟读。AX09/AX19 重新对 R 与 B5核实，现行合同已承接。GR3-M09-001 暂缓、GR3-M02-003 NO_REQUIRED 保持，未重开。

原稿没有发现被净化正文、附表、向量无理由丢弃的独有机制；具体行段见 [original-reconciliation.json](original-reconciliation.json)。原稿的图像泛称使用简化形态已被 B5 正确改为个体图像动态读取，属于正确替换；源行号、旧哈希、历史 PASS 和行政状态不是需要复制进当前行为正文的机制。当前候选不以历史 PASS 为证据，也不递归重审历史管理包。

## 证据边界与交付

这是静态语义完成，不是宿主、媒体、插件或 Demo 可达性认证。固定参考中未找到 MapNNN/MapInfos 或 species/shadow 编译状态文件；没有据脚本存在推断实际事件/道具获得/可选内容已启用。真实素材与原生动画内部帧行为仍未证。未来是否兼容参考异常留待独立实现阶段决策。

七项要求产物均已写入本目录：[reading-coverage.json](reading-coverage.json)、[source-to-spec.json](source-to-spec.json)、[spec-to-source.json](spec-to-source.json)、[findings.json](findings.json)、[shared-interfaces.json](shared-interfaces.json)、[progress.json](progress.json) 及本报告。规格映射逐节、条款、表行、向量索引到稳定能力和精确源锚点；`spec-to-source.json` 的 `source_anchor_ids` 在同文件 `source_anchor_index` 解析，避免重复堆积锚点。

仅写 M04 分配目录；未修改正式规格、reference、历史证据或共享报告，未提交、推送、启动 update、安装工具或改配置。全局 Feature Matrix 的合并由父会话处理，本地能力台账提供其输入。
