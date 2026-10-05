"""Candidate-2 document/hash bookkeeping; never executes reference behavior."""
import copy
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[6]
OUT = pathlib.Path(__file__).resolve().parent
BATCH = OUT.parent
PREV = "8ff72341b5b91736970b5bfa5dc1b88137e618a5"
BASE = "407536adb682a04161d3e9c82f153a62b1becd97"
REF = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
SOURCE = pathlib.Path("/workspace/b09-reference")
CONTRACT = "review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/B09-downstream-contract.json"


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(name, previous=False):
    return json.loads(((BATCH / "candidate-1") if previous else OUT).joinpath(name).read_text())


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def identity(path, commit=None, cwd=ROOT):
    raw = git("show", commit + ":" + path, cwd=cwd) if commit else (cwd / path).read_bytes()
    blob = git("rev-parse", commit + ":" + path, cwd=cwd).decode().strip() if commit else git("hash-object", path, cwd=cwd).decode().strip()
    return dict(path=path, commit=commit, git_blob=blob, sha256=sha(raw), bytes=len(raw))


c = json.loads((ROOT / CONTRACT).read_text())
approval = json.loads((BATCH / "scope-amendment-2/approval.json").read_text())
application = json.loads((BATCH / "scope-amendment-2/application.json").read_text())
extra = [f["path"] for f in application["files"]]
old_norm = read("normative-identities.json", True)
old_paths = [f["after"]["path"] for f in old_norm["files"]]
paths = old_paths + extra
assert len(paths) == 14 and len(set(paths)) == 14
for p in old_paths:
    assert git("show", PREV + ":" + p) == (ROOT / p).read_bytes()
formal = [p for p in paths if p.startswith("deliverables/")]
original = [p for p in paths if p.startswith("specs/")]
assert len(formal) == 8 and len(original) == 6

clause_changes = []
for f in application["files"]:
    for clause in f["clauses"]:
        clause_changes.append(dict(path=f["path"], finding_ids=["GIR-FD82-B013"], clause="§6.4 " + ("正常终局接收集合" if clause["before_lines"][0] in [192, 196] else "满队送盒·伙伴限定"), before_text=clause["before_text"], after_text=clause["intended_after_text"], before_lines=clause["before_lines"], authority="scope-amendment-2/approval.json"))
dump("amended-scope.json", dict(status="BOUNDED_PARENT_SCOPE_AUTHORIZED_NOT_CORRECTNESS_APPROVED", baseline=BASE, previous_candidate=PREV, unchanged_executable_contract=identity(CONTRACT, BASE), amendment_approval=identity(str((BATCH / "scope-amendment-2/approval.json").relative_to(ROOT))), complete_normative_write_count=14, formal_final_count=8, exact_approved_original_count=6, complete_normative_write_paths=paths, original_twelve_unchanged=old_paths, new_paths_only=extra, exact_new_clauses=clause_changes, public_writes_authorized=False, required_independent_affected_batches=["B04", "B05", "B07", "B08"], no_new_root=True, canonical_OPEN=229, canonical_CLOSED=0, B09_B14_serialization=c["B09_B14_operational_serialization"]))

ledger = copy.deepcopy(read("formal-change-log.json", True))
ledger["changes"].extend(e for e in clause_changes if e["path"] in formal)
ledger["candidate_1_change_count"] = 71
ledger["candidate_2_change_count"] = 2
ledger["after_identities"] = [identity(p) for p in formal]
ledger["status"] = "COMPLETE_AMENDED_LOCAL_CANDIDATE_PENDING_INDEPENDENT_REVIEW"
dump("formal-change-log.json", ledger)
norm_patch = git("diff", "--binary", BASE, "--", *paths)
amend_patch = git("diff", "--binary", PREV, "--", *paths)
(OUT / "formal-and-approved-originals.patch").write_bytes(norm_patch)
(OUT / "candidate-1-to-2-normative.patch").write_bytes(amend_patch)
dump("normative-identities.json", dict(baseline=BASE, previous_candidate=PREV, normative_count=14, formal_count=8, approved_original_count=6, approved_original_clause_count=32, final_clause_count=73, files=[dict(before=identity(p, BASE), candidate_1=identity(p, PREV), after=identity(p), changed_since_candidate_1=p in extra) for p in paths], full_normative_diff=dict(path="formal-and-approved-originals.patch", sha256=sha(norm_patch), bytes=len(norm_patch)), complete_amendment_normative_diff=dict(path="candidate-1-to-2-normative.patch", sha256=sha(amend_patch), bytes=len(amend_patch)), not_full_candidate_evidence_diff=True))

