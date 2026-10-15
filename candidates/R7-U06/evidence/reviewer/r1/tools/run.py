"""Capture public command I/O, UTC, and subprocess IDs. No model attestation."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
name, cwd, *argv = sys.argv[1:]
target = root / 'commands' / (name + '.json')
if target.exists():
    raise SystemExit('Refuse to overwrite command evidence: ' + str(target))
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {'argv': argv, 'cwd': cwd, 'start_utc': now(), 'runner_pid': os.getpid()}
p = subprocess.Popen(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
record['command_pid'] = p.pid
stdout, stderr = p.communicate()
record.update(end_utc=now(), exit_code=p.returncode,
              stdout=stdout.decode('utf-8', errors='replace'),
              stderr=stderr.decode('utf-8', errors='replace'))
with target.open('x') as f:
    json.dump(record, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps(record, ensure_ascii=False))
sys.exit(p.returncode)
