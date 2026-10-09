"""New bounded reviewer checker: Git/JSON/text/hash metadata only, no behavior execution.

Reads fixed project objects. Never imports or runs project/reference/old review code.
Writes only this delegation's three affected report directories.
"""
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

REVIEWED = "4fa6b5fcf726e8723ba1aa31b2f22a7f53390c52"
BASE = "0cfe99094b76f8d75fded0d638694677855a5f0c"
DISPATCH = "4cb51a33402ec6559a396226239afe308a4b8849"
WRAPPER = "d65a76268997051a4e5df178af9abcbd254ffa02"
ROOT = Path(__file__).resolve().parents[6]
PREFIX = "review/remediation/20261003-prepare/batches/B11/"
CONTROL_PATH = PREFIX + "refreeze-after-B10-C-1/original-and-acceptance-controls.json"
cache = {}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def raw(commit, path):
    key = (commit, path)
    if key not in cache:
        cache[key] = git("show", commit + ":" + path)
    return cache[key]


def obj(commit, path):
    return json.loads(raw(commit, path))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def identity(commit, path):
    data = raw(commit, path)
    return {"commit": commit, "path": path, "git_blob": git("rev-parse", commit + ":" + path).decode().strip(),
            "sha256": digest(data), "bytes": len(data)}


def pointer(value, path):
    for part in path.strip("/").split("/"):
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def canonical_digest(value):
    return digest(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())


