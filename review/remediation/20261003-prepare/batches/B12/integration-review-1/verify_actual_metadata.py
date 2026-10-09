"""New actual-review Git/JSON/hash/text bookkeeping, never reference behavior."""
import collections
import csv
import hashlib
import io
import json
import pathlib
import re
import subprocess

ACT = "a46d6c457ff0a01181f22a80af25419370f86149"
BASE = "1d06c45cc0a744fca181ac80ee573cc9ebb9b862"
CAND = "8ddba850af71f24e7bd77a80b7605c456c31dc7a"
ADMIN = "9ad5539f38544fef6037356018015fe418021514"
PACKET = "aa90d3988b410b4bec447f4f80d1b63ab97c46c9"
FULL = "76a49b3829fa8193107851b6816ab317ff94c815"
AFFECTED = "e94ed84d5118f3fc53091f8055db00aab20b62fb"
ROOT = "review/remediation/20261003-prepare/"
B12 = ROOT + "batches/B12/"
G = B12 + "integration-stage-1/"
OUT = pathlib.Path(B12 + "integration-review-1")

def git(*args):
    return subprocess.check_output(["git", *args])

def read(commit, path):
    return git("show", commit + ":" + path)

def obj(commit, path):
    return json.loads(read(commit, path))

def sha(data):
    return hashlib.sha256(data).hexdigest()

def identity(commit, path):
    data = read(commit, path)
    return dict(commit=commit, path=path, git_blob=git("rev-parse", commit + ":" + path).decode().strip(), sha256=sha(data), bytes=len(data))

def verify(binding):
    got = identity(binding["commit"], binding["path"])
    matches = {k: got[k] == binding[k] for k in ["git_blob", "sha256", "bytes"] if k in binding}
    assert all(matches.values()), (binding, got)
    return dict(identity=got, matches=matches)

def paths(a, b):
    return git("diff", "--no-ext-diff", "--no-textconv", "--name-only", a, b).decode().splitlines()

def tree(commit):
    entries = {}
    for item in git("ls-tree", "-r", "-z", commit).split(b"\0"):
        if not item:
            continue
        desc, path = item.split(b"\t", 1)
        entries[path.decode()] = desc.decode()
    return entries

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

freeze = obj(PACKET, B12 + "actual-freeze-1/actual-freeze.json")
request = obj(ACT, G + "actual-review-request.json")
manifest = obj(ACT, G + "integration-manifest.json")
copies = obj(ACT, G + "formal-copy-identities.json")
registration = obj(ACT, G + "finding-registration.json")
gates = obj(ACT, G + "candidate-gate-receipts.json")
candidate_review = obj(FULL, B12 + "candidate-review-1/review.json")
candidate_meta = obj(FULL, B12 + "candidate-review-1/metadata-verification.json")
bindings = obj(CAND, B12 + "author-draft-1/qualified-control-bindings.json")
matrix = obj(CAND, B12 + "candidate-1/contribution-matrix.json")
qualified = obj(ADMIN, B12 + "refreeze-after-B15-C-1/B12-downstream-contract.json")
statistics_path = ROOT + "batches/B15/acceptance-stage-1/completion-statistics-successor.json"
statistics = obj(BASE, statistics_path)
assert freeze["reviewed_actual_commit"] == ACT
assert git("rev-parse", ACT + "^{tree}").decode().strip() == freeze["reviewed_actual_tree"] == "1d1c3ea7b217463b88146c7640ae4a6821c25c54"
assert freeze["current_formal_accepted_predecessor"] == BASE
assert candidate_review["reviewed_commit"] == CAND and candidate_review["contribution_count"] == 9 and candidate_review["primary_count"] == 6
packet_bindings = {k: verify(freeze[k]) for k in ["G_request", "G_manifest", "G_complete_registration", "G_formal_copies", "G_original_scope", "candidate_gates"]}
publication = freeze["publication_receipt"]
assert publication["actual_commit"] == ACT and publication["actual_tree"] == freeze["reviewed_actual_tree"]
assert publication["remote_ref"] == publication["FETCH_HEAD"] == publication["tracking_ref"] == ACT
assert len(publication["identities"]) == publication["changed_files"] == 102
for b in publication["identities"]:
    verify(b)
assert {b["path"] for b in publication["identities"]} == set(paths(ADMIN,ACT))

