#!/usr/bin/env python3
"""Mechanical navigation only. Read pinned blobs and the local derived inventory.

No fetch, Ruby, candidate scripts, semantic review, reading credit or acceptance.
The structure DAG preserves every JSON object key and array position, without scalar
values. --resolve PATH POINTER checks a real RFC6901 pointer against the pinned blob
or this derived inventory. Its plain JSON path automatically falls back to JSON.gz.
For JSONL, add --jsonl-line N (the physical one-based line number).
--compress writes deterministic gzip plus the byte/hash mapping. --remove-plain
additionally removes only the verified, untracked inventory created by this task.
"""

import argparse
import collections
import gzip
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[5]
OUT_REL = "review/remediation-eighth-20261016-prepare/reviews/final-ultra/r1/final-navigation-inventory.json"
COMPRESSION_REL = "review/remediation-eighth-20261016-prepare/reviews/final-ultra/r1/final-navigation-compression.json"
ORIGINAL_INVENTORY_BYTES = 13913036
ORIGINAL_INVENTORY_SHA256 = "3bb63a562494ac3bf8559b9eae3815b9bc8620bbaebb7bcf641b4795629679a9"
BINDING = "8ab43a609e60430492b219f0dce14ef4fdb8e47f"
ARTIFACT = "fd414a2c6ec0a0f746b48e0924e5692221ea5d5a"
MANIFEST = "review/remediation-eighth-20261016-prepare/final/independent-review-input.json"
PAYLOAD = "review/remediation-eighth-20261016-prepare/final/payload-identities.json"
HANDOFF = "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff"
FORMAL = "deliverables/final-specification-set/"
POINTER_CHECKS = 0


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def pinned(path, commit=ARTIFACT):
    return git("cat-file", "blob", f"{commit}:{path}")


def reject_duplicates(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON object key: {key!r}")
        out[key] = value
    return out


def parse(raw):
    return json.loads(raw.decode("utf-8-sig"), object_pairs_hook=reject_duplicates)


def inventory_path(path):
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = ROOT / candidate
    return candidate.resolve() in ((ROOT / OUT_REL).resolve(), (ROOT / (OUT_REL + ".gz")).resolve())


def load_inventory(path=OUT_REL):
    """Read the derived inventory; preserve its original JSON logical identity."""
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = ROOT / candidate
    if not inventory_path(candidate):
        raise ValueError("local inventory loader is restricted to this task's inventory")
    if not candidate.exists() and not str(candidate).endswith(".gz"):
        candidate = Path(str(candidate) + ".gz")
    raw = candidate.read_bytes()
    if str(candidate).endswith(".gz"):
        raw = gzip.decompress(raw)
    return raw, candidate.relative_to(ROOT).as_posix()


def compress_inventory(remove_plain=False):
    raw, _ = load_inventory()
    parse(raw)
    carrier = ROOT / (OUT_REL + ".gz")
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, compresslevel=9, mtime=0) as stream:
        stream.write(raw)
    compressed = buffer.getvalue()
    assert int.from_bytes(compressed[4:8], "little") == 0
    carrier.write_bytes(compressed)
    stored = carrier.read_bytes()
    restored = gzip.decompress(stored)
    assert restored == raw
    plain_sha = hashlib.sha256(raw).hexdigest()
    plain = ROOT / OUT_REL
    if remove_plain and plain.exists():
        assert plain.parent == Path(__file__).resolve().parent and not plain.is_symlink()
        assert len(raw) == ORIGINAL_INVENTORY_BYTES and plain_sha == ORIGINAL_INVENTORY_SHA256
        tracked = subprocess.run(["git", "ls-files", "--error-unmatch", "--", OUT_REL],
                                 cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if tracked.returncode == 0:
            raise ValueError("refusing to remove a tracked plain inventory")
        plain.unlink()
    test = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--resolve", OUT_REL, "/summary"],
                          cwd=ROOT, check=True, capture_output=True, text=True)
    test_result = parse(test.stdout.encode())
    expected_carrier = OUT_REL if plain.exists() else OUT_REL + ".gz"
    assert test_result["dereferenced"] and test_result["source_carrier"] == expected_carrier
    mapping = {
        "schema": "r8-final-navigation-lossless-gzip-v1",
        "purpose": "Mechanical derived-navigation carrier compression only; no reading or semantic credit.",
        "plain": {"path": OUT_REL, "bytes": len(raw), "sha256": plain_sha},
        "gzip": {"path": OUT_REL + ".gz", "bytes": len(stored),
                 "sha256": hashlib.sha256(stored).hexdigest(), "mtime": 0,
                 "compression_level": 9, "embedded_filename": ""},
        "decompression_verification": {"full_bytes_equal": restored == raw,
                                       "bytes": len(restored), "sha256": hashlib.sha256(restored).hexdigest()},
        "plain_carrier_present_after_compression": plain.exists(),
        "reader_fallback": {"tool": Path(__file__).relative_to(ROOT).as_posix(),
                            "plain_path_automatically_falls_back_to_gzip": True,
                            "resolve_command_executed_successfully": True,
                            "tested_source_carrier": test_result["source_carrier"],
                            "resolve_command": "python3 " + Path(__file__).relative_to(ROOT).as_posix()
                            + " --resolve " + OUT_REL + " /summary"},
        "semantic_reader": False, "full_reading_credit": False, "semantic_verdict": None,
    }
    encoded = (json.dumps(mapping, ensure_ascii=False, indent=2) + "\n").encode()
    (ROOT / COMPRESSION_REL).write_bytes(encoded)
    print(json.dumps({"compression_mapping": COMPRESSION_REL, "mapping_bytes": len(encoded),
                      "mapping_sha256": hashlib.sha256(encoded).hexdigest(), **mapping}, ensure_ascii=False))


