#!/usr/bin/env python3
"""Reviewer-owned Git/hash/text bookkeeping; no reference/behavior code runs."""
import collections
import gzip
import hashlib
import json
import pathlib
import re
import subprocess

OUT = pathlib.Path(__file__).resolve().parent
ROOT = OUT.parents[5]
BASE = "1e6b11a47370f1c7c4659a32443fc1afda597bac"
C1 = "47f7514765f8569ae9172bb06a2cd615e2b83b8a"
C2 = "af39efbf32549be964cb083bd49bed6d1d5c0d2a"
GLOBAL = "93e10babe0b9c9ef8b3f5277754541b447beeeb4"
PLAN = "41fffb540c6483f5296ea0d33b789b75180d27ed"
REF = pathlib.Path("/tmp/r-b14-b02-reference")
REF_SHA = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
REF_TREE = "7589c800b61ba13a13040ed0d686979b80a84fd0"

def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

def show(rev, path):
    return git("show", rev + ":" + path)

def identity(rev, path):
    data = show(rev, path)
    return {"commit": rev, "path": path, "git_blob": git("rev-parse", rev + ":" + path).decode().strip(), "sha256": sha(data), "bytes": len(data)}

def canon(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()

def equals_identity(actual, recorded):
    return all(actual[k] == recorded[k] for k in ("git_blob", "sha256", "bytes"))

assert git("rev-parse", "HEAD").decode().strip() == C2
git("merge-base", "--is-ancestor", BASE, C2)
git("merge-base", "--is-ancestor", C1, C2)
assert git("rev-parse", "HEAD", cwd=REF).decode().strip() == REF_SHA
assert git("rev-parse", "HEAD^{tree}", cwd=REF).decode().strip() == REF_TREE
assert git("status", "--porcelain", cwd=REF) == b""
assert git("remote", "get-url", "origin", cwd=REF).decode().strip() == "https://github.com/Maruno17/pokemon-essentials.git"

contract_path = "review/remediation/20261003-prepare/batches/B09/acceptance-stage-1/B14-downstream-contract.json"
contract = json.loads(show(BASE, contract_path))
reads = []
for r in contract["planned_reads"]:
    expected = r["accepted_current_input"]
    input_rev = expected.get("commit", BASE)
    current_rev = input_rev if "commit" in expected else C2
    actual = identity(input_rev, r["path"])
    assert equals_identity(actual, expected), r["path"]
    reads.append({"planned_index": r["planned_index"], "baseline": actual, "candidate2_or_fixed_historical": identity(current_rev, r["path"]), "changed": show(input_rev, r["path"]) != show(current_rev, r["path"]), "fixed_historical": "commit" in expected})
assert len(reads) == 72
for r in contract["allowed_write_input_identities"]:
    assert equals_identity(identity(BASE, r["path"]), r)

diffs = []
for old, name in [(BASE, "full-predecessor-candidate2.patch.gz"), (C1, "full-candidate1-candidate2.patch.gz")]:
    data = git("diff", "--no-ext-diff", "--binary", "--full-index", old, C2)
    (OUT / name).write_bytes(gzip.compress(data, mtime=0))
    changes = []
    for line in git("diff", "--name-status", old, C2).decode().splitlines():
        status, p = line.split("\t")
        changes.append({"status": status, "path": p, "before": identity(old, p) if status != "A" else None, "after": identity(C2, p)})
    diffs.append({"before": old, "after": C2, "artifact": name, "uncompressed_sha256": sha(data), "uncompressed_bytes": len(data), "compressed_sha256": sha((OUT / name).read_bytes()), "changes": changes})
assert len(diffs[0]["changes"]) == 46
assert len(diffs[1]["changes"]) == 22
formal = [x for x in diffs[0]["changes"] if x["path"].startswith(("specs/", "deliverables/"))]
assert len(formal) == 12
assert len([x for x in diffs[1]["changes"] if x["path"].startswith(("specs/", "deliverables/"))]) == 8
assert all(x["status"] == "M" for x in formal)
assert all(x["path"].startswith("review/remediation/20261003-prepare/batches/B14/") for x in diffs[0]["changes"] if x not in formal)

# Full-byte preservation outside owned sections, plus old-row order/multiplicity.
catalogs = []
for p, headings, families in [
    ("deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md", ("## I.", "## J."), ("WT", "FS")),
    ("deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md", ("## BP：", "## FP："), ("BP", "FP")),
]:
    def outside(data):
        keep = True
        result = []
        for line in data.splitlines(keepends=True):
            if line.startswith(b"## "):
                keep = not any(line.decode().startswith(h) for h in headings)
            if keep:
                result.append(line)
        return b"".join(result)
    def rows(data):
        return [(m.group(1).decode(), line) for line in data.splitlines(keepends=True) if (m := re.match(rb"\| ([A-Za-z0-9][A-Za-z0-9_-]*[0-9]) \|", line))]
    a, b = show(BASE, p), show(C2, p)
    ra, rb = rows(a), rows(b)
    old_ids, new_ids = [x[0] for x in ra], [x[0] for x in rb]
    count_a, count_b = collections.Counter(old_ids), collections.Counter(new_ids)
    assert all(count_b[k] == v for k, v in count_a.items())
    assert [k for k in new_ids if k in count_a] == old_ids
    assert outside(a) == outside(b), p
    changed = [k for k, line in ra if [l for key, l in rb if key == k] != [line]]
    assert all(any(k.startswith(f) for f in families) for k in changed)
    preserved = [k for k, line in ra if not any(k.startswith(f) for f in families)]
    catalogs.append({"path": p, "baseline": identity(BASE, p), "candidate2": identity(C2, p), "outside_owned_sections_equal": True, "outside_owned_sections_sha256": sha(outside(a)), "old_row_count": len(ra), "current_row_count": len(rb), "old_id_order_and_multiplicity_preserved": True, "changed_old_rows": changed, "added_rows": [k for k in new_ids if k not in count_a], "other_owner_rows_byte_preserved": preserved})
    c1_rows = rows(show(C1, p))
    c1_ids = [k for k, line in c1_rows]
    assert [k for k in new_ids if k in c1_ids] == c1_ids
    assert all(count_b[k] == v for k, v in collections.Counter(c1_ids).items())
    c1_changed = [k for k, line in c1_rows if [l for key, l in rb if key == k] != [line]]
    assert c1_changed == (["WT28"] if "engine-overworld" in p else ["BP18"])
    catalogs[-1]["candidate1_to_candidate2"] = {"old_rows": len(c1_rows), "current_rows": len(rb), "old_order_multiplicity_preserved": True, "changed_old_rows": c1_changed, "added_rows": [k for k in new_ids if k not in c1_ids]}
kernel_catalog = "deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md"
engine = show(C2, kernel_catalog)
engine_base = show(BASE, kernel_catalog)
for n in range(1, 22):
    pat = rb"(?m)^\| EP" + f"{n:02}".encode() + rb" \|.*$"
    assert re.findall(pat, engine) == re.findall(pat, engine_base) and re.findall(pat, engine)
for name in ("BP07", "BP13", "BP14"):
    pat = rb"(?m)^\| " + name.encode() + rb" \|.*$"
    assert re.findall(pat, show(BASE, catalogs[1]["path"])) == re.findall(pat, show(C2, catalogs[1]["path"]))

prior = json.loads(show(BASE, "review/remediation/20261003-prepare/batches/B02/integration-review-1/finding-dispositions.json"))
b02paths = json.loads(show(BASE, "review/remediation/20261003-prepare/batches/B02/author-v2/candidate-manifest.json"))["formal_files"]
protected = []
for r in b02paths:
    p = r["path"]
    assert show(BASE, p) == show(C2, p), p
    protected.append(identity(C2, p))
assert len(protected) == 13
original_path = "review/global-independent-review/2026-10-03-fd82a639/findings.json"
acceptance_path = "review/remediation-20261003-prepare/finding-acceptance.json"
original = {x["id"]: x for x in json.loads(show(GLOBAL, original_path))}
acceptance = json.loads(show(PLAN, acceptance_path))
controls = []
for d in prior["dispositions"]:
    k = d["id"]
    assert sha(canon(original[k])) == d["original_object_canonical_json_sha256"], k
    assert sha(canon(acceptance[k])) == d["acceptance_object_canonical_json_sha256"], k
    controls.append({"id": k, "original": original[k], "approved_acceptance": acceptance[k], "prior_exact_B02_actual_disposition": d})
assert len(controls) == 12
shared = next(x for x in contract["contribution_controls"] if x["id"] == "GIR-FD82-C003")
assert sha(canon(original[shared["id"]])) == shared["whole_original_object_sha256"]
assert sha(canon(acceptance[shared["id"]])) == shared["whole_acceptance_object_sha256"]
for k, v in shared["complete_current_control_fields"].items():
    assert original[shared["id"]].get(k) == v, k
for k, v in shared["complete_minimum_acceptance_fields"].items():
    assert acceptance[shared["id"]].get(k) == v, k
(OUT / "complete-controls.json.gz").write_bytes(gzip.compress(canon({"B02_all12": controls, "B14_shared_C003_complete_control": shared}), mtime=0))
management = []
for r in contract["current_management_reads"]:
    assert equals_identity(identity(BASE, r["path"]), r)
    assert show(BASE, r["path"]) == show(C2, r["path"])
    management.append(identity(C2, r["path"]))

# Post-first-judgment author comparison: identities/dry patch checks are not approval.
author_root = "review/remediation/20261003-prepare/batches/B14/candidate-2/"
revised = json.loads(show(C2, author_root + "revised-identities.json"))
assert len(revised["documents"]) == 12
for r in revised["documents"]:
    assert equals_identity(identity(BASE, r["path"]), r["accepted_B09_before"])
    assert equals_identity(identity(C1, r["path"]), r["candidate1_before"])
    assert equals_identity(identity(C2, r["path"]), r["after"])
    assert r["changed_in_candidate2"] == (show(C1, r["path"]) != show(C2, r["path"]))
bounded = json.loads(show(C2, author_root + "bounded-amendment-1.json"))
application = json.loads(show(C2, author_root + "amendment-application.json"))
assert equals_identity(identity(C2, author_root + "bounded-amendment-1.json"), application["before_application_record"])
patches = []
for r in bounded["documents"]:
    assert equals_identity(identity(C1, r["path"]), r["before"])
    assert equals_identity(identity(C2, r["path"]), r["intended_after"])
    patch_path = author_root + r["patch"]
    assert sha(show(C2, patch_path)) == r["patch_sha256"]
    git("apply", "--reverse", "--check", patch_path)
    actual = next(x for x in application["documents"] if x["path"] == r["path"])
    assert equals_identity(identity(C2, r["path"]), actual["actual_after"])
    assert actual["patch_sha256"] == r["patch_sha256"]
    patches.append({"patch": identity(C2, patch_path), "before": identity(C1, r["path"]), "after": identity(C2, r["path"]), "reverse_dry_check": "PASS; no mutation"})
fly_patch = author_root + revised["original_FLY_amendment_patch"]
assert sha(show(C2, fly_patch)) == revised["original_FLY_patch_sha256"]
git("apply", "--reverse", "--check", fly_patch)
patches.append({"patch": identity(C2, fly_patch), "reverse_dry_check": "PASS; no mutation"})
fix = json.loads(show(C2, author_root + "fix-response.json"))
review_inputs = []
for r in fix["review_inputs"]:
    actual = identity(r["commit"], r["path"])
    assert equals_identity(actual, r)
    review_inputs.append(actual)
for suffix in ("author-stage-1", "candidate-1", "scope-proposal-1"):
    assert git("diff", "--name-only", C1, C2, "--", "review/remediation/20261003-prepare/batches/B14/" + suffix) == b""
for p in ("specs/overworld/wp60-fishing.md", "deliverables/final-specification-set/engine-overworld/wp60-fishing.md", "specs/pokemon-rules/wp61-field-passive-effects-and-blackout.md", "deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md"):
    assert show(C1, p) == show(C2, p)
def except_section(data, start, end):
    before, rest = data.split(start, 1)
    return before + end + rest.split(end, 1)[1]
for p in ("specs/pokemon-rules/wp60-berry-plants.md", "deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md"):
    assert except_section(show(C1, p), b"### 5.2", b"### 5.3") == except_section(show(C2, p), b"### 5.2", b"### 5.3")
for p in ("specs/overworld/wp16-world-rendering-and-visual-transitions.md", "deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md"):
    diff = git("diff", "--unified=0", C1, C2, "--", p).decode().splitlines()
    minus = [s[1:] for s in diff if s.startswith("-") and not s.startswith("---")]
    plus = [s[1:] for s in diff if s.startswith("+") and not s.startswith("+++")]
    assert len(minus) == len(plus) == 1
    assert minus[0].startswith("Rain类别") and plus[0].startswith("Rain类别")
git("diff", "--check", BASE, C2, "--", "specs", "deliverables/final-specification-set")
dump("author-comparison.json", {"phase": "AFTER_REVIEWER_FIRST_JUDGMENT", "author_self_check_is_acceptance": False, "independent_behavior_judgment_unchanged": "PASS_SCOPED_B02_AFFECTED_INTERFACE_ONLY", "all12_before_candidate1_after_document_identities_matched": True, "five_bounded_proposed_applied_identities_and_hashes_matched": True, "six_patch_dry_reverse_checks": patches, "three_foreign_candidate1_reports_and_three_findings_identity_checks": review_inputs, "four_unmodified_formal_paths_against_candidate1": True, "prior_B14_evidence_not_rewritten": True, "berry_except_5_2_byte_identical_against_candidate1": True, "WP16_one_sentence_each_all_other_bytes_unchanged": True, "cumulative_formal_diff_check": "PASS", "author_traceability_is_public_registration": False, "foreign_findings_not_reissued_as_new_B02_defects": ["B14-AFFECTED-B03-001", "R-B14-1-001", "B14-B04-R1-01"], "counting_correction": "Initial reviewer regex excluded28 hyphenated B04-R IDs. Corrected full counts independently:480 accepted predecessor,503 candidate1,505 candidate2; outside-owned-section exact-byte preservation passed both times."})

dump("diff-manifest.json", {"scope": "Complete unfiltered Git diffs; archive reading is text bookkeeping, not source/behavior execution", "diffs": diffs, "formal_paths": formal})
dump("input-identities.json", {"base": BASE, "candidate1": C1, "candidate2": C2, "candidate_tree": git("rev-parse", C2 + "^{tree}").decode().strip(), "contract": identity(BASE, contract_path), "planned72": reads, "B02_formal13_byte_unchanged_against_accepted_predecessor": protected, "management6_byte_unchanged": management, "fixed_original": identity(GLOBAL, original_path), "fixed_acceptance": identity(PLAN, acceptance_path)})
dump("bookkeeping.json", {"reviewer": "R-B02", "scope": "B14 candidate2 affected B02 interface only", "all72_read_identities_matched": True, "allowed6_write_base_identities_matched": True, "full_difference_counts": {"base_to_candidate2": 46, "candidate1_to_candidate2": 22, "cumulative_formal": 12, "incremental_formal": 8}, "catalogs": catalogs, "EP01_to_EP21_byte_preserved": True, "BP07_BP13_BP14_byte_preserved": True, "B02_formal13_byte_preserved": True, "original_B02_12_full_objects_and_acceptance_hashes_match": True, "shared_C003_current_fields_and_4_roots_8_extensions_match": True, "current_management6_byte_preserved": True, "reference": {"path_outside_main_git": str(REF), "sha": REF_SHA, "tree": REF_TREE, "clean": True}, "canonical_required_OPEN": 229, "canonical_CLOSED": 0, "reference_execution": 0, "runtime_observations": 0, "demo_chains": 0, "static_behavior_vectors_executed": 0, "child_tasks": 0})
print(json.dumps({"all_checks_passed": True, "catalogs": [{k: v for k, v in x.items() if k in ["path", "old_row_count", "current_row_count", "changed_old_rows", "added_rows"]} for x in catalogs], "formal_paths": len(formal), "complete_B02_controls": len(controls)}, ensure_ascii=False))
