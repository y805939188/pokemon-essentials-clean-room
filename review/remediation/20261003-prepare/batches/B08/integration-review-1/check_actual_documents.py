#!/usr/bin/env python3
"""New R-B08 actual-only Git/JSON/text verifier. Never imports or runs reference/old verifiers."""
import csv,io,json,hashlib,pathlib,re,subprocess,collections,gzip
ROOT=pathlib.Path('/workspace/r-b08-actual-review')
REFROOT=pathlib.Path('/workspace/r-b08-reference')
TMP=pathlib.Path('/tmp/r-b08-actual-inputs')
ACT='49c21538e72b7a5873972cd00fcae1ee390cce64'
BASE='759eee80ce7856570fde2de12d5dcf98ce7e6017'
CAND='0f35a393d9de467cd5f7e695b6072687bb582186'
GLOBAL='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
R08='239a29c466d6efc1a5a240f57ad53b55c91f9e42'
R07='7fd9271bc77b534e0eba5b47c77034e2453dd560'
R04='ceb6c07340c8f4f2b7c508df36b2a2ef98f12711'
PAY='e91c974c5a05a55da8d6cb228afe5b30174fb02c'
BP='review/remediation/20261003-prepare/batches/B08/'
IP=BP+'integration-stage-1/'
DP='review/remediation-20261003-prepare/'
CACHE={}; checks=[]
def git(*args,root=ROOT):return subprocess.check_output(['git',*args],cwd=root)
def data(c,p):
 k=(c,p)
 if k not in CACHE:CACHE[k]=git('show',c+':'+p,root=REFROOT if c==REF else ROOT)
 return CACHE[k]
