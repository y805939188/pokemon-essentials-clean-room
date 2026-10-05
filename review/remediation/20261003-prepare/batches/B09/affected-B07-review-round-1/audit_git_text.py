"""Independent Git/JSON/hash and specification-text bookkeeping, not behavior tests.
Never import or execute candidate/reference programs; no reference writes.
"""
import collections,hashlib,json,pathlib,re,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[6]
OUT=pathlib.Path(__file__).resolve().parent
BASE='407536adb682a04161d3e9c82f153a62b1becd97'
C='18873059e56314fcd48f6081d5a65a79301a52f6'
C1='8ff72341b5b91736970b5bfa5dc1b88137e618a5'
PAY='ab81adc17a0ee50f21032c58036b7b56b28da51b'
F='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
A='41fffb540c6483f5296ea0d33b789b75180d27ed'
OLD='ca3df824fe4379b7bf8e783a885f5cb0be038ba4'
B09='review/remediation/20261003-prepare/batches/B09/'
P=B09+'candidate-2/'
oldP='review/remediation/20261003-prepare/batches/B08/affected-B07-integration-review-1/'
checks=[]
def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args])
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(c,p):return git('show',c+':'+p)
def js(c,p):return json.loads(blob(c,p))
def ident(c,p):
 b=blob(c,p);return {'commit':c,'path':p,'git_blob':git('rev-parse',c+':'+p).decode().strip(),'sha256':sha(b),'bytes':len(b)}
def check(label,ok,detail=None):checks.append({'check':label,'pass':bool(ok),'detail':detail})
def verify(rec,c=None,p=None,label='identity'):
 c=rec.get('commit') or c;p=rec.get('path') or p
 actual=ident(c,p)
 for k in ['git_blob','sha256','bytes']:
  if k in rec:check(label+':'+p+':'+k,rec[k]==actual[k])
 return actual