dispositions = copy.deepcopy(read("contribution-dispositions.json", True))
b013 = next(d for d in dispositions["dispositions"] if d["id"] == "GIR-FD82-B013")
b013["final_changes"].extend(dict(path=e["path"], clause=e["clause"]) for e in clause_changes if e["path"] in formal)
b013["exact_authorized_original_changes"].extend(dict(path=e["path"], clause=e["clause"]) for e in clause_changes if e["path"] in original)
b013["local_reason"] += " Candidate-2 synchronizes exactly two WP20 original/final §6.4 clauses under the parent amendment; the former extra-reader contradiction is resolved locally, subject to full R-B09 and new bounded affected R-B05 candidate+actual review."
b013["amendment"] = "scope-amendment-2/approval.json; application.json"
dispositions["amendment"] = dict(id="GIR-FD82-B013", new_root=False, scope_authorized=True, correctness_approved=False, affected_B05_review_required=True)
dump("contribution-dispositions.json", dispositions)

b05_manifest_path = "review/remediation/20261003-prepare/batches/B05/acceptance-stage-1/acceptance-manifest.json"
b05_limits_path = "review/remediation/20261003-prepare/batches/B05/integration-review-1/model-and-limits.json"
b05 = json.loads((ROOT / b05_manifest_path).read_text())
b05_limits = json.loads((ROOT / b05_limits_path).read_text())
catalog = "deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md"
wp32 = "deliverables/final-specification-set/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md"
wp50 = "deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md"
coverage = copy.deepcopy(read("read-coverage.json", True))
for row in coverage["readers"]:
    prior = row["current_refreeze"]
    row["candidate_1_refreeze"] = prior
    row["current_refreeze"] = identity(row["path"], prior["commit"]) if prior["commit"] else identity(row["path"])
additional_modes = {
    extra[0]: dict(mode="WP20 §6.4 complete four-before/after approval binding; original context §6.1–6.4; exact full amendment diff", full_file_semantic_read=False),
    extra[1]: dict(mode="WP20 §6.1–6.4 complete held-item interface and exact full amendment diff", full_file_semantic_read=False),
    b05_manifest_path: dict(mode="accepted WP20 original/final identities, exact historical verdict/SHA, future-dependency gate and all stated limitations; unrelated sixteen finding dispositions are not re-adjudicated", full_file_semantic_read=False),
    "review/remediation/20261003-prepare/batches/B05/acceptance-stage-1/downstream-handshake.json": dict(mode="identity and selected exact B05 historical integration/candidate/report references; displayed bulk output truncated, no complete semantic coverage claimed", full_file_semantic_read=False),
    "review/remediation/20261003-prepare/batches/B05/acceptance-stage-1/README.md": dict(mode="complete instructions and bounded acceptance/unknown/serialization context read", full_file_semantic_read=True),
    b05_limits_path: dict(mode="complete historical model-and-limits read; all unknowns preserved, historical configuration not treated as current runtime evidence", full_file_semantic_read=True),
    catalog: dict(mode="complete HP24–31 rows and section/ID locator scan; all file identities preserved, unrelated CI/PT/PS/AQ and remaining HP semantics not re-reviewed", lines=[65,72], full_file_semantic_read=False),
    wp32: dict(mode="same candidate-1 additional consumer; current-item context lines20–30 and capture/world timing61–90 reread; full file identity only outside those clauses", lines=[[20,30],[61,90]], full_file_semantic_read=False),
}
existing = {r["path"] for r in coverage["readers"]}
for p, mode in additional_modes.items():
    if p not in existing:
        coverage["readers"].append(dict(path=p, frozen_input=identity(p, PREV), current_refreeze=identity(p), changed=p in extra, semantic_scope=mode, unread_limits="Unlisted clauses and unrelated historical controls remain unread/unreviewed; identity is not full semantic coverage.", amendment_additional=True))
coverage.update(original_fixed_planned_count=62, original_fixed_bindings_retained=62, amended_additional_count=len(coverage["readers"])-62, amended_total_count=len(coverage["readers"]), bindings_checked=len(coverage["readers"]), planned_count=len(coverage["readers"]), semantic_full_all62_claimed=False, semantic_full_all_amended_claimed=False, amendment_approval="../scope-amendment-2/approval.json", candidate_1_coverage_immutable=True)
coverage["additional_unplanned_readers_history"] = coverage.pop("additional_unplanned_readers", [])
dump("read-coverage.json", coverage)

