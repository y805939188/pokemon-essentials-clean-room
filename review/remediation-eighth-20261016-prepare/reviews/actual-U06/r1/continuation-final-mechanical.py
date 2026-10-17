"""Final identity/scope recheck only. Writes one new adjacent JSON receipt.

No semantic verdict, FULL reading credit, configuration claim, Ruby execution,
source program execution, fetch, checkout, commit, push, or old evidence write.
The 0eee-owned task registry is intentionally compared as two historical states:
its existing 0eee->5ff change is not hidden by a claim of uniform identity.
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
PREFIX = "review/remediation-eighth-20261016-prepare/"
ALLOWED = str(HERE.relative_to(REPO)) + "/"
A = "0eee6d141f33758eda34bd8ebad94a3e2b617f5a"
B = "5ff355c53b73171a0277c95af97e1cbd40eb8b28"
L = "2e2d5e6ab3f531ee902f60574b22e20fb065e04b"
C = "16f986afc1c85e64131f1dc8c6f2477a79c04029"
V = "052236414f6cb350f1781efe98761f336bb43108"
F = "49a558f7d5498680ba88d532f3815e07d7844459"
FB = "56cc0f683249bd54658b94134d1a61be6e8748e0"
SIX = PREFIX + "integration/U01-U04-U05-U07-U08-U09/"
REGISTRY = PREFIX + "coordination/task-registry.json"
OUTPUT = HERE / "continuation-final-mechanical.json"
if OUTPUT.exists():
    raise RuntimeError("Refusing to overwrite the existing final mechanical receipt")
commands = []
checks = []
raw_cache = {}
identity_cache = {}
started = datetime.now(timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    begin = now()
    argv = ["git", *args]
    proc = subprocess.run(argv, cwd=REPO, capture_output=True, check=False)
    record = {"argv": argv, "cwd": str(REPO), "started_utc": begin,
              "finished_utc": now(), "exit_code": proc.returncode,
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
    key = (commit, path)
    if key not in raw_cache:
        raw_cache[key] = git("show", commit + ":" + path)
    return raw_cache[key]


def identity(commit, path):
    key = (commit, path)
    if key not in identity_cache:
        data = raw(commit, path)
        mode, kind, blob = git("ls-tree", commit, "--", path).decode().split("\t")[0].split()
        identity_cache[key] = {"commit": commit, "path": path, "mode": mode,
                               "kind": kind, "blob": blob, "bytes": len(data), "sha256": sha(data)}
    return identity_cache[key]


def working(path):
    absolute = REPO / path
    st = absolute.lstat()
    if stat.S_ISLNK(st.st_mode):
        data = os.readlink(absolute).encode()
        mode = "120000"
    else:
        data = absolute.read_bytes()
        mode = "100755" if st.st_mode & 0o111 else "100644"
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    return {"path": path, "mode": mode, "kind": "blob", "blob": blob,
            "bytes": len(data), "sha256": sha(data)}


def equal(left, right):
    return all(left[key] == right[key] for key in ["mode", "blob", "bytes", "sha256"])


def check(name, condition, evidence, boundary):
    checks.append({"name": name, "mechanical_status": "PASS" if condition else "FAIL",
                   "condition_matched": bool(condition), "evidence": evidence,
                   "semantic_boundary": boundary})


head = git("rev-parse", "HEAD").decode().strip()
branch = git("branch", "--show-current").decode().strip()
git("merge-base", "--is-ancestor", L, head)
check("review branch descends from fixed latest registration", True,
      {"head": head, "branch": branch, "ancestor": L, "ancestor_command_exit": 0},
      "Ancestry does not grant semantic acceptance or owner closure.")
object_format = git("rev-parse", "--show-object-format").decode().strip()
assert object_format == "sha1"
manifest_path = PREFIX + "integration/U06/actual-review-input.json"
manifest = json.loads(raw(B, manifest_path))
assert manifest["artifact_snapshot_commit"] == A
batch = manifest["batches"][0]
assert batch["candidate_commit"] == C and batch["candidate_review_source_commit"] == V
snapshots = [("actual", A), ("binding", B), ("latest_registration", L), ("current_head", head)]

payload = []
for expected in manifest["payload_identities"]:
    owner = identity(expected["commit"], expected["path"])
    versions = {label: identity(commit, expected["path"]) for label, commit in snapshots}
    versions["worktree"] = working(expected["path"])
    payload.append({"expected_declared_identity": expected, "declared_owner_observed": owner,
                    "declared_owner_identity_matched": equal(expected, owner), "versions": versions,
                    "equals_declared_owner": {label: equal(owner, observed) for label, observed in versions.items()},
                    "binding_latest_head_worktree_preserved": all(equal(versions["binding"], versions[label])
                                                                 for label in ["latest_registration", "current_head", "worktree"])})
check("79 payload identities match their actual declared owner commit",
      len(payload) == 79 and all(x["declared_owner_identity_matched"] for x in payload),
      {"count": len(payload), "owner_commit_counts": dict(Counter(x["expected_declared_identity"]["commit"] for x in payload))},
      "Original byte identity is not semantic reading or actual integration correctness.")
check("all 79 payload files preserve their binding bytes through latest HEAD and worktree",
      len(payload) == 79 and all(x["binding_latest_head_worktree_preserved"] for x in payload),
      {"count": len(payload), "binding": B, "latest_registration": L, "head": head},
      "The owner snapshot predates binding bookkeeping; uniform identity with 0eee is reported separately.")
cross_snapshot_changes = [x for x in payload if not all(x["equals_declared_owner"].values())]
check("the only already-existing owner-to-binding payload change is task-registry.json",
      len(cross_snapshot_changes) == 1 and cross_snapshot_changes[0]["expected_declared_identity"]["path"] == REGISTRY,
      {"uniform_79_identity_across_all_snapshots": False,
       "unchanged_from_owner_count": len(payload) - len(cross_snapshot_changes),
       "changed_paths": [x["expected_declared_identity"]["path"] for x in cross_snapshot_changes]},
      "This check identifies a historical file difference; it does not judge registry state semantics.")

targets = []
for expected in batch["actual_target_identities"]:
    path = expected["path"]
    versions = {label: identity(commit, path) for label, commit in snapshots}
    versions["candidate_source_mirror"] = identity(C, batch["candidate_mirror_prefix"] + path)
    versions["worktree"] = working(path)
    targets.append({"expected": expected, "observed": versions,
                    "all_mode_blob_bytes_sha256_equal": all(equal(expected, v) for v in versions.values())})
check("all 12 formal targets retain exact reviewed mirror identities at every snapshot and worktree",
      len(targets) == 12 and all(x["all_mode_blob_bytes_sha256_equal"] for x in targets),
      {"count": len(targets), "formal_bytes": sum(x["expected"]["bytes"] for x in targets)},
      "This is byte/mode/blob equivalence only; no interface, timing, state, scenario or semantic verdict.")

imports = []
records = json.loads(raw(A, PREFIX + "integration/U06/import-identities.json"))["records"]
for expected in records:
    versions = {"source": identity(expected["commit"], expected["path"])}
    versions.update({label: identity(commit, expected["path"]) for label, commit in snapshots})
    versions["worktree"] = working(expected["path"])
    imports.append({"type": expected["type"], "expected": expected, "observed": versions,
                    "all_mode_blob_bytes_sha256_equal": all(equal(expected, v) for v in versions.values())})
groups = Counter(x["type"] for x in imports)
check("all 27 candidate and 19 independent-review artifacts equal original source and all successor bytes",
      groups == {"AUTHOR_CANDIDATE": 27, "INDEPENDENT_CANDIDATE_REVIEW": 19}
      and all(x["all_mode_blob_bytes_sha256_equal"] for x in imports), dict(groups),
      "Original reviewers' qualifications/FULL/PASS remain historical and are not transferred to this mechanical helper.")

frozen = []
for label, origin, expected_count in [("six_freeze", F, 5), ("six_binding", FB, 7)]:
    rows = git("ls-tree", "-r", origin, "--", SIX).decode().splitlines()
    paths = [row.split("\t", 1)[1] for row in rows]
    assert len(paths) == expected_count
    for path in paths:
        expected = identity(origin, path)
        versions = {name: identity(commit, path) for name, commit in snapshots}
        versions["worktree"] = working(path)
        frozen.append({"group": label, "expected": expected, "observed": versions,
                       "all_mode_blob_bytes_sha256_equal": all(equal(expected, v) for v in versions.values())})
check("six-batch five freeze files and seven binding files remain unchanged",
      len(frozen) == 12 and all(x["all_mode_blob_bytes_sha256_equal"] for x in frozen),
      {"freeze_files": 5, "binding_files": 7, "overlap_not_additive_unique_coverage": True},
      "This preserves fixed evidence; it does not review or accept the other six batches.")

scope = {}
for label, args in [("committed_branch_diff", ["diff", "--name-status", L, head]),
                    ("tracked_combined_worktree_diff", ["diff", "--name-status", L]),
                    ("index_diff", ["diff", "--cached", "--name-status", L])]:
    text = git(*args).decode()
    rows = [line.split("\t") for line in text.splitlines()]
    paths = [path for row in rows for path in row[1:]]
    scope[label] = {"rows": rows, "all_paths_within_r1": all(path.startswith(ALLOWED) for path in paths)}
scope["untracked_paths"] = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
check("all tracked changes relative to 2e2d are confined to the authorized r1 directory",
      all(scope[x]["all_paths_within_r1"] for x in ["committed_branch_diff", "tracked_combined_worktree_diff", "index_diff"]),
      scope,
      "Scope containment proves no current branch delta to formal targets, coordination registry or unrelated files; it is not content acceptance.")
protected_diff = git("diff", "--name-status", L, "--", "deliverables/final-specification-set/", PREFIX + "coordination/").decode()
check("formal directory and coordination registry have no current tracked delta from 2e2d", not protected_diff,
      {"name_status": protected_diff}, "No semantic judgment of existing formal/registry content is made.")
remote_main = git("ls-remote", "origin", "refs/heads/main").decode().strip()
expected_main = manifest["B8"]
check("remote main still points to the fixed historical main commit",
      remote_main == expected_main + "\trefs/heads/main", {"remote_ref": remote_main, "expected": expected_main},
      "A present-time remote ref check does not reconstruct every historical ref operation.")
local_main_refs = git("for-each-ref", "--format=%(refname) %(objectname)", "refs/heads/main", "refs/remotes/origin/main").decode()

missing = object()


def json_changes(old, new, pointer=""):
    if isinstance(old, dict) and isinstance(new, dict):
        result = []
        for key in dict.fromkeys([*old, *new]):
            result.extend(json_changes(old.get(key, missing), new.get(key, missing),
                                       pointer + "/" + key.replace("~", "~0").replace("/", "~1")))
        return result
    if isinstance(old, list) and isinstance(new, list):
        result = []
        for index in range(max(len(old), len(new))):
            result.extend(json_changes(old[index] if index < len(old) else missing,
                                       new[index] if index < len(new) else missing, pointer + "/" + str(index)))
        return result
    if old is not missing and new is not missing and type(old) == type(new) and old == new:
        return []
    return [{"pointer": pointer, "old_exists": old is not missing, "old_value": None if old is missing else old,
             "new_exists": new is not missing, "new_value": None if new is missing else new}]


old_registry = json.loads(raw(A, REGISTRY))
new_registry = json.loads(raw(B, REGISTRY))
registry = {"path": REGISTRY, "name_status_0eee_to_5ff": git("diff", "--name-status", A, B, "--", REGISTRY).decode(),
            "owner_0eee": identity(A, REGISTRY), "binding_5ff": identity(B, REGISTRY),
            "latest_2e2d": identity(L, REGISTRY), "current_head": identity(head, REGISTRY), "worktree": working(REGISTRY),
            "all_exact_JSON_differences": json_changes(old_registry, new_registry),
            "qualification": "Exact historical registration difference only; no registry interpretation or semantic verdict."}
end_head = git("rev-parse", "HEAD").decode().strip()
end_branch = git("branch", "--show-current").decode().strip()
check("HEAD and branch remained unchanged during this mechanical run", head == end_head and branch == end_branch,
      {"start_head": head, "end_head": end_head, "start_branch": branch, "end_branch": end_branch},
      "This run performs no branch/ref mutations, commit or push.")

result = {"schema": "r8-u06-continuation-final-mechanical/v1", "started_utc": started, "finished_utc": now(),
          "scope": "Mechanical identity, preservation, ancestry and current diff scope only.",
          "all_mechanical_assertions_pass": all(x["condition_matched"] for x in checks),
          "semantic_verdict": "NOT_ISSUED", "FULL_read_credit": "NONE", "runtime_configuration": "NOT_ASSESSED",
          "business_Ruby_game_native_execution": "NOT_EXECUTED", "write_scope": ALLOWED,
          "bindings": {"actual": A, "input": B, "latest_registration": L, "candidate": C, "review": V,
                       "six_freeze": F, "six_binding": FB, "observed_head": head, "observed_branch": branch},
          "checks": checks, "payload_79": payload, "formal_targets_12": targets,
          "candidate27_review19": imports, "six_batch_frozen5_bound7": frozen,
          "existing_registry_successor_difference": registry, "local_main_ref_observation": local_main_refs,
          "commands": commands, "command_count": len(commands),
          "command_exit_counts": dict(Counter(str(x["exit_code"]) for x in commands)),
          "script_identity": {"path": str(Path(__file__).relative_to(REPO)), "bytes": Path(__file__).stat().st_size,
                              "sha256": sha(Path(__file__).read_bytes())},
          "unasserted_semantic_boundaries": ["No semantic review, FULL source/formal reading, reader configuration inheritance, actual PASS, ACCEPTED, CLOSED, other-batch or whole-round acceptance is granted.",
                                             "Uniform identity of all 79 paths across 0eee and 5ff is explicitly false: 78 match and the existing task registry successor differs. Binding/latest/current preservation is checked separately."]}
OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"output": str(OUTPUT.relative_to(REPO)), "bytes": OUTPUT.stat().st_size,
                  "sha256": sha(OUTPUT.read_bytes()), "checks": len(checks),
                  "all_mechanical_assertions_pass": result["all_mechanical_assertions_pass"],
                  "commands": len(commands), "exit_counts": result["command_exit_counts"],
                  "registry_difference_pointers": [x["pointer"] for x in registry["all_exact_JSON_differences"]]}, ensure_ascii=False))
if not result["all_mechanical_assertions_pass"]:
    raise SystemExit(1)
