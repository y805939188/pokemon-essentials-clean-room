#!/usr/bin/env python3
"""Audit frozen Git identities, document changes and protected bytes only.

No reference code, behavioral vector, interpreter, compiler or solver executes.
Semantic return review is reserved to the same independent R-B03 Ultra reviewer.
"""
import argparse
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
V3 = Path(__file__).resolve().parent
V1, V2 = V3.with_name('author'), V3.with_name('author-v2')
BASE = '9576f00e7d3aeb96f7ca8c42caccfba8f808505e'
PARENT = '76b6f6c6f14f1d676f370be72b61cb2f0a069633'
REVIEW = '4706be652a4d9e70656d1e2db1cbc0be9a9194c6'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
TREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
BRANCH = 'remediation/20261003-prepare/batch-B03'
OLD_PREFIXES = tuple(str(p.relative_to(ROOT))+'/' for p in [V1,V2])
NEW_PREFIX = str(V3.relative_to(ROOT))+'/'
CHECKS = []

def git(*args, repo=ROOT):
    return subprocess.check_output(['git','-C',str(repo),*args])
def sha(data):
    return hashlib.sha256(data).hexdigest()
def canonical_sha(value):
    return sha(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def read(name, directory=V3):
    return json.loads((directory/name).read_text())
def need(condition, label):
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)
def blob(rev, path):
    return git('show', rev+':'+path)
def rows(text, pattern):
    result = {}
    for line in text.splitlines():
        match = re.match(pattern,line)
        if match:
            need(match[1] not in result,'unique table ID '+match[1])
            result[match[1]]=line
    return result
def same_section(old, new, marker):
    def extract(text):
        start=text.index(marker)
        tail=text[start+len(marker):]
        end=re.search(r'^#{1,4} ',tail,re.M)
        return marker+(tail[:end.start()] if end else tail)
    need(extract(old)==extract(new),'protected section '+marker)

