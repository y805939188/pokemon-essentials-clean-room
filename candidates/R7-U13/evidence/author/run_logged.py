"""Run public author tooling with separate stdout/stderr and real process exits."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[4]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
process = subprocess.run(sys.argv[1:], cwd=root, capture_output=True, text=True)
entry = {
    'start_utc': start,
    'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'logger_pid': os.getpid(), 'parent_pid': os.getppid(),
    'cwd': str(root), 'argv': sys.argv[1:],
    'stdout': process.stdout, 'stderr': process.stderr, 'exit_code': process.returncode,
    'qualification': 'Public tooling I/O only; no model stream or credential capture.'
}
with Path(__file__).with_name('commands.jsonl').open('a') as stream:
    stream.write(json.dumps(entry, ensure_ascii=False) + '\n')
print(json.dumps(entry, ensure_ascii=False, indent=2))
sys.exit(process.returncode)
