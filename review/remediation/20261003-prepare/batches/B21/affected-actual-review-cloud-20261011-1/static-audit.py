#!/usr/bin/env python3
"""Fresh read-only exact B21 ACT Git/text/JSON audit; no repository code runs."""
import collections, csv, difflib, hashlib, io, json, pathlib, re, subprocess
REPO='/workspace/b21-review'
C='e9c140dc33de1cb0662521318b051174909e4509'
N='e58486178e746273fb6fab55df00722807f1dc44'
ACT='d7b9f0882ce873eade1e57bf2a4aa76f7b329b0e'
G='d13eedb893abaf39322a022beba1d0a24f43b8aa'
M='b49aa3c2c1aa6992539b06a555477db33b75c0a4'
D='eb1885265fcde2a52767077de3193862036c3a71'
SG='aa57e293bf3a0a77fa42f1f42777df88cbd2fbe8'
R='53a14af81c1c139da047c51450a84aa7bee9b225'
B='review/remediation/20261003-prepare/'
F=B+'batches/B21/actual-freeze-1/'
I=B+'batches/B21/integration-stage-1/'
Q=B+'batches/B21/refreeze-after-B20-C-1/'
RP=B+'batches/B21/affected-review-cloud-20261011-2/'
AP=B+'batches/B21/author-draft-1/'
cache={};checks=[];errors=[]
def git(*args):return subprocess.check_output(['git','-C',REPO,*args])
def raw(s,p):
    if (s,p) not in cache:cache[s,p]=git('show',s+':'+p)
    return cache[s,p]
