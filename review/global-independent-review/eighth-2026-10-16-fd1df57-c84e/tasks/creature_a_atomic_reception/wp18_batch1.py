"""Manual formal-clause decomposition of WP18 lines3–158; audit assembly only."""
from pathlib import Path
import json
import datetime

O = Path(__file__).resolve().parent
P = 'deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md'
ADMIN = {
3: '分类与实现独立合同资格，非运行断言。',
5: '净化正文/引用与字段身份约定；静态无运行证据资格声明，不能作为行为支持。',
13: '本文件主合同责任与后继引用约束。',
17: '物种/个体分层和变更范围导航。',
18: '创建/随机/上下文范围导航。',
19: '复制及后继影响范围导航。',
20: 'Owner/来源/外来/命名范围导航。',
24: '动态处理器/Mega/Shadow主合同分别属于WP21/22/23，本文件接口仍需审核。',
25: '集合/完整获得/捕获/繁殖主责划分，不能排除本文件可得接合。',
26: '属性/持久状态/成长主责划分，不能排除实际接口。',
27: '未来架构中立性要求，非Ruby迁移模板。',
33: '术语表列标题。',62:'字段目录列标题，后续带规则行仍逐条分解。',
86:'记录默认表列标题，后续每个默认实际审查。',
105:'个体字段表列标题。',144:'三形态设置入口比较表引导，不以此签其所有格。',
146:'形态差异表列标题，六个维度在各数据行分别核。',152:'读取语义段落引导。'
}
# Each list contains manually identified distinct meanings of the complete row.
ROWS = {
35: ['物种内容有基身份', '正形态内容键按物种_N命名', '基形态号0', '个体存储species是基身份而非形态记录键'],
36: ['形态为同物种整数变体', '基形态0', 'forced_form记录显式优先值', 'time_form_set记录设置时间', 'form另有当前存储值'],
37: ['个体是运行时实体', '本文件定义身份/来源/拥有者及状态的持久字段责任'],
38: ['personalID创建为32位随机整数', '性别派生消费该ID', '异色派生消费该ID', '特性索引派生消费该ID', '性格派生消费该ID'],
39: ['Owner含id', 'Owner含name', 'Owner含gender', 'Owner含language', '原拥有者身份不同于当前战斗控制者概念'],
40: ['外来是相对于给定训练家的判定', '比较Owner id和名字；性别语言不参与'],
41: ['来源含方式编号', '来源含地图', '来源含文本', '来源含获得等级', '来源含孵化资料', '来源含获得及孵化时间'],
42: ['steps_to_hatch正数定义蛋', '孵化/来源完整流程引用WP35而非本谓词保证'],
43: ['复制保持来源身份数值', '新建重新抽个人ID', '新建重新抽六主能力IV'],
51: ['记录id的基形态键是物种符号', '正形态id键是物种_N', '记录species是基身份', '记录form是编号'],
52: ['先查物种与请求形态键', '缺该形态则回基础键', '两者均缺则未命中', '严格get缺失报错', 'try_get缺失可返回nil', 'exists?为存在判定而非构造'],
53: ['each_species只yield form0记录', 'species_count只统计这些记录'],
54: ['未定义标量继承基础记录当前值', '未定义types克隆外层', '未定义base_stats克隆容器', '未定义evs克隆容器', '未定义tutor_moves克隆外层', '未定义egg_moves克隆外层', '未定义abilities克隆外层', '未定义hidden_abilities克隆外层', '未定义egg_groups克隆外层', '未定义offspring克隆外层', '未定义flags克隆外层', '空等级招式继承每个pair的clone', '空进化表继承每个tuple的clone', '三种野生持物仅全未定义才联合继承', '运行查询读取已完成这些继承的记录而不另按字段回基础'],
56: ['Shape固定14身份次序', 'Color固定10身份次序', 'Habitat固定10身份次序且含Mountain', '14体型icon位置0..13各绑定原身份', '显示名经本地化请求', 'HeadArms为合法Shape', 'Gray为合法Color', 'WatersEdge为合法Habitat', '未知枚举身份不被作者schema接受', '基础省略Shape取Head', '基础省略Color取Red', '基础省略Habitat取None', 'Habitat字段不替代Area遭遇/地图筛选'],
58: ['编译依登记及前向表首次发现选前身', '形态对应前身优先', '缺形态对应时回基础关系', 'minimum_level消费所选反向前身', 'breeding回溯消费所选反向前身', '其它合法前向边不因只选一前身而删除', '不改变已有形态继承/默认/创建顺序'],
64: ['name提供物种本地化显示请求', 'form_name提供形态本地化显示请求', 'category提供类别本地化显示请求', 'pokedex_entry提供条目本地化显示请求', '文本/图鉴合同路由WP08/WP62'],
65: ['pokedex_form控制图鉴形态归类', '主行为合同WP62'],
66: ['types为属性有序列表', '常见1–2是内容约定', '数据/读取无两项截断', '主行为合同WP19'],
67: ['base_stats为基础能力', 'evs为击败产出', 'base_exp为基础经验', '数值主合同WP19', '战斗消费主合同WP43'],
68: ['growth_rate是成长曲线身份', '等级经验换算消费该身份', 'WP19登记接口而WP30定义完整流程'],
69: ['gender_ratio为比例身份', '身份可指固定单性别/无性别', '比例身份可给女性阈值', '主合同WP19'],
70: ['catch_rate是捕获难度输入', '完整捕获主合同WP38'],
71: ['happiness是创建初始值', '创建使用由WP18负责', '后继变化由WP30负责'],
72: ['moves是等级与招式有序表', '表可含重复招式', '学习流程WP30', '个体招式状态WP20'],
73: ['tutor_moves为教学候选表', 'egg_moves为蛋招表', '教学/遗传/重学分别引用WP30/WP34/WP20'],
74: ['abilities为自然候选数组', 'hidden_abilities为隐藏候选数组', '数组可含空位', '解析主合同WP19'],
75: ['wild_item_common为常见持物池', 'wild_item_uncommon为少见池', 'wild_item_rare为稀有池', '野生分配主合同WP36'],
76: ['egg_groups提供繁殖分组', 'hatch_steps提供孵化步数', 'incense提供熏香身份', 'offspring提供后代物种', '完整流程路由WP33–35'],
77: ['evolutions持前向路径', '同容器可持带反向标志前身', '本族/进化条件及提交主合同WP31'],
78: ['height存0.1m', 'weight存0.1kg', '个体读取与展示消费这两个单位'],
79: ['color提供颜色描述身份', 'shape提供体型描述身份', 'habitat提供栖息描述身份', 'generation提供世代描述', '展示主合同WP62等'],
80: ['flags提供关键字标记', 'DefaultForm_N可改变基形态选择', '其它旗标意义按真实消费者决定'],
81: ['mega_stone关联Mega物品', 'mega_move关联Mega招式', 'unmega_form关联解除目标形态', 'mega_message关联演出消息选择', '主合同WP22'],
82: ['pbs_file_suffix记录作者文件来源尾注', '编译写出主合同WP04'],
84: ['下表是记录构造缺省而非PBS全校验成功', '前提是有效id和已登记六主能力', '标量/空列表/nil是不同值', '显式提供字段仍有各自处理门'],
88: ['species省略取传入id', 'form省略取0'],
89: ['原始name省略取Unnamed', 'category省略取???', 'entry省略取???', '本地化展示另有文本入口'],
90: ['form_name省略为nil'],
91: ['pokedex_form省略采用已选form', '显式form2且省略pokedex_form时为2'],
92: ['types省略为新[NORMAL]列表', '每个已登记主能力base<=0填1', '主能力base缺失填1', '每个主能力EV产出<0填0', '主能力EV产出缺失填0'],
93: ['base_exp省略100', 'growth_rate省略Medium', 'gender_ratio省略Female50Percent'],
94: ['catch_rate省略255', 'happiness省略70', 'egg_groups省略新[Undiscovered]', 'hatch_steps省略1'],
95: ['height省略1', 'weight省略1', 'color省略Red', 'shape省略Head', 'habitat省略None', 'generation省略0'],
96: ['moves省略新空列表', 'tutor_moves省略新空列表', 'egg_moves省略新空列表', 'abilities省略新空列表', 'hidden_abilities省略新空列表'],
97: ['wild_item_common省略空列表', 'wild_item_uncommon省略空列表', 'wild_item_rare省略空列表', 'offspring省略空列表', 'evolutions省略空列表', 'flags省略空列表'],
98: ['incense省略nil', 'mega_stone省略nil', 'mega_move省略nil'],
99: ['unmega_form省略0', 'mega_message省略0', 'pbs_file_suffix省略空字符串而非nil'],
101: ['base_form先找DefaultForm_N', '没有该旗标回记录自身form', 'single_gendered按比例记录female_chance是否nil', 'base_stat_total合计基础能力值', 'flag查询不区分大小写'],
108: ['form为存储形态并有动态读取入口', 'forced_form为显式优先值', 'time_form_set为设置时刻字段', '动态语义路由WP21'],
109: ['personalID为个体32位身份', '派生属性引用WP19'],
110: ['exp为经验字段', 'level为等级缓存/接口', '成长流程归WP30'],
113: ['hp为持久生命', 'status为持久异常', 'statusCount为关联计数', '字段行为主合同WP20'],
114: ['moves存已知招式对象有序列表', 'first_moves存最初招式身份列表', '两表独立主合同WP20'],
115: ['shiny字段只有直接写入器', '普通读取经shiny?派生缓存', 'super_shiny另有独立读写缓存', '派生主合同WP19'],
116: ['ability_index保存解析索引', 'ability保存显式或解析特性', '主合同WP19'],
117: ['nature保存表现性格缓存', 'nature_for_stats允许计算性格覆盖', '二者不自动同一化'],
118: ['item为持物身份', 'mail为邮件对象', '持物主合同WP20', '完整邮件主合同WP64'],
119: ['owner为Owner记录，设置验证类别'],
120: ['obtain_method保存方式', 'obtain_map保存地图', 'obtain_text保存自定义文本', 'obtain_level保存获得等级', 'hatched_map保存孵化地图'],
121: ['timeReceived为获得时刻读写接口', 'timeEggHatched为孵化时刻读写接口', '孵化写入流程主合同WP35'],
122: ['poke_ball保存所在球身份', '捕获写入流程主合同WP38'],
123: ['name保存昵称并有物种名回退读取'],
124: ['steps_to_hatch为剩余孵化步数', '正数表示蛋', '完整孵化流程主合同WP35'],
125: ['happiness为友好字段', '创建初始化本文件负责', '受控变化WP30负责'],
126: ['ribbons为缎带身份列表', 'markings为标记列表', 'cool为华丽属性', 'beauty为华丽属性', 'cute为华丽属性', 'smart为华丽属性', 'tough为华丽属性', 'sheen为华丽属性', '展示接口WP21，完整进阶活动仍未决'],
127: ['pokerus编码毒株和剩余时间', '生命周期主合同WP61'],
128: ['fused保存另一只个体对象引用而非新Owner或克隆', '融合工具主合同WP28'],
129: ['ready_to_evolve保存特定进化准备标记', '完整进化主合同WP31'],
130: ['cannot_store为存放限制标记', 'cannot_release为放生限制标记', 'cannot_trade为交换限制标记', 'UI读取主合同WP25/26', '正常流程写入者未定位不是不存在保证'],
131: ['shadow为Shadow标志', 'heart_gauge为心量表', 'hyper_mode为Hyper存储标志', 'saved_exp为暂存经验', 'saved_ev为暂存EV容器', 'shadow_moves为招式记录', 'heart_gauge_step_counter为步计数', '本文件仅登记字段，完整Shadow主合同WP23'],
133: ['IV上限常量31', 'EV总上限常量510', '单项EV上限常量252', '昵称输入上限常量10', '常规招式槽常量4'],
137: ['species=输入可为物种/形态键/Species记录', '进入前要求可解析记录', '其含义是基物种变更而非任意同种形态切换'],
139: ['严格解析目标记录', '基身份相同在所有后继之前早退', '同物种其它形态不能经此入口切换'],
140: ['先写目标基species', '目标default_form优先', '否则正form采用自身形态', '无两者则保留原form'],
141: ['清forced_form', '新物种单性别时清gender缓存', '清level缓存让当前经验沿新曲线重派', '清ability解析缓存', 'ability_index保留', '最后重算能力'],
142: ['该入口不直接改经验', '不直接改招式', '不直接改来源', '不直接改Owner', '不直接改昵称', '不直接改友好度；任意外部callback扩展不在此无副作用保证'],
148: ['form=先写form', '清ability缓存', '调用onSetForm', '重算', '有全局玩家图鉴则register', '登记会读取gender/普通shiny', '无yield中断点', '这些是顺序前缀，后段异常不保证全部完成'],
149: ['setForm先写form/清ability', '有block在onSetForm前yield一次', '再调用handler', '再重算', '再条件register', '登记可填gender/普通shiny', 'block或handler异常保留早写并阻止后段'],
150: ['simple设置写存储form', '不调用handler', '不清ability缓存', '仍重算', '不显式登记', '无yield点'],
154: ['forced_form非nil优先', 'battle真直接读存储', 'storage真直接读存储', '否则请求getForm', 'truthy且不同结果才经form=提交'],
155: ['simple读取forced或存储值', 'simple不请求handler', 'species_data使用simple', '基础能力内容沿species_data读'],
156: ['个体正图入口先读普通form', '个体背图入口先读普通form', '个体图标入口先读普通form', '守卫/forced/动态提交都发生在资源选择之前', 'Summary个体图消费上述入口', '前序界面正常才到对应资源读取', '底层显式形态接口只用已求值参数', '上游先读个体求参数仍可能提交', '孵化示例EG13/20责任保持'],
158: ['未知目标严格物种设置报错', '动态getForm结果相同不触发提交及其副作用']
}

