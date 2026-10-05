import subprocess,json,hashlib,pathlib,re,collections,csv,io,functools
R=pathlib.Path('/workspace/pokemon-essentials-clean-room');T=pathlib.Path('/tmp/b08-b04-actual')
X='49c21538e72b7a5873972cd00fcae1ee390cce64';B='759eee80ce7856570fde2de12d5dcf98ce7e6017';C='0f35a393d9de467cd5f7e695b6072687bb582186';W='d6367692610c83fd24bd1ab8d2ab0cfa6757314d'
F='93e10babe0b9c9ef8b3f5277754541b447beeeb4';P='41fffb540c6483f5296ea0d33b789b75180d27ed';Q='7fd9271bc77b534e0eba5b47c77034e2453dd560';O='ceb6c07340c8f4f2b7c508df36b2a2ef98f12711';V='239a29c466d6efc1a5a240f57ad53b55c91f9e42'
M1='d68eece866631713fe205345be3d93f1e48cbfa9';M2='3a1852d08f854122e4ff36e0a9b810aa331004d2';M3='7d1463f088201a3efad56dadee9a86bb0a923934';Y='e91c974c5a05a55da8d6cb228afe5b30174fb02c'
I='review/remediation/20261003-prepare/batches/B08/integration-stage-1/';H='review/remediation/20261003-prepare/batches/B07/acceptance-stage-1/downstream-handshake.json';A='review/remediation/20261003-prepare/batches/B08/author-stage-2/'
checks=[]
def git(*a,cwd=R):return subprocess.check_output(['git',*a],cwd=cwd)
@functools.lru_cache(None)
def read(c,p):return git('show',c+':'+p)
def obj(c,p):return json.loads(read(c,p))
def sha(b):return hashlib.sha256(b).hexdigest()
@functools.lru_cache(None)
def identity(c,p):
 b=read(c,p);return dict(commit=c,path=p,git_blob=git('rev-parse',c+':'+p).decode().strip(),sha256=sha(b),bytes=len(b))
def ck(n,v):
 checks.append(dict(check=n,pass_=bool(v)))
 if not v:raise AssertionError(n)
