"""Fresh exact-actual Git/JSON/hash/specification-text bookkeeping only.
No imported or executed author, prior reviewer, reference, or behavioral program.
"""
import collections, csv, functools, hashlib, io, json, pathlib, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[6]
OUT = pathlib.Path(__file__).resolve().parent
BASE = '407536adb682a04161d3e9c82f153a62b1becd97'
C = '18873059e56314fcd48f6081d5a65a79301a52f6'
ACT = 'dc64807c2d726171827017ec636c6a73efd8e4b5'
PAY = '3ec4af10f9822999b329ac794e4694bc5aa89aac'
F = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
A = '41fffb540c6483f5296ea0d33b789b75180d27ed'
B09 = 'review/remediation/20261003-prepare/batches/B09/'
STAGE = B09 + 'integration-stage-1/'
PREV = B09 + 'affected-B07-review-round-1/'
PREVCOM = 'ee2084a05dd63ec3a690bd29788f247e100f4d78'
checks = []

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])
def sha(b):
    return hashlib.sha256(b).hexdigest()
@functools.lru_cache(None)
def blob(c, p):
    return git('show', c + ':' + p)
def js(c, p):
    return json.loads(blob(c, p))
@functools.lru_cache(None)
def ident(c, p):
    b = blob(c, p)
    return dict(commit=c, path=p, git_blob=git('rev-parse', c+':'+p).decode().strip(), sha256=sha(b), bytes=len(b))
def ck(label, value, detail=None):
    checks.append(dict(check=label, passed=bool(value), detail=detail))
def dump(n, value):
    (OUT/n).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
def changes(a, b):
    return [tuple(x.split('\t')) for x in git('diff', '--name-status', '--no-renames', a, b).decode().splitlines()]
def objsha(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())
def apply_spec_text_patch(before, patch):
    old = before.decode().splitlines(keepends=True)
    lines = patch.decode().splitlines(keepends=True)
    output, pos, i, hunks = [], 0, 0, 0
    while i < len(lines):
        m = re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', lines[i])
        if not m:
            i += 1
            continue
        start, left_count, right_count = max(int(m[1])-1,0), int(m[2] or 1), int(m[4] or 1)
        lhs, rhs = [], []
        i += 1
        while i < len(lines) and not lines[i].startswith(('@@ ', 'diff --git ', '--- ')):
            t = lines[i]
            if t.startswith(' '): lhs.append(t[1:]); rhs.append(t[1:])
            elif t.startswith('-'): lhs.append(t[1:])
            elif t.startswith('+'): rhs.append(t[1:])
            else: break
            i += 1
        assert len(lhs)==left_count and len(rhs)==right_count and start>=pos and old[start:start+left_count]==lhs
        output.extend(old[pos:start]); output.extend(rhs)
        pos = start+left_count
        hunks += 1
    assert hunks
    output.extend(old[pos:])
    return ''.join(output).encode()
def verify(rec, fallback=ACT, label='identity', path=None):
    c = rec.get('commit') or fallback
    p = rec.get('path') or path
    actual = ident(c, p)
    for k in ('git_blob', 'sha256', 'bytes'):
        if k in rec:
            val = int(rec[k]) if k == 'bytes' else rec[k]
            ck(label+':'+p+':'+k, val == actual[k])
    return actual
def walk(value, pointer, fallback=ACT):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and 'git_blob' in value and 'sha256' in value and 'bytes' in value:
            verify(value, fallback, pointer)
        for k, v in value.items():
            walk(v, pointer+'/'+k, fallback)
    elif isinstance(value, list):
        for i, v in enumerate(value):
            walk(v, pointer+'/'+str(i), fallback)

