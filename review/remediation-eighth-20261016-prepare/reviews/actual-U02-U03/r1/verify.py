"""Bounded immutable-object checks. Does not execute reference code or issue a review verdict."""
import collections
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
OUT = pathlib.Path(__file__).resolve().parent
REF = ROOT.parent / "pokemon-essentials"
INPUT = "9d1809f9727000aeebe598f109ddaa15cce4026e"
ART = "908273093e1f6b27fc58249417675dd62d146224"
BASE = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
B8 = "fd1df570cad987dc3852a3b958f03916e317f7fe"
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
RR = "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/"
PREP = "review/remediation-eighth-20261016-prepare/"
SCOPE = PREP + "reviews/actual-U02-U03/r1/"
FORMAL = "deliverables/final-specification-set/"
COMMANDS = []
ERRORS = []
CACHE = {}


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args, repo=ROOT, ok=True):
    p = subprocess.run(["git", *args], cwd=repo, capture_output=True)
    COMMANDS.append(dict(argv=["git", *args], cwd=str(repo), utc=utc(), exit=p.returncode,
                         stdout_bytes=len(p.stdout), stdout_sha256=sha(p.stdout),
                         stderr=p.stderr.decode(errors="replace")))
    if ok and p.returncode:
        raise RuntimeError(COMMANDS[-1])
    return p.stdout


def data(commit, path, repo=ROOT):
    key = (str(repo), commit, path)
    if key not in CACHE:
        CACHE[key] = git("show", commit + ":" + path, repo=repo)
    return CACHE[key]


def js(commit, path):
    return json.loads(data(commit, path))


def tree(commit, prefix="", repo=ROOT):
    result = {}
    args = ["ls-tree", "-r", "-z", commit]
    if prefix:
        args.extend(["--", prefix])
    for line in git(*args, repo=repo).split(b"\0"):
        if line:
            meta, path = line.split(b"\t", 1)
            result[path.decode()] = tuple(meta.decode().split())
    return result


def identity(commit, path, repo=ROOT):
    ent = tree(commit, path, repo)[path]
    raw = data(commit, path, repo)
    return dict(commit=commit, path=path, mode=ent[0], blob=ent[2], bytes=len(raw), sha256=sha(raw))


def check(condition, meaning):
    if not condition:
        ERRORS.append(meaning)


def check_descriptor(d):
    repo = REF if d.get("repo") == str(REF) else ROOT
    actual = identity(d["commit"], d["path"], repo)
    fields = {k: (d[k], actual[k]) for k in ["mode", "blob", "bytes", "sha256"]
              if k in d and d[k] != actual[k]}
    check(not fields, dict(descriptor=d, differences=fields))
    return dict(expected=d, actual=actual, match=not fields)


def recursive_diff(a, b, path=""):
    if type(a) is not type(b):
        return [dict(path=path, old=a, current=b)]
    if isinstance(a, dict):
        out = []
        for k in sorted(a.keys() | b.keys()):
            if k not in a or k not in b:
                out.append(dict(path=path + "/" + k, old=a.get(k), current=b.get(k)))
            else:
                out.extend(recursive_diff(a[k], b[k], path + "/" + k))
        return out
    return [] if a == b else [dict(path=path, old=a, current=b)]


def readset_parent_fields(x):
    if isinstance(x, dict):
        return {k: readset_parent_fields(v) for k, v in x.items()
                if k not in ["current_recovered_at", "contract_commit", "R8_core", "records"]}
    if isinstance(x, list):
        return [readset_parent_fields(v) for v in x]
    return x