def emit(owner, name, value):
    target = ROOT / (PREFIX + "affected-" + owner + "-review-round-1/")
    target.mkdir(parents=True, exist_ok=True)
    (target / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert git("remote", "get-url", "origin").decode().strip() == "https://github.com/y805939188/pokemon-essentials-clean-room.git"
controls = obj(DISPATCH, CONTROL_PATH)
dispatch = obj(REVIEWED, PREFIX + "candidate-1/independent-review-dispatch.json")
contract = obj(DISPATCH, PREFIX + "refreeze-after-B10-C-1/B11-downstream-contract.json")
assert raw(REVIEWED, PREFIX + "candidate-1/independent-review-dispatch.json") == raw(WRAPPER, PREFIX + "candidate-1/independent-review-dispatch.json")
control_checks = []
for control in controls["controls"]:
    record = {"id": control["id"], "original": {}, "acceptance": {}}
    for label, field, binding in [("original", "whole_original_object", "whole_original_object_binding"),
                                  ("acceptance", "whole_approved_acceptance_object", "whole_approved_acceptance_binding")]:
        bound = control[binding]
        actual = identity(bound["commit"], bound["path"])
        assert all(actual[k] == bound[k] for k in ("git_blob", "sha256", "bytes"))
        original = pointer(obj(bound["commit"], bound["path"]), bound["pointer"])
        assert original == control[field]
        record[label] = {**actual, "pointer": bound["pointer"], "complete_object_equal": True,
                         "canonical_json_sha256": canonical_digest(original)}
    current = control["complete_current_control_fields"]
    assert all(current[k] == control["whole_original_object"][k] for k in current)
    record["complete_current_fields_equal_original"] = True
    record["current_fields_sha256"] = canonical_digest(current)
    record["accepted_contributors"] = control["accepted_contributors"]
    record["pending_contributors"] = control["pending_contributors"]
    control_checks.append(record)

diff = git("diff", "--binary", "--full-index", BASE, REVIEWED)
assert diff == raw(WRAPPER, PREFIX + "candidate-1/full-candidate.diff")
names = git("diff", "--name-status", BASE, REVIEWED).decode().splitlines()
changes = [{"status": row.split("\t")[0], "path": row.split("\t")[1]} for row in names]
amendment = obj(REVIEWED, PREFIX + "candidate-1/scope-amendment-receipt.json")
formal = contract["allowed_formal_write_paths"] + [x["path"] for x in amendment["authorized_scope"]]
assert len(formal) == len(set(formal)) == 10
for change in changes:
    if change["path"] not in formal:
        assert change["status"] == "A" and any(change["path"].startswith(PREFIX + d + "/") for d in ["author-draft-1", "candidate-1"])
formal_identities = []
for path in formal:
    before, after = identity(BASE, path), identity(REVIEWED, path)
    formal_identities.append({"path": path, "before": before, "after": after, "changed": before["git_blob"] != after["git_blob"]})
for record in amendment["records"]:
    assert all(identity(BASE, record["path"])[k] == record["before"][k] for k in ["git_blob", "sha256", "bytes"])
    assert all(identity(REVIEWED, record["path"])[k] == record["proposed_after"][k] for k in ["git_blob", "sha256", "bytes"])
approved_original_diff = git("diff", "--unified=3", BASE, REVIEWED, "--", *[x["path"] for x in amendment["authorized_scope"]])
assert sum(line.startswith(b"@@ ") for line in approved_original_diff.splitlines()) == 3
scope_check = {"baseline": BASE, "reviewed_sha": REVIEWED, "unfiltered_diff_bytes": len(diff), "unfiltered_diff_sha256": digest(diff),
               "wrapper_diff_archive_equal": True, "changed_path_count": len(changes), "unfiltered_changes": changes,
               "formal_boundary": formal_identities, "changed_formal_paths": sum(x["changed"] for x in formal_identities),
               "unapproved_formal_or_public_or_reference_changes": [], "approved_original_hunks": 3,
               "inspection_limit": "Unfiltered paths and hashes checked; assigned interface hunks reviewed. Separate R-B11 FULL review remains required."}

receipt_path = "review/remediation/20261003-prepare/batches/B10/acceptance-stage-1/completion-statistics-successor.json"
receipts = obj(BASE, receipt_path)["accepted_contribution_receipts"]
if isinstance(receipts, dict):
    receipts = list(receipts.values())
receipt_checks = {}
for role in dispatch["potential_affected_determinations"]:
    owner = role["accepted_owner"]
    receipt_checks[owner] = []
    for expected in role["accepted_receipts"]:
        found = [x for x in receipts if x["batch"] == owner and x["id"] == expected["id"]]
        assert len(found) == 1 and all(found[0][k] == v for k, v in expected.items())
        receipt_checks[owner].append(found[0])

reports = {
    "B07": ("d218aed120ed8ea1c88e1ec4752e5f7dcaaac226", "review/remediation/20261003-prepare/batches/B07/integration-review-1/finding-dispositions.json", "records"),
    "B09": ("aa7ed0226f36220c1ac6ad598bdcad132aee5e4b", "review/remediation/20261003-prepare/batches/B09/integration-review-1/contribution-review.json", "contributions"),
    "B10": ("e0259f89915f6448b77f08658c7032a0384db2d4", "review/remediation/20261003-prepare/batches/B10/actual-review-round-1/findings.json", "complete_control_results"),
}
reused = {}
for owner, (commit, path, key) in reports.items():
    assert raw(commit, path) == raw(BASE, path) == raw(REVIEWED, path)
    ids = next(x["scope"]["ids"] for x in dispatch["potential_affected_determinations"] if x["accepted_owner"] == owner)
    records = obj(commit, path)[key]
    reused[owner] = {**identity(commit, path), "same_bytes_at_BASE_and_reviewed": True,
                     "assigned_record_bindings": [{"id": x["id"], "pointer": "/" + key + "/" + str(i),
                                                   "record_canonical_sha256": canonical_digest(x)}
                                                  for i, x in enumerate(records) if x.get("id") in ids],
                     "reuse_limit": "Reuse only exact accepted assigned source/contract judgment; no inherited approval of new B11 candidate or future actual."}

catalogs = ["deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md",
            "deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md",
            "deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md"]
catalog_checks = []
for path in catalogs:
    before, after = raw(BASE, path), raw(REVIEWED, path)
    assert after.startswith(before)
    rows_before = [x for x in before.splitlines(keepends=True) if x.startswith(b"|")]
    rows_after = [x for x in after[:len(before)].splitlines(keepends=True) if x.startswith(b"|")]
    assert rows_before == rows_after and Counter(rows_before) == Counter(rows_after)
    catalog_checks.append({"path": path, "before": identity(BASE, path), "after": identity(REVIEWED, path),
                           "complete_old_byte_prefix_preserved": True, "old_lines": len(before.splitlines()),
                           "old_raw_table_row_count": len(rows_before), "old_row_sequence_equal": True,
                           "old_row_multiplicity_equal": True, "appended_bytes": len(after) - len(before),
                           "appended_text_sha256": digest(after[len(before):])})


def identifiers(cell):
    return re.findall(r"\b[A-Z][A-Z0-9_]*\b", cell)


def final_table(path, empty):
    rows = []
    for line_no, line in enumerate(raw(REVIEWED, path).decode().splitlines(), 1):
        cells = [x.strip() for x in line.split("|")[1:-1]]
        if len(cells) != 3:
            continue
        match = re.fullmatch(r"([A-Za-z0-9]+)（(\d+)）", cells[0])
        if match:
            family, label = match.groups()
            ids = identifiers(cells[1])
            assert int(label) == len(ids)
            rows.append({"family": family, "line": line_no, "label": int(label), "identities": ids, "identity_cell_sha256": digest(cells[1].encode())})
    families = {x["family"] for x in rows}
    for family in empty:
        if family not in families:
            rows.append({"family": family, "line": None, "label": 0, "identities": [], "empty_family_declared_in_prose": True})
    assert len(rows) == len({x["family"] for x in rows})
    return rows


def original_table(path):
    pairs, direct, copies, new = [], 0, 0, 0
    for line in raw(REVIEWED, path).decode().splitlines():
        cells = [x.strip() for x in line.split("|")[1:-1]]
        if len(cells) != 5 or cells[1] not in ["add", "copy"]:
            continue
        family, op, values = cells[:3]
        ids = identifiers(values)
        if op == "copy":
            assert (family, ids[0]) in pairs
            copies += 1
            ids = ids[1:]
            new += len(ids)
        else:
            assert len(ids) == 1
            direct += 1
        pairs.extend((family, item) for item in ids)
    assert len(pairs) == len(set(pairs))
    return pairs, direct, copies, new


family_checks = []
for final_path, original_path, empty, total, families in [
    ("deliverables/final-specification-set/pokemon-rules/wp48-ability-calculation-modifiers.md", "specs/pokemon-rules/wp48-ability-calculation-modifiers.md", ["CertainSwitching"], 148, 27),
    ("deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md", "specs/pokemon-rules/wp50-held-item-effect-coverage.md", ["CriticalCalcFromTarget", "TrappingByTarget"], 196, 32),
]:
    rows = final_table(final_path, empty)
    pairs = [(row["family"], item) for row in rows for item in row["identities"]]
    source, direct, copies, new = original_table(original_path)
    assert len(rows) == families and len(pairs) == len(set(pairs)) == total
    assert Counter(pairs) == Counter(source) and direct + new == total
    before_cells = []
    for line in raw(BASE, final_path).decode().splitlines():
        cells = [x.strip() for x in line.split("|")[1:-1]]
        if len(cells) == 3 and re.fullmatch(r"[A-Za-z0-9]+（\d+）", cells[0]):
            before_cells.append((cells[0].split("（")[0], cells[1], cells[2]))
    after_cells = []
    for line in raw(REVIEWED, final_path).decode().splitlines():
        cells = [x.strip() for x in line.split("|")[1:-1]]
        if len(cells) == 3 and re.fullmatch(r"[A-Za-z0-9]+（\d+）", cells[0]):
            after_cells.append((cells[0].split("（")[0], cells[1], cells[2]))
    assert before_cells == after_cells
    family_checks.append({"final_identity": identity(REVIEWED, final_path), "original_identity": identity(REVIEWED, original_path),
                          "family_count": len(rows), "pair_count": len(pairs), "unique_pair_count": len(set(pairs)),
                          "direct_rows": direct, "copy_statements": copies, "copy_new_pairs": new,
                          "original_minus_final": [], "final_minus_original": [], "all_identity_and_contract_cells_unchanged": True,
                          "rows": rows, "scope": "Opaque textual pair recount only; no ability/item behavior executed or established by counts."})

owner_paths = {
    "B07": ["deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md", "specs/creature-rpg/wp28-item-use-and-training.md", "deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md", "deliverables/final-specification-set/combat-requirements/wp51-ai-decision-defaults.md"],
    "B09": ["deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md", "specs/combat/wp39-battle-context-and-participants.md", "deliverables/final-specification-set/combat-requirements/wp54-entry-rules-and-cup-data.md", "deliverables/final-specification-set/combat-requirements/wp41-switching-positioning-and-escape.md", "specs/combat/wp41-switching-positioning-and-escape.md", "deliverables/final-specification-set/pokemon-rules/wp38-capture-and-receiving.md", "specs/pokemon-rules/wp38-capture-and-receiving.md", "deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md", "deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md"],
    "B10": [x["path"] for x in obj(BASE, "review/remediation/20261003-prepare/batches/B10/integration-stage-1/formal-copy-identities.json")["identities"]],
}
owner_checks = {}
for owner, paths in owner_paths.items():
    owner_checks[owner] = []
    accepted = receipt_checks[owner][0]["actual"]
    for path in paths:
        before, after = raw(BASE, path), raw(REVIEWED, path)
        shared_catalog = path == catalogs[1]
        assert after.startswith(before) if shared_catalog else before == after
        record = {"path": path, "BASE": identity(BASE, path), "reviewed": identity(REVIEWED, path),
                  "preservation": "complete byte prefix" if shared_catalog else "complete file byte identity"}
        if owner == "B10" or (owner == "B07" and "wp28-" in path) or (owner == "B09" and "wp54-" not in path):
            accepted_data = raw(accepted, path)
            record["accepted_actual"] = identity(accepted, path)
            record["BASE_equal_accepted_actual"] = before == accepted_data
            if owner == "B09" and path.endswith("combat-requirements-wp39-40-41-42-45.md"):
                def section(data, heading):
                    lines = data.splitlines(keepends=True)
                    start = next(i for i, line in enumerate(lines) if line.startswith(heading))
                    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith(b"## ")), len(lines))
                    return b"".join(lines[start:end])
                sections = []
                for heading in [b"## BC", b"## SW"]:
                    old = section(accepted_data, heading)
                    assert old == section(before, heading) == section(after, heading)
                    sections.append({"heading": heading.decode(), "bytes": len(old), "sha256": digest(old), "accepted_BASE_and_reviewed_equal": True})
                record["accepted_owner_sections"] = sections
                record["intervening_baseline_note"] = "B10 accepted P-section changes already exist in FIX_BASE; BC/SW sections are identical to exact B09 actual. B11 changes none of this file."
            else:
                assert before == accepted_data
        owner_checks[owner].append(record)

