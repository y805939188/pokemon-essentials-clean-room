"""Read every changed payload fully from GitHub at the exact pushed commit."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import urllib.parse
import urllib.request

BASE = "469a268b92daed7b4d28d7fd0da75520cbb7228f"
BRANCH = "codex/remediation-sixth-r6-u12-author-20261014"
OWN = "review/remediation-sixth-20261014-prepare/candidates/R6-U12/"
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
tree = subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"]).decode().strip()
head = subprocess.run(["git", "ls-remote", "--heads", "origin", BRANCH], capture_output=True, text=True)
assert head.returncode == 0 and head.stdout.split()[0] == commit, head.stderr or head.stdout
paths = subprocess.check_output(["git", "diff", "--name-only", BASE, commit]).decode().splitlines()
assert paths and all(p.startswith(OWN) for p in paths)

def check(path):
    local = subprocess.check_output(["git", "show", commit + ":" + path])
    mode, kind, blob = subprocess.check_output(["git", "ls-tree", commit, "--", path]).decode().split()[:3]
    url = "https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/" + commit + "/" + urllib.parse.quote(path, safe="/")
    attempts = []
    for number in range(1, 4):
        began = datetime.datetime.now(datetime.timezone.utc).isoformat()
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                data = response.read()
                status = response.status
            digest = hashlib.sha256(data).hexdigest()
            remote_blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            assert data == local and remote_blob == blob
            attempts.append({"number": number, "start_utc": began, "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "http_status": status, "result": "MATCH_FULL_BYTES"})
            return {"path": path, "bytes": len(data), "sha256": digest, "git_blob": remote_blob,
                    "mode": mode, "type": kind, "commit": commit, "attempts": attempts,
                    "status": "REMOTE_FULL_PAYLOAD_MATCH"}
        except Exception as error:
            attempts.append({"number": number, "start_utc": began, "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "error": str(error), "result": "FAILED"})
            if number < 3:
                time.sleep(3)
    return {"path": path, "attempts": attempts, "status": "UNRESOLVED"}

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    records = list(pool.map(check, paths))
result = {"kind": "REMOTE_PAYLOAD_READBACK", "argv": sys.argv, "cwd": str(Path.cwd()),
          "start_utc": start, "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "commit": commit, "tree": tree, "branch": BRANCH, "remote_head_stdout": head.stdout,
          "mode_tree_binding": "Remote ref SHA binds the same Git commit/tree; each payload independently read in full over raw HTTPS and compared to its tree blob.",
          "records": records, "complete": all(x["status"] == "REMOTE_FULL_PAYLOAD_MATCH" for x in records),
          "reference_behavior_execution": 0}
if len(sys.argv) == 2:
    output = Path(sys.argv[1])
    assert str(output).startswith(OWN + "evidence/")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(0 if result["complete"] else 1)
