import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parent
commit, path, *pointers = sys.argv[1:]
argv = ["git", "show", commit + ":" + path]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
p = subprocess.run(argv, capture_output=True)
finished = datetime.datetime.now(datetime.timezone.utc).isoformat()
if p.returncode:
    sys.stderr.buffer.write(p.stderr)
    sys.exit(p.returncode)
data = json.loads(p.stdout)
for pointer in pointers:
    node = data
    for key in pointer.strip("/").split("/") if pointer else []:
        key = key.replace("~1", "/").replace("~0", "~")
        node = node[int(key)] if isinstance(node, list) else node[key]
    print(json.dumps({"pointer": pointer, "complete_value": node}, ensure_ascii=False, indent=2))
record = {
    "reader": "R6-U11-R /root", "cwd": str(pathlib.Path.cwd()), "argv": argv,
    "start_utc": started, "end_utc": finished, "exit_code": p.returncode,
    "stderr": p.stderr.decode(), "commit": commit, "path": path,
    "complete_json_pointers": pointers, "payload_bytes": len(p.stdout),
    "payload_sha256": hashlib.sha256(p.stdout).hexdigest(),
    "payload_git_blob": hashlib.sha1(b"blob " + str(len(p.stdout)).encode() + b"\0" + p.stdout).hexdigest(),
    "evidence_level": "HISTORICAL_OR_CONTRACT_DOCUMENT_READ",
    "not_full_file_semantic_read": pointers != [""]
}
with (root / "reading-ledger.jsonl").open("a") as f:
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
