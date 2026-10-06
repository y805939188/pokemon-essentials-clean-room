"""Own static full control document supplement; no inspected program execution."""
import sys,json,hashlib,gzip
from read_documents import OUT,show,PRE,ORIG,PLAN,pool,primary_supplement,record
from consume_audit import digest,pure_identity
root='review/global-independent-review/2026-10-03-fd82a639/'
reg=json.loads(show(PRE,'review/remediation/20261003-prepare/batches/B02/integration-stage-1/finding-registration.json'))
ids=[x['id'] for x in reg['dispositions']]
original=json.loads(show(ORIG,root+'findings.json'));planpath='review/remediation-20261003-prepare/finding-acceptance.json';plan=json.loads(show(PLAN,planpath))
docs=[(ORIG,root+'findings.json','/'+str(i),x) for i,x in enumerate(original) if x['id'] in ids]+[(PLAN,planpath,'/'+i,plan[i]) for i in ids]
raw=set(ids)
for _,_,_,x in docs:
 raw.update(a.get('raw_id','') for a in x.get('raw_reports',[]) if isinstance(a,dict))
for p,key in [('root/adjudication-log.json','adjudications'),('root/extension-adjudications.json','adjudications')]:
 obj=json.loads(show(ORIG,root+p));docs.append((ORIG,root+p,'/metadata',{k:v for k,v in obj.items() if k!=key}))
 for i,x in enumerate(obj[key]):
  if any(r in json.dumps(x,ensure_ascii=False) for r in raw if r):docs.append((ORIG,root+p,'/'+key+'/'+str(i),x))
vs,occ,st=pool(docs)
seed,_,_=pool(primary_supplement());known={digest(v) for v in seed}
with gzip.open(OUT/'continuation-transient-corpus.json.gz','rt') as f:av,ao,ast,ai=json.load(f)
events=[json.loads(l) for l in (OUT/'delivery-log.jsonl').read_text().splitlines()]
conf=set()
for e in events:
 if e.get('kind')=='continuation_semantic_confirmed':conf.update(e['value_hashes'])
 if e.get('kind')=='audit_group_semantic_delivery' and e.get('pattern') in ['/B14/integration-stage-1/','affected-B02-actual-review-1/reading-log.json']:conf.update(e['value_hashes'])
known.update(conf)
left=[i for i,v in enumerate(vs) if digest(v) not in known and not pure_identity(v,occ[i])]
print('B02 complete control pairs',len(ids),'root/extension objects',len(docs)-24,'unique new semantic values',len(left))
mode=sys.argv[1]
if mode=='late':
 old=json.loads((OUT/'owner-original-qualified-supplement.json').read_text());extra=[i for i in left if i not in old['new_semantic_indices']]
 for i in extra:print('V'+str(i),json.dumps(vs[i],ensure_ascii=False))
 record({'kind':'owner_late_identity_semantic_delivery','indices':extra,'value_hashes':[digest(vs[i]) for i in extra],'requires_manual_confirmation':True})
elif mode=='verify':
 m=json.loads((OUT/'owner-original-qualified-supplement.json').read_text());assert m['structures']==st
 for i,x in enumerate(m['values']):assert x['index']==i and x['type']==type(vs[i]).__name__ and x['sha256']==digest(vs[i]) and x['occurrences']==occ[i]
 print('Full original/PLAN/root/extension typed native reconstruction verified against exact fixed Git objects')
elif mode=='map':
 m={'ids':ids,'structures':st,'values':[{'index':i,'type':type(v).__name__,'sha256':digest(v),'occurrences':occ[i],'exact_consumed_reuse':digest(v) in known,'structural_identity_only':pure_identity(v,occ[i])} for i,v in enumerate(vs)],'new_semantic_indices':left,'stage':'Continuation primary control supplement; earlier accepted owner controls and changed consumers read independently; this full original supplement follows deferred comparison, not a retrospective first-stage claim.'}
 (OUT/'owner-original-qualified-supplement.json').write_text(json.dumps(m,ensure_ascii=False,separators=(',',':'))+'\n')
else:
 a,b=map(int,sys.argv[2:4])
 for n in range(a,min(b,len(left))):i=left[n];print('O'+str(n),'V'+str(i),json.dumps(vs[i],ensure_ascii=False))
 record({'kind':'owner_original_supplement_delivery','range':[a,min(b,len(left))],'indices':left[a:b],'value_hashes':[digest(vs[i]) for i in left[a:b]],'total':len(left),'requires_manual_confirmation':True})
