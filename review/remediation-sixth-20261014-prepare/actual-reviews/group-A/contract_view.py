import json,sys
from pathlib import Path
d=json.loads(Path("review/remediation-sixth-20261014-prepare/contracts/R6-"+sys.argv[1]+".json").read_text());identities=[]
def dedup(x):
 if isinstance(x,list):return [dedup(v) for v in x]
 if not isinstance(x,dict):return x
 y={}
 for k,v in x.items():
  if k=="payload_identity":
   if v not in identities:identities.append(v)
   y[k]={"exact_identity_table_index":identities.index(v)}
  else:y[k]=dedup(v)
 return y
view=dedup(d)
if sys.argv[2]=="meta":
 del view["scope_contracts"];view["exact_identity_table"]=identities
else:view=view["scope_contracts"][int(sys.argv[2])]
print(json.dumps(view,ensure_ascii=False,indent=1))
