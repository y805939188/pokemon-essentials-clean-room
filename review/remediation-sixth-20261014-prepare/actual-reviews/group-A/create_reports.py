"""Materialize root's independent semantic adjudications for the frozen actual composition."""
import datetime, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
ACTUAL='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
TREE='67e8c55d520fa8cad2928cb4b95e24c3ed602d5a'
FORMAL='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
input_binding=json.loads((ROOT/'payload-audit/actual-input-group-A-extraction.json').read_text())
ledger=json.loads((ROOT/'reading-ledger.json').read_text())
records=[
 ('GR6-K-001','R6-U01','P3','WP10 §4/4.3; WP27; MG17–19',
  '适用旧版本中旧lastpocket保留，当前游标复制旧2，清的是另一大小写字段；另外三分支清旧。单对象调用不推进上下文，当前5后再调仍回2。',
  '完整成功转换链推进两个版本，后续通常读取不重选；旧值空/当前版本不覆写。晚失败不撤销已到游标前缀。',
  'WP27 当前游标导航与U12丢弃/U14名称条款组合；旧字段不在正常Bag/UI导航中清理。',
  'R1 WP10原迁移范围；三目录旧MG/字段清旧/版本门；不重签电话、植物、寄养或宿主迁移。'),
 ('GR6-K-002','R6-U01','P2','WP18 §6.1/9; CI29–31',
  '同时四项的同值后项覆盖条件；(0,0,0,2)/(1,0,0,2)接纳整数名字0；(1,0,1,2)/(0,0,1,2)拒绝，前项id碰撞本身不能绕过。',
  '合法Valid正常；单字段name=0拒绝并保持旧值。构造拒绝在四次赋值前，未保证畸形名字的后继界面/保存可用。',
  'WP18与U10尺寸/NPC来源及U14初始Happiness组合，既有Owner被Pokemon原样接纳而不递归复查。',
  'R2 B05 A021/A022、B06 A033；CI25–28、拥有者语言、公开号、外来判据保持。'),
 ('GR6-K-003','R6-U01','P2','WP34 §5.2/8.2/9.4; WP21; WP62 §3; BR27–31',
  '默认SHELLOS母系0在正孵化步数5120之后显式同值提交；清特性、重算及条件图鉴登记仍执行，性别/普通异色缓存被求值，写seen/form/空last，不写owned/seen-egg。',
  '缺玩家/缺Dex无记录而仍重算；非空last保持。N0不读不清已有缓存；N>=1首轮读取、末次PID未读取边界保持。后继满队或刷新失败无回滚。',
  'WP62与U10家族/图鉴消费和U11显示/登记条件组合；WP33生成后容量门及WP35孵化重写拥有者/后写拥有集合保持。WP21同值显式提交与动态读守卫分开。',
  'R2 B05/B07 A026、B08 A053；R4 FURFROU432000/432001；R5 M04-002重入请求与实际存储形态分开；BR旧继承顺序和首合格永石保持。'),
 ('GR6-O-001','R6-U03','P3','WP60 §4; R6-FS01–11',
  '普通成功依次等待域、咬钩100、窗口域、上钩100共4；无遭遇/等待取消只等待，咬钩失败2、超时3、自动上钩3，加速等待独立追加一次。',
  '演出异常时窗口抽样尚未到达；上钩样本只在有效输入且非自动后消费。正常计数+1/清理与异常前缀分开；直接钓鱼不直接增加钓鱼战斗统计或请求遭遇。',
  'WP06普通随机域与WP60分支一致；U11解释器直接调用公共事件后仍内置、物品入口全局助手true可替代，公共事件内部抽样不计入协调器清单。',
  'R2 B21真实/cases/6 OldRod主动路径资格；R5 M03-007完整原packet、36/41激活范围、33旧span与FS14/16/receiver对照保持。'),
 ('GR6-O-002','R6-U03','P3','WP13 §4.1; R6-EV01–06',
  '局部循环计数先增，>100才Graphics.update再清零；98注释+终止无刷新，99+终止会在清空列表后的第101次开头刷新，100注释先刷新再处理终止。',
  '116返回false让当次退出，下一update局部计数从0；106返回true不能当同一反例。刷新抛错早于计数归零，不附加Input.update，不混同嵌套深度100/101。',
  'WP13与U11跨图主体、私有键/当前图键、脚本接收者和skip分派组合；新的冻结请求位于map/wait检查之前但不改这些身份合同。',
  'GR5-M03-002/007完整原前提、当前/绑定地图及终止解锁；33旧span唯一插入处分段原行保持，新101阈值不扩成通用每帧调度规则。'),
 ('R6-D-LZ-001','R6-U14','P2','WP08 §5.2; LZ36–38',
  '普通脚本的两个反斜线+n在收集后成U+005C/U+000A，运行对应键为U+005C/U+006E；规范化未把字母n转LF。具名接收成功路径已先写库存，再查消息键。',
  '有效两层只有收集键的译文T不保证运行命中；直接运行键命中Q正常。导出取消不切当前语言，完整编译失败前已截断的边界保留。1321另含暂停拼接，不作为相同最小证明。',
  'WP17消息替换在查找之后处理换行/控制符，不能倒补查找；物品/莓果与普通学招各自前缀限定。',
  'R2 A006 B01/B02分期、A013/A018，R3 M01-001/002，R4 M01-001/002，R5 M01-002/003/008/009的默认集合、规范键、单LF/双LF、作者输入副作用保持。'),
 ('R6-D-LZ-002','R6-U14','P3','WP08 §5.1.1; WP15 §2; WP65; LZ39–41',
  '指定图片身份先经过当前语言game/core查找，命中B则B进入资源入口，无命中仍A；有效空译仍是命中。Controls七图片与固定背景分开，Card女性候选先有独立存在门。',
  'B缺失/空译所致结果依各实际加载入口，不保证自动回A或全场景成功。Voltorb只本地化basename再拼路径。48有限原记录为46完整路径+2basename，不声称全部图片入口。',
  'WP15普通包装/直接位图/nil资源失败和Controls分阶段名义时间线相接，文本标签本地化与图片身份各自观察。',
  'R2 C061/C114、R4 M01-002、R5 M01-003/M10-011：资源失败分流、占位参数、双LF、动画创建时钟/全局相位边界保持，无宿主像素证明。'),
 ('R6-D-PBS-C05','R6-U14','P3','WP03 §4.3.1; WP27; WP43; U14-C05-01–05',
  '有限Type/Move/Item构造默认逐项落实；Move省略类别/威力为Status/0并仍经既有交叉检查，Item缺复数名为Unnamed，显式Review/Reviews保留。',
  '原始默认与语言查找后文字分开；份名缺值回普通对应名，已有份名空译不回退。Physical0警告改Status与Status40拒绝分开。',
  'WP43战斗类别公式未改；WP27按槽数量/重要物图标与注册消费保留；编辑器新建字段失配不是PBS普遍丢显式名字。',
  'R5 M01-013/016、M05-006、M12-101原始字段/提示/文件/父Yes/外层No层次保持。'),
 ('R6-D-PBS-C06','R6-U14','P2','WP03 §4.3.2; WP73-B; U14-C06-01–03',
  '已给非零形态部分metrics记录只按自身默认补缺字段：(0,0)/(0,0)/0/0/2；整个记录缺席的查询才克隆基础记录。基础Back(5,6)：部分缺Back得(0,0)、全缺得(5,6)、显式(7,8)保持。',
  '查询建立记录/空后缀、保存时非零记录选择输出后缀路径、等值省略互不等价；档案保存和PBS重新编译分别观察，不广播改变已布局精灵。',
  '编译、布局应用、编辑器refresh惰性查询、save/write链均接合；WP15资源条件与指标逻辑层分开。',
  'R2 C016的仅基础/同后缀/异后缀/等值非零四例；R5 M01-017形态标量Generation/Habitat反写损失保持，不把它们合并为metrics根因。'),
 ('R6-D-PBS-C07','R6-U14','P2','WP18 §3.3; WP30 §2/8; U14-CI01–04/U14-GR01–05',
  '合法非负Happiness256经PBS、Species与关闭Moves/recheck的普通等级5创建原样保留；没有初始255夹限。默认70、显式0/255对照保持。',
  '后续changeHappiness取区间加值并最终夹0..255，是另一入口；正常254 walking+1得255。没有把有限变化方法表泛化到任意超域初值或确保所有后继消费。',
  'U10 NPC装载/尺寸与U01Owner例外组合，生成蛋120/孵化120是具名后继写入，不推翻普通初始256事实。',
  'R2 A021/A022全默认/复检额外随机；R5 M01-006、M04-002与既有值域变化合同保持，未扩编辑器上限成PBS上限。'),
 ('R6-D-DATA-C01','R6-U14','P3','WP03/04; R6-U14-FLAGS01–04',
  '有效特性节显式空Flags重复文本首组仍求值，得到[nil]并登记；省略是[]。查询内首nil.downcase局部失败，安全导航只保护特性记录缺值，不保护内部元素。',
  '只有该特性为唯一非蛋提供者、蛋2步且先行依赖正常时，首次减到1后查询失败，未达额外减/归零/孵化。正常非匹配Flags得false；其它来源/坏数组/宿主退出不扩大。',
  '泛型登记只丢弃真正空数组，不能将[nil]当[]；与WP35动态非蛋扫描相接，WP04/U09缩进注释与既有CSV耗尽门无冲突。',
  'R2 A001精确引号字符；R3 M01-003井号先处理；R5 M01-012定长尾项/首必需枚举、M01-016省略Flags=[]与C01F-016-01保持，104schema导航非运行验收。')
]
findings={'schema':'r6.actual.group-a.independent-nonauthor-adjudication.v1','utc':UTC,
 'reviewer':'/root','source_thread_id':'01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',
 'actual_commit':ACTUAL,'workspace_tree':TREE,'formal_tree':FORMAL,'exact_actual_input':input_binding['input_identity'],
 'evidence_level':'SOURCE_STATIC_AND_DERIVED_VECTOR','reference_execution':0,'behavior_model_execution':0,'host_execution':0,
 'records':[],'required_repairs':[],'INTEGRATED_PASS':'PASS_GROUP_A_SCOPED_STATIC_11_ONLY',
 'formal_acceptance':'NOT_GRANTED','CLOSED':False,'other45IDs':'NO_VERDICT_BY_THIS_REPORT'}
