"""Reversible current JSON representation, never a semantic reading operation."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
BASE = OWN.parent.parent
label = sys.argv[1]
assert re.fullmatch('[a-z0-9-]+', label)
indices = [int(v) for v in sys.argv[2:]]
ledger = json.loads((OWN / 'reading-ledger.json').read_text())
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
def exact_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
def encode(value):
    if isinstance(value, dict):
        assert '$exact_table' not in value and '$exact_blocks' not in value
        return {key: encode(child) for key, child in value.items()}
    if isinstance(value, list):
        if len(value) >= 2 and all(isinstance(row, dict) and set(row) == set(value[0]) for row in value):
            common = {key: value[0][key] for key in value[0] if all(exact_json(row[key]) == exact_json(value[0][key]) for row in value)}
            columns = [key for key in value[0] if key not in common]
            return {'$exact_table': {'common_fields_for_every_row': encode(common), 'varying_columns_in_order': columns, 'rows_in_original_order': [[encode(row[key]) for key in columns] for row in value]}}
        if len(value) >= 2 and all(isinstance(row, dict) for row in value):
            groups = []
            for row in value:
                if not groups or set(groups[-1][0]) != set(row):
                    groups.append([])
                groups[-1].append(row)
            return {'$exact_blocks': [encode(group) for group in groups]}
        return [encode(child) for child in value]
    return value
def decode(value):
    if isinstance(value, dict):
        if set(value) == {'$exact_blocks'}:
            return [row for block in value['$exact_blocks'] for row in decode(block)]
        if set(value) == {'$exact_table'}:
            table = value['$exact_table']
            common = decode(table['common_fields_for_every_row'])
            return [dict(common, **dict(zip(table['varying_columns_in_order'], [decode(child) for child in row]))) for row in table['rows_in_original_order']]
        return {key: decode(child) for key, child in value.items()}
    if isinstance(value, list):
        return [decode(child) for child in value]
    return value
def display(value, depth=0):
    pad = ' ' * depth
    if isinstance(value, dict):
        return '{\n' + ',\n'.join(' '*(depth+1)+json.dumps(key,ensure_ascii=False)+': '+display(child,depth+1) for key,child in value.items())+'\n'+pad+'}'
    if isinstance(value, list):
        if all(not isinstance(child,(list,dict)) for child in value):
            return json.dumps(value, ensure_ascii=False)
        return '[\n'+',\n'.join(' '*(depth+1)+display(child,depth+1) for child in value)+'\n'+pad+']'
    return json.dumps(value, ensure_ascii=False)
payloads = []
sources = []
for index in indices:
    row = ledger['snapshot_payloads'][index]
    raw = (BASE / row['snapshot']).read_bytes()
    assert len(raw) == row['bytes'] and hashlib.sha256(raw).hexdigest() == row['sha256']
    original = json.loads(raw)
    encoded = encode(original)
    assert exact_json(decode(encoded)) == exact_json(original)
    sources.append({'index': index, 'path': row['original_path'], 'bytes': len(raw), 'sha256': row['sha256']})
    payloads.append({'index': index, 'value': encoded})
view = {'schema': 'gr8-complete-json-columnar-reading-view/v1', 'qualification': 'Every current JSON value preserved, including all row values. Common fields apply to every row; varying row arrays follow declared columns. Exact decode equals each original. Actual complete view reading remains required; generation grants no source/semantic approval.', 'sources': sources, 'payloads': payloads}
target = OWN / (label + '-columnar-view.json')
assert not target.exists()
raw = (display(view)+'\n').encode()
assert json.loads(raw) == view
target.write_bytes(raw)
receipt = {'began_utc': start, 'ended_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'sources': sources, 'output': target.name, 'bytes': len(raw), 'lines': len(raw.splitlines()), 'sha256': hashlib.sha256(raw).hexdigest(), 'all_decode_equals_original': True, 'semantic_reading': False, 'exit_code': 0}
(OWN / (label+'-columnar-generation.json')).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt))
