"""Deliver an exact JSON-pointer record, with the containing frozen identity."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

path, pointer = sys.argv[1:]
raw = subprocess.check_output(["git", "show", f"469a268b92daed7b4d28d7fd0da75520cbb7228f:{path}"])
value = json.loads(raw)
for part in pointer.strip("/").split("/") if pointer else []:
    part = part.replace("~1", "/").replace("~0", "~")
    value = value[int(part)] if isinstance(value, list) else value[part]
output = json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
record = {"kind": "EXACT_JSON_POINTER_READ_DELIVERY", "path": path, "pointer": pointer,
          "commit": "469a268b92daed7b4d28d7fd0da75520cbb7228f", "cwd": str(Path.cwd()),
          "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "argv": sys.argv,
          "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
          "git_blob": subprocess.check_output(["git", "hash-object", "--stdin"], input=raw).decode().strip(),
          "projection_sha256": hashlib.sha256(output.encode()).hexdigest(),
          "stdout_bytes": len(output.encode()), "stderr": "", "exit": 0,
          "scope": "Full selected record; not containing-file semantic full-read"}
with Path(__file__).with_name("json-read-delivery.jsonl").open("a") as f:
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
print(json.dumps({"path": path, "pointer": pointer}, ensure_ascii=False))
print(output, end="")
