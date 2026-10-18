#!/usr/bin/env python3
"""Qualify mechanical pointer kinds; no truth, semantic PASS, or FULL inference."""
from pathlib import Path
import collections,datetime,hashlib,json,re,gzip
OUT=Path(__file__).resolve().parent
RR=OUT.parents[2]
def sha(b):return hashlib.sha256(b).hexdigest()
def get(n):return json.loads((OUT/n).read_bytes())
def put(n,d):
 with (OUT/n).open('w') as f:json.dump(d,f,ensure_ascii=False,separators=(',',':'));f.write('\n')
idx=get('index.json');inp=get('inputs.json');val=get('validation.json')
literal_links=get('links.json')['links']
direct_link_tasks=collections.defaultdict(set)
for link in literal_links:
 if link.get('kind')=='LITERAL_EXISTING_ARTIFACT_PATH':direct_link_tasks[link['to']].add(link['task'])
qualified_roots=[]
for b in inp['candidate_root_bindings']:
 tasks=set()
 for link in b['links']:
  if link.get('depth')==0 or str(link.get('from','')).startswith('adjudication/') or link.get('kind')=='EXPLICIT_ROOT_READER_NAME_DIRECTORY_NAVIGATION_ONLY':tasks.add(link['task'])
 qualified_roots.append((b['directory']+'/',tasks))
def allowed_receipt_tasks(artifact):
 allowed=set(direct_link_tasks.get(artifact,()))
 for prefix,tasks in qualified_roots:
  if artifact.startswith(prefix):allowed.update(tasks)
 return allowed
def input_identity(p,role):
 raw=p.read_bytes();key=str(p.relative_to(RR))
 rec={'path':key,'bytes':len(raw),'sha256':sha(raw),'roles':[role]}
 if not any(x['path']==key for x in inp['inputs']):inp['inputs'].append(rec)
 return json.loads(raw)

assignments=collections.defaultdict(list)
for p in sorted((RR/'delegation/readsets').glob('*.json')):
 d=input_identity(p,'ORIGINAL_READSET_ASSIGNMENT_ONLY_NO_READING_CREDIT')
 def visit(v,j=''):
  if isinstance(v,dict):
   for k,x in v.items():visit(x,j+'/'+k.replace('~','~0').replace('/','~1'))
  elif isinstance(v,list):
   for i,x in enumerate(v):visit(x,j+'/'+str(i))
  elif isinstance(v,str):
   for row in idx['rows']:
    if v==row['path']:
     assignments[(row['kind'],row['path'])].append({'readset':str(p.relative_to(RR)),'pointer':j,'task_name_navigation_only':p.stem})
 visit(d)

priority_dir=RR/'tasks/coverage_acceptance_incremental/delta-inputs/root-primaries/formal_shared'
priority={}
for n in ['reading-ledger.json','identities.json','forward-mapping.json','reverse-mapping.json','interfaces.json','progress.json']:
 p=priority_dir/n
 if p.exists():priority[n]=input_identity(p,'PARENT_REQUESTED_THREE_SHARED_FORMAL_QUALIFICATION_NAVIGATION_ONLY')
pri_summary={'schema':'gr8-three-shared-formal-original-metadata-finding/v1','whole_read_original':priority.get('reading-ledger.json'),
 'progress_original':priority.get('progress.json'),'interfaces_original':priority.get('interfaces.json'),
 'forward_reverse_scope_original':{n:{k:v for k,v in d.items() if k!='records'} for n,d in priority.items() if n in ['forward-mapping.json','reverse-mapping.json']},
 'forward_groups_original':[{k:v for k,v in x.items() if k in ['id','actual_reader','disposition','formal_locators']} for x in priority.get('forward-mapping.json',{}).get('records',[])],
 'interpretation':'Original explicit /root FULL_READ with actual chunks exists for3frozen files. Original18finite groups and3OPEN interface obligations do not constitute current task-final acceptance. Reuse original whole reading credit only subject to root provenance/qualification reception; no new reading credit here.'}
put('three-shared-formal-priority.json',pri_summary)

