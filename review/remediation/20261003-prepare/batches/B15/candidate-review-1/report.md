# R-B15 FULL 候选独立复审

结论 **REQUEST_CHANGES**。精确被审候选 `cc08a9150131b7e9fae8424fb0ede890169dd64f` 的16项本地贡献/10项主责全部完成独立静态审查；15项本地贡献为 PASS_SCOPED，C122 本地贡献有1项 P2 有界需修：**R-B15-C1-001**。PD32/PD33 与原稿 W32/W33 未明确标签 `nil` 与空串的差别，无法唯一推出写定的标签预期。没有自行修复作者内容。

## 身份、权限与方法

| 身份 | 精确版本 |
| --- | --- |
| origin（fetch/push均核实） | https://github.com/y805939188/pokemon-essentials-clean-room.git |
| 接受前驱 FIX_BASE | `0cfe99094b76f8d75fded0d638694677855a5f0c`，tree `f938411894a3e7aeb98fd002f3aef60725cd247f` |
| reviewed candidate | `cc08a9150131b7e9fae8424fb0ede890169dd64f`，tree `9344b2a973519cdbe8fe9ad5c2e5549334669a9a` |
| 管理派发 | `4cb51a33402ec6559a396226239afe308a4b8849`；不是正式基线 |
| 作者发布后继 | `6e26b38d9e0749e0a896b5b64fddfaf3f794cb79`；只读身份/diff/readback |
| 固定原 finding / PLAN | `93e10babe0b9c9ef8b3f5277754541b447beeeb4` / `41fffb540c6483f5296ea0d33b789b75180d27ed` |
| 参考 | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 独立分支 | `codex/cloud-dot-B15-independent-full-1-20261009`，从 exact candidate 起步 |
| 唯一写入目录 | `review/remediation/20261003-prepare/batches/B15/candidate-review-1/` |

先读候选 independent-review-request 与完整 qualified 原finding/PLAN控制、本地原合同/派发范围；不以作者 finding 表或新增行代替判断。69输入的blob/SHA-256/bytes以及16组完整原/PLAN对象pointer与规范JSON哈希重新核实；这不是69文件全文语义复审。按本地职责检查全部root/extension收窄及必要来源/调用点，不递归证明历史阅读，不另做全局review。

AGENTS.md全文已读；未找到本仓库或workspace中的相关.agents/.codex技能文件。请求配置gpt-6.1-sol / ultra / default(Standard)，任务已受理，可信后端参数回显不存在，effective保留 **UNVERIFIED**；按已批准Plan A，缺echo本身不是阻塞。没有unsupported/降级证据，没有配置/额度探测、CLI/native替代或派生任务。

参考在独立临时bare仓库精确fetch后仅以Git读文本。没有执行参考/游戏/Ruby、编译/转换/生成/反序列化、行为模拟或历史作者/review程序。概率、数学、状态与正反例均为 **NOT_EXECUTED静态推导**；新写Python仅处理Git对象、JSON、哈希、diff文本hunk和旧行保护。

## R-B15-C1-001：标签前提不唯一（P2）

位置：`deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md` **144–145行（PD32/PD33）**；`specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md` **207–208行（W32/W33）**，均绑定 reviewed candidate。

C122要求完整标签规则，PLAN验收门要求每个分配反例有明示合法前提、唯一静态结果及邻近反向；派发明确要求nil/空串。净化及原稿WP62 §6.1第144行已正确写“原标签存在（包括空串）”与“不存在”的分支，但四条新增设计只写“无名”，随后固定断言异图两项 Male/Female、同图结构多形态 One Form。这些预期仅在标签不存在时成立。