def same(a,b):return all(a[k]==b[k] for k in ['git_blob','sha256','bytes'])
def statuses(b,c):return [dict(change=s,path=p) for s,p in (x.split('\t') for x in git('diff','--no-renames','--name-status',b,c).decode().splitlines())]
def jsha(x):return sha(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
ck('HEAD is exact actual',git('rev-parse','HEAD').decode().strip()==X)
ck('initial worktree clean',git('status','--porcelain')==b'')
graph=[(X,[Y]),(Y,[M3]),(M3,[M2,O]),(M2,[M1,Q]),(M1,[B,V]),(V,[C]),(Q,[C]),(O,[C]),(C,[W]),(W,[B])]
for c,parents in graph:ck('exact ordinary parents '+c,git('rev-list','--parents','-n','1',c).decode().split()==[c]+parents)
m=obj(X,I+'integration-manifest.json');df=obj(X,I+'diff-and-freeze.json');h=obj(X,I+'downstream-handshake.json');sc=obj(X,I+'scope-counts.json');fr=obj(X,I+'finding-registration.json');scope=obj(X,I+'scope-and-observation-registration.json');bh=obj(B,H)
formal=m['formal_candidate_identities'];source=m['source_identities'];pub=m['current_public_paths'];new=m['new_payload_paths'];last=m['final_evidence_paths']
fp={i['candidate']['path'] for i in formal};sp={i['path'] for i in source};pp={i['path'] for i in pub};np=set(new+last)
ck('exact independent formal/source/public/integration counts',len(fp)==12 and len(sp)==108 and len(pp)==10 and len(np)==13)
changesB=statuses(B,X);changesC=statuses(C,X)
expectedB={p:('M' if p in fp|pp else 'A') for p in sp|pp|np};expectedC={p:('M' if p in pp else 'A') for p in (sp-fp-{p for p in sp if '/author-stage-' in p})|pp|np}
ck('predecessor actual exact131 footprint',len(changesB)==131 and {x['path']:x['change'] for x in changesB}==expectedB)
ck('candidate actual exact74 footprint',len(changesC)==74 and {x['path']:x['change'] for x in changesC}==expectedC)
ck('final three are only actual commit delta',statuses(Y,X)==[dict(change='A',path=p) for p in sorted(last)])
ck('payload exact10 public M plus10 evidence A',{x['path']:x['change'] for x in statuses(M3,Y)}=={**{p:'M' for p in pp},**{p:'A' for p in new}})
outputs=[]
for a in formal:
 p=a['candidate']['path']
 for key in ['before','candidate','merged']:
  i=a[key];ck('formal frozen '+key+' '+p,same(identity(i['commit'],p),i))
 ck('formal actual unchanged reviewed bytes '+p,same(identity(X,p),a['candidate']) and same(identity(X,p),a['current']))
 outputs.append(dict(baseline=identity(B,p),candidate=identity(C,p),actual=identity(X,p)))
for a in source:ck('all108 incoming source preserved '+a['path'],same(identity(a['commit'],a['path']),a) and same(identity(X,a['path']),a))
for a in pub:ck('public actual hash '+a['path'],same(identity(X,a['path']),a))
for a in df['payload_public_and_management_identities']:ck('payload public-management exact actual '+a['path'],same(identity(Y,a['path']),a) and same(identity(X,a['path']),a))
for base,key,ch in [(B,'upstream_to_actual_contract',changesB),(C,'candidate_to_actual_contract',changesC)]:
 contract=df[key];ck('actual contract path count '+key,contract['base']==base and contract['expected_actual_path_count']==len(ch))
 ck('actual contract complete final paths '+key,{x['path']:x['change'] for x in contract['payload_path_statuses']}|{p:'A' for p in contract['final_added_paths']}=={x['path']:x['change'] for x in ch})
opts=['--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3'];diffs=[]
for base,n in [(B,'complete-predecessor-to-actual.diff'),(C,'complete-candidate-to-actual.diff')]:
 b=git('diff',*opts,base,X);ck('independently regenerated full actual diff '+n,(T/n).read_bytes()==b)
 diffs.append(dict(path=n,bytes=len(b),sha256=sha(b),command=['git','diff',*opts,base,X],paths=statuses(base,X)))
for a in df['full_patches']:
 b=git('diff',*a['git_diff_options'],a['base_commit'],a['target_commit']);ck('stored full payload patch exact '+a['path'],read(X,a['path'])==b and same(identity(X,a['path']),a) and a['target_commit']==Y)
 ck('stored patch footprint '+a['path'],a['complete_path_statuses']==statuses(a['base_commit'],Y))
ck('formal report file counts51',sum(1 for p in sp if '/author-stage-' not in p and p not in fp)==51)
ck('author evidence exactly45',sum('/author-stage-' in p for p in sp)==45)
rows=list(csv.DictReader(io.StringIO(read(X,I+'current-hashes.tsv').decode()),delimiter='\t'))
ck('current hashes exact118 source108 plus public10',len(rows)==118 and {x['path'] for x in rows}==sp|pp)
for a in rows:
 i=identity(X,a['path']);ck('current hashes row '+a['path'],i['git_blob']==a['git_blob'] and i['sha256']==a['sha256'] and i['bytes']==int(a['bytes']))
gir=obj(F,'review/global-independent-review/2026-10-03-fd82a639/findings.json');g={x['id']:x for x in gir};acc=obj(P,'review/remediation-20261003-prepare/finding-acceptance.json')
ids={x['id'] for x in fr['dispositions']};ck('fixed17 IDs9primary',len(ids)==17 and sum(x['B08_primary'] for x in fr['dispositions'])==9)
controlhashes=[]
def fixedcontrol(a,label):
 id=a['id'];ck(label+' original complete '+id,a['complete_original_object']==g[id]);ck(label+' acceptance complete '+id,a['complete_approved_acceptance']==acc[id]);ck(label+' original hash '+id,a['original_complete_object_sha256']==jsha(g[id]));ck(label+' acceptance hash '+id,a['acceptance_object_sha256']==jsha(acc[id]))
for a in fr['dispositions']:
 id=a['id'];fixedcontrol(a,'B08');z=g[id];y=acc[id]
 ck('current qualifications exact '+id,a['current_qualifications']==z['current_qualifications'])
 ck('all roots exact '+id,a['root_adjudications']==z.get('root_adjudications',[]));ck('all extensions exact '+id,a['all_extensions']==z.get('extensions',[]))
 for k in ['minimum_revision','determinate_recheck','acceptance_gate']:ck('acceptance detail '+k+' '+id,a[k]==y[k])
 ck('canonical OPEN untouched '+id,a['canonical_state']=='OPEN' and a['canonical_edited'] is False and a['canonical_closure'] is False)
 ck('three actual pending/C not performed '+id,a['candidate']==C and a['candidate_report']==V and a['candidate_verdict']=='PASS_SCOPED' and a['actual_R08']=='PENDING_ULTRA' and a['actual_affected_R07']=='PENDING_SEPARATE_ULTRA' and a['actual_affected_R04']=='PENDING_SEPARATE_BOUNDED_ULTRA' and a['parent_C_acceptance']=='NOT_PERFORMED')
 for row in a['static_row_bindings_not_executed']:
  b=read(X,row['path']).splitlines(keepends=True)[row['line']-1];ck('static row actual byte binding '+id+' '+row['id'],sha(b)==row['sha256'] and len(b)==row['bytes'] and row['status']=='STATIC_DESIGN_NOT_EXECUTED')
 controlhashes.append(dict(id=id,original_sha256=jsha(z),acceptance_sha256=jsha(y),all_qualifications_roots_extensions_preserved=True,semantic_scope='Two B04 caller groups only; other controls identity-preserved'))
public=[]
for p in sorted(pp):
 old=read(B,p);cur=read(X,p);rec=dict(before=identity(B,p),actual=identity(X,p))
 if p.endswith('.tsv'):
  ck('public TSV old bytes exact prefix '+p,cur.startswith(old));oldrows=list(csv.DictReader(io.StringIO(old.decode()),delimiter='\t'));newrows=list(csv.DictReader(io.StringIO(cur.decode()),delimiter='\t'));tail=newrows[len(oldrows):]
  ck('public TSV133+17=150 '+p,len(oldrows)==133 and len(newrows)==150 and {x['finding_id'] for x in tail}==ids)
  for row in tail:
   id=row['finding_id'];a=next(a for a in fr['dispositions'] if a['id']==id);ck('public row candidate binding '+p+' '+id,row['canonical_state']=='OPEN' and row['candidate_commit']==C and row['candidate_review_commit']==V)
   obligations=json.loads(row['remaining_obligations']);ck('public row actual and C pending '+id,obligations['parent_C']=='NOT_PERFORMED' and obligations['actual_affected_R04']=='PENDING_SEPARATE_BOUNDED_ULTRA' and obligations['actual_affected_R07']=='PENDING_SEPARATE_ULTRA' and obligations['actual_R08']=='PENDING_ULTRA' and obligations['canonical_closure'] is False)
   ck('public remaining responsibilities exact '+id,obligations['all_contributors']==a['all_contributor_batches'] and obligations['other_batch_obligations']==a['other_batch_obligations'] and obligations['candidate_reports']==m['candidate_reports'])
   if p.endswith('approval-ledger.tsv'):
    ck('approval candidate PASS only '+id,row['candidate_verdict']=='PASS_SCOPED' and row['integration_verdict']=='NOT_REVIEWED_PENDING_THREE_ULTRA' and row['downstream_gate']=='BLOCKED')
   else:
    q=json.loads(row['current_clause_inputs']);ck('trace reviewed identities exact '+id,q['reviewed_candidate']==C and q['formal_candidate_identities']==[x['candidate'] for x in formal] and q['formal_candidate_identities']==a['formal_candidate_identities'] and q['authorized_original_paths']==a['authorized_original_paths']);ck('trace PASS candidate only '+id,row['accepted_candidate_contribution']=='PASS_SCOPED_B08_CANDIDATE_ONLY' and 'PENDING_THREE' in row['integration_gate'])
  rec.update(old_rows=133,new_rows=150,appended_ids=sorted(ids),old_bytes_prefix_preserved=True)
 elif not p.endswith('test-catalog/README.md'):
  head,tail=old.split(b'\n',2)[:2],old.split(b'\n',2)[2]
  ck('public prose historical bytes exact '+p,cur.endswith(old) or (cur.split(b'\n',2)[:2]==head and cur.endswith(tail)));rec['historical_bytes_exact']=True
 else:
  expected=old.replace(b'BR01\xe2\x80\x93BR25',b'BR01\xe2\x80\x93BR26').replace(b'RM01\xe2\x80\x93RM32',b'RM01\xe2\x80\x93RM37').replace(b'EG01\xe2\x80\x93EG19\xe3\x80\x81EN01\xe2\x80\x93EN24',b'EG01\xe2\x80\x93EG20\xe3\x80\x81EN01\xe2\x80\x93EN32')
  ck('catalog README only3 current ranges and append',cur.startswith(expected));rec['only_three_range_updates_and_append']=True
 public.append(rec)
ck('old accepted statistics fixed identity',same(identity(B,sc['prior_accepted_statistics_identity']['path']),sc['prior_accepted_statistics_identity']))
ck('old accepted statistics entire object exact',sc['prior_accepted_statistics_preserved']==obj(B,sc['prior_accepted_statistics_identity']['path']))
stats=sc['prior_accepted_statistics_preserved']
ck('accepted133/118/87 specific87 strict79pending8 retained',stats['primary_denominator']==87 and stats['contribution_records']==133 and stats['distinct_touched_IDs']==118 and stats['strict_all_planned_contribution_counts']=={'all_contributor_batches_accepted':79,'pending':8} and stats['specific_revision_counts']=={'satisfied_scoped':87,'missing_specific_consumer':0,'insufficient_evidence':0})
auth=obj(C,A+'parent-authorization-and-preapply.json')['original_scope_authorization'];app=obj(C,A+'original-application.json');op=auth['patch_identity']['path']
ck('v2 authorized patch exact31346',read(X,op)==read(C,op) and len(read(X,op))==31346 and sha(read(X,op))=='05b75bcafcb1fd9359e9a35e935e8b7cbb7dd038a0f3349a1172d1fe3ba88f25')
for a in auth['authorized_four_path_clauses']:
 p=a['path'];ck('four original precise authorized result '+p,same(identity(B,p),a['before']) and same(identity(W,p),a['before']) and same(identity(X,p),a['expected_after']) and read(C,p)==read(X,p))
ck('4 original footprint no scope expansion',len(auth['authorized_four_path_clauses'])==4 and {x['path'] for x in auth['authorized_four_path_clauses']}=={p for p in fp if p.startswith('specs/')})
ck('B04 two caller gate exact R07 object',h['B04_two_caller_gate_preserved']==obj(Q,'review/remediation/20261003-prepare/batches/B08/affected-B07-review-round-1/B04-affected-gate.json'))
ck('B04 actual scope preserves own full candidate object',h['B04_actual_scope_preserved']==obj(O,'review/remediation/20261003-prepare/batches/B08/affected-B04-review-round-1/affected-boundaries.json'))
ck('B04 candidate receipt frozen SHA',h['B04_current_candidate_receipt']['commit']==O and same(identity(O,h['B04_current_candidate_receipt']['entry']),h['B04_current_candidate_receipt']['entry_identity']))
ck('B04 actual pending and downstream0',h['B04_actual_pending'] is True and h['downstream_tasks_dispatched']==0 and h['parallel_writers_authorized']==0 and m['parent_C_acceptance'] is False and m['accepted_B08_contributions']==0)
ck('residual other owners exact predecessor',h['existing_other_owner_residuals']==bh['existing_other_owner_residuals'])
ck('all79 B08 inputs refrozen',len(h['B08_effective_read_versions'])==79)
input_versions=[]
for a in h['B08_effective_read_versions']:
 p=a['path'];old=a['author_input'];ck('planned79 author input '+p,same(identity(old['commit'],p),old))
 cur=a['current_actual_input'];c=cur.get('commit',X);ck('planned79 effective actual input '+p,same(identity(c,p),cur))
 input_versions.append(dict(path=p,author_input=old,effective_input=identity(c,p),changed_since_candidate=(read(C,p)!=read(c,p)) if a.get('candidate_version',{}).get('commit')==C else 'FIXED_CONTROL'))
b9=h['B09'];ck('B09 still blocked/unauthorized',b9['accepted'] is False and b9['task_dispatched'] is False and b9['original_specs_write_authorized'] is False and b9['planned_dependencies']==['B06','B07','B08'])
ck('B09 62read7write20contrib13primary',len(b9['planned_reads'])==62 and len(b9['allowed_write_input_identities'])==7 and len(b9['complete20_fixed_controls'])==20 and sum(x['primary'] for x in b9['complete20_fixed_controls'])==13)
for a in b9['complete20_fixed_controls']:fixedcontrol(a,'B09 planned integrity only')
for a in h['fixed_plan_identities']:ck('all fixed plan files '+a['path'],same(identity(P,a['path']),a))
plans={x['id']:x for x in obj(P,'review/remediation-20261003-prepare/batches.json')}
ck('B08 current79 exact fixed planned path set',{x['path'] for x in h['B08_effective_read_versions']}==set(plans['B08']['read_paths']))
ck('B09 exact fixed62 reads7 writes20 IDs13primary',{x['path'] for x in b9['planned_reads']}==set(plans['B09']['read_paths']) and set(b9['allowed_formal_write_paths'])==set(plans['B09']['write_paths']) and {x['id'] for x in b9['complete20_fixed_controls']}==set(plans['B09']['contribution_finding_ids']) and set(b9['primary_finding_ids'])==set(plans['B09']['primary_finding_ids']))
for a in h['downstream_batches']:
 p=plans[a['batch']];ck('downstream fixed plan and gate '+a['batch'],a['planned_dependencies']==p['dependencies'] and a['planned_read_count']==len(p['read_paths']) and a['planned_write_count']==len(p['write_paths']) and 'NOT_DISPATCHED' in a['status'] and 'three actual passes and parent C' in a['future_freeze'])
ck('all13 actual integration identities independently frozen',len(np)==13)
integration_ids=[identity(X,p) for p in sorted(np)]
limits=scope['source_limits'];ownprior=obj(O,'review/remediation/20261003-prepare/batches/B08/affected-B04-review-round-1/source-reading-log.json')
ck('own named unread limitations preserved verbatim',limits['R04_named_limits']==ownprior['named_retained_limits'] and limits['R04_unread_named_content']==ownprior['unread_named_content'])
for a in limits['inherited_limits_preserved_verbatim']:
 i=a['identity'];j=obj(i['commit'],i['path']);ck('inherited full limits field preservation '+i['commit'],all(j[k]==v for k,v in a['limits'].items()))
ck('U G AX and0runtime/vector/demo preserved',limits['retained_source_limits']==['U01–U10','G01–G12','AX01–AX20'] and all(limits[k]==0 for k in ['reference_program_execution','compiler_execution','converter_execution','generator_execution','deserializer_execution','author_reviewer_program_execution','behavior_vectors_executed','runtime_observations','proven_Demo_chains']))
ck('config UNVERIFIED PlanA no probes preserved',scope['configuration']['effective_model_reasoning_speed']=='UNVERIFIED' and scope['configuration']['Plan_A_accepted'] is True and scope['configuration']['review_requested_reasoning']=='Ultra' and scope['configuration']['quota_probes']==0 and scope['configuration']['configuration_probes']==0)
seen=set()
def audit_effective(v,where):
 if isinstance(v,dict):
  if all(k in v for k in ['path','git_blob','sha256','bytes']) and isinstance(v['path'],str):
   c=v.get('commit',X)
   if re.fullmatch('[0-9a-f]{40}',str(c)):
    key=(c,v['path'],v['git_blob'],v['sha256'],v['bytes'])
    if key not in seen:ck('recursive frozen identity '+where+' '+v['path'],same(identity(c,v['path']),v));seen.add(key)
  for k,a in v.items():audit_effective(a,where+'/'+str(k))
 elif isinstance(v,list):
  for i,a in enumerate(v):audit_effective(a,where+'/'+str(i))
audit_effective(h,'handshake')
hist=obj(B,'review/remediation/20261003-prepare/batches/B04/integration-stage-1/integration-manifest.json');preserved=[]
for a in hist['formal_candidate_identities']:
 p=a['candidate']['path'];ck('B04 all13 actual unchanged '+p,read(B,p)==read(X,p));preserved.append(dict(baseline=identity(B,p),actual=identity(X,p)))
guards=[]
for p in git('ls-tree','-r','--name-only',B).decode().splitlines():
 if p.startswith(('deliverables/final-specification-set/','specs/')) and re.search(r'/wp(24|28|30|34)[-.]',p):
  ck('WP24/28/30/34 bodies exact preserved '+p,read(B,p)==read(X,p));guards.append(dict(baseline=identity(B,p),actual=identity(X,p)))
ws=subprocess.run(['git','diff','--check',B,C],cwd=R,capture_output=True);diagnostics=[l for l in ws.stdout.decode().splitlines() if re.search(r':(?:\d+): (trailing whitespace\.|new blank line at EOF\.)$',l)]
ck('bounded N01 independently3533449',ws.returncode==2 and len(diagnostics)==353 and sum(l.endswith('trailing whitespace.') for l in diagnostics)==344 and sum(l.endswith('new blank line at EOF.') for l in diagnostics)==9)
paths={re.sub(r':\d+:.*','',l) for l in diagnostics};ck('bounded N01 exact13 saved diff paths',paths==set(df['bounded_R_B08_N01']['diagnostic_paths']) and all('/author-stage-' in p and p.endswith(('.diff','.patch')) for p in paths))
rp='/tmp/rb04-reference';rc=git('rev-parse','HEAD',cwd=rp).decode().strip();rt=git('rev-parse','HEAD^{tree}',cwd=rp).decode().strip();origin=git('remote','get-url','origin',cwd=rp).decode().strip()
ck('real isolated reference commit/tree/origin/clean',rc=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' and rt=='7589c800b61ba13a13040ed0d686979b80a84fd0' and git('cat-file','-t','HEAD',cwd=rp)==b'commit\n' and origin=='https://github.com/Maruno17/pokemon-essentials.git' and git('status','--porcelain',cwd=rp)==b'')
res=dict(actual=X,actual_tree=git('rev-parse',X+'^{tree}').decode().strip(),baseline=B,candidate=C,graph=[dict(commit=c,parents=p) for c,p in graph],checks=checks,all_checks_pass=True,changes_predecessor_actual=changesB,changes_candidate_actual=changesC,formal12=outputs,source108=source,public10=public,integration13=integration_ids,diffs=diffs,full17_controls_identity_only=controlhashes,planned79=input_versions,B04_outputs13=preserved,WP24_28_30_34_bodies=guards,prior_accepted_statistics_identity=sc['prior_accepted_statistics_identity'],original_patch=identity(X,op),original_temporal_order='AUTHOR_SELF_REPORT_ONLY',N01=dict(base=B,candidate=C,total=353,trailing_space=344,new_blank_at_EOF=9,paths=sorted(paths),not_actual_total=True,canonical_registration=False),reference=dict(commit=rc,tree=rt,origin=origin,path=rp,read_only=True),scope='Actual merge/input/public integrity; business verdict restricted to two B04 caller groups',reference_execution=0,behavior_vectors_executed=0,runtime_observations=0,proven_demo_chains=0)
(T/'independent-input-validation.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),all_pass=True,actual_tree=res['actual_tree'],public10=len(public),source108=len(source),recursive_handshake_identities=len(seen),planned79_changed=sum(x['changed_since_candidate'] is True for x in input_versions)),ensure_ascii=False))