manifest = js(ACT, STAGE+'integration-manifest.json')
freeze = js(ACT, STAGE+'diff-and-freeze.json')
norm = [x['path'] for x in manifest['reviewed_normative_identities']]
public = manifest['public_write_paths']
stagepaths = git('ls-tree', '-r', '--name-only', ACT, STAGE).decode().splitlines()
ck('actual exact single parent', git('rev-list', '--parents', '-n', '1', ACT).decode().split() == [ACT, PAY])
ck('actual exact tree', git('rev-parse', ACT+'^{tree}').decode().strip() == '6f836ef1e40c1720413b8b1202845320880e0954')
ck('actual adds exactly three frozen evidence paths', changes(PAY, ACT) == [('A', p) for p in sorted(manifest['final_freeze_paths'])])
ck('stage independently fourteen paths', len(stagepaths) == 14 and set(stagepaths) == set(manifest['management_stage_paths']+manifest['final_freeze_paths']))
bc, cc = changes(BASE, ACT), changes(C, ACT)
ck('full unfiltered predecessor-actual199', len(bc) == 199 and collections.Counter(s for s,p in bc) == {'M':24,'A':175})
ck('full unfiltered candidate-actual112', len(cc) == 112 and collections.Counter(s for s,p in cc) == {'M':10,'A':102})
ck('predecessor M exact14 normative and10 public', {p for s,p in bc if s=='M'} == set(norm+public))
ck('candidate M exact10 public', {p for s,p in cc if s=='M'} == set(public) and len(public)==10)
ck('normative exact8 final6 original', len(norm)==14 and sum(p.startswith('deliverables/') for p in norm)==8 and sum(p.startswith('specs/') for p in norm)==6)
ck('all normative candidate bytes preserved actual', all(blob(C,p)==blob(ACT,p) for p in norm))
for p in norm:
    verify(next(x for x in manifest['reviewed_normative_identities'] if x['path']==p),label='normative')
sourcepaths = set()
for x in manifest['source_identities']:
    verify(x,label='incoming-source')
    ck('incoming file actual immutable '+x['path'], blob(x['commit'],x['path']) == blob(ACT,x['path']))
    sourcepaths.add(x['path'])
ck('incoming independently175 distinct paths', len(sourcepaths)==175)
ck('incoming set full175 = predecessor-candidate87 plus five report88', sourcepaths == {p for s,p in changes(BASE,C)} | {p for s,p in cc if s=='A' and p not in stagepaths})
ck('no unlisted complete change path', {p for s,p in bc} == sourcepaths | set(public) | set(stagepaths))
def tree_entries(c):
    result = {}
    for entry in git('ls-tree','-r','-z',c).split(b'\0'):
        if entry:
            attributes, path = entry.split(b'\t',1)
            result[path.decode()] = attributes.decode()
    return result
ctree, atree = tree_entries(C), tree_entries(ACT)
ck('all candidate file modes/types/blobs preserved outside authorized public10', all(atree.get(p)==attributes for p,attributes in ctree.items() if p not in public))
for x in manifest['normal_native_merges']:
    ck('native parents '+x['result'],git('rev-list','--parents','-n','1',x['result']).decode().split()[1:]==x['parents'])
    ck('native tree '+x['result'],git('rev-parse',x['result']+'^{tree}').decode().strip()==x['tree'])
reportpaths = set()
for x in manifest['candidate_reports']:
    ck('fixed candidate report parent '+x['role'],git('rev-list','--parents','-n','1',x['commit']).decode().split()==[x['commit'],C])
    ck('fixed candidate report tree '+x['role'],git('rev-parse',x['commit']+'^{tree}').decode().strip()==x['tree'])
    rs=changes(C,x['commit'])
    ck('fixed report exact scope '+x['role'],len(rs)==x['path_count'] and all(s=='A' and p.startswith(x['report_directory']) for s,p in rs))
    ck('fixed report entire package preserved '+x['role'],all(blob(x['commit'],p)==blob(ACT,p) for s,p in rs))
    ck('candidate receipt not actual gate '+x['role'],x['actual_gate_satisfied'] is False)
    reportpaths.update(p for s,p in rs)
ck('five report packages independently88',len(reportpaths)==88)
diffs=[]
for a,b in [(BASE,ACT),(C,ACT),(PAY,ACT)]:
    args=['diff','--no-ext-diff','--no-textconv','--no-renames','--binary',a,b]
    bts=git(*args)
    diffs.append(dict(before=a,after=b,command=['git',*args],path_filter_used=False,sha256=sha(bts),bytes=len(bts),lines=bts.count(b'\n'),changed_path_count=len(changes(a,b))))