unmatched=[]
class_counts=collections.Counter()
for row in idx['rows']:
 row['original_assignment_pointers_only']=assignments.get((row['kind'],row['path']),[])
 fixed=row['fixed_identity']
 for c in row['candidate_groups']:
  artifact=c['artifact'];ps=c['path_pointers']
  allowed=allowed_receipt_tasks(artifact)
  c['incidental_directory_receipts_removed']=[x['task'] for x in c['exact_current_root_receipts'] if x['task'] not in allowed]
  c['exact_current_root_receipts']=[x for x in c['exact_current_root_receipts'] if x['task'] in allowed]
  states=c['status_fields_original'];ranges=c['range_and_qualification_fields_original']
  reader=c['reader_fields_original']
  # Pointer context and explicit row fields determine kind only; status words do not determine truth.
  if any('/administrative_dispositions/' in p for p in ps):typ='ADMINISTRATIVE_IDENTITY_OR_TYPED_METADATA_ONLY'
  elif re.search(r'forward|reverse|source-to-spec|clause-to-source',Path(artifact).name):typ='MAPPING_AUTHOR_OR_FINITE_RECEIVER_FIELD_ONLY'
  elif 'manifest' in Path(artifact).name:typ='MANIFEST_IDENTITY_ONLY'
  elif 'identit' in Path(artifact).name and not (states and ranges):typ='INPUT_IDENTITY_ONLY'
  elif re.search(r'ledger|reading',Path(artifact).name) and states and ranges:typ='EXPLICIT_PATH_READING_ENTRY_CANDIDATE'
  elif re.search(r'ledger|reading',Path(artifact).name):typ='LEDGER_PATH_OCCURRENCE_WITHOUT_COMPLETE_LOCAL_READING_ATTESTATION'
  else:typ='OTHER_EXACT_PATH_METADATA_CANDIDATE'
  c['pointer_kind_only']=typ;class_counts[typ]+=1
  c['reader_field_qualification']='Original field values at these pointers only. Mapping author, finite receiver, administrative reader and source whole reader are distinct; no transfer is inferred.'
  # Identify conflicts explicitly; absence of local identity remains unknown rather than silently inherited.
  comparisons=[]
  keymap={'bytes':'bytes','observed_bytes':'bytes','git_bytes':'bytes','sha256':'sha256','observed_sha256':'sha256','blob':'git_blob','git_blob':'git_blob','actual_blob':'git_blob','commit':'commit','frozen_commit':'commit'}
  for x in c['identity_fields_original']:
   k=x['pointer'].rsplit('/',1)[-1]
   if k in keymap and fixed.get(keymap[k]) is not None:
    comparisons.append({'pointer':x['pointer'],'fixed_key':keymap[k],'matches':x['value']==fixed[keymap[k]]})
  c['local_identity_comparisons_only']=comparisons
  c['local_identity_status']='CONFLICT_PRESENT_NO_TRANSFER' if any(not x['matches'] for x in comparisons) else ('EXPLICIT_LOCAL_VALUES_MATCH' if comparisons else 'NO_LOCAL_IDENTITY_VALUES_UNKNOWN')
  # Do not repeat the entire root registry entry in every candidate.
  c['exact_current_root_receipts']=[{'task':x['task'],'registry_pointer':x['registry_pointer'],'receipt_path':x.get('receipt_path',x.get('expected',{}).get('path')),'inputs_pointer':'/root_receipts/'+x['task'],'exact_current_match':x['exact_current_match']} for x in c['exact_current_root_receipts']]
 credible=[c for c in row['candidate_groups'] if c['pointer_kind_only']=='EXPLICIT_PATH_READING_ENTRY_CANDIDATE' and c['reader_fields_original'] and c['local_identity_status']!='CONFLICT_PRESENT_NO_TRANSFER']
 received=[c for c in credible if c['exact_current_root_receipts']]
 row['mapping_status']='EXPLICIT_READING_ENTRY_AND_CURRENT_TASK_RECEIPT_CANDIDATE' if received else 'INCOMPLETE_READING_ENTRY_OR_CURRENT_RECEIPT_MAPPING'
 row['not_a_source_coverage_decision']=True
 reasons=[]
 if not row['candidate_groups']:reasons.append('NO_EXACT_PATH_IN_SELECTED_ORIGINAL_OWNER_METADATA')
 if not credible:reasons.append('NO_NONCONFLICTING_EXPLICIT_LOCAL_READING_ENTRY_WITH_NAMED_READER')
 if not received:reasons.append('NO_SUCH_READING_ENTRY_BOUND_TO_CURRENT_ROOT_TASK_RECEIPT_CANDIDATE')
 if row['path'] in ['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md']:
  row['parent_requested_primary_qualification']='three-shared-formal-priority.json: original /root full reading exists;18finite dispositions+3OPEN interfaces/task-final NOT_SIGNED preserved. Other scope-statement finite peer reads do not replace this current whole-task qualification.'
  reasons.append('FORMAL_SHARED_CURRENT_TASK_FINAL_NOT_SIGNED_ORIGINAL_FINITE_QUALIFICATION_REMAINS')
 if reasons:unmatched.append({'kind':row['kind'],'path':row['path'],'reasons':reasons,'candidate_artifacts':sorted({c['artifact'] for c in row['candidate_groups']}),'disposition':'UNKNOWN_MAPPING_NOT_MATERIAL_LIMIT_NOT_SEMANTIC_FAIL'})
# Keep the complete generated navigation details in a gzip artifact; compact index is lossless pointer grouping.
with gzip.open(OUT/'candidate-details.json.gz','wt',encoding='utf-8',compresslevel=6) as f:json.dump(idx,f,ensure_ascii=False,separators=(',',':'))
def compress_pointers(pointers):
 exact=[];patterns=collections.defaultdict(set)
 for p in set(pointers):
  m=re.match(r'^(.*?/)(\d+)(/[^0-9].*|)$',p)
  if m:patterns[(m[1],m[3])].add(int(m[2]))
  else:exact.append(p)
 out={'exact':sorted(exact),'indexed_runs':[]}
 for (pre,suf),ns in sorted(patterns.items()):
  runs=[]
  for n in sorted(ns):
   if runs and n==runs[-1][1]+1:runs[-1][1]=n
   else:runs.append([n,n])
  out['indexed_runs'].append({'prefix':pre,'inclusive_index_runs':runs,'suffix':suf})
 return out
