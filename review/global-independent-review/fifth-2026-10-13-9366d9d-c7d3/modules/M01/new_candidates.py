import copy
import review_state as s
import review_ops as o
F='deliverables/final-specification-set/'
C=s.read('reading-coverage.json')
def anchor(path,lines,entry,fact,caller):
 e=next(x for x in C['sources'] if x['path']==path)
 return {'path':path,'version':{'commit':s.R,'git_blob':e['git_blob']},'lines':lines,'symbol_or_data_keys':entry,'caller_config':caller,'supporting_fact':fact}
def sp(path,lines,clause,fact):return {'path':path,'version':s.B,'lines':lines,'section_or_vector':clause,'current_statement':fact}
def base(id,title,root):
 x=copy.deepcopy(s.read('findings.json')['findings'][0])
 x.update(id=id,title=title,root_cause_group=root,source_anchors=[],spec_anchors=[],negative_evidence_search=[],affected_files=[],shared_contracts=[],dependencies=[],related_capabilities=[],related_findings=[],history_links=[],unknowns=[],excluded_claims=[],severity='P2',priority='P2 provisional',disposition='unresolved',status='candidate_pending_independent_counterevidence',category='unresolved_contract_gap',review_resolution='候选事实与当前已读合同差异已登记；不自签最终必修。继续补齐相关当前合同反证，交独立反证审者。',confidence={'source_behavior':'high_static','contract_gap':'provisional_pending_independent_counterevidence'},user_decision_needed={'required_now':False,'later_policy':'先完善固定参考事实；异常兼容选择留到后续，不修改参考或正规格。'})
 return x
