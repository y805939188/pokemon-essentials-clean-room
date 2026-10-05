"""Independent Git/document identity audit. No reference, prior verifier or vector execution."""
import collections
import csv
import functools
import hashlib
import io
import itertools
import json
import pathlib
import re
import subprocess

OUT = pathlib.Path(__file__).resolve().parent
REPO = OUT.parents[5]
ACTUAL = 'adca83d63d18c94429cdb52aef9eaf7b8aa00189'
UP = '259a1c158f317c5e32830e04838a76aa82f4d20a'
BASE = '219cc3c182750155e9dbf2cb619f420b3922de27'
CAND = 'a22df6b1d9465b68e45558c57bc69c61939baeaf'
R07 = '19e2d5f9de40a9220059a62f785ac0bbc13b2154'
R04 = '3e88d42b8d9313e1adbbc8944e54faa1b45e71a0'
ORIG = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
REF = pathlib.Path('/workspace/reference-pokemon-essentials-B07')
REFSHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
STAGE = 'review/remediation/20261003-prepare/batches/B07/integration-stage-1/'
BATCH = 'review/remediation/20261003-prepare/batches/B07/'
results = []
identities = []

def git(*args, root=REPO):
    return subprocess.check_output(['git', '-C', str(root), *args])

@functools.lru_cache(None)
def content(commit, path):
    return git('show', commit + ':' + path)

def obj(commit, path):
    return json.loads(content(commit,path))

def sha(data):
    return hashlib.sha256(data).hexdigest()

def canonical(value):
    return sha(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())

def check(name, ok, evidence):
    results.append({'check':name,'status':'PASS' if ok else 'FAIL','evidence':evidence})

def identity(commit,path):
    raw=content(commit,path)
    return {'commit':commit,'path':path,'git_blob':git('rev-parse',commit+':'+path).decode().strip(),'sha256':sha(raw),'bytes':len(raw)}

def verify(rec, default=ACTUAL):
    actual=identity(rec.get('commit',default),rec['path'])
    ok=all(actual[k]==rec[k] for k in ['git_blob','sha256','bytes'])
    identities.append({**actual,'declared_matches':ok})
    return ok

def statuses(base,target):
    return [{'change':s,'path':p} for s,p in (x.split('\t') for x in git('diff','--no-renames','--name-status',base,target).decode().splitlines())]

DIFF_OPTIONS=['--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3']
def full_diff(base,target):
    return git('diff',*DIFF_OPTIONS,base,target)

freeze=obj(ACTUAL,STAGE+'diff-and-freeze.json')
manifest=obj(ACTUAL,STAGE+'integration-manifest.json')
handshake=obj(ACTUAL,STAGE+'downstream-handshake.json')
reg=obj(ACTUAL,STAGE+'finding-registration.json')
payload=freeze['payload_commit']
check('actual exact single parent and evidence-only final child',
      git('rev-list','--parents','-n','1',ACTUAL).decode().split()==[ACTUAL,payload]
      and statuses(payload,ACTUAL)==[{'change':'A','path':p} for p in sorted(freeze['final_actual_changed_paths'])],
      {'actual':ACTUAL,'tree':git('rev-parse',ACTUAL+'^{tree}').decode().strip(),'payload':payload,'final_delta':statuses(payload,ACTUAL)})
check('payload exact tree and parent',git('rev-parse',payload+'^{tree}').decode().strip()==freeze['payload_tree']
      and git('rev-list','--parents','-n','1',payload).decode().split()==[payload,freeze['payload_parent']],
      {'payload':payload,'tree':freeze['payload_tree']})
merge1='2ec1f30940495c785f45de0a0b72c87ecb9116ad'
merge2='a0d2cec8af3a46e0e5a377966f4ee492ac9cd90e'
check('two normal merges have exact two-parent graph',
      git('rev-list','--parents','-n','1',merge1).decode().split()==[merge1,UP,R07]
      and git('rev-list','--parents','-n','1',merge2).decode().split()==[merge2,merge1,R04],
      {'first':[merge1,UP,R07],'second':[merge2,merge1,R04]})
