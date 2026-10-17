import collections,hashlib,json,subprocess
from pathlib import Path
D=Path('review/r8-disposition-r1-independent-5666b7b-20261017/agents'); P=Path('planning/implementation-routing/r8-20261017')
C='5666b7b912e2fb79b5119283ee6a37401a7071db';B='fd1df570cad987dc3852a3b958f03916e317f7fe';A='908273093e1f6b27fc58249417675dd62d146224';R='a0352c7fba38391afc535525988245701d5ce202'
m=json.load(open(P/'routing-manifest.json')); e=json.load(open(D/'kernel-mechanical.json'));old=json.loads(subprocess.check_output(['git','show',R+':review/r8-disposition-independent-d62b41f-20261017/agents/kernel-full-results.json']))
a={x['feature_id']:x for x in m['features']}; rt={x['feature_id']:x for x in m['retired_features']};mi={x['metadata_id']:x for x in m['metadata_records']};prior={x['feature_id']:x for x in old['features']}
reasons={
388:'配置规模、世代基准和默认值作用域仍是框架配置输入；源§3未变，新增WP03/04/08/65合同是身份、编译和消费交界，未替领域规则实施。',
389:'完整配置词典的历史全文信用仅用于未改默认/分类事实；新职责仍限作者配置输入，去向未变，领域效果没有被移入本行；直接引用提供编译、语言和UI消费者导航。',
390:'默认值派生及显式覆盖、模式联动、直接世代读取是配置规则；重读§5确认框架维护配置关系合理，没有许诺组合兼容。',
391:'普通发现与显式输入、候选材料、作者语言配置归框架；§6明确具体本地化/UI归消费者，现有WP08/WP65直接引用承接，材料不等于支持。',
392:'退役完整行身份保存，但META-000019没有按§7的真实责任关联编译、亲密/进化、场地能力、插件、捕获；仍有钓鱼邻行式泛连，后继导航不合格。',
393:'非法配置、资源ID冲突与发现失败仍保留未知；新框架职责不升级这些事实，依赖指向本篇明确交界。',
394:'36类身份/查询与回退的旧源全文事实及范围未变；当前框架登记责任与WP04/02共同合同相符，没有引入内容规则实现。',
395:'重读§4完整混合表，当前WP04承接缺失文件/编译门，WP08承接名称/描述和StorageCreator回退；正确保留原始字段与消费者查找两层。',
396:'重读§5完整schema/复合节头/重复身份/作者数值表，WP04直接引用承接实际解析和编译生命周期；作者数据校验框架候选合理。',
397:'固定规则身份目录确有登记顺序及引用拒绝合同；旧全文与当前范围/去向不变，可保留框架数据合同；未把字段责任目录退役误扩至本行。',
398:'退役对象完整保存，但META-000020未指到表列的WP19能力、WP20状态、WP27/28道具、WP30成长等主责，邻近WP02/03/04行不能替这些消费者。',
399:'可选Shadow缺席与候选材料不等于目标排除；新框架职责仅数据载入及来源边界，当前仍待U09核对。',
400:'严格/宽容查询、错型拒绝、副作用与最终宿主未知保持；新WP02/04引用与来源共同交界相符。',
401:'重读§3启动及直接编译全表，新增WP05/07用于真实插件先后和失败诊断；U02接受只回填来源，所有目标验证/阶段仍待定。',
402:'解析/校验旧全文信用适用于未改的§4；U02只改§5.2，当前locator逐字节核对，框架作者内容职责没有因回填扩大，WP03/07/08等为明列交界。',
403:'真实git show 908的§5.2已删特定提示承诺；父范围继续排除地图/动画子节，保留编译写回、反写、缓存及失败前缀，历史source保持。',
404:'独立地图事件转换粗标保持MZ/框架双方，源门为已登记地图及实际修改；用户XP迁移范围仍待决策，U02接受没有给目标批准。',
405:'动画映射仍单列MZ接入与框架数据，零/有效条目写入门和缓存边界保持；新引用没有把静态有效条目升级成播放验证。',
406:'启动与直接编译的部分状态和失败前缀已重读；框架编排持有本行，实际事件/动画及诊断由明确源合同消费，未重复实现。',
407:'转元数据方向正确、完整旧行保真，但META-000021没有关联首项本地化主责和具名世界/内容编辑器、呈现消费者；仅近邻编译与音频/动画编辑入口不足。',
408:'默认编译触发、主动导出和未证组合仍为本篇配置投影；U02状态回填不代表其它批接受或目标实现。',
409:'完整通知/处理器表、条件/精确登记和中断前缀重读；框架维护扩展规则合理，具体业务不被本行重做。',
410:'可扩展菜单行只承担注册/排序/过滤/分派；页面业务按原§4归UI，新增共同引用没有把业务菜单归入本行。',
411:'插件元数据、循环/冲突、逐字符版本比较与注册终止门完整重读；框架扩展合同合理，源目录空并未被当作无插件支持。',
412:'发现、编译和预编译消费各前提完整保留；框架承接能力候选未指定Ruby组织或声称发布包运行验证。',
413:'源§7明确格式化/日志/控制台交WP07，现已补同名直接合同；异常传播与直接终止仍按入口区分。',
414:'基线、强制编译、真实插件组合和产物读取未知保留；框架职责/待验证状态没有额外承诺。',
415:'逐字段旅行表已重读；初始化、生产事件和持久化是真行为，来源分类已改为未单列的统计附表，框架数据责任合理。',
416:'完整场地动作表及WP59§5.3.1已读，新增直接锚点和FR374准确提供严格预检后增计数、失败不回退的生产门；分类修复适用。',
417:'道具/钓鱼/雷达/树果九字段表完整重读；框架持久统计与原证据等级区分，源分类不再虚构导航；未宣称事件全部可达。',
418:'NPC三字段仍仅机制登记，更新可达性缺材料保留U01；新分类忠实，框架统计状态没有制造NPC事件实现。',
419:'个体/孵化/进化/交换等十一统计字段已重读，含交换先增后验失败；框架维护持久计数，领域生产按责任表限定，不改真实业务规则。',
420:'WP42/WP38补回结果/经验/金钱与失败球，但Mega统计真实生产为WP22§4.3 L58–60的玩家本人门及先增后变形；本行仍没有WP22直接/功能引用，生产合同未补全。',
421:'货币十一字段表保留实际增额、件数、缺事件和battle_points_won来源待查；新分类/框架统计职责不把待查来源变已知。',
422:'特殊九字段表保留数组/默认、可调用赋值机制和调用者未证两层；仍是框架统计合同，未因Demo缺材料删除行为。',
423:'保存/会话/最近保存时间三字段，现补WP09和WP10当前持久及旧帧数迁移真实合同；与临时锚点分离。',
424:'派生查询及临时游戏时间锚点有真实读写副作用，仍非74个声明字段；不因来源分类修正把它删为纯目录。',
425:'时间四来源、现实/帧消费者及变量计时全节已重读；WP09持久、WP13事件冷却/等待与WP59墙钟作为不同输入/消费者合同，直接引用准确且未统一成离线推进。',
426:'完整计步/统计节和WP12移动完成表已核，WP05有序通知、WP12守卫/零位移完成、WP09保存边界已连接；没有从距离未增推全局步数未变。',
427:'父当前范围精确扣除§5.3并指FR745，保留普通随机、地牢/彩票种子和有状态选择；不再把录像序列吞作统一内核随机。',
428:'已补WP09和WP14；完整地牢种子消费节确认保存待播状态、生成即清和全局随机副作用/失败前缀，新增reason指向真实合同。',
429:'默认随机/时间与未证组合依旧是粗标配置投影；重读§7及§5.3，录像主责已另列FR745，本行未声称统一随机或兼容已证。',
430:'直接告警全节及依赖已重读，新增WP08对应本地化，WP07对应控制台输出，参数与输出通道分开。',
431:'弃用别名参数校验、先告警后转发和块回调限制已重读；框架兼容行为粗标合理，新增WP07/08共同合同不改变原返回前提。',
432:'边界/不变量已重读；框架保留创建失败与使用期顺序，控制台呈现仍由WP07/MZ边界承担。',
433:'完整文件/归档内存流、路径、小端协议混合表已重读；框架I/O候选正确，宿主读取与具体资源播放没有被冒认已支持。',
434:'完整HTTP分层及请求前构造表已读；框架拥有协议和捕获边界，历史隔离替身没有被升级为联网/宿主兼容。',
435:'框架现在明确负责格式化、日志失败前缀和0/1控制流，MZ负责窗口/复制/控制台/重启消费；FR446/451/625/628为具体保存/恢复/UI交界，整节不再仅标MZ。',
436:'WP04/05/09/10路径虽存在，但新增四条specific reason分别谈本地化提取、消息集合、语言选项和语言状态，与源§6实际编译错误/插件终止/主流程超时紧急保存不符；不可把有链接当正确职责。',
437:'诊断配置/模式限制已重读；错误头、内部版回溯与宿主未知没有升级成全模式保证，框架粗标保留合理。',
438:'31文本域、键规范化和地图桶已重新读，框架文本身份服务责任合理；与具体UI表现分开。',
439:'完整语言配置/选择源节及WP65对应节核对：框架拥有候选/当前语言/消息载入及入口直写，MZ菜单交付选择，现已关联FR444/446/642/644。',
440:'历史完整查找/回退、占位及指定图像身份源信用适用，未改源/范围/去向；新通用框架职责仍只文本身份选择，实际加载/呈现仍属已明确资源消费者。',
441:'作者收集/提取/导入/部分写入全源节未改，旧完整阅读信用保留；新依赖是编译/保存/config共同交界，没有擅加具体UI或目标执行资格。',
442:'默认语言及延迟构造/多语言工作流已读；未把无候选变成未来排除，新待验证状态保持。',
443:'完整边界节保留空译、格式异常、覆盖删除及缺地图可达性；框架文本失败合同与UI实际结果分离。',
444:'17持久登记、动态重复身份及槽存取源与范围未变；旧完整信用保留，框架持久状态主责适合，新增WP06/07/08/10属来源明列合同。',
445:'源启动混合表与WP11完整恢复节、WP65载入节已读；框架持装载/保留/重建条件，MZ供标题/选图/取消/地图通知，FR324/326/451/642具体交接已列。',
446:'保存成功/失败与三直写路径已重读；框架持久状态与I/O提交，已改恢复主行负责UI，未因U01仍待整改伪称保存实现。',
447:'默认启动与保存配置已读；新合同引用不改变设置/进度/版本事实，阶段未批准和上游pending保持。',
448:'源§7及WP10完整失败恢复已核，补WP10载入/备份/删除/转换写回真实合同；错型与I/O失败保持不同。',
449:'完整转换机制及WP05版本比较已读；新增范围门明确支持哪些旧数组/表、版本/身份由用户决定，通用编排和具体兼容分开验收。',
450:'完整14项转换目录、64树果/4敷料/旧槽表已重新读；待决策与DEC-SPECIAL-AND-HOST-SCOPE及具体旧版本问题完整绑定，没有自动排除。',
451:'完整恢复混合表已读，框架持有效性/备份/删除/保存及异常前缀，MZ持询问、拒绝退出、清场景/条件恢复与缺图输入；FR326/435/445/642与源相符。',
452:'默认备份/紧急保存/单对象入口不等同具体旧格式承诺；449/450范围门传播已核，新框架候选仍待用户/验证。',
453:'备份同路径、转换失败前缀、寄养/电话缺陷已重读；框架候选不把参考缺陷当未来已批准政策。',
745:'§5.3是录像协作边界，框架保存初态/命令/随机/换人及版本，Showdown按实际域消费已录序列；链接FR132–136提供固定版本/格式、序列、回放/中止与清理合同，普通随机父范围已精确扣除。按章节边界行理解，不另宣称独立新业务能力。'
}
failids={'FR-000392','FR-000398','FR-000407','FR-000420','FR-000436'}
metafind='R1-KF-001';depfind='R1-KF-002'
new_findings=[{
'finding_id':metafind,'severity':'P3','title':'元数据消费者仍由整篇/邻近WP泛连，遗漏真实责任及具名跨域验收消费者','original_finding_refs':['KF-001'],'candidate':C,
'cases':[
{'unit':'META-000019 / FR-000392','candidate_pointer':'/metadata_records/18/feature_refs','source_document':mi['META-000019']['source']['document'],'source_lines':[[246,256]],'source_commit':B,'evidence':'组合表明确指编译生命周期、亲密/进化/战斗、场地能力、插件和Shadow/捕获；现refs含FR385–387钓鱼，而无WP04编译、WP30亲密、WP59场地、WP05插件、WP38捕获主责。配置词典有钓鱼开关不证明§7表与这三钓鱼行的直接责任关系。'},
{'unit':'META-000020 / FR-000398','candidate_pointer':'/metadata_records/19/feature_refs','source_document':mi['META-000020']['source']['document'],'source_lines':[[313,359]],'source_commit':B,'evidence':'字段责任表明确Species能力→WP19、学习→WP30、状态→WP20、Item→WP27/28、指标→WP15/WP67-A等；现大量refs是WP02/03/04邻行，无这些具名主责。部分WP21/31/62/63链接正确不能覆盖其余责任。'},
{'unit':'META-000021 / FR-000407','candidate_pointer':'/metadata_records/20/feature_refs','source_document':mi['META-000021']['source']['document'],'source_lines':[[286,296]],'source_commit':B,'evidence':'首项文本提取/翻译/保存归WP08，数据/世界编辑器归WP73；资源/呈现归真实播放方。现无WP08/内容世界编辑主责，FR277仅动画编辑入口、FR355仅音频，不能代表这些交界。'},
{'unit':'DOC-0108 named catalog consumers','candidate_pointer':'section-coverage.json:/sections/2226/feature_refs; /sections/2227/feature_refs; /sections/2228/feature_refs; /sections/2230/feature_refs; /sections/2231/feature_refs; /sections/2232/feature_refs','source_document':'deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md','source_lines':[[5,91],[97,223]],'source_commit':B,'evidence':'9个标题全用同一37行列表。KC03场地许可、KC05/06语言入口、KR13 Nature/WP19及KL的地图连接/编辑消费没有链接至其实际领域主责；U01-M01-021/022与J01-V01–06/V11具名地牢/图块集，未关联WP14真实消费者；R6-U14-FLAGS-04是孵化步数失败前缀，未关联WP35；指标编辑No/Yes具名WP73-B而列表无该主责。不是要求每个向量造新ID，可按这些已有跨域主责分组引用。'},
{'unit':'DOC-0109 language image catalog consumers','candidate_pointer':'section-coverage.json:/sections/2245/feature_refs','source_document':'deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md','source_lines':[[277,288]],'source_commit':B,'evidence':'LZ36–41明确WP15资源解析及WP65控制帮助；该节仍只有FR409–453的同一45行generic列表，FR440只拥有语言图像身份选择，实际指定键图创建/加载消费者未登记。此处不再把catalog→427→excluded745、catalog→445/451→326的有效机器链判为遗漏。'}],
'why_not_satisfied':'退役不是丢弃原责任表。稳定ID/完整归档已满足，但消费者的语义关联仍不满足完整复核合同；同WP或邻行并非真实主责证明。',
'necessary_fix':'保留全部旧行与ID；按完整责任表/具名跨域目录把metadata及section-coverage关联到已有真实主责，可作章节级合并，不要求逐句新增功能；现有父功能→excluded_child_refs子功能的有效机器链可保留。'
},{'finding_id':depfind,'severity':'P3','title':'战斗统计生产依赖仍漏Mega门，诊断失败依赖用途被本地化模板替代','original_finding_refs':['KF-004'],'candidate':C,'cases':[
{'feature_id':'FR-000420','candidate_pointer':f'/features/{m["features"].index(a["FR-000420"])}/dependencies','source_document':a['FR-000420']['source']['document'],'source_lines':[[73,87]],'producer_document':'deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md','producer_lines':[[37,60]],'source_commit':B,'evidence':'mega_evolution_count的玩家本人门和先统计后变形/异常前缀在WP22§4.3 L58–60；420仅新连WP42/WP38，wp/direct/feature refs均无WP22生产合同。WP42的正常终局统计不是该先提交点。'},
{'feature_id':'FR-000436','candidate_pointer':f'/features/{m["features"].index(a["FR-000436"])}/dependencies/direct_refs','source_document':a['FR-000436']['source']['document'],'source_lines':[[155,168]],'source_commit':B,'evidence':'4条新增specific reasons为“本地化提取/编译”“消息集合”“语言选项”“语言状态”；实际§6讲编译位置错误、插件输出终止、调试包装与非调试超时紧急保存。路径存在不等于用途正确。'}],
'why_not_satisfied':'原KF004要求必要调用/状态资格和真实生产/消费方向。补齐文档名仍不足以表达本行实际生产门和失败链。','necessary_fix':'给FR420补WP22真实统计生产锚点/既有稳定功能引用；将FR436各direct reason重写为实际编译/插件/主流程与紧急保存的失败用途，并核生成视图。'}]
# Full source credit is only inherited for verified identical bytes; changed rows themselves are independently judged.
ranges={'wp02-rule-configuration-and-data-variants.md':[[1,32],[204,278]],'wp03-content-identity-and-schema.md':[[1,24],[73,243],[313,393]],'wp04-pbs-lifecycle.md':[[1,56],[184,320]],'wp05-events-extensions-plugins.md':[[1,147]],'wp06-stats-directory.md':[[1,143]],'wp06-time-random-steps-stats.md':[[1,196]],'wp07-deprecation-appendix.md':[[1,54]],'wp07-diagnostics-files-http.md':[[1,191]],'wp08-localization.md':[[1,52],[199,231]],'wp09-save-startup-continue.md':[[1,20],[95,179]],'wp10-migration-failure-recovery.md':[[1,281]],'generic-kernel-wp02-03-04.md':[[1,236]],'generic-kernel-wp05-06-07-08-09-10.md':[[1,288]]}
ledger=[]
for doc in e['documents']:
 name=Path(doc['path']).name;n=ranges[name]; covered={i for lo,hi in n for i in range(lo,hi+1)};remaining=[i for i in range(1,doc['lines']+1) if i not in covered];comp=[]
 for i in remaining:
  if comp and comp[-1][1]+1==i:comp[-1][1]=i
  else:comp.append([i,i])
 ledger.append(dict(doc,new_read_commit=B,new_read_ranges=n,source_full_read_credit_inherited_from={'commit':R,'path':'review/r8-disposition-independent-d62b41f-20261017/agents/kernel-full-results.json','original_full_ranges':next(x['read_ranges'] for x in old['reading_ledger'] if x['path']==doc['path']),'inherited_unreread_ranges':comp},inheritance_basis='Historical bytes, complete immutable source objects, route and original semantic behavior unchanged where credit is reused; every new responsibility/dependency/current locator independently inspected. Prior verdict is not automatically transferred.',current_new_read_ranges=[[184,210]] if name=='wp04-pbs-lifecycle.md' else n,current_read_credit_note='908 changed line196 read by git show; complete Git diff and all current locators verified. Unchanged context uses verified B8 source credit.' if name=='wp04-pbs-lifecycle.md' else 'Current file byte-identical to fixed B8; no current-only behavior omitted.'))
