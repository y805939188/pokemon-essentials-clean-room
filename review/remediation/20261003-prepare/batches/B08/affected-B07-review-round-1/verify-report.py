"""Validate report consistency and artifact hashes, without any reference execution."""
import hashlib,json,pathlib,re,subprocess
ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT=ROOT/'review/remediation/20261003-prepare/batches/B08/affected-B07-review-round-1'
CAND='0f35a393d9de467cd5f7e695b6072687bb582186'
BASE='759eee80ce7856570fde2de12d5dcf98ce7e6017'
REFROOT=pathlib.Path('/workspace/reference-pokemon-essentials-B07')
checks=[]
def ck(n,b):checks.append({'check':n,'pass':bool(b)})
def doc(n):return json.loads((OUT/n).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
for p in OUT.glob('*.json'):json.loads(p.read_text());ck('JSON parses '+p.name,True)
de=doc('dependency-and-preservation.json');sc=doc('complete-diff-identities.json')
ck('exact before and after IDs in manifest',sc['baseline']==BASE and sc['candidate']==CAND and de['baseline']==BASE and de['candidate']==CAND)
for k in ['complete_diff','output_diff']:
 r=sc[k];b=(OUT/r['artifact']).read_bytes();ck('whole diff artifact identity '+k,sha(b)==r['sha256'] and len(b)==r['bytes'])
rows=doc('B07-conclusion-dispositions.json')['records'];controls=doc('fixed-control-bindings.json')['records']
ck('19 preserved conclusions12primary, no closed status',len(rows)==19 and sum(r['B07_primary'] for r in rows)==12 and all(r['canonical_status']=='OPEN' and not r['canonical_closure'] for r in rows))
ck('same19 full original controls',set(r['id'] for r in rows)==set(r['id'] for r in controls))
for r in rows:
 c=next(c for c in controls if c['id']==r['id'])
 ck('complete controls align '+r['id'],c['original_complete_object_sha256']==r['complete_original_object_sha256'] and c['acceptance_complete_object_sha256']==r['complete_acceptance_object_sha256'])
 for z in r['static_rows_current_exact']:
  b=subprocess.check_output(['git','-C',str(ROOT),'show',CAND+':'+z['path']]).decode().splitlines()
  lines=[b[n-1] for n in z['candidate_lines']]
  ck('current static evidence '+r['id']+'/'+z['static_id'],sha('\n'.join(lines).encode())==z['row_sha256'] and len(lines)==z['ordered_occurrences'] and all(l.startswith('| '+z['static_id']+' |') for l in lines))
source=doc('source-reading-log.json')
for r in source['files']:
 b=(REFROOT/r['path']).read_bytes();ck('read-only reference file identity '+r['path'],len(b)==r['bytes'] and sha(b)==r['sha256'])
 opened={n for a,b in r['fresh_opened_text_ranges'] for n in range(a,b+1)}
 unread={n for a,b in r['not_opened_this_review_ranges'] for n in range(a,b+1)}
 ck('fresh reading/open-unread partition '+r['path'],len(opened)==r['fresh_unique_lines'] and not opened&unread and opened|unread==set(range(1,r['total_lines']+1)))
ck('reference HEAD and clean status',subprocess.check_output(['git','-C',str(REFROOT),'rev-parse','HEAD']).decode().strip()=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' and not subprocess.check_output(['git','-C',str(REFROOT),'status','--porcelain']).strip())
ck('fresh27paths2369 unique lines',source['fresh_reference_paths']==27 and source['fresh_unique_lines']==2369 and sum(r['fresh_unique_lines'] for r in source['files'])==2369)
ck('own288 checks pass',doc('independent-document-checks.json')['passed']==288 and not doc('independent-document-checks.json')['failed'])
ck('author143 bookkeeping checks pass',doc('author-comparison.json')['passed']==143 and not doc('author-comparison.json')['failed'])
ck('first judgment unchanged since comparison',sha((OUT/'independent-first-judgment.json').read_bytes())==doc('author-comparison.json')['first_judgment_sha256'])
ck('new B04 candidate/actual gate retained',doc('independent-first-judgment.json')['additional_affected_B04_review_required'] and doc('B04-affected-gate.json')['decision']=='REQUIRED_SEPARATE_AFFECTED_B04_CANDIDATE_AND_ACTUAL_ULTRA_STANDARD' and doc('B04-affected-gate.json')['new_B04_report_pending'])
ck('no new canonical roots or closures',doc('new-findings.json')['new_canonical_roots']==0 and doc('new-findings.json')['canonical_OPEN']==229 and doc('new-findings.json')['canonical_CLOSED']==0)
report=(OUT/'report.md').read_text()
ck('all19 canonical IDs in final report',all(r['id'] in report for r in rows))
ck('report exact scopes/configuration',all(s in report for s in [CAND,BASE,'PASS_SCOPED','UNVERIFIED','AUTHOR_SELF_REPORT_ONLY','344','14个完整节对象','143','288']))
for m in re.finditer(r'\]\(([^)]+)\)',report):
 p=m.group(1)
 if not p.startswith(('https://','http://','#')):ck('report deliverable link '+p,(OUT/p).exists())
paths=subprocess.check_output(['git','-C',str(ROOT),'status','--porcelain','--untracked-files=all']).decode().splitlines()
prefix='review/remediation/20261003-prepare/batches/B08/affected-B07-review-round-1/'
ck('repository writes confined to report package',all(line[3:].startswith(prefix) for line in paths))
ck('separate fullR08 and actual/parent gates retained',not doc('handoff.json')['global_approval'] and doc('handoff.json')['canonical_closures']==0 and len(doc('handoff.json')['remaining_gates'])==7)
result={'type':'own report-only Git/hash/JSON/text validation','checks':checks,'passed':sum(r['pass'] for r in checks),'failed':[r for r in checks if not r['pass']],'reference_execution':0,'behavior_vectors_executed':0,'runtime_observations':0,'proven_Demo_chains':0}
(OUT/'report-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
manifest=[]
for p in sorted(OUT.iterdir()):
 if p.is_file() and p.name!='artifact-manifest.json':
  b=p.read_bytes();manifest.append({'path':p.name,'sha256':sha(b),'bytes':len(b)})
(OUT/'artifact-manifest.json').write_text(json.dumps({'scope':'All report package artifacts except this self-referential manifest; manifest complete identity external in report commit/readback','candidate':CAND,'baseline':BASE,'artifacts':manifest},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'failed':result['failed'],'artifacts_excluding_manifest':len(manifest)}))
assert not result['failed']
