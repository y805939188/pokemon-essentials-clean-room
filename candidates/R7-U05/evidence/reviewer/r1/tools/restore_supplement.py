"""Restore one newly named immutable source dependency; never execute it."""
import datetime
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import quote
from urllib.request import urlopen

source = sys.argv[1] if len(sys.argv) > 1 else 'Data/Scripts/021_Compiler/001_Compiler.rb'
commit = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
index = json.loads(Path('/workspace/r7-context/R7-U05-reviewer/evidence/tasks/R7-C13/identity-index.json').read_bytes())
expected = next(x for x in index['identities'] if x['path'] == source and x['commit'] == commit)
url = 'https://raw.githubusercontent.com/Maruno17/pokemon-essentials/' + commit + '/' + quote(source)
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
with urlopen(url, timeout=40) as response:
    data = response.read(expected['bytes'] + 1)
    status = response.status
actual = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
          'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}
assert all(actual[k] == expected[k] for k in actual)
target = Path('/workspace/r7-context/R7-U05-reviewer/inputs/reference') / source
target.parent.mkdir(parents=True, exist_ok=True)
if target.exists():
    assert target.read_bytes() == data
else:
    target.write_bytes(data)
target.chmod(0o444)
print(json.dumps({'url': url, 'start_utc': start,
                  'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'http_status': status, 'identity': actual, 'identity_id': expected['identity_id'],
                  'destination': str(target), 'semantic_or_execution_credit': False}, indent=2))
