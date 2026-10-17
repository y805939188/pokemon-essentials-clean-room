"""Independent static combat reconciliation. Does not import author tools."""
import copy
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path('/workspace/r8-disposition-r2-review')
OUT = ROOT / 'review/r8-disposition-r2-independent-a32873d-20261017/agents'
BASE = 'planning/implementation-routing/r8-20261017/'
R1REVIEW = 'review/r8-disposition-r1-independent-5666b7b-20261017/'
CANDIDATE = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
R1 = '5666b7b912e2fb79b5119283ee6a37401a7071db'
REPORT = '8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8'
D62 = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
CURRENT = '908273093e1f6b27fc58249417675dd62d146224'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def blob(commit, path):
    return git('show', commit + ':' + path)

def parsed(commit, path):
    return json.loads(blob(commit, path))

def sha(data):
    return hashlib.sha256(data).hexdigest()

def digest_json(value):
    return sha(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode())

def field_diff(left, right, prefix=''):
    if type(left) is not type(right):
        return [prefix]
    if isinstance(left, dict):
        return [p for key in sorted(left.keys() | right.keys())
                for p in field_diff(left.get(key), right.get(key), prefix + '/' + key)]
    return [] if left == right else [prefix]

def domain(row):
    return '/combat-requirements/' in row['source']['document']

def all_by_id(manifest):
    return {row['feature_id']: row for row in manifest['features'] + manifest.get('retired_features', [])}

def identity(commit, path):
    data = blob(commit, path)
    return dict(commit=commit, path=path, bytes=len(data), sha256=sha(data),
                git_blob=git('rev-parse', commit + ':' + path).decode().strip(),
                lines=len(data.decode().splitlines()))

assert git('rev-parse', 'HEAD').decode().strip() == CANDIDATE
m = parsed(CANDIDATE, BASE + 'routing-manifest.json')
r1 = parsed(R1, BASE + 'routing-manifest.json')
d62 = parsed(D62, BASE + 'routing-manifest.json')
prior = parsed(REPORT, R1REVIEW + 'agents/combat-results.json')
prior_root = parsed(REPORT, R1REVIEW + 'feature-results.json')
prior_groups = parsed(REPORT, R1REVIEW + 'finding-results.json')
prior_reading = parsed(REPORT, R1REVIEW + 'reading-coverage.json')
prior_findings = parsed(REPORT, R1REVIEW + 'findings.json')
current_all, r1_all, d62_all = map(all_by_id, [m, r1, d62])
active = [x for x in m['features'] if domain(x)]
retired = [x for x in m['retired_features'] if domain(x)]
metadata = [x for x in m['metadata_records'] if domain(x)]
old_rows = [x for x in d62['features'] if domain(x)]
old_ids = {x['feature_id'] for x in old_rows}
previous_old = {x['feature_id']: x for x in prior['old_feature_results']}
previous_active = {x['feature_id']: x for x in prior['active_feature_results']}
assert len(old_rows) == 136 and len(active) == 134 and len(retired) == len(metadata) == 11
assert old_ids == set(previous_old)
assert len({x['feature_id'] for x in active + retired}) == len(active + retired)
assert old_ids <= set(current_all)
assert all(current_all[i]['source'] == d62_all[i]['source'] for i in old_ids)

input_ledger = []
for path in ['REPORT.md', 'findings.json', 'finding-results.json', 'feature-results.json',
             'reading-coverage.json', 'root-findings.json', 'agents/combat-report.md',
             'agents/combat-results.json', 'agents/combat-static-evidence.json']:
    fixed = blob(REPORT, R1REVIEW + path)
    physical = Path('/workspace/r8-disposition-r1-review', R1REVIEW, path).read_bytes()
    assert fixed == physical
    input_ledger.append(dict(path=R1REVIEW + path, commit=REPORT, bytes=len(fixed), sha256=sha(fixed),
                             physical_copy_matches_fixed_git=True,
                             consumption='FULL_COMBAT_SEMANTICS_AND_ATTRIBUTED_STRUCTURAL_RECONCILIATION' if path.endswith('.json') else 'FULL_TEXT'))

