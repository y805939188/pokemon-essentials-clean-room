"""Check candidate scope, immutable input identities and historical byte retention.

This is document/transport validation, not a reference or behavior test.
Run from the project checkout after the frozen U05 context has been restored.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

B = "e646432c644dec04d306842cc5a559a29c718fbc"
BRANCH = "codex/r7-u05-author-20261015-pilot1"
PREFIX = "candidates/R7-U05/"
WP = "deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md"
CAT = "deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md"
MARKER = "### R7-U05-PF："


def identity(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob_content_id": hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()}


def pointer(obj, value):
    for part in value.lstrip("/").split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    ap.add_argument("--context", type=Path, default=Path("/workspace/r7-context/R7-U05"))
    ap.add_argument("--plan", type=Path, default=Path("/workspace/r7-bootstrap/R7-U05/recovery/batches/R7-U05.json"))
    args = ap.parse_args()

    def git(*argv):
        return subprocess.check_output(["git", *argv], cwd=args.repo)

    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    check("unique_author_branch", git("branch", "--show-current").decode().strip() == BRANCH)
    subprocess.run(["git", "merge-base", "--is-ancestor", B, "HEAD"], cwd=args.repo, check=True)
    check("formal_tree_unchanged", git("rev-parse", B + ":deliverables/final-specification-set") ==
          git("rev-parse", "HEAD:deliverables/final-specification-set"))
    changed = set(git("diff", "--name-only", B).decode().splitlines())
    changed.update(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    check("all_changes_within_author_candidates", bool(changed) and all(p.startswith(PREFIX) for p in changed))

    old_wp = git("show", B + ":" + WP)
    new_wp = (args.repo / PREFIX / WP).read_bytes()
    old_lines, new_lines = old_wp.splitlines(keepends=True), new_wp.splitlines(keepends=True)
    check("only_wp34_line188_changed", len(old_lines) == len(new_lines) and
          [i for i, pair in enumerate(zip(old_lines, new_lines)) if pair[0] != pair[1]] == [187])
    check("unconditional_parent_nonwrite_removed", "两个槽位个体不被写入".encode() not in new_wp)
    old_cat = git("show", B + ":" + CAT)
    new_cat = (args.repo / PREFIX / CAT).read_bytes()
    start = new_cat.index(MARKER.encode())
    end = new_cat.index("## R4-IV：".encode(), start)
    check("catalog_original_bytes_entirely_preserved", new_cat[:start] + new_cat[end:] == old_cat)
    added = new_cat[start:end].decode()
    check("nine_distinct_parent_vectors", all(added.count(f"| R7-U05-PF{i:02} |") == 1 for i in range(1, 10)))
    check("vectors_remain_unexecuted", "DERIVED_VECTOR，NOT_EXECUTED" in added and "未执行" in added)

    plan = json.loads(args.plan.read_text())
    restored = []
    for row in plan["artifacts"] + plan["evidence"] + plan["fixed_read_inputs"]:
        actual = identity((args.context / row["local_path"]).read_bytes())
        check("restored:" + row["local_path"], all(actual[k] == row[k] for k in actual))
        restored.append({"local_path": row["local_path"], **actual})
    for row in plan["evidence"]:
        actual = identity((args.context / "transport" / row["transport_path"]).read_bytes())
        check("encoded:" + row["transport_path"], all(actual[k] == v for k, v in row["encoded_identity"].items()))

    raw_dir = args.context / "evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs"
    raws = {p.stem: p.read_bytes() for p in raw_dir.glob("*.raw")}
    documents = {key: json.loads(data) for key, data in raws.items()}
    contract = json.loads((args.context / "dispatch/delegation/contracts/R7-U05.json").read_text())
    verified_members = {}

    def visit(value):
        if isinstance(value, dict):
            sha = value.get("input_sha256")
            if sha in raws and "raw_member_byte_offsets" in value:
                lo, hi = value["raw_member_byte_offsets"]
                member = raws[sha][lo:hi]
                key = sha + "#" + value["json_pointer"]
                check("raw_member:" + key, len(member) == value["raw_member_bytes"] and
                      hashlib.sha256(member).hexdigest() == value["raw_member_sha256"])
                logical = pointer(documents[sha], value["json_pointer"])
                canonical = json.dumps(logical, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
                check("canonical_member:" + key, hashlib.sha256(canonical).hexdigest() == value["canonical_sha256"])
                verified_members[key] = {"raw_byte_offsets": [lo, hi], "raw_sha256": value["raw_member_sha256"],
                                         "canonical_sha256": value["canonical_sha256"]}
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(contract)
    manifest_path = args.repo / PREFIX / "evidence/author/artifact-manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        for row in manifest["files"]:
            actual = identity((args.repo / row["path"]).read_bytes())
            check("artifact:" + row["path"], actual == row["new_identity"])
        actual_paths = {str(p.relative_to(args.repo)) for p in (args.repo / PREFIX).rglob("*") if p.is_file()}
        check("manifest_complete_except_explicit_self", actual_paths ==
              {r["path"] for r in manifest["files"]} | {str(manifest_path.relative_to(args.repo))})

    print(json.dumps({"status": "AUTHOR_DOCUMENT_AND_IDENTITY_CHECKS_OK", "semantic_PASS": False,
                      "checks": checks, "restored_files": len(restored),
                      "restored_bytes": sum(r["bytes"] for r in restored), "raw_members": verified_members,
                      "mirror_identities": [{"path": PREFIX + p, "base_identity": identity(git("show", B + ":" + p)),
                                             "new_identity": identity((args.repo / PREFIX / p).read_bytes())} for p in (WP, CAT)],
                      "behavior_reference_host_Demo_save_execution": "NOT_EXECUTED",
                      "effective_model_configuration": "UNVERIFIED"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
