import datetime, difflib, hashlib, json, pathlib, subprocess

OUT=pathlib.Path(__file__).resolve().parent
ACTUAL='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PRIOR='9d5b4e99b617828690e6529b77a1e555d7c9eb1b'
PREFIX='review/remediation-sixth-20261014-prepare/'
INPUT=PREFIX+'integration/U01-U14-final-composite-20261014/actual-review-input.json'
calls=[]
def git(*args):
    begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(['git',*args],capture_output=True)
    calls.append({'argv':['git',*args],'cwd':str(pathlib.Path.cwd()),'start_utc':begin,
                  'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,
                  'stdout_bytes':len(p.stdout),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),
                  'stderr':p.stderr.decode('utf-8',errors='replace')})
    if p.returncode:raise RuntimeError(calls[-1])
    return p.stdout
def ident(d):
    return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()}
data=git('show',ACTUAL+':'+INPUT);j=json.loads(data)
assert ident(data)=={'bytes':152860,'sha256':'4671c1c31f18858a7719e88533029d746c62dfb77d4239cbb0cae633e79863da','git_blob':'ccf79b03165573f27070a417a2e3d986907f6623'}
assert git('rev-parse',ACTUAL+'^{tree}').decode().strip()=='67e8c55d520fa8cad2928cb4b95e24c3ed602d5a'
assert git('rev-parse',ACTUAL+':deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
assert j['required_count']==56 and len(j['batches'])==14 and j['pending_candidates']==[]
delta=j['delta_from_prior_actual'];changes=delta['changed_formal_paths']
actual_changed=git('diff','--name-only',PRIOR,ACTUAL,'--','deliverables/final-specification-set').decode().splitlines()
assert sorted(actual_changed)==sorted(f['path'] for f in changes) and len(changes)==8
delta_records=[]
for f in changes:
    old=git('show',PRIOR+':'+f['path']);new=git('show',ACTUAL+':'+f['path'])
    assert ident(old)==f['before'] and ident(new)==f['after']
    delta_records.append({**f,'identity_assertions_passed':True,'semantic_credit':'Only separately attributed actual reading/necessary interface review.'})
batches=[b for b in j['batches'] if b['batch'] in ['R6-U10','R6-U11','R6-U12']]
group_paths=sorted(set(p for b in batches for p in b['all_candidate_allowlist_paths']))
for b in batches:
    assert ident(git('show',ACTUAL+':'+b['contract_path']))==b['contract_identity']
    r=b['independent_review'];assert ident(git('show',r['review_commit']+':'+r['report_path']))==r['report_identity']
u13=next(b for b in j['batches'] if b['batch']=='R6-U13')
assert u13['candidate_published_commit']=='9971fe84896786645cdcda3ab45e5caf7785cabc'
assert u13['independent_review']['review_commit']=='411b563309a4e642e628dcf8289e36c6fe3fd37f'
assert ident(git('show',ACTUAL+':'+u13['contract_path']))==u13['contract_identity']
r=u13['independent_review'];assert ident(git('show',r['review_commit']+':'+r['report_path']))==r['report_identity']
assert git('rev-parse',u13['candidate_published_commit']+'^{tree}').decode().strip()==u13['candidate_workspace_tree']
assert git('rev-parse',r['review_commit']+'^{tree}').decode().strip()==r['review_workspace_tree']
joint_paths=['deliverables/final-specification-set/'+s for s in [
    'combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md',
    'combat-requirements/wp55-facility-session-and-restoration.md',
    'pokemon-rules/wp53-safari-and-bug-catching-contest.md',
    'test-catalog/combat-requirements-wp54-55-56-58.md']]
records=[]
for path in sorted(set(group_paths+joint_paths)):
    f=next(f for f in j['files'] if f['path']==path)
    new=git('show',ACTUAL+':'+path);old=git('show',PRIOR+':'+path)
    assert ident(new)==f['actual']
    assert git('ls-tree',ACTUAL,path).decode().startswith('100644 blob '+f['actual']['git_blob']+'\t')
    contributions=[]
    base=git('show',j['fixed_main']+':'+path).decode().splitlines(keepends=True)
    for c in f['contributions']:
        cand=git('show',c['candidate_commit']+':'+c['candidate_path']);assert ident(cand)==c['identity']
        blocks=[]
        for kind,a,z,x,y in difflib.SequenceMatcher(None,base,cand.decode().splitlines(keepends=True),autojunk=False).get_opcodes():
            if kind=='equal':continue
            replacement=''.join(cand.decode().splitlines(keepends=True)[x:y]).encode()
            assert not replacement or replacement in new
            blocks.append({'kind':kind,'baseline_lines':[a+1,z],'candidate_lines':[x+1,y],
                           'replacement_bytes':len(replacement),'replacement_sha256':hashlib.sha256(replacement).hexdigest(),
                           'literal_replacement_retained':True if replacement else None})
        contributions.append({'batch':c['batch'],'candidate_commit':c['candidate_commit'],
                              'candidate_path':c['candidate_path'],'identity':c['identity'],'blocks':blocks})
    records.append({'path':path,'actual':ident(new),'prior':ident(old),'unchanged_from_9d':new==old,
                    'physical_lines':len(new.splitlines()),'group_contribution':path in group_paths,
                    'joint_interface_read_path':path in joint_paths,'contributions':contributions})
assert sum(f['unchanged_from_9d'] for f in records if f['group_contribution'])==10
receiver_path=j['receiver_delta']['formal_path'];receiver=git('show',ACTUAL+':'+receiver_path)
assert receiver==git('show',PRIOR+':'+receiver_path)
payload=json.loads(git('show',j['receiver_delta']['payload_commit']+':'+j['receiver_delta']['payload_path']))
assert receiver.count(payload['proposed_full_line'].encode())==1
result={'schema':'r6.actual.group-d.final-validation.v1','actual_commit':ACTUAL,
        'workspace_tree':'67e8c55d520fa8cad2928cb4b95e24c3ed602d5a','formal_tree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c',
        'input_path':INPUT,'input_identity':ident(data),'input_lines':len(data.splitlines()),
        'group_ids':[i for b in batches for i in b['required_ids']],'batches':batches,
        'producer_U13_binding':u13,'delta_from_prior':delta_records,'files':records,
        'group_file_count':len(group_paths),'group_file_bytes':sum(f['actual']['bytes'] for f in records if f['group_contribution']),
        'joint_unique_file_count':len(records),'joint_unique_file_bytes':sum(f['actual']['bytes'] for f in records),
        'receiver_byte_equal_to_9d':True,'all_assertions_passed':True,
        'qualification':'Exact bytes and diff assertions only; no automatic final PASS transfer or semantic/execution credit.'}
(OUT/'final-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'final-validation-command-receipts.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['actual_commit','group_file_count','group_file_bytes','joint_unique_file_count','joint_unique_file_bytes','all_assertions_passed']},ensure_ascii=False))