diff_records=[]
for key in ['final_actual_complete_upstream_diff_contract','final_actual_complete_candidate_diff_contract','final_actual_complete_content_baseline_diff_contract']:
    control=freeze[key];base=control['base'];actual_status=statuses(base,ACTUAL)
    expected=control['payload_path_statuses']+[{'change':'A','path':p} for p in control['final_added_paths']]
    diff=full_diff(base,ACTUAL)
    before=full_diff(base,payload)
    check('complete unfiltered diff: '+key, sorted(actual_status,key=lambda x:x['path'])==sorted(expected,key=lambda x:x['path'])
          and len(actual_status)==control['expected_complete_path_count']
          and sha(before)==control['complete_payload_diff_sha256'] and len(before)==control['complete_payload_diff_bytes'],
          {'base':base,'actual':ACTUAL,'paths':len(actual_status),'actual_diff_sha256':sha(diff),'actual_diff_bytes':len(diff)})
    diff_records.append({'base':base,'actual':ACTUAL,'selected_paths':'ALL','git_diff_options':DIFF_OPTIONS,
                        'sha256':sha(diff),'bytes':len(diff),'path_statuses':actual_status})
for p in freeze['full_patches']:
    stored=content(ACTUAL,p['path']);reconstructed=full_diff(p['base_commit'],p['target_commit'])
    check('saved payload patch exact: '+pathlib.PurePosixPath(p['path']).name,
          stored==reconstructed and sha(stored)==p['sha256'] and len(stored)==p['bytes']
          and statuses(p['base_commit'],p['target_commit'])==p['complete_path_statuses'],
          {'path':p['path'],'bytes':len(stored),'sha256':sha(stored),'end':'payload only; not substituted for final actual diff'})
source_records=manifest['source_identities']
check('all57 incoming source bytes exact at actual', len(source_records)==57 and all([verify(x) and content(x['commit'],x['path'])==content(ACTUAL,x['path']) for x in source_records]),
      {'total':len(source_records),'formal':14,'author_evidence':11,'R_B07_report':12,'R_B04_report':20})
formals=[x['candidate']['path'] for x in manifest['formal_candidate_identities']]
check('all14 formal/original/catalog before-after identities and no candidate-actual delta',len(formals)==14
      and all([all([verify(v) for v in x.values() if isinstance(v,dict) and 'git_blob' in v]) for x in manifest['formal_candidate_identities']])
      and not git('diff','--name-only',CAND,ACTUAL,'--',*formals).decode().strip(),formals)
check('all14 payload and20 public-management freeze identities retained',
      all([verify(x) and content(x['commit'],x['path'])==content(ACTUAL,x['path']) for x in freeze['payload_formal_identities']+freeze['payload_public_and_management_identities']]),
      {'formal':len(freeze['payload_formal_identities']),'public_and_management':len(freeze['payload_public_and_management_identities'])})

catalog_records=[];added_all=[];changed_all=[]
for path in [p for p in formals if '/test-catalog/' in p]:
    old=content(BASE,path).decode();new=content(ACTUAL,path).decode()
    row_pattern=r'^\| ((?:BG|IU|SH|GR|DC)-\d+|(?:BE|CX|RM|CP)\d+) \|.*$'
    before=[(m[1],m[0]) for m in re.finditer(row_pattern,old,re.M)]
    after=[(m[1],m[0]) for m in re.finditer(row_pattern,new,re.M)]
    old_ids=[x[0] for x in before];filtered=[x for x in after if x[0] in old_ids]
    added=[i for i,_ in after if i not in old_ids]
    changed=[i for (i,a),(_,b) in zip(before,filtered) if a!=b]
    protected=[]
    for section in ['BG','DC'] if 'creature-rpg' in path else ['RM','CP']:
        def section_bytes(text):return re.search(r'^## '+section+r'\b.*?(?=^## |\Z)',text,re.M|re.S)[0].encode()
        a,b=section_bytes(old),section_bytes(new)
        protected.append({'section':section,'equal':a==b,'sha256':sha(a),'bytes':len(a)})
    catalog_records.append({'path':path,'old_count':len(before),'actual_count':len(after),'ordered_old_occurrences_preserved':[x[0] for x in filtered]==old_ids,'added':added,'old_rows_changed':changed,'protected_complete_sections':protected})
    added_all+=added;changed_all+=changed
