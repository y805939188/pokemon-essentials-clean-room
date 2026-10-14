"""Capture each subsequent validation attempt without overwriting earlier attempts."""
import datetime
import json
from pathlib import Path
import subprocess
import sys

directory = Path(__file__).parent
existing = list(directory.glob("attempt-*.json"))
number = len(existing) + 1
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(sys.argv[1:], capture_output=True, text=True)
prefix = directory / f"attempt-{number:02d}"
prefix.with_suffix(".stdout.txt").write_text(result.stdout)
prefix.with_suffix(".stderr.txt").write_text(result.stderr)
prefix.with_suffix(".json").write_text(json.dumps({
    "argv": sys.argv[1:], "cwd": str(Path.cwd()), "start_utc": start,
    "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "exit_code": result.returncode, "stdout": prefix.name + ".stdout.txt",
    "stderr": prefix.name + ".stderr.txt", "kind": "PROCESS_CAPTURE",
}, ensure_ascii=False, indent=2) + "\n")
print(result.stdout, end="")
print(result.stderr, end="", file=sys.stderr)
sys.exit(result.returncode)
