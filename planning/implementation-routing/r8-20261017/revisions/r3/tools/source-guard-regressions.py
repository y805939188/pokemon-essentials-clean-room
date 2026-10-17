#!/usr/bin/env python3
"""Author isolated static Git/schema regressions for SOURCE-R2-001..003."""
from pathlib import Path
import argparse
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INVENTORY = HERE.parents[2]
ROOT = INVENTORY.parents[2]
PREVIOUS = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    result = {'schema_version': 'routing-r3-source-guard-regressions.v1',
              'scope': 'AUTHOR_ISOLATED_STATIC_DOCUMENT_FIXTURES; no game/reference execution or semantic review',
              'previous_candidate': PREVIOUS, 'checks': [], 'fixture_commands': []}
    with tempfile.TemporaryDirectory(prefix='r8-r3-source-guards-') as directory:
        fixture = Path(directory)
        inv = fixture / INVENTORY.relative_to(ROOT)
        shutil.copytree(INVENTORY, inv)
        subprocess.run(['git', 'init', '--quiet', str(fixture)], check=True, capture_output=True)
        common = subprocess.check_output(['git', 'rev-parse', '--path-format=absolute', '--git-common-dir'], cwd=ROOT, text=True).strip()
        (fixture / '.git/objects/info/alternates').write_text(str(Path(common) / 'objects') + '\n')
        def git(*argv, data=None):
            done = subprocess.run(['git', *argv], input=data, cwd=fixture, capture_output=True,
                                  env={**os.environ, 'GIT_AUTHOR_NAME': 'Static routing fixture',
                                       'GIT_AUTHOR_EMAIL': 'fixture@example.invalid',
                                       'GIT_COMMITTER_NAME': 'Static routing fixture',
                                       'GIT_COMMITTER_EMAIL': 'fixture@example.invalid',
                                       'GIT_AUTHOR_DATE': '2026-10-17T00:00:00Z',
                                       'GIT_COMMITTER_DATE': '2026-10-17T00:00:00Z'})
            result['fixture_commands'].append({'argv': ['git', *argv], 'exit_code': done.returncode,
                'stdin_sha256': hashlib.sha256(data).hexdigest() if data is not None else None,
                'stdout_sha256': hashlib.sha256(done.stdout).hexdigest(), 'stderr': done.stderr.decode()})
            done.check_returncode()
            return done.stdout
        old_path = inv / 'routing-r2-fixture.py'
        relative = str((INVENTORY / 'routing.py').relative_to(ROOT))
        old_path.write_bytes(subprocess.check_output(['git', 'show', PREVIOUS + ':' + relative], cwd=ROOT))
        old = module('r2_static_gate', old_path)
        new = module('r3_static_gate', inv / 'routing.py')
        manifest = new.read_json(inv / 'routing-manifest.json')
        coverage = new.read_json(inv / 'section-coverage.json')
        registry = new.read_json(inv / 'accepted-source-updates.json')
        baseline_errors = new.errors(manifest, coverage, registry)
        assert not baseline_errors, baseline_errors[:10]
        snapshot = manifest['current_snapshot']['commit']
        path = new.FORMAL + 'generic-kernel/wp04-pbs-lifecycle.md'
        before = new.blob(snapshot, path)
        lines = before.decode().splitlines(keepends=True)
        assert 'VictoryME' in lines[195], 'Pinned WP04 fixture location changed'
        lines[195] = lines[195].rstrip('\n') + ' [AUTHOR UNRECEIPTED STATIC FIXTURE CHANGE]\n'
        altered = ''.join(lines).encode()
        blob = git('hash-object', '-w', '--stdin', data=altered).decode().strip()
        git('read-tree', snapshot)
        git('update-index', '--cacheinfo', '100644,' + blob + ',' + path)
        tree = git('write-tree').decode().strip()
        descendant = git('commit-tree', tree, '-p', snapshot, data=b'Isolated unreceipted document fixture\n').decode().strip()
        mutated = copy.deepcopy(manifest)
        mutated['current_snapshot']['commit'] = descendant
        mutated['current_snapshot']['formal_tree'] = git('rev-parse', descendant + ':' + new.FORMAL.rstrip('/')).decode().strip()
        for d in mutated['documents']:
            current = d['current_applicability']
            current['snapshot_commit'] = descendant
            current['identity'] = new.identity(descendant, current['path'])
        for f in mutated['features']:
            current = f['current_applicability']
            current['snapshot_commit'] = descendant
            identity = new.identity(descendant, current['document'])
            current['locator']['file_sha256'] = identity['sha256']
            current['locator']['file_git_blob'] = identity['git_blob']
            if current['document'] == path:
                current['locator']['unit_sha256'] = new.digest(''.join(
                    ''.join(lines[a-1:b]) for a,b in current['locator']['line_ranges']).encode())
        old_errors = old.errors(mutated, coverage, registry)
        new_errors = new.errors(mutated, coverage, registry)
        case = {'finding': 'SOURCE-R2-001', 'case': 'ancestor receipt cannot authorize changed descendant bytes',
                'parent': snapshot, 'synthetic_descendant': descendant, 'changed_path': path,
                'accepted_blob': new.identity(snapshot, path)['git_blob'], 'unaccepted_blob': blob,
                'new_receipt_supplied': False, 'real_baseline_errors': baseline_errors,
                'old_validator_errors': old_errors, 'new_validator_errors': new_errors,
                'passed': not old_errors and any('lack matching ACCEPTED target identity' in e for e in new_errors)}
        result['checks'].append(case)
        # Execute the actual apply path in the isolated copy, injecting one invalid
        # prospective output. The core write guard must fail before any core writes.
        tools = inv / 'revisions/r3/tools'
        backfill = module('r3_apply_guard', tools / 'backfill-accepted-sources.py')
        build = backfill.build_current_coverage
        def invalid_output(snapshot, sections):
            value = build(snapshot, sections)
            value['sections'][0]['metadata_reason'] = None
            return value
        backfill.build_current_coverage = invalid_output
        core_names = ['routing-manifest.json', 'accepted-source-updates.json', 'current-section-coverage.json', 'section-coverage.json']
        before_hashes = {name: sha(inv / name) for name in core_names}
        archives_before = {p.name: sha(p) for p in tools.glob('source-backfill-input-*.json.gz')}
        previous_argv = sys.argv
        sys.argv = [str(tools / 'backfill-accepted-sources.py'), 'apply', '--snapshot', snapshot,
                    '--new-mapping', str(inv / 'revisions/r3/new-heading-mappings.json')]
        caught = None
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                backfill.main()
        except AssertionError as error:
            caught = str(error)
        finally:
            sys.argv = previous_argv
        after_hashes = {name: sha(inv / name) for name in core_names}
        archives_after = {p.name: sha(p) for p in tools.glob('source-backfill-input-*.json.gz')}
        case = {'finding': 'SOURCE-R2-002', 'case': 'invalid prospective schema rejects before all core/archive writes',
                'injected_value': {'sections/0/metadata_reason': None}, 'actual_apply_guard_error': caught,
                'core_hashes_before': before_hashes, 'core_hashes_after': after_hashes,
                'archives_unchanged': archives_before == archives_after,
                'passed': bool(caught and 'invalid prospective current coverage' in caught)
                          and before_hashes == after_hashes and archives_before == archives_after}
        result['checks'].append(case)
        checker = module('r3_governance_guard', tools / 'current-coverage-check.py')
        data = new.read_json(inv / 'current-section-coverage.json')
        schema = new.read_json(inv / 'current-section-coverage.schema.json')
        real_errors = checker.check(data, manifest, schema)
        ordinary = copy.deepcopy(data)
        s = next(s for s in ordinary['sections'] if s['path'] == new.FORMAL + 'combat-requirements/wp39-battle-context-and-participants.md'
                 and s['anchor'] == '4-战斗初始化与布局')
        s.update(feature_refs=[], metadata_refs=[], coverage_scope='ALL_FORMAL_FEATURES')
        errors = checker.check(ordinary, manifest, schema)
        result['checks'].append({'finding': 'SOURCE-R2-003', 'case': 'ordinary behavior cannot borrow governance exemption',
            'real_current_coverage_errors': real_errors, 'negative_errors': errors,
            'fixed_governance_authority': checker.GOVERNANCE_AUTHORITY,
            'fixed_allowed_headings': len(checker.governance_headings()),
            'passed': not real_errors and any('requires fixed governance' in e for e in errors)})
        # A document containing only metadata has no active-feature snapshot
        # comparison. Its own current identity must still use the global snapshot.
        active_docs = {f['document_id'] for f in manifest['features']}
        document = next(d for d in manifest['documents'] if d['document_id'] not in active_docs
                        and d['upstream']['accepted_events'])
        metadata_path = document['current_applicability']['path']
        metadata_blob = git('hash-object', '-w', '--stdin', data=new.blob(snapshot, metadata_path)
                            + b'\n[AUTHOR UNRECEIPTED METADATA-ONLY STATIC FIXTURE]\n').decode().strip()
        git('read-tree', snapshot)
        git('update-index', '--cacheinfo', '100644,' + metadata_blob + ',' + metadata_path)
        metadata_tree = git('write-tree').decode().strip()
        metadata_descendant = git('commit-tree', metadata_tree, '-p', snapshot,
                                  data=b'Isolated metadata-only stale snapshot fixture\n').decode().strip()
        stale = copy.deepcopy(manifest)
        stale['current_snapshot']['commit'] = metadata_descendant
        stale['current_snapshot']['formal_tree'] = git('rev-parse', metadata_descendant + ':' + new.FORMAL.rstrip('/')).decode().strip()
        for d in stale['documents']:
            if d['document_id'] != document['document_id']:
                d['current_applicability']['snapshot_commit'] = metadata_descendant
                d['current_applicability']['identity'] = new.identity(metadata_descendant,d['current_applicability']['path'])
        for f in stale['features']:
            f['current_applicability']['snapshot_commit'] = metadata_descendant
        old_errors = old.errors(stale, coverage, registry)
        new_errors = new.errors(stale, coverage, registry)
        result['checks'].append({'finding':'SOURCE-R2-001','case':'metadata-only document cannot retain stale accepted snapshot',
            'document':metadata_path,'active_feature_count':0,'synthetic_descendant':metadata_descendant,
            'stale_document_snapshot':snapshot,'old_validator_errors':old_errors,'new_validator_errors':new_errors,
            'existing_guard_preserved':True,
            'passed':any('current applicability snapshot mismatch' in e for e in old_errors)
                     and any('current applicability snapshot mismatch' in e for e in new_errors)})
    result['all_passed'] = all(c['passed'] for c in result['checks'])
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_passed': result['all_passed'], 'checks': [{k:v for k,v in c.items() if k in ['finding','case','passed']}
                                                                  for c in result['checks']]}, ensure_ascii=False, indent=2))
    return int(not result['all_passed'])


if __name__ == '__main__':
    sys.exit(main())
