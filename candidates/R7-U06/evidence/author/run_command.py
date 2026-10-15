"""Record public command argv, UTC, subprocess PID, full stdout/stderr and exit."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

here = Path(__file__).resolve().parent
name, *argv = sys.argv[1:]
assert name.replace('-', '').isalnum()
target = here / 'commands' / (name + '.json')
target.parent.mkdir(exist_ok=True)
assert not target.exists(), target
utc = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {'argv': argv, 'cwd': os.getcwd(), 'start_utc': utc(),
          'runner_pid': os.getpid(), 'stdin': '', 'qualification': 'Public tool I/O; not a model stream or behavior execution certificate.'}
p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
record['command_pid'] = p.pid
stdout, stderr = p.communicate()
record.update(end_utc=utc(), exit_code=p.returncode,
              stdout=stdout.decode('utf-8'), stderr=stderr.decode('utf-8'))
target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
sys.stdout.buffer.write(stdout)
sys.stderr.buffer.write(stderr)
raise SystemExit(p.returncode)