formal = set(request["formal_scope"])
public = {ROOT + x for x in ["approval-ledger.tsv", "traceability-successor.tsv", "final-integration-review.md"]}
management = set(paths(BASE, ADMIN))
assert len(formal) == 16 and len(management) == 28
def category(path):
    if path in formal:
        return "formal11_and_approved_original5"
    if path in public:
        return "public_pending3"
    if path in management:
        return "frozen_management28"
    if path.startswith((B12 + "author-draft-1/", B12 + "candidate-1/")):
        return "author_and_candidate27"
    if path.startswith((B12 + "candidate-review-1/", B12 + "affected-candidate-review-1/")):
        return "independent_candidate45"
    if path.startswith(G):
        return "new_G11"
    raise AssertionError(("unexpected changed path", path))

streams = []
for frozen in freeze["complete_unfiltered_differences"]:
    command = frozen["command"]
    assert command == ["git", "diff", "--no-ext-diff", "--no-textconv", "--binary", "--full-index", frozen["from"], ACT]
    data = subprocess.check_output(command)
    changed = paths(frozen["from"], ACT)
    assert len(data) == frozen["bytes"] and sha(data) == frozen["sha256"] and len(changed) == frozen["changed_path_count"]
    counts = dict(collections.Counter(category(p) for p in changed))
    expected = dict(public_pending3=3, frozen_management28=28, independent_candidate45=45, new_G11=11)
    if frozen["from"] == BASE:
        expected.update(formal11_and_approved_original5=16, author_and_candidate27=27)
    assert counts == expected, counts
    streams.append(dict(name=frozen["name"], command=command, bytes=len(data), sha256=sha(data), changed_path_count=len(changed), categories=counts, full_unfiltered=True, exact_freeze_match=True, reconstruction="Generated complete stream in memory, compared hash/bytes and all-path inventory; no redundant 7MB committed archive.", changed_files=[dict(path=p, category=category(p), actual=identity(ACT, p)) for p in changed]))
write("complete-diff-verification.json", dict(reviewed_actual=ACT, packet=PACKET, streams=streams))

formal_checks = []
assert len(copies["identities"]) == 16
for x in copies["identities"]:
    assert x["path"] in formal
    actual = identity(ACT, x["path"])
    checks = {k: verify(x[k]) for k in ["candidate", "accepted_before", "administrative_before"]}
    assert read(ACT, x["path"]) == read(CAND, x["path"])
    formal_checks.append(dict(path=x["path"], actual=actual, inputs=checks, exact_candidate_bytes=True))
artifact_checks = []
assert len(copies["author_and_report_artifacts_copied"]) == 88
for x in copies["author_and_report_artifacts_copied"]:
    source = verify(x)
    assert read(ACT, x["path"]) == read(x["commit"], x["path"])
    artifact_checks.append(dict(source=source, actual=identity(ACT, x["path"]), exact_source_bytes=True))
assert len({x["actual"]["path"] for x in artifact_checks}) == 88

scope = obj(CAND, B12 + "author-draft-1/scope-amendment-1.json")
scope_application = obj(ACT, G + "original-scope-application.json")
assert scope_application["label_correction"] == scope["label_correction"]
verify(scope["approved_proposal"])
patches = []
for x in scope["proposals"]:
    before = dict(commit=x["before_commit"], path=x["path"], git_blob=x["before_git_blob"], sha256=x["before_sha256"], bytes=x["before_bytes"])
    patch = dict(commit=x["approved_patch_commit"], path=x["approved_patch_path"], git_blob=x["approved_patch_blob"], sha256=x["approved_patch_sha256"])
    verify(before)
    verify(patch)
    output = identity(ACT, x["path"])
    assert output["sha256"] == x["approved_after_sha256"] and output["git_blob"] == x["actual_after_git_blob"] and output["bytes"] == x["actual_after_bytes"]
    assert read(ACT, patch["path"]) == read(patch["commit"], patch["path"])
    patches.append(dict(number=x["proposal_number"], before=before, approved_patch=patch, actual_after=output, exact_before_patch_after=True, quality_basis=dict(commit=FULL, path=B12 + "candidate-review-1/review.json")))
write("output-and-copy-verification.json", dict(reviewed_actual=ACT, formal_outputs=formal_checks, original_patch_scope=patches, proposal4_label_only=scope["label_correction"], exact_artifact_copies=artifact_checks, count=dict(formal=11,originals=5,author=27,independent_candidate=45), archived_program_execution=0))