for ID,batch,severity,formal,fact,counter,interfaces,history in records:
    findings['records'].append({'id':ID,'batch':batch,'severity':severity,'disposition':'required','verdict':'PASS',
     'actual_verdict':'ACTUAL_PASS_STATIC','actual_commit':ACTUAL,'workspace_tree':TREE,'formal_tree':FORMAL,
     'groups':{'1_identity_scope':{'canonical_id':ID,'aliases':[],'new_required_ids':[]},
      '2_bidirectional_source_formal':{'actual_formal_and_vectors':formal,'source_fact':fact,'source_locators':'reading-ledger.json; contracts full original seven-group fields'},
      '3_premises_countercontrols_failure':counter,
      '4_minimum_revision':'Fixed required repair is present in actual full composition; no optional, policy or administrative addition required by this review.',
      '5_acceptance_and_historical_regression':history,
      '6_independent_actual_review':{'root_direct':True,'candidate_verdict_inherited':False,'required_repairs':[],'execution':'NOT_EXECUTED'},
      '7_owner_and_interfaces':{'owner':batch,'actual_interfaces':interfaces,'unique_integrator':'R6-I','admin_sync':'Separate subsequent R6-I stage','formal_acceptance':'NOT_GRANTED','CLOSED':False}},
     'required_repairs':[]})
