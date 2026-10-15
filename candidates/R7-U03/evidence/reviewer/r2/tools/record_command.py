"""Record actual public tool I/O; never infer model configuration from a PID."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

out = Path(os.environ.get('R7_U03_COMMAND_LOG_DIR', str(Path(__file__).resolve().parents[1] / 'commands')))
out.mkdir(parents=True, exist_ok=True)
name, *argv = sys.argv[1:]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
p = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()
for suffix, data in [('stdout', stdout), ('stderr', stderr)]:
    (out / (name + '.' + suffix)).write_bytes(data)
receipt = dict(argv=argv, cwd=os.getcwd(), start_utc=start,
               end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               wrapper_pid=os.getpid(), process_pid=p.pid, exit_code=p.returncode,
               qualification='Actual tool process only; no model PID or semantic credit')
(out / (name + '.json')).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
sys.stdout.buffer.write(stdout)
sys.stderr.buffer.write(stderr)
sys.exit(p.returncode)
