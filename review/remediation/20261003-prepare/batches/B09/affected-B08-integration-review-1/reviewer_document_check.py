"""New R-B08 actual review: Git/text/JSON identities only. No domain execution."""
import csv, hashlib, io, json, pathlib, re, subprocess
ROOT=pathlib.Path('/workspace/r-b08-b09-actual-review')
TMP=pathlib.Path('/tmp/r-b08-b09-actual')
ACTUAL='dc64807c2d726171827017ec636c6a73efd8e4b5'
CAND='18873059e56314fcd48f6081d5a65a79301a52f6'
BASE='407536adb682a04161d3e9c82f153a62b1becd97'
PAYLOAD='3ec4af10f9822999b329ac794e4694bc5aa89aac'
GLOBAL='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
P='review/remediation/20261003-prepare/'
G=P+'batches/B09/integration-stage-1/'
PRIOR=P+'batches/B09/affected-B08-review-round-1/'
checks=[];cache={}
def git(*args,root=ROOT):return subprocess.check_output(['git',*args],cwd=root)
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(c,p):
 key=(c,p)
 if key not in cache:cache[key]=git('show',c+':'+p,root=pathlib.Path('/workspace/r-b08-reference') if c==REF else ROOT)
 return cache[key]
def identity(c,p):
 b=blob(c,p);return {'commit':c,'path':p,'git_blob':sha1blob(b),'sha256':sha(b),'bytes':len(b)}
def sha1blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def check(n,ok,e=None):checks.append({'check':n,'passed':bool(ok),'evidence':e})
def j(c,p):return json.loads(blob(c,p))
def matches(rec,c=None):
 c=c or rec.get('commit') or ACTUAL
 i=identity(c,rec['path']);return all(i[k]==rec[k] for k in ['git_blob','sha256','bytes'] if k in rec)
def walk(v,label):
 if isinstance(v,dict):
  if all(k in v for k in ['path','git_blob','sha256','bytes']):
   try:check('identity:'+label,matches(v),{'commit':v.get('commit',ACTUAL),'path':v['path']})
   except subprocess.CalledProcessError as e:check('identity:'+label,False,{'path':v['path'],'read_error':str(e)})
  for k,x in v.items():walk(x,label+'/'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):walk(x,label+'/'+str(i))
def changed(a,b):return git('diff','--no-ext-diff','--no-textconv','--no-renames','--name-status',a,b).decode().splitlines()
def full(a,b):return git('diff','--no-ext-diff','--no-textconv','--no-renames','--binary',a,b)
check('exact_frozen_HEAD',git('rev-parse','HEAD').decode().strip()==ACTUAL)
check('exact_reference_HEAD',git('rev-parse','HEAD',root=pathlib.Path('/workspace/r-b08-reference')).decode().strip()==REF)
check('reference_clean',not git('status','--porcelain',root=pathlib.Path('/workspace/r-b08-reference')))
manifest=j(ACTUAL,G+'integration-manifest.json');readers=j(ACTUAL,G+'current-readers.json');dep=j(ACTUAL,G+'downstream-dependency-assessment.json');freeze=j(ACTUAL,G+'diff-and-freeze.json');reg=j(ACTUAL,G+'finding-registration.json')
diffs=[]
for label,a,b,count in [('baseline-actual',BASE,ACTUAL,199),('candidate-actual',CAND,ACTUAL,112),('payload-actual',PAYLOAD,ACTUAL,3)]:
 d=full(a,b);stored=(TMP/(label+'.diff')).read_bytes();paths=[s.split('\t',1)[1] for s in changed(a,b)]
 check(label+':full_unfiltered_stream',d==stored and len(paths)==count)
 diffs.append({'before':a,'after':b,'command':['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary',a,b],'path_filter_used':False,'sha256':sha(d),'bytes':len(d),'lines':d.count(b'\n'),'changed_path_count':len(paths),'paths':[{'change':s.split('\t',1)[0],'before':identity(a,p) if s.startswith('M\t') else None,'after':identity(b,p)} for s,p in zip(changed(a,b),paths)]})
