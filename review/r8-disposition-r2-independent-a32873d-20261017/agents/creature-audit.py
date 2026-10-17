"""Read-only Git/JSON reconciliation for the allocated Creature R2 review.

This collects document evidence only. It does not execute reference/game/business code.
Semantic judgments below are the reviewer's findings after reading the cited source ranges.
"""
import collections
import copy
import datetime
import hashlib
import json
import pathlib
import subprocess

C = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
R1C = '5666b7b912e2fb79b5119283ee6a37401a7071db'
R1R = '8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8'
A = '908273093e1f6b27fc58249417675dd62d146224'
F = '0eee6d141f33758eda34bd8ebad94a3e2b617f5a'
P = 'planning/implementation-routing/r8-20261017/'
RP = 'review/r8-disposition-r1-independent-5666b7b-20261017/'
BASE = 'deliverables/final-specification-set/'
OUT = pathlib.Path(__file__).parent
receipts = []

def sha(b):
    return hashlib.sha256(b).hexdigest()

def git(*args):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    q = subprocess.run(['git', *args], capture_output=True)
    receipts.append(dict(argv=['git', *args], start_utc=start,
                         end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         exit_code=q.returncode, stdout_bytes=len(q.stdout),
                         stdout_sha256=sha(q.stdout), stderr=q.stderr.decode()))
    q.check_returncode()
    return q.stdout

def read(path, commit=C):
    return git('show', commit + ':' + path)

def j(path, commit=C):
    return json.loads(read(path, commit))

def fid(n):
    return f'FR-{n:06d}'

m = j(P + 'routing-manifest.json')
pm = j(P + 'routing-manifest.json', R1C)
sections = j(P + 'section-coverage.json')
prior_sections = j(P + 'section-coverage.json', R1C)
old = j(RP + 'agents/creature-results.json', R1R)
prior = {x['feature_id']: x for x in pm['features']}
current = {x['feature_id']: x for x in m['features']}
previous_results = {x['feature_id']: x for x in old['active_feature_results']}
ids = list(previous_results)
assert len(ids) == 122
primary_paths = [x['path'] for x in old['reading_ledger'][:18]]

required_prior = ['REPORT.md', 'findings.json', 'finding-results.json',
                  'feature-results.json', 'reading-coverage.json',
                  'agents/creature-report.md', 'agents/creature-results.json']
input_identities = []
parsed = {}
for path in required_prior:
    b = read(RP + path, R1R)
    local = pathlib.Path('/workspace/r8-disposition-r1-review') / RP / path
    assert b == local.read_bytes()
    if path.endswith('.json'):
        parsed[path] = json.loads(b)
    input_identities.append(dict(commit=R1R, path=RP + path, bytes=len(b),
                                 sha256=sha(b), physical_tree_matches_fixed_git=True,
                                 consumption='COMPLETE_STRUCTURED_PARSE_AND_ALLOCATED_SEMANTIC_RECONCILIATION' if path.endswith('.json') else 'COMPLETE_TEXT_READ'))

global_features = {x['feature_id']: x for x in parsed['feature-results.json']['active_feature_results']}
global_old = {x['feature_id']: x for x in parsed['feature-results.json']['old_feature_results']}
assert all(all(global_features[i].get(k) == v for k,v in previous_results[i].items()) for i in ids)
assert all(all(global_old[x['feature_id']].get(k) == v for k,v in x.items()) for x in old['old_feature_results'])
assert {x['finding_id'] for x in old['finding_results']} <= {x['finding_id'] for x in parsed['finding-results.json']['finding_results']}
assert next(x for x in parsed['findings.json']['findings'] if x.get('finding_id',x.get('id')) == 'R1-CRE-DEP-001')['cases'] == old['new_findings'][0]['cases']
global_reading={x['path']:x for x in parsed['reading-coverage.json']['documents']}
for x in old['reading_ledger'][:18]:
    g=global_reading[x['path']]
    assert g['current_identity']['sha256']==x['sha256']
    assert g['prior_full_reading_identity_match'] is True
    assert g['prior_full_reading_record']['sha256']==x['inherited_full_reading_credit']['sha256']

