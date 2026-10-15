本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B=e646432c644dec04d306842cc5a559a29c718fbc，C2=4580645dfbfec4a3c7ccbad56ae293cc619b0d25，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 R7-U08，必修 GR7-M13-001, GR7-J16-001, GR7-J16-002, GR7-J16-003。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/R7-U08/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/R7-U08/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/R7-U08.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff/prompts/R7-U08-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。

精确写入路径（全部加 candidates/R7-U08/ 前缀；required 与 conditional 分开）：
- required: deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md
- required: deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md
- required: deliverables/final-specification-set/user-interface/wp67-b-lifecycle-presentations-and-history.md
冲突组：CG06。无作者前置批次；接收门：Exact affected clause contribution from frozen B; shared integration by R7-I; non-author actual-result review; precise historical regressions before final CLOSED.

GR7-M13-001
{
  "前提与最小反例": "合法非蛋战斗数据框、T101、实际HP51→50，正常交互战斗且无中止/覆写/中间变更；给定动画经过0.5秒，只判请求颜色。此时h50.5，参考请求绿，精确二分阈值会错误请求黄。",
  "普通对照与正常路径": "实际HP先提交；动画持有浮点显示值，终点回到目标整数。T100时50黄、25红；T101静态51绿/50黄/26黄/25红保持。",
  "取消路径": "本颜色组件没有独立取消动作；外层BACK是另一入口，不据此撤销实际HP。",
  "失败路径": "先前资源、数字、时间或宿主失败可能阻断绘制；未认证最终像素、真实帧时钟或恢复。",
  "部分提交与保存边界": "领域HP可已提交；后续表现失败不自动回滚，不保证补画。",
  "负证据边界": "按原实际独立裁决的有限已读范围接收；全文检索只算定位。原作者较宽负证据保留为证据，不自动升级。"
}
{
  "最小行为合同": "WP67-A的颜色请求应以动画当下显示HP h和总HP T判断：h≤floor(T/4)为红，否则h≤floor(T/2)为黄，其余绿。不能先把h取整，不能用最终HP或精确分数阈值替代。",
  "正确保留范围": [
    "不把数字显示的临时整数用于颜色；数字显示开关与颜色独立。",
    "保留约1秒等待、EffectsOff仍进行HP动画、宽度比例及偶数取整；队伍/摘要条和图标不随本项改。",
    "本次接受的是静态数值与颜色请求，不继承B17/U05/R4的全局PASS。"
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
    "T101：51→50在t0.5/1分别h50.5绿、50黄。",
    "T101：26→25在t0.75/1分别h25.25黄、25红。",
    "T100与T101整数边界、数字显示开/关、EffectsOff各作独立对照。"
  ]
}

