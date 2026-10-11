"""Report assembly only; never executes or changes reference or formal inputs."""
import csv, json, pathlib, datetime

ROOT=pathlib.Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]
OUT=ROOT/'M02'
REF=REPO/'reference/pokemon-essentials'
SRC_COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
SRC_TREE='7589c800b61ba13a13040ed0d686979b80a84fd0'
SPEC_COMMIT='167296dbe9e2384627b0ed696e87aeb01f211252'
SPEC_TREE='33598d8a2a3acdd093cc4fe23f48eea8666100f3'
source={r['path']:r for r in csv.DictReader((ROOT/'reference-file-inventory.tsv').open(),delimiter='\t')}
formal={r['path']:r for r in json.loads((ROOT/'formal-spec-identities.json').read_text())}
def se(path,loci,note):
    return dict(repo='reference',commit=SRC_COMMIT,tree=SRC_TREE,path=path,git_blob=source[path]['git_blob'],loci=loci,note=note)
def pe(name,loci,note):
    path='deliverables/final-specification-set/'+name
    return dict(repo='project',commit=SPEC_COMMIT,tree=SPEC_TREE,path=path,git_blob=formal[path]['git_blob'],loci=loci,note=note)
event='Data/Scripts/003_Game processing/005_Event_Handlers.rb'
collections='Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb'
values='Data/Scripts/002_Save data/002_SaveData_Value.rb'
start='Data/Scripts/003_Game processing/001_StartGame.rb'
saveui='Data/Scripts/016_UI/014_UI_Save.rb'
findings=[
dict(id='GR3-M02-001',severity='P2',status='CONFIRMED',disposition='REQUIRED_REVISION',module='M02',title='通知回调抛错后的停止和部分状态未进入扩展合同',capability='通知失败顺序',category='Generic Kernel',reviewer='/root',source_evidence=[se(event,'40–58;88–90','回调按序直接调用，没有逐回调捕获或回滚'),se(collections,'62–64','命名事件触发沿同一调用路径'),se('Data/Scripts/012_Overworld/001_Overworld.rb','202–218','普通步计数写入先于两个玩家步通知')],spec_evidence=[pe('generic-kernel/wp05-events-extensions-plugins.md','§3.1–3.2;§7','说明依次调用全部，失败表只列插件错误'),pe('test-catalog/generic-kernel-wp05-06-07-08-09-10.md','EP01–EP05','没有回调中断/部分提交对照')],evidence_level='SUPPORTED_STATIC / SOURCE_STATIC_DERIVATION; NOT_EXECUTED',premises=['已登记回调顺序为 A、B、C，A 正常完成，B 抛出异常','无扩展为触发入口补捕获，无更早失败，不讨论并发增删订阅','消费者在触发前或 A 内已有状态写入'],scenarios={'normal':'A/B/C 均正常返回则按序全部执行。','failure':'A 把可见状态从 0 写为 1，B 抛错：C 不执行；状态保留 1，异常传向触发调用者。普通迈步中的计数也已发生，不能当作未迈步。','boundary':'B 位于首位时没有先前回调副作用；B 位于末位时所有前项已发生。调试主流程的外层诊断不是继续本次通知的保证。'},current_vs_expected={'current':'泛称依次调用全部；没有异常导致剩余回调跳过、既有写入保留和触发方中断的合同。','expected':'限定正常完成的全调用保证，并用独立行为文字说明异常传播/停止/无事务撤回及外层处理边界。'},impact='扩展作者和实现团队可能隔离回调错误后继续执行，导致步数、遇敌、孵化或UI消费者顺序与参考不同。',implementation_risk='共享事件链的失败语义不确定，可能重复推进或在已失败的状态上继续推进。',consumers=['M03 世界步进/转移','M06 步数/遭遇/孵化','M10 菜单扩展','M11 野外被动'],historical_relation={'relation':'NEW_SCOPE','notes':'原事件参数/身份/插件控制保持原限定；不是据旧PASS重开原229。'},recommendation='补通知正常/失败/边界合同及测试设计，保留消费者已提交状态；无需规定事件总线或语言异常类型。',acceptance_criteria=['仅凭最终集可确定 A正常、B失败、C被跳过的顺序与状态','说明普通步计数发生在回调异常前，外层捕获不恢复本次调用','新增首项/中项/末项异常与全正常对照；未执行标识保留'],dependencies=['M03/M06/M11 通知消费者交界'],aliases=[],unknowns=['回调在触发期间增删订阅的宿主细节未穷尽，不以此项补写无限事件变体。']),
dict(id='GR3-M02-002',severity='P2',status='CONFIRMED',disposition='REQUIRED_REVISION',module='M02',title='持久值重复身份的保存、读取和撤销语义缺失',capability='持久状态登记碰撞',category='Generic Kernel',reviewer='/root',source_evidence=[se(values,'195–207;220–231;279–283','登记追加而不按ID替换；撤销移除所有同ID；保存后取值覆盖先值；读取依序调用各登记')],spec_evidence=[pe('generic-kernel/wp09-save-startup-continue.md','§3.1','只列单项配置与读值/加载标记，无碰撞行为'),pe('test-catalog/generic-kernel-wp05-06-07-08-09-10.md','SV08–SV11','未给重复登记身份对照')],evidence_level='SUPPORTED_STATIC / SOURCE_STATIC_DERIVATION; NOT_EXECUTED',premises=['动态作者/插件登记两个合法持久值，身份相同，保存值依次为 10 和 20','两项类型约束相容且取值/加载回调均正常，无此前标记跳过','仅分析登记接口，不宣称现有17项默认登记存在重复或缺失插件组合已运行'],scenarios={'normal':'不同身份各自形成保存键并加载一次。','failure':'若同身份两个约束不相容，数据有效性检查要求两者均通过；保存最后值不能自动证明同时满足前者。','boundary':'相同身份两正常登记：保存取值两次、最终键值20；读回同一20时两项加载回调依次各执行一次；撤销该身份移除两项。不是同键后项替换前项的事件/内容登记规则。'},current_vs_expected={'current':'可配置持久值目录没有说明身份碰撞、重复回调和撤销范围。','expected':'给出可观测登记碰撞行为与默认唯一身份范围；独立框架可重设计组织，但兼容策略不得默默套用其它注册表的替换规则。'},impact='插件作者或未来迁移实现可能只保留后项，改变取值副作用、加载先后、有效性判断及卸载结果。',implementation_risk='保存字面看似正常，加载却遗漏或重复处理状态；冲突约束可能使存档不可用。',consumers=['M01 内容身份/注册查询','M02 保存/启动/迁移','M12 作者扩展工具'],historical_relation={'relation':'NEW_NONDEFAULT_REGISTRATION_SCOPE','notes':'现有17默认登记及旧缺键/加载门控制未否定；独立新证据不扩大旧229接受范围。'},recommendation='补架构中立的同身份登记/保存/读取/撤销正常、失败与边界规则；若未来选择拒绝重复身份，列为用户明确的兼容决策。',acceptance_criteria=['10/20同身份向量明确最后保存值、两次取值/加载顺序与撤销全移除','类型约束冲突与已加载门分开说明','不要求复制源容器/类结构，不宣称默认游戏存在重复身份'],dependencies=['M01 登记机制比较','M12 动态扩展范围'],aliases=[],unknowns=['真实插件如何重复登记未有样本。'],user_decision='未来是否拒绝重复身份或保留其兼容行为；本轮只要求先准确登记参考结果。'),
dict(id='GR3-M02-003',severity='P3',status='CONFIRMED',disposition='REQUIRED_REVISION',module='M02',title='无旧存档紧急保存的备份提示未与实际备份状态分开',capability='紧急保存反馈',category='User Interface / Generic Kernel',reviewer='/root',source_evidence=[se(saveui,'1–24','复制备份受旧存档门控制，但成功保存分支恒显示已备份提示')],spec_evidence=[pe('generic-kernel/wp10-migration-failure-recovery.md','§5.2 line127','仅说明旧档已备份在旧档实际存在时成立，没有明确同样提示仍出现'),pe('test-catalog/generic-kernel-wp05-06-07-08-09-10.md','MG07','无旧存档前提未登记恒显示的反馈'),pe('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md','T15','有旧档两提示已给，无旧档成功对照缺失')],evidence_level='SUPPORTED_STATIC / SOURCE_STATIC_DERIVATION; NOT_EXECUTED',premises=['脚本超时进入紧急保存，玩家可保存，开始时默认存档不存在','保存及两条消息调用成功，没有更早异常；无独立已有.bak输入'],scenarios={'normal':'有旧档则先复制备份，保存成功后显示已保存与已备份两提示。','failure':'保存失败进入保存失败提示；未进入成功提示分支。','boundary':'无旧档则跳过复制，保存成功仍显示已保存与已备份两提示；本次并未创建旧档备份。'},current_vs_expected={'current':'规定备份事实成立的条件，但读者无法唯一确定无旧档成功时的实际提示。','expected':'分别记录文件操作事实与恒显示提示；登记这是参考的误导反馈，未来修正与否待用户决定。'},impact='复刻UI、设计测试或解释灾难恢复时可能错误认为出现备份提示即证明备份存在。',implementation_risk='UI回执被用作文件状态证据，造成错误恢复承诺。',consumers=['M10 保存UI','M02 超时/恢复'],historical_relation={'relation':'REFINES_EXISTING_MG07_SCOPE_WITH_NEW_UI_EVIDENCE','notes':'保留MG07无旧档也可保存及实际备份门；不改变旧229关闭结论，追加此前未明示的反馈分支。'},recommendation='补无旧档且保存成功的两提示与无新备份文件对照，明确未来是否修正提示为用户选择。',acceptance_criteria=['无旧档成功向量同时给出提示序列和备份操作未执行','不把提示视为备份存在证明','保留有旧档/保存失败/无玩家的分支与未运行限定'],dependencies=['M10 保存UI合同'],aliases=[],unknowns=['真实超时/宿主消息显示未运行。'],user_decision='未来框架是否修正无旧档时的已备份提示；不默认永久复刻该异常。')]
(OUT/'findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n')

