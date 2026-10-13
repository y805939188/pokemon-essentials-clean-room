"""Audit publication and JSON/anchor preservation checks only; no behavior execution."""
import collections
import datetime
from followup_triage_common import *

dispositions=read('followup-partial-dispositions.json')
draft=read('followup-partial-new-findings-draft.json')
overrides=read('followup-partial-mapping-overrides.json')
assert len(dispositions['records'])==60
assert {r['record_index'] for r in dispositions['records']}==set(range(60))
assert {r['capability_id'] for r in dispositions['records']}=={r['capability_id'] for r in INPUT}
assert all(r['finite_disposition_complete'] and not r['pending_work_in_this_finite_review'] for r in dispositions['records'])
assert len(overrides['overrides'])==60
assert read('followup-partial-triage-input.json')['source_sha256']==BASE['original_files']['source-to-spec.json']
for name,digest in BASE['original_files'].items():
    assert sha(OUT/name)==digest,('prepublication input changed',name)
assert sha(ROOT/CANON_PATH)==BASE['canonical_sha256']

required='id title module severity disposition status reviewer category source_baseline specification_baseline source_anchors spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change affected_files shared_contracts acceptance_criteria dependencies related_capabilities related_findings root_cause_group priority batch_owner history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
new=draft['findings']
assert len(new)==24
assert [f['id'] for f in new]==[f'GR5-M01-{i:03d}' for i in range(8,32)]
assert all(all(k in f for k in required) for f in new)
assert all(f['status']=='candidate_pending_independent_counterevidence' and f['disposition']=='unresolved' for f in new)
assert all(f['execution_status']['followup']=='NOT_EXECUTED' for f in new)
linked={i for r in dispositions['records'] for i in r['new_finding_ids']}
assert linked=={f['id'] for f in new}
for r in dispositions['records']:
    assert r['main_review_record_anchor']['capability_id']==r['capability_id']
    assert OLD[int(r['main_review_record_anchor']['json_pointer'].split('/')[-1])]['capability_id']==r['capability_id']
    for identity in r['existing_finding_ids']:assert identity in {x['id'] for x in CANON}
    for p in r['subscope_dispositions']:
        for f in p['existing_findings']:
            current=next(x for x in CANON if x['id']==f['id'])
            assert (f['status'],f['disposition'],f['severity'])==(current['status'],current['disposition'],current['severity'])

errors=[]
lengths={}
def anchor_check(x,where):
    if isinstance(x,dict):
        path=x.get('path');line=x.get('lines')
        if isinstance(path,str) and path.startswith(('Data/','PBS/','Text_english_core/','deliverables/','specs/','analysis/')):
            p=(REF/path) if path.startswith(('Data/','PBS/','Text_english_core/')) else (ROOT/path)
            if not p.is_file():errors.append((where,'missing',path))
            elif isinstance(line,list) and len(line)==2 and all(isinstance(n,int) for n in line):
                if path not in lengths:lengths[path]=len(p.read_text().splitlines())
                if not 1<=line[0]<=line[1]<=lengths[path]:errors.append((where,'range',path,line))
        for k,v in x.items():anchor_check(v,where+'.'+k)
    elif isinstance(x,list):
        for i,v in enumerate(x):anchor_check(v,where+f'[{i}]')
for name,value in [('dispositions',dispositions),('new_findings',new),('overrides',overrides),('evidence',read('followup-partial-evidence.json'))]:
    anchor_check(value,name)
assert not errors,errors

