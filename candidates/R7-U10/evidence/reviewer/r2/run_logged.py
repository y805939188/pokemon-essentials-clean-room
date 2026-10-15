"""Public tool I/O only; never records model internals or credentials."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
label, *argv = sys.argv[1:]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
proc = subprocess.run(argv, capture_output=True)
end = datetime.datetime.now(datetime.timezone.utc).isoformat()
logs = root / 'logs'
logs.mkdir(exist_ok=True)
for suffix, data in [('stdout', proc.stdout), ('stderr', proc.stderr)]:
    with (logs / f'{label}.{suffix}').open('xb') as stream:
        stream.write(data)
record = {'argv': argv, 'cwd': os.getcwd(), 'runner_pid': os.getpid(),
          'start_utc': start, 'end_utc': end, 'exit_code': proc.returncode,
          'qualification': 'Actual tool I/O; not behavior execution or model configuration authentication.'}
with (logs / f'{label}.json').open('x') as stream:
    json.dump(record, stream, ensure_ascii=False, indent=2)
    stream.write('\n')
sys.stdout.buffer.write(proc.stdout)
sys.stderr.buffer.write(proc.stderr)
sys.exit(proc.returncode)
