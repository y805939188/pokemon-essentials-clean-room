#!/usr/bin/env python3
"""Fresh ACT review: Git/JSON/hash/text metadata only; no historical programs."""
import subprocess,hashlib,json,pathlib,csv,io,collections,re,functools
ROOT='review/remediation/20261003-prepare'
B=ROOT+'/batches/B13'
ACT='d81562bfe0e79ca4df3233ada38fa09e800bdafc'
CAND='db9e6ed1997efe5bf94dac952aad44fd3b9ebd21'
BASE='8e67f780c204d593d89f364f585d2c6c2fe74631'
ADMIN='231c9f25df4dd64961fb9290ff52302782a9fdb8'
PACK='996e4f04bcc34b992c9cc4d25db9548850266a06'
PRIOR='2570ca6dc893cc6bfb1320ef9f2513b5618f6a26'
OUT=pathlib.Path(B+'/affected-actual-review-1/B02')
OUT.mkdir(parents=True,exist_ok=True)
def git(*a):return subprocess.check_output(['git',*a])
@functools.lru_cache(maxsize=None)
def data(c,p):return git('show',c+':'+p)
def obj(c,p):return json.loads(data(c,p))
def sha(b):return hashlib.sha256(b).hexdigest()
def tree(c):
 out={}
 for rec in git('ls-tree','-r','-z',c).split(b'\0'):
  if not rec:continue
  left,p=rec.split(b'\t',1);mode,typ,blob=left.decode().split();out[p.decode()]=(mode,typ,blob)
 return out
T={c:tree(c) for c in [BASE,CAND,ADMIN,ACT,PACK]}
@functools.lru_cache(maxsize=None)
def ident(c,p):
 b=data(c,p);return {'commit':c,'path':p,'git_blob':T[c][p][2] if c in T else git('rev-parse',c+':'+p).decode().strip(),'sha256':sha(b),'bytes':len(b)}
checks=[]
def require(ok,msg):
 if not ok:raise AssertionError(msg)
 checks.append(msg)
def binding(b,also_ACT=False):
 c,p=b['commit'],b['path'];v=ident(c,p)
 require(all(v[k]==b[k] for k in ['git_blob','sha256','bytes']), 'exact binding '+c+':'+p)
 if also_ACT:
  a=ident(ACT,p);require(all(a[k]==v[k] for k in ['git_blob','sha256','bytes']),'ACT exact copy '+p)
 if 'mode' in b:
  mode=(T[c] if c in T else tree(c))[p][0];require(mode==b['mode'],'source mode '+p)
  if also_ACT:require(T[ACT][p][0]==mode,'ACT mode '+p)
 return v
D=obj(PACK,B+'/actual-freeze-1/affected-actual-review-dispatch.json')
require(D['reviewed_actual_commit']==ACT and D['candidate_commit']==CAND and D['formal_accepted_predecessor']==BASE and D['administrative_predecessor']==ADMIN,'dispatch exact identities')
ids={c:{'commit':c,'tree':git('rev-parse',c+'^{tree}').decode().strip(),'parents':git('show','-s','--format=%P',c).decode().strip().split()} for c in T}
require(ids[ACT]['tree']=='ae6ca9bd055f6feca3657db7bd511b2be682d897','ACT exact tree')
require(ids[CAND]['tree']=='d7e8953fb0f3eff949c3dbee1f9361b0b8f71804','candidate exact tree')
require(ids[PACK]['parents']==[ACT],'packet is report-only direct successor')
F=obj(ACT,B+'/integration-stage-1/formal-copy-identities.json');require(len(F['records'])==11 and F['output_count']==11,'eleven formal output records')
formal=[]
for r in F['records']:
 binding(r['frozen_candidate'],True);binding(r['predecessor']);require(T[CAND][r['path']]==T[ACT][r['path']],'formal bytes and modes equal candidate '+r['path']);formal.append({'path':r['path'],'BASE':ident(BASE,r['path']),'candidate':ident(CAND,r['path']),'ACT':ident(ACT,r['path'])})
