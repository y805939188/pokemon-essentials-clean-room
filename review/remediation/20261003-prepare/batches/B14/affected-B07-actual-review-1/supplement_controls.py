# New selected fixed-control documentation bookkeeping only.
import json,pathlib,subprocess,hashlib
D=pathlib.Path(__file__).parent;O='93e10babe0b9c9ef8b3f5277754541b447beeeb4';B='1e6b11a47370f1c7c4659a32443fc1afda597bac';P='41fffb540c6483f5296ea0d33b789b75180d27ed';ROOT='review/global-independent-review/2026-10-03-fd82a639/'
def get(c,p):return subprocess.check_output(['git','show',c+':'+p])
orig=json.loads(get(O,ROOT+'findings.json'));ids=[x['id'] for x in json.loads(get('d48197f365c39925f795c1d325988c0d74e59979','review/remediation/20261003-prepare/batches/B14/integration-stage-1/finding-registration.json'))['dispositions']];selected=[x for x in orig if x['id'] in ids];raw=set()
for x in selected:
 for z in x.get('raw_reports',[])+x.get('root_adjudications',[]):
  if isinstance(z,dict):raw.add(z.get('raw_id'))
 for z in x.get('extensions',[]):raw.add(z.get('raw_id'))
inputs=[]
for p in ['root/adjudication-log.json','root/extension-adjudications.json']:
 v=json.loads(get(O,ROOT+p));items=v.get('adjudications',[]) if isinstance(v,dict) else v
 for n,x in enumerate(items):
  if x.get('raw_id') in raw or any(i in json.dumps(x) for i in ids):inputs.append((O,ROOT+p,'/adjudications/'+str(n),x))
for p,k in [('agents/B/X-B-C06-RECHECK/findings-review.json','items'),('agents/A/X-A-C05-RECHECK/recheck.json','rechecks')]:
 v=json.loads(get(O,ROOT+p))
 for key in ['scope','retained_boundaries','protected_boundaries']: 
  if key in v:inputs.append((O,ROOT+p,'/'+key,v[key]))
 for n,x in enumerate(v[k]):
  if x.get('id') in ['RUN-C-003','RUN-C-006','RUN-C-007','RUN-C-090','RUN-C-092','RUN-C-094']:inputs.append((O,ROOT+p,'/'+k+'/'+str(n),x))
p='review/remediation/20261003-prepare/batches/B07/integration-stage-1/finding-registration.json';v=json.loads(get(B,p))
for n,x in enumerate(v['dispositions']):
 if x['id']=='GIR-FD82-C003':inputs.append((B,p,'/dispositions/'+str(n),x))
known={}
for name in ['primary-controls','gate','bounded-formal']:
 for i,x in enumerate(json.loads((D/(name+'-values.json')).read_text())):known.setdefault(type(x['value']).__name__+':'+json.dumps(x['value'],ensure_ascii=False,separators=(',',':')),{'corpus':name,'value_index':i})
vals=[];maps=[]
def walk(x,ctx):
 if isinstance(x,dict):return {'dict':[[k,walk(z,ctx+'/'+k)] for k,z in x.items()]}
 if isinstance(x,list):return {'list':[walk(z,ctx+'/'+str(i)) for i,z in enumerate(x)]}
 key=type(x).__name__+':'+json.dumps(x,ensure_ascii=False,separators=(',',':'))
 if key in known:return {'reuse':known[key],'value_sha256':hashlib.sha256(key.encode()).hexdigest()}
 i=len(vals);vals.append({'type':type(x).__name__,'value':x,'context':ctx});known[key]={'corpus':'supplement','value_index':i};return {'value':i}
for c,p,selector,x in inputs:
 b=get(c,p);maps.append({'commit':c,'path':p,'selector':selector,'full_file_sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'structure':walk(x,c+':'+p+selector)})
(D/'supplement-controls-values.json').write_text(json.dumps(vals,ensure_ascii=False)+'\n');(D/'supplement-controls-structure.json').write_text(json.dumps(maps,ensure_ascii=False)+'\n');print('SUPPLEMENT',len(inputs),'complete selected fixed objects; novel',len(vals))
for i,x in enumerate(vals):
 if isinstance(x['value'],str) and (len(x['value'])>45 or any(ord(c)>127 for c in x['value'])):print(i,'/'.join(x['context'].split('/')[-3:]),json.dumps(x['value'],ensure_ascii=False))