x=base('GR5-M01-003','翻译键逐行空白归一顺序尚未从一般“压缩空白”合同中区分','M01-LZ-LINE-WHITESPACE')
x['source_anchors']=[anchor('Data/Scripts/001_Technical/003_Intl_Messages.rb',[481,490],'Translation.stringToKey','顺序处理每行行首空白、每行行尾空白、剩余至少两个连续空白；单个内部换行可保留。行首/行尾不是只指整个字符串端部。',{'consumers':'hash lookup, set/add hash messages, translation text import'}),anchor('Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb',[24,25],'controls help localization','实际源调用的两个段落之间有两个换行；随附规范键保留一个换行，值保留两个。',{'entry':'_INTL'}),anchor('Text_english_core/SCRIPT_TEXTS.txt',[4089,4090],'record2042','逐记录文本读取与安全基础类型解码均确认：键单换行、值双换行。不是仅理论异常输入。',{'binary':'Data/messages_core.dat SCRIPT_TEXTS same key/value'})]
x['spec_anchors']=[sp(F+'generic-kernel/wp08-localization.md',[27,32],'§3.2','仅称去首尾空白、压缩连续空白；未给逐行端部处理顺序与内部单换行保留。'),sp(F+'generic-kernel/wp08-localization.md',[133,148],'§6.3.2','规定规范键碰撞后值覆盖，但未补规范化的逐行规则。'),sp(F+'test-catalog/generic-kernel-wp05-06-07-08-09-10.md',[144,145],'LZ26–27','覆盖同键及双ASCII空格碰撞；未覆盖两个换行的归一结果。'),sp('specs/kernel/wp08-localization.md',[48,53],'§3.2','现行原稿同样为一般“去首尾空白、压缩连续空白”。')]
x['expected_reference_behavior']='合法已载入哈希域同时具有键A＋一个LF＋B和值T，以及键A＋一个ASCII空格＋B和值U时，请求A＋两个LF＋B经当前规范化得到单LF键，返回T；不是把两个LF直接压成空格而返回U。仅一个内部LF也保留；普通两个ASCII空格仍变一个空格。规范化仅作用键，不把译文内的双换行压为单换行。'
x['current_spec_behavior']='已读WP08正文/原稿/测试允许理解为整串trim之后压缩空白；缺少可区分上述两种实现的精确顺序。其它当前正文同义反证仍继续，不能凭一次检索就声称全库没有补充。'
x['gap']='候选可实现性缺口：归一的逐行范围与先后决定哈希身份，实际Controls语料已经依赖此区别。'
x['preconditions']=['固定R标准文本入口，无插件覆写','当前语言哈希数据和字符串输入有效','观察窗口处理前查找结果，不要求宿主渲染或真实语言安装']
x['minimal_counterexample']={'input':'当前哈希有A LF B→T及A空格B→U；查询A LF LF B','static_expected':'命中T','execution':'NOT_EXECUTED'}
x['normal_case']={'input':'查询A两个ASCII空格B','static_expected':'归一A单空格B，可命中U'}
x['failure_or_boundary_case']={'input':'独立查询A单LF B，及查询A单空格B；另检查存储值本身含双LF','static_expected':'两个键仍不同；值保持其原有双LF，非查找阶段压缩对象'}
x['impact_on_independent_implementation']='可能对现存译文查错键或回退原文，亦改变导入重复键碰撞关系；不是排版偏好。'
x['negative_evidence_search']=[{'path':F+'generic-kernel/wp08-localization.md','read_ranges':[[1,191]],'result':'全文已读，§3.2只有一般措辞；导入预处理与键归一是不同阶段，§6.3不补此区别。'},{'path':'specs/kernel/wp08-localization.md','read_ranges':[[1,195]],'result':'全文已读，原稿同义措辞没有明确逐行算法。'},{'path':F+'test-catalog/generic-kernel-wp05-06-07-08-09-10.md','read_ranges':[[112,153]],'result':'LZ全部行重核；LZ27仅ASCII空格碰撞，未给LF序列对照。'}]
x['proposed_spec_change']='以文本变换顺序描述逐行边缘与剩余连续空白，明确单内部LF与译文原样；加单LF/双LF/双空格的成对向量及现存Controls键值证据。不复制正则。'
x['affected_files']=[F+'generic-kernel/wp08-localization.md',F+'test-catalog/generic-kernel-wp05-06-07-08-09-10.md'];x['shared_contracts']=['M01-LZ-KEY','M01-LZ-CORPUS-SEMANTICS'];x['related_capabilities']=x['shared_contracts']
x['acceptance_criteria']={'static':['复核所有相关现行规范键正文与向量，排除同义覆盖','分别说明键与值、逐行边缘与整串边缘、变换先后','把现存Controls调用与core记录映射到同一单LF键'], 'must_execute':[], 'execution_if_later_authorized':'若要求隔离验证，先提交具体目的/版本/输入/命令/副作用；本次只做文本解析与静态路径对照。'}
x['dependencies']=['WP08共享键合同的独立反证'];x['unknowns']=['未执行参考归一函数或行为模型；宿主字符串边缘组合未穷尽','全部当前非主责补充是否还有具体规则待最终反证汇总'];x['excluded_claims']=['不把核心旧键等同已无调用者','不从一个真实键推断所有换行组合','不要求修改用户语料或参考实现']
y=base('GR5-M01-004','六项PBS数值的列序尚未与能力登记序和公式向量序明确分开','M01-PBS-SIX-STAT-ORDER')
y['source_anchors']=[anchor('Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb',[1,119],'six main stats/PBS positions','PBS列顺序为HP、攻击、防御、速度、特攻、特防；登记顺序把速度放在特攻/特防之后；命中闪避没有PBS列。',{'schema_consumers':'Species BaseStats, trainer member IV/EV, data getters/writers'}),anchor('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',[292,310],'Species BaseStats conversion','六个数通过各能力声明的PBS位置归到具名能力；并非按主能力遍历顺序直接配对。',{'callers':'base species and form validation'}),anchor('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',[888,913],'trainer member IV/EV conversion','同列序读IV/EV；未给出的尾项取首项，随后再检查每项/总量。',{'caller':'trainer final validation'}),anchor('Data/Scripts/010_Data/002_PBS data/008_Species.rb',[403,418],'BaseStats/EVs write projection','BaseStats反写使用相同PBS位置；EVs则为具名能力/数值对，不应误当同种六列格式。',{'caller':'species writer'}),anchor('Data/Scripts/010_Data/002_PBS data/015_Trainer.rb',[199,205],'IV/EV writer','训练家IV/EV按同样PBS位置输出。',{'caller':'trainer writer'})]
y['spec_anchors']=[sp(F+'generic-kernel/wp03-content-identity-and-schema.md',[99,117],'§5.1','给类型模式目录，没有具体六列位置表。'),sp(F+'creature-rpg/wp18-creature-identity-species-ownership.md',[56,97],'§3.2','给基础能力/EV责任与默认表，未把PBS列序具体化。'),sp(F+'pokemon-rules/wp19-attributes-ability-and-stats.md',[13,27],'§2','能力名录按HP/物攻/物防/特攻/特防/速度列出；不是对PBS列序的定义。'),sp(F+'demo-dx/wp73-a-content-editors.md',[65,75],'§3.5','IV/EV只称“按PBS顺序”，没有在该段列出顺序。')]
y['expected_reference_behavior']='合法Species BaseStats六值1,2,3,4,5,6对应HP1、攻击2、防御3、速度4、特攻5、特防6。合法训练家IV六值同序；尾项省略还重复首项。Species的EVs字段是具名能力/正数对，与训练家EV六列不是同一种结构；反写保持各自结构。'
y['current_spec_behavior']='当前已读合同给能力名录、公式及“PBS顺序”指称；个性/觉醒力量的具体环序虽同PBS顺序，但属于另外的消费者，未明确承担作者数据列映射。全部相关原稿/补充反证仍待汇总。'
y['gap']='候选缺口：独立实现可误用公式常见列序，把速度/特攻/特防三项循环错置；不能以读者知道原游戏格式作为规格。'
y['preconditions']=['合法完整PBS物种/训练家记录，无更早编译失败','固定R的六主能力目录，无新增能力或插件修改','观察数据归名及反写顺序，不运行战斗或数值模型']
y['minimal_counterexample']={'input':'合法基础物种BaseStats六值1,2,3,4,5,6','static_expected':'速度4、特攻5、特防6；HP/攻击/防御1/2/3','execution':'NOT_EXECUTED'}
y['normal_case']={'input':'六值全部相同','static_expected':'两种误用顺序看不出差异，因此必须用不等列验证'}
y['failure_or_boundary_case']={'input':'合法训练家IV为1,2,3,4,5,6；独立省略尾项；另给Species EVs具名对','static_expected':'仍按PBS列序；省略尾项补首项，不能补0或按公式序；具名EV不按六列解读'}
y['impact_on_independent_implementation']='合法默认数据导入后可改变能力与IV归属，连带速度排序、伤害、遗传、觉醒力量与反写；不是术语格式问题。'
y['negative_evidence_search']=[{'path':F+'generic-kernel/wp03-content-identity-and-schema.md','read_ranges':[[1,240]],'result':'全文模式和责任目录已读，没有六列对应表。'},{'path':F+'generic-kernel/wp04-pbs-lifecycle.md','read_ranges':[[1,227]],'result':'全文解析/写回无明确六列对应表。'},{'path':F+'creature-rpg/wp18-creature-identity-species-ownership.md','read_ranges':[[43,98],[157,208]],'result':'相关内容字段/构造/上下文已读；有defaults但未定义PBS列序，余下原稿有效补充仍待检查。'},{'path':F+'pokemon-rules/wp19-attributes-ability-and-stats.md','read_ranges':[[28,220]],'result':'已读具体能力公式/特性/性格/个性表；个性环序不等于已明示的PBS输入合同。'},{'path':F+'demo-dx/wp73-a-content-editors.md','read_ranges':[[54,90]],'result':'只用“PBS顺序”代称；相关原稿检索命中同词，尚不据此作全文阴性结论。'}]
y['proposed_spec_change']='在作者数据边界集中给三类六值字段的具名列序、与Species具名EV对的区别、输入尾项默认及输出顺序；各消费者引用。加不等列与等列对照，不按Ruby结构设计新系统。'
y['affected_files']=[F+'generic-kernel/wp04-pbs-lifecycle.md',F+'generic-kernel/wp03-content-identity-and-schema.md',F+'test-catalog/generic-kernel-wp02-03-04.md'];y['shared_contracts']=['M01-FIXED-Stat','Species BaseStats','Trainer IV/EV','WP73A six-dimensional editor'];y['related_capabilities']=['M01-FIXED-Stat','M01-PBS-SPECIES','M01-PBS-TRAINER']
y['acceptance_criteria']={'static':['完整反查WP18/19/24/73A当前原稿和有效补充中的输入列序','以六个不同合法数值逐列对应source声明/编译/反写','区分Species EVs具名对与Trainer EV六列'], 'must_execute':[], 'execution_if_later_authorized':'本次不执行参考编译/自写行为模型；若要隔离运行须先提交具体计划给父会话。'};y['dependencies']=['WP18/19/24/73A完整相关合同反证'];y['unknowns']=['当前有效附表是否另有完整作者列序尚待反证汇总','实际完整编译/反写未执行'];y['excluded_claims']=['不声称能力公式本身错误','不把个性/觉醒力量的有序位合同当错误','不要求未来复制登记顺序或类结构']
o.upsert('findings.json','findings',[x,y],'id')
# Source observation remains a pending gap, not supported by generic prose alone.
a=s.read('source-to-spec.json')
for c in a['capabilities']:
 if c['capability_id']=='M01-LZ-KEY':c.update(status='partial',related_findings=['GR5-M01-003'],comparison='基本键归一存在，但逐行端部/剩余连续空白顺序的现行精确合同不足候选；记录实际Controls键值，待独立反证。')
s.write('source-to-spec.json',a)
print('Two candidates added, unresolved/pending independent counterevidence; no required sign-off')
