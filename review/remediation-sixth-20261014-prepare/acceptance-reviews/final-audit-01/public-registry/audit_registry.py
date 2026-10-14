import collections, datetime, hashlib, json, pathlib, subprocess, sys

BASE = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = BASE / 'review/remediation-sixth-20261014-prepare/acceptance-reviews/final-audit-01/public-registry'
PACKET = '229260cfd5177581bb88bafd84770ceb1c11b117'
REG = 'd35356005f79b9fdffc5a4202a0b39e9255a36fa'
ACTUAL = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PREFIX = 'review/remediation-sixth-20261014-prepare/'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
cache, reads = {}, []

def identity(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}

def raw(commit, path):
    key = (commit, path)
    if key not in cache:
        cache[key] = subprocess.check_output(['git', 'show', commit + ':' + path])
        reads.append({'commit': commit, 'path': path, **identity(cache[key]),
                      'kind': 'BYTE_IDENTITY_AND_SELECTED_JSON_FIELDS_NOT_FULL_SEMANTIC_READ'})
    return cache[key]

def document(commit, path):
    return json.loads(raw(commit, path))

def pointer(obj, path):
    for token in path.split('/')[1:]:
        token = token.replace('~1', '/').replace('~0', '~')
        obj = obj[int(token)] if isinstance(obj, list) else obj[token]
    return obj

def public_rows(path):
    data = raw(REG, path)
    lines = data.decode().splitlines()
    lo = lines.index('<!-- R6-CURRENT-SYNC-BEGIN -->')
    hi = lines.index('<!-- R6-CURRENT-SYNC-END -->')
    rows = []
    for i in range(lo, hi + 1):
        line = lines[i]
        if line.startswith('| ') and not line.startswith(('| ID ', '| --- ')):
            cells = [x.strip() for x in line.split('|')[1:-1]]
            rows.append({'line': i + 1, 'id': cells[0], 'cells': cells, 'full_line': line})
    return data, rows, [lo + 1, hi + 1]

def locator_display(z):
    if 'display_lines' in z:
        return z['display_lines']
    if 'start_line' in z and 'end_line' in z:
        return str(z['start_line']) + '–' + str(z['end_line'])
    return '资料单元'

packet = document(PACKET, PREFIX + 'integration/final-acceptance-audit-20261014/input.json')
sync = document(REG, PREFIX + 'integration/public-sync-20261014/sync-input.json')
ledger = document(REG, PREFIX + 'ledger.json')
queue = document(REG, PREFIX + 'reception-queue.json')
tasks = document(REG, PREFIX + 'task-register.json')
actual = document(ACTUAL, packet['actual_input']['path'])
matrix_raw, matrix_rows, matrix_range = public_rows('planning/feature-matrix.md')
trace_raw, trace_rows, trace_range = public_rows('audit/source-traceability.md')
mapping = packet['required_mapping']
report_map = {r['group']: r for r in packet['five_independent_actual_reports']}
group_verdicts = {}
global_checks = {}
for group, r in report_map.items():
    global_checks[group + '_exact_root_report_identity'] = identity(raw(r['report_commit'], r['report_path'])) == r['report_identity']
    group_verdicts[group] = document(r['report_commit'], r['structured_verdict_path'])
    global_checks[group + '_exact_structured_verdict_identity'] = identity(raw(r['report_commit'], r['structured_verdict_path'])) == r['structured_verdict_identity']
for r in packet['frozen_read_set']:
    global_checks[r['path'] + '_registration_identity'] = identity(raw(REG, r['path'])) == {k:r[k] for k in ['bytes','sha256','git_blob']}
for r in packet['public_sync_files']:
    previous = raw(ACTUAL, r['path'])
    current = raw(REG, r['path'])
    global_checks[r['path'] + '_exact_old_history_identity'] = identity(previous) == r['before_actual_history_identity']
    global_checks[r['path'] + '_complete_old_history_prefix_preserved'] = current.startswith(previous)
