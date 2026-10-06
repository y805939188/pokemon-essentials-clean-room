"""New reviewer document, JSON, pointer, order and diff bookkeeping. No behavior execution."""
import pathlib,json,hashlib,subprocess,re,csv,io,sys,functools
from read_bookkeeping import get,ACT,PRE,REF
from semantic_bookkeeping import pool,ORIG,PLAN
from completion_reading import audit_units,formal_units,scalar_key,FLAGS,metadata
D=pathlib.Path(__file__).parent
G='review/remediation/20261003-prepare/batches/B14/integration-stage-1/'
C3='c06db6cd964188b3c693a9b7820e3a8aaffe0b04'
@functools.lru_cache(None)
def obj(c,p):return json.loads(get(c,p))
@functools.lru_cache(None)
def audit_object(p):
 b=get(ACT,p).decode()
 return json.loads(b) if p.endswith('.json') else ([json.loads(x) for x in b.splitlines() if x] if p.endswith('.jsonl') else b.splitlines(keepends=True))
def ptr(o,p):
 for k in p.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');o=o[int(k)] if isinstance(o,list) else o[k]
 return o
def loc(x):return ptr(obj(x['source']['commit'],x['source']['path']),x['selector'])
def sha(v):return hashlib.sha256(scalar_key(v).encode()).hexdigest()
def save(p,o):(D/p).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def verify():
 checks=[]
 def ck(n,v,count=None):
  checks.append(dict(check=n,passed=bool(v),count=count));assert v,n
 for mode in ['controls','owner']:
  vals,maps=pool(mode);stored=json.loads((D/(mode+'-lossless-map.json')).read_text())
  ck(mode+' full ordered map regeneration',maps==stored['structures'],len(maps))
  ck(mode+' all typed leaf mappings',stored['unique_values']==[{k:v for k,v in x.items() if k!='value'} for x in vals],len(vals))
 m=obj(ACT,G+'control-reading-map.json');ss=m['scalar_source_selectors'];vs=[loc(x) for x in ss]
 ck('G control scalar first selectors unique',len({scalar_key(x) for x in vs})==len(vs),len(vs))
 ck('G control aliases exact type and value',all(scalar_key(loc(x))==scalar_key(vs[x['value_index']]) for x in m['aliases']),len(m['aliases']))
 ck('G control structures exact kind and ordered children',all(type(loc(x)).__name__==x['kind'] and (list(loc(x)) if isinstance(loc(x),dict) else list(range(len(loc(x)))))==x['children'] for x in m['structures']),len(m['structures']))
 generated_s=[];generated_a=[]
 def walk(o,s,p):
  if isinstance(o,(dict,list)):
   ks=list(o) if isinstance(o,dict) else list(range(len(o)));generated_s.append((s,p,type(o).__name__,ks))
   for k in ks:walk(o[k],s,p+'/'+str(k).replace('~','~0').replace('/','~1'))
  else:generated_a.append((s,p))
 for x in m['inputs']:walk(ptr(obj(x['commit'],x['path']),x['selector']),dict(commit=x['commit'],path=x['path']),x['selector'])
 ck('G map covers every input container and leaf in native order',generated_s==[(x['source'],x['selector'],x['kind'],x['children']) for x in m['structures']] and generated_a==[(x['source'],x['selector']) for x in m['aliases']],len(m['inputs']))
 vals,files,schemas,counts=audit_units();stored=json.loads((D/'completion-audit-map.json').read_text())
 ck('Entire audit corpus exact file identities and schemas reproducible',[(x['path'],x['bytes'],x['sha256']) for x in files]==[(x['path'],x['bytes'],x['sha256']) for x in stored['maps']] and schemas==stored['schemas'],counts['files'])
 old_units={(x['path'],x['pointer'],x['type'],x['value_sha256']):x['n'] for x in stored['semantic_units']}
 ck('Regenerated units are exact first-source subset of captured dictionary',all((x['path'],x['pointer'],x['type'],x['value_sha256']) in old_units for x in vals),len(vals))
 # A later reviewer metadata classification refinement excluded 771 identity strings.
 # Preserve the original dictionary and page numbering; verify every original value directly.
 def resolve(e):
  v=audit_object(e['path'])
  for k in e['pointer'].split('/')[1:]:
   k=k.replace('~1','/').replace('~0','~')
   if k in ['@lines','@jsonl']:continue
   if k=='@text_line':v=v.splitlines(keepends=True);continue
   if k=='@embedded_JSON':v=json.loads(v);continue
   v=v[int(k)] if isinstance(v,list) else v[k]
  return v
 ck('Every original dictionary value resolves exact type and SHA',all(type(resolve(x)).__name__==x['type'] and sha(resolve(x))==x['value_sha256'] for x in stored['semantic_units']),len(stored['semantic_units']))
 save('completion-audit-structure-successor.json',dict(ACT=ACT,original_dictionary='completion-audit-map.json',classification_refinement_only=True,original_semantic_units=len(stored['semantic_units']),refined_units=len(vals),native_order_schemas=schemas,refined_external_source_graph=files,counts=counts,values_unchanged=True,business_delivery='Original101 page numbering retained and consumed; metadata classification is not a reading claim'))
 f,b=formal_units();ck('Formal outer hunk dictionary and all sign/order relationships reproducible',json.loads((D/'completion-formal-map.json').read_text())['maps']==b,len(b))
 # Current registration relationships: independently evaluate the exact objects, not writer labels.
 reg=obj(ACT,G+'finding-registration.json');nav=obj(ACT,G+'clause-location-bindings.json');bound=obj(ACT,G+'boundary-and-bindings.json');rs=reg['dispositions']
 ck('24 ordered contribution keys and 19 primary/5 shared',len(rs)==24 and len({r['record_key'] for r in rs})==24 and sum(r['primary'] for r in rs)==19 and all(r['record_key']=='B14/'+r['id'] for r in rs),24)
 ck('Canonical OPEN and actual/acceptance pending',all(r['canonical_state']=='OPEN' and not r['accepted_B14_contribution'] and not r['closure_authorized'] for r in rs))
 for r in rs:
  original=loc(dict(source={k:r['original'][k] for k in ['commit','path']},selector=r['original']['selector']))
  accepted=loc(dict(source={k:r['approved_acceptance'][k] for k in ['commit','path']},selector=r['approved_acceptance']['selector']))
  canonical=lambda v:hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  ck(r['id']+' complete original/PLAN object binding',original['id']==accepted['id']==r['id'] and canonical(original)==r['whole_original_object_sha256'] and canonical(accepted)==r['whole_acceptance_object_sha256'])
  ck(r['id']+' current qualifications and acceptance projections',all(original[k]==v for k,v in r['complete_current_control_fields'].items()) and all(accepted[k]==v for k,v in r['complete_minimum_acceptance_fields'].items()))
  ck(r['id']+' current navigation mirror',r['current_formal_locations']==nav['records'][r['id']]['current_formal_locations'])
  ck(r['id']+' all eight candidate receipts separately bound',[(x['owner'],x['report_commit'],x['reviewed_candidate']) for x in r['candidate_receipts']]==[(x['owner'],x['report_commit'],C3) for x in bound['report_bindings']])
  for row in r['current_test_rows']:
   raw=get(ACT,row['path']).splitlines(keepends=True)[row['line']-1]
   ck(r['id']+'/'+row['id']+' precise current row bytes',hashlib.sha256(raw).hexdigest()==row['row_sha256'] and len(raw)==row['row_bytes'] and re.match(rb'^\|\s*'+row['id'].encode()+rb'\s*\|',raw) is not None)
 for path in bound['public_paths']:
  old=get(PRE,path);now=get(ACT,path)
  if path.endswith('.tsv'):
   table=csv.DictReader(io.StringIO(now.decode()),delimiter='\t');cols=table.fieldnames;rows=list(table)
   ck(path+' accepted full prefix/schema/194 records',now.startswith(old) and cols==next(csv.reader(io.StringIO(old.decode()),delimiter='\t')) and len(rows)==194)
   ck(path+' appended IDs/order', [r['finding_id'] for r in rows[170:]]==[r['id'] for r in rs])
   for row,r in zip(rows[170:],rs):
    obligations=json.loads(row['remaining_obligations']);ck(path+'/'+r['id']+' current locator obligation',obligations['current_clause_bindings']==G+'clause-location-bindings.json#records/'+r['id'])
    if 'current_clause_inputs' in row:ck(path+'/'+r['id']+' formal locator mirror',json.loads(row['current_clause_inputs'])['formal']==r['current_formal_locations'])
 # Full unfiltered streams regenerated to verify the immutable inventories and outer block path relations.
 diffs=[]
 for start in [PRE,C3]:
  data=subprocess.check_output(['git','diff',*FLAGS,start,ACT]);blocks=[x for x in re.split(rb'(?=^diff --git )',data,flags=re.M) if x]
  diffs.append(dict(from_commit=start,to_commit=ACT,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),flags=FLAGS,path_filter=None,paths=[x.split(b' b/',1)[1].split(b'\n',1)[0].decode() for x in blocks]))
 ck('Exact complete unfiltered stream identities',[(x['bytes'],x['sha256']) for x in diffs]==[(96116311,'1f88e677993c91905b72b747b187f6e94a52881178b08716fe6791bd6cbab444'),(95127902,'5d639c30c53bb37035d2d133b715da5cc5c706afd13d278c8a7ad718368da5d9')])
 save('completion-pointer-relationship-checks.json',dict(kind='REVIEWER_DOCUMENT_METADATA_ONLY_NOT_BEHAVIOR_EVIDENCE',ACT=ACT,checks=checks,diffs=diffs,errors=[],source_execution=0,historical_program_execution=0))
 print('Complete pointer/order/type/input and current registry checks',len(checks),'passed; no behavior execution.')
