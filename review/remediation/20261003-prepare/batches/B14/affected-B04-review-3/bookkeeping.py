import subprocess,json,hashlib,pathlib,sys
O=pathlib.Path(__file__).parent
G='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
P='41fffb540c6483f5296ea0d33b789b75180d27ed'
C='c06db6cd964188b3c693a9b7820e3a8aaffe0b04'
B='1e6b11a47370f1c7c4659a32443fc1afda597bac'
C2='af39efbf32549be964cb083bd49bed6d1d5c0d2a'
R='4299db3e3e3c0323823edbb30a93f592a5493945'
GP='review/global-independent-review/2026-10-03-fd82a639/'
PP='review/remediation-20261003-prepare/'
RP='review/remediation/20261003-prepare/batches/B14/'
def git(*args,repo=None):
 return subprocess.check_output(['git',*(['-C',repo] if repo else []),*args])
def show(c,p,repo=None):return git('show',c+':'+p,repo=repo)
def digest(x):return hashlib.sha256(x).hexdigest()
def event(x):
 f=O/'reading-events.jsonl'
 with f.open('a') as h:h.write(json.dumps(x,ensure_ascii=False)+'\n')
def read(c,p,start=1,end=None,repo=None):
 data=show(c,p,repo);ls=data.decode().splitlines();end=end or len(ls)
 print('READ',c,p,'LINES',start,end,'TOTAL',len(ls))
 for i in range(start-1,min(end,len(ls))):print(str(i+1)+': '+ls[i])
 event({'kind':'displayed_exact_range','commit':c,'path':p,'start':start,'end':min(end,len(ls)),'total':len(ls),'sha256':digest(data),'repository':'fixed reference' if repo else 'project','semantic_claim':'requires model inspection; not inferred from display'})
def controls():
 gs=json.loads(show(G,GP+'findings.json'));ps=json.loads(show(P,PP+'finding-acceptance.json'))
 qc=json.loads(show(R,RP+'affected-B04-review-2/qualified-controls.json'))
 ids=[x['id'] for x in qc['controls']]
 ids+=['GIR-FD82-'+x for x in ['C059','C060','C061','C067','C068','C071','C072','C073','C118','006','A058','A059']]
 ids=list(dict.fromkeys(ids));docs=[]
 raw=set()
 for i in ids:
  x=next(x for x in gs if x['id']==i);docs.append((G,GP+'findings.json',i,x));docs.append((P,PP+'finding-acceptance.json',i,ps[i]))
  for r in x.get('raw_reports',[]):
   if isinstance(r,dict):raw.add(r.get('raw_id',r.get('id','')))
   elif isinstance(r,str):raw.add(r)
  for r in x.get('root_adjudications',[]):
   if isinstance(r,dict):raw.add(r.get('raw_id',''))
 for f in ['root/adjudication-log.json','root/extension-adjudications.json']:
  obj=json.loads(show(G,GP+f))
  for n,x in enumerate(obj['adjudications']):
   if x.get('raw_id') in raw or any(i in json.dumps(x) for i in ids):docs.append((G,GP+f,str(n),x))
 values=[];vmap={};maps=[];identities=[]
 def walk(x,pointer,docindex):
  if isinstance(x,dict):
   for k,v in x.items():walk(v,pointer+'/'+str(k).replace('~','~0').replace('/','~1'),docindex)
  elif isinstance(x,list):
   for i,v in enumerate(x):walk(v,pointer+'/'+str(i),docindex)
  else:
   key=json.dumps(x,ensure_ascii=False,sort_keys=True)
   if key not in vmap:vmap[key]=len(values);values.append(x)
   maps.append({'object':docindex,'pointer':pointer,'value_id':vmap[key]})
 for j,(c,p,k,x) in enumerate(docs):
  identities.append({'commit':c,'path':p,'object_key':k,'canonical_sha256':digest(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()),'structure':x})
  walk(x,'',j)
 # Lossless object skeleton and leaf mapping; no source/claim text copied into report.
 def skeleton(x):
  if isinstance(x,dict):return {k:skeleton(v) for k,v in x.items()}
  if isinstance(x,list):return [skeleton(v) for v in x]
  return {'unique_value_id':vmap[json.dumps(x,ensure_ascii=False,sort_keys=True)]}
 for x in identities:x['structure']=skeleton(x['structure'])
 (O/'qualified-control-mapping.json').write_text(json.dumps({'ids':ids,'objects':identities,'leaf_mapping':maps,'value_identities':[{'id':i,'canonical_sha256':digest(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()),'type':type(v).__name__} for i,v in enumerate(values)],'lossless_deduplication':'Only identical typed primitive values deduplicated; full object skeleton and every occurrence retained. Values read from fixed inputs, not copied into output.'},ensure_ascii=False,indent=2)+'\n')
 return values,maps,identities