objects = []
for commit in [C, R1C, R1R, A, F, 'd62b41f4d620e50bb04c80a7505374bd284d8210',
               'a0352c7fba38391afc535525988245701d5ce202',
               'fd1df570cad987dc3852a3b958f03916e317f7fe',
               '4575e80d041ab0c74a42e2e36399d05791dbaa5b',
               '49a558f7d5498680ba88d532f3815e07d7844459']:
    objects.append(dict(commit=commit, verified=git('rev-parse', commit + '^{commit}').decode().strip(),
                        type=git('cat-file', '-t', commit).decode().strip()))

changed = {}
for i in ids:
    changed[i] = sorted(k for k in set(prior[i]) | set(current[i]) if prior[i].get(k) != current[i].get(k))
assert {i for i, fields in changed.items() if fields} == {fid(n) for n in [155,157,158,186,190,191,192]}
assert all(fields == ['dependencies', 'differences'] for fields in changed.values() if fields)
assert all(prior[i]['source'] == current[i]['source'] for i in ids)

fresh_primary = {
    'wp20-hp-status-moves-helditem.md': [[46,82],[121,171]],
    'wp24-player-trainers-partners.md': [[173,237]],
    'wp28-item-use-and-training.md': [[103,226],[276,294]],
}
text_by_path = {}
reading_ledger = []
for x in old['reading_ledger'][:18]:
    path = x['path']
    b = read(path, A)
    text_by_path[path] = b
    assert sha(b) == x['sha256']
    equalities = {commit: read(path, commit) == b for commit in [C,R1C,'fd1df570cad987dc3852a3b958f03916e317f7fe','4575e80d041ab0c74a42e2e36399d05791dbaa5b']}
    assert all(equalities.values())
    reading_ledger.append(dict(path=path, commit=A, bytes=len(b), line_count=len(b.decode().splitlines()),
                               sha256=sha(b), git_blob=git('rev-parse', A + ':' + path).decode().strip(),
                               primary_document=True, identical_fixed_commits=equalities,
                               new_semantic_read_ranges=fresh_primary.get(path.split('/')[-1], []),
                               inherited_full_reading_credit=dict(commit=R1R, path=RP+'agents/creature-results.json',
                                                                  pointer='/reading_ledger/'+str(old['reading_ledger'].index(x)),
                                                                  ranges=[[1,len(b.decode().splitlines())]],
                                                                  previous_fresh_ranges=x['new_semantic_read_ranges'],
                                                                  original_credit=x['inherited_full_reading_credit'],
                                                                  reason='固定908完整字节、R1 ledger身份与全部本域行完整字段已复核；115个R1 PASS整行相同。仅未变且未受影响facet继承，七变更行及同根因消费者另新读。'),
                               limitation='未把继承全文信用称作本轮全文新读。'))

consumer_ranges = {
    'engine-overworld/wp15-resource-matching-and-audio.md': [[129,190]],
    'engine-overworld/wp16-pre-battle-transitions.md': [[1,21]],
    'combat-requirements/wp39-battle-context-and-participants.md': [[47,195],[260,278]],
    'combat-requirements/wp40-commands-obedience-and-action-order.md': [[97,115]],
    'combat-requirements/wp41-switching-positioning-and-escape.md': [[152,176]],
    'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md': [[166,250]],
    'combat-requirements/wp45-weather-terrain-side-and-position-effects.md': [[1,177]],
    'pokemon-rules/wp21-dynamic-forms-and-display.md': [[185,249]],
    'pokemon-rules/wp22-mega-and-primal-reversion.md': [[76,90]],
    'pokemon-rules/wp38-capture-and-receiving.md': [[17,30]],
    'pokemon-rules/wp44-statuses-stat-stages-and-immunities.md': [[84,114]],
    'pokemon-rules/wp50-held-item-triggers-and-consumption.md': [[66,121]],
    'user-interface/wp66-a-party-and-summary-ui.md': [[66,100]],
    'user-interface/wp67-a-battle-interaction-and-presentation.md': [[132,163],[209,233]],
}
extra_consumers = []
for path, ranges in consumer_ranges.items():
    path = BASE + path
    b = read(path, A)
    extra_consumers.append(dict(path=path, commit=A, bytes=len(b), sha256=sha(b),
                                git_blob=git('rev-parse', A+':'+path).decode().strip(),
                                new_semantic_read_ranges=ranges, inherited_full_reading_credit=None,
                                limitation='仅此处列明新读区间，不声称本域以外整篇全文。'))

