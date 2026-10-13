# Read-only audit display helper; does not load or execute reference programs.
from pathlib import Path
import sys,json,csv
R=Path("/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/PBS")
def trainers(p):
 rows=[]; x=None
 for n,l in enumerate(p.read_text(encoding="utf-8-sig").splitlines(),1):
  if l.startswith("["): x={"section":l,"line":n}; rows.append(x)
  elif x is not None and "=" in l:
   k,v=l.split("=",1);x[k.strip()]=v.strip()
 return rows
def ranges(ns):
 if not ns:return "empty"
 a=b=ns[0]; out=[]
 for v in ns[1:]:
  if v==b+1:b=v
  else:out.append(str(a) if a==b else str(a)+".."+str(b));a=b=v
 out.append(str(a) if a==b else str(a)+".."+str(b));return ",".join(out)
files=sorted([p for p in R.glob("*trainers*.txt") if p.name.startswith(("cup_","battle_"))])
pool=[]
for p in files:
 for row in trainers(p):
  for k in ["BeginSpeech","EndSpeechWin","EndSpeechLose"]:
   v=row.get(k,"")
   if v not in pool:pool.append(v)
mode=sys.argv[1];start=int(sys.argv[3]) if len(sys.argv)>3 else 0;end=int(sys.argv[4]) if len(sys.argv)>4 else 999999
if mode=="texts":
 for i,t in enumerate(pool):
  if start<=i<end:print("S"+str(i)+" "+t)
else:
 p=R/sys.argv[2]
 if mode=="templates":
  rows=[(n,l) for n,l in enumerate(p.read_text(encoding="utf-8-sig").splitlines(),1) if l.strip() and not l.lstrip().startswith("#")]
  for i,(n,l) in enumerate(rows):
   if start<=i<end:print(str(i)+" L"+str(n)+" "+l)
 elif mode=="trainers":
  for i,x in enumerate(trainers(p)):
   if start<=i<end:
    ns=[int(n) for n in x.get("PokemonNos","").split(",") if n.strip()]
    print(str(i)+" L"+str(x["line"])+" "+x.get("Type","")+" "+x.get("Name","")+" texts="+"/".join("S"+str(pool.index(x.get(k,""))) for k in ["BeginSpeech","EndSpeechWin","EndSpeechLose"])+" roster="+ranges(ns))