def dump(name,o):(OUT/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def changes(a,b):return [tuple(x.split('\t')) for x in git('diff','--name-status','--no-renames',a,b).decode().splitlines()]
def objhash(o):return sha(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
norm=js(C,P+'normative-identities.json');env=js(C,B09+'freeze-envelope-2/payload-manifest.json');scope=js(C,P+'amended-scope.json')
paths=[x['after']['path'] for x in norm['files']]
ch=changes(BASE,C);payloadch=changes(BASE,PAY);c1ch=changes(C1,C)
check('candidate exact single parent',git('rev-parse',C+'^').decode().strip()==PAY)
check('payload exact single parent',git('rev-parse',PAY+'^').decode().strip()==C1)
check('payload tree exact',git('rev-parse',PAY+'^{tree}').decode().strip()==env['payload_tree'])
check('87 full changed paths',len(ch)==87)
check('14 modified normative + 73 added evidence',collections.Counter(x[0] for x in ch)=={'M':14,'A':73})
check('normative14 exact complete scope',set(paths)==set(scope['complete_normative_write_paths'])=={p for s,p in ch if s=='M'})
check('8 final + 6 original',sum(p.startswith('deliverables/') for p in paths)==8 and sum(p.startswith('specs/') for p in paths)==6)
check('no out of scope evidence path',all(p.startswith(B09) for s,p in ch if s=='A'))
check('full final path list exact',set(env['full_final_changed_paths'])=={p for s,p in ch})
check('83 payload paths exact',len(payloadch)==83 and {p for s,p in payloadch}=={x['path'] for x in env['payload_changed_paths']})
check('four envelope-only paths exact',changes(PAY,C)==[('A',p) for p in sorted(env['envelope_expected_new_paths'])])
check('candidate1 amendment31 exact',len(c1ch)==31 and sum(s=='M' for s,p in c1ch)==2)
check('remaining12 normative unchanged',all(blob(C1,p)==blob(C,p) for p in scope['original_twelve_unchanged']))
check('candidate1/history unchanged',all(blob(C1,p)==blob(C,p) for p in git('ls-tree','-r','--name-only',C1,B09).decode().splitlines()))
pathrecs=[]
for s,p in ch:
 rec={'status':s,'path':p,'after':ident(C,p)}
 if s=='M':rec['before']=ident(BASE,p)
 pathrecs.append(rec)
 if p.endswith('.json'):
  js(C,p);check('JSON parse '+p,True)
for x in norm['files']:
 verify(x['before'],label='norm-before');verify(x['candidate_1'],label='norm-c1');verify(x['after'],C,label='norm-after')
 check('norm changed flag '+x['after']['path'],x['changed_since_candidate_1']==(blob(C1,x['after']['path'])!=blob(C,x['after']['path'])))
for x in env['payload_changed_paths']:
 for k,c in [('before',BASE),('candidate_1',C1),('after',PAY)]:
  if x[k] is not None:verify(x[k],c,x['path'],'payload-'+k)
  else:check('payload absent '+k+':'+x['path'],git('ls-tree',c,'--',x['path'])==b'')
diffs=[]
for a,b,label in [(BASE,C,'complete-baseline-to-candidate'),(BASE,PAY,'complete-baseline-to-payload'),(C1,C,'complete-candidate1-to-candidate'),(C1,PAY,'complete-candidate1-to-payload'),(PAY,C,'complete-payload-to-candidate')]:
 bts=git('diff','--no-ext-diff','--binary',a,b);diffs.append({'from':a,'to':b,'label':label,'sha256':sha(bts),'bytes':len(bts),'path_filter_used':False,'path_count':len(changes(a,b))})
for k,a,b in [('full_unfiltered_predecessor_to_payload_diff',BASE,PAY),('full_unfiltered_candidate_1_to_payload_diff',C1,PAY)]:
 r=env[k]; data=blob(C,B09+'freeze-envelope-2/'+r['path']);check('envelope stored diff exact '+k,data==git('diff','--no-ext-diff','--binary',a,b));check('envelope diff hash '+k,sha(data)==r['sha256'] and len(data)==r['bytes'])
(OUT/'independent-normative-delta.patch').write_bytes(git('diff','--no-ext-diff',BASE,C,'--',*paths))
dump('candidate-and-complete-paths.json',{'baseline':BASE,'candidate':C,'candidate_parent':PAY,'candidate_tree':git('rev-parse',C+'^{tree}').decode().strip(),'candidate1':C1,'diff_streams':diffs,'changed_paths':pathrecs})
contractpath='review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/B09-downstream-contract.json'
contract=js(BASE,contractpath);verify(scope['unchanged_executable_contract'],label='fixed contract');check('executable contract unchanged',blob(BASE,contractpath)==blob(C,contractpath))
cover=js(C,P+'read-coverage.json');coverrecs=[]
check('62 original + 8 additional identity bindings',len(cover['readers'])==70 and len(contract['planned_reads'])==62)
for x in cover['readers']:
 old=verify(x['frozen_input'],BASE,x['path'],'read-frozen');now=verify(x['current_refreeze'],C,x['path'],'read-current');prior=verify(x.get('candidate_1_refreeze',{}),C1,x['path'],'read-c1')
 check('reader changed flag '+x['path'],x['changed']==(old['sha256']!=now['sha256']))
 coverrecs.append({'path':x['path'],'frozen':old,'candidate1':prior,'current':now,'changed':old['sha256']!=now['sha256'],'full_semantic_read_this_round':False})
for x in contract['planned_reads']:
 current=next(y for y in coverrecs if y['path']==x['path']);check('original planned frozen binding '+x['path'],all(current['frozen'][k]==x[k] for k in ['git_blob','sha256','bytes']))
check('no all70 full semantic claim',cover['semantic_full_all_amended_claimed'] is False)
dump('input-refreeze.json',{'original_planned_count':62,'additional_count':8,'all70_identity_only':True,'no_whole70_semantic_claim':True,'bindings':coverrecs})
# Exact approved specification patch reconstruction is text bookkeeping only.
def projected_patch(before,patch):
 old=before.decode().splitlines(keepends=True); output=[];pos=0;lines=patch.decode().splitlines(keepends=True);i=0;hunks=0
 while i<len(lines):
  m=re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i])
  if not m:i+=1;continue
  start=int(m[1])-1;nold=int(m[2] or 1);nnew=int(m[4] or 1);start=max(start,0);i+=1;lhs=[];rhs=[]
  while i<len(lines) and not lines[i].startswith(('@@ ','diff --git ','--- ')):
   t=lines[i]
   if t.startswith(' '):lhs.append(t[1:]);rhs.append(t[1:])
   elif t.startswith('-'):lhs.append(t[1:])
   elif t.startswith('+'):rhs.append(t[1:])
   elif t.startswith('\\'):raise ValueError('No-newline marker outside this supported exact-text audit')
   else:break
   i+=1
  assert len(lhs)==nold and len(rhs)==nnew
  assert start>=pos and old[start:start+nold]==lhs
  output.extend(old[pos:start]);output.extend(rhs);pos=start+nold;hunks+=1
 output.extend(old[pos:]);assert hunks
 return ''.join(output).encode(),hunks
