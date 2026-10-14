"""A recoverable global index over actual domain matrices; indexing is not semantic approval."""
import collections,datetime,hashlib,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
def get(p):return json.loads((ROOT/p).read_text())
def put(p,x):(ROOT/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def rows(p):
 q=ROOT/p
 if q.suffix=='.jsonl':return [json.loads(l) for l in q.read_text().splitlines() if l.strip()]
 x=json.loads(q.read_text())
 if isinstance(x,list):return x
 return x.get('rows',x.get('records',[]))
def ids(x):
 result=set()
 if isinstance(x,str):result.update(re.findall(r'F\d{3}-C\d{4}',x))
 elif isinstance(x,dict):
  for k in ['id','block_id','clause_id','formal_clause_ids','clause_ids']:
   if k in x:result.update(ids(x[k]))
 elif isinstance(x,list):
  for y in x:result.update(ids(y))
 return result
reverse_paths=[
 'tasks/R6-K/reverse-formal-matrix.jsonl','tasks/R6-C/formal-block-matrix.jsonl',
 'tasks/R6-O/reverse-matrix.jsonl','tasks/R6-CM/formal-clause-matrix.jsonl',
 'tasks/R6-CA/reverse-matrix.jsonl','tasks/R6-UI/reverse-matrix.jsonl',
 'tasks/R6-UI/catalog-reverse-matrix.jsonl','tasks/R6-DX/reverse-matrix.json',
 'tasks/R6-F/reverse-matrix.json','tasks/R6-B/reverse-matrix.json',
]
links=collections.defaultdict(list);catalog=[]
for p in reverse_paths:
 q=ROOT/p;data=q.read_bytes();rr=rows(p)
 catalog.append({'path':p,'axis':'formal-block to actual source-fact/consumer or named nonbehavioral disposition',
                 'rows':len(rr),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                 'reading_implied_by_index':False})
 for i,row in enumerate(rr,1):
  for bid in ids(row):links[bid].append({'matrix':p,'row':i,'domain':p.split('/')[1],
       'status':row.get('status',row.get('disposition','explicit owner assessment')),
       'recover':'JSONL line '+str(i) if p.endswith('.jsonl') else 'JSON rows/records index '+str(i-1)})
blocks=get('inventory/formal-block-denominator.json')
shared={'deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md'}
# A delegated reader used exact formal line identities rather than root F-C IDs.
# Bridge these identifiers, preserving its original assessment, not assigning a new PASS.
line_rows=rows('tasks/R6-F/safari/reverse-matrix.json')
for i,row in enumerate(line_rows,1):
 path=row.get('formal_path');line=row.get('line')
 if not path or not isinstance(line,int):continue
 for b in blocks:
  if b['path']==path and b['start_line']<=line<=b['end_line']:
   links[b['id']].append({'matrix':'tasks/R6-F/safari/reverse-matrix.json','row':i,'domain':'R6-F/safari',
       'original_clause_id':row.get('clause_id'),'status':row.get('disposition'),
       'recover':'JSON /rows/'+str(i-1)+'; exact formal line identity bridge'})
variant_path='tasks/R6-F/variants/reverse-matrix.md'
section=None
for i,line in enumerate((ROOT/variant_path).read_text().splitlines(),1):
 if line=='## WP56':section='deliverables/final-specification-set/combat-requirements/wp56-palace-and-arena-variants.md'
 elif line=='## WP58':section='deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md'
 elif line.startswith('## PA'):section='deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md'
 if not section or not line.startswith('|'):continue
 cols=line.split('|')
 if len(cols)<5:continue
 cell=cols[1].strip()
 # The finite handwritten row explicitly gives the formal line(s), usually after its final comma.
 tail=cell.rsplit(',',1)[-1] if ',' in cell else cell.split('/')[0]
 ranges=[]
 for match in re.finditer(r'(?<![A-Za-z])([0-9]+)(?:[–\-]([0-9]+))?',tail):
  lo=int(match[1]);hi=int(match[2] or lo);ranges.append((lo,hi))
 for b in blocks:
  if b['path']==section and any(lo<=b['start_line']<=hi or b['start_line']<=lo<=b['end_line'] for lo,hi in ranges):
   links[b['id']].append({'matrix':variant_path,'row':i,'domain':'R6-F/variants',
       'status':'MANUAL_SOURCE_CONSUMER_PREMISE_REVIEW_ROW','recover':'Markdown line '+str(i),
       'reading_or_PASS_inferred_by_bridge':False})
manual=ROOT/'coverage/root-manual-residual-blocks.json'
if manual.exists():
 for i,row in enumerate(json.loads(manual.read_text()),1):
  links[row['id']].append({'matrix':'coverage/root-manual-residual-blocks.json','row':i,'domain':'R6-I',
      'status':row['disposition'],'recover':'JSON array index '+str(i-1)+'; actual text and exact child fact receiver retained'})
forward_paths={
 'R6-K':['tasks/R6-K/forward-source-matrix.jsonl','tasks/R6-K/named-review-units.json','tasks/R6-K/foreign-source-dispositions.json'],
 'R6-C':['tasks/R6-C/source-unit-index.jsonl','tasks/R6-C/forward-map.jsonl','tasks/R6-C/accepted-facts.json','tasks/R6-C/test-vector-map.jsonl'],
 'R6-O':['tasks/R6-O/forward-matrix.jsonl','tasks/R6-O/external-forward-matrix.jsonl','tasks/R6-O/interface-bindings.json'],
 'R6-CM':['tasks/R6-CM/forward-unit-matrix.jsonl','tasks/R6-CM/forward-matrix.jsonl','tasks/R6-CM/interface-observations.jsonl'],
 'R6-CA':['tasks/R6-CA/forward-matrix.jsonl','tasks/R6-CA/catalog-matrix.jsonl','tasks/R6-CA/coverage-proof.json'],
 'R6-UI':['tasks/R6-UI/forward-matrix.jsonl','tasks/R6-UI/source-unit-coverage.json','tasks/R6-UI/root/behavioral-facts.json'],
 'R6-DX':['tasks/R6-DX/forward-matrix.json','tasks/R6-DX/author-control-bindings.json','tasks/R6-DX/interface-consumption.json'],
 'R6-F':['tasks/R6-F/forward-matrix.json','tasks/R6-F/data-field-consumer-matrix.json','tasks/R6-F/root-structural-units.json'],
 'R6-D':['tasks/R6-D/source-to-spec-matrix.jsonl','tasks/R6-D/forward-matrix-index.json','tasks/R6-D/config-forward-matrix.json','tasks/R6-D/combined-reading-ledger.jsonl'],
 'R6-B':['tasks/R6-B/forward-matrix.json','tasks/R6-B/compat-unit-forward.json','tasks/R6-B/compat-field-index.json','tasks/R6-B/animmaker-method-forward.json','tasks/R6-B/extendtext-forward.json','tasks/R6-B/controller-meta/forward-matrix.json'],
 'R6-I':['evidence/resource-parser/soundfont-full-audit.json','evidence/shader-reading.json','tasks/R6-H/subtasks/supplement-inventory/resource-countercheck.json']}
for reader,paths in forward_paths.items():
 for p in paths:
  q=ROOT/p
  if not q.exists():continue
  data=q.read_bytes()
  catalog.append({'path':p,'axis':'file/unit/fact/consumer/spec or full-field data/resource evidence','owner':reader,
                  'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'reading_implied_by_index':False})
for b in blocks:
 b['original_denominator_status']='NOT_YET_REVIEWED at initial inventory'
 b['domain_evidence']=links.get(b['id'],[])
 if b['path'] in shared:
  b['domain_evidence'].append({'matrix':'tasks/R6-H/report.md','domain':'R6-H',
      'status':'FULL_TEXT_SHARED_SCOPE_HISTORY_NAVIGATION_DISPOSITION',
      'recover':'shared README/scope/test README exact full-range logs and supplement report; no game or runtime approval inferred'})
 b['current_index_status']='CURRENT_EXACT_DOMAIN_ASSESSMENT_OR_NAMED_DISPOSITION' if b['domain_evidence'] else 'UNMAPPED_BLOCK'
 b['aggregate_PASS']=False
unmapped=[{'id':b['id'],'path':b['path'],'lines':[b['start_line'],b['end_line']]} for b in blocks if not b['domain_evidence']]
ownership={x['path']:x['primary_reader'] for x in get('control/source-primary-ownership.json')}
references=[]
for x in get('inventory/reference.json'):
 x=dict(x);x.pop('reading_status',None);reader=ownership[x['path']]
 x['primary_reader']=reader
 x['semantic_evidence_index']=[p for p in forward_paths[reader] if (ROOT/p).exists()]
 x['reading_ledger_index']=[str(p.relative_to(ROOT)) for p in (ROOT/'tasks'/reader).rglob('*reading-ledger*.jsonl') if 'history/' not in str(p)] if reader!='R6-I' else ['tasks/R6-H/subtasks/supplement-inventory/resource-countercheck.json']
 if x['path'].startswith(('PBS/','Text_english_core/')):
  x['reading_scope']='full finite data structure/record/field inventory with currently new parser/consumer semantic rules; not claimed handwritten prose reading of every repeated row'
 elif x['type']=='binary':
  x['reading_scope']='full available finite serialization/font/BMP/SF2/PE structure and readable program units, as exact domain ledgers specify; raw machine code/host output excluded explicitly'
 elif x['path'] in {'.gitignore','.rubocop.yml','README.md','LICENSE','wiki.url'}:
  x['reading_scope']='full text purpose/type disposition; no game or legal behavior conclusion'
 else:x['reading_scope']='fresh continuous full text, declared by actual domain reader and checked against range evidence; no old blob/PASS substitute'
 x['current_semantic_state']='DOMAIN_EVIDENCE_RECORDED_GLOBAL_COUNTER_REQUIRED'
 references.append(x)
formal=[]
for x in get('inventory/formal131.json'):
 x=dict(x);x.pop('reading_status',None)
 own=[b for b in blocks if b['path']==x['path']]
 x['finite_blocks']=len(own);x['exact_assessed_block_ids']=[b['id'] for b in own if b['domain_evidence']]
 x['missing_block_ids']=[b['id'] for b in own if not b['domain_evidence']]
 x['reading_scope']='fresh whole text plus every finite block source-fact/premise join or named structural/history/scope disposition'
 formal.append(x)
put('coverage/global-reverse-block-index.json',blocks)
put('coverage/matrix-catalog.json',catalog)
put('coverage/reference-payloads-current.json',references)
put('coverage/formal-payloads-current.json',formal)
put('coverage/module-primary-mapping.json',[{'path':x['path'],'domain':x['path'].split('/')[2],
 'module_id':re.findall(r'wp\d+[a-z-]*',pathlib.Path(x['path']).name)[:1],
 'finite_block_count':x['finite_blocks'],'current_readers':sorted({p['domain'] for b in blocks if b['path']==x['path'] for p in b['domain_evidence']}),
 'primary_rule':'main formal classified body/data/coverage/test distinct; original specs mapped secondary by H; one canonical root cause per required finding'} for x in formal])
put('coverage/assembly-check.json',{'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reference_files':len(references),'formal_files':len(formal),'formal_blocks':len(blocks),
 'blocks_with_exact_owner_assessment_or_named_disposition':len(blocks)-len(unmapped),
 'unmapped_blocks':unmapped,'missing_forward_matrix_payloads':[p for pp in forward_paths.values() for p in pp if not (ROOT/p).exists()],
 'semantic_proof_not_inferred_from_assembly':True,'global_counter_required':True,'update_started':False})
print(json.dumps({'blocks':len(blocks),'unmapped_count':len(unmapped),'unmapped_paths':dict(collections.Counter(x['path'] for x in unmapped)),'forward_index_files':len(catalog)},ensure_ascii=False))