families=[
('通知列表与命名事件','Generic Kernel',[event,collections],'wp05-events-extensions-plugins.md','§3;EP01–05','正常按注册顺序；同名替换；参数适配；异常中止与部分写入见001','PARTIAL','GR3-M02-001'),
('内容处理器及菜单扩展','Generic Kernel',[event,collections],'wp05-events-extensions-plugins.md','§3–4;EP03–05','精确键优先/条件回退；处理器校验先于空身份；排序缺省/条件过滤/动态名','SUPPORTED_STATIC','实际菜单业务分别交M10/M12；不保证触发中修改容器的宿主语义'),
('插件元数据与依赖形态','Generic Kernel',['Data/Scripts/001_Technical/005_PluginManager.rb'],'wp05-events-extensions-plugins.md','§5.1;EP06–15','缺键与显式空值、可选精确版本及错误终止不同','SUPPORTED_STATIC','无真实插件样本'),
('插件版本比较及依赖排序','Generic Kernel',['Data/Scripts/001_Technical/005_PluginManager.rb'],'wp05-events-extensions-plugins.md','§5.1–5.2;EP08–12','1.10小于1.9；依赖先行；循环与缺必需依赖终止；Link前提','SUPPORTED_STATIC','不以通常语义版本规则替代；动态组合未运行'),
('插件发现与编译候选','Generic Kernel',['Data/Scripts/001_Technical/005_PluginManager.rb','Data/Scripts/001_Technical/002_Files/001_FileTests.rb'],'wp05-events-extensions-plugins.md','§6.1–6.2;EP18–21','小写.rb路径子串；显式先/自动后首次去重；mtime与手动编译门','SUPPORTED_STATIC','不创建或执行示例插件'),
('预编译插件消费与错误','Generic Kernel',['Data/Scripts/001_Technical/005_PluginManager.rb','Data/Scripts/999_Main/999_Main.rb'],'wp05-events-extensions-plugins.md','§6.3–7;EP16–17','发布模式仍消费；兼容警告非拒绝；脚本求值错误走插件诊断终止','PARTIAL','读/解码损坏产物的宿主行为未穷尽，未作为已执行通过'),
('持久值登记与加载门','Generic Kernel',[values],'wp09-save-startup-continue.md','§3.1;SV08–11','缺键/错型；启动/重置/加载标记；重复身份见002','PARTIAL','GR3-M02-002'),
('17项默认持久单元与新游戏','Generic Kernel',['Data/Scripts/002_Save data/004_Game_SaveValues.rb',start],'wp09-save-startup-continue.md','§3.2;§4.2;SV07','5启动值；设置及系统保留；stats重建后会话1；地图容器无新值','SUPPORTED_STATIC','类型标识为取证数据，不强制未来类结构'),
('启动系统及标题分流','Generic Kernel',[start,'Data/Scripts/999_Main/999_Main.rb','Data/Scripts/016_UI/013_UI_Load.rb'],'wp09-save-startup-continue.md','§4.1;SV01–02','消息→插件→编译→初始化→系统设置→标题；三门仅跳菜单，空/非空决定新/继续','PARTIAL','缺System/Tilesets/CommonEvents/地图资源，不能实际启动或验证场景'),
('继续载入与地图恢复','Engine / Overworld Integration',[start,'Data/Scripts/016_UI/013_UI_Load.rb'],'wp09-save-startup-continue.md','§4.1;SV03–06','magic差异/safesave重设；缺图debug选图、取消退出；nil事件不同空集合','PARTIAL','缺真实地图，静态门确认，运行未证'),
('正常保存成功与失败','Generic Kernel',[start,'Data/Scripts/002_Save data/001_SaveData.rb',values],'wp09-save-startup-continue.md','§5–7;SV10–11','先提交安全标记/计数/时间；取值错型不回退计数；IO只回退计数；打开覆盖后文件未知','SUPPORTED_STATIC','无磁盘故障注入，无原子写入保证'),
('迁移注册、触发、备份和写回','Generic Kernel',['Data/Scripts/002_Save data/003_SaveData_Conversion.rb','Data/Scripts/002_Save data/001_SaveData.rb'],'wp10-migration-failure-recovery.md','§3;MG01–05','引擎族先；阈值低到高；同阈值登记序；默认备份/实际读取路径写回；旧数组默认空表','SUPPORTED_STATIC','旧档样本/宿主反序列化未运行'),
('坏档、递归备份、删除和拒绝','Generic Kernel',['Data/Scripts/016_UI/013_UI_Load.rb','Data/Scripts/002_Save data/001_SaveData.rb',start],'wp10-migration-failure-recovery.md','§5.1','无效返回才递归.bak；读取异常/早期启动值错误不保证进入恢复；拒删退出','SUPPORTED_STATIC','备份链缺实档，删除部分失败只静态'),
('超时与紧急保存','Generic Kernel',[saveui,'Data/Scripts/999_Main/999_Main.rb','Data/Scripts/001_Technical/001_Debugging/003_Errors.rb'],'wp10-migration-failure-recovery.md','§5.2–5.3;MG06–08','无玩家不恢复场景；有旧档先备份；保存成功恒显示两提示；正常到底恢复场景','PARTIAL','GR3-M02-003；真实Hangup/宿主重启未运行'),
('文件遍历、路径、存在和目录删除','Generic Kernel',['Data/Scripts/001_Technical/002_Files/001_FileTests.rb'],'wp07-diagnostics-files-http.md','§3;IO06–07,13–15','排序/本层文件先；删根区别导出保目录；首字节与全文捕获集合不同','SUPPORTED_STATIC','链接/隐藏条目/加密归档宿主未穷尽'),
('内存流与二进制读写辅助','Generic Kernel',['Data/Scripts/001_Technical/002_Files/001_FileTests.rb','Data/Scripts/001_Technical/002_Files/002_FileMixins.rb'],'wp07-diagnostics-files-http.md','§3非详细定义','小端8/16/32位、8位符号/固定索引读；内存流关闭/seek/EOF/短读可读；检索未发现业务消费者','UNRESOLVED','工具辅助能力，实际调用者与未来兼容义务未证；未补造未来I/O API'),
('HTTP基础与便利包装','Generic Kernel',['Data/Scripts/001_Technical/002_Files/003_HTTP_Utilities.rb'],'wp07-diagnostics-files-http.md','§4;IO01–05','GET无协议门/POST只http；非表响应原样；200文件覆盖；请求与写入捕获界不同','PARTIAL','参数编码与宿主协议/网络异常全域未运行，不推外部服务可用'),
('异常格式、日志与主流程处理','Generic Kernel',['Data/Scripts/001_Technical/001_Debugging/003_Errors.rb','Data/Scripts/001_Technical/001_Debugging/001_PBDebug.rb','Data/Scripts/999_Main/999_Main.rb'],'wp07-diagnostics-files-http.md','§5–6;IO08–12','日志先输出后；日志失败会中断；debug超时转重启/nondebug专门打印保存；退出/Reset分支区别插件','SUPPORTED_STATIC','宿主未捕获异常最终表现未知'),
('控制台、调试日志与参数验证','Demo / Developer Experience',['Data/Scripts/001_Technical/001_Debugging/001_PBDebug.rb','Data/Scripts/001_Technical/001_Debugging/002_DebugConsole.rb','Data/Scripts/001_Technical/001_Debugging/004_Validation.rb'],'wp07-diagnostics-files-http.md','§5.2','debug与internal同真日志；刷新清空；转储独立；验证错误聚合；格式化标记支持','PARTIAL','完整控制台排版归M12；宿主终端可见性未运行'),
('弃用直接告警与别名','Generic Kernel',['Data/Scripts/001_Technical/001_Debugging/005_Deprecation.rb'],'wp07-deprecation-appendix.md','§1–8;DP01–05','告警可选版本/建议；别名先警告后位置/关键字转发，块无显式转发；创建失败分层','SUPPORTED_STATIC','核心无别名构造调用，直接消费者存在；动态插件未知'),
('统计、游玩时间与持久性','Generic Kernel',['Data/Scripts/004_Game classes/012_Game_Stats.rb',start,'Data/Scripts/002_Save data/004_Game_SaveValues.rb'],'wp06-time-random-steps-stats.md','§3–4;TM04,08–11,13','74字段初始化含数组；游戏时间读取惰性累加；标题锚点清/载入重建；写入业务分配各模块','PARTIAL','8事件写入缺地图；BP赢取来源未知；未将avg会话或任意负输入推广为支持承诺'),
('通用步数与提前返回','Generic Kernel',['Data/Scripts/012_Overworld/001_Overworld.rb'],'wp06-time-random-steps-stats.md','§4.1;TM12','强制/解释器早退；普通步按2^31回绕，写入先于订阅/菜单遇敌门','SUPPORTED_STATIC','订阅者失败见001；业务步效果分别M06/M11'),
('随机输入、范围与辅助数学','Generic Kernel',['Data/Scripts/001_Technical/002_RubyUtilities.rb'],'wp06-time-random-steps-stats.md','§5;TM05–07','普通上下界、整数Range端点、全局播种/回放分开；lerp零时长与端点；纯辅助布局/色彩','PARTIAL','非整数/非法随机域、跨语言PRNG和未用辅助的兼容义务未证；消费者实际分布逐模块审'),
('临时状态、开关/变量/自开关','Generic Kernel',['Data/Scripts/004_Game classes/001_Switches and Variables/001_Game_Temp.rb','Data/Scripts/004_Game classes/001_Switches and Variables/002_Game_Switches.rb','Data/Scripts/004_Game classes/001_Switches and Variables/003_Game_Variables.rb','Data/Scripts/004_Game classes/001_Switches and Variables/004_Game_SelfSwitches.rb'],'wp09-save-startup-continue.md','§3持久目录；WP13命令消费者','临时flag默认false/0/空；开关未值false、变量nil回0但false保留、自开关仅真返回真；写入上界5000','PARTIAL','负索引/宿主任意脚本身份不作为未来架构要求；消费者由M03/M12核验'),
('低电量通知与延迟BGM守卫','Engine / Overworld Integration',['Data/Scripts/012_Overworld/001_Overworld.rb'],'wp06-time-random-steps-stats.md','帧通知消费者；WP61/15交界','放电且剩余≤600秒优先或≤15%；菜单/战斗/消息/路线/解释器守卫；一次性临时警告；BGM延迟门','PARTIAL','宿主power_state不可得、实际低电量/音频未运行；M03/M11具体合同'),
('宿主窗口/缩放兼容','Engine / Overworld Integration',['Data/Scripts/001_Technical/001_MKXP_Compatibility.rb'],'wp09-save-startup-continue.md','§4启动resize与WP65选项交界','首轮调整分辨率；负factor或4全屏，否则半级缩放；版本不符警告继续','PARTIAL','窗口/字体/渲染资源缺失；M10选项消费者，不强制未来MKXP适配结构'),
]
conversions=[
('v20树果数值身份','v20_fix_planted_berry_numerical_ids','6–8长度数组；未知树果ORAN回退，敷料未知空；字段转换先行'),
('v20树果状态改制','v20_refactor_planted_berries_data','创建→有符号才填充→正常末尾替换；失败未替换；上游归一影响输入'),
('v20跟随数据','v20_refactor_follower_data','旧非空转跟随；旧字段在条件外置空，空数组也变化'),
('v20寄养数据','v20_refactor_day_care_variables','首旧A填两空槽、B无槽；已有新C/空得到C/A；旧字段仍清'),
('v20背包字段','v20_rename_bag_variables','存在旧字段时重命名/复制；缺失跳过；未理想化清理全部旧拼写'),
('v20玩家编号','v20_increment_player_character_id','角色编号增加1'),
('v20图鉴','v20_add_pokedex_records','补计数/见蛋及异色层，已为新形态跳过'),
('v20选项','v20_add_new_default_options','缺取名/送箱设置补0，存在不覆盖'),
('v20天气','v20_fix_default_weather_type','类型0→无天气，其他保持'),
('v20统计','v20_add_stats','只有stats键不存在；浮点N/F、假值回0；读取time影响已有锚点；MG13–16'),
('v20标记','v20_convert_pokemon_markings','各持有者整数转6项；队伍/储存/伙伴/漫游/净化/名人堂/变量范围'),
('v21电话','v21_replace_phone_data','全局对象内部新建但静默调用运行全局；冷启动非空联系人可失败'),
('v21笛子','v21_replace_flute_booleans','设置决定转等级/率旗标；已存在旧旗标转并清'),
('v21碰撞统计','v21_add_bump_stat','未赋/假值补0；已有值保留'),
]
for name,key,behavior in conversions:
    families.append((name,'Generic Kernel',['Data/Scripts/002_Save data/005_Game_SaveConversions.rb'],'wp10-migration-failure-recovery.md','§4 / '+key,behavior,'SUPPORTED_STATIC','单项静态分支；全链可更早失败；旧档/宿主未运行'))
