"""Record static candidate findings; no reference or behavioral model execution."""
import copy
import review_state as s
import review_ops as o

F='deliverables/final-specification-set/'
coverage={x['path']:x for x in s.read('reading-coverage.json')['sources']}
def source(path, lines, keys, fact, caller):
    return dict(path=path,version=dict(commit=s.R,git_blob=coverage[path]['git_blob']),lines=lines,
                symbol_or_data_keys=keys,supporting_fact=fact,caller_config=caller)
def spec(path,lines,clause,text):
    return dict(path=path,version=s.B,lines=lines,section_or_vector=clause,current_statement=text)
def finding(identity,title,root):
    x=copy.deepcopy(s.read('findings.json')['findings'][0])
    x.update(id=identity,title=title,root_cause_group=root,severity='P2',priority='P2 provisional',
             disposition='unresolved',status='candidate_pending_independent_counterevidence',
             category='static_contract_gap',source_anchors=[],spec_anchors=[],negative_evidence_search=[],
             affected_files=[],shared_contracts=[],dependencies=[],related_capabilities=[],related_findings=[],
             history_links=[],unknowns=[],excluded_claims=[],
             confidence=dict(source_behavior='high_static',contract_gap='high_for_named_clauses_pending_independent_counterevidence'),
             review_resolution='当前已读合同未消解具名差异；提交独立反证，不自签最终必修。',
             user_decision_needed=dict(required_now=False,later_policy='先裁定参考事实与规格范围；未来是否保留异常兼容行为另作产品决策。'))
    return x

x=finding('GR5-M01-005','负盒号的容量查询不能沿用仅−1代表队伍的寻址分支','M01-STORAGE-NEGATIVE-CAPACITY')
x['category']='contradiction'
x['source_anchors']=[source('Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',[132,176],
    'maxPokemon / pbFirstFreePos / indexed reads',
    '容量查询对任何负盒号返回队伍上限；寻址与空位查找的队伍特例只接受−1，其它有效负号仍寻址真实盒。',
    {'configuration':'Settings::MAX_PARTY_SIZE; default6','consumer':'automatic empty-slot scan'})]
x['spec_anchors']=[spec(F+'creature-rpg/wp25-party-and-storage.md',[44,64],'§3.1–3.2','容量表只把−1写为6，其余取盒长度；空位扫描称按当前长度。'),
    spec(F+'creature-rpg/wp25-party-and-storage.md',[138,153],'§7–8','重复每盒容量=当前长度及−1容量例外；没有所有负盒号的例外。'),
    spec(F+'user-interface/wp66-b-storage-and-pokedex-ui.md',[35,43],'§2.2','−2按真实倒数第二盒寻址，选择模式可把特殊位置交给该寻址；这里没有定义容量。'),
    spec('specs/creature-rpg/wp25-party-and-storage.md',[43,60],'§3.1–3.2','现行原稿也写−1→6、其余盒当前长度。')]
x['expected_reference_behavior']='默认40盒、每盒30格且队伍上限6时，容量查询盒号−2得到6，读取盒号−2则指向零基盒38。其自动空位查找只扫描该盒前6格；这些格均占用而第6格为空时返回−1，不返回6。'
x['current_spec_behavior']='按WP25容量表，−2不等于−1且不是正向越界，会落入真实盒当前长度30；其空位查找可被实现成扫描全部30格。WP66B已说明−2的寻址对象，但没有修正这个不同入口的容量分支。'
x['gap']='当前容量合同与固定源条件不同，且传播至自动空位查找。'
x['preconditions']=['基础储存对象正常、40个长度30的盒、队伍容量6','盒38前6格被占且格6为空，无插件覆写','直接容量/空位查询；不要求选择模式后续动作都可达']
x['minimal_counterexample']=dict(input='容量查询盒号−2',static_expected='6；不是盒长度30',execution='NOT_EXECUTED')
x['normal_case']=dict(input='盒号38容量查询；另查−1且队伍长度2',static_expected='38→30；−1→6，−1空位位置2')
x['failure_or_boundary_case']=dict(input='盒38仅前6格占用，查询−2首空位；另查盒号40容量',static_expected='−2首空位−1；盒号40容量0')
x['impact_on_independent_implementation']='负位置容量、自动寻空位与真实格读取可能相互不兼容；常规非负盒号不受此差异影响。'
x['negative_evidence_search']=[
    dict(path=F+'creature-rpg/wp25-party-and-storage.md',read_ranges=[[1,218]],result='全文当前容量、操作、失败与引用均已读；只列−1容量特例。'),
    dict(path='specs/creature-rpg/wp25-party-and-storage.md',read_ranges=[[1,250]],result='全文原稿与场景相同，没有所有负盒号容量规则。'),
    dict(path=F+'user-interface/wp66-b-storage-and-pokedex-ui.md',read_ranges=[[1,271]],result='−2/-1的真实盒寻址是重要反证检查，但该条只定义读取位置，不定义容量；仍委托WP25。'),
    dict(path=F+'test-catalog/creature-rpg-wp18-20-24-25-26.md',read_ranges=[[162,207]],result='PS全部42项已读；负目标格自动选择与负盒号容量不同，尚未给后者向量。'),
    dict(path='specs/ui/wp66-b-storage-and-pokedex-ui.md',read_ranges=[[35,43],[289,289]],result='原稿同样只说明选择模式−2寻址；B36不是容量规则。')]