trees = {k: tree(k) for k in [BASE, CAND, ADMIN, ACT]}
old_changes = {p: (v, trees[ACT].get(p)) for p,v in trees[BASE].items() if trees[ACT].get(p) != v}
assert set(old_changes) == formal | public
candidate_changes = {p: (v, trees[ACT].get(p)) for p,v in trees[CAND].items() if trees[ACT].get(p) != v}
assert set(candidate_changes) == public
assert all(trees[ADMIN][p] == trees[ACT][p] for p in management)
namespaces = []
for owner in ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B09", "B10", "B11", "B14", "B15"]:
    prefix = ROOT + "batches/" + owner + "/"
    old = {p:v for p,v in trees[BASE].items() if p.startswith(prefix)}
    new = {p:v for p,v in trees[ACT].items() if p.startswith(prefix)}
    if owner == "B15":
        additions = set(new) - set(old)
        assert additions <= management
    assert all(new.get(p) == v for p,v in old.items())
    namespaces.append(dict(batch=owner, prior_paths=len(old), prior_entries_preserved=True, only_frozen_management_additions=sorted(set(new)-set(old))))
b16_before = {p:v for p,v in trees[ADMIN].items() if p.startswith(ROOT + "batches/B16/")}
b16_after = {p:v for p,v in trees[ACT].items() if p.startswith(ROOT + "batches/B16/")}
assert b16_before == b16_after
assert read(ACT,statistics_path) == read(BASE,statistics_path)
catalogs = []
for path in ["deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md", "deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md"]:
    def rows(c):
        return [x for x in read(c,path).decode().splitlines() if re.match(r"^\| [A-Z]+\d+[a-z]? \|",x)]
    old, new = rows(BASE), rows(ACT)
    assert not (collections.Counter(old)-collections.Counter(new))
    it = iter(new)
    assert all(any(z==x for z in it) for x in old)
    added = list((collections.Counter(new)-collections.Counter(old)).elements())
    assert read(ACT,path) == read(CAND,path)
    catalogs.append(dict(path=path, old_rows=len(old), actual_rows=len(new), all_old_bytes_order_multiplicity_preserved=True, candidate_exact=True, added_static_rows_not_executed=added))
assert sum(x["old_rows"] for x in catalogs) == 387 and sum(len(x["added_static_rows_not_executed"]) for x in catalogs) == 15
accepted_files = obj(FULL,B12+"candidate-review-1/accepted-interface-preservation.json")
consumer_files = []
for x in accepted_files["files"]:
    p = x["after"]["path"]
    assert read(BASE,p) == read(CAND,p) == read(ACT,p)
    consumer_files.append(dict(input=identity(ACT,p), same_BASE_and_candidate=True))
write("accepted-result-protection.json", dict(reviewed_actual=ACT, accepted_predecessor=BASE, all_prior_tree_entries_preserved_except_authorized16_and_public3=True, prior_tree_entry_count=len(trees[BASE]), candidate_prior_entries_preserved_except_public3=True, prior_changed_entries=old_changes, accepted_namespaces=namespaces, management28_preserved=True, receiving23_files=consumer_files, catalogs=catalogs, accepted_statistics=identity(ACT,statistics_path), accepted_statistics_same_blob=True, B16_namespace_exact_ADMIN=True, B16_private_preparation_not_imported_or_revalidated=True))

receipts = []
assert len(gates["receipts"]) == 11
for x in gates["receipts"]:
    report = verify(x["report"])
    assert read(ACT,x["report"]["path"]) == read(x["report_commit"],x["report"]["path"])
    for b in x["artifacts"]:
        verify(b)
        assert read(ACT,b["path"]) == read(b["commit"],b["path"])
    disposition = obj(x["report_commit"],x["report"]["path"])
    assert disposition["verdict"] == x["verdict"]
    reviewed_key = "reviewed_commit" if x["gate"] == "FULL" else "reviewed_sha"
    assert disposition[reviewed_key] == CAND and not disposition["blocking_findings"]
    receipts.append(dict(gate=x["gate"], report=report, verdict=x["verdict"], actual_verdict_transferred=x["actual_verdict_transferred"], archived_exact=True, artifact_count=len(x["artifacts"]), disposition_keys=list(disposition), actual_owner_receipt_signed_by_FULL=False))
    assert not x["actual_verdict_transferred"]
assert set(gates["affected_PASS"]) == {"B07","B08","B09","B10","B11"}
assert set(gates["affected_supported_NOT_AFFECTED"]) == {"B02","B03","B04","B14","B15"}
canonical = git("diff","--binary","--full-index","--no-ext-diff","--no-textconv",BASE,CAND)
assert len(canonical) == gates["full_index_canonical_diff"]["bytes"] and sha(canonical) == gates["full_index_canonical_diff"]["sha256"]
def normalize_indexes(data):
    return re.sub(rb"(?m)^index [0-9a-f]+\.\.[0-9a-f]+( [0-9]+)?$",lambda m:b"index HASH..HASH"+(m[1] or b""),data)
