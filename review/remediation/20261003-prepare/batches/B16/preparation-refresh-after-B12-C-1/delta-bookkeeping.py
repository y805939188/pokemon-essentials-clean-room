"""New finite Git/JSON/hash/text delta bookkeeping. Never import old programs.

No source, game, behavior vector, prior preparation/check/proposal or patch run.
"""
import hashlib
import json
import re
import subprocess
from pathlib import Path

BASE = "8e67f780c204d593d89f364f585d2c6c2fe74631"
TREE = "ae2f491294eb4f97be6b75f75706c16279f9bf46"
BEFORE = "1d06c45cc0a744fca181ac80ee573cc9ebb9b862"
PREP = "b48e919cce08058bcd29453232d4eb55aa9e9563"
PACKET = "e8caada4ab919e48e3dc817f0638ce595fde449c"
PFX = "review/remediation/20261003-prepare/batches/B16/refreeze-after-B12-C-1/"
OLD = "review/remediation/20261003-prepare/batches/B16/author-preparation-1/"
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
PREFIX = OUT.relative_to(ROOT).as_posix() + "/"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def data(commit, path):
    return git("show", commit + ":" + path)


def doc(commit, path):
    return json.loads(data(commit, path))


def packet(name):
    return doc(PACKET, PFX + name)


def blobid(commit, path):
    return git("rev-parse", commit + ":" + path).decode().strip()


def identity(commit, path):
    b = data(commit, path)
    return {"commit": commit, "path": path, "git_blob": blobid(commit, path),
            "sha256": hashlib.sha256(b).hexdigest(), "bytes": len(b)}


def digest(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True,
                                   separators=(",", ":")).encode()).hexdigest()


def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def verify_binding(b):
    actual = identity(b["commit"], b["path"])
    assert all(actual[k] == b[k] for k in actual), b["path"]
    return {**b, "identity_match": True}


def read_range(commit, path, lo, hi):
    ls = data(commit, path).splitlines(keepends=True)
    assert 1 <= lo <= hi <= len(ls)
    return {"commit": commit, "path": path, "lines": f"{lo}-{hi}",
            "range_sha256": hashlib.sha256(b"".join(ls[lo-1:hi])).hexdigest(),
            "kind": "BOUNDED_CURRENT_CALLER_TEXT_NOT_REFERENCE_EXECUTION"}


