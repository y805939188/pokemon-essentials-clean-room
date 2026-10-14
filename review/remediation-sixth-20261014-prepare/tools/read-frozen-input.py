#!/usr/bin/env python3
"""Read and validate fixed input bytes into scratch; never execute the payload."""
import argparse
import hashlib
import json
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('batch', choices=['R6-U%02d' % i for i in range(1, 15)])
p.add_argument('kind', choices=['source', 'formal'])
p.add_argument('path')
p.add_argument('--cache-root', default='/workspace/r6-input-cache/frozen-payloads')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
repo = root.parents[1]
contract = json.loads((root / 'contracts' / (a.batch + '.json')).read_text())
inputs = json.loads((root / 'inputs/frozen-inputs.json').read_text())
allowed = contract['read_only_reference_paths' if a.kind == 'source' else 'candidate_formal_paths']
if a.path not in allowed:
    raise SystemExit('Additional consumers are read-only permitted, but first register their exact fixed identity and new reading scope with root; this helper validates the frozen primary readset.')
key = 'source_materials' if a.kind == 'source' else 'formal_materials'
row = next(x for x in inputs[key] if x['path'] == a.path)
commit = inputs['reference_commit'] if a.kind == 'source' else '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
repository = 'Maruno17/pokemon-essentials' if a.kind == 'source' else 'y805939188/pokemon-essentials-clean-room'
cache = Path(a.cache_root).resolve()
if not (cache == Path('/workspace/r6-input-cache/frozen-payloads') or str(cache).startswith('/tmp/')):
    raise SystemExit('Use the registered scratch cache or /tmp; never overwrite candidate/formal/history.')
out = cache / repository / commit / a.path
if out.exists():
    data = out.read_bytes()
    origin = 'existing full-byte verified cache'
elif a.kind == 'formal':
    data = subprocess.check_output(['git', 'cat-file', 'blob', commit + ':' + a.path], cwd=repo)
    origin = 'fixed local Git object'
else:
    url = 'https://raw.githubusercontent.com/' + repository + '/' + commit + '/' + urllib.parse.quote(a.path, safe='/')
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read()
    origin = 'fixed raw remote payload'
actual = {'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(),
          'git_blob':hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}
assert all(actual[k] == row[k] for k in actual), (a.path, actual)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(data)
print(json.dumps({'path':str(out), 'commit':commit, **actual, 'origin':origin,
                  'evidence_level':'TOOL_VALIDATION', 'semantic_full_read':False, 'execution':False}, ensure_ascii=False))