limits = copy.deepcopy(read("source-limits.json", True))
limits["additional_B05_historical_limits"] = dict(acceptance_identity=identity(b05_manifest_path, PREV), acceptance_limitations=b05["limitations"], model_and_limits_identity=identity(b05_limits_path, PREV), unknowns_preserved=b05_limits["unknowns_preserved"])
dump("source-limits.json", limits)
source_log = copy.deepcopy(read("source-reading-log.json", True))
source_log["candidate_1_log_identity"] = identity(str((BATCH / "candidate-1/source-reading-log.json").relative_to(ROOT)), PREV)
source_log["amendment_rereads"] = [dict(**identity(e["path"], REF, SOURCE), displayed_text_ranges=[e["lines"]], role=e["role"], read_only=True) for e in read("out-of-scope-reader-proposal.json", True)["source_evidence"]]
source_log["reference_clean"] = git("status", "--porcelain=v1", "--untracked-files=all", cwd=SOURCE) == b""
dump("source-reading-log.json", source_log)
dump("static-cases.json", dict(**copy.deepcopy(read("static-cases.json", True)), amendment_crosschecks=dict(id="GIR-FD82-B013", new_catalog_ids=0, existing_case_prerequisites_unchanged=True, directly_consume=["CP20", "CP21", "CP22", "E14", "CX40", "CX41", "CX42", "B09-CAPTURE-TEMPORARY-REMOVAL", "B09-CAPTURE-MIDDLE-WORLD"], forward="Actually participating partner + full-party replacement retains boxed identity in old merged participation and shifted six-player restore records; qualified no-KnockOff primary and middle-member mapping remain unchanged.", reverse="No participating partner/list aligned uses normal member record; merely registered partner is insufficient. Temporary KnockOff uses qualified Shadow/Snag trainer route; ordinary permanent consumption not substituted.", executed=False)))
dump("whole-catalog-lock-check.json", copy.deepcopy(read("whole-catalog-lock-check.json", True)))

def clause(path, start, end):
    before = git("show", PREV + ":" + path).decode().splitlines(keepends=True)
    now = (ROOT / path).read_text().splitlines(keepends=True)
    a = "".join(before[start-1:end]); b = "".join(now[start-1:end])
    assert a == b
    return dict(path=path, lines=[start,end], before=identity(path,PREV), current=identity(path), text=b, byte_identical=True)

