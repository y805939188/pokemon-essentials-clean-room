#!/usr/bin/env python3
"""Check document identity, scoped edits and frozen rows only; never execute reference."""
import difflib
import hashlib
import json
import re
import subprocess
from pathlib import Path

STAGE = Path(__file__).resolve().parent
ROOT = STAGE.parents[5]
PREFIX = STAGE.relative_to(ROOT).as_posix() + "/"
REF_ROOT = Path("/workspace/reference-b06-20261003-prepare")


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(name):
    return json.loads((STAGE / name).read_text())


def canonical(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":")).encode())


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def section(text, heading):
    lines = text.splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.startswith(heading))
    level = len(lines[start].split(" ")[0])
    end = next((i for i in range(start + 1, len(lines))
                if re.match(r"^#{1," + str(level) + r"} ", lines[i])), len(lines))
    return "".join(lines[start:end]).encode()


def rows(text):
    result = {}
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\| ([A-Z]+-\d+) \|", line)
        if match:
            key = match[1]
            assert key not in result, ("duplicate test ID", key)
            result[key] = line
    return result


scope = read_json("scope-successor.json")
freeze = read_json("input-freeze.json")
preservation = read_json("preservation-freeze.json")
inputs = read_json("finding-inputs.json")
reading = read_json("source-reading-log.json")
responses = read_json("finding-responses.json")
proposals = read_json("registrar-proposals.json")
resume = read_json("resume-checkpoint.json")
patches = read_json("patch-identities.json")
BASE = scope["base_commit"]
formal = scope["authorization_constraints"]["formal_write_paths"]
assert len(formal) == 8
assert scope["branch"] == git("branch", "--show-current").decode().strip()
git("merge-base", "--is-ancestor", BASE, "HEAD")
git("diff", "--check", BASE)

