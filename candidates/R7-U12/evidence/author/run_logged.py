"""Capture public audit commands; never collect environment secrets/model streams."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

def main():
    name, *argv = sys.argv[1:]
    directory = Path(__file__).parent / 'logs'
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    proc = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    (directory / (name + '.stdout')).write_bytes(stdout)
    (directory / (name + '.stderr')).write_bytes(stderr)
    row = {'argv': argv, 'cwd': os.getcwd(), 'start_utc': start,
           'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'audit_subprocess_pid': proc.pid, 'logger_pid': os.getpid(),
           'exit_code': proc.returncode,
           'stdout': name + '.stdout', 'stderr': name + '.stderr',
           'qualification': 'Public audit subprocess I/O only; no model PID/configuration certificate.'}
    (directory / (name + '.json')).write_text(json.dumps(row, ensure_ascii=False, indent=2) + '\n')
    sys.stdout.buffer.write(stdout)
    sys.stderr.buffer.write(stderr)
    raise SystemExit(proc.returncode)

if __name__ == '__main__':
    main()
