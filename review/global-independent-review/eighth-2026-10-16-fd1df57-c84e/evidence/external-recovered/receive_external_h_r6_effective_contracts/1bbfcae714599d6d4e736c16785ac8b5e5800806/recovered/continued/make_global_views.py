import json,gzip,pathlib,hashlib,re
T=pathlib.Path(__file__).resolve().parents[1];O=T/'continued/global';O.mkdir(exist_ok=True);rows=json.loads((T/'payload-catalog.json').read_text())['rows'];seen={};index=[];inventory=[]
def enc(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'),sort_keys=True)
def key(v):return hashlib.sha256(enc(v).encode()).hexdigest()
def get(i):
 s=gzip.decompress((T/rows[i]['decoded_object']).read_bytes()).decode()
 try:return json.loads(s)
 except ValueError:return s
def seed(v,ref):
 h=key(v)
 if len(enc(v))>100:seen.setdefault(h,ref)
 if isinstance(v,dict):
  for k,a in v.items():seed(a,ref+'/'+k.replace('~','~0').replace('/','~1'))
 elif isinstance(v,list):
  for k,a in enumerate(v):seed(a,ref+'/'+str(k))
for i in [0,6,9,15,19,21,39,40,41,42,47,48,50,52,54,56,58]+list(range(23,37)):seed(get(i),'READ_ROW_'+str(i)+'#')
for p in sorted((T/'recovered-r6-cases-current/tasks').glob('*/assigned-14-current-reception.json')):seed(json.loads(p.read_text()),'READ_CASE_'+p.parent.name+'#')
admin={'report_core_full_remote_payload_identities','report_publication_full_remote_payload_identities'}
identity_keys={'repository','commit','tree','workspace_tree','directory_tree','path','bytes','sha256','git_blob','blob','mode','type','lines','total_lines','line_count','encoded_bytes','decoded_bytes','encoding','decoded_sha256','encoded_sha256'}
def visit(v,ref,k=''):
 s=enc(v);h=key(v)
 if len(s)>100 and h in seen:return {'$exact_same':seen[h]}
 if k in admin or (ref.startswith('row45#') and ref.endswith('/full_handoff_package_remote_readback/entries')):
  n=len(inventory);inventory.append({'id':n,'ref':ref,'sha256':h,'count':len(v),'value':v,'purpose':'PURE_PAYLOAD_IDENTITY_TRANSPORT_INVENTORY; no semantic or execution approval'})
  return {'$identity_inventory':n,'count':len(v),'purpose':'payload transport identities; no semantic approval'}
 if isinstance(v,dict) and set(v)<=identity_keys and ('sha256' in v or 'git_blob' in v):
  n=len(inventory);inventory.append({'id':n,'ref':ref,'sha256':h,'value':v,'purpose':'PURE_OBJECT_IDENTITY_ONLY'})
  return {'$identity_inventory':n,'path':v.get('path'),'commit':v.get('commit')}
 alias=None
 if len(s)>100:
  alias='G'+str(len(index));seen[h]=alias;index.append({'id':alias,'ref':ref,'sha256':h})
 if isinstance(v,dict):out={a:visit(b,ref+'/'+a.replace('~','~0').replace('/','~1'),a) for a,b in v.items()}
 elif isinstance(v,list):out=[visit(b,ref+'/'+str(a)) for a,b in enumerate(v)]
 else:out=v
 return {'$id':alias,'value':out} if alias else out
def doc(s,ref):
 parts=re.split(r'(```json\s*\n.*?\n```)',s,flags=re.S);out=[]
 for j,a in enumerate(parts):
  if a.startswith('```json'):
   try:out.append(visit(json.loads(a[a.index('\n')+1:a.rfind('\n```')]),ref+'/fence/'+str(j)));continue
   except ValueError:pass
  for n,b in enumerate(a.splitlines()):
   if b:out.append(visit(b,ref+'/line/'+str(j)+'/'+str(n)))
 return out
manifest=[]
order=[49,51,53,55,57,59,46,1,2,3,4,5,18,20,22,37,38,44,45,43,7,8,16,17,10,11,12,13,14]
for i in order:
 v=get(i);r='row'+str(i)+'#';z=doc(v,r) if isinstance(v,str) else visit(v,r);lines=json.dumps(z,ensure_ascii=False,indent=1).splitlines();pages=[];buf='';n=1
 for line in lines:
  if len(buf)+len(line)>12000 and buf:
   p=O/f'row{i:02d}-{n:03d}.txt';p.write_text(buf);pages.append(str(p.relative_to(T)));buf='';n+=1
  buf+=line+'\n'
 if buf:
  p=O/f'row{i:02d}-{n:03d}.txt';p.write_text(buf);pages.append(str(p.relative_to(T)))
 manifest.append({'row':i,'input':rows[i]['input'],'pages':pages,'chars':sum((T/p).stat().st_size for p in pages),'status':'UNREAD_VIEW_GENERATED_NO_SEMANTIC_CREDIT'})
(O/'index.json').write_text(json.dumps({'exact_aliases':index,'seeds':'Previously completely read rows and current four assigned14 case records; see continued reading ledgers','rows':manifest},ensure_ascii=False,indent=2)+'\n')
with gzip.open(O/'identity-inventory.json.gz','wt') as f:json.dump(inventory,f,ensure_ascii=False)
print(json.dumps([(a['row'],len(a['pages']),a['chars']) for a in manifest]));print('definitions',len(index),'identity inventory',len(inventory))
