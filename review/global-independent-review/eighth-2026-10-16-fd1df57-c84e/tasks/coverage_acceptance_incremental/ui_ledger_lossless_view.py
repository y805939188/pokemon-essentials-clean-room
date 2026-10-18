"""Render all UI-ledger fields with exact repeated fact-ID lists interned.

This is a lossless reading format, not a semantic reviewer or source executor.
Every unit is retained. A list definition is read once with every exact unit
association. Reconstructing the input is checked before any output is written.
"""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
source = ROOT / 'ledger-views-v2/231.semantic-fields.json'
raw = source.read_bytes()
data = json.loads(raw)
records = data['records']
lines = []
recovered = []
unit_count = 0
group_count = 0

def emit(label, value):
    lines.append(label + ' ' + json.dumps(value, ensure_ascii=False, separators=(',', ':')))

emit('ROOT_FIELDS', {k: v for k, v in data.items() if k != 'records'})
for i, record in enumerate(records):
    header = {k: v for k, v in record.items() if k != 'structure_units'}
    emit(f'RECORD_{i}_FIELDS', header)
    groups = []
    rows = []
    for unit in record.get('structure_units', []):
        if not isinstance(unit, dict):
            raise ValueError('Unexpected unit type')
        converted = dict(unit)
        if 'fact_ids' in unit:
            value = unit['fact_ids']
            if not isinstance(value, list) or any(not isinstance(v, str) for v in value):
                raise ValueError('Unexpected fact-ID value')
            if value not in groups:
                groups.append(value)
            del converted['fact_ids']
            if 'exact_fact_ids_list_ref' in converted:
                raise ValueError('Reference-key collision')
            converted['exact_fact_ids_list_ref'] = groups.index(value)
        rows.append(converted)
    for j, group in enumerate(groups):
        emit(f'RECORD_{i}_EXACT_FACT_IDS_{j}', group)
    for j, row in enumerate(rows):
        emit(f'RECORD_{i}_UNIT_{j}', row)
    reconstructed = dict(header)
    if 'structure_units' in record:
        reconstructed['structure_units'] = []
        for row in rows:
            restored = dict(row)
            if 'exact_fact_ids_list_ref' in restored:
                ref = restored.pop('exact_fact_ids_list_ref')
                restored['fact_ids'] = groups[ref]
            reconstructed['structure_units'].append(restored)
    if reconstructed != record:
        raise ValueError('Lossless reconstruction failed')
    recovered.append(reconstructed)
    unit_count += len(rows)
    group_count += len(groups)
restored_data = {k: v for k, v in data.items() if k != 'records'}
restored_data['records'] = recovered
if restored_data != data:
    raise ValueError('Whole input reconstruction failed')
out = ('\n'.join(lines) + '\n').encode()
(ROOT / 'ui-ledger-lossless-fields.txt').write_bytes(out)
receipt = {
    'source': str(source.relative_to(ROOT)),
    'source_view_sha256': hashlib.sha256(raw).hexdigest(),
    'source_view_bytes': len(raw),
    'rendering_bytes': len(out),
    'rendering_sha256': hashlib.sha256(out).hexdigest(),
    'rendering_lines': len(lines),
    'records': len(records), 'unit_objects': unit_count,
    'exact_fact_id_list_definitions': group_count,
    'all_fields_losslessly_reconstructed': True,
    'source_read_or_semantic_acceptance': False,
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'qualification': 'Only exact repeated list representation changed; no field or unit discarded.'
}
(ROOT / 'ui-ledger-lossless-view-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt))
