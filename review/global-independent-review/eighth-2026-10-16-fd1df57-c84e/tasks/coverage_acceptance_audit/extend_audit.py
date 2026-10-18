import pathlib
exec((pathlib.Path('tasks/coverage_acceptance_audit/audit_coverage.py')).read_text().split('claims=[];issues=[]')[0])
a=load('tasks/coverage_acceptance_audit/acceptance-register.json');claims=a['all_ledger_claims'];files=a['files'];facts=[];checks=[]
def linecheck(reader,repo,p,rs):
 base=R if repo=='R' else B;q=base/p
 if not q.is_file():return {'exists':False,'reason':'Derived/decoded or synthetic locator requires its separately bound identity'}
 n=len(q.read_bytes().splitlines());matches=[x for x in claims if x['reader']==reader and x['repo']==repo and x['path']==p and x['eligible_current_baseline']];cov=merge([z for x in matches for z in x['clipped_read_ranges']]); bad=[];unread=[]
 for x,y in rs:
  if x<1 or y<x or y>n:bad.append([x,y])
  if not any(v<=x<=y<=w for v,w in cov):unread.append([x,y])
 return {'exists':True,'actual_lines':n,'range_errors':bad,'outside_reader_reported_ranges':unread}
for file,key,reader in [('tasks/kernel_review/file-unit-fact-consumer-spec-matrix.json','rows','/root/kernel_review'),('tasks/combat_review/source-to-spec.json','facts','/root/combat_review'),('tasks/creature_review/forward-matrix.pending.json','facts','/root/creature_review'),('tasks/preflight_resources/forward-map.json','facts','/root/preflight_resources')]:
 for i,r in enumerate(load(file)[key]):
  ident=r.get('fact_id',r.get('id'));src=[];spec=[]
  if reader.endswith('kernel_review'):
   for s in r['sources']:src.append({'path':s['path'],'ranges':s['ranges'],'check':linecheck(reader,'R',s['path'],s['ranges'])})
   for s in r['spec']:spec.append({'path':s['path'],'ranges':[s['range']],'check':linecheck(reader,'B8',s['path'],[s['range']])})
  elif reader.endswith('combat_review'):
   src.append({'path':r['source'],'ranges':[r['range']],'check':linecheck(reader,'R',r['source'],[r['range']])});spec=r['spec']
  elif reader.endswith('creature_review'):
   s=r['source'];src.append({'path':s['path'],'ranges':[s['lines']],'check':linecheck(reader,'R',s['path'],[s['lines']])});f=r['formal'];rs=[[n,n] for n in f['matching_lines']];spec.append({'path':f['path'],'ranges':rs,'check':linecheck(reader,'B8',f['path'],rs)})
  else:
   s=r['source']
   if 'start' in s and 'end_exclusive' in s:
    b=(R/s['path']).read_bytes();start,end=s['start'],s['end_exclusive'];src.append({'path':s['path'],'byte_range':[start,end],'exact_current_slice_sha256_match':digest(b[start:end])==s['sha256'],'within_file':0<=start<=end<=len(b)})
   else:src.append({'locator':s,'check':'FINITE_STRUCTURE_OR_CIL_REFERENCE_REQUIRES_NAMED_RECEPTION; NOT_FULL_FILE_PROOF'})
   spec=r['spec']
  facts.append({'matrix':file,'row':i,'fact_id':ident,'sources':src,'spec_locators':spec,'consumer_locators':r.get('consumers',r.get('consumer',[])),'existing_status':r.get('acceptance',r.get('status',r.get('support_status',r.get('disposition')))),'complete_semantic_acceptance':'UNRECEIVED','rule':'Local finite assertion and named partial receipts retained; no full compound clause or transitive consumer closure is inferred.'})
# Every known source structure, including methodless modules and nested definitions, is retained for joining.
structure_rows=[]
for e in load('tasks/kernel_review/source-unit-inventory.json')['items']:
 p=e['source_identity']['path']
 for j,s in enumerate(e['structures']):
  structure_rows.append({'source':'tasks/kernel_review/source-unit-inventory.json','path':p,'structure_index':j,'kind':s['kind'],'identity':s['identity'],'range':s['range'],'state':'UNRECEIVED','range_check':linecheck('/root/kernel_review','R',p,[s['range']]),'required':'Read complete context and define each real assertion/premise; indentation locator is not a semantic unit acceptance'})
co=load('tasks/combat_review/source-to-spec.json');known={r['id']:r for r in co['facts']};core_units=[]
for s in co['source_units']:
 linked=[known[x] for x in s['facts'] if x in known]
 core_units.append({'id':s['id'],'path':s['path'],'range':[s['start'],s['end']],'linked_facts':s['facts'],'unknown_fact_ids':[x for x in s['facts'] if x not in known],'locator_contained_by_linked_fact_range':any(r['source']==s['path'] and r['range'][0]<=s['start']<=s['end']<=r['range'][1] for r in linked),'state':'UNRECEIVED','note':'Complete method control flow/branch premises must be received; signature locator alone is not unit coverage'})
# All lexical settings/stat consumers remain obligations, even if another reader reported full-file reading.
census=load('tasks/kernel_review/consumer-census.json');consumer_rows=[]
by_path={r['path']:r for r in files if r['repo']=='R'}
for kind in ['settings','stats']:
 for name,d in census[kind].items():
  for ref in d['references']:
   f=by_path.get(ref['path']);consumer_rows.append({'kind':kind,'name':name,'declarations':d['declarations'],'consumer_path':ref['path'],'consumer_line':ref['line'],'primary':f['primary'] if f else [],'reported_full_readers':f['reported_full_file_readers'] if f else [],'state':'UNRECEIVED_LEXICAL_CANDIDATE','note':'Must decide comment/actual consumer, finite branch, input premise, output consumer and formal child clause; lexical match is not an interface fact'})
