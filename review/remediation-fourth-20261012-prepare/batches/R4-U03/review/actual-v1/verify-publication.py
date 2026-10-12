#!/usr/bin/env python3
"""Read-only TOOL_VALIDATION: compare freshly fetched actual report and all tracked bytes.

No reference function, behavior model, host, or demo is imported or executed.
The caller creates a fresh bare object store and fetches the report branch first.
"""
import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

BASE = "d305ba47f31ecfde747b763682e87f32abe54888"
CANDIDATE = "5dd6789b22e03b85bb81ae73b9c65a1fab585186"
PACKAGE = "08a57fb55118914a74ac1ffaf617647c01df8938"
ROOT = "review/remediation-fourth-20261012-prepare/batches/R4-U03/review/actual-v1/"
PRIOR_REVIEW = "4c89f30285f55f017b021f5d6b5a538a02c4bc41"
PRIOR_ROOT = "review/remediation-fourth-20261012-prepare/batches/R4-U03/review/candidate-v2/"


def git(repo, *args):
    return subprocess.check_output(["git", "-C", repo, *args])


def entries(repo, commit, prefix=None):
    args = ["ls-tree", "-r", "-z", commit]
    if prefix:
        args.append(prefix)
    result = {}
    for entry in git(repo, *args).split(b"\0"):
        if not entry:
            continue
        header, path = entry.split(b"\t", 1)
        mode, kind, blob = header.decode().split()
        result[path.decode()] = (mode, kind, blob)
    return result


class BlobReader:
    def __init__(self, repo):
        self.process = subprocess.Popen(
            ["git", "-C", repo, "cat-file", "--batch"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        )

    def read(self, blob):
        self.process.stdin.write(blob.encode() + b"\n")
        self.process.stdin.flush()
        identity, kind, size = self.process.stdout.readline().split()
        assert identity.decode() == blob and kind == b"blob"
        remaining = int(size)
        pieces = []
        while remaining:
            chunk = self.process.stdout.read(remaining)
            assert chunk, "truncated blob"
            pieces.append(chunk)
            remaining -= len(chunk)
        assert self.process.stdout.read(1) == b"\n"
        return b"".join(pieces)

    def close(self):
        self.process.stdin.close()
        self.process.stdout.close()
        assert self.process.wait() == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", required=True)
    parser.add_argument("--fresh", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    assert not (Path(args.fresh) / "objects/info/alternates").exists(), "fresh store has alternates"
    remote_url = git(args.fresh, "config", "--get", "remote.origin.url").decode().strip()
    assert remote_url == "https://github.com/y805939188/pokemon-essentials-clean-room.git"
    assert git(args.fresh, "rev-parse", "FETCH_HEAD").decode().strip() == args.commit
    assert git(args.local, "cat-file", "commit", args.commit) == git(args.fresh, "cat-file", "commit", args.commit), "complete commit bytes differ"
    tree_id = git(args.local, "rev-parse", args.commit + "^{tree}").decode().strip()
    assert git(args.local, "cat-file", "tree", tree_id) == git(args.fresh, "cat-file", "tree", tree_id), "complete root tree bytes differ"
    for fixed in [BASE, CANDIDATE]:
        assert git(args.local, "cat-file", "commit", fixed) == git(args.fresh, "cat-file", "commit", fixed), "fixed complete commit bytes differ"
        fixed_tree = git(args.local, "rev-parse", fixed + "^{tree}").decode().strip()
        assert git(args.local, "cat-file", "tree", fixed_tree) == git(args.fresh, "cat-file", "tree", fixed_tree), "fixed complete root tree bytes differ"
    local = entries(args.local, args.commit)
    remote = entries(args.fresh, args.commit)
    assert local == remote, "complete tree entries differ"
    assert git(args.local, "rev-parse", args.commit + "^{tree}") == git(
        args.fresh, "rev-parse", args.commit + "^{tree}"
    ), "root tree differs"
    changed = git(args.local, "diff", "--name-only", BASE, args.commit).decode().splitlines()
    assert changed and all(p.startswith(ROOT) for p in changed), "review write domain exceeded"
    records = []
    local_reader = BlobReader(args.local)
    remote_reader = BlobReader(args.fresh)
    for path, (mode, kind, blob) in local.items():
        assert kind == "blob", "unexpected non-blob tracked entry"
        a = local_reader.read(blob)
        b = remote_reader.read(remote[path][2])
        assert a == b, "complete bytes differ: " + path
        if path.startswith(ROOT):
            assert a == (Path(args.local) / path).read_bytes(), "worktree bytes differ: " + path
        records.append({"path": path, "mode": mode, "git_blob": blob,
                        "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest(),
                        "full_remote_bytes_compared": True})
    local_reader.close()
    remote_reader.close()
    assert git(args.local, "cat-file", "commit", PRIOR_REVIEW) == git(
        args.fresh, "cat-file", "commit", PRIOR_REVIEW
    ), "prior review commit bytes differ"
    prior_local = entries(args.local, PRIOR_REVIEW, PRIOR_ROOT)
    prior_remote = entries(args.fresh, PRIOR_REVIEW, PRIOR_ROOT)
    assert prior_local == prior_remote, "prior review report entries differ"
    prior_records = []
    for path, (mode, kind, blob) in prior_local.items():
        assert kind == "blob"
        a = git(args.local, "cat-file", "blob", blob)
        b = git(args.fresh, "cat-file", "blob", prior_remote[path][2])
        assert a == b, "prior complete report bytes differ: " + path
        prior_records.append({"path": path, "mode": mode, "git_blob": blob,
                              "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest(),
                              "full_remote_bytes_compared": True})
    contract_path = "review/remediation-fourth-20261012-prepare/tasks/R4-U03/batch-contract.json"
    contract = json.loads(git(args.local, "show", PACKAGE + ":" + contract_path))
    formal = []
    for path in contract["allowed_formal_write_paths"]:
        a = git(args.local, "show", CANDIDATE + ":" + path)
        b = git(args.fresh, "show", args.commit + ":" + path)
        assert a == b, "published report inherited different candidate bytes: " + path
        formal.append({"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest(),
                       "full_candidate_bytes_equal": True})
    data = {"status": "PASS_FULL_REMOTE_BYTES", "evidence_level": "TOOL_VALIDATION",
            "checked_at": datetime.now(timezone.utc).isoformat(), "report_commit": args.commit,
            "report_tree": git(args.fresh, "rev-parse", args.commit + "^{tree}").decode().strip(),
            "fresh_object_store": args.fresh, "no_local_objects_or_alternates_copied": True,
            "fetched_from": remote_url, "fetched_head_matches_report_commit": True,
            "complete_tree_and_all_tracked_blob_bytes_compared": True,
            "complete_commit_bytes_compared": True, "complete_root_tree_bytes_compared": True,
            "file_count": len(records), "total_bytes": sum(x["bytes"] for x in records),
            "report_files": [x for x in records if x["path"].startswith(ROOT)],
            "prior_scoped_review_commit": PRIOR_REVIEW,
            "prior_report_files_compared": prior_records,
            "actual_commit": CANDIDATE, "task_publication": BASE, "formal_files_compared": formal,
            "changed_paths_from_evidence_parent": changed,
            "new_reference_execution": 0, "new_model_execution": 0,
            "new_host_or_demo_execution": 0, "execution_status": "NOT_EXECUTED_THIS_UPDATE"}
    Path(args.output).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: data[k] for k in ["status", "report_commit", "report_tree", "file_count", "total_bytes"]}))


if __name__ == "__main__":
    main()