started = utc()
manifest = js(INPUT, PREP + "integration/U02-U03/actual-review-input.json")
check(manifest["artifact_snapshot_commit"] == ART, "artifact binding")
check(git("rev-parse", ART + "^{tree}").decode().strip() == manifest["artifact_workspace_tree"], "artifact tree")
check(git("rev-parse", ART + ":deliverables/final-specification-set").decode().strip() == manifest["artifact_formal_tree"], "formal tree")
payloads = [check_descriptor(d) for d in manifest["payload_identities"]]
contracts = js(ART, RR + "handoff/contracts.zh.json")["records"]
old_prefix = RR + "evidence/external-recovered/handoff_preparation_cloud/5caff3bd1a1b062b48b7eda46777a614921946f3/handoff/"
old_contracts = js(ART, old_prefix + "contracts.zh.json")
assignments = js(ART, RR + "handoff/batch-assignment.json")["batches"]
readsets = {}
contract_deltas = {}
for batch, idx in [("R8-U02", 2), ("R8-U03", 7)]:
    rs = js(ART, RR + "handoff/batches/" + batch + "/readset.json")
    inherited = rs["inherited_contents"]
    descriptors = inherited["source_spec_files"] + inherited["mandatory_root_input"] + inherited["additional_mandatory_companions"] + [rs["inherited_complete_readset"], rs["delta_complete_readset"]]
    checked = [check_descriptor(d) for d in descriptors]
    original_rs = js(ART, old_prefix + "batches/" + batch + "/readset.json")
    check(readset_parent_fields(original_rs) == readset_parent_fields(inherited), batch + " inherited parent identities preserved")
    check(original_rs["records"] == [old_contracts[idx]], batch + " original embedded full contract")
    check(inherited["records"] == [dict(id=contracts[idx]["id"], path="handoff/contracts.zh.json", pointer="/records/" + str(idx))], batch + " current contract locator")
    readsets[batch] = dict(descriptors=len(checked), identities=checked,
                          source_spec=len(inherited["source_spec_files"]), root_input=64, extra_companions=8,
                          delta_scope=rs["delta_contents"], semantic_credit="IDENTITY_ONLY; bounded readings separately in reading-ledger.json")
    assignment = next(x for x in assignments if x["id"] == batch)
    for name in ["prompt.md", "reviewer-prompt.md"]:
        text = data(ART, RR + "handoff/batches/" + batch + "/" + name).decode()
        objects = [json.loads(x.split("```")[0]) for x in text.split("```json")[1:]]
        check(objects[:2] == [assignment, contracts[idx]], batch + " embedded prompt contracts " + name)
    text = data(ART, old_prefix + "batches/" + batch + "/prompt.md").decode()
    decoder = json.JSONDecoder()
    objects = [decoder.raw_decode(text[m.start():])[0] for m in re.finditer(r"(?m)^\{", text)]
    check(objects[1:] == list(old_contracts[idx]["seven_groups"].values()), batch + " original prompt seven groups")
    contract_deltas[batch] = recursive_diff(old_contracts[idx]["seven_groups"], contracts[idx]["full_contract"])

targets = {}
imports = {}
for batch in manifest["batches"]:
    b = batch["batch"]
    target = batch["actual_target_path"]
    mirror = batch["candidate_mirror_path"]
    actual = identity(ART, target)
    candidate = identity(batch["candidate_commit"], mirror)
    check({k: actual[k] for k in ["mode", "blob", "bytes", "sha256"]} == {k: candidate[k] for k in ["mode", "blob", "bytes", "sha256"]}, b + " candidate to actual")
    check(data(ART, target) == data(batch["candidate_commit"], mirror) == data(ART, mirror), b + " full bytes")
    old = data(BASE, target)
    if b == "R8-U02":
        before, after = "并提示「Changes made to file X」", ""
    else:
        before, after = "**样本**：多数 `3/15/2,5`", "**样本**：CHERI/CHESTO/PECHA/RAWST/ASPEAR `3/15/2,5`"
    check(old.decode().count(before) == 1 and old.decode().replace(before, after).encode() == data(ART, target), b + " single literal edit")
    targets[b] = dict(actual=actual, candidate=candidate, full_bytes_equal=True, single_literal_edit=True)
    prefix = PREP + "reviews/" + b + "/"
    source_tree = tree(batch["candidate_review_source_commit"], prefix)
    art_tree = tree(ART, prefix)
    check(source_tree == art_tree, b + " candidate report file set/modes/blobs")
    for path in source_tree:
        check(data(batch["candidate_review_source_commit"], path) == data(ART, path), b + " import bytes " + path)
    result = js(ART, batch["candidate_review_result_path"])
    check(result["verdict"] == "PASS", b + " candidate verdict")
    bound = result.get("candidate_commit", result.get("fixed_inputs", {}).get("candidate"))
    check(bound == batch["candidate_commit"], b + " candidate result binding")
    imports[b] = dict(commit=batch["candidate_review_source_commit"], file_count=len(source_tree), exact=True,
                      files=[identity(ART, p) for p in source_tree])

formal_old, formal_new = tree(B8, FORMAL), tree(ART, FORMAL)
changed = [p for p in formal_old if formal_old[p] != formal_new.get(p)]
check(formal_old.keys() == formal_new.keys() and len(formal_old) == 131, "formal exact set of 131")
check(set(changed) == {b["actual_target_path"] for b in manifest["batches"]}, "formal changed set")
unchanged = []
for p in formal_old:
    if p not in changed:
        check(data(B8, p) == data(ART, p), "formal preserved bytes " + p)
        unchanged.append(identity(ART, p))
