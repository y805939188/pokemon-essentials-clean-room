import json,hashlib,runpy
from pathlib import Path
M=runpy.run_path(str(Path(__file__).parent/'read_projection.py'));ROWS=M['ROWS']
SOURCE=json.load(open(ROWS[27]['local_path']))
READ_RECORDS=json.load(open(Path(__file__).parent/'reading-ledger.json'))['records']
READ_PATHS={r['path'] for r in READ_RECORDS}
ACTUALLY_READ_SOURCE_INDICES=[i for i,r in enumerate(ROWS) if r['path'] in READ_PATHS and r['path'].endswith('.json')]
KNOWN={}
def encoded(x):return json.dumps(x,ensure_ascii=False,separators=(',',':')).encode()
def register(x,pointer):
 if isinstance(x,(dict,list,str)):
  b=encoded(x)
  if len(b)>160:KNOWN.setdefault(b,pointer)
  if isinstance(x,dict):
   for k,v in x.items():register(v,pointer+'/'+k.replace('~','~0').replace('/','~1'))
  elif isinstance(x,list):
   for i,v in enumerate(x):register(v,pointer+'/'+str(i))
for i in ACTUALLY_READ_SOURCE_INDICES:register(json.load(open(ROWS[i]['local_path'])),'payload'+str(i)+'#')
def assoc(x,pointer='',receipts=None):
 if isinstance(x,(dict,list,str)):
  b=encoded(x)
  if b in KNOWN:
   row={'from':pointer,'to':KNOWN[b],'canonical_bytes':len(b),'canonical_sha256':hashlib.sha256(b).hexdigest(),'credit':'This context already actually read same complete semantic values at the exact target pointer; raw whitespace identity not claimed'}
   if receipts is not None:receipts.append(row)
   return {'_already_read_this_context_same_values':KNOWN[b]}
  if isinstance(x,dict):return {k:assoc(v,pointer+'/'+k,receipts) for k,v in x.items()}
  if isinstance(x,list):return [assoc(v,pointer+'/'+str(i),receipts) for i,v in enumerate(x)]
 return x
