#!/usr/bin/env python3
"""Capture actual command output and exit independently, within this evidence dir."""
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

evidence = Path(__file__).resolve().parent
repo = evidence.parents[4]
name, *argv = sys.argv[1:]
if not name or '/' in name or not argv:
    raise SystemExit('usage: record-command.py simple-name argv...')
log = evidence / (name + '.json')
if log.exists():
    raise SystemExit('choose a new name; attempts are never overwritten')
start = datetime.now(timezone.utc).isoformat()
result = subprocess.run(argv, cwd=repo, capture_output=True, text=True)
payload = {'argv': argv, 'cwd': str(repo), 'utc_start': start,
           'utc_end': datetime.now(timezone.utc).isoformat(), 'exit': result.returncode,
           'stdout': result.stdout, 'stderr': result.stderr,
           'capture_runtime': sys.version, 'evidence_level': 'TOOL_VALIDATION',
           'reference_execution': False, 'host_execution': False}
log.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(payload, ensure_ascii=False))
raise SystemExit(result.returncode)