protection = {}
for base in [B8, BASE]:
    old_all, new_all = tree(base), tree(ART)
    historical = [p for p in old_all if p.startswith("review/")]
    check(all(old_all[p] == new_all.get(p) for p in historical), base + " existing review protected")
    groups = {}
    for prefix in ["AGENTS.md", "audit/", "planning/", "specs/", RR]:
        a = {p: x for p, x in old_all.items() if p == prefix or p.startswith(prefix)}
        z = {p: x for p, x in new_all.items() if p == prefix or p.startswith(prefix)}
        match = a == z if a or prefix != RR else True
        check(match, base + " protected " + prefix)
        groups[prefix] = dict(files=len(a), protected_existing_set_equal=match,
                              exact_set_equal=a == z, new_eighth_review_not_present_in_B8=not a and prefix == RR)
    protection[base] = dict(groups=groups, existing_review_paths=len(historical), existing_review_modified_or_deleted=0)
base_tree, art_tree = tree(BASE), tree(ART)
changed_all = sorted(p for p in base_tree.keys() | art_tree.keys() if base_tree.get(p) != art_tree.get(p))
check(all(p.startswith(PREP) or p in changed for p in changed_all), "integration write scope")
check(data(ART, PREP + "integration/U02-U03/formal-changes.patch") == git("diff", "--unified=0", BASE, ART, "--", FORMAL), "full changed-lines diff exact")
check(git("rev-parse", "HEAD", repo=REF).decode().strip() == R, "reference HEAD")
check(not git("status", "--porcelain=v1", repo=REF), "reference clean")

counts = []
for p in ["PBS/berry_plants.txt"] + ["PBS/Gen " + str(g) + " backup/berry_plants.txt" for g in [5, 6, 7, 8]]:
    raw = data(R, p, REF)
    records = {}
    for line in raw.decode("utf-8-sig").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("["):
            key = line[1:-1]
            check(key not in records, p + " duplicate ID")
            records[key] = {}
        else:
            k, v = [s.strip() for s in line.split("=", 1)]
            check(k not in records[key], p + " duplicate field")
            records[key][k] = tuple(int(x.strip()) for x in v.split(","))
    tuples = {k: v["HoursPerStage"] + v["DryingPerHour"] + v["Yield"] for k, v in records.items()}
    matches = [k for k, v in tuples.items() if v == (3, 15, 2, 5)]
    check(len(records) == (64 if "Gen 5" in p else 67), p + " denominator")
    check(matches == ["CHERIBERRY", "CHESTOBERRY", "PECHABERRY", "RAWSTBERRY", "ASPEARBERRY"], p + " five sample identities")
    counts.append(dict(identity=identity(R, p, REF), records=len(records), matching=len(matches), matched_ids=matches,
                       razz=tuples["RAZZBERRY"], combinations=[dict(values=k, count=v) for k, v in sorted(collections.Counter(tuples.values()).items())]))

registry = {}
for c in [ART, INPUT]:
    reg = js(c, PREP + "coordination/task-registry.json")
    selected = [x for x in reg["tasks"] if x.get("batch") in ["R8-U02", "R8-U03"]]
    for x in selected:
        check(not x["ACCEPTED"] and not x["CLOSED"] and not x["independent_review"]["actual_integrated_PASS"], "no early gate promotion")
    check(reg["counts"]["candidate_reviews_PASS_received"] == 2 and reg["counts"]["actual_integrated_reviews_PASS_received"] == 0, "registry gates distinct")
    registry[c] = dict(phase=reg["phase"], counts=reg["counts"], tasks=selected)
result = dict(schema="r8-bounded-actual-object-verification/v1", started_utc=started, finished_utc=utc(),
              input_binding_commit=INPUT, artifact_snapshot_commit=ART, qualification="TOOL_VALIDATION_ONLY; no semantic verdict",
              payload_identities=payloads, readset_identities=readsets, contract_deltas=contract_deltas,
              targets=targets, candidate_review_imports=imports, formal_files_total=len(formal_new), formal_files_changed=changed,
              formal_files_unchanged=unchanged, protection=protection, integration_changed_paths=changed_all,
              reference=dict(commit=R, clean=True), explicit_record_counts=counts, registry=registry,
              errors=ERRORS, ok=not ERRORS, Ruby_game_host_execution="NOT_EXECUTED")
(OUT / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
(OUT / "commands.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in COMMANDS))
print(json.dumps(dict(ok=not ERRORS, errors=ERRORS, payloads=len(payloads), readsets={k:v["descriptors"] for k,v in readsets.items()},
                      formal_changed=len(changed), formal_unchanged=len(unchanged), imported_files=sum(x["file_count"] for x in imports.values()),
                      explicit_record_counts=[(x["records"],x["matching"]) for x in counts], git_commands=len(COMMANDS)), ensure_ascii=False))
sys.exit(bool(ERRORS))
