from pathlib import Path
import sys,json,hashlib
r=Path(__file__).parent
p=Path(sys.argv[1]);a=int(sys.argv[2]);ls=p.read_text().splitlines();b=min(int(sys.argv[3]),len(ls));name=sys.argv[4]
out="\n".join(f"{i}: {ls[i-1]}" for i in range(a,b+1))+"\n"
(r/"logs"/name).write_text(out)
with (r/"logs/reading-ledger.jsonl").open("a") as f:f.write(json.dumps({"phase":"displayed","path":str(p),"start":a,"end":b,"total":len(ls),"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"log":name,"semantic_pass":False})+"\n")
print(out,end="")
