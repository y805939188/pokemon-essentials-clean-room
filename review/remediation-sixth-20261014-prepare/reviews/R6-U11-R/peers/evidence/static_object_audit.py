"""Independent finite static artifact audit. Does not import or run author/project code."""
from pathlib import Path
from collections import defaultdict
import subprocess, hashlib, json, difflib, datetime, sys, re

ROOT=Path('/workspace/pokemon-essentials-clean-room')
OUT=ROOT/'review/remediation-sixth-20261014-prepare/reviews/R6-U11-R/peers/evidence'
PREP='review/remediation-sixth-20261014-prepare'
OWN=PREP+'/candidates/R6-U11/'
P='e93d0e56750a6a16cc50cc68b2c97f11ea255153'
C='54af598ca85211641348e6057ed0c348044787fe'
B='469a268b92daed7b4d28d7fd0da75520cbb7228f'
M='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REQUESTED_REF=Path('/workspace/pokemon-essentials-reference-r6')
REF=REQUESTED_REF if REQUESTED_REF.exists() else ROOT
READSET=[]

def git(*args, reference=False):
    return subprocess.check_output(['git','-C',str(REF if reference else ROOT),*args])

def identity(b):
    return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}

def read_object(commit,path,purpose,reference=False):
    b=git('show',commit+':'+path,reference=reference)
    entry=git('ls-tree','-z',commit,'--',path,reference=reference).rstrip(b'\0').decode()
    props=entry.split('\t',1)[0].split()
    rec={'repository':str(REF if reference else ROOT),'commit':commit,
         'tree':git('rev-parse',commit+'^{tree}',reference=reference).decode().strip(),
         'path':path,'mode':props[0],'git_object_type':props[1],**identity(b),
         'physical_lines':len(b.splitlines()),'read_purpose':purpose,
         'static_complete_bytes_read':True,'semantic_read_credit_from_hash':False}
    assert rec['git_blob']==props[2]
    READSET.append(rec)
    return b,rec

def semantic_file(path,purpose):
    b,rec=read_object(P,path,purpose)
    rec['semantic_read_scope']='Complete file read in reviewer tool transcript, then independently parsed for audit'
    return b,rec

def check_expected(expected,actual):
    return all(expected.get(k)==actual.get(k) for k in ('bytes','sha256','git_blob'))

start=datetime.datetime.now(datetime.timezone.utc).isoformat()
contract_bytes,contract_ident=read_object(P,PREP+'/contracts/R6-U11.json','semantic complete via exact embedded prompt copy')
contract=json.loads(contract_bytes)
prompt_bytes,prompt_ident=read_object(P,PREP+'/prompts/R6-U11-R.md','reviewer prompt complete semantic read, lines1..3446')
embedded=re.findall(rb'```json\n(.*?)\n```',prompt_bytes,re.S)[0]+b'\n'
assert embedded==contract_bytes
agents_bytes,agents_ident=read_object(P,'AGENTS.md','complete semantic repository guidance')
missing={'/workspace/AGENTS.md':not Path('/workspace/AGENTS.md').exists(),
         str(ROOT/'.agents'):not (ROOT/'.agents').exists(),
         str(ROOT/'.agents/skills'):not (ROOT/'.agents/skills').exists(),
         str(ROOT/'.codex'):not (ROOT/'.codex').exists()}

changed=[x for x in git('diff','--name-only',B,P).decode().splitlines()]
core_changed=git('diff','--name-only',B,C).decode().splitlines()
pub_changed=git('diff','--name-only',C,P).decode().splitlines()
assert len(changed)==25 and len(core_changed)==20 and len(pub_changed)==5
assert all(x.startswith(OWN) for x in changed)
assert not git('diff','--name-only',B,P,'--','deliverables','audit','planning','reference')

evidence_identities=[]
for p in git('ls-tree','-r','--name-only',P,'--',OWN+'evidence').decode().splitlines():
    b,rec=semantic_file(p,'complete author evidence semantic read and independent static parse')
    assert (ROOT/p).read_bytes()==b
    evidence_identities.append(rec)

