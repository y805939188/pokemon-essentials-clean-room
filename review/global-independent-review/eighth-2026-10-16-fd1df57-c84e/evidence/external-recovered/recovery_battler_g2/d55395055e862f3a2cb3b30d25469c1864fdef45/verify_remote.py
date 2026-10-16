"""Independently fetch an already published C; verify this task's whole payload.

Usage: python verify_remote.py COMMIT [--record]
--record writes the result for the semantic core, before the proof-only commit.
No source, game, vector, or downloaded review script is executed.
"""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / ".git").exists())
TASK = HERE.relative_to(REPO).as_posix()
BRANCH = "codex/r8-recovery-battler-g2-20261016"
ORIGINAL = "codex/r8-battler-reception-group-2-20261016"
COMMIT = sys.argv[1]
assert len(COMMIT) == 40 and all(c in "0123456789abcdef" for c in COMMIT)


def call(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


origin = call(REPO, "remote", "get-url", "origin").decode().strip()
refs = call(REPO, "ls-remote", "--heads", "origin", BRANCH, ORIGINAL).decode()
branch_lines = [x.split() for x in refs.splitlines()]
assert [x[0] for x in branch_lines if x[1] == "refs/heads/" + BRANCH] == [COMMIT]
original_heads = [x for x in branch_lines if x[1] == "refs/heads/" + ORIGINAL]
assert not original_heads, "Original delivery appeared: inspect and deduplicate before further publication."
with tempfile.TemporaryDirectory(prefix=".remote-verify-", dir=HERE) as temporary:
    isolated = Path(temporary)
    subprocess.run(["git", "init", "--bare", str(isolated)], check=True, capture_output=True)
    call(isolated, "remote", "add", "origin", origin)
    fetched = subprocess.run(
        ["git", "-C", str(isolated), "fetch", "--no-tags", "--depth=1",
         "--filter=blob:none", "origin", COMMIT], check=True, capture_output=True, text=True)
    assert not (isolated / "objects/info/alternates").exists()
    remote_listing = call(isolated, "ls-tree", "-rz", COMMIT, "--", TASK)
    assert remote_listing == call(REPO, "ls-tree", "-rz", COMMIT, "--", TASK)
    rows = []
    for entry in remote_listing.split(b"\0"):
        if not entry:
            continue
        meta, path_bytes = entry.split(b"\t", 1)
        mode, kind, blob = meta.decode().split()
        assert kind == "blob" and mode == "100644"
        path = path_bytes.decode()
        remote_data = call(isolated, "cat-file", "blob", blob)
        local_data = call(REPO, "show", COMMIT + ":" + path)
        assert remote_data == local_data
        rows.append({"path": path, "mode": mode, "blob": blob,
                     "bytes": len(remote_data), "sha256": hashlib.sha256(remote_data).hexdigest()})
    workspace_tree = call(isolated, "rev-parse", COMMIT + "^{tree}").decode().strip()
    task_tree = call(isolated, "rev-parse", COMMIT + ":" + TASK).decode().strip()
    assert task_tree == call(REPO, "rev-parse", COMMIT + ":" + TASK).decode().strip()
result = {"schema": "r8-recovery-battler-g2-remote-readback/v1",
          "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "branch": BRANCH, "commit": COMMIT, "workspace_tree": workspace_tree,
          "task_tree": task_tree, "files": rows, "file_count": len(rows),
          "total_bytes": sum(x["bytes"] for x in rows), "independent_bare": True,
          "alternates": False, "fetch_exit": fetched.returncode,
          "fetch_stderr": fetched.stderr, "original_branch_heads": original_heads,
          "set_mode_blob_bytes_sha256_tree": "ALL_MATCH",
          "semantic_credit_from_transport": 0, "business_execution": "NOT_EXECUTED",
          "UPDATE_NOT_STARTED": True}
if "--record" in sys.argv[2:]:
    assert not (HERE / "remote-readback.json").exists()
    (HERE / "remote-readback.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k not in ["files", "fetch_stderr"]}, ensure_ascii=False))