# Verify fixed Git identities independently for every native/formal inventory path.
fixed_checks=[]
for repo,base,commit in [('R',R,RC),('B8',B,B8)]:
 tree={}
 raw=subprocess.check_output(['git','-C',str(base),'ls-tree','-r','-z',commit])
 for row in raw.split(b'\0'):
  if not row:continue
  meta,p=row.split(b'\t',1);mode,kind,blob=meta.decode().split();tree[p.decode()]={'mode':mode,'kind':kind,'blob':blob}
 for f in files:
  if f['repo']!=repo:continue
  p=f['path'];b=(base/p).read_bytes();actual=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();fixed_checks.append({'repo':repo,'commit':commit,'path':p,**tree[p],'working_blob':actual,'matches':actual==tree[p]['blob'],'bytes':len(b),'sha256':digest(b)})
# Every PE region and every finite discovery candidate is checked; status remains distinct.
resources=[]
for item in load('tasks/preflight_resources/native-region-denominator.json')['files']:
 b=(R/item['path']).read_bytes();pos=0;errors=[]
 for i,r in enumerate(item['continuous_partition']):
  if r['start']!=pos:errors.append({'partition':i,'gap_or_overlap_after':pos})
  if digest(b[r['start']:r['end_exclusive']])!=r['sha256']:errors.append({'partition':i,'sha':'mismatch'})
  pos=r['end_exclusive']
 if pos!=len(b):errors.append({'final_end':pos,'actual':len(b)})
 resources.append({'path':item['path'],'bytes':len(b),'complete_byte_partition':not errors,'partition_rows':len(item['continuous_partition']),'errors':errors,'semantic_status':'STRUCTURE_PARSED; only explicit ledger finite units read; native CFG and host not inferred'})
ld=load('tasks/preflight_resources/literal-discovery-reception.json');literal_rows=[]
for row in ld['rows']:
 b=(R/row['path']).read_bytes();literal_rows.append({'id':row['id'],'path':row['path'],'range':[row['start'],row['end_exclusive']],'sha_match':digest(b[row['start']:row['end_exclusive']])==row['sha256'],'reported_status':row['reading_status'],'classification':row['classification'],'independent_acceptance':'PENDING'})
# Audit every normalized PBS-world record/field locator; not a consumer approval.
pbsfile=ROOT/'tasks/pbs_world_record_audit/records.json';pbsrows=[]
if pbsfile.exists():
 for i,row in enumerate(load('tasks/pbs_world_record_audit/records.json')['records']):
  lines=(R/row['source']).read_text().splitlines();n=row['line_start'];err=[]
  if not 1<=n<=len(lines):err.append('RECORD_START_OUT_OF_BOUNDS')
  for f in row['fields']:
   if isinstance(f,dict):
    ln=f['line']
    if not 1<=ln<=len(lines):err.append('FIELD_OUT_OF_BOUNDS');continue
    raw=lines[ln-1].strip();parts=raw.split('=',1)
    if len(parts)!=2 or parts[0].strip()!=f['field'] or parts[1].strip()!=f['value']:err.append('FIELD_TRANSCRIPTION_DIFFERENCE')
  pbsrows.append({'record_index':i,'source':row['source'],'record_id':row['id'],'line_start':n,'field_count':len(row['fields']),'range_errors':err,'semantic_status':'REPORTED_FULL_RECORD_READ;CONSUMER_FORMAL_RECEIPT_PENDING','reader':'/root/pbs_world_record_audit'})
a['pbs_world_record_audits']=pbsrows
a['forward_fact_audits']=facts;a['kernel_structure_audits']=structure_rows;a['core_method_locator_audits']=core_units;a['consumer_join_obligations']=consumer_rows;a['fixed_identity_checks']=fixed_checks;a['resource_partition_audit']=resources;a['resource_new_literal_audit']=literal_rows;a['finite_cross_domain_receipts']=load('tasks/creature_review/cross-domain-reception.json');a['resource_aggregate_counts']=ld['counts']
dump('acceptance-register.json',a)
print(json.dumps({'forward_rows':len(facts),'kernel_structure_rows':len(structure_rows),'core_method_rows':len(core_units),'consumer_obligations':len(consumer_rows),'consumer_paths':len(set(r['consumer_path'] for r in consumer_rows)),'fixed_paths':len(fixed_checks),'fixed_identity_mismatches':sum(not x['matches'] for x in fixed_checks),'source_range_errors':[(r['fact_id'],s) for r in facts for s in r['sources'] if isinstance(s.get('check'),dict) and (s['check'].get('range_errors') or s['check'].get('outside_reader_reported_ranges'))],'spec_range_errors':[(r['fact_id'],s) for r in facts for s in r['spec_locators'] if isinstance(s,dict) and isinstance(s.get('check'),dict) and (s['check'].get('range_errors') or s['check'].get('outside_reader_reported_ranges'))],'native_partitions':resources,'new_literals':len(literal_rows),'new_literal_sha_mismatches':sum(not x['sha_match'] for x in literal_rows),'core_method_not_contained_by_fact_range':sum(not r['locator_contained_by_linked_fact_range'] for r in core_units)},ensure_ascii=False,indent=2))
