"""Bounded read delivery and identity ledger; never executes reference code."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ref, path, first, last = sys.argv[1:]
first, last = int(first), int(last)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
if ref == "WORKTREE":
    raw = Path(path).read_bytes()
    blob = subprocess.check_output(["git", "hash-object", "--stdin"], input=raw).decode().strip()
    mode = "100644"
else:
    raw = subprocess.check_output(["git", "show", f"{ref}:{path}"])
    entry = subprocess.check_output(["git", "ls-tree", ref, "--", path], text=True).split()
    mode, blob = entry[0], entry[2]
lines = raw.decode("utf-8-sig").splitlines()
assert 1 <= first <= last <= len(lines), (first, last, len(lines))
output = "\n".join(f"{i}: {lines[i-1]}" for i in range(first, last+1)) + "\n"
record = {"kind": "READ_DELIVERY_NOT_AUTOMATIC_SEMANTIC_PASS", "argv": sys.argv,
          "cwd": str(Path.cwd()), "start_utc": started,
          "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "ref": ref, "path": path, "mode": mode, "type": "blob", "bytes": len(raw),
          "sha256": hashlib.sha256(raw).hexdigest(), "git_blob": blob,
          "total_lines": len(lines), "ranges": [[first, last]],
          "stdout_bytes": len(output.encode()), "stdout_sha256": hashlib.sha256(output.encode()).hexdigest(),
          "stderr": "", "exit": 0, "runtime": sys.version}
ledger = Path(__file__).with_name("read-delivery.jsonl")
with ledger.open("a") as f:
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
print(json.dumps({"input": path, "ref": ref, "ranges": [[first,last]], "total_lines": len(lines)}, ensure_ascii=False))
print(output, end="")
