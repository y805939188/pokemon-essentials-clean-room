"""Independent Git/text/JSON review checks. No reference-code execution or vectors.

Run from the repository root. All generated artifacts stay in this review folder,
except the two large reconstructed complete diffs, written under /tmp.
"""
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
BASE = '0a12de641542f9a59909d2a950c1de8df17ca09d'
CAND = '46cd726c35e9d754a8e42b32986313ce3d4d1782'
REPORT = '94b012ee12d457aa4b99103477a0d35f083b1182'
PAYLOAD = '8b9bb081088e54dfdc7d8cc78af776442ccb9db4'
TARGET = '1b1e169faf273e89ad6b7f5e46fd7b60d87d3946'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
GLOBAL = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
REF = Path('/tmp/r-b02-reference')
REF_SHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF_TREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
RUN = 'review/remediation/20261003-prepare/'
B02 = RUN + 'batches/B02/'
STAGE = B02 + 'integration-stage-1/'
OLD_REVIEW = B02 + 'review-round-1/'
CAT = 'deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md'
PUBLIC = sorted(['audit/source-traceability.md', 'deliverables/final-specification-set/README.md',
 'deliverables/final-specification-set/scope-statement.md', 'deliverables/final-specification-set/test-catalog/README.md',
 'planning/coverage.md', 'planning/feature-matrix.md'] + [RUN+x for x in
 ['approval-ledger.tsv','traceability-successor.tsv','final-integration-review.md','historical-errata.md']])
checks = []

def git(*args, repo=ROOT):
    return subprocess.check_output(['git','-C',str(repo),*args])

def data(commit, path, repo=ROOT):
    return git('show',commit+':'+path,repo=repo)

def obj(path, commit=TARGET):
    return json.loads(data(commit,path))

def sha(b):
    return hashlib.sha256(b).hexdigest()

def canonical(v):
    return sha(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())

def ident(commit,path,repo=ROOT):
    b=data(commit,path,repo)
    return {'commit':commit,'path':path,'git_blob':git('rev-parse',commit+':'+path,repo=repo).decode().strip(),'sha256':sha(b),'bytes':len(b)}

def check(name,ok,evidence):
    checks.append({'check':name,'ok':bool(ok),'evidence':evidence,'kind':'INDEPENDENT_DOCUMENT_GIT_IDENTITY_CHECK_NOT_BEHAVIOR_EXECUTION'})

