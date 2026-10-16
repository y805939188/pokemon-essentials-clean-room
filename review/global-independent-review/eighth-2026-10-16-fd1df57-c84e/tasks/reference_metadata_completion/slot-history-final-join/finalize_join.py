import datetime
import hashlib
import json
import pathlib
import stat

base=pathlib.Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()

def read(p):
    return json.loads(pathlib.Path(p).read_text())

def write(name,value):
    (base/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def sha(data):
    return hashlib.sha256(data).hexdigest()

old=read(base.parent/'completion-manifest.json')
for row in old['files']:
    data=(base.parent/row['path']).read_bytes()
    assert len(data)==row['bytes'] and sha(data)==row['sha256']
assert len(old['files'])==89
assert sha((base.parent/'completion-manifest.json').read_bytes())=='c5acdd1f8154e72a743ce1ae203ca0fad30f0ac619c863764cfe9208e6c10093'
d=read(base/'finite-comparison.json')
assert d['comparison_rows']==len(d['comparisons'])==20
required=['premises','old_normal_control','old_minimal_counterexample','observation_point',
 'old_minimum_revision_obligation','strongest_alias_or_no_required_argument',
 'substantive_relationship_to_ELR001','old_status_and_qualification','actual_read_io']
assert all(all(r[k] for k in required) for r in d['comparisons'])
assert d['exact_old_parent']=='R6-D-LZ-002'
assert d['new_independent_votes']==d['new_contexts']==d['new_findings']==0
assert d['necessary_available_meanings_unread']==d['necessary_incoming_unreceived']==[]
facts=read(base/'qualified-facts.json')
assert len(facts['R5_qualified_original_criterion_meanings'])==29
assert len(facts['R5_qualified_Slot_complete_meaning_and_nine_obligations']['criteria'])==9
assert len(facts['R6_current_complete_qualified_meaning']['facts'])==5
ios=[]
for p in sorted((base/'read-io').glob('*.json')):
    row=read(p)
    for stream in ['stdout','stderr']:
        raw=p.with_suffix('.'+stream).read_bytes()
        assert len(raw)==row[stream+'_bytes'] and sha(raw)==row[stream+'_sha256']
    assert row['exit_code']==0
    ios.append(row)
assert len(ios)==18
ledger=read(base/'reading-ledger.json')
ledger['captured_io']=ios
ledger['finalized_utc']=now
write('reading-ledger.json',ledger)
progress=read(base/'progress.json')
progress['finalized_utc']=now
progress['validation']='validation.json: finite artifact checks only'
write('progress.json',progress)
write('validation.json',{'schema':'gr8-slot-history-finite-validation/v1','utc':now,
 'status':'FINITE_CHECKS_PASSED','original89_payloads_unchanged':89,'original_manifest_unchanged':True,
 'comparison_rows':20,'required_comparison_fields_nonempty':True,
 'selected_R5_locale_criteria':29,'selected_R5_Slot_criteria':9,'selected_R6_complete_current_facts':5,
 'captured_commands':18,'stdout_stderr_streams_exact':36,'captured_nonzero_exits':0,
 'projection_truncation_003_recovered_by':['004','005','011'],
 'necessary_available_unread':0,'necessary_incoming_unreceived':0,
 'semantic_credit_from_this_validation':0,'new_contexts':0,'new_independent_votes':0,
 'new_business_runs':0,'root_actual_reception':'PENDING','UPDATE_NOT_STARTED':True})
payload=[]
for p in sorted(base.rglob('*')):
    if not p.is_file() or p.name=='manifest.json':
        continue
    data=p.read_bytes()
    if p.suffix=='.json':read(p)
    payload.append({'path':str(p.relative_to(base)),'mode':'100755' if p.stat().st_mode&stat.S_IXUSR else '100644',
     'bytes':len(data),'sha256':sha(data),
     'computed_git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()})
manifest={'schema':'gr8-slot-history-final-join-manifest/v1','utc':now,
 'task':'/root/reference_metadata_completion','same_context_continuation':True,
 'write_set':'tasks/reference_metadata_completion/slot-history-final-join/',
 'fixed_B8':'fd1df570cad987dc3852a3b958f03916e317f7fe','fixed_R':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
 'result':d['finite_conclusion'],'current_GR8_ELR_001_required_P3_preserved':True,
 'comparison_rows':20,'qualified_original_meanings':'qualified-facts.json',
 'necessary_unread':0,'necessary_incoming_unreceived':0,'new_findings':0,
 'new_contexts':0,'new_independent_votes':0,'business_execution':'NOT_EXECUTED',
 'root_canonical_and_final_reception':'RESERVED; no self-granted global canonical decision',
 'original89_and_manifest_unchanged':True,
 'requested':progress['requested'],'actual':progress['actual'],
 'payload_count':len(payload),'payload_bytes':sum(r['bytes'] for r in payload),'files':payload,
 'self_binding':'Manifest excludes itself; parent binds actual bytes/SHA externally. No future commit/self hash.',
 'UPDATE_NOT_STARTED':True}
write('manifest.json',manifest)
print(json.dumps({'status':'FINITE_CHECKS_PASSED','payload_count':len(payload),
 'payload_bytes':manifest['payload_bytes'],'manifest_bytes':(base/'manifest.json').stat().st_size,
 'manifest_sha256':sha((base/'manifest.json').read_bytes()),'original89_changed':0,
 'comparison_rows':20,'necessary_unread':0,'necessary_unreceived':0,
 'new_contexts':0,'new_independent_votes':0,'UPDATE_NOT_STARTED':True}))
