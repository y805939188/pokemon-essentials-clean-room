from pathlib import Path
import json,subprocess,hashlib,gzip,re
R=Path('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'); T=R/'tasks/handoff_preparation_cloud'; C='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'
def git(*a):return subprocess.check_output(['git',*a])
def read(c,p):return git('show',c+':'+p)
rs=json.loads((R/'delegation/readsets/handoff_preparation_cloud.complete.json').read_text());su=json.loads((R/'delegation/handoff-preparation-mandatory-supplement.v1.json').read_text()); ledger=[];docs=[]
for phase,rows in [('original',rs['files']),('successor',su['complete_successor_inputs'])]:
 for x in rows:
  c=x.get('commit',C);p=x['path'] if phase=='original' else str(R/x['path']);b=read(c,p); actual={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':git('hash-object','--stdin').decode().strip() if False else hashlib.sha1(('blob '+str(len(b))+'\0').encode()+b).hexdigest(),'mode':git('ls-tree',c,'--',p).decode().split()[0]}
  assert all(actual[k]==x[k] for k in actual),(phase,p,actual,x)
  ledger.append({'phase':phase,'commit':c,'tree':git('rev-parse',c+'^{tree}').decode().strip(),'path':p,**actual,'transport':'git object complete','semantic_status':'PENDING_READING'})
  try:d=json.loads(b)
  except ValueError:d={'complete_text':b.decode()}
  docs.append({'phase':phase,'path':p,'content':d})
(T/'reading-ledger').mkdir(exist_ok=True); (T/'audit').mkdir(exist_ok=True)
with gzip.open(T/'audit/exact-inputs.json.gz','wb') as f:f.write(json.dumps(docs,ensure_ascii=False,separators=(',',':')).encode())
(T/'reading-ledger/input-identities.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
# Content-addressed, lossless typed node graph. The reader receives unique semantic values;
# identity-only strings are separately mechanically verified, with complete paths retained.
seen={}; nodes=[]; root=[]
def intern(v):
 s=json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'));h=hashlib.sha256(s.encode()).hexdigest()
 if h in seen:return seen[h]
 n=len(nodes);seen[h]=n;nodes.append(None)
 if isinstance(v,dict):o={'object':{k:intern(x) for k,x in v.items()}}
 elif isinstance(v,list):o={'array':[intern(x) for x in v]}
 else:o={'value':v}
 nodes[n]=o;return n
for d in docs:root.append({'phase':d['phase'],'path':d['path'],'node':intern(d['content'])})
(T/'audit/typed-input-graph.json').write_text(json.dumps({'roots':root,'nodes':nodes},ensure_ascii=False,separators=(',',':'))+'\n')
print('verified',len(ledger),'payloads','unique nodes',len(nodes),'strings',sum(isinstance(x.get('value'),str) for x in nodes))
print('graph bytes',(T/'audit/typed-input-graph.json').stat().st_size)
# Operative root contracts: strip repeated byte identities only for reading view, never from artifacts.
d=json.loads(read(C,str(R/'adjudication/root-decisions.partial.json')))
identity={'repo','commit','tree','mode','blob','bytes','sha256','binding_validation','fixed_B8','fixed_R','fixed_R_tree','fixed_formal_tree'}
def view(v):
 if isinstance(v,dict):return {k:view(x) for k,x in v.items() if k not in identity}
 if isinstance(v,list):return [view(x) for x in v]
 return v
for i,rec in enumerate(d['records']):
 (T/'reading-ledger'/f'record-{i:02}.json').write_text(json.dumps(view(rec),ensure_ascii=False,separators=(',',':'))+'\n')
print('records reading chars',sum(p.stat().st_size for p in (T/'reading-ledger').glob('record-*.json')))
