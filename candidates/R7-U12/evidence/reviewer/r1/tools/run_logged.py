"""Record actual public subprocess I/O. Does not read private model streams."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
label, *argv = sys.argv[1:]
logs = root / 'logs'
logs.mkdir(exist_ok=True)
target = logs / label
if target.with_suffix('.json').exists():
    raise SystemExit('Refusing to overwrite existing command evidence')
record = {'argv': argv, 'cwd': os.getcwd(), 'start_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'runner_pid': os.getpid(), 'qualification': 'Public audit subprocess only; no model configuration inference'}
with target.with_suffix('.stdout').open('xb') as out, target.with_suffix('.stderr').open('xb') as err:
    process = subprocess.Popen(argv, stdout=out, stderr=err)
    record['subprocess_pid'] = process.pid
    record['exit_code'] = process.wait()
record['end_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
target.with_suffix('.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False))
print(target.with_suffix('.stdout').read_text())
print(target.with_suffix('.stderr').read_text(), file=sys.stderr)
raise SystemExit(record['exit_code'])
