"""New reviewer bookkeeping only. Does not load or execute repository programs."""
import hashlib
import difflib
import json
import re
import subprocess
from pathlib import Path

BASE = "8e67f780c204d593d89f364f585d2c6c2fe74631"
CANDIDATE = "5845e8084ced280e51c51a4081ec8583a9c2ca39"
PUBLICATION = "1dc5cc80854e02965b9bb7a02c00a7c40d392f89"
MANAGEMENT = "e8caada4ab919e48e3dc817f0638ce595fde449c"
SCOPE = "2b23c82947bcecec4ab059d63048f9b67586575b"
PREFIX = "review/remediation/20261003-prepare/batches/B13/"
AUTHOR = PREFIX + "author-draft-1/"
OUT = Path(PREFIX + "candidate-review-1")

def git(*args):
    return subprocess.check_output(["git", *args])

def content(ref, path):
    return git("show", ref + ":" + path)

def obj(ref, path):
    return json.loads(content(ref, path))

def identity(ref, path):
    b = content(ref, path)
    return {"commit": ref, "path": path, "git_blob": git("rev-parse", ref + ":" + path).decode().strip(),
            "sha256": hashlib.sha256(b).hexdigest(), "bytes": len(b)}

def bound(binding):
    got = identity(binding["commit"], binding["path"])
    return {"binding": binding, "actual": got,
            "matched": all(got[k] == binding[k] for k in ["git_blob", "sha256", "bytes"])}

def pointer(d, ptr):
    for k in ptr.strip("/").split("/"):
        k = k.replace("~1", "/").replace("~0", "~")
        d = d[int(k)] if isinstance(d, list) else d[k]
    return d

def tree(ref):
    raw = git("ls-tree", "-rz", "--full-tree", ref)
    result = {}
    for entry in raw.split(b"\0"):
        if entry:
            meta, path = entry.split(b"\t", 1)
            mode, typ, sha = meta.decode().split()
            result[path.decode()] = {"mode": mode, "type": typ, "sha": sha}
    return result

OUT.mkdir(parents=True, exist_ok=True)
patch = git("diff", "--no-ext-diff", "--no-textconv", "--no-renames", "--binary", "--full-index", BASE, CANDIDATE)
(OUT / "FIX_BASE-to-candidate.full.patch").write_bytes(patch)
before, after = tree(BASE), tree(CANDIDATE)
paths = sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))
outputs = obj(CANDIDATE, AUTHOR + "scope-applied-1/all-11-output-identities.json")
allowed = {r["path"] for r in outputs["records"]}
changes = [{"path": p, "before": before.get(p), "after": after.get(p),
            "category": "FORMAL11" if p in allowed else "AUTHOR_EVIDENCE" if p.startswith(AUTHOR) else "CANDIDATE_PACKAGE" if p.startswith(PREFIX + "candidate-1/") else "UNEXPECTED"} for p in paths]
output_checks = []
for r in outputs["records"]:
    a, b = identity(BASE, r["path"]), identity(CANDIDATE, r["path"])
    output_checks.append({"path": r["path"], "kind": r["kind"], "before": a, "after": b,
        "author_input_matched": all(a[k] == r["formal_input"][k] for k in ["git_blob", "sha256", "bytes"]),
        "author_output_matched": all(b[k] == r["output"][k] for k in ["git_blob", "sha256", "bytes"]),
        "publication_same_bytes": content(CANDIDATE, r["path"]) == content(PUBLICATION, r["path"])})

