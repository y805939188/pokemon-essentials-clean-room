"""Package this review's actual receipts and explicitly scoped human/model judgments."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

OUT=Path(__file__).resolve().parents[1]
REPO=OUT.parents[4]
BOOT=Path('/workspace/r7-review-bootstrap/R7-U03-r2')
CTX=Path('/workspace/r7-context/R7-U03-reviewer')
INPUT=Path('/workspace/r7-review-input/R7-U03-r2-11bff8e7912a98de09691ad7d7b7a2d3194e2757')
B='e646432c644dec04d306842cc5a559a29c718fbc'
C='11bff8e7912a98de09691ad7d7b7a2d3194e2757'
T='b12b63cd5f19b4d550aae3548a618bf10416e56f'

def load(p):return json.loads(p.read_bytes())
def identity(d):return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest())
def dump(name,value):(OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

audit=load(OUT/'input-byte-audit.json')
provenance=load(OUT/'provenance-audit.json')
document=load(OUT/'document-audit.json')
freeze=load(BOOT/'candidate-input.json')
thread=os.environ['CODEX_THREAD_ID']
assert thread=='01a1401b-538b-764d-b23c-eafd6825c025'
evidence=OUT/'input-evidence';evidence.mkdir(exist_ok=True)
copies={
 'dispatch.md':Path('/workspace/r7-bootstrap/R7-U03-reviewer/reviewer-dispatch.md'),
 'original-recovery-plan.json':Path('/workspace/r7-bootstrap/R7-U03-reviewer/recovery/batches/R7-U03.json'),
 'recovery-tool.py':Path('/workspace/r7-bootstrap/R7-U03-reviewer/tools/restore_container_context.py'),
 'candidate-restore-plan.json':BOOT/'candidate-restore/R7-U03.json',
 'candidate-input.json':BOOT/'candidate-input.json',
 'frozen-root-readback.json':BOOT/'remote-readback.json',
 'original-recovery-receipt.json':next(CTX.glob('recovery-receipt-*.json')),
 'candidate-recovery-receipt.json':next(INPUT.glob('recovery-receipt-*.json')),
 'L01-L14.json':CTX/'evidence/tasks/R7-C17/limits-and-alias-reception.json',
}
for name,p in copies.items():shutil.copyfile(p,evidence/name)
for name in ['original-restore.stdout','original-restore.stderr','candidate-restore.stdout','candidate-restore.stderr']:
    shutil.copyfile(Path('/workspace/r7-local-logs/R7-U03-r2')/name,evidence/name)

configuration=dict(requested=dict(model='gpt-6.1-sol',reasoning_effort='ultra',service_tier='default',speed='normal; Fast forbidden'),effective={k:'UNVERIFIED' for k in ['model','reasoning_effort','service_tier','speed']},qualification='Contract request only; no authoritative effective return; PID is not model authentication')
execution=dict(SOURCE_STATIC='current independent file/clause reasoning',DERIVED_VECTOR='paper expectations only',TOOL_VALIDATION='hash/membership/scope/link/remote byte checks only',behavior_vectors='NOT_EXECUTED',reference_observation=0,independent_full_model=0,game_host=0,Demo=0,native_media=0,real_save_replay=0)
independence=dict(actual_reviewer_thread_id=thread,actual_session_id=os.environ.get('CODEX_SESSION_ID'),actual_environment_id='ccarenv_b64_Y2NhcmVudl8xZThmYjJhZTliOTg4MTkxYWY4NGNmMzBhM2E5NzI2YQ',caas_session_id=os.environ.get('CODEX_CAAS_SESSION_ID'),source_parent_external_id='01a13f49-a154-7054-9b04-ce31f924d01c',author_external_task_id=freeze['author_task_id'],author_internal_task_context='NOT_EXPOSED; original author qualification retained',prior_r1_reviewer_thread='01a13ff0-363e-7412-826d-e4a795522002',distinct_exposed_identifiers=True,child_AI_tasks_created_before_dispatch_read=0,child_AI_tasks_created_total=0,additional_model_calls=0,model_PID='NOT_EXPOSED',tool_packaging_PID=os.getpid())
unmet=['R7-I exact clause/shared/consumer reception and serial integration','Fresh different-context R7-IR on actual cumulative integrated commit/tree','Final direct/transitive dependency and exact historical-regression reception','Formal acceptance/closure by authorized R7-I only']
filemap={r['path']:r for r in audit['candidate']}
prefix='candidates/R7-U03/deliverables/final-specification-set/'
paths05=[prefix+p for p in ['engine-overworld/wp12-terrain-movement-vehicles.md','pokemon-rules/wp61-field-passive-effects-and-blackout.md','test-catalog/engine-overworld-wp11-15-59-60.md','test-catalog/pokemon-rules-wp53-60-61-62-69-70.md']]
paths06=[prefix+'test-catalog/engine-overworld-wp16.md']
notes05=[
 ('01','Full legal ordinary-ground fixture; creation B+1 with unchanged position/distance, 0/0/2 counters; qualified completion 1/1/1. Empty day-care cycle may advance; friendship count is not numerical happiness gain.'),
 ('02','Passable-only control commits position/distance at start; completion-side counters remain distinct.'),
 ('03','Precompletion preserves creation prefix without player counters.'),
 ('04','Successful legal touch with no old motion creates no new collision chain; event consequences separate.'),
 ('05','Direct diagonal fixed-segment failure may retain direction change, with no collision timer/count/completion.'),
 ('06','Legal nonskippable nonrepeat [right, WAIT20, end]; forcing explicitly retained through completion. Motion advances MR02; WAIT is not dispatched while moving. Two general notifications, no global/player/Repel advance.'),
 ('07','Separate injected write-before-failure premises: first general consumer fails after motion clear => 0/0/2; first player consumer fails after global commit => 1/0/2. No later effects/rollback/host-resume guarantee.'),
 ('08','No more qualified completion updates => actual creation prefix only, no added cancel API or unconditional eventual completion.')]
notes06=[('WR01','Actual display 320→448, y fixed; independently quantized 80→112 gives same-tile projection -32, valid normal drawing and no zoom/other camera writes.'),('R7-CAM01','Small 10×8 SnapEdges map clamps display to 0 despite player move; no new right region required.'),('R7-CAM02','Centered 30×20 unclamped/no-old-task player move supports actual 320→448 display change.'),('R7-CAM03','Right edge upper bound1792 stays fixed as player21→22; normal dual state.'),('R7-CAM04','Valid live scroll speed4/right1 at T+0.1: total0.2, display384/projection-16; follow gate suppresses addition during live scroll only.')]

records=[dict(id='GR7-M05-001',priority='P2',verdict='PASS_SCOPED_CANDIDATE',candidate_commit=C,candidate_tree=T,candidate_files=[filemap[p] for p in paths05],minimum_rule_review='Separate zero-displacement collision creation from normal qualified completion; no displacement gate added to player counters.',vectors=[dict(ids=['R7-BP'+n,'R7-FP'+n],assessment=s,content_review='SATISFIES_SCOPED_CONTRACT',execution='NOT_EXECUTED') for n,s in notes05],original_C04_map={'C04-BP-A':['R7-BP01','R7-BP03'],'C04-BP-B':['R7-BP02'],'C04-BP-C':['R7-BP04','R7-BP05'],'C04-BP-D':['R7-BP06'],'C04-BP-E':['R7-BP07','R7-BP08']},conditional_sync=dict(WP06_adopted=False,reason='Existing guard/count/distance contract correct; no concrete contradiction. No extra clock-kernel requirement.'),preserved=['ordinary movement start vs completion','forced/interpreter/automatic-motion/consumer guards','touch/diagonal/ledge/encounter distinctions','nonplayer blocked movement has no new player bump timer','MR02 motion-state route advancement and legal WAIT','default poison off; empty day-care cycle; consumer order and gates','no rollback, default fault or future compatibility policy'],current_input_blockers=[],unmet_later_gates=unmet),
 dict(id='GR7-M06-001',priority='P3',verdict='PASS_SCOPED_CANDIDATE',candidate_commit=C,candidate_tree=T,candidate_files=[filemap[p] for p in paths06],minimum_rule_review='WR01 display-input premise plus player-movement/camera-held reverse controls; WP16 body unchanged.',vectors=[dict(id=n,assessment=s,content_review='SATISFIES_SCOPED_CONTRACT',execution='NOT_EXECUTED') for n,s in notes06],original_C04_map={'C04-CAM-A':['R7-CAM01'],'C04-CAM-B':['R7-CAM02'],'C04-CAM-C':['R7-CAM03'],'C04-CAM-D':['R7-CAM04']},cancellation='Blocked/unmoved cases outside counterexample; existing movement rules retained',failure='Resource/update failure only supports reached prefixes',partial_commit='Player/camera independent state is normal, not transaction failure',preserved=['WP16 quantization/neighbors/durations/clamping/center rules','GR3-CAM06–08 and12/15–17; WR16','GR3-M03-001 WR01 residual relation; no new behavior root or ledger reopen','no pixel observation or object-reuse guarantee'],current_input_blockers=[],unmet_later_gates=unmet)]
dump('per-id.json',dict(schema='r7-u03-r2.independent-per-id.v1',reviewer=independence,freeze_commit='aa369555b0e8b6c8b077f964b54ed63d3b924f26',freeze_tree='08bd0f362c74ef7645b5bbd70b557489c122ae29',records=records,configuration=configuration,execution=execution,L01_L14='RETAINED',progress_denominator=dict(items=27,batches=13,changed=False),integrated_PASS=False,ACCEPTED=False,CLOSED=False,old_r1_process_qualification='WAIT_INPUT_OR_INDEPENDENCE retained, no waiver or PASS migration'))

commands=[]
author=INPUT/'candidate/candidates/R7-U03/evidence/author'
for p in sorted((author/'commands').glob('*.json')):
    commands.append(dict(path=str(p.relative_to(INPUT/'candidate')),identity=identity(p.read_bytes()),actual_record=load(p),qualification='Original author tool log only; not independent semantic or behavior-execution credit'))
dump('author-command-qualification.json',dict(commands=commands,configuration=load(author/'context-and-configuration.json'),qualification='All original failures/configuration/logging limits retained; no author program executed by r2'))

supplement=CTX/'supplement/proposal-successor-deltas-C04-C06.json'
fixed_files=[]
for p in [supplement,*[REPO/q for q in ['AGENTS.md','deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md','review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M03/spec-coverage.tsv']]]:
    fixed_files.append(dict(local_path=str(p),identity=identity(p.read_bytes()),qualification='Supplement identity and named read only; full historical coverage not asserted'))

dump('review-input-receipt.json',dict(schema='r7-u03-r2.review-input-receipt.v1',packaged_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer=independence,dispatch_commit='c64774c60d91e522cb515ef71e3e9d4ea6b4712c',dispatch_path='review/remediation-seventh-20261015-prepare/review-rechecks/R7-U03/r2/reviewer-dispatch.md',fixed_B=B,freeze_commit='aa369555b0e8b6c8b077f964b54ed63d3b924f26',freeze_tree='08bd0f362c74ef7645b5bbd70b557489c122ae29',candidate_commit=C,candidate_tree=T,freeze_review_round_field='r1 retained because r2 reviews same unchanged freeze',original_recovery=dict(files=34,bytes=6088763,receipt='input-evidence/original-recovery-receipt.json'),candidate_recovery=dict(files=84,bytes=774948,mirrors=5,author_evidence=79,receipt='input-evidence/candidate-recovery-receipt.json'),parent_byte_count_qualification='Original parent supplied84 files only;774948 is immutable Git/complete HTTP sum computed by root and independently rechecked here',candidate_files=audit['candidate'],actual_tree_mode_blob_match=True,complete_diff_against_B=audit['complete_diff_against_B'],raw_member_checks=dict(count=149,evidence='input-byte-audit.json'),author_manifest_nonself_checks=83,provenance_evidence='provenance-audit.json',named_extra_fixed_files=fixed_files,read_qualification='Original two full seven-group contracts, full nonauthor records and proposer records, current five complete mirrors/catalogs, actual B comparison and all changed clauses independently read. No old PASS inheritance; no full reference tree or historical corpus certification.',skills=dict(workspace_agents_empty=True,B_and_dispatch_agents_absent=True,evidence='provenance-audit.json'),configuration=configuration,execution=execution,initial_log_qualification='Initial platform tool I/O and genuine restoration receipts retained; no independently separated UTC/PID/stdout/stderr for each early reading or aborted unfiltered fetch/API request; no backfill. Later commands are genuinely wrapped.',retained_tool_failures=['input-byte-audit: target-row preservation assertion','input-byte-audit-final: JSON set serialization after variable-name reuse','document-audit: nondeterministic file ordering'],prior_r1=dict(commit='e75aa46a17e99bcc17795e051461a727c795aa6c',tree='372a02c6b8bd19401efeddcfe05050b614367af2',original_two_content_PASS_preserved=True,precontract_auxiliary_AI_disclosure_preserved=True,R7_I_final_process_qualification='WAIT_INPUT_OR_INDEPENDENCE',waived=False,semantic_PASS_migrated=False),shared=dict(CG04='MV01/MV02 and new R7-BP contribution only; U01 header/dungeon and U13 B04-R contributions preserved',CG05='new R7-FP only; U09 PD and record-consumer contributions preserved',actual_integration='NOT_PERFORMED',reception_gate='R7-I serial clause reception then fresh independent actual integrated R7-IR'),current_input_blockers=[],unmet_later_gates=unmet,L01_L14='input-evidence/L01-L14.json unchanged',old_56_92_boundary='RETAINED',denominator=dict(items=27,batches=13),result_branch='codex/r7-u03-reviewer-20261015-r2',only_result_write_prefix='candidates/R7-U03/evidence/reviewer/r2/',result_commit_tree_binding='Final handoff outside commit; manifest self is bound by actual result Git tree',integrated_PASS=False,ACCEPTED=False,CLOSED=False))
print(json.dumps(dict(packaged_input_evidence_files=len(copies)+4,records=2,candidate_verdicts=[r['verdict'] for r in records],stage='Packaging; not new behavior execution')))
