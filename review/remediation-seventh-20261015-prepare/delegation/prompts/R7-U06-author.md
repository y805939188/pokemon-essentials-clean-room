本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B=e646432c644dec04d306842cc5a559a29c718fbc，C2=4580645dfbfec4a3c7ccbad56ae293cc619b0d25，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 R7-U06，必修 GR7-M09-001, GR7-M10-001。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/R7-U06/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/R7-U06/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/R7-U06.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff/prompts/R7-U06-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。

精确写入路径（全部加 candidates/R7-U06/ 前缀；required 与 conditional 分开）：
- required: deliverables/final-specification-set/combat-requirements/wp49-ability-phase-triggers.md
- conditional_same_record_not_automatic: deliverables/final-specification-set/pokemon-rules/wp43-types-accuracy-and-damage.md
- required: deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md
- required: deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md
- required: deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md
冲突组：。无作者前置批次；接收门：Exact affected clause contribution from frozen B; shared integration by R7-I; non-author actual-result review; precise historical regressions before final CLOSED.

GR7-M09-001
{
  "前提与最小反例": "当前代、合法槽/正PP、普通单目标且所有前门通过，无替身/模式破坏者；双方全程存活且无睡冻/换人/反应/物品/重入/插件/宿主失败。SNEASEL围攻的合格业主段恰[SNEASEL基础攻95,MAGIKARP基础攻10]，MIMIKYU0画皮：计划2，首击吸收C1且直接损0，不消费；第二击首次基底14，非6。",
  "普通对照与正常路径": "目标起始已破皮形态1时基底14再6；三连踢P10对EISCUE0：首吸收后基底10/20，成功击3；形态1为10/20/30。后续攻防可随形态变，不固定最终伤害。",
  "取消路径": "本族执行后没有UI取消；上游取消不建立本次使用。",
  "失败路径": "失手在该击求值前停止；吸收不是失败重试。独立濒死/睡冻/目标倒下停止门仍生效，不保证后击完成。",
  "部分提交与保存边界": "已到吸收/形态/HP/PP前缀保留；后续反应或宿主失败不回滚，不补后击。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "WP46围攻将参与者消费绑定实际普通基底求值，不绑每个成功击。形态吸收可占计划/成功击而不推进有状态基底；无吸收序列保持。三连踢已有每次求值加P的措辞，仅其序号例若保留应限定三个基底求值。",
  "正确保留范围": [
    "WP43 L113–119的C1早返已正确，不能写成整个伤害核心遗漏。",
    "三连踢L54已写求值触发，不改成完全缺失。",
    "替身仍进行普通求值推进，不混同形态吸收或固定伤害。",
    "基底14/6/10/20不是最终伤害/实际HP损失；不改AI、身份计数、计划/成功击数、资格或攻防。"
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
    "围攻吸收/已破皮对照：第二基底14与普通14/6。",
    "三连踢吸收/无吸收：后续10/20与10/20/30，命中规则独立。",
    "替身推进对照；首失手与吸收后各独立停止门只保留已到前缀。"
  ]
}

GR7-M10-001
{
  "前提与最小反例": "默认合法WATERGUN打存活默认ROLYCOLY，当前普通有效STEAMENGINE、速度阶级0，无替身/无效和中间改写，先前门/表现正常；当前PP5合法而非总PP改5。到直接尾部请求+6，原速度35不改，后继普通速度可读140。",
  "普通对照与正常路径": "先前PP/伤害保持，再经中央请求升阶；同水命中换HEATPROOF无此速度反应。",
  "取消路径": "更早取消/失败/无效不到此反应，不补PP退款。",
  "失败路径": "有效性、替身和非零计算伤害是独立门；不是新加正真实肉身HP损失门。",
  "部分提交与保存边界": "只保留已到PP/HP/阶级；后段反馈失败不保证回滚或宿主恢复。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "在WP49补具名直接每击规则并由WP46正确时序交叉引用：本次计算类型火/水，对实际目标集合排除unaffected、calcDamage0、替身，要求当下普通有效STEAMENGINE并经中央可升资格请求速度+6。位置在附效/畏缩/减伤果消费后、后续濒死检查前；此处没有独立模式破坏者或强行屏蔽门。",
  "正确保留范围": [
    "请求+6不是赋绝对+6：-4→+2，+5→+6，+6不再升。",
    "当前单一能力快照不构造同时蒸汽机/唱反调/单纯夹具。",
    "普通有效性/濒死/压制及夹限保持；48族267对、WP48的27族148对计数不变。",
    "AI评级/孵化角色、动态OnBeingHit和更早每击时序不改。"
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
    "火和水分别触发；其它计算类型不触发，改计算类型作门对照。",
    "替身、unaffected、calcDamage0、压制、失能各自拒绝。",
    "阶级-4/0/+5/+6→+2/+6/+6/不升；两次合法火水逐击重查。",
    "模式破坏者真及合法强行火水各自不统一屏蔽此尾部；错误只保留已到前缀。"
  ]
}

角色：作者。完整读取本批七组和被接收的独立反证；用固定 B 字节建立镜像，按最小规则修正文/必要目录/向量，保留正确scope。提交 evidence/author/report.md、per-id.json、artifact-manifest.json（逐镜像固定B身份、新bytes/SHA/blob、读写集、精确变更、每向量阶段、失败/取消/部分提交、未满足依赖和配置UNVERIFIED）。不得宣称独立PASS、ACCEPTED或CLOSED。完成后停止写入，回报全部产物路径供 R7-I 固定快照。
