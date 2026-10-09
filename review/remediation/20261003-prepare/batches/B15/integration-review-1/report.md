# R-B15 FULL actual 独立复审

**PASS_SCOPED**，精确 reviewed actual `fd44556f877a400337eb893757d91f1adfa856ba`（tree `b05ced639a821a14021496e383c24106f7d6681b`）。16项本地贡献／10项主责最低验收全部通过，本角色未解阻塞 **0**。这是自己的实际整合质量结论：候选静态证据按准确版本复用，随后独立核本次完整差异、控制/登记、最新B11前驱和当前接口条件；没有自动转签候选裁决。

## 身份与准确基线

- actual：`fd44556f877a400337eb893757d91f1adfa856ba`；其直接parent为当前正式接受前驱B11-C `6811b313b18bb1b4ed59ca3218b3fbf4a9f1f411`。
- candidate：`6cd88996e5d48bffb1e85fd4bdaa87bed2d0a1d4`；候选原FIX_BASE `0cfe99094b76f8d75fded0d638694677855a5f0c`只用于核基线前移，不能回滚当前正式前驱。
- 管理派发包：`e2b1e93375be583320711c1ca7d387373bf328a9`，仅报告后继，未作为reviewed目标。
- 本角色候选语义报告：`966ef4de91a760cd30eb35434c214265df2e1b2a`；发布 `49c233f939fc60e98a27d3286ebffe5e6cb8428a`。九owner候选语义 `779388c2d83bf1d9b80d07a03ca87b029cfeaa4c`／发布 `80021cfe0ac99f78767892a45dcc11e0f26ef3a1`。
- origin fetch/push均核实为https://github.com/y805939188/pokemon-essentials-clean-room.git；独立分支 `codex/cloud-dot-B15-full-actual-review-1-20261009` 从准确ACT创建；唯一写入 `review/remediation/20261003-prepare/batches/B15/integration-review-1/`。

请求gpt-6.1-sol／ultra／default(Standard)。原独立FULL角色续接，requested/admission/effective分别记录；可信后端echo缺失为UNVERIFIED，沿用批准Plan A，非阻塞。无不支持或降级证据，无额度/配置探测、CLI/native替代或重复/嵌套任务。AGENTS全文与clean-room、参考只读、静态行为合同保持。

## 两份完整差异与整合边界

| 完整未过滤差异 | 全部路径 | 字节 | SHA-256 |
| --- | ---: | ---: | --- |
| accepted-predecessor-to-actual | 137 | 10192150 | `21b13a5c01a8d2842b7837a87be18709641e8aa4cb6b9ac96c23b8fed6b6dacd` |
| candidate-to-actual | 257 | 15166811 | `0d1d9467bef9fb260f226393b5f5d8b52a37bdbea76c5c2d0d0794a3e409be75` |

本角色独立执行 `git diff --no-ext-diff --binary --full-index <准确from> fd44556f877a400337eb893757d91f1adfa856ba`，不加路径过滤；与冻结hash逐字节匹配。完整命令、全部137／257路径及每路径分类/身份保存在integration-and-protection-verification，临时raw缓存仅便利；可从固定提交重建，不复制25MB归档制造额外读取门。导航或旧draft均未代替完整差异。

最新前驱→ACT精确137路径＝九正式＋45作者/候选材料＋69独立候选文件＋11新G材料＋三公共登记文件。候选→ACT精确257路径＝169当前B11-C保留路径＋74发布原字节复制路径＋11新G材料＋三公共增量。全部路径已独立核验；新增/既有历史archive逐字节保留，不把内嵌旧diff当新行为审查。

九正式文件完全等于NEW；九before完全等于FIX_BASE。因此最新前驱→ACT九正式diff精确等于FIX_BASE→NEW已独立审查的完整正式diff。正确WP62§6.1、final WP63§3.1/§8、三份净化正文及其它14项贡献均无actual语义改写；不是仅凭G的formal9_equal声明。

三original初次范围批准和后续C122仅W32/W33、C109仅原P33与§8一句的具体批准/补丁/应用证据保持准确候选原字节。原稿ACT字节等于已独立检查的NEW，before未因B11前移改变；两修复前后和初次三原稿完整patch质量/范围证明分别精确复用首轮与round2 FULL证据。范围许可不充当质量PASS。