reasons = {
155: '完整WP24§5.4与WP15§6、WP16§1、WP39§7.5及WP67-A§8对照：355/726/733/682分别承播放与暂停、包装恢复/清预置、请求交付、捕获成功等待，旧伙伴/换人误用已清。',
157: '完整WP24§6.2与WP39§3.5/§4/§5对照：1/2/3准确承参与谓词、布局及业主队伍段；已删除WP10迁移的direct/feature误边。wp_refs仍是旧计划索引，不把WP10的保留当现行语义依赖。',
158: '完整WP24§6.3与WP42§7.1、WP21§4.3、WP22§6对照：32承伙伴存在即治疗及可败2/5的独立分支，464/473承一般形态/特殊还原；净化室749误边已清。',
186: 'WP40§4.2、WP67-A§5及捕获525的有效边已补，种植/驱虫误边已清；但direct_refs/1及FR32把“战后退款”交WP42§7。退款实际在正常战斗对象终局WP42§6/§6.0，§7是后续世界善后，仍错接阶段。',
190: 'WP20 HP、WP40物品登记、WP67-A目标/取消、WP66-A奶招及WP50主动/被动对照均真实；但direct_refs/2称WP42§7为“治疗/退款善后”，FR32实际全队治疗不是本节主动药品效果，且不退款。应删不相干治疗边或准确指正常终局§6/31说明退款。',
191: '完整WP28§5.2与WP20§5、WP40§4.2、WP67-A§5、WP50§4 L92对照：持久槽/PP成长、主动登记及选招取消、持物LEPPA例外分别准确；旧香/净化488误边已清。允许147经excluded739追达PP同步。',
192: 'WP40/UI、X阶级546、娃娃22、球525和特殊形态463的用途真实，教学/香/邮件误边已清；但direct_refs/3及FR40声称GuardSpec Mist建立/期限，所指WP45§7仅交换/清除等，真实5回合建立/期限在§6.2 L127，需FR39或等效正确锚点。',
}
failed = {fid(n) for n in [186,190,192]}
active_results = []
old_results = []
locator_checks = []
spans = []
for i in ids:
    f = current[i]
    pr = previous_results[i]
    changed_fields = changed[i]
    verdict = 'FAIL' if i in failed else 'PASS'
    reason = reasons.get(int(i[3:]), pr['reason'])
    method = 'COMPLETE_AFFECTED_SOURCE_UNIT_AND_REAL_CONSUMER_REREAD' if changed_fields else 'INHERITED_R1_PASS_AFTER_WHOLE_ROW_IDENTITY_AND_NONIMPACT_RECONCILIATION'
    refs = ['R2-CRE-DEP-001'] if i in failed else []
    scope = f['functional_scope']['line_ranges']
    loc = f['current_applicability']['locator']
    b = text_by_path[f['source']['document']]
    lines = b.decode().splitlines(keepends=True)
    unit = ''.join(''.join(lines[a-1:z]) for a,z in scope).encode()
    check = dict(feature_id=i, source_unchanged=prior[i]['source']==f['source'],
                 current_commit=f['current_applicability']['snapshot_commit'] if 'snapshot_commit' in f['current_applicability'] else None,
                 locator_ranges_match=scope==loc['line_ranges'], unit_sha256_match=sha(unit)==loc['unit_sha256'],
                 file_sha256_match=sha(b)==loc['file_sha256'])
    assert check['source_unchanged'] and check['locator_ranges_match'] and check['unit_sha256_match'] and check['file_sha256_match']
    locator_checks.append(check)
    active_results.append(dict(feature_id=i, r1_verdict=pr['verdict'], verdict=verdict,
                               candidate_pointer='/features/'+str(m['features'].index(f)),
                               reason=reason, affected_fields=changed_fields, review_mode=method,
                               destination_semantics='PASS', dependency_semantics=verdict,
                               finding_refs=refs, source=f['source'], functional_scope=f['functional_scope'],
                               source_identity_verified=True, r1_whole_row_equal=prior[i]==f,
                               dependencies=f['dependencies']))
    if i in global_old:
        old_results.append(dict(feature_id=i, r1_verdict=global_old[i]['new_verdict'],
                                old_verdict=global_old[i]['new_verdict'], new_verdict=verdict,
                                disposition='active', active=True, reason=reason, review_mode=method,
                                r1_whole_row_equal=prior[i]==f, affected_fields=changed_fields,
                                finding_refs=refs))
    for a,z in scope:
        spans.append((f['source']['document'],a,z,i))
