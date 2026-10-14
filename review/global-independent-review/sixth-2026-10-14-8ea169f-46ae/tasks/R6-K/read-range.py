from pathlib import Path
import sys,json,datetime,hashlib
root=Path(__file__).parent
p=Path(sys.argv[1]); start=int(sys.argv[2]); end=int(sys.argv[3]); seq=sys.argv[4]
lines=p.read_text().splitlines(); end=min(end,len(lines))
out="PATH "+str(p)+" RANGE "+str(start)+"-"+str(end)+" TOTAL "+str(len(lines))+"\n"+"\n".join(str(i)+"\t"+lines[i-1] for i in range(start,end+1))+"\n"
(root/"logs"/(seq+".txt")).write_text(out)
with (root/"logs"/"commands.jsonl").open("a") as f: f.write(json.dumps({"argv":sys.argv,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"timestamp":datetime.datetime.now(datetime.timezone.utc).isoformat(),"exit_code":0,"log":seq+".txt"})+"\n")
print(out,end="")