formalpaths={r['path'] for r in formal}
public={ROOT+'/'+p for p in ['approval-ledger.tsv','traceability-successor.tsv','final-integration-review.md']}
require(len([p for p in formalpaths if p.startswith('deliverables/')])==7 and len([p for p in formalpaths if p.startswith('specs/')])==4,'seven final and four permitted originals')
def changes(a,b):
 records=git('diff','--no-ext-diff','--no-textconv','--name-status','-z',a,b).split(b'\0');result=[];i=0
 while i<len(records) and records[i]:
  status=records[i].decode();p=records[i+1].decode();i+=2
  require(status in ['A','M'],'no rename/delete/type change '+a+' '+status+' '+p)
  result.append({'status':status,'path':p})
 return result
streams=[]
for s in D['complete_unfiltered_differences']:
 require(s['command']==['git','diff','--no-ext-diff','--no-textconv','--binary','--full-index',s['from'],ACT] and s['path_filter'] is None,'prescribed complete stream '+s['name'])
 raw=subprocess.check_output(s['command']);published=data(PACK,s['published_patch_path'])
 require(raw==published and sha(raw)==s['sha256'] and len(raw)==s['bytes'],'entire stream bytes/hash '+s['name'])
 require(T[PACK][s['published_patch_path']][2]==s['git_blob'],'entire stream Git blob '+s['name'])
 ch=changes(s['from'],ACT);require(len(ch)==s['changed_path_count'],'entire path count '+s['name'])
 for r in ch:
  p=r['path'];r['class']='formal_11' if p in formalpaths else 'public_registration_3' if p in public else 'management_review_evidence'
  if r['class']=='management_review_evidence':require(r['status']=='A' and p.startswith(ROOT+'/batches/'),'nonformal/public stream paths are new batch metadata '+p)
 require({r['path'] for r in ch if r['status']=='M'}==(formalpaths|public if s['from']==BASE else public),'complete modified path boundary '+s['name'])
 streams.append({**s,'independently_regenerated':True,'entire_bytes_equal_packet':True,'all_changed_paths':ch,'classification_counts':dict(collections.Counter(r['class'] for r in ch))})
protect={}
for c,allowed in [(BASE,formalpaths|public),(CAND,public),(ADMIN,formalpaths|public)]:
 changed=[p for p,v in T[c].items() if p not in allowed and T[ACT].get(p)!=v]
 require(not changed,'all predecessor existing paths modes/blobs protected '+c)
 protect[c]={'existing_path_count':len(T[c]),'allowed_existing_changed_paths':sorted(allowed),'all_other_existing_paths_exact':True,'unexpected_changes':changed}
pkch=changes(ACT,PACK);require(all(r['status']=='A' and r['path'].startswith(B+'/actual-freeze-1/') for r in pkch),'packet only adds actual-freeze reports')
C=obj(ACT,B+'/integration-stage-1/published-artifact-copies.json');require(C['copy_count']==153 and len(C['records'])==153,'all153 evidence copies')
copies=[binding(r,True) for r in C['records']]
require(sum('/affected-candidate-review-2/' in r['path'] for r in copies)==30,'all30 prior independent affected reports copied')
S=obj(ACT,B+'/integration-stage-1/original-scope-application.json');grants={k:binding(S[k]) for k in ['scope1','scope2']}
scope=[]
for r in S['records']:
 binding(r['formal_base_before']);binding(r['candidate_to_copy'],True);binding(r['scope1_exact_after'])
 target=r['scope2_after'] or r['scope1_exact_after']
 if r['scope2_after']:binding(r['scope2_after'])
 require(all(target[k]==r['candidate_to_copy'][k] for k in ['git_blob','sha256','bytes']),'permitted scope1/scope2 endpoint exact '+r['path'])
 scope.append(r)