assert len(old_results)==116 and len(active_results)==122
overlaps=[(i,k) for n,(p,a,z,i) in enumerate(spans) for q,b,y,k in spans[:n] if p==q and i!=k and max(a,b)<=min(z,y)]
assert not overlaps

def closure(values):
    pending=list(values); result=set()
    while pending:
        i=pending.pop()
        if i in result: continue
        result.add(i)
        if i in current: pending.extend(current[i]['functional_scope']['excluded_child_refs'])
    return sorted(result)

section_metadata_results=[]
for x in old['retired_metadata_results']:
    index=int(x['candidate_pointer'].split('/')[-1])
    s=sections['sections'][index]
    ps=prior_sections['sections'][index]
    assert s==ps
    assert s['path']==x['path'] and s['title']==x['title']
    assert s['feature_refs']==x['consumer_feature_refs']
    assert closure(s['feature_refs'])==x['effective_consumers_via_explicit_excluded_child_refs']
    section_metadata_results.append(dict(unit_kind='section-metadata', candidate_pointer=x['candidate_pointer'],
                                         path=x['path'], title=x['title'], r1_verdict=x['verdict'], verdict='PASS',
                                         source_lines=x['source_lines'], row_exactly_equal_r1=True,
                                         consumer_feature_refs=s['feature_refs'], metadata_refs=s['metadata_refs'],
                                         retired_feature_refs=s['retired_feature_refs'],
                                         effective_consumers_via_explicit_excluded_child_refs=closure(s['feature_refs']),
                                         reason=x['reason'], review_mode='INHERITED_R1_SECTION_RESULT_AFTER_FULL_SECTION_RECORD_IDENTITY_AND_CONSUMER_CLOSURE_CHECK',
                                         finding_refs=[]))
assert len(section_metadata_results)==158
assert not [f for f in m['retired_features'] if f['source']['document'] in primary_paths]
assert not [f for f in m['metadata_records'] if f['source']['document'] in primary_paths]

groups=[]
for g in old['finding_results']:
    r=copy.deepcopy(g)
    r['r1_verdict']=g['new_verdict']
    r['old_verdict']=g['new_verdict']
    r['new_verdict']='FAIL' if g['finding_id']=='CK-DEP-001' else 'PASS'
    r['review_mode']='ALL_13_ORIGINAL_CASES_RECONCILED_SEVEN_CHANGED_REREAD' if g['finding_id']=='CK-DEP-001' else 'INHERITED_AFTER_ALL_CASE_ROW_AND_SOURCE_IDENTITY_NONIMPACT_CHECK'
    for case in r['all_original_cases']:
        i=case.get('old_feature_id') or case.get('new_feature_id')
        if i:
            case['r1_verdict']=case['verdict']
            case['verdict']='FAIL' if i in failed else 'PASS'
            case['reason']=reasons.get(int(i[3:]),previous_results[i]['reason'])
            case['review_mode']='COMPLETE_SOURCE_CONSUMER_REREAD' if changed[i] else 'WHOLE_ROW_AND_SOURCE_IDENTICAL_R1'
    r['same_root_affected_PASS_evidence']='全部122行比较，仅七行dependencies/differences变；115个R1 PASS整行原样。WP42/WP45关联的147/158/186/187/190/192/204/207全部用途核对；187宽锚实际可达§6.0，147/204/207为PP/成长实际交界，未把宽粒度本身判FAIL。158正确外层伙伴治疗与186/190退款错层分开。'
    groups.append(r)