manifest=json.loads((ROOT/(OWN+'evidence/candidate-manifest.json')).read_bytes())
manifest_results=[]
for record in manifest['files']:
    b,actual=read_object(C,record['path'],'manifest independent complete object identity')
    manifest_results.append({'path':record['path'],'claimed':record,'actual':actual,
                             'identity_match':check_expected(record,actual),
                             'mode_match':record['mode']==actual['mode'],
                             'UTF8_text':b.decode('utf-8') is not None})
assert all(x['identity_match'] and x['mode_match'] for x in manifest_results)
self_path=OWN+'evidence/candidate-manifest.json'
assert set(x['path'] for x in manifest['files'])==set(core_changed)-{self_path}
assert len(manifest_results)==19 and manifest['manifest_self_excluded'] is True

fixed_results=[]
for record in json.loads((ROOT/(OWN+'evidence/fixed-payload-validation.json')).read_bytes())['records']:
    b,actual=read_object(record['commit'],record['path'],'author fixed identity independent check',record['commit']==R)
    fixed_results.append({'path':record['path'],'commit':record['commit'],'match':check_expected(record,actual),
                          'tree_match':record['tree']==actual['tree'],'entry_match':record['entry'].split('\t')[0]==actual['mode']+' blob '+actual['git_blob']})
assert all(x['match'] and x['tree_match'] and x['entry_match'] for x in fixed_results)

diff_results=[]
rows_results=[]
diff_text=[]
for p in contract['candidate_formal_paths']:
    original,old_id=read_object(M,p,'complete frozen formal bytes for independent diff/protection')
    baseline,base_id=read_object(B,OWN+'mirror/'+p,'complete baseline mirror identity')
    candidate,new_id=read_object(P,OWN+'mirror/'+p,'complete candidate bytes for independent diff/protection')
    current=(ROOT/p).read_bytes()
    assert original==baseline and original==current and original!=candidate
    a=original.decode().splitlines(keepends=True);z=candidate.decode().splitlines(keepends=True)
    ops=[]
    for tag,i,j,k,l in difflib.SequenceMatcher(None,a,z,autojunk=False).get_opcodes():
        if tag!='equal':ops.append({'kind':tag,'baseline_zero_based_half_open':[i,j],
                                    'candidate_zero_based_half_open':[k,l],
                                    'baseline_lines_1based_inclusive':[i+1,j] if j>i else None,
                                    'candidate_lines_1based_inclusive':[k+1,l] if l>k else None,
                                    'old_text':''.join(a[i:j]),'new_text':''.join(z[k:l])})
    diff_results.append({'formal_path':p,'baseline':old_id,'candidate':new_id,
                         'baseline_mirror_equals_frozen_formal':True,'current_formal_equals_frozen':True,
                         'byte_delta':len(candidate)-len(original),'diff':ops})
    diff_text.extend(difflib.unified_diff(a,z,fromfile='frozen/'+p,tofile='candidate/'+p))
    if '/test-catalog/' in p:
        oldrows=[(i+1,x) for i,x in enumerate(original.splitlines(keepends=True)) if x.startswith(b'|')]
        newrows=[(i+1,x) for i,x in enumerate(candidate.splitlines(keepends=True)) if x.startswith(b'|')]
        cursor=0;maps=[]
        for line,row in oldrows:
            while cursor<len(newrows) and newrows[cursor][1]!=row:cursor+=1
            assert cursor<len(newrows),(p,line)
            maps.append({'baseline_line':line,'candidate_line':newrows[cursor][0],
                         'row_sha256':hashlib.sha256(row).hexdigest()})
            cursor+=1
        rows_results.append({'path':p,'old_rows':len(oldrows),'candidate_rows':len(newrows),
                             'all_old_rows_byte_equal_in_order':True,
                             'complete_old_rows_sha256':hashlib.sha256(b''.join(x[1] for x in oldrows)).hexdigest(),
                             'mapping':maps})
