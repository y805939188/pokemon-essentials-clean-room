#!/usr/bin/env python3
"""Finite artifact checks only; never load or execute reference/game definitions."""
import difflib
import hashlib
import json
import pathlib
import re
import subprocess

REPO = pathlib.Path(__file__).resolve().parents[5]
ROOT = REPO / "review/remediation-sixth-20261014-prepare"
OWN = ROOT / "candidates/R6-U08"
PREPARE = "469a268b92daed7b4d28d7fd0da75520cbb7228f"
MAIN = "8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
SELECTED = "13fddb0a217b36974c75657aa68da0caf104ee48"
CONTRACT = json.loads((ROOT / "contracts/R6-U08.json").read_text())


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO)


def identity(data):
    return {
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "git_blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
    }


checks = []
changed = []
allow = str(OWN.relative_to(REPO)) + "/"
paths = CONTRACT["candidate_formal_paths"]
mirrors = {allow + "mirror/" + p for p in paths}
for p in set(git("diff", "--name-only", PREPARE).decode().splitlines()
             + git("ls-files", "--others", "--exclude-standard").decode().splitlines()):
    assert p in mirrors or p.startswith(allow + "evidence/"), p
checks.append("tracked and untracked difference stays in exact author allowlist")
assert git("branch", "--show-current").decode().strip() == "codex/remediation-sixth-r6-u08-author-20261014"
assert not git("diff", PREPARE, "--", "deliverables", "reference", "audit", "planning")
checks.append("protected tracked formal/reference/audit/planning paths unchanged from prepare")

allowed_old_lines = [{33, 59, 60, 108, 123, 285}, {11, 15, 20, 33}]
for p, allowed_lines in zip(paths, allowed_old_lines):
    original = git("show", MAIN + ":" + p)
    assert original == (REPO / p).read_bytes()
    assert original == git("show", SELECTED + ":" + p)
    mirror_path = OWN / "mirror" / p
    before = original.decode().splitlines(keepends=True)
    after = mirror_path.read_text().splitlines(keepends=True)
    removed, added, retained = [], [], 0
    for op, a, b, c, d in difflib.SequenceMatcher(None, before, after, autojunk=False).get_opcodes():
        if op == "equal":
            retained += b - a
        else:
            for n in range(a, b):
                assert n + 1 in allowed_lines, (p, op, n + 1)
                removed.append(n + 1)
            added += after[c:d]
    assert set(removed) == allowed_lines
    new_text = "".join(added)
    assert not re.search(r"Data/Scripts/|MenuHandlers|\bdef self\.|\bclass [A-Z]|```(?:ruby|typescript|ts)", new_text)
    changed.append({"formal_path": p, "baseline": identity(original),
                    "candidate": identity(mirror_path.read_bytes()),
                    "only_replaced_baseline_lines": sorted(removed),
                    "retained_baseline_lines": retained, "added_line_count": len(added)})
checks.append("only six WP72 and four catalog baseline lines replaced; all other old lines preserved")
checks.append("selected fifth candidate bytes equal frozen formal baseline; no historical verdict transfer")
checks.append("new formal text introduces no source code or source organization tokens")

catalog = (OWN / "mirror" / paths[1]).read_text()
vector_ids = re.findall(r"^\| (DG-U08-\d+)／DEBUG-\d{3} \|", catalog, re.M)
assert vector_ids == ["DG-U08-%02d" % n for n in range(1, 29)]
assert len(vector_ids) == len(set(vector_ids))
checks.append("28 additional static vectors have unique sequential IDs; original DG-M01–M30 retained")
packet = json.loads((OWN / "evidence/id-evidence.json").read_text())
required_groups = {"identity_and_verdict", "bidirectional_evidence", "premises_and_counterexample",
                   "minimum_revision_contract", "acceptance_and_regression",
                   "independent_adjudication", "dependencies_and_receivers"}
assert [r["id"] for r in packet["records"]] == CONTRACT["required_ids"]
for r, original in zip(packet["records"], CONTRACT["scope_contracts"]):
    assert required_groups <= r.keys()
    assert r["identity_and_verdict"]["severity"] == original["identity_and_verdict"]["severity"]
    assert not r["identity_and_verdict"]["candidate_pass"]
    assert not r["identity_and_verdict"]["formal_accepted"]
    assert not r["identity_and_verdict"]["closed"]
    for x in r["bidirectional_evidence"]["formal_mirror"]:
        actual = identity((REPO / x["path"]).read_bytes())
        assert all(actual[k] == x[k] for k in actual)
checks.append("all five IDs have seven evidence groups, current mirror hashes, and independent review pending")
assert sum(len(r["acceptance_and_regression"]["vectors"]) for r in packet["records"]) == 28
status = json.loads((OWN / "evidence/execution-status.json").read_text())
for k in ("reference_execution", "independent_behavior_model_execution", "native_host_execution",
          "demo_execution", "physical_input", "real_save"):
    assert status[k] == 0
assert not status["real_username_read"] and not status["closed"]
checks.append("source/static/tool and unexecuted host/model/save evidence remain separate")
result = {"schema": "r6-u08.artifact-validation.v1", "level": "TOOL_VALIDATION",
          "result": "PASS_FINITE_ARTIFACT_CHECKS", "semantic_execution": False,
          "independent_review": "PENDING", "checks": checks, "mirror_changes": changed}
(OWN / "evidence/validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(result, ensure_ascii=False, indent=2))
