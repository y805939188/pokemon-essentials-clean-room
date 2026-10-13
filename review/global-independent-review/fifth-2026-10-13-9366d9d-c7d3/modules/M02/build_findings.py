from record import *
S='Data/Scripts/'
def sa(path,lo,hi,symbol,fact,caller='',config='fixed R; no plugin override'):
 return {'path':S+path,'version':RV,'lines':[lo,hi],'symbol_or_data_keys':symbol,'caller':caller,'config':config,'supporting_fact':fact}
def sp(file,lo,hi,section,wording):
 return {'path':F+file,'version':B,'lines':[lo,hi],'section_or_vector':section,'current_wording':wording}
def finding(num,title,severity,category,src,specs,expected,current,gap,premises,counter,normal,boundary,impact,negative,change,criteria,deps,caps,root,shared,confidence='high for source facts; medium for mandatory extraction scope'):
 base=json.loads((P/'findings.json').read_text())
 item={'id':f'GR5-M02-{num:03d}','title':title,'module':'M02','severity':severity,'disposition':'unresolved','status':'candidate_pending_independent_counterevidence','reviewer':'M02 independent reviewer; requested gpt-6-astra/ultra/default, actual echo UNVERIFIED','category':category,'source_baseline':base['source_baseline'],'specification_baseline':base['specification_baseline'],'source_anchors':src,'spec_anchors':specs,'expected_reference_behavior':expected,'current_spec_behavior':current,'gap':gap,'preconditions':premises,'minimal_counterexample':counter,'normal_case':normal,'failure_or_boundary_case':boundary,'impact_on_independent_implementation':impact,'negative_evidence_search':negative,'proposed_spec_change':change,'affected_files':list(dict.fromkeys(x['path'] for x in specs if '/generic-kernel/' in x['path'] or '/test-catalog/generic-kernel-' in x['path'])),'shared_contracts':shared,'acceptance_criteria':{'static':criteria,'must_execute':[],'execution_boundary':'Static revision can be checked without reference/model/host execution. Any later experiment requires a purpose/input/version/command/side-effect proposal to the parent session.'},'dependencies':deps,'related_capabilities':caps,'related_findings':[],'root_cause_group':root,'priority':severity,'batch_owner':'M02; parent owns final counterevidence, deduplication and disposition','history_links':{'relation':'new scoped candidate; not a reopening of GR3-M02-003','GR3-M02-003':'NO_REQUIRED retained','historical_PASS_used_as_evidence':False},'evidence_level':['SOURCE_STATIC','CURRENT_SPEC_STATIC','DERIVED_COUNTEREXAMPLE_NOT_EXECUTED'],'execution_status':'NOT_EXECUTED_THIS_REVIEW','confidence':confidence,'unknowns':['Host runtime and real save/plugin/demo behavior not executed; missing archive/map/plugin materials remain unavailable.','Independent parent counterevidence and final required/optional decision pending.'],'excluded_claims':['No reference defect is repaired or automatically made mandatory future compatibility policy.','No new architecture, class hierarchy, production API, runtime success, or complete foreign-module review is claimed.'],'user_decision_needed':'No decision needed to finish this review; any future preservation/correction policy is separate.','review_resolution':{'local_analysis':'source and named current-contract counterevidence reviewed','recommendation':'consider specification revision after independent counterevidence','final_required_revision_signed':False,'next_owner':'parent review session'}}
 mutate('findings','findings',item,'id')
