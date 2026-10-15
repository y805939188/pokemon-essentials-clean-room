"""Validate artifact identity and bounded differences, never reference behavior."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[4]
PREFIX = ROOT / 'candidates/R7-U07'
EVIDENCE = PREFIX / 'evidence/author'
BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'
PATHS = [
    'deliverables/final-specification-set/combat-requirements/wp55-facility-session-and-restoration.md',
    'deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md',
]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


def main():
    assert git('branch', '--show-current').decode().strip() == 'codex/r7-u07-author-20261015-wave1'
    assert git('rev-parse', f'{BASE}:deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    changes = []
    for relative in PATHS:
        old = git('show', f'{BASE}:{relative}')
        assert (ROOT / relative).read_bytes() == old, 'Formal working bytes changed'
        new = (PREFIX / relative).read_bytes()
        a, b = old.decode().splitlines(True), new.decode().splitlines(True)
        edits = [x for x in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes() if x[0] != 'equal']
        if relative == PATHS[0]:
            assert [(op, i, j) for op, i, j, _, _ in edits] == [('replace', 92, 93), ('replace', 123, 124)], edits
        else:
            assert len(edits) == 1 and edits[0][0] == 'insert', edits
            _, i, j, k, end = edits[0]
            assert i == j == 103 and a[i].startswith('## PA：'), edits
            assert b[:k] + b[end:] == a, 'Existing catalog bytes changed'
            assert sum(line.startswith('| GR7-M12-001-C') for line in b[k:end]) == 6
        for _, _, _, i, j in edits:
            text = ''.join(b[i:j])
            assert not any(s in text for s in ['Data/Scripts/', 'createPokemon', 'def ', 'class ']), 'Source expression in new specification'
        changes.append({'path': relative, 'before': identity(old), 'after': identity(new), 'opcodes': edits})
    historical = ['deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md',
                  'deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md',
                  'deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md']
    for relative in historical:
        assert (ROOT / relative).read_bytes() == git('show', f'{BASE}:{relative}')
    record = json.loads((EVIDENCE / 'per-id.json').read_text())
    assert record['state'] == 'CANDIDATE_READY_NOT_REVIEWED'
    assert len(record['vectors']) == 6
    assert all(v['execution'] == 'NOT_EXECUTED' and v['stage'] == 'DERIVED_VECTOR' for v in record['vectors'])
    assert all(v == 'NOT_REACHED' for v in record['gates'].values())
    json_count = 0
    files = []
    for path in sorted(PREFIX.rglob('*')):
        assert not path.is_symlink()
        if not path.is_file():
            continue
        rel = str(path.relative_to(PREFIX))
        assert rel in PATHS or rel.startswith('evidence/author/'), rel
        if path.suffix == '.json':
            json.loads(path.read_text())
            json_count += 1
        files.append(str(path.relative_to(ROOT)))
    changed = set(git('diff', '--name-only', BASE).decode().splitlines())
    changed.update(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    assert all(p.startswith('candidates/R7-U07/') for p in changed), sorted(changed)
    result = {'schema': 'r7.u07.artifact-tool-validation.v1',
              'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'result': 'TOOL_VALIDATION_COMPLETE', 'behavioral_execution': 'NOT_EXECUTED',
              'independent_review': 'NOT_PERFORMED', 'changes': changes,
              'existing_catalog_bytes_preserved': True, 'historical_files_unchanged': historical,
              'all_changes_within_allowlist': True, 'json_files_parsed': json_count,
              'files_checked': files, 'reference_host_fullmodel_Demo_native_save_replay_runs': 0}
    (EVIDENCE / 'validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['result', 'behavioral_execution', 'independent_review', 'existing_catalog_bytes_preserved', 'all_changes_within_allowlist', 'json_files_parsed']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