# Root aggregates add attribution fields; every original semantic field is reconciled.
for list_name in ['old_feature_results', 'active_feature_results']:
    indexed = {x['feature_id']: x for x in prior_root[list_name]}
    for row in prior[list_name]:
        assert all(indexed[row['feature_id']][key] == value for key, value in row.items())
for group in prior['finding_results']:
    aggregate = next(x for x in prior_groups['finding_results'] if x['finding_id'] == group['finding_id'])
    assert all(aggregate[key] == value for key, value in group.items())

fresh = {
    'wp41-switching-positioning-and-escape.md': [[46, 137], [152, 195]],
    'wp42-growth-end-of-round-and-battle-outcomes.md': [[166, 236]],
    'wp49-ability-phase-triggers.md': [[100, 123]],
    'wp51-ai-action-selection-and-skill.md': [[132, 160]],
    'wp52-a-evaluation-coverage-and-data.md': [[237, 260]],
    'wp52-a-generic-numerical-and-status-evaluation.md': [[1, 111]],
    'wp52-b-field-damage-healing-and-target-evaluation.md': [[23, 114]],
    'wp52-c-items-calling-and-control-evaluation.md': [[106, 133]],
    'combat-requirements-wp49-51-52.md': [[1, 42]],
}
reading = []
coverage_by_path = {x['path']: x for x in prior_reading['documents']}
for index, entry in enumerate(prior['reading_ledger']):
    path = entry['path']
    identities = [identity(commit, path) for commit in [B8, R1, CANDIDATE, CURRENT]]
    assert len({x['sha256'] for x in identities}) == 1
    assert identities[-1]['sha256'] == entry['sha256']
    root_credit = coverage_by_path[path]
    assert root_credit['source_identity']['sha256'] == identities[0]['sha256']
    assert root_credit['current_identity']['sha256'] == identities[-1]['sha256']
    prior_credit = root_credit['prior_full_reading_record']
    assert prior_credit['sha256'] == identities[0]['sha256']
    reading.append(dict(path=path, source_commit=B8, current_commit=CURRENT,
                        candidate_commit=CANDIDATE, **{k:v for k,v in identities[-1].items() if k not in ['path','commit']},
                        new_read_ranges=fresh.get(Path(path).name, []),
                        identities=identities, all_four_fixed_versions_same_bytes=True,
                        r1_reading_credit=dict(commit=REPORT, record=R1REVIEW + 'agents/combat-results.json#/reading_ledger/' + str(index),
                                               prior_fresh_ranges=entry['new_read_ranges'],
                                               original_full_read=prior_credit,
                                               inherited_R1_predecessor_credit=entry['inherited_reading']),
                        method='TARGETED_FRESH_SOURCE_REVIEW_PLUS_IDENTITY_BOUND_FACET_INHERITANCE',
                        inheritance_justification='本轮未改的完整源字节及逐行分类/职责/依赖/范围相等，才保留R1已核语义；67/86/六AI及新769的改变facet已按完整问题源节和混合表重新判断。未输出的新范围不计本轮全文重读。'))