def obj(c,p):return json.loads(data(c,p))
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(v):return sha(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def check(ok,label,detail=None):checks.append({'check':label,'pass':bool(ok),**({'detail':detail} if detail is not None else {})})
def paths(c,prefix=''):return git('ls-tree','-r','--name-only',c,'--',prefix).decode().splitlines()
def statuses(a,b):return [{'change':s,'path':p} for s,p in (x.split('\t',1) for x in git('diff','--no-renames','--name-status',a,b).decode().splitlines())]
def identity(d,default=ACT,label='identity'):
 c=d.get('commit') or default;p=d['path'];b=data(c,p)
 for k,v in [('sha256',sha(b)),('bytes',len(b)),('git_blob',git('rev-parse',c+':'+p,root=REFROOT if c==REF else ROOT).decode().strip())]:
  if k in d:check(d[k]==v,label+':'+k,{'commit':c,'path':p})
def walk_identities(v,loc,default=ACT):
 if isinstance(v,dict):
  if 'path' in v and 'sha256' in v and ('bytes' in v or 'git_blob' in v) and 'line' not in v:
   identity(v,default,loc)
  for k,x in v.items():walk_identities(x,loc+'/'+k,default)
 elif isinstance(v,list):
  for i,x in enumerate(v):walk_identities(x,loc+'/'+str(i),default)
m=obj(ACT,IP+'integration-manifest.json');fr=obj(ACT,IP+'finding-registration.json');df=obj(ACT,IP+'diff-and-freeze.json');sc=obj(ACT,IP+'scope-counts.json');hs=obj(ACT,IP+'downstream-handshake.json');md=obj(ACT,IP+'merge-and-dependency-impact.json');obs=obj(ACT,IP+'scope-and-observation-registration.json')
plan={d['id']:d for d in obj(PLAN,DP+'batches.json')};orig={d['id']:d for d in obj(GLOBAL,'review/global-independent-review/2026-10-03-fd82a639/findings.json')};acc=obj(PLAN,DP+'finding-acceptance.json')
ids=plan['B08']['contribution_finding_ids'];primary=plan['B08']['primary_finding_ids']
check([d['id'] for d in fr['dispositions']]==ids,'exact17 registration ID order');check(len(ids)==17 and len(primary)==9,'17/9 plan scope')
formal=[d['candidate']['path'] for d in m['formal_candidate_identities']]
check(len(formal)==12 and set(plan['B08']['write_paths']).issubset(formal),'exact12 with planned8')
for p in formal:check(data(ACT,p)==data(CAND,p),'candidate bytes preserved:'+p)
source=m['source_identities']; check(len(source)==108,'108 incoming identities')
for d in source:
 identity(d,label='incoming source');check(data(ACT,d['path'])==data(d['commit'],d['path']),'incoming actual byte preservation:'+d['path'])
reports=[]
for c,directory,count in [(R08,'review-round-1/',13),(R07,'affected-B07-review-round-1/',22),(R04,'affected-B04-review-round-1/',16)]:
 ps=paths(c,BP+directory);reports+=ps;check(len(ps)==count,'exact report file count:'+directory)
 check(git('rev-parse',c+'^').decode().strip()==CAND,'candidate report parent:'+c)
 for p in ps:check(data(ACT,p)==data(c,p),'immutable imported report:'+p)
auth=paths(CAND,BP+'author-stage-1/')+paths(CAND,BP+'author-stage-2/');check(len(auth)==45,'45 author paths')
for p in auth:check(data(ACT,p)==data(CAND,p),'immutable author:'+p)
check(set(formal+auth+reports)=={d['path'] for d in source},'108 complete incoming union')
public=[d['path'] for d in m['current_public_paths']];management=paths(ACT,IP);check(len(public)==10 and len(management)==13,'10 public13 management')
statBA=statuses(BASE,ACT);statCA=statuses(CAND,ACT)
check(len(statBA)==131 and {d['path'] for d in statBA}==set(formal+auth+reports+public+management),'full131 partition')
check(len(statCA)==74 and {d['path'] for d in statCA}==set(reports+public+management),'full74 partition')
check(all(d['change']==('M' if d['path'] in formal+public else 'A') for d in statBA),'all131 kinds')
check(all(d['change']==('M' if d['path'] in public else 'A') for d in statCA),'all74 kinds')
check(git('rev-parse',ACT+'^').decode().strip()==PAY,'actual single parent payload');check(len(git('show','-s','--format=%P',ACT).decode().split())==1,'one actual parent')
check(statuses(PAY,ACT)==[{'change':'A','path':p} for p in sorted(m['final_evidence_paths'])],'only3 final evidence additions')
for d in m['normal_merges']:
 check(git('show','-s','--format=%P',d['commit']).decode().split()==d['parents'],'native merge parents:'+d['commit'])
 check(git('rev-parse',d['commit']+'^{tree}').decode().strip()==d['tree'],'native merge tree:'+d['commit'])
 for p in paths(d['parents'][1],BP):
  if p.startswith(BP+'integration-'):continue
  check(data(d['commit'],p)==data(d['parents'][1],p),'merge fixed second-parent bytes:'+p)
for d in df['full_patches']:
 b=git('diff',*d['git_diff_options'],d['base_commit'],d['target_commit']);check(b==data(ACT,d['path']),'exact unfiltered payload patch:'+d['path']);identity(d,label='saved payload diff')
 check(statuses(d['base_commit'],d['target_commit'])==d['complete_path_statuses'],'saved full payload statuses:'+d['path'])
for c,name in [(BASE,'predecessor-to-actual'),(CAND,'candidate-to-actual')]:
 b=git('diff','--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3',c,ACT)
 (TMP/(name+'.full-index.diff')).write_bytes(b)
 with (TMP/(name+'.full-index.diff.gz')).open('wb') as fp:fp.write(gzip.compress(b,mtime=0))
# Fixed controls and their full duplicated qualifications, roots, cases and every extension.
for d in fr['dispositions']:
 i=d['id'];a=acc[i];o=orig[i]
 check(d['complete_original_object']==o,'full original:'+i);check(d['complete_approved_acceptance']==a,'full acceptance:'+i)
 check(d['original_complete_object_sha256']==canon(o) and d['acceptance_object_sha256']==canon(a),'full object hashes:'+i)
 check(d['B08_primary']==(i in primary) and d['priority']==o['priority'],'primary and severity:'+i)
 for k,expected in [('current_qualifications',o.get('current_qualifications')),('root_adjudications',o.get('root_adjudications',[])),('all_extensions',o.get('extensions',[])),('minimum_revision',o.get('minimum_revision')),('determinate_recheck',o.get('determinate_recheck')),('acceptance_gate',a.get('acceptance_gate'))]:
  check(d[k]==expected,'registration control:'+i+':'+k)
 control=d['accepted_B07_contract_control_preserved'];check(control['complete_original_object']==o and control['complete_approved_acceptance']==a,'accepted B07 full control:'+i)
 check(d['all_contributor_batches']==control['all_contributors'] and d['other_batch_obligations']==control['other_contributors_pending'] and d['accepted_other_contributors_at_fixed_versions']==control['accepted_other_contributors_at_fixed_receipts'],'owner residuals:'+i)
 check(d['full_R08_candidate_disposition_preserved']==next(x for x in obj(R08,BP+'review-round-1/contribution-review.json') if x['id']==i),'immutable R08 candidate judgment:'+i)
 check(d['author_proposal_preserved']==next(x for x in obj(CAND,BP+'author-stage-2/finding-contribution-map.json') if x['id']==i),'immutable author proposal:'+i)
 check(d['canonical_state']=='OPEN' and d['canonical_edited'] is False and d['canonical_closure'] is False,'no canonical closure:'+i)
 check(d['actual_R08']=='PENDING_ULTRA' and d['actual_affected_R07']=='PENDING_SEPARATE_ULTRA' and d['actual_affected_R04']=='PENDING_SEPARATE_BOUNDED_ULTRA' and d['parent_C_acceptance']=='NOT_PERFORMED','triple actual+C gate:'+i)
 for row in d['static_row_bindings_not_executed']:
  line=data(ACT,row['path']).splitlines(keepends=True)[row['line']-1];check(row['sha256']==sha(line) and row['bytes']==len(line),'actual static binding:'+i+':'+row['id'])
# Recursively verify explicitly addressed evidence identities, including all new management freeze copies.
for name,d in [('manifest',m),('registration',fr),('freeze',df),('counts',sc),('handshake',hs),('dependency',md),('scope',obs)]:walk_identities(d,name)
# Current-hashes TSV uses external exact SHA for blank commits, independently resolved here.
rows=list(csv.DictReader(io.StringIO(data(ACT,IP+'current-hashes.tsv').decode()),delimiter='\t'))
for r in rows:
 d={k:r[k] for k in ['path','git_blob','sha256','commit']};d['bytes']=int(r['bytes']);identity(d,label='current-hashes:'+r['kind'])
# Registries append17 only; no old133 changes. Inspect every new semantic field.
registry_rows={}
for name in ['approval-ledger.tsv','traceability-successor.tsv']:
 p='review/remediation/20261003-prepare/'+name;b=data(BASE,p);n=data(ACT,p);check(n.startswith(b),'immutable previous registry prefix:'+name)
 old=list(csv.DictReader(io.StringIO(b.decode()),delimiter='\t'));new=list(csv.DictReader(io.StringIO(n.decode()),delimiter='\t'));registry_rows[name]=new
 check(len(old)==133 and len(new)==150 and [r['finding_id'] for r in new[133:]]==ids,'133+17 registry order:'+name)
 for r,d in zip(new[133:],fr['dispositions']):
  check(r['canonical_state']=='OPEN' and r['candidate_commit']==CAND and r['candidate_review_commit']==R08,'exact candidate registry identity:'+name+':'+r['finding_id'])
  rem=json.loads(r['remaining_obligations']);check(rem['canonical_closure'] is False and rem['actual_R08']=='PENDING_ULTRA' and rem['actual_affected_R07']=='PENDING_SEPARATE_ULTRA' and rem['actual_affected_R04']=='PENDING_SEPARATE_BOUNDED_ULTRA' and rem['parent_C']=='NOT_PERFORMED','registry no premature acceptance:'+name+':'+r['finding_id'])
  check(rem['all_contributors']==d['all_contributor_batches'] and rem['other_batch_obligations']==d['other_batch_obligations'],'registry owner duties:'+name+':'+r['finding_id'])
  check(rem['candidate_reports']==m['candidate_reports'],'three frozen candidate receipts:'+name+':'+r['finding_id'])
  if name=='approval-ledger.tsv':
   check(r['candidate_verdict']=='PASS_SCOPED' and r['downstream_gate']=='BLOCKED' and r['integration_verdict']=='NOT_REVIEWED_PENDING_THREE_ULTRA','ledger exact statuses:'+r['finding_id'])
   check(('PRIMARY' in r['accepted_contribution_kind'])==d['B08_primary'],'ledger9 primary:'+r['finding_id'])
  else:
   x=json.loads(r['current_clause_inputs']);check(x['reviewed_candidate']==CAND and x['formal_candidate_identities']==[x['candidate'] for x in m['formal_candidate_identities']],'trace formal input bindings:'+r['finding_id'])
   check(x['authorized_original_paths']==d['authorized_original_paths'],'trace original scope:'+r['finding_id'])
# Historical public markdown preserved, catalog index only3 authorized navigation rows.
for p in public:
 if not p.endswith('.md'):continue
 old=data(BASE,p).decode().splitlines();new=data(ACT,p).decode().splitlines()
 if p.endswith('test-catalog/README.md'):
  matcher=__import__('difflib').SequenceMatcher(None,old,new,autojunk=False);replaced=[old[a:b] for tag,a,b,c,d in matcher.get_opcodes() if tag in ['replace','delete']]
  check(sum(map(len,replaced))==3 and all(x.startswith('| [') for chunk in replaced for x in chunk),'catalog index only3 old rows')
 else:
  it=iter(new);check(all(any(v==x for v in it) for x in old),'old public prose ordered preservation:'+p)
# Approval patch exact4 before/prepared-after/current identities and reverse applicability CHECK ONLY.
request=obs['original_sync_request_preserved'];check(request==obj(CAND,BP+'author-stage-1/original-sync-request-v2.json'),'complete scope request preserved')
patch=request['patch'];check(sha(data(ACT,patch['path']))=='05b75bcafcb1fd9359e9a35e935e8b7cbb7dd038a0f3349a1172d1fe3ba88f25','authorized original patch hash')
check(len(request['paths'])==4,'only4 originals');check(obs['parent_authorization_record_preserved']==obj(CAND,BP+'author-stage-2/parent-authorization-and-preapply.json'),'original permission record preserved');check(obs['original_application_preserved']==obj(CAND,BP+'author-stage-2/original-application.json'),'original application preserved')
for d in request['paths']:
 identity(dict(d['before'],path=d['path']),BASE,'original before');identity(dict(d['prepared_after'],path=d['path']),ACT,'original exact prepared after')
reverse=subprocess.run(['git','apply','--reverse','--check',str(ROOT/patch['path'])],cwd=ROOT,capture_output=True);check(reverse.returncode==0,'exact original patch reverse CHECK ONLY',reverse.stderr.decode())
# Catalog rows, order, five corrected old rows,14 protected sections and15 unexecuted designs.
def static_rows(c,p):
 out=[]
 for n,l in enumerate(data(c,p).splitlines(keepends=True),1):
  match=re.match(rb'^\| ([A-Z]+-?\d+) \|',l)
  if match:out.append((match[1].decode(),l,n))
 return out
changed=[];newids=[];totalold=totalnew=0; protected=0
allowed_sections={'DC','EG','EN','RM','BR'}
for p in [p for p in formal if '/test-catalog/' in p]:
 old=static_rows(BASE,p);new=static_rows(ACT,p);totalold+=len(old);totalnew+=len(new); oldmap={i:l for i,l,n in old};newmap={i:l for i,l,n in new}
 check([i for i,l,n in new if i in oldmap]==[i for i,l,n in old],'old catalog ID ordered occurrences:'+p)
 changed += [i for i,l,n in old if l.rstrip(b'\n')!=newmap[i].rstrip(b'\n')]
 newids += [i for i,l,n in new if i not in oldmap]
 def sections(c):
  txt=data(c,p);return dict((m.group(1).decode(),m.group(0)) for m in re.finditer(rb'^## ([A-Z]+).*?(?=^## |\Z)',txt,re.M|re.S))
 ob=sections(BASE);nb=sections(ACT)
 for s in ob:
  if s not in allowed_sections:protected+=1;check(ob[s]==nb[s],'protected whole section:'+p+':'+s)
 declared=df['catalogs'][p];check(declared['before']==len(old) and declared['after']==len(new),'catalog declared count:'+p)
check(changed==['DC-08','EG-13','EN-01','EN-15','EN-16'],'exact5 old row text revisions',changed)
check(totalold==649 and totalnew==664 and len(newids)==15 and protected==14,'649 to66415 designs14 protected sections')
check(set(newids)=={d['id'] for d in sc['new_static_ids']},'exact15 new static identity membership')
for d in sc['new_static_ids']:
 l=data(ACT,d['path']).splitlines(keepends=True)[d['line']-1];check(sha(l)==d['sha256'] and len(l)==d['bytes'],'new row identity:'+d['id'])
for p in ['specs/pokemon-rules/wp34-inheritance-and-offspring.md','deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md']:
 check(data(BASE,p)==data(ACT,p),'WP34 entire body unchanged:'+p)
# Full fixed plan B09 scope and other-owner residual controls; all current79/62 bindings.
b9=hs['B09'];check(len(b9['planned_reads'])==62 and {d['path'] for d in b9['planned_reads']}==set(plan['B09']['read_paths']),'B09 exact62 plan paths')
check(b9['allowed_formal_write_paths']==plan['B09']['write_paths'] and len(b9['allowed_formal_write_paths'])==7,'B09 exact7 writes');check(b9['primary_finding_ids']==plan['B09']['primary_finding_ids'] and len(b9['primary_finding_ids'])==13,'B09 exact13 primary')
check([d['id'] for d in b9['complete20_fixed_controls']]==plan['B09']['contribution_finding_ids'],'B09 exact20 control membership')
for d in b9['complete20_fixed_controls']:
 i=d['id'];check(d['complete_original_object']==orig[i] and d['complete_approved_acceptance']==acc[i],'B09 inherited full controls:'+i)
 check(d['original_complete_object_sha256']==canon(orig[i]) and d['acceptance_object_sha256']==canon(acc[i]),'B09 control hashes:'+i)
check(b9['accepted'] is False and b9['task_dispatched'] is False and b9['original_specs_write_authorized'] is False,'B09 no acceptance dispatch original permission')
check(len(hs['B08_effective_read_versions'])==79 and {d['path'] for d in hs['B08_effective_read_versions']}==set(plan['B08']['read_paths']),'all79 exact B08 plan inputs')
for d in hs['B08_effective_read_versions']:
 for key,c in [('author_input',BASE),('candidate_version',CAND),('current_actual_input',ACT)]:identity(d[key],c,'79 '+key)
check(len(md['five_changed_B07_readers'])==5,'five B07 changed readers')
for x in hs['downstream_batches']:
 p=plan[x['batch']];check(x['planned_dependencies']==p['dependencies'] and x['planned_read_count']==len(p['read_paths']) and x['planned_write_count']==len(p['write_paths']),'downstream complete plan dimensions:'+x['batch'])
 for filename,key in [('semantic-dependencies.tsv','semantic_rows'),('physical-conflicts.tsv','physical_rows'),('shared-premise-conflicts.tsv','shared_premise_rows')]:
  rs=list(csv.DictReader(io.StringIO(data(PLAN,DP+filename).decode()),delimiter='\t'))
  relevant=[r for r in rs if (r.get('upstream')=='B08' and r.get('downstream')==x['batch']) or ({r.get('batch_a'),r.get('batch_b')}=={'B08',x['batch']}) or ('B08' in r.get('contributors','').split(';') and x['batch'] in r.get('contributors','').split(';'))]
  check(x[key]==relevant,'all exact downstream conflict rows:'+x['batch']+':'+key)
  check(x['status'].startswith('NOT_DISPATCHED'),'downstream still blocked:'+x['batch'])
check(hs['parallel_writers_authorized']==0 and hs['public_writer']=='A-REG_ONLY' and hs['downstream_tasks_dispatched']==0,'writer/dispatch gates')
check(hs['B04_two_caller_gate_preserved']['decision']=='REQUIRED_SEPARATE_AFFECTED_B04_CANDIDATE_AND_ACTUAL_ULTRA_STANDARD' and len(hs['B04_actual_scope_preserved']['cases'])==2 and hs['B04_actual_pending'] is True,'separate bounded B04 actual gate')
# Bind exact accepted B07 controls and preserve every B04 formal output and B06 audio input.
b7contract=obj(BASE,'review/remediation/20261003-prepare/batches/B07/acceptance-stage-1/downstream-handshake.json')
check([d['accepted_B07_contract_control_preserved'] for d in fr['dispositions']]==b7contract['contribution_controls'],'all17 accepted B07 control objects unchanged')
b4=obj(BASE,'review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/acceptance-manifest.json')['accepted_formal_identities']
check(len(b4)==13,'B04 exact13 protected outputs')
for d in b4:check(data(BASE,d['path'])==data(ACT,d['path']),'B04 accepted entire output unchanged:'+d['path'])
b6path=hs['B06_WP24']['current']['path'];check(data(BASE,b6path)==data(ACT,b6path),'B06 WP24 entire bytes unchanged')
check(md['accepted_B07_preservation_dispositions']==obj(R07,BP+'affected-B07-review-round-1/B07-conclusion-dispositions.json'),'all19 B07 candidate dispositions exact preserved')
for p in paths(CAND,BP+'author-stage-1/'):check(data(CAND,p)==data('d6367692610c83fd24bd1ab8d2ab0cfa6757314d',p),'frozen WIP stage1 unchanged:'+p)
for d in fr['dispositions']:check(d['effective_case_constraints']==d['complete_original_object'].get('effective_case_constraints'),'case constraints:'+d['id'])
# Accepted statistics are copied verbatim, candidate counts excluded.
check(sc['prior_accepted_statistics_preserved']==obj(BASE,sc['prior_accepted_statistics_identity']['path']),'prior accepted statistics exact full object')
check(sc['prior_accepted_records']==133 and sc['current_public_contribution_records']==150 and sc['accepted_B08_contributions']==0,'accepted vs candidate denominators')
# Explicitly preserve unknowns and zero claims, without executing any historical program.
for name,d in [('manifest',m),('scope',obs),('freeze',df)]:
 check(d['configuration']['effective_model_reasoning_speed']=='UNVERIFIED' and d['configuration']['configuration_probes']==0 and d['configuration']['quota_probes']==0 and d['configuration']['quota_checks_temporarily_disabled_by_user'] is True,'UNVERIFIED Plan A quota disabled:'+name)
 check(d['source_limits']['retained_source_limits']==['U01–U10','G01–G12','AX01–AX20'],'unknown families:'+name)
for d in obs['source_limits']['inherited_limits_preserved_verbatim']:
 check(d['limits']=={k:obj(d['identity']['commit'],d['identity']['path'])[k] for k in d['limits']},'inherited named unread exact')
# Whitespace: calculate the real exact actual denominator; raw saved patches deliberately remain immutable.
whitespace={}
for base,label in [(BASE,'predecessor_to_actual'),(CAND,'candidate_to_actual'),(BASE,'predecessor_to_candidate')]:
 target=CAND if label=='predecessor_to_candidate' else ACT
 r=subprocess.run(['git','diff','--check',base,target],cwd=ROOT,capture_output=True);s=r.stdout.decode(); diag=[l for l in s.splitlines() if re.search(r': (trailing whitespace|new blank line at EOF)\.$',l)];kind=collections.Counter(l.rsplit(': ',1)[1] for l in diag)
 whitespace[label]={'exit_code':r.returncode,'total_diagnostics':len(diag),'classified':dict(kind),'paths':sorted({l.split(':',1)[0] for l in diag})}
 check(all(p.endswith(('.diff','.patch')) for p in whitespace[label]['paths']),'whitespace only exact stored patch artifacts:'+label)
check(whitespace['predecessor_to_candidate']['total_diagnostics']==353 and whitespace['predecessor_to_candidate']['classified']=={'trailing whitespace.':344,'new blank line at EOF.':9},'N01 exact fixed candidate353=344+9')
r=subprocess.run(['git','diff','--check',BASE,ACT,'--',*formal],cwd=ROOT,capture_output=True);check(r.returncode==0,'12 current formal diff check')
# Save all exact input identities and complete unfiltered path manifests; do not infer semantic conclusions from these checks.
result={'reviewed_actual':ACT,'baseline':BASE,'candidate':CAND,'checks':len(checks),'failed':[x for x in checks if not x['pass']],'check_records':checks,'full_path_counts':{'predecessor_to_actual':len(statBA),'candidate_to_actual':len(statCA)},'whitespace':whitespace,'behavior_vectors_executed':0,'reference_program_execution':0,'historical_author_or_reviewer_verifier_execution':0,'scope':'Git/JSON/text identity, ordering, protected scope and registration semantics only; manual behavioral judgments separately documented'}
(TMP/'independent-document-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
manifest={'actual':ACT,'actual_tree':git('rev-parse',ACT+'^{tree}').decode().strip(),'predecessor':BASE,'candidate':CAND,'full_predecessor_to_actual_statuses':statBA,'full_candidate_to_actual_statuses':statCA,'input_identities':[{'commit':c,'path':p,'sha256':sha(b),'bytes':len(b),'git_blob':git('rev-parse',c+':'+p,root=REFROOT if c==REF else ROOT).decode().strip()} for (c,p),b in sorted(CACHE.items())]}
(TMP/'independent-input-identities.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'failed':result['failed'],'paths':[len(statBA),len(statCA)],'whitespace':whitespace},ensure_ascii=False,indent=2))
