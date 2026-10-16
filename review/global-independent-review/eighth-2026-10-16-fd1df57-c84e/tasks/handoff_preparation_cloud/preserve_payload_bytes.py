"""Preserve exact frozen input bytes. Tool work only, no reading credit."""
from pathlib import Path
import base64
import gzip
import hashlib
import json
import subprocess

TASK = Path('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/handoff_preparation_cloud')
manifest = json.loads((TASK / 'handoff/cloud-eighth-update-handoff-manifest.json').read_text())
payloads = []
for item in manifest['input_payloads'] + manifest['additional_payloads']:
    data = subprocess.check_output(['git', 'show', item['commit'] + ':' + item['path']])
    blob = hashlib.sha1(('blob ' + str(len(data)) + '\0').encode() + data).hexdigest()
    mode = subprocess.check_output(['git', 'ls-tree', item['commit'], '--', item['path']]).decode().split()[0]
    assert len(data) == item['bytes'] and hashlib.sha256(data).hexdigest() == item['sha256']
    assert blob == item['blob'] and mode == item['mode']
    payloads.append({**{k: item[k] for k in ['commit', 'tree', 'path', 'mode', 'blob', 'bytes', 'sha256']},
                     'phase': item.get('phase', 'additional'),
                     'base64': base64.b64encode(data).decode('ascii')})
assert len(payloads) == 72
packed = json.dumps({'schema': 'r8-exact-input-bytes/v1', 'payloads': payloads},
                    ensure_ascii=False, separators=(',', ':')).encode()
(TASK / 'audit/exact-payload-bytes.json.gz').write_bytes(gzip.compress(packed, mtime=0))
print(json.dumps({'raw_payloads': len(payloads), 'raw_bytes': sum(p['bytes'] for p in payloads),
                  'container_bytes': len(packed), 'compressed_bytes': (TASK / 'audit/exact-payload-bytes.json.gz').stat().st_size,
                  'credit': 'TOOL_VALIDATION_ONLY'}))
