#!/usr/bin/env python3
"""Document identities/ranges only. No source execution or behavior simulation."""
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from document_integrity import checked_range_sha256

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
PREFIX = OUT.relative_to(ROOT).as_posix() + "/"
REF = Path("/workspace/reference-b06-20261003-prepare")


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(name):
    return json.loads((OUT / name).read_text())


def blob(commit, path):
    return git("show", commit + ":" + path)


def identity(item, current=False):
    data = blob(item["commit"], item["path"])
    assert sha(data) == item["sha256"] and len(data) == item["bytes"]
    assert git("rev-parse", item["commit"] + ":" + item["path"]).decode().strip() == item["git_blob"]
    if current:
        assert (ROOT / item["path"]).read_bytes() == data


def rows(data):
    result = {}
    for number, line in enumerate(data.decode().splitlines(keepends=True), 1):
        match = re.match(r"^\| ([A-Z]+-\d+) \|", line)
        if match:
            assert match[1] not in result
            result[match[1]] = (number, line)
    return result


def section(data, prefix):
    lines = data.decode().splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.startswith(prefix))
    level = len(lines[start].split(" ")[0])
    end = next((j for j in range(start + 1, len(lines))
                if re.match(r"^#{1," + str(level) + r"} ", lines[j])), len(lines))
    return "".join(lines[start:end]).encode()


scope = load("scope-successor.json")
freeze = load("input-freeze.json")
base = scope["recovered_base_commit"]
assert git("branch", "--show-current").decode().strip() == scope["branch"]
git("merge-base", "--is-ancestor", base, "HEAD")
assert git("show", "-s", "--format=%P", base).decode().strip().split() == [
    scope["previous_author_evidence"], scope["accepted_dependency_commit"]]