raw_archives = []
for x in gates["raw_diff_archives"]:
    verify(x["source"])
    raw = read(x["source"]["commit"],x["source"]["path"])
    assert normalize_indexes(raw) == normalize_indexes(canonical)
    assert read(ACT,x["source"]["path"]) == raw
    raw_archives.append(dict(identity=x["source"], full_index_equivalent_except_index_abbreviation=True, archived_raw_bytes_unchanged=True))
write("candidate-evidence-reuse.json", dict(reviewed_actual=ACT, candidate=CAND, FULL_report=FULL, affected_report=AFFECTED, exact_candidate_receipts=receipts, own_source_review_identity=identity(FULL,B12+"candidate-review-1/reading-log.json"), raw_diff_archives=raw_archives, no_old_programs_executed=True, own_prior_routing_is_navigation_not_owner_verdict=True, B09_latest_independent_candidate_PASS_consumed=True, no_candidate_actual_transfer=True))

approval_rows = None
public_tables = []
for path in [ROOT+"approval-ledger.tsv",ROOT+"traceability-successor.tsv"]:
    old, new = read(BASE,path), read(ACT,path)
    assert new.startswith(old)
    old_rows = list(csv.DictReader(io.StringIO(old.decode()),delimiter="\t"))
    new_rows = list(csv.DictReader(io.StringIO(new.decode()),delimiter="\t"))
    assert len(old_rows) == 223 and len(new_rows) == 232 and new_rows[:223] == old_rows
    added = new_rows[223:]
    assert [x["finding_id"] for x in added] == [x["id"] for x in registration["records"]]
    assert all(x["canonical_state"] == "OPEN" for x in added)
    if path.endswith("approval-ledger.tsv"):
        approval_rows = {x["finding_id"]:x for x in added}
        assert sum("PRIMARY_MINIMUM" in x["accepted_contribution_kind"] for x in added) == 6
        for x in added:
            assert "PENDING" in x["accepted_contribution_kind"] and "PENDING" in x["integration_disposition"]
            assert x["integration_review_commit"] == "" and x["candidate_commit"] == CAND and x["candidate_review_commit"] == FULL
    public_tables.append(dict(path=path, before=identity(BASE,path), after=identity(ACT,path), old223_exact_raw_prefix=True, old_rows=223, physical_rows=232, new9_pending_rows=added))
canonical_ledger = ROOT+"finding-ledger.tsv"
assert read(BASE,canonical_ledger) == read(ACT,canonical_ledger)
ledger_rows = list(csv.DictReader(io.StringIO(read(ACT,canonical_ledger).decode()),delimiter="\t"))
required = [x for x in ledger_rows if x["required_revision"] == "true"]
assert len(required) == 229 and all(x["canonical_state"] == "OPEN" for x in required)
final_review = ROOT+"final-integration-review.md"
assert read(ACT,final_review).endswith(read(ADMIN,final_review))
assert statistics["contribution_records"] == 223 and len(statistics["accepted_batches"]) == 13 and len(statistics["accepted_contribution_receipts"]) == 223
assert statistics["distinct_touched_IDs"] == 175 and statistics["primary_denominator"] == 143
assert statistics["strict_all_planned_contribution_counts"] == dict(all_contributor_batches_accepted=133,pending=10)
assert not statistics["global_gate_passed"]
write("public-registration-verification.json",dict(reviewed_actual=ACT, tables=public_tables, accepted_batches=statistics["accepted_batches"], accepted_contributions=223, physical_rows=232, new_B12_accepted=0, new_B12_pending=9, primary_minimum_denominator=143, specific_minimum_satisfied=143, touched_IDs=175, strict_primary_satisfied=133, strict_primary_pending=10, canonical_ledger=identity(ACT,canonical_ledger), canonical_required_OPEN=229, canonical_CLOSED=0, global_gate_passed=False, old_final_review_suffix_exact_ADMIN=True, final_review_prefix_bytes=len(read(ACT,final_review))-len(read(ADMIN,final_review))))

