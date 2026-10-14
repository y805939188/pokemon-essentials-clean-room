from pathlib import Path
import sys,json,hashlib,datetime
ROOT=Path("/Users/dingshinn/Desktop/pokemon-framework-reference")
OUT=ROOT/"review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-DX/compiler"
p=ROOT/sys.argv[1]; start=int(sys.argv[2]); end=int(sys.argv[3]); lines=p.read_text().splitlines()
if not 1 <= start <= end <= len(lines): raise ValueError("Invalid complete range")
entry={"path":str(p.relative_to(ROOT)),"start":start,"end":end,"file_lines":len(lines),"file_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"read_kind":"tool_display_full_contiguous_range","semantic_status":"PENDING_AGENT_REASONING","utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}
with (OUT/"reading-ledger.jsonl").open("a") as f: f.write(json.dumps(entry,ensure_ascii=False)+"\n")
display="\n".join(f"{i}: {lines[i-1]}" for i in range(start,end+1))
with (OUT/"logs"/(str(p.relative_to(ROOT)).replace("/","__")+f".{start}-{end}.txt")).open("w") as f:f.write(display+"\n")
print(display)