合法空串不是畸形或插件入口：在有效已登记的两性RATTATA基础种静态内容夹具中保持其余有效字段、展示形态0，只将基础 `FormName` 显式设为空文本。Species schema是小写q；section reader保留空文本，generic编译只跳nil，q返回原文本，Species初始化和Intl没有把空串归为nil。省略字段才产生不存在的标签。这里只静态检查compiler/schema文字，**没有编译或改参考数据**。非0 RATTATA1 Alolan仍可作为结构合格而未见的对照。前图解析差异或相同是条件输入，实际素材存在性未验证。

| 设计 | 具名合法前提 | 固定参考推导 | 候选预期的问题 |
| --- | --- | --- | --- |
| PD32/W32异图对照 | 形态0标签存在且为空串，两性都见，基础前图解析不同 | 雄/雌两项，但两项标签均为空串 | 不是写定的Male/Female |
| PD33/W33 | 同图解析，雄档见，形态0空串，结构合格非0形态未见、show-all关闭 | 雄档一项，标签仍为空串 | 不生成/保留One Form |
| 邻近反向一 | 其它同异图例，标签不存在(nil) | 两项生成Male/Female | 原预期只在这个明确前提下成立 |
| 邻近反向二 | 其它同结构多形态例，标签不存在(nil) | 雄档一项保留生成的One Form；没有结构多形态才清空 | 不能把nil/空串合并 |

来源：R02 `004_UI_Pokedex_Entry.rb:154–199`（161只对非0排空名，172/187区分存在与缺失）；R13 `008_Species.rb:60,175–193,229–230`；R23 `001_Compiler.rb:95–148,690–737`；R24 `002_Compiler_CompilePBS.rb:30–60,292–330`；R25 `003_Intl_Messages.rb:598–615`。精确commit/blob/range-hash在reading-log，完整机器记录在findings。

**最小修复**：只在PD32/PD33及W32/W33明确原始/本地化标签不存在(nil)，保留现有生成标签预期；同时在这些行或有界关联设计加入“存在但空串”的上述反向结果，使两个分支不再混同。无需改正确的§6.1正文、基础折叠、结构门、排序或首轮写回。更新对应作者证据/after身份；原稿新patch按父统筹批准范围规则处理，提交新精确候选供独立复核。本报告不新增canonical根因，也不替B16裁决其剩余贡献。

## 16项本地逐控制结果

以下PASS只绑定本候选、本批本地范围，不是正式接受或canonical关闭；完整original/PLAN对象及qualified约束在input-and-control-verification绑定，逐项机器记录在findings。C003/P29与C113共享修订，不重复计根因。

