"""Check B09 document scope and identities; no reference behavior is executed.

Run after build_evidence.py. This verifies current document/evidence consistency,
not source semantics or independent acceptance. No reference modules are loaded.
"""
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[6]
OUT = pathlib.Path(__file__).resolve().parent
BASE = "407536adb682a04161d3e9c82f153a62b1becd97"
SCOPE = "de11c8a712b3fbce5c1e11756919536c4739e2a5"
REF = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
REF_TREE = "7589c800b61ba13a13040ed0d686979b80a84fd0"
SOURCE = pathlib.Path("/workspace/b09-reference")
PREFIX = "review/remediation/20261003-prepare/batches/B09/"
CONTRACT = "review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/B09-downstream-contract.json"
checks = []


def git(*args, cwd=ROOT, input=None):
    return subprocess.check_output(["git", *args], cwd=cwd, input=input)


def read(name):
    return json.loads((OUT / name).read_text())


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def check(name, condition, detail=None):
    assert condition, name
    checks.append(dict(check=name, passed=True, evidence=detail))


def identity_matches(raw, obj):
    return (sha(raw) == obj["sha256"] and len(raw) == obj["bytes"]
            and git("hash-object", "--stdin", input=raw).decode().strip() == obj["git_blob"])


c = json.loads((ROOT / CONTRACT).read_text())
formal = c["allowed_formal_write_paths"]
proposal = json.loads((OUT.parent / "scope-proposal-1/original-sync-proposal.json").read_text())
original = [f["path"] for f in proposal["files"]]
allowed = set(formal + original)
check("seven formal paths and five bounded approved originals", len(formal) == 7 and len(original) == 5)
check("isolated branch", git("branch", "--show-current").decode().strip() == "remediation/20261003-prepare/batch-B09")
check("accepted baseline and scope checkpoint are ancestors", all(subprocess.run(["git", "merge-base", "--is-ancestor", x, "HEAD"], cwd=ROOT).returncode == 0 for x in [BASE, SCOPE]))
changed = git("diff", "--name-only", BASE).decode().splitlines()
untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
check("complete current diff and untracked scope", all(p in allowed or p.startswith(PREFIX) for p in changed + untracked), dict(changed=changed, untracked=untracked))
check("all twelve normative paths changed", allowed <= set(changed))
check("whole-catalog lock and serialization controls retained", read("whole-catalog-lock-check.json")["serialization_contract"] == c["B09_B14_operational_serialization"])
check("no public registries or other batch files changed", all(p in allowed or p.startswith(PREFIX) for p in changed + untracked))
check("immutable scope checkpoint evidence", all(git("show", SCOPE + ":" + p) == (ROOT / p).read_bytes() for p in git("ls-tree", "-r", "--name-only", SCOPE, "--", PREFIX + "scope-proposal-1/").decode().splitlines()))
check("fixed contract unchanged", git("show", BASE + ":" + CONTRACT) == (ROOT / CONTRACT).read_bytes())

approval = read("original-scope-approval.json")
check("exact approved proposal manifest", sha((OUT.parent / "scope-proposal-1/original-sync-proposal.json").read_bytes()) == approval["manifest_sha256"])
clause_count = 0
for f in proposal["files"]:
    before = git("show", BASE + ":" + f["path"])
    check("original before identity " + f["path"], identity_matches(before, f["before"]))
    text = before.decode()
    for clause in f["clauses"]:
        check("unique approved before clause " + f["path"] + " " + clause["clause"], text.count(clause["before_text"]) == 1)
        text = text.replace(clause["before_text"], clause["intended_after_text"], 1)
        clause_count += 1
    actual = (ROOT / f["path"]).read_bytes()
    check("exact approved original reconstruction " + f["path"], actual == text.encode() and identity_matches(actual, f["intended_after"]))
    patch = (ROOT / f["complete_diff_path"]).read_bytes()
    check("approved original full patch hash " + f["path"], sha(patch) == f["complete_diff_sha256"] == approval["exact_original_patch_sha256"][f["path"]])
check("all thirty approved original clauses", clause_count == 30)

# The correct original experience, learning, result directions and saved-source
# Perish behavior must survive the unrelated approved synchronization.
wp42 = original[3]
before = git("show", BASE + ":" + wp42).decode()
after = (ROOT / wp42).read_text()
for start, end, label in [
    ("### 4.2 ", "## 5.", "A047/A049 complete original experience and learning"),
    ("### 3.2 ", "## 4.", "B025 original result table/directions"),
]:
    region = lambda t: t[t.index(start):t.index(end, t.index(start))]
    check(label, region(before) == region(after), sha(region(before).encode()))
