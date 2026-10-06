"""Own report consistency/hash/privacy/publication bookkeeping, not behavior tests."""
import completion_read as R
import json,gzip,pathlib,re,hashlib
O=R.OUT;checks=[]
def check(name,ok):
 checks.append({'check':name,'passed':bool(ok)})
 assert ok,name
required=['report.md','findings.json','independent-first-judgment.md','first-judgment-receipt.json','author-comparison.md','review-manifest.json','input-identities.json','reading-log.json','static-designs.json']
for n in required:check('Required current artifact '+n,(O/n).is_file())
f=json.loads((O/'findings.json').read_text());m=json.loads((O/'review-manifest.json').read_text());i=json.loads((O/'input-identities.json').read_text());r=json.loads((O/'reading-log.json').read_text());d=json.loads((O/'static-designs.json').read_text());c=json.loads((O/'completion-current-disposition.json').read_text());native=R.gzload('completion-native-verification.json.gz')
check('Current exact-ACT B03 PASS consistent',all(x['verdict']=='PASS_SCOPED' for x in [f,m,c]) and all(x['reviewed_ACT']==R.ACT for x in [f,r,d,c]))
check('Current reading and author comparison complete',r['complete_semantic_review'] and m['complete_semantic_review'] and m['author_comparison_complete'] and not r['remaining_required_review_reading'] and not native['semantic_remainder'])
check('No ACT payload defect or canonical closure invented',not f['new_scoped_issues'] and not f['new_payload_gameplay_findings'] and not f['new_canonical'] and not f['canonical_closed'] and not f['acceptance'])
check('Exactly24 unique current B14 slices',len(f['current_B14_contribution_dispositions'])==24 and len({x['id'] for x in f['current_B14_contribution_dispositions']})==24)
check('Exactly27 accepted B03 qualified dispositions',len(f['current_accepted_B03_owner_dispositions'])==27 and len({x['id'] for x in f['current_accepted_B03_owner_dispositions']})==27)
loc=json.loads(R.git(R.ACT,R.BASE+'integration-stage-1/clause-location-bindings.json'))['records']
for x in f['current_B14_contribution_dispositions']:
 check('Canonical current locator '+x['id'],x['current_locators_binding']['selector']=='/records/'+x['id'] and x['id'] in loc)
