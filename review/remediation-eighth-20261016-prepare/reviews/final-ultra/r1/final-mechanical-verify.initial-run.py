"""Bounded final mechanical identity/provenance verification, never semantics.

Only new files adjacent to this script may be written. No old U06 evidence,
candidate, formal, registration, ref, commit or remote state is mutated. This
script reads Git objects and worktree bytes; it executes no source/business
Ruby, candidate verification program, or imported artifact script.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / ".git").exists())
P = "review/remediation-eighth-20261016-prepare/"
FORMAL = "deliverables/final-specification-set/"
B = "8ab43a609e60430492b219f0dce14ef4fdb8e47f"
A = "fd414a2c6ec0a0f746b48e0924e5692221ea5d5a"
BASE = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
ALLOWED = str(HERE.relative_to(REPO)) + "/"
commands = []
checks = []
cache = {}
trees = {}
started = datetime.now(timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def utc():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    begin = utc()
    argv = ["git", *args]
    proc = subprocess.run(argv, cwd=REPO, capture_output=True, check=False)
    record = {"argv": argv, "cwd": str(REPO), "started_utc": begin,
              "finished_utc": utc(), "exit_code": proc.returncode,
              "stdout_bytes": len(proc.stdout), "stdout_sha256": sha(proc.stdout),
              "stderr_bytes": len(proc.stderr), "stderr_sha256": sha(proc.stderr),
              "stderr_utf8": proc.stderr.decode(errors="replace")}
    if len(proc.stdout) <= 8192:
        record["stdout_utf8"] = proc.stdout.decode(errors="replace")
    commands.append(record)
    if proc.returncode:
        raise RuntimeError(record)
    return proc.stdout


def raw(commit, path):
    return git("show", commit + ":" + path)


def tree(commit, prefix):
    key = (commit, prefix)
    if key not in trees:
        result = {}
        for line in git("ls-tree", "-r", commit, "--", prefix).decode().splitlines():
            header, path = line.split("\t", 1)
            result[path] = header.split()
        trees[key] = result
    return trees[key]


def identity(commit, path, data=None):
    key = (commit, path)
    if key not in cache:
        if data is None:
            data = raw(commit, path)
        entry = tree(commit, path)[path]
        cache[key] = {"commit": commit, "path": path, "mode": entry[0], "kind": entry[1],
                      "blob": entry[2], "bytes": len(data), "sha256": sha(data)}
    return cache[key]


def working(path, data=None):
    target = REPO / path
    mode = target.lstat().st_mode
    if stat.S_ISLNK(mode):
        content = os.readlink(target).encode()
        gitmode = "120000"
    else:
        content = target.read_bytes() if data is None else data
        gitmode = "100755" if mode & 0o111 else "100644"
    return {"path": path, "mode": gitmode, "kind": "blob", "bytes": len(content),
            "blob": hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest(),
            "sha256": sha(content)}


def same(left, right):
    return all(left[k] == right[k] for k in ["mode", "blob", "bytes", "sha256"])


def check(name, condition, evidence, boundary):
    checks.append({"name": name, "mechanical_status": "PASS" if condition else "FAIL",
                   "condition_matched": bool(condition), "evidence": evidence,
                   "semantic_boundary": boundary})


def pointer(value, path):
    if not path:
        return value
    for part in path[1:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


head = git("rev-parse", "HEAD").decode().strip()
branch = git("branch", "--show-current").decode().strip()
git("merge-base", "--is-ancestor", B, head)
check("review branch is based on exact input binding", True,
      {"input_binding": B, "head": head, "branch": branch}, "Ancestry grants no semantic acceptance.")
manifest_path = P + "final/independent-review-input.json"
index_path = P + "final/payload-identities.json"
manifest_raw = raw(B, manifest_path)
index_raw = raw(B, index_path)
m = json.loads(manifest_raw)
index = json.loads(index_raw)
assert m["artifact_snapshot_commit"] == index["artifact_snapshot_commit"] == A
assert m["fixed_delivery_commit"] == index["fixed_delivery_commit"] == BASE
index_identity = identity(B, index_path, index_raw)
check("final payload index matches the input manifest's declared identity",
      len(index_raw) == m["payload_identities"]["bytes"] and sha(index_raw) == m["payload_identities"]["sha256"]
      and index_identity["blob"] == m["payload_identities"]["git_blob"],
      {"input_manifest": identity(B, manifest_path, manifest_raw), "payload_index": index_identity},
      "JSON parse and exact file identity are not semantic FULL reading.")

availability_path = HERE / "final-object-availability.json"
availability_raw = availability_path.read_bytes()
availability = json.loads(availability_raw)
object_checks = []
for commit in m["fixed_repository_commit_objects_required"]:
    content = git("cat-file", "commit", commit)
    observed = hashlib.sha1(b"commit " + str(len(content)).encode() + b"\0" + content).hexdigest()
    object_checks.append({"commit": commit, "bytes": len(content), "content_sha256": sha(content),
                          "recomputed_commit_object_id": observed, "matched": observed == commit})
check("all 43 required exact commit objects are available and their object bytes reconstruct their IDs",
      len(object_checks) == 43 and all(x["matched"] for x in object_checks)
      and availability["all43_exact_commit_objects_available"],
      {"count": len(object_checks), "availability_receipt": str(availability_path.relative_to(REPO)),
       "availability_receipt_sha256": sha(availability_raw), "initial_missing": availability["initial_missing_count"]},
      "Object/transport availability adds no original reader, semantic or configuration credit.")

exceptions = set(m["post_snapshot_binding_records"])
payload = []
for expected in index["files"]:
    path = expected["path"]
    source = raw(A, path)
    bound = raw(B, path)
    current = (REPO / path).read_bytes()
    actual_identity = identity(A, path, source)
    bound_identity = identity(B, path, bound)
    work_identity = working(path, current)
    payload.append({"expected": expected, "artifact_observed": actual_identity,
                    "owning_identity_matched": same(expected, actual_identity),
                    "binding_observed": bound_identity, "worktree_observed": work_identity,
                    "post_snapshot_declared_exception": path in exceptions,
                    "artifact_binding_full_bytes_equal": source == bound,
                    "binding_worktree_full_bytes_equal": bound == current,
                    "artifact_binding_mode_equal": actual_identity["mode"] == bound_identity["mode"],
                    "binding_worktree_mode_equal": bound_identity["mode"] == work_identity["mode"]})
check("all 1008 artifact payload records match original full bytes mode blob bytes SHA256",
      len(payload) == index["file_count"] == 1008 and all(x["owning_identity_matched"] for x in payload)
      and sum(x["artifact_observed"]["bytes"] for x in payload) == index["total_bytes"] == 134222799,
      {"files": len(payload), "total_bytes": sum(x["artifact_observed"]["bytes"] for x in payload)},
      "Full-object byte verification is mechanical and gives no semantic FULL credit.")
unlisted_changes = [x["expected"]["path"] for x in payload
                    if not x["artifact_binding_full_bytes_equal"] and not x["post_snapshot_declared_exception"]]
check("all nonexception payload bytes remain exact at input binding and all binding bytes remain current",
      not unlisted_changes and all(x["binding_worktree_full_bytes_equal"] and x["binding_worktree_mode_equal"] for x in payload),
      {"undeclared_changed_paths": unlisted_changes, "artifact_vs_binding_equal_count": sum(x["artifact_binding_full_bytes_equal"] for x in payload)},
      "Declared successor binding records are separated below; they do not change original content acceptance.")
post_rows = git("diff", "--name-status", A, B).decode().splitlines()
post_paths = [row.split("\t")[-1] for row in post_rows]
post_snapshot = []
artifact_paths = {x["expected"]["path"] for x in payload}
for path in m["post_snapshot_binding_records"]:
    braw = raw(B, path)
    work = (REPO / path).read_bytes()
    row = {"path": path, "binding": identity(B, path, braw), "worktree": working(path, work),
           "binding_current_full_bytes_equal": braw == work,
           "name_status": next(x for x in post_rows if x.split("\t")[-1] == path)}
    row["artifact"] = identity(A, path) if path in artifact_paths else None
    row["artifact_status"] = "existing record changed" if row["artifact"] else "new successor binding record; not part of the 1008 artifact payload"
    post_snapshot.append(row)
check("artifact-to-binding change set is exactly the four declared post-snapshot records",
      set(post_paths) == exceptions and len(post_paths) == 4 and all(x["binding_current_full_bytes_equal"] for x in post_snapshot),
      {"name_status": post_rows, "declared_exception_count": len(exceptions)},
      "This is a phase/identity distinction, not a semantic endorsement of post-snapshot bookkeeping.")

base_formal = tree(BASE, FORMAL)
actual_formal = tree(A, FORMAL)
binding_formal = tree(B, FORMAL)
changed = [p for p, v in base_formal.items() if actual_formal.get(p) != v]
unchanged = [p for p, v in base_formal.items() if actual_formal.get(p) == v]
check("formal131 consists of 38 changed and 93 unchanged baseline files",
      len(base_formal) == len(actual_formal) == len(binding_formal) == 131
      and base_formal.keys() == actual_formal.keys() and actual_formal == binding_formal
      and len(changed) == 38 and len(unchanged) == 93
      and git("rev-parse", A + ":" + FORMAL.rstrip("/")).decode().strip() == m["formal_current_tree"] == index["formal_tree"],
      {"base_total": len(base_formal), "actual_total": len(actual_formal), "changed_paths": changed,
       "unchanged_paths": unchanged, "actual_tree": m["formal_current_tree"]},
      "Counts, preserved paths and content identity do not verify behavior, interfaces or scenarios.")

# All original candidate/reviewer/actual-review directories, plus exact receipts.
groups = []
group_index = {}
batch_links = []
for batch in m["batches"]:
    definitions = [("candidate", batch["candidate_commit"], P + "candidates/" + batch["batch"] + "/")]
    for field in ["candidate_review_report", "actual_integrated_review_report"]:
        r = batch[field]
        definitions.append((field, r["commit"], str(Path(r["report_path"]).parent) + "/"))
    receipt = batch["batch_ACCEPTED_receipt"]
    definitions.append(("accepted_receipt", receipt["commit"], receipt["path"]))
    link = {"batch": batch["batch"], "groups": [], "actual_integration_commit": batch["actual_integration_commit"]}
    for role, commit, prefix in definitions:
        key = (commit, prefix)
        if key not in group_index:
            rows = []
            for path in tree(commit, prefix):
                original = raw(commit, path)
                integrated = raw(A, path)
                rows.append({"source": identity(commit, path, original), "artifact": identity(A, path, integrated),
                             "full_bytes_equal": original == integrated,
                             "mode_blob_bytes_sha256_equal": same(identity(commit, path, original), identity(A, path, integrated))})
            group_index[key] = len(groups)
            groups.append({"commit": commit, "prefix": prefix, "source_files": len(rows), "files": rows})
        link["groups"].append({"role": role, "source_group_id": group_index[key]})
    rid = identity(batch["candidate_manifest_identity"]["commit"], batch["candidate_manifest_identity"]["path"])
    rr = identity(receipt["identity"]["commit"], receipt["identity"]["path"])
    receipt_object = json.loads(raw(receipt["commit"], receipt["path"]))
    link["candidate_manifest_identity_matched"] = same(batch["candidate_manifest_identity"], rid)
    link["accepted_identity_matched"] = same(receipt["identity"], rr)
    link["accepted_record_pointer"] = receipt["record_pointer"]
    link["accepted_record_pointer_resolved"] = pointer(receipt_object, receipt["record_pointer"])
    batch_links.append(link)
check("nine batches preserve complete candidate independent actual-review and accepted source groups",
      len(batch_links) == 9 and all(x["candidate_manifest_identity_matched"] and x["accepted_identity_matched"] for x in batch_links)
      and all(x["files"] and all(y["full_bytes_equal"] and y["mode_blob_bytes_sha256_equal"] for y in x["files"]) for x in groups),
      {"batch_count": len(batch_links), "distinct_source_groups": len(groups), "source_group_file_occurrences": sum(x["source_files"] for x in groups)},
      "Original verdicts and owner acceptance are historical source records; this check grants none of those gates anew.")

# The original 38 mirror contributions, plus the separately bound WP65 repair.
mirrors = []
for batch in m["batches"]:
    for source_path in tree(batch["candidate_commit"], P + "candidates/" + batch["batch"] + "/"):
        if FORMAL not in source_path:
            continue
        target = source_path[source_path.index(FORMAL):]
        original = raw(batch["candidate_commit"], source_path)
        integrated = raw(A, target)
        mirrors.append({"batch": batch["batch"], "source": identity(batch["candidate_commit"], source_path, original),
                        "formal": identity(A, target, integrated), "full_bytes_equal": original == integrated,
                        "mode_blob_bytes_sha256_equal": same(identity(batch["candidate_commit"], source_path, original), identity(A, target, integrated))})
mirror_differences = [x for x in mirrors if not x["full_bytes_equal"] or not x["mode_blob_bytes_sha256_equal"]]
repair_path = P + "integration/U04-repair-r1/change-record.json"
repair = json.loads(raw(A, repair_path))
repair_formal = identity(A, repair["changed_file"])
repair_source = identity(m["prepared_formal_source_commit"], repair["changed_file"])
check("38 final changed files map to 37 exact original mirrors plus the explicit WP65 receiver repair",
      len(mirrors) == 38 and {x["formal"]["path"] for x in mirrors} == set(changed)
      and len(mirror_differences) == 1 and mirror_differences[0]["formal"]["path"] == repair["changed_file"]
      and repair_formal["bytes"] == repair["new_bytes"] and repair_formal["sha256"] == repair["new_sha256"]
      and same(repair_formal, repair_source),
      {"original_mirror_count": len(mirrors), "exact_original_mirrors": len(mirrors) - len(mirror_differences),
       "separate_repair_record": identity(A, repair_path), "repair_target": repair_formal,
       "prepared_source": repair_source, "original_mirror_difference_paths": [x["formal"]["path"] for x in mirror_differences]},
      "The explicit later repair is kept distinct; mechanical identity does not decide its semantic adequacy.")

tagging_path = P + "integration/tagging-final-7ed3e05/source-file-identities.json"
tagging = json.loads(raw(A, tagging_path))
tagging_rows = []
for expected in tagging["files"]:
    original = raw(expected["commit"], expected["path"])
    integrated = raw(A, expected["path"])
    srcid = identity(expected["commit"], expected["path"], original)
    actualid = identity(A, expected["path"], integrated)
    tagging_rows.append({"role": expected["role"], "expected": expected, "source": srcid, "artifact": actualid,
                         "source_declared_identity_matched": same(expected, srcid),
                         "full_bytes_equal": original == integrated, "mode_blob_bytes_sha256_equal": same(srcid, actualid)})
tag_groups = Counter(x["role"] for x in tagging_rows)
check("all 175 tagging files and 75 plus 111 independent lineage files preserve exact original identities",
      len(tagging_rows) == 361 and sorted(tag_groups.values()) == [75, 111, 175]
      and all(x["source_declared_identity_matched"] and x["full_bytes_equal"] and x["mode_blob_bytes_sha256_equal"] for x in tagging_rows),
      {"groups": dict(tag_groups), "total_files": len(tagging_rows), "total_bytes": sum(x["source"]["bytes"] for x in tagging_rows)},
      "Tagging classification/calibration and historical FAIL/PASS are not re-adjudicated by byte comparison.")

u06_batch = next(x for x in m["batches"] if x["batch"] == "R8-U06")
u06_ledger_path = P + "reviews/actual-U06/r1/continuation-reading-ledger.json"
u06_ledger_raw = raw(A, u06_ledger_path)
u06_ledger = json.loads(u06_ledger_raw)
u06_reuse = []
for old in u06_ledger["all12_actual_formal_full_reads"]:
    original = raw(old["commit"], old["path"])
    integrated = raw(A, old["path"])
    oldid = identity(old["commit"], old["path"], original)
    currentid = identity(A, old["path"], integrated)
    u06_reuse.append({"old_ledger_identity": old, "old_observed": oldid, "final_observed": currentid,
                      "old_declared_identity_matched": same(old, oldid), "full_bytes_equal": original == integrated,
                      "mode_blob_bytes_sha256_equal": same(oldid, currentid),
                      "same_final_U06_target_path": old["path"] in u06_batch["actual_target_paths"],
                      "declared_original_semantic_use": old.get("semantic_use"),
                      "purpose_qualification": "Same exact document is still a final R8-U06 actual target; whether the root's earlier personal reading serves the final cumulative purpose remains the root's explicit judgment, not this helper's credit."})
check("old U06 root twelve-file identities are unchanged final U06 actual targets",
      len(u06_reuse) == 12 and {x["final_observed"]["path"] for x in u06_reuse} == set(u06_batch["actual_target_paths"])
      and all(x["old_declared_identity_matched"] and x["full_bytes_equal"] and x["mode_blob_bytes_sha256_equal"] for x in u06_reuse),
      {"old_ledger": identity(A, u06_ledger_path, u06_ledger_raw), "same_byte_documents": len(u06_reuse),
       "declared_purpose_labels": sorted({x["declared_original_semantic_use"] for x in u06_reuse})},
      "Prior root reading remains attributed to that root. This helper transfers no FULL, model/tier or semantic vote; same-purpose reuse is expressly root-owned.")

scope_rows = git("diff", "--name-status", B).decode().splitlines()
scope_paths = [p for row in scope_rows for p in row.split("\t")[1:]]
check("current tracked review differences remain within the new final-ultra r1 output directory",
      all(path.startswith(ALLOWED) for path in scope_paths), {"name_status": scope_rows},
      "The review has not edited old U06, source candidate, formal or registration files.")
main = git("ls-remote", "origin", "refs/heads/main").decode().strip()
check("remote main still matches the frozen historical main",
      main == m["historical_main_commit"] + "\trefs/heads/main", {"remote_main": main},
      "This is a present-time ref observation, not an authorization to merge or a reconstruction of all past operations.")
end_head = git("rev-parse", "HEAD").decode().strip()
end_branch = git("branch", "--show-current").decode().strip()
check("HEAD and branch unchanged during verification", head == end_head and branch == end_branch,
      {"start_head": head, "end_head": end_head, "start_branch": branch, "end_branch": end_branch},
      "No checkout, ref mutation, commit, push or force operation was performed by this script.")

result = {"schema": "r8-final-independent-mechanical-identity-scope/v1", "started_utc": started, "finished_utc": utc(),
          "input_binding": B, "artifact_snapshot": A, "fixed_delivery": BASE, "observed_head": head, "observed_branch": branch,
          "all_mechanical_assertions_pass": all(x["condition_matched"] for x in checks), "checks": checks,
          "payload_1008": payload, "post_snapshot_records": post_snapshot, "fixed_commit_object_bytes": object_checks,
          "nine_batch_links": batch_links, "nine_batch_source_groups": groups, "candidate_formal_mirrors_38": mirrors,
          "tagging_175_and_review_75_plus111": tagging_rows, "old_U06_root_twelve_identity_reuse": u06_reuse,
          "commands": commands, "command_count": len(commands), "command_exit_counts": dict(Counter(str(x["exit_code"]) for x in commands)),
          "earlier_object_availability_evidence": {"path": str(availability_path.relative_to(REPO)), "bytes": len(availability_raw), "sha256": sha(availability_raw)},
          "preexecution_failure_and_repair": json.loads((HERE / "final-mechanical-preexecution-failure.json").read_text()),
          "navigation_inventory": {"path": str((HERE / "final-navigation-inventory.json").relative_to(REPO)),
                                   "bytes": (HERE / "final-navigation-inventory.json").stat().st_size,
                                   "sha256": sha((HERE / "final-navigation-inventory.json").read_bytes())},
          "script_identity": {"path": str(Path(__file__).relative_to(REPO)), "bytes": Path(__file__).stat().st_size, "sha256": sha(Path(__file__).read_bytes())},
          "qualification": "All PASS labels are mechanical assertions only. No semantic/source FULL/configuration/independent-vote/whole-round acceptance or owner ACCEPTED/CLOSED is granted.",
          "business_execution": "NOT_EXECUTED", "semantic_verdict": "NOT_ISSUED", "FULL_read_credit": "NONE"}
output = HERE / "final-mechanical.json"
if output.exists():
    number = 1
    while (HERE / ("final-mechanical-attempt-" + str(number) + ".json")).exists():
        number += 1
    output.rename(HERE / ("final-mechanical-attempt-" + str(number) + ".json"))
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"output": str(output.relative_to(REPO)), "bytes": output.stat().st_size, "sha256": sha(output.read_bytes()),
                  "checks": len(checks), "all_mechanical_assertions_pass": result["all_mechanical_assertions_pass"],
                  "commands": len(commands), "exit_counts": result["command_exit_counts"],
                  "failed_assertions": [x["name"] for x in checks if not x["condition_matched"]]}, ensure_ascii=False))
if not result["all_mechanical_assertions_pass"]:
    raise SystemExit(1)
