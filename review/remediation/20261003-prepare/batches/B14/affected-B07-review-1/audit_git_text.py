"""Own bounded Git/text/JSON/hash audit. No reference program or behavior runs.

Input constants are immutable commits. Patch application below compares prose bytes
in memory only; it never applies a patch to a tracked file or to the reference.
"""
import collections
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = pathlib.Path(__file__).resolve().parent
BASE = '1e6b11a47370f1c7c4659a32443fc1afda597bac'
C1 = '47f7514765f8569ae9172bb06a2cd615e2b83b8a'
C2 = 'af39efbf32549be964cb083bd49bed6d1d5c0d2a'
F = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
A = '41fffb540c6483f5296ea0d33b789b75180d27ed'
PREFIX = 'review/remediation/20261003-prepare/batches/'
B14 = PREFIX + 'B14/'
CONTRACT = PREFIX + 'B09/acceptance-stage-1/B14-downstream-contract.json'
REF = pathlib.Path('/workspace/reference-pokemon-essentials-B07')
REFSHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
checks = []

def git(*args, root=ROOT):
    return subprocess.check_output(['git', '-C', str(root), *args])

def sha(b):
    return hashlib.sha256(b).hexdigest()

def objsha(x):
    return sha(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())

def blob(c, p):
    return git('show', c + ':' + p)

def j(c, p):
    return json.loads(blob(c, p))

def identity(c, p):
    b = blob(c, p)
    return dict(commit=c, path=p, git_blob=git('rev-parse', c + ':' + p).decode().strip(), sha256=sha(b), bytes=len(b))

def check(name, ok, detail=None):
    checks.append(dict(check=name, passed=bool(ok), detail=detail))

def registered(record, c, p=None):
    actual = identity(c, p or record['path'])
    ok = all(record[k] == actual[k] for k in ['git_blob', 'sha256', 'bytes'])
    check('registered byte identity ' + c + ':' + actual['path'], ok)
    return actual

def dump(n, d):
    (OUT / n).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

def changes(a, b):
    raw = git('diff', '--no-ext-diff', '--no-textconv', '--no-renames', '--name-status', '-z', a, b)
    pieces = raw.decode().split('\0')[:-1]
    return [dict(status=pieces[i], path=pieces[i+1]) for i in range(0, len(pieces), 2)]

def rows(c, p):
    result = []
    for i, l in enumerate(blob(c, p).decode().splitlines(), 1):
        m = re.match(r'^\|\s*([A-Z][A-Z0-9-]*\d)\s*\|', l)
        if m:
            result.append(dict(id=m[1], line=i, text=l, sha256=sha(l.encode())))
    return result

def sections(c, p):
    lines = blob(c, p).decode().splitlines(keepends=True)
    starts = [(i,l.strip()) for i,l in enumerate(lines) if l.startswith('## ')]
    return {name: ''.join(lines[i: starts[k+1][0] if k+1<len(starts) else len(lines)]).encode() for k,(i,name) in enumerate(starts)}

def apply_prose_patch(before, patch):
    old = before.decode().splitlines(keepends=True)
    lines = patch.decode().splitlines(keepends=True)
    out, pos, i, hunks = [], 0, 0, []
    while i < len(lines):
        m = re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', lines[i])
        if not m:
            i += 1
            continue
        begin, count, newbegin, newcount = (int(m[1]), int(m[2] or 1), int(m[3]), int(m[4] or 1))
        target = begin-1 if count else begin
        assert target >= pos
        out.extend(old[pos:target]); pos=target; i+=1; seen_old=seen_new=0
        while i<len(lines) and not lines[i].startswith('@@ '):
            l=lines[i]
            if l.startswith(('diff --git ', '--- ', '+++ ')):
                break
            if l.startswith('\\ No newline'):
                raise AssertionError('Unexpected no-newline hunk; audit must handle explicitly')
            assert l[:1] in (' ', '-', '+'), repr(l)
            text=l[1:]
            if l[:1] in (' ', '-'):
                assert old[pos]==text, (begin,pos+1)
                pos+=1;seen_old+=1
            if l[:1] in (' ', '+'):
                out.append(text);seen_new+=1
            i+=1
        assert (seen_old,seen_new)==(count,newcount)
        hunks.append(dict(before_start=begin,before_count=count,after_start=newbegin,after_count=newcount))
    assert hunks
    out.extend(old[pos:])
    return ''.join(out).encode(), hunks

