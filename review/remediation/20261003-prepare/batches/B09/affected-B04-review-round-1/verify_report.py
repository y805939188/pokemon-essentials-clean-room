#!/usr/bin/env python3
"""Own report bookkeeping only: Git/text/hash/JSON; no source/vector execution."""

import argparse
import ast
import collections
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess


REPORT = Path(__file__).resolve().parent
DEFAULT_GIT_DIRECTORY = REPORT
CANDIDATE = "18873059e56314fcd48f6081d5a65a79301a52f6"
BASELINE = "407536adb682a04161d3e9c82f153a62b1becd97"
PAYLOAD = "ab81adc17a0ee50f21032c58036b7b56b28da51b"
CANDIDATE1 = "8ff72341b5b91736970b5bfa5dc1b88137e618a5"
REFERENCE = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
BRANCH = "remediation/20261003-prepare/review-B09-affected-B04-1"
DIRECTORY = "review/remediation/20261003-prepare/batches/B09/affected-B04-review-round-1"
MANIFEST = "report-file-manifest.json"
RESULTS = "report-validation-results.json"
EXCLUDED = {MANIFEST, RESULTS}


def git(*args, cwd=None):
    return subprocess.check_output(["git", *args], cwd=cwd or DEFAULT_GIT_DIRECTORY)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(name):
    return json.loads((REPORT / name).read_text(encoding="utf-8"))