for n in ['upstream-to-payload-identities.json','candidate-to-payload-identities.json']:
    d=js(ACT,STAGE+n);bts=git(*d['command'][1:])
    ck('payload stream exact '+n,sha(bts)==d['diff_sha256'] and len(bts)==d['diff_bytes'] and bts.count(b'\n')==d['diff_lines'])
    ck('payload inventory exact '+n,changes(d['before_commit'],PAY)==[(x['change'],x['path']) for x in d['changed_paths']])
records=[]
for s,p in bc:
    records.append(dict(status=s,path=p,before=ident(BASE,p) if s=='M' else None,after=ident(ACT,p),candidate=ident(C,p) if git('ls-tree',C,'--',p) else None))
dump('actual-and-complete-paths.json',dict(actual=ACT,candidate=C,predecessor=BASE,actual_parent=PAY,actual_tree=git('rev-parse',ACT+'^{tree}').decode().strip(),full_diff_streams=diffs,all199_paths=records,candidate_actual112=[dict(status=s,path=p) for s,p in cc],normative14=norm,public10=public,stage14=stagepaths,incoming175=sorted(sourcepaths),preserved_reports88=sorted(reportpaths)))

for p in stagepaths:
    if p.endswith('.json'):
        walk(js(ACT,p),'stage/'+p)
    elif p.endswith('.tsv'):
        for row in csv.DictReader(io.StringIO(blob(ACT,p).decode()),delimiter='\t'):
            verify(row,label='current-hashes')
readers=js(ACT,STAGE+'current-readers.json')
ck('current70 no full semantic claim', len(readers['readers'])==70 and readers['full_semantic_coverage_claim'] is False)
ck('current public10 reader versions exact',{x['path'] for x in readers['current_public_versions']}==set(public))
for x in readers['readers']:
    prior = verify(x['reviewed_candidate'], C, 'reader-candidate')
    current = verify(x['actual_current'], ACT, 'reader-current')
    ck('current reader changed flag '+x['path'],x['candidate_to_actual_changed']==(prior['sha256']!=current['sha256']))
dump('current-input-refreeze.json',dict(actual=ACT,all70_identity_only=True,full70_semantic_claim=False,fixed_external_controls_keep_their_explicit_commits=True,readers=[dict(path=x['path'],candidate=verify(x['reviewed_candidate'],C,'reader-output-candidate'),actual=verify(x['actual_current'],ACT,'reader-output-current'),candidate_to_actual_changed=x['candidate_to_actual_changed'],declared_semantic_scope=x['semantic_scope']) for x in readers['readers']],current_public10=[ident(ACT,p) for p in public]))

fp='review/global-independent-review/2026-10-03-fd82a639/findings.json'
ap='review/remediation-20261003-prepare/finding-acceptance.json'
findings={x['id']:x for x in js(F,fp)};acceptance=js(A,ap)
verify(js(ACT,STAGE+'finding-registration.json')['fixed_original_findings_file'],label='immutable original fixed-commit input')
verify(js(ACT,STAGE+'finding-registration.json')['fixed_approved_acceptance_file'],label='immutable acceptance fixed-commit input')
ck('canonical required229',sum(x.get('required_revision') is True for x in findings.values())==229)
reg=js(ACT,STAGE+'finding-registration.json')
ck('current twenty contribution13 primary',len(reg['dispositions'])==20 and sum(x['B09_primary'] for x in reg['dispositions'])==13)
for x in reg['dispositions']:
    f,a=findings[x['id']],acceptance[x['id']]
    ck('current full finding hash '+x['id'],objsha(f)==x['original_complete_object_sha256'])
    ck('current full acceptance hash '+x['id'],objsha(a)==x['acceptance_complete_object_sha256'])
    qualified_fields={'status','required_revision','current_decision','current_qualifications','adjudication_precedence','root_adjudications','effective_case_constraints','extensions','extension_decisions'}
    ck('current control fields complete '+x['id'],set(x['complete_current_control_fields'])==qualified_fields.intersection(f))
    for k,v in x['complete_current_control_fields'].items():
        ck('current final qualified field '+x['id']+':'+k,v==f.get(k))
    for k,v in x['complete_minimum_acceptance_fields'].items():
        ck('current acceptance field '+x['id']+':'+k,v==a.get(k))
    ck('current candidate only no closure '+x['id'],x['candidate']==C and x['canonical_state']=='OPEN' and x['canonical_edited'] is False and x['accepted_B09_contributions']==0 and x['canonical_closure'] is False)