(ROOT/'findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n')
provenance={'schema':'r6.actual.group-a.reviewer-provenance.v1','utc':UTC,'reviewer':'/root',
 'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'default','fast':False},
 'effective':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','reviewer_platform_uuid']},
 'configuration_evidence':'No valid effective echo exposed. User explicitly directs direct review without CLI or extra agent configuration proof.',
 'independence':{'candidate_author':False,'formal_author':False,'prior_U01_reviewer':True,
                 'semantic_final_reviewer':'root only','payload_audit':'Mechanical identity, receipt and extraction only; no semantic verdict delegated'},
 'allowed_branch':'codex/remediation-sixth-actual-a-20261014','allowed_prefix':str(ROOT.relative_to(pathlib.Path('/workspace/pokemon-essentials-clean-room'))),
 'reference_or_model_or_native_host_execution':0,'Mac_operations':0,'CLI_relaunch':0,'force_or_delete_or_main_merge':False}
(ROOT/'reviewer-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
report=r'''# R6 实际整合独立非作者复审：A 组 U01／U03／U14

结论：**11 PASS，0 FAIL，必要修复 0**，均为 **ACTUAL_PASS_STATIC**。本报告授予的独立实际整合结论仅为 **PASS_GROUP_A_SCOPED_STATIC_11_ONLY**；不签另外45项，不授予正式接受或 CLOSED。作者候选 PASS 没有直接继承为本结论。

| 固定绑定 | 对象 |
| --- | --- |
| 最终实际冻结 commit | `86bbc99b28d93db4ed9d6897daf5f3725ccd1808` |
| workspace tree | `67e8c55d520fa8cad2928cb4b95e24c3ed602d5a` |
| 实际 formal tree | `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c` |
| 实际输入 | `integration/U01-U14-final-composite-20261014/actual-review-input.json`；152860 bytes；SHA256 `4671c1c31f18858a7719e88533029d746c62dfb77d4239cbb0cae633e79863da`；blob `ccf79b03165573f27070a417a2e3d986907f6623` |
| 固定准备／main | `469a268b92daed7b4d28d7fd0da75520cbb7228f`／`8ea169fbd0f33f378b5d732fd6bea59e854e04a6` |
| 固定参考 commit／tree | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／`7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 审查分支 | `codex/remediation-sixth-actual-a-20261014`，从最终86bbc99分叉 |
| 唯一新报告写入前缀 | `review/remediation-sixth-20261014-prepare/actual-reviews/group-A/` |

路径均以同一 prepare 前缀为基准。由当前 `/root` 直接审查和逐ID终裁，本人没有撰写或修补候选／正式规格。`/root/payload_audit` 只做完整字节读回、原字段提取、身份／接收核对；不代签语义。请求仍为 **gpt-6.1-sol／ultra／default tier／default speed，Fast=false**。有效 model／effort／tier／speed／本人平台UUID未有可靠回显，实际全部 **UNVERIFIED**；没有CLI重启或额外配置证明任务。原 source thread 仅记录用户给定引用，非本人UUID证明。

## 阅读与证据层级

适用 `AGENTS.md` 已完整读取。U01完整原七组合同／原反证／11份源脚本全文／指定PBS完整SHELLOS记录／历史资格来自本 reviewer 前次直接审读；本次核对相同固定身份后复用其事实，并重新读三项关键源链与最终全文。没有复用旧候选结论。U03、U14完整合同及 original_full_proposal、原独立证据／反证／反向查询／原消费者／原验收和排除限定已实际审读。U14展示视图只对完全相同的身份对象去重，全部语义字段和完整原proposal原样保留。三份原独立候选报告完整读回，并保持原固定对象，不要求它们已经合入最终树。

**22份指定实际正式文件／6066行已逐行阅读**，包括共享文件中其他作者已收到的所有段落和旧测试行，全文身份见 [reading-ledger.json](reading-ledger.json)。大输出显示被截断之处用窄范围重读：WP73-B 74–143、WP08 110–128、WP43 90–96、WP62 95–118、engine目录634–636等均修复；完整原始stdout还在日志中。没有把后台读取的完整字节说成模型已读语义。额外消费者仅对必需交界读具体范围：WP06随机、WP17消息替换、WP33领取、WP35孵化／缓存／动态形态、WP67-A指标／资源接点，不扩大为这些整包的新PASS。

新源阅读覆盖Intl Messages 823行、Type 141、Metrics 101、Ability45、Controls83、Owner73、Validation31、Fishing1–110及Interpreter1–454的完整单位，以及Move/Item/Species默认、两个Compiler的解析／登记／交叉检查、metrics反写与编辑器refresh/save、Pokemon创建／友好／形态提交、DayCare、Pokedex、EggHatching、Bag/UI导航、物品接收、莓果、消息显示、Card、Battle菜单与Voltorb实际消费的必要上下文。新读取源文件及精确范围回执列于ledger；其余完整固定源身份与先前U01可复用范围独立列出。指定二进制和文本有限记录以完整原字节及有界诊断核对，不宣称反序列化整个消息表或全随附语料语义审读。

所有新结论为 **SOURCE_STATIC／DERIVED_VECTOR**。本人81项绑定／覆盖核对、助手217项身份／接收核对是 **TOOL_VALIDATION**，不是行为测试。A组新增设计向量55行（U01 11、U03 17、U14 27）没有运行。原U03七夹具是在既往Ruby2.6.10替身条件下观测源协调器；本次只读完整原Ruby／结果，不重跑、不升级为宿主执行。原K/O运行出处和失败尝试、原二进制会员／字节推导分别保留。本次参考／行为模型／native/UI/Demo／真实存档运行均 **0**，Ruby不可用状态保持。

## 共享整合实际核对

全部14个primary已收到、全局53个正式路径冻结是输入状态与机械事实；本人的完整语义审核范围为A组22份，其中21份实际改动，WP21为受保护原字节全文。26个A组候选白名单文件、31个共享贡献、82个新增／替换块已完整对应到实际对象，所有pending为空。明细见 [payload-audit/shared-composition-complete-metadata.json](payload-audit/shared-composition-complete-metadata.json)，不是只核本组候选mirror与最终文件相同。

| 共享接点 | 本次实际语义结论 |
| --- | --- |
| WP18：U01＋U10＋U14；创建目录：U01＋U14 | Owner有界碰撞例外、NPC／大小来源及初始Happiness256互不覆盖；正常类型域、构造默认、复检额外随机仍有各自前提 |
| WP27：U12＋U14，U01保留上下文 | 名称／份名／复数默认与数量图标、丢弃消息前缀分开；U01迁移规则没有覆盖当前背包导航或正确清旧登记字段 |
| WP10：U01＋U10；内核目录：U01＋U14 | 旧迁移版本资格与U10莓果映射不同根因；MG17–19和LZ36–41同目录完整承接且旧行不被抹去 |
| WP34：U01＋U10；WP62：U01＋U10＋U11；Pokemon目录：U01＋U10 | 同值母系提交与家族/后代/图鉴显式映射、显示入口各自成立；首次last与非空last、生成已见与后继拥有/见过蛋区分清楚 |
| WP13/WP60：U03＋U11；engine目录：U03＋U09＋U11 | 101次刷新及分支抽样没有改写地图身份/私有键/接收者、旧运动与动画合同；所有正文/旧向量全文核对 |
| WP04：U09＋U14；generic02目录：U09＋U14 | 实际第303行合并U14 FLAGS与U09 KL37–50导航句；只删KL36/37间空行、规则体未损失。缩进注释门与空Flags首组不是同一阶段 |
| WP15：U14 | 图片身份语言查找先于资源入口；既有加载失败分流／缓存／音频与时序不改写为统一回退 |

最终9d5b4e9→86bbc99的八份正式变化为U13修复生产者／测试，A组22份字节均未变化。本次仍绑定86bbc99并新读A组完整组合，不以旧快照审核作签名。WP66-A精确receiver已收和U13新producer/QC0/1/3、nil/empty接合属于其他实际组范围，本报告不给它们代签。全局40／53全文的整体验收不是A组声称。

## 逐 ID 实际终裁

以下每项均按原七组：身份／双向证据／具名前提与正常反例及失败／最小修订／验收及历史／非作者终裁／唯一接收者和接口核对。完整机器可读裁定见 [findings.json](findings.json)。

### GR6-K-001 — PASS，required／P3

**身份和事实。** 无别名／新根因。原WP10:88的清旧笼统承诺已修；原WP27:164正确登记字段清旧没有被判错。固定SaveConversions207–230实际复制旧lastpocket并清另一个大小写字段；余三分支转移后清旧，choices克隆。SaveData170–223区分资格与完整／单对象版本写入；普通Bag/UI当前游标由启动／左右导航写入而不清旧浏览字段。

**反例与对照。** 合法旧2／另一字段8／当前3及仍旧版本：首次当前2、另一字段空、旧2保留；导航改5后单对象旧上下文再次回2。尝试“完整链成功便不重复”反证确实排除通常次次重跑，但不能排除直接单对象；尝试“改名只指复制”不能消除后继状态差异。旧值空、当前20/21上下文及完整链成功双版本推进均作对照。无本入口交互取消；晚失败不补事务回滚。

**实际验收与保留。** WP10表／§4.3、MG17–19全文对应源，完整版本链没有被写成默认重跑。WP27/U12/U14组合和U10莓果表无冲突，原其它迁移、MG旧行及保留段不扩审。实际静态PASS，修复0；U01主责，R6-I后续公共同步和正式接受另行办理。

### GR6-K-002 — PASS，required／P2

**身份和事实。** 无别名。Owner19–25／Validation全单位显示同值的后项会覆盖条件，成功才原样四赋值；Owner单字段setter另有独立验证。Pokemon已有Owner原样接收／只验记录类型，不递归复查。WP18 §6.1正常域／§9有界例外与CI29–31已实际收到。

**反例与对照。** 普通整数／文本、无自定义hash/equality：`(0,0,0,2)`和`(1,0,0,2)`接纳整数名字0；`(1,0,1,2)`和`(0,0,1,2)`拒绝，名字只等前项id不能遮蔽条件；正常Valid成功，单字段name=0拒绝并保留Valid。尝试“有校验即四字段皆达类型”“后继创建再次校验”“setter同样例外”均被具体源链排除。失败在赋值前；畸形名字的后继界面／文件成功未被承诺。

**实际验收与保留。** U10 NPC/尺寸及U14友好创建没有冲淡正常Owner语言、外来判据／公开号。R2 B05 A021/A022、B06 A033与CI25–28完整资格保留。只修原必需全称拒绝句，未来容器/API/兼容畸形数据政策未选。实际PASS，修复0；唯一接收R6-I，正式接受/CLOSED尚未授权本review签发。

### GR6-K-003 — PASS，required／P2

**身份和事实。** 原WP34同值无操作已收窄，WP21受保护全文与裸提交/动态读分界不变。默认SHELLOS母系0、HatchSteps5120、母系标志以及无具名handler由完整原PBS记录／完整FormHandlers事实复用。DayCare先建基础蛋、置正步数后显式母系提交；Pokemon159–184始终写形态、清特性、handler、重算、条件注册。Pokedex195–219先求值两缓存、写seen/forms/空last，不写owned/seen-egg。

**反例与对照。** 合法父母／无强制形态、插件、先行错误／player+Dex有效及初始未见、last空：同值0仍是5120步蛋却完成上述缓存与登记。尝试“同值无副作用”“标题仅战斗即防蛋”“后续N0清缓存”“满队取消生成副作用”均无源守卫。缺player/Dex只旁路记录而仍重算，非空last保持；N0不读不清，N>=1循环开始才读、末次PID仍未读，Nature缓存分列。永石第一合格父母顺序和重算／刷新／后继容量失败前缀保持。

**实际验收与保留。** WP34三接点、WP62§3/集合表、BR27–31及全部实际组合一致。WP33生成→容量和WP35核心重写Owner→演出→后写拥有集合不抵消生成seen；U10家族、U11图鉴显示/缓存仍各自有界。R2 A026/A053、R4严格432000/432001、R5M04-002请求1与实际存储0及回调重入保留；不重开已有同值基本规则。实际PASS，修复0，未来蛋登记政策独立。

### GR6-O-001 — PASS，required／P3

**事实与反证。** 原WP60“统一一次随机”已移除。源Fishing1–110四阶段分别由守卫决定：等待域5..10；遭遇存在且未取消才咬钩100；命中咬钩且动画正常后才窗口5..10；有效输入且未自动才上钩100。成功4次、无遭遇/等待取消1、咬钩失败2、超时3、自动成功3；加速无遭遇独立先取8再5的两等待样本。协调器计数+1、正常清理与返回，物品caller另外才战斗统计+1并请求遭遇。

**失败／共享。** R6-FS01–11明确演出失败尚未窗口样本，依赖晚失败不补清理。尝试“固定成功四次可推广所有调用”“自动仍上钩抽样”“直接true即战斗已发生”均被守卫/caller击破。U11公共事件分派保持：Interpreter正常公共事件返回nil继续内置；物品global助手成功true可替代，对该事件内部抽样不声明总数。WP06域、初次活成员能力加速及正常动作清理保持。

**历史与终裁。** 完整原七夹具Ruby／结果只是旧替身证据，本次未运行。R2 B21真实数组/cases/6只限制OldRod主动机会与步进表，非公共助手接收者；R5 M03-007完整原packet与旧FS14/16/receiver保持，33有界旧span另核实际全文。原最小修订全部收到，实际PASS，修复0；U03/R6-I各自职责和admin后继不混同。

### GR6-O-002 — PASS，required／P3

**事实与反证。** Interpreter每次update局部计数从0，循环先加后判`>100`，刷新正常返回才清0。未知注释也占一轮；终止命令正常true且清列表，仍有下一次loop检查。98注释+终止退出前不刷；99+终止的第101轮在清列表后刷新；100注释第101轮先刷再终止。原“99不刷新”提案的撤回／修正保留，未替作者重新恢复错误反例。

**失败与共享。** 116在eventID0也手动推进后false，当次update退出、下次计数重置；106设置wait后true不作为同等假出口。刷新异常发生在归零前，不附加Input.update，depth100/101是另一入口。尝试“100条命令即刷新”“终止后不会循环”“刷新计数是全局帧计数”均被具体控制流否定。WP13原绑定map/当前map、等待与U11脚本接收者/skip合同及101门兼容。

**历史与终裁。** R5 M03-002/007完整原前提和激活36/41仅原scope；33旧span中WP13旧81–94因插入而非连续，旧14行顺序保留，不能用范围hash不同推成丢失规则。R6-EV01–06逐项静态验收，实际PASS，修复0；无新的宿主调度／深度能力或政策必修。

### R6-D-LZ-001 — PASS，required／P2

**事实与反证。** WP08 §5.2和LZ36–38落实普通脚本收集／运行键差异。源两个U+005C接字母n经有限收集顺序变为U+005C+真实LF；运行字符串对应U+005C+n。现有归一化不转换字母n。原记录1154/1162的文本与二进制完整有界字节诊断吻合；1321还有额外暂停控制符拼接，只作补充限制，不冒充同一最小证据。

**对照／消费者。** 有效选定语言game/core只含收集键→T，运行对应键无命中按原文继续；直接运行键→Q命中是正常对照。尝试“窗口之后把n处理成换行可修键”“已有默认键规范化消除差异”“库存消息失败等于未接收”均违反观察时点：具名物品／莓果成功路径先写库存再查找，WP17显示处理在查找之后。只是有界字符串／前缀事实，不声称完整操作顶层失败或补回滚。

**保留与终裁。** 导出目标语言与游戏语言、取消前无写、默认集合替换/追加、game/core优先、单LF/双LF、井号/空行、数组地图门、完整入口预截断与R4同域合并保持。R2A006/A013/A018、R3/R4/R5原精确资格全对读。实际PASS，修复0；剩余全量本地化阅读债不升级本条必要行政或运行门。

### R6-D-LZ-002 — PASS，required／P3

**事实与反证。** 指定Controls七按键图、Card、Battle菜单和Voltorb代表入口先将图片身份当语言键查找。没有译文返回A，有B译文交B到实际资源入口；不翻译固定背景或标签控制字段。Card女性图片存在门发生在其局部候选选择，Voltorb两项是basename后拼路径；48有限原记录／46完整身份＋2basename不是“全图片目录已审”。

**失败与消费。** 尝试“翻译仅影响可见标签”“资源B失败一定再查A”“空译自动原图”“全部入口缺图同结果”分别被具体调用及WP15分流否定。空译命中不回原文；加载nil、直接位图、普通包装各自边界，未承诺整场景成功／清理／像素。WP08 §5.1.1、WP15局部资源段、WP65附表和LZ39–41实际组合齐全。

**历史与终裁。** R2C061加载失败／C114帮助名义时间线、R4占位参数、R5单LF/双LF与strip时钟、正常创建时钟/专用全局相位保持。只添加已被原合同要求的语言资源交界，不追加所有图像资源扫描必修。实际PASS，修复0；无媒体、宿主或默认Demo到达证明。

### R6-D-PBS-C05 — PASS，required／P3

**事实／正常对照。** WP03有限Type/Move/Item默认表、WP27文字/数量消费、WP43类别接点及U14-C05-01–05完整收到。Type图标0/特殊及伪类型false为默认，显式3/true/true保留；Move Status/0/Target None/Function None与已有Type NONE、PP5、命中100分开。Item原始Name/NamePlural Unnamed，不凭显式原名自行产生复数。显式Review/Reviews保留，缺份名回对应普通名，有份名空译继续空。

**反证与边界。** 尝试“最小PBS所有未写属性必需”“省略类别可搭正威力”“默认字面保证所有语言UI”“新建编辑器失配等于PBS丢显式Name”均被原默认/交叉检查和不同生产入口否定。Physical/Special0警告后改Status，Status/缺类别搭40拒绝；先登记记录／尚未保存表的失败前缀保留。WP27按当前槽数、图标遮数、Consumable/Pocket格式门未被新默认泛化。

**历史／终裁。** R5M01-013/016、M05-006和M12-101新建与已有schema编辑、原字段/成功提示/档案/PBS各层合同保持。没有重复计Item已存在的默认根因，也不复制全部私有字段/API。实际PASS，修复0；U14主责、R6-I后续同步仍为另一事件。

### R6-D-PBS-C06 — PASS，required／P2

**事实与成对反例。** Metrics构造按自身缺省填(0,0)/(0,0)/0/0/2，非“逐字段继承基础”。指定基础Back(5,6)，部分非零记录只给Front时Back(0,0)；整个非零记录缺席的查询才克隆基础Back(5,6)；显式Back(7,8)保持。WP03§4.3.2、WP73-B及U14-C06-01–03完整接收。

**消费者／保存。** 尝试“全部非零metrics继承”“查询不可能改变登记集合”“档案保存成功即PBS改写”“记录改变立即广播现有布局”均由query/register、应用到sprite和write_pokemon_metrics291–345及编辑器refresh/save顺序否定。输出路径只来自保存时非零记录的后缀，等值非零虽可省略仍先选出路径；全缺查询建立记录的空后缀与原基记录来源后缀分开。原数据档案重载与PBS再编译有不同观察结果。

**历史／终裁。** R2C016仅基础／同后缀／异后缀／等值非零原完整资格，与R5M01-017 Generation0/None反写省略损失均保留。WP15资源条件与WP67-A已布局/refresh接点无新矛盾；未要求额外刷新架构或新审C005可选布局。实际PASS，修复0。

### R6-D-PBS-C07 — PASS，required／P2

**事实与反例。** Happiness格式是非负而不是初始≤255，Species保留显式256，Pokemon合法等级5创建、Moves=false/recheck=false且无后继改写时原样256。默认70、显式0/255保持。WP18/30与两目录全部U14-CI01–04／GR01–05一致；同创建对照跨目录投影不算重复运行。

**后继界限。** 尝试“正常变化最终夹255等于初始也夹”“编辑器上限等于PBS上限”“产生蛋120推翻普通256”均混同入口。changeHappiness先选0–99/100–199/200–255段、加值后最终夹0..255；254 walking得255的正常例有效，但没有声称任意超域初值在每个方法必正常求值。生成／孵化120、NPC装载钩子与U10来源另有具名后写，不作初始反证。

**历史／终裁。** R2A021完整默认、A022构造复检额外随机与同PID缓存关联，R5M01-006 NPC覆盖、M04-002重入显示均保留。U01Owner构造例外不扩大创建域，WP30变化表没有被错误改成无上限保证。实际PASS，修复0；无真实创建／后继UI运行。

### R6-D-DATA-C01 — PASS，required／P3

**事实与反例。** 合法新Ability仅显式空Flags：`*s`重复模式至少尝试首组，s空项为nil，形成[nil]并登记；遗漏Flags则[]。generic登记对空数组的删除门不适用于含nil数组；has_flag?循环的nil.downcase失败，外层安全导航只保护Ability记录缺值。WP03/04和FLAGS01–04落实正常遗漏／显式空／正常Other／孵化投影。

**已到前缀。** 蛋2步、该坏Flags特性为唯一非蛋扫描提供者、其它依赖正常：首次减1已经完成，查询处异常，额外减／置0／孵化未到。尝试“安全导航保护数组内容”“空属性就是空数组”“先失败就未减步”“任何扫描成员次序同结果”均不成立；因此唯一提供者、实际扫描时点与无更早命中前提保留。异常的外层恢复／进程退出和真实坏数据是否随附仍未知。

**历史／终裁。** R2A001耗尽引号与Other尾对照、R3井号预处理、R5M01-012首必需枚举/定长尾忽略与M01-016 Flags省略=[]、C01F-016-01正常构造保持。U09缩进注释与FLAGS局部schema是不同阶段。104schema导航/登记覆盖不变运行闭合；不把所有Flags/List统一推广。实际PASS，修复0。

## 精确历史与未验证范围

U01前次完整原资格／固定源身份复用有 [payload-audit/prior-U01-source-identity-list-readback.json](payload-audit/prior-U01-source-identity-list-readback.json) 及旧固定review绑定，不以旧PASS代新语义。U03完整两个原packet、closure36/41与真实R2/cases/6／旧named locator对应保留，33旧span按最终全文重新核对。U14完整118资格字段、78原案例前提／正常／反例／失败／排除／unknown逐pointer核原对象；1–117新语义读，118完整activation的同身份事实从前次U01历史读取复用。明细 [payload-audit/U03-verified-full-original-history-fields.json](payload-audit/U03-verified-full-original-history-fields.json)、[U14原资格](payload-audit/U14-verified-full-original-qualification-fields.json)、[U14原案例](payload-audit/U14-verified-full-original-case-fields.json)。这些选中原字段全部保留，不声称32MB历史包全部joins本次语义新读。

R1原WP范围不臆造总数；R2 229/21/341与scoped/partial/deferred原分期；R3 23/76、M09 optional历史U08未启动／M02 no-required；R4当前17/76与B5摘要16/75；R5唯一activation选13fddb候选＋044c348独立报告后92CLOSED/OPEN0，仅其原精确范围。410static/568schema/158额外/21shared/18deps/85writer/262原贡献及6行政transfer/3纠正不算本次行为分母。旧G03/G09 FAIL、U03旧FAIL与定向修复、两advisory MISMATCH、SC-U07-001体内LF错误/纠正以及旧OPEN/WAIT保留历史时点。原optional7／no-required7／政策6／限制13，以及R6政策7／限制14不由本报告关闭；永久兼容选择仍由用户另行裁决。

范围／provenance限制如实列出：初次U03整合同大输出截断的缺口已窄范围重读；read.py错误x参数、working git尚无U03/U14报告、拼错额外消费者路径的失败均保留并使用固定正确对象重读。助手初次默认目录折叠的状态假设、过强全追溯文件保留假设、R2具名locator误作数组下标已纠正，不判候选缺陷；根verify初次误假定旧review报告已在实际树合入，后改为原固定远端对象身份验证。完整原命令exit/stdout/stderr保留，不伪造首次成功。工具输出元数据、相同字节或正常返回不能替代源语义、真实宿主／UI观察。

**接收后继仍未完成于本review。** R6-I应在独立实际组结论收齐后处理原合同必要的planning/feature-matrix与audit/source-traceability同步，随后独立核实际registry／正式接受／CLOSED。最终已有U04追溯13行追加是其他原批写入，并非本review新写或A组返修。这里没有将行政回执、可选文字、政策或未知宿主条件另造11项的必要修复。

报告只在授权group-A前缀新增文件；候选、正式、公共台账/main/tag不改，没有force、删除、main合并或Mac操作。语义core与后继有限publication文件使用真实普通commit/push发布；每个新增路径的模式／类型／tree和完整不同blob均独立远端读回，最终SHA/tree由最终答复／外部receipt绑定，避免递归自哈希。**候选PASS、内容接收、A组实际静态PASS、公共同步、正式接受及CLOSED各为不同事件。**

## 指定全文身份目录

以下22份均已实际全文阅读，完整bytes/SHA256/blob及逐次范围见ledger；附加消费者不混入此全文数。

| 正式文件 | 行数 | 完整blob |
| --- | --- | --- |
'''
for r in ledger['formal_full_reads']:
    report+=f"| `{r['path']}` | {r['lines']} | `{r['identity']['git_blob']}` |\n"
(ROOT/'report.md').write_text(report,encoding='utf-8')
print(json.dumps({'report_bytes':(ROOT/'report.md').stat().st_size,'verdicts':len(records),'required_repairs':0,'utc':UTC},ensure_ascii=False))
