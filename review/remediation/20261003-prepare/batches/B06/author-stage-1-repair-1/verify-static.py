#!/usr/bin/env python3
"""Bounded successor document checks only. Never execute a source behavior vector."""
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
OLD_DIR = "review/remediation/20261003-prepare/batches/B06/author-stage-1/"
REVIEW_DIR = "review/remediation/20261003-prepare/batches/B06/review-stage-1-round-1/"
PARENT = "806c969105f4f2aca916708013ad54f972524d5e"
REVIEW = "e12791309ace5458da29fd91c7bed70ac4175700"
BASE = "ae230e76e9c041f39c28948321d0960804c02388"
REF = Path("/workspace/reference-b06-20261003-prepare")


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd)


def blob(commit, path):
    return git("show", commit + ":" + path)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(name):
    return json.loads((OUT / name).read_text())


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def rows(data):
    result = {}
    for n, line in enumerate(data.decode().splitlines(keepends=True), 1):
        match = re.match(r"^\| ([A-Z]+-\d+) \|", line)
        if match:
            assert match[1] not in result
            result[match[1]] = (n, line)
    return result


def section(data, heading):
    lines = data.decode().splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.startswith(heading))
    level = len(lines[start].split(" ")[0])
    end = next((i for i in range(start + 1, len(lines))
                if re.match(r"^#{1," + str(level) + r"} ", lines[i])), len(lines))
    return "".join(lines[start:end]).encode()