untouched = [clause(extra[0], 170, 191), clause(extra[0], 193, 196), clause(extra[0], 198, 198), clause(extra[1], 174, 190), clause(extra[1], 191, 195), clause(extra[1], 197, 200), clause(extra[1], 202, 202), clause(catalog, 65, 72), clause(wp32,20,30), clause(wp32,61,90), clause(wp50,9,42)]
analysis = [
    dict(interface="WP20 §6.4 → WP38 receive/send-box → WP42 normal terminal restoration", impact="AFFECTED", before="Unqualified restoration only for current party/outgoing boxed member absent from loop.", after="Normal terminal reads player-side participants against current same-index records. No-partner aligned ordinary rows retained; actual partner/full-party shift can retain boxed identity and misassign held items. Four exact approved clauses only.", evidence=["CP20","CP21","CP22","E14","CX40","CX41","CX42"], bound="No broad B05 identity/HP/status/PP/learning re-review; no architecture or callback replacement."),
    dict(interface="WP20 item writes/record updates → WP50 held-item consumers", impact="AFFECTED_INTERFACE_DESCRIPTION_REQUIRES_REVIEW", before="Field versus battle-write validation, permanent consume/obtain and temporary KnockOff records already correct.", after="Those writes and effects remain unchanged; WP20's terminal receiver qualification now agrees with WP42. Wrongly restored actual items can feed later current-item consumers. Shadow/Snag temporary-removal route remains separate from ordinary double-wild partner primary.", evidence=["CP20","CP21","CP22","B09-CAPTURE-TEMPORARY-REMOVAL"], bound="Only held-item identity/temporary-vs-permanent/restoration boundary; no new review of full WP50 effects/weight/ability mechanics."),
    dict(interface="WP42 normal restore → current-party world passives/WP32", impact="AFFECTED_DATA_PREMISE_REQUIRES_REVIEW", before="WP32 already reads actual current player items after normal restoration and world healing; captured/outgoing identity and index sets differ.", after="WP20 now documents that same terminal mapping. WP32 and WP42 sequence, evolution K/D/L0 records and world current-party identity remain unchanged; middle replacement retains qualified arbitrary-slot counterexample.", evidence=["CP22","E14","CX42","B09-CAPTURE-MIDDLE-WORLD"], bound="B05 review checks corrected WP20 input promises; B07 still owns accepted WP32 context. No general world/evolution re-review or automatic dependency approval."),
    dict(interface="Untouched WP20 surrounding clauses and accepted catalog HP24–31", impact="SUPPORTED_UNCHANGED_SUBCLAUSES_ONLY", before="Unknown identifier validation, mail coupling, initial-record updates and ordinary member examples.", after="Exact bytes unchanged. HP27–30 remain ordinary member/current-record examples under amended aligned-list qualification; they are not a blanket partner/full-party receiver guarantee. HP31 captured-direct-box differs from old member sent-box.", evidence=["HP-24","HP-25","HP-26","HP-27","HP-28","HP-29","HP-30","HP-31"], bound="Full same-candidate independent request must assess these bounded premises. No whole B05 NOT_AFFECTED or new prior PASS transfer."),
]
dump("semantic-dependency-log.json", dict(status="AUTHOR_BOUNDED_IMPACT_ANALYSIS_NOT_APPROVAL", amendment_id="GIR-FD82-B013", exact_new_before_after=clause_changes, existing_twelve_outputs_unchanged=True, additional_mandatory_local_correction=False, analysis=analysis, untouched_owner_consumer_clauses=untouched, required_affected_review_batches=["B04","B05","B07","B08"], static_designs_only=True, source_limits="source-limits.json", no_cross_owner_closure=True))
req = dict(batch="B05", author_impact_disposition="AFFECTED_SEPARATE_INDEPENDENT_CANDIDATE_AND_ACTUAL_REQUIRED", author_approval=False, candidate_binding="Exact final candidate-2 freeze-envelope SHA delivered by ordinary push and independent remote readback; full unfiltered predecessor-to-final and candidate-1-to-final diffs required", historical_accepted_manifest=identity(b05_manifest_path,PREV), historical_reviewed_integration_commit=b05["reviewed_integration_commit"], historical_reviewed_integration_tree=b05["reviewed_integration_tree"], historical_independent_result=b05["independent_review_result"], historical_limits=b05["limitations"], exact_changed_paths=[dict(before=identity(p,PREV),after=identity(p)) for p in extra], exact_four_before_after_clauses=clause_changes, scoped_reader_caller_data_condition_analysis=analysis, untouched_owner_clauses=untouched, review_boundary="WP20 original/final §6.4 two-clause synchronizations and their held-item/capture/normal-terminal/current-item consumers; confirm protected surrounding WP20 clauses and HP24–31 without re-adjudicating unrelated B05 identity/stats/forms/Shadow/HP/PP/move-learning roots or all catalog owner sections.", required_inputs=["unchanged complete B09 downstream contract and all effective B013 root/qualifications/extensions", "scope-amendment-2 exact approval/application and candidate-1 proposal", "complete current WP20 original/final context and exact complete diffs", "WP38/WP42 existing qualified CP20–22/E14 and accepted CX40–42", "semantic-dependency-log.json exact unchanged WP20/HP/WP32/WP50 clauses", "all amended read refreezes/source limits", "full unfiltered exact final candidate diff, including evidence/public/history preservation"], static_cases=["CP20","CP21","CP22","E14","CX40","CX41","CX42","B09-CAPTURE-TEMPORARY-REMOVAL","B09-CAPTURE-MIDDLE-WORLD"], all_amended_current_refreeze="read-coverage.json", independent_review=dict(requested_model="gpt-6.1-sol",reasoning="Ultra",speed="Standard(default)",effective_configuration="UNVERIFIED under approved Plan A",candidate_required=True,actual_required=True,actual_requirement="Separate bounded R-B05 at exact AREG integration SHA; full predecessor-to-actual and candidate-to-actual public/management/source deltas, current owner/reader refreezes, no old PASS transfer"), no_new_B05_contribution_or_primary_count=True, no_root_or_canonical_closure=True, reference_execution=0, behavior_vectors_executed=0, runtime_observations=0, proven_Demo_chains=0)
dump("affected-B05-review-request.json", req)
for b in ["B04", "B07", "B08"]:
    req = copy.deepcopy(read("affected-"+b+"-review-request.json", True))
    req["candidate_binding"] = "Exact final candidate-2 freeze-envelope SHA in ordinary push/readback handoff; candidate-1 is immutable history, not current review target"
    req["all_amended_current_refreeze"] = req.pop("all62_current_refreeze")
    req.pop("unapplied_extra_reader_scope_proposal", None)
    req["resolved_WP20_amendment"] = dict(authority="../scope-amendment-2/approval.json",application="../scope-amendment-2/application.json",scope="Two exact WP20 §6.4 clauses per original/final; existing twelve normative outputs unchanged",new_separate_B05_review="affected-B05-review-request.json")
    req["complete_normative_diff"] = "formal-and-approved-originals.patch (all fourteen normative paths); candidate-1-to-2-normative.patch is the complete two-path amendment"
    req["complete_unfiltered_diff"] = "../freeze-envelope-2/full-predecessor-to-payload.patch and candidate-1-to-payload.patch plus payload-to-final-envelope delta; exact final SHA/full diff identity in pushed handoff"
    if b == "B07":
        req["changed_readers"].extend(dict(path=p,before=identity(p,PREV),after=identity(p),full_before_after_clauses=[e for e in clause_changes if e["path"]==p]) for p in extra)
        req["reader_caller_data_condition_analysis"].append(analysis[2])
    dump("affected-"+b+"-review-request.json",req)
