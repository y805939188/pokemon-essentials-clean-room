"""Git/text/JSON identity checks only; no reference code or behavior vector runs.

Run from repository root with Python. Optional first argument is the separately
cloned read-only reference repository. Writes only this review directory.
"""
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
BASE = '0a12de641542f9a59909d2a950c1de8df17ca09d'
CAND = '46cd726c35e9d754a8e42b32986313ce3d4d1782'
V1 = '1c8027835e2be9057ca9040046e9ee986125ad04'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
GLOBAL = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
REF_SHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF_TREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
REF = Path(sys.argv[1] if len(sys.argv) > 1 else '/tmp/r-b02-reference').resolve()
PREFIX = 'review/remediation/20261003-prepare/batches/B02/'
GLOBAL_DIR = 'review/global-independent-review/2026-10-03-fd82a639/'
IDS = ['GIR-FD82-' + x for x in ['A006','A010','A011','A012','A013','A014','A015','A016','A017','A018','C003','C081']]
KERNEL = 'deliverables/final-specification-set/generic-kernel/'
FINAL = [KERNEL + x for x in ['wp06-stats-directory.md','wp06-time-random-steps-stats.md','wp07-diagnostics-files-http.md','wp08-localization.md','wp09-save-startup-continue.md','wp10-migration-failure-recovery.md']]
CAT = 'deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md'
FINAL.append(CAT)
ORIGINAL = ['specs/kernel/' + x for x in ['wp02-rule-configuration-and-data-variants.md','wp02-settings-inventory-appendix.md','wp06-stats-directory.md','wp07-diagnostics-files-http.md','wp08-localization.md','wp10-migration-failure-recovery.md']]
FORMAL = sorted(FINAL + ORIGINAL)
checks = []

def git(*args, repo=ROOT):
    return subprocess.check_output(['git', '-C', str(repo), *args])

def content(commit, path, repo=ROOT):
    return git('show', commit + ':' + path, repo=repo)

def parsed(commit, path):
    return json.loads(content(commit, path))

def digest(data):
    return hashlib.sha256(data).hexdigest()

def identity(commit, path, repo=ROOT):
    b = content(commit, path, repo)
    return {'commit': commit, 'path': path, 'git_blob': git('rev-parse', commit + ':' + path, repo=repo).decode().strip(), 'sha256': digest(b), 'bytes': len(b)}

def check(name, ok, evidence):
    checks.append({'check': name, 'ok': bool(ok), 'evidence': evidence, 'kind': 'INDEPENDENT_GIT_TEXT_JSON_CHECK_NOT_BEHAVIOR_TEST'})

def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

changed = git('diff','--name-status',BASE,CAND).decode().splitlines()
pairs = [s.split('\t') for s in changed]
check('candidate_parent_and_base', git('rev-parse',CAND+'^').decode().strip() == V1 and git('rev-parse',V1+'^').decode().strip() == BASE, {'candidate': CAND, 'parent': V1, 'full_base': BASE})
check('exact_full_13_formal_and_30_author_paths', sorted(p[1] for p in pairs if not p[1].startswith(PREFIX)) == FORMAL and all(p[0]=='M' if p[1] in FORMAL else p[0]=='A' and (p[1].startswith(PREFIX+'author/') or p[1].startswith(PREFIX+'author-v2/')) for p in pairs) and len(pairs)==43, {'changes': pairs})
check('reference_separate_fixed_clean', not REF.is_relative_to(ROOT) and git('rev-parse','HEAD',repo=REF).decode().strip()==REF_SHA and git('rev-parse','HEAD^{tree}',repo=REF).decode().strip()==REF_TREE and git('status','--porcelain=v1',repo=REF)==b'', {'repository':str(REF), 'sha':REF_SHA, 'tree':REF_TREE, 'origin':git('remote','get-url','origin',repo=REF).decode().strip(), 'execution':0})
plan_paths = git('ls-tree','-r','--name-only',PLAN,'review/remediation-20261003-prepare').decode().splitlines()
check('approved_plan_all_bytes_preserved', all(content(PLAN,p)==content(CAND,p) for p in plan_paths), {'paths':len(plan_paths), 'plan':PLAN})
v1_paths = git('ls-tree','-r','--name-only',V1,PREFIX+'author').decode().splitlines()
check('all_v1_author_and_seven_final_bytes_preserved', all(content(V1,p)==content(CAND,p) for p in v1_paths+FINAL), {'author_paths':len(v1_paths), 'final_paths':len(FINAL)})

