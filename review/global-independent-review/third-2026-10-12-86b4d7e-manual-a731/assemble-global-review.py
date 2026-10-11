"""Finite artifact aggregation, identity/navigation validation, no game logic execution."""
from pathlib import Path
import csv,json,hashlib,collections,datetime
OUT=Path(__file__).resolve().parent
REPO=OUT.parents[2]
def read(n):return json.loads((OUT/n).read_text())
def dump(n,d):(OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def table(p):return list(csv.DictReader(p.open(),delimiter='\t'))
def write(n,rows):
 with (OUT/n).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
modules=[f'M{i:02}' for i in range(1,13)]
required=['report.md','findings.json','file-coverage.tsv','capability-coverage.tsv','spec-coverage.tsv','regression-review.json','junction-review.md']
missing=[str(OUT/m/n) for m in modules for n in required if not (OUT/m/n).is_file()]
if missing:raise SystemExit('Incomplete module artifacts: '+str(missing))
caps=[];spec=[];files=[];counts=[]
for m in modules:
 cc=table(OUT/m/'capability-coverage.tsv');ss=table(OUT/m/'spec-coverage.tsv');ff=table(OUT/m/'file-coverage.tsv')
 for x in cc:x['record_origin']=f'{m}/capability-coverage.tsv';x['direction']='REFERENCE_TO_SPEC';caps.append(x)
 for x in ss:x['review_module']=m;x['record_origin']=f'{m}/spec-coverage.tsv';spec.append(x)
 for x in ff:x['review_module']=m;x['record_origin']=f'{m}/file-coverage.tsv';files.append(x)
 counts.append({'module':m,'capability_families':len(cc),'capability_statuses':dict(collections.Counter(x['status'] for x in cc)),'source_records':len(ff),'spec_records':len(ss),'findings':len(read(m+'/findings.json')),'historical_projection_records':len(read(m+'/regression-review.json')),'report':m+'/report.md'})
for x in table(OUT/'root-spec-coverage.tsv'):x['review_module']='ROOT';x['record_origin']='root-spec-coverage.tsv';spec.append(x)
write('capability-coverage.tsv',caps)
write('spec-coverage.tsv',spec)
write('file-read-observations.tsv',files)
formal=read('formal-spec-identities.json');reference=table(OUT/'reference-file-inventory.tsv')
primary={x['path']:m for m in modules for x in read(m+'/assigned-files.json')}
index=[]
for x in reference:
 rs=[f for f in files if f['source_path']==x['path']]
 if not rs:raise SystemExit('Unattributed reference '+x['path'])
 own=[f for f in rs if f['review_module']==x['primary_module']];row=own[0] if own else rs[0]
 index.append({'source_path':x['path'],'git_blob':x['git_blob'],'bytes':x['bytes'],'sha256':x['sha256'],'primary_module':x['primary_module'],'primary_status':row['status'],'actual_observation_modules':';'.join(sorted({f['review_module'] for f in rs})),'actual_read_scopes':' || '.join(f['review_module']+':'+f['read_scope'] for f in rs),'capability_ids':';'.join(sorted({c for f in rs for c in f['capability_ids'].split(';') if c})),'limitation':' || '.join(sorted({f['limitations'] for f in rs})),'interpretation':'File classification/actual range, not identity=semantic coverage; primary PARTIAL not upgraded by unrelated cross read.'})
write('reference-file-coverage.tsv',index)
reverse=[]
for x in formal:
 rs=[s for s in spec if s['spec_path']==x['path']]
 if not rs:raise SystemExit('Formal file has no reverse record '+x['path'])
 reverse.append({'spec_path':x['path'],'git_blob':x['git_blob'],'bytes':x['bytes'],'sha256':x['sha256'],'modules':';'.join(sorted({s['review_module'] for s in rs})),'records':len(rs),'statuses':json.dumps(dict(collections.Counter(s['status'] for s in rs)),ensure_ascii=False),'record_navigation':';'.join(sorted({s['record_origin'] for s in rs})),'interpretation':'Multiple projections are retained; NOT_REVIEWED in a shared catalog remains local, another module may supply its actual owned clauses. No runtime PASS.'})
write('formal131-reverse-index.tsv',reverse)
findings=read('findings.json');fids={x['id'] for x in findings}
if len(fids)!=len(findings):raise SystemExit('Duplicate canonical IDs')
for x in findings:
 for side,ident in [('source_evidence',{r['path']:r for r in reference}),('spec_evidence',{r['path']:r for r in formal})]:
  for ev in x[side]:
   if ev['path'] not in ident or ev['git_blob']!=ident[ev['path']]['git_blob']:raise SystemExit('Bad evidence identity '+x['id']+' '+ev['path'])
   expected=('8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','7589c800b61ba13a13040ed0d686979b80a84fd0') if side=='source_evidence' else ('167296dbe9e2384627b0ed696e87aeb01f211252','33598d8a2a3acdd093cc4fe23f48eea8666100f3')
   if (ev['commit'],ev['tree'])!=expected:raise SystemExit('Wrong fixed evidence SHA '+x['id'])
  for field in ['premises','scenarios','current_vs_expected','impact','implementation_risk','consumers','historical_relation','recommendation','acceptance_criteria','unknowns']:
   if field not in x:raise SystemExit('Missing finding field '+x['id']+' '+field)
dump('coverage-summary.json',{'kind':'FINITE_STATIC_REVIEW_COVERAGE','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'modules':counts,'reference_tracked_denominator':432,'reference_classified':len(index),'formal_denominator':131,'formal_reverse_attributed':len(reverse),'capability_families':len(caps),'capability_statuses':dict(collections.Counter(x['status'] for x in caps)),'family_count_semantics':'Independent module behavior families with explicit shared boundary projections; not globally mutually exclusive gameplay features, not source methods or old113 IDs.','source_binary_data_semantics':'Mechanism/full source reading, samples/full content, binary/metadata and actual activation/host distinguished in ranges/limits.','canonical_ids':sorted(fids),'dispositions':dict(collections.Counter(x['disposition'] for x in findings)),'severity':dict(collections.Counter(x['severity'] for x in findings)),'runtime_observations':0,'reference_execution':0,'behavior_or_static_case_execution':0,'real_demo_chains':0,'files_and_rows_not_runtime_proof':True})
dump('dedup-aliases.json',{'exact_duplicates':[],'canonical_ids':sorted(fids),'retained_dispute':{'id':'GR3-M02-003','original':'M02/findings.json','counterevidence':'M10/junction-review.md','decision':'NO_REQUIRED_REVISION; root complete-set adjudication retained in findings/adjudications'},'related_not_duplicate':[{'ids':['GR3-M01-001','GR3-M01-003'],'reason':'Translation section reader vs PBS preprocessing, different admissible text and consumers'},{'ids':['GR3-M07-001','GR3-M10-001'],'reason':'Battle stale refunded choice vs UI cached held identity, different entry/state/terminal conditions'},{'ids':['GR3-M04-001','GR3-M05-001'],'reason':'SPINDA pixel modification vs scalar individual size helper, different inputs/outputs/reachability'},{'ids':['GR3-M08-001'],'historical':'GR-014 Fling missing item','reason':'Different move, earliest failure point and per-hit self-consumption prerequisites'},{'ids':['GR3-M10-004'],'historical':'GIR-FD82-B028','reason':'Current UI residual inconsistency; domain successor already correct; original scope stays CLOSED'},{'ids':['GR3-M11-001'],'historical':'GIR-FD82-C110/C111','reason':'Area mask/visible union vs map cursor length/first point rules, different consumers'}]})
dump('execution-records.json',{'kind':'ACTUAL_EXECUTION_SCOPE','phase0':'Read-only Git identities/working bytes/blob/SHA256 and necessary input readability; no modifications or module spawning before READY_WITH_LIMITS.','executed_checks':[{'command':'protected-input-check.py','purpose':'131+151+13+14+2+control+coverage/432 reference/62 old candidates byte preservation','result':'MATCH; see protected-input-check.json; no game behavior executed'},{'command':'M04/data-audit.py','purpose':'Static PBS fields vs formal Mega48/Shadow131/effect18 tables','result':'M04/data-field-equivalence.json; not source compiler or behavior cases'},{'command':'Mxx builders/schema/JSON/TSV validation','purpose':'Report integrity/navigation consistency only','result':'All seven artifacts per module present; evidence commit/tree/blob validated; no source game execution'},{'command':'BMP header byte read','purpose':'knownpoint.bmp/selpoint.bmp identity,246 bytes/8×8 header','result':'Available binary headers; no rendering'},{'command':'GitHub fixed-commit metadata/raw README read','purpose':'Cloud availability of fixed reference and delivery identities','result':'remote-input-readback.json and reference-cloud-availability.json; all432 metadata, only README body read remotely so far'}],'check_repairs':[{'artifact':'protected-input-check.py','initial_result':'SyntaxError unmatched closing parenthesis in report-only helper','repair':'Removed one redundant parenthesis; subsequent preservation check succeeds','effect':'No protected files or reference were changed; no behavior test ran'}],'execution_counts':{'runtime_observations':0,'reference_behavior_runs':0,'behavior_or_static_case_runs':0,'real_demo_chains':0},'future_publication_readback':'Separate real Git/remote byte readbacks recorded in publication receipts; not gameplay validation'})
print(json.dumps({'reference':len(index),'formal':len(reverse),'caps':len(caps),'spec_records':len(spec),'findings':len(findings),'statuses':dict(collections.Counter(x['status'] for x in caps))},ensure_ascii=False))
