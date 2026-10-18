"""Capture a tool process with separate full outputs, UTC, and real exit code."""
from pathlib import Path
import datetime, json, subprocess, sys
ROOT=Path(__file__).resolve().parent
key=sys.argv[1]
if '/' in key or '..' in key: raise ValueError(key)
args=sys.argv[2:]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.run(args,cwd=ROOT,capture_output=True)
end=datetime.datetime.now(datetime.timezone.utc).isoformat()
base=ROOT/'evidence'/key
base.with_suffix('.stdout').write_bytes(p.stdout)
base.with_suffix('.stderr').write_bytes(p.stderr)
base.with_suffix('.json').write_text(json.dumps({'key':key,'argv':args,'cwd':str(ROOT),'start_utc':start,'end_utc':end,'exit':p.returncode,'stdout':str(base.with_suffix('.stdout')),'stderr':str(base.with_suffix('.stderr')),'qualification':'TOOL_VALIDATION unless a separately registered behavior observation says otherwise'},ensure_ascii=False,indent=2)+'\n')
sys.stdout.buffer.write(p.stdout)
sys.stderr.buffer.write(p.stderr)
sys.exit(p.returncode)
