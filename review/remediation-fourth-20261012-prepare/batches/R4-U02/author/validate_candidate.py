#!/usr/bin/env python3
"""Validate file identities and bounded candidate structure; never execute behavior."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
PACK = ROOT / "review/remediation-fourth-20261012-prepare"
START = "08a57fb55118914a74ac1ffaf617647c01df8938"
BASE = "1f36475d22120a0d1175967d5b17d71fe8311d88"
REL = HERE.relative_to(ROOT).as_posix() + "/"


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def read(name):
    return json.loads((HERE / name).read_text())


def require(value, message):
    if not value:
        raise AssertionError(message)


def verify_bytes(record, data):
    require(len(data) == record["bytes"], "bytes: " + record["path"])
    require(hashlib.sha256(data).hexdigest() == record["sha256"], "sha256: " + record["path"])
    blob = subprocess.check_output(["git", "hash-object", "--stdin"], input=data).decode().strip()
    require(blob == record["git_blob"], "blob: " + record["path"])


def main():
    contract = json.loads((PACK / "tasks/R4-U02/batch-contract.json").read_text())
    formal = contract["allowed_formal_write_paths"]
    changed = set(git("diff", "--name-only", START).decode().splitlines())
    untracked = set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    all_changed = changed | untracked
    require(all(p in formal or p.startswith(REL) for p in all_changed), "write outside allowlist")
    require({p for p in changed if not p.startswith(REL)} == set(formal), "exact 8 formal paths")
    git("diff", "--check", START)
    for path in formal:
        require(git("show", START + ":" + path) == git("show", BASE + ":" + path), "formal input drift")

    identities = read("formal-identities.json")
    require(len(identities["files"]) == 8, "formal identity count")
    for item in identities["files"]:
        verify_bytes(item["before"], git("show", BASE + ":" + item["before"]["path"]))
        verify_bytes(item["after"], (ROOT / item["after"]["path"]).read_bytes())

    acceptance = read("acceptance-map.json")
    canonical = json.loads((PACK / "tasks/R4-U02/findings-input.json").read_text())["canonical_root_records"]
    require(acceptance["not_independent_pass"] is True, "author cannot sign independent PASS")
    require({r["id"] for r in acceptance["records"]} == set(contract["finding_ids"]), "finding set")
    require(sum(len(r["criteria"]) for r in acceptance["records"]) == 15, "all acceptance criteria")
    for record in acceptance["records"]:
        original = next(r for r in canonical if r["id"] == record["id"])
        require([c["complete_criterion"] for c in record["criteria"]] == original["acceptance_criteria"], "complete criteria")
        require(record["preconditions"] == original["preconditions"], "complete preconditions")
        require(record["all_required_refinements"] == original["review_resolution"]["independent_counterreview"]["required_refinements"], "complete refinements")
        require(record["independent_verdict"] is None, "independent verdict pending")
        for criterion in record["criteria"]:
            require(criterion["execution_status"] == "NOT_EXECUTED_THIS_UPDATE", "execution limit")
            for anchor in criterion["anchors"]:
                line = (ROOT / anchor["path"]).read_text().splitlines()[anchor["line"] - 1]
                require(anchor["contains"] in line, "precise anchor drift")

    test_path = formal[-1]
    tests = (ROOT / test_path).read_text().splitlines()
    vectors = [line for line in tests if re.match(r"\| GR4-(RM|SF|ER)\d{2} \|", line)]
    require(len(vectors) == 26, "vector count")
    vector_ids = [line.split("|")[1].strip() for line in vectors]
    require(len(set(vector_ids)) == 26, "unique vector IDs")
    for prefix, count in [("RM", 12), ("SF", 7), ("ER", 7)]:
        require({v for v in vector_ids if v.startswith("GR4-" + prefix)} == {f"GR4-{prefix}{i:02d}" for i in range(1, count + 1)}, "complete vector IDs")
    require(all(line.endswith("| NOT_EXECUTED |") and len(line.split("|")) == 6 for line in vectors), "vector status/table shape")

    regression = read("affected-regression.json")
    old_tests = git("show", BASE + ":" + test_path).decode().splitlines()
    for row in regression["protected_rows_checked"]:
        token = "| " + row["id"] + " |"
        old = next(x for x in old_tests if x.startswith(token))
        new = next(x for x in tests if x.startswith(token))
        require(old == new, "protected row changed: " + row["id"])
        require(hashlib.sha256(new.encode()).hexdigest() == row["row_sha256"], "protected row identity")
    for record in regression["unchanged_consumers"]:
        require((ROOT / record["path"]).read_bytes() == git("show", BASE + ":" + record["path"]), "read-only consumer changed")
    for path in ["deliverables/final-specification-set/creature-rpg/wp35-eggs-and-hatching.md", "deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md", "deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md", "CURRENT-DELIVERY.md"]:
        require((ROOT / path).read_bytes() == git("show", START + ":" + path), "protected delivery changed")

    for path in formal:
        added = git("diff", "--unified=0", START, "--", path).decode().splitlines()
        for line in added:
            if not line.startswith("+") or line.startswith("+++"):
                continue
            for target in re.findall(r"\]\(([^)]+)\)", line[1:]):
                if not re.match(r"[a-zA-Z]+:", target) and not target.startswith("#"):
                    require((ROOT / path).parent.joinpath(target.split("#")[0]).is_file(), "new link target: " + target)
    for path in HERE.glob("*.json"):
        json.loads(path.read_bytes())

    dispatch = json.loads((PACK / "dispatch-plan.json").read_text())
    batches = dispatch["plan"]["author_batches"]
    owners = [set(b["allowed_formal_write_paths"]) for b in batches]
    require(len(owners) == 5 and len(set.union(*owners)) == 28, "frozen ownership counts")
    require(all(not a & b for i, a in enumerate(owners) for b in owners[i + 1:]), "formal ownership collision")

    execution = read("execution.json")
    require(execution["new_behavior_execution"] == "NOT_EXECUTED_THIS_UPDATE", "new execution claim")
    require(all(execution[k] == 0 for k in ["EXECUTED_REFERENCE", "EXECUTED_MODEL", "EXECUTED_HOST_OR_DEMO"]), "new behavior execution")
    require(len(execution["historical_fourth_review"]["reference_probe_runs"]) == 4, "historical evidence retained")
    result = {
        "status": "PASS_TOOL_VALIDATION_ONLY",
        "evidence_level": "TOOL_VALIDATION",
        "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "tool": "exec_command / python3 validate_candidate.py",
        "python_version": sys.version,
        "exit_code": 0,
        "checks": ["all changed paths including untracked allowlisted", "exact 8 formal files and complete bytes/SHA256/blob", "15 complete criteria, source premises/refinements and anchored mapping", "26 unique unexecuted vectors", "38 existing control rows unchanged", "5 read-only consumers and protected delivery bytes retained", "new local links and JSON parse", "5 disjoint owners / 28 frozen formal paths", "no new execution / four historical isolated calls preserved"],
        "changed_paths": sorted(all_changed),
        "formal_diff_numstat": git("diff", "--numstat", START, "--", *formal).decode().strip(),
        "not_behavior_pass": True,
        "not_independent_review": True,
        "next_gate": "Parent-arranged independent candidate review; sole-registrar actual integration and acceptance pending",
    }
    (HERE / "validation-result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "formal_files": 8, "criteria": 15, "vectors": 26, "protected_rows": len(regression["protected_rows_checked"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