patch = git('diff',BASE,CAND,'--','deliverables','specs')
(OUT/'full-formal.patch').write_bytes(patch)
manifest = parsed(CAND,PREFIX+'author-v2/candidate-manifest.json')
errors = []
for row in manifest['formal_files']:
    p=row['path']; actual=identity(CAND,p)
    if any(row[k]!=actual[k] for k in ['sha256','bytes']) or row['candidate_blob']!=actual['git_blob'] or row['initial_handoff_blob']!=identity(BASE,p)['git_blob'] or row['parent_blob']!=identity(V1,p)['git_blob']:
        errors.append(p)
check('author_v2_all_13_manifest_entries_independently_recomputed', not errors and sorted(x['path'] for x in manifest['formal_files'])==FORMAL, {'mismatches':errors})
check('author_full_diff_exact', digest(patch)==manifest['full_diff_sha256'], {'bytes':len(patch),'sha256':digest(patch)})
increment = git('diff',V1,CAND,'--','specs')
fd = parsed(CAND,PREFIX+'author-v2/formal-diff.json')
check('author_incremental_diff_exact', digest(increment)==manifest['incremental_diff_sha256'] and increment.decode()==fd['incremental_unified_diff'], {'sha256':digest(increment),'bytes':len(increment)})

expected_ops = {
 ORIGINAL[0]: [('replace',287,288)], ORIGINAL[1]: [('replace',199,200)], ORIGINAL[2]: [('replace',65,66)],
 ORIGINAL[3]: [('replace',44,45),('insert',160,160)],
 ORIGINAL[4]: [('replace',57,58),('replace',108,109),('insert',170,170)],
 ORIGINAL[5]: [('replace',113,114),('insert',201,201)]}
original_ops = []
for p in ORIGINAL:
    a=content(BASE,p).decode().splitlines(keepends=True); b=content(CAND,p).decode().splitlines(keepends=True)
    ops=[(t,i,j,k,l) for t,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes() if t!='equal']
    original_ops.append({'path':p,'operations':[{'kind':t,'base_start_1':i+1,'base_end_1':j,'candidate_start_1':k+1,'candidate_end_1':l} for t,i,j,k,l in ops]})
    check('authorized_original_clause_boundary:'+p, [(t,i,j) for t,i,j,k,l in ops]==expected_ops[p], original_ops[-1])

def rows(data):
    result={}
    for line in data.decode().splitlines():
        m=re.match(r'^\| ((?:EP|TM|IO|DP|LZ|SV|MG)\d+) \|',line)
        if m:
            if m[1] in result: raise ValueError('duplicate test ID '+m[1])
            result[m[1]]=line
    return result

old=content(BASE,CAT); new=content(CAND,CAT); before=rows(old); after=rows(new)
expected_changed={'TM09','TM12','LZ08','LZ09','LZ10','LZ11','LZ12','LZ13','LZ14','SV02','SV06','MG12'}
expected_new={'TM13','TM14','IO13','IO14','IO15','LZ15','LZ16','LZ17','MG13','MG14','MG15','MG16'}
check('catalog_only_12_assigned_existing_rows_changed_12_added_none_removed', {i for i in before if before[i]!=after.get(i)}==expected_changed and set(after)-set(before)==expected_new and not(set(before)-set(after)), {'changed':sorted(i for i in before if before[i]!=after.get(i)), 'added':sorted(set(after)-set(before)), 'removed':sorted(set(before)-set(after))})
for p,start,end in [('EP','## EP:','## TM:'),('DP','## DP:','## LZ:')]:
    def section(x):
        # Current repository headings use the fullwidth colon.
        t=x.decode(); s=t.index(start.replace(':','：')); e=t.index(end.replace(':','：')); return t[s:e].encode()
    a=section(old);b=section(new)
    check(p+'_entire_section_byte_preserved',a==b,{'sha256':digest(b),'bytes':len(b)})
counts={p:sum(i.startswith(p) for i in after) for p in ['EP','TM','IO','DP','LZ','SV','MG']}
check('catalog_99_rows_unique_sequential_three_columns',counts=={'EP':21,'TM':14,'IO':15,'DP':5,'LZ':17,'SV':11,'MG':16} and all([i for i in after if i.startswith(p)]==[p+f'{j:02d}' for j in range(1,n+1)] for p,n in counts.items()) and all(len(x.split('|'))==5 for x in after.values()),{'counts':counts,'total':len(after)})

