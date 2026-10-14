import datetime, hashlib, json
from pathlib import Path

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
BASE = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'
OUT = BASE / 'tasks/R6-C'
OWNER = BASE / 'tasks/R6-K/context-116-joins.json'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
raw = OWNER.read_bytes()
owner = json.loads(raw)
blocks = {v['id']: v for v in json.loads((BASE / 'inventory/formal-block-denominator.json').read_text())}
records = [json.loads(v) for v in (OUT / 'test-vector-map.jsonl').read_text().splitlines()]
rows = {v['id']: v for v in records}
identities, issues, received = {}, [], []

for v in owner['vectors']:
    record = rows[v['id']]
    formal = ROOT / v['formal_path']
    line = formal.read_text().splitlines()[v['formal_line'] - 1]
    digest = hashlib.sha256(line.encode()).hexdigest()
    block = blocks[v['formal_block_id']]
    checks = {
        'row_hash': digest == v['row_sha256'],
        'C_original_row_hash': digest == record['literal_inputs_hash'],
        'C_exact_path_line': record['path'] == v['formal_path'] and record['line'] == v['formal_line'],
        'root_exact_block': block['path'] == v['formal_path'] and block['start_line'] <= v['formal_line'] <= block['end_line'],
        'no_parent_pending': all('PENDING' not in p['status'] for p in v['parent_facts']),
        'has_consumer_join': bool(v['manual_consumer_join'] and v['source_and_necessary_consumer_refs']),
        'not_executed': v['reference_vector_execution'] == 'NOT_EXECUTED',
    }
    for ref in v['source_and_necessary_consumer_refs']:
        path = ref['path']
        if path not in identities:
            data = (ROOT / path).read_bytes()
            identities[path] = {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(), 'lines': len(data.decode('utf-8').splitlines()), 'purpose': 'IMPORTED_OWNER_LOCATOR_IDENTITY_ONLY_NOT_C_SOURCE_READ'}
        if not (1 <= ref['start_line'] <= ref['end_line'] <= identities[path]['lines']):
            issues.append({'id': v['id'], 'invalid_source_range': ref})
    if not all(checks.values()):
        issues.append({'id': v['id'], 'failed_checks': checks})
    received.append({'id': v['id'], 'checks': checks, 'owner_formal': {k: v[k] for k in ('formal_path', 'formal_line', 'formal_block_id', 'row_sha256')}, 'stated_preconditions': v['stated_preconditions'], 'derived_expected': v['derived_expected'], 'manual_consumer_join': v['manual_consumer_join'], 'primary_unit_ids': v['primary_unit_ids'], 'source_refs': v['source_and_necessary_consumer_refs'], 'source_read_credit': 0, 'execution_credit': 0})

if issues:
    raise AssertionError(issues)
receipt_rel = str((OUT / 'received-K-exact116.json').relative_to(ROOT))
for v in received:
    rows[v['id']]['exact_vector_receipt'] = {'artifact': receipt_rel, 'owner_artifact': str(OWNER.relative_to(ROOT)), 'owner_sha256': hashlib.sha256(raw).hexdigest(), 'id': v['id'], 'formal_block_id': v['owner_formal']['formal_block_id'], 'primary_unit_ids': v['primary_unit_ids'], 'source_refs': v['source_refs'], 'C_new_source_read_credit': 0, 'C_execution_credit': 0}
(OUT / 'test-vector-map.jsonl').write_text(''.join(json.dumps(v, ensure_ascii=False) + '\n' for v in records))
receipt = {'at': now, 'owner_artifact': str(OWNER.relative_to(ROOT)), 'owner_sha256': hashlib.sha256(raw).hexdigest(), 'counts': owner['counts'], 'actual_projection_read': 'All116 id/path/line/block/premises/derived expected/manual consumer join/parent IDs/evidence/execution fields reviewed in BE37,CX42,RM37 tool outputs; repeated parent full facts already actually read in prior current-K receipt.', 'vectors': received, 'source_identities': list(identities.values()), 'source_read_credit': 0, 'execution_credit': 0, 'issues': issues}
(OUT / 'received-K-exact116.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
with (OUT / 'reading-ledger.jsonl').open('a') as f:
    for prefix, count in owner['counts'].items():
        f.write(json.dumps({'at': now, 'path': str(OWNER.relative_to(ROOT)), 'status': 'READ_CURRENT_OWNER_VECTOR_PROJECTION', 'logical_range': prefix + '01-' + prefix + str(count), 'actual_rows': count, 'semantic_summary': {'BE': 'Condition guards, selected target vs submit/cancel, persistent species and form cache, item/clone postactions, current-world scan and event/trade consumers.', 'CX': 'Current time/weather/map/nonEgg inputs; current C K/D actual damage and capture shifts; O notification/scan; event cancel/retry; trade double cleanup unknownhost; partner merged-list initial-item restore mismatch scoped.', 'RM': 'Roam and Radar ordinary/variant/skip/direct-input distinctions; NaturalCure terminal mutation vs Regenerator end skip; successful Bike cancellation; debug branch-local fields; candidate nil failures; generation twice and save conversion prefix.'}[prefix], 'verification': 'Exact116 root block/path/line/row hash + original C catalog row hash + parent nonpending + valid source ranges checked; imported source identity is not full C source reading.', 'evidence': 'SOURCE_STATIC_OWNER_RECEIPT + DERIVED_VECTOR_NOT_EXECUTED', 'source_read_credit': 0, 'execution_credit': 0}, ensure_ascii=False) + '\n')
with (OUT / 'command-log.jsonl').open('a') as f:
    f.write(json.dumps({'at': now, 'command': 'python3 ' + str(Path(__file__).relative_to(ROOT)), 'operation': 'RECEIPT_IDENTITY_AND_EXACT_VECTOR_BINDING', 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'vector_count': len(received), 'issues': 0, 'reference_execution': 0}, ensure_ascii=False) + '\n')
print(json.dumps({'received': len(received), 'source_identity_paths': len(identities), 'issues': 0, 'source_read_credit': 0, 'execution_credit': 0}))
