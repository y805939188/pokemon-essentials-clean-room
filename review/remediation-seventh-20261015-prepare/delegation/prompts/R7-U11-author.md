本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B=e646432c644dec04d306842cc5a559a29c718fbc，C2=4580645dfbfec4a3c7ccbad56ae293cc619b0d25，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 R7-U11，必修 GR7-M16-001, GR7-M17-002。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/R7-U11/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/R7-U11/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/R7-U11.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff/prompts/R7-U11-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。

精确写入路径（全部加 candidates/R7-U11/ 前缀；required 与 conditional 分开）：
- required: audit/source-traceability.md
- required: deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md
- required: deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md
- required: planning/feature-matrix.md
- conditional_same_record_not_automatic: specs/demo/wp75-project-conversion-and-authoring-tools.md
冲突组：CG01, CG03, CG07。无作者前置批次；接收门：Exact affected clause contribution from frozen B; shared integration by R7-I; non-author actual-result review; precise historical regressions before final CLOSED.

GR7-M16-001
{
  "前提与最小反例": "兼容未加密宿主到达档案唯一Main，目录可枚举、普通A.rb可读，先前文件正常且无覆盖；不是新建或启动夹具。唯一Main末尾无条件发出发现调用，因此A.rb可到读/求值请求。",
  "普通对照与正常路径": "根文件先于递归可见子目录、各自排序；普通A.rb/子B.rb有序。跳过.txt/隐藏目录不使加载入口失活。",
  "取消路径": "加载入口没有用户取消动作；不能制造确认或取消回滚门。",
  "失败路径": "发现/打开/读取可在局部求值保护之前失败；顺序处理错误不保证后续C被求值。",
  "部分提交与保存边界": "先行A的副作用可保留，后续B失败不回滚全部脚本；不承诺整个加载原子性。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "仅从WP75 §16第6项“非活动”清单移出随附脚本档案加载器，并交叉引用§12.4已有条件入口。兼容宿主达到档案唯一Main且有可枚举可读.rb时，末尾会请求发现并求值；静态可达不等于实际启动。",
  "正确保留范围": [
    "WP75 §12.4错误分阶段、900阈值、§18宿主未知与WP08文本限额保持。",
    "其它真正禁用入口、提取/合并脚本守卫和排序保持。",
    "C01的档案解码/解压/文本身份是工具验证，绝非Ruby求值、原生启动或Demo观测。"
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
    "唯一普通A.rb的条件请求；根A/子B顺序。",
    "txt/隐藏目录跳过不取消入口；A成功而B失败保留前缀且C不保证。"
  ]
}

GR7-M17-002
{
  "前提与最小反例": "兼容窗口查询/尺寸API、已到业务入口、无重复mutex且目标在本轮无外部改变。即使Script/Show Text不存在，Comment正常存在仍请求840×164/800×92；不是前一目标存在才处理后者。门不校验所有权进程，不认证本地化同义标题。",
  "普通对照与正常路径": "窗口请求标志保持位置/z序/激活，Batch按钮定位不改尺寸。每轮Sleep150只是请求，非实测精确周期。",
  "取消路径": "没有独立业务取消；标记消失时下一次检查退出并关闭有效mutex，不恢复已请求尺寸。",
  "失败路径": "目标缺席仅跳过该目标；有外框无EDIT仍请求外框、跳子框并继续其它目标。尺寸API假返回未被检查，不能据此断言中止。重复mutex返回0停止，与创建失败−1分支分开。",
  "部分提交与保存边界": "已到尺寸请求不自动恢复；没有文件写入事务，且不保证API实际执行或窗口几何。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "WP75 §14补有限静态请求表。门为类名含区分大小写Afx:且标题含RPG Maker XP的标记窗口；目标类#32770及精确英文标题，取首个EDIT。四目标独立按Script→Show Text→Comment→Batch Text Entry处理：外框/EDIT分别840×240/800×176、840×144/800×72、840×164/800×92、840×444/800×372；Batch按钮id1/id2仅定位25,392与150,392。",
  "正确保留范围": [
    "说明书提Script/Show Text为真但不完整；R6 L07运行/所有权/自动启动未知保持。",
    "Interpreter只诊断提及工具，不证明启动或修复。",
    "未来旧宿主兼容政策另选，不强制Win32/API结构。"
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
    "四目标逐个独立出现/缺席；前两缺而Comment存在。",
    "目标存在无EDIT仍外框；尺寸API返回假后继续；Batch两按钮位置而非尺寸。",
    "重复mutex与创建失败分开；标记消失无恢复，150为等待请求。"
  ]
}

角色：作者。完整读取本批七组和被接收的独立反证；用固定 B 字节建立镜像，按最小规则修正文/必要目录/向量，保留正确scope。提交 evidence/author/report.md、per-id.json、artifact-manifest.json（逐镜像固定B身份、新bytes/SHA/blob、读写集、精确变更、每向量阶段、失败/取消/部分提交、未满足依赖和配置UNVERIFIED）。不得宣称独立PASS、ACCEPTED或CLOSED。完成后停止写入，回报全部产物路径供 R7-I 固定快照。
