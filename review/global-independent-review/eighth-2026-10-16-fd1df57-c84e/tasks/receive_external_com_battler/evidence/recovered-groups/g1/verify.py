"""Validate this bounded evidence and read its published blobs from a fresh remote store.

No game, recovered script, model, or reference code is executed. A remote receipt
binds an earlier immutable core; its own later publication is checked externally.
"""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[4]
ROOT = TASK.parents[1]
CONTRACT = "02c8206651676effe40ff9a33dbb70998b79c1b1"
BRANCH = "codex/r8-recovery-battler-g1-20261016"
ORIGINAL = "codex/r8-battler-reception-group-1-20261016"
URL = "https://github.com/y805939188/pokemon-essentials-clean-room.git"
TASK_PATH = TASK.relative_to(REPO).as_posix()


def run(*args):
    return subprocess.check_output(args, stderr=subprocess.PIPE)


def git(*args):
    return run("git", "-C", str(REPO), *args)


def check():
    ledger = json.loads((TASK / "reception.json").read_text())
    selected = {}
    for split in ("P01A", "P01B", "P02"):
        selected[split] = json.loads((ROOT / "tasks/receive_external_com_battler/splits" / split / "readset.json").read_text())
    expected_units = {u["id"] for d in selected.values() for u in d["primary_compounds"]}
    expected_children = {c for d in selected.values() for c in d["primary_child_ids"]}
    actual_children = [c for u in ledger["primary"] for c in u["child_ids"]]
    assert {u["id"] for u in ledger["primary"]} == expected_units
    assert len(actual_children) == len(set(actual_children)) == 382
    assert set(actual_children) == expected_children
    assert {r["id"] for r in ledger["reverse_local_facets"]} == {c for d in selected.values() for c in d["assigned_reverse_child_ids"]}
    assert len(ledger["reverse_local_facets"]) == 61
    assert len(ledger["cross_split_support_units"]) == 17
    assert len(ledger["consumer_facts"]) == 23
    assert len(ledger["foreign_facets"]) == 12
    for row in ledger["primary"]:
        obj = next(u for u in selected[row["split"]]["primary_compounds"] if u["id"] == row["id"])
        assert row["source_ref"]["ranges"] == obj["source"]["ranges"]
        assert row["comparison"] in ledger["manual_comparisons"]
    reading = json.loads((TASK / "reading.json").read_text())
    for f in reading["identities"]:
        raw = run("git", "-C", f["repo"], "show", f["commit"] + ":" + f["path"])
        assert len(raw) == f["bytes"] and hashlib.sha256(raw).hexdigest() == f["sha256"]
    assert git("branch", "--show-current").decode().strip() == BRANCH
    changes = git("diff", "--name-only", CONTRACT).decode().splitlines()
    untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
    assert all(p.startswith(TASK_PATH + "/") for p in changes + untracked)
    print(json.dumps({"scope_check": "PASS", "primary_units": 160, "children": 382,
                      "local_reverse": 61, "cross_support": 17, "consumer_facts": 23,
                      "foreign_whole_facets_open": 12, "semantic_credit_from_validation": 0}))


def remote(commit, receipt_name=None):
    assert len(commit) == 40 and all(c in "0123456789abcdef" for c in commit)
    bare = TASK / ".remote.git"
    if not bare.exists():
        run("git", "init", "--bare", str(bare))
        run("git", "--git-dir=" + str(bare), "remote", "add", "origin", URL)
        run("git", "--git-dir=" + str(bare), "config", "remote.origin.promisor", "true")
        run("git", "--git-dir=" + str(bare), "config", "remote.origin.partialclonefilter", "blob:none")
    assert not (bare / "objects/info/alternates").exists()

    def rg(*args):
        return run("git", "--git-dir=" + str(bare), *args)

    rg("fetch", "--depth=1", "--filter=blob:none", "--no-tags", "origin", commit)
    assert rg("rev-parse", "FETCH_HEAD").decode().strip() == commit
    entries = rg("ls-tree", "-r", commit, "--", TASK_PATH)
    assert entries == git("ls-tree", "-r", commit, "--", TASK_PATH)
    files = []
    for line in entries.decode().splitlines():
        meta, path = line.split("\t")
        mode, kind, blob = meta.split()
        assert mode == "100644" and kind == "blob"
        raw = rg("cat-file", "blob", blob)
        assert raw == git("cat-file", "blob", blob)
        assert raw == (REPO / path).read_bytes()
        if path.endswith(".json"):
            json.loads(raw)
        files.append({"path": path, "mode": mode, "blob": blob, "bytes": len(raw),
                      "sha256": hashlib.sha256(raw).hexdigest(), "complete_remote_equal": True})
    refs = run("git", "ls-remote", URL, "refs/heads/" + BRANCH, "refs/heads/" + ORIGINAL, "refs/heads/main").decode().splitlines()
    assert commit + "\trefs/heads/" + BRANCH in refs
    changed = git("diff", "--name-only", CONTRACT, commit).decode().splitlines()
    assert all(p.startswith(TASK_PATH + "/") for p in changed)
    tree = rg("rev-parse", commit + "^{tree}").decode().strip()
    task_tree = rg("rev-parse", commit + ":" + TASK_PATH).decode().strip()
    assert tree == git("rev-parse", commit + "^{tree}").decode().strip()
    assert task_tree == git("rev-parse", commit + ":" + TASK_PATH).decode().strip()
    result = {"schema": "r8-recovery-battler-g1-remote/v1",
              "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "commit": commit, "workspace_tree": tree, "task_tree": task_tree,
              "branch": BRANCH, "files": files, "file_count": len(files),
              "remote_refs": refs, "original_branch_present": any(x.endswith("refs/heads/" + ORIGINAL) for x in refs),
              "isolated_store_no_alternates": True, "mode_blob_bytes_sha256_set_tree": "ALL_MATCH",
              "changed_paths": changed, "semantic_credit": 0, "business": "NOT_EXECUTED",
              "UPDATE_NOT_STARTED": True}
    if receipt_name:
        receipt = TASK / receipt_name
        assert receipt.parent == TASK and not receipt.exists()
        receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        check()
    else:
        remote(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