def fields(data):
    return [(m[1],line) for line in data.decode().splitlines() if (m:=re.match(r'^\| ([a-z][a-z_]+) \|',line))]
for p in [KERNEL+'wp06-stats-directory.md','specs/kernel/wp06-stats-directory.md']:
    a=fields(content(BASE,p));b=fields(content(CAND,p))
    changes=[x[0] for x,y in zip(a,b) if x!=y]
    expected=['berry_plants_picked','max_yield_berry_plants','trade_count','play_time'] if p.startswith('deliverables') else ['trade_count']
    check('74_stat_field_identity_order_and_unrelated_rows:'+p,len(a)==len(b)==74 and [x[0] for x in a]==[x[0] for x in b] and changes==expected,{'changed_field_rows':changes,'count':len(b)})

# All existing static scenario rows of the three amended originals are preserved.
for p,expected_added in [(ORIGINAL[3],2),(ORIGINAL[4],3),(ORIGINAL[5],4)]:
    def table(x):
        t=x.decode().split('### 8.2')[-1] if p!=ORIGINAL[4] else x.decode().split('### 9.2')[-1]
        t=t.split('## 9.')[0] if p!=ORIGINAL[4] else t.split('## 10.')[0]
        return [line for line in t.splitlines() if line.startswith('| ') and not line.startswith('| ---')]
    a=table(content(BASE,p));b=table(content(CAND,p))
    check('original_old_static_rows_preserved:'+p, all(line in b for line in a) and len(b)-len(a)==expected_added, {'base_rows_including_header':len(a),'candidate_rows_including_header':len(b),'added':expected_added})
conversion='specs/kernel/wp10-migration-failure-recovery.md'
def conversions(data):
    return {m[1]:line for line in data.decode().splitlines() if (m:=re.match(r'^\| (v\d+_[a-z_]+) \|',line))}
a=conversions(content(BASE,conversion));b=conversions(content(CAND,conversion))
check('other_13_migration_conversion_rows_preserved',len(a)==len(b)==14 and [k for k in a if a[k]!=b[k]]==['v20_add_stats'],{'count':len(a)})
for p in ['specs/kernel/wp06-time-random-steps-stats.md','specs/kernel/wp09-save-startup-continue.md','specs/creature-rpg/wp26-acquisition-gifts-and-script-trade.md','deliverables/final-specification-set/creature-rpg/wp26-acquisition-gifts-and-script-trade.md','audit/source-traceability.md']:
    check('correct_original_or_shared_contract_unchanged:'+p,content(BASE,p)==content(CAND,p),identity(CAND,p))

