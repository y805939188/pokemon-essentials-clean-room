"""Current candidate-2 scope/identity audit; no behavioral execution or approval."""
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[6]
OUT = pathlib.Path(__file__).resolve().parent
PREV = "8ff72341b5b91736970b5bfa5dc1b88137e618a5"
BASE = "407536adb682a04161d3e9c82f153a62b1becd97"
REF = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
REF_TREE = "7589c800b61ba13a13040ed0d686979b80a84fd0"
SOURCE = pathlib.Path("/workspace/b09-reference")
PREFIX = "review/remediation/20261003-prepare/batches/B09/"
CONTRACT = "review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/B09-downstream-contract.json"
checks = []


def git(*args, cwd=ROOT, input=None):
    return subprocess.check_output(["git", *args], cwd=cwd, input=input)


def read(name, prev=False):
    return json.loads(((OUT.parent / "candidate-1") if prev else OUT).joinpath(name).read_text())


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def match(raw, obj):
    return sha(raw) == obj["sha256"] and len(raw) == obj["bytes"] and git("hash-object", "--stdin", input=raw).decode().strip() == obj["git_blob"]


def check(name, condition, detail=None):
    assert condition, name
    checks.append(dict(check=name, passed=True, evidence=detail))


scope = read("amended-scope.json")
paths = scope["complete_normative_write_paths"]
extra = scope["new_paths_only"]
check("fourteen exact normative paths/eight finals/six originals", len(paths) == 14 and len(set(paths)) == 14 and sum(p.startswith("deliverables/") for p in paths) == 8 and sum(p.startswith("specs/") for p in paths) == 6)
check("same isolated batch branch", git("branch", "--show-current").decode().strip() == "remediation/20261003-prepare/batch-B09")
check("candidate-1 ancestor", subprocess.run(["git", "merge-base", "--is-ancestor", PREV, "HEAD"], cwd=ROOT).returncode == 0)
changed = git("diff", "--name-only", BASE).decode().splitlines()
untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
check("complete current scope", all(p in paths or p.startswith(PREFIX) for p in changed + untracked))
check("all fourteen normative paths present", set(paths) <= set(changed))
since = git("diff", "--name-only", PREV).decode().splitlines()
check("only authorized WP20 normative delta", sorted(p for p in since if not p.startswith(PREFIX)) == sorted(extra))
for p in git("ls-tree", "-r", "--name-only", PREV, "--", PREFIX).decode().splitlines():
    check("immutable candidate-1/history " + p, git("show", PREV + ":" + p) == (ROOT / p).read_bytes())
for p in scope["original_twelve_unchanged"]:
    check("existing normative output unchanged " + p, git("show", PREV + ":" + p) == (ROOT / p).read_bytes())
check("fixed executable contract unchanged", git("show", BASE + ":" + CONTRACT) == (ROOT / CONTRACT).read_bytes())

approval = json.loads((OUT.parent / "scope-amendment-2/approval.json").read_text())
application = json.loads((OUT.parent / "scope-amendment-2/application.json").read_text())
proposal = read("out-of-scope-reader-proposal.json", True)
check("exact parent-reviewed proposal identity", sha((OUT.parent / "candidate-1/out-of-scope-reader-proposal.json").read_bytes()) == approval["approved_proposal_sha256"])
check("scope authorization not correctness verdict", approval["scope_authorization_only"] is True and approval["independent_correctness_approval"] is False)
for f in proposal["files"]:
    p = f["path"]
    before = git("show", PREV + ":" + p)
    check("WP20 before identity " + p, match(before, f["before"]))
    text = before.decode()
    for e in f["clause_changes"]:
        check("exact unique approved before clause " + p + " " + str(e["before_lines"]), text.count(e["before_text"]) == 1)
        text = text.replace(e["before_text"], e["intended_after_text"], 1)
    after = (ROOT / p).read_bytes()
    check("exact complete approved after/all other bytes preserved " + p, after == text.encode() and match(after, f["intended_after"]))
    patch = (OUT.parent / "candidate-1" / f["full_diff"]["path"]).read_bytes()
    check("exact approved WP20 patch hash " + p, sha(patch) == f["full_diff"]["sha256"] == approval["approved_patch_sha256"][p])
    app = next(x for x in application["files"] if x["path"] == p)
    check("application after identity " + p, match(after, app["after"]) and app["exact_approved_after_matches"])
