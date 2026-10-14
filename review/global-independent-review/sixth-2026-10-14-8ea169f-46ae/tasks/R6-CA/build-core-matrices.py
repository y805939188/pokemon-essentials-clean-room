"""Serialize manually authored semantic notes; never infer PASS from reads.
Inputs: task structural inventory, core-facts.tsv, fixed formal block IDs.
Outputs only: task forward-core.jsonl, reverse-core.jsonl, core-matrix-counts.json.
The trivial forwarding accessors below were explicitly read and assessed.
"""
import csv,json,re
from pathlib import Path
O=Path(__file__).resolve().parent
D=json.loads((O/'structural-denominator.json').read_text())
facts={}
for row in csv.DictReader((O/'core-facts.tsv').open(),delimiter='\t'):
    facts[(row['file'],int(row['start']))]=row
getters={
 '010': {21:'持久个体',22:'等级',23:'当前HP',24:'总HP',25:'倒下状态',26:'真实状态',27:'状态计数',28:'性别',29:'在场轮',30:'效果集合',31:'阶级集合',32:'中央阶级上限查询',33:'中央阶级下限查询',34:'当前战斗招式槽',49:'己侧索引',50:'己侧效果',51:'对侧索引',52:'对侧效果',221:'当前类型',222:'可选额外类型的当前类型',262:'能力身份',263:'能力数据',279:'持物身份',280:'持物数据'},
 '011': {20:'招式身份',21:'招式名称',22:'给定类型物理类别',23:'给定类型特殊类别',24:'伤害类别',25:'变化类别',26:'效果身份',30:'原数据类型'}
}
for file,mapping in getters.items():
    for start,field in mapping.items():
        facts[(file,start)]={'file':file,'start':str(start),'formal':'52a:15-17',
            'fact':f'直接委托当前真实对象的{field}；不建立独立隐藏副本或补资格',
            'consumer':'各AI handler输入；具体技能/有效性门由调用方'}
short={
 '51':'wp51-ai-action-selection-and-skill.md', '51d':'wp51-ai-decision-defaults.md',
 '52a':'wp52-a-generic-numerical-and-status-evaluation.md',
 '52b':'wp52-b-field-damage-healing-and-target-evaluation.md',
 '52c':'wp52-c-items-calling-and-control-evaluation.md'
}
def formal(s):
    out=[]
    for section in s.split(';'):
        key,spans=section.split(':')
        for span in spans.split(','):
            ns=list(map(int,span.split('-')))
            out.append({'path':'deliverables/final-specification-set/combat-requirements/'+short[key],
                        'start':ns[0],'end':ns[-1]})
    return out
forward=[]; missing=[]
for file in D['source_files'][:11]:
    key=Path(file['path']).name[:3]
    for unit in file['units']:
        f=facts.get((key,unit['start']))
        if not f:
            missing.append({'path':file['path'],**unit});continue
        forward.append({'id':f'CA-CORE-{key}-{unit["start"]}',
            'source':{'path':file['path'],'start':unit['start'],'end':unit['envelope_end'],
                      'range_kind':'lexical_envelope_including_adjacent_comments'},
            'unit':unit['unit'],'fact':f['fact'],'necessary_consumer':f['consumer'],
            'formal':formal(f['formal']),
            'judgment':'GAP_SUPPORT_GR6_C_001' if key=='002' and unit['start'] in [318,374] else 'STATIC_CORRESPONDENCE_WITH_STATED_PRECONDITIONS',
            'evidence':'SOURCE_STATIC; not dynamic PASS',
            'shared_preconditions':'core-review-notes.md'})
data_notes={int(r['line']):r for r in csv.DictReader((O/'reverse-wp51-data.tsv').open(),delimiter='\t')}
source_item='reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/003_AI_UseItem.rb'
W=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
reverse=[]
for b in D['formal_blocks']:
    if '/wp51-' not in b['path']:continue
    matches=[r for r in forward if any(q['path']==b['path'] and q['start']<=b['start_line']<=q['end'] for q in r['formal'])]
    matched_status=('GAP_SUPPORT_GR6_C_001' if any(r['judgment']=='GAP_SUPPORT_GR6_C_001' for r in matches) else 'STATIC_LINKS_PRESENT')
    result={**b,'status':matched_status if matches else 'NEEDS_EXPLICIT_DATA_OR_DOCUMENT_METADATA_CLASSIFICATION',
       'source_fact_ids':[r['id'] for r in matches],
       'source_facts':[r['fact'] for r in matches],
       'preconditions':'见关联fact及core-review-notes.md；不是仅由读取日志推导通过'}
    n=b['start_line']; text=(W/b['path']).read_text().splitlines()[n-1]
    is_data='defaults' in b['path']
    if is_data and n in data_notes:
        note=data_notes[n]
        result.update(status='STATIC_DATA_CORRESPONDENCE',source=[{'path':source_item,'start':int(note['source_start']),'end':int(note['source_end'])}],source_facts=[note['fact']],preconditions='资格扫描先行；AI估量非实际效果；两个代际配置分别保留')
    elif not matches and (text.startswith('#') or text=='---' or text.startswith('| ---') or (is_data and n in [11,32,45])):
        result.update(status='DOCUMENT_STRUCTURE_NO_BEHAVIOR_ASSERTION',source_facts=['标题、分隔符或数据列头；不伪造源行为PASS'])
    elif not matches and is_data and n in [84,86,88]:
        starts=[177,192,233,294,318,374,424,448,508,556,574] if n!=88 else [608,633,668,685]
        result.update(status='STATIC_REGISTRY_ORDER_CORRESPONDENCE',source=[{'path':'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/002_AI_Switch.rb','start':s} for s in starts],source_facts=['11愿换/4否决注册顺序逐一核对；先愿换首真再否决首真，不是所有条件都会执行'])
    elif not matches and not is_data and n==11:
        result.update(status='SCOPE_AND_CONSUMER_CONTRACT',source=[{'path':'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/001_Battle_AI.rb','start':48,'end':78}],source_facts=['动作输入/输出边界有源支撑；不宣称最优或公平，真实伤害/状态/执行引用其它主合同，不在AI目录重定义'])
    elif not matches and not is_data and n==150:
        result.update(status='CATALOG_CROSS_REFERENCE_CHECKED',source_facts=['30条AI向量均有vectors-core.tsv逐行新推导；不是已执行测试'])
    elif not matches and ((not is_data and n in [154,155,156]) or (is_data and n==92)):
        result.update(status='DEPENDENCY_AND_RESERVED_SCOPE',source_facts=['范围/依赖/历史定位；本文未据它把旧PASS或其它包状态当本轮新语义证据。当前AI行为仍完整核，不以未来Showdown缩域。'])
    elif not matches and n in [3,5]:
        result.update(status='CLASSIFICATION_AND_PROVENANCE_METADATA',source_facts=['分类/净化稿来源/静态未运行说明；历史批准字样非本轮验证结论，主事实另逐unit核。'])
    reverse.append(result)
def save(name,rows):
    (O/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
save('forward-core.jsonl',forward);save('reverse-core.jsonl',reverse)
(O/'core-matrix-counts.json').write_text(json.dumps({'source_lexical_units':sum(len(x['units']) for x in D['source_files'][:11]),'annotated':len(forward),'missing':missing,'reverse_blocks':len(reverse)},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'annotated':len(forward),'missing':missing},ensure_ascii=False))
