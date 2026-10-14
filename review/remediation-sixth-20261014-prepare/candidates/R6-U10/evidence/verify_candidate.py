"""Identity, scope, and preservation checks; does not execute reference behavior."""
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

PREP = "469a268b92daed7b4d28d7fd0da75520cbb7228f"
MAIN = "8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
REF = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
BRANCH = "codex/remediation-sixth-r6-u10-author-20261014"
ROOT = Path(__file__).resolve().parents[5]
BASE = "review/remediation-sixth-20261014-prepare"
OWN = BASE + "/candidates/R6-U10"
EVIDENCE = Path(OWN + "/evidence")
CONTRACT = BASE + "/contracts/R6-U10.json"
PROMPT = BASE + "/prompts/R6-U10-A.md"
STARTED = datetime.datetime.now(datetime.timezone.utc).isoformat()


def git(*args, data=None):
    return subprocess.check_output(["git", *args], input=data)


def show(ref, path):
    return git("show", ref + ":" + path)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(raw):
    return {"bytes": len(raw), "sha256": sha(raw),
            "git_blob": git("hash-object", "--stdin", data=raw).decode().strip()}


def write(name, value):
    (EVIDENCE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def canon(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":")).encode())


assert Path.cwd() == ROOT, (Path.cwd(), ROOT)
assert git("branch", "--show-current").decode().strip() == BRANCH
subprocess.run(["git", "merge-base", "--is-ancestor", PREP, "HEAD"], check=True)
prompt_raw = show(PREP, PROMPT)
contract_raw = show(PREP, CONTRACT)
assert identity(prompt_raw) == {
    "bytes": 233697, "sha256": "a12719578a2582f4760235fdf3139166895f58902171091819fb228fce897e11",
    "git_blob": "b788e4e277ad66832950440bc55b1afa2803073e"}
# The blob is derived and recorded; only the user-supplied prompt blob is normative.
assert len(contract_raw) == 120055
assert sha(contract_raw) == "eb86301b11ef040f4a98365b93d8a6649409f32fe095a13974e697fe160d64f0"
blocks = re.findall(rb"```json\n(.*?)\n```", prompt_raw, re.S)
assert blocks[0] + b"\n" == contract_raw
contract = json.loads(contract_raw)
assert contract["required_ids"] == ["R6-UI-001", "R6-UI-002", "R6-UI-PARTY-001", "R6-UI-PARTY-002"]

payloads = {}


def collect(value):
    if isinstance(value, dict):
        p = value.get("payload_identity")
        if isinstance(p, dict) and p.get("commit") in (MAIN, REF):
            payloads[(p["commit"], p["path"])] = p
        for child in value.values():
            collect(child)
    elif isinstance(value, list):
        for child in value:
            collect(child)


collect(contract)
bindings = []
for (commit, path), expected in sorted(payloads.items()):
    raw = show(commit, path)
    actual = identity(raw)
    for key in ("bytes", "sha256", "git_blob"):
        assert actual[key] == expected[key], (path, key)
    entry = git("ls-tree", commit, "--", path).decode().split()
    assert entry[:2] == [expected["mode"], "blob"]
    actual_tree = git("rev-parse", commit + (":deliverables/final-specification-set" if commit == MAIN else "^{tree}")).decode().strip()
    assert actual_tree == expected["tree"]
    bindings.append({"commit": commit, "tree": actual_tree, "path": path,
                     "mode": entry[0], "type": entry[1], **actual, "expected_match": True})

recovery = json.loads(blocks[1])
counter_bindings = []
for eid in contract["scope_contracts"][0]["bidirectional_evidence"]["counter_evidence_ids"]:
    expected = recovery[eid]
    path = BASE + "/inputs/evidence/" + expected["path"]
    actual = identity(show(PREP, path))
    assert all(actual[k] == expected[k] for k in ("bytes", "sha256", "git_blob")), eid
    counter_bindings.append({"evidence_id": eid, "recovery_commit": PREP,
                             "cached_path": path, "original_commit": expected["commit"],
                             "original_path": expected["recovery"].split(":", 1)[1],
                             **actual, "exact_cached_bytes_match": True})
write("input-bindings.json", {"prepare": PREP, "prompt": identity(prompt_raw),
    "contract": identity(contract_raw), "embedded_contract_exact_equal": True,
    "full_frozen_payload_bindings": bindings, "counter_evidence_bindings": counter_bindings,
    "original_R6_report_commit_locally_available": False,
    "cached_recovery_not_new_independent_review": True})

