#!/usr/bin/env python3
"""Pure mechanical source/issue/event/contribution mapping. Never semantic/FULL.

Read pinned local Git objects and the parent's existing complete identity evidence.
Write only new final-sync-mapping-* files in this directory. Never run old tools.
"""
import ast
import collections
import gzip
import hashlib
import io
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
OUT = pathlib.Path(__file__).resolve().parent
BINDING = "8ab43a609e60430492b219f0dce14ef4fdb8e47f"
ARTIFACT = "fd414a2c6ec0a0f746b48e0924e5692221ea5d5a"
BASE = "planning/implementation-routing/r8-20261017/"
PREP = "review/remediation-eighth-20261016-prepare/"
MANIFEST = PREP + "final/independent-review-input.json"
PAYLOAD = PREP + "final/payload-identities.json"
ROUTE = BASE + "routing-manifest.json"
EVENTS = BASE + "accepted-source-updates.json"
INDEX = PREP + "accepted-cumulative/batch-receipts.json"
ASSIGNMENT = "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batch-assignment.json"
FORMAL = "deliverables/final-specification-set/"
COMMANDS, SOURCES, CACHE, POINTERS, DIFFERENCES = [], [], {}, 0, []


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    COMMANDS.append({"command": ["git", *args], "cwd": str(ROOT), "returncode": result.returncode,
                     "stdout_bytes": len(result.stdout), "stdout_sha256": sha(result.stdout),
                     "stderr_bytes": len(result.stderr), "stderr": result.stderr.decode("utf-8", "replace")})
    if result.returncode:
        raise RuntimeError("read-only Git command failed: " + repr(args))
    return result.stdout


def raw(commit, path):
    key = (commit, path)
    if key not in CACHE:
        data = git("cat-file", "blob", commit + ":" + path)
        CACHE[key] = data
        SOURCES.append({"commit": commit, "path": path, "bytes": len(data), "sha256": sha(data),
                        "blob_computed_from_complete_bytes": hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()})
    return CACHE[key]


def parsed(commit, path):
    return json.loads(raw(commit, path))


def esc(key):
    return str(key).replace("~", "~0").replace("/", "~1")


def ptr(value, pointer):
    global POINTERS
    current = value
    if pointer:
        assert pointer.startswith("/")
        for token in pointer[1:].split("/"):
            key = token.replace("~1", "/").replace("~0", "~")
            current = current[int(key)] if isinstance(current, list) else current[key]
    POINTERS += 1
    return current


