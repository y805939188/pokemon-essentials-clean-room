from current_evidence import *
from datetime import datetime,timezone
from collections import Counter
V=json.loads((HERE/'artifact-validation.json').read_text());assert V['structural_checks_passed'] and not V['issues']
L=json.loads((HERE/'regression-legacy-scope.json').read_text());assert L['mapping_complete'] and len(L['controls'])==229 and len(L['contributions'])==341
assert all(r['current_R5_semantic_review']['mapping_complete'] for r in L['contributions'])
O=json.loads((HERE/'original-comparison-joins.json').read_text());assert all(r['status']=='supported' for r in O['records'])
finite={}
for fn in ['regression-fourth-17.json','regression-third-23.json']:
 d=json.loads((HERE/fn).read_text());d['complete']=True;d['completion_scope']='Every assigned finite criterion actually reviewed against fixed R/B5 and fresh current source/spec/reading records. Partial is an observed contract result, not unread scope.'
 for i,r in enumerate(d['records']):
  finite[r['id']]={'file':fn,'pointer':f'/records/{i}','record':r}
  j=r['current_R5_semantic_review']['fresh_global_review_join'];j['status']='supported';j['evidence_level']='supported_static_address_and_scope_join';j['join_complete']=True;j['semantic_result']=r['current_R5_semantic_review']['status'];j['REG_applicability_review']='Curated current capability roles and exact body/vector/reading record addresses reviewed; primary wider partial/missing/unresolved scopes remain distinct.'
  for c in r['criteria']:c['current_R5_semantic_review']['fresh_record_join']={'file':fn,'pointer':f'/records/{i}/current_R5_semantic_review/fresh_global_review_join'}
 save(fn,d)
for r in L['contributions']:
 nav=r['current_B5_navigation'];nav['mapping_status']='current_qualified_scope_bound_and_reviewed'
 nav['historical_payload_context_without_authored_selector']=nav.pop('paths_still_needing_finite_selector',[])
 for a in nav['clause_candidates']:
  a.pop('semantic_status',None);a['address_status']='bound_current_section_or_vector';a['scope_boundary']='Location of the explicit manual local comparison; unrelated facts elsewhere in this range are not a REG whole-file signature.'
 r['current_R5_semantic_review']['current_clause_locator_resolution']='current_B5_navigation.clause_candidates are exact B5 section/vector addresses; supported applies only accepted_local_scope_fields + manual_scope_comparison. Historical payload context is not silently treated as authored scope.'
L['complete']=True;L['completion_scope']='All229 original identities and341 exact local contributions mapped to current clauses/source facts/fresh primary results with original qualification; this is not a global no-gap verdict or source-first replacement.'
save('regression-legacy-scope.json',L)
for fn,key in [('source-to-spec.json','capabilities'),('spec-to-source.json','clauses')]:
 d=json.loads((HERE/fn).read_text());d['complete']=True;d['counting_rule']='REG records are historical finite-control projections, not new product capabilities. Unique shared identities remain with primary owners.';d['legacy_mapping']='regression-legacy-scope.json';d['primary_fresh_records']='fresh-evidence-snapshots.json';d['primary_original_comparisons']='original-comparison-joins.json';d['primary_source_reading']='fresh-source-ledger.json'
 for r in d[key]:
  f=finite[r['historical_control']];r['fresh_current_evidence']={'file':f['file'],'pointer':f['pointer']+'/current_R5_semantic_review/fresh_global_review_join'};r['count_as_product_capability']=False;r['review_extent']='complete_within_finite_historical_scope';r['wider_source_intervals']='See reading-coverage.json unreviewed intervals and exact primary domain ledger; not signed by REG.'
 save(fn,d)