caprows=[]
for i,(name,category,paths,spec,clauses,behavior,status,limits) in enumerate(families,1):
    caprows.append(dict(capability_id=f'M02-C{i:03}',module='M02',category=category,capability=name,source_paths=';'.join(paths),source_loci='完整固定文件中的相应入口/注册；实际已读，分支说明见normal_failure_boundary',spec_paths='deliverables/final-specification-set/generic-kernel/'+spec,spec_clauses=clauses,test_design='原目录 '+clauses+'；新失败向量见finding；全部NOT_EXECUTED',normal_failure_boundary=behavior,status=status,limitations=limits))
def tsv(path,rows):
    with path.open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
tsv(OUT/'capability-coverage.tsv',caprows)
files=json.loads((OUT/'assigned-files.json').read_text())
file_rows=[]
for row in files:
    relevant=[x for x in caprows if row['path'] in x['source_paths'].split(';')]
    file_rows.append(dict(source_path=row['path'],git_blob=row['git_blob'],category=';'.join(sorted(set(x['category'] for x in relevant))),read_scope='FULL_TEXT_READ; actual root source reading; callers/branches as capability rows; no execution',status='SUPPORTED_STATIC' if all(x['status']=='SUPPORTED_STATIC' for x in relevant) else 'PARTIAL',capability_ids=';'.join(x['capability_id'] for x in relevant),limitations=';'.join(sorted(set(x['limitations'] for x in relevant)))))
