from pathlib import Path
import json,sys,hashlib,datetime,shlex
out=Path(__file__).resolve().parent
path=Path(sys.argv[1]); start=int(sys.argv[2]); end=int(sys.argv[3])
raw=path.read_bytes(); lines=raw.decode().splitlines(); end=min(end,len(lines))
with (out/"command-log.jsonl").open("a") as f:
 f.write(json.dumps({"command":shlex.join(["python3"]+sys.argv),"time":datetime.datetime.now(datetime.timezone.utc).isoformat(),"path":str(path),"start":start,"end":end,"sha256":hashlib.sha256(raw).hexdigest(),"operation":"read-emitted-not-yet-reviewed"})+"\n")
print("FILE "+str(path)+" TOTAL "+str(len(lines))+" READ "+str(start)+".."+str(end))
for n in range(start,end+1): print(str(n)+": "+lines[n-1])