coverage=json.loads((HERE/'reading-coverage.json').read_text());coverage['complete']=True;coverage['completion_scope']='REG direct finite source/caller/spec slices plus manually reviewed legacy scope/current-primary joins. Full domain source bodies were read by their primary reviewers; REG does not rebrand those as its own direct reading.'
coverage['legacy_scope_review']={'controls':229,'contributions':341,'manual_assessment_file':'scope-assessments.json','source_fact_ledger':'fresh-source-ledger.json','current_clause_snapshots':'fresh-evidence-snapshots.json','original_comparison_records':'original-comparison-joins.json','qualifier':'These counts are scope/navigation denominators, never proof of semantic completion by themselves.'}
coverage['historical_inputs']=[
 {'path':R4PATH,'version':B,'frozen_criteria_version':'1dd05964f59772886de9b808a929c168c73fa184','semantic_scope':'All17/76 criterion wording, premises/exclusions and exact scoped navigation; historical actual verdicts excluded as R5 evidence.','review_extent':'partial','unreviewed_scope':'Retired administrative gate reacceptance deliberately outside scope','material_availability':'available_text','evidence_level':'HISTORICAL_IDENTITY_QUALIFICATION_ONLY'},
 {'path':R3PATH,'version':B,'semantic_scope':'All23/76 accepted finite criteria, original accepted scope, current clauses/cases; OPTIONAL and NO_REQUIRED exclusions preserved.','review_extent':'partial','unreviewed_scope':'Historical runtime/acceptance claims not transferred','material_availability':'available_text','evidence_level':'HISTORICAL_IDENTITY_QUALIFICATION_ONLY'},
 {'path':'review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/all229-closure-records.json','version':'167296dbe9e2384627b0ed696e87aeb01f211252','semantic_scope':'All229 original/approved identity bindings and all scoped contributor keys','review_extent':'partial','unreviewed_scope':'Historical CLOSED is not a new semantic verdict','material_availability':'available_text','evidence_level':'HISTORICAL_IDENTITY_QUALIFICATION_ONLY'},
 {'path':'review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/all341-public-source-map.json','version':'167296dbe9e2384627b0ed696e87aeb01f211252','semantic_scope':'All341 exact batch/ID/candidate/actual/receipt identities; finite disposition scope resolved via exact pointer for every record','review_extent':'partial','unreviewed_scope':'Retired administrative receipts not recursively audited','material_availability':'available_text','evidence_level':'HISTORICAL_IDENTITY_QUALIFICATION_ONLY'},
 {'path':'review/remediation/20261003-prepare/batches/B21/author-draft-1/traceability.json','version':'e58486178e746273fb6fab55df00722807f1dc44','semantic_scope':'All14 author_revision/affected_boundary/static_case/new_output fields; current_consumer_nodes are navigation, not whole-file semantic signatures','review_extent':'partial','unreviewed_scope':'Nested historical approval bodies reused by exact qualification only','material_availability':'available_text_at_fixed_archive','evidence_level':'CURRENT_EFFECTIVE_QUALIFIED_SCOPE'},
 {'path':'review/remediation/20261003-prepare/batches/B21/author-draft-1/static-cases.json','version':'e58486178e746273fb6fab55df00722807f1dc44','semantic_scope':'All14 finite case IDs/preconditions/expected results; B21-CASE-DISPATCH OldRod scope distinguished from interpreter common-event receiver','review_extent':'full','unreviewed_scope':[],'material_availability':'available_text_at_fixed_archive','evidence_level':'CURRENT_STATIC_DESIGN_NOT_EXECUTED'}]
for module,name,scope in [
 ('M03','source-to-spec.json','All48 bounded capability comparisons including final EVENT_STATE_STORAGE; command/route inverse clauses joined by current IDs.'),
 ('M05','reading-coverage.json','All semantic_segments rules/comparison fields in source records0–45 read; necessary other creator/owner/item/source anchors followed through exact current primary records. This does not claim direct REG reading of all142 source bodies.'),
 ('M05','source-to-spec.json','All38 final capability comparisons read; final added acquisition/ability anchors and updated original conclusions compared before refreshing hashes.'),
 ('M06','reading-coverage.json','All95 entries_and_rules/incremental comparison fields read; long PBS physical row-address arrays are navigation, not fresh REG data execution.'),
 ('M08','original-comparison.json','All14 completed original comparison files and all distinct per-range/table/vector disposition texts/additional identity qualifications read. Original raw source-read claims remain M08; no historical approval transfer.'),
 ('M09','source-to-spec.json','All45 capability identities and all primary semantic segment comparisons in source_paths SRC001–051 reviewed; registration/source segment pointers resolved precisely.'),
 ('M10','source-to-spec.json','All45 capability comparisons and all271 distinct semantic_ranges entry_and_rules reviewed; older pending notes interpreted with final precise mapping and independent narrowed candidates, not blindly reused.'),
 ('M11','source-to-spec.json','All86 bounded behavior_purpose comparisons read; new grid/multikey/slot timing and narrowed timing005 not transferred from legacy accepted cases.'),
 ('M12B','source-to-spec.json','All40 semantic_comparison fields and all123 unique source semantic_groups supporting_fact fields read, including defaults, cancellations, partial writes and inactive helpers.'),
 ('M12','source-to-spec.json','All25 root static semantic comparison groups read; root separate executions are not REG evidence of execution.'),
 ('C00','reading-coverage.json','All32 semantic_disposition records and14 effective supplement scope records reviewed; current/retired/optional provenance kept distinct. No current gameplay acceptance inherited from metadata.'),
 ('JXN','shared-interfaces.json','Canonical shared IDs/ownership reused solely for identity; REG24 consumer projections do not sign JXN pending whole chains.')]:
 p=HERE.parent/module/name;raw=p.read_bytes();coverage['fresh_review_inputs'].append({'path':str(p.relative_to(ROOT)),'sha256':digest(raw),'review_extent':'partial','semantic_scope':scope,'material_availability':'available_text','evidence_level':'FRESH_PRIMARY_STATIC_EVIDENCE_FIELDS','unreviewed_scope':'Any primary fields/foreign whole-domain proofs beyond the listed REG projection; direct R5 source body reading belongs named primary reviewers.'})