perish = next(line for line in before.splitlines(keepends=True) if line.startswith("灭亡歌对每名合格者"))
check("B025 saved Perish source original paragraph", perish in after, sha(perish.encode()))

ledger = read("formal-change-log.json")
check("seventy-one formal clause entries", len(ledger["changes"]) == 71)
for entry in ledger["changes"]:
    check("current final clause " + entry["path"] + " " + entry["clause"], entry["path"] in formal and entry["after_text"] in (ROOT / entry["path"]).read_text())
for item in read("normative-identities.json")["files"]:
    check("normative before/after hashes " + item["after"]["path"], identity_matches(git("show", BASE + ":" + item["before"]["path"]), item["before"]) and identity_matches((ROOT / item["after"]["path"]).read_bytes(), item["after"]))
normative = read("normative-identities.json")["complete_normative_diff"]
check("complete twelve-path normative diff", (OUT / normative["path"]).read_bytes() == git("diff", "--binary", BASE, "--", *formal, *original) and sha((OUT / normative["path"]).read_bytes()) == normative["sha256"])

coverage = read("read-coverage.json")
check("sixty-two read binding membership", len(coverage["readers"]) == 62 and {r["path"] for r in coverage["readers"]} == {r["path"] for r in c["planned_reads"]})
for row in coverage["readers"]:
    before = row["frozen_input"]
    current = row["current_refreeze"]
    current_raw = git("show", current["commit"] + ":" + row["path"]) if current["commit"] else (ROOT / row["path"]).read_bytes()
    check("read binding/refreeze " + row["path"], identity_matches(git("show", before["commit"] + ":" + row["path"]), before) and identity_matches(current_raw, current))
check("no blanket semantic coverage claim", coverage["semantic_full_all62_claimed"] is False)

serial = lambda obj: json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
disp = read("contribution-dispositions.json")
check("all twenty contribution IDs and thirteen primary", len(disp["dispositions"]) == 20 and sum(d["primary"] for d in disp["dispositions"]) == 13 and {d["id"] for d in disp["dispositions"]} == set(c["contribution_finding_ids"]))
by_id = {d["id"]: d for d in disp["dispositions"]}
for control in c["contribution_controls"]:
    fid = control["id"]
    d = by_id[fid]
    check("complete effective control binding " + fid, sha(serial(control["complete_original_object"])) == control["original_complete_object_sha256"] and sha(serial(control["complete_approved_acceptance"])) == control["acceptance_object_sha256"] and d["source_control"]["current_qualifications"] == control["complete_original_object"].get("current_qualifications") and d["source_control"]["effective_case_constraints"] == control["complete_original_object"].get("effective_case_constraints"))
    check("pending contributors and canonical OPEN " + fid, d["other_contributors_pending"] == control["other_contributors_pending"] and d["canonical_state"] == "OPEN" and d["canonical_closed"] is False)

locks = read("whole-catalog-lock-check.json")
new_ids = []
for lock in locks["locks"]:
    p = lock["path"]
    old = git("show", BASE + ":" + p).decode()
    now = (ROOT / p).read_text()
    pattern = r"^\| ([A-Z]+-?\d+b?) \|"
    old_ids = re.findall(pattern, old, re.M)
    now_ids = re.findall(pattern, now, re.M)
    check("old catalog ID order/multiplicity and no duplicates " + p, len(now_ids) == len(set(now_ids)) and [i for i in now_ids if i in old_ids] == old_ids)
    added = [i for i in now_ids if i not in old_ids]
    new_ids.extend(added)
    check("exact new catalog IDs " + p, added == lock["new_ids"])
    protected = lambda t: t.split("## W：", 1)[1] if "combat-requirements" in p else t.split("## CP：", 1)[0]
    check("protected unrelated catalog bytes " + p, protected(old) == protected(now) and sha(protected(now).encode()) == lock["protected_sha256"])
check("twenty-four new catalog IDs", len(new_ids) == 24)
static = read("static-cases.json")
check("forty-three linked catalog rows/eighteen supplemental designs only", len(static["catalog_cases"]) == 43 and len(static["supplemental_designs"]) == 18 and all(r["executed"] is False for r in static["catalog_cases"] + static["supplemental_designs"]))
check("all catalog cases resolve to exact current rows", all((ROOT / r["path"]).read_text().splitlines()[r["line"] - 1].startswith("| " + r["id"] + " |") for r in static["catalog_cases"]))

