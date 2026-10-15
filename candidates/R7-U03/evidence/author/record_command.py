"""Capture separate public command streams and process identity; no model claims."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

directory = Path(__file__).resolve().parent / 'commands'
directory.mkdir(exist_ok=True)
label = sys.argv[1]
argv = sys.argv[2:]
assert label.replace('-', '').replace('_', '').isalnum()
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
row = dict(label=label, argv=argv, cwd=os.getcwd(), wrapper_pid=os.getpid(),
           process_pid=process.pid, start_utc=start,
           end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
           exit_code=process.returncode, stdout_file=label+'.stdout', stderr_file=label+'.stderr',
           qualification='Command I/O and exit only; not semantic acceptance or model configuration.')
for suffix, data in [('stdout', stdout), ('stderr', stderr)]:
    (directory/(label+'.'+suffix)).write_bytes(data)
(directory/(label+'.json')).write_text(json.dumps(row, ensure_ascii=False, indent=2)+'\n')
sys.stdout.buffer.write(stdout)
sys.stderr.buffer.write(stderr)
print(json.dumps(row, ensure_ascii=False))
sys.exit(process.returncode)