controls = obj(CANDIDATE, AUTHOR + "original-and-acceptance-controls.json")
control_checks = []
for c in controls["controls"]:
    original_binding = c["whole_original_object_binding"]
    approved_binding = c["whole_approved_acceptance_binding"]
    original = pointer(obj(original_binding["commit"], original_binding["path"]), original_binding["pointer"])
    approved = pointer(obj(approved_binding["commit"], approved_binding["path"]), approved_binding["pointer"])
    current = c["complete_current_control_fields"]
    control_checks.append({"id": c["id"], "primary": c["primary"], "primary_owner": c["primary_owner"],
        "original_binding": bound(original_binding), "approved_binding": bound(approved_binding),
        "whole_original_equal": original == c["whole_original_object"],
        "whole_approved_equal": approved == c["whole_approved_acceptance_object"],
        "current_field_equal_to_whole_original": {k: v == original.get(k) for k, v in current.items()},
        "accepted_contributors_retained": c["accepted_contributors"],
        "scope_rule": c["scope_rule"], "semantic_verdict_is_separate": True})
management_controls = PREFIX + "refreeze-after-B12-C-1/original-and-acceptance-controls.json"
copy_checks = [{"source": identity(MANAGEMENT, management_controls),
    "copy": identity(CANDIDATE, AUTHOR + "original-and-acceptance-controls.json"),
    "same_bytes": content(MANAGEMENT, management_controls) == content(CANDIDATE, AUTHOR + "original-and-acceptance-controls.json")},
    {"source": identity(SCOPE, PREFIX + "scope-amendment-1/scope-amendment.json"),
    "copy": identity(CANDIDATE, AUTHOR + "scope-applied-1/scope-amendment.json"),
    "same_bytes": content(SCOPE, PREFIX + "scope-amendment-1/scope-amendment.json") == content(CANDIDATE, AUTHOR + "scope-applied-1/scope-amendment.json")}]
scope = obj(SCOPE, PREFIX + "scope-amendment-1/scope-amendment.json")
scope_checks = []
for r in scope["records"]:
    scope_checks.append({"path": r["path"], "before": bound(r["before"]),
        "after_binding": bound(r["after_to_apply"]), "candidate": identity(CANDIDATE, r["path"]),
        "candidate_equals_exact_proposed_after": content(CANDIDATE, r["path"]) == content(r["after_to_apply"]["commit"], r["after_to_apply"]["path"])})
scope_patch = git("diff", "--no-ext-diff", "--no-textconv", "--no-renames", "--binary", "--full-index", BASE, CANDIDATE, "--", *scope["allowed_original_write_paths"])
scope_patch_bound = scope["source_whole_patch"]
approved_format_patch = "".join("".join(difflib.unified_diff(content(BASE, p).decode().splitlines(True),
    content(CANDIDATE, p).decode().splitlines(True), fromfile="a/" + p, tofile="b/" + p))
    for p in scope["allowed_original_write_paths"]).encode()
scope_patch_check = {"git_diff_sha256": hashlib.sha256(scope_patch).hexdigest(), "git_diff_bytes": len(scope_patch),
    "approved_format": "Python difflib unified_diff; n=3; a/path and b/path; no Git metadata headers",
    "actual_sha256": hashlib.sha256(approved_format_patch).hexdigest(), "actual_bytes": len(approved_format_patch),
    "matched_approved_patch": approved_format_patch == content(scope_patch_bound["commit"], scope_patch_bound["path"]),
    "approved_patch_identity": bound(scope_patch_bound)}

planned = obj(CANDIDATE, AUTHOR + "planned-inputs-52.json")
planned_checks = [bound(r["input"]) for r in planned["records"]]

def rows(text):
    group = ""
    out = []
    for line in text.splitlines():
        if line.startswith("## "):
            group = line
        m = re.match(r"^\|\s*((?:Q|W|P)\d{2}[a-z]?|(?:EG|EN|FC|MG|TT)-\d+)\s*\|", line)
        if m:
            out.append({"group": group, "id": m.group(1), "row": line})
    return out