# identify full-section rereads per row
bydoc={x['path']:x for x in ledger}
old_results=[];active_results=[]
for fid,pr in sorted(prior.items()):
 f=a.get(fid) or rt[fid];oldnum=int(fid[3:]);newverdict='FAIL' if fid in failids else 'PASS';source=f['source'];rr=ranges[Path(source['document']).name];selected={i for lo,hi in source['line_ranges'] for i in range(lo,hi+1)};seen={i for lo,hi in rr for i in range(lo,hi+1)}
 mode='FULL_RELEVANT_SOURCE_UNIT_REREAD_AND_CHANGED_FIELDS_REVIEW' if selected <= seen else 'VERIFIED_UNCHANGED_SOURCE_CREDIT_PLUS_CHANGED_FIELDS_AND_NECESSARY_BOUNDARIES_REVIEW'
 refs=[metafind] if fid in {'FR-000392','FR-000398','FR-000407'} else ([depfind] if fid in {'FR-000420','FR-000436'} else [])
 r={'feature_id':fid,'old_verdict':pr['verdict'],'new_verdict':newverdict,'verdict':newverdict,'disposition':'retired' if fid in rt else 'active','reason':reasons[oldnum],'review_method':mode,'prior_reason_received':pr['reason'],'source_complete_object_unchanged':True,'changed_fields_independently_reviewed':next(x['changed_top_fields'] for x in e['old_row_identity_results'] if x['feature_id']==fid),'old_finding_refs':pr['finding_refs'],'finding_refs':refs,'source_document':source['document'],'source_line_ranges':source['line_ranges'],'source_commit':B,'manifest_pointer':('/retired_features/'+str(m['retired_features'].index(f))) if fid in rt else ('/features/'+str(m['features'].index(f)))}
 old_results.append(r)
 if fid in a:active_results.append(dict(r,verdict=newverdict))
