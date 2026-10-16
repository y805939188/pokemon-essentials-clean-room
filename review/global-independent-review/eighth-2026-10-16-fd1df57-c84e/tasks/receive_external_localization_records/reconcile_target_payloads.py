"""Bind duplicate target views to fixed sources; no semantic credit from generation."""
from pathlib import Path
import collections
import hashlib
import json
import re
import subprocess

T = Path(__file__).resolve().parent
P = T / 'evidence/recovered-target'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B = 'fd1df570cad987dc3852a3b958f03916e317f7fe'

def load(p):
    return json.loads(p.read_text())

def save(p, value):
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

cache = {}
def fixed(which, path):
    key = which, path
    if key not in cache:
        cmd = ['git'] + (['--git-dir=/tmp/r8-elr-reception-reference.git'] if which == 'R' else [])
        cache[key] = subprocess.check_output(cmd + ['show', (R if which == 'R' else B) + ':' + path])
    return cache[key]

def check_numbered(view, which, path, ranges):
    text = view.read_text().splitlines()
    if text[0].startswith('FILE '): text = text[1:]
    expected = [n for a, b in ranges for n in range(a, b + 1)]
    seen = []
    source = fixed(which, path).decode('utf-8-sig').splitlines()
    for line in text:
        m = re.fullmatch(r'(\d+)(?:: | )(.*)', line)
        assert m, (str(view), line)
        n = int(m[1]); seen.append(n)
        assert source[n - 1] == m[2], (str(view), n)
    assert seen == expected, (str(view), seen[:2], expected[:2])
    return {'view': str(view.relative_to(P)), 'source': which + ':' + path, 'ranges': ranges,
            'bytes': view.stat().st_size, 'sha256': hashlib.sha256(view.read_bytes()).hexdigest(),
            'all_numbered_lines_exact': True, 'semantic_credit_from_binding': 0}

def source_views():
    proofs = []
    for view in sorted((P / 'evidence/units').glob('*.txt')):
        head = view.read_text().splitlines()[0]
        m = re.fullmatch(r'FILE ([RB]) (.*) L(\d+)-(\d+)/(\d+)', head)
        assert m, head
        proofs.append(check_numbered(view, m[1], m[2], [[int(m[3]), int(m[4])]]))
    rows = load(P / 'evidence/continuation/own-reading-ledger.json')['source_rows']
    for row in rows:
        if 'view' not in row: continue
        proofs.append(check_numbered(P / row['view'], 'R', row['identity']['path'], row['ranges']))
    image = load(P / 'evidence/continuation/image-unit-inventory.json')
    for row in image:
        view = P / row['view']
        proofs.append(check_numbered(view, 'R', row['path'], [row['range']]))
    return proofs

