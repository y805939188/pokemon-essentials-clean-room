import collections
import datetime
import difflib
import hashlib
import json
import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
repo = pathlib.Path.cwd()
publication = "e93d0e56750a6a16cc50cc68b2c97f11ea255153"
semantic = "54af598ca85211641348e6057ed0c348044787fe"
main = "8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
prepare = "469a268b92daed7b4d28d7fd0da75520cbb7228f"
reference = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
prefix = "review/remediation-sixth-20261014-prepare/"

def git(*args):
    return subprocess.check_output(["git", *args], cwd=repo)

def identity(commit, path):
    b = git("show", commit + ":" + path)
    mode, kind, blob_path = git("ls-tree", commit, path).decode().strip().split(" ", 2)
    blob = blob_path.split("\t", 1)[0]
    computed = hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()
    assert blob == computed
    return {"commit": commit, "path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest(),
            "git_blob": blob, "mode": mode, "type": kind, "lines": len(b.splitlines())}, b

started = datetime.datetime.now(datetime.timezone.utc).isoformat()
contract_id, contract_bytes = identity(prepare, prefix + "contracts/R6-U11.json")
contract = json.loads(contract_bytes)
prompt_id, prompt = identity(prepare, prefix + "prompts/R6-U11-R.md")
assert prompt_id["bytes"] == 214824
assert prompt_id["sha256"] == "bfc9b60c7b006e1fdd2205b55d0cb21198aa4366e0aa4c4c5eecc82aa111e030"
assert prompt_id["git_blob"] == "cd1d62ebaec092af61a76918a4abe6c6d41e1e9d"
embedded = prompt.split("## 本批确定合同".encode())[1].split(b"```json\n")[1].split(b"```")[0]
assert embedded == contract_bytes
assert git("rev-parse", publication + "^{tree}").decode().strip() == "930b677271ddfb2f8833a0deac79d87b6d01c157"
assert git("diff", semantic, publication, "--", prefix + "candidates/R6-U11/mirror/") == b""
assert git("diff", main, publication, "--", "deliverables/final-specification-set/") == b""
files = []
total_old_catalog_table_lines = 0
for path in contract["candidate_formal_paths"]:
    old_id, old = identity(main, path)
    new_id, new = identity(publication, prefix + "candidates/R6-U11/mirror/" + path)
    assert new == git("show", semantic + ":" + new_id["path"])
    old_lines, new_lines = old.decode().splitlines(), new.decode().splitlines()
    opcodes = [dict(zip(["kind", "old_start0", "old_end0", "new_start0", "new_end0"], op))
               for op in difflib.SequenceMatcher(a=old_lines, b=new_lines, autojunk=False).get_opcodes() if op[0] != "equal"]
    catalog = "/test-catalog/" in path
    old_rows = [line for line in old_lines if line.startswith("|")]
    missing = list((collections.Counter(old_rows) - collections.Counter(new_lines)).elements())
    if catalog:
        assert not missing
        total_old_catalog_table_lines += len(old_rows)
    files.append({"formal": old_id, "candidate": new_id, "changed_spans": opcodes,
                  "old_table_line_count": len(old_rows), "catalog_old_rows_preserved": not missing if catalog else None,
                  "body_table_replacements": missing if not catalog else []})
assert total_old_catalog_table_lines == 931
ref_ids = [identity(reference, path)[0] for path in contract["read_only_reference_paths"]]
changed = git("diff", "--name-only", prepare, publication).decode().splitlines()
assert len(changed) == 25
assert all(path.startswith(prefix + "candidates/R6-U11/") for path in changed)
payloads = [identity(publication, p)[0] for p in changed]
result = {"schema": "r6-u11-independent-fixed-validation.v1", "started_utc": started,
          "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "cwd": str(repo), "argv": ["python", str(root.relative_to(repo) / "validate_fixed.py")],
          "evidence_level": "TOOL_VALIDATION", "semantic_PASS_from_hash_or_rows": False,
          "frozen_publication": publication, "publication_tree": "930b677271ddfb2f8833a0deac79d87b6d01c157",
          "semantic_candidate": semantic, "semantic_tree": git("rev-parse", semantic + "^{tree}").decode().strip(),
          "candidate_directory_tree": git("rev-parse", publication + ":" + prefix + "candidates/R6-U11").decode().strip(),
          "mirror_directory_tree": git("rev-parse", publication + ":" + prefix + "candidates/R6-U11/mirror").decode().strip(),
          "prompt": prompt_id, "contract": contract_id, "embedded_contract_byte_equal": True,
          "formal_unchanged_at_publication": True, "core_publication_mirrors_byte_equal": True,
          "old_catalog_table_lines_preserved": 931, "table_line_count_includes_headers_and_separators": True,
          "old_catalog_rows_are_not_931_executed_business_vectors": True,
          "files": files, "fixed_reference": ref_ids, "candidate_payload_count": 25,
          "candidate_payloads": payloads, "undeclared_candidate_changes": []}
(root / "fixed-validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"status": "PASS_TOOL_VALIDATION_ONLY", "candidate_payloads": 25, "catalog_old_table_lines": 931,
                  "formal_files_unchanged": True, "mirror_same_core_publication": True}, ensure_ascii=False))
