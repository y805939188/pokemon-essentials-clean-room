"""Record an explicitly supplied tool command, PID, UTC and full stdout/stderr."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

destination = Path(sys.argv[1])
argv = sys.argv[2:]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
p = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = p.communicate()
record = {'argv': argv, 'cwd': os.getcwd(), 'wrapper_pid': os.getpid(),
          'tool_pid': p.pid, 'start_utc': start,
          'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'exit_code': p.returncode, 'stdout': out, 'stderr': err}
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(out, end='')
print(err, end='', file=sys.stderr)
sys.exit(p.returncode)
