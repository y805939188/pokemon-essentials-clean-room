import subprocess,json,hashlib,pathlib,datetime,re,collections
R=pathlib.Path('/workspace/pokemon-essentials-clean-room')
T=pathlib.Path('/tmp/b09-b04')
B='407536adb682a04161d3e9c82f153a62b1becd97'
C='18873059e56314fcd48f6081d5a65a79301a52f6'
C1='8ff72341b5b91736970b5bfa5dc1b88137e618a5'
PAY='ab81adc17a0ee50f21032c58036b7b56b28da51b'
G='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
P='41fffb540c6483f5296ea0d33b789b75180d27ed'
PREFIX='review/remediation/20261003-prepare/batches/B09/'
cache={};checks=[];identities=[]
def git(*args):return subprocess.check_output(['git',*args],cwd=R)
def content(c,p):
 k=(c,p)
 if k not in cache:cache[k]=git('show',c+':'+p)
 return cache[k]
def sha(b):return hashlib.sha256(b).hexdigest()
def check(condition,kind,label):
 checks.append(dict(kind=kind,label=label,passed=bool(condition)))
def obj(c,p):return json.loads(content(c,p))
def identity(c,p):
 b=content(c,p);return dict(commit=c,path=p,git_blob=git('rev-parse',c+':'+p).decode().strip(),sha256=sha(b),bytes=len(b))
def verify(v,default,label,path=None):
 c=v.get('commit') or default;p=v.get('path') or path
 if not p or not all(k in v for k in ['git_blob','sha256','bytes']):return
 a=identity(c,p);ok=all(v[k]==a[k] for k in ['git_blob','sha256','bytes'])
 check(ok,'identity',label+' '+c+':'+p);identities.append(dict(label=label,declared=v,actual=a,matched=ok))
def recurse(v,default,label):
 if isinstance(v,dict):
  verify(v,default,label)
  for k,x in v.items():recurse(x,C1 if k=='candidate_1_refreeze' else B if k=='baseline' else default,label+'/'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):recurse(x,default,label+'/'+str(i))
