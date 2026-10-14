import sys,json,subprocess,hashlib,datetime,urllib.request,urllib.parse,traceback
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=D.parents[3]
PRE=D.parents[1]
def identity(b):
 return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"git_blob":hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()}
t0=datetime.datetime.now(datetime.timezone.utc).isoformat()
a=sys.argv[1:];kind=a[0];path=a[1];start=int(a[2]) if len(a)>2 else 1;end=int(a[3]) if len(a)>3 else None
commit="64c77cf1733ab7db300e9f5ac7c79a2886c8ac68"
try:
 if kind=="source":
  commit="8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
  ix=json.loads((PRE/"inputs/frozen-inputs.json").read_text())
  row=next(x for x in ix["source_materials"] if x["path"]==path)
  url="https://raw.githubusercontent.com/Maruno17/pokemon-essentials/"+commit+"/"+urllib.parse.quote(path)
  with urllib.request.urlopen(url,timeout=30) as r: b=r.read()
  assert all(identity(b)[k]==row[k] for k in identity(b))
 elif kind=="formal":
  commit="8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
  b=subprocess.check_output(["git","show",commit+":"+path],cwd=ROOT)
 elif kind=="candidate":
  path=str((PRE/"candidates/R6-U05/mirror"/path).relative_to(ROOT)); b=subprocess.check_output(["git","show",commit+":"+path],cwd=ROOT)
 elif kind=="evidence":
  path=str((PRE/"inputs/evidence"/path).relative_to(ROOT)); b=subprocess.check_output(["git","show",commit+":"+path],cwd=ROOT)
 elif kind=="git":
  commit,path=path.split(":",1);b=subprocess.check_output(["git","show",commit+":"+path],cwd=ROOT)
 else:
  b=(ROOT/path).read_bytes()
 lines=b.decode().splitlines();end=end or len(lines)
 assert 1<=start<=end<=len(lines),(start,end,len(lines))
 stdout=kind+" "+commit+" "+path+" "+str(start)+"-"+str(end)+"/"+str(len(lines))+"\n"+"\n".join(str(i)+": "+lines[i-1] for i in range(start,end+1))+"\n"
 rec={"utc_start":t0,"utc_end":datetime.datetime.now(datetime.timezone.utc).isoformat(),"cwd":str(ROOT),"argv":sys.argv,"kind":kind,"path":path,"commit":commit,"identity":identity(b),"line_count":len(lines),"read_range":[start,end],"level":"SOURCE_STATIC","exit":0,"stderr":"","stdout":stdout}
 with (D/"reading-ledger.jsonl").open("a") as f:f.write(json.dumps(rec,ensure_ascii=False)+"\n")
 print(stdout,end="")
except Exception:
 err=traceback.format_exc();rec={"utc_start":t0,"utc_end":datetime.datetime.now(datetime.timezone.utc).isoformat(),"cwd":str(ROOT),"argv":sys.argv,"kind":kind,"path":path,"commit":commit,"exit":1,"stderr":err}
 with (D/"reading-ledger.jsonl").open("a") as f:f.write(json.dumps(rec,ensure_ascii=False)+"\n")
 raise