global_checks['registration_workspace_tree'] = subprocess.check_output(['git','rev-parse',REG+'^{tree}'],text=True).strip() == packet['frozen_registration_workspace_tree']
global_checks['formal_tree_unchanged_at_registration'] = subprocess.check_output(['git','rev-parse',REG+':deliverables/final-specification-set'],text=True).strip() == packet['frozen_formal_tree']
ids = [x['id'] for x in mapping]
for name, sequence in [('mapping', mapping), ('sync',sync['items']), ('ledger',ledger['required']),('matrix',matrix_rows),('trace',trace_rows)]:
    names = [z['id'] for z in sequence]
    global_checks[name + '_56_unique_same_ID_set'] = len(names) == len(set(names)) == 56 and set(names) == set(ids)
global_checks['severity_39_P2_17_P3'] = dict(collections.Counter(x['severity'] for x in mapping)) == {'P2':39,'P3':17}
global_checks['groups_11_9_19_9_8'] = dict(collections.Counter(x['actual_primary_group'] for x in mapping)) == {'A':11,'B':9,'C':19,'D':9,'E':8}
global_checks['ledger_counts_56_56_0_0_56'] = all(ledger['totals'][k] == v for k,v in {'candidate_pass':56,'integrated_pass':56,'accepted':0,'closed':0,'open':56}.items())
global_checks['all_fourteen_batches_received'] = queue['actually_integrated_batches'] == 14 and queue['actually_integrated_items'] == 56
global_checks['all_five_actual_tasks_equal_across_three_registers'] = ledger['actual_review_tasks'] == queue['actual_review_tasks'] == tasks['actual_review_tasks']
global_checks['all_five_tasks_sixteen_zero_counts_not_claimed_runtime'] = tasks['completed_actual_content_review_groups'] == 5 and tasks['independent_actual_content_PASS_items'] == 56
projection = {'common': {'phase':ledger['phase'], 'totals':ledger['totals'],
    'queue_current_counts': {k:queue[k] for k in ['actually_integrated_batches','actually_integrated_items','independent_actual_content_PASS_items']},
    'task_current_counts': {k:tasks[k] for k in ['completed_actual_content_review_groups','independent_actual_content_PASS_items']},
    'sync_qualification':sync['qualification'], 'source_locator_projection_scope':sync['source_locator_projection_scope'],
    'joint_interfaces':packet['dependency_status']['qualified_joint_interfaces']}, 'batches':[], 'actual_groups':[], 'per_id':[]}
for i,q in enumerate(queue['batches']):
    author = next(t for t in tasks['tasks'] if t['batch']==q['batch'] and t['role']=='author')
    reviewer = next(t for t in tasks['tasks'] if t['batch']==q['batch'] and t['role']=='independent_reviewer')
    projection['batches'].append({'batch':q['batch'],'queue_pointer':'/batches/'+str(i),
        'required_ids':q['required_ids'], 'candidate_published_commit':q['candidate_published_commit'],
        'candidate_receipt_state':q['candidate_receipt_state'], 'candidate_PASS_state':q['candidate_pass']['state'],
        'candidate_configuration':q['candidate_pass']['effective_configuration'],
        'current_integrated_PASS':{k:q['integrated_pass'].get(k) for k in ['state','group','actual_commit','review_commit','necessary_content_revisions','effective_configuration','configuration_qualified_acceptance','global_INTEGRATED_PASS','new_reference_model_host_save_execution','formal_acceptance','CLOSED']},
        'older_actual_transport_state':q['actual_integration']['state'], 'public_sync':q['public_sync'],
        'author_task_state':author['state'],'reviewer_task_state':reviewer['state'],
        'task_candidate_published_commits':[author['candidate_identity']['published_commit'],reviewer['candidate_identity']['published_commit']],
        'task_integrated_identities':[author.get('integrated_identity'),reviewer.get('integrated_identity')],
        'formal_acceptance':q['formal_acceptance'],'closed':q['closed']})
for i,g in enumerate(ledger['actual_review_tasks']):
    projection['actual_groups'].append({'pointer':'/actual_review_tasks/'+str(i), **{k:g[k] for k in ['group','required_ids','required_count','frozen_actual_commit','frozen_formal_tree','state','effective_configuration','independent_actual_PASS','actual_review_report']}})
