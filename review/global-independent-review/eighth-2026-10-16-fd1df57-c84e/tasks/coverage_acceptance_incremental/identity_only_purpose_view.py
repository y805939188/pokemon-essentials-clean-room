"""Strict administrative-table purpose audit; never source or row-reading credit."""
import datetime
import hashlib
import json
from pathlib import Path

OWN = Path(__file__).resolve().parent
BASE = OWN.parent.parent
ledger = json.loads((OWN / 'reading-ledger.json').read_text())
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
expected = {
    4: {'bytes', 'end_exclusive', 'id', 'kind', 'path', 'semantic_contributor', 'sha256', 'start', 'status', 'this_reader_semantic_credit'},
    141: {'actual_mode', 'bytes', 'commit', 'computed_git_blob', 'path', 'purpose', 'sha256'},
    146: {'blob', 'commit', 'consumers', 'facts', 'path', 'repo', 'semantic_status', 'sha256', 'spec_clauses', 'tree', 'unit_expansion', 'unit_id'},
    150: {'blob', 'clause_expansion', 'commit', 'consumers', 'path', 'premises', 'repo', 'semantic_status', 'sha256', 'source_facts', 'tree', 'unit_id'},
    212: {'bytes', 'git_blob_content_id', 'logical_path', 'semantic_reading_credit', 'sha256', 'status', 'transport_path'},
}
out = []
rows_out = []
for index, keys in expected.items():
    source = ledger['snapshot_payloads'][index]
    raw = (BASE / source['snapshot']).read_bytes()
    assert len(raw) == source['bytes'] and hashlib.sha256(raw).hexdigest() == source['sha256']
    obj = json.loads(raw)
    rows = obj if isinstance(obj, list) else obj['files' if index in (141, 212) else 'rows']
    assert all(set(row) == keys for row in rows)
    if index == 4:
        assert len(rows) == 787
        assert all(row['this_reader_semantic_credit'] is False and row['status'] == 'IDENTITY_VERIFIED_STRUCTURE_RECEIVED' for row in rows)
        assert all(row['end_exclusive'] - row['start'] == row['bytes'] for row in rows)
        semantic_keys = ['kind', 'status', 'semantic_contributor', 'this_reader_semantic_credit']
        constants = {key: sorted({json.dumps(row[key], ensure_ascii=False) for row in rows}) for key in semantic_keys}
    elif index == 141:
        assert len(rows) == 61
        constants = {key: sorted({json.dumps(row[key], ensure_ascii=False) for row in rows}) for key in ['actual_mode', 'commit', 'purpose']}
    elif index == 146:
        assert len(rows) == 432
        assert all(row['facts'] is None and row['consumers'] is None and row['spec_clauses'] is None and row['unit_id'] == 'FILE:' + row['path'] for row in rows)
        constants = {key: sorted({json.dumps(row[key], ensure_ascii=False) for row in rows}) for key in ['repo', 'commit', 'tree', 'unit_expansion', 'facts', 'consumers', 'spec_clauses', 'semantic_status']}
    elif index == 150:
        assert len(rows) == 131
        assert all(row['source_facts'] is None and row['premises'] is None and row['consumers'] is None and row['unit_id'] == 'FILE:' + row['path'] for row in rows)
        constants = {key: sorted({json.dumps(row[key], ensure_ascii=False) for row in rows}) for key in ['repo', 'commit', 'tree', 'clause_expansion', 'source_facts', 'premises', 'consumers', 'semantic_status']}
    else:
        assert len(rows) == 125
        assert all(row['semantic_reading_credit'] is False and row['status'] == 'RESTORED_EXACT_BYTES' for row in rows)
        constants = {key: sorted({json.dumps(row[key], ensure_ascii=False) for row in rows}) for key in ['status', 'semantic_reading_credit']}
    root = {} if isinstance(obj, list) else {key: value for key, value in obj.items() if key not in ('files', 'rows')}
    out.append({'index': index, 'exact_source': source, 'rows': len(rows), 'strict_all_row_keyset': sorted(keys), 'all_nonidentity_field_values': constants, 'all_root_values': root, 'purpose': 'IDENTITY/LOCATION/RESTORE ADMINISTRATION ONLY; no embedded source text or positive semantic proof. Every row remains not personally literal-read; strict shape and constants justify this purpose disposition, not a reading claim.'})
    for number, row in enumerate(rows):
        rows_out.append({'snapshot_index': index, 'json_pointer': ('/' if isinstance(obj, list) else '/files/' if index in (141, 212) else '/rows/') + str(number), 'row_sha256': hashlib.sha256(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest(), 'purpose': 'IDENTITY_ONLY_NO_SOURCE_OR_ATOMIC_OR_ROW_READING_CREDIT'})
result = {'schema': 'gr8-strict-administrative-table-purpose/v1', 'began_utc': started, 'ended_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'inputs': out, 'total_rows': len(rows_out), 'literal_all_rows_read': False, 'purpose_disposed_not_source_read': True, 'exit_code': 0}
target = OWN / 'strict-identity-purpose-view.json'
assert not target.exists()
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
(OWN / 'strict-identity-exact-row-purpose-dispositions.json').write_text(json.dumps(rows_out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output': target.name, 'lines': len(target.read_text().splitlines()), 'bytes': target.stat().st_size, 'row_dispositions': len(rows_out), 'exit_code': 0}))