for name,before,count in [('upstream-to-payload-identities.json',BASE,196),('candidate-to-payload-identities.json',CAND,109)]:
 d=j(ACTUAL,G+name);stream=full(before,PAYLOAD);inventory=changed(before,PAYLOAD)
 check(name+':unfiltered_payload_stream',sha(stream)==d['diff_sha256'] and len(stream)==d['diff_bytes'] and stream.count(b'\n')==d['diff_lines'] and len(inventory)==count and not d['path_filter_used'])
 check(name+':full_path_inventory',[s.split('\t',1)[1] for s in inventory]==[x['path'] for x in d['changed_paths']])
 walk(d['changed_paths'],name)
for name in ['integration-manifest.json','diff-and-freeze.json','current-readers.json','downstream-dependency-assessment.json','finding-registration.json','scope-and-observation-registration.json','scope-counts.json']:
 walk(j(ACTUAL,G+name),name)
check('175_source_identities',len(manifest['source_identities'])==175)
for r in manifest['source_identities']:check('source175_byte_preserved:'+r['path'],matches(r,ACTUAL))
norm=[r['path'] for r in manifest['reviewed_normative_identities']]
check('all14_normative_candidate_actual_unchanged',len(norm)==14 and all(blob(CAND,p)==blob(ACTUAL,p) for p in norm))
check('14_normative_8_final_6_original',sum(p.startswith('deliverables/') for p in norm)==8 and sum(p.startswith('specs/') for p in norm)==6)
public=manifest['public_write_paths'];stage=manifest['management_stage_paths'];tail=manifest['final_freeze_paths']
reportpaths=[]
for r in manifest['candidate_reports']:
 ps=git('ls-tree','-r','--name-only',r['commit'],'--',r['report_directory']).decode().splitlines();reportpaths+=ps
 check('candidate_report_directory_complete:'+r['role'],len(ps)==r['path_count'])
 for p in ps:check('candidate_report_bytes:'+p,blob(r['commit'],p)==blob(ACTUAL,p))
check('all88_candidate_reports',len(reportpaths)==88 and len(set(reportpaths))==88)
check('candidate_actual_only_report_public_management',set(x.split('\t',1)[1] for x in changed(CAND,ACTUAL))==set(reportpaths+public+stage+tail))
check('baseline_actual_only_declared_199',set(x.split('\t',1)[1] for x in changed(BASE,ACTUAL))==set([r['path'] for r in manifest['source_identities']]+public+stage+tail))
check('final_child_single_parent_and_three_additions',git('rev-list','--parents','-n','1',ACTUAL).decode().strip().split()==[ACTUAL,PAYLOAD] and set(x.split('\t',1)[1] for x in changed(PAYLOAD,ACTUAL))==set(tail) and all(s.startswith('A\t') for s in changed(PAYLOAD,ACTUAL)))
for r in manifest['normal_native_merges']:
 parents=git('rev-list','--parents','-n','1',r['result']).decode().strip().split()[1:]
 check('native_merge_parents_tree:'+r['result'],parents==r['parents'] and git('rev-parse',r['result']+'^{tree}').decode().strip()==r['tree'])
 check('native_merge_contains_before_source:'+r['result'],subprocess.run(['git','merge-base','--is-ancestor',r['before'],r['result']],cwd=ROOT).returncode==0 and subprocess.run(['git','merge-base','--is-ancestor',r['source'],r['result']],cwd=ROOT).returncode==0)
check('70_current_readers_and4_scopes',len(readers['readers'])==70 and len(readers['affected_current_scopes'])==4 and len(readers['current_public_versions'])==10)
for r in readers['readers']:
 c=r['reviewed_candidate'].get('commit',CAND);a=r['actual_current'].get('commit',ACTUAL)
 check('current_reader_changed_flag:'+r['path'],r['candidate_to_actual_changed']==(blob(c,r['path'])!=blob(a,r['path'])))