def evidence_pool():
 # Complete unfiltered added document payloads; lossless leaf deduplication against read controls.
 seed,_,_=controls();vals=[];vmap={json.dumps(v,ensure_ascii=False,sort_keys=True):'control:'+str(i) for i,v in enumerate(seed)}
 formal_lines=set()
 for fn in ['accepted-to-C3-formal.diff','C2-to-C3-formal.diff']:
  for l in (O/fn).read_text().splitlines():
   if l.startswith(('+','-',' ')) and not l.startswith(('+++','---')):formal_lines.add(l[1:])
 for l in formal_lines:vmap.setdefault(json.dumps(l,ensure_ascii=False),'read_formal_line:'+digest(l.encode()))
 maps=[];docs=[];plain=[]
 paths=[x.split('\t')[1] for x in (O/'accepted-to-C3-paths.txt').read_text().splitlines() if x.startswith('A\t')]
 extra=[(R,RP+'affected-B04-review-2/'+n) for n in ['static-designs.json','qualified-controls.json','refrozen-input-verification.json','B04-formal-preservation.json','catalog-comparison.json','protected-sections.json','affected-dispositions.json','identity-and-verdict.json','handoff.json']]
 pairs=[(C,p) for p in paths]+extra
 def walk(x,ptr,di):
  if isinstance(x,dict):return {k:walk(v,ptr+'/'+str(k).replace('~','~0').replace('/','~1'),di) for k,v in x.items()}
  if isinstance(x,list):return [walk(v,ptr+'/'+str(i),di) for i,v in enumerate(x)]
  key=json.dumps(x,ensure_ascii=False,sort_keys=True)
  if key not in vmap:vmap[key]='evidence:'+str(len(vals));vals.append(x)
  vi=vmap[key];maps.append({'object':di,'pointer':ptr,'value_id':vi});return {'unique_value_id':vi}
 for c,p in pairs:
  data=show(c,p);di=len(docs)
  doc={'commit':c,'path':p,'sha256':digest(data),'bytes':len(data)}
  if p.endswith('.json'):
   x=json.loads(data);doc['structure']=walk(x,'',di)
  else:
   # Every patch body line maps to an exact already-read formal line if possible.
   lines=data.decode().splitlines();doc['line_mapping']=[]
   for i,l in enumerate(lines,1):
    q=l[1:] if p.endswith('.patch') and l.startswith(('+','-',' ')) and not l.startswith(('+++','---')) else l
    k=json.dumps(q,ensure_ascii=False)
    if k in vmap:doc['line_mapping'].append({'line':i,'mapped_value_id':vmap[k]})
    else:plain.append({'commit':c,'path':p,'line':i,'text':l});doc['line_mapping'].append({'line':i,'plain_index':len(plain)-1})
  docs.append(doc)
 (O/'evidence-mapping.json').write_text(json.dumps({'objects':docs,'occurrences':maps,'value_identities':[{'id':i,'sha256':digest(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()),'type':type(v).__name__} for i,v in enumerate(vals)],'plain_line_identities':[{'index':i,'commit':x['commit'],'path':x['path'],'line':x['line'],'sha256':digest(x['text'].encode())} for i,x in enumerate(plain)],'deduplication':'Only exact primitive values and exact previously read formal lines reused, with every occurrence mapped; no inferred semantic equivalence.'},ensure_ascii=False,indent=2)+'\n')
 return vals,maps,docs,plain
