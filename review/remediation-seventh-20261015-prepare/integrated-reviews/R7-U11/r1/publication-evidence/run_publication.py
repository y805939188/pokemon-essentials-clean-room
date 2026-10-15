import sys,json,datetime,subprocess
from pathlib import Path
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
name=sys.argv[1]; cmd=sys.argv[2:]; out=Path("/workspace/r7-ir-R7-U11/publication-io");out.mkdir(exist_ok=True)
start=utc()
with (out/(name+".stdout")).open("xb") as so,(out/(name+".stderr")).open("xb") as se:
 p=subprocess.Popen(cmd,stdout=so,stderr=se);pid=p.pid;code=p.wait()
r={"argv":cmd,"pid":pid,"start_utc":start,"end_utc":utc(),"exit_code":code,"stdout":name+".stdout","stderr":name+".stderr","qualification":"Tool I/O only; not model configuration or behavior execution proof."}
(out/(name+".json")).write_text(json.dumps(r,indent=2)+"\n")
print(json.dumps(r));sys.exit(code)
