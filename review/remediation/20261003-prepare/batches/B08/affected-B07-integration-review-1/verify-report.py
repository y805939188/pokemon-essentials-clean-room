#!/usr/bin/env python3
"""Report integrity and scope checks only; not behavioral tests."""
import pathlib,json,hashlib,subprocess,collections
O=pathlib.Path(__file__).resolve().parent;ROOT=O.parents[5];A='49c21538e72b7a5873972cd00fcae1ee390cce64';checks=[]
def get(n):return json.loads((O/n).read_text())
def ck(n,v):checks.append({'check':n,'pass':bool(v)})
def sha(b):return hashlib.sha256(b).hexdigest()
m=get('artifact-manifest.json')
for r in m['files']:
 p=O/r['file'];ck('artifact bytes/hash '+r['file'],p.is_file() and p.stat().st_size==r['bytes'] and sha(p.read_bytes())==r['sha256'])
actual=get('B07-conclusion-dispositions.json');h=get('handoff.json');s=get('source-reading-log.json');di=get('complete-diff-identities.json');v=get('independent-document-checks.json');g=get('B04-affected-gate.json')
ck('exact actual disposition',actual['actual']==A and len(actual['records'])==19 and sum(x['B07_primary'] for x in actual['records'])==12)
ck('19 unique IDs',len({x['id'] for x in actual['records']})==19)
for r in actual['records']:
 ck('scoped actual case '+r['id'],r['actual']==A and r['verdict']=='PASS_SCOPED_B07_CONTRIBUTION_PRESERVED_AT_EXACT_B08_ACTUAL' and not r['canonical_closure'] and bool(r['independent_positive_static_reasoning']) and bool(r['independent_negative_or_reverse_control']) and bool(r['actual_semantic_recheck']))
 for row in r['static_rows_current_exact']:
  ck('current actual row locator '+r['id']+'/'+row['static_id'],row['actual_commit']==A and bool(row['actual_lines']))
ck('own checks all pass',v['actual']==A and v['passed']==v['check_count']==1233 and not v['failed'])
ck('full path counts131/74',[len(x['complete_path_statuses']) for x in di['complete_diffs']]==[131,74] and all(x['selected_paths'] is None for x in di['complete_diffs']))
ck('actual12/source108/public10/integration13',[len(di[k]) for k in ['formal12_actual','source108_identities','public10_actual','integration13_actual']]==[12,108,10,13])
ck('five-reader actual preserved',len(get('dependency-and-preservation.json')['five_changed_reverse_readers'])==5)
ck('author comparison after frozen judgment',get('author-comparison.json')['comparison_performed_after_independent_first_judgment'] and get('independent-first-judgment.json')['verdict']=='PASS_SCOPED')
ck('other actual and parent gates',h['three_same_actual_passes_then_parent_C_required'] and not h['full_R08_actual_approval'] and not h['bounded_R04_actual_approval'] and not h['parent_C_acceptance'] and not h['downstream_unlock'] and h['canonical_closures']==0 and g['actual_bounded_B04_review_required'])
ck('requested/effective scope',get('configuration-and-scope-receipt.json')['requested_reasoning']=='Ultra' and all(get('configuration-and-scope-receipt.json')[k]=='UNVERIFIED' for k in ['effective_model','effective_reasoning','effective_speed']) and get('configuration-and-scope-receipt.json')['derived_subtasks']==0)
ck('zero execution observations demos',all(s[k]==0 for k in ['reference_execution','behavior_vectors_executed','runtime_observations','proven_Demo_chains']))
ck('fresh ranges count',len(s['files'])==23 and sum(x['fresh_unique_lines'] for x in s['files'])==1948 and s['fresh_events']==25)
for f in s['files']:
 a={i for l,u in f['fresh_opened_ranges'] for i in range(l,u+1)};b={i for l,u in f['unread_this_round_ranges'] for i in range(l,u+1)}
 ck('fresh/read complement '+f['path'],len(a)==f['fresh_unique_lines'] and not a&b and a|b==set(range(1,f['file_lines']+1)))
ck('complete prior named limits retained',bool(s['inherited_exact_named_limits']['retained_limits']) and bool(s['inherited_exact_named_limits']['unread_named_content']) and bool(s['inherited_exact_named_limits']['additional_limits']))
ck('report contains verdict/actual/19cases',all(x in (O/'report.md').read_text() for x in ['PASS_SCOPED',A,'UNVERIFIED','AUTHOR_SELF_REPORT_ONLY',*[r['id'] for r in actual['records']]]))
status=subprocess.check_output(['git','-C',str(ROOT),'status','--porcelain','-uall']).decode().splitlines();allowed=str(O.relative_to(ROOT))+'/'
ck('only new authorized directory dirty',all(s[3:].startswith(allowed) for s in status))
ck('single exact actual branch base',subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD']).decode().strip()==A)
result={'reviewed_actual':A,'operation':'Own report integrity/scope checks; no behavioral execution','check_count':len(checks),'passed':sum(x['pass'] for x in checks),'failed':[x for x in checks if not x['pass']],'checks':checks,'validated_artifact_manifest_sha256':sha((O/'artifact-manifest.json').read_bytes())}
(O/'report-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='checks'}));assert not result['failed']
