"""Review-only data decoding. Does not import/execute Ruby, reference, or game code.
Whitelist Marshal primitives; rejects all class/object/user-defined load tags.
Writes hashes/locations and diagnostics only within M01. Not a behavior test.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,re
import review_state as s
class PrimitiveReader:
 def __init__(self,data): self.data=data; self.pos=0; self.objects=[]; self.symbols=[]; self.tags=Counter()
 def byte(self):
  if self.pos>=len(self.data): raise ValueError('Unexpected EOF')
  c=self.data[self.pos]; self.pos+=1; return c
 def integer(self):
  c=self.byte(); c=c if c<128 else c-256
  if c==0:return 0
  if c>4:return c-5
  if c< -4:return c+5
  n=abs(c); b=self.data[self.pos:self.pos+n]; self.pos+=n
  if len(b)!=n:raise ValueError('Short integer')
  v=int.from_bytes(b,'little'); return v if c>0 else v-(1<<(8*n))
 def size(self):
  n=self.integer()
  if not 0<=n<=2_000_000:raise ValueError('Bad/oversized length')
  return n
 def obj(self,depth=0):
  if depth>128:raise ValueError('Depth bound')
  t=chr(self.byte()); self.tags[t]+=1
  if t=='0':return None
  if t=='T':return True
  if t=='F':return False
  if t=='i':return self.integer()
  if t=='@':return self.objects[self.size()]
  if t==';':return self.symbols[self.size()]
  if t in ('"',':'):
   n=self.size(); b=self.data[self.pos:self.pos+n]; self.pos+=n
   if len(b)!=n:raise ValueError('Short string')
   if t==':': v=('symbol',b); self.symbols.append(v)
   else: v=b; self.objects.append(v)
   return v
  if t=='[':
   n=self.size(); a=[]; self.objects.append(a)
   for _ in range(n):a.append(self.obj(depth+1))
   return a
  if t=='{':
   n=self.size(); h={}; self.objects.append(h)
   for _ in range(n):k=self.obj(depth+1); v=self.obj(depth+1); h[k]=v
   return h
  if t=='I':
   v=self.obj(depth+1)
   for _ in range(self.size()):
    k=self.obj(depth+1); meta=self.obj(depth+1)
    if k not in [('symbol',b'E'),('symbol',b'encoding')]:raise ValueError('Unsupported instance metadata')
    if k==('symbol',b'E') and not isinstance(meta,bool):raise ValueError('Invalid encoding metadata')
    if k==('symbol',b'encoding') and not isinstance(meta,bytes):raise ValueError('Invalid encoding name')
   return v
  raise ValueError('Rejected non-whitelisted tag '+repr(t)+' at '+str(self.pos-1))
def sha(b):return hashlib.sha256(b).hexdigest()
def de_escape(v):
 # Text format decoding only, not execution of compiler or behavior assertions.
 for old,new in [('<<1>>','\x01'),('<<r>>','\r'),('<<n>>','\n'),('<<[>>','['),('<<]>>',']'),('<<t>>','\t')]:v=v.replace(old,new)
 return v
IDs={'SPECIES_NAMES':1,'SPECIES_CATEGORIES':2,'POKEDEX_ENTRIES':3,'SPECIES_FORM_NAMES':4,'MOVE_NAMES':5,'MOVE_DESCRIPTIONS':6,'ITEM_NAMES':7,'ITEM_NAME_PLURALS':8,'ITEM_DESCRIPTIONS':9,'ABILITY_NAMES':10,'ABILITY_DESCRIPTIONS':11,'TYPE_NAMES':12,'TRAINER_TYPE_NAMES':13,'SCRIPT_TEXTS':24,'RIBBON_NAMES':25,'RIBBON_DESCRIPTIONS':26,'ITEM_PORTION_NAMES':28,'ITEM_PORTION_NAME_PLURALS':29}
b=(s.REF/'Data/messages_core.dat').read_bytes(); p=PrimitiveReader(b)
assert p.byte()==4 and p.byte()==8,'Marshal header'; payload=p.obj(); assert p.pos==len(b),'Trailing bytes'
summary={'schema_version':'gr5.review.v1','module':'M01','source_baseline':s.R,'parser_boundary':'Whitelist data-only decode. No Ruby/Marshal.load/reference execution; no user object hooks; all other tags rejected. Parser output is DATA_INSPECTION_ONLY, not full semantic review.','bytes':len(b),'consumed':p.pos,'sha256':sha(b),'tags':dict(p.tags),'sections':[],'text_files':[]}
for i,v in enumerate(payload):
 row={'id':i,'shape':type(v).__name__,'entries':len(v) if isinstance(v,(list,dict)) else None}
 if isinstance(v,list):row['child_shapes']=dict(Counter(type(x).__name__ for x in v)); row['nonempty_child_indices']=[j for j,x in enumerate(v) if x]
 summary['sections'].append(row)
for path in sorted((s.REF/'Text_english_core').glob('*.txt')):
 lines=path.read_text(encoding='utf-8-sig').splitlines(); domain=path.stem; expected=payload[IDs[domain]]
 assert isinstance(expected,dict)
 assert lines[3]=='['+domain+']'
 body=lines[4:]; assert len(body)%2==0
 ledger=[]; same=0; missing=[]; mismatch=[]; seen=Counter(); decoded={}; edge=Counter()
 for j in range(0,len(body),2):
  k,v=body[j:j+2]; kd=de_escape(k).encode(); vd=de_escape(v).encode(); seen[kd]+=1; decoded[kd]=vd
  if kd not in expected:missing.append(j//2)
  elif expected[kd]!=vd:mismatch.append(j//2)
  else:same+=1
  marks=[]
  for label,pred in [('empty',not k or not v),('raw_hash_lead',k.startswith('#') or v.startswith('#')),('edge_whitespace',k!=k.strip() or v!=v.strip()),('digits_key',bool(re.fullmatch(r'\d+',k))),('escape_marker','<<' in k or '<<' in v),('placeholder',bool(re.search(r'\{\d+',k+v))),('bracket_start',k.startswith(('[' ,']')) or v.startswith(('[',']')))]:
   if pred:marks.append(label);edge[label]+=1
  ledger.append({'record':j//2,'lines':[j+5,j+6],'key_sha256':sha(kd),'value_sha256':sha(vd),'text_key_equals_value':k==v,'matches_binary_entry':kd in expected and expected[kd]==vd,'markers':marks,'review_extent':'inventory_only','semantic_status':'not_reviewed','consumer_mapping':'M01-LZ-DOMAINS / '+domain})
 data={'schema_version':'gr5.review.v1','source':str(path.relative_to(s.REF)),'source_baseline':s.R,'sha256':sha(path.read_bytes()),'records':ledger,'all_records_semantically_reviewed':False}
 s.write('text-records-'+domain+'.json',data)
 summary['text_files'].append({'path':str(path.relative_to(s.REF)),'domain':IDs[domain],'records':len(ledger),'binary_matches':same,'binary_missing_record_indices':missing,'binary_different_record_indices':mismatch,'binary_extra_entries':len(set(expected)-set(decoded)),'duplicate_decoded_keys':[sha(k) for k,v in seen.items() if v>1],'marker_counts':dict(edge),'semantic_review':'inventory_only; every record still requires domain/consumer semantic comparison'})
s.write('message-data-inspection.json',summary)
c=s.read('reading-coverage.json')
for x in c['sources']:
 if x['path'].startswith('Text_english_core/') or x['path']=='Data/messages_core.dat':
  x['material_availability']='available_safe_primitive_decode' if x['path'].endswith('.dat') else 'available_text'
  x['review_extent']='inventory_only'; x['evidence_level']='data_inspection_only'; x['inspection_artifact']='message-data-inspection.json'; x['semantic_review_warning']='Automatic full read/comparison is not semantic review; record consumers remain not_reviewed.'
s.write('reading-coverage.json',c)
print(json.dumps(summary,ensure_ascii=False,indent=2))