def public_prepare():
 vals,_,_,_=audit_units();prior,_=pool('owner');formal,_=formal_units();seen={scalar_key(x['value']) for x in vals+prior};seen.update(scalar_key(x['value']) for x in formal)
 novel=[];mapping=[]
 def walk(v,path,p):
  if isinstance(v,dict):return {k:walk(w,path,p+'/'+k.replace('~','~0').replace('/','~1')) for k,w in v.items()}
  if isinstance(v,list):return [walk(w,path,p+'/'+str(i)) for i,w in enumerate(v)]
  key=scalar_key(v);h=sha(v)
  if key in seen:return dict(reuse='Exact typed value already consumed',sha256=h)
  seen.add(key)
  if metadata(v,p):return dict(metadata=True,sha256=h)
  n=len(novel);novel.append(dict(n=n,path=path,pointer=p,value=v));return dict(unit=n,sha256=h)
 bound=obj(ACT,G+'boundary-and-bindings.json');raw=subprocess.check_output(['git','diff',*FLAGS,PRE,ACT])
 for block in re.split(rb'(?=^diff --git )',raw,flags=re.M):
  if not block:continue
  path=block.split(b' b/',1)[1].split(b'\n',1)[0].decode()
  if path not in bound['public_paths']:continue
  if path.endswith('.tsv'):
   now=list(csv.DictReader(io.StringIO(get(ACT,path).decode()),delimiter='\t'))[170:]
   for row in now:
    for k,v in list(row.items()):
     if v.lstrip().startswith(('{','[')):
      try:row[k]={'exact_encoded_string_sha256':sha(v),'parsed_relationships':json.loads(v)}
      except ValueError:pass
   graph=walk(now,path,'/pending_rows')
  else:
   graph=walk([line.decode() for line in block.splitlines(keepends=True) if line[:1] in b'+- ' and not line.startswith((b'+++',b'---'))],path,'/outer_diff_body')
  mapping.append(dict(path=path,outer_diff_bytes=len(block),outer_diff_sha256=hashlib.sha256(block).hexdigest(),graph=graph))
 save('completion-public-map.json',dict(ACT=ACT,full_unfiltered_acquisition=True,mechanical_metadata_not_semantic_proof=True,ordered_relationships=mapping,novel_values=novel))
 print('Public complete outer-block relationships',len(mapping),'novel semantic units',len(novel),'characters',sum(len(str(x['value'])) for x in novel))
if __name__=='__main__':
 if sys.argv[1]=='verify':verify()
 elif sys.argv[1]=='public':public_prepare()
 elif sys.argv[1]=='page':
  o=json.loads((D/'completion-public-map.json').read_text());a=int(sys.argv[2]);z=int(sys.argv[3]);
  for x in o['novel_values'][a:z]:print(x['n'],x['path'],x['pointer'],json.dumps(x['value'],ensure_ascii=False))
