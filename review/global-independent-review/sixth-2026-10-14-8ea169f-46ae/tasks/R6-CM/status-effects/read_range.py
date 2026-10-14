import sys,json,hashlib,subprocess
from pathlib import Path
p=Path(sys.argv[1]); a=int(sys.argv[2]); b=int(sys.argv[3]); raw=p.read_bytes(); lines=raw.decode().splitlines(); b=min(b,len(lines))
base=Path(__file__).parent
identity={"agent":"/root/cm_status_effects","requested_model":"gpt-6.1-sol","requested_effort":"ultra","actual_model":"UNVERIFIED","actual_effort":"UNVERIFIED","actual_tier":"UNVERIFIED","actual_speed":"UNVERIFIED","actual_uuid":"UNVERIFIED"}
r={"path":str(p),"range_start":a,"range_end":b,"total_lines":len(lines),"sha256":hashlib.sha256(raw).hexdigest(),"evidence":"static_full_text_range","reader":identity}
with (base/"reading-ledger.jsonl").open("a") as f:f.write(json.dumps(r)+"\n")
print(json.dumps(r))
for n in range(a,b+1):print(f"{n:5} {lines[n-1]}")