def doc(s,p):return json.loads(raw(s,p))
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(o):return sha(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def ident(s,p):
    b=raw(s,p)
    return dict(commit=s,path=p,git_blob=git('rev-parse',s+':'+p).decode().strip(),sha256=sha(b),bytes=len(b))
def pointer(o,p):
    for k in p.split('/')[1:]:
        k=k.replace('~1','/').replace('~0','~');o=o[int(k)] if isinstance(o,list) else o[k]
    return o
def check(n,ok,**details):
    checks.append(dict(check=n,satisfied=bool(ok),**details))
    if not ok:errors.append(n)
def binding(x,label):
    actual=ident(x['commit'],x['path'])
    check(label,all(actual.get(k)==x[k] for k in actual if k in x),identity=actual,pointer=x.get('pointer'))
    if 'pointer' in x:return pointer(doc(x['commit'],x['path']),x['pointer'])
    return None
def rows(s,p):return list(csv.DictReader(io.StringIO(raw(s,p).decode()),delimiter='\t'))
def tree(s):return {l.split('\t',1)[1]:l.split('\t',1)[0] for l in git('ls-tree','-r',s).decode().splitlines()}
def changes(a,b):return git('diff','--no-renames','--name-status',a,b).decode().splitlines()
fixed={C:'5baa01c8a604400b73f560bb06fa5d770089502a',N:'1dbe28a733bfde428129ed662d7e0d66243978c4',ACT:'aed1622a540c3fb9c898e1c7b94741be319f7a83',G:'10b08e7ce7f461d8a351f6f02734ed5e60029bfd',M:'72fdb37b03fdf59caa522f262becd85f25fac7c7',R:'baa164d68c76bc82d4fbaf11e018554073aa3f57',D:'c85948f536d7444bfe83d3c323ea6a48ba15d143',SG:'d1333b17eb6987d51dac40988d7d0e744b2ed677'}
commit_ids=[]
for s,t in fixed.items():
    v=git('show','-s','--format=%H %T %P',s).decode().split();commit_ids.append(dict(commit=v[0],tree=v[1],parents=v[2:]));check('fixed_tree_'+s,v[1]==t)
check('ACT_unique_G_parent',next(x['parents'] for x in commit_ids if x['commit']==ACT)==[G])
check('management_separate_successor',next(x['parents'] for x in commit_ids if x['commit']==M)==[ACT])
packet=doc(M,F+'packet-manifest.json')
for x in packet['files']:binding(dict(x,commit=M),'management_packet_'+x['path'])
dispatch=doc(M,F+'affected-actual-dispatch.json')
manifest=doc(M,F+'diff-manifest.json');streams=[]
for s in manifest['streams']:
    # Exact publisher stream uses Git's default rename detection, no path filters.
    b=git('-c','core.quotePath=true','diff','--no-ext-diff','--binary','--full-index',s['from_commit'],ACT)
    p=raw(M,s['path']);ev=changes(s['from_commit'],ACT)
    blocks=re.split(r'^diff --git ',b.decode(),flags=re.MULTILINE)[1:]
    summary=[dict(header=z.splitlines()[0],hunk_count=sum(l.startswith('@@ ') for l in z.splitlines()),added_lines=sum(l.startswith('+') and not l.startswith('+++') for l in z.splitlines()),removed_lines=sum(l.startswith('-') and not l.startswith('---') for l in z.splitlines()),rename=any(l.startswith('rename from ') for l in z.splitlines())) for z in blocks]
    check('complete_stream_'+s['role'],b==p and sha(b)==s['sha256'] and len(b)==s['bytes'] and ev==s['changed_paths'],published=ident(M,s['path']),independent_bytes=len(b),independent_sha256=sha(b),expanded_path_events=len(ev),display_blocks=len(blocks),rename_blocks=sum(z['rename'] for z in summary),copied_to_report=False)
    streams.append(dict(role=s['role'],fixed_reference=ident(M,s['path']),expanded_changed_paths=ev,full_stream_block_inventory=summary))
outputs=doc(M,F+'frozen-output-identities.json');payload=[];public=[]
for i,x in enumerate(outputs['exact_NEW2_payload22']):
    for k in ['NEW2','actual']:binding(x[k],'exact_payload_'+str(i)+'_'+k)
    p=x['actual']['path'];check('payload_byte_equal_'+p,raw(N,p)==raw(ACT,p));payload.append(dict(NEW2=ident(N,p),ACT=ident(ACT,p),whole_bytes_equal=True,prior_qualified_evidence_only=True))
for x in outputs['public3_management']:
    p=x['actual']['path']
    for k in ['candidate','G','actual']:binding(x[k],'public_identity_'+k+'_'+p)
    check('public_G_to_ACT_'+p,raw(G,p)==raw(ACT,p) and raw(N,p)!=raw(ACT,p))
    public.append(dict(path=p,NEW2=ident(N,p),G=ident(G,p),ACT=ident(ACT,p),G_ACT_equal=True))
contract=doc(D,Q+'author-contract.json');grant=doc(SG,B+'batches/B21/original-scope-grant-R-B21-006-1/scope-grant.json')
formal=set(contract['formal_write_paths_now']);granted={x['path'] for x in grant['authorized_paths']};allowed=formal|granted
check('25_output_scope_set',len(allowed)==25 and set(x['ACT']['path'] for x in payload)|set(x['path'] for x in public)==allowed)
gtach=changes(G,ACT);check('G_to_ACT_exact22',len(gtach)==22 and {x.split('\t')[-1] for x in gtach}=={x['ACT']['path'] for x in payload},paths=gtach)
tc,tn,ta=tree(C),tree(N),tree(ACT)
cach=changes(C,ACT);extrac={x.split('\t')[-1] for x in cach}-allowed
check('C_to_ACT52_bounded',len(cach)==52 and len(extrac)==27 and all(p.startswith((I,Q,B+'batches/B21/original-scope-grant-R-B21-006-1/')) for p in extrac),extra_management_paths=sorted(extrac))
nach=changes(N,ACT);deleted=[x.split('\t')[1] for x in nach if x.startswith('D\t')];added=[x.split('\t')[1] for x in nach if x.startswith('A\t')];modified=[x.split('\t')[1] for x in nach if x.startswith('M\t')]
check('NEW2_to_ACT62_layers',len(nach)==62 and len(deleted)==32 and len(added)==27 and set(modified)=={x['path'] for x in public} and all(p.startswith(AP) and p not in tc for p in deleted),only_candidate_evidence_absent_from_ACT=deleted,only_new_management_paths=added,only_public3_modified=modified)
author_fixed=[]
for x in outputs['author32_evidence_fixed_at_NEW2_not_actual_paths']:
    binding(x,'fixed_author_evidence_'+x['path']);check('author_location_'+x['path'],x['path'] in deleted and x['path'] not in tc and x['path'] not in ta)
    author_fixed.append(dict(fixed_identity=ident(N,x['path']),present_in_ACT=False,previously_in_C=False,scope='External immutable NEW2 evidence; not an ACT relative-path claim'))
check('exact_fixed_author32_set',set(x['fixed_identity']['path'] for x in author_fixed)==set(deleted))
for p in added:
    if p.startswith(Q):check('original_contract_layer_'+p,raw(ACT,p)==raw(D,p))
    elif p.startswith(B+'batches/B21/original-scope-grant-R-B21-006-1/'):check('scope_grant_layer_'+p,raw(ACT,p)==raw(SG,p))
scope=[]
for x in grant['authorized_paths']:
    p=x['path'];before=raw(C,p);after=raw(ACT,p);a=x['after']
    op=[dict(kind=k,old_start_line=i+1,old_end_exclusive_line=j+1,new_start_line=y+1,new_end_exclusive_line=z+1) for k,i,j,y,z in difflib.SequenceMatcher(a=before.splitlines(keepends=True),b=after.splitlines(keepends=True),autojunk=False).get_opcodes() if k!='equal']
    check('granted_ACT_exact_after_'+p,sha(after)==a['sha256'] and len(after)==a['bytes'] and ident(ACT,p)['git_blob']==a['git_blob'] and op==[x['bounded_change']] and after==raw(N,p))
    scope.append(dict(path=p,C=ident(C,p),NEW2=ident(N,p),ACT=ident(ACT,p),bounded_changes=op,permission_not_quality_pass=True))
stats_path=B+'batches/B20/acceptance-stage-1/completion-statistics-successor.json';receipt_doc=doc(C,stats_path);receipts=receipt_doc['accepted_contribution_receipts']
oldhashes=[dict(index=i,batch=x['batch'],id=x['id'],object_sha256=canonical(x)) for i,x in enumerate(receipts)]
prior_audit=doc(R,RP+'static-audit.json')
check('327_objects_same_prior_independent',len(receipts)==327 and [(x['index'],x['batch'],x['id'],x['object_sha256']) for x in oldhashes]==[(x['index'],x['batch'],x['id'],x['sha256']) for x in prior_audit['old327_object_hashes']],canonical_sorted_array_sha256=canonical(receipts))
check('old_statistics_full_bytes_C_N_ACT',raw(C,stats_path)==raw(N,stats_path)==raw(ACT,stats_path),identity=ident(ACT,stats_path))
pres=doc(ACT,I+'accepted-result-preservation.json');ordered_hash=sha(json.dumps(receipts,ensure_ascii=False,separators=(',',':')).encode())
check('registrar_ordered_hash_not_sorted_hash',ordered_hash==pres['old327_array_sha256'],registrar_ordered_array_sha256=ordered_hash,independent_sorted_array_sha256=canonical(receipts),distinct_serializations_same_objects=True)
registrations=doc(ACT,I+'finding-registration.json')['records'];oblig=doc(D,Q+'current229-statistics-and-obligations.json');expected_ids=oblig['remaining14_exactly_B21_contributions'];controls=doc(D,Q+'control-and-acceptance-overlay.json')['complete_control_records']
check('14_registration_ids_original_order',[x['id'] for x in registrations]==expected_ids and len(registrations)==14 and sum(x['primary'] for x in registrations)==9 and all(x['canonical_state']=='OPEN' and x['B21_C'] is None and x['canonical_closure'] is None and x['remaining_contributors']==['B21'] for x in registrations))
ledger=[]
for leaf in ['approval-ledger.tsv','traceability-successor.tsv']:
    p=B+leaf;before=raw(C,p);after=raw(ACT,p);br=rows(C,p);ar=rows(ACT,p);new=ar[len(br):]
    check('327_raw_prefix_'+leaf,after.startswith(before) and len(br)==327 and len(ar)==341)
    check('14_new_public_rows_'+leaf,[x['finding_id'] for x in new]==expected_ids and all(x['canonical_state']=='OPEN' and x['candidate_commit']==N for x in new))
    for i,x in enumerate(new):
        if leaf=='approval-ledger.tsv':
            obj=json.loads(x['remaining_obligations']);ok=x['candidate_review_commit']=='f361d565c9e8de5467e59df6e0ed7994822d9fce' and x['reviewed_integration_commit']=='EXTERNAL_ACT_FREEZE_REQUIRED' and x['integration_review_commit']=='NOT_PERFORMED' and 'PENDING' in x['integration_verdict'] and 'PENDING' in x['integration_disposition'] and obj['record_key']==registrations[i]['record_key'] and obj['remaining_contributors']==['B21'] and obj['B21_C']=='NOT_PERFORMED' and obj['canonical_closure']=='NOT_PERFORMED'
        else:
            obj=json.loads(x['remaining_obligations']);ok=x['candidate_review_commit']=='f361d565c9e8de5467e59df6e0ed7994822d9fce' and 'PENDING' in x['integration_gate'] and json.loads(x['remaining_batches'])==['B21'] and obj['record_key']==registrations[i]['record_key'] and obj['B21_C']=='NOT_PERFORMED' and obj['actual_gate']=='PENDING_AT_EXTERNAL_ACT_FREEZE'
        check('pending_signature_separation_'+leaf+'_'+x['finding_id'],ok)
    ledger.append(dict(path=p,C=ident(C,p),ACT=ident(ACT,p),old327_raw_prefix=True,physical_data_rows=341,pending_rows=14,pending_signatures_not_filled=True))
binding_doc=doc(M,F+'public-registration-actual-binding.json');binding_rows=[]
for i,x in enumerate(binding_doc['new14_rows']):
    o=binding(x['G_record'],'actual_bound_G_'+str(i));binding(x['candidate_FULL_record'],'candidate_FULL_bound_'+str(i))
    check('actual_binding_'+str(i),x['id']==expected_ids[i] and x['record_key']==registrations[i]['record_key'] and o==registrations[i] and x['approval_data_row_1based']==328+i and x['trace_data_row_1based']==328+i and x['frozen_integration_commit']==ACT and x['frozen_integration_tree']==fixed[ACT] and x['state']=='PENDING_EXACT_ACTUAL_FULL_AFFECTED_AND_B21_C')
    binding_rows.append(dict(record_key=x['record_key'],data_row=x['approval_data_row_1based'],ACT_bound=True,still_pending=True))
oldfind=rows(C,B+'finding-ledger.tsv');newfind=rows(ACT,B+'finding-ledger.tsv')
check('229_same_order_all_OPEN',[x['finding_id'] for x in oldfind]==[x['finding_id'] for x in newfind] and len(newfind)==229 and all(x['canonical_state']=='OPEN' for x in newfind))
for a,z in zip(oldfind,newfind):
    changed=[k for k in a if a[k]!=z[k]];check('canonical_preservation_'+a['finding_id'],changed==[] if a['finding_id'] not in expected_ids else changed==['closure_gate'] and z['closure_gate'].startswith(a['closure_gate']))
protected=[p for p in tc if (p.startswith(('specs/','reference/','deliverables/final-specification-set/')) or p=='AGENTS.md' or p.startswith('review/') and not p.startswith(B) or p.startswith(B+'batches/B') and not p.startswith(B+'batches/B21/')) and p not in allowed]
bad=[p for p in protected if tc[p]!=ta.get(p)];check('all_protected_C_mode_type_blob',not bad,protected_paths=len(protected),mismatches=bad,not_fresh_semantic_re_read=True)
old_batches=[p for p in tc if p.startswith(B+'batches/B') and not p.startswith(B+'batches/B21/')]
check('all_old_batch_evidence_mode_type_blob',all(tc[p]==ta.get(p) for p in old_batches),old_batch_paths=len(old_batches))
for leaf in ['candidate-manifest.json','global-premises.json','integration-manifest.json','model-request-receipts.json','scope-counts.json']:
    before=doc(C,B+leaf);after=doc(ACT,B+leaf);check('old_JSON_fields_'+leaf,all(after.get(k)==v for k,v in before.items()))
for p in sorted(formal):
    if p.endswith('.md'):check('old_markdown_layer_'+p,raw(C,p) in raw(ACT,p))
inputs=doc(M,F+'frozen-review-inputs.json');input_ids=[]
for i,x in enumerate(inputs['complete_original_planned_reads']):
    z=x['actual_input'];binding(z,'planned_input_'+str(i));input_ids.append(dict(planned_index=i,identity=z,immutable_original_review=x['immutable_original_review'],current_bytes_changed=x['current_bytes_changed'],identity_not_new_whole_read=True))
check('96_original_input_layers',len(input_ids)==96 and sum(x['immutable_original_review'] for x in input_ids)==2)
dep=doc(D,Q+'accepted-dependency-map.json')['dependencies'];entry=doc(M,F+'affected-owner-entrypoints.json')['owners'];owner_counts=[]
for i,x in enumerate(entry):
    owner=x['owner'];own=[z for z in receipts if z['batch']==owner];bound=[binding(z,'owner_receipt_'+owner+'_'+str(j)) for j,z in enumerate(x['all_prior_fixed_receipt_bindings'])]
    check('owner_'+owner,owner==f'B{i+1:02d}' and own==bound==dep[i]['exact_candidate_actual_and_independent_report_fields'] and x['prior_receipt_count']==len(own))
    binding(x['candidate_affected_owner_record'],'prior_affected_owner_'+owner)
    owner_counts.append(dict(owner=owner,receipt_count=len(own),primary_count=sum(z['primary'] for z in own),all_receipt_objects_equal=True,actual_scope=x['required_actual_scope']))
prev=doc(R,RP+'b01-b14-fixed-evidence-reuse.json');owner_reuse=[]
for i,x in enumerate(prev['owners']):
    consumers=[]
    for z in x['current_consumer_identities']:
        n=z['current_NEW2'];p=n['path'];a=ident(ACT,p);ok=raw(ACT,p)==raw(N,p) and a['git_blob']==n['git_blob'] and a['sha256']==n['sha256'] and a['bytes']==n['bytes'];check('B01_B14_actual_consumer_'+x['owner']+'_'+p,ok)
        consumers.append(dict(ACT=a,whole_bytes_same_as_reviewed_NEW2=ok,qualification='Prior same-byte supported scope reused with fixed attribution; not a fresh full-body review'))
    owner_reuse.append(dict(owner=x['owner'],old_receipt_count=x['old_receipt_count'],prior_NEW2_evidence=dict(**ident(R,RP+'b01-b14-fixed-evidence-reuse.json'),pointer='/owners/'+str(i)),current_consumer_identities=consumers,prior_qualified_interface_assessment=x['current_affected_assessment'],new_actual_scope=entry[i]['required_actual_scope'],actual_disposition='PENDING_ROOT_SEMANTIC_COMPLETION'))
receipt_pairs={(z['batch'],z['id']) for z in receipts};strict=[z['id'] for z in oblig['all229_records'] if all((owner,z['id']) in receipt_pairs for owner in z['all_contributors'])];pending=[(owner,z['id']) for z in oblig['all229_records'] for owner in z['all_contributors'] if (owner,z['id']) not in receipt_pairs]
counts=dict(accepted_batches=len(owner_counts),accepted_contributions=len(receipts),touched_ids=len({z['id'] for z in receipts}),primary_minima=len({z['id'] for z in receipts if z['primary']}),strict_whole_controls=len(strict),pending_contributions=len(pending),pending_primary=sum(z['primary_owner']=='B21' for z in oblig['all229_records']),canonical_OPEN=len(newfind),canonical_CLOSED=0)
check('independent_counts',counts==dict(accepted_batches=20,accepted_contributions=327,touched_ids=228,primary_minima=220,strict_whole_controls=215,pending_contributions=14,pending_primary=9,canonical_OPEN=229,canonical_CLOSED=0))
result=dict(kind='EXACT_ACT_INDEPENDENT_AFFECTED_METADATA_AUDIT',ACT=ACT,ACT_tree=fixed[ACT],management=M,NEW2=N,C=C,commit_identities=commit_ids,checks=checks,complete_streams=streams,exact_NEW2_payload22=payload,public3_management=public,scope3_actual_application=scope,author32_external_fixed_evidence=author_fixed,old327_object_hashes=oldhashes,old_ledger_preservation=ledger,actual_binding14=binding_rows,original96_input_identities=input_ids,all20_owner_receipt_bindings=owner_counts,derived_counts=counts,errors=errors,no_recursive_diff_or_evidence_copy=True,reference_program_execution=0,static_cases_executed=False,no_model_or_quota_audit=True,metadata_audit_not_semantic_actual_signature=True)
pathlib.Path('/tmp/b21-actual-static-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
pathlib.Path('/tmp/b21-actual-b01-b14-reuse.json').write_text(json.dumps(dict(kind='ACT_ROOT_B01_B14_FIXED_QUALIFIED_REUSE',ACT=ACT,ACT_tree=fixed[ACT],owners=owner_reuse,errors=errors,qualification='Exact same bytes only; actual public G and changed conditions judged separately'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),errors=errors,protected_paths=len(protected),counts=counts),ensure_ascii=False))
