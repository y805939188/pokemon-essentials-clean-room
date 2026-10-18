"""Read-only evidence reader; only writes this task's isolated I/O directory."""
import datetime
import hashlib
import json
from pathlib import Path
import sys
import traceback

BASE = Path(__file__).resolve().parent
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
request = json.loads(sys.argv[1])
chunks = []
records = []
exit_code = 0
stderr = ""
try:
    for entry in request["reads"]:
        path = Path(entry["path"])
        data = path.read_bytes()
        lines = data.decode("utf-8-sig").splitlines(keepends=True)
        start, end = entry.get("range", [1, len(lines)])
        content = "".join(lines[start - 1:end])
        chunks.append("PATH " + str(path) + " RANGE " + str(start) + "-" + str(end) + "\n" + content)
        records.append({"path": str(path), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "range": [start, end], "file_lines": len(lines)})
except Exception:
    exit_code = 1
    stderr = traceback.format_exc()
stdout = "\n".join(chunks)
ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
folder = BASE / "io"
folder.mkdir(exist_ok=True)
name = request["id"]
(folder / (name + ".stdout.txt")).write_text(stdout, encoding="utf-8")
(folder / (name + ".stderr.txt")).write_text(stderr, encoding="utf-8")
record = {"id": name, "argv": sys.argv, "started_utc": started, "ended_utc": ended, "reads": records, "underlying_exit_code": exit_code, "stdout_path": str(folder / (name + ".stdout.txt")), "stderr_path": str(folder / (name + ".stderr.txt")), "reading_credit": "IO_ONLY_REQUIRES_ACTUAL_MODEL_READ"}
(folder / (name + ".json")).write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
sys.stdout.write(stdout)
sys.stderr.write(stderr)
sys.exit(exit_code)
