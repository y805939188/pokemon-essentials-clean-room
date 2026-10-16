"""D independent bounded renderer comparison: no target helper import/execution."""
import json,pathlib,hashlib
P=pathlib.Path(__file__).resolve().parent
def scope_text(s):
    if not isinstance(s, dict):
        return json.dumps(s, ensure_ascii=False)
    terms = []
    for k, v in s.items():
        if k == 'lines' and isinstance(v, list):
            terms.append('L' + '–'.join(map(str, v)))
        elif k == 'ranges' and isinstance(v, list):
            terms.append('行区间' + json.dumps(v, ensure_ascii=False, separators=(',', ':')))
        elif k in ('byte_range', 'byte_ranges', 'bytes'):
            terms.append('字节范围' + json.dumps(v, ensure_ascii=False, separators=(',', ':')))
        elif k in ('clause', 'anchor', 'operation', '限定', 'boundary', 'role', 'kind'):
            terms.append(str(v))
        else:
            terms.append(k + '=' + json.dumps(v, ensure_ascii=False, separators=(',', ':')))
    return '；'.join(terms) or '具体范围见同记录原始字段引用'

def mdvalue(v):
    if isinstance(v, str):
        return [v]
    if isinstance(v, list):
        if not v:
            return ['不适用：原集合为空，具体原因见同组。']
        return ['- `' + x['path'] + '` — ' + scope_text(x.get('scope', {})) + '；身份 `' + x.get('identity_id', '见原引用') + '`。' if isinstance(x, dict) and 'path' in x else '- ' + (x if isinstance(x, str) else json.dumps(x, ensure_ascii=False, separators=(',', ':'))) for x in v]
    if isinstance(v, dict):
        if 'items' in v:
            return mdvalue(v['items']) if v['items'] else [str(v.get('empty_reason', '原集合为空，见原始证据。'))]
        if 'file' in v:
            return ['`' + v['file'] + '#' + v.get('json_pointer', '') + '`（SHA256 ' + v['file_sha256'] + '）']
        if 'binding_id' in v:
            return ['`' + v['binding_id'] + '#' + v.get('json_pointer', '') + '`；原始成员字节' + str(v.get('raw_member_byte_offsets')) + '；成员SHA256 ' + v.get('raw_member_sha256', v.get('canonical_sha256', '见原成员'))]
        out = []
        for k, x in v.items():
            out += ['', '**' + k + '**', ''] + mdvalue(x)
        return out
    return [str(v)]

records=json.loads((P/'originals/15').read_text())['records']
lines=(P/'originals/9').read_text().splitlines();body=[];spans=[]
for i,r in enumerate(records):
 start=211+len(body)
 expected=[f"## {r['id']} — {r['groups']['一_身份']['中文标题']}",'',f"根分类 `{r['classification']}`，优先级 `{r['severity']}`。当前 `UPDATE_NOT_STARTED`；中文字段不新增裁决。",'']
 for title,g in r['groups'].items():
  expected+=['### '+title.replace('_',' '),'']
  for k,v in g.items():expected+=['**'+k+'**','']+mdvalue(v)+['']
 expected+=['---',''];body+=expected
 spans.append({'id':r['id'],'lines':[start,210+len(body)],'exact_C13_pointer':f'file15#/records/{i}/groups','body_approval':'OWN_D_DOES_NOT_RECEIVE_OTHER_PARTITION_BODY'})
actual=lines[210:11033]
proof={'schema':'gr8-d-whole-handoff-associations/v1','all_37_rendered_bodies_line_exact_equal':body==actual,'exact_lines':[211,11033],'record_spans':spans,'rendering_authority':'Pure static formatting comparison; displayed source functions were read, only copied AST formatting functions evaluated; no semantic_reader/state/file side effect','body_credit':0,'embedded_values':json.loads((P/'private/handoff-json-values.json').read_text())['ranges'],'control_ranges':[[1,24],[154,210],[11034,11049],[11337,11345],[11641,11645],[41969,41972],[53502,53505],[59915,59918],[60086,60089],[60251,60261]],'all_noncanonical_purpose_review':'Controls,9 embedded JSON values and graphs/qualifications read or exact whole association; canonical body receipt stays separately owned','execution':'NOT_EXECUTED'}
(P/'handoff-associations.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'all_37_rendered_bodies_line_exact_equal':body==actual,'expected_lines':len(body),'actual_lines':len(actual)}))