def token(key):
    return str(key).replace("~", "~0").replace("/", "~1")


def resolve(doc, pointer):
    if pointer == "":
        return doc
    if not pointer.startswith("/"):
        raise ValueError("RFC6901 pointer must be empty or start with /")
    cur = doc
    for part in pointer[1:].split("/"):
        # Reject invalid escapes as well as invalid array indices.
        i = 0
        while i < len(part):
            if part[i] == "~":
                if i + 1 >= len(part) or part[i + 1] not in "01":
                    raise ValueError("invalid RFC6901 escape")
                i += 1
            i += 1
        key = part.replace("~1", "/").replace("~0", "~")
        if isinstance(cur, list):
            if not key.isdigit() or (len(key) > 1 and key.startswith("0")):
                raise ValueError("invalid array index")
            cur = cur[int(key)]
        elif isinstance(cur, dict):
            cur = cur[key]
        else:
            raise ValueError("pointer continues beyond a scalar")
    return cur


def checked(doc, pointer, expected=None, compare=False):
    global POINTER_CHECKS
    result = resolve(doc, pointer)
    if compare and result != expected:
        raise ValueError(f"pointer did not dereference to expected value: {pointer}")
    POINTER_CHECKS += 1
    return result


def kind(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, str):
        return "string"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    raise TypeError(type(value))


def brief(value):
    result = {"type": kind(value)}
    if isinstance(value, dict):
        result["keys"] = list(value)
        result["member_count"] = len(value)
    elif isinstance(value, list):
        result["item_count"] = len(value)
    return result


class Structures:
    def __init__(self):
        self.definitions = []
        self.interned = {}
        self.nodes_examined = 0

    def add(self, value):
        self.nodes_examined += 1
        typ = kind(value)
        if typ == "object":
            members = tuple((key, self.add(child)) for key, child in value.items())
            identity = (typ, members)
            definition = {"type": typ, "members": [list(item) for item in members]}
        elif typ == "array":
            runs = []
            for child in value:
                ref = self.add(child)
                if runs and runs[-1][0] == ref:
                    runs[-1][1] += 1
                else:
                    runs.append([ref, 1])
            identity = (typ, tuple(tuple(run) for run in runs))
            definition = {"type": typ, "length": len(value), "item_structure_runs": runs}
        else:
            identity = (typ,)
            definition = {"type": typ}
        if identity not in self.interned:
            self.interned[identity] = len(self.definitions)
            self.definitions.append(definition)
        return self.interned[identity]