require(len(scope)==4 and S['B027_original_extension'] is False and S['B030_increment']==0 and S['new_scope_amendment_by_G'] is False,'scope does not broaden B027/B030 or become quality gate')
P=obj(ACT,B+'/integration-stage-1/accepted-result-preservation.json')
# Freeze complete stats without reading its historical report dependencies.
statbind=P['latest_accepted_statistics'] if 'latest_accepted_statistics' in P else next(v for v in P.values() if isinstance(v,dict) and v.get('path','').endswith('completion-statistics-successor.json'))
binding(statbind,True);ST=obj(ACT,statbind['path'])
require(ST['contribution_records']==232 and len(ST['accepted_contribution_receipts'])==232 and len(ST['accepted_batches'])==14,'all232 qualified accepted receipts and14 batches')
require(ST['canonical_OPEN']==229 and ST['canonical_CLOSED']==0 and ST['formal_closures']==0 and ST['global_gate_passed'] is False,'canonical229 remain open')
priorAudit=obj(PRIOR,B+'/affected-candidate-review-2/B02/shared-incremental-audit.json')
priorAuditID=ident(PRIOR,B+'/affected-candidate-review-2/B02/shared-incremental-audit.json');binding(priorAuditID,True)
ownerrows=[]
for o in D['owners']:
 binding(o['frozen_candidate_result'],True);binding(o['actual_copy_of_candidate_result'])
 prior=obj(PRIOR,o['frozen_candidate_result']['path']);require(prior['reviewed_candidate']==CAND and prior['reviewed_tree']==ids[CAND]['tree'] and prior['verdict']==o['candidate_verdict_at_NEW_only'],'prior result exact reviewed NEW '+o['gate'])
 interfaces=[]
 for r in o['current_interface_bindings']['current_inputs']:
  binding(r['reviewed_NEW'],True);interfaces.append({'candidate':r['reviewed_NEW'],'ACT':ident(ACT,r['reviewed_NEW']['path']),'byte_and_mode_equal':T[CAND][r['reviewed_NEW']['path']]==T[ACT][r['reviewed_NEW']['path']]})
 extras=[]
 for r in o['additional_current_interfaces']:
  binding(r['identity_NEW'],True);extras.append({'candidate':r['identity_NEW'],'ACT':ident(ACT,r['identity_NEW']['path'])})
 for receipt in o['accepted_boundary_receipts_from_latest_B12_C']:require(receipt in ST['accepted_contribution_receipts'],'qualified accepted receipt fully retained '+o['gate']+' '+receipt['id'])
 binding(o['all_qualified_accepted_receipts_available_at'],True)
 ownerrows.append({'owner':o['gate'],'finite_scope':o['finite_scope'],'prior_result':o['frozen_candidate_result'],'prior_verdict_at_NEW_only':prior['verdict'],'interface_bindings':interfaces,'additional_interfaces':extras,'qualified_accepted_boundary_receipts':o['accepted_boundary_receipts_from_latest_B12_C']})