reverse = copy.deepcopy(read("reverse-impact.json", True))
reverse.pop("unapplied_extra_reader_scope_proposal", None)
reverse["all_amended_refreeze"] = "read-coverage.json"
reverse["amendment_dependency_log"] = "semantic-dependency-log.json"
reverse["required_affected_reviews"] = ["affected-"+b+"-review-request.json" for b in ["B04","B05","B07","B08"]]
reverse["former_WP20_residual"] = "Exactly authorized and applied in candidate-2; independent R-B09 and bounded R-B05 required, no correctness approval inferred"
dump("reverse-impact.json",reverse)
registry = copy.deepcopy(read("registry-change-proposals.json",True))
registry.pop("unapplied_extra_reader_scope_proposal",None)
registration = next(d for d in registry["contributions"] if d["id"] == "GIR-FD82-B013")
registration["final_clauses"] = b013["final_changes"]
registration["exact_authorized_original_changes"] = b013["exact_authorized_original_changes"]
registry["amendment"] = dict(existing_id="GIR-FD82-B013",scope_application="../scope-amendment-2/application.json",new_canonical_ids=0,new_AX=0,new_B05_acceptance_counts=0,required_candidate_actual_affected_receipts=["B04","B05","B07","B08"],former_WP20_scope_residual="Applied exactly; independent review pending; immutable candidate-1 proposal retained")
dump("registry-change-proposals.json",registry)
review = copy.deepcopy(read("candidate-review-request.json",True))
review.pop("unapplied_extra_reader_scope_proposal",None)
review.update(binding="Exact final candidate-2 freeze-envelope SHA in ordinary push/remote-readback handoff",previous_candidate=PREV,formal_count=8,approved_originals=6,normative_count=14,final_clause_count=73,original_clause_count=32,amended_read_count=len(coverage["readers"]),required_affected_batches=["B04","B05","B07","B08"])
review["required_inputs"] = ["unchanged full executable contract and all twenty complete effective controls/qualifications/extensions", "immutable candidate-1/scope-proposal-1/freeze-envelope; exact scope-amendment-2 approval/application", "all fourteen current normative files: eight final/six exact-authorized originals, seventy-three final clauses and thirty-two original clauses", "all twenty dispositions/thirteen primary, unchanged forty-three catalog rows/eighteen supplemental static designs", "all amended frozen read/refreeze identities, full source and unknown limits", "separate affected B04/B05/B07/B08 candidate and actual requests with bounded unchanged owner clauses", "full unfiltered baseline-to-candidate-2-payload, candidate-1-to-payload and payload-to-final-envelope diffs"]
review["required_actual"] = "Full separate R-B09 exact AREG integration SHA Ultra/Standard, plus separately scoped affected B04/B05/B07/B08 actual reviews; full predecessor-to-actual and candidate-to-actual public/management/source deltas and refreezes"
dump("candidate-review-request.json",review)
print(json.dumps(dict(normative_paths=14,final=8,originals=6,final_clauses=73,original_clauses=32,read_bindings=len(coverage["readers"]),contributions=20,primary=13,new_catalog_ids=24,WP20_exact_scope_applied=True,affected=["B04","B05","B07","B08"],independent_approval=False)))