original_findings={x['id']:x for x in parsed(GLOBAL,GLOBAL_DIR+'findings.json') if x['id'] in IDS}
accept=parsed(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
ai=parsed(CAND,PREFIX+'author/effective-finding-inputs.json')['selected_original_objects']
aa=parsed(CAND,PREFIX+'author/acceptance-inputs.json')['findings']
check('all_12_author_original_objects_equal_global_full_objects',{x['id']:x for x in ai}==original_findings,{'count':len(ai),'source':GLOBAL,'extensions':{k:len(v.get('extensions',[])) for k,v in original_findings.items()}})
check('all_12_author_acceptance_objects_equal_approved_plan',aa=={i:accept[i] for i in IDS},{'count':len(aa),'source':PLAN})
responses=parsed(CAND,PREFIX+'author-v2/finding-responses.json')['contributions']
proposals=parsed(CAND,PREFIX+'author-v2/registry-proposals.json')
check('IDs_priorities_aliases_primary_roles_preserved', {x['id'] for x in responses}==set(IDS) and all(x['priority']==original_findings[x['id']]['priority'] and x['aliases']==[r['raw_id'] for r in original_findings[x['id']]['raw_reports']] for x in responses) and sum(x['is_B02_primary'] for x in responses)==9, {'IDs':IDS,'primary_count':9})
check('no_author_self_approval_closure_or_public_mutation', all(not x['canonical_status_changed'] and not x['self_approval'] for x in responses) and proposals['closed_IDs']==0 and proposals['public_formal_changes_applied_by_author']==[] and proposals['unique_writer']=='A-REG', {'canonical_closed':0,'public_writer':'A-REG'})
scope=parsed(CAND,PREFIX+'author-v2/scope-expansion-authorization.json')
check('scope_expansion_only_six_paths_five_IDs', sorted(x['path'] for x in scope['clauses'])==sorted(ORIGINAL) and {i for x in scope['clauses'] for i in x['IDs']}=={'GIR-FD82-'+i for i in ['A006','A013','A011','A012','A016']}, {'authorization_is_behavior_approval':not scope['not_a_behavior_approval']})

path_results=[]
audit=content(CAND,'audit/source-traceability.md').decode().splitlines()
root_paths=parsed(GLOBAL,GLOBAL_DIR+'root/traceability-path-check.json')['wrong_directory_locations']
for p,r in zip(proposals['A017_eight_navigation_proposals_inherited'],root_paths):
    wrong='Data/Scripts/'+p['replace_path_only'];correct=p['replacement_full_reference_path']
    actual=identity(REF_SHA,correct,REF)
    path_results.append({'original_line':r['line'],'current_line':p['frozen_handoff_line'],'wrong':wrong,'correct':correct,'correct_identity':actual,'proposal_only':True,'original_reference_ranges':p['preserve_reference_ranges']})
    check('A017_path_proposal:'+str(r['line']),not(REF/wrong).exists() and (REF/correct).is_file() and p['replace_path_only']==r['claimed'] and correct==r['unique_basename_locations'][0] and p['replace_path_only'] in audit[p['frozen_handoff_line']-1] and all(actual[k]==p['correct_identity'][k] for k in actual),path_results[-1])

json_paths=[p[1] for p in pairs if p[1].startswith(PREFIX) and p[1].endswith('.json')]
for p in json_paths: parsed(CAND,p)
check('all_23_author_json_parse',len(json_paths)==23,{'count':len(json_paths)})
check('full_candidate_diff_whitespace', subprocess.run(['git','-C',str(ROOT),'diff','--check',BASE,CAND],capture_output=True).returncode==0,{'command':'git diff --check BASE CAND'})
remote=git('ls-remote','--heads','origin','refs/heads/remediation/20261003-prepare/batch-B02').decode().strip()
check('candidate_remote_exact_readback',remote.split()[0]==CAND,{'remote_readback':remote})
save('scope-manifest.json',{'run_id':'20261003-prepare','role':'R-B02','full_base':BASE,'candidate':CAND,'candidate_parent':V1,'candidate_tree':git('rev-parse',CAND+'^{tree}').decode().strip(),'global_review_base':'e1e01bb18d824931e54f182dd61af5a9f908ba85','global_report':GLOBAL,'approved_plan':PLAN,'reference':{'sha':REF_SHA,'tree':REF_TREE,'separate_git':True},'formal_files':[{'base':identity(BASE,p),'candidate':identity(CAND,p)} for p in FORMAL],'author_materials':[identity(CAND,p[1]) for p in pairs if p[1].startswith(PREFIX)],'formal_diff':{'sha256':digest(patch),'bytes':len(patch)},'original_clause_operations':original_ops,'publication_report_sha':'EXTERNAL_HANDOFF_AFTER_COMMIT_NOT_SELF_REFERENCED','candidate_remote_readback':remote})
save('a017-navigation-proposal-check.json',path_results)
save('original-finding-input-check.json',{'source_report':GLOBAL,'approved_plan':PLAN,'full_object_sha256':{i:digest(json.dumps(original_findings[i],sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()) for i in IDS},'acceptance_sha256':{i:digest(json.dumps(accept[i],sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()) for i in IDS},'complete_objects_preserved':True,'qualification_precedence':'current_qualifications/effective_case_constraints/final second review and extension adjudications','canonical_findings_closed':0})
save('independent-validation.json',{'candidate':CAND,'full_base':BASE,'result':'ALL_DOCUMENT_IDENTITY_CHECKS_PASS' if all(x['ok'] for x in checks) else 'DOCUMENT_CHECK_FAILURE','behavior_approval':'SEPARATE_MANUAL_STATIC_REVIEW','check_count':len(checks),'checks':checks,'runtime_observations':0,'proven_demo_event_chains':0,'reference_execution':0,'static_vectors_executed':0})
for x in checks:
    print(('PASS ' if x['ok'] else 'FAIL ')+x['check'])
if not all(x['ok'] for x in checks): sys.exit(1)
