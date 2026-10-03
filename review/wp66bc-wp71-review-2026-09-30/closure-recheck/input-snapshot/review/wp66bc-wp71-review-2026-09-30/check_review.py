"""Reviewer-owned text/hash/JSON/diff checks. Never executes reference material."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent.parent
REF = ROOT / 'reference/pokemon-essentials'
DELIVERY = ROOT / 'review/wp66bc-wp71-delivery-2026-09-30'
BASE = ROOT / 'review/wp22-wp23-wp32-review-2026-09-30/recheck-v2/input-snapshot'
COMMIT = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def ident(b):
    return {'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}

def put(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def rebuild(original, diff):
    """Reconstruct a single UTF-8 unified diff in memory, with exact context checks."""
    src = original.decode().splitlines(keepends=True)
    lines = diff.decode().splitlines(keepends=True)
    result, cursor, i = [], 0, 0
    while i < len(lines):
        if not lines[i].startswith('@@ '):
            i += 1
            continue
        m = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', lines[i])
        assert m
        start = int(m[1]) - 1 if int(m[1]) else 0
        assert start >= cursor
        result.extend(src[cursor:start])
        cursor = start
        old_count = new_count = 0
        i += 1
        while i < len(lines) and not lines[i].startswith('@@ '):
            line = lines[i]
            assert line[0] in ' +-'
            if line[0] in ' -':
                assert src[cursor] == line[1:]
                cursor += 1
                old_count += 1
            if line[0] in ' +':
                result.append(line[1:])
                new_count += 1
            i += 1
        assert old_count == int(m[2] or 1)
        assert new_count == int(m[4] or 1)
    result.extend(src[cursor:])
    return ''.join(result).encode()

def main():
    manifest = json.loads((OUT / 'input-manifest.json').read_text())
    for row in manifest['inputs']:
        expected = {k: row[k] for k in ('sha256', 'bytes')}
        assert ident((ROOT / row['path']).read_bytes()) == expected, row['path']
        assert ident((OUT / 'input-snapshot' / row['path']).read_bytes()) == expected
    for row in manifest['external_inputs']:
        expected = {k: row[k] for k in ('sha256', 'bytes')}
        assert ident(Path(row['path']).read_bytes()) == expected
        assert ident((OUT / row['snapshot']).read_bytes()) == expected
    supplemental = json.loads((OUT / 'supplemental-inputs.json').read_text())
    for row in supplemental:
        expected = {k: row[k] for k in ('sha256', 'bytes')}
        assert ident(Path(row['path']).read_bytes()) == expected
        assert ident((OUT / row['snapshot']).read_bytes()) == expected

    binding = json.loads((DELIVERY / 'diff-bindings.json').read_text())
    diffs, staged = [], None
    for row in binding['bindings']:
        original = (BASE / row['path']).read_bytes()
        assert ident(original) == row['from_snapshot']
        result = rebuild(original, (DELIVERY / row['diff']).read_bytes())
        assert ident(result) == row['to_current'], row['path']
        if row['path'] == 'planning/feature-matrix.md':
            staged = result
        else:
            assert result == (ROOT / row['path']).read_bytes()
        diffs.append({'path': row['path'], 'reconstruction': 'PASS', 'to': ident(result)})
    row = binding['batch_final_matrix']
    assert ident(staged) == row['from_staged']
    result = rebuild(staged, (DELIVERY / row['increment_diff']).read_bytes())
    assert ident(result) == row['to_batch_final']
    assert result == (ROOT / row['path']).read_bytes()
    put('diff-checks.json', {'backfill_diffs': diffs, 'matrix_two_stage': 'PASS', 'final_matrix': ident(result)})

    sources = json.loads((DELIVERY / 'source-identities.json').read_text())['sources']
    additional = [
        'Data/Scripts/001_Settings.rb',
        'Data/Scripts/010_Data/001_GameData.rb',
        'Data/Scripts/010_Data/002_PBS data/006_Item.rb',
        'Data/Scripts/013_Items/001_Item_Utilities.rb',
        'Data/Scripts/013_Items/002_Item_Effects.rb',
        'Data/Scripts/015_Trainers and player/001_Trainer.rb',
        'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',
        'Data/Scripts/016_UI/023_UI_PurifyChamber.rb',
    ]
    source_checks = []
    for path in sorted({r['path'] for r in sources} | set(additional)):
        b = (REF / path).read_bytes()
        pinned = subprocess.check_output(['git', '-C', str(REF), 'show', COMMIT + ':' + path])
        assert b == pinned
        original = next((r for r in sources if r['path'] == path), None)
        if original:
            assert ident(b) == {k: original[k] for k in ('sha256', 'bytes')}
        source_checks.append({'path': path, **ident(b), 'pinned_blob_match': True,
                              'semantic_read_scope': 'See reading-log.md; hash verification is not a claim of full semantic review.'})
    put('source-checks.json', {'reference_commit': COMMIT, 'sources': source_checks})

    json_paths = list(DELIVERY.glob('*.json'))
    for path in json_paths:
        json.loads(path.read_text())
    bc = json.loads((DELIVERY / 'boundary-checks.json').read_text())
    bound = []
    def walk(value):
        if isinstance(value, dict):
            target = value.get('receiver', value.get('path'))
            if target and all(k in value for k in ('sha256', 'bytes')) and (ROOT / target).is_file():
                assert ident((ROOT / target).read_bytes()) == {k: value[k] for k in ('sha256', 'bytes')}
                bound.append(target)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(bc)
    assert len(bound) == 9
    scenarios = {}
    for path, prefix, count in [
        ('specs/ui/wp66-b-storage-and-pokedex-ui.md', 'B', 34),
        ('specs/ui/wp66-c-bag-item-storage-and-shop-ui.md', 'C', 34),
        ('specs/ui/wp71-tile-puzzles.md', 'T', 18),
    ]:
        ids = re.findall(r'^\| (' + prefix + r'\d+) \|', (ROOT / path).read_text(), re.M)
        assert ids == [prefix + f'{i:02}' for i in range(1, count + 1)]
        scenarios[path] = {'count': len(ids), 'unique_and_contiguous': True, 'behavior_status': 'REQUEST_CHANGES; see findings.json'}
    head = subprocess.check_output(['git', '-C', str(REF), 'rev-parse', 'HEAD'], text=True).strip()
    status = subprocess.check_output(['git', '-C', str(REF), 'status', '--porcelain'], text=True)
    assert head == COMMIT and status == ''
    put('review-checks.json', {
        'mechanical_status': 'PASS', 'behavior_status': 'REQUEST_CHANGES',
        'fixed_inputs_unchanged': len(manifest['inputs']),
        'input_snapshots_unchanged': len(manifest['inputs']),
        'external_handoff_inputs_unchanged': len(manifest['external_inputs']),
        'supplemental_external_inputs_unchanged': len(supplemental),
        'source_blob_matches': len(source_checks), 'delivery_json_parsed': len(json_paths),
        'boundary_identity_bindings': bound, 'backfill_diff_reconstructions': 10,
        'matrix_two_stage_reconstruction': True, 'scenarios': scenarios,
        'reference_head': head, 'reference_status': status,
        'execution_scope': 'Only this reviewer-owned checker; text/hash/JSON/diff reconstruction and read-only Git. No reference execution.'
    })
    print(json.dumps({'mechanical': 'PASS', 'inputs': len(manifest['inputs']), 'sources': len(source_checks),
                      'diffs': 10, 'matrix_stages': 2, 'boundary_bindings': len(bound), 'scenarios': 86}))

if __name__ == '__main__':
    main()