changed = set(git("diff", "--name-only", BASE).decode().splitlines())
changed.update(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
assert {p for p in changed if not p.startswith(PREFIX)} == set(formal)
assert not scope["authorization_constraints"]["full_B06_ready"]
assert not responses["whole_B06_ready"] and not resume["full_B06_ready"]
assert proposals["public_writer"] == "A-REG"
assert proposals["public_writes_by_author"] == proposals["closures_by_author"] == 0
for item in patches["patches"]:
    actual = git("diff", "--binary", "--unified=0", BASE, "--", *item["selected_formal_paths"])
    assert actual == (ROOT / item["path"]).read_bytes()
    assert sha(actual) == item["sha256"]

# Whole-file and section guards cover B03 read/write intersections and B05/other batches.
protected = []
for identity in preservation["protected_whole_files"]:
    actual = (ROOT / identity["path"]).read_bytes()
    assert sha(actual) == identity["sha256"], identity["path"]
    protected.append({"path": identity["path"], "sha256": sha(actual)})
for identity in preservation["protected_sections"]:
    actual = section((ROOT / identity["path"]).read_text(), identity["heading_prefix"])
    assert sha(actual) == identity["sha256"], identity
for identity in preservation["protected_test_rows"]:
    row = rows((ROOT / identity["path"]).read_text())[identity["test_id"]]
    assert sha(row.encode()) == identity["sha256"], identity

# Every edited body opcode must replace exactly a named frozen baseline line.
allowed_lines = {
    formal[0]: {77, 207, 216, 237},
    formal[1]: {79, 89, 185},
    formal[2]: {102, 158},
    formal[5]: {76, 203},
    formal[6]: {77, 85, 211},
    formal[7]: {98},
}
body_edits = []
for path, permitted in allowed_lines.items():
    old = git("show", BASE + ":" + path).decode().splitlines(keepends=True)
    new = (ROOT / path).read_text().splitlines(keepends=True)
    seen = set()
    for kind, i, j, m, n in difflib.SequenceMatcher(a=old, b=new, autojunk=False).get_opcodes():
        if kind == "equal":
            continue
        assert kind == "replace" and j == i + 1 and i + 1 in permitted, (path, kind, i, j)
        seen.add(i + 1)
        body_edits.append({"path": path, "base_line": i + 1,
                           "new_lines": [m + 1, n], "old_sha256": sha(old[i].encode()),
                           "new_clause_sha256": sha("".join(new[m:n]).encode())})
    assert seen == permitted, (path, seen, permitted)

# A038 changes only Give in the pre-existing command list; other entries are byte-identical.
for path in (formal[2], formal[7]):
    old = git("show", BASE + ":" + path).decode()
    new = (ROOT / path).read_text()
    old_command = next(line for line in old.splitlines() if line.startswith("- 背包界面命令按物品动态生成"))
    new_command = next(line for line in new.splitlines() if line.startswith("- 背包界面命令按物品动态生成"))
    assert re.sub(r"给予（[^）]*）", "GIVE_GUARD", old_command) == re.sub(r"给予（[^）]*）", "GIVE_GUARD", new_command)

# Normalize only appended stage rows, owned range headers and the two fixed existing rows.
catalog_results = []
for path, groups, amended in [
    (formal[3], {"PT": (28, 34), "PS": (28, 38), "AQ": (35, 36)}, {"PS-11", "AQ-04"}),
    (formal[4], {"BG": (29, 31)}, set()),
]:
    old = git("show", BASE + ":" + path).decode()
    new = (ROOT / path).read_text()
    old_rows, new_rows = rows(old), rows(new)
    appended = {f"{group}-{i:02d}" for group, (prior, current) in groups.items()
                for i in range(prior + 1, current + 1)}
    assert set(new_rows) - set(old_rows) == appended
    assert set(old_rows) - set(new_rows) == set()
    assert {key for key in old_rows if old_rows[key] != new_rows[key]} == amended
    normalized = new
    for key in appended:
        normalized = normalized.replace(new_rows[key], "")
    for key in amended:
        normalized = normalized.replace(new_rows[key], old_rows[key])
    for group, (prior, current) in groups.items():
        normalized = normalized.replace(f"（{group}-01～{group}-{current:02d}）",
                                        f"（{group}-01～{group}-{prior:02d}）")
        expected_ids = {f"{group}-{i:02d}" for i in range(1, current + 1)}
        assert {key for key in new_rows if key.startswith(group + "-")} == expected_ids
    assert normalized == old, ("unowned catalog change", path)
    assert all(len(line.strip().strip("|").split("|")) == 3 for line in new_rows.values())
    catalog_results.append({"path": path, "appended_ids": sorted(appended),
                            "amended_existing_ids": sorted(amended),
                            "all_other_rows_and_text_byte_preserved": True})

# Recheck complete immutable canonical objects, precedence and their exact hashes.
report = json.loads(git("show", inputs["objects"][0]["original_report_commit"] +
                       ":review/global-independent-review/2026-10-03-fd82a639/findings.json"))
acceptance = json.loads(git("show", scope["approved_plan_commit"] +
                           ":review/remediation-20261003-prepare/finding-acceptance.json"))
for item in inputs["objects"]:
    for document, field, hash_field in [
        (report, "original_object", "original_sha256"),
        (acceptance, "approved_acceptance_object", "acceptance_sha256"),
    ]:
        matches = [value for value in walk(document)
                   if value.get("id") == item["id"] and canonical(value) == item[hash_field]]
        assert len(matches) == 1 and matches[0] == item[field]
for identity in freeze["B05_handoff_identity_checks"] + freeze["plan_controls"] + freeze["formal_baseline"]:
    assert sha(git("show", identity["commit"] + ":" + identity["path"])) == identity["sha256"]
for identity in freeze["plan_controls"]:
    assert sha((ROOT / identity["path"]).read_bytes()) == identity["sha256"]

# Case and clause receipts describe already-written independent behavior prose only.
assigned = scope["authorization_constraints"]["stage_ids"]
assert {r["id"] for r in responses["responses"]} == set(assigned)
case_count = 0
for response in responses["responses"]:
    assert response["independent_review_verdict"] is None
    assert response["actual_integration_review_verdict"] is None
    assert not response["closure_requested"]
    suffix = response["id"].removeprefix("GIR-FD82-")
    assert [case["test_id"] for case in response["test_cases"]] == preservation["stage_test_allocation"][suffix]
    for case in response["test_cases"]:
        actual = rows((ROOT / case["path"]).read_text())[case["test_id"]]
        assert sha(actual.encode()) == case["row_sha256"]
        fields = [part.strip() for part in actual.strip().strip("|").split("|")]
        assert fields[1] == case["input_and_premises"] and fields[2] == case["static_expected_result"]
        case_count += 1
assert case_count == 21
assert set(resume["remaining_ids"]) == set(scope["authorization_constraints"]["pending_ids"])
assert not preservation["unaccepted_B03_consumed_as_accepted"]

# Inspect exact source identity/reading ranges as bytes. No Ruby/game/media functions are called.
assert git("rev-parse", "HEAD", cwd=REF_ROOT).decode().strip() == reading["reference_commit"]
assert git("rev-parse", "HEAD^{tree}", cwd=REF_ROOT).decode().strip() == reading["reference_tree"]
assert not git("status", "--porcelain=v1", cwd=REF_ROOT)
assert not reading["reference_execution"]
for item in reading["readings"]:
    data = (REF_ROOT / item["path"]).read_bytes()
    assert sha(data) == item["sha256"]
    lines = data.splitlines(keepends=True)
    for span in item["read_ranges"]:
        assert sha(b"".join(lines[span["start"] - 1:span["end"]])) == span["range_sha256"]

result = {
    "stage": "B06_AUTHOR_STAGE_1_SEVEN_CONTRIBUTIONS_ONLY",
    "result": "AUTHOR_STATIC_CHECKS_COMPLETED_NO_REVIEW_VERDICT",
    "base_commit": BASE,
    "formal_paths_checked": formal,
    "formal_path_count": len(formal),
    "body_clause_edit_bounds": body_edits,
    "catalog_scope_checks": catalog_results,
    "assigned_static_case_count": case_count,
    "new_test_row_count": 19,
    "existing_test_rows_revised": ["PS-11", "AQ-04"],
    "exact_patch_identities_checked": patches["patches"],
    "protected_section_count": len(preservation["protected_sections"]),
    "protected_test_ids": [item["test_id"] for item in preservation["protected_test_rows"]],
    "protected_whole_files": protected,
    "B05_handoff_identity_count": len(freeze["B05_handoff_identity_checks"]),
    "complete_canonical_input_pairs_rechecked": len(inputs["objects"]),
    "fixed_reference_text_reading_files": len(reading["readings"]),
    "B03_candidate_consumed_as_accepted": False,
    "independent_review_verdict": None,
    "actual_integration_review_verdict": None,
    "canonical_status_changes": 0,
    "public_registry_writes": 0,
    "full_B06_ready": False,
    "runtime_observations": 0,
    "proven_demo_event_chains": 0,
    "reference_execution": False,
    "reference_status_porcelain": "",
    "retained_boundaries": scope["evidence_limits"]["retained_boundaries"],
    "limitations": "Document/byte identity and author static comparison only; no game tests, independent verdict, acceptance, integration or closure.",
}
(STAGE / "static-validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(f"Author static checks completed: {len(formal)} formal paths, {case_count} assigned cases, "
      "19 appended rows; no independent review verdict.")
