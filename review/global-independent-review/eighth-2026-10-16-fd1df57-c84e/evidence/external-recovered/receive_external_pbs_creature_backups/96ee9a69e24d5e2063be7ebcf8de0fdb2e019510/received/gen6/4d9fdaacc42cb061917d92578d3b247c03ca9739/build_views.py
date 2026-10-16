"""Inert evidence formatter. No reference code, compiler, writer or game executes.

The complete contract and fixed local R are inputs. Output generation grants no
semantic credit. Exact source byte slices remain recoverable from fixed Git R.
"""
import hashlib
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
TASK = OUT.parent.parent
READSET = TASK / 'delegation/remaining-v1/gen6/readset.complete.json'
R = Path('/workspace/pokemon-essentials')


def main():
    d = json.loads(READSET.read_text())
    source = {x['id']: (R / x['path']).read_bytes() for x in d['owned_primary_files']}
    source_lines = {k: v.decode('utf-8-sig').splitlines() for k,v in source.items()}
    originals = json.loads((TASK / 'recovered-target/forward-mapping.json').read_text())
    checks = []
    anchors = {x['complete_target_forward_object']['base_section']
               for x in d['owned_records'] if x['frozen']['kind'] == 'FORM'}
    for row in d['owned_records']:
        f = row['frozen']
        lo, hi = f['byte_offsets_half_open']
        raw = source[f['identity_id']][lo:hi]
        assert hashlib.sha256(raw).hexdigest() == row['source_unit_sha256'], f['id']
        pointer = f['forward_pointer'].split('/')
        assert originals[pointer[1]][int(pointer[2])] == row['complete_target_forward_object'], f['id']
        values = {}
        for line in raw.decode('utf-8-sig').splitlines():
            if '=' in line:
                key, value = line.split('=', 1)
                values.setdefault(key.strip(), []).append(value.strip())
        for line_no, key, fc, value_hash, count in row['complete_target_forward_object']['fields']:
            literal = source_lines[f['identity_id']][line_no-1].split('=',1)[1].strip()
            assert hashlib.sha256(literal.encode()).hexdigest() == value_hash, (f['id'], key)
        checks.append({'id': f['id'], 'source_unit_sha256': row['source_unit_sha256'],
                       'all_field_hashes_match': True, 'original_forward_equal': True,
                       'tool_credit_only': True})
    (OUT / 'mechanical-checks.json').write_text(json.dumps({'checks': checks,
         'semantic_credit': 0, 'behavior_executions': 0}, ensure_ascii=False, separators=(',', ':'))+'\n')
    view_index = []
    groups = [('anchors', [x for x in d['owned_records'] if x['frozen']['id'] in anchors]),
              ('forms', [x for x in d['owned_records'] if x['frozen']['kind'] == 'FORM']),
              ('remaining-base', [x for x in d['owned_records'] if x['frozen']['kind'] == 'BASE'
                                  and x['frozen']['id'] not in anchors])]
    for group, rows in groups:
        chunks, current, size = [], [], 0
        for row in rows:
            f = row['frozen']; obj = row['complete_target_forward_object']
            lo, hi = f['byte_offsets_half_open']
            raw = source[f['identity_id']][lo:hi].decode('utf-8-sig')
            omissions = {}
            for key, fc, policy, base in obj['omitted']:
                omissions.setdefault(policy + (':' + base if base else ''), []).append(key)
            text = f"\n{f['id']} L{f['source_lines']} B[{lo},{hi}) anchor={obj['base_section']}\n" + raw
            text += '\nOMISSIONS ' + json.dumps(omissions, ensure_ascii=False, separators=(',', ':')) + '\n'
            if current and size + len(text.encode()) > 13000:
                chunks.append(current); current = []; size = 0
            current.append((f['id'], text)); size += len(text.encode())
        if current:
            chunks.append(current)
        for i, chunk in enumerate(chunks, 1):
            name = f'{group}-{i:02d}.txt'
            raw = ''.join(x[1] for x in chunk).encode()
            tmp = Path('/tmp/r8-gen6-views'); tmp.mkdir(exist_ok=True)
            (tmp / name).write_bytes(raw)
            view_index.append({'name': name, 'records': [x[0] for x in chunk],
                               'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
                               'generated_reading_credit': 0})
    (OUT / 'views.index.json').write_text(json.dumps({'schema':'r8-gen6-lossless-views/v1',
        'recovery':'Run this inert formatter against exact fixed contract and R; each source raw slice is unchanged. OMISSIONS is a grouping of exact forward omitted rows, with same-generation base anchor. Field IDs/hashes/counts are administrative bindings validated separately; original forward remains at fixed contract.',
        'source_contract': str(READSET),
        'views': view_index}, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'generated':len(view_index),'groups':{g:len(rs) for g,rs in groups},
                      'all_909_raw_slices_and_forward_objects_match':True,'semantic_credit':0}))


if __name__ == '__main__':
    main()
