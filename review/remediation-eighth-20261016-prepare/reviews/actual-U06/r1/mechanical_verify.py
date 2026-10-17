"""Recheck fixed Git identities and document preservation; no semantic verdict.

Only this script's sibling mechanical-checks.json is written in the worktree.
The first two Git commands re-receive the source commits with explicit parent
authorization, without checkout or branch/ref change (FETCH_HEAD/objects only).
All subsequent Git commands are read-only.
No Ruby, game model, media, native behavior, or candidate verifier is executed.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / ".git").exists())
PREFIX = "review/remediation-eighth-20261016-prepare/"
FORMAL = "deliverables/final-specification-set/"
BINDING = "5ff355c53b73171a0277c95af97e1cbd40eb8b28"
ACTUAL = "0eee6d141f33758eda34bd8ebad94a3e2b617f5a"
CANDIDATE = "16f986afc1c85e64131f1dc8c6f2477a79c04029"
REVIEW = "052236414f6cb350f1781efe98761f336bb43108"
LATEST_REGISTRATION = "2e2d5e6ab3f531ee902f60574b22e20fb065e04b"
DELIVERY = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
SIX_FREEZE = "49a558f7d5498680ba88d532f3815e07d7844459"
SIX_BINDING = "56cc0f683249bd54658b94134d1a61be6e8748e0"
SIX_PREFIX = PREFIX + "integration/U01-U04-U05-U07-U08-U09/"
INPUT_PATH = PREFIX + "integration/U06/actual-review-input.json"
commands = []
checks = []
identity_cache = {}
data_cache = {}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def utc():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    started = utc()
    argv = ["git", *args]
    proc = subprocess.run(argv, cwd=REPO, capture_output=True, check=False)
    record = {
        "argv": argv, "cwd": str(REPO), "started_utc": started,
        "finished_utc": utc(), "exit_code": proc.returncode,
        "stdout_bytes": len(proc.stdout), "stdout_sha256": digest(proc.stdout),
        "stderr_bytes": len(proc.stderr), "stderr_sha256": digest(proc.stderr),
        "stderr_utf8": proc.stderr.decode("utf-8", "replace"),
        "credit": "MECHANICAL_ONLY; not semantic full reading or behavior execution",
    }
    if len(proc.stdout) <= 1024:
        record["stdout_utf8"] = proc.stdout.decode("utf-8", "replace")
    commands.append(record)
    if proc.returncode:
        raise RuntimeError(record)
    return proc.stdout


def content(commit, path):
    key = (commit, path)
    if key not in data_cache:
        data_cache[key] = git("show", commit + ":" + path)
    return data_cache[key]


def document(commit, path):
    return json.loads(content(commit, path))


def identity(commit, path):
    key = (commit, path)
    if key not in identity_cache:
        raw = content(commit, path)
        mode, kind, blob = git("ls-tree", commit, "--", path).decode().split("\t")[0].split()
        identity_cache[key] = {
            "commit": commit, "path": path, "mode": mode, "kind": kind,
            "blob": blob, "bytes": len(raw), "sha256": digest(raw),
        }
    return identity_cache[key]


def compare_identity(expected, commit=None, path=None):
    got = identity(commit or expected["commit"], path or expected["path"])
    fields = ["mode", "blob", "bytes", "sha256"]
    differences = {k: {"expected": expected[k], "observed": got[k]}
                   for k in fields if expected[k] != got[k]}
    return {"expected": expected, "observed": got, "matched": not differences,
            "differences": differences}


def tree(commit, path):
    result = {}
    for line in git("ls-tree", "-r", commit, "--", path).decode().splitlines():
        header, name = line.split("\t", 1)
        result[name] = header.split()
    return result


def check(name, matched, evidence):
    checks.append({"name": name, "matched": bool(matched), "evidence": evidence})


def catalog_rows(raw):
    return Counter(line for line in raw.decode().splitlines() if line.startswith("|"))


started = utc()
# Capture a fresh, complete transport receipt including actual UTC and exit.
# Earlier successful receptions were observed through the tool; these repeats
# avoid assigning invented UTC timestamps to those earlier operations.
git("fetch", "origin", CANDIDATE)
git("fetch", "origin", REVIEW)
manifest = document(BINDING, INPUT_PATH)
batch = manifest["batches"][0]
input_identity = identity(BINDING, INPUT_PATH)
check("fixed identity binding fields", (
    manifest["artifact_snapshot_commit"] == ACTUAL
    and batch["actual_integration_commit"] == ACTUAL
    and batch["candidate_commit"] == CANDIDATE
    and batch["candidate_review_source_commit"] == REVIEW
    and manifest["fixed_delivery_commit"] == DELIVERY
    and len(batch["required_ids"]) == 11
    and len(batch["selected_optional_ids"]) == 3
), {"manifest_identity": input_identity, "required_ids": batch["required_ids"],
    "selected_optional_ids": batch["selected_optional_ids"]})
check("input manifest preserved at latest registration",
      content(BINDING, INPUT_PATH) == content(LATEST_REGISTRATION, INPUT_PATH),
      identity(LATEST_REGISTRATION, INPUT_PATH))
workspace_tree = git("rev-parse", ACTUAL + "^{tree}").decode().strip()
formal_tree = git("rev-parse", ACTUAL + ":" + FORMAL.rstrip("/")).decode().strip()
check("actual workspace and formal tree identities", (
    workspace_tree == manifest["artifact_workspace_tree"]
    and formal_tree == manifest["artifact_formal_tree"]
), {"workspace_tree": workspace_tree, "formal_tree": formal_tree})

payload = [compare_identity(item) for item in manifest["payload_identities"]]
check("all 79 frozen payload identities", len(payload) == 79 and all(x["matched"] for x in payload),
      {"entries": len(payload), "mismatches": [x for x in payload if not x["matched"]]})
targets = [compare_identity(item) for item in batch["actual_target_identities"]]
check("all 12 actual target identities", len(targets) == 12 and all(x["matched"] for x in targets),
      {"entries": len(targets), "mismatches": [x for x in targets if not x["matched"]]})

import_manifest = document(ACTUAL, PREFIX + "integration/U06/import-identities.json")
imports = []
groups = Counter()
for item in import_manifest["records"]:
    groups[item["type"]] += 1
    imported = {"type": item["type"], "source": compare_identity(item)}
    for label, commit in [("actual", ACTUAL), ("binding", BINDING), ("latest", LATEST_REGISTRATION)]:
        imported[label] = compare_identity(item, commit)
    raw = (REPO / item["path"]).read_bytes()
    imported["working_file"] = {
        "bytes": len(raw), "sha256": digest(raw),
        "matched": raw == content(item["commit"], item["path"]),
    }
    imports.append(imported)
check("27 candidate and 19 independent-review imports equal original sources", (
    groups == {"AUTHOR_CANDIDATE": 27, "INDEPENDENT_CANDIDATE_REVIEW": 19}
    and all(v[part]["matched"] for v in imports
            for part in ["source", "actual", "binding", "latest", "working_file"])
), {"groups": dict(groups), "records": len(imports)})

target_equalities = []
for expected in batch["actual_target_identities"]:
    path = expected["path"]
    mirror = batch["candidate_mirror_prefix"] + path
    locations = [(ACTUAL, path), (CANDIDATE, mirror), (ACTUAL, mirror),
                 (BINDING, path), (LATEST_REGISTRATION, path)]
    entries = [identity(c, p) for c, p in locations]
    raw = content(ACTUAL, path)
    equal = all(content(c, p) == raw for c, p in locations)
    working = (REPO / path).read_bytes()
    target_equalities.append({"formal_path": path, "matched": equal and working == raw,
                              "locations": entries, "working_bytes": len(working),
                              "working_sha256": digest(working)})
check("12 formal targets equal reviewed source mirrors and preserved latest bytes",
      len(target_equalities) == 12 and all(x["matched"] for x in target_equalities),
      {"entries": len(target_equalities), "formal_bytes": sum(x["locations"][0]["bytes"] for x in target_equalities)})

base_formal = tree(DELIVERY, FORMAL)
actual_formal = tree(ACTUAL, FORMAL)
binding_formal = tree(BINDING, FORMAL)
latest_formal = tree(LATEST_REGISTRATION, FORMAL)
changed = [p for p in base_formal if actual_formal.get(p) != base_formal[p]]
unchanged = [p for p in base_formal if actual_formal.get(p) == base_formal[p]]
formal_counts = {
    "delivery_total": len(base_formal), "actual_total": len(actual_formal),
    "binding_total": len(binding_formal), "latest_total": len(latest_formal),
    "changed_from_delivery": len(changed), "unchanged_from_delivery": len(unchanged),
    "added": sorted(actual_formal.keys() - base_formal.keys()),
    "removed": sorted(base_formal.keys() - actual_formal.keys()),
    "changed_paths": changed, "unchanged_paths": unchanged,
    "actual_equals_binding": actual_formal == binding_formal,
    "actual_equals_latest": actual_formal == latest_formal,
}
check("formal file count and cumulative 38 changed plus 93 unchanged", (
    len(base_formal) == len(actual_formal) == len(binding_formal) == len(latest_formal) == 131
    and len(changed) == 38 and len(unchanged) == 93
    and base_formal.keys() == actual_formal.keys()
    and actual_formal == binding_formal == latest_formal
), formal_counts)

catalogs = []
new_ids = []
for name in ["combat-requirements-wp39-40-41-42-45.md", "combat-requirements-wp49-51-52.md",
             "pokemon-rules-wp19-21-22-23-34.md"]:
    path = FORMAL + "test-catalog/" + name
    old = catalog_rows(content(DELIVERY, path))
    new = catalog_rows(content(ACTUAL, path))
    removed = list((old - new).elements())
    exceptional = []
    if "wp49-51-52" in name:
        exceptional = [row for row in old if row.startswith("| T02 |")]
        same_id = [row for row in new if row.startswith("| T02 |")]
        exception_ok = len(exceptional) == len(same_id) == 1 and old[exceptional[0]] == new[same_id[0]] == 1
        old_without_exception = old.copy()
        for row in exceptional:
            del old_without_exception[row]
        preserved = not (old_without_exception - new)
    else:
        same_id = []
        exception_ok = True
        old_without_exception = old
        preserved = not (old - new)
    added_rows = list((new - old).elements())
    ids = []
    for row in added_rows:
        value = row.split("|", 2)[1].strip()
        if value.startswith("R8-U06-"):
            ids.append(value)
    new_ids.extend(ids)
    entry = {
        "path": path, "old_table_rows": sum(old.values()), "actual_table_rows": sum(new.values()),
        "old_rows_required_unchanged": sum(old_without_exception.values()),
        "missing_required_old_row_multiset": list((old_without_exception - new).elements()),
        "removed_full_rows": removed, "AE_family_T02_original": exceptional,
        "AE_family_T02_actual_same_ID": same_id, "same_ID_exception_matched": exception_ok,
        "added_rows": added_rows, "new_R8_U06_IDs": ids,
        "matched": preserved and exception_ok,
    }
    catalogs.append(entry)
expected_new_ids = ([f"R8-U06-Z{i:02d}" for i in range(1, 6)]
                    + [f"R8-U06-M{i:02d}" for i in range(1, 5)]
                    + [f"R8-U06-EV{i:02d}" for i in range(1, 3)]
                    + [f"R8-U06-CV{i:02d}" for i in range(1, 6)]
                    + [f"R8-U06-ST{i:02d}" for i in range(1, 6)])
check("three complete old table row multisets and same-ID AE T02 retained",
      len(catalogs) == 3 and all(x["matched"] for x in catalogs),
      {"old_total_rows": sum(x["old_table_rows"] for x in catalogs),
       "unchanged_old_rows": sum(x["old_rows_required_unchanged"] for x in catalogs),
       "same_ID_revised_rows": 1, "catalogs": catalogs})
check("21 new U06 catalog IDs counted separately without renumbering originals",
      Counter(new_ids) == Counter(expected_new_ids),
      {"observed": new_ids, "expected": expected_new_ids, "count": len(new_ids)})

six_preservation = []
for origin in [SIX_FREEZE, SIX_BINDING]:
    original = tree(origin, SIX_PREFIX)
    for end in [ACTUAL, BINDING, LATEST_REGISTRATION]:
        current = tree(end, SIX_PREFIX)
        altered = [p for p, value in original.items() if current.get(p) != value]
        extra = sorted(current.keys() - original.keys())
        six_preservation.append({"origin": origin, "endpoint": end,
                                 "original_files": len(original), "altered_or_deleted": altered,
                                 "added": extra, "matched": not altered and (origin != SIX_BINDING or not extra)})
check("six-batch freeze content preserved and binding subtree unchanged in successors",
      all(x["matched"] for x in six_preservation), six_preservation)
six_working = []
for path in tree(SIX_BINDING, SIX_PREFIX):
    expected = content(SIX_BINDING, path)
    current = (REPO / path).read_bytes()
    six_working.append({"path": path, "bytes": len(current), "sha256": digest(current),
                        "matched": current == expected})
check("current working six-batch input directory equals its complete frozen binding",
      len(six_working) == 7 and all(x["matched"] for x in six_working), six_working)
six_frozen_input = identity(SIX_BINDING, SIX_PREFIX + "actual-review-input.json")
six_frozen_entry = identity(SIX_BINDING, SIX_PREFIX + "reviewer-entry.md")

protected = []
for path in ["AGENTS.md", "audit/", "planning/", "review/"]:
    original = tree(DELIVERY, path)
    current = tree(LATEST_REGISTRATION, path)
    outside = [p for p, v in original.items() if current.get(p) != v and not p.startswith(PREFIX)]
    protected.append({"path": path, "old_tracked_entries": len(original),
                      "modified_or_deleted_outside_R8": outside, "matched": not outside})
check("original AGENTS audit planning and prior review evidence preserved",
      all(x["matched"] for x in protected), protected)

ancestry = []
for start, end in [(SIX_FREEZE, SIX_BINDING), (SIX_BINDING, ACTUAL), (ACTUAL, BINDING),
                   (BINDING, LATEST_REGISTRATION)]:
    git("merge-base", "--is-ancestor", start, end)
    ancestry.append({"ancestor": start, "descendant": end, "exit_code": 0})
check("fixed ancestry chain", len(ancestry) == 4, ancestry)

report = {
    "schema": "r8-u06-actual-mechanical-identity-scope/v1",
    "started_utc": started, "finished_utc": utc(), "repo": str(REPO),
    "outcome": "MECHANICAL_IDENTITY_SCOPE_CHECKS_COMPLETE",
    "all_mechanical_comparisons_matched": all(x["matched"] for x in checks),
    "qualification": "Mechanical identity/scope only. No semantic/full-reading/configuration verdict or PASS/FAIL is issued by this helper.",
    "behavior_execution": "NOT_EXECUTED", "semantic_full_reading_credit": "NONE",
    "configuration_qualification": "NOT_ASSESSED; this helper makes no runtime/model/tier claim",
    "write_scope": str(HERE.relative_to(REPO)) + "/",
    "bindings": {"input": BINDING, "actual": ACTUAL, "candidate": CANDIDATE,
                 "independent_review": REVIEW, "latest_registration": LATEST_REGISTRATION,
                 "delivery": DELIVERY, "six_freeze": SIX_FREEZE, "six_binding": SIX_BINDING},
    "input_identity": input_identity, "checks": checks,
    "payload_identities": payload, "actual_target_identities": targets,
    "source_import_identities": imports, "target_mirror_equalities": target_equalities,
    "six_frozen_input_identity": six_frozen_input, "six_frozen_entry_identity": six_frozen_entry,
    "script_identity": {"path": str(Path(__file__).relative_to(REPO)),
                        "bytes": Path(__file__).stat().st_size,
                        "sha256": digest(Path(__file__).read_bytes())},
    "commands": commands,
    "source_reception_commands_before_script": [
        {"argv": ["git", "fetch", "origin", CANDIDATE], "exit_code": 0,
         "stdout": "", "stderr": "From https://github.com/y805939188/pokemon-essentials-clean-room\n * branch              16f986afc1c85e64131f1dc8c6f2477a79c04029 -> FETCH_HEAD\n",
         "UTC": "NOT_CAPTURED_IN_ORIGINAL_TOOL_OUTPUT; fresh repeats are fully recorded in commands",
         "authorization": "Parent explicitly allowed Git object/FETCH_HEAD metadata reception; no checkout or branch change."},
        {"argv": ["git", "fetch", "origin", REVIEW], "exit_code": 0,
         "stdout": "", "stderr": "From https://github.com/y805939188/pokemon-essentials-clean-room\n * branch              052236414f6cb350f1781efe98761f336bb43108 -> FETCH_HEAD\n",
         "UTC": "NOT_CAPTURED_IN_ORIGINAL_TOOL_OUTPUT; fresh repeats are fully recorded in commands",
         "authorization": "Parent explicitly allowed Git object/FETCH_HEAD metadata reception; no checkout or branch change."},
    ],
    "initial_navigation_failures": [
        {"argv": ["git", "cat-file", "-t", CANDIDATE], "exit_code": 128,
         "reason": "Source commit absent locally before authorized fetch; subsequently resolved."},
        {"argv": ["git", "cat-file", "-t", REVIEW], "exit_code": 128,
         "reason": "Source commit absent locally before authorized fetch; subsequently resolved."},
        {"argv": ["gh", "api", "repos/y805939188/pokemon-essentials-clean-room/git/commits/" + CANDIDATE,
                  "--jq", "{sha:.sha, tree:.tree.sha}"], "exit_code": "NOT_RETAINED_IN_DISPLAYED_OUTPUT",
         "observed_tool_output": "Get \"https://api.github.com/repos/y805939188/pokemon-essentials-clean-room/git/commits/16f986afc1c85e64131f1dc8c6f2477a79c04029\": Forbidden",
         "UTC": "NOT_CAPTURED_IN_ORIGINAL_TOOL_OUTPUT",
         "reason": "Read-only API route failed; Git transport succeeded. No evidence credit assigned to this call."},
    ],
    "remaining_mechanical_blockers": [],
}
output = HERE / "mechanical-checks.json"
output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"outcome": report["outcome"], "all_mechanical_comparisons_matched": report["all_mechanical_comparisons_matched"],
                  "checks": len(checks), "commands": len(commands), "output": str(output.relative_to(REPO)),
                  "output_bytes": output.stat().st_size, "output_sha256": digest(output.read_bytes())}, ensure_ascii=False))
if not report["all_mechanical_comparisons_matched"]:
    raise SystemExit(1)
