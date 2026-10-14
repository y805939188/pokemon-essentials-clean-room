"""Record the reviewer's adjudication and actual coverage, without editing inputs."""
import datetime, hashlib, json, pathlib, re, subprocess
ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
REL='review/remediation-sixth-20261014-prepare/reviews/R6-U10-R'
OUT=ROOT/REL
PREP='469a268b92daed7b4d28d7fd0da75520cbb7228f'
CAND='d3554f9479fadcd1255cf8103b19e4aa88e1825b'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
BASE='review/remediation-sixth-20261014-prepare/'
def write(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def show(ref,path): return subprocess.check_output(['git','show',ref+':'+path],cwd=ROOT)
contract=json.loads(show(PREP,BASE+'contracts/R6-U10.json'))
tool=json.loads((OUT/'independent-tool-validation.json').read_text())
requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default',speed='default',fast=False)
effective={k:'UNVERIFIED_NOT_ECHOED' for k in ['model','effort','tier','speed','platform_uuid']}
peers=[
 dict(task='/root/capture_counterreview',role='Non-author supporting counterreview; no candidate/report writes',
      ids=['R6-UI-001','R6-UI-002'],requested=requested,effective=effective,
      conclusion='SUPPORTS_FIXED_CANDIDATE_STATIC_RULES_NO_REQUIRED_REVISION',
      full_reference=[['CatchAndStoreMixin',1,271],['Battle_Peers',1,77],['PokemonStorage',1,400],['Utilities_Pokemon',1,292],['SafariBattle',1,502],['Battle_Scene',1,419],['SafariZone',1,196]],
      partial_reference=[['Battle',78,121],['Battle',815,841],['Battle_StartAndEnd',400,501],['Trainer',57,89],['Settings',215,221],['Scene_ChooseCommands',141,228],['Item_BattleEffects',1,65],['Overworld_BattleStarting',138,305],['Overworld_BattleStarting',340,412]],
      formal_read=[['WP67-A',1,348],['WP38',88,146],['WP53',49,99],['UI catalog',320,385]],
      candidate_read='Complete five-mirror diff plus changed WP67-A text and U10 addition; not five direct candidate full-file reads',
      old_evidence_full=['storage/counterreview-R6-UI-001.json','bag/counterreview-R6-UI-002.json','bag/counterreview.json','root/counterreview-storage.json','root/counterreview-bag.json','R6-F/countercheck-ui-entry-stale-command.json'],
      imported_facts_complete_selected_records=[50,54,56,69,70,71,72,73,74],
      historical_full=[['WP67-A first review',1,305],['WP67-A recheck-v3',1,38],['R4-U03 actual-v1 report',1,29]],
      fixed_core_remote_full=['capture-message-order.rb','capture-message-order.stdout.jsonl','capture-message-order.stderr.log','tool-evidence-status.json','execution-evidence.json'],
      counter_attempts=['Storage performs deletion before caller','Message does not block subsequent memory updates','Cancellation deletes old party anyway','Storage failure already committed deletion','Safari has an implicit full-party entry gate','Safari uses a different full predicate','WP53 clause automatically cures old WP67-A wording'],
      limits=['Source/model/host execution0','Original probe surrogate Storage and message, healingfalse and Shadow surrogate; stdout only initial item and level memories','Original probe UTC absent; not backfilled','No blanket R2-R5 or 92-item semantic reapproval']),
 dict(task='/root/party_counterreview',role='Non-author supporting counterreview; no file writes',
      ids=['R6-UI-PARTY-001','R6-UI-PARTY-002'],requested=requested,effective=effective,
      conclusion='SUPPORTS_FIXED_CANDIDATE_STATIC_RULES_NO_REQUIRED_REVISION',
      full_reference=[['Summary',1,1400],['MoveRelearner',1,199]],
      partial_reference=[['Pokemon',1,60],['Pokemon',604,723],['Pokemon',1159,1227],['SaveConversions',163,199],['SaveConversions',275,350],['Party',700,715],['Storage',1245,1407],['Evolution',1,28],['Settings',1,18],['Settings',140,158],['PBS pokemon BULBASAUR',1,29],['Window_text',1056,1255],['Item_Utilities',582,757],['Utilities001',413,489],['Item_Effects',64,97]],
      candidate_full=[['WP66-A',1,267],['WP18',1,383]],
      formal_mode='Candidate full text plus exact old replacements and equal-span checks; direct formal full files also read by payload_history_audit',
      old_evidence_full_records=['storage/counterreview-party.json wrapper and results/0 and results/1','F withdrawal counterevidence','K withdrawal note','root/storage counterevidence'],
      imported_facts_complete_selected_records=list(range(77)),
      counter_attempts=['Initialization or old save migration pads the array','Display writes zero back','BACK+ACTION must fail','USE+ACTION must fail','Storage direct Mark has the same ACTION branch','Final dedup moves overlapping records forward','Window sorts names after candidate computation','Low-level BULBASAUR fields are illegal','Reminder statistic precedes successful teaching'],
      peer_support=['Separate non-author full MoveRelearner and command-consumer audit','WP30 baseline/candidate1-282','B16 exact records244/245/250 qualifications and tuple','R5 records52/67 and corresponding contract/activation pointers'],
      limits=['B16 mechanical carrier-line arrays and local_projections not fully reread','No blanket341-contribution or92-item semantic reapproval','Source/model/host execution0']),
 dict(task='/root/payload_history_audit',role='Non-author full-text/identity/history audit; no file writes',
      requested=requested,effective=effective,
      full_formal=[['WP18',1,383],['WP30',1,282],['WP66-A',1,265],['WP67-A',1,348]],
      full_candidate=[['WP18',1,383],['WP30',1,282]],
      nested_full_catalog=dict(baseline=[1,914],candidate=[1,978],role='Non-author read-only catalog peer'),
      candidate_ui_full_credited_to='/root primary: WP66-A1-267 and WP67-A1-348',
      original_history_full=[['WP66-A first review',1,139],['WP66-A closure',1,22],['WP66-A recheck-v3',1,45],['WP67-A first review',1,305],['WP67-A recheck-v3',1,38],['WP18/20 closure',1,88],['WP26/27/30 closure',1,127]],
      author_evidence_full=['historical-state-binding','protected-regressions1-3829','publication-readback1-1578','author read-delivery62 records','author json-read-delivery8 records'],
      history_original_object_checks=['activation-receipt at12df95a8e81061a606d50d3f0a0528793b2e6b2c full JSON including92 selections','closing candidate at13fddb0a217b36974c75657aa68da0caf104ee48 complete records52/67','R5-U03/U06 task-packets at22fba778 original bytes and findings4/0'],
      activation_tool_scope='92 selected states and whole closing-record qualification hashes matched, errors=[]; this is not92 full semantic new reviews',
      remote_candidate_receipt=dict(commit=CAND,tree='f71699038cbd900eedaeb76f28f7fd1910ec9185',
         subtree='59cf3a02ff13c1bf45bedcea63ad28668355db69',started_utc='2026-10-14T14:52:26.888925Z',ended_utc='2026-10-14T14:52:28.111796Z',
         method='Fixed-commit raw HTTP whole payload reads plus GitHub commit/tree/compare',http200=25,payloads=25,bytes=694268,bytes_sha256_git_blob_match=True,
         tree_truncated=False,trees=7,blobs=25,prepare_to_core=23,core_to_publication=2,prepare_to_candidate=25,
         role='Same-round non-author supporting remote audit, not author receipt reuse'),
      audit_clarification='Author R1 original-review term is ambiguous: actual author reads are GROUP1-C02 closure and v3, not first139-line progress review or all29 findings; independent peer supplemented first review; no specification amendment needed')]
write('peer-reading-receipts.json',dict(kind='SAME_ROUND_NONAUTHOR_RECEIPTS_RECORDED_BY_PRIMARY',fixed_candidate=CAND,
   delivery='Collaboration tool messages/final receipts; these are peer attestations, not the primary own read ledger or invented platform UUIDs',
   receipts=peers,source_content_not_copied=True))
primary_rows=[json.loads(x) for x in (OUT/'primary-read-delivery.jsonl').read_text().splitlines()]
prompt_ranges=[[1,220],[221,500],[501,900],[901,1300],[1301,1700],[1701,2100],[2101,2492],[2493,2870],[2871,3290],[3291,3767]]
write('reading-coverage.json',dict(kind='ACTUAL_PRIMARY_AND_PEER_READING_COVERAGE',primary='/root',
   primary_prompt=dict(identity=tool['prompt'],ranges=prompt_ranges,delivery='Connected GitHub full UTF-8 body stored then delivered as contiguous nontruncated ranges;221-500 reread after combined output truncation',semantic_full=True),
   independent_contract=dict(identity=tool['contract'],semantic_full=True,mode='Complete separately fetched contract and exact full embedded contract; initial combined truncation not credited, complete embedded text reread'),
   own_full_candidate=[['WP66-A',1,267],['WP67-A',1,348]],own_catalog_addition=[915,978],
   own_full_reference=['CatchAndStoreMixin1-271','Battle_Peers1-77','SafariBattle1-502','Utilities_Pokemon1-292','PokemonStorage1-400','Battle_Scene1-419','MoveRelearner1-199'],
   own_partial_reference='Exact commit/path/ranges and whole-payload identities in primary-read-delivery.jsonl; do not credit entire Pokemon/Summary/SaveConversions/PBS from partial reads',
   all_5_formal_and_5_candidate_full_coverage='Complete same-round team coverage; attribution in peer-reading-receipts.json, not an assertion all10 were primary direct reads',
   original_counterevidence='All9 complete identity checks; related complete records/read carriers via capture and Party peers. Imported320 full carrier is not semantic full-credit',
   raw_delivery_rows=primary_rows,hash_credit='Identity/tool validation only; never semantic full reading',
   truncations_preserved=[dict(path='WP67-A',attempt='combined ranges1-100/101-200 exceeded orchestration output; both fully redelivered individually',credited=False),
       dict(path='per-id-validation.json',attempt='large full delivery truncated; omitted245-365 reread; remainder visible and peer records also read',credited=False),
       dict(path='publication-readback.json',attempt='primary full output truncated; primary only visible structural content. Full1-1578 credit belongs to payload_history_audit',credited=False),
       dict(path='initial combined contract/prompt',attempt='orchestration output truncated; contract full coverage uses independently complete prompt block',credited=False)],
   uncredited_initial_metadata='Initial status/search/fetch tools and connector404/timeout do not have retained per-call UTC/raw output files; original tool outputs remain in conversation, not backfilled as a launcher archive'))
clauses=[['WP67-A226','WP67-A228','catalog926-934'],['WP67-A304','catalog942-946'],['WP18 179','WP66-A182','WP66-A184','catalog954-962'],['WP30 42','WP30 228','WP66-A218','catalog970-978']]
families=['CP','SF','MK','RL']; sizes=[9,5,9,9]
rules=[
 '成功送盒→删除玩家队伍旧成员→暂停→正常返回后移动四类记忆→通常接收新个体；入队暂停正常返回后才回填初始道具。',
 '仅玩家队伍与全部当前盒同时满才拒绝；拒绝在扣球前且正常消息返回后重显；放行先扣球再刷新／投球请求。',
 '默认标记为空列表；显示缺失槽为零不补齐。独立ACTION缺失槽在提交前失败；显式零和BACK／USE优先组合另按正常合同。',
 '等级候选首现次序；仅未会且不在等级候选的最初记录项前置，重叠项留原等级位置；显示／首选／选择保持该序。']
controls=[
 '暂停内盒持同一A、队伍5、N未入队、四记忆旧；正常后移位／入队；Send to a Box不删旧人；选人BACK在转移前；消息异常仅已存已删前缀；更早双满失败尚未删。',
 'party1/boxes全满放行10→9；party6/boxes全满拒绝仍10且不进回合末；party6/box有位放行；Run及末球／捕获结局原条件保持；后段失败不保证退球。',
 '[]独立ACTION失败；显式六零ACTION无操作；[]USE→ACTION→BACK弃稿；先编辑再缺槽ACTION未提交；BACK+ACTION取消；USE+ACTION仅USE；OK差异写入，Storage入口无清零分支。',
 '合法BULBASAUR L2仅AMNESIA：空记录和[GROWL]均[TACKLE,GROWL]；[CURSE]前置。重复诊断、已会记录／配置关／混合序、BACK和USE成功才统计均分列；不证明Demo。']
regressions=[
 ['R1 WP67-A R04/R06/R07 qualified spans','K32/K33 and K17/K49','WP38 partner/held-item/capacity scope'],
 ['R1 WP67-A original/v3 qualified spans','K17/K49 ordinary gate','K37 Safari factors and outcomes','WP53 correct clause read-only'],
 ['R1 WP66-A normal Mark and egg scope','A30/A35','WP18 creation default','Storage directMark','R4 Summary display scope','R5 related52/67/confirmation scope'],
 ['A31/A32','B16-A044/A048/C003 exact records244/245/250 qualified scope','WP30§6.3 precise unchanged','HM/full-slot cancellations','R5 exact selected old scopes']]
records=[]
for i,c in enumerate(contract['scope_contracts']):
    rec=dict(id=c['id'],candidate_verdict='PASS',evidence_level='SOURCE_STATIC_AND_DERIVED_VECTOR_NOT_EXECUTED',
      identity_and_verdict=dict(classification='required',severity='P2',aliases=c['aggregation_aliases'],
          complete_fixed_contract_record_sha256=hashlib.sha256(json.dumps(c,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
          original_proposal_generation_status_preserved=True,no_new_root_cause=True),
      bidirectional_evidence=dict(fixed_source_commit=REF,source_producers=c['bidirectional_evidence']['source'],
          necessary_consumers=c['bidirectional_evidence']['necessary_consumers'],fixed_primary_formal=c['identity_and_verdict']['primary_contract'],
          candidate_clause_locators=clauses[i],actual_forward_reverse_join='New source/consumer review to precise changed clause and complete vector family; no definition-only wiring inference',
          all_9_original_ev_identity_checks='independent-tool-validation.json',semantic_original_counterevidence='peer-reading-receipts.json with actual carrier/record scope'),
      premises_and_counterexample=dict(complete_original_contract_input_domain=c['premises_and_counterexample']['input_domain'],
          newly_checked_controls_and_failure_prefix=controls[i],counter_attempts=peers[0 if i<2 else 1]['counter_attempts'],
          source_bug_vs_future_policy_separated=True,static_not_runtime=True),
      minimum_revision_contract=dict(candidate_rule=rules[i],satisfied=True,additional_necessary_behavior_revisions=[],
          preserved_scope=c['minimum_revision_contract']['preserve_correct_scope'],
          no_architecture_or_source_copy=True,no_optional_policy_write=True),
      acceptance_and_regression=dict(complete_contract_conditions=c['acceptance_and_regression']['conditions_and_vectors'],
          candidate_vectors=[f'U10-{families[i]}{n:02}' for n in range(1,sizes[i]+1)],
          static_vector_check='PASS',executed_vectors=0,regression_scopes=regressions[i],
          exact_old_byte_preservation='independent-tool-validation.json and peer independent span audit',
          no_old_pass_transferred=True,no_blanket341_or92_new_semantic_pass=True),
      independent_adjudication=dict(reviewer='/root R6-U10-R',supporting_peer=peers[0 if i<2 else 1]['task'],
          not_candidate_author_in_current_task=True,candidate_hash_binding=CAND,
          requested_configuration=requested,effective_configuration=effective,
          configuration_qualification='UNVERIFIED',behavior_scope_verdict='PASS',
          independent_reads='primary-read-delivery.jsonl, reading-coverage.json, peer-reading-receipts.json'),
      dependencies_and_receivers=dict(primary_batch='R6-U10',author_dependencies=[],sole_integration_receiver='R6-I',
          candidate_write_paths=c['minimum_revision_contract']['candidate_formal_write_set'],
          administrative_sync_owner='R6-I; audit/source-traceability and planning/feature-matrix after actual acceptance',
          shared_file_receivers='WP18 U01/U14; WP30 U14; WP67-A U07; catalog U11/U12; WP66-A U10',
          integrated_review='PENDING_ACTUAL_COMBINED_VERSION',formal_acceptance=False,CLOSED=False))
    records.append(rec)
write('adjudication.json',dict(kind='INDEPENDENT_NONAUTHOR_FIXED_CANDIDATE_ADJUDICATION',verdict='PASS',
  exact_scope='Four required P2 candidate behaviors and static acceptance only',candidate_commit=CAND,candidate_tree='f71699038cbd900eedaeb76f28f7fd1910ec9185',
  prepare_commit=PREP,frozen_formal_commit=MAIN,frozen_reference_commit=REF,adjudicated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
  reviewer_configuration_qualification='UNVERIFIED_NOT_ECHOED',records=records,
  behavior_execution=dict(reference=0,independent_model=0,host_demo=0,real_save_or_production_behavior=0),
  required_additional_candidate_behavior_revisions=[],
  metadata_clarifications=['Author R1 original-review wording scoped to closure+v3; current peer separately read initial report','Author receipt core23 is not finalcandidate25; current independent remote readback25 fills binding','No effective model/effort/tier/speed/platformUUID echo or missing historical raw logs backfilled'],
  integrated_pass=False,formal_acceptance=False,CLOSED=False))
write('reviewer-environment.json',dict(reviewer='/root',logical_entry='R6-U10-R',requested=requested,effective=effective,
  actual_platform_configuration_echo_available=False,CLI_configuration_proof_runs=0,
  source_thread_id_user_supplied='01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',source_thread_id_is_current_reviewer_platform_uuid=False,
  cwd=str(ROOT),branch='codex/remediation-sixth-r6-u10-review-20261014',initial_head=MAIN,
  branch_start_commit=CAND,only_content_write_allowlist=REL+'/',
  reference_recovery='Fixed official reference objects fetched into project object database; no checkout/source modification',
  applicable_AGENTS=['AGENTS.md'],applicable_nested_AGENTS_or_agent_skills=[],
  real_task_names=[p['task'] for p in peers],uuid_proof='UNVERIFIED; canonical collaboration task names are not platform UUIDs',
  timestamp='This is metadata generation time, not an invented launcher start time',metadata_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
  initial_observed_failures=['No shell tools until selected environment ready','Prepare object absent beforefetch:git128','Missing .agents/prepare/reference search:rg2','Connectedreview/AGENTS404 andprepare/AGENTS404 (later git tree confirmed absent)','Contract connector initial ConnectTimeout, successful ordinary reread','Combined long outputs truncated and subsequent credited coverage distinguished'],
  raw_early_metadata='Per-call UTC/raw stdout/stderr not retroactively reconstructed; tool conversation retains observed returns',
  no_Mac=True,no_force=True,no_delete=True,no_merge_main=True,no_candidate_formal_or_public_ledger_edits=True))
files=[]
for p in sorted(OUT.rglob('*')):
    if not p.is_file() or any(x in ['local-evidence'] or x.startswith('remote-readback-') for x in p.parts): continue
    if p.name in ['package-manifest.json','core-remote-readback.json']: continue
    b=p.read_bytes();files.append(dict(path=p.relative_to(ROOT).as_posix(),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),
        git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),mode='100644',type='blob'))
write('package-manifest.json',dict(kind='FINITE_SEMANTIC_REVIEW_PAYLOAD_MANIFEST',candidate_commit=CAND,files=files,
   excluded=['package-manifest.json (no self-hash)','core-remote-readback.json (later publication proof)','ignored fresh remote object stores','local-evidence/final-remote-readback.json (external final readback; final response binds final commit/tree)'],
   own_git_tree_binding='External real commit/tree after commit, never a prefilled self identity',
   signature_scope='Static candidate PASS; actual configuration UNVERIFIED; not integratedPASS/acceptance/CLOSED'))
print(json.dumps(dict(verdict='PASS',records=len(records),configuration='UNVERIFIED',manifested_semantic_payloads=len(files),reference_model_host_execution=0),ensure_ascii=False))