x['proposed_spec_change']='把容量查询、成员寻址、空位扫描的负盒号规则分列；增加−2与−1、正向盒号三组对照。保留固定参考异常事实，不把全部负号改成安全拒绝。'
x['affected_files']=[F+'creature-rpg/wp25-party-and-storage.md',F+'test-catalog/creature-rpg-wp18-20-24-25-26.md']
x['shared_contracts']=['M01-CONFIG-STORAGE-CAPACITY'];x['related_capabilities']=['M01-CONFIG-STORAGE-CAPACITY']
x['dependencies']=['WP25 owner independent counterevidence','WP66B negative-position boundary; no expansion of its reserved downstream scope']
x['acceptance_criteria']=dict(static=['逐入口区分负盒号与负格索引','复核容量6/30及前6格扫描的控制流','保留WP66B已正确的−2寻址结论'],must_execute=[],execution_if_later_authorized='本次不执行容器；若需运行，先报版本、输入、命令和副作用。')
x['unknowns']=['选择模式泄漏位置的全部后续消费者仍非M01完整认证范围','未执行参考或模型']
x['excluded_claims']=['不声称正常UI一定把成员错误存入','不改变每盒通常30格的事实','不修改参考实现']

y=finding('GR5-M01-006','NPC队伍缺省字段的确定性覆盖尚未被“按数据覆盖”合同完整描述','M01-TRAINER-MEMBER-ABSENT-DEFAULTS')
y['source_anchors']=[source('Data/Scripts/010_Data/002_PBS data/015_Trainer.rb',[129,175],'NPC member generation overlay',
    '未给特性槽固定0，未给性别按训练家男→0、否则1；普通/超级异色未给则分别假；未给Nature用两登记表零基位置之和取Nature数量模后选该登记位置。',
    {'caller':'Trainer record conversion','explicit_override':'provided member fields; single-gender Pokemon setter still applies'}),
    source('PBS/trainers.txt',[79,82],'COOLCOUPLE / Alice & Bob','两个成员为TURTWIG与CHIMCHAR，均未指定性别/特性槽/异色/Nature。',{'profile':'current root; automatic default data'}),
    source('PBS/trainer_types.txt',[269,273],'COOLCOUPLE','类型性别Unknown（2），不是male。',{'consumer':'trainer.male? during member generation'})]
y['spec_anchors']=[spec(F+'creature-rpg/wp18-creature-identity-species-ownership.md',[188,203],'§4.3 NPC上下文','列按数据覆盖的字段及Nature“物种序号＋类型序号”、IV/EV公式，未列其它缺省覆盖。'),
    spec(F+'creature-rpg/wp24-player-trainers-partners.md',[132,157],'§5.1–5.3','把成员生成覆盖细节委托WP18。'),
    spec(F+'pokemon-rules/wp19-attributes-ability-and-stats.md',[35,98],'属性派生/覆盖','普通个体未缓存时从个体编号派生；这是NPC覆盖前的合同，不能直接用作最终NPC缺省。'),
    spec(F+'demo-dx/wp73-a-content-editors.md',[65,75],'§3.5','补充未指定IV/EV与显式零的区别，没有补性别、特性槽或异色缺省。')]
