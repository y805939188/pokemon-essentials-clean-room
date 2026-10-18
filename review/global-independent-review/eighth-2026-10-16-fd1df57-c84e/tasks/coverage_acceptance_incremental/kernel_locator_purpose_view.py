"""Strictly dispose locator-only values; retain every reading/qualification field.
No reviewed program is imported or executed, and no source credit is granted.
"""
from pathlib import Path
from collections import Counter
import datetime, hashlib, json
root = Path(__file__).resolve().parent
source = root / 'fact-views/159.semantic-fields.json'
raw = source.read_bytes()
data = json.loads(raw)
assert set(data) == {'schema', 'evidence_grade', 'items'}
assert len(data['items']) == 77
out = {k: v for k, v in data.items() if k != 'items'}
out['items'] = []
locators = []
for i, item in enumerate(data['items']):
    assert set(item) == {'source_identity', 'physical_read_ranges', 'unread_ranges', 'structures', 'status', 'semantic_join'}
    statuses = Counter()
    for j, row in enumerate(item['structures']):
        ordinary = row['kind'] in {'module', 'class', 'def'}
        assert set(row) == ({'kind', 'identity', 'range', 'locator_method', 'review_status'} if ordinary else {'kind', 'identity', 'range', 'review_status'})
        assert ordinary or row['kind'] == 'registered-record'
        assert isinstance(row['identity'], str)
        assert isinstance(row['range'], list) and len(row['range']) == 2 and all(isinstance(v, int) for v in row['range'])
        assert row['review_status'] == ('FULL_FILE_READ / UNIT_JOIN_PENDING' if ordinary else 'FULL_RECORD_READ / DOMAIN_CONSUMER_JOIN_PENDING')
        if ordinary:
            assert row['locator_method'] == 'indentation END locator, not semantic parser'
        statuses[row['review_status']] += 1
        locators.append({'pointer': f'/items/{i}/structures/{j}', 'exact_value': row, 'purpose': 'INVENTORY_ONLY_LOCATION; no body/record-value/premise/consumer semantic evidence'})
    retained = {k: v for k, v in item.items() if k != 'structures'}
    retained['locator_only_subtree'] = {'exact_pointer': f'/items/{i}/structures', 'count': len(item['structures']), 'all_review_statuses_exact': dict(statuses), 'disposition': 'PURE_TYPED_LOCATORS; every status still pending; no source reading credit'}
    out['items'].append(retained)
assert len(locators) == 1504
(root / 'kernel-source-unit-current-fields.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
(root / 'kernel-source-unit-exact-locator-dispositions.json').write_text(json.dumps(locators, ensure_ascii=False, indent=2)+'\n')
receipt = {'input': str(source.relative_to(root)), 'input_bytes': len(raw), 'input_sha256': hashlib.sha256(raw).hexdigest(), 'all77_nonlocator_fields_retained': True, 'strict_locator_only_shape_and_pending_status_rows': 1504, 'source_credit': False, 'business': 'NOT_EXECUTED', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root / 'kernel-source-unit-purpose-view-receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt))
