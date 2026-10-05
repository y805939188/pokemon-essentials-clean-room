import hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path('/workspace/review-B09-actual-1');A='dc64807c2d726171827017ec636c6a73efd8e4b5';C='18873059e56314fcd48f6081d5a65a79301a52f6';P='407536adb682a04161d3e9c82f153a62b1becd97';C1='8ff72341b5b91736970b5bfa5dc1b88137e618a5';B='review/remediation/20261003-prepare/batches/B09/'
checks=[];rows=[]
def g(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def raw(c,p):return g('show',c+':'+p)
def obj(p):return json.loads(raw(A,B+p))
def ck(n,v,d=None):checks.append({'check':n,'passed':bool(v),'detail':d})
def hashmatches(c,p,d):
 b=raw(c,p)
 return g('rev-parse',c+':'+p).decode().strip()==d['git_blob'] and hashlib.sha256(b).hexdigest()==d['sha256'] and len(b)==d['bytes']
proposal=obj('scope-proposal-1/original-sync-proposal.json');clausecount=0
for f in proposal['files']:
 p=f['path'];ck('approved original before '+p,hashmatches(P,p,f['before']));ck('approved original intended after actual '+p,hashmatches(A,p,f['intended_after']))
 old=raw(P,p).decode();new=raw(A,p).decode();reconstructed=old
 for x in f['clauses']:
  before=x['before_text'];after=x['intended_after_text'];ck('original exact before present '+p+'/'+x['clause'],before in old);ck('original exact after present '+p+'/'+x['clause'],after in new)
  reconstructed=reconstructed.replace(before,after);clausecount+=1
 ck('approved literal original reconstruction '+p,reconstructed==new)
 patch=raw(A,f['complete_diff_path']);ck('approved full original patch hash '+p,hashlib.sha256(patch).hexdigest()==f['complete_diff_sha256'])
ck('five original thirty approved clauses',len(proposal['files'])==5 and clausecount==30)
approval=obj('scope-amendment-2/approval.json');application=obj('scope-amendment-2/application.json');extra=0
ck('WP20 scope only and required B05',approval['scope_authorization_only'] and not approval['independent_correctness_approval'] and approval['new_affected_B05_candidate_actual_review_required'] and approval['clause_count']==4)
for f in approval['files']:
 p=f['path'];ck('WP20 candidate1 exact before '+p,hashmatches(C1,p,f['before']));ck('WP20 actual intended after '+p,hashmatches(A,p,f['intended_after']))
 old=raw(C1,p).decode();reconstructed=old
 for x in f['clause_changes']:
  ck('WP20 approved exact original before '+p+'/'+str(x['before_lines']),x['before_text'] in old)
  reconstructed=reconstructed.replace(x['before_text'],x['intended_after_text']);extra+=1
 ck('WP20 only four approved clauses reconstruct actual '+p,reconstructed.encode()==raw(A,p))
 patch=raw(C1,B+'candidate-1/'+f['full_diff']['path']);ck('WP20 approved patch SHA '+p,hashlib.sha256(patch).hexdigest()==approval['approved_patch_sha256'][p] and len(patch)==f['full_diff']['bytes'])
 ck('WP20 application after exact '+p,hashmatches(A,p,next(x['after'] for x in application['files'] if x['path']==p)))
log=obj('candidate-2/formal-change-log.json');ck('73 final descriptive revisions',len(log['changes'])==73)
for x in log['changes']:ck('actual final after literal '+x['path']+'/'+x['clause'],x['after_text'] in raw(A,x['path']).decode())
st=obj('candidate-2/static-cases.json');ck('static only all61designs',len(st['catalog_cases'])==43 and len(st['supplemental_designs'])==18 and st['executed']==0 and st['runtime_observations']==0 and st['proven_Demo_chains']==0 and not st['reference_simulator_used'] and all(not x['executed'] for x in st['catalog_cases']+st['supplemental_designs']))
for x in st['catalog_cases']:
 text=raw(A,x['path']).decode().splitlines();row=text[x['line']-1]
 ck('catalog link ID/row actual '+x['id'],re.match(r'^\|\s*'+re.escape(x['id'])+r'\s*\|',row) is not None and x['input_and_premises'] in row and x['static_expected'] in row)
 rows.append({'id':x['id'],'path':x['path'],'line':x['line'],'row_sha256_without_newline':hashlib.sha256(row.encode()).hexdigest(),'design':x,'actual_row':row})
m=obj('integration-stage-1/integration-manifest.json');paths=[x['path'] for x in m['reviewed_normative_identities']]
ck('full14 normative predecessor patch unchanged from candidate',g('diff','--no-ext-diff','--no-textconv','--no-renames','--binary',P,A,'--',*paths)==g('diff','--no-ext-diff','--no-textconv','--no-renames','--binary',P,C,'--',*paths))
readers=obj('integration-stage-1/current-readers.json');ck('no additional normative reader change',set(x['path'] for x in readers['readers'] if x['candidate_to_actual_changed'])=={'deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md'})
result={'actual':A,'candidate':C,'accepted_predecessor':P,'method':'New independent static text/hash/approval bookkeeping only','checks':checks,'check_count':len(checks),'failures':[x for x in checks if not x['passed']],'catalog43_links':rows,'original_clause_count':clausecount+2,'final_clause_count':73,'execution':{'reference':0,'author_historical_verifiers':0,'vectors':0,'observations':0,'demo':0}}
Path('/tmp/B09-actual-supplement-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'check_count':len(checks),'failures':result['failures']},ensure_ascii=False,indent=2))