check('B14_assessment_72_reads_6_writes',len(dep['B14']['all72_current_assessment_inputs'])==72 and len(dep['B14']['allowed6_write_input_versions'])==6)
check('B14_formal_blocked_not_author_baseline',dep['B14']['formal_writer_authorized'] is False and dep['B14']['assessment_is_author_baseline'] is False and 'BLOCKED' in dep['B14']['status'])
check('no_downstream_dispatch_or_parallel_formal',dep['tasks_dispatched']==dep['parallel_formal_writers_authorized']==0)
check('six_reciprocal_dependency_paths_and_shared_root',len(dep['B09_B14_serialization']['B09_writes_B14_reads'])==2 and len(dep['B09_B14_serialization']['B14_writes_B09_reads'])==4 and dep['B09_B14_serialization']['shared_control_IDs']==['GIR-FD82-003'] and dep['B09_B14_serialization']['semantic_independence'] is False)
globalrows={r['id']:r for r in j(GLOBAL,'review/global-independent-review/2026-10-03-fd82a639/findings.json')};plan=j(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
controls=j(ACTUAL,PRIOR+'fixed-controls.json');accepted=j(BASE,P+'batches/B08/acceptance-stage-1/acceptance-manifest.json')
check('25_fixed_full_original_and_acceptance_objects',len(controls['bindings'])==25 and all(r['original']==globalrows[r['id']] and r['acceptance']==plan[r['id']] for r in controls['bindings']))
check('all17_B08_9primary_retained',set(controls['B08_ids'])=={r['id'] for r in accepted['independent_full_R08_dispositions']} and len(controls['B08_ids'])==17 and sum(r['B08_primary'] for r in accepted['independent_full_R08_dispositions'])==9)
for r in reg['dispositions']:
 check('registration_all_current_controls:'+r['id'],all(v==globalrows[r['id']].get(k) for k,v in r['complete_current_control_fields'].items()))
 check('registration_all_minimum_acceptance:'+r['id'],all(v==plan[r['id']].get(k) for k,v in r['complete_minimum_acceptance_fields'].items()))
 check('registration_not_closure:'+r['id'],r['canonical_state']=='OPEN' and r['canonical_edited'] is False and r['canonical_closure'] is False and r['accepted_B09_contributions']==0)
check('B09_20_dispositions_13_primary',len(reg['dispositions'])==20 and sum(r['B09_primary'] for r in reg['dispositions'])==13)
for name in ['approval-ledger.tsv','traceability-successor.tsv']:
 p=P+name;b=blob(BASE,p);a=blob(ACTUAL,p);bl=b.splitlines(keepends=True);al=a.splitlines(keepends=True)
 check('public_history_first150_rows_exact:'+name,len(bl)==151 and len(al)==171 and al[:151]==bl)
 rows=list(csv.DictReader(io.StringIO(a.decode()),delimiter='\t'));new=rows[-20:]
 check('public_20_current_candidate_rows:'+name,{r['finding_id'] for r in new}=={r['id'] for r in reg['dispositions']} and all(r['canonical_state']=='OPEN' and r['candidate_commit']==CAND for r in new))
 for r,d in zip(new,reg['dispositions']):
  ob=json.loads(r['remaining_obligations'])
  check('public_obligations:'+name+':'+r['finding_id'],r['finding_id']==d['id'] and ob['other_batch_obligations']==d['other_contributors_pending'] and ob['canonical_closure'] is False and ob['parent_C']=='NOT_PERFORMED' and len(ob['candidate_receipts'])==5)
  if name=='approval-ledger.tsv':check('public_pending_actual:'+r['finding_id'],r['integration_verdict']=='NOT_REVIEWED_PENDING_FIVE_ULTRA_STANDARD' and r['downstream_gate']=='BLOCKED')
  else:
   clauses=json.loads(r['current_clause_inputs']);check('public_clause_inputs:'+r['finding_id'],clauses['reviewed_candidate']==CAND and clauses['clauses']==d['formal_clause_locators'])
check('accepted_B08_producer12_context',len(accepted['accepted_formal_identities'])==12)
for r in accepted['accepted_formal_identities']:
 p=r['path']
 if 'test-catalog/pokemon-rules-wp31-32-37-38.md' not in p:check('B08_producer_unchanged:'+p,blob(BASE,p)==blob(ACTUAL,p))
 else:
  b=blob(BASE,p).split(b'## CP',1)[0];a=blob(ACTUAL,p).split(b'## CP',1)[0]
  check('B08_BE_CX_RM_catalog_prefix_retained',b==a,{'bytes':len(b),'sha256':sha(b)})
wp34=git('ls-tree','-r','--name-only',BASE).decode().splitlines()
for p in wp34:
 if '/wp34-' in p and (p.startswith('specs/') or p.startswith('deliverables/')):check('WP34_body_immutable:'+p,blob(BASE,p)==blob(ACTUAL,p))
matrix=j(ACTUAL,PRIOR+'contribution-preservation.json')
for d in matrix['dispositions']:
 for r in d['current_static_row_identities']:
  rows=blob(ACTUAL,r['path']).splitlines(keepends=True);hits=[l for l in rows if re.match(rb'^\|\s*'+re.escape(r['id'].encode())+rb'\s*\|',l)]
  check('current_B08_static_row:'+d['id']+':'+r['id'],len(hits)==1 and sha(hits[0])==r['sha256'] and len(hits[0])==r['bytes'])
for r in json.loads((TMP/'fresh-source-reads.json').read_text()):check('fresh_reference_text_identity:'+r['path']+':'+str(r['ranges']),matches(r))
for r in csv.DictReader(io.StringIO(blob(ACTUAL,G+'current-hashes.tsv').decode()),delimiter='\t'):
 if 'path' not in r:continue
 check('management_current_hash:'+r['path'],matches({'path':r['path'],'git_blob':r['git_blob'],'sha256':r['sha256'],'bytes':int(r['bytes'])},ACTUAL))
check('five_separate_actual_gates_required',len(manifest['actual_gates'])==5 and all('PENDING' in r['status'] for r in manifest['actual_gates']))
check('no_B09_acceptance_canonical_closure_or_execution',manifest['accepted_B09_contributions']==0 and manifest['canonical_OPEN']==229 and manifest['canonical_CLOSED']==0 and manifest['reference_execution']==manifest['author_reviewer_program_execution']==manifest['behavior_vectors_executed']==manifest['runtime_observations']==manifest['proven_Demo_chains']==0)
for p in [s.split('\t',1)[1] for s in changed(BASE,ACTUAL) if s.endswith('.json')]:
 j(ACTUAL,p);check('changed_JSON_parse_only:'+p,True)
for name,count in [('input-inspection.json',511),('validation-results.json',799)]:
 d=j(ACTUAL,G+name);check('management_claim_structure:'+name,len(d['checks'])==count and all(c.get('pass_') is True for c in d['checks']))
counts=j(ACTUAL,G+'scope-counts.json')
def rows(b):
 return [(m.group(1).decode(),line) for line in b.splitlines(keepends=True) if (m:=re.match(rb'^\|\s*((?:BC-|CM-|SW-|G|R|E|BE|CX|RM|CP|W|T|F|S|H|P|C)[0-9]+[a-z]?)\s*\|',line))]
for p,c in counts['catalog_counts'].items():
 old=rows(blob(BASE,p));new=rows(blob(ACTUAL,p));od=dict(old);nd=dict(new)
 check('catalog_ordinal_IDs_and_multiplicity:'+p,[i for i,_ in old]==[i for i,_ in new if i in od] and len(new)==len(nd))
 check('catalog_counts_and_old_edits:'+p,len(old)==c['before'] and len(new)==c['after'] and [i for i,_ in new if i not in od]==c['added_ids'] and [i for i,l in old if nd[i]!=l]==c['changed_old_ids'])
for r in counts['protected_whole_sections']:
 def section(b):
  text=b.decode();start=text.index(r['heading']);end=text.find('\n## ',start+1);return text[start:end+1 if end>=0 else len(text)].encode()
 a=section(blob(ACTUAL,r['path']));b=section(blob(BASE,r['path']))
 check('protected_section:'+r['heading'],a==b and sha(a)==r['sha256'] and len(a)==r['bytes'])
for c,directory in [('aa7ed0226f36220c1ac6ad598bdcad132aee5e4b',P+'batches/B09/integration-review-1/'),('2790043cc7f605fd58489806ce2dc8c54ffbeb2c',P+'batches/B09/affected-B05-integration-review-1/')]:
 changes=changed(ACTUAL,c)
 check('external_actual_receipt_only_new_reports:'+c,git('rev-list','--parents','-n','1',c).decode().strip().split()==[c,ACTUAL] and all(s.startswith('A\t'+directory) for s in changes))
 for p in reportpaths:check('external_receipt_preserves_candidate_history:'+c+':'+p,blob(c,p)==blob(ACTUAL,p))
(TMP/'full-diff-identities.json').write_text(json.dumps(diffs,ensure_ascii=False,indent=2)+'\n')
report={'reviewed_actual':ACTUAL,'mode':'NEW_REVIEWER_GIT_TEXT_JSON_ONLY_NOT_BEHAVIOR_TESTS','checks':checks,'count':len(checks),'passed':all(x['passed'] for x in checks),'failures':[x for x in checks if not x['passed']]}
(TMP/'input-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'count':report['count'],'passed':report['passed'],'failures':report['failures']},ensure_ascii=False,indent=2))
