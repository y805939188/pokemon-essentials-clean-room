"""Private exact-interface/refreeze navigation, not public registration."""
import hashlib
import json
import re
from prepare import BASE, PACKAGE, OUT, UI, CAT, FILES, blob, dump, identity, package, log_ranges


def main():
    imap = package("affected-interface-map.json")
    current = package("input-identities.json")
    b12_path = "review/remediation/20261003-prepare/batches/B12/refreeze-after-B15-C-1/B12-downstream-contract.json"
    b12 = json.loads(blob(PACKAGE, b12_path))
    b16read = {r["input"]["path"] for r in current["planned_reads"]}
    forwards = sorted(b16read.intersection(b12["allowed_formal_write_paths"]))
    b12read = {r["input"]["path"] for r in b12["planned_reads"]}
    reverses = sorted(b12read.intersection([v['path'] for v in current["formal_write_input_snapshots"]]))
    assert len(forwards) == 5 and len(reverses) == 2
    acceptance_path = "review/remediation/20261003-prepare/batches/B15/acceptance-stage-1/contribution-acceptance.json"
    accepted = json.loads(blob(BASE, acceptance_path))
    deps = []
    for n, r in enumerate(accepted["records"]):
        if r["id"] not in ["GIR-FD82-A055", "GIR-FD82-A056", "GIR-FD82-C122"]:
            continue
        short = r["id"].removeprefix("GIR-FD82-")
        deps.append({
            "id": r["id"], "B15_accepted_primary": r["primary"], "B16_primary": short != "A055",
            "accepted_scoped_record": {**identity(BASE, acceptance_path), "pointer": f"/records/{n}"},
            "candidate": r["reviewed_candidate"], "reviewed_actual": r["reviewed_actual"],
            "independent_FULL_actual": r["independent_FULL_actual_disposition"],
            "specific_minimum_receipt_basis": r["specific_minimum_receipt_basis"],
            "accepted_contributors": r["accepted_contributors"], "pending_contributors": r["pending_contributors"],
            "canonical_state": r["canonical_state"],
            "B16_UI_work": {"A055": "Preserve four-state Start-before-filter/no-Cancel-rollback already correct UI and give precise UI design.",
                             "A056": "Correct UI third visible count; preserve length as completion input and give two-field/completion design.",
                             "C122": "Bring UI full form first-qualified-sex/structural label rules into alignment; preserve B31/B38/first-loop write, extend fold design."}[short],
            "acceptance_transfer": False,
        })
    dump("dependency-and-refreeze-plan.json", {
        "status": "PRIVATE_PREPARATION_NAVIGATION_NO_INDEPENDENT_DISPOSITION",
        "formal_input": BASE, "management_package": PACKAGE,
        "B15_dependency_records": deps,
        "dependency_UI_source_read": log_ranges(BASE, "deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md", "123-145"),
        "B12_gate": {
            "gate_kind": "Physical mutual reader/writer and shared qualified003; not new PLAN dependency",
            "B12_contract_identity": identity(PACKAGE, b12_path),
            "forward_five_B12_writes_B16_reads": [identity(BASE, p) for p in forwards],
            "reverse_two_B16_future_writes_B12_reads": [identity(BASE, p) for p in reverses],
            "shared_qualified_id": "GIR-FD82-003",
            "B12_full_author_and_B16_preparation_only_can_parallel": True,
            "B16_full_author_release": "Parent receives published exact B12 candidate/necessary affected/G/actual/C gates, then issues fresh B16 latest accepted exact baseline refreeze; no auto-transition from this branch.",
        },
        "accepted_interface_navigation": [{
            "batch": i["accepted_batch"], "reader_inputs": i["reverse_declared_reader_inputs"],
            "shared_whole_file_write_paths": i["shared_whole_file_write_paths"],
            "shared_control_IDs": i["shared_control_IDs"],
            "existing_scoped_receipts_preserved": i["relevant_accepted_scoped_receipts"],
            "new_author_disposition": None,
            "later_required_review_rule": "Exact changed clause/caller/data/premise/minimum determines bounded real impact. Candidate and actual decisions separate; whole filename or sharedID alone does not trigger full owner reapproval. Independent affected reviewers issue supported PASS_SCOPED or NOT_AFFECTED.",
        } for i in imap["potential_interfaces"]],
        "resumption_sequence": [
            "Parent supplies exact latest accepted formal baseline/tree after B12C with ordinary publication/readback and unchanged immutable original/approved controls or precisely registered amendments; management successor never replaces formal baseline.",
            "Bind new five B12-written forward inputs and two reverse reader interfaces; compare exact old/new bytes and affected clauses/callers/data/conditions including qualified003 and original sync; rebuild accepted map adding B12 and any genuinely new accepted impacts.",
            "Re-bind all formal write input snapshots/catalog locks and any original proposal target. Reuse unchanged source-range hashes/reference version and unchanged controls with provenance; update only changed inputs plus necessary callers. Retain old input artifacts as historical preparation, never relabel as new accepted snapshot.",
            "Preserve every accepted clause and all old catalog row identities/order/multiplicity/other-owner meanings. Revise only assigned local WP rows and register necessary new static designs; do not claim ID counts prove semantic preservation.",
            "Parent sole registrar confirms each exact original amendment before applying it. Independently judge whether qualified finding establishes an actual original extraction defect; correct originals stay intact. Original patches are alternatives per ID; combined per-file patches are one-pass suggestions, refresh before use.",
            "Fresh full B16 author writes authorized formal scope and candidate evidence; mandatory independent Ultra FULL every24 contribution/20 primary minimum plus required affected exact candidate gates. Repairs produce a new exact candidate and fresh required review.",
            "Parent sole G integrates on latest accepted baseline only after gates; bind exact actual/readback, independent Ultra FULL and separate real affected actual dispositions including full predecessor-to-actual and candidate-to-actual streams; sole C accepts scoped contributions only after actual gates. Global OPEN/closure remains governed by all contributors and final global Ultra.",
        ],
        "reuse_limit": "Identity is not semantic approval. Static expected cases are designs, not run tests. Source/asset/host/dynamic/Demo limits remain; no re-reading all history, recursive proofs, quota probes or additional purity checkpoints.",
        "canonical_required_OPEN": 229, "canonical_CLOSED": 0,
        "formal_author_started": False, "candidate_created": False, "G_performed": False,
        "independent_review_performed": False, "C_performed": False, "closure_performed": False,
    })
    text = blob(BASE, CAT).decode()
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        match = re.match(r'^\|\s*([A-Z][A-Za-z0-9_-]*[0-9][A-Za-z0-9_-]*)\s*\|', line)
        if match:
            rows.append({"ordinal": len(rows)+1, "line": n, "id": match.group(1),
                         "row_sha256": hashlib.sha256(line.encode()).hexdigest()})
    dump("catalog-preservation.json", {
        "status": "BASELINE_ROW_LOCK_ONLY_NO_CATALOG_WRITE",
        "catalog": identity(BASE, CAT), "all_old_table_rows_in_physical_order": rows,
        "row_counts_are_not_semantic_equivalence": True,
        "existing_rows_order_multiplicity_and_meaning_protected": True,
        "local_planned_edits_only": ["T01时序", "T03空非空分支保护", "T20 BGS", "T34屏幕", "T35预览", "CH换页", "PT A23/A31/A33前提", "PT A32空重学", "PT A38选择器中立化", "PT A40旧源失败", "BX交换held/区域计数/标尺/locale/性别折叠/背景", "BG C05保存索引", "BG C24有限槽回退", "BG C29正确半价×数量保护"],
        "explicit_protected_acceptance": ["B31结构门", "B38首次循环写入", "B37过滤上下限哨兵", "B25/B26/B35 last-able guards", "A41盒写不回滚", "T06b语言整体系统对象写档", "T25b双退出可见性", "其他owner全部旧行"],
        "B12_crossing_catalog_is_distinct": "deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md",
        "later_refresh": "Bind new whole input/catalog and compare changed row meaning plus unfiltered row order/multiplicity; do not reuse baseline locks as a new accepted identity.",
    })


if __name__ == '__main__':
    main()
