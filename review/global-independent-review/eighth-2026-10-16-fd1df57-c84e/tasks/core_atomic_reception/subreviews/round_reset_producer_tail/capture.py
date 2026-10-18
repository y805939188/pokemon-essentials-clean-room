import datetime
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
label = sys.argv[1]
command = sys.argv[2:]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(command, capture_output=True, text=True, check=False)
ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {"label": label, "argv": command, "cwd": str(pathlib.Path.cwd()),
          "started_utc": started, "ended_utc": ended,
          "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr,
          "qualification": "STATIC_READ_OR_TOOL_VALIDATION; NOT_GAME_EXECUTION"}
(ROOT / (label + ".io.json")).write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
raise SystemExit(result.returncode)
