"""Reviewer-owned Git/JSON/text checks only. No reference or domain program loads."""
import subprocess, json, hashlib, re, pathlib
ROOT=pathlib.Path.cwd()
REFROOT=pathlib.Path('/workspace/r-b08-reference')
DATA=pathlib.Path(__file__).resolve().parent
BASE='407536adb682a04161d3e9c82f153a62b1becd97'
CAND='18873059e56314fcd48f6081d5a65a79301a52f6'
C1='8ff72341b5b91736970b5bfa5dc1b88137e618a5'
PAY='ab81adc17a0ee50f21032c58036b7b56b28da51b'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
GLOBAL='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
P='review/remediation/20261003-prepare/batches/'
checks=[]
def git(*args,root=ROOT):return subprocess.check_output(['git',*args],cwd=root)
def blob(commit,path):return git('show',commit+':'+path)
def sha(b):return hashlib.sha256(b).hexdigest()
def check(name,ok,detail=None):checks.append({'id':name,'passed':bool(ok),'detail':detail})
def identity(commit,path):
 b=blob(commit,path);return {'commit':commit,'path':path,'git_blob':git('rev-parse',commit+':'+path).decode().strip(),'sha256':sha(b),'bytes':len(b)}
def match(rec,commit=None,path=None):
 i=identity(commit or rec.get('commit') or CAND,path or rec['path'])
 return all(i[k]==rec[k] for k in ['git_blob','sha256','bytes'] if k in rec)
def obj(path,commit=CAND):return json.loads(blob(commit,path))
def paths(a,b):return git('diff','--name-only',a,b).decode().splitlines()
changed=paths(BASE,CAND);norm=[p for p in changed if p.startswith(('deliverables/','specs/'))]
added=[p for p in changed if p not in norm]
check('scope87_14_73',len(changed)==87 and len(norm)==14 and len(added)==73,{'changed':len(changed),'normative':len(norm),'evidence':len(added)})
check('eight_final_six_original',sum(p.startswith('deliverables/') for p in norm)==8 and sum(p.startswith('specs/') for p in norm)==6)
check('only_new_B09_evidence',all(p.startswith(P+'B09/') for p in added) and all(git('diff','--name-status',BASE,CAND,'--',p).startswith(b'A\t') for p in added))
check('candidate_payload_parent',git('rev-parse',CAND+'^').decode().strip()==PAY)
check('payload_candidate1_parent',git('rev-parse',PAY+'^').decode().strip()==C1)
envelope=obj(P+'B09/freeze-envelope-2/payload-manifest.json')
check('payload_tree',git('rev-parse',PAY+'^{tree}').decode().strip()==envelope['payload_tree'])
check('payload_paths_complete',paths(BASE,PAY)==[r['path'] for r in envelope['payload_changed_paths']])
for r in envelope['payload_changed_paths']:
 for k,commit in [('before',BASE),('candidate_1',C1),('after',PAY)]:
  if r.get(k):check('payload_identity:'+k+':'+r['path'],match(r[k],commit,r['path']))
check('amendment_paths_complete',paths(C1,PAY)==envelope['amendment_changed_paths'])
check('full_candidate_inventory',changed==envelope['full_final_changed_paths'])
check('only_four_envelope_additions',paths(PAY,CAND)==sorted(envelope['envelope_expected_new_paths']))
diffs=[]
for field,a,b in [('full_unfiltered_predecessor_to_payload_diff',BASE,PAY),('full_unfiltered_candidate_1_to_payload_diff',C1,PAY)]:
 r=envelope[field];p=P+'B09/freeze-envelope-2/'+r['path'];stored=blob(CAND,p)
 check(field+'_stored_hash',sha(stored)==r['sha256'] and len(stored)==r['bytes'])
 rebuilt=git('diff','--no-ext-diff','--no-textconv','--no-color','--no-renames',a,b)
 check(field+'_reconstructed',rebuilt==stored,{'stored_sha256':sha(stored),'reconstructed_sha256':sha(rebuilt),'no_path_filter':True})
 diffs.append({'path':p,'sha256':sha(stored),'bytes':len(stored),'reconstructed_equal':rebuilt==stored})
ni=obj(P+'B09/candidate-2/normative-identities.json')
check('normative_manifest_exact_scope',sorted(x['after']['path'] for x in ni['files'])==norm)
for r in ni['files']:
 p=r['after']['path']
 check('normative_identity:'+p,match(r['before'],BASE) and match(r['candidate_1'],C1) and match(r['after'],CAND))
check('existing_twelve_payload_bytes_preserved',sum(blob(C1,p)==blob(CAND,p) for p in norm)==12)
approval=obj(P+'B09/scope-amendment-2/approval.json');application=obj(P+'B09/scope-amendment-2/application.json')
check('amendment_proposal_hash',sha(blob(CAND,approval['approved_proposal_path']))==approval['approved_proposal_sha256'])
for r in approval['files']:
 p=r['path'];t=blob(BASE,p).decode()
 for c in r['clause_changes']:
  check('amendment_before_unique:'+p+':'+str(c['before_lines']),t.count(c['before_text'])==1)
  t=t.replace(c['before_text'],c['intended_after_text'],1)
 check('amendment_exact_text:'+p,t.encode()==blob(CAND,p))
 check('amendment_after_identity:'+p,match(r['intended_after'],CAND,p))
 rdiff=r['full_diff'];p2=P+'B09/candidate-1/'+rdiff['path'];check('approved_WP20_patch:'+p,sha(blob(CAND,p2))==rdiff['sha256'] and len(blob(CAND,p2))==rdiff['bytes'])
