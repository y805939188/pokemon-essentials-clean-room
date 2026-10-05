"""Fresh R-B04 report metadata/citation verifier; no source behavior or historical verifier execution."""
import collections
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess

R=Path('/workspace/pokemon-essentials-clean-room')
REF=Path('/tmp/b09-b04-actual-reference')
D=R/'review/remediation/20261003-prepare/batches/B09/affected-B04-integration-review-1'
A='dc64807c2d726171827017ec636c6a73efd8e4b5'
B='407536adb682a04161d3e9c82f153a62b1becd97'
C='18873059e56314fcd48f6081d5a65a79301a52f6'
S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
FLAGS=['--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3']
checks=[];cache={}
def git(*args,cwd=R):return subprocess.check_output(['git',*args],cwd=cwd)
def sha(b):return hashlib.sha256(b).hexdigest()
def obj(n):return json.loads((D/n).read_text())
def content(c,p):
 k=(c,p)
 if k not in cache:cache[k]=git('show',c+':'+p,cwd=REF if c==S else R)
 return cache[k]
def check(v,k):checks.append(dict(check=k,passed=bool(v)))
def walk(v):
 if isinstance(v,dict):
  if all(k in v for k in ['commit','path','git_blob','sha256','bytes'])and v['commit']:
   c,p=v['commit'],v['path'];b=content(c,p)
   check(v['sha256']==sha(b)and v['bytes']==len(b)and v['git_blob']==git('rev-parse',c+':'+p,cwd=REF if c==S else R).decode().strip(),'fixed full file identity '+c+':'+p)
  for x in v.values():walk(x)
 elif isinstance(v,list):
  for x in v:walk(x)

assert D.is_dir()
for p in sorted(D.glob('*.json')):
 if p.name not in ['report-validation-results.json','report-file-manifest.json']:
  v=json.loads(p.read_text());check(True,'valid JSON '+p.name);walk(v)
for p in D.glob('*.jsonl'):
 for i,line in enumerate(p.read_text().splitlines()):
  e=json.loads(line);check(e['sha256']==sha(content(e['commit'],e['path']))and e['bytes']==len(content(e['commit'],e['path'])),'fresh successful reading event '+p.name+':'+str(i+1))
coverage=collections.defaultdict(set)
for n in ['reference-reading-events.jsonl','project-reading-events.jsonl']:
 for line in (D/n).read_text().splitlines():
  e=json.loads(line);coverage[(e['commit'],e['path'])].update(range(e['start'],e['end']+1))
def citations(v):
 if isinstance(v,dict):
  if all(k in v for k in ['repository','commit','path','start','end']):
   c,p=v['commit'],v['path'];lo,hi=v['start'],v['end'];b=content(c,p)
   check(c in [A,S]and 1<=lo<=hi<=len(b.decode().splitlines()),'actual/fixed citation valid '+p+':'+str(lo)+'-'+str(hi))
   check(set(range(lo,hi+1))<=coverage[(c,p)],'fresh successful range covers citation '+p+':'+str(lo)+'-'+str(hi))
  for x in v.values():citations(x)
 elif isinstance(v,list):
  for x in v:citations(x)
designs=obj('fresh-independent-static-designs.json')
check(len(designs['cases'])==15 and designs['count']==15 and designs['executed']==0,'15 manual static groups, execution0')
for c in designs['cases']:
 check(c['fresh_actual']==A and not c['executed']and not c['runtime_observed']and bool(c['fresh_actual_assessment'])and bool(c['neighboring_reverse']),'fresh manual group/premise/reverse '+c['id'])
citations(designs);citations(obj('B09-G-O01-independent-assessment.json'))
scope=obj('scope-and-impact.json')
check(sum(len(x['full_before_after_clauses'])for x in scope['required_changed_readers'])==28 and len(scope['unchanged_owner_clauses'])==5,'28 complete changed clauses/five owner ranges')
for x in scope['required_changed_readers']:
 for v in x['full_before_after_clauses']:
  check(v['before_text']in content(B,x['path']).decode()and v['after_text']in content(A,x['path']).decode(),'full clause beforeB/afterA '+x['path']+' '+v['clause'])
for x in scope['unchanged_owner_clauses']:
 lo,hi=x['lines'];cited=''.join(content(A,x['path']).decode().splitlines(keepends=True)[lo-1:hi])
 check(cited==x['before_text']==x['after_text']and content(B,x['path'])==content(C,x['path'])==content(A,x['path']),'whole owner preserved and current range '+x['path']+str(x['lines']))
 check(set(range(lo,hi+1))<=coverage[(A,x['path'])],'fresh read covers owner clause '+x['path']+str(x['lines']))
