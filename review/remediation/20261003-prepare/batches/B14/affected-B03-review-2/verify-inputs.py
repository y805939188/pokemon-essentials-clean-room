#!/usr/bin/env python3
"""Independent round2 Git/text/JSON/hash/document-ID audit only."""
import collections,csv,hashlib,io,json,pathlib,re,subprocess
D=pathlib.Path(__file__).resolve().parent
P=next(x for x in D.parents if (x/'.git').exists())
REF=pathlib.Path('/workspace/reference-b03')
B='1e6b11a47370f1c7c4659a32443fc1afda597bac'
C1='47f7514765f8569ae9172bb06a2cd615e2b83b8a'
C='af39efbf32549be964cb083bd49bed6d1d5c0d2a'
S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
G='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
AP='review/remediation/20261003-prepare/'
BP=AP+'batches/B14/'
CON=AP+'batches/B09/acceptance-stage-1/B14-downstream-contract.json'
E='deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'
Q='deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
checks=[]
def need(v,label):
 checks.append({'check':label,'pass':bool(v)})
 if not v:raise AssertionError(label)
def git(*args,repo=P):return subprocess.check_output(['git',*args],cwd=repo)
def raw(rev,p,repo=P):return git('show',rev+':'+p,repo=repo)
def obj(rev,p):return json.loads(raw(rev,p))
def sha(b):return hashlib.sha256(b).hexdigest()
def stable(d):return sha(json.dumps(d,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def ident(rev,p,repo=P):
 b=raw(rev,p,repo);return {'commit':rev,'path':p,'git_blob':git('rev-parse',rev+':'+p,repo=repo).decode().strip(),'sha256':sha(b),'bytes':len(b)}
def dump(p,d):(D/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
need(git('rev-parse','HEAD').decode().strip()==C,'fixed candidate2 before report commit')
need(git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/review-B14-affected-B03-2','prescribed independent branch')
need(git('merge-base','--is-ancestor',C1,C)==b'','candidate1 ancestry')
need(git('merge-base','--is-ancestor',B,C)==b'','accepted predecessor ancestry')
contract=obj(B,CON)
refreeze=obj(C1,BP+'author-stage-1/input-refreeze.json')
dependency_versions=[]
for group in ['planned_reads','write_inputs','current_extra_inputs']:
 for row in refreeze[group]:
  baseline_rev=row.get('verified_commit',B)
  i=ident(baseline_rev,row['path'])
  need(all(i[q]==row[q] for q in ['git_blob','sha256','bytes']),'fixed accepted dependency identity '+group+' '+row['path'])
  def available(rev):
   exists=subprocess.run(['git','cat-file','-e',rev+':'+row['path']],cwd=P,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
   return ident(rev,row['path']) if exists else None
  c1_i=available(C1);c2_i=available(C)
  dependency_versions.append({'group':group,'path':row['path'],'accepted_or_fixed_external':i,'candidate1':c1_i,'candidate2':c2_i,'changed_from_accepted':None if c2_i is None else i['git_blob']!=c2_i['git_blob'],'fixed_external_input_not_required_in_candidate_tree':c2_i is None})
need(len(refreeze['planned_reads'])==72 and len(refreeze['write_inputs'])==6,'complete planned72/write6 identity inventory; no semantic full-domain reread claim')
for row in contract['whole_catalog_locks']:
 i=ident(B,row['path']);need(all(i[q]==row['baseline'][q] for q in ['git_blob','sha256','bytes']),'accepted whole-file catalogue lock identity '+row['path'])
package=next(x for x in obj(C1,BP+'candidate-1/reverse-impact-packages.json')['accepted_owner_packages'] if x['accepted_owner']=='B03')
gate=next(x for x in contract['accepted_reverse_review_gates'] if x['accepted_batch']=='B03')
need(package['contract_gate']==gate,'exact B03 request matches accepted B09-C contract')
need(raw(C1,BP+'candidate-1/reverse-impact-packages.json')==raw(C,BP+'candidate-1/reverse-impact-packages.json'),'candidate1 package preserved; independent successor review mandatory')
deltas=[]
for start,end,n in [(B,C,'accepted_B09_to_candidate2'),(C1,C,'candidate1_to_candidate2')]:
 data=git('diff','--binary','--full-index','--no-renames','--no-ext-diff','--no-textconv','--no-color',start,end)
 rows=[x.split('\t',1) for x in git('diff','--name-status','--no-renames',start,end).decode().splitlines()]
 inventory=[]
 for status,p in rows:
  item={'status':status,'path':p,'after':ident(end,p)}
  if status!='A':item['before']=ident(start,p)
  inventory.append(item)
 count=46 if start==B else 22
 need(len(rows)==count,'complete unfiltered path inventory '+n)
 need(all(status=='A' and p.startswith(BP) or status=='M' and p.startswith(('specs/','deliverables/')) for status,p in rows),'all cumulative/incremental paths inside authorized formal or new B14 evidence '+n)
 deltas.append({'name':n,'before':start,'after':end,'method':'git diff --binary --full-index --no-renames --no-ext-diff --no-textconv --no-color; no exclusions','bytes':len(data),'sha256':sha(data),'path_count':len(rows),'paths':inventory})
revised=obj(C,BP+'candidate-2/revised-identities.json')
formal_paths=[x['path'] for x in deltas[0]['paths'] if x['path'].startswith(('specs/','deliverables/'))]
need(len(formal_paths)==12 and sorted(formal_paths)==sorted(x['path'] for x in revised['documents']),'twelve exact cumulative formal paths')
need(len([x for x in deltas[1]['paths'] if x['status']=='M'])==8,'eight formal changes from candidate1')
for row in revised['documents']:
 for rev,k in [(B,'accepted_B09_before'),(C1,'candidate1_before'),(C,'after')]:
  i=ident(rev,row['path']);need(all(i[q]==row[k][q] for q in ['git_blob','sha256','bytes']),'revised full identity '+rev[:7]+' '+row['path'])
 need((raw(C1,row['path'])!=raw(C,row['path']))==row['changed_in_candidate2'],'changed flag '+row['path'])
for x in deltas[0]['paths']:
 if x['status']=='A' and '/candidate-2/' not in x['path']:
  need(raw(C1,x['path'])==raw(C,x['path']),'candidate1 original approval/author evidence immutable '+x['path'])
amend=obj(C,BP+'candidate-2/bounded-amendment-1.json')
application=obj(C,BP+'candidate-2/amendment-application.json')
need(amend['state']=='EXPLICIT_PARENT_SCOPE_AUTHORIZED_RECORDED_BEFORE_APPLICATION_NOT_CORRECTNESS_APPROVAL','appended scope is not correctness approval')
need(all(ident(C,BP+'candidate-2/bounded-amendment-1.json')[q]==application['before_application_record'][q] for q in ['git_blob','sha256','bytes']),'scope/application whole identity')
for row in amend['documents']:
 before=ident(C1,row['path']);after=ident(C,row['path']);patch=BP+'candidate-2/'+row['patch']
 need(all(before[q]==row['before'][q] and after[q]==row['intended_after'][q] for q in ['git_blob','sha256','bytes']),'appended amendment actual before/after '+row['path'])
 need(sha(raw(C,patch))==row['patch_sha256'],'appended approved patch exact '+patch)
 ar=next(x for x in application['documents'] if x['path']==row['path'])
 need(all(after[q]==ar['actual_after'][q] for q in ['git_blob','sha256','bytes']),'application actual identity '+row['path'])
 if 'wp16-' in row['path']:
  a=raw(C1,row['path']).splitlines(keepends=True);b=raw(C,row['path']).splitlines(keepends=True)
  need(len(a)==len(b) and sum(x!=y for x,y in zip(a,b))==1,'WP16 exactly one line changed '+row['path'])
need(sha(raw(C,BP+'candidate-2/original-FLY-amendment.patch'))==revised['original_FLY_patch_sha256'],'original FLY amendment exact byte identity')
for row in gate['changed_planned_reverse_readers']:
 before=ident(B,row['path'])
 need(all(before[q]==row['current_baseline'][q] for q in ['git_blob','sha256','bytes']),'stale accepted B03 reader baseline '+row['path'])
source_controls={x['id']:x for x in contract['contribution_controls']}
original={x['id']:x for x in obj(G,'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
acceptance=obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
control_ids=gate['shared_control_ids']+['GIR-FD82-C103','GIR-FD82-C104','GIR-FD82-C088','GIR-FD82-C100','GIR-FD82-C092','GIR-FD82-C093']
bindings=[]
for fid in control_ids:
 k=source_controls[fid];o=original[fid];a=acceptance[fid]
 need(stable(o)==k['whole_original_object_sha256'] and stable(a)==k['whole_acceptance_object_sha256'],'whole original/effective acceptance '+fid)
 for field,v in k['complete_current_control_fields'].items():need(v==o.get(field),'complete current field '+fid+' '+field)
 need(k['complete_minimum_acceptance_fields']['acceptance_gate']==a['acceptance_gate'],'complete acceptance gate '+fid)
 bindings.append({'id':fid,'scope':'B03 affected shared control' if fid in gate['shared_control_ids'] else 'Adjacent interface only; no whole B14/B04 approval','complete_contract_control':k})
owner=obj('dea9d118d7ed3b7ddb57b1c4e7bd40db8dd06497',AP+'batches/B03/integration-review-1/finding-dispositions.json')
owner_paths=sorted({e['path'] for x in owner['dispositions'] for e in x['actual_project_evidence']}|{x['path'] for x in obj('dea9d118d7ed3b7ddb57b1c4e7bd40db8dd06497',AP+'batches/B03/integration-review-1/complete-diff-manifest.json')['formal_payload']})
need(len(owner_paths)==13,'accepted B03 complete formal ownership inventory')
for p in owner_paths:
 if p!=E:need(raw(B,p)==raw(C,p),'accepted B03 formal owner file unchanged '+p)
catalogs=[]
def rows(b):return [(m[1].decode(),l) for l in b.splitlines(keepends=True) if (m:=re.match(rb'^\| ([A-Z]+[A-Z0-9-]*\d+) \|',l))]
for p in [E,Q]:
 versions={k:rows(raw(rev,p)) for k,rev in [('accepted',B),('candidate1',C1),('candidate2',C)]}
 new=dict(versions['candidate2']);summary={'path':p,'versions':{},'behavior_execution':0}
 for k,rr in versions.items():
  need(len(dict(rr))==len(rr),'unique static IDs '+p+' '+k)
  summary['versions'][k]=len(rr)
 for k in ['accepted','candidate1']:
  old=dict(versions[k]);need([i for i,l in versions['candidate2'] if i in old]==[i for i,l in versions[k]],'all old ID order/multiplicity '+p+' '+k)
  changed=[i for i,l in versions[k] if new[i]!=l];added=[i for i,l in versions['candidate2'] if i not in old]
  allow=(['WT03','WT07','WT09','WT14','WT15','WT17','WT18','WT20','WT23','WT25','FS02','FS03','FS06'] if p==E else ['FP01','FP02','FP06','FP12','FP14','FP15']) if k=='accepted' else (['WT28'] if p==E else ['BP18'])
  need(changed==allow,'exact changed row set '+p+' '+k)
  if k=='candidate1':need(added==(['WT39','WT40'] if p==E else []),'only two new WT39/40 IDs '+p)
  summary[k+'_comparison']={'changed_old_ids':changed,'added_ids':added,'preserved_old_ids':[i for i,l in versions[k] if i not in changed]}
  for i,l in versions[k]:
   if i not in changed:need(new[i]==l,'old row byte preservation '+k+' '+i)
 if p==E:
  own=[i for i,l in versions['accepted'] if re.sub(r'\d+$','',i) in ['MP','MV','EV','FW','IM','MR','DG']]
  need(len(own)==251 and all(dict(versions['accepted'])[i]==new[i] for i in own),'251 accepted B03 rows preserved')
  b04=[i for i,l in versions['accepted'] if i.startswith('B04-R')]
  need(len(b04)==28 and all(dict(versions['accepted'])[i]==new[i] for i in b04),'28 B04-R rows preserved')
  need(raw(B,p).split(b'## H.',1)[0]==raw(C,p).split(b'## H.',1)[0],'entire shared engine prefix before H preserved')
 else:need(all(dict(versions['accepted'])['BP'+str(i).zfill(2)]==new['BP'+str(i).zfill(2)] for i in range(1,18)),'BP01–17 including GR012 preserved')
 catalogs.append(summary)
need(sum(x['versions']['accepted'] for x in catalogs)==480 and sum(x['versions']['candidate1'] for x in catalogs)==503 and sum(x['versions']['candidate2'] for x in catalogs)==505,'480→503→505 static inventory only')
need(not git('diff','--name-only',B,C,'--',AP+'batches/B03/',AP+'batches/B09/acceptance-stage-1/',AP+'finding-ledger.tsv',AP+'approval-ledger.tsv',AP+'traceability-successor.tsv').strip(),'accepted history and public registries unchanged')
ledger=list(csv.DictReader(io.StringIO(raw(C,AP+'finding-ledger.tsv').decode()),delimiter='\t'))
need(len(ledger)==229 and all(x['canonical_state']=='OPEN' for x in ledger),'229 canonical OPEN / zero closures')
reports=[]
for sha1,p,fkey in [('06dd362d2eb2674453646c899c9fd76af0841c8e',BP+'affected-B03-review-1/findings.json','new_findings'),('0579404a69952d24e9901664a611f5a05a01877e',BP+'review-round-1/findings.json','findings'),('3aa4c41de2f58bd65405bc0855a7f45155a878c2',BP+'affected-B04-review-1/findings.json','blocking_findings')]:
 d=obj(sha1,p);need(d['verdict']=='REQUEST_CHANGES' and d['reviewed_candidate']==C1,'immutable round1 finding input '+sha1)
 reports.append({'input':ident(sha1,p),'verdict':d['verdict'],'whole_findings':d[fkey]})
response=obj(C,BP+'candidate-2/fix-response.json')
for row in response['review_inputs']:
 i=ident(row['commit'],row['path']);need(all(i[q]==row[q] for q in ['git_blob','sha256','bytes']),'all six author-bound immutable round1 input identities '+row['path'])
need([x['id'] for x in response['fixes']]==['B14-AFFECTED-B03-001','R-B14-1-001','B14-B04-R1-01'],'three original findings traced without duplication')
for row in response['successor_local_traceability']:
 i=ident(C1,row['old_entry']['path']);need(all(i[q]==row['old_entry'][q] for q in ['git_blob','sha256','bytes']),'appended successor trace keeps old contribution identity '+row['id'])
need(response['contribution_count']==24 and response['primary_count']==19 and response['canonical_root_count_changed'] is False,'full R14 scope retained but not approved by affected B03')
need(git('rev-parse','HEAD',repo=REF).decode().strip()==S and git('rev-parse','HEAD^{tree}',repo=REF).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0' and not git('status','--porcelain',repo=REF).strip(),'fixed independent reference HEAD/tree/clean')
whitespace=[]
for start,label in [(B,'B09-C2'),(C1,'C1-C2')]:
 result=subprocess.run(['git','diff','--check',start,C],cwd=P,capture_output=True,text=True)
 warnings=[l for l in result.stdout.splitlines() if re.match(r'.*:\d+: ',l)]
 need(all(l.split(':',1)[0].endswith('.patch') for l in warnings),'raw whitespace warnings confined to evidence patch files '+label)
 paths=[x['path'] for x in deltas[0 if start==B else 1]['paths'] if not x['path'].endswith('.patch')]
 nonpatch=subprocess.run(['git','diff','--check',start,C,'--',*paths],cwd=P,capture_output=True,text=True)
 need(nonpatch.returncode==0,'nonpatch formal/evidence whitespace '+label)
 whitespace.append({'delta':label,'raw_returncode':result.returncode,'raw_warnings':len(warnings),'raw_warning_paths':dict(collections.Counter(l.split(':',1)[0] for l in warnings)),'nonpatch_returncode':nonpatch.returncode})
manifest={'run_id':'20261003-prepare','reviewed_candidate':C,'candidate_tree':git('rev-parse',C+'^{tree}').decode().strip(),'candidate1':C1,'accepted_predecessor':B,'reference':S,'complete_unfiltered_deltas':deltas,'B03_request_package':package,'accepted_contract_identity':ident(B,CON),'contract_lock_dependency_versions':{k:contract[k] for k in ['planned_dependencies','dependency_baselines','whole_catalog_locks','fixed_original_findings','fixed_approved_acceptance','candidate_and_actual_gates','additional_current_B09_normative_inputs','current_B09_actual_review_receipts']},'planned_dependency_versions':dependency_versions,'revised_twelve_formal_identity_inventory':revised,'bounded_amendment_identity':ident(C,BP+'candidate-2/bounded-amendment-1.json'),'B03_formal_owner_inventory':[{'path':p,'accepted':ident(B,p),'candidate2':ident(C,p),'unchanged':raw(B,p)==raw(C,p)} for p in owner_paths],'prior_scope_approval_commit':'b37533ef1cfc7808ed41d64215647a78d165ada4','round1_findings':reports,'all_six_round1_report_input_identities':response['review_inputs'],'inventory_is_not_full_B14_B04_B09_semantic_approval':True,'actual_integration_checked':False}
dump('input-identity-manifest.json',manifest)
dump('qualified-control-bindings.json',bindings)
dump('catalog-preservation.json',{'candidate2':C,'catalogs':catalogs,'B03_rows_preserved':251,'B04_R_rows_preserved':28,'behavior_execution':0})
dump('independent-validation.json',{'result':'PASS_GIT_TEXT_JSON_HASH_DOCUMENT_INVENTORY_ONLY','semantic_verdict_separate':True,'reviewed_candidate':C,'check_count':len(checks),'checks':checks,'raw_whitespace_checks':whitespace,'reference_behavior_execution':0,'static_design_execution':0,'runtime_observations':0,'canonical_closed':0,'actual_integration_checked':False})
print(json.dumps({'checks':len(checks),'cumulative_paths':46,'incremental_paths':22,'formal_paths':12,'catalog_total':505,'whitespace':whitespace,'semantic_verdict_separate':True},ensure_ascii=False))
