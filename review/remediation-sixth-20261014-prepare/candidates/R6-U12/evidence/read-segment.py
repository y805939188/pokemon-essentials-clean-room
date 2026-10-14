"""Read a bounded Git payload segment; receipt is output evidence, not semantic PASS."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

start = datetime.datetime.now(datetime.timezone.utc).isoformat()
commit, path, first, last = sys.argv[1:]
first, last = int(first), int(last)
data = subprocess.check_output(["git", "show", f"{commit}:{path}"])
lines = data.decode().splitlines()
assert 1 <= first <= last <= len(lines)
out = f"{commit}:{path} [{first}-{last}/{len(lines)}]\n" + "\n".join(
    f"{i + 1}: {lines[i]}" for i in range(first - 1, last)
) + "\n"
print(out, end="")
receipt = {
    "argv": sys.argv, "cwd": str(Path.cwd()), "start_utc": start,
    "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "commit": commit, "path": path, "range": [first, last],
    "total_lines": len(lines), "bytes": len(data),
    "sha256": hashlib.sha256(data).hexdigest(),
    "git_blob": subprocess.check_output(["git", "rev-parse", f"{commit}:{path}"]).decode().strip(),
    "stdout_sha256": hashlib.sha256(out.encode()).hexdigest(),
    "stderr": "", "exit_code": 0, "kind": "READ_OUTPUT_ONLY",
}
with Path(__file__).with_name("read-segments.jsonl").open("a") as f:
    f.write(json.dumps(receipt, ensure_ascii=False) + "\n")