for x in obj('diff-manifest.json')['diffs']:
 data=(D/x['file']).read_bytes();raw=gzip.decompress(data)if x['file'].endswith('.gz')else data
 check(sha(raw)==x['raw_sha256']and len(raw)==x['raw_bytes'],'raw complete/scoped diff hash '+x['file'])
 if not x['path_filter']:
  check(raw==git('diff',*FLAGS,x['before'],A),'independently regenerate unfiltered diff '+x['file'])
  check(sha(data)==x['gzip_sha256']and len(data)==x['gzip_bytes'],'report compression identity '+x['file'])
for n,c,count in [('baseline-to-actual-identities.json',B,199),('candidate-to-actual-identities.json',C,112)]:
 v=obj(n);entries=v if isinstance(v,list)else v['changed_paths']
 check(len(entries)==count,'full path count '+n)
 rows=git('diff','--name-status','--no-renames',c,A).decode().splitlines()
 actual=[tuple(x.split('\t'))for x in rows]
 declared=[(x['status']if'status'in x else x['change'],x['path'])for x in entries]
 check(declared==actual,'complete path ordering and statuses '+n)
audit=obj('actual-identity-audit.json');check(audit['actual']==A and audit['failed']==0 and audit['passed']==audit['checks']==2701,'fresh independent identity2701/2701')
first=obj('first-judgment.json');cmp=obj('AREG-check-comparison.json')
check(first['at_utc']<cmp['compared_at_utc']and cmp['comparison_after_first_judgment']and not cmp['independent_conclusion_changed'],'independent first judgment then detailed AREG comparison')
limits=obj('model-and-limits.json');check(limits['effective_configuration']=='UNVERIFIED'and limits['children_spawned']==0,'effective configuration UNVERIFIED, no child tasks')
for k in ['reference_program_execution','game_execution','compiler_execution','converter_execution','generator_execution','deserializer_execution','reference_behavior_simulator_execution','author_or_historical_verifier_execution','behavior_vectors_execution','runtime_observations','proven_Demo_chains','auth_config_quota_probes']:
 check(limits[k]==0,'retained zero '+k)
ref=obj('reference-identity.json');check(ref['commit']==ref['HEAD']==ref['fetch_HEAD']==S and ref['tree']=='7589c800b61ba13a13040ed0d686979b80a84fd0'and ref['detached']and ref['clean']and ref['real_object_type']=='commit','own reference real exact/detached/clean')
check(git('rev-parse','HEAD',cwd=REF).decode().strip()==S and not git('status','--porcelain',cwd=REF).strip(),'reference remains read-only clean')
controls=obj('complete-control-bindings.json');check(len(controls)==23 and all(x['all_complete_fields_match']and x['complete_extensions_preserved']for x in controls[:20]),'complete20 controls plus C071–73')
check(obj('handoff.json')['actual']==A and obj('handoff.json')['verdict']=='PASS_SCOPED'and not obj('handoff.json')['parent_C_acceptance'],'scoped handoff no parent acceptance')
check(obj('findings.json')['new_blocking_findings']==[]and obj('findings.json')['new_canonical_findings']==[],'no invented new blocking/root findings')
readme=(D/'README.md').read_text()
for label,path in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',readme):check((D/path).is_file(),'README deliverable link '+path)
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines();changed=git('diff','--name-only',A).decode().splitlines();staged=git('diff','--cached','--name-only',A).decode().splitlines()
prefix=str(D.relative_to(R))+'/'
check(all(p.startswith(prefix)for p in untracked+changed+staged),'only authorized new report directory')
check(not git('ls-tree','-r','--name-only',A,'--',prefix).strip(),'new report directory absent from fixed actual')
check(git('rev-parse','HEAD').decode().strip()==A,'report checkout still exact actual before commit')
files=[]
for p in sorted(D.iterdir()):
 if p.is_file()and p.name not in ['report-file-manifest.json','report-validation-results.json']:
  b=p.read_bytes();files.append(dict(path=p.name,sha256=sha(b),bytes=len(b)))
(D/'report-file-manifest.json').write_text(json.dumps(dict(actual=A,files=files,count=len(files),self_and_validation_results_excluded=True,report_commit_binding='External exact ordinary commit/push/ref-readback SHA'),ensure_ascii=False,indent=2)+'\n')
out=dict(at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),actual=A,verifier=__doc__,checks=len(checks),passed=sum(x['passed']for x in checks),failed=sum(not x['passed']for x in checks),results=checks,reference_behavior_execution=0,historical_verifier_execution=0,behavior_vectors_executed=0)
(D/'report-validation-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checks=out['checks'],passed=out['passed'],failed=[x for x in checks if not x['passed']],manifest_files=len(files)),ensure_ascii=False))
if out['failed']:raise SystemExit(1)
