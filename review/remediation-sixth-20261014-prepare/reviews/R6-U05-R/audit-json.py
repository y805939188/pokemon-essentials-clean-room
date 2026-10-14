import sys,json,hashlib,datetime
from pathlib import Path
D=Path(__file__).resolve().parent; ROOT=D.parents[3]
p=ROOT/sys.argv[1];a=int(sys.argv[2]);z=int(sys.argv[3]);b=p.read_bytes();x=json.loads(b);s=json.dumps(x,ensure_ascii=False,separators=(",",":"))
assert 0<=a<z<=len(s),(a,z,len(s))
out=s[a:z]
rec={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"cwd":str(ROOT),"argv":sys.argv,"path":str(p.relative_to(ROOT)),"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"representation":"complete parsed JSON compact UTF8, no fields removed","character_range":[a,z],"representation_characters":len(s),"stdout":out,"stderr":"","exit":0,"level":"SOURCE_STATIC_STRUCTURED_INPUT"}
with (D/"structured-reading.jsonl").open("a") as f:f.write(json.dumps(rec,ensure_ascii=False)+"\n")
print(out)
