"""Read back only this task's changed payloads at an immutable pushed commit.

No gameplay, old scripts, global inventory downloads, or remote mutation.
Usage from repository root:
  python <this-path> <immutable-commit> <base-commit> [output-file-in-this-directory]
The verification output is not included in the commit it verifies.
"""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.request

OUT = Path(__file__).resolve().parent
ROOT = Path.cwd().resolve()
PREFIX = str(OUT.relative_to(ROOT)) + "/"
REPO = "y805939188/pokemon-essentials-clean-room"


def git(*args):
    return subprocess.check_output(["git", *args])


def fetch_json(path):
    request = urllib.request.Request(
        "https://api.github.com/repos/" + REPO + "/" + path,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "Codex-R8-records-b-independent-review"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        assert response.status == 200
        return json.load(response)


def main():
    commit, base = sys.argv[1:3]
    assert len(commit) == len(base) == 40
    task_tree = git("rev-parse", commit + ":" + PREFIX[:-1]).decode().strip()
    checkout_tree = git("rev-parse", commit + "^{tree}").decode().strip()
    # The complete own task tree is small and exclusively new report material.
    local_entries = {}
    for line in git("ls-tree", "-r", task_tree).decode().splitlines():
        meta, path = line.split("\t", 1)
        mode, kind, sha = meta.split()
        assert kind == "blob"
        local_entries[path] = dict(mode=mode, type=kind, sha=sha)
    remote_tree = fetch_json("git/trees/" + task_tree + "?recursive=1")
    assert remote_tree["sha"] == task_tree and not remote_tree.get("truncated")
    remote_entries = {x["path"]: {k: x[k] for k in ["mode", "type", "sha"]}
                      for x in remote_tree["tree"] if x["type"] == "blob"}
    assert remote_entries == local_entries
    changed = git("diff", "--name-status", base, commit).decode().splitlines()
    changed_paths = []
    for line in changed:
        status, path = line.split("\t", 1)
        assert status in ["A", "M"] and path.startswith(PREFIX), line
        changed_paths.append(path)
    assert changed_paths

    def read_one(path):
        short = path[len(PREFIX):]
        entry = local_entries[short]
        expected = git("cat-file", "blob", entry["sha"])
        # Use raw bytes rather than printing/re-parsing a large text payload.
        request = urllib.request.Request(
            "https://raw.githubusercontent.com/" + REPO + "/" + commit + "/" + path,
            headers={"User-Agent": "Codex-R8-records-b-independent-review"},
        )
        with urllib.request.urlopen(request, timeout=45) as response:
            assert response.status == 200
            actual = response.read()
        assert actual == expected, path
        blob = hashlib.sha1(b"blob " + str(len(actual)).encode() + b"\0" + actual).hexdigest()
        assert blob == entry["sha"]
        return dict(path=path, mode=entry["mode"], git_blob=blob,
                    bytes=len(actual), sha256=hashlib.sha256(actual).hexdigest(),
                    full_remote_bytes_equal=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        entries = sorted(pool.map(read_one, changed_paths), key=lambda x: x["path"])
    remote_head = git("ls-remote", "--heads", "origin", "refs/heads/codex/r8-elr-records-b-20261016").decode().split()[0]
    assert remote_head == commit
    result = dict(schema="r8-records-b-incremental-remote-readback/v1", commit=commit,
        base_commit=base, checkout_tree=checkout_tree, task_tree=task_tree,
        remote_branch_head=remote_head, own_task_tree_exact=True,
        own_task_tree_files=len(local_entries),
        changed_payload_files=len(entries), changed_payload_bytes=sum(x["bytes"] for x in entries),
        entries=entries, all_changed_payloads_fully_read_back=True,
        tool_finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        qualification="TOOL_VALIDATION transport only; no semantic/gameplay credit. Reused unchanged fixed inputs, downloaded only changed own report bytes.")
    if len(sys.argv) > 3:
        dest = Path(sys.argv[3]).resolve()
        assert dest.parent == OUT and dest.name not in local_entries
        dest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "entries"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
