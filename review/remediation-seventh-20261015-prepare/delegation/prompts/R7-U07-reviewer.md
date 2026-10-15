本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B=e646432c644dec04d306842cc5a559a29c718fbc，C2=4580645dfbfec4a3c7ccbad56ae293cc619b0d25，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 R7-U07，必修 GR7-M12-001。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/R7-U07/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/R7-U07/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/R7-U07.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff/prompts/R7-U07-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。

精确写入路径（全部加 candidates/R7-U07/ 前缀；required 与 conditional 分开）：
- required: deliverables/final-specification-set/combat-requirements/wp55-facility-session-and-restoration.md
- required: deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md
冲突组：。无作者前置批次；接收门：Exact affected clause contribution from frozen B; shared integration by R7-I; non-author actual-result review; precise historical regressions before final CLOSED.

GR7-M12-001
{
  "前提与最小反例": "受控直接工具边界：合法训练家0及文本，候选[]、模板[]、建议3；有效受伤非空玩家队伍、Tower、明确无等级调整且非debug跳过；先前场景正常。不声称默认Demo/PBS产生此输入。",
  "普通对照与正常路径": "候选[0,1]/两合法模板按原序返回2，不补齐或最终队伍校验；[]零次创建返回空NPC。",
  "取消路径": "入口UI的nil取消另分，debug跳过排除在主例之外。",
  "失败路径": "[0]/[]在个体创建时失败，未到治疗；[]/[]包装先治疗，再在记录战斗继承构造的空对手门失败。",
  "部分提交与保存边界": "玩家治疗已提交；旧临时战斗记录可能仍在，正常恢复/末尾清记录/胜负统计未到。本无等级调整夹具返回nil经验记录，不能带回“已存经验数组”。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "把“缺模板时个体创建失败”限定到实际尝试了该缺失条目。补零候选返回空对手；在明列正常包装/无等级调整依赖下，玩家治疗先提交，稍后构造才拒空对手。不补统一回退或要求修源。",
  "正确保留范围": [
    "长度1/2不补齐/不最终校验的正确规则与WS-W31保持。",
    "空训练家表/非整数随机入口、工厂生成与WP76估计/作者生成器分开。",
    "不承诺默认普通Demo受阻或未来必须采用治疗后拒绝策略。"
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
    "[]/[]：空NPC→治疗→构造拒；[0]/[]：创建失败、未治疗。",
    "[0,1]/有效模板保原序2；无等级调整经验记录nil、对手物品表空。",
    "debug跳过提前true并清临时记录，不是主例；早构造失败不补正常恢复和统计。"
  ]
}

角色：独立非作者 reviewer。此 prompt 现在只发布，不立即启动。须先由 R7-I 提供冻结的 candidate-input.json，含作者真实context、候选提交/树或逐文件bytes/SHA/blob、作者证据与完整差异；缺少则报告明确依赖，不自行猜HEAD。必须是与作者不同的实际context。逐必修核完整合同、原非作者反证、固定R的源/消费者、候选正文/目录/向量、正确保留和共享贡献；对正常/取消/异常/部分提交及必要历史回归出逐ID PASS/FAIL/WAIT。写 evidence/reviewer/report.md 与 per-id.json，绑定实际输入和真实context/配置回参。候选PASS只进入待整合，不等于整合PASS、ACCEPTED或CLOSED。不以作者报告或自审代替独立内容审查。
