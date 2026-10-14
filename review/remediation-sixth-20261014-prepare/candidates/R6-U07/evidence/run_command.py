#!/usr/bin/env python3
"""Capture each explicit tool subprocess independently, without shell evaluation."""
import sys, subprocess, json
from pathlib import Path
from datetime import datetime, timezone

out = Path(__file__).resolve().parent
name = sys.argv[1]
assert name.replace('-', '').replace('_', '').isalnum()
assert not (out / (name + '.json')).exists(), 'Do not overwrite a recorded attempt'
argv = sys.argv[2:]
start = datetime.now(timezone.utc).isoformat()
p = subprocess.run(argv, capture_output=True, cwd=Path.cwd())
(out / (name + '.stdout')).write_bytes(p.stdout)
(out / (name + '.stderr')).write_bytes(p.stderr)
row = {'argv': argv, 'cwd': str(Path.cwd()), 'utc_start': start,
       'utc_end': datetime.now(timezone.utc).isoformat(), 'exit_code': p.returncode,
       'stdout': name + '.stdout', 'stderr': name + '.stderr',
       'runtime_driver': sys.version, 'platform_identity': 'UNVERIFIED'}
(out / (name + '.json')).write_text(json.dumps(row, ensure_ascii=False, indent=2)+'\n')
print(p.stdout.decode(errors='replace'), end='')
print(p.stderr.decode(errors='replace'), end='', file=sys.stderr)
print(json.dumps(row, ensure_ascii=False))
sys.exit(p.returncode)
