"""Run reviewer-owned, explicit read/check commands and preserve public I/O."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

destination = Path(sys.argv[1])
command = sys.argv[2:]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(command, capture_output=True, text=True)
record = {'argv': command, 'cwd': os.getcwd(), 'start_utc': start,
          'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'recorder_pid': os.getpid(), 'exit_code': result.returncode,
          'stdout': result.stdout, 'stderr': result.stderr,
          'qualification': 'Public tool I/O only; not private model stream or behavior execution proof.'}
destination.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(result.stdout, end='')
print(result.stderr, end='', file=sys.stderr)
sys.exit(result.returncode)
