import json,datetime,hashlib,sys
from pathlib import Path
b=Path(__file__).resolve().parent
relative,label=sys.argv[1:];src=b/relative;assert src.resolve().is_relative_to(b) and '/' not in label and label.replace('-','').isalnum()
start=datetime.datetime.now(datetime.timezone.utc).isoformat();raw=src.read_bytes();j=json.loads(raw)
def emit(v,depth=0,compact_rows=False):
 sp=' '*depth
 if isinstance(v,dict):
  if not v:return '{}'
  return '{\n'+',\n'.join(' '*(depth+1)+json.dumps(k,ensure_ascii=False)+': '+emit(x,depth+1,k=='rows_in_original_order') for k,x in v.items())+'\n'+sp+'}'
 if isinstance(v,list):
  if not v:return '[]'
  if compact_rows:return '[\n'+',\n'.join(' '*(depth+1)+json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in v)+'\n'+sp+']'
  if all(not isinstance(x,(dict,list)) for x in v):return json.dumps(v,ensure_ascii=False)
  return '[\n'+',\n'.join(' '*(depth+1)+emit(x,depth+1) for x in v)+'\n'+sp+']'
 return json.dumps(v,ensure_ascii=False)
text=emit(j)+'\n';assert json.loads(text)==j
out=b/(label+'-compact-view.json');assert not out.exists();out.write_text(text)
p={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'input':relative,'input_bytes':len(raw),'input_sha256':hashlib.sha256(raw).hexdigest(),'output':out.name,'output_bytes':len(text.encode()),'output_sha256':hashlib.sha256(text.encode()).hexdigest(),'output_lines':len(text.splitlines()),'all_JSON_values_identical':True,'generation_semantic_reading_credit':0}
(b/(label+'-compact-generation.json')).write_text(json.dumps(p,indent=2)+'\n');print(json.dumps(p))
