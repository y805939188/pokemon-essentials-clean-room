import subprocess,sys,json,pathlib,hashlib
D=pathlib.Path(__file__).parent
ACT="d48197f365c39925f795c1d325988c0d74e59979"
PRE="1e6b11a47370f1c7c4659a32443fc1afda597bac"
REF="8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
REFDIR=str(pathlib.Path.cwd().parent / "pokemon-framework-reference" / "reference" / "pokemon-essentials")
def get(c,p,reference=False):
 cmd=["git"]+(["-C",REFDIR] if reference else [])+["show",c+":"+p]
 return subprocess.check_output(cmd)
def record(entry):
 with (D/"display-receipts.jsonl").open("a") as f:f.write(json.dumps(entry,ensure_ascii=False)+"\n")
def display(c,p,start,end,reference=False):
 b=get(c,p,reference);ls=b.decode().splitlines();end=min(end,len(ls))
 out="\n".join(str(i+1)+": "+ls[i] for i in range(start-1,end))
 print(p,c,"range",start,end,"total",len(ls));print(out)
 record({"commit":c,"path":p,"repository":"reference" if reference else "project","sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b),"line_start":start,"line_end":end,"total_lines":len(ls),"delivery":"DISPLAYED; human semantic assessment separate"})
if __name__=="__main__":display(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),len(sys.argv)>5)