check("no other mandatory correction or public write", application["mandatory_additional_local_correction_identified"] is False and application["public_registry_edits"] == 0 and application["unapproved_writes"] == 0)
old_originals = json.loads((OUT.parent / "scope-proposal-1/original-sync-proposal.json").read_text())["files"]
for f in old_originals:
    check("first five exactly approved originals preserved " + f["path"], match((ROOT / f["path"]).read_bytes(), f["intended_after"]))

norm = read("normative-identities.json")
for f in norm["files"]:
    p = f["after"]["path"]
    check("normative before/candidate-1/current identities " + p, match(git("show", BASE + ":" + p), f["before"]) and match(git("show", PREV + ":" + p), f["candidate_1"]) and match((ROOT / p).read_bytes(), f["after"]))
for key, commit in [("full_normative_diff", BASE), ("complete_amendment_normative_diff", PREV)]:
    obj = norm[key]; raw = (OUT / obj["path"]).read_bytes()
    check("complete exact " + key, raw == git("diff", "--binary", commit, "--", *paths) and sha(raw) == obj["sha256"] and len(raw) == obj["bytes"])
ledger = read("formal-change-log.json")
check("seventy-one retained/two new final clauses", len(ledger["changes"]) == 73 and ledger["changes"][:71] == read("formal-change-log.json", True)["changes"])
for e in ledger["changes"]:
    check("current final clause " + e["path"] + " " + e["clause"], e["after_text"] in (ROOT / e["path"]).read_text())
check("thirty-two exact-authorized original clauses", norm["approved_original_clause_count"] == 32 and sum(len(f["clauses"]) for f in old_originals) + sum(len(f["clause_changes"]) for f in proposal["files"] if f["path"].startswith("specs/")) == 32)

coverage = read("read-coverage.json")
check("seventy unique amended reads retain all sixty-two fixed inputs", len(coverage["readers"]) == 70 and len({r["path"] for r in coverage["readers"]}) == 70 and {r["path"] for r in read("read-coverage.json",True)["readers"]} <= {r["path"] for r in coverage["readers"]})
for row in coverage["readers"]:
    before = row["frozen_input"]; now = row["current_refreeze"]
    raw = git("show", now["commit"] + ":" + row["path"]) if now["commit"] else (ROOT / row["path"]).read_bytes()
    check("input/refreeze " + row["path"], match(git("show", before["commit"] + ":" + row["path"]), before) and match(raw, now))
check("bounded reading limits honest", coverage["semantic_full_all_amended_claimed"] is False)
c = json.loads((ROOT / CONTRACT).read_text())
disp = read("contribution-dispositions.json")
check("twenty contributions/thirteen primary/canonical OPEN", len(disp["dispositions"]) == 20 and sum(d["primary"] for d in disp["dispositions"]) == 13 and {d["id"] for d in disp["dispositions"]} == set(c["contribution_finding_ids"]) and all(d["canonical_state"] == "OPEN" and d["canonical_closed"] is False for d in disp["dispositions"]))
old_disp = {d["id"]:d for d in read("contribution-dispositions.json",True)["dispositions"]}
for d in disp["dispositions"]:
    check("complete effective qualification and pending-owner preservation " + d["id"], d["source_control"] == old_disp[d["id"]]["source_control"] and d["other_contributors_pending"] == old_disp[d["id"]]["other_contributors_pending"])
    if d["id"] != "GIR-FD82-B013":
        check("unrelated contribution unchanged " + d["id"], d == old_disp[d["id"]])

for lock in read("whole-catalog-lock-check.json")["locks"]:
    p = lock["path"]
    check("whole locked catalog unchanged from candidate-1 " + p, (ROOT / p).read_bytes() == git("show", PREV + ":" + p))
    before = git("show", BASE + ":" + p).decode(); now = (ROOT / p).read_text()
    pattern = r"^\| ([A-Z]+-?\d+b?) \|"
    a = re.findall(pattern,before,re.M); b = re.findall(pattern,now,re.M)
    check("catalog old IDs/order/multiplicity " + p, len(b) == len(set(b)) and [x for x in b if x in a] == a)