def paths(a,b):return [line.split('\t') for line in git('diff','--name-status','--no-renames',a,b).decode().splitlines()]
def diff(a,b,ps=()):return git('diff','--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3',a,b,*(['--',*ps] if ps else []))
def write(n,v):(T/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
allpaths=paths(B,C);mods=[p for s,p in allpaths if s=='M'];adds=[p for s,p in allpaths if s=='A']
check(len(allpaths)==87 and len(mods)==14 and len(adds)==73,'partition','B-to-C exact 87=14M+73A')
check(all(p.startswith(PREFIX) for p in adds),'partition','all evidence additions under B09')
check(all(s in ['M','A'] for s,p in allpaths),'partition','no deletions/renames/type changes')
check(git('rev-list','--parents','-n','1',C).decode().split()==[C,PAY],'graph','final envelope parent exact payload')
check(git('rev-list','--parents','-n','1',PAY).decode().split()==[PAY,C1],'graph','payload parent exact C1')
check(subprocess.run(['git','merge-base','--is-ancestor',B,C],cwd=R).returncode==0,'graph','accepted B ancestor of exact C')
check(diff(B,C)==(T/'complete-baseline-to-candidate.diff').read_bytes(),'diff','own unfiltered exact final diff reproducible')
check(diff(B,C,mods)==(T/'all14-normative.diff').read_bytes(),'diff','all14 modified normative diff reproducible')
ni=obj(C,PREFIX+'candidate-2/normative-identities.json');sc=obj(C,PREFIX+'candidate-2/amended-scope.json')
check(set(mods)==set(sc['complete_normative_write_paths']) and len(set(mods))==14,'scope','exact amended fourteen path set')
check(sum(p.startswith('specs/') for p in mods)==6,'scope','six approved original bodies')
check(sum(p.startswith('deliverables/') for p in mods)==8,'scope','eight final/catalog paths')
recurse(ni,C,'normative-identities')
check(set(x['after']['path']for x in ni['files'])==set(mods),'scope','all14 manifest files exhaust modifications')
am=obj(C,PREFIX+'scope-amendment-2/approval.json');app=obj(C,PREFIX+'scope-amendment-2/application.json')
check(am['scope_authorization_only'] and not am['independent_correctness_approval'],'scope','WP20 authority is only scope')
check(am['approved_candidate']==C1,'scope','amendment fixed C1 proposal')
check(sha(content(C,am['approved_proposal_path']))==am['approved_proposal_sha256'],'scope','approved unchanged proposal hash')
wp20=[f['path']for f in am['files']]
oa=obj(C,PREFIX+'candidate-1/original-scope-approval.json')
op=obj(C,PREFIX+'scope-proposal-1/original-sync-proposal.json')
check(oa['scope_authorized'] and not oa['correctness_approval'],'scope','first five original authority only scope')
check(sha(content(C,PREFIX+'scope-proposal-1/original-sync-proposal.json'))==oa['manifest_sha256'],'scope','parent-approved original manifest exact hash')
check(len(op['files'])==5 and sum(len(f['clauses'])for f in op['files'])==30,'scope','five original paths/thirty scope clauses')
for f in op['files']:
 p=f['path'];verify(f['before'],B,'first5 approved before',p);verify(f['intended_after'],C,'first5 approved intended after',p)
 b=content(C,f['complete_diff_path'])
 check(sha(b)==f['complete_diff_sha256']==oa['exact_original_patch_sha256'][p],'scope','first5 approved exact whole patch '+p)
 for cl in f['clauses']:
  check(cl['before_text'] in content(B,p).decode() and cl['intended_after_text'] in content(C,p).decode(),'scope','first5 exact before/after clause '+p+' '+cl['clause'])
check(set(wp20)==set(sc['new_paths_only']) and len(wp20)==2,'scope','exact two WP20 paths')
for f in am['files']:
 p=f['path'];verify(f['before'],B,'WP20 before');verify(f['intended_after'],C,'WP20 intended after',p)
 text=content(B,p).decode();out=text
 for cl in f['clause_changes']:
  check(out.count(cl['before_text'])==1,'scope','unique approved clause '+p+' '+str(cl['before_lines']))
  out=out.replace(cl['before_text'],cl['intended_after_text'],1)
 check(out.encode()==content(C,p),'scope','exact four authorized replacements reconstruct '+p)
 patch=content(C,PREFIX+'candidate-1/'+f['full_diff']['path'])
 check(sha(patch)==f['full_diff']['sha256'] and len(patch)==f['full_diff']['bytes'],'scope','approved unapplied patch unchanged '+p)
check(all(content(C1,p)==content(C,p) for p in mods if p not in wp20),'scope','other twelve normative outputs identical to C1')
historypaths=git('ls-tree','-r','--name-only',C1,PREFIX+'candidate-1',PREFIX+'scope-proposal-1',PREFIX+'freeze-envelope').decode().splitlines()
check(all(content(C1,p)==content(C,p)for p in historypaths),'history','all C1/proposal/envelope history byte preserved')
env=obj(C,PREFIX+'freeze-envelope-2/payload-manifest.json')
envdelta=paths(PAY,C)
check(sorted(envdelta)==sorted([['A',p]for p in env['envelope_expected_new_paths']]),'envelope','exact four final envelope additions')
check(env['payload_tree']==git('rev-parse',PAY+'^{tree}').decode().strip(),'envelope','real payload tree')
check(set(env['full_final_changed_paths'])==set(p for s,p in allpaths),'envelope','final all87 manifest matches Git')
for key,a in [('full_unfiltered_predecessor_to_payload_diff',B),('full_unfiltered_candidate_1_to_payload_diff',C1)]:
 meta=env[key];b=content(C,PREFIX+'freeze-envelope-2/'+meta['path'])
 check(sha(b)==meta['sha256'] and len(b)==meta['bytes'],'diff',key+' stored integrity')
 plain=git('diff','--no-ext-diff','--no-textconv','--no-color','--no-renames','--unified=3',a,PAY)
 check(b==plain,'diff',key+' independently regenerated with stored abbreviated index format')
contractpath='review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/B09-downstream-contract.json'
ct=obj(B,contractpath);check(content(B,contractpath)==content(C,contractpath),'history','B08 downstream contract byte preserved')
recurse(ct,B,'accepted-contract')
rc=obj(C,PREFIX+'candidate-2/read-coverage.json');check(len(rc['readers'])==70,'readers','70 exact reader entries')
check([x['path']for x in rc['readers'][:62]]==[x['path']for x in ct['planned_reads']],'readers','original62 planned order retained')
for x in rc['readers']:recurse(x,C,'reader/'+x['path'])
verify(rc['contract'],B,'readcoverage-contract')
root={x['id']:x for x in obj(G,'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
accept=obj(P,'review/remediation-20261003-prepare/finding-acceptance.json')
cd=obj(C,PREFIX+'candidate-2/contribution-dispositions.json')
check([x['id']for x in cd['dispositions']]==ct['contribution_finding_ids'],'controls','all20 contribution order retained')
check(sum(x['primary']for x in cd['dispositions'])==13,'controls','13 primary records')
controls=[]
for c,d in zip(ct['contribution_controls'],cd['dispositions']):
 i=c['id'];o=root[i];a=accept[i];s=d['source_control']
 check(c['complete_original_object']==o,'controls',i+' full original source object')
 check(c['complete_approved_acceptance']==a,'controls',i+' full approved acceptance object')
 for k in ['current_qualifications','effective_case_constraints','root_adjudications','minimum_revision','determinate_recheck']:
  check(s[k]==o.get(k),'controls',i+' '+k+' retained')
 expected_extensions=[dict(report=e['report'],raw_id=e['raw_id'],root_review=e['root_review'])for e in o.get('extensions',[])]
 actual_extensions=[{k:e[k]for k in ['report','raw_id','root_review']}for e in s['extensions']]
 check(actual_extensions==expected_extensions,'controls',i+' every projected extension root_review retained; full extension text bound via complete original')
 check(s['acceptance_gate']==a['acceptance_gate'],'controls',i+' acceptance_gate retained')
 check(d['canonical_state']=='OPEN' and not d['canonical_closed'] and d['no_other_contributor_approval'],'controls',i+' no root/other-owner closure')
 controls.append(dict(id=i,primary=d['primary'],primary_owner=d['primary_owner'],source_control=s,semantic_reapproval='ONLY_B04_AFFECTED_INTERFACE_WHERE_RELEVANT; other B09 correctness not covered'))
q=obj(C,PREFIX+'candidate-2/affected-B04-review-request.json');recurse(q,C,'affected-request')
for d in q['changed_readers']:
 p=d['path'];old=content(B,p).decode();new=content(C,p).decode()
 for cl in d['full_before_after_clauses']:
  check(cl['before_text'] in old and cl['after_text'] in new,'clauses','actual full before/after '+p+' '+cl['clause'])
for x in q['untouched_owner_clauses']:
 p=x['path'];a,z=x['lines'];text=''.join(content(C,p).decode().splitlines(keepends=True)[a-1:z])
 check(text==x['before_text']==x['after_text'],'clauses','untouched owner exact excerpt '+p+' '+str([a,z]))
 check(content(B,p)==content(C,p),'history','untouched owner whole file '+p)
ap='review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/acceptance-manifest.json';ba=obj(B,ap)
check(content(B,ap)==content(C,ap),'history','B04 acceptance receipt preserved')
b04=[]
for x in ba['accepted_formal_identities']:
 p=x['path'];verify(x,x['commit'],'historical B04 accepted original');b04.append(dict(historical=x,baseline=identity(B,p),candidate=identity(C,p),unchanged_baseline_to_candidate=content(B,p)==content(C,p),historical_equals_baseline=content(x['commit'],p)==content(B,p)))
 check(content(B,p)==content(C,p),'preservation','B04 all13 current predecessor paths '+p)
locks=obj(C,PREFIX+'candidate-2/whole-catalog-lock-check.json')
for n,x in enumerate(locks['locks']):
 p=x['path'];old=content(B,p);new=content(C,p);marker='## W：'.encode() if n==0 else '## CP：'.encode()
 protected_old=old[old.index(marker):] if n==0 else old[:old.index(marker)]
 protected_new=new[new.index(marker):] if n==0 else new[:new.index(marker)]
 identity_region=new[-x['protected_bytes']:] if n==0 else protected_new
 check(protected_old==protected_new and sha(identity_region)==x['protected_sha256'] and len(identity_region)==x['protected_bytes'],'locks','complete protected other-owner section plus recorded content hash '+p)
 ids=lambda b:re.findall(rb'^\| ([A-Z]+-?[0-9]+[a-z]?) \|',b,re.M)
 oi,ni2=ids(old),ids(new);check(len(oi)==x['old_id_count']and len(ni2)==x['current_id_count'],'locks','old/current whole catalog ID counts '+p)
 check([i for i in ni2 if i in oi]==oi,'locks','old order and multiplicity retained '+p)
 check([i.decode()for i in ni2 if i not in oi]==x['new_ids'],'locks','exact new catalog IDs '+p)
static=obj(C,PREFIX+'candidate-2/static-cases.json')
ledger=obj(C,PREFIX+'candidate-2/formal-change-log.json')
check(len(ledger['changes'])==73,'clauses','seventy-three final clause ledger entries')
prior_after={}
for x in ledger['changes']:
 p=x['path'];anchor_ok=x['before_text'] in content(B,p).decode() or any(x['before_text'] in t for t in prior_after.get(p,[]))
 check(anchor_ok and x['after_text'] in content(C,p).decode(),'clauses','localized ledger baseline/prior-staged anchor and actual final text '+p+' '+x['clause'])
 prior_after.setdefault(p,[]).append(x['after_text'])
limits=obj(C,PREFIX+'candidate-2/source-limits.json')
check(limits['contract_source_limits']==ct['source_limits'],'limits','all named accepted contract limits verbatim')
check(limits['configuration']==ct['configuration'],'limits','accepted configuration/UNVERIFIED limits verbatim')
for x in static['catalog_cases']:
 line=content(C,x['path']).decode().splitlines()[x['line']-1]
 check(x['id'] in line and x['input_and_premises'] in line and x['static_expected'] in line and not x['executed'],'static-metadata','catalog exact static design '+x['id'])
check(len(static['catalog_cases'])==43 and len(static['supplemental_designs'])==18 and static['executed']==0,'static-metadata','43 catalog+18 supplement all unexecuted')
write('control-bindings.json',controls);write('B04-preserved-current-identities.json',b04)
write('all87-path-identities.json',[dict(status=s,path=p,before=identity(B,p)if s=='M'else None,after=identity(C,p),coverage='COMPLETE_NORMATIVE_DIFF_SEMANTIC_READ'if s=='M'else 'ADDED_EVIDENCE_IDENTITY_AND_STRUCTURAL_AUDIT; HISTORICAL/VERIFIER_CONTENT_NOT_CORRECTNESS_APPROVAL')for s,p in allpaths])
write('identity-audit.json',dict(at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline=B,candidate=C,method='Own Python/Git/text/hash/JSON bookkeeping only; no program or vector execution',checks=len(checks),passed=sum(x['passed']for x in checks),failed=sum(not x['passed']for x in checks),results=checks,identity_bindings=identities))
print(json.dumps(dict(checks=len(checks),passed=sum(x['passed']for x in checks),failed=[x for x in checks if not x['passed']],cached_files=len(cache)),ensure_ascii=False))