prevcontrols=js(PREVCOM,PREV+'fixed-control-bindings.json')
preserve=js(PREVCOM,PREV+'B07-preservation.json')
dispositions=js(PREVCOM,PREV+'B07-conclusion-dispositions.json')
for x in prevcontrols['B07_records19']:
    ck('B07 full original '+x['id'],objsha(findings[x['id']])==x['complete_original_object_sha256'])
    ck('B07 full acceptance '+x['id'],objsha(acceptance[x['id']])==x['complete_acceptance_object_sha256'])
    for k in ('current_qualifications','effective_case_constraints','root_adjudications','extensions','extension_decisions'):
        if k in x:
            expected=findings[x['id']].get(k)
            if k=='extensions':
                expected=[{key:e.get(key) for key in ('report','raw_id','adjudication','root_review')} for e in expected or []]
            ck('B07 preserved final qualified field '+x['id']+':'+k,x[k]==expected)
ck('B07 nineteen twelve same controls',len(dispositions['records'])==19 and sum(x['B07_primary'] for x in dispositions['records'])==12)
owner=[]
for x in preserve['owner_outputs14']:
    p=x['path'];same=blob(BASE,p)==blob(ACT,p)
    ck('B07 exact candidate actual owner '+p,blob(C,p)==blob(ACT,p))
    owner.append(dict(path=p,baseline=ident(BASE,p),candidate=ident(C,p),actual=ident(ACT,p),whole_predecessor_unchanged=same))
ck('B07 thirteen of fourteen whole unchanged',sum(x['whole_predecessor_unchanged'] for x in owner)==13)
rowchecks=[]
for x in preserve['accepted_rows']:
    p=x['path'];id_=x['id'];lines=blob(ACT,p).decode().splitlines()
    matches=[(i+1,l) for i,l in enumerate(lines) if l.startswith('| '+id_+' |')]
    ck('B07 old accepted exact row '+p+':'+id_, len(matches)==1 and sha(matches[0][1].encode())==x['sha256'])
    rowchecks.append(dict(finding=x['finding'],path=p,id=id_,actual_lines=[i for i,l in matches],sha256=x['sha256']))
ck('B0744 row uses42 unique',len(rowchecks)==44 and len({(x['path'],x['id']) for x in rowchecks})==42)
full19=[]
for x in prevcontrols['B07_records19']:
    now=dict(x)
    now['extensions']=findings[x['id']].get('extensions',[])
    now['full_original_object_locator']=dict(identity=ident(F,fp),object_id=x['id'])
    now['full_acceptance_object_locator']=dict(identity=ident(A,ap),object_id=x['id'])
    now['prior_extension_projection']='Historical record preserved report/raw_id/adjudication/root_review; this current record also restores full extension payload from fixed complete original'
    full19.append(now)
dump('B07-current-preservation.json',dict(actual=ACT,owner14=owner,old_accepted_rows44=rowchecks,all19_complete_controls=full19,fresh_four_cases=['GIR-FD82-B008','GIR-FD82-A047','GIR-FD82-A049','GIR-FD82-B013'],remaining15='Exact unchanged owner/row preservation with prior fixed source evidence, not fresh full-domain behavior reapproval',previous_independent_candidate=ident(PREVCOM,PREV+'report.md')))

