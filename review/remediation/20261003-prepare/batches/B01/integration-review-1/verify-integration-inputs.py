"""R-B01 independent Git/text identity checks; never execute reference programs.

Run from the main repository. Reads only immutable input objects and an independently
cloned reference; writes evidence only in this report directory. No behavioral test
vectors, game logic, compiler, converter, deserializer or solver are executed.
"""
import csv
import hashlib
import json
import posixpath
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
REF = Path('/workspace/reference-r-b01-integration-independent')
I = '93d0714ddfdb4900e946c0acd1cc80cf6431f0a0'
C = 'c7e30a1197083e86315d735fcfde5e31574d935a'
R = 'c919657840bb09394ce03a8a8688b02666f030dc'
P = '8f3a811855fc43b5fe5eb7809931b4e1749200de'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
BASE = 'e1e01bb18d824931e54f182dd61af5a9f908ba85'
ORIGINAL = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
MERGE = '56a2391b49156abbf81b8e8f0add5ac7a9e5bff0'
D = 'review/remediation/20261003-prepare/'
B = D + 'batches/B01/'
FINDINGS = 'review/global-independent-review/2026-10-03-fd82a639/findings.json'
checks = []

def git(*args, root=ROOT):
    return subprocess.check_output(['git', *args], cwd=root)

def read(commit, path):
    return git('show', commit + ':' + path)

def obj(commit, path):
    return json.loads(read(commit, path))

def digest(b):
    return hashlib.sha256(b).hexdigest()

def identity(path, commit=I):
    b = read(commit, path)
    return dict(path=path, git_blob=git('rev-parse', commit + ':' + path).decode().strip(),
                sha256=digest(b), bytes=len(b), lines=len(b.splitlines()))

def check(name, ok, evidence):
    checks.append(dict(check=name, result='PASS' if ok else 'FAIL', evidence=evidence))

def names(a, b):
    return git('diff', '--name-only', a, b).decode().splitlines()

def tsv(commit, path):
    return list(csv.DictReader(read(commit, path).decode().splitlines(), delimiter='\t'))

def rows(commit, path):
    out = {}
    for line in read(commit, path).decode().splitlines():
        m = re.match(r'^\| ([A-Z]{2}\d+) \|', line)
        if m:
            if m[1] in out:
                raise ValueError('duplicate catalog ID: ' + m[1])
            out[m[1]] = line
    return out

def audit_targets(text):
    # These historical prose references are code-span paths, not clickable links.
    # Parse complete delimited tokens; a two-level path must never match the suffix
    # of a correct three-level token. Also support explicit Markdown link targets.
    return (re.findall(r'`((?:\.\./)+audit/source-traceability\.md)`',text) +
            re.findall(r'\]\(((?:\.\./)+audit/source-traceability\.md)\)',text))

def write(name, data):
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

m = obj(I, D+'integration-manifest.json')
prior = obj(R, B+'review-round-1/finding-dispositions.json')
batch = obj(PLAN, 'review/remediation-20261003-prepare/batches.json')[0]
stages = {s['stage']:s for s in obj(PLAN, 'review/remediation-20261003-prepare/stage-locks.json')}
formal = [e['path'] for e in m['accepted_formal_inputs']]
public = m['relative_to_candidate_public_edits'] + m['relative_to_candidate_public_new_records']
full = names(P, I)
candidate_changes = names(P, C)
review_records = names(C, R)
author_records = [p for p in candidate_changes if p.startswith(B)]
remote = {}
for line in git('ls-remote', '--heads', 'origin', 'main',
                'remediation/20261003-prepare/integration',
                'remediation/20261003-prepare/batch-B01',
                'remediation/20261003-prepare/review-B01-1').decode().splitlines():
    sha, ref = line.split('\t'); remote[ref] = sha
