"""Finite data/identity checks only. Does not execute reference or a battle model."""
import concurrent.futures, datetime, difflib, hashlib, json, re, subprocess, sys
import urllib.parse, urllib.request
from pathlib import Path

D = Path(__file__).resolve().parent
ROOT = D.parents[3]
PRE = D.parents[1]
A = "64c77cf1733ab7db300e9f5ac7c79a2886c8ac68"
P = "469a268b92daed7b4d28d7fd0da75520cbb7228f"
M = "8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
C = "83cbd3fd2fbdf436a0e6788902f7bdd8918efbbb"
GROUPS = ["identity_and_verdict", "bidirectional_evidence", "premises_and_counterexample",
          "minimum_revision_contract", "acceptance_and_regression", "independent_adjudication",
          "dependencies_and_receivers"]
checks = []
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(b):
    return {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest(),
            "git_blob": hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()}
def canonical(x):
    return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def git(*a): return subprocess.check_output(["git", *a], cwd=ROOT)
def load(p): return json.loads(p.read_bytes())
def blob(commit, path): return git("show", commit + ":" + path)
def test(name, value, evidence=None):
    checks.append({"name": name, "pass": bool(value), "evidence": evidence})
def identity_matches(b, row): return all(ident(b)[k] == row[k] for k in ident(b))
def rel(p): return str(p.relative_to(ROOT))
def pointer(x, p):
    for t in p.strip("/").split("/"):
        t = t.replace("~1", "/").replace("~0", "~")
        x = x[int(t)] if isinstance(x, list) else x[t]
    return x
def cover(rows, path, commit, a, z):
    spans = [r["read_range"] for r in rows if r.get("exit") == 0 and r.get("path") == path and r.get("commit") == commit]
    return all(any(x <= n <= y for x, y in spans) for n in range(a, z + 1))
def get(repo, commit, path):
    url = "https://raw.githubusercontent.com/" + repo + "/" + commit + "/" + urllib.parse.quote(path)
    t = now()
    with urllib.request.urlopen(url, timeout=40) as response:
        b = response.read(); status = response.status
    return b, {"utc_start": t, "utc_end": now(), "url": url, "http_status": status, **ident(b)}

t0 = now()
contract_path = PRE / "contracts/R6-U05.json"
contract = load(contract_path)
prompt_path = PRE / "prompts/R6-U05-R.md"
prompt = prompt_path.read_bytes()
blocks = re.findall(r"```json\s*\n(.*?)\n```", prompt.decode(), flags=re.S)
test("prompt exact requested identity", identity_matches(prompt, {"bytes": 268511,
     "sha256": "3896335f207f8a52a722b2830692b4479acea9b569e1c0224f2e4aca5ab4c49e",
     "git_blob": "829e21d41537cc0dd9e3e612e3233675583a2a15"}), ident(prompt))
test("complete embedded contract equals standalone", json.loads(blocks[0]) == contract)
recovery = json.loads(blocks[1])
test("complete prompt recovery dictionary has 115 unique bindings", len(recovery) == 115, len(recovery))
test("prepare ancestor of frozen author", subprocess.run(["git", "merge-base", "--is-ancestor", P, A], cwd=ROOT).returncode == 0)
test("frozen author workspace tree", git("rev-parse", A + "^{tree}").decode().strip() == "1cf207996da85adaa677a5a3bcb2c7cf47fd8859")
test("frozen mirror tree", git("rev-parse", A + ":" + rel(PRE / "candidates/R6-U05/mirror")).decode().strip() == "ecc24a2e991ba0eaaf1964ceaa076af551846778")
test("formal subtree unchanged between main/prepare/author", len({git("rev-parse", x + ":deliverables/final-specification-set").strip() for x in [M,P,A]}) == 1)
changed = git("diff", "--name-only", P, A).decode().splitlines()
test("author 58 changes all owned candidate paths", len(changed) == 58 and all(x.startswith(rel(PRE / "candidates/R6-U05") + "/") for x in changed), changed)
ev = PRE / "candidates/R6-U05/evidence"
author = load(ev / "author-results.json")
test("four original contracts", len(contract["scope_contracts"]) == 4 and contract["required_ids"] == [s["id"] for s in contract["scope_contracts"]])
for s in contract["scope_contracts"]:
    ar = next(x for x in author["per_id"] if x["id"] == s["id"])
    for g in GROUPS:
        test(s["id"] + " author frozen group " + g, ar["seven_groups"][g]["frozen_input"] == s[g], canonical(s[g]))
for fname, key, commit in [("payload-manifest.json", "core_payloads", C), ("publication-manifest.json", "publication_only_payloads", A)]:
    man = load(ev / fname)
    for row in man[key]:
        b = blob(commit, row["path"])
        metadata = git("ls-tree", commit, "--", row["path"]).decode().strip().split()
        test("author payload " + row["path"], identity_matches(b, row) and metadata[:3] == [row["mode"], "blob", row["git_blob"]])