def run(ref):
    scope=read('scope.json',V1)
    manifest=read('input-manifest.json',V1)
    append=read('input-manifest.json')
    amendment=read('scope-amendment.json',V2)
    ledger=read('formal-edit-ledger.json')
    formal=amendment['authorized_formal_paths']
    originals=amendment['additional_formal_write_paths']
    need(git('branch','--show-current').decode().strip()==BRANCH,'own B03 branch only')
    need(git('merge-base',BASE,PARENT).decode().strip()==BASE,'accepted B02 base is ancestor of frozen parent')
    need(len(formal)==len(set(formal))==13,'13 approved formal paths')
    need(amendment['inherited_formal_write_paths']==scope['write_paths'],'original seven-path write lock')
    need(len(scope['read_paths'])==len(manifest['read_identities'])==57,'57 frozen stage reads')
    need(len(scope['contribution_finding_ids'])==27 and len(scope['primary_finding_ids'])==19,'27 original contributions and 19 primaries')
    stage_lock=next(x for x in json.loads(blob(BASE,'review/remediation-20261003-prepare/stage-locks.json')) if x['stage']=='B03-A')
    need(stage_lock['reads']==scope['read_paths'] and stage_lock['writes']==scope['write_paths'],'approved stage lock exact')
    changed=set(git('diff','--name-only',BASE).decode().splitlines())
    untracked=set(git('ls-files','--others','--exclude-standard').decode().splitlines())
    need(changed.intersection(formal)==set(formal),'complete candidate has all 13 formal paths versus B02')
    need(all(p in formal or p.startswith(OLD_PREFIXES+(NEW_PREFIX,)) for p in changed|untracked),'full scope whitelist, no public/historical or upstream edits')
    git('diff','--check',BASE)
    need(True,'complete diff has no whitespace errors')

    for item in manifest['read_identities']+manifest.get('supplementary_read_identities',[]):
        data=blob(item['commit'],item['path'])
        need(sha(data)==item['sha256'] and len(data)==item['bytes'],'frozen 57+1 input identity '+item['path'])
        need(git('rev-parse',item['commit']+':'+item['path']).decode().strip()==item['git_blob'],'frozen stage blob '+item['path'])
        if item.get('in_fix_base') and item['path'] not in formal:
            need((ROOT/item['path']).read_bytes()==data,'read-only upstream bytes '+item['path'])
    inherited_append=read('append-input-manifest.json',V2)
    for item in inherited_append['additional_read_identities']:
        data=blob(item['commit'] if 'commit' in item else inherited_append['append_parent_commit'],item['path'])
        need(sha(data)==item['sha256'] and len(data)==item['bytes'],'old v2 append identity '+item['path'])
    for collection in ['formal_input_identities','previous_author_files','review_input_identities']:
        for item in append[collection]:
            data=blob(item['commit'],item['path'])
            need(sha(data)==item['sha256'] and len(data)==item['bytes'],'v3 frozen identity '+item['path'])
            need(git('rev-parse',item['commit']+':'+item['path']).decode().strip()==item['git_blob'],'v3 frozen blob '+item['path'])
            if collection=='previous_author_files':
                need((ROOT/item['path']).read_bytes()==data,'old author immutable '+item['path'])
    expected_old=set(x['path'] for x in append['previous_author_files'])
    actual_old={str(p.relative_to(ROOT)) for directory in [V1,V2] for p in directory.iterdir() if p.is_file()}
    need(expected_old==actual_old and len(expected_old)==28,'both historical author directories exact 28-file set')
    review_paths=git('ls-tree','-r','--name-only',REVIEW,'--',str(V3.parent.relative_to(ROOT))+'/review-round-1/').decode().splitlines()
    need(set(review_paths)=={x['path'] for x in append['review_input_identities']} and len(review_paths)==12,'complete 12-file round1 frozen input')
    formal_increment=set(git('diff','--name-only',PARENT,'--',*formal).decode().splitlines())
    need(formal_increment==set(ledger['formal_increment_paths']) and len(formal_increment)==9,'exact nine-path formal return scope')
    for p in formal:
        old=blob(PARENT,p).decode()
        expected=old
        for edit in [x for x in ledger['edits'] if x['path']==p]:
            need(expected.count(edit['old'])==1,'unique frozen replacement '+p+':'+edit['clause'])
            need(set(edit['review_issues']).issubset({'R-B03-001','R-B03-002','R-B03-003'}),'edit belongs to one of three return issues')
            expected=expected.replace(edit['old'],edit['new'],1)
        need((ROOT/p).read_text()==expected,'all bytes outside exact return edit spans protected '+p)
    need(len(ledger['edits'])==17,'17 bounded paragraph/reference/append edits')

    histories=[]
    for p in originals:
        old,new=blob(PARENT,p).decode(),(ROOT/p).read_text()
        if '## 1.' in old:
            need(old[:old.index('## 1.')]==new[:new.index('## 1.')],'original history header exact '+p)
        marker='## 4. 证据与来源（traceability）' if p.endswith('move-route-matrix.md') else '## 10. 证据与来源（traceability）'
        if marker in old:
            tail=old[old.index(marker):]
            need(tail==new[new.index(marker):],'historical traceability/unknowns/approval suffix exact '+p)
            histories.append(dict(path=p,marker=marker,sha256=sha(tail.encode())))
    for p in [formal[1],formal[8]]:
        old,new=blob(PARENT,p).decode(),(ROOT/p).read_text()
        same_section(old,new,'### 4.1')
        same_section(old,new,'### 4.2')
    for p in [formal[3],formal[10]]:
        old,new=blob(PARENT,p).decode(),(ROOT/p).read_text()
        same_section(old,new,'### 3.2')
        same_section(old,new,'### 4.2')
        same_section(old,new,'### 6.2')
        same_section(old,new,'### 6.3')
    for p,markers in [(formal[2],['### 3.1','### 3.3','## 4.']),(formal[9],['### 2.1','### 2.3','## 3.'])]:
        old,new=blob(PARENT,p).decode(),(ROOT/p).read_text()
        for marker in markers: same_section(old,new,marker)

    numeric=r'^\| (\d+) \|'
    for p in [formal[2],formal[9]]:
        oldrows=rows(blob(PARENT,p).decode(),numeric)
        newrows=rows((ROOT/p).read_text(),numeric)
        need(oldrows==newrows and len(newrows)==96,'all 96 command rows exact '+p)
    matrix=rows((ROOT/formal[2]).read_text(),numeric)
    categories=dict(collections.Counter(l.split('|')[7].strip().strip('*') for l in matrix.values()))
    need(categories=={'有实现':66,'标记':2,'空操作':28},'314 non-noop and original 28/2/66 categories preserved')
    for p in [formal[4],formal[11]]:
        oldrows=rows(blob(PARENT,p).decode(),numeric)
        newrows=rows((ROOT/p).read_text(),numeric)
        need(oldrows==newrows and set(newrows)=={str(i) for i in range(46)},'all 46 route rows exact '+p)
        for literal in ['move_random_range','move_random_UD','move_random_LR']:
            need(literal in (ROOT/p).read_text(),'literal route prefix retained '+p+':'+literal)
    for p in [formal[3],formal[10]]:
        for literal in ['`sight(N)`/`trainer(N)`','`counter(N)`','`s:`']:
            need(literal in (ROOT/p).read_text(),'ASCII literal retained '+p+':'+literal)
    for p in [formal[0],formal[7],formal[5],formal[12]]:
        need((ROOT/p).read_bytes()==blob(PARENT,p),'entire WP11/WP14 unchanged '+p)

    cat=formal[6]
    base_cat,old_cat,new_cat=blob(BASE,cat),blob(PARENT,cat),(ROOT/cat).read_bytes()
    pattern=r'^\| ((?:MP|MV|EV|FW|IM|MR|DG)\d+) \|'
    base_rows,old_rows,new_rows=[rows(x.decode(),pattern) for x in [base_cat,old_cat,new_cat]]
    need(len(old_rows)==235 and all(new_rows.get(i)==v for i,v in old_rows.items()),'all 235 prior static vectors byte preserved')
    new_ids=set(new_rows)-set(old_rows)
    need(new_ids=={f'MV{i}' for i in range(68,78)}|{f'IM{i}' for i in range(36,42)},'exact 16 new combination/reverse static IDs')
    counts=dict(collections.Counter(re.sub(r'\d+$','',i) for i in new_rows))
    need(counts=={'MP':27,'MV':77,'EV':39,'FW':7,'IM':41,'MR':17,'DG':43},'251 B03 static vectors with continuous domains')
    for prefix,count in counts.items():
        need({i for i in new_rows if i.startswith(prefix)}=={prefix+f'{n:02d}' for n in range(1,count+1)},'continuous static ID domain '+prefix)
    tail=new_cat.split(b'## H.',1)[1]
    need(tail==old_cat.split(b'## H.',1)[1]==base_cat.split(b'## H.',1)[1] and sha(tail)=='b6408d8196cd78cca94d956a338af9475e50c133a72189b5ec7c582696f9831c','WP15/59/60 tail exact and frozen digest')
    for i in ['DG18','DG19','DG20','DG21','DG22']:
        need(new_rows[i]==base_rows[i],'B01 GR006 catalog baseline exact '+i)
    b01_final=next(l for l in blob(BASE,formal[5]).decode().splitlines() if l.startswith('- **大网格奇数参数调整'))
    b01_orig=next(l for l in blob(PARENT,formal[12]).decode().splitlines() if l.startswith('- **大网格奇数参数调整'))
    need(b01_final in (ROOT/formal[5]).read_text().splitlines() and b01_orig in (ROOT/formal[12]).read_text().splitlines(),'both respective B01 first odd-write failure paragraphs exact')

    effective=read('effective-finding-inputs.json',V1)
    original_objects={x['id']:x for x in json.loads(blob('93e10babe0b9c9ef8b3f5277754541b447beeeb4','review/global-independent-review/2026-10-03-fd82a639/findings.json'))}
    accepted=json.loads(blob('41fffb540c6483f5296ea0d33b789b75180d27ed','review/remediation-20261003-prepare/finding-acceptance.json'))
    for item in effective:
        need(item['complete_original_object']==original_objects[item['id']] and item['acceptance']==accepted[item['id']],'complete original/qualifications/valid rechecks/extensions/acceptance '+item['id'])
        need(canonical_sha(original_objects[item['id']])==item['original_object_sha256'],'original finding hash '+item['id'])
    round1=json.loads(blob(REVIEW,str(V3.parent.relative_to(ROOT))+'/review-round-1/finding-dispositions.json'))
    prior={x['id']:x for x in round1['dispositions']}
    responses=read('finding-responses.json')
    proposals=read('registry-proposals.json')
    issues=read('review-responses.json')
    need({x['id'] for x in responses}=={x['id'] for x in proposals['requests']}==set(scope['contribution_finding_ids']),'27 per-ID responses and registry suggestions')
    need(sum(x['primary_in_B03'] for x in responses)==19,'19 original primary findings preserved')
    protected_prior=[]
    for row in responses:
        need(row['complete_round_1_scoped_disposition']==prior[row['id']],'exact prior scoped disposition '+row['id'])
        if prior[row['id']]['verdict']=='PASS_SCOPED':
            ids=[x['id'] for x in prior[row['id']]['test_evidence']['rows']]
            need(all(new_rows[i]==old_rows[i] for i in ids),'all prior passing contribution vectors exact '+row['id'])
            protected_prior.append(dict(id=row['id'],static_vector_ids=ids))
    need(len(protected_prior)==26 and prior['GIR-FD82-C053']['verdict']=='REQUEST_CHANGES','26 local passes and C053 return preserved without acceptance rewrite')
    need({x['id'] for x in issues}=={'R-B03-001','R-B03-002','R-B03-003'},'three review-issue responses')
    for issue in issues:
        original=next(x for x in round1['new_findings'] if x['id']==issue['id'])
        need(issue['complete_first_round_finding']==original,'full independent counterexample retained '+issue['id'])
        need(all(i in new_ids for i in issue['static_vector_ids']),'issue points to new frozen static vectors '+issue['id'])
        need(issue['static_vectors_executed']==issue['runtime_observations']==issue['proven_demo_chains']==0 and not issue['canonical_edited'],'review response has no execution/canonical claim')
    need({x['id'] for x in proposals['new_distinct_root_proposals']}=={'R-B03-001','R-B03-002'},'two proposed new roots only')
    need(proposals['combination_aliases']==[{'observation':'R-B03-003','canonical_root':'GIR-FD82-C053','new_root_count_delta':0}] and proposals['original_aggregate_229_unchanged'] and proposals['canonical_mutations']==0,'C053 combination not duplicate root; global 229 untouched')

    links,tables=0,0
    for p in formal:
        text=(ROOT/p).read_text()
        need('```' not in text,'no reference-source code fences '+p)
        for target in re.findall(r'\[[^\]]+\]\(([^)]+\.md)(?:#[^)]*)?\)',text):
            if not re.match(r'[a-z]+:',target):
                need(((ROOT/p).parent/target).resolve().is_file(),'relative document link '+p+':'+target)
                links+=1
        for block in re.findall(r'(?:^\|[^\n]*\n)+',text,re.M):
            lines=block.splitlines()
            need(len(lines)>1 and re.match(r'^\|(?:\s*:?-+:?\s*\|)+$',lines[1]),'contiguous table header '+p)
            tables+=1
    need(not ref.is_relative_to(ROOT) and not ref.is_relative_to(Path('/workspace/pokemon-essentials-clean-room')),'reference is outside both project repositories')
    need(git('rev-parse','HEAD',repo=ref).decode().strip()==REFERENCE and git('rev-parse','HEAD^{tree}',repo=ref).decode().strip()==TREE,'fixed reference HEAD/tree')
    need(not git('status','--porcelain',repo=ref).strip(),'reference remains clean')
    source_logs=read('source-reading-log.json',V1)+read('source-reading-log.json',V2)+read('source-reading-log.json')
    for item in source_logs:
        data=(ref/item['path']).read_bytes()
        need(sha(data)==item['sha256'] and len(data)==item['bytes'],'source metadata identity '+item['path'])
        need(git('rev-parse','HEAD:'+item['path'],repo=ref).decode().strip()==item['git_blob'],'source blob identity '+item['path'])
    receipt=read('execution-request-receipt.json')
    need(receipt['requested_model']=='gpt-6.1-sol' and receipt['requested_reasoning']=='Max' and receipt['requested_speed']=='Standard/default','requested author model/Max/Standard retained')
    need(all(receipt['actual_effective_'+k]=='UNVERIFIED' for k in ['model','reasoning','speed']) and receipt['max_unsupported_evidence'] is None and not receipt['fallback_requested'] and receipt['subagents_spawned']==0,'strategy A effective config UNVERIFIED, no fallback/delegation')
    return dict(result='PASS_DOCUMENT_AND_GIT_IDENTITY_AUDIT',semantic_review_status='AUTHOR_V3_AWAITING_SAME_R_B03_ULTRA_PROBLEM_AND_REGRESSION_RECHECK',audit_type='Document/Git frozen identity and byte protection only; never behavioral execution',checks=len(CHECKS),fix_base_commit=BASE,append_parent_commit=PARENT,review_input_commit=REVIEW,formal_write_count=13,formal_increment_count=9,formal_increment_paths=sorted(formal_increment),formal_payload=[dict(path=p,sha256=sha((ROOT/p).read_bytes()),bytes=len((ROOT/p).read_bytes())) for p in formal],frozen_stage_read_count=57,supplementary_historical_read_count=1,round1_review_files_verified=12,previous_author_files_byte_preserved=28,complete_original_and_acceptance_objects_verified=27,original_contribution_count=27,original_primary_count=19,prior_PASS_SCOPED_contributions_byte_protected=protected_prior,review_issue_count=3,new_distinct_root_proposals=2,C053_combination_alias='R-B03-003; new root delta0',static_vector_counts=counts,static_vectors_total=len(new_rows),prior_static_vectors_byte_preserved=len(old_rows),new_static_vectors_since_author_v2=len(new_ids),new_static_vector_ids=sorted(new_ids),new_static_vectors_since_B02=len(new_rows)-len(base_rows),WP15_WP59_WP60_tail_sha256=sha(tail),B01_original_paragraph_sha256=sha(b01_orig.encode()),B01_final_paragraph_sha256=sha(b01_final.encode()),protected_original_history=histories,interpreter_rows_exact=96,interpreter_categories=categories,move_route_rows_exact=46,relative_links_checked=links,markdown_tables_checked=tables,reference_commit=REFERENCE,reference_tree=TREE,reference_clean=True,reference_files_in_inherited_and_new_read_logs=len({x['path'] for x in source_logs}),inherited_source_read_operations=51,new_source_read_operations=13,all_existing_paths_outside_scope_unchanged=True,canonical_and_public_registry_mutations=0,original_aggregate_229_unchanged=True,runtime_observations=0,proven_demo_chains=0,static_vectors_executed=0,reference_or_solver_execution=False,effective_execution_configuration='UNVERIFIED; strategy A')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--reference',default='/workspace/reference-B03-20261003-prepare')
    parser.add_argument('--report')
    args=parser.parse_args()
    result=run(Path(args.reference).resolve())
    target=Path(args.report) if args.report else V3/'self-check-result.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    omit={'formal_payload','protected_original_history','prior_PASS_SCOPED_contributions_byte_protected'}
    print(json.dumps({k:v for k,v in result.items() if k not in omit},ensure_ascii=False,indent=2))
