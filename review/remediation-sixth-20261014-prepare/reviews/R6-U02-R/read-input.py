#!/usr/bin/env python3
"""Bounded read-only input viewer; writes only a metadata receipt in this directory."""
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
OWN = Path(__file__).resolve().parent
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
mode, target, first, last = sys.argv[1:5]
first, last = int(first), int(last)
command = ["git", "show", target] if mode == "git" else None
if mode == "pair":
    baseline = subprocess.check_output(["git", "show", "8ea169fbd0f33f378b5d732fd6bea59e854e04a6:" + target], cwd=ROOT)
    candidate_path = "review/remediation-sixth-20261014-prepare/candidates/R6-U02/mirror/" + target
    candidate = (ROOT / candidate_path).read_bytes()
    before, after = baseline.decode().splitlines(), candidate.decode().splitlines()
    assert 1 <= first <= last <= len(after)
    print(f"PAIRED FULL-TEXT READ {target} C{first}-{last}/{len(after)} Btotal={len(before)}")
    covered = []
    for kind, b1, b2, c1, c2 in difflib.SequenceMatcher(None, before, after, autojunk=False).get_opcodes():
        if kind == "equal":
            for c in range(max(c1, first-1), min(c2, last)):
                b = b1 + c - c1
                print(f"B{b+1}/C{c+1}: {after[c]}")
                covered.append(b+1)
        elif c1 < last and c2 >= first-1:
            for b in range(b1, b2):
                print(f"B{b+1} removed/replaced: {before[b]}")
                covered.append(b+1)
            for c in range(max(c1, first-1), min(c2, last)):
                print(f"C{c+1} added/replaced: {after[c]}")
    receipts = []
    for role, content, name, span, n in [("baseline",baseline,target,[min(covered),max(covered)],len(before)),("candidate",candidate,candidate_path,[first,last],len(after))]:
        receipts.append({"argv":sys.argv,"cwd":str(ROOT),"UTC_start":start,"UTC_end":datetime.datetime.now(datetime.timezone.utc).isoformat(),"runtime":sys.version,"mode":mode,"role":role,"input":name,"range":span,"total_lines":n,"bytes":len(content),"sha256":hashlib.sha256(content).hexdigest(),"git_blob":hashlib.sha1(f"blob {len(content)}\0".encode()+content).hexdigest(),"exit":0,"stderr":"","level":"PAIRED_STATIC_FULL_TEXT_READ","semantic_review":"Both payloads expanded in order; common exact lines printed once with both coordinates. Not behavior execution."})
    with (OWN / "reading-receipts.jsonl").open("a") as stream:
        for receipt in receipts:
            stream.write(json.dumps(receipt,ensure_ascii=False)+"\n")
    sys.exit(0)
if command:
    proc = subprocess.run(command, cwd=ROOT, capture_output=True)
    content, error, code = proc.stdout, proc.stderr.decode(), proc.returncode
else:
    content, error, code = (ROOT / target).read_bytes(), "", 0
lines = content.decode().splitlines()
if code or first < 1 or last > len(lines) or last < first:
    raise RuntimeError((code, error, first, last, len(lines)))
print(f"INPUT {target} LINES {first}-{last}/{len(lines)}")
for i in range(first - 1, last):
    print(f"{i+1}: {lines[i]}")
blob = hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest()
receipt = {"argv": sys.argv, "cwd": str(ROOT), "UTC_start": start,
           "UTC_end": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "runtime": sys.version, "mode": mode, "input": target,
           "range": [first, last], "total_lines": len(lines),
           "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest(),
           "git_blob": blob, "exit": code, "stderr": error,
           "level": "SOURCE_STATIC_READ_OUTPUT", "semantic_review": "human assessment follows output; receipt alone is not PASS"}
with (OWN / "reading-receipts.jsonl").open("a") as stream:
    stream.write(json.dumps(receipt, ensure_ascii=False) + "\n")