T='test-catalog/generic-kernel-wp05-06-07-08-09-10.md'
finding(1,'持久开关与变量的空值、假值和直接访问边界尚无完整合同','P2','Generic Kernel / persistent state',[
 sa('004_Game classes/001_Switches and Variables/002_Game_Switches.rb',7,25,'initialize, [], []=','空或假存值读成false；其余值原样，只有5000上界，没有布尔约束或自动地图刷新'),
 sa('004_Game classes/001_Switches and Variables/003_Game_Variables.rb',7,25,'initialize, [], []=','nil/缺失读0，false可保存并原样读回；写入超5000忽略'),
 sa('004_Game classes/001_Switches and Variables/004_Game_SelfSwitches.rb',7,24,'initialize, [], []=','读取比较存值与true；数字0/文本等真值不变成true'),
 sa('019_Utilities/001_Utilities.rb',509,520,'pbGet, pbSet','便利写入拒绝缺号/负号并请求地图刷新，与原始存值写入不同'),
 sa('002_Save data/004_Game_SaveValues.rb',35,54,'switches, variables, self_switches','三类作为独立持久值保存并有新游戏初值')],[
 sp('generic-kernel/wp09-save-startup-continue.md',59,81,'§3.2 三持久值行','只登记类型/新游戏值/保存归属，字段语义交领域规格'),
 sp('demo-dx/wp72-debug-contexts-and-controls.md',62,66,'§4.2','说明上界ID≤5000及调试编辑，但未给三种原始读值归一的区别'),
 sp('engine-overworld/wp13-interpreter-command-matrix.md',41,44,'121–124','命令置ON/OFF、变量运算和计时器；不是原始存值读写合同'),
 sp(T,159,175,'SV01–SV17','覆盖持久值登记而未覆盖三个已登记状态单元的读取区别')],
 '合法非负槽可存不同值：普通变量nil/缺失读0而false保留；普通开关nil/false读false、其他真值原样；持久自开关仅存值等于true时读true。原始写入不自动刷新地图，便利写入另有刷新门；5000可写、5001忽略。',
 '持久化身份、初值存在与5000上界已被多个当前合同覆盖；空/假值区别、开关非布尔值读取、自开关严格真值、原始写入和便利写入副作用尚未合成有界合同。',
 '独立实现只能得知三个持久容器被保存，不能仅凭当前合同唯一确定false与nil存值后的读取结果。',
 ['固定R默认脚本，无覆写，相关对象已建立；仅使用普通整数槽和nil/false/true/数值0等原始值。','排除自定义相等运算、负数组索引宿主差异及错误输入类型；地图刷新调用本身正常。'],
 {'input':'分别向同一有效游戏变量槽写false和nil后读取（独立复位）。','reference':'false例返回false；nil例返回数字0。','contract_gap':'WP09只登记Game_Variables类型，WP72仅写编辑范围/上界，未限定这两个不同结果。'},
 '槽1写整数7读7；开关写true读true；自开关写true读true；三对象仍按WP09保存。',
 '普通开关写数值0读数值0；同键自开关写0读false。槽5001写入不保留；原始写入没有pbSet的刷新请求。',
 '以通用truthy/falsy回退或统一布尔强制实现三类状态会改变脚本条件、计时变量和保存后的读取结果。',
 {'search_record':'negative-search.json#persistent_stores','actually_read':[{'path':F+'generic-kernel/wp09-save-startup-continue.md','ranges':'1–163; all registration table and SV mappings'},{'path':F+'demo-dx/wp72-debug-contexts-and-controls.md','ranges':'62–66'},{'path':F+'engine-overworld/wp13-interpreter-command-matrix.md','ranges':'10–45,136–140'},{'path':F+'engine-overworld/wp13-map-events-npc-followers.md','ranges':'26–64,94–106'},{'path':F+'pokemon-rules/wp70-lottery.md','ranges':'variable-boundary clause 44 (read next before finalization)'},{'path':'specs/kernel/wp09-save-startup-continue.md','ranges':'1–199'}],'result':'5000上界有反证，撤回其缺失主张；命令/彩票/调试合同未替代三类值的nil/false/strict-true区别。'},
 '在持久状态合同增加独立值语义小表及原始/便利访问分层；仅记录兼容观察，不规定容器或语言API。',
 ['给nil/false/true/0四个独立读值对照，并区分普通变量、开关和自开关。','保留5000/5001既有合同；区分原始写入与便利写入的地图刷新。','测试不得将单元值类型语义与SaveData登记级类型校验混淆。'],
 ['WP09持久值登记','WP13事件条件','WP72调试变量','WP06变量墙钟计时'],['M02-PERSISTENT-STORES'],'M02-persistent-store-value-contract',['KERNEL-PERSISTENT-VALUES','KERNEL-VARIABLE-ACCESS'])
