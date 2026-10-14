#!/usr/bin/env python3
"""Finite read/identity evidence; lossless JSON anchor display, never execute input."""
import sys, json, hashlib, re, subprocess
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[3]
EVIDENCE=Path(__file__).resolve().parent
start=datetime.now(timezone.utc).isoformat()
mode=sys.argv[1]
p=Path(sys.argv[2]).resolve()
b=p.read_bytes()
identity={"path":str(p),"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"git_blob":hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()}
if mode=="json":
    obj=json.loads(b)
    for key in sys.argv[3:]:
        obj=obj[int(key)] if isinstance(obj,list) else obj[key]
    memo={};definitions={}
    def pack(v):
        if isinstance(v,dict):
            key=json.dumps(v,sort_keys=True,ensure_ascii=False)
            if len(key)>150:
                if key in memo:return {"$read_anchor":memo[key]}
                a="A"+str(len(memo));memo[key]=a
                definitions[a]={k:pack(x) for k,x in v.items()}
                return {"$read_anchor":a}
            return {k:pack(x) for k,x in v.items()}
        if isinstance(v,list):return [pack(x) for x in v]
        return v
    result=pack(obj)
    out=json.dumps({"root":result,"definitions":definitions},ensure_ascii=False)
    scope={"json_path":sys.argv[3:],"representation":"lossless exact object anchors; all values displayed"}
else:
    lines=b.decode().splitlines(); a=int(sys.argv[3]);z=int(sys.argv[4]);assert 1<=a<=z<=len(lines)
    out="\n".join(str(i)+" "+lines[i-1] for i in range(a,z+1))
    scope={"lines":[a,z],"total_lines":len(lines)}
log={"argv":sys.argv,"cwd":str(Path.cwd()),"utc_start":start,"utc_end":datetime.now(timezone.utc).isoformat(),"identity":identity,"scope":scope,"stdout_bytes":len(out.encode()),"stdout_sha256":hashlib.sha256(out.encode()).hexdigest(),"stderr":"","exit_code":0,"level":"SOURCE_STATIC_READ_DISPLAY; semantic review by author after complete untruncated tool output"}
with (EVIDENCE/"read-journal.jsonl").open("a") as f:f.write(json.dumps(log,ensure_ascii=False)+"\n")
print(out)