proposal=js(C,B09+'scope-proposal-1/original-sync-proposal.json');auth5=js(C,B09+'candidate-1/original-scope-approval.json');auth2=js(C,B09+'scope-amendment-2/approval.json');applied=js(C,B09+'scope-amendment-2/application.json')
check('five original scope only authorization',auth5['scope_authorized'] is True and auth5['correctness_approval'] is False)
check('five original exact checkpoint manifest hash',sha(blob(auth5['approved_checkpoint_sha'],B09+'scope-proposal-1/original-sync-proposal.json'))==auth5['manifest_sha256'])
check('five original approved checkpoint proposal retained',blob(auth5['approved_checkpoint_sha'],B09+'scope-proposal-1/original-sync-proposal.json')==blob(C,B09+'scope-proposal-1/original-sync-proposal.json'))
check('WP20 exact scope only authorization',auth2['scope_authorization_only'] is True and auth2['independent_correctness_approval'] is False and auth2['public_registry_write_authorized'] is False)
check('authorized immutable WP20 proposal hash',sha(blob(C1,auth2['approved_proposal_path']))==auth2['approved_proposal_sha256'])
patchrecords=[]
for x in proposal['files']:
 p=x['path'];verify(x['before'],BASE,p,'orig-before');verify(x['intended_after'],C,p,'orig-after')
 data=blob(C,x['complete_diff_path']);check('original proposed patch hash '+p,sha(data)==x['complete_diff_sha256']==auth5['exact_original_patch_sha256'][p])
 projected,hunks=projected_patch(blob(BASE,p),data);check('exact projected authorized original result '+p,projected==blob(C,p))
 patchrecords.append({'path':p,'clauses':len(x['clauses']),'hunks':hunks,'patch':ident(C,x['complete_diff_path']),'before':ident(BASE,p),'after':ident(C,p),'scope_authorized':True,'quality_approved_by_scope_record':False})
check('five original30 clauses exact',sum(x['clauses'] for x in patchrecords)==30)
for x in auth2['files']:
 p=x['path'];verify(x['before'],BASE,p,'WP20-before');verify(x['intended_after'],C,p,'WP20-after')
 data=blob(C,B09+'candidate-1/'+x['full_diff']['path']);check('WP20 patch exact authorized hash '+p,sha(data)==auth2['approved_patch_sha256'][p])
 projected,hunks=projected_patch(blob(C1,p),data);check('WP20 projected exact current result '+p,projected==blob(C,p))
 text=blob(C1,p).decode()
 for z in x['clause_changes']:
  check('WP20 literal before unique '+p+str(z['before_lines']),text.count(z['before_text'])==1)
  text=text.replace(z['before_text'],z['intended_after_text'],1)
 check('WP20 only two exact literals '+p,text.encode()==blob(C,p))
 patchrecords.append({'path':p,'clauses':len(x['clause_changes']),'hunks':hunks,'patch':ident(C,B09+'candidate-1/'+x['full_diff']['path']),'before':ident(C1,p),'after':ident(C,p),'scope_authorized':True,'quality_approved_by_scope_record':False})
