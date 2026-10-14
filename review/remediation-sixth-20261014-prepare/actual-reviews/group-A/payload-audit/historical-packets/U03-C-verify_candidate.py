#!/usr/bin/env python3
"""Finite identity, document, preservation and arithmetic checks; never load R."""
import datetime
import difflib
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

EVIDENCE = Path(__file__).resolve().parent
BATCH = EVIDENCE.parent
PREPARE = BATCH.parents[1]
REPO = PREPARE.parents[1]
PREPARE_COMMIT = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
R_GIT = '/tmp/r6-u03-reference.git'
BRANCH = 'codex/remediation-sixth-r6-u03-author-20261014'
checks = []


def check(name, condition, detail=None):
    checks.append({'check': name, 'result': 'PASS' if condition else 'FAIL',
                   'detail': detail, 'evidence_level': 'TOOL_VALIDATION'})
    if not condition:
        raise AssertionError(name)


def git(*args, reference=False):
    prefix = ['git', '--git-dir=' + R_GIT] if reference else ['git']
    return subprocess.check_output(prefix + list(args), cwd=REPO)


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


def json_read(path):
    return json.loads(path.read_text())


def verify():
    contract = json_read(PREPARE / 'contracts/R6-U03.json')
    frozen = json_read(PREPARE / 'inputs/frozen-inputs.json')
    prompt = (PREPARE / 'prompts/R6-U03-A.md').read_bytes()
    check('prompt_fixed_identity', identity(prompt) == {
        'bytes': 153401,
        'sha256': 'a992f8056df8b131e531a7a948c0224358fd1f806ec9e91937c7c1f5d1d23f1e',
        'git_blob': 'b8718da9428a88c3a1c9a02970199cce94a148ce'})
    embedded = json.loads(prompt.decode().split('```json\n', 1)[1].split('\n```', 1)[0])
    check('complete_embedded_contract_equals_canonical', embedded == contract)
    check('two_canonical_required_ids', contract['required_ids'] == ['GR6-O-001', 'GR6-O-002'])
    check('fixed_formal_tree', git('rev-parse', MAIN + ':deliverables/final-specification-set').decode().strip()
          == '1046fbb657882e84b3dfc6d017943a9edf7782e5')
    check('fixed_reference_tree', git('rev-parse', R + '^{tree}', reference=True).decode().strip()
          == '7589c800b61ba13a13040ed0d686979b80a84fd0')
    check('author_branch', git('branch', '--show-current').decode().strip() == BRANCH)
    check('author_base', git('merge-base', 'HEAD', PREPARE_COMMIT).decode().strip() == PREPARE_COMMIT)

    allow_files = {str((BATCH / 'mirror' / p).relative_to(REPO)) for p in contract['candidate_formal_paths']}
    evidence_prefix = str(EVIDENCE.relative_to(REPO)) + '/'
    changes = set(git('diff', '--name-only', PREPARE_COMMIT).decode().splitlines())
    changes.update(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    check('write_allowlist', all(p in allow_files or p.startswith(evidence_prefix) for p in changes), sorted(changes))
    check('formal_protected', not git('diff', '--name-only', MAIN, '--', 'deliverables'))
    check('whitespace', subprocess.run(['git', 'diff', '--check'], cwd=REPO, capture_output=True).returncode == 0)

    identities = []
    opcodes = {}
    base_bytes = {}
    new_bytes = {}
    for path in contract['candidate_formal_paths']:
        old = git('cat-file', 'blob', MAIN + ':' + path)
        original_mirror = git('cat-file', 'blob', PREPARE_COMMIT + ':' + str((BATCH / 'mirror' / path).relative_to(REPO)))
        frozen_row = next(x for x in frozen['formal_materials'] if x['path'] == path)
        check('baseline_identity:' + path, identity(old) == {k: frozen_row[k] for k in identity(old)})
        check('mirror_was_baseline_only:' + path, original_mirror == old)
        new = (BATCH / 'mirror' / path).read_bytes()
        base_bytes[path], new_bytes[path] = old, new
        new.decode('utf-8')
        check('utf8_lf:' + path, new.endswith(b'\n') and b'\r' not in new and b'\0' not in new)
        old_lines = old.splitlines(keepends=True)
        new_lines = new.splitlines(keepends=True)
        ops = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False).get_opcodes()
        opcodes[path] = ops
        identities.append({'formal_path': path, 'candidate_path': str((BATCH / 'mirror' / path).relative_to(REPO)),
                           'baseline': identity(old), 'candidate': identity(new), 'mode': '100644', 'type': 'blob',
                           'changed_ranges': [{'operation': tag, 'old_lines': [a+1, b], 'new_lines': [c+1, d]}
                                              for tag, a, b, c, d in ops if tag != 'equal']})

    source_rows = []
    for path in contract['read_only_reference_paths']:
        source = git('cat-file', 'blob', R + ':' + path, reference=True)
        row = next(x for x in frozen['source_materials'] if x['path'] == path)
        check('reference_payload:' + path, identity(source) == {k: row[k] for k in identity(source)})
        mode_type = git('ls-tree', R, '--', path, reference=True).decode().split()[0:2]
        check('reference_mode_type:' + path, mode_type == ['100644', 'blob'])
        source_rows.append({'path': path, 'commit': R, 'mode': '100644', 'type': 'blob', **identity(source)})

    # Preserve every preexisting line except the explicit two rules, their navigation,
    # and FS05/FS11. Insertions do not authorize replacement of surrounding content.
    authorized_prefixes = {
        'wp13-map-events-npc-followers.md': ('| 冻结防护 |', '静态推导场景（未运行）'),
        'wp60-fishing.md': ('   3. **咬钩检定**', '- **随机输入目录**', '静态推导场景（未运行）'),
        'engine-overworld-wp11-15-59-60.md': ('| FS05 |', '| FS11 |'),
    }
    for path, old in base_bytes.items():
        changed_original = []
        for tag, a, b, c, d in opcodes[path]:
            if tag in ('replace', 'delete'):
                changed_original.extend(old.decode().splitlines()[a:b])
        check('all_other_original_lines_preserved:' + path,
              all(line.startswith(authorized_prefixes[Path(path).name]) for line in changed_original), changed_original)

    catalog = next(p for p in base_bytes if '/test-catalog/' in p)
    for path, new in new_bytes.items():
        added = []
        for tag, a, b, c, d in opcodes[path]:
            if tag in ('replace', 'insert'):
                added.extend(new.decode().splitlines()[c:d])
        check('no_reference_code_in_new_formal:' + path,
              not any(re.match(r'\s*(def |class |module |require |load |@\w+\s*=)', line) for line in added))
    new_ids = re.findall(r'^\| (R6-(?:FS|EV)\d+) \|', new_bytes[catalog].decode(), re.M)
    expected = ['R6-FS%02d' % i for i in range(1, 12)] + ['R6-EV%02d' % i for i in range(1, 7)]
    check('17_unique_static_vectors', new_ids == expected and len(new_ids) == len(set(new_ids)))

    # Fixed integer arithmetic only, not an interpreter or game model.
    freeze = []
    for n, expected_requests, expected_order in [(98, [], None), (99, [101], 'after_terminal'), (100, [101], 'before_terminal')]:
        terminal = n + 1
        empty_check = n + 2
        requests = list(range(101, empty_check + 1, 101))
        order = ('before_terminal' if requests[0] <= terminal else 'after_terminal') if requests else None
        check('DERIVED_VECTOR_freeze_' + str(n), requests == expected_requests and order == expected_order,
              {'comments': n, 'terminal_cycle': terminal, 'empty_list_check_cycle': empty_check,
               'graphics_request_cycles': requests, 'order': order})
        freeze.append(checks[-1]['detail'])
    probabilities = []
    for rod, normal_count, speed_count in [(1, 45, 68), (2, 70, 100), (3, 95, 100)]:
        normal = 20 + 25 * rod
        speed = Fraction(normal) * Fraction(3, 2)
        counts = [sum(value < threshold for value in range(100)) for threshold in (normal, speed)]
        check('DERIVED_VECTOR_unchanged_probability_rod' + str(rod), counts == [normal_count, speed_count],
              {'rod': rod, 'thresholds': [str(normal), str(speed)], 'accepted_integer_results': counts})
        probabilities.append(checks[-1]['detail'])

    regression_input = json_read(EVIDENCE / 'historical-regression-input.json')
    spans = []
    for row in regression_input['relevant_file_spans']:
        consumer = row['consumer']
        path = consumer['path']
        start, end = consumer['lines']
        old_lines = base_bytes[path].splitlines(keepends=True)
        old_span = b''.join(old_lines[start-1:end])
        check('historical_baseline_span:' + row['id'] + ':' + path + ':' + str(start),
              hashlib.sha256(old_span).hexdigest() == consumer['span_sha256'])
        mapped_lines = []
        for tag, a, b, c, d in opcodes[path]:
            if tag == 'equal':
                for old_line in range(max(a, start-1), min(b, end)):
                    mapped_lines.append(c + old_line - a + 1)
        check('historical_candidate_original_lines_unchanged:' + row['id'] + ':' + path + ':' + str(start),
              len(mapped_lines) == end-start+1)
        current_lines = new_bytes[path].splitlines(keepends=True)
        projection = b''.join(current_lines[i-1] for i in mapped_lines)
        check('historical_ordered_line_projection:' + row['id'] + ':' + path + ':' + str(start), projection == old_span)
        contiguous = mapped_lines[-1] - mapped_lines[0] + 1 == len(mapped_lines)
        spans.append({'id': row['id'], 'path': path, 'old_lines': [start, end],
                      'current_original_line_positions': mapped_lines,
                      'span_sha256': consumer['span_sha256'],
                      'result': 'IDENTICAL_SPAN' if contiguous else 'PRESERVED_ORIGINAL_LINES_WITH_NEW_RULE_INSERTION',
                      'new_containing_span_sha256': hashlib.sha256(b''.join(current_lines[mapped_lines[0]-1:mapped_lines[-1]])).hexdigest(),
                      'claim': 'qualification/preservation only, not a renewed historical whole-domain PASS'})

    check('historical_R5_selected_scope', regression_input['actual_activation_selection'][0]['id'] == 'GR5-M03-007'
          and regression_input['selected_candidate_record']['frozen_required_scope'] ==
          regression_input['immediate_interpreter_fishing_qualification']['frozen_scope'])
    return {'candidate_identities': identities, 'reference_identities': source_rows,
            'historical_spans': spans, 'derived_freeze_arithmetic': freeze,
            'derived_probability_arithmetic': probabilities,
            'new_reference_execution': 0, 'independent_full_gameplay_model_execution': 0,
            'host_or_demo_execution': 0, 'independent_review': 'PENDING_NON_AUTHOR_ULTRA'}


def main():
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {'start_utc': start, 'cwd': str(REPO), 'argv': sys.argv,
              'runtime': sys.version, 'evidence_level': 'TOOL_VALIDATION + finite DERIVED_VECTOR arithmetic'}
    try:
        result.update(verify())
        result['result'] = 'AUTHOR_STATIC_CHECKS_PASS'
        code = 0
    except Exception as error:
        result.update({'result': 'FAIL', 'error': str(error)})
        code = 1
    result.update({'checks': checks, 'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   'exit_code': code})
    (EVIDENCE / 'static-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'result': result['result'], 'checks': len(checks), 'error': result.get('error'),
                      'reference_execution': 0, 'host_execution': 0}, ensure_ascii=False))
    return code


if __name__ == '__main__':
    sys.exit(main())