| finding | 主责 | 本地结论 | 条款/静态设计与独立核验 |
| --- | --- | --- | --- |
| 003 | 否 | PASS_SCOPED | §2.2、4.1–4.6、6、7、10；P31/P32/P47。菜单集合、持久顺序、共享状态改为独立领域行为；18个ASCII旧输入及参数顺序是必要兼容身份例外。保留记录/身份呼出的不同失败、稳定可见排序、版本失配和真实共享副作用。 P47独立表示概念见证与P31/P32真实失败对照，不要求源类、继承、数组或调用组织；必要兼容缺陷也不能净化为成功。 来源R06,R29,R30。 |
| A054 | 是 | PASS_SCOPED | §3.4、4；PD26/PD27；W26/W27。普通登记查展示形态名称，最近见到查原形态名称。默认有效雌性非异色ALCREMIE8无名→展示7 Ruby Cream：普通写已见7及[1,7,false]，最近见到覆[1,0,false]、不清已见7且不刷新。 原形态有名/展示P无名合法反向夹具：普通0、最近P；基种键、性别归一/原gender、首写与刷新差异未合并。 来源R01,R13,R15,R16,R24,R25。 |
| A055 | 是 | PASS_SCOPED | §6搜索；PD28/PD29；W28/W29；既有B25/B26/B35。合法区域0仅见BULBASAUR且无拥有，普通列表/持久0，最重4 Start先写4再零结果；列表、旧已接受会话参数与结果态不替换。Cancel及非结果态BACK保留4；同场景复制旧0参数，整个图鉴重开才用持久4。 未Start取消无此次持久写；命中结果态BACK才清结果、模式0/参数复位并按物种恢复游标。WP66-B正确四状态合同及B25/B26/B35字节保持。 来源R03,R09,R17,R18。 |
| A056 | 否 | PASS_SCOPED | §6区域菜单；PD30；W30。默认两区域、已解锁/可访问及设置/有图鉴前提明确：只显示区域名、见过、拥有两数字；长度仅用于全见/全拥有标记比较。 未完成与所有成员已见的对照只改变完成标记，不增加第三数字。只审B15 WP62，WP66-B其余由B16承担。 来源R04,R17,R18。 |
| A057 | 是 | PASS_SCOPED | §7、8；MG-29/MG-30/MG-31/MG-32；M29–M32。合法ID7非蛋PICHU P、玩家已加载/队伍有位、无图鉴提示/插件、在线空表：同会话Receive入同一P，玩家槽改[7]而管理仍持P；随后Edit选Faraway place、命名取消确认停止，队伍P来源仍已改变，主文件不写。 未Receive且无共享的Edit不改队伍；Receive后未选新来源即取消无此次新写。旧Create原成员来源先写后取消、Delete会话及Export/主文件范围保留。 来源R11,R12,R16。 |
| C003 | 否 | PASS_SCOPED | §6；目录P29；P29/P44；原P29/P44。本地P29恢复命令后与新图设置后的两个观测点，前提含无覆盖/输入正常/无事件插件再写；与C113同一修订，不重复根因。 Custom覆盖独立跨图保留的反向见P44。FS/FP等其它owner和历史WP80处置不重写、不重审。 来源R07,R08,R09,R10。 |
| C007 | 否 | PASS_SCOPED | §4.6；PL01–PL18；P45/P46；原相同行。全部18旧入口逐项输入/默认/转发/返回/失败核对。RegisterBattle预检start0，注册版本数0→1、传入count成为start/current；Reset未定义参数名先于查询求值失败；delete赋值结果false、NPC也可隐藏；Ready只写自开关不写再战旗标。 静默/普通、记录级/标识级、训练家/NPC、拒绝确认/未知类型、空表/空队伍等反向分开；完整目录见本报告逐入口表。67树果仍仅有条件性范围问题，无新增全表义务。 来源R06,R19,R20,R21,R22,R28,R30。 |
| C020 | 否 | PASS_SCOPED | §8 Custom；P43；原P43。已有覆盖A、前置UI/宿主正常：先进入Audio/BGM目录再列文件；缺目录在子列表/清覆盖/清旗标前失败，A及旗标保持。 可进入的空目录USE才可清覆盖/两旗标；空BACK均保持。宿主具体异常画面、dispose恢复与媒体存在未证。 来源R07,R10。 |
| C107 | 是 | PASS_SCOPED | §4.3；P39/PL01/PL02；原相同行。登记CAMPER、Jeff、有效地图/事件、同键无可见、默认count1/start0四独立夹具：文本普通规范化新增并排序后，原输入反馈查找失败，不回滚且记录可见。 文本静默true、规范身份普通true、规范身份静默true；未知类型新增前false。失败未改成写入失败或事务回滚。 来源R06,R19,R28。 |
| C108 | 是 | PASS_SCOPED | §5.1、8；P40/PL03；原相同行。NPC现有记录呼出且有信号，ID0/省略不满足正ID分派，走训练家消息类型校验失败、记录保留；正ID缺失由全局公共事件助手false后显示缺事件提示；正ID存在进入事件路径。 无信号更早拒绝；训练家0正常走训练家文字；未混同解释器同名成员或承诺已执行事件。 来源R06,R19,R20,R21。 |
| C109 | 是 | PASS_SCOPED | §3.1、8；P34/P33；原相同行。有当前位置有效0请求未知99→当前位置0；有效不同区域1→左上角无玩家图标；无定位即使请求有效1也优先0左上角；严格查询只对最终实际区域。 当前指向未知或无定位且0缺失仍Unknown ID在友好提示前失败；旧P33正确边界保持。 来源R05,R19,R27。 |
| C110 | 是 | PASS_SCOPED | §3.1子格；P35/P36；原相同行。W,H>0且玩家坐标合法、正区域宽w：h=ceil(len(S)/w)，轴尺寸>1时加floor(x*w/W)、floor(y*h/H)；(13,12)+20×20,w3,len5,(19,19)→(15,13)。 同长10000/11111同结果；w1/len1两轴0、缺尺寸/宽0无偏移。只使用长度，不添加字符掩码阻挡，不外推畸形尺寸。 来源R05,R27。 |
| C111 | 是 | PASS_SCOPED | §3.2、3.4；P37/P38；原相同行。重复同格点合法且有序：第一点开关51关闭时名称/详情空串、治疗无值；第一点可见却缺详情/治疗也不由第二点补齐。图标与USE均消费首治疗查询。 交换顺序或完整可见第一点生效；wallmap开关首条隐藏；debug+CTRL仅豁免已访问，不越首条/隐藏/缺字段。 来源R05,R26,R24。 |
| C112 | 是 | PASS_SCOPED | §5.3、4.6；P41/P42/PL15–PL17；原相同行。每通播放先取得一次TP/TE，即使无占位也取；分段与重复占位共用。TP队伍版本max(current,start)、按成员均匀。TE首非空Land/Cave/Water前min(n,4)槽均匀、保留重复、不权重、第五排除。 97/1/1/1前四各1/4；A/A/B/C为1/2,1/4,1/4；Cave两槽/Water一槽、版本0回退、三表空或双版本无记录空文字。空队伍/非法物种非统一空保护；普通遭遇权重不改。 来源R06,R22。 |
| C113 | 是 | PASS_SCOPED | §6、7；目录P29；P29/P30/P44；原相同行。March命令后lower=false/higher=true且不写覆盖；另一图新图设置后两旗标false；默认BGM覆盖是独立全局状态，Custom A跨图仍在。 P44 Custom→March→换图对照与旧P30 Custom→March→Stop保持；只核状态/请求，不承诺最终曲目和宿主输出。 来源R07,R08,R09,R10。 |
| C122 | 否 | REQUEST_CHANGES | §6.1；目录PD31–34；PD31/PD32/PD33/PD34；W31–W34；既有B31/B38。正文结构门、show-all只放已见门、形态0同图雄档折叠、具名形态首合格性别、结构多形态而非可见项数、nil/空串分支、排序和首轮写回正确。 PD31 RATTATA1两性/仅雌/show-all，PD34首轮/BACK及旧结构门均支持；但PD32/PD33及W32/W33用“无名”未区分nil/空串，统一标签预期不能唯一成立，见R-B15-C1-001。 来源R02,R13,R14,R15,R23,R24,R25。 |

