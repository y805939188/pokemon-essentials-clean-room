"""Verify only U11 original raw JSON bindings, without executing input programs."""
import hashlib
import json
from pathlib import Path

ROOT = Path('/workspace/r7-ir-R7-U11')
OUT = Path(__file__).resolve().parent.parent
ORIG = ROOT / 'original'
base = ORIG / 'evidence/tasks/R7-C13/inputs/tasks/R7-P02'
contract = json.loads((ORIG / 'dispatch/delegation/contracts/R7-U11.json').read_bytes())
normalized_path = base / 'normalized-record-candidates.json'
normalized = json.loads(normalized_path.read_bytes())
raw = {p.stem: p.read_bytes() for p in (base / 'evidence/inputs').glob('*.raw')}
received = (ORIG / 'evidence/tasks/R7-C01/M16-received-findings.json').read_bytes()
raw[hashlib.sha256(received).hexdigest()] = received
for p in (ROOT / 'binding-supplement').glob('*.raw'):
    raw[p.stem] = p.read_bytes()
parsed = {key: json.loads(value) for key, value in raw.items()}
sha = lambda b: hashlib.sha256(b).hexdigest()
for key, value in raw.items():
    assert sha(value) == key

def pointer(doc, text):
    for part in text.split('/')[1:]:
        part = part.replace('~1', '/').replace('~0', '~')
        doc = doc[int(part)] if isinstance(doc, list) else doc[part]
    return doc

results = []
def walk(value, where):
    if isinstance(value, dict):
        if all(k in value for k in ('canonical_sha256', 'input_sha256', 'json_pointer')):
            content = raw[value['input_sha256']]
            item = pointer(parsed[value['input_sha256']], value['json_pointer'])
            canonical = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
            assert sha(canonical) == value['canonical_sha256'], where
            start, end = value['raw_member_byte_offsets']
            member = content[start:end]
            assert len(member) == value['raw_member_bytes'], where
            assert sha(member) == value['raw_member_sha256'], where
            assert json.loads(member) == item, where
            results.append({'location': where, 'binding_id': value['binding_id'],
                            'json_pointer': value['json_pointer'], 'input_sha256': value['input_sha256'],
                            'raw_member_byte_offsets': [start, end], 'canonical_sha256': sha(canonical),
                            'raw_member_sha256': sha(member), 'verified': True})
        for key, child in value.items():
            walk(child, where + '/' + key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            walk(child, where + '/' + str(i))

walk(contract, 'contract')
contract_count = len(results)
for i in (20, 22):
    walk(normalized['records'][i], f'normalized/records/{i}')
report = {'qualification': 'TOOL_VALIDATION of inert bound JSON only; no semantic or runtime PASS implied',
          'contract_references': contract_count, 'normalized_U11_references': len(results)-contract_count,
          'raw_files': [{'sha256': key, 'bytes': len(value)} for key, value in raw.items()],
          'references': results}
(OUT / 'original-binding-audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: report[k] for k in ('contract_references', 'normalized_U11_references', 'raw_files')}))
