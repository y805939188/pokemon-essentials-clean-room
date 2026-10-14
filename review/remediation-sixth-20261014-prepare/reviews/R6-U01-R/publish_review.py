"""Finite ordinary publication and full immutable remote object readback."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

CWD = pathlib.Path('/workspace/pokemon-essentials-clean-room')
ROOT = pathlib.Path(__file__).resolve().parent
PREFIX = str(ROOT.relative_to(CWD))
PARENT = '0f2bf0318405ab281682023c6cf0a68eabdd73ad'
BRANCH = 'codex/remediation-sixth-r6-u01-review-20261014'
URL = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
REMOTE_DB = pathlib.Path('/tmp/r6-u01-r-payload-remote.git')
SCRATCH = pathlib.Path('/tmp/r6-u01-r-publication')
SCRATCH.mkdir(exist_ok=True)
LOGS = SCRATCH / 'logs'
LOGS.mkdir(exist_ok=True)
journal = []

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def identity(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}

def run(argv, cwd=CWD):
    n = len(journal) + 1
    start = now()
    result = subprocess.run(argv, cwd=cwd, capture_output=True)
    end = now()
    out = LOGS / f'{n:04d}.stdout'
    err = LOGS / f'{n:04d}.stderr'
    out.write_bytes(result.stdout)
    err.write_bytes(result.stderr)
    row = {'number': n, 'cwd': str(cwd), 'argv': argv, 'start_utc': start, 'end_utc': end,
           'exit': result.returncode, 'stdout': str(out), 'stderr': str(err),
           'stdout_identity': identity(result.stdout), 'stderr_identity': identity(result.stderr)}
    if len(result.stdout) <= 12000:
        row['stdout_text'] = result.stdout.decode(errors='replace')
    if len(result.stderr) <= 12000:
        row['stderr_text'] = result.stderr.decode(errors='replace')
    journal.append(row)
    (SCRATCH / 'commands.json').write_text(json.dumps(journal, ensure_ascii=False, indent=2) + '\n')
    if result.returncode:
        raise RuntimeError({'command': argv, 'exit': result.returncode, 'stderr': result.stderr.decode(errors='replace')})
    return result.stdout

def git(*args):
    return run(['git', *args])

def remote_git(*args):
    return run(['git', '-C', str(REMOTE_DB), *args])

def entries(data):
    return sorted(data.decode().splitlines())

def readback(commit):
    remote_git('fetch', '--depth=1', '--filter=blob:none', URL, commit)
    assert remote_git('rev-parse', 'FETCH_HEAD').decode().strip() == commit
    local_tree = git('rev-parse', commit + '^{tree}').decode().strip()
    remote_tree = remote_git('rev-parse', commit + '^{tree}').decode().strip()
    assert local_tree == remote_tree
    local_entries = entries(git('ls-tree', '-r', '-t', commit, '--', PREFIX))
    remote_entries = entries(remote_git('ls-tree', '-r', '-t', commit, '--', PREFIX))
    assert local_entries == remote_entries
    payloads = []
    local_bodies = {}
    remote_bodies = {}
    for line in local_entries:
        meta, path = line.split('\t', 1)
        mode, typ, sha = meta.split()
        if typ != 'blob':
            continue
        if sha not in local_bodies:
            local_bodies[sha] = git('cat-file', 'blob', sha)
            remote_bodies[sha] = remote_git('cat-file', 'blob', sha)
            assert local_bodies[sha] == remote_bodies[sha], path
            assert identity(remote_bodies[sha])['git_blob'] == sha
        payloads.append({'path': path, 'mode': mode, 'type': typ, **identity(remote_bodies[sha]),
                         'local_remote_full_bytes_equal': True})
    branch_tip = git('ls-remote', URL, 'refs/heads/' + BRANCH).decode().split()[0]
    assert branch_tip == commit
    result = {'state': 'COMPLETE_NEW_REPORT_PAYLOAD_READBACK_PASS', 'observed_utc': now(),
              'commit': commit, 'workspace_tree': local_tree,
              'review_directory_tree': remote_git('rev-parse', commit + ':' + PREFIX).decode().strip(),
              'remote_branch': 'refs/heads/' + BRANCH, 'observed_remote_tip': branch_tip,
              'review_prefix': PREFIX, 'file_paths': len(payloads), 'distinct_full_blob_bodies': len(remote_bodies),
              'tree_entries_below_prefix': len(local_entries), 'payload_bytes_by_path': sum(x['bytes'] for x in payloads),
              'mode_type_path_tree_complete_match': True, 'payloads': payloads,
              'method': 'Fresh independently fetched remote object database; read each complete distinct blob, compare raw bytes and all path/mode/type/tree entries to exact local commit; shared bodies mapped to every path',
              'evidence_level': 'TOOL_VALIDATION', 'reference_or_behavior_or_host_execution': 0,
              'formal_acceptance': 'NOT_GRANTED', 'CLOSED': 'NOT_REGISTERED'}
    return result

def publication_push():
    result = run(['git', 'push', 'origin', 'HEAD:refs/heads/' + BRANCH])
    print('ordinary push completed', result.decode(errors='replace'), flush=True)

def main():
    assert git('branch', '--show-current').decode().strip() == BRANCH
    assert git('rev-parse', 'HEAD').decode().strip() == PARENT
    changed = git('diff', '--name-only').decode().splitlines()
    assert not changed
    findings = json.loads((ROOT / 'findings.json').read_text())
    assert [(r['id'], r['verdict']) for r in findings['records']] == [('GR6-K-001', 'PASS'), ('GR6-K-002', 'PASS'), ('GR6-K-003', 'PASS')]
    assert not findings['required_repairs']
    assert git('rev-parse', 'HEAD:deliverables/final-specification-set').decode().strip() == '1046fbb657882e84b3dfc6d017943a9edf7782e5'
    files = sorted(p for p in ROOT.rglob('*') if p.is_file())
    assert not any('publication' in p.relative_to(ROOT).parts for p in files)
    manifest = {'schema': 'r6-u01-review-finite-core-manifest.v1', 'created_utc': now(),
                'reviewed_candidate': PARENT, 'self_hash_excluded': 'core-manifest.json',
                'publication_files_are_later_finite_binding': True,
                'items': [{'path': str(p.relative_to(CWD)), 'mode': '100644', 'type': 'blob', **identity(p.read_bytes())} for p in files]}
    (ROOT / 'core-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    git('add', '--', PREFIX)
    staged = git('diff', '--cached', '--name-only').decode().splitlines()
    assert staged and all(x.startswith(PREFIX + '/') for x in staged)
    formatted = [p for p in staged if '/logs/' not in p and not p.endswith(('.stdout', '.stderr', '.patch'))]
    git('diff', '--cached', '--check', '--', *formatted)
    git('commit', '-m', 'Review frozen R6-U01 candidate: three scoped static PASS verdicts')
    core = git('rev-parse', 'HEAD').decode().strip()
    print('review semantic core', core, flush=True)
    publication_push()
    core_readback = readback(core)
    (SCRATCH / 'core-readback.json').write_text(json.dumps(core_readback, ensure_ascii=False, indent=2) + '\n')
    publication_dir = ROOT / 'publication'
    publication_dir.mkdir()
    (publication_dir / 'core-readback.json').write_text(json.dumps(core_readback, ensure_ascii=False, indent=2) + '\n')
    binding = {'state': 'REVIEW_CORE_PUBLISHED_AND_COMPLETELY_READ_BACK', 'recorded_utc': now(),
               'reviewed_candidate': PARENT, 'review_core_commit': core,
               'review_core_workspace_tree': core_readback['workspace_tree'],
               'review_core_directory_tree': core_readback['review_directory_tree'],
               'core_manifest': {'path': PREFIX + '/core-manifest.json', **identity((ROOT / 'core-manifest.json').read_bytes())},
               'core_readback': {'path': PREFIX + '/publication/core-readback.json', **identity((publication_dir / 'core-readback.json').read_bytes())},
               'core_payload_paths': core_readback['file_paths'], 'core_distinct_blobs': core_readback['distinct_full_blob_bodies'],
               'ordinary_branch': BRANCH, 'candidate_verdicts': {x['id']: 'PASS' for x in findings['records']},
               'requested_repairs': 0, 'formal_acceptance': 'NOT_GRANTED', 'CLOSED': 'NOT_REGISTERED',
               'final_publication_commit_tree': 'Bound externally by final response after actual P commit/push/full readback; no recursive self-hash'}
    (publication_dir / 'publication-binding.json').write_text(json.dumps(binding, ensure_ascii=False, indent=2) + '\n')
    (publication_dir / 'core-publication-commands.json').write_text(json.dumps({'scope': 'Actual core freeze/push and full immutable readback commands only; large stdout full raw files retained at declared scratch paths with exact identities', 'commands': journal}, ensure_ascii=False, indent=2) + '\n')
    git('add', '--', PREFIX + '/publication')
    git('diff', '--cached', '--check')
    git('commit', '-m', 'Bind R6-U01 review core publication and complete remote readback')
    publication = git('rev-parse', 'HEAD').decode().strip()
    publication_push()
    final = readback(publication)
    final['core_commit'] = core
    final['core_workspace_tree'] = core_readback['workspace_tree']
    final['core_review_directory_tree'] = core_readback['review_directory_tree']
    delta = git('diff', '--name-only', PARENT, publication).decode().splitlines()
    assert len(delta) == final['file_paths'] and all(x.startswith(PREFIX + '/') for x in delta)
    assert not git('status', '--porcelain').strip()
    final['only_review_prefix_changed'] = True
    final['worktree_clean'] = True
    receipt = SCRATCH / 'final-readback.json'
    receipt.write_text(json.dumps(final, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in final.items() if k != 'payloads'}, ensure_ascii=False, indent=2), flush=True)
    print('final external receipt', str(receipt), identity(receipt.read_bytes()), flush=True)

try:
    main()
except Exception as exc:
    (SCRATCH / 'failure.json').write_text(json.dumps({'utc': now(), 'error': str(exc), 'automatic_retries': 0,
          'journal': str(SCRATCH / 'commands.json'), 'force': False, 'delete': False}, ensure_ascii=False, indent=2) + '\n')
    raise
