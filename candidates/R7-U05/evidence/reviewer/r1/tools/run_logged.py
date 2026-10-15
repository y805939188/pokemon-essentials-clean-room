"""Record actual public command I/O; no reconstructed timestamps or private streams."""
import datetime
import json
from pathlib import Path
import subprocess
import sys

label, *argv = sys.argv[1:]
assert label and all(c.isalnum() or c in '-_' for c in label)
output = Path(__file__).resolve().parent / 'logs' / (label + '.json')
output.parent.mkdir(exist_ok=True)
assert not output.exists(), output
def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
start = utc()
process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
record = dict(argv=argv, cwd=str(Path.cwd()), start_utc=start, end_utc=utc(),
              command_pid=process.pid, exit_code=process.returncode,
              stdout=stdout.decode('utf-8'), stderr=stderr.decode('utf-8'))
with output.open('x') as stream:
    json.dump(record, stream, ensure_ascii=False, indent=2)
    stream.write('\n')
sys.stdout.write(record['stdout'])
sys.stderr.write(record['stderr'])
sys.exit(process.returncode)
