"""Publishable partial reading ledger. Parsing is never semantic credit."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[4]
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
READER = 'external /root; actual platform session ID UNVERIFIED'
CONTRACT = '30cfed0996003b6ebf4b5c51cc04f31ca9255440'
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'

def save(name, data):
    (TASK / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def ident(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

def leaves(value):
    if isinstance(value, dict):
        return sum(leaves(x) for x in value.values())
    if isinstance(value, list):
        return sum(leaves(x) for x in value)
    return 1

def esc(s):
    return s.replace('~', '~0').replace('/', '~1')

inventory = json.loads((TASK / 'material-inventory.json').read_text())
documents = {}
for row in inventory:
    assert ident(Path(row['materialized_path'])) == {
        'bytes': row['bytes'], 'sha256': row['sha256'], 'git_blob': row['git_blob']}
    if row['index'] not in (2, 9):
        documents[row['index']] = json.loads(Path(row['materialized_path']).read_text())

# FULL_READ means the whole original payload was actually displayed and read.
full = {2, 3, 4, 7, 8, 17, 23, 24}
contract_files = {0, 1, 15}
units = []
ledger = []
dispositions = []

for row in inventory:
    i = row['index']
    entry = dict(row)
    entry['semantic_status_at_materialization'] = entry.pop('semantic_status', 'UNREAD')
    entry['prior_history_current_status_in_readset'] = entry.pop('reading', 'UNVERIFIED')
    entry.update(reader=READER, recorded_after_read_utc=NOW,
                 exact_read_start_utc='UNVERIFIED_NOT_CAPTURED',
                 final_root_reception='NOT_RECEIVED',
                 behavior_execution='NOT_EXECUTED',
                 previous_reader_credit_imported=False)
    if i in full:
        entry.update(read_status='FULL_READ', read_ranges=['entire payload'],
                     semantic_scope='Read what the historical record claims, including its qualifications. Supporting facts are not automatically reverified for B8.')
    elif i in contract_files:
        entry.update(read_status='FIELD_SCOPE_READ',
                     read_ranges=['all top-level fields except /records', '/records/0'],
                     unread_ranges=[{'pointer': '/records', 'inclusive_indices': [1, 36]}],
                     semantic_scope='First complete record only; no sampling inference to remaining records. C13 record0 groups were read in canonical0 and equal field values explicitly associated.')
    elif i == 16:
        entry.update(read_status='FIELD_SCOPE_READ_WITH_EXACT_VALUE_ASSOCIATION',
                     read_ranges=['/records/0 through /records/36', '/qualification'],
                     associated_ranges=[{'pointer': '/additional_facets', 'same_value_as_file': 24,
                                         'proof': 'structure-equality.json'}],
                     qualification='All37 alias rows read; facet original values read in file24. This is not a whole lexical file FULL_READ or proof of root cause equivalence.')
    elif i == 18:
        entry.update(read_status='FIELD_SCOPE_READ_WITH_INVENTORY_DISPOSITION',
                     read_ranges=['all top-level fields except /inputs', '/records/0 through /records/36'],
                     inventory_only_ranges=['/inputs/0 through /inputs/59'],
                     qualification='All37 integrity statements read, not all37 original proposal/counter chains. Input rows have exactly bytes,path,sha256,snapshot; identity navigation only.')
    else:
        entry.update(read_status='STRUCTURE_PARSED_SEMANTIC_READ_INCOMPLETE',
                     read_ranges=[], unread_ranges=['all semantic fields unless a narrower receipt is explicitly listed'],
                     qualification='Exploratory key/size listings and truncated displays grant no FULL_READ. Current semantic fields have not been bulk classified as administrative.')
    ledger.append(entry)
    if i in (2, 9):
        n = len(Path(row['materialized_path']).read_bytes().splitlines())
        units.append({'file_index': i, 'line_range': [1, n], 'status': 'FULL_READ' if i in full else 'UNREAD',
                      'purpose': 'historical report and current qualifications' if i == 2 else 'complete Chinese handoff contract and embedded records; semantic obligation remains',
                      'independent_requirement_count': False})
    else:
        for key, value in documents[i].items():
            pointer = '/' + esc(key)
            split = isinstance(value, list) and key in {'records', 'limits', 'inputs'} and i not in {19, 20, 21, 22}
            parts = [(pointer + '/' + str(j), x) for j, x in enumerate(value)] if split else [(pointer, value)]
            for p, v in parts:
                status = 'UNREAD'
                purpose = 'CURRENT_SEMANTIC_OR_QUALIFICATION_OBLIGATION_NOT_BULK_ADMINISTRATIVE'
                if i in full:
                    status = 'FULL_READ'
                elif i in contract_files and (key != 'records' or p == '/records/0'):
                    status = 'FULL_READ' if i != 15 or key != 'records' else 'READ_VALUES_ASSOCIATED'
                elif i == 16:
                    status = 'READ_VALUES_ASSOCIATED' if key == 'additional_facets' else 'FULL_READ'
                elif i == 18:
                    status = 'INVENTORY_ONLY' if key == 'inputs' else 'FULL_READ'
                elif i == 10 and key == 'all_core_logical_payloads':
                    status = 'INVENTORY_ONLY'
                    purpose = 'TRANSPORT_IDENTITY_INDEX_ONLY; no underlying payload reading/execution/approval credit'
                units.append({'file_index': i, 'pointer': p, 'status': status,
                              'exact_inclusive_array_indices': [0, len(v)-1] if isinstance(v, list) and v else None,
                              'array_member_count': len(v) if isinstance(v, list) else None,
                              'scalar_leaf_count_for_bookkeeping_only': leaves(v),
                              'purpose': purpose, 'independent_requirement_count': False})
    dispositions.append({'file_index': i, 'path': row['path'], 'original_purpose': row['purpose'],
                         'current_use': entry.get('semantic_scope', entry.get('qualification')),
                         'read_status': entry['read_status'], 'R8_source_or_spec_approval': False,
                         'supporting_evidence_reception': 'UNVERIFIED_EXCEPT_EXPLICIT_RECORD0_SCOPE',
                         'preserve_generation_time_and_successor_states': True})

counts = {
    'readset_payloads': len(inventory),
    'readset_decoded_bytes': sum(x['bytes'] for x in inventory),
    'original_C2_identities_verified': len(inventory),
    'material_missing': 0,
    'full_payloads_read': len(full),
    'full_payload_decoded_bytes': sum(x['bytes'] for x in inventory if x['index'] in full),
    'payloads_without_whole_file_FULL_READ': len(inventory) - len(full),
    'canonical_records': 37, 'canonical_records_fully_read': 1,
    'canonical_records_not_fully_read': 36,
    'original_findings_records_fully_read': 1, 'original_findings_records_not_fully_read': 36,
    'C13_records_read_or_exact_value_associated': 1, 'C13_records_not_fully_read': 36,
    'C19_integrity_rows_read': 37, 'C19_integrity_rows_are_full_proposal_credit': False,
    'alias_rows_read': 37, 'additional_optional_facet_records_read': 2,
    'C17_limit_successor_rows_read': 14,
    'R8_final_root_received_records': 0, 'R8_final_root_not_received_records': 37,
    'new_behavior_runs': 0, 'findings_submitted': 0,
    'global_no_required_revision_claim': False,
}
unit_counts = {}
for u in units:
    unit_counts[u['status']] = unit_counts.get(u['status'], 0) + 1

save('reading-ledger.json', {'schema': 'r8.external-h-c2.reading-ledger.v1',
     'reader': READER, 'recorded_utc': NOW, 'input_commit': CONTRACT, 'counts': counts,
     'entries': ledger, 'unit_status_counts': unit_counts,
     'unit_count_qualification': 'JSON field/record bookkeeping units, not independent facts or requirements; repeated versions are retained.',
     'raw_command_stream': 'Platform conversation only. No exported private stream or fabricated per-command timestamp/exit log.',
     'truncation_rule': 'Exploratory truncated output grants no credit. Canonical0 subsequently reread whole compactly; alias facets associated with complete file24 values. All other truncations remain uncredited.'})
save('semantic-units.json', {'schema': 'r8.external-h-c2.units.v1', 'units': units})
save('purpose-dispositions.json', {'schema': 'r8.external-h-c2.purpose.v1', 'entries': dispositions,
     'special_manifest_disposition': 'transport-index-purpose-disposition.json',
     'no_blanket_administrative_exclusion': True})
save('unread.json', {'schema': 'r8.external-h-c2.unread.v1', 'status': 'INCOMPLETE_READABLE_SEMANTIC_DEBT',
     'counts': counts, 'unread_units': [x for x in units if x['status'] == 'UNREAD'],
     'whole_file_FULL_READ_missing': [x['index'] for x in inventory if x['index'] not in full],
     'all37_final_root_reception': 'NOT_RECEIVED; main reviewer must receive actual scope, no inferred acceptance from this delivery',
     'prior_receipts': {'reading-ledger_at_30cfed0': 'FULL_READ receipt document only; no wholesale source credit imported',
                        'current-nonmandatory-semantic-records.json': 'NOT_RECEIVED_IN_FULL_BY_EXTERNAL',
                        'R7-stage-identity-audit.json': 'NOT_RECEIVED_IN_FULL_BY_EXTERNAL'},
     'further_supporting_evidence': 'Remaining36 records require their exact original proposal/counter/evidence and necessary B8/R consumers, including any manifest-only semantic payloads. Expanded evidence denominator remains open; do not report it as zero.',
     'R6_original_limit_records': 'NOT_READ_IN_FULL_BY_EXTERNAL; C17 successor14 read, not substituted for original L01-L14.',
     'material_limit': False, 'reason': 'This actual context did not complete the assigned full semantic reading. Available unread material is reading debt, not a host/material limit.',
     'update_status': 'UPDATE_NOT_STARTED'})

save('history-current-acceptance.json', {
    'schema': 'r8.external-h-c2.acceptance.v1', 'reader': READER, 'recorded_utc': NOW,
    'stage': 'HISTORICAL_RECORD_SEMANTICS_READ_WITH_BOUNDED_CURRENT_COUNTERCHECK',
    'root_final_acceptance': 'NOT_RECEIVED', 'global_pass': False,
    'record0': {'id': 'GR7-M01-001',
        'original_C2_state': 'required P2; R7 report record accepted, manual update then not started',
        'original_proposal_status': 'PROPOSED and PENDING_OTHER_ACTUAL_REVIEWER are preserved generation-time author fields',
        'original_counter_scope': 'TownMap minimal case; inspected declarations support four other integer-only kinds; original unread tails remain historical limits of that counter',
        'current_B8_countercheck': 'WP03 section3.1 and catalog GR7-M01-001-V1/V2/V3 retain separation of integer-key lookup, numeric-sequence equality and same-kind primary identity. No new contradiction established in this bounded scope.',
        'source_to_spec': [
            {'fact': 'TownMap and the four named kinds initialize integer primary identity without another numeric sequence; inherited integer comparison is separate.', 'source': 'R GameData full + five complete declaration files', 'spec': 'B8 WP03 section3.1; catalog V1/V2'},
            {'fact': 'Same-kind primary identity comparison is separate from number comparison.', 'source': 'R GameData instance comparison complete method', 'spec': 'B8 WP03 section3.1; catalog V2'},
            {'fact': 'TerrainTag Grass carries numeric sequence2; valid Item symbol/string comparison remains supported.', 'source': 'R TerrainTag and Item complete files; PBS EXPSHARE section and battle experience consumer method', 'spec': 'B8 WP03 section3.1; catalog V3'}],
        'premises': ['valid normally registered records', 'no equality/query override or extra numeric sequence', 'read-only direct query/comparison'],
        'normal_controls': ['TownMap lookup1 succeeds and same-kind ID1 equals', 'TerrainTag Grass versus2 true', 'valid EXPSHARE Item versus corresponding symbol/string true'],
        'minimal_case': 'TownMap record with primary identity1 versus integer1 normally yields false; registration lookup1 still succeeds.',
        'failure_cancel_partial_commit': 'False is a normal Boolean result. Comparison has no write/cancel/save/partial-commit flow; existing class-specific query overrides are preserved.',
        'evidence_levels': ['SOURCE_STATIC', 'DERIVED_VECTOR'], 'execution': 'NOT_EXECUTED',
        'source_negative_scope': 'Full eight source files and complete experience consumer method only. No new whole010_Data/plugin negative-evidence claim.',
        'correct_scope_preserved': 'No assertion that all integer lookups fail, all comparisons fail, or ordinary gameplay fails. Future compatibility choice remains separate.',
        'not_proved': ['all other assertions in the two fully read formal files', 'remaining36 full contracts', 'complete historical negative-search logs', 'original27 closure qualification', 'runtime/host equivalence'],
        'independent_root_reception': 'PENDING_MAIN_REVIEWER'},
    'classification_and_limits': {
        'alias_37_rows': 'Read as alias/historical-relation metadata; null legacy root fields are not invented IDs.',
        'two_optional_aliases': ['GR7-M13-002 -> R6-UI-PARTY-003', 'GR7-M18-001 -> R6-D-FONT-C01'],
        'facets': 'OF01/OF02 preserve valid alternative navigation; their two entries do not expand the mandatory DEBUG001 scope or add canonical roots.',
        'policy': 'UTIL-03 terminal-LF fact qualification and the new font compatibility policy remain unselected distinct entries; not mandatory adoption.',
        'limits': 'All14 C17 successor statements read, including overlays. Their supporting source/host and original R6 records remain separately unverified.'},
    'historical_state_rule': 'C2 UPDATE_NOT_STARTED, R7 remediation ACCEPTED/CLOSED, and B8 current clauses are different objects/stages; no rewriting old ledgers.',
    'update_status': 'UPDATE_NOT_STARTED'})
save('findings.json', {'schema': 'r8.external-h-c2.findings.v1', 'records': [],
     'new_findings': 0, 'independent_counter_requests': [], 'required_classification_by_this_task': 0,
     'conclusion': 'No new contradiction established in the explicitly read and counterchecked scope. This is not NO_REQUIRED_UPDATE or global PASS; unread debt prevents a complete conclusion.',
     'final_adjudicator': 'main reviewer; NOT_RECEIVED', 'update_started': False})

progress = json.loads((TASK / 'progress.json').read_text())
progress.update(state='INTERRUPTED', semantic_reception='NOT_ACCEPTED', updated_utc=NOW,
                status_detail='PARTIAL_EVIDENCE_READY_FOR_PUBLICATION; full assigned reading incomplete',
                counts=counts, global_pass=False,
                behavior_execution='NOT_EXECUTED', new_behavior_runs=0,
                report='report.md', unread='unread.json',
                publication_state='PENDING_COMMIT_PUSH_AND_REMOTE_READBACK')
save('progress.json', progress)

report = f'''# H-C2-CURRENT-RECORDS 外部审读阶段证据

本任务**未完成全量语义审读**。可读缺读保留为阅读债务，不标材料 limit，不给全量 PASS／NO_REQUIRED_UPDATE。最终接收交主审；UPDATE_NOT_STARTED。

任务输入固定于 `{CONTRACT}`；唯一当前 B8 为 fd1df570cad987dc3852a3b958f03916e317f7fe，workspace tree751dfde81048c81390f89a65ca1d1a565ba8e1ca，formal treef292698cdd4a8e725525a9be6dc34b75faaf151e。C2为 `{C2}`／tree1f4375e2a51801ed62bc143c1d51f70296fa52f3。R为8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b／tree7589c800b61ba13a13040ed0d686979b80a84fd0。

实际项目路径 /workspace/pokemon-essentials-clean-room；R路径 /workspace/pokemon-essentials。唯一写集为本目录，唯一分支 codex/r8-external-h-c2-current-records-20261016。用户本次明确授权 own-directory commit 和普通 push，替代原共享容器 no-commit/push 条款；其余合同保留。没有 spawn、整改、main/tag／正式规格／R／公共台账写入。

25/25载荷原对象、mode/blob/bytes/SHA256均已核；解码总分母113,396,087字节。10个压缩载荷在此前不存在、无symlink的独立目录恢复，解码15,103,963字节，保留编码／解码双身份；另恢复首记录必要的3份证据13,705字节。恢复只产生材料，不执行证据程序。大文件及恢复文件不重复提交；原gzip位于固定C2树中，恢复方法和全部身份在恢复manifest。本目录readset保留原25行及原write_root，最新独占写集覆盖关系由progress明确。

全文实际已读8/25载荷，合计{counts['full_payload_decoded_bytes']:,}字节；其余17份没有整文件FULL_READ。37条canonical原记录只完整实读首条；其余36条、findings其余36条、C13其余36条仍缺完整审读。C19的37行完整性声明、aliases的37行、2个optional facet、C17的14个limit后继声明均有各自字段范围；它们不能代替37条原合同或支撑事实。主审最终接收0/37，待接收37/37。

首条GR7-M01-001已完整读canonical、原finding、原作者snapshot、独立counter及对应中文组值；新读固定R的8个完整源文件、EXP consumer完整方法及EXPSHARE节，B8 WP03完整393行和测试目录完整236行。当前§3.1与V1/V2/V3保留查找、同类主身份比较、整数序号比较及查询覆写的区别，限定范围未建立新矛盾。两篇正式文件的其它事实虽已读，不因此变成全部事实核验完成。

约80MB manifest已核真实结构。仅/all_core_logical_payloads按传输身份索引用途处置：34,251逻辑路径、21,449编码对象及74个本地私有流导航。其余当前规则、案例、依赖、事实、状态未一概标行政。与独立载荷的23个JSON值关联证明只供定位、去重，不自动授予全文阅读。尤其manifest-only的source_units、formal_units、tasks等内容仍须按真实用途审读。具体结构单元和未读pointer集合见semantic-units／unread。

14个limit后继、两个optional根别名、两个导航facet和UTIL-03政策资格分别保留。C2生成时PROPOSED／PENDING字段与后继root reception分层；原27关闭与B8当前条款分开。本任务未完整读R6原L01–L14及全部支撑证据，不能用后继接收记录替代。

请求配置为gpt-6.1-sol／ultra／default普速／Fast关闭；实际model、effort、tier、speed及自己的平台ID均UNVERIFIED。source_thread_id为调用方提供，不能冒充本context平台ID。行为执行NOT_EXECUTED，新增0。平台对话保留实际工具输出；未导出私有流，未倒填独立UTC／stdout／stderr／退出记录。

交付reading-ledger、purpose-dispositions、history-current-acceptance、findings、unread、逐结构台账、双身份恢复manifest和发布回读证据。没有新发现提交不代表全局无需修订。可读缺读仍阻塞本任务完成；未出现材料不可读或权限拒绝。
'''
(TASK / 'report.md').write_text(report)
print(json.dumps({'counts': counts, 'unit_status_counts': unit_counts}, ensure_ascii=False))