def structural_document(doc, structures):
    top = []
    if isinstance(doc, dict):
        children = doc.items()
    elif isinstance(doc, list):
        children = enumerate(doc)
    else:
        children = []
    for key, val in children:
        pointer = "/" + token(key)
        node = checked(doc, pointer, val, True)
        top.append({"json_pointer": pointer, **brief(node)})
    checked(doc, "", doc, True)
    return {"root_json_pointer": "", "root_structure_ref": structures.add(doc),
            "top_level_navigation": top}


def format_of(path):
    if path.endswith(".json.gz"):
        return "gzip/application-json"
    if path.endswith(".jsonl"):
        return "application-jsonlines"
    if path.endswith(".json"):
        return "application-json"
    if path.endswith(".gz"):
        return "gzip/" + format_of(path[:-3])
    return {".md": "text/markdown", ".py": "text/x-python", ".js": "text/javascript",
            ".tsv": "text/tab-separated-values", ".diff": "text/x-diff",
            ".patch": "text/x-diff", ".txt": "text/plain", ".stdout": "text/plain",
            ".stderr": "text/plain"}.get(Path(path).suffix, "application/octet-stream")


def inspect_raw(path, raw, structures):
    entry = {"format": format_of(path), "bytes": len(raw)}
    decoded = raw
    if path.endswith(".gz"):
        decoded = gzip.decompress(raw)
        entry["uncompressed_bytes"] = len(decoded)
    if path.endswith((".json", ".json.gz")):
        doc = parse(decoded)
        entry["json_structure"] = structural_document(doc, structures)
        entry["json_parse"] = "complete_document_parsed_duplicate_keys_rejected"
    elif path.endswith(".jsonl"):
        documents = []
        physical_lines = decoded.splitlines()
        for number, line in enumerate(physical_lines, 1):
            if line.strip():
                doc = parse(line)
                documents.append({"physical_line": number,
                                  **structural_document(doc, structures)})
        entry["jsonl_structure"] = {"physical_line_count": len(physical_lines),
                                    "nonblank_record_count": len(documents),
                                    "records": documents}
        entry["json_parse"] = "all_nonblank_lines_parsed_duplicate_keys_rejected"
    return entry