## C007：18旧入口逐项核验

共同前提为固定默认环境无插件补充，弃用警告/消息/地图服务正常，记录及类型输入合法。ASCII名称/参数序列是兼容身份，不要求新实现采用源类或同名内部接口。R06完整1–706行静态回读；下面每项与候选§4.6及PL01–18逐一比较，未执行入口。

| 旧输入 | 默认/行为/返回 | 失败与反向边界 |
| --- | --- | --- |
| pbPhoneRegisterBattle(message,event,type,name,count) | 预检start0；message假/空值用默认邀请；确认后count被置起始版本、版本数0提升1；反馈匹配时true | 预检/确认拒绝false无新增；文本类型先写后反馈失败；不修正参数误置 |
| pbPhoneRegister(event,type,name) | 静默，count1/start0；合法类型true | 不强制持机；未知false；隐藏同键可另建 |
| pbPhoneRegisterNPC(id,name,map,show_message=true) | true普通/false静默，正常均true | NPC0注册有效，拨打类型校验失败；正ID事件另列 |
| pbPhoneDeleteContact(index) | 完整持久序列零基/有效负索引，赋可见false而返回false | 训练家清倒计时/旗标、A=true/刷新；NPC也能隐藏；越界局部失败；不套UI不可删NPC门 |
| pbFindPhoneTrainer(type,name) | 尝试标识查找 | 缺公开查询能力，失败而不是空；记录级正确查询对照 |
| pbHasPhoneTrainer?(type,name) | 尝试存在性查询 | 在真假比较前失败，不返回false |
| pbPhoneReadyToBattle?(type,name) | 尝试查询后检查就绪 | 查询前失败；记录级flag1/0正确对照 |
| pbPhoneReset(tr_type,tr_name) | 尝试重置 | 未定义trainer_type/name实参求值先失败，无任何查询/重置；不把后续不可达返回作合同 |
| pbPhoneBattleCount(type,name) | 起始0公开相对版本查询，正常标识恒0 | 类型错入布尔联系人选择；记录级相对进度可为1 |
| pbPhoneIncrement(type,name,count) | 忽略count，start0，正常无动作返回空 | 同失配；记录级可推进，胜利重置独立 |
| pbSetReadyToBattle(contact) | 训练家A=false/B=true/刷新，末项true | flag/倒计时不写；NPC无动作空；不是完整计时就绪 |
| pbRandomPhoneTrainer() | 同区、异图、地图名不同的可见训练家均匀选；无位置/候选空 | 不查信号；选中不是已拨打 |
| pbCallTrainer(type,name) | 按身份呼出 | 缺查询在信号/距离门前失败；UI记录呼出正常走门 |
| pbPhoneGenerateCall(contact) | 返回文字，flag1可写2 | 不播放、不抽TP/TE；NPC空类型可失败；flag0无同推进 |
| pbPhoneCall(dialogue,contact) | 播放分段，TP/TE每通各一次，透传Click收尾消息结果 | 不补布尔成功保证，也不执行呼出门；异常局部传播 |
| pbEncounterSpecies(contact) | 单次TE首非空表前四槽均匀；无训练家/双版本无记录/三表空为空文字 | 每次独立可重抽；非法参数/物种不是统一空保护；不改变普通遭遇权重 |
| pbTrainerSpecies(contact) | 单次TP版本max(current,start)，队伍成员均匀；非训练家/无数据空文字 | 空队伍或非法物种可失败；重复成员保留次数 |
| pbTrainerMapName(contact) | 地图命名服务值 | 不新增信号、可见或访问门；未知边界由命名服务决定 |