## 两项P2在ACT重新判断

**C122 / R-B15-C1-001：PASS_SCOPED。** ACT的PD32/PD33（目录144–145）及原W32/W33（207–208）明确有效RATTATA两性形态0展示自身、其余有效、show-all关闭、无插件；省略FormName使原始/本地化nil，显式空文本且本地化仍空串是合法邻近反向。固定源分支和schema/本地化证据复用准确FULL阅读记录，ACT完整保存该前提与预期。

| 静态前提 | ACT唯一预期 |
| --- | --- |
| nil，同前图（可皆未找到），仅雌见 | 最多一项，按雄档展示；不证明图像资源存在 |
| nil，异前图，两性见 | 雄/雌两项，生成Male/Female |
| 上例仅改原始/本地化为空串 | 仍两项同排序，两空标签 |
| nil，同前图雄见，有结构合格却未见RATTATA1 Alolan | 生成One Form，结构多形态使其保留，不能按最终可见项数清空 |
| 上例仅改为空串 | 同一雄档项，空标签，不生成One Form |
| nil同图例去掉结构合格非0形态 | 原生成One Form置空 |

show-all只放宽已见门、结构门/雄档折叠/性别排序、具名首合格性别与首轮末次形态写入/BACK不回滚均保持。没有新增无效输入假例，也没有运行形态列表。

**C109 / R-B15-AFF-B03-001：PASS_SCOPED（FULL本地）。** ACT目录P33第87行、原P33第223行及原§8第172行将Unknown ID失败限定为最终实际选定查询的未登记ID；正确final§3.1/§8与P34保持。首轮FULL未检出旧P33泛化问题，round2及本ACT用准确修复证据重新判断，旧历史不改。

| 静态前提 | 最终ID与ACT预期 |
| --- | --- |
| 无定位、0未登记，其余UI/数据正常 | 优先0，严格查询失败先于友好提示；显式有效不同请求不越无定位门 |
| 当前99未登记、请求-1或未登记请求 | 最终99，严格失败先于友好提示 |
| 0未登记、当前1已登记、请求-1 | 只查询1，不查询缺0，按当前定位；显示等于当前且定位有效时有玩家图标 |
| 当前99未登记、显式不同且已登记1 | 只查询1，不查询缺99，区域1左上角且无玩家图标 |
| 当前0已登记、显式99未登记 | 回当前0定位，无Unknown ID；保留原minimum/P34反例 |

子格公式、首点/隐藏/缺字段不后找、CTRL/FLY与返回三元组没有因actual整合变化。具体渲染及真实地图未证。本结论不代签B03 actual gate。

## FULL16与主责10的实际最低验收

完整原finding、approved PLAN acceptance、当前qualified root/extensions/premises/minimum全部以原完整对象/准确pointer/hash绑定；ACT registry16条与这些完整字段精确匹配。findings给每项新的actual结论、全minimum/recheck/有效前提/反例及精确复用出处，primary10逐项最低验收满足；不是用作者摘要或目录保护取代PASS。