new_expected=[*(f'IU-{i}' for i in range(49,60)),'SH-27','SH-28',*(f'GR-{i}' for i in range(45,54)),'BE36','BE37',*(f'CX{i}' for i in range(39,43))]
old_expected=['SH-08','GR-15',*(f'GR-{i}' for i in range(30,35)),'CX22']
check('actual catalogs independently show28 new8 changed; all old occurrence order and four full sections preserved',
      collections.Counter(added_all)==collections.Counter(new_expected) and collections.Counter(changed_all)==collections.Counter(old_expected)
      and all(r['ordered_old_occurrences_preserved'] and all(s['equal'] for s in r['protected_complete_sections']) for r in catalog_records),catalog_records)

originals={x['id']:x for x in obj(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
acceptances=obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
plans={x['id']:x for x in obj(PLAN,'review/remediation-20261003-prepare/batches.json')}
old_contract=obj(BASE,'review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/downstream-handshake.json')
old_controls={x['id']:x for x in old_contract['contribution_controls']}
prior_review={x['id']:x for x in obj(R07,BATCH+'review-round-1/finding-dispositions.json')['records']}
control_results=[]
for r in reg['dispositions']:
    o=originals[r['id']];a=acceptances[r['id']];c=old_controls[r['id']]
    extension_projection=[{k:e.get(k) for k in ['report','raw_id','adjudication','root_review']} for e in o.get('extensions',[])]
    tests={'complete_original_hash':canonical(o)==r['original_complete_object_sha256'],
      'complete_acceptance_hash':canonical(a)==r['acceptance_object_sha256'],
      'root_and_qualification':all(r[k]==o.get(k) for k in ['current_qualifications','adjudication_precedence','effective_case_constraints','root_adjudications','minimum_revision','determinate_recheck']),
      'every_extension':r['all_extensions_controls']==extension_projection,
      'full_acceptance_gate':r['acceptance_gate']==a['acceptance_gate'],
      'roles_and_pending':r['B07_primary']==c['B07_primary'] and r['primary_owner']==c['primary_owner']
          and r['all_contributor_batches']==c['all_contributors'] and r['accepted_other_contributors_at_fixed_versions']==c['accepted_other_contributors']
          and r['other_batch_obligations']==c['other_contributors_pending'],
      'prior_R07_disposition_exact':r['complete_R_B07_candidate_disposition_preserved']==prior_review[r['id']],
      'correct_candidate_and_reports':r['candidate']==CAND and r['candidate_report']==R07 and r['affected_B04_candidate_report']==R04,
      'no_early_acceptance_or_closure':r['canonical_state']=='OPEN' and not r['canonical_edited'] and not r['canonical_closure']
          and r['actual_R_B07_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and r['actual_R_B04_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and r['parent_C_acceptance']=='NOT_PERFORMED'}
    control_results.append({'id':r['id'],'checks':tests,'root_count':len(o['root_adjudications']),'extension_count':len(o.get('extensions',[]))})
check('19 full controls and12 primary retained without enlarging candidate verdict',len(control_results)==19
      and {x['id'] for x in reg['dispositions']}==set(plans['B07']['contribution_finding_ids'])
      and sum(x['B07_primary'] for x in reg['dispositions'])==12 and all(all(x['checks'].values()) for x in control_results),control_results)
sync_plan=obj(CAND,BATCH+'original-sync-plan.json')
locator_results=[]
for r in reg['dispositions']:
    prior=prior_review[r['id']]
    originals_for_id=sorted(x['path'] for x in sync_plan['files'] if r['id'] in x['finding_ids'])
    exact=all([verify(x) and content(x['commit'],x['path'])==content(ACTUAL,x['path']) for x in r['related_formal_file_identities']])
    exact=exact and r['formal_clause_locator']==prior['candidate_body_locator'] and r['static_locator']==prior['candidate_static_ids']
    exact=exact and sorted(r['authorized_original_paths'])==originals_for_id
    locator_results.append({'id':r['id'],'exact_locator_file_identity_and_authorized_original_scope':exact})
check('all19 public clause/static pointers, related file identities and six-original allocations match independent candidate evidence',all(x['exact_locator_file_identity_and_authorized_original_scope'] for x in locator_results),locator_results)
static_checks=[]
for r in reg['dispositions']:
    for v in r['static_row_bindings_not_executed']:
        lines=content(ACTUAL,v['path']).decode().splitlines(keepends=True)
        raw=lines[v['line']-1].encode()
        ok=sha(raw)==v['sha256'] and len(raw)==v['bytes'] and v['status']=='STATIC_DESIGN_NOT_EXECUTED'
        static_checks.append({'finding':r['id'],'static_id':v['id'],'path':v['path'],'line':v['line'],'exact':ok})
check('each registered static row has exact actual content and nonexecution label',all(x['exact'] for x in static_checks),static_checks)
check('every one of28 new actual static designs is bound in original-ID registration',
      set(new_expected).issubset({x['static_id'] for x in static_checks}),
      {'new_designs':28,'missing':sorted(set(new_expected)-{x['static_id'] for x in static_checks})})

public=[x['path'] if isinstance(x,dict) else x for x in manifest['current_public_paths']]
new_payload=[x['path'] if isinstance(x,dict) else x for x in manifest['new_payload_paths']]
check('payload changes exactly10 public and10 new management files',
      {x['path'] for x in statuses(merge2,payload) if x['change']=='M'}==set(public)
      and {x['path'] for x in statuses(merge2,payload) if x['change']=='A'}==set(new_payload)
      and len(statuses(merge2,payload))==20, {'public':public,'new_payload':new_payload})
ledger_results=[]
for path in ['review/remediation/20261003-prepare/approval-ledger.tsv','review/remediation/20261003-prepare/traceability-successor.tsv']:
    before=content(UP,path);after=content(ACTUAL,path)
    old=list(csv.DictReader(io.StringIO(before.decode()),delimiter='\t'));now=list(csv.DictReader(io.StringIO(after.decode()),delimiter='\t'))
    extra=now[len(old):]
    ok=len(old)==114 and len(now)==133 and after.startswith(before) and [r['finding_id'] for r in extra]==[r['id'] for r in reg['dispositions']]
    ok=ok and all(r['canonical_state']=='OPEN' and r['candidate_commit']==CAND and r['candidate_review_commit']==R07 for r in extra)
    if 'approval-ledger' in path:
        ok=ok and all(r['integration_verdict']=='NOT_REVIEWED_PENDING_TWO_ULTRA' and r['downstream_gate']=='BLOCKED' for r in extra)
    else:ok=ok and all(r['integration_gate']=='PENDING_SEPARATE_R_B07_AND_R_B04_ULTRA_OF_EXACT_ACTUAL_THEN_PARENT_C' for r in extra)
    for r in extra:
        obligations=json.loads(r['remaining_obligations']);c=old_controls[r['finding_id']]
        ok=ok and obligations['other_batch_obligations']==c['other_contributors_pending'] and obligations['parent_C']=='NOT_PERFORMED'
    ledger_results.append({'path':path,'pass':ok,'old114_literal_bytes_preserved':after.startswith(before),'before_sha256':sha(before),'before_bytes':len(before),'current_rows':len(now)})
check('114 old acceptance/trace rows exact; only19 blocked candidate rows appended',all(x['pass'] for x in ledger_results),ledger_results)
prose_guards=[]
for path in public:
    if not path.endswith('.md'):continue
    raw=content(ACTUAL,path).decode();patch=git('diff','--no-ext-diff','--no-textconv','--unified=0',UP,ACTUAL,'--',path).decode()
    removed=[line for line in patch.splitlines() if line.startswith('-') and not line.startswith('---')]
    ok=len(removed)==(2 if path.endswith('test-catalog/README.md') else 0)
    prose_guards.append({'path':path,'old_removed_lines':len(removed),'only_expected_removals':ok})
check('public historical prose preserved; only2 necessary catalog index lines replaced',all(x['only_expected_removals'] for x in prose_guards),prose_guards)
config_paths=['review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/'+x for x in ['README.md','acceptance-manifest.json','downstream-handshake.json','runtime-policy-successor.json']]
check('259a xhigh policy and correction provenance exact, no Max rollback',all(content(UP,p)==content(ACTUAL,p) for p in config_paths)
      and obj(ACTUAL,config_paths[-1])['current_author_request']['reasoning']=='xhigh',config_paths)
check('all previous tracked acceptance/history outside explicit public changes exact to management predecessor',
      all(x['path'] in set(public+formals) or x['change']=='A' for x in statuses(UP,ACTUAL)),
      'No pre-existing path outside10 public and14 B07 output paths changed from259a.')
stats_rec=obj(ACTUAL,STAGE+'scope-counts.json')['prior_accepted_statistics_identity']
stats=obj(UP,stats_rec['path'])
check('accepted completion statistics114/105/75 and74-1-0/71-4 remain exact',verify(stats_rec)
      and content(UP,stats_rec['path'])==content(ACTUAL,stats_rec['path'])
      and stats['contribution_records']==len(stats['accepted_contribution_receipts'])==114
      and stats['distinct_touched_IDs']==len(stats['touched_ID_rows'])==105
      and stats['primary_denominator']==len(stats['rows'])==75,
      {'identity':stats_rec,'specific_revision_counts':stats['specific_revision_counts'],'strict_all_planned_contribution_counts':stats['strict_all_planned_contribution_counts'],'specific_missing_ids':stats['specific_revision_missing_ids'],'strict_pending_ids':stats['strict_pending_ids']})
b04_formals=obj(ACTUAL,'review/remediation/20261003-prepare/batches/B04/integration-stage-1/integration-manifest.json')['formal_candidate_identities']
check('all13 accepted B04 final/original outputs unchanged at actual, not globally reapproved',len(b04_formals)==13
      and all(content('9e2dadfa650e2111b77f9eae1f834cc00b8805d5',x['candidate']['path'])==content(ACTUAL,x['candidate']['path']) for x in b04_formals),
      [x['candidate']['path'] for x in b04_formals])
input_records=obj(CAND,BATCH+'input-identities.json')['checks']
input_changes=[];external_fixed_inputs=[]
actual_tree_paths=set(git('ls-tree','-r','--name-only',ACTUAL).decode().splitlines())
for x in input_records:
    if x['path'] not in actual_tree_paths:
        external_fixed_inputs.append({'commit':x['commit'],'path':x['path'],'meaning':'Immutable control/evidence is read from its supplied fixed Git object; it is not required to be copied into the actual tree.'})
        continue
    old_data=content(x['commit'],x['path']);actual_data=content(ACTUAL,x['path'])
    if old_data!=actual_data:
        input_changes.append({'path':x['path'],'group':x['group'],'fixed_candidate_input':identity(x['commit'],x['path']),'actual':identity(ACTUAL,x['path']),
          'change_scope':'B07 output' if x['path'] in formals else 'public status successor' if x['path'] in public else '259a configuration-only successor' if x['path'] in config_paths else 'UNCLASSIFIED'})
check('all116 original candidate input identities retained at pinned revisions; every actual change classified',len(input_records)==116 and all([verify(x) for x in input_records])
      and all(x['change_scope']!='UNCLASSIFIED' for x in input_changes),
      {'pinned_inputs':116,'changed_actual_inputs':input_changes,'external_fixed_inputs_not_copied_to_actual':external_fixed_inputs,'meaning':'Pinned candidate input identities are historical, not asserted to be current actual inputs. Actual changes have separate exact identities.'})

b08=handshake['B08'];p08=plans['B08'];p07=plans['B07']
check('B08 exact planned79 reads8 writes17 contributions9 primary and dependencies',
      [x['path'] for x in b08['planned_reads']]==p08['read_paths'] and len(b08['planned_reads'])==79
      and b08['allowed_writes']==p08['write_paths'] and len(b08['allowed_writes'])==8
      and [x['id'] for x in b08['full17_control_bindings']]==p08['contribution_finding_ids']
      and b08['primary_IDs']==p08['primary_finding_ids'] and len(b08['primary_IDs'])==9
      and b08['planned_dependencies']==p08['dependencies'], {'reads':79,'writes':8,'contributions':17,'primary':9,'dependencies':p08['dependencies']})
check('all79 B08 actual input identities exact',all([verify(x) for x in b08['planned_reads']]),{'count':len(b08['planned_reads'])})
b08_controls=[]
for c in b08['full17_control_bindings']:
    o=originals[c['id']];a=acceptances[c['id']]
    ok=canonical(o)==c['original_complete_object_sha256'] and canonical(a)==c['acceptance_object_sha256']
    ok=ok and all(c[k]==o.get(k) for k in ['current_qualifications','effective_case_constraints','root_adjudications']) and c['all_extensions']==o.get('extensions',[])
    ok=ok and c['B08_primary']==(c['id'] in p08['primary_finding_ids']) and c['no_closure']
    ok=ok and c['full_original_fixed_commit']==ORIG and c['full_acceptance_fixed_commit']==PLAN
    ok=ok and c['all_contributor_batches']==[p['id'] for p in plans.values() if c['id'] in p['contribution_finding_ids']]
    b08_controls.append({'id':c['id'],'identities_and_all_controls_match':ok,'extensions':len(o.get('extensions',[]))})
check('B08 all17 full original/acceptance controls and all extensions preserved',all(x['identities_and_all_controls_match'] for x in b08_controls),b08_controls)
formal_set=set(formals)
changed=set(p08['read_paths'])&formal_set
reverse=set(p08['write_paths'])&set(p07['read_paths'])
check('independent set intersection proves3 changed B08 inputs and5 reverse B07 readers',
      changed=={x['current']['path'] for x in b08['changed_planned_B07_readers3']} and len(changed)==3
      and reverse=={x['path'] for x in handshake['B08_to_B07_reverse_readers5']} and len(reverse)==5,
      {'changed_B08_inputs':sorted(changed),'reverse_B07_readers':sorted(reverse)})
check('all3 changed-input baseline/candidate/current bindings exact',all([verify(v) for r in b08['changed_planned_B07_readers3'] for v in r.values()]),3)
check('all5 reverse-reader current identities and all4 whole-catalog locks exact',
      all([verify(x['current']) for x in handshake['B08_to_B07_reverse_readers5']+b08['whole_catalog_locks']])
      and {x['path'] for x in b08['whole_catalog_locks']}=={p for p in p08['write_paths'] if '/test-catalog/' in p},
      {'reverse_readers':5,'catalog_locks':4})
check('WP34 body read-only; B08 originals unapproved and work still blocked',
      not any('/wp34-' in p and '/test-catalog/' not in p for p in b08['allowed_writes'])
      and b08['WP34_body'].startswith('READ_ONLY') and not b08['original_specs_write_authorized'] and not b08['accepted'] and not b08['task_dispatched']
      and handshake['status']=='BLOCKED_BOTH_B07_ACTUAL_ULTRA_AND_PARENT_C' and handshake['downstream_tasks_dispatched']==0,
      {'WP34':b08['WP34_body'],'status':handshake['status'],'original_authorization':False})
check('fixed7 plans and B06 WP24 current/accepted identities exact',all([verify(x) for x in handshake['fixed_plan_inputs']])
      and verify(handshake['B06_WP24']['current']) and verify(handshake['B06_WP24']['accepted_baseline']),
      {'fixed_plans':7,'WP24_scope':handshake['B06_WP24']['scope']})
hash_rows=list(csv.DictReader(io.StringIO(content(ACTUAL,STAGE+'current-hashes.tsv').decode()),delimiter='\t'))
hash_tests=[]
for row in hash_rows:
    rec={**row,'bytes':int(row['bytes'])}
    if not rec['commit']:rec.pop('commit')
    hash_tests.append(verify(rec))
check('every current-hashes TSV identity rechecked from its exact declared/current object',all(hash_tests),
      {'rows':len(hash_rows),'kinds':dict(collections.Counter(x['kind'] for x in hash_rows))})

def table(path):return list(csv.DictReader(io.StringIO(content(PLAN,'review/remediation-20261003-prepare/'+path).decode()),delimiter='\t'))
semantic=table('semantic-dependencies.tsv');physical=table('physical-conflicts.tsv')
edges=collections.defaultdict(set)
for row in semantic:edges[row['upstream']].add(row['downstream'])
def reachable(start,target):
    seen=set();todo=[start]
    while todo:
        cur=todo.pop()
        for next_ in edges[cur]:
            if next_==target:return True
            if next_ not in seen:seen.add(next_);todo.append(next_)
    return False
parallel=handshake['bounded_parallel_inquiry'];pair_tests=[]
for row in parallel['pairs']:
    left,right=row['batch_a'],row['batch_b'];a,b=plans[left],plans[right]
    expected={'write_write_paths':sorted(set(a['write_paths'])&set(b['write_paths'])),
      'a_writes_b_reads':sorted(set(a['write_paths'])&set(b['read_paths'])),
      'b_writes_a_reads':sorted(set(b['write_paths'])&set(a['read_paths'])),
      'shared_control_IDs':sorted(set(a['contribution_finding_ids'])&set(b['contribution_finding_ids'])),
      'declared_semantic_path':reachable(left,right) or reachable(right,left),
      'physical_table_rows':[r for r in physical if {r['batch_a'],r['batch_b']}=={left,right}]}
    match=all(row[k]==v for k,v in expected.items())
    absent=not any(expected[k] for k in ['write_write_paths','a_writes_b_reads','b_writes_a_reads','shared_control_IDs','declared_semantic_path','physical_table_rows'])
    match=match and row['fixed_metadata_obstacle_absent']==absent and row['write_independence'].startswith('NOT_ESTABLISHED')
    pair_tests.append({'left':left,'right':right,'fixed_metadata_matches':match,'metadata_obstacle_absent':absent})
check('all91 fixed-metadata pair rows independently recomputed without author independence claims',len(pair_tests)==91
      and {(x['left'],x['right']) for x in pair_tests}==set(itertools.combinations(parallel['pending_batches'],2))
      and all(x['fixed_metadata_matches'] for x in pair_tests)
      and parallel['fixed_metadata_obstacle_absent_pairs']==[[x['left'],x['right']] for x in pair_tests if x['metadata_obstacle_absent']]
      and parallel['tasks_created']==0 and parallel['writers_authorized_in_parallel']==0,
      {'pairs':91,'failed':[x for x in pair_tests if not x['fixed_metadata_matches']],'conditional_only_pairs':parallel['fixed_metadata_obstacle_absent_pairs']})
check('reference independently held exact tree/origin and remains clean',
      git('rev-parse','HEAD',root=REF).decode().strip()==REFSHA
      and git('rev-parse','HEAD^{tree}',root=REF).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0'
      and git('remote','get-url','origin',root=REF).decode().strip().removesuffix('.git')=='https://github.com/Maruno17/pokemon-essentials'
      and not git('status','--porcelain',root=REF).decode().strip(),{'commit':REFSHA,'execution':0})
whitespace=subprocess.run(['git','-C',str(REPO),'diff','--check',UP,ACTUAL],capture_output=True)
patch_paths={p['path'] for p in freeze['full_patches']} | {BATCH+'affected-B04-review-round-1/'+p for p in ['complete.diff','formal.diff','reverse.diff']}
warning_counts=collections.Counter()
for line in whitespace.stdout.decode().splitlines():
    found=re.match(r'(.+):[0-9]+: (.+)',line)
    if found:warning_counts[(found[1],found[2])]+=1
non_patch=[x['path'] for x in statuses(UP,ACTUAL) if x['path'] not in patch_paths]
non_patch_check=subprocess.run(['git','-C',str(REPO),'diff','--check',UP,ACTUAL,'--',*non_patch],capture_output=True)
check('ordinary documents clean; unfiltered whitespace warnings only immutable literal Git patches',
      non_patch_check.returncode==0 and all(p in patch_paths and (warning=='trailing whitespace.'
        or (p==BATCH+'affected-B04-review-round-1/reverse.diff' and warning=='new blank line at EOF.'
            and content(ACTUAL,p).endswith(b'\n \n'))) for p,warning in warning_counts),
      {'unfiltered_returncode':whitespace.returncode,'literal_patch_warning_counts':[{'path':p,'warning':w,'count':n} for (p,w),n in sorted(warning_counts.items())],
       'non_patch_returncode':non_patch_check.returncode,'explanation':'Unified Git patch blank-context records contain the required single-space prefix. The immutable R-B04 reverse diff ends with a blank context record. Candidate report diffs and reconstructed frozen full patches are byte-exact; these archival-format warnings do not change a behavior or document rule. Do not normalize immutable history.'})

(OUT/'document-checks.json').write_text(json.dumps({'kind':'INDEPENDENT_GIT_DOCUMENT_AUDIT_ONLY','actual':ACTUAL,'management_predecessor':UP,'formal_baseline':BASE,'candidate':CAND,'results':results,'all_pass':all(x['status']=='PASS' for x in results),'reference_execution':0,'behavior_vectors_executed':0,'prior_author_reviewer_verifiers_executed':0},ensure_ascii=False,indent=2)+'\n')
(OUT/'input-and-diff-identities.json').write_text(json.dumps({'records':identities,'complete_unfiltered_diffs':diff_records,'B07_full_control_checks':control_results,'B08_control_checks':b08_controls,'scope':'Identity comparison is not source-wide semantic inspection or behavior execution.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(results),'all_pass':all(x['status']=='PASS' for x in results),'failed':[x['check'] for x in results if x['status']!='PASS']},ensure_ascii=False))
