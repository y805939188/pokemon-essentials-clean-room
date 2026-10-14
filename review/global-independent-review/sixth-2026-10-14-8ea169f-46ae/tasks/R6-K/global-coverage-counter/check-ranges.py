from pathlib import Path
import json,collections,hashlib,datetime,re
P=Path(__file__).parent; B=P.parents[2]; W=Path.cwd(); REF='reference/pokemon-essentials/'
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def normalize(s):
 if not isinstance(s,str):return None
 p=Path(s)
 if p.is_absolute():
  try:s=str(p.relative_to(W))
  except ValueError:return s
 if s.startswith(('Data/','PBS/','Text_english_core/','Fonts/')) or s in ['README.md','LICENSE','.gitignore','.rubocop.yml','wiki.url']:
  # only called on non-formal ledger paths; current shared README is fully qualified.
  s=REF+s
 return s

def intervals(x):
 if x.get('count_toward_readable_coverage') is False:return []
 if x.get('semantic_read_completed') is False:return []
 for a,b in [('start_line','end_line'),('start','end'),('range_start','range_end')]:
  if isinstance(x.get(a),int) and isinstance(x.get(b),int):return [[x[a],x[b]]]
 for k in ['semantic_ranges','ranges','read_ranges','range','line_range','delivered_range']:
  a=x.get(k)
  if isinstance(a,list):
   if len(a)==2 and all(isinstance(v,int) for v in a):return [a]
   return [r for r in a if isinstance(r,list) and len(r)==2 and all(isinstance(v,int) for v in r)]
 if isinstance(x.get('lines'),int) and x.get('stage')=='structure_only':return [[1,x['lines']]]
 return []
ledgerfiles=[p for p in (B/'tasks').rglob('*reading-ledger*.jsonl') if '/history/' not in str(p) and 'global-coverage-counter' not in str(p)]
records=[];issues=[];schemas=[]
for lp in ledgerfiles:
 raw=lp.read_text().splitlines();shape=collections.Counter();n=0
 for ln,s in enumerate(raw,1):
  if not s.strip():continue
  x=json.loads(s);shape.update([tuple(x.keys())]);origin=lp
  if 'original_entry' in x:x=x['original_entry']
  elif 'record' in x and isinstance(x['record'],dict):x=x['record']
  path=x.get('path',x.get('source'));path=path.split(':',1)[1] if isinstance(path,str) and re.match(r'^[a-f0-9]{40}:',path) else path;path=normalize(path);rs=intervals(x)
  if not path or not rs:continue
  n+=1
  log=x.get('acquisition_log',x.get('log',x.get('stdout_log',x.get('transcript'))))
  candidates=[]
  if isinstance(log,str):
   candidates=[Path(log),lp.parent/log,lp.parent/'logs'/log,B/log]
   found=[str(z) for z in candidates if z.is_file()]
  else:found=[]
  mode=' '.join(str(x.get(k,'')) for k in ['stage','mode','review_extent','semantic_status','semantic_review','method','read_basis'])
  structural=bool(re.search(r'structure.only|full.bytes.parsed|not semantic reading|finite.data.structure|full_byte_inventory|field_structure|full_structure|deterministic_full_byte_and_record_inventory|deterministic_id_parameter_location_scan',mode,re.I))
  records.append({'path':path,'ranges':rs,'ledger':str(lp.relative_to(B)),'record_line':ln,'sha256':x.get('sha256',x.get('file_sha256')),'log_pointer':log,'logs_resolved':sorted(set(found)),'mode':mode,'structural_only':structural,'record':x})
 schemas.append({'path':str(lp.relative_to(B)),'sha256':hashlib.sha256(lp.read_bytes()).hexdigest(),'records':len(raw),'range_records':n,'shapes':[{'keys':list(k),'count':v}for k,v in shape.items()]})
by=collections.defaultdict(list)
for r in records:by[r['path']].append(r)
def merged(rs):
 out=[]
 for a,b in sorted(rs):
  if out and a<=out[-1][1]+1:out[-1][1]=max(out[-1][1],b)
  else:out.append([a,b])
 return out
def gaps(n,rs):
 m=merged(rs);out=[];at=1
 for a,b in m:
  if at<a:out.append([at,a-1])
  at=max(at,b+1)
 if at<=n:out.append([at,n])
 return out
result=[]
for kind,name in [('reference','reference.json'),('formal','formal131.json')]:
 for inv in json.loads((B/'inventory'/name).read_text()):
  path=(REF+inv['path']) if kind=='reference' else inv['path']; rr=by[path]
  current=[];wrong=[];invalid=[]
  for r in rr:
   if r['sha256'] and r['sha256']!=inv['sha256']:wrong.append({'ledger':r['ledger'],'record':r['record_line'],'sha':r['sha256']});continue
   for a,b in r['ranges']:
    if not(1<=a<=b<=inv.get('lines',0)):
     invalid.append({'ledger':r['ledger'],'record':r['record_line'],'range':[a,b]});continue
    current.append({**r,'one_range':[a,b]})
  text=inv['type']=='text';sr=[r['one_range'] for r in current if not r['structural_only']];st=[r['one_range'] for r in current if r['structural_only']]
  result.append({'kind':kind,'path':path,'type':inv['type'],'sha256':inv['sha256'],'lines':inv.get('lines'),'current_actual_range_union':merged(sr),'finite_structural_range_union':merged(st),'actual_read_gap_ranges':gaps(inv['lines'],sr)if text else None,'all_declared_range_gap_ranges':gaps(inv['lines'],sr+st)if text else None,'actual_log_pointer_union':merged([r['one_range']for r in current if r['logs_resolved']]),'current_range_receipts':[{'ledger':r['ledger'],'record_line':r['record_line'],'range':r['one_range'],'mode':r['mode'],'logs_resolved':r['logs_resolved'],'log_pointer':r['log_pointer']}for r in current],'wrong_revision_range_receipts':wrong,'invalid_bounds':invalid,'semantic_full_review_not_inferred_from_range_union':True})
put('ledger-schema-catalog.json',schemas);put('range-results.json',result)
put('range-normalized-receipts.json',records)
s={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'ledger_files':len(ledgerfiles),'normalized_range_records':len(records),'files':len(result),'reference_text_actual_read_gap_files':[{'path':x['path'],'gaps':x['actual_read_gap_ranges']}for x in result if x['kind']=='reference' and x['actual_read_gap_ranges']],'formal_actual_read_gap_files':[{'path':x['path'],'gaps':x['actual_read_gap_ranges']}for x in result if x['kind']=='formal' and x['actual_read_gap_ranges']],'all_declared_gap_files':[{'path':x['path'],'gaps':x['all_declared_range_gap_ranges']}for x in result if x['all_declared_range_gap_ranges']],'invalid_bound_records':sum(len(x['invalid_bounds'])for x in result),'binary_files':[x['path']for x in result if x['type']=='binary'],'evidence':'TOOL_VALIDATION_OF_CURRENT_LEDGER_RANGES_NOT_NEW_SEMANTIC_SOURCE_READ'}
put('range-summary.json',s)
print(json.dumps({k:v for k,v in s.items()if k not in ['reference_text_actual_read_gap_files','formal_actual_read_gap_files','all_declared_gap_files','binary_files']},ensure_ascii=False));print('gapcounts',len(s['reference_text_actual_read_gap_files']),len(s['formal_actual_read_gap_files']),len(s['all_declared_gap_files']));print('formal',s['formal_actual_read_gap_files']);print('reference',[x['path']for x in s['reference_text_actual_read_gap_files']])
