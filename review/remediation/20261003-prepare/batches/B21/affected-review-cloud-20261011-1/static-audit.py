#!/usr/bin/env python3
"""New read-only Git/document metadata audit; never runs project/reference code."""
import collections, csv, hashlib, io, json, subprocess
from pathlib import Path

C = 'e9c140dc33de1cb0662521318b051174909e4509'
N = '5c3e19831e1e29450247fa6061f3c2feac2f893e'
P = 'fa5e1d876c9082797d6eb71f1590f3d8d9a19b0a'
D = 'eb1885265fcde2a52767077de3193862036c3a71'
B = 'review/remediation/20261003-prepare/'
A = B + 'batches/B21/author-draft-1/'
F = A + 'freeze-1/'
Q = B + 'batches/B21/refreeze-after-B20-C-1/'
cache = {}
def git(*args):
    return subprocess.check_output(['git', *args])
def raw(s, p):
    k = (s, p)
    if k not in cache: cache[k] = git('show', s + ':' + p)
    return cache[k]
def doc(s, p): return json.loads(raw(s, p))
def sha(b): return hashlib.sha256(b).hexdigest()
def canonical(o): return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()
def objhash(o): return sha(canonical(o))
def ident(s, p):
    r = raw(s, p)
    return dict(commit=s, path=p, git_blob=git('rev-parse', s+':'+p).decode().strip(), sha256=sha(r), bytes=len(r))
def pointer(x, p):
    for t in p.split('/')[1:]:
        t=t.replace('~1','/').replace('~0','~')
        x=x[int(t)] if isinstance(x,list) else x[t]
    return x
def rows(s, p): return list(csv.DictReader(io.StringIO(raw(s,p).decode()), delimiter='\t'))

freeze = doc(P, F+'frozen-NEW.json')
contract = doc(D,Q+'author-contract.json')
inputs = doc(D,Q+'input-identities.json')
deps = doc(D,Q+'accepted-dependency-map.json')
oblig = doc(D,Q+'current229-statistics-and-obligations.json')
stats_path=B+'batches/B20/acceptance-stage-1/completion-statistics-successor.json'
stats=doc(C,stats_path)
receipts=stats['accepted_contribution_receipts']
pres=doc(N,A+'accepted-result-preservation.json')
errors=[]
checks=[]
def check(name, condition, **evidence):
    checks.append(dict(check=name, satisfied=bool(condition), **evidence))
    if not condition: errors.append(name)

commits=[]
for s,t in [(C,'5baa01c8a604400b73f560bb06fa5d770089502a'),(N,'98062bf1205669936426ae870913e578528b740c'),(P,'de3dae76d08f1d08e54f78fe95a185211a63d14a'),(D,'c85948f536d7444bfe83d3c323ea6a48ba15d143')]:
    fields=git('show','-s','--format=%H %T %P',s).decode().strip().split()
    commits.append(dict(commit=fields[0],tree=fields[1],parents=fields[2:]))
    check('commit_tree_'+s,fields[1]==t)
check('NEW_sole_parent_C',commits[1]['parents']==[C])
rebuilt=git('-c','core.quotePath=true','diff','--no-ext-diff','--binary','--full-index',C,N)
stored=raw(P,F+'complete-C-to-NEW.diff')
check('unfiltered_binary_full_index_diff_exact',rebuilt==stored,rebuilt_sha256=sha(rebuilt),bytes=len(rebuilt),published_identity=ident(P,F+'complete-C-to-NEW.diff'),copied_to_report=False)
changed=git('diff','--name-status',C,N).decode().splitlines()
paths=[line.split('\t')[-1] for line in changed]
formal=contract['formal_write_paths_now']
check('all_formal_outputs_in_delta',set(formal)<=set(paths))
extras=set(paths)-set(formal)
check('only_author_evidence_extra',all(p.startswith(A) and not p.startswith(F) for p in extras),changed_path_count=len(paths),formal_path_count=len(formal),extra_paths=sorted(extras))
output_ids=[]
for r in freeze['all22_outputs']:
    actual=ident(N,r['path'])
    check('frozen_output_'+r['path'],actual==r['after'])
    if r['before'].get('exists') is not False: check('frozen_before_'+r['path'],ident(C,r['path'])==r['before'])
    check('published_formal_output_unchanged_'+r['path'],raw(N,r['path'])==raw(P,r['path']))
    output_ids.append(actual)

