import pathlib,json,collections,hashlib,datetime
ROOT=pathlib.Path('.');OUT=ROOT/'tasks/coverage_acceptance_audit';PRE=ROOT/'tasks/preflight_resources';R=pathlib.Path('/workspace/pokemon-essentials')
def sha(b):return hashlib.sha256(b).hexdigest()
index=json.loads((PRE/'handoff/readset-index.json').read_text());inventory=[]
for meta in index['strings']:
 p=PRE/meta['inventory'];source=(R/meta['path']).read_bytes();cnt=collections.Counter();errors=[];n=0
 with p.open() as h:
  for n,line in enumerate(h,1):
   row=json.loads(line);x,y=row['start'],row['end_exclusive'];raw=source[x:y];cnt[row['classification']]+=1;cnt[row['encoding']]+=1
   if not 0<=x<=y<=len(source) or len(raw)!=row['bytes'] or sha(raw)!=row['sha256']:errors.append({'row':n,'check':'BYTE_RANGE_LENGTH_SHA'})
   decoded=raw.decode('ascii' if row['encoding']=='ascii' else 'utf-16-le')
   if decoded!=row['text']:errors.append({'row':n,'check':'DECODED_TEXT'})
 b=p.read_bytes();inventory.append({'path':str(p),'bytes':len(b),'sha256':sha(b),'identity_matches':len(b)==meta['inventory_bytes'] and sha(b)==meta['inventory_sha256'],'rows':n,'all_row_classification_encoding_counts':dict(cnt),'all_row_errors':errors,'semantic_credit':'NO_NEW_READ_CREDIT; indexed finite candidates are not automatically genuine text or clauses'})
c=json.loads((PRE/index['controller']).read_text());source=(R/c['source_path']).read_bytes();end=c['offset'];errs=[]
for i,row in enumerate(c['rows']):
 raw=source[row['start']:row['end_exclusive']]
 if row['start']!=end or len(raw)!=row['raw_bytes'] or sha(raw)!=row['sha256']:errs.append({'row':i,'check':'CONTINUITY_LENGTH_SHA'})
 if raw.decode('ascii').rstrip('\r\n')!=row['text']:errs.append({'row':i,'check':'ASCII_TEXT'})
 end=row['end_exclusive']
controller={'path':'tasks/preflight_resources/'+index['controller'],'rows':len(c['rows']),'records':c['record_count'],'patterns':c['pattern_count'],'platform_counts':c['platform_counts'],'byte_range':[c['offset'],c['end_exclusive']],'whole_region_sha_matches':sha(source[c['offset']:c['end_exclusive']])==c['region_sha256'],'all_rows_errors':errs,'continuous_end_matches':end==c['end_exclusive'],'status':'UNREAD_BY_NEW_READER; priorSTRUCTURE_PARSED not semantic acceptance'}
f=OUT/'acceptance-register.json';a=json.loads(f.read_text());a['resource_frozen_followup_handoff_audit']={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'strings':inventory,'controller':controller,'totals':index['totals'],'scope':'Every260161candidate range/sha/decoder checked mechanically, all1678controller physical rows checked; no source semantic reading or consumer receipt inferred.'};f.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
for filename in ['coverage-gaps.json','proposed-denominator.json']:
 p=OUT/filename;d=json.loads(p.read_text());arr=d.get('supplemental_contracts',d.get('supplemental_acceptance_contracts'))
 for r in arr:
  if r['id']=='controller_record_semantic_reception':
   r['current_exact_handoff_index']='tasks/preflight_resources/handoff/readset-index.json';r['current_exact_handoff_manifest']='tasks/preflight_resources/handoff/manifest.json';r['current_exact_parent_dispatch_prompt']='tasks/preflight_resources/handoff/next-context-prompt.md';r['current_finite_candidate_totals']=index['totals'];r['acceptance_contract'].append('Also fully type-dispose all260161indexed min4 ASCII/UTF16LE-ASCII-subset candidates:255158 currently unread. Existing exact program/nonprogram slice associations retained. Printable machine-code/random candidates are not automatically real strings; known recoverable metadata/program/data semantic content must be read by a named context and remaining true opaque boundary stated precisely.')
 if filename=='coverage-gaps.json':
  for g in d['gaps']:
   if g['id']=='COV-RESOURCE-001':g['newly_frozen_available_unread_scope']={'finite_candidates':260161,'currently_unread_candidates':255158,'index':'tasks/preflight_resources/handoff/readset-index.json','qualification':'Available finite candidates require complete type/purpose disposition and actual semantic reading where applicable; they are neither automatically meaningful text nor automatically L04 opaque.'}
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'string_rows':sum(x['rows'] for x in inventory),'string_errors':sum(len(x['all_row_errors']) for x in inventory),'string_identity_mismatches':sum(not x['identity_matches'] for x in inventory),'controller':controller},ensure_ascii=False,indent=2))
