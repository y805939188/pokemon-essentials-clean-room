"""Capture public argv, UTC, PID, exit, stdout and stderr without a shell."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

root=Path(__file__).resolve().parent
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
argv=sys.argv[1:]
started=now()
run=subprocess.run(argv,capture_output=True)
record=dict(argv=argv,cwd=os.getcwd(),pid=os.getpid(),actual_thread_id=os.environ.get('CODEX_THREAD_ID'),start_utc=started,end_utc=now(),exit_code=run.returncode,stdout=run.stdout.decode(),stderr=run.stderr.decode(),credit='PUBLIC_TOOL_IO_ONLY_NOT_BEHAVIOR_EXECUTION')
with (root/'public-command-log.jsonl').open('a') as stream:stream.write(json.dumps(record,ensure_ascii=False)+'\n')
print(json.dumps(record,ensure_ascii=False))
sys.exit(run.returncode)
