"""Serialize this auditor's actual reading limits and mechanical registers.

This does not manufacture semantic acceptance, run a target program, or write
outside this task. Existing immutable evidence is referenced, not changed.
"""
import collections
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

BASE = Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e')
OUT = BASE / 'tasks/coverage_acceptance_incremental'
PROJECT = Path('/workspace/pokemon-essentials-clean-room')
REFERENCE = Path('/workspace/pokemon-essentials')
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
DATA = json.loads((BASE / 'delegation/readsets/coverage-incremental-v2.json').read_text())
ENTRIES = DATA['snapshot_entries']
BY_PATH = {entry['original_path']: entry for entry in ENTRIES}
FULL = {299, 158, 121, 90, 36, 47, 71, 115, 138, 223, 262, 168, 179, 31, 64, 238, 194, 218}
CONTRACT_ASSOCIATIONS = {202, 203}
PARTIAL = {151, 86, 129, 153, 123, 91, 297, 295, 177, 166}
FULL_INTERFACES = {31, 64, 238, 194, 218}

def load(entry):
    return json.loads((BASE / entry['snapshot']).read_text())

def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def identity(path):
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}

coverage = json.loads((OUT / 'file-coverage.json').read_text())
identity_check = []
for repo, root, commit in [('R', REFERENCE, DATA['R']), ('F', PROJECT, DATA['B8'])]:
    command = ['git', '-C', str(root), 'ls-tree', '-rz', '--full-tree', commit]
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    run = subprocess.run(command, capture_output=True)
    end = datetime.datetime.now(datetime.timezone.utc).isoformat()
    (OUT / f'{repo}-fixed-tree.stdout.bin').write_bytes(run.stdout)
    (OUT / f'{repo}-fixed-tree.stderr.txt').write_bytes(run.stderr)
    trees = {}
    for item in run.stdout.split(b'\0'):
        if not item:
            continue
        metadata, raw_path = item.split(b'\t', 1)
        mode, typ, blob = metadata.decode().split()
        trees[raw_path.decode()] = {'mode': mode, 'type': typ, 'blob': blob}
    mismatches = []
    for entry in coverage['files']:
        if entry['repo'] == repo:
            tree = trees.get(entry['path'])
            if not tree or tree['blob'] != entry['git_blob']:
                mismatches.append(entry['path'])
    identity_check.append({'repo': repo, 'command': command, 'start_utc': start, 'end_utc': end,
                           'exit_code': run.returncode, 'stdout': f'{repo}-fixed-tree.stdout.bin',
                           'stderr': f'{repo}-fixed-tree.stderr.txt', 'checked_files': 432 if repo == 'R' else 131,
                           'mismatches': mismatches, 'semantic_credit': False})

read_records = []
for index, entry in enumerate(ENTRIES):
    state = ('FULL_ARTIFACT_READ' if index in FULL else
             'SAME_BYTES_LINK_TO_PERSONALLY_FULL_READ_CONTRACT_NO_SECOND_READING' if index in CONTRACT_ASSOCIATIONS else
             'PARTIAL_OR_SELECTED_STRUCTURE_FIELDS_ONLY' if index in PARTIAL else
             'IDENTITY_VERIFIED_AND_MACHINE_LOADED_NOT_PERSONALLY_SEMANTICALLY_READ')
    read_records.append(dict(entry, read_state=state,
                             reader='/root/coverage_acceptance_incremental',
                             source_or_formal_semantic_credit=False,
                             exact_unread_scope=('NONE_FOR_ARTIFACT_TEXT' if index in FULL or index in CONTRACT_ASSOCIATIONS else
                                                 'FULL_PAYLOAD_REQUIRES_CURRENT_FIELD_PURPOSE_DISPOSITION_OR_ACTUAL_READING; PARTIAL_SELECTIONS_DO_NOT_CLOSE_REMAINDER'),
                             original_read_io=('read-%03d.receipt.json' % index if (OUT / ('read-%03d.receipt.json' % index)).exists() else
                                               'PRIVATE_PLATFORM_TOOL_OUTPUT; NO_RETROACTIVE_RAW_IO_OR_UTC_INVENTED')))
