"""Package already adjudicated facts; never infer new gameplay from a keyword search."""
import collections, hashlib, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]

def read(p):
    return json.loads((ROOT / p).read_text())

def save(p, x):
    (ROOT / p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

R = {x['path']: x for x in read('inventory/reference.json')}
F = {x['path']: x for x in read('inventory/formal131.json')}
W = {x['path']: x for x in read('inventory/workspace-tracked.json')}

def first(x, keys, default=None):
    for k in keys:
        if k in x and x[k] not in (None, '', [], {}):
            return x[k]
    return default

def listify(x):
    return x if isinstance(x, list) else [] if x is None else [x]

def locations(x, keys, source=False):
    result = []
    for v in listify(first(x, keys)):
        if isinstance(v, str):
            v = {'original_locator': v, 'path': v.split(':')[0]}
        if not isinstance(v, dict):
            continue
        path = v.get('path', '')
        p = path.removeprefix('reference/pokemon-essentials/') if source else path
        inv = (F.get(p) if p.startswith('deliverables/') else R.get(p)) if source else F.get(p, W.get(p))
        if inv:
            inv={k:value for k,value in inv.items() if k!='reading_status'}
        result.append({'locator': v, 'payload_identity': inv, 'identity_resolved': inv is not None,
                       'payload_role': 'formal_consumer_misgrouped_in_original_source_list' if source and p.startswith('deliverables/') else 'reference' if source else 'formal'})
    return result

def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)

def exact_paths(x):
    found = set()
    for s in strings(x):
        for p in F:
            if p in s or p.removeprefix('deliverables/final-specification-set/') in s:
                found.add(p)
    return sorted(found)

SYNC = ['sync_files', 'synchronization_files', 'synchronize', 'synchronized_files',
        'synchronize_files', 'scope_synchronization_files', 'dependencies_and_sync_files',
        'synchronization', 'synchronize_if_accepted']
SOURCE = ['source', 'sources', 'source_locations', 'source_location']
FORMAL = ['formal', 'spec', 'formal_locations', 'spec_locations', 'specification_locations',
          'formal_location', 'spec_location']

