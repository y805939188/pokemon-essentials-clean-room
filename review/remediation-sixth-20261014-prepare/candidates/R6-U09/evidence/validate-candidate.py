#!/usr/bin/env python3
"""Bounded text/identity/preservation checks, not reference or host execution."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone

EVIDENCE = Path(__file__).resolve().parent
REPO = EVIDENCE.parents[4]
PREP = EVIDENCE.parents[2]
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
BASE = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CONTRACT = json.loads((PREP / 'contracts/R6-U09.json').read_text())
FROZEN = json.loads((PREP / 'inputs/frozen-inputs.json').read_text())
PREFIX = str(EVIDENCE.parent.relative_to(REPO)) + '/'
checks = []

def check(name, condition, detail=None):
    checks.append({'name': name, 'result': 'OK' if condition else 'FAIL', 'detail': detail})

def git(*argv):
    return subprocess.check_output(['git', *argv], cwd=REPO)

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}

def section(text, start, end=None):
    return text[text.index(start):text.index(end)] if end else text[text.index(start):]

prompt = (PREP / 'prompts/R6-U09-A.md').read_bytes()
check('fixed prompt exact bytes/SHA/blob', identity(prompt) == {
    'bytes': 227242, 'sha256': 'b21be4d214a9d157f0526122981669ea72fe0c39e534aff8376a00f7538b5c0b',
    'git_blob': '500382c78bf7d13b1383f8ba3b7fe8f1997a9abf'})
embedded = json.loads(prompt.decode().split('## 本批确定合同（含原证据、反例、验收、同步和实际路径）')[1].split('```json\n', 1)[1].split('\n```', 1)[0])
check('standalone contract equals fully read embedded contract', embedded == CONTRACT)
check('exact canonical required IDs', CONTRACT['required_ids'] == [f'R6-DX-COMP-00{i}' for i in (1, 2, 3)])
check('fixed main workspace tree', git('rev-parse', MAIN + '^{tree}').decode().strip() == '6ab3429170d2762607fbc2237014c3a160449fa1')
check('fixed main formal tree', git('rev-parse', MAIN + ':deliverables/final-specification-set').decode().strip() == '1046fbb657882e84b3dfc6d017943a9edf7782e5')
check('author branch from fixed preparation', git('merge-base', BASE, 'HEAD').decode().strip() == BASE)
check('unique author branch', git('branch', '--show-current').decode().strip() == 'codex/remediation-sixth-r6-u09-author-20261014')

formal_rows = {r['path']: r for r in FROZEN['formal_materials']}
old, new, outputs = {}, {}, []
mirror_paths = []
for path in CONTRACT['candidate_formal_paths']:
    candidate = EVIDENCE.parent / 'mirror' / path
    rel = str(candidate.relative_to(REPO))
    mirror_paths.append(rel)
    baseline = git('show', MAIN + ':' + path)
    prepared = git('show', BASE + ':' + rel)
    current = candidate.read_bytes()
    expected = formal_rows[path]
    check('fixed formal identity ' + path, all(identity(baseline)[k] == expected[k] for k in identity(baseline)))
    check('preparation was exact baseline, not a repair ' + path, prepared == baseline)
    check('real text change ' + path, current != baseline)
    tree_row = git('ls-tree', MAIN, '--', path).decode().strip().split()
    check('fixed formal mode/type ' + path, tree_row[:2] == ['100644', 'blob'])
    old[path] = baseline.decode()
    new[path] = current.decode()
    outputs.append({'formal_path': path, 'candidate_path': rel, 'mode': '100644', 'type': 'text',
                    'baseline': identity(baseline), 'candidate': identity(current)})

retrieval = json.loads((EVIDENCE / 'input-retrieval.json').read_text())
input_rows = []
for record in retrieval:
    check('retrieval exit ' + record['argv'][-1], record['exit'] == 0)
    row = json.loads(record['stdout'])
    data = Path(row['path']).read_bytes()
    check('retrieved input exact bytes/SHA/blob ' + record['argv'][-1], all(identity(data)[k] == row[k] for k in identity(data)))
    key = 'source_materials' if record['argv'][-2] == 'source' else 'formal_materials'
    frozen = dict(next(r for r in FROZEN[key] if r['path'] == record['argv'][-1]))
    frozen.setdefault('commit', REFERENCE if key == 'source_materials' else MAIN)
    frozen.setdefault('tree', FROZEN['reference_tree'] if key == 'source_materials' else FROZEN['formal_tree'])
    frozen.setdefault('type', 'text')
    input_rows.append({'identity': frozen, 'local_path': row['path'], 'retrieval': record['utc_start']})
for row in json.loads((EVIDENCE / 'additional-readset.json').read_text()):
    data = Path(row['local']).read_bytes()
    check('extra input exact bytes/SHA/blob ' + row['identity']['path'], all(identity(data)[k] == row['identity'][k] for k in identity(data)))
    input_rows.append({'identity': row['identity'], 'local_path': row['local'], 'retrieval': row['utc']})
tree_binding = json.loads((EVIDENCE / 'source-tree-readback.json').read_text())
check('fixed R remote tree binding', tree_binding['tree'] == FROZEN['reference_tree'] and tree_binding['commit'] == REFERENCE)
for row in input_rows:
    if row['identity']['commit'] == REFERENCE:
        entry = next(e for e in tree_binding['selected_entries'] if e['path'] == row['identity']['path'])
        check('remote R path/mode/blob ' + entry['path'], entry['mode'] == row['identity']['mode'] and entry['type'] == 'blob' and entry['sha'] == row['identity']['git_blob'])

wp04 = 'deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md'
wp72 = 'deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md'
wp74 = 'deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md'
wp75 = 'deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md'
wp62 = 'deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md'
gc = 'deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md'
dc = 'deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md'
preservations = [
    (wp04, '### 3.1 ', '### 3.2 ', 'startup discovery/mtime/early boundary'),
    (wp04, '| 异常类别/阶段 |', '## 4. ', 'startup exception table'),
    (wp04, '### 4.1 ', '### 4.2 ', 'PBS discovery'),
    (wp04, '**分词**', '## 5. ', 'tokenization/schema/encounter/validation'),
    (wp04, '### 5.2 ', '### 5.3 ', 'fixed compatibility rewrites'),
    (wp04, '**遭遇概率往返**', '## 6. ', 'encounter/metrics/evolution/phone/hash exports'),
    (wp04, '## 7. ', '## 9. ', 'boundaries/default configuration'),
    (wp04, '## 10. ', None, 'dependencies/unknown'),
    (wp72, '## 1. ', '### 8.3 ', 'debug gates/actions/log/persistence'),
    (wp72, '## 9. ', None, 'debug variants/limits/full effects table'),
    (wp74, '## 1. ', '## 15. ', 'editor/exchange/history/SC-U07 correction'),
    (wp74, '- **命名 → 映射**', '- 编辑器侧可见事实', 'mapping naming/zero-effective gate/playback fallback'),
    (wp74, '## 17. ', None, 'controls/animmaker/limits/dependencies'),
    (wp75, '### 3.2 ', '## 4. ', 'script tooling B20-C024'),
    (wp75, '## 5. ', '## 16. ', 'event conversion/renaming/script roundtrip'),
    (wp62, '## 1. ', '### 5.1 ', 'record ownership/write/identity'),
    (wp62, '### 5.2 ', None, 'unlock/content/display/record refresh'),
]
preserved = []
for path, start, end, label in preservations:
    a, b = section(old[path], start, end), section(new[path], start, end)
    # Insertions at the end of two old sections are compared separately below.
    if path == wp04 and start == '| 异常类别/阶段 |':
        b = b.split('### 3.3 ')[0]
    if path == wp04 and start == '**遭遇概率往返**':
        b = b.split('### 5.6 ')[0]
    ok = a == b
    check('preserved ' + label, ok)
    preserved.append({'path': path, 'start': start, 'end': end, 'label': label, 'identical': ok,
                      'baseline_bytes_sha256': identity(a.encode())['sha256']})
check('existing demo catalog full prefix retained', new[dc].startswith(old[dc]))
old_rows = {line.split('|')[1].strip(): line for line in old[gc].splitlines() if re.match(r'^\| (K[LRB]\d+) \|', line)}
new_rows = {line.split('|')[1].strip(): line for line in new[gc].splitlines() if re.match(r'^\| (K[LRB]\d+) \|', line)}
for identifier, line in old_rows.items():
    if identifier in ('KL02', 'KL03'):
        check('startup-only scope correction, old expected result retained ' + identifier,
              new_rows[identifier].split('|')[3:] == line.split('|')[3:] and '启动检查' in new_rows[identifier])
    else:
        check('old catalog vector unchanged ' + identifier, new_rows.get(identifier) == line)
check('exact new generic vector IDs', set(new_rows) - set(old_rows) == {f'KL{i}' for i in range(37, 51)})
check('new vectors explicitly not executed', all('NOT_EXECUTED' in new_rows[f'KL{i}'] for i in range(37, 51)))
check('exact new demo vector IDs', re.findall(r'^\| (DXCOMP-C\d+) \|', new[dc], re.M) == [f'DXCOMP-C{i:02d}' for i in range(1, 9)])

link_count = 0
for path, text in new.items():
    for match in re.finditer(r'\]\(([^)]+)\)', text):
        target = match.group(1)
        if '://' in target or target.startswith('#'):
            continue
        raw_path, _, fragment = target.partition('#')
        resolved = (REPO / path).parent.joinpath(raw_path).resolve()
        check('local link target ' + path + ' -> ' + target, resolved.is_file())
        link_count += 1
        if fragment and resolved.name == 'wp04-pbs-lifecycle.md':
            check('new WP04 anchor ' + fragment,
                  fragment in ('33-运行中直接全量编译', '56-磁盘产物与同会话缓存'))
tracked = git('diff', '--name-only', BASE).decode().splitlines()
untracked = git('ls-files', '--others', '--exclude-standard').decode().splitlines()
check('write set only own exact mirrors/evidence', all(p in mirror_paths or p.startswith(PREFIX + 'evidence/') for p in tracked + untracked))
check('all and only seven mirrors changed', {p for p in tracked if '/mirror/' in p} == set(mirror_paths))
check('formal baseline still unchanged', git('diff', BASE, '--', 'deliverables') == b'')
diff_check = subprocess.run(['git', 'diff', '--check', BASE], cwd=REPO, capture_output=True, text=True)
check('git diff --check', diff_check.returncode == 0, {'exit': diff_check.returncode, 'stdout': diff_check.stdout, 'stderr': diff_check.stderr})
for p in EVIDENCE.glob('*.json'):
    json.loads(p.read_text())
for line in (EVIDENCE / 'reading-ledger.jsonl').read_text().splitlines():
    json.loads(line)
check('own JSON/JSONL parses', True)

result = {'utc': datetime.now(timezone.utc).isoformat(), 'argv': sys.argv, 'cwd': str(REPO),
          'runtime': sys.version, 'evidence_level': 'TOOL_VALIDATION',
          'scope': 'bounded payload identities, permitted text writes, links, retained historical clauses/vectors; no reference behavior execution',
          'reference_execution': 0, 'independent_behavior_model_execution': 0, 'host_demo_execution': 0,
          'checks': checks, 'checks_total': len(checks), 'failed': sum(c['result'] == 'FAIL' for c in checks),
          'preserved_spans': preserved, 'local_link_targets_checked': link_count}
(EVIDENCE / 'static-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
(EVIDENCE / 'input-manifest.json').write_text(json.dumps({'fixed_prepare': BASE, 'fixed_main': MAIN, 'fixed_reference': REFERENCE,
    'inputs': input_rows, 'prompt': identity(prompt), 'contract': identity((PREP / 'contracts/R6-U09.json').read_bytes())}, ensure_ascii=False, indent=2) + '\n')
(EVIDENCE / 'candidate-files.json').write_text(json.dumps({'binding': 'working tree payloads; core/final commit externally bound',
    'files': outputs, 'write_set': mirror_paths, 'manifest_self_hash': False}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'checks': len(checks), 'failed': result['failed'], 'link_targets': link_count,
                  'failures': [c for c in checks if c['result'] == 'FAIL']}, ensure_ascii=False))
sys.exit(1 if result['failed'] else 0)