static = read("static-cases.json"); old_static = read("static-cases.json",True)
check("all static prerequisites and designs unchanged", static["catalog_cases"] == old_static["catalog_cases"] and static["supplemental_designs"] == old_static["supplemental_designs"] and len(static["catalog_cases"]) == 43 and len(static["supplemental_designs"]) == 18 and all(x["executed"] is False for x in static["catalog_cases"]+static["supplemental_designs"]))
all_cases = {e["id"] for e in static["catalog_cases"]+static["supplemental_designs"]}
check("amendment crosscheck IDs resolve", set(static["amendment_crosschecks"]["directly_consume"]) <= all_cases)
dep = read("semantic-dependency-log.json")
for e in dep["untouched_owner_consumer_clauses"]:
    a,b = e["lines"]; p=e["path"]
    now = "".join((ROOT / p).read_text().splitlines(keepends=True)[a-1:b])
    before = "".join(git("show",PREV+":"+p).decode().splitlines(keepends=True)[a-1:b])
    check("bounded unchanged owner/consumer clause " + p + " " + str(e["lines"]), now == before == e["text"])

for batch in ["B04","B05","B07","B08"]:
    req = read("affected-"+batch+"-review-request.json")
    check("separate bounded candidate+actual review " + batch, req["author_approval"] is False and req["author_impact_disposition"] == "AFFECTED_SEPARATE_INDEPENDENT_CANDIDATE_AND_ACTUAL_REQUIRED" and req["independent_review"]["candidate_required"] is True and req["independent_review"]["actual_required"] is True)
    check("current amended read coverage request " + batch, len(read(req["all_amended_current_refreeze"])["readers"]) == 70)
check("B05 review original/final exact four clauses and held-item boundary", len(read("affected-B05-review-request.json")["exact_four_before_after_clauses"]) == 4 and read("affected-B05-review-request.json")["no_new_B05_contribution_or_primary_count"] is True)
limits = read("source-limits.json")
check("all inherited named source/configuration limits preserved", all(limits[k] == v for k,v in read("source-limits.json",True).items()) and limits["contract_source_limits"] == c["source_limits"])
check("reference exact/detached/clean", git("rev-parse","HEAD",cwd=SOURCE).decode().strip() == REF and git("rev-parse","HEAD^{tree}",cwd=SOURCE).decode().strip() == REF_TREE and git("branch","--show-current",cwd=SOURCE) == b"" and git("status","--porcelain=v1","--untracked-files=all",cwd=SOURCE) == b"")
for e in read("source-reading-log.json")["amendment_rereads"]:
    raw=git("show",REF+":"+e["path"],cwd=SOURCE)
    check("amendment reference identity/range " + e["path"], match(raw,e) and all(1 <= a <= b <= len(raw.decode().splitlines()) for a,b in e["displayed_text_ranges"]))
check("zero runtime/source/vector/Demo claims", limits["reference_execution"] == static["executed"] == limits["behavior_vectors_executed"] == limits["runtime_observations"] == limits["proven_Demo_chains"] == 0)
registry=read("registry-change-proposals.json")
check("AREG sole public writer/no canonical closure", registry["public_paths_modified"] == [] and registry["canonical_CLOSED"] == 0 and registry["new_canonical_ids"] == 0)
check("B14 serialization unchanged", scope["B09_B14_serialization"] == c["B09_B14_operational_serialization"])
subprocess.run(["git","diff","--check",BASE,"--",".",":(exclude)**/*.patch"],cwd=ROOT,check=True)
check("document/non-patch evidence whitespace", True, "Exact unified-diff blank context markers preserved; all patch hashes checked separately.")
report=dict(status="PASS_AMENDED_DOCUMENT_SCOPE_AND_IDENTITY_SELF_CHECK_ONLY", baseline=BASE, previous_candidate=PREV, checks_count=len(checks), checks=checks, normative_paths=14, final=8, approved_originals=6, read_bindings=70, contributions=20, primary=13, final_clauses=73, original_clauses=32, existing_twelve_unchanged=True, candidate_1_history_unchanged=True, WP20_exact_amendment_applied=True, independent_approval=False, behavioral_semantics_proven=False, reference_execution=0,behavior_vectors_executed=0,runtime_observations=0,proven_Demo_chains=0,canonical_OPEN=229,canonical_CLOSED=0,outstanding=["Full R-B09 exact candidate and actual Ultra/Standard", "Separate affected B04/B05/B07/B08 exact candidate and actual Ultra/Standard", "AREG integration/registry proposals only after required gates", "B14 formal after accepted B09-C and mandated refreeze"], scope_blockers=[])
(OUT / "author-self-check.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:report[k] for k in ["status","checks_count","normative_paths","read_bindings","WP20_exact_amendment_applied","independent_approval","scope_blockers"]}))
