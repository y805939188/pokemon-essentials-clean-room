"""Record new ordinary audit subprocesses; never infer model identity from PID."""
import datetime
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
name, *command = sys.argv[1:]
logs = root / 'logs'
logs.mkdir(exist_ok=True)
def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
start = utc()
with (logs / (name + '.stdout')).open('xb') as stdout, (logs / (name + '.stderr')).open('xb') as stderr:
    child = subprocess.Popen(command, stdout=stdout, stderr=stderr)
    pid = child.pid
    code = child.wait()
receipt = dict(argv=command, cwd=str(Path.cwd()), start_utc=start, end_utc=utc(),
               audit_subprocess_pid=pid, exit_code=code,
               qualification='Audit process only. Not a model PID or runtime/semantic certificate.')
(logs / (name + '.json')).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(receipt, ensure_ascii=False))
sys.exit(code)
