"""Structural equality checks after manual full-table semantic reading.
Reads only fixed literal table ranges, no eval or project imports; outputs task
data-check.jsonl/data-check-summary.json. Equality is not a semantic PASS.
"""
import re,json,hashlib
from pathlib import Path
W=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
O=Path(__file__).resolve().parent
S='reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/008_AI_Utilities.rb'
A='deliverables/final-specification-set/combat-requirements/wp52-a-evaluation-coverage-and-data.md'
C='deliverables/final-specification-set/combat-requirements/wp52-c-item-control-coverage-and-data.md'
lines=(W/S).read_text().splitlines()
def source_groups(first,last):
    data={}; grade=None
    for n in range(first,last+1):
        line=lines[n-1].split('#')[0]
        m=re.match(r'\s*(-?\d+)\s*=>\s*\[',line)
        if m:grade=int(m[1])
        if grade is not None:
            for name in re.findall(r':([A-Z][A-Z0-9_]*)',line):
                assert name not in data
                data[name]=(grade,n)
    return data
def formal_groups(path,first,last):
    data={}
    for n,line in enumerate((W/path).read_text().splitlines(),1):
        if not first<=n<=last:continue
        cells=[x.strip() for x in line.split('|')]
        if len(cells)<4:continue
        value=int(cells[1].replace('−','-'))
        for name in cells[2].split(', '):
            assert name not in data
            data[name]=(value,n)
    return data
rows=[]
for label,srange,path,frange in [('ability',(101,159),A,(221,233)),('item',(163,228),C,(96,110))]:
    left=source_groups(*srange);right=formal_groups(path,*frange)
    for name in sorted(set(left)|set(right)):
        rows.append({'type':'literal_default_binding_comparison','domain':label,'identity':name,
          'source':{'path':S,'line':left.get(name,(None,None))[1],'value':left.get(name,(None,None))[0]},
          'formal':{'path':path,'line':right.get(name,(None,None))[1],'value':right.get(name,(None,None))[0]},
          'equal':name in left and name in right and left[name][0]==right[name][0],
          'semantic_consumer':'中等才修正评级；未知0；各名字不按常识改写。见人工core-facts及core-review-notes。'})
boost={}
for n in range(837,855):
    line=lines[n-1]
    m=re.search(r':([A-Z]+)\s*=>\s*\[(.*?)\]',line)
    if m:
        for name in re.findall(r':([A-Z0-9]+)',m[2]):boost[name]=(m[1],n)
gems={}
for n in range(876,894):
    m=re.search(r':([A-Z0-9]+)\s*=>\s*:([A-Z]+)',lines[n-1])
    if m:gems[m[1]]=(m[2],n)
for n,line in enumerate((W/C).read_text().splitlines(),1):
    if not 120<=n<=176:continue
    cells=[x.strip() for x in line.split('|')]
    group,name,type_=cells[1:4]
    val=(boost if group=='type_boosting_items' else gems).get(name)
    rows.append({'type':'conditional_type_binding_comparison','group':group,'identity':name,
      'source':{'path':S,'line':val[1] if val else None,'value':val[0] if val else None},
      'formal':{'path':C,'line':n,'value':type_},'equal':bool(val and val[0]==type_),
      'semantic_consumer':'直接键先取；组仅首次匹配，评级需中等与可用伤害类型门；宝石世代门另核。'})
(O/'data-check.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
summary={'checks':len(rows),'unequal':[x for x in rows if not x['equal']],
 'ability_defaults':sum(x.get('domain')=='ability' for x in rows),
 'item_defaults':sum(x.get('domain')=='item' for x in rows),
 'conditional_bindings':sum(x['type']=='conditional_type_binding_comparison' for x in rows),
 'scope':'TOOL_VALIDATION_LITERAL_BINDINGS_ONLY_NOT_SEMANTIC_PASS'}
(O/'data-check-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