GR7-J16-001
{
  "精确主张与层级": {
    "formal": "WP67-B L141“记录写入（先于演出）”；L17演出包括音效/音乐，L143演出序列首项为BGM。",
    "source": "Hall L67–74为基础显示准备、非空音乐请求、记录登记、成员建立及淡入；L120–131为克隆/追加/编号/裁剪；L436–440包装在之后才进入动画循环。",
    "layer": "逻辑BGM请求；不认证底层Audio调用必达、实际发声、像素、Demo可达或落盘。"
  },
  "完整前提": {
    "entry": "直接普通登记包装；不是PC浏览。",
    "state": "显式历史[]/累计编号0；一名有效非蛋健康Pikachu，默认音乐非空、上限50、ALLOW_EGGS真；无插件/竞争修改。",
    "dependencies": "基础画面构造与物种登记查询正常；观察外层逻辑BGM请求刚被交付时。登记正常对照还要求该请求、克隆和后续构造正常返回。",
    "observer": "同一历史数组内容和累计编号；补观察请求参数。"
  },
  "普通对照": "空音乐配置：该音乐请求不存在；登记仍先于成员滑入。非空音乐正常返回：请求边界[]/0，之后追加一届/编号1，再进入视觉链。",
  "最小反例": "保持普通有效夹具，只观察第一次逻辑BGM请求入口：历史仍[]、编号仍0。若照L141+L143字面把登记放在BGM之前，观察值会是一届/1；无需注入错误即可区分。",
  "正常_取消_拒绝_失败_部分提交": {
    "normal": "基础显示准备→非空BGM逻辑请求→克隆/追加/编号/裁剪→成员建立与淡入→动画循环。",
    "cancellation": "登记段无玩家取消分支；PC BACK不是登记取消。",
    "rejection": "空/无音乐只跳过请求，不拒绝记录；基本资源前置失败属于异常。",
    "failure": "若BGM请求内发生未返回的异常，登记尚未调用；不承诺消息窗口、宿主退出、恢复或清理。",
    "partial_commit": "此前显示资源可能已建立，音频消费者可已更改自己的播放请求状态；不推登记已提交，也不推自动保存/回滚。"
  },
  "必要消费者": [
    "Hall L178–211成员建立、L310–318/L347–401动画推进，确认视觉链在登记之后。",
    "Audio_Play L52–68解析/分派；Game_System L44–83保留逻辑播放状态并按资源/默认音乐决定是否向Audio交付。因此只裁最外层请求先后。",
    "Hall L471–478历史与编号查询以及L452–460 PC消费者保持各自门。"
  ],
  "有限负证据": {
    "receipts": [
      "017-hall-source-full",
      "020-consumer-locator",
      "021-audio-wrapper",
      "022-audio-consumer",
      "044-history-index-corrected",
      "053-history-known-roots-locator"
    ],
    "scope": "完整Hall定义/包装/PC独立入口及已定位音频消费者；本轮所有tasks/*/findings.json的相关标题定位。",
    "result": "没有在该入口中找到把保存移到BGM之前的旁路；本轮标题定位未发现另一个同提案。非穷尽历史/动态插件证明。"
  },
  "原始独立反证": {
    "file": "inputs/delta-j16/tasks/R7-C14/counter-review.json",
    "json_pointer": "/decisions/0",
    "file_bytes": 27323,
    "file_sha256": "f912ce3080054f9f436d516b3ae00154f7ecbd94c116a29a40111ce23eb5a5e2"
  },
  "原始作者载荷": {
    "file": "inputs/delta-j16/evidence/received-final-proposals/GR7-J16-001/proposal.json",
    "json_pointer": "/new_proposed/0",
    "file_bytes": 91439,
    "file_sha256": "9740561fe394a49c1a4529369975573b1e71e01ccd0c3dc80a63d29b3f393b6f"
  }
}
{
  "最低合同": "最低必要修订为WP67-B L141的一句顺序限定。全文§2把音乐纳入演出，§7.1又把BGM列为演出首项，因此“先于演出”不能在未说明的情况下改读成“先于逐成员视觉”。该句与非空音乐的静态请求次序相反。",
  "精确必修级别": "MAIN_TEXT_ORDER_WORDING_ONLY",
  "必须保留": [
    "克隆和默认蛋收录",
    "正/负/0上限及每次只删一届",
    "累计编号不回退与PC门",
    "无取消、无自动保存/片尾",
    "记录先于视觉滑入",
    "实际媒体/宿主未知"
  ],
  "排除写集": [
    "L22等正确向量无需改写；不要求新增全局测试ID。",
    "reference/**；WP23；WP67-A；旧报告、旧资格、公共台账。"
  ],
  "未来政策": "无需决定未来是否修复参考；这是文字顺序校正，不要求未来重现宿主错误。",
  "不扩张": "不以中文翻译升级RGBA或新增净化规则；原作者错误经验driver只保留原字节，由C14真实283–293取代支持定位。"
}
{
  "全组具名向量": [
    {
      "id": "C14-HOF-A",
      "given": "非空音乐、初始[]/0，观察首逻辑BGM请求入口",
      "expected": "历史[]/编号0；未登记",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-HOF-B",
      "given": "同一请求正常返回，登记正常完成",
      "expected": "克隆一届/编号1，再视觉成员链",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-HOF-C",
      "given": "独立空音乐配置",
      "expected": "无该请求；仍可登记并先于视觉链",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-HOF-D",
      "given": "条件化请求内异常且不返回",
      "expected": "未到登记；此前资源/音频侧状态不承诺回滚或清理",
      "execution": "NOT_EXECUTED"
    }
  ],
  "限定": "原全部向量NOT_EXECUTED；验收只覆盖最低文字/测试前提及正确保留范围，后续实际更改另由非作者核验。"
}