f=a['FR-000745'];active_results.append({'feature_id':'FR-000745','verdict':'PASS','reason':reasons[745],'review_method':'FULL_SOURCE_UNIT_AND_WP58_FULL_DOCUMENT_REREAD','source_document':f['source']['document'],'source_commit':B,'source_line_ranges':f['source']['line_ranges'],'manifest_pointer':'/features/'+str(m['features'].index(f)),'finding_refs':[],'related_metadata_propagation_verdict':'PASS','related_metadata_finding_refs':[], 'related_metadata_navigation':'catalog→FR427→functional_scope.excluded_child_refs→FR745'})
# Each old finding has every old case, plus explicit propagation units.
fr=[]
for oldf in old['findings']:
 cases=[]
 for case in oldf['cases']:
  fid=case['feature_id'];v=('PASS' if oldf['id']=='KF-006' else ('FAIL' if fid in failids else 'PASS'));cases.append({'feature_id':fid,'original_case':case,'verdict':v,'reason':('DOC0062与本行当前来源分类均改成“源文未单列分类（统计行为/数据附表）”；完整统计表确含初始化/更新/持久化，保留本行功能合理。其它生产依赖问题按KF004独立裁定。' if oldf['id']=='KF-006' else reasons[int(fid[3:])]),'finding_refs':([] if oldf['id']=='KF-006' else ([metafind] if fid in {'FR-000392','FR-000398','FR-000407'} else ([depfind] if fid in {'FR-000420','FR-000436'} else [])))})
 v='FAIL' if any(x['verdict']=='FAIL' for x in cases) else 'PASS'
 extra=[]
 if oldf['id']=='KF-003':extra=[{'unit':'FR-000745','verdict':'PASS','reason':reasons[745]},{'unit':'WP06 metadata /sections/1478 and catalog TM /sections/2236','verdict':'PASS','reason':'Both reference parent FR427; functional_scope.excluded_child_refs explicitly reaches FR745, a valid machine navigation chain without repeating dependencies.feature_refs.'}]
 if oldf['id']=='KF-001':extra=[{'unit':x,'verdict':'FAIL','reason':'Full retired object preserved, but actual consumer mapping incomplete/misdirected; see R1-KF-001.'} for x in ['META-000019','META-000020','META-000021']]
 if oldf['id']=='KF-002':extra=[{'unit':'FR-000391/435/437/439/440/442/444/445/446/447/451/452/453 and linked UI/world consumers','verdict':'PASS','reason':'Config projections, text identity, persistent value ownership and actual input/scene consumers examined for same root; concrete mixed rows now assign both framework and MZ.'}]
 if oldf['id']=='KF-004':extra=[{'unit':'All 36 prior PASS rows, and FR745','verdict':'PASS','reason':'Every changed dependency set reviewed; source common-prerequisite references kept as boundary/navigation, not blindly interpreted as mandatory implementation DAG. 420/436 remain FAIL in case results.'}]
 fr.append({'finding_id':oldf['id'],'verdict':v,'original_severity':oldf['severity'],'all_original_cases_checked':True,'original_cases':cases,'related_new_or_propagated_units':extra,'finding_refs':([metafind] if oldf['id']=='KF-001' else ([depfind] if oldf['id']=='KF-004' else [])),'summary':{'KF-001':'Retirement/count correction passes; real metadata consumers remain incomplete.','KF-002':'All four concrete mixed-boundary cases corrected through responsibilities and existing feature links; no sentence-by-sentence split required.','KF-003':'Original parent, new collaboration row and explicit parent→excluded-child metadata chain corrected; no duplicated dependency ID required.','KF-004':'12/14 original cases corrected; 420/436 remain.','KF-005':'Both exact legacy support scope gates corrected; user decision remains pending.','KF-006':'Document and all ten row source classifications corrected without deleting real stats behavior.'}[oldf['id']]})