ai_ids = ['FR-000076','FR-000088','FR-000089','FR-000098','FR-000099','FR-000111']
ai_details = {
    'FR-000076': '逐槽/逐目标准备calcType及global moldBreaker，评分正常结束清moldBreaker，再登记原槽；框架协调评分顺序，Showdown候选拥有共享准备写入/正常清理，异常残留不承诺回滚。',
    'FR-000088': '按目标恢复原评估对象、Copycat/NaturePower/MirrorMove替换及随后准备有明确框架协调/对象重建与Showdown共享查询状态候选责任；不将预测准备视为纯查询。',
    'FR-000089': 'Prankster优先查询后显式清、GemConsumed在宝石判定后显式清、真实类别prepare及damageState读取已具名交给共享战斗状态候选；没有把所有字段都清除或统一finally作为事实。',
    'FR-000098': 'NaturalGift无物异常可在类型/忽略特性准备后发生；初始100只是未完成评分外包装，非HP/PP/持物提交；候选共享状态拥有者与框架协调责任明确。',
    'FR-000099': 'BeatUp零人数分母异常在共享准备后；非宝石夹具不虚构GemConsumed重置；框架消费评分/失败前缀、Showdown候选拥有准备状态，正常清理与异常残留分开。',
    'FR-000111': '调用替换遵循共同准备；SecretPower真实prepare写效果代码后由AI自身坏映射打分，战斗状态与框架策略分开，不按真实降阶补造AI收益。',
}
reasons = dict(ai_details)
reasons['FR-000067'] = '完整原source保留；当前scope/locator仅100–105、107–123，精确扣L106到769。剩余普通HP/状态/阶级/行动反馈可保留Showdown候选，未将真实退出交接留在父范围。'
reasons['FR-000086'] = '§5逐文件/包/族只是A阶段历史已有/前向责任索引，现完整d62原行加retirement转META33；现行换人、B/C评分与数据绑定消费者承担行为，无新实现空壳。'
reasons['FR-000769'] = '新单元精确L106，野生可逃后决定3、训练家非回合末业主等待/负选择假及已提示前缀、回合末只召回留待补位分支完整保留；Showdown规则、框架等待恢复/终局世界消费及MZ选择有候选责任，接20/22/31/32/734和PROTO-ESCAPE，仍待验证。'
issue_ref = {i:'CAI-R1-01' for i in ai_ids}
issue_ref.update({'FR-000067':'COMBAT-R1-01','FR-000769':'COMBAT-R1-01','FR-000086':'CAI-R1-02'})

old_results = []
for feature_id in sorted(old_ids):
    before, now = r1_all[feature_id], current_all[feature_id]
    changes = field_diff(before, now)
    old = previous_old[feature_id]
    if old['verdict'] == 'PASS':
        assert not changes
        reason = 'R1限定PASS的完整记录逐字段相等；源字节固定同一，逐根因检查无新影响。R1具体判断：' + old['reason']
        method = 'EXACT_FULL_RECORD_IDENTITY_PLUS_SCOPED_R1_SEMANTIC_CREDIT_AND_PROPAGATION'
    else:
        reason, method = reasons[feature_id], 'FRESH_FULL_AFFECTED_SOURCE_UNIT_AND_CONSUMER_REASSESSMENT'
    old_results.append(dict(feature_id=feature_id, r1_verdict=old['verdict'], prior_verdict=old['verdict'],
                            verdict='PASS', disposition='active' if feature_id in {x['feature_id'] for x in active} else 'retired',
                            reason=reason, method=method, changed_fields=changes,
                            r1_record_sha256=digest_json(before), candidate_record_sha256=digest_json(now),
                            immutable_source_preserved=True, finding_refs=[issue_ref[feature_id]] if feature_id in issue_ref else [],
                            r1_evidence=R1REVIEW+'agents/combat-results.json#/old_feature_results/'+str(list(previous_old).index(feature_id)),
                            source=now['source']))

active_results = []
for row in active:
    feature_id = row['feature_id']
    old = previous_active.get(feature_id)
    changes = field_diff(r1_all[feature_id], row) if old else ['NEW_STABLE_ID']
    if old and old['verdict'] == 'PASS':
        assert row == r1_all[feature_id]
        reason = 'R1完整行与全部被审字段相等；未改源及本轮退出/准备/metadata修正不改变本行有效范围、去向或真实消费者。R1具体判断：' + old['reason']
        method = 'EXACT_FULL_RECORD_IDENTITY_PLUS_SCOPED_R1_SEMANTIC_CREDIT_AND_PROPAGATION'
    else:
        reason, method = reasons[feature_id], 'FRESH_FULL_AFFECTED_SOURCE_UNIT_AND_CONSUMER_REASSESSMENT'
    index = m['features'].index(row)
    active_results.append(dict(feature_id=feature_id, r1_verdict=old['verdict'] if old else 'NEW', verdict='PASS',
                               reason=reason, method=method, affected_fields=changes, changed_fields=changes,
                               candidate_pointer='/features/'+str(index), source=row['source'],
                               functional_scope=row['functional_scope'], current_applicability=row['current_applicability'],
                               future_plan=row['future_plan'], dependencies=row['dependencies'],
                               r1_record_sha256=digest_json(r1_all[feature_id]) if old else None,
                               candidate_record_sha256=digest_json(row),
                               finding_refs=[issue_ref[feature_id]] if feature_id in issue_ref else []))