unread_shas = {e['sha256'] for i,e in enumerate(ENTRIES) if i not in FULL | CONTRACT_ASSOCIATIONS}
full_shas = {e['sha256'] for i,e in enumerate(ENTRIES) if i in FULL | CONTRACT_ASSOCIATIONS}
unread_shas -= full_shas
sha_size = {e['sha256']:e['bytes'] for e in ENTRIES}
dump('reading-ledger.json', {
    'schema':'gr8-incremental-auditor-reading-ledger/v1', 'utc':NOW,
    'contract_full_reads':[
        identity(BASE / 'delegation/prompts/coverage-incremental-v2.md'),
        identity(BASE / 'inputs/eighth-global-review-prompt.md'),
        identity(PROJECT / 'AGENTS.md'), identity(BASE / 'inputs/review-SKILL.md'),
        dict(identity(BASE / 'delegation/readsets/coverage-incremental-v2.json'),
             complete_mapping_read='All fields of301entries read; initially truncated middle was re-read in continuous50-entry windows')],
    'snapshot_payloads':read_records, 'full_frozen_artifact_payloads_personally_read':len(FULL),
    'same_bytes_contract_associations':len(CONTRACT_ASSOCIATIONS),
    'remaining_not_fully_personally_semantically_read_unique_sha':len(unread_shas),
    'remaining_not_fully_personally_semantically_read_unique_bytes':sum(sha_size[sha] for sha in unread_shas),
    'full_contribution_reports_read':13, 'full_interface_artifacts_read':5,
    'full_interface_records_read':41,
    'audit_own_R_full_text_reads':0, 'audit_own_formal_full_text_reads':0,
    'qualification':'Full report or interface artifact reading does not replace its source facts, clauses, premises, original complete I/O or consumer reception. Machine loading all301snapshots is not semantic reading.'})

old_locators = []
old_stats = []
for index,key,identifier,path_key in [(151,'clauses','clause_id','path'),(86,'rows','id','path'),(129,'rows',None,'formal_path')]:
    frozen = ENTRIES[index]; document = load(frozen); rows=document[key]
    for row_index,row in enumerate(rows):
        old_locators.append({'matrix':frozen['original_path'],'snapshot':frozen['snapshot'],'sha256':frozen['sha256'],
                             'json_pointer':f'/{key}/{row_index}',
                             'id':row.get(identifier) if identifier else f"CRE-LOC:{row['formal_path']}:L{row['line']}",
                             'path':row[path_key], 'range':row.get('range',[row.get('line'),row.get('line')]),
                             'sourcefact_links':row.get('fact_links',row.get('source_facts',row.get('manual_fact_candidates',[]))),
                             'original_pending_fields':{k:v for k,v in row.items() if k in ('claim_reconciliation','premise_status','support_status','premises','composite_subassertions','source_facts_complete','premise_and_consumer_reception_complete')},
                             'auditor_semantic_reception':'NOT_GRANTED; STATUS_AND_LINK_AUDIT_ONLY',
                             'completion_requirement':'Every substantive child assertion needs a complete sourcefact/premise/consumer chain and an actual nonauthor receiver. Layout needs explicit bounded type disposition.'})
    old_stats.append({'path':frozen['original_path'],'rows':len(rows),
                      'all_still_not_complete_in_frozen_matrix':True,
                      'actual_semantic_atomic_denominator':'UNFROZEN',
                      'not_a_count_of_bad_clauses':True})

