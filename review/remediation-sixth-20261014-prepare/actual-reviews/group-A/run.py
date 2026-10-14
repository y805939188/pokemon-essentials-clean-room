"""Capture new reviewer commands; never execute reference Ruby or game binaries."""
import datetime
import json
import pathlib
import subprocess
import sys
import uuid

ROOT = pathlib.Path(__file__).resolve().parent
CWD = pathlib.Path('/workspace/pokemon-essentials-clean-room')
logs = ROOT / 'logs'
logs.mkdir(exist_ok=True)
ledger = ROOT / 'commands.jsonl'
number = 'v2-' + uuid.uuid4().hex[:12]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(sys.argv[1:], cwd=CWD, capture_output=True)
end = datetime.datetime.now(datetime.timezone.utc).isoformat()
out = logs / f'{number}.stdout'
err = logs / f'{number}.stderr'
out.write_bytes(result.stdout)
err.write_bytes(result.stderr)
with ledger.open('a') as handle:
    handle.write(json.dumps({'number': number, 'cwd': str(CWD), 'argv': sys.argv[1:],
                            'start_utc': start, 'end_utc': end, 'exit': result.returncode,
                            'stdout': str(out.relative_to(ROOT)),
                            'stderr': str(err.relative_to(ROOT))}, ensure_ascii=False) + '\n')
sys.stdout.buffer.write(result.stdout)
sys.stderr.buffer.write(result.stderr)
sys.exit(result.returncode)