cases=[]
for n in [186,190,192]:
    i=fid(n); f=current[i]
    wrong_index={186:1,190:2,192:3}[n]
    target='combat-requirements/wp45-weather-terrain-side-and-position-effects.md' if n==192 else 'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md'
    cases.append(dict(feature_id=i, candidate_pointer='/features/'+str(m['features'].index(f))+'/dependencies',
                      exact_wrong_ref_pointer='/features/'+str(m['features'].index(f))+'/dependencies/direct_refs/'+str(wrong_index),
                      wrong_ref=f['dependencies']['direct_refs'][wrong_index],
                      source_document=f['source']['document'], source_commit=A,
                      source_lines=f['source']['line_ranges'], target_document=BASE+target,
                      target_wrong_ranges=[[147,177]] if n==192 else [[203,250]],
                      correct_source_ranges=[[122,135]] if n==192 else [[166,191]],
                      reason=reasons[n], necessary_fix='用WP45§6.2/FR39承Mist建立与期限；§7/FR40只有真实交换/清除用途时另保留。' if n==192 else '将退款指向WP42正常终局§6/§6.0/FR31；外层§7/FR32仅在有实际独立世界善后用途时保留并准确说明，勿把全队治疗当主动药品效果。'))
new_findings=[dict(finding_id='R2-CRE-DEP-001', severity='P3', verdict='FAIL',
                   original_issue_id='R1-CRE-DEP-001', original_group_id='CK-DEP-001',
                   title='退款与Mist依赖仍指向不承担该用途的精确源单元',
                   candidate_commit=C, candidate_path=P+'routing-manifest.json', feature_ids=sorted(failed), cases=cases,
                   required_fix='保留已补的真实WP40/UI/HP/形态等边；更正三条错误source unit用途，不改正式正文、不重编号、不要求逐句功能ID。',
                   classification_boundary='五类去向和本域全部122行source/scope保持PASS；FAIL仅依赖用途与相应来源定位。')]
issue_cases=[]
for n in [155,157,158,186,190,191,192]:
    i=fid(n)
    issue_cases.append(dict(feature_id=i, r1_verdict='FAIL', verdict='FAIL' if i in failed else 'PASS',
                            reason=reasons[n], finding_refs=['R2-CRE-DEP-001'] if i in failed else []))

future_diff=git('diff','--unified=3',A,F,'--',*primary_paths)
future_changes=git('diff','--name-only',A,F,'--',*primary_paths).decode().splitlines()
future_evidence=dict(snapshot=F,status='PREPARATION_ONLY_NOT_CURRENT_APPLICATION',
                     domain_changed_documents=future_changes, complete_primary_domain_diff_read=True,
                     complete_diff_sha256=sha(future_diff),
                     findings='六份本域后继小差分：物种蛋群域、记录/回放区分、普通EV越额前门、遭遇负概率前缀、礼物命名取消及MG32对照；保持既有消费者137/173/204/227/244/9c目录的候选职责，无新增实现功能必需。',
                     mapped_new_sections_reviewed=[dict(document=BASE+'generic-kernel/wp03-content-identity-and-schema.md',ranges=[[313,338]],feature_refs=[fid(137),fid(214)],reason='15值作者蛋群及形态继承/寄养匹配由已有物种与寄养主责消费。'),dict(document=BASE+'test-catalog/combat-requirements-wp39-40-41-42-45.md',ranges=[[299,317]],feature_refs=[fid(204)],reason='EV01/02只沿普通EV分配/成长，未扩Shadow/道具。'),dict(document=BASE+'test-catalog/pokemon-rules-wp19-21-22-23-34.md',ranges=[[344,356]],feature_refs=[fid(204)],reason='ST01–05准确区分255模板存储、普通EV首失败与非内部设施早门。')],
                     current_application=A, current_applied_receipts=['R8-U02','R8-U03'],
                     unaccepted_U04_not_counted_as_current_coverage=True,
                     does_not_grant_final_cumulative_source_acceptance=True)