check('remote frozen inputs and main verified independently',
      remote.get('refs/heads/main') == BASE and
      remote.get('refs/heads/remediation/20261003-prepare/integration') == I and
      remote.get('refs/heads/remediation/20261003-prepare/batch-B01') == C and
      remote.get('refs/heads/remediation/20261003-prepare/review-B01-1') == R, remote)
check('integration direct parent and preserving merge two parents',
      git('rev-parse', I+'^').decode().strip() == MERGE and
      git('show','-s','--format=%P',MERGE).decode().split() == [P,R],
      dict(integration=I,parent=MERGE,merge_parents=git('show','-s','--format=%P',MERGE).decode().split()))
check('preserving merge tree equals independently reviewed candidate report tree',
      git('rev-parse', MERGE+'^{tree}') == git('rev-parse',R+'^{tree}'),
      dict(merge_tree=git('rev-parse',MERGE+'^{tree}').decode().strip(),
           candidate_report_tree=git('rev-parse',R+'^{tree}').decode().strip(),
           limit='tree equality proves no version discarded; transient merge worktree history is not independently observed'))
check('PRE0 parent equals approved plan and review report directly follows candidate',
      git('rev-parse',P+'^').decode().strip() == PLAN and git('rev-parse',R+'^').decode().strip() == C,
      dict(PRE0=P,plan=PLAN,review_report=R,candidate=C))
check('complete PRE0 integration scope reconstructed independently',
      len(full)==59 and len(candidate_changes)==38 and len(author_records)==30 and
      len(review_records)==6 and len(public)==15 and
      set(full)==set(formal+author_records+review_records+public),
      dict(total=len(full),formal=len(formal),author=len(author_records),candidate_review=len(review_records),public=len(public),paths=full))
check('exact 15 public paths added after candidate review, within approved B01-G writes',
      names(R,I)==sorted(public) and set(public)<=set(stages['B01-G']['writes']), public)
check('all eight formal inputs byte identical at candidate review and actual integration',
      len(formal)==8 and all(read(C,p)==read(R,p)==read(I,p) for p in formal), [identity(p) for p in formal])
check('all thirty author and six independent candidate review records byte immutable',
      all(read(C,p)==read(I,p) for p in author_records) and
      all(read(R,p)==read(I,p) for p in review_records), dict(author=author_records,review=review_records))
patch = git('diff',P,I,'--',*formal)
check('complete formal diff equals full candidate diff, rather than incremental candidate delta',
      patch==git('diff',P,C,'--',*formal) and patch==read(C,B+'author-v2/formal-diff.patch'),
      dict(bytes=len(patch),sha256=digest(patch)))
patch_all = git('diff',P,I)
patch_public = git('diff',R,I)
(OUT/'PRE0-to-integration.patch').write_bytes(patch_all)
(OUT/'candidate-review-to-integration-public.patch').write_bytes(patch_public)
history_paths = ['planning/review-manifest-2026-09-19.md',
                 'review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv',
                 D+'global-premises.json',D+'model-request-receipts.json',D+'PRE0-handoff.md']
check('dated manifest current-hashes and PRE0 records remain byte immutable',
      all(read(P,p)==read(I,p) for p in history_paths),[identity(p) for p in history_paths])
check('approved plan identity immutable',not git('diff','--name-only',PLAN,I,'--','review/remediation-20261003-prepare'),PLAN)
reference_identity = dict(path=str(REF),commit=git('rev-parse','HEAD',root=REF).decode().strip(),
                          tree=git('rev-parse','HEAD^{tree}',root=REF).decode().strip(),
                          remote=git('remote','get-url','origin',root=REF).decode().strip(),
                          clean=not git('status','--porcelain',root=REF))
check('independently cloned outside-main fixed reference remains read-only clean',
      reference_identity['commit']==REFERENCE and reference_identity['tree']=='7589c800b61ba13a13040ed0d686979b80a84fd0' and
      reference_identity['remote']=='https://github.com/Maruno17/pokemon-essentials.git' and reference_identity['clean'],reference_identity)