def owner_pool():
 seed,_,_=controls();es,_,_,_=evidence_pool();known={json.dumps(v,ensure_ascii=False,sort_keys=True):'previous:'+digest(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()) for v in seed+es}
 c='acda1abc811cc07ea83c6a0930872e9a8cea174e';p='review/remediation/20261003-prepare/batches/B04/integration-review-1/finding-dispositions.json'
 x=json.loads(show(c,p));ids={'GIR-FD82-002','GIR-FD82-003','GIR-FD82-C003','GIR-FD82-C007','GIR-FD82-C093','GIR-FD82-C106','GIR-FD82-C071','GIR-FD82-C072','GIR-FD82-C073'}
 vals=[];mapping=[]
 def walk(v,ptr):
  if isinstance(v,dict):return {k:walk(a,ptr+'/'+k) for k,a in v.items()}
  if isinstance(v,list):return [walk(a,ptr+'/'+str(i)) for i,a in enumerate(v)]
  k=json.dumps(v,ensure_ascii=False,sort_keys=True)
  if k not in known:known[k]='owner:'+str(len(vals));vals.append(v)
  mapping.append({'pointer':ptr,'value_id':known[k]});return {'value_id':known[k]}
 rows=[r for r in x['rows'] if r['id'] in ids];structure=walk(rows,'/rows')
 (O/'accepted-owner-control-mapping.json').write_text(json.dumps({'commit':c,'path':p,'source_sha256':digest(show(c,p)),'ids':sorted(ids),'structure':structure,'mapping':mapping,'unique_value_identities':[{'id':i,'sha256':digest(json.dumps(v,ensure_ascii=False,sort_keys=True).encode())} for i,v in enumerate(vals)]},ensure_ascii=False,indent=2)+'\n')
 return vals,mapping
if __name__=='__main__':
 mode=sys.argv[1]
 if mode=='owner':
  vs,ms=owner_pool();a=int(sys.argv[2]);b=int(sys.argv[3]);print('OWNER_POOL',len(vs))
  for n in range(a,min(b,len(vs))):
   ptr=next(m['pointer'] for m in ms if m['value_id']=='owner:'+str(n));print(str(n)+' '+ptr+' '+json.dumps(vs[n],ensure_ascii=False))
  event({'kind':'accepted_owner_unique_values_displayed','start':a,'end_exclusive':min(b,len(vs)),'total':len(vs),'mapping':'accepted-owner-control-mapping.json'})
 elif mode in ['epool','plain']:
  vs,ms,ds,pl=evidence_pool();a=int(sys.argv[2]);b=int(sys.argv[3]);print('EVIDENCE_POOL',len(vs),'PLAIN_LINES',len(pl),'OBJECTS',len(ds),'OCCURRENCES',len(ms))
  if mode=='plain':
   for i in range(a,min(b,len(pl))):
    x=pl[i];print(str(i)+' '+x['path'].split('B14/',1)[-1]+':'+str(x['line'])+' '+x['text'])
  else:
   for n in range(a,min(b,len(vs))):
    contexts=[(ds[m['object']]['path'].split('B14/',1)[-1],m['pointer']) for m in ms if m['value_id']=='evidence:'+str(n)]
    print(str(n)+' '+contexts[0][0]+contexts[0][1]+' '+json.dumps(vs[n],ensure_ascii=False))
  event({'kind':'evidence_unique_values_displayed' if mode=='epool' else 'evidence_unique_plain_lines_displayed','start':a,'end_exclusive':min(b,len(vs) if mode=='epool' else len(pl)),'mapping':'evidence-mapping.json','semantic_claim':'requires model inspection'})
 elif mode=='pool':
  vs,ms,ds=controls();a=int(sys.argv[2]);b=int(sys.argv[3]);print('POOL',len(vs),'OBJECTS',len(ds),'OCCURRENCES',len(ms))
  for n in range(a,min(b,len(vs))):
   context=[(ds[m['object']]['object_key'],m['pointer']) for m in ms if m['value_id']==n]
   print(str(n)+' '+context[0][0]+' '+context[0][1]+' '+json.dumps(vs[n],ensure_ascii=False))
  event({'kind':'qualified_control_unique_values_displayed','start':a,'end_exclusive':min(b,len(vs)),'total':len(vs),'mapping':'qualified-control-mapping.json','semantic_claim':'requires model inspection'})
 elif mode=='read':read(sys.argv[2],sys.argv[3],int(sys.argv[4]) if len(sys.argv)>4 else 1,int(sys.argv[5]) if len(sys.argv)>5 else None)
