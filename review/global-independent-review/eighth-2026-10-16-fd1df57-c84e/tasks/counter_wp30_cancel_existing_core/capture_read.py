"""Read an exact UTF-8 text interval and retain actual helper I/O; no target runs."""
import datetime
import hashlib
import json
import pathlib
import sys
import uuid

OUT = pathlib.Path(__file__).resolve().parent / "io"
OUT.mkdir(exist_ok=True)
start_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
path = pathlib.Path(sys.argv[1]).resolve()
start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
end = int(sys.argv[3]) if len(sys.argv) > 3 else None
kind = sys.argv[4] if len(sys.argv) > 4 else "lines"
stem = "read-" + uuid.uuid4().hex
stdout = ""
stderr = ""
exit_code = 0
try:
    raw = path.read_bytes()
    if kind == "records":
        data = json.loads(raw)
        ids = set(sys.argv[5:])
        records = data["records"]
        chosen = [x for x in records if x.get("id") in ids]
        if {x["id"] for x in chosen} != ids:
            raise ValueError("requested IDs missing")
        stdout = json.dumps(chosen, ensure_ascii=False, indent=2) + "\n"
    else:
        lines = raw.decode().splitlines(keepends=True)
        end = len(lines) if end is None else end
        stdout = "".join(f"{i + 1:05d}: {x}" for i, x in enumerate(lines) if start <= i + 1 <= end)
    identity = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
except Exception as error:
    stderr = f"{type(error).__name__}: {error}\n"
    identity = None
    exit_code = 1
(OUT / (stem + ".stdout")).write_text(stdout)
(OUT / (stem + ".stderr")).write_text(stderr)
(OUT / (stem + ".json")).write_text(json.dumps({
    "argv": sys.argv, "path": str(path), "interval": [start, end],
    "kind": kind, "identity": identity, "start_utc": start_utc,
    "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "helper_exit": exit_code, "business_execution": "NOT_EXECUTED",
    "stdout": stem + ".stdout", "stderr": stem + ".stderr"
}, ensure_ascii=False, indent=2) + "\n")
sys.stdout.write(stdout)
sys.stderr.write(stderr)
raise SystemExit(exit_code)
