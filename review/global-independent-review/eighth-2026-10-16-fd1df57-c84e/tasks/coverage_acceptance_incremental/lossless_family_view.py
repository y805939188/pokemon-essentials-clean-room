import collections
import datetime
import hashlib
import json
import pathlib
import re
import sys

OWN = pathlib.Path(__file__).resolve().parent
BASE = OWN.parent.parent
label = sys.argv[1]
assert re.fullmatch(r'[a-z0-9-]+', label)
indices = [int(x) for x in sys.argv[2:]]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
ledger = json.loads((OWN / 'reading-ledger.json').read_text())
source = []
values = []
for index in indices:
    row = ledger['snapshot_payloads'][index]
    raw = (BASE / row['snapshot']).read_bytes()
    assert len(raw) == row['bytes'] and hashlib.sha256(raw).hexdigest() == row['sha256']
    values.append(json.loads(raw))
    source.append({'index': index, 'original_path': row['original_path'], 'bytes': len(raw), 'sha256': row['sha256']})
counts = collections.Counter()
examples = {}
def signature(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
def visit(value):
    key = signature(value)
    if isinstance(value, (str, dict, list)) and len(key) >= 60:
        counts[key] += 1
        examples[key] = value
    if isinstance(value, dict):
        assert '$exact_shared_ref' not in value
        for child in value.values():
            visit(child)
    elif isinstance(value, list):
        for child in value:
            visit(child)
for value in values:
    visit(value)
shared = {key: 'D' + str(i) for i, key in enumerate(key for key, n in counts.items() if n > 1)}
def encode(value, own=None):
    key = signature(value)
    if key in shared and shared[key] != own:
        return {'$exact_shared_ref': shared[key]}
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, list):
        return [encode(v) for v in value]
    return value
definitions = {shared[key]: encode(examples[key], shared[key]) for key in shared}
def decode(value):
    if isinstance(value, dict):
        if set(value) == {'$exact_shared_ref'}:
            return decode(definitions[value['$exact_shared_ref']])
        return {k: decode(v) for k, v in value.items()}
    if isinstance(value, list):
        return [decode(v) for v in value]
    return value
encoded = [encode(value) for value in values]
assert [decode(value) for value in encoded] == values
view = {'schema': 'gr8-exact-json-shared-value-reading-view/v1',
        'qualification': 'All current JSON field values preserved and exactly reconstructed. Reading a reference requires also actually reading its shared definition. This representation is not source reading or semantic approval.',
        'sources': source, 'shared_definitions': definitions,
        'payloads': [{'index': index, 'value': value} for index, value in zip(indices, encoded)]}
target = OWN / (label + '-lossless-view.json')
assert not target.exists(), target
raw = (json.dumps(view, ensure_ascii=False, indent=1) + '\n').encode()
target.write_bytes(raw)
receipt = {'began_utc': started, 'ended_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'sources': source, 'shared_definitions': len(definitions), 'output': target.name,
           'output_bytes': len(raw), 'output_sha256': hashlib.sha256(raw).hexdigest(),
           'output_lines': len(raw.splitlines()), 'exact_reconstruction_assertion': True,
           'actual_semantic_reading': False, 'source_credit': False, 'exit_code': 0}
(OWN / (label + '-lossless-generation.json')).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(receipt))
