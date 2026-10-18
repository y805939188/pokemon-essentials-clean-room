#!/usr/bin/env python3
"""Read tagging mechanical navigation, with gzip fallback; never grants FULL."""
import argparse
import collections
import gzip
import hashlib
import importlib.util
import json
import pathlib
import sys

sys.dont_write_bytecode = True
OUT = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("tagging_reading_build", OUT / "tagging-reading-build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


def source(logical):
    path = OUT / logical
    if not path.exists():
        path = pathlib.Path(str(path) + ".gz")
    return gzip.open(path, "rt", encoding="utf-8") if str(path).endswith(".gz") else path.open(encoding="utf-8")


def rows(logical):
    with source(logical) as stream:
        for line in stream:
            if line.strip():
                yield json.loads(line)


def source_text(path):
    stored = build.raw(path)
    decoded = gzip.decompress(stored) if path.endswith(".gz") else stored
    return decoded.decode("utf-8"), decoded


def node_count(value):
    count, stack = 0, [value]
    while stack:
        cur = stack.pop()
        count += 1
        if isinstance(cur, dict):
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)
    return count


def use_signature(use):
    return build.encoded([use[key] for key in ("document_index", "document", "source_path", "pointer", "unicode_start", "unicode_end", "byte_start", "byte_end", "raw_token_sha256")]).encode() + b"\n"