def corpus_views():
    received = {x['id'] for x in load(T / 'continuation/received-parts/parent-acceptance.json')['records']}
    received |= {x['id'] for x in load(T / 'reading-ledger.json')['literal_record_reads']}
    decoder = json.JSONDecoder()
    proofs = []
    for view in sorted((P / 'evidence/reads').glob('*.txt')):
        domain, first, last = re.fullmatch(r'(.*)-(\d+)-(\d+)\.txt', view.name).groups()
        raw = (T / 'evidence/primary-reference' / (domain + '.txt')).read_text(encoding='utf-8-sig').splitlines()
        lines = view.read_text().splitlines()
        assert lines[0].startswith('FILE ' + domain + '.txt ')
        for n in range(1, 5): assert lines[n] == 'L' + str(n) + ' ' + json.dumps(raw[n - 1], ensure_ascii=False)
        ids = []
        for line in lines[5:]:
            equal = re.fullmatch(r'R(\d+) L(\d+)/(\d+) key=translation=(.*)', line)
            if equal:
                n, a, z = map(int, equal.groups()[:3]); key = value = json.loads(equal[4])
            elif line.startswith('"'):
                n = int(first) + len(ids); a, z = 2*n + 3, 2*n + 4
                key = value = json.loads(line)
            else:
                m = re.match(r'R(\d+) L(\d+) key=', line); assert m, line
                n, a = int(m[1]), int(m[2]); key, pos = decoder.raw_decode(line[m.end():])
                rest = line[m.end() + pos:]; end = re.match(r' L(\d+) translation=', rest); assert end
                z = int(end[1]); value = json.loads(rest[end.end():])
            assert [a, z] == [2*n + 3, 2*n + 4] and [key, value] == [raw[a-1], raw[z-1]]
            ids.append('ELR-' + domain + '-' + str(n).zfill(4))
        expected = ['ELR-' + domain + '-' + str(n).zfill(4) for n in range(int(first), min(int(last), (len(raw)-4)//2) + 1)]
        assert ids == expected
        missing = [i for i in ids if i not in received]
        proofs.append({'view': str(view.relative_to(P)), 'domain': domain, 'record_ids': ids,
                       'all_raw_fields_exact': True, 'headers_exact': True,
                       'actual_reader_received_pairs': len(ids)-len(missing), 'pending_reader_ids': missing,
                       'new_literal_reading_credit': 0})
    return proofs

def primary_json():
    rd = load(P / 'reading-ledger.json'); fw = load(P / 'forward-mapping.json')
    units = {x['id']: x for x in rd['units'] if 'record' in x}
    assert len(units) == len(fw['records']) == 10697
    pure = {'id', 'identity', 'lines', 'record', 'key_sha256', 'translation_sha256'}
    templates = collections.defaultdict(lambda: collections.defaultdict(list))
    for key, row in units.items():
        domain = key[4:].rsplit('-', 1)[0]
        business = {k:v for k,v in row.items() if k not in pure}
        templates[domain][json.dumps(business, ensure_ascii=False, sort_keys=True)].append(key)
    groups = {g['id']:g for g in fw['fact_groups']}
    for row in fw['records']:
        unit = units[row['unit']]; group = groups[row['fact']]
        assert unit['fact_group'] == row['fact'] and row['consumer'] == group['receiver']
        assert row['spec_clauses'] == ['WP08-30','WP08-51','WP08-130','WP08-153','WP08-155']
        assert row['reception'] == 'WAIT_ROOT' and row['evidence_level'] == 'SOURCE_STATIC'
        assert set(row) == {'unit','fact','consumer','spec_clauses','reception','evidence_level'}
    factored = {domain:[{'business':json.loads(value),'ids':ids} for value,ids in variants.items()] for domain,variants in templates.items()}
    return {'schema':'gr8-elr-original-primary-exact-factoring/v1', 'record_templates':factored,
            'all_original_units_reconstructed_exactly':True, 'all_forward_records_match_exact_group_receiver_and_shared_fields':True,
            'original_FULL_READ_WAIT_ROOT':'Original author historical states, never new receiver reading credit.',
            'actual_literal_reception':'Parent433 + named A/B/C5437; D4827 still pending.', 'generation_credit':0}

def purposes(source, corpus):
    source_map = {r['view']: n for n,r in enumerate(source)}
    corpus_map = {r['view']: n for n,r in enumerate(corpus)}
    explicit = {
        'continuation-review.md': ('FULL_REPORT_MEANING_RECEIVED','完整后继报告；七有限C01–07及两原OPEN保留，不冒全历史/PBS通过。'),
        'review.md': ('FULL_REPORT_MEANING_RECEIVED','完整初稿报告/原提案与边界；旧PROPOSED不推翻后继root有限裁决。'),
        'interfaces.json': ('FULL_FINITE_INTERFACE_FIELDS_RECEIVED','七完整local_evidence/pending/status/blocking/资格及原incoming/outgoing计数已读，原时点不转授。'),
        'progress.json': ('FULL_STATUS_AND_QUALIFICATIONS_RECEIVED','原配置/实际UNVERIFIED、过程、失败、读者分母和剩余已读；身份/UTC仅原记录。'),
        'identities.json': ('IDENTITY_WITH_AUTHORIZATION_CONFIGURATION_QUALIFICATION','payloads/continuation-own/peer身份数组仅绑定对象；原授权覆盖、请求/实际配置、启动/路径/库存资格及五合同use已全文读，不把旧角色指令当本任务授权。'),
        'proposals.json': ('FULL_PROPOSAL_RECEIVED','ELR001八节/正常反例/最强no-required/部分失败/同步/验收完整，后继独立反证与root裁决另具名。'),
        'reading-ledger.json': ('EXACT_SEMANTIC_FACTORING_LITERAL_RECEPTION_SEPARATE','全部unit业务字段20种精确变体、18file业务字段、41依赖资格/续读范围已呈现；10697文字信用按parent/named reader分列，D待接。'),
        'forward-mapping.json': ('EXACT_SEMANTIC_FACTORING_LITERAL_RECEPTION_SEPARATE','18完整fact_group及10697forward共享字段/每域receiver/7续接事实已读并严格核对；不因原WAIT_ROOT建立新接收。'),
        'reverse-mapping.json': ('FULL_FINITE_REVERSE_MEANING_RECEIVED','125完整条款398子断言及LZ41、七续接反向字段实际读完，原定位与实际完整必要定义分列。'),
        'evidence/assignment-metadata.json': ('FULL_ASSIGNMENT_FIELDS_RECEIVED','9项任务/精确selected_paths/status/reason作为原分派元数据；NOT_RECEIVED不是当前结论。'),
        'evidence/continuation/37-title-projection.json': ('FULL_NAVIGATION_RECEIVED_NOT_CONTRACT_BODIES','37完整title/canonical/root/alias只作导航；不把这些标题当完整历史原合同。'),
        'evidence/continuation/all-dependency-personal-ranges.json': ('FULL_RANGE_ACCOUNTING_QUALIFICATION_RECEIVED','54路径/12whole42partial/22022未读为原作者范围；区间与计数身份用途，不授源正文新信用。'),
        'evidence/continuation/image-unit-inventory.json': ('FULL36_FACT_OBJECTS_RECEIVED','全部36完整meaning/premise/status与63调用定位已接收；对应36必要方法实际完整读完。'),
        'evidence/continuation/limit-records.json': ('FULL14_CURRENT_LIMIT_OBJECTS_RECEIVED','L01–L14完整当前记录、前提/输入/输出/owner/限制；原更老载荷未回收资格保留，不冒历史运行。'),
        'evidence/continuation/own-reading-ledger.json': ('FULL_READING_QUALIFICATIONS_RECEIVED','31source_rows范围/whole/partial资格及derivedMain/limits/I-O/技术失败已读；原whole不转为本接收者。'),
        'evidence/continuation/peer-reception.json': ('FULL7_FINITE_FACTS_AND_QUALIFICATIONS_RECEIVED','C01–07全文；UI17-U045原164超过源157 EOF，仅有限icon事实，不接受不可能范围。'),
        'evidence/continuation/unread-scope-routing.json': ('FULL_NECESSARY_ROUTE_FIELDS_RECEIVED','18局部原范围/owner/必要scope及35PBS必要字段/激活/未收body资格已接；本轮35字段投影另证，不签其它PBS正文。'),
        'evidence/execution-boundaries.json': ('FULL_EXECUTION_QUALIFICATIONS_RECEIVED','全部零执行与原工具失败/截断/未证字段已读，不倒填私有I/O。'),
        'evidence/pbs-dependencies.inventory-only.json': ('EXACT_IDENTITY_AND_NECESSARY_FIELD_INVENTORY','35路径身份和必要字段库存，仅定位；真实值/上下文阅读在pbs-field-binding及具名记录读者。'),
        'evidence/primary-mechanical-inventory.json': ('EXACT_PRIMARY_FORMAT_IDENTITY_ONLY','18原文件bytes/lines/BOM/CRLF/SHA/blob与5不等对定位；不把格式机械检查当文字阅读。'),
        'evidence/ui-resource-search.json': ('EXACT_LOCATOR_ONLY','原rg命中63调用只作定位；stdout不是完整caller，实际36方法独立接收。'),
        'evidence/read-invocations.jsonl': ('ORIGINAL_RENDER_INVOCATION_METADATA_ONLY','每条argv/UTC/范围/file/note仅原呈现定位；输出内容由38精确视图回查，不运行原helper。'),
        'evidence/unit-invocations.jsonl': ('ORIGINAL_RENDER_INVOCATION_METADATA_ONLY','每条repo/path/range/UTC/output/evidence_level只是原呈现定位；不以日志授函数全文。'),
    }
    selected = {
        'kernel-fact-matrix.json':'采用完整KER-F102–112及必要保存/lifecycle F113–125有限贡献；其余001–101/126–135更广业务断言不采用，原PARTIAL_NOT_PASS保留。',
        'media-data-getters.json':'MED-DATA01–09全部完整事实/普通/失败前缀及共前提接收，8源身份用途；不接全部编译数据人口。',
        'media-encoding.json':'完整本地化/序列化encoding有限贡献已接收；字符串/元数据/压缩Main字节和运行资格分列。',
        'media-kernel-core.json':'完整kernel15+3、core4及必要绑定接收；仅这些有限接口，不批准整个kernel或combat领域。',
        'media-messages.json':'完整messages结构/字节/5差异/178链接/加载边界贡献已接；所有文字仍按实际记录读者，非原生运行。',
        'media-progress.json':'完整原进度/部分native可读未读/字体与媒体运行资格已读，只采用ELR有关范围，不转授全native主责。',
        'media-ui-text.json':'完整36语义单元、全部共前提/资格/open/parentWP66接收；5+28源身份仅身份用途；不冒整个行政容器全文。',
        'pbs_battle--field-contracts.json':'全部字段文字已读，仅采用Name/Description/份量/身份/缺省/激活的有限合同；其它战斗属性未由本任务验收。',
        'resource_media_serialized_cloud--kernel-core-additional-binding-receptions.json':'完整必要Compiler/TrainerType与Core名称/优先级后继绑定已读，保留原有限source范围。',
        'resource_media_serialized_cloud--media-consumer-receptions.json':'采用完整UI17-U026–030/U034–036及共前提/资格；其它UI25对象不自动授全域或新caller信用。',
        'resource_media_serialized_cloud--static-recovery-001--current-serialized--Main.identity.json':'精确Scripts594/派生Main1197及49行身份/恢复资格；不执行解码产物。',
        'resource_media_serialized_cloud--static-recovery-001--current-serialized--Main.rb':'派生Main49行完整已读，仅静态装载/执行边界；不同于另外读的R999_Main60，不混对象。',
        'resource_media_serialized_cloud--ui-dex-name-consumer-reception.json':'完整7单元/24事实、所有资格和5身份已接；Area生产者61017B正文不由此批准。',
        'ui_full--kernel-consumers-interface.v2.json':'采用完整UI65-U001–004/U020/U022–025与UIKC001/002/032–035四图像trace，及与已接UI36严格重叠对象；其它66/30/9业务正文明确不采用、不授信用。',
        'ui_full--kernel-consumers-correction-and-dex-supplement.json':'完整Mart顺序更正、Dex补充/11事实、D01/D04/D05/D08/CFG02、Credits完整有限对象已读；21来源对象仅身份用途。',
    }
    report_names = {'kernel-report.md','ui_full--review.md','ui_minigames--review.md','pbs_battle--review.md','pbs_creature_facility--review.md','pbs_world_record_audit--review.md',
        'external_h_c2_current_records--report.md','external_h_r6_effective_contracts--report.md','h_r7_final_receptions--report.md','history_current--report.md'}
    entries = []
    for row in load(T / 'reading-ledger.json')['target_file_states']:
        path = row['path']; local = P / path; b = local.read_bytes()
        assert len(b) == row['bytes'] and hashlib.sha256(b).hexdigest() == row['sha256']
        out = {k:row[k] for k in ['path','bytes','sha256','mode','git_blob']}
        if path in source_map:
            out.update(purpose='EXACT_FIXED_SOURCE_VIEW_ALIAS', meaning='逐行固定源别名；必要完整方法的实际阅读/具名接收见source ledger与七接口，邻接partial或其它函数不授whole。', proof={'source_view_index':source_map[path]})
        elif path in corpus_map:
            view = corpus[corpus_map[path]]
            out.update(purpose='EXACT_CORPUS_LITERAL_VIEW_ALIAS', meaning='原完整字段重复呈现；按精确ID接读者，不重复逐字阅读。', proof={'corpus_view_index':corpus_map[path]}, necessary_pending_reader_ids=view['pending_reader_ids'])
        elif path in explicit:
            out.update(purpose=explicit[path][0], meaning=explicit[path][1])
        elif path.startswith('evidence/continuation/received/') and local.name in selected:
            out.update(purpose='EXPLICIT_FINITE_CONTRIBUTION_SCOPE', meaning=selected[local.name])
        elif path.startswith('evidence/continuation/received/') and local.name in report_names:
            out.update(purpose='FULL_REPORT_READ_FINITE_QUALIFICATION_ONLY', meaning='报告全文已读；采用其中ELR必要接口、实际读者/开放/执行/历史资格。报告之外原大域记录/正式正文/提案不会由报告全文转授。')
        elif path.startswith('evidence/contracts/'):
            out.update(purpose='FROZEN_ORIGINAL_CONTRACT', meaning='原AGENTS/global/skill全文与本任务固定合同逐字同源；原localization prompt全文及18条readset所有语义资格已读，路径/模式/blob/SHA字段作身份库存。原角色/旧写集指令不覆盖当前用户授权。')
        elif path.endswith('.py'):
            out.update(purpose='AUTHOR_REPORT_TOOL_NOT_EXECUTED_NOT_ADOPTED_AS_BEHAVIOR', meaning='保留原审者工具源字节，非参考行为/当前规则合同。仅采用独立接收并固定校验的报告/视图输出；不靠helper源码或exit作业务证明。read_records/read_units已全文看用途，其余代码正文未获全文阅读信用。')
        elif any(token in path for token in ['remote-readback','publication-receipt','publication-core-io','preflight-io','package-validation','fetched-peer-manifest']) or path=='identities.json':
            out.update(purpose='EXPLICIT_TRANSPORT_AND_IDENTITY_ONLY', meaning='身份/集合/mode/blob/bytes/SHA/路径/UTC/argv/原exit/stdout/stderr及旧机械检查结果。失败与资格已读并保留；仅绑定原载荷与原进程，不作源行为或语义PASS。原stdout非私有事件流导出，非当前执行。')
        else:
            raise AssertionError('Unassigned exact target purpose: ' + path)
        out['whole_file_semantic_acceptance_from_generation'] = False
        entries.append(out)
    assert len(entries) == 213
    return {'schema':'gr8-elr-exact-target-payload-purpose/v1','fixed_target':'90b9e27ef03feb2c018bb2f258b5e0d5aaed012b','entries':entries,
            'count':213,'generation_credit':0,'meaning':'每路径明确采用的实际有限字段/别名和未采用正文。不是全部文件FULL_READ清单；D值信用仍待实际读者。',
            'field_purpose_rules':{'pure_identity':'path/mode/blob/bytes/SHA/tree/line/range/ID/pointer只绑定精确对象；不赋新语义信用。',
                'business':'meaning/fact/premise/expected/default/enum/normal/cancel/failure/partial/reason/correction/open/qualification均须实际读；上述具体采用对象已在接收ledger和后继全文说明。',
                'unadopted_peer_business':'更大外域容器的其它业务正文明确未读/未采用，保留原owner；其存在不扩成本任务重审全系统。',
                'original_status':'原FULL_READ/WAIT_ROOT/PASS/OPEN为原时点，绝不批量改写为本审者。'}}

if __name__ == '__main__':
    source = source_views(); corpus = corpus_views(); primary = primary_json()
    save(T / 'continuation/target-view-reuse.json', {'schema':'gr8-elr-exact-target-view-reuse/v1','source_views':source,'corpus_views':corpus,
        'qualification':'Exact fixed-source aliases only. Actual source/record reader credit and necessary adopted scope remain separate; binding itself reading0.',
        'source_execution':'NOT_EXECUTED','recovered_scripts_execution':'NOT_EXECUTED'})
    save(T / 'continuation/original-primary-semantics.factored.json', primary)
    save(T / 'continuation/target-payload-purpose.json', purposes(source, corpus))
    print(json.dumps({'source_views_bound':len(source),'corpus_views_bound':len(corpus),'primary_records_structurally_factored':10697,'semantic_credit_from_tool':0}))
