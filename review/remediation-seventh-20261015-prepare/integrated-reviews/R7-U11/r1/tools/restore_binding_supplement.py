"""Restore four exact missing U11 binding objects, not a package scan."""
import datetime
import gzip
import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path('/workspace/r7-ir-R7-U11')
OUT = Path(__file__).resolve().parent.parent
fixed = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
manifest = json.loads((ROOT / 'original/evidence/tasks/R7-C13/raw-binding-manifest.json').read_bytes())
wanted = {
 '3290b8a77f8f3779c8726b32d7a53573fbdcaeea8149487246f4a9a500db1c51',
 '9f68b18a4a3f12cff0b452977d24171aca0165b74f3a50a615c95f9927f9765c',
 '2d1c2389a51c357450e6efcc7956f57be237ecf43d60e0dce716061a56338399',
 '73e72ebe018347a6b74354ea4ac229070cf32821d66f5e6e053ad4327641e45c'}
dest = ROOT / 'binding-supplement'
dest.mkdir(exist_ok=True)
rows = []
for digest in sorted(wanted):
    expected = next(x for x in manifest if x['sha256'] == digest)
    url = ('https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'
           + fixed + '/review/global-independent-review/seventh-2026-10-14-e646432-7a91/'
           + f'publication-transport/core/objects/{digest[:2]}/{digest}.gz')
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with urllib.request.urlopen(url, timeout=45) as response:
        status = response.status
        compressed = response.read(1000001)
    assert status == 200 and len(compressed) <= 1000000
    content = gzip.decompress(compressed)
    assert len(content) == expected['bytes']
    assert hashlib.sha256(content).hexdigest() == digest
    blob = hashlib.sha1(f'blob {len(content)}\0'.encode() + content).hexdigest()
    assert blob == expected['content_git_blob']
    path = dest / (digest + '.raw')
    if path.exists():
        assert path.read_bytes() == content
    else:
        path.write_bytes(content)
    rows.append({'url': url, 'start_utc': start,
                 'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 'http_status': status, 'bytes': len(content), 'sha256': digest,
                 'git_blob': blob, 'compressed_sha256': hashlib.sha256(compressed).hexdigest(),
                 'local_path': str(path)})
(OUT / 'binding-supplement-receipt.json').write_text(json.dumps({
    'qualification': 'TOOL_VALIDATION; fixed raw JSON only, no behavior execution',
    'fixed_publication_commit': fixed, 'rows': rows}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'restored': len(rows), 'bytes': sum(x['bytes'] for x in rows)}))
