"""Create only the six authorized U12 mirrors from immutable B bytes."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'candidates/R7-U12'
EVID = OUT / 'evidence/author'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
H = 'e58486178e746273fb6fab55df00722807f1dc44'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX = 'review/remediation/20261003-prepare/batches/B21/author-draft-1/'
ERRATA = 'review/remediation-seventh-20261015-prepare/current-navigation-errata.json'

def git(*argv):
    return subprocess.check_output(['git', *argv], cwd=ROOT)

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def main():
    contract = json.loads((EVID / 'frozen-contract.json').read_bytes())
    inputs = {}
    changed = []
    history = []
    plan = json.loads((EVID / 'recovery-plan.json').read_bytes())
    for row in plan['fixed_read_inputs']:
        if row['commit'] == H:
            data = Path('/workspace/r7-context/R7-U12-author', row['local_path']).read_bytes()
            expected = {k: row[k] for k in ('bytes', 'sha256')}
            assert all(identity(data)[k] == v for k, v in expected.items())
            assert identity(data)['git_blob'] == row['git_blob_content_id']
            history.append({'commit': H, 'path': row['path'], **identity(data),
                            'qualification': 'Restored immutable raw-URL bytes match the frozen plan; local historical Git object is not assumed. No semantic approval transfer.'})
    for row in contract['paths']:
        path = row['path']
        if path == ERRATA:
            continue
        data = git('show', B + ':' + path)
        assert data == (Path('/workspace/r7-context/R7-U12-author/inputs/project') / path).read_bytes()
        inputs[path] = identity(data)
        text = data.decode()
        if path.startswith('deliverables/'):
            count = 0
            def replace(match):
                nonlocal count
                target = match.group(1)
                if PREFIX not in target:
                    return match.group(0)
                count += 1
                return '](' + 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + H + '/' + PREFIX + target.rsplit('/', 1)[1] + ')'
            text = re.sub(r'\]\(([^)]+)\)', replace, text)
            assert count == (4 if '/test-catalog/' in path else 3)
            note = ('GR7-M19-001 历史导航勘误：上述 B21 作者候选链接固定到历史提交 `'
                    + H + '` 的 `' + PREFIX + '`，不是当前树中的相对目标。离线检索须先有包含该提交对象的仓库，或具备下述文件身份的历史档案；在仓库中用 `git show '
                    + H + ':' + PREFIX + '<文件名>` 读取相应 `README.md`、`traceability.json`、`eight-chains.json` 或 `static-cases.json`。四文件的 bytes/SHA256/blob 记录于本批候选证据 `candidates/R7-U12/evidence/author/mirror-identities.json`，实际取得后须匹配身份；缺少对象或档案时该检索仍不可用。这里只纠正历史候选的定位，保留历史正文、候选/实际审查及批准状态；不以当前实际审查工件替代候选追溯，也不授予新的语义批准。')
            # Place the note after the original affected paragraph(s), before the historical separator.
            pos = text.index('\n---\n')
            text = text[:pos] + '\n' + note + '\n' + text[pos:]
        else:
            lines = text.splitlines(keepends=True)
            line_no = 553 if path.startswith('planning/') else 1828
            line = lines[line_no - 1]
            assert 'R6-DX-DEBUG-001' in line and line.count('WP72 §5.2／WP27') == 1
            link = '../' + ERRATA
            lines[line_no - 1] = line.replace('WP72 §5.2／WP27',
                'WP72 §5.3／WP27（当前导航勘误：[GR7-H08-001](' + link + ')）')
            text = ''.join(lines)
        target = OUT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(text.encode())
        changed.append({'path': path, 'candidate_path': str(target.relative_to(ROOT)),
                        'baseline': {'commit': B, **inputs[path]}, 'new': identity(target.read_bytes())})

    sync_path = 'review/remediation-sixth-20261014-prepare/integration/public-sync-20261014/sync-input.json'
    sync = git('show', B + ':' + sync_path)
    item = json.loads(sync)['items'][42]
    assert item['id'] == 'R6-DX-DEBUG-001' and item['actual_clause_label'] == 'WP72 §5.2／WP27'
    wp72 = 'deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md'
    body = git('show', B + ':' + wp72)
    clause = body.splitlines(keepends=True)[123]
    assert '加道具' in clause.decode()
    errata = {
        'schema': 'r7.current-navigation-errata.v1', 'batch_id': 'R7-U12',
        'status': 'CANDIDATE_READY_NOT_REVIEWED', 'formal_writer': 'R7-I only after independent candidate review',
        'record_id': 'GR7-H08-001', 'subject_id': 'R6-DX-DEBUG-001',
        'old_label': 'WP72 §5.2／WP27', 'current_label': 'WP72 §5.3／WP27',
        'precedence': 'After R7-I integrates and accepts this entry, it takes precedence only for current navigation for this ID. The frozen R6 payload remains historical, unchanged; no behavior, acceptance or CLOSED decision is replaced.',
        'frozen_original': {'repository': 'y805939188/pokemon-essentials-clean-room', 'commit': B,
            'path': sync_path, 'pointer': '/items/42/actual_clause_label', **identity(sync),
            'subject_id': item['id'], 'contract_path': item['contract_path'],
            'contract_pointer': item['contract_pointer'], 'contract_identity': item['contract_identity']},
        'current_clause': {'repository': 'y805939188/pokemon-essentials-clean-room', 'commit': B,
            'path': wp72, **identity(body), 'section': '5.3', 'heading_line': 122,
            'rule_line': 124, 'rule_line_identity_including_LF': identity(clause),
            'ordinary_control': 'Section 5.2 lines 112–120 covers party/storage; add-item rule is section 5.3 line 124.',
            'inventory_cross_reference': 'WP27 §3.2–3.3; unchanged'},
        'fixed_source': {'repository': 'Maruno17/pokemon-essentials', 'commit': R,
            'tree': '7589c800b61ba13a13040ed0d686979b80a84fd0',
            'locators': [{k: row[k] for k in ('path','bytes','sha256','git_blob_content_id')} |
                         {'lines': [[778,797]] if 'MenuCommands' in row['path'] else [[81,93],[263,281]]}
                         for row in plan['fixed_read_inputs'] if row['commit'] == R]},
        'current_projections': [
            {'path': 'planning/feature-matrix.md', 'baseline_line': 553, 'subject_id': item['id']},
            {'path': 'audit/source-traceability.md', 'baseline_line': 1828, 'subject_id': item['id']}],
        'preserved_scope': ['WP72 §5.2/§5.3 behavior and WP27 unchanged',
            'DG-U08-01–04 and all R6 IDs/states unchanged',
            'Normal quantity 1 adds 1 when capacity/dependencies permit; list cancel/quantity 0 do not add or request giving message.',
            'Finite one-slot max 999, initial 998, request 2: add 1, false return, no successful-add sorting; after normal add return feedback still uses request 2.',
            'Zero room can add zero with false return and requested-quantity feedback. Add/message failures retain reached writes and do not guarantee normal feedback or cleanup.',
            'Frozen R6 input, acceptance, closure and receipt bytes unchanged; old 56/92 closure boundaries preserved'],
        'evidence': {'SOURCE_STATIC': 'Selected fixed source ranges read; not executed',
            'DERIVED_VECTOR': 'Paper expectations only; NOT_EXECUTED',
            'TOOL_VALIDATION': 'Identity and current navigation/projection checks only',
            'REFERENCE_OBSERVATION': 'NOT_EXECUTED', 'host_Demo_native_media_real_save_replay': 0,
            'supplement_search_qualification': 'Prior nine-supplement searches were locator searches, not nine complete semantic readings.'},
        'reception': {'candidate_review': 'PENDING different actual context ultra reviewer after R7-I candidate-input freeze',
            'shared_integration': 'PENDING R7-I clause integration; CG01/CG07 remain',
            'actual_integration_review': 'PENDING new R7-IR', 'ACCEPTED': False, 'CLOSED': False}}
    dump(OUT / ERRATA, errata)
    changed.append({'path': ERRATA, 'candidate_path': 'candidates/R7-U12/' + ERRATA,
                    'baseline': {'commit': B, 'exists': False, 'bytes': None, 'sha256': None, 'git_blob': None},
                    'new': identity((OUT / ERRATA).read_bytes())})
    dump(EVID / 'mirror-identities.json', {'baseline_commit': B, 'historical_commit': H,
         'files': changed, 'historical_targets': history})
    print(json.dumps({'status': 'SIX_ISOLATED_MIRRORS_CREATED', 'files': len(changed),
                      'navigation_occurrences': 10, 'history_targets': len(history)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
