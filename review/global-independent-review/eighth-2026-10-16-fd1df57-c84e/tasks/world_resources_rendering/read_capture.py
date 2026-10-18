import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).parent
outdir = root / 'read-io'
outdir.mkdir(exist_ok=True)
label, cwd, command = sys.argv[1:4]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(['bash', '-c', command], cwd=cwd, capture_output=True)
end = datetime.datetime.now(datetime.timezone.utc).isoformat()
(outdir / (label + '.stdout')).write_bytes(result.stdout)
(outdir / (label + '.stderr')).write_bytes(result.stderr)
record = {'label': label, 'cwd': cwd, 'command': command, 'start_utc': start,
          'end_utc': end, 'underlying_exit': result.returncode,
          'stdout': label + '.stdout', 'stderr': label + '.stderr',
          'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
          'kind': 'SOURCE_STATIC_READ_ONLY', 'semantic_credit': 'NONE_FROM_CAPTURE_ALONE'}
with (outdir / 'index.jsonl').open('a') as stream:
    stream.write(json.dumps(record, ensure_ascii=False) + '\n')
print(result.stdout.decode(), end='')
if result.stderr:
    print(result.stderr.decode(), file=sys.stderr, end='')
print(json.dumps(record, ensure_ascii=False), file=sys.stderr)
sys.exit(result.returncode)