finding(2,'条件处理器的单项移除与整体清空缺少不同状态结果','P3','Generic Kernel / extensions',[
 sa('003_Game processing/005_Event_Handlers.rb',148,197,'HandlerHashSymbol lookup/addIf/remove/clear/trigger','单项remove只删除精确身份登记；条件登记仍在；clear删除精确与条件两类'),
 sa('003_Game processing/005_Event_Handlers.rb',285,298,'content-specific handlers','物种/特性/道具/招式共用该行为')],[
 sp('generic-kernel/wp05-events-extensions-plugins.md',24,39,'§3.1–3.2','符号处理器列注册/归一/条件回退/触发，未列条件生命周期；命名事件的按键移除不等同此表'),
 sp('creature-rpg/wp28-item-use-and-training.md',32,67,'§2、§3.1','精确优先、条件首命中和复制已解析结果已有，未说明移除不影响条件组'),
 sp(T,9,13,'EP01–EP05','现有替换/空身份/字符串键向量无移除与clear对照')],
 '已有条件组G覆盖身份X时，移除G或仅移除X的精确登记不会注销G；X仍可匹配条件效果。整体清空才同时移除条件组与精确登记。',
 '当前合同可重建查询优先级，但无法确定一般“移除”是否也撤销同名条件登记。',
 '两种删除动作实际效果不同；动态作者扩展可能把移除条件身份误当作注销条件规则。',
 ['使用当前符号处理器，条件G对X恒真、处理器正常，触发期间不动态修改注册。','只调用已存在的注册、remove与clear能力；无插件改写这些原语。'],
 {'input':'只登记条件组G→处理器C，条件对X为真；调用移除G，再触发X。','reference':'C仍执行；该移除没有修改条件组。'},
 'X有精确处理器D时优先D；移除X后回落到仍存在的C。',
 '整体清空后X不再命中；不同于移除G。复制条件已解析结果已有WP28合同，本项不重复申请复制语义修订。',
 '将条件与精确注册统一按身份删除会改变插件覆盖/撤销后的可见效果与规则选择。',
 {'search_record':'negative-search.json#conditional_lifecycle','actually_read':[{'path':F+'generic-kernel/wp05-events-extensions-plugins.md','ranges':'1–141'},{'path':'specs/kernel/wp05-events-extensions-plugins.md','ranges':'1–198'},{'path':F+'creature-rpg/wp28-item-use-and-training.md','ranges':'32–67'},{'path':F+'pokemon-rules/wp21-dynamic-forms-and-display.md','ranges':'256–302'},{'path':F+T,'ranges':'1–36'}],'result':'WP28已覆盖复制的条件解析，WP21已覆盖共享处理器；均不能反证单项移除仍留条件组。其它宽词命中属于队伍/地图/动画删除，不作为本原语合同。'},
 '以行为表补精确覆盖、移除精确、移除条件组同名键、整体清空的结果；保留可扩展行为身份，不规定表或类组织。',
 ['X先精确D、删除精确后条件C的对照明确。','只删条件组同名键仍命中C，整体清空后不命中。','不把命名事件删除合同套给内容条件处理器。'],
 ['WP05内容处理器','WP28道具条件消费者'],['M02-CONDITIONAL-HANDLERS'],'M02-conditional-handler-removal',['KERNEL-HANDLER-SELECTION'])
