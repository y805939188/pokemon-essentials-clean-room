"""Restore a named text-collection consumer and WP77 dependency, read-only."""
import datetime
import hashlib
import json
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path('/workspace/r7-ir-R7-U11')
OUT = Path(__file__).resolve().parent.parent
fixed_r = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
mi = '45c80832a41c1b56dcd7e9d93497758cbb7721de'
path = 'Data/Scripts/001_Technical/003_Intl_Messages.rb'
inventory = json.loads((ROOT / 'binding-supplement/9f68b18a4a3f12cff0b452977d24171aca0165b74f3a50a615c95f9927f9765c.raw').read_bytes())
row = next(x for x in inventory if x['path'] == path)
url = f'https://raw.githubusercontent.com/Maruno17/pokemon-essentials/{fixed_r}/' + path
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
with urllib.request.urlopen(urllib.request.Request(url), timeout=45) as response:
    content = response.read(1000001)
    status = response.status
assert status == 200 and len(content) == row['bytes']
assert hashlib.sha256(content).hexdigest() == row['sha256']
blob = hashlib.sha1(f'blob {len(content)}\0'.encode() + content).hexdigest()
assert blob == row['git_blob']
dest = ROOT / 'consumer-supplement'
dest.mkdir(exist_ok=True)
(dest / '003_Intl_Messages.rb').write_bytes(content)
p = 'deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md'
wp77 = subprocess.check_output(['git', 'show', mi + ':' + p])
(dest / 'wp77-demo-evidence-and-capability-coverage.md').write_bytes(wp77)
(OUT / 'consumer-supplement-receipt.json').write_text(json.dumps({
    'start_utc': start, 'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reference': {'commit': fixed_r, 'path': path, 'url': url, 'http_status': status,
                  'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest(), 'git_blob': blob},
    'project': {'commit': mi, 'path': p, 'bytes': len(wp77), 'sha256': hashlib.sha256(wp77).hexdigest(),
                'git_blob': hashlib.sha1(f'blob {len(wp77)}\0'.encode() + wp77).hexdigest()},
    'qualification': 'Fixed bytes only; semantic read ranges separately reported; no code execution'
}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'reference_bytes': len(content), 'wp77_bytes': len(wp77)}))
