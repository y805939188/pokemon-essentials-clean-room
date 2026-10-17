"""Read-only, lossless navigation printer. Never assigns semantic reading credit.

Examples:
  python3 continuation_print.py --id GR8-COM-008 --chars 10000
  python3 continuation_print.py --id GR8-COM-008 --start 10000 --chars 10000
  python3 continuation_print.py --id GR8-COM-008 --mode leaves --chars 10000
  python3 continuation_print.py --id READSET --pointer /conditional_F05_readset

The default JSON view reconstructs every parsed value, object key and array order.
Leaf mode retains every leaf occurrence; repeated typed values point to the first
document/pointer. Pass --expand-repeats to print those repeated values as well.
All output is stdout; this program creates or changes no files.
"""
from pathlib import Path
import argparse
import hashlib
import json

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--id", help="READSET or exact contract ID; omitted lists all IDs")
parser.add_argument("--pointer", default="", help="RFC6901 pointer within this record")
parser.add_argument("--mode", choices=["json", "leaves", "values"], default="json")
parser.add_argument("--expand-repeats", action="store_true")
parser.add_argument("--start", type=int, default=0, help="zero-based character offset")
parser.add_argument("--chars", type=int, default=10000, help="maximum characters; 0 means all")
args = parser.parse_args()
inventory = json.loads((Path(__file__).resolve().parent / "continuation-input-inventory.json").read_text())
documents = inventory["lossless_documents"]
values = inventory["value_table"]


def decode(node):
    if node[0] == "v":
        return values[node[1]]["value"]
    if node[0] == "o":
        return {key: decode(child) for key, child in node[1]}
    return [decode(child) for child in node[1]]


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


def leaf_rows(node, pointer=""):
    if node[0] == "v":
        entry = values[node[1]]
        row = {"pointer": pointer, "value_id": node[1]}
        first = {"document": entry["first_document"], "pointer": entry["first_pointer"]}
        if args.expand_repeats or first == {"document": args.id, "pointer": pointer}:
            row["exact_value"] = entry["value"]
        else:
            row["duplicate_exact_typed_value_of"] = first
        return [row]
    if not node[1]:
        return [{"pointer": pointer, "exact_empty_container": {} if node[0] == "o" else []}]
    rows = []
    children = node[1] if node[0] == "o" else enumerate(node[1])
    for key, child in children:
        rows.extend(leaf_rows(child, pointer + "/" + escape(key)))
    return rows


if not args.id:
    print(json.dumps([{"id": x["id"], "carrier_pointer": x["carrier_pointer"],
                       "canonical_sha256": x["parsed_value_canonical_sha256"]}
                      for x in documents], ensure_ascii=False, indent=2))
else:
    doc = next(x for x in documents if x["id"] == args.id)
    restored = decode(doc["tree"])
    canonical = json.dumps(restored, ensure_ascii=False, separators=(",", ":")).encode()
    assert hashlib.sha256(canonical).hexdigest() == doc["parsed_value_canonical_sha256"]
    if args.mode == "json":
        value = at(restored, args.pointer)
        rendered = json.dumps(value, ensure_ascii=False, indent=2)
    else:
        rows = leaf_rows(doc["tree"])
        if args.pointer:
            rows = [x for x in rows if x["pointer"] == args.pointer
                    or x["pointer"].startswith(args.pointer + "/")]
        if args.mode == "values":
            unique = {}
            empty = []
            for row in rows:
                if "value_id" not in row:
                    empty.append(row)
                    continue
                number = row["value_id"]
                if number not in unique:
                    entry = values[number]
                    unique[number] = {"value_id": number, "exact_value": entry["value"],
                                      "global_first": {"document": entry["first_document"],
                                                       "pointer": entry["first_pointer"]},
                                      "all_occurrence_pointers_in_selected_document": []}
                unique[number]["all_occurrence_pointers_in_selected_document"].append(row["pointer"])
            rows = [*unique.values(), *empty]
        rendered = "\n".join(json.dumps(x, ensure_ascii=False, separators=(",", ":")) for x in rows)
    end = len(rendered) if args.chars == 0 else min(len(rendered), args.start + args.chars)
    if not (0 <= args.start <= len(rendered)):
        raise ValueError("--start is outside the rendered record")
    print(json.dumps({"document": args.id, "mode": args.mode, "pointer": args.pointer,
                      "start": args.start, "end_exclusive": end, "total_chars": len(rendered),
                      "next_start": end if end < len(rendered) else None,
                      "render_sha256": hashlib.sha256(rendered.encode()).hexdigest(),
                      "credit": "navigation only; output does not certify reading"}, ensure_ascii=False))
    print(rendered[args.start:end])
