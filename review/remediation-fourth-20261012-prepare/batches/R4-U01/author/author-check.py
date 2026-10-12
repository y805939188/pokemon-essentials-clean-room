"""Author document/identity checks only; never execute reference or a behavior model."""
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
PACK = '08a57fb55118914a74ac1ffaf617647c01df8938'
BASE = '1f36475d22120a0d1175967d5b17d71fe8311d88'
PREFIX = 'review/remediation-fourth-20261012-prepare/batches/R4-U01/author/'
TASK = ROOT / 'review/remediation-fourth-20261012-prepare/tasks/R4-U01'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def old(path):
    return git('show', PACK + ':' + path).decode()

def block(text, heading):
    start = text.index(heading)
    next_heading = re.search(r'^#{2,3} ', text[start + len(heading):], re.M)
    end = start + len(heading) + next_heading.start() if next_heading else len(text)
    return text[start:end].strip()

contract = json.loads((TASK / 'batch-contract.json').read_bytes())
formal = contract['allowed_formal_write_paths']
changes = set(git('diff', '--name-only', PACK).decode().splitlines())
changes |= set(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
bad = sorted(p for p in changes if p not in formal and not p.startswith(PREFIX))
assert not bad, bad
assert changes.intersection(formal) == set(formal)
assert git('diff', '--name-only', BASE, PACK, '--', 'deliverables/final-specification-set') == b''
subprocess.run(['git', '-C', str(ROOT), 'diff', '--check', PACK], check=True)

identities = json.loads((OUT / 'formal-file-identities.json').read_bytes())
file_checks = []
for item in identities['files']:
    path = item['candidate_bytes']['path']
    data = (ROOT / path).read_bytes()
    text = data.decode('utf-8')
    assert b'\r' not in data
    assert data.endswith(b'\n')
    current_id = {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                  'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}
    assert current_id == item['candidate_bytes'], path
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            assert (ROOT / path).parent.joinpath(target.split('#')[0]).exists(), (path, target)
    file_checks.append(current_id)

catalog = formal[-1]
rows = lambda text: dict(re.findall(r'^(\| ([A-Z][A-Z0-9-]*\d+) \|.*)$', text, re.M))
before_rows = {key: line for line, key in rows(old(catalog)).items()}
after_text = (ROOT / catalog).read_text()
after_pairs = re.findall(r'^(\| ([A-Z][A-Z0-9-]*\d+) \|.*)$', after_text, re.M)
after_rows = {key: line for line, key in after_pairs}
assert len(after_pairs) == len(after_rows), 'duplicate vector IDs'
assert all(after_rows.get(key) == line for key, line in before_rows.items())
expected = {f'TM{i:02}' for i in range(15, 24)} | {f'IO{i:02}' for i in range(16, 21)} | {f'LZ{i:02}' for i in range(26, 36)}
assert set(after_rows) - set(before_rows) == expected

untouched_sections = {
    formal[0]: ['### 3.1 四类来源对照', '### 3.2 现实时间/帧计时消费者表', '### 3.3 现实时间规则族',
                '### 4.1 通用计步入口', '### 4.2 统计字段清单', '### 5.1 随机入口/消费者族目录',
                '### 5.2 地牢待播种子的清空', '### 5.3 记录/回放'],
    formal[1]: ['### 3.1 遍历与目录操作', '### 3.2 存在性与读写（逐入口的捕获集合、分支与返回形态）',
                '### 3.3 资源路径解析（资源路径候选与扩展名回退）', '### 3.4 写入面（静态入口）',
                '### 4.1 分层行为表', '### 5.1 异常与错误日志', '### 5.2 调试日志与控制台',
                '### 5.3 调用前提（诊断函数能力 ≠ 全模式保证）'],
    formal[2]: ['### 3.1 文本域目录', '### 3.2 存储形态与真实消费者', '## 4. 语言配置与选择',
                '### 5.1 查找链（当前语言 game → 当前语言 core，不再查默认语料）', '### 5.2 空译与异常边界',
                '### 6.1 文本收集（编译流程末段）', '### 6.2 提取（作者导出）', '### 6.2.1 地图导出的稀疏桶边界',
                '### 6.3 编译（作者导入）', '### 6.3.1 运行空译与作者文本表达边界', '### 6.4 写回与失败副作用']}
preserved = []
for path, headings in untouched_sections.items():
    current = (ROOT / path).read_text()
    for heading in headings:
        assert block(old(path), heading) == block(current, heading), (path, heading)
        preserved.append({'path': path, 'section': heading})

mapping = json.loads((OUT / 'acceptance-and-regression.json').read_bytes())
assert [r['finding'] for r in mapping['records']] == contract['finding_ids']
assert not mapping['accepted_or_closed_registered']
criteria_count = 0
for record in mapping['records']:
    for criterion in record['criteria']:
        assert criterion['independent_verdict'] == 'PENDING_PARENT_REVIEWER'
        assert set(criterion['vectors']) <= set(after_rows)
        criteria_count += 1

json_files = sorted(OUT.glob('*.json'))
for path in json_files:
    json.loads(path.read_bytes())
read_evidence = json.loads((OUT / 'input-and-read-evidence.json').read_bytes())
assert read_evidence['new_reference_execution'] == 0
assert read_evidence['new_model_execution'] == 0
assert read_evidence['new_host_or_demo_execution'] == 0
assert read_evidence['historical_fourth_review_reference_execution_records'] == 4
source_materializations = 0
for item in read_evidence['source_read']:
    data = Path('/tmp/r4-u01-source', item['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256']
    source_materializations += 1

assert (OUT / 'formal-diff.patch').read_bytes() == git('diff', '--binary', PACK, '--', *formal)
result = {
    'batch': 'R4-U01', 'status': 'ALL_MECHANICAL_CHECKS_SATISFIED', 'evidence_level': 'TOOL_VALIDATION',
    'observed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'command': ['python', PREFIX + 'author-check.py'], 'author_start_commit': PACK,
    'checked_changed_paths': sorted(changes), 'outside_write_scope': bad,
    'formal_files_full_bytes_verified': file_checks, 'new_vector_count': len(expected),
    'existing_vector_rows_verbatim_retained': len(before_rows), 'preserved_sections': preserved,
    'mapped_acceptance_and_optional_criteria': criteria_count,
    'read_source_materializations_full_hash_match': source_materializations,
    'json_parse_links_utf8_lf_diff_check': 'SATISFIED',
    'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE', 'independent_semantic_verdict': 'PENDING_PARENT_REVIEWER',
    'limitations': 'Only byte identity, allowlist, unchanged old rows/sections, references and JSON structure. No behavior/model/reference execution, statistics, host, networking, persistence, independent review or acceptance signature.'}
(OUT / 'validation-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k in ['status', 'evidence_level', 'new_vector_count', 'existing_vector_rows_verbatim_retained', 'mapped_acceptance_and_optional_criteria', 'independent_semantic_verdict']}, ensure_ascii=False))