head=git('rev-parse','HEAD').decode().strip()
head_scoped=(head==C2 or (git('show','-s','--format=%P',head).decode().strip()==C2 and all(x['status']=='A' and x['path'].startswith(str(OUT.relative_to(ROOT))+'/') for x in changes(C2,head))))
check('current checkout is C2 or its report-only single-parent successor',head_scoped)
check('candidate2 single parent candidate1',git('show','-s','--format=%P',C2).decode().strip()==C1)
check('accepted predecessor ancestor',subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',BASE,C2]).returncode==0)
check('exact readonly reference HEAD',git('rev-parse','HEAD',root=REF).decode().strip()==REFSHA)
check('reference clean tracked/untracked state',git('status','--porcelain=v1','--untracked-files=all',root=REF)==b'')

contract=j(C2,CONTRACT)
check('contract unchanged at accepted predecessor',blob(BASE,CONTRACT)==blob(C2,CONTRACT))
findings={x['id']:x for x in j(F,'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
acceptance=j(A,'review/remediation-20261003-prepare/finding-acceptance.json')
registered(contract['fixed_original_findings'],F)
registered(contract['fixed_approved_acceptance'],A)
control_results=[]
for x in contract['contribution_controls']:
    id_=x['id'];f=findings.get(id_)
    ac=acceptance[id_]
    # Intake entries use the full contract's fixed scope rather than a nonexistent GIR record.
    if f is not None:
        check('full F object '+id_,objsha(f)==x['whole_original_object_sha256'])
        for key,value in x['complete_current_control_fields'].items():
            check('current qualification/control '+id_+':'+key, f.get(key)==value)
    check('full A object '+id_,objsha(ac)==x['whole_acceptance_object_sha256'])
    control_results.append(dict(id=id_,whole_original_object_sha256=x['whole_original_object_sha256'],whole_acceptance_object_sha256=objsha(ac),primary=x['primary'],semantic_status='C003 B07 slice freshly reviewed; remaining B14 controls identity/scope binding only'))

reads=[]
for x in contract['planned_reads']:
    r=x['accepted_current_input'];p=x['path'];c=r.get('commit',BASE)
    actual=registered(r,c,p)
    reads.append(dict(planned_index=x['planned_index'],input=actual,candidate2=identity(C2,p) if c==BASE else None,semantic_read_claim=False))
check('contract planned count72',len(reads)==72)
refreeze=j(C2,B14+'author-stage-1/input-refreeze.json')
for x in refreeze['planned_reads']:
    registered(x,x.get('verified_commit',x.get('commit',BASE)))

diffs=[]
for a,b in [(BASE,C2),(C1,C2)]:
    args=['diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index',a,b]
    stream=git(*args);cs=changes(a,b)
    for x in cs:
        if x['status']!='A': x['before']=identity(a,x['path'])
        if x['status']!='D': x['after']=identity(b,x['path'])
    diffs.append(dict(before=a,after=b,command=['git',*args],path_filter_used=False,sha256=sha(stream),bytes=len(stream),lines=stream.count(b'\n'),status_counts=dict(collections.Counter(x['status'] for x in cs)),paths=cs))
dump('complete-diff-identities.json',dict(candidate_tree=git('rev-parse',C2+'^{tree}').decode().strip(),diffs=diffs))
norm=[x for x in diffs[0]['paths'] if x['status']=='M']
newrecords=[x for x in diffs[0]['paths'] if x['status']=='A']
expected=set(contract['allowed_formal_write_paths'])
proposal=j(C2,B14+'scope-proposal-1/scope-manifest.json')
expected.update(x['path'] for x in proposal['records'])
expected.update(['specs/overworld/wp16-world-rendering-and-visual-transitions.md','deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md'])
check('complete12 normative paths authorized exact set',{x['path'] for x in norm}==expected)
check('all added paths only local B14 author evidence',all(x['path'].startswith(B14+('author-stage-1','candidate-1','candidate-2','scope-proposal-1')[0]) or any(x['path'].startswith(B14+n+'/') for n in ['candidate-1','candidate-2','scope-proposal-1']) for x in newrecords))
check('candidate1-to-candidate2 exactly8 normative M and14 evidence A',diffs[1]['status_counts']=={'M':8,'A':14})
check('candidate1-to-candidate2 additions only candidate2',all(x['path'].startswith(B14+'candidate-2/') for x in diffs[1]['paths'] if x['status']=='A'))
check('no deletes renames modes outside bounded M/A',all(x['status'] in ('M','A') for d in diffs for x in d['paths']))
check('no public/formal scope/registry or unrelated tracked changes',all(x['path'] in expected or x['path'].startswith(B14) for x in diffs[0]['paths']))
before20=git('ls-tree','-r','--name-only',C1,'--',B14).decode().splitlines()
check('earlier B14 evidence all immutable',all(blob(C1,p)==blob(C2,p) for p in before20))

amend=j(C2,B14+'candidate-2/bounded-amendment-1.json')
application=j(C2,B14+'candidate-2/amendment-application.json')
patches=[]
for x in proposal['records']:
    p=x['path'];registered(x['before'],BASE,p);registered(x['intended_after'],C1,p)
    q=B14+'scope-proposal-1/'+x['complete_diff'];patch=blob(C2,q)
    check('approved original proposal patch unchanged from fixed proposal '+q,patch==blob('b37533ef1cfc7808ed41d64215647a78d165ada4',q))
    check('approved original patch sha '+q,sha(patch)==x['diff_sha256'])
    after,hunks=apply_prose_patch(blob(BASE,p),patch)
    check('approved original exact complete patch result '+p,after==blob(C1,p))
    patches.append(dict(path=p,stage='approved initial four original patches BASE→C1',patch=identity(C2,q),hunks=hunks,exact_after=True))
for x in amend['documents']:
    p=x['path'];registered(x['before'],C1,p);registered(x['intended_after'],C2,p)
    q=B14+'candidate-2/'+x['patch'];patch=blob(C2,q)
    check('bounded amendment patch sha '+q,sha(patch)==x['patch_sha256'])
    after,hunks=apply_prose_patch(blob(C1,p),patch)
    check('bounded exact complete patch result '+p,after==blob(C2,p))
    patches.append(dict(path=p,stage='explicit narrow C2 amendment',patch=identity(C2,q),hunks=hunks,exact_after=True,bounded_scope=x['bounded_scope']))
registered(application['before_application_record'],C2)
for x in application['documents']:registered(x['actual_after'],C2,x['path'])
revised=j(C2,B14+'candidate-2/revised-identities.json')
for x in revised['documents']:
    registered(x['accepted_B09_before'],BASE,x['path']);registered(x['candidate1_before'],C1,x['path']);registered(x['after'],C2,x['path'])
    check('changed flag '+x['path'],x['changed_in_candidate2']==(blob(C1,x['path'])!=blob(C2,x['path'])))
q=B14+'candidate-2/'+revised['original_FLY_amendment_patch'];patch=blob(C2,q)
check('additional original FLY amendment sha',sha(patch)==revised['original_FLY_patch_sha256'])
p='specs/overworld/wp59-world-time-weather-field-moves.md';after,hunks=apply_prose_patch(blob(C1,p),patch)
check('additional original FLY exact patch result',after==blob(C2,p))
patches.append(dict(path=p,stage='explicit C2 FLY original amendment',patch=identity(C2,q),hunks=hunks,exact_after=True))
origapp=j(C2,B14+'author-stage-1/original-application.json')
for x in origapp['application']:registered(x['before'],BASE,x['path']);registered(x['actual_after'],C1,x['path'])
registered(revised['earlier_original_application'],C1)
fix=j(C2,B14+'candidate-2/fix-response.json')
for x in fix['review_inputs']:registered(x,x['commit'])
for x in fix['successor_local_traceability']:registered(x['old_entry'],C1)
dump('authorization-and-patch-checks.json',dict(permission_basis='Explicit parent delegated narrow authorization; immutable proposed/appended identities independently matched. Authorization is not correctness evidence. Git verifies bytes but cannot independently timestamp an uncommitted before-application action.',initial_original_count=4,narrow_WP16_pair_count=2,total_original_count=5,total_final_count=7,patches=patches,earlier_B14_evidence_file_count=len(before20),earlier_approval_record_unchanged=blob(C1,B14+'author-stage-1/original-application.json')==blob(C2,B14+'author-stage-1/original-application.json')))

catalogs=contract['allowed_formal_write_paths'][-2:]
catchecks=[]
for p in catalogs:
    rr={c:rows(c,p) for c in [BASE,C1,C2]}
    for c,r in rr.items():check('unique full catalog IDs '+c+':'+p,len(r)==len({x['id'] for x in r}))
    vals=[]
    for a,b in [(BASE,C2),(C1,C2)]:
        old,new=rr[a],rr[b];oldids=[x['id'] for x in old];newids=[x['id'] for x in new]
        check('all old ID order and multiplicity retained '+a+'→'+b+':'+p,[x for x in newids if x in oldids]==oldids)
        nm={x['id']:x for x in new};changed=[dict(id=x['id'],before_line=x['line'],after_line=nm[x['id']]['line'],before_sha256=x['sha256'],after_sha256=nm[x['id']]['sha256']) for x in old if x['text']!=nm[x['id']]['text']]
        added=[dict(id=x['id'],line=x['line'],sha256=x['sha256']) for x in new if x['id'] not in oldids]
        vals.append(dict(before=a,after=b,old_count=len(old),new_count=len(new),changed_rows=changed,added_rows=added))
    ss={c:sections(c,p) for c in [BASE,C1,C2]}
    protected=[]
    for heading,bts in ss[BASE].items():
        keep=(p==catalogs[1] and re.match(r'^## (SF|PD|VF|LT)：',heading)) or (p==catalogs[0] and not re.match(r'^## (I\.|J\.)',heading))
        if keep:
            ok=all(ss[c].get(heading)==bts for c in [C1,C2]);check('entire protected owner section '+heading,ok)
            protected.append(dict(heading=heading,sha256=sha(bts),bytes=len(bts),unchanged=ok))
    catchecks.append(dict(path=p,comparisons=vals,protected_whole_sections=protected))
check('candidate1-to-candidate2 catalog row edits exactly WT28/BP18',set(x['id'] for c in catchecks for x in c['comparisons'][1]['changed_rows'])=={'WT28','BP18'})
check('candidate1-to-candidate2 additions exactly WT39/40',set(x['id'] for c in catchecks for x in c['comparisons'][1]['added_rows'])=={'WT39','WT40'})
dump('whole-catalog-preservation.json',dict(catalogs=catchecks,protected_pokemon_rows_count=sum(len([x for x in rows(C2,catalogs[1]) if x['id'].startswith(q)]) for q in ['SF','PD','VF','LT'])))

prior=j(C2,PREFIX+'B09/affected-B07-integration-review-1/B07-current-preservation.json')
owner=[]
for x in prior['owner14']:
    p=x['path'];ok=blob(BASE,p)==blob(C1,p)==blob(C2,p);check('B07 whole owner file unchanged '+p,ok)
    owner.append(dict(path=p,baseline=identity(BASE,p),candidate2=identity(C2,p),unchanged=ok,disposition='NOT_AFFECTED_BY_EXACT_BYTE_AND_CALLER_COMPARISON'))
rowchecks=[]
for x in prior['old_accepted_rows44']:
    p=x['path'];id_=x['id'];matches=[v for v in rows(C2,p) if v['id']==id_]
    ok=len(matches)==1 and matches[0]['sha256']==x['sha256'];check('B07 accepted exact row '+p+':'+id_,ok)
    rowchecks.append(dict(finding=x['finding'],path=p,id=id_,current_lines=[v['line'] for v in matches],sha256=x['sha256'],unchanged=ok))
b07controls=[]
for x in prior['all19_complete_controls']:
    id_=x['id'];f=findings[id_];ac=acceptance[id_]
    check('B07 complete F '+id_,objsha(f)==x['complete_original_object_sha256'])
    check('B07 complete A '+id_,objsha(ac)==x['complete_acceptance_object_sha256'])
    for k in ['current_qualifications','effective_case_constraints','root_adjudications','extensions','minimum_revision','determinate_recheck']:
        if k in x:
            # The preceding reviewer explicitly recorded absent extension arrays as [].
            # Full canonical-object hashes above still retain absence versus presence.
            value=f.get(k, [] if k=='extensions' else None)
            check('B07 entire preserved control '+id_+':'+k,value==x[k])
    b07controls.append(dict(id=id_,complete_original_object_sha256=objsha(f),complete_acceptance_object_sha256=objsha(ac),status='C003 B07 shared slice/source callers freshly checked; other owner conclusions preserved by exact owner/accepted-row/control identities, not fresh global reapproval'))
c003=findings['GIR-FD82-C003'];ac003=acceptance['GIR-FD82-C003']
dump('fixed-C003-control.json',dict(fixed_original=identity(F,contract['fixed_original_findings']['path']),fixed_acceptance=identity(A,contract['fixed_approved_acceptance']['path']),complete_original_object_sha256=objsha(c003),complete_acceptance_object_sha256=objsha(ac003),root_count=len(c003['root_adjudications']),extension_count=len(c003['extensions']),current_control_fields={k:c003.get(k) for k in ['current_qualifications','effective_case_constraints','adjudication_precedence','root_adjudications','extensions','extension_decisions','minimum_revision','determinate_recheck','evidence_limits']},acceptance_current_control=ac003,semantic_review_boundary='Only B07 cross-domain slice and three explicitly authorized narrow additions freshly reviewed. Other C003 roots/extensions remain OPEN with complete qualifiers preserved, not approved/closed here.'))
dump('B07-preservation-and-refreeze.json',dict(accepted_predecessor=BASE,candidate2=C2,owner14=owner,old_accepted_row_uses44=rowchecks,distinct_accepted_row_count=len({(x['path'],x['id']) for x in rowchecks}),complete_controls19=b07controls,planned72_identity_checks=reads,planned72_semantic_read_claim=False))

contrib=j(C2,B14+'candidate-1/contributions.json')
check('24 contributions19 primary unchanged',len(contrib['contributions'])==24 and sum(x['primary'] for x in contrib['contributions'])==19 and contrib['contribution_count']==24 and contrib['primary_count']==19)
check('fixed global denominator229 required and4 nonrequired',sum(bool(x.get('required_revision')) for x in findings.values())==229 and len(findings)==233)
check('all canonical contribution states OPEN',all(x['canonical_state']=='OPEN' for x in contrib['contributions']))
check('canonical denominator retained229 OPEN0 CLOSED',contrib['canonical_required_OPEN']==229 and contrib['canonical_CLOSED']==0 and fix['canonical_required_OPEN']==229 and fix['canonical_CLOSED']==0)
for x in contrib['contributions']:
    b=x['complete_control_binding'];id_=x['id']
    if id_ in findings:check('author complete original control '+id_,b['whole_original_object_sha256']==objsha(findings[id_]))
    check('author complete acceptance control '+id_,b['whole_acceptance_object_sha256']==objsha(acceptance[id_]))

# Parse all newly added bookkeeping JSON without invoking any author verifier.
# This is document syntax/identity bookkeeping, never a reference binary loader.
for x in newrecords:
    if x['path'].endswith('.json'):
        data=j(C2,x['path'])
        check('all added JSON is syntactically readable '+x['path'],isinstance(data,(dict,list)))

log=[json.loads(l) for l in pathlib.Path('/tmp/b14_r07_static_read_log.jsonl').read_text().splitlines()]
source_summary=[]
for p in sorted({x['path'] for x in log}):
    b=(REF/p).read_bytes();ranges=[r for x in log if x['path']==p for r in x['ranges']]
    for x in [x for x in log if x['path']==p]:check('fresh source bytes '+p,sha(b)==x['sha256'] and len(b)==x['bytes'] and x['commit']==REFSHA)
    source_summary.append(dict(commit=REFSHA,path=p,git_blob=git('rev-parse',REFSHA+':'+p,root=REF).decode().strip(),sha256=sha(b),bytes=len(b),lines=len(b.decode().splitlines()),ranges=ranges,full_file_semantic_read_claim=False))
dump('fresh-source-reading-log.json',dict(reference_commit=REFSHA,reference_tree=git('rev-parse',REFSHA+'^{tree}',root=REF).decode().strip(),reader='Own static UTF8 numbered-range text reader; no reference functions, programs or behavior vectors executed.',files=source_summary,events=log,read_limit='Only displayed ranges support fresh semantic claims; one truncated combined output was followed by focused rereads. Unlisted source files/ranges remain unread.'))
(OUT/'read_reference_text.py').write_bytes(pathlib.Path('/tmp/b14_r07_static_read.py').read_bytes())
normpaths=[x['path'] for x in norm]
normstream=git('diff','--no-ext-diff','--no-textconv','--no-renames','--full-index',BASE,C2,'--',*normpaths)
(OUT/'complete-normative.diff').write_bytes(normstream)
white=subprocess.run(['git','-C',str(ROOT),'diff','--check',BASE,C2],capture_output=True)
warnings=white.stdout.decode().splitlines()
locations=[l.split(':',1)[0] for l in warnings if ': trailing whitespace.' in l or ': new blank line at EOF.' in l]
check('complete whitespace output only exact prose patch context/EOF',bool(locations) and all(p.startswith(B14) and p.endswith('.patch') for p in locations))
check('actual normative specification whitespace clean',subprocess.run(['git','-C',str(ROOT),'diff','--check',BASE,C2,'--',*normpaths],capture_output=True).returncode==0)
dump('whitespace-boundary.json',dict(complete_exit_code=white.returncode,complete_output=warnings,warning_paths=sorted(set(locations)),qualification='The full unfiltered check is nonzero because newly stored unified patches preserve space-prefixed blank context lines and context EOF. Exact patch reproduction passed. Actual12 normative files are clean. Do not trim immutable approved patch bytes.',normative_clean=True))
dump('git-text-audit-results.json',dict(status='PASS' if all(x['passed'] for x in checks) else 'FAIL',checks=checks,check_count=len(checks),failures=[x for x in checks if not x['passed']],full_unfiltered_diffs=2,normative_diff_identity=dict(sha256=sha(normstream),bytes=len(normstream),paths=normpaths),scope='Git/text/JSON/hash bookkeeping only. No game/reference behavior tests.'))
print(json.dumps(dict(status='PASS' if all(x['passed'] for x in checks) else 'FAIL',checks=len(checks),failures=[x for x in checks if not x['passed']],diff_counts=[x['status_counts'] for x in diffs],normative_diff_bytes=len(normstream),catalog_counts=[[(x['old_count'],x['new_count']) for x in c['comparisons']] for c in catchecks]),ensure_ascii=False))