y['expected_reference_behavior']='标准NPC成员装载后：缺省特性槽0；缺省性别以训练家男性为男、其它类型为女（固定性别/无性别物种仍受其设置入口约束）；未指定普通/超级异色分别写假。缺省Nature使用基物种和训练家类型各自在当前登记键序列的零基位置相加，对Nature数量取余，再按Nature登记序选取；不是全国图鉴号、等级或随机个体编号。'
y['current_spec_behavior']='现行WP18上下文表列覆盖字段，但没有说明省略值仍会覆盖普通创建结果；Nature只写“序号＋序号”，未限定零基登记序。WP24委托该表，WP19则规定普通个体的派生缓存规则。'
y['gap']='缺省NPC内容无法由现行表唯一复现；给出字段名或普通个体派生不足以确定最终数据。'
y['preconditions']=['固定默认内容已装载，依赖查询与创建正常，无插件/训练家装载钩子改写','使用普通NPC数据装载，缺省成员字段','性别例使用混合性别物种，排除固定性别/无性别设置守卫']
y['minimal_counterexample']=dict(input='实际COOLCOUPLE Alice & Bob成员TURTWIG/CHIMCHAR，均无Gender字段',static_expected='两者均被设置为女；不保留按随机个体编号派生的性别',execution='NOT_EXECUTED')
y['normal_case']=dict(input='同类混合性别物种显式Gender=Male，或男性训练家省略Gender',static_expected='男；前者由显式值决定，后者由训练家男性分支决定')
y['failure_or_boundary_case']=dict(input='固定无性别物种省略Gender；普通双特性物种省略AbilityIndex；未指定Shiny/SuperShiny',static_expected='无性别设置门保留无性别；特性槽0；两异色覆盖为假。明确提供SuperShiny真可随后影响普通异色，仍按写入顺序。')
y['impact_on_independent_implementation']='默认随附训练家可得到不同性别、特性与Nature，影响战斗、繁殖或展示；并可能错误允许缺省NPC随机异色。'
y['negative_evidence_search']=[
    dict(path=F+'creature-rpg/wp18-creature-identity-species-ownership.md',read_ranges=[[1,363]],result='全文含构造默认与NPC上下文，NPC缺省细节仍只明确IV/EV及概略Nature。'),
    dict(path='specs/creature-rpg/wp18-creature-identity-species-ownership.md',read_ranges=[[1,384]],result='现行原稿全文同样缺少这组确定性覆盖值。'),
    dict(path=F+'creature-rpg/wp24-player-trainers-partners.md',read_ranges=[[1,289]],result='全文训练家/装载表委托WP18，无另一个缺省表。'),
    dict(path='specs/creature-rpg/wp24-player-trainers-partners.md',read_ranges=[[136,161]],result='当前原稿相关NPC数据/装载条款委托WP18。'),
    dict(path=F+'pokemon-rules/wp19-attributes-ability-and-stats.md',read_ranges=[[1,268]],result='普通派生、单性别守卫是反证限定，不能补NPC最终覆盖。'),
    dict(path='specs/pokemon-rules/wp19-attributes-ability-and-stats.md',read_ranges=[[1,417]],result='全文核对；训练家上下文仍只给IV/EV并委托WP24。'),
    dict(path=F+'demo-dx/wp73-a-content-editors.md',read_ranges=[[1,174]],result='全篇编辑默认说明不等于NPC装载默认；未指定IV/EV零化已有覆盖，不重复立项。')]
y['proposed_spec_change']='集中给NPC成员字段省略/显式值/最终覆盖的表，写清Nature的身份序列、零基索引与取余；保留单性别守卫及现有IV/EV公式。加入实际Unknown类型双成员例与显式Gender对照。'
y['affected_files']=[F+'creature-rpg/wp18-creature-identity-species-ownership.md',F+'creature-rpg/wp24-player-trainers-partners.md',F+'test-catalog/creature-rpg-wp18-20-24-25-26.md']
y['shared_contracts']=['M01-DATA-Trainer-3','WP18 NPC generation','WP24 trainer load'];y['related_capabilities']=['M01-DATA-Trainer-3']
y['dependencies']=['WP18/WP24 owner independent counterevidence'];y['related_findings']=['GR5-M01-004']
y['acceptance_criteria']=dict(static=['区分普通创建结果与NPC后续覆盖','逐字段列缺省与显式值，不把编辑器默认替代装载默认','Nature使用零基登记位置并明确登记数据变化可能改变结果','保留单性别与SuperShiny写入顺序'],must_execute=[],execution_if_later_authorized='本轮仅静态核对实际PBS字段与构造路径；执行创建前需另报计划。')
y['unknowns']=['未执行随机创建或训练家装载','额外插件与事件覆盖不在已核实路径内']
y['excluded_claims']=['不把所有未知训练家性别改成female，只有成员缺省写入分支如此','不声称IV/EV公式缺失','不以未来产品策略替代参考事实']
o.upsert('findings.json','findings',[x,y],'id')
for path,ranges,rule in [
 ('specs/creature-rpg/wp18-creature-identity-species-ownership.md',[[364,384]],'Current original final sections completed; historical PASS not reused.'),
 ('specs/pokemon-rules/wp19-attributes-ability-and-stats.md',[[1,417]],'Whole current original read; distinguish ordinary derivation, formula order, NPC data overlays and PBS order.'),
 ('specs/demo/wp73-a-content-editors.md',[[65,109]],'Current original reference/compound editor rules; PBS order remains unspecified and editor defaults are not runtime NPC defaults.'),
 ('specs/creature-rpg/wp24-player-trainers-partners.md',[[136,161]],'NPC data/load delegation checked against WP18 and actual Trainer construction.'),
 ('specs/ui/wp66-b-storage-and-pokedex-ui.md',[[35,43],[289,289]],'Exact negative-position consumer and B36: addressing only, not capacity.'),
]:
    n=len((s.ROOT/path).read_text().splitlines());o.spec(path,[[a,min(b,n)] for a,b in ranges],rule)
o.progress('登记GR5-M01-005负盒容量和006 NPC缺省覆盖两条候选，均保留待独立反证状态，不签最终必修。原始WP18/19及相关编辑/装载条款已进一步补读。','更新全部主责条款/表/向量映射与完成边界；继续核对未闭合配置分支')
print('Two static candidates recorded; no final required disposition')
