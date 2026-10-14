from pathlib import Path
import json,re,hashlib,datetime,collections,csv
P=Path(__file__).parent;B=P.parents[2];W=Path.cwd();REF='reference/pokemon-essentials/'
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
cache={}
def payload(p):
 p=Path(p)
 if p not in cache:
  if p.suffix=='.jsonl':cache[p]=[json.loads(s)for s in p.read_text().splitlines()if s.strip()]
  elif p.suffix=='.json':cache[p]=json.loads(p.read_text())
  elif p.suffix=='.csv':cache[p]=list(csv.DictReader(p.open()))
  else:cache[p]=p.read_text().splitlines()
 return cache[p]
def rows(p):
 x=payload(p)
 return x if isinstance(x,list)else x.get('rows',x.get('records',[]))
def walk(x,at=''):
 if isinstance(x,dict):
  yield at,x
  for k,v in x.items():yield from walk(v,at+'/'+str(k))
 elif isinstance(x,list):
  for i,v in enumerate(x):yield from walk(v,at+'/'+str(i))
def ids(x):
 if isinstance(x,str):return set(re.findall(r'F\d{3}-C\d{4}',x))
 if isinstance(x,(dict,list)):return set().union(*(ids(v)for v in (x.values()if isinstance(x,dict)else x)))
 return set()
def pathnorm(s):
 if not isinstance(s,str):return None
 if s.startswith(str(W)+'/'):s=s[len(str(W))+1:]
 if s.startswith(('Data/','PBS/','Text_english_core/','Fonts/')):s=REF+s
 return s
inv={REF+x['path']:x for x in payload(B/'inventory/reference.json')};forms={x['path']:x for x in payload(B/'inventory/formal131.json')}
def rng(x):
 for a,b in [('start_line','end_line'),('start','end'),('start','end_envelope')]:
  if isinstance(x.get(a),int)and isinstance(x.get(b),int):return [x[a],x[b]]
 for k in ['lines','range','spec_lines','formal_lines','matched_formal_lines']:
  r=x.get(k)
  if isinstance(r,list)and len(r)==2 and all(isinstance(v,int)for v in r):return r
 if isinstance(x.get('line'),int):return [x['line'],x['line']]
 return None
den=payload(B/'inventory/formal-block-denominator.json');glob=payload(B/'coverage/global-reverse-block-index.json');dby={x['id']:x for x in den}
blockchecks=[];badroot=[];badrow=[];allmat=set()
for b in glob:
 identity=b['id']in dby and all(b[k]==dby[b['id']][k]for k in ['path','start_line','end_line'])
 ev=[]
 for e in b['domain_evidence']:
  fp=B/e['matrix'];allmat.add(fp)
  if not fp.is_file():ev.append({'entry':e,'valid':False,'reason':'matrix missing'});continue
  n=e.get('row')
  if not n:
   valid=e['matrix']=='tasks/R6-H/report.md' and b['path']in ['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md']
   ev.append({'entry':e,'valid':valid,'kind':'NAMED_FULLTEXT_SHARED_SCOPE_DISPOSITION'});continue
  rr=rows(fp);valid=isinstance(n,int)and 1<=n<=len(rr)
  if not valid:ev.append({'entry':e,'valid':False,'reason':'row out of bounds'});continue
  r=rr[n-1]
  if fp.suffix=='.md':valid=bool(r.strip().startswith('|'))
  elif b['id']in ids(r):valid=True
  else:
   q=r.get('formal_path',r.get('path',r.get('spec_path',r.get('formal'))))if isinstance(r,dict)else None
   if isinstance(q,dict):q=q.get('path')
   a=rng(r)if isinstance(r,dict)else None
   if not a and isinstance(r,dict)and isinstance(r.get('line'),int):a=[r['line'],r['line']]
   valid=q==b['path']and a and a[0]<=b['end_line']and b['start_line']<=a[1]
  ev.append({'entry':e,'valid':bool(valid),'kind':'EXACT_RECOVERABLE_ROW_OR_FINITE_LINE_BRIDGE'})
  if not valid:badrow.append({'block':b['id'],'matrix':e['matrix'],'row':n,'reason':'neither current block ID nor correct exact formal path/range'})
 blockchecks.append({'id':b['id'],'path':b['path'],'lines':[b['start_line'],b['end_line']],'denominator_identity_matches':identity,'recoverable_evidence':ev,'named_index_not_semantic_pass':True})
 if not identity:badroot.append(b['id'])
# independently check immutable snapshots/current material hashes and indexed matrix snapshots.
cat=payload(B/'coverage/matrix-catalog.json');stale=[];missingcat=[]
for c in cat:
 p=B/c['path']
 if not p.exists():missingcat.append(c['path']);continue
 h=hashlib.sha256(p.read_bytes()).hexdigest()
 if c['sha256']!=h or c['bytes']!=p.stat().st_size:stale.append({'path':c['path'],'indexed_sha256':c['sha256'],'current_sha256':h,'indexed_bytes':c['bytes'],'current_bytes':p.stat().st_size})
