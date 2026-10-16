"""Reversible lexical presentation of exact consecutive JSON pointer strings.
This is a text-only representation; it does not read target sources, decide
coverage, or turn pointers into semantic acceptance. Generation grants 0 reading.
"""
import datetime,hashlib,json,re,sys
from pathlib import Path
P=Path(__file__).resolve().parent
src=P/sys.argv[1];label=sys.argv[2]
assert src.resolve().is_relative_to(P) and re.fullmatch('[a-z0-9-]+',label)
begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
raw=src.read_bytes();original=json.loads(raw)
def encode(v):
 if isinstance(v,dict):
  assert '$exact_consecutive_pointer_strings' not in v
  return {k:encode(x) for k,x in v.items()}
 if isinstance(v,list):
  if len(v)>=3 and all(isinstance(x,str) for x in v):
   m=[re.fullmatch(r'(.*?/)([0-9]+)',x) for x in v]
   if all(m) and len({x[1] for x in m})==1:
    a=[int(x[2]) for x in m]
    if a==list(range(a[0],a[0]+len(a))) and v==[m[0][1]+str(x) for x in a]:
     return {'$exact_consecutive_pointer_strings':{'prefix':m[0][1],'inclusive_first_integer':a[0],'inclusive_last_integer':a[-1],'qualification':'Exact ordered locator strings only; no source records or semantic facts read by this representation.'}}
  return [encode(x) for x in v]
 return v
def decode(v):
 if isinstance(v,dict):
  if set(v)=={'$exact_consecutive_pointer_strings'}:
   a=v['$exact_consecutive_pointer_strings'];return [a['prefix']+str(i) for i in range(a['inclusive_first_integer'],a['inclusive_last_integer']+1)]
  return {k:decode(x) for k,x in v.items()}
 if isinstance(v,list):return [decode(x) for x in v]
 return v
encoded=encode(original);assert decode(encoded)==original
out=P/(label+'-pointer-view.json');assert not out.exists()
data=(json.dumps(encoded,ensure_ascii=False,indent=2)+'\n').encode();out.write_bytes(data)
r={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input':str(src.relative_to(P)),'input_bytes':len(raw),'input_sha256':hashlib.sha256(raw).hexdigest(),'output':out.name,'output_bytes':len(data),'output_lines':len(data.splitlines()),'output_sha256':hashlib.sha256(data).hexdigest(),'exact_decode_equals_input':True,'generation_reading_credit':0,'exit_code':0}
(P/(label+'-pointer-generation.json')).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
