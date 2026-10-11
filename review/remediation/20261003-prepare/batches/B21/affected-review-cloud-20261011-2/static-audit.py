#!/usr/bin/env python3
"""New NEW2 read-only Git/document audit; no project/reference program execution."""
import collections, csv, difflib, hashlib, io, json, pathlib, subprocess
C='e9c140dc33de1cb0662521318b051174909e4509'
N='e58486178e746273fb6fab55df00722807f1dc44'
P='9b6d16e34daf59e205f8a3df20e24930175064ed'
OLD='5c3e19831e1e29450247fa6061f3c2feac2f893e'
R1='7db07543137cc11ef76b725e0a3c8975796bc7b0'
D='eb1885265fcde2a52767077de3193862036c3a71'
G='aa57e293bf3a0a77fa42f1f42777df88cbd2fbe8'
B='review/remediation/20261003-prepare/'
A=B+'batches/B21/author-draft-1/'
F=A+'freeze-2/'
Q=B+'batches/B21/refreeze-after-B20-C-1/'
cache={}
def git(*args):return subprocess.check_output(['git',*args])
def raw(s,p):
    key=(s,p)
    if key not in cache:cache[key]=git('show',s+':'+p)
    return cache[key]
def doc(s,p):return json.loads(raw(s,p))
def sha(b):return hashlib.sha256(b).hexdigest()
def objsha(o):return sha(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def ident(s,p):
    b=raw(s,p)
    return dict(commit=s,path=p,git_blob=git('rev-parse',s+':'+p).decode().strip(),sha256=sha(b),bytes=len(b))
def ptr(o,p):
    for k in p.split('/')[1:]:
        k=k.replace('~1','/').replace('~0','~');o=o[int(k)] if isinstance(o,list) else o[k]
    return o
def tsv(s,p):return list(csv.DictReader(io.StringIO(raw(s,p).decode()),delimiter='\t'))
checks=[];errors=[]
def check(name,ok,**e):
    checks.append(dict(check=name,satisfied=bool(ok),**e))
    if not ok:errors.append(name)
freeze=doc(P,F+'frozen-NEW2.json')
grant=doc(G,B+'batches/B21/original-scope-grant-R-B21-006-1/scope-grant.json')
contract=doc(D,Q+'author-contract.json')
deps=doc(D,Q+'accepted-dependency-map.json')
oblig=doc(D,Q+'current229-statistics-and-obligations.json')
stats_path=B+'batches/B20/acceptance-stage-1/completion-statistics-successor.json'
stats=doc(C,stats_path);receipts=stats['accepted_contribution_receipts']
pres=doc(N,A+'accepted-result-preservation.json')
fixed_trees={C:'5baa01c8a604400b73f560bb06fa5d770089502a',N:'1dbe28a733bfde428129ed662d7e0d66243978c4',P:'11c07f505fc57d62ffd0bf643a1ea0b575a3fd8d',D:'c85948f536d7444bfe83d3c323ea6a48ba15d143',G:'d1333b17eb6987d51dac40988d7d0e744b2ed677',R1:'16cdcc4016407cbe1d58ede64f745090b2282b21'}
commits=[]
for s,t in fixed_trees.items():
    f=git('show','-s','--format=%H %T %P',s).decode().split();commits.append(dict(commit=f[0],tree=f[1],parents=f[2:]));check('tree_'+s,f[1]==t)
check('NEW2_exact_parent',commits[1]['parents']==['a740b86cb6b721c61e23fbcea5e365180fc4523e'])
rebuilt=git('-c','core.quotePath=true','diff','--no-ext-diff','--binary','--full-index',C,N)
published=raw(P,F+'complete-C-to-NEW2.diff')
check('independent_full_unfiltered_diff_exact',rebuilt==published and len(rebuilt)==4541616 and sha(rebuilt)=='0213e85fbe687500343f9e3848b49650bafdb7a726cac8beb54f083ee7e41b15',published_identity=ident(P,F+'complete-C-to-NEW2.diff'),independent_bytes=len(rebuilt),independent_sha256=sha(rebuilt),copied_to_report=False)
formal=set(contract['formal_write_paths_now'])
granted={r['path'] for r in grant['authorized_paths']}
allowed=formal|granted
changed=git('diff','--name-status',C,N).decode().splitlines();paths={r.split('\t')[-1] for r in changed}
check('57_paths_exact_scope',len(formal)==22 and len(granted)==3 and len(allowed)==25 and allowed<=paths and len(paths)==57 and all(p.startswith(A) for p in paths-allowed),formal_paths=sorted(formal),granted_paths=sorted(granted),author_evidence_paths=sorted(paths-allowed))
outputs=[]
for r in freeze['all25_output_identities']:
    actual=ident(N,r['path']);outputs.append(actual)
    check('output_after_'+r['path'],actual==r['after_NEW2'] and raw(N,r['path'])==raw(P,r['path']))
    before=r['before_C']
    if before is not None and before.get('exists') is not False:check('output_before_'+r['path'],ident(C,r['path'])==before)
check('all25_output_set',set(r['path'] for r in outputs)==allowed)
scope_changes=[]
for r in grant['authorized_paths']:
    p=r['path'];after=r['after'];before=raw(C,p);new=raw(N,p)
    check('scope_exact_after_'+p,sha(new)==after['sha256'] and len(new)==after['bytes'] and ident(N,p)['git_blob']==after['git_blob'] and new==raw(after['artifact_commit'],after['artifact_path']))
    check('scope_before_'+p,before==raw(r['before']['commit'],p) and sha(before)==r['before']['sha256'])
    oldlines=before.splitlines(keepends=True);newlines=new.splitlines(keepends=True)
    operations=[dict(kind=k,old_start_line=i+1,old_end_exclusive_line=j+1,new_start_line=a+1,new_end_exclusive_line=z+1) for k,i,j,a,z in difflib.SequenceMatcher(a=oldlines,b=newlines,autojunk=False).get_opcodes() if k!='equal']
    expected=r['bounded_change'];check('scope_single_bounded_change_'+p,operations==[expected],independent_operations=operations)
    scope_changes.append(dict(path=p,before=ident(C,p),after=ident(N,p),operations=operations,not_quality_verdict=True))
oldhashes=[dict(index=i,batch=r['batch'],id=r['id'],sha256=objsha(r)) for i,r in enumerate(receipts)]
check('all327_receipt_objects',oldhashes==pres['receipt_object_hashes'] and len(receipts)==327,receipt_array_sha256=objsha(receipts))
check('all327_array',objsha(receipts)==pres['receipt_array_canonical_sha256'])
check('old_statistics_immutable',raw(C,stats_path)==raw(N,stats_path)==raw(P,stats_path))
ledger=[]
for leaf in ['approval-ledger.tsv','traceability-successor.tsv']:
    old=raw(C,B+leaf);new=raw(N,B+leaf);oldrows=tsv(C,B+leaf);newrows=tsv(N,B+leaf);added=newrows[len(oldrows):]
    check('old_TSV_prefix_'+leaf,new.startswith(old) and len(oldrows)==327)
    check('new14_pending_'+leaf,len(added)==14 and all(r['canonical_state']=='OPEN' and not r['candidate_review_commit'] for r in added))
    ledger.append(dict(path=B+leaf,old=ident(C,B+leaf),new=ident(N,B+leaf),old327_bytes_preserved=new.startswith(old),added_rows=len(added)))
oldrows=tsv(C,B+'finding-ledger.tsv');newrows=tsv(N,B+'finding-ledger.tsv');assigned=set(oblig['remaining14_exactly_B21_contributions'])
check('229_same_order_OPEN',len(oldrows)==len(newrows)==229 and [r['finding_id'] for r in oldrows]==[r['finding_id'] for r in newrows] and all(r['canonical_state']=='OPEN' for r in newrows))
for before,after,oldline,newline in zip(oldrows,newrows,raw(C,B+'finding-ledger.tsv').splitlines()[1:],raw(N,B+'finding-ledger.tsv').splitlines()[1:]):
    keys=[k for k in before if before[k]!=after[k]]
    check('finding_preservation_'+before['finding_id'],oldline==newline if before['finding_id'] not in assigned else keys==['closure_gate'] and after['closure_gate'].startswith(before['closure_gate']))
owners=[]
for i,dep in enumerate(deps['dependencies']):
    own=[r for r in receipts if r['batch']==dep['batch']]
    bound=[ptr(doc(x['commit'],x['path']),x['pointer']) for x in dep['accepted_receipt_bindings']]
    check('dependency_'+dep['batch'],own==bound==dep['exact_candidate_actual_and_independent_report_fields'])
    owners.append(dict(batch=dep['batch'],receipt_count=len(own),primary_count=sum(r['primary'] for r in own),all_old_objects_bound_exactly=own==bound,dispatch_pointer='/dependencies/'+str(i)))
def tree(s):return {l.split('\t',1)[1]:l.split('\t',1)[0] for l in git('ls-tree','-r',s).decode().splitlines()}
tc,tn=tree(C),tree(N)
protected=[p for p in tc if ((p.startswith('review/') and not p.startswith(B)) or (p.startswith(B+'batches/B') and not p.startswith(B+'batches/B21/')) or p.startswith(('specs/','reference/')) or p=='AGENTS.md' or p.startswith('deliverables/final-specification-set/')) and p not in allowed]
bad=[p for p in protected if tc[p]!=tn.get(p)]
check('all_protected_objects',not bad,protected_path_count=len(protected),mismatches=bad,method='mode/type/blob identities; unchanged evidence reuse, not fresh semantic reads')
md=[]
for p in sorted(formal):
    if p.endswith('.md'):
        old=raw(C,p);new=raw(N,p);check('old_markdown_layer_'+p,old in new);md.append(dict(path=p,old_contiguous_bytes=old in new,old_sha256=sha(old),new_sha256=sha(new)))
for leaf in ['candidate-manifest.json','global-premises.json','integration-manifest.json','model-request-receipts.json','scope-counts.json']:
    old=doc(C,B+leaf);new=doc(N,B+leaf);check('old_JSON_fields_'+leaf,all(new[k]==v for k,v in old.items()),fields=list(old))
oldcases=raw(C,'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md').splitlines(keepends=True)
newcases=raw(N,'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md').splitlines(keepends=True)
mr=[]
for i in range(1,18):
    label='MR'+str(i).zfill(2);o=[(a,l) for a,l in enumerate(oldcases,1) if l.startswith(('| '+label+' |').encode())];z=[(a,l) for a,l in enumerate(newcases,1) if l.startswith(('| '+label+' |').encode())]
    check('old_case_'+label,len(o)==len(z)==1 and o[0][1]==z[0][1]);mr.append(dict(case=label,old_line=o[0][0],new_line=z[0][0],row_sha256=sha(o[0][1]),preserved=o[0][1]==z[0][1]))
for p in ['deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md','specs/overworld/wp13-move-route-matrix.md']:
    check('WP13_immutable_'+p,raw(C,p)==raw(N,p),identity=ident(N,p))
# Fixed old report remains available by exact identity; do not copy its evidence tree.
prior_entry=B+'batches/B21/affected-review-cloud-20261011-1/report.md'
prior=ident(R1,prior_entry)
check('old_affected_report_fixed_identity',prior['sha256']=='8518c5237ae522b680db7922ebf0ae74ef9bde56696f5dd5d16e8d9d3e7a0a18')
receipt_set={(r['batch'],r['id']) for r in receipts}
strict=[r['id'] for r in oblig['all229_records'] if all((b,r['id']) in receipt_set for b in r['all_contributors'])]
pending=[(b,r['id']) for r in oblig['all229_records'] for b in r['all_contributors'] if (b,r['id']) not in receipt_set]
counts=dict(accepted_batches=len(owners),accepted_contributions=len(receipts),touched_ids=len({r['id'] for r in receipts}),primary_minima=len({r['id'] for r in receipts if r['primary']}),strict_whole_controls=len(strict),pending_contributions=len(pending),pending_primary=sum(r['primary_owner']=='B21' for r in oblig['all229_records']),canonical_OPEN=len(newrows),canonical_CLOSED=0)
check('independent_counts',counts==dict(accepted_batches=20,accepted_contributions=327,touched_ids=228,primary_minima=220,strict_whole_controls=215,pending_contributions=14,pending_primary=9,canonical_OPEN=229,canonical_CLOSED=0))
result=dict(kind='NEW2_INDEPENDENT_AFFECTED_STATIC_METADATA_AUDIT_NOT_FULL_OR_RUNTIME',NEW2=N,C=C,P=P,D=D,grant=G,commit_identities=commits,checks=checks,formal_outputs=outputs,scope_application=scope_changes,old327_object_hashes=oldhashes,all20_dependencies=owners,old_ledger_preservation=ledger,old_markdown_layers=md,MR01_to_MR17_preservation=mr,prior_report_fixed_identity=prior,derived_counts=counts,errors=errors,scope_permission_is_quality_PASS=False,reference_or_project_execution=0,static_cases_executed=False,actual_or_C_or_FINAL_signed=False)
pathlib.Path('/tmp/b21-new2-static-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),protected_paths=len(protected),errors=errors,counts=counts),ensure_ascii=False))