def main():
    assert git("rev-parse", BASE + "^{tree}").decode().strip() == TREE
    subprocess.run(["git", "merge-base", "--is-ancestor", BASE, PACKET], cwd=ROOT, check=True)
    d = packet("preparation-reuse-and-input-delta.json")
    inputs = packet("input-identities.json")
    contract = packet("B16-downstream-contract.json")
    dispatch = packet("author-dispatch.json")
    assert dispatch["own_author_evidence_scope"] == PREFIX
    assert dispatch["formal_input"] == BASE and not dispatch["full_author_allowed_now"]
    assert not contract["formal_writes_allowed_now"]
    assert d["published_preparation_commit"] == PREP
    assert d["previous_accepted_baseline"] == BEFORE and d["current_accepted_baseline"] == BASE
    changes = [x for x in d["planned_input_delta"] if x["changed"]]
    unchanged = [x for x in d["planned_input_delta"] if not x["changed"]]
    assert len(changes) == 5 and len(unchanged) == 69
    change_records = []
    whole_diff = b""
    for entry in changes:
        before = verify_binding(entry["before"])
        current = verify_binding(entry["current"])
        diff = git("diff", "--no-ext-diff", "--unified=0", BEFORE, BASE, "--", entry["path"])
        whole_diff += diff
        hunks = [{"before_start": int(m[0]), "before_count": int(m[1] or 1),
                  "current_start": int(m[2]), "current_count": int(m[3] or 1)}
                 for m in re.findall(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', diff.decode(), re.M)]
        assert hunks
        change_records.append({"path": entry["path"], "before": before, "current": current,
                               "full_five_input_diff_file": "changed-inputs.diff", "hunks_inspected": hunks,
                               "diff_sha256": hashlib.sha256(diff).hexdigest()})
    catalog_path = changes[4]["path"]
    prior_catalog_lines = data(BEFORE, catalog_path).decode().splitlines(keepends=True)
    current_catalog_lines = data(BASE, catalog_path).decode().splitlines(keepends=True)
    additions = [s for s in current_catalog_lines if s.startswith("| SF35 |")]
    assert len(additions) == 1
    assert [s for s in current_catalog_lines if not s.startswith("| SF35 |")] == prior_catalog_lines
    (OUT / "changed-inputs.diff").write_bytes(whole_diff)
    # Unchanged objects reuse their exact Git identities; no semantic re-reading.
    for entry in unchanged:
        b, c = entry["before"], entry["current"]
        assert blobid(b["commit"], b["path"]) == b["git_blob"] == c["git_blob"] == blobid(c["commit"], c["path"])
    assert len(d["preparation_files"]) == 40
    for f in d["preparation_files"]:
        assert f["commit"] == PREP and blobid(PREP, f["path"]) == f["git_blob"]
    formal = []
    for b in inputs["formal_write_input_snapshots"]:
        assert b["commit"] == BASE and blobid(BASE, b["path"]) == blobid(BEFORE, b["path"]) == b["git_blob"]
        formal.append({**b, "same_blob_as_B15_C": True, "semantic_preparation_reused": True})
    original_inputs = []
    for e in inputs["potential_original_sync_read_inputs"]:
        b = e["frozen_input"]
        assert blobid(BASE, b["path"]) == blobid(BEFORE, b["path"]) == b["git_blob"]
        original_inputs.append({**b, "same_blob_as_B15_C": True, "scope_amendment_received": False})
    old = doc(PREP, OLD + "contribution-analysis.json")
    controls = packet("original-and-acceptance-controls.json")["controls"]
    control_reuse = []
    wrapper_omissions = []
    assert len(controls) == 24 and sum(c["primary"] for c in controls) == 20
    for n, (c, prev) in enumerate(zip(controls, old["contributions"])):
        assert c["id"] == prev["id"] and c["primary"] == prev["primary"]
        assert c["whole_original_object_binding"] == prev["whole_original_object_binding"]
        assert c["whole_approved_acceptance_binding"] == prev["whole_approved_acceptance_binding"]
        cur = c["complete_current_control_fields"]
        before = prev["qualified_current_control"]
        same_object = cur == before
        if not same_object:
            assert set(before) - set(cur) == {"effective_case_constraints"}
            assert {k: v for k, v in before.items() if k != "effective_case_constraints"} == cur
            matches = []
            for case in before["effective_case_constraints"]:
                root_indices = [i for i, r in enumerate(cur["root_adjudications"])
                                if all(r.get(k) == v for k, v in case.items())]
                assert root_indices
                matches.append({"raw_id": case["raw_id"], "effective_constraint_sha256": digest(case),
                    "current_exact_root_pointer": f"/controls/{n}/complete_current_control_fields/root_adjudications/{root_indices[0]}"})
            wrapper_omissions.append({"id": c["id"], "omitted_aggregate_key": "effective_case_constraints",
                "prior_exact_field": {"commit": PREP, "path": OLD + "contribution-analysis.json",
                                       "pointer": f"/contributions/{n}/qualified_current_control/effective_case_constraints"},
                "prior_exact_field_sha256": digest(before["effective_case_constraints"]),
                "current_packet": {"commit": PACKET, "path": PFX + "original-and-acceptance-controls.json"},
                "all_effective_values_still_exact_in_current_root": matches,
                "semantic_scope_or_minimum_reduced": False,
                "action": "Preserve prior aggregate field by exact binding and current root; report packaging omission to parent for then-latest refreeze. No frozen package edit or new quality gate."})
        control_reuse.append({"id": c["id"], "primary": c["primary"],
            "old_analysis": {"commit": PREP, "path": OLD + "contribution-analysis.json", "pointer": f"/contributions/{n}"},
            "current_complete_control": {"commit": PACKET, "path": PFX + "original-and-acceptance-controls.json", "pointer": f"/controls/{n}"},
            "qualified_current_fields_sha256": digest(cur),
            "prior_complete_qualified_fields_sha256": digest(before),
            "whole_original_object_binding": c["whole_original_object_binding"],
            "whole_approved_acceptance_binding": c["whole_approved_acceptance_binding"],
            "complete_field_object_exact_equal": same_object,
            "all_substantive_qualified_values_and_effective_cases_preserved": True,
            "new_semantic_full_read": False, "B16_minimum_acceptance_completed": False})
    assert len(wrapper_omissions) == 12
    write("control-field-delta.json", {
        "status": "PRIVATE_WRAPPER_METADATA_OMISSION_PRESERVATION",
        "field_objects_exact_equal": 12, "field_objects_omitting_only_effective_aggregate": 12,
        "all_omitted_case_values_exactly_present_in_current_root": True,
        "original_and_approved_object_bindings_unchanged24": True,
        "no_new_qualified_behavior_minimum_or_recheck_change": True,
        "omissions": wrapper_omissions,
        "parent_action": "Keep complete prior controls and current root bindings; restore aggregate key or explicitly retain exact old-field provenance in next refreeze. No full re-reading, independent author verdict or edit to frozen management package.",
    })
    proposal_reuse = []
    assert len(d["unapproved_original_proposals"]) == 21
    for p in d["unapproved_original_proposals"]:
        assert not p["scope_amendment_received"] and not p["applied"]
        proposal_reuse.append({k: p[k] for k in ["id", "path", "before", "proposal_binding", "patch_binding", "patch_sha256", "proposed_after_sha256", "scope_amendment_received", "applied"]})
    write("refresh-manifest.json", {
        "status": "FINITE_PRIVATE_PREPARATION_DELTA_ONLY", "formal_input": BASE, "formal_input_tree": TREE,
        "management_package": PACKET, "package_is_not_formal_input": True,
        "previous_formal_input": BEFORE, "previous_preparation": PREP,
        "write_scope": PREFIX, "requested_configuration": dispatch["requested_configuration"],
        "effective_backend": "UNVERIFIED; no trusted echo, no substitution or configuration/quota audit",
        "changed_five": change_records, "unchanged69": unchanged,
        "reused40_preparation_files": d["preparation_files"],
        "old_files_imported_rewritten_or_reexecuted": False,
        "unchanged_future_formal6": formal, "unchanged_original5": original_inputs,
        "qualified24_primary20_reused": control_reuse,
        "original21_proposals_reused_not_approved": proposal_reuse,
        "preparation_does_not_satisfy_candidate_independent_actual_or_C_gates": True,
        "B13_full_author_hold": contract["operational_execution_gate"],
        "retained_source_limits_binding": identity(PACKET, PFX + "source-limits.json"),
        "retained_old_source_limits": identity(PREP, OLD + "source-limits.json"),
        "retained_old_source_reading_log": identity(PREP, OLD + "source-reading-log.json"),
        "retained_catalog_row_locks": identity(PREP, OLD + "catalog-preservation.json"),
        "reference": contract["reference"],
        "reference_or_behavior_or_old_program_execution": 0,
        "formal_writes": 0, "new_original_proposals": 0, "original_patches_checked_or_applied": 0,
        "candidate": False, "independent_review": False, "G": False, "C": False,
        "canonical_required_OPEN": 229, "canonical_CLOSED": 0,
    })
    analyses = [
      {"file": 0, "change": "AbilityRanking标题23→25；重复登记章节改为族+身份的最终行为，去来源行号组织锚点，保留FuryCutter基数/EchoedVoice效果分、RemoveProtections+7、PartingShot降阶及未登记默认。",
       "B16_interface": "共有003仅消费B12已接受的局部中立化边界。B16原T选项与A选择器/招式/奖章的组织泄漏仍待局部作者整改；不能要求复现同一内部登记表示，也不能丢兼容身份、评分阶段或失败。",
       "reuse": "旧003分析、源读范围和静态设计完整复用；新增B12接受方，不重定义全局003，不把B12 PASS移给B16。"},
      {"file": 1, "change": "OHKOIce失败门为冰目标拒绝后普通OHKO条件；目标失HP身份修正；移除错列整体评分身份；HealTargetDependingOnGrassyTerrain仅复制的出现记账；连续切割/解除保护最终行为保持。",
       "B16_interface": "这些是AI族/身份和出现表精确数据；不把AI失败预测写成UI拒选或实际招式结果，不改变摘要招式显示/学习选择器的前提。",
       "reuse": "旧UI及C126/其他全部本地设计不变；源程序版本未变，无新UI源码重读或运行。未来必要受影响独立门按实际修改判断。"},
      {"file": 2, "change": "新增默认GEOMANCY零目标的整体调用边界（非逐目标升阶/两回合偏好）；PainSplit移交WP46的实际平均/限值/恢复物品次序，AI局部未钳比例仍保留；测试数量63→67。",
       "B16_interface": "候选100/20不保证选中或执行，不推出HP/阶级/香草消费。PainSplit AI估量不得替代真实HP/物品变化；旧奶招A23恢复上限、学习/详情失败和所有UI表现设计不能从评分表重推。",
       "reuse": "B12已接受B017/B023结果作为当前领域边界；旧B16证据仍适用，不新增行为向量、不替代旧原稿C003/A23建议。"},
      {"file": 3, "change": "宝石的≤5明确为机制世代；撤退射击缺源跨族复制不改变目标降阶分，不能得到自换偏好；CE设计55→59。",
       "B16_interface": "评级/评分阶段不等于背包/队伍持物使用、消耗或换位提交。旧A044入口差异、BoxLink旧源索引C125部分写入与普通UI取消合同保持，不套用AI自换评分。",
       "reuse": "003局部接受接口更新；其它旧分析和21原稿提案不改。真实受影响审查仍由后来独立candidate/actual角色判断。"},
      {"file": 4, "change": "目录只追加SF35，旧SF01–SF34及其它旧行未改。有效大会缩为一员仍保留伙伴；伙伴真门先于一员假门，默认条件可走普通2v2，预算20/K不传不写；无伙伴/force-single且允许覆盖并无早接管才单敌大会接管。",
       "B16_interface": "WP65的Save/Safari退出/捕虫退出依据会话条件的100/010/001/011集合不改；不能由一员队伍推大会战斗接管、Ball菜单或消费。WP66A规则多选返回人数只说明选择结果，不抹去伙伴、force-single、allow-override及调用时点。",
       "reuse": "旧T25b、A27资格与nil边界、A41盒写入、A40/C125和未批准原稿补丁保持。SF35的Demo组合仍未证；B13后还需审查真实挑战报名/资格调用变化。"},
    ]
    for entry in analyses:
        idx = entry.pop("file")
        entry.update(change_records[idx])
        entry["author_delta_analysis_not_independent_affected_disposition"] = True
    t = "deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md"
    a = "deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md"
    write("input-delta-analysis.json", {
        "formal_input": BASE, "previous": BEFORE, "only_changed_input_hunks_semantically_refreshed": True,
        "unfiltered_five_input_diff": {"path": "changed-inputs.diff", "sha256": hashlib.sha256(whole_diff).hexdigest()},
        "inputs": analyses,
        "bounded_current_caller_reading": [read_range(BASE, t, 145, 156), read_range(BASE, a, 113, 114), read_range(BASE, a, 201, 201)],
        "current_callers_same_blob_as_before": True,
        "pokemon_rules_catalog_old_lines_order_multiplicity_and_bytes_preserved": True,
        "pokemon_rules_catalog_only_new_row": "SF35",
        "new_reference_ranges": [], "reference_reexecuted": False,
        "reused_old_evidence": {"commit": PREP, "source_log": OLD + "source-reading-log.json", "analysis": OLD + "contribution-analysis.json"},
        "minimum_and_full_qualified_control": "All24 exact bindings/current qualifications/root/extensions/effective premises/minimum/recheck remain at prior preparation and current package; no repeated full semantic consumption or historical proof chase.",
        "original21_semantic_effect": "No B12 change touches the five original/UI blobs or assigned local proposal clauses. Keep old fullpatch/proposed-after identities and nonapproval. Refresh later only on actual B13/new caller predicates; byte identity never conveys scope approval or quality acceptance.",
    })
    imap = packet("affected-interface-map.json")
    oldplan = doc(PREP, OLD + "dependency-and-refreeze-plan.json")
    oldbatches = {i["batch"] for i in oldplan["accepted_interface_navigation"]}
    added = [i for i in imap["potential_interfaces"] if i["accepted_batch"] not in oldbatches]
    assert {i["accepted_batch"] for i in added} == {"B01", "B12"}
    apath = "review/remediation/20261003-prepare/batches/B12/acceptance-stage-1/contribution-acceptance.json"
    accepted = doc(BASE, apath)
    receipt_binding = verify_binding(d["new_B12_acceptance_receipts"])
    records = []
    for n, r in enumerate(accepted["records"]):
        records.append({"id": r["id"], "primary": r["primary"], "canonical_state": r["canonical_state"],
                        "status": r["status"], "B12_scoped_record": {**receipt_binding, "pointer": f"/records/{n}"},
                        "candidate": r["reviewed_candidate"], "actual": r["reviewed_actual"],
                        "qualified_registration": r["qualified_registration"],
                        "independent_FULL_actual_disposition": r["independent_FULL_actual_disposition"],
                        "B16_acceptance_transfer": False})
    # Consume only new accepted local interface conclusions, not their old proof chains.
    reviewpath = "review/remediation/20261003-prepare/batches/B12/integration-review-1/review.json"
    review = doc(BASE, reviewpath)
    conclusions = []
    for n, r in enumerate(review["contributions"]):
        if r["id"] not in ["GIR-FD82-003", "GIR-FD82-B017", "GIR-FD82-B023", "GIR-FD82-B026"]:
            continue
        conclusions.append({"id": r["id"], "binding": {**identity(BASE, reviewpath), "pointer": f"/contributions/{n}"},
                            "accepted_local_minimum_judgment": r["actual_minimum_judgment"],
                            "accepted_positive_reverse_old_regression": r["actual_legal_positive_reverse_and_old_regression_judgment"],
                            "source": "Previously independent B12 actual conclusion consumed through published C; not author-issued reapproval."})
    write("accepted-interface-delta.json", {
        "formal_input": BASE, "old_interface_plan": identity(PREP, OLD + "dependency-and-refreeze-plan.json"),
        "current_map": identity(PACKET, PFX + "affected-interface-map.json"),
        "old11_navigation_reused": sorted(oldbatches), "current13_navigation": [i["accepted_batch"] for i in imap["potential_interfaces"]],
        "added_navigation": added,
        "B01_change": "Existing accepted generic-kernel reader recorded by current freezer; unchanged input, no sharedID/reverse writer. Navigation addition only, no new semantic obligation or independent NOT_AFFECTED issued.",
        "B12_scoped_records_consumed": records, "bounded_new_local_conclusions": conclusions,
        "shared_003": "Only B12 local contribution accepted; primary B21 and pending B13/B16/nonlocal duties remain. Preserve family/identity, final behavior and defaults while removing unnecessary organization. UI local controls do not inherit B12 PASS.",
        "B15_reuse": "A055/A056/C122 dependency records remain exact at prior preparation/current accepted payload. B16 UI work/20 primary minima remain unfulfilled.",
        "candidate_actual_affected_review_rule": "Determine necessary bounded affected reviews from real changed clause/caller/data/predicate or original required condition. Separate independent candidate/actual dispositions; filenames/sharedID alone do not require full old-owner reapproval. Author issues no PASS_SCOPED or NOT_AFFECTED.",
        "independent_B16_review_performed": False,
    })
    b13path = "review/remediation/20261003-prepare/batches/B13/refreeze-after-B12-C-1/B13-downstream-contract.json"
    b13 = doc(PACKET, b13path)
    readpaths = {i["input"]["path"] for i in contract["planned_reads"]}
    forward = sorted(readpaths.intersection(b13["allowed_formal_write_paths"]))
    reverse = sorted({i["input"]["path"] for i in b13["planned_reads"]}.intersection(contract["allowed_formal_write_paths"]))
    assert len(forward) == 4 and len(reverse) == 2
    sensitivities = {
        "wp54-entry-eligibility-level-adjustment-and-clauses.md": "Rule qualification/count/minimum, legal empty-list submission versus nil cancellation and failure phase; compare actual B13 changes against WP66A multi-entry startup/CONFIRM/BACK, A27/A33 premises without importing unrelated rule implementation.",
        "wp56-palace-and-arena-variants.md": "Participant/replacement lifecycle, Arena replenishment and retained state, replacement attack records; distinguish UI selected member/command from actual participant replacement and resets. Follow only changed predicate/caller branches, not all WP67/reference behavior.",
        "wp58-battle-recording-and-playback.md": "Recording/playback input and positional EXP/item restoration plus exceptions; distinguish selector return, stored party index/identity and later restoration. Preserve B16 partial-write/no-rollback and audio/display controls unless real B13 caller delta proves adjustment.",
        "creature-rpg-wp35-36-57-64-68.md": "Existing row IDs/order/multiplicity and decisive selection/encounter/facility premises. Keep other-owner C003 extensions independent of B16 PT A23/A31/A33; update only real changed rows, never add B030 as required scope.",
    }
    forward_records = []
    for path in forward:
        assert blobid(BASE, path) == blobid(BEFORE, path)
        forward_records.append({"current_input": identity(BASE, path), "unchanged_since_B15_C": True,
                                "sensitivity": sensitivities[path.rsplit('/', 1)[1]],
                                "after_B13_C": "Compare to then-latest published accepted C; refresh only actual input/condition change and necessary callers, reuse rest."})
    write("B13-sensitive-inputs.json", {
        "status": "FULL_B16_HELD_UNTIL_PARENT_REFREEZE_AND_EXPLICIT_RELEASE",
        "current_input": BASE, "current_tree": TREE, "B13_contract": identity(PACKET, b13path),
        "forward_four_B13_writes_B16_reads": forward_records,
        "reverse_two_B16_future_writes_B13_reads": [{"current_input": identity(BASE, path),
            "sensitivity": "Protect the exact B13 accepted caller/qualification/return/input facts when later editing WP65/WP66A; existing six payload input identities remain unchanged now. Separate necessary later independent candidate and actual affected B13 gates."} for path in reverse],
        "shared_qualified_control": "GIR-FD82-003", "shared_primary_owner": "B21",
        "B13_acceptance_focus_as_dispatched": b13["acceptance_focus"],
        "B030_not_required_and_not_in_B13_scope": b13["B030_not_required_and_not_in_B13_scope"],
        "release_condition": "B13 exact candidate/necessary affected/G/actual/C published with ordinary readback; parent refreezes then-latest accepted C/tree and real changed interfaces and explicitly releases full B16. This refresh never auto-transitions even if B13C arrives.",
        "then_latest_input_requirement": "Current B12C74/6 packet cannot be relabelled as then-latest full input. Preserve old40 and this finite delta with exact provenance, bind changed B13 inputs/accepted receipts and refreshed future output/catalog/original snapshots.",
        "future_remaining": "Full B16 assigned24/20 author evidence and independent Ultra FULL all24/20 plus necessary independent affected candidate; sole G then exact actual FULL/affected over both unfiltered streams; sole C thereafter. 21 originals require precise sole registrar amendment confirmation before application; all nonlocal/final-global obligations remain.",
    })
    # Publication self-check is bookkeeping only, not a quality gate or old test.
    changed = git("diff", "--name-only", BASE).decode().splitlines()
    untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
    assert all(p.startswith(PREFIX) for p in changed + untracked), (changed, untracked)
    for p in OUT.glob('*.json'):
        json.loads(p.read_text())
    subprocess.run(["git", "diff", "--check", BASE], cwd=ROOT, check=True)
    write("verification.json", {
        "status": "AUTHOR_PRIVATE_DELTA_BOOKKEEPING_SELF_CHECK_ONLY", "formal_input": BASE, "formal_tree": TREE,
        "five_changed_exact_before_current_blob_sha256_bytes": True,
        "69_unchanged_planned_inputs_same_git_blob": True,
        "40_original_preparation_git_bindings_reused": True,
        "24_substantive_qualified_values_preserved_and_binding_reuse": True,
        "complete_control_field_objects_exact_equal": 12,
        "aggregate_only_omissions12_exact_current_root_preservation": True,
        "formal6_original5_same_blob_as_B15_C": True,
        "21_proposals_no_scope_amendment_no_apply_no_dry_check": True,
        "B13_real_forward_reverse_intersection": "4/2 + shared qualified003",
        "old_programs_imported_or_executed": 0, "new_reference_semantic_ranges": 0,
        "reference_game_behavior_vectors_runtime_observations_proven_Demo": 0,
        "formal_original_candidate_public_main_history_writes": 0,
        "all_changes_in_dispatch_refresh_directory": True,
        "json_parse_and_git_diff_check": True, "new_independent_review_or_C": False,
        "remote_readback": "Returned externally after ordinary commit/push/ref+FETCH_HEAD/tree/all new output bytes readback; no recursive self hash.",
    })
    print("Finite5-input delta; reuse69/40/24; same6/5; proposals21 unapproved; B13 hold4/2+003. No old program, reference or behavior execution.")


if __name__ == "__main__":
    main()
