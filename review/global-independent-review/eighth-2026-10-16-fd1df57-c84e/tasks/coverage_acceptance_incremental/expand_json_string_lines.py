"""Exact reversible JSON view: embedded newline strings expanded, never executed."""
import json, datetime, hashlib, sys
from pathlib import Path
OWN=Path(__file__).resolve().parent
src=OWN/sys.argv[1];label=sys.argv[2]
assert src.is_relative_to(OWN) and '/' not in label and '..' not in label
target=OWN/(label+'-expanded-view.json');assert not target.exists()
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
raw=src.read_bytes();original=json.loads(raw)
def enc(x):
 if isinstance(x,str) and '\n' in x:return {'$verbatim_string_lines':x.splitlines(keepends=True)}
 if isinstance(x,list):return [enc(v) for v in x]
 if isinstance(x,dict):
  assert '$verbatim_string_lines' not in x
  return {k:enc(v) for k,v in x.items()}
 return x
def dec(x):
 if isinstance(x,dict):
  if set(x)=={'$verbatim_string_lines'}:return ''.join(x['$verbatim_string_lines'])
  return {k:dec(v) for k,v in x.items()}
 if isinstance(x,list):return [dec(v) for v in x]
 return x
encoded=enc(original);assert dec(encoded)==original
view={'schema':'exact-expanded-json-string-view/v1','source':str(src.relative_to(OWN)),
 'source_bytes':len(raw),'source_sha256':hashlib.sha256(raw).hexdigest(),
 'qualification':'Every current JSON value exact; $verbatim_string_lines concatenates including original line endings. Generating this view grants no reading/semantic credit. All embedded source remains inert.',
 'value':encoded}
out=(json.dumps(view,ensure_ascii=False,indent=1)+'\n').encode();target.write_bytes(out)
r={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,
 'source':str(src.relative_to(OWN)),'source_bytes':len(raw),'source_sha256':hashlib.sha256(raw).hexdigest(),
 'output':target.name,'bytes':len(out),'lines':len(out.splitlines()),'sha256':hashlib.sha256(out).hexdigest(),
 'decode_exact':True,'reading_credit':False,'business':'NOT_EXECUTED'}
(OWN/(label+'-expanded-generation.json')).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