# First allocated domain IDs remain canonical; parent aggregation IDs are recoverable aliases.
canonical = {x['id']: x['original_id'] for x in read('tasks/R6-F/finding-id-map.json')}
counter_extras = {
    'R6-C': ['tasks/R6-K/counter-C-001.json', 'tasks/R6-K/counter-C-002.json',
             'tasks/R6-CA/gr6-c-001-independent-rebuttal.md', 'tasks/R6-CM/counter-C-002.json'],
    'R6-O': ['tasks/R6-C/counter-O-002.json'],
    'R6-K': ['tasks/R6-O/counter-K-001.json', 'tasks/R6-O/counter-K-002.json', 'tasks/R6-O/counter-K-003.json'],
    'R6-UI': ['tasks/R6-F/countercheck-ui-entry-stale-command.json', 'tasks/R6-K/imported-ui-party-storage-bag-facts.json'],
}
evidence = {}
records = []
for row in read('findings/adjudicated-records.json'):
    x = row['original_record']
    rid = canonical.get(row['id'], row['id'])
    source = locations(x, SOURCE, True)
    formal = locations(x, FORMAL)
    reader = row['reader']
    counter_files = set()
    for p in (ROOT / 'tasks' / reader).rglob('*'):
        if p.is_file() and p.suffix in ('.json', '.md', '.jsonl', '.txt') and any(s in p.name for s in ('counter', 'rebuttal')):
            counter_files.add(str(p.relative_to(ROOT)))
    counter_files.update(counter_extras.get(reader, []))
    counter_files.update(str(p.relative_to(ROOT)) for p in (ROOT / 'findings').glob('independent-*.json') if row['id'].removeprefix('GR6-') in p.name)
    counter_ids = []
    for p in sorted(counter_files):
        q = ROOT / p
        if not q.is_file():
            continue
        data = q.read_bytes()
        eid = 'EV-' + hashlib.sha256(p.encode()).hexdigest()[:16]
        # Exact payload is published in report core, hash/byte binding is independently checked.
        evidence[eid] = {'path': p, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                         'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(),
                         'recovery': 'git show <R6-core>:<review-root>/' + p,
                         'purpose': 'non-proposer source counterevidence; original scope and conflicting evidence preserved'}
        counter_ids.append(eid)
    sync_raw = {k: x[k] for k in SYNC if k in x}
    writes = exact_paths(sync_raw)
    if row['classification'] == 'required' and not writes:
        writes = exact_paths({k: x[k] for k in FORMAL if k in x})
    if row['id'] in ('GR6-O-001','GR6-O-002'):
        writes=sorted(set(writes)|{'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'})
    rules = first(x, ['minimum_revision', 'minimal_revision', 'minimal_rule', 'minimal_repair',
                     'minimal_fix', 'minimal_correction', 'minimal_revision_scope'])
    preserve = first(x, ['retained_scope', 'preserved_scope', 'preserve_scope', 'preserve_correct_scope',
                        'scope_preservation'], '仅按原记录与独立裁决的具体前提；不扩展为运行等价或永久缺陷兼容。')
    acceptance = first(x, ['acceptance_regression', 'acceptance_regressions', 'acceptance',
                           'acceptance_vectors', 'acceptance_criteria', 'acceptance_regression_designs', 'tests', 'regression'])
    cancellation = {k: v for k, v in x.items() if any(s in k for s in ('cancel', 'partial', 'failure_prefix', 'exception'))}
    negative = {k: v for k, v in x.items() if 'negative' in k}
    counter = {k: v for k, v in x.items() if any(s in k for s in ('non_proposer', 'nonproposer', 'counter', 'independent_review'))}
    deps = first(x, ['dependencies', 'regression_dependencies'], [])
    premise = first(x, ['preconditions', 'prerequisites', 'premises', 'source_preconditions'])
    if not premise:
        premise = first(x.get('minimal_counterexample', {}) if isinstance(x.get('minimal_counterexample'), dict) else {}, ['preconditions'])
    if not premise:
        premise = {'specific_input_domain': x.get('minimal_counterexample'), 'additional_gate': x.get('additional_precondition_gap'),
                   'reason': '本记录的前提与输入共同位于具体反例中，不另造前提。'}
    correction=None
    if row['id']=='GR6-C-001':
        acceptance=list(acceptance)
        acceptance[3]='1v2空槽前已有束缚指向命中：本yawning/asleep处理器正常返回false而未到空槽；意愿组仍可继续后续处理器。不得把本处理器拒绝写成最终全阶段必不换人。'
        correction='R6-C/final-packet-counter非提出者检查：收窄洞前指向的处理器false，保留后续意愿继续。'
    elif row['id']=='GR6-C-002':
        original_premises=listify(premise)
        premise={'common':[original_premises[0],original_premises[2], 'TACKLE真实槽/PP正、过去正常使用、Disable及Herb各具体门满足；不把一个速度关系强加给两种向量。'],
                 'next_menu_vector':'当轮T先正常TACKLE、较慢U随后Disable+Herb；随后下一普通菜单资格观察。',
                 'queued_execution_vector':'过去已正常TACKLE；当前先合法登记TACKLE，较快U本轮先成功Disable+Herb，然后T已登记普通执行在PP前被禁用身份拒。'}
        formal.sort(key=lambda a:0 if '/wp40-' in a['locator']['path'] else 1)
        correction='R6-C/final-packet-counter非提出者检查：common/menu/executor速度分列；WP40:84为主合同，WP50本地正确事实保持。'
    elif row['id']=='R6-DX-AN-007':
        rules='必修仅自动默认中间控制点采用0.3333/0.6666比例的近似三等分请求。端点(0,0)/(300,0)给约(99.99,0)/(199.98,0)，不是把默认点定义为精确1/3与2/3。保留显式N5控制点示例及数学概念；宿主坐标量化/像素未知。一般N浮点递推/位级端点兼容只属独立optional facet，禁止并入本ID必修。'
        acceptance=['默认端点(0,0)/(300,0)：初建两个中间点按0.3333和0.6666比例，数值请求约99.99与199.98；区分精确100/200。',
                    '显式控制点的现行N5示例按原值保留，不误称自动默认点。',
                    '没有原生资源/宿主证据时不承诺整数坐标或实际像素；一般N逐步加法端点差异仍单列optional。']
        correction='R6-C/final-packet-counter非提出者检查：当前最小规则和验收只保mandatory默认点，原递推建议在原始提案与optional facet中保留。'
    groups = sorted({a['locator'].get('path', '').split('/')[2] for a in formal if len(a['locator'].get('path', '').split('/')) > 2})
    levels={k:v for k,v in x.items() if any(s in k for s in ('evidence', 'execution', 'validation', 'verification', 'observation', 'runtime', 'HostDemo', 'host_demo', 'independent_model'))}
    if reader=='R6-D' and not levels:
        levels={'SOURCE_STATIC':'本轮D连续源/条款新读与非提出者counter；报告和combined-reading-ledger记录具体范围',
                'DERIVED_VECTOR':'本记录具体输入/结果是静态推导，未执行参考函数或玩法模型',
                'TOOL_VALIDATION':'材料结构/字段/字节或负定位工具只按D当前报告的实际载荷保留；未分配全队其它执行给本项',
                'REFERENCE_OBSERVATION':'NOT_EXECUTED','independent_model':'NOT_EXECUTED','complete_host':'NOT_EXECUTED',
                'counter_adoption':'R6-C/final-packet-counter检查发现原提案没有统一层字段；依据其实际NOT_EXECUTED及D原有限解析报告补层，不制造运行证据'}
    record = {
        'id': rid, 'aggregation_aliases': [row['id']] if rid != row['id'] else [],
        'identity_and_verdict': {'classification': row['classification'], 'severity': row['severity'],
                                'severity_reason': row['root_decision_reason'], 'title': x.get('title'),
                                'domain_groups': groups, 'primary_contract': formal[0] if formal else None,
                                'root_cause_key': rid, 'historical_relationship': {k:v for k,v in x.items() if 'histor' in k or 'original_id' in k},
                                'state': row['state'], 'update_started': False},
        'bidirectional_evidence': {'source': source, 'formal': formal,
                                   'necessary_consumers': first(x, ['necessary_consumers', 'needed_consumer'], {'exact_source_consumer_locations':source,'reason':'该原提案将必要消费者直接合列于source定位及反例有序步骤，未另立消费者数组。'}),
                                   'negative_evidence': negative, 'counter_evidence_ids': counter_ids,
                                   'fact_consumer_chain': {'producer_context':first(x,['behavioral_fact','claim'], source),
                                       'state_observation_and_later_result':first(x,['minimal_counterexample','minimal_counterexample_to_an_overbroad_interpretation']),
                                       'consumer':first(x,['necessary_consumers','needed_consumer'],source),
                                       'definition_vs_wiring':'仅按本记录的具体前提与实际consumer定位；不由名称存在推默认接线。'}},
        'premises_and_counterexample': {'input_domain': premise,
                                       'ordinary_control': first(x, ['ordinary_control', 'normal_control', 'comparison', 'ordinary_contrast']),
                                       'minimal_counterexample': first(x, ['minimal_counterexample', 'minimal_counterexample_to_an_overbroad_interpretation']),
                                       'failure_cancel_partial_commit': cancellation,
                                       'impact': x.get('impact', row['root_decision_reason']),
                                       'evidence_levels_and_execution': levels},
        'minimum_revision_contract': {'rule': rules, 'preserve_correct_scope': preserve,
                                      'root_scope_override': row['root_decision_reason'],
                                      'synchronization_original_contract': sync_raw,
                                      'candidate_formal_write_set': writes,
                                      'read_only_source_set': sorted({a['payload_identity']['path'] for a in source if a['payload_identity'] and a['payload_role']=='reference'}),
                                      'administrative_sync_owner': 'R6-I only, after actual integrated review; audit/planning are not reviewed-source write targets'},
        'acceptance_and_regression': {'conditions_and_vectors': acceptance, 'original_dependencies': deps,
                                      'history_regression': '保留R1原WP、R2 229/21/341、R3 23/76、R4 17/76与B5 16/75限定、R5唯一92CLOSED原精确scope。按实际受影响path/span及接口取回归；旧PASS不替新验收。',
                                      'static_acceptance_without_host': True, 'host_unknown_not_promoted': True},
        'independent_adjudication': {'proposer': x.get('proposer', x.get('proposal_origin', reader)),
                                     'non_proposer_records': counter, 'counter_evidence_ids': counter_ids,
                                     'arbitrator': row['root_arbitrator'], 'decision_reason': row['root_decision_reason'],
                                     'decided_at': row['decided_at'], 'conflicting_reports_preserved': True},
        'dependencies_and_receivers': {'original_dependencies': deps, 'primary_batch': None,
                                       'blocking_author_dependencies': [],
                                       'integration_receiver': 'R6-I', 'shared_file_writer': 'R6-I',
                                       'closure': '候选PASS、唯一写者接收后的独立实际结果PASS、全部接口/精确历史回归、正式接受、最后CLOSED依次分别登记。',
                                       'policy': '准确记录源行为不决定未来保留缺陷；六既有独立policy继续隔离。',
                                       'excluded_claims': ['full host/Demo', 'native graphics/audio/input equivalence', 'unbounded plugin/configuration combinations', 'real save/network/production service success']},
        'original_full_proposal': x,
        'original_proposal_status_scope':'原始提案/子任务阶段的PENDING或待裁字段按生成时点保留；本记录identity_and_verdict及独立root裁决为当前状态。',
        'non_proposer_packet_scope_correction':correction,
    }
    records.append(record)

