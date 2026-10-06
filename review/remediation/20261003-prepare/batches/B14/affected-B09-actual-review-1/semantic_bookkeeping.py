import sys,json,pathlib,hashlib
from read_bookkeeping import get,ACT,PRE,record
D=pathlib.Path(__file__).parent
ORIG="93e10babe0b9c9ef8b3f5277754541b447beeeb4";PLAN="41fffb540c6483f5296ea0d33b789b75180d27ed"
def inputs(mode):
 root="review/remediation/20261003-prepare/batches/"
 ids=set(x["id"] for x in json.loads(get(ACT,root+"B14/integration-stage-1/finding-registration.json"))["dispositions"])
 ids.update(x["id"] for x in json.loads(get(PRE,root+"B09/integration-stage-1/finding-registration.json"))["dispositions"])
 if mode=="controls":
  p="review/global-independent-review/2026-10-03-fd82a639/findings.json";o=json.loads(get(ORIG,p));yield ORIG,p,{str(i):v for i,v in enumerate(o) if v["id"] in ids}
  p="review/remediation-20261003-prepare/finding-acceptance.json";o=json.loads(get(PLAN,p));yield PLAN,p,{k:v for k,v in o.items() if k in ids}
 elif mode=="owner":
  for fn in ["finding-registration.json","current-readers.json","integration-manifest.json"]:
   p=root+"B09/integration-stage-1/"+fn;yield PRE,p,json.loads(get(PRE,p))
 elif mode=="registration":
  for fn in ["finding-registration.json","current-readers.json","clause-location-bindings.json","pre-freeze-navigation-correction.json","boundary-and-bindings.json","scope-and-observation-registration.json"]:
   p=root+"B14/integration-stage-1/"+fn;yield ACT,p,json.loads(get(ACT,p))
def pool(mode):
 seen={};values=[];maps=[]
 if mode!="controls":
  for seedmode in (["controls"] if mode=="owner" else ["controls","owner"]):
   seedvals,_=pool(seedmode)
   for entry in seedvals:
    h=hashlib.sha256(json.dumps(entry["value"],ensure_ascii=False,separators=(",",":")).encode()).hexdigest()
    if h not in seen:
     seen[h]=len(values);values.append({**entry,"n":len(values),"seed_mode":seedmode})
 seed_end=len(values)
 def walk(x,ptr,c,p):
  if isinstance(x,dict):return {k:walk(v,ptr+"/"+k.replace("~","~0").replace("/","~1"),c,p) for k,v in x.items()}
  if isinstance(x,list):return [walk(v,ptr+"/"+str(i),c,p) for i,v in enumerate(x)]
  s=json.dumps(x,ensure_ascii=False,separators=(",",":"));h=hashlib.sha256(s.encode()).hexdigest()
  if h not in seen:
   seen[h]=len(values);values.append({"n":len(values),"commit":c,"path":p,"pointer":ptr,"value":x})
  return {"exact_value":seen[h],"value_sha256":h}
 for c,p,o in inputs(mode):maps.append({"commit":c,"path":p,"structure":walk(o,"",c,p)})
 return values,maps
if __name__=="__main__":
 mode=sys.argv[1];vals,maps=pool(mode)
 if len(sys.argv)==2:
  (D/(mode+"-lossless-map.json")).write_text(json.dumps({"rule":"Every object/list member and order retained; values reside at exact external first-occurrence selectors. Identity bookkeeping alone is not semantic reading.","structures":maps,"unique_values":[{k:v for k,v in x.items() if k!="value"} for x in vals]},ensure_ascii=False,indent=2)+"\n")
  print(mode,"seed_end",sum(1 for x in vals if "seed_mode" in x),"unique",len(vals),"valuechars",sum(len(json.dumps(x["value"],ensure_ascii=False)) for x in vals))
 else:
  a=int(sys.argv[2]);z=int(sys.argv[3]);out=vals[a:z]
  for x in out:print(str(x["n"])+" "+x["path"].rsplit("/",1)[-1]+x["pointer"]+" = "+json.dumps(x["value"],ensure_ascii=False))
  record({"semantic_mode":mode,"unique_value_start":a,"unique_value_end_exclusive":min(z,len(vals)),"delivery":"DISPLAYED; semantic reading assessed separately"})
