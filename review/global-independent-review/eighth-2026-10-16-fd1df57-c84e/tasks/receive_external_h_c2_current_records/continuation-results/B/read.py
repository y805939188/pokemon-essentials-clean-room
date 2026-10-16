"""Lossless JSON display with exact-value dedup. Display generation earns zero credit."""
from pathlib import Path
import argparse,json,hashlib,datetime
T=Path(__file__).resolve().parent
S=T/'display-state.json'
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def save(v):S.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def walk(v,p,pool):
 pool.setdefault(sha(enc(v)),p)
 if isinstance(v,dict):
  for k,x in v.items():walk(x,p+'/'+k.replace('~','~0').replace('/','~1'),pool)
 elif isinstance(v,list):
  for i,x in enumerate(v):walk(x,p+'/'+str(i),pool)
def display(v,p,pool,local):
 h=sha(enc(v))
 if len(enc(v))>80:
  if h in pool:
   metadata.append(dict(pointer=p,same_previously_read=pool[h],sha256=h,purpose='Exact same value already acknowledged'))
   return {'$same_read':len(metadata)-1}
  if h in local:
   metadata.append(dict(pointer=p,same_within_display=local[h],sha256=h,purpose='Exact same value in this complete display'))
   return {'$same_display':len(metadata)-1}
  local[h]=p
 if isinstance(v,dict):
  if set(v).issubset({'identity_id','path','scope','original_scope_ref','kind','commit','revision','lines','clause','source_commit','repo','repository'}) and 'path' in v and any(k in v for k in ('identity_id','lines','scope')):
   metadata.append(dict(pointer=p,value=v,purpose='Exact source/formal locator only; no target body credit'))
   return {'$locator':len(metadata)-1}
  refs={'document','sha256','bytes','json_pointer','original_report_path','binding_id','canonical_sha256','input_sha256','raw_member_byte_offsets','raw_member_bytes','raw_member_sha256','file','file_bytes','file_sha256'}
  if set(v).issubset(refs) and ('document' in v or 'binding_id' in v or 'file_sha256' in v):
   metadata.append(dict(pointer=p,value=v,purpose='Complete immutable identity/pointer binding; target semantic body gets zero credit'))
   return {'$typed_binding':len(metadata)-1,'document':v.get('document',v.get('file')),'pointer':v.get('json_pointer')}
  if set(v)=={'字段','完整值引用'}:
   metadata.append(dict(pointer=p,value=v,purpose='Exact field pointer; underlying full value must be separately read'))
   return {'$field_binding':len(metadata)-1,'field':v['字段']}
  return {k:display(x,p+'/'+k.replace('~','~0').replace('/','~1'),pool,local) for k,x in v.items()}
 if isinstance(v,list):return [display(x,p+'/'+str(i),pool,local) for i,x in enumerate(v)]
 return v
ap=argparse.ArgumentParser();ap.add_argument('action');ap.add_argument('label');ap.add_argument('--file',type=int);ap.add_argument('--pointer',default='');ap.add_argument('--part',type=int,default=0);ap.add_argument('--note');a=ap.parse_args()
s=json.loads(S.read_text()) if S.exists() else dict(pool={},pending={},read=[])
if a.action=='prepare':
 v=json.loads((T/'.work/originals'/str(a.file)).read_text())
 for x in a.pointer.split('/')[1:]:v=v[int(x)] if isinstance(v,list) else v[x.replace('~1','/').replace('~0','~')]
 metadata=s.setdefault('typed_identity',[]);anchor=f'file{a.file}#{a.pointer}';txt=json.dumps(display(v,anchor,s['pool'],{}),ensure_ascii=False,separators=(',',':'));parts=[txt[i:i+9500] for i in range(0,len(txt),9500)] or [''];(T/'views').mkdir(exist_ok=True)
 for n,t in enumerate(parts):(T/'views'/f'{a.label}.{n}.txt').write_text(t)
 s['pending'][a.label]=dict(file=a.file,pointer=a.pointer,anchor=anchor,object_sha256=sha(enc(v)),display_sha256=sha(txt.encode()),parts=len(parts),shown=[]);print(a.label,len(parts),len(txt))
elif a.action=='show':
 r=s['pending'][a.label];print(a.label,a.part+1,'/',r['parts'],r['anchor']);print((T/'views'/f'{a.label}.{a.part}.txt').read_text());r['shown'].append(a.part)
elif a.action=='ack':
 r=s['pending'].pop(a.label);assert set(r['shown'])==set(range(r['parts'])) and a.note
 v=json.loads((T/'.work/originals'/str(r['file'])).read_text())
 for x in r['pointer'].split('/')[1:]:v=v[int(x)] if isinstance(v,list) else v[x.replace('~1','/').replace('~0','~')]
 assert sha(enc(v))==r['object_sha256'];walk(v,r['anchor'],s['pool']);r.update(label=a.label,reader_note=a.note,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),behavior='NOT_EXECUTED');s['read'].append(r);print('ACK',a.label)
save(s)