| 控制 | 主责 | ACT结论 | 完整本地最低验收与反向 |
| --- | --- | --- | --- |
| 003 | 否 | PASS_SCOPED | 菜单集合、持久顺序、共享状态改为独立领域行为；18个ASCII旧输入及参数顺序是必要兼容身份例外。保留记录/身份呼出的不同失败、稳定可见排序、版本失配和真实共享副作用。 P47独立表示概念见证与P31/P32真实失败对照，不要求源类、继承、数组或调用组织；必要兼容缺陷也不能净化为成功。 |
| A054 | 是 | PASS_SCOPED | 普通登记查展示形态名称，最近见到查原形态名称。默认有效雌性非异色ALCREMIE8无名→展示7 Ruby Cream：普通写已见7及[1,7,false]，最近见到覆[1,0,false]、不清已见7且不刷新。 原形态有名/展示P无名合法反向夹具：普通0、最近P；基种键、性别归一/原gender、首写与刷新差异未合并。 |
| A055 | 是 | PASS_SCOPED | 合法区域0仅见BULBASAUR且无拥有，普通列表/持久0，最重4 Start先写4再零结果；列表、旧已接受会话参数与结果态不替换。Cancel及非结果态BACK保留4；同场景复制旧0参数，整个图鉴重开才用持久4。 未Start取消无此次持久写；命中结果态BACK才清结果、模式0/参数复位并按物种恢复游标。WP66-B正确四状态合同及B25/B26/B35字节保持。 |
| A056 | 否 | PASS_SCOPED | 默认两区域、已解锁/可访问及设置/有图鉴前提明确：只显示区域名、见过、拥有两数字；长度仅用于全见/全拥有标记比较。 未完成与所有成员已见的对照只改变完成标记，不增加第三数字。只审B15 WP62，WP66-B其余由B16承担。 |
| A057 | 是 | PASS_SCOPED | 合法ID7非蛋PICHU P、玩家已加载/队伍有位、无图鉴提示/插件、在线空表：同会话Receive入同一P，玩家槽改[7]而管理仍持P；随后Edit选Faraway place、命名取消确认停止，队伍P来源仍已改变，主文件不写。 未Receive且无共享的Edit不改队伍；Receive后未选新来源即取消无此次新写。旧Create原成员来源先写后取消、Delete会话及Export/主文件范围保留。 |
| C003 | 否 | PASS_SCOPED | 本地P29恢复命令后与新图设置后的两个观测点，前提含无覆盖/输入正常/无事件插件再写；与C113同一修订，不重复根因。 Custom覆盖独立跨图保留的反向见P44。FS/FP等其它owner和历史WP80处置不重写、不重审。 |
| C007 | 否 | PASS_SCOPED | 全部18旧入口逐项输入/默认/转发/返回/失败核对。RegisterBattle预检start0，注册版本数0→1、传入count成为start/current；Reset未定义参数名先于查询求值失败；delete赋值结果false、NPC也可隐藏；Ready只写自开关不写再战旗标。 静默/普通、记录级/标识级、训练家/NPC、拒绝确认/未知类型、空表/空队伍等反向分开；完整18入口表复用准确首轮FULL的C007逐入口节；文件身份见本目录reading-and-reuse-log绑定的首轮／round2证据。67树果仍仅有条件性范围问题，无新增全表义务。 |
| C020 | 否 | PASS_SCOPED | 已有覆盖A、前置UI/宿主正常：先进入Audio/BGM目录再列文件；缺目录在子列表/清覆盖/清旗标前失败，A及旗标保持。 可进入的空目录USE才可清覆盖/两旗标；空BACK均保持。宿主具体异常画面、dispose恢复与媒体存在未证。 |
| C107 | 是 | PASS_SCOPED | 登记CAMPER、Jeff、有效地图/事件、同键无可见、默认count1/start0四独立夹具：文本普通规范化新增并排序后，原输入反馈查找失败，不回滚且记录可见。 文本静默true、规范身份普通true、规范身份静默true；未知类型新增前false。失败未改成写入失败或事务回滚。 |
| C108 | 是 | PASS_SCOPED | NPC现有记录呼出且有信号，ID0/省略不满足正ID分派，走训练家消息类型校验失败、记录保留；正ID缺失由全局公共事件助手false后显示缺事件提示；正ID存在进入事件路径。 无信号更早拒绝；训练家0正常走训练家文字；未混同解释器同名成员或承诺已执行事件。 |
| C109 | 是 | PASS_SCOPED | 两版P33及原稿§8把失败限定为最终实际查询的未登记ID。无定位缺0、最终仍99缺失失败；0缺失但跟随合法1、当前99缺失但有效不同请求1成功；正确§3.1/净化§8及P34保持，未证明具体渲染。  |
| C110 | 是 | PASS_SCOPED | W,H>0且玩家坐标合法、正区域宽w：h=ceil(len(S)/w)，轴尺寸>1时加floor(x*w/W)、floor(y*h/H)；(13,12)+20×20,w3,len5,(19,19)→(15,13)。 同长10000/11111同结果；w1/len1两轴0、缺尺寸/宽0无偏移。只使用长度，不添加字符掩码阻挡，不外推畸形尺寸。 |
| C111 | 是 | PASS_SCOPED | 重复同格点合法且有序：第一点开关51关闭时名称/详情空串、治疗无值；第一点可见却缺详情/治疗也不由第二点补齐。图标与USE均消费首治疗查询。 交换顺序或完整可见第一点生效；wallmap开关首条隐藏；debug+CTRL仅豁免已访问，不越首条/隐藏/缺字段。 |
| C112 | 是 | PASS_SCOPED | 每通播放先取得一次TP/TE，即使无占位也取；分段与重复占位共用。TP队伍版本max(current,start)、按成员均匀。TE首非空Land/Cave/Water前min(n,4)槽均匀、保留重复、不权重、第五排除。 97/1/1/1前四各1/4；A/A/B/C为1/2,1/4,1/4；Cave两槽/Water一槽、版本0回退、三表空或双版本无记录空文字。空队伍/非法物种非统一空保护；普通遭遇权重不改。 |
| C113 | 是 | PASS_SCOPED | March命令后lower=false/higher=true且不写覆盖；另一图新图设置后两旗标false；默认BGM覆盖是独立全局状态，Custom A跨图仍在。 P44 Custom→March→换图对照与旧P30 Custom→March→Stop保持；只核状态/请求，不承诺最终曲目和宿主输出。 |
| C122 | 否 | PASS_SCOPED | PD32/PD33及W32/W33现分别给出原始/本地化nil和存在空串；nil异图Male/Female、空串异图两空标签；nil同图结构多形态One Form、空串同图仍空；去掉结构多形态时nil生成标签置空。正确正文、结构/雄档折叠、排序与首轮写回未改。  |