# Every domain metadata section, retired object and explicit metadata record gets a verdict.
rm=[]
for fid in sorted(set(rt)&set(prior)):
 f=rt[fid];rm.append({'unit_type':'retired_feature','unit_id':fid,'manifest_pointer':'/retired_features/'+str(m['retired_features'].index(f)),'verdict':'FAIL','identity_verdict':'PASS','functional_count_treatment':'not active; exact old complete row retained except retirement','reason':reasons[int(fid[3:])],'finding_refs':[metafind]})
for mid in ['META-000019','META-000020','META-000021']:
 x=mi[mid];rm.append({'unit_type':'metadata_record','unit_id':mid,'manifest_pointer':'/metadata_records/'+str(m['metadata_records'].index(x)),'verdict':'FAIL','source':x['source'],'consumers':x['feature_refs'],'nonfunctional_treatment_verdict':'PASS','reason':'Nonfunctional classification and historical navigation are correct; concrete source-table consumers are incomplete or misdirected. See case evidence.','finding_refs':[metafind]})
# Concrete catalog units with necessary named consumer omissions; generic purpose/use boundaries may retain broad scoped navigation.
section_fail={1361:'Original combination responsibility table still has incomplete actual consumers (META19).',1391:'Original field responsibility table still has incomplete actual consumers (META20).',1420:'Original compilation boundary table still has incomplete actual consumers (META21).',2226:'Named KC03 field-move and KC05/06 player-language consumers absent; all nine sections repeat same broad union.',2227:'Named Nature→WP19 and text-language consumers absent; same broad union is not a typed consumer mapping.',2228:'Named metrics/content editors, map connections and battle animation playback consumers absent; compiler rows alone do not assign their consumer responsibility.',2230:'Named dungeon/tileset and map connection/editor input consumers absent.',2231:'FLAGS-04 hatching failure-prefix and metrics editor consumers absent.',2232:'Named DungeonParameters/DungeonTileset consumer WP14 absent.',2245:'Named WP15 image and WP65 control-help consumers absent.'}
for s in e['sections']:
 if s['mapping_kind']!='section-metadata':continue
 idx=int(s['pointer'].split('/')[-1]);v='FAIL' if idx in section_fail else 'PASS';rm.append({'unit_type':'section_metadata','unit_id':s['document_id']+'#'+s['anchor'],'candidate_pointer':'section-coverage.json:'+s['pointer'],'path':s['path'],'source_commit':B,'source_lines':[[s['line_start'],s['line_end']]],'verdict':v,'nonfunctional_treatment_verdict':'PASS','reason':section_fail.get(idx,'Purpose, scope, concepts, evidence/unknowns or test-source navigation only; not an implementation function or executed-test claim. Scoped document-level relation is sufficient here.'),'consumers':s['feature_refs'],'metadata_refs':s['metadata_refs'],'finding_refs':[metafind] if v=='FAIL' else []})
