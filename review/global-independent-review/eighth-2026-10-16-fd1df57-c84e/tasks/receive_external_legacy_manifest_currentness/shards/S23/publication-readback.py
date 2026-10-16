#!/usr/bin/env python3
"""Verify only this group's changed publication bytes; grants no reading credit."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.parse
import urllib.request

REPO = "y805939188/pokemon-essentials-clean-room"
CONTRACT = "2d44dafe215842de6355f46de7d4d273d8b4c264"
GROUP = ("review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/"
         "tasks/receive_external_legacy_manifest_currentness/shards")
ROOT = Path(__file__).resolve().parents[7]
OWN = Path(__file__).resolve().parent


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "r8-group5-readback"})
    with urllib.request.urlopen(request, timeout=40) as response:
        assert response.status == 200
        return response.read()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--base", default=CONTRACT)
    parser.add_argument("--output")
    parser.add_argument("--api-evidence", help="Exact commit/tree responses from connected GitHub read-only fetch")
    args = parser.parse_args()
    commit = git("rev-parse", args.commit + "^{commit}").decode().strip()
    base = git("rev-parse", args.base + "^{commit}").decode().strip()
    git("merge-base", "--is-ancestor", base, commit)
    paths = git("diff", "--name-only", "-z", base, commit).decode().split("\0")[:-1]
    allowed = tuple(GROUP + "/" + shard + "/" for shard in ["S21", "S22", "S23"])
    assert paths and all(path.startswith(allowed) for path in paths), paths
    workspace_tree = git("rev-parse", commit + "^{tree}").decode().strip()
    group_tree = git("rev-parse", commit + ":" + GROUP).decode().strip()
    api = "https://api.github.com/repos/" + REPO + "/git/"
    supplied_api = json.loads(Path(args.api_evidence).read_text()) if args.api_evidence else None
    remote_commit = supplied_api["commit"] if supplied_api else json.loads(fetch(api + "commits/" + commit))
    assert remote_commit["sha"] == commit
    assert remote_commit["tree"]["sha"] == workspace_tree
    remote_tree = supplied_api["group_tree"] if supplied_api else json.loads(fetch(api + "trees/" + group_tree + "?recursive=1"))
    assert remote_tree["sha"] == group_tree and not remote_tree.get("truncated")
    expected = {}
    for line in git("ls-tree", "-r", "-z", commit, GROUP).split(b"\0"):
        if not line:
            continue
        metadata, path = line.split(b"\t", 1)
        mode, kind, blob = metadata.decode().split()
        assert kind == "blob" and mode == "100644"
        expected[path.decode()[len(GROUP) + 1:]] = (mode, blob)
    actual = {item["path"]: (item["mode"], item["sha"])
              for item in remote_tree["tree"] if item["type"] == "blob"}
    assert actual == expected, "remote path/mode/blob set differs"

    def verify(path):
        relative = path[len(GROUP) + 1:]
        mode, blob = actual[relative]
        local = git("show", commit + ":" + path)
        url = ("https://raw.githubusercontent.com/" + REPO + "/" + commit + "/"
               + urllib.parse.quote(path, safe="/"))
        raw = fetch(url)
        computed_blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        assert raw == local and computed_blob == blob, path
        return {"path": path, "mode": mode, "blob": blob, "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(), "remote_url": url,
                "whole_remote_bytes_read": True}

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        files = list(pool.map(verify, sorted(paths)))
    branch = "refs/heads/codex/r8-legacy-reception-group-5-20261016"
    remote_head = git("ls-remote", "origin", branch).decode().split()[0]
    assert remote_head == commit, (remote_head, commit)
    receipt = {"schema": "r8-group5-remote-readback/v1",
               "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "repository": REPO, "branch": branch, "commit": commit,
               "workspace_tree": workspace_tree, "group_tree": group_tree,
               "shard_trees": {s: git("rev-parse", commit + ":" + GROUP + "/" + s).decode().strip()
                               for s in ["S21", "S22", "S23"]},
               "base": base, "remote_branch_tip_matches": True,
               "remote_commit_and_tree_api_verified": True,
               "subtree_binding": "local Git Merkle paths bound by exact remote root tree; remote group tree independently fetched",
               "full_group_blob_set_mode_blob_verified": True,
               "group_total_file_count": len(actual), "changed_files_read_back": len(files),
               "changed_bytes_read_back": sum(f["bytes"] for f in files),
               "files": files, "semantic_credit": 0, "business_execution": 0,
               "qualification": "Transport identity only. S22 remains INCOMPLETE. Parent task-final signature retained."}
    if supplied_api:
        receipt["api_evidence"] = supplied_api
    encoded = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = (OWN / args.output).resolve()
        assert output.parent == OWN and not output.exists()
        output.write_text(encoded)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