shared_inputs = [identity(DISPATCH, CONTROL_PATH), identity(DISPATCH, "handoff/cloud-dot-20261009/original-contract.md"),
                 identity(DISPATCH, PREFIX + "refreeze-after-B10-C-1/B11-downstream-contract.json"),
                 identity(DISPATCH, PREFIX + "refreeze-after-B10-C-1/affected-interface-map.json"),
                 identity(REVIEWED, PREFIX + "candidate-1/independent-review-dispatch.json"), identity(BASE, receipt_path),
                 identity(REVIEWED, PREFIX + "candidate-1/scope-amendment-receipt.json"),
                 identity(REVIEWED, PREFIX + "candidate-1/source-limits.json"),
                 identity(WRAPPER, PREFIX + "candidate-1/remote-readback.json"), identity(REVIEWED, "AGENTS.md"),
                 identity(BASE, "review/remediation/20261003-prepare/batches/B09/candidate-2/source-limits.json")]
proposals = obj(REVIEWED, PREFIX + "candidate-1/public-registration-proposals.json")
assert proposals["public_files_modified"] is False and proposals["accepted_B11_contributions"] == 0
assert proposals["canonical_CLOSED_increment"] == 0
assert all(x["canonical_state"] == "OPEN" for x in proposals["rows"])
assert next(x for x in proposals["rows"] if x["id"] == "GIR-FD82-B018")["nonlocal_pending_contributors"] == ["B13"]
for owner in reports:
    assigned = next(x for x in dispatch["potential_affected_determinations"] if x["accepted_owner"] == owner)
    ids = assigned["scope"]["ids"]
    payload = {"role": assigned["role"], "reviewed_sha": REVIEWED, "baseline": BASE,
               "common_scope_checks": scope_check, "complete_qualified_control_checks": [x for x in control_checks if x["id"] in ids],
               "accepted_receipts": receipt_checks[owner], "accepted_report_reuse": reused[owner],
               "accepted_owner_preservation": owner_checks[owner], "catalog_protection": catalog_checks,
               "metadata_execution_only": True, "reference_execution": 0, "behavior_vectors_executed": 0}
    if owner == "B10":
        payload["family_pair_recounts"] = family_checks
        payload["B018_nonlocal_B13_pending_preserved"] = True
    if owner == "B09":
        payload["B019_context_control_checks"] = [x for x in control_checks if x["id"] == "GIR-FD82-B019"]
    emit(owner, "static-checks.json", payload)
    emit(owner, "identity.json", {"role": assigned["role"], "reviewed_sha": REVIEWED,
         "reviewed_tree": git("rev-parse", REVIEWED + "^{tree}").decode().strip(), "FIX_BASE": BASE,
         "management_dispatch_sha": DISPATCH, "publication_wrapper_sha_not_candidate": WRAPPER,
         "branch": git("branch", "--show-current").decode().strip(), "remote_url": git("remote", "get-url", "origin").decode().strip(),
         "common_inputs": shared_inputs, "qualified_controls": [x for x in control_checks if x["id"] in ids],
         "exact_accepted_evidence_reused": reused[owner], "role_input_identities": owner_checks[owner],
         "candidate_formal_identities": formal_identities, "self_commit_identity": "Externally supplied after commit; no recursive self-hash refill."})
print(json.dumps({"reviewed_sha": REVIEWED, "control_objects_exact": len(control_checks),
                  "changed_paths": len(changes), "formal_changed": scope_check["changed_formal_paths"],
                  "catalog_prefixes_preserved": len(catalog_checks), "families": [{k: x[k] for k in ["family_count", "pair_count", "direct_rows", "copy_statements", "copy_new_pairs"]} for x in family_checks],
                  "owners": {o: len(v) for o, v in owner_checks.items()}, "status": "STATIC_METADATA_VALIDATED_NOT_QUALITY_VERDICT"}, ensure_ascii=False))
