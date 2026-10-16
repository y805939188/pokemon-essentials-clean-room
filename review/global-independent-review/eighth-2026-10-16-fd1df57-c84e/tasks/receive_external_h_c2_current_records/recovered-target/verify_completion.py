"""Static artifact/identity/protection checks, not a source semantic PASS."""
from pathlib import Path
import json,hashlib,gzip,subprocess,datetime
T=Path(__file__).parent;REPO=T.parents[4];R=Path('/workspace/pokemon-essentials')
B='fd1df570cad987dc3852a3b958f03916e317f7fe';RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def git(repo,*args):return subprocess.check_output(['git',*args],cwd=repo)
def save(n,v):(T/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
checks=[]
def check(name,condition,detail=None):
    checks.append(dict(name=name,passed=bool(condition),detail=detail))
    assert condition,(name,detail)
check('project HEAD remains B8',git(REPO,'rev-parse','HEAD').decode().strip()==B)
check('reference HEAD remains R',git(R,'rev-parse','HEAD').decode().strip()==RC)
check('project tracked worktree unchanged',not git(REPO,'diff','--name-only').strip())
check('project original index unchanged',not git(REPO,'diff','--cached','--name-only').strip())
check('reference tracked worktree unchanged',not git(R,'diff','--name-only').strip())
relative=str(T.relative_to(REPO))+'/'
others=git(REPO,'ls-files','--others','--exclude-standard').decode().splitlines()
check('all new visible files confined to task root',all(p.startswith(relative) for p in others),len(others))
for repo,rev,prefix,label,expected_count in ((REPO,B,'deliverables/final-specification-set','formal',131),(R,RC,'','reference',432)):
    args=['ls-tree','-r','-z',rev]
    if prefix:args+=['--',prefix]
    rows=[]
    for raw in git(repo,*args).split(b'\0'):
        if not raw:continue
        meta,path=raw.split(b'\t',1);mode,kind,blob=meta.decode().split();path=path.decode()
        if kind!='blob':continue
        data=(repo/path).read_bytes();actual=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
        rows.append(dict(path=path,mode=mode,blob=blob,worktree_blob=actual,bytes=len(data)))
        check(label+' frozen file '+path,actual==blob)
    check(label+' exact frozen count',len(rows)==expected_count,len(rows))
    if label=='formal':formal=rows
    else:reference=rows
protected=('refs/heads/main','refs/tags/delivery/seventh-round-closed-final-20261016')
remote_refs=git(REPO,'ls-remote','origin',*protected).decode()
resolved={x.split('\t')[1]:x.split('\t')[0] for x in remote_refs.splitlines()}
for ref in protected:check('protected remote ref '+ref,resolved.get(ref)==B)
ledger=json.loads((T/'reading-ledger.json').read_text());c=ledger['counts']
check('25 exact readset identities',len(ledger['entries'])==25 and c['original_C2_identities_verified']==25)
check('37 complete records and 259 groups',c['canonical_records_fully_value_read']==37 and c['C13_seven_groups']==259)
check('31 original nonmandatory records',c['inherited_nonmandatory_records']==31)
check('typed strata do not give body approval',all(not x.get('underlying_target_reading_credit_from_inventory') for x in json.loads((T/'purpose-dispositions.json').read_text())['entries']))
check('no unfinished exact display pending',not json.loads((T/'continued-reading-ledger.json').read_text())['pending'])
check('handoff complete rendering equal',json.loads((T/'handoff-view-comparison.json').read_text())['complete_37_rendered_body_equal'])
find=json.loads((T/'findings.json').read_text())
check('one suspect pending main nonproposer',len(find['records'])==1 and find['accepted_findings']==0 and find['records'][0]['independent_counter_reception']=='NOT_RECEIVED')
check('no self classification required',find['required_classification_by_this_task']==0)
bi=json.loads((T/'exact-reading-evidence.identity.json').read_text());enc=(T/'exact-reading-evidence.json.gz').read_bytes();dec=gzip.decompress(enc)
check('evidence gzip roundtrip identity',len(dec)==bi['decoded_bytes'] and hashlib.sha256(dec).hexdigest()==bi['decoded_sha256'])
parsed=json.loads(dec)
check('exact reading evidence recoverable',bool(parsed['acknowledgments']) and bool(parsed['pool']) and bool(parsed['exact_displays']))
check('UPDATE_NOT_STARTED and new execution zero',json.loads((T/'progress.json').read_text())['update_state']=='UPDATE_NOT_STARTED' and c['new_behavior_runs']==0)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
save('protection-validation.json',dict(status='FROZEN_INPUTS_AND_WRITE_BOUNDARY_MATCH',utc=now,formal_files=formal,reference_files=reference,
    project_HEAD=B,reference_HEAD=RC,visible_new_files=others,only_task_writes=True,protected_remote_refs=resolved,
    local_protected_refs='Not created: main is absent in this cloud checkout; remote refs checked directly',
    original_Mac_untracked_and_other_worktree_state='NOT_ASSERTED_FOR_THIS_DIFFERENT_CLOUD_ENVIRONMENT',no_behavior_execution=True))
save('validation.json',dict(status='STATIC_ARTIFACT_IDENTITY_AND_PROTECTION_CHECKS_PASS',utc=now,checks=checks,
    check_count=len(checks),failures=0,qualification='Not source semantics, not runtime, not root acceptance; no test vector executed',
    assigned_record_value_reading_complete=True,source_formal_global_PASS=False,root_final_reception='NOT_RECEIVED',
    retained_validation_failure='First check assumed local refs/heads/main existed and exited128. No mutation; corrected to verify actual remote protected refs. Not a material blocker.'))
print(json.dumps(dict(status='STATIC_CHECKS_PASS',checks=len(checks),formal_files=len(formal),reference_files=len(reference),task_files=len(others))))
