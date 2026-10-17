"""Mechanical navigation only: display exact values/ranges, never certify reading.

Examples (all offsets are zero-based Unicode character offsets):
  python3 continuation-reading-nav.py --doc READSET --mode values
  python3 continuation-reading-nav.py --doc READSET --pointer /inherited_contents
  python3 continuation-reading-nav.py --ledger full-reading-ledger.json --mode values
  python3 continuation-reading-nav.py --ledger full-reading-ledger.json --start 15000
  python3 continuation-reading-nav.py --source 'Data/Scripts/002_BattleSettings.rb' --range 4:19
  python3 continuation-reading-nav.py --formal 'deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md' --range 1:40

Fixed JSON documents are selected from the lossless inventory or original seven
candidate-review ledgers. Metadata reference mode substitutes only explicitly
named identity keys with a mechanical SHA reference; other exact leaf values,
all occurrence pointers, container structure and empty containers remain.
--metadata inline includes every original metadata value as well. No substring
or content-based semantic filtering is used.

Source/formal commands only call git show and slice fixed text. They never run
the source. Every invocation records actual tool times, full-read byte hashes,
render hashes and returned chunk limits to the r1-local JSONL navigation log.
These are navigation/tool records, not semantic FULL or execution evidence.
"""
import argparse
from collections import OrderedDict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / ".git").exists())
SOURCE = Path("/workspace/pokemon-essentials")
INVENTORY = HERE / "continuation-input-inventory.json"
data = json.loads(INVENTORY.read_text())
LEDGER_PREFIX = "review/remediation-eighth-20261016-prepare/reviews/R8-U06/independent-20261017/"
LEDGERS = {x["path"].rsplit("/", 1)[-1]: x for x in data["candidate_ledger_JSON_structures"]}
IDENTITY_KEYS = {
    "repo", "commit", "tree", "workspace_tree", "report_tree", "formal_tree",
    "path", "pointer", "json_pointer", "blob", "mode", "bytes", "sha256",
    "wholefile_sha256", "unit_sha256", "slice_sha256", "slice_bytes",
    "canonical_projection_sha256", "render_sha256", "value_sha256",
    "stdout_sha256", "stdout_bytes", "fixed_R", "fixed_B8",
    "baseline_commit", "candidate_commit", "reference_commit", "fixed_head",
    "fixed_candidate", "fixed_baseline", "fixed_reference",
}

parser = argparse.ArgumentParser(description=__doc__)
group = parser.add_mutually_exclusive_group()
group.add_argument("--doc", help="READSET or exact contract ID")
group.add_argument("--ledger", choices=sorted(LEDGERS))
group.add_argument("--payload", help="exact candidate:relative-path or review:relative-path from inventory")
group.add_argument("--source", help="fixed reference repo path; text only")
group.add_argument("--formal", help="fixed project repo path; text only")
parser.add_argument("--pointer", default="", help="RFC6901 pointer within JSON document")
parser.add_argument("--mode", choices=["values", "json", "structure"], default="values")
parser.add_argument("--metadata", choices=["reference", "inline"], default="reference")
parser.add_argument("--start", type=int, default=0)
parser.add_argument("--chars", type=int, default=15000, help="max characters per chunk; 0 means all")
parser.add_argument("--range", action="append", default=[], help="inclusive line range start:end; repeatable")
parser.add_argument("--commit", help="explicit fixed commit for source/formal text")
parser.add_argument("--log", default="continuation-navigation-reads.jsonl",
                    help="r1-relative JSONL log path; cannot escape allowed directory")
args = parser.parse_args()
log_path = (HERE / args.log).resolve()
if not log_path.is_relative_to(HERE):
    raise ValueError("--log must remain within the allowed r1 directory")
started = datetime.now(timezone.utc).isoformat()
commands = []


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode()


def show(root, commit, path):
    begin = datetime.now(timezone.utc).isoformat()
    command = ["git", "show", commit + ":" + path]
    proc = subprocess.run(command, cwd=root, capture_output=True, check=False)
    commands.append({"argv": command, "cwd": str(root), "started_utc": begin,
                     "finished_utc": datetime.now(timezone.utc).isoformat(),
                     "exit_code": proc.returncode, "stdout_bytes": len(proc.stdout),
                     "stdout_sha256": sha(proc.stdout), "stderr_bytes": len(proc.stderr),
                     "stderr_sha256": sha(proc.stderr),
                     "stderr_utf8": proc.stderr.decode(errors="replace")})
    if proc.returncode:
        raise RuntimeError(commands[-1])
    return proc.stdout


def restore(node):
    if node[0] == "v":
        return data["value_table"][node[1]]["value"]
    if node[0] == "o":
        return {key: restore(child) for key, child in node[1]}
    return [restore(child) for child in node[1]]


def at(value, pointer):
    if not pointer:
        return value
    if not pointer.startswith("/"):
        raise ValueError("--pointer must be empty or begin with /")
    for key in pointer[1:].split("/"):
        key = key.replace("~1", "/").replace("~0", "~")
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def escape(key):
    return str(key).replace("~", "~0").replace("/", "~1")


def walk(value, pointer="", field=""):
    yield pointer, field, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, pointer + "/" + escape(key), key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, pointer + "/" + str(index), field)


