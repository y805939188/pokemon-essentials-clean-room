"""Assemble this receiver's judgments and evidence pointers; never run old code."""
import json, pathlib, datetime, subprocess
from recover import T, ident, save

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
raw = json.loads((T / '.work/originals/0').read_text())['records']
proposals = json.loads((T / '.work/originals/1').read_text())['records']
notes = json.loads((T / 'judgments.json').read_text())
state = json.loads((T / 'view-state.json').read_text())
displays = json.loads((T / 'source-displays.json').read_text())
contract = json.loads((T.parent.parent / 'continuation-v2/A.complete.json').read_text())
recovery = json.loads((T / 'recovery.json').read_text())
status = json.loads((T / '.work/originals/200').read_text())
denom = [r['id'] for r in raw[1:13]]
assert [n['id'] for n in notes] == denom

def canonical_id(value):
    return ident(json.dumps(value, ensure_ascii=False, sort_keys=True,
                           separators=(',', ':')).encode())

def refs(value):
    out = []
    if isinstance(value, dict):
        if isinstance(value.get('path'), str):
            p = value['path']
            if p.startswith(('Data/Scripts/', 'PBS/', 'deliverables/')):
                out.append({k: v for k, v in value.items()
                            if k in ('path', 'scope', 'identity_id', 'original_scope_ref')})
        for v in value.values():
            out.extend(refs(v))
    elif isinstance(value, list):
        for v in value:
            out.extend(refs(v))
    seen = set()
    return [v for v in out if not (json.dumps(v, sort_keys=True) in seen or
                                  seen.add(json.dumps(v, sort_keys=True)))]

def ack_for(file, pointer):
    rows = [a for a in state['acks']
            if str(a['file']) == str(file) and a['pointer'] == pointer]
    assert len(rows) == 1, (file, pointer, len(rows))
    return rows[0]

records, interfaces = [], []
normalization_sha = 'f9b4669e58799ae9633f9784e1165754aa567aaaf3aeea0f2d5b2faf990dae44'
for i, n in enumerate(notes, 1):
    r = raw[i]
    literal_refs = refs(r) + refs(proposals[i])
    paths = {v['path'] for v in literal_refs}
    joined_displays = [j for j, d in enumerate(displays) if d['path'] in paths]
    old = {k: r[k] for k in ('id', 'canonical_id', 'canonical_root_id', 'aliases',
                             'title_zh', 'classification', 'severity', 'status',
                             'finding_status_at_frozen_root', 'root_original_record',
                             'authority', 'primary_batch', 'complete_chinese_groups_origin')}
    current = [d for d in status['decisions'] if d['id'] == r['id']]
    record = dict(n)
    record.update({
        'canonical_index': i,
        'scope_result': 'RECEIVED_COMPLETE_SCOPED_STATIC',
        'new_required_proposal': False,
        'new_formal_acceptance_or_closure': False,
        'original_current_values_preserved': old,
        'current_B8_state': current[0]['state'] if current else 'OPTIONAL_NOT_ADOPTED',
        'current_B8_state_qualification': 'Historical B8 authority only; A creates no new ACCEPTED/CLOSED and does not inherit source approval.',
        'seven_groups': [{'name': k, 'value_identity': canonical_id(v),
                          'source_pointer': f'/records/{i}/groups/{k}',
                          'reading': f'views/r{i}.*.txt + view-state.json'}
                         for k, v in r['groups'].items()],
        'original_field_binding_groups': {'keys': list(r['original_field_binding_groups']),
                                         'value_identity': canonical_id(r['original_field_binding_groups']),
                                         'reading': f'views/r{i}.*.txt; no locator substitutes for the original values'},
        'exact_display_receipts': [ack_for(0, f'/records/{i}'),
                                   ack_for(1, f'/records/{i}'),
                                   ack_for(normalization_sha, f'/records/{i}')],
        'supporting_complete_values': 'views/extras.*.txt + bundle100-binding.json: exact C13/C19/alias scopes and author/counter members; counter1/counter2 separately full',
        'old_locator_literals': literal_refs,
        'locator_qualification': 'Old author readsets (including whole-byte scopes) are accepted as literal historical fields, not claimed as this receiver whole-file reading. Current fixed source/spec ranges and complete necessary methods are independently shown in source-displays.json and joined by the authored reasoning.',
        'display_indices_for_declared_paths': joined_displays,
        'additional_source_and_clause_reading': 'See source-displays.json for complete method expansion and current added vectors beyond old line locators.',
        'own_unread': [],
        'behavior': 'NOT_EXECUTED',
        'limits': ['No physical input/media/file/host observation', 'No independent complete behavior model',
                   'No global historical deduplication or other partition signature',
                   'No optional/policy adoption; model/config UNVERIFIED']
    })
    records.append(record)
    interfaces.append({'id': r['id'], 'producer_caller_consumer_join': n['source_join'],
                       'current_B8_clause_join': n['b8_join'], 'compatibility_reason': n['resolution'],
                       'negative_control': n['strongest_counter'],
                       'fixed_reading_indices': joined_displays,
                       'extra_reading': record['additional_source_and_clause_reading'],
                       'scope': 'Only the stated facts and preserved boundaries; neither shared producer use nor a historical PASS grants other records a signature.'})