wp = json.loads((BASE / 'tasks/inventory_denominator/wp-map.json').read_text())
wp_inventory = [dict(row, independent_incremental_atomic_reception='NOT_ESTABLISHED',
                     remaining_requirement='All current bodies/data/coverage/catalog subassertions and actual interfaces; inventory membership is not accepted semantic coverage') for row in wp['work_packages']]
reported_manual = [
    {'domain':'WORLD','artifacts':[ENTRIES[i]['original_path'] for i in (258,259,260,261)],'reported_scope':[{'wp':'WP12','groups':145,'subassertions':265},{'wp':'WP14','groups':187,'subassertions':284},{'wp':'WP59','groups':195,'subassertions':346},{'wp':'WP60','groups':86,'subassertions':105}],'qualification':'Only manual artifact headers inspected here; complete child facts and consumers not personally read; no sum into a global denominator'},
    {'domain':'UI','artifact':ENTRIES[222]['original_path'],'reported_subassertions':638,'reported_source_assertions':642,'reported_source_units':99,'scope':'WP17 304 plus WP63 334; source/control and scope remain local','complete_semantic_reception_by_this_audit':False},
    {'domain':'AI','artifact':ENTRIES[48]['original_path'],'reported_manual_source_groups':65,'reported_source_facts':196,'reported_reverse_groups':72,'reported_reverse_branch_assertions':273,'reported_catalog_rows':285,'scope':'Primary29full declaration; default/backup/compile/reload external interface remains open','complete_semantic_reception_by_this_audit':False},
    {'domain':'MOVE','artifact':ENTRIES[71]['original_path'],'reported_parent_assertions':231,'reported_child_assertions':1432,'reported_stage_units':114,'reported_Fling_Flags_fields':578,'reported_vectors':331,'qualification':'Overlapping different partitions; cannot add231+1432+114+578+331 as atomic denominator','complete_semantic_reception_by_this_audit':False},
    {'domain':'ABILITY_ITEM','artifact':ENTRIES[36]['original_path'],'reported_families':80,'reported_expanded_pairs':463,'reported_reverse_locator_rows':441,'reported_phrase_condition_locations':1479,'reported_vectors':116,'qualification':'Families/pairs/phrase locators/vectors differ; raw source reader remains com_move','complete_semantic_reception_by_this_audit':False},
    {'domain':'CRE_B','artifact':ENTRIES[115]['original_path'],'reported_primary_source_units':50,'reported_dependency_units':42,'reported_formal_groups':47,'reported_vectors':125,'reported_interfaces':20,'reported_finite_accepted_interfaces':15,'reported_open_interfaces':5,'complete_semantic_reception_by_this_audit':False},
    {'domain':'PBS_BATTLE','artifact':ENTRIES[168]['original_path'],'reported_primary_paths':21,'reported_path_record_instances':7704,'reported_own_raw_or_field_view_paths':11,'reported_own_same_bytes_associations':5,'reported_CRE_B_full_raw_contributions':4,'reported_CRE_B_same_bytes_association':1,'reported_manual_fact_groups':20,'reported_local_reverse_units':21,'global_reception':'PB-O01–04OPEN; notall62externalpathsclosed','complete_semantic_reception_by_this_audit':False},
    {'domain':'PBS_FACILITY','artifact':ENTRIES[179]['original_path'],'reported_primary_paths':7,'reported_Tower_raw_records':882,'reported_trainer_structure_records':1600,'reported_trainer_fields':9600,'reported_formal_groups':62,'reported_test_rows':196,'qualification':'Six trainer raw files not claimed separately displayed; view/tuple/pool/linkage proof and actual scope need reception','complete_semantic_reception_by_this_audit':False},
    {'domain':'H_R7','artifact':ENTRIES[138]['original_path'],'reported_payloads':243,'reported_candidate_versions':17,'reported_actual_result_versions':15,'reported_actual_contexts':12,'reported_unique_tasks':42,'qualification':'32versions and finite27closure accepted by contributor; full7.6MB ledger/precise current fields not fully read by this auditor; no currentB8gameplayPASS','complete_semantic_reception_by_this_audit':False},
    {'domain':'BINARY','scope':'Frozen controller/text readsets plus later Ruby/zlib/YARB deltas','qualification':'Candidate occurrence counts are not program/semantic atom counts; fourBINnegativeclaims bounded;16YARBactual programs must be received separately','complete_semantic_reception_by_this_audit':False},
]