check('scope_authorization_only',approval['scope_authorization_only'] and not approval['independent_correctness_approval'] and not approval['public_registry_write_authorized'])
check('all_separate_candidate_actual_gates_retained',approval['new_affected_B05_candidate_actual_review_required'] and set(approval['retained_affected_reviews'])=={'B04','B07','B08'})
accepted=obj(P+'B08/acceptance-stage-1/acceptance-manifest.json',BASE)
preserved=[]
shared='deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md'
for r in accepted['accepted_formal_identities']:
 p=r['path'];same=blob(BASE,p)==blob(CAND,p);preserved.append({'path':p,'baseline':identity(BASE,p),'candidate':identity(CAND,p),'identical':same})
 check('accepted_B08_identity:'+p,match(r,BASE) and (same or p==shared))
wp34='deliverables/final-specification-set/pokemon-rules/wp34-breeding-inheritance.md'
exists=git('ls-tree','--name-only',CAND,'deliverables/final-specification-set/pokemon-rules').decode()
wp34s=git('ls-tree','-r','--name-only',CAND,'deliverables/final-specification-set/pokemon-rules','specs/pokemon-rules').decode().splitlines()
wp34s=[p for p in wp34s if pathlib.Path(p).name.startswith('wp34')]
check('WP34_body_unchanged',len(wp34s)>=1 and all(blob(BASE,p)==blob(CAND,p) for p in wp34s),wp34s)
def rows(data):
 out=[]
 for l in data.decode().splitlines():
  m=re.match(r'^\| ([A-Z]+-?[0-9]+[a-z]?) \|',l)
  if m:out.append((m[1],l))
 return out
locks=[]
for p,start in [(shared,b'## CP'),('deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md',b'## W')]:
 b=blob(BASE,p);c=blob(CAND,p)
 before=b.split(start)[0] if p==shared else start+b.split(start,1)[1]
 after=c.split(start)[0] if p==shared else start+c.split(start,1)[1]
 check('protected_catalog_bytes:'+p,before==after,{'bytes':len(before),'sha256':sha(before)})
 br=rows(b);cr=rows(c);old=[i for i,_ in br];cur=[i for i,_ in cr]
 check('old_ID_order_and_multiplicity:'+p,[i for i in cur if i in old]==old and len(cur)==len(set(cur)))
 locks.append({'path':p,'old_rows':len(br),'current_rows':len(cr),'added_ids':[i for i in cur if i not in old],'changed_old_ids':[i for i,l in br if dict(cr)[i]!=l],'protected_sha256':sha(before),'protected_bytes':len(before),'protected_equal':before==after})
coverage=obj(P+'B09/candidate-2/read-coverage.json');bad=[]
for r in coverage['readers']:
 for k in ['frozen_input','current_refreeze','candidate_1_refreeze']:
  if k in r:
   commit=r[k].get('commit') or (C1 if k=='candidate_1_refreeze' else CAND)
   if not match(r[k],commit,r['path']):bad.append((r['path'],k))
check('all70_author_reader_identity_bindings',len(coverage['readers'])==70 and not bad,bad)
controls=json.loads((DATA/'fixed-controls.json').read_text())
globalrows={r['id']:r for r in obj('review/global-independent-review/2026-10-03-fd82a639/findings.json',GLOBAL)}
check('all25_exact_global_control_objects',all(r['original']==globalrows[r['id']] for r in controls['bindings']))
check('all17_B08_accepted_contribution_IDs',set(controls['B08_ids'])=={r['id'] for r in accepted['independent_full_R08_dispositions']} and len(controls['B08_ids'])==17)
check('nine_primary_contributions',sum(r['B08_primary'] for r in accepted['independent_full_R08_dispositions'])==9)
plan=obj('review/remediation-20261003-prepare/finding-acceptance.json','41fffb540c6483f5296ea0d33b789b75180d27ed')
check('all25_exact_approved_acceptance_objects',all(r['acceptance']==plan[r['id']] for r in controls['bindings']))
firstapproval=obj(P+'B09/candidate-1/original-scope-approval.json')
proposal=obj(P+'B09/scope-proposal-1/original-sync-proposal.json')
check('first_five_original_scope_manifest',sha(blob(CAND,P+'B09/scope-proposal-1/original-sync-proposal.json'))==firstapproval['manifest_sha256'])
check('first_original_scope_only',firstapproval['scope_authorized'] and not firstapproval['correctness_approval'])
for r in proposal['files']:
 p=r['path'];check('first_original_before_after:'+p,match(r['before'],BASE,p) and match(r['intended_after'],CAND,p))
 check('first_original_approved_patch:'+p,sha(blob(CAND,r['complete_diff_path']))==r['complete_diff_sha256']==firstapproval['exact_original_patch_sha256'][p])
 t=blob(BASE,p).decode()
 for c in r['clauses']:t=t.replace(c['before_text'],c['intended_after_text'],1)
 check('first_original_exact_clause_reconstruction:'+p,t.encode()==blob(CAND,p))