control_checks = []
accepted_receipts = statistics["accepted_contribution_receipts"]
assert len(registration["records"]) == 9
for index,x in enumerate(registration["records"]):
    candidate = bindings["contributions"][index]
    previous = candidate_review["contributions"][index]
    planned = matrix["contributions"][index]
    exact = qualified["contribution_controls"][index]
    assert x["id"] == candidate["id"] == previous["id"] == planned["id"] == exact["id"]
    assert x["primary"] == candidate["primary"] == previous["primary"]
    assert x["primary_owner"] == candidate["primary_owner"]
    assert x["complete_current_control_fields"] == candidate["complete_current_control_fields"] == exact["complete_current_control_fields"]
    for field in ["whole_original_object_sha256","whole_acceptance_object_sha256","whole_original_object_binding","whole_approved_acceptance_binding"]:
        assert x[field] == candidate[field]
    assert x["complete_minimum_acceptance_fields"]["binding"] == x["whole_approved_acceptance_binding"]
    verify(x["complete_qualified_control_binding"])
    assert x["complete_qualified_control_binding"]["pointer"] == "/contribution_controls/" + str(index)
    verify(x["whole_original_object_binding"])
    verify(x["whole_approved_acceptance_binding"])
    verify(x["candidate_FULL_disposition"])
    assert x["candidate_FULL_disposition"]["pointer"] == "/contributions/" + str(index)
    assert x["candidate_primary_or_local_minimum"] == {k:previous[k] for k in ["minimum_review","legal_counterexample_and_reverse_review","consumer_and_retained_boundary_review","original_scope_quality_review"]}
    assert x["current_formal_locators"]["paths"] == planned["formal_paths"] and x["current_formal_locators"]["clauses"] == planned["clauses"]
    assert x["static_test_ids_not_executed"] == planned["designs"]
    accepted = sorted({r["batch"] for r in accepted_receipts if r["id"] == x["id"]})
    assert sorted(x["accepted_contributors"]) == accepted
    assert x["remaining_contributors"] == [b for b in x["all_contributors"] if b not in accepted]
    assert "B12" in x["remaining_contributors"] and "B12" not in accepted
    assert x["canonical_state"] == "OPEN" and not x["final_closure"] and "PENDING" in x["current_status"]
    public_remaining = json.loads(approval_rows[x["id"]]["remaining_obligations"])
    for k in ["record_key","all_contributors","accepted_contributors","remaining_contributors"]:
        assert public_remaining[k] == x[k]
    assert public_remaining["complete_control"] == G+"finding-registration.json#/records/"+str(index)
    control_checks.append(dict(id=x["id"], primary=x["primary"], canonical_state=x["canonical_state"], original_and_approved_exact_candidate=True, full_current_qualified_fields_equal_candidate_and_ADMIN=True, complete_minimum_binding_preserved=True, formal_locator_and_static_design_bindings_equal_candidate=True, prior_candidate_minimum_and_contrasts_preserved=True, accepted_contributors=accepted, remaining_contributors=x["remaining_contributors"], accepted_contributors_independently_recomputed_from_old223=True, public_remaining_object_matches=True, source_scope=previous["exact_control_metadata"]))
assert sum(x["primary"] for x in control_checks)==6
write("control-registration-verification.json",dict(reviewed_actual=ACT, registration_identity=identity(ACT,G+"finding-registration.json"), records=control_checks, count=9, primary=6, current_minimum_preserved=True, actual_review_verdict="OWN_INDEPENDENT_VERDICT_IN_REVIEW_JSON; not a metadata PASS"))

register_tuples = obj(FULL,B12+"candidate-review-1/registration-comparison.json")
assert all(x["equal"] and not x["missing"] and not x["extra"] for x in register_tuples.values())
counts = {g:x["original_count"] for g,x in register_tuples.items()}
assert counts == dict(A=334,B=270,C=167) and sum(counts.values()) == 771
for x in candidate_meta["outputs"]:
    assert identity(ACT,x["output"]["path"])["sha256"] == x["output"]["sha256"]
new_json_paths = [p for p in paths(BASE,ACT) if p.endswith(".json")]
for p in new_json_paths:
    obj(ACT,p)
summary = dict(reviewed_actual=ACT, reviewed_tree=freeze["reviewed_actual_tree"], FIX_BASE=BASE, candidate=CAND, packet=PACKET, packet_bindings=packet_bindings, changed_paths_BASE_to_ACT=130, changed_paths_CAND_to_ACT=87, all16_candidate_payloads_exact=True, all27_author_and45_independent_archives_exact=True, management28_exact=True, prior_accepted223_raw_rows_exact=True, all9_complete_controls_current=True, accepted_batches=13, canonical_OPEN=229, canonical_CLOSED=0, runtime_observations=0, behavior_vectors_executed=0, old_program_execution=0, new_JSON_parsed=len(new_json_paths), A_B_C_occurrences=counts, A_B_C_sum=771, dispatch_arithmetic_typo="Dispatch/request say 766; A334+B270+C167=771. Actual tables/tuple archive and 786 including WP51's15 are correct; informational metadata correction only, no candidate/formal quality defect.")
write("metadata-verification.json",summary)
print(json.dumps({k:v for k,v in summary.items() if k != "packet_bindings"},ensure_ascii=False,indent=2))
