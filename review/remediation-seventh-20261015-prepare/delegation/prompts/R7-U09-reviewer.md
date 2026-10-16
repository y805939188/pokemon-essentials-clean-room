本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B=e646432c644dec04d306842cc5a559a29c718fbc，C2=4580645dfbfec4a3c7ccbad56ae293cc619b0d25，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 R7-U09，必修 GR7-M14-001, GR7-M14-002。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/R7-U09/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/R7-U09/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/R7-U09.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff/prompts/R7-U09-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。

精确写入路径（全部加 candidates/R7-U09/ 前缀；required 与 conditional 分开）：
- required: deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md
- required: deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md
- required: deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md
冲突组：CG05。无作者前置批次；接收门：Exact affected clause contribution from frozen B; shared integration by R7-I; non-author actual-result review; precise historical regressions before final CLOSED.

GR7-M14-001
{
  "前提与最小反例": "默认两地区表、合法已见已拥有CHIKORITA非蛋、有图鉴；USE_CURRENT_REGION=false，保存视图-1、全国已解锁、无偏移；地图/资源正常。-1是普通菜单能产生的合法值。从摘要View Dex进入完整单条前写最近见形态。直接负索引取最后地区表，CHIKORITA编号001；摘要/简略全国编号152。",
  "普通对照与正常路径": "保存视图0而不在表中时???，视图1为001；当前地区设置true且地区1有效时001。偏移只含-1时000，只含1仍001，不能按后解析出的地区1套偏移。",
  "取消路径": "未选View Dex时没有这次最近见写入；已打开后BACK不撤销已写最近见形态。",
  "失败路径": "后续启动/资源失败只保留到达前缀，不能保证画面或完整返回。",
  "部分提交与保存边界": "只涉及编号显示、选中图鉴和最近见形态；不增加经验、拥有、捕获或击倒计数。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "WP62应单列完整单条图鉴的编号消费：按当前地区设置或已保存视图取编号集合；先编号查询，负地图解析为当前地区时不重算编号；缺/不属于该集合为0并显示???。偏移按选定视图值判断。摘要、简略图鉴和主列表的既有各自规则保持。",
  "正确保留范围": [
    "PD25/R4-PD02既有摘要全国/首个解锁即停、简略全国/继续查找、主列表编号保持。",
    "不能把负索引差异写成所有图鉴编号错误；未来是否保持该兼容差异另决。",
    "普通资源请求不等于像素观测。"
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
    "CHIKORITA：视图-1完整001，对照摘要/简略152；视图0???、1为001。",
    "偏移键-1与1分例；当前地区设置true/false独立。",
    "View前取消/打开后BACK、后续资源错误分别检查最近见写入前缀。"
  ]
}

GR7-M14-002
{
  "前提与最小反例": "合法BULBASAUR0雄性，静默入队see_form=false已拥有但未见，健康且无其它动态入场形态/幻觉/变身/插件；后续实际内部战斗玩家首次出场，peer/scene/指令重置前段正常。共同入口无阵营过滤：seen和雄性form0变真，空last_seen变[0,0,false]。",
  "普通对照与正常路径": "已见重复登记幂等；已有last_seen=[0,0,true]保留；实际替换/伙伴出场同门。owned已真，捕获/击倒计数不变。",
  "取消路径": "实际出场前取消选择不登记；未出场后备不登记；非内部包装本入口不登记，其它独立形态提交另列。",
  "失败路径": "scene/重置等前段失败可阻止写；写后刷新失败可保留seen/form/last前缀。",
  "部分提交与保存边界": "不把登记和显示合成事务，也不新增owned或捕获计数。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "把WP62 §3.1实际出场登记入口写为内部战斗中所有实际传入的出场者，包括玩家、伙伴和对手；以battle player为接收者，保存显示形态。不能延伸为所有后备成员或所有濒死/捕获消费者。",
  "正确保留范围": [
    "PD24静默入队只拥有的独立入口仍正确。",
    "对手专属濒死调用及捕获计数门不改；并非所有战斗外层无条件登记。",
    "记录/地区可达性仍取决各自配置与既有能力门。"
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
    "owned-only首次己方实际出场后seen/form/空last；非空last保留。",
    "实际替换和伙伴出场；未出场后备、选择取消、非内部包装均为独立负对照。",
    "前门失败与写后刷新失败分别核前缀；PD24入队对照保持。"
  ]
}

角色：独立非作者 reviewer。此 prompt 现在只发布，不立即启动。须先由 R7-I 提供冻结的 candidate-input.json，含作者真实context、候选提交/树或逐文件bytes/SHA/blob、作者证据与完整差异；缺少则报告明确依赖，不自行猜HEAD。必须是与作者不同的实际context。逐必修核完整合同、原非作者反证、固定R的源/消费者、候选正文/目录/向量、正确保留和共享贡献；对正常/取消/异常/部分提交及必要历史回归出逐ID PASS/FAIL/WAIT。写 evidence/reviewer/report.md 与 per-id.json，绑定实际输入和真实context/配置回参。候选PASS只进入待整合，不等于整合PASS、ACCEPTED或CLOSED。不以作者报告或自审代替独立内容审查。