coverage['direct_reread_delta']='010-form-summary-overlap independently confirms WP18/66A current contradiction; no duplicate REG finding.'
save('reading-coverage.json',coverage)
F=json.loads((HERE/'findings.json').read_text());F['complete']=True;F['new_REG_candidates']=0;F['existing_candidate_scope_relationships']='history-relations.json';F['related_primary_candidates'][0]['current_independent_resolution']='counterevidence/root-M04/canonical-findings.json GR5-M04-002; independently confirmed with existing-contract credit';F['completion_scope']='No new root or duplicate finding manufactured; current Summary consistency residue and71 existing candidate/canonical history relationships supplied.';save('findings.json',F)
for fn in ['scope-assessments.json','original-comparison-joins.json','history-relations.json','shared-interfaces.json','fresh-evidence-snapshots.json','finite-fresh-snapshots.json','fresh-source-ledger.json']:
 d=json.loads((HERE/fn).read_text());d['complete']=True;d['completion_boundary']='Complete only for the REG assigned finite review and qualified mapping described by this artifact; no source runtime or foreign whole-module signature.';save(fn,d)
P=json.loads((HERE/'progress.json').read_text());P.update({'complete':True,'status':'complete_assigned_static_regression_and_scope_mapping','next_actual_scope':None,'pending_joins':[],'last_checkpoint':'011-final-qualified-joins','updated_at':datetime.now(timezone.utc).isoformat(),'counts':{'GR4_records':17,'GR4_criteria':76,'GR4_supported_criteria':75,'GR4_partial_current_consistency_criteria':1,'GR3_records':23,'GR3_criteria_supported_static':76,'legacy_controls_mapped':229,'scoped_contributions_mapped':341,'original_comparison_records':113,'shared_identity_REG_projections':24,'new_current_finding_history_relations':71,'new_REG_findings':0},'source_runtime_executions':0,'behavior_model_executions':0,'parent_integration':'Parent retains canonical severity/dedup and global JXN/coverage integration; REG scope is complete, no unfinished readable assigned slice concealed.'});save('progress.json',P)
(HERE/'progress.md').write_text('# REG 完成\n\ncomplete=true。固定B5/R；参数实际回显UNVERIFIED。纯静态，参考/行为模型执行均0。\n\nGR4 17项/76标准全部实际审读：75 supported_static，1项当前一致性partial（GR4-M04-001/C01，现有GR5-M04-002摘要投影）。上游WP18规则及IF向量成立，但WP66-A§8残留只读断言；不改历史CLOSED。\n\nGR3 23项/76标准supported_static；GR3-M09-001 OPTIONAL/U08未启动、GR3-M02-003 NO_REQUIRED保持。\n\n229控制/341局部贡献全部完成原身份/批次owner/局部资格/接受引用→B5当前条款→本轮源能力与主审证据映射。全341逐条人工比较说明、113原稿承接记录、24共享身份消费者投影、71新旧范围关系可读。六类纯行政/导航行以当前C00资格记录闭合，不伪造产品源能力。\n\n结构/指针/哈希/行界检查通过；不是行为执行。report.md和各regression矩阵为主入口。父会话仅继续其全局去重/批次汇总和JXN整合；REG无剩余实际阅读范围。\n')
(HERE/'report.md').write_text('''# REG 第五轮独立历史回归与资格映射

已完成分配范围，`complete=true`。固定规格 B5 `9366d9d17aaeac3b4414236468affa650fb3dd27`（正式树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`）；固定来源 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（树 `7589c800b61ba13a13040ed0d686979b80a84fd0`）。请求 astra/ultra/default，实际参数回显 `UNVERIFIED`。

| 有限审查范围 | 本轮结果 |
| --- | --- |
| GR4 17项／76标准 | 全部实际定点读源、必要调用者与B5条款；75 supported_static，1 current-consistency partial |
| GR3 23项／76标准 | 全部实际定点回归，76 supported_static |
| 旧229控制／341 scoped contributions | 全量逐条原ID、批次owner、具体范围、接受引用→当前条款／来源事实／本轮主审记录映射完成；支持仅限原具名资格 |
| 原稿承接 | 113个精确原稿比较记录；复用本轮主审的实际差异/逐节/表/向量结论，REG直接原稿阅读另在ledger标明 |
| 共享与新增范围 | 24个唯一共享身份的REG消费者投影；71个现有新候选／规范记录的新旧范围关系；不新增产品能力计数 |

两组76是不同分母。229控制、341局部贡献、原稿记录、条款／向量地址和产品能力也不互换。

## 当前一致性残留

`GR4-M04-001/C01`不能作为全合同一致通过：WP18 §3.4已正确规定摘要个体取图先求动态形态，但WP66-A §8（218、221行）仍断言显示不改成员。REG直接重读摘要调用链、个体取图、动态提交与FURFROU五日门：在原R4具名合法摘要前提下，t+432001先提交形态0并清时间戳，早于资源匹配。因此上游修订及IF边界向量仍成立，当前下游一致性为partial。

该范围与现有 `GR5-M04-002` 的摘要部分合并；PRISONBOTTLE是追加消费者范围。没有另建GR5-REG重复根，也没有证据称此矛盾在R4接受后新引入。历史CLOSED保持。

## 资格和证据边界

17／23项的判断来自本轮REG直接有限源审，不继承旧CLOSED/PASS。229／341按用户指定方式消费本轮各域source-first实际语义比较，并逐条审定本地适用范围；精确文件哈希、JSON指针、源范围和当前接收条款均可沿快照与ledger复核。源模块广域partial/missing/unresolved及其新GR5问题不被旧局部接受抹去。

READ_ONLY、NOT_AFFECTED、只改测试标号、只作导航、更正取证路径和中央资格后继分别保留。例如B02-C003仅缓存色调观察点，B17-C003仅L09第三标号；B08-A052的WP34只读依赖不转成作者全篇修订或整个ID签名。历史整批payload身份不是每条贡献的全文件语义范围。

`GR3-M09-001`仍OPTIONAL暂缓、U08未启动；`GR3-M02-003`仍NO_REQUIRED。M08 Shadow结论消费父审纠正：false为动画参数，不是关闭第三参数的伤害登记。M11新普通网格/同轮输入/老虎机索引和收窄后的时间锁定范围不能借旧尺寸或单键接受覆盖。

没有修改正式规格、reference、历史证据或共享报告；没有提交、推送、联网、安装或运行参考/行为模型。原R4及其它审者单列的执行均不计为REG执行。结构检查通过只证明地址、身份、分母及行界一致，不替代上述人工语义比较。

## 文件入口

- `regression-fourth-17.json`、`regression-third-23.json`：逐标准独立结论、原范围与精确fresh接点。
- `regression-legacy-scope.json`、`scope-assessments.json`：229／341全量资格和逐条实际比较；行政导航不是额外产品能力。
- `fresh-evidence-snapshots.json`、`finite-fresh-snapshots.json`、`fresh-source-ledger.json`：精确当前条款／能力／源阅读证据。
- `original-comparison-joins.json`、`history-relations.json`、`shared-interfaces.json`：原稿独有事实处置、新旧范围及唯一共享身份消费者。
- `reading-coverage.json`、`source-to-spec.json`、`spec-to-source.json`、`artifact-validation.json`：REG直接读段、主审复用边界和双向追溯。

父会话保留全局最终去重、严重度及批次汇总权。REG自身没有待补的可得分配阅读／join；JXN尚未签的完整链不由本报告代签。
''')
print('REG completed assigned review;17/76 and23/76 remain distinct,229/341 fully mapped,one R4 consistency residue linked.')