# Complete historical original rows are compared against d62, not the later R1 templates.
retired_results = []
for row in retired:
    feature_id = row['feature_id']
    history = {k:v for k,v in row.items() if k != 'retirement'}
    assert history == d62_all[feature_id]
    related = next(x for x in metadata if feature_id in x['retired_feature_ids'])
    assert row['retirement']['metadata_record_id'] == related['metadata_id']
    retired_results.append(dict(unit_type='retired-feature', feature_id=feature_id, metadata_id=related['metadata_id'],
                                verdict='PASS', reason=reasons.get(feature_id, 'R1退役记录整行未变；完整d62历史行为/计划/依赖/状态均保留，仅退役导航不计实现。'),
                                complete_d62_body_preserved=True, historical_body_sha256=digest_json(history),
                                retirement=row['retirement'], source=row['source']))
for row in metadata:
    meta_id = row['metadata_id']
    before = next((x for x in r1['metadata_records'] if x['metadata_id']==meta_id), None)
    if before is not None:
        assert row == before
    assert all(x in {f['feature_id'] for f in m['features']} for x in row['feature_refs'])
    if meta_id=='META-000033':
        reason = 'L239明确历史定位；L241–242换人→74/80，L243物品评级→103–105，L244–254按B/C效果登记及评分→94/95/98–102/109–113。允许章节字段组导航，不据A历史状态赋新行为。完整86退役、source及旧ID保全。'
    else:
        reason = '与R1完整metadata记录相等；源责任/覆盖/保留单元仍无独立实现承诺。其已核消费者和明确父子间接导航保持；六AI与67后继只补候选准备/退出责任，不移走已有实际消费者。'
    retired_results.append(dict(unit_type='metadata-record', metadata_id=meta_id, verdict='PASS',
                                r1_verdict='PASS' if before else 'NEW', method='EXACT_FULL_RECORD_AND_FIXED_SOURCE_IDENTITY' if before else 'FRESH_COMPLETE_HISTORICAL_TABLE_REVIEW',
                                reason=reason, consumer_refs=row['feature_refs'], retired_feature_ids=row['retired_feature_ids'],
                                source=row['source'], candidate_pointer='/metadata_records/'+str(m['metadata_records'].index(row)),
                                exact_r1_record_preserved=before==row if before else None))