上述两P2之外14项，准确候选完整记录（仅after身份刷新除外）和正确正文的既有独立源证据继续有效；ACT复制与本次所有差异未改变其调用/数据/条件。18旧电话逐入口完整输入/默认/返回/失败表复用首轮FULL报告e08998ab5d208f7607a4750ab57beb6a4b985bf6的C007节；不把单一兼容摘要签作全表。C007条件树果67范围仍保留，未扩大为新的完整树果枚举义务。

## B11-C前移：自己的有界接口结论

67项当前B15 read输入和九before从FIX_BASE到B11-C逐字节未变；另两immutable原review按93e10…准确提交保留，不要求旧原件进入当前树。独立核B11/B15双向read/write、formal与local qualified ID集合无交集。B11十正式边界（八净化/目录＋两已批准原稿）和142份自有namespace全部等于当前B11-C；不是将初始八formal计划误当最终十路径。

本轮读完B11基线正式前移的九路径59新增/22删除：动态目标/诅咒重定向、结冻头成功击、skillswapclause、0.1kg有效重量/捕获消费者、能力/物品配对重数、主动HP与持物HP分工及13条新增静态设计。只核这些变化对B15当前调用/数据/条件的影响，未重新裁定B11全部历史质量。

| 当前交界 | 本ACT clause/caller/data/condition与结论 |
| --- | --- |
| 图鉴登记/形态与捕获接收 | ACT WP62§3.1: 战斗包装内部战斗门与全局个体形态提交分列；捕获队列直接接收另有无门路径。§3.4/§6.1消费展示形态/原始名称/结构门；不消费招式动态目标、成功击数或战斗重量。 WP38捕获资格/随机与接收仍由自身限定；B15只在既有登记/接收接点按明确输入推导记录。B11没有改变登记接口、展示号映射或FormName数据，也未增加/移除该调用。 没有新B11接口义务；保留已正确的包装/直接调用/全局玩家接收者差异。B11的EISCUE静态例不会把形态列表或登记门改成统一规则。 |
| 图鉴搜索/区域与地图首点 | ACT WP62§6主列表行体型取末次形态数据，排序/拥有过滤及四搜索状态不取场上临时重量管道。ACT WP63§3.1/§3.2/§3.4消费地图定位/区域注册/Point顺序和FLY资格。 物种及形态数据、WP66-B四状态、地图/FLY调用条件等当前读取不变；B11仅战斗有效重量和捕获率消费者数值层，不定义区域或Point。 没有新增搜索/地图回归前提；不是把重量数值或战斗目标类别作为地图/搜索条件。 |
| 电话18旧输入/注册反馈/NPC/抽样/跨图 | ACT WP63§4.2–4.6/§5.1–5.3: 类型/版本/持久联系记录、正公共事件ID、消息/信号/地图门；TP成员等概率、TE前四槽均匀、每通共享。§6/§7消费新图旗标和独立BGM覆盖。 训练家/遭遇数据、地图事件及新图设置合同均属原有固定读输入；战斗行动目标/实际HP损失不进入这些数据查询或分派/抽样门。WP63§5.2战斗中暂停已有，不修改。 没有真实新B11接口影响；电话采样不是普通遭遇权重或战斗随机。公共事件/跨图实际运行仍未证。 |
| 礼物同一PICHU个体Receive→Edit | ACT WP64§6.1/§7: ID7非蛋PICHU、队伍有位、无图鉴提示、无插件/额外修改；静默收编成功后队列[7]、管理会话仍持同一P，来源选择先写而命名取消不回滚。 WP26/队伍容量/获得接点与原读取不变；例中没有主动或持物治疗、捕获抽签或战斗行动；同一个体共享并未被B11改为复制。 B11没有更改礼物/管理/来源赋值接口；没有新增有界B11门。真实下载/解码/事件仍未执行。 |