rows = [json.loads(x) for x in (D / "reading-ledger.jsonl").read_text().splitlines()]
frozen = load(PRE / "inputs/frozen-inputs.json")
formal_index = {r["path"]: r for r in frozen["formal_materials"]}
file_bindings, differences, new_vectors = [], [], []
for p in contract["candidate_formal_paths"]:
    before = blob(M, p)
    cp = rel(PRE / "candidates/R6-U05/mirror" / p)
    after = blob(A, cp)
    test("formal identity " + p, identity_matches(before, formal_index[p]))
    test("formal full read " + p, cover(rows, p, M, 1, len(before.decode().splitlines())))
    test("candidate unchanged core to publication " + p, blob(C, cp) == after)
    metadata = git("ls-tree", A, "--", cp).decode().strip().split()
    file_bindings.append({"formal_path": p, "formal_commit": M, "formal": ident(before),
                          "candidate_path": cp, "candidate_commit": A, "candidate": ident(after),
                          "mode": metadata[0], "git_object_type": metadata[1],
                          "formal_full_semantic_read": True, "candidate_read": "FULL_BASELINE_PLUS_COMPLETE_DIFF"})
    differences.append("".join(difflib.unified_diff(before.decode().splitlines(True), after.decode().splitlines(True), fromfile=M+":"+p, tofile=A+":"+cp)))
    if "/test-catalog/" in p:
        old = {m.group(1): line for line in before.decode().splitlines() if (m := re.match(r"\| ((?:SS\d+|MA-T\d+)) \|", line))}
        current = [(m.group(1), n, line) for n,line in enumerate(after.decode().splitlines(),1) if (m := re.match(r"\| ((?:SS\d+|MA-T\d+)) \|", line))]
        test("all previous test rows preserved " + p, all(sum(id == k and line == v for id,_,line in current) == 1 for k,v in old.items()))
        for id,n,line in current:
            if id not in old: new_vectors.append({"id":id,"path":cp,"line":n,"complete_row":line,"level":"DERIVED_VECTOR","executed":False})
test("exact 23 new unique vectors", sorted(x["id"] for x in new_vectors) == sorted(["SS"+str(x) for x in range(43,60)]+["MA-T"+str(x) for x in range(11,17)]))
sources = []
for s in contract["scope_contracts"]:
    for r in s["bidirectional_evidence"]["source"]:
        loc = r["locator"];p = r["payload_identity"]["path"]
        a,z = loc.get("range", [loc.get("start"), loc.get("end")])
        matches = [x for x in rows if x.get("exit") == 0 and x.get("kind") == "source" and x.get("path") == p]
        test(s["id"] + " bound source read " + p + ":"+str(a)+"-"+str(z), cover(rows,p,R,a,z) and all(all(x["identity"][k] == r["payload_identity"][k] for k in ["bytes","sha256","git_blob"]) for x in matches))
        sources.append({"id":s["id"],"path":p,"range":[a,z],"identity":r["payload_identity"],"read_coverage":cover(rows,p,R,a,z)})
counter = []
for id in contract["scope_contracts"][0]["bidirectional_evidence"]["counter_evidence_ids"]:
    r = recovery[id];p = rel(PRE / "inputs/evidence" / r["path"]);b = blob(A,p)
    test("counter identity/full read " + id, identity_matches(b,r) and cover(rows,p,A,1,len(b.decode().splitlines())))
    counter.append({"id":id,"path":p,"recovery_binding":r,"identity":ident(b),"full_semantic_read":True})
regressions = []
for r in load(ev / "historical-relations.json")["relations"]:
    a,z = r["formal_lines"];p=r["formal_path"]
    b = "\n".join(blob(M,p).decode().splitlines()[a-1:z])
    after = blob(A,rel(PRE / "candidates/R6-U05/mirror" / p)).decode()
    exact = b in after
    extension = not exact and all(sentence in after for line in b.splitlines() for sentence in line.split("。") if sentence)
    test("qualified historical span " + r["historical_scope_consumer"] + " " + p + ":"+str(a)+"-"+str(z), exact or extension)
    regressions.append({**r,"full_old_span":b,"status":"EXACT_CONTINUOUS_TEXT_PRESERVED" if exact else "OLD_SENTENCES_RETAINED_WITH_BOUNDED_ADDITION" if extension else "FAIL","new_game_PASS":False})