check('WP20 exactly4 clauses + previous originals30',sum(x['clauses'] for x in patchrecords)==34)
dump('approved-scope-text-check.json',{'five_originals30_and_WP20_pair4':patchrecords,'six_original_paths':6,'WP20_final_is_eighth_final':True,'author_gate_claims_are_not_approval':True,'patch_projection_in_memory_only':True})
# Current complete canonical controls, not raw or old status projections.
fp='review/global-independent-review/2026-10-03-fd82a639/findings.json';ap='review/remediation-20261003-prepare/finding-acceptance.json'
findings={x['id']:x for x in js(F,fp)};acc=js(A,ap);ownold=js(OLD,oldP+'fixed-control-bindings.json')
controls=[]
for old in ownold['records']:
 id=old['id'];orig=findings[id];accept=acc[id]
 check('B07 full original object '+id,objhash(orig)==old['original_complete_object_sha256'])
 check('B07 full acceptance object '+id,objhash(accept)==old['acceptance_complete_object_sha256'])
 controls.append({'id':id,'complete_original_object_sha256':objhash(orig),'complete_acceptance_object_sha256':objhash(accept),'current_qualifications':orig.get('current_qualifications'),'effective_case_constraints':orig.get('effective_case_constraints'),'root_adjudications':orig.get('root_adjudications',[]),'extensions':[{k:v for k,v in e.items() if k!='extension'} for e in orig.get('extensions',[])],'extension_decisions':orig.get('extension_decisions',[]),'prior_own_record':old})
for x in contract['contribution_controls']:
 id=x['id'];check('B09 complete20 control original '+id,objhash(findings[id])==x['original_complete_object_sha256']);check('B09 complete20 control acceptance '+id,objhash(acc[id])==x['acceptance_object_sha256']);check('B09 contract original full object '+id,x['complete_original_object']==findings[id]);check('B09 contract acceptance full object '+id,x['complete_approved_acceptance']==acc[id])
dis=js(C,P+'contribution-dispositions.json');check('B09 20/13 complete OPEN',len(dis['dispositions'])==20 and sum(x['primary'] for x in dis['dispositions'])==13 and all(x['canonical_state']=='OPEN' and x['canonical_closed'] is False for x in dis['dispositions']))
for x in dis['dispositions']:
 id=x['id'];s=x['source_control'];check('B09 author complete original hash '+id,s['complete_original_object_sha256']==objhash(findings[id]));check('B09 author complete acceptance hash '+id,s['complete_approved_acceptance_sha256']==objhash(acc[id]));check('B09 author current qualification '+id,s['current_qualifications']==findings[id].get('current_qualifications'));check('B09 author complete roots '+id,s['root_adjudications']==findings[id].get('root_adjudications',[]));check('B09 author all finalized extension controls '+id,[(e['report'],e['raw_id'],e['root_review']) for e in s['extensions']]==[(e['report'],e['raw_id'],e['root_review']) for e in findings[id].get('extensions',[])])
dump('fixed-control-bindings.json',{'original':ident(F,fp),'acceptance':ident(A,ap),'previous_own_controls':ident(OLD,oldP+'fixed-control-bindings.json'),'B07_records19':controls,'B09_complete20_contract_controls_verified':True,'required_canonical_count':sum(x.get('required_revision',False) for x in findings.values()),'no_canonical_closure':True})
# B07 whole owner outputs, exact row bytes/order/occurrences and shared protected regions.
prior=js(OLD,oldP+'dependency-and-preservation.json');owner=[]
for x in prior['accepted_B07_outputs14']:
 p=x['actual']['path'];before=ident(BASE,p);after=ident(C,p);check('baseline B07 output equals own previous actual '+p,before['sha256']==x['actual']['sha256']);same=before['sha256']==after['sha256'];owner.append({'path':p,'baseline':before,'candidate':after,'whole_byte_identical':same})
 check('B07 owner output preserved '+p,same or p.endswith('test-catalog/pokemon-rules-wp31-32-37-38.md'))
rowchecks=[]
previous19=js(OLD,oldP+'B07-conclusion-dispositions.json')
for x in previous19['records']:
 for row in x['static_rows_current_exact']:
  p=row['path'];id=row['static_id'];pattern=re.compile(r'^\|\s*'+re.escape(id)+r'\s*\|');lhs=[(n+1,l) for n,l in enumerate(blob(BASE,p).decode().splitlines()) if pattern.match(l)];rhs=[(n+1,l) for n,l in enumerate(blob(C,p).decode().splitlines()) if pattern.match(l)]
  check('accepted B07 row '+x['id']+':'+id,[l for n,l in lhs]==[l for n,l in rhs] and len(rhs)==row['ordered_occurrences'])
  rowchecks.append({'finding':x['id'],'path':p,'id':id,'baseline_lines':[n for n,l in lhs],'candidate_lines':[n for n,l in rhs],'sha256':sha(('\n'.join(l for n,l in rhs)).encode()),'byte_identical':True})
