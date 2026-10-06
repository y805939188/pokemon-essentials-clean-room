"""New review bookkeeping only: fixed Git text/JSON/hash/range inventory; no behavior execution."""
import subprocess, json, hashlib, pathlib, sys, re
OUT = pathlib.Path(__file__).parent
ACT = 'd48197f365c39925f795c1d325988c0d74e59979'
PRE = '1e6b11a47370f1c7c4659a32443fc1afda597bac'
C3 = 'c06db6cd964188b3c693a9b7820e3a8aaffe0b04'
ORIG = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
BASE = 'review/remediation/20261003-prepare/batches/'
def git(*args): return subprocess.check_output(['git', *args])
def blob(c,p): return git('show', c+':'+p)
def obj(c,p): return json.loads(blob(c,p))
def save(n,x): (OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ident(c,p):
 d=blob(c,p)
 return {'commit':c,'path':p,'git_blob':git('rev-parse',c+':'+p).decode().strip(),'sha256':hashlib.sha256(d).hexdigest(),'bytes':len(d)}
def inputs(group):
 if group=='controls':
  ids=json.loads((OUT/'control-selection.json').read_text())['ids']
  a=obj(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json')
  q=obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
  return [(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json', '/'+str(i),x) for i,x in enumerate(a) if x['id'] in ids]+[(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json','/'+i,q[i]) for i in ids]
 if group=='owner':
  return [(PRE,BASE+'B02/integration-stage-1/'+p,'',obj(PRE,BASE+'B02/integration-stage-1/'+p)) for p in ['finding-registration.json','integration-manifest.json']]
 if group=='registration':
  return [(ACT,BASE+'B14/integration-stage-1/'+p,'',obj(ACT,BASE+'B14/integration-stage-1/'+p)) for p in ['finding-registration.json','clause-location-bindings.json','scope-and-observation-registration.json','pre-freeze-navigation-correction.json','boundary-and-bindings.json','source-lineage.json','source-limits.json']]
 raise ValueError(group)
def pool(group):
 values=[]; byval={}; mapping=[];structures=[]
 def walk(v,p,c,f):
  if isinstance(v,(dict,list)):
   structures.append({'commit':c,'path':f,'pointer':p,'kind':type(v).__name__,'members':list(v) if isinstance(v,dict) else len(v)})
   for k,z in (v.items() if isinstance(v,dict) else enumerate(v)):walk(z,p+'/'+str(k).replace('~','~0').replace('/','~1'),c,f)
  else:
   s=json.dumps(v,ensure_ascii=False,separators=(',',':'));h=hashlib.sha256(s.encode()).hexdigest()
   if s not in byval:byval[s]=len(values);values.append({'value':v,'first':c+':'+f+'#'+p,'sha256':h})
   mapping.append({'commit':c,'path':f,'pointer':p,'value_index':byval[s]})
 for c,f,p,v in inputs(group):walk(v,p,c,f)
 return values,mapping,structures
if __name__=='__main__':
 mode=sys.argv[1]
 if mode=='pool':
  group=sys.argv[2];values,mapping,structures=pool(group)
  save(group+'-structure-map.json',structures);save(group+'-value-map.json',{'policy':'Values retained at exact fixed Git object/pointer; no summaries. SHA256 is canonical JSON scalar identity, not semantic approval. Display ranges separately recorded.','values':[{'index':i,'first':v['first'],'sha256':v['sha256'],'characters':len(str(v['value']))} for i,v in enumerate(values)],'mappings':mapping})
  print('values',len(values),'strings',sum(isinstance(x['value'],str) for x in values),'long',sum(isinstance(x['value'],str) and len(x['value'])>=100 for x in values))
 elif mode=='values':
  group=sys.argv[2];start=int(sys.argv[3]);stop=int(sys.argv[4]);kind=sys.argv[5] if len(sys.argv)>5 else 'all'
  vals=pool(group)[0]
  indices=[i for i,v in enumerate(vals) if kind=='all' or (isinstance(v['value'],str) and len(v['value'])>=100) if True]
  for ix in indices[start:stop]:
   v=vals[ix];print('VALUE',ix,v['first']);print(json.dumps(v['value'],ensure_ascii=False))
  print('DISPLAYED_INDEX_RANGE',start,stop,'of',len(indices),'kind',kind)
 elif mode=='text':
  c,p,start,stop=sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]);lines=blob(c,p).decode().splitlines()
  for i in range(start-1,min(stop,len(lines))):print(str(i+1)+': '+lines[i])
  print('TOTAL_LINES',len(lines))

def novel_prejudgment():
 known={json.dumps(x['value'],ensure_ascii=False) for x in pool('controls')[0]}; vals=[];seen=set()
 deferred={'author_record','full_candidate_disposition','candidate_AREG_overlay_records','C3_successor','positive_reverse_designs','current_locator_derivation','current_locator_quality','writer_validation'}
 def walk(v,where):
  if isinstance(v,dict):
   for k,x in v.items():
    if k not in deferred:walk(x,where+'/'+k)
  elif isinstance(v,list):
   for i,x in enumerate(v):walk(x,where+'/'+str(i))
  elif isinstance(v,str):
   try:z=json.loads(v)
   except ValueError:z=None
   if isinstance(z,(list,dict)):walk(z,where+'/EMBEDDED_JSON');return
   if json.dumps(v,ensure_ascii=False) in known or v in seen:return
   seen.add(v)
   if not re.fullmatch(r'[a-f0-9]{40}|[a-f0-9]{64}',v) and not v.startswith(('review/','deliverables/','specs/','Data/','PBS/','http')):vals.append({'value':v,'pointer':where})
 for group in ['owner','registration']:
  for c,f,ptr,v in inputs(group):walk(v,group+':'+f+'#'+ptr)
 return vals
if __name__=='__main__' and sys.argv[1]=='novel':
 vals=novel_prejudgment();a=int(sys.argv[2]);b=int(sys.argv[3])
 for i in range(a,min(b,len(vals))):print(i,json.dumps(vals[i]['value'],ensure_ascii=False))
 print('RANGE',a,b,'TOTAL',len(vals))