scope = load("scope-successor.json")
freeze = load("input-freeze.json")
reading = load("source-reading-log.json")
formal = scope["inherited_eight_formal_paths"]
assert git("branch", "--show-current").decode().strip() == scope["branch"]
git("merge-base", "--is-ancestor", PARENT, "HEAD")
git("diff", "--check", PARENT)
changed = set(git("diff", "--name-only", PARENT).decode().splitlines())
changed.update(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
assert {p for p in changed if not p.startswith(PREFIX)} == set(scope["repair_formal_write_paths"])
assert not scope["whole_B06_ready"] and not scope["integration_started"]

# The first author packet and the independent report remain immutable.
for item in freeze["immutable_prior_author_artifacts"]:
    assert (ROOT / item["path"]).read_bytes() == blob(PARENT, item["path"])
    assert sha(blob(PARENT, item["path"])) == item["sha256"]
for item in load("review-reading-receipt.json")["review_artifacts"]:
    assert sha(blob(REVIEW, item["path"])) == item["sha256"]

# Exact repair delta, separate from inherited seven-ID behavior changes.
delta_bounds = {formal[1]: {94, 201}, formal[6]: {77}}
clause_checks = []
for path, allowed in delta_bounds.items():
    old = blob(PARENT, path).decode().splitlines(keepends=True)
    new = (ROOT / path).read_text().splitlines(keepends=True)
    seen = set()
    for kind, i, j, m, n in difflib.SequenceMatcher(a=old, b=new, autojunk=False).get_opcodes():
        if kind == "equal":
            continue
        if kind == "insert":
            assert path == formal[1] and i == 95
            assert n - m == 2
        else:
            assert kind == "replace" and j == i + 1 and i + 1 in allowed, (path, kind, i, j)
            seen.add(i + 1)
        clause_checks.append({"path": path, "delta_kind": kind,
                              "parent_lines": [i + 1, j], "new_lines": [m + 1, n],
                              "before_sha256": sha("".join(old[i:j]).encode()),
                              "after_sha256": sha("".join(new[m:n]).encode())})
    assert seen == allowed, (path, seen)
for path in set(formal) - set(scope["repair_formal_write_paths"]):
    assert (ROOT / path).read_bytes() == blob(PARENT, path)

# Existing rows and all CI/HP/PT/AQ text are byte-preserved; only PS appended/header extended.
catalog = formal[3]
old = blob(PARENT, catalog)
new = (ROOT / catalog).read_bytes()
old_rows, new_rows = rows(old), rows(new)
new_ids = {"PS-39", "PS-40", "PS-41", "PS-42"}
assert set(new_rows) - set(old_rows) == new_ids and not set(old_rows) - set(new_rows)
assert all(old_rows[key][1] == new_rows[key][1] for key in old_rows)
normalized = new.decode()
for key in new_ids:
    normalized = normalized.replace(new_rows[key][1], "")
normalized = normalized.replace("（PS-01～PS-42）", "（PS-01～PS-38）")
assert normalized.encode() == old
assert {key for key in new_rows if key.startswith("PS-")} == {f"PS-{n:02d}" for n in range(1, 43)}
assert all(len(row.strip().strip("|").split("|")) == 3 for _, row in new_rows.values())

# Recheck every inherited stage row and its review identity; do not migrate prior verdicts.
prior = json.loads(blob(PARENT, OLD_DIR + "preservation-freeze.json"))
regression = []
review_inputs = json.loads(blob(REVIEW, REVIEW_DIR + "input-and-preservation.json"))
for item in review_inputs["stage_row_identities"]:
    row = rows((ROOT / item["path"]).read_bytes())[item["test_id"]][1]
    assert sha(row.encode()) == item["sha256"]
    regression.append(dict(item, successor_line=rows((ROOT / item["path"]).read_bytes())[item["test_id"]][0],
                           successor_bytes_unchanged=True))
assert len(regression) == 21
for item in prior["protected_whole_files"]:
    assert (ROOT / item["path"]).read_bytes() == blob(BASE, item["path"])
    assert sha((ROOT / item["path"]).read_bytes()) == item["sha256"]
for item in prior["protected_sections"]:
    current = section((ROOT / item["path"]).read_bytes(), item["heading_prefix"])
    assert sha(current) == item["sha256"]
for item in prior["protected_test_rows"]:
    row = rows((ROOT / item["path"]).read_bytes())[item["test_id"]][1]
    assert sha(row.encode()) == item["sha256"]

# N002: the range must be valid BEFORE slice construction or hash calculation.
assert git("rev-parse", "HEAD", cwd=REF).decode().strip() == reading["reference_commit"]
assert git("rev-parse", "HEAD^{tree}", cwd=REF).decode().strip() == reading["reference_tree"]
assert not git("status", "--porcelain=v1", cwd=REF)
checked_spans = []
for item in reading["readings"]:
    data = (REF / item["path"]).read_bytes()
    assert data == git("show", reading["reference_commit"] + ":" + item["path"], cwd=REF)
    assert sha(data) == item["sha256"]
    assert len(data.splitlines(keepends=True)) == item["actual_line_count"]
    for span in item["read_ranges"]:
        actual = checked_range_sha256(data, span["start"], span["end"])
        assert actual == span["range_sha256"]
        checked_spans.append({"reading_id": item["reading_id"], "path": item["path"],
                              "start": span["start"], "end": span["end"],
                              "actual_lines": item["actual_line_count"], "sha256": actual})
trainer = next(item for item in reading["readings"] if item["reading_id"] == "B06-SR-03")
data = (REF / trainer["path"]).read_bytes()
assert trainer["actual_line_count"] == 124
assert trainer["read_ranges"] == [{"start": 1, "end": 124, "range_sha256": trainer["sha256"]}]
valid_checks = []
for start, end in [(1, 124), (124, 124)]:
    actual = checked_range_sha256(data, start, end)
    assert len(actual) == 64
    valid_checks.append({"start": start, "end": end, "accepted": True})
rejected = []
for start, end in [(1, 135), (125, 125), (0, 124), (124, 1), (1, 0)]:
    hash_calls = []

    def prohibited_hasher(chunk):
        hash_calls.append(True)
        raise AssertionError("Invalid range reached hashing")

    try:
        checked_range_sha256(data, start, end, hash_bytes=prohibited_hasher)
    except ValueError:
        assert not hash_calls
        rejected.append({"start": start, "end": end, "rejected_before_hash": True,
                         "hash_function_calls": 0})
    else:
        raise AssertionError(("Invalid evidence range accepted", start, end))
dump("source-range-validation.json", {
    "issue_id": "B06-S1-R1-N002", "trainer_actual_lines": 124,
    "current_recorded_trainer_range": [1, 124], "checked_actual_source_spans": checked_spans,
    "document_range_valid_cases": valid_checks, "document_range_rejection_cases": rejected,
    "document_range_fixture_checks_executed": 7,
    "reference_program_execution": 0, "behavioral_vectors_executed": 0,
    "history_note": "The old 1–135 slice/hash silently truncated. The old packet is immutable and its hash never proves lines 125–135 exist."
})

# New vector identities are document assertions. No wallpaper regex is executed here.
responses = load("finding-responses.json")
assert {item["id"] for item in responses["new_defect_responses"]} == set(scope["repair_ids"])
for item in responses["all_seven_stage_responses"]:
    assert item["new_independent_verdict"] is None and not item["close"]
    for case in item["test_cases"]:
        actual = rows((ROOT / case["path"]).read_bytes())[case["test_id"]][1]
        assert sha(actual.encode()) == case["row_sha256"]
assert sum(len(item["test_cases"]) for item in responses["all_seven_stage_responses"]) == 25
assert not responses["whole_B06_ready"]
patches = load("patch-identities.json")
for item in patches["patches"]:
    actual = git("diff", "--binary", "--unified=0", item["base_commit"], "--", *item["paths"])
    assert actual == (ROOT / item["path"]).read_bytes() and sha(actual) == item["sha256"]

dump("static-validation.json", {
    "result": "AUTHOR_SUCCESSOR_DOCUMENT_CHECKS_COMPLETED_NO_INDEPENDENT_VERDICT",
    "review_source_commit": REVIEW, "parent_author_evidence": PARENT,
    "repair_formal_paths": scope["repair_formal_write_paths"],
    "full_stage_formal_path_count": 8, "repair_formal_path_count": 3,
    "repair_clause_delta_bounds": clause_checks,
    "inherited_21_vector_regression": regression, "appended_static_ids": sorted(new_ids),
    "all_existing_catalog_rows_and_text_preserved": True,
    "all_seven_static_vector_count": 25, "reference_source_span_count": len(checked_spans),
    "source_ranges_bounded_before_hash": True, "invalid_range_fixture_rejections": rejected,
    "previous_author_artifacts_unchanged": len(freeze["immutable_prior_author_artifacts"]),
    "fixed_independent_review_artifacts_unchanged": 11,
    "protected_section_count": 10, "protected_whole_file_count": 17,
    "prior_six_review_verdicts_transfer_automatically": False,
    "public_registry_writes": 0, "finding_closures": 0, "integration_started": False,
    "whole_B06_ready": False, "runtime_observations": 0, "proven_demo_event_chains": 0,
    "reference_execution": 0, "behavioral_vectors_executed": 0,
    "retained_boundaries": scope["retained_boundaries"],
    "limitations": "Text/byte identity, source-range metadata and manual static inference only; next independent Ultra and actual integration affected review remain required."
})
print("Successor document checks completed: 3 repair paths, 21 preserved vectors + 4 static additions; "
      "124-line source range bounded; invalid ranges rejected before hashing. No independent verdict.")
