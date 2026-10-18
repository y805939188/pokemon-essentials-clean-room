"""Inert fixed-object identity checking and lossless bounded reading views.

Never runs restored code. View generation earns no semantic credit.
"""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

TASK = Path(__file__).resolve().parent
ROOT = TASK.parents[1]
REPO = ROOT.parents[2]
CONTRACT = '2d44dafe215842de6355f46de7d4d273d8b4c264'
ORIGINAL = ROOT / 'tasks/receive_external_legacy_manifest_currentness'
BARE = '/tmp/r8-recovery-legacy-g1-input.git'

def git(*args, bare=False):
    command = ['git', '--git-dir=' + BARE] if bare else ['git', '-C', str(REPO)]
    return subprocess.check_output(command + list(args))

def load(shard):
    return json.loads((ORIGINAL / f'split-contracts/{shard}.complete.json').read_text())

def digest(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

def recover():
    d = load('S01')
    commit = d['target_commit']
    assert git('rev-parse', commit + '^{tree}', bare=True).decode().strip() == d['target_checkout_tree']
    prefix = d['files'][0]['remote_path_at_target_commit'].rsplit('/', 1)[0]
    tree = git('rev-parse', commit + ':' + prefix, bare=True).decode().strip()
    assert tree == d['target_task_tree_observed_from_fixed_commit']
    entries = {}
    for raw in git('ls-tree', '-rz', commit, prefix, bare=True).split(b'\0'):
        if raw:
            meta, path = raw.split(b'\t')
            mode, kind, blob = meta.decode().split()
            assert kind == 'blob' and mode == '100644'
            entries[path.decode()] = (mode, blob)
    assert set(entries) == {f['remote_path_at_target_commit'] for f in d['files']}
    dest = TASK / '.cache/target-93d7df7f'
    dest.mkdir(parents=True, exist_ok=False)
    rows = []
    for f in d['files']:
        data = git('show', commit + ':' + f['remote_path_at_target_commit'], bare=True)
        ident = digest(data)
        assert (ident['bytes'], ident['sha256'], ident['blob']) == (f['bytes'], f['sha256'], f['git_blob'])
        assert entries[f['remote_path_at_target_commit']] == (f['mode'], ident['blob'])
        rel = Path(f['relative_to_target_task'])
        assert not rel.is_absolute() and '..' not in rel.parts
        (dest / rel).write_bytes(data)
        rows.append({'path': f['remote_path_at_target_commit'], 'mode': f['mode'], **ident})
    contracts = []
    for n in range(1, 6):
        shard = f'S{n:02}'
        q = load(shard)
        assert q['files'] == d['files']
        manifest = git('show', d['fixed_B8'] + ':planning/review-manifest-2026-09-19.md').splitlines(keepends=True)
        for row in q['physical_line_identities']:
            data = manifest[row['line'] - 1]
            assert (len(data), hashlib.sha256(data).hexdigest()) == (row['bytes'], row['sha256'])
        contracts.append({'id': shard, 'events': [e['id'] for e in q['events_all_fields']],
                          'lines': [p['line'] for p in q['physical_line_identities']],
                          'content_paragraphs': [p['line'] for p in q['paragraph_dispositions_all_fields'] if p['structure'] == 'content_paragraph'],
                          'readset': digest((ORIGINAL / f'split-contracts/{shard}.complete.json').read_bytes()),
                          'prompt': digest((ORIGINAL / f'split-contracts/{shard}.md').read_bytes())})
    receipt = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'contract': CONTRACT,
               'target_commit': commit, 'target_tree': d['target_checkout_tree'], 'target_task_tree': tree,
               'files': rows, 'set_exact': True, 'file_count': len(rows),
               'total_bytes': sum(r['bytes'] for r in rows), 'shards': contracts,
               'semantic_credit': 0, 'restored_code_executed': False}
    (TASK / 'input-identities.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k not in ['files', 'shards']}, ensure_ascii=False))

def events(shard, start, end):
    d = load(shard)
    lines = git('show', d['fixed_B8'] + ':planning/review-manifest-2026-09-19.md').decode().splitlines(keepends=True)
    for e in d['events_all_fields'][start:end]:
        print('\nEVENT', e['id'])
        common = ['read', 'purpose_review', 'effective_qualification', 'behavior_layer', 'acceptance_layer',
                  'identity_layer', 'workflow_layer', 'root_reception', 'not_claimed']
        first = load('S01')['events_all_fields'][0]
        assert all(e[k] == first[k] for k in common)
        print(json.dumps({k: v for k, v in e.items() if k not in common + ['primary_line_ids', 'content_paragraph_lines']}, ensure_ascii=False))
        for a, b in e['line_ranges']:
            for number in range(a, b + 1):
                print(f'LM-L{number}: {lines[number - 1]}', end='')

if __name__ == '__main__':
    if sys.argv[1] == 'recover':
        recover()
    elif sys.argv[1] == 'events':
        events(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
