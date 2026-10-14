import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parent
path = "deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md"
start, end = map(int, sys.argv[1:])
candidate_path = "review/remediation-sixth-20261014-prepare/candidates/R6-U11/mirror/" + path
identities = []
texts = []
for commit, p, offset in [("8ea169fbd0f33f378b5d732fd6bea59e854e04a6", path, 0),
                           ("e93d0e56750a6a16cc50cc68b2c97f11ea255153", candidate_path, 31)]:
    argv = ["git", "show", commit + ":" + p]
    begin = datetime.datetime.now(datetime.timezone.utc).isoformat()
    r = subprocess.run(argv, capture_output=True, check=True)
    finish = datetime.datetime.now(datetime.timezone.utc).isoformat()
    rows = r.stdout.decode().splitlines(keepends=True)
    texts.append(rows[start + offset - 1:end + offset])
    identities.append({"reader": "R6-U11-R /root", "commit": commit, "path": p,
                       "lines": [start + offset, end + offset], "cwd": str(pathlib.Path.cwd()),
                       "argv": argv, "start_utc": begin, "end_utc": finish, "exit_code": 0,
                       "stderr": r.stderr.decode(), "payload_bytes": len(r.stdout),
                       "payload_sha256": hashlib.sha256(r.stdout).hexdigest(),
                       "payload_git_blob": hashlib.sha1(b"blob " + str(len(r.stdout)).encode() + b"\0" + r.stdout).hexdigest(),
                       "read_mode": "fresh complete matched span from both fixed blobs; shared text output with two line coordinates"})
assert texts[0] == texts[1]
out = "".join(f"formal:{start+i} candidate:{start+i+31} | {line}" for i, line in enumerate(texts[0]))
for record in identities:
    record["stdout_shared_span_bytes"] = len(out.encode())
    record["stdout_shared_span_sha256"] = hashlib.sha256(out.encode()).hexdigest()
    with (root / "reading-ledger.jsonl").open("a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
print(out, end="")