validation = []
for x in records:
    if x['identity_and_verdict']['classification'] != 'required':
        continue
    for key, value in [
        ('source', x['bidirectional_evidence']['source']), ('formal', x['bidirectional_evidence']['formal']),
        ('premises', x['premises_and_counterexample']['input_domain']),
        ('control', x['premises_and_counterexample']['ordinary_control']),
        ('counterexample', x['premises_and_counterexample']['minimal_counterexample']),
        ('minimum_rule', x['minimum_revision_contract']['rule']), ('preserve_scope', x['minimum_revision_contract']['preserve_correct_scope']),
        ('acceptance', x['acceptance_and_regression']['conditions_and_vectors']),
        ('counter', x['independent_adjudication']['counter_evidence_ids']),
        ('write_set', x['minimum_revision_contract']['candidate_formal_write_set']),
    ]:
        if not value:
            validation.append({'id': x['id'], 'missing': key})
    for a in x['bidirectional_evidence']['source'] + x['bidirectional_evidence']['formal']:
        if not a['identity_resolved']:
            validation.append({'id': x['id'], 'unresolved_locator': a['locator']})
save('findings/normative-records.json', records)
save('findings/evidence-binding-index.json', evidence)
save('findings/normalization-validation.json', {'required_contract_gaps': validation, 'records': len(records),
     'classification': dict(collections.Counter(x['identity_and_verdict']['classification'] for x in records)),
     'aliases': [{'canonical': x['id'], 'aliases': x['aggregation_aliases']} for x in records if x['aggregation_aliases']]})
print(json.dumps({'records':len(records),'gaps':validation},ensure_ascii=False,indent=2))
