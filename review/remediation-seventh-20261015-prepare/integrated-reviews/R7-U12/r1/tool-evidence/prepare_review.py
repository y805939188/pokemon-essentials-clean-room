"""Package a qualified WAIT result; never promote byte audits into content PASS."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil
import subprocess

OUT=Path(__file__).resolve().parent
RESULT=OUT.parent
ROOT=Path('/workspace/r7-ir-R7-U12')
A=ROOT/'actual-input'
O=ROOT/'original'
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI='13d76ba61838b13925ba9d41f58a6b047564d926'
def ident(d):return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest())
def save(path,value): path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def git(*args):return subprocess.check_output(['git','-C',str(ROOT/'checkout'),*args])

# Read-only supplementary snapshots remain local inputs, not carried as MI bodies.
extra=[]
local_only=ROOT/'supplementary-read-inputs'
copied=OUT/'inputs/additional'
if copied.exists():
    for p in copied.rglob('*'):
        if not p.is_file():continue
        rel=p.relative_to(copied);data=p.read_bytes()
        target=local_only/rel;target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():assert target.read_bytes()==data
        else:shutil.copyfile(p,target)
        extra.append(dict(path=rel.as_posix(),commit=MI,local_path=str(target),**ident(data)))
    shutil.rmtree(copied)
else:
    for p in local_only.rglob('*'):
        if p.is_file():extra.append(dict(path=p.relative_to(local_only).as_posix(),commit=MI,local_path=str(p),**ident(p.read_bytes())))
save(OUT/'supplementary-input-identities.json',dict(files=extra,qualification='Fixed MI snapshots read locally; no MI body or candidate mirror is included in the result branch.'))

context=json.loads((OUT/'actual-context.json').read_bytes())
dispatch=(ROOT/'bootstrap/R7-U12-R7IR.md').read_text()
import re
excluded=sorted(set(re.findall(r'01[a-f0-9]{6}-[a-f0-9-]{27}',dispatch)))
assert context['thread_id'] not in excluded
context['excluded_visible_identities']=excluded
context['visible_thread_independent']=True
context['opaque_internal_context']='UNVERIFIED_NOT_EXPOSED; qualification retained, not inferred equal or independent'
save(OUT/'actual-context.json',context)

journal=json.loads((A/'integration/applied-clauses.json').read_bytes())
checks=json.loads((ROOT/'actual-plans/R7-U12.json').read_bytes())['shared_preservation_checks']
shared=[]
for check in checks:
    path=check['path'];batch=check['other_batch']
    row=next(f for f in journal['files'] if f['path']==path)
    hunks=[h for h in row['hunks'] if h['batch_id']==batch]
    review=json.loads((A/'shared-candidate-review'/batch/'per-id.json').read_bytes())
    eligibility=json.loads((A/'shared-root-reception'/batch/'eligibility.json').read_bytes())
    shared.append(dict(**check,actual_identity=ident((A/'actual'/path).read_bytes()),
        candidate_identity=ident((A/'shared-candidate'/batch/path).read_bytes()),
        candidate_review_evidence_identity=ident((A/'shared-candidate-review'/batch/'per-id.json').read_bytes()),
        root_eligibility=eligibility.get('root_eligibility'),
        journal_contributions=[dict(base=h['base_line_indices_half_open'],actual=h['actual_final_line_indices_half_open'],added_identity=h['added_identity']) for h in hunks],
        mechanical_result='EXACT_CONTRIBUTION_PRESERVED_BY_NEW_RECONSTRUCTION',
        semantic_compatibility='NOT_COMPLETED_WHOLE_CURRENT_SHARED_CONTENT_REVIEW',
        new_semantic_PASS_for_other_ids=False,receiver='R7-I',receiver_status='PENDING_CONTENT_AND_RESPONSIBILITY_RECEPTION'))
save(OUT/'shared-contribution-receipt.json',dict(checks=shared,same_boundary_order=journal['same_boundary_insertions'],
    all56_reconstruction='tool-evidence/all-56-clauses-audit.json',
    nonmandatory_adoption='NONE',unintegrated_procedural_waits=['R7-U03','R7-U07','R7-U10'],
    engine_UI_DX_cross_consumer_semantic_review='NOT_COMPLETED; bytes reconstruction alone does not satisfy it'))

missing=[
 dict(gate='WHOLE_CURRENT_SHARED_CONTENT',paths=['audit/source-traceability.md','planning/feature-matrix.md'],
      detail='Complete bytes restored/read by audit tools and exact clause assembly verified. Interactive semantic reads covered the U12 current projections, root phase notes and portions of history; they did not complete all shared current prose and every contribution/approval/consumer content review. Some long display attempts were truncated/omitted; those are not counted as full semantic reads.'),
 dict(gate='WHOLE_APPROVED_CONDITION_TARGETS_AND_CATALOGS',paths=[
 'deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md',
 'deliverables/final-specification-set/combat-requirements/wp41-switching-positioning-and-escape.md',
 'deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md',
 'deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md',
 'deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md'],
 detail='Five exact prior accepted MI bodies are mechanically preserved, but this review did not complete the required full content and intersecting domain-consumer review. Earlier actual PASS and matching bytes cannot substitute.'),
 dict(gate='COMPLETE_FROZEN_HISTORY_AND_DEPENDENCY_CONTENT',paths=[
 'review/remediation-sixth-20261014-prepare/integration/public-sync-20261014/sync-input.json',
 'deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md'],
 detail='Exact sync-input, item42, WP72 current rule and most contextual body sections were read/checked; the entire frozen sync-input and all required history/consumer material were not exhaustively content-reviewed here. Root M20/M21, WP72 domain and shared receiver responsibilities therefore remain pending.')]
save(OUT/'content-review-coverage.json',dict(required_actual_files=14,actual_bytes=1454436,
    complete_actual_full_text_semantic_review=False,
    generation_map_is_not_read_receipt='complete-content-line-map.json describes possible output pages, not completion; only actual platform tool output was viewed.',
    transport_or_source_availability_blocker=False,reason='These are readable remaining review obligations, not a material/host limit and not a discovered content defect.',
    missing=missing,semantic_scope_completed=[
      'Full R7IR dispatch and original Chinese seven-group contracts for both IDs; normalized verification/dependencies and C01/C08 counterproof substance; 12 original raw slice/pointer identities independently checked.',
      'M19 exact three entry navigation changes, same four H targets, historical README/static-cases qualification, ordinary controls, inverse reconstruction.',
      'H08 actual current errata, both ID projection lines, original item42/contract identity, WP72 5.2/5.3, WP27 3.2/3.3 and DG-U08-01-04, fixed Debug/Bag selected source ranges.',
      'Root errata metadata delta, new current reception text and source binding read rule; no acceptance/closure promoted.'
    ]))

nav=json.loads((OUT/'m19-navigation-audit.json').read_bytes())
h08=json.loads((OUT/'h08-navigation-audit.json').read_bytes())
common=dict(verdict='WAIT',content_verdict='SUPPORTED_NARROW_CHECKS_NO_FINAL_ACTUAL_PASS',
    actual_MI=MI,actual_MI_tree='6480ffe3df49bd9776c719f3c9be1c13618fdb0a',
    actual_FI=FI,actual_FI_tree='6747a584b91c86acd4771c1a6dee93260602106f',
    candidate_verdict_not_inherited=True,behavior_execution='NOT_EXECUTED',reference_observation='NOT_EXECUTED',
    new_reference_complete_model_host_Demo_native_media_real_save_replay=0,
    effective_configuration='UNVERIFIED',L01_L14='RETAINED',ACCEPTED=False,CLOSED=False,
    unmet_review_gates=missing,unmet_independence_gate=[],new_global_or_other_required_PASS=False)
def v(id,premise,reason,stage='SOURCE_STATIC + DERIVED_VECTOR'):
    return dict(id=id,premise=premise,independent_static_reason=reason,result='SUPPORTED_WITHIN_READ_SCOPE',stage=stage,behavior_execution='NOT_EXECUTED',whole_integration_content_gate='PENDING')
m19_vectors=[
v('C01-M19-MISSING','B three entries; inline local destinations, files and existing directories both count.',
  'New full-path parser obtains 136 local destinations,126 existing,10 missing occurrences/four unique B21 author targets.','TOOL_VALIDATION'),
v('C01-M19-DIRECTORY','README user-interface/ directory exists.',
  'Directory-prefix recognition keeps it valid; old012 exit1/11-5 error is preserved separately from corrected013.','TOOL_VALIDATION'),
v('C01-M19-FAMILY','All17 catalog families and three root/current/delivery controls.',
  '126 ordinary destinations preserve href/order and resolve against actual MI tree; controls remain exact B bytes.','TOOL_VALIDATION'),
v('C01-M19-RECOVER','Exact e58486178e746273fb6fab55df00722807f1dc44 four author files; archive/object prerequisite.',
  'All four independently restored with exact bytes/SHA/blob. Historical README identifies NEW2 candidate; actual-freeze distinguishes ACT. JSON payload identity/top qualification is not semantic reapproval.','TOOL_VALIDATION'),
v('M19-NAV-01','Three actual MI entries,3+3+4 changed hrefs.',
  'All10 immutable addresses identify H/four exact original author targets, no current actual-review substitution.','TOOL_VALIDATION'),
v('M19-NAV-02','Historical identity lookup and missing archive/object case.',
  'Notes explicitly require H objects or matching archive and say unavailable if absent; mirror identity bytes agree with fixed restoration.','TOOL_VALIDATION'),
v('M19-NAV-03','Complete three entry diffs and formal131/17 families.',
  'Remove each one navigation note and reverse only10 hrefs to reproduce exact B; actual three files equal corresponding approved candidate files. Full formal table retains131 paths/17 families.','TOOL_VALIDATION'),
v('M19-NAV-04','Existing routes and historical current/candidate/actual/closing labels.',
  'Normal routes remain unchanged; historical static-cases remain14 unexecuted designs; no runtime/approval transfer.','TOOL_VALIDATION')]
m19=dict(common,record_id='GR7-M19-001',actual_clauses=nav['scopes'],historical_target_identities=nav['historical_files'],vectors=m19_vectors,
    state_paths=dict(normal='Existing ordinary routes resolve; ten H destinations restore intended historical artifacts.',cancel='Stop read-only navigation; no domain write.',failure='Missing local B target cannot show artifact; adjacent valid link cannot substitute. H retrieval still requires available archive/objects.',partial_commit='No domain transaction/save mutation. Evidence commits are review publication only.'),
    counterproof_preserved=['Not a general relative-depth defect.','Not proof B21 evidence never existed.','Historical-body edits or replacement by actual-review payload are unnecessary.'],
    dependencies=dict(direct_record_edges=[],transitive_record_edges=[],qualification='Empty author scheduling edges do not satisfy domain/history obligations.',direct_consumers=['three actual entry documents','four historical author targets','current root/delivery/actual-freeze navigation'],transitive_consumers=['M20 historical qualification','M21 current supplement judgment','R7-I historical/source-binding receiver'],reception='PENDING_WHOLE_CONTENT_AND_ROOT_RESPONSIBILITY_REGISTRATION'),
    shared_receiver='R7-I; full shared contribution content remains a gate; no whole-mirror overwrite found by independent assembly audit.')
hvec=[
v('H08-NAV-01','Read historical /items/42/actual_clause_label.', 'Old label is5.2; actual WP72 5.2 covers party/storage and5.3 line124 covers adding items. New errata names both and exact source/clause identities.','TOOL_VALIDATION'),
v('H08-NAV-02','Both current projections, historical state columns.', 'Actual audit line1833 and matrix line553 point to5.3/WP27 and same named errata; state columns match B. Frozen R6 original remains5.2.','TOOL_VALIDATION'),
v('H08-NAV-03','WP72/WP27/DG and old R6.', 'Relevant rule/control bytes are unchanged. R6 subtree exact preservation is mechanical evidence; whole content/history acceptance is still pending.','TOOL_VALIDATION'),
v('H08-NAV-05','Actual whole-file/current clause identity.', 'MI bytes and LF-inclusive line124 identity match, root delta changes only status/reception, not label/rule/precedence.','TOOL_VALIDATION'),
v('H08-NAV-04-normal1','Registered valid item; one finite slot,max999,empty,request1; add/message dependencies normal.', 'Enough capacity permits1,true; message uses requested1; automatic sorting also needs configured enabled and successful sort.'),
v('H08-NAV-04-list-cancel','List cancelled before selected USE item.', 'Caller guard prevents both add and giving message.'),
v('H08-NAV-04-quantity0','Quantity BACK explicitly returns0.', 'Positive quantity guard prevents add and giving message.'),
v('DG-U08-01','POTION,finite one slot,max999,empty,request2; normal dependencies.', 'Capacity accommodates2; normal add returns true; message uses2.'),
v('DG-U08-02','Same finite configuration,initial998,request2; no concurrent bag change,observe after normal add/message.', 'Only1 fits; written999 remains when false returns; successful-sort path skipped; caller ignores false so normal message still requests2.'),
v('DG-U08-03','Same finite slot,initial999,request1.', 'Zero added,false,no successful sort; normal caller still requests message1.'),
v('DG-U08-04-list-cancel','Independent cancellation/quantity0 controls.', 'Guards prevent mutations and giving message; not generalized to all Debug cancellations.'),
v('DG-U08-04-message-failure','Add reached full/partial writes,then message fails.', 'No rollback contract; reached writes persist; normal feedback/cleanup not guaranteed.'),
v('DG-U08-04-infinite-pocket','Independent infinite pocket,existing999,request1; valid data/dependencies.', 'Infinite max becomes current length+1, so another slot can receive1; finite one-slot anomaly is not a default pocket-full claim.'),
v('DG-U08-04-fill-bag-control','Separate fill-bag path,quantity3,important and ordinary items.', 'Clear precedes filling; important1/ordinary3,unavailable/full pockets skip; separate path does not consume add return.'),
v('H08-NAV-04-zero-capacity','Finite zero available room; normal dependencies.', 'No caller precheck; can add0 and return false while normal message still uses requested quantity.'),
v('H08-NAV-04-add-failure','Add fails exceptionally after some writes reached.', 'Following message may not be reached; no general rollback,cleanup or final host-output guarantee.')]
hrecord=dict(common,record_id='GR7-H08-001',actual_clauses=h08,vectors=hvec,
    state_paths=dict(normal='Positive quantity with space writes and normal feedback uses request.',cancel='List/BACK0 guard prevents add/message.',failure='Add/message exceptions do not promise cleanup or rollback.',partial_commit='Finite998+2 retains1 despite false; not all-or-nothing.'),
    counterproof_preserved=['5.2 has no adding-item rule;5.3 is the intended clause.','Earlier nine-supplement searches were locators, not full content reads.','No old ACCEPTED/CLOSED behavior is reopened.'],
    dependencies=dict(direct_record_edges=[],transitive_record_edges=[],qualification='No named author schedule edges does not remove domain obligations.',direct_consumers=['current-navigation-errata','audit/matrix projections','WP72 5.3'],transitive_consumers=['WP27 3.2/3.3','DG-U08-01-04','WP72/domain owner including M15','root current-supplement/public-sync owner'],reception='PENDING_WHOLE_CONTENT_AND_ROOT_RESPONSIBILITY_REGISTRATION'),
    shared_receiver='R7-I,CG01/CG07; U01/U02/U11/U13 bytes preserved mechanically; U03/U10 future contributions not assumed present.')
save(RESULT/'per-id.json',dict(schema='r7.u12.actual-independent-review.v1',reviewer_thread=context['thread_id'],records=[m19,hrecord],
    denominator=dict(required_items=27,batches=13),old56_92='Retained limited historical boundaries; not re-signed.',nonmandatory_adoption='NONE',all_behavior='NOT_EXECUTED'))

input_rows=json.loads((OUT/'restored-byte-audit.json').read_bytes())
save(RESULT/'review-input-receipt.json',dict(schema='r7.u12.actual-input-receipt.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    thread=context['thread_id'],internal_context='UNVERIFIED_NOT_EXPOSED',subagents_created=0,
    dispatch=dict(commit='c64774c60d91e522cb515ef71e3e9d4ea6b4712c',path='review/remediation-seventh-20261015-prepare/integration/wave2/v1/dispatch/R7-U12-R7IR.md',**ident((ROOT/'bootstrap/R7-U12-R7IR.md').read_bytes())),
    fixed_B=B,fixed_R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',actual_MI=MI,actual_MI_tree='6480ffe3df49bd9776c719f3c9be1c13618fdb0a',actual_formal_tree='8403869aaeb4726518414b409b3808c3c0780e65',actual_FI=FI,actual_FI_tree='6747a584b91c86acd4771c1a6dee93260602106f',
    original_restore=dict(files=26,bytes=7587353,destination=str(O)),actual_restore=dict(files=240,bytes=8075455,destination=str(A)),
    restored_identity_audit=dict(count=input_rows['count'],bytes=input_rows['bytes'],path='tool-evidence/restored-byte-audit.json'),
    fixed_input_plans=[dict(path=str(ROOT/p/'R7-U12.json'),**ident((ROOT/p/'R7-U12.json').read_bytes())) for p in ['original-plans','actual-plans']],
    extra_inputs=extra,source_snapshots='Read-only bounded fixed R snapshots; not full reference checkout or execution.',
    no_80MB_manifest_or_full_core_scan=True,restored_programs_executed=0,
    full_semantic_review_complete=False,content_coverage='tool-evidence/content-review-coverage.json',
    effective_configuration='UNVERIFIED',L01_L14='RETAINED',history_logs='Original012/013,author002/013/020/021 and candidate-review qualifications preserved; no backfill.',
    result_scope='Only two WAIT decisions and actual independent tool evidence, no acceptance/closure.'))
print(json.dumps(dict(records=2,verdicts=['WAIT','WAIT'],source_or_transport_failure=False,remaining_gate='Required whole-current-content and consumer/history review incomplete',new_behavior_executions=0)))