def unit_for(line):
    if line in [51,52,53,54,56,58,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,88,89,90,91,92,93,94,95,96,97,98,99,101]:
        return {'own': ['GameData::Species complete455L', 'Pokemon complete1227L', 'GenderRatio/Stat/Nature complete definitions'], 'received': ['KERNEL SP01..SP15, complete41 defaults, corrected14/10/10 catalogs', 'UI D04/D07/E02/E03/S05/S06/X25/X26'], 'premise': '固定登记/构造/编译入口分别观察；未提供字段，不把显式0/空列表/nil混同；六主能力已登记；无插件/并发覆写。', 'failure': '查找缺失和作者枚举失败按各入口；构造/编译后续异常保留此前容器/登记写入，不推原子回滚。', 'open': '仅文本本地化实现/完全作者记录值/下游繁殖进化效果族超出本字段责任时，按对应具体源单元扩读；当前行的已定义字段接口与正常consumer收到。'}
    if line in [148,149,150,154,155,156,158,137,139,140,141,142]:
        return {'own': ['Pokemon complete1227L', 'Pokemon_Sprites complete316L', 'Player_Pokedex complete361L', 'Battle_Peers complete77L'], 'received': ['UI S02/P02/B08/X16 and UI-BF-001..UI-BF-020 complete meanings'], 'premise': '普通有效记录/个体；只有更早handler/yield/重算/场景正常返回才到后段；全局player与pokedex存在性独立。', 'failure': 'form/ability先写；yield/handler/stat/dex可阻止后段且不恢复早写；动态相同值守卫与显式提交不混同。', 'open': '所有具体MultipleForms handlers源族/真实素材不由此接收。156孵化场景EG13/20的完整自身caller尚待完整受收，不冒全域。'}
    return {'own': ['Pokemon complete1227L', 'Owner/Move/Trainer/Player/Pokedex/Storage complete definitions', 'MegaEvolution and ShadowPokemon complete definition files'], 'received': ['UI P01..12/S01..13/B01..12/E01..06', 'KERNEL VAL/LANG/SAVE complete bounded records', 'UI-BF001..055'], 'premise': '固定普通公开API与六主能力，字段责任定义不等于任意反射写入受限；不从默认缺caller移出能力分母。', 'failure': '字段setter与直接容器入口分别看；后续UI/领域失败只保实际到达前缀；纯责任路由没有独立取消或状态写。', 'open': '130正常事件写入者仍需固定脚本负证据；跨领域完整生命周期保持对应主责。'}

