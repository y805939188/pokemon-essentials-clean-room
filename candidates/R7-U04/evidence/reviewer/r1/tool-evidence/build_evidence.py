"""Serialize this reviewer's recorded static conclusions and exact cited byte spans."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil

TOOLS = Path(__file__).resolve().parent
OUT = TOOLS.parent
CONTEXT = Path('/workspace/r7-context/R7-U04-reviewer')
BOOT = Path('/workspace/r7-bootstrap/R7-U04-reviewer')
FREEZE = Path('/workspace/r7-review-bootstrap/R7-U04')
CR = Path('/workspace/r7-review-input/R7-U04-242e1f9fb2fbdf7d609bcdb6de0a95547f9f4c6a')
PREFIX = 'candidates/R7-U04/'
BASE = 'deliverables/final-specification-set/'
WP39 = PREFIX+BASE+'combat-requirements/wp39-battle-context-and-participants.md'
WP41 = PREFIX+BASE+'combat-requirements/wp41-switching-positioning-and-escape.md'
CAT = PREFIX+BASE+'test-catalog/combat-requirements-wp39-40-41-42-45.md'


def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())


def write(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


def anchor(path, first, last=None):
    data=(CR/'candidate'/path).read_bytes()
    lines=data.splitlines(keepends=True)
    last=first if last is None else last
    lo=sum(map(len,lines[:first-1]));hi=sum(map(len,lines[:last]))
    return dict(commit='242e1f9fb2fbdf7d609bcdb6de0a95547f9f4c6a',path=path,
                lines_inclusive=[first,last],byte_offsets_half_open=[lo,hi],
                file_identity=identity(data),span_identity=identity(data[lo:hi]))


now=datetime.datetime.now(datetime.timezone.utc).isoformat()
freeze=json.loads((FREEZE/'candidate-input.json').read_bytes())
contract=json.loads((BOOT/'dispatch/delegation/contracts/R7-U04.json').read_bytes())
audit=json.loads((TOOLS/'input-audit.json').read_bytes())
thread=os.environ.get('CODEX_THREAD_ID','NOT_EXPOSED_UNVERIFIED')
assert thread=='01a13f7e-d577-727a-9565-f64f6a663024'
assert thread!=freeze['author_task_id']
assert audit['status']=='BYTES_SCOPE_BINDINGS_VERIFIED'
for root,target in [(CONTEXT,'source-recovery-receipt.json'),(CR,'candidate-recovery-receipt.json')]:
    receipts=list(root.glob('recovery-receipt-*.json'))
    assert len(receipts)==1
    shutil.copyfile(receipts[0],TOOLS/target)
shutil.copyfile(FREEZE/'candidate-input.json',TOOLS/'frozen-candidate-input.json')

configuration=dict(requested=dict(model='gpt-6.1-sol',reasoning_effort='ultra',service_tier='default',speed='ordinary',Fast='forbidden'),effective=dict(model='UNVERIFIED',reasoning_effort='UNVERIFIED',service_tier='UNVERIFIED',speed='UNVERIFIED'),qualification='No effective backend configuration response is exposed. Environment/PID/argv/exit do not authenticate it.')
unmet=[
    'R7-I reception of this independently authored review result',
    'R7-I clause-level integration and shared-consumer reception of actual cumulative bytes',
    'New different-context R7-IR review of actual integrated commit/tree',
    'Exact direct/transitive dependencies, historical regressions, and R7-I formal acceptance/closure decisions'
]
execution=dict(SOURCE_STATIC='PERFORMED_WITH_NAMED_RANGES',DERIVED_VECTOR='PAPER_REVIEW_ONLY',TOOL_VALIDATION='BYTES_SCOPE_BINDINGS_ONLY',REFERENCE_OBSERVATION='NO_NEW_OBSERVATION',behavior_vectors='NOT_EXECUTED',reference_execution=0,independent_full_behavior_model_execution=0,UI=0,host=0,Demo=0,native_media=0,real_save_replay=0)
binding=dict(dispatch_commit='6ec1d09e9c470954964d72761c83a760ef4f0364',dispatch_tree='15f3c40eb9733d04be228b47c6ea52e33c6123b7',freeze_commit='f76135fdc8b626de1dabdecf5288fc926b04e7ac',freeze_tree='65b3ef0352b10f638ba9867414b2bc68f5a2ae80',candidate_commit=freeze['candidate_commit'],candidate_tree=freeze['candidate_tree'],B=freeze['fixed_B'],B_root_tree=freeze['fixed_B_tree'],B_formal_tree='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c',R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',R_tree_expected='7589c800b61ba13a13040ed0d686979b80a84fd0',R_whole_tree_verified=False,contract=freeze['original_contract_commit_path_identity'])
write(OUT/'review-input-receipt.json',dict(
    schema='r7.u04.r1.review-input-receipt.v1',created_utc=now,batch_id='R7-U04',required_ids=freeze['required_ids'],input_binding=binding,
    actual_reviewer_thread_id=thread,reviewer_thread_provenance='CODEX_THREAD_ID observed by actual exec_command Python environment; independent external thread from supplied author task',
    actual_separate_reviewer_task_id='NOT_EXPOSED_UNVERIFIED',reviewer_environment='ccarenv_b64_Y2NhcmVudl9hYWRhNjdlZjU1MDA4MTkxODM3NmM3YWE2NzNiNmUzMw',
    parent_source_thread_id='01a13f49-a154-7054-9b04-ce31f924d01c',author_external_task_id=freeze['author_task_id'],
    author_internal_context=freeze['author_context_and_qualification'],author_environment_as_recorded='ccarenv_b64_Y2NhcmVudl9hNzFjMDc4ODhlODA4MTkxOWY4Y2Q4NTUwZWNhZWQ0Mg',
    independence='DISTINCT_VISIBLE_REVIEWER_THREAD_AND_ENVIRONMENT; author internal-to-external match remains unverified',configuration=configuration,
    input_reception_complete=True,actual_frozen_files=audit['candidate_files'],original_recovery=dict(files=29,bytes=5789300,receipt='tool-evidence/source-recovery-receipt.json'),
    candidate_recovery=dict(files=17,bytes=285560,receipt='tool-evidence/candidate-recovery-receipt.json'),supplemental_reference='tool-evidence/supplemental-source-receipt.json',
    independent_audit='tool-evidence/input-audit.json',source_snapshot_qualification='Selected immutable files, not whole project/reference checkout; restored candidates chmod444 and read-only in this workflow',
    skills=dict(B_and_dispatch_git_tree='No .agents paths',workspace_agents='Empty',project_agents_skills='Absent',applied_project_skills=[]),
    initial_commands=dict(qualification='Initial reads/fetch/recovery have real platform tool I/O but were not timestamp-wrapped; no invented initial stdout/stderr files',observed_chunks=['39cc23','51e1cb','498610','e29bdc','af2cbc','0e624f']),
    execution=execution,L01_L14='RETAINED',old_56_92='UNCHANGED',denominator=dict(issues=27,batches=13),child_tasks_created=0,
    output_branch='codex/r7-u04-reviewer-20261015-r1',clean_output_checkout_base=freeze['fixed_B'],output_checkout='/workspace/r7-u04-reviewer-checkout',
    input_or_independence_blockers=[],unmet_later_dependencies=unmet,actual_integrated_PASS=False,formal_ACCEPTED=False,CLOSED=False))

ledger=[]
for record in contract['original_full_contracts']:
    for row in record['complete_seven_groups']['六_依赖接收_精确读写集']['读取义务']['items']:
        ledger.append(dict(record_id=record['record_id'],path=row['path'],identity_id=row['identity_id'],scope=row['scope'],qualification='Static semantic read of this exact contract range; complete mirror reading paired with B unchanged blocks and original replaced lines. No whole-source read inferred.'))
ledger.extend([
    dict(path='Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',additional_ranges_inclusive=[[1,141],[286,315],[438,467]],commit=binding['R']),
    dict(path='Data/Scripts/011_Battle/002_Battler/002_Battler_Initialize.rb',additional_ranges_inclusive=[[60,310]],commit=binding['R'],identity=json.loads((TOOLS/'supplemental-source-receipt.json').read_bytes())),
    dict(path='Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',additional_ranges_inclusive=[[686,748]],commit=binding['R']),
    dict(path='Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb',additional_ranges_inclusive=[[192,202],[260,313]],commit=binding['R']),
    dict(path=BASE+'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md',additional_ranges_inclusive=[[100,148],[244,285]],commit=binding['B'])
])
# Additional source lines 311-315 were printed with the original source-range read,
# and its coverage is recorded conservatively below rather than inferred from a hash.
ledger[-5]['additional_ranges_inclusive']=[[1,141],[286,315],[438,467]]
write(TOOLS/'reading-ledger.json',dict(schema='r7.u04.r1.reading-ledger.v1',reader_thread=thread,full_dispatch_and_seven_groups=True,
    documents_fully_read=[WP39,WP41,CAT],B_read_method='All mirror text was read. Every identical B block is matched; all B replaced lines read in full diffs. This is complete B-target text coverage without implying every unrelated B file was read.',
    evidence_read=dict(M01='Full 17baa363...raw',M02='Full 3b76e268...raw',root_raw='/records/1 and /records/2 of e0c5ebb2...raw',normalized='/records/1 and /records/2 verification/dependencies/revision/stages/retained_contract',limits='Full L01-L14',author='All17 files received; three mirrors, report/per-id/reading/context/logs/scripts read; metadata/receipts/manifests independently compared'),
    reads=ledger,negative_evidence='Finite named ranges only; search is location evidence. No semantic whole-reference, full Battle/Battler-subtree, or global caller-absence claim.',
    execution='NOT_EXECUTED',qualification='This ledger records completed reviewer reading; it is not a reference runtime transcript.'))

sw_reasons=[
    ('SW-30',112,'Legal 2v1 retained at setup; sole able reserve prevents entry loss. Raw100>50 makes during-replacement escape deterministic; the existing scan continues. Binding swaps indices2/1; heal60→120 precedes one-layer15 damage to105. No further reserve or result producer; outer EOR sees3 after normal return.'),
    ('SW-31',113,'Only one fainted seat and no switch in the pass: no second prompt, no entry collection, no binding/heal/hazard for reserveP; success leaves3.'),
    ('SW-32',114,'First Yes binds reserveP to0 without invoking escape. Sole reserve now active, so seat2 has no legal non-active replacement; nonlethal fixture leaves0.'),
    ('SW-33',115,'Ordinary replacement entry with positive decision returns before judge/scan. Distinguish pre-existing positive decision from one written during scan.'),
    ('SW-34',116,'Replacement selection uses default non-cancellable route; cancel input repeats chooser. No already reached escape feedback or decision is rolled back.'),
    ('SW-35',117,'Separate faults before binding, after binding/order, and during entry retain only actual reached prefixes. No guarantee of unperformed steps, rollback, final3 or host success; WP42 diagnosis/propagation boundary retained.')
]
bc_reasons=[
    ('BC-26',34,'For1v3 order[3,5,1], first existing fainted3 breaks preferred traversal; fallback restarts at3. The read-only query writes nothing; result is3, not filtered5.'),
    ('BC-27',35,'Same query with3 living returns3 immediately; this positive control does not prove a universal living guarantee.'),
    ('BC-28',36,'Absent3 is skipped and living5 is first existing member; absence is distinct from existing fainted state.'),
    ('BC-29',37,'Own-side0 direct wild throw uses raw3 then its living-allies list. Global ordering filters out fainted3 and selects1 before5. Capture calculation receives1; no capture success/failure or ordinary-menu reachability is claimed.'),
    ('BC-30',38,'Explicit opposing5 is used directly and remains living; own-side helper is bypassed. Normal menu and independent permission remain preserved.'),
    ('BC-31',39,'No living ally yields empty fallback; subsequent state query fails before no-target message. This is the existing WP38 boundary, not a new mandatory finding or refund/rollback promise.')
]


def vectors(rows):
    result=[]
    for name,line,reason in rows:
        text=(CR/'candidate'/CAT).read_text().splitlines()[line-1]
        cells=text.split('|')
        assert cells[1].strip()==name
        result.append(dict(id=name,verdict='PASS_SCOPED_CANDIDATE',candidate_anchor=anchor(CAT,line),premise=cells[2].strip(),authored_expected=cells[3].strip(),independent_reason=reason,review_phase='SOURCE_STATIC_AND_PAPER_DERIVATION',execution='NOT_EXECUTED'))
    return result


common=dict(configuration=configuration,execution=execution,input_binding=binding,actual_reviewer_thread_id=thread,
            input_or_independence_blockers=[],unmet_later_dependencies=unmet,formal_ACCEPTED=False,CLOSED=False,actual_integrated_PASS=False,
            old_global_PASS_used=False,L01_L14='RETAINED',conditional_paths_used=[],source_defect_compatibility_policy='User decision remains separate; no permanent anomalous implementation requirement')
records=[dict(common,id='GR7-M03-001',verdict='PASS_SCOPED_CANDIDATE',required_revisions=[],
    candidate_clauses=[anchor(WP41,123),anchor(WP41,127,128),anchor(WP41,237)],
    original_nonauthor=dict(reviewer='R7-M01',binding='p02-64f59f549be82df4101e',minimum='Nonlethal continuation/state commit after decision3 only; retain WP42 generic non-immediate consumption',lethal_extension='NOT_ADOPTED'),
    criteria=[
        dict(condition='Only minimum scoped body/catalog correction',result='PASS',reason='Only WP41 clause/count and SW30–35 additions; no other formal target, optional or policy contribution.'),
        dict(condition='Normal fixture and three controls',result='PASS',reason='Full legal2v1 with raw-speed, sole reserve, normal callbacks; independent single-faint/firstYes/entry-positive controls recorded and supported.'),
        dict(condition='Cancellation, exception and partial commit separately',result='PASS',reason='No invokes escape; later forced selection cannot return by cancelling; faults retain reached decision/binding/order/position/HP prefixes only.'),
        dict(condition='Preserve correct context and historical regressions',result='PASS',reason='WP42 atB lines51/135 and phases21/22 unchanged. Old SW/R/E rows remain; no old certificate adopted.'),
        dict(condition='Actual nonauthor result review and truthful phases',result='PASS',reason='This distinct visible thread reviewed frozen bytes; all domain vectors remain NOT_EXECUTED and effective configuration remains UNVERIFIED.')],
    normal_path='SW30 only in the stated nonlethal normal-return fixture; no blanket final3',cancellation='SW34 mandatory chooser policy only',
    failure='SW35 distinct actual reached fault prefixes; WP42 diagnostic scope preserved',partial_commit='Feedback/decision/binding/order/flags/HP commit at separate reached points; no transaction rollback',
    vectors=vectors(sw_reasons),preserved_scopes=['one fainted seat may have no second prompt','ordinary entry-positive early return','firstYes does not write escape3','WP42 generic delayed consumption','no lethal-result extension','no future permanent-defect policy'],
    source_consumers=['Battle182–209,329–350','StartAndEnd16–104,322–347,557–568','ActionRunning60–160','BattlerChangeSelf64–99','BattlerInitialize60–310','ActionSwitching1–467','SceneChooseCommands141–191','EndOfRound686–748']),
    dict(common,id='GR7-M03-002',verdict='PASS_SCOPED_CANDIDATE',required_revisions=[],
    candidate_clauses=[anchor(WP39,190),anchor(WP39,322)],
    original_nonauthor=dict(reviewer='R7-M02',binding='p02-7c5bfd2d8a1dc5f59b7a',minimum='Preference/fallback raw query precision; recovered capture target, preserve WP38 and explicit-menu route',broader_capture_failure='REFUTED_AND_NOT_ADOPTED'),
    criteria=[
        dict(condition='Preference instead of guarantee, first-existing-fainted exception',result='PASS',reason='WP39 actual line190 states preference and exception without rewriting opposition order or other helpers.'),
        dict(condition='Query true normal/fainted/absent controls',result='PASS',reason='BC26→3, BC27→3, BC28→5 on separate stable-input premises.'),
        dict(condition='Actual capture rescue and explicit target',result='PASS',reason='BC29 global living-allies ordering yields1, not5; BC30 explicit5 bypasses helper; no normal-menu entitlement or capture-failure claim.'),
        dict(condition='Cancellation/failure/partial commit and preserved consumers',result='PASS',reason='Query readonly/no interaction; BC31 existing empty-fallback failure retained; later capture writes/consumption/cancellation remain WP38. False/default callers and WP47-A family targeting unchanged.'),
        dict(condition='Actual nonauthor result review and truthful phases',result='PASS',reason='This distinct visible thread reviewed frozen bytes against M02 and named R consumers. No author self-review or hash exit substituted for semantic reasoning.')],
    normal_path='BC26–30 stable1v3 input, actual recovery target vs raw query kept separate',cancellation='No query interaction; later capture cancellation remainsWP38',
    failure='BC31 retains existing WP38 empty fallback exception before no-target message; no broad capture-failure claim',partial_commit='Raw query writes no HP/party/choice; later capture writes acquire no new rollback guarantee',
    vectors=vectors(bc_reasons),preserved_scopes=['WP38 living ally fallback','WP38 existing no-live failure','explicit opponent5 route','SleepTalk/Imposter/switch messages false/default','WP47-A independent construction/fallback','no permanent anomaly policy'],
    source_consumers=['Battler720–777','Battle440–555','CatchAndStore90–165','ActionSwitching235–275','MoveChangeMoveEffect1170–1206','AbilityEffects2824–2850','SceneChooseCommands290–310'])]
write(OUT/'per-id.json',dict(schema='r7.u04.r1.independent-per-id.v1',batch_id='R7-U04',records=records,findings_requiring_revision=[],qualification='Human/model static content assessment, independently authored here; no runtime assertion or formal acceptance'))
print(json.dumps(dict(status='REVIEW_RECORDS_SERIALIZED',actual_reviewer_thread_id=thread,verdicts={r['id']:r['verdict'] for r in records},domain_execution='NOT_EXECUTED',created_utc=now),ensure_ascii=False))