results=[]
for m in mapping:
    id_=m['id']; group=m['actual_primary_group']; batch=m['primary_batch']
    sr=pointer(sync,m['public_registry_item_pointer']); lr=next(x for x in ledger['required'] if x['id']==id_)
    qr=next(x for x in queue['batches'] if x['batch']==batch)
    original_actual_batch=next(x for x in actual['batches'] if x['batch']==batch)
    ts=[x for x in tasks['tasks'] if x['batch']==batch]
    ar=next(x for x in ledger['actual_review_tasks'] if x['group']==group)
    mr=next(x for x in matrix_rows if x['id']==id_);tr=next(x for x in trace_rows if x['id']==id_)
    cr=document(REG,m['contract_path']);cp=pointer(cr,m['contract_pointer'])
    vr=pointer(group_verdicts[group],m['report_per_id_pointer'])
    report=report_map[group]
    checks={
      'sync_pointer_exact_ID':sr['id']==id_,
      'one_primary_batch_group':sr['primary_batch']==lr['primary_batch']==batch and sr['actual_group']==lr['integrated_pass']['group']==group,
      'severity_immutable':sr['severity']==lr['severity']==cp['identity_and_verdict']['severity']==m['severity'],
      'contract_identity':identity(raw(REG,m['contract_path']))==m['contract_identity']==sr['contract_identity'],
      'contract_pointer_ID':cp['id']==id_,
      'original_dependencies_exact':sr['original_dependencies']==cp['dependencies_and_receivers']['original_dependencies']==lr['integration_receivers']['original_dependencies'],
      'necessary_consumer_pointer_exact':pointer(cr,sr['necessary_consumers_pointer'])==cp['bidirectional_evidence']['necessary_consumers'],
      'root_verdict_pointer_exact_ID':vr['id']==id_,
      'root_verdict_is_pass_no_repairs':'PASS' in str(vr.get('actual_verdict',vr.get('verdict',vr.get('actual_content_verdict')))),
      'one_actual_primary_signature':sum(id_ in z['required_ids'] for z in packet['five_independent_actual_reports'])==1,
      'actual_commit_formal_tree':lr['integrated_pass']['actual_commit']==ACTUAL and lr['integrated_pass']['actual_formal_tree']==packet['frozen_formal_tree'],
      'report_binding':lr['integrated_pass']['review_commit']==report['report_commit'] and lr['integrated_pass']['report_path']==report['report_path'] and lr['integrated_pass']['report_identity']==report['report_identity'],
      'sync_review_exact_ledger_current':sr['actual_content_review']==lr['integrated_pass'],
      'queue_current_review_matches_primary':qr['integrated_pass']['group']==group and qr['integrated_pass']['review_commit']==report['report_commit'] and id_ in qr['required_ids'],
      'task_pair_and_actual_task_membership':len(ts)==2 and all(id_ in z['required_ids'] for z in ts) and id_ in ar['required_ids'],
      'current_candidate_receipt_matches_tasks':all(z['candidate_identity']['published_commit']==qr['candidate_published_commit'] for z in ts),
      'current_namespace_exact_actual_candidate_receipt':qr['candidate_published_commit']==original_actual_batch['candidate_published_commit'] and set(qr['required_ids'])==set(original_actual_batch['required_ids']),
      'candidate_received_not_baseline':id_ in qr['candidate_pass']['scope_ids'] and qr['candidate_pass']['candidate_published_commit']==qr['candidate_published_commit'],
      'public_matrix_exact_rule_control_label':mr['cells'][1]==batch+'／'+group and mr['cells'][2]==sr['rule_summary']+' 控制：'+sr['case_controls'] and mr['cells'][3]==sr['actual_clause_label'],
      'public_trace_exact_rule_control_label':tr['cells'][1]==sr['rule_summary']+' 落点：'+sr['actual_clause_label']+'／'+sr['case_controls'],
      'public_trace_selected_locators_faithful':tr['cells'][2]=='；'.join('`'+z['path']+'` '+locator_display(z) for z in sr['source_locators'][:2]),
      'sync_is_applied':sr['public_sync_state'].startswith('APPLIED') and lr['public_sync']['state'].startswith('APPLIED') and qr['public_sync']['state'].startswith('APPLIED'),
      'configuration_UNVERIFIED_not_global_cert':lr['integrated_pass']['effective_configuration']=='UNVERIFIED' and not lr['integrated_pass']['configuration_qualified_acceptance'] and not lr['integrated_pass']['global_INTEGRATED_PASS'],
      'execution_not_promoted':sr['behavior_execution']=='NOT_EXECUTED' and lr['integrated_pass']['new_reference_model_host_save_execution']==0,
      'acceptance_closed_open_distinct':sr['formal_acceptance'] is lr['formal_acceptance'] is qr['formal_acceptance'] is None and not sr['closed'] and not lr['closed'] and not qr['closed'],
      'no_content_revision_pending':lr['integrated_pass']['necessary_content_revisions']==0,
    }
    results.append({'id':id_,'severity':m['severity'],'primary_batch':batch,'primary_group':group,
        'matrix_line':mr['line'],'trace_line':tr['line'],'sync_pointer':m['public_registry_item_pointer'],
        'ledger_pointer':'/required/'+str(ledger['required'].index(lr)),
        'queue_pointer':'/batches/'+str(queue['batches'].index(qr)),
        'task_pointers':['/tasks/'+str(tasks['tasks'].index(z)) for z in ts],
        'actual_task_pointer':'/actual_review_tasks/'+str(ledger['actual_review_tasks'].index(ar)),
        'contract_pointer':m['contract_pointer'],'root_report_per_ID_pointer':m['report_per_id_pointer'],
        'checks':checks,'machine_registry_PASS':all(checks.values()),
        'semantic_registry_comparison':'SEPARATE_HUMAN_RULE_NORMAL_FAILURE_QUALIFICATION_REVIEW_NO_NEW_GLOBAL_SEMANTICS'})
    projection['per_id'].append({'id':id_,'severity':m['severity'],'primary_batch':batch,'group':group,
        'rule_summary':sr['rule_summary'],'case_controls':sr['case_controls'],'actual_clause_label':sr['actual_clause_label'],
        'original_dependencies':sr['original_dependencies'], 'necessary_consumers_pointer':sr['necessary_consumers_pointer'],
        'source_full_required_set':sr['source_full_required_set'],
        'source_qualification':sr['source_qualification'],'behavior_execution':sr['behavior_execution'],
        'ledger_state':lr['state'],'candidate_state':lr['candidate_state'],
        'integrated_PASS_state':lr['integrated_pass']['state'],'public_sync':lr['public_sync'],
        'dependency_status':lr['dependency_status'], 'formal_acceptance':lr['formal_acceptance'],'closed':lr['closed']})
