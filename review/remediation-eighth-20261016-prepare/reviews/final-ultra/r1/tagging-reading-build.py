#!/usr/bin/env python3
"""Lossless mechanical tagging navigation; no semantic/FULL/configuration credit.

Only new tagging-reading-* carriers in this directory are written. Local immutable
artifact blobs are read; no fetch, Ruby, candidate tool or original evidence runs.
"""
import array
import collections
import gzip
import hashlib
import io
import json
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = pathlib.Path(__file__).resolve().parents[5]
OUT = pathlib.Path(__file__).resolve().parent
ARTIFACT = "fd414a2c6ec0a0f746b48e0924e5692221ea5d5a"
BINDING = "8ab43a609e60430492b219f0dce14ef4fdb8e47f"
MANIFEST = "review/remediation-eighth-20261016-prepare/final/independent-review-input.json"
PAYLOAD = "review/remediation-eighth-20261016-prepare/final/payload-identities.json"
ALLOWLIST = ("repo", "commit", "tree", "workspace_tree", "report_tree", "formal_tree", "path", "pointer", "json_pointer", "mode", "blob", "bytes", "sha256")
RECORD_KEYS = ("id", "feature_id", "metadata_id", "section_id", "finding_id", "requirement_id", "document_id")
EVIDENCE_TOKEN = re.compile(r"report|result|qualification|config|creat|startup|runtime|model|reasoning|service.tier|speed|fast", re.I)
NAME_TOKENS = {"report", "reports", "result", "results", "qualification", "configuration", "create", "creation", "created"}
KEY_TOKENS = {"qualification", "configuration", "create", "creation", "created"}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def raw(path, commit=ARTIFACT):
    return git("cat-file", "blob", commit + ":" + path)


def esc(value):
    return str(value).replace("~", "~0").replace("/", "~1")


def unesc(value):
    return value.replace("~1", "/").replace("~0", "~")


def typ(value):
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
    return "object" if isinstance(value, dict) else "array"


def resolve(value, pointer):
    if pointer == "":
        return value
    assert pointer.startswith("/")
    for part in pointer[1:].split("/"):
        key = unesc(part)
        if isinstance(value, list):
            assert key.isdigit() and (key == "0" or not key.startswith("0"))
            value = value[int(key)]
        else:
            value = value[key]
    return value


def format_of(path):
    if path.endswith(".gz"):
        return "gzip/" + format_of(path[:-3])
    return {".json": "application-json", ".jsonl": "application-jsonlines", ".md": "text/markdown",
            ".py": "text/x-python", ".txt": "text/plain", ".diff": "text/x-diff",
            ".patch": "text/x-diff", ".stdout": "text/plain", ".stderr": "text/plain",
            ".tsv": "text/tab-separated-values", ".js": "text/javascript"}.get(pathlib.Path(path).suffix, "application/octet-stream")


