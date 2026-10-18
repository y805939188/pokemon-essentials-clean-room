"""Produce an honest field-level checkpoint. Parsing never grants reading credit."""
from pathlib import Path
import datetime, hashlib, json, subprocess
from collections import Counter

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[4]
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
D = '30cfed0996003b6ebf4b5c51cc04f31ca9255440'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
READER = 'external-H-EARLY-QUALIFICATIONS/root'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def dump(name, obj):
    (TASK/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

def identity(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}

def git(*args):
    r = subprocess.run(['git', '-C', str(REPO), *args], capture_output=True)
    return {'exit': r.returncode, 'stdout': r.stdout.decode(errors='replace'), 'stderr': r.stderr.decode(errors='replace')}

def ptr_escape(s):
    return str(s).replace('~','~0').replace('/','~1')

def get(x, ptr):
    for k in ptr.lstrip('/').split('/') if ptr else []:
        k=k.replace('~1','/').replace('~0','~')
        x=x[int(k)] if isinstance(x,list) else x[k]
    return x

readset = json.loads((TASK/'inputs/readset.json').read_text())
recovery = json.loads((TASK/'early-history-recovery-manifest.json').read_text())
objects={}
states={}
inventory=[]
full=[
 'tasks/R7-H12/report.md', 'tasks/R7-H12/preserved-special-history.json',
 'tasks/R7-H05/execution-qualification.json','tasks/R7-H05/report.md']
ack_names=['001-u03-fail','002-u03-limited','003-u08-candidate-fail','004-u08-actual','005-u08-final',
 '006-sc-original','008-summary','009-r3-excluded-retry','010-parent-ledger','011-r2-rules',
 '012-r1-scope-rules','013-r1-errata','014-r1-approval-corrections','015-qualifier-projection','016-purpose-field-view','017-r3-r4-counts']
acks=[]
for n in ack_names:
    r=json.loads((TASK/'read-logs'/f'{n}.receipt.json').read_text())
    r['semantic_status']='ACTUALLY_READ_ACKNOWLEDGED_BY_NAMED_READER'
    r['acknowledgement_scope']='exact displayed payload/pointer only; no original-source or current-formal body inheritance'
    r['receipt_file']='read-logs/'+n+'.receipt.json'
    acks.append(r)
dump('read-acknowledgements.json',{'reader':READER,'recorded_utc':NOW,'acknowledgements':acks,
 'truncated_attempts_not_credited':['007-r3-excluded; superseded by009','earlier broad structure/sample displays'],
 'earliest_full_reads':'four readset bodies and contracts read via platform outputs; separate first-read local UTC/stdout/stderr not captured; not backfilled'})

def add(logical, pointer, status, evidence):
    states.setdefault(logical,[]).append({'pointer':pointer,'status':status,'evidence':evidence})

for row in readset['files']:
    lp=row['logical_path'];p=TASK/'recovered-early-history'/lp;b=p.read_bytes()
    ident=identity(b)
    assert ident['bytes']==row['bytes'] and ident['sha256']==row['sha256'] and ident['git_blob']==row['git_blob']
    objects[lp]=json.loads(b) if p.suffix=='.json' else b.decode()
    tr=row['transport_path']
    a=git('ls-tree',C2,'--',tr);b8=git('ls-tree',B8,'--',tr)
    assert a['exit']==0 and b8['exit']==0 and a['stdout']==b8['stdout'] and a['stdout']
    inventory.append({**row,'actual_restored_path':str(p),'decoded_identity_verified':ident,
      'original_C2_and_B8_transport_membership':a['stdout'].strip(),
      'Git_commit_available':git('cat-file','-t',row['commit'])['exit']==0,
      'payload_available':True,'restoration_only_semantic_credit':False})
    if lp in full:add(lp,'','FULL_READ','platform complete nontruncated body presentation; earliest separate local UTC unknown')

prefix='recovered-early-history/'
for a in acks:
    lp=a['source_task_path']
    if lp.startswith(prefix):add(lp[len(prefix):],a['pointer'],'FIELD_READ',a['receipt_file'])

for row in json.loads((TASK/'qualifier-projection.json').read_text()):
    if row['source'].startswith(prefix):
        lp=row['source'][len(prefix):]
        assert get(objects[lp],row['pointer'])==row['exact_value']
        add(lp,row['pointer'],'FIELD_READ','015-qualifier-projection; exact value/source pointer checked')

r2='tasks/R7-H12/subreaders/r2/qualification.json'
for k in objects[r2]:
    if k!='per_control':add(r2,'/'+ptr_escape(k),'FIELD_READ','016-purpose-field-view exact top field')
for i,row in enumerate(objects[r2]['per_control']):
    for k in row:
        add(r2,f'/per_control/{i}/'+k,'INVENTORY_ONLY' if k in ['id','scope_identity'] else 'FIELD_READ',
            '016 exact common field values + purpose-field-associations.json; IDs/source hashes are administrative routes')

auth='tasks/R7-H12/subreaders/r1/original-authorities.inventory.json'
for k in objects[auth]:
    if k!='records':add(auth,'/'+k,'FIELD_READ','016-purpose-field-view exact top field')
for i,row in enumerate(objects[auth]['records']):
    for k in row:
        add(auth,f'/records/{i}/'+k,'FIELD_READ' if k in ['named_purpose','state_time','qualification'] else 'INVENTORY_ONLY',
            '016 exact common purpose fields + identity/old-reader receipt route; underlying83 contracts UNREAD')

selection='tasks/R7-H12/r5-activation-selections.json'
add(selection,'','INVENTORY_ONLY','activation-selector-validation.json; all92 exact associations, identity table only')

aggregate='tasks/R7-H12/earlier-round-qualification-full.json'
for src,dest in [(r2,'/R2/qualification'),('tasks/R7-H12/subreaders/r1/qualification.json','/R1/qualification'),
                 ('tasks/R7-H12/subreaders/r3-r4/qualification.json','/R3_R4/qualification')]:
    assert get(objects[aggregate],dest)==objects[src]
    for row in list(states.get(src,[])):
        add(aggregate,dest+row['pointer'],'EXACT_ASSOCIATED_'+row['status'],{'source':src,'pointer':row['pointer'],'basis':row['evidence']})
assert objects[aggregate]['preserved_special_history']==objects['tasks/R7-H12/preserved-special-history.json']
add(aggregate,'/preserved_special_history','EXACT_ASSOCIATED_FULL_READ','exact JSON subtree equality to fully read preserved-special-history.json')
r1='tasks/R7-H12/subreaders/r1/qualification.json'
assert objects[r1]['read_original_authority_and_contract_records']==objects[auth]['records']
for row in list(states[auth]):
    if row['pointer'].startswith('/records/'):
        tail=row['pointer'][len('/records'):]
        add(r1,'/read_original_authority_and_contract_records'+tail,'EXACT_ASSOCIATED_'+row['status'],auth+row['pointer'])
        add(aggregate,'/R1/qualification/read_original_authority_and_contract_records'+tail,'EXACT_ASSOCIATED_'+row['status'],auth+row['pointer'])

def leaves(x,p=''):
    if isinstance(x,dict) and x:
        for k,v in x.items():yield from leaves(v,p+'/'+ptr_escape(k))
    elif isinstance(x,list) and x:
        for i,v in enumerate(x):yield from leaves(v,p+'/'+str(i))
    else:yield p

def classify(lp,pt):
    lookup=state_lookup.get(lp,{})
    while True:
        if pt in lookup:return lookup[pt]['status']
        if not pt:return 'UNREAD'
        pt=pt.rsplit('/',1)[0]

def unread_frontier(lp,x,p=''):
    ps=[s['pointer'] for s in states.get(lp,[])]
    if any(q=='' or p==q or p.startswith(q+'/') for q in ps):return []
    if not any(q.startswith(p+'/') for q in ps):return [p]
    out=[]
    if isinstance(x,dict):
        for k,v in x.items():out+=unread_frontier(lp,v,p+'/'+ptr_escape(k))
    elif isinstance(x,list):
        for i,v in enumerate(x):out+=unread_frontier(lp,v,p+'/'+str(i))
    else:out.append(p)
    return out

state_lookup={lp:{s['pointer']:s for s in ss} for lp,ss in states.items()}
entries=[];unreads=[]
for row in inventory:
    lp=row['logical_path'];obj=objects[lp]
    counts=Counter(classify(lp,pt) for pt in leaves(obj)) if isinstance(obj,(dict,list)) else Counter({'FULL_READ':len(obj.splitlines())})
    frontier=unread_frontier(lp,obj) if isinstance(obj,(dict,list)) else []
    status='FULL_READ' if lp in full else ('PURPOSE_FIELDS_READ_ADMIN_ROUTED' if lp in [r2,auth,selection] else 'PARTIAL_READ_UNREAD_REMAINDER')
    entries.append({'input':row,'reading_status':status,'reader':READER,'read_ranges_or_pointers':states.get(lp,[]),
      'structure_unit':'atomic JSON value/empty container; text counted separately in lines','mechanical_structure_status_counts':dict(counts),
      'full_current_source_or_formal_approval':False,'parent_reception':'NOT_RECEIVED_BY_PARENT'})
    if frontier:unreads.append({'logical_path':lp,'maximal_unread_JSON_pointers':frontier,'atomic_unread_count':counts.get('UNREAD',0),
        'reason':'Available content not actually read; not a material/host limit','continuation':'Read these exact subtrees continuously, bind further original contracts and consumers; no sample-based close'})

summary={'readset_payloads':len(entries),'decoded_bytes':sum(r['bytes'] for r in inventory),
 'fully_body_read_payloads':len(full),'fully_body_read_bytes':sum(r['bytes'] for r in inventory if r['logical_path'] in full),
 'purpose_fields_read_admin_routed_payloads':3,'partially_read_payloads':3,'not_fully_body_read_payloads':6,
 'payloads_with_actual_unread_content':len(unreads),'atomic_JSON_unread_occurrences_in_readset':sum(r['atomic_unread_count'] for r in unreads),
 'parent_received_payloads':0,'parent_not_received_payloads':len(entries),
 'semantic_clause_denominator':'UNVERIFIED_NOT_FULLY_ENUMERATED; atomic JSON values are not semantic clauses',
 'current_formal_full_body_read_by_this_task':0,'new_behavior_executions':0}
dump('reading-ledger.json',{'schema':'r8.external-h.reading-ledger.v1','reader':READER,'recorded_utc':NOW,
 'summary':summary,'entries':entries,'credit_rule':'Only named exact displayed scopes; no old PASS or parsing upgrade. Exact subtree association preserves only original scope. Raw body FULL_READ is never inferred from purpose disposition.'})
dump('unread.json',{'schema':'r8.external-h.unread.v1','summary':summary,'readset_unread':unreads,
 'additional_unread_dependencies':['R1 original primary/successor contracts not explicitly read here; inventory83 is not their body',
 'R2 original229 qualified owner records/341 contribution bodies not reread by this task',
 'R3/R4 original40 control bodies/152 criteria and applicable original source qualification',
 'R5 original92 full finite premise/case/exception/synchronization scopes;568 percheck dictionary and source record bindings',
 'R5 optional7/no-required7/policy6/limits13 complete individual semantic records',
 'B8 current necessary compiler/consumer/formal contexts beyond the cited historical reports',
 'parent-current-nonmandatory-semantic-records.json and R7-stage-identity-audit.json body; no inherited body credit claimed'],
 'disposition':'INCOMPLETE_AVAILABLE_READING; not a new limit; no full task/global PASS'})
dump('purpose-dispositions.json',{'schema':'r8.external-h.purpose.v1','reader':READER,'recorded_utc':NOW,
 'payloads':[{'logical_path':e['input']['logical_path'],'purpose':e['input']['purpose'],'status':e['reading_status'],
  'body_approval':False,'unread_exact':'unread.json','parent_reception':'NOT_RECEIVED_BY_PARENT'} for e in entries],
 'administrative_rules':{'r5_selection':'All92 selector identity rows exact equal original activation; no premise/body credit',
 'r2_control_identity':'All229 source pointer/hash routes are inventory-only; common historical stage qualifiers actually read once with complete field associations',
 'r1_authority_inventory':'All83 original-object/old-reader receipts inventory-only; purpose/state-time/qualification exact values read. Original83 bodies remain unread'},
 'duplicates':'R1/R2/R3_R4 composite and preserved_special_history exact subtree associations recorded; no unpresented sibling credit'})

baseline={'recorded_utc':NOW,'status':'READY_WITH_LIMITS_FOR_ISOLATED_READING','B8':B8,'delegation_commit':D,'R':R,'C2':C2,
 'expected_B8_tree':'751dfde81048c81390f89a65ca1d1a565ba8e1ca','expected_formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e',
 'local_mapping':{'project':str(REPO),'reference':'/workspace/pokemon-essentials','reference_origin_fork':'https://github.com/y805939188/pokemon-essentials.git','upstream_source':'Maruno17/pokemon-essentials; exact commit/tree match'},
 'local':{'head':git('rev-parse','HEAD'),'B8_tree':git('rev-parse',B8+'^{tree}'),'formal_tree':git('rev-parse',B8+':deliverables/final-specification-set'),
 'origin':git('remote','-v'),'cached_origin_main':git('rev-parse','refs/remotes/origin/main'),
 'local_main':git('rev-parse','--verify','refs/heads/main'),'local_delivery_tag':git('rev-parse','--verify','refs/tags/delivery/seventh-round-closed-final-20261016'),
 'worktrees':git('worktree','list','--porcelain'),'status':git('status','--porcelain=v1')},
 'remote_main_and_delivery_tag':'GitHub connector read observed exact B8; see remote-input-observations.json',
 'original_platform_readiness':'Mac67,835 untracked/478ignored/8worktrees/35branches/257tags not applicable to this cloud clone and not re-certified',
 'activity':'One local worktree; no conflicting writer observed in this owned directory. Other sessions state UNVERIFIED; no spawn.',
 'protected_inputs':'B8 formal/planning/audit/reference/main/tag/other task directories read-only; final staged diff must be confined to task root',
 'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'standard','Fast':False},
 'actual':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','Fast':'UNVERIFIED','platform_task_id':'UNVERIFIED'},
 'source_thread_id_is_parent_reference_not_actual_task_echo':'01a13f49-a154-7054-9b04-ce31f924d01c',
 'execution':{'reference':0,'model':0,'host':0,'Demo':0,'native_media':0,'real_save':0,'vectors':'NOT_EXECUTED','restored_code_executed':False}}
dump('preflight.json',baseline)
dump('progress.json',{'schema':'r8.external-h.progress.v1','logical_id':'EXTERNAL-H-EARLY-QUALIFICATIONS','reader':READER,
 'status':'INCOMPLETE_UNREAD_CHECKPOINT','semantic_complete':False,'recorded_utc':NOW,
 'inputs':{'B8':B8,'R':R,'delegation_commit':D},'write_root':str(TASK),'branch':'codex/r8-external-h-early-qualifications-20261016',
 'summary':summary,'actual_platform_id':'UNVERIFIED','independent_reception':'PENDING_PARENT_INDEPENDENT_COUNTERREVIEW_AND_FINAL_RECEPTION',
 'remaining_blocker':'Available unread semantic subtrees and unreceived consumer/original qualification scopes; not material unavailability',
 'publication':'CORE_NOT_YET_COMMITTED_AT_GENERATION; later publication receipt binds actual identities','update_started':False,'final_state':'UPDATE_NOT_STARTED'})
dump('findings.json',{'schema':'r8.external-h.findings.v1','reader':READER,'records':[],
 'proposed':0,'confirmed_required':0,'interpretation':'No new concrete current defect established; incomplete review is not NO_REQUIRED_UPDATE/PASS',
 'independent_counterreview':'PENDING_PARENT; no self-assigned required disposition','update_started':False})
print(json.dumps(summary,ensure_ascii=False))
