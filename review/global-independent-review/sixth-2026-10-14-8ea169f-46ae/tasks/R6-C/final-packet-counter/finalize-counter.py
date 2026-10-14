import collections, datetime, hashlib, json, shutil
from pathlib import Path

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
BASE = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'
OUT = BASE / 'tasks/R6-C'
b = OUT / 'final-packet-counter'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
binding = json.loads((b / 'input-binding.json').read_text())
for v in binding['files']:
    assert hashlib.sha256((ROOT / v['path']).read_bytes()).hexdigest() == v['sha256'], v['path']
records = json.loads((b / 'findings__normative-records.json').read_text())
previous = {q['id']:q for q in json.loads((b / 'snapshot-v1-64/findings__normative-records.json').read_text())}
current = {q['id']:q for q in records}
batch = json.loads((b / 'handoff__batch-assignment.json').read_text())
structure = json.loads((b / 'structure-validation.json').read_text())
graph = json.loads((b / 'graph-validation.json').read_text())
assert not structure['issues'] and not graph['issues']
assert len(current) == 65 and collections.Counter(q['identity_and_verdict']['classification'] for q in records) == {'required':56,'optional':8,'no_required_revision':1}
assert all(previous[k]['original_full_proposal'] == current[k]['original_full_proposal'] for k in previous)
assert all(q['premises_and_counterexample']['evidence_levels_and_execution'] for q in records)
assert all(q == current[q['id']] for batchitem in batch['batches'] for q in batchitem['scope_contracts'])
ledger = [json.loads(line) for line in (b / 'semantic-reading-ledger-v1.jsonl').read_text().splitlines()]
assessments = [json.loads(line) for line in (b / 'semantic-assessments-v1.jsonl').read_text().splitlines()]
changes = []
for q in records:
    k = q['id']
    fields = [name for name in ['identity_and_verdict','premises_and_counterexample','minimum_revision_contract','acceptance_and_regression'] if k not in previous or q[name] != previous[k][name]]
    if fields:
        ledger.append({'record_id':k,'persisted_at':now,'status':'REVISED_FIELDS_ACTUALLY_READ','snapshot_sha256':binding['files'][0]['sha256'],'fields':fields,'qualification':'Exact revised semantic fields and added record read from bounded tool output; original64 unchanged fullproposal preservation is a mechanical check, not new reading.'})
        changes.append({'id':k,'fields':fields})
        for a in assessments:
            if a['id']==k:
                a['current_scope_review']='Revised65 packet: reported scope/evidence-field issue resolved; original assessment above retained as old-stage evidence.'
                a['current_snapshot_sha256']=binding['files'][0]['sha256']
