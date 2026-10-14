"""Capture an explicit command; output files stay in this review directory."""
import datetime, json, subprocess, sys
from pathlib import Path
D = Path(__file__).resolve().parent
ROOT = D.parents[3]
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
name, *argv = sys.argv[1:]
assert name and "/" not in name
t0 = now()
p = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
record = {"utc_start":t0,"utc_end":now(),"cwd":str(ROOT),"argv":argv,
          "stdout":p.stdout,"stderr":p.stderr,"independent_exit_code":p.returncode,
          "actual_platform_model_effort_tier_speed_UUID":"UNVERIFIED"}
(D / "commands").mkdir(exist_ok=True)
(D / "commands" / (name+".json")).write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
print(p.stdout, end="")
print(p.stderr, end="", file=sys.stderr)
sys.exit(p.returncode)