def save(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def ns(a,b):
    return [{'change':t,'path':p} for t,p in (line.split('\t') for line in git('diff','--name-status','--no-renames',a,b).decode().splitlines())]

def diff(a,b):
    return git('diff','--binary','--full-index','--no-renames','--no-ext-diff','--no-textconv',a,b)

def paths(commit,prefix):
    return git('ls-tree','-r','--name-only',commit,prefix).decode().splitlines()

def tsv(commit,path):
    return list(csv.DictReader(io.StringIO(data(commit,path).decode()),delimiter='\t'))

manifest=obj(STAGE+'integration-manifest.json')
freeze=obj(STAGE+'diff-and-freeze.json')
registration=obj(STAGE+'finding-registration.json')
nav=obj(STAGE+'a017-navigation-successor.json')
counts=obj(STAGE+'scope-counts.json')
author_validation=obj(STAGE+'validation-results.json')
formal=[x['reviewed_candidate']['path'] for x in manifest['formal_candidate_identities']]
prior_scope=obj(OLD_REVIEW+'scope-manifest.json',REPORT)
check('formal_scope_and_expansion_identity_match_independent_candidate_review',set(formal)=={x['candidate']['path'] for x in prior_scope['formal_files']} and manifest['candidate_scope_expansion_authorization']==ident(CAND,B02+'author-v2/scope-expansion-authorization.json'),{'formal_files':len(formal),'authorization':manifest['candidate_scope_expansion_authorization']})
full=ns(BASE,TARGET); incremental=ns(CAND,TARGET); evidence=ns(PAYLOAD,TARGET)
check('exact_frozen_ancestry', all(git('rev-parse',a+'^').decode().strip()==b for a,b in [(TARGET,PAYLOAD),(PAYLOAD,REPORT),(REPORT,CAND),(CAND,'1c8027835e2be9057ca9040046e9ee986125ad04'),('1c8027835e2be9057ca9040046e9ee986125ad04',BASE)]), {'reviewed_integration':TARGET,'payload':PAYLOAD,'candidate_report':REPORT,'candidate':CAND,'accepted_upstream':BASE})
remote=git('ls-remote','--heads','origin','refs/heads/remediation/20261003-prepare/integration').decode().strip()
check('reviewed_remote_integration_exact',remote.split()[0]==TARGET,{'readback':remote})
check('full_75_and_candidate_32_complete_scope', len(full)==75 and len(incremental)==32 and {r['path'] for r in full if r['change']=='M'}==set(formal+PUBLIC) and {r['path'] for r in incremental if r['change']=='M'}==set(PUBLIC) and all(r['change']=='M' or r['change']=='A' and (r['path'].startswith(B02+'author/') or r['path'].startswith(B02+'author-v2/') or r['path'].startswith(OLD_REVIEW) or r['path'].startswith(STAGE)) for r in full), {'full_count':len(full),'candidate_count':len(incremental),'modified_formal':len(formal),'new_public_modified':len(PUBLIC)})
check('evidence_successor_exact_three_additions', evidence==sorted(freeze['evidence_only_successor_contract']['allowed_changes'],key=lambda x:x['path']) and all(r['change']=='A' for r in evidence), {'changes':evidence,'payload_tree':git('rev-parse',PAYLOAD+'^{tree}').decode().strip(),'target_tree':git('rev-parse',TARGET+'^{tree}').decode().strip()})
check('freeze_payload_tree_and_complete_name_status',freeze['payload_tree']==git('rev-parse',PAYLOAD+'^{tree}').decode().strip() and freeze['accepted_upstream_to_payload_complete_name_status']==ns(BASE,PAYLOAD) and freeze['candidate_to_payload_complete_name_status']==ns(CAND,PAYLOAD) and freeze['public_payload_name_status']==ns(REPORT,PAYLOAD), {'payload_upstream_paths':len(ns(BASE,PAYLOAD)),'payload_candidate_paths':len(ns(CAND,PAYLOAD)),'payload_public_paths':len(ns(REPORT,PAYLOAD))})
for row in freeze['full_payload_diffs']:
    b=diff(row['base_commit'],PAYLOAD)
    check('complete_payload_patch:'+Path(row['path']).name,b==data(TARGET,row['path']) and sha(b)==row['sha256'] and len(b)==row['bytes'],{'sha256':sha(b),'bytes':len(b),'base':row['base_commit'],'target':PAYLOAD,'no_path_exclusions':True})
reconstructed=[]
for base,label in [(BASE,'upstream'),(CAND,'candidate'),(PAYLOAD,'evidence')]:
    b=diff(base,TARGET); target=Path('/tmp')/('r-b02-integration-'+label+'-complete.patch');target.write_bytes(b)
    reconstructed.append({'base':base,'target':TARGET,'sha256':sha(b),'bytes':len(b),'path_count':len(ns(base,TARGET)),'temporary_reconstructed_path':str(target),'command':'git diff --binary --full-index --no-renames --no-ext-diff --no-textconv '+base+' '+TARGET})

formal_results=[]
for row in manifest['formal_candidate_identities']:
    a=row['upstream'];b=row['reviewed_candidate'];p=b['path']
    actual=ident(TARGET,p)
    formal_results.append({'path':p,'upstream':ident(BASE,p),'reviewed_candidate':ident(CAND,p),'reviewed_integration':actual})
    check('formal_candidate_bytes_preserved:'+p,a==ident(BASE,p) and b==ident(CAND,p) and data(CAND,p)==data(TARGET,p),actual)
auth_paths=paths(CAND,B02+'author/')+paths(CAND,B02+'author-v2/')
review_paths=paths(REPORT,OLD_REVIEW)
check('all_30_author_and_12_review_files_original_bytes',len(auth_paths)==30 and len(review_paths)==12 and all(data(CAND,p)==data(TARGET,p) for p in auth_paths) and all(data(REPORT,p)==data(TARGET,p) for p in review_paths),{'author_count':len(auth_paths),'review_count':len(review_paths)})
identity_errors=[]
for field,commit in [('current_dependency_identities',BASE),('preserved_author_records',CAND),('preserved_candidate_review_records',REPORT)]:
    for x in manifest[field]:
        if x!=ident(commit,x['path']) or data(commit,x['path'])!=data(TARGET,x['path']): identity_errors.append((field,x['path']))
for x in manifest['current_public_paths']:
    p=x['current']['path'];actual=ident(TARGET,p)
    if x['previous']!=ident(BASE,p) or any(x['current'][k]!=actual[k] for k in ['path','git_blob','sha256','bytes']):identity_errors.append(('public',p))
check('all_manifest_35_dependencies_30_authors_12_reviews_10_public_identities',not identity_errors and len(manifest['current_dependency_identities'])==35 and len(manifest['current_public_paths'])==10,{'mismatches':identity_errors})
hash_rows=tsv(TARGET,STAGE+'current-hashes.tsv');hash_errors=[]
for x in hash_rows:
    actual=ident(TARGET,x['path'])
    if any(str(x[k])!=str(actual[k]) for k in ['git_blob','sha256','bytes']):hash_errors.append(x['path'])
check('current_hash_58_rows_exact_with_no_self_or_evidence_loop',len(hash_rows)==58 and len({x['path'] for x in hash_rows})==58 and not hash_errors and all(not x['path'].startswith(STAGE) for x in hash_rows),{'role_counts':{r:sum(x['role']==r for x in hash_rows) for r in ['formal','public','dependency']},'mismatches':hash_errors})

protected_prefixes=['review/remediation-20261003-prepare/',RUN+'batches/B01/',RUN+'preflight/']
protected=[]
for prefix in protected_prefixes:protected+=paths(BASE,prefix)
historical_root=[p for p in paths(BASE,RUN) if '/batches/' not in p[len(RUN):] and p not in PUBLIC]
protected+=historical_root
check('B01_plan_PRE0_and_root_evidence_all_bytes_retained', all(data(BASE,p)==data(TARGET,p) for p in protected),{'checked_paths':len(set(protected)),'prefixes':protected_prefixes,'root_evidence_count':len(historical_root)})
for p in [RUN+'approval-ledger.tsv',RUN+'traceability-successor.tsv']:
    old=data(BASE,p);new=data(TARGET,p);rows=tsv(TARGET,p);before=tsv(BASE,p)
    check('B01_14_rows_append_only:'+Path(p).name,new.startswith(old) and len(before)==14 and len(rows)==26 and len({(x['finding_id'],x['candidate_commit']) for x in rows})==26,{'prior_rows':len(before),'current_contribution_rows':len(rows),'B02_new_rows':len(rows)-len(before),'canonical_count_not_row_count':True})
check('B01_central_handoff_byte_exact_suffix',data(TARGET,RUN+'final-integration-review.md').endswith(data(BASE,RUN+'final-integration-review.md')),{'upstream':BASE})
for p in ['audit/source-traceability.md','planning/coverage.md','planning/feature-matrix.md',RUN+'historical-errata.md']:
    old=data(BASE,p);new=data(TARGET,p);split=old.index(b'\n\n')+2
    check('historical_public_body_preserved:'+p,new.startswith(old[:split]) and new.endswith(old[split:]),{'old_body_sha256':sha(old[split:])})
scope='deliverables/final-specification-set/scope-statement.md'
old=data(BASE,scope).decode();new=data(TARGET,scope).decode()
check('U_G_AX_named_unknown_scope_sections_2_3_4_preserved',old.split('## 2.')[1].split('## 5.')[0]==new.split('## 2.')[1].split('## 5.')[0],{'U':'U01–U10','G':'G01–G12','AX':'AX01–AX20','runtime_upgrade':False})

def catalog(b):
    return {m[1]:line for line in b.decode().splitlines() if (m:=re.match(r'^\| ((?:EP|TM|IO|DP|LZ|SV|MG)\d+) \|',line))}
before=catalog(data(BASE,CAT));after=catalog(data(TARGET,CAT))
families={p:sum(i.startswith(p) for i in after) for p in ['EP','TM','IO','DP','LZ','SV','MG']}
check('catalog_99_rows_families_and_exact_changes',len(before)==87 and len(after)==99 and families==counts['catalog_families'] and sorted(set(after)-set(before))==counts['new_catalog_ids'] and sorted(k for k in before if before[k]!=after.get(k))==counts['existing_catalog_rows_changed'] and not(set(before)-set(after)),{'families':families,'new_ids':sorted(set(after)-set(before)),'changed_ids':sorted(k for k in before if before[k]!=after.get(k))})
for prefix,next_prefix in [('EP','TM'),('DP','LZ')]:
    def section(b):return b.decode().split('## '+prefix+'：')[1].split('## '+next_prefix+'：')[0].encode()
    a=section(data(BASE,CAT));b=section(data(TARGET,CAT))
    # Include the heading in the hash, exactly as in the candidate review.
    whole=('## '+prefix+'：').encode()+b
    check('B01_'+prefix+'_complete_section_retained',a==b,{'sha256_with_heading':sha(whole),'bytes_with_heading':len(whole)})
other_cat='deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md'
other_rows=[l for l in data(TARGET,other_cat).decode().splitlines() if re.match(r'^\| (?:KC|KR|KL)\d+ \|',l)]
check('B01_other_catalog_51_unchanged_and_combined_150',len(other_rows)==51 and data(BASE,other_cat)==data(TARGET,other_cat) and len(other_rows)+len(after)==150,{'other_rows':len(other_rows),'combined':len(other_rows)+len(after)})
index='deliverables/final-specification-set/test-catalog/README.md'
old_rows=[l for l in data(BASE,index).decode().splitlines() if l.startswith('| [')];new_rows=[l for l in data(TARGET,index).decode().splitlines() if l.startswith('| [')]
changed_index=[(a,b) for a,b in zip(old_rows,new_rows) if a!=b]
check('catalog_index_only_shared_row_amended',len(old_rows)==len(new_rows) and len(changed_index)==1 and 'TM01–TM14、IO01–IO15、DP01–DP05、LZ01–LZ17、SV01–SV11、MG01–MG16' in changed_index[0][1] and data(BASE,index).decode().split('B01 当前目录登记：')[1].strip() in data(TARGET,index).decode(),{'changed_rows':len(changed_index),'unchanged_rows':len(old_rows)-len(changed_index)})
for wp,heading,next_heading in [('WP07','### 8.2','## 9.'),('WP08','### 9.2','## 10.'),('WP10','### 8.2','## 9.')]:
    p={'WP07':'specs/kernel/wp07-diagnostics-files-http.md','WP08':'specs/kernel/wp08-localization.md','WP10':'specs/kernel/wp10-migration-failure-recovery.md'}[wp]
    def scenes(commit):
        t=data(commit,p).decode().split(heading)[1].split(next_heading)[0]
        return [l for l in t.splitlines() if l.startswith('| ') and not l.startswith('| ---')][1:]
    a=scenes(BASE);b=scenes(TARGET)
    check('original_scene_count_and_old_rows:'+wp,len(b)==counts['original_static_scenes_current'][wp] and len(b)-len(a)==counts['new_original_static_scenes'][wp] and all(l in b for l in a),{'old':len(a),'current':len(b),'added':len(b)-len(a),'executed':0})
all_final=paths(TARGET,'deliverables/final-specification-set/')
catalog_paths=[p for p in paths(TARGET,'deliverables/final-specification-set/test-catalog/') if Path(p).name!='README.md']
check('final_set_131_markdown_17_catalog_files',sum(p.endswith('.md') for p in all_final)==131 and len(catalog_paths)==17,{'markdown_count':sum(p.endswith('.md') for p in all_final),'catalog_file_count_excluding_index':len(catalog_paths),'index_files':1})

original={x['id']:x for x in obj('review/global-independent-review/2026-10-03-fd82a639/findings.json',GLOBAL)}
ledger=tsv(TARGET,RUN+'finding-ledger.tsv')
required={i for i,x in original.items() if x.get('required_revision') is True}
check('233_canonical_229_required_OPEN_priority_preserved',len(original)==233 and len(required)==229 and len(ledger)==229 and {x['finding_id'] for x in ledger}==required and all(x['canonical_state']=='OPEN' and x['priority']==original[x['finding_id']]['priority'] for x in ledger) and data(BASE,RUN+'finding-ledger.tsv')==data(TARGET,RUN+'finding-ledger.tsv'),{'canonical':len(original),'required':len(required),'OPEN':sum(x['canonical_state']=='OPEN' for x in ledger),'priorities':{p:sum(x['priority']==p for x in ledger) for p in ['P2','P3']}})
prior={x['id']:x for x in obj(OLD_REVIEW+'finding-dispositions.json',REPORT)['dispositions']}
responses={x['id']:x for x in obj(B02+'author-v2/finding-responses.json',CAND)['contributions']}
acceptance=obj('review/remediation-20261003-prepare/finding-acceptance.json',PLAN)
reg={x['id']:x for x in registration['dispositions']}
reg_errors=[]
for fid,x in reg.items():
    o=original[fid];r=prior[fid];a=responses[fid]
    unchanged={k:v for k,v in r.items() if k not in ['actual_integration_review','public_registration']}
    if any(x[k]!=v for k,v in unchanged.items()):reg_errors.append((fid,'candidate_fields'))
    if x['original_object_canonical_json_sha256']!=canonical(o) or x['acceptance_object_canonical_json_sha256']!=canonical(acceptance[fid]) or x['original_effective_constraints']!=o.get('effective_case_constraints',o['current_qualifications']) or x['source_extensions_count']!=len(o.get('extensions',[])):reg_errors.append((fid,'effective_inputs'))
    if x['original_source_inputs_and_final_test_mapping']!=a['mapping'] or x['v2_original_clause_changes']!=a.get('v2_original_clause_changes',[]):reg_errors.append((fid,'mapping'))
check('12_dispositions_all_original_qualifications_aliases_scope_mappings_retained',set(reg)==set(prior) and not reg_errors,{'mismatches':reg_errors,'count':len(reg),'C003_effective_extensions':reg['GIR-FD82-C003']['source_extensions_count']})
binding_errors=[]
for x in manifest['original_finding_binding']:
    o=original[x['id']]
    if x['commit']!=GLOBAL or x['canonical_object_sha256']!=canonical(o) or x['severity']!=o['priority'] or x['aliases']!=[r['raw_id'] for r in o['raw_reports']]:binding_errors.append(x['id'])
check('12_original_binding_hashes_severity_aliases_exact',not binding_errors and len(manifest['original_finding_binding'])==12,{'mismatches':binding_errors})
approval=[x for x in tsv(TARGET,RUN+'approval-ledger.tsv') if x['candidate_commit']==CAND]
trace=[x for x in tsv(TARGET,RUN+'traceability-successor.tsv') if x['candidate_commit']==CAND]
approval_errors=[];trace_errors=[]
for x in approval:
    r=reg[x['finding_id']];remaining=json.loads(x['remaining_obligations'])
    if x['canonical_state']!='OPEN' or x['candidate_review_commit']!=REPORT or x['candidate_reviewer']!='R-B02' or x['accepted_contribution_kind']!=r['candidate_decision'] or x['integration_verdict']!='NOT_REVIEWED_PENDING_ULTRA' or x['downstream_gate']!='BLOCKED' or remaining['remaining_owners']!=r['remaining_owners'] or remaining['remaining_responsibility']!=r['remaining_responsibility']:approval_errors.append(x['finding_id'])
for x in trace:
    r=reg[x['finding_id']]
    expected_tests='PATH01–PATH08; navigation identities only' if x['finding_id']=='GIR-FD82-A017' else ';'.join(r['static_scenario_ids_reviewed_not_executed'])
    if x['canonical_state']!='OPEN' or x['candidate_review_commit']!=REPORT or x['original_report_commit']!=GLOBAL or x['effective_priority']!=r['severity_preserved'] or json.loads(x['current_clause_inputs'])!=r['original_source_inputs_and_final_test_mapping'] or x['static_test_ids_not_executed']!=expected_tests or x['remaining_batches']!=';'.join(r['remaining_owners']):trace_errors.append(x['finding_id'])
check('new_12_approval_and_trace_rows_match_scoped_pending_registration',len(approval)==len(trace)==12 and not approval_errors and not trace_errors,{'approval_mismatches':approval_errors,'trace_mismatches':trace_errors})

check('fixed_reference_external_SHA_tree_clean',not REF.is_relative_to(ROOT) and git('rev-parse','HEAD',repo=REF).decode().strip()==REF_SHA and git('rev-parse','HEAD^{tree}',repo=REF).decode().strip()==REF_TREE and git('status','--porcelain=v1',repo=REF)==b'',{'repository':str(REF),'sha':REF_SHA,'tree':REF_TREE,'execution':0})
audit=data(TARGET,'audit/source-traceability.md').decode();base_audit=data(BASE,'audit/source-traceability.md').decode().splitlines();nav_results=[]
for x in nav['corrections']:
    p=x['replacement_full_reference_path'];wrong='Data/Scripts/'+x['replace_path_only'];actual=ident(REF_SHA,p,REF)
    line=next((l for l in audit.splitlines() if l.startswith('| '+x['vector_id']+' |')),None)
    ranges=re.findall(r'\d+',x['preserve_reference_ranges']);available_lines=len(data(REF_SHA,p,REF).splitlines())
    ok=(not (REF/wrong).exists() and actual==x['correct_identity'] and base_audit[x['frozen_handoff_line']-1]==x['original_audit_row'] and x['corrected_reference_row']==x['original_audit_row'].replace(x['replace_path_only'],x['replacement_audit_relative_path']) and x['original_audit_row'] in audit and line and ('`'+p+'`') in line and x['preserve_reference_ranges'] in line and all(0<int(n)<=available_lines for n in ranges))
    item={'id':x['vector_id'],'original_baseline_line':x['original_baseline_line'],'upstream_line':x['frozen_handoff_line'],'current_audit_line':audit.splitlines().index(line)+1 if line else None,'correct_identity':actual,'ranges_preserved':x['preserve_reference_ranges'],'original_wrong_path_absent':not(REF/wrong).exists(),'corrected_row_path_only':x['corrected_reference_row']==x['original_audit_row'].replace(x['replace_path_only'],x['replacement_audit_relative_path']),'formal_current_entry_applied':bool(line),'legacy_reading_claims_promoted':False}
    nav_results.append(item);check('A017_actual_current_navigation:'+x['vector_id'],ok,item)
check('A017_eight_authoritative_rows_and_pending_canonical_status',len(nav_results)==8 and nav['canonical_state']=='OPEN' and nav['integration_verdict']=='PENDING_R_B02_ULTRA' and audit.count('| PATH')==8,{'authoritative_rows':len(nav_results),'original_candidate_proposal_status_preserved':reg['GIR-FD82-A017']['candidate_decision']})

link_errors=[];link_results=[]
for x in author_validation['checked_new_relative_links']:
    # Author table stores already-normalized repository paths, not literal hrefs.
    source=data(TARGET,x['source']).decode()
    literal_hrefs=[h for h in re.findall(r'\]\(([^)]+)\)',source) if not h.startswith(('http:','https:','#'))]
    actual_targets={os.path.normpath(str(Path(x['source']).parent/h.split('#')[0])) for h in literal_hrefs}
    p=(ROOT/x['target']).resolve()
    present=p.is_relative_to(ROOT) and p.exists() and x['target'] in actual_targets
    link_results.append({**x,'exists_and_actual_Markdown_href_resolves_to_target':present})
    if not present:link_errors.append(x)
check('all_30_new_relative_links_resolve',len(link_results)==30 and not link_errors,{'errors':link_errors})
for x in paths(TARGET,STAGE):
    if x.endswith('.json'):obj(x)
check('all_6_integration_JSON_read_and_parse',len([x for x in paths(TARGET,STAGE) if x.endswith('.json')])==6,{'stage_files':len(paths(TARGET,STAGE)),'author_success_not_independent_approval':True})
locks=obj('review/remediation-20261003-prepare/stage-locks.json',PLAN)
b03=next(x for x in locks if x['stage']=='B03-A');b02i=next(x for x in locks if x['stage']=='B02-I')
check('B03_dependency_gate_correct_and_unchanged',b03['dependencies']==['B01-I','B02-I','PRE0'] and b02i['dependencies']==['B02-G'] and data(PLAN,'review/remediation-20261003-prepare/stage-locks.json')==data(TARGET,'review/remediation-20261003-prepare/stage-locks.json'),{'B03_dependencies':b03['dependencies'],'B02_I_dependencies':b02i['dependencies'],'job_dispatch':'PARENT_ONLY'})
check('no_B05_or_other_batch_changes_in_complete_diff',all(r['path'].startswith(B02) or r['path'] in formal+PUBLIC for r in full),{'unreviewed_B05_consumed':False,'other_batch_files_changed':0})
check('post_candidate_public_semantics_pending_not_borrowed_approval',manifest['integration_independent_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and registration['integration_review']=='PENDING_R_B02_ULTRA' and all(x['integration_verdict']=='NOT_REVIEWED_PENDING_ULTRA' for x in approval) and manifest['canonical_closed']==0 and manifest['downstream_gate']=='BLOCKED_PENDING_B02_I_AND_PARENT_FREEZE',{'manual_semantic_review':'report.md separately adjudicates exact new public text','canonical_closed':0})
whitespace=subprocess.run(['git','-C',str(ROOT),'diff','--check',CAND,TARGET,'--',*PUBLIC],capture_output=True)
check('public_actual_new_text_whitespace',whitespace.returncode==0,{'result':whitespace.stdout.decode()+whitespace.stderr.decode(),'raw_exact_patch_context_spaces':'evidence artifacts not prose'})

save('complete-diff-manifest.json',{'run_id':'20261003-prepare','reviewed_integration':TARGET,'reviewed_integration_tree':git('rev-parse',TARGET+'^{tree}').decode().strip(),'accepted_upstream':BASE,'candidate':CAND,'candidate_report':REPORT,'payload':PAYLOAD,'complete_actual_diffs':reconstructed,'upstream_complete_name_status':full,'candidate_complete_name_status':incremental,'evidence_complete_name_status':evidence,'all_changed_file_identities':[{'change':r['change'],**ident(TARGET,r['path'])} for r in full],'formal_preservation':formal_results,'stage_inputs':[ident(TARGET,p) for p in paths(TARGET,STAGE)],'report_commit_identity':'EXTERNAL_PUBLICATION_HANDOFF_NOT_SELF_REFERENCED'})
save('navigation-check.json',{'reviewed_integration':TARGET,'reference_sha':REF_SHA,'reference_tree':REF_TREE,'canonical_closed':False,'behavior_evidence':'path identity/ranges only; source semantics not inferred from existence','checks':nav_results})
save('new-link-check.json',{'reviewed_integration':TARGET,'checks':link_results})
save('independent-validation.json',{'reviewed_integration':TARGET,'accepted_upstream':BASE,'candidate':CAND,'result':'ALL_DOCUMENT_CHECKS_PASS' if all(x['ok'] for x in checks) else 'DOCUMENT_CHECK_FAILURE','manual_verdict':'report.md is authoritative scoped semantic decision','check_count':len(checks),'checks':checks,'reference_execution':0,'runtime_observations':0,'proven_demo_event_chains':0,'static_vectors_executed':0})
for x in checks:print(('PASS ' if x['ok'] else 'FAIL ')+x['check'])
if not all(x['ok'] for x in checks):raise SystemExit(1)