interface_register=[]
for index,frozen in enumerate(ENTRIES):
    if frozen['original_path'].endswith('/interfaces.json') or frozen['original_path'].endswith('-interfaces.json'):
        document=load(frozen)
        interface_register.append({'original_path':frozen['original_path'],'snapshot':frozen['snapshot'],
                                   'sha256':frozen['sha256'],'captured_utc':frozen['captured_utc'],
                                   'artifact_full_read_by_auditor':index in FULL_INTERFACES,
                                   'full_original_structure':document,
                                   'audit_decision':'FINITE_QUALIFIERS_READ_NO_GLOBAL_PROMOTION' if index in FULL_INTERFACES else 'PENDING_FULL_ARTIFACT_AND_SUPPORT_RECEPTION',
                                   'no_acceptance_from_serialization':True})
dump('atomic-and-interface-denominator.json', {'schema':'gr8-incremental-atomic-interface-register/v1','utc':NOW,
     'global_source_semantic_atomic_denominator':'UNFROZEN', 'global_formal_atomic_denominator':'UNFROZEN',
     'global_effective_interface_denominator':'UNFROZEN', 'fixed_file_denominators':{'R':432,'F':131,'B8_effective_inventory_reported':980},
     'not_atomic_denominators':{'plan_rows':87,'features':113,'declared_dependency_edges':395},
     'all_WP_inventory':wp_inventory,'reported_manual_partial_denominators':reported_manual,
     'old_locator_state_audits':old_stats,'old_locator_rows':old_locators,
     'interface_artifacts':interface_register,'independent_complete_global_acceptance':False,
     'qualification':'No count of method/locator/source lines/samebytes/script output is promoted to actual semantic atom or consumer acceptance. Unread manual records are exact available pending work.'})

root=load(ENTRIES[297]); decisions=[]
for index,row in enumerate(root['records']):
    decisions.append({'id':row['id'],'json_pointer':f'/records/{index}',
                      'source_snapshot':ENTRIES[297]['snapshot'],'source_sha256':ENTRIES[297]['sha256'],
                      'original_classification':row['classification'],'original_severity':row['severity'],
                      'proposer':row.get('proposer'),'actual_nonproposer_reviewer':row.get('actual_nonproposer_reviewer'),
                      'status':row.get('status'),'root_complete_semantic_contract_received':row.get('complete_semantic_contract_received'),
                      'metadata_only_audit':True,'entire_contract_and_original_independent_version_received_by_this_auditor':False,
                      'global_completion_granted':False,'audit_disposition':'PRESERVE_ROOT_BOUNDED_CLASSIFICATION; INCREMENTAL_QUALIFICATION_RECEPTION_PENDING'})

supplemental=[]
(OUT/'supplemental-inputs').mkdir(exist_ok=True)
for name in ['root-binary-bounded-receptions.json','root-ui002-reception.json']:
    path=BASE/'adjudication'/name; raw=path.read_bytes(); ident=identity(path)
    target=OUT/'supplemental-inputs'/name;target.write_bytes(raw)
    supplemental.append(dict(ident,local_frozen_copy=str(target.relative_to(BASE)),
                              read_scope='FULL_ARTIFACT_TEXT_ACTUALLY_READ',
                              source_or_formal_full_read_credit=False,
                              original_read_utc='NO_PER_READ_TOOL_UTC_ECHO; NOT_RETROFILLED',
                              original_tool_chunks=['3276ad','a779e1'] if name.startswith('root-binary') else ['a779e1']))