changed = set(git("diff", "--name-only", base).decode().splitlines())
changed.update(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
assert {x for x in changed if not x.startswith(PREFIX)} == set(scope["new_delta_formal_paths"])
git("diff", "--check", base)
assert not scope["whole_B06_ready"] and not scope["integration_started"]

# Complete original/acceptance bindings, not just titles or old dispositions.
inputs = load("finding-inputs.json")
originals = {x["id"]: x for x in json.loads(blob(
    "93e10babe0b9c9ef8b3f5277754541b447beeeb4",
    "review/global-independent-review/2026-10-03-fd82a639/findings.json"))}
acceptances = json.loads(blob("41fffb540c6483f5296ea0d33b789b75180d27ed",
                             "review/remediation-20261003-prepare/finding-acceptance.json"))
assert {x["id"] for x in inputs["objects"]} == set(scope["complete_ten_ids"])
for item in inputs["objects"]:
    assert item["original_object"] == originals[item["id"]]
    assert item["approved_acceptance_object"] == acceptances[item["id"]]
    for field, expected in [("original_object", "original_sha256"),
                            ("approved_acceptance_object", "acceptance_sha256")]:
        normalized = json.dumps(item[field], ensure_ascii=False, sort_keys=True,
                                separators=(",", ":")).encode()
        assert sha(normalized) == item[expected]

# Historical author packets stay in the tree; reviews stay fixed at their original commits.
historical_files = historical_in_tree = 0
for directory in freeze["historical_B06_evidence_fixed_inputs"]:
    for item in directory["files"]:
        identity(item)
        historical_files += 1
        if (ROOT / item["path"]).exists():
            identity(item, current=True)
            historical_in_tree += 1
for item in freeze["all8_local_B06_formal_input_identities"]:
    assert blob(base, item["path"]) == blob(item["commit"], item["path"])
for item in freeze["all13_accepted_B03_formal_inputs"]:
    identity(item, current=True)
for item in freeze["additional_read_only_context_refrozen"]:
    identity(item, current=True)
for item in freeze["planned25_reads_refrozen"]:
    identity(item["old_accepted"])
    identity(item["new_accepted_actual"])
    identity(item["recovered_input"])
    if item["path"] not in scope["full_stage_formal_paths"] and item["read_source_kind"] != "external_fixed_original_review_object":
        identity(item["recovered_input"], current=True)
for item in freeze["planned5_writes_refrozen"] + freeze["three_original_formal_inputs_refrozen"]:
    identity(item)
for key in ["contract_identity", "contract_readme_identity", "full_B03_report_identity",
            "B03_interface_evidence_identity", "full_B06_second_round_report_identity"]:
    identity(freeze[key])

# Prior seven clause bytes/order and all25 rows are independent of shifted line numbers.
clause_guards = []
for item in freeze["all15_preserved_clause_guards"]:
    data = (ROOT / item["path"]).read_bytes()
    literal = item["literal_text"].encode()
    assert sha(literal) == item["sha256"] and data.count(literal) == 1
    offset = data.index(literal)
    clause_guards.append({"path": item["path"], "current_start_line": data[:offset].count(b"\n") + 1,
                          "sha256": item["sha256"], "bytes_unchanged": True})
prior_rows = []
for item in freeze["all25_preserved_static_rows"]:
    number, line = rows((ROOT / item["path"]).read_bytes())[item["test_id"]]
    assert sha(line.encode()) == item["sha256"]
    prior_rows.append(dict(item, successor_line=number, bytes_unchanged=True))
for item in freeze["five_local_whole_file_guards"]:
    identity(item, current=True)
for item in freeze["protected_upstream_version_successor"]:
    identity(item["accepted_successor"], current=True)
preserved_sections = 0
for item in freeze["protected_sections_successor"]:
    if item["successor_rule"] != "PRESERVE_EXACT_BYTES":
        continue
    guard = item["historical_frozen_guard"]
    assert sha(section((ROOT / guard["path"]).read_bytes(), guard["heading"])) == guard["sha256"]
    preserved_sections += 1

# Exact allowed delta: two one-line replacements plus named insertions; no other WP24 edits.
ledger = load("formal-edit-ledger.json")["WP24_clause_edits"]
for path in scope["new_delta_formal_paths"][:2]:
    old = blob(base, path).decode().splitlines(keepends=True)
    new = (ROOT / path).read_text().splitlines(keepends=True)
    expected = [x for x in ledger if x["path"] == path]
    actual = []
    limits = ({98, 195}, {160, 238}) if path.startswith("deliverables/") else ({95, 184}, {153})
    for kind, i, j, m, n in difflib.SequenceMatcher(a=old, b=new, autojunk=False).get_opcodes():
        if kind == "equal":
            continue
        assert ((kind == "replace" and j == i + 1 and i + 1 in limits[0]) or
                (kind == "insert" and i in limits[1]))
        actual.append({"path": path, "kind": kind,
                       "parent_range": None if kind == "insert" else [i + 1, j],
                       "parent_anchor_after_line": i if kind == "insert" else None,
                       "new_range": [m + 1, n],
                       "before_sha256": sha("".join(old[i:j]).encode()),
                       "after_sha256": sha("".join(new[m:n]).encode())})
    assert actual == [{k: v for k, v in x.items() if k != "allowed_named_clause"} for x in expected]
    assert len(actual) == (4 if path.startswith("deliverables/") else 3)
    for heading in ["### 5.1", "### 5.2", "### 5.3", "### 6.1"]:
        assert section((ROOT / path).read_bytes(), heading) == section(blob(base, path), heading)

# Reconstruct entire old catalog from the new one, not just assigned test rows.
catalog = scope["new_delta_formal_paths"][2]
old, new = blob(base, catalog), (ROOT / catalog).read_bytes()
oldrows, newrows = rows(old), rows(new)
added = {f"PT-{n:02d}" for n in range(35, 70)}
assert set(newrows) - set(oldrows) == added and not set(oldrows) - set(newrows)
assert all(oldrows[key][1] == newrows[key][1] for key in oldrows)
normalized = new.decode()
for key in added:
    normalized = normalized.replace(newrows[key][1], "")
assert normalized.replace("（PT-01～PT-69）", "（PT-01～PT-34）").encode() == old
vectors = load("new-static-vectors.json")
assert len(vectors["cases"]) == 35
for case in vectors["cases"]:
    number, line = newrows[case["test_id"]]
    assert number == case["candidate_line"] and line == case["row_text"]
    assert sha(line.encode()) == case["row_sha256"] and line.count("|") == 4
responses = load("finding-responses.json")["all_ten_responses"]
assert {x["id"] for x in responses} == set(scope["complete_ten_ids"])
assert sum(len(x["test_cases"]) for x in responses) == 60
for item in responses:
    assert item["new_independent_verdict"] is None and not item["close"]
    for case in item["test_cases"]:
        number, line = rows((ROOT / case["path"]).read_bytes())[case["test_id"]]
        assert number == case["candidate_line"] and sha(line.encode()) == case["row_sha256"]

# Bounded reference byte/range metadata only. The raw source is never evaluated.
reading = load("source-reading-log.json")
assert git("rev-parse", "HEAD", cwd=REF).decode().strip() == reading["reference_commit"]
assert git("rev-parse", "HEAD^{tree}", cwd=REF).decode().strip() == reading["reference_tree"]
assert not git("status", "--porcelain=v1", cwd=REF)
span_count = 0
for item in reading["fresh_readings"] + reading["inherited_corrected_readings"]:
    data = (REF / item["path"]).read_bytes()
    assert data == git("show", reading["reference_commit"] + ":" + item["path"], cwd=REF)
    assert sha(data) == item["sha256"] and len(data.splitlines(keepends=True)) == item["actual_line_count"]
    for span in item["read_ranges"]:
        assert checked_range_sha256(data, span["start"], span["end"]) == span["range_sha256"]
        span_count += 1
trainer = next(x for x in reading["inherited_corrected_readings"] if x["reading_id"] == "B06-SR-03")
data = (REF / trainer["path"]).read_bytes()
assert trainer["actual_line_count"] == 124 and trainer["read_ranges"][0]["end"] == 124
assert checked_range_sha256(data, 1, 124) == sha(data)
assert checked_range_sha256(data, 124, 124) == sha(data.splitlines(keepends=True)[123])
invalid = [(trainer["path"], a, b) for a, b in [(1, 135), (125, 125), (0, 124), (124, 1), (1, 0)]]
invalid += [(x["path"], *x["requested_display_range"]) for x in reading["pre_receipt_bounds_corrections"]]
rejected = []
for path, start, end in invalid:
    calls = []

    def prohibited_hasher(chunk):
        calls.append(True)
        raise AssertionError("invalid range reached hashing")

    try:
        checked_range_sha256((REF / path).read_bytes(), start, end, hash_bytes=prohibited_hasher)
    except ValueError:
        assert not calls
        rejected.append({"path": path, "range": [start, end], "hash_calls": 0, "rejected_before_hash": True})
    else:
        raise AssertionError((path, start, end))
for item in load("patch-identities.json")["patches"]:
    actual = git("diff", "--binary", "--unified=0", item["base_commit"], "--", *item["selected_formal_paths"])
    assert actual == (ROOT / item["path"]).read_bytes() and sha(actual) == item["sha256"]

result = {"result": "AUTHOR_STAGE2_DOCUMENT_CHECKS_COMPLETED_NO_INDEPENDENT_VERDICT",
          "recovered_base": base, "new_delta_formal_path_count": 3, "full_B06_formal_path_count": 8,
          "all_ten_original_and_acceptance_objects_exact": True,
          "historical_fixed_file_checks": historical_files, "historical_in_tree_bytes_unchanged": historical_in_tree,
          "accepted_B03_formal_files_unchanged": 13, "planned25_input_identities_refrozen": True,
          "upstream_planned_read_drift_count": 1, "original_review_inputs_remain_external_fixed_objects": 2,
          "all15_prior_clause_guards": clause_guards, "all25_prior_row_guards": prior_rows,
          "five_local_whole_files_unchanged": 5, "protected_upstream_version_files_unchanged": 17,
          "protected_sections_byte_preserved": preserved_sections, "scoped_sections_released": ["WP24 §4.1", "WP24 §6.4"],
          "WP24_5_1_5_2_5_3_6_1_sections_exact": True, "all_existing_catalog_rows_and_text_preserved": True,
          "new_static_PT_rows": 35, "full_ten_static_rows": 60, "PT_catalog_total": 69,
          "reference_source_spans_validated_before_hash": span_count,
          "document_range_guard_valid_cases": 2, "document_range_guard_invalid_cases": rejected,
          "document_only_range_fixture_checks_executed": 9, "behavioral_vectors_executed": 0,
          "new_independent_review_verdict": None, "actual_integration_review_verdict": None,
          "whole_B06_ready": False, "public_registry_writes": 0, "finding_closures": 0,
          "runtime_observations": 0, "proven_demo_event_chains": 0, "reference_execution": 0,
          "effective_configuration": "UNVERIFIED"}
(OUT / "static-validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print("Document checks completed: all ten bindings, 15 clauses/25 old rows preserved, 35 PT additions, 40 bounded source spans; no independent verdict or behavior execution.")