check('Pending B14 actual registration retained',all(x['ACT_contribution_status']=='INTEGRATED_PENDING_ACTUAL' and not x['accepted'] and x['canonical_state']=='OPEN' and not x['candidate_receipts_are_actual_PASS'] for x in f['current_B14_contribution_dispositions']))
check('Four prior observations and three historical qualifications',len(f['prior_observation_dispositions'])==4 and len(f['historical_C3_report_qualification_dispositions'])==3 and all(x['disposition']=='HISTORICAL_REPORT_ONLY_QUALIFICATION' for x in f['historical_C3_report_qualification_dispositions']))
check('All8 same-ACT gates remain separate',m['all8_same_ACT_gates_still_required'] and not m['this_actual_gate_only']['B14_accepted'])
check('No report-SHA recursion or reviewed/report substitution',m['roles']['this_report_commit'] is None and i['report_SHA']['value'] is None and m['roles']['reviewed_ACT']!=m['roles']['candidate'])
check('Backend effective UNVERIFIED',m['configuration']['effective_configuration']=='UNVERIFIED' and i['configuration']['backend_certificate'] is None)
check('Static designs and limits unexecuted',not d['executed'] and f['limits']['runtime_observations']==0 and f['limits']['proven_Demo_chains']==0 and f['limits']['behavior_vectors_executed']==0)
for n,h in [('independent-first-judgment.md','4d281d2f2b849df89d3ece67356d38c5bbb42957cf252eb60020fad0208bc393'),('first-judgment-receipt.json','1708eedfbd1b2f721385df94be7b99714636c510edb7a7875d8144599b7a701b')]:check('Immutable '+n,R.h((O/n).read_bytes())==h)
snap=json.loads((O/'preliminary-turn-1/snapshot-manifest.json').read_text())
check('All26 initial files exact locally',len(snap['files'])==26 and all(R.h((O/'preliminary-turn-1'/x['path']).read_bytes())==x['sha256'] and len((O/'preliminary-turn-1'/x['path']).read_bytes())==x['bytes'] for x in snap['files']))
included=[];excluded=[];patterns=[rb'/Users/[A-Za-z0-9_.-]+/',rb'/home/[A-Za-z0-9_.-]+/',rb'/private/tmp/[A-Za-z0-9_.-]+',rb'/tmp/[A-Za-z0-9_.-]+',rb'/private/var/[A-Za-z0-9_.-]+'];skip={'publication-manifest.json','completion-report-qa.json'}
for p in sorted(O.rglob('*')):
 if not p.is_file():continue
 n=p.relative_to(O).as_posix();raw=p.read_bytes();row={'path':n,'bytes':len(raw),'sha256':R.h(raw)}
 if '__pycache__/' in n or p.suffix=='.pyc':
  excluded.append({**row,'role':'LOCAL_IMMUTABLE_PRESERVATION_ONLY','reason':'Compiled cache embeds private host provenance; no execution/deserialization and no public publication.'});continue
 if n in skip:continue
 body=gzip.decompress(raw) if n.endswith('.gz') else raw
 check('No private host-path values '+n,not any(re.search(v,body) for v in patterns))
 if n.endswith(('.json','.json.gz')):
  json.loads(body);check('Valid own JSON '+n,True)
 if n.startswith('preliminary-turn-1/'):
  row['role']='INITIAL_PRELIMINARY_TURN1_RECORD_NOT_CURRENT_REVIEW'
 elif n in ['independent-first-judgment.md','first-judgment-receipt.json']:
  row['role']='IMMUTABLE_PROVISIONAL_FIRST_RECEIPT_NOT_FINAL_PASS'
 elif n.startswith('completion-') or n.startswith('completion_') or n in required:
  row['role']='CURRENT_COMPLETION_REPORT_OR_READING_RECONSTRUCTION_BOOKKEEPING'
 else:row['role']='INITIAL_BOOKKEEPING_OR_GENUINELY_CONSUMED_INITIAL_MAP_RETAINED_WITH_EXACT_BINDING'
 included.append(row)
result={'kind':'Own report/document/hash/privacy/JSON consistency checks only; no behavior or historical verifier execution','reviewed_ACT':R.ACT,'current_verdict':'PASS_SCOPED','scope':'B03 only','checks':checks,'all_passed':True,'publication_exclusions':excluded,'first_receipt_and_preliminary_preserved':True,'no_ACT_repair':True}
R.save('completion-report-qa.json',result)
qa=(O/'completion-report-qa.json').read_bytes();included.append({'path':'completion-report-qa.json','bytes':len(qa),'sha256':R.h(qa),'role':'CURRENT_REPORT_DOCUMENT_QA_NOT_BEHAVIOR_TESTS'})
R.save('publication-manifest.json',{'reviewed_ACT':R.ACT,'verdict':'PASS_SCOPED','role':'B03 actual gate only','report_SHA':None,'assigned_externally':True,'publication_owner':'Coordinator mechanical publication only; no quality acceptance by publisher','strict_allowlist':included,'excluded_local_preservation':excluded,'snapshot_manifest_sha256':R.h((O/'preliminary-turn-1/snapshot-manifest.json').read_bytes()),'recursive_self_hash_required':False,'public_paths_logical_only':True,'all8_actual_gates_still_required_before_AREG_C':True})
print('REPORT_QA_PASS',len(checks),'SAFE_PUBLIC_FILES',len(included),'LOCAL_ONLY_FILES',len(excluded));print('report.md',R.h((O/'report.md').read_bytes()));print('publication-manifest.json',R.h((O/'publication-manifest.json').read_bytes()))