在上述有界当前范围**未发现真实新B11接口影响，故不需要新增B11门**。这是自己的B15 actual回归判断，G身份声明只作待核材料；不代表B11新整域质量PASS或其它reviewer签名。若之后出现具体新调用/字段/条件影响，须按那个精确接口定点重冻结，不能据假设扩大本任务。

## 目录、发布原件与公共保护

18目录独立文本检查：BASE旧2,995 ID顺序/重复保留；NEW的3,038条静态行文字/顺序/重复全部在ACT保留（43原B15新增不添新ID）。当前B11-C已有3,008行；ACT共3,051行，多出的13行完全是已接受B11设计，而非新B15设计。旧2,907其它owner行保护依据原FULL＋本次完整NEW行/文本保持；批准的B15旧P29/MG-29等内容修订也保持，不误称所有旧内容从未改变。

45作者/候选材料与69独立候选文件按各准确publication source逐字节核验。B02语义manifest（7793…）与发布manifest（8002…）不同：七条语义文件身份全部相同，仅在排序列表插入一条publication-receipt并追加report_payload_commit/publication_receipt_scope；不声称整个manifest相同。其余候选门原语义/发布身份已核，仍仅为候选历史，九owner actual没有自动转签。

两公共TSV均保留当前B11-C旧207行完整raw prefix，仅追加本16条pending；223物理行不是223已接受贡献。每条完整控制pointer、canonical OPEN、primary身份、candidate与实际门pending、全contributors、从当前207条接受receipt独立重算accepted/remaining、非本地义务均匹配。B11接受统计原文件保持：12/21批次、207accepted、229OPEN/0CLOSED；六B11接受成果未回退，B15接受增量0。final-integration-review旧完整body为字节相同suffix，仅新增本G待审说明；finding-ledger整体不变。

B12原序列化与B16仍待B15-C后新冻结；没有释放依赖。新G、正式及公共文本对准确PRE→ACT whitespace检查独立通过。所有冻结.diff/.patch literal字节保留；不把历史归档whitespace重写成新规范。

## 保留限制与结束条件

source-limits保留完整先前FULL对象及精确身份：U01–U10/G01–G12/AX01–AX20、binary/serialized、真实地图/公共事件、媒体/字体/soundfont、宿主/配置/容量、八杯赛/pokemon_metrics样本、backup/gen、实际插件/动态调用/deprecated/EventScene/动态阴影可达性、条件树果67和非局部Demo/global义务均不缩减。

参考/游戏/Ruby/编译/转换/生成/反序列化/行为模拟器/任何历史作者review程序执行0；静态设计执行0，runtime observations0，Demo proven0。新Git/JSON/hash/文本只是检查与证据整理；静态合法正反例不是已执行测试。媒体、事件执行、宿主结果/异常恢复与具体渲染仍未证。

本角色有限FULL actual16/10门已完成，PASS_SCOPED，未解阻塞0。九owner actual由另一原reviewer负责，不等待、不代签；此报告不执行sole C、canonical关闭或最终global门。公共16仍pending，父收齐全部准确actual裁决后才可唯一C。仅写新integration-review-1，作者、formal/public/reference、候选与历史报告保持只读。

普通report commit/push后用独立fresh bare HTTPS网络抓取核remote ref/FETCH_HEAD/tree/所有报告字节并保存receipt后继；报告SHA与reviewed ACT分离，未构造自身hash循环。
