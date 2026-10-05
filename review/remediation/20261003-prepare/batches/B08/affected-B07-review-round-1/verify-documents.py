"""Independent Git/JSON/text bookkeeping only; never imports or runs reference code."""
import collections,datetime,difflib,hashlib,json,pathlib,re,subprocess
ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT=ROOT/'review/remediation/20261003-prepare/batches/B08/affected-B07-review-round-1'
BASE='759eee80ce7856570fde2de12d5dcf98ce7e6017'
WIP='d6367692610c83fd24bd1ab8d2ab0cfa6757314d'
CAND='0f35a393d9de467cd5f7e695b6072687bb582186'
ORIG='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
checks=[]
def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args])
def raw(c,p):return git('show',c+':'+p)
def doc(c,p):return json.loads(raw(c,p))
def sha(b):return hashlib.sha256(b).hexdigest()
def objsha(o):return sha(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def identity(c,p):
 b=raw(c,p);return {'commit':c,'path':p,'git_blob':git('rev-parse',c+':'+p).decode().strip(),'sha256':sha(b),'bytes':len(b)}
def check(name,ok,details=None):checks.append({'check':name,'pass':bool(ok),'details':details})
def write(name,o):
 OUT.mkdir(parents=True,exist_ok=True)
 (OUT/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def pair(p):return {'before':identity(BASE,p),'after':identity(CAND,p),'changed':raw(BASE,p)!=raw(CAND,p)}
handpath='review/remediation/20261003-prepare/batches/B07/acceptance-stage-1/downstream-handshake.json'
h=doc(BASE,handpath)
formal=h['allowed_formal_write_paths']
originals=[r['original_path'] for r in h['potential_original_sync_contract4']]
check('candidate single parent',git('show','-s','--format=%P',CAND).decode().strip()==WIP)
check('WIP single parent is accepted B07-C',git('show','-s','--format=%P',WIP).decode().strip()==BASE)
check('active branch bound to candidate',git('rev-parse','HEAD').decode().strip()==CAND)
changes=[line.split('\t',1) for line in git('diff','--name-status',BASE,CAND).decode().splitlines()]
modified=[p for s,p in changes if s=='M'];added=[p for s,p in changes if s=='A']
check('complete unfiltered57-path delta',len(changes)==57 and len(modified)==12 and len(added)==45)
check('only8 authorized finals and4 exact authorized originals modified',set(modified)==set(formal+originals))
check('all45 additions batch-local author evidence',all(p.startswith('review/remediation/20261003-prepare/batches/B08/author-stage-') for p in added))
check('no delete/rename/extra status',all(s in ['A','M'] for s,p in changes))
all_delta=git('diff','--no-ext-diff','--binary','--full-index',BASE,CAND)
output_delta=git('diff','--no-ext-diff','--binary','--full-index',BASE,CAND,'--',*formal,*originals)
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'complete-predecessor-to-candidate.diff').write_bytes(all_delta)
(OUT/'complete-output.diff').write_bytes(output_delta)
manifest={'baseline':BASE,'WIP':WIP,'candidate':CAND,'candidate_tree':git('rev-parse',CAND+'^{tree}').decode().strip(),'paths':[{'status':s,'path':p,'before':None if s=='A' else identity(BASE,p),'after':identity(CAND,p)} for s,p in changes],'complete_diff':{'artifact':'complete-predecessor-to-candidate.diff','sha256':sha(all_delta),'bytes':len(all_delta)},'output_diff':{'artifact':'complete-output.diff','sha256':sha(output_delta),'bytes':len(output_delta)}}
write('complete-diff-identities.json',manifest)
planned=[]
for r in h['planned_reads']:
 p=r['path'];c=r.get('commit',BASE);b=identity(c,p);a=identity(c if c==ORIG else CAND,p)
 check('accepted planned input identity '+p,all(b[k]==r[k] for k in ['git_blob','sha256','bytes']))
 planned.append({'before':b,'current':a,'changed':b['sha256']!=a['sha256']})
check('all79 accepted planned inputs rebound',len(planned)==79)
check('ten planned paths changed at candidate',sum(r['changed'] for r in planned)==10)
ap='review/remediation/20261003-prepare/batches/B07/acceptance-stage-1/acceptance-manifest.json'
acc=doc(BASE,ap)
accepted14=[]
for r in acc['accepted_formal_identities']:
 p=r['path'];b=identity(BASE,p);check('accepted B07 baseline identity '+p,all(b[k]==r[k] for k in ['git_blob','sha256','bytes']));accepted14.append(pair(p))
check('B07 accepted14 changed onlytwo complete sharedcatalogs',len(accepted14)==14 and {r['after']['path'] for r in accepted14 if r['changed']}=={formal[4],formal[7]})
historical=[]
for r in acc['immutable37_actual_report_materials']:
 p=r['path'];check('all immutable B07 actual report '+p,raw(BASE,p)==raw(CAND,p));historical.append(pair(p))
check('all37 accepted actual reports immutable',len(historical)==37)
dep=doc(CAND,'review/remediation/20261003-prepare/batches/B08/author-stage-2/dependency-and-reverse-impact.json')
readers=[r['path'] for r in dep['five_mandatory_changed_reverse_readers']]
check('five exact reverse readers',set(readers)=={formal[2],*formal[4:]})
consumers=[]
for r in dep['unchanged_B07_domain_consumers']:
 p=r['path'];a=identity(CAND,p);b=identity(BASE,p)
 check('B07 consumer original and current identity '+p,a['sha256']==b['sha256'] and all(b[k]==r[k] for k in ['git_blob','sha256','bytes']))
 consumers.append(pair(p))
check('13 unchanged B07 body/original/WP24 consumers',len(consumers)==13)
b04path='review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/acceptance-manifest.json'
b04=doc(BASE,b04path);b04outputs=[]
for r in b04['accepted_formal_identities']:
 p=r['path'];q=pair(p);check('B04 frozen output identity '+p,not q['changed']);b04outputs.append(q)
check('B04 13 outputs byte-preserved (does not decide new caller gate)',len(b04outputs)==13)
check('WP34 final/original read-only preserved',all(raw(BASE,p)==raw(CAND,p) for p in ['deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md','specs/pokemon-rules/wp34-inheritance-and-offspring.md']))
catalogs=formal[4:]
allowed={'DC-08','EG-13','EN-01','EN-15','EN-16'}
catalog_audit=[]
for p in catalogs:
 old=raw(BASE,p).decode();new=raw(CAND,p).decode()
 def rows(t):return [(m.group(1),m.group(0)) for m in re.finditer(r'^\| ([A-Z]+-?\d+) \|.*$',t,re.M)]
 before=rows(old);after=rows(new);oldcounts=collections.Counter(k for k,v in before);aftercounts=collections.Counter(k for k,v in after)
 oldsequence=[k for k,v in before];retained=[k for k,v in after if k in oldcounts]
 check('catalog old ordered occurrences '+p,retained==oldsequence and all(aftercounts[k]==v for k,v in oldcounts.items()))
 afterold=iter([v for k,v in after if k in oldcounts]);changed_old=[]
 for k,v in before:
  a=next(afterold)
  if a!=v:changed_old.append(k)
 check('catalog old changes onlyassigned B08 premises '+p,set(changed_old)<=allowed)
 protected=[]
 pattern=r'^## ([A-Z]+)：.*$'
 def sections(t):
  ms=list(re.finditer(pattern,t,re.M));return {m.group(1):t[m.start():ms[i+1].start() if i+1<len(ms) else len(t)] for i,m in enumerate(ms)}
 a=sections(old);b=sections(new);owned={'DC','EG','EN','BR','RM'}
 for key in a:
  if key in owned:continue
  check('complete other-owner section byte preserved '+p+'#'+key,a[key]==b[key]);protected.append({'section':key,'sha256':sha(a[key].encode()),'bytes':len(a[key].encode()),'unchanged':a[key]==b[key]})
 catalog_audit.append({'path':p,'before_rows':len(before),'after_rows':len(after),'old_changed_ids':changed_old,'new_ids':[k for k,v in after if k not in oldcounts],'protected_sections':protected})
check('five old premise rows corrected, B0728 rows untouched',sum(len(r['old_changed_ids']) for r in catalog_audit)==5)
check('fifteen new B08 static rows only',sum(len(r['new_ids']) for r in catalog_audit)==15)
auth=doc(CAND,'review/remediation/20261003-prepare/batches/B08/author-stage-2/parent-authorization-and-preapply.json')['original_scope_authorization']
patchpath=auth['patch_identity']['path'];patch=raw(CAND,patchpath)
check('authorized v2 patch SHA256/bytes exact',sha(patch)==auth['patch_identity']['sha256']=='05b75bcafcb1fd9359e9a35e935e8b7cbb7dd038a0f3349a1172d1fe3ba88f25' and len(patch)==auth['patch_identity']['bytes'])
check('v2 prepared patch preserved from WIP',raw(WIP,patchpath)==patch)
orig_audit=[]
for r in auth['authorized_four_path_clauses']:
 p=r['path'];b=identity(BASE,p);a=identity(CAND,p)
 check('exact original before WIP/C '+p,raw(BASE,p)==raw(WIP,p) and all(b[k]==r['before'][k] for k in ['git_blob','sha256','bytes']))
 check('exact authorized original result '+p,all(a[k]==r['expected_after'][k] for k in ['git_blob','sha256','bytes']))
 orig_audit.append({'path':p,'before':b,'after':a,'authorized_clauses':r['clauses'],'assigned_ids':r['assigned_ids'],'order_limit':'AUTHOR_SELF_REPORT_ONLY; object hashes do not attest historical ordering'})
check('authorized original exactlyfour named paths',len(orig_audit)==4 and {r['path'] for r in orig_audit}==set(originals))
check('prepared unified patch has exactlyfour paths',set(re.findall(rb'^--- a/(.+)$',patch,re.M))=={p.encode() for p in originals} and set(re.findall(rb'^\+\+\+ b/(.+)$',patch,re.M))=={p.encode() for p in originals})
independent_prepared=''.join(''.join(difflib.unified_diff(raw(WIP,p).decode().splitlines(keepends=True),raw(CAND,p).decode().splitlines(keepends=True),fromfile='a/'+p,tofile='b/'+p)) for p in originals).encode()
check('independent four original text diffs exactly prepared patch',independent_prepared==patch)
origdiff=git('diff','--no-ext-diff',WIP,CAND,'--',*originals)
check('authorized originals WIPdiff exact candidate evidence',origdiff==raw(CAND,'review/remediation/20261003-prepare/batches/B08/author-stage-2/authorized-originals-WIP-to-candidate.diff'))
oldrecords=doc(BASE,'review/remediation/20261003-prepare/batches/B07/integration-review-1/finding-dispositions.json')['records']
findings=doc(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json');findings={r['id']:r for r in findings}
accept=doc(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
controls=[]
for r in oldrecords:
 id=r['id'];f=findings[id];a=accept[id]
 check('full original canonical object '+id,objsha(f)==r['original_complete_object_sha256'])
 check('full fixed acceptance object '+id,objsha(a)==r['approved_acceptance_object_sha256'])
 check('all adjudications/qualification unchanged '+id,r['root_adjudications']==f.get('root_adjudications',[]) and r['current_qualifications']==f.get('current_qualifications') and r['effective_case_constraints']==f.get('effective_case_constraints'))
 check('all finalized extension controls '+id,r['all_extensions_controls']==[{'report':e.get('report'),'raw_id':e.get('raw_id'),'adjudication':e.get('root_review',{}).get('decision'),'root_review':e.get('root_review')} for e in f.get('extensions',[])])
 controls.append({'id':id,'original_complete_object_sha256':objsha(f),'acceptance_complete_object_sha256':objsha(a),'original_git_locator':{'commit':ORIG,'path':'review/global-independent-review/2026-10-03-fd82a639/findings.json'},'acceptance_git_locator':{'commit':PLAN,'path':'review/remediation-20261003-prepare/finding-acceptance.json'},'current_qualifications':f.get('current_qualifications'),'effective_case_constraints':f.get('effective_case_constraints'),'root_adjudications':f.get('root_adjudications',[]),'all_extensions_controls':r['all_extensions_controls'],'raw_report_ids':[q.get('raw_id') for q in f.get('raw_reports',[])]})
check('all19 accepted conclusions including12 primary',len(controls)==19 and sum(r['B07_primary'] for r in oldrecords)==12)
shared=next(r for r in controls if r['id']=='GIR-FD82-C003');check('C0034 canonical roots and8 adjudicated extensions',len(shared['root_adjudications'])==4 and len(shared['all_extensions_controls'])==8)
check('canonical accepted receipts still229 OPEN0 CLOSED',acc['canonical_required_OPEN']==229 and acc['canonical_CLOSED']==0 and not acc['global_gate_passed'])
write('fixed-control-bindings.json',{'fixed_original':identity(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json'),'fixed_acceptance':identity(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json'),'records':controls,'complete19_original_object_hashes_verified':True,'C003_scope':'Full roots and8 extensions retained; B08 EN01/15/16 complement B07 A23/A31/A33, not canonical closure'})
write('dependency-and-preservation.json',{'baseline':BASE,'candidate':CAND,'accepted_handshake':identity(BASE,handpath),'all79_planned_input_refreeze':planned,'five_changed_reverse_readers':[pair(p) for p in readers],'unchanged_B07_consumers13':consumers,'accepted_B07_outputs14':accepted14,'immutable_actual_reports37':historical,'B04_byte_preserved_outputs13':b04outputs,'catalog_preservation':catalog_audit,'authorized_originals4':orig_audit,'original_patch_identity':identity(CAND,patchpath),'canonical_OPEN':229,'canonical_CLOSED':0,'public_metadata_changed':False,'B06_WP24_scope':'six logical requests plus intro memory only; no full partner/radar/BattleAudio approval','full_R_B08_review':'SEPARATE_PENDING_NOT_REPLACED','affected_actual_review':'SEPARATE_REQUIRED_AFTER_ORDINARY_INTEGRATION'})
write('independent-document-checks.json',{'phase':'BEFORE_AUTHOR_SELF_CHECK_COMPARISON','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':'own Git/hash/JSON/text checks only','checks':checks,'passed':sum(r['pass'] for r in checks),'failed':[r for r in checks if not r['pass']],'reference_execution':0,'behavior_vectors_executed':0})
print(json.dumps({'checks':len(checks),'passed':sum(r['pass'] for r in checks),'failed':[r for r in checks if not r['pass']],'diff_bytes':len(all_delta),'output_diff_bytes':len(output_delta),'catalogs':catalog_audit},ensure_ascii=False))