dump('acceptance-register.json',{'schema':'gr8-incremental-acceptance-register/v1','utc':NOW,
      'auditor':'/root/coverage_acceptance_incremental','independence':'Actual new context; not a primary domain semantic author. No role renaming or extra child created.',
      'frozen_root_bounded_counts':root['bounded_counts'],'whole_review_required_count':'UNKNOWN_NOT_FINAL',
      'root_records':decisions,'root_record_qualification':'All21IDs/classifications/actorfields parsed; complete contracts/root restrictions/original full versions not all personally read. No independent re-certification granted.',
      'supplemental_full_reads':supplemental,
      'binary_negative_claims':{'ids':['GR8-BIN-001','GR8-BIN-002','GR8-BIN-003','GR8-BIN-004'],'read_scope':'All four complete root objects and full embedded proposals read','preserved_scope':'Only each finite negative claim; not binary/native/resource/global no-required or successful host execution'},
      'UI002':{'version':'v1 exception candidate','disposition':'ROOT_BOUNDED_REJECTED_PRESERVED','new_visibility_candidate':'NOT_AUTOMATICALLY_REQUIRED'},
      'late_deltas':[{'id':'UI003_OPTIONAL','state':'ROOT_REPORTED_AFTER_FREEZE_NOT_READ_OR_RECEIVED_HERE'},
                     {'id':'WRR_FINAL_AND_WORLD_RECEIPT','state':'ROOT_REPORTED_AFTER_FREEZE_NOT_READ_OR_RECEIVED_HERE','reported':'69/1282 source;693+288body;205vectors822+41supp;requested410corrected406'},
                     {'id':'RUBY_ZLIB_20907_16YARB','state':'ROOT_REPORTED_AFTER_FREEZE_NOT_READ_OR_RECEIVED_HERE','reported':'20907candidate textdisposition;16recoveredreadableYARBprograms not yet independently received here'},
                     {'id':'WORLD_CATALOG_REMAINING','state':'ACTUAL_LIVE_CONTEXT_OBSERVED; OUTPUT_NOT_RECEIVED_HERE'}],
      'interface_register':'atomic-and-interface-denominator.json#/interface_artifacts',
      'global_or_full_domain_pass_signed_by_this_auditor':False,'update_started':False})

plan=load(ENTRIES[295]); reserved=set(plan['parent_reserved_not_started_jobs']); next_jobs=[]
for job in plan['jobs']:
    if job['id'] not in reserved:
        continue
    prompt=BASE/job['prompt']; readset=BASE/job['readset']; rs=json.loads(readset.read_text())
    next_jobs.append(dict(job, prompt_identity=identity(prompt), readset_identity=identity(readset),
                         complete_existing_prompt=prompt.read_text(),
                         fixed_complete_readset=rs,
                         dispatch_qualification='EXISTING_PARENT_RESERVED_PLAN; NOT_STARTED_BY_THIS_AUDITOR; SOURCE_ALREADY_READ_ELSEWHERE_MAY_BE_RECEIVED_WITH_EXACT_ACTUAL_CREDIT_NO_ROLE_RENAME',
                         required_completion='Full actual remaining reading, real atomic decomposition, exact premise and all consumer receptions; preserve all current valid scope; no global selfPASS; NOT_EXECUTED/UPDATE_NOT_STARTED unless actually authorized and observed otherwise'))