# Every read listed by dispatch is verified from its own pinned commit.
input_ids=[]
for r in inputs['complete_planned_reads']:
    i=r['input']; actual=ident(i['commit'],i['path'])
    check('input_identity_'+str(r['planned_index']),actual==i)
    input_ids.append(actual)

# Recursively verify project identity references, once per identity, without claiming
# full semantic reading of all historical documents or any reference source samples.
references={}
def walk(x):
    if isinstance(x,dict):
        if all(k in x for k in ['commit','path','git_blob','sha256','bytes']) and x.get('repository','project')=='project':
            references[(x['commit'],x['path'])]={k:x[k] for k in ['commit','path','git_blob','sha256','bytes']}
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
for p in git('ls-tree','-r','--name-only',N,A).decode().splitlines():
    if p.endswith('.json'): walk(doc(N,p))
for p in git('ls-tree','-r','--name-only',D,Q).decode().splitlines():
    if p.endswith('.json'): walk(doc(D,p))
verified_refs=[]
for (s,p),i in sorted(references.items()):
    try:
        actual=ident(s,p)
        if actual!=i: errors.append('bound_identity_'+s+':'+p)
        verified_refs.append(dict(**actual,matches=actual==i))
    except Exception as e:
        errors.append('unreadable_identity_'+s+':'+p)
        verified_refs.append(dict(**i,matches=False,error=str(e)))

# Preserve original receipts as whole objects and both old TSV byte prefixes.
hashes=[dict(index=j,batch=r['batch'],id=r['id'],sha256=objhash(r)) for j,r in enumerate(receipts)]
check('all327_receipt_object_hashes',hashes==pres['receipt_object_hashes'],receipt_count=len(receipts),array_sha256=objhash(receipts))
check('receipt_array_hash',objhash(receipts)==pres['receipt_array_canonical_sha256'])
check('accepted_statistics_unchanged_C_NEW_P',raw(C,stats_path)==raw(N,stats_path)==raw(P,stats_path),identity=ident(C,stats_path))
tsv=[]
for p in ['approval-ledger.tsv','traceability-successor.tsv']:
    old=raw(C,B+p); new=raw(N,B+p)
    oldrows=rows(C,B+p); newrows=rows(N,B+p)
    check('old_327_TSV_bytes_'+p,new.startswith(old),old_rows=len(oldrows),new_rows=len(newrows),old_identity=ident(C,B+p),new_identity=ident(N,B+p))
    added=newrows[len(oldrows):]
    check('new14_pending_OPEN_'+p,len(added)==14 and all(r['canonical_state']=='OPEN' for r in added) and all(not r['candidate_review_commit'] for r in added))
    tsv.append(dict(path=B+p,original_byte_prefix_preserved=new.startswith(old),old_rows=len(oldrows),added_rows=len(added),added_finding_ids=[r['finding_id'] for r in added]))
oldrows=rows(C,B+'finding-ledger.tsv'); newrows=rows(N,B+'finding-ledger.tsv')
assigned=set(oblig['remaining14_exactly_B21_contributions'])
changes=[]
for before,after,oldline,newline in zip(oldrows,newrows,raw(C,B+'finding-ledger.tsv').splitlines()[1:],raw(N,B+'finding-ledger.tsv').splitlines()[1:]):
    keys=[k for k in before if before[k]!=after[k]]
    if keys: changes.append(dict(id=before['finding_id'],changed_fields=keys,old_row_sha256=sha(oldline),new_row_sha256=sha(newline)))
    if before['finding_id'] not in assigned: check('unassigned229_row_'+before['finding_id'],oldline==newline)
    else: check('assigned14_closure_gate_only_'+before['finding_id'],keys==['closure_gate'] and after['closure_gate'].startswith(before['closure_gate']) and after['canonical_state']=='OPEN')
check('all229_rows_same_order_OPEN',len(oldrows)==len(newrows)==229 and [r['finding_id'] for r in oldrows]==[r['finding_id'] for r in newrows] and all(r['canonical_state']=='OPEN' for r in newrows),changed_rows=changes)

