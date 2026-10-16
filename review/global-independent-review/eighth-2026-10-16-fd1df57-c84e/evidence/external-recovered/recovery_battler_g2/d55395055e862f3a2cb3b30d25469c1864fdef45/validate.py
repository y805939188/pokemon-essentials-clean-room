"""Mechanical checks only; never executes Ruby, restored scripts or vectors."""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / ".git").exists())
PREFIX = HERE.relative_to(REPO).as_posix() + "/"
ROOT = HERE.parent.parent
BASE = "02c8206651676effe40ff9a33dbb70998b79c1b1"
BRANCH = "codex/r8-recovery-battler-g2-20261016"
REFERENCE = Path("/workspace/pokemon-essentials")


def git(*args, repo=REPO):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def read_json(path):
    return json.loads(path.read_text())


def identity_check(item):
    repo = REFERENCE if item["repo"] == "R" else REPO
    data = git("show", item["commit"] + ":" + item["path"], repo=repo)
    entry = git("ls-tree", item["commit"], "--", item["path"], repo=repo)
    mode, kind, blob = entry.decode().split(None, 3)[:3]
    assert kind == "blob" and mode == item["mode"] and blob == item["blob"]
    assert len(data) == item["bytes"]
    assert hashlib.sha256(data).hexdigest() == item["sha256"]
    assert (repo / item["path"]).read_bytes() == data


review = read_json(HERE / "reception.json")
evidence = read_json(HERE / "evidence.json")
assert git("branch", "--show-current").decode().strip() == BRANCH
assert review["fixed_contract_commit"] == evidence["contract_commit"] == BASE
assert review["UPDATE_NOT_STARTED"] and evidence["UPDATE_NOT_STARTED"]
assert review["spawn_calls"] == review["new_votes"] == 0
assert review["counts"]["required_added"] == review["counts"]["optional_added"] == 0
assert review["parent_task_final"] == "OPEN_NOT_SIGNED"

inputs = {
    split: read_json(ROOT / "tasks/receive_external_com_battler/splits" / split / "readset.json")
    for split in ["P03", "P04", "P05", "P06"]
}
forward = {x["id"]: x for x in review["forward"]}
reverse = {x["id"]: x for x in review["reverse"]}
assert len(forward) == len(review["forward"]) == 102
assert len(reverse) == len(review["reverse"]) == 63
children = []
for split, data in inputs.items():
    expected = {x["id"]: x for x in data["primary_compounds"]}
    actual = {k: x for k, x in forward.items() if x["split"] == split}
    assert set(expected) == set(actual)
    for ident, item in actual.items():
        source = expected[ident]
        assert item["source"] == source["source"] and item["unit"] == source["unit"]
        assert item["children"] == [{"id": c["id"], "assertion": c["assertion"]} for c in source["children"]]
        assert item["necessary_consumer_ids"] == source["necessary_consumers"]
        assert item["comparison"].strip() and item["execution"] == "NOT_EXECUTED"
        children.extend(c["id"] for c in item["children"])
    assert {k for k, x in reverse.items() if x["split"] == split} == set(data["assigned_reverse_child_ids"])
    groups = {g["id"]: g for g in data["complete_required_formal_group_objects"]}
    for ident in data["assigned_reverse_child_ids"]:
        item = reverse[ident]
        group = groups[ident.rsplit(".", 1)[0]]
        original = next(x for x in group["subassertions"] if x["id"] == ident)
        assert item["assertion"] == original["assertion"]
        assert item["foreign_facet"] == original.get("foreign_facet")
        assert item["formal"] == group["formal"] and item["comparison"].strip()
        assert not item["full_foreign_domain_accepted"]
assert len(children) == len(set(children)) == 245
assert set(children) == {c for d in inputs.values() for c in d["primary_child_ids"]}
assert sum(x["foreign_facet"] is not None for x in reverse.values()) == 10

required_facts = {x["id"] for d in inputs.values() for x in d["full_required_consumer_fact_objects"]}
received_facts = {ident for r in evidence["consumer_receipts"] for ident in r["ids"]}
assert len(required_facts) == 19 and required_facts == received_facts
assert evidence["consumer_primary_denominator"] == 0
assert len(evidence["vectors"]) == 12
assert all(v["execution"] == "NOT_EXECUTED" and v["inputs"] and v["expected"] for v in evidence["vectors"])

identities = evidence["controls"] + evidence["foreign_packets"]
identities += [x["identity"] for x in evidence["primary_reads"] + evidence["formal_reads"] + evidence["bounded_additional_source_reads"]]
for identity in identities:
    identity_check(identity)
assert len(evidence["primary_reads"]) == 4
assert all(x["credit"] == "OWN_FULL_LITERAL_READ_THIS_RECOVERY" for x in evidence["primary_reads"])

target = inputs["P03"]["original_complete_readset"]
for item in target["files"]:
    data = git("show", target["target_commit"] + ":" + item["remote_path_at_target_commit"])
    cached = ROOT / "tasks/receive_external_com_battler/inputs/target-5cf9503a" / item["relative_to_target_task"]
    entry = git("ls-tree", target["target_commit"], "--", item["remote_path_at_target_commit"]).decode()
    mode, kind, blob = entry.split(None, 3)[:3]
    assert kind == "blob" and mode == item["mode"] and blob == item["git_blob"]
    assert data == cached.read_bytes() and len(data) == item["bytes"]
    assert hashlib.sha256(data).hexdigest() == item["sha256"]

assert not git("status", "--porcelain", repo=REFERENCE).strip()
assert git("rev-parse", "HEAD", repo=REFERENCE).decode().strip() == review["R"]
assert git("rev-parse", "HEAD:deliverables/final-specification-set") == git("rev-parse", review["B8"] + ":deliverables/final-specification-set")
changes = git("diff", "--name-only", BASE).decode().splitlines()
changes += git("ls-files", "--others", "--exclude-standard").decode().splitlines()
assert all(path.startswith(PREFIX) for path in changes), changes
print(json.dumps({"result": "PASS_MECHANICAL_ONLY", "primary_files": 4,
                  "compounds": 102, "forward_children": 245, "assigned_reverse": 63,
                  "foreign_facets_preserved": 10, "necessary_facts": 19,
                  "vectors_not_executed": 12, "identity_objects_checked": len(identities),
                  "exclusive_write_set": PREFIX, "UPDATE_NOT_STARTED": True}, ensure_ascii=False))
