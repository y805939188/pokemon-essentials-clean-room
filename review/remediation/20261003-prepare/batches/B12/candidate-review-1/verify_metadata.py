"""Independent Git/JSON/hash/text metadata only. No reference program execution."""
import collections
import hashlib
import json
import pathlib
import re
import subprocess

BASE = "1d06c45cc0a744fca181ac80ee573cc9ebb9b862"
CANDIDATE = "8ddba850af71f24e7bd77a80b7605c456c31dc7a"
PACKET = "9ad5539f38544fef6037356018015fe418021514"
ROOT = "review/remediation/20261003-prepare/batches/B12/"
OUT = pathlib.Path(ROOT + "candidate-review-1")

def git(*args):
    return subprocess.check_output(["git", *args])

def read(commit, path):
    return git("show", commit + ":" + path)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def logical(obj):
    return digest(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())

def identity(commit, path):
    data = read(commit, path)
    return dict(commit=commit, path=path, git_blob=git("rev-parse", commit + ":" + path).decode().strip(), sha256=digest(data), bytes=len(data))

def verify(binding):
    got = identity(binding["commit"], binding["path"])
    return dict(identity=got, matches={k: got[k] == binding[k] for k in ("git_blob", "sha256", "bytes") if k in binding})

def pointer(obj, ptr):
    for key in ptr.strip("/").split("/"):
        obj = obj[int(key)] if isinstance(obj, list) else obj[key.replace("~1", "/").replace("~0", "~")]
    return obj

bindings = json.loads(read(CANDIDATE, ROOT + "author-draft-1/qualified-control-bindings.json"))
packet = json.loads(read(PACKET, bindings["packet_controls"]["path"]))
controls = {x["id"]: x for x in packet["controls"]}
result = dict(reviewed_commit=CANDIDATE, reviewed_tree=git("rev-parse", CANDIDATE + "^{tree}").decode().strip(), FIX_BASE=BASE)
result["packet_binding"] = verify(bindings["packet_controls"])
result["controls"] = []
for item in bindings["contributions"]:
    row = dict(id=item["id"], primary=item["primary"], current_fields_equal_packet=item["complete_current_control_fields"] == controls[item["id"]]["complete_current_control_fields"])
    for kind, key, objkey in [("original", "whole_original_object_binding", "whole_original_object"), ("acceptance", "whole_approved_acceptance_binding", "whole_approved_acceptance_object")]:
        b = item[key]
        obj = pointer(json.loads(read(b["commit"], b["path"])), b["pointer"])
        row[kind] = dict(binding=verify(b), object_hash=logical(obj), matches_declared_hash=logical(obj) == item["whole_" + kind + "_object_sha256"], full_object_equal_packet=obj == controls[item["id"]][objkey])
    result["controls"].append(row)
result["outputs"] = []
for filename in ["formal-output-identities.json", "original-output-identities.json"]:
    for item in json.loads(read(CANDIDATE, ROOT + "candidate-1/" + filename))["outputs"]:
        inp = item.get("input") or dict(commit=item["input_commit"], path=item["path"], git_blob=item["input_blob"], sha256=item["input_sha256"], bytes=item["input_bytes"])
        got = identity(CANDIDATE, item["path"])
        result["outputs"].append(dict(kind=filename, input=verify(inp), output=got, matches_output_hash=got["sha256"] == item["output_sha256"], matches_output_bytes=got["bytes"] == item["output_bytes"]))
amendment = json.loads(read(CANDIDATE, ROOT + "author-draft-1/scope-amendment-1.json"))
result["scope_amendment"] = dict(proposal=verify(amendment["approved_proposal"]), patches=[])
for p in amendment["proposals"]:
    approved = read(p["approved_patch_commit"], p["approved_patch_path"])
    candidate_patch = read(CANDIDATE, p["approved_patch_path"])
    after = read(CANDIDATE, p["path"])
    before_binding = dict(commit=p["before_commit"], path=p["path"], git_blob=p["before_git_blob"], sha256=p["before_sha256"], bytes=p["before_bytes"])
    patch_identity = identity(p["approved_patch_commit"], p["approved_patch_path"])
    after_identity = identity(CANDIDATE, p["path"])
    result["scope_amendment"]["patches"].append(dict(number=p["proposal_number"], path=p["path"], patch=patch_identity, patch_unchanged=approved == candidate_patch, matches_patch_blob=patch_identity["git_blob"] == p["approved_patch_blob"], matches_patch_hash=digest(approved) == p["approved_patch_sha256"], matches_after=digest(after) == p["approved_after_sha256"], matches_after_blob=after_identity["git_blob"] == p["actual_after_git_blob"], matches_after_bytes=len(after) == p["actual_after_bytes"], before=verify(before_binding)))
diff = git("diff", "--binary", "--no-ext-diff", "--no-textconv", BASE, CANDIDATE)
assert diff == (OUT / "FIX_BASE-to-candidate.full.diff").read_bytes()
result["full_diff"] = dict(command=["git", "diff", "--binary", "--no-ext-diff", "--no-textconv", BASE, CANDIDATE], bytes=len(diff), sha256=digest(diff))
paths = git("diff", "--name-only", "--no-ext-diff", "--no-textconv", BASE, CANDIDATE).decode().splitlines()
result["changed_files"] = [dict(path=p, output=identity(CANDIDATE, p)) for p in paths]
result["scope_counts"] = dict(total=len(paths), formal=sum(p.startswith("deliverables/") for p in paths), originals=sum(p.startswith("specs/") for p in paths), author_and_candidate_evidence=sum(p.startswith(ROOT) for p in paths), unexpected=[p for p in paths if not p.startswith(("deliverables/", "specs/", ROOT))])
result["reading_log_identities"] = [verify(x["input"]) for x in json.loads(read(CANDIDATE, ROOT + "author-draft-1/reading-log.json"))["records"]]
result["source_identities"] = [verify(x) for x in json.loads(read(CANDIDATE, ROOT + "author-draft-1/source-reading-log.json"))["static_reads"]]
result["catalogs"] = []
for p in ["deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md", "deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md"]:
    def rows(c):
        return [x for x in read(c,p).decode().splitlines() if re.match(r"^\| [A-Z]+\d+[a-z]? \|", x)]
    before, after = rows(BASE), rows(CANDIDATE)
    counts = collections.Counter(after)
    missing = []
    for row in before:
        if counts[row]: counts[row] -= 1
        else: missing.append(row)
    old_in_order = iter(after)
    ordered = all(any(x == row for x in old_in_order) for row in before)
    result["catalogs"].append(dict(path=p, old_rows=len(before), new_rows=len(after), all_old_row_bytes_and_multiplicity_preserved=not missing, all_old_rows_order_preserved=ordered, missing_or_changed=missing, added_rows=list(counts.elements())))
(OUT / "metadata-verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k:result[k] for k in ("reviewed_commit","reviewed_tree","scope_counts","full_diff")},ensure_ascii=False,indent=2))
print("controls", [(x["id"],x["current_fields_equal_packet"],x["original"]["matches_declared_hash"],x["acceptance"]["matches_declared_hash"]) for x in result["controls"]])
print("catalogs",[(x["old_rows"],x["new_rows"],x["all_old_row_bytes_and_multiplicity_preserved"],x["all_old_rows_order_preserved"]) for x in result["catalogs"]])
