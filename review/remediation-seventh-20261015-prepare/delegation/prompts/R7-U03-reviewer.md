本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B=e646432c644dec04d306842cc5a559a29c718fbc，C2=4580645dfbfec4a3c7ccbad56ae293cc619b0d25，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 R7-U03，必修 GR7-M05-001, GR7-M06-001。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/R7-U03/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/R7-U03/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/R7-U03.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff/prompts/R7-U03-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。

精确写入路径（全部加 candidates/R7-U03/ 前缀；required 与 conditional 分开）：
- required: deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md
- conditional_same_record_not_automatic: deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md
- required: deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md
- required: deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md
- required: deliverables/final-specification-set/test-catalog/engine-overworld-wp16.md
- required: deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md
冲突组：CG04, CG05。无作者前置批次；接收门：Exact affected clause contribution from frozen B; shared integration by R7-I; non-author actual-result review; precise historical regressions before final CLOSED.

GR7-M05-001
{
  "前提与最小反例": "有效20×20普通地面，玩家(5,5)已朝右、(6,5)全向阻挡；无事件/through/遭遇标记、自动运动、强制/解释器/菜单/换图或竞争写。健康非蛋非Shadow队员、空合法寄养、无Safari等干扰；步数/友好计数0、Repel2，一次尝试后松方向，正常小时间差更新到碰撞完成。",
  "普通对照与正常路径": "创建时B+1、运动存在，位置/距离不变且步数0/Repel2；正常完成后仍零位移，却步数1/友好1/Repel1。通行对照在开始就位置到(6,5)、距离D+1，完成侧计数相同。",
  "取消路径": "没有新增取消接口；不再给完成机会只支持碰撞前缀。触碰成功/失败对角不建立此碰撞运动。",
  "失败路径": "一般消费者异常可在玩家链前中断；玩家链异常保留已写步数和前项效果。",
  "部分提交与保存边界": "碰撞计数创建即提交；一般消费者失败前运动可能已清。位置、距离和全局计步分开，不作事务。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "WP12分开碰撞创建与正常完成：创建不改位置/距离/离格通知；完成仍发一般步通知并可能进入玩家后处理。WP61登记该可达来源，保留强制路线、解释器、自动运动及消费者中断门。",
  "正确保留范围": [
    "不是所有失败移动/碰撞创建立即全局+1；非玩家受阻不新增此计时。",
    "保持普通移动开始写位置/距离、完成再玩家计步；WP13/MR02与WP06守卫正确。",
    "默认毒伤关闭；不主张默认中毒损伤，也不称只有所列三字段变化。空寄养仍可推进自身周期。"
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
    "碰撞返回/完成两点分别观察B、坐标/距离、全局/友好/Repel。",
    "仅前方通行对照；触碰成功及失败对角无新碰撞链。",
    "强制路线碰撞并用合法WAIT保持forcing到完成：一般通知后早退，无玩家周期/Repel推进。",
    "未完成或一般消费者失败：只断言实际前缀。"
  ]
}

GR7-M06-001
{
  "前提与最小反例": "32像素格、512×384屏、有效普通地图，无额外镜头写入。10×8小图SnapEdges真、显示(0,0)，玩家(1,1)→(2,1)正常移动，显示与图块投影仍不动。后文GR3夹具不反向补给WR01。",
  "普通对照与正常路径": "大图30×20且居中、SnapEdges假，玩家(10,8)→(11,8)，显示x320→448，图块投影差32像素。",
  "取消路径": "阻挡/未移动不是此反例，不修改移动取消规则。",
  "失败路径": "夹具排除更新/资源失败；宿主错误不代替静态坐标对照。",
  "部分提交与保存边界": "玩家坐标改变而镜头保持是正常双状态，不是部分事务或回滚。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "WR01应直接给显示坐标x实际增加128子像素（无放大、前后独立量化），或补居中跟随/无旧卷动/无钳边条件，并增加玩家右移而镜头不移的对照。",
  "正确保留范围": [
    "WP16量化/邻图/镜头时长/钳边/中心规则与GR3-CAM06–08保持。",
    "不提出新镜头算法、整文重写、像素可见或对象复用保证。"
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
    "小图右移显示0；居中大图320→448。",
    "30×20、SnapEdges真、显示x1792向右仍1792。",
    "已有手动卷动只按在途任务，不按人物位移推镜头增量。"
  ]
}

角色：独立非作者 reviewer。此 prompt 现在只发布，不立即启动。须先由 R7-I 提供冻结的 candidate-input.json，含作者真实context、候选提交/树或逐文件bytes/SHA/blob、作者证据与完整差异；缺少则报告明确依赖，不自行猜HEAD。必须是与作者不同的实际context。逐必修核完整合同、原非作者反证、固定R的源/消费者、候选正文/目录/向量、正确保留和共享贡献；对正常/取消/异常/部分提交及必要历史回归出逐ID PASS/FAIL/WAIT。写 evidence/reviewer/report.md 与 per-id.json，绑定实际输入和真实context/配置回参。候选PASS只进入待整合，不等于整合PASS、ACCEPTED或CLOSED。不以作者报告或自审代替独立内容审查。
