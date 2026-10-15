本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B=e646432c644dec04d306842cc5a559a29c718fbc，C2=4580645dfbfec4a3c7ccbad56ae293cc619b0d25，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 R7-U04，必修 GR7-M03-001, GR7-M03-002。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/R7-U04/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/R7-U04/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/R7-U04.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff/prompts/R7-U04-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。

精确写入路径（全部加 candidates/R7-U04/ 前缀；required 与 conditional 分开）：
- required: deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md
- required: deliverables/final-specification-set/combat-requirements/wp41-switching-positioning-and-escape.md
- required: deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md
冲突组：。无作者前置批次；接收门：Exact affected clause contribution from frozen B; shared integration by R7-I; non-author actual-result review; precise historical regressions before final CLOSED.

GR7-M03-001
{
  "前提与最小反例": "正常2v1野生战、单玩家业主、0/2已正式濒死，仍有可战斗后备P；canRun真，首席原始速度高于敌，无额外触发，场景正常。首席拒绝下一只并成功逃跑，后席仍选择P；仅采用非致死入场效果夹具。",
  "普通对照与正常路径": "首席写3后仍可提示后席；P绑定、顺序调整和派出可提交，位置治愈先于非致死危害。正常返回后本夹具仍3，EOR在外层检查处跳过尾清理。",
  "取消路径": "先前选No会启动逃跑，不能解释为撤回操作；后续必选后备选择另有自己的取消权限。",
  "失败路径": "后续显示、选择或入场异常按既有诊断边界，不保证未到步骤、恢复或最终结果必为3。",
  "部分提交与保存边界": "逃跑反馈/决定、后续替换、位置标志和HP分别在各自写点提交；不保证事务回滚。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "只细化WP41 L123的替补路径“成功结束战斗”：决定3写入后，同一替补扫描仍可能继续后席提示、选择、绑定及入场。WP42 L51/L135已有“不立即跳出嵌套调用”的正确概括应保留。",
  "正确保留范围": [
    "仅接受非致死继续扫描及状态提交；作者的危害致死后结果覆写扩张未升为独立证明。",
    "只有一个待补席时可无第二提示；入口已有正决定则早退；正常选Yes不涉及决定3。",
    "不要求未来永久复制参考异常。"
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
    "完整2v1夹具：首席No成功，后席Yes选P，观察后续绑定及非致死入场前缀。",
    "单待补席、首席改Yes、入口已有正决定为独立对照。",
    "回调失败只保留已到前缀，不要求最终3或危害致死结果。"
  ]
}

GR7-M03-002
{
  "前提与最小反例": "有效1v3：用户席0，对手查询序为3/5/1，席3既存但濒死，5与1存活且期间无变更。prefer-unfainted=true原始结果仍3；按“滤掉濒死”误读则会得到5。",
  "普通对照与正常路径": "席3活则返回3；席3缺失则跳过而返回5。将本状态直接交给以己侧席为候选的投球解析时，存活盟友兜底可按全局席序取得1，非5。",
  "取消路径": "不适用：原始查询只读无交互；后续捕获有自己独立的取消合同。",
  "失败路径": "不得推出必然无目标或普通菜单必选错；无活盟友时既有空值失败已在WP38登记，不重开。",
  "部分提交与保存边界": "查询自身不写状态；后续捕获写入/失败不由本查询新增回滚保证。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "将WP39 L190括注改为存活偏好并说明首个既存濒死对象可触发回退；附只读原始查询向量。捕获回归应断言实际补救目标，不笼统断言捕获失败。",
  "正确保留范围": [
    "保留WP38存活盟友兜底及现有无活目标失败。",
    "普通菜单显式选对侧席5直接用5，不经该己侧查询。",
    "梦话、变身者和换人消息用false/默认；WP47-A有自己的构造/回退，不泛化为所有目标族。"
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
    "[3,5,1]首3濒死：原始true查询3；3缺失对照5；3存活对照3。",
    "直接捕获解析的条件对照恢复到席1；显式席5入口保持席5。",
    "无活盟友只沿WP38既有失败，不新增必修。"
  ]
}

角色：作者。完整读取本批七组和被接收的独立反证；用固定 B 字节建立镜像，按最小规则修正文/必要目录/向量，保留正确scope。提交 evidence/author/report.md、per-id.json、artifact-manifest.json（逐镜像固定B身份、新bytes/SHA/blob、读写集、精确变更、每向量阶段、失败/取消/部分提交、未满足依赖和配置UNVERIFIED）。不得宣称独立PASS、ACCEPTED或CLOSED。完成后停止写入，回报全部产物路径供 R7-I 固定快照。
