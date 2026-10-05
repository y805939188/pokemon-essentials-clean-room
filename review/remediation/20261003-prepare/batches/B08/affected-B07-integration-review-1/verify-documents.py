#!/usr/bin/env python3
"""Independent Git/text/JSON bookkeeping only; no reference or author program runs."""
import subprocess,json,pathlib,hashlib,csv,io,re,collections,functools,datetime
ROOT=pathlib.Path(__file__).resolve().parents[6]
OUT=pathlib.Path(__file__).resolve().parent
A='49c21538e72b7a5873972cd00fcae1ee390cce64';C='0f35a393d9de467cd5f7e695b6072687bb582186';B='759eee80ce7856570fde2de12d5dcf98ce7e6017';P='e91c974c5a05a55da8d6cb228afe5b30174fb02c'
F='93e10babe0b9c9ef8b3f5277754541b447beeeb4';L='41fffb540c6483f5296ea0d33b789b75180d27ed'
REF=pathlib.Path('/workspace/reference-pokemon-essentials-B07');R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
I='review/remediation/20261003-prepare/batches/B08/integration-stage-1/'
OLD='review/remediation/20261003-prepare/batches/B08/affected-B07-review-round-1/'
checks=[]
def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args])
@functools.lru_cache(None)
def raw(c,p):return git('show',c+':'+p)
def sha(b):return hashlib.sha256(b).hexdigest()
def cj(d):return sha(json.dumps(d,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def data(c,p):return json.loads(raw(c,p))
def ident(c,p):
 b=raw(c,p);return {'commit':c,'path':p,'git_blob':git('rev-parse',c+':'+p).decode().strip(),'sha256':sha(b),'bytes':len(b)}
def check(n,ok,details=None):checks.append({'check':n,'pass':bool(ok),**({'details':details} if details is not None else {})})
def save(n,d): (OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def statuses(b,a):return [{'change':s.split('\t')[0],'path':s.split('\t')[1]} for s in git('diff','--no-ext-diff','--no-renames','--name-status',b,a).decode().splitlines()]
DOPT=['--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3']
def diff(b,a,paths=None):return git('diff',*DOPT,b,a,*(['--',*paths] if paths else []))
meta={n:data(A,I+n) for n in ['integration-manifest.json','diff-and-freeze.json','input-inspection.json','scope-counts.json','finding-registration.json','scope-and-observation-registration.json','merge-and-dependency-impact.json','downstream-handshake.json']}
m=meta['integration-manifest.json'];freeze=meta['diff-and-freeze.json'];h=meta['downstream-handshake.json'];dep=data('7fd9271bc77b534e0eba5b47c77034e2453dd560',OLD+'dependency-and-preservation.json')
check('actual parent',git('show','-s','--format=%P',A).decode().strip()==P)
check('actual tree',git('rev-parse',A+'^{tree}').decode().strip()=='6312cddce2e2a43841bde5ec19d0bb480c284314')
check('reference exact',subprocess.check_output(['git','-C',str(REF),'rev-parse','HEAD']).decode().strip()==R)
check('reference clean',subprocess.check_output(['git','-C',str(REF),'status','--porcelain'])==b'')
fullpaths=m['source_identities'];formal=[x['candidate']['path'] for x in m['formal_candidate_identities']];pub=[x['path'] for x in m['current_public_paths']];ip=git('ls-tree','-r','--name-only',A,'--',I).decode().splitlines()
check('independent counts12/45/51/10/13',(len(formal),len(meta['input-inspection.json']['author_paths']),sum(len(v) for v in meta['input-inspection.json']['report_paths'].values()),len(pub),len(ip))==(12,45,51,10,13))
sb=statuses(B,A);sc=statuses(C,A);sp=statuses(P,A)
check('predecessor actual complete131 exact sets',len(sb)==131 and {x['path'] for x in sb}=={x['path'] for x in fullpaths}|set(pub)|set(ip))
reportpaths={p for v in meta['input-inspection.json']['report_paths'].values() for p in v}
check('candidate actual complete74 exact sets',len(sc)==74 and {x['path'] for x in sc}==reportpaths|set(pub)|set(ip))
check('final three additions',sp==[{'change':'A','path':p} for p in sorted(freeze['final_actual_changed_paths'])])
allids=[]
for x in fullpaths:
 z=ident(x['commit'],x['path']);a=ident(A,x['path']);check('source imported exact '+x['path'],all(z[k]==x[k] for k in ['git_blob','sha256','bytes']) and all(a[k]==z[k] for k in ['git_blob','sha256','bytes']));allids.append({'fixed_source':z,'actual':a})
for p in formal:check('formal actual candidate byte identity '+p,raw(A,p)==raw(C,p))
for merge in m['normal_merges']:
 check('ordinary merge parents '+merge['commit'],git('show','-s','--format=%P',merge['commit']).decode().split()==merge['parents'])
 check('ordinary merge tree '+merge['commit'],git('rev-parse',merge['commit']+'^{tree}').decode().strip()==merge['tree'])
check('public payload only exact ten M ten A',statuses(freeze['payload_parent'],P)==sorted([{'change':'M','path':p} for p in pub]+[{'change':'A','path':p} for p in m['new_payload_paths']],key=lambda x:x['path']))
# Recursive identity audit is independent of author check booleans. Only complete explicit identities audited here.
seen=set();identity_checks=[]
def walk(d,loc):
 if isinstance(d,dict):
  if all(k in d for k in ['path','git_blob','sha256','bytes']) and ('commit' in d or 'binding' in d):
   c=d.get('commit') or A;p=d['path'];key=(c,p,d['git_blob'],d['sha256'],d['bytes'])
   if key not in seen:
    seen.add(key)
    try:z=ident(c,p);ok=all(z[k]==d[k] for k in ['git_blob','sha256','bytes'])
    except subprocess.CalledProcessError:ok=False;z=None
    check('registered identity '+loc,ok);identity_checks.append({'locator':loc,'declared':d,'recomputed':z,'pass':ok})
  for k,v in d.items():
   if k!='checks':walk(v,loc+'/'+k)
 elif isinstance(d,list):
  for i,v in enumerate(d):walk(v,loc+'/'+str(i))
for n,d in meta.items():walk(d,n)
for r in csv.DictReader(io.StringIO(raw(A,I+'current-hashes.tsv').decode()),delimiter='\t'):
 z=ident(r['commit'] or A,r['path']);check('current-hashes.tsv '+r['path'],z['git_blob']==r['git_blob'] and z['sha256']==r['sha256'] and z['bytes']==int(r['bytes']))
# Every original/accepted control hash, full root and extension object stays immutable.
original={v['id']:v for v in data(F,'review/global-independent-review/2026-10-03-fd82a639/findings.json')};acc=data(L,'review/remediation-20261003-prepare/finding-acceptance.json')
control=data('7fd9271bc77b534e0eba5b47c77034e2453dd560',OLD+'fixed-control-bindings.json');cases=data('7fd9271bc77b534e0eba5b47c77034e2453dd560',OLD+'B07-conclusion-dispositions.json')
for r in control['records']:
 check('B07 full original '+r['id'],cj(original[r['id']])==r['original_complete_object_sha256'])
 check('B07 full acceptance '+r['id'],cj(acc[r['id']])==r['acceptance_complete_object_sha256'])
 check('B07 qualifications/root/extensions '+r['id'],r['current_qualifications']==original[r['id']].get('current_qualifications') and r['effective_case_constraints']==original[r['id']].get('effective_case_constraints') and r['root_adjudications']==original[r['id']].get('root_adjudications') and r['all_extensions_controls']==[{k:v for k,v in x.items() if k!='extension'} for x in (original[r['id']].get('extensions') or [])])
 for row in next(v for v in cases['records'] if v['id']==r['id'])['static_rows_current_exact']:
  lines=raw(A,row['path']).decode().splitlines();found=[(i+1,s) for i,s in enumerate(lines) if s.startswith('| '+row['static_id']+' |')]
  check('B07 fixed row '+r['id']+'/'+row['static_id'],len(found)==row['ordered_occurrences'] and all(sha(s.encode())==row['row_sha256'] for i,s in found));row['actual_lines']=[i for i,s in found];row['actual_commit']=A
for r in meta['finding-registration.json']['dispositions']:
 check('B08 complete original embedded '+r['id'],r['complete_original_object']==original[r['id']] and cj(original[r['id']])==r['original_complete_object_sha256'])
 check('B08 complete acceptance embedded '+r['id'],r['complete_approved_acceptance']==acc[r['id']] and cj(acc[r['id']])==r['acceptance_object_sha256'])
 check('B08 current qualification/root/extension '+r['id'],r['current_qualifications']==original[r['id']].get('current_qualifications') and r['effective_case_constraints']==original[r['id']].get('effective_case_constraints') and r['root_adjudications']==original[r['id']].get('root_adjudications') and r['all_extensions']==(original[r['id']].get('extensions') or []))
 check('B08 no actual or C promotion '+r['id'],r['canonical_state']=='OPEN' and not r['canonical_closure'] and not r['canonical_edited'] and r['parent_C_acceptance']=='NOT_PERFORMED' and r['actual_R08']=='PENDING_ULTRA' and r['actual_affected_R07']=='PENDING_SEPARATE_ULTRA' and r['actual_affected_R04']=='PENDING_SEPARATE_BOUNDED_ULTRA')
# Fixed input versions and previous accepted scopes.
for r in h['B09']['complete20_fixed_controls']:
 check('B09 full20 original/acceptance '+r['id'],r['complete_original_object']==original[r['id']] and r['complete_approved_acceptance']==acc[r['id']] and cj(original[r['id']])==r['original_complete_object_sha256'] and cj(acc[r['id']])==r['acceptance_object_sha256'] and not r['canonical_closure'] and r['canonical_state']=='OPEN')
preserved={}
for k in ['five_changed_reverse_readers','unchanged_B07_consumers13','accepted_B07_outputs14','immutable_actual_reports37','B04_byte_preserved_outputs13','all79_planned_input_refreeze']:
 z=[]
 for r in dep[k]:
  p=r['before']['path'];external=r['before']['commit'] if r['before']['commit']!=B else None;a=ident(external or A,p);b=ident(external or B,p);c=ident(external or C,p);z.append({'before':b,'candidate':c,'actual':a,'changed_from_predecessor':a['sha256']!=b['sha256']})
  check('actual rebind '+k+'/'+p,a['sha256']==c['sha256'] if p not in pub else True)
  if k in ['unchanged_B07_consumers13','immutable_actual_reports37','B04_byte_preserved_outputs13']:check('predecessor preservation '+k+'/'+p,a['sha256']==b['sha256'])
 preserved[k]=z
for p in [v['before']['path'] for v in h['WP34_bodies']]:
 check('WP34 whole unchanged '+p,raw(A,p)==raw(B,p))
# Catalog ordered rows and protected complete sections, independently extracted.
cat=[]; protected=0
for r in dep['catalog_preservation']:
 p=r['path'];old=raw(B,p).decode();new=raw(A,p).decode()
 rows=lambda t:[s for s in t.splitlines() if re.match(r'^\| [A-Z]+-?\d+[a-z]? \|',s)]
 ro,rn=rows(old),rows(new);oldids=[s.split('|')[1].strip() for s in ro];newids=[s.split('|')[1].strip() for s in rn];changed=[]
 check('catalog ordered occurrence preservation '+p,[x for x in newids if x in oldids]==oldids)
 for s in ro:
  i=s.split('|')[1].strip();ns=[v for v in rn if v.split('|')[1].strip()==i]
  if ns!=[s]:changed.append(i)
 newonly=[i for i in newids if i not in oldids];check('catalog counts/new/old changes '+p,len(ro)==r['before_rows'] and len(rn)==r['after_rows'] and changed==r['old_changed_ids'] and newonly==r['new_ids'])
 for sec in r['protected_sections']:
  # Same complete source span as the previous own independently extracted section, additionally candidate=actual.
  headings=list(re.finditer(r'^## .*$',old,re.M)); span=None
  for i,hd in enumerate(headings):
   segment=old[hd.start():headings[i+1].start() if i+1<len(headings) else len(old)]
   if re.search(r'^\| '+sec['section']+r'-?\d',segment,re.M):span=segment;break
  check('protected whole section '+p+'/'+sec['section'],span is not None and span in new)
  protected+=1
 cat.append({'path':p,'old_count':len(ro),'actual_count':len(rn),'changed_old_ids':changed,'new_static_ids':newonly,'protected_sections':r['protected_sections']})
check('14 protected sections',protected==14)
# Append-only TSV history; decode nested JSON and compare all new rows against full registration controls.
registrations=[];reg={r['id']:r for r in meta['finding-registration.json']['dispositions']}
for n in ['approval-ledger.tsv','traceability-successor.tsv']:
 p='review/remediation/20261003-prepare/'+n;before=raw(B,p);after=raw(A,p);br=list(csv.DictReader(io.StringIO(before.decode()),delimiter='\t'));ar=list(csv.DictReader(io.StringIO(after.decode()),delimiter='\t'))
 check('old133 TSV raw prefix preserved '+n,after.startswith(before) and len(br)==133 and len(ar)==150 and ar[:133]==br)
 new=ar[133:];check('17 unique B08 TSV rows '+n,len(new)==17 and len({r['finding_id'] for r in new})==17 and {r['finding_id'] for r in new}==set(reg))
 for row in new:
  r=reg[row['finding_id']];ob=json.loads(row['remaining_obligations']);check('TSV three actual/C gate '+n+'/'+r['id'],row['canonical_state']=='OPEN' and row['candidate_commit']==C and row['candidate_review_commit']=='239a29c466d6efc1a5a240f57ad53b55c91f9e42' and ob['candidate_reports']==m['candidate_reports'] and ob['actual_R08']=='PENDING_ULTRA' and ob['actual_affected_R07']=='PENDING_SEPARATE_ULTRA' and ob['actual_affected_R04']=='PENDING_SEPARATE_BOUNDED_ULTRA' and ob['parent_C']=='NOT_PERFORMED' and not ob['canonical_closure'] and ob['all_contributors']==r['all_contributor_batches'] and ob['other_batch_obligations']==r['other_batch_obligations'])
  if n=='traceability-successor.tsv':
   inp=json.loads(row['current_clause_inputs']);check('TSV clause/formal/full-control identity '+r['id'],inp['locator']==r['formal_clause_locator'] and inp['formal_candidate_identities']==r['formal_candidate_identities'] and row['static_test_ids_not_executed']==r['static_locator']);check('TSV original priority '+r['id'],row['original_report_commit']==F and row['effective_priority']==r['priority'])
 registrations.append({'path':p,'before':ident(B,p),'actual':ident(A,p),'old_raw_bytes_preserved':after.startswith(before),'added_rows':new})
# Complete frozen plan, B09, versions and dependency locks.
batches={r['id']:r for r in data(L,'review/remediation-20261003-prepare/batches.json')};b9=h['B09']
check('B09 complete62 reads and7 writes exact plan',len(b9['planned_reads'])==62 and [x['path'] for x in b9['planned_reads']]==batches['B09']['read_paths'] and b9['allowed_formal_write_paths']==batches['B09']['write_paths'] and len(b9['allowed_write_input_identities'])==7)
check('B09 complete20/13 controls exact plan',len(b9['complete20_fixed_controls'])==20 and b9['primary_finding_ids']==batches['B09']['primary_finding_ids'])
check('B09 gate no dispatch/original permission',not b9['accepted'] and not b9['task_dispatched'] and not b9['original_specs_write_authorized'] and h['parallel_writers_authorized']==0 and h['downstream_tasks_dispatched']==0 and h['B04_actual_pending'])
check('79 B08 planned exact inputs',len(h['B08_effective_read_versions'])==79 and [r['path'] for r in h['B08_effective_read_versions']]==batches['B08']['read_paths'])
# Accepted statistics and public history remain exact predecessor objects.
scope=meta['scope-counts.json'];st=scope['prior_accepted_statistics_identity'];oldstats=data(B,st['path'])
check('prior accepted complete statistics JSON unchanged',scope['prior_accepted_statistics_preserved']==oldstats and raw(A,st['path'])==raw(B,st['path']))
check('B08 exact17/9 plan roles',list(reg)==batches['B08']['contribution_finding_ids'] and [r['id'] for r in reg.values() if r['B08_primary']]==batches['B08']['primary_finding_ids'] and sum(r['B08_primary'] for r in reg.values())==9)
check('B09 exact20 controls plan roles',[r['id'] for r in b9['complete20_fixed_controls']]==batches['B09']['contribution_finding_ids'] and [r['id'] for r in b9['complete20_fixed_controls'] if r['primary']]==batches['B09']['primary_finding_ids'])
for p in pub:
 if p.endswith('.tsv'):continue
 text=diff(B,A,[p]).decode();deleted=[x for x in text.splitlines() if x.startswith('-') and not x.startswith('--- ')]
 check('public historical text no unrelated deletion '+p,len(deleted)==(3 if p=='deliverables/final-specification-set/test-catalog/README.md' else 0))
# Literal authorised patch result equality, not a new patch application.
auth=meta['scope-and-observation-registration.json'];patchp=auth['literal_authorized_patch']['path'];patch=raw(A,patchp);originalpaths=[x['path'] for x in auth['original_sync_request_preserved']['paths']]
actual_original_diff=git('diff','--no-ext-diff','--no-renames','--binary','--full-index',B,A,'--',*originalpaths)
check('literal authorised patch identity',sha(patch)=='05b75bcafcb1fd9359e9a35e935e8b7cbb7dd038a0f3349a1172d1fe3ba88f25')
# In-memory project-document text hunk validation; no file application, executable loading or behavior simulation.
hunk_results=[];chunks=re.split(r'(?m)^--- a/',patch.decode())[1:]
for chunk in chunks:
 lines=chunk.splitlines(keepends=True);p=lines[0].strip();before=raw(B,p).decode().splitlines(keepends=True);result=[];cursor=0; i=2;hc=0
 while i<len(lines):
  mt=re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i]);assert mt,(p,i,lines[i]);start=int(mt[1])-1;oldcnt=int(mt[2] or 1);newcnt=int(mt[4] or 1);assert start>=cursor
  result.extend(before[cursor:start]);cursor=start;consumed=0;written=0;i+=1
  while i<len(lines) and not lines[i].startswith('@@ '):
   ln=lines[i];assert ln[0] in ' +-';v=ln[1:]
   if i+1<len(lines) and lines[i+1].startswith('\\ No newline'):v=v.rstrip('\n');i+=1
   if ln[0] in ' -':assert before[cursor]==v,(p,cursor);cursor+=1;consumed+=1
   if ln[0] in ' +':result.append(v);written+=1
   i+=1
  assert (consumed,written)==(oldcnt,newcnt),(p,consumed,written,oldcnt,newcnt);hc+=1
 result.extend(before[cursor:]);b=''.join(result).encode();ok=b==raw(A,p);check('literal authorised hunk result '+p,ok);hunk_results.append({'path':p,'hunks':hc,'before':ident(B,p),'actual':ident(A,p),'literal_hunk_result_sha256':sha(b),'all_context_lines_matched':True,'exact_actual_result':ok})
check('literal patch exact four paths',sorted(x['path'] for x in hunk_results)==sorted(originalpaths))
save('original-patch-hunk-proof.json',{'patch':ident(A,patchp),'operation':'In-memory project text hunk/identity comparison only; did not apply/write originals','four_results':hunk_results,'historical_order':'AUTHOR_SELF_REPORT_ONLY'})
for r in auth['parent_authorization_record_preserved']['original_scope_authorization']['authorized_four_path_clauses']:
 check('four original before/result '+r['path'],all(ident(B,r['path'])[k]==r['before'][k] for k in ['git_blob','sha256','bytes']) and all(ident(A,r['path'])[k]==r['expected_after'][k] for k in ['git_blob','sha256','bytes']))
# Payload patches are exact and incomplete for actual; compute both unfiltered actual differences independently.
diffs=[]
for b,tag in [(B,'predecessor-to-actual'),(C,'candidate-to-actual')]:
 z=diff(b,A);path=pathlib.Path('/tmp/b08-r07-'+tag+'.diff');path.write_bytes(z)
 diffs.append({'base':b,'actual':A,'options':DOPT,'selected_paths':None,'sha256':sha(z),'bytes':len(z),'complete_path_statuses':statuses(b,A),'storage':'Locally recomputed unfiltered full Git diff; regenerable from fixed Git objects. Large duplicate patch bodies are not recopied into this report.'})
for r in freeze['full_patches']:
 check('payload patch literal exact '+r['path'],raw(A,r['path'])==diff(r['base_commit'],r['target_commit']) and sha(raw(A,r['path']))==r['sha256'])
(OUT/'complete-formal.diff').write_bytes(diff(B,A,formal));(OUT/'complete-public.diff').write_bytes(diff(B,A,pub))
whitespace=[]
for base,target,tag,paths in [(B,C,'historical_candidate',None),(B,A,'actual_full',None),(B,A,'actual_formal12',formal)]:
 run=subprocess.run(['git','-C',str(ROOT),'diff','--no-ext-diff','--no-renames','--check',base,target,*(['--',*paths] if paths else [])],capture_output=True)
 lines=run.stdout.decode().splitlines();diagnostics=[s for s in lines if re.match(r'.*:\d+: (trailing whitespace\.|new blank line at EOF\.)$',s)]
 whitespace.append({'tag':tag,'base':base,'target':target,'exit_code':run.returncode,'diagnostics':len(diagnostics),'trailing_whitespace':sum(s.endswith('trailing whitespace.') for s in diagnostics),'new_blank_EOF':sum(s.endswith('new blank line at EOF.') for s in diagnostics),'diagnostic_paths':sorted({s.rsplit(':',2)[0] for s in diagnostics}),'raw_output_sha256':sha(run.stdout)})
check('historical N01 exact353=344+9',whitespace[0]['diagnostics']==353 and whitespace[0]['trailing_whitespace']==344 and whitespace[0]['new_blank_EOF']==9)
check('actual formal12 whitespace pass',whitespace[2]['exit_code']==0)
save('complete-diff-identities.json',{'actual':A,'actual_tree':git('rev-parse',A+'^{tree}').decode().strip(),'candidate':C,'predecessor':B,'payload':P,'complete_diffs':diffs,'final_three_additions':sp,'source108_identities':allids,'formal12_actual':[ident(A,p) for p in formal],'public10_actual':[ident(A,p) for p in pub],'integration13_actual':[ident(A,p) for p in ip]})
save('registered-identity-audit.json',{'unique_complete_identities':len(identity_checks),'checks':identity_checks})
save('dependency-and-preservation.json',{'actual':A,'candidate':C,'predecessor':B,**preserved,'catalogs':cat,'B09':{'planned_read_count':62,'formal_write_count':7,'contributions':20,'primary':13,'blocked':True,'original_write_permission':False,'whole_locks':b9['whole_catalog_locks'],'reverse_readers':b9['future_B09_to_B08_reverse_readers'],'semantic_callers':b9['semantic_callers']}})
save('public-registration-checks.json',{'actual':A,'registrations':registrations,'B08_accepted':0,'prior_accepted':133,'total_candidate_and_accepted':150,'canonical_closures':0})
save('fixed-control-bindings.json',control)
save('B07-case-rebind.json',cases)
save('whitespace-scope.json',{'results':whitespace,'historical_reports_preserved':True,'canonical_new_finding':False,'N01_scope':'353 concerns only predecessor-to-candidate; actual full measured separately; saved patch contexts preserved'})
save('independent-document-checks.json',{'actual':A,'operation':'Own Git/text/JSON checks only, not behavioral tests','checks':checks,'check_count':len(checks),'passed':sum(x['pass'] for x in checks),'failed':[x for x in checks if not x['pass']]})
print(json.dumps({'checks':len(checks),'failed':[x for x in checks if not x['pass']],'unique_metadata_identities':len(identity_checks),'diffs':[{k:v for k,v in x.items() if k!='complete_path_statuses'} for x in diffs],'whitespace':whitespace},ensure_ascii=False,indent=2))