test("33 qualified spans: 32 exact/1 bounded extension", len(regressions)==33 and sum(r["status"]=="EXACT_CONTINUOUS_TEXT_PRESERVED" for r in regressions)==32 and sum(r["status"]=="OLD_SENTENCES_RETAINED_WITH_BOUNDED_ADDITION" for r in regressions)==1)
bindings = load(ev / "historical-input-bindings.json")
def recover(item):
    p,r = item;b,rec=get("y805939188/pokemon-essentials-clean-room",r["commit"],p)
    return p,json.loads(b),rec,identity_matches(b,r)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    recovered = list(pool.map(recover,bindings["files"].items()))
hist_objects={p:x for p,x,_,_ in recovered}
for p,x,rec,ok in recovered:test("full fixed historical payload " + p,ok,rec)
selected = load(ev / "selected-historical-scopes.json")
for r in bindings["selected_records"]:
    fr=r["frozen_record"];qs=r["qualified_scope_binding"];x=hist_objects[fr["path"]]
    raw_record=pointer(x,fr["pointer"]);qualified=pointer(x,qs["pointer"])
    same=next(x for x in selected if x["id"]==r["id"] and x["record_key"]==r["record_key"] and x["owner"]==r["batch_owner"])
    test("qualified historical tuple " + r["id"] + " " + str(r["record_key"]), canonical(raw_record)==fr["record_sha256"] and canonical(qualified)==qs["record_sha256"] and same["qualification"]=={k:qualified[k] for k in qs["scope_keys"]}, r)
test("41 exact qualified projections", len(selected)==len(bindings["selected_records"])==41)
source_tree_receipt={"attempt":"independent-check-02","result":"API_METADATA_UNAVAILABLE_PROXY_TUNNEL_403","raw":"commands/independent-check-02.json","tree":"7589c800b61ba13a13040ed0d686979b80a84fd0","mode_and_type_basis":"Fixed source_materials identity index; source bytes/hash/blob independently verified via complete pinned raw GitHub payloads. No successful API tree response claimed."}
tree_index={x["path"]:x for x in frozen["source_materials"]}
for p in sorted({x["path"] for x in rows if x.get("exit")==0 and x.get("kind")=="source"}):
    entry=tree_index[p];reads=[x for x in rows if x.get("exit")==0 and x.get("kind")=="source" and x["path"]==p]
    test("fixed R indexed mode/type and actual blob " + p,entry["mode"]=="100644" and entry["type"]=="text" and all(x["identity"]["git_blob"]==entry["git_blob"] and x["identity"]["bytes"]==entry["bytes"] for x in reads),entry)
activation=load(D / "activation-qualified.json")
closure_path="review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-closure-candidate/closure-candidate.json"
closure=json.loads(blob("13fddb0a217b36974c75657aa68da0caf104ee48",closure_path))
for r in activation["selection"]:
    v=r["record"];record=closure["records"][v["record_index"]]
    test("R5 selected activation " + v["id"], record["id"]==v["id"] and canonical(record)==v["scope_record_sha256"] and canonical(pointer(closure,v["selected_state_pointer"]))==v["selected_state_record_sha256"],v)

(D/"candidate-diff.patch").write_text("\n".join(differences))
(D/"input-bindings.json").write_text(json.dumps({"schema":"r6.u05.independent-input-binding.v1","prepare":P,"author_commit":A,"author_workspace_tree":"1cf207996da85adaa677a5a3bcb2c7cf47fd8859","mirror_tree":"ecc24a2e991ba0eaaf1964ceaa076af551846778","prompt":{"path":rel(prompt_path),**ident(prompt)},"contract":{"path":rel(contract_path),**ident(contract_path.read_bytes())},"candidate_files":file_bindings,"contract_sources":sources,"counter_evidence":counter},ensure_ascii=False,indent=2)+"\n")
(D/"new-vectors.json").write_text(json.dumps(new_vectors,ensure_ascii=False,indent=2)+"\n")
(D/"historical-span-checks.json").write_text(json.dumps(regressions,ensure_ascii=False,indent=2)+"\n")
result={"schema":"r6.u05.independent-tool-checks.v1","utc_start":t0,"utc_end":now(),"cwd":str(ROOT),"argv":sys.argv,"level":"TOOL_VALIDATION","boundary":"Data identities, line coverage, old-byte preservation and qualified pointers only. No reference/model/host execution and no semantic verdict by this program.","checks":checks,"count":len(checks),"passed":sum(x["pass"] for x in checks),"failed":sum(not x["pass"] for x in checks),"historical_full_payload_reads":[r for _,_,r,_ in recovered],"actual_source_tree_readback":source_tree_receipt}
(D/"independent-checks.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:result[k] for k in ["utc_start","utc_end","level","count","passed","failed"]},ensure_ascii=False))
for x in checks:
    if not x["pass"]: print(json.dumps(x,ensure_ascii=False))
sys.exit(0 if not result["failed"] else 1)
