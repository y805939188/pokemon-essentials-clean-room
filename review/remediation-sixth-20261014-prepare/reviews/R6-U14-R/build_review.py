#!/usr/bin/env python3
"""Package this independent review; do not edit any author or formal payload."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
BASE = "review/remediation-sixth-20261014-prepare/"
CAND = "12a35f0d4635524ab2148c0979a1a4d69eeb982e"
FORMAL = "8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
REF = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
PREP = "469a268b92daed7b4d28d7fd0da75520cbb7228f"

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

def load(path):
    return json.loads((ROOT / path).read_text())

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

def identity(commit, path):
    data = git("show", commit + ":" + path)
    entry = git("ls-tree", commit, "--", path).decode().split()
    return {"commit": commit, "path": path, "mode": entry[0], "type": entry[1],
            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "git_blob": entry[2]}

def main():
    contract = load(BASE + "contracts/R6-U14.json")
    handoff = load(BASE + "candidates/R6-U14/evidence/per-id-author-handoff.json")
    validation = load(BASE + "reviews/R6-U14-R/independent-validation.json")
    receiver = load(BASE + "candidates/R6-U14/evidence/integration-request.json")
    findings = {
        "R6-D-LZ-001": {"clauses": {"generic-kernel/wp08-localization.md": [[108, 110]]}, "reason": "新回源证明收集[92,10]与运行[92,110]不同；正常运行键命中、库存前写及取消/截断各自保留，显示换行不修查找。", "rebuttal": "规范化不把n转LF；查找先于显示；仅收集键语言译文的最小输入确实缺译，未推广全语料。"},
        "R6-D-LZ-002": {"clauses": {"generic-kernel/wp08-localization.md": [[58, 67]], "engine-overworld/wp15-resource-matching-and-audio.md": [[34, 34]], "user-interface/wp65-controls-help-appendix.md": [[28, 28], [52, 52]]}, "reason": "七键图、代表菜单/卡片和两基名具名消费先查语言再请求资源，固定背景和标签独立；女性卡另有存在性门。", "rebuttal": "图像不是只翻译标签；没有译后失败通用重试A，空译仍命中；观察资源身份，不认证媒体/像素。"},
        "R6-D-PBS-C05": {"clauses": {"generic-kernel/wp03-content-identity-and-schema.md": [[95, 104]], "creature-rpg/wp27-bag-and-item-storage.md": [[62, 62]], "pokemon-rules/wp43-types-accuracy-and-damage.md": [[163, 163]]}, "reason": "Item省复数独立Unnamed，Type/Move有限默认与显式对照正确；原值与语言显示分层。", "rebuttal": "既有编辑器Unnamed/???已覆盖，不再重复根因；混合显式/省略仍需有限新合同，价格/用途/类别威力旧门不变。"},
        "R6-D-PBS-C06": {"clauses": {"generic-kernel/wp03-content-identity-and-schema.md": [[118, 130]], "demo-dx/wp73-b-world-editors.md": [[123, 123]]}, "reason": "部分指标记录取自身五组默认，整条缺席才克隆；三组0,0/5,6/7,8可唯一推得。", "rebuttal": "查询不修已有部分字段；来源后缀、查询登记、PBS选路径/等值省略及已有布局不广播边界保持。"},
        "R6-D-PBS-C07": {"clauses": {"creature-rpg/wp18-creature-identity-species-ownership.md": [[181, 181]], "creature-rpg/wp30-growth-learning-and-friendship.md": [[40, 40], [186, 193]]}, "reason": "合法基础作者256通过非负域/物种验证并由成功创建直接保留；255/70/0对照和正常变化末端夹限正确。", "rebuttal": "PBS、编辑器、NPC成员、创建和后继变化分别观察；第三档不无限外推，异常未到末端不保证夹限。"},
        "R6-D-DATA-C01": {"clauses": {"generic-kernel/wp03-content-identity-and-schema.md": [[108, 108]], "generic-kernel/wp04-pbs-lifecycle.md": [[73, 73], [80, 82]]}, "reason": "省略/显式空/Other三例不同，单缺值元素登记后比较失败；限定蛋步先2→1后失败，未到额外步骤。", "rebuttal": "安全导航不保护内部缺值元素；不推全部列表或孵化失败，外层恢复/真实存档仍未知，旧省略默认仍正确。"},
    }
    per_id = []
    for record, author_record in zip(contract["scope_contracts"], handoff["per_id"]):
        name = record["id"]
        assert author_record["id"] == name
        note = findings[name]
        actual = author_record["minimum_revision_contract"]["actual_changed_files"]
        clauses = []
        for short, spans in note["clauses"].items():
            path = BASE + "candidates/R6-U14/mirror/deliverables/final-specification-set/" + short
            clauses.append({"payload": identity(CAND, path), "lines": spans})
        vectors = author_record["acceptance_and_regression"]["actual_vector_rows"]
        for vector in vectors:
            text = git("show", CAND + ":" + vector["path"]).decode().splitlines()[vector["line"] - 1]
            assert text.startswith("| " + vector["id"] + " |")
        per_id.append({
            "id": name,
            "identity_and_verdict": {"classification": "required", "severity": record["identity_and_verdict"]["severity"], "root_cause_key": record["identity_and_verdict"]["root_cause_key"], "aliases": record["aggregation_aliases"], "candidate_commit": CAND, "candidate_tree": validation["candidate_tree"], "verdict": "CANDIDATE_PASS", "evidence_level": "SOURCE_STATIC", "formal_acceptance": "NOT_GRANTED", "CLOSED": "NOT_REGISTERED"},
            "bidirectional_evidence": {"fixed_source": record["bidirectional_evidence"]["source"], "formal_before": record["bidirectional_evidence"]["formal"], "candidate_after": clauses, "necessary_consumers": record["bidirectional_evidence"]["necessary_consumers"], "actual_changed_files": actual, "new_source_reasoning": note["reason"], "new_rebuttal": note["rebuttal"], "original_negative_evidence": record["bidirectional_evidence"]["negative_evidence"], "original_counter_evidence_ids": record["bidirectional_evidence"]["counter_evidence_ids"]},
            "premises_and_counterexample": record["premises_and_counterexample"],
            "minimum_revision_contract": {"original_required_rule": record["minimum_revision_contract"]["rule"], "preserved_scope": record["minimum_revision_contract"]["preserve_correct_scope"], "independent_result": note["reason"], "required_minimum_revisions": []},
            "acceptance_and_regression": {"original_conditions": record["acceptance_and_regression"]["conditions_and_vectors"], "actual_vectors": vectors, "new_manual_result": "PASS_WITH_EXACT_PREMISES_SOURCE_STATIC_ONLY", "history_controls": author_record["acceptance_and_regression"]["historical_controls"], "new_history_review": "Full affected catalogs and old criteria/premises freshly reviewed; 118 pointers/78 premise fields faithfully recovered; old PASS not transferred", "reference_execution": "NOT_EXECUTED_THIS_REVIEW", "complete_host": "NOT_EXECUTED_THIS_REVIEW"},
            "independent_adjudication": {"original_root_decision": record["independent_adjudication"], "current_reviewer": "R6-U14-R delegated /root", "read_only_semantic_peer": "/root/independent_semantics", "read_only_history_peer": "/root/historical_audit", "new_counter_attempt": note["rebuttal"], "verdict": "PASS", "required_minimum_revisions": [], "actual_configuration_echo": "UNVERIFIED"},
            "dependencies_and_receivers": {"primary_batch": "R6-U14", "receiver": "R6-I", "receiver_source_thread": "01a10d94-84b9-759e-aa1d-edb0d9b6d0e2", "sole_public_writer": "parent integration root", "actual_file_batches": {f["formal_path"]: receiver["formal_file_receivers"][f["formal_path"]] for f in actual}, "nonblocking_domain_dependencies": record["dependencies_and_receivers"]["original_dependencies"], "candidate_diff": "candidate-diff.txt", "remaining_blocking_gates": contract["closure_gate"][1:], "administrative_sync": record["minimum_revision_contract"]["synchronization_original_contract"], "admin_order_advisory": "R6-I must distinguish semantic integrated review, required public synchronization, formal acceptance and CLOSED; no public acceptance before all required conditions"},
            "original_full_proposal": record["original_full_proposal"],
            "original_proposal_status_scope": record["original_proposal_status_scope"],
        })
    write("per-id-adjudication.json", {"schema": "r6.u14.independent-seven-group-review.v1", "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "prepare": PREP, "candidate": CAND, "per_id": per_id, "verdict": "CANDIDATE_PASS", "required_revisions": [], "integrated_pass": "NOT_GRANTED", "formal_acceptance": "NOT_GRANTED", "CLOSED": "NOT_REGISTERED"})
    formal = "deliverables/final-specification-set/"
    full = [
        ("creature-rpg/wp18-creature-identity-species-ownership.md", 383, 385, "independent_semantics PBS peer's specification reader"),
        ("creature-rpg/wp27-bag-and-item-storage.md", 221, 223, "independent_semantics PBS peer"),
        ("creature-rpg/wp30-growth-learning-and-friendship.md", 282, 286, "independent_semantics PBS peer's specification reader"),
        ("demo-dx/wp73-b-world-editors.md", 217, 219, "independent_semantics PBS peer's specification reader"),
        ("engine-overworld/wp15-resource-matching-and-audio.md", 220, 222, "independent_semantics"),
        ("generic-kernel/wp03-content-identity-and-schema.md", 344, 364, "R6-U14-R /root; paired complete candidate plus all baseline preimages"),
        ("generic-kernel/wp04-pbs-lifecycle.md", 279, 283, "R6-U14-R /root; paired complete candidate plus all baseline preimages"),
        ("generic-kernel/wp08-localization.md", 214, 231, "R6-U14-R /root paired read; independent_semantics complete candidate"),
        ("pokemon-rules/wp43-types-accuracy-and-damage.md", 188, 190, "independent_semantics PBS peer"),
        ("test-catalog/creature-rpg-wp18-20-24-25-26.md", 308, 321, "historical_audit catalog peer"),
        ("test-catalog/creature-rpg-wp27-28-29-30-33.md", 314, 326, "historical_audit catalog peer"),
        ("test-catalog/generic-kernel-wp02-03-04.md", 165, 184, "historical_audit"),
        ("test-catalog/generic-kernel-wp05-06-07-08-09-10.md", 265, 278, "historical_audit"),
        ("user-interface/wp65-controls-help-appendix.md", 59, 61, "independent_semantics"),
    ]
    full_rows = []
    for path, before, after, reader in full:
        bpath = formal + path
        cpath = BASE + "candidates/R6-U14/mirror/" + bpath
        assert len(git("show", FORMAL + ":" + bpath).decode().splitlines()) == before
        assert len(git("show", CAND + ":" + cpath).decode().splitlines()) == after
        full_rows.append({"reader": reader, "formal": identity(FORMAL, bpath), "formal_full_range": [1, before], "candidate": identity(CAND, cpath), "candidate_full_range": [1, after], "read_method": "Actual complete text semantic read; root paired reading uses complete unchanged candidate text and every replaced baseline preimage; peer ranges are peer testimony, not root's physical full display"})
    root_ranges = {
        "Data/Scripts/001_Technical/003_Intl_Messages.rb": [[180, 215], [470, 500], [585, 615], [770, 795]],
        "Data/Scripts/021_Compiler/001_Compiler.rb": [[250, 293], [412, 438], [690, 740]],
        "Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb": [[30, 68], [181, 200], [292, 380], [543, 563]],
        "Data/Scripts/010_Data/002_PBS data/004_Ability.rb": [[1, 45]],
        "Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb": [[245, 268]],
        "Data/Scripts/010_Data/002_PBS data/003_Type.rb": [[16, 76]],
        "Data/Scripts/010_Data/002_PBS data/005_Move.rb": [[25, 96]],
        "Data/Scripts/010_Data/002_PBS data/006_Item.rb": [[119, 164]],
        "Data/Scripts/010_Data/002_PBS data/010_SpeciesMetrics.rb": [[1, 101]],
        "Data/Scripts/010_Data/002_PBS data/008_Species.rb": [[70, 80], [181, 206]],
        "Data/Scripts/014_Pokemon/001_Pokemon.rb": [[927, 970], [1159, 1227]],
        "Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb": [[1, 60]],
    }
    write("reading-and-independence.json", {
        "schema": "r6.u14.independent-reading-scope.v1", "utc_record_created": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "reviewer": "R6-U14-R delegated /root", "source_thread_id": "01a10d94-84b9-759e-aa1d-edb0d9b6d0e2",
        "requested": {"model": "gpt-6.1-sol", "effort": "ultra", "tier": "default", "speed": "default", "fast": False},
        "effective": {k: "UNVERIFIED" for k in ["model", "effort", "tier", "speed", "UUID"]},
        "independence": "Fresh non-author review; no candidate/formal/public-ledger mutation; peer authorship disjoint from candidate", "CLI_configuration_probe": False,
        "prompt": identity(PREP, BASE + "prompts/R6-U14-R.md"), "contract": identity(PREP, BASE + "contracts/R6-U14.json"),
        "complete_prompt_semantic_read": {"prose_ranges": [[1, 153], [6318, 6322]], "embedded_contract": "Full six records and all top fields read; exact repeated objects factored with references; byte-identical contract parsed and validated", "restoration_table": "All115 full records rendered with exact common fields/recovery pattern factored; no record omitted", "rendering_boundary": "Complete semantic content, not an assertion of one raw untruncated 6322-line output; initial truncated attempts excluded and missing pieces completed"},
        "full_formal_and_candidate_team_read_set": full_rows,
        "root_source_context_reads": [{"payload": identity(REF, p), "ranges": rr, "reader": "R6-U14-R /root"} for p, rr in root_ranges.items()],
        "original_reports_and_diagnostics": [identity("5210b009db5191f307301115845e31475cd798ef", "review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D/" + p) for p in ["localization/report.md", "pbs-bulk/report.md", "data-contract-counter/report.md", "localization/localized-image-matrix.json", "localization/newline-key-diagnostic.json", "counter-review.json", "counter-newline-bytes.json"]],
        "original_proposals": "All six full original proposals and seven-group contracts freshly read; scope corrections and historical pending status retained",
        "peer_source_scope": "See peer-findings.md for exact new ranges; full peer reads are distinguished from root context joins; no inherited author reading receipt",
        "early_read_metadata": "Per-read UTC/argv/stderr not separately captured in files for early platform tool reads; platform transcripts exist; no backfill frommtime or later runs",
        "execution": {k: 0 for k in ["reference_functions", "complete_gameplay_model", "host", "Demo", "real_save", "media", "production_services"]},
        "retained_failures": ["Initial parent cwd git status was outside repository; corrected to discovered path", "Initial missing frozen/source/history objects restored via ordinary fetch only", "Oversized contract/restoration/handoff displays truncated; not counted as full; lossless repeated-content rendering and full missing reads completed", "One independent NOT_EXECUTED per-row assertion invalid because section premises declare status; exit1 and corrected exit0 both in tool-attempts.jsonl", "Unauthenticated read-only api.github.com urllib attempt failed proxy tunnel403; no configuration/escalation; successful connector fallback", "Semantic peer first bareLF primitive construction omitted other slash normalization; corrected separately; not reference execution"],
        "remaining_limits": ["Effective task configuration/UUID echo unverified", "Complete host, pixels, serialization loader, real save, all unassigned consumers and arbitrary plugin combinations unexecuted", "Actual shared integration, integrated review, required public synchronization, formal acceptance and CLOSED pending parent"],
    })
    print(json.dumps({"per_id": len(per_id), "full_formal_candidate_pairs": len(full_rows), "verdict": "CANDIDATE_PASS", "required_minimum_revisions": 0}, ensure_ascii=False))

if __name__ == "__main__":
    main()