def verify():
    values, declared, actual = [], [], []
    all_occurrences = 0
    for row in rows("tagging-reading-values.jsonl"):
        assert row["value_index"] == len(values)
        assert build.typ(row["value"]) == row["type"]
        values.append((row["type"], row["value"]))
        digest = hashlib.sha256()
        assert row["all_occurrences_explicit_metadata"] == all(use["explicit_metadata_key"] for use in row["occurrences"])
        for use in row["occurrences"]:
            pointer = use["pointer"]
            terminal = build.unesc(pointer.rsplit("/", 1)[-1]) if pointer else ""
            assert terminal == use["exact_terminal_key"]
            assert use["explicit_metadata_key"] == (terminal in build.ALLOWLIST)
            digest.update(use_signature(use))
        declared.append((len(row["occurrences"]), digest.hexdigest()))
        actual.append([0, hashlib.sha256()])
        all_occurrences += len(row["occurrences"])
    current_document, current_path, original, text, decoded, seen = None, None, None, None, None, set()
    expected_count, total_nodes, roots = 0, 0, 0
    for row in rows("tagging-reading-nodes.jsonl"):
        if current_document != row["document"]:
            if current_document is not None:
                assert len(seen) == expected_count
            if current_path != row["source_path"]:
                current_path = row["source_path"]
                text, decoded = source_text(current_path)
            current_document = row["document"]
            if row.get("source_kind") == "whole_text_document":
                original = text
                expected_count = 1
            elif "#jsonl-line/" in current_document:
                line_number = int(current_document.rsplit("/", 1)[-1])
                original = json.loads(text.splitlines()[line_number - 1])
                expected_count = node_count(original)
            else:
                original = json.loads(text.lstrip("\ufeff"))
                expected_count = node_count(original)
            seen = set()
            roots += 1
        pointer = row["pointer"]
        assert pointer not in seen
        seen.add(pointer)
        selected = build.resolve(original, pointer)
        assert build.typ(selected) == row["type"]
        token = decoded[row["byte_start"]:row["byte_end"]]
        assert token == text[row["unicode_start"]:row["unicode_end"]].encode()
        assert build.sha(token) == row["raw_token_sha256"]
        if row["type"] == "object":
            assert list(selected) == row["keys"]
        elif row["type"] == "array":
            assert len(selected) == row["length"]
        else:
            index = row["value_index"]
            assert (build.typ(selected), build.encoded(selected)) == (values[index][0], build.encoded(values[index][1]))
            actual[index][0] += 1
            actual[index][1].update(use_signature(row))
        total_nodes += 1
        if total_nodes % 250000 == 0:
            print(build.encoded({"mechanical_verification_nodes": total_nodes, "credit": "none"}), file=sys.stderr, flush=True)
    assert len(seen) == expected_count
    assert len(actual) == len(declared)
    for expected, observed in zip(declared, actual):
        assert expected == (observed[0], observed[1].hexdigest())
    retained = excluded = retained_uses = excluded_uses = 0
    with source("tagging-reading-strict-narrative.txt") as stream:
        narrative = stream.read()
    for row in rows("tagging-reading-strict-use-index.jsonl"):
        index = row["value_index"]
        assert not row["all_occurrences_explicit_metadata"]
        assert row["narrative_index"] == retained
        body = values[index][1] if values[index][0] == "string" else build.encoded(values[index][1])
        expected = f"[N{retained} V{index} {values[index][0]}]\n" + body + "\n"
        assert narrative[row["projection_unicode_start"]:row["projection_unicode_end"]] == expected
        assert len(row["all_occurrences"]) == declared[index][0]
        digest = hashlib.sha256()
        for use in row["all_occurrences"]:
            digest.update(use_signature(use))
        assert digest.hexdigest() == declared[index][1]
        retained += 1
        retained_uses += row["occurrence_count"]
    for row in rows("tagging-reading-strict-excluded.jsonl"):
        index = row["value_index"]
        assert row["all_occurrences_explicit_metadata"]
        assert all(use["exact_terminal_key"] in build.ALLOWLIST for use in row["all_occurrences"])
        assert (row["type"], build.encoded(row["value"])) == (values[index][0], build.encoded(values[index][1]))
        digest = hashlib.sha256()
        for use in row["all_occurrences"]:
            digest.update(use_signature(use))
        assert (len(row["all_occurrences"]), digest.hexdigest()) == declared[index]
        excluded += 1
        excluded_uses += row["occurrence_count"]
    assert retained + excluded == len(values)
    assert retained_uses + excluded_uses == all_occurrences
    print(build.encoded({"mechanical_equality_verification": "complete", "nodes": total_nodes, "roots_including_whole_text": roots,
                         "unique_typed_values": len(values), "all_scalar_or_whole_text_uses": all_occurrences,
                         "retained_narrative_values": retained, "excluded_identity_only_values": excluded,
                         "semantic_reader": False, "full_reading_credit": False, "configuration_verdict": None}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--narrative", action="store_true")
    modes.add_argument("--value", type=int)
    modes.add_argument("--document")
    modes.add_argument("--pointer", nargs=2, metavar=("PATH", "RFC6901_POINTER"))
    modes.add_argument("--file", help="Read one tagging-reading-* logical carrier, with gzip fallback")
    modes.add_argument("--local-pointer", nargs=2, metavar=("LOGICAL_CARRIER", "RFC6901_POINTER"))
    modes.add_argument("--verify", action="store_true")
    parser.add_argument("--jsonl-line", type=int)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--chars", type=int, default=8192)
    args = parser.parse_args()
    if args.verify:
        verify()
        return
    if args.narrative:
        with source("tagging-reading-strict-narrative.txt") as stream:
            text = stream.read()
        meta = {"logical_carrier": "tagging-reading-strict-narrative.txt", "gzip_fallback": True}
    elif args.local_pointer:
        logical, pointer = args.local_pointer
        assert pathlib.Path(logical).name == logical and logical.startswith("tagging-reading-")
        with source(logical) as stream:
            selected = build.resolve(json.load(stream), pointer)
        text = selected if isinstance(selected, str) else json.dumps(selected, ensure_ascii=False, indent=2)
        meta = {"logical_carrier": logical, "gzip_fallback": True, "pointer": pointer, "pointer_dereferenced": True}
    elif args.file:
        assert pathlib.Path(args.file).name == args.file and args.file.startswith("tagging-reading-")
        with source(args.file) as stream:
            text = stream.read()
        meta = {"logical_carrier": args.file, "gzip_fallback": True}
    elif args.value is not None:
        row = next(row for row in rows("tagging-reading-values.jsonl") if row["value_index"] == args.value)
        text = row["value"] if row["type"] == "string" else build.encoded(row["value"])
        meta = {key: row[key] for key in ("value_index", "type", "all_occurrences_explicit_metadata")}
        meta["occurrence_count"] = len(row["occurrences"])
    elif args.document:
        text, _ = source_text(args.document)
        meta = {"source_path": args.document, "artifact": build.ARTIFACT}
    else:
        path, pointer = args.pointer
        text, _ = source_text(path)
        doc = json.loads(text.splitlines()[args.jsonl_line - 1]) if args.jsonl_line else json.loads(text.lstrip("\ufeff"))
        selected = build.resolve(doc, pointer)
        text = selected if isinstance(selected, str) else json.dumps(selected, ensure_ascii=False, indent=2)
        meta = {"source_path": path, "pointer": pointer, "type": build.typ(selected), "pointer_dereferenced": True}
    assert args.start >= 0 and args.chars >= 0
    end = min(len(text), args.start + args.chars)
    print(build.encoded({**meta, "unicode_start": args.start, "unicode_end": end, "total_unicode_characters": len(text),
                         "exact_text_sha256": build.sha(text.encode()), "semantic_reader": False, "full_reading_credit": False}))
    print(text[args.start:end], end="")


if __name__ == "__main__":
    main()
