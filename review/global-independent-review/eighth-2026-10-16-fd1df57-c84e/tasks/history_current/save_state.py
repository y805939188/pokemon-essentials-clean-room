"""Persist honest review state. Extraction/identity never creates reading credit."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import subprocess

REPO = Path('/workspace/pokemon-essentials-clean-room')
TASK = Path(__file__).resolve().parent
R7ROOT = 'review/remediation-seventh-20261015-prepare/'
C2ROOT = 'review/global-independent-review/seventh-2026-10-14-e646432-7a91/'
R6ROOT = 'review/remediation-sixth-20261014-prepare/'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
R6 = '9aa72bc99a4cf52c8fb9cad8a637a963341388b0'

def read(path):
    return json.loads((REPO/path).read_text())

def save(name, value):
    (TASK/name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def identity(path, commit=B8):
    data = (REPO/path).read_bytes()
    entry = subprocess.check_output(['git', 'ls-tree', commit, '--', path], cwd=REPO).decode().split()
    return {'repository': str(REPO), 'commit': commit, 'path': path,
            'mode': entry[0] if entry else 'UNTRACKED', 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest(),
            'commit_tree': subprocess.check_output(['git', 'rev-parse', commit+'^{tree}'], cwd=REPO).decode().strip()}

def main():
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    reg = read(R7ROOT+'delegation/task-registry/current.json')
    nav = read('delivery/2026-10-16-seventh/history-navigation.json')
    binding = read(R7ROOT+'completion/final-delivery-binding.json')
    ledger = read(R7ROOT+'ledger.json')
    closure = read(R7ROOT+'closure/final/decision.json')
    deps = read(R7ROOT+'closure/final/dependency-and-history-reception.json')
    ids = [r['id'] for r in closure['records']]
    source_ids = [i for b in binding['source_bindings'] for i in b['required_ids']]
    mechanical = {
        'qualification': 'TOOL_VALIDATION_ONLY; no semantic or independent approval credit',
        'task_roles': dict(collections.Counter(x['role'] for x in reg['entries'])),
        'unique_task_ids': len({x['task_id'] for x in reg['entries']}),
        'registry_tasks_equal_history_tasks': reg['entries']==nav['tasks'],
        'binding_sources_equal_history_sources': binding['source_bindings']==nav['source_bindings'],
        'source_bindings_batches': len(binding['source_bindings']),
        'source_ids_total': len(source_ids), 'source_ids_unique': len(set(source_ids)),
        'source_ids_equal_closure_ids': set(source_ids)==set(ids),
        'unique_actual_contexts': len({b['actual_reviewer'] for b in binding['source_bindings']}),
        'U04_U05_share_actual_context': binding['source_bindings'][3]['actual_reviewer']==binding['source_bindings'][4]['actual_reviewer'],
        'ledger_counters': ledger['counters'], 'registry_semantic_stage_counters': reg['semantic_stage_counters'],
        'required_ids': ids, 'source_bindings': binding['source_bindings'],
        'tasks': reg['entries'], 'continuations': reg['continuations'],
        'severities': dict(collections.Counter(x['severity'] for x in closure['records'])),
        'shared_receivers_count': len(deps['shared_receivers'])}
    save('R7-stage-identity-audit.json', mechanical)
    c2records = read(C2ROOT+'canonical-records.json')['records']
    optional = read(R6ROOT+'inputs/optional-records.json')
    policy = read(R6ROOT+'inputs/policy-records.json')
    no_required = read(R6ROOT+'inputs/no-required-revision-records.json')
    facets = json.loads((TASK/'recovered-facets/evidence/root-h22-counter/counter-review-and-facets.json').read_text())
    save('current-nonmandatory-semantic-records.json', {
        'schema':'r8.history.nonmandatory-restoration.v1','recorded_utc':now,
        'authority_rule':'Original proposals and generation-time PENDING remain historical. Root final decisions and later exact scope overlays control. No R8 source PASS or automatic adoption.',
        'R6': {'commit':R6,'current_same_bytes':True,'optional':optional,'policy':policy,'no_required':no_required,
               'optional_current_fields_read_exclusions':['payload_identity (inventory only)','original_full_proposal (historical unreviewed copy; current verdict and scope read)'],
               'counts':{'optional_entries':8,'FLOAT_facets':1,'policy_roots':7,'limits':14,'no_required':1}},
        'R7': {'commit':C2,'records':[x for x in c2records if x['classification']!='required'],
               'current_groups_read_exclusions':['原始证据','原裁决字段定位','读取义务','全部原验收向量证据','历史依赖原证据','条件可选写集 (read for M04-001/102, other records inventory only)'],
               'extra_optional_facets':facets,
               'counts':{'optional_entries':7,'new_optional_roots':5,'inherited_optional_aliases':2,'extra_navigation_facets':2,'no_required':1,'policy_entries':2,'new_policy_roots':1,'inherited_policy_qualification_facets':1}},
        'successor_relations':[
            {'from':'R6-UI-PARTY-003','to':'GR7-M13-002','kind':'same-root optional alias'},
            {'from':'R6-D-FONT-C01','to':'GR7-M18-001','kind':'same-root optional alias'},
            {'from':'UTIL-03','to':'GR7-H14-001','kind':'source-fact qualification single trailing LF; canonical policy count7 unchanged'},
            {'from':'R6-C-P02','to':'GR7-J16-002','kind':'later narrowed mandatory source-request-color wording; old optional historical classification retained, not blanket adoption'}],
        'execution':{'new_R8_behavior':'NOT_EXECUTED','new_R8_behavior_processes':0,
                     'R7_local_Ruby_history':{'processes':1,'inputs':10,'qualification':'fixed numeric predicate only; no native game host; historical only'}}})
    full = ['README.md','CURRENT-DELIVERY.md','AGENTS.md',
            'delivery/2026-10-16-seventh/README.md','delivery/2026-10-16-seventh/cleanup-report.md',
            R7ROOT+'current-navigation-errata.json',R7ROOT+'completion/final-report.md',
            C2ROOT+'final-report.md',C2ROOT+'reading-ledger.final.json',C2ROOT+'coverage/summary.final.json',
            R7ROOT+'review-receptions/IR-U04-U05/r1/report.md']
    full += [R7ROOT+'review-receptions/'+p+'/report.md' for p in ['IR-R7-U01/r1','IR-R7-U03/r1-final',
        'IR-R7-U06/r1-final','IR-R7-U10/r1-complete','IR-R7-U12/r1-complete']]
    full += [R7ROOT+p for p in ['process-adjudications/R7-U06-IR-PROC-001/v1/decision.json',
        'closure/preflight/final-static-projection.json','completion/final-publication-receipt.json',
        'completion/current-public-reception.json','completion/public-sync-manifest.json','completion/public-sync-validation.json']]
    full += [R6ROOT+'integration/public-sync-20261014/sync-report.md']
    reading = [{'input':identity(p, C2 if p.startswith(C2ROOT) else B8),'status':'FULL_READ','range':'entire payload','reviewer':'/root/history_current'} for p in full]
    reading += [
        {'path':'contract.md','status':'FULL_READ','range':'Library lines1-241 via two nontruncated windows; exact byte reconstruction verified','bytes':36653,'sha256':'63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b'},
        {'path':'delivery/2026-10-16-seventh/eighth-review-inputs.json','status':'FIELD_SCOPE_READ','range':'all top-level fields except /formal_files identity table','excluded':'/formal_files INVENTORY_ONLY'},
        {'path':'delivery/2026-10-16-seventh/history-navigation.json','status':'FIELD_SCOPE_READ','range':'top fields and13/source_bindings','excluded':'tasks/key_commit_coverage/archive_tags ADMIN_IDENTITY inventory; registry summary/continuations separately read'},
        {'path':R7ROOT+'completion/final-delivery-binding.json','status':'FIELD_SCOPE_READ','range':'all top-level fields except /files identity table;13/source_bindings exact equal navigation','excluded':'/files INVENTORY_ONLY'},
        {'path':R6ROOT+'inputs/optional-records.json','status':'FIELD_SCOPE_READ','range':'8records, every current authoritative field; 4/5 truncated boundary separately reread','excluded':['payload_identity INVENTORY_ONLY','original_full_proposal historical copy UNREAD']},
        {'path':R6ROOT+'inputs/policy-records.json','status':'FIELD_SCOPE_READ','range':'all current policy fields,7records','excluded':['source_payload_identity INVENTORY_ONLY']},
        {'path':R6ROOT+'inputs/no-required-revision-records.json','status':'FIELD_SCOPE_READ','range':'1record, all current authoritative fields; refuted original hypothesis explicitly historical','excluded':['payload_identity INVENTORY_ONLY','original_full_proposal historical copy UNREAD']},
        {'path':C2ROOT+'canonical-records.json','status':'FIELD_SCOPE_READ','range':'current groups of7optional+1no-required+2policy; excluded navigation identities listed in nonmandatory records','excluded':'required27; original_field_binding_groups; referenced full evidence UNREAD'},
        {'path':C2ROOT+'history/qualifications.final.json','status':'FIELD_SCOPE_READ','range':'/rounds all6; other nodes only structure/locator inspection','excluded':'current56 records/nonmandatory copied containers and original qualification reports UNREAD'},
        {'path':'recovered-transport/tasks/R7-H08/findings.json','status':'FULL_READ','range':'entire restored object; original PROPOSED qualified by successor current errata'},
        {'path':'recovered-transport/tasks/R7-H08/report.md','status':'FULL_READ','range':'entire restored report; truncated sentence separately reread'},
        {'path':'recovered-transport/tasks/R7-C17/limits-and-alias-reception.json','status':'FULL_READ','range':'all14limits, overlays, aliases, qualification fields'},
        {'path':'recovered-facets/evidence/root-h22-counter/counter-review-and-facets.json','status':'FIELD_SCOPE_READ','range':'both current records excluding identity surfaces; premise_and_cases exact equal source_proposal/seven_groups, thus associated once','excluded':['original_payload_identity','fixed_payload_identities','source_proposal wrapper not all independently read']},
        {'path':'recovered-facets/evidence/root-h22-counter/optional-navigation-facets.zh.md','status':'STRUCTURE_ASSOCIATED_WITH_READ_OBJECTS','range':'outside-JSON prose fully read; both embedded JSON objects verified structurally equal full record containers; projected fields read as above'},
        {'path':R7ROOT+'delegation/task-registry/current.json','status':'FIELD_SCOPE_READ','range':'top meta plus all42identity summary; continuation states all read; full entries not all semantically read'},
        {'path':'tasks/inventory_denominator/r6-small-payload-reading.json','status':'RECEIVED_NAMED_COLLABORATOR_READ','reader':'/root/inventory_denominator','range':'R6 limit-records all14,optional-facets,historical-qualification,classification-counts; B8 and9aa identity equal','not_source_approval':True}]
    reading += [
        {'path':'recovered-early-history/tasks/R7-H12/'+p,'status':'FULL_READ','range':'entire restored payload','reviewer':'/root/history_current'}
        for p in ['preserved-special-history.json','report.md','subreaders/r1/report.md','subreaders/r2/report.md','subreaders/r3-r4/report.md']]
    reading += [
        {'path':'recovered-early-history/tasks/R7-H12/subreaders/r3-r4/qualification.json','status':'FIELD_SCOPE_READ','range':'purpose/counts/execution/R7_semantic_PASS/incident; both excluded_R3 original records entire; later_summary_residue C01-C05 entire','excluded':'/records40 old criteria bodies UNREAD'},
        {'path':R6ROOT+'integration/public-sync-20261014/sync-input.json','status':'FIELD_SCOPE_READ','range':'all56 /items rule_summary,actual_clause_label,case_controls,original_dependencies,behavior_execution; items0-6 actual_content_review full; first source locator; three joint interfaces from dependency-status','excluded':'other source locators/admin stage objects and complete original case/contract payloads UNREAD'},
        {'path':R7ROOT+'closure/final/dependency-and-history-reception.json','status':'FIELD_SCOPE_READ','range':'all top fields excluding full27records, history, all7shared_receivers; all27 required_dependency_contract current receivers/write_scope/qualification/edges; complete first record','excluded':'remaining26 root responsibility receipts/full retained-boundary containers not fully read'}]
    save('reading-ledger.json', {'recorded_utc':now,'reviewer':'/root/history_current','entries':reading,
        'rule':'FULL_READ never inferred from parsing, extraction, inventory or old PASS. Truncated attempts only credited when exact missing spans were subsequently read.',
        'local_command_stream_capture':'Earlier tool actions available in platform conversation; separate per-command local UTC/stdout/stderr not captured and not backfilled. Recovery manifests preserve their real execution outcomes.'})
    save('findings.json',{'recorded_utc':now,'proposals': [{
        'id':'GR8-HIST-001','status':'PROPOSED_PENDING_NONPROPOSER_COUNTERREVIEW','classification':'UNDECIDED','severity_proposed':'P3',
        'title':'Current R7 task registry retains unqualified early semantic stage counters beside final closure state',
        'proposer':'/root/history_current','independent_counterreview':'PENDING_ROOT_ASSIGNMENT',
        'input':identity(R7ROOT+'delegation/task-registry/current.json'),
        'source_locator':{'path':R7ROOT+'delegation/task-registry/current.json','lines':[1074,1082],'pointers':['/semantic_stage_counters','/completion_state'],'final_state_line':1126},
        'counterpart_evidence':[{'identity':identity(R7ROOT+'ledger.json'),'lines':[6,18],'pointer':'/counters'}, {'identity':identity(R7ROOT+'completion/current-public-reception.json'),'lines':[6,12]}],
        'premise':'Read the B8 named current task registry as current semantic-stage metadata; no runtime or special input needed.',
        'ordinary_control':'Registry counts/task completion describe42 tasks correctly; ledger/current-public-reception separately show27items/13batches at all four stages.',
        'minimal_counterexample':'Registry /semantic_stage_counters reports candidate3items/2batches and integrated/accepted/closed0 while the same object says root scoped closure complete and current ledger reports27/13.',
        'strongest_counterargument_to_test':'These may intentionally preserve a historical creation-time snapshot; seek an explicit field-level timestamp or generation-scope rule. Independent reviewer must decide optional navigation qualification versus required status consistency; final authoritative closure remains present elsewhere.',
        'impact':'A reader consuming the named current registry can report contradictory remaining acceptance/closure work. No game behavior or old closure invalidation is alleged.',
        'minimum_revision':'If confirmed, either give these counters an explicit historical snapshot scope/time or publish a current overlay of27/13, preserving immutable old task/review/FAIL/WAIT evidence.',
        'preserve_scope':['42unique tasks13authors17candidate12actual','U04/U05 one actual context','candidate/actual/ACCEPTED/CLOSED separate','all finite static/runtime/configuration limits','old56/92/27 ledgers unchanged until root adjudicates'],
        'normal_cancel_failure_partial':'Text-only metadata; no gameplay cancellation/commit and no runtime vector executed.',
        'evidence_level':'SOURCE_STATIC current metadata contradiction; not behavioral execution','execution':'NOT_EXECUTED',
        'negative_search':'Current object top-level metadata and entry summaries inspected; full historical scope qualification search pending. Do not infer absence globally.'}], 'required_adjudicated':0,'update_started':False})
    gaps = [
        {'scope':'R7 final closure27/dependency27/shared7','status':'UNREAD_OR_PARTIAL','paths':[R7ROOT+'closure/final/decision.json',R7ROOT+'closure/final/dependency-and-history-reception.json',R7ROOT+'closure/preflight/final-static-projection.json'],'reason':'Structure/identity inspected only; complete current record and seven shared receiver semantics still need reading'},
        {'scope':'R7 candidate freezes13 and qualified candidate reports17; actual12 plus old versions','status':'UNREAD_OR_PARTIAL','read_actual':['IR-U04-U05/r1/report.md'],'reason':'32report payloads405737bytes; only one shared actual report FULL_READ so far'},
        {'scope':'R6 nine effective supplements','status':'UNREAD_OR_PARTIAL','reason':'All exact objects restored; complete current behavior/contracts/cases across nine files not read in this task. Seven unchanged B8/9aa, matrix/audit successors differ.'},
        {'scope':'R1-R5 original qualification restoration','status':'UNREAD_OR_PARTIAL','reason':'Summary /rounds read only; exact immutable original controls, contributions, R3/R4/R5 correction scope not yet read.'},
        {'scope':'R6 original report and A-E/5c historical objects','status':'RESOLVED_ISOLATED_CACHE_READING_STILL_PENDING','reason':'Initial main-object lookup128 was not a material limit. Exact7 navigation-bound commits fetched successfully into isolated object-cache.git;15 declared payloads20339632bytes restored with original hashes; see isolated-git-recovery.json and cached-r6-recovery-manifest.json.'},
        {'scope':'C2 canonical required27/original finding evidence/handoff full3.1MB','status':'UNREAD','reason':'Not replaced by nonmandatory projection, final summary or identity parsing'},
        {'scope':'C2 manifest80MB and binding8.5MB','status':'INVENTORY_ADMIN_INDEX_PENDING_FULL_PURPOSE_DISPOSITION','reason':'Sizes/structure known; all identity-only rows may receive inventory treatment, embedded current semantics must be separately extracted/read'}]
    save('unread-and-blockers.json', {'recorded_utc':now,'gaps':gaps,'unread_is_not_material_limit':True})
    progress = json.loads((TASK/'progress.json').read_text())
    progress.update(updated_utc=now,status='RUNNING',completed=['Contract and root AGENTS full read','24 exact fixed Git blobs safely restored; all matched','5 selected gzip evidence files302328bytes safely restored','3 optional-facet payloads safely restored','R6 optional8/policy7/no-required1 current fields read','R7 optional7/policy2/no-required1 current semantic groups read','R7 H08 two extra optional facets restored/current fields read','R7 C17 all14 retained limits/alias overlays full read','R7 task42 and required27/batch13 mechanical identities verified'],
                    pending=[g['scope'] for g in gaps],findings='findings.json',reading_ledger='reading-ledger.json',
                    evidence='R7-stage-identity-audit.json; recovery-manifest.json; transport-recovery-manifest.json; facet-recovery-manifest.json',
                    behavior_execution='NOT_EXECUTED',update_status='UPDATE_NOT_STARTED',
                    followup_dispatch='subshards.json: four PLANNED_NOT_DISPATCHED independent readsets/prompts; parent assigns actual contexts/write roots',
                    material_recovery='7 exact historical commits fetched to isolated bare cache;15 original payloads recovered; no material blocker asserted from initial local absence')
    save('progress.json',progress)
    print(json.dumps({'saved_utc':now,'task_ids':mechanical['unique_task_ids'],'actual_contexts':mechanical['unique_actual_contexts'],'required_ids':len(ids),'proposal_pending':1,'full_read_entries':sum(x['status']=='FULL_READ' for x in reading),'scope_complete':False}))

if __name__ == '__main__':
    main()
