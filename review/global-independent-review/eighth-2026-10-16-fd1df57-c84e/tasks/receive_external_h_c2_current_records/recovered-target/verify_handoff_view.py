"""Compare the complete view to already-read exact C13 objects; no behavior run."""
from pathlib import Path
import json, difflib, hashlib
import semantic_reader as sr
T=Path(__file__).parent;W=T/'.publication-work'/'strata'
state=json.loads(sr.STATE.read_text());lines=Path(sr.INVENTORY[9]['materialized_path']).read_text().splitlines()
records=sr.load_doc(15)['records']

def scope_text(s):
    if not isinstance(s,dict):return json.dumps(s,ensure_ascii=False)
    terms=[]
    for k,v in s.items():
        if k=='lines' and isinstance(v,list):terms.append('L'+'–'.join(map(str,v)))
        elif k=='ranges' and isinstance(v,list):terms.append('行区间'+json.dumps(v,ensure_ascii=False,separators=(',',':')))
        elif k in ('byte_range','byte_ranges','bytes'):terms.append('字节范围'+json.dumps(v,ensure_ascii=False,separators=(',',':')))
        elif k in ('clause','anchor','operation','限定','boundary','role','kind'):terms.append(str(v))
        else:terms.append(k+'='+json.dumps(v,ensure_ascii=False,separators=(',',':')))
    return '；'.join(terms) or '具体范围见同记录原始字段引用'

def mdvalue(v):
    if isinstance(v,str):return [v]
    if isinstance(v,list):
        if not v:return ['不适用：原集合为空，具体原因见同组。']
        return ['- `'+x['path']+'` — '+scope_text(x.get('scope',{}))+'；身份 `'+x.get('identity_id','见原引用')+'`。' if isinstance(x,dict) and 'path' in x else '- '+(x if isinstance(x,str) else json.dumps(x,ensure_ascii=False,separators=(',',':'))) for x in v]
    if isinstance(v,dict):
        if 'items' in v:return mdvalue(v['items']) if v['items'] else [str(v.get('empty_reason','原集合为空，见原始证据。'))]
        if 'file' in v:return ['`'+v['file']+'#'+v.get('json_pointer','')+'`（SHA256 '+v['file_sha256']+'）']
        if 'binding_id' in v:return ['`'+v['binding_id']+'#'+v.get('json_pointer','')+'`；原始成员字节'+str(v.get('raw_member_byte_offsets'))+'；成员SHA256 '+v.get('raw_member_sha256',v.get('canonical_sha256','见原成员'))]
        out=[]
        for k,x in v.items():out+=['','**'+k+'**','']+mdvalue(x)
        return out
    return [str(v)]

body=[];receipts=[]
for n,r in enumerate(records):
    expected=[f"## {r['id']} — {r['groups']['一_身份']['中文标题']}",'',f"根分类 `{r['classification']}`，优先级 `{r['severity']}`。当前 `UPDATE_NOT_STARTED`；中文字段不新增裁决。",'']
    for title,g in r['groups'].items():
        expected+=['### '+title.replace('_',' '),'']
        for k,v in g.items():expected+=['**'+k+'**','']+mdvalue(v)+['']
    expected+=['---',''];body+=expected
    receipts.append({'id':r['id'],'C13_pointer':f'/records/{n}/groups','groups':len(r['groups']),
        'purpose':'EXACT_RENDERING_ASSOCIATION_TO_THIS_CONTEXT_FULL_C13_GROUP_READING; no fresh source or behavior approval'})
actual=lines[210:11033]
ok=body==actual
if not ok:
    (W/'view-differences.txt').write_text('\n'.join(difflib.unified_diff(body,actual,fromfile='expected_from_read_C13',tofile='handoff_211_11034')))

fences=[];start=None
for j,l in enumerate(lines,1):
    if l.startswith('```'):
        if start is None:start=j
        else:fences.append((start,j));start=None
parsed=[]
for n,(a,b) in enumerate(fences):parsed.append({'line_range':[a,b],'value':json.loads('\n'.join(lines[a:b-1]))})
for a,b in ((11050,11336),(11346,11640)):
    parsed.append({'line_range':[a,b],'value':json.loads('\n'.join(lines[a-1:b]))})
display=json.dumps(sr.render(parsed,'file9#exact_embedded_JSON_ranges',state,{}),ensure_ascii=False,separators=(',',':'))
for j in range(0,len(display),16000):(W/f'handoff_embedded.{j//16000}.txt').write_text(display[j:j+16000])
control_ranges=[(1,24),(154,210),(11034,11049),(11337,11345),(11641,11645),(41969,41972),(53502,53505),(59915,59918),(60086,60089),(60251,60261)]
(W/'handoff_control.txt').write_text('\n'.join(f'{j}:{lines[j-1]}' for a,b in control_ranges for j in range(a,b+1)))
result={'schema':'r8.external-h-c2.handoff-view-comparison.v1','handoff_identity':sr.INVENTORY[9],
    'C13_identity':sr.INVENTORY[15],'complete_37_rendered_body_equal':ok,'compared_line_range':[211,11033],
    'comparison':'Exact complete line array equality, no whitespace or value normalization; already-read groups linked, not old PASS',
    'record_group_associations':receipts,'embedded_json_ranges':[x['line_range'] for x in parsed],
    'embedded_parts':(len(display)+15999)//16000,'embedded_values_pending_display':True,'control_ranges_pending_display':control_ranges,
    'generator_context_read_only':'C13/build_views.py lines185-273 bounded read; generator not imported or executed',
    'behavior_execution':'NOT_EXECUTED','final_root_reception':'NOT_RECEIVED'}
(T/'handoff-view-comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
sr.STATE.write_text(json.dumps(state,ensure_ascii=False,indent=1)+'\n')
print(json.dumps({'body_equal':ok,'record_groups':37*7,'embedded_JSON_objects':len(parsed),'embedded_chars':len(display),'embedded_parts':result['embedded_parts']}))