# Walk actual maps, including their own named child artifacts; source and formal citations are validated as pointers.
allmat.update(B/c['path']for c in cat if (B/c['path']).exists()and (B/c['path']).suffix in ['.json','.jsonl'])
allmat.update([B/'tasks/R6-F/safari/forward-matrix.json',B/'tasks/R6-K/context-116-joins.json',B/'tasks/R6-H/subtasks/supplement-inventory/specs113-primary-matrix.json',B/'tasks/R6-H/subtasks/supplement-inventory/effective-supplement116.json'])
sourcepoints=[];invalid=[];childissues=[];childseen=set();queue=list(allmat)
while queue:
 fp=queue.pop()
 if fp in childseen:continue
 childseen.add(fp)
 for at,x in walk(payload(fp)):
  path=pathnorm(x.get('path',x.get('source_path',x.get('source') if isinstance(x.get('source'),str) else x.get('formal_path',x.get('spec_path')))))
  rr=x.get('source_lines') if x.get('source_path') else rng(x)
  if path and rr and path.startswith(REF):
   if path not in inv:invalid.append({'artifact':str(fp.relative_to(B)),'json_pointer':at,'path':path,'range':rr,'reason':'not in fixed R432 inventory'})
   elif inv[path]['type']=='text'and not(1<=rr[0]<=rr[1]<=inv[path]['lines']):invalid.append({'artifact':str(fp.relative_to(B)),'json_pointer':at,'path':path,'range':rr,'total_lines':inv[path].get('lines'),'reason':'source range out of fixed physical bounds'})
   else:sourcepoints.append({'artifact':str(fp.relative_to(B)),'json_pointer':at,'path':path,'range':rr,'exact_source_pointer_not_behavior_pass':True})
  for k in ['artifact','origin_artifact','matrix','receipt']:
   pp=x.get(k)
   if not isinstance(pp,str)or not pp.endswith(('.json','.jsonl','.csv'))or ' / 'in pp or '\n'in pp:continue
   candidates=[Path(pp),fp.parent/pp,B/pp]
   found=[p for p in candidates if p.is_file()]
   if not found:continue # free prose/foreign receipt identifiers are separately retained, not coerced into a file pointer
   target=found[0].resolve()
   n=x.get('row',x.get('record',x.get('origin_record')))
   if isinstance(n,int):
    rrs=rows(target)
    if not(1<=n<=len(rrs)):childissues.append({'artifact':str(fp.relative_to(B)),'json_pointer':at,'target':str(target),'row':n,'rows':len(rrs),'reason':'child record out of bounds'})
   if target.resolve().is_relative_to(B.resolve()):queue.append(target)
by=collections.defaultdict(list)
for x in sourcepoints:by[x['path']].append(x)
no_source=[{'path':p,'type':x['type'],'reason':'No exact source-line citation found in current maps; binary/type/metadata disposition must be checked separately, not automatically behavior absent.'}for p,x in inv.items()if not by[p]]
# Current116 rows must truly resolve to matching current manual parents and correct formal line/hash.
j=payload(B/'tasks/R6-K/context-116-joins.json');uu={x['id']:x for x in payload(B/'tasks/R6-K/named-review-units.json')};ctxbad=[]
for v in j['vectors']:
 s=Path(v['formal_path']).read_text().splitlines()[v['formal_line']-1]
 if hashlib.sha256(s.encode()).hexdigest()!=v['row_sha256'] or not all(i in uu and 'PENDING'not in uu[i]['status'] for i in v['primary_unit_ids']):ctxbad.append(v['id'])
put('formal-block-recovery-checks.json',blockchecks);put('source-pointer-index.json',sourcepoints);put('invalid-source-pointers.json',invalid);put('child-record-pointer-issues.json',childissues);put('stale-matrix-snapshots.json',stale);put('source-files-without-line-citations.json',no_source)
s={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'formal_denominator':len(den),'current_index_blocks':len(glob),'duplicate_or_missing_block_ids':sorted(set(dby)-{x['id']for x in glob}),'identity_errors':badroot,'unrecoverable_index_evidence_entries':badrow,'blocks_without_recoverable_entry':[x['id']for x in blockchecks if not any(e['valid']for e in x['recoverable_evidence'])],'catalog_entries':len(cat),'catalog_missing_payloads':missingcat,'stale_matrix_snapshots':stale,'visited_map_artifacts':len(childseen),'exact_source_pointer_records':len(sourcepoints),'invalid_source_pointers':len(invalid),'child_record_pointer_issues':len(childissues),'source_files_without_line_citations':no_source,'context116_rows':len(j['vectors']),'context116_unresolved':ctxbad,'semantic_consistency_not_inferred_from_mechanical_check':True}
put('mapping-summary.json',s)
print(json.dumps({k:v for k,v in s.items()if k not in ['source_files_without_line_citations','stale_matrix_snapshots','unrecoverable_index_evidence_entries']},ensure_ascii=False));print('STALE',[x['path']for x in stale]);print('NO SOURCE',no_source);print('BAD ROW',badrow[:8]);print('INVALID',invalid[:12]);print('CHILD',childissues[:12])
