# Reviewer-owned static bookkeeping; no source behavioral execution.
import subprocess,json,pathlib,hashlib,re,stat,os
R=pathlib.Path('/workspace/b14-affected-b04-review-2');A=pathlib.Path('/tmp/b14-b04-round2-audit');S=pathlib.Path('/tmp/b14-b04-round2-reference')
B='1e6b11a47370f1c7c4659a32443fc1afda597bac';C1='47f7514765f8569ae9172bb06a2cd615e2b83b8a';C2='af39efbf32549be964cb083bd49bed6d1d5c0d2a';REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';Q='review/remediation/20261003-prepare/batches/';D=Q+'B14/candidate-2/'
def g(*a,root=R):return subprocess.check_output(['git','-C',str(root),*a])
def data(c,p):return g('show',c+':'+p)
def sha(b):return hashlib.sha256(b).hexdigest()
def ident(c,p):
 b=data(c,p);return dict(commit=c,path=p,git_blob=g('rev-parse',c+':'+p).decode().strip(),sha256=sha(b),bytes=len(b))
def j(c,p):return json.loads(data(c,p))
def w(n,x):(A/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
checks=[]
def ck(n,x,detail=None):checks.append(dict(check=n,passed=bool(x),details=detail))
fix=j(C2,D+'fix-response.json');reviews=[]
for e in fix['review_inputs']:
 i=ident(e['commit'],e['path']);ok=all(i[k]==e[k] for k in ('git_blob','sha256','bytes'));ck('fixed review identity '+e['role']+' '+e['path'],ok);reviews.append(dict(role=e['role'],identity=i,matched=ok))
ck('prior scope proposal/application bytes unchanged',g('diff','--name-only',C1,C2,'--',Q+'B14/scope-proposal-1',Q+'B14/candidate-1/original-application.json')==b'')
# Reconstruct the declared FLY text patch without changing any file or executing a vector.
def result(before,patch):
 ls=before.splitlines(keepends=True);pp=patch.splitlines(keepends=True);out=[];pos=0;k=next(i for i,l in enumerate(pp) if l.startswith(b'@@'))
 while k<len(pp):
  m=re.match(rb'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',pp[k]);assert m
  n=int(m[1])-1;out+=ls[pos:n];pos=n;k+=1;an=bn=0
  while k<len(pp) and not pp[k].startswith(b'@@'):
   op=pp[k][:1];line=pp[k][1:];assert op in (b' ',b'-',b'+')
   if op in (b' ',b'-'):assert ls[pos]==line;pos+=1;an+=1
   if op in (b' ',b'+'):out.append(line);bn+=1
   k+=1
  assert an==int(m[2] or b'1') and bn==int(m[4] or b'1')
 out+=ls[pos:];return b''.join(out)
f='specs/overworld/wp59-world-time-weather-field-moves.md';ck('sixth FLY amendment exact text result',result(data(C1,f),data(C2,D+'original-FLY-amendment.patch'))==data(C2,f))
cat='deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'
def row(c,id):return next(l for l in data(c,cat).splitlines(keepends=True) if l.startswith(('| '+id+' |').encode()))
for id in ('WT31','WT32','WT36','MP27'):ck('C1 to C2 unchanged '+id,row(C1,id)==row(C2,id))
f='deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md'
def sect(c,a,b):return data(c,f).split(a.encode(),1)[1].split(b.encode(),1)[0]
ck('WP59 section4.1 unchanged',sect(C1,'### 4.1','### 4.2')==sect(C2,'### 4.1','### 4.2'))
old=j(C1,Q+'B14/candidate-1/contributions.json');new=j(C2,Q+'B14/candidate-1/contributions.json');ck('historical contributions unchanged',old==new)
records=[]
for line in g('diff','--name-status',C1,C2).decode().splitlines():
 status,p=line.split('\t')
 if not p.startswith(D):continue
 bb=data(C2,p);rec=dict(identity=ident(C2,p),kind='exact patch text' if p.endswith('.patch') else 'structured JSON' if p.endswith('.json') else 'text')
 if p.endswith('.json'):json.loads(bb);ck('candidate2 JSON parse '+p,True)
 bb.decode('utf8',errors='strict');records.append(rec)
manifest=json.load(open(A/'complete-change-manifest.json'))
ck('cumulative46 paths',len(manifest['changes']['B-to-C2'])==46)
ck('successor22 paths',len(manifest['changes']['C1-to-C2'])==22)
# Whitespace diagnostics of committed documents, not execution/acceptance tests.
wh=[]
for start,label in [(B,'B-to-C2'),(C1,'C1-to-C2')]:
 for scope in ('all','formal','nonpatch'):
  paths=[] if scope=='all' else ['deliverables','specs'] if scope=='formal' else [x['path'] for x in manifest['changes'][label] if not x['path'].endswith('.patch')]
  z=subprocess.run(['git','-C',str(R),'diff','--no-ext-diff','--no-textconv','--check',start,C2,'--',*paths],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out=z.stdout+z.stderr
  warning_paths=sorted(set(l.split(':',1)[0] for l in out.decode().splitlines() if ': trailing whitespace.' in l or ': new blank line at EOF.' in l))
  wh.append(dict(comparison=label,scope=scope,exit_code=z.returncode,output_sha256=sha(out),warning_paths=warning_paths,diagnostic_lines=out.decode().splitlines()))
  if scope!='all':ck(label+' '+scope+' whitespace',z.returncode==0)
  else:ck(label+' raw warnings confined to literal patch records',z.returncode==2 and warning_paths and all(p.endswith('.patch') for p in warning_paths))
w('whitespace-diagnostics.json',wh)
heads={}
for label,root,expected in [('current_worktree',R,C2),('main_worktree',pathlib.Path('/workspace/pokemon-essentials-clean-room'),'d0914c539c00cefc0ae6ae549caf2f8c7004a528'),('prior_B04_review',pathlib.Path('/workspace/b14-affected-b04-review'),'3aa4c41de2f58bd65405bc0855a7f45155a878c2'),('reference',S,REF)]:
 h=g('rev-parse','HEAD',root=root).decode().strip();status=g('status','--porcelain=v1',root=root).decode();heads[label]=dict(path=str(root),HEAD=h,status=status);ck(label+' exact unchanged HEAD',h==expected);ck(label+' clean before report creation',status=='')
ck('reference no remotes',g('remote',root=S)==b'')
ck('reference all entries read only',all(not (os.stat(path).st_mode & 0o222) for path in [S,*S.rglob('*')]))
reference=dict(repository='https://github.com/Maruno17/pokemon-essentials',preparation='New independent git init/direct URL exact-S depth1 fetch/detached checkout for this round; no remote configuration; chmod -R a-w after preparation. Subsequent text/Git metadata reads only.',commit=REF,tree=g('rev-parse','HEAD^{tree}',root=S).decode().strip(),HEAD=heads['reference']['HEAD'],clean=heads['reference']['status']=='',remotes=[],read_only=True,reference_inside_main_git=False,reference_program_execution=0,source_copy_into_project=False,provenance_limit='Verified fetched requested SHA/tree locally; no assertion that a movable reference branch tip is the fixed commit.')
w('reference-preparation.json',reference)
w('execution-checkpoint.json',dict(worktrees=heads,transport='A single executor disconnection interrupted read.py creation; subsequent pwd, file creation, fresh static reads and bookkeeping succeeded. Same C2 continued without relogin, duplicate task, candidate change or scope expansion.',checkpoint_dir=str(A),requested=dict(model='gpt-6.1-sol',reasoning='Ultra',speed='Standard(default)'),effective='UNVERIFIED',accepted_Plan_A=True,configuration_probes=0,quota_probes=0,child_tasks=0))
comparison=dict(independent_first_judgment=dict(identity=dict(path='first-judgment.json',sha256=sha((A/'first-judgment.json').read_bytes())),before_detailed_author_validation=True,blind_review_claim=False),fixed_review_inputs=reviews,candidate2_records=records,author_claim_comparison=[
 dict(claim='Exact C2 revised and bounded identities / scopes',assessment='FRESHLY_MATCHED',evidence='identity-checks.json; sixth FLY text patch reconstructed here; no formal writes'),
 dict(claim='503 catalog IDs preserved, WT39–40 added',assessment='FRESHLY_MATCHED',evidence='catalog-comparison.json checks complete row/order/multiplicity and whole protected sections'),
 dict(claim='Three narrow correctness fixes',assessment='SUPPORTED_WITHIN_B04_AFFECTED_SCOPE',evidence='Independent first-judgment.json and report static designs/source ranges; not full B03/R14 approval'),
 dict(claim='24 controls, 72reads/6writes/14extra/8fixed inputs',assessment='IDENTITIES_AND_CURRENT_FIELDS_FRESHLY_MATCHED',limit='Not a claim of 72 semantic rereads or all24/19 contribution acceptance'),
 dict(claim='Six local successor traceability additions',assessment='CONSISTENT_WITH_SCOPED_FIXES',evidence='fix-response.json local002/C003/C088/C100/C092/C093 map current clauses and WT28/39/40/BP18/WT31/32; prior contributions remain byte-identical'),
 dict(claim='Bounded record authored before applying',assessment='PUBLISHED_RECORD_AND_PARENT_AUTHORIZATION_CONSISTENT',limit='Static committed Git content cannot independently attest timing of uncommitted author actions; no claim of observed before-application chronology'),
 dict(claim='Author own staged reverse checks/source preparation/environment state',assessment='NOT_INDEPENDENTLY_ATTESTED_AS_AUTHOR_EXECUTION',evidence='Own text reconstruction, reference preparation and diagnostics performed instead; author or historical verifier not executed'),
 dict(claim='Formal/nonpatch whitespace pass; patch-container warnings',assessment='FRESHLY_MATCHED_SCOPE',evidence='whitespace-diagnostics.json; whole raw diffs return2 only for literal patch containers; not an overall clean diff assertion'),
 dict(claim='No runtime/Demo/vector execution; no public writes/selfapproval/closure',assessment='RETAINED_LIMITS_AND_NO_REVIEW_AUTHORIZATION_EXTENSION',limit='Own execution/write inventory is independently recorded; author historical external actions not runtime-attested')],checks=checks,passed=sum(c['passed'] for c in checks),failed=sum(not c['passed'] for c in checks))
w('author-comparison.json',comparison)
limits=j(C2,Q+'B14/candidate-1/source-limits.json');full=j('18873059e56314fcd48f6081d5a65a79301a52f6',Q+'B09/candidate-2/source-limits.json');w('source-limits.json',dict(complete_B14_inherited_limits=limits,complete_B09_inherited_limits=full,own_limits='All unlisted reference ranges/files unread this round. Data/Scripts.rxdata and all binary/serialized data; actual maps/events; executables/DLLs/mkxp.json and host/capacity output; images/audio/fonts/soundfont; eight cup-list files/pokemon_metrics samples; backup/gen directories unread/unverified. Dynamic aliases/plugins/dispatch/EventScene/shadow and real Demo chains unexhausted. No full67 berry data read or full-content compatibility claim. PBS map_metadata only92–102 was freshly read as text; no map event reachability proved.',own_execution=dict(reference_game=0,reference_behavior=0,compiler=0,converter=0,generator=0,deserializer=0,simulator=0,author_historical_verifier=0,behavior_vectors=0,runtime_observations=0,proven_Demo_chains=0),own_configuration=dict(requested_model='gpt-6.1-sol',requested_reasoning='Ultra',requested_speed='Standard(default)',effective='UNVERIFIED',Plan_A_accepted=True,configuration_probes=0,quota_probes=0,child_tasks=0)))
assert all(c['passed'] for c in checks),[c for c in checks if not c['passed']]
print(json.dumps(dict(checks=len(checks),failed=0,whitespace=[dict(comparison=x['comparison'],scope=x['scope'],exit_code=x['exit_code'],warning_files=len(x['warning_paths'])) for x in wh]),ensure_ascii=False))