assert sum(x['old_rows'] for x in rows_results)==931

ledger=[json.loads(x) for x in (ROOT/(OWN+'evidence/reading-ledger.jsonl')).read_text().splitlines()]
ledger_results=[]
coverage=defaultdict(set)
for n,record in enumerate(ledger,1):
    b,actual=read_object(record['commit'],record['path'],'author ledger input complete identity; no semantic inference',record['commit']==R)
    assert check_expected(record,actual)
    if 'range' in record:
        lo,hi=record['range'];lines=b.decode().splitlines()
        assert 1<=lo<=hi<=len(lines)
        emitted='\n'.join(lines[lo-1:hi])+'\n'
        coverage[(record['commit'],record['path'])].update(range(lo,hi+1))
        assert record['total_lines']==len(lines)
    else:
        j=json.loads(b);out=[]
        for pointer in record['json_pointers']:
            v=j
            for part in pointer.strip('/').split('/') if pointer else []:
                part=part.replace('~1','/').replace('~0','~')
                v=v[int(part)] if isinstance(v,list) else v[part]
            out.append({'pointer':pointer,'content':v})
        emitted=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
    stdout_match=hashlib.sha256(emitted.encode()).hexdigest()==record['stdout_sha256']
    assert stdout_match
    ledger_results.append({'ledger_line':n,'path':record['path'],'commit':record['commit'],
                           'identity_match':True,'declared_output_hash_match':True,
                           'range':record.get('range'),'json_pointers':record.get('json_pointers'),
                           'actual_stdout_transcript_independently_available':False,
                           'limit':'Reconstruction matches declaration; this does not prove actual tool output was untruncated or author semantic comprehension.'})
early=json.loads((ROOT/(OWN+'evidence/early-reading-and-attempts.json')).read_bytes())
for record in early['early_complete_reads']:
    for lo,hi in record['ranges']:coverage[(record['commit'],record['path'])].update(range(lo,hi+1))
coverage_results=[]
for claim in json.loads((ROOT/(OWN+'evidence/tool-validation.json')).read_bytes())['complete_primary_read_ranges']:
    ranges=coverage[(claim['commit'],claim['path'])]
    coverage_results.append({'commit':claim['commit'],'path':claim['path'],'lines':claim['lines'],
                             'declared_ranges_complete':set(range(1,claim['lines']+1))<=ranges,
                             'identity_and_output_hash_only_not_independent_semantic_proof':True})
assert all(x['declared_ranges_complete'] for x in coverage_results)

remote_capture=json.loads((OUT/'remote-full-content-capture.json').read_bytes())
remote_results=[]
for expected,got in zip(remote_capture['expected'],remote_capture['remote']):
    assert expected['path']==got['path'] and not got.get('isError') and not got.get('error')
    content=got['result']['content'].encode('utf-8')
    b,local_id=read_object(P,expected['path'],'remote full content independent exact byte comparison')
    actual=identity(content)
    remote_results.append({'path':expected['path'],'requested_blob':got['requested_blob'],
                           'utc_start':got['utc_start'],'utc_end':got['utc_end'],
                           'actual':actual,'local':local_id,
                           'exact_bytes_match':content==b,'identity_match':check_expected(expected,actual),
                           'git_blob_independently_computed':actual['git_blob'],
                           'mode_type_path_checked_in_local_immutable_commit':True,
                           'method':'Fresh remote fetch_blob complete returned UTF-8 content; Python hashlib SHA256 and Git blob SHA1'})
assert len(remote_results)==25 and all(x['exact_bytes_match'] and x['identity_match'] for x in remote_results)
binding=json.loads((OUT/'remote-commit-binding.json').read_bytes())
assert set(binding['core_files'])==set(core_changed)
assert set(binding['publication_files'])==set(pub_changed)
receipt=json.loads((ROOT/(OWN+'evidence/publication/core-readback.json')).read_bytes())
core_receipt_checks=[]
for record in receipt['records']:
    b,actual=read_object(C,record['path'],'author core receipt independent identity check')
    core_receipt_checks.append({'path':record['path'],'claimed_expected_match':check_expected(record['expected'],actual),
                                'claimed_actual_match':record['actual']['bytes']==actual['bytes'] and record['actual']['sha256']==actual['sha256'],
                                'matched_boolean':record['matched'] is True})