catchecks=[]
for lock in js(C,P+'whole-catalog-lock-check.json')['locks']:
 p=lock['path'];a=blob(BASE,p);b=blob(C,p)
 if 'pokemon-rules' in p:before=a.split('## CP：'.encode())[0];after=b.split('## CP：'.encode())[0]
 else:before=a.split('## W：'.encode(),1)[1];after=b.split('## W：'.encode(),1)[1]
 check('catalog whole protected region '+p,before==after)
 check('catalog protected hash/bytes '+p,sha(after)==lock['protected_sha256'] and len(after)==lock['protected_bytes'])
 ids=lambda data:re.findall(r'^\|\s*([A-Z]+-?\d+[a-z]?)\s*\|',data.decode(),re.M)
 oldids=ids(a);newids=ids(b);new=set(newids)-set(oldids)
 check('catalog old order/multiplicity '+p,[id for id in newids if id in set(oldids)]==oldids)
 check('catalog exactly new IDs '+p,new==set(lock['new_ids']));check('catalog all IDs unique '+p,len(newids)==len(set(newids)))
 catchecks.append({'path':p,'protected_bytes':len(after),'protected_sha256':sha(after),'byte_identical':True,'before_ids':len(oldids),'after_ids':len(newids),'new_ids':[i for i in newids if i in new]})
req=js(C,P+'affected-B07-review-request.json');verify(req['fixed_acceptance']['identity'],label='accepted B07 exact manifest');deps=js(C,P+'semantic-dependency-log.json')
for x in req['changed_readers']:
 verify(x['before'],BASE,x['path'],'affected-before');verify(x['after'],C,x['path'],'affected-after')
for group in [req['untouched_owner_clauses'],deps['untouched_owner_consumer_clauses']]:
 for x in group:
  p=x['path'];t=x.get('text',x.get('after_text'));check('protected consumer clause bytes '+p,t in blob(BASE,p).decode() and t in blob(C,p).decode());check('protected consumer supplied identical flag '+p,x['byte_identical'] is True)
dump('B07-preservation.json',{'owner_outputs14':owner,'whole_unchanged13':sum(x['whole_byte_identical'] for x in owner),'accepted_rows':rowchecks,'catalogs':catchecks,'19_complete_conclusions_rechecked_for_preservation':True,'fresh_semantic_review_is_bounded_to_changed_dependencies':True,'previous_own_report':ident(OLD,oldP+'report.md')})
# Nonbehavioral trace coverage and static-only semantics.
check('73 declared final clause changes traced',len(js(C,P+'formal-change-log.json')['changes'])==73)
cases=js(C,P+'static-cases.json')
check('43 linked catalog rows +18 supplemental static designs',len(cases['catalog_cases'])==43 and len(cases['supplemental_designs'])==18)
for r in cases['catalog_cases']:
 data=blob(C,r['path']).decode().splitlines();check('case row exact trace '+r['id'],r['id'] in data[r['line']-1]);check('static case unexecuted '+r['id'],r['executed'] is False)
for r in cases['supplemental_designs']:check('supplemental design unexecuted '+r['id'],r['executed'] is False)
check('no B14 authorization from review',env['B14_formal_authorization'] is False and env['independent_approval'] is False)
check('four affected batch gates',scope['required_independent_affected_batches']==['B04','B05','B07','B08'])
limits=js(C,P+'source-limits.json');check('configuration remains UNVERIFIED PlanA',limits['configuration']['effective_model_reasoning_speed']=='UNVERIFIED' and limits['configuration']['Plan_A_accepted'] is True)
check('unknown gates retained',set(limits['contract_source_limits']['retained_source_limits'])=={'U01–U10','G01–G12','AX01–AX20'})
report={'kind':'INDEPENDENT_GIT_JSON_HASH_SPEC_TEXT_BOOKKEEPING_ONLY','candidate':C,'baseline':BASE,'checks_count':len(checks),'failed_count':sum(not x['pass'] for x in checks),'checks':checks,'reference_execution':0,'behavior_vectors_executed':0,'runtime_observations':0,'proven_Demo_chains':0,'author_programs_executed':0}
dump('git-text-audit-results.json',report)
print(json.dumps({'checks':len(checks),'failures':[x for x in checks if not x['pass']],'complete_paths':len(ch),'normative_paths':len(paths)},ensure_ascii=False))
