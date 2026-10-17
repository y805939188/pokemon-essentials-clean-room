"""Read-only, fixed-input checks for R8-U03. Never loads or executes Ruby."""
import collections
import datetime
import hashlib
import json
import pathlib
import re
import subprocess

REPO = pathlib.Path(__file__).resolve().parents[4]
SOURCE = REPO.parent / "pokemon-essentials"
CANDIDATE = "8b69bca8bf9141276425a963f350b19048bb2b51"
BASE = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
B8 = "fd1df570cad987dc3852a3b958f03916e317f7fe"
REFERENCE = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
ROOT = "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e"
BATCH = "review/remediation-eighth-20261016-prepare/candidates/R8-U03"
TARGET = "deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md"
MIRROR = BATCH + "/mirror/" + TARGET
CATALOG = "deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md"


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def read(repo, commit, path):
    return git(repo, "show", commit + ":" + path)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def identity(repo, commit, path):
    data = read(repo, commit, path)
    entry = git(repo, "ls-tree", commit, "--", path).decode().split()
    return {"repository": str(repo), "commit": commit, "path": path,
            "mode": entry[0], "blob": entry[2], "bytes": len(data), "sha256": sha(data)}


def parsed_records(path):
    data = read(SOURCE, REFERENCE, path).decode("utf-8-sig")
    records, section = {}, None
    for number, line in enumerate(data.splitlines(), 1):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("["):
            section = line[1:-1]
            assert section not in records, (path, section)
            records[section] = {"line": number, "fields": {}}
        else:
            key, value = (x.strip() for x in line.split("=", 1))
            assert section and key not in records[section]["fields"]
            records[section]["fields"][key] = tuple(int(x.strip()) for x in value.split(","))
    for record in records.values():
        fields = record.pop("fields")
        assert set(fields) == {"HoursPerStage", "DryingPerHour", "Yield"}
        assert len(fields["HoursPerStage"]) == len(fields["DryingPerHour"]) == 1
        assert len(fields["Yield"]) == 2
        record["tuple"] = fields["HoursPerStage"] + fields["DryingPerHour"] + fields["Yield"]
    return records


