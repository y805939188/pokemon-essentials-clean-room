"""Capture public audit-tool I/O. This never launches a model or reference program."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
label, *argv = sys.argv[1:]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(argv, capture_output=True, text=True)
record = {
    "label": label, "argv": argv, "cwd": os.getcwd(),
    "start_utc": start,
    "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "logger_pid": os.getpid(), "logger_parent_pid": os.getppid(),
    "pid_qualification": "Public audit tool process; model process PID not exposed",
    "stdout": result.stdout, "stderr": result.stderr, "exit_code": result.returncode,
    "evidence_level": "TOOL_VALIDATION", "reference_execution": 0,
}
with (root / "commands.jsonl").open("a") as stream:
    stream.write(json.dumps(record, ensure_ascii=False) + "\n")
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
raise SystemExit(result.returncode)