## 九正式路径、完整diff与原稿批准应用

九个正式输出是WP62/WP63/WP64的三份净化正文、对应三共用测试目录，以及三份原spec：pokemon-rules/wp62、ui/wp63、creature-rpg/wp64。完整path/before/after的commit/blob/SHA-256/bytes在diff-and-scope-verification；全部与author formal-identities字段匹配。

完整**未过滤**前驱→候选差异保存在[complete-predecessor-to-candidate.diff](complete-predecessor-to-candidate.diff)，834,537字节，SHA-256 `a8dc56586bc3397aa0570bec8360985caac64c6b588c165865b1364a585125d3`。新Git生成字节与发布后继complete-candidate-after-sync.diff完全相同。31变更路径=9正式+22作者/候选证据；全部路径及边界核验，九正式文件的全部变更hunks与本地修订逐项核对。无公共台账/index/导航/覆盖、其它owner正文、参考、历史审查路径改动。证据内的旧six-file draft diff/旧publication不作为当前候选；未执行它们或历史校验程序。

后继6e26…相对候选只新增四个author-draft-1证据文件（两diff、publication md/receipt）；九个正式blob与候选完全相同。没有将后继SHA、旧529fa2…六文件草案或dispatchSHA替作reviewed版本。

三原稿权限来自父对`70a28cfc56ee17b8dc4d815515e96640d80c6321`冻结proposal/patch的明确范围批准：proposal blob `4f9c627cc4b5f8e377aae1034ebc34985ae59b5e`；patch blob `3560c08a8c1899db54986cc687939c25cffa68de`，46,822字节，SHA-256 `9ea9fbce20b311616b3350bf4a1d8ae997c13093b1ac468527d0a630cbf17b87`。批准只解决范围，未给质量PASS。