for path in ['Data/Scripts/016_UI/013_UI_Load.rb',saveui]:
    relevant=[x for x in caprows if path in x['source_paths'].split(';')]
    file_rows.append(dict(source_path=path,git_blob=source[path]['git_blob'],category='User Interface / Generic Kernel',read_scope='UI_Load FULL; UI_Save emergency entry lines1–24 and cross-consumer only',status='PARTIAL',capability_ids=';'.join(x['capability_id'] for x in relevant),limitations='M10主责其完整UI；root只核启动/保存交界'))
tsv(OUT/'file-coverage.tsv',file_rows)
specrows=[]
for row in json.loads((OUT/'assigned-specs.json').read_text()):
    path=row['path'];name=pathlib.Path(path).name;text=(REPO/path).read_text();lines=text.splitlines()
    relevant=[x for x in caprows if x['spec_paths']==path]
    if 'stats-directory' in name:relevant=[x for x in caprows if '统计' in x['capability']]
    if '/test-catalog/' in path:relevant=caprows
    for lineno,line in enumerate(lines,1):
        isheading=line.startswith('#')
        istable=line.startswith('| ') and not line.startswith('| ---') and '输入／前提' not in line and not line.startswith('| 字段 |')
        if not (isheading or istable):continue
        clause=f'line {lineno}: '+line.split('|')[1].strip() if istable else f'line {lineno}: '+line.lstrip('#').strip()
        status='SUPPORTED_STATIC';limit='静态机制/具名输入条件；来源定位不证明调用可达或运行。'
        if '/test-catalog/' in path and istable:
            key=line.split('|')[1].strip()
            if key.startswith('LZ'):status='PARTIAL';limit='M01主责；root读有效控制/接口关系，不签本地化全行为'
            if key.startswith('TM') and key not in ['TM04','TM08','TM12']:status='PARTIAL';limit='M03/M05/M06/M09/M11业务消费者及交界共同支持，非root全业务复审'
            if key=='MG07':status='PARTIAL';limit='GR3-M02-003 反馈需补充'
        if name.startswith('wp06-stats') and istable:status='PARTIAL';limit='字段初始化已核；各业务更新语义分别所属模块，8缺地图事件与BP来源未知保留'
        if name.startswith('wp05') and ('3.1' in clause or '7.' in clause):status='PARTIAL';limit='GR3-M02-001 通知异常缺口'
        if name.startswith('wp09') and '3.1' in clause:status='PARTIAL';limit='GR3-M02-002 重复登记缺口'
        if name.startswith('wp10') and '5.2' in clause:status='PARTIAL';limit='GR3-M02-003 UI回执与文件事实'
        if '未决' in clause or '未验证' in clause:status='UNRESOLVED';limit='正文明确保留的旧样本/宿主/动态插件/运行未知，未由本轮静态读取解除。'
        specrows.append(dict(spec_path=path,clause=clause,source_paths=';'.join(sorted(set(p for x in relevant for p in x['source_paths'].split(';')))),source_loci='对应完整静态入口/目录；细分见capability-coverage.tsv',status=status,test_design='本文件具名目录及关联finding；NOT_EXECUTED',limitations=limit))
