"""Capture exact argv and independent exit status for bounded author tools."""
from pathlib import Path
import datetime
import json
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[5]
OUT=Path(__file__).resolve().parent
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
result=subprocess.run(sys.argv[1:],cwd=ROOT,capture_output=True)
record=dict(argv=sys.argv[1:],cwd=str(ROOT),utc_start=start,
            capture_runtime=sys.version,
            utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            stdout=result.stdout.decode(),stderr=result.stderr.decode(),exit_code=result.returncode,
            evidence_level='TOOL_VALIDATION_OR_GIT_OPERATION; not gameplay execution')
with (OUT/'tool-attempts.jsonl').open('a') as stream:stream.write(json.dumps(record,ensure_ascii=False)+'\n')
print(json.dumps(record,ensure_ascii=False))
sys.exit(result.returncode)
