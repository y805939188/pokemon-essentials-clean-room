#!/usr/bin/env python3
"""Read fixed Git objects and emit bounded, non-semantic mechanical evidence.

This helper does not issue an independent actual-integration review verdict.
It never evaluates source behavior, candidate prose, or PASS evidence semantics.
It does not execute Ruby, change Git refs, or write outside its own output JSON.
"""

import collections
import hashlib
import json
import pathlib
import re
import subprocess
import sys


REPO = pathlib.Path(__file__).resolve().parents[5]
BINDING = "56cc0f683249bd54658b94134d1a61be6e8748e0"
ARTIFACT = "49a558f7d5498680ba88d532f3815e07d7844459"
REGISTRATION = "3cc8e017c6629a0fc8cb0827bc16dda0e9adca91"
MANIFEST = (
    "review/remediation-eighth-20261016-prepare/integration/"
    "U01-U04-U05-U07-U08-U09/actual-review-input.json"
)
FORMAL = "deliverables/final-specification-set/"
R8 = "review/remediation-eighth-20261016-prepare/"
OUTPUT = pathlib.Path(__file__).with_name("mechanical-checks.json")


def git(*args, optional=False):
    p = subprocess.run(
        ["git", "-C", str(REPO), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if p.returncode:
        if optional:
            return None
        raise RuntimeError(
            f"git {' '.join(args)} returned {p.returncode}: "
            + p.stderr.decode(errors="replace").strip()
        )
    return p.stdout


def body(commit, path):
    return git("show", commit + ":" + path)


def obj(commit, path):
    raw = git("ls-tree", "-z", commit, "--", path)
    if not raw:
        return None
    meta, actual_path = raw.rstrip(b"\0").split(b"\t", 1)
    mode, kind, blob = meta.decode().split()
    if actual_path.decode() != path:
        raise RuntimeError("Unexpected ls-tree path")
    data = body(commit, path) if kind == "blob" else None
    return {
        "commit": commit,
        "path": path,
        "mode": mode,
        "type": kind,
        "blob": blob,
        **({"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()} if data is not None else {}),
    }


def tree(commit, prefix=""):
    raw = git("ls-tree", "-r", "-z", commit, "--", prefix)
    result = {}
    for item in raw.split(b"\0"):
        if not item:
            continue
        meta, path = item.split(b"\t", 1)
        mode, kind, blob = meta.decode().split()
        result[path.decode()] = {"mode": mode, "type": kind, "blob": blob}
    return result


def check_identity(record):
    actual = obj(record["commit"], record["path"])
    mismatches = {
        key: {"expected": record[key], "actual": actual.get(key) if actual else None}
        for key in ("mode", "blob", "bytes", "sha256")
        if key in record and (actual is None or actual.get(key) != record[key])
    }
    return {
        "commit": record["commit"], "path": record["path"],
        "actual": actual, "matches_identity": not mismatches,
        "mismatches": mismatches,
    }


def compare(left_commit, left_path, right_commit, right_path):
    left, right = obj(left_commit, left_path), obj(right_commit, right_path)
    return {
        "left": left, "right": right,
        "same_mode_and_blob": bool(left and right and left["mode"] == right["mode"] and left["blob"] == right["blob"]),
        "same_full_bytes": bool(left and right and body(left_commit, left_path) == body(right_commit, right_path)),
    }


def main():
    manifest = json.loads(body(BINDING, MANIFEST))
    baseline = manifest["fixed_delivery_commit"]
    b8 = manifest["B8"]
    actual_changes = json.loads(body(BINDING, manifest["actual_change_record_path"]))
    imports = json.loads(body(BINDING, R8 + "integration/U01-U04-U05-U07-U08-U09/import-identities.json"))
    output = {
        "schema": "r8-bounded-mechanical-evidence/v1",
        "qualification": "Mechanical helper only. No semantic reading claim or independent PASS/FAIL vote. Reviewer root must assess actual integration semantics separately.",
        "fixed_objects": {"binding": BINDING, "artifact": ARTIFACT, "registration": REGISTRATION, "baseline": baseline, "B8": b8},
        "input_manifest_identity": obj(BINDING, MANIFEST),
        "business_execution": "NOT_EXECUTED",
        "ruby_execution": "NOT_EXECUTED",
        "git_mutation": "NONE",
    }
    checks = []

    def claim(name, observed, expected):
        checks.append({"name": name, "observed": observed, "expected": expected, "matches": observed == expected})

    claim("artifact_commit_declared", manifest["artifact_snapshot_commit"], ARTIFACT)
    claim("artifact_workspace_tree", git("rev-parse", ARTIFACT + "^{tree}").decode().strip(), manifest["artifact_workspace_tree"])
    claim("artifact_formal_tree", git("rev-parse", ARTIFACT + ":" + FORMAL.rstrip("/")).decode().strip(), manifest["artifact_formal_tree"])
    claim("manifest_unchanged_at_registration", body(BINDING, MANIFEST), body(REGISTRATION, MANIFEST))
    # Avoid JSON-encoding binary values in the equality-only claim.
    checks[-1]["observed"] = hashlib.sha256(checks[-1]["observed"]).hexdigest()
    checks[-1]["expected"] = hashlib.sha256(checks[-1]["expected"]).hexdigest()
    claim("payload_identity_count", len(manifest["payload_identities"]), 264)
    output["payload_identities"] = [check_identity(i) for i in manifest["payload_identities"]]
    claim("all_payload_identities_match", all(i["matches_identity"] for i in output["payload_identities"]), True)
    claim("candidate_import_record_count", len(imports["records"]), 225)
    output["source_import_identities"] = []
    for r in imports["records"]:
        item = check_identity(r)
        item["artifact_equality"] = compare(r["commit"], r["path"], ARTIFACT, r["path"])
        output["source_import_identities"].append(item)
    claim("all_source_import_identities_match", all(i["matches_identity"] for i in output["source_import_identities"]), True)
    claim("all_source_imports_preserve_bytes", all(i["artifact_equality"]["same_mode_and_blob"] and i["artifact_equality"]["same_full_bytes"] for i in output["source_import_identities"]), True)

    output["targets"] = []
    all_paths = []
    required, optionals = [], []
    for batch in manifest["batches"]:
        required.extend(batch["required_ids"])
        optionals.extend(batch["selected_optional_ids"])
        identities = {r["path"]: r for r in batch["actual_target_identities"]}
        for path in batch["actual_target_paths"]:
            all_paths.append(path)
            output["targets"].append({
                "batch": batch["batch"],
                "target": path,
                "declared_actual_identity": check_identity(identities[path]),
                "candidate_mirror_equality": compare(batch["candidate_commit"], batch["candidate_mirror_prefix"] + path, ARTIFACT, path),
                "registration_equality": compare(ARTIFACT, path, REGISTRATION, path),
            })
    claim("required_ids_count", len(required), 16)
    claim("selected_optional_ids_count", len(optionals), 7)
    claim("target_count", len(all_paths), 25)
    claim("unique_target_count", len(set(all_paths)), 25)
    claim("all_actual_target_identities_match", all(i["declared_actual_identity"]["matches_identity"] for i in output["targets"]), True)
    claim("all_actual_targets_equal_fixed_candidate_mirrors", all(i["candidate_mirror_equality"]["same_mode_and_blob"] and i["candidate_mirror_equality"]["same_full_bytes"] for i in output["targets"]), True)
    claim("all_actual_targets_unchanged_at_registration", all(i["registration_equality"]["same_mode_and_blob"] and i["registration_equality"]["same_full_bytes"] for i in output["targets"]), True)
    u01 = next(b for b in manifest["batches"] if b["batch"] == "R8-U01")
    old_u01 = "bce1659e01ca33ecafb91464ce1ada32c0499faf"
    original_u01_review = "1a5c6dab85b6638403ef6e42bc97f23e842580b1"
    original_u01_prefix = R8 + "independent-reviews/R8-U01/cloud-independent-20261017/"
    original_u01_paths = sorted(tree(original_u01_review, original_u01_prefix))
    output["U01_revision_identity_checks"] = {
        "old_candidate": old_u01, "revised_candidate": u01["candidate_commit"],
        "old_mirror_tree": tree(old_u01, u01["candidate_mirror_prefix"]),
        "revised_mirror_tree": tree(u01["candidate_commit"], u01["candidate_mirror_prefix"]),
        "all_mirror_files": [compare(old_u01, p, u01["candidate_commit"], p) for p in sorted(tree(old_u01, u01["candidate_mirror_prefix"]))],
        "original_independent_review_files": [compare(original_u01_review, p, ARTIFACT, p) for p in original_u01_paths],
        "qualification": "Only candidate-tree equality and original review byte preservation are checked; root must interpret original FAIL versus revised PASS binding.",
    }
    claim("U01_four_mirror_paths", len(output["U01_revision_identity_checks"]["old_mirror_tree"]), 4)
    claim("U01_old_and_revised_mirror_tree_equal", output["U01_revision_identity_checks"]["old_mirror_tree"], output["U01_revision_identity_checks"]["revised_mirror_tree"])
    claim("U01_original_independent_review_files_retained", all(i["same_mode_and_blob"] and i["same_full_bytes"] for i in output["U01_revision_identity_checks"]["original_independent_review_files"]), True)
    output["actual_change_record_identity_checks"] = []
    for record in actual_changes["targets"]:
        item = {"batch": record["batch"], "target": record["target"]}
        for key in ("old_identity", "candidate_identity"):
            if record.get(key):
                item[key] = check_identity(record[key])
            else:
                item[key] = {"declared": record.get(key), "baseline_object": obj(baseline, record["target"])}
        item["new_sha256_matches_artifact"] = obj(ARTIFACT, record["target"])["sha256"] == record["new_sha256"]
        output["actual_change_record_identity_checks"].append(item)

    formal_baseline, formal_actual = tree(baseline, FORMAL), tree(ARTIFACT, FORMAL)
    formal_changed = sorted(p for p in set(formal_baseline) | set(formal_actual) if formal_baseline.get(p) != formal_actual.get(p))
    formal_unchanged = sorted(p for p in formal_actual if formal_baseline.get(p) == formal_actual[p])
    output["formal_preservation"] = {
        "formal_file_count": len(formal_actual), "changed_count": len(formal_changed), "unchanged_count": len(formal_unchanged),
        "changed_paths": formal_changed, "unchanged_paths": formal_unchanged,
        "added_paths": sorted(set(formal_actual) - set(formal_baseline)), "deleted_paths": sorted(set(formal_baseline) - set(formal_actual)),
    }
    claim("formal_file_total", len(formal_actual), 131)
    claim("formal_cumulative_changed", len(formal_changed), 26)
    claim("formal_cumulative_unchanged", len(formal_unchanged), 105)
    prior_manifest_path = R8 + "integration/U02-U03/actual-review-input.json"
    prior = json.loads(body(BINDING, prior_manifest_path))
    prior_paths = [b["actual_target_path"] for b in prior["batches"]]
    claim("formal_changed_set_is_six_batch_targets_plus_prior_two", formal_changed, sorted([p for p in all_paths if p.startswith(FORMAL)] + prior_paths))
    claim("all_formal_paths_unchanged_after_artifact", tree(ARTIFACT, FORMAL) == tree(REGISTRATION, FORMAL), True)

    historic_baseline = tree(baseline, "review/")
    historic_protected = {p: v for p, v in historic_baseline.items() if not p.startswith(R8)}
    historic_actual, historic_registration = tree(ARTIFACT, "review/"), tree(REGISTRATION, "review/")
    output["historical_review_protection"] = {
        "comparison_baseline": baseline,
        "rule": "Every baseline review path outside current eighth-remediation namespace is protected, including all R7 original histories.",
        "protected_existing_paths": len(historic_protected),
        "changed_or_missing_at_artifact": [p for p, value in historic_protected.items() if historic_actual.get(p) != value],
        "changed_or_missing_at_registration": [p for p, value in historic_protected.items() if historic_registration.get(p) != value],
    }
    claim("historical_review_preserved_at_artifact", output["historical_review_protection"]["changed_or_missing_at_artifact"], [])
    claim("historical_review_preserved_at_registration", output["historical_review_protection"]["changed_or_missing_at_registration"], [])
    output["reference_protection"] = {
        "baseline": tree(baseline, "reference/"), "artifact": tree(ARTIFACT, "reference/"), "registration": tree(REGISTRATION, "reference/")
    }
    claim("reference_tree_unchanged_at_artifact", output["reference_protection"]["baseline"], output["reference_protection"]["artifact"])
    claim("reference_tree_unchanged_at_registration", output["reference_protection"]["baseline"], output["reference_protection"]["registration"])
    output["root_AGENTS_protection"] = compare(baseline, "AGENTS.md", ARTIFACT, "AGENTS.md")
    claim("root_AGENTS_unchanged", output["root_AGENTS_protection"]["same_mode_and_blob"], True)
    remote = git("ls-remote", "--heads", "origin", "main").decode().strip()
    output["main_remote_readback"] = remote
    claim("remote_main_remains_B8", remote.split()[0] if remote else None, b8)

    output["prior_U02_U03_protection"] = {"prior_artifact": prior["artifact_snapshot_commit"], "targets": [], "payloads": [], "accepted_report_imports": []}
    for b in prior["batches"]:
        output["prior_U02_U03_protection"]["targets"].append({
            "batch": b["batch"],
            "artifact_equality": compare(prior["artifact_snapshot_commit"], b["actual_target_path"], ARTIFACT, b["actual_target_path"]),
            "registration_equality": compare(ARTIFACT, b["actual_target_path"], REGISTRATION, b["actual_target_path"]),
        })
    for r in prior["payload_identities"]:
        output["prior_U02_U03_protection"]["payloads"].append(compare(r["commit"], r["path"], ARTIFACT, r["path"]))
    acceptance_path = R8 + "acceptance/U02-U03/receipt.json"
    acceptance = json.loads(body(ARTIFACT, acceptance_path))
    output["prior_U02_U03_protection"]["acceptance_receipt_registration_equality"] = compare(ARTIFACT, acceptance_path, REGISTRATION, acceptance_path)
    for record in acceptance["records"]:
        for key in ("actual_independent_report_path", "actual_independent_result_path"):
            output["prior_U02_U03_protection"]["accepted_report_imports"].append(compare(record["actual_independent_report_commit"], record[key], ARTIFACT, record[key]))
    for key in ("targets", "payloads", "accepted_report_imports"):
        items = output["prior_U02_U03_protection"][key]
        if key == "targets":
            value = all(i[k]["same_mode_and_blob"] and i[k]["same_full_bytes"] for i in items for k in ("artifact_equality", "registration_equality"))
        else:
            value = all(i["same_mode_and_blob"] and i["same_full_bytes"] for i in items)
        claim("prior_U02_U03_" + key + "_unchanged", value, True)
    output["prior_U02_U03_protection"]["payload_equality_qualification"] = "Full prior-payload equality is an intentionally stronger comparator. Any changed live coordination file is reported for root interpretation; it is not itself a semantic finding or a changed accepted-target claim."

    def bound_pointers(value, pointer=""):
        found = []
        if isinstance(value, dict):
            for key, child in value.items():
                found.extend(bound_pointers(child, pointer + "/" + str(key).replace("~", "~0").replace("/", "~1")))
        elif isinstance(value, list):
            for index, child in enumerate(value):
                found.extend(bound_pointers(child, pointer + "/" + str(index)))
        elif isinstance(value, str) and (BINDING in value or ARTIFACT in value):
            found.append({"pointer": pointer, "value": value})
        return found

    registry_path = R8 + "coordination/task-registry.json"
    output["registration_fixed_object_references"] = {
        "commit": REGISTRATION, "path": registry_path,
        "identity": obj(REGISTRATION, registry_path),
        "matching_JSON_pointers": bound_pointers(json.loads(body(REGISTRATION, registry_path))),
        "reviewer_entry_identity": obj(BINDING, MANIFEST.replace("actual-review-input.json", "reviewer-entry.md")),
        "reviewer_entry_registration_equality": compare(BINDING, MANIFEST.replace("actual-review-input.json", "reviewer-entry.md"), REGISTRATION, MANIFEST.replace("actual-review-input.json", "reviewer-entry.md")),
    }
    publication_path = R8 + "publication/readback-56cc0f68.json"
    publication = json.loads(body(REGISTRATION, publication_path))
    output["registration_fixed_object_references"]["publication_readback_identity"] = obj(REGISTRATION, publication_path)
    output["registration_fixed_object_references"]["publication_readback_fixed_pointers"] = bound_pointers(publication)
    claim("registered_publication_published_commit", publication["published_commit"], BINDING)
    claim("registered_publication_six_batch_input_binding", publication["six_batch_input_binding_commit"], BINDING)
    claim("registered_publication_six_batch_artifact", publication["actual_group_artifact_commit"], ARTIFACT)

    catalog = FORMAL + "test-catalog/creature-rpg-wp35-36-57-64-68.md"
    id_regex = re.compile(r"\b(?:EG|EN|FC|TT|MG)-\d+\b")
    before_ids = id_regex.findall(body(b8, catalog).decode())
    after_ids = id_regex.findall(body(ARTIFACT, catalog).decode())
    id_counter = collections.Counter(after_ids)
    unique = set(after_ids)
    row_regex = re.compile(r"^\|\s*`?((?:EG|EN|FC|TT|MG)-\d+)`?\s*\|", re.MULTILINE)
    before_rows = row_regex.findall(body(b8, catalog).decode())
    after_rows = row_regex.findall(body(ARTIFACT, catalog).decode())
    output["creature_catalog_id_preservation"] = {
        "baseline": b8, "actual": ARTIFACT, "path": catalog,
        "id_regex": id_regex.pattern, "row_regex": row_regex.pattern,
        "baseline_all_id_occurrences": before_ids,
        "actual_all_id_occurrences": after_ids,
        "baseline_row_id_order": before_rows, "actual_row_id_order": after_rows,
        "unique_original_ID_total": len(unique),
        "unique_prefix_counts": dict(sorted(collections.Counter(i.split("-")[0] for i in unique).items())),
        "all_occurrence_count": len(after_ids),
        "all_ID_occurrence_counter_unchanged": collections.Counter(before_ids) == id_counter,
        "all_ID_occurrence_order_unchanged": before_ids == after_ids,
        "row_ID_order_unchanged": before_rows == after_rows,
        "MG32_all_occurrences": id_counter["MG-32"],
        "MG32_catalog_row_occurrences": after_rows.count("MG-32"),
        "ID_occurrence_order_sha256": hashlib.sha256("\n".join(after_ids).encode()).hexdigest(),
    }
    claim("creature_catalog_unique_original_total", len(unique), 127)
    claim("creature_catalog_unique_prefix_counts", output["creature_catalog_id_preservation"]["unique_prefix_counts"], {"EG": 20, "EN": 32, "FC": 17, "MG": 32, "TT": 26})
    claim("creature_catalog_all_occurrences_and_order_unchanged", before_ids == after_ids, True)
    claim("creature_catalog_MG32_exactly_one_row", after_rows.count("MG-32"), 1)
    output["checks"] = checks
    output["mechanical_anomalies"] = [c for c in checks if not c["matches"]]
    output["mechanical_match_count"] = sum(c["matches"] for c in checks)
    output["mechanical_check_count"] = len(checks)
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(OUTPUT.relative_to(REPO)), "mechanical_check_count": len(checks), "mechanical_match_count": output["mechanical_match_count"], "mechanical_anomalies": output["mechanical_anomalies"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