common = {'schema': 'r8-c2-reception-a-v1', 'utc': now,
          'contract_commit': '64cfde5aa3f6b25adc7291b2c2e880d87baf1ebd',
          'target_commit': contract['target_commit'],
          'branch': 'codex/r8-c2-reception-a-20261016',
          'receiver_context': '01a1448b-68af-70ff-b817-bacab22f0014',
          'status': 'READY_FOR_PARENT_RECEPTION', 'scope': 'A only',
          'behavior': 'NOT_EXECUTED', 'root_ACCEPTED_or_CLOSED_granted': False}
save(T / 'reception-ledger.json', dict(common, denominator=12, records=records))
save(T / 'interfaces.json', dict(common, records=interfaces))
save(T / 'proposal-counters.json', dict(common,
    new_required_proposals=[], new_required_count=0,
    current_covered_required=[n['id'] for n in notes if raw[denom.index(n['id'])+1]['classification']=='required'],
    optional_not_adopted=[n['id'] for n in notes if raw[denom.index(n['id'])+1]['classification']=='optional'],
    records=[{'id': n['id'], 'strongest_NO_REQUIRED_or_already_covered': n['strongest_counter'],
              'independent_resolution': n['resolution'], 'minimum_and_history': n['history'],
              'decision': 'No new mandatory proposal; parent/main reviewer retains final decision'} for n in notes]))
save(T / 'frozen-denominator.json', dict(common,
    records=[{'index': i, 'id': raw[i]['id'], 'classification': raw[i]['classification'],
              'severity': raw[i]['severity'], 'whole_current_record_identity': canonical_id(raw[i]),
              'whole_proposal_and_adjudication_identity': canonical_id(proposals[i]),
              'canonical_pointer': f'/records/{i}', 'proposal_pointer': f'/records/{i}'}
             for i in range(1,13)],
    canonical_records=12, canonical_Chinese_groups=84,
    original_P02_records=12, original_P02_groups=84,
    denominator_qualification='Separate populations of the same twelve identities; not 24 independent records, not 168 PASS votes, not a 37/31 global signature.',
    input_manifest_identity=ident((T.parent.parent/'continuation-v2/A.complete.json').read_bytes()),
    fixed_B8=contract['fixed_B8'], fixed_R=contract['fixed_R'],
    reused_recovery='recovery.json / extra-recovery.json; no repeated old remote publication audit'))

