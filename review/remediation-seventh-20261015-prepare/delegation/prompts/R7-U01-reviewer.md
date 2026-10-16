本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B=e646432c644dec04d306842cc5a559a29c718fbc，C2=4580645dfbfec4a3c7ccbad56ae293cc619b0d25，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 R7-U01，必修 GR7-M01-001, GR7-J01-001。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/R7-U01/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/R7-U01/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/R7-U01.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff/prompts/R7-U01-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。

精确写入路径（全部加 candidates/R7-U01/ 前缀；required 与 conditional 分开）：
- required: audit/source-traceability.md
- conditional_same_record_not_automatic: deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md
- conditional_same_record_not_automatic: deliverables/final-specification-set/engine-overworld/wp14-random-dungeons.md
- required: deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md
- required: deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md
- conditional_same_record_not_automatic: deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md
- conditional_same_record_not_automatic: deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md
- required: deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md
- required: deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md
- required: planning/feature-matrix.md
冲突组：CG01, CG02, CG03, CG04, CG07。无作者前置批次；接收门：Exact affected clause contribution from frozen B; shared integration by R7-I; non-author actual-result review; precise historical regressions before final CLOSED.

GR7-M01-001
{
  "前提与最小反例": "合法TownMap身份1已登记、无相等覆写和另加数值序号。按1严格查找成功，但该记录与整数1比较正常返回假；同类主身份1记录之间相等。TerrainTag Grass的数值序号2与整数2比较为真。",
  "普通对照与正常路径": "查找成功与比较假可以同时成立；普通同类与双身份对照保持。",
  "取消路径": "不适用：此处是无交互的只读比较，没有取消操作。",
  "失败路径": "比较假是正常布尔结果；不扩为未知身份、查询类型错误或登记失败。",
  "部分提交与保存边界": "不适用：比较本身没有写入，不产生提交或回滚。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "仅将“按整数序号比较”限定到确有另一数值序号的记录。五种仅以整数为主身份的内容，其整数键查找与记录对整数比较应分别描述；符号、字符串、同类记录比较和既有查询覆写保持。",
  "正确保留范围": [
    "独立最小实例是TownMap；声明证据支持Metadata、PlayerMetadata、MapMetadata、DungeonTileset同样继承边界。",
    "不得推成所有整数查找失败、同类比较失败或普通游戏消费者必定使用该比较。",
    "EXPSHARE物品对象与对应符号相等的正确反证保留。"
  ],
  "禁止扩大": "本中文视图不得复活已被反证排除的普通游戏故障、统一事务、宿主成功或未来架构强制。"
}
{
  "验收条件": [
    "正文、目录及必要同步只陈述本记录最小行为合同，所有保留范围均不变。",
    "按下列具名前提/普通对照/取消/失败/部分提交分别核验；执行阶段按第七组真实证据标记。",
    "后续实际变更须由非作者核验，根接受中文视图不等于已经修订或关闭。"
  ],
  "回归向量与可判观察点": [
    "TownMap：查找1成功、记录对整数1为假、同类同身份为真。",
    "TerrainTag：Grass序号2对整数2为真。",
    "分别核查五类声明，不将查找覆写混入相等合同。"
  ]
}

GR7-J01-001
{
  "前提与最小反例": "固定B/R且schema/登记/查询无扩展覆写，输入可读且早期调用正常。Metrics/Shadow首分量须已在Species登记；Shadow可选输入在本夹具启用，不以顶层缺席假定默认启用；正形态号不额外假定同号形态必存在。先[cave_1]后[cave,1]合法条目别名到同一登记身份，第二节以区域cave/版本1重复拒绝；反序诊断区域cave_1/版本0。",
  "普通对照与正常路径": "仅[cave]6×4可query(cave,0)得6×4；[cave]5×4与[cave,1]6×4正常共存、query2回基础5×4。[cave_1]单独登记元数据区域cave_1/版本0，query(cave,1)亦命中6×4。[cave]5×4和[cave_0]6×4共存时query(cave,0)先得6×4。",
  "取消路径": "PBS编译本身无交互取消。独立指标编辑器No正常重载档案；Yes先档案后PBS，后PBS失败不自动撤销先存档案。",
  "失败路径": "显式[cave,0]/[RATTATA,0]在转换前拒绝；未知Species拒绝。Metrics/Shadow先[RATTATA_1]后[RATTATA,1]各独立复位时第二节经通用门拒绝，第一节内存保留。",
  "部分提交与保存边界": "失败条目未登记、终检/本表save未到。直接编译旧dat可能仍在且其它表先存档可保留；启动预删除/诊断后删除只是尝试，Reset/SystemExit原样重抛。没有统一事务/全磁盘删除。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "给DungeonParameters、SpeciesMetrics、ShadowPokemon三类外部节头补接受域/省略位/身份等价关系：次位可选正整数，省略或空位语义0，显式0拒绝。用合法向量规定别名后的查询和第二节拒绝，不规定未来符号/下划线/类结构；若不保留别名兼容，需具名差异政策。",
  "正确保留范围": [
    "仅三类复合节头；DungeonTileset单整数7/23正常共存、重复7通用拒绝，必须先满足各一合法Autotile/Tile完整组。",
    "直接register覆盖与PBS转换后拒绝是不同入口。",
    "Metrics正形态query门与Shadow/地牢所有整数先试复合查询分开；默认字段、惰性克隆/后缀/PBS路径保持。",
    "不宣称默认Shadow/普通游戏故障、缓存刷新、字节往返、真实画面或Demo可达。"
  ],
  "禁止扩大": "本中文视图不得复活已被反证排除的普通游戏故障、统一事务、宿主成功或未来架构强制。"
}
{
  "验收条件": [
    "正文、目录及必要同步只陈述本记录最小行为合同，所有保留范围均不变。",
    "按下列具名前提/普通对照/取消/失败/部分提交分别核验；执行阶段按第七组真实证据标记。",
    "后续实际变更须由非作者核验，根接受中文视图不等于已经修订或关闭。"
  ],
  "回归向量与可判观察点": [
    "完整J01-V01–V13逐项保留：省略0、正数、不冲突、显式0/未知Species拒绝、外部别名、重复诊断及save前缀。",
    "Species已登记RATTATA与RATTATA_1时，Metrics仅[RATTATA_1]的BackSprite7,8由query(RATTATA,1)命中且不克隆；query0走基础门。",
    "同Species前提启用Shadow、GaugeSize5000由query(RATTATA,1)消费5000而非缺记录默认4000。",
    "三个生产者与Tileset正常对照、编辑器No/Yes和直接/启动失败前缀独立。"
  ]
}

角色：独立非作者 reviewer。此 prompt 现在只发布，不立即启动。须先由 R7-I 提供冻结的 candidate-input.json，含作者真实context、候选提交/树或逐文件bytes/SHA/blob、作者证据与完整差异；缺少则报告明确依赖，不自行猜HEAD。必须是与作者不同的实际context。逐必修核完整合同、原非作者反证、固定R的源/消费者、候选正文/目录/向量、正确保留和共享贡献；对正常/取消/异常/部分提交及必要历史回归出逐ID PASS/FAIL/WAIT。写 evidence/reviewer/report.md 与 per-id.json，绑定实际输入和真实context/配置回参。候选PASS只进入待整合，不等于整合PASS、ACCEPTED或CLOSED。不以作者报告或自审代替独立内容审查。