groups = []
for old in prior['finding_results']:
    group = dict(finding_id=old['finding_id'], r1_verdict=old['verdict'], verdict='PASS',
                 method='FRESH_REASSESSMENT_OF_RESIDUAL_AND_PROPAGATION' if old['verdict']=='FAIL' else 'EXACT_FACET_PRESERVATION_WITH_AFFECTED_CASE_REASSESSMENT',
                 original_case_count=len(old['original_cases']), original_cases=[], propagation_cases=[], all_original_cases_checked=True)
    for case in old['original_cases']:
        i = case['feature_id']
        group['original_cases'].append(dict(feature_id=i, r1_case_verdict=case['verdict'], verdict='PASS',
                                           new_child_refs=current_all[i].get('functional_scope',{}).get('excluded_child_refs',[]),
                                           reason=reasons.get(i, '原case R1修正facet及完整行精确保留。' + case['evidence']),
                                           changed_fields=field_diff(r1_all[i], current_all[i])))
    for case in old.get('propagation_cases',[]):
        i = case['feature_id']
        group['propagation_cases'].append(dict(feature_id=i, verdict='PASS', reason=reasons[i], finding_ref=issue_ref[i]))
    group['scope'] = {'CAI-01':'41原case；六共享准备新写入/清理责任和86历史索引退役另行重审。',
                       'CAI-02':'三个已退役责任原case完整保全，传播86新退役META33。',
                       'CAI-03':'16依赖case；六AI新增具名共享准备direct_refs只扩明确消费者，既有依赖全部保留。',
                       'COMBAT-01':'10/11退款case及731/732父子/物品原型完整保全。',
                       'COMBAT-02':'7持久/物权case及735写生双提交；本轮未改，不受L106单独拆分影响。',
                       'COMBAT-03':'6音频/队伍UI/报名/裁判/回放case及733/732/734/736/737/738完整保全；29→206共享UI继续可用。',
                       'COMBAT-04':'7来源/责任/历史case完整保全；86同根因新按META33重审。',
                       'COMBAT-05':'6依赖case，61→740→577→574/576与29→206间接合同依然完整。',
                       'COMBAT-06':'20/58原case精确保留；传播67已精确扣子L106，769补退出原型和世界/MZ责任。'}[old['finding_id']]
    groups.append(group)

issues = [
    dict(issue_id='COMBAT-R1-01', finding_id='COMBAT-R1-01', verdict='PASS', severity='P2', cases=[
        dict(feature_id=i, verdict='PASS', reason=reasons[i]) for i in ['FR-000067','FR-000769']],
        propagation='20/22/23/31/32/58/734退出、替补、世界终局和共享UI合同未改；新769依赖20/22/31/32/734及PROTO-ESCAPE，父source与覆盖链完整。'),
    dict(issue_id='CAI-R1-01', finding_id='CAI-R1-01', verdict='PASS', severity='P3', cases=[
        dict(feature_id=i, verdict='PASS', reason=ai_details[i]) for i in ai_ids],
        propagation='全部41原AI case、其余预测/登记/偏好行逐字段保全；六个实际共享准备入口有共同粗合同，不据未运行原型拒绝正确候选，亦不将候选当目标支持。'),
    dict(issue_id='CAI-R1-02', finding_id='CAI-R1-02', verdict='PASS', severity='P3', cases=[
        dict(feature_id='FR-000086', metadata_id='META-000033', verdict='PASS', reason=reasons['FR-000086'])],
        propagation='81/97/108等既有退役索引未改；86没有active依赖引用，章节/目录移除86活跃关联并保留META33和retired导航。'),
]

coverage = parsed(CANDIDATE, BASE + 'section-coverage.json')['sections']
r1coverage = {(x['path'],x['anchor']):x for x in parsed(R1, BASE+'section-coverage.json')['sections']}
catalogs = []
for old in prior['catalog_consumer_results']:
    now = next(x for x in coverage if x['path']==old['path'] and x['anchor']==old['anchor'])
    before = r1coverage[(now['path'],now['anchor'])]
    delta = field_diff(before, now)
    if delta:
        assert delta == ['/feature_refs']
        assert set(before['feature_refs']) - set(now['feature_refs']) == {'FR-000086'}
        assert not set(now['feature_refs']) - set(before['feature_refs'])
    child_refs = sorted({c for i in now['feature_refs'] for c in current_all[i].get('functional_scope',{}).get('excluded_child_refs',[])})
    catalogs.append(dict(path=now['path'], anchor=now['anchor'], ranges=[[now['line_start'],now['line_end']]],
                         verdict='PASS', r1_verdict=old['verdict'], changed_fields=delta, consumer_refs=now['feature_refs'],
                         explicit_indirect_child_navigation=child_refs,
                         reason='未改静态向量与NOT_EXECUTED资格；R1章节级消费映射保留，仅移除已退役86的活跃引用。AB退出向量H02/H03可经67→769到真实协作；不要求每case新ID。' if now['path'].endswith('combat-requirements-wp49-51-52.md') else '完整源和章节映射精确保留；目录→父→excluded_child_refs子导航仍明确，R1具体已核主规则与静态未执行性质不变。'))
