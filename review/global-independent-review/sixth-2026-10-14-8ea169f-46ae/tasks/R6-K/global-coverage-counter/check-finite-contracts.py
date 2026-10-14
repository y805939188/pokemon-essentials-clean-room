from pathlib import Path
import json,gzip,hashlib,collections,datetime
P=Path(__file__).parent;B=P.parents[2];W=Path.cwd();REF='reference/pokemon-essentials/'
def get(p):return json.loads((B/p).read_text())
def put(p,x):(P/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
ri={REF+x['path']:x for x in get('inventory/reference.json')};fi={x['path']:x for x in get('inventory/formal131.json')};bad=[]
def cite(r,where):
 p=r.get('path');p=REF+p if p and p.startswith(('Data/','PBS/','Text_english_core/')) else p
 rs=r.get('lines',[r.get('start_line'),r.get('end_line')]);a,b=rs if isinstance(rs,list)and len(rs)==2 else(None,None)
 iv=ri.get(p,fi.get(p))
 if not(iv and isinstance(a,int)and isinstance(b,int)and 1<=a<=b<=iv.get('lines',0)):bad.append({'where':where,'citation':r})
meta=get('tasks/R6-D/pbs-bulk/source-to-spec-matrix.json');bulk=json.loads(gzip.decompress((B/'tasks/R6-D/pbs-bulk'/meta['artifact']).read_bytes()));rules=get('tasks/R6-D/pbs-bulk/field-semantic-rules.json');rb={x['rule_id']:x for x in rules};heads={x['header_rule_id']:x for x in get('tasks/R6-D/pbs-bulk/header-contracts.json')};bulkissues=[];fc=collections.Counter();paths=collections.Counter()
for n,r in enumerate(bulk):
 paths[r['path']]+=1;cite(r,'bulk:'+str(n))
 if r['header_rule_id']not in heads:bulkissues.append({'record':n,'reason':'header rule unavailable'})
 if not r.get('profile_premise')or not r.get('field_applications'):bulkissues.append({'record':n,'reason':'missing premise or field applications'})
 for f in r['field_applications']:
  rid=f['rule_id'];fc[f['author_input']]+=1
  if rid not in rb:bulkissues.append({'record':n,'rule':rid,'reason':'field rule unavailable'});continue
  q=rb[rid]
  if not q.get('premises')or not q.get('necessary_consumers')or not q.get('formal_clauses'):bulkissues.append({'record':n,'rule':rid,'reason':'manual rule missing explicit premise/consumer/formal clause'})
for q in rules:
 for k in ['schema_source','normalization_source','formal_clauses']:
  for c in q.get(k,[]):cite(c,q['rule_id']+'/'+k)
 if q.get('constructor_source'):cite(q['constructor_source'],q['rule_id']+'/constructor')
 for c in q.get('necessary_consumers',[]):
  if isinstance(c.get('location'),dict):cite(c['location'],q['rule_id']+'/consumer')
# All29 special PBS finite record/field relations under15 manually authored rules.
special=[json.loads(z)for z in(B/'tasks/R6-D/source-to-spec-matrix.jsonl').read_text().splitlines()if z.strip()];specialrules=get('tasks/R6-D/manual-rule-catalog.json');specialissues=[];specialpaths=collections.Counter()
for n,r in enumerate(special):
 specialpaths[r['source']['path']]+=1;cite(r['source'],'special:'+str(n))
 if not r.get('fact')or not r.get('premise')or not r.get('consumer_locations')or not r.get('formal_locations'):specialissues.append({'row':n,'reason':'missing explicit rule fact/premise/consumer/formal'})
 for c in r['consumer_locations']+r['formal_locations']:cite(c,'special-consumer-formal:'+str(n))
# All localized record facts/consumer/formal and semantic-unit acceptance, distinct from raw line presentation.
local=get('tasks/R6-D/localization/source-to-formal.json');facts={x['id']:x for x in get('tasks/R6-D/localization/facts.json')};localissues=[];lpaths=collections.Counter();accepted=collections.defaultdict(set)
ledgers=[B/'tasks/R6-D/localization/reading-ledger.jsonl',B/'tasks/R6-D/localization/pokedex/reading-ledger.jsonl']
for p in ledgers:
 for s in p.read_text().splitlines():
  if not s.strip():continue
  x=json.loads(s);path=x.get('path');rg=x.get('unit_range');ex=x.get('review_extent','')
  if path and rg and 'structure'not in ex and 'semantic'in ex:
   accepted[path].update(range(rg[0],rg[1]+1))
  if path and isinstance(x.get('unit_ids'),list)and ('semantic'in ex):accepted[path].update(x['unit_ids'])
for n,r in enumerate(local):
 p=r['source']['path'];lpaths[p]+=1;cite(r['source'],'localized:'+str(n));cite(r['consumer'],'localized-consumer:'+str(n))
 for f in r['formal']:cite(f,'localized-formal:'+str(n))
 if r.get('semantic_status')!='read_this_round' or not r.get('consumer_prerequisites')or not r.get('facts')or not all(x in facts for x in r['facts']):localissues.append({'row':n,'unit':r['unit'],'reason':'missing current semantic acceptance or actual fact/consumer premise'})
# Acceptance origin IDs are record offsets, never game identities. Preserve per-path deficits for exact evidence audit.
deficits=[]
for path,count in lpaths.items():
 missing=sorted(set(range(count))-accepted[path])
 if missing:deficits.append({'path':path,'records':count,'missing_unit_acceptance_ids':missing})
# Every finite font/BMP unit and forward fact has an existing artifact/JSON pointer; asset source point counts are byte intervals.
fu=get('tasks/R6-D/fonts/source-unit-matrix.json');ft=get('tasks/R6-D/fonts/traceability.json');fontissues=[]
for u in fu['units']:
 ev=u.get('evidence');p=(B/'tasks/R6-D/fonts'/ev.split('#',1)[0])if isinstance(ev,str)else None
 if not p or not p.is_file():fontissues.append({'unit':u['unit'],'reason':'evidence artifact absent'})
for f in ft['forward']:
 if not f.get('fact')or not f.get('consumer')or not f.get('formal'):fontissues.append({'unit':f.get('unit'),'reason':'fact/consumer/formal missing'})
 for c in f.get('consumer',[])+f.get('formal',[]):cite(c,'font-trace:'+str(f.get('unit')))
s={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'special_units':len(special),'special_paths':len(specialpaths),'special_manual_rules':len(specialrules),'special_missing_fact_premise_consumer_formal':specialissues,'bulk_records':len(bulk),'bulk_paths':len(paths),'bulk_rules':len(rb),'bulk_header_rules':len(heads),'bulk_actual_application_modes':dict(fc),'bulk_missing_rule_or_premise_consumer_joins':bulkissues,'localization_records':len(local),'localization_paths':len(lpaths),'localization_fact_families':len(facts),'localization_missing_current_semantic_fact_consumer_joins':localissues,'localization_unit_acceptance_deficits':deficits,'font_bitmap_units':len(fu['units']),'font_bitmap_forward_facts':len(ft['forward']),'font_bitmap_missing_evidence_fact_consumer':fontissues,'invalid_citations':bad,'qualification':'Complete finite traversal of current author-rule/record/consumer receipts. Not new K manual reading of every repeated data row, not original parser/reference gameplay execution, not host/native approval.'}
put('finite-contract-special-path-counts.json',dict(specialpaths));put('finite-contract-summary.json',s);put('finite-contract-bulk-path-counts.json',dict(paths));put('finite-contract-local-path-counts.json',dict(lpaths));print(json.dumps({k:v for k,v in s.items()if k!='localization_unit_acceptance_deficits'},ensure_ascii=False));print('acceptance deficits',[(x['path'],len(x['missing_unit_acceptance_ids']))for x in deficits])
