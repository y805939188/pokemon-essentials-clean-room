本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B=e646432c644dec04d306842cc5a559a29c718fbc，C2=4580645dfbfec4a3c7ccbad56ae293cc619b0d25，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 R7-U10，必修 GR7-M15-001, GR7-M15-002, GR7-M17-001。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/R7-U10/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/R7-U10/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/R7-U10.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff/prompts/R7-U10-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。

精确写入路径（全部加 candidates/R7-U10/ 前缀；required 与 conditional 分开）：
- required: audit/source-traceability.md
- required: deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md
- required: deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md
- required: deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md
- required: planning/feature-matrix.md
- conditional_same_record_not_automatic: specs/demo/wp74-battle-animation-authoring-and-exchange.md
冲突组：CG01, CG02, CG03, CG07。无作者前置批次；接收门：Exact affected clause contribution from frozen B; shared integration by R7-I; non-author actual-result review; precise historical regressions before final CLOSED.

GR7-M15-001
{
  "前提与最小反例": "合法物种/形态无自定义阴影；通用阴影1、2可加载且不同，3是首次缺失；正常输入/窗口/动画。初始size1/binding1、此前无确认编辑；浏览2后BACK：size恢复1、confirmed=false，绑定仍2。只判绑定身份，不判像素。",
  "普通对照与正常路径": "USE确认2不前进；ACTION确认2并前进，二者设置确认真。重新打开明确资源加载可绑定回数据对应1；已有confirmed=true时BACK仍保留true。",
  "取消路径": "BACK是本例：恢复数据而绑定可未恢复；不能说完全没有刷新，也不自动持久化预览值。",
  "失败路径": "前段资源/输入或宿主失败不在正常前提内，不保证像素、回滚或最终重画。",
  "部分提交与保存边界": "已经绑定的资源可以比恢复后的数据新；只有明确重载等实际消费者再同步，不能以数据恢复推导资源事务。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "WP73-B区分位置刷新和阴影资源选择：正常BACK可恢复大小数据/确认标志，但主菜单的位置刷新不重新绑定资源；浏览过的阴影资源可保持到下一次明确资源重载。",
  "正确保留范围": [
    "保留首次缺失即停、自定义阴影拒绝、数据/确认标志恢复、USE/ACTION及总保存门。",
    "普通坐标编辑BACK恢复位置并刷新仍正确。",
    "不要求未来永久保留旧预览副作用，不改普通战斗布局。"
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
    "size1→浏览2→BACK数据1/绑定2；不浏览BACK仍1。",
    "重新打开资源重载回1；USE与ACTION分别确认/前进。",
    "已有true标志BACK保true；坐标编辑BACK的正确恢复/刷新作对照。"
  ]
}

GR7-M15-002
{
  "前提与最小反例": "合法A0/A1/A2三条与画布/资源、无外部导航；独立例旧游标0/1/2，缩3→2后立即操作。原2被置为新长度2而非最后有效1，Load/Rename访问nil失败；Delete确认向槽2追加新条恢复长度3、无洞。",
  "普通对照与正常路径": "旧0/1缩后仍有效，Load/Rename正常，Delete只替换相应槽且长度2；先导航可重新获得有效位置。",
  "取消路径": "Delete取消不追加；列表BACK不撤销已截短的内存集合。",
  "失败路径": "Load的nil失败前可已经绑定画布/释放旧位图；不能承诺完全无可见副作用或精确宿主错误文字。",
  "部分提交与保存边界": "内存缩容已发生；磁盘需外层明确Save，失败/取消不自动回滚此前内存或保证存盘。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "仅修AN-M09测试输入：3→2后Load/Rename失败或Delete尾添的子例须明确原selected=2且后续尚未导航。加原selected0/1普通对照。WP74正文已有正确条件，不需重写。",
  "正确保留范围": [
    "保留WP74正确条件、有效删除/尾添、普通导航。",
    "R6 U07/AN007近似控制点数值facet及Float可选问题、AN002焦点观测均不同根。",
    "不把静态nil访问推成已观察宿主错误或全动画编辑器故障。"
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
    "原游标2、长度3改2后不导航：Load/Rename失败；Delete确认长度3、取消长度2。",
    "原0/1独立例正常Load/Rename/Delete长度2；先导航恢复有效。",
    "Load已到表现前缀与磁盘明确Save边界分别验证。"
  ]
}

GR7-M17-001
{
  "前提与最小反例": "首参数为存在且完整合法XML，库可给预期元素，构造/枚举前段正常；一动画两有序pattern，0路径缺失、1存在且矩形56×68，输出可写且先前调用正常。0跳过但原索引递增；1仍槽1，原点192,0，绘制目标232,28,112,136，之后可到保存请求；不是整体中止或紧凑填槽。",
  "普通对照与正常路径": "两图均存在保原序；n0最少一行，n6为960×384、槽5原点0,192；56×68在槽0目标40,28,112,136。x缺/空走整图，不消费y/w/h；负数拒绝并exit1，零可接受。",
  "取消路径": "无参数帮助等待ENTER后返回是单独门；不是业务取消/回滚。",
  "失败路径": "先完整解析全部XML，再逐动画创建图像/绘制/保存。XML缺失、指定FormatException和负数exit1；缺值/溢出/图像/保存错误分开。XML诊断含未匹配占位符，不保证普遍成功诊断或完整输出清单。",
  "部分提交与保存边界": "若动画A保存确已成功而B后失败，A可保留；无总体回滚。finally是清理请求，不能保证库清理实际成功。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "WP74 §18新增有限静态工具合同：输入门、按原序号保留缺图槽、输出尺寸/绘制/保存请求与失败阶段。宽960；n=0高192，n>0高192·ceil(n/5)。槽i原点(192(i mod5),192floor(i/5))，矩形w×h在槽内偏移(96−w,96−h)，请求双倍尺寸。只支持图像保存请求，不承诺实际PNG或RMXP动画数据。",
  "正确保留范围": [
    "五列192格与双倍居中的既有几何不是全新遗漏；≤96仅文档建议，未发现同样运行上限门。",
    "alpha分支与非alpha左上色透明请求分开，无像素/编码保证；x缺省与数字零不改成严格正数。",
    "保留.anm类型门、停用RMXP转换、关联/cache规则及R6 L06/L07库/API/编码/回滚未知。",
    "不指称历史只读身份的审阅不诚实，不新增自动导入/关联桥。"
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
    "缺0/有效1仍槽1且可到保存；两图都存在保序。",
    "n0与n6尺寸、槽0/5坐标数学对照；x缺/空忽略其它矩形属性。",
    "负/零/格式错/缺值/溢出分列；A保存成功/B错误只保已到前缀。"
  ]
}

角色：作者。完整读取本批七组和被接收的独立反证；用固定 B 字节建立镜像，按最小规则修正文/必要目录/向量，保留正确scope。提交 evidence/author/report.md、per-id.json、artifact-manifest.json（逐镜像固定B身份、新bytes/SHA/blob、读写集、精确变更、每向量阶段、失败/取消/部分提交、未满足依赖和配置UNVERIFIED）。不得宣称独立PASS、ACCEPTED或CLOSED。完成后停止写入，回报全部产物路径供 R7-I 固定快照。