catalog_checks = []
for lock in obj(CANDIDATE, AUTHOR + "catalog-locks.json")["catalogs"]:
    p = lock["path"]
    old, new = rows(content(BASE, p).decode()), rows(content(CANDIDATE, p).decode())
    key = lambda r: (r["group"].split("（")[0], r["id"])
    # Group count labels may change; IDs can recur across WS and RC.
    def group_key(r):
        m = re.match(r"##\s+([A-Z]+|\d+)", r["group"])
        return (m.group(1) if m else r["group"], r["id"])
    newmap = {group_key(r): r for r in new}
    old_keys = [group_key(r) for r in old]
    preserved = [group_key(r) for r in new if group_key(r) in set(old_keys)]
    changed = [{"group": r["group"], "id": r["id"], "before": r["row"], "after": newmap[group_key(r)]["row"]}
               for r in old if group_key(r) in newmap and r["row"] != newmap[group_key(r)]["row"]]
    added = [r for r in new if group_key(r) not in set(old_keys)]
    counts = lambda rs: {g: sum(r["group"] == g for r in rs) for g in dict.fromkeys(r["group"] for r in rs)}
    catalog_checks.append({"path": p, "old_count": len(old), "new_count": len(new),
        "old_counts_by_heading": counts(old), "new_counts_by_heading": counts(new),
        "old_order_and_multiplicity_preserved": old_keys == preserved,
        "missing_old_ids": [k for k in old_keys if k not in newmap],
        "changed_old_rows": changed, "added_rows": added,
        "other_owner_rows_byte_equal": all(r["row"] == newmap[group_key(r)]["row"] for r in old if not r["id"].startswith("FC-")) if p.endswith("creature-rpg-wp35-36-57-64-68.md") else None,
        "execution_claim": "STATIC_UNEXECUTED"})

protected = [p for p in before if p not in allowed and not p.startswith(PREFIX)]
protected_changed = [p for p in protected if before[p] != after.get(p)]
evidence = {"kind": "INDEPENDENT_NEW_GIT_JSON_HASH_TEXT_METADATA_ONLY_NOT_BEHAVIOR_EXECUTION",
    "reviewed_candidate": CANDIDATE, "reviewed_tree": git("rev-parse", CANDIDATE + "^{tree}").decode().strip(),
    "formal_FIX_BASE": BASE, "publication_navigation_only": PUBLICATION,
    "complete_unfiltered_diff": {"argv": ["git", "diff", "--no-ext-diff", "--no-textconv", "--no-renames", "--binary", "--full-index", BASE, CANDIDATE],
        "bytes": len(patch), "sha256": hashlib.sha256(patch).hexdigest(), "changed_paths": len(paths),
        "stored": "FIX_BASE-to-candidate.full.patch", "semantic_review_not_inferred_from_hash": True},
    "changes": changes, "unexpected_changes": [r for r in changes if r["category"] == "UNEXPECTED"],
    "all11_outputs": output_checks, "control_bindings": control_checks, "management_copy_identity": copy_checks,
    "exact_original_scope": scope_checks, "exact_original_whole_patch": scope_patch_check,
    "planned52_identity": planned_checks, "catalog_checks": catalog_checks,
    "whole_preexisting_path_protection": {"checked_paths": len(protected), "changed": protected_changed,
        "limited_to_byte_identity_preservation_not_semantic_acceptance": True},
    "publication_delta": git("diff", "--name-status", CANDIDATE, PUBLICATION).decode().splitlines(),
    "reference_Ruby_game_vectors_historical_programs_executed": 0,
    "B030_required": False, "B030_count": 0, "WP67A_B16_obligation_closed": False}
(OUT / "independent-metadata.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"changed_paths": len(paths), "full_diff_bytes": len(patch),
    "unexpected": evidence["unexpected_changes"], "all11_match": all(r["author_input_matched"] and r["author_output_matched"] for r in output_checks),
    "all8_whole_controls_equal": all(r["whole_original_equal"] and r["whole_approved_equal"] for r in control_checks),
    "all52_match": all(r["matched"] for r in planned_checks), "protected_changed": protected_changed,
    "exact4_patch_equal": scope_patch_check["matched_approved_patch"],
    "catalogs": [{k: r[k] for k in ["path", "old_count", "new_count", "old_order_and_multiplicity_preserved", "missing_old_ids"]} for r in catalog_checks]}, ensure_ascii=False))