assessments.append({'id':'R6-C-P02','root_classification_preserved':'optional','assessment':'Source RGBA request known, final rendered white/cyan pixels unknown; full/partial/no-bar/time controls and audio/flash prefix remain. No primary batch, no host or reference execution promoted.','scope':'REVISED_PACKET_AND_C_OWN_OBJECTS_SOURCE_FACT_JOIN','C_reference_execution':0,'not_required_self_adjudication':True})
(b / 'semantic-reading-ledger.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in ledger))
(b / 'semantic-assessments.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in assessments))
issues = json.loads((b / 'semantic-findings-in-progress.json').read_text())['notes']
resolutions = {
    'C-PACKET-01':'C001 acceptance[3] now explicitly local handler false; later intention handlers continue.',
    'C-PACKET-02':'C002 input_domain now common / next_menu_vector slowerU / queued_execution_vector fasterU with prior and legally preselected TACKLE.',
    'C-PACKET-03':'C002 primary_contract and formal locator order now WP40:82–84; WP50 remains correct local consumer association.',
    'C-PACKET-04':'AN007 binding rule and acceptance now mandatory approximate0.3333/0.6666 default points only; general float recurrence is separate optional facet.',
    'C-PACKET-05':'All six required D evidence-layer fields populated from actual static/not-executed limits; aggregate validation counts not assigned to proposals. Optional D fields also filled without mandatory promotion.'
}
for issue in issues:
    issue['status']='RESOLVED_BY_ROOT_REVISED_PACKET_REVIEWED'
    issue['resolution']=resolutions[issue['counter_id']]
    issue['verified_at']=now
for rel in ['findings/policy-records.json','findings/optional-facets.json']:
    raw=(BASE/rel).read_bytes()
    (b/rel.replace('/','__')).write_bytes(raw)
policies=json.loads((b/'findings__policy-records.json').read_text())
facets=json.loads((b/'findings__optional-facets.json').read_text())
assert policies['count']==7 and policies['historical_policies']==6 and policies['new_policies']==1
assert all(not v['required_in_update'] for v in policies['records'])
assert set(v['id'] for v in policies['records']).isdisjoint(batch['unique_primary_batch'])
assert len(facets)==1 and facets[0]['classification']=='optional'
counter={'at':now,'reviewer':'R6-C /root/combat_review','status':'CURRENT_REVISED_PACKET_SUPPORTED_WITH_RETAINED_LIMITS','input_binding':binding,'normative_counts':{'total':65,'required':56,'optional':8,'no_required_revision':1},'semantic_review':{'old64_projection_records_actually_read':64,'required_source_annotations_consumer_reason_negative_failure_and_evidence_fields_actually_read':56,'revised_record_field_groups_actually_read':changes,'added_optional_record_actually_read':'R6-C-P02','original64_full_proposals_unchanged':True,'external_source_fullread_claim':False,'C_proposer_findings_self_required_adjudication':False,'scope':'Independent review of root packet contracts. C own core/battler/scene/handlers source joins remain personal fresh evidence; other domains retain their actual named readers and independent counters.'},'structure':structure,'graphs':graph,'semantic_packet_issues':issues,'unresolved_packet_issues':[],'batch':{'unique_required_primary':56,'batches':14,'formal_paths':54,'all56_scope_contracts_byte_structurally_equal_current_records':True,'optional_or_policy_in_primary':0,'withdrawn_UI_PARTY004_in_primary':False,'C_AF001_only_merged_with':'GR6-F-V001','variant_canonical_ids_retained':True,'formal_solewriter':'R6-I','actual_author_reviewer_execution':'NOT_STARTED; distinct logical roles are planning identities, not verified future independent reviewer execution'},'optional_and_policy_boundary':{'optional_records':8,'optional_float_facets':1,'historical_policies':6,'new_profile_policy':1,'policy_count':7,'new_profile_policy_semantic_read':'GR6-POL-001 whole record read; legacy6 only IDs/count/nonrequired status checked here. Native embedded-profile selection remains unknown, O nonproposer policy counter separately owned.','all_excluded_from_required_primary':True},'execution':{'C_reference_execution':0,'C_independent_behavior_model':0,'C_complete_host':0,'validation':'Text/identity/graph and static contract checks only; named external isolated evidence retains its owner and surrogate limits.'},'source_formal_public_packet_mutations_by_C':False,'root_required_authority_preserved':True,'not_authorization_to_start_update_or_close_formal':True}
(b/'counter.json').write_text(json.dumps(counter,ensure_ascii=False,indent=2)+'\n')
report='''# R6-C 最终裁决与批次独立反证

修订后的65条裁决包审查完成：56 required、8 optional、1 no_required_revision。原64完整提案保存，五个packet精度/层字段问题均由root修订并经本任务实际回读，当前未解决packet问题0。

C001洞前指向仅当前handler返回false，后续意愿仍继续；C002慢U菜单与快U已登记执行夹具分列，主定位WP40:82–84、WP50保正确本地事实；AN007必修仅默认approx控制点，浮点递推单列optional。六个D required补SOURCE_STATIC/DERIVED_VECTOR和实际工具限制，未把全队探针分摊为这些提案的参考执行。

实际语义阅读为原64条规范字段投影，以及56必修的source语义注释、必要消费者理由、负证据、失败/取消/部分提交和证据层字段；随后精确读修订字段与新增R6-C-P02。C主域源事实有本轮本人全文证据，其余领域保留当前具名reader/counter，不能据本报告宣称本人重读全部外域源码。982个嵌套定位的当前bytes/SHA/blob/行或具名材料位置校验0问题；该结构结果不替语义阅读。

56必修各进唯一主批，14批、54正式文件；全部scope_contracts与当前裁决一致。24共享文件冲突对及接收关系准确，100节点/110边依赖图无环，实际正式写者仅R6-I。28具名作者/审者是未启动逻辑角色，不作为已执行的独立审查。UI-PARTY-004保持撤销，C_AF001只并F-V001；8可选、1浮点可选facet及7独立policy均不进入必修主批。

新EXP闪光项限定RGBA请求参数，最终白色/青色像素仍未知。GR6-POL-001整条政策边界已读，只选择未来旧剖面兼容输入域，保留实际native选择未知；其O非提出者政策反证另归O。C参考/独立玩法模型/完整host运行均0，公共packet及正式/spec/reference未修改。候选审查、整合后独立审查、接口/历史回归与正式接受仍是未来逐项门，不因本审查自动CLOSED。

完整证据入口：counter.json、input-binding.json、structure-validation.json、locator-checks.jsonl、nonempty-required-checks.jsonl、graph-validation.json、semantic-reading-ledger.jsonl、semantic-assessments.jsonl。原64快照、旧语义意见与校验器格式错误阶段保留，未改写成参考缺陷。
'''
(b/'report.md').write_text(report)
# Current main-task metadata only; immutable prior stage copies retained.
hist=OUT/'history'/('phase-packet-final-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
hist.mkdir(parents=True,exist_ok=True)
for name in ['task-status.json','primary-freeze.json','report.md','file-list.json']:
    shutil.copy2(OUT/name,hist/name)
status=json.loads((OUT/'task-status.json').read_text())
status.update({'state':'ASSIGNED_COMBAT_SCENE_AND_FINAL_PACKET_REVIEW_COMPLETE','last_updated':now,'next':'Root final aggregation / future update remains separately unstarted','packet_counter_complete':True,'packet_unresolved':0})
status['mapping']['read_complete']=True
status['external_evidence_received']['R6-CA']='Full20source/8formal actual-reader receipt integrated; 24 stubbed reference handler cases owner-labelled, not C execution.'
status['counts']['K_exact_vector_receipts']=116
status['counts']['K_imported_source_identity_paths']=59
status['packet_counter']={'path':str((b/'counter.json').relative_to(ROOT)),'records':65,'required':56,'optional':8,'batches':14,'nested_locators':982,'structure_issues':0,'semantic_unresolved':0}
(OUT/'task-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
freeze=json.loads((OUT/'primary-freeze.json').read_text())
freeze['packet_review_completed_at']=now
freeze['packet_counter']=status['packet_counter']
freeze['exact_K_116_receipt']='received-K-exact116.json'
(OUT/'primary-freeze.json').write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n')
main_report=(OUT/'report.md').read_text()
main_report=main_report.replace('下一独立工作为final-packet-counter/根裁决与批次完整性核验；不得据结构校验自动接受语义，不修改公共文件。','final-packet-counter/根裁决与批次独立核验已完成；65条规范包、56必修14主批及982定位已检查，五个精度/层字段问题已由root修订并回读。结构结果不替语义、未修改公共文件。')
main_report+='\n## 最终证据追加（'+now+'）\n\nK最新116逐向量id/前提/预期/consumer接合与具名source区间已实际投影读完，精确formal行/block/hash及59来源身份核对保存received-K-exact116.json，并附每条vector。此接收不增加C源全文或执行credit。主域实际pending仍0；独立packet counter实际pending0，完整host/global131篇批准仍不由C宣告。\n'
(OUT/'report.md').write_text(main_report)
with (OUT/'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps({'at':now,'path':str((b/'findings__normative-records.json').relative_to(ROOT)),'status':'FINAL_PACKET_SEMANTIC_PROJECTION_AND_REVISED_FIELDS_READ','logical_count':65,'ledger':str((b/'semantic-reading-ledger.jsonl').relative_to(ROOT)),'semantic_summary':'56mandatory scope preserved, 8optional/1withdrawn separated; five packet precision/layer findings rootfixed and actualrechecked; newEXP requestvsrendering separated; original64 full proposals unchanged.','verification':'982identitylocators/56unique14batches/24fileoverlaps/100node110edgeDAG/toolscopes validated, not source-reading substitute or execution/authorization.','evidence':'SOURCE_STATIC_PACKET + TOOL_VALIDATION_TEXT_ONLY','new_source_fullread_credit':0,'reference_execution':0},ensure_ascii=False)+'\n')
with (OUT/'command-log.jsonl').open('a') as f:
    for name in ['final-packet-counter/write-semantic-v1.py','final-packet-counter/validate-structure.py','final-packet-counter/validate-graphs.py','final-packet-counter/finalize-counter.py']:
        f.write(json.dumps({'at':now,'command':'python3 '+str((OUT/name).relative_to(ROOT)),'script_sha256':hashlib.sha256((OUT/name).read_bytes()).hexdigest(),'operation':'ACTUAL_STATIC_AUDIT_SCRIPT_EXECUTION','C_reference_execution':0,'note':'Recorded at final persistence; tool transcript preserves call sequence, not reconstructed per-call wall time'},ensure_ascii=False)+'\n')
    f.write(json.dumps({'at':now,'operation':'AUDIT_ERROR_CORRECTION','details':'policy-records is dict, initial [-1] shape assumption raised KeyError before any mutation; retried records[-1] and read complete new policy. Finalizer initially queried issue_count which is stdout summary only, persisted structure uses issues array; KeyError before any mutation, corrected to actual schema. A whole changed-record output was truncated; only bounded revised field outputs count as actual reading. No source/spec defect or runtime credit.'},ensure_ascii=False)+'\n')
files=[]
for path in sorted(OUT.rglob('*')):
    if not path.is_file() or path==OUT/'file-list.json':continue
    data=path.read_bytes()
    files.append({'path':str(path.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'history': '/history/'in str(path)or'/snapshot-v1-64/'in str(path)})
manifest={'at':now,'directory':str(OUT),'file_count_including_self':len(files)+1,'self_manifest':'file-list.json (not self-hashed)','files':files,'primary_pending':0,'packet_pending':0,'source_formal_public_modified':False}
(OUT/'file-list.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'completed_at':now,'task_file_count':len(files)+1,'primary_pending':0,'packet_pending':0,'records':65,'required':56,'optional':8,'batches':14,'nested_locators':982,'all_original64_full_proposals_preserved':True,'unresolved':0}))