assert len(catalogs)==37

# Independently recompute every active current unit locator and all effective scopes.
scope_owner = {}
for row in active:
    s, c = row['source'], row['current_applicability']
    lines = blob(CURRENT, c['document']).decode().splitlines(keepends=True)
    loc = c['locator']
    unit = ''.join(''.join(lines[a-1:b]) for a,b in loc['line_ranges']).encode()
    assert sha(unit)==loc['unit_sha256']
    assert sha(blob(CURRENT,c['document']))==loc['file_sha256']
    assert git('rev-parse',CURRENT+':'+c['document']).decode().strip()==loc['file_git_blob']
    assert loc['line_ranges']==row['functional_scope']['line_ranges']
    for start,end in row['functional_scope']['line_ranges']:
        for line in range(start,end+1):
            key=(s['document'],line)
            assert key not in scope_owner
            scope_owner[key]=row['feature_id']
assert current_all['FR-000067']['source']==d62_all['FR-000067']['source']
assert current_all['FR-000067']['functional_scope']['line_ranges']==[[100,105],[107,123]]
assert current_all['FR-000769']['functional_scope']['line_ranges']==[[106,106]]
assert all('FR-000086' not in x['dependencies'].get('feature_refs',[]) for x in m['features'])
view = blob(CANDIDATE,BASE+'views/combat-requirements.md').decode()
for row in active:
    if row['functional_scope']['excluded_child_refs']:
        matching=[x for x in view.splitlines() if x.startswith('| '+row['feature_id']+' ')]
        assert len(matching)==1
        assert all(child in matching[0] for child in row['functional_scope']['excluded_child_refs'])

result = dict(schema='r8-disposition-r2-combat-independent.v1', candidate_commit=CANDIDATE,
              r1_candidate_commit=R1, r1_report_commit=REPORT, current_snapshot=CURRENT,
              canonical_task='/root/r2_combat', conclusion='PASS_SCOPED_CLASSIFICATION_REPAIR',
              configuration={key:'UNVERIFIED' for key in ['actual_model','actual_effort','actual_service_tier','actual_speed','actual_Fast','cloud_task_UUID']},
              counts=dict(primary_body_documents=23, primary_catalog_documents=4, old_ids=len(old_results),
                          r1_old_verdicts=dict(Counter(x['r1_verdict'] for x in old_results)),
                          old_verdicts=dict(Counter(x['verdict'] for x in old_results)), active=len(active_results),
                          active_verdicts=dict(Counter(x['verdict'] for x in active_results)),
                          retained_R1_new_active=8, new_active=1, retired=len(retired), metadata=len(metadata),
                          catalog_sections=37, original_groups=len(groups), residual_issues=len(issues),
                          unchanged_R1_pass_active=sum(x['r1_verdict']=='PASS' for x in active_results)),
              old_feature_results=old_results, active_feature_results=active_results,
              retired_metadata_results=retired_results, issue_results=issues, original_group_results=groups,
              reading_ledger=reading, catalog_consumer_results=catalogs,
              input_consumption_ledger=input_ledger,
              shared_ai_contract=parsed(CANDIDATE,BASE+'revisions/r2/shared-ai-preparation.json'),
              structural_checks=dict(all_original_ids_exactly_once=True, all_136_immutable_sources_preserved=True,
                                     all_11_complete_d62_retired_bodies_preserved=True, all_126_R1_PASS_active_rows_exact=True,
                                     all_10_R1_metadata_rows_exact=True, all_27_source_files_identity_bound=True,
                                     all_134_current_locator_hashes_recomputed=True, active_scope_overlap_count=0,
                                     split_67_769_exact_L106=True, all_domain_parent_child_view_ids_present=True),
              new_findings=[],
              limits=['仅固定候选当前908阶段分类修正限定通过；不授予目标兼容、实现、上游最终校准或用户阶段批准。',
                      '本域27源文档与B8/R1/当前908同字节；后继49/0eee准备不能替代当前，U04正式回执独立门保留。',
                      '四原型未运行；无Ruby/参考游戏/业务向量/宿主/Showdown/框架执行。',
                      'fresh范围仅reading_ledger列明的9文档章节；其他全文语义信用来自固定R1及原a035，未把机械身份解析说成新全文阅读。',
                      '全局工具/视图/后继接受及保护由root负责；本报告本域父子导航检查不替代全局验收。'])