evidence=dict(candidate_commit=C, prior_review_commit=R1R, prior_inputs=input_identities,
              prior_structural_reconciliation=dict(old_rows=116,active_rows=122,section_metadata=158,groups=7,
                                                   global_domain_active_results_equal=True, global_domain_old_results_equal=True,
                                                   issue_cases_equal=True, full_json_records_parsed=True),
              fixed_objects=objects, changed_fields=changed,
              r1_pass_whole_rows_identical=sum(not fields for fields in changed.values()),
              immutable_source_objects_preserved=122, locator_checks=locator_checks, overlap_pairs=overlaps,
              section_records_exactly_equal_r1=158, future_preparation=future_evidence,
              command_receipts=receipts,
              boundary='静态Git/JSON/Markdown，业务向量/Ruby/游戏/宿主/Showdown/框架执行0；未运行作者迁移或生成工具；未改输入/提交。')
results=dict(schema_version='r2-independent-domain-review/v1', reviewer_task='/root/r2_creature',
             candidate_commit=C, prior_candidate_commit=R1C, prior_review_commit=R1R,
             current_source_commit=A, configuration=dict(requested='gpt-6.1-sol/ultra/default/Fast off',
                 effective_model='UNVERIFIED',effective_effort='UNVERIFIED',effective_service_tier='UNVERIFIED',
                 effective_speed='UNVERIFIED',effective_Fast='UNVERIFIED',cloud_task_uuid='UNVERIFIED'),
             verdict='FAIL_DEPENDENCY_UNIT_USES_ONLY',
             summary=dict(original_ids=116,old_PASS=113,old_FAIL=3,old_pending=0,
                          active_ids=122,active_PASS=119,active_FAIL=3,active_pending=0,
                          r1_new_features=6,r1_new_PASS=6,r1_PASS_rows_inherited_exactly=115,
                          original_groups=7,original_group_PASS=6,original_group_FAIL=1,
                          allocated_residual_issues=1,residual_issue_PASS=0,residual_issue_FAIL=1,
                          retired_features=0,metadata_records=0,section_metadata=158,section_metadata_PASS=158,
                          primary_documents=18,body_documents=15,catalog_documents=3),
             old_feature_results=old_results,active_feature_results=active_results,
             retired_metadata_results=[], section_metadata_results=section_metadata_results,
             issue_results=[dict(issue_id='R1-CRE-DEP-001',r1_verdict='FAIL',verdict='FAIL',all_cases=issue_cases,
                                 propagation_checked=True,finding_refs=['R2-CRE-DEP-001'])],
             original_group_results=groups,reading_ledger=reading_ledger,extra_consumer_reading=extra_consumers,
             new_findings=new_findings, future_preparation_review=future_evidence,
             same_root_propagation=dict(checked_feature_refs=[fid(n) for n in [147,158,186,187,190,192,204,207]],
                                       reason='全部本域WP42/WP45 direct_refs遍历并按源用途复核；未变187的整篇锚可真实到达§6.0，不把粗粒度本身判错。',additional_failed_ids=[]),
             execution_boundary=evidence['boundary'],evidence_file='creature-evidence.json')