tsv(OUT/'spec-coverage.tsv',specrows)
controls=json.loads((OUT/'regression-controls.json').read_text())
f1=json.loads((REPO/'review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/all229-dispositions.json').read_text())
f1index={r['id']:(i,r) for i,r in enumerate(f1['records'])}
records=[]
for x in controls:
    i,h=f1index[x['id']]
    records.append(dict(id=x['id'],reviewer='/root',actual_read_scope='完整approved有效前提/反例/minimum/recheck/root和extension裁决字段；FINAL1相应正常/反向/部分失败/限定字段；当前M02正文/案例与源入口；跨域root/extension由相应模块归属审查',historical_reuse={'commit':'c2bc1a341ba6acdf7c8c111dc88d39a162a093d6','path':'review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/all229-dispositions.json','pointer':f'/records/{i}','basis':'131正式字节全一致+完整有效前提不变；不转移签名、不新执行案例'},current_paths=[r['path'] for r in json.loads((OUT/'assigned-specs.json').read_text())],judgment='QUALIFIED_HISTORICAL_STATIC_EVIDENCE_REUSED_WITH_CURRENT_M02_RECHECK',normal_reverse_partial_failure=h.get('normal_reverse_partial_failure_review',h.get('normal_reverse_partial_failure',{'normal':h.get('normal_static_judgment'),'reverse':h.get('reverse_and_neighbor_static_judgment'),'partial':h.get('partial_failure_and_specific_limits')})),scope_limits='其他领域/共享根因不据M02单签全ID；0运行；已关闭原账不改变',new_findings_relation=['GR3-M02-003'] if x['id']=='GIR-FD82-C003' else []))