result={'utc_start':started,'utc_end':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'cwd':str(pathlib.Path.cwd()),'argv':sys.argv,'exit':0,'kind':'OWN_DOCUMENT_REGISTRY_CHECK_NO_AUTHOR_OR_SOURCE_EXECUTION',
        'registration_commit':REG,'actual_semantic_commit':ACTUAL,
        'source_identities':reads,'public_ranges':{'planning/feature-matrix.md':matrix_range,'audit/source-traceability.md':trace_range},
        'global_checks':global_checks,'per_id':results,
        'all_machine_checks_pass':all(global_checks.values()) and all(z['machine_registry_PASS'] for z in results),
        'scope':'Registry mapping/retention/pointers only; source semantics and original 110-edge proof are separately reviewed by parent/history agents.',
        'effective_configuration':'UNVERIFIED','formal_acceptance_count':0,'CLOSED_count':0,'OPEN_count':56}
(OUT/'registry-machine-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
with (OUT/'registration-relevant-projection.jsonl').open('w') as f:
    for key in ['common','batches','actual_groups']:
        f.write(json.dumps({key:projection[key]},ensure_ascii=False)+'\n')
    for row in projection['per_id']:
        f.write(json.dumps(row,ensure_ascii=False)+'\n')
with (OUT/'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps({'utc_start':started,'utc_end':result['utc_end'],'cwd':result['cwd'],'argv':sys.argv,'exit':0,
        'kind':'STRUCTURAL_VALIDATION_AND_EXACT_SELECTED_REGISTRATION_PROJECTION','source_identities':reads,
        'projection':'registration-relevant-projection.jsonl','all_machine_checks_pass':result['all_machine_checks_pass'],
        'semantic_read_follows':True},ensure_ascii=False)+'\n')
print(json.dumps({'all_machine_checks_pass':result['all_machine_checks_pass'],
    'global_failed':[k for k,v in global_checks.items() if not v],
    'per_id_failed':{z['id']:[k for k,v in z['checks'].items() if not v] for z in results if not z['machine_registry_PASS']},
    'rows':len(results),'projection_lines':59},ensure_ascii=False))