for p in public:
    old,now=blob(C,p),blob(ACT,p)
    if p.endswith('.tsv'):
        ck('old150 public byte prefix '+p,now.startswith(old))
        rows=list(csv.DictReader(io.StringIO(now.decode()),delimiter='\t'))
        ck('independent public170 rows '+p,len(rows)==170)
        appended=rows[150:]
        ck('public new twenty exact IDs '+p,{x['finding_id'] for x in appended}=={x['id'] for x in reg['dispositions']})
        ck('public new all canonical OPEN candidate exact '+p,all(x['canonical_state']=='OPEN' and x['candidate_commit']==C for x in appended))
        ck('no wrong B013 normative result imported '+p,all(not any(s in v for s in ['restored to X','later receive Y','two restoration passes']) for x in appended for v in x.values()))
        if p.endswith('approval-ledger.tsv'):
            ck('public B09 primary13',sum('B09_PRIMARY_' in x['accepted_contribution_kind'] for x in appended)==13)
            ck('public B09 gates all blocked actual unreviewed',all(x['downstream_gate']=='BLOCKED' and x['integration_verdict']=='NOT_REVIEWED_PENDING_FIVE_ULTRA_STANDARD' for x in appended))
    elif p.endswith('test-catalog/README.md'):
        # Index ranges are intentionally updated; preserve every other old line in order.
        rlines=[l for l in old.splitlines() if 'pokemon-rules-wp31-32-37-38.md' not in l.decode() and 'combat-requirements-wp39-40-41-42-45.md' not in l.decode()]
        idx=0
        for l in now.splitlines():
            if idx<len(rlines) and l==rlines[idx]:idx+=1
        ck('public catalogue old other lines in order',idx==len(rlines))
    else:
        head,sep,body=old.partition(b'\n\n')
        ck('public historical complete heading/body bytes intact '+p,old in now or (bool(sep) and now.startswith(head+sep) and now.endswith(body)))
    ck('public registration remains five actual/C pending '+p,'PENDING' in now.decode() or '五' in now.decode())

sc=js(ACT,STAGE+'scope-counts.json')
catalogs=[]
for p,claim in sc['catalog_counts'].items():
    def table(c):
        return [(l.split('|')[1].strip(),l) for l in blob(c,p).decode().splitlines() if re.match(r'^\|\s*(?:[A-Z]{1,3}-?\d+[a-z]?)\s*\|',l)]
    old,new=table(BASE),table(ACT);oldmap=dict(old);newmap=dict(new)
    added=[i for i,l in new if i not in oldmap];revised=[i for i,l in old if newmap.get(i)!=l]
    ck('catalog independently counts '+p,(len(old),len(new))==(claim['before'],claim['after']))
    ck('catalog unique old new IDs '+p,len(oldmap)==len(old) and len(newmap)==len(new))
    ck('catalog old order all preserved '+p,[i for i,l in old]==[i for i,l in new if i in oldmap])
    ck('catalog exact added and revised IDs '+p,added==claim['added_ids'] and revised==claim['changed_old_ids'])
    catalogs.append(dict(path=p,before=len(old),after=len(new),added_ids=added,changed_old_ids=revised))
for x in sc['new_static_designs_not_executed']:
    l=blob(ACT,x['path']).decode().splitlines(keepends=True)[x['line']-1]
    ck('new static row exact '+x['id'],sha(l.encode())==x['sha256'] and len(l.encode())==x['bytes'] and x['status']=='STATIC_DESIGN_NOT_EXECUTED')
for x in sc['protected_whole_sections']:
    def section(c):
        t=blob(c,x['path']).decode();start=t.index(x['heading']);end=t.find('\n## ',start+len(x['heading']));return t[start:end+1 if end>=0 else len(t)].encode()
    b=section(ACT)
    ck('protected whole other-owner section '+x['heading'],b==section(BASE) and sha(b)==x['sha256'] and len(b)==x['bytes'])
dump('catalog-current-text-check.json',dict(actual=ACT,catalogs=catalogs,new_unexecuted_IDs24=sum(len(x['added_ids']) for x in catalogs),changed_old_rows10=sum(len(x['changed_old_ids']) for x in catalogs),protected_sections=sc['protected_whole_sections'],behavior_vectors_executed=0))
auth5=js(ACT,B09+'candidate-1/original-scope-approval.json');proposal=js(ACT,B09+'scope-proposal-1/original-sync-proposal.json');auth2=js(ACT,B09+'scope-amendment-2/approval.json')
ck('five scope permission not correctness',auth5['scope_authorized'] is True and auth5['correctness_approval'] is False)
ck('five exact approved checkpoint hash',sha(blob(auth5['approved_checkpoint_sha'],B09+'scope-proposal-1/original-sync-proposal.json'))==auth5['manifest_sha256'])
ck('five approved checkpoint proposal unchanged',blob(auth5['approved_checkpoint_sha'],B09+'scope-proposal-1/original-sync-proposal.json')==blob(ACT,B09+'scope-proposal-1/original-sync-proposal.json'))
for x in proposal['files']:
    verify(x['before'],BASE,label='original-authorized-before',path=x['path']);verify(x['intended_after'],ACT,label='original-authorized-after',path=x['path'])
    ck('five authorized exact patch '+x['path'],sha(blob(ACT,x['complete_diff_path']))==auth5['exact_original_patch_sha256'][x['path']]==x['complete_diff_sha256'])
    ck('five authorized specification patch exact in-memory result '+x['path'],apply_spec_text_patch(blob(BASE,x['path']),blob(ACT,x['complete_diff_path']))==blob(ACT,x['path']))
