"""Read this exact review directory back through an incremental Git fetch.

Use a disposable bare repository whose object store was snapshotted BEFORE the
review commit. All new payload blobs and the new commit must be absent before
fetch. Existing baseline pack files may be hardlinked; no baseline re-download.
Usage: python verify_remote.py --commit SHA --isolated-git-dir /tmp/r6a-remote.git
       --output /tmp/r6a-readback.json
No reference code is imported or executed. The receipt stays outside this tree.
"""
import argparse
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

BRANCH = "codex/r8-final-r6-a-20261016"
ORIGIN = "https://github.com/y805939188/pokemon-essentials-clean-room.git"


def run(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd)


def identity(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob": hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()}


def exists(repo, obj):
    return subprocess.run(["git", "cat-file", "-e", obj], cwd=repo,
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--isolated-git-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(run("git", "rev-parse", "--show-toplevel").decode().strip())
    directory = Path(__file__).resolve().parent.relative_to(root).as_posix()
    isolated = args.isolated_git_dir.resolve()
    assert isolated != root and not (isolated / "objects/info/alternates").exists()
    assert not args.output.resolve().is_relative_to(root / directory)
    assert run("git", "rev-parse", "--is-bare-repository", cwd=isolated).strip() == b"true"
    assert run("git", "remote", "get-url", "origin", cwd=isolated).decode().strip() == ORIGIN
    commit = run("git", "rev-parse", f"{args.commit}^{{commit}}").decode().strip()
    assert not exists(isolated, commit), "Commit already existed: not a fresh remote reception"
    expected = {}
    for entry in run("git", "ls-tree", "-r", "-z", commit, "--", directory).split(b"\0"):
        if not entry:
            continue
        metadata, path = entry.split(b"\t", 1)
        mode, kind, blob = metadata.decode().split()
        assert kind == "blob"
        assert not exists(isolated, blob), "New blob already existed in isolated receiver"
        expected[path.decode()] = {"mode": mode, "blob": blob}
    remote = run("git", "ls-remote", "--heads", "origin", "refs/heads/" + BRANCH).decode().split()
    assert remote[0] == commit
    subprocess.run(["git", "fetch", "--no-tags", "origin", commit], cwd=isolated, check=True)
    assert run("git", "rev-parse", "FETCH_HEAD", cwd=isolated).decode().strip() == commit
    root_tree = run("git", "rev-parse", f"{commit}^{{tree}}", cwd=isolated).decode().strip()
    task_tree = run("git", "rev-parse", f"{commit}:{directory}", cwd=isolated).decode().strip()
    assert root_tree == run("git", "rev-parse", f"{commit}^{{tree}}").decode().strip()
    assert task_tree == run("git", "rev-parse", f"{commit}:{directory}").decode().strip()
    actual = {}
    for entry in run("git", "ls-tree", "-r", "-z", commit, "--", directory, cwd=isolated).split(b"\0"):
        if not entry:
            continue
        metadata, path = entry.split(b"\t", 1)
        mode, kind, blob = metadata.decode().split()
        assert kind == "blob"
        actual[path.decode()] = {"mode": mode, "blob": blob}
    assert actual == expected
    files = []
    for path, row in sorted(expected.items()):
        payload = run("git", "cat-file", "blob", row["blob"], cwd=isolated)
        local = run("git", "cat-file", "blob", row["blob"])
        assert payload == local
        values = identity(payload)
        assert values["git_blob"] == row["blob"]
        files.append({"path": path, "mode": row["mode"], **values})
    result = {"schema": "r8-r6-a-remote-readback/v1",
              "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "repository": ORIGIN, "branch": BRANCH, "commit": commit,
              "workspace_tree": root_tree, "task_tree": task_tree,
              "all_new_blobs_and_commit_absent_before_fetch": True,
              "no_alternates": True, "incremental_fetch_only": True,
              "complete_set_mode_blob_bytes_sha_tree_verified": True,
              "files": files, "files_verified": len(files),
              "bytes_verified": sum(x["bytes"] for x in files),
              "semantic_completion_credit": 0, "semantic_state": "INCOMPLETE"}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "files"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
