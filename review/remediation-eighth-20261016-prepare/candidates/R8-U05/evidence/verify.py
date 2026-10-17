"""R8-U05 document/identity checks only. Never execute reference code or vectors."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[5]
BASE = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
REFERENCE = Path("/workspace/pokemon-essentials")
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
REPORT = ROOT / "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e"
BATCH = ROOT / "review/remediation-eighth-20261016-prepare/candidates/R8-U05"
EVIDENCE = BATCH / "evidence"


def git(*args, repo=ROOT):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def identity(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()}


def check_identity(entry, repo, commit, path):
    data = git("show", f"{commit}:{path}", repo=repo)
    actual = identity(data)
    mode = git("ls-tree", commit, "--", path, repo=repo).decode().split()[0]
    assert mode == entry["mode"], path
    assert all(actual[key] == entry[key] for key in ["bytes", "sha256", "blob"]), path
    return {"original_identity": entry, "verified_commit": commit,
            "verified_path": path, "actual": actual, "mode": mode,
            "credit": "TOOL_VALIDATION_IDENTITY_ONLY"}


readset = json.loads((REPORT / "handoff/batches/R8-U05/readset.json").read_text())
assignment = next(x for x in json.loads((REPORT / "handoff/batch-assignment.json").read_text())["batches"]
                  if x["id"] == "R8-U05")
assert git("rev-parse", "HEAD").decode().strip() != ""
assert git("merge-base", BASE, "HEAD").decode().strip() == BASE
assert git("branch", "--show-current").decode().strip() == "revision/r8-u05-20261017"
assert git("rev-parse", "HEAD", repo=REFERENCE).decode().strip() == R
assert git("rev-parse", "HEAD^{tree}", repo=REFERENCE).decode().strip() == readset["R"]["tree"]
assert not git("status", "--porcelain", "--untracked-files=no", repo=REFERENCE)

inherited = []
for group in ["source_spec_files", "mandatory_root_input", "additional_mandatory_companions"]:
    for entry in readset["inherited_contents"][group]:
        inherited.append({"group": group, **check_identity(entry, entry.get("repo", ROOT),
                                                         entry["commit"], entry["path"])})
payloads = json.loads((REPORT / "handoff/payload-manifest.json").read_text())["payloads"]
handoff = [check_identity(x, ROOT, BASE, x["path"]) for x in payloads]
assert len(handoff) == 45
assert len(inherited) == 80

changes = {
    "deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md": (
        "正常文本数据下步骤概率与累加器均为整数，故加数是非负整数而非小数",
        "文本输入的步骤概率与累加器均为整数，整数商向下取整；基础步骤概率与当前累加器均非负时，加数为非负整数；接受的负概率前缀沿同一算法处理，累加器及整数商可为负，不钳零"),
    "deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md": (
        "野生等级低于队首（可战）成员等级则拒绝并清累积——遭遇规格主规格，本文件不重算",
        "比较成员按配置选择：默认首非蛋成员（含濒死），替代配置为首位可战成员；野生等级低于该成员等级则拒绝并清累积——见普通遭遇规格 WP36 §4.3，本文件不重算"),
}
manifest = []
for path, (old, new) in changes.items():
    original = git("show", f"{BASE}:{path}")
    assert (ROOT / path).read_bytes() == original
    assert git("show", f"{readset['B8']['commit']}:{path}") == original
    candidate = BATCH / "mirror" / path
    data = candidate.read_bytes()
    assert original.count(old.encode()) == 1
    assert data == original.replace(old.encode(), new.encode())
    assert len(data.splitlines()) == len(original.splitlines())
    assert data.endswith(b"\n")
    assert "GR8-" not in data.decode()
    manifest.append({"candidate_path": str(candidate.relative_to(ROOT)), "formal_target": path,
                     "base": {"commit": BASE, **identity(original)},
                     "candidate": {"mode": "100644", **identity(data)},
                     "changed_line": data[:data.index(new.encode())].count(b"\n") + 1,
                     "preservation": "EXACT_SINGLE_REPLACEMENT_ALL_OTHER_BYTES_IDENTICAL"})
assert sorted(assignment["candidate_write_set"]) == sorted(x["candidate_path"] for x in manifest)
assert sorted(str(x.relative_to(ROOT)) for x in (BATCH / "mirror").rglob("*") if x.is_file()) == sorted(assignment["candidate_write_set"])

changed = set(git("diff", "--name-only", BASE).decode().splitlines())
changed.update(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
allowed = str(BATCH.relative_to(ROOT)) + "/"
assert all(path.startswith(allowed) for path in changed), sorted(changed)
assert git("rev-parse", f"{BASE}:deliverables/final-specification-set") == git("rev-parse", "HEAD:deliverables/final-specification-set")
subprocess.run(["git", "-C", str(ROOT), "diff", "--check", BASE], check=True)

utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
out = {"schema": "r8-u05-author-static-document-validation/v1", "utc": utc,
       "base": BASE, "reference": R, "result": "AUTHOR_DOCUMENT_CHECKS_COMPLETED",
       "checks": {"inherited_exact_identities": len(inherited), "handoff_payloads": len(handoff),
                  "candidate_files": len(manifest), "single_replacement_each": True,
                  "unaffected_bytes_preserved": True, "formal_targets_unchanged": True,
                  "reference_clean_fixed": True, "scope_allowlist": True, "diff_check": True},
       "execution": {"classification": "TOOL_VALIDATION", "business_vectors": "NOT_EXECUTED",
                     "Ruby_game_host_execution": 0, "independent_review": "PENDING",
                     "actual_integrated_PASS": "PENDING", "ACCEPTED": "PENDING", "CLOSED": "PENDING"}}
(EVIDENCE / "validation.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
(EVIDENCE / "input-identity-verification.json").write_text(json.dumps(
    {"schema": "r8-u05-identity-only-inventory/v1", "utc": utc,
     "semantic_read_credit": "NONE_FROM_HASH_OR_PARSE", "inherited": inherited, "handoff": handoff},
    ensure_ascii=False, indent=2) + "\n")
(EVIDENCE / "candidate-manifest.json").write_text(json.dumps(
    {"schema": "r8-u05-candidate-manifest/v1", "utc": utc, "base": BASE,
     "branch": "revision/r8-u05-20261017", "files": manifest,
     "self_binding": "Enclosing commit supplied by actual git commit and remote readback; no future SHA."},
    ensure_ascii=False, indent=2) + "\n")
print(json.dumps(out, ensure_ascii=False, indent=2))
