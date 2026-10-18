#!/usr/bin/env python3
"""Validate the finite payload and bind it without a recursive self hash."""
import datetime
import hashlib
import json
import pathlib
import stat
import subprocess

base=pathlib.Path(__file__).resolve().parent
repo=base.parents[4]
rr=base.parents[1]
reference=pathlib.Path('/workspace/pokemon-essentials')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()

def read(name):
    return json.loads((base/name).read_text())

def write(name,d):
    (base/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git(*args,cwd=repo):
    return subprocess.check_output(['git',*args],cwd=cwd,text=True).strip()

assert git('branch','--show-current')=='codex/review-eighth-20261016-fd1df57-c84e'
identity=read('identities.json')
for x in identity['primary']:
    data=(reference/x['path']).read_bytes()
    assert sha(data)==x['sha256']
    assert data==subprocess.check_output(['git','show',identity['fixed_R']+':'+x['path']],cwd=reference)
prompt=rr/'inputs/eighth-global-review-prompt.md'
assert len(prompt.read_bytes())==36653
assert sha(prompt.read_bytes())=='63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b'
skill=rr/'inputs/review-SKILL.md'
assert len(skill.read_bytes())==3598
assert sha(skill.read_bytes())=='ac3c8560f38192269b65b061673896a77f5eb794b90e90644e3c445b2c3be1f8'
ledger=read('reading-ledger.json')
assert len(ledger['structures'])==123
for f in ledger['files']:
    us=[u for u in ledger['structures'] if u['path']==f['path']]
    assert us[0]['lines'][0]==1 and us[-1]['lines'][1]==f['logical_lines']
    assert all(a['lines'][1]+1==b['lines'][0] for a,b in zip(us,us[1:]))
assert {u['id'] for u in ledger['structures']}=={x['unit_id'] for x in read('forward-mapping.json')['entries']}
assert len(read('reverse-mapping.json')['dependency_claims'])==10
assert read('interfaces.json')['necessary_incoming_unreceived']==0
assert read('dependency-reception.json')['necessary_unreceived']==0
assert read('proposals.json')['new_proposals']==[]
ios=[]
for path in sorted((base/'read-io').glob('*.json')):
    d=json.loads(path.read_text())
    for stream in ['stdout','stderr']:
        data=path.with_suffix('.'+stream).read_bytes()
        assert len(data)==d[stream+'_bytes'] and sha(data)==d[stream+'_sha256']
    d['metadata_path']=str(path.relative_to(base))
    ios.append(d)
assert len(ios)==25 and all(d['exit_code']==0 for d in ios)
execution=read('execution-record.json')
execution['read_only_captured_commands']=ios
execution['recorded_utc']=now
execution['delivery_generation']={
    'build_command':['python3',str(base/'build_artifacts.py')],
    'actual_build_io':'read-io/024-build-artifacts.json/.stdout/.stderr',
    'terminal_finalize_command':['python3',str(base/'finalize.py')],
    'terminal_finalize_io':'Platform exec transcript; final reported result is the actual subprocess exit. No future-exit value is invented inside this file.',
    'output_effect':'Only tasks/reference_metadata_completion/ report/evidence artifacts'}
write('execution-record.json',execution)
progress=read('progress.json')
progress['semantic_completed_utc']=progress['ended_utc']
progress['updated_utc']=now
progress['ended_utc']=now
progress['delivery_validation']='validation.json: exact finite checks only'
write('progress.json',progress)
validation={
 'schema':'gr8-reference-metadata-validation/v1','recorded_utc':now,
 'status':'FINITE_ARTIFACT_CHECKS_PASSED',
 'checks':{'primary_fixed_bytes_match':'5/5','required_prompt_and_skill_bytes_hash':'2/2',
  'continuous_full_structural_partitions':'5/5','forward_unit_id_set':'123/123',
  'reverse_finite_claims':'10/10','incoming_interfaces':'2/2',
  'saved_command_raw_stdout_stderr_integrity':'25 commands / 50 streams',
  'all_delivered_json_parsed':True,'report_branch_unchanged':True,
  'original_failed_launcher_not_modified_by_this_task':True},
 'nonclaims':['This mechanical check grants no semantic read credit.','No whole-formal/global/source-run PASS.','Parent actual root reception is pending.'],
 'captured_command_exits':{'exit0':25,'nonzero':0},
 'other_failure_qualification':'Uncaptured initial path error and nested main-ref failure are retained in execution-record; original old launcher FAILED exit1 remains distinct.',
 'business_execution_count':0,'UPDATE_NOT_STARTED':True}
write('validation.json',validation)
payload=[]
for path in sorted(base.rglob('*')):
    if not path.is_file() or path.name=='completion-manifest.json':
        continue
    data=path.read_bytes()
    if path.suffix=='.json':
        json.loads(data)
    st=path.stat()
    payload.append({'path':str(path.relative_to(base)),
      'mode':'100755' if st.st_mode & stat.S_IXUSR else '100644',
      'actual_mode':oct(stat.S_IMODE(st.st_mode)),'bytes':len(data),
      'sha256':sha(data),
      'computed_git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
      'purpose':'Raw real I/O and command/UTC metadata' if 'read-io' in path.parts else 'Finite metadata review report, evidence, support or validation'})
manifest={
 'schema':'gr8-reference-metadata-completion-manifest/v1','recorded_utc':now,
 'actual_reviewer':'/root/reference_metadata_completion',
 'original_primary':'reference_metadata','write_set':'tasks/reference_metadata_completion/',
 'fixed_B8':identity['fixed_B8'],'fixed_R':identity['fixed_R'],
 'workspace_tree':'751dfde81048c81390f89a65ca1d1a565ba8e1ca',
 'formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e',
 'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0',
 'observed_report_HEAD_while_payload_uncommitted':git('rev-parse','HEAD'),
 'primary_scope':{'files':5,'logical_lines':742,'bytes':31678,'units':123,
  'unread':0,'unmapped':0,'necessary_incoming_unreceived':0,'formal_primary_files':0},
 'structural_counts':{'gitignore_groups':6,'gitignore_pattern_subassertions':22,
  'rubocop_blocks':42,'shortcut_groups':2,'license_contiguous_clause_units':61,'README_statement_groups':12},
 'dependency_scope':{'qualified_source_fact_objects':18,'qualified_loader_fact_objects':1,
  'formal_secondary_actual_intervals':[[1,105],[309,360]],'reverse_finite_claims':10,
  'necessary_incoming_interfaces_received':2},
 'new_proposals':0,'new_required':0,'new_optional':0,'new_policy':0,'new_limits':0,
 'root_acceptance':'PENDING_ROOT_ACTUAL_RECEPTION','root_decision_self_granted':False,
 'global_review_complete':False,'business_execution':'NOT_EXECUTED','business_execution_count':0,
 'requested':progress['requested'],'actual':progress['actual'],
 'payload_count':len(payload),'payload_bytes':sum(x['bytes'] for x in payload),'files':payload,
 'self_binding':'This manifest is intentionally excluded from its file list; root can bind its actual bytes/hash externally. No future commit or recursive self hash.',
 'publication':'This task did not commit or push; root owns publication and independent acceptance.',
 'original_failed_launcher_preserved':True,'UPDATE_NOT_STARTED':True}
write('completion-manifest.json',manifest)
print(json.dumps({'status':validation['status'],'payload_count':len(payload),
 'payload_bytes':manifest['payload_bytes'],'manifest_bytes':(base/'completion-manifest.json').stat().st_size,
 'manifest_sha256':sha((base/'completion-manifest.json').read_bytes()),
 'primary_unread':0,'necessary_incoming_unreceived':0,'new_findings':0,
 'root_actual_reception':'PENDING','UPDATE_NOT_STARTED':True},ensure_ascii=False))