(OUT/'creature-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
(OUT/'creature-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
report = [
    '# Creature R2 独立复核：依赖 facet FAIL',
    '',
    f'固定候选 `{C}`；R1候选 `{R1C}`；固定R1报告 `{R1R}`。当前适用源为 `{A}`，从Git对象读取。',
    '',
    '**122 active：119 PASS / 3 FAIL / 0待查；116原ID：113 PASS / 3 FAIL。6个R1新增全部PASS。原7组为6 PASS / 1 FAIL，残余issue R1-CRE-DEP-001仍FAIL。** 三条失败均限依赖用途，全部122行分类、历史source和有效范围继续PASS。',
    '',
    '## 残余 P3：R2-CRE-DEP-001',
    '',
    '作者已补多数真实依赖，清掉七条中的迁移、净化室、种植、香、邮件等误用。错误仍在三条新精确源单元的用途；已有有效WP40/UI边不能使错误的另一条边变真。',
    '',
    '| 行 | 候选指针 | 仍存在的问题 | 必要修正 |',
    '| --- | --- | --- | --- |',
    '| FR-000186 | `/features/174/dependencies/direct_refs/1`；`feature_refs`含FR32 | 新指WP42§7，称“战后退款/终局外层善后接收”。current908退款在WP42 L177及§6.0 L183–191；§7 L203–250是后续世界治疗/进化/拾取/恢复，不退款。 | 退款指§6/§6.0及FR31，外层善后如有独立真实用途另说明。 |',
    '| FR-000190 | `/features/178/dependencies/direct_refs/2`；`feature_refs`含FR32 | 新指同一§7，称“治疗/退款善后”。该全队治疗不等于WP28§5.1主动药品/复活效果，且§7不退款。HP/命令/UI/奶招/持物对照其余边成立。 | 删除不相干治疗依赖，或把退款准确连接正常终局§6/FR31；不能拿同名治疗替代实际用途。 |',
    '| FR-000192 | `/features/180/dependencies/direct_refs/3`；`feature_refs`含FR40 | 新指WP45§7并称GuardSpec的Mist建立/期限。§7 L147–177讨论火海、保护、交换/清除；Mist建立5回合、侧期限递减在§6.2 L122–135（L127），属于FR39。 | 建立/期限指§6.2/FR39。§7/FR40只有实际交换/清除用途时另保留。 |',
    '',
    '这里接受章节级聚合，不要求逐句/逐案例新ID。失败在所选精确章节不承担所声称用途；对照FR187整篇WP42锚能实际到达§6.0，因此维持其PASS。',
    '',
    '## 七个R1失败case全部重审',
    '',
    '| ID | R1 → R2 | 完整源节及实际消费者核对 |',
    '| --- | --- | --- |',
]
for n in [155,157,158,186,190,191,192]:
    report.append(f'| {fid(n)} | FAIL → {"FAIL" if fid(n) in failed else "PASS"} | {reasons[n]} |')
report += [
    '',
    '## 原7组及新增单元',
    '',
    '| 原组 | R1 → R2 | 具体范围与方法 |',
    '| --- | --- | --- |',
    '| CK-META-001 | PASS → PASS | 722/723，完整行与源身份相同；物品数据缺省和逐槽显示的独立职责保全。 |',
    '| CK-BATTLE-001 | PASS → PASS | 原147/148/153及新739/740/741全部整行相同；持久PP/持物/奖金父子有效范围与依赖职责保全。 |',
    '| CK-MZ-001 | PASS → PASS | 原15case全部逐行相同：152/166/171/172/178/179/183/196/197/205/206/213/239/240/242；具体输入、取消、刷新和提交前缀保全。 |',
    '| CK-TOOLS-001 | PASS → PASS | 154/244及742整行相同；正常装载/调试新建、编辑导出及用户范围门保全。 |',
    '| CK-MIXED-001 | PASS → PASS | 235/236/249/250整行相同；Factory两屏/取消和Triad手选随机/输入/结算保全。 |',
    '| CK-DEP-001 | FAIL → FAIL | 原13case全核：147/148/187/204/207/221继承有依据PASS；155/157/158/191新读转PASS；186/190/192新读仍FAIL。 |',
    '| CC-CATALOG-F01 | PASS → PASS | 9c的8节映射逐字段相同，真实35功能与247–252 Triad保留，695–698 Duel误边未恢复；另两目录22节一并核。 |',
    '',
    '六个R1新增722/723/739/740/741/742全部整行相同且源不变，按原源范围、职责、父子排除关系及本轮影响分析继承PASS。本域无新增769或META33分配，无retired_feature或metadata_record；158个section-metadata另有逐项结果，不混入33 metadata分母。',
    '',
    '## 全量比较、阅读和传播',
    '',
    '完整读取R1本域报告；固定Git解析全部R1根REPORT/findings/finding-results/feature-results/reading-coverage及本域results，逐116旧行、122active、7组、158个section-metadata与根汇总作结构投影核对。R1输入物理文件逐字节等于固定8c8b对象。根汇总新增归属字段已按明确投影处理，不删掉原字段后冒称整对象相同。',
    '',
    '独立比较R1→R2全部122完整feature对象，仅155/157/158/186/190/191/192的dependencies和differences变；其余115个R1 PASS完整行相同。所有122 immutable source/current locator/scope及158个section记录相同；15正文与3catalog在B8、R8、R1、R2及current908逐字节等同。逐122重新计算scope与current unit/file SHA，重叠0。',
    '',
    '七变更行的完整源单元与新增消费者按用途新读；其它行仅在未变、未受影响facet继承R1有身份的全文信用。全部本域WP42/WP45 direct_ref行147/158/186/187/190/192/204/207另核传播：伙伴外层治疗158、退款187、PP147及成长204/207用途真实，未因共享词或章节宽度判错。跨域749/664对157/158、761/762对186的反向错误用途已通知负责分工；它们是出站行的问题，不反授为157/158等目标功能失败。',
    '',
    '本轮primary新读：WP20 L46–82/121–171；WP24 L173–237；WP28 L103–226/276–294。其余primary区间继承固定R1 ledger（进一步链接初次a035全文记录），逐篇重新核Git blob/SHA256。额外14份consumer的实际新读区间、身份及限制见results。没有把字节解析、标题遍历或继承信用冒称本轮18篇全文新读。',
    '',
    '## 当前源与未来准备',
    '',
    f'当前仍908/U02+U03；后继 `{F}`仅preparation，不授为已应用current或最终累计来源验收。另完整读本域6份后继文档小差分，以及WP03新增蛋群L313–338和两份EV静态目录新节。它们适配既有137/173/204/227/244及catalog职责，无新功能ID必需；准备证据保持独立。未应用U04及其10新标题不单独成为本轮分类修复FAIL。',
    '',
    '全部目标去向、实现、验收、用户范围和四协作原型状态保留R1的待验证/未完成边界；本域current33批次绑定仍待核。没有执行Ruby、参考游戏、业务向量、宿主、Showdown或框架，没有运行作者迁移/生成工具，没有改输入、提交或发布。',
    '',
    '请求配置为gpt-6.1-sol/ultra/default/Fast off；实际model/effort/service_tier/speed/Fast及云UUID没有权威echo，逐字段UNVERIFIED。任务名不是云UUID，分工不是独立接受票。静态收集器最初两次因R1根结果额外归属字段及finding id键差异被断言阻断，修正投影/键适配后通过；未把失败检查记为PASS。',
    '',
    '## 全部122行逐项裁定',
    '',
    '“继承”均指R1整行身份、source身份及非影响核对后的有限信用；“新读”为七条完整源单元及实际消费者重审。',
    '',
    '| ID | 原721成员 | R1 → R2 | 方法 | 理由 |',
    '| --- | --- | --- | --- | --- |',
]
old_id_set={x['feature_id'] for x in old_results}
for x in active_results:
    report.append('| '+x['feature_id']+' | '+('是' if x['feature_id'] in old_id_set else 'R1新增')+' | '+x['r1_verdict']+' → '+x['verdict']+' | '+('新读' if x['affected_fields'] else '继承')+' | '+x['reason'].replace('|','／')+' |')
report += ['', '逐158 section-metadata结果、逐18 primary阅读ledger、额外consumer与全部Git静态命令回执见 [creature-results.json](creature-results.json) 和 [creature-evidence.json](creature-evidence.json)。静态收集脚本为 [creature-audit.py](creature-audit.py)。', '']
(OUT/'creature-report.md').write_text('\n'.join(report))
print(json.dumps(results['summary'],ensure_ascii=False))
print('PASS: complete allocated row/section/source identity reconciliation; residual P3 on 186/190/192.')
