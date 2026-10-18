"""Serialize explicitly authored review atoms; never derive them from text."""
import datetime
import json
import pathlib
import sys

P = pathlib.Path(__file__).resolve().parent
data = json.loads((P / sys.argv[1]).read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
manual = json.loads((P / "manual-atomic-clauses.json").read_text())
old = json.loads((P / "old-locator-disposition.json").read_text())
by_id = {row["id"]: row for row in old["rows"]}
existing = {row["id"] for row in manual["rows"]}
for authored in data["rows"]:
    number = authored["number"]
    locator = f"CORE-C{number:04d}"
    row = by_id[locator]
    if "layout_reason" in authored:
        row.update({"decomposition": "MANUAL_NONBEHAVIOR_TYPE_DISPOSITION", "all_children_received": True,
                    "status": "LAYOUT_SCOPE_OR_NAVIGATION_ONLY", "manual_type_reason": authored["layout_reason"], "missing_action": []})
        continue
    ids = []
    for index, assertion in enumerate(authored["children"], 1):
        ident = f"CAR-C{number:04d}-{index:02d}"
        ids.append(ident)
        if ident in existing:
            raise ValueError("manual atom already frozen: " + ident)
        source_units = [dict(data["source_dictionary"][x]) if isinstance(x, str) else x for x in authored["source_units"]]
        manual["rows"].append({
            "id": ident, "old_locator": locator,
            "spec": {"path": row["original"]["path"], "range": row["original"]["range"]},
            "assertion": assertion,
            "source_units": source_units,
            "premise": authored.get("premise", data["common_premise"]),
            "producer_write_consumer_chain": authored["chain"],
            "support": authored.get("support", "SUPPORTED_BOUNDED_SOURCE_STATIC"),
            "pending_consumers": authored.get("open", []),
            "cancel": authored.get("cancel", data["common_cancel"]),
            "exception_partial_commit": authored.get("failure", data["common_failure"]),
            "persistence_reload": authored.get("persistence", data["common_persistence"]),
            "evidence": "SOURCE_STATIC", "business_execution": "NOT_EXECUTED", "manual_authored_utc": now,
            "authoring_packet": sys.argv[1],
        })
    pending = authored.get("open", [])
    row.update({"manual_atom_ids": ids, "decomposition": "MANUAL_BY_ACTUAL_SEMANTIC_CHILDREN",
                "all_children_received": not pending and authored.get("support") not in ["EXISTING_ROOT_REQUIRED_BOUNDED", "CANDIDATE_REQUIRES_OTHER_REVIEW"],
                "status": authored.get("support") or ("OPEN_EXACT_FOREIGN_RECEIVER" if pending else "RECEIVED_BOUNDED_SOURCE_STATIC"),
                "missing_action": pending})
manual.update({"updated_utc": now, "frozen_subset": len(manual["rows"]), "global_atomic_denominator": "NOT_FROZEN"})
(P / "manual-atomic-clauses.json").write_text(json.dumps(manual, ensure_ascii=False, indent=2) + "\n")
(P / "old-locator-disposition.json").write_text(json.dumps(old, ensure_ascii=False, indent=2) + "\n")
progress = json.loads((P / "progress.json").read_text())
progress.update({"updated_utc": now, "manual_atomic_frozen_subset": len(manual["rows"]),
                 "manual_locator_frozen_subset": sum(bool(x["manual_atom_ids"]) for x in old["rows"]),
                 "old_layout_disposed": sum(x["status"] == "LAYOUT_SCOPE_OR_NAVIGATION_ONLY" for x in old["rows"]),
                 "old_bounded_source_received": sum(x["status"] == "RECEIVED_BOUNDED_SOURCE_STATIC" for x in old["rows"]),
                 "old_locators_complete": sum(x["all_children_received"] for x in old["rows"]),
                 "global_atomic_denominator": "NOT_FROZEN"})
(P / "progress.json").write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n")
gaps = json.loads((P / "coverage-gaps.json").read_text())
gaps.update({"updated_utc": now,
             "undecomposed_exact_ids": [x["id"] for x in old["rows"] if x["decomposition"] == "OPEN_NOT_MANUALLY_DECOMPOSED"],
             "decomposed_but_foreign_join_open": [x["id"] for x in old["rows"] if x["manual_atom_ids"] and not x["all_children_received"]],
             "manual_decomposed_locator_subset": [x["id"] for x in old["rows"] if x["manual_atom_ids"]],
             "manual_atoms_frozen_subset": len(manual["rows"]), "atomic_denominator_frozen": False,
             "material_or_host_limit_for_available_unread": False})
(P / "coverage-gaps.json").write_text(json.dumps(gaps, ensure_ascii=False, indent=2) + "\n")
frontier = gaps["undecomposed_exact_ids"][0] if gaps["undecomposed_exact_ids"] else "OLD_LOCATORS_DECOMPOSED_ACTUAL_CONSUMERS_OPEN"
note_count = sum(x.get("record_type") in {"REVIEW_DEPENDENCY_NOTE", "RESOLVED_REVIEW_DEPENDENCY_NOTE"}
                 or x["id"] == "CAR-C0138-07" for x in manual["rows"])
progress.update({"current_old_locator_frontier": frontier,
                 "manual_rows_with_dependency_note_type": note_count,
                 "manual_behavior_or_scope_child_records": len(manual["rows"]) - note_count})
(P / "progress.json").write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n")
continuation = json.loads((P / "next-dispatch.json").read_text())
continuation.update({"updated_utc": now, "next_actual_old_locator": frontier, "current_primary_frontier": frontier,
                     "manual_atoms_now": len(manual["rows"]),
                     "manually_decomposed_locators_now": progress["manual_locator_frozen_subset"],
                     "layout_scope_history_dispositions_now": progress["old_layout_disposed"],
                     "undecomposed_locators_now": len(gaps["undecomposed_exact_ids"])})
(P / "next-dispatch.json").write_text(json.dumps(continuation, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"utc": now, "manual_atoms": len(manual["rows"]), "manual_locators": progress["manual_locator_frozen_subset"],
                  "layout": progress["old_layout_disposed"], "bounded_source_rows": progress["old_bounded_source_received"],
                  "undecomposed_old_locators": len(gaps["undecomposed_exact_ids"])}))
