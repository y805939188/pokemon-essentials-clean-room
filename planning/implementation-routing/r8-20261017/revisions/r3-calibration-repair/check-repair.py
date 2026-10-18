#!/usr/bin/env python3
"""Prove exact seven-leaf repair, source binding and complete patch reconstruction."""
import argparse
import ast
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INV = HERE.parents[1]
ROOT = INV.parents[2]
BASE = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
REVIEW = '34202eb7accfee48bb8761db88b340bd77f54a42'
SOURCE = '5f87743293290de2e219ecdd6c19e88280f60c9a'
PREFIX = str(INV.relative_to(ROOT)) + '/'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def differences(a, b, pointer=''):
    if type(a) != type(b):
        return [pointer]
    if isinstance(a, dict):
        assert a.keys() == b.keys(), pointer
        return [p for k in a for p in differences(a[k], b[k], pointer + '/' + k)]
    if isinstance(a, list):
        assert len(a) == len(b), pointer
        return [p for i, (x, y) in enumerate(zip(a, b)) for p in differences(x, y, pointer + '/' + str(i))]
    return [pointer] if a != b else []


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE / 'repair-proof.json')
    args = parser.parse_args()
    receipt = load(HERE / 'correction-record.json')
    before_bytes = git('show', BASE + ':' + PREFIX + 'routing-manifest.json')
    current_bytes = (INV / 'routing-manifest.json').read_bytes()
    before = json.loads(before_bytes)
    current = json.loads(current_bytes)
    changes = differences(before, current)
    assert sorted(changes) == sorted(r['pointer'] for r in receipt['records'])
    assert sha(before_bytes) == receipt['manifest_before_sha256']
    assert sha(current_bytes) == receipt['manifest_after_sha256']
    fs = {f['feature_id']: f for f in current['features']}
    delta = {r['feature_id']: r for r in load(INV / 'revisions/r3/feature-source-deltas.json')['records']}
    files = {r['document']: r for r in load(INV / 'revisions/r3/source-file-reassessment.json')['records']}
    module = importlib.util.spec_from_file_location('repair_inputs', HERE / 'repair-seven-narratives.py')
    repair = importlib.util.module_from_spec(module)
    module.loader.exec_module(repair)
    source_results = []
    for row in receipt['records']:
        fid = row['feature_id']
        src = row['fixed_source']
        raw = git('show', SOURCE + ':' + src['document'])
        lines = raw.decode().splitlines(keepends=True)
        unit = ''.join(''.join(lines[a-1:b]) for a, b in src['line_ranges']).encode()
        assert sha(raw) == src['file_sha256']
        assert sha(unit) == src['unit_sha256']
        assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == src['file_git_blob']
        assert fs[fid]['differences'][1] == row['after']
        assert delta[fid]['source_fact_delta'] == repair.FACTS[fid]
        name = Path(src['document']).name
        assert files[src['document']]['source_fact_reassessment'] == repair.FILE_FACTS[name]
        assert files[src['document']]['future_plan_reassessment'] == delta[fid]['future_boundary_reassessment'] == repair.BOUNDARIES[name]
        source_results.append({'feature_id': fid, 'source_identity_matches_fixed_git': True,
                               'complete_effective_ranges': src['line_ranges'], 'unit_sha256': sha(unit)})
    archive_path = INV / 'revisions/r3/tools/post-source-pre-semantic-35175c7094b0.json.gz'
    archived = gzip.decompress(archive_path.read_bytes())
    patch_path = INV / 'revisions/r3/source-refinement-patch.json'
    patch = load(patch_path)
    old_patch = json.loads(git('show', BASE + ':' + PREFIX + 'revisions/r3/source-refinement-patch.json'))
    assert sha(archived) == patch['input_manifest_sha256']
    assert archive_path.read_bytes() == git('show', BASE + ':' + PREFIX + str(archive_path.relative_to(INV)))
    expected_patch = copy.deepcopy(old_patch)
    for row in expected_patch['records']:
        if row['feature_id'] in repair.FACTS:
            next(c for c in row['field_changes'] if c['pointer'] == '/differences')['after'] = fs[row['feature_id']]['differences']
    assert patch == expected_patch, 'Only the seven declared patch after-values may change'
    expected = json.loads(archived)
    expected_fs = {f['feature_id']: f for f in expected['features']}
    for row in patch['records']:
        for change in row['field_changes']:
            obj = expected_fs[row['feature_id']]
            parts = change['pointer'].strip('/').split('/')
            for part in parts[:-1]:
                obj = obj[part]
            assert obj[parts[-1]] == change['before']
            obj[parts[-1]] = copy.deepcopy(change['after'])
    expected_bytes = (json.dumps(expected, ensure_ascii=False, indent=2) + '\n').encode()
    assert expected == current and expected_bytes == current_bytes
    generator = (INV / 'revisions/r3/build-author-evidence.py').read_text()
    old_generator = git('show', BASE + ':' + PREFIX + 'revisions/r3/build-author-evidence.py').decode()
    assert generator.splitlines()[:7] == old_generator.splitlines()[:7]
    tree = ast.parse(generator)
    assignments = {n.targets[0].id: n.value for n in tree.body if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name)}
    manual = ast.literal_eval(assignments['manual'])
    units = ast.literal_eval(assignments['unit_narratives'])
    for name in repair.FILE_FACTS:
        assert manual[name] == (repair.FILE_FACTS[name], repair.BOUNDARIES[name])
    assert units == {k: repair.FACTS[k] for k in ['FR-000029', 'FR-000032']}
    for name in ['author-refinement-application.json', 'source-narrative-correction.json']:
        assert (INV / 'revisions/r3' / name).read_bytes() == git('show', BASE + ':' + PREFIX + 'revisions/r3/' + name)
    for name in ['facet-inheritance.json', 'feature-resolution.json']:
        data = load(INV / 'revisions/r3' / name)
        old_data = json.loads(git('show', BASE + ':' + PREFIX + 'revisions/r3/' + name))
        expected_data = copy.deepcopy(old_data)
        key = 'records' if name.startswith('facet') else 'active_feature_results'
        byid = {r['feature_id']: r for r in data[key]}
        for row in expected_data[key]:
            if row['feature_id'] in repair.FACTS:
                row['current_calibration_repair'] = byid[row['feature_id']]['current_calibration_repair']
                assert row['current_calibration_repair']['author_status'] == 'CORRECTED_AWAITING_INDEPENDENT_REVIEW'
        assert data == expected_data
    changed_paths = set(git('diff', '--name-only', BASE).decode().splitlines())
    changed_paths.update(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    assert all(p.startswith(PREFIX) for p in changed_paths)
    assert not git('diff', BASE, '--', 'deliverables/final-specification-set', 'reference')
    checks = {
        'exact_seven_manifest_leaf_changes_only': True,
        'all_other_manifest_values_preserved': True,
        'seven_source_units_match_actual_5f_git': True,
        'unit_and_file_evidence_synchronized': True,
        'original_35175_archive_and_application_receipts_byte_preserved': True,
        'only_seven_consolidated_patch_after_values_changed': True,
        'complete_manifest_object_and_serialized_bytes_reconstructed': True,
        'reusable_generator_fact_boundary_and_unit_overrides_synchronized': True,
        'historical_writer_fixed_input_guard_unchanged': True,
        'only_seven_current_facet_resolution_rows_extended': True,
        'only_independent_routing_directory_changed': True,
        'formal_and_reference_diff_empty': True,
    }
    result = {'schema_version': 'routing-r3-seven-repair-proof.v1',
              'role': 'AUTHOR_EXACT_CHANGE_AND_STATIC_STRUCTURE_ONLY; independent semantic acceptance pending',
              'fixed_candidate': BASE, 'fixed_review': REVIEW, 'current_source': SOURCE,
              'manifest_sha256': sha(current_bytes), 'patch_sha256': sha(patch_path.read_bytes()),
              'manifest_changed_pointers': changes, 'source_results': source_results,
              'reconstruction': {'rows': len(patch['records']), 'fields': sum(len(r['field_changes']) for r in patch['records']),
                                 'object_and_serialized_bytes_equal': True},
              'static_distinguishing_cases_not_executed': [
                  'HP255 + ATK255 = total510; HP per-stat allowance252−255=−3 fails before total clamp.',
                  'HP/ATK/DEF/SPA/SPD100, SPE20 gives total520, first per-stat allowance152 and total allowance−10; total excess does not imply first per-stat failure.',
                  'Accumulator−1: floor(−1/200)=−1, distinguish truncation or clamp to0.',
                  'ActiveRepel: first nonEgg faintedL50, next ableL10, wildL20; default rejects, alternate allows if other gates pass.',
                  'Recorded-battle storage no-op does not imply replay bag isolation or normal-terminal callback suppression.'
              ], 'checks': checks, 'all_passed': all(checks.values())}
    save(args.output, result)
    print(json.dumps({'checks': checks, 'all_passed': result['all_passed'], 'manifest_sha256': result['manifest_sha256']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