GR7-J16-002
{
  "精确主张与层级": {
    "formal": "WP67-A L196/L248均为满槽0.2秒“闪白”；K22/K35没有白色断言。",
    "source": "数据框L350–386首次达到满槽时，在音效请求之后对本框与未释放子精灵交付RGBA=(64,200,248,192)，时长参数为0.2×帧率；后续计时到期清动画。",
    "layer": "静态闪光颜色/时长请求，与宿主混色/资源遮盖/真实像素分开。"
  },
  "完整前提": {
    "entry": "普通交互战斗中玩家侧单席位数据框经验动画；已建立可见经验条。",
    "state": "有效非蛋Pikachu L10，Medium区间1000至1331，实际经验已写1331；显示经验从1000推进到1331，正区间331且有变化；无已有满槽闪光起点。",
    "dependencies": "对象/资源/时钟/消息/SE正常返回，无外部中止、插件覆写或同时闪光；只观察flash请求交付。",
    "observer": "本数据框及其未释放子精灵收到的RGBA和名义时长参数。"
  },
  "普通对照": "相同框只增到1100：到非满段后结束经验动画，没有满槽闪光；多席位或对方框无经验条，动画入口直接返回。满槽正常仍保留1.75秒比例目标、0.2秒等待与音效。",
  "最小反例": "玩家单席位331/331满槽首次更新：首闪光请求RGB为64/200/248而不是白色RGB。此差异只在请求层成立，不用最终像素作反例。",
  "正常_取消_拒绝_失败_部分提交": {
    "normal": "实际经验先提交→经验条补间及刷新→首次满槽设闪光计时起点→停止旧SE并请求满槽SE→本框闪光请求→逐个未释放子精灵请求→以后更新到期才清动画。",
    "cancellation": "该组件无玩家取消；可中止战斗BACK是独立外层路径，本夹具排除。",
    "rejection": "无条、无变化或区间0不启动；无战斗者/无区间的场景入口可直接返回。",
    "failure": "SE或前序操作失败可在首闪光前中断；本框或某个子精灵已收请求后失败不保证其余子精灵收到。",
    "partial_commit": "实际经验与已推进显示值不因呈现错误自动回滚；不承诺所有请求、最终像素、宿主退出或恢复。"
  },
  "必要消费者": [
    "Battle_ExpAndMoveLearning L162–224，实际经验L194先写，L195才交场景。",
    "Scene_PlayAnimations实际经验驱动为L283–293；J16七组所列S4 L234–254是伤害动画，不能用作经验驱动证据，本任务已独立更正定位。",
    "Battle_Scene L79–119更新数据框；DataBox L191–204启动门及L403–413更新；lerp L394–406支持到端判断。"
  ],
  "有限负证据": {
    "receipts": [
      "018-data-box-source-a",
      "019-data-box-source-b",
      "020-consumer-locator",
      "025-exp-callers-locator",
      "026-exp-real-driver",
      "027-exp-domain-commit",
      "028-lerp-consumer"
    ],
    "scope": "数据框完整类1–413、场景驱动、领域调用及Data/Scripts相关flash/经验入口定位。",
    "result": "该满槽分支没有改成白色的本地参数转换；没有读取或运行native像素混合，不据此推全部动态覆写不存在。"
  },
  "原始独立反证": {
    "file": "inputs/delta-j16/tasks/R7-C14/counter-review.json",
    "json_pointer": "/decisions/1",
    "file_bytes": 27323,
    "file_sha256": "f912ce3080054f9f436d516b3ae00154f7ecbd94c116a29a40111ce23eb5a5e2"
  },
  "原始作者载荷": {
    "file": "inputs/delta-j16/evidence/received-final-proposals/GR7-J16-002/proposal.json",
    "json_pointer": "/new_proposed/1",
    "file_bytes": 91439,
    "file_sha256": "9740561fe394a49c1a4529369975573b1e71e01ccd0c3dc80a63d29b3f393b6f"
  }
}
{
  "最低合同": "最低必要修订是WP67-A L196和L248去掉不受支持的白色断言（改为“0.2秒闪光”即可）。可选再登记蓝青色RGBA请求，但不能要求白色或蓝青色最终像素。",
  "精确必修级别": "TWO_LOCAL_COLOR_WORDS_ONLY",
  "必须保留": [
    "1.75秒比例与满槽名义0.2秒",
    "经验先提交和逐级顺序",
    "满槽音效/等待门",
    "无条立即完成",
    "动画开关Off仍播放",
    "像素/素材/宿主未知"
  ],
  "排除写集": [
    "不改K22/K35、不新增强制像素断言。",
    "reference/**、经验公式/成长/学招/HP颜色规则、旧资格及公共台账。"
  ],
  "未来政策": "没有新增未来兼容政策；最低修订只是撤回无证白色断言。",
  "不扩张": "不以中文翻译升级RGBA或新增净化规则；原作者错误经验driver只保留原字节，由C14真实283–293取代支持定位。"
}
{
  "全组具名向量": [
    {
      "id": "C14-EXP-A",
      "given": "玩家单席位，从区间0/331到331/331，前序正常",
      "expected": "本框及正常未释放子精灵收到RGBA64/200/248/192及名义.2秒请求；不认证像素",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-EXP-B",
      "given": "同框只到100/331",
      "expected": "无满槽闪光；原增益声音与结束门保持",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-EXP-C",
      "given": "多席位或对方无条",
      "expected": "经验动画立即完成，无满槽请求",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-EXP-D",
      "given": "满槽SE或某个闪光请求内条件化失败",
      "expected": "只保留已提交经验/已交付前缀，不保证所有子精灵或统一恢复",
      "execution": "NOT_EXECUTED"
    }
  ],
  "限定": "原全部向量NOT_EXECUTED；验收只覆盖最低文字/测试前提及正确保留范围，后续实际更改另由非作者核验。"
}

