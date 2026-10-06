"""New document, hash, row and Git-object checks. No inspected program execution."""
import subprocess,json,hashlib,csv,io,re
from read_documents import OUT,ACT,PRE,ORIG,PLAN,show
ROOT='review/remediation/20261003-prepare/batches/B14/integration-stage-1/'
C3='c06db6cd964188b3c693a9b7820e3a8aaffe0b04'
def doc(n):return json.loads(show(ACT,ROOT+n))
def identity(rev,p):
    b=show(rev,p)
    return {'commit':rev,'path':p,'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def bind(x,default=ACT):
    p=x['path'];rev=x.get('commit',default)
    if 'commit' not in x and p.startswith('review/global-independent-review/2026-10-03-fd82a639/'):rev=ORIG
    if 'commit' not in x and p.startswith('review/remediation-20261003-prepare/'):rev=PLAN
    actual=identity(rev,p)
    fields=[k for k in ['git_blob','sha256','bytes'] if k in x]
    return {'recorded_commit':x.get('commit'),'resolved_commit':rev,'path':p,'fields':fields,'match':all(actual[k]==x[k] for k in fields),'actual':actual}
result={'reviewed_actual':ACT,'mechanical_only':True}
copies=[]
for x in doc('copy-identities.json')['files']:
    source=bind(x);actual=identity(ACT,x['path']);copies.append({'path':x['path'],'source_commit':x['commit'],'binding':x['binding'],'source_record_match':source['match'],'actual_exact_copy':actual==dict(source['actual'],commit=ACT)})
result['copies']=copies
boundary=doc('boundary-and-bindings.json');changed=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--name-only',PRE,ACT,'--']).decode().splitlines()
allowed={x['path'] for x in copies}|set(boundary['public_paths'])
unexpected=[p for p in changed if p not in allowed and not p.startswith(ROOT)]
result['boundary']={'changed_paths':len(changed),'unexpected':unexpected,'copied_paths':len(copies),'new_G_records':len([p for p in changed if p.startswith(ROOT)]),'public_paths':boundary['public_paths'],'all_predecessor_paths_outside_explicit_changes_preserved':not unexpected}
hashrows=list(csv.DictReader(io.StringIO(show(ACT,ROOT+'current-hashes.tsv').decode()),delimiter='\t'))
for x in hashrows:x['bytes']=int(x['bytes'])
result['current_hashes']=[bind(x) for x in hashrows]
readers=doc('current-readers.json');planned=[]
for x in readers['planned']:
    planned.append({'index':x['planned_index'],'path':x['path'],'before':bind(x['before'],PRE),'current':bind(x['current']),'reading_not_proven_by_identity':True})
result['planned_readers']=planned
reg=doc('finding-registration.json');original=json.loads(show(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json'));original={x['id']:x for x in original}
accepted=json.loads(show(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json'))
qualified=[]
for x in reg['dispositions']:
    o=original[x['id']];a=accepted[x['id']]
    def matching_fields(projection,full):return isinstance(projection,dict) and all(k in full and full[k]==v for k,v in projection.items())
    qualified.append({'id':x['id'],'record_key':x['record_key'],'primary':x['primary'],'canonical_state':x['canonical_state'],'status':x['status'],'original_complete_hash_match':hashlib.sha256(json.dumps(o,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()==x['whole_original_object_sha256'],'acceptance_complete_hash_match':hashlib.sha256(json.dumps(a,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()==x['whole_acceptance_object_sha256'],'current_control_projection_matches':matching_fields(x['complete_current_control_fields'],o),'minimum_acceptance_projection_matches':matching_fields(x['complete_minimum_acceptance_fields'],a),'exact_candidate':x['exact_candidate'],'accepted_B14':x['accepted_B14_contribution'],'closure_authorized':x['closure_authorized']})
result['qualified_registrations']=qualified
public=[]
for name in ['approval-ledger.tsv','traceability-successor.tsv']:
    p='review/remediation/20261003-prepare/'+name;b=show(PRE,p);new=show(ACT,p)
    old=list(csv.DictReader(io.StringIO(b.decode()),delimiter='\t'));rows=list(csv.DictReader(io.StringIO(new.decode()),delimiter='\t'))
    appended=rows[len(old):];checks=[]
    for i,x in enumerate(appended):
        checks.append({'id':x['finding_id'],'registration_id':reg['dispositions'][i]['id'],'column_count':len(x),'no_overflow':None not in x,'canonical_OPEN':x['canonical_state']=='OPEN','candidate':x.get('candidate_commit'),'original':x.get('original_finding_commit'),'pending_actual':x.get('integration_verdict',x.get('downstream_gate')),'actual_review_fields':{k:v for k,v in x.items() if k in ['reviewed_integration_commit','integration_review_commit','integration_reviewer','integration_disposition']}})
    public.append({'path':p,'header_exact':new.splitlines(keepends=True)[0]==b.splitlines(keepends=True)[0],'accepted_prefix_exact_including_terminators':new.startswith(b),'accepted_records':len(old),'total_records':len(rows),'appended_records':len(appended),'checks':checks})
result['public_registration']=public
loc=doc('clause-location-bindings.json');first=next(iter(loc['records'].values())) if isinstance(loc['records'],dict) else loc['records'][0]
result['locator_schema']={'keys':list(loc),'first_record_keys':list(first)}
result['report_receipts']=boundary['report_bindings']
# Required exact diff flags are re-acquired; initial acquisition used find-renames and produced equal streams.
streams=[]
for base in [PRE,C3]:
    argv=['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',base,ACT,'--']
    b=subprocess.check_output(argv);streams.append({'base':base,'target':ACT,'argv':argv,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
result['required_flag_streams']=streams
(OUT/'independent-identity-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('copies',len(copies),'unequal',[x['path'] for x in copies if not x['actual_exact_copy'] or not x['source_record_match']])
print('boundary',result['boundary'])
print('hash rows',len(hashrows),'failures',[x['path'] for x in result['current_hashes'] if not x['match']])
print('planned',len(planned),'failures',[x['path'] for x in planned if not x['before']['match'] or not x['current']['match']])
print('qualified',len(qualified),'summary', [{k:v for k,v in x.items() if k in ['id','primary','original_complete_hash_match','acceptance_complete_hash_match','current_control_projection_matches','minimum_acceptance_projection_matches']} for x in qualified])
for x in public:print('public',{k:v for k,v in x.items() if k!='checks'})
print('locators',result['locator_schema'])
print('reports',[(x['owner'],x['report_commit'],x['reviewed_candidate'],len(x['paths'])) for x in boundary['report_bindings']])
print('streams',streams)