class Carrier:
    def __init__(self, logical):
        self.logical = logical
        self.path = OUT / (logical + ".gz")
        self.file = self.path.open("wb")
        self.gz = gzip.GzipFile(filename="", mode="wb", fileobj=self.file, compresslevel=9, mtime=0)
        self.buffer = io.BufferedWriter(self.gz, 1024 * 1024)
        self.hash = hashlib.sha256()
        self.size = 0

    def write(self, data):
        if isinstance(data, str):
            data = data.encode()
        self.hash.update(data)
        self.size += len(data)
        self.buffer.write(data)

    def row(self, value):
        self.write(encoded(value) + "\n")

    def close(self):
        self.buffer.close()
        self.file.close()
        stored_hash = hashlib.sha256()
        with self.path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                stored_hash.update(chunk)
        restored_hash = hashlib.sha256()
        restored_bytes = 0
        with gzip.open(self.path, "rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                restored_hash.update(chunk)
                restored_bytes += len(chunk)
        assert restored_bytes == self.size and restored_hash.hexdigest() == self.hash.hexdigest()
        with self.path.open("rb") as stream:
            header = stream.read(10)
        assert int.from_bytes(header[4:8], "little") == 0
        return {"logical_path": str((OUT / self.logical).relative_to(ROOT)),
                "plain_bytes": self.size, "plain_sha256": self.hash.hexdigest(),
                "gzip_path": str(self.path.relative_to(ROOT)), "gzip_bytes": self.path.stat().st_size,
                "gzip_sha256": stored_hash.hexdigest(), "gzip_mtime": 0,
                "full_decompression_bytes_and_sha256_verified": True}


class Parser:
    def __init__(self, text, base=0):
        self.text, self.base, self.nodes = text, base, {}
        self.decoder = json.JSONDecoder()

    def ws(self, i):
        while i < len(self.text) and self.text[i] in " \t\r\n":
            i += 1
        return i

    def parse(self):
        begin = 1 if self.text.startswith("\ufeff") else 0
        value, end = self.val(self.ws(begin), "")
        assert self.ws(end) == len(self.text)
        assert value == json.loads(self.text.lstrip("\ufeff"))
        return value, self.nodes

    def val(self, i, pointer):
        start, char, keys, keyspans = i, self.text[i], [], []
        if char == "{":
            value = {}
            i = self.ws(i + 1)
            while self.text[i] != "}":
                key_start = i
                key, i = self.decoder.raw_decode(self.text, i)
                assert isinstance(key, str) and key not in value
                keys.append(key)
                keyspans.append([key, self.base + key_start, self.base + i])
                i = self.ws(i)
                assert self.text[i] == ":"
                child, i = self.val(self.ws(i + 1), pointer + "/" + esc(key))
                value[key] = child
                i = self.ws(i)
                if self.text[i] == "}":
                    break
                assert self.text[i] == ","
                i = self.ws(i + 1)
            i += 1
        elif char == "[":
            value = []
            i = self.ws(i + 1)
            while self.text[i] != "]":
                child, i = self.val(i, pointer + "/" + str(len(value)))
                value.append(child)
                i = self.ws(i)
                if self.text[i] == "]":
                    break
                assert self.text[i] == ","
                i = self.ws(i + 1)
            i += 1
        else:
            value, i = self.decoder.raw_decode(self.text, i)
        node = {"pointer": pointer, "type": typ(value), "unicode_start": self.base + start,
                "unicode_end": self.base + i}
        if isinstance(value, dict):
            node.update(keys=keys, key_unicode_spans=keyspans)
        elif isinstance(value, list):
            node["length"] = len(value)
        else:
            node["value"] = value
        self.nodes[pointer] = node
        return value, i


def record_contexts(value):
    result = {}
    def walk(cur, pointer="", context=None):
        if isinstance(cur, dict):
            local = next((key for key in RECORD_KEYS if key in cur and isinstance(cur[key], (str, int)) and not isinstance(cur[key], bool)), None)
            if local:
                context = {"record_pointer": pointer, "exact_record_key": local, "record_value": cur[local]}
            if context:
                result[pointer] = context
            for key, child in cur.items():
                walk(child, pointer + "/" + esc(key), context)
        elif isinstance(cur, list):
            if context:
                result[pointer] = context
            for index, child in enumerate(cur):
                walk(child, pointer + "/" + str(index), context)
        elif context:
            result[pointer] = context
    walk(value)
    return result


def write_json(name, value):
    path = OUT / ("tagging-reading-" + name)
    data = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()
    if len(data) > 1024 * 1024:
        writer = Carrier(path.name)
        writer.write(data)
        result = writer.close()
        if path.exists():
            assert path.read_bytes() == data and not path.is_symlink()
            tracked = subprocess.run(["git", "ls-files", "--error-unmatch", "--", str(path.relative_to(ROOT))],
                                     cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert tracked.returncode != 0
            path.unlink()
        return result
    path.write_bytes(data)
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def priority(manifest, payload):
    paths = manifest["tagging"]["artifact_paths"]
    origins = [("candidate", "7ed3e0554ac24339a7e61cab152f628037111644", "planning/implementation-routing/r8-20261017/", 175),
               ("final_independent", "1baee5d7346592478b72d8983b0109e1b2a5e2d9", manifest["review_artifact_retention"]["final_review_prefix"], 75),
               ("prior_full_R3_independent", "34202eb7accfee48bb8761db88b340bd77f54a42", manifest["review_artifact_retention"]["prior_full_R3_prefix"], 111)]
    allpaths = list(paths)
    for role, commit, prefix, count in origins[1:]:
        found = git("ls-tree", "-r", "--name-only", ARTIFACT, "--", prefix).decode().splitlines()
        assert len(found) == count
        allpaths += found
    assert len(allpaths) == len(set(allpaths)) == 361
    identities = {row["path"]: row for row in payload["files"]}
    routepath = "planning/implementation-routing/r8-20261017/routing-manifest.json"
    route = json.loads(raw(routepath))
    coverpath = "planning/implementation-routing/r8-20261017/current-section-coverage.json"
    cover = json.loads(raw(coverpath))
    indexes = {}
    for key, idkey, count in [("features", "feature_id", 736), ("retired_features", "feature_id", 33), ("metadata_records", "metadata_id", 33)]:
        assert len(route[key]) == count
        rows = []
        for i, row in enumerate(route[key]):
            pointer = "/" + key + "/" + str(i)
            actual = resolve(route, pointer)
            assert actual is row
            rows.append({"pointer": pointer, idkey: actual[idkey]})
        indexes[key] = {"path": routepath, "pointer": "/" + key, "count": count, "records": rows}
    backfilled = []
    for i, feature in enumerate(route["features"]):
        if feature["upstream"]["accepted_events"]:
            ptr = "/features/" + str(i)
            assert resolve(route, ptr) is feature
            assert resolve(route, ptr + "/upstream/status") == "已回填ACCEPTED源规格；去向待独立复审"
            backfilled.append({"pointer": ptr, "feature_id": feature["feature_id"],
                               "status_pointer": ptr + "/upstream/status",
                               "accepted_events_pointer": ptr + "/upstream/accepted_events",
                               "accepted_event_count": len(resolve(route, ptr + "/upstream/accepted_events"))})
    assert len(backfilled) == 230
    sections = []
    for i, section in enumerate(cover["sections"]):
        ptr = "/sections/" + str(i)
        assert resolve(cover, ptr) is section
        sections.append({"pointer": ptr, "path": section["path"], "anchor": section["anchor"],
                         "title": section["title"], "document_id": section["document_id"]})
    assert len(sections) == 2704
    focused = []
    for path in allpaths:
        name_matches = sorted(set(re.split(r"[^a-z0-9]+", pathlib.Path(path).name.lower())) & NAME_TOKENS)
        pointer_matches = []
        if path.endswith((".json", ".json.gz")):
            data = raw(path)
            parsed = json.loads(gzip.decompress(data) if path.endswith(".gz") else data)
            def scan(cur, ptr=""):
                if isinstance(cur, dict):
                    for key, child in cur.items():
                        target = ptr + "/" + esc(key)
                        tokens = sorted(set(re.split(r"[^a-z0-9]+", key.lower())) & KEY_TOKENS)
                        if tokens:
                            assert resolve(parsed, target) is child or resolve(parsed, target) == child
                            pointer_matches.append({"pointer": target, "exact_key": key, "matched_key_tokens": tokens,
                                                    "type": typ(child), **({"length": len(child)} if isinstance(child, (dict, list)) else {})})
                        scan(child, target)
                elif isinstance(cur, list):
                    for i, child in enumerate(cur):
                        scan(child, ptr + "/" + str(i))
            scan(parsed)
        if name_matches or pointer_matches:
            focused.append({"path": path, "format": format_of(path), "bytes": identities[path]["bytes"],
                            "matched_basename_tokens": name_matches, "actual_JSON_property_pointers": pointer_matches})
    assert len(focused) == 116 and sum(row["bytes"] for row in focused) == 45784983
    p = {"qualification": "MECHANICAL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT",
         "artifact": ARTIFACT, "origins": [{"role": r, "commit": c, "prefix": p, "files": n} for r, c, p, n in origins],
         "routing_record_indexes": indexes, "backfilled_features": {"path": routepath, "count": 230, "records": backfilled},
         "current_sections": {"path": coverpath, "pointer": "/sections", "count": 2704, "records": sections},
         "all_361_file_list": [{"path": path, "format": format_of(path), "bytes": identities[path]["bytes"]} for path in allpaths],
         "independent_report_result_qualification_configuration_creation_navigation": focused,
         "focused_evidence_file_count": len(focused), "focused_evidence_stored_bytes": sum(row["bytes"] for row in focused),
         "evidence_discovery_rule": "All361 files listed. Focused list matches lowercase basename tokens report,reports,result,results,qualification,configuration,create,creation,created; additionally recursively matches exact JSON property-name tokens qualification,configuration,create,creation,created. Split tokens by [^a-z0-9]+. Every printed pointer dereferenced. No string-value search or semantic eligibility judgment."}
    write_json("priority.json", p)
    return allpaths, identities, p


def main():
    manifest = json.loads(raw(MANIFEST, BINDING))
    payload = json.loads(raw(PAYLOAD, BINDING))
    paths, identities, pri = priority(manifest, payload)
    print("priority written: 736 active, 33 retired, 33 metadata, 230 backfilled, 2704 sections, all361 paths", flush=True)
    if "--priority-only" in sys.argv:
        return
    values, value_ids, documents, evidence = [], {}, [], []
    nodes_out = Carrier("tagging-reading-nodes.jsonl")
    scalar_occurrences = node_count = dereferences = json_document_count = 0

    def intern(value, occurrence):
        nonlocal scalar_occurrences
        key = (typ(value), encoded(value))
        if key not in value_ids:
            value_ids[key] = len(values)
            values.append({"value_index": len(values), "type": key[0], "value": value, "occurrences": []})
        index = value_ids[key]
        values[index]["occurrences"].append(occurrence)
        scalar_occurrences += 1
        return index

    for doc_index, path in enumerate(paths):
        stored = raw(path)
        assert len(stored) == identities[path]["bytes"]
        decoded = gzip.decompress(stored) if path.endswith(".gz") else stored
        text = decoded.decode("utf-8")
        is_json = path.endswith((".json", ".json.gz"))
        is_jsonl = path.endswith(".jsonl")
        document = {"document_index": doc_index, "path": path, "artifact": ARTIFACT,
                    "format": format_of(path), "stored_bytes": len(stored), "stored_sha256": sha(stored),
                    "decoded_bytes": len(decoded), "decoded_sha256": sha(decoded),
                    "unicode_characters": len(text), "line_count": len(text.splitlines()),
                    "logical_documents": [], "heading_navigation": []}
        if path.endswith(".md"):
            document["heading_navigation"] = [{"line": i, "heading": line} for i, line in enumerate(text.splitlines(), 1) if line.startswith("#")]
        keymatches = set()
        if is_json:
            parts = [(path, text, 0, None, 0)]
        elif is_jsonl:
            parts, offset, byte_offset = [], 0, 0
            for line_number, line in enumerate(text.splitlines(keepends=True), 1):
                if line.strip():
                    parts.append((path + "#jsonl-line/" + str(line_number), line, offset, line_number, byte_offset))
                offset += len(line)
                byte_offset += len(line.encode())
        else:
            occurrence = {"document_index": doc_index, "document": path, "source_path": path, "pointer": "",
                          "unicode_start": 0, "unicode_end": len(text), "byte_start": 0, "byte_end": len(decoded),
                          "raw_token_sha256": sha(decoded), "exact_terminal_key": "", "explicit_metadata_key": False,
                          "source_kind": "whole_text_document"}
            vi = intern(text, occurrence)
            nodes_out.row({**occurrence, "type": "string", "value_index": vi, "pointer_dereferenced": True})
            node_count += 1
            dereferences += 1
            document["logical_documents"].append({"document": path, "kind": "whole_text_document", "root_pointer": "", "node_count": 1, "root_value_index": vi})
            parts = []
        for name, part, base, line_number, base_byte in parts:
            value, nodes = Parser(part, base).parse()
            json_document_count += 1
            contexts = record_contexts(value)
            boundary_positions = {base, base + len(part)}
            for node in nodes.values():
                boundary_positions.update((node["unicode_start"], node["unicode_end"]))
                for key, start, end in node.get("key_unicode_spans", []):
                    boundary_positions.update((start, end))
                    if EVIDENCE_TOKEN.search(key):
                        keymatches.add(key)
            byte_at, previous, offset = {}, base, base_byte
            for position in sorted(boundary_positions):
                offset += len(text[previous:position].encode())
                byte_at[position] = offset
                previous = position
            for pointer, node in nodes.items():
                current = resolve(value, pointer)
                assert typ(current) == node["type"]
                if node["type"] == "object":
                    assert list(current) == node["keys"]
                elif node["type"] == "array":
                    assert len(current) == node["length"]
                else:
                    assert (typ(current), encoded(current)) == (node["type"], encoded(node["value"]))
                dereferences += 1
                start, end = node["unicode_start"], node["unicode_end"]
                row = {"document_index": doc_index, "document": name, "source_path": path, **node,
                       "byte_start": byte_at[start], "byte_end": byte_at[end],
                       "raw_token_sha256": sha(text[start:end].encode()), "pointer_dereferenced": True}
                if "key_unicode_spans" in row:
                    row["key_byte_spans"] = [[key, byte_at[start], byte_at[end]] for key, start, end in row["key_unicode_spans"]]
                if "value" in row:
                    tokens = pointer.split("/")[1:]
                    last = unesc(tokens[-1]) if tokens else ""
                    occurrence = {key: row[key] for key in ("document_index", "document", "source_path", "pointer", "unicode_start", "unicode_end", "byte_start", "byte_end", "raw_token_sha256")}
                    occurrence.update(exact_terminal_key=last, explicit_metadata_key=last in ALLOWLIST, source_kind="json_scalar")
                    if pointer in contexts:
                        occurrence["enclosing_record_identity"] = contexts[pointer]
                    row["value_index"] = intern(row.pop("value"), occurrence)
                nodes_out.row(row)
                node_count += 1
            top = []
            children = value.items() if isinstance(value, dict) else enumerate(value) if isinstance(value, list) else []
            for key, child in children:
                ptr = "/" + esc(key)
                selected = resolve(value, ptr)
                assert selected is child or selected == child
                top.append({"pointer": ptr, "type": typ(child), **({"length": len(child)} if isinstance(child, (list, dict)) else {})})
            document["logical_documents"].append({"document": name, "kind": "jsonl_record" if line_number else "json_document",
                                                   "jsonl_physical_line": line_number, "root_pointer": "", "node_count": len(nodes),
                                                   "top_level_navigation": top, "all_node_pointers_dereferenced": True})
        if keymatches or EVIDENCE_TOKEN.search(pathlib.Path(path).name):
            evidence.append({"path": path, "format": format_of(path), "bytes": len(stored),
                             "filename_token_matches": EVIDENCE_TOKEN.findall(pathlib.Path(path).name),
                             "exact_JSON_key_token_matches": sorted(keymatches)})
        documents.append(document)
        if (doc_index + 1) % 25 == 0:
            print(f"processed {doc_index + 1}/361 documents; {node_count} nodes; {len(values)} unique typed values", flush=True)

    carriers = [nodes_out.close()]
    values_out = Carrier("tagging-reading-values.jsonl")
    retained_out = Carrier("tagging-reading-strict-use-index.jsonl")
    excluded_out = Carrier("tagging-reading-strict-excluded.jsonl")
    narrative_out = Carrier("tagging-reading-strict-narrative.txt")
    retained = excluded = retained_occurrences = excluded_occurrences = narrative_characters = 0
    for value in values:
        uses = value["occurrences"]
        all_metadata = all(use["explicit_metadata_key"] for use in uses)
        value["all_occurrences_explicit_metadata"] = all_metadata
        values_out.row(value)
        entry = {"value_index": value["value_index"], "type": value["type"], "occurrence_count": len(uses),
                 "all_occurrences_explicit_metadata": all_metadata, "all_occurrences": uses}
        if all_metadata:
            assert all(use["exact_terminal_key"] in ALLOWLIST for use in uses)
            entry["value"] = value["value"]
            excluded_out.row(entry)
            excluded += 1
            excluded_occurrences += len(uses)
        else:
            body = value["value"] if value["type"] == "string" else encoded(value["value"])
            piece = f"[N{retained} V{value['value_index']} {value['type']}]\n" + body + "\n"
            entry.update(narrative_index=retained, projection_unicode_start=narrative_characters,
                         projection_unicode_end=narrative_characters + len(piece), projection_byte_start=narrative_out.size,
                         projection_byte_end=narrative_out.size + len(piece.encode()))
            narrative_characters += len(piece)
            narrative_out.write(piece)
            retained_out.row(entry)
            retained += 1
            retained_occurrences += len(uses)
    for writer in [values_out, retained_out, excluded_out, narrative_out]:
        carriers.append(writer.close())
    assert retained + excluded == len(values)
    assert retained_occurrences + excluded_occurrences == scalar_occurrences
    docfile = write_json("documents.json", {"qualification": "MECHANICAL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT",
                                            "documents": documents, "evidence_filename_or_key_navigation": evidence})
    pri["evidence_filename_or_key_navigation"] = evidence
    prifile = write_json("priority.json", pri)
    summary = {"schema": "r8-tagging-lossless-typed-scalar-navigation-v1", "artifact": ARTIFACT, "input_binding": BINDING,
               "qualification": "MECHANICAL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT",
               "exact_metadata_terminal_key_allowlist": list(ALLOWLIST),
               "deduplication": "Exact typed scalar equality only: key=(type,json.dumps(value,ensure_ascii=False,separators=(',',':'))). boolean and integer are distinct.",
               "exclusion_rule": "A value is omitted only from the narrative projection iff EVERY occurrence's exact final JSON pointer key is in the closed 13-key allowlist. Array indices and whole-text roots are not identity keys. No content/hash/path/filename heuristic filters values. Every original value and all its uses remain in values.jsonl.",
               "structure": "Every JSON/JSONL node has an actually dereferenced RFC6901 pointer, object ordered keys, array length, exact typed scalar value_index, Unicode/UTF8 ranges and original raw-token SHA256. Every nonJSON decoded document is retained as one complete string value, including stdout/scripts/Markdown/whitespace. No paragraph or sourceguard filtering.",
               "reconstruction": "Object ordered keys/array length plus every child pointer and value_index reconstruct each parsed JSON value exactly, including all scalar values. Whole-text nodes recover full decoded text exactly. Original serialized lexical tokens remain pinned by source path/artifact and exact ranges/SHA256.",
               "counts": {"documents": len(documents), "stored_source_bytes": sum(row["stored_bytes"] for row in documents),
                          "decoded_source_bytes": sum(row["decoded_bytes"] for row in documents), "parsed_JSON_or_JSONL_roots": json_document_count,
                          "nodes": node_count, "pointer_dereferences": dereferences, "unique_typed_scalar_values": len(values),
                          "scalar_occurrences": scalar_occurrences, "retained_narrative_values": retained, "excluded_from_narrative_only_values": excluded,
                          "retained_occurrences": retained_occurrences, "excluded_occurrences": excluded_occurrences,
                          "narrative_unicode_characters": narrative_characters},
               "carriers": carriers, "documents_file": docfile, "priority_file": prifile,
               "semantic_reader": False, "full_reading_credit": False, "configuration_verdict": None, "semantic_verdict": None}
    write_json("summary.json", summary)
    print(encoded(summary["counts"]), flush=True)


if __name__ == "__main__":
    main()