result={'schema':'r8-r1-independent-kernel.v1','candidate':C,'prior_candidate':'d62b41f4d620e50bb04c80a7505374bd284d8210','prior_review':R,'domain':'generic-kernel','task':'/root/r1_kernel','configuration':{'requested':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'normal','Fast':'off'},'authoritative_creation_echo':{k:'UNVERIFIED' for k in ['model','effort','service_tier','speed','Fast','cloud_task_uuid']},'effective_runtime_echo':{k:'UNVERIFIED' for k in ['model','effort','service_tier','speed','Fast']},'qualification':'Natural-language delegation, inherited configuration and tool advertising are not execution telemetry.'},'verdict':'FAIL','verdict_scope':'FIXED_CANDIDATE_DOMAIN_ONLY','counts':{'documents':13,'body_documents':11,'catalog_documents':2,'headings':258,'metadata_sections':86,'behavior_sections':172,'old_feature_count':66,'old_verdict_counts':dict(collections.Counter(x['old_verdict'] for x in old_results)),'old_re_review_counts':dict(collections.Counter(x['new_verdict'] for x in old_results)),'active_feature_count':64,'active_feature_verdicts':dict(collections.Counter(x['verdict'] for x in active_results)),'retired_feature_count':3,'explicit_metadata_records':3,'new_feature_count':1,'source_reread_lines':sum(sum(hi-lo+1 for lo,hi in x['new_read_ranges']) for x in ledger),'source_text_credit_inherited_lines':sum(sum(hi-lo+1 for lo,hi in x['source_full_read_credit_inherited_from']['inherited_unreread_ranges']) for x in ledger)},'catalog_results':[{'document_id':'DOC-0108','verdict':'FAIL','classification_verdict':'PASS','execution_status_preservation':'PASS / NOT_EXECUTED','reason':'Full catalog source and all 9 metadata mappings examined; named dungeon/tileset, hatching and metrics-editor consumer mappings still incomplete. Existing generic data owners do not supply those consumer duties.','finding_refs':[metafind]},{'document_id':'DOC-0109','verdict':'FAIL','classification_verdict':'PASS','execution_status_preservation':'PASS / NOT_EXECUTED','reason':'Full source/all 12 mappings examined. Replay via parent427→excluded745 and world recovery via445/451→326 are valid. LZ36–41 actual resource/control-help consumer navigation remains incomplete.','finding_refs':[metafind]}],'old_feature_results':old_results,'active_feature_results':active_results,'retired_metadata_results':rm,'finding_results':fr,'reading_ledger':ledger,'direct_dependency_reading':[{'path':'deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md','commit':A,'new_read_ranges':[[1,181]],'purpose':'FR745 actual domains, omissions, state, replay abort/cleanup/version; current equals B8'}, {'path':'deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md','commit':A,'new_read_ranges':[[121,159]],'purpose':'Full map restoration section for FR445/451 and named catalog world load'}, {'path':'deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md','commit':A,'new_read_ranges':[[24,50],[221,228]],'purpose':'Clock/variable consumers and full strength push production subsection'}, {'path':'deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md','commit':A,'new_read_ranges':[[90,115]],'purpose':'Full movement input/result mixed table and completion/zero-displacement step boundary'}, {'path':'deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md','commit':A,'new_read_ranges':[[26,40],[76,101]],'purpose':'Full page/cooldown and interpreter update/wait mixed table'}, {'path':'deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md','commit':A,'new_read_ranges':[[37,62]],'purpose':'Full Mega battle qualification/cancel/production subsection'}, {'path':'deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md','commit':A,'new_read_ranges':[[193,215]],'purpose':'Full money/stats and outer outcome return consumer subsection; other keyword hits are navigation only'}, {'path':'deliverables/final-specification-set/pokemon-rules/wp38-capture-and-receiving.md','commit':A,'new_read_ranges':[[18,30],[45,53]],'purpose':'Entry table / failed-ball producer; only stated ranges read, no full consumer-file claim'}, {'path':'deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md','commit':A,'new_read_ranges':[[23,82],[102,147]],'purpose':'Full title/load and options/language sections for specific KF002 consumers'}],'view_review':e['view'],'acceptance_backfill':{'candidate_snapshot':A,'receipt_commit':'861f7a44a6f763c265a11761ab17a8ec3b55f304','actual_report_commit':'548d6bb9a21d0967680445c013e66d9d5661d2d6','actual_report_and_result_read':True,'current_WP04_identity':next(x for x in e['documents'] if x['document_id']=='DOC-0060'),'active_accepted_feature_ids':[x['feature_id'] for x in e['active_locator_results'] if x['accepted_events']],'retired_FR407':'Old complete object remains unchanged/pending as historical row; not an eighth active accepted row. Current metadata source chapter unchanged.','direct_text_changed_feature':'FR-000403 only in this domain','delta':'WP04 line196 only removes specific Changes made to file X output promise, 37 bytes; fixed paths, changed-only rewrite, all other outputs/partial writes retained.','gates':'U02/U03 only ACCEPTED; CLOSED false; other bound batches and final routing/target validation remain pending.'},'mechanical_evidence':'kernel-mechanical.json','mechanical_execution':'kernel-command.json; kernel-check.py final exit 0 from exec cf015d','new_findings':new_findings,'remaining':['Repair metadata consumers and propagation; repair FR420/436 dependencies; freeze new exact candidate and re-review cumulative affected scope.','Global schema/tool/generated byte checks and ROOT findings owned by root; no domain-level whole-tool acceptance claimed.','User legacy/XP/special system scope and stages remain pending; Showdown prototypes and all business/host execution not run.','Only U02/U03 source acceptance received; other batches and final cumulative gates are not accepted or CLOSED.','Authoritative model/effort/tier/speed/Fast and cloud UUID remain individually UNVERIFIED.']}
# Independent current/historical identity proof for every newly read direct dependency.
for q in result['direct_dependency_reading']:
    pp=q['path']; hist=subprocess.check_output(['git','show',B+':'+pp]); cur=subprocess.check_output(['git','show',A+':'+pp])
    q['actual_text_read_from']='candidate worktree / fixed B8 bytes'
    q['historical_commit']=B; q['current_commit']=A; q['current_equal_historical']=cur==hist
    q['historical_blob']=subprocess.check_output(['git','rev-parse',B+':'+pp],text=True).strip()
    q['current_blob']=subprocess.check_output(['git','rev-parse',A+':'+pp],text=True).strip()
    q['bytes']=len(cur); q['sha256']=hashlib.sha256(cur).hexdigest()
    assert cur==hist, pp