def main():
    ledger = json.loads((O/'old-locator-disposition.json').read_text())
    existing = json.loads((O/'manual-atomic-clauses.json').read_text())
    facts = []
    for r in ledger['rows']:
        if r['path'] != P or r['range'][0] > 158:
            continue
        ln = r['range'][0]
        if ln in [107,111,112]:
            continue
        if ln in ADMIN:
            r.update(decomposition='COMPLETE_BOUNDED_TYPE_DISPOSITION', type_disposition=ADMIN[ln], source_support='NONBEHAVIORAL_SCOPE_LAYOUT_OR_EVIDENCE_QUALIFICATION', accepted=True, consumer='NOT_APPLICABLE_TO_THIS_TYPED_ROW; substantive child rows are independent')
            continue
        assert ln in ROWS, ln
        u = unit_for(ln)
        ids=[]
        for n, meaning in enumerate(ROWS[ln],1):
            aid=f'CAA-W18-L{ln:03d}-A{n:02d}'; ids.append(aid)
            facts.append({'id':aid, 'formal_path':P, 'formal_line':ln, 'assertion':meaning, 'complete_source_and_receiver_contract':u, 'premise_verified':'LOCAL_DEFINITION_AND_RECEIVED_CONSUMER_MEANINGS', 'support':'SUPPORTED_BOUNDED_STATIC', 'business':'NOT_EXECUTED', 'old_locator':r['id'], 'formal_parent_children':'MANUALLY_EXHAUSTED_FOR_THIS_ROW', 'whole_lifecycle_approval':False})
        r.update(decomposition='MANUAL_EXHAUSTED_BOUNDED_FORMAL_ROW', manual_children=ids, source_support='SUPPORTED_BOUNDED_STATIC_CHILDREN', premise=u['premise'], consumer=u, accepted=False)
    # Snapshot records preserve the old checkpoint as history in source snapshots;
    # this current file is the explicitly evolving WIP, not an immutable receipt.
    existing['atoms'] += facts
    existing['formal_wp18_batch1_atoms']=len(facts)
    existing['formal_wp18_batch1_extent']=[3,158]
    existing['recorded_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    ledger['manually_exhausted_locators']=sum(x['decomposition'].startswith('MANUAL_EXHAUSTED') for x in ledger['rows'])
    ledger['typed_dispositions']=sum(x['decomposition']=='COMPLETE_BOUNDED_TYPE_DISPOSITION' for x in ledger['rows'])
    ledger['not_manually_exhausted_locators']=sum(x['decomposition'].startswith('OPEN') for x in ledger['rows'])
    ledger['fully_accepted_locators']=sum(x['accepted'] for x in ledger['rows'])
    for name,obj in [('manual-atomic-clauses.json',existing),('old-locator-disposition.json',ledger)]:
        (O/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    (O/'wp18-batch1-result.json').write_text(json.dumps({'utc':existing['recorded_utc'],'atoms':len(facts),'complete_source_and_receiver_contracts':{str(k):unit_for(k) for k in ROWS},'formal_parent_ids':[x['old_locator'] for x in facts], 'type_dispositions':ADMIN,'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'new_formal_atoms':len(facts),'total_atoms':len(existing['atoms']),'decomposed_formal_rows':ledger['manually_exhausted_locators'],'typed_rows':ledger['typed_dispositions'],'remaining_old_rows':ledger['not_manually_exhausted_locators']},ensure_ascii=False))

if __name__=='__main__':
    main()
