"""Required private artifact/scope/hash and patch dry checks, no behavior tests."""
import hashlib
import json
import subprocess
from pathlib import Path
from prepare import BASE, OUT, FILES, CAT, identity, package, blob, dump


def main():
    inputs = json.loads((OUT / "input-verification.json").read_text())
    analysis = json.loads((OUT / "contribution-analysis.json").read_text())
    proposals = json.loads((OUT / "original-sync-proposals.json").read_text())
    plan = json.loads((OUT / "dependency-and-refreeze-plan.json").read_text())
    locks = json.loads((OUT / "catalog-preservation.json").read_text())
    ctrls = package("original-and-acceptance-controls.json")["controls"]
    assert inputs["formal_input"] == BASE and inputs["whole_control_equality_checks"] == 48
    assert len(inputs["planned_reads"]) == 74 and len(inputs["formal_snapshot_checks"]) == 6
    assert len(inputs["original_and_management_identity_checks"]) == 10
    assert len(analysis["contributions"]) == 24
    assert sum(r["primary"] for r in analysis["contributions"]) == 20
    assert analysis["formal_writes"] == 0 and analysis["independent_reviews"] == 0
    assert analysis["record_order_matches_dispatch"]
    for c, r in zip(ctrls, analysis["contributions"]):
        assert r["id"] == c["id"] and r["qualified_current_control"] == c["complete_current_control_fields"]
        assert r["source_and_caller_reading"] and r["static_minimum_counterexample_design"] and r["adjacent_reverse_design"]
        assert not r["designs_executed"] and not r["formal_remediation_claim"]
    logs = json.loads((OUT / "source-reading-log.json").read_text())["reading"]
    for log in logs:
        data = blob(log["commit"], log["path"], log["commit"] != BASE)
        ls = data.splitlines(keepends=True)
        assert hashlib.sha256(data).hexdigest() == log["sha256"]
        for r in log["ranges"]:
            lo, hi = map(int, r["lines"].split('-'))
            assert 1 <= lo <= hi <= len(ls), (log["path"], r["lines"])
            assert hashlib.sha256(b''.join(ls[lo-1:hi])).hexdigest() == r["sha256"]
    dry_checks = []
    for proposal in proposals["proposals"]:
        original = blob(BASE, proposal["path"]).decode()
        ls = original.splitlines(keepends=True)
        for clause in proposal["clauses"]:
            assert ls[clause["original_line"]-1].rstrip('\n') == clause["before"]
            ls[clause["original_line"]-1] = clause["proposed_after"] + '\n'
        after = ''.join(ls).encode()
        assert hashlib.sha256(after).hexdigest() == proposal["proposed_after_file_sha256"]
        patch = OUT / proposal["fullpatch"]
        assert hashlib.sha256(patch.read_bytes()).hexdigest() == proposal["fullpatch_sha256"]
        subprocess.run(["git", "apply", "--check", "--unidiff-zero", str(patch)], check=True)
        dry_checks.append(proposal["fullpatch"])
    for combined in proposals["combined_patches_apply_each_file_once_on_exact_input_only"]:
        patch = OUT / combined["fullpatch"]
        assert hashlib.sha256(patch.read_bytes()).hexdigest() == combined["sha256"]
        subprocess.run(["git", "apply", "--check", "--unidiff-zero", str(patch)], check=True)
        assert not combined["applied"]
        dry_checks.append(combined["fullpatch"])
    assert len(plan["B12_gate"]["forward_five_B12_writes_B16_reads"]) == 5
    assert len(plan["B12_gate"]["reverse_two_B16_future_writes_B12_reads"]) == 2
    assert len(plan["accepted_interface_navigation"]) == 11
    assert [r["id"] for r in plan["B15_dependency_records"]] == ["GIR-FD82-A055", "GIR-FD82-A056", "GIR-FD82-C122"]
    # Real local source/docs stay at formal input; --check never applies patches.
    for item in inputs["formal_snapshot_checks"] + inputs["original_and_management_identity_checks"]:
        path = item["path"]
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == item["sha256"]
    assert locks["catalog"] == identity(BASE, CAT)
    prefix = OUT.relative_to(Path.cwd()).as_posix() + '/'
    changed = subprocess.check_output(["git", "diff", "--name-only", BASE]).decode().splitlines()
    untracked = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"]).decode().splitlines()
    assert all(p.startswith(prefix) for p in changed + untracked), (changed, untracked)
    assert not list(OUT.rglob('__pycache__'))
    subprocess.run(["git", "diff", "--check", BASE], check=True)
    for path in OUT.rglob('*.json'):
        json.loads(path.read_text())
    result = {
        "status": "AUTHOR_PRIVATE_ARTIFACT_SELF_CHECK_ONLY",
        "formal_input": BASE, "formal_writes": 0, "contributions": 24, "primary": 20,
        "input_identity_checks": 74, "future_formal_snapshots": 6,
        "original_and_management_identities": 10, "whole_control_equalities": 48,
        "source_range_hashes_and_bounds": True,
        "exact_original_before_and_proposed_after_digests": True,
        "private_patch_git_apply_check_only": dry_checks,
        "originals_unchanged": True, "formal_snapshots_unchanged": True,
        "all_repo_changes_within_author_preparation_directory": True,
        "json_parse_and_git_diff_check": True,
        "independent_verdict": None, "candidate_or_acceptance": False,
        "behavior_vectors_executed": 0,
        "remaining_gate": "B12 exact published C followed by parent latest accepted refreeze before full B16 author. Original precise amendments require sole registrar confirmation. All future candidate/actual independent Ultra/affected/G/C gates remain.",
        "self_commit_SHA": "External final response after ordinary push/readback; no recursive self hash or extra purity checkpoint.",
    }
    dump("verification.json", result)
    print(f"24/20,74+6+10 identities,48 object equalities; {len(dry_checks)} patches dry-check; scope/formal/original unchanged. No behavior execution or independent PASS.")


if __name__ == '__main__':
    main()
