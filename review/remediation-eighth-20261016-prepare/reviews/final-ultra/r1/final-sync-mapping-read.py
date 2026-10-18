#!/usr/bin/env python3
"""Read only this mechanical scope's JSON carriers with gzip fallback."""
import argparse
import gzip
import json
import pathlib

OUT = pathlib.Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("pointer", nargs="?", default="/counts")
parser.add_argument("--file", default="result.json")
args = parser.parse_args()
assert pathlib.Path(args.file).name == args.file
path = OUT / ("final-sync-mapping-" + args.file)
if not path.exists():
    path = pathlib.Path(str(path) + ".gz")
data = path.read_bytes()
value = json.loads(gzip.decompress(data) if path.suffix == ".gz" else data)
if args.pointer:
    assert args.pointer.startswith("/")
    for token in args.pointer[1:].split("/"):
        key = token.replace("~1", "/").replace("~0", "~")
        value = value[int(key)] if isinstance(value, list) else value[key]
print(json.dumps({"mechanical_navigation_only": True, "source_carrier": path.name,
                  "pointer": args.pointer, "pointer_dereferenced": True,
                  "value": value}, ensure_ascii=False, indent=2))
