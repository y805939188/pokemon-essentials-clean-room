"""Read new mechanical evidence from plain JSON or its exact gzip transport.

Reads only; no FULL/semantic/acceptance credit. Examples:
  python3 final-mechanical-read.py --verify-only
  python3 final-mechanical-read.py --pointer /checks --chars 15000
  python3 final-mechanical-read.py --pointer /old_U06_root_twelve_identity_reuse
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--file", default="final-mechanical.json")
p.add_argument("--pointer", default="")
p.add_argument("--start", type=int, default=0)
p.add_argument("--chars", type=int, default=15000)
p.add_argument("--verify-only", action="store_true")
a = p.parse_args()
logical = (HERE / a.file).resolve()
if not logical.is_relative_to(HERE):
    raise ValueError("Only this new review output directory can be read by --file")
transport = logical if logical.exists() else Path(str(logical) + ".gz")
raw_transport = transport.read_bytes()
raw = raw_transport if logical.exists() else gzip.decompress(raw_transport)
digest = hashlib.sha256(raw).hexdigest()
mapping_path = HERE / "final-mechanical-compression.json"
mapping = json.loads(mapping_path.read_text())
entry = next(x for x in mapping["files"] if x["logical_plain_name"] == logical.name)
assert len(raw) == entry["plain_bytes"] and digest == entry["plain_sha256"]
if not logical.exists():
    assert hashlib.sha256(raw_transport).hexdigest() == entry["gzip_sha256"]
    assert len(raw_transport) == entry["gzip_bytes"]
value = json.loads(raw)
if a.pointer:
    if not a.pointer.startswith("/"):
        raise ValueError("--pointer must be empty or an RFC6901 pointer")
    for part in a.pointer[1:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
if a.verify_only:
    print(json.dumps({"logical_file": logical.name, "transport": transport.name,
                      "plain_bytes": len(raw), "plain_sha256": digest,
                      "exact_decompression_verified": True,
                      "credit": "mechanical transport only; no semantic reading"}, ensure_ascii=False))
else:
    rendered = json.dumps(value, ensure_ascii=False, indent=2)
    if not 0 <= a.start <= len(rendered):
        raise ValueError("--start outside the rendered value")
    end = len(rendered) if a.chars == 0 else min(len(rendered), a.start + a.chars)
    print(json.dumps({"logical_file": logical.name, "transport": transport.name,
                      "pointer": a.pointer, "start": a.start, "end_exclusive": end,
                      "total_chars": len(rendered), "next_start": end if end < len(rendered) else None,
                      "render_sha256": hashlib.sha256(rendered.encode()).hexdigest(),
                      "credit": "navigation only; no FULL/semantic verdict"}, ensure_ascii=False))
    print(rendered[a.start:end])