for key, expected_count in [('accepted_formal_inputs',8),('current_original_dependencies',8),
                            ('current_public_input_identity',7),('public_successor_record_hashes',7),
                            ('independent_review_record_identities',6)]:
    errors=[]
    for e in m[key]:
        a=identity(e['path'])
        for k in ('sha256','git_blob','bytes','lines'):
            if k in e and e[k]!=a[k]:errors.append([e['path'],k,e[k],a[k]])
        if 'previous_candidate_sha256' in e and e['previous_candidate_sha256']!=identity(e['path'],C)['sha256']:
            errors.append([e['path'],'previous_candidate_sha256'])
    check('manifest exact current identities: '+key,len(m[key])==expected_count and not errors,
          dict(count=len(m[key]),mismatches=errors))
check('current dependency originals unchanged from candidate and PRE0, with no approval transferred',
      all(read(P,e['path'])==read(C,e['path'])==read(I,e['path']) for e in m['current_original_dependencies']),
      [e['path'] for e in m['current_original_dependencies']])
check('public successor identities omit self-referential manifest',
      D+'integration-manifest.json' not in [e['path'] for e in m['public_successor_record_hashes']] and
      m['candidate_commit']==C and m['candidate_review_commit']==R and m['PRE0_COMMIT']==P and
      m['approved_PLAN_FIX_BASE']==PLAN and m['original_REVIEW_BASE']==BASE and
      m['original_REVIEW_REPORT']==ORIGINAL and m['reference_commit']==REFERENCE,
      dict(manifest_identity=identity(D+'integration-manifest.json'),integration_commit_field=m['integration_commit']))
