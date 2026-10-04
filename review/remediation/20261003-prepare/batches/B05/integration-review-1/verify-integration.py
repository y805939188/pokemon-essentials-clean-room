import subprocess,pathlib,json,csv,io,re,hashlib,datetime,collections
P=pathlib.Path('/workspace/pokemon-essentials-clean-room'); R=pathlib.Path('/workspace/b05-reference')
T='cc085d618ce8b5ebda82c28a3a1ac9a09dda9a85';U='9576f00e7d3aeb96f7ca8c42caccfba8f808505e';C='1914cd379bcb7c8b6feb13dc3e872b7ded27d9a4';CR='0da269077aa5a02d5cef08021171acf3719e1b69';B='0a12de641542f9a59909d2a950c1de8df17ca09d';M='be9e78e32fd550d5210ab21db0a1868af685f6f5';PAY='b82dde24ae1e0980fe442031e421ea4a709e0981';O='93e10babe0b9c9ef8b3f5277754541b447beeeb4';PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
ROOT='review/remediation/20261003-prepare/';BASE=ROOT+'batches/B05/';ST=BASE+'integration-stage-1/';OUT=P/(BASE+'integration-review-1');OUT.mkdir(parents=True,exist_ok=True)
def g(*a):return subprocess.check_output(['git','-C',str(P),*a])
def txt(c,p):return g('show',c+':'+p).decode()
def blob(c,p):return g('rev-parse',c+':'+p).decode().strip()
def ls(c,p=None):return g('ls-tree','-r','--name-only',c,*([p] if p else [])).decode().splitlines()
def ns(a,b):return [{'status':s,'path':p} for s,p in (r.split('\t',1) for r in g('diff','--no-renames','--name-status',a,b).decode().splitlines())]
def changed(a,b):return [r['path'] for r in ns(a,b)]
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def j(p,c=T):return json.loads(txt(c,p))
def tab(p,c=T):return list(csv.DictReader(io.StringIO(txt(c,p)),delimiter='\t'))
def save(n,x):(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
checks=[]
def ck(n,b,d=None):checks.append({'check':n,'ok':bool(b),'details':d})
old=j(BASE+'review-round-1/independent-static-validation.json',CR); formal=old['formal_paths']; hist=ls(CR,BASE); public=changed(M,PAY);public=[p for p in public if not p.startswith(ST)];ev=ls(T,ST)
ck('full actual diffs include all paths including final evidence',(len(ns(U,T)),len(ns(C,T)))==(86,115))
ck('15 formal files equal reviewed candidate',len(formal)==15 and all(blob(T,p)==blob(C,p) for p in formal))
ck('51 historical B05 records equal candidate report',len(hist)==51 and all(blob(T,p)==blob(CR,p) for p in hist))
ck('10 public and 10 integration evidence paths',len(public)==len(ev)==10)
ck('upstream actual diff fully partitioned',set(changed(U,T))==set(formal+hist+public+ev))
ck('normal two-parent preserving merge',g('show','-s','--format=%P',M).decode().strip().split()==[U,CR])
ck('report direct child of complete candidate',g('show','-s','--format=%P',CR).decode().strip()==C)
ck('merge imports complete 66-path B05 source',set(changed(U,M))==set(changed(B,CR))==set(formal+hist))
ck('merge preserves all source byte identities',all(blob(M,p)==blob(CR,p) for p in formal+hist))
ck('public payload then final evidence-only successor',g('show','-s','--format=%P',PAY).decode().strip()==M and g('show','-s','--format=%P',T).decode().strip()==PAY and set(changed(PAY,T))=={ST+'candidate-to-payload.patch',ST+'upstream-to-payload.patch',ST+'diff-and-freeze.json'})
upstream_protected=[p for p in ls(U) if p not in formal and p not in public]
ck('all preexisting upstream paths outside formal/public unchanged',all(blob(U,p)==blob(T,p) for p in upstream_protected),{'files':len(upstream_protected)})
ck('B01/B02 histories frozen',all(blob(U,p)==blob(T,p) for batch in ['B01','B02'] for p in ls(U,ROOT+'batches/'+batch)))
ck('all PRE0/plan inputs frozen',all(blob(U,p)==blob(T,p) for p in ls(U,'review/remediation-20261003-prepare')))
manifest=j(ST+'integration-manifest.json');registration=j(ST+'finding-registration.json');count=j(ST+'scope-counts.json');df=j(ST+'diff-and-freeze.json');merge=j(ST+'merge-independence.json')
identity_results=[]
def walk(x):
 if isinstance(x,dict):
  if all(k in x for k in ['path','git_blob','sha256','bytes']):
   c=x.get('commit',T);raw=g('show',c+':'+x['path']);identity_results.append({'path':x['path'],'commit_checked':c,'ok':blob(c,x['path'])==x['git_blob'] and sha(raw)==x['sha256'] and len(raw)==x['bytes']})
  for y in x.values():walk(y)
 elif isinstance(x,list):
  for y in x:walk(y)
walk(manifest)
ck('all manifest immutable/current file identities match Git',all(x['ok'] for x in identity_results),{'identities':len(identity_results)})
hashes=tab(ST+'current-hashes.tsv');hash_checks=[]
for x in hashes:
 raw=g('show',T+':'+x['path']);hash_checks.append({'role':x['role'],'path':x['path'],'ok':blob(T,x['path'])==x['git_blob'] and sha(raw)==x['sha256'] and len(raw)==int(x['bytes'])})
ck('current hashes cover exactly formal/public/dependency identities',len(hashes)==35 and collections.Counter(x['role'] for x in hashes)=={'formal':15,'public':10,'dependency':10} and all(x['ok'] for x in hash_checks))
ck('new evidence all JSON parse',(all(isinstance(j(p),(list,dict)) for p in ev if p.endswith('.json'))))
patches=[]
for x in df['full_payload_diffs']:
 raw=g('diff','--binary','--full-index','--no-renames','--no-ext-diff','--no-textconv','--no-color',x['base_commit'],x['target_commit']);record=g('show',T+':'+x['path']);ok=raw==record and sha(raw)==x['sha256'] and len(raw)==x['bytes'];patches.append({'path':x['path'],'ok':ok,'bytes':len(raw),'sha256':sha(raw)})
ck('both stored complete payload patches match independent Git reconstruction',all(x['ok'] for x in patches))
ck('payload freeze name-status arrays match Git',df['accepted_B02_baseline_to_payload_complete_name_status']==[{'change':x['status'],'path':x['path']} for x in ns(U,PAY)] and df['B05_candidate_to_payload_complete_name_status']==[{'change':x['status'],'path':x['path']} for x in ns(C,PAY)])
final_diffs=[]
for base in [U,C]:
 raw=g('diff','--binary','--full-index','--no-renames','--no-ext-diff','--no-textconv','--no-color',base,T)
 final_diffs.append({'base_commit':base,'target_commit':T,'paths':len(ns(base,T)),'bytes':len(raw),'sha256':sha(raw),'name_status':[{'status':x['status'],'path':x['path'],'old_blob':blob(base,x['path']) if x['status']!='A' else None,'new_blob':blob(T,x['path'])} for x in ns(base,T)]})
led=tab(ROOT+'finding-ledger.tsv');approve=tab(ROOT+'approval-ledger.tsv');trace=tab(ROOT+'traceability-successor.tsv')
ck('229 canonical OPEN ledger byte-identical to accepted B02',len(led)==229 and all(x['canonical_state']=='OPEN' and x['required_revision']=='true' for x in led) and blob(U,ROOT+'finding-ledger.tsv')==blob(T,ROOT+'finding-ledger.tsv'))
ck('42 contribution rows preserve original 26 exactly',len(approve)==len(trace)==42 and all(g('show',T+':'+p).startswith(g('show',U+':'+p)) and len(tab(p,U))==26 for p in [ROOT+'approval-ledger.tsv',ROOT+'traceability-successor.tsv']))
ck('contributions unique by finding/candidate',all(len({(x['finding_id'],x['candidate_commit']) for x in a})==42 for a in [approve,trace]))
orig={x['id']:x for x in j('review/global-independent-review/2026-10-03-fd82a639/findings.json',O)};accept=j('review/remediation-20261003-prepare/finding-acceptance.json',PLAN);previous={x['id']:x for x in j(BASE+'review-round-1/finding-dispositions.json',CR)};proposal={x['id']:x for x in j(BASE+'author-v2/registrar-proposals.json')['all_16_ids']};ledger={x['finding_id']:x for x in led};per=[]
for x in registration['dispositions']:
 i=x['id'];binding=x['complete_original_source_binding'];a=next(r for r in approve if r['finding_id']==i and r['candidate_commit']==C);tr=next(r for r in trace if r['finding_id']==i and r['candidate_commit']==C)
 obligations=sorted(set(ledger[i]['contributor_batches'].split(';'))-{'B05','B01'})
 vals={'original_review_fields_preserved':all(x[k]==v for k,v in previous[i].items()),'author_proposal_preserved':x['author_v2_mapping_preserved']==proposal[i],'original_priority_owner_contributors_preserved':x['original_priority']==orig[i]['priority']==ledger[i]['priority'] and x['primary_owner']==ledger[i]['primary_owner'] and x['all_contributor_batches']==ledger[i]['contributor_batches'].split(';'),'original_and_acceptance_hashes_match':binding['original_canonical_sha256']==canon(orig[i]) and binding['approved_acceptance_canonical_sha256']==canon(accept[i]),'remaining_batches_correct':sorted(x['other_batch_obligations'])==obligations,'state_OPEN_pending_not_closed':x['canonical_state']=='OPEN' and x['canonical_status']=='OPEN' and not x['finding_closed'] and not x['integration_verified'] and 'PENDING' in x['actual_integration_review'],'approval_pending_candidate_only':a['canonical_state']=='OPEN' and a['candidate_review_commit']==CR and a['candidate_verdict']=='PASS_SCOPED' and a['integration_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and a['downstream_gate']=='BLOCKED','trace_maps_current_proposal_and_tests':json.loads(tr['current_clause_inputs'])==proposal[i] and tr['static_test_ids_not_executed'].split(';')==x['static_test_ids'] and tr['effective_priority']==orig[i]['priority'],'tests_exist':all('| '+s+' |' in txt(T,x['test_catalog']) for s in x['static_test_ids']),'all_proposal_file_hashes_match':all(sha(g('show',T+':'+p))==h for p,h in proposal[i]['file_sha256'].items())}
 per.append({'id':i,'original_priority':orig[i]['priority'],'B05_primary':x['B05_primary'],'checks':vals,'ok':all(vals.values()),'scope':x['scope_and_acceptance'],'counterexample':x['independent_counterexample_and_neighbor'],'remaining_work':x['remaining_work'],'other_batch_obligations':x['other_batch_obligations'],'tests':x['static_test_ids']})
ck('all 16 public registrations match qualified historical review/owner/tests/remaining',len(per)==16 and all(x['ok'] for x in per),{'failed':[{'id':x['id'],'checks':[k for k,v in x['checks'].items() if not v]} for x in per if not x['ok']]})
ck('233 originals / 229 required / 10 primary / 6 partial / none closed',len(orig)==233 and sum(bool(x['required_revision']) for x in orig.values())==229 and sum(x['B05_primary'] for x in per)==10 and registration['canonical_closed']==0)
# Independent literal row inventories and unchanged shared tails.
def testrows(c,p):
 out={}
 for line in txt(c,p).splitlines():
  if re.match(r'^\| [A-Z]+-?\d+ \|',line):out[line.split('|')[1].strip()]=line
 return out
catalogs=[]
for p,marker in [(formal[8],'## PT：'),(formal[9],'## BR：')]:
 before=testrows(U,p);current=testrows(T,p);catalogs.append({'path':p,'before':len(before),'current':len(current),'added':[s for s in current if s not in before],'modified':[s for s in before if before[s]!=current.get(s)],'deleted':[s for s in before if s not in current],'protected_tail_equal':txt(U,p).split(marker,1)[1]==txt(T,p).split(marker,1)[1]})
ck('catalog inventories 149/190 to 164/213, +38, three named modifications only',[(x['before'],x['current']) for x in catalogs]==[(149,164),(190,213)] and sum(len(x['added']) for x in catalogs)==38 and catalogs[0]['modified']==[] and catalogs[1]['modified']==['FM15','FM20','SH06'] and all(not x['deleted'] and x['protected_tail_equal'] for x in catalogs))
ck('scope-count inventory agrees with actual Git/text',count['affected_catalog_rows_before']==339 and count['affected_catalog_rows_current']==377 and count['new_static_rows']==38 and count['root_approval_contribution_rows']==count['root_trace_contribution_rows']==42)
ck('131 final Markdown and 17 static catalogs',len([p for p in ls(T,'deliverables/final-specification-set') if p.endswith('.md')])==131 and len([p for p in ls(T,'deliverables/final-specification-set/test-catalog') if p.endswith('.md') and not p.endswith('/README.md')])==17)
upcat=['deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md','deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md'];ck('B01/B02 catalogs preserve 51/99 rows',[len(testrows(T,p)) for p in upcat]==[51,99] and all(blob(T,p)==blob(U,p) for p in upcat))
# Old appendix bodies stay exact; two current index lines are updated in place.
append_docs=['audit/source-traceability.md','planning/coverage.md','planning/feature-matrix.md',ROOT+'historical-errata.md',ROOT+'final-integration-review.md']
ck('historic public appendix bodies retain exact upstream suffix',all(txt(T,p).endswith(txt(U,p) if p.endswith('final-integration-review.md') else txt(U,p).split('\n',2)[2]) for p in append_docs))
idx='deliverables/final-specification-set/test-catalog/README.md'
def mask_index(s):return '\n'.join(line for line in s.split('\n') if not line.startswith('| [creature-rpg-wp18-20-24-25-26.md]') and not line.startswith('| [pokemon-rules-wp19-21-22-23-34.md]'))
ck('test README modifies only two batch index lines then appends successor',mask_index(txt(T,idx)).startswith(mask_index(txt(U,idx))))
links=[]
for p in public+[ST+'README.md']:
 for dest in re.findall(r'\]\(([^)]+)\)',txt(T,p)):
  if '://' in dest or dest.startswith('#'):continue
  path=pathlib.PurePosixPath(p).parent/dest.split('#')[0]
  # historical existing links are retained; only added destinations need validating here
  if ']('+dest+')' in txt(U,p) if p in public else False:continue
  norm=str(pathlib.Path(str(path)));ok=(P/norm).exists();links.append({'from':p,'destination':dest,'ok':ok})
ck('all new public/evidence Markdown local links resolve',all(x['ok'] for x in links),{'links':len(links),'failed':[x for x in links if not x['ok']]})
reference=j(BASE+'review-round-1/source-reading-log.json');refhash=all(sha((R/x['path']).read_bytes())==x['sha256'] for x in reference['source_files']);refhead=subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD'],text=True).strip();reftree=subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD^{tree}'],text=True).strip();refclean=not subprocess.check_output(['git','-C',str(R),'status','--porcelain'])
ck('fixed reference clean with all 26 corrected prior source identities',refhead=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' and reftree=='7589c800b61ba13a13040ed0d686979b80a84fd0' and refclean and refhash)
ck('locator errata retained and public successor points at correction','001_Utilities.rb:450–490' in txt(T,BASE+'review-round-1/evidence-locator-errata.md') and '001_Utilities.rb:450–490' in txt(T,'audit/source-traceability.md') and '定位勘误' in txt(T,ROOT+'historical-errata.md'))
result={'reviewer':'R-B05','reviewed_integration_commit':T,'accepted_upstream_commit':U,'candidate_commit':C,'candidate_report_commit':CR,'checks':checks,'all_checks_pass':all(x['ok'] for x in checks),'per_id':per,'catalogs':catalogs,'reference':{'head':refhead,'tree':reftree,'clean':refclean,'26_corrected_prior_file_hashes_equal':refhash},'new_findings':[],'runtime_observations':0,'demo_chains':0,'behavioral_vectors_executed':0,'author_or_old_reviewer_scripts_executed':False,'this_script_method':'Independent read-only Git/JSON/text/hash audit; no reference programs, compiled data, behavior emulation or solver.'}
save('independent-validation.json',result);save('complete-diff-manifest.json',{'reviewed_commit':T,'reviewed_tree':g('rev-parse',T+'^{tree}').decode().strip(),'diffs':final_diffs,'formal_paths':formal,'preserved_B05_record_paths':hist,'public_paths':public,'all_10_integration_evidence_paths':ev,'three_final_evidence_files':changed(PAY,T),'payload_patch_verifications':patches,'identity_checks':identity_results,'current_hash_checks':hash_checks});save('new-link-check.json',links)
print('checks',len(checks),'all_pass',result['all_checks_pass'])
for x in checks:
 if not x['ok']:print('FAILED',x['check'],x['details'])