独立逐hunk比对批准patch的旧上下文，并仅在内存中重建文本以比对candidate三原稿字节；结果精确等于approved proposed_after。没有Git apply、没有改作者输出。before三项均为FIX_BASE：WP62 `37bd28e…`→`657a417…`，WP63 `6863e9c…`→`ad42003…`，WP64 `9744c9b…`→`0a021ae…`，完整40位blob与sha/bytes在证据。proposal/patch历史状态字段按原字节保留，当前应用状态由application receipt辨认，不能用历史false字段重建一个已解除的授权阻塞。

原稿静态设计旧25/33/30行的序列和重复保持，变为34/65/32；仅旧P29/M29精确修订，其它旧行不变。三个净化正文与原稿对应新增语义一致；C122四行的相同欠前提也明确作为质量需修报告，精确应用成功不能免除这个问题。

## 18目录行保护与新增设计

独立从18份前驱目录提取旧行，比对完整顺序/重复及其它owner分节字节，未调用作者保护程序。2,995旧行全部保留，B15旧88行以外的2,907行和所有非本地分节字节不变；15份整文件byte-identical。只修订批准的旧P29/MG-29两行。新增43行=PD26–34九行、P34–47十四行、PL01–18十八行、MG-31/32两行；无删行、重排或额外ID。

完整本地PD01–34、P01–47/PL01–18、MG-01–32及相关B行已按控制/必要来源检查。全部新增正反设计均为静态设计，C122的PD32/33是本报告唯一需修组；保护统计不冒充所有2,995条语义测试已通过，也不重审其它owner未改条目。

## 接口、未证范围与后续

九组affected接口（B02/B03/B04/B06/B07/B08/B09/B10/B14）由父另派，本报告不等待、不代签，不把作者导航或目录保护签为他们的NOT_AFFECTED。本地检查保留地图返回三元组、FLY/访问/CTRL门、电话事件及采样粒度、普通遭遇权重、March/覆盖、新图通知的界线；没有发现另一个本地需修接口问题。C122标签设计问题涉及WP62/形态UI，已明确报告，供父及相关owner处置。B16的A056/C122 WP66-B其余义务不纳入本批通过。canonical全部保持OPEN，接受/关闭增量均0。

U01–U10/G01–G12/AX01–AX20及完整继承具名限制保存在source-limits。Scripts.rxdata及所有二进制/真实地图事件、媒体/字体/soundfont、Game/host/DLL/mkxp配置与容量、8杯赛名单与pokemon_metrics样本、备份/gen、插件/动态调用/deprecated/EventScene/动态阴影实际可达性、真实Demo链均不因本审查变成已证。素材解析、宿主服务与有效图尺寸只是静态夹具前提；不保证像素、音频最终曲目、事件执行或异常恢复。参考/编译/转换/生成/反序列化/行为模拟/历史审者程序执行0，向量执行0，运行观察0，已证Demo链0。

本轮FULL本地候选审查已完成，当前质量阻塞只有R-B15-C1-001。作者按有界范围返回新SHA后再独立复核；candidate及分别affected门通过后才由sole A-REG整合、冻结actual，并完成独立FULL/affected actual门。相同正式blob、15个本地PASS或管理读回均不代替新candidate/actual批准。本报告发布与独立远端读回见publication-receipt，不写共享登记、不合并main。
