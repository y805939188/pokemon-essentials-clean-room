"""Separate exact trait field-line locators from all current reading claims.

No reference program is imported or executed. The excluded subtree contains
only source line positions and class identifiers, not the class definitions or
PBS field values. This does not grant source or field-value reading credit.
"""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
source = ROOT / 'ledger-views-v2/186.semantic-fields.json'
raw = source.read_bytes()
document = json.loads(raw)
records = document['species_pbs_fields']['records']
allowed_fields = {
    'BaseStats', 'Abilities', 'HiddenAbilities', 'Height', 'Weight',
    'Evolution', 'Evolutions', 'Flags', 'Incense'
}
counts = {}
positions = 0
for path, rows in records.items():
    if not isinstance(path, str) or not isinstance(rows, list):
        raise ValueError('Unexpected locator container')
    counts[path] = len(rows)
    for row in rows:
        if set(row) != {'class', 'record_start', 'record_end', 'field_lines'}:
            raise ValueError('Unexpected record fields: retain for actual reading')
        for key in ['class', 'record_start', 'record_end']:
            if type(row[key]) is not int or row[key] < 1:
                raise ValueError('Unexpected position or class identifier')
        if row['record_start'] > row['record_end']:
            raise ValueError('Reversed record range')
        fields = row['field_lines']
        if not isinstance(fields, dict) or set(fields) - allowed_fields:
            raise ValueError('Unexpected field selector')
        for lines in fields.values():
            if not isinstance(lines, list) or any(type(n) is not int for n in lines):
                raise ValueError('Field value found in locator list')
            if any(n < row['record_start'] or n > row['record_end'] for n in lines):
                raise ValueError('Field position outside recorded section')
            positions += len(lines)
canonical = json.dumps(records, ensure_ascii=False, separators=(',', ':')).encode()
disposition = {
    'pointer': '/species_pbs_fields/records',
    'purpose': 'EXACT_SOURCE_LINE_AND_CLASS_ID_LOCATORS_ONLY_NO_PBS_VALUES',
    'source_view': str(source.relative_to(ROOT)),
    'source_view_sha256': hashlib.sha256(raw).hexdigest(),
    'subtree_sha256_canonical_json': hashlib.sha256(canonical).hexdigest(),
    'subtree_canonical_bytes': len(canonical),
    'records_by_path': counts,
    'record_instances': sum(counts.values()),
    'field_position_instances': positions,
    'complete_shape': {
        'class': 'positive integer class identifier; class meaning is elsewhere',
        'record_start': 'positive source line',
        'record_end': 'positive source line',
        'field_lines': 'named field to exact source line positions only'
    },
    'all_nonlocator_fields_retained_in_reading_view': True,
    'source_field_value_or_history_semantic_credit': False,
    'actual_PBS_value_and_class_definition_reception': 'OPEN_SEPARATE_ARTIFACTS',
    'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'qualification': 'Mechanical shape and identity disposition only; no semantic reading inferred.'
}
document['species_pbs_fields']['records'] = {'inventory_only_disposition': disposition}
(ROOT / 'trait-locator-purpose-disposition.json').write_text(
    json.dumps(disposition, ensure_ascii=False, indent=2) + '\n'
)
(ROOT / 'trait-ledger-current-fields.json').write_text(
    json.dumps(document, ensure_ascii=False, indent=2) + '\n'
)
print(json.dumps({'records': sum(counts.values()), 'positions': positions,
                  'reading_view_lines': len(json.dumps(document, indent=2).splitlines()),
                  'source_credit': False}))