check("reference exact commit/tree, detached and clean", git("rev-parse", "HEAD", cwd=SOURCE).decode().strip() == REF and git("rev-parse", "HEAD^{tree}", cwd=SOURCE).decode().strip() == REF_TREE and git("branch", "--show-current", cwd=SOURCE).decode().strip() == "" and git("status", "--porcelain=v1", "--untracked-files=all", cwd=SOURCE) == b"")
source_log = read("source-reading-log.json")
for row in source_log["additional_source_reads"]:
    raw = git("show", REF + ":" + row["path"], cwd=SOURCE)
    check("reference additional path identity/range " + row["path"], identity_matches(raw, row) and all(1 <= a <= b <= len(raw.decode().splitlines()) for a, b in row["displayed_text_ranges"]))
limits = read("source-limits.json")
check("all inherited named source limits and configuration preserved", limits["contract_source_limits"] == c["source_limits"] and limits["configuration"] == c["configuration"])
check("zero execution/observations/Demo claims", all(obj[key] == 0 for obj in [limits, static, source_log] for key in ["behavior_vectors_executed", "runtime_observations", "proven_Demo_chains"] if key in obj) and limits["reference_execution"] == 0 and static["executed"] == 0)

wp20 = read("out-of-scope-reader-proposal.json")
for f in wp20["files"]:
    raw = (ROOT / f["path"]).read_bytes()
    check("WP20 reader unchanged and unapplied " + f["path"], raw == git("show", BASE + ":" + f["path"]) and f["applied"] is False and f["authorized"] is False)
    text = raw.decode()
    for entry in f["clause_changes"]:
        check("WP20 exact unique before clause " + f["path"], text.count(entry["before_text"]) == 1)
        text = text.replace(entry["before_text"], entry["intended_after_text"], 1)
    check("WP20 intended after identity/full diff " + f["path"], identity_matches(text.encode(), f["intended_after"]) and sha((OUT / f["full_diff"]["path"]).read_bytes()) == f["full_diff"]["sha256"])
for batch in ["B04", "B07", "B08"]:
    req = read("affected-" + batch + "-review-request.json")
    check("separate affected candidate and actual request " + batch, req["author_approval"] is False and req["author_impact_disposition"] == "AFFECTED_SEPARATE_INDEPENDENT_CANDIDATE_AND_ACTUAL_REQUIRED" and req["independent_review"]["candidate_required"] is True and req["independent_review"]["actual_required"] is True)
    check("affected request all62 refreeze " + batch, len(read(req["all62_current_refreeze"])["readers"]) == 62)
check("WP20 residual included in B07 request", "out-of-scope-reader-proposal.json" in json.dumps(read("affected-B07-review-request.json")))
check("author checks confer no approval", read("candidate-review-request.json")["author_self_check_is_approval"] is False)
check("zero canonical closure and AREG sole writer", read("registry-change-proposals.json")["canonical_CLOSED"] == 0 and read("registry-change-proposals.json")["public_paths_modified"] == [])
subprocess.run(["git", "diff", "--check", BASE, "--", ".", ":(exclude)**/*.patch"], cwd=ROOT, check=True)
check("Git document/evidence whitespace check", True, "Exact .patch artifacts are hash-checked separately: unified-diff blank context requires a literal space and must not be stripped.")

report = dict(
    status="PASS_DOCUMENT_SCOPE_AND_IDENTITY_SELF_CHECK_ONLY",
    baseline=BASE, checkpoint=SCOPE, binding="Payload commit records these exact bytes; final envelope and remote SHA are supplied in handoff",
    checks_count=len(checks), checks=checks, independent_approval=False,
    behavioral_semantics_proven=False, reference_execution=0,
    behavior_vectors_executed=0, runtime_observations=0, proven_Demo_chains=0,
    canonical_OPEN=229, canonical_CLOSED=0,
    outstanding=["R-B09 full exact candidate/actual Ultra review", "Separate R-B04/R-B07/R-B08 affected candidate and actual reviews", "Parent scope disposition of exact unapplied WP20 two-file proposal", "AREG integration and registry proposals only after required independent gates", "B14 formal serialization after accepted B09-C and re-frozen reads; preflight not approved"],
)
(OUT / "author-self-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(dict(status=report["status"], checks=len(checks), contributions=20, primary=13, formal=7, approved_originals=5, new_catalog_ids=24, reference_execution=0, independent_approval=False)))
