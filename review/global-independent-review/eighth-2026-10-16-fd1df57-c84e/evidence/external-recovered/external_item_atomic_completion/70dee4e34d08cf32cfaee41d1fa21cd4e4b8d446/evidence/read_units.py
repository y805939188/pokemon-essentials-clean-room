"""Read-only source recovery; writes only operation metadata in this task directory.

No reference code, model, game, save, plugin or callback is executed.
Ranges are inclusive and command output is the actual text offered for reading.
"""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = pathlib.Path(__file__).resolve().parent
repo, path, bounds = sys.argv[1:]
base = pathlib.Path('/workspace/pokemon-essentials') if repo == 'R' else ROOT
raw = (base / path).read_bytes()
lines = raw.decode('utf-8-sig').splitlines()
ranges = [[int(a),len(lines) if b=='eof' else int(b)] for a,b in (s.split(':') for s in bounds.split(','))]
view = '\n'.join(f'{i}: {lines[i-1]}' for a, b in ranges for i in range(a, b+1)) + '\n'
rec = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'repo': str(base), 'path': path, 'ranges': ranges,
       'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
       'git_blob': subprocess.check_output(['git', '-C', str(base), 'hash-object', '--stdin'], input=raw).decode().strip(),
       'stdout_bytes': len(view.encode()), 'stdout_sha256': hashlib.sha256(view.encode()).hexdigest(),
       'execution_class': 'TEXT_RECOVERY_ONLY', 'business': 'NOT_EXECUTED',
       'read_credit': 'Only actual nontruncated tool output reviewed by the reader; no automatic credit.'}
with (OUT / 'read-operations.ndjson').open('a') as f:
    f.write(json.dumps(rec, ensure_ascii=False)+'\n')
print(view, end='')
