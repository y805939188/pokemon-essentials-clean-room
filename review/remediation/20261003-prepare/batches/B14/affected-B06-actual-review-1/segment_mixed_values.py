"""Lossless document-string segmentation: never discard mixed substantive prose."""
import sys;sys.dont_write_bytecode=True
import pathlib,json,re,hashlib,importlib.util
D=pathlib.Path(__file__).parent
spec=importlib.util.spec_from_file_location('r',D/'read_documents.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
values=json.loads((D/'reading-values.json').read_text());lookup={};native={}
def scalar(x):
 v=m.document_value(x['first'][0])
 for k in x['first'][1]:v=v[k]
 if 'segment' in x:v=v[x['segment'][0]:x['segment'][1]]
 return v
for x in values:
 v=scalar(x);key=(type(v).__name__,json.dumps(v,ensure_ascii=False,separators=(',',':')));lookup[key]=x['id']
original_total=len(values);maps=[]
pattern=re.compile(r'(?<![A-Za-z0-9_/])(?:deliverables/|review/|specs/|audit/|planning/|batches/)[A-Za-z0-9_./\-]+\.(?:md|jsonl|json|tsv|py|patch|diff|txt)(?:#[A-Za-z0-9_./\-]+)?')
for x in values[:original_total]:
 if x['class']!='semantic' or x['id']<44788 or 273749<=x['id']<274421:continue
 v=scalar(x);matches=list(pattern.finditer(v))
 if not matches:continue
 parts=[];pos=0
 for match in matches:
  if match.start()>pos:parts.append((pos,match.start(),'prose'))
  parts.append((match.start(),match.end(),'logical_path_identity'));pos=match.end()
 if pos<len(v):parts.append((pos,len(v),'prose'))
 seg=[]
 for a,b,role in parts:
  s=v[a:b];key=('str',json.dumps(s,ensure_ascii=False,separators=(',',':')))
  if key not in lookup:
   vi=len(values);lookup[key]=vi;values.append({'id':vi,'type':'str','sha256':hashlib.sha256(key[1].encode()).hexdigest(),'first':x['first'],'segment':[a,b],'parent_value':x['id'],'characters':len(s),'class':'identity_or_numeric' if role=='logical_path_identity' or not s.strip() or m.pure(s.strip()) else 'semantic'})
  seg.append({'start':a,'end':b,'role':role,'value_id':lookup[key]})
 assert ''.join(v[p['start']:p['end']] for p in seg)==v
 maps.append({'parent_value_id':x['id'],'original_scalar_type':x['type'],'original_scalar_sha256':x['sha256'],'first_original_context':x['first'],'segments':seg,'exact_reconstruction':True})
 x['class']='exact_mixed_segments'
(D/'reading-values.json').write_text(json.dumps(values,indent=2)+'\n')
(D/'mixed-string-reconstruction-map.json').write_text(json.dumps({'rule':'Native full string type/value/hash and every original occurrence in typed maps retained. Only exact logical path substrings are structural. Every remaining prose substring has its own exact typed value ID and must be semantically consumed; no mixed string is blindly discarded. Segment concatenation is exact.','records':maps},indent=2)+'\n')
print('Mixed strings losslessly mapped',len(maps),'original values',original_total,'new total',len(values),'remaining semantic count',sum(x['class']=='semantic' and x['id']>=44788 and not 273749<=x['id']<274421 for x in values),'remaining semantic characters',sum(x['characters'] or 0 for x in values if x['class']=='semantic' and x['id']>=44788 and not 273749<=x['id']<274421))
