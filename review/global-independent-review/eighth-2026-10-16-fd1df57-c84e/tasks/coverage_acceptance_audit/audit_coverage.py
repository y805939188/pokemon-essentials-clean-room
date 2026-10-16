import json,pathlib,hashlib,datetime,collections,subprocess,re
ROOT=pathlib.Path('.').resolve(); OUT=ROOT/'tasks/coverage_acceptance_audit'; B=ROOT.parents[3]; R=pathlib.Path('/workspace/pokemon-essentials')
# Repository root is found independently; report depth is not an identity rule.
B=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'; RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def load(p): return json.loads((ROOT/p).read_text())
def dump(p,d): (OUT/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def digest(b): return hashlib.sha256(b).hexdigest()
def merge(rs):
 o=[]
 for a,b in sorted(rs):
  if o and a<=o[-1][1]+1:o[-1][1]=max(o[-1][1],b)
  else:o.append([a,b])
 return o
def minus(n,rs):
 o=[];start=1
 for a,b in merge(rs):
  if a>start:o.append([start,a-1])
  start=max(start,b+1)
 if start<=n:o.append([start,n])
 return o
claims=[];issues=[]
def walk_claims(task,file,entries,group):
 for i,e in enumerate(entries):
  if not isinstance(e,dict):continue
  inp=e.get('input',{});p=e.get('path',inp.get('path',''));repo=e.get('repo',inp.get('repository',e.get('identity',{}).get('repo','')))
  if not p:continue
  inferred='R' if p.startswith(('Data/','PBS/','Fonts/')) or repo in ['R',str(R)] else 'B8'
  if p in ['Game.exe','animmaker.exe','extendtext.exe','mkxp.json','scripts_extract.rb','scripts_combine.rb','townmapgen.html','animmaker.txt','extendtext.txt','x64-msvcrt-ruby310.dll','soundfont.sf2']:inferred='R'
  base=R if inferred=='R' else B
  input_commit=e.get('commit',inp.get('commit',e.get('identity',{}).get('commit')))
  eligible_current=input_commit in [None,'WORKTREE',B8,RC]
  q=base/p
  status=e.get('read_status',e.get('reading_status',e.get('status',e.get('text_status','FULL_READ' if e.get('full_read') is True else ''))))
  raw=e.get('ranges_read',e.get('read_ranges',e.get('ranges',e.get('range',e.get('coverage',e.get('read_scope',e.get('scope')))))))
  n=None;b=None;textual=False
  if q.is_file():
   b=q.read_bytes()
   try:b.decode('utf8');textual=(b'\0' not in b)
   except UnicodeDecodeError:pass
   if textual:n=len(b.splitlines())
  ranges=[]
  if isinstance(raw,dict): raw=raw.get('lines')
  if isinstance(raw,list):
   if len(raw)==2 and all(isinstance(x,int) for x in raw):ranges=[raw]
   elif all(isinstance(x,list) and len(x)==2 and all(isinstance(a,int) for a in x) for x in raw):ranges=raw
  coarse=False
  if n is not None and status=='FULL_READ' and not ranges and isinstance(raw,str) and any(s in raw.lower() for s in ['entire','full file']):ranges=[[1,n]];coarse=True
  errors=[]
  for a,z in ranges:
   if a<1 or z<a or (n is not None and z>n):errors.append({'range':[a,z],'actual_lines':n})
  if errors:issues.append({'type':'OUT_OF_BOUNDS_REPORTED_RANGE','task':task,'ledger':file,'group':group,'row':i,'path':p,'details':errors})
  clipped=merge([[max(1,a),min(n,z)] for a,z in ranges if n is not None and a<=n and z>=1 and z>=a])
  gaps=minus(n,clipped) if n is not None else None
  full=(status in ['FULL_READ','FULL_RECORD_SEMANTIC_READ'] and n is not None and gaps==[])
  if status=='FULL_READ' and n is not None and not full and raw is not None and eligible_current:issues.append({'type':'FULL_READ_WITH_NONCOVERING_RANGE','task':task,'ledger':file,'row':i,'path':p,'raw':raw,'gaps':gaps})
  ident={}
  if b is not None:
   expect=e.get('sha256',inp.get('sha256',e.get('identity',{}).get('sha256')));ident={'actual_bytes':len(b),'actual_sha256':digest(b),'declared_sha256':expect,'sha_match':None if not expect else expect==digest(b)}
   if expect and expect!=digest(b) and eligible_current:issues.append({'type':'CLAIM_WORKING_IDENTITY_MISMATCH','task':task,'ledger':file,'row':i,'path':p,**ident})
  claims.append({'reader':'/root/'+task,'ledger':file,'group':group,'row':i,'repo':inferred,'input_commit':input_commit,'eligible_current_baseline':eligible_current,'path':p,'reported_status':status,'reported_range':raw,'actual_lines':n,'clipped_read_ranges':clipped,'coarse_entire_file_claim':coarse,'range_complete_full_read_claim':full,'unread_ranges_for_this_entry':gaps,'range_errors':errors,'identity':ident,'credit':'READING_CLAIM_AUDITED_FOR_RANGE_IDENTITY_ONLY; SOURCE_SEMANTICS_NOT_REPERFORMED; ACCEPTANCE_NOT_GRANTED'})
for ledger in sorted([*(ROOT/'tasks').glob('*/reading-ledger.json'),*(ROOT/'tasks').glob('*/read-ledger.json')]):
 task=ledger.parent.name
 if task=='coverage_acceptance_audit':continue
 file=str(ledger.relative_to(ROOT));d=load(file)
 if isinstance(d,list):walk_claims(task,file,d,'entries')
 else:
  for group,entries in d.items():
   if isinstance(entries,list):walk_claims(task,file,entries,group)
# Additional creature identity ledgers have precise status/ranges for every source/formal, including UNREAD.
for file in ['tasks/creature_review/source-reading.json','tasks/creature_review/formal-readset.json']:
 walk_claims('creature_review',file,load(file),'identity_readset')
# primary routing exact all files
routes=load('delegation/scope-freeze.v1.json')['primary_assignments']; primary={}; route_issues=[]
for task,assign in routes.items():
 d=load(assign['readset'])
 for typ,repo in [('reference','R'),('formal','B8')]:
  for e in d[typ]:
   key=(repo,e['path']);primary.setdefault(key,[]).append(task)
for key,tasks in primary.items():
 if len(tasks)!=1:route_issues.append({'key':key,'tasks':tasks})
file_register=[]
for (repo,p),tasks in sorted(primary.items()):
 q=(R if repo=='R' else B)/p;b=q.read_bytes();textual=False
 try:b.decode('utf8');textual=b'\0' not in b
 except UnicodeDecodeError:pass
 n=len(b.splitlines()) if textual else None
 matches=[c for c in claims if (c['repo'],c['path'])==(repo,p) and c['eligible_current_baseline']]
 all_ranges=merge([r for c in matches for r in c['clipped_read_ranges']]);full=[c['reader'] for c in matches if c['range_complete_full_read_claim']]
 file_register.append({'repo':repo,'path':p,'primary':tasks,'bytes':len(b),'sha256':digest(b),'physical_lines_if_utf8_text':n,'reported_readers':sorted(set(c['reader'] for c in matches)),'reported_full_file_readers':sorted(set(full)),'reported_ranges_union':all_ranges,'unread_physical_ranges':minus(n,all_ranges) if n is not None else 'FINITE_BINARY_STRUCTURE_RECEPTION_REQUIRED','reading_state':'REPORTED_FULL_READ_UNRECEIVED' if full else ('REPORTED_PARTIAL_READ_UNRECEIVED' if all_ranges else 'UNREAD_OR_NO_EXACT_TEXT_RANGE_LEDGER'),'semantic_acceptance':'UNRECEIVED','reason':'No complete atomic-clause/source-fact/premise/consumer acceptance certificate exists; finite local supported facts retained separately'})
# Exhaustively check every reported reverse locator and every ID link.
matrices=[]; row_audit=[]
def audit_reverse(file,key,pathkey,rangefn,linkkey,valid_ids,reader):
 d=load(file);rows=d[key];cnt=collections.Counter();paths=collections.Counter()
 for i,row in enumerate(rows):
  p=row[pathkey];a,z=rangefn(row);matches=[c for c in claims if c['path']==p and c['reader']==reader and c['eligible_current_baseline']];cov=merge([r for c in matches for r in c['clipped_read_ranges']]);q=B/p;n=len(q.read_bytes().splitlines());covered=any(x<=a<=z<=y for x,y in cov)
  links=row.get(linkkey,[]);bad=[x for x in links if x not in valid_ids]
  errs=[]
  if a<1 or z<a or z>n:errs.append('OUT_OF_BOUNDS')
  if not covered:errs.append('LOCATOR_OUTSIDE_READER_REPORTED_RANGE')
  if bad:errs.append('UNKNOWN_FACT_ID')
  for k in errs:cnt[k]+=1
  if not links:cnt['NO_LOCAL_FACT_LINK']+=1
  paths[p]+=1
  row_audit.append({'matrix':file,'row':i,'id':row.get('clause_id',row.get('id',f'{p}:L{a}')),'path':p,'range':[a,z],'links':links,'link_resolution_errors':bad,'reported_range_covered':covered,'issues':errs,'semantic_acceptance':'UNRECEIVED','required':'Named reader must decompose all subassertions, establish precise source facts, premises, consumers, and disposition before acceptance'})
 matrices.append({'path':file,'rows':len(rows),'counts':dict(cnt),'all_rows_semantically_unreceived':len(rows),'paths':dict(paths)})
ker=load('tasks/kernel_review/file-unit-fact-consumer-spec-matrix.json')['rows']; core=load('tasks/combat_review/source-to-spec.json')['facts']; cre=load('tasks/creature_review/forward-matrix.pending.json')['facts']
audit_reverse('tasks/kernel_review/clause-source-premise-matrix.json','clauses','path',lambda r:r['range'],'fact_links',{r['fact_id'] for r in ker},'/root/kernel_review')
audit_reverse('tasks/combat_review/clause-to-source.json','rows','path',lambda r:[r['line'],r['line']],'source_facts',{r['id'] for r in core},'/root/combat_review')
audit_reverse('tasks/creature_review/reverse-matrix.pending.json','rows','formal_path',lambda r:[r['line'],r['line']],'manual_fact_candidates',{r['id'] for r in cre},'/root/creature_review')
for file,key in [('tasks/kernel_review/file-unit-fact-consumer-spec-matrix.json','rows'),('tasks/combat_review/source-to-spec.json','facts'),('tasks/creature_review/forward-matrix.pending.json','facts'),('tasks/preflight_resources/forward-map.json','facts'),('tasks/preflight_resources/reverse-map.json','rows')]:
 rows=load(file)[key];cnt={}
 for k in ['support_status','acceptance','status','disposition','support']:
  c=collections.Counter(str(r[k]) for r in rows if k in r)
  if c:cnt[k]=dict(c)
 matrices.append({'path':file,'rows':len(rows),'status_counts':cnt,'audit':'All rows schema/status/identifiers inspected by script; hand-read report limitations apply to every row. Existing source facts retained but no complete file/clause acceptance is granted.'})
# Verify all legacy manifest physical-line disposition fields against original bytes.
m=load('tasks/inventory_denominator/manifest-purpose-disposition.json');bb=(B/m['path']).read_bytes();lines=bb.splitlines(keepends=True); offset=0;manifest_errors=[]
for i,e in enumerate(m['lines']):
 b=lines[i];expected={'line':i+1,'byte_start':offset,'bytes':len(b),'sha256':digest(b)}
 for k,v in expected.items():
  if e.get(k)!=v:manifest_errors.append({'line':i+1,'field':k,'expected':v,'actual':e.get(k)})
 offset+=len(b)
manifest_audit={'path':m['path'],'original_bytes':len(bb),'original_sha256':digest(bb),'rows':len(m['lines']),'physical_lines':len(lines),'fields':sorted(set(k for r in m['lines'] for k in r)),'all_disposition_counts':dict(collections.Counter(r['disposition'] for r in m['lines'])),'all_reason_counts':dict(collections.Counter(r['reason'] for r in m['lines'])),'errors':manifest_errors,'semantic_qualification':'Type/identity treatment verified, currentness of behavior/cases is not inferred from historic date or index placement; semantic use must be traced to current B8/qualification consumers'}
# Complete primary physical source and formal structural locator freeze. No automatic semantic units are counted.
formal=[]; source=[]
for f in file_register:
 p=f['path'];q=(R if f['repo']=='R' else B)/p;b=q.read_bytes();blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 if f['repo']=='R':
  source.append({'path':p,'blob':blob,'bytes':len(b),'primary':f['primary'],'read_state':f['reading_state'],'physical_unread_ranges':f['unread_physical_ranges'],'semantic_units':'UNFROZEN_REQUIRES_READER_DEFINED_COMPLETE_CONTROL_FLOW_RECORD_FIELD_OR_FINITE_BINARY_STRUCTURE_PARTITION','acceptance':'UNRECEIVED'})
  continue
 ls=b.splitlines(keepends=True);section=[];spans=[];i=0;offs=[0]
 for line in ls:offs.append(offs[-1]+len(line))
 while i<len(ls):
  t=ls[i].decode('utf8');a=i
  if not t.strip():kind='layout';i+=1
  elif re.match(r'^#{1,6}\s',t):
   level=len(t)-len(t.lstrip('#'));section=section[:level-1]+[t.strip()];kind='heading';i+=1
  elif t.lstrip().startswith('|'):kind='table_row';i+=1
  elif re.match(r'^\s*(?:[-*+]\s|\d+[.)]\s)',t):
   kind='list_item';i+=1
   while i<len(ls) and ls[i][:1] in [b' ',b'\t'] and ls[i].strip():i+=1
  elif t.lstrip().startswith('```'):
   kind='fenced_payload';i+=1
   while i<len(ls) and not ls[i].lstrip().startswith(b'```'):i+=1
   if i<len(ls):i+=1
  else:
   kind='paragraph';i+=1
   while i<len(ls) and ls[i].strip() and not re.match(rb'^(?:#{1,6}\s|\s*\||\s*[-*+]\s|\s*\d+[.)]\s|\s*```)',ls[i]):i+=1
  raw=b[offs[a]:offs[i]]
  spans.append({'locator_id':f'B8:{blob}:L{a+1}-{i}','line_range':[a+1,i],'byte_range':[offs[a],offs[i]],'kind':kind,'section_path':section.copy(),'sha256':digest(raw),'semantic_children':'UNDECOMPOSED_BY_NAMED_READER','status':'LAYOUT_TYPE_ONLY' if kind=='layout' else 'UNRECEIVED'})
 formal.append({'path':p,'blob':blob,'bytes':len(b),'sha256':digest(b),'lines':len(ls),'primary':f['primary'],'physical_partition_contiguous':bool(spans and spans[0]['byte_range'][0]==0 and spans[-1]['byte_range'][1]==len(b) and all(x['byte_range'][1]==y['byte_range'][0] for x,y in zip(spans,spans[1:]))),'physical_locator_count':len(spans),'semantic_atomic_clause_count':'UNFROZEN','locators':spans})
summary={repo:dict(collections.Counter(f['reading_state'] for f in file_register if f['repo']==repo)) for repo in ['R','B8']}
dump('acceptance-register.json',{'schema':'r8-coverage-acceptance-audit/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'global_conclusion':'INCOMPLETE_NO_PASS','evidence_limit':'All input JSON rows parsed and audited mechanically. Actual domain source semantics are reported claims, not independently repeated full reading. This audit does not grant atomic-clause acceptance.','file_counts':summary,'route_issues':route_issues,'files':file_register,'all_ledger_claims':claims,'matrix_audits':matrices,'reverse_row_audits':row_audit,'legacy_manifest_audit':manifest_audit,'issues':issues,'update_started':False})
dump('proposed-denominator.json',{'schema':'r8-proposed-denominator/v1','frozen_B8':B8,'frozen_R':RC,'file_denominators':{'R':432,'formal':131},'formal_physical_locator_count':sum(len(f['locators']) for f in formal),'formal_atomic_semantic_clauses':'UNFROZEN','source_semantic_units_and_facts':'UNFROZEN','consumer_interfaces':'UNFROZEN','locator_contract':'IDs bind exact immutable file blob, complete contiguous line and byte ranges, section hierarchy, span SHA. Mechanical paragraphs/table/list/fences/layout are candidate locators, never atomic assertions. Named reader assigns child /A01 /A02 only after full semantic decomposition. No semicolon or method counts are semantic denominators.','formal':formal,'reference':source,'update_started':False})
print(json.dumps({'file_counts':summary,'issues':issues,'route_issues':route_issues,'matrices':[{k:v for k,v in x.items() if k!='paths'} for x in matrices],'manifest_errors':manifest_errors,'formal_locator_count':sum(len(f['locators']) for f in formal)},ensure_ascii=False,indent=2))