dump('next-dispatch.json',{'schema':'gr8-incremental-next-dispatch/v1','utc':NOW,
      'automatic_spawn_or_update_started':False,'existing_parent_reserved_count':len(next_jobs),
      'existing_parent_reserved_jobs':next_jobs,
      'auditor_remaining_reception':{'task':'Continue actual coverage audit of all not-full-read frozen payloads',
             'exclusive_write_set':'tasks/coverage_acceptance_incremental/',
             'complete_contract':'delegation/prompts/coverage-incremental-v2.md',
             'exact_input_register':'reading-ledger.json#/snapshot_payloads',
             'remaining_unique_sha':len(unread_shas),'remaining_unique_bytes':sum(sha_size[s] for s in unread_shas),
             'requirements':'Actually read all current semantic records/ledgers and full selected source/premise/consumer proofs, use exact JSON structures/continuous text ranges, mark truly administrative identities with exact reasons, retain incomplete available text as pending; do not convert machine unions or report reading to semantic approval.'},
      'separate_reception_jobs':[
          {'task':'KERNEL_ATOMIC_CONSUMER_RECEPTION','write_set':'tasks/kernel_atomic_reception/','inputs':['tasks/kernel_review/clause-source-premise-matrix.json','tasks/kernel_review/file-unit-fact-consumer-spec-matrix.json','tasks/kernel_review/consumer-census.json'],'complete_remaining_locators':'atomic-and-interface-denominator.json#/old_locator_rows','scope':'All2219locators/all135facts; manual children, precise premises,714lexicalcandidates to real consumers plus actual discovered consumers; receive actual PBS/domain facts; not all source reread automatically'},
          {'task':'CORE_ATOMIC_CONSUMER_RECEPTION','write_set':'tasks/core_atomic_reception/','inputs':['tasks/combat_review/clause-to-source.json','tasks/combat_review/source-to-spec.json'],'scope':'All994locators/63facts and currentBattler/Move/AbilityItem/AI/Facility/UI/CRE final consumers; actual stage/alias/failureprefix; fullsource reads not allformal approval'},
          {'task':'CRE_A_ATOMIC_CONSUMER_RECEPTION','write_set':'tasks/creature_a_atomic_reception/','inputs':['tasks/creature_review/reverse-matrix.pending.json','tasks/creature_review/facts-and-claims.json','tasks/creature_review/cross-domain-reception.json'],'scope':'All1430locators/102facts;100emptyconsumerrecords; actual complete premises and consumers or explicit no-defaultcaller disposition; C/D/Ewholeformal remain respective17reservedtasks'},
          {'task':'LATE_DELTA_RECEPTION','write_set':'tasks/coverage_acceptance_incremental/','scope':'Freeze exact newWRR/WORLD receipt, Ruby/zlib20907 and16YARB programs,UI003 andworldcatalog output; actual full meaningful content reading before any acceptance; do not backdate capturedUTC'}],
      'live_capacity_observed':7,'actual_context_cumulative_parent_reported':34,
      'not_started_plan_count_is_not_context_count':True})