now=datetime.datetime.now(datetime.timezone.utc).isoformat()
existing=read('findings.json')
old7=copy.deepcopy(existing['findings'])
assert len(old7)==BASE['original_findings_count']==7
assert hashlib.sha256(json.dumps(old7,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==BASE['original_findings_semantic_sha256']
existing['findings'].extend(new)
write('findings.json',existing)
assert read('findings.json')['findings'][:7]==old7

dispositions.update(complete=True,completed_at=now,
    counts=dict(input_records=60,records_with_new_candidates=42,records_only_reusing_existing_findings=9,
                records_without_finding_route=9,new_unique_candidates=24,new_severity=dict(collections.Counter(f['severity'] for f in new)),
                independent_counterevidence_pending_for_new_candidates=24,final_new_required_signed=0),
    canonical_decision_index=[canon(i,'旧ID最终有界裁决整体保持，本次不重开。') for i in range(1,8)],
    pending_input_records=[],scope_complete='All60 finite records substantively disposed; new-candidate counterevidence is a subsequent different-reviewer task, not unfinished reading here.')
write('followup-partial-dispositions.json',dispositions)
draft.update(complete=True,publication='All24 appended to findings.json after original7; still provisional, not independently adjudicated.')
write('followup-partial-new-findings-draft.json',draft)

candidate_table='\n'.join(f'| {f["id"]} | {f["severity"]} | {f["title"]} |' for f in new)
appendix=f'''

---

## 有限 partial/unresolved 后继处置（{now}）

**本次 complete=true：仅对 `followup-partial-triage-input.json` 的60条记录完成实质处置。** 没有重做全库/PBS/语料审读，没有运行参考、行为模型、场景、编译器、编辑器或生成器，没有更新正式规格。请求 gpt-6-astra / ultra / service_tier=default、禁Fast保持；实际回显仍为 **UNVERIFIED**。

旧001–007的最新判断以母汇总者 [canonical-findings.json](../../counterevidence/root-M01/canonical-findings.json) 为准：**001–006 required，007 optional**，并采用其中的严重度与子范围更正。上文原阶段“七条均待反证、最终required为0”保留为当时记录，不再作为这些旧ID的最新处置。本后继没有重开或改写原七条内容。

[followup-partial-dispositions.json](followup-partial-dispositions.json) 为每个输入给出主审record锚、源/规格锚、子范围去向及状态理由：42条连接新增候选（可同时复用旧ID），9条仅复用旧发现，9条没有发现去向、按现有合同或定义/政策边界收口。别名/消费者投影只指向唯一主规则，不按行数增加能力或发现数。阅读完成没有被自动换成supported。

重要反证与更正已记录在 [专门后继覆盖](followup-partial-mapping-overrides.json)：WP18正式54行/原稿55行已有明确形态继承；WP74§15–16已有完整映射写入门；WP51§2已有资金30/技能随资金。另修正审查自身两处概括：过滤的是空节名，不是所有空内容节；旧复数进化表先建立，单数条目追加，**不是单数覆盖复数**。旧source-to-spec、spec-to-source和完整reading-coverage的原字节保持，修正没有无痕回填。地图名消费者的错误附表路径及005的旧锚点亦只在后继更正。

新增 **GR5-M01-008～031共24条候选（5条P2、19条P3）**，已追加至 [findings.json](findings.json)。全部为 `unresolved / candidate_pending_independent_counterevidence`；没有自签任何新增required。它们限于正面源事实支持的作者输入、默认、失败、生成/反写或具名可见消费结果，不把所有辅助方法、缓存、等价输出样式或任意内部坏状态都列成产品必修。每项具备完整字段、正常/边界对照、实际反证、静态/运行分层与独立政策说明；由母任务派非原提出者反证。

| 新候选 | 级别 | 具名范围 |
| --- | --- | --- |
{candidate_table}

仅保留定义/政策边界而不新增的具体例子包括：无公开热更新承诺的缓存重试细节、枚举承载容器/反射方式、有效连接的等价文本规范式、区域图鉴族换行分组、元数据继承值物化、地牢派生映射的内部起源标志、非作者非负版本模式下的任意直接构造负版本、未承诺的备份组合/自动迁移。它们的源事实仍在逐记录处置中，不因缺默认调用者被说成不存在。

[followup-partial-evidence.json](followup-partial-evidence.json) 区分复用的完整阅读证明与本次精准补读；[followup-partial-validation.json](followup-partial-validation.json) 只核对产物格式、锚点、引用及保留性，不是行为执行。本次有限输入没有未处置行；下一步是新增候选的独立反证，不是等待用户决定是否补完整范围。
'''
report=OUT/'report.md'
old_report_bytes=report.read_bytes()
assert hashlib.sha256(old_report_bytes).hexdigest()==BASE['original_files']['report.md']
with report.open('a') as f:f.write(appendix)
assert hashlib.sha256(report.read_bytes()[:len(old_report_bytes)]).hexdigest()==BASE['original_files']['report.md']

preserved={name:sha(OUT/name)==digest for name,digest in BASE['original_files'].items() if name not in ('findings.json','report.md')}
assert all(preserved.values())
validation=dict(schema_version='gr5.review.v1',module='M01',result='PASS',errors=[],
    scope='Audit JSON schema/record identity/anchor ranges/canonical refs and preservation only. Not reference/model/vector/author-tool execution.',
    finite_records=60,unique_new_candidates=24,new_candidates_full_schema=True,
    original_seven_findings_semantically_unchanged=True,
    original_seven_semantic_sha256=BASE['original_findings_semantic_sha256'],
    original_report_prefix_unchanged=True,original_report_bytes=len(old_report_bytes),preserved_files=preserved,
    canonical_file_unchanged=sha(ROOT/CANON_PATH)==BASE['canonical_sha256'],
    model_parameters_actual='UNVERIFIED',timestamp=now)
write('followup-partial-validation.json',validation)
write('followup-partial-progress.json',dict(schema_version='gr5.review.v1',module='M01',complete=True,
    total_records=60,disposed_records=60,pending_records=[],phase='finite partial disposition complete',completed_at=now,
    routes=dispositions['counts'],existing_final_decisions='001–006 required;007 optional; bounded canonical reuse, no reopening',
    new_ids='GR5-M01-008..031',new_status='candidate_pending_independent_counterevidence',
    next_owner_action='mother task assigns a different reviewer for the24 new candidates',
    execution_status='STATIC_ONLY; reference/model/vector/compiler/generator/UI not executed',model_parameters_actual='UNVERIFIED',
    unchanged=['source-to-spec.json','spec-to-source.json','reading-coverage.json','original7 findings content'],
    successor_override='followup-partial-mapping-overrides.json',validation='followup-partial-validation.json: PASS (artifact-only)'))
print('Published60 dispositions;24 new provisional candidates; old7/proof/mappings preserved; complete=true')