def main():
    result = {"schema": "r8-u03-independent-tool-validation/v1",
              "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "qualification": "TOOL_VALIDATION; static text/data checks and DERIVED_VECTOR arithmetic; no reference execution"}
    assert git(SOURCE, "rev-parse", "HEAD").decode().strip() == REFERENCE
    assert not git(SOURCE, "status", "--porcelain")
    assert git(REPO, "rev-parse", CANDIDATE + "^").decode().strip() == BASE
    result["fixed_inputs"] = {"candidate": CANDIDATE, "base": BASE, "B8": B8, "reference": REFERENCE,
                              "candidate_tree": git(REPO, "rev-parse", CANDIDATE + "^{tree}").decode().strip(),
                              "base_tree": git(REPO, "rev-parse", BASE + "^{tree}").decode().strip(),
                              "reference_tree": git(SOURCE, "rev-parse", REFERENCE + "^{tree}").decode().strip()}
    before, after = read(REPO, BASE, TARGET), read(REPO, CANDIDATE, MIRROR)
    old, new = "多数 `3/15/2,5`".encode(), "CHERI/CHESTO/PECHA/RAWST/ASPEAR `3/15/2,5`".encode()
    assert before.count(old) == 1 and after == before.replace(old, new, 1)
    assert b"\n" in after and before.count(b"\n") == after.count(b"\n")
    assert read(REPO, B8, TARGET) == before == read(REPO, CANDIDATE, TARGET)
    result["candidate_identities"] = [identity(REPO, CANDIDATE, p) for p in [MIRROR, BATCH + "/change-record.json"]]
    result["literal_edit"] = {"exactly_one_replacement": True, "changed_line": 45,
                              "all_other_bytes_identical": True, "base": identity(REPO, BASE, TARGET)}
    trees = {c: git(REPO, "rev-parse", c + ":deliverables/final-specification-set").decode().strip()
             for c in [B8, BASE, CANDIDATE]}
    assert len(set(trees.values())) == 1
    assert not git(REPO, "diff", "--name-only", BASE, CANDIDATE, "--", "deliverables", "specs", "planning", "audit", ROOT, "AGENTS.md")
    result["unchanged_formal_trees"] = trees
    result["candidate_commit_changed_paths"] = git(REPO, "diff", "--name-status", BASE, CANDIDATE).decode().splitlines()
    inventory = git(REPO, "ls-tree", "-r", "--name-only", CANDIDATE, "--", BATCH).decode().splitlines()
    assert sorted(inventory) == sorted([MIRROR, BATCH + "/change-record.json"])
    result["u03_complete_inventory"] = inventory
    readset = json.loads(read(REPO, CANDIDATE, ROOT + "/handoff/batches/R8-U03/readset.json"))
    result["required_readset_identities"] = []
    for item in readset["inherited_contents"]["source_spec_files"]:
        repo = SOURCE if item["repo"] == str(SOURCE) else REPO
        got = identity(repo, item["commit"], item["path"])
        for field in ["bytes", "sha256", "blob", "mode"]:
            assert got[field] == item[field], (item["path"], field)
        assert read(repo, item["commit"], item["path"]) == (repo / item["path"]).read_bytes()
        result["required_readset_identities"].append(got)
    reviewer = read(REPO, CANDIDATE, ROOT + "/handoff/batches/R8-U03/reviewer-prompt.md").decode()
    contracts = json.loads(read(REPO, CANDIDATE, ROOT + "/handoff/contracts.zh.json"))
    contract = next(x for x in contracts["records"] if x["id"] == "GR8-PBSW-001")
    assert json.dumps(contract, ensure_ascii=False, indent=2) in reviewer
    assignment = json.loads(read(REPO, CANDIDATE, ROOT + "/handoff/batch-assignment.json"))
    unit = next(x for x in assignment["batches"] if x["id"] == "R8-U03")
    assert json.dumps(unit, ensure_ascii=False, indent=2) in reviewer
    result["embedded_contract_and_assignment_exact"] = True
    paths = ["PBS/berry_plants.txt"] + [f"PBS/Gen {g} backup/berry_plants.txt" for g in [5, 6, 7, 8]]
    expected_ids = ["CHERIBERRY", "CHESTOBERRY", "PECHABERRY", "RAWSTBERRY", "ASPEARBERRY"]
    result["complete_explicit_record_counts"] = []
    for path in paths:
        records = parsed_records(path)
        matching = [name for name, record in records.items() if record["tuple"] == (3, 15, 2, 5)]
        assert matching == expected_ids and len(records) == (64 if "Gen 5" in path else 67)
        assert records["RAZZBERRY"]["tuple"] == (2, 35, 2, 10)
        result["complete_explicit_record_counts"].append({"identity": identity(SOURCE, REFERENCE, path),
            "denominator": len(records), "matching_count": len(matching),
            "matching_ids_and_source_lines": {name: records[name]["line"] for name in matching},
            "RAZZBERRY": records["RAZZBERRY"],
            "tuple_frequency": [{"tuple": list(k), "count": v} for k, v in collections.Counter(r["tuple"] for r in records.values()).items()]})
    catalog = read(REPO, CANDIDATE, CATALOG)
    assert catalog == read(REPO, BASE, CATALOG) == read(REPO, B8, CATALOG)
    ids = re.findall(r"^\| ((?:R5-)?BP\d+) \|", catalog.decode(), re.M)
    assert ids == [f"BP{i:02}" for i in range(1, 21)] + [f"R5-BP{i:02}" for i in range(1, 5)]
    result["preserved_test_ids"] = ids
    result["links_at_destination"] = []
    for link in re.findall(r"\]\(([^)]+)\)", after.decode()):
        destination = (REPO / TARGET).parent / link
        assert destination.is_file(), link
        result["links_at_destination"].append({"link": link, "resolved": str(destination.resolve())})
    result["derived_arithmetic"] = []
    for hours in [3, 6, 7, 8, 10]:
        # Independent arithmetic from the reviewed behavioral rule, not source translation.
        moisture = max(100 - 15 * hours, -5)
        penalty = max(hours - 7, 0)
        result["derived_arithmetic"].append({"hours": hours, "stage": 1 + hours // 3,
            "moisture": moisture, "penalty": penalty, "qualification": "DERIVED_VECTOR; NOT_REFERENCE_EXECUTED"})
    result["result"] = "PASS"
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