GR7-J16-003
{
  "精确主张与层级": {
    "formal": "UI catalog L440 LC-L13给存在合格组即全链；L443/L444正确分默认跨级失败与同级/遗迹石，WP67-B L125–128已正确。",
    "source": "PurifyChamberScreen L570–603调用统一净化后才存放/清中心，且只有列表尚有下一项才询问。统一净化L17–58经跨级辅助后才精确写回经验；成长窗口L206–221在确认键前先调用包装更新。",
    "layer": "静态控制可达与内存部分提交；不是新缺方法根因、不是宿主错误界面或Demo自然生成链。"
  },
  "完整前提": {
    "entry": "默认净化室包装，见过标志先写；存在且仅有一合格非Lugia组。",
    "state": "中心健康合法非蛋Pikachu L10/E1000、Shadow真、Hyper假、G0、S500、有效六项V0和合法已知招/首招；一个普通有效外圈，其他组空；队伍/盒有容量。",
    "dependencies": "源定义无插件补更新操作，无竞争修改；前序资源/消息/EV/招式/统计正常；不用真实存档。",
    "legality": "Pikachu为Medium；L10=1000/L11=1331。恢复floor(4×500/5)=400，目标1400属L11。这是合法已保存状态入口夹具，不证明默认Demo内容自然产生。",
    "observer": "首能力窗口的更新交付、同一中心对象引用、存放/清中心/下一组消息是否到达。"
  },
  "普通对照": "同一对象仅S改0，前序正常且拒绝昵称：不进等级窗口，可存入有位队伍并清中心；只有一合格组，不出现下一组询问。两组S0且前序正常时，第一组清中心后才有下一组询问，拒绝后第二组保持。",
  "最小反例": "L13允许上述一组合格跨级输入：先清Shadow/Hyper、授缎带、恢复招式/V并清V/S；等级工具设L11及下限E1331并重算；首能力窗更新失败，E1400尾部写回、命名、存放/清中心均不到达。L16已正确描述此结果。另最小普通反例为一组S0：即便所有调用正常，也没有下一组询问。",
  "正常_取消_拒绝_失败_部分提交": {
    "normal": "入口标志→场景建立→合格组快照→开组/刷新接点→统一净化；正常返回后才通用存放→清中心；列表还有下一项才询问。",
    "cancellation": "开场不先问取消；选择器取消另属L15。默认跨级失败早于学招/进化/昵称取消点；同级昵称拒绝不撤销前缀。",
    "rejection": "非Shadow/G非0的统一净化早退与外层组资格分开；下一组拒绝只停止后续组；双满存放提示正常返回后仍清中心，不能把修订前提写成‘必须存放成功’。",
    "failure": "默认跨级首能力窗包装缺更新操作，先于确认键；前序资源失败可更早停止；均不保证统一退出/清理/回滚。",
    "partial_commit": "同一中心对象保留；Shadow/Hyper清除、缎带/已执行招式/EV/清S/等级下限经验与能力前缀保持。精确1400与存放/清中心尚未到。"
  },
  "必要消费者": [
    "完整PurifyChamberScreen L348–628：有显示/确认/刷新转发，无所需更新转发；Data/Scripts精确类名定位仅得该定义及构造，动态插件排除。",
    "Items L132–221首次窗口更新先于USE；Pokemon L199–205等级设置把实际经验写为等级下限。",
    "统一净化L17–58；遗迹石Screen L106–141有空更新回调，是不同对照。",
    "通用存放 Utilities_Pokemon L17–31：双满提示返回、否则入队/入盒，调用者L583–584随后清中心。"
  ],
  "有限负证据": {
    "receipts": [
      "029-purify-controller-a",
      "030-purify-controller-b",
      "031-purify-controller-end",
      "032-shadow-unified-and-relic",
      "033-growth-helper",
      "036-chamber-eligibility-and-entry",
      "047-purify-negative-definition-locator",
      "049-general-storage-consumer",
      "051-pokemon-level-setter"
    ],
    "scope": "净化室包装完整定义、统一净化/遗迹石包装/成长窗口/等级设置/接收消费者；公共测试前提与本地LC全组。",
    "result": "缺更新不是单关键词未命中：完整定义与实际接收者已读。已找到主文和现有测试的正确例外；未把动态/native未知外推为全项目无定义。"
  },
  "原始独立反证": {
    "file": "inputs/delta-j16/tasks/R7-C14/counter-review.json",
    "json_pointer": "/decisions/2",
    "file_bytes": 27323,
    "file_sha256": "f912ce3080054f9f436d516b3ae00154f7ecbd94c116a29a40111ce23eb5a5e2"
  },
  "原始作者载荷": {
    "file": "inputs/delta-j16/evidence/received-final-proposals/GR7-J16-003/proposal.json",
    "json_pointer": "/new_proposed/2",
    "file_bytes": 91439,
    "file_sha256": "9740561fe394a49c1a4529369975573b1e71e01ccd0c3dc80a63d29b3f393b6f"
  }
}
{
  "最低合同": "L13是输入→推导预期表中的单条向量，输入只给“存在合格组”，不足以保证完整存放/清中心后续，更不足以保证有下一组询问。最低必要是仅收紧L13的前提或把预期缩到入口/条件后续；WP23、WP67-B和L16/L17无需改写。",
  "精确必修级别": "TEST_VECTOR_PREMISE_AND_CONDITIONAL_SUFFIX_ONLY",
  "必须保留": [
    "旧跨级失败及部分提交",
    "同级S0/遗迹石对照",
    "双满正常返回仍清中心",
    "选择链正常UI/特殊负位置/直接调用三层",
    "下一组拒绝只停止后续",
    "资源/错误呈现/清理未知"
  ],
  "排除写集": [
    "WP23、WP67-B主文均正确，不改。",
    "L16/L17/L18/L19、SH38/39/43/44/45保持原义，不新增重复领域测试。",
    "reference/**、原裁决、旧资格及公共台账。"
  ],
  "未来政策": "不决定未来是否兼容缺操作错误；只保持参考静态事实及既有政策边界。",
  "不扩张": "不以中文翻译升级RGBA或新增净化规则；原作者错误经验driver只保留原字节，由C14真实283–293取代支持定位。"
}
{
  "全组具名向量": [
    {
      "id": "C14-PURIFY-A",
      "given": "一合格Pikachu L10/E1000/G0/S500，默认包装，前序正常",
      "expected": "目标1400；实际前缀到L11/E1331，首窗更新失败；未精确写1400、未存放/清中心",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-PURIFY-B",
      "given": "同一夹具仅S0，前序/存放正常返回、拒绝昵称、一组",
      "expected": "可存放/清中心；无下一组询问",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-PURIFY-C",
      "given": "两合格同级S0组，第一组前序/存放正常返回，拒绝switch sets",
      "expected": "第一组清中心，第二组保留，关闭并停止",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-PURIFY-D",
      "given": "同级S0确实到通用存放且双满，提示正常返回",
      "expected": "存放未成功仍清中心；不把前提收紧为必须成功",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-PURIFY-E",
      "given": "同跨级数值改由遗迹石包装，窗口与后续正常",
      "expected": "不在相同缺更新点失败；等级辅助正常返回后才精确写1400",
      "execution": "NOT_EXECUTED"
    }
  ],
  "限定": "原全部向量NOT_EXECUTED；验收只覆盖最低文字/测试前提及正确保留范围，后续实际更改另由非作者核验。"
}

角色：独立非作者 reviewer。此 prompt 现在只发布，不立即启动。须先由 R7-I 提供冻结的 candidate-input.json，含作者真实context、候选提交/树或逐文件bytes/SHA/blob、作者证据与完整差异；缺少则报告明确依赖，不自行猜HEAD。必须是与作者不同的实际context。逐必修核完整合同、原非作者反证、固定R的源/消费者、候选正文/目录/向量、正确保留和共享贡献；对正常/取消/异常/部分提交及必要历史回归出逐ID PASS/FAIL/WAIT。写 evidence/reviewer/report.md 与 per-id.json，绑定实际输入和真实context/配置回参。候选PASS只进入待整合，不等于整合PASS、ACCEPTED或CLOSED。不以作者报告或自审代替独立内容审查。