deliveries = [json.loads(line) for line in (EVIDENCE / "read-delivery.jsonl").read_text().splitlines()]
coverage = []
for path in contract["read_only_reference_paths"] + contract["candidate_formal_paths"]:
    commit = MAIN if path.startswith("deliverables/") else REF
    raw = show(commit, path)
    total = len(raw.decode("utf-8-sig").splitlines())
    ranges = [r for d in deliveries if d["path"] == path and d["ref"] == commit for r in d["ranges"]]
    seen = {line for first, last in ranges for line in range(first, last + 1)}
    required = set(range(1, 30)) if path == "PBS/pokemon.txt" else set(range(1, total + 1))
    assert required <= seen, (path, sorted(required - seen)[:10])
    coverage.append({"path": path, "commit": commit, **identity(raw), "total_lines": total,
                     "delivered_ranges": ranges, "required_unit": [1, 29] if path == "PBS/pokemon.txt" else [1, total],
                     "full_file_read": path != "PBS/pokemon.txt", "required_unit_fully_delivered": True,
                     "semantic_credit": "Author read exact bounded deliveries; delivery alone is not quality proof"})
write("read-coverage.json", {"coverage": coverage,
    "prompt_semantic_read": {"kind": "AUTHOR_SESSION_READ_ATTESTATION", "commit": PREP,
        "path": PROMPT, **identity(prompt_raw), "total_lines": 3770,
        "ranges": [[1,110],[111,300],[301,650],[651,1000],[1001,1370],[1371,1800],
                   [1801,2200],[2201,2640],[2641,3070],[3071,3500],[3501,3770]],
        "per_range_stdout_retained_locally": False, "utc_per_initial_range": None,
        "contract_credit": "Exact embedded contract bytes, completely read in those prompt intervals"},
    "projection_reads": "See json-read-delivery.jsonl; full selected records, not full containing carriers",
    "uncredited_truncated_attempts": "See tool-attempts.json"})

expected_removed = {
    "creature-rpg/wp18-creature-identity-species-ownership.md": [179],
    "creature-rpg/wp30-growth-learning-and-friendship.md": [42,228],
    "user-interface/wp66-a-party-and-summary-ui.md": [182,216],
    "user-interface/wp67-a-battle-interaction-and-presentation.md": [226,228,304],
    "test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md": []}
changed_payloads = []
preserved = []
formal_prefix = "deliverables/final-specification-set/"
catalog_path = formal_prefix + "test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md"
for path in contract["candidate_formal_paths"]:
    mirror = OWN + "/mirror/" + path
    before = show(PREP, mirror)
    assert before == show(MAIN, path), path
    after = Path(mirror).read_bytes()
    assert before != after, "baseline mirror is not an outcome"
    oldlines = before.decode().splitlines(keepends=True)
    newlines = after.decode().splitlines(keepends=True)
    removed = []
    kept = []
    for tag, a, b, c, d in difflib.SequenceMatcher(a=oldlines, b=newlines, autojunk=False).get_opcodes():
        if tag in ("delete", "replace"):
            removed.extend(range(a + 1, b + 1))
        if tag == "equal":
            kept.append({"old_lines": [a+1,b], "candidate_lines": [c+1,d],
                         "sha256": sha("".join(oldlines[a:b]).encode())})
    assert removed == expected_removed[path.removeprefix(formal_prefix)], (path, removed)
    if path == catalog_path:
        assert after.startswith(before)
    if path.endswith("wp66-a-party-and-summary-ui.md"):
        old_empty = oldlines[215].split("**空候选", 1)[1]
        assert next(line for line in newlines if "**空候选" in line).split("**空候选", 1)[1] == old_empty
    changed_payloads.append({"formal_target_for_integrator_only": path, "candidate_path": mirror,
        "mode": "100644", "type": "blob", "before": identity(before), "candidate": identity(after),
        "removed_or_replaced_frozen_lines": removed})
    preserved.append({"path": path, "equal_spans": kept})

catalog_before = show(MAIN, catalog_path)
catalog_after = Path(OWN + "/mirror/" + catalog_path).read_bytes()
new_rows = [line for line in catalog_after.decode().splitlines() if line.startswith("| U10-")]
assert len(new_rows) == 32
ids = [line.split("|")[1].strip() for line in new_rows]
assert len(set(ids)) == 32 and all(cid.encode() not in catalog_before for cid in ids)
assert {group: sum(cid.startswith("U10-" + group) for cid in ids) for group in ("CP","SF","MK","RL")} == {"CP":9,"SF":5,"MK":9,"RL":9}
assert all(len(line.split("|")) == 5 for line in new_rows)
old_case_rows = [{"frozen_line": i, "sha256_with_LF": sha(line.encode()),
                  "id_cell": line.split("|")[1].strip()}
                 for i, line in enumerate(catalog_before.decode().splitlines(keepends=True), 1)
                 if line.startswith("| ") and len(line.split("|")) > 2]