check('first_original_30_clauses',sum(len(r['clauses']) for r in proposal['files'])==30)
for field,a in [('full_normative_diff',BASE),('complete_amendment_normative_diff',C1)]:
 r=ni[field];stored=blob(CAND,P+'B09/candidate-2/'+r['path']);rebuilt=git('diff','--no-ext-diff','--no-textconv','--no-color','--no-renames',a,CAND,'--',*norm)
 check(field+'_hash_reconstruction',sha(stored)==r['sha256'] and len(stored)==r['bytes'] and rebuilt==stored)
ledger=obj(P+'B09/candidate-2/formal-change-log.json')
texts={p:blob(BASE,p).decode() for p in norm if p.startswith('deliverables/')};bad=[]
for r in ledger['changes']:
 if r['before_text'] not in texts[r['path']] or r['after_text'] not in blob(CAND,r['path']).decode():bad.append(r['clause'])
 texts[r['path']]=texts[r['path']].replace(r['before_text'],r['after_text'],1)
check('73_final_ledger_text_anchors_and_current_after_texts',len(ledger['changes'])==73 and not bad,{'unresolved_texts':bad,'boundary':'Clause ledger mixes excerpts and insertion anchors; it is not an executable replacement patch. Complete normative patch is reconstructed separately.'})
check('all_B08_historical_paths_unchanged',not git('diff','--name-only',BASE,CAND,'--',P+'B08/'))
for r in accepted['independent_full_R08_dispositions']:
 bad=[]
 for row in r['actual_static_row_identities']:
  p=row['path'];lines=blob(CAND,p).splitlines(keepends=True);matches=[l for l in lines if l.startswith(('| '+row['id']+' |').encode())]
  if len(matches)!=1 or sha(matches[0])!=row['sha256'] or len(matches[0])!=row['bytes']:bad.append(row['id'])
 check('accepted_static_row_identities:'+r['id'],not bad,bad)
static=obj(P+'B09/candidate-2/static-cases.json');bad=[]
for r in static['catalog_cases']:
 l=blob(CAND,r['path']).decode().splitlines()[r['line']-1]
 if l!='| '+r['id']+' | '+r['input_and_premises']+' | '+r['static_expected']+' |' or r['executed']:bad.append(r['id'])
check('43_static_case_row_texts_no_execution',len(static['catalog_cases'])==43 and not bad,bad)
check('static_designs_zero_execution',static['executed']==0 and static['runtime_observations']==0 and static['proven_Demo_chains']==0 and not static['reference_simulator_used'])
limits=obj(P+'B09/candidate-2/source-limits.json')
check('inherited_source_limits_exact',limits['contract_source_limits']==accepted['source_limits'])
check('retained_named_limits',limits['contract_source_limits']['retained_source_limits']==['U01–U10','G01–G12','AX01–AX20'])
check('configuration_UNVERIFIED_Plan_A',limits['configuration']['effective_model_reasoning_speed']=='UNVERIFIED' and limits['configuration']['Plan_A_accepted'] and limits['configuration']['configuration_probes']==0 and limits['configuration']['quota_probes']==0)
refreads=json.loads((DATA/'fresh-source-reading-log.json').read_text())['fresh_events']
for r in refreads:
 b=git('show',REF+':'+r['path'],root=REFROOT)
 check('fresh_reference_identity:'+r['path']+':'+str(r['ranges']),sha(b)==r['sha256'] and len(b)==r['bytes'] and git('rev-parse',REF+':'+r['path'],root=REFROOT).decode().strip()==r['git_blob'])
check('reference_fixed_HEAD',git('rev-parse','HEAD',root=REFROOT).decode().strip()==REF)
check('reference_clean',not git('status','--porcelain',root=REFROOT))
whitespace=subprocess.run(['git','diff','--check',BASE,CAND,'--',*norm],cwd=ROOT,capture_output=True)
check('all14_normative_whitespace',whitespace.returncode==0,whitespace.stdout.decode())
report={'baseline':BASE,'candidate':CAND,'checks':checks,'passed':all(x['passed'] for x in checks),'scope':{'changed_paths':changed,'normative_paths':norm,'evidence_paths':added},'accepted_B08_file_preservation':preserved,'catalog_locks':locks,'author_patch_reconstruction':diffs,'fresh_reference_read_events':len(refreads),'runtime_observations':0,'proven_Demo_chains':0,'behavior_vectors_executed':0,'mode':'DOCUMENT_GIT_JSON_TEXT_HASH_ONLY_NOT_SEMANTIC_CERTIFICATION'}
(DATA/'input-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'passed':report['passed'],'failures':[x for x in checks if not x['passed']],'catalog_locks':locks,'read_events':len(refreads)},ensure_ascii=False,indent=2))