result['independent_domain_file_set']={'commit':A,'body_paths':subprocess.check_output(['git','ls-tree','-r','--name-only',A,'deliverables/final-specification-set/generic-kernel'],text=True).splitlines(),'catalog_paths':[x for x in subprocess.check_output(['git','ls-tree','-r','--name-only',A,'deliverables/final-specification-set/test-catalog'],text=True).splitlines() if '/generic-kernel-' in x]}
assert set(result['independent_domain_file_set']['body_paths']+result['independent_domain_file_set']['catalog_paths'])=={x['path'] for x in e['documents']}
(D/'kernel-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
lines=['# Generic kernel R1 独立复核', '',f'固定候选 `{C}`；结论 **FAIL（需返修）**。旧66行：61 PASS、5 FAIL；新活跃64行：62 PASS、2 FAIL；3个退役旧行及3个元数据后继均逐项检查。11正文＋2catalog共258标题（172行为映射、86元数据映射），分母分别保留。','', '本审者非作者，只读候选与固定Git对象，只写本目录kernel-*；没有运行Ruby、游戏、宿主、Showdown、业务向量或未来框架。请求gpt-6.1-sol / ultra / default / normal / Fast off；权威创建/执行model、effort、tier、speed、Fast及云UUID逐字段UNVERIFIED。','', '## 必修问题','']
for f in new_findings:
 lines += ['### '+f['finding_id']+' / '+f['severity']+' — '+f['title'],'',f['why_not_satisfied'],'']
 for c in f['cases']:
  unit=c.get('unit',c.get('feature_id')); lines += ['- **'+unit+'**：`'+c['candidate_pointer']+'`；'+c['evidence']]
 lines += ['', '**必要修正：** '+f['necessary_fix'],'']
lines+=['## 六组原问题逐项裁定','','| 原组 | 新裁定 | 证据与剩余 |','| --- | --- | --- |']
for f in fr:lines.append('| '+f['finding_id']+' | '+f['verdict']+' | '+f['summary']+' |')
lines+=['','全部原case分别保存在kernel-results.json/finding_results；没有用作者finding-resolution的处置代替独立裁定。KF003的catalog→父427→excluded_child_refs→子745是有效显式机器链；不要求重复deps.feature_refs或每个catalog标题直接列子ID。世界读档目录经445/451到326同样有效，未误判缺项。','', '## 阅读与继承','',f'实际新读本域源文本 {result["counts"]["source_reread_lines"]} 行；另 {result["counts"]["source_text_credit_inherited_lines"]} 行仅继承旧独立报告的完整源阅读信用，逐文件字节身份已核。旧36 PASS的源内容、原路由/范围不变部分可保留；每个新职责、依赖、当前定位均重新审查。所有变化或受同根因影响的混合表/章节按下表重读，并读必要下游。没有把继承源信用写成新的全文阅读。','', '| 文件 | 本次实际新读B8区间 | 当前适用 / 旧全文信用 |','| --- | --- | --- |']
for l in ledger:lines.append('| '+Path(l['path']).name+' | '+', '.join(str(lo)+'–'+str(hi) for lo,hi in l['new_read_ranges'])+' | '+('908仅L196变更；git show读184–210及完整差分' if not l['current_equal_historical'] else '908与B8完整字节相同')+'；未重读区间 '+str(l['source_full_read_credit_inherited_from']['inherited_unreread_ranges'])+' |')
lines+=['','源身份、blob/SHA256、旧全文范围、实际新范围和继承理由均在reading_ledger。依赖阅读包括WP58全文、WP11恢复全节、WP59时钟/巨石推动、WP12移动表、WP13页冷却/解释器表、WP22 Mega提交、WP42终局统计、WP38失败球和WP65标题/语言设置；确切区间见JSON。原源文件被截断的工具输出已由后续分段补读；不声称完整重读未列区间。','', '本域新视图145行、64行均作关键字段/职责/状态/定位一致性核对；语义基于完整机器行及去重字段投影，未声称逐字完整阅读约百KB重复的literal view。根团队负责整体生成字节/工具校验。metadata view的三条后继链接已直接读，未把生成一致性当消费者正确性。','', '## 接受回填与身份','', '候选工作区正式树仍为B8 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。真实current908树为 `6ae817df5b11eafdec671214b0d04e542ad364bc`；WP04当前blob `d895aa9d0df2024d9bcd99f1d954d8a5685f6211`，41768B，SHA256 `70d794ed63d4ff1f98ed21a9aecfea4923063d10a45e69965e7dad294678adb2`。', '', '已真实git show读取861接受回执及548 actual报告/机器结果，并读908的实际§5.2。U02只删除L196特定提示承诺；FR403差异、当前unit/file身份正确，7个活跃WP04行401/402/403/404/405/406/408已按ACCEPTED核对。第8个原WP04行407是完整退役历史，保持旧pending字节，不是第8个当前活跃接受行。全部64当前locator的file/blob/unit/heading身份正确，66旧ID恰落active/retired一次、source完整对象不变，3退役去retirement后与d62完整行逐字段相同；新增745未复用。活跃源有效范围无物理交叠。','', 'U01、U08、U09以及其它已绑定范围仍待整改后核对；U07范围仅历史overlay，不据猜测绑定本域正式来源。861为U02/U03 ACCEPTED=true、CLOSED=false；实际报告的有限静态PASS没有被扩成目标验证、实现/验收、整轮通过。','', '## 逐旧行与追加行','', '| ID | 旧判定 | R1判定 / 处置 | 独立理由 |','| --- | --- | --- | --- |']
for r in old_results:lines.append('| '+r['feature_id']+' | '+r['old_verdict']+' | '+r['new_verdict']+' / '+r['disposition']+' | '+r['reason']+' |')
lines.append('| FR-000745 | 新增 | PASS / active | '+reasons[745]+' |')
lines+=['','全部退役、3 metadata记录及86元数据章节另有逐单元定位/消费者/非功能处理结果；未执行静态向量仍为NOT_EXECUTED。机械脚本kernel-check.py真实exit0，完整Git读取argv/exit/输出身份在kernel-command.json，覆盖与逐行身份在kernel-mechanical.json。早期结构探索曾因path/document字段假设出现只读KeyError，未用于任何PASS信用；后续按真实结构补核。','', '剩余：修正两组metadata/依赖问题后冻结新候选复核；目标原型、用户范围决定、其它上游批次和最终累计接受门继续保留。']
(D/'kernel-report.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(result['counts'],ensure_ascii=False));print('wrote kernel-report.md and kernel-results.json')