(OUT/'regression-review.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(OUT/'junction-review.md').write_text('''# M02交界实质审查

独立主角色 /root；固定源/规格身份见baseline与各证据条目；全部静态，运行=0。

| 链 | 正常 | 失败/边界 | 判定 |
|---|---|---|---|
| 插件→编译→初始化→启动值→UI | 主流程严格此序；发布仍消费预编译插件；17默认值中5启动加载 | 插件脚本错误终止；系统早期读值/转换异常可能早于备份UI；读失败不同空产物 | SUPPORTED_STATIC，真实插件/宿主未知 |
| 保存→个体/世界→读档 | 保存对象各领域持久单元；新游戏设置/system保留、stats重建后1 | SaveData取值错型未开文件；IO只回退save_count；场景恢复无兜底 | SUPPORTED_STATIC；源对象结构仅取证 |
| 迁移→备份→写回 | 引擎族先/阈值有序，预转换默认.bak，写回实际读取路径 | 旧数组17默认映射空表；.bak作为来源可能被同名备份/写回覆盖；电话全局早期未载入和寄养同对象异常不理想化 | SUPPORTED_STATIC；旧档与宿主未运行 |
| 世界步→通知→遭遇/孵化/野外 | 普通步先2^31回绕，再玩家步与可转移步；事件/菜单仅后战斗门 | 强制路线/解释器早退不累计；共享handled挡战斗；中途回调异常不执行后项且计数已写 | PARTIAL，GR3-M02-001；M03/M06/M11共同消费者 |
| 语言菜单→消息与存档 | 有非空数据直接改选项并写档，无数据不写；不经普通保存 | 先切语言后写入异常不保证回滚；M01负责导出/导入和格式失败 | SUPPORTED_STATIC交界，不签全部翻译 |
| 超时→UI确认→备份/存档 | 旧档存在才先复制；保存成功走两条提示 | 无旧档成功仍提示备份，但复制未发生；无玩家不恢复scene；保存失败另提示 | PARTIAL，GR3-M02-003；M10须共同核 |
| 登记身份→持久状态加载 | 不同身份保存/加载独立 | 同身份保留两注册、保存后值覆盖、两加载及全撤销不同于内容/事件注册后项替换 | PARTIAL，GR3-M02-002；M01/M12兼容边界 |

源文件001_Overworld额外地图/音频/伙伴/赠物入口均实际阅读并归M03/M05/M11消费者；不把一个主责文件归属当作排除其它模块。
''')
(OUT/'report.md').write_text(f'''# M02 通用运行与生命周期独立评审

执行范围完成：COMPLETED_STATIC_WITH_LIMITS，不是运行PASS。实际reviewer为新独立主角色 /root，主会话入口 codex://threads/01a12bbf-9300-7833-82d7-d392ae9fa731；未参与受审正式作者/登记。模型请求 sol/ultra/Standard，回显UNVERIFIED，不绕过UI拒绝。固定身份见baseline。

独立实读全部26分配源文件及8份正式材料，追加UI_Load完整和UI_Save紧急保存入口；读取相关主流程、事件、save值、迁移14分支、诊断/HTTP/文件/时间/统计/随机/临时状态及跨域调用者。能力分母为{len(caprows)}个行为族/有界迁移分支，{len(file_rows)}份文件范围记录，{len(specrows)}个反向条款/表行导航。计数不是语义证明；具体正常/失败/边界在矩阵与finding。

发现3项：GR3-M02-001 P2通知异常部分提交；002 P2持久值登记碰撞；003 P3无旧档紧急保存的提示与备份事实。未修任何规格。未来是否拒绝重复身份/修正误导提示留用户决定，准确记录参考与验收向量是建议修订任务。

保存/迁移主要合同具备顺序、单位、缺键/错型、零值回退、启动/继续、备份目标及部分失败；原控制13项按完整有效前提、反例、最低修订/复核和FINAL限定复用，相关当前源/正文另核。跨域C003/C007扩展不能由M02一项替代其它模块审查；完整原229及341映射由主角色整合。旧CLOSED保持原义，原证据签名不转移。

辅助流二进制/未用工具、负索引/非法类型、任意参数编码、宿主power/窗口/终端、损坏插件产物、真实旧档/地图资源保留UNRESOLVED/PARTIAL；不强制未来复制内部包装类。统计所有74初始化可核，领域写入由所属模块支持，8事件缺资源与BP来源不虚构。无源片段进入本报告，允许独立架构设计。

运行观察/参考执行/行为向量/静态案例执行/真实Demo链均0。自身Python仅组装审查记录，不运行源或案例。下一步是交界整合与总报告，不是整改。
''')
print(json.dumps({'module':'M02','capabilities':len(caprows),'file_records':len(file_rows),'spec_records':len(specrows),'regression_controls':len(records),'findings':len(findings)},ensure_ascii=False))