save(T / 'reading-ledger.json', dict(common,
    all_current_fields=contract['semantic_objects'][0]['all_current_fields_required'],
    exact_current_receipts=state['acks'],
    source_and_B8_displays='source-displays.json (identities, line ranges, UTC and display digest)',
    source_file_counts={r:len({d['path'] for d in displays if d['repo']==r}) for r in ('R','B')},
    display_count=len(displays),
    actual_judgment='judgments.json and reception-ledger.json: per-record complete meaning, parameters, ordinary/cancel/failure paths, complete examples, strongest counter and source/consumer/current-clause join',
    typing='@ and # atoms are full typed identities/locators retained in view-state metadata; = references point to exact already read values with full SHA in pool. No business text is replaced by a summary.',
    dedup_qualification='Acknowledge only after all parts were displayed and read. p6tail is an alias only, not new reading credit; p6 part2 was subsequently directly re-read in full.',
    helper_and_restore_credit=0, automated_line_coverage_credit=0,
    shared_parent_reception={'commit':'1b46a33526f086241c765b700155c5406a86f65e',
      'purpose':'Read parent complete report/independence/helper and reuse completed public responsibility; do not re-sign the parent reserved objects.'},
    whole_original_byte_scope_claimed=False,
    old_status_handling='Current canonical record includes historical FINAL_REVIEW_RECORD_ACCEPTED_UPDATE_NOT_STARTED, REQUIRED_OPEN_FOR_MANUAL_UPDATE, old PENDING_ROOT_ACCEPTANCE, root accepted clarifiers and original nulls. Preserve their original time/layer; B8 closed state is separate, never overwrite the original fields.',
    no_sampling=True, own_unread=[]))

save(T / 'unread.json', dict(common, A_available_unread=[], A_required_unresolved=[],
    A_remaining_count=0,
    external_separate_work=['Parent receipt of this exact published A result and registration',
      'B/C/D partition reviews and the parent global denominator/dedup/task-final signature; A makes no statement that they are complete',
      'Main reviewer final integration/decision; no main merge or formal change performed'],
    retained_limits=['REFERENCE_OBSERVATION=NOT_EXECUTED', 'INDEPENDENT_COMPLETE_MODEL=NOT_EXECUTED',
      'HOST/DEMO/MEDIA/REAL_SAVE_REPLAY=NOT_EXECUTED', 'model/effort/tier/speed/Fast=UNVERIFIED',
      'L01–L14 and old56/92 are not closed by A'],
    purpose_qualification='Availability is not a host limit. No A source/consumer/clause left unread is hidden in retained runtime limits. Outside-A semantic populations remain outside this signature.'))

save(T / 'transport-disposition.json', dict(common,
    all45=[{'relative_to_target_task':f['relative_to_target_task'],
             'mode':f['mode'], 'git_blob':f['git_blob'], 'sha256':f['sha256'], 'bytes':f['bytes'],
             'purpose':'Exact frozen transport available; identity only here. A substantive scope is precisely manifest semantic_objects/original purpose indices; parent shared artifacts remain its separate responsibility.'}
            for f in contract['files']],
    original_purpose_indices=contract['original_purpose_indices'],
    restored_originals='25 identities checked in recovery.json; indices0/1/15/16/18 records1..12 plus exact binding members are substantive A reads.',
    no_unread_business_hidden_by_typing=True,
    ignored_local_cache='.work/: own isolation only; not input from author cache, not published',
    remote_publication_validation='Only own new increment is to be fetched into a separate no-alternates bare cache and fully compared. Old input identities reused.'))

save(T / 'operation-notes.json', dict(common,
    issues=[
      {'issue':'Some initial aggregate contract/manifest outputs truncated', 'resolution':'Fully re-read in bounded chunks before canonical reception; no aggregate output alone credited.'},
      {'issue':'p6 aggregate output truncated 159 tokens near acceptance tail', 'resolution':'p6tail dedup did not recover missing text; actual views/p6.2.txt then directly displayed in full. p6tail grants zero additional credit.'},
      {'issue':'norm2 requested nonexistent part1', 'resolution':'IndexError retained; its sole part0 was fully read. No missing body is claimed.'},
      {'issue':'WP41/WP42 initial aggregate truncated', 'resolution':'WP41 180–220 and WP42 42–60/100–144 subsequently read without truncation; required joining clauses fully present.'},
      {'issue':'Later seven-file B8 batch truncated inside FP83–88', 'resolution':'FP81–89 separately fully displayed at 12:06:52 UTC; no remaining semantic loss.'},
      {'issue':'Redundant metadata debug outputs truncated; one acks.items call failed; wrong-repo B8 grep and guessed Interpreter path failed', 'resolution':'All were discovery/debug only. Exact previously read objects remain bound by views; correct source paths/current B8 were subsequently explicitly displayed. No extra reading credit.'}
    ],
    helper_policy='recover.py/view.py/source.py/extras.py/assemble.py are own understood inert tools. No old recovered script, Ruby, game, model, GUI or business behavior executed.',
    initial_fetch='Own recovery bare uses read-only workspace object alternates, exact HTTPS ordinary fetch; publication readback will use a different bare with no alternates.',
    claim_limit='Tool displays/JSON parsing/hashes and publication equality are corroboration, not semantic judgments or executed behavior. Platform actual displays are session evidence; private platform logs are not asserted public artifacts.'))