write("protected-regressions.json", {"kind": "BYTE_PRESERVATION_PLUS_AUTHOR_SCOPED_SEMANTIC_RECHECK",
    "equal_spans": preserved, "old_catalog_prefix_bytes": len(catalog_before),
    "all_old_catalog_bytes_preserved": True, "old_catalog_table_rows": old_case_rows,
    "new_vector_ids": ids, "new_vector_status": "DERIVED_VECTOR_NOT_EXECUTED",
    "historic_review_signatures_transferred": False, "new_full_ID_acceptance_inferred": False})
write("candidate-path-manifest.json", {"prepare": PREP, "frozen_main": MAIN,
    "branch": BRANCH, "changed_formal_mirrors": changed_payloads,
    "evidence_directory": OWN + "/evidence/", "formal_write_owner": "R6-I",
    "independent_candidate_review": "PENDING_NONAUTHOR", "integrated_actual_review": "PENDING"})

activation_path = "review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-activation/activation-receipt.json"
closing_path = "review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-closure-candidate/closure-candidate.json"
actraw, closeraw = show(PREP, activation_path), show(PREP, closing_path)
act, close = json.loads(actraw), json.loads(closeraw)
assert act["effective_counts"]["CLOSED"] == 92 and act["effective_counts"]["OPEN_REQUIRED"] == 0
assert len(act["state_resolution"]["selection"]) == len(close["records"]) == 92
for sel in act["state_resolution"]["selection"]:
    rec = close["records"][sel["record_index"]]
    assert rec["id"] == sel["id"]
    assert rec["proposed_only_after_valid_activation"] == {"status":"CLOSED", "final_CLOSED":True}
    assert canon(rec["proposed_only_after_valid_activation"]) == sel["selected_state_record_sha256"]
    # The activation hashes the complete qualified closing record as its scope binding.
    assert canon(rec) == sel["scope_record_sha256"]
assert all(Path(p).read_bytes() == show(PREP, p) for p in (activation_path, closing_path))
write("historical-state-binding.json", {"activation": {"path": activation_path, **identity(actraw)},
    "closing_payload": {"path": closing_path, **identity(closeraw)},
    "selected92_state_and_exact_scope_hashes_match": True,
    "related_records": ["GR5-M04-002", "GR5-M10-001"],
    "effective_counts": act["effective_counts"], "preserved_exclusions": act["preserved_exclusions"],
    "all_92_semantic_contracts_read_or_reviewed_here": False,
    "current_state_mutation": False, "new_candidate_acceptance_from_old_signature": False})

changed = git("diff", "--name-only", PREP).decode().splitlines()
untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
mirror_allow = {OWN + "/mirror/" + p for p in contract["candidate_formal_paths"]}
assert all(p in mirror_allow or p.startswith(OWN + "/evidence/") for p in changed + untracked)
subprocess.run(["git", "diff", "--check", PREP], check=True)
assert git("diff", "--name-only", MAIN, "--", "deliverables", "planning", "reference") == b""
write("tool-validation.json", {"kind": "TOOL_VALIDATION_ONLY", "cwd": str(Path.cwd()),
    "argv": sys.argv, "started_utc": STARTED, "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "exit_code": 0, "stderr": "", "runtime": sys.version,
    "checks": ["requested branch and prepare ancestry", "prompt exact expected identity",
        "separate contract hash and exact embedded equality", "all frozen contract source/formal identities",
        "nine cached counterevidence exact identities", "bounded source/formal reading delivery coverage",
        "all five mirrors actually changed", "exact eight changed old lines, other old spans preserved",
        "entire old catalog prefix preserved", "32 unique correctly shaped static vectors",
        "R5 exact92 activation status/scope bindings preserved", "own allowlist only", "git diff --check"],
    "reference_behavior_executions": 0, "independent_model_executions": 0,
    "host_demo_executions": 0, "save_network_behavior_executions": 0,
    "quality_verdict": "AUTHOR_TOOL_CHECKS_COMPLETE_NOT_INDEPENDENT_REVIEW"})
print(json.dumps({"result":"AUTHOR_TOOL_CHECKS_COMPLETE", "mirrors":len(changed_payloads),
                  "vectors":len(ids), "frozen_payload_bindings":len(bindings),
                  "reference_model_host_executions":0}, ensure_ascii=False))
