"""Exact semantic-value display with separately inventoried identity atoms.

No prose summarization. Repeated exact JSON values may reference an actually
acknowledged earlier display. Hash/byte identity atoms are inventoried, never
given source-behavior credit. A display is not credited until explicit ack.
"""
from pathlib import Path
import argparse, json, hashlib, datetime, re

TASK = Path(__file__).parent
WORK = TASK / '.publication-work' / 'reading'
WORK.mkdir(exist_ok=True, parents=True)
INVENTORY = json.loads((TASK / 'material-inventory.json').read_text())
STATE = WORK / 'state.json'

def canon(v):
    return json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()

def digest(v):
    return hashlib.sha256(canon(v)).hexdigest()

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def pointer(obj, ptr):
    for part in ptr.split('/')[1:]:
        part = part.replace('~1', '/').replace('~0', '~')
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj

def add_pool(v, anchor, pool):
    if isinstance(v, (list, dict)) or isinstance(v, str) and len(v) > 20:
        pool.setdefault(digest(v), anchor)
    if isinstance(v, dict):
        if 'path' in v and 'scope' in v:
            pool.setdefault(digest({'path': v['path'], 'scope': v['scope']}), anchor + '[path,scope]')
        for k, x in v.items():
            add_pool(x, anchor + '/' + k.replace('~', '~0').replace('/', '~1'), pool)
    elif isinstance(v, list):
        for i, x in enumerate(v):
            add_pool(x, anchor + '/' + str(i), pool)

def load_doc(i):
    return json.loads(Path(INVENTORY[i]['materialized_path']).read_text())

def initial():
    pool = {}
    # Exact previously read ranges in the same actual context, not old PASS.
    for i in [2, 3, 4, 7, 8, 17, 23, 24]:
        if i == 2:
            continue
        add_pool(load_doc(i), f'file{i}#', pool)
    add_pool(load_doc(0)['records'][0], 'file0#/records/0', pool)
    add_pool(load_doc(1)['records'][0], 'file1#/records/0', pool)
    add_pool(load_doc(18), 'file18#', pool)  # input identity rows remain inventory only
    return {'pool': pool, 'acks': [], 'metadata': [], 'pending': {}}

def is_meta(k, v):
    return ((k in {'bytes', 'file_bytes', 'raw_member_bytes', 'raw_member_byte_offsets',
                   'byte_offsets', 'mode', 'logical_posix_mode', 'identity_id',
                   'git_blob', 'git_blob_content_id', 'transport_bytes', 'transport_git_blob_content_id'}
             or k.endswith('sha256') or k.endswith('_sha256'))
            and isinstance(v, (str, int, list)))

