"""Check every displayed semantic value against this auditor's inert decode."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
units = json.loads((ROOT/'binary-redecode-0704/yarb-decoded.json').read_text())
lines = []
compact = lambda x: json.dumps(x, ensure_ascii=False, separators=(',', ':'))
for unit in units:
    lines.append('UNIT '+unit['name']+' '+str(unit['start'])+'..'+str(unit['end_exclusive'])+' '+unit['sha256'])
    for obj in unit['objects']:
        semantic = {k:v for k,v in obj.items() if k not in ('index','offset','end_exclusive','raw_hex')}
        lines.append('O'+str(obj['index'])+' '+compact(semantic))
    for q in unit['iseqs']:
        f = q['fields']
        params = {k:f[k] for k in ('param_flags','param_size','param_lead_num','param_opt_num','param_rest_start','param_post_start','param_post_num','param_block_start')}
        semantic = {'label':q['label'],'line':f['location_first_lineno'],'type':f['type'],'parent':f['parent_iseq_index'],'local':f['local_iseq_index'],'mandatory':f['mandatory_only_iseq_index'],'params':params,'locals':q['locals'],'opt':q['optional_jumps'],'keyword':q['keyword'],'catch':q['catch_table'],'outer':q['outer_variables'],'stack':f['stack_max']}
        lines.append('Q'+str(q['index'])+' '+compact(semantic))
        for ins in q['code']:
            operands = []
            for arg in ins['operands']:
                typ = arg['type']
                if typ == 'R':
                    operands.append('R:'+str(arg['index'])+':'+arg['name'])
                elif typ in 'VIH':
                    operands.append(typ+':'+compact(arg['value'])+'@'+str(arg['raw_value']))
                else:
                    operands.append(typ+':'+compact(arg['value']))
            lines.append(str(ins['pc'])+' '+ins['name']+' '+','.join(operands))
raw = ('\n'.join(lines)+'\n').encode()
target = ROOT/'binary-redecode-0704/semantic-projection.txt'
assert not target.exists()
target.write_bytes(raw)
expected = (ROOT/'delta-inputs/binary-final-0703/ruby-independent-reception__semantic-view.txt').read_bytes()
assert raw == expected
result = {'began_utc':started,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'output':str(target.relative_to(ROOT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'all_displayed_semantic_values_equal_own_inert_decode':True,'nonsemantic_offsets_rawhex_source_line_events_not_claimed_literally_read':True,'actual_semantic_reading_is_separate':True,'exit_code':0}
(ROOT/'binary-redecode-0704/semantic-projection-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