require(len(ownerrows)==11,'eleven potential owners individually bound')
G=obj(ACT,B+'/integration-stage-1/candidate-gate-receipts.json')
require(G['candidate']==CAND and G['candidate_tree']==ids[CAND]['tree'] and G['formal_FIX_BASE']==BASE and G['actual_verdict'] is None and G['C'] is False,'candidate gate does not stand for actual or C')
for k in ['findings','coverage','report','validation']:binding(G['FULL'][k],True)
find=obj(ACT,G['FULL']['findings']['path']);require(not find.get('findings',[]) and G['FULL']['verdict']=='PASS' and G['FULL']['contributions']==8 and G['FULL']['primary']==5 and G['FULL']['outputs']==11,'FULL candidate8/5/11 receipt exact only')
R=obj(ACT,B+'/integration-stage-1/finding-registration.json');require(len(R['records'])==8 and R['complete_control_count']==8 and R['primary']==5 and R['shared']==3 and R['actual_receipts'] is None and R['new_B13_accepted_contributions']==0 and R['canonical_CLOSED_increment']==0,'eight pending records no accepted B13/C closure')
controls=obj(CAND,B+'/author-draft-1/original-and-acceptance-controls.json')['controls'];require(len(controls)==8,'eight complete approved controls')
reg=[]
for r,c in zip(R['records'],controls):
 require(r['id']==c['id'] and r['canonical_state']=='OPEN' and r['current_status']=='CANDIDATE_LOCAL_PASS_INTEGRATED_PENDING_ALL_EXACT_ACTUAL_GATES','current pending control '+r['id'])
 binding(r['complete_qualified_control_binding'],True)
 require(r['complete_current_control_fields']==c['complete_current_control_fields'] and r['complete_minimum_acceptance_fields']==c['whole_approved_acceptance_object'],'whole current/root/extension/minimum fields exact '+r['id'])
 for k in ['whole_original_object_sha256','whole_acceptance_object_sha256','whole_original_object_binding','whole_approved_acceptance_binding']:require(r[k]==c[k],'frozen whole-object qualifier '+r['id']+' '+k)
 accepted=[batch for batch in r['all_contributors'] if any(z['batch']==batch and z['id']==r['id'] for z in ST['accepted_contribution_receipts'])]
 require(accepted==r['accepted_contributors'] and [x for x in r['all_contributors'] if x not in accepted]==r['remaining_contributors'],'accepted/remaining computed from exact232 receipts '+r['id'])
 require(r['all_contributors']==c['all_contributor_batches'],'all contributor boundary retained '+r['id'])
 require(r['accepted_B13_contributions']==0 and r['final_closure'] is False and r['actual_full_and_affected_receipts'] is None,'no actual signature/closure synthesized '+r['id'])
 binding(r['local_author_output'],True);binding(r['candidate_FULL_record'],True)
 reg.append({'id':r['id'],'primary':r['primary'],'all_contributors':r['all_contributors'],'accepted_contributors':accepted,'remaining_contributors':r['remaining_contributors'],'whole_current_and_minimum_fields_exact':True,'root_extensions_and_qualifiers_retained':True,'local_author_output':r['local_author_output'],'candidate_FULL_record':r['candidate_FULL_record'],'actual_receipts':None,'canonical_state':'OPEN','accepted_B13_contributions':0})
publiccheck=[]
for p in sorted(public):
 old=data(BASE,p);new=data(ACT,p);require(data(CAND,p)==old and data(ADMIN,p)==old,'public frozen accepted predecessor bytes '+p)
 if p.endswith('.tsv'):
  require(new.startswith(old),'all old232 raw public records byte-exact prefix '+p)
  rows=list(csv.DictReader(io.StringIO(new.decode()),delimiter='\t'));oldrows=list(csv.DictReader(io.StringIO(old.decode()),delimiter='\t'));added=rows[len(oldrows):]
  require(len(oldrows)==232 and len(rows)==240 and len(added)==8,'public232+8 rows '+p)
  require([r['finding_id'] for r in added]==[r['id'] for r in R['records']],'all eight ordered pending IDs '+p)
  for row in added:
   require(row['canonical_state']=='OPEN' and row['candidate_commit']==CAND,'public current identity/open '+row['finding_id'])
   if p.endswith('approval-ledger.tsv'):
    require(row['reviewed_integration_commit']=='EXTERNAL_ACTUAL_SHA_PENDING' and not row['integration_review_commit'] and row['integration_disposition']=='PENDING_EXACT_ACTUAL; CANONICAL_OPEN','approval row no false actual signature '+row['finding_id'])
   else:
    require(row['integration_gate']=='PENDING_EXACT_ACTUAL;CANONICAL_OPEN' or 'PENDING' in row['integration_gate'],'traceability pending gate '+row['finding_id'])
  publiccheck.append({'path':p,'before':ident(BASE,p),'ACT':ident(ACT,p),'old232_raw_prefix_exact':True,'old_rows':len(oldrows),'physical_rows':len(rows),'new8_rows':added})
 else:
  require(new.endswith(old),'prior final integration review whole body byte-exact suffix')
  publiccheck.append({'path':p,'before':ident(BASE,p),'ACT':ident(ACT,p),'old_whole_body_suffix_exact':True,'new_prefix':new[:-len(old)].decode()})
ledger=ROOT+'/finding-ledger.tsv';require(T[BASE][ledger]==T[ACT][ledger],'canonical finding ledger entire blob/mode preserved')
LR=list(csv.DictReader(io.StringIO(data(ACT,ledger).decode()),delimiter='\t'));require(collections.Counter(x['canonical_state'] for x in LR)=={'OPEN':229},'canonical ledger independently229 OPEN0 CLOSED')
L=obj(ACT,B+'/integration-stage-1/source-limits.json')
for v in L.values():
 if isinstance(v,dict) and all(k in v for k in ['commit','path','git_blob','sha256','bytes']):binding(v,True)
