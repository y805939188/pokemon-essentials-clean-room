#!/usr/bin/env python3
"""Capture a task command with separate stdout/stderr and its own exit status."""
import datetime
import json
import subprocess
import sys
from pathlib import Path

evidence = Path(__file__).resolve().parent
stem, *argv = sys.argv[1:]
assert '/' not in stem and argv
logs = evidence / 'commands'
logs.mkdir(exist_ok=True)
receipt = logs / (stem + '.json')
assert not receipt.exists(), 'Keep prior attempts; use a new stem.'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
p = subprocess.run(argv, capture_output=True)
(logs / (stem + '.stdout')).write_bytes(p.stdout)
(logs / (stem + '.stderr')).write_bytes(p.stderr)
row = dict(argv=argv, cwd=str(Path.cwd()), started_utc=started,
           ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), exit=p.returncode,
           stdout=str(logs / (stem + '.stdout')), stderr=str(logs / (stem + '.stderr')))
receipt.write_text(json.dumps(row, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(row, ensure_ascii=False))
print(p.stdout.decode(errors='replace'), end='')
print(p.stderr.decode(errors='replace'), file=sys.stderr, end='')
sys.exit(p.returncode)