dependency_checks=[]
for dep in deps['dependencies']:
    own=[r for r in receipts if r['batch']==dep['batch']]
    bound=[pointer(doc(x['commit'],x['path']),x['pointer']) for x in dep['accepted_receipt_bindings']]
    check('dependency_receipts_'+dep['batch'],own==bound==dep['exact_candidate_actual_and_independent_report_fields'])
    dependency_checks.append(dict(batch=dep['batch'],receipt_count=len(own),primary_count=sum(r['primary'] for r in own),bound_whole_objects_match=own==bound,receipt_object_hashes=[x for x in hashes if x['batch']==dep['batch']],dependency_dispatch_pointer='/dependencies/'+str(len(dependency_checks))))
check('all20_dependencies_exact_set',{d['batch'] for d in deps['dependencies']}=={f'B{i:02d}' for i in range(1,21)})

# All immutable historical paths in C remain byte-identical by tree object identity.
def tree(s):
    return {line.split('\t',1)[1]:line.split('\t',1)[0] for line in git('ls-tree','-r',s).decode().splitlines()}
tc,tn=tree(C),tree(N)
protected=[]
for p in tc:
    history=(p.startswith('review/') and not p.startswith(B)) or p.startswith(B+'batches/B') and not p.startswith(B+'batches/B21/')
    invariant=p.startswith(('specs/','reference/')) or p=='AGENTS.md' or (p.startswith('deliverables/final-specification-set/') and p not in formal)
    if history or invariant: protected.append(p)
mismatch=[p for p in protected if tc[p]!=tn.get(p)]
check('historical_body_test_specs_reference_AGENTS_tree_identity',not mismatch,protected_path_count=len(protected),mismatches=mismatch,method='mode/type/Git-object identity comparison; unchanged fixed evidence reuse, not fresh semantic reread')
mdprefix=[]
for p in formal:
    if p.endswith('.md'):
        old=raw(C,p);new=raw(N,p)
        check('old_markdown_contiguous_'+p,old in new)
        mdprefix.append(dict(path=p,old_contiguous_bytes_retained=old in new,old_sha256=sha(old),new_sha256=sha(new)))
for p in ['candidate-manifest.json','global-premises.json','integration-manifest.json','model-request-receipts.json','scope-counts.json']:
    before=doc(C,B+p); after=doc(N,B+p)
    check('historical_json_fields_'+p,all(after[k]==v for k,v in before.items()),preserved_top_level_fields=list(before))

# Independently derive accepted coverage from required contributor lists and receipt set.
receipt_set={(r['batch'],r['id']) for r in receipts}
ids={r['id'] for r in receipts}; primary={r['id'] for r in receipts if r['primary']}
strict=[r['id'] for r in oblig['all229_records'] if all((b,r['id']) in receipt_set for b in r['all_contributors'])]
pending=[(b,r['id']) for r in oblig['all229_records'] for b in r['all_contributors'] if (b,r['id']) not in receipt_set]
derived=dict(accepted_contributions=len(receipts),accepted_batches=len({r['batch'] for r in receipts}),touched_ids=len(ids),primary_minima=len(primary),strict_whole_required_controls=len(strict),pending_contributions=len(pending),pending_primary=sum(r['primary_owner']=='B21' for r in oblig['all229_records']),canonical_OPEN=len(newrows),canonical_CLOSED=0)
check('independent_statistics_derivation',derived==dict(accepted_contributions=327,accepted_batches=20,touched_ids=228,primary_minima=220,strict_whole_required_controls=215,pending_contributions=14,pending_primary=9,canonical_OPEN=229,canonical_CLOSED=0),derived=derived,pending=[dict(batch=b,id=i) for b,i in pending])

result=dict(scope='B21 affected static metadata audit; not behavior execution or independent FULL/actual/FINAL signature',C=C,NEW=N,P=P,D=D,commit_identities=commits,checks=checks,identity_reference_checks=verified_refs,dispatch_input_identities=input_ids,formal_output_identities=output_ids,old_receipt_hashes=hashes,dependency_preservation=dependency_checks,TSV_preservation=tsv,old_markdown_preservation=mdprefix,derived_statistics=derived,errors=errors,project_reference_code_executed=False,static_cases_executed=False)
Path('/tmp/b21-static-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),fixed_identity_references=len(verified_refs),protected_paths=len(protected),errors=errors,derived_statistics=derived),ensure_ascii=False))