readback=obj(PACK,B+'/actual-freeze-1/G-publication-readback.json');require(readback['actual_commit']==ACT and readback['actual_tree']==ids[ACT]['tree'] and len(readback['identities'])==179,'G frozen readback179 exact target')
for r in readback['identities']:
 v=ident(ACT,r['path']);require(all(v[k]==r[k] for k in ['git_blob','sha256','bytes']),'G179 independent ACT byte readback '+r['path'])
require({r['path'] for r in changes(ADMIN,ACT)}=={r['path'] for r in readback['identities']},'G179 coverage exactly all admin-toACT paths')
# Independent scoped protection, granted sequence, and public embedded objects.
permission_checks=[]
grantobjects={k:obj(S[k]['commit'],S[k]['path']) for k in ['scope1','scope2']}
require(grantobjects['scope1']['status']=='GRANTED_EXACT_FIXED_PATCH_SCOPE_ONLY' and grantobjects['scope1']['quality_PASS'] is None and grantobjects['scope2']['quality_PASS'] is None,'both grants are exact scope only with no quality PASS')
for k,grant in grantobjects.items():
 for q in grant['records']:
  binding(q['before']);binding(q['after_to_apply']);require(q['write_authorized'] is True,'exact original write authorized '+q['path'])
  applied=next(x for x in S['records'] if x['path']==q['path'])
  target=applied['scope1_exact_after'] if k=='scope1' else applied['scope2_after']
  require(all(q['after_to_apply'][x]==target[x] for x in ['git_blob','sha256','bytes']),'actual endpoint equals grant record '+k+' '+q['path'])
  before=applied['formal_base_before'] if k=='scope1' else applied['scope1_exact_after']
  require(all(q['before'][x]==before[x] for x in ['git_blob','sha256','bytes']),'grant sequence before bytes exact '+k+' '+q['path'])
  permission_checks.append({'grant':k,'path':q['path'],'before':q['before'],'granted_after':q['after_to_apply'],'scope_only':True})
wp58='specs/combat/wp58-battle-recording-and-playback.md'
old58=data(grantobjects['scope2']['records'][0]['before']['commit'],wp58)
new58=data(ACT,wp58)
def section52parts(b):
 a=b.index('### 5.2'.encode());z=b.index('### 5.3'.encode(),a);return b[:a],b[a:z],b[z:]
oldparts=section52parts(old58);newparts=section52parts(new58)
require(oldparts[0]==newparts[0] and oldparts[2]==newparts[2],'WP58 scope2 outside section5.2 byte-exact')
creature='deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md'
def creature_rows(c):
 return [(m.group(1).decode(),m.group(2).decode(),m.group(0).decode()) for m in re.finditer(rb'^\| (EG|EN|FC|MG|TT)-(\d+) \|.*$',data(c,creature),re.M)]
br=creature_rows(BASE);ar=creature_rows(ACT)
require([(x[0],x[1]) for x in br]==[(x[0],x[1]) for x in ar] and len(br)==125,'all125 creature ID order and multiplicity retained')
rowchanges=[{'series':x[0],'id':x[1],'before':x[2],'ACT':y[2]} for x,y in zip(br,ar) if x[2]!=y[2]]
require(len(rowchanges)==1 and rowchanges[0]['series']=='FC' and rowchanges[0]['id']=='10','creature only FC10 text changed')
require(collections.Counter(x[0] for x in ar)=={'EG':20,'EN':32,'FC':17,'MG':32,'TT':24},'creature finite family counts retained')
family_protection={'BASE':ident(BASE,creature),'ACT':ident(ACT,creature),'counts':dict(collections.Counter(x[0] for x in ar)),'order_and_multiplicity_exact':True,'unchanged_rows':124,'unchanged_other_owner_rows':108,'changed_rows':rowchanges}
for o in ownerrows:
 o['qualified_all_owner_accepted_receipts']=[x for x in ST['accepted_contribution_receipts'] if x['batch']==o['owner']]
 for item in o['interface_bindings']:
  p=item['ACT']['path'];item['BASE']=ident(BASE,p);item['BASE_to_ACT_byte_and_mode_equal']=T[BASE][p]==T[ACT][p]
 o['prior_original_finite_result']=ident('4a75ca146e10062e469a42a9610bc3026861a34c',B+'/affected-candidate-review-1/'+o['owner']+'/result.json')
