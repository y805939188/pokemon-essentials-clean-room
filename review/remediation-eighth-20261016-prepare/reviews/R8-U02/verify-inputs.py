"""Read-only input/scope verification; never executes the reference implementation."""
import datetime
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[4]
OUT = pathlib.Path(__file__).resolve().parent
RR = "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e"
CANDIDATE = "8b69bca8bf9141276425a963f350b19048bb2b51"
BASE = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
B8 = "fd1df570cad987dc3852a3b958f03916e317f7fe"
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
TARGET = "deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md"
MIRROR = "review/remediation-eighth-20261016-prepare/candidates/R8-U02/mirror/" + TARGET
EVENTS = []


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def git(repo, *args):
    start = now()
    p = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
    # Identity operations only: persist output hashes rather than duplicate source text.
    EVENTS.append({"argv": ["git", "-C", str(repo), *args], "start_utc": start,
                   "end_utc": now(), "exit": p.returncode,
                   "stdout_bytes": len(p.stdout), "stdout_sha256": hashlib.sha256(p.stdout).hexdigest(),
                   "stderr": p.stderr.decode(errors="replace")})
    if p.returncode:
        raise RuntimeError(p.stderr.decode(errors="replace"))
    return p.stdout


def identity(repo, commit, path):
    data = git(repo, "show", f"{commit}:{path}")
    entry = git(repo, "ls-tree", commit, "--", path).decode().strip().split()
    return {"repo": str(repo), "commit": commit, "path": path, "mode": entry[0],
            "blob": entry[2], "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


start = now()
readset = json.loads((ROOT / RR / "handoff/batches/R8-U02/readset.json").read_text())
inherited = readset["inherited_contents"]
descriptors = (inherited["source_spec_files"] + inherited["mandatory_root_input"] +
               inherited["additional_mandatory_companions"] +
               [readset["inherited_complete_readset"], readset["delta_complete_readset"]])
checks = []
seen = {}
for d in descriptors:
    current = d.get("current_recovered_at", d)
    repo = pathlib.Path(current.get("repo", str(ROOT)))
    key = (str(repo), current["commit"], current["path"])
    if key not in seen:
        actual = identity(repo, current["commit"], current["path"])
        ok = all(actual[k] == current[k] for k in ["mode", "blob", "bytes", "sha256"])
        seen[key] = {"actual": actual, "identity_pass": ok}
    checks.append({"original_provenance": d, "verified_current_payload": seen[key]})

original = git(ROOT, "show", f"{BASE}:{TARGET}")
candidate = git(ROOT, "show", f"{CANDIDATE}:{MIRROR}")
old = '有变化才整体重写并提示「Changes made to file X」。'.encode()
new = '有变化才整体重写。'.encode()
assert original.count(old) == 1
literal_pass = original.replace(old, new) == candidate
formal_trees = {c: git(ROOT, "rev-parse", f"{c}:deliverables/final-specification-set").decode().strip()
                for c in [B8, BASE, CANDIDATE]}
scope_paths = git(ROOT, "diff", "--name-status", BASE, CANDIDATE).decode().splitlines()
protected_changes = git(ROOT, "diff", "--name-only", BASE, CANDIDATE, "--",
                        "deliverables", "specs", "planning", "audit", "AGENTS.md").decode().splitlines()
source_status = git("/workspace/pokemon-essentials", "status", "--porcelain").decode()
source_head = git("/workspace/pokemon-essentials", "rev-parse", "HEAD").decode().strip()
fixed = [identity(ROOT, CANDIDATE, MIRROR), identity(ROOT, BASE, TARGET)]
for path in ["AGENTS.md", f"{RR}/handoff/batches/R8-U02/reviewer-prompt.md",
             f"{RR}/handoff/batches/R8-U02/prompt.md", f"{RR}/handoff/batches/R8-U02/readset.json",
             f"{RR}/handoff/contracts.zh.json", f"{RR}/handoff/batch-assignment.json",
             f"{RR}/handoff/cloud-eighth-update-handoff-manifest.json",
             f"{RR}/handoff/accepted-facts-and-mandatory-companions.json",
             f"{RR}/handoff/history-qualifications.json", f"{RR}/handoff/policy-and-preservation.json",
             "review/remediation-eighth-20261016-prepare/candidates/R8-U02/change-record.json",
             "review/remediation-eighth-20261016-prepare/coordination/first-two-candidate-checks.json"]:
    fixed.append(identity(ROOT, CANDIDATE, path))

summary = {"qualification": "TOOL_VALIDATION_ONLY_NOT_REFERENCE_EXECUTION",
           "start_utc": start, "end_utc": now(), "candidate": CANDIDATE, "baseline": BASE,
           "B8": B8, "reference": R, "candidate_tree": git(ROOT, "rev-parse", f"{CANDIDATE}^{{tree}}").decode().strip(),
           "readset_descriptor_count": len(checks), "unique_verified_payloads": len(seen),
           "readset_identities_pass": all(x["identity_pass"] for x in seen.values()),
           "exact_single_literal_replacement_pass": literal_pass,
           "candidate_bytes": len(candidate), "base_bytes": len(original),
           "formal_trees": formal_trees, "formal_trees_equal": len(set(formal_trees.values())) == 1,
           "baseline_to_candidate_changes": scope_paths, "protected_changes": protected_changes,
           "reference_head_pass": source_head == R, "reference_worktree_clean": not source_status,
           "semantic_full_read_credit_from_this_script": False,
           "Ruby_game_native_execution": "NOT_EXECUTED"}
write("input-manifest.json", fixed)
write("readset-identity-checks.json", checks)
write("verification.json", summary)
with (OUT / "commands.jsonl").open("a") as f:
    f.write("\n".join(json.dumps(e, ensure_ascii=False) for e in EVENTS) + "\n")
print(json.dumps(summary, ensure_ascii=False, indent=2))
assert summary["readset_identities_pass"] and literal_pass and summary["formal_trees_equal"]
assert not protected_changes and summary["reference_head_pass"] and summary["reference_worktree_clean"]
