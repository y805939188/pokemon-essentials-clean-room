import ast,collections,csv,hashlib,io,json,re,subprocess
from pathlib import Path
ROOT=Path('/workspace/review-B09-actual-1');REF=Path('/workspace/reference-B09-1')
A='dc64807c2d726171827017ec636c6a73efd8e4b5';C='18873059e56314fcd48f6081d5a65a79301a52f6';P='407536adb682a04161d3e9c82f153a62b1becd97';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B='review/remediation/20261003-prepare/batches/B09/';ST=B+'integration-stage-1/'
checks=[];identities=[];cache={}
def git(*args,root=ROOT):return subprocess.check_output(['git',*args],cwd=root)
def blob(commit,path,root=ROOT):
 key=(str(root),commit,path)
 if key not in cache:cache[key]=git('show',f'{commit}:{path}',root=root)
 return cache[key]
def obj(path):return json.loads(blob(A,path))
def check(name,value,detail=None):checks.append({'check':name,'passed':bool(value),'detail':detail})
def ident(commit,path,root=ROOT):
 raw=blob(commit,path,root)
 return {'commit':commit,'path':path,'git_blob':git('rev-parse',f'{commit}:{path}',root=root).decode().strip(),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
def verify(d,label):
 path=d['path'];commit=d.get('commit') or A
 root=REF if commit==R and path.startswith(('Data/','PBS/')) else ROOT
 if not re.fullmatch('[0-9a-f]{40}',commit):commit=A
 try:
  actual=ident(commit,path,root);good=all(str(actual[k])==str(d[k]) for k in ['git_blob','sha256','bytes'] if k in d)
  check(label,good,{'actual':actual} if not good else None);identities.append({'location':label,'declared_identity':d,'actual_identity':actual,'passed':good})
 except subprocess.CalledProcessError:check(label,False,{'unavailable':commit+':'+path})
def walk(d,label):
 if isinstance(d,dict):
  if all(k in d for k in ['path','git_blob','sha256','bytes']):verify(d,label)
  for k,v in d.items():walk(v,label+'/'+k)
 elif isinstance(d,list):
  for i,v in enumerate(d):walk(v,label+'/'+str(i))
def objecthash(d):return hashlib.sha256(json.dumps(d,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
check('exact actual HEAD',git('rev-parse','HEAD').decode().strip()==A)
check('isolated actual branch',git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/review-B09-actual-1')
check('reference exact/clean/detached',git('rev-parse','HEAD',root=REF).decode().strip()==R and git('status','--porcelain',root=REF)==b'' and subprocess.run(['git','symbolic-ref','-q','HEAD'],cwd=REF,capture_output=True).returncode==1)
m=obj(ST+'integration-manifest.json');f=obj(ST+'diff-and-freeze.json');registration=obj(ST+'finding-registration.json');readers=obj(ST+'current-readers.json');dep=obj(ST+'downstream-dependency-assessment.json')
stage_paths=git('ls-tree','-r','--name-only',A,'--',ST).decode().splitlines()
check('14 actual integration-stage files',len(stage_paths)==14)
for path in stage_paths:
 if path.endswith('.json'):walk(obj(path),path)
for row in csv.DictReader(io.StringIO(blob(A,ST+'current-hashes.tsv').decode()),delimiter='\t'):verify(row,'current-hashes/'+row['path'])
norm=m['reviewed_normative_identities']
normpaths=[r['path'] for r in norm]
for d in norm:verify(d,'normative14/'+d['path']);check('candidate actual normative identity '+d['path'],blob(C,d['path'])==blob(A,d['path']))
check('normative 14/8 final/6 original',len(normpaths)==14 and len(set(normpaths))==14 and sum(p.startswith('deliverables/') for p in normpaths)==8 and sum(p.startswith('specs/') for p in normpaths)==6)
public=m['public_write_paths'];check('10 unique public paths',len(public)==10 and len(set(public))==10)
diffs={}
for before,label in [(P,'predecessor_to_actual'),(C,'candidate_to_actual'),(f['payload_commit'],'payload_to_actual')]:
 raw=git('diff','--no-ext-diff','--no-textconv','--no-renames','--binary',before,A)
 Path('/tmp/B09-actual-'+label+'.patch').write_bytes(raw)
 names=git('diff','--no-ext-diff','--no-textconv','--no-renames','--name-only',before,A).decode().splitlines()
 diffs[label]={'before':before,'after':A,'path_filter_used':False,'bytes':len(raw),'lines':len(raw.splitlines()),'sha256':hashlib.sha256(raw).hexdigest(),'paths':names,'path_count':len(names)}
check('199 complete predecessor paths',diffs['predecessor_to_actual']['path_count']==199)
check('112 complete candidate-to-actual paths',diffs['candidate_to_actual']['path_count']==112)
check('actual evidence-only child exact three files',git('rev-parse',A+'^').decode().strip()==f['payload_commit'] and set(diffs['payload_to_actual']['paths'])==set(m['final_freeze_paths']) and len(m['final_freeze_paths'])==3)
incoming=m['source_identities'];check('175 incoming source identities',len(incoming)==175 and len({d['path'] for d in incoming})==175)
for d in incoming:check('incoming actual preservation '+d['path'],blob(d['commit'],d['path'])==blob(A,d['path']))
check('199 path classification complete',set(diffs['predecessor_to_actual']['paths'])=={d['path'] for d in incoming}|set(public)|set(stage_paths))
reportdirs=[r['report_directory'] for r in m['candidate_reports']]
check('112 path classification complete',set(diffs['candidate_to_actual']['paths'])=={d['path'] for d in incoming if any(d['path'].startswith(x) for x in reportdirs)}|set(public)|set(stage_paths))
for n in ['upstream-to-payload-identities.json','candidate-to-payload-identities.json']:
 d=obj(ST+n);raw=git('diff','--no-ext-diff','--no-textconv','--no-renames','--binary',d['before_commit'],d['payload_commit'])
 check(n+' full unfiltered diff exact',len(raw)==d['diff_bytes'] and hashlib.sha256(raw).hexdigest()==d['diff_sha256'] and len(raw.splitlines())==d['diff_lines'])
 check(n+' full path set',set(git('diff','--name-only',d['before_commit'],d['payload_commit']).decode().splitlines())=={x['path'] for x in d['changed_paths']})
for merge in m['normal_native_merges']:
 check('merge parents '+merge['result'],git('show','-s','--format=%P',merge['result']).decode().split()==merge['parents'])
 check('merge tree '+merge['result'],git('rev-parse',merge['result']+'^{tree}').decode().strip()==merge['tree'])
 check('merge contains source '+merge['result'],subprocess.run(['git','merge-base','--is-ancestor',merge['source'],merge['result']],cwd=ROOT).returncode==0)
for receipt in m['candidate_reports']:
 paths=git('diff','--name-only',C,receipt['commit']).decode().splitlines()
 check('candidate receipt exact scope '+receipt['role'],git('rev-parse',receipt['commit']+'^').decode().strip()==C and len(paths)==receipt['path_count'] and all(p.startswith(receipt['report_directory']) for p in paths))
 check('candidate receipt never actual '+receipt['role'],receipt['verdict']=='PASS_SCOPED' and receipt['actual_gate_satisfied'] is False)
fixedfinds={r['id']:r for r in json.loads(blob(registration['fixed_original_findings_file']['commit'],registration['fixed_original_findings_file']['path']))}
fixedaccept=json.loads(blob(registration['fixed_approved_acceptance_file']['commit'],registration['fixed_approved_acceptance_file']['path']))
contract=obj('review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/B09-downstream-contract.json')
controls=registration['dispositions']
check('all 20/13 current registered controls',len(controls)==20 and sum(x['B09_primary'] for x in controls)==13 and {x['id'] for x in controls}==set(contract['contribution_finding_ids']))
for d in controls:
 fid=d['id'];o=fixedfinds[fid];a=fixedaccept[fid]
 check('complete fixed original object hash '+fid,objecthash(o)==d['original_complete_object_sha256'])
 check('complete fixed approved acceptance object hash '+fid,objecthash(a)==d['acceptance_complete_object_sha256'])
 for k,v in d['complete_current_control_fields'].items():check('qualified current control '+fid+'/'+k,k in o and v==o[k])
 for k,v in d['complete_minimum_acceptance_fields'].items():check('minimum full acceptance '+fid+'/'+k,k in a and v==a[k])
 requiredcurrent=[k for k in ['current_qualifications','effective_case_constraints','adjudication_precedence','root_adjudications','extensions','extension_decisions'] if k in o]
 requiredminimum=[k for k in ['minimum_revision','determinate_recheck','premises','minimum_counterexample','acceptance_gate'] if k in a]
 check('no effective control omissions '+fid,all(k in d['complete_current_control_fields'] for k in requiredcurrent) and all(k in d['complete_minimum_acceptance_fields'] for k in requiredminimum))
 check('no contribution/ID prematurely accepted '+fid,d['canonical_state']=='OPEN' and d['canonical_edited'] is False and d['accepted_B09_contributions']==0 and d['canonical_closure'] is False and d['parent_C_acceptance']=='NOT_PERFORMED')
check('70 actual current bindings',len(readers['readers'])==70 and len({x['path'] for x in readers['readers']})==70)
for r in readers['readers']:
 check('actual changed reader disposition '+r['path'],(r['reviewed_candidate']['git_blob']!=r['actual_current']['git_blob'])==r['candidate_to_actual_changed'])
check('B14 72 current inputs',len(dep['B14']['all72_current_assessment_inputs'])==72)
check('B14 serialization/gates/no dispatch',dep['B14']['status']=='FORMAL_BLOCKED_UNTIL_FIVE_ACTUAL_PASSES_PARENT_B09_C_AND_SUCCESSOR_REFREEZE' and dep['tasks_dispatched']==0 and dep['B09_B14_serialization']==contract['B09_B14_operational_serialization'])
ledgers={}
for n in ['approval-ledger.tsv','traceability-successor.tsv']:
 p='review/remediation/20261003-prepare/'+n;old=blob(P,p);new=blob(A,p)
 rows=list(csv.DictReader(io.StringIO(new.decode()),delimiter='\t'));oldrows=list(csv.DictReader(io.StringIO(old.decode()),delimiter='\t'))
 check('old 150 ledger bytes prefix retained '+n,new.startswith(old) and rows[:150]==oldrows and len(oldrows)==150)
 check('exact 20 appended rows '+n,len(rows)==170 and {r['finding_id'] for r in rows[150:]}=={r['id'] for r in controls})
 for row in rows[150:]:
  fid=row['finding_id'];control=next(d for d in controls if d['id']==fid)
  check('ledger binding/OPEN '+n+'/'+fid,row['canonical_state']=='OPEN' and row['candidate_commit']==C and row['candidate_review_commit']==m['candidate_reports'][0]['commit'])
  remaining=json.loads(row['remaining_obligations'])
  check('complete remaining obligations '+n+'/'+fid,remaining['batch']=='B09' and remaining['all_contributors']==control['all_contributor_batches'] and remaining['other_batch_obligations']==control['other_contributors_pending'])
  if n=='approval-ledger.tsv':check('approval pending actual/downstream '+fid,row['integration_verdict']=='NOT_REVIEWED_PENDING_FIVE_ULTRA_STANDARD' and row['downstream_gate']=='BLOCKED')
 ledgers[n]={'before_rows':len(oldrows),'after_rows':len(rows),'old_bytes':len(old),'new_bytes':len(new),'actual_identity':ident(A,p),'added_rows':rows[150:]}
canonical=list(csv.DictReader(io.StringIO(blob(A,'review/remediation/20261003-prepare/finding-ledger.tsv').decode()),delimiter='\t'))
check('canonical ledger unchanged all229 OPEN',len(canonical)==229 and {r['canonical_state'] for r in canonical}=={'OPEN'} and blob(P,'review/remediation/20261003-prepare/finding-ledger.tsv')==blob(A,'review/remediation/20261003-prepare/finding-ledger.tsv'))
check('accepted statistics immutable',blob(P,'review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/completion-statistics-successor.json')==blob(A,'review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/completion-statistics-successor.json'))
counts=obj(ST+'scope-counts.json')
for path,cat in counts['catalog_counts'].items():
 pattern=r'^\|\s*([A-Z]+-?\d+(?:[a-z])?)\s*\|'
 oldids=re.findall(pattern,blob(P,path).decode(),re.M);newids=re.findall(pattern,blob(A,path).decode(),re.M)
 check('actual catalog row count '+path,len(oldids)==cat['before'] and len(newids)==cat['after'])
 check('old ID sequence/multiplicity '+path,[x for x in newids if x in set(oldids)]==oldids)
 check('new IDs exact '+path,[x for x in newids if x not in set(oldids)]==cat['added_ids'])
 oldrows={m.group(1):m.group(0) for m in re.finditer(pattern+r'.*$',blob(P,path).decode(),re.M)}
 newrows={m.group(1):m.group(0) for m in re.finditer(pattern+r'.*$',blob(A,path).decode(),re.M)}
 check('changed ten old rows exact '+path,{k for k in oldrows if oldrows[k]!=newrows[k]}==set(cat['changed_old_ids']))
for d in counts['protected_whole_sections']:
 p=d['path'];heading=d['heading'];text=blob(A,p).decode();start=text.index(heading);end=text.find('\n## ',start+len(heading));section=text[start:end+1] if end>=0 else text[start:]
 # Section delimiters in the checked-in hash omit the preceding newline and
 # terminate immediately before the next heading.
 raw=section.encode()
 check('protected whole section '+heading,heading in blob(P,p).decode() and (raw==blob(P,p).decode()[blob(P,p).decode().index(heading):].split('\n## ',1)[0].encode()+ (b'\n' if end>=0 else b'')))
 check('protected declared section hash '+heading,hashlib.sha256(raw).hexdigest()==d['sha256'] and len(raw)==d['bytes'])
for d in counts['new_static_designs_not_executed']:
 row=blob(A,d['path']).splitlines(keepends=True)[d['line']-1]
 check('new static row exact '+d['id'],hashlib.sha256(row).hexdigest()==d['sha256'] and len(row)==d['bytes'] and d['status']=='STATIC_DESIGN_NOT_EXECUTED')
parsedjson=0;parsedpython=0
for path in diffs['predecessor_to_actual']['paths']:
 if path.endswith('.json'):json.loads(blob(A,path));parsedjson+=1
 elif path.endswith('.py'):ast.parse(blob(A,path).decode(),filename=path);parsedpython+=1
result={'method':'Fresh independent actual Git/hash/text/control bookkeeping only; no historical/author verifier or behavioral vector execution.','actual':A,'candidate':C,'accepted_predecessor':P,'checks':checks,'check_count':len(checks),'failures':[r for r in checks if not r['passed']],'diffs':diffs,'identity_records':identities,'input_identity_count':len(identities),'public_registration_ledgers':ledgers,'changed_json_parsed':parsedjson,'python_AST_only':parsedpython,'execution':{'reference':0,'author_historical_verifier':0,'behavior_vectors':0,'observations':0,'demo':0}}
Path('/tmp/B09-actual-audit-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'check_count':len(checks),'failure_count':len(result['failures']),'failures':result['failures'][:15],'identity_records':len(identities),'diffs':{k:{q:v[q] for q in ['path_count','bytes','lines','sha256']} for k,v in diffs.items()},'changed_json_parsed':parsedjson,'python_AST_only':parsedpython},ensure_ascii=False,indent=2))