for p in sorted(public):
 if not p.endswith('.tsv'):continue
 rows=list(csv.DictReader(io.StringIO(data(ACT,p).decode()),delimiter='\t'))[-8:]
 for i,(row,r) in enumerate(zip(rows,R['records'])):
  qualifier=json.loads(row['remaining_obligations'])
  for k in ['all_contributors','accepted_contributors','remaining_contributors']:require(qualifier[k]==r[k],'public embedded complete contributor qualification '+r['id']+' '+k)
  locator=B+'/integration-stage-1/finding-registration.json#/records/'+str(i)
  require(qualifier['complete_control']==locator and qualifier['canonical_final_closure']=='NOT_PERFORMED' and qualifier['candidate_affected_report']==PRIOR and qualifier['candidate_FULL_report']==G['report_commits']['FULL'],'public pending gate and complete current control pointer '+r['id'])
  if p.endswith('traceability-successor.tsv'):
   inputs=json.loads(row['current_clause_inputs']);require(inputs['complete_control']==locator and inputs['candidate']==CAND and row['public_successor_application']==locator and json.loads(row['remaining_batches'])==r['remaining_contributors'],'trace current inputs/control/remaining exact '+r['id'])
A={'role':'INDEPENDENT_AFFECTED_ACTUAL_SHARED_METADATA_CHECK','reviewed_actual':ACT,'reviewed_actual_tree':ids[ACT]['tree'],'candidate':CAND,'candidate_tree':ids[CAND]['tree'],'formal_accepted_predecessor':BASE,'administrative_predecessor':ADMIN,'dispatch_packet':PACK,'identities':ids,'complete_unfiltered_streams':streams,'all11_formal_output_identities':formal,'all_predecessor_path_protection':protect,'dispatch_packet_only_new_report_paths':pkch,'all153_evidence_copies_verified':copies,'all30_prior_affected_reports_exact':True,'scope_grant_bindings':grants,'all4_original_scope_sequence_checks':scope,'scope_permission_is_not_quality':True,'latest232_receipt_statistics':statbind,'accepted_batches':ST['accepted_batches'],'accepted_contributions':232,'all11_owner_interfaces_and_qualified_receipts':ownerrows,'candidate_FULL8_5_11_receipt_verified_without_signing_FULL':G['FULL'],'all8_pending_registration_control_checks':reg,'all3_public_delta_checks':publiccheck,'canonical_ledger':ident(ACT,ledger),'canonical_OPEN':229,'canonical_CLOSED':0,'prior_own_exact_candidate_audit':priorAuditID,'prior_catalog_checks_reused_after_entire_catalog_byte_equality':priorAudit['catalog_checks'],'all_G179_publication_identity_records_rechecked':True,'source_limits':L,'scope_grant_record_sequence_independently_rechecked':permission_checks,'WP58_scope2_outside_section52_exact':True,'independent_creature_family_protection':family_protection,'public_embedded_qualified_contributors_and_control_pointers_exact':True,'checks_count':len(checks),'metadata_check_result':'PASS','fresh_reference_reads':0,'runtime_or_behavior_vector_validation':False,'reference_Ruby_game_behavior_historical_program_execution':0,'new_tasks':0,'C':False,'B16_released':False,'B030_increment':0,'actual_owner_verdicts_must_be_separate':True}
(OUT/'shared-actual-audit.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':'PASS','checks':len(checks),'complete_streams':[{'name':s['name'],'bytes':s['bytes'],'sha256':s['sha256'],'paths':len(s['all_changed_paths']),'classes':s['classification_counts']} for s in streams],'outputs':len(formal),'copies':len(copies),'qualified_accepted_receipts':232,'new_pending':8,'owners':len(ownerrows)},ensure_ascii=False))