def merge_fields(groups,key):
 by=collections.defaultdict(list);original={}
 for c in groups:
  for x in c.get(key,[]):
   # Only literal original values are grouped; pointer omission markers stay explicit.
   value={k:v for k,v in x.items() if k!='pointer'}
   h=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'))
   original[h]=value;by[h].append(x['pointer'])
 return [{**original[h],'original_pointer_set':compress_pointers(ps)} for h,ps in sorted(by.items())]
before=sum(len(r['candidate_groups']) for r in idx['rows'])
for row in idx['rows']:
 by=collections.defaultdict(list)
 for c in row['candidate_groups']:by[(c['artifact'],c['pointer_kind_only'])].append(c)
 compact=[]
 for (artifact,typ),cs in sorted(by.items()):
  receipts={x['task']:x for c in cs for x in c['exact_current_root_receipts']}
  compact.append({'artifact':artifact,'pointer_kind_only':typ,'path_pointer_set':compress_pointers(p for c in cs for p in c['path_pointers']),
   'owner_task_candidates':sorted({t for c in cs for t in c['owner_task_candidates']}),
   'reader_fields_original':merge_fields(cs,'reader_fields_original'),'status_fields_original':merge_fields(cs,'status_fields_original'),
   'range_and_qualification_fields_original':merge_fields(cs,'range_and_qualification_fields_original'),
   'identity_fields_original':merge_fields(cs,'identity_fields_original'),
   'exact_current_root_receipts':list(receipts.values()),
   'local_identity_comparisons_only':merge_fields(cs,'local_identity_comparisons_only'),
   'local_identity_statuses_original_candidates':sorted({c['local_identity_status'] for c in cs}),
   'navigation_labels_only':sorted({x for c in cs for x in c['navigation_labels_only']}),
   'incidental_directory_receipts_removed':sorted({x for c in cs for x in c['incidental_directory_receipts_removed']}),
   'qualification':'Lossless grouping of original pointer/value fields within artifact and pointer kind. No original status overwrite or semantic/FULL transfer. Whole-file own reading differs finite mapping/received source facts.'})
 row['candidate_groups']=compact
idx['schema']='gr8-fixed-path-evidence-pointer-candidates/v2'
idx['pointer_encoding']='inclusive_index_runs expands prefix+decimal(index)+suffix; exact pointers retained separately. Original field values grouped by exact JSON value, never interpreted as semantic PASS.'
put('index.json',idx)
put('unmatched.json',{'schema':'gr8-mechanical-mapping-unmatched/v2','qualification':'Conservative local reading-entry/reader/identity/receipt pointer qualification only, not semantic coverage. No missing mapping is converted to a material limit.','rows':unmatched})
put('inputs.json',inp)
val['qualifier_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
val['pointer_kind_counts']=dict(class_counts)
val['paths_with_candidate_reader_and_receipt']=sum(x['mapping_status']=='EXPLICIT_READING_ENTRY_AND_CURRENT_TASK_RECEIPT_CANDIDATE' for x in idx['rows'])
val['unmatched_paths']=len(unmatched)
val['input_artifacts']=len(inp['inputs'])
val['raw_candidate_groups_not_semantic_denominator']=before
val['compact_artifact_kind_groups_not_semantic_denominator']=sum(len(r['candidate_groups']) for r in idx['rows'])
val['three_shared_formal_current_taskfinal_not_signed_preserved']=True
val['registry_snapshot_still_exact_at_qualification']=sha((RR/'adjudication/root-primary-task-final-registry.v1.json').read_bytes())==inp['registry_snapshot_sha256']
val['all_index_rows_no_FULL_or_PASS_grant']=all(not x['individual_FULL_granted'] and x['semantic_PASS'] is None for x in idx['rows'])
put('validation.json',val)
text=(OUT/'report.md').read_text()
text+='\n附加机械资格：`pointer_kind_only` 区分原读账条目、mapping作者/finite接收者、manifest身份和行政身份。原本地身份冲突逐字段标出；无本地身份保持 UNKNOWN。保守索引有 '+str(val['paths_with_candidate_reader_and_receipt'])+' 路径具原显式读账/具名reader/当前收据候选，'+str(len(unmatched))+' 路径仍有机械缺口。这不是语义覆盖率。\n\n父请求核查的3份公共formal另见 `three-shared-formal-priority.json`：原root全文阅读可追溯，18有限组、3OPEN接口及task-final未签原资格同时保留。\n'
(OUT/'report.md').write_text(text)
print(json.dumps({'paths':len(idx['rows']),'explicit_reading_and_receipt_candidates':val['paths_with_candidate_reader_and_receipt'],'unmatched':len(unmatched),'pointer_kinds':dict(class_counts)},ensure_ascii=False))