finding(3,'归档内存读取流的定位、末尾和关闭语义没有可复核合同','P2','Generic Kernel / file access',[
 sa('001_Technical/002_Files/001_FileTests.rb',292,311,'pbRgssOpen','归档分支把宿主读取内容交给内存读取对象；块形式用其ensure关闭；非块形式返回对象'),
 sa('001_Technical/002_Files/001_FileTests.rb',366,484,'StringInput seek/eof/read/gets/getc/close/open','尾相对定位用长度减偏移；EOF在内部位置大于长度时为真；整读末尾先空串随后nil；已关闭操作报错；块形式最终关闭'),
 sa('018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb',142,144,'pbPlayBattleFromFile','回放调用者用归档感知打开及全文读取'),
 sa('001_Technical/003_Intl_Messages.rb',531,545,'load_default_messages','消息读取也消费打开后的读取能力，M01仅作为消费者投影')],[
 sp('generic-kernel/wp07-diagnostics-files-http.md',29,39,'§3.2','归档打开仅“打开文件”、路径分支与失败未逐分支验证，未给返回流的可观察读/定位/关闭'),
 sp('generic-kernel/wp07-diagnostics-files-http.md',136,143,'§10','把归档打开失败分支列为未验证；无归档材料不妨碍当前可读实现的条件语义提取'),
 sp(T,74,98,'IO01–IO20','没有归档内存流与本地文件流的边界对照')],
 '限定宿主返回ASCII内容ABC、流成功建立：末尾相对偏移1定位到C，读1得到C；定位到长度位置本身尚非EOF，首次整读返回空串并置EOF，再整读返回空值。块关闭在退出时执行，已关闭再关闭/读/定位会失败。',
 '已说明归档/非归档路径与一字节/全文包装的捕获集合，但没有打开所得读取能力的状态合同。',
 '可得源码中的读取状态机被归入归档未验证，无法区分可静态判定的流语义与需要真实归档/宿主验证的部分。',
 ['归档路径分支已进入，宿主原始读取成功返回给定ASCII内容；只审返回读取对象，不真实加载归档。','有效整数位置/长度，无插件覆写；不外推非ASCII字符单位、宿主序列化器内部行为或普通磁盘File的等价性。'],
 {'input':'长度3的ABC；末尾相对偏移1，然后读取1。','reference':'定位到位置2并读取C；不是通常尾位置加正偏移的结果。'},
 '新流全文读取ABC，随后EOF为真；正常块退出关闭流。',
 '定位到位置3后EOF仍假；整读一次为空串，下一次为空值。块体自行关闭后，退出清理再次关闭可产生关闭错误，不能承诺完全透明的File等价。',
 '未来资源读取或工具兼容若直接采用常规流末尾偏移/EOF约定，可能改变脚本侧读取得到的内容及错误传播。',
 {'search_record':'negative-search.json#archive_stream','actually_read':[{'path':F+'generic-kernel/wp07-diagnostics-files-http.md','ranges':'1–143'},{'path':'specs/kernel/wp07-diagnostics-files-http.md','ranges':'1–184'},{'path':F+'engine-overworld/wp15-resource-matching-and-audio.md','ranges':'20–48,115–163'},{'path':F+'combat-requirements/wp58-battle-recording-and-playback.md','ranges':'25–62,87–116,135–147'},{'path':F+T,'ranges':'70–109'}],'result':'未定位流生命周期/定位/EOF合同；广义EOF正则误命中HallOfFame与文件名说明，已排除。WP15资源存在性与WP58录像字节结构不等价于读取流状态。'},
 '在WP07增加条件式归档读取状态合同，或明确选择不要求兼容该作者侧行为并登记排除理由；分开SOURCE_STATIC和真实归档材料缺失，不要求复刻StringInput类。',
 ['用ABC输入说明初始读取、尾偏移、恰末尾、再次整读与关闭后行为。','块式正常/异常退出关闭和本地分支责任区别清楚。','不把静态给定内容测试称为真实归档/宿主序列化测试。'],
 ['WP07归档打开','WP58回放文件读取','WP08消息读取M01'],['M02-ARCHIVE-STREAM'],'M02-archive-stream-state-contract',['KERNEL-FILE-ACCESS','KERNEL-ARCHIVE-READ'])
