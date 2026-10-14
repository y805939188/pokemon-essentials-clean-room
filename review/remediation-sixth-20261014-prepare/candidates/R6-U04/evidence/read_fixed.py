#!/usr/bin/env python3
"""Read fixed blobs, record actual intervals; no reference execution."""
from pathlib import Path
import subprocess,json,hashlib,sys,datetime
root=Path(__file__).resolve().parents[5]
ev=Path(__file__).resolve().parent
kind,path,lo,hi=sys.argv[1:]
lo,hi=int(lo),int(hi)
commit="8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b" if kind=="source" else "8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
repo="/tmp/r6-u04-reference-objects" if kind=="source" else str(root)
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
argv=["git","-C",repo,"cat-file","blob",commit+":"+path]
x=subprocess.run(argv,capture_output=True)
assert x.returncode==0,x.stderr
b=x.stdout;lines=b.decode("utf-8-sig").splitlines()
hi=len(lines) if hi==0 else hi
assert 1<=lo<=hi<=len(lines),(path,lo,hi,len(lines))
output="\n".join(f"{i}: {lines[i-1]}" for i in range(lo,hi+1))
mode=subprocess.check_output(["git","-C",repo,"ls-tree",commit,"--",path],text=True).strip()
row={"kind":kind,"path":path,"commit":commit,"git_tree_entry":mode,"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"git_blob":hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest(),"lines":len(lines),"read_interval":[lo,hi],"argv":argv,"cwd":str(Path.cwd()),"utc_start":start,"utc_end":datetime.datetime.now(datetime.timezone.utc).isoformat(),"exit":x.returncode,"stderr":x.stderr.decode(),"display_sha256":hashlib.sha256(output.encode()).hexdigest(),"evidence_level":"SOURCE_STATIC","reference_execution":False}
with (ev/"new-reading-ledger.jsonl").open("a") as f:f.write(json.dumps(row,ensure_ascii=False)+"\n")
print(f"FILE {kind} {path} [{lo},{hi}] / {len(lines)}");print(output)