gaps=[
    {'id':'COV-AUDITOR-READSET-INCOMPLETE','category':'AVAILABLE_UNREAD_AUDIT_INPUT','status':'OPEN','unique_sha':len(unread_shas),'bytes':sum(sha_size[s] for s in unread_shas),'exact_entries':'reading-ledger.json#/snapshot_payloads','not_material_or_host_limit':True},
    {'id':'COV-CURRENT-ACTUAL-READ-TOTAL-UNVERIFIED','category':'QUALIFICATION_NOT_YET_FULLY_RECEIVED','status':'OPEN','mechanical_declared_counts':coverage['counts'],'actual_global_full_partial_unread':'UNVERIFIED; all exact declared ranges and complements retained per563paths','why':'Full realI/O/EOF/truncation/fieldview/raw/association qualifications across allledgers have not been personally received','not_material_or_host_limit':True},
    {'id':'COV-GLOBAL-ATOMIC-INTERFACE-UNFROZEN','status':'OPEN','scope':'All87WP/131formal/R432/currenteffectiveB8supplements; manual partialdomains differ and overlap','exact_units':'atomic-and-interface-denominator.json','accepted_total':'UNVERIFIED_NOT_ZERO_ASSERTED','not_material_or_host_limit':True},
    {'id':'COV-KERNEL-2219','status':'OPEN','locators':2219,'no_local_fact_link':771,'facts':135,'generic_identical_premise_facts':135,'not_closed_by_new_domain_source_full_reads':True},
    {'id':'COV-CORE-994','status':'OPEN','locators':994,'no_local_fact_link':165,'facts':63,'generic_premise_rows':994,'not_closed_by_new_domain_source_full_reads':True},
    {'id':'COV-CRE-1430','status':'OPEN','locators':1430,'no_local_fact_link':1307,'facts':102,'facts_with_empty_consumer':100,'manual_decomposition_pending':1430},
    {'id':'COV-EOF-FROZEN-WRR','status':'FROZEN_RANGE_DEFECT_LATE_CORRECTION_REPORTED_UNRECEIVED','path':'Data/Scripts/001_Technical/002_RubyUtilities.rb','snapshot':ENTRIES[280]['snapshot'],'pointer':'/files/45','declared':[390,410],'actual_EOF':406,'effective_declared_clipped_credit':[390,406],'late_root_report':'Correction410requested/406actual; originalfrozenv1retained','not_a_business_finding':True},
    {'id':'COV-PARENT17','status':'NOT_STARTED_RESERVED','jobs':sorted(reserved),'not_material_or_host_limit':True},
    {'id':'COV-LATE-DELTAS','status':'OPEN_ACTUAL_RECEPTION_REQUIRED','items':['UI003','WRR_final_WORLD_received','Ruby_zlib20907_16YARB','world_catalog_remaining']},
    {'id':'COV-ROOT21-CLASSIFICATION-CONTENT-RECEPTION','status':'OPEN_FOR_THIS_AUDITOR','counts':root['bounded_counts'],'scope':'Each exact originalcompleteproposal, actualnonproposer content, rootrestriction/alias/historyqualifier; no revision of accepted local classification without evidence'},
    {'id':'COV-PUBLICATION','status':'PUSH_CONFIRMED_REMOTE_READBACK_PENDING_AS_LAST_PARENT_MESSAGE','commit':'cab9deade98ff3038f4d8002531958fd74bd5fbd','initial_push':'503failure then normalpushreportedexit0; not a content/material limit'},
    {'id':'COV-TRUE-MATERIAL-HOST-BOUNDARIES','status':'BOUNDED_REPORTED_NOT_REESTABLISHED_FULLY_HERE','missing_material':'Parent reports onlyZIP DNS retrieval missing; complete maps/Graphics/Audio/native host material distinctions remain originalpreciseL01–L14','qualification':'Cannot classify available PBS/controller/text/YARB/font/SF2/messages/formal/ledgers as missinghost; opaque nativeCFG and actualhost results are separate.'}
]
dump('coverage-gaps.json',{'schema':'gr8-incremental-coverage-gaps/v1','utc':NOW,'conclusion':'INCOMPLETE_NO_PASS; AUDIT_ITSELF_INCOMPLETE','gaps':gaps,
      'exact_per_path_declared_unread':'file-coverage.json#/files','global_actual_semantic_unread_count':'UNVERIFIED_NOT_ZERO',
      'global_current_semantic_unreceived_count':'UNVERIFIED_NOT_ZERO','update_started':False})

identities=json.loads((OUT/'input-identities.json').read_text())
identities.update({'publication_status':'PUSH_CONFIRMED_REMOTE_READBACK_PENDING_AS_LAST_PARENT_MESSAGE',
                   'fixed_tree_verification':identity_check,
                   'contracts':[identity(BASE/'inputs/eighth-global-review-prompt.md'),identity(PROJECT/'AGENTS.md'),identity(BASE/'inputs/review-SKILL.md')],
                   'supplemental_inputs':supplemental,'cab9_workspace_tree':'4bee3e4983fc90ee8ad40bc6557af6c5dbdd1188'})
