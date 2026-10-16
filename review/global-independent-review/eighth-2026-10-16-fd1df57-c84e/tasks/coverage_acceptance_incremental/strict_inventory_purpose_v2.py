"""Strictly type two inert identity/status inventories; no source reading credit."""
import datetime
import hashlib
import json
import re
from pathlib import Path

OWN = Path(__file__).resolve().parent
BASE = OWN.parent.parent
ledger = json.loads((OWN / 'reading-ledger.json').read_text())
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
expected = {
    88: {
        'root_keys': {'inputs', 'note', 'files'},
        'row_keys': {'repo', 'path', 'bytes', 'sha256', 'blob', 'lines', 'group', 'read_status'},
        'array': 'files',
        'count': 132,
        'nonidentity': ['repo', 'group', 'read_status'],
    },
    155: {
        'root_keys': {'schema', 'frozen_utc', 'scope', 'items'},
        'row_keys': {'repo', 'commit', 'tree', 'path', 'mode', 'blob', 'bytes', 'sha256', 'line_count', 'purpose', 'reading_status', 'read_ranges'},
        'array': 'items',
        'count': 163,
        'nonidentity': ['repo', 'commit', 'tree', 'mode', 'purpose', 'reading_status', 'read_ranges'],
    },
}
out = []
rows_out = []
for index, rule in expected.items():
    source = ledger['snapshot_payloads'][index]
    raw = (BASE / source['snapshot']).read_bytes()
    assert len(raw) == source['bytes']
    assert hashlib.sha256(raw).hexdigest() == source['sha256']
    obj = json.loads(raw)
    assert set(obj) == rule['root_keys']
    rows = obj[rule['array']]
    assert len(rows) == rule['count']
    for number, row in enumerate(rows):
        assert set(row) == rule['row_keys']
        assert row['repo'] in ('/workspace/pokemon-essentials', '/workspace/pokemon-essentials-clean-room')
        assert isinstance(row['path'], str) and row['path'] and '\n' not in row['path']
        assert not row['path'].startswith('/') and '..' not in Path(row['path']).parts
        assert re.fullmatch('[0-9a-f]{64}', row['sha256'])
        assert re.fullmatch('[0-9a-f]{40}', row['blob'])
        assert type(row['bytes']) is int and row['bytes'] >= 0
        line_key = 'lines' if index == 88 else 'line_count'
        assert type(row[line_key]) is int and row[line_key] >= 0
        if index == 155:
            assert row['reading_status'] == 'UNREAD' and row['read_ranges'] == []
            assert row['mode'] == '100644'
            assert re.fullmatch('[0-9a-f]{40}', row['commit'])
            assert re.fullmatch('[0-9a-f]{40}', row['tree'])
        rows_out.append({
            'snapshot_index': index,
            'json_pointer': '/' + rule['array'] + '/' + str(number),
            'row_sha256': hashlib.sha256(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
            'purpose': 'TYPED_IDENTITY_AND_DECLARED_STATUS_ONLY; NOT_LITERAL_ROW_READING_OR_SOURCE_OR_SEMANTIC_ACCEPTANCE',
        })
    constants = {key: sorted({json.dumps(row[key], ensure_ascii=False) for row in rows}) for key in rule['nonidentity']}
    root = {key: value for key, value in obj.items() if key != rule['array']}
    out.append({
        'index': index,
        'source_identity': {key: source[key] for key in ('original_path', 'snapshot', 'bytes', 'sha256', 'git_blob', 'captured_utc')},
        'rows': len(rows),
        'all_row_keys_validated': sorted(rule['row_keys']),
        'all_nonidentity_field_values': constants,
        'all_root_fields': root,
        'qualification': 'Identity paths/hash/size/line counts not personally literal-read. All nonidentity unique values and root metadata require actual reading of this view. Typed row shape has no source/assertion/premise/consumer bodies. Declared FULL_READ labels grant no independent source credit; frozen UNREAD is not a live total.',
    })
view = {
    'schema': 'gr8-strict-inventory-purpose/v2',
    'began_utc': started,
    'ended_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'inputs': out,
    'total_rows': len(rows_out),
    'literal_all_rows_read': False,
    'source_or_atomic_semantic_credit': False,
    'semantic_current_values_read_by_generation': False,
    'exit_code': 0,
}
target = OWN / 'strict-inventory-purpose-v2-view.json'
assert not target.exists()
target.write_text(json.dumps(view, ensure_ascii=False, indent=2) + '\n')
row_target = OWN / 'strict-inventory-purpose-v2-row-dispositions.json'
assert not row_target.exists()
row_target.write_text(json.dumps(rows_out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output': target.name, 'lines': len(target.read_text().splitlines()), 'bytes': target.stat().st_size, 'rows': len(rows_out), 'exit_code': 0}))