def write(name, value):
    (REPORT / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def file_records():
    return [
        {"path": p.name, "bytes": len(p.read_bytes()), "sha256": sha(p.read_bytes())}
        for p in sorted(REPORT.iterdir()) if p.is_file() and p.name not in EXCLUDED
    ]


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--create-manifest", action="store_true")
parser.add_argument("--write-results", action="store_true")
args = parser.parse_args()
if args.create_manifest:
    write(MANIFEST, {
        "candidate": CANDIDATE,
        "report_directory": DIRECTORY,
        "algorithm": "SHA-256",
        "files": file_records(),
        "excluded": sorted(EXCLUDED),
        "excluded_binding": "Containing ordinary report commit Git tree; no hash self-reference.",
    })

checks = []


def check(ok, kind, label):
    checks.append({"kind": kind, "label": label, "passed": bool(ok)})


root = Path(git("rev-parse", "--show-toplevel").decode().strip())
DEFAULT_GIT_DIRECTORY = root
check(REPORT == root / DIRECTORY, "scope", "exact allowed report directory")
check(git("branch", "--show-current").decode().strip() == BRANCH, "scope", "isolated report branch")
check(git("remote", "get-url", "origin").decode().strip() ==
      "https://github.com/y805939188/pokemon-essentials-clean-room.git", "identity", "main origin")
check(not any(p.is_symlink() or p.is_dir() for p in REPORT.iterdir()), "scope", "report flat and no symlinks")
head = git("rev-parse", "HEAD").decode().strip()
parents = git("rev-list", "--parents", "-n", "1", "HEAD").decode().split()[1:]
check(head == CANDIDATE or parents == [CANDIDATE], "identity", "candidate HEAD or single report parent C")
if head != CANDIDATE:
    additions = [x.split("\t") for x in git("diff", "--name-status", "--no-renames", CANDIDATE, head).decode().splitlines()]
    check(bool(additions) and all(s == "A" and p.startswith(DIRECTORY + "/") for s, p in additions),
          "scope", "committed report contains only permitted additions")
status = [x.decode() for x in git("status", "--porcelain=v1", "-z", "--untracked-files=all").split(b"\0") if x]
check(all(x[3:].startswith(DIRECTORY + "/") and x[:2] in {"??", "A ", "AM", " M", "M "} for x in status),
      "scope", "all workspace changes confined to report")
for commit, tree in [
    (CANDIDATE, "bf79e3a86623e05d7f3d994194b67cc4e2dd4fea"),
    (BASELINE, "aeccdd10ac56344c3faf5b7c66300c8e5ab258d3"),
    (PAYLOAD, "b8c33f2aa972e8d43bcbe3bba7a47928f6afb028"),
]:
    check(git("cat-file", "-t", commit).strip() == b"commit" and
          git("rev-parse", commit + "^{tree}").decode().strip() == tree,
          "identity", "exact real commit/tree " + commit)
check(git("rev-list", "--parents", "-n", "1", CANDIDATE).decode().split() == [CANDIDATE, PAYLOAD],
      "identity", "C parent PAY")
check(git("rev-list", "--parents", "-n", "1", PAYLOAD).decode().split() == [PAYLOAD, CANDIDATE1],
      "identity", "PAY parent C1")

for p in sorted(REPORT.glob("*.json")):
    json.loads(p.read_text(encoding="utf-8"))
    check(True, "format", "JSON parses " + p.name)
for p in sorted(REPORT.glob("*.py")):
    ast.parse(p.read_text(encoding="utf-8"))
    check(True, "format", "own audit Python parses without execution " + p.name)
for p in sorted(REPORT.iterdir()):
    if p.suffix in {".md", ".json", ".py"}:
        text = p.read_text(encoding="utf-8")
        check(text.endswith("\n") and all(line == line.rstrip() for line in text.splitlines()),
              "format", "final newline/trailing whitespace " + p.name)
for link in re.findall(r"\]\(([^)]+)\)", (REPORT / "README.md").read_text(encoding="utf-8")):
    check((REPORT / link).is_file() or (link == RESULTS and args.write_results),
          "trace", "README target " + link)

manifest = load(MANIFEST)
check(manifest["candidate"] == CANDIDATE and manifest["files"] == file_records() and
      set(manifest["excluded"]) == EXCLUDED, "envelope", "complete report file hash manifest")
audit = load("identity-audit.json")
check(audit["checks"] == audit["passed"] == len(audit["results"]) == 945 and
      audit["failed"] == 0 and all(x["passed"] for x in audit["results"]),
      "audit", "945 independent identity/text assertions passed")
check(audit["candidate"] == CANDIDATE and audit["baseline"] == BASELINE and
      all(x["matched"] for x in audit["identity_bindings"]), "audit", "audit bindings/status")
first = load("first-judgment.json")
comparison = load("author-check-comparison.json")
check(sha((REPORT / "first-judgment.json").read_bytes()) == comparison["first_judgment_sha256"] and
      datetime.datetime.fromisoformat(first["at_utc"]) < datetime.datetime.fromisoformat(comparison["compared_at_utc"]),
      "provenance", "first judgment hash and time precede detailed author comparison")
check(first["identity_assertions"] == 821 and not first["author_success_summary_basis"] and
      first["verdict"] == "PASS_SCOPED" and not comparison["verdict_change"] and
      not comparison["author_verifier_executed"], "provenance", "first judgment/author comparison boundaries")
author_data = git("show", CANDIDATE + ":" + comparison["author_self_check_path"])
check(sha(author_data) == comparison["author_self_check_sha256"] and
      comparison["reported_count"] == comparison["reported_passed"] == 321,
      "provenance", "author self-check exact data identity and attributed count")

path_records = load("all87-path-identities.json")
statuses = [x.split("\t") for x in git("diff", "--name-status", "--no-renames", BASELINE, CANDIDATE).decode().splitlines()]
check([(x["status"], x["path"]) for x in path_records] == [tuple(x) for x in statuses] and
      collections.Counter(x[0] for x in statuses) == {"M": 14, "A": 73}, "scope", "all87 exact partition")
for record in path_records:
    for key in ["before", "after"]:
        v = record[key]
        if v is None:
            continue
        data = git("show", v["commit"] + ":" + v["path"])
        check(sha(data) == v["sha256"] and len(data) == v["bytes"] and
              git("rev-parse", v["commit"] + ":" + v["path"]).decode().strip() == v["git_blob"],
              "identity", "path " + key + " " + v["path"])
mods = [p for s, p in statuses if s == "M"]
diff_manifest = load("diff-manifest.json")
for entry in diff_manifest["complete_unfiltered_diffs"]:
    packed = (REPORT / entry["path"]).read_bytes()
    raw = gzip.decompress(packed)
    exact = git("diff", *diff_manifest["flags"], entry["before"], entry["after"])
    check(not entry["path_filter"] and sha(packed) == entry["compressed_sha256"] and
          len(packed) == entry["compressed_bytes"] and sha(raw) == entry["uncompressed_sha256"] and
          len(raw) == entry["uncompressed_bytes"] and raw == exact,
          "diff", "complete unfiltered diff " + entry["path"])
norm = diff_manifest["normative_diff"]
raw = (REPORT / norm["path"]).read_bytes()
check(len(mods) == norm["explicit_paths"] == 14 and sha(raw) == norm["sha256"] and
      len(raw) == norm["bytes"] and raw == git("diff", *diff_manifest["flags"], BASELINE, CANDIDATE, "--", *mods),
      "diff", "complete14 normative diff")
preserved = load("B04-preserved-current-identities.json")
check(len(preserved) == 13 and all(x["unchanged_baseline_to_candidate"] and
      x["baseline"]["sha256"] == x["candidate"]["sha256"] for x in preserved),
      "scope", "13 current B04 paths preserved")
for record in preserved:
    for key in ["historical", "baseline", "candidate"]:
        v = record[key]
        data = git("show", v["commit"] + ":" + v["path"])
        check(sha(data) == v["sha256"] and len(data) == v["bytes"],
              "identity", "B04 " + key + " " + v["path"])

reference = load("reference-identity.json")
ref_root = Path(reference["local_path"])
check(git("cat-file", "-t", REFERENCE, cwd=ref_root).strip() == b"commit" and
      git("rev-parse", "HEAD", cwd=ref_root).decode().strip() == REFERENCE and
      git("rev-parse", "HEAD^{tree}", cwd=ref_root).decode().strip() == reference["tree"] and
      not git("branch", "--show-current", cwd=ref_root).strip() and
      not git("status", "--porcelain=v1", "--untracked-files=all", cwd=ref_root).strip(),
      "reference", "real fixed detached clean reference still read-only")
read_ranges = collections.defaultdict(set)
for name, repository, commit, location in [
    ("source-reading-log.json", "reference", REFERENCE, ref_root),
    ("project-reading-log.json", "project", CANDIDATE, root),
]:
    log = load(name)
    local_ranges = collections.defaultdict(set)
    for event in log["events"]:
        data = git("show", commit + ":" + event["path"], cwd=location)
        lines = data.decode("utf-8").splitlines()
        check(event["commit"] == commit and event["sha256"] == sha(data) and
              event["bytes"] == len(data) and event["line_count"] == len(lines) and
              1 <= event["start"] <= event["end"] <= len(lines),
              "trace", "read log " + event["path"] + ":" + str(event["start"]))
        values = set(range(event["start"], event["end"] + 1))
        local_ranges[event["path"]].update(values)
        read_ranges[repository, event["path"]].update(values)
    actual = {"events": len(log["events"]), "files": len(local_ranges),
              "unique_numbered_lines": sum(len(x) for x in local_ranges.values())}
    check(actual == log["stats"], "trace", "unique counted own read ranges " + name)


def citation(v, label):
    repository = v["repository"]
    commit, location = (REFERENCE, ref_root) if repository == "reference" else (CANDIDATE, root)
    data = git("show", commit + ":" + v["path"], cwd=location)
    check(v["commit"] == commit and 1 <= v["start"] <= v["end"] <= len(data.decode("utf-8").splitlines()) and
          set(range(v["start"], v["end"] + 1)) <= read_ranges[repository, v["path"]],
          "trace", label + " " + v["path"] + ":" + str(v["start"]) + "-" + str(v["end"]))


cases = load("independent-static-designs.json")
check(cases["count"] == len(cases["cases"]) == 15 and
      cases["executed"] == cases["runtime_observations"] == cases["proven_Demo_chains"] == 0,
      "limits", "15 static groups all unexecuted")
for case in cases["cases"]:
    check(not case["executed"] and not case["runtime_observed"] and
          case["scope"] in {"B04_AFFECTED_INTERFACE_ONLY",
                            "B04_COMMON_PRESENTATION_INPUT_BOUNDARY; NOT_B05_ITEM_ACCEPTANCE"},
          "limits", "unexecuted " + case["id"])
    for evidence in case["evidence"]:
        citation(evidence, case["id"])
impact = load("scope-and-impact.json")
check(impact["complete_candidate_normative_paths"] == 14 and
      not impact["complete_B09_primary_review"] and not impact["whole_B04_replay"] and
      not impact["actual_integration_approval"], "scope", "bounded affected interface gate")
for entry in impact["additional_bounded_scope"]:
    for evidence in entry["evidence"]:
        citation(evidence, "additional bounded scope")
limits = load("model-and-limits.json")
check(limits["effective_configuration"] == "UNVERIFIED" and
      not limits["trusted_effective_model_reasoning_tier_echo"] and
      limits["children_spawned"] == 0 and not limits["quota_checks"], "limits", "configuration and no children")
for key in ["auth_config_quota_probes", "reference_program_execution", "game_execution",
            "compiler_execution", "converter_execution", "generator_execution", "deserializer_execution",
            "reference_behavior_simulator_execution", "author_or_historical_verifier_execution",
            "behavior_vectors_execution", "runtime_observations", "proven_Demo_chains"]:
    check(limits[key] == 0, "limits", key + " stays zero")
findings = load("findings.json")
check(findings["candidate"] == CANDIDATE and findings["verdict"] == "PASS_SCOPED" and
      not findings["new_blocking_findings"] and findings["new_defect_count"] == findings["new_root_count"] == 0,
      "verdict", "PASS_SCOPED no new blockers/roots")
handoff = load("handoff.json")
check(handoff["reviewed_candidate"] == CANDIDATE and handoff["report_parent_must_equal"] == CANDIDATE and
      handoff["report_branch"] == BRANCH and not handoff["actual_gate_satisfied"] and
      not handoff["integration_authorized"] and not handoff["canonical_closure_authorized"],
      "scope", "handoff exact candidate and retained actual/public gates")
retained = load("retained-obligations.json")
check(retained["canonical_OPEN"] == 229 and retained["canonical_CLOSED"] == 0 and
      not retained["global_gate_passed"] and retained["no_public_registry_write"] and
      retained["no_ID_integration_or_closure"] and retained["actual_required"],
      "scope", "canonical and other-owner gates retained")

result = {
    "at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "method": __doc__,
    "candidate": CANDIDATE,
    "baseline": BASELINE,
    "checked_head": head,
    "report_directory": DIRECTORY,
    "report_manifest_sha256": sha((REPORT / MANIFEST).read_bytes()),
    "checks": len(checks),
    "passed": sum(x["passed"] for x in checks),
    "failed": sum(not x["passed"] for x in checks),
    "results": checks,
    "behavior_execution": 0,
    "reference_execution": 0,
    "runtime_observations": 0,
    "proven_Demo_chains": 0,
}
if args.write_results:
    write(RESULTS, result)
print(json.dumps({k: result[k] for k in ["checks", "passed", "failed", "candidate", "checked_head"]}))
if result["failed"]:
    print(json.dumps([x for x in checks if not x["passed"]], ensure_ascii=False, indent=2))
    raise SystemExit(1)
