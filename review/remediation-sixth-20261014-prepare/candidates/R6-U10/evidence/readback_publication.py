"""Fetch published branch into separate objects, then verify every changed payload."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

PREP = "469a268b92daed7b4d28d7fd0da75520cbb7228f"
BRANCH = "codex/remediation-sixth-r6-u10-author-20261014"
OWN = "review/remediation-sixth-20261014-prepare/candidates/R6-U10"
EVIDENCE = Path(OWN + "/evidence")
expected, output_name = sys.argv[1:]
assert len(expected) == 40 and all(ch in "0123456789abcdef" for ch in expected)
assert output_name == "-" or ("/" not in output_name and output_name.endswith(".json"))
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
bare = EVIDENCE / "remote-readback.git"
commands = []


def run(argv, data=None):
    result = subprocess.run(argv, input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    commands.append({"argv": argv, "exit_code": result.returncode,
                     "stderr": result.stderr.decode(errors="replace"),
                     "stdout_sha256": hashlib.sha256(result.stdout).hexdigest(),
                     "stdout_bytes": len(result.stdout)})
    assert result.returncode == 0, commands[-1]
    return result.stdout


def local(*args):
    return run(["git", *args])


def remote(*args, data=None):
    return run(["git", "--git-dir=" + str(bare), *args], data=data)


url = local("remote", "get-url", "origin").decode().strip()
assert url == "https://github.com/y805939188/pokemon-essentials-clean-room.git"
if not bare.exists():
    run(["git", "init", "--bare", "--quiet", str(bare)])
    remote("remote", "add", "origin", url)
    remote("config", "remote.origin.promisor", "true")
    remote("config", "remote.origin.partialclonefilter", "blob:none")
remote("fetch", "--depth=1", "--filter=blob:none", "origin", "refs/heads/" + BRANCH)
assert not (bare / "objects/info/alternates").exists()
actual = remote("rev-parse", "FETCH_HEAD").decode().strip()
assert actual == expected, (actual, expected)
local_tree = local("rev-parse", expected + "^{tree}").decode().strip()
remote_tree = remote("rev-parse", actual + "^{tree}").decode().strip()
assert local_tree == remote_tree
local_mirror_tree = local("rev-parse", expected + ":" + OWN + "/mirror").decode().strip()
remote_mirror_tree = remote("rev-parse", actual + ":" + OWN + "/mirror").decode().strip()
assert local_mirror_tree == remote_mirror_tree
paths = local("diff", "--name-only", PREP, expected).decode().splitlines()
assert all(path.startswith(OWN + "/mirror/") or path.startswith(OWN + "/evidence/") for path in paths)
rows = []
for path in paths:
    entry_local = local("ls-tree", expected, "--", path).decode().split()
    entry_remote = remote("ls-tree", actual, "--", path).decode().split()
    assert entry_local == entry_remote, path
    blob = entry_remote[2]
    raw_local = local("cat-file", "blob", blob)
    raw_remote = remote("cat-file", "blob", blob)
    assert raw_local == raw_remote, path
    rows.append({"path": path, "mode": entry_remote[0], "type": entry_remote[1],
                 "git_blob": blob, "bytes": len(raw_remote),
                 "sha256": hashlib.sha256(raw_remote).hexdigest(), "full_bytes_match": True})
receipt = {"kind": "PUBLISHED_CANDIDATE_FULL_CHANGED_PAYLOAD_READBACK_TOOL_ONLY",
           "started_utc": started, "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "cwd": str(Path.cwd()), "remote": url, "branch": BRANCH, "prepare": PREP,
           "expected_commit": expected, "actual_fetched_commit": actual,
           "actual_tree": remote_tree, "mirror_tree": remote_mirror_tree,
           "object_isolation": "Fresh independent bare Git object directory; no alternates; filtered remote fetch",
           "changed_paths": rows, "changed_path_count": len(rows),
           "commands": commands, "exit_code": 0, "reference_model_host_behavior_execution": 0,
           "author_review_status": "READY_FOR_NONAUTHOR_REVIEW_NOT_SELF_PASS",
           "formal_acceptance": False, "CLOSED": False}
if output_name != "-":
    (EVIDENCE / output_name).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"commit": actual, "tree": remote_tree, "mirror_tree": remote_mirror_tree,
                  "full_changed_payloads_verified": len(rows), "tool_exit_code": 0,
                  "all_payload_mode_type_blob_bytes_sha256_match": True,
                  "receipt": str(EVIDENCE / output_name) if output_name != "-" else "Final tool output; no recursive receipt commit"}, ensure_ascii=False))
