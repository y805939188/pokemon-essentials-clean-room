"""Read existing audit artifacts only; never execute reference code or probes."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import sys

START = datetime.datetime.now(datetime.timezone.utc).isoformat()
REPO = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
BASE = REPO / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'
OUT = BASE / 'tasks/R6-O/execution-boundary-counter'
OUT.mkdir(exist_ok=True)

def read(rel):
    return json.loads((BASE / rel).read_text())

def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def selected_commands(task, names):
    result = []
    path = BASE / 'tasks' / task / 'stdout.jsonl'
    for line, text in enumerate(path.read_text().splitlines(), 1):
        record = json.loads(text)
        item = record.get('item', {})
        command = item.get('command', '')
        if record.get('type') == 'item.completed' and item.get('type') == 'command_execution' and 'ruby ' in command and any(name in command for name in names):
            result.append({'artifact': str(path.relative_to(BASE)), 'line': line, 'item_id': item.get('id'), 'command': command,
                           'exit_code': item.get('exit_code'), 'captured_output': item.get('aggregated_output'),
                           'start_utc': 'NOT_CAPTURED_IN_THIS_COMMAND_RECORD', 'end_utc': 'NOT_CAPTURED_IN_THIS_COMMAND_RECORD'})
    return result

ca = read('tasks/R6-CA/sparse-reference-result.json')
ca_commands = selected_commands('R6-CA', ['sparse-reference-probe.rb'])
f_commands = selected_commands('R6-F', ['isolated_facility_checks.rb', 'isolated_record_terrain.rb', 'isolated_entry_rejection_counter.rb'])
ui_commands = selected_commands('R6-UI', ['purify-first-refresh.rb', 'capture-message-order.rb'])
ca_errors = [i for i, row in enumerate(ca['rows'], 1) if row['errors']]
assert len(ca['rows']) == 24 and len(ca_errors) == 9
assert len(ca_commands) == 1 and ca_commands[0]['exit_code'] == 0
assert collections.Counter(x['exit_code'] for x in f_commands) == {0: 4, 1: 1}
assert collections.Counter(x['exit_code'] for x in ui_commands) == {0: 3, 1: 1}
f_cases = {name: len(read('tasks/R6-F/' + name)['results']) for name in ['isolated-facility-checks.json', 'isolated-record-terrain.json', 'isolated-entry-rejection-counter.json']}
assert list(f_cases.values()) == [5, 2, 3]
k_findings = read('tasks/R6-K/findings.json')
k_validations = [{'id': x['id'], 'validation': x['validation']} for x in k_findings if x['id'] in ['GR6-K-001', 'GR6-K-002']]
assert len(k_validations) == 2
o_fishing = read('tasks/R6-O/execution-log.json')
o_owner = read('tasks/R6-O/counter-K-002.json')['execution']
o_phone = read('tasks/R6-O/phone-existing-contract-results.json')
phone_output = json.loads(o_phone['stdout'])
assert phone_output['vector_count'] == 10 and len(phone_output['results']) == 10
assert o_owner['vectors'] == 5 and o_owner['exit'] == 0 and o_phone['exit'] == 0
assert [x['exit'] for x in o_fishing['processes']] == [1, 1, 0]
ui_bag = read('tasks/R6-UI/bag/toss-order-probe.execution.json')
assert ui_bag['ruby_exit_code'] == 0
incident = read('control/write-boundary-incident.json')
assert incident['id'] == 'INC-R6-001' and incident['strict_write_boundary_compliant'] is False

families = [
 {'id': 'R6-O', 'evidence': 'ISOLATED_REFERENCE_EXECUTION / REFERENCE_OBSERVATION_WITH_SURROGATES',
  'ruby_process_attempts': 5, 'known_exit_zero': 3, 'known_exit_nonzero': 2, 'ruby_exit_unknown': 0,
  'failed_before_reference_load': 1, 'failed_after_partial_reference_coordinator': 1,
  'retained_completed_case_rows': 22, 'case_split': {'Fishing': 7, 'Owner': 5, 'Phone': 10},
  'invalid_or_incomplete_attempts': 'Wrong initial path caused LoadError before reference load; missing ProbePlayer.x stopped second attempt at Fishing:49. Both retained. Expected caught vector exceptions are not failed processes.',
  'time_capture': 'Fishing attempts UTC unavailable; Owner and Phone actual UTC/argv/stdout/stderr/exit captured.',
  'boundary': 'Selected actual coordinator/definitions/conversion callback. Input, messages, animation, map/player and registration providers are explicit surrogates; no whole conversion chain, game, host or real save.'},
 {'id': 'R6-K', 'evidence': 'ISOLATED_REFERENCE_EXECUTION / REFERENCE_OBSERVATION_WITH_SURROGATES',
  'ruby_process_attempts': 2, 'known_exit_zero': 0, 'known_exit_nonzero': 0, 'ruby_exit_unknown': 2,
  'shell_pipeline_exit_zero': 2, 'retained_completed_case_rows': 7,
  'case_split': {'selected_bag_conversion_callbacks': 2, 'Owner_constructor_and_setter': 5},
  'metadata_limit': 'tee pipeline exit0 is not independently captured Ruby exit. Actual UTC and exact patch were not captured; administrative update UTC is not run time. Outputs labelled TOOL_VALIDATION still execute original callbacks/definitions.',
  'boundary': 'Loaded original inspected definitions and target callback, bare object/collector. No normal migration chain, old save, creature creation or bag UI. O independent Owner run does not retroactively supply K missing metadata.'},
 {'id': 'R6-CA', 'evidence': 'ISOLATED_ACTUAL_REFERENCE_HANDLERS_WITH_STUBS',
  'ruby_process_attempts': 1, 'known_exit_zero': 1, 'known_exit_nonzero': 0, 'ruby_exit_unknown': 0,
  'retained_completed_case_rows': 24, 'caught_handler_exception_case_rows': 9, 'normal_case_rows': 15,
  'exception_row_numbers': ca_errors,
  'boundary': 'Actual two switch handlers directly invoked using SparseArray/rng/debug surrogates. Nine NoMethodError diagnostics are caught by logonerr, not nine failed processes. No full battle initialization, action registration, frequency distribution, UI reporter or host.',
  'time_capture': 'Actual UTC absent from completed command item; adjacent Ruby version check is language/runtime inventory, not an extra reference probe.'},
 {'id': 'R6-F', 'evidence': 'ISOLATED_ACTUAL_REFERENCE_WITH_MEMORY_ONLY_STUBS',
  'harness_types': 3, 'ruby_process_attempts': 5, 'known_exit_zero': 4, 'known_exit_nonzero': 1, 'ruby_exit_unknown': 0,
  'retained_completed_case_rows': 10, 'retained_case_split': f_cases,
  'repeated_entry_counter_processes': 1, 'earlier_entry_counter_configured_cases': 3,
  'repeat_output_limit': 'Earlier entry counter exit0 is recorded; its redirected result was overwritten by the later labels-only BULBASAUR/EEVEE rerun. Do not describe 13 independent retained vectors. Current final output has three entry cases.',
  'invalid_fixture_attempt': 'First facility script selected Summary with numeric menu stub1 instead of Entry0, then lacked pbSummary. Corrected command selects actual Entry label; original exit1 retained. Not a source failure finding.',
  'language_only_control': 'Two loop-local iterations (0 then nil) in entry probe are a separate Ruby language control, not two more reference vectors.',
  'boundary': 'Original inspected Challenge/Rulesets/selected full entry method and recorded field/record/restore/setters. Game.save only increments a memory request counter; recorded Marshal packet is harness-created. Base Battle initializer/start and maps/scenes remain stubs. No real save, whole battle or native Summary.',
  'time_capture': 'Actual UTC absent from selected CLI completed records.'},
 {'id': 'R6-UI', 'evidence': 'ISOLATED_ACTUAL_REFERENCE_WITH_SURROGATES',
  'harness_types': 3, 'ruby_process_attempts': 5, 'known_exit_zero': 4, 'known_exit_nonzero': 1, 'ruby_exit_unknown': 0,
  'valid_fixture_exit_zero_processes': 3, 'invalid_fixture_exit_zero_processes': 1,
  'retained_completed_valid_fixture_case_rows': 7, 'valid_case_split': {'Purify_v3': 2, 'capture_store_order': 2, 'bag_toss_order': 3},
  'invalid_fixture_attempts': 'Purifyv1 exit1 and v2 caught NameError/exit0 both lacked inherited Sprite.angle. v3 restores reader default0 and original first refresh completes; suspected source error refuted. v1 ordinary explicit angle case alone does not validate invalid first-refresh fixture.',
  'controlled_interruption_scope': 'Capture MessageInterruption and bag message failure are harness-injected exceptions; they establish reached reference prefixes with those surrogates, not physical user cancel/host failure/recovery.',
  'boundary': 'Actual selected Purify view/flow, capture storage/peer and Bag/PC toss coordinators. Drawing, Sprite, bitmap, messages, species/items, storage/container and scene providers are memory surrogates. No capture battle, native UI, input, pixel result or real save.',
  'time_capture': 'Bag exact UTC/argv/Rubyexit/runtime captured. Purify/Capture actual UTC absent from completed CLI items.'},
 {'id': 'R6-CM', 'evidence': 'INDEPENDENT_RATIONAL_ARITHMETIC_ORACLE + LANGUAGE_ONLY_CAPABILITY_PROBE',
  'reference_process_attempts': 0, 'coordinator_arithmetic_assertions': 19, 'quantitative_arithmetic_assertions': 150,
  'assertion_overlap': '169 is only a sum of assertions, including overlapping catalog cases; not 169 independent battle vectors.',
  'language_probe': 'Generic temporary namespace and empty Array under Ruby2.6.10; existing/absent binding and lack of public instance constructor. No actual reference class, metadata/compiler, game model or host loaded.',
  'boundary': 'Python Fraction fixed math and lexical/catalog artifact parsing only; no reference file evaluation/import/instantiation. No independent full gameplay or combat model.'},
 {'id': 'SF2_PE', 'evidence': 'TOOL_VALIDATION_ONLY', 'reference_process_attempts': 0,
  'two_root_reparse_tool_commands_exit_zero': 2,
  'boundary': 'Standard-library RIFF/SF2/PCM/table reader and PE/CLI/COFF/resource/string/CIL byte decoders. read_bytes/struct/decoded instructions are data access, not EXE/DLL/IL/Ruby loading or execution. No synthesizer, actual audio, GPU, WindowsAPI/CLR behavior or native compatibility selector.',
  'native_limits': 'Exact remaining .text/CFG/dataflow/version-selection/host API and unselected string limits preserved from current R6-B/limits.json; successful parser commands do not close them.'},
]
counts = {'scope': 'Only specifically requested, independently checked execution families; no fabricated global census of all tool commands.',
          'families': families,
          'reviewed_ruby_attempts_sum': 18, 'known_ruby_exit_zero_sum': 12, 'known_ruby_exit_nonzero_sum': 4, 'ruby_exit_unknown_sum': 2,
          'reference_body_entered_attempts': 17, 'reference_not_loaded_attempts': 1,
          'summation_warning': 'Process exit0 includes invalid Purifyv2, repeated F entry execution and expected caught exceptions. Case counts stay per family; shared Owner cases and repeat runs are not unique global vectors.',
          'complete_native_host': 0, 'complete_Demo': 0, 'complete_independent_gameplay_model': 0,
          'real_save': 0, 'network_or_external_service': 0, 'physical_input': 0,
          'model_effort_tier_speed_UUID': 'UNVERIFIED; no actual runtime echo',
          'incident': incident,
          'current_incident_root_paths_absent': {p: not (REPO/p).exists() for p in incident['paths']},
          'counter_action': 'No probes rerun; no reference or formal edited; inspection/data comparison only.'}
assert sum(x.get('ruby_process_attempts',0) for x in families) == 18
assert sum(x.get('known_exit_zero',0) for x in families) == 12
assert sum(x.get('known_exit_nonzero',0) for x in families) == 4
save('counts.json', counts)

provenance = {
 'O': {'Fishing': o_fishing, 'Owner': o_owner, 'Phone': o_phone},
 'K': k_validations,
 'CA_completed_command': ca_commands,
 'F_completed_commands': f_commands,
 'UI_completed_commands': ui_commands, 'UI_Bag_execution': ui_bag,
 'SF2_reparse': read('evidence/commands/20261014T080039760467Z-sf2-reparse.json'),
 'PE_reparse': read('evidence/commands/20261014T080040580173Z-pe-cli-reparse.json'),
 'metadata_policy': 'Recovered original fields are retained as-is. Unknown UTC/Rubyexit fields remain unknown, not replaced by filesystem mtime, administrative time or parent shell pipeline status.'}
save('process-evidence.json', provenance)

full_read = [
 'tasks/R6-K/isolated-bag-migration.rb', 'tasks/R6-K/isolated-owner-validation.rb',
 'tasks/R6-CA/sparse-reference-probe.rb', 'tasks/R6-F/tools/isolated_facility_checks.rb',
 'tasks/R6-F/tools/isolated_record_terrain.rb', 'tasks/R6-F/tools/isolated_entry_rejection_counter.rb',
 'tasks/R6-UI/purify-first-refresh.rb', 'tasks/R6-UI/capture-message-order.rb', 'tasks/R6-UI/bag/toss-order-probe.rb',
 'tasks/R6-CM/tools/wp43_numeric.py', 'tasks/R6-CM/quantitative/check_vectors.py',
 'evidence/resource-parser/audit_resources.py', 'evidence/resource-parser/audit_binaries.py',
 'tasks/R6-B/controller-meta/verify_pe.py', 'tasks/R6-UI/tool-evidence-status.json',
 'tasks/R6-F/validation-notes.md', 'tasks/R6-CM/tool-review.json', 'tasks/R6-B/limits.json',
 'control/write-boundary-incident.json', 'tasks/R6-UI/party/independent-vectors.json']
artifact_checked = [
 'tasks/R6-O/execution-log.json', 'tasks/R6-O/counter-K-002.json', 'tasks/R6-O/phone-existing-contract-results.json',
 'tasks/R6-K/findings.json', 'tasks/R6-K/logs/bag-migration-validation.json', 'tasks/R6-K/logs/owner-validation.json',
 'tasks/R6-CA/sparse-reference-result.json', 'tasks/R6-CA/stdout.jsonl', 'tasks/R6-F/stdout.jsonl',
 'tasks/R6-F/isolated-facility-checks.json', 'tasks/R6-F/isolated-record-terrain.json', 'tasks/R6-F/isolated-entry-rejection-counter.json',
 'tasks/R6-UI/stdout.jsonl', 'tasks/R6-UI/bag/toss-order-probe.execution.json', 'tasks/R6-UI/bag/toss-order-probe.stdout.json',
 'tasks/R6-CM/wp43-numeric-results.json', 'tasks/R6-CM/quantitative/constant-arithmetic-checks.json',
 'tasks/R6-CM/call-control/counter-R6-CM-FB-01.json', 'tasks/R6-UI/report.md', 'tasks/R6-UI/party/report.md',
 'evidence/commands/20261014T080039760467Z-sf2-reparse.json', 'evidence/commands/20261014T080040580173Z-pe-cli-reparse.json']
bindings = []
for name in full_read + artifact_checked:
    raw = (BASE/name).read_bytes()
    bindings.append({'path': name, 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
                     'lines': len(raw.splitlines()), 'read_basis': 'NEW_FULL_TOOL_BODY_OR_LIMIT_CONTENT_READ' if name in full_read else 'NEW_TARGET_RECORD_INSPECTION_NOT_FULL_PEER_SOURCE_REVIEW',
                     'semantic_use': 'Execution classification/provenance only; does not count as own domain source/formal semantic coverage.'})
save('artifact-bindings.json', bindings)
(OUT/'reading-ledger.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in bindings))

report = '''# R6-O 本轮执行与限制独立反证

已独立核对要求的探针脚本、原始完成命令、结果及限制记录，没有重跑探针。下列进程数、当前保留向量、被捕获异常和工具断言分别计量；这份反证不裁正式提案、不修formal，也不把源请求视作宿主结果。

| 记录 | 实际进程与结果 | 证据边界 |
| --- | --- | --- |
| O | 5次Ruby：3个exit0、2个exit1；当前22向量＝Fishing7＋Owner5＋Phone10 | 第一次错误路径未加载R；第二次原Fishing部分执行后缺x替身停止。成功三次执行原定义／协调器。预期异常向量不增加失败进程。FishingUTC未捕获；Owner／Phone具实际UTC。 |
| K | 2次原Ruby；2个tee管道exit0，Ruby独立exit与实际UTC未知；2bag回调＋5Owner向量 | 日志“TOOL_VALIDATION”不是正确源执行分类；原定义和回调确已调用，应记隔离源执行／替身观察。没有普通完整迁移、真实save或UI；更新时间不补运行时间。 |
| CA | 1次原handler进程exit0；24行含9个诊断捕获NoMethodError、15个无异常 | 9不是失败进程；稀疏数组／随机／诊断替身，不是完整战斗或频率验证。 |
| F | 3种脚本，实际5次Ruby：4个exit0、1个exit1；当前结果10例＝5＋2＋3 | 首次坏menu替身误入Summary；修正后成功。entry脚本又做一次换物种标签的成功重跑，旧输出被覆盖；不能声称只有3进程或13个独立保留向量。Game.save计数只是内存请求；录制包由夹具自造。 |
| UI | 5次Ruby：4个exit0、1个exit1；有效夹具3成功进程，当前7例＝Purify2＋Capture2＋Bag3 | Purifyv1/v2缺Sprite.angle；v2捕获错误exit0仍是无效夹具。v3补继承reader后首刷新成功，原怀疑撤销。Capture／Bag故障为注入消息异常，不是物理用户取消。 |
| CM | 19与150个算术断言，另generic Ruby Array／名字查询语言探针；源执行0 | 算术案例有重叠；不是169个独立战斗向量或完整模型。语言探针未加载R，不能证实真实工厂／compiler／host运行。 |
| SF2／PE | 两条具UTC的root重解析工具命令exit0；源执行0 | 读取PCM／RIFF／PE／CIL字节、解析外部MemberRef或完整IL不加载synth、EXE、DLL、IL；没有真实声音／GPU／WindowsAPI／CLR结果。 |

所核Ruby尝试合计18：已知exit0为12、exit1为4、独立Rubyexit未知为2；其中1次未加载R，其余17次进入原定义／协调器。合计仅是上述指定家族，不能当作全队所有工具调用普查，也不能把exit0等同于语义PASS。向量保留各家族原分母，共享Owner案例／F重跑／无效Purify版本没有合并为全局唯一向量。

本轮记录没有完整原宿主、Demo、独立完整玩法模型、真实save、网络／外部服务或物理Input执行，均0。Sprite／Bitmap／音频资源请求、保存请求、时钟／抽样和动画调用只证明源侧发起或替身记录；实际可见／可听／持久化结果仍未知。model／effort／tier／speed／UUID无实际回显，均UNVERIFIED。R6-B剩余native CFG/dataflow、runtime／兼容选择、GPU精度／拼接／采样、WindowsAPI／CLR及未选字符串候选limits保留；字节工具成功不消除限制。算术oracle确执行，但完整游戏或战斗模型未执行。

**INC-R6-001须保留真实流程违规。** UI Party最初汇总命令遗漏cwd，在仓库根创建`build_review.py`和`forward-matrix.jsonl`两个新untracked文件，随后移入自己的任务目录。现根路径不存在、protected tracked无差异与R clean只能说明当前状态及保护检查，不能改写为全队从未越界写入。它是过程事件，不能制造formal缺陷ID。报告时间也不当作创建／移动实际UTC。

`counts.json`为分层计数；`process-evidence.json`保留实际命令／退出／输出字段及缺失元数据；`artifact-bindings.json`与`reading-ledger.jsonl`锁定新读工具体／指定记录。既有错误夹具、失败、被覆盖重跑和修正均保留。只写本独立目录，未运行参考程序、未知脚本或宿主来补证。
'''
(OUT/'report.md').write_text(report)
END = datetime.datetime.now(datetime.timezone.utc).isoformat()
save('task-status.json', {'task':'R6-O-execution-boundary-counter','state':'COMPLETE_BOUNDED_INDEPENDENT_ARTIFACT_COUNTER',
                         'pending':0,'counter_reference_execution':0,'counter_host':0,'counter_real_save':0,'counter_network':0,
                         'runtime':'UNVERIFIED','incident_retained':'INC-R6-001','started_utc':START,'ended_utc':END})
with (OUT/'command-log.jsonl').open('a') as handle:
    handle.write(json.dumps({'argv':[sys.executable,str(Path(__file__).resolve())], 'cwd':str(REPO), 'started_utc':START,'ended_utc':END,
                            'mode':'TOOL_VALIDATION_ONLY existing artifacts parse/hash/classification; no source evaluation',
                            'script_body_reviewed_before_execution':True,'reference_execution':0,'host':0,'stdout_summary':'18 reviewed Ruby attempts:12 known0/4 known1/2 unknown; O22/CA24/F10/UI7 retained cases; incident retained',
                            'process_exit':'Recorded by invoking tool after return, not fabricated inside running script'},ensure_ascii=False)+'\n')
print(json.dumps({'counter_complete':True,'reviewed_ruby_attempts':18,'known_exit_zero':12,'known_exit_nonzero':4,'unknown_Rubyexit':2,'counter_reference_execution':0,'pending':0}))
