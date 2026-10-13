import review_state as s
C='Data/Scripts/021_Compiler/001_Compiler.rb';CP='Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb';SP='Data/Scripts/010_Data/002_PBS data/008_Species.rb';L='Data/Scripts/001_Technical/003_Intl_Messages.rb'
WP3='deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md';WP4='deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md';WP8='deliverables/final-specification-set/generic-kernel/wp08-localization.md';TC='deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md';LTC='deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md'
cov=s.read('reading-coverage.json'); common=s.read('findings.json')
def src(path,lines,symbol,fact,caller):
 e=next(x for x in cov['sources'] if x['path']==path)
 return {'path':path,'version':{'commit':s.R,'git_blob':e['git_blob']},'lines':lines,'symbol_or_data_keys':symbol,'caller_config':caller,'supporting_fact':fact}
def sa(path,lines,section,statement):return dict(path=path,version=s.B,lines=lines,section_or_vector=section,current_statement=statement)
def neg(path,lines,result):return dict(path=path,read_ranges=lines,result=result)
base=dict(module='M01',severity='P2',disposition='unresolved',status='candidate_pending_independent_counterevidence',reviewer='M01 independent reviewer',category='unresolved_contract_gap',source_baseline=common['source_baseline'],specification_baseline=common['specification_baseline'],evidence_level='static_semantic_source_analysis',execution_status='NOT_EXECUTED_THIS_REVIEW; no reference/model/behavior vector execution',review_resolution='待完成当前合同反证并交独立审者；本审者未作最终必修裁决。',history_links=[],related_findings=[],priority='P2 provisional',batch_owner='M01',user_decision_needed={'required_now':False,'later_policy':'参考事实明确后，是否兼容异常可另作产品决策；不将该政策问题当成本轮事实遗漏的证据。'})
f1={**base,'id':'GR5-M01-001','title':'活跃浮点字段的接受边界尚未在数值模式合同中闭合',
'source_anchors':[src(C,[384,435],'cast_csv_value: f','活跃浮点分支对文本先作专有识别，再宽容转浮点。负号、加号、指数形式不进入成功分支；单独小数点可进入。',{'entry':'get_csv_record','lines':[690,737]}),src(SP,[52,111],'Height,Weight','基础和形态的 Height/Weight 均使用同一浮点模式。',{'consumer':'Species PBS field'}),src(CP,[292,310],'validate_compiled_pokemon: height/weight','成功浮点值乘10、取整、至少1；形态校验亦调用。',{'caller':'compile_pokemon / validate_compiled_pokemon_form'})],
'spec_anchors':[sa(WP3,[99,117],'§5.1 模式表','f 只称浮点，完整解析规则交给 PBS 生命周期。'),sa(WP4,[58,92],'§4.2 活跃解析','逐值类型求值引用WP03模式表，已详述引号/q/可选/重复；未在该段给浮点特殊接受集合。'),sa(TC,[16,35],'KR09–KR10','数值例仅v/u与枚举；该已读目录没有浮点反例。')],
'expected_reference_behavior':'在活跃 PBS 记录入口，合法基础物种的 Height 文本为单独 ASCII 小数点时，静态路径得到浮点0，再登记十分之一单位值1；-1.0、+1.0、1e2 在浮点文本识别阶段拒绝。1.0 正常得到10。该事实不是对未来应接受什么输入的建议。',
'current_spec_behavior':'当前已全文读取的WP03/WP04及通用测试只提供“浮点”类别与一般求值/错误合同；相关领域物理尺寸条款尚未完成全文反证，所以不能正式裁定所有当前合同缺失。',
'gap':'候选缺口：如果所有当前领域合同均无补充，独立实现会自行选择常规浮点解析而无法复现上述异常接受/拒绝集合。当前仅确认主责文本未具体化，反证待办。',
'preconditions':['固定R活跃入口、无插件覆写','物种节身份和其他依赖合法，无更早失败','观察字段解析/登记的局部结果；不假定完整工程可编译'],
'minimal_counterexample':{'input':'有效基础物种条目的 Height 仅含一个ASCII小数点','static_expected':'浮点识别成功，转换值0，物种登记height为1（十分之一单位）','execution':'not_executed'},
'normal_case':{'input':'同前提，Height为1.0','static_expected':'登记height为10'},
'failure_or_boundary_case':{'input':'独立输入Height为-1.0、+1.0、1e2；另有字段省略对照','static_expected':'前三者浮点分支拒绝；省略走类默认，不等于显式非法文本'},
'impact_on_independent_implementation':'作者数据的接受集合、错误阶段、最小身高/体重与后续反写结果可能不一致。不是名称/格式修订。',
'negative_evidence_search':[neg(WP3,[[1,240]],'全文模式、默认、校验、责任目录和未决均读过；没有在该文件给本具体接受边界。'),neg(WP4,[[1,227]],'全文解析、失败、写回与全部向量入口读过；未给本具体浮点例。'),neg('specs/kernel/wp03-content-identity-and-schema.md',[[1,292]],'现行原稿全文同样只有浮点类别；旧Reviewed不作证据。'),neg('specs/kernel/wp04-pbs-lifecycle.md',[[1,264]],'现行原稿全文同样未给本具体例。'),neg(TC,[[1,81]],'逐KC/KR/KL行已读，无浮点向量；全领域尺寸/编辑合同仍待反查。')],
'proposed_spec_change':'若独立反证确认缺口，在WP04补活跃浮点文本规则与单小数点/正常小数/负号/指数对照；WP03保持字段类别但准确引用；领域尺寸继承十分之一单位规范。不要复制正则或改参考。',
'affected_files':[WP4,WP3,TC], 'shared_contracts':['M01-CSV-CAST','Species Height/Weight'],
'acceptance_criteria':{'static':['跟读所有Height/Weight/浮点当前领域条款及有效补充，先排除同义覆盖','逐条映射正常、接受异常、拒绝异常、缺省四类输入至活跃路径','明确与旧Unused浮点辅助不同，并保持现有q/引号规则'], 'must_execute':[], 'execution_if_later_authorized':'如需隔离验证，先向父会话提交目的/精确版本/输入/命令/副作用；本任务没有执行许可。'},
'dependencies':['WP18/WP19/WP21/WP62相关物理数据合同完整反查','WP73A编辑器与PBS入口区分'], 'related_capabilities':['M01-CSV-CAST','M01-CSV-RECORD','M01-PBS-SPECIES'], 'root_cause_group':'M01-ACTIVE-FLOAT-ADMISSION',
'confidence':{'source_behavior':'high_static','contract_gap':'provisional_pending_full_counterevidence'},'unknowns':['领域尺寸合同的全部补充尚未读完','具体宿主错误呈现/完整编译运行未验证'],'excluded_claims':['不宣称全部浮点输入已执行','不把注释数学预期当成实际解析器','不要求未来必须保留异常输入政策','不重开GR3-M09-001或GR3-M02-003']}
f2={**base,'id':'GR5-M01-002','title':'作者默认消息的差量生成与导出条目选择合同待闭合',
'source_anchors':[src(L,[553,587],'set/add array/hash/map messages','set使用新集合、add保留旧game集合；默认core参与过滤，map按各自桶。',{'caller':'PBS终检、script/event gather'}),src(L,[644,669],'default-core exclusion','数组忽略空值和与core同索引相等值；哈希只按core是否有规范键排除，不比较原始值。',{'config':'默认core数据，而非当前语言层'}),src(L,[291,370],'extract_text/write_section_texts_to_file','只遍历默认域及其非空原文条目；当前语言中独有域/键不扩充输出集合。',{'entry':'作者选定core/game导出'}),src(CP,[220,229],'move text collection','编译终检将招式名/描述经默认哈希set建立game差量。',{'consumer':'WP08 author material'})],
'spec_anchors':[sa(WP8,[13,32],'§2–3','定义默认材料、当前语言层和哈希身份。'),sa(WP8,[81,96],'§6.1–6.2','收集文本入域并从默认消息导出，说明形态/覆盖/转义，未在该段给core差量过滤及set/add不同。'),sa(WP8,[98,148],'§6.2.1–6.3.2','覆盖稀疏桶、空译和重复导入，后者不是默认生成的set/add语义。'),sa(WP4,[193,202],'§7','收集细节明确交给WP08。')],
'expected_reference_behavior':'默认core某哈希域已有规范键A时，收集A不再次写入新建game默认域；不同原文归一为A也排除。新键B进入game域。替换收集丢弃旧game独有键，追加收集保留它们。导出选择的默认材料没有键X时，即使目标语言有X的译文，输出也不新增X。数组按索引/值排除与哈希按键排除不同。',
'current_spec_behavior':'已全文核对WP08正文、原稿和LZ目录，已有语言game/core运行优先级及作者导入归并；这些并未等价描述上述默认差量生成。调试工具及全域有效补充反证尚未完成，保持候选。',
'gap':'候选缺口是作者材料集合的生成/保留/排除规则；不是已有运行查找优先级错误。不能在全部相关补充未读完前称最终missing。',
'preconditions':['默认消息外层及目标域合法','初始默认core哈希仅键A，初始game默认仅旧键Z','无插件覆写；相关收集/导出文件操作成功','默认消息与当前语言消息严格区分'],
'minimal_counterexample':{'input':'对该默认域作替换式收集，输入A与新键B','static_expected':'新game默认仅有B；A因core已有键排除，旧Z因set替换排除','execution':'not_executed'},
'normal_case':{'input':'默认core无输入规范键，输入非空B','static_expected':'B被收入game默认并可从该默认材料导出'},
'failure_or_boundary_case':{'input':'相同A/B输入改为追加式收集；独立导出对照只有当前语言有X，默认无X','static_expected':'追加保留Z并加入B；导出不新增X。异常I/O另按既有先删后写，不能由局部集合成功推完整工作流成功。'},
'impact_on_independent_implementation':'会影响core/game翻译分工、重复词条处理、重编译后残留条目和重导出时哪些译文可见；实现方仅照运行回退链无法重建作者材料。',
'negative_evidence_search':[neg(WP8,[[1,191]],'完整正文及表/向量/依赖读完；默认生成差量与导出独有键集合尚无本地明确规则。'),neg('specs/kernel/wp08-localization.md',[[1,195]],'现行原稿全文同样只总结收集/提取，不能补具体过滤。'),neg(LTC,[[110,153]],'LZ01–35逐行；重复归并是导入合同，不替代默认集生成。'),neg(WP4,[[1,227]],'全文读过；末段收集转交WP08。'),neg('deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md',[[1,40]],'§1与§3.1将翻译规则交WP08；其余匹配部分尚未完整读取，不声称排除全部工具补充。')],
'proposed_spec_change':'完成独立反证后，为WP08作者工作流补默认core过滤、set/add保留语义及默认条目主导导出集合；增加数组/哈希差异、同规范键不同原文、语言独有键三类对照。保持运行回退合同不变。',
'affected_files':[WP8,LTC], 'shared_contracts':['M01-LZ-DEFAULT-BUILD','M01-LZ-EXPORT','PBS文本终检'],
'acceptance_criteria':{'static':['先读完所有当前相关有效补充并检索合理同义合同','将默认/当前语言、core/game、set/add、数组/哈希/地图作用域分别说明','每个对照给出集合前后与导出包含/省略预期；不推断随附语料全部受影响'], 'must_execute':[], 'execution_if_later_authorized':'仅经父会话批准后才能运行隔离参考/模型；数据文件安全解码不代替上述行为验证。'},
'dependencies':['调试/编译/翻译有效补充的完整反证','全部31文本域消费来源与18文本语料逐记录映射'], 'related_capabilities':['M01-LZ-DEFAULT-BUILD','M01-LZ-EXPORT','M01-LZ-COLLECT'], 'root_cause_group':'M01-AUTHOR-MESSAGE-MATERIAL-SELECTION',
'confidence':{'source_behavior':'high_static','contract_gap':'provisional_pending_full_counterevidence'},'unknowns':['所有文本消费者/插件覆盖未知','全域有效补充尚未闭合','真实作者工作流I/O表现未执行'],'excluded_claims':['不重报LZ重复节归并或插值历史问题','不指称现有18份英文语料存在重复/不一致','不把自编数据解码器结果算行为测试','不要求兼容异常的未来产品决策']}
common['findings']=[f1,f2]; s.write('findings.json',common)
print('Wrote 2 unresolved candidates, neither required nor finalized')
