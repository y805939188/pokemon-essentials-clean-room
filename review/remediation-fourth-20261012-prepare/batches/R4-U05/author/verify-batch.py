#!/usr/bin/env python3
"""Read-only identity/scope audit; never executes reference behavior."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
START = '08a57fb55118914a74ac1ffaf617647c01df8938'
RECEIPT = 'a53b11789bdfe0ee6a373e0c705a2c79f5187400'
B = '1f36475d22120a0d1175967d5b17d71fe8311d88'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REPORT = '130452d902530140331c21064a3188b7887f72ae'
PACK = 'review/remediation-fourth-20261012-prepare/'
REPORT_ROOT = 'review/global-independent-review/fourth-2026-10-12-1f36475-c92e/'
EVIDENCE = PACK + 'batches/R4-U05/author/'
FORMAL = [
    'deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md',
    'deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md',
]


def git(*args, repo=ROOT):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def blob(commit, path, repo=ROOT):
    return git('show', commit + ':' + path, repo=repo)


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


def dump(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def verify_expected(commit, path, expected, repo=ROOT):
    actual = identity(blob(commit, path, repo))
    for key in ['bytes', 'sha256', 'git_blob']:
        assert actual[key] == expected[key], (commit, path, key)
    return {'commit': commit, 'path': path, **actual, 'full_bytes_checked': True}


def preflight(reference_repo):
    scope = json.loads((ROOT / (PACK + 'tasks/R4-U05/read-scope.json')).read_bytes())
    frozen = json.loads(blob(RECEIPT, PACK + 'freeze-and-publication.json'))
    assert frozen['author_start_commit'] == START
    assert git('rev-parse', START + '^{tree}').decode().strip() == frozen['author_start_tree']
    assert git('rev-parse', B + '^{tree}').decode().strip() == frozen['formal_input_tree']
    assert git('rev-parse', R + '^{tree}', repo=reference_repo).decode().strip() == frozen['reference_tree']
    assert git('rev-parse', REPORT + '^{tree}').decode().strip() == frozen['fixed_review_publication']['tree']
    assert git('diff', '--name-only', B, START, '--', 'deliverables/final-specification-set') == b''
    assert git('diff', '--name-only', B, REPORT, '--', 'deliverables/final-specification-set') == b''
    packet_records = []
    relevant = {PACK + 'README.md', PACK + 'input-verification.json', PACK + 'resource-scope.json',
                PACK + 'dispatch-plan.json', PACK + 'task-file-identities.json'}
    relevant.update(PACK + 'tasks/R4-U05/' + name for name in [
        'author.md', 'batch-contract.json', 'read-scope.json', 'findings-input.json',
        'handoff-findings.md', 'legacy-navigation.json', 'launch-contract.json'])
    for record in frozen['task_pack_readback']['file_identities']:
        if record['path'] in relevant:
            packet_records.append(verify_expected(START, record['path'], record))
    assert {x['path'] for x in packet_records} == relevant
    prepared = json.loads(blob(START, PACK + 'input-verification.json'))
    external_records = [verify_expected(x['commit'], x['path'], x) for x in prepared['external_bindings']]
    source_records = [verify_expected(R, x['path'], x['identity'], reference_repo) for x in scope['source']]
    formal_before = [verify_expected(B, x['path'], x['identity']) for x in scope['formal_anchors']]
    findings = json.loads(blob(REPORT, REPORT_ROOT + 'findings.json'))['findings']
    selected = next(x for x in findings if x['id'] == 'GR4-M12-001')
    packet_finding = json.loads(blob(START, PACK + 'tasks/R4-U05/findings-input.json'))['canonical_root_records'][0]
    assert selected == packet_finding
    dispatch = json.loads(blob(START, PACK + 'dispatch-plan.json'))
    batches = dispatch['plan']['author_batches']
    all_paths = [p for x in batches for p in x['allowed_formal_write_paths']]
    assert len(all_paths) == len(set(all_paths)) == 28
    assert next(x for x in batches if x['id'] == 'R4-U05')['allowed_formal_write_paths'] == FORMAL
    execution = json.loads(blob(REPORT, REPORT_ROOT + 'execution-evidence.json'))
    assert execution['counts_by_record_not_testcase']['EXECUTED_REFERENCE'] == 4
    assert execution['no_full_host_or_demo_execution'] is True
    legacy = json.loads(blob(REPORT, REPORT_ROOT + 'regression-third-23.json'))
    legacy_records = [{k: v for k, v in x.items() if k in [
        'id', 'title', 'historical_effective_state', 'historical_scope', 'fourth_status', 'limitations']}
        for x in legacy['records'] if x['id'] in ['GR3-M12-001', 'GR3-M12-002']]
    dump('input-check.json', {
        'evidence_level': 'TOOL_VALIDATION', 'identity_checks_verified': True,
        'task_package': {'commit': START, 'tree': frozen['author_start_tree']},
        'publication_receipt': {'commit': RECEIPT, 'tree': git('rev-parse', RECEIPT + '^{tree}').decode().strip(),
                                'path': PACK + 'freeze-and-publication.json',
                                **identity(blob(RECEIPT, PACK + 'freeze-and-publication.json'))},
        'formal_baseline': {'commit': B, 'tree': frozen['formal_input_tree']},
        'reference': {'commit': R, 'tree': frozen['reference_tree'], 'read_only_object_store': str(reference_repo)},
        'report': frozen['fixed_review_publication'],
        'start_and_report_formal_drift_from_B': 'NONE',
        'canonical_GR4_M12_001_matches_fixed_report': True,
        'packet_complete_file_identities': packet_records, 'external_handoff_bindings': external_records,
        'source_complete_file_identities': source_records, 'formal_input_identities': formal_before,
        'all_28_formal_write_paths_disjoint': True,
        'legacy_scope_read': legacy_records,
        'historical_execution': {'fixed_report_EXECUTED_REFERENCE_records': 4,
                                'full_host_or_demo': 'NOT_EXECUTED', 'not_reexecuted_or_recertified': True},
        'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE',
        'author_thread_id': os.environ.get('CODEX_THREAD_ID'),
        'source_thread_id': '01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',
        'model_request': {'model': 'gpt-6.1-sol', 'reasoning_effort': 'xhigh',
                          'service_tier': 'default', 'fast': False, 'actual_echo': 'UNVERIFIED'},
        'independent_review_verdict': None,
    })
    terms = [
        '遭遇集|encounter set|pbEncountersEditor|WE-M11',
        '空槽类型|空类型|空遭遇|empty.{0,20}(encounter|slot)',
        '(遭遇|类型|步数率|触发概率).{0,30}(空|复制|拷贝|过滤)|(空|复制|拷贝|过滤).{0,30}(遭遇|类型|步数率|触发概率)',
    ]
    paths = git('ls-tree', '-r', '--name-only', B, '--', 'deliverables/final-specification-set').decode().splitlines()
    paths = [p for p in paths if p.endswith('.md')]
    assert len(paths) == 131
    hits = []
    for term in terms:
        proc = subprocess.run(['git', '-C', str(ROOT), 'grep', '-n', '-E', term, B,
                               '--', 'deliverables/final-specification-set'], capture_output=True, check=False)
        assert proc.returncode in [0, 1]
        lines = proc.stdout.decode().splitlines()
        locations = []
        for line in lines:
            match = re.match(re.escape(B) + r':([^:]+):(\d+):', line)
            assert match, line
            locations.append({'path': match[1], 'line': int(match[2])})
        hits.append({'term': term, 'hit_count': len(lines), 'locations': locations})
    dump('negative-search.json', {'evidence_level': 'SPEC_STATIC', 'commit': B,
        'root': 'deliverables/final-specification-set', 'markdown_files': 131, 'searches': hits,
        'scope': '仅检索本finding反证及具名消费者，不重启全局语义复审；详见read-ledger.json与self-check.json',
        'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE'})
    current_identities = [{'path': p, **identity((ROOT / p).read_bytes())} for p in FORMAL]
    dump('formal-file-identities.json', {'evidence_level': 'TOOL_VALIDATION',
        'scope': '完整候选正文bytes/SHA256/blob；候选commit由后继发布回执绑定',
        'formal_files': current_identities})
    section = lambda data, start, end: data[data.index(start):data.index(end)]
    before = blob(B, FORMAL[0])
    now = (ROOT / FORMAL[0]).read_bytes()
    protected_sections = [('1–5', b'## 1.', b'## 6.'), ('6.3', b'### 6.3', b'### 6.4'),
                          ('6.5–10', b'### 6.5', b'## 11.'), ('12+', b'## 12.', None)]
    for label, left, right in protected_sections:
        a = section(before, left, right) if right else before[before.index(left):]
        b = section(now, left, right) if right else now[now.index(left):]
        assert a == b, label
    tests_before = blob(B, FORMAL[1]).decode()
    tests_now = (ROOT / FORMAL[1]).read_text()
    old_line = next(x for x in tests_before.splitlines(True) if x.startswith('| WE-M11 |'))
    new_line = next(x for x in tests_now.splitlines(True) if x.startswith('| WE-M11 |'))
    supplemental = tests_now[tests_now.index('### WE-M11 的空类型补充对照'):tests_now.index('## AN：')]
    assert tests_before.replace(old_line, '') == tests_now.replace(new_line, '').replace(supplemental, '')
    for path in HERE.glob('*.json'):
        json.loads(path.read_bytes())
    git('diff', '--check')
    tracked = git('diff', '--name-only', START).decode().splitlines()
    untracked = git('ls-files', '--others', '--exclude-standard').decode().splitlines()
    changed = sorted(set(tracked + untracked))
    assert all(p in FORMAL or p.startswith(EVIDENCE) for p in changed), changed
    assert set(p for p in changed if p.startswith('deliverables/')) == set(FORMAL)
    dump('scope-check.json', {'evidence_level': 'TOOL_VALIDATION', 'comparison_base': START,
        'allowed_formal_paths': FORMAL, 'allowed_evidence_root': EVIDENCE,
        'changed_paths_at_preflight': changed, 'all_changed_paths_allowed': True,
        'protected_WP73B_sections_equal_B': [x[0] for x in protected_sections],
        'test_catalog_other_bytes_equal_B': True, 'git_diff_check_exit': 0,
        'json_parse_checked': True, 'independent_behavior_PASS': False})
    print(json.dumps({'identity_and_scope_checks_verified': True, 'source_files': len(source_records),
                      'formal_files': len(current_identities), 'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE'}))


def remote_check(commit, remote_repo):
    local_tree = git('rev-parse', commit + '^{tree}').decode().strip()
    assert git('rev-parse', commit + '^{tree}', repo=remote_repo).decode().strip() == local_tree
    assert git('cat-file', 'commit', commit) == git('cat-file', 'commit', commit, repo=remote_repo)
    paths = git('diff', '--name-only', START, commit).decode().splitlines()
    assert all(p in FORMAL or p.startswith(EVIDENCE) for p in paths)
    records = []
    for p in paths:
        local = blob(commit, p)
        remote = blob(commit, p, remote_repo)
        assert local == remote, p
        oid = git('rev-parse', commit + ':' + p, repo=remote_repo).decode().strip()
        info = identity(remote)
        assert oid == info['git_blob']
        records.append({'path': p, **info, 'complete_remote_bytes_equal_frozen_local': True})
    result = {'evidence_level': 'TOOL_VALIDATION', 'commit': commit, 'tree': local_tree,
        'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'fresh_remote_object_store': str(remote_repo), 'no_alternates_or_local_objects_copied': True,
        'complete_commit_bytes_equal': True, 'all_changed_paths_allowed': True,
        'files_count': len(records), 'total_bytes': sum(x['bytes'] for x in records),
        'file_identities': records, 'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE',
        'independent_review_verdict': None}
    dump('candidate-remote-readback.json', result)
    print(json.dumps({'full_remote_bytes_verified': True, 'commit': commit, 'tree': local_tree,
                      'changed_files': len(records)}))


if __name__ == '__main__':
    if sys.argv[1] == 'preflight':
        preflight(Path(sys.argv[2]))
    elif sys.argv[1] == 'remote':
        remote_check(sys.argv[2], Path(sys.argv[3]))
    else:
        raise ValueError('Expected preflight or remote')