ck('five originals30 clauses',len(proposal['files'])==5 and sum(len(x['clauses']) for x in proposal['files'])==30)
ck('WP20 scope permission not correctness/public writes',auth2['scope_authorization_only'] is True and auth2['independent_correctness_approval'] is False and auth2['public_registry_write_authorized'] is False)
C1='8ff72341b5b91736970b5bfa5dc1b88137e618a5'
ck('WP20 exact immutable approved proposal',sha(blob(C1,auth2['approved_proposal_path']))==auth2['approved_proposal_sha256'])
for x in auth2['files']:
    p=x['path'];t=blob(C1,p).decode()
    for z in x['clause_changes']:
        ck('WP20 literal before unique '+p+str(z['before_lines']),t.count(z['before_text'])==1)
        t=t.replace(z['before_text'],z['intended_after_text'],1)
    ck('WP20 only two clauses exact actual '+p,len(x['clause_changes'])==2 and t.encode()==blob(ACT,p))
    ck('WP20 authorized patch immutable exact '+p,sha(blob(ACT,B09+'candidate-1/'+x['full_diff']['path']))==auth2['approved_patch_sha256'][p])
    verify(x['intended_after'],ACT,label='WP20-authorized-after',path=p)
dump('approved-scope-current-check.json',dict(actual=ACT,original5=ident(ACT,B09+'candidate-1/original-scope-approval.json'),WP20=ident(ACT,B09+'scope-amendment-2/approval.json'),original5_clauses=30,additional_WP20_original_clauses=2,additional_WP20_final_clauses=2,scope_permission_only=True,chronology_and_leases='AUTHOR_SELF_REPORT_ONLY',six_original_and_eight_final_exact_candidate_bytes=True))
dep=js(ACT,STAGE+'downstream-dependency-assessment.json')
ck('B14 full72 frozen identities',len(dep['B14']['all72_current_assessment_inputs'])==72)
ck('no dispatched author or parallel formal writer',dep['tasks_dispatched']==0 and dep['parallel_formal_writers_authorized']==0)
ck('B14 serialization six cross read/write paths',len(dep['B09_B14_serialization']['B09_writes_B14_reads'])==2 and len(dep['B09_B14_serialization']['B14_writes_B09_reads'])==4 and dep['B09_B14_serialization']['semantic_independence'] is False)
ck('accepted B09 remains0 and parent not performed',manifest['accepted_B09_contributions']==0 and manifest['parent_C']=='NOT_PERFORMED')
ck('five actual gates remain separately pending',len(manifest['actual_gates'])==5 and all(x['status']=='PENDING_SEPARATE_EXACT_ACTUAL' for x in manifest['actual_gates']))
author=js(ACT,STAGE+'validation-results.json')
dump('author-registration-check-comparison.json',dict(actual=ACT,comparison_after_fresh_first_judgment=True,author_result=author['result'],author_checks=len(author['checks']),author_failed=[x for x in author['checks'] if not x['pass_']],author_claims_not_independent_evidence=True,own_check_set_is_distinct=True,source_execution=0,behavior_vectors_executed=0))
dump('git-text-audit-results.json',dict(actual=ACT,mode='FRESH_INDEPENDENT_GIT_JSON_HASH_SPEC_TEXT_BOOKKEEPING_ONLY',check_count=len(checks),passed=sum(x['passed'] for x in checks),failed=[x for x in checks if not x['passed']],checks=checks,reference_execution=0,behavior_vectors_executed=0))
print(json.dumps(dict(check_count=len(checks),failed=[x for x in checks if not x['passed']]),ensure_ascii=False,indent=2))
