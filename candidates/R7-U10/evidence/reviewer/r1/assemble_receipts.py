"""Assemble review decisions and actual input/tool evidence; no candidate writes."""
import datetime, hashlib, json, pathlib
P=pathlib.Path(__file__).parent
def read(p):return json.loads(pathlib.Path(p).read_bytes())
def put(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
fixed={'dispatch_commit':'95c260d8f3fb4a171675dde877137fcd4c2f1c8d','dispatch_tree':'577c350364bb4e2eb712325a9095d53d29eeeeb3','freeze_commit':'aa369555b0e8b6c8b077f964b54ed63d3b924f26','freeze_tree':'08bd0f362c74ef7645b5bbd70b557489c122ae29','candidate_commit':'583330fb69935ff6b2eb32ca11ede6c23bde5ecd','candidate_tree':'7a81a11b22d771fe79f165a265fa108c4a85502c','base_commit':'e646432c644dec04d306842cc5a559a29c718fbc','contract_commit':'f622356f3beb9e84ea8cff9db07c7fb382565d3f','contract_path':'review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U10.json'}
identity=read(P/'execution-identity.json')
audit=read(P/'independent-validation.json')
context=pathlib.Path('/workspace/r7-context/R7-U10-reviewer')
norm=read(context/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json')
author=pathlib.Path('/workspace/r7-review-input/R7-U10-r1-583330fb69935ff6b2eb32ca11ede6c23bde5ecd/candidate/candidates/R7-U10/evidence/author')
vectors=read(author/'per-id.json')['records']
reasons={
'GR7-M15-001':[
 ('C01-M15-BACK','Explicit reload occurs on browse; BACK restores size only; main-menu coordinate refresh preserves selected bitmap identity.'),
 ('C01-M15-NO-BROWSE','Entry binds registration1, no selection change occurs, BACK leaves binding1.'),
 ('C01-M15-REOPEN','Reopening invokes explicit species/resource selection from restored registration1.'),
 ('C01-M15-USE','Independent changed-size confirmation sets true and leaves current item.'),
 ('C01-M15-ACTION','Independent changed-size confirmation sets true and cycles; later page effects require their own premise.'),
 ('C01-M15-PREEXISTING','BACK never clears preexisting true; later total-save gate still applies.'),
 ('C01-M15-POSITION','Coordinate BACK restores fields then refreshes positions; no resource rebinding inferred.'),
 ('U10-M15-FAILURE','Successful resource/input/window premise is explicit; no exception rollback/redraw guarantee.'),
 ('U10-M15-SAVE','No persistence on BACK; prior true versus false total-save paths remain distinct.')],
'GR7-M15-002':[
 ('M09-0-Load','selected0 remains valid after resize2; loads A0.'),('M09-0-Rename','selected0 remains valid; normal name access.'),('M09-0-Delete','Replaces slot0; length2, slot1 unchanged.'),
 ('M09-1-Load','selected1 remains valid; loads A1.'),('M09-1-Rename','selected1 remains valid; normal name access.'),('M09-1-Delete','Replaces slot1; length2, slot0 unchanged.'),
 ('M09-2-Load','selected2 equals new length; no navigation/clamping; canvas prefix may change before nil graphic access.'),
 ('M09-2-Rename','Same independent reset: nil name access unprotected.'),
 ('M09-2-DeleteYes','Assignment at exactly length appends slot2; no gap, length3, old0/1 unchanged.'),
 ('M09-2-DeleteNo','Confirmation canceled: no write/append, length2.'),
 ('M09-2-Navigate','Direction modulo restores a valid window index before consumer action.'),
 ('M09-BACK-SAVE','Memory resize precedes listBACK; explicit outer Save controls disk; Exit clears cache by its separate gate.')],
'GR7-M17-001':[
 ('TOOL-AN-01','Main count=0 height192 branch; save request conditional on prior normal calls.'),
 ('TOOL-AN-02','Main count6 requests two rows; index5 row1/column0.'),
 ('TOOL-AN-03','Rectangle destination subtracts source width/height from slot+96, doubles extents; source x/y separate.'),
 ('TOOL-AN-04','File.Exists false branch jumps to original index increment; normal slot1 is retained and save follows loop.'),
 ('TOOL-AN-05','IsNullOrEmpty(x) bypasses all four numeric conversions and constructs all-zero rectangle request.'),
 ('TOOL-AN-06','Whole parse precedes output; each animation saves separately; finally is cleanup, no restore of successfully saved A.'),
 ('TOOL-AN-07','No-argument branch prints help, ReadLine then return; else only args[0] read.'),
 ('TOOL-AN-08','CreateXmlTextReader has missing-path and IOException-specific exit1 requests; not a blanket exception handler.'),
 ('TOOL-AN-09','Nonnegative helper compares parsed value<0; diagnostic and Exit(1) requests.'),
 ('TOOL-AN-10','Zero does not enter negative branch; rectangle/library consequences remain unknown.'),
 ('TOOL-AN-11','EH catches FormatException only; specified invalid numeric text is conditional on that exception.'),
 ('TOOL-AN-12','Missing attribute is handed to external integer conversion; do not infer same caught exception or partial outputs.'),
 ('TOOL-AN-13','Overflow is not caught by the FormatException-only helper; no universal exit1/recovery.'),
 ('TOOL-AN-14','XML handler requests a format containing {2} with only two arguments; no guaranteed diagnostic or returned collection.'),
 ('TOOL-AN-15','LoadImage checks alpha; non-alpha requests Bitmap copy, GetPixel(0,0), MakeTransparent; no pixel claim.'),
 ('TOOL-AN-16','Local numeric gate has no96 upper-bound; documentation preserved without adding clamp.'),
 ('TOOL-AN-17','Existing-path LoadImage failure is not the missing-path skip branch; no later save/normal completion guarantee.')]
}
sources={
'GR7-M15-001':['SpritePositioning.rb 1–411','Species_files.rb 156–179','SpeciesMetrics.rb 1–101','BitmapSprite.rb 141–207','MessageConfig.rb 492–511','Debug_MenuCommands.rb 1226–1237'],
'GR7-M15-002':['BattleAnimationPlayer.rb 334–390','AnimEditor_Functions.rb 91–183,994–1001','SpriteWindow_text.rb 753–976,1044–1248','Editor_Listers.rb 4–11','AnimEditor_SceneElements.rb 409–427'],
'GR7-M17-001':['animmaker.exe all15 methods/all11 EH; primary 14/15 and helpers9/11, metadata','animmaker.txt 1–26','AnimEditor_Functions.rb 1–183','AnimEditor_ExportImport.rb 1–147','Compiler_CompilePBS.rb 1260–1321']}
records=[]
for idx,ar in zip([19,27,21],vectors):
    rid=ar['record_id'];original=norm['records'][idx]
    byid={v['id']:v for v in ar['candidate_vectors']}
    checks=[]
    for vid,reason in reasons[rid]:
        v=byid[vid];checks.append({'id':vid,'candidate_premise':v['premise'],'candidate_expected_static':v['expected_static'],'independent_assessment':reason,'content_verdict':'PASS_SCOPED_CANDIDATE','behavior_execution':'NOT_EXECUTED','basis':'Fresh root reviewer source/control-flow and candidate text reading; not author static_result or a tool exit code.'})
    records.append({'record_id':rid,'content_verdict':'PASS_SCOPED_CANDIDATE','workflow_qualification':'WAIT_INPUT_OR_INDEPENDENCE','workflow_reason':'Before full dispatch access, one read-only repository-access helper was created; no candidate review delegated. Contract no-subtask deviation requires R7-I disposition.','input_identity':fixed,'candidate_files':[x for x in audit['candidate_files'] if x['path'].endswith('.md') and '/evidence/' not in x['path']],'fresh_source_read_scope':sources[rid],'original_full_contract_ref':fixed['contract_commit']+':'+fixed['contract_path']+'#/original_full_contracts/'+str([19,27,21].index(idx)),'original_normalized_record_pointer':'/records/'+str(idx),'original_verification':original['groups']['verification'],'original_dependencies_retained':original['groups']['dependencies'],'checks':checks,'preservation':'Full five-mirror byte diff; permitted clauses only; unmodified B semantics retain their historical qualification. No optional/policy adoption; no host claim.','unmet_dependencies':['R7-I workflow deviation disposition and actual result reception','R7-I serial clause integration/shared receivers','Exact historical dedup and affected regression reception','Fresh different-context R7-IR of actual cumulative integration','Formal acceptance then closure gates'], 'integrated_PASS':False,'ACCEPTED':False,'CLOSED':False})
put('per-id.json',{'schema':'r7.u10.reviewer.per-id.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'overall_workflow_verdict':'WAIT_INPUT_OR_INDEPENDENCE','scoped_content_verdict':'PASS_SCOPED_CANDIDATE','actual_reviewer_thread':identity['visible_runtime_identity']['CODEX_THREAD_ID'],'identity_qualification':identity,'records':records,'denominators':{'required_items':27,'batches':13},'execution':{'reference_observation':0,'reference_target':0,'independent_full_model':0,'host':0,'Demo':0,'native_media':0,'real_save_replay':0,'vectors':'NOT_EXECUTED','audits':'TOOL_VALIDATION / SOURCE_STATIC only'},'L01_L14':'RETAINED'})
def idfile(p):
    b=pathlib.Path(p).read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
put('review-input-receipt.json',{'schema':'r7.u10.reviewer.actual-input-receipt.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),**fixed,'actual_context':identity,'original_restore':{'count':39,'bytes':6796155,'receipt':'tool-evidence/original-recovery-receipt.json'},'candidate_restore':{'count':61,'bytes':1050546,'receipt':'tool-evidence/candidate-recovery-receipt.json','read_only_directory':'/workspace/r7-review-input/R7-U10-r1-583330fb69935ff6b2eb32ca11ede6c23bde5ecd/candidate','files':audit['candidate_files']},'supplements':{'count':10,'bytes':454772,'receipt':'supplement-reception.json'},'original_bindings_verified':171,'dispatch':idfile(P/'tool-evidence/dispatch-fetch.json'),'candidate_input_exact_bytes':idfile(P/'tool-evidence/candidate-input.json'),'scope_audit':'independent-validation.json','semantic_credit_from_transport':False,'snapshot_limit':'Bounded immutable file snapshots; not a complete new Git/reference checkout. No imported author/reference/native program execution. C06 audit decoder was read in full and its byte loader adapted; target not evaluated.','log_qualification':'Actual restoration per-request times retained. Initial platform discovery was not locally wrapped; logs001 onward are real separated audit subprocess I/O. No retrospective original timestamps/PIDs invented.','workflow_qualification':'WAIT_INPUT_OR_INDEPENDENCE','workflow_deviation':'One pre-contract read-only access feasibility helper; candidate review remained with this root reviewer.'})
print(json.dumps({'records':len(records),'checked_vectors':sum(len(r['checks']) for r in records),'content':'PASS_SCOPED_CANDIDATE','workflow':'WAIT_INPUT_OR_INDEPENDENCE'}))