def save(name, value):
    path = OUT / ("final-sync-mapping-" + name)
    data = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()
    if len(data) > 1024 * 1024:
        buffer = io.BytesIO()
        with gzip.GzipFile(filename="", fileobj=buffer, mode="wb", compresslevel=9, mtime=0) as stream:
            stream.write(data)
        stored = buffer.getvalue()
        path = pathlib.Path(str(path) + ".gz")
        path.write_bytes(stored)
        assert gzip.decompress(path.read_bytes()) == data
        return {"logical_path": str(path.with_suffix("").relative_to(ROOT)), "plain_bytes": len(data), "plain_sha256": sha(data),
                "gzip_path": str(path.relative_to(ROOT)), "gzip_bytes": len(stored), "gzip_sha256": sha(stored), "gzip_mtime": 0,
                "full_bytes_equal_after_decompression": True}
    path.write_bytes(data)
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def main():
    manifest = parsed(BINDING, MANIFEST)
    payload = parsed(BINDING, PAYLOAD)
    route, updates, index = [parsed(ARTIFACT, path) for path in (ROUTE, EVENTS, INDEX)]
    assignment = parsed(manifest["fixed_delivery_commit"], ASSIGNMENT)
    contract = parsed(ARTIFACT, BASE + "backfill-contract.json")
    assert manifest["artifact_snapshot_commit"] == ARTIFACT and len(manifest["batches"]) == 9
    parent_path = OUT / "final-mechanical.json.gz"
    parent_stored = parent_path.read_bytes()
    parent_bytes = gzip.decompress(parent_stored)
    assert len(parent_bytes) == 12980999 and sha(parent_bytes) == "6b620ffc35671b53a747d9bb2876e9295e6e5edd1275c9b6ffea05215b0848a9"
    parent = json.loads(parent_bytes)
    for pointer, count in [("/payload_1008", 1008), ("/nine_batch_links", 9), ("/nine_batch_source_groups", 26), ("/tagging_175_and_review_75_plus111", 361)]:
        assert len(ptr(parent, pointer)) == count
    observed = {row["expected"]["path"]: (i, row["artifact_observed"]) for i, row in enumerate(parent["payload_1008"])}
    payload_positions = {row["path"]: i for i, row in enumerate(payload["files"])}
    events = {row["event_id"]: (i, row) for i, row in enumerate(updates["events"])}
    batches = {row["batch"]: (i, row) for i, row in enumerate(index["records"])}
    planned = {row["id"]: (i, row) for i, row in enumerate(assignment["batches"])}
    assert len(events) == len(batches) == len(planned) == 9
    issue_rows, contributions, source_bindings, required, optional = [], [], [], [], []
    for batch_index, batch_manifest in enumerate(manifest["batches"]):
        batch = batch_manifest["batch"]
        index_i, record = batches[batch]
        index_pointer = "/records/" + str(index_i)
        assert ptr(index, index_pointer) is record
        manifest_pointer = "/batches/" + str(batch_index)
        assert ptr(manifest, manifest_pointer) is batch_manifest
        ref = record["acceptance_receipt"]
        assert batch_manifest["batch_ACCEPTED_receipt"] == ref
        receipt = parsed(ref["commit"], ref["path"])
        receipt_record = ptr(receipt, ref["record_pointer"])
        assert receipt_record["batch"] == batch
        assert record["required_ids"] == receipt_record["required_ids"] == batch_manifest["required_ids"]
        assert record["required_ids"] == planned[batch][1]["required_ids"]
        assert record["candidate_commit"] == receipt_record["candidate_commit"] == batch_manifest["candidate_commit"]
        assert record["accepted_actual_snapshot"] == receipt_record["actual_artifact_commit"] == batch_manifest["actual_integration_commit"]
        targets_key = "actual_target_identities" if "actual_target_identities" in receipt_record else "actual_target_identity"
        receipt_targets = receipt_record[targets_key] if targets_key.endswith("identities") else [receipt_record[targets_key]]
        assert record["accepted_targets"] == receipt_targets
        assert set(batch_manifest["actual_target_paths"]) == {row["path"] for row in receipt_targets}
        selected_present = "selected_optional_ids" in receipt_record
        assert record["selected_optional_ids"] == receipt_record.get("selected_optional_ids", [])
        if not selected_present:
            DIFFERENCES.append({"kind": "source_field_absent_index_empty_projection", "batch": batch,
                                "receipt_path": ref["path"], "receipt_record_pointer": ref["record_pointer"],
                                "source_field": "selected_optional_ids", "index_value": record["selected_optional_ids"],
                                "source_field_is_absent": True, "unresolved": False})
        if record.get("formal_delta") != receipt_record.get("formal_delta"):
            DIFFERENCES.append({"kind": "formal_delta_label_projection", "batch": batch,
                                "receipt_field_present": "formal_delta" in receipt_record,
                                "receipt_value": receipt_record.get("formal_delta"), "index_value": record.get("formal_delta"), "unresolved": False})
        batch_events = [(i, e) for i, e in events.values() if e["batches"] == [batch]]
        assert len(batch_events) == 1
        event_i, event = batch_events[0]
        event_pointer = "/events/" + str(event_i)
        assert ptr(updates, event_pointer) is event
        assert event["required_ids"] == record["required_ids"]
        assert "selected_optional_ids" not in event
        assert event["commit"] == record["accepted_actual_snapshot"]
        assert set(event["documents"]) == {row["path"] for row in receipt_targets}
        assert event["evidence"][0] == {"commit": ref["commit"], "path": ref["path"]}
        assert event["receipt_record_pointer"] == ref["record_pointer"]
        for manifest_key, index_key in [("candidate_review_report", "candidate_independent_review"), ("actual_integrated_review_report", "actual_independent_review")]:
            for key in ("commit", "report_path", "result_path"):
                assert batch_manifest[manifest_key][key] == record[index_key][key]
        for evidence in event["evidence"]:
            raw(evidence["commit"], evidence["path"])
        binding = {"batch": batch, "final_manifest_pointer": manifest_pointer, "cumulative_index_pointer": index_pointer,
                   "original_receipt": {"commit": ref["commit"], "path": ref["path"], "record_pointer": ref["record_pointer"]},
                   "event_pointer": event_pointer, "event_id": event["event_id"], "actual_source_commit": event["commit"],
                   "candidate_manifest_identity_verbatim": batch_manifest["candidate_manifest_identity"],
                   "candidate_review_verbatim": batch_manifest["candidate_review_report"],
                   "actual_review_verbatim": batch_manifest["actual_integrated_review_report"],
                   "event_evidence_verbatim": event["evidence"], "required_ids": record["required_ids"],
                   "selected_optional_ids": record["selected_optional_ids"], "selected_optional_field_present_in_original": selected_present,
                   "target_contribution_count": len(receipt_targets),
                   "parent_existing_nine_batch_link_pointer": "/nine_batch_links/" + str(next(i for i, row in enumerate(parent["nine_batch_links"]) if row["batch"] == batch))}
        ptr(parent, binding["parent_existing_nine_batch_link_pointer"])
        source_bindings.append(binding)
        for issue_kind, key in [("required", "required_ids"), ("selected_optional", "selected_optional_ids")]:
            for issue_i, issue in enumerate(record[key]):
                target_list = required if issue_kind == "required" else optional
                target_list.append(issue)
                issue_pointer = index_pointer + "/" + key + "/" + str(issue_i)
                assert ptr(index, issue_pointer) == issue
                original_pointer = ref["record_pointer"] + "/" + key + "/" + str(issue_i)
                assert ptr(receipt, original_pointer) == issue
                row = {"issue_id": issue, "kind": issue_kind, "batch": batch, "cumulative_index_pointer": issue_pointer,
                       "original_receipt_commit": ref["commit"], "original_receipt_path": ref["path"], "original_receipt_pointer": original_pointer,
                       "event_id": event["event_id"], "event_pointer": event_pointer,
                       "mapping_granularity": "Recorded issue-to-batch membership. Batch targets are not asserted to be every issue's individual affected documents."}
                if "per_ID_actual_decisions" in receipt_record:
                    decisions = receipt_record["per_ID_actual_decisions"]
                    row["per_ID_actual_decisions_original_shape"] = type(decisions).__name__
                    matches = [(str(j), value) for j, value in enumerate(decisions) if value.get("id") == issue] if isinstance(decisions, list) else [(esc(issue), decisions[issue])] if issue in decisions else []
                    assert len(matches) == 1
                    if matches:
                        decision_index, decision = matches[0]
                        decision_pointer = ref["record_pointer"] + "/per_ID_actual_decisions/" + decision_index
                        row["explicit_per_ID_record_pointer"] = decision_pointer
                        row["explicit_per_ID_record_verbatim"] = ptr(receipt, decision_pointer)
                        carrier = decision["contract"]
                        carrier_doc = parsed(carrier["carrier_commit"], carrier["carrier_path"])
                        carrier_record = ptr(carrier_doc, carrier["carrier_pointer"])
                        assert carrier_record["id"] == issue
                        compact_sha = sha(json.dumps(carrier_record, ensure_ascii=False, separators=(",", ":")).encode())
                        assert compact_sha == carrier["parsed_value_canonical_sha256"]
                        row["explicit_per_ID_contract_pointer_dereferenced_ID_and_compact_hash_equal"] = True
                issue_rows.append(row)
        for target_i, identity in enumerate(receipt_targets):
            target_pointer = index_pointer + "/accepted_targets/" + str(target_i)
            assert ptr(index, target_pointer) == identity
            receipt_target_pointer = ref["record_pointer"] + "/" + targets_key + ("/" + str(target_i) if targets_key.endswith("identities") else "")
            assert ptr(receipt, receipt_target_pointer) == identity
            data = raw(identity["commit"], identity["path"])
            tree = git("ls-tree", "-z", identity["commit"], "--", identity["path"]).split(b"\0")[0]
            prefix, actual_path = tree.split(b"\t", 1)
            mode, kind, blob = prefix.decode().split()
            assert actual_path.decode() == identity["path"] and kind == "blob"
            source_observed = {"commit": identity["commit"], "path": identity["path"], "mode": mode, "blob": blob, "bytes": len(data), "sha256": sha(data)}
            assert source_observed == identity
            parent_i, current = observed[identity["path"]]
            current_ptr = "/payload_1008/" + str(parent_i) + "/artifact_observed"
            assert ptr(parent, current_ptr) == current
            payload_ptr = "/files/" + str(payload_positions[identity["path"]])
            assert ptr(payload, payload_ptr)["sha256"] == current["sha256"]
            matches = all(identity[key] == current[key] for key in ("mode", "blob", "bytes", "sha256"))
            contributions.append({"batch": batch, "path": identity["path"], "formal_path": identity["path"].startswith(FORMAL),
                                  "index_target_pointer": target_pointer, "original_receipt_target_pointer": receipt_target_pointer,
                                  "original_receipt_commit": ref["commit"], "original_receipt_path": ref["path"],
                                  "accepted_identity": identity, "accepted_source_complete_bytes_observed": source_observed,
                                  "current_identity_reused_from_parent_full_byte_audit": current,
                                  "parent_audit_pointer": current_ptr, "fixed_payload_pointer": payload_ptr,
                                  "accepted_identity_equals_current": matches})
    assert len(required) == len(set(required)) == 29
    assert len(optional) == len(set(optional)) == 10 and not set(required) & set(optional)
    assert len(issue_rows) == 39 and len(contributions) == 40
    paths = {row["path"] for row in contributions}
    assert len(paths) == 39
    formal = [row for row in contributions if row["formal_path"]]
    assert len(formal) == 39 and len({row["path"] for row in formal}) == 38
    nonformal = [row for row in contributions if not row["formal_path"]]
    assert len(nonformal) == 1 and nonformal[0]["batch"] == "R8-U07"
    stale = [row for row in contributions if not row["accepted_identity_equals_current"]]
    assert len(stale) == 1 and stale[0]["batch"] == "R8-U01" and stale[0]["path"].endswith("/wp65-title-load-options-pause-and-pc.md")

    docs = {row["document_id"]: row for row in route["documents"]}
    active_ids = {row["feature_id"] for row in route["features"]}
    retired_ids = {row["feature_id"] for row in route["retired_features"]}
    metadata_ids = {row["metadata_id"] for row in route["metadata_records"]}
    assert len(active_ids) == 736 and len(retired_ids) == len(metadata_ids) == 33 and not active_ids & retired_ids
    all_rows, bound = [], []
    collection_counts, event_counts, batch_counts, issue_counts = {}, collections.Counter(), collections.Counter(), collections.Counter()
    for collection, idkey in [("features", "feature_id"), ("retired_features", "feature_id"), ("metadata_records", "metadata_id"), ("documents", "document_id")]:
        current_rows = []
        for i, row in enumerate(route[collection]):
            pointer = "/" + collection + "/" + str(i)
            assert ptr(route, pointer) is row
            doc = docs[row["document_id"]]
            source_path = row["source"].get("document", row["source"].get("path"))
            assert source_path == doc["source"]["path"]
            entry = {"collection": collection, "record_id": row[idkey], "record_pointer": pointer,
                     "document_id": row["document_id"], "source_pointer": pointer + "/source", "source_verbatim": ptr(route, pointer + "/source")}
            if "current_applicability" in row:
                entry["current_applicability_pointer"] = pointer + "/current_applicability"
                entry["current_applicability_verbatim"] = ptr(route, entry["current_applicability_pointer"])
            if "upstream" in row:
                upstream = ptr(route, pointer + "/upstream")
                entry.update(upstream_pointer=pointer + "/upstream", upstream_verbatim=upstream)
                assert upstream["authority"] == {"commit": manifest["fixed_delivery_commit"], "path": ASSIGNMENT}
                assert set(upstream["batches"]) <= set(batches)
                assert set(upstream["required_ids"]) <= set(required)
                assert set(upstream["accepted_events"]) <= set(events)
                for event_id in upstream["accepted_events"]:
                    event = events[event_id][1]
                    assert source_path in event["documents"]
                    assert set(event["batches"]) <= set(upstream["batches"])
                if collection in ("features", "documents"):
                    expected_batches = {b for event_i, event in events.values() if source_path in event["documents"] for b in event["batches"]}
                    expected_batches |= {batch for batch, (j, plan) in planned.items() if source_path in plan.get("actual_target_write_set", [])}
                    expected_ids = {issue for batch in expected_batches for issue in planned[batch][1]["required_ids"]}
                    assert upstream["binding_basis"] == "DOCUMENT_WRITE_SET_CONSERVATIVE"
                    assert set(upstream["batches"]) == expected_batches and set(upstream["required_ids"]) == expected_ids
                    entry["actual_planned_plus_event_batch_set_equal"] = True
                    entry["required_ID_union_equal_fixed_assignment"] = True
                if collection == "features":
                    event_counts.update(upstream["accepted_events"])
                    batch_counts.update(upstream["batches"])
                    issue_counts.update(upstream["required_ids"])
                    if upstream["accepted_events"]:
                        assert upstream["status"] == "已回填ACCEPTED源规格；去向待独立复审"
                        bound.append(entry)
            if collection == "metadata_records":
                assert set(row["feature_refs"]) <= active_ids and set(row["retired_feature_ids"]) <= retired_ids
                entry["feature_refs_verbatim"] = row["feature_refs"]
                entry["retired_feature_ids_verbatim"] = row["retired_feature_ids"]
                entry["upstream_field_present"] = "upstream" in row
            if collection == "retired_features":
                assert row["retirement"]["metadata_record_id"] in metadata_ids
                assert set(row["retirement"]["replacement_feature_refs"]) <= active_ids
                entry["retirement_verbatim"] = row["retirement"]
            current_rows.append(entry)
        collection_counts[collection] = len(current_rows)
        all_rows.extend(current_rows)
    assert len(bound) == 230
    assert contract["current_applied_source"]["accepted_events"] == len(events)
    assert contract["current_applied_source"]["bound_active_rows"] == len(bound)
    assert sum(event_counts.values()) == 238 and sum(batch_counts.values()) == 238
    event_reverse = []
    for event_id, (i, event) in events.items():
        records = [row for row in all_rows if event_id in row.get("upstream_verbatim", {}).get("accepted_events", [])]
        event_reverse.append({"event_id": event_id, "event_pointer": "/events/" + str(i),
                              "batch_ids": event["batches"], "active_rows": [row["record_pointer"] for row in records if row["collection"] == "features"],
                              "document_rows": [row["record_pointer"] for row in records if row["collection"] == "documents"],
                              "other_rows": [row["record_pointer"] for row in records if row["collection"] not in ("features", "documents")]})
    script_rows = []
    for path in [BASE + "routing.py", BASE + "revisions/r3/tools/backfill-accepted-sources.py", BASE + "revisions/r3/tools/accepted-binding-regressions.py"]:
        data = raw(ARTIFACT, path)
        text = data.decode()
        tree = ast.parse(text, filename=path)
        lines = text.splitlines(keepends=True)
        script_rows.append({"path": path, "commit": ARTIFACT, "bytes": len(data), "sha256": sha(data), "complete_AST_parse": True, "executed": False,
                            "function_navigation": [{"name": node.name, "line_start": node.lineno, "line_end": node.end_lineno,
                                                     "complete_function_bytes_sha256": sha("".join(lines[node.lineno - 1:node.end_lineno]).encode())}
                                                    for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]})
    result = {"schema": "r8-final-sync-pure-mechanical-mapping-v1", "binding": BINDING, "artifact": ARTIFACT,
              "qualification": "MECHANICAL_MAPPING_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT",
              "source_document_roles": {"final_manifest": MANIFEST, "routing_manifest": ROUTE, "accepted_events": EVENTS,
                                        "accepted_cumulative_receipts": INDEX, "fixed_assignment": ASSIGNMENT},
              "reused_parent_identity_evidence": {"path": str(parent_path.relative_to(ROOT)), "plain_bytes": len(parent_bytes), "plain_sha256": sha(parent_bytes),
                                                    "gzip_bytes": len(parent_stored), "gzip_sha256": sha(parent_stored),
                                                    "pointers": ["/payload_1008", "/nine_batch_links", "/nine_batch_source_groups", "/tagging_175_and_review_75_plus111"]},
              "counts": {"batches": len(source_bindings), "required_issues": len(required), "selected_optional_issues": len(optional), "unique_issues": len(set(required + optional)),
                         "target_contributions": len(contributions), "unique_target_paths": len(paths), "formal_contributions": len(formal), "unique_formal_paths": len({row["path"] for row in formal}),
                         "nonformal_contributions": len(nonformal), "active_bound_rows": len(bound), "active_batch_references": sum(batch_counts.values()), "active_event_references": sum(event_counts.values()),
                         "collections": collection_counts, "explicit_pointer_dereferences": POINTERS},
              "nine_source_bindings": source_bindings, "issue_membership_39": issue_rows, "target_contributions_40": contributions,
              "all_source_and_upstream_record_references": all_rows, "bound_active_230": bound,
              "active_reverse_counts": {"batches": dict(batch_counts), "events": dict(event_counts), "required_issue_ids": dict(issue_counts)},
              "all9_event_reverse_navigation": event_reverse,
              "original_backfill_contract_pointer": "/current_applied_source", "original_backfill_contract_value_verbatim": ptr(contract, "/current_applied_source"),
              "source_scripts_complete_parse_navigation": script_rows,
              "observed_projection_distinctions": DIFFERENCES,
              "shared_WP65_historical_contribution_identity_difference": stale,
              "interpretation_limits": ["Event required_ids represent required29, not selected optional10; complete39 membership is preserved by original receipt/index arrays.",
                                        "U02/U03 missing selected_optional_ids fields remain recorded as absent; index empty arrays are not relabeled as original fields.",
                                        "40 is batch-to-target contribution count, with shared WP65 counted once for U01 and once for U04. Only39 unique paths and38 unique formal paths exist.",
                                        "U07 contributes one nonformal metadata target; no active formal feature row is inferred solely to give all9 events active references.",
                                        "Retired rows retain original upstream fields; their empty accepted_events are recorded without applying current-active acceptance rules.",
                                        "Issue-to-batch and batch-to-target relations are explicit. Their Cartesian product is not asserted as per-issue affected-document evidence."],
              "unresolved_mechanical_differences": [], "semantic_reader": False, "full_reading_credit": False, "configuration_verdict": None, "semantic_verdict": None}
    result["counts"]["explicit_pointer_dereferences"] = POINTERS
    output = save("result.json", result)
    save("summary.json", {"qualification": result["qualification"], "counts": result["counts"], "result_file": output,
                           "active_reverse_counts": result["active_reverse_counts"], "unresolved_mechanical_differences": [],
                           "read_only_git_commands": len(COMMANDS), "failures": sum(row["returncode"] != 0 for row in COMMANDS), "repairs": [],
                           "source_scripts_executed": False, "semantic_reader": False, "full_reading_credit": False})
    print(json.dumps({"result_file": output, "counts": result["counts"], "unresolved_mechanical_differences": []}, ensure_ascii=False))


if __name__ == "__main__":
    failure = None
    try:
        main()
    except BaseException as error:
        failure = {"type": type(error).__name__, "message": str(error)}
        raise
    finally:
        save("source-log.json", {"qualification": "MECHANICAL_MAPPING_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT",
                                  "commands": COMMANDS, "complete_sources_read": SOURCES, "failure": failure, "repairs": [],
                                  "old_evidence_scripts_executed": False, "Ruby_execution": False, "network_fetch": False,
                                  "read_only_reconnaissance_note": "Initial rg/source-shape discovery was followed by complete immutable Git source reads logged here. All asserted identities and pointers derive from those full reads and the pinned parent full-byte evidence."})