def render(v, p, state, local):
    h = digest(v)
    if h in state['pool'] and len(canon(v)) > 80:
        return '=read:' + h[:12]
    if h in local and len(canon(v)) > 80:
        return '=here:' + h[:12]
    local.setdefault(h, p)
    if isinstance(v, list) and v and all(isinstance(x, dict) and set(x) == {'字段', '完整值引用'} for x in v):
        idx = len(state['metadata'])
        state['metadata'].append({'pointer': p, 'value': v,
                                  'purpose': 'typed_field_name_to_immutable_pointer_index_only'})
        return '@field-binding-index:' + str(idx)
    if isinstance(v, dict):
        if {'path', 'scope'}.issubset(v) and set(v).issubset({'path','scope','identity_id','original_scope_ref'}):
            idx = len(state['metadata'])
            state['metadata'].append({'pointer': p, 'value': v,
                                      'purpose': 'location_and_immutable_binding_exact_original'})
            loc = {'path': v['path'], 'scope': v['scope']}
            lh = digest(loc)
            if lh in state['pool']:
                return '=read-location:' + lh[:12]
            if lh in local and local[lh] != p:
                return '=here-location:' + lh[:12]
            local[lh] = p
            return loc
        ref_keys = {'document', 'sha256', 'bytes', 'json_pointer', 'original_report_path',
                    'binding_id', 'canonical_sha256', 'input_sha256', 'raw_member_byte_offsets',
                    'raw_member_bytes', 'raw_member_sha256', 'file', 'file_bytes', 'file_sha256'}
        if set(v).issubset(ref_keys) and ('document' in v or 'binding_id' in v or 'file_sha256' in v):
            idx = len(state['metadata'])
            state['metadata'].append({'pointer': p, 'value': v,
                                      'purpose': 'immutable_reference_binding_not_payload_semantics'})
            return '@immutable-reference:' + str(idx)
        out = {}
        meta_start = len(state['metadata'])
        for k, x in v.items():
            q = p + '/' + k.replace('~', '~0').replace('/', '~1')
            if (k.endswith('_utc') and isinstance(x, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}T[\d:.+Z-]+', x)) or k in {'visible_entries', 'actual_session_log', 'public_log_projection', 'source_log', 'platform_uuid_evidence'}:
                idx = len(state['metadata'])
                state['metadata'].append({'pointer': q, 'value': x,
                    'purpose': 'timestamp_or_log_locator_inventory_only_not_scope_status_or_qualification'})
            elif k == 'argv' and isinstance(x, list):
                idx = len(state['metadata'])
                state['metadata'].append({'pointer': q, 'value': x,
                    'purpose': 'historical_command_invocation_inventory_only_not_output_or_current_rule'})
                out[k] = '@historical-command-invocation:' + str(idx)
            elif is_meta(k, x):
                idx = len(state['metadata'])
                state['metadata'].append({'pointer': q, 'value': x,
                                          'purpose': 'identity_atom_only_no_behavior_credit'})
            else:
                out[k] = render(x, q, state, local)
        return out
    if isinstance(v, list):
        return [render(x, p + '/' + str(i), state, local) for i, x in enumerate(v)]
    return v

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('action', choices=['prepare', 'show', 'ack', 'status'])
    ap.add_argument('label', nargs='?')
    ap.add_argument('--file', type=int)
    ap.add_argument('--pointer', default='')
    ap.add_argument('--part', type=int, default=0)
    args = ap.parse_args()
    state = json.loads(STATE.read_text()) if STATE.exists() else initial()
    if args.action == 'prepare':
        assert args.label not in state['pending']
        obj = pointer(load_doc(args.file), args.pointer)
        anchor = f'file{args.file}#{args.pointer}'
        text = json.dumps(render(obj, anchor, state, {}), ensure_ascii=False, separators=(',', ':'))
        # Continuous Unicode character windows, never ellipsized content.
        parts = [text[i:i+24000] for i in range(0, len(text), 24000)] or ['']
        paths = []
        for i, part in enumerate(parts):
            path = WORK / f'{args.label}.{i}.txt'
            path.write_text(part)
            paths.append(str(path))
        state['pending'][args.label] = {'file': args.file, 'pointer': args.pointer,
            'anchor': anchor, 'parts': paths, 'shown': [], 'original_subtree_sha256': digest(obj),
            'prepared_utc': now(), 'display_sha256': hashlib.sha256(text.encode()).hexdigest(),
            'chars': len(text), 'parts_count': len(parts)}
        print(json.dumps({k:v for k,v in state['pending'][args.label].items() if k != 'parts'}))
    elif args.action == 'show':
        row = state['pending'][args.label]
        print(f"EXACT DISPLAY {args.label} part {args.part + 1}/{len(row['parts'])}; {row['anchor']}")
        print(Path(row['parts'][args.part]).read_text())
        row['shown'].append(args.part)
    elif args.action == 'ack':
        row = state['pending'].pop(args.label)
        assert set(row['shown']) == set(range(len(row['parts'])))
        obj = pointer(load_doc(row['file']), row['pointer'])
        assert digest(obj) == row['original_subtree_sha256']
        add_pool(obj, row['anchor'], state['pool'])
        row.update(ack_utc=now(), reader='external /root actual continuing context',
                   status='SEMANTIC_VALUES_READ_IDENTITY_ATOMS_INVENTORIED',
                   final_root_reception='NOT_RECEIVED', behavior_execution='NOT_EXECUTED')
        state['acks'].append(row)
        print(json.dumps({'acknowledged': args.label, 'scope': row['anchor'], 'acks': len(state['acks'])}))
    else:
        print(json.dumps({'acks': [(x['file'], x['pointer']) for x in state['acks']],
                          'pending': list(state['pending']), 'metadata_atoms': len(state['metadata'])}))
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1) + '\n')
    (TASK / 'continued-reading-ledger.json').write_text(json.dumps({
        'schema': 'r8.external-h-c2.continued-reading.v1', 'recorded_utc': now(),
        'rule': 'Only explicitly acknowledged complete displays count. Exact repeated JSON values are linked to named read scopes. Identity atoms are separate inventory. No parser/old PASS or execution credit.',
        'acks': state['acks'], 'pending': state['pending']}, ensure_ascii=False, indent=2) + '\n')

if __name__ == '__main__':
    main()
