"""Read fixed Git text without executing it; record exact presented slices, never PASS."""
import argparse
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPOS = {
    "R": ("/workspace/pokemon-essentials", "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"),
    "B8": ("/workspace/pokemon-essentials-clean-room", "fd1df570cad987dc3852a3b958f03916e317f7fe"),
}


def present(repo, path, start, end):
    directory, commit = REPOS[repo]
    args = ["git", "-C", directory]
    raw = subprocess.check_output(args + ["show", commit + ":" + path])
    lines = raw.decode("utf-8").splitlines(keepends=True)
    assert 1 <= start <= end <= len(lines), (path, start, end, len(lines))
    selected = "".join(lines[start - 1:end])
    assert len(selected) <= 16000, "Use smaller consecutive ranges; nothing presented."
    listing = subprocess.check_output(args + ["ls-tree", commit, "--", path]).decode().strip()
    print(f"{repo} {path} L{start}-{end} / {len(lines)}")
    for index in range(start - 1, end):
        print(f"{index + 1}: {lines[index]}", end="")
    entry = {
        "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "repo": repo, "commit": commit, "path": path, "tree_entry": listing,
        "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
        "range": [start, end], "slice_sha256": hashlib.sha256(selected.encode()).hexdigest(),
        "meaning": "ACTUAL_PRESENTATION_ONLY; reader judgment separately recorded",
        "behavior_execution": 0,
    }
    with (ROOT / "evidence/read-slices.jsonl").open("a") as stream:
        stream.write(json.dumps(entry, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", choices=REPOS)
    parser.add_argument("path")
    parser.add_argument("start", type=int)
    parser.add_argument("end", type=int)
    cli = parser.parse_args()
    present(cli.repo, cli.path, cli.start, cli.end)
