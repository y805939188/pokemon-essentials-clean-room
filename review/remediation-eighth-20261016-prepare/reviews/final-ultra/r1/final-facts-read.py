"""Read-only JSON-pointer navigation for this helper's final mechanical facts.

Plain and gzip transports are checked against final-protection-locator-
compression.json when present. No source, review verdict, or scope is inferred.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def read(name):
    if Path(name).name != name:
        raise ValueError("Use an allowed local basename")
    path = HERE / name
    if path.exists():
        raw = path.read_bytes()
    else:
        raw = gzip.decompress((HERE / (name + ".gz")).read_bytes())
    mapping_path = HERE / "final-protection-locator-compression.json"
    mapping = json.loads(mapping_path.read_bytes()) if mapping_path.exists() else {}
    for row in mapping.get("files", []):
        if row["plain_name"] == name:
            assert len(raw) == row["plain_bytes"]
            assert digest(raw) == row["plain_sha256"]
            zipped = (HERE / row["gzip_name"]).read_bytes()
            assert len(zipped) == row["gzip_bytes"]
            assert digest(zipped) == row["gzip_sha256"]
            assert gzip.decompress(zipped) == raw
    return json.loads(raw), raw


def pointer(value, path):
    if not path:
        return value
    if not path.startswith("/"):
        raise ValueError("JSON pointer must start with /")
    for key in path.split("/")[1:]:
        key = key.replace("~1", "/").replace("~0", "~")
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="final-current-locator-facts.json")
    parser.add_argument("--pointer", default="")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--chars", type=int, default=15000)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    value, raw = read(args.file)
    value = pointer(value, args.pointer)
    if args.verify_only:
        print(json.dumps({"file": args.file, "plain_bytes": len(raw),
                          "plain_sha256": digest(raw), "pointer": args.pointer,
                          "pointer_exists": True, "complete_JSON_parse": True,
                          "qualification": "MECHANICAL_TRANSPORT_ONLY"}))
    else:
        text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
        print(text[args.start:args.start + args.chars], end="")