# Later requested full outbound-edge review supersedes the earlier scoped inheritance
# for dependency correctness; it does not erase the original repaired facets.
supplement_path = OUT/'combat-dependency-crosscheck.json'
if supplement_path.exists():
    supplement = json.loads(supplement_path.read_text())
    assert supplement['candidate_commit'] == CANDIDATE
    bad = {x['source_feature_id'] for x in supplement['edge_results'] if x['verdict']=='FAIL'}
    assert bad == {'FR-000061','FR-000066','FR-000069'}
    for key in ['old_feature_results','active_feature_results']:
        for row in result[key]:
            row['classification_facet_verdict'] = 'PASS'
            if row['feature_id'] in bad:
                row['repaired_classification_reason'] = row['reason']
                row['verdict'] = row['overall_verdict'] = 'FAIL'
                row['dependency_facet_verdict'] = 'FAIL'
                row['reason'] = '完整出站边补核：本有效源范围没有招式/PP同步用途，却引用仅WP20§5.5招式/PP边界FR739；见COMBAT-R2-DEP-001。原分类/持久责任修正保留PASS，目标739不反向FAIL。'
                row['method'] = 'FRESH_FULL_OUTBOUND_EDGE_SET_SEMANTIC_REASSESSMENT'
                row['finding_refs'] = list(set(row.get('finding_refs',[])) | {'COMBAT-R2-DEP-001'})
    for group in result['original_group_results']:
        group['original_case_verdict'] = 'PASS'
        group['current_scope_verdict'] = 'FAIL' if group['finding_id']=='COMBAT-05' else 'PASS'
        for case in group['original_cases']:
            case['original_case_verdict'] = 'PASS'
            case['current_overall_feature_verdict'] = 'FAIL' if case['feature_id'] in bad else 'PASS'
        if group['finding_id']=='COMBAT-05':
            group['verdict']='FAIL'
            group['scope'] += ' 补核发现61/66/69→739同根因错用途边；原六case缺口已修为PASS，扩大的当前依赖scope为FAIL。'
            group['propagation_cases'].extend(dict(feature_id=i,verdict='FAIL',finding_ref='COMBAT-R2-DEP-001',reason='无招式/PP同步用途却挂739。') for i in sorted(bad))
    result['conclusion']='FAIL_DEPENDENCY_PROPAGATION_WITH_CLASSIFICATION_REPAIRS_PRESERVED'
    result['new_findings']=supplement['new_findings']
    result['dependency_crosscheck']='combat-dependency-crosscheck.json'
    result['author_transform_consistency']='combat-author-transform-consistency.json'
    result['counts']['old_verdicts']=dict(Counter(x['verdict'] for x in result['old_feature_results']))
    result['counts']['active_verdicts']=dict(Counter(x['verdict'] for x in result['active_feature_results']))
    result['counts']['classification_facet_verdicts']={'PASS':len(result['active_feature_results'])}
    result['counts']['dependency_edges_checked']=len(supplement['edge_results'])
    result['counts']['dependency_edges_failed']=sum(x['verdict']=='FAIL' for x in supplement['edge_results'])
    result['supplemental_reading_ledger']=supplement['reading_ledger']
    result['reading_mode_correction']='未改整行保全不证明依赖语义；后来已对本域全部98出站边、24源、52目标完整有效scope重新读，3源overall据此转FAIL。'
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'combat-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result['counts'],ensure_ascii=False))
print('ALL INDEPENDENT STATIC ASSERTIONS PASSED')