def source_value(doc, pointer):
    return {"manifest_json_pointer": pointer,
            "value": checked(doc, pointer)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--resolve", nargs=2, metavar=("PATH", "RFC6901_POINTER"))
    actions.add_argument("--compress", action="store_true")
    actions.add_argument("--summary", action="store_true")
    parser.add_argument("--remove-plain", action="store_true")
    parser.add_argument("--jsonl-line", type=int)
    args = parser.parse_args()
    if args.remove_plain and not args.compress:
        parser.error("--remove-plain requires --compress")
    if args.compress:
        compress_inventory(args.remove_plain)
        return
    if args.summary:
        raw, carrier = load_inventory()
        print(json.dumps({"logical_path": OUT_REL, "source_carrier": carrier,
                          "summary": checked(parse(raw), "/summary")}, ensure_ascii=False, indent=2))
        return
    if args.resolve:
        path, pointer = args.resolve
        carrier = path
        if inventory_path(path):
            raw, carrier = load_inventory(path)
        else:
            raw = pinned(path, BINDING if path in (MANIFEST, PAYLOAD) else ARTIFACT)
            if path.endswith(".gz"):
                raw = gzip.decompress(raw)
        if args.jsonl_line:
            raw = raw.splitlines()[args.jsonl_line - 1]
        doc = parse(raw)
        selected = checked(doc, pointer)
        shapes = Structures()
        info = structural_document(selected, shapes)
        print(json.dumps({"path": path, "source_carrier": carrier, "json_pointer": pointer, "dereferenced": True,
                          "node": brief(selected), "selected_structure": info,
                          "structure_definitions": shapes.definitions},
                         ensure_ascii=False, indent=2))
        return

    manifest_raw = pinned(MANIFEST, BINDING)
    payload_raw = pinned(PAYLOAD, BINDING)
    manifest, payload = parse(manifest_raw), parse(payload_raw)
    assert manifest["artifact_snapshot_commit"] == ARTIFACT
    assert payload["artifact_snapshot_commit"] == ARTIFACT
    assert manifest["fixed_delivery_commit"] == payload["fixed_delivery_commit"]
    assert len(payload["files"]) == payload["file_count"] == 1008
    assert len({record["path"] for record in payload["files"]}) == 1008
    structures = Structures()
    files = []
    source_docs = []
    for path, raw, doc in [(MANIFEST, manifest_raw, manifest), (PAYLOAD, payload_raw, payload)]:
        source_docs.append({"path": path, "commit": BINDING, "bytes": len(raw),
                            "sha256": hashlib.sha256(raw).hexdigest(),
                            "format": format_of(path),
                            "json_structure": structural_document(doc, structures)})

    # Read locally available immutable blobs once; do not fetch objects or run artifacts.
    cat = subprocess.Popen(["git", "cat-file", "--batch"], cwd=ROOT,
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    per_blob = {}
    try:
        for index, record in enumerate(payload["files"]):
            pointer = f"/files/{index}"
            checked(payload, pointer, record, True)
            blob = record["blob"]
            cache_key = (blob, format_of(record["path"]))
            if cache_key not in per_blob:
                cat.stdin.write((blob + "\n").encode())
                cat.stdin.flush()
                header = cat.stdout.readline().decode().rstrip("\n").split()
                if len(header) != 3 or header[1] != "blob":
                    raise ValueError(f"unavailable local blob: {blob}: {header}")
                size = int(header[2])
                raw = cat.stdout.read(size)
                if len(raw) != size or cat.stdout.read(1) != b"\n":
                    raise ValueError("truncated git cat-file output")
                per_blob[cache_key] = inspect_raw(record["path"], raw, structures)
            info = per_blob[cache_key]
            assert info["bytes"] == record["bytes"]
            files.append({"path": record["path"], **info,
                          "payload_record_json_pointer": pointer,
                          "payload_record_pointer_dereferenced": True,
                          "formal_current_file": record["formal_current_file"],
                          "changed_vs_fixed_delivery": record["changed_vs_fixed_delivery"]})
    finally:
        cat.stdin.close()
        cat.wait()
    assert sum(entry["bytes"] for entry in files) == payload["total_bytes"]
    by_path = {entry["path"]: (i, entry) for i, entry in enumerate(files)}

    def file_link(path):
        index, entry = by_path[path]
        return {"path": path, "format": entry["format"], "bytes": entry["bytes"],
                "file_inventory_json_pointer": f"/files/{index}",
                **({"root_structure_ref": entry["json_structure"]["root_structure_ref"]}
                   if "json_structure" in entry else {}),
                **({"jsonl_record_count": entry["jsonl_structure"]["nonblank_record_count"]}
                   if "jsonl_structure" in entry else {})}

    def retained(prefix, expected):
        paths = git("ls-tree", "-r", "--name-only", ARTIFACT, "--", prefix).decode().splitlines()
        assert len(paths) == expected
        assert set(paths) == {path for path in by_path if path.startswith(prefix)}
        return {"prefix": prefix, "file_count": len(paths), "files": [file_link(p) for p in paths]}

    tagging_paths = checked(manifest, "/tagging/artifact_paths")
    assert len(tagging_paths) == 175 and len(set(tagging_paths)) == 175
    tagging = {"manifest_json_pointer": "/tagging/artifact_paths", "file_count": 175,
               "files": [file_link(path) for path in tagging_paths]}
    final_prefix = checked(manifest, "/review_artifact_retention/final_review_prefix")
    prior_prefix = checked(manifest, "/review_artifact_retention/prior_full_R3_prefix")
    final_review = retained(final_prefix, checked(manifest, "/review_artifact_retention/final_review_files"))
    prior_review = retained(prior_prefix, checked(manifest, "/review_artifact_retention/prior_full_R3_files"))
    origin_path = "review/remediation-eighth-20261016-prepare/integration/tagging-final-7ed3e05/source-file-identities.json"
    origin_doc = parse(pinned(origin_path))
    origin_groups = []
    for index, expected_prefix, expected_files in [(0, "planning/implementation-routing/r8-20261017/", 175),
                                                   (1, final_prefix, 75), (2, prior_prefix, 111)]:
        pointer = f"/groups/{index}"
        group = checked(origin_doc, pointer)
        assert group["prefix"] == expected_prefix and group["files"] == expected_files
        origin_groups.append({"source_json_pointer": pointer,
                              "source_fields_verbatim": {key: group[key] for key in ("role", "commit", "prefix", "files", "bytes")}})
    changes = git("diff", "--name-status", "-z", manifest["fixed_delivery_commit"], ARTIFACT,
                  "--", FORMAL).decode().split("\0")
    changes = changes[:-1] if changes[-1] == "" else changes
    assert len(changes) % 2 == 0
    changed_formal = []
    for status, path in zip(changes[::2], changes[1::2]):
        assert status == "M"
        changed_formal.append({"git_diff_status": status, **file_link(path)})
    assert len(changed_formal) == 38

    batches = []
    entry_keys = ["batch", "required_ids", "candidate_commit", "candidate_entry_kind",
                  "candidate_manifest_path", "candidate_manifest_identity", "candidate_review_report",
                  "independent_reviewer_thread_id", "independent_reviewer_identity_evidence",
                  "actual_target_paths", "actual_integration_commit", "actual_integration_change_record",
                  "actual_integrated_review_report", "batch_ACCEPTED_receipt",
                  "additional_receiver_repair_record"]
    for index, batch in enumerate(manifest["batches"]):
        batch_pointer = f"/batches/{index}"
        checked(manifest, batch_pointer, batch, True)
        receipt = batch["batch_ACCEPTED_receipt"]
        receipt_doc = parse(pinned(receipt["path"], receipt["commit"]))
        receipt_record = checked(receipt_doc, receipt["record_pointer"])
        assert receipt_record["batch"] == batch["batch"]
        original = []
        for name in ("prompt.md", "reviewer-prompt.md", "readset.json"):
            path = f"{HANDOFF}/batches/{batch['batch']}/{name}"
            raw = pinned(path)
            original.append({"path": path, "format": format_of(path), "bytes": len(raw),
                             "local_artifact_blob_available": True})
        batches.append({"batch": batch["batch"], "manifest_json_pointer": batch_pointer,
                        "manifest_source_entries_verbatim": [source_value(manifest, batch_pointer + "/" + token(key))
                                                             for key in entry_keys if key in batch],
                        "original_handoff_entries": original,
                        "accepted_receipt_record_navigation": {
                            "commit": receipt["commit"], "path": receipt["path"],
                            "record_json_pointer": receipt["record_pointer"],
                            "record_pointer_dereferenced": True,
                            "batch_field_matches_manifest": True, "record_structure": brief(receipt_record)},
                        "full_original_contract_path": HANDOFF + "/contracts.zh.json",
                        "contract_id_navigation": "delegated_separately_no_semantic_or_reading_credit"})
    assert len(batches) == 9 and len({batch["batch"] for batch in batches}) == 9

    roadmap_paths = ["planning/framework-roadmap/README.md", "planning/framework-roadmap/DETAILED-PLAN.md",
                     "planning/framework-roadmap/QUICK-PLAN.md", "review/framework-roadmap-v1-20261017/report.md",
                     "review/framework-roadmap-v1-20261017/recheck-67d0e170/report.md"]
    roadmap = []
    for path in roadmap_paths:
        lines = pinned(path).decode("utf-8-sig").splitlines()
        headings = [{"line": n, "heading": line} for n, line in enumerate(lines, 1)
                    if line.startswith("#")]
        roadmap.append({**file_link(path), "line_count": len(lines), "heading_navigation": headings})
    roadmap_related = [file_link(entry["path"]) for entry in files
                       if entry["path"].startswith("review/framework-roadmap-v1-20261017/")]
    counts = collections.Counter(entry["format"] for entry in files)
    output = {
        "schema": "r8-final-navigation-only-inventory-v1",
        "purpose": "Mechanical file/format/byte/JSON-structure/pointer navigation only.",
        "credit_boundary": {"semantic_reader": False, "full_reading_credit": False,
                            "configuration_verdict": None, "semantic_verdict": None,
                            "acceptance_verdict": None, "source_verdict_strings_are_new_credit": False},
        "fixed_inputs": {"binding_commit": BINDING, "artifact_snapshot_commit": ARTIFACT,
                         "fixed_delivery_commit": manifest["fixed_delivery_commit"],
                         "input_json_documents": source_docs},
        "method": {"all_payload_paths_from_complete_parsed_index": True,
                   "local_immutable_git_blobs_only": True, "network_fetch": False,
                   "ruby_or_existing_evidence_scripts_executed": False,
                   "source_values_copied": "Only requested batch entry fields and Markdown headings; JSON scalar payloads omitted.",
                   "json_structure_encoding": {
                       "structure_ref": "Zero-based index into json_structure_definitions.",
                       "object_members": "Every actual key in source order paired with the child structure reference.",
                       "array_item_structure_runs": "Ordered [child structure reference, repeat count] runs; expanding yields every array index exactly.",
                       "scalar_definitions": "Only JSON type; string contents and scalar values are deliberately omitted.",
                       "complete_structure": "Object keys, array lengths, per-index child structures and scalar types are preserved at every depth.",
                       "pointer_navigation": "RFC6901: append escaped object key or decimal array index; actual pointers printed in this inventory are dereferenced.",
                       "jsonl": "Each nonblank physical line has its own JSON root and complete structure.",
                       "gzip": "Stored byte count plus decoded byte count; JSON.gz parsed after local decompression.",
                       "resolve_command": "python3 review/remediation-eighth-20261016-prepare/reviews/final-ultra/r1/build-final-navigation-only.py --resolve PATH RFC6901_POINTER [--jsonl-line N]"}},
        "summary": {"file_count": len(files), "stored_bytes": sum(entry["bytes"] for entry in files),
                    "format_counts": dict(sorted(counts.items())), "changed_formal_files": len(changed_formal),
                    "tagging_files": 175, "final_review_files": final_review["file_count"],
                    "prior_full_R3_review_files": prior_review["file_count"],
                    "json_structural_nodes_examined": structures.nodes_examined,
                    "unique_structure_definitions": len(structures.definitions)},
        "files": files,
        "changed_formal": {"comparison": {"base": manifest["fixed_delivery_commit"], "target": ARTIFACT},
                           "path_prefix": FORMAL, "file_count": 38, "files": changed_formal},
        "tagging_author_files": tagging,
        "retained_final_review": final_review,
        "retained_prior_full_R3_review": prior_review,
        "retained_origin_commit_navigation": {"path": origin_path, "commit": ARTIFACT,
                                               "groups": origin_groups},
        "batch_source_entry_navigation": batches,
        "roadmap_and_faithfulness_entry_navigation": {"requested_entries": roadmap,
                                                     "related_review_files": roadmap_related,
                                                     "faithfulness_verdict": None},
        "json_structure_definitions": structures.definitions,
    }
    for group in [tagging, final_review, prior_review, output["changed_formal"]]:
        for link in group["files"]:
            selected = checked(output, link["file_inventory_json_pointer"])
            assert selected["path"] == link["path"] and selected["bytes"] == link["bytes"]
    for link in roadmap + roadmap_related:
        assert checked(output, link["file_inventory_json_pointer"])["path"] == link["path"]
    output["summary"]["explicit_pointer_dereferences_checked"] = POINTER_CHECKS
    encoded = (json.dumps(output, ensure_ascii=False, indent=2) + "\n").encode()
    destination = ROOT / OUT_REL
    assert destination.parent == Path(__file__).resolve().parent
    destination.write_bytes(encoded)
    print(json.dumps({"output": OUT_REL, "bytes": len(encoded),
                      "sha256": hashlib.sha256(encoded).hexdigest(),
                      "summary": output["summary"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