dump('input-identities.json',identities)
dump('execution-records.json',{'schema':'gr8-incremental-execution-integrity/v1','utc':NOW,
     'business_execution':'NOT_EXECUTED','new_reference_business_runs':0,'new_model_business_runs':0,
     'target_programs_executed':False,'install_commit_push_spawn_by_auditor':False,
     'fixed_tree_tool_records':identity_check,
     'captured_tool_receipts':sorted(p.name for p in OUT.glob('*.receipt.json')),
     'known_failed_tool_call':{'tool_chunk':'395b2e','exit_code':1,'command':'wc -l -c adjudication/root-binary-bounded-receptions.json adjudication/root-ui002-reception.json adjudication/root-ui003-reception.json','reason':'Third guessed supplementalfilename absent; firsttwoexistingcountsreturned; not originalinputmissing','utc':'UNVERIFIED_NO_TOOL_UTC_ECHO','original_output':'Private platform tool stream; no fabricated publicstderr'},
     'truncation_history':'Initial concatenatedprompt/readset outputs truncated; completeprompt1–120/121–241 andreadset0–49/50–99/100–149/150–199/200–244/245–300 fields subsequently actually read. Truncated payload output itself not granted full credit.',
     'early_tool_IO_boundary':'Some early shellstdout/stderr/UTC only in platformtool stream. No fullpublicrawIO export and no backfilled timestamps claimed.',
     'update_started':False})
dump('progress.json',{'schema':'gr8-incremental-coverage-progress/v1','updated_utc':NOW,
     'task':'/root/coverage_acceptance_incremental','process':'RUNNING_WHEN_RECORD_WRITTEN',
     'deliverable_state':'PARTIAL_AUDIT_OUTPUTS; COMPLETE_CONTRACT_REMAINS_OPEN',
     'conclusion':'INCOMPLETE_NO_PASS','all301_identity_verified':True,
     'snapshot_unique_sha':289,'snapshot_original_paths':301,'snapshot_original_path_bytes':118161094,
     'personally_full_read_frozen_artifacts':len(FULL),'samebyte_contract_links':2,
     'pending_unique_sha':len(unread_shas),'pending_unique_bytes':sum(sha_size[s] for s in unread_shas),
     'personally_full_read_reports':13,'full_interface_artifacts':5,'interface_records':41,
     'own_R_full_source_reads':0,'own_F_full_source_reads':0,
     'mechanical_declared_line_domain_union_counts':coverage['counts'],
     'actual_current_global_reading_counts':'UNVERIFIED_PENDING_FULL_LEDGER_IO_RECEPTION',
     'actual_current_global_semantic_acceptance_counts':'UNVERIFIED_PENDING_ATOMIC_AND_ALL_CONSUMER_RECEPTION',
     'actual_configuration':{key:'UNVERIFIED' for key in ['model','effort','tier','speed','Fast','opaque_platform_id']},
     'requested_configuration':DATA['requested'],'live_contexts_observed':7,
     'cumulative_actual_contexts_parent_reported':34,'new_contexts_created_by_this_auditor':0,
     'actual_independence_increment_for_this_new_context':1,
     'publication':'PUSH_CONFIRMED_REMOTE_READBACK_PENDING_AS_LAST_PARENT_MESSAGE',
     'behavior_execution':'NOT_EXECUTED','update_started':False,'marker':'UPDATE_NOT_STARTED'})
print(json.dumps({'identity_mismatches':{r['repo']:r['mismatches'] for r in identity_check},
                   'full_snapshot_artifact_reads':len(FULL),'pending_unique_sha':len(unread_shas),
                   'pending_unique_bytes':sum(sha_size[s] for s in unread_shas),
                   'old_pending_locator_rows':len(old_locators),'all_wp_inventory_rows':len(wp_inventory),
                   'interface_artifacts_preserved':len(interface_register),'reserved_jobs':len(next_jobs),
                   'global_pass':False},ensure_ascii=False,indent=2))
