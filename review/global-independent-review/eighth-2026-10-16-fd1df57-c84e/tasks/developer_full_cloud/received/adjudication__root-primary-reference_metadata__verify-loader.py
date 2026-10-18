"""Decode already inspected literal data only; never import or execute Ruby."""
from pathlib import Path
import hashlib
import json
import zlib

source = Path("/workspace/pokemon-essentials")
root = Path(__file__).resolve().parents[2]
expected = (root / "tasks/preflight_resources/current-serialized/Main.rb").read_bytes()
assert len(expected) == 1197
assert hashlib.sha256(expected).hexdigest() == "da24a2220936c6d44ddc60f180aed37beede022012d7addc99b5562ed07c52e1"
escapes = {"a": 7, "b": 8, "e": 27, "f": 12, "n": 10, "r": 13, "t": 9, "v": 11, "s": 32, "\\": 92, '"': 34}
rows = []
for filename in ["scripts_extract.rb", "scripts_combine.rb"]:
    line = (source / filename).read_text().splitlines()[69].strip()
    assert line.startswith('txt = "') and line.endswith('"')
    literal = line[len('txt = "'):-1]
    assert "#{" not in literal
    result = bytearray()
    i = 0
    while i < len(literal):
        char = literal[i]
        if char != "\\":
            assert ord(char) < 128
            result.append(ord(char))
            i += 1
            continue
        escape = literal[i + 1]
        if escape == "x":
            digits = literal[i + 2:i + 4]
            assert len(digits) == 2
            result.append(int(digits, 16))
            i += 4
        else:
            assert escape in escapes, "Unsupported escape: reject without Ruby execution"
            result.append(escapes[escape])
            i += 2
    decoded = zlib.decompress(bytes(result))
    assert decoded == expected
    rows.append({"source": filename, "literal_line": 70, "compressed_bytes": len(result), "compressed_sha256": hashlib.sha256(result).hexdigest(), "decoded_bytes": len(decoded), "decoded_sha256": hashlib.sha256(decoded).hexdigest(), "exact_current_loader_match": True})
serialized = (source / "Data/Scripts.rxdata").read_bytes()
assert hashlib.sha256(serialized).hexdigest() == "c5c0db0b1e0001c8e62db1a5a6079c342d7a8c1ca21dd45b3c8c7e92cf358fab"
assert zlib.decompress(serialized[29:590]) == expected
print(json.dumps({"static_literal_checks": rows, "current_serialized_payload": [29, 590], "source_or_target_execution": "NOT_EXECUTED", "scope": "Exact literal/decoded-byte equivalence only, no file writes or Ruby semantics execution"}))
