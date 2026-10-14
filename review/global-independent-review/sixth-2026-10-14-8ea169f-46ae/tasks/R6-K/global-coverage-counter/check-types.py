from pathlib import Path
import json,hashlib,datetime,collections,subprocess,gzip
P=Path(__file__).parent;B=P.parents[2];W=Path.cwd();R=W/'reference/pokemon-essentials';PIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6';RPIN='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def get(p):return json.loads((B/p).read_text())
def put(p,x):(P/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def bind(path):
 p=B/path;return {'path':path,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
# Exact fixed-file identity, not new behavioral reading.
ident=[]
for kind,file in [('R','reference.json'),('formal','formal131.json')]:
 for x in get('inventory/'+file):
  p=(R/x['path'])if kind=='R'else(W/x['path']);raw=p.read_bytes()
  ident.append({'kind':kind,'path':x['path'],'bytes_match':len(raw)==x['bytes'],'sha256_match':hashlib.sha256(raw).hexdigest()==x['sha256']})
# Every fixed workspace blob has one retained type; current source-primary is independent of type purpose.
ls=subprocess.run(['git','ls-tree','-rz','--full-tree',PIN],capture_output=True,check=True).stdout
actual={}
for row in ls.split(b'\0'):
 if not row:continue
 head,path=row.split(b'\t',1);mode,kind,blob=head.decode().split();actual[path.decode()]={'mode':mode,'kind':kind,'blob':blob}
ht=get('tasks/R6-H/subtasks/supplement-inventory/workspace-types-full.json');stored={x['path']:x for x in ht};diff=[]
for p,x in actual.items():
 if p not in stored or any(stored[p][k]!=x[k]for k in ['mode','kind','blob']) or not stored[p]['type_disposition']:diff.append(p)
extra=sorted(set(stored)-set(actual));tc=collections.Counter(x['type_disposition']for x in ht)
# All116 supplementary paths; retain exact5 full reading versus111 secondary primary relation.
supp=get('tasks/R6-H/subtasks/supplement-inventory/effective-supplement116.json');sm=get('tasks/R6-H/subtasks/supplement-inventory/specs113-primary-matrix.json');pm={x['source']:x for x in sm};reads=[];sec=[];errs=[]
ledger=[json.loads(s)for s in (B/'tasks/R6-H/subtasks/supplement-inventory/reading-ledger.jsonl').read_text().splitlines()if s.strip()]
for x in supp:
 p=W/x['path'];raw=p.read_bytes();ok=len(raw)==x['bytes']and hashlib.sha256(raw).hexdigest()==x['sha256']
 if not ok:errs.append({'path':x['path'],'reason':'fixed current identity differs'})
 retained=x['path']in ['planning/coverage.md','planning/feature-matrix.md','audit/source-traceability.md','specs/demo/wp01-baseline-and-evidence-scope.md','specs/kernel/wp02-settings-inventory-appendix.md']
 if retained:
  rr=[];logs=[]
  for z in ledger:
   zp=z.get('path',z.get('source',''));zp=zp.split(':',1)[1] if len(zp.split(':',1)[0])==40 and ':' in zp else zp
   if zp!=x['path']:continue
   rg=z.get('range',[z.get('start_line'),z.get('end_line')]);lg=z.get('log',z.get('stdout_log'))
   if isinstance(rg,list)and lg and(B/'tasks/R6-H/subtasks/supplement-inventory'/lg).exists():rr.append(rg);logs.append(lg)
  cover={n for a,b in rr for n in range(a,b+1)};miss=[n for n in range(1,x['lines']+1)if n not in cover]
  reads.append({'path':x['path'],'identity_matches':ok,'actual_contiguous_ranges':rr,'logs':logs,'missing':miss,'purpose':x.get('use'),'no_game_PASS':True})
  if miss:errs.append({'path':x['path'],'reason':'retained fulltext actual durable range missing','missing':miss})
 else:
  rel=pm.get(x['path']);valid=bool(rel and (W/rel['primary']).is_file())
  sec.append({'source':x['path'],'identity_matches':ok,'primary':rel['primary']if rel else None,'trace_clause':rel.get('trace_clause')if rel else None,'audit_input_line':rel.get('input_line')if rel else None,'secondary_type_disposition':'full structural type/heading/table inventory, primary current classified body owns behavior; original text is not new gameplay PASS','relation_exists':valid})
  if not valid:errs.append({'path':x['path'],'reason':'secondary primary unavailable'})
# All binary assets get named current producer/fact/consumer scope rather than a fabricated line citation.
binrows=[]
for x in get('inventory/reference.json'):
 if x['type']!='binary':continue
 path=x['path']
 if path.startswith('Fonts/')or path.endswith('.bmp'):
  artifacts=['tasks/R6-D/fonts/source-unit-matrix.json','tasks/R6-D/fonts/traceability.json','tasks/R6-D/fonts/report.md'];scope='Full static font table/cmap/geometry/metrics or all BMP pixel bytes; conditional font-name and marker consumers. Native rendering/installation unknown.'
 elif path in ['Data/Scripts.rxdata','Data/messages_core.dat']:
  artifacts=['tasks/R6-D/localization/binary-sections.json','tasks/R6-D/localization/event-buckets.json','tasks/R6-D/localization/structure-validation.json','tasks/R6-D/localization/decoded-script-00.txt','tasks/R6-D/localization/report.md'];scope='Inert primitive serialization structure, every text domain/empty event bucket or full49-line decompressed external loader; no Marshal.load or script execution.'
 elif path=='soundfont.sf2':
  artifacts=['evidence/resource-parser/soundfont-full-audit.json','tasks/R6-H/subtasks/supplement-inventory/resource-countercheck.json','tasks/R6-O/counter-receipt-K-global-evidence.json'];scope='All RIFF/tables/PCM/sample/voice structure and explicitly conditional parameter/modulator projection; no synth/voice/audio observation; format conformity not certified.'
 else:
  artifacts=['evidence/resource-parser/binary-interface-audit.json','tasks/R6-B/forward-matrix.json','tasks/R6-B/limits.json','tasks/R6-B/report.md','tasks/R6-O/counter-receipt-K-global-evidence.json'];scope='Full PE static structure and named readable embedded sources/controller/shaders/15 CIL/finite extendtext body; full native CFG/dynamic selector/external OS/CLR/GPU/inputs excluded as exact B limits.'
 binrows.append({'path':'reference/pokemon-essentials/'+path,'input_sha256':x['sha256'],'bytes':x['bytes'],'recoverable_artifacts':[bind(p)for p in artifacts],'named_scope':scope,'new_reference_execution_by_K_counter':0,'native_semantic_PASS':False})
# Validate every finite font/BMP interval and its fact consumer receipt.
fu=get('tasks/R6-D/fonts/source-unit-matrix.json');bm={('reference/pokemon-essentials/'+x['path']):x for x in get('inventory/reference.json')if x['type']=='binary'};fontbad=[]
for u in fu['units']:
 a,b=u['bytes']
 if u['path']not in bm or not(0<=a<=b<=bm[u['path']]['bytes']):fontbad.append(u['unit'])
# Decode known inert compressed review payload; compare complete-byte receipt before finite record traversal.
meta=get('tasks/R6-D/pbs-bulk/source-to-spec-matrix.json');gz=B/'tasks/R6-D/pbs-bulk'/meta['artifact'];packed=gz.read_bytes();raw=gzip.decompress(packed)
compressed_identity={'compressed_bytes_match':len(packed)==meta['compressed_bytes'],'compressed_sha256_match':hashlib.sha256(packed).hexdigest()==meta['compressed_sha256'],'uncompressed_bytes_match':len(raw)==meta['uncompressed_bytes'],'uncompressed_sha256_match':hashlib.sha256(raw).hexdigest()==meta['uncompressed_sha256']}
j=json.loads(raw);shape={'type':type(j).__name__,'top_keys':list(j)if isinstance(j,dict)else None,'records':len(j)if isinstance(j,list)else None};sample=j[0]if isinstance(j,list)else j
# Do not confuse a parser with manual reading. Save actual shape for next bounded record-consumer check.
put('bulk-record-shape.json',{'shape':shape,'first_record_schema':sample if isinstance(j,list)else {k:type(v).__name__ for k,v in j.items()},'compressed_identity':compressed_identity,'own_semantic_read_credit':0})
put('supplement-retained5-check.json',reads);put('supplement-secondary111-check.json',sec);put('binary18-scope-bindings.json',binrows);put('current-file-identity-checks.json',ident)
s={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'fixed_payloads':len(ident),'identity_mismatches':[x for x in ident if not x['bytes_match']or not x['sha256_match']],'workspace_blobs':len(actual),'workspace_type_rows':len(ht),'workspace_type_diff':diff,'workspace_type_extra':extra,'complete_type_counts':dict(tc),'supplement_paths':len(supp),'retained_actual_fulltext':len(reads),'secondary_exact_primary':len(sec),'supplement_errors':errs,'binary_assets':len(binrows),'font_bitmap_unit_counts':fu['counts_by_kind'],'invalid_font_bitmap_byte_bounds':fontbad,'compressed_bulk_identity':compressed_identity,'bulk_actual_structure_shape':shape,'administrative_and_structural_check_not_behavior_approval':True}
put('type-summary.json',s);print(json.dumps({k:v for k,v in s.items() if k!='supplement_errors'},ensure_ascii=False));print('supplement_errors',errs)