finding(4,'旧树果身份映射与数组形态迁移只列名称，缺少完整兼容输入输出','P2','Generic Kernel / migration with Pokémon Rules data',[
 sa('002_Save data/005_Game_SaveConversions.rb',6,97,'v20_fix_planted_berry_numerical_ids; IDs389–452 and mulch59–62','仅6–8元素数组；64树果与4敷料身份表；未知树果回退ORAN，未知敷料可空；符号保留'),
 sa('002_Save data/005_Game_SaveConversions.rb',101,141,'v20_refactor_planted_berries_data','6元素与7/8元素选择不同机制及字段输入；旧时间按阶段×配置小时×3600；合法填充后替换'),
 sa('012_Overworld/006_Overworld_BerryPlants.rb',1,33,'BerryPlantData initialize/reset','新对象字段初值，为跳过填充分支提供确定输出')],[
 sp('generic-kernel/wp10-migration-failure-recovery.md',78,99,'§4 两树果转换行','写“完整映射表”但未提供各旧数值到当前身份；第二行只说明创建/填充/替换顺序'),
 sp('pokemon-rules/wp60-berry-plants.md',20,50,'§3 当前字段/重置/内容输入','提供当前领域字段，未给旧6/7/8元素布局和数字身份兼容映射'),
 sp(T,177,196,'MG01–MG16','迁移机制及寄养/电话/帧数已覆盖，没有上述数据转换向量')],
 '引擎阈值20下，合格旧数组先归一身份，再按6或7/8元素解释为旧或新植物状态；每个旧数值身份及每个保留字段具有确定映射。长度不在6–8之外不进入第一转换；未知数字树果和敷料有不同回退。',
 '合同宣称当前14个转换及前提/输出目录，但这两个转换缺实际映射表、旧布局字段到新领域量的对应和身份转换精确长度门。当前植物字段表不能重建旧输入。',
 '这是固定可读兼容数据与数学规则的缺失，不是旧存档真实运行未验证本身。',
 ['固定v20两转换已被选中且此前转换无失败；给定可处理全局事件变量与合法树果内容定义。','使用旧表中的合法身份；只推导这两项的输入输出，不声称整条迁移链或真实存档一定成功。'],
 {'input':'一个6元素旧植物记录，树果数值身份389、阶段2、配置每阶段3小时，其余旧字段合法。','reference':'第一转换身份为CHERIBERRY；第二转换为旧机制，存活秒数21600，并按旧槽位保留更新时间/浇水/重植状态。','contract_gap':'仅“完整映射表/按条件填充”不能独立算出389的目标或21600。'},
 '8元素记录中合法数值树果与敷料先归一，再保留新机制的存活时间、水分、产量惩罚与重植数。',
 '长度5或9记录不进身份转换；未知数字树果回退ORANBERRY，未知数字敷料无相同ORAN回退；单项非符号填充跳过仍到末尾替换，现有正确顺序须保留。',
 '独立实现旧存档兼容时无法重建种植品种、肥料、成长时间与浇水/水分状态，只能回读参考或自行猜测。',
 {'search_record':'negative-search.json#legacy_berry_mapping','actually_read':[{'path':F+'generic-kernel/wp10-migration-failure-recovery.md','ranges':'1–175; all 14 conversion rows'},{'path':'specs/kernel/wp10-migration-failure-recovery.md','ranges':'1–229'},{'path':F+'pokemon-rules/wp60-berry-plants.md','ranges':'1–197'},{'path':F+T,'ranges':'177–206'},{'path':'audit/source-traceability.md','ranges':'458–469'}],'result':'树果现行字段及转换源导航都已读；未提供旧数值表或旧数组布局。6/7/8其它命中是地牢/配置/天气，不是迁移表。source路径审计不是独立行为数据附表。'},
 '增加净化兼容数据附表：旧身份映射、6/7/8输入形态到领域量、长度/符号/未知值门和先归一后重建次序；保留两项分开与完整链前提。只要求记录事实，未来是否支持旧格式另定。',
 ['64树果/4敷料表成员和映射经静态数据核对，自动计数只作辅助。','6/7/8布局及旧阶段小时换秒完整可独立推导。','增加合法数值/已符号/未知数值、5/6/7/8/9长度和单项/整链独立向量。','不能用缺旧档样本替代已可读映射；真实存档往返仍NOT_EXECUTED。'],
 ['WP10迁移选择与顺序','WP60植物字段','WP03树果数据查询','WP09全局元数据'],['M02-MIGRATION-BERRY'],'M02-legacy-berry-input-output-data',['KERNEL-SAVE-MIGRATION','CREATURE-PLANT-PERSISTENCE'])
