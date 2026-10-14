"""Finite document/identity checks. Does not execute reference behavior."""
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys

ROOT = Path.cwd()
PREP = ROOT / "review/remediation-sixth-20261014-prepare"
OWN = PREP / "candidates/R6-U12"
BASE = "469a268b92daed7b4d28d7fd0da75520cbb7228f"
MAIN = "8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
REF = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
start = datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(*args):
    return subprocess.check_output(["git", *args])

def identity(data):
    return {
        "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
        "git_blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
        "lines": len(data.splitlines()), "mode": "100644", "type": "blob"}

contract = json.loads((PREP / "contracts/R6-U12.json").read_text())
frozen = json.loads((PREP / "inputs/frozen-inputs.json").read_text())
prompt = git("show", BASE + ":review/remediation-sixth-20261014-prepare/prompts/R6-U12-A.md")
assert identity(prompt)["bytes"] == 177114
assert identity(prompt)["sha256"] == "7403f05c52dd05b082031e5afc43343d85477d30226ef4b8e4cee3b8cf2f7fea"
assert identity(prompt)["git_blob"] == "952837313e6f3a7bdad1417652f70ab76c9a281b"
assert (PREP / "contracts/R6-U12.json").read_bytes() in prompt
reads = [json.loads(x) for x in (OWN / "evidence/read-segments.jsonl").read_text().splitlines()]
inputs = []
for entry in reads:
    key = (entry["commit"], entry["path"])
    if key in [(e["commit"], e["path"]) for e in inputs]:
        continue
    data = git("show", key[0] + ":" + key[1])
    actual = identity(data)
    mode, object_type, blob = git("ls-tree", key[0], "--", key[1]).decode().split()[:3]
    assert object_type == "blob" and blob == actual["git_blob"]
    actual["mode"] = mode
    expected = next(e for e in frozen["source_materials" if key[0] == REF else "formal_materials"] if e["path"] == key[1])
    for field in ["bytes", "sha256", "git_blob", "mode"]:
        assert actual[field] == expected[field], (key, field)
    intervals = [e["range"] for e in reads if (e["commit"], e["path"]) == key]
    covered = {i for a, b in intervals for i in range(a, b + 1)}
    inputs.append(dict(actual, commit=key[0], path=key[1], ranges=intervals,
                       full_output_coverage=len(covered) == actual["lines"]))

manifest = []
changes = []
for path in contract["candidate_formal_paths"]:
    current = (OWN / "mirror" / path).read_bytes()
    baseline = git("show", MAIN + ":" + path)
    assert git("show", BASE + ":" + str((OWN / "mirror" / path).relative_to(ROOT))) == baseline
    a, b = baseline.decode().splitlines(), current.decode().splitlines()
    ops = difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes()
    ranges = [{"kind": k, "baseline_lines": [i + 1, j], "candidate_lines": [m + 1, n]}
              for k, i, j, m, n in ops if k != "equal"]
    assert ranges, path
    manifest.append({"formal_path": path, "candidate_path": str((OWN / "mirror" / path).relative_to(ROOT)),
                     "baseline": dict(identity(baseline), commit=MAIN), "candidate": identity(current)})
    changes.append({"path": path, "changes": ranges})

catalog = next(x["formal_path"] for x in manifest if "/test-catalog/" in x["formal_path"])
old = git("show", MAIN + ":" + catalog).decode().splitlines()
new = (OWN / "mirror" / catalog).read_text().splitlines()
preserved = [x for x in old if x.startswith("| ") and not x.startswith(("| C12 |", "| C36 |"))]
assert all(x in new for x in preserved)
vectors = [x for x in new if x.startswith("| R6-U12-")]
assert len(vectors) == 9
assert len({x.split("|")[1].strip() for x in vectors}) == 9
assert all(len(x.split("|")) == 5 for x in vectors)
assert all(git("show", MAIN + ":" + e["formal_path"]) == (ROOT / e["formal_path"]).read_bytes() for e in manifest)
changed_tracked = git("diff", "--name-only", BASE).decode().splitlines()
untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
allow = str(OWN.relative_to(ROOT)) + "/"
assert all(p.startswith(allow + "mirror/") or p.startswith(allow + "evidence/") for p in changed_tracked + untracked)
check = subprocess.run(["git", "diff", "--check"], capture_output=True, text=True)
assert check.returncode == 0, check.stderr

result = {"kind": "TOOL_VALIDATION", "argv": sys.argv, "cwd": str(ROOT),
          "start_utc": start, "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "runtime": platform.python_version(), "exit_code": 0, "stderr": "",
          "input_identities": inputs, "candidate_mirrors": manifest, "changed_ranges": changes,
          "catalog_preserved_rows": len(preserved), "new_derived_vectors": len(vectors),
          "checks": {"frozen_prompt_and_embedded_contract": "PASS", "input_identities": "PASS",
                     "baseline_is_frozen_main": "PASS", "catalog_other_rows_byte_preserved": "PASS",
                     "candidate_has_actual_edits": "PASS", "formal_worktree_unmodified": "PASS",
                     "allowlist": "PASS", "diff_check": "PASS"},
          "reference_behavior_executions": 0, "independent_model_executions": 0,
          "host_demo_executions": 0, "real_save_executions": 0,
          "scope": "Document identity, finite difference, coverage and retained-row checks only; author semantic findings are separate."}
(OWN / "evidence/tool-validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"checks": result["checks"], "preserved_rows": len(preserved), "vectors": len(vectors)}, ensure_ascii=False))
