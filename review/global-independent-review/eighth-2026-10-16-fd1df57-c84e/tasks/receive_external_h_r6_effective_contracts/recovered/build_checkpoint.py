from pathlib import Path
import collections, datetime, gzip, hashlib, json, subprocess

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[4]
UTC = datetime.datetime.now(datetime.timezone.utc).isoformat()
FULL = {0,6,9,15,19,21,39,40,41,42,47,48,50,52,54,56,58}
CATALOG = json.loads((TASK/'payload-catalog.json').read_text())
PRIOR = json.loads((TASK/'named-field-reception.json').read_text())
NAMED = {18:PRIOR['rows'][0],20:PRIOR['rows'][1],22:PRIOR['rows'][2]}
READING = []
COUNTS = collections.Counter()

def encode(value):
    return json.dumps(value,ensure_ascii=False,separators=(',',':')).encode()

def identity(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

def write(name,value):
    (TASK/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def terminal_values(value,pointer=''):
    if isinstance(value,dict) and value:
        for key,item in value.items():
            yield from terminal_values(item,pointer+'/'+key.replace('~','~0').replace('/','~1'))
    elif isinstance(value,list) and value:
        for i,item in enumerate(value):
            yield from terminal_values(item,pointer+'/'+str(i))
    else:
        yield pointer,value

def reading_state(row,pointer):
    if row in {0,6}:return 'SAME_TURN_IDENTICAL_PAYLOAD_READING_ASSOCIATION'
    if row in FULL:return 'DIRECT_FULL_READ'
    if row in NAMED:
        if pointer in NAMED[row]['received_current_leaf_pointers']:
            return 'NAMED_PRIOR_FIELD_ASSOCIATED_PENDING_MAIN_RECEPTION'
        for z in NAMED[row]['excluded_subtrees']:
            if pointer==z['pointer'] or pointer.startswith(z['pointer']+'/'):
                return 'UNREAD_ORIGINAL_PROPOSAL' if 'original_full_proposal' in z['pointer'] else 'INVENTORY_ONLY_IDENTITY'
    if row in {4,13} and pointer.startswith('/items/'):
        a=pointer.split('/')
        if len(a)>3 and a[3] in {'rule_summary','actual_clause_label','case_controls','original_dependencies','behavior_execution'}:
            return 'NAMED_PRIOR_FIELD_ASSOCIATED_PENDING_MAIN_RECEPTION'
        if len(a)>3 and int(a[2])<7 and a[3]=='actual_content_review':
            return 'NAMED_PRIOR_FIELD_ASSOCIATED_PENDING_MAIN_RECEPTION'
    if row in {5,14}:
        if not (pointer.startswith('/edges/') or pointer.startswith('/per_id/')):
            return 'DIRECT_FIELD_READ'
        if pointer.startswith('/per_id/0/'):
            return 'DIRECT_FIELD_READ'
        if pointer.startswith('/edges/'):
            a=pointer.split('/'); i=int(a[2])
            if i in {0,28,107}:return 'DIRECT_FIELD_READ'
            if len(a)>4 and a[3]=='evidence':
                k=a[4]
                if k.endswith('_identity') or k.endswith('_commit') or k in {'candidate','candidate_PASS_review','actual_workspace_tree','actual_formal_tree'}:
                    return 'INVENTORY_ONLY_IDENTITY'
            return 'DIRECT_FIELD_READ'
    if row==37:
        if not pointer.startswith('/records/'):return 'DIRECT_FIELD_READ'
        a=pointer.split('/'); i=int(a[2])
        if i<28 or i>=42:return 'DIRECT_FIELD_READ'
        if len(a)>5 and a[3]=='current_fact_reference' and a[5] in {'rule','id','execution','evidence_level','sourceconsumer_binding_qualification'}:
            return 'DIRECT_FIELD_READ'
    return 'UNREAD_FOR_COMPLETION'

with gzip.open(TASK/'terminal-reading-ledger.jsonl.gz','wb') as stream:
    for item in CATALOG['rows']:
        row=item['row'];data=gzip.decompress((TASK/item['decoded_object']).read_bytes())
        try:
            value=json.loads(data);kind='JSON_TERMINAL_VALUES_AND_EMPTY_CONTAINERS'
            leaves=list(terminal_values(value))
        except (ValueError,UnicodeDecodeError):
            value=None;kind='TEXT_PHYSICAL_LINES'
            leaves=[(f'/lines/{i}',line) for i,line in enumerate(data.decode().splitlines(),1)]
        states=collections.Counter()
        for pointer,val in leaves:
            state=reading_state(row,pointer);states[state]+=1;COUNTS[state]+=1
            stream.write(encode({'row':row,'pointer':pointer,'status':state})+b'\n')
        if row in {0,6}:state='FULL_READ_ASSOCIATED_IDENTICAL_SAME_TURN_BYTES'
        elif row in FULL:state='FULL_READ'
        elif any(s.startswith('DIRECT') for s in states):state='FIELD_SCOPE_READ_WITH_UNREAD_REMAINDER'
        elif any(s.startswith('NAMED') for s in states):state='NAMED_FIELD_ASSOCIATION_WITH_UNREAD_REMAINDER'
        else:state='UNREAD_FOR_COMPLETION'
        READING.append({'row':row,'input':item['input'],'payload_recovery':item['decoded_object'],
            'reader':'/root (external_h_r6_effective_contracts)','platform_uuid':'UNVERIFIED',
            'recorded_utc':UTC,'individual_original_read_utc':'UNVERIFIED_NOT_BACKFILLED',
            'reading':state,'range':'entire exact payload' if row in FULL else 'exact per-terminal pointers in terminal-reading-ledger.jsonl.gz',
            'unit_kind':kind,'terminal_or_line_count':len(leaves),'statuses':dict(states),
            'source_or_current_formal_approval':False,'main_reception':'NOT_RECEIVED'})

write('reading-ledger.json',{'schema':'r8.external-r6-reading-ledger.v1','recorded_utc':UTC,
    'direct_reader':'/root','actual_model':'UNVERIFIED','actual_effort':'UNVERIFIED','actual_tier':'UNVERIFIED','actual_speed':'UNVERIFIED','actual_fast':'UNVERIFIED',
    'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'default','fast':False},
    'rule':'Parsing, exact identity, recovery, old PASS and locator reading supply no current source or formal-clause approval. Terminal units are not behavior requirement counts.',
    'full_read_rows':sorted(FULL),'full_read_rows_count':len(FULL),'not_full_read_rows_count':60-len(FULL),
    'direct_full_read_unique_payloads':15,'same_turn_byte_associated_version_rows':{'0':9,'6':15},'version_and_alias_multiplicity_preserved':True,'terminal_or_line_status_counts':dict(COUNTS),
    'entries':READING,'contract_inputs':'input-verification.json',
    'prior_receipt_read':{'path':'prior-reading-receipts/reading-ledger.json','range':'entire payload','reader':'/root','associated_reader':'/root/history_current'},
    'truncated_attempts':[
        {'object':'readset via initial GitHub tool output','credit':'none until complete three contiguous slices were read'},
        {'object':'global prompt initial combined output','credit':'middle explicitly reread; all original content read across nontruncated windows'},
        {'object':'R6-U01 scope_contracts/0 20000-character inspection','credit':'fragment only; no completed contract credit'},
        {'object':'C17 records18:32 and all14 H21 projections','credit':'no full-object credit for truncated records; records18:27 explicitly reread; exact rule/evidence/qualification fields28:41 explicitly reread'}],
    'private_platform_stream':'Actual earlier calls remain in platform conversation. No claim that original private stream was newly published or all original command UTC/stdout/stderr were captured.'})

contracts=[]
for row in range(23,37):
    item=CATALOG['rows'][row];d=json.loads(gzip.decompress((TASK/item['decoded_object']).read_bytes()))
    for i,c in enumerate(d['scope_contracts']):
        contracts.append({'id':c['id'],'row':row,'pointer':f'/scope_contracts/{i}',
            'complete_seven_group_read':'UNREAD','current_R_source_and_B8_clause_chain':'NOT_RECEIVED',
            'behavior_execution':'NOT_EXECUTED','necessary_consumers':c.get('bidirectional_evidence',{}).get('necessary_consumers')})
assert len(contracts)==56 and len({c['id'] for c in contracts})==56
c17=json.loads(gzip.decompress((TASK/CATALOG['rows'][37]['decoded_object']).read_bytes()))
assert len(c17['records'])==56 and sum(z['case_count'] for z in c17['records'])==351
case_rows=[{'id':z['canonical_R6_id'],'owner':z['owner'],'count':z['case_count'],
    'case_reference':z['case_reference'],'reading':'UNREAD_CASE_BODIES','B8_reception':'NOT_RECEIVED'} for z in c17['records']]
write('unread.json',{'schema':'r8.external-r6-unread.v1','recorded_utc':UTC,
    'state':'INCOMPLETE_READING_BLOCKS_ACCEPTANCE','material_limit':False,
    'reason':'Actual full sequential semantic reading and necessary consumers have not been completed. These are available unread materials, not host/material exemptions.',
    'payload_rows':60,'full_read':17,'not_fully_read':43,'exact_units':'terminal-reading-ledger.jsonl.gz',
    'complete_contracts':{'denominator':56,'complete_read':0,'unread_or_incomplete':56,'records':contracts},
    'case_bodies':{'denominator':351,'complete_read':0,'unread':351,'groups':case_rows},
    'dependency_edges':{'denominator':110,'current_gate_fields_read':110,'fresh_original_evidence_and_consumer_reception':0,'unreceived':110},
    'joint_interfaces':{'denominator':3,'qualification_records_read':3,'fresh_B8_source_consumer_acceptance':0,'unreceived':3},
    'historical_actual_root_reports':{'denominator':5,'full_read':5,'original_structured_verdicts_full_read':0},
    'historical_final_registry':{'report_full_read':True,'verdict_full_read':False},
    'nine_supplement_version_rows':{'denominator':18,'full_read':4,'not_full_read':14},
    'source_full_files_fresh':0,'B8_formal_full_files_fresh':0,
    'additional_dependencies':'R7-H19/H20/H21/H22 case and clause bodies, R/B8 necessary consumers, public matrix/audit predecessor and successor full text, full original proposals and report-manifest current effective semantics remain for continued reading.',
    'not_required_absence_verdict':True})

groups=[('A',11,48),('B',9,50),('C',19,52),('D',9,54),('E',8,56)]
history={'schema':'r8.external-r6-history-current-acceptance.v1','recorded_utc':UTC,
    'state':'QUALIFIED_HISTORICAL_ASSERTIONS_READ_CURRENT_SOURCE_ACCEPTANCE_PENDING',
    'groups':[{'group':g,'unique_primary_required_count':n,'readset_row':i,'root_report_full_read':True,'binding_actual':'86bbc99b28d93db4ed9d6897daf5f3725ccd1808','binding_formal_tree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c','original_structured_verdict_full_read':False,'not_B8_global_approval':True} for g,n,i in groups],
    'phase_chain':[
        {'stage':'actual independent content','commit':'86bbc99b28d93db4ed9d6897daf5f3725ccd1808','counts':[11,9,19,9,8],'meaning':'five scoped static reports; no formal acceptance or closure'},
        {'stage':'final independent registry','commit':'5c9aecc14e2da1e79256edf1e189a77dcc104d86','report_row':58,'snapshot':'accepted0/CLOSED0/OPEN56; 108 gates plus two future process gates','meaning':'finite exact registry eligibility only; no new behavior or configuration certificate'},
        {'stage':'formal acceptance','commit':'b7b2b31a40478bd95ea677d713e8882113acdb90','reported_utc':'2026-10-14T19:41:34.391764+00:00','snapshot':'accepted56/CLOSED0','independent_full_stage_payload_read':False},
        {'stage':'closure','commit':'4df21dee08c3afe054ed12d8416f55fd3ea6317b','reported_utc':'2026-10-14T19:45:15.282641+00:00','snapshot':'CLOSED56/OPEN0 within original finite static contracts','independent_full_stage_payload_read':False}],
    'joint_interfaces':[
        {'primary':'E','receiver':'D','ids':['GR6-F-002'],'scope':'0/1/3; raw-negative versus Standard-negative; focus is not submit; nil versus [] identity; counts once'},
        {'primary':'E','receiver':'B','ids':['GR6-F-V004'],'scope':'Arena cancellation preserves surviving winner recharge; earlier Disable gate and Charge cleanup distinct; counts once'},
        {'primary':'A','receiver':'C','ids':['R6-D-LZ-001','R6-D-LZ-002','R6-D-PBS-C05','R6-D-PBS-C06','R6-D-PBS-C07','R6-D-DATA-C01'],'scope':'C signs named language/data/cache consumers only; no additional primary count'}],
    'U13':{'old_candidate':'00b45de642f07cee9953e42f04cce9c35d77346f','old_FAIL_report':'3ef4854ef43eac92fd1dc57350e4cf6aa160082b','repair_candidate':'9971fe84896786645cdcda3ab45e5caf7785cabc','repair_PASS_report':'411b563309a4e642e628dcf8289e36c6fe3fd37f','both_root_reports_full_read':True,'old_reason':'S001 lost SF30 normal save/load and default conversion controls; wrong R5 path-absence assertion and overstrong tool uniqueness/probability claims also needed correction. F002 WP66-A was an allowed later integration condition, not candidate allowlist defect.','repair_scope':'SF30 d/e restored without reviving blanket active-save prohibition; retrieval notes and generators corrected, original failure cause unknown; tool proof narrowed. Candidate PASS still awaited actual receiver review.','actual_successor':'E report plus D F002 receiver and B Arena receiver are separately bounded; original FAIL not rewritten'},
    'nonmandatory':'named-field-reception.json; 8 optional, one FLOAT facet, 7 policy, 14 limits, one no-required stay separate; original_full_proposal unread not promoted to FULL_READ',
    'historical_execution':{'Ruby_attempts':18,'known_exit0':12,'known_nonzero':4,'unknown_exit':2,'entered_definition':17,'not_loaded':1,'invalid_or_duplicate_present':True,'not18_successful_tests':True},
    'new_behavior_execution':{'state':'NOT_EXECUTED','processes':0},'main_final_reception':'NOT_RECEIVED','UPDATE_NOT_STARTED':True}
write('history-current-acceptance.json',history)

purposes=[]
for item in READING:
    row=item['row']
    purpose=('current effective supplement and historical stage identity, versions separate' if row<18 else
             'nonmandatory current fields and historical proposals, no automatic adoption' if row<23 else
             'complete normative contracts requiring original source and B8 consumer review' if row<37 else
             'historical reception/current assertion container requiring independent present source reception')
    purposes.append({'row':row,'path':item['input']['path'],'commit':item['input']['commit'],'purpose':purpose,
        'reading':item['reading'],'identity_checks':'payload-catalog.json','effective_semantics_exempted':False,
        'unread_status':'unread.json','same_bytes_aliases_do_not_inherit_PASS':True})
write('purpose-dispositions.json',{'schema':'r8.external-r6-purpose-dispositions.v1','rows':purposes,
    'deduplication':{'decoded_rows':60,'unique_decoded_objects':52,'same_bytes_nine_supplement_pairs':7,
    'different_predecessor_successor_pairs':['planning/feature-matrix.md','audit/source-traceability.md'],
    'duplicate_manifest_identity':'rows38 and44 exact same decoded object; both source roles retained'}})
write('findings.json',{'schema':'r8.external-r6-findings.v1','recorded_utc':UTC,'proposed':[],
    'confirmed_required':[],'verdict':'NOT_ADJUDICATED_READING_INCOMPLETE','NO_REQUIRED_UPDATE':False,
    'independent_counter_review':'PENDING_MAIN_REVIEW_IF_PROPOSED','current_source_approval':False})
write('progress.json',{'schema':'r8.external-r6-progress.v1','updated_utc':UTC,
    'logical_task_id':'external_h_r6_effective_contracts','actual_platform_id':'UNVERIFIED','routing_name':'/root',
    'source_thread_reference':'01a13f49-a154-7054-9b04-ce31f924d01c','source_thread_is_own_platform_id':False,
    'task_state':'INTERRUPTED','semantic_state':'INCOMPLETE_READING_BLOCKS_ACCEPTANCE',
    'publication_state':'PENDING_OWN_BRANCH_COMMIT_AND_ORDINARY_PUSH',
    'B8':'fd1df570cad987dc3852a3b958f03916e317f7fe','R':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
    'contract_commit':'30cfed0996003b6ebf4b5c51cc04f31ca9255440',
    'branch':'codex/r8-external-h-r6-effective-contracts-20261016','write_root':str(TASK),
    'spawned_agents':0,'formal_changes':0,'update_started':False,'update_status':'UPDATE_NOT_STARTED',
    'denominators':{'rows':60,'decoded_bytes':44241376,'unique_decoded_objects':52,'full_read_rows_including_identity_associations':17,'direct_full_read_unique_payloads':15,
    'not_full_read_rows':43,'contracts':56,'complete_contracts_read':0,'cases':351,'case_bodies_read':0,
    'edges':110,'gate_fields_read':110,'edge_evidence_and_consumers_accepted':0,'joint_interfaces':3,'B8_joint_source_acceptances':0},
    'remaining_blocker':'Available semantic reading remains incomplete. No material/host limitation is used to excuse it; main reviewer must continue and independently receive exact scopes.',
    'all_new_behavior':'NOT_EXECUTED','effective_configuration':'UNVERIFIED'})
write('checkpoint-validation.json',{'utc':UTC,'rows':60,'identities_verified':60,
    'contracts_unique':len(contracts),'cases_sum':sum(x['count'] for x in case_rows),
    'FULL_READ_only_direct_bound_payloads':True,'no_behavior_execution':True,
    'terminal_reading_ledger_identity':identity((TASK/'terminal-reading-ledger.jsonl.gz').read_bytes()),
    'tool_validation_does_not_create_semantic_credit':True})
print(json.dumps({'full_rows':17,'not_full_rows':43,'units':sum(COUNTS.values()),'states':dict(COUNTS)},ensure_ascii=False))