finding(5,'关键段包装的完成状态与调试主入口收尾尚未明确','P3','Generic Kernel / failure propagation',[
 sa('001_Technical/001_Debugging/003_Errors.rb',76,94,'pbCriticalCode','正常返回完成标记1；一般异常报告成功后返回0；Reset/SystemExit重抛；Hangup转Reset'),
 sa('999_Main/999_Main.rb',16,60,'mainFunction/mainFunctionDebug/top-level loop','调试主入口忽略关键段返回值，正常走出该调用后恒返1；外层循环据1结束，未继续原场景，也不走0的持续刷新分支')],[
 sp('generic-kernel/wp07-diagnostics-files-http.md',85,105,'§5.1–5.3','列异常打印/Reset传播/模式门，没有一般异常报告后的返回/主入口结束控制'),
 sp('generic-kernel/wp09-save-startup-continue.md',85,96,'§4.1','只列成功启动顺序及早期中断，没有包装返回后顶层分流'),
 sp(T,81,85,'IO08–IO12','打印、重启与日志失败，未给一般异常与正常返回的完成状态对照')],
 '在调试主入口内抛普通异常且诊断正常完成时，关键段包装吸收异常并返回失败标记；主入口不消费该标记而正常给出自己的完成值，顶层脚本循环结束。失败点之后的场景动作不继续；不据此推断宿主窗口/进程退出。',
 '当前合同准确描述打印/重启/退出信号，却不能确定一般异常报告之后是重抛、回到场景、等待刷新还是结束脚本主循环。其它战斗/AI包装的继续合同属于不同调用层。',
 '启动/主循环错误后的有限控制结果仍未提取；不要求保留具体数值API，但需要区分这条收口和回调/战斗局部恢复。',
 ['DEBUG真，异常在mainFunctionDebug进入关键段包装内，普通异常不是Reset/SystemExit/Hangup，诊断日志/提示正常完成。','不在编译/插件内部先行截获的路径；无外部包装或重写；只分析脚本控制流。'],
 {'input':'调试主场景执行中在某动作写状态后抛普通异常，异常报告成功。','reference':'状态前缀保持；失败动作之后未到；包装返回后主入口完成、顶层脚本循环退出，不重入原场景。'},
 '没有异常时关键段成功完成；顶层主入口同样正常结束其脚本循环。',
 'Reset/SystemExit仍抛；Hangup先按主流程紧急保存后再由调试关键段转Reset；诊断自身失败不保证返回。这些既有合同保留。',
 '实现方可能为普通异常补自动恢复/重试，或错误认为继续刷新分支会被关键段失败状态触发。',
 {'search_record':'negative-search.json#critical_completion','actually_read':[{'path':F+'generic-kernel/wp07-diagnostics-files-http.md','ranges':'1–143'},{'path':F+'generic-kernel/wp09-save-startup-continue.md','ranges':'1–163'},{'path':F+'generic-kernel/wp10-migration-failure-recovery.md','ranges':'1–175'},{'path':F+'user-interface/wp65-title-load-options-pause-and-pc.md','ranges':'24–144'},{'path':F+'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md','ranges':'251–256'},{'path':F+'combat-requirements/wp51-ai-action-selection-and-skill.md','ranges':'19–27,106'},{'path':F+'demo-dx/wp72-debug-contexts-and-controls.md','ranges':'230–237'}],'result':'战斗/AI异常包装“不重抛可继续”已有，未据此另立重复必修；关键段及主脚本调用者是不同包装，当前条款止于打印/信号。'},
 '补一般异常在诊断成功/诊断失败两前提下的包装及顶层控制结果；不规定未来返回整数或进程结局，不要求自动恢复。',
 ['正常、一般异常、重启/退出、超时、诊断失败五分支区分。','一般异常收口明确本次场景不续跑、脚本主循环可结束；宿主最终行为仍未知。','不混用PBDebug局部包装与关键段主流程包装。'],
 ['WP07诊断成功前提','WP09启动顺序','WP10超时紧急保存'],['M02-CRITICAL-COMPLETION'],'M02-critical-main-completion',['KERNEL-DIAGNOSTIC-FAILURE'],confidence='high for static control flow; medium for requirement priority')
print('Candidates written:',len(json.loads((P/'findings.json').read_text())['findings']))
# Final counterevidence refinement after full lottery variable-boundary contract was read.
p=P/'findings.json';d=json.loads(p.read_text());x=next(x for x in d['findings'] if x['id']=='GR5-M02-001')
x['title']='三类持久状态对假值和非布尔真值的读取差异未明确'
x['severity']='P3';x['priority']='P3'
x['current_spec_behavior']='WP09提供持久身份；WP72明确5000上界；WP70 §2/§5已明确nil读0、0/5001/负索引及直接写入与便利写入的刷新区别。剩余未明示的是变量false保留、普通开关非布尔真值原样和自开关只认true。'
x['gap']='候选仅限剩余布尔值/非布尔值读取差异；明确撤回nil默认值、上界和刷新行为缺失的宽主张。'
x['negative_evidence_search']['actually_read']=[dict(v,ranges='1–57; especially §2 lines17 and §5 lines44–46') if v['path']==F+'pokemon-rules/wp70-lottery.md' else v for v in x['negative_evidence_search']['actually_read']]
x['negative_evidence_search']['result']='WP70全文反证补足nil→0、直接/便利刷新、0/5001/负索引；这些不再列缺口。当前相关合同仍未给变量false保留与两类开关对数值0的不同读出。'
x['spec_anchors'].append(sp('pokemon-rules/wp70-lottery.md',13,46,'§2/§5 反证','变量nil读0及写入/索引/刷新已明确，本候选排除这些已支持行为。'))
x['proposed_spec_change']='若兼容作者直接存值为目标，在WP09补变量false保留/普通开关原值/自开关严格真值的小表与两个向量；引用WP70已正确的上界/nil/刷新合同，不重复修订。'
x['acceptance_criteria']['static']=['变量同一合法槽false/nil独立读出分别为false/数字0，其中nil对照保持已有WP70合同。','普通开关存数值0读数值0；自开关存0读false，存true才读true。','原有5000/5001及直接/便利刷新合同不变；不把登记级类型检查当槽值布尔约束。']
x['confidence']='high for static primitive-value distinction; medium for future author-compatibility relevance'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
