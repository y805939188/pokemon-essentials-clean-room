"""Freeze audit identities and observed task registries without changing any input."""
import datetime, hashlib, json, pathlib, subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]; REPO=ROOT.parents[2]
def get(p):return json.loads((ROOT/p).read_text())
def put(p,x):(ROOT/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
fixed=get('control/session.json')
fixed.update({'project_path':str(REPO),'project_origin':'y805939188/pokemon-essentials-clean-room',
 'reference_path':str(REPO/'reference/pokemon-essentials'),'reference_relative_path':'reference/pokemon-essentials',
 'reference_origin':'Maruno17/pokemon-essentials','delivery_tag':'refs/tags/delivery/fifth-round-closed-final-20261014',
 'delivery_tag_kind':'lightweight','delivery_tag_commit':fixed['main'],
 'admin_core_commit':'b67f542b47ad33ac23053a21f62748077c167a23','admin_core_tree':'e5fa5de69c1e3164597815a42776aa859c6ea4b7',
 'admin_core_payload_directory':'review/remediation-fifth-20261013-prepare/integration/final-main-publication-20261014',
 'activation_directory':'review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-activation',
 'history_commits':{'B5':'9366d9d17aaeac3b4414236468affa650fb3dd27',
   'R5_semantic_core':'c0ff33024aea424c68d29f9778fe7c8e807d21e8','R5_semantic_publication':'f49d870c6fd616ab6736754a218a4553b5acac7f',
   'U08_actual':'e9f7590e68347849450fd5cbdba538e605cda0a7','U08_actual_report':'debf59f3c5370df253706969fd4dd1c103300bf2',
   'accepted_closure_candidate':'13fddb0a217b36974c75657aa68da0caf104ee48','closure_report':'044c3483229e7e76bedf1fc244fc84d274bf059c',
   'sole_activation_core':'12df95a8e81061a606d50d3f0a0528793b2e6b2c','sole_activation_publication':'0378dc85cab61642ca1467e5a901b3c829df976a'},
 'protection':{'reference_readonly':True,'formal_131_readonly':True,'planning_audit_specs_readonly_during_review':True,
    'old_reports_and_receipts_readonly':True,'original_62_untracked_preserved':'inventory/protected-untracked.json',
    'main_and_tags_not_moved':True,'no_force_or_delete_or_worktree_archive':True,
    'actual_write_boundary_incident':'control/write-boundary-incident.json'},
 'r6_core':'NOT_YET_FROZEN','r6_publication':'NOT_YET_PUBLISHED','update_started':False})
put('control/fixed-inputs.json',fixed)
registry=get('control/task-register.json')
byid={x['logical_id']:x for x in registry}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for taskdir in sorted((ROOT/'tasks').iterdir()):
    lid=taskdir.name
    if lid not in byid:continue
    row=byid[lid]
    p=taskdir/'launcher-status.json'
    launcher=json.loads(p.read_text()) if p.exists() else None
    statusp=taskdir/'task-status.json'
    status=json.loads(statusp.read_text()) if statusp.exists() else None
    row['observed_semantic_status_payload']=str(statusp.relative_to(ROOT)) if status else None
    row['observed_semantic_status']=status
    if launcher:
        row['launcher']=launcher
        row['process_state']=launcher.get('state');row['exit_code']=launcher.get('exit_code')
        row['started_at']=launcher.get('started_at');row['ended_at']=launcher.get('ended_at')
        for line in (taskdir/'stdout.jsonl').read_text().splitlines():
            try:event=json.loads(line)
            except json.JSONDecodeError:continue
            if event.get('type')=='thread.started':row['platform_uuid']=event['thread_id'];break
        row['state']='COMPLETED_PROCESS_SEMANTIC_SCOPE_RECORDED' if launcher.get('state')=='COMPLETED' else launcher.get('state')
    row['last_observed_at']=now
    row['current_dependencies']='own full-source/formal read; actual foreign receipts and final counter review as recorded in semantic status'
    row['logs']=[str(p.relative_to(ROOT)) for p in [taskdir/'stdout.jsonl',taskdir/'stderr.log',taskdir/'reading-ledger.jsonl',taskdir/'report.md',statusp] if p.exists()]

children=[]
for p in sorted((ROOT/'tasks').rglob('task-status.json')):
    rel=p.relative_to(ROOT/'tasks')
    if len(rel.parts)<=2 or 'history' in rel.parts:continue
    subdir=p.parent
    x=json.loads(p.read_text())
    logical='R6-SUB:'+str(subdir.relative_to(ROOT/'tasks'))
    row={'logical_id':logical,'parent_entry':rel.parts[0],'role':'independent bounded domain reader/counter as raw task status and report specify',
         'platform_canonical_task':x.get('canonical_task_name',x.get('actual_task_name','UNVERIFIED')),
         'platform_uuid':x.get('actual_uuid',x.get('platform_uuid','UNVERIFIED')),
         'requested_model':'gpt-6.1-sol','requested_effort':'ultra','requested_speed':'default','requested_tier':'default','fast_requested':False,
         'actual_model':'UNVERIFIED','actual_effort':'UNVERIFIED','actual_tier':'UNVERIFIED','actual_speed':'UNVERIFIED',
         'state':'SCOPED_ARTIFACTS_RECORDED_PARENT_RECEIPT_REQUIRED','raw_status':x,
         'started_at':x.get('started_at','UNVERIFIED'),'ended_at':x.get('ended_at','UNVERIFIED'),
         'last_observed_at':now,'write_directory':str(subdir.relative_to(REPO)),
         'scope_and_read_set':'own inventory/prompt/reading ledger and parent delegate receipt; no blanket scope transfer',
         'frozen_inputs':{'main':fixed['main'],'reference_commit':fixed['reference_commit'],'formal_tree':fixed['formal_tree']},
         'dependencies':['parent domain acceptance of exact source/spec ranges','global root adjudication'],
         'result_logs':[str(q.relative_to(ROOT)) for q in subdir.iterdir() if q.is_file() and (q.name in ['report.md','findings.json','reading-ledger.jsonl','prompt.md','task-status.json'] or 'log' in q.name)],
         'query':'read the recorded status/ledger/log paths; missing platform live endpoint and exact start/end remain UNVERIFIED, not simulated'}
    children.append(row)
registry=[byid[x['logical_id']] for x in registry]+children
put('control/task-register-current.json',{'schema':'r6.task-register.v1','observed_at':now,'parents':registry[:len(byid)],'subtasks':children,
 'model_echo_boundary':'requested settings do not prove actual model/effort/tier/speed; CLI thread.started UUIDs alone are verified platform identifiers',
 'process_semantic_state_separate':True,'update_started':False})
print(json.dumps({'parents':len(byid),'subtasks':len(children),'observed_at':now}))