canon=obj(ORIGINAL,FINDINGS)
by_id={e['id']:e for e in canon}
ids=batch['contribution_finding_ids']
required=[e for e in canon if e['required_revision']]
acceptance=obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
old_objects=obj(C,B+'author/original-findings.json')
check('all fourteen complete canonical original objects including qualifications adjudications extensions retained',
      {e['id']:e for e in old_objects}=={i:by_id[i] for i in ids} and
      all(hashlib.sha256(json.dumps(by_id[e['id']],sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
          ==e['original_object_source']['canonical_object_sha256_sorted_json'] for e in prior['dispositions']),
      dict(ids=ids,canonical_identity=identity(FINDINGS,ORIGINAL)))
check('approved acceptance overlapping canonical effective fields unaltered',
      all(by_id[i][k]==v for i in ids for k,v in acceptance[i].items() if k in by_id[i]),dict(count=14,plan=PLAN))
check('canonical original and plan responsibility counts preserved',
      len(canon)==233 and len(required)==229 and sum(e['priority']=='P2' for e in required)==200 and
      sum(e['priority']=='P3' for e in required)==29 and len(ids)==14 and len(batch['primary_finding_ids'])==7,
      dict(canonical=233,required=229,P2=200,P3=29,nonrequired=4,primary=batch['primary_finding_ids']))
ledger=tsv(I,D+'finding-ledger.tsv'); old_ledger=tsv(P,D+'finding-ledger.tsv')
old_l={e['finding_id']:e for e in old_ledger}
changed=[e['finding_id'] for e in ledger if e!=old_l[e['finding_id']]]
unchanged_columns=['finding_id','priority','required_revision','primary_owner','contributor_batches','source_status','canonical_state','closure_gate']
check('all229 required IDs OPEN and exactly14 permitted workflow updates; other215 unchanged',
      len(ledger)==229 and {e['finding_id'] for e in ledger}=={e['id'] for e in required} and
      all(e['canonical_state']=='OPEN' for e in ledger) and set(changed)==set(ids) and
      all(e[k]==old_l[e['finding_id']][k] for e in ledger for k in unchanged_columns),
      dict(rows=len(ledger),changed_ids=changed,unchanged_rows=229-len(changed)))
approval=tsv(I,D+'approval-ledger.tsv'); trace=tsv(I,D+'traceability-successor.tsv')
pd={e['id']:e for e in prior['dispositions']}
check('approval rows bind candidate scope to correct reviewer/report; current integration still pending at author snapshot',
      {e['finding_id'] for e in approval}==set(ids) and len(approval)==14 and
      all(e['canonical_state']=='OPEN' and e['candidate_commit']==C and e['candidate_review_commit']==R and
          e['candidate_reviewer']=='R-B01' and e['candidate_verdict']=='PASS_SCOPED' and
          e['accepted_contribution_kind']==pd[e['finding_id']]['disposition'] and
          e['public_registration_verdict']=='PENDING_INTEGRATION_ULTRA' and
          e['integration_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and e['downstream_gate']=='BLOCKED' for e in approval),approval)
all_test_ids={}
for p in formal[4:6]:all_test_ids.update(rows(I,p))
trace_errors=[]
for e in trace:
    if not(e['canonical_state']=='OPEN' and e['original_report_commit']==ORIGINAL and
           e['candidate_commit']==C and e['candidate_review_commit']==R and
           e['effective_priority']==by_id[e['finding_id']]['priority'] and
           e['accepted_candidate_contribution']==pd[e['finding_id']]['disposition']):trace_errors.append(e['finding_id'])
    for t in e['static_test_ids_not_executed'].split(';'):
        if t and t not in all_test_ids:trace_errors.append([e['finding_id'],t])
    for target in e['current_clause_inputs'].split(';'):
        if target and target.split(' §')[0] not in formal:trace_errors.append([e['finding_id'],target])
check('all fourteen current traceability rows bind original/candidate/review identities and existing clauses/tests',
      len(trace)==14 and {e['finding_id'] for e in trace}==set(ids) and not trace_errors,dict(rows=14,errors=trace_errors))
check('manifest freezes fourteen historical dispositions exactly, separate from current integration state',
      m['independent_candidate_dispositions_frozen_at_review']==prior['dispositions'] and
      len(m['current_per_id_integration_registration_state'])==14 and
      {e['finding_id'] for e in m['current_per_id_integration_registration_state']}==set(ids) and
      all(e['canonical_state']=='OPEN' and not e['closed'] and e['candidate_commit']==C and
          e['candidate_review_commit']==R and e['candidate_disposition']==pd[e['finding_id']]['disposition'] and
          e['actual_integration_state']=='INTEGRATED_PENDING_ULTRA' and
          e['new_public_registration_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and e['downstream']=='BLOCKED'
          for e in m['current_per_id_integration_registration_state']),
      dict(count=14,new_verdict='NOT_REVIEWED_PENDING_ULTRA',canonical_closed=0))
old_rows={}
for p in formal[4:6]:old_rows.update(rows(P,p))
new_ids=sorted(set(all_test_ids)-set(old_rows)); changed_rows=sorted(k for k in old_rows if old_rows[k]!=all_test_ids.get(k))
check('20 added static IDs three existing row edits zero deletions; shared non-EP rules unchanged',
      set(new_ids)=={'KC06','KR13',*['KL'+str(n) for n in range(19,33)],*['EP'+str(n) for n in range(18,22)]} and
      changed_rows==['EP07','EP08','KL10'] and not(set(old_rows)-set(all_test_ids)) and
      all(old_rows[k]==all_test_ids[k] for k in rows(P,formal[5]) if not k.startswith('EP')),
      dict(added=new_ids,changed=changed_rows,total=len(all_test_ids),vectors_executed=0))
counts=obj(I,D+'scope-counts.json')
inventory=git('ls-tree','-r','--name-only',I,'--','deliverables/final-specification-set').decode().splitlines()
md=[p for p in inventory if p.endswith('.md')]
catalog=[p for p in md if '/test-catalog/' in p and not p.endswith('/README.md')]
behavior=[p for p in md if '/test-catalog/' not in p and not p.endswith('/README.md') and not p.endswith('/scope-statement.md')]
check('scope-counts current Git inventory and static catalog row counts are accurate',
      len(md)==counts['current_final_set_markdown_files']==131 and len(behavior)==counts['current_final_behavior_markdown_files']==111 and
      len(catalog)==counts['static_catalog_files']==17 and len(rows(I,formal[4]))==counts['B01_catalogs'][0]['rows']==51 and
      len(rows(I,formal[5]))==counts['B01_catalogs'][1]['rows']==87 and counts['B01_related_catalog_rows']==138 and
      counts['canonical_required_open']==229 and counts['canonical_closed']==0,
      dict(all_markdown=len(md),behavior_markdown=len(behavior),catalogs=len(catalog),B01_rows=[51,87],historical_source_inputs=113))
raw=next(e for e in by_id['GIR-FD82-001']['raw_reports'] if e['raw_id']=='RUN-C-132')
canonical_seven=[e['path'] for e in raw['evidence'] if e.get('note')=='错误相对审计路径']
all_tree=set(git('ls-tree','-r','--name-only',I).decode().splitlines())
links=[]
for p in canonical_seven:
    actual=audit_targets(read(I,p).decode())
    target=actual[0] if len(actual)==1 else None
    resolved=posixpath.normpath(posixpath.join(posixpath.dirname(p),target)) if target else None
    correct=posixpath.normpath(posixpath.join(posixpath.dirname(p),'../../../audit/source-traceability.md'))
    links.append(dict(path=p,actual_targets=actual,resolved_actual=resolved,actual_exists=resolved in all_tree,
                      corrected=correct,corrected_exists=correct in all_tree,identity=identity(p),
                      unchanged_from_original=read(BASE,p)==read(P,p)==read(C,p)==read(I,p)))
check('canonical actual seven broken links, exact parsed targets and valid three-level controls',
      len(links)==7 and all(e['actual_targets']==['../../audit/source-traceability.md'] and
          not e['actual_exists'] and e['corrected_exists'] and e['unchanged_from_original'] for e in links) and
      set(canonical_seven)=={e['path'] for e in m['deferred_seven_audit_links']} and
      all(e['sha256']==identity(e['path'])['sha256'] and e['old_target']=='../../audit/source-traceability.md' and
          e['correct_target']=='../../../audit/source-traceability.md' and not e['old_target_exists'] and
          e['correct_target_exists'] for e in m['deferred_seven_audit_links']),links)
voltorb='deliverables/final-specification-set/pokemon-rules/wp69-voltorb-layouts.md'
vol_targets=audit_targets(read(I,voltorb).decode())
check('Voltorb is correct control rather than a broken member; reviewer prior supporting check superseded',
      vol_targets==['../../../audit/source-traceability.md'] and
      posixpath.normpath(posixpath.join(posixpath.dirname(voltorb),vol_targets[0])) in all_tree and
      voltorb not in canonical_seven,dict(path=voltorb,actual_targets=vol_targets,successor_erratum='R-B01-I-ERR01'))
public_links=[]
for p in public:
    if not p.endswith('.md'):continue
    for target in re.findall(r'\]\(([^)\s]+)\)',read(I,p).decode()):
        if target.startswith(('https://','http://','mailto:','#')):continue
        rel=target.split('#')[0]
        normalized=posixpath.normpath(posixpath.join(posixpath.dirname(p),rel))
        exists=normalized in all_tree or any(x.startswith(normalized.rstrip('/')+'/') for x in all_tree)
        public_links.append(dict(path=p,target=target,resolved=normalized,exists=exists))
check('all local file/directory Markdown targets in changed/new public Markdown resolve',
      bool(public_links) and all(e['exists'] for e in public_links),dict(count=len(public_links),failed=[e for e in public_links if not e['exists']]))
check('current user-interface directory navigation exact target exists',
      '[user-interface/](user-interface/)' in read(I,'deliverables/final-specification-set/README.md').decode(),
      dict(target='deliverables/final-specification-set/user-interface',git_directory_exists=any(p.startswith('deliverables/final-specification-set/user-interface/') for p in all_tree)))
hist_rows=[]
for line in read(I,history_paths[1]).decode().splitlines():
    if line.startswith('#'):continue
    fields=line.split('\t')
    if len(fields)==3 and fields[2] in formal:
        h,n,p=fields
        hist_rows.append(dict(path=p,historical_sha256=h,historical_bytes=int(n),
                              matches_PRE0=(h==identity(p,P)['sha256'] and int(n)==identity(p,P)['bytes']),
                              matches_integration=(h==identity(p,I)['sha256'] and int(n)==identity(p,I)['bytes']),
                              current_successor=identity(p)))
check('six catalog/final historical current-hashes rows bind old PRE0 bytes; successor carries all eight current identities',
      len(hist_rows)==6 and {e['path'] for e in hist_rows}==set(formal[:6]) and
      all(e['matches_PRE0'] and not e['matches_integration'] for e in hist_rows),
      dict(rows=hist_rows,limit='two original WP04/WP05 identities reside in dated manifest/audit, not this six-row TSV slice'))
original_historic=[]
dated=read(I,history_paths[0]).decode().splitlines()
for p in formal[6:]:
    line=next(line for line in dated if line.startswith('| `'+p+'`') and len(re.findall(r'`[0-9a-f]{64}`',line))==1)
    h=re.findall(r'`([0-9a-f]{64})`',line)[0]
    n=int(line.split('|')[-2].strip().replace(',',''))
    original_historic.append(dict(path=p,old_sha256=h,old_bytes=n,old_matches_PRE0=h==identity(p,P)['sha256'] and n==identity(p,P)['bytes'],
                                 distinct_current_identity=identity(p),old_matches_current=h==identity(p)['sha256']))
check('dated WP04/WP05 identities explicitly bind old bytes rather than newly approved content',
      len(original_historic)==2 and all(e['old_matches_PRE0'] and not e['old_matches_current'] for e in original_historic),original_historic)
cm=obj(I,D+'candidate-manifest.json')
check('root candidate manifest binds eight formal identities to fixed candidate report',
      cm['candidate_commit']==C and cm['candidate_review_commit']==R and
      cm['candidate_verdict']=='PASS_SCOPED' and len(cm['formal_files'])==8 and
      [e['path'] for e in cm['formal_files']]==formal and
      all(e['candidate_git_blob']==identity(e['path'])['git_blob'] and
          e['candidate_sha256']==identity(e['path'])['sha256'] and e['bytes']==identity(e['path'])['bytes'] and
          e['complete_review_base_blob']==identity(e['path'],P)['git_blob'] for e in cm['formal_files']),
      dict(keys=list(cm),candidate=C,review=R))
check('author snapshot zero execution and inherited unverified ranges preserved',
      m['reference_programs_executed']==m['runtime_observations']==m['proven_demo_event_chains']==m['static_vectors_executed']==0 and
      m['canonical_findings_required_open']==229 and m['canonical_findings_closed']==0 and
      m['downstream_gate']=='BLOCKED' and not m['B02_B05_started'],
      dict(inherited=m['inherited_limits'],model_request=m['model_request'],counts=counts))
scope_path='deliverables/final-specification-set/scope-statement.md'
def scope_sections(commit):
    out={}; heading=None
    for line in read(commit,scope_path).decode().splitlines():
        if line.startswith('## '):heading=line
        out.setdefault(heading,[]).append(line)
    return out
old_scope=scope_sections(R); current_scope=scope_sections(I)
protected=[h for h in old_scope if h and h.startswith(('## 2.','## 3.','## 4.'))]
section5=next(h for h in old_scope if h and h.startswith('## 5.'))
check('scope unknown tables and discipline sections2/3/4 unchanged; section5 evidence limits retained',
      len(protected)==3 and all(old_scope[h]==current_scope[h] for h in protected) and
      all(line in current_scope[section5] for line in old_scope[section5][:4]),
      dict(unchanged_sections=protected,section5_changed=old_scope[section5]!=current_scope[section5],
           reason='section5 completion status and successor navigation intentionally updated, no new runtime evidence'))
claim=next(e for e in m['author_validation']['checks'] if e['check']=='scope preserves all unverifiable tables, evidence levels and clean-room discipline')
check('author sections2/3/4 exact evidence assertion is factually true',
      all(old_scope[h]==current_scope[h] for h in protected),
      dict(author_claim=claim,actual_section5_heading=section5,
           reviewer_checker_development_correction='completion is section5, not section4; provisional concern rejected by exact section equality; no new finding'))
check('B02/B05 author stages depend on actual B01-I and PRE0; reviewer writes no formal paths',
      stages['B02-A']['dependencies']==stages['B05-A']['dependencies']==['B01-I','PRE0'] and
      stages['B01-I']['writes']==[] and stages['B01-C']['dependencies']==['B01-I'],
      {k:{x:v for x,v in stages[k].items() if x!='reads'} for k in ['B01-I','B01-C','B02-A','B05-A']})
ws=subprocess.run(['git','diff','--check',P,I,'--',*formal,*public],cwd=ROOT,capture_output=True,text=True)
check('all eight formal and fifteen public input changes have no Git whitespace errors',ws.returncode==0,dict(output=ws.stdout+ws.stderr))
raw_ws=subprocess.run(['git','diff','--check',P,I],cwd=ROOT,capture_output=True,text=True)
raw_paths={line.split(':')[0] for line in raw_ws.stdout.splitlines() if line.startswith('review/')}
check('full-diff whitespace diagnostics limited to immutable exact author patch payloads',
      raw_ws.returncode==2 and raw_paths=={B+'author/formal-diff.patch',B+'author-v2/formal-diff.patch',B+'author-v2/incremental-formal-diff.patch'},
      dict(paths=sorted(raw_paths),diagnostic_lines=len(raw_ws.stdout.splitlines()),
           reason='stored unified-diff blank context lines are a space; preserving exact patch bytes is intentional',
           not_a_formal_text_whitespace_failure=True))
write('independent-validation.json',dict(reviewer='R-B01',reviewed_integration_commit=I,complete_diff_base=P,
      kind='independent Git/JSON/text metadata checks only; semantic judgments in report.md',checks=checks,
      PASS=sum(e['result']=='PASS' for e in checks),FAIL=sum(e['result']=='FAIL' for e in checks),
      reference_programs_executed=0,runtime_observations=0,proven_demo_event_chains=0,static_vectors_executed=0,
      prior_evidence_correction='R-B01-I-ERR01; prior nav enumeration check not valid and superseded'))
write('scope-manifest.json',dict(reviewed_integration_commit=I,reviewed_integration_tree=git('rev-parse',I+'^{tree}').decode().strip(),
      complete_diff_base=P,candidate_commit=C,candidate_review_report_commit=R,
      complete_name_status=git('diff','--name-status',P,I).decode().splitlines(),
      formal_identities=[identity(p) for p in formal],public_identities=[identity(p) for p in public],
      author_paths_unchanged=author_records,candidate_review_paths_unchanged=review_records,
      patch_identities=[dict(path='PRE0-to-integration.patch',bytes=len(patch_all),sha256=digest(patch_all)),
                        dict(path='candidate-review-to-integration-public.patch',bytes=len(patch_public),sha256=digest(patch_public))],
      reference=reference_identity,remote_inputs=remote,canonical_seven_audit_links=links))
print(json.dumps(dict(PASS=sum(e['result']=='PASS' for e in checks),FAIL=[e['check'] for e in checks if e['result']=='FAIL']),ensure_ascii=False))
raise SystemExit(any(e['result']=='FAIL' for e in checks))