identity = {}
range_receipts = []
if args.source or args.formal:
    if args.pointer:
        raise ValueError("--pointer is for JSON; use --range for source/formal text")
    if not args.range:
        raise ValueError("source/formal navigation requires an explicit --range")
    root = SOURCE if args.source else REPO
    path = args.source or args.formal
    commit = args.commit or ("8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
                             if args.source else data["actual_snapshot"])
    raw = show(root, commit, path)
    lines = raw.splitlines(keepends=True)
    identity = {"repo": str(root), "commit": commit, "path": path,
                "bytes": len(raw), "sha256": sha(raw), "line_count": len(lines)}
    blocks = []
    for specification in args.range:
        first, last = map(int, specification.split(":", 1))
        if not 1 <= first <= last <= len(lines):
            raise ValueError("inclusive range outside the complete fixed file")
        sliced = b"".join(lines[first - 1:last])
        range_receipts.append({"range_inclusive": [first, last], "bytes": len(sliced),
                               "sha256": sha(sliced), "slice_rule": "original line endings retained"})
        blocks.append(json.dumps({"range_inclusive": [first, last], "slice_sha256": sha(sliced)})
                      + "\n" + sliced.decode())
    rendered = "\n".join(blocks)
elif args.doc or args.ledger or args.payload:
    text_payload = None
    if args.doc:
        doc = next(x for x in data["lossless_documents"] if x["id"] == args.doc)
        value = restore(doc["tree"])
        assert sha(canonical(value)) == doc["parsed_value_canonical_sha256"]
        identity = {key: doc[key] for key in ["id", "carrier_repo", "carrier_commit",
                                            "carrier_path", "carrier_pointer", "carrier_bytes",
                                            "carrier_sha256", "parsed_value_canonical_sha256"]}
    elif args.ledger:
        ledger = LEDGERS[args.ledger]
        raw = show(REPO, ledger["commit"], ledger["path"])
        assert len(raw) == ledger["bytes"] and sha(raw) == ledger["sha256"]
        value = json.loads(raw)
        identity = {key: ledger[key] for key in ["id", "commit", "path", "bytes", "sha256"]}
    else:
        item = next(x for x in data["candidate_and_review_file_navigation"] if x["key"] == args.payload)
        raw = show(REPO, item["actual_commit"], item["path"])
        assert len(raw) == item["bytes"] and sha(raw) == item["sha256"]
        identity = dict(item)
        if item["format"] == "JSON":
            value = json.loads(raw)
        elif item["format"] == "JSONL":
            value = [json.loads(line) for line in raw.decode().splitlines() if line.strip()]
        else:
            if args.pointer:
                raise ValueError("--pointer requires JSON or JSONL payload")
            text_payload = raw.decode()
    selected = None if text_payload is not None else at(value, args.pointer)
    if text_payload is not None:
        rendered = text_payload
    elif args.mode == "json":
        # Exact original parsed JSON, including identity values, always remains available.
        rendered = json.dumps(selected, ensure_ascii=False, indent=2)
    else:
        structures = []
        unique = OrderedDict()
        metadata = []
        for pointer, field, leaf in walk(selected, args.pointer):
            if isinstance(leaf, (dict, list)):
                structures.append([pointer, "object", list(leaf)] if isinstance(leaf, dict)
                                  else [pointer, "array", len(leaf)])
                continue
            is_metadata = field in IDENTITY_KEYS
            if is_metadata and args.metadata == "reference":
                metadata.append([pointer, type(leaf).__name__])
                continue
            key = (type(leaf).__name__, canonical(leaf))
            if key not in unique:
                unique[key] = {"first_pointer": pointer, "exact_value": leaf,
                               "JSON_type": type(leaf).__name__, "later_exact_occurrence_pointers": []}
            else:
                unique[key]["later_exact_occurrence_pointers"].append(pointer)
        rows = []
        if args.mode == "values":
            rows.extend(unique.values())
        rows.append({"container_structure_encoding": "[pointer, object, ordered keys] or [pointer, array, length]",
                     "container_structure": structures})
        if args.mode == "values":
            rows.append({"identity_metadata_reference_encoding": "[pointer, JSON scalar type]; exact value in fixed carrier already named by receipt and mechanical identity evidence",
                         "identity_metadata_references": metadata})
        rendered = "\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in rows)
else:
    rendered = json.dumps({"documents": [x["id"] for x in data["lossless_documents"]],
                           "ledgers": sorted(LEDGERS),
                           "payloads": [x["key"] for x in data.get("candidate_and_review_file_navigation", [])],
                           "credit": "navigation only; no semantic reading or verdict"}, ensure_ascii=False, indent=2)

end = len(rendered) if args.chars == 0 else min(len(rendered), args.start + args.chars)
if not 0 <= args.start <= len(rendered):
    raise ValueError("--start outside the complete rendered text")
chunk = rendered[args.start:end]
receipt = {"schema": "r8-u06-mechanical-navigation-tool-read/v1", "started_utc": started,
           "finished_utc": datetime.now(timezone.utc).isoformat(), "identity": identity,
           "selected_pointer": args.pointer, "mode": args.mode, "metadata_mode": args.metadata,
           "start": args.start, "end_exclusive": end, "total_chars": len(rendered),
           "next_start": end if end < len(rendered) else None,
           "render_sha256": sha(rendered.encode()), "chunk_bytes": len(chunk.encode()),
           "chunk_sha256": sha(chunk.encode()), "range_receipts": range_receipts,
           "commands": commands, "semantic_read_credit": "NOT_ASSESSED_BY_TOOL",
           "business_execution": "NOT_EXECUTED"}
with log_path.open("a") as stream:
    stream.write(json.dumps(receipt, ensure_ascii=False, separators=(",", ":")) + "\n")
print(json.dumps(receipt, ensure_ascii=False, separators=(",", ":")))
print(chunk)