assert len(core_receipt_checks)==20 and all(all(v for k,v in x.items() if k!='path') for x in core_receipt_checks)
assert receipt['remote_payload_bytes']==sum(x['bytes'] for x in remote_capture['expected'] if x['path'] in core_changed)==439832

report={'schema':'r6-u11-independent-evidence-object-audit.v1',
        'reviewer_task':'/root/evidence_audit','started_utc':start,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'runtime':sys.version,'evidence_level':'TOOL_VALIDATION; no author/project/reference code execution',
        'configuration':{'requested_model':'gpt-6.1-sol','requested_effort':'ultra','requested_tier':'default','requested_speed':'default',
                         'effective_model':'UNVERIFIED','effective_effort':'UNVERIFIED','effective_tier':'UNVERIFIED','effective_speed':'UNVERIFIED','platform_uuid':'UNVERIFIED'},
        'input':{'P':P,'C':C,'B':B,'main':M,'reference':R,'requested_reference_database':str(REQUESTED_REF),'requested_reference_database_exists':REQUESTED_REF.exists(),'actual_reference_object_database':str(REF),'prompt':prompt_ident,'contract':contract_ident,'prompt_contract_byte_equal':True,'AGENTS':agents_ident,'missing_guidance_paths':missing},
        'scope':{'changed_paths':changed,'core_changed_paths':core_changed,'publication_changed_paths':pub_changed,
                 'all_25_paths_within_candidate_allowlist':True,'no_formal_public_reference_tree_changes_in_candidate_commits':True,
                 'entire_historical_uncommitted_write_history_proved':False},
        'author_evidence_files':evidence_identities,'manifest_entries':manifest_results,'manifest_exact_19_excluding_self':True,
        'fixed_payload_checks':fixed_results,'mirror_diffs':diff_results,'catalog_old_rows':rows_results,
        'author_ledger_checks':ledger_results,'author_primary_declared_read_coverage':coverage_results,
        'remote_full_payloads':remote_results,'remote_payload_count':25,'remote_payload_bytes':sum(x['actual']['bytes'] for x in remote_results),
        'remote_all_complete_bytes_SHA256_git_blob_match':True,'remote_binding':binding,
        'author_core_receipt_checks':core_receipt_checks,
        'new_reference_execution':0,'new_behavior_model_execution':0,'new_host_Demo_save_execution':0,
        'read_set':READSET,
        'limitations':['No valid effective runtime model/effort/tier/speed/UUID echo exposed; remain UNVERIFIED.',
                       'Actual author stdout transcripts outside the frozen evidence pack are not independently available; ledger declarations and reconstructed output hashes are independently checked only.',
                       'Reference/source objects were read as inert Git bytes; hash/range checks are not source semantic behavior approval.',
                       'Current and committed object scope checks do not prove absence of transient historical writes or changes on unseen Mac hosts.',
                       'GitHub connector returns normalized commit metadata without raw tree or mode fields; identical complete commit SHA cryptographically binds the independently verified local immutable commit tree.',
                       'No candidate behavior, integrated acceptance, formal acceptance or CLOSED is signed by this evidence-only audit.']}
(OUT/'static-object-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(OUT/'mirror-diff.patch').write_text(''.join(diff_text))
print(json.dumps({'result':'INDEPENDENT_STATIC_ARTIFACT_CHECKS_PASS','manifest_entries':19,'author_evidence_files':len(evidence_identities),'old_catalog_rows':931,'ledger_records':44,'remote_payloads':25,'remote_bytes':report['remote_payload_bytes'],'changed_paths':25,'new_reference_executions':0},ensure_ascii=False))
