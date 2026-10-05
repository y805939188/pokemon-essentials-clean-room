"""Own report artifact checks only, not reference behavior tests."""
import hashlib,json,pathlib,re,subprocess
OUT=pathlib.Path(__file__).resolve().parent
REPO=OUT.parents[5]
ACTUAL='adca83d63d18c94429cdb52aef9eaf7b8aa00189'
REF=pathlib.Path('/workspace/reference-pokemon-essentials-B07')
results=[]
def git(*args,root=REPO):return subprocess.check_output(['git','-C',str(root),*args]).decode().strip()
def check(name,ok,evidence):results.append({'check':name,'status':'PASS' if ok else 'FAIL','evidence':evidence})
records=json.loads((OUT/'finding-dispositions.json').read_text())['records']
expected='A020 A024 A026 A039 A040 A041 A043 A044 A045 A046 A047 A048 A049 A050 A051 B008 B013 C003 D023'.split()
check('19 actual dispositions,12 primary and no canonical closure',len(records)==19 and sum(x['B07_primary'] for x in records)==12
 and {x['id'] for x in records}=={'GIR-FD82-'+x for x in expected}
 and all(x['reviewed_actual']==ACTUAL and x['verdict']=='PASS_SCOPED' and x['canonical_status']=='OPEN' and not x['canonical_closure'] for x in records),19)
checks=json.loads((OUT/'document-checks.json').read_text())
check('independent object checks pass and bind same actual',checks['actual']==ACTUAL and checks['all_pass'] and len(checks['results'])==36,36)
comparison=json.loads((OUT/'author-comparison.json').read_text())
lock_sha=hashlib.sha256((OUT/'independent-first-judgment.md').read_bytes()).hexdigest()
check('independent judgment lock unchanged',lock_sha==comparison['independent_first_lock_sha256'],lock_sha)
missing=[]
for path in OUT.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
  if not target.startswith(('http://','https://')) and not (path.parent/target).is_file():missing.append([path.name,target])
check('all relative report links resolve',not missing,missing)
logs=json.loads((OUT/'source-reading-log.json').read_text());bad=[]
for e in logs['new_actual_review_opened_ranges']:
 raw=(REF/e['path']).read_bytes()
 if hashlib.sha256(raw).hexdigest()!=e['sha256'] or len(raw)!=e['bytes']:bad.append(e['path'])
check('fresh reference reading event identities exact',not bad,{'files':len({x['path'] for x in logs['new_actual_review_opened_ranges']}),'failed':bad})
check('reference remains exact and clean',git('rev-parse','HEAD',root=REF)==logs['reference_commit'] and not git('status','--porcelain',root=REF),logs['reference_commit'])
receipt=json.loads((OUT/'configuration-and-scope-receipt.json').read_text())
check('zero reference/vector/observation/demo and actual configUNVERIFIED',receipt['actual_effective_configuration']=='UNVERIFIED'
 and not receipt['new_configuration_confirmation_gate'] and not receipt['global_approval']
 and all(receipt[k]==0 for k in ['reference_execution','behavior_vectors_executed','runtime_observations','proven_Demo_chains','canonical_closures']),
 {'requested_model':'gpt-6.1-sol','reasoning':'ultra','speed':'Standard'})
down=json.loads((OUT/'downstream-check.json').read_text())
check('B08 gate unchanged, WP34 read-only and no launch',not down['B08_accepted'] and down['tasks_dispatched']==down['parallel_writes_authorized']==0
 and down['WP34_body'].startswith('READ_ONLY') and not down['originals_write_authorized'],down['B08_status'])
for path in OUT.glob('*.json'):json.loads(path.read_text())
check('all new review JSON parses',True,len(list(OUT.glob('*.json'))))
prefix=str(OUT.relative_to(REPO))+'/'
status=git('status','--porcelain','--untracked-files=all').splitlines()
outside=[x for x in status if not x[3:].startswith(prefix)]
check('only new requested directory changes; HEAD exact actual before report commit',not outside and git('rev-parse','HEAD')==ACTUAL,
 {'outside':outside,'current_head':git('rev-parse','HEAD'),'new_paths':len(status)})
result={'kind':'OWN_REPORT_DOCUMENT_CHECKS_ONLY','actual':ACTUAL,'results':results,'all_pass':all(x['status']=='PASS' for x in results),'reference_execution':0,'behavior_vectors_executed':0}
(OUT/'report-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'all_pass':result['all_pass'],'checks':len(results),'failed':[x['check'] for x in results if x['status']!='PASS']}))
raise SystemExit(0 if result['all_pass'] else 1)
