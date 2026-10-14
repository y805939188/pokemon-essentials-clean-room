#!/usr/bin/env python3
"""Read-only object/document checks; writes evidence only in this review directory."""
import collections
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
PREP = "469a268b92daed7b4d28d7fd0da75520cbb7228f"
CAND = "12a35f0d4635524ab2148c0979a1a4d69eeb982e"
TREE = "605030b0c08187a910032d45adf05f4e9cd5d72b"
FORMAL = "8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
REF = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
BASE = "review/remediation-sixth-20261014-prepare/"
PKG = BASE + "candidates/R6-U14/"

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

def obj(commit, path):
    return git("show", commit + ":" + path)

def identity(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()}

def inventory(commit, directory):
    rows = []
    for row in git("ls-tree", "-rz", commit, directory).split(b"\0"):
        if not row:
            continue
        meta, path = row.split(b"\t", 1)
        mode, kind, blob = meta.decode().split()
        name = path.decode()
        data = obj(commit, name)
        rows.append({"path": name, "mode": mode, "type": kind, **identity(data)})
        assert rows[-1]["git_blob"] == blob
    return rows

def main():
    started = utc()
    assert git("rev-parse", CAND + "^{tree}").decode().strip() == TREE
    assert git("rev-parse", REF + "^{tree}").decode().strip() == "7589c800b61ba13a13040ed0d686979b80a84fd0"
    prompt = obj(PREP, BASE + "prompts/R6-U14-R.md")
    assert identity(prompt) == {"bytes": 347700, "sha256": "6147147c2128aed9b37bcc61329e0583037290ff5d150f4f05535bfa268fa0be", "git_blob": "7a28dd53bc1a6a86f6f2de8e29ab4085bbc3af84"}
    raw_contract = obj(PREP, BASE + "contracts/R6-U14.json")
    contract = json.loads(raw_contract)
    ptext = prompt.decode()
    start = ptext.index("```json\n") + 8
    end = ptext.index("\n```", start)
    assert ptext[start:end].encode() + b"\n" == raw_contract
    payloads = inventory(CAND, PKG)
    changed = git("diff", "--name-only", PREP, CAND).decode().splitlines()
    assert len(changed) == 40
    assert all(p.startswith(PKG) for p in changed)
    assert set(changed) == {v["path"] for v in payloads}
    mirrors = [x for x in payloads if "/mirror/" in x["path"]]
    assert len(mirrors) == 14
    manifest = json.loads(obj(CAND, PKG + "evidence/candidate-manifest.json"))
    assert len(manifest["files"]) == 14
    for row in manifest["files"]:
        actual = identity(obj(CAND, row["candidate_path"]))
        assert all(actual[k] == row[k] for k in actual)
        baseline = obj(FORMAL, row["formal_path"])
        assert hashlib.sha256(baseline).hexdigest() == row["baseline_sha256"]
        assert obj(PREP, row["candidate_path"]) == baseline
    originals = {}
    def visit(v):
        if isinstance(v, dict):
            if "payload_identity" in v:
                i = v["payload_identity"]
                originals[(i["commit"], i["path"])] = i
            for x in v.values():
                visit(x)
        elif isinstance(v, list):
            for x in v:
                visit(x)
    visit(contract)
    inputs = []
    for (commit, path), row in sorted(originals.items()):
        data = obj(commit, path)
        actual = identity(data)
        assert all(actual[k] == row[k] for k in actual)
        tree_row = git("ls-tree", commit, "--", path).decode().strip().split()
        assert tree_row[0] == row["mode"] and tree_row[1] == "blob"
        inputs.append({"commit": commit, "path": path, "mode": tree_row[0], "type": row["type"], **actual})
    diffs = []
    old_tables = []
    new_vectors = []
    for row in manifest["files"]:
        path = row["formal_path"]
        before = obj(FORMAL, path).decode().splitlines(keepends=True)
        after = obj(CAND, row["candidate_path"]).decode().splitlines(keepends=True)
        diffs.extend(difflib.unified_diff(before, after, fromfile=FORMAL + ":" + path,
                                        tofile=CAND + ":" + row["candidate_path"]))
        if "/test-catalog/" in path:
            old = [x for x in before if x.startswith("|")]
            position = 0
            for line in old:
                position = after.index(line, position) + 1
            old_tables.append({"path": path, "preserved_table_lines": len(old), "evidence_level": "TOOL_VALIDATION; includes structural rows"})
            old_counts = collections.Counter(before)
            for number, line in enumerate(after, 1):
                if old_counts[line]:
                    old_counts[line] -= 1
                elif line.startswith("| LZ3") or line.startswith("| LZ4") or line.startswith("| R6-U14-"):
                    cells = line.split("|")
                    name = cells[1].strip()
                    if name.startswith("LZ") and int(name[2:]) < 36:
                        continue
                    # Status is declared in each new section's shared premises.
                    # Requiring the marker in every table row would misread the document.
                    preceding = "".join(after[max(0, number - 22):number])
                    assert "NOT_EXECUTED_THIS_UPDATE" in preceding
                    new_vectors.append({"id": name, "path": row["candidate_path"], "line": number,
                                        "row": line.rstrip("\n"), "evidence_level": "DERIVED_VECTOR; NOT_EXECUTED_THIS_UPDATE"})
    assert sum(x["preserved_table_lines"] for x in old_tables) == 910
    assert len(new_vectors) == 27
    declared_readbacks = json.loads(obj(CAND, PKG + "evidence/publication-readback.json"))
    core = declared_readbacks["core_commit"]
    assert git("rev-parse", core + "^{tree}").decode().strip() == declared_readbacks["core_tree"]
    core_changed = git("diff", "--name-only", PREP, core).decode().splitlines()
    assert len(core_changed) == 39
    assert {r["path"] for r in declared_readbacks["payload_readbacks"]} == set(core_changed)
    for r in declared_readbacks["payload_readbacks"]:
        data = obj(core, r["path"])
        actual = identity(data)
        assert all(actual[k] == r[k] for k in actual)
        assert r["remote_bytes"] == len(data) and r["remote_sha256"] == actual["sha256"]
    assert obj(CAND, PKG + "evidence/changed-paths.txt").decode().splitlines() == changed
    report = {"schema": "r6.u14.independent-tool-validation.v1", "utc_start": started, "utc_end": utc(),
              "argv": sys.argv, "cwd": str(ROOT), "runtime": platform.python_version(),
              "evidence_level": "TOOL_VALIDATION; document/object validation only; no source or host execution",
              "prepare": PREP, "candidate_commit": CAND, "candidate_tree": TREE,
              "candidate_directory_tree": git("rev-parse", CAND + ":" + PKG.rstrip("/")).decode().strip(),
              "prompt": identity(prompt), "contract": identity(raw_contract), "embedded_contract_exact_bytes": True,
              "candidate_payloads": payloads, "source_and_formal_inputs": inputs,
              "mirror_count": len(mirrors), "changed_payload_count": len(changed),
              "old_tables": old_tables, "new_vectors": new_vectors,
              "author_remote_receipt_static_check": "39 core paths match exact core; final frozen package has 40; independent remote readback is separate",
              "process_exit_code": 0, "stderr": "", "status": "PASS_TOOL_CHECKS_ONLY"}
    (OUT / "independent-validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    (OUT / "candidate-diff.txt").write_text("".join(diffs))
    print(json.dumps({"mirrors": len(mirrors), "new_vectors": len(new_vectors), "old_table_lines": 910,
                      "changed_payloads": len(changed), "validated_original_payloads": len(inputs),
                      "status": report["status"]}, ensure_ascii=False))

if __name__ == "__main__":
    main()