lines = ['# 第八轮 H-C2 剩余接收 A 组', '',
         '状态：**READY_FOR_PARENT_RECEPTION（仅A）**。12/12完整记录、84/84当前中文组、12份完整原提案/独立裁决及12份原P02七组均接收；两套七组保持不同总体，不合并票数。没有新增必改提案，八条旧required在B8的缩窄修订已覆盖，四条optional未选择。', '',
         '固定合同 `64cfde5aa3f6b25adc7291b2c2e880d87baf1ebd`；目标报告 `967b90fac83a6b0c3313087d8871312b4eac18b9`，只读该冻结对象。B8与R的完整身份见 [frozen-denominator.json](frozen-denominator.json)。本分支从父后继 `1b46a33526f086241c765b700155c5406a86f65e` 开始，不重复父保留对象。', '',
         '实际接收context为 `01a1448b-68af-70ff-b817-bacab22f0014`，不同于目标原作者与父接收者；未spawn。模型、effort、tier、speed、Fast均UNVERIFIED。所有行为、宿主、独立完整模型、媒体、Demo、真实保存/回放均NOT_EXECUTED。', '',
         '| 记录 | 原分类 | 本次结论 |', '| --- | --- | --- |']
for n, r in zip(notes, raw[1:13]):
    lines.append(f"| {r['id']} | {r['classification']}/{r['severity']} | {n['resolution']} |")
lines += ['', '每条完整意义、默认/枚举与前提、正常/取消/失败及部分提交、具体对照、当前条款接合与历史限定见 [reception-ledger.json](reception-ledger.json)。实际反证与无必改理由见 [proposal-counters.json](proposal-counters.json)，生产者/调用者/消费者关系见 [interfaces.json](interfaces.json)。', '',
          '接收依据为逐对象实际显示与独立静态推导。原始字段的全文值通过 `views/`、`view-state.json` 的精确已读引用及 `recovery.json`/绑定文件回溯；当前源码和B8条款的固定身份、实际行段及显示摘要在 [source-displays.json](source-displays.json)。必要方法读至完整结束，再核对调用者和消费者；机械范围覆盖与摘要生成均不给阅读信用。旧作者的整文件byte readset是保留的历史字段，不冒充本接收者对整份无关正文的阅读。', '',
          '原FINAL_REVIEW_RECORD_ACCEPTED_UPDATE_NOT_STARTED、PENDING/WAIT、失败、原null、后继clarifier与同值别名均按时间和权限层次保留。B8当前有限闭合与原提案状态分开；M06-001仍是GR3残留关系，M06-002不补造历史ID，GR6-O-002图形链及M09的不同AI根不被改写。原旧27、56/92、全局37/31和其它分区不获本签署。', '',
          '**真实剩余**：A可得未读与自身必需未决均为0。父仍须接收本精确发布、登记A范围并整合其它分组和全局最终签字；本报告不判断B/C/D是否完成，不授根ACCEPTED/CLOSED，不修改正式规格、不整改、不合main。详见 [unread.json](unread.json)。', '',
          '发布只覆盖此目录的新增报告证据。提交及无alternates远端完整回读结果见 `publication.json`（如存在）；该文件之后的收据提交另由最终工具回读与答复绑定，避免自指哈希。输出截断、补读及发现性命令失败均在 [operation-notes.json](operation-notes.json)明确保留。', '']
(T / 'report.md').write_text('\n'.join(lines))
print('Assembled 12 individualized receptions; behavior NOT_EXECUTED; publication not yet asserted.')
