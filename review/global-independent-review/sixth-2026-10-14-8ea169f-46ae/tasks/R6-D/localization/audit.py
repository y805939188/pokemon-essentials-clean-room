"""Review tooling only. Primitive whitelist decoder; never evaluates reference data.
Authored in this review after inspecting the historical decoder as a design aid.
No historical verdicts imported. Output is structural inventory, not semantic reading.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import json, hashlib, re, sys, zlib
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D/localization'
REF=ROOT/'reference/pokemon-essentials'
def sha(x):return hashlib.sha256(x).hexdigest()
def write(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def append(name,obj):
 with (OUT/name).open('a') as f:f.write(json.dumps(obj,ensure_ascii=False)+'\n')
def event(kind,**kw):append('command-log.jsonl',{'utc':datetime.now(timezone.utc).isoformat(),'action':kind,**kw})
class PrimitiveReader:
 def __init__(self,b):self.b=b; self.p=0; self.refs=[]; self.syms=[]; self.tags=Counter()
 def take(self,n):
  if n<0 or self.p+n>len(self.b):raise ValueError('bounded EOF')
  v=self.b[self.p:self.p+n];self.p+=n;return v
 def byte(self):return self.take(1)[0]
 def integer(self):
  q=self.byte(); q=q if q<128 else q-256
  if q==0:return 0
  if q>4:return q-5
  if q< -4:return q+5
  v=int.from_bytes(self.take(abs(q)),'little');return v if q>0 else v-(1<<(8*abs(q)))
 def size(self):
  n=self.integer()
  if n<0 or n>2_000_000:raise ValueError('size bound')
  return n
 def obj(self,depth=0):
  if depth>128:raise ValueError('depth bound')
  t=chr(self.byte());self.tags[t]+=1
  if t=='0':return None
  if t=='T':return True
  if t=='F':return False
  if t=='i':return self.integer()
  if t=='@':
   n=self.size()
   if n>=len(self.refs):raise ValueError('bad object reference')
   return self.refs[n]
  if t==';':
   n=self.size()
   if n>=len(self.syms):raise ValueError('bad symbol reference')
   return self.syms[n]
  if t in ('"',':'):
   b=self.take(self.size())
   if t==':':v=('symbol',b); self.syms.append(v)
   else:v=b; self.refs.append(v)
   return v
  if t=='[':
   n=self.size();v=[];self.refs.append(v)
   for _ in range(n):v.append(self.obj(depth+1))
   return v
  if t=='{':
   n=self.size();v={};self.refs.append(v)
   for _ in range(n):
    k=self.obj(depth+1);val=self.obj(depth+1)
    if not isinstance(k,(bytes,int,tuple,type(None),bool)):raise ValueError('nonprimitive hash key')
    v[k]=val
   return v
  if t=='I':
   v=self.obj(depth+1)
   for _ in range(self.size()):
    k=self.obj(depth+1);val=self.obj(depth+1)
    if k==('symbol',b'E'):
     if not isinstance(val,bool):raise ValueError('bad encoding flag')
    elif k==('symbol',b'encoding'):
     if not isinstance(val,bytes):raise ValueError('bad encoding name')
    else:raise ValueError('unsupported metadata')
   return v
  raise ValueError(f'rejected tag {t!r} at {self.p-1}')
def decode(path):
 b=path.read_bytes();p=PrimitiveReader(b)
 if p.take(2)!=b'\x04\x08':raise ValueError('header')
 v=p.obj()
 if p.p!=len(b):raise ValueError('trailing bytes')
 event('safe_primitive_decode',path=str(path.relative_to(ROOT)),sha256=sha(b),bytes=len(b),consumed=p.p,tags=dict(p.tags),semantic_status='structure_only')
 return v
IDS={'SPECIES_NAMES':1,'SPECIES_CATEGORIES':2,'POKEDEX_ENTRIES':3,'SPECIES_FORM_NAMES':4,'MOVE_NAMES':5,'MOVE_DESCRIPTIONS':6,'ITEM_NAMES':7,'ITEM_NAME_PLURALS':8,'ITEM_DESCRIPTIONS':9,'ABILITY_NAMES':10,'ABILITY_DESCRIPTIONS':11,'TYPE_NAMES':12,'TRAINER_TYPE_NAMES':13,'SCRIPT_TEXTS':24,'RIBBON_NAMES':25,'RIBBON_DESCRIPTIONS':26,'ITEM_PORTION_NAMES':28,'ITEM_PORTION_NAME_PLURALS':29}
def deescape(t):
 for old,new in [('<<1>>','\x01'),('<<r>>','\r'),('<<n>>','\n'),('<<[>>','['),('<<]>>',']'),('<<t>>','\t')]:t=t.replace(old,new)
 return t

def inventory():
 payload=decode(REF/'Data/messages_core.dat');rows=[];bins=[]
 for i,v in enumerate(payload):bins.append({'section':i,'shape':type(v).__name__,'entries':len(v) if isinstance(v,(dict,list)) else None})
 write('binary-sections.json',bins)
 for p in sorted((REF/'Text_english_core').glob('*.txt')):
  lines=p.read_text(encoding='utf-8-sig').splitlines();domain=p.stem
  assert lines[3]=='['+domain+']'; assert (len(lines)-4)%2==0
  expected=payload[IDS[domain]];recs=[]
  for j in range(4,len(lines),2):
   k,v=lines[j:j+2];kd=deescape(k).encode();vd=deescape(v).encode()
   rec={'unit':f'{domain}:{(j-4)//2}','lines':[j+1,j+2],'key_sha256':sha(kd),'value_sha256':sha(vd),'duplicate_identity':k==v,'binary_equal':expected.get(kd)==vd,'placeholders':re.findall(r'\{[^{}]*\}',k),'escapes':re.findall(r'<<[^<>]*>>',k),'controls':re.findall(r'\\(?:[A-Za-z]+|[.!|^<>])(?:\[[^\]]*\])?',k),'tags':re.findall(r'</?[^>]+>',k),'semantic_status':'not_read','consumer':'MessageTypes section '+str(IDS[domain])}
   recs.append(rec)
  write('records-'+domain+'.json',recs)
  rows.append({'path':str(p.relative_to(REF)),'sha256':sha(p.read_bytes()),'lines':len(lines),'records':len(recs),'section':IDS[domain],'identity_duplicates':sum(x['duplicate_identity'] for x in recs),'binary_equal':sum(x['binary_equal'] for x in recs),'extra_binary_keys':len(set(expected)-{deescape(lines[j]).encode() for j in range(4,len(lines),2)}),'review_extent':'structure_only','semantic_unread':len(recs)})
  append('reading-ledger.jsonl',{'path':str(p.relative_to(REF)),'range':[1,len(lines)],'review_extent':'structure_only','method':'full bytes parsed; not semantic reading','sha256':sha(p.read_bytes()),'units':len(recs)})
 write('inventory.json',rows)
 scripts=decode(REF/'Data/Scripts.rxdata');sr=[]
 for i,row in enumerate(scripts):
  assert isinstance(row,list) and len(row)==3
  sid,name,compressed=row
  assert isinstance(sid,int) and isinstance(name,bytes) and isinstance(compressed,bytes)
  d=zlib.decompressobj();body=d.decompress(compressed,5_000_000)
  assert d.eof and not d.unused_data and not d.unconsumed_tail
  text=body.decode('utf-8-sig');file=OUT/f'decoded-script-{i:02}.txt';file.write_text(text)
  sr.append({'record':i,'id':sid,'name':name.decode(),'compressed_sha256':sha(compressed),'decoded_sha256':sha(body),'decoded_bytes':len(body),'decoded_lines':len(text.splitlines()),'review_extent':'structure_only'})
 write('script-records.json',sr)
 print(json.dumps({'text':rows,'scripts':sr},ensure_ascii=False,indent=2))
def read(path,start,end,extent='semantic'):
 p=ROOT/path;b=p.read_bytes();lines=b.decode('utf-8-sig').splitlines();start=int(start);end=min(int(end),len(lines))
 text='\n'.join(f'{i+1}: {lines[i]}' for i in range(start-1,end))
 append('reading-ledger.jsonl',{'path':path,'range':[start,end],'sha256':sha(b),'review_extent':extent,'method':'contiguous displayed range; semantic acceptance recorded separately'})
 event('read_contiguous_range',path=path,start=start,end=end,sha256=sha(b))
 print(text)
def corpus(domain,start,end):
 p=REF/'Text_english_core'/f'{domain}.txt';lines=p.read_text(encoding='utf-8-sig').splitlines();recs=json.loads((OUT/f'records-{domain}.json').read_text());a=int(start);b=min(int(end),len(recs)-1)
 for n in range(a,b+1):
  j=4+n*2;k,v=lines[j:j+2]
  print(f'{domain}:{n} L{j+1}-{j+2} '+k+((' | TRANSLATION: '+v) if k!=v else ''))
 append('reading-ledger.jsonl',{'path':str(p.relative_to(REF)),'unit_range':[a,b],'line_range':[5+a*2,6+b*2],'sha256':sha(p.read_bytes()),'review_extent':'semantic_display','method':'every unique key/body displayed; identity translation copy deduplicated'})
 event('read_corpus_contiguous',domain=domain,unit_range=[a,b])
if __name__=='__main__':
 if sys.argv[1]=='inventory':inventory()
 elif sys.argv[1]=='read':read(*sys.argv[2:])
 elif sys.argv[1]=='corpus':corpus(*sys.argv[2:])
