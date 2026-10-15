"""Capture public command I/O; does not authenticate model configuration."""
import datetime, json, os, pathlib, subprocess, sys

output, cwd, *command = sys.argv[1:]
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
start = now()
result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
record = dict(command=command, cwd=cwd, start_utc=start, end_utc=now(),
              recorder_pid=os.getpid(), child_pid_qualification='subprocess.run does not expose completed child PID',
              actual_context=os.environ.get('CODEX_THREAD_ID', 'NOT_EXPOSED'),
              exit_code=result.returncode, stdout=result.stdout, stderr=result.stderr)
pathlib.Path(output).write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(record, ensure_ascii=False))
sys.exit(result.returncode)
