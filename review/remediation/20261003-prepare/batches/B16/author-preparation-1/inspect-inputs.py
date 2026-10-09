"""New B16 Git/JSON/text bookkeeping; never execute reference or behavior vectors."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

BASE = "1d06c45cc0a744fca181ac80ee573cc9ebb9b862"
PACKAGE = "9ad5539f38544fef6037356018015fe418021514"
REFERENCE = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
PREFIX = "review/remediation/20261003-prepare/batches/B16/refreeze-after-B15-C-1/"
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]


def git(*args, reference=False):
    command = ["git"]
    if reference:
        command += ["--git-dir=/tmp/b16-reference.git"]
    return subprocess.check_output(command + list(args), cwd=ROOT)


def blob(commit, path, reference=False):
    return git("show", commit + ":" + path, reference=reference)


def package(name):
    return json.loads(blob(PACKAGE, PREFIX + name))


def identity(commit, path, reference=False):
    data = blob(commit, path, reference)
    return dict(commit=commit, path=path,
                git_blob=git("rev-parse", commit + ":" + path, reference=reference).decode().strip(),
                sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))


def resolve_pointer(document, pointer):
    for token in pointer.lstrip("/").split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        document = document[int(token)] if isinstance(document, list) else document[token]
    return document


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def verify_inputs():
    supplied = package("input-identities.json")
    controls = package("original-and-acceptance-controls.json")["controls"]
    caches = {}
    comparisons = []
    for c in controls:
        record = {"id": c["id"], "primary": c["primary"], "canonical_state": c["canonical_state"]}
        for field, binding in [("whole_original_object", "whole_original_object_binding"),
                               ("whole_approved_acceptance_object", "whole_approved_acceptance_binding")]:
            b = c[binding]
            key = (b["commit"], b["path"])
            if key not in caches:
                actual = identity(*key)
                assert all(actual[k] == b[k] for k in actual)
                caches[key] = json.loads(blob(*key))
            assert resolve_pointer(caches[key], b["pointer"]) == c[field]
            record[binding] = b
            record[field + "_exact_equal"] = True
        record["original_sha256_as_dispatched"] = c["whole_original_object_sha256"]
        record["acceptance_sha256_as_dispatched"] = c["whole_acceptance_object_sha256"]
        record["qualified_control_keys"] = list(c["complete_current_control_fields"])
        record["reading_note"] = "Whole qualified bindings retained; bounded analysis does not replace root/extensions/effective premises/minimum/recheck."
        comparisons.append(record)
    checked = []
    for item in supplied["planned_reads"]:
        b = item["input"]
        actual = identity(b["commit"], b["path"])
        assert all(actual[k] == b[k] for k in actual)
        checked.append({**item, "identity_match": True,
                        "identity_is_not_semantic_read_or_quality_pass": True})
    for b in supplied["formal_write_input_snapshots"]:
        actual = identity(b["commit"], b["path"])
        assert all(actual[k] == b[k] for k in actual)
    extra_checks = []
    for group in ["potential_original_sync_read_inputs", "current_management_inputs"]:
        for item in supplied[group]:
            b = item.get("input", item.get("frozen_input", item))
            actual = identity(b["commit"], b["path"])
            assert all(actual[k] == b[k] for k in actual)
            extra_checks.append({"group": group, **actual, "identity_match": True})
    assert git("rev-parse", BASE + "^{tree}").decode().strip() == "5c99f51ec4cc084bc1c2b081306f1b55370744df"
    assert git("rev-parse", PACKAGE + "^").decode().strip() == BASE
    assert git("rev-parse", REFERENCE + "^{tree}", reference=True).decode().strip() == "7589c800b61ba13a13040ed0d686979b80a84fd0"
    dump("input-verification.json", {
        "status": "AUTHOR_PREPARATION_IDENTITY_CHECK_ONLY", "formal_input": BASE,
        "formal_tree": "5c99f51ec4cc084bc1c2b081306f1b55370744df", "management_package": PACKAGE,
        "package_is_not_formal_input": True, "requested_configuration": package("preparation-dispatch.json")["requested_configuration"],
        "effective_configuration": "UNVERIFIED; no trusted backend echo; no metadata/quota probe or model substitution",
        "planned_reads": checked, "formal_snapshot_checks": supplied["formal_write_input_snapshots"],
        "formal_writes_allowed_now": [], "potential_original_sync_read_inputs": supplied["potential_original_sync_read_inputs"],
        "current_management_inputs": supplied["current_management_inputs"],
        "original_and_management_identity_checks": extra_checks,
        "package_file_identities": [identity(PACKAGE, PREFIX + name) for name in [
            "preparation-dispatch.md", "preparation-dispatch.json", "B16-downstream-contract.json",
            "input-identities.json", "original-and-acceptance-controls.json", "affected-interface-map.json", "source-limits.json"]],
        "controls": comparisons, "whole_control_equality_checks": 48,
        "reference": identity(REFERENCE, "Data/Scripts/016_UI/005_UI_Party.rb", True),
        "reference_tree": git("rev-parse", REFERENCE + "^{tree}", reference=True).decode().strip(),
        "source_cache": "/tmp/b16-reference.git; newly recovered immutable Git objects, no checkout or reference modification",
    })
    print("74 planned read identities, six formal snapshots, 48 whole-control equalities verified; semantic reading is separate.")


if __name__ == "__main__":
    action = sys.argv[1]
    if action == "verify":
        verify_inputs()
    elif action == "read":
        repository, path, ranges = sys.argv[2:5]
        is_reference = repository == "reference"
        commit = REFERENCE if is_reference else BASE
        lines = blob(commit, path, is_reference).decode().splitlines()
        print(json.dumps(identity(commit, path, is_reference), ensure_ascii=False))
        for span in ranges.split(";"):
            lo, hi = map(int, span.split("-"))
            for n in range(lo, min(hi, len(lines)) + 1):
                print(f"{n}: {lines[n - 1]}")
    else:
        raise SystemExit("verify or read <project|reference> <exact-path> <start-end;start-end>")
